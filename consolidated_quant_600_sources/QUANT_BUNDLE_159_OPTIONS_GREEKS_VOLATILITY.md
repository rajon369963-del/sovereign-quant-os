# ⚡ [QUANT-SOURCE-159] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_159_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Options-Trading-Strategies-2010-2020 (`PHASE4-QUANT-186`)
- **Full Name**: `PHASE4-QUANT-186_nirajneupane17__Options-Trading-Strategies-2010-2020`
- **Description**: European · American · Asian · Barrier · Binary options — 10 trading strategies · P&L profiles · Greeks surfaces · regime analysis · Draghi recovery to COVID crash 2010–2020. Python.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">

# Options Trading Strategies — 2010–2020

### Quant Trading Projects · Series 6 of 20

*European · American · Asian · Barrier · Binary options*  
*10 trading strategies · P&L profiles · Greeks surfaces · Regime analysis*  
*Draghi recovery → Volmageddon → COVID crash*

[![Python](https://img.shields.io/badge/Python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## Why 2010–2020?

> *"In 2017 selling volatility felt like free money — VIX averaged 9. In February 2018 it hit 50 in two days. In March 2020 it hit 85. The same strategy. Three completely different outcomes."*

The 2010–2020 decade contains every market condition options traders need to understand:

| Period | VIX | What happened | Options lesson |
|:---|:---:|:---|:---|
| **2010–2011** | 18–45 | EU sovereign debt crisis | Protection pays |
| **2012–2016** | 10–25 | Draghi bull market | Income strategies win |
| **2017** | **9–12** | Historically lowest VIX ever | Short vol = free money |
| **Feb 2018** | **9→50** | Volmageddon — 2 days | Short vol blows up |
| **2019** | 12–20 | Trade war recovery | Spreads outperform |
| **Mar 2020** | **85** | COVID crash — fastest ever | Protective puts pay off |

---

## Strategy P&L Profiles

![Strategy P&L](results/img1_strategy_pnl.png)

---

## Data

### `data/market_timeseries.csv` — 2,869 daily rows

| Column | Description |
|:---|:---|
| `date` | Trading date |
| `spot` | S&P 500 proxy price |
| `return_pct` | Daily log return (%) |
| `vix` | VIX proxy |
| `rv_21d` | 21-day realized volatility |
| `vrp` | Volatility risk premium (VIX − RV) |
| `sigma` | Regime implied volatility |
| `regime` | Market regime label |

### `data/option_prices.csv` — 378 quotes · 3 regimes · 5 option types

| Column | Description |
|:---|:---|
| `european_call` | Black-Scholes European call |
| `american_put` | CRR binomial tree American put |
| `asian_call` | Monte Carlo arithmetic average call |
| `barrier_call` | Down-and-out barrier call (H = 85% of K) |
| `binary_call` | Cash-or-nothing binary call |
| `early_ex_prem` | American − European (early exercise premium) |
| `delta` | dC/dS |
| `vega` | dC/dσ |

---

## Option Types Comparison

![Option Types](results/img2_option_types.png)

---

## Options Pricing Models

### European — Black-Scholes (1973)
```
C = S·e^(-qT)·N(d₁) − K·e^(-rT)·N(d₂)
P = K·e^(-rT)·N(-d₂) − S·e^(-qT)·N(-d₁)
```

### American — CRR Binomial Tree
Early exercise optimal for puts (high r) and calls (high q).
`Early exercise premium = American − European`

### Asian — Monte Carlo (Arithmetic Average)
Payoff based on average spot over the life of the option.
Cheaper than European — averaging reduces effective volatility by ~1/√3.

### Barrier — Down-and-Out Call
Knocked out if spot ever falls below barrier H.
Cheaper than European — knock-out risk reduces value.

### Binary/Digital
Cash-or-nothing: pays $1 if S_T > K (call) or S_T < K (put).
Used for pure directional bets with defined payout.

---

## Greeks Surfaces

![Greeks](results/img3_greeks.png)

---

## 10 Trading Strategies

| # | Strategy | Outlook | Max Profit | Max Loss | Use when |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | **Long Call** | Bullish | Unlimited | Premium | Strong directional view upward |
| 2 | **Long Put** | Bearish | K − Premium | Premium | Strong directional view downward |
| 3 | **Bull Call Spread** | Mildly bullish | Spread − Debit | Debit | Moderate upside, capped cost |
| 4 | **Bear Put Spread** | Mildly bearish | Spread − Debit | Debit | Moderate downside, capped cost |
| 5 | **Long Straddle** | Volatile | Unlimited | 2× Premium | Expect big move, unknown direction |
| 6 | **Long Strangle** | Very volatile | Unlimited | 2× Premium | Cheaper straddle, needs bigger move |
| 7 | **Iron Condor** | Range-bound | Net Credit | Width − Credit | Low VIX, market going nowhere |
| 8 | **Covered Call** | Neutral/Bullish | Credit | Unlimited | Generate income on long stock |
| 9 | **Protective Put** | Long stock hedge | Unlimited | Put Premium | Insurance on long position |
| 10 | **Butterfly Spread** | Precise target | Spread − Debit | Debit | Expect spot at exact level |

---

## Vol Regime Analysis 2010–2020

![Regime Analysis](results/img4_regime_analysis.png)

---

## 3D P&L Surface

![P&L Surface](results/img5_pnl_surface.png)

---

## Long Vol vs Short Vol — 2017 vs 2018 vs 2020

![Long Vol Short Vol](results/img6_longvol_vs_shortvol.png)

---

## Key Results

### Annual P&L Backtest

| Year | Regime | VIX avg | Straddle | Covered Call | Protective Put |
|:---|:---|:---:|:---:|:---:|:---:|
| 2017 | Historically Low VIX | 9.5 | −$340 | +$620 | −$290 |
| 2018 | Volmageddon | 20.0 | +$840 | −$480 | +$560 |
| 2020 | COVID Crash | 28.0 | +$2,100 | −$1,200 | +$1,840 |

---

## Risk Dashboard

![Risk Dashboard](results/img7_risk_dashboard.png)

---

## Key Findings

**1. Same strategy, wildly different outcomes across regimes.**
Iron Condor earned steadily in 2017 (VIX=9) and was catastrophically unprofitable in Feb 2018 (VIX=50 in 2 days). Strategy selection must be regime-aware.

**2. Volatility itself is the risk — not just direction.**
A portfolio can look delta-neutral and appear safe while carrying enormous vega exposure. When VIX moves from 12 to 50, vega risk dominates everything.

**3. American put premium spikes in high-vol regimes.**
Early exercise premium is near-zero in calm markets and meaningful in crisis — the right to exercise early has real value when rates are high or dividends are large.

**4. Asian options are natural instruments for portfolio hedging.**
Averaging reduces effective volatility, making Asian options systematically cheaper than European. For index hedges held over months, this cost reduction is significant.

**5. The 2017→2018 transition is the most important case study.**
February 5, 2018: VIX went from 17 to 37 intraday. Short-vol products (XIV, SVXY) lost 80–90% in one day. The Iron Condor positions that had been printing for 18 months were destroyed in hours.

---

## Project Structure

```
Options-Trading-Strategies-2010-2020/
│
├── data/
│   ├── market_timeseries.csv     2,869 daily rows — VIX · spot · regime
│   ├── option_prices.csv         378 quotes — 5 option types × 3 regimes
│   ├── strategy_pnl.csv          300 spot values × 10 strategies
│   ├── regime_backtest.csv       11-year annual P&L by strategy
│   └── annual_summary.csv        Year-by-year VIX and market stats
│
├── notebooks/
│   ├── 01_european_american_options.ipynb
│   ├── 02_exotic_options.ipynb
│   ├── 03_trading_strategies.ipynb
│   ├── 04_greeks_analysis.ipynb
│   └── 05_regime_backtesting.ipynb
│
├── src/
│   ├── option_pricing.py     BS · Binomial · Monte Carlo · Barrier · Binary
│   ├── strategies.py         10 strategy payoff functions
│   └── risk_analytics.py     Greeks · scenario analysis · prob of profit
│
├── results/
│   ├── img1_strategy_pnl.png         10-panel P&L profiles
│   ├── img2_option_types.png         European vs Asian vs Barrier vs Binary
│   ├── img3_greeks.png               Delta · Gamma · Vega · Theta surfaces
│   ├── img4_regime_analysis.png      VIX arc + VRP + annual P&L
│   ├── img5_pnl_surface.png          3D Plasma straddle P&L surface
│   ├── img6_longvol_vs_shortvol.png  2017 vs 2018 vs 2020 comparison
│   └── img7_risk_dashboard.png       Max profit · max loss · breakeven · PoP
│
└── README.md
```

---

## References

- Black, F. & Scholes, M. (1973). The pricing of options and corporate liabilities. *Journal of Political Economy*, 81(3), 637–654.
- Cox, J., Ross, S. & Rubinstein, M. (1979). Option pricing: A simplified approach. *Journal of Financial Economics*, 7(3), 229–263.
- Heston, S. (1993). A closed-form solution for options with stochastic volatility. *Review of Financial Studies*, 6(2), 327–343.
- Hull, J. (2022). *Options, Futures, and Other Derivatives* (11th ed.). Pearson.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.

---

<div align="center">

**Niraj Neupane**  
Quantitative Researcher, Financial Economist

[github.com/nirajneupane17](https://github.com/nirajneupane17)

*Built with Python · NumPy · Pandas · SciPy · Matplotlib*

</div>

### Core Implementation Code & Architecture
#### File: `src/risk_analytics.py`
```python
"""
risk_analytics.py — Greeks, scenario analysis, risk metrics
Author: Niraj Neupane | github.com/nirajneupane17
"""
import numpy as np, pandas as pd
from scipy.stats import norm
from option_pricing import bs_call, bs_put, bs_greeks

def portfolio_greeks(positions, S, T, r=0.02, sigma=0.20, q=0.015):
    """
    Aggregate Greeks for a multi-leg options position.
    positions: list of (type, K, qty) e.g. [('call',2000,1),('put',1900,-1)]
    """
    totals = dict(delta=0, gamma=0, vega=0, theta=0, value=0)
    for opt_type, K, qty in positions:
        gk = bs_greeks(S, K, T, r, sigma, q, opt=opt_type)
        pv = (bs_call(S,K,T,r,sigma,q) if opt_type=='call'
              else bs_put(S,K,T,r,sigma,q))
        for k in ['delta','gamma','vega','theta']:
            totals[k] += qty * gk[k]
        totals['value'] += qty * pv
    return {k: round(v, 6) for k, v in totals.items()}

def breakeven_points(strategy, K, premiums, K2=None):
    """Return upper and lower breakeven spot prices."""
    if strategy == 'long_call':   return [K + sum(premiums)]
    if strategy == 'long_put':    return [K - sum(premiums)]
    if strategy == 'straddle':    return [K - sum(premiums), K + sum(premiums)]
    if strategy == 'strangle':    return [K - sum(premiums), K2 + sum(premiums)]
    if strategy == 'covered_call':return [K - sum(premiums)]
    return []

def scenario_pnl(strategy_func, S_range, S_shocks=None):
    """
    Compute P&L under spot shocks.
    S_shocks: list of pct moves e.g. [-0.20, -0.10, 0, 0.10, 0.20]
    """
    if S_shocks is None:
        S_shocks = [-0.30, -0.20, -0.10, -0.05, 0, 0.05, 0.10, 0.20, 0.30]
    S_mid = S_range[len(S_range)//2]
    results = []
    for shock in S_shocks:
        S_shocked = S_mid * (1 + shock)
        idx = np.argmin(np.abs(S_range - S_shocked))
        pnl = strategy_func[idx] if idx < len(strategy_func) else 0
        results.append({'shock_pct': round(shock*100, 1),
                         'spot': round(S_shocked, 2),
                         'pnl': round(float(pnl), 2)})
    return pd.DataFrame(results)

def prob_profit(pnl_array, S_range, S_current, sigma, T, r=0.02, q=0.015):
    """
    Risk-neutral probability of profit at expiry.
    Uses log-normal distribution of terminal spot price.
    """
    probs = []
    for s, p in zip(S_range, pnl_array):
        lognorm_prob = norm.cdf(
            (np.log(s/S_current) - (r-q-0.5*sigma**2)*T) / (sigma*np.sqrt(T)))
        probs.append(lognorm_prob if p > 0 else 0)
    return round(sum(np.diff(probs[:-1])) * 100, 2)

if __name__ == '__main__':
    pos = [('call', 2000, 1), ('put', 2000, 1)]
    print("Straddle Greeks:", portfolio_greeks(pos, S=2000, T=0.25, sigma=0.20))
    print("Breakeven:",       breakeven_points('straddle', 2000, [80, 75]))
```

#### File: `src/strategies.py`
```python
"""
strategies.py — 10 options trading strategy payoff functions
Author: Niraj Neupane | github.com/nirajneupane17
"""
import numpy as np
from option_pricing import bs_call, bs_put

def long_call(S_range, K, premium):
    """Bullish. Unlimited upside, max loss = premium paid."""
    return np.maximum(S_range - K, 0) - premium

def long_put(S_range, K, premium):
    """Bearish. Max profit = K - premium. Max loss = premium."""
    return np.maximum(K - S_range, 0) - premium

def bull_call_spread(S_range, K_low, K_high, net_debit):
    """Mildly bullish. Capped profit and loss."""
    return (np.maximum(S_range-K_low, 0)
            - np.maximum(S_range-K_high, 0) - net_debit)

def bear_put_spread(S_range, K_high, K_low, net_debit):
    """Mildly bearish. Capped profit and loss."""
    return (np.maximum(K_high-S_range, 0)
            - np.maximum(K_low-S_range, 0) - net_debit)

def long_straddle(S_range, K, call_prem, put_prem):
    """Volatility play. Profit if large move either direction."""
    return (np.maximum(S_range-K, 0)
            + np.maximum(K-S_range, 0) - call_prem - put_prem)

def long_strangle(S_range, K_call, K_put, call_prem, put_prem):
    """Cheaper straddle. Wider breakeven, needs bigger move."""
    return (np.maximum(S_range-K_call, 0)
            + np.maximum(K_put-S_range, 0) - call_prem - put_prem)

def iron_condor(S_range, K1, K2, K3, K4, net_credit):
    """
    Short strangle + wings. Income strategy.
    Profit when spot stays between K2 and K3.
    K1 < K2 < K3 < K4
    """
    short_call_spread = (np.maximum(S_range-K3,0) - np.maximum(S_range-K4,0))
    short_put_spread  = (np.maximum(K2-S_range,0) - np.maximum(K1-S_range,0))
    return net_credit - short_call_spread - short_put_spread

def covered_call(S_range, S_entry, K, premium):
    """Hold stock, sell call. Income generation. Caps upside."""
    return (S_range - S_entry) - np.maximum(S_range-K, 0) + premium

def protective_put(S_range, S_entry, K, premium):
    """Hold stock, buy put. Insurance. Floors downside."""
    return (S_range - S_entry) + np.maximum(K-S_range, 0) - premium

def butterfly_spread(S_range, K_low, K_mid, K_high, net_debit):
    """Profit if spot pins at K_mid at expiry. Precision play."""
    return (np.maximum(S_range-K_low,  0)
            - 2*np.maximum(S_range-K_mid,  0)
            + np.maximum(S_range-K_high, 0) - net_debit)

def strategy_summary(S, K, T, r=0.02, sigma=0.20, q=0.015):
    """Print cost, max profit, max loss for all 10 strategies."""
    Cp = bs_call(S,K,T,r,sigma,q); Pp = bs_put(S,K,T,r,sigma,q)
    print(f"{'Strategy':<22} {'Cost':>8} {'Max Profit':>12} {'Max Loss':>10}")
    print("-"*56)
    print(f"{'Long Call':<22} {'$'+str(round(Cp,2)):>8} {'Unlimited':>12} {'$'+str(round(Cp,2)):>10}")
    print(f"{'Long Put':<22} {'$'+str(round(Pp,2)):>8} {'$'+str(round(K-Pp,2)):>12} {'$'+str(round(Pp,2)):>10}")
    print(f"{'Long Straddle':<22} {'$'+str(round(Cp+Pp,2)):>8} {'Unlimited':>12} {'$'+str(round(Cp+Pp,2)):>10}")
    print(f"{'Covered Call':<22} {'0':>8} {'$'+str(round(Cp,2)):>12} {'Unlimited':>10}")
    print(f"{'Protective Put':<22} {'$'+str(round(Pp,2)):>8} {'Unlimited':>12} {'$'+str(round(Pp,2)):>10}")

if __name__ == '__main__':
    strategy_summary(S=2000, K=2000, T=0.25)
```

#### File: `src/option_pricing.py`
```python
"""
option_pricing.py — European, American, Asian, Barrier, Binary
Author: Niraj Neupane | github.com/nirajneupane17
Series: Quant Trading Projects — Options Strategies 2010-2020
"""
import numpy as np
from scipy.stats import norm

R = 0.02; Q = 0.015   # default risk-free rate and dividend yield

# ── Black-Scholes ─────────────────────────────────────────────
def bs_call(S, K, T, r=R, sigma=0.20, q=Q):
    """European call — Black-Scholes (1973)."""
    if T <= 0 or sigma <= 0: return max(0.0, S - K)
    d1 = (np.log(S/K) + (r - q + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S*np.exp(-q*T)*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

def bs_put(S, K, T, r=R, sigma=0.20, q=Q):
    """European put — Black-Scholes (1973)."""
    if T <= 0 or sigma <= 0: return max(0.0, K - S)
    d1 = (np.log(S/K) + (r - q + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return K*np.exp(-r*T)*norm.cdf(-d2) - S*np.exp(-q*T)*norm.cdf(-d1)

def bs_greeks(S, K, T, r=R, sigma=0.20, q=Q, opt='call'):
    """Delta, Gamma, Vega, Theta for European options."""
    if T <= 0: return dict(delta=0, gamma=0, vega=0, theta=0)
    d1 = (np.log(S/K) + (r - q + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    sign = 1 if opt == 'call' else -1
    delta = sign * np.exp(-q*T) * norm.cdf(sign*d1)
    gamma = np.exp(-q*T) * norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega  = S * np.exp(-q*T) * norm.pdf(d1) * np.sqrt(T) / 100
    theta = ((-S*np.exp(-q*T)*norm.pdf(d1)*sigma/(2*np.sqrt(T))
              - sign*r*K*np.exp(-r*T)*norm.cdf(sign*d2)
              + sign*q*S*np.exp(-q*T)*norm.cdf(sign*d1)) / 365)
    return dict(delta=round(delta,6), gamma=round(gamma,8),
                vega=round(vega,6), theta=round(theta,6))

# ── American — Binomial Tree ───────────────────────────────────
def american_option(S, K, T, r=R, sigma=0.20, q=Q, n=100, opt='call'):
    """
    American option via Cox-Ross-Rubinstein binomial tree.
    Early exercise premium = american_option() - bs_call/put()
    """
    dt = T/n; u = np.exp(sigma*np.sqrt(dt)); d = 1/u
    p  = (np.exp((r - q)*dt) - d) / (u - d)
    disc = np.exp(-r*dt)
    prices = S * u**np.arange(n, -1, -1) * d**np.arange(0, n+1)
    vals   = np.maximum(prices - K, 0) if opt == 'call' else np.maximum(K - prices, 0)
    for _ in range(n-1, -1, -1):
        vals   = disc * (p*vals[:-1] + (1-p)*vals[1:])
        prices = prices[:-1] / u
        intrinsic = np.maximum(prices-K,0) if opt=='call' else np.maximum(K-prices,0)
        vals = np.maximum(vals, intrinsic)
    return float(vals[0])

# ── Asian — Arithmetic Average (Monte Carlo) ───────────────────
def asian_option(S, K, T, r=R, sigma=0.20, q=Q,
                  n_paths=10000, n_steps=252, opt='call'):
    """
    Asian option on arithmetic average of spot price.
    Cheaper than European — averaging reduces effective volatility.
    """
    dt  = T / n_steps
    Z   = np.random.randn(n_paths, n_steps)
    logS = np.log(S) + np.cumsum((r-q-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z, axis=1)
    avg  = np.exp(logS).mean(axis=1)   # arithmetic average
    if opt == 'call': payoff = np.maximum(avg - K, 0)
    else:             payoff = np.maximum(K - avg, 0)
    return float(np.exp(-r*T) * payoff.mean())

# ── Barrier — Down-and-Out Call (Monte Carlo) ──────────────────
def barrier_down_out_call(S, K, T, H, r=R, sigma=0.20, q=Q,
                           n_paths=10000, n_steps=252):
    """
    Down-and-out call: knocked out if spot ever falls below barrier H.
    Cheaper than European — knock-out risk reduces value.
    Typical barrier: 10-15% below current spot.
    """
    dt   = T / n_steps
    Z    = np.random.randn(n_paths, n_steps)
    logS = np.log(S) + np.cumsum((r-q-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z, axis=1)
    paths   = np.exp(np.hstack([np.log(S)*np.ones((n_paths,1)), logS]))
    knocked = paths.min(axis=1) < H
    payoff  = np.where(knocked, 0, np.maximum(paths[:,-1] - K, 0))
    return float(np.exp(-r*T) * payoff.mean())

# ── Binary/Digital ─────────────────────────────────────────────
def binary_call(S, K, T, r=R, sigma=0.20, Q_payout=1.0, q=Q):
    """Binary cash-or-nothing call: pays Q if S_T > K, else 0."""
    if T <= 0: return Q_payout if S > K else 0.0
    d2 = (np.log(S/K) + (r-q-0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return Q_payout * np.exp(-r*T) * norm.cdf(d2)

def binary_put(S, K, T, r=R, sigma=0.20, Q_payout=1.0, q=Q):
    """Binary cash-or-nothing put: pays Q if S_T < K, else 0."""
    if T <= 0: return Q_payout if S < K else 0.0
    d2 = (np.log(S/K) + (r-q-0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return Q_payout * np.exp(-r*T) * norm.cdf(-d2)

if __name__ == '__main__':
    S, K, T, sigma = 2000, 2000, 0.25, 0.20
    print(f"European Call : ${bs_call(S,K,T):.2f}")
    print(f"European Put  : ${bs_put(S,K,T):.2f}")
    print(f"American Call : ${american_option(S,K,T):.2f}")
    print(f"Asian Call    : ${asian_option(S,K,T,n_paths=5000):.2f}")
    print(f"Barrier Call  : ${barrier_down_out_call(S,K,T,H=1800,n_paths=5000):.2f}")
    print(f"Binary Call   : ${binary_call(S,K,T):.4f}")
    print(f"Greeks        : {bs_greeks(S,K,T)}")
```


==================================================


## [2/3] Repository: ivsurf (`PHASE4-QUANT-184`)
- **Full Name**: `PHASE4-QUANT-184_thedhruvhegde__ivsurf`
- **Description**: Options volatility research terminal with 3D spatial analytics, opening scanner, and quant models. Python, Streamlit, FastAPI.
- **GitHub Stars**: 4
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# OpenPulse

**OpenPulse** is an opening-hours volatility scanner and spatial research platform — 3D math visualizations, ML graphs, knowledge maps, and optional paper trading. Built as an educational and research tool, not a live trading system.

Formerly **IVSURF** (Integrated Volatility Surface Research Facility). The GitHub repo remains `ivsurf`; environment variables keep the `IVSURF_*` prefix for compatibility.

![OpenPulse Terminal](scripts/23.png)

[![Launch Live Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ivsurf-volatility-explorer.streamlit.app)

## Live Demo

[https://ivsurf-volatility-explorer.streamlit.app](https://ivsurf-volatility-explorer.streamlit.app)

## What It Does

OpenPulse combines opening-hours scanning, 3D spatial analytics, and classical quant finance in a Streamlit terminal:

- **3D Spatial Lab** — parametric math surfaces, ML loss landscapes, PCA feature space, knowledge graphs, correlation sphere, opening score terrain
- **Opening scanner** — ranks tickers by gap, premarket volume, opening range, and regime-adjusted scores
- **Market scanner** — ranks NASDAQ tickers by rule-based swing opportunity scores
- **Volatility surfaces** — builds and visualizes IV surfaces from Yahoo Finance options chains
- **Quant models** — GARCH, regime switching, Heston MC, VaR, Monte Carlo simulation
- **ML forecasting** — sklearn ensemble + walk-forward XGBoost ranker (TensorFlow LSTM optional)
- **Risk analytics** — VaR, stress testing, regime-aware backtesting
- **REST API** — FastAPI endpoints for scan, predict, signal history, and live opening-range websocket
- **Paper trading** — Alpaca and simulated brokers with pre-trade guardrails

**Data sources:** Yahoo Finance (default). Alpaca optional for 1-min bars and paper trading.

## Quick Start

```bash
git clone https://github.com/DDVHegde100/ivsurf.git
cd ivsurf

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
streamlit run scripts/ivsurf_retro_terminal.py --server.port 8503

# Optional: REST API
pip install -e ".[api]"
uvicorn api.main:app --reload --port 8000

# Docker (UI + API)
./scripts/compose-up.sh
```

### Optional Dependencies

Install extras via `pyproject.toml`:

```bash
pip install -e ".[dev]"        # pytest, ruff
pip install -e ".[ml]"           # TensorFlow for LSTM models
pip install -e ".[quant]"        # arch, statsmodels for clustering diagnostics
pip install -e ".[perf]"         # numba for Monte Carlo acceleration
pip install -e ".[all]"          # everything
```

## Project Structure

```
ivsurf/
├── engine/                  # Business logic (data, features, signals, backtest, execution)
├── api/                     # FastAPI routes (OpenPulse API)
├── app/                     # Streamlit UI components and themes
├── core/                    # Black-Scholes, Greeks, spatial geometry
├── visuals/plot_3d/         # 3D Plotly visualizations
├── models/                  # GARCH, regime switching, Heston, jump diffusion
├── ml/                      # Volatility forecasting, neural networks
├── scripts/
│   └── ivsurf_retro_terminal.py   # Main Streamlit app
└── tests/                   # pytest suite
```

## Testing

```bash
pip install -r requirements-dev.txt
pytest                          # unit tests (excludes integration by default)
pytest -m integration           # live market data tests (requires network)
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for Streamlit Cloud, Docker Compose, FastAPI, and Alpaca setup.

## Known Limitations

- Opening scanner uses **heuristic scoring** with optional ML re-ranking when a trained model is present
- Yahoo Finance data is delayed and may break without notice; Alpaca recommended for intraday bars
- Live order submission requires explicit user confirmation; guardrails are enabled by default
- Not investment advice — research and educational use only

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

MIT License — see [LICENSE](LICENSE).

## Disclaimer

This software is for **educational and research purposes only**. Not investment advice. All trading involves substantial risk of loss.

---

**Dhruv Hegde** — Quantitative Developer & Trading Systems Engineer

### Core Implementation Code & Architecture
#### File: `api/routes/__init__.py`
```python
"""API route modules."""
```

#### File: `tests/test_smoke.py`
```python
def test_smoke():
    assert True
```

#### File: `app/__init__.py`
```python
"""IVSURF Streamlit UI components."""
```

#### File: `app/components/__init__.py`
```python
"""Reusable Streamlit UI components."""
```

#### File: `api/__init__.py`
```python
"""FastAPI backend for IVSURF engine."""
```

#### File: `dashboard/__init__.py`
```python
"""Streamlit dashboard and components."""
```


==================================================


## [3/3] Repository: Trivya-portfolio-tracker (`PHASE4-QUANT-189`)
- **Full Name**: `PHASE4-QUANT-189_GoDkILLeR-04__Trivya-portfolio-tracker`
- **Description**: Real-time equity & options portfolio tracker with Greeks calculation, P&L analytics, and Streamlit dashboard for Indian markets (NSE/BSE)
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# 📊 Trivya Portfolio Tracker

<div align="center">

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/status-unactive-success.svg)

**Real-time equity portfolio tracker with risk analytics, Monte Carlo projections, and performance visualizations for Indian markets (NSE/BSE)**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Roadmap](#-roadmap)

</div>

---

## 🎯 Overview

For Indian equity traders and investors, Trivya is a feature-rich portfolio analytics platform built on Python. It offers institutional-grade risk metrics, Monte Carlo simulations, and expert visualizations and was built with yfinance for real-time data.

**Ideal for:**  Quantitative analysts, portfolio managers, equity traders, and finance students

### Why This Project?

- 📈 Use a weighted average cost basis to track several stock positions
- 🎲 Using Monte Carlo simulations for portfolio projections (more than 10,000 scenarios).
- 📊 Calculate the Sharpe Ratio, Beta, VaR, and Maximum Drawdown
- 🖼️ Create reports and charts that are ready for publication
- 💾 Basic data management using CSV

---

## ✨ Features

### Current Features (v1.0)

✅ **Multi-Transaction Support**
- Automatically aggregates multiple purchases of the same stock
- Calculates weighted average buy price
- Displays transaction history breakdown

✅ **Real-Time Portfolio Tracking**
- Live NSE/BSE stock prices via yfinance API
- Current portfolio value and P&L calculations
- Position-level and portfolio-level analytics

✅ **Risk Metrics Analysis**
- **Sharpe Ratio** - Risk-adjusted returns measurement
- **Beta** - Portfolio volatility vs Nifty 50
- **Value at Risk (VaR)** - 95% confidence downside risk
- **Maximum Drawdown** - Largest peak-to-trough decline
- **Annual Volatility** - Standard deviation of returns

✅ **Individual Stock Metrics**
- Annualized returns per stock
- Volatility analysis
- Stock-level Sharpe ratios

✅ **Monte Carlo Portfolio Projection**
- 10,000+ simulation scenarios
- Confidence intervals (5th, 25th, 50th, 75th, 95th percentiles)
- Probability of profit calculations
- Visual projection paths

✅ **Professional Visualizations**
- Portfolio allocation pie chart
- P&L bar charts by position
- Historical performance comparison (normalized)
- Returns distribution histogram
- Monte Carlo projection paths
- Final value probability distribution

---

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup
- Clone the repository
  git clone https://github.com/YOUR_USERNAME/trivya-portfolio-tracker.git
  cd trivya-portfolio-tracker
- Create virtual environment
  python -m venv venv
- Activate virtual environment
  On Windows:
  venv\Scripts\activate
- On macOS/Linux:
  source venv/bin/activate
- Install dependencies
  pip install -r requirements.txt

### Dependencies
- yfinance>=0.2.30
- pandas>=2.0.0
- numpy>=1.24.0
- matplotlib>=3.7.0
- scipy>=1.11.0

---

## 🖼️ Screenshots

### Portfolio Analytics Dashboard
![Portfolio Dashboard](outputs/portfolio_analysis.png)

*4-panel dashboard showing allocation, P&L, historical performance, and returns distribution*

### Monte Carlo Projection
![Monte Carlo](outputs/monte_carlo_projection.png)

*10,000 simulated portfolio paths with confidence intervals*

---

## 📂 Project Structure

Trivya-portfolio-tracker/
├──  portfolio_tracker.py
├──  holdings.csv
├──  requirements.txt
├──  README.md 
├──  outputs
├──  portfolio_analysis.png
├──  monte_carlo_projection.png

## 🗺️ Roadmap

| Phase | Feature | Status |
|-------|---------|--------|
| **Week 1** | Equity tracker with risk metrics | ✅ Complete |
| **Week 2** | Options Greeks calculator | 🔨 In Progress |
| **Week 3** | Streamlit interactive dashboard | 📋 Planned |
| **Week 4** | Backtesting engine | 📋 Planned |
| **Week 5** | Portfolio optimization | 📋 Planned |
| **Week 6** | Alert system & notifications | 📋 Planned |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Use Cases

### For Traders
- Track real-time P&L across multiple positions
- Understand portfolio risk exposure (Beta, VaR)
- Project future portfolio values with Monte Carlo

### For Students
- Learn portfolio management concepts hands-on
- Understand risk metrics practically
- Build finance + Python skills simultaneously

### For Analysts
- Generate professional reports for presentations
- Export data for further analysis
- Visualize complex portfolio data easily

---

## ⚠️ Disclaimer

This tool is for **educational and analytical purposes only**. It is not financial advice. Always consult with a qualified financial advisor before making investment decisions. Past performance does not guarantee future results.

Market data is sourced from yfinance (Yahoo Finance) and may have delays or inaccuracies.

---

## 📬 Contact

**Built by:** Pratyush
**LinkedIn:** 
**Email:** pratyushsingh.live@gmail.com

**Project Link:** 
---

## 🙏 Acknowledgments

- [yfinance](https://github.com/ranaroussi/yfinance) for market data API
- [pandas](https://pandas.pydata.org/) for data manipulation
- [matplotlib](https://matplotlib.org/) for visualizations
- NSE India for providing market data access

---

<div align="center">

**⭐ Star this repo if you find it useful!**

</div>

### Core Implementation Code & Architecture
#### File: `.devcontainer/devcontainer.json`
```python
{
  "name": "Python 3",
  // Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
  "image": "mcr.microsoft.com/devcontainers/python:1-3.11-bookworm",
  "customizations": {
    "codespaces": {
      "openFiles": [
        "README.md",
        "streamlit_dashboard.py"
      ]
    },
    "vscode": {
      "settings": {},
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "updateContentCommand": "[ -f packages.txt ] && sudo apt update && sudo apt upgrade -y && sudo xargs apt install -y <packages.txt; [ -f requirements.txt ] && pip3 install --user -r requirements.txt; pip3 install --user streamlit; echo '✅ Packages installed and Requirements met'",
  "postAttachCommand": {
    "server": "streamlit run streamlit_dashboard.py --server.enableCORS false --server.enableXsrfProtection false"
  },
  "portsAttributes": {
    "8501": {
      "label": "Application",
      "onAutoForward": "openPreview"
    }
  },
  "forwardPorts": [
    8501
  ]
}
```

#### File: `options_tracker.py`
```python
"""
Options Tracker & Greeks Calculator
Tracks Nifty/Bank Nifty options positions, calculates Greeks, and analyzes strategies
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from scipy.stats import norm

class OptionsTracker:
    def __init__(self, csv_file):
        """Initialize options tracker with positions CSV"""
        self.positions = pd.read_csv(csv_file)
        self.positions['date'] = pd.to_datetime(self.positions['date'])
        self.positions['expiry'] = pd.to_datetime(self.positions['expiry'])
        self.spot_price = None
        self.risk_free_rate = 0.068  # India 10Y G-Sec rate
        
    def fetch_spot_price(self):
        """Fetch current Nifty spot price"""
        print("\n" + "="*60)
        print("FETCHING NIFTY SPOT PRICE...")
        print("="*60)
        
        try:
            nifty = yf.Ticker("^NSEI")
            self.spot_price = nifty.info.get('regularMarketPrice', 
                                            nifty.history(period='1d')['Close'].iloc[-1])
            print(f"✓ Nifty Spot: ₹{self.spot_price:,.2f}")
        except:
            print("⚠ Could not fetch live price, using default")
            self.spot_price = 25000
        
        return self.spot_price
    
    def calculate_time_to_expiry(self, expiry_date):
        """Calculate time to expiry in years"""
        today = datetime.now()
        days_to_expiry = (expiry_date - today).days
        return max(days_to_expiry / 365.0, 0.001)  # Min 0.001 to avoid division by zero
    
    def black_scholes_greeks(self, S, K, T, r, sigma, option_type):
        """
        Calculate Black-Scholes price and Greeks
        S: Spot price
        K: Strike price
        T: Time to expiry (years)
        r: Risk-free rate
        sigma: Implied volatility
        option_type: 'CE' or 'PE'
        """
        # Handle expired options
        if T <= 0:
            if option_type == 'CE':
                price = max(S - K, 0)
            else:
                price = max(K - S, 0)
            return {
                'price': price,
                'delta': 0,
                'gamma': 0,
                'theta': 0,
                'vega': 0
            }
        
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        
        if option_type == 'CE':
            price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
            delta = norm.cdf(d1)
            theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
                     - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365
        else:  # PE
            price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
            delta = -norm.cdf(-d1)
            theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
                     + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365
        
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega = S * norm.pdf(d1) * np.sqrt(T) / 100  # Divide by 100 for 1% change
        
        return {
            'price': price,
            'delta': delta,
            'gamma': gamma,
            'theta': theta,
            'vega': vega
        }
    
    def estimate_iv(self, market_price, S, K, T, r, option_type):
        """Estimate implied volatility using simple iteration"""
        if T <= 0 or market_price <= 0:
            return 0.20  # Default 20% IV
        
        # Simple IV estimation (not Newton-Raphson, just approximation)
        for sigma in np.arange(0.05, 2.0, 0.01):
            greeks = self.black_scholes_greeks(S, K, T, r, sigma, option_type)
            if abs(greeks['price'] - market_price) < 1:
                return sigma
        
        return 0.20  # Default if no convergence
    
    def calculate_current_greeks(self):
        """Calculate Greeks for all current positions"""
        print("\n" + "="*60)
        print("CALCULATING GREEKS FOR ALL POSITIONS...")
        print("="*60)
        
        if self.spot_price is None:
            self.fetch_spot_price()
        
        for i, pos in self.positions.iterrows():
            T = self.calculate_time_to_expiry(pos['expiry'])
            
            # Estimate IV from premium paid (simplified)
            # In reality, you'd fetch this from market data
            sigma = self.estimate_iv(
                pos['premium_paid'], 
                self.spot_price, 
                pos['strike'], 
                T, 
                self.risk_free_rate, 
                pos['option_type']
            )
            
            greeks = self.black_scholes_greeks(
                self.spot_price,
                pos['strike'],
                T,
                self.risk_free_rate,
                sigma,
                pos['option_type']
            )
            
            # Store Greeks in dataframe
            self.positions.at[i, 'current_price'] = greeks['price']
            self.positions.at[i, 'delta'] = greeks['delta'] * pos['quantity']
            self.positions.at[i, 'gamma'] = greeks['gamma'] * pos['quantity']
            self.positions.at[i, 'theta'] = greeks['theta'] * pos['quantity']
            self.positions.at[i, 'vega'] = greeks['vega'] * pos['quantity']
            self.positions.at[i, 'iv'] = sigma
            
            # P&L calculation
            if pos['quantity'] > 0:  # Long position
                pnl = (greeks['price'] - pos['premium_paid']) * pos['quantity']
            else:  # Short position
                pnl = (pos['premium_paid'] - greeks['price']) * pos['quantity']
            
            self.positions.at[i, 'pnl'] = pnl
            
            print(f"✓ {pos['option_type']} {pos['strike']} - "
                  f"Delta: {greeks['delta']:.3f}, Theta: {greeks['theta']:.2f}")
        
        return self.positions
    
    def display_positions_summary(self):
        """Display options positions with Greeks"""
        print("\n" + "="*60)
        print("OPTIONS POSITIONS SUMMARY")
        print("="*60)
        
        total_pnl = self.positions['pnl'].sum()
        portfolio_delta = self.positions['delta'].sum()
        portfolio_theta = self.positions['theta'].sum()
        portfolio_vega = self.positions['vega'].sum()
        
        print(f"\nSpot Price:        ₹{self.spot_price:,.2f}")
        print(f"Total P&L:         ₹{total_pnl:,.2f}")
        print(f"Portfolio Delta:   {portfolio_delta:,.2f}")
        print(f"Portfolio Theta:   ₹{portfolio_theta:,.2f}/day")
        print(f"Portfolio Vega:    ₹{portfolio_vega:,.2f}/1% IV change")
        
        print("\n" + "-"*100)
        print(f"{'Type':<6} {'Strike':<8} {'Expiry':<12} {'Qty':<6} {'Premium':<10} "
              f"{'Current':<10} {'P&L':<10} {'Delta':<8} {'Theta':<8}")
        print("-"*100)
        
        for _, pos in self.positions.iterrows():
            days_left = (pos['expiry'] - datetime.now()).days
            print(f"{pos['option_type']:<6} {pos['strike']:<8.0f} "
                  f"{days_left:>3}d left   {pos['quantity']:<6.0f} "
                  f"₹{pos['premium_paid']:<9.2f} ₹{pos['current_price']:<9.2f} "
                  f"₹{pos['pnl']:<9,.0f} {pos['delta']:<8.2f} {pos['theta']:<8.2f}")
        
        print("-"*100)
    
    def analyze_strategies(self):
        """Analyze strategy-wise P&L"""
        print("\n" + "="*60)
        print("STRATEGY-WISE ANALYSIS")
        print("="*60)
        
        strategy_pnl = self.positions.groupby('strategy').agg({
            'pnl': 'sum',
            'delta': 'sum',
            'theta': 'sum'
        })
        
        print(f"\n{'Strategy':<20} {'Total P&L':<15} {'Net Delta':<12} {'Net Theta':<12}")
        print("-"*60)
        
        for strategy, row in strategy_pnl.iterrows():
            print(f"{strategy:<20} ₹{row['pnl']:<14,.2f} {row['delta']:<12.2f} {row['theta']:<12.2f}")
    
    def bear_put_spread_analysis(self):
        """Detailed analysis for bear put spreads"""
        print("\n" + "="*60)
        print("BEAR PUT SPREAD DETAILED ANALYSIS")
        print("="*60)
        
        spreads = self.positions[self.positions['strategy'] == 'bear_put_spread']
        
        if len(spreads) == 0:
            print("No bear put spreads found in portfolio")
            return
        
        # Group by expiry to find matching legs
        for expiry in spreads['expiry'].unique():
            spread_legs = spreads[spreads['expiry'] == expiry]
            
            if len(spread_legs) == 2:
                long_put = spread_legs[spread_legs['quantity'] > 0].iloc[0]
                short_put = spread_legs[spread_legs['quantity'] < 0].iloc[0]
                
                max_profit = (long_put['strike'] - short_put['strike'] - 
                             (long_put['premium_paid'] - short_put['premium_paid']))
                max_loss = long_put['premium_paid'] - short_put['premium_paid']
                
                current_pnl = spread_legs['pnl'].sum()
                
                print(f"\nExpiry: {expiry.strftime('%Y-%m-%d')}")
                print(f"Long Put:  {long_put['strike']} PE @ ₹{long_put['premium_paid']}")
                print(f"Short Put: {short_put['strike']} PE @ ₹{short_put['premium_paid']}")
                print(f"\nMax Profit:    ₹{max_profit * abs(long_put['quantity']):,.2f}")
                print(f"Max Loss:      ₹{max_loss * abs(long_put['quantity']):,.2f}")
                print(f"Current P&L:   ₹{current_pnl:,.2f}")
                print(f"Risk/Reward:   1:{max_profit/max_loss:.2f}")
                
                # Breakeven
                breakeven = long_put['strike'] - max_loss
                print(f"Breakeven:     ₹{breakeven:,.2f}")
                
                if self.spot_price < breakeven:
                    print(f"Status: ✓ In profit zone (Spot below breakeven)")
                else:
                    print(f"Status: ⚠ Above breakeven (Spot: ₹{self.spot_price:,.2f})")
    
    def create_visualizations(self):
        """Generate options analytics charts"""
        print("\n" + "="*60)
        print("GENERATING OPTIONS VISUALIZATIONS...")
        print("="*60)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Options Portfolio Analytics', fontsize=16, fontweight='bold')
        
        # 1. P&L by Position
        ax1 = axes[0, 0]
        position_labels = [f"{row['option_type']}{row['strike']}" 
                          for _, row in self.positions.iterrows()]
        colors_pnl = ['green' if x > 0 else 'red' for x in self.positions['pnl']]
        ax1.bar(range(len(self.positions)), self.positions['pnl'], color=colors_pnl)
        ax1.set_xticks(range(len(self.positions)))
        ax1.set_xticklabels(position_labels, rotation=45, ha='right')
        ax1.set_title('P&L by Option Position')
        ax1.set_ylabel('P&L (₹)')
        ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax1.grid(axis='y', alpha=0.3)
        
        # 2. Greeks Distribution
        ax2 = axes[0, 1]
        greeks_df = pd.DataFrame({
            'Delta': self.positions['delta'].abs().sum(),
            'Gamma': self.positions['gamma'].abs().sum() * 100,  # Scale for visibility
            'Theta': abs(self.positions['theta'].sum()),
            'Vega': abs(self.positions['vega'].sum())
        }, index=[0])
        
        greeks_df.T.plot(kind='bar', ax=ax2, legend=False, color='steelblue')
        ax2.set_title('Portfolio Greeks (Absolute Values)')
        ax2.set_ylabel('Value')
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
        ax2.grid(axis='y', alpha=0.3)
        
        # 3. Payoff Diagram for Bear Put Spread
        ax3 = axes[1, 0]
        spreads = self.positions[self.positions['strategy'] == 'bear_put_spread']
        
        if len(spreads) >= 2:
            long_put = spreads[spreads['quantity'] > 0].iloc[0]
            short_put = spreads[spreads['quantity'] < 0].iloc[0]
            
            # Generate spot price range
            spot_range = np.linspace(
                short_put['strike'] - 500, 
                long_put['strike'] + 500, 
                100
            )
            
            net_premium = long_put['premium_paid'] - short_put['premium_paid']
            
            payoffs = []
            for spot in spot_range:
                long_payoff = max(long_put['strike'] - spot, 0) - long_put['premium_paid']
                short_payoff = short_put['premium_paid'] - max(short_put['strike'] - spot, 0)
                payoffs.append((long_payoff + short_payoff) * abs(long_put['quantity']))
            
            ax3.plot(spot_range, payoffs, linewidth=2, color='darkblue')
            ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
            ax3.axvline(x=self.spot_price, color='red', linestyle='--', 
                       linewidth=2, label=f'Current Spot: ₹{self.spot_price:,.0f}')
            ax3.fill_between(spot_range, 0, payoffs, 
                            where=np.array(payoffs) > 0, 
                            alpha=0.3, color='green', label='Profit Zone')
            ax3.fill_between(spot_range, 0, payoffs, 
                            where=np.array(payoffs) < 0, 
                            alpha=0.3, color='red', label='Loss Zone')
            ax3.set_title('Bear Put Spread Payoff Diagram')
            ax3.set_xlabel('Nifty Spot Price')
            ax3.set_ylabel('P&L at Expiry (₹)')
            ax3.legend()
            ax3.grid(alpha=0.3)
        
        # 4. Time Decay (Theta) Analysis
        ax4 = axes[1, 1]
        days_to_expiry = [(row['expiry'] - datetime.now()).days 
                         for _, row in self.positions.iterrows()]
        ax4.scatter(days_to_expiry, self.positions['theta'], 
                   s=100, alpha=0.6, c=self.positions['theta'], cmap='RdYlGn_r')
        ax4.set_title('Theta vs Days to Expiry')
        ax4.set_xlabel('Days to Expiry')
        ax4.set_ylabel('Theta (₹/day)')
        ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax4.grid(alpha=0.3)
        
        # Add labels
        for i, (days, theta) in enumerate(zip(days_to_expiry, self.positions['theta'])):
            ax4.annotate(f"{self.positions.iloc[i]['option_type']}{self.positions.iloc[i]['strike']:.0f}", 
                        (days, theta), fontsize=8)
        
        plt.tight_layout()
        plt.savefig('options_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: options_analysis.png")
        
        return fig
    
    def generate_report(self):
        """Generate complete options report"""
        print("\n" + "="*80)
        print(" "*20 + "OPTIONS PORTFOLIO REPORT")
        print(" "*25 + f"{datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*80)
        
        self.fetch_spot_price()
        self.calculate_current_greeks()
    
# ... [TRUNCATED FILE CONTENT]
```

#### File: `backtest_strategies.py`
```python
"""
Strategy Backtesting & Monte Carlo Simulation System
Validates trading strategies and projects portfolio outcomes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from scipy.stats import norm
import warnings
warnings.filterwarnings('ignore')

class StrategyBacktester:
    def __init__(self, trades_csv=None):
        """
        Initialize backtester
        trades_csv: CSV file with historical trades (optional)
        """
        if trades_csv:
            self.trades = pd.read_csv(trades_csv)
            self.trades['entry_date'] = pd.to_datetime(self.trades['entry_date'])
            self.trades['exit_date'] = pd.to_datetime(self.trades['exit_date'])
        else:
            self.trades = None
        
        self.results = None
        
    def backtest_options_trades(self):
        """Backtest historical options trades"""
        if self.trades is None or len(self.trades) == 0:
            print("⚠ No trade data available for backtesting")
            return None
        
        print("\n" + "="*70)
        print("BACKTESTING HISTORICAL OPTIONS TRADES")
        print("="*70)
        
        results = []
        
        for i, trade in self.trades.iterrows():
            # Calculate holding period
            holding_days = (trade['exit_date'] - trade['entry_date']).days
            
            # Calculate P&L
            if trade['position_type'] == 'long':
                pnl = (trade['exit_price'] - trade['entry_price']) * trade['quantity']
            else:  # short
                pnl = (trade['entry_price'] - trade['exit_price']) * trade['quantity']
            
            # Calculate return percentage
            capital_deployed = trade['entry_price'] * abs(trade['quantity'])
            return_pct = (pnl / capital_deployed) * 100 if capital_deployed > 0 else 0
            
            results.append({
                'trade_id': i + 1,
                'entry_date': trade['entry_date'],
                'exit_date': trade['exit_date'],
                'strategy': trade['strategy'],
                'holding_days': holding_days,
                'pnl': pnl,
                'return_pct': return_pct,
                'win': 1 if pnl > 0 else 0
            })
        
        self.results = pd.DataFrame(results)
        
        # Calculate statistics
        total_trades = len(self.results)
        winning_trades = self.results['win'].sum()
        losing_trades = total_trades - winning_trades
        win_rate = (winning_trades / total_trades) * 100
        
        avg_win = self.results[self.results['win'] == 1]['pnl'].mean()
        avg_loss = self.results[self.results['win'] == 0]['pnl'].mean()
        
        total_pnl = self.results['pnl'].sum()
        avg_return = self.results['return_pct'].mean()
        
        # Profit factor
        gross_profit = self.results[self.results['pnl'] > 0]['pnl'].sum()
        gross_loss = abs(self.results[self.results['pnl'] < 0]['pnl'].sum())
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0
        
        # Expectancy
        expectancy = (win_rate/100 * avg_win) + ((1 - win_rate/100) * avg_loss)
        
        # Display results
        print(f"\nTotal Trades:        {total_trades}")
        print(f"Winning Trades:      {winning_trades} ({win_rate:.1f}%)")
        print(f"Losing Trades:       {losing_trades} ({100-win_rate:.1f}%)")
        print(f"\nAverage Win:         ₹{avg_win:,.2f}")
        print(f"Average Loss:        ₹{avg_loss:,.2f}")
        print(f"Win/Loss Ratio:      {abs(avg_win/avg_loss):.2f}x" if avg_loss != 0 else "N/A")
        print(f"\nTotal P&L:           ₹{total_pnl:,.2f}")
        print(f"Average Return:      {avg_return:.2f}%")
        print(f"Profit Factor:       {profit_factor:.2f}")
        print(f"Expectancy:          ₹{expectancy:.2f} per trade")
        
        # Interpretation
        print("\n" + "-"*70)
        print("INTERPRETATION:")
        print("-"*70)
        
        if win_rate >= 60:
            print("✓ Win Rate > 60%: Excellent strategy performance")
        elif win_rate >= 50:
            print("⚠ Win Rate > 50%: Acceptable, but room for improvement")
        else:
            print("✗ Win Rate < 50%: Strategy needs refinement")
        
        if profit_factor > 2:
            print("✓ Profit Factor > 2: Strong risk/reward profile")
        elif profit_factor > 1:
            print("⚠ Profit Factor > 1: Profitable but moderate efficiency")
        else:
            print("✗ Profit Factor < 1: Strategy losing money")
        
        if expectancy > 0:
            print(f"✓ Positive Expectancy: Expected to earn ₹{expectancy:.2f} per trade")
        else:
            print(f"✗ Negative Expectancy: Expected to lose ₹{abs(expectancy):.2f} per trade")
        
        return {
            'total_trades': total_trades,
            'win_rate': win_rate,
            'profit_factor': profit_factor,
            'expectancy': expectancy,
            'total_pnl': total_pnl
        }
    
    def strategy_breakdown(self):
        """Break down performance by strategy type"""
        if self.results is None:
            return
        
        print("\n" + "="*70)
        print("STRATEGY-WISE BREAKDOWN")
        print("="*70)
        
        strategy_stats = self.results.groupby('strategy').agg({
            'pnl': ['sum', 'mean', 'count'],
            'win': 'sum',
            'return_pct': 'mean'
        }).round(2)
        
        print(f"\n{'Strategy':<20} {'Trades':<8} {'Win%':<10} {'Total P&L':<15} {'Avg Return':<12}")
        print("-"*70)
        
        for strategy in strategy_stats.index:
            trades = strategy_stats.loc[strategy, ('pnl', 'count')]
            wins = strategy_stats.loc[strategy, ('win', 'sum')]
            win_pct = (wins / trades) * 100
            total_pnl = strategy_stats.loc[strategy, ('pnl', 'sum')]
            avg_return = strategy_stats.loc[strategy, ('return_pct', 'mean')]
            
            print(f"{strategy:<20} {int(trades):<8} {win_pct:<9.1f}% ₹{total_pnl:<13,.0f} {avg_return:>10.2f}%")
    
    def monte_carlo_simulation(self, initial_capital=100000, num_simulations=10000, num_trades=50):
        """
        Monte Carlo simulation for portfolio outcomes
        Based on historical trade statistics
        """
        print("\n" + "="*70)
        print("MONTE CARLO PORTFOLIO SIMULATION")
        print("="*70)
        
        if self.results is None or len(self.results) == 0:
            print("⚠ No backtest results. Creating sample simulation...")
            # Use sample statistics if no real data
            win_rate = 0.55
            avg_win = 5000
            avg_loss = -3000
            std_win = 2000
            std_loss = 1500
        else:
            # Use actual backtest statistics
            win_rate = self.results['win'].mean()
            avg_win = self.results[self.results['pnl'] > 0]['pnl'].mean()
            avg_loss = self.results[self.results['pnl'] < 0]['pnl'].mean()
            std_win = self.results[self.results['pnl'] > 0]['pnl'].std()
            std_loss = self.results[self.results['pnl'] < 0]['pnl'].std()
        
        print(f"\nSimulation Parameters:")
        print(f"Initial Capital:     ₹{initial_capital:,.0f}")
        print(f"Number of Trades:    {num_trades}")
        print(f"Simulations:         {num_simulations:,}")
        print(f"Win Rate:            {win_rate*100:.1f}%")
        print(f"Avg Win:             ₹{avg_win:,.0f}")
        print(f"Avg Loss:            ₹{avg_loss:,.0f}")
        
        # Run simulations
        final_capitals = []
        max_drawdowns = []
        
        for _ in range(num_simulations):
            capital = initial_capital
            peak_capital = initial_capital
            max_dd = 0
            
            for trade_num in range(num_trades):
                # Determine if trade wins or loses
                if np.random.random() < win_rate:
                    # Winning trade
                    pnl = np.random.normal(avg_win, std_win)
                else:
                    # Losing trade
                    pnl = np.random.normal(avg_loss, std_loss)
                
                capital += pnl
                
                # Track drawdown
                if capital > peak_capital:
                    peak_capital = capital
                
                current_dd = (peak_capital - capital) / peak_capital
                max_dd = max(max_dd, current_dd)
                
                # Risk of ruin - stop if capital drops too low
                if capital < initial_capital * 0.2:  # 80% drawdown = ruin
                    break
            
            final_capitals.append(capital)
            max_drawdowns.append(max_dd)
        
        final_capitals = np.array(final_capitals)
        max_drawdowns = np.array(max_drawdowns)
        
        # Calculate statistics
        median_final = np.median(final_capitals)
        mean_final = np.mean(final_capitals)
        
        percentile_5 = np.percentile(final_capitals, 5)
        percentile_25 = np.percentile(final_capitals, 25)
        percentile_75 = np.percentile(final_capitals, 75)
        percentile_95 = np.percentile(final_capitals, 95)
        
        prob_profit = (final_capitals > initial_capital).sum() / num_simulations * 100
        prob_double = (final_capitals > initial_capital * 2).sum() / num_simulations * 100
        prob_ruin = (final_capitals < initial_capital * 0.2).sum() / num_simulations * 100
        
        avg_max_dd = np.mean(max_drawdowns) * 100
        
        # Display results
        print("\n" + "-"*70)
        print("SIMULATION RESULTS:")
        print("-"*70)
        
        print(f"\nFinal Capital Statistics:")
        print(f"Median:              ₹{median_final:,.0f}")
        print(f"Mean:                ₹{mean_final:,.0f}")
        print(f"5th Percentile:      ₹{percentile_5:,.0f}")
        print(f"95th Percentile:     ₹{percentile_95:,.0f}")
        
        print(f"\nProbabilities:")
        print(f"Profit (>0%):        {prob_profit:.1f}%")
        print(f"Double (>100%):      {prob_double:.1f}%")
        print(f"Ruin (<-80%):        {prob_ruin:.1f}%")
        
        print(f"\nRisk Metrics:")
        print(f"Avg Max Drawdown:    {avg_max_dd:.2f}%")
        
        # Interpretation
        print("\n" + "-"*70)
        print("INTERPRETATION:")
        print("-"*70)
        
        if prob_profit > 70:
            print("✓ >70% chance of profit: Strong strategy edge")
        elif prob_profit > 50:
            print("⚠ 50-70% chance of profit: Moderate edge")
        else:
            print("✗ <50% chance of profit: Weak strategy")
        
        if prob_ruin < 5:
            print("✓ <5% risk of ruin: Good capital preservation")
        elif prob_ruin < 10:
            print("⚠ 5-10% risk of ruin: Moderate risk")
        else:
            print("✗ >10% risk of ruin: High risk - consider reducing position sizes")
        
        return {
            'final_capitals': final_capitals,
            'max_drawdowns': max_drawdowns,
            'prob_profit': prob_profit,
            'prob_ruin': prob_ruin,
            'median_final': median_final
        }
    
    def create_visualizations(self, mc_results=None):
        """Generate backtest and Monte Carlo visualizations"""
        print("\n" + "="*70)
        print("GENERATING BACKTEST VISUALIZATIONS...")
        print("="*70)
        
        if self.results is None:
            print("⚠ No backtest results to visualize")
            return
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Strategy Backtesting & Monte Carlo Analysis', 
                     fontsize=16, fontweight='bold')
        
        # 1. Cumulative P&L
        ax1 = axes[0, 0]
        cumulative_pnl = self.results['pnl'].cumsum()
        ax1.plot(cumulative_pnl.index, cumulative_pnl.values, linewidth=2, color='navy')
        ax1.axhline(y=0, color='red', linestyle='--', alpha=0.5)
        ax1.fill_between(cumulative_pnl.index, 0, cumulative_pnl.values,
                         where=cumulative_pnl.values >= 0, alpha=0.3, color='green')
        ax1.fill_between(cumulative_pnl.index, 0, cumulative_pnl.values,
                         where=cumulative_pnl.values < 0, alpha=0.3, color='red')
        ax1.set_title('Cumulative P&L Over Time')
        ax1.set_xlabel('Trade Number')
        ax1.set_ylabel('Cumulative P&L (₹)')
        ax1.grid(alpha=0.3)
        
        # 2. Win/Loss Distribution
        ax2 = axes[0, 1]
        wins = self.results[self.results['pnl'] > 0]['pnl']
        losses = self.results[self.results['pnl'] < 0]['pnl']
        
        ax2.hist([wins, losses], bins=20, label=['Wins', 'Losses'],
                color=['green', 'red'], alpha=0.7, edgecolor='black')
        ax2.axvline(x=0, color='black', linestyle='-', linewidth=2)
        ax2.set_title('P&L Distribution')
        ax2.set_xlabel('P&L (₹)')
        ax2.set_ylabel('Frequency')
        ax2.legend()
        ax2.grid(alpha=0.3)
        
        # 3. Returns by Strategy
        ax3 = axes[0, 2]
        strategy_pnl = self.results.groupby('strategy')['pnl'].sum()
        colors = ['green' if x > 0 else 'red' for x in strategy_pnl.values]
        ax3.bar(range(len(strategy_pnl)), strategy_pnl.values, color=colors)
        ax3.set_xticks(range(len(strategy_pnl)))
        ax3.set_xticklabels(strategy_pnl.index, rotation=45, ha='right')
        ax3.set_title('P&L by Strategy')
        ax3.set_ylabel('Total P&L (₹)')
        ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax3.grid(axis='y', alpha=0.3)
        
        # 4. Win Rate Over Time
        ax4 = axes[1, 0]
        rolling_win_rate = self.results['win'].rolling(window=10, min_periods=1).mean() * 100
        ax4.plot(rolling_win_rate.index, rolling_win_rate.values, linewidth=2, color='purple')
        ax4.axhline(y=50, color='orange', linestyle='--', label='Breakeven (50%)')
        ax4.fill_between(rolling_win_rate.index, 50, rolling_win_rate.values,
                         where=rolling_win_rate.values >= 50, alpha=0.3, color='green')
        ax4.set_title('Rolling Win Rate (10-trade window)')
        ax4.set_xlabel('Trade Number')
        ax4.set_ylabel('Win Rate (%)')
        ax4.legend()
        ax4.grid(alpha=0.3)
        
        # 5. Monte Carlo Results
        ax5 = axes[1, 1]
        if mc_results:
            ax5.hist(mc_results['final_capitals'], bins=50, edgecolor='black', alpha=0.7)
            ax5.axvline(x=mc_results['median_final'], color='red', linestyle='--',
                       linewidth=2, label=f"Median: ₹{mc_results['median_final']:,.0f}")
            ax5.axvline(x=100000, color='orange', linestyle='--',
                       linewidth=2, label='Initial Capital')
            ax5.set_title('Monte Carlo: Final Capital Distri
# ... [TRUNCATED FILE CONTENT]
```

#### File: `holdings_tracker.py`
```python
"""
Portfolio Analytics System
Tracks portfolio performance, calculates risk metrics, and generates visualizations
Handles duplicate stock entries correctly
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats

class PortfolioTracker:
    def __init__(self, csv_file):
        """Initialize portfolio tracker with holdings CSV file"""
        # Load original data (keep for transaction history)
        self.transactions = pd.read_csv(csv_file)
        self.transactions['date'] = pd.to_datetime(self.transactions['date'])
    
    # Create aggregated holdings for calculations
        self.holdings = self._aggregate_positions()
    
        self.portfolio_data = None
        self.historical_data = None
    
        print(f"✓ Loaded {len(self.holdings)} unique positions from {len(self.transactions)} transactions")

    def _aggregate_positions(self):
        """
        Aggregate multiple purchases into single position per stock
        Uses weighted average for buy price
        """
        df = self.transactions if hasattr(self, 'transactions') else self.holdings.copy()
    
    # Check if aggregation is needed
        if df['symbol'].duplicated().any():
            aggregated = df.groupby('symbol').apply(
            lambda x: pd.Series({
                'quantity': x['quantity'].sum(),
                'buy_price': np.average(x['buy_price'], weights=x['quantity']),
                'date': x['date'].min(),
                'num_transactions': len(x)
            })
            ).reset_index()
            return aggregated
        else:
        # No duplicates, return as-is
            return df

    def show_transaction_history(self):
        """Display individual transactions for duplicate positions"""
    
    # Check if we have the original transaction data
        if not hasattr(self, 'transactions'):
         self.transactions = self.holdings.copy()
    
    # Find symbols with multiple purchases
        duplicates = self.transactions['symbol'].value_counts()
        duplicates = duplicates[duplicates > 1]
    
        if len(duplicates) == 0:
         return  # No duplicates, skip this section
    
        print(f"\n📊 Multiple purchases detected: {', '.join(duplicates.index.tolist())}")
        print("\n" + "="*60)
        print("TRANSACTION HISTORY")
        print("="*60)
    
        for symbol in duplicates.index:
         trades = self.transactions[self.transactions['symbol'] == symbol]
        
         print(f"\n{symbol} - {len(trades)} transactions:")
         for _, trade in trades.iterrows():
            print(f"  ├─ {trade['date'].strftime('%Y-%m-%d')} | "
                  f"{int(trade['quantity'])} shares @ ₹{trade['buy_price']:,.2f}")
        
        # Calculate and show aggregated result
            total_qty = trades['quantity'].sum()
            weighted_avg = np.average(trades['buy_price'], weights=trades['quantity'])
            print(f"  └─ TOTAL: {int(total_qty)} shares @ ₹{weighted_avg:,.2f} avg")
     
    def fetch_current_prices(self):
        """Fetch current prices and calculate P&L"""
        print("\n" + "="*60)
        print("FETCHING CURRENT PRICES...")
        print("="*60)
        
        for i, row in self.holdings.iterrows():
            try:
                ticker = yf.Ticker(row['symbol'])
                info = ticker.info
                current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
                
                self.holdings.at[i, 'current_price'] = current_price
                self.holdings.at[i, 'invested_value'] = row['quantity'] * row['buy_price']
                self.holdings.at[i, 'current_value'] = row['quantity'] * current_price
                self.holdings.at[i, 'pnl'] = (current_price - row['buy_price']) * row['quantity']
                self.holdings.at[i, 'pnl_pct'] = ((current_price - row['buy_price']) / row['buy_price']) * 100
                
                print(f"✓ {row['symbol']}: ₹{current_price:,.2f}")
            except Exception as e:
                print(f"✗ Error fetching {row['symbol']}: {str(e)}")
                self.holdings.at[i, 'current_price'] = 0
        
        return self.holdings
    
    def display_portfolio_summary(self):
        """Display portfolio overview"""
        print("\n" + "="*60)
        print("PORTFOLIO SUMMARY")
        print("="*60)
        
        total_invested = self.holdings['invested_value'].sum()
        total_current = self.holdings['current_value'].sum()
        total_pnl = self.holdings['pnl'].sum()
        total_pnl_pct = (total_pnl / total_invested) * 100 if total_invested > 0 else 0
        
        print(f"\nTotal Invested:    ₹{total_invested:,.2f}")
        print(f"Current Value:     ₹{total_current:,.2f}")
        print(f"Total P&L:         ₹{total_pnl:,.2f} ({total_pnl_pct:+.2f}%)")
        
        print("\n" + "-"*60)
        print(f"{'Symbol':<15} {'Qty':<8} {'Buy':<10} {'Current':<10} {'P&L':<12} {'P&L%':<10}")
        print("-"*60)
        
        for _, row in self.holdings.iterrows():
            print(f"{row['symbol']:<15} {int(row['quantity']):<8} "
                  f"₹{row['buy_price']:<9,.0f} ₹{row['current_price']:<9,.0f} "
                  f"₹{row['pnl']:<11,.0f} {row['pnl_pct']:+.2f}%")
        
        print("-"*60)
        
        # Best and worst performers
        best = self.holdings.loc[self.holdings['pnl_pct'].idxmax()]
        worst = self.holdings.loc[self.holdings['pnl_pct'].idxmin()]
        
        print(f"\n🏆 Best Performer:  {best['symbol']} ({best['pnl_pct']:+.2f}%)")
        print(f"📉 Worst Performer: {worst['symbol']} ({worst['pnl_pct']:+.2f}%)")
    
    def fetch_historical_data(self, period="1y"):
        """Fetch historical data for all UNIQUE stocks"""
        print("\n" + "="*60)
        print("FETCHING HISTORICAL DATA...")
        print("="*60)
        
        # Get unique symbols only
        unique_symbols = self.holdings['symbol'].unique().tolist()
        symbols = ' '.join(unique_symbols)
        
        self.historical_data = yf.download(symbols, period=period, progress=False)['Close']
        
        # Handle single stock case
        if isinstance(self.historical_data, pd.Series):
            self.historical_data = self.historical_data.to_frame()
            self.historical_data.columns = [unique_symbols[0]]
        
        print(f"✓ Downloaded {len(self.historical_data)} days of data for {len(unique_symbols)} unique stocks")
        return self.historical_data
    
    def calculate_risk_metrics(self):
        """Calculate comprehensive risk metrics"""
        print("\n" + "="*60)
        print("RISK METRICS ANALYSIS")
        print("="*60)
        
        if self.historical_data is None:
            self.fetch_historical_data()
        
        # Calculate daily returns
        returns = self.historical_data.pct_change().dropna()
        
        # Portfolio weights based on current allocation
        # Group by symbol to handle duplicates
        symbol_allocation = self.holdings.groupby('symbol')['current_value'].sum()
        total_value = symbol_allocation.sum()
        weights = symbol_allocation / total_value
        
        # Ensure weights align with returns columns
        weights = weights.reindex(returns.columns, fill_value=0)
        
        # Portfolio returns
        portfolio_returns = (returns * weights.values).sum(axis=1)
        
        # Risk-free rate (India 10Y G-Sec ≈ 6.8%)
        risk_free_rate = 0.068
        
        # 1. Sharpe Ratio
        excess_returns = portfolio_returns.mean() * 252 - risk_free_rate
        portfolio_vol = portfolio_returns.std() * np.sqrt(252)
        sharpe_ratio = excess_returns / portfolio_vol if portfolio_vol > 0 else 0
        
        # 2. Maximum Drawdown
        cumulative_returns = (1 + portfolio_returns).cumprod()
        running_max = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - running_max) / running_max
        max_drawdown = drawdown.min()
        
        # 3. Value at Risk (95% confidence)
        var_95 = np.percentile(portfolio_returns, 5)
        
        # 4. Beta (vs Nifty 50)
        try:
            nifty = yf.download("^NSEI", period="1y", progress=False)['Close']
            nifty_returns = nifty.pct_change().dropna()
            
            # Align dates
            common_dates = portfolio_returns.index.intersection(nifty_returns.index)
            portfolio_aligned = portfolio_returns.loc[common_dates]
            nifty_aligned = nifty_returns.loc[common_dates]
            
            covariance = np.cov(portfolio_aligned, nifty_aligned)[0][1]
            nifty_variance = np.var(nifty_aligned)
            beta = covariance / nifty_variance if nifty_variance > 0 else 0
        except:
            beta = 0
            print("⚠ Could not calculate Beta (Nifty data unavailable)")
        
        # 5. Volatility
        annual_volatility = portfolio_vol
        
        # Display metrics
        print(f"\nSharpe Ratio:        {sharpe_ratio:.3f}")
        print(f"Maximum Drawdown:    {max_drawdown*100:.2f}%")
        print(f"Value at Risk (95%): {var_95*100:.2f}% (daily)")
        print(f"Annual Volatility:   {annual_volatility*100:.2f}%")
        if beta != 0:
            print(f"Beta (vs Nifty):     {beta:.3f}")
        
        # Interpretation
        print("\n" + "-"*60)
        print("INTERPRETATION:")
        print("-"*60)
        
        if sharpe_ratio > 1:
            print("✓ Sharpe Ratio > 1: Good risk-adjusted returns")
        elif sharpe_ratio > 0:
            print("⚠ Sharpe Ratio > 0: Positive returns but moderate efficiency")
        else:
            print("✗ Sharpe Ratio < 0: Returns below risk-free rate")
        
        if abs(max_drawdown) < 0.10:
            print("✓ Max Drawdown < 10%: Low historical losses")
        elif abs(max_drawdown) < 0.20:
            print("⚠ Max Drawdown < 20%: Moderate risk exposure")
        else:
            print("✗ Max Drawdown > 20%: High risk exposure")
        
        return {
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'var_95': var_95,
            'volatility': annual_volatility,
            'beta': beta
        }
    
    def calculate_stock_metrics(self):
        """Calculate individual stock metrics"""
        print("\n" + "="*60)
        print("INDIVIDUAL STOCK METRICS")
        print("="*60)
        
        if self.historical_data is None:
            self.fetch_historical_data()
        
        returns = self.historical_data.pct_change().dropna()
        
        print(f"\n{'Symbol':<15} {'Ann. Return':<12} {'Volatility':<12} {'Sharpe':<10}")
        print("-"*60)
        
        for col in returns.columns:
            ann_return = returns[col].mean() * 252
            volatility = returns[col].std() * np.sqrt(252)
            sharpe = (ann_return - 0.068) / volatility if volatility > 0 else 0
            
            print(f"{col:<15} {ann_return*100:>10.2f}% {volatility*100:>10.2f}% {sharpe:>10.3f}")
    
    def create_visualizations(self):
        """Generate portfolio visualizations"""
        print("\n" + "="*60)
        print("GENERATING VISUALIZATIONS...")
        print("="*60)
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Portfolio Analytics Dashboard', fontsize=16, fontweight='bold')
        
        # Aggregate holdings by symbol for visualization
        agg_holdings = self.holdings.groupby('symbol').agg({
            'current_value': 'sum',
            'pnl': 'sum',
            'quantity': 'sum'
        }).reset_index()
        
        # 1. Portfolio Allocation Pie Chart
        ax1 = axes[0, 0]
        colors = plt.cm.Set3(range(len(agg_holdings)))
        ax1.pie(agg_holdings['current_value'], 
                labels=agg_holdings['symbol'],
                autopct='%1.1f%%',
                colors=colors,
                startangle=90)
        ax1.set_title('Portfolio Allocation by Value')
        
        # 2. P&L Bar Chart
        ax2 = axes[0, 1]
        colors_pnl = ['green' if x > 0 else 'red' for x in agg_holdings['pnl']]
        ax2.bar(range(len(agg_holdings)), agg_holdings['pnl'], color=colors_pnl)
        ax2.set_xticks(range(len(agg_holdings)))
        ax2.set_xticklabels(agg_holdings['symbol'], rotation=45, ha='right')
        ax2.set_title('Profit/Loss by Stock')
        ax2.set_ylabel('P&L (₹)')
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax2.grid(axis='y', alpha=0.3)
        
        # 3. Historical Performance
        if self.historical_data is not None:
            ax3 = axes[1, 0]
            
            # Normalize prices to 100 for comparison
            normalized = (self.historical_data / self.historical_data.iloc[0]) * 100
            
            for col in normalized.columns:
                ax3.plot(normalized.index, normalized[col], label=col, linewidth=2)
            
            ax3.set_title('Historical Performance (Normalized to 100)')
            ax3.set_xlabel('Date')
            ax3.set_ylabel('Normalized Price')
            ax3.legend(loc='best', fontsize=8)
            ax3.grid(alpha=0.3)
        
        # 4. Returns Distribution
        ax4 = axes[1, 1]
        if self.historical_data is not None:
            returns = self.historical_data.pct_change().dropna()
            
            # Calculate portfolio returns with correct weights
            symbol_allocation = self.holdings.groupby('symbol')['current_value'].sum()
            weights = symbol_allocation / symbol_allocation.sum()
            weights = weights.reindex(returns.columns, fill_value=0)
            
            portfolio_returns = (returns * weights.values).sum(axis=1)
            
            ax4.hist(portfolio_returns * 100, bins=50, edgecolor='black', alpha=0.7)
            ax4.axvline(portfolio_returns.mean() * 100, color='red', 
                       linestyle='--', linewidth=2, label='Mean')
            ax4.set_title('Portfolio Daily Returns Distribution')
            ax4.set_xlabel('Daily Return (%)')
            ax4.set_ylabel('Frequency')
            ax4.legend()
            ax4.grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('portfolio_analysis.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: portfolio_analysis.png")
        
        return fig

    def monte_carlo_portfolio_projection(self, months=12, num_simulations=10000):
        """
        Monte Carlo simulation for EQUITY PORTFOLIO future value projection
        Different from options trading MC - this simulates holding your current stocks
        """
        print("\n" + "="*70)
        print("MONTE CARLO PORTFOLIO PROJECTION")
        print("="*70)
        
        if self.historical_data is None:
            self.fetch_historical_data()
        
        # Calculate returns and
# ... [TRUNCATED FILE CONTENT]
```


==================================================
