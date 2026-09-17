# ⚡ [QUANT-SOURCE-025] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_025_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: dhan-trading-app (`WHEEL_dhan-trading-app`)
- **Full Name**: `dhan-trading-app`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Dhan Risk-Based Auto-Quantity Tool

A simple Streamlit app that **auto-calculates order quantity** from a fixed risk % and stop-loss distance, and **places orders via Dhan** (entry + immediate SL order).

> ⚠️ Use in **paper / mock** first. Market trading is risky. Lot sizes & product availability can change. Verify all values with your broker.

---

## Features
- Position sizing: `qty = floor( (capital * risk%) / (abs(entry - SL) * contract_multiplier) )`
- Supports NSE Futures & Options (editable instrument list; override lot size/multiplier in UI)
- Place **entry** order and then **instant stop-loss** order (SL-M or SL-L) via a pluggable Dhan client
- Dry-run mode, order preview, and CSV logs in `logs/orders.csv`
- Sensible checks: min 1 lot, tick-size alignment, price guardrails
- Optional TradingView webhook JSON → computes qty from risk inputs and calls the same order function (small FastAPI server)

---

## Quick Start

1. **Create a Dhan API access token** (per your DhanHQ docs).
2. Download and open this folder in VS Code/PyCharm.
3. Create & edit your `.env` (or set environment vars directly):
```
DHAN_CLIENT_ID=your-dhan-client-id
DHAN_ACCESS_TOKEN=your-dhan-access-token
```
4. Install deps:
```
python -m venv .venv
# activate venv (Windows) .venv\Scripts\activate    (Linux/Mac) source .venv/bin/activate
pip install -r requirements.txt
```
5. Run the Streamlit app:
```
streamlit run streamlit_app.py
```
6. (Optional) Run webhook server for TradingView alerts:
```
uvicorn webhook:app --host 0.0.0.0 --port 7860 --reload
```

> In TradingView alert box, set **Webhook URL** to `http://<your-ip>:7860/tv`, and use a JSON payload like:
```json
{
  "symbol": "NIFTY24SEPFUT",
  "side": "BUY",
  "entry": 24125.0,
  "sl": 24075.0,
  "capital": 500000,
  "risk_pct": 0.01,
  "multiplier": 50,
  "product_type": "INTRADAY",
  "order_type": "LIMIT",
  "sl_order_type": "SL-M",
  "qty_override": null
}
```

---

## Dhan API Integration

This project ships with a **stub** Dhan client (`dhan_client.py`). Fill the `place_order` function with the actual REST call or use the official/community SDK as you prefer. The app passes a normalized order dict:
```python
{
  "symbol": "...",
  "side": "BUY"/"SELL",
  "quantity": 50,
  "order_type": "MARKET"/"LIMIT",
  "price": 123.45,
  "product_type": "CNC"/"INTRADAY"/"MARGIN",
  "validity": "DAY"/"IOC",
  "exchange": "NSE",
  "variety": "REGULAR",
  "tag": "risk-sizer"
}
```

Then for SL:
```python
{
  "symbol": "...",
  "side": "SELL"/"BUY",         # opposite of entry side
  "quantity": 50,
  "order_type": "SL-M"/"SL-L",  # stop-market or stop-limit
  "trigger_price": 120.0,
  "price": 120.0,               # for SL-L
  ...
}
```

**Important:** Symbols, varieties, and product types may differ at Dhan. Confirm exact params in their docs before going live.

---

## Files
- `streamlit_app.py` – main UI/logic
- `risk_sizer.py` – position sizing, validation helpers
- `dhan_client.py` – stub Dhan API client (replace with real call)
- `webhook.py` – FastAPI webhook for TradingView alerts
- `requirements.txt` – deps
- `.env.example` – environment variables template
- `logs/orders.csv` – created automatically on first order

---

## Disclaimer
For educational purposes. No warranty. You are responsible for compliance with broker/exchange rules.

