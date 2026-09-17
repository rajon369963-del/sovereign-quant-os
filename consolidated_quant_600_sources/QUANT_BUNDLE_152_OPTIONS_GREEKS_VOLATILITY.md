# ⚡ [QUANT-SOURCE-152] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_152_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: NiftyOptionTradingSystem (`WHEEL_NiftyOptionTradingSystem`)
- **Full Name**: `NiftyOptionTradingSystem`
- **Description**: NOTS - is a autonomus Program that trades into Derivate Market Of Nifty 50, uses multiple analysis, Using Dhan API
- **GitHub Stars**: 2
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# NIFTY 50 Options Trading Engine

A production-grade autonomous algorithmic options trading system for Indian markets using Dhan and AngelOne APIs.

## ⚡ Quick Start

```bash
# 1. Clone & install
git clone <repo>
cd NiftyOptionTradingSystem
uv sync

# 2. Configure credentials
cp .env.example .env
# For step-by-step instructions on obtaining API credentials, see:
# docs/BROKER_SETUP_GUIDE.md
# Edit .env with your Dhan or AngelOne credentials

# 3. Run in paper mode (default)
uv run python -m nifty_engine
# or
uv run nifty-engine
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   TradingEngine                          │
│  ┌──────────┐  ┌──────────┐  ┌────────────────────────┐│
│  │ Strategy │  │ Strategy │  │ Strategy N             ││
│  │ Runner 1 │  │ Runner 2 │  │ (plugin architecture)  ││
│  └────┬─────┘  └────┬─────┘  └────────┬───────────────┘│
│       │              │                  │                │
│  ┌────▼──────────────▼──────────────────▼─────────────┐ │
│  │            Strategy Context                        │ │
│  │   (risk-validated order placement)                 │ │
│  └────────────────────┬───────────────────────────────┘ │
│                       │                                  │
│  ┌────────────────────▼───────────────────────────────┐ │
│  │              Risk Manager                          │ │
│  │  Position Sizer │ Stop Manager │ Kill Switch       │ │
│  └────────────────────┬───────────────────────────────┘ │
│                       │                                  │
│  ┌────────────────────▼───────────────────────────────┐ │
│  │         Broker (Paper / Dhan Live)                 │ │
│  │  ┌───────────┐  ┌───────────┐  ┌────────────────┐ │ │
│  │  │ DhanBroker│  │PaperBroker│  │  Market Feed   │ │ │
│  │  └───────────┘  └───────────┘  └────────────────┘ │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

## 📦 Project Structure

```
src/nifty_engine/
├── broker/           # Broker interfaces & Dhan implementation
│   ├── base.py       # BrokerBase, MarketFeedBase ABCs
│   ├── models.py     # Pydantic data models (Order, Position, etc.)
│   ├── dhan_broker.py # Dhan API wrapper
│   ├── dhan_feed.py   # WebSocket market feed
│   └── circuit_breaker.py
├── data/             # Data layer
│   ├── database.py   # Async SQLite with migrations
│   ├── instruments.py # Dhan instrument master manager
│   └── market_data.py # Market data aggregator
├── engine/           # Core engine
│   ├── orchestrator.py # Main trading engine
│   ├── strategy_base.py # Abstract strategy class
│   └── context.py    # Strategy context (controlled access)
├── strategies/       # Trading strategies (plugin system)
│   ├── short_straddle.py    # ATM theta decay
│   ├── iron_condor.py       # Defined-risk range play
│   ├── otm_credit_spread.py # Directional credit spread
│   ├── delta_neutral.py     # Dynamic delta hedging
│   ├── gamma_scalp.py       # Long gamma scalping
│   ├── mean_reversion.py    # Z-score reversion
│   ├── trend_following.py   # EMA crossover
│   └── momentum_breakout.py # Bollinger squeeze breakout
├── risk/             # Risk management
│   ├── risk_manager.py   # 10-point pre-trade validation
│   ├── position_sizer.py # Fixed-fraction/Kelly/vol-adjusted
│   ├── stop_manager.py   # Hard/trailing/time/break-even stops
│   ├── kill_switch.py    # Emergency halt
│   └── transaction_costs.py # Indian F&O fee model
├── paper/            # Paper trading
│   ├── paper_broker.py  # Simulated broker
│   ├── fill_simulator.py # Realistic fill simulation
│   └── pnl_tracker.py  # P&L tracking & reporting
├── notifications/    # Alerts
│   └── telegram.py   # Telegram bot notifications
├── research/         # Strategy research
│   └── strategy_research.py # Metrics & backtesting
└── utils/            # Shared utilities
    ├── config.py     # Pydantic config models
    ├── greeks.py     # Black-Scholes Greeks & IV solvers
    ├── helpers.py    # IST time, holidays, async utilities
    └── logging.py    # Rich console + JSON file logging
```

## 🎯 Strategies

| Strategy | Type | Risk | Description |
|----------|------|------|-------------|
| **Short Straddle** | Premium Selling | Undefined | ATM CE+PE sell, IV rank filter, trailing stops |
| **Iron Condor** | Premium Selling | Defined | 4-leg range play with wings |
| **OTM Credit Spread** | Directional | Defined | PCR-based directional spread |
| **Delta Neutral** | Hedged | Mixed | Strangle + dynamic delta hedging |
| **Gamma Scalp** | Volatility | Defined | Long straddle + frequent rebalancing |
| **Mean Reversion** | Statistical | Defined | Z-score deviation from MA |
| **Trend Following** | Momentum | Defined | EMA crossover with options |
| **Momentum Breakout** | Breakout | Defined | Bollinger squeeze + breakout |

## 🛡️ Risk Management

- **10-point pre-trade validation**: market hours, loss limits, drawdown, positions, duplicates
- **Position sizing**: fixed-fraction, volatility-adjusted, half-Kelly criterion
- **Stop losses**: hard, trailing, time-based, break-even
- **Kill switch**: auto-triggers on daily loss, drawdown, API errors, volatility spikes
- **Transaction costs**: full Indian F&O fee model (brokerage, STT, exchange, SEBI, GST, stamp)
- **Live trading safety gate**: double-gated (config + env var `NIFTY_LIVE_TRADING_CONFIRM=YES`)

## 🔧 Configuration

All configuration via YAML files in `config/`:
- `broker.yaml` — Dhan credentials, exchange settings
- `risk.yaml` — Risk limits, stops, position sizing
- `strategies.yaml` — Strategy parameters and enable/disable
- `paper.yaml` — Paper trading simulation settings
- `notifications.yaml` — Telegram bot settings

## 📊 CLI Usage

```bash
# Paper trading (default)
uv run python -m nifty_engine

# Force paper mode
uv run python -m nifty_engine --paper

# Specific strategies only
uv run python -m nifty_engine --strategies short_straddle iron_condor

# Debug logging
uv run python -m nifty_engine --log-level DEBUG
```

## ⚠️ Disclaimer

This software is for educational and research purposes. Trading in derivatives carries significant risk. Always paper trade first. The authors are not responsible for any financial losses.

### Core Implementation Code & Architecture
#### File: `scripts/__init__.py`
```python

```

#### File: `tests/test_risk/__init__.py`
```python
"""Tests for risk management."""
```

#### File: `tests/test_strategies/__init__.py`
```python
"""Tests for trading strategies."""
```

#### File: `tests/test_data/__init__.py`
```python
"""Tests for the market data layer."""
```

#### File: `tests/test_engine/__init__.py`
```python
"""Tests for the core trading engine."""
```

#### File: `tests/test_paper/__init__.py`
```python
"""Tests for the paper trading engine."""
```


==================================================


## [2/3] Repository: OPTION-DASHBOARD (`WHEEL_OPTION-DASHBOARD`)
- **Full Name**: `OPTION-DASHBOARD`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# QuantFlow AI V5

**Institutional-grade options intelligence platform for Indian index & stock options — built entirely on the DhanHQ v2 API.**

QuantFlow AI ingests live option chains, futures, equity quotes and market depth, computes 200+ derived metrics per strike every few seconds, detects market regimes, generates graded trade signals, and scores its own accuracy afterwards — feeding the results back into its own weights. Every edge shipped in the scanner was first validated against multi-year historical studies (80k–110k stock-days), not guessed.

![All four indices live at once — spot, PCR, max pain, ATM IV, SMI and the option walls](docs/index-grid.png)

All four indices stream at once, each on its own WebSocket. A grade of `INVALID` is the honest and common case: the engine only promotes a signal to `A+`/`A`/`B+` when the evidence actually clears the thresholds, so most of a quiet session reads as no trade rather than a manufactured one.

Opening one index gives the full picture behind that verdict — every contributing term with its own signed score, so a grade can be argued with instead of taken on trust.

![The NIFTY dashboard — AI signal with per-term evidence, smart-money gauge, regime, and the strike metrics](docs/index-detail.png)

The OI profile is the map underneath it all: calls to the left, puts to the right, thickest where the market has committed the most open interest.

![Open interest by strike, clustered around max pain — CE on the left, PE on the right](docs/oi-profile.png)

The scanner applies the same treatment to roughly 210 F&O stocks, sweeping them continuously for intraday runners and next-day BTST setups.

![The F&O stock scanner — intraday runners, BTST setups and the watchlist, live during market hours](docs/stocks-scanner.png)

Each BTST card carries the evidence that produced it — the futures quadrant, the day's CE/PE OI shift, the volume multiple and the IV change — so a setup stays readable rather than arriving as a bare verdict.

![The premium day-change ranking and the full BTST rank order across all 210 scanned names](docs/stocks-btst-board.png)

---

## What it does

| Layer | Capability |
|---|---|
| **Data collection** | Option chain polling, live tick feed (WebSocket), 20/200-level market depth, market quotes, historical rolling-option candles, futures daily bars, F&O scrip master |
| **Processing** | Normalisation, validation, enrichment (moneyness, ATM, DTE, intrinsic/extrinsic), time & sales tape with whale/block detection |
| **Analytics** | OI analytics (PCR, max pain, call/put walls, buildup classification), IV surface (ATM IV, IV rank/percentile, skew, curvature), Smart Money Index (0–100), 8-state market regime detector |
| **AI / signals** | Evidence-based signal engine with A+ → INVALID grading, entry/stop/target + risk-reward, online self-learning weight manager |
| **Outcome loop** | Every signal is re-evaluated at +3m / +10m / +30m / +1h against real premium data → WIN / LOSS / BREAK-EVEN → weights adapt |
| **Stock scanner** | ~210 F&O stocks swept continuously: options OI/IV/flow + futures quadrant + equity tape, producing ranked intraday and BTST (buy-today-sell-tomorrow) candidates |
| **Research** | Backtest engine, event studies, event forensics, daily-movers ranking studies, and an append-only live-snapshot dataset for continuous threshold optimisation |
| **Frontend** | React + TypeScript dashboard — live index grid, runners board, BTST signal cards, OI profile, regime/SMI panels, streaming over WebSocket |

---

## Architecture

```
DhanHQ v2 APIs
      │
      ▼
