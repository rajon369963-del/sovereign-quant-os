# ⚡ [QUANT-SOURCE-016] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_016_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: DhanSetu (`WHEEL_DhanSetu`)
- **Full Name**: `DhanSetu`
- **Description**: DhanSetu is a full-stack MERN Zerodha clone featuring user authentication, dashboards, and real-time trading-style UI. Built to practice scalable architecture, clean APIs, and modern frontend–backend integration.
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

### Core Implementation Code & Architecture
#### File: `.vscode/settings.json`
```python
{
  "emmet.includeLanguages": {
    "javascript": "javascriptreact",
    "javascriptreact": "javascriptreact",
    "html": "html"
  },
  "emmet.triggerExpansionOnTab": true
}
```

#### File: `frontend/public/manifest.json`
```python
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
```

#### File: `Backend/package.json`
```python
{
  "name": "backend",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "nodemon index.js"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "devDependencies": {
    "nodemon": "^3.1.11"
  },
  "dependencies": {
    "bcrypt": "^6.0.0",
    "bcryptjs": "^3.0.3",
    "body-parser": "^2.2.2",
    "cookie-parser": "^1.4.7",
    "cors": "^2.8.6",
    "cros": "^1.1.0",
    "dotenv": "^17.3.1",
    "express": "^5.2.1",
    "jsonwebtoken": "^9.0.3",
    "mongoose": "^9.1.6",
    "passport": "^0.7.0",
    "passport-local": "^1.0.0",
    "passport-local-mongoose": "^9.0.1"
  }
}
```

#### File: `package.json`
```python
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/dom": "^10.4.1",
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-router-dom": "^7.9.6",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

#### File: `frontend/package.json`
```python
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/dom": "^10.4.1",
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^1.13.5",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-router-dom": "^6.30.3",
    "react-scripts": "5.0.1",
    "react-toastify": "^11.0.5",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

#### File: `dashboard/package.json`
```python
{
  "name": "dashboard",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@emotion/react": "^11.14.0",
    "@emotion/styled": "^11.14.1",
    "@mui/icons-material": "^5.18.0",
    "@mui/material": "^5.18.0",
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^1.13.5",
    "chart.js": "^4.5.1",
    "react": "^18.2.0",
    "react-chartjs-2": "^5.3.1",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.2",
    "react-scripts": "5.0.1",
    "uid": "^2.0.2",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```


==================================================


## [2/3] Repository: api_trading (`WHEEL_Dhan_api_trading`)
- **Full Name**: `Dhan_api_trading`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<div align="center">

# 🤖 DhanBot — Automated Options Trading Bot