### Core Implementation Code & Architecture
#### File: `.venv/Lib/site-packages/streamlit/vendor/__init__.py`
```python

```

#### File: `.venv/Lib/site-packages/streamlit/vendor/ipython/__init__.py`
```python

```

#### File: `.venv/Lib/site-packages/streamlit/vendor/pympler/__init__.py`
```python

```

#### File: `.venv/Lib/site-packages/google/protobuf/testdata/__init__.py`
```python

```

#### File: `.venv/Lib/site-packages/google/protobuf/util/__init__.py`
```python

```

#### File: `.venv/Lib/site-packages/google/protobuf/pyext/__init__.py`
```python

```


==================================================


## [2/3] Repository: dhan-trading-bot (`WHEEL_dhan-trading-bot`)
- **Full Name**: `dhan-trading-bot`
- **Description**: Swing & positional equity trading bot with Piotroski F-score screening and Dhan API execution
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Swing & Positional Trading Bot

A three-layer automated trading system for Indian midcap and large cap stocks. Combines fundamental quality screening (Piotroski F-score, ROCE, management quality) with technical entry/exit timing (EMA, RSI, volume breakouts), executed through the DhanHQ API.

## Architecture

```
Layer 1: Fundamental Screener (weekly, Saturday)
  ↓ basket.json
Layer 2: Technical Signal Generator (daily, 3:45 PM IST)
  ↓ signals.json
Layer 3: Dhan Execution Engine (daily, 9:15 AM IST + intraday SL monitoring)
  ↓ positions.json
```

Each layer is independent and communicates through JSON files. This separation is deliberate — fundamentals change quarterly, technicals change daily, and execution happens in real-time.

| Layer | Runs | Where | Dhan API? | Schedule |
|-------|------|-------|-----------|----------|
| 1. Fundamental Screener | Weekly | Laptop | No | Saturday 10 AM |
| 2. Technical Scanner | Daily EOD | VPS | No | 3:45 PM IST |
| 3. Execution Engine | Market hours | VPS | Yes | 9:15 AM IST |
| 3b. SL Monitor | Every 5 min | VPS | Yes | 9:15 AM – 3:30 PM |

## Quick Start

### 1. Clone and install

```bash
git clone https://github.com/yourusername/dhan-trading-bot.git
cd dhan-trading-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure credentials

```bash
cp .env.example .env
# Edit .env with your Dhan API credentials
```

You need:
- **DHAN_CLIENT_ID** — from web.dhan.co → Profile → My Profile
- **DHAN_API_KEY** — from web.dhan.co → Profile → Access DhanHQ APIs
- **DHAN_API_SECRET** — generated with the API key (shown once)
- **DHAN_TOTP_SECRET** — from the TOTP setup in Dhan's API portal

See the [Dhan API setup guide](https://docs.dhanhq.co/) for detailed instructions.

### 3. Adjust settings

Edit `config/settings.yaml` to set:
- Capital per stock, max positions
- Piotroski minimum, ROCE threshold, max debt/equity
- Swing vs positional strategy parameters (EMAs, RSI, SL %)
- Stock universe indices (default: Nifty Midcap 150 + Nifty 100)

### 4. Run Layer 1 (on your laptop)

```bash
cd dhan-trading-bot
source venv/bin/activate
python -m src.screener
```

This screens ~250 stocks, scores them, and saves the top 15 to `data/basket.json`. Takes about 10-15 minutes (rate-limited by Screener.in).

### 5. Deploy Layers 2 & 3 (on VPS)

Push `basket.json` to your VPS:
```bash
scp data/basket.json trader@your-vps:~/dhan-trading-bot/data/
```

On the VPS:
```bash
# Download instrument master (security ID mapping)
python scripts/download_instruments.py

# Run technical scan (generates signals.json)
python -m src.technicals

# Execute signals at market open
python -m src.executor

