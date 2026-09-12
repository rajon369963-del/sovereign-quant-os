from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Any

from live_broker_wire_bridge import LiveBrokerWireBridge, WireOrderPayload, WireState


@dataclass(frozen=True)
class VenueConstraintSnapshot:
    symbol: str
    venue: str
    tick_size: str
    qty_step: str
    min_qty: str
    revision: str
    min_notional: str | None = None


@dataclass(frozen=True)
class VenuePreflightDecision:
    allowed: bool
    code: str
    detail: str


def _positive_decimal(value: Any, field: str) -> Decimal:
    try:
        parsed = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"{field} is not a decimal") from exc
    if not parsed.is_finite() or parsed <= 0:
        raise ValueError(f"{field} must be finite and > 0")
    return parsed


def _multiple_of(value: Decimal, quantum: Decimal) -> bool:
    return value % quantum == 0


def validate_venue_order(
    order: WireOrderPayload,
    constraint: VenueConstraintSnapshot,
    *,
    validated_revision: str | None,
    send_boundary_revision: str | None,
) -> VenuePreflightDecision:
    """Fail-closed venue-grid/minimum court using decimal, revision-bound inputs."""
    if not constraint.revision:
        return VenuePreflightDecision(False, "HOLD_MISSING_SNAPSHOT_REVISION", "constraint snapshot has no revision")
    if not validated_revision or not send_boundary_revision:
        return VenuePreflightDecision(False, "HOLD_MISSING_BOUNDARY_REVISION", "validation/send-boundary revision required")
    if validated_revision != constraint.revision or send_boundary_revision != constraint.revision:
        return VenuePreflightDecision(
            False,
            "HOLD_STALE_CONSTRAINT_REVISION",
            f"snapshot={constraint.revision} validated={validated_revision} send={send_boundary_revision}",
        )
    if order.symbol != constraint.symbol or order.venue != constraint.venue:
        return VenuePreflightDecision(False, "HOLD_CONSTRAINT_IDENTITY_MISMATCH", "symbol/venue do not match snapshot")

    try:
        price = _positive_decimal(order.price, "price")
        quantity = _positive_decimal(order.quantity, "quantity")
        tick_size = _positive_decimal(constraint.tick_size, "tick_size")
        qty_step = _positive_decimal(constraint.qty_step, "qty_step")
        min_qty = _positive_decimal(constraint.min_qty, "min_qty")
        min_notional = (
            _positive_decimal(constraint.min_notional, "min_notional")
            if constraint.min_notional is not None
            else None
        )
    except ValueError as exc:
        return VenuePreflightDecision(False, "HOLD_INVALID_CONSTRAINT_OR_ORDER", str(exc))

    if not _multiple_of(price, tick_size):
        return VenuePreflightDecision(False, "REJECT_OFF_TICK", f"price={price} tick_size={tick_size}")
    if not _multiple_of(quantity, qty_step):
        return VenuePreflightDecision(False, "REJECT_OFF_QTY_STEP", f"quantity={quantity} qty_step={qty_step}")
    if quantity < min_qty:
        return VenuePreflightDecision(False, "REJECT_BELOW_MIN_QTY", f"quantity={quantity} min_qty={min_qty}")
    if min_notional is not None and price * quantity < min_notional:
        return VenuePreflightDecision(
            False,
            "REJECT_BELOW_MIN_NOTIONAL",
            f"notional={price * quantity} min_notional={min_notional}",
        )
    return VenuePreflightDecision(True, "PASS", "exact snapshot/grid/minimum checks passed")


class VenueConstrainedWireBridge(LiveBrokerWireBridge):
    """Opt-in bridge that makes venue preflight mandatory on this transmission path."""

    async def transmit_order(
        self,
        order: WireOrderPayload,
        *,
        constraint: VenueConstraintSnapshot,
        validated_revision: str | None,
        send_boundary_revision: str | None,
    ) -> WireOrderPayload:
        decision = validate_venue_order(
            order,
            constraint,
            validated_revision=validated_revision,
            send_boundary_revision=send_boundary_revision,
        )
        if not decision.allowed:
            order.wire_state = WireState.REJECTED
            order.rejection_reason = f"VENUE_PREFLIGHT_{decision.code}: {decision.detail}"
            inserted = self._sandwich_pre_commit(order)
            if not inserted:
                return self.lookup_order(order.cl_ord_id) or order
            return order
        return await super().transmit_order(order)
