# ⚡ [QUANT-SOURCE-163] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_163_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: optionsx-platform (`PHASE4-QUANT-197`)
- **Full Name**: `PHASE4-QUANT-197_parameshwaran-vijayakumar__optionsx-platform`
- **Description**: Advanced Options Trading Platform - Strategy Builder, Greeks Lab, Risk Analysis, Data Lab | Python + Streamlit
- **GitHub Stars**: 0
- **Source Pool**: `phase4_quant_wheels_100`

### Core Implementation Code & Architecture
#### File: `src/api/routes/__init__.py`
```python
"""API route modules."""
```

#### File: `src/api/__init__.py`
```python
"""FastAPI REST API layer."""
```

#### File: `src/ui/__init__.py`
```python
"""Streamlit UI application."""
```

#### File: `src/services/__init__.py`
```python
"""Application services layer."""
```

#### File: `src/data/migrations/__init__.py`
```python
"""Database migrations package."""
```

#### File: `src/utils/__init__.py`
```python
"""Utility functions and helpers."""
```


==================================================


## [2/3] Repository: options-trading-py (`PHASE4-QUANT-200`)
- **Full Name**: `PHASE4-QUANT-200_KevinSheeranxyj__options-trading-py`
- **Description**: Black-scholes + Greeks +   IV + Binomial Tree implement in python
- **GitHub Stars**: 0
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# options-trading-py
Black-scholes + Greeks +   IV + Binomial Tree implement in python