data_collection/  ──►  processing/  ──►  analytics/  ──►  ai/
 (7 API clients,        (normalise,      (OI, IV, SMI,     (signal engine,
  WS feeds, scrip        validate,        regime, 200+      model manager,
  master, futures)       enrich)          metrics)          outcome evaluator)
                                                │
                        ┌───────────────────────┴──────────────────────┐
                        ▼                                              ▼
              TimescaleDB (history)                         Redis (hot cache + pub/sub)
                                                                       │
                                                          FastAPI REST + /ws/dashboard
                                                                       │
                                                       React + Vite + Tailwind + Recharts
```

**Backend:** Python 3.12 · FastAPI · asyncio · SQLAlchemy 2 (async) · asyncpg · Redis · structlog
**Storage:** PostgreSQL + TimescaleDB hypertables (dev: SQLite) · Redis cache & pub/sub
**Frontend:** React 18 · TypeScript (strict) · Vite · Tailwind v4 · Recharts
**Data source:** DhanHQ v2 only — Option Chain, Expiry List, Live Feed WS, Market Quote, 20-Level Depth, 200-Level Depth, Historical Expired Options

---

## The research behind the signals

The scanner does not fire on intuition. Each signal was mined and cross-validated across two independent measurement frames (threshold-based *and* next-day ranking-based) over 80,000–110,000 stock-days of options + futures + equity history. Only patterns that held up in **both** frames were shipped.

Representative validated edges:

- **MEGA BULL** — futures volume 3×, long buildup, and call OI ≥15% aligned → **6.8× lift** on being a next-day top gap-up
- **FUT LEADS BEAR** — futures basis crash with a falling stock → **4.6× lift** on next-day gap-down (highest bearish lift found)
- **Triple bull / triple bear** stacks — consistent 3–4× across both frames
- **Put-crowd fade** — put-heavy option flow precedes gap-*ups*, not downs

Equally valuable are the **disproven** theories baked in as vetoes: quiet-range accumulation predicts nothing (disproven six separate ways), 20-day-high closes suppress next-day follow-through, and up-streaks signal exhaustion. Signals also carry veto logic so a bullish setup is suppressed when the futures basis is overheated.

Every fired signal is later graded against what actually happened, and the live snapshot table (per-strike OI/IV/greeks/bid-ask captured every sweep — data historical APIs simply do not retain) feeds a weekly forensics job that re-tunes provisional thresholds.

---

## Getting started

### Prerequisites
- Python 3.12+, Node 18+
- PostgreSQL 16+ with the TimescaleDB extension (Docker Compose file included)
- Redis 7+
- A DhanHQ trading account with API access

### Setup

```bash
git clone <your-repo-url>
cd quantflow_v5

python -m venv .venv && .venv\Scripts\activate     # Windows
pip install -r requirements.txt

cp .env.example .env        # then fill in your DhanHQ + DB credentials

docker compose up -d        # Postgres/TimescaleDB + Redis
alembic upgrade head

uvicorn backend.main:app --port 8000
```

```bash
cd frontend
npm install
npm run dev                 # http://localhost:5173
```

On Windows, `START_SYSTEM.bat` launches services, backend and frontend in one click — and kills any stale backend first (running two instances at once makes them revoke each other's API tokens).

### Configuration

All settings live in `.env` — see `.env.example` for the full list. Authentication is fully automated via TOTP; the token manager verifies the stored token server-side on startup and regenerates only when it has actually been revoked.

---

## Repository layout

```
backend/
  auth/              DhanHQ TOTP auth + token lifecycle
  data_collection/   7 API clients, WS feeds, scrip master, scanner, futures
  processing/        normaliser, validator, enricher, tick compressor
  analytics/         OI, IV, smart money, regime, metrics engine, pipeline
  ai/                signal engine, model manager, outcome evaluator
  api/               REST routes + dashboard WebSocket
  database/          models, migrations, TimescaleDB, Redis cache
  backtest/          BTST, event studies, forensics
frontend/src/
  pages/             IndexPage, StocksPage
  components/        panels, charts, signal cards, scanner board
  lib/               API client, WS hooks, formatting, types
tests/unit/          400+ tests
run_*.py             research, download and daily-update scripts
```

### Useful scripts

| Script | Purpose |
|---|---|
| `run_daily_update.py` | One-command daily top-up: indices, stocks, futures, equity |
| `run_download_stocks.py` | Full F&O universe historical download (resumable) |
| `run_event_forensics.py` | D-1 clue → D outcome lift tables |
| `run_deep_clues.py` | 64-pattern sweep across both measurement frames |
| `run_snapshot_forensics.py` | Re-tune live-clue thresholds from stored snapshots |
| `run_btst_analysis.py` | Overnight-gap BTST validation |

---

## Testing

```bash
pytest                          # 400+ unit tests
cd frontend && npm run build    # strict tsc + vite build
```

Tests run entirely offline — no live API calls, no lifespan startup — using stub caches, stub DB readers and synthetic fixtures.

---

## Notes & limitations

- **Single instance only.** DhanHQ invalidates the previous access token whenever a new one is generated, so two backends running concurrently will revoke each other's tokens.
- Token generation is rate-limited to once every two minutes.
- Real-time quote endpoints only serve data during market hours (09:15–15:30 IST); use the historical endpoints outside them.
- TimescaleDB compression requires the licensed edition; migrations skip it gracefully on the Apache build.
- IV rank/percentile need a 52-week IV history bootstrap that is not yet automated.
- Signal base rates for rare events are small (2–3%), so even a 4× lift means roughly a 10% event probability. These are **watchlist filters, not certainties.**

---

## Disclaimer

This project is for research and educational purposes. It is not investment advice. Options trading carries substantial risk of loss. Backtested and historical results do not guarantee future performance. Use at your own risk.

---

## Licence

[MIT](LICENSE) © 2026 Tej Gohel

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/unit/__init__.py`
```python

```

#### File: `tests/integration/__init__.py`
```python

```

#### File: `backend/__init__.py`
```python

```

#### File: `backend/database/migrations/__init__.py`
```python

```

#### File: `backend/database/migrations/versions/__init__.py`
```python

```


==================================================


## [3/3] Repository: ai-algorithmic-trading-bot (`WHEEL_ai-algorithmic-trading-bot`)
- **Full Name**: `ai-algorithmic-trading-bot`
- **Description**: AI-assisted intraday NSE options trading bot using Python, Angel One SmartAPI, Claude, Telegram alerts, and backtesting tools.
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# AI Algorithmic Trading Bot

AI-assisted intraday NSE options trading system built with Python, broker integration, technical indicators, live alerts, and backtesting support.

This project is designed as an end-to-end automation workflow for Nifty and BankNifty options trading. It combines Angel One SmartAPI for market access, Anthropic Claude for decision support, Telegram for real-time notifications, and custom strategy logic for signal generation, risk checks, and trade tracking.

This repository is intentionally sanitized for GitHub. Real API keys, broker credentials, logs, tokens, and local trade outputs are excluded.

## Project Overview

This project demonstrates:

- AI-assisted trade decisions using Claude
- Technical indicator computation with Pandas and NumPy
- Intraday options workflow for Nifty and BankNifty
- Automated trade logging and position-state recovery
- Backtesting support using historical candle data
- Telegram notifications for monitoring and alerts

## Features

- Symmetric trading logic for both call and put entries
- Technical indicators including EMA, RSI, ADX, ATR, PDI, and NDI
- Paper trading mode for safer testing
- Live trade execution flow through Angel One SmartAPI
- Separate BankNifty variant for lower-capital execution
- Backtest script to evaluate performance on historical data
- Test script to validate configuration, APIs, and core logic

## Tech Stack

- Python
- Pandas
- NumPy
- Anthropic Claude API
- Angel One SmartAPI
- Telegram Bot API
- PyOTP

## Project Structure

```text
.
|-- backtest.py
|-- banknifty_final.py
|-- config.example.py
|-- final.py
|-- requirements.txt
|-- test_bot.py
`-- assets/
    `-- screenshots/
```

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies.
4. Copy `config.example.py` to `config.py`.
5. Fill in your own broker, Claude, and Telegram credentials.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item config.example.py config.py
```

## How To Run

Run logic checks without live API calls:

```powershell
python test_bot.py --no-api
```

Run the full validation flow:

```powershell
python test_bot.py
```

Run the Nifty bot in paper trading mode first:

```powershell
python final.py
```

Run the BankNifty version:

```powershell
python banknifty_final.py
```

Run the historical backtest:

```powershell
python backtest.py
```

## Screenshots

### Paper Trading Console

![Paper trading console](assets/screenshots/paper-trading-console.png)

Live terminal monitoring during paper trading, showing periodic Nifty LTP updates, trade count, running P&L, and the next evaluation cycle.

### Telegram Alerts

![Telegram alerts](assets/screenshots/telegram-alerts-current.svg)

Telegram notifications used for bot startup confirmation and real-time alert delivery during execution.

## Safety Notes

- Keep `PAPER_TRADING = True` until you finish testing
- Never commit `config.py`, `.env`, logs, or generated trade files
- Regenerate any credentials that were previously stored in plain text
- Review broker-side order behavior manually before enabling live execution

## Future Improvements

- Move configuration loading to environment variables or `.env`
- Add unit tests for signal generation and risk checks
- Split strategy, broker, and notification logic into modules
- Add structured logging and a metrics dashboard
- Add Docker support and deployment documentation

## Author

**Krishna Daryani**

- B.Tech Artificial Intelligence & Data Science student
- Python developer focused on AI automation and trading systems
- GitHub: [KR1SHNA464](https://github.com/KR1SHNA464)

### Core Implementation Code & Architecture
#### File: `config.example.py`
```python
# ================================================================
#   CONFIG TEMPLATE
#   Copy this file to config.py and replace the placeholders.
#   Never commit your real config.py to GitHub.
# ================================================================

