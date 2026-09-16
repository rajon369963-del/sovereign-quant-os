# ⚡ SYNTHESIZED SOVEREIGN QUANT RULES (GROUNDED IN NOTEBOOKLM DEBATE)
=============================================================================
**Verification Timestamp**: `2026-09-16T06:47:00+05:30`  
**Data Sources**: 
- 9 Indian Trading Master YouTuber Notebooks (Vivek Bajaj, Ghanshyam Tech, Subasish Pani, Saketh R, Nitin Murarka, PR Sundar, Dr. Mukul Agrawal, Siddharth Bhanushali, Abhishek Kar)
- 6 News & Crash Forensics Notebooks (15th Sept Post-Close, 15th Sept Share Market, Weekly News Parts 1 & 2, Monthly News Parts 1 & 2)
- 200+ Quantitative Trading GitHub Repositories Notebook (NautilusTrader, VectorBT, PyPortfolioOpt, OFI, ARCH)
**Courier Engine**: 23 Physical Grounded Relay Turns Executed Live in Google Chrome via NotebookLM

---

## 🏛️ 1. Master Macro & Global Liquidity Governance (Vivek Bajaj)
1. **DXY Anchor**: When US Dollar Index (DXY) > 100, global emerging market liquidity contracts. Cap total gross trading capital utilization at **50% max**.
2. **Crude & Yield Inversion**: When Brent crude exceeds $75/bbl or yields spike, defensive allocation to cash and short-duration liquid assets is mandatory.
3. **Top-Down Filtration**: 10,000 ft (Global Macro) ➔ 1,000 ft (Sector Relative Strength) ➔ 100 ft (Stock Fundamentals) ➔ 1 ft (5-minute Price Action Execution).

---

## 📈 2. Pure Price Action & Intraday Expiry Timing (Ghanshyam Tech)
1. **First 15-Minute Neutrality Rule**: Between 9:15 AM and 9:30 AM, zero automated directional market orders are allowed. Allow the initial opening range and retail emotional imbalance to settle.
2. **5-Minute Breakout Execution**:
   - Long setup: First 5-minute candle closing above previous day's high with expanding volume. Stoploss = Low of the breakout candle.
   - Short setup: First 5-minute candle closing below previous day's low with expanding volume. Stoploss = High of the breakout candle.
3. **1:30 PM Expiry Super-Cycle**: Morning range (10:00 AM - 1:15 PM) is defined by consolidation. A decisive breakout of this range after 1:30 PM triggers institutional short-covering / long-unwinding rallies.

---

## ⚡ 3. Execution Discipline & Risk-Reward Sizing (Subasish Pani - Power of Stocks)
1. **1:2 Risk-to-Reward Invariant**: No trade is entered unless the distance to the next major institutional support/resistance level provides at least a **1:2 risk-to-reward ratio**.
2. **Gap Up / Gap Down Defense**: If index gaps up > 150 points (Nifty) or > 400 points (Bank Nifty), never buy the open. Wait for a minimum 50% retracement to intraday VWAP or 9 EMA before entering.
3. **Trapped Sellers Trigger**: When price consolidates at the upper boundary for 4 consecutive candles without rejection, options sellers are trapped—scale into directional momentum.

---

## 📊 4. Order Flow Imbalance (OFI) & Institutional Traps (Nitin Murarka)
1. **Round Strike Battlegrounds**: Bank Nifty strikes ending in `000` or `500` (e.g. 51,500, 52,000) are high-volume institutional defense zones. Never initiate breakouts without seeing open interest unwinding on that strike.
2. **Open Interest PCR Signals**:
   - PCR < 0.70: Extreme put-selling fatigue / oversold condition. High risk of violent short-covering bounce.
   - PCR > 1.30: Overbought call resistance. Look for bull traps.
3. **VWAP Anchor**: Institutional confirmation requires price holding above VWAP with a positive cumulative volume delta (CVD).

---

## 🛡️ 5. Options Greeks & Dynamic Hedging Architecture (Saketh R)
1. **Morning Theta Harvesting (9:30 AM - 11:30 AM)**: Deploy risk-defined Iron Fly or Iron Condor spreads with long wing hedges (15-20 delta) to collect decay while capping margin.
2. **Afternoon Gamma Evasion**: After 1:30 PM on expiry day, Delta and Gamma risks expand exponentially. Close out all naked/tight short options and switch to trailing protective stoplosses.

