import asyncio
import tempfile
import unittest
from pathlib import Path

from live_broker_wire_bridge import WireMode, WireOrderPayload, WireState
from venue_constraint_preflight import (
    VenueConstraintSnapshot,
    VenueConstrainedWireBridge,
    validate_venue_order,
)


def order(price=0.015, quantity=0.10):
    return WireOrderPayload(
        cl_ord_id="preflight-1", symbol="BTCUSD", venue="TEST", side="BUY",
        price=price, quantity=quantity, order_type="LIMIT"
    )


def snapshot(**overrides):
    data = dict(symbol="BTCUSD", venue="TEST", tick_size="0.005", qty_step="0.01",
                min_qty="0.05", min_notional="0.001", revision="rev-7")
    data.update(overrides)
    return VenueConstraintSnapshot(**data)


class VenueConstraintUnitTests(unittest.TestCase):
    def decision(self, candidate, snap=None, validated="rev-7", send="rev-7"):
        return validate_venue_order(candidate, snap or snapshot(),
                                    validated_revision=validated, send_boundary_revision=send)

    def test_on_grid_passes_unchanged(self):
        candidate = order()
        result = self.decision(candidate)
        self.assertTrue(result.allowed)
        self.assertEqual((candidate.price, candidate.quantity), (0.015, 0.10))

    def test_non_power_of_ten_tick_rejects(self):
        result = self.decision(order(price=0.014))
        self.assertFalse(result.allowed)
        self.assertEqual(result.code, "REJECT_OFF_TICK")

    def test_qty_step_and_minimums_fail_closed(self):
        self.assertEqual(self.decision(order(quantity=0.105)).code, "REJECT_OFF_QTY_STEP")
        self.assertEqual(self.decision(order(quantity=0.04)).code, "REJECT_BELOW_MIN_QTY")
        self.assertEqual(self.decision(order(price=0.005, quantity=0.05), snapshot(min_notional="0.001")).code,
                         "REJECT_BELOW_MIN_NOTIONAL")

    def test_tiny_decimals_do_not_use_binary_modulo(self):
        tiny = snapshot(tick_size="0.00000005", qty_step="0.00000001", min_qty="0.00000001", min_notional=None)
        result = self.decision(order(price=0.00000015, quantity=0.00000003), tiny)
        self.assertTrue(result.allowed)

    def test_revision_and_identity_holds(self):
        self.assertEqual(self.decision(order(), validated="rev-6").code, "HOLD_STALE_CONSTRAINT_REVISION")
        self.assertEqual(self.decision(order(), send=None).code, "HOLD_MISSING_BOUNDARY_REVISION")
        self.assertEqual(self.decision(order(), snapshot(venue="OTHER")).code, "HOLD_CONSTRAINT_IDENTITY_MISMATCH")


class VenueConstraintIntegrationTests(unittest.TestCase):
    def test_rejection_is_audited_and_wire_delta_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            bridge = VenueConstrainedWireBridge(Path(tmp) / "wire.db", mode=WireMode.TESTNET_MOCK)
            candidate = order(price=0.014)
            before = bridge.total_wire_sent
            result = asyncio.run(bridge.transmit_order(candidate, constraint=snapshot(),
                                                       validated_revision="rev-7", send_boundary_revision="rev-7"))
            self.assertEqual(result.wire_state, WireState.REJECTED)
            self.assertEqual(bridge.total_wire_sent - before, 0)
            audited = bridge.lookup_order(candidate.cl_ord_id)
            self.assertIsNotNone(audited)
            self.assertIn("VENUE_PREFLIGHT_REJECT_OFF_TICK", audited.rejection_reason)

    def test_valid_testnet_mock_uses_existing_wire_path_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            bridge = VenueConstrainedWireBridge(Path(tmp) / "wire.db", mode=WireMode.TESTNET_MOCK)
            candidate = order()
            before = bridge.total_wire_sent
            result = asyncio.run(bridge.transmit_order(candidate, constraint=snapshot(),
                                                       validated_revision="rev-7", send_boundary_revision="rev-7"))
            self.assertEqual(bridge.total_wire_sent - before, 1)
            self.assertNotEqual(result.wire_state, WireState.REJECTED)


if __name__ == "__main__":
    unittest.main()
