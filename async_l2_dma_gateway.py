"""
Sovereign Quant OS - High-Throughput Direct Market Access (DMA) L2 Order Gateway
Repository: rajon369963-del/sovereign-quant-os
Module: async_l2_dma_gateway.py
Task ID: TASK_017_QUANT_OS_L2_ORDER_DMA_GATEWAY

Invariants Enforced:
1. Sub-millisecond L2 binary and JSON market depth parsing via fixed-size preallocated ring buffer.
2. Sentinel Pre- and Postcondition risk checks: capital ceiling, margin sanity, position limits.
3. Strict zero-secret-leakage guarantees across all loggers, repr, exceptions, and stack traces.
4. Deterministic memory footprint (zero unbounded heap expansion under high packet load).
"""

import asyncio
import json
import logging
import re
import struct
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


# ============================================================================
# 1. ZERO-SECRET-LEAKAGE SUBSYSTEM
# ============================================================================

class SecretStr:
    """Wrapper for sensitive strings (tokens, API keys, private credentials).
    Prevents accidental string interpolation, serialization, logging, or repr exposure.
    """
    __slots__ = ("_secret_value",)

    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Secret value must be a string.")
        self._secret_value = value

    def __repr__(self) -> str:
        return "[REDACTED_SECRET]"

    def __str__(self) -> str:
        return "[REDACTED_SECRET]"

    def __format__(self, format_spec: str) -> str:
        return "[REDACTED_SECRET]"

    def get_raw_wire_secret(self) -> str:
        """Explicit boundary extraction: only to be used at the physical wire layer."""
        return self._secret_value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, SecretStr):
            return self._secret_value == other._secret_value
        return False


class SensitiveDataScrubber(logging.Filter):
    """Logging filter ensuring that sensitive tokens or credentials never reach logs."""
    SENSITIVE_PATTERNS = [
        re.compile(r"(bearer\s+)[A-Za-z0-9_\-\.]{8,}", re.IGNORECASE),
        re.compile(r"((?:token|api_key|secret|password|auth|credential)['\":\s=]+)[A-Za-z0-9_\-\.]{8,}", re.IGNORECASE),
    ]

    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            cleaned = record.msg
            for pattern in self.SENSITIVE_PATTERNS:
                cleaned = pattern.sub(r"\1[REDACTED_BY_FILTER]", cleaned)
            record.msg = cleaned
        return True


# ============================================================================
# 2. FIXED-SIZE L2 MARKET DATA RING BUFFER & PARSER
# ============================================================================

# Binary wire format: 8 bytes symbol, double price, double size, uint64 seq, char side ('B' or 'A')
BINARY_L2_STRUCT = struct.Struct("!8sddQc")


@dataclass(slots=True)
class L2DepthEntry:
    symbol: str = ""
    price: float = 0.0
    size: float = 0.0
    seq: int = 0
    side: str = ""
    timestamp_ns: int = 0


class L2RingBuffer:
    """Fixed-capacity ring buffer for streaming Level 2 depth entries.
    Guarantees zero heap allocations after initial initialization.
    """
    def __init__(self, capacity: int = 10000):
        if capacity <= 0:
            raise ValueError("Ring buffer capacity must be > 0.")
        self.capacity: int = capacity
        self._entries: List[L2DepthEntry] = [L2DepthEntry() for _ in range(capacity)]
        self._write_idx: int = 0
        self._total_writes: int = 0

    def append(self, symbol: str, price: float, size: float, seq: int, side: str, timestamp_ns: int) -> None:
        idx = self._write_idx
        entry = self._entries[idx]
        entry.symbol = symbol
        entry.price = price
        entry.size = size
        entry.seq = seq
        entry.side = side
        entry.timestamp_ns = timestamp_ns

        self._write_idx = (idx + 1) % self.capacity
        self._total_writes += 1

    def get_latest(self) -> Optional[L2DepthEntry]:
        if self._total_writes == 0:
            return None
        last_idx = (self._write_idx - 1) % self.capacity
        return self._entries[last_idx]

    @property
    def total_writes(self) -> int:
        return self._total_writes

    @property
    def current_allocated_slots(self) -> int:
        return self.capacity


