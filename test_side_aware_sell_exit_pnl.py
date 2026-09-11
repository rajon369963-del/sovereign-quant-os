#!/usr/bin/env python3
"""V2.2 real-path BUY/SELL bracket-exit and realized-PnL regression battery.

Runs the production ExecutionDaemon.simulate_price_tick path against a temporary
SQLite ledger. No broker/network credentials or real-money execution are used.
"""

import sqlite3
import tempfile
from pathlib import Path

from execution_daemon import ExecutionDaemon, OrderState, TradeOrder


class StubRiskGate:
    def __init__(self):
        self.outcomes = []

    def record_trade_outcome(self, pnl):
        self.outcomes.append(pnl)


def make_order(order_id, side, *, fill, tp, sl, qty=2.0):
    return TradeOrder(
        order_id=order_id,
        symbol="NIFTY_FUT",
        strategy="V22_SIDE_REGRESSION",
        side=side,
        quantity=qty,
        entry_price=fill,
        hard_stop_loss=sl,
        hard_take_profit=tp,
        state=OrderState.FILLED,
        created_at=1.0,
        fill_price=fill,
    )


def read_trade(db_path, order_id):
    with sqlite3.connect(db_path) as conn:
        return conn.execute(
            "SELECT side, exit_price, realized_pnl, state FROM trades WHERE order_id = ?",
            (order_id,),
        ).fetchone()


def run_close_case(side, *, fill, tp, sl, tick, expected_exit, expected_pnl):
    with tempfile.TemporaryDirectory(prefix="air10_side_v22_") as td:
        db_path = str(Path(td) / "ledger.sqlite")
        daemon = ExecutionDaemon(
            db_path=db_path,
            initial_capital=10000.0,
            daily_loss_limit_pct=1.0,
            max_account_drawdown=1000000.0,
        )
        gate = StubRiskGate()
        order = make_order(f"CASE_{side}_{tick}", side, fill=fill, tp=tp, sl=sl)
        daemon.active_orders[order.order_id] = order

        daemon.simulate_price_tick(tick, gate)

        assert order.state == OrderState.CLOSED, (side, tick, order.state)
        assert order.exit_price == expected_exit, (side, order.exit_price, expected_exit)
        assert abs(order.realized_pnl - expected_pnl) < 1e-9, (
            side,
            order.realized_pnl,
            expected_pnl,
        )
        assert order.order_id not in daemon.active_orders
        assert daemon.completed_trades[-1].order_id == order.order_id
        assert abs(daemon.current_equity - (10000.0 + expected_pnl)) < 1e-9
        expected_loss = abs(expected_pnl) if expected_pnl < 0 else 0.0
        assert abs(daemon.daily_realized_loss - expected_loss) < 1e-9
        assert gate.outcomes == [expected_pnl]

        row = read_trade(db_path, order.order_id)
        assert row is not None
        db_side, db_exit, db_pnl, db_state = row
        assert db_side == side
        assert abs(db_exit - expected_exit) < 1e-9
        assert abs(db_pnl - expected_pnl) < 1e-9
        assert db_state == OrderState.CLOSED.value


def run_neutral_case(side, *, fill, tp, sl, tick):
    with tempfile.TemporaryDirectory(prefix="air10_side_neutral_v22_") as td:
        db_path = str(Path(td) / "ledger.sqlite")
        daemon = ExecutionDaemon(
            db_path=db_path,
            initial_capital=10000.0,
            daily_loss_limit_pct=1.0,
            max_account_drawdown=1000000.0,
        )
        gate = StubRiskGate()
        order = make_order(f"NEUTRAL_{side}", side, fill=fill, tp=tp, sl=sl)
        daemon.active_orders[order.order_id] = order

        daemon.simulate_price_tick(tick, gate)

        assert order.state == OrderState.FILLED
        assert order.order_id in daemon.active_orders
        assert daemon.current_equity == 10000.0
        assert daemon.daily_realized_loss == 0.0
        assert gate.outcomes == []
        assert read_trade(db_path, order.order_id) is None


def assert_known_bad_long_only_mutant_is_discriminated():
    """Prove these SELL fixtures would reject the previous long-only semantics."""

    def legacy_exit(fill, tp, sl, tick):
        if tick >= tp:
            return tp
        if tick <= sl:
            return sl
        return None

    # Correct short bracket: TP below fill, SL above fill.
    fill, tp, sl = 100.0, 90.0, 110.0
    assert legacy_exit(fill, tp, sl, 89.0) != tp, "Known-bad SELL-TP mutant unexpectedly passed"
    assert legacy_exit(fill, tp, sl, 111.0) != sl, "Known-bad SELL-SL mutant unexpectedly passed"

    # Previous PnL formula would report a profitable short exit as a loss.
    legacy_short_pnl = (tp - fill) * 2.0
    assert legacy_short_pnl < 0
    correct_short_pnl = (fill - tp) * 2.0
    assert correct_short_pnl > 0


def main():
    assert_known_bad_long_only_mutant_is_discriminated()

    # BUY no-regression controls.
    run_close_case(
        "BUY", fill=100.0, tp=110.0, sl=90.0, tick=111.0,
        expected_exit=110.0, expected_pnl=20.0,
    )
    run_close_case(
        "BUY", fill=100.0, tp=110.0, sl=90.0, tick=89.0,
        expected_exit=90.0, expected_pnl=-20.0,
    )

    # SELL V2.2 discriminating cases: TP direction, SL direction and PnL sign invert.
    run_close_case(
        "SELL", fill=100.0, tp=90.0, sl=110.0, tick=89.0,
        expected_exit=90.0, expected_pnl=20.0,
    )
    run_close_case(
        "SELL", fill=100.0, tp=90.0, sl=110.0, tick=111.0,
        expected_exit=110.0, expected_pnl=-20.0,
    )

    run_neutral_case("BUY", fill=100.0, tp=110.0, sl=90.0, tick=100.0)
    run_neutral_case("SELL", fill=100.0, tp=90.0, sl=110.0, tick=100.0)

    print("PASS: side-aware BUY/SELL exit and PnL real-path battery")


if __name__ == "__main__":
    main()
