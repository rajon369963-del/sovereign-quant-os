#!/usr/bin/env python3
"""V2.2 real-path court for daily-risk session + policy persistence.

The fixture runs the production ExecutionDaemon close path against temporary SQLite,
then reopens the DB to verify same-session reconstruction, next-session rollover,
and fail-closed same-session policy drift.  No broker/network/live-money path exists.
"""

from __future__ import annotations

import os
import sqlite3
import sys
import tempfile
import types
from enum import Enum


# Keep the court hermetic: execution_daemon only needs these interfaces here.
alpha = types.ModuleType("alpha_engine")


class SignalType(Enum):
    BUY = "BUY"
    SELL = "SELL"


class StrategyArchetype(Enum):
    TEST = "TEST"


class TradeSignal:
    pass


alpha.SignalType = SignalType
alpha.StrategyArchetype = StrategyArchetype
alpha.TradeSignal = TradeSignal
sys.modules["alpha_engine"] = alpha

risk = types.ModuleType("risk_gatekeeper")


class RiskGateResult:
    pass


class RiskGatekeeper:
    def __init__(self):
        self.outcomes = []

    def record_trade_outcome(self, pnl):
        self.outcomes.append(float(pnl))


risk.RiskGateResult = RiskGateResult
risk.RiskGatekeeper = RiskGatekeeper
sys.modules["risk_gatekeeper"] = risk

from daily_risk_session import RiskPolicyConflict
from execution_daemon import ExecutionDaemon, OrderState, TradeOrder


def loss_order(order_id: str, quantity: float) -> TradeOrder:
    return TradeOrder(
        order_id=order_id,
        symbol="NIFTY_FUT",
        strategy="TEST",
        side="BUY",
        quantity=float(quantity),
        entry_price=100.0,
        hard_stop_loss=90.0,
        hard_take_profit=110.0,
        state=OrderState.FILLED,
        created_at=1.0,
        fill_price=100.0,
        filled_quantity=float(quantity),
        remaining_quantity=0.0,
        last_fill_sequence=1,
    )


def assert_close(a, b, eps=1e-9):
    assert abs(float(a) - float(b)) <= eps, (a, b)


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = os.path.join(td, "ledger.sqlite")
        session = {"id": "D1"}
        provider = lambda: session["id"]
        gate = RiskGatekeeper()

        # D1: realize 150 loss through the actual simulate_price_tick close path.
        d1 = ExecutionDaemon(
            db_path=db,
            initial_capital=10000.0,
            daily_loss_limit_pct=0.02,
            session_id_provider=provider,
            session_policy_id="TEST_SESSION_V1",
        )
        o1 = loss_order("D1_LOSS_150", 15.0)
        d1.active_orders[o1.order_id] = o1
        d1.simulate_price_tick(89.0, gate)
        assert_close(d1.daily_realized_loss, 150.0)
        assert d1.is_circuit_broken is False

        # Same-session restart MUST reconstruct 150, not reset to zero.
        d1_restart = ExecutionDaemon(
            db_path=db,
            initial_capital=10000.0,
            daily_loss_limit_pct=0.02,
            session_id_provider=provider,
            session_policy_id="TEST_SESSION_V1",
        )
        assert_close(d1_restart.daily_realized_loss, 150.0)
        assert_close(d1_restart.daily_loss_limit, 200.0)

        # Another 60 loss in D1 makes cumulative session loss 210 and trips.
        o2 = loss_order("D1_LOSS_60", 6.0)
        d1_restart.active_orders[o2.order_id] = o2
        d1_restart.simulate_price_tick(89.0, gate)
        assert_close(d1_restart.daily_realized_loss, 210.0)
        assert d1_restart.is_circuit_broken is True

        # DB readback is authoritative and restart reproduces breaker state.
        with sqlite3.connect(db) as conn:
            row = conn.execute(
                "SELECT session_id, session_policy_id, policy_sha256, starting_baseline, "
                "daily_loss_limit_pct, daily_loss_limit_amount, realized_loss, breaker_state, "
                "state_schema_version FROM daily_risk_session_state WHERE session_id='D1'"
            ).fetchone()
        assert row is not None
        assert row[0] == "D1"
        assert row[1] == "TEST_SESSION_V1"
        assert len(row[2]) == 64
        assert_close(row[3], 10000.0)
        assert_close(row[4], 0.02)
        assert_close(row[5], 200.0)
        assert_close(row[6], 210.0)
        assert row[7] == 1
        assert row[8] == "daily_risk_session_v1"

        d1_again = ExecutionDaemon(
            db_path=db,
            initial_capital=10000.0,
            daily_loss_limit_pct=0.02,
            session_id_provider=provider,
            session_policy_id="TEST_SESSION_V1",
        )
        assert_close(d1_again.daily_realized_loss, 210.0)
        assert d1_again.is_circuit_broken is True

        # Same authoritative session + changed threshold MUST fail closed rather
        # than silently reinterpret persisted 210 under a new constructor policy.
        try:
            ExecutionDaemon(
                db_path=db,
                initial_capital=10000.0,
                daily_loss_limit_pct=0.01,
                session_id_provider=provider,
                session_policy_id="TEST_SESSION_V1",
            )
        except RiskPolicyConflict:
            pass
        else:
            raise AssertionError("same-session policy pct drift was silently accepted")

        # Same session + changed baseline must also fail closed, even if the pct is unchanged.
        try:
            ExecutionDaemon(
                db_path=db,
                initial_capital=20000.0,
                daily_loss_limit_pct=0.02,
                session_id_provider=provider,
                session_policy_id="TEST_SESSION_V1",
            )
        except RiskPolicyConflict:
            pass
        else:
            raise AssertionError("same-session baseline drift was silently accepted")

        # Only the injected authoritative session identity changes. D2 starts clean,
        # while D1 stays durable/auditable in the same SQLite ledger.
        session["id"] = "D2"
        d2 = ExecutionDaemon(
            db_path=db,
            initial_capital=10000.0,
            daily_loss_limit_pct=0.02,
            session_id_provider=provider,
            session_policy_id="TEST_SESSION_V1",
        )
        assert d2.current_session_id == "D2"
        assert_close(d2.daily_realized_loss, 0.0)
        assert d2.is_circuit_broken is False
        with sqlite3.connect(db) as conn:
            rows = conn.execute(
                "SELECT session_id, realized_loss, breaker_state FROM daily_risk_session_state ORDER BY session_id"
            ).fetchall()
        assert rows == [("D1", 210.0, 1), ("D2", 0.0, 0)], rows

        # Cumulative drawdown configuration remains a separate contract.
        assert_close(d2.max_account_drawdown, 10000.0)
        assert_close(d2.current_equity, 10000.0)
        assert_close(d2.peak_equity, 10000.0)

    print("PASS: daily-risk session restart/rollover/policy-binding real-path court")


if __name__ == "__main__":
    main()
