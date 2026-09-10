# 🔒 SECRET_SAUCE.md — CANONICAL PROPRIETARY TRADING INVARIANTS
> **STATUS: READ-ONLY PROTECTED (chmod 444)**  
> **SYSTEM: GEMINI ANTIGRAVITY FULL YOLO 2 — INDIAN AGENTIC ALPHA (NSE/BSE/NFO)**  
> **Axiom: "In non-ergodic systems, survival precedes optimization. The math trades, the gate protects."**

---

## 1. Mathematical Alpha Invariants

### 1.1 Pre-Market Auction Gap Fading (09:15 - 09:30 AM IST)
$$\text{Gap}_{\%} = \frac{\text{Open}_{09:15} - \text{VWAP}_{prev}}{\text{VWAP}_{prev}} \times 100$$
- **Condition**: If $|\text{Gap}_{\%}| \ge 0.60\%$:
  - **Long Fade (Gap Down)**: Trigger Buy when 5-min candle shows absorption wick. Target: $70\%$ gap fill. Stop Loss: $35\%$ of gap below low.
  - **Short Fade (Gap Up)**: Trigger Sell when 5-min candle shows rejection wick. Target: $70\%$ gap fill. Stop Loss: $35\%$ of gap above high.

### 1.2 NSE Option Chain Shadow & Max Pain Mechanics
- **Put-Call Ratio (PCR)**:
  $$\text{PCR} = \frac{\sum_{i \in \text{ATM}\pm 10} \text{OI}_{put, i}}{\sum_{i \in \text{ATM}\pm 10} \text{OI}_{call, i}}$$
  - $\text{PCR} < 0.65$: Severe oversold exhaustion $\rightarrow$ High-probability contrarian bounce gate.
  - $\text{PCR} > 1.40$: Severe overbought call euphoria $\rightarrow$ High-probability contrarian short gate.
- **Max Pain Formulation**:
  $$\text{Strike}_{\text{MaxPain}} = \arg\min_{K} \sum_{i} \left[ \text{OI}_{call, i} \times \max(0, S_K - K_i) + \text{OI}_{put, i} \times \max(0, K_i - S_K) \right]$$

### 1.3 BankNifty Friday Weekend Drift
- On Fridays between 14:00 and 15:15 IST, non-directional premium writers aggressively adjust gamma and retail traders square off intraday MIS orders:
  $$\vec{v}_{\text{drift}} = 0.60 \times (\text{Strike}_{\text{MaxPain}} - \text{Spot}_{\text{BankNifty}})$$

### 1.4 HDFC Bank vs ICICI Bank Statistical Arbitrage (Pairs)
- Cointegration Spread Ratio:
  $$R_t = \frac{\text{Price}_{\text{HDFCBANK}}}{\text{Price}_{\text{ICICIBANK}}}$$
  $$Z_t = \frac{R_t - \mu_{R, 30}}{\sigma_{R, 30}}$$
  - Entry Trigger: $|Z_t| \ge 2.00$
    - If $Z_t \ge +2.00$: Short HDFC Bank / Long ICICI Bank
    - If $Z_t \le -2.00$: Long HDFC Bank / Short ICICI Bank
  - Exit Trigger: $|Z_t| \le 0.50$ (Mean reversion achieved)
  - Hard Stop Trigger: $|Z_t| \ge 3.20$ (Cointegration breakdown)

---

## 2. Risk & Volatility Invariants

### 2.1 3*ATR Dynamic Chandelier Trailing Stop
- Trailing Stop Ratchet:
  - **Long Trades**: $\text{Stop}_t = \max(\text{Stop}_{t-1}, \text{Price}_t - 3.0 \times \text{ATR}_{14})$
  - **Short Trades**: $\text{Stop}_t = \min(\text{Stop}_{t-1}, \text{Price}_t + 3.0 \times \text{ATR}_{14})$
  - *Invariant: Ratchet only — stop levels NEVER widen or retreat against open positions.*

### 2.2 The 3-5-7 Structural Risk Rule
1. **Max Concurrent Positions**: $\le 3$ active positions across all instruments.
2. **Max Aggregate Portfolio Risk**: $\le 5.0\%$ cumulative capital at risk.
3. **Loss Lockout Barrier**: $7$ consecutive losses triggers an automated 24-hour execution lockout.

---

## 3. Multi-Agent Debate & High-Conviction Gate (>85%)

### 3.1 Debate Structure
- **Bull Agent**: Evaluates price momentum, CVD buying volume, VWAP pullbacks, and Put OI floor build-up. Emits Bull Conviction $C_{bull} \in [0.0, 1.0]$.
- **Bear Agent**: Evaluates overhead Call OI walls, bearish divergence, macro negative sentiment, and liquidity sweeps. Emits Bear Conviction $C_{bear} \in [0.0, 1.0]$.
- **Judge Agent**: Weighs arguments, adjusts for market regime (EGARCH) and FinBERT macro score. Emits Judge Confidence $C_{judge} \in [0.0, 1.0]$.

### 3.2 High-Conviction Threshold
$$\text{Trade Status} = \begin{cases} \text{APPROVED} & \text{if } C_{judge} > 0.85 \\ \text{VETOED} & \text{if } C_{judge} \le 0.85 \end{cases}$$
*Trade is strictly VETOED if confidence is $\le 85\%$. No exceptions.*

---

## 4. Full YOLO 2 Darwinian Mechanics

### 4.1 Delete-Until-Profit Loop
- Tracks rolling 30-trade Sharpe Ratio for each active strategy.
- If $\text{Sharpe}_{30} < 1.50$ or $\text{MaxDrawdown} > 8.0\%$:
  $$\text{Action} = \text{QUARANTINE\_AND\_DELETE}$$

### 4.2 2% Liquidator Daily Circuit Breaker
- Peak Equity Tracking:
  $$\text{Drawdown}_{\text{daily}} = \frac{\text{PeakEquity} - \text{CurrentEquity}}{\text{PeakEquity}}$$
- If $\text{Drawdown}_{\text{daily}} \ge 0.02$ ($2.0\%$):
  - **ACTION**: Cancel ALL pending orders.
  - **ACTION**: Flatten ALL open positions at market.
  - **ACTION**: Trip circuit breaker flag `is_circuit_broken = True`.
  - **ACTION**: Log event to SQLite and freeze engine for the remainder of the trading day.

### 4.3 Pre-Flight Wallet Unit Testing
Before any order payload touches the broker socket, it must satisfy all 4 asserts:
1. $\text{RequiredMargin} \le \text{AvailableMargin} \times 0.90$ (10% safety buffer)
2. $\text{Quantity} \pmod{\text{LotSize}} == 0$ (Nifty: 25, BankNifty: 15)
3. $\text{Quantity} \le \text{ExchangeFreezeLimit}$ (Nifty: 1800, BankNifty: 900)
4. $\text{OrderPrice} \pmod{0.05} == 0$ (Tick size quantization)
