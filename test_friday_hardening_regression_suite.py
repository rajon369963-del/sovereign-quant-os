"""
⚡ FRIDAY HARDENING REGRESSION TEST SUITE (SEP 18, 2026 INVARIANTS)
===================================================================
Automated regression suite verifying:
1. Syntax, imports, and schema contracts across all core modules.
2. Friday Sep 18, 2026 locked parameters:
   - MAX_DAILY_TRADES = 2
   - MAX_TURNOVER_CAP = 2500.0
   - NOISE_AVOIDANCE_SLEEP_UNTIL = '10:15:00'
   - COOLDOWN_SECONDS = 900.0 (15 min)
   - TICK_SIZE_QUANTIZATION = 0.05
3. Strict NSE Tick Size Quantization (round(price * 20) / 20).
4. Pre-Flight Turnover Hard-Cap Throttling (NautilusTrader OrderThrottler pattern).
5. Risk-Reducing Exit Invariant (exits permitted even when turnover cap reached).
6. Anti-Churn Cooldown Lockout (15 min / 900s per symbol post-exit).
7. Daily Trade Limit Gate (Vivek Bajaj & bot_live_parameters max 2 completed trades).
8. Noise Avoidance & Entry Window Timing Discipline.
9. 3:10 PM Graceful Auto-Square-Off with 0 Net Residue across 4 positions.
10. Single-Instance POSIX Flock Mutex.
"""

import asyncio
import datetime
import json
import os
import sys
import time
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Core imports to verify syntax and availability
from dhan_live_bridge import DhanLiveBridge
from dhan_sniper_momentum_engine import CandidateStock, DhanSniperMomentumEngine
from nine_mentors_live_shield import NineMentorsLiveShield


class FridayHardeningRegressionSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = REPO_ROOT / "config" / "bot_live_parameters.json"
        with open(cls.config_path, "r", encoding="utf-8") as f:
            cls.config = json.load(f)

    # --------------------------------------------------------------------------
    # TEST 1: Parameter Lock-In for Friday Sep 18, 2026
    # --------------------------------------------------------------------------
    def test_01_parameter_lock_in_config(self):
        """Verifies bot_live_parameters.json contains the exact locked parameters."""
        cap_law = self.config["CAPITAL_PRESERVATION_LAW"]
        timing = self.config["TIMING_DISCIPLINE"]
        rules = self.config["EXECUTION_RULES"]

        self.assertEqual(cap_law["MAX_DAILY_TRADES"], 2)
        self.assertEqual(float(cap_law["MAX_TURNOVER_CAP"]), 2500.0)
        self.assertEqual(timing["NOISE_AVOIDANCE_SLEEP_UNTIL"], "10:15:00")
        self.assertEqual(timing["NO_NEW_ENTRIES_AFTER"], "14:15:00")
        self.assertEqual(timing["MANDATORY_GRACEFUL_SQUARE_OFF"], "15:10:00")
        self.assertEqual(float(rules["TICK_SIZE_QUANTIZATION"]), 0.05)
        self.assertEqual(float(rules["COOLDOWN_SECONDS"]), 900.0)
        self.assertEqual(rules["COOLDOWN_MINUTES_AFTER_EXIT"], 15)

    def test_02_engine_and_shield_parameter_binding(self):
        """Verifies engine, bridge, and shield dynamically bind the locked parameters."""
        bridge = DhanLiveBridge(dry_run=True)
        self.assertEqual(bridge.max_daily_turnover, 2500.0)

        engine = DhanSniperMomentumEngine(initial_capital=918.43, dry_run=True)
        self.assertEqual(engine.max_daily_trades, 2)
        self.assertEqual(engine.max_turnover_cap, 2500.0)
        self.assertEqual(engine.noise_avoidance_sleep_until, "10:15:00")
        self.assertEqual(engine.no_new_entries_after, "14:15:00")
        self.assertEqual(engine.cooldown_seconds, 900.0)
        self.assertEqual(engine.tick_size_quantization, 0.05)

        # Shield parameters
        shield = NineMentorsLiveShield(initial_capital=918.43)
        self.assertEqual(shield.max_daily_trades, 2)
        self.assertEqual(shield.max_turnover_cap, 2500.0)
        self.assertEqual(shield.max_allowed_turnover, 2500.0)
        self.assertEqual(shield.noise_avoidance_sleep_until, "10:15:00")
        self.assertEqual(shield.cooldown_seconds, 900.0)
        self.assertEqual(shield.tick_size_quantization, 0.05)

    # --------------------------------------------------------------------------
    # TEST 3: Strict NSE Tick Size Quantization (0.05 Multiple)
    # --------------------------------------------------------------------------
    def test_03_strict_tick_size_quantization(self):
        """Tests that quantize_tick forces prices to exact multiples of 0.05."""
        test_cases = [
            (100.01, 100.00),
            (100.02, 100.00),
            (100.03, 100.05),
            (100.04, 100.05),
            (100.06, 100.05),
            (100.07, 100.05),
            (100.08, 100.10),
            (100.09, 100.10),
            (52.33, 52.35),
            (123.49, 123.50),
            (183.74, 183.75),
            (0.0, 0.0),
            (-5.0, 0.0),
        ]
        for raw, expected in test_cases:
            quantized = DhanLiveBridge.quantize_tick(raw)
            self.assertEqual(quantized, expected, f"Failed for {raw}: got {quantized}, expected {expected}")
            if quantized > 0:
                # Modulo 0.05 must be essentially 0
                cents = round(quantized * 100)
                self.assertEqual(cents % 5, 0, f"{quantized} is not a multiple of 0.05")

    # --------------------------------------------------------------------------
    # TEST 4: Pre-Flight Turnover Hard-Cap Throttling (NautilusTrader Pattern)
    # --------------------------------------------------------------------------
    def test_04_turnover_hard_cap_throttler(self):
        """Tests that entry orders exceeding ₹2500 cumulative turnover are throttled."""
        bridge = DhanLiveBridge(dry_run=True)
        bridge.cumulative_turnover = 2400.0  # ₹100 remaining before ₹2500 cap

        # Order of ₹150 (exceeds remaining budget)
        rejected_order = bridge.execute_micro_order(
            symbol="TATASTEEL",
            security_id="3499",
            quantity=1,
            side="BUY",
            price=150.0,
            dry_run=True,
            is_entry=True,
        )
        self.assertEqual(rejected_order["status"], "REJECTED")
        self.assertEqual(rejected_order["result_class"], "TURNOVER_CAP_EXCEEDED")
        self.assertEqual(rejected_order["execution_mode"], "THROTTLER_BLOCKED")
        self.assertEqual(bridge.cumulative_turnover, 2400.0)  # Turnover unchanged

    # --------------------------------------------------------------------------
    # TEST 5: Risk-Reducing Exit Invariant
    # --------------------------------------------------------------------------
    def test_05_risk_reducing_exit_permitted_at_cap(self):
        """Tests that EXIT orders (is_entry=False) are NEVER blocked by the turnover throttler."""
        bridge = DhanLiveBridge(dry_run=True)
        bridge.cumulative_turnover = 2600.0  # Already above ₹2500 cap

        exit_order = bridge.execute_micro_order(
            symbol="TATASTEEL",
            security_id="3499",
            quantity=10,
            side="SELL",
            price=150.0,
            dry_run=True,
            is_entry=False,  # Risk-reducing exit
        )
        # Must be approved, not rejected by turnover throttler
        self.assertEqual(exit_order["status"], "ORDER_PLACED")
        self.assertEqual(exit_order["result_class"], "SIMULATED_ORDER")

    # --------------------------------------------------------------------------
    # TEST 6: Anti-Churn Cooldown Lockout (15 min / 900s)
    # --------------------------------------------------------------------------
    def test_06_anti_churn_cooldown_lockout(self):
        """Tests 15-minute anti-churn lockout post-exit."""
        engine = DhanSniperMomentumEngine(initial_capital=918.43, dry_run=True)
        symbol = "TATASTEEL"

        # Initially not in cooldown
        self.assertFalse(engine.is_symbol_in_cooldown(symbol))
        self.assertEqual(engine.get_symbol_cooldown_remaining(symbol), 0.0)

        # Mock an active position
        engine.active_positions[symbol] = {
            "symbol": symbol,
            "security_id": "3499",
            "side": "BUY",
            "quantity": 10,
            "entry_price": 150.0,
            "stop_loss": 148.5,
            "take_profit": 153.0,
            "highest_price": 150.0,
            "lowest_price": 150.0,
            "entry_time": time.time(),
        }

        # Close position
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            close_res = loop.run_until_complete(engine.close_position(152.0, symbol=symbol, reason="MANUAL_TEST"))
            self.assertEqual(close_res["status"], "POSITION_CLOSED")

            # Symbol should now be in cooldown
            self.assertTrue(engine.is_symbol_in_cooldown(symbol))
            rem = engine.get_symbol_cooldown_remaining(symbol)
            self.assertGreater(rem, 890.0)
            self.assertLessEqual(rem, 900.0)

            # Another symbol should NOT be in cooldown
            self.assertFalse(engine.is_symbol_in_cooldown("PNB"))

            # Trying to evaluate tick stream for TATASTEEL during market hours should return COOLDOWN_ACTIVE
            with patch.object(engine, "is_square_off_time", return_value=False):
                eval_res = loop.run_until_complete(engine.evaluate_tick_stream(symbol, 152.0, 151.95, 152.05))
                self.assertIsNotNone(eval_res)
                self.assertEqual(eval_res.get("status"), "COOLDOWN_ACTIVE")
        finally:
            loop.close()

    # --------------------------------------------------------------------------
    # TEST 7: Daily Trade Limit Gate (Max 2 Completed Trades)
    # --------------------------------------------------------------------------
    def test_07_daily_trade_limit_gate(self):
        """Tests that when max_daily_trades (2) is reached, new entries are blocked."""
        engine = DhanSniperMomentumEngine(initial_capital=918.43, dry_run=True)
        engine.active_stage.trades_executed = 2  # Max limit reached

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            # Force market open
            with patch.object(engine, "is_market_open_for_entry", return_value=True):
                # Attempt entry on a qualified candidate
                engine.premarket_candidates["ITC"] = CandidateStock(
                    symbol="ITC",
                    security_id="1660",
                    previous_close=410.0,
                    open_price=415.0,
                    current_price=416.0,
                    gap_pct=1.22,
                    gap_factor=0.0122,
                    safe_leverage=4.5,
                    max_buying_power=2000.0,
                    approved_quantity=2,
                    risk_rupees=10.0,
                    stop_loss_distance=2.0,
                    status="TARGET_LONG",
                    rejection_reason=None,
                )
                entry_res = loop.run_until_complete(
                    engine._check_entry_opportunity("ITC", 416.0, 415.95, 416.05, side="BUY")
                )
                self.assertIsNone(entry_res, "Expected entry to be blocked when trades_executed >= max_daily_trades")
        finally:
            loop.close()

    # --------------------------------------------------------------------------
    # TEST 8: Noise Avoidance & Entry Window Timing Discipline
    # --------------------------------------------------------------------------
    def test_08_noise_avoidance_and_entry_window_timing(self):
        """Tests time discipline gates: Noise avoidance (before 10:15), Window open (10:15-14:15), Cutoff (after 14:15)."""
        engine = DhanSniperMomentumEngine(initial_capital=918.43, dry_run=True)

        # Helper to simulate IST datetime on a weekday (Friday 2026-09-18)
        def make_dt(hour, minute, second):
            return datetime.datetime(2026, 9, 18, hour, minute, second, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

        # 1. 09:30:00 IST -> Morning noise chop zone (must be False)
        dt_0930 = make_dt(9, 30, 0)
        self.assertFalse(engine.is_market_open_for_entry(dt_0930), "09:30 AM should be blocked by noise avoidance")

        # 2. 10:14:59 IST -> Just before 10:15:00 IST (must be False)
        dt_1014 = make_dt(10, 14, 59)
        self.assertFalse(engine.is_market_open_for_entry(dt_1014), "10:14:59 AM should be blocked by noise avoidance")

        # 3. 10:15:01 IST -> Professional setup window open (must be True)
        dt_1015 = make_dt(10, 15, 1)
        self.assertTrue(engine.is_market_open_for_entry(dt_1015), "10:15:01 AM should be open for entry")

        # 4. 14:14:59 IST -> Just before 14:15:00 IST cutoff (must be True)
        dt_1414 = make_dt(14, 14, 59)
        self.assertTrue(engine.is_market_open_for_entry(dt_1414), "14:14:59 PM should be open for entry")

        # 5. 14:15:01 IST -> Professional setup window closed (must be False)
        dt_1415 = make_dt(14, 15, 1)
        self.assertFalse(engine.is_market_open_for_entry(dt_1415), "14:15:01 PM should be blocked by entry cutoff")

        # 6. 15:10:00 IST -> Square-off cutoff (is_square_off_time must be True)
        dt_1510 = make_dt(15, 10, 0)
        self.assertTrue(engine.is_square_off_time(dt_1510), "15:10:00 PM should trigger is_square_off_time")

    # --------------------------------------------------------------------------
    # TEST 9: 3:10 PM Graceful Auto-Square-Off Across 4 Positions
    # --------------------------------------------------------------------------
    def test_09_graceful_auto_square_off_four_positions(self):
        """Simulates 4 positions (TATASTEEL, PNB, ITC, RBLBANK) squared off at 3:10 PM with 0 net quantity left."""
        engine = DhanSniperMomentumEngine(initial_capital=918.43, dry_run=True)
        test_positions = {
            "TATASTEEL": {"quantity": 10, "entry_price": 152.40, "side": "BUY", "security_id": "3499", "cl_ord_id": "cl_tata_001"},
            "PNB": {"quantity": 15, "entry_price": 101.10, "side": "BUY", "security_id": "10666", "cl_ord_id": "cl_pnb_001"},
            "ITC": {"quantity": 5, "entry_price": 412.50, "side": "BUY", "security_id": "1660", "cl_ord_id": "cl_itc_001"},
            "RBLBANK": {"quantity": 8, "entry_price": 183.75, "side": "BUY", "security_id": "18391", "cl_ord_id": "cl_rbl_001"},
        }
        for sym, data in test_positions.items():
            engine.active_positions[sym] = {
                "symbol": sym,
                "security_id": data["security_id"],
                "cl_ord_id": data["cl_ord_id"],
                "side": data["side"],
                "quantity": data["quantity"],
                "entry_price": data["entry_price"],
                "stop_loss": data["entry_price"] * 0.992,
                "take_profit": data["entry_price"] * 1.016,
                "highest_price": data["entry_price"],
                "lowest_price": data["entry_price"],
            }

        self.assertEqual(len(engine.active_positions), 4)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            # Force square-off time
            with patch.object(engine, "is_square_off_time", return_value=True):
                # Call evaluate_tick_stream which triggers 3:10 PM square-off
                res = loop.run_until_complete(
                    engine.evaluate_tick_stream("TATASTEEL", 153.0, 152.95, 153.05)
                )
                self.assertIsNotNone(res)
                self.assertEqual(res.get("status"), "INACTIVE")
                self.assertEqual(res.get("reason"), "POST_MARKET_HOURS")
                # Active positions must now be completely empty
                self.assertEqual(len(engine.active_positions), 0)
        finally:
            loop.close()

    # --------------------------------------------------------------------------
    # TEST 10: POSIX Flock Single-Instance Mutex
    # --------------------------------------------------------------------------
    def test_10_posix_flock_single_instance(self):
        """Verifies POSIX flock mutex behavior preventing duplicate process execution."""
        import fcntl
        lock_path = "/tmp/test_dhan_bot_atomic.lock"
        fd1 = open(lock_path, "w")
        fcntl.flock(fd1, fcntl.LOCK_EX | fcntl.LOCK_NB)

        # Second lock attempt must fail with BlockingIOError / OSError
        fd2 = open(lock_path, "w")
        with self.assertRaises((BlockingIOError, OSError)):
            fcntl.flock(fd2, fcntl.LOCK_EX | fcntl.LOCK_NB)

        # Release fd1
        fcntl.flock(fd1, fcntl.LOCK_UN)
        fd1.close()
        fd2.close()
        if os.path.exists(lock_path):
            os.remove(lock_path)

    # --------------------------------------------------------------------------
    # TEST 11: Date-Filtered Turnover Sync (Zero Stale Lockout Invariant)
    # --------------------------------------------------------------------------
    def test_11_sync_daily_turnover_date_filtering(self):
        """Tests that sync_daily_turnover ignores trades from previous calendar sessions."""
        bridge = DhanLiveBridge(dry_run=True)
        bridge.dhan = unittest.mock.MagicMock()
        bridge.is_connected = True

        # Mock trade book with yesterday's trades (₹40,000 turnover on Sep 17)
        mock_trades = [
            {
                "tradingSymbol": "PNB",
                "tradedQuantity": 100,
                "tradedPrice": 100.0,
                "exchangeTime": "2026-09-17 09:30:00",
                "createTime": "2026-09-17 09:30:00",
            },
            {
                "tradingSymbol": "TATASTEEL",
                "tradedQuantity": 200,
                "tradedPrice": 150.0,
                "exchangeTime": "2026-09-17 11:00:00",
                "createTime": "2026-09-17 11:00:00",
            },
        ]
        bridge.dhan.get_trade_book.return_value = {"status": "success", "data": mock_trades}

        # Simulate running on tomorrow Friday Sep 18, 2026
        bridge.sync_daily_turnover(target_date="2026-09-18")
        # Stale trades from Sep 17 must NOT be counted on Sep 18
        self.assertEqual(bridge.cumulative_turnover, 0.0, "Yesterday's trades must be filtered out by date")

        # Now add a trade with Sep 18 timestamp
        mock_trades.append({
            "tradingSymbol": "ITC",
            "tradedQuantity": 2,
            "tradedPrice": 415.0,
            "exchangeTime": "2026-09-18 10:20:00",
            "createTime": "2026-09-18 10:20:00",
        })
        bridge.dhan.get_trade_book.return_value = {"status": "success", "data": mock_trades}
        bridge.sync_daily_turnover(target_date="2026-09-18")
        self.assertEqual(bridge.cumulative_turnover, 830.0, "Only today's trades should be counted")

    # --------------------------------------------------------------------------
    # TEST 12: Non-Duplication of Broker Exits on Physical Reconciled Square-Off
    # --------------------------------------------------------------------------
    def test_12_non_duplication_on_broker_reconciled_square_off(self):
        """Tests dispatch_broker_order=False skips sending duplicate broker order when position already squared off."""
        engine = DhanSniperMomentumEngine(initial_capital=918.43, dry_run=True)
        symbol = "TATASTEEL"
        engine.active_positions[symbol] = {
            "symbol": symbol,
            "security_id": "3499",
            "side": "BUY",
            "quantity": 10,
            "entry_price": 150.0,
            "stop_loss": 148.5,
            "take_profit": 153.0,
            "highest_price": 150.0,
            "lowest_price": 150.0,
            "cl_ord_id": "test_tata_reconcile",
        }

        with patch.object(engine.bridge, "execute_micro_order") as mock_exec:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                # Close position with dispatch_broker_order=False (already executed at physical broker)
                res = loop.run_until_complete(
                    engine.close_position(152.0, symbol=symbol, reason="TIME_CUTOFF_0310_PM", dispatch_broker_order=False)
                )
                self.assertEqual(res["status"], "POSITION_CLOSED")
                # Broker order must NOT have been called
                mock_exec.assert_not_called()
                # Internal position must still be cleanly cleared
                self.assertNotIn(symbol, engine.active_positions)
                # Cooldown must be armed
                self.assertTrue(engine.is_symbol_in_cooldown(symbol))
            finally:
                loop.close()

    # --------------------------------------------------------------------------
    # TEST 13: Timezone Robustness in Shield Graceful Square-Off
    # --------------------------------------------------------------------------
    def test_13_timezone_robustness_in_shield_square_off(self):
        """Tests that NineMentorsLiveShield.execute_310_pm_graceful_square_off strictly follows IST."""
        shield = NineMentorsLiveShield(initial_capital=918.43)

        # 14:00 IST -> Should return NOT_YET_310_PM
        dt_1400 = datetime.datetime(2026, 9, 18, 14, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
        res_early = shield.execute_310_pm_graceful_square_off(now_ist=dt_1400)
        self.assertEqual(res_early.get("status"), "NOT_YET_310_PM")

        # 15:10 IST -> Should proceed to square off
        dt_1510 = datetime.datetime(2026, 9, 18, 15, 10, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
        with patch.object(shield, "audit_broker_reality", return_value={"active_positions": []}):
            res_cutoff = shield.execute_310_pm_graceful_square_off(now_ist=dt_1510)
            self.assertEqual(res_cutoff.get("status"), "SQUARE_OFF_DISPATCHED")

    # --------------------------------------------------------------------------
    # TEST 14: Dynamic Mandatory Square-Off Time Binding
    # --------------------------------------------------------------------------
    def test_14_dynamic_mandatory_square_off_time(self):
        """Tests that mandatory_graceful_square_off parameter is bound and dynamically evaluated."""
        engine = DhanSniperMomentumEngine(initial_capital=918.43, dry_run=True)
        self.assertEqual(engine.mandatory_graceful_square_off, "15:10:00")

        # Dynamically adjust square-off to 15:05:00
        engine.mandatory_graceful_square_off = "15:05:00"
        dt_1504 = datetime.datetime(2026, 9, 18, 15, 4, 59, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
        dt_1505 = datetime.datetime(2026, 9, 18, 15, 5, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

        self.assertFalse(engine.is_square_off_time(dt_1504))
        self.assertTrue(engine.is_square_off_time(dt_1505))


if __name__ == "__main__":
    unittest.main(verbosity=2)
