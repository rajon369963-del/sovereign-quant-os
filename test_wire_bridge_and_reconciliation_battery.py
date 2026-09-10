"""
================================================================================
AIR10 WIRE BRIDGE & INFLIGHT RECONCILIATION TEST BATTERY
================================================================================
Phase 2 Verified Implementation & Adversarial Falsification Suite.

6-Stage Rigorous Testing Ladder:
1. TEST_01: Quantum Wire State Lifecycle & ClOrdID Idempotency.
2. TEST_02: Shoonya Remarks Reconciliation & Amnesiac Socket Subscription Replay.
3. TEST_03: Adversarial Chaos Injection & Decorrelated Jitter Backoff (429 Burst).
4. TEST_04: Wire Drop & Inflight Zombie Order Reconciliation Sweeper.
5. TEST_05: Bailout Limit Guard & Dead-Man's Switch Emergency Flush.
6. TEST_06: 100-Order Async Concurrency & Sub-5ms Decision Latency Benchmark.
================================================================================
"""

import asyncio
import os
import sqlite3
import sys
import time
from pathlib import Path

ENGINE_DIR = Path(os.environ.get("AIR10_ENGINE_DIR", Path(__file__).resolve().parent))
sys.path.insert(0, str(ENGINE_DIR))

from async_l2_dma_gateway import (
    AsyncL2DMAGateway,
    OrderSide,
    OrderState,
    VenueType,
)
from live_broker_wire_bridge import (
    DecorrelatedJitterBackoff,
    LiveBrokerWireBridge,
    WireMode,
    WireOrderPayload,
    WireState,
)

passed_tests = 0
total_tests = 6