# Angel One SmartAPI
ANGEL_API_KEY = "PASTE_ANGEL_API_KEY"
ANGEL_CLIENT_ID = "PASTE_ANGEL_CLIENT_ID"
ANGEL_PIN = "PASTE_ANGEL_PIN"
ANGEL_TOTP_SECRET = "PASTE_ANGEL_TOTP_SECRET"

# Anthropic Claude API
CLAUDE_API_KEY = "PASTE_CLAUDE_API_KEY"

# Telegram bot
TELEGRAM_BOT_TOKEN = "PASTE_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "PASTE_TELEGRAM_CHAT_ID"

# Risk and capital settings
CAPITAL = 10000
MAX_DAILY_LOSS = 1000
CONFIDENCE_MIN = 65
```

#### File: `test_bot.py`
```python
# ================================================================
#   TEST_BOT.PY — Safe testing script
#   Tests ALL components WITHOUT placing any real orders
#   Run this BEFORE going live to verify everything works
# ================================================================

import json, re, datetime, sys
import anthropic

# ── Test results tracker ─────────────────────────────────────────
results = []

def test(name, fn):
    print(f"\n{'─'*50}")
    print(f"TEST: {name}")
    print(f"{'─'*50}")
    try:
        passed, detail = fn()
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"Result: {status}")
        print(f"Detail: {detail}")
        results.append((name, passed, detail))
        return passed
    except Exception as e:
        print(f"Result: ❌ ERROR")
        print(f"Detail: {e}")
        results.append((name, False, str(e)))
        return False


# ================================================================
#   TEST 1 — Config file loads correctly
# ================================================================
def test_config():
    from config import (
        ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET,
        CLAUDE_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID,
        CONFIDENCE_MIN, MAX_DAILY_LOSS, CAPITAL
    )
    issues = []
    if "PASTE" in str(ANGEL_API_KEY):      issues.append("ANGEL_API_KEY not set")
    if "PASTE" in str(ANGEL_CLIENT_ID):    issues.append("ANGEL_CLIENT_ID not set")
    if "PASTE" in str(ANGEL_PIN):          issues.append("ANGEL_PIN not set")
    if "PASTE" in str(ANGEL_TOTP_SECRET):  issues.append("ANGEL_TOTP_SECRET not set")
    if "PASTE" in str(CLAUDE_API_KEY):     issues.append("CLAUDE_API_KEY not set")

    if issues:
        return False, f"Fill in config.py: {', '.join(issues)}"

    print(f"  Client ID: {ANGEL_CLIENT_ID}")
    print(f"  Capital:   Rs.{CAPITAL}")
    print(f"  Daily SL:  Rs.{MAX_DAILY_LOSS}")
    print(f"  Min Conf:  {CONFIDENCE_MIN}%")
    return True, "All config values filled"


# ================================================================
#   TEST 2 — Angel One login
# ================================================================
def test_angel_login():
    import pyotp
    from SmartApi import SmartConnect
    from config import ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET

    totp = pyotp.TOTP(ANGEL_TOTP_SECRET).now()
    print(f"  TOTP generated: {totp}")

    obj  = SmartConnect(api_key=ANGEL_API_KEY)
    data = obj.generateSession(ANGEL_CLIENT_ID, ANGEL_PIN, totp)

    if data["status"]:
        return True, f"Logged in as {ANGEL_CLIENT_ID}"
    return False, f"Login failed: {data.get('message','unknown error')}"


# ================================================================
#   TEST 3 — Get Nifty live price
# ================================================================
def test_live_price():
    import pyotp
    from SmartApi import SmartConnect
    from config import ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET

    totp = pyotp.TOTP(ANGEL_TOTP_SECRET).now()
    obj  = SmartConnect(api_key=ANGEL_API_KEY)
    obj.generateSession(ANGEL_CLIENT_ID, ANGEL_PIN, totp)

    q = obj.ltpData("NSE", "Nifty 50", "99926000")
    if q["status"] and q.get("data"):
        price = float(q["data"]["ltp"])
        print(f"  Nifty LTP: Rs.{price}")
        if 15000 < price < 35000:
            return True, f"Live price: Rs.{price}"
        return False, f"Price looks wrong: Rs.{price}"
    return False, f"LTP call failed: {q}"


# ================================================================
#   TEST 4 — Get candle data + indicators
# ================================================================
def test_market_data():
    import pyotp, pandas as pd, numpy as np
    from SmartApi import SmartConnect
    from config import ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET

    totp = pyotp.TOTP(ANGEL_TOTP_SECRET).now()
    obj  = SmartConnect(api_key=ANGEL_API_KEY)
    obj.generateSession(ANGEL_CLIENT_ID, ANGEL_PIN, totp)

    now   = datetime.datetime.now()
    start = (now-datetime.timedelta(hours=7)).strftime("%Y-%m-%d %H:%M")
    end   = now.strftime("%Y-%m-%d %H:%M")

    hist    = obj.getCandleData({
        "exchange":"NSE","symboltoken":"99926000",
        "interval":"FIVE_MINUTE","fromdate":start,"todate":end
    })
    candles = hist.get("data", [])

    if not candles:
        # Outside market hours — use mock data for testing
        print("  Market closed — testing with mock data")
        mock = {
            "price": 22500.0,
            "ema9": 22510.0, "ema21": 22490.0, "ema_gap": 20.0,
            "rsi": 62.5, "adx": 22.0, "pdi": 28.0, "ndi": 18.0,
            "atr": 35.0, "day_high": 22600.0, "day_low": 22350.0,
            "day_range": 250.0
        }
        print(f"  Mock data: {mock}")
        return True, "Market closed — mock data OK for testing Claude"

    df = pd.DataFrame(candles, columns=["datetime","open","high","low","close","volume"])
    for c in ["open","high","low","close","volume"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna()

    df["ema9"]  = df["close"].ewm(span=9, adjust=False).mean()
    df["ema21"] = df["close"].ewm(span=21, adjust=False).mean()
    lt = df.iloc[-1]
    gap = round(float(lt["ema9"]-lt["ema21"]), 2)

    print(f"  Candles fetched: {len(df)}")
    print(f"  EMA9:  {round(float(lt['ema9']),2)}")
    print(f"  EMA21: {round(float(lt['ema21']),2)}")
    print(f"  Gap:   {gap}")
    return True, f"{len(df)} candles fetched, indicators computed"


# ================================================================
#   TEST 5 — Claude API responds correctly
# ================================================================
def test_claude_brain():
    from config import CLAUDE_API_KEY

    SYSTEM_PROMPT = """You are the decision brain for an intraday Nifty 50 options trading system.
Return ONLY this JSON:
{
  "action": "BUY_CE" or "BUY_PE" or "HOLD",
  "confidence": 0-100,
  "reason": "one sentence",
  "market_state": "TRENDING_UP" or "TRENDING_DOWN" or "SIDEWAYS",
  "risk_flag": "LOW" or "MEDIUM" or "HIGH"
}"""

    # Test 3 scenarios
    test_cases = [
        {
            "name": "Strong uptrend",
            "msg": "Time:10:30 Nifty:22500 EMA9:22520 EMA21:22490 Gap:30pts RSI:65 ADX:25 PDI:28 NDI:18 ATR:35 Range:200pts High:22550 Low:22350 P&L:0 Trades:0/2 Capital:10000",
            "expected": "BUY_CE"
        },
        {
            "name": "Strong downtrend",
            "msg": "Time:10:30 Nifty:22200 EMA9:22180 EMA21:22220 Gap:-40pts RSI:35 ADX:28 PDI:15 NDI:30 ATR:40 Range:220pts High:22350 Low:22180 P&L:0 Trades:0/2 Capital:10000",
            "expected": "BUY_PE"
        },
        {
            "name": "Sideways/neutral",
            "msg": "Time:10:30 Nifty:22400 EMA9:22402 EMA21:22399 Gap:3pts RSI:50 ADX:12 PDI:20 NDI:19 ATR:20 Range:80pts High:22440 Low:22360 P&L:0 Trades:0/2 Capital:10000",
            "expected": "HOLD"
        }
    ]

    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
    all_ok = True
    details = []

    for tc in test_cases:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=250,
            system=SYSTEM_PROMPT,
            messages=[{"role":"user","content":tc["msg"]}]
        )
        raw   = response.content[0].text.strip()
        match = re.search(r'\{[^{}]*\}', raw, re.DOTALL)
        dec   = json.loads(match.group() if match else raw)

        ok  = dec["action"] == tc["expected"]
        sym = "✅" if ok else "⚠️"
        print(f"  {sym} [{tc['name']}] → {dec['action']} "
              f"(expected:{tc['expected']}) Conf:{dec['confidence']}%")
        print(f"     Reason: {dec['reason']}")

        if not ok:
            all_ok = False
        details.append(f"{tc['name']}:{dec['action']}")

    return all_ok, " | ".join(details)


# ================================================================
#   TEST 6 — Telegram notification
# ================================================================
def test_telegram():
    import urllib.request
    from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

    if "PASTE" in str(TELEGRAM_BOT_TOKEN):
        return False, "TELEGRAM_BOT_TOKEN not set in config.py"

    url  = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    msg  = ("🤖 TEST MESSAGE\n"
            "Nifty AI Bot test successful!\n"
            f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}\n"
            "This is a test — no real trade placed.")
    data = json.dumps({"chat_id":str(TELEGRAM_CHAT_ID),"text":msg}).encode("utf-8")
    req  = urllib.request.Request(url, data=data,
           headers={"Content-Type":"application/json"})
    resp = urllib.request.urlopen(req, timeout=5)
    body = json.loads(resp.read())

    if body.get("ok"):
        return True, "Message sent — check your Telegram!"
    return False, f"Failed: {body}"


