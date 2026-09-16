"""
CORTEX COMPOUND ORCHESTRATOR: THE INTERCONNECTION OF INTERCONNECTIONS
Connects all 6 core quant engines into a seamless institutional trading workflow:
1. Historical Lakehouse (DuckDB + Parquet) ->
2. Technical Screener & Signal Generator ->
3. Options & Greeks Volatility Engine ->
4. Vectorized Strategy Backtester with Indian Friction ->
5. SEBI 2026 OTR Compliance Shield & Iceberg Slicer ->
6. Unified Multi-Broker Order Routing Bridge.
"""

import time
import json
from cortex_historical_lakehouse import HistoricalLakehouse
from cortex_options_greeks import OptionsGreeksEngine
from cortex_screener_engine import ScreenerEngine
from cortex_sebi_compliance_shield import SEBIComplianceShield
from cortex_backtesting_engine import BacktestingEngine, IndianFrictionModel
from cortex_unified_broker_bridge import UnifiedBrokerBridge

class CompoundQuantPipeline:
    def __init__(self):
        print("⚡ Initializing Cortex Compound Quant Pipeline...")
        self.lakehouse = HistoricalLakehouse()
        self.greeks_engine = OptionsGreeksEngine()
        self.screener = ScreenerEngine(self.lakehouse)
        self.sebi_shield = SEBIComplianceShield()
        self.backtester = BacktestingEngine(initial_capital=1000000.0)
        self.broker = UnifiedBrokerBridge("SOVEREIGN_OPENALGO_FENIX")
        print("✅ All 6 Subsystems Integrated & Operational.")

    def execute_e2e_trading_cycle(self, symbol="NIFTY 50"):
        cycle_start = time.time()
        print("\n[STEP 1/6] Querying Point-in-Time Lakehouse for " + symbol + "...")
        df = self.lakehouse.query_history(symbol)
        if df is None or len(df) == 0:
            self.lakehouse.generate_synthetic_history(180)
            df = self.lakehouse.query_history(symbol)
        step1_ms = (time.time() - cycle_start) * 1000.0
        n_bars = len(df)
        print(f"  Retrieved {n_bars} historical bars in {step1_ms:.2f}ms.")

        t2 = time.time()
        print("[STEP 2/6] Running Multi-Factor Technical Screener...")
        scan_result = self.screener.scan_symbol(df)
        step2_ms = (time.time() - t2) * 1000.0
        action = scan_result["action"]
        score = scan_result["composite_score"]
        signals_str = str(scan_result["signals"])
        print(f"  Screening verdict: {action} (Score: {score}, Signals: {signals_str}) in {step2_ms:.2f}ms.")

        t3 = time.time()
        print("[STEP 3/6] Computing Options Volatility & Dynamic Wing Sizing...")
        spot = scan_result["close"]
        wings = self.greeks_engine.calculate_dynamic_iron_condor_wings(spot, india_vix=14.2)
        atm_call_greeks = self.greeks_engine.calculate_greeks(spot, spot, 5/365.0, 0.142, "CE")
        step3_ms = (time.time() - t3) * 1000.0
        d_val = atm_call_greeks["delta"]
        g_val = atm_call_greeks["gamma"]
        th_val = atm_call_greeks["theta"]
        print(f"  ATM Call Delta: {d_val}, Gamma: {g_val}, Theta: {th_val}/day in {step3_ms:.2f}ms.")
        sc = wings["short_call"]
        sp = wings["short_put"]
        ww = wings["wing_width"]
        print(f"  Dynamic Wings: Short CE {sc} / Short PE {sp} (Wing Width: {ww} pts).")

        t4 = time.time()
        print("[STEP 4/6] Vectorized Backtest with Indian Statutory Friction...")
        df_bt = df.copy()
        df_bt["sma_fast"] = df_bt["close"].rolling(10).mean()
        df_bt["sma_slow"] = df_bt["close"].rolling(30).mean()
        signals = [1 if df_bt["sma_fast"].iloc[i] > df_bt["sma_slow"].iloc[i] else -1 for i in range(len(df_bt))]
        bt_results = self.backtester.backtest_strategy(df_bt, signals, instrument="OPTIONS")
        step4_ms = (time.time() - t4) * 1000.0
        sh_val = bt_results["sharpe_ratio"]
        wr_val = bt_results["win_rate_pct"]
        pnl_val = bt_results["total_net_pnl"]
        print(f"  Backtest Sharpe: {sh_val}, Win Rate: {wr_val}%, Net PnL: INR {pnl_val} in {step4_ms:.2f}ms.")

        t5 = time.time()
        print("[STEP 5/6] Routing through SEBI 2026 Compliance Shield & Dynamic Iceberg Slicer...")
        target_qty = 2500
        limit_px = round(atm_call_greeks["price"] * 1.02, 2)
        iceberg = self.sebi_shield.slice_iceberg_order(symbol, target_qty, "BUY", limit_px, atm_call_greeks["price"], lot_size=25)
        sc_cnt = iceberg["slice_count"]
        is_exempt = iceberg["otr_band_status"]["is_otr_exempt"]
        print(f"  Iceberg Slicer created {sc_cnt} child orders. Safe OTR Exempt: {is_exempt}.")

        t6 = time.time()
        print("[STEP 6/6] Executing Child Orders via Unified Multi-Broker Bridge...")
        executed_orders = []
        for child in iceberg["child_orders"]:
            if self.sebi_shield.acquire_order_slot():
                self.sebi_shield.record_order_event("PLACE")
                strike_formatted = round(spot / 50.0) * 50
                res = self.broker.place_order(
                    symbol=f"{symbol}26SEP{strike_formatted}CE",
                    exchange="NFO",
                    transaction_type=child["side"],
                    quantity=child["qty"],
                    order_type="LIMIT",
                    price=child["price"],
                    tag="CORTEX_COMPOUND"
                )
                self.sebi_shield.record_order_event("TRADE")
                executed_orders.append(res["data"])
            else:
                print("  Throttled by Token Bucket rate limiter!")

        live_otr = self.sebi_shield.calculate_live_otr()
        otr_val = live_otr["current_otr"]
        tier_val = live_otr["regulatory_tier"]
        print(f"  Placed {len(executed_orders)} child orders. Live Session OTR: {otr_val} ({tier_val}).")

        total_latency_ms = (time.time() - cycle_start) * 1000.0
        print(f"\n🏁 Full Compound Trading Cycle Completed in {total_latency_ms:.2f} ms!")

        return {
            "symbol": symbol,
            "spot": spot,
            "screener": scan_result,
            "greeks": atm_call_greeks,
            "dynamic_wings": wings,
            "backtest_summary": {
                "sharpe": bt_results["sharpe_ratio"],
                "net_pnl": bt_results["total_net_pnl"],
                "win_rate": bt_results["win_rate_pct"]
            },
            "sebi_compliance": live_otr,
            "executed_orders_count": len(executed_orders),
            "total_latency_ms": round(total_latency_ms, 2)
        }

if __name__ == "__main__":
    pipeline = CompoundQuantPipeline()
    summary = pipeline.execute_e2e_trading_cycle("NIFTY 50")
    print("\nSummary Receipt:")
    print(json.dumps(summary, indent=2))
