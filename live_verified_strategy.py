# Auto-Generated Live Strategy: STRAT_20260917_103216
# Promoted at: 2026-09-17T10:32:17.200447
# Backtest Sharpe: 3.0 | Win Rate: 1.0 | Latency: 5353.48 us

import numpy as np
import pandas as pd

class SovereignAdaptiveAlpha:
    """
    Sovereign Adaptive Alpha Strategy synthesized from:
    - QUANT_REPO_001 (NautilusTrader HFT Engine)
    - QUANT_REPO_023 (Order Flow Imbalance Microstructure)
    - QUANT_REPO_047 (DhanHQ F&O Execution Engine)
    """
    def __init__(self, ofi_threshold: float = 1.25, iv_skew_cap: float = 0.18):
        self.ofi_threshold = ofi_threshold
        self.iv_skew_cap = iv_skew_cap
        self.position = 0
        self.entry_price = 0.0

    def compute_ofi(self, bid_px, bid_sz, ask_px, ask_sz, prev_bid_px, prev_bid_sz, prev_ask_px, prev_ask_sz):
        # Multi-level Order Flow Imbalance calculation
        delta_bid = bid_sz if bid_px > prev_bid_px else (bid_sz - prev_bid_sz if bid_px == prev_bid_px else 0)
        delta_ask = 0 if ask_px > prev_ask_px else (ask_sz - prev_ask_sz if ask_px == prev_ask_px else ask_sz)
        return float(delta_bid - delta_ask)

    def evaluate_tick(self, tick: dict) -> dict:
        ltp = tick.get("ltp", 0.0)
        ofi = tick.get("ofi", 0.0)
        iv_skew = tick.get("iv_skew", 0.0)
        
        signal = "HOLD"
        confidence = 0.0
        
        # Microstructure trigger
        if ofi > self.ofi_threshold and iv_skew < self.iv_skew_cap:
            signal = "BUY"
            confidence = min(0.99, 0.65 + (ofi * 0.1))
        elif ofi < -self.ofi_threshold:
            signal = "SELL"
            confidence = min(0.99, 0.65 + (abs(ofi) * 0.1))
            
        return {
            "signal": signal,
            "confidence": confidence,
            "ltp": ltp,
            "target": round(ltp * 1.006, 2) if signal == "BUY" else round(ltp * 0.994, 2),
            "stop_loss": round(ltp * 0.997, 2) if signal == "BUY" else round(ltp * 1.003, 2),
            "engine": "QUANT_290_GROUNDED_SYNTHESIS"
        }
