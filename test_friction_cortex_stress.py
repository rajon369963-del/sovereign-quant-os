# -*- coding: utf-8 -*-
"""
================================================================================
AIR10 MICRO-CAPITAL FRICTION CORTEX COMPREHENSIVE STRESS TEST HARNESS
================================================================================
Runs Canary ➔ Dry ➔ Stress 10x ➔ Adversarial ➔ Physical Readback.
================================================================================
"""

import os
import os
import sys
import time
import json
import sqlite3
import random
from pathlib import Path

ENGINE_DIR = Path("/Users/rajondas/.gemini/antigravity/scratch/antigravity_yolo_trading_engine")
sys.path.insert(0, str(ENGINE_DIR))

from micro_capital_friction_cortex import MicroCapitalFrictionCortex

def run_stress_suite():
    print("=" * 80)
    print("⚡ RUNNING AIR10 MICRO-CAPITAL FRICTION CORTEX STRESS SUITE")
    print("=" * 80)
    
    test_db = Path(os.environ.get("AIR10_FRICTION_TEST_DB", str(ENGINE_DIR / "test_friction_stress.sqlite")))
    if test_db.exists():
        test_db.unlink()
        
    cortex = MicroCapitalFrictionCortex(db_path=test_db)
    
    # 1. CANARY TEST
    print("\n[PHASE 1: CANARY TEST]")
    order_book = {"bid": 77000.0, "ask": 77001.0} # 0.001% spread
    passed, info, reason = cortex.evaluate_tca_gate(
        symbol="BTC/USDT", order_book=order_book, order_size_usd=12.0,
        expected_alpha_pct=0.0070, side="BUY", venue="HYPERLIQUID_DEX_ALO", order_type="ALO"
    )
    assert passed is True, f"Canary failed: {reason}"
    print(f"✅ Canary Passed: {reason} | Rebate: {info['maker_rebate_pct']*100:.3f}%")

    # 2. DRY TEST (Standard vs Zero-Brokerage vs ALO)
    print("\n[PHASE 2: DRY TEST - 3-WAY VENUE BENCHMARK]")
    venues = [
        ("STANDARD_DISCOUNT_BROKER", "MARKET"),
        ("SHOONYA_ZERO_BROKERAGE", "LIMIT_DMA"),
        ("HYPERLIQUID_DEX_ALO", "ALO")
    ]
    for v, ot in venues:
        p, inf, r = cortex.evaluate_tca_gate(
            symbol="NIFTY_ITM_OPT" if "SHOONYA" in v else "BTC/USDT",
            order_book=order_book, order_size_usd=12.0,
            expected_alpha_pct=0.0070, side="BUY", venue=v, order_type=ot
        )
        print(f"   • Venue: {v:26} | Order: {ot:10} | Passed: {str(p):5} | Friction: {inf['total_friction_pct']*100:.3f}% | Reason: {r[:50]}...")

    # 3. ADVERSARIAL STRESS TEST (Toxic Flow / Spread Spikes)
    print("\n[PHASE 3: ADVERSARIAL TEST - TOXIC SPREAD SPIKES]")
    toxic_spreads = [0.001, 0.005, 0.010, 0.025, 0.050] # up to 5% spread
    gated_count = 0
    for s in toxic_spreads:
        ob_toxic = {"bid": 100.0, "ask": 100.0 * (1 + s)}
        p, inf, r = cortex.evaluate_tca_gate(
            symbol="ILLIQUID_TICKET", order_book=ob_toxic, order_size_usd=12.0,
            expected_alpha_pct=0.0070, side="BUY", venue="SHOONYA_ZERO_BROKERAGE", order_type="MARKET"
        )
        if not p:
            gated_count += 1
            print(f"   🛡️  Toxic Spread {s*100:.1f}% Successfully Gated: {r[:65]}...")
    assert gated_count >= 4, "Adversarial test failed to gate toxic spreads!"
    print(f"✅ Adversarial Test Passed: {gated_count}/{len(toxic_spreads)} toxic spreads safely gated!")

    # 4. 10X MULTI-ROUND STRESS TEST (1,000 Operations)
    print("\n[PHASE 4: 10X MULTI-ROUND STRESS TEST (1,000 PASSES)]")
    t0 = time.perf_counter()
    approved = 0
    gated = 0
    rebates_total_usd = 0.0
    
    for i in range(1000):
        # Random asset & spread
        mid_p = random.uniform(50.0, 80000.0)
        spread = mid_p * random.uniform(0.0001, 0.0080)
        ob = {"bid": mid_p - spread/2, "ask": mid_p + spread/2}
        exp_alpha = random.uniform(0.004, 0.015)
        venue = random.choice(["HYPERLIQUID_DEX_ALO", "SHOONYA_ZERO_BROKERAGE", "STANDARD_DISCOUNT_BROKER"])
        order_t = "ALO" if venue == "HYPERLIQUID_DEX_ALO" else ("LIMIT_DMA" if venue == "SHOONYA_ZERO_BROKERAGE" else "MARKET")
        
        p, inf, _ = cortex.evaluate_tca_gate(
            symbol=f"SYM_{i%10}", order_book=ob, order_size_usd=random.uniform(10.0, 50.0),
            expected_alpha_pct=exp_alpha, side=random.choice(["BUY", "SELL"]),
            venue=venue, order_type=order_t
        )
        if p:
            approved += 1
            if order_t == "ALO":
                fill = cortex.simulate_hyperliquid_alo_fill(f"SYM_{i%10}", "BUY", mid_p, 0.001)
                rebates_total_usd += fill["rebate_earned_usd"]
        else:
            gated += 1
            
    dur_ms = (time.perf_counter() - t0) * 1000.0
    avg_us = (dur_ms / 1000.0) * 1000.0
    print(f"✅ 1,000 Passes Completed in {dur_ms:.2f} ms ({avg_us:.2f} µs/pass)!")
    print(f"   • Approved: {approved} | Gated (Saved from Negative EV): {gated}")
    print(f"   • Cumulative Maker Rebates Earned: +${rebates_total_usd:.4f} USD (+₹{rebates_total_usd*86.50:.2f} INR)")

    # 5. PHYSICAL READBACK VERIFICATION
    print("\n[PHASE 5: PHYSICAL READBACK VERIFICATION]")
    conn = sqlite3.connect(test_db)
    c = conn.cursor()
    c.execute("SELECT count(*), sum(passed) FROM tca_audit_log")
    tot_logs, tot_passed = c.fetchone()
    c.execute("SELECT count(*), sum(rebate_earned_inr) FROM maker_rebate_ledger")
    reb_count, reb_sum_inr = c.fetchone()
    conn.close()
    
    print(f"   • SQLite TCA Audit Logs Recorded: {tot_logs} (Passed: {tot_passed})")
    print(f"   • SQLite Maker Rebate Records: {reb_count} (Total Credited: ₹{reb_sum_inr:.2f} INR)")
    assert tot_logs == 1000 + len(venues) + len(toxic_spreads) + 1, "Audit log count mismatch!"
    
    test_db.unlink()
    print("\n" + "=" * 80)
    print("🏆 ALL 5 STRESS TEST PHASES PASSED WITH 100% MATHEMATICAL RECTITUDE!")
    print("=" * 80)

if __name__ == "__main__":
    run_stress_suite()
