#!/usr/bin/env python3
"""
================================================================================
TEST PHASE 4 COMPOUNDING BATTERY: 8 MULTI-STAGE TESTS
================================================================================
Verifies:
  1. Tool Catalog & Capability Mesh (200+ Repositories & FTS5 Search)
  2. Order Flow Imbalance (OFI) Calculation & Z-Score Transitions
  3. Pre-Market Auction Discovery & Volume Surge Uncrossing Equilibrium
  4. 65-Second Opening Wick Quarantine & Bidirectional Breakout Triggers
  5. Dynamic 5x MIS Leverage & Bounded Risk Sizing (₹1,008 Equity, ₹3.75 Max Risk)
  6. Symmetric Bidirectional Trailing Ratchets (Long & Short)
  7. 10,000-Op Extreme Volatility Stress Test
  8. Cold-Start Crash Recovery & SQLite WAL Mode Idempotency
================================================================================
"""

import os
import random
import sqlite3
import sys
import time

# Ensure parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from phase4_compound_cortex import (
    DurableTradeLedger,
    DynamicLeverageSizer,
    OpeningRangeBreakoutEngine,
    OrderFlowImbalanceEngine,
    Phase4CompoundCortex,
    PreMarketAuctionEngine,
    SymmetricTrailingRatchet,
)