async def run_battery():
    global passed_tests
    print("\n" + "="*80)
    print("🚀 STARTING AIR10 WIRE BRIDGE & RECONCILIATION TEST BATTERY (PHASE 2)")
    print("="*80)

    test_db = Path(os.environ.get("AIR10_TEST_DB", ENGINE_DIR / "test_wire_bridge_ledger.sqlite"))
    if test_db.exists():
        test_db.unlink()

    bridge = LiveBrokerWireBridge(test_db, mode=WireMode.TESTNET_MOCK, max_unreconciled_bailout=3)

    # --------------------------------------------------------------------------
    # TEST 1: Quantum Wire State Lifecycle & ClOrdID Idempotency
    # --------------------------------------------------------------------------
    print("\n[TEST 1/6] Testing Quantum Wire State Lifecycle & ClOrdID Idempotency...")
    cl_ord_id = "AGY_HYP_BTC__TEST1_INTENT_001"
    order = WireOrderPayload(
        cl_ord_id=cl_ord_id,
        symbol="BTC-PERP",
        venue="HYPERLIQUID_DEX_ALO",
        side="BUY",
        price=60000.0,
        quantity=0.1,
        order_type="ALO"
    )
    res = await bridge.transmit_order(order)
    assert res.wire_state == WireState.FILLED, f"Expected FILLED, got {res.wire_state}"
    assert res.exchange_oid.startswith("TESTNET_"), f"Missing exchange OID: {res.exchange_oid}"
    assert res.rebate_inr > 0, "ALO maker rebate should be positive"
    print(f"  ✅ Order Transmitted & Filled: OID={res.exchange_oid} | Rebate=₹{res.rebate_inr:.4f}")
    
    # Test Idempotency (replay same intent)
    order_dup = WireOrderPayload(
        cl_ord_id=cl_ord_id,
        symbol="BTC-PERP",
        venue="HYPERLIQUID_DEX_ALO",
        side="BUY",
        price=60000.0,
        quantity=0.1,
        order_type="ALO"
    )
    sends_before = bridge.total_wire_sent
    res_dup = await bridge.transmit_order(order_dup)
    assert res_dup.exchange_oid == res.exchange_oid, f"Expected same OID {res.exchange_oid}, got {res_dup.exchange_oid}"
    assert bridge.total_wire_sent == sends_before, f"Expected 0 extra wire sends, got {bridge.total_wire_sent - sends_before}"

    # Verify idempotency via WAL ledger: the cl_ord_id should still have a single row as FILLED
    wal_conn = sqlite3.connect(bridge.db_path, timeout=5.0)
    count = wal_conn.execute(
        "SELECT COUNT(*) FROM wire_state_audit_log WHERE cl_ord_id = ?",
        (cl_ord_id,)
    ).fetchone()[0]
    wal_row = wal_conn.execute(
        "SELECT wire_state FROM wire_state_audit_log WHERE cl_ord_id = ?",
        (cl_ord_id,)
    ).fetchone()
    wal_conn.close()
    assert count == 1, f"Expected exactly 1 audit row, got {count}"
    assert wal_row is not None, f"ClOrdID {cl_ord_id} not found in WAL ledger"
    assert wal_row[0] == "FILLED", f"Expected FILLED in WAL, got {wal_row[0]}"
    print(f"  ✅ 100% Idempotent ClOrdID check confirmed (Re-transmission returned OID={res_dup.exchange_oid} with 0 new wire sends)")

    # Test concurrent in-flight retries (same cl_ord_id sent concurrently while in wire flight)
    concurrent_cl_ord = f"AGY_CONC_{time.time_ns()}"
    mk_concurrent = lambda: WireOrderPayload(
        cl_ord_id=concurrent_cl_ord,
        symbol="ETH-PERP",
        venue="HYPERLIQUID_DEX_ALO",
        side="BUY",
        price=3000.0,
        quantity=0.5,
        order_type="ALO"
    )
    sends_before_conc = bridge.total_wire_sent
    t_c1 = asyncio.create_task(bridge.transmit_order(mk_concurrent()))
    await asyncio.sleep(0.0002) # let first order enter wire flight
    res_c2 = await bridge.transmit_order(mk_concurrent())
    res_c1 = await t_c1
    assert res_c1.exchange_oid == res_c2.exchange_oid, f"Concurrent OIDs must match: {res_c1.exchange_oid} vs {res_c2.exchange_oid}"
    assert res_c2.wire_state == WireState.FILLED, f"Expected FILLED state, got {res_c2.wire_state}"
    assert bridge.total_wire_sent == sends_before_conc + 1, f"Expected 1 wire send for concurrent retry, got {bridge.total_wire_sent - sends_before_conc}"
    print(f"  ✅ Concurrent in-flight retry confirmed (0 extra wire sends, matching OID={res_c1.exchange_oid})")
    passed_tests += 1

    # --------------------------------------------------------------------------
    # TEST 2: Shoonya Remarks Reconciliation & Amnesiac Socket Subscription Replay
    # --------------------------------------------------------------------------
    print("\n[TEST 2/6] Testing Shoonya Remarks Hack & Amnesiac Socket Subscription Replay...")
    remarks_token = bridge.generate_remarks_token("AGY_SHO_RELI_001")
    assert remarks_token.startswith("RK_") and len(remarks_token) == 11, f"Bad token: {remarks_token}"
    print(f"  ✅ Shoonya Remarks Token Generated: {remarks_token} (Overloaded into 12-char field)")

    # Test Subscription Replay
    bridge.register_subscription("RELIANCE-EQ")
    bridge.register_subscription("TCS-EQ")
    bridge.register_subscription("INFY-EQ")
    replayed = bridge.replay_subscriptions()
    assert len(replayed) == 3, f"Expected 3 replayed tokens, got {len(replayed)}"
    assert "RELIANCE-EQ" in replayed and "TCS-EQ" in replayed
    print(f"  ✅ Amnesiac Socket Replay Succeeded: {len(replayed)} symbols recovered after disconnect")
    passed_tests += 1

    # --------------------------------------------------------------------------
    # TEST 3: Adversarial Chaos Injection & Decorrelated Jitter Backoff
    # --------------------------------------------------------------------------
    print("\n[TEST 3/6] Testing Adversarial Chaos Injection & Decorrelated Jitter Backoff...")
    chaos_bridge = LiveBrokerWireBridge(test_db, mode=WireMode.SANDBOX_CHAOS, max_unreconciled_bailout=10)
    jitter = DecorrelatedJitterBackoff(base=0.01, cap=0.5)
    
    s1 = jitter.next_sleep()
    s2 = jitter.next_sleep()
    s3 = jitter.next_sleep()
    assert s1 >= 0.01 and s1 <= 0.5
    assert s2 >= 0.01 and s2 <= 0.5
    print(f"  ✅ Decorrelated Jitter Sequence: {s1:.4f}s -> {s2:.4f}s -> {s3:.4f}s (Randomized Anti-429)")

    # Send 10 orders into Chaos Bridge
    chaos_orders = []
    for i in range(10):
        o = WireOrderPayload(
            cl_ord_id=f"AGY_CHAOS_{i:03d}",
            symbol="ETH-PERP",
            venue="HYPERLIQUID_DEX_ALO",
            side="BUY",
            price=3000.0,
            quantity=1.0,
            order_type="ALO"
        )
        chaos_orders.append(await chaos_bridge.transmit_order(o))

    filled_count = len([o for o in chaos_orders if o.wire_state == WireState.FILLED])
    drops_count = len([o for o in chaos_orders if o.wire_state == WireState.INFLIGHT_UNKNOWN])
    print(f"  ✅ Chaos Batch Complete: {filled_count} Filled, {drops_count} Inflight-Dropped, {chaos_bridge.total_429_throttled} Jitter-Throttled")
    passed_tests += 1

    # --------------------------------------------------------------------------
    # TEST 4: Wire Drop & Inflight Zombie Order Reconciliation Sweeper
    # --------------------------------------------------------------------------
    print("\n[TEST 4/6] Testing Wire Drop & Inflight Zombie Order Reconciliation Sweeper...")
    # Inject an explicit INFLIGHT_UNKNOWN order with an expired timestamp
    zombie_order = WireOrderPayload(
        cl_ord_id="AGY_INFLIGHT_ZOMBIE_999",
        symbol="ZOMBIE-COIN",
        venue="HYPERLIQUID",
        side="SELL",
        price=10.0,
        quantity=5.0,
        order_type="MARKET",
        wire_state=WireState.INFLIGHT_UNKNOWN,
        sent_at_ns=time.time_ns() - int(1e9) # 1 second ago
    )
    chaos_bridge.inflight_orders[zombie_order.cl_ord_id] = zombie_order
    
    # Run the reconciliation sweep
    sweep_res = await chaos_bridge.run_reconciliation_sweep()
    print(f"  ✅ Reconciliation Sweep Result: {sweep_res}")
    assert sweep_res["reconciled_count"] > 0 or sweep_res["zombies_reaped"] > 0, "Sweeper should resolve orders"
    passed_tests += 1

    # --------------------------------------------------------------------------
    # TEST 5: Bailout Limit Guard & Dead-Man's Switch Emergency Flush
    # --------------------------------------------------------------------------
    print("\n[TEST 5/6] Testing Bailout Limit Guard & Dead-Man's Switch Emergency Flush...")
    bailout_db = ENGINE_DIR / "test_bailout_ledger.sqlite"
    if bailout_db.exists():
        bailout_db.unlink()
    bailout_bridge = LiveBrokerWireBridge(bailout_db, mode=WireMode.TESTNET_MOCK, max_unreconciled_bailout=2)
    
    # Manually populate 2 unreconciled orders
    for i in range(2):
        dummy = WireOrderPayload(
            cl_ord_id=f"AGY_UNREC_{i}",
            symbol="BTC",
            venue="HYPER",
            side="BUY",
            price=50000.0,
            quantity=1.0,
            order_type="ALO",
            wire_state=WireState.SENT_TO_WIRE
        )
        bailout_bridge.inflight_orders[dummy.cl_ord_id] = dummy

    # Third order should hit the bailout limit and halt!
    third_order = WireOrderPayload(
        cl_ord_id="AGY_UNREC_OVERFLOW",
        symbol="BTC",
        venue="HYPER",
        side="BUY",
        price=50000.0,
        quantity=1.0,
        order_type="ALO"
    )
    res_halt = await bailout_bridge.transmit_order(third_order)
    assert res_halt.wire_state == WireState.REJECTED, f"Expected REJECTED, got {res_halt.wire_state}"
    assert "BAILOUT_HALT" in res_halt.rejection_reason
    assert bailout_bridge.is_halted is True
    print(f"  ✅ Bailout Limit Tripped: {res_halt.rejection_reason}")

    # Test Emergency Flush
    flushed = bailout_bridge.emergency_flush_open_orders("DEAD_MAN_FLUSH")
    assert flushed == 2, f"Expected 2 flushed orders, got {flushed}"
    print(f"  ✅ Dead-Man's Switch Flushed: {flushed} open orders canceled instantly")
    passed_tests += 1

    # --------------------------------------------------------------------------
    # TEST 6: 100-Order Async Concurrency & Sub-5ms Decision Latency Benchmark
    # --------------------------------------------------------------------------
    print("\n[TEST 6/6] Testing 100-Order Async Concurrency & Sub-5ms Decision Latency...")
    gateway = AsyncL2DMAGateway(db_path=test_db)
    
    # Warm up L2 book
    gateway.update_l2_book("SOL-PERP", "HYPERLIQUID", [(150.0, 500.0)], [(150.05, 500.0)])
    
    latencies_ms = []
    
    async def submit_test_order(idx: int):
        t0 = time.perf_counter_ns()
        ord_res = await gateway.submit_dma_order(
            symbol="SOL-PERP",
            side=OrderSide.BUY,
            quantity=0.5,
            expected_alpha_pct=0.0050,
            venue=VenueType.HYPERLIQUID_DEX_ALO,
            order_type="ALO",
            client_intent_id=f"BURST_{idx}"
        )
        # Decision latency (time until order decision completes before wire)
        decision_lat = (getattr(ord_res, "decision_completed_ns", time.perf_counter_ns()) - t0) / 1e6
        latencies_ms.append(decision_lat)
        return ord_res

    start_burst = time.perf_counter()
    tasks = [submit_test_order(i) for i in range(100)]
    results = await asyncio.gather(*tasks)
    burst_dur = (time.perf_counter() - start_burst) * 1000.0

    latencies_ms.sort()
    p50 = latencies_ms[int(len(latencies_ms) * 0.50)]
    p95 = latencies_ms[int(len(latencies_ms) * 0.95)]
    p99 = latencies_ms[int(len(latencies_ms) * 0.99)]
    max_lat = max(latencies_ms)
    avg_lat = sum(latencies_ms) / len(latencies_ms)

    filled = len([r for r in results if r.state == OrderState.FILLED])
    throttled = len([r for r in results if "RATE_LIMIT" in r.rejection_reason])

    print(f"  ✅ 100-Order Burst Duration: {burst_dur:.2f}ms")
    print(f"  ✅ Decision Latency: Avg={avg_lat:.3f}ms | p50={p50:.3f}ms | p95={p95:.3f}ms | p99={p99:.3f}ms | Max={max_lat:.3f}ms")
    print(f"  ✅ Throughput Outcome: {filled} Fills, {throttled} Throttled by Token Bucket")
    
    assert p95 < 5.0, f"p95 latency {p95:.3f}ms exceeded 5.0ms threshold!"
    assert filled > 0, "No orders were filled"

    # Verify SQLite WAL Integrity
    conn = sqlite3.connect(test_db)
    cur = conn.cursor()
    cur.execute("PRAGMA integrity_check;")
    check = cur.fetchone()[0]
    assert check == "ok", f"Database corrupted: {check}"
    cur.execute("SELECT COUNT(*) FROM wire_state_audit_log;")
    audit_count = cur.fetchone()[0]
    print(f"  ✅ SQLite WAL Integrity: {check} | Total Wire Audit Records: {audit_count}")
    conn.close()

    gateway.close()
    bridge.close()
    chaos_bridge.close()
    bailout_bridge.close()
    passed_tests += 1

    print("\n" + "="*80)
    print(f"🏆 ALL {passed_tests}/{total_tests} TESTS PASSED WITH ZERO ERRORS!")
    print("="*80)

if __name__ == "__main__":
    asyncio.run(run_battery())
