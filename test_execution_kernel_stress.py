"""
Test Battery for Execution Kernel Stress & Idempotency Audit
Module: test_execution_kernel_stress.py
Task ID: TASK_016_QUANT_OS_STRESS_SCENARIOS
Repository: rajon369963-del/sovereign-quant-os
"""

import asyncio
import json
import time
import sys

# Ensure module is in sys.path
sys.path.insert(0, "/Users/rajondas/teamwork_projects/sovereign-quant-os")

from execution_kernel_stress import (
    ConnectionState,
    ExecutionKernel,
    OrderState,
    PriorityTokenBucket,
    SecretStr,
    StressOrder,
)


def test_zero_secret_leakage():
    print("[TEST 1/4] Testing Zero Secret Leakage in Orders & Traces...")
    raw_token = "eyJhGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.super_secret_quant_order_token_99999"
    secret = SecretStr(raw_token)

    assert str(secret) == "[REDACTED_SECRET]"
    assert repr(secret) == "[REDACTED_SECRET]"
    assert f"{secret}" == "[REDACTED_SECRET]"
    assert raw_token not in repr(secret)

    order = StressOrder(
        cl_ord_id="ORD-SEC-001",
        symbol="NIFTY",
        quantity=25.0,
        price=24600.0,
        side="BUY",
        session_token=secret,
    )
    order_repr = repr(order)
    assert raw_token not in order_repr
    assert "[REDACTED_SECRET]" in order_repr
    print("  -> PASS: Zero Secret Leakage verified across order representations.")


async def test_1000_retry_idempotency():
    print("[TEST 2/4] Testing 1,000 Rapid Retry Idempotency Barrier (Zero Duplicate Execution)...")
    kernel = ExecutionKernel(db_path=":memory:")
    dummy_secret = SecretStr("token_test_abc_123")

    single_cl_ord_id = "CLORD-IDEMPOTENT-STORM-001"
    order = StressOrder(
        cl_ord_id=single_cl_ord_id,
        symbol="RELIANCE",
        quantity=100.0,
        price=1500.0,
        side="BUY",
        session_token=dummy_secret,
    )

    t0 = time.perf_counter()
    results = []
    for _ in range(1000):
        res = await kernel.dispatch_order(order)
        results.append(res)
    t1 = time.perf_counter()

    wire_dispatches = [r for r in results if r["wire_dispatched"] is True]
    idempotent_ignores = [r for r in results if r["status"] == "IDEMPOTENT_DUPLICATE_IGNORED"]

    print(f"  -> Total attempts: {len(results)}")
    print(f"  -> Actual wire dispatches: {len(wire_dispatches)}")
    print(f"  -> Idempotently suppressed: {len(idempotent_ignores)}")

    assert len(wire_dispatches) == 1, f"Expected exactly 1 wire dispatch, got {len(wire_dispatches)}"
    assert len(idempotent_ignores) == 999, f"Expected 999 ignored duplicates, got {len(idempotent_ignores)}"
    assert kernel.wire_dispatch_count == 1, f"Kernel wire dispatch count mismatch: {kernel.wire_dispatch_count}"

    count = kernel.get_journal_order_count(single_cl_ord_id)
    assert count == 1, f"Database has {count} entries, expected 1"
    kernel.close()

    print("  -> PASS: 100% deduplication achieved across 1,000 rapid retry storms.")


async def test_network_disconnect_and_reconnect_watchdog():
    print("[TEST 3/4] Testing Network Disconnects & Reconnect Watchdog Recovery...")
    kernel = ExecutionKernel(db_path=":memory:")
    dummy_secret = SecretStr("token_net_test")

    o1 = StressOrder("CLORD-NET-01", "INFY", 10.0, 1500.0, "BUY", dummy_secret)
    res1 = await kernel.dispatch_order(o1)
    assert res1["wire_dispatched"] is True

    await kernel.simulate_network_disconnect()
    assert kernel.conn_state == ConnectionState.DISCONNECTED
    assert kernel.disconnect_event_count == 1

    o2 = StressOrder("CLORD-NET-02", "INFY", 20.0, 1505.0, "SELL", dummy_secret)
    res2 = await kernel.dispatch_order(o2)

    assert kernel.conn_state == ConnectionState.CONNECTED
    assert kernel.reconnect_event_count >= 1
    assert res2["wire_dispatched"] is True
    assert res2["wire_seq"] == 2
    kernel.close()

    print("  -> PASS: Reconnect watchdog cleanly restored link and dispatched pending wire order.")


async def test_high_throughput_stress_benchmark():
    print("[TEST 4/4] Testing High-Throughput Stress Benchmark (> 500 ops/sec)...")
    kernel = ExecutionKernel(db_path=":memory:")
    dummy_secret = SecretStr("token_stress_benchmark")

    orders = [
        StressOrder(
            cl_ord_id=f"BURST-ORD-{i:05d}",
            symbol="TCS",
            quantity=10.0,
            price=3500.0,
            side="BUY" if (i % 2 == 0) else "SELL",
            session_token=dummy_secret,
        )
        for i in range(1000)
    ]

    t0 = time.perf_counter()
    for order in orders:
        res = await kernel.dispatch_order(order, simulated_latency_ms=0.2)
        assert res["wire_dispatched"] is True
    t1 = time.perf_counter()

    duration_sec = t1 - t0
    ops_per_sec = len(orders) / duration_sec
    print(f"  -> Processed {len(orders)} orders in {duration_sec:.3f} s ({ops_per_sec:.1f} ops/sec)")
    assert ops_per_sec > 500.0, f"Throughput target (> 500 ops/sec) failed: {ops_per_sec:.1f} ops/sec"
    kernel.close()

    print("  -> PASS: Execution throughput exceeded 500 ops/sec under stress load.")


def main():
    print("=================================================================")
    print("RUNNING SOVEREIGN QUANT OS EXECUTION KERNEL STRESS TEST SUITE")
    print("TASK ID: TASK_016_QUANT_OS_STRESS_SCENARIOS")
    print("=================================================================")

    test_zero_secret_leakage()
    asyncio.run(test_1000_retry_idempotency())
    asyncio.run(test_network_disconnect_and_reconnect_watchdog())
    asyncio.run(test_high_throughput_stress_benchmark())

    print("=================================================================")
    print("ALL 4 STRESS BATTERY SUITES PASSED CLEANLY")
    print("=================================================================")


if __name__ == "__main__":
    main()