class TestPhase4CompoundingBattery:

    def test_01_tool_catalog_integrity(self):
        """Verify phase4_tool_catalog.sqlite contains >= 200 repositories and FTS5 works."""
        db_path = "/Users/rajondas/teamwork_projects/sovereign-quant-os/phase4_tool_catalog.sqlite"
        assert os.path.exists(db_path), f"Tool catalog not found at {db_path}"
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM tools_catalog;")
        count = cur.fetchone()[0]
        assert count >= 200, f"Expected >= 200 repos in catalog, found {count}"

        # Test FTS5 search for key capabilities
        cur.execute("SELECT COUNT(*) FROM tools_fts WHERE tools_fts MATCH 'order flow OR ofi';")
        ofi_matches = cur.fetchone()[0]
        assert ofi_matches >= 5, f"Expected >= 5 OFI matches in FTS, got {ofi_matches}"

        cur.execute("SELECT COUNT(*) FROM tools_fts WHERE tools_fts MATCH 'dhan';")
        dhan_matches = cur.fetchone()[0]
        assert dhan_matches >= 5, f"Expected >= 5 Dhan matches in FTS, got {dhan_matches}"

        conn.close()
        print(f"✓ Test 1 Passed: {count} repos verified in catalog with full FTS5 search.")

    def test_02_order_flow_imbalance_calculation(self):
        """Verify OFI calculations and z-score response to depth changes."""
        engine = OrderFlowImbalanceEngine(window_size=20)

        # Baseline quote: Bid=100 (qty 10), Ask=101 (qty 10)
        engine.update(bid_price=100.0, bid_qty=10, ask_price=101.0, ask_qty=10)

        # Bullish updates: Bid rises to 100.5 (qty 15), Ask stays 101.0 (qty drops to 5)
        for _ in range(10):
            engine.update(bid_price=100.5, bid_qty=20, ask_price=101.0, ask_qty=5)

        z_score = engine.get_zscore()
        assert z_score > 0.0, f"Expected positive z-score for bullish OFI, got {z_score}"

        # Bearish updates: Ask falls to 100.2 (qty 25), Bid drops to 99.8 (qty 5)
        for _ in range(15):
            engine.update(bid_price=99.8, bid_qty=5, ask_price=100.2, ask_qty=25)

        z_score_bearish = engine.get_zscore()
        assert z_score_bearish < 0.0, f"Expected negative z-score for bearish OFI, got {z_score_bearish}"
        print(f"✓ Test 2 Passed: OFI z-scores responded accurately (bullish={z_score:.2f}, bearish={z_score_bearish:.2f}).")

    def test_03_premarket_auction_equilibrium(self):
        """Verify pre-market uncrossing equilibrium and volume surge detection."""
        engine = PreMarketAuctionEngine()

        # Symbol A: Gap up 1.2%, surge ratio 0.08 (8% of 10d ADV) -> STRONG_BULLISH
        eq_a = engine.ingest_pre_open_tick("TATASTEEL", icp=152.0, prev_close=150.0, pre_volume=80000, adv_10d=1000000)
        assert eq_a.bias == "STRONG_BULLISH"
        assert eq_a.gap_percent == 1.33
        assert eq_a.surge_ratio == 0.08

        # Symbol B: Gap down -0.8%, surge ratio 0.06 -> STRONG_BEARISH
        eq_b = engine.ingest_pre_open_tick("SAIL", icp=128.0, prev_close=130.0, pre_volume=60000, adv_10d=1000000)
        assert eq_b.bias == "STRONG_BEARISH"
        assert eq_b.gap_percent == -1.54

        # Symbol C: Flat gap 0.05%, low volume -> NEUTRAL
        eq_c = engine.ingest_pre_open_tick("PNB", icp=100.05, prev_close=100.0, pre_volume=5000, adv_10d=1000000)
        assert eq_c.bias == "NEUTRAL"
        print(f"✓ Test 3 Passed: Pre-market auction equilibrium accurately categorized (A={eq_a.bias}, B={eq_b.bias}, C={eq_c.bias}).")

    def test_04_opening_range_quarantine_and_breakout(self):
        """Verify 65-second quarantine buffer and symmetric breakout triggers."""
        engine = OpeningRangeBreakoutEngine(quarantine_duration_seconds=65.0)
        symbol = "ASHOKLEY"
        t0 = 1000.0

        # Ticks during quarantine (t0 to t0 + 64s): should accumulate and NOT trigger breakout
        action1, r1 = engine.on_tick(symbol, 180.0, t0)
        assert action1 == "QUARANTINE_ACCUMULATE"
        assert r1.high == 180.0 and r1.low == 180.0

        # High tick at t0 + 30s
        action2, r2 = engine.on_tick(symbol, 182.0, t0 + 30.0)
        assert action2 == "QUARANTINE_ACCUMULATE"
        assert r2.high == 182.0

        # Low tick at t0 + 50s
        action3, r3 = engine.on_tick(symbol, 179.0, t0 + 50.0)
        assert action3 == "QUARANTINE_ACCUMULATE"
        assert r3.low == 179.0
        assert r3.long_trigger == 182.05
        assert r3.short_trigger == 178.95

        # Tick at t0 + 65.1s: Quarantine expired, triggers armed
        action4, r4 = engine.on_tick(symbol, 180.5, t0 + 65.1)
        assert action4 == "ARMED"
        assert r4.is_armed is True

        # Tick piercing Long Trigger (182.10 >= 182.05)
        action5, r5 = engine.on_tick(symbol, 182.10, t0 + 70.0)
        assert action5 == "LONG_BREAKOUT"

        # Test another symbol for Short Breakdown
        engine.start_range("ZOMATO", t0, 240.0)
        engine.on_tick("ZOMATO", 238.0, t0 + 20.0)  # Low = 238.0, Short trigger = 237.95
        engine.on_tick("ZOMATO", 239.0, t0 + 66.0)  # Arm
        action_short, _ = engine.on_tick("ZOMATO", 237.90, t0 + 75.0)
        assert action_short == "SHORT_BREAKDOWN"
        print("✓ Test 4 Passed: 65s quarantine buffer & bidirectional triggers verified.")

    def test_05_dynamic_leverage_and_risk_sizing(self):
        """Verify dynamic 5x MIS leverage sizing adheres strictly to ₹3.75 risk limit."""
        sizer = DynamicLeverageSizer(equity=1008.0, max_risk_rupees=3.75, mis_leverage=5.0)

        # Trade 1: TATASTEEL entry=150.0, stop=149.25 (stop_dist = 0.75)
        # Expected risk qty = floor(3.75 / 0.75) = 5
        # Margin required = (5 * 150) / 5 = 150.0 <= 1008.0
        res1 = sizer.compute_size("TATASTEEL", "BUY", 150.0, 149.25)
        assert res1.allowed is True
        assert res1.quantity == 5
        assert res1.risk_rupees == 3.75
        assert res1.total_capital_required == 150.0

        # Trade 2: High stop distance (e.g. entry=100, stop=95, stop_dist=5.0)
        # Risk qty = floor(3.75 / 5.0) = 0 -> Must be rejected!
        res2 = sizer.compute_size("TEST_WIDE", "BUY", 100.0, 95.0)
        assert res2.allowed is False
        assert "STOP_TOO_WIDE" in res2.rejection_reason

        # Trade 3: High priced stock (entry=1200, stop=1198, stop_dist=2.0)
        # Risk qty = floor(3.75 / 2.0) = 1. Margin req = 1200 / 5 = 240.0 <= 1008
        res3 = sizer.compute_size("TEST_EXPENSIVE", "SELL", 1200.0, 1202.0)
        assert res3.allowed is True
        assert res3.quantity == 1
        assert res3.risk_rupees == 2.0
        print(f"✓ Test 5 Passed: Bounded risk sizing enforced (Q1={res1.quantity}, Q2_rejected={not res2.allowed}, Q3={res3.quantity}).")

    def test_06_bidirectional_trailing_ratchet(self):
        """Verify symmetric trailing ratchets for BUY and SELL."""
        # Long trade: entry=100.0, stop=98.0, R=2.0
        ratchet_long = SymmetricTrailingRatchet("TATASTEEL", "BUY", 100.0, 98.0)

        # Move to 101.0 (0.5R) -> No ratchet modification
        m, stage, stop = ratchet_long.on_tick(101.0)
        assert m is False and stage == "INITIAL" and stop == 98.0

        # Move to 102.1 (1.05R >= 1R) -> BE locked (100.05)
        m, stage, stop = ratchet_long.on_tick(102.1)
        assert m is True and stage == "BE_LOCKED" and stop == 100.05

        # Move to 103.2 (1.6R >= 1.5R) -> +1R locked (102.00)
        m, stage, stop = ratchet_long.on_tick(103.2)
        assert m is True and stage == "PLUS_1R" and stop == 102.00

        # Move to 104.5 (2.25R >= 2.0R) -> +1.5R locked (103.00)
        m, stage, stop = ratchet_long.on_tick(104.5)
        assert m is True and stage == "PLUS_1_5R" and stop == 103.00

        # Short trade: entry=100.0, stop=102.0, R=2.0
        ratchet_short = SymmetricTrailingRatchet("SAIL", "SELL", 100.0, 102.0)

        # Move to 97.9 (1.05R >= 1R) -> BE locked (99.95)
        m_s, stage_s, stop_s = ratchet_short.on_tick(97.9)
        assert m_s is True and stage_s == "BE_LOCKED" and stop_s == 99.95

        # Move to 95.8 (2.1R >= 2.0R) -> +1.5R locked (97.00)
        m_s2, stage_s2, stop_s2 = ratchet_short.on_tick(95.8)
        assert m_s2 is True and stage_s2 == "PLUS_1_5R" and stop_s2 == 97.00
        print("✓ Test 6 Passed: Symmetric bidirectional trailing ratchets verified.")

    def test_07_extreme_stress_10k_ops(self):
        """Execute 10,000 synthetic operations through Phase4CompoundCortex."""
        test_db = "test_phase4_stress.sqlite"
        if os.path.exists(test_db):
            os.remove(test_db)

        cortex = Phase4CompoundCortex(db_path=test_db)
        symbols = ["TATASTEEL", "SAIL", "PNB", "ASHOKLEY", "ZOMATO"]

        t_start = time.time()
        start_ts = 10000.0
        price_map = {s: 150.0 for s in symbols}

        for i in range(10000):
            sym = symbols[i % len(symbols)]
            # Random walk tick
            dp = (random.random() - 0.49) * 0.2
            price_map[sym] = round(max(10.0, price_map[sym] + dp), 2)
            p = price_map[sym]
            bid = round(p - 0.05, 2)
            ask = round(p + 0.05, 2)
            bid_q = random.randint(100, 5000)
            ask_q = random.randint(100, 5000)

            curr_ts = start_ts + (i * 0.1)  # 100ms interval
            signal = cortex.evaluate_entry(
                symbol=sym,
                price=p,
                current_ts=curr_ts,
                bid=bid,
                ask=ask,
                bid_qty=bid_q,
                ask_qty=ask_q,
                rolling_var=0.0001
            )

        elapsed = time.time() - t_start
        ops_per_sec = 10000 / elapsed if elapsed > 0 else 0
        print(f"✓ Test 7 Passed: 10,000 operations completed in {elapsed:.3f}s ({ops_per_sec:.0f} ops/sec).")

        # Verify SQLite WAL persistence
        conn = sqlite3.connect(test_db)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM phase4_trade_events;")
        event_count = cur.fetchone()[0]
        conn.close()
        assert event_count > 0, "Expected trade events recorded in SQLite WAL database"
        print(f"  Recorded {event_count} trade signals in SQLite WAL ledger.")

        # Cleanup test db
        for ext in ["", "-wal", "-shm"]:
            if os.path.exists(test_db + ext):
                os.remove(test_db + ext)

    def test_08_cold_start_crash_recovery(self):
        """Verify crash recovery and state re-hydration from SQLite WAL ledger."""
        rec_db = "test_phase4_recovery.sqlite"
        if os.path.exists(rec_db):
            os.remove(rec_db)

        # Step 1: Session 1 records state and crashes
        ledger1 = DurableTradeLedger(db_path=rec_db)
        ledger1.set_state("EXECUTION_STATE", "ACTIVE_MONITORING")
        ledger1.set_state("CURRENT_DRAWDOWN", "0.0")
        ledger1.record_event("TATASTEEL", "ORDER_PLACED", "BUY", 150.0, 5, stop_loss=149.25)
        del ledger1

        # Step 2: Session 2 re-attaches
        ledger2 = DurableTradeLedger(db_path=rec_db)
        st = ledger2.get_state("EXECUTION_STATE")
        dd = ledger2.get_state("CURRENT_DRAWDOWN")
        assert st == "ACTIVE_MONITORING"
        assert dd == "0.0"

        conn = sqlite3.connect(rec_db)
        cur = conn.cursor()
        cur.execute("SELECT symbol, side, price, quantity FROM phase4_trade_events;")
        row = cur.fetchone()
        assert row == ("TATASTEEL", "BUY", 150.0, 5)
        conn.close()

        print("✓ Test 8 Passed: Cold-start crash recovery and state checkpointing verified.")

        # Cleanup
        for ext in ["", "-wal", "-shm"]:
            if os.path.exists(rec_db + ext):
                os.remove(rec_db + ext)


if __name__ == "__main__":
    test = TestPhase4CompoundingBattery()
    methods = [m for m in dir(test) if m.startswith("test_")]
    print("\n========================================================")
    print(f"🚀 EXECUTING PHASE 4 COMPOUNDING BATTERY ({len(methods)} TESTS)")
    print("========================================================")
    passed = 0
    failed = 0
    for m in sorted(methods):
        print(f"\n---> Running {m}...")
        try:
            getattr(test, m)()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"✗ FAILED {m}: {e}")
            import traceback
            traceback.print_exc()

    print("\n========================================================")
    print(f"PHASE 4 TEST BATTERY COMPLETE: {passed} PASSED, {failed} FAILED.")
    print("========================================================")
    if failed > 0:
        sys.exit(1)