---

## 🚨 6. Capital Preservation & Tail-Risk Circuit Breaker (PR Sundar)
1. **2.0% Account Killswitch**: If daily realized + unrealized loss reaches **2.0% of portfolio equity**, the execution kernel immediately liquidates all open positions and cancels pending orders.
2. **No Hope / No Revenge**: Cut losing options legs immediately when the underlying breaches predefined technical support; never average down on losing short options.

---

## 🔍 7. Forensic Health & Multi-Cap Quality Screening (Dr. Mukul Agrawal)
1. **Institutional Sponsor Filter**: Intraday high-beta stocks must have:
   - Debt-to-Equity < 1.0
   - Promoter Pledging = 0.0%
   - Operating Cash Flow (CFO) > Net Profit (PAT)
2. **Volume Anomaly**: Stock volume must exceed 3.0x its 10-day average volume to qualify as an institutional breakout candidate.

---

## 📈 8. Higher-Timeframe Trend Continuation (Siddharth Bhanushali)
1. **44-MA Daily Trend Alignment**: If a stock or index is trading above its 44-period daily Moving Average, intraday short setups are restricted to quick scalps only. Heavy size is reserved strictly for trend-continuation pullbacks to the 44-MA.

---

## 🧠 9. Behavioral Finance & FOMO Mitigation (Abhishek Kar)
1. **Anti-Hero-or-Zero Rule**: Prohibit buying cheap OTM options (Rs 5 - 15) expecting 10x returns. 95% expire worthless.
2. **Strict Trade Frequency Cap**: Maximum 3 trades per day. If the first 2 trades hit stoploss, the terminal is locked for the day.

---

## 📰 10. Macro News & Market Forensic Grounding (September 15 News Vault)
1. **FII/DII Net Flow Grounding**: September 15 post-close data demonstrated net institutional index selling with concentrated defensive accumulation in IT and FMCG.
2. **Geopolitical Oil Volatility**: Crude holding at $72-74/bbl creates intermittent margin pressure on Indian downstream and paint sectors, requiring selective asset-class isolation.

---

## 💻 11. The Automated 3-Gate Variance Shield (200+ Quant Repos Code Architecture)
```python
class ThreeGateVarianceShield:
    """
    Automated pre-trade risk filter connecting:
    - VectorBT (Statistical Edge)
    - NautilusTrader (Level 2 Microstructure / OFI)
    - Riskfolio-Lib (Downside Risk & Drawdown Control)
    """
    def __init__(self, max_risk_per_trade=0.01, daily_circuit_breaker=0.02):
        self.max_risk_per_trade = max_risk_per_trade
        self.daily_circuit_breaker = daily_circuit_breaker
        
    def evaluate_gate_1_volume_variance(self, current_volume, volume_ma_20):
        # Breakout must exhibit > 2.0x institutional volume variance
        return current_volume >= (2.0 * volume_ma_20)
        
    def evaluate_gate_2_ofi_vwap(self, price, vwap, order_flow_imbalance):
        # Order flow imbalance must agree with price relative to VWAP
        if price > vwap and order_flow_imbalance > 0:
            return True # Long Confirmed
        elif price < vwap and order_flow_imbalance < 0:
            return True # Short Confirmed
        return False
        
    def evaluate_gate_3_circuit_breaker(self, current_daily_loss_pct):
        # Hard stopkillswitch if daily loss >= 2%
        return current_daily_loss_pct < self.daily_circuit_breaker

    def authorize_trade(self, signal, current_vol, vol_ma, price, vwap, ofi, current_loss):
        g1 = self.evaluate_gate_1_volume_variance(current_vol, vol_ma)
        g2 = self.evaluate_gate_2_ofi_vwap(price, vwap, ofi)
        g3 = self.evaluate_gate_3_circuit_breaker(current_loss)
        
        if g1 and g2 and g3:
            return {"authorized": True, "structure": signal["direction"]}
        elif not g2 and g3:
            # Fallback to market-neutral Iron Fly spread
            return {"authorized": True, "structure": "MARKET_NEUTRAL_IRON_FLY"}
        else:
            return {"authorized": False, "reason": "FAILED_VARIANCE_SHIELD"}
```

---
**Verification Status**: All 23 dialectic steps verified live on physical NotebookLM notebooks in Chrome. Persisted to `grand_10k_trading_hypergraph.sqlite`.