### NSE F&O · NIFTY & BANKNIFTY · ATM CE/PE · DhanHQ API

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DhanHQ](https://img.shields.io/badge/DhanHQ-API%20v2-00C853?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PC9zdmc+&logoColor=white)](https://dhanhq.co)
[![WebSocket](https://img.shields.io/badge/WebSocket-Live%20Feed-FF6B35?style=for-the-badge&logo=websocket&logoColor=white)](https://dhanhq.co/docs/latest/marketfeed/)
[![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-LTP%20Fallback-720E9E?style=for-the-badge&logo=yahoo&logoColor=white)](https://finance.yahoo.com)
[![Telegram](https://img.shields.io/badge/Telegram-Alerts-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://core.telegram.org/bots)
[![Flask](https://img.shields.io/badge/Flask-Webhook-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> **Paper-trade tested · Live-ready · Institutional order-block strategy**

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Tools & Technologies](#-tools--technologies)
- [Project Structure](#-project-structure)
- [Strategies](#-strategies)
- [Signal Flow](#-signal-flow)
- [Greeks Filter](#-greeks-filter)
- [Slippage Model](#-slippage-model)
- [Quick Start](#-quick-start)
- [Configuration (.env)](#-configuration-env)
- [Running the Bot](#-running-the-bot)
- [Monitoring & Logs](#-monitoring--logs)
- [Sandbox vs Live](#-sandbox-vs-live-comparison)
- [Important Notes](#-important-notes)

---

## 🔍 Overview

**DhanBot** is a fully automated NSE F&O options trading bot built on the [DhanHQ broker API](https://dhanhq.co). It identifies institutional **Order Block** zones on 5-minute candles, confirms entry with **Bullish/Bearish Engulfing** patterns and **Breakout Trend** signals, then places ATM CE or PE orders on NIFTY and BANKNIFTY.

| Mode | File | Description |
|------|------|-------------|
| **Sandbox** | `Dhan_api.py` | Paper trading — no real money. Candle polling every 5 min. |
| **Live** | `dhan_live.py` | Real orders via DhanHQ WebSocket real-time feed. |

**What it does:**
- 🏦 Detects institutional **Order Block** zones (demand/supply)
- 🕯️ Confirms entry with **5-min Engulfing** candle pattern
- 📊 Filters options by **Black-Scholes Greeks** (Delta ≥ 0.30, Gamma ≤ 0.005)
- ⚡ Places **parallel CE + PE** orders when price is between both OB zones
- 📱 Sends real-time **Telegram alerts** for entries, exits, and EOD report
- 🔔 Accepts **TradingView webhook** alerts via Flask server
- 📈 Fetches **present market LTP** via Yahoo Finance for accurate strike selection
- 💾 Logs every tick and trade to CSV for post-session analysis

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                          │
│                                                             │
│  ┌─────────────────┐    ┌─────────────────────────────┐    │
│  │  DhanHQ API v2  │    │   Yahoo Finance Public API   │    │
│  │  /charts/intra  │    │   ^NSEI  /  ^ENSEBANK        │    │
│  │  day (5-min)    │    │   (Real-time LTP fallback)   │    │
│  └────────┬────────┘    └──────────────┬────────────────┘    │
│           │                            │                     │
│           ▼                            ▼                     │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              dhan_historical.py                       │    │
│  │   fetch_candles()  +  fetch_live_ltp()               │    │
│  │   Attempt 1: Dhan API → Attempt 2: Yahoo Finance     │    │
│  │   Attempt 3: Synthetic 5-min fallback (24 bars)      │    │
│  └────────────────────────┬────────────────────────────┘    │
└───────────────────────────┼────────────────────────────────--┘
                            │
          ┌─────────────────▼──────────────────┐
          │         SIGNAL ENGINE              │
          │                                    │
          │  greeks_options.combined_signal()  │
          │  ┌──────────────────────────────┐  │
          │  │ Step 1: OB Proximity Gate    │  │
          │  │  order_block_signal()        │  │
          │  │  → BUY / SELL / BOTH / None  │  │
          │  ├──────────────────────────────┤  │
          │  │ Step 2: Engulfing Confirm    │  │
          │  │  _bullish_engulfing()        │  │
          │  │  _bearish_engulfing()        │  │
          │  ├──────────────────────────────┤  │
          │  │ Step 3: BTF Vote             │  │
          │  │  breakout_trend_signal()     │  │
          │  └──────────────────────────────┘  │
          └─────────────────┬──────────────────┘
                            │
         ┌──────────────────┴───────────────────┐
         │                                      │
         ▼                                      ▼
┌────────────────────┐              ┌────────────────────────┐
│   SANDBOX MODE     │              │      LIVE MODE          │
│   Dhan_api.py      │              │      dhan_live.py       │
│                    │              │                         │
│ Poll every 300s    │              │ DhanHQ WebSocket        │
│ Paper orders       │              │ Real-time ticks         │
│ Slippage: 1.5%     │              │ LIMIT orders            │
│ Port: 5001         │              │ Slippage buffer: Rs.3   │
│                    │              │ Port: 5002              │
└────────┬───────────┘              └───────────┬────────────┘
         │                                      │
         ▼                                      ▼
┌──────────────────────────────────────────────────────────┐
│                   OUTPUT LAYER                            │
│  Telegram Alerts · CSV Trade Log · EOD Report · Log File  │
└──────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tools & Technologies

| Tool / Library | Version | Purpose |
|---------------|---------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) **Python** | 3.11+ | Core runtime |
| **dhanhq** | latest | DhanHQ broker SDK — order placement, history, OAuth |
| ![WebSocket](https://img.shields.io/badge/-WebSocket-FF6B35) **DhanHQ WebSocket** | MarketFeed | Real-time tick feed for live bot (`dhan_live.py`) |
| ![Yahoo Finance](https://img.shields.io/badge/-Yahoo%20Finance-720E9E?logo=yahoo) **Yahoo Finance API** | Public REST | Present LTP fallback (`^NSEI`, `^ENSEBANK`) when Dhan sandbox returns 404 |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas) **pandas** | ≥ 2.0 | OHLCV DataFrame manipulation, candle resampling |
| **numpy** | ≥ 1.26 | Numerical operations |
| **scipy** | ≥ 1.12 | Black-Scholes normal CDF (`scipy.special.ndtr`) |
| **pandas-ta** | latest | Technical indicators reference (not in active signal path) |
| ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask) **Flask** | ≥ 3.0 | TradingView webhook receiver (`/webhook` endpoint) |
| **websockets** | ≥ 12.0 | Underlying WebSocket transport for DhanHQ MarketFeed |
| **requests** | ≥ 2.31 | Telegram Bot API, Yahoo Finance, Dhan REST calls |
| ![Telegram](https://img.shields.io/badge/-Telegram-26A5E4?logo=telegram) **Telegram Bot API** | Bot API v7 | Real-time trade alerts and EOD session report |
| **python-dotenv** | ≥ 1.0 | Load secrets from `.env` file |
| **threading** | stdlib | Webhook server, tick recorder — non-blocking daemon threads |
| **math / ast** | stdlib | Black-Scholes Greeks (`math.erf`, `math.log`) |
| **csv / logging** | stdlib | Trade log CSV and rotating log file |

---

## 📁 Project Structure

```
Dhan_Execution/
│
├── Dhan_api.py                  ← SANDBOX entry point (paper trading)
├── dhan_live.py                 ← LIVE entry point  (real orders)
├── requirements.txt             ← All Python dependencies
├── .env                         ← Secrets (NOT committed — see below)
├── .gitignore
├── README.md
│
├── Scripts/                     ← Helper package
│   ├── __init__.py
│   ├── greeks_options.py        ← Black-Scholes Greeks + combined_signal()
│   ├── slippage.py              ← Slippage config + simulate_fill()
│   ├── dhan_historical.py       ← Candle fetch + Yahoo Finance LTP fallback
│   ├── tick_recorder.py         ← Thread-safe CSV tick logger
│   ├── webhook_trade.py         ← Flask webhook + execute_signal()
│   └── websocket_feed.py        ← DhanHQ MarketFeed WebSocket callback factory
│
├── Strategies/                  ← Strategy package
│   ├── __init__.py
│   ├── strategies_order_block.py    ← Order Block + Engulfing detection (PRIMARY)
│   ├── strategies_breakout_trend.py ← Breakout Trend Follower (BTF vote)
│   └── strategies_ema_rsi.py        ← EMA/RSI (DISABLED — kept for reference)
│
└── (auto-generated, git-ignored)
    ├── dhan_bot.log             ← Sandbox runtime log
    ├── dhan_live.log            ← Live runtime log
    ├── sandbox_trades.csv       ← Paper trade entries/exits
    ├── live_trades.csv          ← Live trade entries/exits
    ├── ticks_sandbox_*.csv      ← Sandbox candle records
    ├── ticks_live_*.csv         ← Live WebSocket tick records
    └── sandbox_backtest_report.txt ← EOD sandbox summary
```

---

## 📊 Strategies

### 1. Order Block Detection (`strategies_order_block.py`) — **PRIMARY HARD GATE**

Identifies institutional supply and demand zones on 5-minute candles.

```
Bullish OB:  Last RED candle before N consecutive GREEN candles
             → Demand zone (support) — look for BUY

Bearish OB:  Last GREEN candle before N consecutive RED candles
             → Supply zone (resistance) — look for SELL
```

**OB Zone dictionary:**
```python
bull_ob = { "high": ob_candle["open"],  # upper edge of demand zone
            "low" : ob_candle["low"],   # lower edge
            "avg" : (high + low) / 2 }  # midpoint
```

**Proximity check:** LTP must be **inside or within 0.5%** of the zone boundary for a signal to fire. Price NOT near any OB → **no trade** (hard gate).

**Parallel signal:** When LTP is simultaneously inside **both** a bullish and a bearish OB zone, `signal = "BOTH"` → places **CE + PE** in parallel.

---

### 2. Engulfing Candle Confirmation (`strategies_order_block.py`)

Applied to the two most recent **5-minute** bars before every entry decision.

| Pattern | Condition |
|---------|-----------|
| **Bullish Engulfing** | Prev candle red · Current candle green · Current body fully wraps prev body |
| **Bearish Engulfing** | Prev candle green · Current candle red · Current body fully wraps prev body |

> ⚠️ No trade fires unless **OB zone proximity AND matching engulfing** both confirm.

---

### 3. Breakout Trend Follower — BTF (`strategies_breakout_trend.py`) — **VOTE**

Swing breakout strategy using pivot highs/lows and a 50-period SMA filter.

```
BUY  signal: price breaks above swing high AND close > SMA-50
SELL signal: price breaks below swing low
```

BTF adds a **confirmation label** to the strategy tag when it agrees with the OB+Engulfing direction (e.g., `OB+BullEng+BTF`). It does **not** block or override the OB gate.

---

### 4. EMA / RSI — **DISABLED**

File `Strategies/strategies_ema_rsi.py` is kept for reference only. It is **never imported** in the active signal path. Monkey-patch in `Dhan_api.py` and `dhan_live.py` ensures it cannot accidentally activate.

---

## 🔄 Signal Flow

```
Every 5 minutes (sandbox poll / live candle gate):

  1.  fetch_candles()          → 5-min OHLCV DataFrame (24+ bars)
  2.  fetch_live_ltp()         → Present market LTP
        Attempt 1: Dhan /marketfeed/ltp
        Attempt 2: Yahoo Finance ^NSEI / ^ENSEBANK   ← real-time
        Attempt 3: candle close fallback

  3.  combined_signal(df, index, ltp):
        a. order_block_signal() → detect OB zones, check proximity
              near_bull AND near_bear  →  "BOTH"
              near_bull only           →  "BUY"
              near_bear only           →  "SELL"
              neither                  →  None  (NO TRADE)
        b. _bullish_engulfing() / _bearish_engulfing()
              Signal must be confirmed by matching engulfing pattern
        c. breakout_trend_signal()
              Adds "+BTF" to label if BTF agrees with direction

  4.  select_option(df_master, index, ltp, signal)
        → finds nearest ATM CE (BUY) or PE (SELL) in scrip master
        → computes Black-Scholes Delta & Gamma for filter

  5.  Greeks filter:
        |Delta| < 0.30  → skip (too OTM)
        Gamma   > 0.005 → skip (too close to expiry)

  6.  execute_signal() / _place_entry()
        → paper_order() [sandbox]  OR  place_order() [live LIMIT]
        → SL = fill * 0.95   (5% stop loss)
        → Target = fill * 1.10  (10% target)

  7.  Telegram alert + trade log CSV entry
```

---

## ⚗️ Greeks Filter

Black-Scholes Delta and Gamma computed in `Scripts/greeks_options.py` using:

- **Risk-free rate:** 6.5% (Indian repo rate)
- **Assumed IV:** 15% (ATM NIFTY typical)
- **Time to expiry (T):** derived from `SEM_EXPIRY_DATE` in scrip master

| Parameter | Threshold | Reason |
|-----------|-----------|--------|
| `\|Delta\|` | ≥ **0.30** | Skip deep OTM options (low sensitivity to underlying) |
| `Gamma` | ≤ **0.005** | Skip options near expiry (gamma risk too high) |

---

## 📉 Slippage Model

### Sandbox (`Scripts/slippage.py`)
```python
SANDBOX_SLIPPAGE_PCT = 0.015   # 1.5% of option premium per fill

BUY  fill = premium × 1.015   # pays more  (pessimistic)
SELL fill = premium × 0.985   # receives less (pessimistic)
```

| Index | ATM Premium | Slippage/fill |
|-------|-------------|--------------|
| NIFTY | ~Rs. 150 | **Rs. 2.25** |
| BANKNIFTY | ~Rs. 200 | **Rs. 3.00** |

### Live (`dhan_live.py`)
```python
SLIPPAGE_BUFFER = 3.00   # Rs. 3 added to LTP for BUY LIMIT orders

BUY  limit price = LTP + Rs.3   (ensures fill in rising market)
SELL limit price = LTP − Rs.3   (floor at Rs.0.05)
```
If actual slippage exceeds `3 × buffer`, a high-slippage Telegram alert fires automatically.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- DhanHQ account with sandbox + live access
- Telegram Bot Token and Chat ID
- `.env` file with credentials (see below)

### Install Dependencies

```bash
git clone https://github.com/tejak6958/Dhan_api_trading.git
cd Dhan_api_trading
pip install -r requirements.txt
```

### Create `.env` File

```env
CLIENT_ID       = "your_dhan_client_id"
ACCESS_TOKEN    = "your_dhan_access_token"
BOT_TOKEN       = "your_telegram_bot_token"
CHAT_ID         = your_telegram_chat_id
TOKEN_TYPE      = "api"          # "api" = 30-day token | "web" = 24-hour token
TOKEN_ISSUED_AT = "2026-05-07T09:00:00"   # only needed if TOKEN_TYPE=web
```

> ⚠️ Never commit `.env` to GitHub. It is already in `.gitignore`.

---

## ⚙️ Configuration (.env)

| Variable | Description | Example |
|----------|-------------|---------|
| `CLIENT_ID` | DhanHQ client/user ID | `"2508191356"` |
| `ACCESS_TOKEN` | DhanHQ JWT access token | `"eyJhbG..."` |
| `BOT_TOKEN` | Telegram bot token from [@BotFather](https://t.me/BotFather) | `"8422359342:AAF..."` |
| `CHAT_ID` | Telegram chat ID to receive alerts | `1932823870` |
| `TOKEN_TYPE` | `api` (30-day) or `web` (24-hour) | `"api"` |
| `TOKEN_ISSUED_AT` | ISO timestamp of token creation (web only) | `"2026-05-07T09:00:00"` |

**Key constants (edit in source if needed):**

| File | Constant | Default | Description |
|------|----------|---------|-------------|
| `Dhan_api.py` | `POLL_SLEEP` | `300` | Sandbox poll interval in seconds (5 min) |
| `Dhan_api.py` | `WEBHOOK_PORT` | `5001` | Flask webhook port (sandbox) |
| `dhan_live.py` | `CANDLE_TICKS` | `300` | WebSocket ticks per candle gate (5 min) |
| `dhan_live.py` | `MAX_DAILY_LOSS` | `-15000` | Hard stop in Rs. per day |
| `dhan_live.py` | `SLIPPAGE_BUFFER` | `3.00` | LIMIT order Rs. buffer |
| `dhan_live.py` | `WEBHOOK_PORT` | `5002` | Flask webhook port (live) |
| `slippage.py` | `SANDBOX_SLIPPAGE_PCT` | `0.015` | 1.5% paper slippage |
| `strategies_order_block.py` | `OB_PERIODS` | `5` | Candles needed to validate OB |

---

## ▶️ Running the Bot

### Sandbox (Paper Trading — No Real Money)

```bash
python Dhan_api.py
```

- Runs during NSE market hours: **09:15 – 15:30 IST, Mon–Fri**
- Pre-market: waits automatically and prints countdown
- Generates `sandbox_backtest_report.txt` + Telegram EOD summary at 15:30

### Live (Real Orders — Real Money)

> ⚠️ **Complete at least 5–10 sandbox sessions before going live.**

```bash
python dhan_live.py
```

- Connects to DhanHQ WebSocket for real-time ticks
- Places real LIMIT orders on NSE F&O
- Emergency stop: create a file named `STOP` in the project folder
- Daily loss limit: Rs.15,000 (configurable via `MAX_DAILY_LOSS`)

### TradingView Webhook

Send a POST request to `http://your-server:5001/webhook` (sandbox) or `:5002/webhook` (live):

```json
{
  "index":    "NIFTY",
  "signal":   "BUY",
  "ltp":      24500.00,
  "strategy": "TradingView"
}
```

Health check: `GET http://localhost:5001/` · Status: `GET http://localhost:5001/status`

---

## 📡 Monitoring & Logs

| File | Contents | Updated |
|------|----------|---------|
| `dhan_bot.log` | All sandbox events, errors, signals | Every poll cycle |
| `dhan_live.log` | All live events, order fills, errors | Every WebSocket tick gate |
| `sandbox_trades.csv` | Entry/exit/PnL rows (sandbox) | Per trade |
| `live_trades.csv` | Entry/exit/PnL rows (live) | Per trade |
| `ticks_sandbox_YYYYMMDD.csv` | 5-min candle bars recorded | Per poll |
| `ticks_live_YYYYMMDD.csv` | Individual WebSocket ticks | Per tick |

**Key log prefixes to watch:**

```
[LTP DHAN]   → Dhan API LTP fetched successfully
[LTP YAHOO]  → Yahoo Finance LTP used (Dhan failed)
[OB]         → Order Block zone detected / proximity check
[SIGNAL]     → combined_signal() output
[PAPER]      → Paper order placed (sandbox)
[SLIPPAGE]   → Fill vs signal LTP comparison
[WEBHOOK]    → TradingView alert received
[WS FEED]    → WebSocket subscription status (live)
```

---

## 📊 Sandbox vs Live Comparison

| Aspect | Sandbox (`Dhan_api.py`) | Live (`dhan_live.py`) |
|--------|------------------------|----------------------|
| **Data feed** | Candle poll every 300s | DhanHQ WebSocket real-time |
| **Candle data** | Dhan API → Yahoo LTP → Synthetic | Rolling WebSocket tick buffer |
| **LTP for strikes** | Yahoo Finance (real-time) | WebSocket `last_traded_price` |
| **Order execution** | Paper only — no real money | Real LIMIT orders via Dhan API |
| **Slippage** | 1.5% on option premium | Rs.3 buffer on LIMIT price |
| **SL / Target** | 5% / 10% on option fill | 5% / 10% on option fill |
| **Engulfing gate** | `combined_signal()` | `websocket_feed.on_message()` |
| **OB hard gate** | `process_index()` | `websocket_feed.on_message()` |
| **Daily loss limit** | None (paper mode) | Rs.15,000/day hard stop |
| **EOD exit** | `run_backtest_report()` at 15:30 | Force-exit at 15:25 |
| **Webhook port** | 5001 | 5002 |
| **Log file** | `dhan_bot.log` | `dhan_live.log` |
| **Tick CSV** | `ticks_sandbox_YYYYMMDD.csv` | `ticks_live_YYYYMMDD.csv` |
| **Reconnect** | N/A (polling) | Auto-reconnect after 30s |
| **STOP file** | Not supported | `STOP` file triggers clean shutdown |

---

## ⚠️ Important Notes

### Sandbox API Limitations (Dhan)
- `/charts/intraday` returns **HTTP 500** for `IDX_I` (index) instruments — known limitation
- `/marketfeed/ltp` returns **HTTP 404** for index LTP in sandbox
- **Workaround:** Bot automatically falls back to Yahoo Finance for real LTP, and generates realistic 5-min synthetic candles for strategy testing

### Stop Loss Behaviour
- SL = **5% of option fill price** (not underlying index)
- ATM NIFTY ~Rs.150 → SL at Rs.142.50 (~12 NIFTY pts adverse move)
- In sandbox: synthetic random-walk data causes more SL hits than live
- In live: OB zone + engulfing entries have higher probability of respecting the zone

### Parallel Signal (BOTH)
- When NIFTY price is simultaneously near a **bullish OB** and a **bearish OB** (range-bound):
  - Bot places **both CE and PE** options simultaneously
  - Profits from whichever direction breaks out
  - Strategy label: `OB+Engulfing|BOTH`

### Token Management
- Use `TOKEN_TYPE=api` in `.env` for the **30-day API token** (recommended for live)
- `web` tokens expire in **24 hours** — bot warns when < 2 hours remain and blocks live start if expired

### Risk Disclaimer
> This bot is for **educational and research purposes**. Options trading involves
> substantial risk of loss. **Always test in sandbox first.** The authors are not
> responsible for any financial losses. Never risk money you cannot afford to lose.

---

## 📦 Dependencies

```txt
dhanhq          # DhanHQ broker SDK
pandas          # DataFrame and candle processing
numpy           # Numerical operations
scipy           # Black-Scholes normal CDF
pandas_ta       # Technical indicators (reference)
requests        # HTTP calls (Telegram, Yahoo Finance, Dhan REST)
python-dotenv   # Load .env credentials
flask           # TradingView webhook receiver
websockets      # DhanHQ WebSocket live feed transport
```

Install all:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: description"`
4. Push and open a Pull Request

---

<div align="center">

**Built with ❤️ for algorithmic trading on Indian markets**

[![GitHub](https://img.shields.io/badge/GitHub-tejak6958-181717?style=for-the-badge&logo=github)](https://github.com/tejak6958/Dhan_api_trading)

</div>

### Core Implementation Code & Architecture
#### File: `Scripts/__init__.py`
```python
"""
Scripts package — DhanBot helper modules.

Making this an explicit Python package (via __init__.py) ensures:
  1. Reliable absolute imports from any working directory
     (e.g. `from Scripts.greeks_options import combined_signal`)
  2. Prevents Python from silently picking a wrong namespace
     package if another 'Scripts' directory appears on sys.path.
  3. IDEs (PyCharm, VS Code) and linters (pylint, flake8, mypy)
     treat the folder as a proper package for code-completion
     and type-checking.
  4. pytest discovers test modules correctly when tests live
     alongside package code.
  5. Enables relative imports within the package if needed in future.

Modules:
    greeks_options   — Black-Scholes Greeks, ATM option selector,
                       combined_signal aggregator
    slippage         — Sandbox slippage config & paper-fill simulator
    dhan_historical  — Historical + live-LTP fetch for sandbox polling
    tick_recorder    — Thread-safe CSV tick recorder (sandbox + live)
    webhook_trade    — Flask webhook receiver + core execute_signal()
    websocket_feed   — DhanHQ MarketFeed WebSocket callback factory
"""
```

#### File: `Strategies/strategies_ema_rsi.py`
```python
"""
EMA/RSI Momentum Strategy

Combines Exponential Moving Average (EMA) crossover with Relative Strength Index (RSI).
- BUY: EMA-20 > EMA-50 AND RSI > 55
- SELL: EMA-20 < EMA-50 AND RSI < 45
"""

import pandas as pd
import pandas_ta as ta


def ema_rsi_signal(df: pd.DataFrame):
    """
    EMA/RSI momentum confirmation signal.
    Returns 'BUY', 'SELL', or None.
    """
    d = df.copy()
    d["ema20"] = ta.ema(d["close"], length=20)
    d["ema50"] = ta.ema(d["close"], length=50)
    d["rsi"] = ta.rsi(d["close"], length=14)
    d.dropna(inplace=True)
    if d.empty:
        return None
    last = d.iloc[-1]
    if last["ema20"] > last["ema50"] and last["rsi"] > 55:
        return "BUY"
    if last["ema20"] < last["ema50"] and last["rsi"] < 45:
        return "SELL"
    return None


def ema_rsi_confirmation(df: pd.DataFrame, index: str, ltp: float):
    """
    Evaluate EMA/RSI confirmation signal.
    Returns signal ('BUY', 'SELL', or None).
    """
    er_sig = ema_rsi_signal(df)

    if er_sig == "BUY":
        print(f"[EMA/RSI] {index}  → BUY vote")
    elif er_sig == "SELL":
        print(f"[EMA/RSI] {index}  → SELL vote")

    return er_sig
```

#### File: `Strategies/__init__.py`
```python
"""
Strategies package — DhanBot trading strategy modules.

Making this an explicit Python package (via __init__.py) ensures:
  1. Reliable absolute imports from any working directory
     (e.g. `from Strategies.strategies_order_block import order_block_signal`)
  2. Prevents Python from silently picking a wrong namespace
     package if another 'Strategies' directory appears on sys.path.
  3. IDEs (PyCharm, VS Code) and linters (pylint, flake8, mypy)
     treat the folder as a proper package for code-completion
     and type-checking.
  4. pytest discovers test modules correctly when tests live
     alongside package code.
  5. Enables relative imports within the package if needed in future.

Modules:
    strategies_order_block      — Institutional Order Block detection
                                  (bullish/bearish OB + engulfing patterns).
                                  Primary hard-gate signal source in
                                  greeks_options.combined_signal().
    strategies_breakout_trend   — Swing breakout + MA trend-filter strategy
                                  (BTF). Used as a confirmation vote
                                  alongside the Order Block gate.
    strategies_ema_rsi          — EMA/RSI strategy (DISABLED per [Item vii]).
                                  Kept for reference / future re-activation.
"""
```

#### File: `Strategies/strategies_breakout_trend.py`
```python
"""
Breakout Trend Follower Strategy (Python port of Pine Breakout_Trend_follower.txt)

Identifies swing breakouts and uses MA filter for trend confirmation.
- BUY: price breaks above swing high AND close > MA
- SELL: price breaks below swing low (trailing stop)
"""

import pandas as pd

# Configuration
BTF_PVT_LEN = 3         # pivot look-back / look-forward periods
BTF_MA_LEN = 50         # MA period for trend filter
BTF_MA_TYPE = "SMA"     # "SMA" or "EMA"


def pivot_high(highs, pvt_len: int = BTF_PVT_LEN):
    """Return most recent confirmed swing high value."""
    if len(highs) < 2 * pvt_len + 1:
        return None
    for i in range(len(highs) - pvt_len - 1, pvt_len - 1, -1):
        if all(highs[i] >= highs[i - j] for j in range(1, pvt_len + 1)) and \
           all(highs[i] >= highs[i + j] for j in range(1, pvt_len + 1)):
            return highs[i]
    return None


def pivot_low(lows, pvt_len: int = BTF_PVT_LEN):
    """Return most recent confirmed swing low value."""
    if len(lows) < 2 * pvt_len + 1:
        return None
    for i in range(len(lows) - pvt_len - 1, pvt_len - 1, -1):
        if all(lows[i] <= lows[i - j] for j in range(1, pvt_len + 1)) and \
           all(lows[i] <= lows[i + j] for j in range(1, pvt_len + 1)):
            return lows[i]
    return None


def btf_signal(df: pd.DataFrame) -> tuple:
    """
    Breakout Trend Follower signal.
    Returns (signal, buy_level, stop_level) where signal is 'BUY'/'SELL'/None.
    Logic:
      - BUY  when high > swing_high AND close > MA filter
      - SELL when low  < swing_low  (trailing stop)
    """
    if len(df) < BTF_MA_LEN + 2 * BTF_PVT_LEN + 2:
        return None, None, None

    closes = df["close"].tolist()
    highs = df["high"].tolist()
    lows = df["low"].tolist()

    # MA filter
    if BTF_MA_TYPE == "EMA":
        ma_val = df["close"].ewm(span=BTF_MA_LEN, adjust=False).mean().iloc[-1]
    else:
        ma_val = df["close"].rolling(BTF_MA_LEN).mean().iloc[-1]

    buy_level = pivot_high(highs)
    stop_level = pivot_low(lows)

    if buy_level is None or stop_level is None:
        return None, buy_level, stop_level

    last_high = highs[-1]
    last_low = lows[-1]
    last_close = closes[-1]

    if last_high > buy_level and last_close > ma_val:
        return "BUY", buy_level, stop_level
    if last_low < stop_level:
        return "SELL", buy_level, stop_level
    return None, buy_level, stop_level


def breakout_trend_signal(df: pd.DataFrame, index: str, ltp: float):
    """
    Evaluate Breakout Trend Follower signal.
    Returns (signal, buy_level, stop_level).
    """
    btf_sig, buy_lvl, stop_lvl = btf_signal(df)

    if btf_sig == "BUY":
        print(f"[BTF] {index}: Breakout above {buy_lvl:.1f}  → BUY vote")
    elif btf_sig == "SELL":
        print(f"[BTF] {index}: Breakdown below {stop_lvl:.1f}  → SELL vote")

    return btf_sig, buy_lvl, stop_lvl
```

#### File: `Scripts/tick_recorder.py`
```python
"""
==============================================================
  DhanBot / tick_recorder.py
  [Item v] TICK DATA RECORDER

  Used in BOTH Dhan_api.py (sandbox) AND dhan_live.py (live).

  ITEM viii ANSWER — Should this be in dhan_live.py? YES.
  In live mode, record_tick() captures every WebSocket tick
  (~1/sec), which is far more valuable than 1-min candle bars:
    - Validates whether SL was hit between candle closes
    - Enables slippage analysis (signal LTP vs actual fill)
    - Provides real market data for strategy refinement
  Runs in daemon threads so zero impact on order latency.

  SANDBOX usage:
    tick_rec = TickRecorder(mode="sandbox")
    tick_rec.record_candles(index, df)    # after fetch_candles()

  LIVE usage:
    tick_rec = TickRecorder(mode="live")
    tick_rec.record_tick(index, ltp, open_p, high_p, low_p)
                                           # inside on_message()
==============================================================
"""

import os
import csv
import threading
from datetime import datetime


class TickRecorder:
    """
    Thread-safe local CSV tick recorder for sandbox and live bots.

    File naming:
        ticks_sandbox_YYYYMMDD.csv   <- sandbox bot
        ticks_live_YYYYMMDD.csv      <- live bot
    Rolls over to a new file automatically each trading day.
    """

    def __init__(self, mode: str = "sandbox", output_dir: str = "."):
        self.mode       = mode.lower()
        self.output_dir = output_dir
        self._lock      = threading.Lock()
        self._csv_path  = None
        self._ready     = False
        self._init_csv()

    # ------------------------------------------------------------------ init

    def _build_path(self) -> str:
        today = datetime.now().strftime("%Y%m%d")
        return os.path.join(self.output_dir,
                            f"ticks_{self.mode}_{today}.csv")

    def _init_csv(self):
        path = self._build_path()
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([
                    "timestamp", "index", "open", "high",
                    "low", "close", "volume", "source"
                ])
        self._csv_path = path
        self._ready    = True
        print(f"[TickRecorder] Initialised -> {path}")

    def _ensure_daily_rollover(self):
        if self._build_path() != self._csv_path:
            self._ready = False
            self._init_csv()

    # ------------------------------------------------------------------ API

    def record_tick(self, index: str, ltp: float,
                    open_p: float = None, high_p: float = None,
                    low_p: float  = None, volume: int = 0):
        """
        Record a single WebSocket tick (live mode).
        Non-blocking — spawns daemon thread.
        """
        if not self._ready:
            return
        self._ensure_daily_rollover()
        ts  = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        row = [
            ts, index,
            open_p if open_p is not None else ltp,
            high_p if high_p is not None else ltp,
            low_p  if low_p  is not None else ltp,
            ltp, volume, "websocket"
        ]
        threading.Thread(target=self._write_row,
                         args=(row,), daemon=True).start()

    def record_candles(self, index: str, df):
        """
        Append all rows from a candle poll DataFrame (sandbox mode).
        Non-blocking — spawns daemon thread.
        """
        if not self._ready or df is None or df.empty:
            return
        self._ensure_daily_rollover()

        def _write():
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with self._lock:
                with open(self._csv_path, "a", newline="",
                          encoding="utf-8") as f:
                    w = csv.writer(f)
                    for _, row in df.iterrows():
                        w.writerow([
                            ts, index,
                            row.get("open",   ""),
                            row.get("high",   ""),
                            row.get("low",    ""),
                            row.get("close",  ""),
                            row.get("volume", 0),
                            "candle_poll"
                        ])
        threading.Thread(target=_write, daemon=True).start()

    def _write_row(self, row: list):
        with self._lock:
            with open(self._csv_path, "a", newline="",
                      encoding="utf-8") as f:
                csv.writer(f).writerow(row)

    @property
    def csv_path(self) -> str:
        return self._csv_path or ""
```

#### File: `Scripts/slippage.py`
```python
"""
==============================================================
  DhanBot / slippage.py
  [Item ii] SLIPPAGE CONFIG + OPTION PREMIUM FETCHER
            + PAPER FILL SIMULATOR

  Used by Dhan_api.py (sandbox) for paper trade simulation.
  dhan_live.py has its own real-fill fetcher (_fetch_fill_price)
  and uses SLIPPAGE_BUFFER for limit order pricing instead.
==============================================================
"""

import logging

import requests

logger = logging.getLogger("DhanBot")

# ── SLIPPAGE CONFIG ───────────────────────────────────────────
#
# SANDBOX_SLIPPAGE_PCT:
#   Applied to option PREMIUM price (not underlying index LTP).
#   BUY  -> fill = premium * (1 + SANDBOX_SLIPPAGE_PCT)  [pays more]
#   SELL -> fill = premium * (1 - SANDBOX_SLIPPAGE_PCT)  [receives less]
#
#   0.005 = 0.5%  <- old default
#   0.010 = 1.0%  <- current [Item ii]: conservative / worst-case testing
#
# WHY APPLY TO OPTION PREMIUM, NOT UNDERLYING:
#   Wrong: underlying LTP = Rs.48,040 -> 0.5% slip = Rs.240
#          (absurd; option itself costs Rs.200 total)
#   Right: option premium = Rs.200    -> 0.5% slip = Rs.1.00
#          (realistic bid-ask spread on ATM option)
#
SANDBOX_SLIPPAGE_PCT = 0.015  # [Item ii] raised: 0.5% → 1.0% → 1.5%
# ATM NIFTY option ~Rs.150 → slip = Rs.2.25/fill
# ATM BANKNIFTY option ~Rs.200 → slip = Rs.3.00/fill
# Realistic for typical NSE FnO bid-ask spread

# Fallback option premium when sandbox API is unavailable
_FALLBACK_PREMIUM = {
    "NIFTY": 150.0,
    "BANKNIFTY": 200.0,
}


# ── OPTION PREMIUM FETCHER ────────────────────────────────────


def fetch_option_premium(
    opt_sid: str, index: str, sandbox_base_url: str, access_token: str, client_id: str
) -> float:
    """
    Fetch the OPTION's own market price (LTP) from Dhan quote API.
    Used so slippage is applied to the option premium, not the index.

    Sandbox often fails on this endpoint; falls back to a hardcoded
    realistic estimate so simulation stays meaningful.

    Args:
        opt_sid          : option security ID string
        index            : "NIFTY" or "BANKNIFTY" (for fallback lookup)
        sandbox_base_url : e.g. https://sandbox.dhan.co/v2
        access_token     : from .env
        client_id        : from .env

    Returns:
        float option LTP, or fallback premium if fetch fails
    """
    try:
        url = f"{sandbox_base_url}/marketfeed/ltp"
        headers = {
            "access-token": access_token,
            "client-id": client_id,
            "Content-Type": "application/json",
        }
        r = requests.post(
            url, json={"NSE_FNO": [int(opt_sid)]}, headers=headers, timeout=5
        )
        r.raise_for_status()
        data = r.json()
        ltp_val = (
            data.get("data", {})
            .get("NSE_FNO", {})
            .get(str(opt_sid), {})
            .get("last_price", 0)
        )
        if ltp_val and float(ltp_val) > 0:
            logger.info(f"[OPT PREMIUM] sid={opt_sid} LTP=Rs.{ltp_val:.2f}")
            return float(ltp_val)
    except Exception as e:
        logger.info(f"[OPT PREMIUM] fetch failed sid={opt_sid}: {e}")

    fallback = _FALLBACK_PREMIUM.get(index, 200.0)
    logger.info(f"[OPT PREMIUM] Using fallback Rs.{fallback:.0f} (sid={opt_sid})")
    return fallback


# ── PAPER FILL SIMULATOR ──────────────────────────────────────


def simulate_fill(
    ltp: float, side: str, slippage_pct: float = SANDBOX_SLIPPAGE_PCT
) -> float:
    """
    Simulate a realistic fill price for sandbox paper trades.

    WHY: Real MARKET orders fill worse than signal LTP due to
    bid-ask spread. Without this, sandbox PnL is overstated and
    strategies will look more profitable than they are in live trading.

    BUY  -> fill = ltp * (1 + slippage_pct)   [pays more — pessimistic]
    SELL -> fill = ltp * (1 - slippage_pct)   [receives less — pessimistic]

    Args:
        ltp          : option premium at signal time (NOT underlying LTP)
        side         : "BUY" or "SELL"
        slippage_pct : override default if needed (default SANDBOX_SLIPPAGE_PCT)

    Returns:
        float simulated fill price
    """
    if side == "BUY":
        fill = round(ltp * (1 + slippage_pct), 2)
    else:
        fill = round(ltp * (1 - slippage_pct), 2)

    slip = round(fill - ltp, 2)
    logger.info(
        f"[SLIPPAGE SIM] {side} | signal_ltp={ltp:.2f} "
        f"fill={fill:.2f} slippage={slip:+.2f} "
        f"({slippage_pct * 100:.1f}%)"
    )
    return fill
```


==================================================


## [3/3] Repository: automation1 (`WHEEL_Dhan_automation1`)
- **Full Name**: `Dhan_automation1`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Dhan_automation1
Automated trading strategy using Dhan API

### Core Implementation Code & Architecture
#### File: `app.py`
```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Dhan Automation is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
```


==================================================
