#!/usr/bin/env python3
"""Quant #62: canonical default TradeSignal runtime path and missing-uuid kill mutant."""

import tempfile
import time
from pathlib import Path

import pytest

import execution_daemon as execution_module
from alpha_engine import SignalType, StrategyArchetype, TradeSignal
from execution_daemon import ExecutionDaemon
from risk_gatekeeper import RiskGateResult


def _signal() -> TradeSignal:
    return TradeSignal(
        bar_id=62,
        timestamp=time.time(),
        strategy=StrategyArchetype.MEAN_REVERSION,
        signal_type=SignalType.BUY,
        price=100.0,
        stop_loss=90.0,
        take_profit=110.0,
        risk_reward_ratio=2.0,
        confidence=0.85,
    )


def _gate() -> RiskGateResult:
    return RiskGateResult(
        passed=True,
        reason="PASS",
        approved_quantity=1.0,
        risk_amount=10.0,
        hard_stop_loss=90.0,
        hard_take_profit=110.0,
    )


def _daemon(tmp_path: Path) -> ExecutionDaemon:
    return ExecutionDaemon(db_path=str(tmp_path / "quant62.sqlite"), initial_capital=50000.0)


def test_default_tradesignal_without_intent_id_executes_real_dispatch_path(tmp_path: Path):
    signal = _signal()
    assert not hasattr(signal, "intent_id")
    assert not hasattr(signal, "order_intent_id")

    order = _daemon(tmp_path).dispatch_order_with_self_healing(signal, _gate())

    assert order is not None
    assert order.order_id.startswith(f"ORD_{signal.strategy.value[:3]}_")
    assert order.order_id.count("_") >= 3


def test_explicit_intent_positive_control_remains_stable(tmp_path: Path):
    signal = _signal()
    signal.intent_id = "Q62_EXPLICIT_CONTROL"

    order = _daemon(tmp_path).dispatch_order_with_self_healing(signal, _gate())

    assert order is not None
    assert order.order_id.endswith("Q62_EXPLICIT_CONTROL")


def test_missing_runtime_identity_dependency_mutant_turns_red(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    signal = _signal()
    monkeypatch.delattr(execution_module, "uuid")

    with pytest.raises(NameError, match="uuid"):
        _daemon(tmp_path).dispatch_order_with_self_healing(signal, _gate())