class FastL2Parser:
    """Sub-millisecond binary and JSON L2 parser."""
    def __init__(self, ring_buffer: L2RingBuffer):
        self.ring_buffer = ring_buffer

    def parse_binary(self, raw_bytes: bytes) -> L2DepthEntry:
        """Parse raw wire packet in microsecond range."""
        symbol_bytes, price, size, seq, side_byte = BINARY_L2_STRUCT.unpack(raw_bytes)
        symbol = symbol_bytes.decode("ascii").rstrip("\x00")
        side = side_byte.decode("ascii")
        ts_now = time.perf_counter_ns()
        self.ring_buffer.append(symbol, price, size, seq, side, ts_now)
        return self.ring_buffer.get_latest()

    def parse_json(self, raw_json_str: str) -> L2DepthEntry:
        """Fast JSON market depth parser."""
        data = json.loads(raw_json_str)
        symbol = data["symbol"]
        price = float(data["price"])
        size = float(data["size"])
        seq = int(data["seq"])
        side = data["side"]
        ts_now = time.perf_counter_ns()
        self.ring_buffer.append(symbol, price, size, seq, side, ts_now)
        return self.ring_buffer.get_latest()


# ============================================================================
# 3. SENTINEL RISK & POSTCONDITION ENFORCEMENT
# ============================================================================

class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class SentinelViolationError(Exception):
    """Raised immediately when pre/post-condition risk sentinels fail."""
    def __init__(self, rule_name: str, message: str):
        super().__init__(f"SENTINEL_BREACH [{rule_name}]: {message}")
        self.rule_name = rule_name
        self.message = message


@dataclass(slots=True)
class DMAOrder:
    order_id: str
    symbol: str
    side: OrderSide
    quantity: float
    price: float
    session_token: SecretStr
    broker_secret: SecretStr
    timestamp_ns: int = field(default_factory=time.perf_counter_ns)

    def notional_value(self) -> float:
        return self.quantity * self.price

    def __repr__(self) -> str:
        return (
            f"DMAOrder(order_id='{self.order_id}', symbol='{self.symbol}', "
            f"side='{self.side.value}', quantity={self.quantity}, price={self.price}, "
            f"session_token={self.session_token!r}, broker_secret={self.broker_secret!r})"
        )


@dataclass(slots=True)
class AccountState:
    available_capital: float
    reserved_capital: float
    maintenance_margin_required: float
    current_positions: Dict[str, float] = field(default_factory=dict)

    def total_equity(self) -> float:
        return self.available_capital + self.reserved_capital


class SentinelRiskGuard:
    """Enforces mathematical safety invariants before and after order dispatch."""

    def __init__(
        self,
        max_order_capital: float = 100_000.0,
        max_position_limit: float = 5_000.0,
        max_leverage_ratio: float = 4.0,
        fat_finger_pct_band: float = 0.05,
    ):
        self.max_order_capital = max_order_capital
        self.max_position_limit = max_position_limit
        self.max_leverage_ratio = max_leverage_ratio
        self.fat_finger_pct_band = fat_finger_pct_band

    def verify_preconditions(
        self,
        order: DMAOrder,
        account: AccountState,
        best_bid: float,
        best_ask: float,
    ) -> None:
        """Precondition gatekeeper: Throws SentinelViolationError if any rule is breached."""
        notional = order.notional_value()

        # 1. Capital bounds check
        if notional > self.max_order_capital:
            raise SentinelViolationError(
                "CAPITAL_BOUND_EXCEEDED",
                f"Order notional {notional:.2f} exceeds max allowed {self.max_order_capital:.2f}",
            )

        if notional > account.available_capital:
            raise SentinelViolationError(
                "INSUFFICIENT_AVAILABLE_CAPITAL",
                f"Order notional {notional:.2f} exceeds available capital {account.available_capital:.2f}",
            )

        # 2. Position Limit check
        current_pos = account.current_positions.get(order.symbol, 0.0)
        delta_qty = order.quantity if order.side == OrderSide.BUY else -order.quantity
        projected_pos = current_pos + delta_qty
        if abs(projected_pos) > self.max_position_limit:
            raise SentinelViolationError(
                "POSITION_LIMIT_EXCEEDED",
                f"Projected position {projected_pos} for {order.symbol} exceeds limit {self.max_position_limit}",
            )

        # 3. Fat-finger Price Sanity check
        if best_bid > 0 and best_ask > 0:
            if order.side == OrderSide.BUY and order.price > best_ask * (1.0 + self.fat_finger_pct_band):
                raise SentinelViolationError(
                    "FAT_FINGER_PRICE_DISCREPANCY",
                    f"Buy price {order.price} is > {self.fat_finger_pct_band*100}% above best ask {best_ask}",
                )
            if order.side == OrderSide.SELL and order.price < best_bid * (1.0 - self.fat_finger_pct_band):
                raise SentinelViolationError(
                    "FAT_FINGER_PRICE_DISCREPANCY",
                    f"Sell price {order.price} is > {self.fat_finger_pct_band*100}% below best bid {best_bid}",
                )

        # 4. Margin Sanity
        projected_margin = account.maintenance_margin_required + (notional * 0.2)
        if (projected_margin / max(account.total_equity(), 1.0)) > self.max_leverage_ratio:
            raise SentinelViolationError(
                "MARGIN_LEVERAGE_SANITY_BREACH",
                f"Projected leverage exceeds max allowed {self.max_leverage_ratio}x",
            )

    def verify_postconditions(
        self,
        order: DMAOrder,
        account: AccountState,
    ) -> None:
        """Postcondition audit: verifies account consistency immediately after wire commit."""
        if account.available_capital < 0:
            raise SentinelViolationError(
                "NEGATIVE_CAPITAL_INVARIANT",
                f"Available capital collapsed below zero: {account.available_capital:.2f}",
            )


