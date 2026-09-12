import math
import sys
import types

# `alpha_engine.py` imports Polars only for the `scan_all_bars` type surface.
# This court exercises the exact production `evaluate_bar()` path and should not
# add a heavy unrelated runtime wheel merely to satisfy an import-only annotation.
if "polars" not in sys.modules:
    sys.modules["polars"] = types.SimpleNamespace(DataFrame=object)

from alpha_engine import AlphaEngine, StrategyArchetype


def mean_reversion_case():
    return {
        "bar_id": 1,
        "timestamp": 1.0,
        "close": 100.0,
        "atr_14": 1.0,
        "rsi_14": 20.0,
        "bb_lower": 100.0,
        "ema_20": 100.0,
        "ema_200": 100.0,
        "volume": 100.0,
        "cvd": 0.0,
    }, None, StrategyArchetype.MEAN_REVERSION, 2.0


def breakout_case():
    row = {
        "bar_id": 2,
        "timestamp": 2.0,
        "close": 101.0,
        "atr_14": 1.0,
        "rsi_14": 50.0,
        "ema_20": 100.0,
        "ema_200": 90.0,
        "volume": 200.0,
        "cvd": 0.0,
    }
    prev = {"close": 99.0, "ema_20": 100.0, "volume": 100.0}
    return row, prev, StrategyArchetype.QULLAMAGGIE_BREAKOUT, 2.5


def cvd_case():
    return {
        "bar_id": 3,
        "timestamp": 3.0,
        "close": 100.0,
        "atr_14": 1.0,
        "rsi_14": 50.0,
        "ema_20": 100.0,
        "ema_200": 100.0,
        "volume": 100.0,
        "cvd": 400.0,
    }, None, StrategyArchetype.LEAD_LAG_CVD_SURGE, 2.8 / 1.2


def cases():
    return [mean_reversion_case(), breakout_case(), cvd_case()]


def test_high_configured_floor_blocks_all_otherwise_qualifying_strategies():
    engine = AlphaEngine(min_rr_ratio=10.0)
    for row, prev, _, _ in cases():
        assert engine.evaluate_bar(row, prev) is None


def test_low_floor_preserves_strategy_signals_and_computed_rr():
    engine = AlphaEngine(min_rr_ratio=1.0)
    for row, prev, expected_strategy, expected_rr in cases():
        signal = engine.evaluate_bar(row, prev)
        assert signal is not None
        assert signal.strategy is expected_strategy
        assert math.isclose(signal.risk_reward_ratio, expected_rr, rel_tol=0.0, abs_tol=1e-12)


def test_equal_floor_is_eligible():
    row, prev, expected_strategy, expected_rr = mean_reversion_case()
    engine = AlphaEngine(min_rr_ratio=2.0)
    signal = engine.evaluate_bar(row, prev)
    assert signal is not None
    assert signal.strategy is expected_strategy
    assert math.isclose(signal.risk_reward_ratio, expected_rr, rel_tol=0.0, abs_tol=1e-12)


def test_invalid_min_rr_configuration_fails_closed():
    for invalid in (-0.01, float("nan"), float("inf"), float("-inf")):
        try:
            AlphaEngine(min_rr_ratio=invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid min_rr_ratio accepted: {invalid!r}")


def test_known_bad_gate_bypass_would_be_detected():
    # Explicit kill condition: every exact qualifying strategy fixture computes
    # RR below 10.0. Removing/bypassing `_rr_gate_allows()` would make the
    # high-floor production-path test return TradeSignal objects and fail.
    for _, _, _, rr in cases():
        assert rr < 10.0


if __name__ == "__main__":
    tests = [
        test_high_configured_floor_blocks_all_otherwise_qualifying_strategies,
        test_low_floor_preserves_strategy_signals_and_computed_rr,
        test_equal_floor_is_eligible,
        test_invalid_min_rr_configuration_fails_closed,
        test_known_bad_gate_bypass_would_be_detected,
    ]
    for test in tests:
        test()
        print(f"PASS: {test.__name__}")