# ================================================================
#   TEST 7 — Pre-check logic (no API needed)
# ================================================================
def test_precheck_logic():
    EMA_GAP_MIN = 5; ADX_MIN = 15; RSI_BLOCK_HIGH = 80; RSI_BLOCK_LOW = 18

    def check(d):
        blocks = []
        if abs(d["ema_gap"]) < EMA_GAP_MIN: blocks.append("gap")
        if d["adx"] < ADX_MIN:              blocks.append("adx")
        if 49 <= d["rsi"] <= 51:             blocks.append("neutral")
        if d["rsi"] > RSI_BLOCK_HIGH:        blocks.append("overbought")
        if d["rsi"] < RSI_BLOCK_LOW:         blocks.append("oversold")
        if d["day_range"] > 400:             blocks.append("extreme")
        return len(blocks) == 0, blocks

    cases = [
        ({"ema_gap":25, "adx":22, "rsi":65, "day_range":180}, True,  "BUY_CE scenario"),
        ({"ema_gap":-30,"adx":26, "rsi":35, "day_range":200}, True,  "BUY_PE scenario"),
        ({"ema_gap":3,  "adx":22, "rsi":60, "day_range":150}, False, "Gap too small"),
        ({"ema_gap":20, "adx":10, "rsi":60, "day_range":150}, False, "ADX too low"),
        ({"ema_gap":20, "adx":22, "rsi":50, "day_range":150}, False, "RSI neutral"),
        ({"ema_gap":20, "adx":22, "rsi":85, "day_range":150}, False, "RSI extreme OB"),
        ({"ema_gap":20, "adx":22, "rsi":15, "day_range":150}, False, "RSI extreme OS"),
    ]

    all_ok = True
    for d, expected, label in cases:
        ok, blocks = check(d)
        sym = "✅" if ok==expected else "❌"
        print(f"  {sym} {label}: pass={ok} {blocks if blocks else ''}")
        if ok != expected:
            all_ok = False

    return all_ok, "All pre-check scenarios correct" if all_ok else "Some pre-check logic wrong"


# ================================================================
#   TEST 8 — Risk check logic (no API needed)
# ================================================================
def test_risk_logic():
    def risk_ok(dec, daily_pnl=0, trades_today=0, open_position=None,
                max_daily_loss=2000, max_trades=2):
        now = datetime.datetime(2025, 5, 15, 10, 30)  # fixed test time
        for failed, msg in [
            (daily_pnl <= -max_daily_loss, "Daily SL hit"),
            (dec["confidence"] < 65, "Conf too low"),
            (dec.get("risk_flag")=="HIGH", "HIGH risk"),
            (open_position is not None, "Position open"),
            (trades_today >= max_trades, "Max trades done"),
        ]:
            if failed: return False, msg
        return True, "OK"

    cases = [
        ({"confidence":75,"risk_flag":"LOW"}, 0,    0, None,  True,  "Normal BUY_CE"),
        ({"confidence":75,"risk_flag":"LOW"}, -2500,0, None,  False, "Daily SL hit"),
        ({"confidence":50,"risk_flag":"LOW"}, 0,    0, None,  False, "Low confidence"),
        ({"confidence":75,"risk_flag":"HIGH"},0,    0, None,  False, "HIGH risk"),
        ({"confidence":75,"risk_flag":"LOW"}, 0,    0, "open",False, "Position open"),
        ({"confidence":75,"risk_flag":"LOW"}, 0,    2, None,  False, "Max trades"),
    ]

    all_ok = True
    for dec, pnl, trades, pos, expected, label in cases:
        ok, msg = risk_ok(dec, pnl, trades, pos)
        sym = "✅" if (ok==expected) else "❌"
        print(f"  {sym} {label}: ok={ok} ({msg})")
        if ok != expected:
            all_ok = False

    return all_ok, "All risk checks correct" if all_ok else "Risk logic has issues"


# ================================================================
#   MAIN
# ================================================================
if __name__ == "__main__":
    print("\n" + "="*54)
    print("   NIFTY AI BOT — FULL TEST SUITE")
    print(f"   {datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')}")
    print("="*54)

    # Always run these (no API needed)
    test("Pre-check logic",        test_precheck_logic)
    test("Risk check logic",       test_risk_logic)
    test("Config file",            test_config)

    # These need internet/API
    if "--no-api" not in sys.argv:
        test("Angel One Login",    test_angel_login)
        test("Nifty Live Price",   test_live_price)
        test("Market Data + Indicators", test_market_data)
        test("Claude Brain",       test_claude_brain)
        test("Telegram Notify",    test_telegram)

    # ── Summary ─────────────────────────────────────────────────
    print("\n" + "="*54)
    print("   TEST SUMMARY")
    print("="*54)
    passed = sum(1 for _, p, _ in results if p)
    total  = len(results)
    for name, p, detail in results:
        sym = "✅" if p else "❌"
        print(f"  {sym} {name}")

    print(f"\n  {passed}/{total} tests passed")

    if passed == total:
        print("\n  🟢 ALL TESTS PASSED — Bot is ready!")
        print("  Set PAPER_TRADING=True in final.py and run:")
        print("  python final.py")
    elif passed >= total - 1:
        print("\n  🟡 ALMOST READY — Check failed tests above")
    else:
        print("\n  🔴 ISSUES FOUND — Fix before running bot")
    print("="*54 + "\n")
```

#### File: `backtest.py`
```python
# ================================================================
#   BACKTEST.PY — 3 Month Historical Backtest
#   Uses REAL Angel One candle data (no TradingView needed)
#   Tests your exact CE/PE logic on past data
#   Shows: Win rate, P&L, trade-by-trade breakdown
# ================================================================

import json, re, datetime, time, pyotp, os
import pandas as pd
import numpy as np
from SmartApi import SmartConnect
from config import (
    ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET,
    CAPITAL, MAX_DAILY_LOSS
)

# ================================================================
#   BACKTEST SETTINGS — change these to test different periods
# ================================================================
BACKTEST_DAYS       = 365        # How many days back to test (90 = 3 months)
TIMEFRAME           = "FIVE_MINUTE"   # 5-min candles (same as live bot)
CONFIDENCE_MIN      = 65        # Same as live bot
ADX_MIN             = 15
EMA_GAP_MIN         = 5
RSI_CE_MIN, RSI_CE_MAX = 52, 75
RSI_PE_MIN, RSI_PE_MAX = 25, 48
RSI_BLOCK_HIGH      = 80
RSI_BLOCK_LOW       = 18
MAX_TRADES_PER_DAY  = 2
NO_TRADE_BEFORE_H   = 9
NO_TRADE_BEFORE_M   = 45
NO_TRADE_AFTER_H    = 13
NO_TRADE_AFTER_M    = 30
SL_MULTIPLIER       = 0.7       # ATR × 0.7 = stop loss
TGT_MULTIPLIER      = 1.4      # ATR × 1.4 = target
LOT_PNL_PER_PT      = 0.5 * 65 # Rs. per Nifty point (approx)

# ================================================================
#   LOGIN
# ================================================================
def login():
    print("[LOGIN] Connecting to Angel One...")
    totp = pyotp.TOTP(ANGEL_TOTP_SECRET).now()
    obj  = SmartConnect(api_key=ANGEL_API_KEY)
    data = obj.generateSession(ANGEL_CLIENT_ID, ANGEL_PIN, totp)
    if data["status"]:
        print(f"       ✅ Connected: {ANGEL_CLIENT_ID}")
        return obj
    raise Exception(f"Login failed: {data['message']}")