# Start SL monitor (runs continuously)
python -m src.sl_monitor
```

### 6. Set up cron

```bash
crontab scripts/crontab
# Edit paths to match your VPS setup
```

## Project Structure

```
dhan-trading-bot/
├── config/
│   └── settings.yaml          # All thresholds and parameters
├── data/                      # JSON files (gitignored)
│   ├── basket.json            # Layer 1 output: 10-15 approved stocks
│   ├── signals.json           # Layer 2 output: buy/sell actions
│   ├── positions.json         # Layer 3 state: currently held positions
│   └── instrument_master.json # Dhan security ID mapping
├── src/
│   ├── __init__.py
│   ├── utils.py               # Config loading, logging, Telegram, file I/O
│   ├── auth.py                # Dhan OAuth + TOTP token generation
│   ├── screener.py            # Layer 1: fundamental screening
│   ├── technicals.py           # Layer 2: EOD signal generation
│   ├── executor.py             # Layer 3: order placement
│   └── sl_monitor.py          # Layer 3b: intraday SL checking
├── tests/
│   ├── test_screener.py       # Piotroski F-score tests
│   └── test_technicals.py     # Indicator and signal tests
├── scripts/
│   ├── download_instruments.py # Cache Dhan instrument master
│   └── crontab                 # Cron schedule template
├── logs/                      # Log files (gitignored)
├── .env.example                # Template for credentials
├── .gitignore
├── requirements.txt
└── README.md
```

## Strategy Details

### Layer 1: Fundamental Screening

Scans the Nifty Midcap 150 + Nifty 100 universe and scores stocks on:

| Factor | Weight | Pass criteria |
|--------|--------|---------------|
| Piotroski F-score | 25% | ≥ 7 (out of 9) |
| ROCE | 20% | ≥ 18% |
| Debt/Equity | 15% | ≤ 0.5 |
| Revenue growth (3Y CAGR) | 20% | ≥ 12% |
| Promoter holding | 10% | ≥ 50% |
| Promoter pledging | 10% | ≤ 5% |

Data source: [Screener.in](https://www.screener.in) via the `openscreener` Python library (free, no API key).

### Layer 2: Technical Timing

**Swing strategy** (2-10 day holds):
- Entry: Price breaks above 20-day high on 1.5× average volume, RSI 40-65
- Exit: Close below 10-day EMA, or RSI > 75
- Stop loss: 2% below entry (trailing)

**Positional strategy** (3-12 week holds):
- Entry: Golden cross (50 EMA > 200 EMA) or 50-day high breakout on volume
- Exit: Death cross (50 EMA < 200 EMA), or close below 200 EMA
- Stop loss: 5% below entry (trailing)

Data source: [Yahoo Finance](https://finance.yahoo.com) via the `yfinance` library (free).

### Layer 3: Dhan Execution

- Places CNC (delivery) orders via DhanHQ API
- Monitors positions every 5 minutes during market hours
- Auto-sells when SL or target is hit
- Sends Telegram alerts for every order

## Configuration

All parameters live in `config/settings.yaml`. Key sections:

```yaml
fundamental:
  min_f_score: 7           # Piotroski threshold
  min_roce: 18.0           # ROCE %
  basket_size: 15          # Number of stocks in basket

execution:
  max_positions: 8         # Max concurrent positions
  capital_per_stock: 62500 # ₹ per position

technical:
  swing:
    stop_loss_pct: 0.02    # 2% SL
    target_pct: 0.06       # 6% target
  positional:
    stop_loss_pct: 0.05    # 5% SL
    target_pct: 0.15       # 15% target
```

## VPS Setup

Recommended: **Google Cloud Platform e2-small** in `asia-south2` (Delhi).

```bash
# On the VPS:
sudo apt update && sudo apt install -y python3 python3-venv
git clone https://github.com/yourusername/dhan-trading-bot.git
cd dhan-trading-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Whitelist the VPS static IP on web.dhan.co → Profile → Access DhanHQ APIs → Static IP

# Download instrument master
python scripts/download_instruments.py

