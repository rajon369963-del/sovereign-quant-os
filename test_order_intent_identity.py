import os
import sqlite3
import sys
import tempfile
import types
from enum import Enum

# Hermetic imports: exercise the real ExecutionDaemon dispatch/fill/SQLite path
# without pulling unrelated alpha/risk dependencies into this focused court.
alpha_stub = types.ModuleType("alpha_engine")
class SignalType(Enum):
    BUY = "BUY"
    SELL = "SELL"
class StrategyArchetype(Enum):
    TEST = "TEST_STRATEGY"
class TradeSignal:
    def __init__(self, *, price=100.0, side=SignalType.BUY, strategy=StrategyArchetype.TEST):
        self.price = price
        self.signal_type = side
        self.strategy = strategy
alpha_stub.TradeSignal = TradeSignal
alpha_stub.SignalType = SignalType
alpha_stub.StrategyArchetype = StrategyArchetype
sys.modules.setdefault("alpha_engine", alpha_stub)

risk_stub = types.ModuleType("risk_gatekeeper")
class RiskGatekeeper:
    pass
class RiskGateResult:
    def __init__(self, *, quantity=10.0, stop=90.0, take=110.0):
        self.approved_quantity = quantity
        self.hard_stop_loss = stop
        self.hard_take_profit = take
risk_stub.RiskGatekeeper = RiskGatekeeper
risk_stub.RiskGateResult = RiskGateResult
sys.modules.setdefault("risk_gatekeeper", risk_stub)

import execution_daemon
from execution_daemon import ExecutionDaemon
from order_intent_identity import IntentIdentityConflict


def expect_conflict(fn, message):
    try:
        fn()
    except IntentIdentityConflict:
        return
    raise AssertionError(message)


def main():
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "intent_identity.sqlite")
        fixed_time = 1_799_999_999.123
        original_time = execution_daemon.time.time
        execution_daemon.time.time = lambda: fixed_time
        try:
            daemon = ExecutionDaemon(db_path=db_path)
            signal = TradeSignal(price=100.0)
            gate = RiskGateResult(quantity=10.0, stop=90.0, take=110.0)

            # Same strategy, exact same millisecond, different semantic intents.
            first = daemon.dispatch_order_with_self_healing(
                signal, gate, intent_id="INTENT-A", effect_id="EFFECT-A"
            )
            second = daemon.dispatch_order_with_self_healing(
                signal, gate, intent_id="INTENT-B", effect_id="EFFECT-B"
            )
            assert first is not None and second is not None
            assert first.order_id != second.order_id, "same-ms distinct intents collapsed to one order_id"
            assert len(daemon.active_orders) == 2, "active_orders dict overwrote one distinct intent"

            with sqlite3.connect(db_path) as conn:
                assert conn.execute("SELECT COUNT(*) FROM order_intent_bindings").fetchone()[0] == 2
                assert conn.execute("SELECT COUNT(*) FROM order_fill_state").fetchone()[0] == 2
                assert conn.execute("SELECT COUNT(*) FROM fill_events").fetchone()[0] == 2
                ids = [row[0] for row in conn.execute(
                    "SELECT order_id FROM order_intent_bindings ORDER BY intent_key"
                ).fetchall()]
            assert len(set(ids)) == 2

            # Exact same retry identity + exact same canonical payload is zero-delta.
            replay = daemon.dispatch_order_with_self_healing(
                signal, gate, intent_id="INTENT-A", effect_id="EFFECT-A"
            )
            assert replay is first
            with sqlite3.connect(db_path) as conn:
                assert conn.execute("SELECT COUNT(*) FROM order_intent_bindings").fetchone()[0] == 2
                assert conn.execute("SELECT COUNT(*) FROM fill_events").fetchone()[0] == 2

            # Same idempotency identity with changed semantic payload MUST fail closed.
            mutated_gate = RiskGateResult(quantity=11.0, stop=90.0, take=110.0)
            expect_conflict(
                lambda: daemon.dispatch_order_with_self_healing(
                    signal, mutated_gate, intent_id="INTENT-A", effect_id="EFFECT-A"
                ),
                "mutated-payload retry was accepted as the original intent",
            )

            # Restart: first binding/digest survives; exact retry reuses stable order ID.
            restarted = ExecutionDaemon(db_path=db_path)
            after_restart = restarted.dispatch_order_with_self_healing(
                signal, gate, intent_id="INTENT-A", effect_id="EFFECT-A"
            )
            assert after_restart is not None
            assert after_restart.order_id == first.order_id
            with sqlite3.connect(db_path) as conn:
                assert conn.execute("SELECT COUNT(*) FROM order_intent_bindings").fetchone()[0] == 2
                assert conn.execute("SELECT COUNT(*) FROM fill_events").fetchone()[0] == 2

            expect_conflict(
                lambda: restarted.dispatch_order_with_self_healing(
                    signal, mutated_gate, intent_id="INTENT-A", effect_id="EFFECT-A"
                ),
                "restart forgot the first-bound payload digest",
            )

            # Legacy callers with no explicit key also cannot collide in one millisecond.
            legacy_one = restarted.dispatch_order_with_self_healing(signal, gate)
            legacy_two = restarted.dispatch_order_with_self_healing(signal, gate)
            assert legacy_one is not None and legacy_two is not None
            assert legacy_one.order_id != legacy_two.order_id

            # Demonstrate the exact old mutant is non-discriminating under frozen time.
            naive_a = f"ORD_{signal.strategy.value[:3]}_{int(fixed_time * 1000)}"
            naive_b = f"ORD_{signal.strategy.value[:3]}_{int(fixed_time * 1000)}"
            assert naive_a == naive_b, "known-bad timestamp-only mutant unexpectedly differed"

            print("PASS: same-ms collision-safe order intent identity + payload-bound retry court")
        finally:
            execution_daemon.time.time = original_time


if __name__ == "__main__":
    main()