# ================================================================
#   FETCH HISTORICAL CANDLES — Angel One allows max 60 days per call
#   So we fetch in chunks for 3 months
# ================================================================
def fetch_all_candles(angel, days=90):
    print(f"\n[DATA] Fetching {days} days of 5-min Nifty candles...")
    all_candles = []
    end_date    = datetime.datetime.now()
    chunk_days  = 55  # Angel One limit per request

    chunks = []
    temp_end = end_date
    while True:
        temp_start = temp_end - datetime.timedelta(days=chunk_days)
        total_fetched = (end_date - temp_end).days + chunk_days
        chunks.append((temp_start, temp_end))
        if total_fetched >= days:
            break
        temp_end = temp_start - datetime.timedelta(minutes=5)

    chunks.reverse()

    for i, (start, end) in enumerate(chunks):
        try:
            print(f"       Chunk {i+1}/{len(chunks)}: "
                  f"{start.strftime('%d-%b-%Y')} → {end.strftime('%d-%b-%Y')}")
            hist = angel.getCandleData({
                "exchange":    "NSE",
                "symboltoken": "99926000",
                "interval":    TIMEFRAME,
                "fromdate":    start.strftime("%Y-%m-%d %H:%M"),
                "todate":      end.strftime("%Y-%m-%d %H:%M"),
            })
            candles = hist.get("data", [])
            if candles:
                all_candles.extend(candles)
                print(f"       Got {len(candles)} candles")
            time.sleep(0.5)  # avoid rate limit
        except Exception as e:
            print(f"       ⚠️  Chunk error: {e}")
            time.sleep(2)

    if not all_candles:
        raise Exception("No candle data fetched!")

    df = pd.DataFrame(all_candles,
         columns=["datetime","open","high","low","close","volume"])
    for c in ["open","high","low","close","volume"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.dropna().drop_duplicates("datetime").sort_values("datetime")
    df = df.reset_index(drop=True)

    print(f"\n       ✅ Total candles: {len(df)}")
    print(f"       From: {df['datetime'].iloc[0].strftime('%d-%b-%Y')}")
    print(f"       To:   {df['datetime'].iloc[-1].strftime('%d-%b-%Y')}")
    return df


# ================================================================
#   COMPUTE INDICATORS on full dataframe
# ================================================================
def compute_indicators(df):
    print("\n[INDICATORS] Computing EMA, RSI, ADX, ATR...")

    df["ema9"]  = df["close"].ewm(span=9,  adjust=False).mean()
    df["ema21"] = df["close"].ewm(span=21, adjust=False).mean()
    df["ema_gap"] = df["ema9"] - df["ema21"]

    # RSI
    d = df["close"].diff()
    g = d.clip(lower=0).rolling(14, min_periods=2).mean()
    l = (-d.clip(upper=0)).rolling(14, min_periods=2).mean()
    df["rsi"] = (100 - (100 / (1 + g / l.replace(0, np.nan)))).fillna(50)

    # ATR
    tr = pd.concat([
        df["high"] - df["low"],
        (df["high"] - df["close"].shift()).abs(),
        (df["low"]  - df["close"].shift()).abs()
    ], axis=1).max(axis=1)
    df["atr"] = tr.rolling(14, min_periods=3).mean().fillna(30)

    # ADX / PDI / NDI
    up  = df["high"] - df["high"].shift()
    dn  = df["low"].shift() - df["low"]
    pdm = np.where((up > dn) & (up > 0), up, 0.0)
    ndm = np.where((dn > up) & (dn > 0), dn, 0.0)
    pdi = 100 * pd.Series(pdm, index=df.index).rolling(14, min_periods=3).mean() / df["atr"]
    ndi = 100 * pd.Series(ndm, index=df.index).rolling(14, min_periods=3).mean() / df["atr"]
    dx  = 100 * (pdi - ndi).abs() / (pdi + ndi).replace(0, np.nan)
    df["adx"] = dx.rolling(14, min_periods=3).mean().fillna(10)
    df["pdi"] = pdi.fillna(0)
    df["ndi"] = ndi.fillna(0)

    print("       ✅ All indicators ready")
    return df


# ================================================================
#   PRE-CHECK — same logic as live bot
# ================================================================
def pre_check_ok(row):
    gap = row["ema_gap"]
    rsi = row["rsi"]
    adx = row["adx"]
    if abs(gap) < EMA_GAP_MIN:   return False, "gap_small"
    if adx < ADX_MIN:             return False, "adx_low"
    if 49 <= rsi <= 51:           return False, "rsi_neutral"
    if rsi > RSI_BLOCK_HIGH:      return False, "rsi_extreme_high"
    if rsi < RSI_BLOCK_LOW:       return False, "rsi_extreme_low"
    return True, "OK"


# ================================================================
#   SIGNAL LOGIC — same as Claude would decide (deterministic)
# ================================================================
def get_signal(row):
    gap = row["ema_gap"]
    rsi = row["rsi"]
    adx = row["adx"]

    ok, reason = pre_check_ok(row)
    if not ok:
        return "HOLD", reason

    # BUY_CE: uptrend
    if (gap > EMA_GAP_MIN and
        RSI_CE_MIN <= rsi <= RSI_CE_MAX and
        adx >= ADX_MIN):
        return "BUY_CE", "uptrend confirmed"

    # BUY_PE: downtrend
    if (gap < -EMA_GAP_MIN and
        RSI_PE_MIN <= rsi <= RSI_PE_MAX and
        adx >= ADX_MIN):
        return "BUY_PE", "downtrend confirmed"

    return "HOLD", "no clear trend"


# ================================================================
#   RUN BACKTEST — day by day simulation
# ================================================================
def run_backtest(df):
    print("\n[BACKTEST] Running simulation...\n")

    trades     = []
    daily_stats= []

    # Group by date
    df["date"] = df["datetime"].dt.date
    dates = sorted(df["date"].unique())
    trading_days = [d for d in dates if datetime.date(d.year, d.month, d.day).weekday() < 5]

    for day in trading_days:
        day_df      = df[df["date"] == day].copy().reset_index(drop=True)
        day_pnl     = 0.0
        trades_today= 0
        open_pos    = None   # dict with entry info

        for i, row in day_df.iterrows():
            t = row["datetime"]

            # Only trade in allowed window
            in_window = (
                (t.hour > NO_TRADE_BEFORE_H or
                 (t.hour == NO_TRADE_BEFORE_H and t.minute >= NO_TRADE_BEFORE_M))
                and
                (t.hour < NO_TRADE_AFTER_H or
                 (t.hour == NO_TRADE_AFTER_H and t.minute <= NO_TRADE_AFTER_M))
            )

            # ── Check open position for SL/Target ──────────────
            if open_pos:
                price = row["close"]
                ot    = open_pos["type"]
                sl    = open_pos["sl"]
                tgt   = open_pos["tgt"]
                exit_reason = None

                # Force close at 3 PM
                if t.hour >= 15:
                    exit_reason = "TIME_EXIT"
                    exit_price  = price

                elif ot == "CE":
                    if price <= sl:
                        exit_reason = "SL_HIT"
                        exit_price  = sl
                    elif price >= tgt:
                        exit_reason = "TARGET_HIT"
                        exit_price  = tgt

                else:  # PE
                    if price >= sl:
                        exit_reason = "SL_HIT"
                        exit_price  = sl
                    elif price <= tgt:
                        exit_reason = "TARGET_HIT"
                        exit_price  = tgt

                if exit_reason:
                    entry = open_pos["entry"]
                    pts   = (exit_price - entry) if ot == "CE" else (entry - exit_price)
                    pnl   = round(pts * LOT_PNL_PER_PT, 2)
                    day_pnl += pnl

                    trades.append({
                        "date":        str(day),
                        "entry_time":  open_pos["entry_time"].strftime("%H:%M"),
                        "exit_time":   t.strftime("%H:%M"),
                        "type":        f"BUY_{ot}",
                        "entry_price": entry,
                        "exit_price":  exit_price,
                        "sl":          sl,
                        "tgt":         tgt,
                        "exit_reason": exit_reason,
                        "pts":         round(pts, 2),
                        "pnl":         pnl,
                        "result":      "WIN" if pnl > 0 else "LOSS",
                    })
                    open_pos = None
                    continue

            # ── Look for new entry ───────────────────────────────
            if (open_pos is None and
                in_window and
                trades_today < MAX_TRADES_PER_DAY and
                day_pnl > -MAX_DAILY_LOSS):

                signal, reason = get_signal(row)

                if signal != "HOLD":
                    atr     = row["atr"]
                    price   = row["close"]
                    sl_pts  = round(atr * SL_MULTIPLIER, 1)
                    tgt_pts = round(atr * TGT_MULTIPLIER, 1)
                    ot      = "CE" if signal == "BUY_CE" else "PE"
                    sl      = round(price - sl_pts, 2) if ot == "CE" else round(price + sl_pts, 2)
                    tgt     = round(price + tgt_pts, 2) if ot == "CE" else round(price - tgt_pts, 2)

                    open_pos = {
                        "type":       ot,
                        "entry":      price,
                        "entry_time": t,
                        "sl":         sl,
                        "tgt":        tgt,
                        "reason":     reason,
                    }
                    trades_today += 1

        # ── Force close any open position at end of day ──────────
        if open_pos and len(day_df) > 0:
            last       = day_df.iloc[-1]
            exit_price = last["close"]
            entry      = open_pos["entry"]
            ot         = open_pos["type"]
            pts        = (exit_price - entry) if ot == "CE" else (entry - exit_price)
            pnl        = round(pts * LOT_PNL_PER_PT, 2)
            day_pnl   += pnl
            trades.append({
                "date":        str(day),
                "entry_time":  open_pos["entry_time"].strftime("%H:%M"),
                "exit_time":   "15:29",
                "type":        f"BUY_{ot}",
                "entry_price": entry,
                "exit_price":  exit_price,
                "sl":          open_pos["sl"],
                "tgt":         open_pos["tgt"],
                "exit_reason": "EOD_CLOSE",
                "pts":         round(pts, 2),
                "pnl":         pnl,
                "result":      "WIN" if pnl > 0 else "LOSS",
            })

        daily_stats.append({
            "date":         str(day),
            "trades":       trades_today,
            "day_pnl":      round(day_pnl, 2),
            "result":       "PROFIT" if day_pnl > 0 else "LOSS" if day_pnl < 0 else "BREAKEVEN",
        })

    return trades, daily_stats


# ================================================================
#   PRINT RESULTS
# ================================================================
def print_results(trades, daily_stats):
    print("\n" + "="*60)
    print("   📊 BACKTEST RESULTS — TRADE BY TRADE")
    print("="*60)

    if not trades:
        print("   No trades generated!")
        return

    trade_df = pd.DataFrame(trades)
    daily_df = pd.DataFrame(daily_stats)

    # ── Trade-by-trade ───────────────────────────────────────────
    print(f"\n{'Date':<12} {'Time':<6} {'Type':<8} {'Entry':>8} "
          f"{'Exit':>8} {'Pts':>7} {'P&L':>10} {'Result':<10} {'Reason'}")
    print("─"*90)

    for _, t in trade_df.iterrows():
        sym = "✅" if t["result"] == "WIN" else "❌"
        sign = "+" if t["pnl"] >= 0 else ""
        print(f"{t['date']:<12} {t['entry_time']:<6} {t['type']:<8} "
              f"{t['entry_price']:>8.1f} {t['exit_price']:>8.1f} "
              f"{t['pts']:>+7.1f} {sign}Rs.{t['pnl']:>7.0f}  "
              f"{sym} {t['result']:<8} {t['exit_reason']}")

    # ── Daily Summary ────────────────────────────────────────────
    print(f"\n\n{'='*60}")
    print("   📅 DAILY SUMMARY")
    print("="*60)
    print(f"\n{'Date':<12} {'Trades':>7} {'Day P&L':>12} {'Result'}")
    print("─"*45)

    running_total = 0
    for _, d in daily_df[daily_df["trades"] > 0].iterrows():
        running_total += d["day_pnl"]
        sym  = "🟢" if d["day_pnl"] > 0 else "🔴" if d["day_pnl"] < 0 else "⚪"
        sign = "+" if d["day_pnl"] >= 0 else ""
        print(f"{d['date']:<12} {d['trades']:>7}  "
              f"{sign}Rs.{d['day_pnl']:>7.0f}  {sym} {d['result']}")

    # ── Overall Stats ────────────────────────────────────────────
    wins   = trade_df[trade_df["result"] == "WIN"]
    losses = trade_df[trade_df["result"] == "LOSS"]
    total  = len(trade_df)
    total_pnl    = round(trade_df["pnl"].sum(), 2)
    win_rate     = round(len(wins) / total * 100, 1) if total > 0 else 0
    avg_win      = round(wins["pnl"].mean(), 2) if len(wins) > 0 else 0
    avg_loss     = round(losses["pnl"].mean(), 2) if len(losses) > 0 else 0
    max_win      
# ... [TRUNCATED FILE CONTENT]
```

#### File: `final.py`
```python
# ================================================================
#   NIFTY AI ALGO — FINAL v4.0
#   SYMMETRIC: treats UP and DOWN moves exactly the same way
#   Big drop  → BUY_PE (RSI low = strong down = valid signal)
#   Big rise  → BUY_CE (RSI high = strong up = valid signal)
#   Option lookup via instrument master (no more searchScrip fail)
# ================================================================

import json, re, time, datetime, os, pyotp, urllib.request
import pickle, threading, requests
import pandas as pd
import numpy as np
import anthropic
from SmartApi import SmartConnect
from config import (
    ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET,
    CLAUDE_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID,
    CONFIDENCE_MIN, MAX_DAILY_LOSS, CAPITAL
)

# ================================================================
#   SETTINGS
# ================================================================
PAPER_TRADING        = True          # ← SET TO FALSE FOR LIVE TRADING

MAX_TRADES_PER_DAY   = 2
NO_TRADE_BEFORE      = "09:45"
NO_TRADE_AFTER       = "13:30"
EXIT_CHECK_INTERVAL  = 2
LOG_FILE             = "trades.csv"
STATE_FILE           = "position_state.pkl"
CONFIDENCE_MIN_ENTRY = 65
ADX_MIN              = 15
EMA_GAP_MIN          = 5
DAY_RANGE_MAX        = 400           # only block truly extreme days

# ── SYMMETRIC RSI RULES ──────────────────────────────────────────
RSI_CE_MIN    = 52
RSI_CE_MAX    = 75
RSI_PE_MIN    = 25
RSI_PE_MAX    = 48
RSI_BLOCK_HIGH= 80
RSI_BLOCK_LOW = 18

INSTRUMENT_DF = None

# ================================================================
#   SYSTEM PROMPT — SYMMETRIC BOTH DIRECTIONS
# ================================================================
SYSTEM_PROMPT = """You are the decision brain for an intraday Nifty 50 options trading system.

CORE RULE: Treat UP moves and DOWN moves EXACTLY the same way.
A strong downtrend with low RSI is just as valid as a strong uptrend with high RSI.

ENTRY RULES (symmetric):
BUY_CE: EMA9 > EMA21 AND RSI 52-75 AND ADX > 15 AND EMA gap > 5pts
BUY_PE: EMA9 < EMA21 AND RSI 25-48 AND ADX > 15 AND EMA gap > 5pts (gap is negative)

IMPORTANT FOR PE:
- RSI of 25-35 during a downtrend is VALID — it means strong selling momentum
- Do NOT block PE just because RSI is low — low RSI in downtrend = strong signal
- EMA9 below EMA21 with widening gap = confirmed downtrend

IMPORTANT FOR CE:
- RSI of 65-75 during an uptrend is VALID — it means strong buying momentum
- EMA9 above EMA21 with widening gap = confirmed uptrend

HOLD WHEN (apply equally to both directions):
- RSI exactly 49-51 (pure neutral — no momentum either way)
- ADX below 15 (no trend at all)
- EMA gap less than 5 points (trend not confirmed)
- Before 9:45 AM or after 13:30
- RSI above 80 or below 18 (extreme exhaustion — trend may reverse)
- Confidence below 65
- Risk flag HIGH

Return ONLY this JSON:
{
  "action": "BUY_CE" or "BUY_PE" or "HOLD",
  "confidence": 0-100,
  "reason": "one sentence",
  "market_state": "TRENDING_UP" or "TRENDING_DOWN" or "SIDEWAYS",
  "risk_flag": "LOW" or "MEDIUM" or "HIGH"
}"""

# ================================================================
#   SHARED STATE
# ================================================================
open_position = None
daily_pnl     = 0.0
trades_today  = 0
angel         = None
exit_lock     = threading.Lock()


# ================================================================
#   TELEGRAM
# ================================================================
def send_telegram(msg):
    if not TELEGRAM_BOT_TOKEN or "PASTE" in str(TELEGRAM_BOT_TOKEN):
        print(f"   [TELEGRAM SKIPPED — not configured]\n   MSG: {msg}")
        return
    try:
        url  = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = json.dumps({"chat_id": str(TELEGRAM_CHAT_ID),
                           "text": msg}).encode("utf-8")
        req  = urllib.request.Request(url, data=data,
               headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=5)
        print("     ✅ Telegram sent")
    except Exception as e:
        print(f"     ❌ Telegram error: {e}")


# ================================================================
#   POSITION STATE
# ================================================================
def save_pos(pos):
    with open(STATE_FILE, "wb") as f: pickle.dump(pos, f)

def load_pos():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "rb") as f: return pickle.load(f)
    return None

