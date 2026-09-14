#!/usr/bin/env python3
"""V2.2 real-path court for execution intent presence vs validity.

This court deliberately uses the canonical TradeSignal shape with no injected intent
attribute, then exercises explicit-empty, explicit-valid and conflicting dual IDs.
It must fail if the production dispatch path collapses an explicitly present blank
identity into the generated/default path, or if generated fallback identity loses its
same-millisecond collision discriminator.
"""

import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from alpha_engine import SignalType, StrategyArchetype, TradeSignal
from execution_daemon import ExecutionDaemon
from risk_gatekeeper import RiskGateResult


def canonical_signal() -> TradeSignal:
    return TradeSignal(
        bar_id=1,
        timestamp=1.0,
        strategy=StrategyArchetype.MEAN_REVERSION,
        signal_type=SignalType.BUY,
        price=100.0,
        stop_loss=98.0,
        take_profit=104.0,
        risk_reward_ratio=2.0,
        confidence=0.9,
    )


def approved_gate() -> RiskGateResult:
    return RiskGateResult(
        passed=True,
        reason="fixture",
        approved_quantity=1.0,
        risk_amount=2.0,
        hard_stop_loss=98.0,
        hard_take_profit=104.0,
    )


class ExecutionIntentIdentityCourt(unittest.TestCase):
    def make_daemon(self, directory: str) -> ExecutionDaemon:
        return ExecutionDaemon(db_path=str(Path(directory) / "intent-court.sqlite"))

    def test_absent_intent_uses_bounded_generated_fallback(self):
        with tempfile.TemporaryDirectory() as td:
            signal = canonical_signal()
            self.assertFalse(hasattr(signal, "intent_id"))
            self.assertFalse(hasattr(signal, "order_intent_id"))
            order = self.make_daemon(td).dispatch_order_with_self_healing(signal, approved_gate())
            self.assertIsNotNone(order)
            self.assertTrue(order.order_id.startswith("ORD_MEA_"))
            self.assertGreater(len(order.order_id.removeprefix("ORD_MEA_")), 6)

    def test_two_absent_intents_same_millisecond_stay_distinct(self):
        """Kill court: timestamp-only fallback must collide and fail this test."""
        with tempfile.TemporaryDirectory() as td:
            daemon = self.make_daemon(td)
            uuids = [
                SimpleNamespace(hex="aaa111ffffffffffffffffffffffffff"),
                SimpleNamespace(hex="bbb222ffffffffffffffffffffffffff"),
            ]
            with patch("execution_daemon.time.time", return_value=1234.567), patch(
                "execution_daemon.uuid.uuid4", side_effect=uuids
            ):
                first = daemon.dispatch_order_with_self_healing(canonical_signal(), approved_gate())
                second = daemon.dispatch_order_with_self_healing(canonical_signal(), approved_gate())

            self.assertIsNotNone(first)
            self.assertIsNotNone(second)
            self.assertNotEqual(first.order_id, second.order_id)
            self.assertEqual(first.order_id, "ORD_MEA_1234567_aaa111")
            self.assertEqual(second.order_id, "ORD_MEA_1234567_bbb222")
            self.assertEqual(len(daemon.active_orders), 2)

    def test_explicit_empty_intent_is_invalid_not_absent(self):
        with tempfile.TemporaryDirectory() as td:
            signal = canonical_signal()
            signal.intent_id = ""
            with self.assertRaisesRegex(ValueError, "intent_id"):
                self.make_daemon(td).dispatch_order_with_self_healing(signal, approved_gate())

    def test_explicit_valid_intent_is_preserved(self):
        with tempfile.TemporaryDirectory() as td:
            signal = canonical_signal()
            signal.intent_id = "intent-fixed-001"
            order = self.make_daemon(td).dispatch_order_with_self_healing(signal, approved_gate())
            self.assertIsNotNone(order)
            self.assertEqual(order.order_id, "ORD_MEA_intent-fixed-001")

    def test_conflicting_dual_intent_fields_fail_closed(self):
        with tempfile.TemporaryDirectory() as td:
            signal = canonical_signal()
            signal.intent_id = "intent-A"
            signal.order_intent_id = "intent-B"
            with self.assertRaisesRegex(ValueError, "conflicting"):
                self.make_daemon(td).dispatch_order_with_self_healing(signal, approved_gate())


if __name__ == "__main__":
    unittest.main(verbosity=2)
