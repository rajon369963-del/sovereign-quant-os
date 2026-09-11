"""V2.2 real-path regression battery for circuit-breaker durability.

This battery deliberately calls ExecutionDaemon.check_circuit_breaker(), not a helper
facsimile. A log-only breaker implementation must fail because the assertions require
per-order durable HOLD truth, same-EFFECT idempotency, and restart reconstruction.
No broker/network/live-money path is used.
"""

import sqlite3
import tempfile
import time
from pathlib import Path

from execution_daemon import ExecutionDaemon, OrderState, TradeOrder


def count_rows(db_path: str, table: str) -> int:
    with sqlite3.connect(db_path) as conn:
        return conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]


def make_filled_order(order_id: str) -> TradeOrder:
    return TradeOrder(
        order_id=order_id,
        symbol="NIFTY_FUT",
        strategy="TEST_ONLY",
        side="BUY",
        quantity=1.0,
        entry_price=100.0,
        hard_stop_loss=95.0,
        hard_take_profit=105.0,
        state=OrderState.FILLED,
        created_at=time.time(),
        fill_price=100.0,
    )


def exercise_active_order_hold_and_restart() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        db_path = str(Path(tmp) / "breaker.sqlite")
        daemon = ExecutionDaemon(
            db_path=db_path,
            max_account_drawdown=10.0,
            initial_capital=1000.0,
        )
        order = make_filled_order("ORD_BREAKER_001")
        daemon.active_orders[order.order_id] = order
        daemon.peak_equity = 1000.0
        daemon.current_equity = 980.0
        effect_id = "EFFECT-TEST-BREAKER-001"

        # Exact production path: threshold check -> _trigger_kill_switch.
        assert daemon.check_circuit_breaker(effect_id=effect_id) is False
        assert daemon.is_circuit_broken is True
        assert order.order_id in daemon.active_orders, "breaker must not silently delete unresolved order state"
        assert order.state is OrderState.FILLED, "no external ACK exists, so CLOSED must not be invented"

        obligations = daemon.get_unresolved_breaker_obligations()
        assert len(obligations) == 1
        obligation = obligations[0]
        assert obligation["effect_id"] == effect_id
        assert obligation["order_id"] == order.order_id
        assert obligation["pre_state"] == "FILLED"
        assert obligation["unwind_action"] == "HOLD_FOR_AUTHORITATIVE_RECONCILIATION"
        assert obligation["ack_state"] == "UNKNOWN"
        assert obligation["reconciled_state"] == "HOLD_RECONCILE_REQUIRED"
        assert obligation["retry_allowed"] == 0
        assert count_rows(db_path, "circuit_breaker_effects") == 1
        assert count_rows(db_path, "circuit_breaker_events") == 1
        assert count_rows(db_path, "breaker_unwind_outcomes") == 1

        # Same EFFECT_ID replay must not duplicate event/outcome rows.
        assert daemon.check_circuit_breaker(effect_id=effect_id) is False
        assert count_rows(db_path, "circuit_breaker_effects") == 1
        assert count_rows(db_path, "circuit_breaker_events") == 1
        assert count_rows(db_path, "breaker_unwind_outcomes") == 1

        # Restart readback must preserve the safety fence and unresolved obligation.
        restarted = ExecutionDaemon(
            db_path=db_path,
            max_account_drawdown=10.0,
            initial_capital=1000.0,
        )
        assert restarted.is_circuit_broken is True
        restarted_obligations = restarted.get_unresolved_breaker_obligations()
        assert len(restarted_obligations) == 1
        assert restarted_obligations[0]["order_id"] == order.order_id
        assert restarted_obligations[0]["reconciled_state"] == "HOLD_RECONCILE_REQUIRED"


def exercise_no_active_order_known_good() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        db_path = str(Path(tmp) / "breaker-empty.sqlite")
        daemon = ExecutionDaemon(
            db_path=db_path,
            max_account_drawdown=10.0,
            initial_capital=1000.0,
        )
        daemon.peak_equity = 1000.0
        daemon.current_equity = 980.0

        assert daemon.check_circuit_breaker(effect_id="EFFECT-TEST-BREAKER-EMPTY") is False
        assert daemon.is_circuit_broken is True
        assert count_rows(db_path, "circuit_breaker_effects") == 1
        assert count_rows(db_path, "circuit_breaker_events") == 1
        assert count_rows(db_path, "breaker_unwind_outcomes") == 0

        restarted = ExecutionDaemon(db_path=db_path, initial_capital=1000.0)
        assert restarted.is_circuit_broken is True


def main() -> None:
    exercise_active_order_hold_and_restart()
    exercise_no_active_order_known_good()
    print("PASS: circuit breaker durable reconciliation real-path battery")


if __name__ == "__main__":
    main()