def clear_pos():
    if os.path.exists(STATE_FILE): os.remove(STATE_FILE)


# ================================================================
#   LOGIN
# ================================================================
def login_angel():
    global angel
    print("\n[LOGIN] Connecting to Angel One...")
    try:
        totp = pyotp.TOTP(ANGEL_TOTP_SECRET).now()
        obj  = SmartConnect(api_key=ANGEL_API_KEY)
        data = obj.generateSession(ANGEL_CLIENT_ID, ANGEL_PIN, totp)
        if data["status"]:
            angel = obj
            print(f"       ✅ Connected: {ANGEL_CLIENT_ID}")
            return obj
        print(f"       ❌ FAILED: {data['message']}")
        return None
    except Exception as e:
        print(f"       ❌ ERROR: {e}")
        return None


# ================================================================
#   LOAD INSTRUMENT MASTER
# ================================================================
def load_instrument_master():
    global INSTRUMENT_DF
    print("\n[INSTRUMENTS] Loading NFO master list...")
    try:
        url  = ("https://margincalculator.angelbroking.com"
                "/OpenAPI_File/files/OpenAPIScripMaster.json")
        resp = requests.get(url, timeout=20)
        data = resp.json()
        df   = pd.DataFrame(data)

        opts = df[
            (df["exch_seg"] == "NFO") &
            (df["name"]     == "NIFTY") &
            (df["instrumenttype"] == "OPTIDX")
        ].copy()

        opts["strike"] = pd.to_numeric(opts["strike"], errors="coerce") / 100
        opts["expiry"] = pd.to_datetime(opts["expiry"], format="%d%b%Y", errors="coerce")

        INSTRUMENT_DF = opts
        print(f"       ✅ Loaded {len(opts)} Nifty options")
        return True
    except Exception as e:
        print(f"       ❌ Master load failed: {e}")
        INSTRUMENT_DF = None
        return False


