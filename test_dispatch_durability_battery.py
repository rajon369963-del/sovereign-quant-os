import os
import sqlite3
import sys
import tempfile
import types

# execution_daemon imports alpha_engine, whose scan_all_bars type annotation references
# polars.DataFrame. Dispatch durability itself does not execute any Polars behavior, and
# the repo's CI requirements do not install Polars. Provide only the import/type surface
# needed to reach the exact production dispatch path without adding a new runtime wheel.
if "polars" not in sys.modules:
    polars_stub = types.ModuleType("polars")
    polars_stub.DataFrame = object
    sys.modules["polars"] = polars_stub

from alpha_engine import SignalType, StrategyArchetype, TradeSignal
from execution_daemon import ExecutionDaemon, OrderState
from risk_gatekeeper import RiskGatekeeper, RiskGateResult


def make_signal() -> TradeSignal:
    return TradeSignal(
        bar_id=1,
        timestamp=1.0,
        strategy=StrategyArchetype.MEAN_REVERSION,
        signal_type=SignalType.BUY,
        price=100.0,
        stop_loss=99.0,
        take_profit=103.0,
        risk_reward_ratio=3.0,
        confidence=0.9,
    )


def make_gate() -> RiskGateResult:
    return RiskGateResult(
        passed=True,
        reason="test",
        approved_quantity=2.0,
        risk_amount=2.0,
        hard_stop_loss=99.0,
        hard_take_profit=103.0,
    )


def durable_count(db_path: str, order_id: str) -> int:
    with sqlite3.connect(db_path) as conn:
        return conn.execute("SELECT COUNT(*) FROM trades WHERE order_id = ?", (order_id,)).fetchone()[0]


def test_dispatch_is_durable_before_return_and_after_restart() -> None:
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "ledger.sqlite")
        daemon = ExecutionDaemon(db_path=db_path)
        order = daemon.dispatch_order_with_self_healing(make_signal(), make_gate())
        assert order is not None
        assert order.state == OrderState.FILLED
        assert durable_count(db_path, order.order_id) == 1

        row = daemon.read_durable_order(order.order_id)
        assert row is not None
        assert row["order_id"] == order.order_id
        assert row["state"] == "FILLED"
        assert row["quantity"] == order.quantity
        assert row["fill_price"] == order.fill_price

        restarted = ExecutionDaemon(db_path=db_path)
        row_after_restart = restarted.read_durable_order(order.order_id)
        assert row_after_restart is not None
        assert row_after_restart["state"] == "FILLED"
        assert row_after_restart["fill_price"] == order.fill_price
        assert restarted.active_orders == {}
        assert restarted.lifecycle_hold_reason == "HOLD_RECONCILIATION_REQUIRED"
        assert restarted._refresh_reconciliation_hold() == "HOLD_RECONCILIATION_REQUIRED"
        assert restarted.dispatch_order_with_self_healing(make_signal(), make_gate()) is None


def test_dispatch_fails_closed_when_durable_readback_is_bypassed() -> None:
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "ledger.sqlite")
        daemon = ExecutionDaemon(db_path=db_path)
        daemon._persist_order_with_readback = lambda order: False
        order = daemon.dispatch_order_with_self_healing(make_signal(), make_gate())
        assert order is None
        with sqlite3.connect(db_path) as conn:
            count = conn.execute("SELECT COUNT(*) FROM trades").fetchone()[0]
        assert count == 0
        assert daemon.active_orders == {}


def test_known_bad_old_shape_is_detected() -> None:
    """Known bad: memory FILLED with no durable row must never satisfy the new court."""
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "ledger.sqlite")
        daemon = ExecutionDaemon(db_path=db_path)
        signal = make_signal()
        gate = make_gate()

        order = daemon.dispatch_order_with_self_healing(signal, gate)
        assert order is not None
        with sqlite3.connect(db_path) as conn:
            conn.execute("DELETE FROM trades WHERE order_id = ?", (order.order_id,))
        assert order.state == OrderState.FILLED
        assert order.order_id in daemon.active_orders
        assert daemon.read_durable_order(order.order_id) is None


def test_close_persistence_failure_cannot_promote_process_or_risk_state() -> None:
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "ledger.sqlite")
        daemon = ExecutionDaemon(db_path=db_path)
        gate = RiskGatekeeper()
        order = daemon.dispatch_order_with_self_healing(make_signal(), make_gate())
        assert order is not None

        original_persist = daemon._persist_order_with_readback
        daemon._persist_order_with_readback = (
            lambda candidate: False if candidate.state == OrderState.CLOSED else original_persist(candidate)
        )

        before_equity = daemon.current_equity
        before_peak = daemon.peak_equity
        before_daily_loss = daemon.daily_realized_loss
        before_gate = (
            gate.account_equity,
            gate.current_scale_step,
            gate.consecutive_wins,
            gate.profit_buffer,
        )

        try:
            daemon.simulate_price_tick(104.0, gate)
        except RuntimeError as exc:
            assert str(exc).startswith("CLOSE_LEDGER_READBACK_FAILED:")
        else:
            raise AssertionError("close persistence failure must fail closed")

        assert order.order_id in daemon.active_orders
        assert daemon.active_orders[order.order_id].state == OrderState.FILLED
        assert daemon.completed_trades == []
        assert daemon.current_equity == before_equity
        assert daemon.peak_equity == before_peak
        assert daemon.daily_realized_loss == before_daily_loss
        assert (
            gate.account_equity,
            gate.current_scale_step,
            gate.consecutive_wins,
            gate.profit_buffer,
        ) == before_gate
        durable = daemon.read_durable_order(order.order_id)
        assert durable is not None
        assert durable["state"] == OrderState.FILLED.value


def test_successful_close_persists_before_promotion_and_closed_restart_is_ready() -> None:
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "ledger.sqlite")
        daemon = ExecutionDaemon(db_path=db_path)
        gate = RiskGatekeeper()
        order = daemon.dispatch_order_with_self_healing(make_signal(), make_gate())
        assert order is not None

        daemon.simulate_price_tick(104.0, gate)

        assert order.order_id not in daemon.active_orders
        assert len(daemon.completed_trades) == 1
        closed = daemon.completed_trades[0]
        assert closed.order_id == order.order_id
        assert closed.state == OrderState.CLOSED
        durable = daemon.read_durable_order(order.order_id)
        assert durable is not None
        assert durable["state"] == OrderState.CLOSED.value
        assert durable["realized_pnl"] == closed.realized_pnl
        assert daemon.current_equity > daemon.initial_capital
        assert gate.current_scale_step == 2

        restarted = ExecutionDaemon(db_path=db_path)
        assert restarted.lifecycle_hold_reason is None
        assert restarted.active_orders == {}
        assert restarted._refresh_reconciliation_hold() is None


def main() -> None:
    test_dispatch_is_durable_before_return_and_after_restart()
    test_dispatch_fails_closed_when_durable_readback_is_bypassed()
    test_known_bad_old_shape_is_detected()
    test_close_persistence_failure_cannot_promote_process_or_risk_state()
    test_successful_close_persists_before_promotion_and_closed_restart_is_ready()
    print("DISPATCH_DURABILITY_COURT=PASS_BOUNDED")
    print("CLOSE_PERSIST_BEFORE_PROMOTE_COURT=PASS_BOUNDED")
    print("RESTART_RECONCILIATION_FENCE_COURT=PASS_BOUNDED")


if __name__ == "__main__":
    main()
