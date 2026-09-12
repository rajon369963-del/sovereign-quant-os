#!/usr/bin/env python3
"""V2.2 hostile court for TWAP slice-domain invariants.

This battery exercises the exact production TWAPExecutionEngine.plan_twap_slices
path. It never contacts a broker and never submits an order.
"""

import math
import random

import numpy as np

from agentic_alpha_shift import TWAPExecutionEngine


def expect_hold(engine, total_size, expected_code):
    try:
        engine.plan_twap_slices(total_size)
    except ValueError as exc:
        assert expected_code in str(exc), (expected_code, str(exc))
    else:
        raise AssertionError(f"expected {expected_code} for total_size={total_size!r}")


def test_seed79_tiny_total_fails_closed():
    engine = TWAPExecutionEngine(min_chunks=4, max_chunks=4)
    random.seed(79)
    np.random.seed(79)
    expect_hold(engine, 0.0002, "HOLD_BELOW_MIN_EXECUTABLE_SIZE")


def test_invalid_totals_fail_closed():
    engine = TWAPExecutionEngine(min_chunks=4, max_chunks=4)
    for value in (0.0, -0.001, float("nan"), float("inf"), float("-inf")):
        expect_hold(engine, value, "HOLD_INVALID_TOTAL_SIZE")


def test_executable_totals_stay_positive_and_conserved():
    engine = TWAPExecutionEngine(min_chunks=4, max_chunks=4)
    for seed in range(200):
        random.seed(seed)
        np.random.seed(seed)
        slices = engine.plan_twap_slices(0.0040)
        sizes = [s["size"] for s in slices]
        assert len(sizes) == 4
        assert all(math.isfinite(x) and x > 0 for x in sizes), (seed, sizes)
        assert round(sum(sizes), 4) == 0.0040, (seed, sizes)


def test_bypass_shape_is_known_bad():
    """Document the exact old residual allocator as a kill-condition fixture."""
    np.random.seed(79)
    weights = np.random.dirichlet(np.ones(4))
    sizes = [float(round(0.0002 * w, 4)) for w in weights]
    sizes[-1] = float(round(sizes[-1] + (0.0002 - sum(sizes)), 4))
    assert round(sum(sizes), 4) == 0.0002
    assert any(size <= 0 for size in sizes), sizes


def main():
    test_seed79_tiny_total_fails_closed()
    test_invalid_totals_fail_closed()
    test_executable_totals_stay_positive_and_conserved()
    test_bypass_shape_is_known_bad()
    print("TWAP_SLICE_DOMAIN_COURT=PASS")


if __name__ == "__main__":
    main()