# ================================================================
#   OPTION LOOKUP
# ================================================================
def find_best_option(nifty_price, opt_type):
    global INSTRUMENT_DF

    max_prem = round((CAPITAL / 65) * 0.85, 0)
    atm      = round(nifty_price / 50) * 50
    print(f"     Finding {opt_type} | ATM:{atm} | Max Rs.{max_prem}/unit")

    today    = datetime.date.today()
    days     = (1 - today.weekday()) % 7
    if days == 0: days = 7
    exp_date = today + datetime.timedelta(days=days)

    strikes = ([atm, atm+50, atm+100, atm+150, atm+200]
               if opt_type == "CE"
               else [atm, atm-50, atm-100, atm-150, atm-200])

    # Method 1: instrument master
    if INSTRUMENT_DF is not None:
        for weeks in [0, 1]:
            chk_exp = exp_date + datetime.timedelta(days=weeks*7)
            filt    = INSTRUMENT_DF[
                (INSTRUMENT_DF["expiry"].dt.date == chk_exp) &
                (INSTRUMENT_DF["symbol"].str.endswith(opt_type))
            ]
            for strike in strikes:
                row = filt[filt["strike"] == strike]
                if len(row) == 0: continue
                r   = row.iloc[0]
                sym = r["symbol"]
                tok = str(r["token"])
                try:
                    q = angel.ltpData("NFO", sym, tok)
                    if not q["status"] or not q.get("data"): continue
                    prem = float(q["data"]["ltp"])
                    cost = round(prem*65, 0)
                    print(f"     {sym}: Rs.{prem} | Rs.{cost} total")
                    if 0.5 < prem <= max_prem:
                        print(f"     ✅ SELECTED: {sym}")
                        return sym, tok, strike, prem
                except: continue

    # Method 2: fallback symbol formats
    print("     Trying fallback formats...")
    mm = {1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN",
          7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
    m  = mm[exp_date.month]
    y  = exp_date.strftime("%y")

    for strike in strikes:
        s = int(strike)
        for fmt in [
            f"NIFTY{exp_date.day}{m}{y}{s}{opt_type}",
            f"NIFTY{exp_date.strftime('%d')}{m}{y}{s}{opt_type}",
            f"NIFTY{exp_date.strftime('%d%b%y').upper()}{s}{opt_type}",
        ]:
            try:
                res = angel.searchScrip("NFO", fmt)
                dl  = (res.get("data") or []) if res and res.get("status") else []
                if not dl: continue
                tok = dl[0]["symboltoken"]
                sym = dl[0]["tradingsymbol"]
                q   = angel.ltpData("NFO", sym, tok)
                if not q["status"] or not q.get("data"): continue
                prem = float(q["data"]["ltp"])
                cost = round(prem*65, 0)
                print(f"     {sym}: Rs.{prem} | Rs.{cost} total")
                if 0.5 < prem <= max_prem:
                    print(f"     ✅ SELECTED (fallback): {sym}")
                    return sym, tok, strike, prem
            except: continue

    print(f"     ❌ No option found within budget")
    return None, None, atm, None


# ================================================================
#   GET LIVE LTP
# ================================================================
def get_ltp():
    try:
        q = angel.ltpData("NSE", "Nifty 50", "99926000")
        return float(q["data"]["ltp"])
    except:
        return None


# ================================================================
#   EXECUTE EXIT
# ================================================================
def execute_exit(exit_price, exit_reason):
    global open_position, daily_pnl

    with exit_lock:
        if open_position is None: return

        pos   = open_position
        ot    = "CE" if pos["type"]=="BUY_CE" else "PE"
        entry = pos["entry_nifty"]
        pts   = (exit_price-entry) if ot=="CE" else (entry-exit_price)
        pnl   = round(pts*0.5*65, 2)
        daily_pnl += pnl
        sign  = "+" if pnl>=0 else ""
        res   = "WIN ✅" if pnl>=0 else "LOSS ❌"
        ts    = datetime.datetime.now().strftime("%H:%M:%S")

        print(f"\n{'='*54}")
        print(f"  EXIT [{exit_reason}] @ {ts}")
        print(f"  {pos['type']} {pos.get('strike','')} | "
              f"Entry:Rs.{entry} Exit:Rs.{exit_price}")
        print(f"  P&L:{sign}Rs.{pnl} | Day:Rs.{round(daily_pnl,2)} | {res}")
        print(f"{'='*54}\n")

        if (not PAPER_TRADING and pos.get("symbol")
                and pos.get("token") and pos.get("order_id")):
            try:
                angel.placeOrder({
                    "variety":"NORMAL",
                    "tradingsymbol":pos["symbol"],
                    "symboltoken":pos["token"],
                    "transactiontype":"SELL",
                    "exchange":"NFO","ordertype":"MARKET",
                    "producttype":"INTRADAY","duration":"DAY",
                    "quantity":"65",
                })
                print("  ✅ SELL placed OK")
            except Exception as e:
                print(f"  ❌ SELL error:{e}")
                send_telegram(f"⚠️ SELL FAILED — SQUARE OFF MANUALLY\n{e}")

        label = ("🎯 TARGET HIT" if "TARGET" in exit_reason
                 else "🛑 STOP LOSS" if "SL" in exit_reason else "🚪 EXIT")
        send_telegram(
            f"{label}\nType:{pos['type']}\nStrike:{pos.get('strike','?')}\n"
            f"Entry:Rs.{entry} Exit:Rs.{exit_price}\n"
            f"P&L:{sign}Rs.{pnl}\nDay P&L:Rs.{round(daily_pnl,2)}"
        )

        hdr = not os.path.exists(LOG_FILE)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            if hdr:
                f.write("date,time,type,strike,entry,exit,reason,pnl,result,conf\n")
            f.write(f"{datetime.datetime.now().strftime('%d-%m-%Y')},"
                    f"{ts},{pos['type']},{pos.get('strike','?')},"
                    f"{entry},{exit_price},{exit_reason},"
                    f"{pnl},{res},{pos.get('confidence',0)}\n")

        open_position = None
        clear_pos()


# ================================================================
#   EXIT MONITOR — instant SL/Target check every 2 seconds
# ================================================================
def exit_monitor():
    print("     ✅ Exit monitor running (2s)")
    while True:
        try:
            now = datetime.datetime.now()
            if now.weekday() >= 5:
                time.sleep(60); continue
            mo = now.replace(hour=9,  minute=15, second=0)
            mc = now.replace(hour=15, minute=30, second=0)
            if not (mo <= now <= mc):
                time.sleep(30); continue
            if open_position is None:
                time.sleep(EXIT_CHECK_INTERVAL); continue

            ltp = get_ltp()
            if ltp is None:
                time.sleep(EXIT_CHECK_INTERVAL); continue

            pos = open_position
            ot  = "CE" if pos["type"]=="BUY_CE" else "PE"
            sl  = pos["sl_nifty"]
            tgt = pos["tgt_nifty"]

            if now.hour >= 15:
                execute_exit(ltp, "TIME EXIT 3PM")
            elif ot == "CE":
                if ltp <= sl:    execute_exit(sl,  "SL HIT")
                elif ltp >= tgt: execute_exit(tgt, "TARGET HIT")
            else:
                if ltp >= sl:    execute_exit(sl,  "SL HIT")
                elif ltp <= tgt: execute_exit(tgt, "TARGET HIT")

            time.sleep(EXIT_CHECK_INTERVAL)
        except Exception as e:
            print(f"     ❌ Monitor error: {e}")
            time.sleep(EXIT_CHECK_INTERVAL)


# ================================================================
#   GET MARKET DATA + INDICATORS
# ================================================================
def get_market_data():
    print(f"\n[DATA] {datetime.datetime.now().strftime('%H:%M:%S')}")
    try:
        price = get_ltp()
        if not price: return None
        print(f"       Nifty LTP: Rs.{price}")

        now   = datetime.datetime.now()
        start = (now-datetime.timedelta(hours=7)).strftime("%Y-%m-%d %H:%M")
        end   = now.strftime("%Y-%m-%d %H:%M")

        hist    = angel.getCandleData({
            "exchange":"NSE","symboltoken":"99926000",
            "interval":"FIVE_MINUTE","fromdate":start,"todate":end
        })
        candles = hist["data"]
        if not candles or len(candles) < 5: return None

        df = pd.DataFrame(candles,
             columns=["datetime","open","high","low","close","volume"])
        for c in ["open","high","low","close","volume"]:
            df[c] = pd.to_nu
# ... [TRUNCATED FILE CONTENT]
```

#### File: `banknifty_final.py`
```python
# ================================================================
#   BANKNIFTY AI ALGO — v1.0
#   Switched from Nifty → BankNifty (fits Rs.2,948 capital)
#   Lot size: 15 units (vs Nifty's 65-75)
#   SYMMETRIC: CE and PE treated equally
#   Claude AI Brain for decisions
# ================================================================

import json, re, time, datetime, os, pyotp, urllib.request
import pickle, threading, requests
import pandas as pd
import numpy as np
import anthropic
from SmartApi import SmartConnect
from config import (
    ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET,
    CLAUDE_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID,
    CONFIDENCE_MIN, MAX_DAILY_LOSS, CAPITAL
)

# ================================================================
#   SETTINGS — BankNifty Specific
# ================================================================
PAPER_TRADING        = True         # ← SET False FOR LIVE TRADING

# ── BankNifty Details ───────────────────────────────────────────
LOT_SIZE             = 15            # BankNifty lot = 15 units
STRIKE_GAP           = 100           # BankNifty strikes in 100pt gaps
INDEX_NAME           = "Bank Nifty"
INDEX_TOKEN          = "99926009"    # Angel One token for BankNifty
INDEX_EXCHANGE       = "NSE"
OPTION_NAME          = "BANKNIFTY"   # Used in symbol lookup
INSTRUMENT_NAME      = "BANKNIFTY"   # In master list

MAX_TRADES_PER_DAY   = 2
NO_TRADE_BEFORE      = "09:45"
NO_TRADE_AFTER       = "13:30"
EXIT_CHECK_INTERVAL  = 2
LOG_FILE             = "banknifty_trades.csv"
STATE_FILE           = "banknifty_state.pkl"
CONFIDENCE_MIN_ENTRY = 65
ADX_MIN              = 15
EMA_GAP_MIN          = 10           # BankNifty moves more — gap min 10pts
DAY_RANGE_MAX        = 1500         # BankNifty daily range can be 500-800pts
RSI_BLOCK_HIGH       = 80
RSI_BLOCK_LOW        = 18
RSI_CE_MIN           = 52
RSI_CE_MAX           = 75
RSI_PE_MIN           = 25
RSI_PE_MAX           = 48

INSTRUMENT_DF        = None

# ================================================================
#   SYSTEM PROMPT — BankNifty specific
# ================================================================
SYSTEM_PROMPT = """You are the decision brain for an intraday BankNifty options trading system.

BankNifty is MORE volatile than Nifty — moves of 200-500pts in a day are normal.

CORE RULE: Treat UP moves and DOWN moves EXACTLY the same way.

ENTRY RULES (symmetric):
BUY_CE: EMA9 > EMA21 AND RSI 52-75 AND ADX > 15 AND EMA gap > 10pts
BUY_PE: EMA9 < EMA21 AND RSI 25-48 AND ADX > 15 AND EMA gap < -10pts

IMPORTANT:
- BankNifty ATR of 80-150pts is NORMAL — don't be scared by big moves
- Strong RSI (65-75) in uptrend = valid BUY_CE
- Weak RSI (25-35) in downtrend = valid BUY_PE
- ADX above 20 = very strong trend — prefer these setups

HOLD WHEN:
- RSI 49-51 (pure neutral)
- ADX below 15 (no trend)
- EMA gap less than 10 points
- RSI above 80 or below 18 (exhaustion)
- Before 9:45 AM or after 13:30
- Confidence below 65
- Risk flag HIGH

Return ONLY this JSON:
{
  "action": "BUY_CE" or "BUY_PE" or "HOLD",
  "confidence": 0-100,
  "reason": "one sentence",
  "market_state": "TRENDING_UP" or "TRENDING_DOWN" or "SIDEWAYS",
  "risk_flag": "LOW" or "MEDIUM" or "HIGH"
}"""

# ================================================================
#   SHARED STATE
# ================================================================
open_position = None
daily_pnl     = 0.0
trades_today  = 0
angel         = None
exit_lock     = threading.Lock()


# ================================================================
#   TELEGRAM
# ================================================================
def send_telegram(msg):
    if not TELEGRAM_BOT_TOKEN or "PASTE" in str(TELEGRAM_BOT_TOKEN):
        print(f"   [TELEGRAM SKIPPED]\n   MSG: {msg}")
        return
    try:
        url  = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = json.dumps({"chat_id": str(TELEGRAM_CHAT_ID),
                           "text": msg}).encode("utf-8")
        req  = urllib.request.Request(url, data=data,
               headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=5)
        print("     ✅ Telegram sent")
    except Exception as e:
        print(f"     ❌ Telegram error: {e}")


# ================================================================
#   POSITION STATE
# ================================================================
def save_pos(pos):
    with open(STATE_FILE, "wb") as f: pickle.dump(pos, f)

def load_pos():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "rb") as f: return pickle.load(f)
    return None

def clear_pos():
    if os.path.exists(STATE_FILE): os.remove(STATE_FILE)