### Core Implementation Code & Architecture
#### File: `src/option_pricing.py`
```python
import math


# =========================
# 1) 基础数学函数
# =========================

def norm_pdf(x: float) -> float:
    """标准正态分布密度函数 φ(x)"""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def norm_cdf(x: float) -> float:
    """标准正态分布累积分布函数 N(x)"""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


# =========================
# 2) d1 / d2
# =========================

def bs_d1(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    """
    Black-Scholes d1
    q: 连续分红收益率
    """
    if S <= 0 or K <= 0 or sigma <= 0 or T <= 0:
        raise ValueError("S, K, sigma, T must be positive.")
    return (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))


def bs_d2(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    """Black-Scholes d2"""
    return bs_d1(S, K, r, sigma, T, q) - sigma * math.sqrt(T)


# =========================
# 3) Black-Scholes 定价
# =========================

def bs_call_price(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    """
    欧式看涨期权价格
    q: 连续分红收益率
    """
    if T <= 0:
        return max(S - K, 0.0)

    d1 = bs_d1(S, K, r, sigma, T, q)
    d2 = d1 - sigma * math.sqrt(T)

    return S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)


def bs_put_price(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    """
    欧式看跌期权价格
    q: 连续分红收益率
    """
    if T <= 0:
        return max(K - S, 0.0)

    d1 = bs_d1(S, K, r, sigma, T, q)
    d2 = d1 - sigma * math.sqrt(T)

    return K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)


# =========================
# 4) Greeks
# =========================

def bs_call_delta(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    d1 = bs_d1(S, K, r, sigma, T, q)
    return math.exp(-q * T) * norm_cdf(d1)


def bs_put_delta(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    d1 = bs_d1(S, K, r, sigma, T, q)
    return math.exp(-q * T) * (norm_cdf(d1) - 1.0)


def bs_gamma(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    d1 = bs_d1(S, K, r, sigma, T, q)
    return math.exp(-q * T) * norm_pdf(d1) / (S * sigma * math.sqrt(T))


def bs_vega(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    """
    返回的是“波动率每变化 1.00（即100%）时价格变化多少”
    若想看“IV 每变化 1%”的影响，可再除以 100
    """
    d1 = bs_d1(S, K, r, sigma, T, q)
    return S * math.exp(-q * T) * norm_pdf(d1) * math.sqrt(T)


def bs_call_theta(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    """
    返回的是每年 theta
    若想换算成每日 theta，可除以 365
    """
    d1 = bs_d1(S, K, r, sigma, T, q)
    d2 = d1 - sigma * math.sqrt(T)

    term1 = -S * math.exp(-q * T) * norm_pdf(d1) * sigma / (2.0 * math.sqrt(T))
    term2 = q * S * math.exp(-q * T) * norm_cdf(d1)
    term3 = -r * K * math.exp(-r * T) * norm_cdf(d2)
    return term1 - term2 + term3


def bs_put_theta(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    d1 = bs_d1(S, K, r, sigma, T, q)
    d2 = d1 - sigma * math.sqrt(T)

    term1 = -S * math.exp(-q * T) * norm_pdf(d1) * sigma / (2.0 * math.sqrt(T))
    term2 = -q * S * math.exp(-q * T) * norm_cdf(-d1)
    term3 = r * K * math.exp(-r * T) * norm_cdf(-d2)
    return term1 + term2 + term3


def bs_call_rho(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    d2 = bs_d2(S, K, r, sigma, T, q)
    return K * T * math.exp(-r * T) * norm_cdf(d2)


def bs_put_rho(S: float, K: float, r: float, sigma: float, T: float, q: float = 0.0) -> float:
    d2 = bs_d2(S, K, r, sigma, T, q)
    return -K * T * math.exp(-r * T) * norm_cdf(-d2)


# =========================
# 5) 隐含波动率 IV 求解
# =========================

def implied_volatility_newton(
    market_price: float,
    S: float,
    K: float,
    r: float,
    T: float,
    option_type: str = "call",
    q: float = 0.0,
    initial_sigma: float = 0.2,
    tol: float = 1e-8,
    max_iter: int = 100
) -> float:
    """
    牛顿法求隐含波动率
    option_type: "call" 或 "put"
    """
    sigma = initial_sigma

    for _ in range(max_iter):
        if option_type == "call":
            price = bs_call_price(S, K, r, sigma, T, q)
        elif option_type == "put":
            price = bs_put_price(S, K, r, sigma, T, q)
        else:
            raise ValueError("option_type must be 'call' or 'put'.")

        diff = price - market_price
        if abs(diff) < tol:
            return sigma

        vega = bs_vega(S, K, r, sigma, T, q)
        if abs(vega) < 1e-12:
            raise RuntimeError("Vega too small, Newton method may fail.")

        sigma = sigma - diff / vega

        if sigma <= 0:
            sigma = 1e-4

    raise RuntimeError("Newton method did not converge.")


def implied_volatility_bisection(
    market_price: float,
    S: float,
    K: float,
    r: float,
    T: float,
    option_type: str = "call",
    q: float = 0.0,
    low: float = 1e-6,
    high: float = 5.0,
    tol: float = 1e-8,
    max_iter: int = 200
) -> float:
    """
    二分法求隐含波动率，更稳
    """
    def price_given_sigma(sig: float) -> float:
        if option_type == "call":
            return bs_call_price(S, K, r, sig, T, q)
        elif option_type == "put":
            return bs_put_price(S, K, r, sig, T, q)
        else:
            raise ValueError("option_type must be 'call' or 'put'.")

    low_price = price_given_sigma(low)
    high_price = price_given_sigma(high)

    if market_price < low_price or market_price > high_price:
        raise RuntimeError("Market price is out of feasible range for given bounds.")

    for _ in range(max_iter):
        mid = 0.5 * (low + high)
        mid_price = price_given_sigma(mid)

        if abs(mid_price - market_price) < tol:
            return mid

        if mid_price < market_price:
            low = mid
        else:
            high = mid

    return 0.5 * (low + high)


# =========================
# 6) 二叉树定价：欧式 / 美式
# =========================

def binomial_option_price(
    S: float,
    K: float,
    r: float,
    sigma: float,
    T: float,
    steps: int,
    option_type: str = "call",
    american: bool = False,
    q: float = 0.0
) -> float:
    """
    CRR 二叉树模型
    option_type: "call" / "put"
    american: True 表示美式
    """
    if steps <= 0:
        raise ValueError("steps must be positive.")
    if T <= 0:
        if option_type == "call":
            return max(S - K, 0.0)
        return max(K - S, 0.0)

    dt = T / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1.0 / u
    disc = math.exp(-r * dt)
    p = (math.exp((r - q) * dt) - d) / (u - d)

    if not (0.0 <= p <= 1.0):
        raise RuntimeError("Risk-neutral probability out of bounds. Try increasing steps or check params.")

    # 终端节点 payoff
    values = []
    for j in range(steps + 1):
        # j 次上涨, steps-j 次下跌
        ST = S * (u ** j) * (d ** (steps - j))
        if option_type == "call":
            values.append(max(ST - K, 0.0))
        elif option_type == "put":
            values.append(max(K - ST, 0.0))
        else:
            raise ValueError("option_type must be 'call' or 'put'.")

    # 倒推
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            hold_value = disc * (p * values[j + 1] + (1.0 - p) * values[j])

            if american:
                ST = S * (u ** j) * (d ** (i - j))
                if option_type == "call":
                    exercise_value = max(ST - K, 0.0)
                else:
                    exercise_value = max(K - ST, 0.0)
                values[j] = max(hold_value, exercise_value)
            else:
                values[j] = hold_value

    return values[0]


# =========================
# 7) 测试
# =========================

if __name__ == "__main__":
    S = 100.0
    K = 100.0
    r = 0.05
    sigma = 0.20
    T = 1.0
    q = 0.0

    call_price = bs_call_price(S, K, r, sigma, T, q)
    put_price = bs_put_price(S, K, r, sigma, T, q)

    print("=== Black-Scholes ===")
    print(f"Call Price: {call_price:.6f}")
    print(f"Put  Price: {put_price:.6f}")

    print("\n=== Greeks (Call) ===")
    print(f"Delta: {bs_call_delta(S, K, r, sigma, T, q):.6f}")
    print(f"Gamma: {bs_gamma(S, K, r, sigma, T, q):.6f}")
    print(f"Vega : {bs_vega(S, K, r, sigma, T, q):.6f}")
    print(f"Theta: {bs_call_theta(S, K, r, sigma, T, q):.6f}  (per year)")
    print(f"Rho  : {bs_call_rho(S, K, r, sigma, T, q):.6f}")

    print("\n=== Greeks (Put) ===")
    print(f"Delta: {bs_put_delta(S, K, r, sigma, T, q):.6f}")
    print(f"Gamma: {bs_gamma(S, K, r, sigma, T, q):.6f}")
    print(f"Vega : {bs_vega(S, K, r, sigma, T, q):.6f}")
    print(f"Theta: {bs_put_theta(S, K, r, sigma, T, q):.6f}  (per year)")
    print(f"Rho  : {bs_put_rho(S, K, r, sigma, T, q):.6f}")

    market_call_price = call_price
    iv_newton = implied_volatility_newton(
        market_price=market_call_price,
        S=S, K=K, r=r, T=T,
        option_type="call", q=q
    )
    iv_bisect = implied_volatility_bisection(
        market_price=market_call_price,
        S=S, K=K, r=r, T=T,
        option_type="call", q=q
    )

    print("\n=== Implied Volatility ===")
    print(f"IV (Newton)   : {iv_newton:.6f}")
    print(f"IV (Bisection): {iv_bisect:.6f}")

    euro_call_tree = binomial_option_price(
        S=S, K=K, r=r, sigma=sigma, T=T,
        steps=200, option_type="call", american=False, q=q
    )
    amer_put_tree = binomial_option_price(
        S=S, K=K, r=r, sigma=sigma, T=T,
        steps=200, option_type="put", american=True, q=q
    )

    print("\n=== Binomial Tree ===")
    print(f"European Call (Tree): {euro_call_tree:.6f}")
    print(f"American Put  (Tree): {amer_put_tree:.6f}")
```


