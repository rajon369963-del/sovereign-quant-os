"""
Sovereign Quant OS - Execution Kernel Stress, Wire Idempotency & Reconnect Watchdog
Repository: rajon369963-del/sovereign-quant-os
Module: execution_kernel_stress.py
Task ID: TASK_016_QUANT_OS_STRESS_SCENARIOS
"""

import asyncio
import logging
import re
import sqlite3
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Set


# ============================================================================
# 1. SECRET MASKING SUBSYSTEM
# ============================================================================

class SecretStr:
    """Wrapper ensuring zero secret exposure in repr, str, format, or traces."""
    __slots__ = ("_val",)

    def __init__(self, val: str):
        if not isinstance(val, str):
            raise TypeError("Secret value must be a string.")
        self._val = val

    def __repr__(self) -> str:
        return "[REDACTED_SECRET]"

    def __str__(self) -> str:
        return "[REDACTED_SECRET]"

    def __format__(self, format_spec: str) -> str:
        return "[REDACTED_SECRET]"

    def get_raw_wire_secret(self) -> str:
        return self._val


# ============================================================================
# 2. DATA MODELS & ENUMS
# ============================================================================

class ConnectionState(str, Enum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
    RECONNECTING = "RECONNECTING"


class OrderState(str, Enum):
    PENDING = "PENDING"
    IN_FLIGHT = "IN_FLIGHT"
    COMMITTED = "COMMITTED"
    REJECTED = "REJECTED"


@dataclass(slots=True)
class StressOrder:
    cl_ord_id: str
    symbol: str
    quantity: float
    price: float
    side: str
    session_token: SecretStr
    timestamp_ns: int = field(default_factory=time.perf_counter_ns)

    def __repr__(self) -> str:
        return (
            f"StressOrder(cl_ord_id='{self.cl_ord_id}', symbol='{self.symbol}', "
            f"qty={self.quantity}, price={self.price}, side='{self.side}', "
            f"token={self.session_token!r})"
        )


# ============================================================================
# 3. PRIORITY TOKEN BUCKET & FRICTION GATE
# ============================================================================

class PriorityTokenBucket:
    """High-throughput rate limiter with latency friction backoff."""

    def __init__(self, rate: float = 100000.0, capacity: float = 50000.0):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_update = time.perf_counter()
        self.friction_active = False

    def allow(self, simulated_latency_ms: float = 0.0) -> bool:
        now = time.perf_counter()
        elapsed = now - self.last_update
        self.last_update = now

        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)

        if simulated_latency_ms > 10.0:
            self.friction_active = True
            self.tokens = min(self.tokens, self.capacity * 0.25)
        else:
            self.friction_active = False

        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False


# ============================================================================
# 4. EXECUTION KERNEL & IDEMPOTENCY BARRIER
# ============================================================================

class ExecutionKernel:
    """DMA Execution Kernel managing wire dispatches, idempotency barriers, and reconnects."""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self._conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_sqlite_wal()
        self.conn_state = ConnectionState.CONNECTED
        self.rate_limiter = PriorityTokenBucket()
        self.wire_dispatch_count = 0
        self.dispatched_cl_ord_ids: Set[str] = set()
        self.cached_receipts: Dict[str, Dict[str, Any]] = {}
        self._lock = asyncio.Lock()
        self.disconnect_event_count = 0
        self.reconnect_event_count = 0

    def _init_sqlite_wal(self) -> None:
        """Initialize SQLite database for state sandwich commits."""
        if self.db_path != ":memory:":
            self._conn.execute("PRAGMA journal_mode=WAL;")
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS order_journal (
                cl_ord_id TEXT PRIMARY KEY,
                symbol TEXT NOT NULL,
                quantity REAL NOT NULL,
                price REAL NOT NULL,
                state TEXT NOT NULL,
                dispatched_at_ns INTEGER NOT NULL,
                wire_seq INTEGER
            );
        """)
        self._conn.commit()

    async def simulate_network_disconnect(self) -> None:
        """Simulate unexpected TCP socket drop."""
        async with self._lock:
            self.conn_state = ConnectionState.DISCONNECTED
            self.disconnect_event_count += 1

    async def reconnect_watchdog(self) -> None:
        """Watchdog to safely recover link without corrupting in-flight state."""
        async with self._lock:
            if self.conn_state == ConnectionState.DISCONNECTED:
                self.conn_state = ConnectionState.RECONNECTING
                await asyncio.sleep(0.001)
                self.conn_state = ConnectionState.CONNECTED
                self.reconnect_event_count += 1

    async def dispatch_order(
        self,
        order: StressOrder,
        simulated_latency_ms: float = 0.5,
    ) -> Dict[str, Any]:
        """Atomic idempotent dispatch pipeline."""
        async with self._lock:
            # 1. Idempotency Barrier Check (Zero Duplicate Execution)
            if order.cl_ord_id in self.dispatched_cl_ord_ids:
                cached = self.cached_receipts[order.cl_ord_id]
                return {
                    "cl_ord_id": order.cl_ord_id,
                    "status": "IDEMPOTENT_DUPLICATE_IGNORED",
                    "wire_dispatched": False,
                    "original_wire_seq": cached["wire_seq"],
                }

            # 2. Network Connectivity & Watchdog
            if self.conn_state != ConnectionState.CONNECTED:
                self.conn_state = ConnectionState.RECONNECTING
                self.conn_state = ConnectionState.CONNECTED
                self.reconnect_event_count += 1

            # 3. Rate Throttling & Noise Friction Gate
            if not self.rate_limiter.allow(simulated_latency_ms):
                return {
                    "cl_ord_id": order.cl_ord_id,
                    "status": "RATE_LIMITED_BACKOFF",
                    "wire_dispatched": False,
                }

            # 4. State Sandwich Pre-Commit
            self.wire_dispatch_count += 1
            wire_seq = self.wire_dispatch_count
            now_ns = time.perf_counter_ns()

            self._conn.execute(
                "INSERT INTO order_journal (cl_ord_id, symbol, quantity, price, state, dispatched_at_ns, wire_seq) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (order.cl_ord_id, order.symbol, order.quantity, order.price, OrderState.COMMITTED.value, now_ns, wire_seq),
            )
            self._conn.commit()

            # 5. Wire Dispatch Record
            receipt = {
                "cl_ord_id": order.cl_ord_id,
                "symbol": order.symbol,
                "status": "COMMITTED_TO_WIRE",
                "wire_dispatched": True,
                "wire_seq": wire_seq,
                "dispatched_at_ns": now_ns,
            }
            self.dispatched_cl_ord_ids.add(order.cl_ord_id)
            self.cached_receipts[order.cl_ord_id] = receipt

            return receipt

    def get_journal_order_count(self, cl_ord_id: str) -> int:
        cur = self._conn.execute("SELECT count(*) FROM order_journal WHERE cl_ord_id = ?", (cl_ord_id,))
        return cur.fetchone()[0]

    def close(self) -> None:
        self._conn.close()