# ================================================================
#   LOGIN
# ================================================================
def login_angel():
    global angel
    print("\n[LOGIN] Connecting to Angel One...")
    try:
        totp = pyotp.TOTP(ANGEL_TOTP_SECRET).now()
        obj  = SmartConnect(api_key=ANGEL_API_KEY)
        data = obj.generateSession(ANGEL_CLIENT_ID, ANGEL_PIN, totp)
        if data["status"]:
            angel = obj
            print(f"       ✅ Connected: {ANGEL_CLIENT_ID}")
            return obj
        print(f"       ❌ FAILED: {data['message']}")
        return None
    except Exception as e:
        print(f"       ❌ ERROR: {e}")
        return None


# ================================================================
#   LOAD INSTRUMENT MASTER — BankNifty options
# ================================================================
def load_instrument_master():
    global INSTRUMENT_DF
    print("\n[INSTRUMENTS] Loading NFO master list for BankNifty...")
    try:
        url  = ("https://margincalculator.angelbroking.com"
                "/OpenAPI_File/files/OpenAPIScripMaster.json")
        resp = requests.get(url, timeout=20)
        data = resp.json()
        df   = pd.DataFrame(data)

        # Filter for BankNifty options only
        opts = df[
            (df["exch_seg"] == "NFO") &
            (df["name"]     == INSTRUMENT_NAME) &
            (df["instrumenttype"] == "OPTIDX")
        ].copy()

        opts["strike"] = pd.to_numeric(
            opts["strike"], errors="coerce") / 100
        opts["expiry"] = pd.to_datetime(
            opts["expiry"], format="%d%b%Y", errors="coerce")

        INSTRUMENT_DF = opts
        print(f"       ✅ Loaded {len(opts)} BankNifty options")
        return True
    except Exception as e:
        print(f"       ❌ Master load failed: {e}")
        INSTRUMENT_DF = None
        return False


# ================================================================
#   OPTION LOOKUP — BankNifty specific
# ================================================================
def find_best_option(bnf_price, opt_type):
    global INSTRUMENT_DF

    # Budget calculation for Rs.2,948 capital
    max_prem = round((CAPITAL / LOT_SIZE) * 0.85, 0)
    atm      = round(bnf_price / STRIKE_GAP) * STRIKE_GAP

    print(f"     Finding {opt_type} | ATM:{atm} | "
          f"Max Rs.{max_prem}/unit | Budget:Rs.{round(max_prem*LOT_SIZE,0)}")

    # BankNifty strikes to check
    strikes = ([atm, atm+100, atm+200, atm+300, atm+400,
                atm+500, atm+600, atm+700]
               if opt_type == "CE"
               else [atm, atm-100, atm-200, atm-300, atm-400,
                     atm-500, atm-600, atm-700])

    today    = datetime.date.today()
    # Find next Wednesday (BankNifty expires on Wednesday)
    days_to_wed = (2 - today.weekday()) % 7
    if days_to_wed == 0: days_to_wed = 7
    exp_date = today + datetime.timedelta(days=days_to_wed)

    # Method 1: instrument master
    if INSTRUMENT_DF is not None:
        for weeks in [0, 1, 2]:
            chk_exp = exp_date + datetime.timedelta(days=weeks*7)
            filt    = INSTRUMENT_DF[
                (INSTRUMENT_DF["expiry"].dt.date == chk_exp) &
                (INSTRUMENT_DF["symbol"].str.endswith(opt_type))
            ]
            for strike in strikes:
                row = filt[filt["strike"] == strike]
                if len(row) == 0: continue
                r   = row.iloc[0]
                sym = r["symbol"]
                tok = str(r["token"])
                try:
                    q = angel.ltpData("NFO", sym, tok)
                    if not q["status"] or not q.get("data"): continue
                    prem = float(q["data"]["ltp"])
                    cost = round(prem * LOT_SIZE, 0)
                    print(f"     {sym}: Rs.{prem}/unit | Rs.{cost} total")
                    if 0.5 < prem <= max_prem:
                        print(f"     ✅ SELECTED: {sym}")
                        return sym, tok, strike, prem
                except: continue

    # Method 2: fallback symbol formats
    print("     Trying fallback formats...")
    mm = {1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN",
          7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
    m  = mm[exp_date.month]
    y  = exp_date.strftime("%y")

    for strike in strikes:
        s = int(strike)
        for fmt in [
            f"BANKNIFTY{exp_date.day}{m}{y}{s}{opt_type}",
            f"BANKNIFTY{exp_date.strftime('%d')}{m}{y}{s}{opt_type}",
            f"BANKNIFTY{exp_date.strftime('%d%b%y').upper()}{s}{opt_type}",
        ]:
            try:
                res = angel.searchScrip("NFO", fmt)
                dl  = (res.get("data") or []) if res and res.get("status") else []
                if not dl: continue
                tok  = dl[0]["symboltoken"]
                sym  = dl[0]["tradingsymbol"]
                q    = angel.ltpData("NFO", sym, tok)
                if not q["status"] or not q.get("data"): continue
                prem = float(q["data"]["ltp"])
                cost = round(prem * LOT_SIZE, 0)
                print(f"     {sym}: Rs.{prem}/unit | Rs.{cost} total")
                if 0.5 < prem <= max_prem:
                    print(f"     ✅ SELECTED (fallback): {sym}")
                    return sym, tok, strike, prem
            except: continue

    print(f"     ❌ No option found within budget Rs.{round(max_prem*LOT_SIZE,0)}")
    return None, None, atm, None


# ================================================================
#   GET LIVE LTP — BankNifty
# ================================================================
def get_ltp():
    try:
        q = angel.ltpData(INDEX_EXCHANGE, INDEX_NAME, INDEX_TOKEN)
        return float(q["data"]["ltp"])
    except:
        return None


# ================================================================
#   EXECUTE EXIT
# ================================================================
def execute_exit(exit_price, exit_reason):
    global open_position, daily_pnl

    with exit_lock:
        if open_position is None: return

        pos   = open_position
        ot    = "CE" if pos["type"]=="BUY_CE" else "PE"
        entry = pos["entry_price"]
        pts   = (exit_price-entry) if ot=="CE" else (entry-exit_price)
        pnl   = round(pts * 0.5 * LOT_SIZE, 2)
        daily_pnl += pnl
        sign  = "+" if pnl>=0 else ""
        res   = "WIN ✅" if pnl>=0 else "LOSS ❌"
        ts    = datetime.datetime.now().strftime("%H:%M:%S")

        print(f"\n{'='*54}")
        print(f"  EXIT [{exit_reason}] @ {ts}")
        print(f"  {pos['type']} {pos.get('strike','')} | "
              f"Entry:Rs.{entry} Exit:Rs.{exit_price}")
        print(f"  P&L:{sign}Rs.{pnl} | Day:Rs.{round(daily_pnl,2)} | {res}")
        print(f"{'='*54}\n")

        if (not PAPER_TRADING and pos.get("symbol")
                and pos.get("token") and pos.get("order_id")):
            try:
                angel.placeOrder({
                    "variety":        "NORMAL",
                    "tradingsymbol":  pos["symbol"],
                    "symboltoken":    pos["token"],
                    "transactiontype":"SELL",
                    "exchange":       "NFO",
                    "ordertype":      "MARKET",
                    "producttype":    "INTRADAY",
                    "duration":       "DAY",
                    "quantity":       str(LOT_SIZE),
                })
                print("  ✅ SELL placed OK")
            except Exception as e:
                print(f"  ❌ SELL error: {e}")
                send_telegram(f"⚠️ SELL FAILED — SQUARE OFF MANUALLY\n{e}")

        label = ("🎯 TARGET HIT" if "TARGET" in exit_reason
                 else "🛑 STOP LOSS" if "SL" in exit_reason else "🚪 EXIT")
        send_telegram(
            f"{label} — BankNifty\n"
            f"Type:{pos['type']} | Strike:{pos.get('strike','?')}\n"
            f"Entry:Rs.{entry} → Exit:Rs.{exit_price}\n"
            f"P&L:{sign}Rs.{pnl} | Day:Rs.{round(daily_pnl,2)}"
        )

        hdr = not os.path.exists(LOG_FILE)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            if hdr:
                f.write("date,time,type,strike,entry,exit,"
                        "reason,pnl,result,conf\n")
            f.write(f"{datetime.datetime.now().strftime('%d-%m-%Y')},"
                    f"{ts},{pos['type']},{pos.get('strike','?')},"
                    f"{entry},{exit_price},{exit_reason},"
                    f"{pnl},{res},{pos.get('confidence',0)}\n")

        open_position = None
        clear_pos()


# ================================================================
#   EXIT MONITOR — checks every 2 seconds
# ================================================================
def exit_monitor():
    print("     ✅ Exit monitor running (2s)")
    while True:
        try:
            now = datetime.datetime.now()
            if now.weekday() >= 5:
                time.sleep(60); continue
            mo = now.replace(hour=9,  minute=15, second=0)
            mc = now.replace(hour=15, minute=30, second=0)
            if not (mo <= now <= mc):
                time.sleep(30); continue
            if open_position is None:
                time.sleep(EXIT_CHECK_INTERVAL); continue

            ltp = get_ltp()
            if ltp is None:
                time.sleep(EXIT_CHECK_INTERVAL); continue

            pos = open_position
            ot  = "CE" if pos["type"]=="BUY_CE" else "PE"
            sl  = pos["sl_price"]
            tgt = pos["tgt_price"]

            if now.hour >= 15:
                execute_exit(ltp, "TIME EXIT 3PM")
            elif ot == "CE":
                if ltp <= sl:    execute_exit(sl,  "SL HIT")
                elif ltp >= tgt: execute_exit(tgt, "TARGET HIT")
            else:
                if ltp >= sl:    execute_exit(sl,  "SL HIT")
                elif ltp <= tgt: execute_exit(tgt, "TARGET HIT")

            time.sleep(EXIT_CHECK_INTERVAL)
        except Exception as e:
            print(f"     ❌ Monitor error: {e}")
            time.sleep(EXIT_CHECK_INTERVAL)


# ================================================================
#   GET MARKET DATA + INDICATORS — BankNifty
# =================================================
# ... [TRUNCATED FILE CONTENT]
```


==================================================