==================================================


## [3/3] Repository: alpaca-options-trading-ai-agent (`PHASE4-QUANT-199`)
- **Full Name**: `PHASE4-QUANT-199_harshkmr__alpaca-options-trading-ai-agent`
- **Description**: OptionPulse AI — Autonomous options trading agent powered by Alpaca Markets, Black-Scholes quantitative Greeks, Google Gemini 3.6 Flash reasoning, and hardcoded deterministic risk gates.
- **GitHub Stars**: 0
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# ⚡ OptionPulse AI (Aegis-Options Agent)

> **Autonomous Multi-Agent Options Trading System on Alpaca Trading API, Model Context Protocol (MCP) & Google Gemini**  
> Production-ready quantitative options intelligence with deterministic risk gates and high-frequency glassmorphic HUD

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Alpaca API](https://img.shields.io/badge/Alpaca-Trading%20API%20%26%20MCP-brightgreen.svg)](https://alpaca.markets/)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-Gemini%203.6%20Flash%20%2F%20OpenAI-blueviolet.svg)](https://aistudio.google.com/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B.svg)](https://streamlit.io/)

---

## 📌 System Deployment & Core Parameters

* **Trading Protocol:** Alpaca Paper Trading API (Configured securely via `.env`)
* **Starting Capital:** **$100,000.00 USD** simulated capital ($400,000.00 Buying Power)
* **Options Target:** High-liquidity US Equity/Index Options (`SPY`, `QQQ`, `NVDA`, `AAPL`, `TSLA`)
* **DTE Strategy Window:** Active short-dated options expiring in **2 to 7 days** (DTE 2–7) with **Delta 0.30 to 0.50**
* **Technical Specifications:** [`docs/SPEC.md`](docs/SPEC.md)

---

## 🏛️ End-to-End System Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│                       1. MARKET PERCEPTION LAYER                       │
│  - Alpaca Stock & Historical Option Data API                           │
│  - Real-Time Underlying Quotes (SPY, QQQ, NVDA, AAPL, TSLA)            │
│  - Active Options Chain Ingestion (DTE: 2–7 Days, Strikes, Bid/Ask)    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                       2. LLM STRATEGY ENGINE                           │
│  - Multi-factor Prompting (Technical Setup, Volatility, Skew)          │
│  - Structured JSON Output Enforcement via Gemini 3.6 Flash / OpenAI    │
│  - Directional Strategy Generation (BUY_CALL / BUY_PUT / Spreads)      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   3. DETERMINISTIC RISK GATE (Hard Code)               │
│  [!] Intercepts every LLM trade decision before execution              │
│  - Position Allocation Cap: Max 5% ($5,000) per single trade           │
│  - Account Drawdown Check: Max 3% daily drawdown breaker               │
│  - Contract Validation: Verified against active Alpaca option list     │
│  - Buying Power Buffer: $1,000 minimum cash cushion enforced           │
└───────────────────┬────────────────────────────────┬───────────────────┘
                    │                                │
            [PASSED]│                        [FAILED]│
                    ▼                                ▼
┌─────────────────────────────────────┐    ┌─────────────────────────────┐
│    4. ALPACA EXECUTION ENGINE       │    │    LOGGED REJECTION         │
│  - Alpaca Paper Trading API Client  │    │  - Audit Trail Updated      │
│  - Order Execution: Market/Limit    │    │  - No Trade Submitted       │
│  - Position State Synchronization   │    └─────────────────────────────┘
└───────────────────┬─────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   5. LIVE DASHBOARD & AUDIT TELEMETRY                  │
│  - Streamlit Web Dashboard: Live P&L, Active Contracts, Balances       │
│  - Explainable AI Trace: LLM Reasoning Rationale & Risk Gate Telemetry │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Deterministic Zero-Trust Risk Gate Specifications

| Guardrail | Hardcoded Rule / Constraint | Action Upon Breach |
| :--- | :--- | :--- |
| **Max Position Sizing** | $\le 5.0\%$ of total portfolio value (\$5,000 max on \$100k) | **REJECT / DOWNSIZE** immediately |
| **Daily Drawdown Breaker** | $\le 3.0\%$ account loss in rolling 24-hour window | **HALT SYSTEM** (freezes trading) |
| **Strike Verification** | Option symbol must exist in Alpaca active contracts query | **REJECT ORDER** (blocks hallucinations) |
| **Buying Power Buffer** | Trade cost + \$1,000 minimum cash cushion | **REJECT ORDER** (prevents margin calls) |
| **Profit/Loss Targets** | Take-Profit at +40%, Stop-Loss at -20% | **AUTO EXIT** automated market close |

---

## 🚀 Quickstart & Usage

### 1. Installation
```bash
git clone https://github.com/harshkmr/alpaca-options-trading-ai-agent.git
cd alpaca-options-trading-ai-agent
pip install -r requirements.txt
```

### 2. Configure Environment (`.env`)
Create or edit your `.env` file:
```env
ALPACA_API_KEY_ID=your_alpaca_key
ALPACA_SECRET_KEY=your_alpaca_secret
ALPACA_PAPER=true
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.6-flash
```

### 3. Launch Streamlit Live Web Dashboard
```bash
streamlit run app.py
```
*Or via CLI:* `python main.py streamlit`  
Opens the institutional trading dashboard at **[http://localhost:8501](http://localhost:8501)**.

### 4. Run Live Simulation in Terminal
```bash
python main.py simulate
```

### 5. Start Autonomous Market-Hours Scheduler (Mon-Fri 9:30 AM – 4:00 PM ET)
```bash
python main.py run
```

### 6. Run Alpaca MCP Server
```bash
python main.py mcp
```

### 7. Run Test Suite
```bash
pytest -v
```

---

## 📂 Project Structure

```text
├── app.py                      # Streamlit Live Dashboard & Monitoring UI
├── config.py                   # Master configuration & risk parameters
├── main.py                     # Multi-command CLI & entry point
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration
├── src/
│   ├── alpaca/                 # Alpaca broker client & MCP server
│   ├── alpaca_client.py        # Alpaca Options Manager wrapper
│   ├── config/settings.py      # Pydantic Settings
│   ├── core/engine.py          # Master orchestrator trading loop
│   ├── core/scheduler.py       # Market-hours APScheduler
│   ├── db/                     # SQLite immutable audit logger
│   ├── execution/              # Order management & position tracker
│   ├── quant/                  # Black-Scholes Greeks, IV & Scanner
│   ├── reasoning/              # Gemini / OpenAI LLM Reasoning Engine
│   ├── risk/gate.py            # Deterministic Zero-Trust Risk Gate
│   ├── risk_guard.py           # Risk gate helper alias
│   └── strategy_engine.py      # LLM Strategy Prompting Engine
├── docs/
│   ├── SLIDES.md               # 5-Slide presentation deck outline
│   ├── PITCH_SCRIPT.md         # 3-Minute word-for-word pitch script
│   ├── SUBMISSION.md           # Submission deliverables checklist
│   ├── SPEC.md                 # Technical specification
│   └── TICKETS.md              # Vertical slice implementation tickets
└── tests/                      # Full unit and integration test suite
```

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

### Core Implementation Code & Architecture
#### File: `src/api/__init__.py`
```python
"""API package."""
from src.api.app import app
```

#### File: `src/__init__.py`
```python
"""OptionPulse AI (Aegis-Options Agent) Package."""
__version__ = "1.0.0"
```

#### File: `src/risk/__init__.py`
```python
"""Deterministic risk gate package."""
from src.risk.gate import DeterministicRiskGate, RiskGateResult
```

#### File: `src/core/__init__.py`
```python
"""Core engine and scheduler package."""
from src.core.engine import OptionPulseEngine
from src.core.scheduler import AutonomousScheduler
```

#### File: `src/db/__init__.py`
```python
"""Database and audit persistence package."""
from src.db.database import get_db_connection, init_db
from src.db.audit_logger import AuditLogger
```

#### File: `src/alpaca/__init__.py`
```python
"""Alpaca integration and MCP server package."""
from src.alpaca.client import AlpacaBrokerClient
from src.alpaca.mcp_server import mcp_server, run_mcp_server
from src.alpaca.mcp_client import AlpacaMCPClientBridge
```


==================================================