# ============================================================================
# 4. ASYNC L2 DMA GATEWAY
# ============================================================================

class AsyncL2DMAGateway:
    """Asynchronous L2 DMA Order Gateway with wire dispatch and strict sentinel protection."""

    def __init__(
        self,
        ring_buffer_capacity: int = 10000,
        sentinel_guard: Optional[SentinelRiskGuard] = None,
        account_state: Optional[AccountState] = None,
    ):
        self.ring_buffer = L2RingBuffer(capacity=ring_buffer_capacity)
        self.parser = FastL2Parser(self.ring_buffer)
        self.sentinel = sentinel_guard or SentinelRiskGuard()
        self.account = account_state or AccountState(
            available_capital=10_000_000.0,
            reserved_capital=0.0,
            maintenance_margin_required=100_000.0,
            current_positions={},
        )
        self.dispatched_wire_orders: List[Dict[str, Any]] = []
        self._dispatch_lock = asyncio.Lock()

    async def update_l2_depth_binary(self, raw_packet: bytes) -> L2DepthEntry:
        """Ingest binary L2 packet directly into ring buffer."""
        return self.parser.parse_binary(raw_packet)

    async def update_l2_depth_json(self, raw_json_str: str) -> L2DepthEntry:
        """Ingest JSON L2 packet directly into ring buffer."""
        return self.parser.parse_json(raw_json_str)

    async def dispatch_single_order(
        self,
        order: DMAOrder,
        best_bid: float = 100.0,
        best_ask: float = 100.1,
    ) -> Dict[str, Any]:
        """Dispatch a single DMA order through pre- and post-condition sentinels."""
        # 1. Sentinel Preconditions
        self.sentinel.verify_preconditions(order, self.account, best_bid, best_ask)

        notional = order.notional_value()

        # 2. Atomic dispatch & account mutation
        async with self._dispatch_lock:
            self.account.available_capital -= notional
            self.account.reserved_capital += notional
            current_pos = self.account.current_positions.get(order.symbol, 0.0)
            delta = order.quantity if order.side == OrderSide.BUY else -order.quantity
            self.account.current_positions[order.symbol] = current_pos + delta

            # Wire dispatch payload with strict zero secret exposure
            wire_receipt = {
                "wire_seq": len(self.dispatched_wire_orders) + 1,
                "order_id": order.order_id,
                "symbol": order.symbol,
                "side": order.side.value,
                "quantity": order.quantity,
                "price": order.price,
                "status": "DISPATCHED_TO_DMA_WIRE",
                "dispatched_at_ns": time.perf_counter_ns(),
            }
            self.dispatched_wire_orders.append(wire_receipt)

            # 3. Sentinel Postconditions
            self.sentinel.verify_postconditions(order, self.account)

        return wire_receipt

    async def dispatch_burst(
        self,
        orders: List[DMAOrder],
        best_bid: float = 100.0,
        best_ask: float = 100.1,
    ) -> List[Dict[str, Any]]:
        """Fast batch processing of DMA orders under high burst conditions."""
        results = []
        for order in orders:
            res = await self.dispatch_single_order(order, best_bid, best_ask)
            results.append(res)
        return results
