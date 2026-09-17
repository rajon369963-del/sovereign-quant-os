# ⚡ [QUANT-SOURCE-013] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_013_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Python-for-Indian-Traders (`WHEEL_Python-for-Indian-Traders`)
- **Full Name**: `Python-for-Indian-Traders`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# GitHub companion repository for book titled:
![Python for Indian Stock Traders](https://github.com/SankarSrinivasan1/Python-for-Indian-Traders/blob/main/utils/python%201j.jpg)

## Buy the book at Amazon and leading online bookstores
[Python for Indian Stock Traders](https://www.amazon.in/Python-Indian-Stock-Traders-Analytics-ebook/dp/B0H3ZL3JF1)

# Python-for-Indian-Traders
# Trade Code NSE Python Lab

A beginner friendly Python trading lab designed for Indian stock market traders.

This repository is part of the Trade Code Series.

It helps you learn:
- NSE data handling
- Simple trading strategies
- Basic algo trading logic
- Backtesting concepts
- Zerodha Kite API integration
- Trade journaling and analytics

---

## IMPORTANT DISCLAIMER

This is an educational project only.

- Not financial advice
- Not a guaranteed profit system
- Not a production trading engine

Trading involves risk. Use paper trading first.

---

## WHY THIS REPO EXISTS

Most trading resources fall into two extremes:

1. Too theoretical (boring academic stuff)
2. Too advanced (institutional level systems)

This repo sits in the middle.

Simple.
Practical.
Beginner friendly.

---

## WHAT YOU WILL LEARN

By using this repo, you will understand:

- How trading data flows in Python
- How simple strategies are built
- How backtesting actually works
- How brokers execute orders
- How risk management is applied
- How traders track performance

---

## FOLDER GUIDE

### data/
Handles NSE data fetching and processing

### strategies/
Basic trading strategy examples

### backtest/
Simple backtesting engine for testing ideas

### broker/
Zerodha Kite API integration examples

### risk/
Position sizing and risk control tools

### dashboard/
Streamlit dashboards for trade analysis

### journal/
Trade logging and performance tracking

### notebooks/
Step by step learning notebooks

### trade_forensics_lite/
Simple trader behavior and mistake tracking tools

### utils/
Helper functions and indicators

---

## QUICK START

### 1. Install dependencies

```
pip install -r requirements.txt
```

---

### 2. Set up config

Rename:

```
config.example.py -> config.py
```

Add your API keys inside config file.

---

### 3. Run a strategy

Example:

```
python strategies/moving_average_crossover.py
```

---

### 4. Run backtest

```
python backtest/simple_backtester.py
```

---

### 5. Launch dashboard

```
streamlit run dashboard/streamlit_app.py
```

---

## KEY STRATEGIES INCLUDED

- Moving Average Crossover
- Breakout Strategy
- RSI Signal System
- Momentum Tracker

These are intentionally simple for learning.

---

## BROKER INTEGRATION

This repo includes examples using Zerodha Kite API.

You can:
- fetch live data
- place sample orders
- simulate paper trading

---

## RISK MANAGEMENT MODULE

Includes:
- position sizing calculator
- stop loss logic
- max loss control rules

Because survival matters more than strategy.

---

## TRADE JOURNAL SYSTEM

Track:
- entry price
- exit price
- profit/loss
- mistake notes

If you do not journal trades, you are basically guessing.

---

## TRADE FORENSICS LITE

A simple behavioral tracking system:

- emotional tagging
- mistake tracking
- trade review templates

This is where real improvement happens.

---

## RECOMMENDED LEARNING PATH

1. Start with notebooks
2. Try simple strategies
3. Run backtests
4. Paper trade
5. Analyze results
6. Improve slowly

Do not rush to live trading.

---

## COMMON MISTAKES TO AVOID

- Overcomplicating strategies
- Ignoring risk management
- Skipping backtesting
- Expecting instant profits
- Changing strategy daily

---

## FUTURE EXPANSION IDEAS

This repo can grow into:

- advanced AI trading modules
- portfolio optimization tools
- real-time dashboards
- machine learning strategies
- trading bot automation system

---

## CONTRIBUTION

Feel free to fork and improve.

Keep it simple and practical.

---

## PART OF

Trade Code Series

### Core Implementation Code & Architecture
#### File: `journal/export_trades.py`
```python
print("Exporting trades...")
```

#### File: `utils/helpers.py`
```python
def print_separator():
    print("-" * 50)
```

#### File: `dashboard/analytics_view.py`
```python
def show_analytics():
    print("Displaying analytics")
```

#### File: `trade_forensics_lite/mistake_tracker.py`
```python
def track_mistake(note):
    print(f"Mistake logged: {note}")
```

#### File: `trade_forensics_lite/emotional_tags.py`
```python
def tag_emotion(emotion):
    print(f"Emotion tagged: {emotion}")
```

#### File: `journal/performance_summary.py`
```python
def summary(total_profit):
    print(f"Total Profit: {total_profit}")
```


==================================================


## [2/3] Repository: nifty-breakout-lab (`VAULT_IN-QUANT-122_Raj1984__nifty-breakout-lab`)
- **Full Name**: `IN-QUANT-122_Raj1984__nifty-breakout-lab`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# 📊 NIFTY Breakout Lab — Multi-Stock 5-Min Backtest System

A **production-ready, browser-based backtesting tool** for NSE 5-minute OHLCV data.  
Upload multiple stock CSVs → get full breakout analysis across all time windows — zero installation, runs entirely in the browser.

NIFTY Breakout Lab is a production-ready, browser-based backtesting system 
for NSE 5-minute OHLCV data. Upload multiple stock CSVs simultaneously and 
run a first-breakout-of-range strategy across 10 configurable time windows 
(5 AM + 5 PM) in seconds.

Key outputs per stock:
- Total trades, overall win rate, gross points
- Best window by points and by win rate
- Top 3 windows with individual P&L
- Weakest window flagged for skipping
- Cumulative equity curves and year-wise breakdown

Built entirely in vanilla JavaScript — no Python, no server, no dependencies.
Compatible with Zerodha KiteConnect, Angel One SmartAPI, and any NSE broker 
historical data export.

![Version](https://img.shields.io/badge/version-4.0--MULTI-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-NSE%20India-orange)
![Data](https://img.shields.io/badge/data-5--min%20OHLCV-yellow)

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/nifty-breakout-lab.git
cd nifty-breakout-lab

# 2. Open the tool — NO installation needed
#    Just open the HTML file in any modern browser:
open nifty_backtest_multifile.html       # macOS
start nifty_backtest_multifile.html      # Windows
xdg-open nifty_backtest_multifile.html  # Linux

# 3. Drop your CSV files from data/ and click RUN
```

> 💡 **No Python, no server, no pip install** — it's a single self-contained HTML file.

---

## 📁 Project Structure

```
nifty-breakout-lab/
│
├── nifty_backtest_multifile.html   ← 🎯 Main tool (open this in browser)
│
├── data/
│   ├── README.md                   ← How to get & format data
│   └── sample/
│       └── LICI_5minute_sample.csv ← Demo file (20 rows, shows format)
│
├── .gitignore                      ← Excludes large CSV files from Git
└── README.md                       ← This file
```

> **Your actual CSV data files** (`NIFTY50_5minute.csv`, `TCS_5minute.csv`, etc.) go in the `data/` folder but are **excluded from Git** via `.gitignore` (they are 10–11 MB each). See [`data/README.md`](data/README.md) for how to obtain them.

---

## 🎯 What It Does

### Strategy: First Breakout of Range
For each trading day, the engine:
1. Builds a **price range** using all bars up to a configurable time window (e.g. 10:15 AM)
2. Enters **LONG** on the first bar that breaks above the range high
3. Enters **SHORT** on the first bar that breaks below the range low
4. Exits after a fixed hold duration (default: 20 min)
5. Optionally uses the opposite side of the range as Stop Loss

This is tested across **10 time windows** simultaneously:
- **AM windows:** 09:30, 09:45, 10:00, 10:15, 10:30
- **PM windows:** 14:00, 14:15, 14:30, 14:45, 15:00

---

## 📊 Dashboard Views

### 1. Stock Summary Tab
The flagship view — **one row per stock** showing:

| Column | Description |
|--------|-------------|
| **STOCK** | Name (auto-detected from filename) + date range |
| **TOTAL TRADES** | Total breakout signals across all windows |
| **OVERALL WIN RATE** | Combined win% across all 10 windows |
| **TOTAL POINTS (ALL)** | Gross PnL sum across all windows |
| **BEST WINDOW** | Highest-points window + its pts |
| **TOP 3 BY POINTS** | Top 3 windows with individual points |
| **BEST WIN RATE** | Window with highest win%, its % |
| **WEAKEST WINDOW** | Worst window — consider skipping |

Fully **sortable** (click any column), **searchable** (type stock name), with stock-wise color coding.

### 2. Compare Charts Tab
- Total points per stock (bar chart)
- Win rate: overall vs best window (overlay)
- Cross-stock window breakdown (all 10 windows × all stocks)
- Full comparison table with every window × every stock

### 3. Stock Detail Tab
Click any row in the summary to drill into a full per-stock view:
- KPI row (trades, WR, total pts, best window, price range)
- Strategy insights (top 3 windows, AM vs PM edge, best WR, weakest window)
- AM + PM window tables (n, WR%, avg PnL, avg win, avg loss, W/L ratio, total pts)
- Cumulative equity curve (per window or combined)
- Year-wise P&L table (best 4 windows × each year)

---

## ⚙️ Configuration

All parameters are set in the UI before running — no code changes needed:

| Parameter | Default | Description |
|-----------|---------|-------------|
| Hold Duration | 20 min | How long to hold after breakout entry |
| Min Range | 5 pts | Minimum range size to qualify a window |
| Session | AM + PM | Filter to AM-only, PM-only, or both |
| SL Mode | None | No SL, or use opposite range boundary |

---

## 📂 Data Requirements

**Format:** NSE 5-minute OHLCV CSV

```csv
date,open,high,low,close,volume
2022-05-17 09:15:00,872.0,875.0,870.0,873.5,3759243
2022-05-17 09:20:00,873.5,876.0,872.0,875.0,1250000
```

**Compatible sources:**
- Zerodha KiteConnect `historical_data()` API
- Angel One SmartAPI historical endpoint
- Upstox / Fyers / Shoonya / Dhan historical APIs
- Any broker providing NSE 5-min OHLCV

See [`data/README.md`](data/README.md) for detailed data fetching instructions with code.

**Tested stocks** (from `C:\Raj\app\NiftyData\10Y_5M_2015_2025\`):
```
NIFTY 50 · NIFTY BANK · TCS · LICI · HDFCBANK · MARUTI
HEROMOTOCO · LT · ULTRACEMCO · BRITANNIA · KOTAKBANK
APOLLOHOSP · ASIANPAINT · HINDUNILVR · DIVISLAB
INDUSINDBK · INFY · SHREECEM · BOSCHLTD · and more
```

---

## 🔬 Backtest Engine Details

- **Bar-by-bar simulation** — no look-ahead bias
- **Chunked async processing** — browser stays responsive during computation
- **Robust CSV parser** — handles datetime, date, timestamp column names; multiple date formats; Windows/Linux line endings
- **Session labels** — S1/S2/S3 anchors at 11:27, 13:27, 15:30 for day-type classification (TREND_UP, TREND_DOWN, LATE_REV_UP, etc.)
- **No external dependencies** — Chart.js loaded from CDN, everything else is vanilla JS

---

## 🗂️ Related Projects

This tool is part of a broader **Algorithmic Trading Suite** built for NSE markets:

| Project | Description | Stack |
|---------|-------------|-------|
| **Breakout Lab** ← You are here | Multi-stock 5-min breakout backtester | HTML + JS |
| **ML-VWAP Dashboard** | VWAP + Gap + ML (XGBoost/RF/LSTM) research paper implementations | Python + Streamlit |
| **ORB+FVG Strategy** | Opening Range Breakout + Fair Value Gap with 5 modes | Python + Zerodha KiteConnect |
| **Smart Flow Confluence** | 8-module confluence system (VWAP, RSI, PCR, IV, India VIX) | Python |
| **Agentic FnO Trader** | CrewAI-based automated FnO trading | Python + CrewAI |
| **RBI Bot v3** | Production trading bot — MACD, RSI MeanRev, CVD strategies | Python + Rich dashboard |

---

## 📈 Sample Results (LICI, 2022–2025)

> Results are **gross points only** — no commissions, no slippage, no lot size applied.  
> Always apply realistic transaction costs before trading live.

| Window | Trades | Win Rate | Total Pts |
|--------|--------|----------|-----------|
| AM 10:15 | ~1,200 | ~52–55% | Varies by stock |
| PM 14:15 | ~1,100 | ~51–54% | Varies by stock |

---

## 🚧 Limitations & Disclaimer

- **Gross PnL only** — No commissions, STT, slippage, or impact cost deducted
- **No position sizing** — Each trade = 1 unit (apply lot size externally)
- **NSE RTH only** — 09:15 to 15:30 IST, Monday–Friday
- **Past performance ≠ future results**
- This is a research/education tool — not financial advice

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| UI | Vanilla HTML5 + CSS3 (CSS variables, grid, flexbox) |
| Charts | Chart.js 4.4.1 (CDN) |
| Engine | Vanilla JavaScript (ES2020, async/await, chunked processing) |
| Fonts | IBM Plex Mono + Bebas Neue + Barlow (Google Fonts) |
| Data | Browser FileReader API — no server needed |

---

## 📝 License

MIT License — free to use, modify, and distribute.  
Attribution appreciated but not required.

---

## 🤝 Contributing

Pull requests welcome. Key areas:
- Additional exit strategies (trailing SL, target-based)
- Monthly P&L breakdown view
- CSV export of trade log per stock
- Angel One / Upstox data fetch script in `data/`

---

*Built for Indian NSE markets · 5-minute OHLCV · Breakout research*


==================================================


## [3/3] Repository: Based_trading_with_dhan_API (`WHEEL_Ai_Based_trading_with_dhan_API`)
- **Full Name**: `Ai_Based_trading_with_dhan_API`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
🚀 Quick Start
Install all required libraries

Run main.py

Provide the required data

✅ Done.

🔧 Additional Notes
You can manipulate, train, and modify the model

Customize the platform according to your own analytics and strategy requirements

### Core Implementation Code & Architecture
#### File: `keys.json`
```python
{
    "client_id": "11###53",
    "access_token": "eyJ0nRJZC FAKE KEY Example mpWn5R9BGoiw3HjUD1FfWp6-oWj60Whq8kKxEZ--gQwrDQ"
}
```

#### File: `saveState.py`
```python
import joblib


def save_state(self):
    print("save_state")
    # global data, ohlc_data, signal_history
    joblib.dump({
        "data": self.data,
        "ohlc_data": self.ohlc_data,
        "signal_history": self.signal_history
    }, self.STATE_PATH)
```

#### File: `log.py`
```python
from datetime import datetime
import tkinter as tk
    
    ####completed
def log(self, message):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        self.log_box.insert(tk.END, timestamp + " " + message + "\n")
        self.log_box.see(tk.END)
        return
```

#### File: `loadModel.py`
```python
from log import log
import os
import joblib


def load_model(self):
    print("load model")
    if os.path.exists(self.MODEL_PATH):
        self.ml_model = joblib.load(self.MODEL_PATH)
        log(self, "✅ Loaded saved ML model.")
    else:
        log(self, "⚠️ No saved model found.")


###### completed ######
```

#### File: `refreshChart.py`
```python
# commmmpltd


def refresh_chart(self):
    print("refresh_chart")
    # if self.chart_mode.get() == "live":
    #     #from evaluateSignal import evaluate_signal
    #     #evaluate_signal(self, self.ohlc_data)
    # elif self.chart_mode.get() == "backtest":
    #     from fetchHistoricalData import fetch_historical_data
    #    # df = fetch_historical_data(self)
    #   #  if not df.empty:
    #        # evaluate_signal(self, df)
```

#### File: `exportDataToCSV.py`
```python
from log import log
import pandas as pd


def export_data_to_csv(self):
    print("export_data_to_csv")
    if not self.ohlc_data.empty:
        self.ohlc_data.to_csv("historical_data.csv")
        log(self, "✅ Exported historical data to historical_data.csv")
    if self.signal_history:
        pd.DataFrame(self.signal_history, columns=["datetime", "signal"]).to_csv(
            "signals.csv", index=False)
        log(self, "✅ Exported signal history to signals.csv")
```


==================================================
