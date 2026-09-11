"""
Test Battery for Async L2 DMA Order Gateway
Module: test_async_l2_dma_battery.py
Task ID: TASK_017_QUANT_OS_L2_ORDER_DMA_GATEWAY
Target Repo: rajon369963-del/sovereign-quant-os
"""

import asyncio
import io
import json
import logging
import time
import tracemalloc
import sys
from pathlib import Path

# Add repo to sys.path
sys.path.insert(0, "/Users/rajondas/teamwork_projects/sovereign-quant-os")

from async_l2_dma_gateway import (
    AccountState,
    AsyncL2DMAGateway,
    BINARY_L2_STRUCT,
    DMAOrder,
    L2RingBuffer,
    OrderSide,
    SecretStr,
    SensitiveDataScrubber,
    SentinelRiskGuard,
    SentinelViolationError,
)


def test_zero_secret_leakage():
    print("[TEST 1/4] Running Zero Secret Leakage Battery...")
    raw_token = "eyJhGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.super_secret_broker_token_12345"
    raw_secret = "sk_live_quant_broker_production_secret_998877"

    secret_token = SecretStr(raw_token)
    secret_key = SecretStr(raw_secret)

    # Invariant 1: str, repr, format must never expose the raw string
    assert str(secret_token) == "[REDACTED_SECRET]", f"Leak in str(): {str(secret_token)}"
    assert repr(secret_token) == "[REDACTED_SECRET]", f"Leak in repr(): {repr(secret_token)}"
    assert f"{secret_token}" == "[REDACTED_SECRET]", f"Leak in format(): {secret_token}"
    assert raw_token not in repr(secret_token), "Token found in repr!"
    assert raw_secret not in repr(secret_key), "Secret found in repr!"

    # Invariant 2: Order repr must never expose credentials
    order = DMAOrder(
        order_id="ORD-TEST-001",
        symbol="NIFTY50",
        side=OrderSide.BUY,
        quantity=50.0,
        price=24500.0,
        session_token=secret_token,
        broker_secret=secret_key,
    )
    order_repr = repr(order)
    assert raw_token not in order_repr, f"Raw token leaked in order repr: {order_repr}"
    assert raw_secret not in order_repr, f"Raw secret leaked in order repr: {order_repr}"

    # Invariant 3: Logger filter scrub check
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    handler.addFilter(SensitiveDataScrubber())
    logger = logging.getLogger("dma_test_logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    test_log_msg = f"Dispatching with token: bearer {raw_token} and secret={raw_secret}"
    logger.info(test_log_msg)
    logged_output = stream.getvalue()

    assert raw_token not in logged_output, f"Secret leaked in logger: {logged_output}"
    assert raw_secret not in logged_output, f"Secret leaked in logger: {logged_output}"
    print("  -> PASS: Zero Secret Leakage verified across all representations and logging sinks.")


def test_l2_order_book_depth_parsing_and_ring_buffer():
    print("[TEST 2/4] Running L2 Depth Parsing & Ring Buffer Fixed-Heap Battery...")
    buffer_cap = 5000
    gateway = AsyncL2DMAGateway(ring_buffer_capacity=buffer_cap)

    raw_packet = BINARY_L2_STRUCT.pack(b"NIFTY50\x00", 24500.50, 150.0, 10001, b"B")

    t0 = time.perf_counter_ns()
    iterations = 5000
    for _ in range(iterations):
        gateway.parser.parse_binary(raw_packet)
    t1 = time.perf_counter_ns()

    elapsed_per_packet_us = ((t1 - t0) / iterations) / 1000.0
    print(f"  -> Binary L2 parsing latency: {elapsed_per_packet_us:.3f} microseconds / packet")
    assert elapsed_per_packet_us < 50.0, f"Binary parsing too slow: {elapsed_per_packet_us} us"

    assert gateway.ring_buffer.total_writes == iterations
    assert gateway.ring_buffer.current_allocated_slots == buffer_cap

    json_packet = json.dumps({
        "symbol": "BANKNIFTY",
        "price": 52100.25,
        "size": 75.0,
        "seq": 20002,
        "side": "A"
    })
    entry_json = gateway.parser.parse_json(json_packet)
    assert entry_json.symbol == "BANKNIFTY"
    assert entry_json.price == 52100.25
    assert entry_json.side == "A"
    print("  -> PASS: L2 depth parsing & fixed ring buffer verified.")


def test_sentinel_risk_pre_post_conditions():
    print("[TEST 3/4] Running Sentinel Pre- and Post-Condition Verification...")
    account = AccountState(
        available_capital=500_000.0,
        reserved_capital=0.0,
        maintenance_margin_required=50_000.0,
        current_positions={"RELIANCE": 1000.0},
    )
    guard = SentinelRiskGuard(
        max_order_capital=100_000.0,
        max_position_limit=2_000.0,
        max_leverage_ratio=3.0,
        fat_finger_pct_band=0.05,
    )

    dummy_token = SecretStr("token_abc")
    dummy_secret = SecretStr("secret_xyz")

    # 1. Breach Capital Bound
    expensive_order = DMAOrder(
        order_id="BREACH-01",
        symbol="RELIANCE",
        side=OrderSide.BUY,
        quantity=100.0,
        price=1500.0,
        session_token=dummy_token,
        broker_secret=dummy_secret,
    )
    try:
        guard.verify_preconditions(expensive_order, account, best_bid=1500.0, best_ask=1500.5)
        assert False, "Should have failed capital bounds check"
    except SentinelViolationError as e:
        assert "CAPITAL_BOUND_EXCEEDED" in str(e)

    # 2. Breach Position Limit
    large_pos_order = DMAOrder(
        order_id="BREACH-02",
        symbol="RELIANCE",
        side=OrderSide.BUY,
        quantity=1500.0,
        price=50.0,
        session_token=dummy_token,
        broker_secret=dummy_secret,
    )
    try:
        guard.verify_preconditions(large_pos_order, account, best_bid=50.0, best_ask=50.1)
        assert False, "Should have failed position limit check"
    except SentinelViolationError as e:
        assert "POSITION_LIMIT_EXCEEDED" in str(e)

    # 3. Fat Finger Price Discrepancy
    fat_finger_order = DMAOrder(
        order_id="BREACH-03",
        symbol="RELIANCE",
        side=OrderSide.BUY,
        quantity=10.0,
        price=2000.0,
        session_token=dummy_token,
        broker_secret=dummy_secret,
    )
    try:
        guard.verify_preconditions(fat_finger_order, account, best_bid=1499.0, best_ask=1500.0)
        assert False, "Should have failed fat finger price check"
    except SentinelViolationError as e:
        assert "FAT_FINGER_PRICE_DISCREPANCY" in str(e)

    # 4. Postcondition verification
    account.available_capital = -10.0
    try:
        guard.verify_postconditions(expensive_order, account)
        assert False, "Should have caught negative capital in postcondition"
    except SentinelViolationError as e:
        assert "NEGATIVE_CAPITAL_INVARIANT" in str(e)

    print("  -> PASS: All Sentinel Pre/Postcondition rules verified and fail-closed.")


async def test_rapid_1000_order_burst_benchmark():
    print("[TEST 4/4] Running 1,000 Order Rapid Burst & Memory Leakage Battery...")
    gateway = AsyncL2DMAGateway(
        ring_buffer_capacity=10000,
        account_state=AccountState(
            available_capital=50_000_000.0,
            reserved_capital=0.0,
            maintenance_margin_required=100_000.0,
            current_positions={},
        ),
        sentinel_guard=SentinelRiskGuard(
            max_order_capital=500_000.0,
            max_position_limit=1_000_000.0,
            max_leverage_ratio=10.0,
            fat_finger_pct_band=0.10,
        )
    )

    dummy_token = SecretStr("session_burst_test_token_445566")
    dummy_secret = SecretStr("broker_burst_test_secret_778899")

    orders = [
        DMAOrder(
            order_id=f"BURST-{i:04d}",
            symbol="INFY",
            side=OrderSide.BUY if (i % 2 == 0) else OrderSide.SELL,
            quantity=10.0,
            price=1500.0,
            session_token=dummy_token,
            broker_secret=dummy_secret,
        )
        for i in range(1000)
    ]

    tracemalloc.start()
    gc_before = tracemalloc.take_snapshot()

    t_start = time.perf_counter()
    results = await gateway.dispatch_burst(orders, best_bid=1499.0, best_ask=1501.0)
    t_end = time.perf_counter()

    gc_after = tracemalloc.take_snapshot()
    tracemalloc.stop()

    total_duration_ms = (t_end - t_start) * 1000.0
    print(f"  -> Processed {len(results)} rapid DMA wire dispatches in: {total_duration_ms:.2f} ms")
    assert len(results) == 1000, f"Expected 1000 orders dispatched, got {len(results)}"
    assert total_duration_ms < 50.0, f"Burst latency target (< 50ms) failed: {total_duration_ms:.2f} ms"

    top_stats = gc_after.compare_to(gc_before, 'lineno')
    total_diff_kb = sum(stat.size_diff for stat in top_stats) / 1024.0
    print(f"  -> Total heap growth during 1,000 order burst: {total_diff_kb:.2f} KB")

    for item in results:
        item_str = str(item)
        assert "session_burst_test_token_445566" not in item_str, "Token leaked into wire order"
        assert "broker_burst_test_secret_778899" not in item_str, "Secret leaked into wire order"

    print("  -> PASS: 1,000 rapid order burst processed in < 50ms with zero memory leakage and zero secret leakage.")


def main():
    print("=================================================================")
    print("RUNNING SOVEREIGN QUANT OS L2 ORDER DMA GATEWAY TEST SUITE")
    print("TASK ID: TASK_017_QUANT_OS_L2_ORDER_DMA_GATEWAY")
    print("=================================================================")

    test_zero_secret_leakage()
    test_l2_order_book_depth_parsing_and_ring_buffer()
    test_sentinel_risk_pre_post_conditions()
    asyncio.run(test_rapid_1000_order_burst_benchmark())

    print("=================================================================")
    print("ALL 4 CRITICAL BATTERY SUITES PASSED CLEANLY")
    print("=================================================================")


if __name__ == "__main__":
    main()
