#!/usr/bin/env python3
"""
qullamaggie_breakout_scanner.py
Scans Indian equities for Kristjan Qullamaggie setups (EP Episodic Pivot & High Tight Flag / VCP)
combined with the Antigravity Relative Strength Divergence against NIFTY 50.
"""

import pandas as pd
import yfinance as yf

TICKERS = [
    "HCLTECH.NS", "ZENSARTECH.NS", "TCS.NS", "INFY.NS", "TECHM.NS",
    "WIPRO.NS", "SUNTV.NS", "HDFCBANK.NS", "TATASTEEL.NS", "SAIL.NS",
    "PNB.NS", "ASHOKLEY.NS", "BEL.NS"
]

def scan_antigravity_qullamaggie():
    print("=" * 65)
    print("⚡ QULLAMAGGIE + ANTIGRAVITY RELATIVE STRENGTH SCANNER (NSE)")
    print("=" * 65)
    
    nifty = yf.download("^NSEI", period="1mo", interval="1d", progress=False)
    if nifty.empty:
        print("Failed to download Nifty benchmark.")
        return
    
    close_s = nifty['Close'].squeeze()
    nifty_close = float(close_s.dropna().iloc[-1])
    nifty_prev = float(close_s.dropna().iloc[-5])
    nifty_5d_ret = ((nifty_close - nifty_prev) / nifty_prev) * 100
    print(f"NIFTY 50: {nifty_close:.2f} | 5-Day Return: {nifty_5d_ret:+.2f}%\n")
    
    results = []
    
    for sym in TICKERS:
        try:
            df = yf.download(sym, period="3mo", interval="1d", progress=False)
            if df.empty or len(df) < 50:
                continue
            
            c_s = df['Close'].squeeze()
            h_s = df['High'].squeeze()
            l_s = df['Low'].squeeze()
            
            close = float(c_s.dropna().iloc[-1])
            c5 = float(c_s.dropna().iloc[-5])
            ret_5d = ((close - c5) / c5) * 100
            
            # Moving averages
            ema10 = float(c_s.ewm(span=10, adjust=False).mean().dropna().iloc[-1])
            ema20 = float(c_s.ewm(span=20, adjust=False).mean().dropna().iloc[-1])
            sma50 = float(c_s.rolling(window=50).mean().dropna().iloc[-1])
            
            # Trend condition
            trend_aligned = bool(close > ema10 > ema20)
            
            # Relative Strength Divergence (Stock Green / Positive while Nifty Falling)
            rs_divergence = bool((ret_5d > 0) and (nifty_5d_ret < 0))
            
            # Consolidation (20-day high vs low range)
            h20 = float(h_s.dropna().iloc[-20:].max())
            l20 = float(l_s.dropna().iloc[-20:].min())
            consolidation_range = float(((h20 - l20) / l20) * 100)
            
            # Score
            score = 0
            if rs_divergence: score += 40
            if trend_aligned: score += 30
            if consolidation_range < 12.0: score += 30 # Tight flag
            
            status = "ANTIGRAVITY BUY" if score >= 70 else ("NEUTRAL" if score >= 40 else "GRAVITY / AVOID")
            
            results.append({
                "Symbol": sym.replace(".NS", ""),
                "Price": round(float(close), 2),
                "5D_Return_%": round(float(ret_5d), 2),
                "Trend_Aligned": trend_aligned,
                "Range_20D_%": round(float(consolidation_range), 1),
                "Score": score,
                "Status": status
            })
        except Exception:
            continue
            
    res_df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
    print(res_df.to_string(index=False))
    print("=" * 65)
    return res_df

if __name__ == "__main__":
    scan_antigravity_qullamaggie()
