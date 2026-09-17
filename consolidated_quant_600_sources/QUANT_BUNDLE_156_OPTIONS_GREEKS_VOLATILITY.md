# ⚡ [QUANT-SOURCE-156] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_156_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: nifty-options-paper-trading-bot (`PHASE4-QUANT-141`)
- **Full Name**: `PHASE4-QUANT-141_workratananmol-hub__nifty-options-paper-trading-bot`
- **Description**: Paper-only NIFTY 50 options research bot with read-only Dhan data, risk gates, backtesting, and P&L journals.
- **GitHub Stars**: 4
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# NIFTY Paper Options Research Bot

> **PAPER ONLY** — this project **never places, modifies, or cancels real broker orders**.
> Simulated research desk for NIFTY 50 long-options strategies. Not financial advice. Not a live trading system.

[Project page](https://workratananmol-hub.github.io/nifty-options-paper-trading-bot/) · [Setup](docs/SETUP.md) · [Architecture](docs/ARCHITECTURE.md) · [Security](SECURITY.md)

![Architecture overview](images/nifty-paper-bot-architecture.png)

| | |
| --- | --- |
| **Mode** | `TRADING_MODE=paper` only (hard gate at startup) |
| **Default capital** | **INR 100,000** simulated |
| **Risk per trade** | **1%** of current equity (stop-based sizing) |
| **Max premium** | **8%** of current equity |
| **Orders** | None — paper fills + local journal only |
| **Broker data** | Optional Dhan **market-data** (read-only adapter) |

Zero paper trades is a valid, safe outcome when risk, cash, fees, spread, liquidity, or depth gates reject size.

---

## What this is

A **paper-only** research stack for NIFTY 50 options:

- Offline **fixture** path (no credentials)
- Optional **Dhan read-only** market data for live quotes/chains/candles
- Strategy lab + liquidity-aware contract selector
- Simulated fills with approximate Indian option costs
- SQLite journal, Excel/CSV P&L ledgers
- Evidence-safe walk-forward backtest (refuses to crown a winner without adequate data)
- Optional **n8n** webhook → Google Sheets (inactive template; no broker nodes)
- Local FastAPI dashboard/API (paper status, not an order router)

**Out of scope:** live order placement, naked short options, overnight inventory, guaranteed edge, AI “certainty.”

---

## Quickstart

### Requirements

- Python **3.12+** (developed/tested on **3.14**)
- Windows, macOS, or Linux with `Asia/Kolkata` timezone data

### Windows (PowerShell)

```powershell
git clone https://github.com/workratananmol-hub/nifty-options-paper-trading-bot.git
cd nifty-options-paper-trading-bot
python -m pip install -r requirements.txt
Copy-Item .env.example .env
# Keep TRADING_MODE=paper. Leave DHAN_* empty for offline fixtures.
python -m src.cli fixture-demo
python -m pytest -q
```

### Unix / macOS

```bash
git clone https://github.com/workratananmol-hub/nifty-options-paper-trading-bot.git
cd nifty-options-paper-trading-bot
python -m pip install -r requirements.txt
cp .env.example .env
# Keep TRADING_MODE=paper. Leave DHAN_* empty for offline fixtures.
python -m src.cli fixture-demo
python -m pytest -q
```

`.env.example` is a **human template only**. Runtime loads process env + local `.env` + code defaults — **never** the template file.

### Continuous paper engine (fixtures)

```text
python -m src.cli run-engine --fixtures
```

### Local API / dashboard

```text
python -m uvicorn src.api:app --port 8000
```

Open `http://127.0.0.1:8000` — banner shows **PAPER ONLY**. No order endpoints exist.

---

## Simulated capital & risk defaults

| Control | Default | Env |
| --- | --- | --- |
| Starting paper capital | **₹1,00,000** | `STARTING_CAPITAL` |
| Risk per trade | **1.0%** of current equity | `RISK_PER_TRADE_PCT` |
| Max premium allocation | **8%** of current equity | `MAX_PREMIUM_ALLOCATION_PCT` |
| Max daily loss | 1.5% of **starting capital** baseline | `MAX_DAILY_LOSS_PCT` |
| Max entries / day | 2 | `MAX_ENTRIES_PER_DAY` |
| Max open positions | 1 | `MAX_OPEN_POSITIONS` |
| Stop / target | 25% / 35% of premium | `STOP_LOSS_PCT`, `TARGET_PCT` |
| Max spread | 2% | `MAX_SPREAD_PCT` |
| Min OI / volume | 5000 / 500 | `MIN_OPTION_OI`, `MIN_OPTION_VOLUME` |
| Min days to expiry | 1 (excludes 0-DTE by default) | `MIN_DAYS_TO_EXPIRY` |

Full table: [docs/RISK.md](docs/RISK.md).

---

## Dhan read-only market data (optional)

Dhan is used for **market data only**. The adapter is `DhanReadOnlyAdapter` — **no** `place_order` / `modify_order` / `cancel_order` (or related) methods.

1. Copy `.env.example` → `.env`.
2. Set placeholders only in your private `.env` (never commit real values):

```env
TRADING_MODE=paper
USE_FIXTURES=false
DHAN_CLIENT_ID=your_client_id_here
DHAN_ACCESS_TOKEN=your_access_token_here
```

3. Ensure an active **Dhan Data API** subscription. Authentication alone is not data entitlement. Missing quotes fail closed (no fabricated LTP/OI).
4. Run paper engine (still **paper fills only**):

```text
python -m src.cli run-engine
```

Details: [docs/CONNECTORS.md](docs/CONNECTORS.md), [docs/SETUP.md](docs/SETUP.md).

Official references: [Dhan authentication](https://dhanhq.co/docs/v2/authentication/), [market quote](https://dhanhq.co/docs/v2/market-quote/), [option chain](https://dhanhq.co/docs/v2/option-chain/), and [instrument master](https://dhanhq.co/docs/v2/instruments/).

---

## Backtest schema (exact)

Research CSVs must include executable option quotes. Spot close is **never** used as option premium. Spreads are **never** fabricated.

**Required columns:**

```text
timestamp, open, high, low, close, volume,
ce_bid, ce_ask, pe_bid, pe_ask,
ce_security_id, pe_security_id,
ce_expiry, pe_expiry, ce_strike, pe_strike,
ce_quote_timestamp, pe_quote_timestamp,
quantity   # or lot_size
```

**Rules (summary):**

- Timestamps strictly increasing weekday NSE regular-session minutes
- CE and PE use **distinct** quote series
- Next-bar fills (signal at bar `i`, enter at `i+1` ask; exit at bid + costs)
- Unaffordable entries skipped — never forced
- Synthetic API smoke **never** declares a winner
- Winner only after chronological dev / OOS / holdout evidence

```text
python -m src.cli backtest --csv data/your_options_bars.csv
```

See [docs/STRATEGY.md](docs/STRATEGY.md) and [docs/DATA_COLLECTION.md](docs/DATA_COLLECTION.md).

---

## P&L and journal outputs

| Path | Contents |
| --- | --- |
| `output/logs/paper_journal.sqlite3` | Paper journal (trades, risk, decisions) |
| `output/logs/pnl-ledger.xlsx` | Sheets: **Trades**, **Daily PnL**, **Summary** |
| `output/logs/trades.csv` | Flat trade log |
| `output/logs/fixture/` | Isolated fixture-demo storage only |
| `output/backtests/` | Optional backtest artifacts |
| `output/cache/` | Constituent / master caches |

**Excel / CSV trade columns:**
`trade_id`, `symbol`, `option_type`, `strike`, `expiry`, `direction`, `lots`, `quantity`, `entry_price`, `exit_price`, `entry_fees`, `exit_fees`, `slippage_cost`, `pnl`, `pnl_pct`, `entry_time`, `exit_time`, `exit_reason`, `strategy`, `mode`

**Summary metrics (Excel):** mode=`PAPER ONLY`, starting capital, trades, net P&L, win rate, profit factor, expectancy, max drawdown, ending equity.

```text
python -m src.cli export-ledger
```

**Fixture P&L is not live performance evidence.** Paper results do not imply profitability.

---

## n8n Google Sheets connector (optional)

1. Import [`automation/pnl-to-google-sheets-webhook.json`](automation/pnl-to-google-sheets-webhook.json) into n8n.
2. Workflow ships **`active: false`** with `REPLACE_*` placeholders only.
3. Configure Google Sheets credential + spreadsheet id in **your** n8n instance.
4. Activate workflow; set `N8N_PNL_WEBHOOK_URL` to the webhook URL.
5. Nodes: webhook → transform → Google Sheets append → respond. **No broker/order nodes.**

Payload event: `paper_trade_closed` with `mode: "paper"`. See [docs/CONNECTORS.md](docs/CONNECTORS.md).

---

## Project layout

| Path | Purpose |
| --- | --- |
| `src/strategies/` | Strategy lab + contract selector |
| `src/data/` | Dhan RO adapter, fixtures, market context |
| `src/engine/` | Paper engine, risk, fills, journal, Excel, webhook |
| `src/backtest/` | Walk-forward evaluator |
| `docs/` | User docs + GitHub Pages (`index.html`) |
| `docs/audit/` | Internal review history (not product marketing) |
| `automation/` | Inactive n8n template |
| `output/` | Runtime logs/cache/backtests (**gitignored**) |
| `images/` | Architecture diagram asset |
| `scripts/` | Release safety checks |

---

## Documentation

| Doc | Description |
| --- | --- |
| [docs/index.html](docs/index.html) | GitHub Pages project page |
| [docs/SETUP.md](docs/SETUP.md) | Install, env, commands, API |
| [docs/RISK.md](docs/RISK.md) | Risk defaults, session, fills |
| [docs/STRATEGY.md](docs/STRATEGY.md) | Strategy lab + backtest rules |
| [docs/RESEARCH.md](docs/RESEARCH.md) | Research notes & data limits |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | System architecture |
| [docs/CONNECTORS.md](docs/CONNECTORS.md) | Dhan RO, n8n, API surface |
| [docs/DATA_COLLECTION.md](docs/DATA_COLLECTION.md) | Fixtures, live data, CSV schema |
| [docs/PUBLIC_DEPLOYMENT.md](docs/PUBLIC_DEPLOYMENT.md) | Public repo & Pages hygiene |
| [SECURITY.md](SECURITY.md) | Security policy |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution rules |

---

## Security (public release)

- **Never** commit `.env`, tokens, client secrets, or real account IDs.
- Credentials: placeholders in `.env.example` only; real values stay local.
- Do not publish `output/` journals, Excel ledgers, or private caches.
- `TRADING_MODE` must remain `paper`; non-paper values raise at startup.
- Safety gate: `python scripts/check_public_release_safety.py`
- Full policy: [SECURITY.md](SECURITY.md)

---

## Roadmap (research only)

Planned or open research items — **not** commitments, and **not** live-trading features:

1. Richer historical option-quote datasets under the same fail-closed schema
2. Additional defined-risk long-premium strategy candidates with walk-forward gates
3. Better holiday/calendar maintenance as NSE publishes years
4. Dashboard UX polish for paper status / decision logs
5. Optional debit-spread research (still no naked short, no live orders)

Explicitly **not** on the roadmap for this repository: broker order routers, live auto-execution, or “guaranteed profit” claims.

---

## Commands cheat sheet

```text
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/check_public_release_safety.py
python -m src.cli fixture-demo
python -m src.cli analyze-once --fixtures --force
python -m src.cli run-engine --fixtures
python -m src.cli export-ledger
python -m src.cli backtest --csv data/sample.csv
python -m src.cli context --fixtures
python -m uvicorn src.api:app --port 8000
```

---

## Disclaimer

This software is for **education and research**. Paper and backtest results are **not** forecasts. Markets involve loss of capital. Nothing here is investment, tax, or trading advice. The authors accept no liability for decisions made from this tooling.

## License

[MIT](LICENSE)

### Core Implementation Code & Architecture
#### File: `src/__init__.py`
```python
"""NIFTY 50 options paper research and simulated-execution system."""

__version__ = "1.0.0"
```

#### File: `src/engine/__init__.py`
```python
"""Paper trading engine."""

from src.engine.paper_engine import PaperEngine

__all__ = ["PaperEngine"]
```

#### File: `src/market/__init__.py`
```python
"""Market session helpers."""

from src.market.session import MarketSession, SessionState

__all__ = ["MarketSession", "SessionState"]
```

#### File: `src/backtest/__init__.py`
```python
"""Backtest / walk-forward evaluation."""

from src.backtest.engine import BacktestEngine, BacktestResult, evaluate_strategies

__all__ = ["BacktestEngine", "BacktestResult", "evaluate_strategies"]
```

#### File: `src/data/__init__.py`
```python
"""Market data adapters and context builders."""

from src.data.dhan_adapter import DhanReadOnlyAdapter, FORBIDDEN_DHAN_METHODS, create_market_data_source
from src.data.fixtures import FixtureMarketData, ensure_fixture_files
from src.data.market_context import build_market_context

__all__ = [
    "DhanReadOnlyAdapter",
    "FORBIDDEN_DHAN_METHODS",
    "FixtureMarketData",
    "build_market_context",
    "create_market_data_source",
    "ensure_fixture_files",
]
```

#### File: `src/models/__init__.py`
```python
"""Shared domain models."""

from src.models.types import (
    ContractCandidate,
    Direction,
    ExitReason,
    Fill,
    MarketContext,
    OptionQuote,
    PaperPosition,
    PaperTrade,
    Signal,
    SignalAction,
    StrategyResult,
)

__all__ = [
    "ContractCandidate",
    "Direction",
    "ExitReason",
    "Fill",
    "MarketContext",
    "OptionQuote",
    "PaperPosition",
    "PaperTrade",
    "Signal",
    "SignalAction",
    "StrategyResult",
]
```


==================================================


## [2/3] Repository: fully-automated-nifty-options-trading (`PHASE4-QUANT-145`)
- **Full Name**: `PHASE4-QUANT-145_srikar-kodakandla__fully-automated-nifty-options-trading`
- **Description**: It is fully automated algo trading , It trades for you in Nifty options using Zerodha kite . You don't need to pay 4000 indian rupees monthly for kite api because this program uses selenium to access zerodha kite website
- **GitHub Stars**: 248
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
## Fully automated nifty options trading

It is fully automated algo trading , It trades for you in Nifty options using Zerodha kite . You don't need to pay 4000 indian rupees monthly for kite api because this program uses selenium to access zerodha kite website

Notice: This project is deprecated as Fyers has updated their API from version 2 to version 3, which is not supported by this program.

The Program follows supertrend strategy with adx to trade options , i rigorously backtested nifty in 5 min chart and find out the best supertrend values and adx values. when ever supertrend gives buy signal , This program sells options corresponding to the buy signal. it also checks all combinations of nifty options to sell , to see which combination gives more profits, there is a risk paramater in kite_strategy.py , where 50 is lowest possible risk , where it tries to sell options with 50 points difference (if nifty is at 14000 and supertrend gives buy signal then it tries to sell 14050PE and buys 14000PE) and if you choose 500 then , it tries to select  options with 500 points difference (selecting 13500PE buy and 14000 PE sell). when the option goes above 95% of your profit , then it sells and selects next week options and trades with them.

![Screenshot from 2022-06-25 20-14-25](https://user-images.githubusercontent.com/46400867/175778598-47c9f645-084d-46e8-a4ae-5e90cee7b07a.png)

as shown in the screenshot , it sells corresponding options when ever a signal is triggered in supertrend indicator


you can use crontab to schedule to trade everyday , write the below code in "crontab -e"

>59 08 * * 1-5  DISPLAY=:10 screen -dmS srikartrade ipython3 kite_strategy.py # it trades by above explained strategy 

>59 08 * * 1-5  DISPLAY=:10 screen -dmS check_database ipython3 check_database.py  #to check if the live data is fetching from fyers api

>30 15 * * 1-5 screen -XS database quit # it stops trade at 3:30 PM as markets closes at that time


The program uses selenium to make trades in zerodha kite and it uses fyers account to get past data . Fyers provides free api for past data and trading.

This code is kept publicly in github for educational purpose only. I am not responsible with your profit and losses.


## About Me

I have extensive experience building algorithmic trading strategies and systems, including 4+ years of active trading experience across stocks, options, currencies, and commodities. In addition to trading system development, I have a strong background in cutting-edge deep learning techniques.
- Email: kodakandlasrikar99@gmail.com
- Phone no: (+91) 9176462946 (Please use WhatApp messages only; no calls) 
- LinkedIn: [https://www.linkedin.com/in/srikar-kodakandla/]

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `common/__init__.py`
```python

```

#### File: `fyers/__init__.py`
```python

```

#### File: `kite/ZerodhaAutomationExample.py`
```python

```

#### File: `kite/Brokers/__init__.py`
```python
#
```

#### File: `kite/Loggers/__init__.py`
```python
#
```


==================================================


## [3/3] Repository: betterOptionsTrading (`PHASE4-QUANT-147`)
- **Full Name**: `PHASE4-QUANT-147_amit0rana__betterOptionsTrading`
- **Description**: This repository has 2 userscripts. (1) To add features to kite.zerodha.com (2) To add features to pro.upstox.com
- **GitHub Stars**: 135
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
Disclaimer: I have made this tool for my personal use, it may have bugs. 

This repository has 2 userscripts
* [For Zerodha](https://github.com/amit0rana/betterOptionsTrading/blob/master/betterKite.md)
* [For Upstox](https://github.com/amit0rana/betterOptionsTrading/blob/master/betterUpstox.md)
* [For Sensibull](https://github.com/amit0rana/betterOptionsTrading/blob/master/betterSensibull.md)
* [For NSEIndia site] (https://github.com/amit0rana/betterOptionsTrading/blob/master/betterNSE.md)

------
# Developing betterKite

`betterKite.user.js` is **generated** from the modules in `src/`. Editing it directly
will be overwritten on the next build.

```bash
npm install
npm run build    # src/ -> betterKite.user.js + betterKite.meta.js
npm run verify   # build is current + lint + tests
```

| Command | What it does |
| --- | --- |
| `npm run build` | Rebuilds both output files from `src/`. |
| `npm run check` | Fails if the checked-in outputs are stale. |
| `npm run lint` | ESLint over the built script, `betterCommon.js`, `src/`, `build/`, `test/`. |
| `npm test` | Behaviour tests. No browser or Kite login needed. |
| `npm run format` | Prettier. Not yet applied to `src/` — see below. |

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the module layout, why the build
concatenates rather than bundles, and the list of known-odd behaviour that was
deliberately preserved.

**Faster edit loop:** rather than pasting into the Tampermonkey editor, point a small
loader userscript at your working copy with
`// @require file:///path/to/betterOptionsTrading/betterKite.user.js` (needs "Allow
access to file URLs" enabled for the Tampermonkey extension). Every `npm run build` is
then live on the next page refresh.

`src/` has not been run through Prettier yet, to keep the cleanup diff readable.
`npm run format` will do it whenever you want that as its own commit.

### Core Implementation Code & Architecture
#### File: `package.json`
```python
{
  "name": "better-options-trading",
  "version": "5.08",
  "description": "Userscripts that add features to online trading platforms. betterKite is the main one.",
  "private": true,
  "license": "Unlicense",
  "scripts": {
    "build": "node build/build.js",
    "check": "node build/build.js --check",
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier --write \"src/**/*.js\" \"build/**/*.js\" \"test/**/*.js\"",
    "format:check": "prettier --check \"src/**/*.js\" \"build/**/*.js\" \"test/**/*.js\"",
    "test": "node --test test/",
    "verify": "npm run check && npm run lint && npm test"
  },
  "devDependencies": {
    "eslint": "^8.57.1",
    "prettier": "^3.3.3"
  }
}
```

#### File: `build/manifest.json`
```python
{
  "files": [
    "src/metadata.txt",
    "src/legal/unlicense.txt",
    "src/runtime/00-toastify-css.js",
    "src/runtime/01-analytics.js",
    "src/runtime/02-jquery.js",
    "src/core/10-constants.js",
    "src/core/11-dom-paths.js",
    "src/core/12-utils.js",
    "src/core/13-settings.js",
    "src/core/14-stored-data.js",
    "src/ui/20-tooltips.js",
    "src/features/30-holdings.js",
    "src/features/31-positions.js",
    "src/features/32-dropdown-toggle.js",
    "src/core/15-margin-api.js",
    "src/features/33-watchlist.js",
    "src/features/34-pnl.js",
    "src/core/16-row-objects.js",
    "src/features/35-margin-saving.js",
    "src/ui/21-full-width.js",
    "src/main.js",
    "src/features/36-context-menu.js",
    "src/features/37-roi-nudges.js",
    "src/features/38-order-bump.js",
    "src/features/39-console-pnl.js",
    "src/features/40-trail-buttons.js",
    "src/features/41-order-window.js",
    "src/features/42-order-send.js",
    "src/bootstrap/00-visit-ping.js",
    "src/legal/disclaimer.txt",
    "src/bootstrap/01-init.js"
  ]
}
```

#### File: `test/golden/pure-functions.json`
```python
{
  "capturedFrom": "betterKite.ORIGINAL.js",
  "cases": [
    {
      "fn": "closestStrike",
      "args": [
        23412
      ],
      "result": 23400
    },
    {
      "fn": "closestStrike",
      "args": [
        23425
      ],
      "result": 23400
    },
    {
      "fn": "closestStrike",
      "args": [
        23437
      ],
      "result": 23450
    },
    {
      "fn": "closestStrike",
      "args": [
        58340,
        100
      ],
      "result": 58300
    },
    {
      "fn": "closestStrike",
      "args": [
        0,
        50
      ],
      "result": 0
    },
    {
      "fn": "getExpiryText",
      "args": [
        "NIFTY 26Jun 23000 CE"
      ],
      "result": "26Jun"
    },
    {
      "fn": "getExpiryText",
      "args": [
        "INFY"
      ],
      "result": ""
    },
    {
      "fn": "getExpiryText",
      "args": [
        "BANKNIFTY 26Jun FUT"
      ],
      "result": "26Jun"
    },
    {
      "fn": "getLastThursday",
      "args": [
        "JAN",
        2025
      ],
      "result": "30Jan"
    },
    {
      "fn": "getLastThursday",
      "args": [
        "Jun",
        2025
      ],
      "result": "26Jun"
    },
    {
      "fn": "getLastThursday",
      "args": [
        "DEC",
        2024
      ],
      "result": "26Dec"
    },
    {
      "fn": "getLastThursday",
      "args": [
        "FEB",
        2024
      ],
      "result": "29Feb"
    },
    {
      "fn": "getLastThursday",
      "args": [
        "JUN"
      ],
      "result": "26Jun"
    },
    {
      "fn": "getSensibullZerodhaTradingSymbol",
      "args": [
        "NIFTY"
      ],
      "result": "NIFTY"
    },
    {
      "fn": "getSensibullZerodhaTradingSymbol",
      "args": [
        "BHARTIARTL JUN FUT NFO"
      ],
      "result": "BHARTIARTL 26Jun FUT"
    },
    {
      "fn": "getSensibullZerodhaTradingSymbol",
      "args": [
        "NIFTY 8th w APR 14200 CE NFO"
      ],
      "result": "NIFTY 08APR 14200 CE"
    },
    {
      "fn": "getSensibullZerodhaTradingSymbol",
      "args": [
        "BANKNIFTY JUN 30000 PE NFO"
      ],
      "result": "BANKNIFTY 26Jun 30000 PE"
    },
    {
      "fn": "getSensibullZerodhaTradingSymbol",
      "args": [
        "NIFTY 24JUN 23000 CE NFO"
      ],
      "result": "NIFTY 24JUN 23000 CE"
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "",
        "NFO",
        "NRML",
        1,
        1
      ],
      "result": null
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "INFY",
        "NSE",
        "CNC",
        10,
        1500
      ],
      "result": null
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "SBIN",
        "BSE",
        "CNC",
        10,
        800
      ],
      "result": null
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "NIFTY JUN FUT NFO",
        "NFO",
        "NRML",
        75,
        23000
      ],
      "result": {
        "exchange": "NFO",
        "symbol": "NIFTY",
        "product": "NRML",
        "tradingsymbol": "NIFTY25JUNFUT",
        "pece": "PE",
        "strike": "",
        "optfut": "FUT",
        "scrip": "NIFTY25JUN",
        "quantity": 75,
        "price": 23000,
        "transaction_type": "BUY"
      }
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "NIFTY 8th w APR 14200 CE NFO LABELS",
        "NFO",
        "NRML",
        -75,
        120
      ],
      "result": {
        "exchange": "NFO",
        "symbol": "NIFTY",
        "product": "NRML",
        "optfut": "OPT",
        "tradingsymbol": "NIFTY2540814200CE",
        "pece": "CE",
        "strike": "14200",
        "scrip": "NIFTY2548",
        "quantity": 75,
        "price": 120,
        "transaction_type": "SELL"
      }
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "BANKNIFTY JUN 30000 PE NFO",
        "NFO",
        "NRML",
        -15,
        200
      ],
      "result": {
        "exchange": "NFO",
        "symbol": "BANKNIFTY",
        "product": "NRML",
        "optfut": "OPT",
        "tradingsymbol": "BANKNIFTY25JUN30000PE",
        "pece": "PE",
        "strike": "30000",
        "scrip": "BANKNIFTY25JUN",
        "quantity": 15,
        "price": 200,
        "transaction_type": "SELL"
      }
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "NIFTY 24JUN 23000 CE NFO",
        "NFO",
        "NRML",
        75,
        12
      ],
      "result": {
        "exchange": "NFO",
        "symbol": "NIFTY",
        "product": "NRML",
        "optfut": "OPT",
        "tradingsymbol": "NIFTY24JUN23000CE",
        "pece": "CE",
        "strike": "23000",
        "scrip": "NIFTY2524JUN",
        "quantity": 75,
        "price": 12,
        "transaction_type": "BUY"
      }
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "SENSEX 24JUN 80000 PE BFO",
        "BFO",
        "NRML",
        -10,
        90
      ],
      "result": {
        "exchange": "BFO",
        "symbol": "SENSEX",
        "product": "NRML",
        "optfut": "OPT",
        "tradingsymbol": "SENSEX24JUN80000PE",
        "pece": "PE",
        "strike": "80000",
        "scrip": "SENSEX2524JUN",
        "quantity": 10,
        "price": 90,
        "transaction_type": "SELL"
      }
    },
    {
      "fn": "getMarginCalculationData",
      "args": [
        "NIFTY  JUN  23000  CE  NFO",
        "NFO",
        " NRML ",
        75,
        12
      ],
      "result": {
        "exchange": "NFO",
        "symbol": "NIFTY",
        "product": "NRML",
        "optfut": "OPT",
        "tradingsymbol": "NIFTY25JUN23000CE",
        "pece": "CE",
        "strike": "23000",
        "scrip": "NIFTY25JUN",
        "quantity": 75,
        "price": 12,
        "transaction_type": "BUY"
      }
    },
    {
      "fn": "queryStringToJSON",
      "args": [
        "tradingsymbol=NIFTY25JUN23000CE&quantity=75&price=0"
      ],
      "result": {
        "tradingsymbol": "NIFTY25JUN23000CE",
        "quantity": "75",
        "price": "0"
      }
    },
    {
      "fn": "queryStringToJSON",
      "args": [
        "a=1&a=2&a=3"
      ],
      "result": {
        "a": [
          "1",
          "2",
          "3"
        ]
      }
    },
    {
      "fn": "queryStringToJSON",
      "args": [
        "name=NIFTY%20BANK&empty="
      ],
      "result": {
        "name": "NIFTY BANK",
        "empty": ""
      }
    },
    {
      "fn": "isLastDay",
      "args": [
        4
      ],
      "result": true
    },
    {
      "fn": "isLastDay",
      "args": [
        1
      ],
      "result": false
    },
    {
      "fn": "isLastDay",
      "args": [
        3
      ],
      "result": false
    },
    {
      "fn": "createPnlText",
      "args": [
        1500,
        -5000,
        100000
      ],
      "result": "<span random-att='temppnl' class='text-green open pnl randomClassToHelpHide'>P&L: INR 1500.00<br><span class='text-label randomClassToHelpHide'>Prem Taken: INR -5000.00 / -5.00%</span><br><span class='text-label randomClassToHelpHide'>Current Prem: INR -6500.00 </span><br><span class='text-label randomClassToHelpHide'>Margin: INR 100000.00</span><br><span class='text-label randomClassToHelpHide'>Current ROI: 1.50% </span></span>"
    },
    {
      "fn": "createPnlText",
      "args": [
        -1500,
        -5000,
        100000
      ],
      "result": "<span random-att='temppnl' class='text-red open pnl randomClassToHelpHide'>P&L: INR -1500.00<br><span class='text-label randomClassToHelpHide'>Prem Taken: INR -5000.00 / -5.00%</span><br><span class='text-label randomClassToHelpHide'>Current Prem: INR -3500.00 </span><br><span class='text-label randomClassToHelpHide'>Margin: INR 100000.00</span><br><span class='text-label randomClassToHelpHide'>Current ROI: -1.50% </span></span>"
    },
    {
      "fn": "createPnlText",
      "args": [
        0,
        0,
        -1
      ],
      "result": "<span random-att='temppnl' class='text-red open pnl randomClassToHelpHide'>P&L: INR 0.00<br><span class='text-label randomClassToHelpHide'>Prem Taken: INR 0.00 / 0.00%</span><br><span class='text-label randomClassToHelpHide'>Current Prem: INR 0.00 </span></span>"
    }
  ]
}
```

#### File: `package-lock.json`
```python
{
  "name": "better-options-trading",
  "version": "5.08",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "better-options-trading",
      "version": "5.08",
      "license": "Unlicense",
      "devDependencies": {
        "eslint": "^8.57.1",
        "prettier": "^3.3.3"
      }
    },
    "node_modules/@eslint-community/eslint-utils": {
      "version": "4.10.1",
      "resolved": "https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.10.1.tgz",
      "integrity": "sha512-cuadcxVFE8sDK6iWJbs8Sn0av2Nrh2QSGQhVlBW9AaAHqHwjWsZHT8LJ4hFGPh7ASBV2deFdM7H/DPjulmh8rg==",
      "dev": true,
      "dependencies": {
        "eslint-visitor-keys": "^3.4.3"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      },
      "peerDependencies": {
        "eslint": "^6.0.0 || ^7.0.0 || >=8.0.0"
      }
    },
    "node_modules/@eslint-community/regexpp": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz",
      "integrity": "sha512-EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==",
      "dev": true,
      "engines": {
        "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
      }
    },
    "node_modules/@eslint/eslintrc": {
      "version": "2.1.4",
      "resolved": "https://registry.npmjs.org/@eslint/eslintrc/-/eslintrc-2.1.4.tgz",
      "integrity": "sha512-269Z39MS6wVJtsoUl10L60WdkhJVdPG24Q4eZTH3nnF6lpvSShEK3wQjDX9JRWAUPvPh7COouPpU9IrqaZFvtQ==",
      "dev": true,
      "dependencies": {
        "ajv": "^6.12.4",
        "debug": "^4.3.2",
        "espree": "^9.6.0",
        "globals": "^13.19.0",
        "ignore": "^5.2.0",
        "import-fresh": "^3.2.1",
        "js-yaml": "^4.1.0",
        "minimatch": "^3.1.2",
        "strip-json-comments": "^3.1.1"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/@eslint/js": {
      "version": "8.57.1",
      "resolved": "https://registry.npmjs.org/@eslint/js/-/js-8.57.1.tgz",
      "integrity": "sha512-d9zaMRSTIKDLhctzH12MtXvJKSSUhaHcjV+2Z+GK+EEY7XKpP5yR4x+N3TAcHTcu963nIr+TMcCb4DBCYX1z6Q==",
      "dev": true,
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      }
    },
    "node_modules/@humanwhocodes/config-array": {
      "version": "0.13.0",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/config-array/-/config-array-0.13.0.tgz",
      "integrity": "sha512-DZLEEqFWQFiyK6h5YIeynKx7JlvCYWL0cImfSRXZ9l4Sg2efkFGTuFf6vzXjK1cq6IYkU+Eg/JizXw+TD2vRNw==",
      "deprecated": "Use @eslint/config-array instead",
      "dev": true,
      "dependencies": {
        "@humanwhocodes/object-schema": "^2.0.3",
        "debug": "^4.3.1",
        "minimatch": "^3.0.5"
      },
      "engines": {
        "node": ">=10.10.0"
      }
    },
    "node_modules/@humanwhocodes/module-importer": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz",
      "integrity": "sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==",
      "dev": true,
      "engines": {
        "node": ">=12.22"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/nzakas"
      }
    },
    "node_modules/@humanwhocodes/object-schema": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/object-schema/-/object-schema-2.0.3.tgz",
      "integrity": "sha512-93zYdMES/c1D69yZiKDBj0V24vqNzB/koF26KPaagAfd3P/4gUlh3Dys5ogAK+Exi9QyzlD8x/08Zt7wIKcDcA==",
      "deprecated": "Use @eslint/object-schema instead",
      "dev": true
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "dev": true,
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "dev": true,
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "dev": true,
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@ungap/structured-clone": {
      "version": "1.3.3",
      "resolved": "https://registry.npmjs.org/@ungap/structured-clone/-/structured-clone-1.3.3.tgz",
      "integrity": "sha512-60YRaenCQcVjYEKOcG824+DRGGIQ3VKErcBoAEDJZz5bKIs2ZG+X/H9Nk+Q6EVkwJk5QNApxbrc5QtBSwtrXAg==",
      "dev": true
    },
    "node_modules/acorn": {
      "version": "8.18.0",
      "resolved": "https://registry.npmjs.org/acorn/-/acorn-8.18.0.tgz",
      "integrity": "sha512-lGq+9yr1/GuAWaVYIHRjvvySG5/4VfKIvC8EWxStPdcDh/Ka7FG3twP6v4d5BkravUilhIAsG4Qj83t02LWUPQ==",
      "dev": true,
      "bin": {
        "acorn": "bin/acorn"
      },
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/acorn-jsx": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz",
      "integrity": "sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==",
      "dev": true,
      "peerDependencies": {
        "acorn": "^6.0.0 || ^7.0.0 || ^8.0.0"
      }
    },
    "node_modules/ajv": {
      "version": "6.15.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-6.15.0.tgz",
      "integrity": "sha512-fgFx7Hfoq60ytK2c7DhnF8jIvzYgOMxfugjLOSMHjLIPgenqa7S7oaagATUq99mV6IYvN2tRmC0wnTYX6iPbMw==",
      "dev": true,
      "dependencies": {
        "fast-deep-equal": "^3.1.1",
        "fast-json-stable-stringify": "^2.0.0",
        "json-schema-traverse": "^0.4.1",
        "uri-js": "^4.2.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "dev": true,
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "dev": true,
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/argparse": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz",
      "integrity": "sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==",
      "dev": true
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true
    },
    "node_modules/brace-expansion": {
      "version": "1.1.18",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.18.tgz",
      "integrity": "sha512-Edep/X9fGqVNmzKBVsDYIOtD+z1tuezV70LBjdCst9Tqu76lsnvRiZ6oTic1n+/BIwX6QDGAO94PN4N2SADvtw==",
      "dev": true,
      "dependencies": {
        "balanced-match": "^1.0.0",
        "concat-map": "0.0.1"
      }
    },
    "node_modules/callsites": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz",
      "integrity": "sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==",
      "dev": true,
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/chalk": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz",
      "integrity": "sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==",
      "dev": true,
      "dependencies": {
        "ansi-styles": "^4.1.0",
        "supports-color": "^7.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "dev": true,
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "dev": true
    },
    "node_modules/concat-map": {
      "version": "0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz",
      "integrity": "sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==",
      "dev": true
    },
    "node_modules/cross-spawn": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
      "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
      "dev": true,
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "dev": true,
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/deep-is": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz",
      "integrity": "sha512-oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==",
      "dev": true
    },
    "node_modules/doctrine": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/doctrine/-/doctrine-3.0.0.tgz",
      "integrity": "sha512-yS+Q5i3hBf7GBkd4KG8a7eBNNWNGLTaEwwYWUijIYM7zrlYDM0BFXHjjPWlWZ1Rg7UaddZeIDmi9jF3HmqiQ2w==",
      "dev": true,
      "dependencies": {
        "esutils": "^2.0.2"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/escape-string-regexp": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz",
      "integrity": "sha512-TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==",
      "dev": true,
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/eslint": {
      "version": "8.57.1",
      "resolved": "https://registry.npmjs.org/eslint/-/eslint-8.57.1.tgz",
      "integrity": "sha512-ypowyDxpVSYpkXr9WPv2PAZCtNip1Mv5KTW0SCurXv/9iOpcrH9PaqUElksqEB6pChqHGDRCFTyrZlGhnLNGiA==",
      "deprecated": "This version is no longer supported. Please see https://eslint.org/version-support for other options.",
      "dev": true,
      "dependencies": {
        "@eslint-community/eslint-utils": "^4.2.0",
        "@eslint-community/regexpp": "^4.6.1",
        "@eslint/eslintrc": "^2.1.4",
        "@eslint/js": "8.57.1",
        "@humanwhocodes/config-array": "^0.13.0",
        "@humanwhocodes/module-importer": "^1.0.1",
        "@nodelib/fs.walk": "^1.2.8",
        "@ungap/structured-clone": "^1.2.0",
        "ajv": "^6.12.4",
        "chalk": "^4.0.0",
        "cross-spawn": "^7.0.2",
        "debug": "^4.3.2",
        "doctrine": "^3.0.0",
        "escape-string-regexp": "^4.0.0",
        "eslint-scope": "^7.2.2",
        "eslint-visitor-keys": "^3.4.3",
        "espree": "^9.6.1",
        "esquery": "^1.4.2",
        "esutils": "^2.0.2",
        "fast-deep-equal": "^3.1.3",
        "file-entry-cache": "^6.0.1",
        "find-up": "^5.0.0",
        "glob-parent": "^6.0.2",
        "globals": "^13.19.0",
        "graphemer": "^1.4.0",
        "ignore": "^5.2.0",
        "imurmurhash": "^0.1.4",
        "is-glob": "^4.0.0",
        "is-path-inside": "^3.0.3",
        "js-yaml": "^4.1.0",
        "json-stable-stringify-without-jsonify": "^1.0.1",
        "levn": "^0.4.1",
        "lodash.merge": "^4.6.2",
        "minimatch": "^3.1.2",
        "natural-compare": "^1.4.0",
        "optionator": "^0.9.3",
        "strip-ansi": "^6.0.1",
        "text-table": "^0.2.0"
      },
      "bin": {
        "eslint": "bin/eslint.js"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/eslint-scope": {
      "version": "7.2.2",
      "resolved": "https://registry.npmjs.org/eslint-scope/-/eslint-scope-7.2.2.tgz",
      "integrity": "sha512-dOt21O7lTMhDM+X9mB4GX+DZrZtCUJPL/wlcTqxyrx5IvO0IYtILdtrQGQp+8n5S0gwSVmOf9NQrjMOgfQZlIg==",
      "dev": true,
      "dependencies": {
        "esrecurse": "^4.3.0",
        "estraverse": "^5.2.0"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "
# ... [TRUNCATED FILE CONTENT]
```


==================================================