# Set up cron
crontab scripts/crontab
```

## Testing

```bash
pytest tests/ -v
```

Tests cover:
- Piotroski F-score computation (all-positive, negative income, insufficient data)
- Revenue CAGR calculation
- Safe division helper
- Technical indicator computation (column presence, RSI range)
- Swing entry/exit signal detection

## Important Notes

- **Start with paper trading.** Use Dhan's sandbox environment before going live.
- **The 2% rule.** Never risk more than 2% of total capital on a single trade.
- **SEBI compliance.** Static IP, OAuth, and TOTP are mandatory for API-based trading in India. Ensure your VPS IP is whitelisted on Dhan.
- **No investment advice.** This is infrastructure, not a trading recommendation. The Piotroski F-score and technical indicators are well-known frameworks, not proprietary edges. Backtest thoroughly before deploying real capital.

## Tech Stack

- **DhanHQ v2.2.0** — Trading API (orders, positions, market data)
- **openscreener** — Screener.in scraper for fundamental data
- **yfinance** — Yahoo Finance for price history
- **pandas** — Data manipulation and indicators
- **pyotp** — TOTP generation for Dhan auth
- **PyYAML** — Configuration management

## License

MIT

### Core Implementation Code & Architecture
#### File: `backtests/__init__.py`
```python

```

#### File: `strategies/__init__.py`
```python

```

#### File: `common/__init__.py`
```python

```

#### File: `data/signals_A.json`
```python
[]
```

#### File: `data/signals_T.json`
```python
[]
```

#### File: `data/signals_V.json`
```python
[]
```


==================================================


## [3/3] Repository: dhanhq-ts (`WHEEL_dhanhq-ts`)
- **Full Name**: `dhanhq-ts`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# DhanHQ API NodeJs client (Typescript)

## Requirements

- NodeJS v12.20.0+
- Typescript v4.9.0+

## Installation

Install via [npm](https://www.npmjs.com/package/kiteconnect)

    npm install dhanhq-ts

Or via Yarn

    yarn add dhanhq-ts

## Getting started with API

```javascript
import DhanHqClient from "dhanhq-ts";

const client: DhanHqClient = new DhanHqClient({
  accessToken: ACCESS_TOKEN,
  env: DhanEnv.PROD
});

const orderDetail = await client.getOrderById(orderId);

```

# Available API Interface in library are:

![Alt text](./docs/api_interface.png?raw=true "Api Interface")

### Core Implementation Code & Architecture
#### File: `tsconfig.build.json`
```python
{
  "extends": "./tsconfig.json",
  "exclude": [
    "./node_modules",
    "./test",
    "./dist",
    "./**/*spec.ts"
  ]
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "module": "commonjs",
    "declaration": true,
    "removeComments": true,
    "allowSyntheticDefaultImports": true,
    "target": "es2017",
    "sourceMap": false,
    "outDir": "./dist",
    "baseUrl": "./",
    "incremental": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "test", "lib", "**/*spec.ts"]
}
```

#### File: `package.json`
```python
{
  "name": "dhanhq-ts",
  "version": "1.0.1",
  "description": "DhanHQ API NodeJs Client (Typescript)",
  "main": "dist/index.js",
  "module": "dist/index.m.js",
  "unpkg": "dist/index.umd.js",
  "types": "dist/index.d.ts",
  "exports": {
    "require": "./dist/index.js",
    "default": "./dist/index.modern.js"
  },
  "scripts": {
    "build": "rm -rf dist && microbundle --tsconfig tsconfig.json --no-sourcemap",
    "dev": "microbundle --watch --tsconfig tsconfig.json --no-sourcemap",
    "tsc": "npm run tsc -w --no-initial-compille"
  },
  "author": "Vinay S",
  "repository": {
    "type": "git",
    "url": "https://github.com/vinay-sd17/dhanhq-ts"
  },
  "devDependencies": {
    "microbundle": "0.15.0"
  },
  "dependencies": {
    "isomorphic-unfetch": "^3.1.0",
    "typescript": "^4.6.3"
  },
  "files": [
    "dist"
  ]
}
```


==================================================
