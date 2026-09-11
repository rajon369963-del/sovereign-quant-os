import os
import sqlite3
import sys
import tempfile
import types
from enum import Enum

# Keep this regression hermetic: execution_daemon imports these modules, but this
# battery exercises only its real fill-fragment path and SQLite persistence.
alpha_stub = types.ModuleType("alpha_engine")
class SignalType(Enum):
    BUY = "BUY"
    SELL = "SELL"
class StrategyArchetype(Enum):
    TEST = "TEST"
class TradeSignal:
    pass
alpha_stub.TradeSignal = TradeSignal
alpha_stub.SignalType = SignalType
alpha_stub.StrategyArchetype = StrategyArchetype
sys.modules.setdefault("alpha_engine", alpha_stub)

risk_stub = types.ModuleType("risk_gatekeeper")
class RiskGatekeeper:
    pass
class RiskGateResult:
    pass
risk_stub.RiskGatekeeper = RiskGatekeeper
risk_stub.RiskGateResult = RiskGateResult
sys.modules.setdefault("risk_gatekeeper", risk_stub)

from execution_daemon import ExecutionDaemon, OrderState, TradeOrder


def make_order(order_id: str, quantity: float = 100.0) -> TradeOrder:
    return TradeOrder(
        order_id=order_id,
        symbol="NIFTY_FUT",
        strategy="TEST",
        side="BUY",
        quantity=quantity,
        entry_price=100.0,
        hard_stop_loss=90.0,
        hard_take_profit=120.0,
        state=OrderState.PENDING,
        created_at=1.0,
        remaining_quantity=quantity,
    )


def expect_raises(fn, message: str) -> None:
    try:
        fn()
    except ValueError:
        return
    raise AssertionError(message)


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "partial_fill.sqlite")
        daemon = ExecutionDaemon(db_path=db_path)
        order = make_order("ORD_PARTIAL_100")

        # Known-good first fragment: requested 100, actually filled 37.
        daemon.apply_fill_fragment(order, "E1", 37.0, 100.0, 1)
        assert order.state == OrderState.PARTIALLY_FILLED
        assert order.filled_quantity == 37.0
        assert order.remaining_quantity == 63.0
        assert order.fill_price == 100.0

        with sqlite3.connect(db_path) as conn:
            event_count = conn.execute("SELECT COUNT(*) FROM fill_events").fetchone()[0]
            state = conn.execute(
                "SELECT requested_quantity, filled_quantity, remaining_quantity, avg_fill_price, last_fill_sequence, state "
                "FROM order_fill_state WHERE order_id = ?",
                (order.order_id,),
            ).fetchone()
        assert event_count == 1
        assert state == (100.0, 37.0, 63.0, 100.0, 1, "PARTIALLY_FILLED")

        # Exact replay must be zero-delta and idempotent.
        daemon.apply_fill_fragment(order, "E1", 37.0, 100.0, 1)
        with sqlite3.connect(db_path) as conn:
            assert conn.execute("SELECT COUNT(*) FROM fill_events").fetchone()[0] == 1
        assert order.filled_quantity == 37.0
        assert order.remaining_quantity == 63.0

        # Same event ID with mutated payload must fail closed.
        expect_raises(
            lambda: daemon.apply_fill_fragment(order, "E1", 38.0, 100.0, 1),
            "mutated replay was accepted",
        )

        # Same event ID cannot be attached to another order.
        other = make_order("ORD_OTHER_100")
        expect_raises(
            lambda: daemon.apply_fill_fragment(other, "E1", 37.0, 100.0, 1),
            "cross-order event reuse was accepted",
        )

        # Non-contiguous sequence and overfill both fail closed.
        expect_raises(
            lambda: daemon.apply_fill_fragment(order, "E3", 10.0, 101.0, 3),
            "out-of-order fragment was accepted",
        )
        expect_raises(
            lambda: daemon.apply_fill_fragment(order, "E2_TOO_BIG", 64.0, 110.0, 2),
            "fragment exceeding remaining quantity was accepted",
        )

        # Second canonical fragment completes the request with deterministic VWAP.
        daemon.apply_fill_fragment(order, "E2", 63.0, 110.0, 2)
        assert order.state == OrderState.FILLED
        assert order.filled_quantity == 100.0
        assert order.remaining_quantity == 0.0
        assert abs(order.fill_price - 106.3) < 1e-12

        with sqlite3.connect(db_path) as conn:
            assert conn.execute("SELECT COUNT(*) FROM fill_events WHERE order_id = ?", (order.order_id,)).fetchone()[0] == 2
            final_state = conn.execute(
                "SELECT filled_quantity, remaining_quantity, avg_fill_price, last_fill_sequence, state "
                "FROM order_fill_state WHERE order_id = ?",
                (order.order_id,),
            ).fetchone()
        assert final_state == (100.0, 0.0, 106.3, 2, "FILLED")

        # Existing full-fill behavior remains a special case using the same primitive.
        full = make_order("ORD_FULL_50", 50.0)
        daemon.apply_fill_fragment(full, "FULL_E1", 50.0, 99.5, 1)
        assert full.state == OrderState.FILLED
        assert full.filled_quantity == 50.0
        assert full.remaining_quantity == 0.0
        assert full.fill_price == 99.5

        print("PASS: partial-fill event identity/idempotency SQLite battery")


if __name__ == "__main__":
    main()
