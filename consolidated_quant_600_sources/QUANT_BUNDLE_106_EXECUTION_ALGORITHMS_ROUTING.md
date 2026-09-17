# ⚡ [QUANT-SOURCE-106] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_106_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Trading_System (`WHEEL_Algorithmic_Trading_System`)
- **Full Name**: `Algorithmic_Trading_System`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# 📈 Algorithmic Trading System

![CI](https://github.com/ari2612sarkar/Algorithmic_Trading_System/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![Docker](https://img.shields.io/badge/deploy-Docker-2496ED)
![License](https://img.shields.io/badge/license-MIT-green)

An end-to-end algorithmic trading research platform for NSE equities. It ingests
historical OHLCV data, engineers technical features, trains a deep-learning +
gradient-boosting ensemble to forecast price direction, backtests an RSI/SMA
strategy under realistic risk controls, and serves it all through an interactive
web dashboard — deployable anywhere with a single Docker command.

**Tech stack:** Python · PyTorch (LSTM) · LightGBM · pandas · Plotly · Streamlit ·
APScheduler · Docker.

**Pipeline:** `collect → engineer features → train (LSTM + LightGBM) → predict /
forecast → risk-aware backtest → schedule & monitor`.

> ⚠️ For research and educational use only. This is **not** financial advice and
> places no live broker orders.

## 🖥️ Dashboard

The Streamlit dashboard (`app.py`) gives an interactive view of the whole
pipeline — candlestick + SMA + volume + RSI charts, one-click train/predict/
backtest, a probability gauge, a strategy-vs-buy-&-hold equity curve, a live
scheduler monitor, and a CSV report browser.

```bash
streamlit run app.py          # → http://localhost:8501
```

<!-- Add a screenshot at docs/dashboard.png and uncomment:
![Dashboard](docs/dashboard.png)
-->

## 🌟 Features

### Core Features (100% Implementation)
1. **Data Ingestion** - NSE data via nselib with yfinance fallback for NIFTY 50 stocks
2. **Trading Strategy** - RSI + Moving Average crossover strategy
3. **Backtesting** - Risk-aware historical backtesting with detailed metrics
4. **ML Predictions** - LSTM (deep learning) + LightGBM (gradient boosting) models
5. **CSV Reporting** - Automated logging of trades, performance, and predictions to `reports/`
6. **Full Automation** - Scheduled multi-interval execution for all symbols

### Technical Indicators
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- 20-day & 50-day Simple Moving Averages
- Volume indicators
- Price momentum

## 📋 Requirements

- Python 3.8+
- Active internet connection

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd algo-trading-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Edit `src/config.py` to adjust the universe and strategy/model parameters:

```python
TICKERS = ["RELIANCE", "TCS", "HDFCBANK", "INFY", "ICICIBANK"]  # NIFTY 50 stocks
RSI_WINDOW = 14
SMA_FAST = 20
SMA_SLOW = 50
```

### 3. Run the System

The entry point is the `src.run` CLI module:

```bash
# Collect + cache OHLCV (daily)
python -m src.run --collect

# Train models, then generate next-bar predictions
python -m src.run --train
python -m src.run --predict

# Risk-aware backtest
python -m src.run --backtest

# Run everything across both intervals (1d + 1h)
python -m src.run --all
```

All output is written as timestamped CSV files to the `reports/` directory.

### 4. Interactive Dashboard (Web UI)

An interactive [Streamlit](https://streamlit.io/) dashboard wraps the whole
pipeline — pick a ticker/interval and collect data, train, predict, forecast,
and backtest with live charts:

```bash
streamlit run app.py
```

Then open http://localhost:8501. Features:
- Candlestick chart with SMA overlay, buy-signal markers, and an RSI panel
- One-click **Collect / Train / Predict / Forecast / Backtest** from the sidebar
- Prediction card (UP/DOWN + confidence) and N-bar forecast path
- Risk-aware backtest metrics, equity curve, and trade log
- Browser for the timestamped CSV reports (with download)

## 🐳 Deployment (Docker)

The repo ships a `Dockerfile` and `docker-compose.yml`. CPU-only PyTorch is
installed in the image, so it runs on any host without a GPU.

```bash
# Build and start the dashboard (http://localhost:8501)
docker compose up --build

# Run in the background
docker compose up -d

# Also run the live scheduler daemon (hourly/daily predict + weekly retrain)
docker compose --profile live up -d scheduler
```

`data/`, `models/`, and `reports/` are mounted as volumes, so fetched data,
trained models, and reports persist across container restarts. The timezone
defaults to `Asia/Kolkata` (NSE hours) and can be changed in `docker-compose.yml`.

Because it's a standard container, you can deploy the same image to any
Docker-capable host (a VPS, or PaaS like Render / Railway / Fly.io) — point the
platform at this repo or push the built `algo-trading-dashboard` image.

## 📊 Trading Strategy

### Buy Signal
- **Condition 1**: RSI < 30 (oversold)
- **Condition 2**: 20-day MA crosses above 50-day MA (bullish crossover)

### Sell Signal
- **Condition 1**: RSI > 70 (overbought)
- **Condition 2**: 20-day MA crosses below 50-day MA (bearish crossover)

## 🤖 Machine Learning Models

### Features Used (`src/features.py`)
- Returns (1-bar, 5-bar, 20-bar)
- RSI (14-period)
- SMA 20 & SMA 50
- MACD, MACD signal, MACD histogram
- Volume change & high–low range
- ATR and return-over-ATR

### Labels
Targets are **triple-barrier** labels (take-profit / stop-loss / timeout) computed
from ATR-scaled barriers — a higher signal-to-noise target than naive next-bar
direction. Label = 1 if the TP barrier is hit before the SL barrier.

### Models
1. **LSTM Classifier** (PyTorch, `src/predictor.py`)
   - 2-layer LSTM (hidden=64) with dropout, sigmoid head
   - Trained on scaled, windowed sequences (`SEQ_LEN` per interval)
   - Class-imbalance-weighted loss; runs on GPU if available, else CPU

2. **LightGBM Classifier** (`src/gbm.py`)
   - Gradient-boosted trees on the same feature set
   - Trained per ticker as an ensemble companion to the LSTM

Predictions are the **average of the LSTM and LightGBM probabilities** (the LSTM
alone is used if LightGBM is unavailable). Persisted per ticker/interval under
`models/` and evaluated via a rolling **walk-forward** split.

### Performance Metrics
- Accuracy
- Precision
- Recall
- F1-Score

## 📈 Backtest Metrics

The system calculates:
- **Total Return %**: Overall portfolio performance
- **Win Ratio**: Percentage of profitable trades
- **Sharpe Ratio**: Risk-adjusted returns
- **Max Drawdown**: Largest peak-to-trough decline
- **Number of Trades**: Total buy/sell signals

## 📑 CSV Report Structure

All reports are written to `reports/` as timestamped CSV files:

### `trades_*.csv` / `backtest_*.csv`
Trade signals and backtest results: ticker, interval, total return, win rate, Sharpe, max drawdown, number of trades.

### `predictions_*.csv`
Next-bar model predictions per symbol.

### `training_*.csv`
Model training metrics per symbol.

## 📁 Project Structure

```
algo-trading-system/
├── app.py                   # Streamlit interactive dashboard
├── Dockerfile               # Container image (CPU-only PyTorch)
├── docker-compose.yml       # Dashboard + optional live scheduler
├── .streamlit/config.toml   # Dashboard theme
├── .github/workflows/ci.yml # Lint + compile + import CI
├── LICENSE                  # MIT
├── src/
│   ├── run.py               # CLI entry point
│   ├── config.py            # Universe + parameters
│   ├── data_collector.py    # OHLCV ingestion (nselib + yfinance)
│   ├── strategy.py          # RSI + MA crossover signals
│   ├── backtest.py          # Backtesting engine
│   ├── risk.py              # Risk-aware backtest (ATR stops + Kelly)
│   ├── predictor.py         # Train / predict / forecast orchestration
│   ├── dl_model.py          # LSTM deep-learning model
│   ├── gbm.py               # LightGBM model
│   └── scheduler.py         # APScheduler live daemon
├── data/                    # Cached OHLCV CSVs (git-ignored)
├── models/                  # Trained model artifacts (git-ignored)
├── reports/                 # Timestamped output CSVs (git-ignored)
├── logs/                    # system.log for the Live tab (git-ignored)
├── Demo/                    # Standalone Colab demo notebook
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

## 🧩 Module Breakdown

### 1. DataIngestion
- Fetches historical data from NSE
- Handles API rate limiting
- Generates sample data for testing

### 2. TechnicalAnalysis
- Calculates RSI, MACD, Moving Averages
- Adds volume indicators
- Computes price momentum

### 3. TradingStrategy
- Implements buy/sell logic
- Generates trading signals
- Tracks positions

### 4. Backtester
- Simulates historical trading
- Calculates portfolio returns
- Computes performance metrics

### 5. MLPredictor
- Prepares features from indicators
- Trains classification models
- Predicts next-day movements

### 6. ReportWriter
- Writes trades, performance, and ML results to CSV
- Timestamps each report under `reports/`

### 7. AutomatedTradingSystem
- Orchestrates all modules
- Runs analysis for multiple symbols
- Handles errors gracefully

## 🔧 Advanced Usage

All settings live in `src/config.py`.

### Running for Different Stocks

```python
TICKERS = ['HDFCBANK', 'ICICIBANK', 'SBIN', 'KOTAKBANK', 'AXISBANK']
```

### Changing Strategy Parameters

```python
RSI_WINDOW = 14
SMA_FAST = 20
SMA_SLOW = 50
```

### Tuning the Models

```python
EPOCHS = 40          # LSTM training epochs
SEQ_LEN = {"1d": 10, "1h": 40}    # sequence window per interval
TB_HORIZON = {"1d": 10, "1h": 30} # triple-barrier look-forward
```

## 📊 Sample Output

```
================================================================================
TRADING SYSTEM SUMMARY
================================================================================

RELIANCE:
  Latest Price: ₹2,543.75
  Latest RSI: 45.32
  Total Return: 12.45%
  Win Ratio: 65.50%
  ML Accuracy: 68.75%
  Next Day Prediction: UP

TCS:
  Latest Price: ₹3,687.20
  Latest RSI: 52.18
  Total Return: 8.92%
  Win Ratio: 61.20%
  ML Accuracy: 72.30%
  Next Day Prediction: DOWN

INFY:
  Latest Price: ₹1,523.45
  Latest RSI: 38.67
  Total Return: 15.67%
  Win Ratio: 70.40%
  ML Accuracy: 71.85%
  Next Day Prediction: UP
```

## 🐛 Troubleshooting

### NSE API Issues
- Check internet connection
- Verify nselib is latest version
- System automatically falls back to yfinance if nselib fails


## 📝 Logging

All activities are logged to `trading_system.log`:
- Data fetching operations
- Signal generation
- Backtest results
- ML training progress
- Errors and warnings

## ⚡ Performance Tips

1. **Rate Limiting**: Add delays between API calls
2. **Caching**: Store fetched data locally
3. **Parallel Processing**: Use multiprocessing for multiple symbols
4. **Database**: Store historical data in SQLite/PostgreSQL

## 🔮 Future Enhancements

- [ ] Live trading integration
- [ ] More technical indicators (Bollinger Bands, ATR)
- [ ] Advanced ML models (Random Forest, XGBoost)
- [ ] Real-time WebSocket data
- [ ] Portfolio optimization
- [ ] Risk management system
- [ ] Web dashboard
- [ ] Paper trading mode

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

**Built with ❤️ for algorithmic trading enthusiasts**

### Core Implementation Code & Architecture
#### File: `src/__init__.py`
```python

```

#### File: `.streamlit/config.toml`
```python
[theme]
base = "dark"
primaryColor = "#00C49A"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#161A23"
textColor = "#E6E9EF"
font = "sans serif"

[browser]
gatherUsageStats = false

[client]
toolbarMode = "minimal"
```

#### File: `src/indicators.py`
```python
# src/indicators.py
import pandas as pd
import numpy as np

def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()

def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    gain = up.ewm(alpha=1/n, adjust=False).mean()
    loss = down.ewm(alpha=1/n, adjust=False).mean()
    rs = gain / (loss.replace(0, np.nan))
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)

def macd(close: pd.Series, fast=12, slow=26, signal=9):
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    line = ema_fast - ema_slow
    sig = line.ewm(span=signal, adjust=False).mean()
    hist = line - sig
    return line, sig, hist

def atr(high: pd.Series, low: pd.Series, close: pd.Series, n: int = 14) -> pd.Series:
    """Average True Range — volatility measure used for stops & barrier sizing."""
    prev = close.shift(1)
    tr = pd.concat([(high - low), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()
```

#### File: `src/strategy.py`
```python
# src/strategy.py
import pandas as pd
from src.indicators import rsi, sma
from src.config import RSI_WINDOW, SMA_FAST, SMA_SLOW

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["RSI"] = rsi(out["Close"], RSI_WINDOW)
    out["SMA_F"] = sma(out["Close"], SMA_FAST)
    out["SMA_S"] = sma(out["Close"], SMA_SLOW)
    return out

def generate_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Return df with columns: RSI, SMA_F, SMA_S, signal (1 buy today), position (1 long/0 flat) executed next day."""
    d = add_indicators(df)
    # entry rule (today): RSI<30 and SMA20>SMA50
    d["buy_rule"] = (d["RSI"] < 30) & (d["SMA_F"] > d["SMA_S"])
    # exit rule (today): SMA20<SMA50 OR RSI>50
    d["exit_rule"] = (d["SMA_F"] < d["SMA_S"]) | (d["RSI"] > 50)

    # stateful position (execute next day -> shift to avoid lookahead)
    position = []
    in_pos = False
    for i in range(len(d)):
        if not in_pos and d["buy_rule"].iloc[i]:
            in_pos = True
        elif in_pos and d["exit_rule"].iloc[i]:
            in_pos = False
        position.append(1 if in_pos else 0)
    d["position"] = pd.Series(position, index=d.index).shift(1).fillna(0)  # trade next bar
    d["signal"] = d["buy_rule"].astype(int)
    return d
```

#### File: `src/config.py`
```python
# src/config.py
import logging
import os
from datetime import datetime, timedelta

# ---- Universe ----
TICKERS = ["RELIANCE", "TCS", "HDFCBANK", "INFY", "ICICIBANK"]

# ---- Intervals ----
SUPPORTED_INTERVALS = ("1d", "1h")

# ---- Lookbacks per interval ----
# Daily: 5 years. Hourly: 720 days (yfinance hard cap is ~730 for 1h).
LOOKBACK_DAYS = {"1d": 1825, "1h": 720}

# ---- Strategy / indicator params ----
RSI_WINDOW = 14
SMA_FAST = 20
SMA_SLOW = 50

# ---- ML / DL sequence length per interval ----
# Hourly: ~6 bars/day x 7 days ≈ 40 bars window
SEQ_LEN = {"1d": 10, "1h": 40}

# ---- Triple-barrier horizons per interval ----
TB_HORIZON = {"1d": 10, "1h": 30}  # ~5 trading days hourly

# Training hyper-params
EPOCHS = 40
BATCH_SIZE = 32
LEARNING_RATE = 1e-3
TEST_FRAC = 0.2

# ---- Paths ----
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
MODEL_DIR = os.path.join(PROJECT_ROOT, "models")
REPORT_DIR = os.path.join(PROJECT_ROOT, "reports")
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
for _p in (DATA_DIR, MODEL_DIR, REPORT_DIR, LOG_DIR):
    os.makedirs(_p, exist_ok=True)

# Shared log file the dashboard can tail to show live scheduler/CLI activity.
LOG_FILE = os.path.join(LOG_DIR, "system.log")


def date_range(lookback_days: int):
    """Return (start, end) as dd-mm-YYYY strings expected by nselib."""
    end = datetime.today()
    start = end - timedelta(days=lookback_days)
    return start.strftime("%d-%m-%Y"), end.strftime("%d-%m-%Y")


# ---- Logger ----
# Log to both stdout and a rotating file so the dashboard's Live tab can tail it.
from logging.handlers import RotatingFileHandler  # noqa: E402

_fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
_file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=2,
                                    encoding="utf-8")
_file_handler.setFormatter(_fmt)
_stream_handler = logging.StreamHandler()
_stream_handler.setFormatter(_fmt)
logging.basicConfig(level=logging.INFO, handlers=[_stream_handler, _file_handler])
log = logging.getLogger("algo")
```

#### File: `src/backtest.py`
```python
# src/backtest.py
import pandas as pd
import numpy as np

def backtest_long_only(df: pd.DataFrame, fee_bp: float = 5.0) -> dict:
    """
    Long-only, enter when position goes 0->1, exit when 1->0. Fee in basis points per trade side.
    Expects columns: Close, position
    """
    d = df.copy()
    d["pos_prev"] = d["position"].shift(1).fillna(0)
    d["entry"] = (d["position"] == 1) & (d["pos_prev"] == 0)
    d["exit"]  = (d["position"] == 0) & (d["pos_prev"] == 1)

    # daily returns
    d["ret"] = d["Close"].pct_change().fillna(0)
    strat_ret = d["ret"] * d["position"]

    # fees: apply when toggling position
    turn = (d["entry"] | d["exit"]).astype(float)
    fee = (fee_bp / 10000.0) * turn  # subtract on those days
    strat_ret_net = strat_ret - fee

    # equity curve
    d["equity"] = (1 + strat_ret_net).cumprod()

    # trade stats
    entries = d.index[d["entry"]].tolist()
    exits   = d.index[d["exit"]].tolist()
    # align trades (ignore open trade at end)
    pairs = []
    e_ix = 0
    for t_in in entries:
        while e_ix < len(exits) and exits[e_ix] <= t_in:
            e_ix += 1
        if e_ix < len(exits):
            pairs.append((t_in, exits[e_ix]))
            e_ix += 1
    trades = []
    for t_in, t_out in pairs:
        px_in  = d.at[t_in, "Close"]
        px_out = d.at[t_out, "Close"]
        gross = (px_out/px_in) - 1.0
        gross -= 2 * (fee_bp/10000.0)  # entry + exit cost
        trades.append(gross)

    # metrics
    total_return = d["equity"].iloc[-1] - 1.0
    win_rate = float(np.mean([1 if x > 0 else 0 for x in trades])) if trades else 0.0
    sharpe = _sharpe(strat_ret_net)
    max_dd = _max_drawdown(d["equity"])
    return {
        "total_return": total_return,
        "win_rate": win_rate,
        "sharpe": sharpe,
        "max_drawdown": max_dd,
        "n_trades": len(trades),
        "equity_curve": d["equity"],
        "daily_returns": strat_ret_net
    }

def _sharpe(r: pd.Series, risk_free_daily: float = 0.0):
    excess = r - risk_free_daily
    if excess.std() == 0:
        return 0.0
    return (excess.mean() / excess.std()) * np.sqrt(252)

def _max_drawdown(equity: pd.Series):
    roll_max = equity.cummax()
    dd = (equity/roll_max) - 1.0
    return dd.min()
```


==================================================


## [2/3] Repository: FinRobot (`WHEEL_FinRobot`)
- **Full Name**: `FinRobot`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models
[![Downloads](https://static.pepy.tech/badge/finrobot)](https://pepy.tech/project/finrobot)
[![Downloads](https://static.pepy.tech/badge/finrobot/week)](https://pepy.tech/project/finrobot)
[![Join Discord](https://img.shields.io/badge/Discord-Join-blue)](https://discord.gg/trsr8SXpW5)
[![Python 3.8](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PyPI](https://img.shields.io/pypi/v/finrobot.svg)](https://pypi.org/project/finrobot/)
![License](https://img.shields.io/github/license/AI4Finance-Foundation/finrobot.svg?color=brightgreen)
![](https://img.shields.io/github/issues-raw/AI4Finance-Foundation/finrobot?label=Issues)
![](https://img.shields.io/github/issues-closed-raw/AI4Finance-Foundation/finrobot?label=Closed+Issues)
![](https://img.shields.io/github/issues-pr-raw/AI4Finance-Foundation/finrobot?label=Open+PRs)
![](https://img.shields.io/github/issues-pr-closed-raw/AI4Finance-Foundation/finrobot?label=Closed+PRs)
[![FinRobot Desktop](https://img.shields.io/badge/Desktop-v0.1.0-blue)](https://github.com/AI4Finance-Foundation/FinRobot/releases/tag/desktop-v0.1.0)

<div align="center">
<img align="center" src=figs/logo_white_background.jpg width="40%"/>
</div>

**FinRobot** is an AI Agent platform tailored for financial applications, surpassing FinGPT's single-model approach. It unifies multiple AI technologies—including LLMs, reinforcement learning, and quantitative analytics—to power investment research automation, algorithmic trading strategies, and risk assessment, delivering a full-stack intelligent solution for the financial industry.

**Concept of AI Agent**: an AI Agent is an intelligent entity that uses large language models as its brain to perceive its environment, make decisions, and execute actions. Unlike traditional artificial intelligence, AI Agents possess the ability to independently think and utilize tools to progressively achieve given objectives.

[Whitepaper on arXiv](https://arxiv.org/abs/2405.14767)  
[Official Academic Page](https://ai4finance.org/research/finrobot-open-source-ai-agent.html)

![Visitors](https://api.visitorbadge.io/api/VisitorHit?user=AI4Finance-Foundation&repo=FinRobot&countColor=%23B17A)
[![Discord](https://dcbadge.limes.pink/api/server/trsr8SXpW5?v=20260320)](https://discord.gg/trsr8SXpW5)

## 🚀 FinRobot Desktop v0.1.0 Released

We are excited to announce the first public release of **FinRobot Desktop v0.1.0** — a native desktop equity research cockpit powered by a production-grade multi-agent architecture.

FinRobot Desktop brings AI-native financial research workflows into a macOS application, helping analysts move from market data and company filings to valuation, debate, synthesis, and investment committee-style reports in one traceable workflow.

👉 **Latest Release:** [FinRobot Desktop v0.1.0](https://github.com/AI4Finance-Foundation/FinRobot/releases/tag/desktop-v0.1.0)

For macOS Apple Silicon users, download:

```text id="5vbf1p"
FinRobot_0.1.0_aarch64.dmg
```

Then drag **FinRobot** into the **Applications** folder.

### System Requirement

FinRobot Desktop currently supports **Apple Silicon Macs** — M1, M2, M3, or later. Intel Mac builds are not available in this release.

### Installation Note for macOS

FinRobot Desktop is not yet Apple-notarized. On first launch, macOS may report that the downloaded app is “damaged.” Run the following command once in Terminal, then open the app normally:

```bash id="yql6j7"
xattr -cr /Applications/FinRobot.app
```

### What’s New in FinRobot Desktop

FinRobot Desktop v0.1.0 introduces a full-stack desktop research system built on **PydanticAI + FastAPI + React/Tauri**. It combines role-based financial agents, deterministic valuation engines, live data providers, and analyst-style report generation inside a native desktop experience.

Key capabilities include:

- **Multi-agent equity research** with orchestrated research, modeling, synthesis, reporting, and debate agents.
- **Code-calculated valuation** for DCF, DDM, LBO, comps, WACC, and Monte Carlo analysis.
- **Traceable analyst reports** with 13-chapter research output, IC memos, evidence links, and numeric provenance.
- **Native desktop workflow** with live market data, SEC filing support, automatic failover, and GitHub-based auto-updates.

### Multi-Agent Architecture

FinRobot is a multi-agent equity research platform where a **Lead Agent** orchestrates specialized research agents through a pipeline-driven execution engine.

The system includes:

- **1 Lead Agent** for orchestration and task routing
- **5 role-based sub-agents** for data, analysis, modeling, synthesis, and report generation
- **3 debate agents** for bull case, bear case, and judge-style investment reasoning

This design separates complex financial research into modular agent roles while keeping the full workflow auditable and extensible.

```text id="whmuv4"
User Research Request
        ↓
Lead Agent / Orchestrator
        ↓
Data Agent → Analysis Agent → Modeling Agent → Synthesis Agent → Report Agent
        ↓
Bull Agent ↔ Bear Agent → Judge Agent
        ↓
Traceable Investment Research Output
```

### Deterministic Compute, LLM Narration

A core design principle of FinRobot is the strict separation between **deterministic financial computation** and **LLM-based narration**.

All financial numbers are generated by pure-Python compute operators, not by the language model. The LLM is used for reasoning, synthesis, explanation, and report writing, while valuation outputs such as DCF, DDM, LBO, WACC, comparable-company analysis, and Monte Carlo simulations are calculated through deterministic code paths with full provenance.

In short:

```text id="2l0biq"
Numbers are code-calculated.
Narratives are LLM-assisted.
Every output is provenance-tracked.
```
### Codebase Snapshot

| Layer | What It Includes |
|---|---|
| **Full-stack system** | ~184k lines across Python backend, React/Tauri desktop frontend, Rust shell, and tests |
| **Agent runtime** | 9 agents: lead orchestrator, 5 role-based pipeline agents, and 3 debate agents |
| **Research pipelines** | 7 pipelines covering company research, DCF, comps, LBO, DDM, earnings, and IC memo generation |
| **Deterministic compute** | 30 pure-Python operators and 7 coordinators for valuation, WACC, Monte Carlo, and financial modeling |
| **Data infrastructure** | 7 providers with failover, including FMP, Finnhub, yfinance, SEC EDGAR, Adanos, NewsAggregator, and FX |
| **Product stack** | PydanticAI, FastAPI, SQLite, React 19, Vite 6, Zustand, Tauri/Rust, and Recharts |


## 🎬 FinRobot Pro — Your Personal AI-Powered Equity Research Assistant
🌐 https://finrobot.ai/

<div align="center">
  <a href="https://www.youtube.com/watch?v=ebgPiJINi-k" target="_blank">
    <img src="https://github.com/user-attachments/assets/de3b9f9c-50aa-49f0-82c6-3d2b938f4670" width="90%" />
  </a>
</div>

<img width="1490" height="808" alt="image" src="https://github.com/user-attachments/assets/bf56065d-a134-4ff8-99e2-8a1e52258ce7" />


<p align="center">
  ▶️ Click the image above to watch the demo video, or see the short preview below.
</p>

A locally-deployed AI assistant that fetches financial data, runs multi-agent LLM analysis, and generates professional equity research reports.

**1. Configure API Keys**
```bash
cp finrobot_equity/core/config/config.ini.example finrobot_equity/core/config/config.ini
```
Edit `config.ini` with your keys:
```ini
[API_KEYS]
fmp_api_key = YOUR_FMP_API_KEY          # https://financialmodelingprep.com/developer
openai_api_key = YOUR_OPENAI_API_KEY    # https://platform.openai.com/account/api-keys
adanos_api_key = YOUR_ADANOS_API_KEY    # Optional: enables Retail Sentiment Insights
```

**2. One-Command Deploy (Web Interface)**
```bash
chmod +x deploy.sh
./deploy.sh start

#if deploy.sh not working then
python3 -m venv venv                                                                                                                                           
source venv/bin/activate
pip install -r requirements-equity.txt                                                                                                                         
python run_web_app.py  
```
Access at `http://127.0.0.1:8001`

| Command | Description |
|:---|:---|
| `./deploy.sh start` | Start the web app (auto-installs dependencies) |
| `./deploy.sh stop` | Stop the application |
| `./deploy.sh restart` | Restart the application |
| `./deploy.sh status` | Check running status |

**3. Or Run via Command Line**
```bash
# Step 1: Financial analysis
python finrobot_equity/core/src/generate_financial_analysis.py \
    --company-ticker NVDA \
    --company-name "NVIDIA Corporation" \
    --config-file finrobot_equity/core/config/config.ini \
    --peer-tickers AMD INTC \
    --generate-text-sections

# Step 2: Generate report
python finrobot_equity/core/src/create_equity_report.py \
    --company-ticker NVDA \
    --company-name "NVIDIA Corporation" \
    --analysis-csv output/NVDA/analysis/financial_metrics_and_forecasts.csv \
    --ratios-csv output/NVDA/analysis/ratios_raw_data.csv \
    --config-file finrobot_equity/core/config/config.ini
```

**Pipeline**:
1. **Fetch Financial Data**: income statements, balance sheets, cash flows via FMP API
2. **Process & Forecast**: 3-year financial projections, DCF valuation, peer comparison
3. **AI Agent Analysis**: 8 specialized agents generate investment thesis, risk assessment, valuation overview, etc.
4. **Report Generation**: professional multi-page HTML/PDF with 15+ chart types

### Example Reports
- [NVDA Equity Research Report](https://ai4finance-foundation.github.io/FinRobot/finrobot_equity/core/output/NVDA_Equity_Research_Report.html)
- [MSFT Equity Research Report](https://ai4finance-foundation.github.io/FinRobot/finrobot_equity/core/output/MSFT_Equity_Research_Report.html)
- [COP Equity Research Report](https://ai4finance-foundation.github.io/FinRobot/finrobot_equity/core/output/COP_Equity_Research_Report.html)
- [TSLA Equity Research Report](https://ai4finance-foundation.github.io/FinRobot/finrobot_equity/core/output/TSLA_Equity_Research_Report.html)
- [META Equity Research Report](https://ai4finance-foundation.github.io/FinRobot/finrobot_equity/core/output/META_Equity_Research_Report.html)

For full documentation, see [finrobot_equity/README.md](finrobot_equity/README.md).


## What is FinRobot Pro?


https://github.com/user-attachments/assets/93ec0f1e-e28b-4474-a0bf-a79e0c12f0ff


[FinRobot Pro](https://finrobot.ai/ ) is an AI-powered equity research platform that automates professional stock analysis using Large Language Models (LLMs) and AI Agents.

**Key Features:**

- **Automated Report Generation** – Generate professional equity research reports instantly
- **Financial Analysis** – Deep dive into income statements, balance sheets, and cash flows
- **Valuation Analysis** – P/E ratio, EV/EBITDA multiples, and peer comparison
- **Risk Assessment** – Comprehensive investment risk evaluation


## FinRobot Ecosystem
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/6b30d9c1-35e5-4d36-a138-7e2769718f62" width="90%"/>
</div>

### The overall framework of FinRobot is organized into four distinct layers, each designed to address specific aspects of financial AI processing and application:
1. **Financial AI Agents Layer**: The Financial AI Agents Layer now includes Financial Chain-of-Thought (CoT) prompting, enhancing complex analysis and decision-making capacity. Market Forecasting Agents, Document Analysis Agents, and Trading Strategies Agents utilize CoT to dissect financial challenges into logical steps, aligning their advanced algorithms and domain expertise with the evolving dynamics of financial markets for precise, actionable insights.
2. **Financial LLMs Algorithms Layer**: The Financial LLMs Algorithms Layer configures and utilizes specially tuned models tailored to specific domains and global market analysis. 
3. **LLMOps and DataOps Layers**: The LLMOps layer implements a multi-source integration strategy that selects the most suitable LLMs for specific financial tasks, utilizing a range of state-of-the-art models. 
4. **Multi-source LLM Foundation Models Layer**: This foundational layer supports the plug-and-play functionality of various general and specialized LLMs. 


## FinRobot: Agent Workflow
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/ff8033be-2326-424a-ac11-17e2c9c4983d" width="60%"/>
</div>

1. **Perception**: This module captures and interprets multimodal financial data from market feeds, news, and economic indicators, using sophisticated techniques to structure the data for thorough analysis.

2. **Brain**: Acting as the core processing unit, this module perceives data from the Perception module with LLMs and utilizes Financial Chain-of-Thought (CoT) processes to generate structured instructions.

3. **Action**: This module executes instructions from the Brain module, applying tools to translate analytical insights into actionable outcomes. Actions include trading, portfolio adjustments, generating reports, or sending alerts, thereby actively influencing the financial environment.

## FinRobot: Smart Scheduler
<div align="center">
<img align="center" src="https://github.com/AI4Finance-Foundation/FinRobot/assets/31713746/06fa0b78-ac53-48d3-8a6e-98d15386327e" width="60%"/>
</div>

The Smart Scheduler is central to ensuring model diversity and optimizing the integration and selection of the most appropriate LLM for each task.
* **Director Agent**: This component orchestrates the task assignment process, ensuring that tasks are allocated to agents based on their performance metrics and suitability for specific tasks.
* **Agent Registration**: Manages the registration and tracks the availability of agents within the system, facilitating an efficient task allocation process.
* **Agent Adaptor**: Tailor agent functionalities to specific tasks, enhancing their performance and integration within the overall system.
* **Task Manager**: Manages and stores different general and fine-tuned LLMs-based agents tailored for various financial tasks, updated periodically to ensure relevance and efficacy.

## File Structure

The main folder **finrobot** has three subfolders **agents, data_source, functional**. 

```
FinRobot
├── finrobot (main folder)
│   ├── agents
│   	├── agent_library.py
│   	└── workflow.py
│   ├── data_source
│   	├── finnhub_utils.py
│   	├── finnlp_utils.py
│   	├── fmp_utils.py
│   	├── sec_utils.py
│   	└── yfinance_utils.py
│   ├── functional
│   	├── analyzer.py
│   	├── charting.py
│   	├── coding.py
│   	├── quantitative.py
│   	├── reportlab.py
│   	└── text.py
│   ├── toolkits.py
│   └── utils.py
│
├── configs
├── experiments
├── tutorials_beginner (hands-on tutorial)
│   ├── agent_fingpt_forecaster.ipynb
│   └── agent_annual_report.ipynb 
├── tutorials_advanced (advanced tutorials for potential finrobot developers)
│   ├── agent_trade_strategist.ipynb
│   ├── agent_fingpt_forecaster.ipynb
│   ├── agent_annual_report.ipynb 
│   ├── lmm_agent_mplfinance.ipynb
│   └── lmm_agent_opt_smacross.ipynb
├── setup.py
├── OAI_CONFIG_LIST_sample
├── config_api_keys_sample
├── requirements.txt
└── README.md
```

## Installation:

**1. (Recommended) Create a new virtual environment**
```shell
conda create --name finrobot python=3.10
conda activate finrobot
```
**2. download the FinRobot repo use terminal or download it manually**
```shell
git clone https://github.com/AI4Finance-Foundation/FinRobot.git
cd FinRobot
```
**3. install finrobot & dependencies from source or pypi**

get our latest release from pypi
```bash
pip install -U finrobot
```
or install from this repo directly
```
pip install -e .
```
**4. modify OAI_CONFIG_LIST_sample file**
```shell
1) rename OAI_CONFIG_LIST_sample to OAI_CONFIG_LIST
2) remove the four lines of comment within the OAI_CONFIG_LIST file
3) add your own openai api-key <your OpenAI API key here>
```
**5. modify config_api_keys_sample file**
```shell
1) rename config_api_keys_sample to config_api_keys
2) remove the comment within the config_api_keys file
3) add your own finnhub-api "YOUR_FINNHUB_API_KEY"
4) add your own financialmodelingprep and sec-api keys "YOUR_FMP_API_KEY" and "YOUR_SEC_API_KEY" (for financial report generation)
```
**6. start navigating the tutorials or the demos below:**
```
# find these notebooks in tutorials
1) agent_annual_report.ipynb
2) agent_fingpt_forecaster.ipynb
3) agent_trade_strategist.ipynb
4) lmm_agent_mplfinance.ipynb
5) lmm_agent_opt_smacross.ipynb
```


## AI Agent Papers

+ [Stanford University + Microsoft Research] [Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568)
+ [Stanford University] [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)
+ [Fudan NLP Group] [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864)
+ [Fudan NLP Group] [LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List)
+ [Tsinghua University] [Large Language Models Empowered Agent-based Modeling and Simulation: A Survey and Perspectives](https://arxiv.org/abs/2312.11970)
+ [Renmin University] [A Survey on Large Language Model-based Autonomous Agents](https://arxiv.org/pdf/2308.11432.pdf)
+ [Nanyang Technological University] [FinAgent: A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://arxiv.org/abs/2402.18485)


## AI Agent Open-Source Frameworks & Tools
+ [AutoGPT (183k stars)](https://github.com/Significant-Gravitas/AutoGPT): autonomous AI agent platform.
+ [Dify (134k stars)](https://github.com/langgenius/dify): LLM app development platform with workflow orchestration and RAG.
+ [LangChain (130k stars)](https://github.com/langchain-ai/langchain): framework for building context-aware LLM applications.
+ [MetaGPT (65.6k stars)](https://github.com/geekan/MetaGPT): multi-agent framework with role-based collaboration.
+ [AutoGen (56k stars)](https://github.com/microsoft/autogen): framework for multi-agent LLM applications with tools and human interaction.
+ [CrewAI (46.6k stars)](https://github.com/joaomdmoura/crewAI): framework for orchestrating collaborative AI agents.
+ [ChatDev (31.7k stars)](https://github.com/OpenBMB/ChatDev): multi-agent framework for software development tasks.
+ [FastGPT (27.4k stars)](https://github.com/labring/FastGPT): knowledge-based LLM platform with workflow support.
+ [Langfuse (23.4k stars)](https://github.com/langfuse/langfuse): open-source LLM observability and evaluation platform.
+ [BabyAGI (22.2k stars)](https://github.com/yoheinakajima/babyagi): task-driven experimental autonomous agent framework.
+ [SuperAGI (17.3k stars)](https://github.com/TransformerOptimus/SuperAGI): developer-focused autonomous agent framework.
+ [CAMEL (16.4k stars)](https://github.com/camel-ai/camel): framework for cooperative and communicative AI agents.
+ [Bisheng (11.2k stars)](https://github.com/dataelement/bisheng): enterprise open-source LLM application platform.

## Citing FinRobot
```
@article{yang2024finrobot,
  title   = {FinRobot: An Open-Source AI Agent Platform for Financial Applications using Large Language Models},
  author  = {Yang, Hongyang and Zhang, Boyu and Wang, Neng and Guo, Cheng and Zhang, Xiaoli and Lin, Likun and Wang, Junlin and Zhou, Tianyu and Guan, Mao and Zhang, Runjia and Wang, Christina Dan},
  journal = {arXiv preprint arXiv:2405.14767},
  year    = {2024},
  doi     = {10.48550/arXiv.2405.14767},
  url     = {https://arxiv.org/abs/2405.14767}
}

@inproceedings{
zhou2024finrobot,
title={FinRobot: {AI} Agent for Equity Research and Valuation with Large Language Models},
author={Tianyu Zhou and Pinqiao Wang and Yilin Wu and Hongyang Yang},
booktitle={ICAIF 2024: The 1st Workshop on Large Language Models and Generative AI for Finance},
year={2024}
}


@inproceedings{han2024enhancing,
  title={Enhancing Investment Analysis: Optimizing AI-Agent Collaboration in Financial Research},
  author={Han, Xuewen and Wang, Neng and Che, Shangkun and Yang, Hongyang and Zhang, Kunpeng and Xu, Sean Xin},
  booktitle={ICAIF 2024: Proceedings of the 5th ACM International Conference on AI in Finance},
  pages={538--546},
  year={2024}
}
```
**Disclaimer**: The codes and documents provided herein are released under the Apache-2.0 license. They should not be construed as financial counsel or recommendations for live trading. It is imperative to exercise caution and consult with qualified financial professionals prior to any trading or investment actions.


<div align="center">
<img align="center" width="30%" alt="image" src="https://github.com/AI4Finance-Foundation/FinGPT/assets/31713746/e0371951-1ce1-488e-aa25-0992dafcc139">
</div>

### Core Implementation Code & Architecture
#### File: `finrobot/__init__.py`
```python

```

#### File: `finrobot/data_source/filings_src/prepline_sec_filings/__init__.py`
```python

```

#### File: `finrobot/data_source/filings_src/prepline_sec_filings/api/__init__.py`
```python

```

#### File: `finrobot/agents/__init__.py`
```python

```

#### File: `finrobot/data_source/filings_src/__init__.py`
```python
from finrobot.data_source.filings_src.secData import sec_main
```

#### File: `.vscode/settings.json`
```python
{
    "python.analysis.extraPaths": [
        "./FinNLP"
    ]
}
```


==================================================


## [3/3] Repository: Hands-On-Algorithmic-Trading-with-Python (`WHEEL_Hands-On-Algorithmic-Trading-with-Python`)
- **Full Name**: `Hands-On-Algorithmic-Trading-with-Python`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Hands-On-Algorithmic-Trading-with-Python
 Hands-On Algorithmic Trading with Python, By Packt


==================================================
