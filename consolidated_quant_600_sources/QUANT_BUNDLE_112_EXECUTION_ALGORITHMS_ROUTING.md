# ⚡ [QUANT-SOURCE-112] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_112_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: trading-algoo (`WHEEL_trading-algoo`)
- **Full Name**: `trading-algoo`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Trading Bot

A backtesting engine being built from scratch, whose #1 job is **not** to find winning
strategies — it's to **stop us fooling ourselves**. Honest measurement over
impressive-looking results.

Full plan, decisions and status: **[SPEC.md](SPEC.md)** (single source of truth).

## What exists right now (P0)

- **One normalized data shape** — every data source (CSV, Binance, later anything) is
  converted to UTC timestamps + `open, high, low, close, volume` before the engine touches it.
- **Loaders** — `load_csv()` for any CSV, plus Angel One SmartAPI candle parsing for
  Indian (NSE) stock data.
- **Integrity checks** — finds the data problems that make backtests lie: gaps, duplicate
  bars, timezone mistakes, impossible candles (high below low), suspected un-adjusted
  stock splits, missing values.
- **A backtest engine** — replays history one bar at a time. A decision made on a bar can only
  execute at the *next* bar's open, which makes peeking at the future structurally impossible
  rather than merely discouraged.
- **Real Indian costs** — brokerage, STT, exchange fees, SEBI fee, stamp duty, GST and slippage,
  charged on every trade, on by default.
- **An audit log** — every trade records *why*, and every order the engine refused records why not.
- **An honest scorecard** — Sharpe, Sortino, max drawdown (and how long it lasted), win rate,
  profit factor, exposure, turnover, plus a side-by-side verdict against buy-and-hold. It attaches
  **warnings** when the evidence is too thin to believe — too few trades, a suspiciously high
  Sharpe, a drawdown you'd probably have panicked out of.
- **A full test suite** — in the repo from commit 1.

- **An anti-overfitting battery** — walk-forward testing, parameter-sensitivity heatmaps, Monte
  Carlo resampling, and a multiple-testing "luck bar" that rises every time you try another
  variant. It keeps a permanent count of every variant ever tested, because forgetting the
  failures inflates everything that follows.
- **Plug-in strategies** — MA crossover, mean reversion, breakout, plus intraday square-off
  discipline so nothing is ever held overnight.

See it work:

```powershell
.venv\Scripts\python.exe scripts\demo_backtest.py
```

- **A risk layer** — position sizing based on what you'd actually lose (not what you'd spend),
  hard exposure caps, and one-way circuit breakers. It can stop you entering; it can never
  stop you exiting.
- **A go-live gate** — a checklist that says *no* by default, splitting what code can verify
  from what only you can attest to.

Throw the whole gauntlet at every strategy:

```powershell
.venv\Scripts\python.exe scripts\run_gauntlet.py --all
```

Ask whether anything has earned real money yet (expect "not ready"):

```powershell
.venv\Scripts\python.exe scripts\go_live_check.py --strategy ma_crossover
```

## Setup (one time)

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

## Run the tests

```powershell
.venv\Scripts\python.exe -m pytest
```

## Get real NSE data (once the Angel One account is approved)

1. Create a (free) SmartAPI app at https://smartapi.angelbroking.com and enable TOTP.
2. Copy `credentials.local.example.json` → `credentials.local.json` and fill it in.
   That file is git-ignored: it stays on this computer only. **Never share its
   contents with anyone — not in chats, not with Claude.**
3. Install the broker SDK and fetch:

```powershell
.venv\Scripts\python.exe -m pip install -e ".[angelone]"
```

```powershell
.venv\Scripts\python.exe scripts\fetch_angelone_data.py --symbol RELIANCE-EQ --interval FIVE_MINUTE --days 60
```

Downloads live in `data/` (git-ignored). A synthetic sample dataset
(`data/sample_daily.csv`) is committed so tests and demos never need the internet.

## Boundaries

Claude builds, tests and hardens this system. It does **not** place trades, hold API keys,
or recommend what to buy or sell. Paper trading comes before any real money, and going
live is entirely the user's decision.

### Core Implementation Code & Architecture
#### File: `credentials.local.example.json`
```python
{
  "api_key": "PASTE-YOUR-SMARTAPI-APP-KEY",
  "client_code": "PASTE-YOUR-CLIENT-CODE",
  "pin": "PASTE-YOUR-LOGIN-PIN",
  "totp_secret": "PASTE-YOUR-TOTP-SECRET"
}
```

#### File: `engine/__init__.py`
```python
"""Market-agnostic trading backtest engine.

The engine's #1 job is not to find winning strategies — it's to stop us
fooling ourselves. See SPEC.md at the project root.
"""

__version__ = "0.1.0"
```

#### File: `engine/data/__init__.py`
```python
"""Data layer: load market data from anywhere, hand back one normalized shape."""

from engine.data.integrity import Issue, IntegrityReport, check_integrity
from engine.data.loaders import load_csv, parse_angelone_candles
from engine.data.schema import REQUIRED_COLUMNS, SchemaError, normalize, validate

__all__ = [
    "REQUIRED_COLUMNS",
    "SchemaError",
    "normalize",
    "validate",
    "Issue",
    "IntegrityReport",
    "check_integrity",
    "load_csv",
    "parse_angelone_candles",
]
```

#### File: `engine/metrics/__init__.py`
```python
"""Honest measurement: what the strategy really did, including the ugly parts."""

from engine.metrics.performance import (
    Comparison,
    PerformanceReport,
    analyze,
    compare,
    infer_periods_per_year,
)
from engine.metrics.plots import plot_equity
from engine.metrics.trades import RoundTrip, build_round_trips, trades_frame

__all__ = [
    "analyze",
    "compare",
    "infer_periods_per_year",
    "PerformanceReport",
    "Comparison",
    "RoundTrip",
    "build_round_trips",
    "trades_frame",
    "plot_equity",
]
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "trading-engine"
version = "0.1.0"
description = "Market-agnostic backtesting engine built to stop us fooling ourselves"
requires-python = ">=3.10"
dependencies = [
    "pandas>=2.1",
    "numpy>=1.24",
    "requests>=2.31",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "matplotlib>=3.8",
]
angelone = [
    "smartapi-python>=1.4",
    "pyotp>=2.9",
    # smartapi-python forgets to declare these itself:
    "logzero>=1.7",
    "websocket-client>=1.6",
]

[tool.setuptools.packages.find]
include = ["engine*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra"
```

#### File: `engine/strategies/__init__.py`
```python
"""Strategy plug-ins. The framework is the point, not these strategies."""

from engine.strategies.baselines import Breakout, MaCrossover, MeanReversion
from engine.strategies.indicators import (
    atr,
    ema,
    rolling_high,
    rolling_low,
    rsi,
    sma,
    zscore,
)
from engine.strategies.intraday import IntradayGuard
from engine.strategies.registry import (
    STRATEGIES,
    StrategySpec,
    available,
    get,
    register,
)

__all__ = [
    "MaCrossover",
    "MeanReversion",
    "Breakout",
    "IntradayGuard",
    "StrategySpec",
    "STRATEGIES",
    "available",
    "get",
    "register",
    "sma",
    "ema",
    "rsi",
    "atr",
    "rolling_high",
    "rolling_low",
    "zscore",
]
```


==================================================


## [2/3] Repository: trading-strategy-templates-python (`WHEEL_trading-strategy-templates-python`)
- **Full Name**: `trading-strategy-templates-python`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Python Trading Strategy Templates for NSE/BSE India

**Gateway to Automated Trading & Algorithmic Trading Software for Indian & Global Markets**

> **Ready-to-use Python algorithmic trading strategy templates** for Indian and global financial markets. Maintained by [**Trade Vectors LLP**](https://tradevectors.com/) — India's algorithmic trading software development company.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Trade Vectors](https://img.shields.io/badge/By-Trade%20Vectors%20LLP-purple)](https://tradevectors.com)

---

## About Trade Vectors LLP

[Trade Vectors LLP](https://tradevectors.com/) is a specialized **algorithmic trading software development company** based in India (Mumbai / Surat) and Canada with 13+ years of experience in:

* • **Custom Algorithmic Trading Software Development** — Institutional-grade automated systems for equities, futures, options, commodities, forex, and digital assets
* • **Broker API Integration Services** — Secure REST and WebSocket API integration with Interactive Brokers, MetaTrader, Angel One, Zerodha, Kotak, IC Markets, and more
* • **Trading Backtesting Software Development** — Advanced historical simulation and strategy validation engines with Sharpe ratio, drawdown, and equity curve analytics
* • **Automated Trading Consulting** — Technology consultancy for migrating manual workflows into rules-based, software-driven systems
* • **AI & Machine Learning for Trading** — Neural networks, regression models, deep learning, NLP-based news sentiment integration

> **Contact:** [contact@tradevectors.com](mailto:contact@tradevectors.com) | [Book a Free Consultation](https://tradevectors.com/book-appointment.php)

---

## Strategy Templates Included

| # | Strategy | File | Indicators | Asset Classes |
|---|---|---|---|---|
| 1 | Moving Average Crossover | `moving_average_crossover.py` | SMA 20, SMA 50 (Golden/Death Cross) | Equities, Futures, Forex |
| 2 | RSI Mean Reversion | `rsi_strategy.py` | RSI 14 (Oversold/Overbought) | Equities, Commodities, Crypto |
| 3 | MACD Momentum | `macd_strategy.py` | MACD 12/26/9, Signal Line, Histogram | Equities, Forex, Index Futures |
| 4 | Bollinger Bands Mean Reversion | `bollinger_bands_strategy.py` | BB 20,2 with %B and Bandwidth | Equities, Options Premium, Forex |
| 5 | Pairs Trading (Statistical Arbitrage) | `pairs_trading_strategy.py` | Correlation, Cointegration, Z-Score | Equities, NSE/BSE |
| 6 | 0DTE SPXW Options Writing | `0dte_spxw_options_writing_strategy.py` | Delta, Theta, Premium Thresholds | SPX Index Options (IBKR API) |

### Coming Soon
- `supertrend_strategy.py` — ATR-based Supertrend for NSE/BSE trending markets
- `options_pcr_strategy.py` — Put-Call Ratio analytics for NIFTY/BANKNIFTY
- `vwap_strategy.py` — Volume Weighted Average Price intraday strategy
- `risk_management_module.py` — Position sizing, stop-loss automation, portfolio rebalancing

---

## Supported Trading Platforms & Broker APIs

Trade Vectors builds custom trading systems for these platforms. These templates can be adapted to connect with any of the following:

### Indian Brokers & Platforms
| Broker/Platform | API Type | Asset Classes |
|---|---|---|
| **Zerodha Kite Connect** | REST + WebSocket | Equities, F&O, Commodities |
| **Angel One (AngelBroking)** | REST + WebSocket | Equities, F&O, Commodities |
| **Upstox** | REST + WebSocket | Equities, F&O |
| **Kotak Securities** | REST | Equities, F&O |
| **NEST / ODIN / Symphony** | FIX Protocol | Multi-asset |
| **Tradetron** | REST | Strategy automation |

### Global Brokers & Platforms
| Broker/Platform | API Type | Asset Classes |
|---|---|---|
| **Interactive Brokers (IBKR)** | REST + WebSocket + FIX | Equities, Forex, Futures, Options |
| **MetaTrader 5 (MT5)** | MQL5 + Python bridge | Forex, CFDs, Futures |
| **TradingView** | Pine Script + Webhooks | Multi-asset charting |
| **NinjaTrader** | C# + REST | Futures, Forex |

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/tradevectorsrobots/trading-strategy-templates-python.git
cd trading-strategy-templates-python
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run a Strategy (Example: 0DTE SPXW on IBKR)
```bash
python 0dte_spxw_options_writing_strategy.py
```

---

## Disclaimer

> Trade Vectors LLP provides **technology development and API integration services only**. These templates are for **educational and informational purposes**. We do **not** offer investment advice, portfolio management, or fund management services. All strategy design, risk management, and execution decisions remain solely with the user. Past performance does not guarantee future results. Trading involves substantial risk and may not be suitable for all investors.

Copyright 2026 Trade Vectors LLP | GSTIN: 27AAJFT1084A1ZE | India & Canada

### Core Implementation Code & Architecture
#### File: `0dte_spxw_options_writing_strategy.py`
```python
"""
0DTE SPXW Options Writing Strategy (Automated via IBKR API)
Trade Vectors | https://tradevectors.com

Strategy Logic:
- Target: SPXW (S&P 500 Weekly Options) 0DTE (Zero Days to Expiration)
- Entry: Credit Spread (Bull Put or Bear Call) or Iron Condor based on premium thresholds
- Automation: Interactive Brokers (IBKR) API (ib_insync)
"""

import logging
from ib_insync import *
import datetime

# --- CONFIGURATION ---
IB_HOST = '127.0.0.1'
IB_PORT = 7497  # Use 7496 for Live, 7497 for Paper Trading
CLIENT_ID = 10

SYMBOL = "SPX"
STRIKE_DISTANCE = 5  # Distance between spread legs
DELTA_TARGET = 0.10  # Target delta for short leg
QUANTITY = 1

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SPX0DTEStrategy:
    def __init__(self):
        self.ib = IB()

    def connect(self):
        try:
            self.ib.connect(IB_HOST, IB_PORT, clientId=CLIENT_ID)
            logging.info("Connected to IBKR API")
        except Exception as e:
            logging.error(f"Connection failed: {e}")

    def get_spxw_contract(self):
        """Fetch SPX weekly options for the current expiration."""
        spx = Index('SPX', 'CBOE')
        self.ib.qualifyContracts(spx)
        
        # Get option chains
        chains = self.ib.reqSecDefOptParams(spx.symbol, '', spx.secType, spx.conId)
        chain = next(c for c in chains if c.exchange == 'SMART')
        
        # Get 0DTE expiration (today)
        today = datetime.datetime.now().strftime('%Y%m%d')
        expirations = sorted([e for e in chain.expirations if e == today])
        
        if not expirations:
            logging.warning("No 0DTE expirations found for today.")
            return None
        
        return chain

    def place_spread_order(self, action, strike, right):
        """Place a credit spread order."""
        # This is a simplified template for demonstration
        logging.info(f"Preparing {action} {right} spread at strike {strike}")
        # In a real system, you would define the legs and use a Bag contract
        pass

    def run(self):
        self.connect()
        chain = self.get_spxw_contract()
        if chain:
            logging.info(f"Fetched option chain for {SYMBOL}")
            # Logic for selecting strikes and placing orders goes here
        
        self.ib.disconnect()

if __name__ == "__main__":
    strategy = SPX0DTEStrategy()
    strategy.run()
```

#### File: `pairs_trading_strategy.py`
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import coint, adfuller
from statsmodels.api import OLS
import warnings
warnings.filterwarnings('ignore')

class PairsTradingStrategy:
    def __init__(self, filepath, corr_threshold=0.7, pvalue_threshold=0.05):
        self.filepath = filepath
        self.corr_threshold = corr_threshold
        self.pvalue_threshold = pvalue_threshold
        self.df = None
        self.pairs_df = None

    def load_data(self):
        """Load stock price data from CSV file."""
        self.df = pd.read_csv(self.filepath, index_col=0, parse_dates=True)
        print(f"Loaded data shape: {self.df.shape}")
        return self.df

    def test_cointegration(self):
        """Test cointegration for highly correlated pairs."""
        stocks = self.df.columns
        n = len(stocks)
        pairs = []

        print("
COINTEGRATION TESTING")
        for i in range(n):
            for j in range(i + 1, n):
                stock1, stock2 = stocks[i], stocks[j]
                corr = self.df[stock1].corr(self.df[stock2])
                
                if abs(corr) < self.corr_threshold:
                    continue

                try:
                    score, pvalue, _ = coint(self.df[stock1], self.df[stock2])
                    if pvalue < self.pvalue_threshold:
                        model = OLS(self.df[stock1], self.df[stock2]).fit()
                        hedge_ratio = model.params[0]
                        spread = self.df[stock1] - hedge_ratio * self.df[stock2]
                        adf_stat, adf_pval, _, _, _, _ = adfuller(spread)

                        pairs.append({
                            'stock1': stock1, 'stock2': stock2,
                            'correlation': corr, 'coint_pvalue': pvalue,
                            'hedge_ratio': hedge_ratio, 'spread_mean': spread.mean(),
                            'spread_std': spread.std(), 'adf_pvalue': adf_pval
                        })
                except:
                    continue

        self.pairs_df = pd.DataFrame(pairs)
        print(f"Found {len(self.pairs_df)} cointegrated pairs.")
        return self.pairs_df

class PairsTradingBacktest:
    def __init__(self, df, pair_info, entry_std=1.5, exit_std=0.3, stop_loss_std=4.0):
        self.df = df
        self.stock1 = pair_info['stock1']
        self.stock2 = pair_info['stock2']
        self.hedge_ratio = pair_info['hedge_ratio']
        self.spread_mean = pair_info['spread_mean']
        self.spread_std = pair_info['spread_std']
        self.entry_std = entry_std
        self.exit_std = exit_std
        self.stop_loss_std = stop_loss_std
        self.trades = []
        self.position = None

    def run(self, initial_capital=100000):
        spread = self.df[self.stock1] - self.hedge_ratio * self.df[self.stock2]
        zscore = (spread - self.spread_mean) / self.spread_std
        capital = initial_capital

        for i in range(1, len(self.df)):
            date = self.df.index[i]
            z = zscore.iloc[i]
            p1, p2 = self.df[self.stock1].iloc[i], self.df[self.stock2].iloc[i]

            if self.position is None:
                if z > self.entry_std: # Short spread
                    self.position = {'type': 'shortspread', 'date': date, 'p1': p1, 'p2': p2, 'cap': capital * 0.5}
                elif z < -self.entry_std: # Long spread
                    self.position = {'type': 'longspread', 'date': date, 'p1': p1, 'p2': p2, 'cap': capital * 0.5}
            else:
                exit = False
                if (self.position['type'] == 'shortspread' and z < self.exit_std) or \
                   (self.position['type'] == 'longspread' and z > -self.exit_std) or \
                   abs(z) > self.stop_loss_std:
                    exit = True
                
                if exit:
                    pnl = self.calculate_pnl(p1, p2)
                    capital += pnl
                    self.trades.append({'date': date, 'pnl': pnl, 'return': (pnl/(self.position['cap']*2))*100})
                    self.position = None
        return capital

    def calculate_pnl(self, p1, p2):
        if self.position['type'] == 'shortspread':
            return self.position['cap'] * (self.position['p1'] - p1)/self.position['p1'] + \
                   self.position['cap'] * (p2 - self.position['p2'])/self.position['p2']
        else:
            return self.position['cap'] * (p1 - self.position['p1'])/self.position['p1'] + \
                   self.position['cap'] * (self.position['p2'] - p2)/self.position['p2']

if __name__ == "__main__":
    strategy = PairsTradingStrategy('stock_data.csv')
    df = strategy.load_data()
    pairs = strategy.test_cointegration()
    
    for _, pair in pairs.iterrows():
        backtester = PairsTradingBacktest(df, pair)
        final = backtester.run()
        print(f"Pair {pair['stock1']}-{pair['stock2']} Final Capital: {final:.2f}")
```

#### File: `moving_average_crossover.py`
```python
"""
Moving Average Crossover Strategy for NSE/BSE India
Trade Vectors | https://tradevectors.com

Strategy Logic:
- Buy when the short-term SMA crosses above the long-term SMA (Golden Cross)
- Sell when the short-term SMA crosses below the long-term SMA (Death Cross)

Compatible with: Zerodha Kite Connect, Upstox API
Data Source: yfinance (Yahoo Finance)
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
SYMBOL = "RELIANCE.NS"       # NSE symbol (append .NS for NSE, .BO for BSE)
START_DATE = "2023-01-01"
END_DATE = "2024-12-31"
SHORT_WINDOW = 20             # Short-term SMA period
LONG_WINDOW = 50              # Long-term SMA period
INITIAL_CAPITAL = 100000      # Starting capital in INR
# ──────────────────────────────────────────────────────────────────────────────


def fetch_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch OHLCV data from Yahoo Finance."""
    print(f"Fetching data for {symbol} from {start} to {end}...")
    df = yf.download(symbol, start=start, end=end, auto_adjust=True)
    if df.empty:
        raise ValueError(f"No data found for symbol: {symbol}")
    df.index = pd.to_datetime(df.index)
    print(f"Downloaded {len(df)} trading days.")
    return df


def compute_signals(df: pd.DataFrame, short_window: int, long_window: int) -> pd.DataFrame:
    """Compute SMA indicators and generate buy/sell signals."""
    df = df.copy()
    df["SMA_Short"] = df["Close"].rolling(window=short_window, min_periods=1).mean()
    df["SMA_Long"] = df["Close"].rolling(window=long_window, min_periods=1).mean()

    # Signal: 1 = long (hold), 0 = no position
    df["Signal"] = 0
    df.loc[df["SMA_Short"] > df["SMA_Long"], "Signal"] = 1

    # Crossover events: 1 = buy, -1 = sell
    df["Crossover"] = df["Signal"].diff()
    return df


def backtest(df: pd.DataFrame, initial_capital: float) -> pd.DataFrame:
    """Run a simple backtest on the crossover signals."""
    df = df.copy()
    position = 0
    capital = initial_capital
    shares = 0
    portfolio_values = []

    for _, row in df.iterrows():
        price = row["Close"]
        if row["Crossover"] == 1 and capital > 0:   # Buy signal
            shares = capital // price
            capital -= shares * price
            position = 1
        elif row["Crossover"] == -1 and position == 1:  # Sell signal
            capital += shares * price
            shares = 0
            position = 0
        portfolio_values.append(capital + shares * price)

    df["Portfolio_Value"] = portfolio_values
    return df


def print_performance(df: pd.DataFrame, initial_capital: float) -> None:
    """Print strategy performance metrics."""
    final_value = df["Portfolio_Value"].iloc[-1]
    total_return = ((final_value - initial_capital) / initial_capital) * 100
    buy_hold_return = ((df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]) * 100

    print("\n" + "=" * 45)
    print(" MOVING AVERAGE CROSSOVER — PERFORMANCE")
    print("=" * 45)
    print(f" Symbol          : {SYMBOL}")
    print(f" Period          : {START_DATE} to {END_DATE}")
    print(f" Short SMA       : {SHORT_WINDOW} days")
    print(f" Long SMA        : {LONG_WINDOW} days")
    print(f" Initial Capital : ₹{initial_capital:,.2f}")
    print(f" Final Value     : ₹{final_value:,.2f}")
    print(f" Strategy Return : {total_return:.2f}%")
    print(f" Buy & Hold      : {buy_hold_return:.2f}%")
    print("=" * 45)


def plot_strategy(df: pd.DataFrame) -> None:
    """Plot price, SMAs, buy/sell signals, and portfolio value."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

    ax1.plot(df.index, df["Close"], label="Close Price", color="steelblue", linewidth=1.5)
    ax1.plot(df.index, df["SMA_Short"], label=f"SMA {SHORT_WINDOW}", color="orange", linewidth=1.2)
    ax1.plot(df.index, df["SMA_Long"], label=f"SMA {LONG_WINDOW}", color="green", linewidth=1.2)

    buy_signals = df[df["Crossover"] == 1]
    sell_signals = df[df["Crossover"] == -1]
    ax1.scatter(buy_signals.index, buy_signals["Close"], marker="^", color="lime", s=100, label="Buy", zorder=5)
    ax1.scatter(sell_signals.index, sell_signals["Close"], marker="v", color="red", s=100, label="Sell", zorder=5)

    ax1.set_title(f"MA Crossover Strategy — {SYMBOL}", fontsize=14)
    ax1.set_ylabel("Price (INR)")
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(df.index, df["Portfolio_Value"], color="purple", linewidth=1.5)
    ax2.set_title("Portfolio Value Over Time")
    ax2.set_ylabel("Value (INR)")
    ax2.set_xlabel("Date")
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("ma_crossover_strategy.png", dpi=150)
    plt.show()
    print("Chart saved as ma_crossover_strategy.png")


if __name__ == "__main__":
    # 1. Fetch data
    data = fetch_data(SYMBOL, START_DATE, END_DATE)

    # 2. Compute signals
    data = compute_signals(data, SHORT_WINDOW, LONG_WINDOW)

    # 3. Backtest
    data = backtest(data, INITIAL_CAPITAL)

    # 4. Performance report
    print_performance(data, INITIAL_CAPITAL)

    # 5. Plot
    plot_strategy(data)

    # 6. Show buy/sell signal dates
    print("\nBuy signals:")
    print(data[data["Crossover"] == 1][["Close", "SMA_Short", "SMA_Long"]].to_string())
    print("\nSell signals:")
    print(data[data["Crossover"] == -1][["Close", "SMA_Short", "SMA_Long"]].to_string())

# ─── LIVE TRADING INTEGRATION (Zerodha Kite Connect) ─────────────────────────
# To use with live data, replace fetch_data() with:
#
#   from kiteconnect import KiteConnect
#   kite = KiteConnect(api_key="YOUR_API_KEY")
#   kite.set_access_token("YOUR_ACCESS_TOKEN")
#   data = kite.historical_data(instrument_token, from_date, to_date, "day")
#
# Visit https://tradevectors.com for Kite Connect integration guides.
# ─────────────────────────────────────────────────────────────────────────────
```

#### File: `bollinger_bands_strategy.py`
```python
"""
Bollinger Bands Strategy for NSE/BSE India
Trade Vectors | https://tradevectors.com

Strategy Logic:
- Buy when price touches or crosses below the Lower Bollinger Band
- Sell when price touches or crosses above the Upper Bollinger Band
- Middle Band (SMA) acts as a reference / exit level

Compatible with: Zerodha Kite Connect, Upstox API
Data Source: yfinance (Yahoo Finance)
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
SYMBOL = "TCS.NS"             # NSE symbol (.NS for NSE, .BO for BSE)
START_DATE = "2023-01-01"
END_DATE = "2024-12-31"
BB_PERIOD = 20                # Rolling window for SMA and std dev
BB_STD = 2.0                  # Number of standard deviations for bands
INITIAL_CAPITAL = 100000      # Starting capital in INR
# ──────────────────────────────────────────────────────────────────────────────


def fetch_data(symbol, start, end):
    """Fetch OHLCV data from Yahoo Finance."""
    df = yf.download(symbol, start=start, end=end, auto_adjust=True)
    if df.empty:
        raise ValueError(f"No data found for symbol: {symbol}")
    df.index = pd.to_datetime(df.index)
    return df


def compute_bollinger_bands(df, period, num_std):
    """Compute Bollinger Bands and %B indicator."""
    df = df.copy()
    df["BB_Middle"] = df["Close"].rolling(window=period).mean()
    rolling_std = df["Close"].rolling(window=period).std()
    df["BB_Upper"] = df["BB_Middle"] + (num_std * rolling_std)
    df["BB_Lower"] = df["BB_Middle"] - (num_std * rolling_std)
    df["BB_Pct"] = (df["Close"] - df["BB_Lower"]) / (df["BB_Upper"] - df["BB_Lower"])
    df["BB_Width"] = (df["BB_Upper"] - df["BB_Lower"]) / df["BB_Middle"]
    return df


def compute_signals(df):
    """Generate buy/sell signals based on Bollinger Band touches."""
    df = df.copy()
    df["Below_Lower"] = (df["Close"] < df["BB_Lower"]).astype(int)
    df["Above_Upper"] = (df["Close"] > df["BB_Upper"]).astype(int)
    df["Buy_Signal"] = df["Below_Lower"].diff().clip(lower=0)
    df["Sell_Signal"] = df["Above_Upper"].diff().clip(lower=0)
    return df


def backtest(df, initial_capital):
    """Run a simple backtest on Bollinger Band signals."""
    df = df.copy()
    position = 0
    capital = initial_capital
    shares = 0
    portfolio_values = []

    for _, row in df.iterrows():
        price = row["Close"]
        if row["Buy_Signal"] == 1 and capital > 0:
            shares = capital // price
            capital -= shares * price
            position = 1
        elif row["Sell_Signal"] == 1 and position == 1:
            capital += shares * price
            shares = 0
            position = 0
        portfolio_values.append(capital + shares * price)

    df["Portfolio_Value"] = portfolio_values
    return df


def print_performance(df, initial_capital):
    """Print strategy performance metrics."""
    final_value = df["Portfolio_Value"].iloc[-1]
    total_return = ((final_value - initial_capital) / initial_capital) * 100
    buy_hold_return = ((df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]) * 100

    print("\n" + "=" * 45)
    print(" BOLLINGER BANDS STRATEGY — PERFORMANCE")
    print("=" * 45)
    print(f" Symbol          : {SYMBOL}")
    print(f" Period          : {START_DATE} to {END_DATE}")
    print(f" BB Period       : {BB_PERIOD}")
    print(f" BB Std Dev      : {BB_STD}")
    print(f" Buy Signals     : {int(df['Buy_Signal'].sum())}")
    print(f" Sell Signals    : {int(df['Sell_Signal'].sum())}")
    print(f" Initial Capital : ₹{initial_capital:,.2f}")
    print(f" Final Value     : ₹{final_value:,.2f}")
    print(f" Strategy Return : {total_return:.2f}%")
    print(f" Buy & Hold      : {buy_hold_return:.2f}%")
    print("=" * 45)


def plot_strategy(df):
    """Plot price with Bollinger Bands, %B, and portfolio value."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12), sharex=True,
                                         gridspec_kw={"height_ratios": [3, 1.5, 1.5]})

    ax1.plot(df.index, df["Close"], label="Close Price", color="steelblue", linewidth=1.5)
    ax1.plot(df.index, df["BB_Upper"], label="Upper Band", color="red", linewidth=1, linestyle="--")
    ax1.plot(df.index, df["BB_Middle"], label=f"Middle Band (SMA {BB_PERIOD})", color="orange", linewidth=1)
    ax1.plot(df.index, df["BB_Lower"], label="Lower Band", color="green", linewidth=1, linestyle="--")
    ax1.fill_between(df.index, df["BB_Lower"], df["BB_Upper"], alpha=0.05, color="gray")

    buy_signals = df[df["Buy_Signal"] == 1]
    sell_signals = df[df["Sell_Signal"] == 1]
    ax1.scatter(buy_signals.index, buy_signals["Close"], marker="^", color="lime", s=100, label="Buy", zorder=5)
    ax1.scatter(sell_signals.index, sell_signals["Close"], marker="v", color="red", s=100, label="Sell", zorder=5)
    ax1.set_title(f"Bollinger Bands Strategy — {SYMBOL}", fontsize=14)
    ax1.set_ylabel("Price (INR)")
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(df.index, df["BB_Pct"], label="%B", color="purple", linewidth=1.2)
    ax2.axhline(1.0, color="red", linestyle="--", linewidth=1, label="Overbought (1.0)")
    ax2.axhline(0.0, color="green", linestyle="--", linewidth=1, label="Oversold (0.0)")
    ax2.set_ylabel("%B")
    ax2.legend()
    ax2.grid(alpha=0.3)

    ax3.plot(df.index, df["Portfolio_Value"], color="purple", linewidth=1.5)
    ax3.set_title("Portfolio Value Over Time")
    ax3.set_ylabel("Value (INR)")
    ax3.set_xlabel("Date")
    ax3.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("bollinger_bands_strategy.png", dpi=150)
    plt.show()
    print("Chart saved as bollinger_bands_strategy.png")


if __name__ == "__main__":
    data = fetch_data(SYMBOL, START_DATE, END_DATE)
    data = compute_bollinger_bands(data, BB_PERIOD, BB_STD)
    data = compute_signals(data)
    data = backtest(data, INITIAL_CAPITAL)
    print_performance(data, INITIAL_CAPITAL)
    plot_strategy(data)

# ─── LIVE TRADING INTEGRATION (Zerodha Kite Connect) ─────────────────────────
# Replace fetch_data() with real-time Kite Connect API calls.
# Visit https://tradevectors.com for live trading setup guides.
# ─────────────────────────────────────────────────────────────────────────────
```

#### File: `rsi_strategy.py`
```python
"""
RSI (Relative Strength Index) Strategy for NSE/BSE India
Trade Vectors | https://tradevectors.com

Strategy Logic:
- Buy when RSI crosses below the oversold threshold (default: 30)
- Sell when RSI crosses above the overbought threshold (default: 70)

Compatible with: Zerodha Kite Connect, Upstox API
Data Source: yfinance (Yahoo Finance)
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
SYMBOL = "INFY.NS"            # NSE symbol (.NS for NSE, .BO for BSE)
START_DATE = "2023-01-01"
END_DATE = "2024-12-31"
RSI_PERIOD = 14               # Lookback period for RSI calculation
OVERSOLD = 30                 # RSI level considered oversold (buy zone)
OVERBOUGHT = 70              # RSI level considered overbought (sell zone)
INITIAL_CAPITAL = 100000      # Starting capital in INR
# ──────────────────────────────────────────────────────────────────────────────


def fetch_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch OHLCV data from Yahoo Finance."""
    print(f"Fetching data for {symbol} from {start} to {end}...")
    df = yf.download(symbol, start=start, end=end, auto_adjust=True)
    if df.empty:
        raise ValueError(f"No data found for symbol: {symbol}")
    df.index = pd.to_datetime(df.index)
    print(f"Downloaded {len(df)} trading days.")
    return df


def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """Calculate RSI using Wilder's smoothing method."""
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def compute_signals(df: pd.DataFrame, period: int, oversold: int, overbought: int) -> pd.DataFrame:
    """Compute RSI and generate buy/sell signals."""
    df = df.copy()
    df["RSI"] = compute_rsi(df["Close"], period)

    # Generate signals based on RSI thresholds
    df["Signal"] = 0
    df.loc[df["RSI"] < oversold, "Signal"] = 1   # Oversold -> potential buy
    df.loc[df["RSI"] > overbought, "Signal"] = -1 # Overbought -> potential sell

    # Detect crossover events (avoid repeated signals in same zone)
    df["Position"] = df["Signal"].replace(0, np.nan).ffill().fillna(0)
    df["Trade"] = df["Position"].diff()
    return df


def backtest(df: pd.DataFrame, initial_capital: float) -> pd.DataFrame:
    """Run a simple backtest on RSI signals."""
    df = df.copy()
    position = 0
    capital = initial_capital
    shares = 0
    portfolio_values = []

    for _, row in df.iterrows():
        price = row["Close"]
        if row["Trade"] > 0 and capital > 0:    # Buy signal
            shares = capital // price
            capital -= shares * price
            position = 1
        elif row["Trade"] < 0 and position == 1:  # Sell signal
            capital += shares * price
            shares = 0
            position = 0
        portfolio_values.append(capital + shares * price)

    df["Portfolio_Value"] = portfolio_values
    return df


def print_performance(df: pd.DataFrame, initial_capital: float) -> None:
    """Print strategy performance metrics."""
    final_value = df["Portfolio_Value"].iloc[-1]
    total_return = ((final_value - initial_capital) / initial_capital) * 100
    buy_hold_return = ((df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]) * 100

    print("\n" + "=" * 45)
    print(" RSI STRATEGY — PERFORMANCE")
    print("=" * 45)
    print(f" Symbol          : {SYMBOL}")
    print(f" Period          : {START_DATE} to {END_DATE}")
    print(f" RSI Period      : {RSI_PERIOD}")
    print(f" Oversold Level  : {OVERSOLD}")
    print(f" Overbought Level: {OVERBOUGHT}")
    print(f" Initial Capital : ₹{initial_capital:,.2f}")
    print(f" Final Value     : ₹{final_value:,.2f}")
    print(f" Strategy Return : {total_return:.2f}%")
    print(f" Buy & Hold      : {buy_hold_return:.2f}%")
    print("=" * 45)


def plot_strategy(df: pd.DataFrame) -> None:
    """Plot price with buy/sell signals and RSI indicator."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12), sharex=True,
                                         gridspec_kw={"height_ratios": [3, 1.5, 1.5]})

    # Price chart
    ax1.plot(df.index, df["Close"], label="Close Price", color="steelblue", linewidth=1.5)
    buy_signals = df[df["Trade"] > 0]
    sell_signals = df[df["Trade"] < 0]
    ax1.scatter(buy_signals.index, buy_signals["Close"], marker="^", color="lime", s=100, label="Buy", zorder=5)
    ax1.scatter(sell_signals.index, sell_signals["Close"], marker="v", color="red", s=100, label="Sell", zorder=5)
    ax1.set_title(f"RSI Strategy — {SYMBOL}", fontsize=14)
    ax1.set_ylabel("Price (INR)")
    ax1.legend()
    ax1.grid(alpha=0.3)

    # RSI chart
    ax2.plot(df.index, df["RSI"], label="RSI", color="darkorange", linewidth=1.2)
    ax2.axhline(OVERBOUGHT, color="red", linestyle="--", linewidth=1, label=f"Overbought ({OVERBOUGHT})")
    ax2.axhline(OVERSOLD, color="green", linestyle="--", linewidth=1, label=f"Oversold ({OVERSOLD})")
    ax2.fill_between(df.index, OVERSOLD, df["RSI"], where=(df["RSI"] < OVERSOLD), alpha=0.2, color="green")
    ax2.fill_between(df.index, OVERBOUGHT, df["RSI"], where=(df["RSI"] > OVERBOUGHT), alpha=0.2, color="red")
    ax2.set_ylabel("RSI")
    ax2.set_ylim(0, 100)
    ax2.legend()
    ax2.grid(alpha=0.3)

    # Portfolio value
    ax3.plot(df.index, df["Portfolio_Value"], color="purple", linewidth=1.5)
    ax3.set_title("Portfolio Value Over Time")
    ax3.set_ylabel("Value (INR)")
    ax3.set_xlabel("Date")
    ax3.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("rsi_strategy.png", dpi=150)
    plt.show()
    print("Chart saved as rsi_strategy.png")


if __name__ == "__main__":
    data = fetch_data(SYMBOL, START_DATE, END_DATE)
    data = compute_signals(data, RSI_PERIOD, OVERSOLD, OVERBOUGHT)
    data = backtest(data, INITIAL_CAPITAL)
    print_performance(data, INITIAL_CAPITAL)
    plot_strategy(data)

# ─── LIVE TRADING INTEGRATION (Zerodha Kite Connect) ─────────────────────────
# Replace fetch_data() with real-time Kite Connect API calls.
# Visit https://tradevectors.com for live trading setup guides.
# ─────────────────────────────────────────────────────────────────────────────
```

#### File: `macd_strategy.py`
```python
"""
MACD (Moving Average Convergence Divergence) Strategy for NSE/BSE India
Trade Vectors | https://tradevectors.com

Strategy Logic:
- Buy when MACD line crosses above the Signal line (bullish crossover)
- Sell when MACD line crosses below the Signal line (bearish crossover)
- Optional histogram filter: only trade when histogram confirms direction

Compatible with: Zerodha Kite Connect, Upstox API
Data Source: yfinance (Yahoo Finance)
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
SYMBOL = "HDFCBANK.NS"        # NSE symbol (.NS for NSE, .BO for BSE)
START_DATE = "2023-01-01"
END_DATE = "2024-12-31"
FAST_PERIOD = 12              # Fast EMA period
SLOW_PERIOD = 26             # Slow EMA period
SIGNAL_PERIOD = 9            # Signal line EMA period
INITIAL_CAPITAL = 100000     # Starting capital in INR
# ──────────────────────────────────────────────────────────────────────────────


def fetch_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch OHLCV data from Yahoo Finance."""
    print(f"Fetching data for {symbol} from {start} to {end}...")
    df = yf.download(symbol, start=start, end=end, auto_adjust=True)
    if df.empty:
        raise ValueError(f"No data found for symbol: {symbol}")
    df.index = pd.to_datetime(df.index)
    print(f"Downloaded {len(df)} trading days.")
    return df


def compute_macd(df: pd.DataFrame, fast: int, slow: int, signal: int) -> pd.DataFrame:
    """Compute MACD line, Signal line, and Histogram."""
    df = df.copy()
    ema_fast = df["Close"].ewm(span=fast, adjust=False).mean()
    ema_slow = df["Close"].ewm(span=slow, adjust=False).mean()

    df["MACD"] = ema_fast - ema_slow
    df["Signal_Line"] = df["MACD"].ewm(span=signal, adjust=False).mean()
    df["Histogram"] = df["MACD"] - df["Signal_Line"]
    return df


def compute_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Generate buy/sell signals based on MACD crossover."""
    df = df.copy()

    # 1 when MACD above Signal, 0 when below
    df["Position"] = np.where(df["MACD"] > df["Signal_Line"], 1, 0)

    # Detect crossover: +1 = bullish (buy), -1 = bearish (sell)
    df["Crossover"] = df["Position"].diff()
    return df


def backtest(df: pd.DataFrame, initial_capital: float) -> pd.DataFrame:
    """Run a simple backtest on MACD crossover signals."""
    df = df.copy()
    position = 0
    capital = initial_capital
    shares = 0
    portfolio_values = []

    for _, row in df.iterrows():
        price = row["Close"]
        if row["Crossover"] == 1 and capital > 0:    # Buy signal
            shares = capital // price
            capital -= shares * price
            position = 1
        elif row["Crossover"] == -1 and position == 1:  # Sell signal
            capital += shares * price
            shares = 0
            position = 0
        portfolio_values.append(capital + shares * price)

    df["Portfolio_Value"] = portfolio_values
    return df


def print_performance(df: pd.DataFrame, initial_capital: float) -> None:
    """Print strategy performance metrics."""
    final_value = df["Portfolio_Value"].iloc[-1]
    total_return = ((final_value - initial_capital) / initial_capital) * 100
    buy_hold_return = ((df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]) * 100

    buy_trades = len(df[df["Crossover"] == 1])
    sell_trades = len(df[df["Crossover"] == -1])

    print("\n" + "=" * 45)
    print(" MACD STRATEGY — PERFORMANCE")
    print("=" * 45)
    print(f" Symbol          : {SYMBOL}")
    print(f" Period          : {START_DATE} to {END_DATE}")
    print(f" MACD            : {FAST_PERIOD}/{SLOW_PERIOD}/{SIGNAL_PERIOD}")
    print(f" Buy Signals     : {buy_trades}")
    print(f" Sell Signals    : {sell_trades}")
    print(f" Initial Capital : ₹{initial_capital:,.2f}")
    print(f" Final Value     : ₹{final_value:,.2f}")
    print(f" Strategy Return : {total_return:.2f}%")
    print(f" Buy & Hold      : {buy_hold_return:.2f}%")
    print("=" * 45)


def plot_strategy(df: pd.DataFrame) -> None:
    """Plot price chart, MACD indicator, and portfolio value."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12), sharex=True,
                                         gridspec_kw={"height_ratios": [3, 2, 1.5]})

    # Price chart with signals
    ax1.plot(df.index, df["Close"], label="Close Price", color="steelblue", linewidth=1.5)
    buy_signals = df[df["Crossover"] == 1]
    sell_signals = df[df["Crossover"] == -1]
    ax1.scatter(buy_signals.index, buy_signals["Close"], marker="^", color="lime", s=100, label="Buy", zorder=5)
    ax1.scatter(sell_signals.index, sell_signals["Close"], marker="v", color="red", s=100, label="Sell", zorder=5)
    ax1.set_title(f"MACD Strategy — {SYMBOL}", fontsize=14)
    ax1.set_ylabel("Price (INR)")
    ax1.legend()
    ax1.grid(alpha=0.3)

    # MACD chart
    ax2.plot(df.index, df["MACD"], label="MACD", color="blue", linewidth=1.2)
    ax2.plot(df.index, df["Signal_Line"], label="Signal Line", color="orange", linewidth=1.2)
    colors = ["green" if h >= 0 else "red" for h in df["Histogram"]]
    ax2.bar(df.index, df["Histogram"], label="Histogram", color=colors, alpha=0.5)
    ax2.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax2.set_ylabel("MACD")
    ax2.legend()
    ax2.grid(alpha=0.3)

    # Portfolio value
    ax3.plot(df.index, df["Portfolio_Value"], color="purple", linewidth=1.5)
    ax3.set_title("Portfolio Value Over Time")
    ax3.set_ylabel("Value (INR)")
    ax3.set_xlabel("Date")
    ax3.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("macd_strategy.png", dpi=150)
    plt.show()
    print("Chart saved as macd_strategy.png")


if __name__ == "__main__":
    data = fetch_data(SYMBOL, START_DATE, END_DATE)
    data = compute_macd(data, FAST_PERIOD, SLOW_PERIOD, SIGNAL_PERIOD)
    data = compute_signals(data)
    data = backtest(data, INITIAL_CAPITAL)
    print_performance(data, INITIAL_CAPITAL)
    plot_strategy(data)

    print("\nBuy signals (MACD crossover above Signal):")
    print(data[data["Crossover"] == 1][["Close", "MACD", "Signal_Line"]].to_string())
    print("\nSell signals (MACD crossover below Signal):")
    print(data[data["Crossover"] == -1][["Close", "MACD", "Signal_Line"]].to_string())

# ─── LIVE TRADING INTEGRATION (Zerodha Kite Connect) ─────────────────────────
# Replace fetch_data() with real-time Kite Connect API calls.
# Visit https://tradevectors.com for live trading setup guides.
# ─────────────────────────────────────────────────────────────────────────────
```


==================================================


## [3/3] Repository: trading-system (`WHEEL_trading-system`)
- **Full Name**: `trading-system`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Core Implementation Code & Architecture
#### File: `data/__init__.py`
```python
# data package
```

#### File: `risk/__init__.py`
```python
# risk package
```

#### File: `models/__init__.py`
```python
# models package
```

#### File: `monitor/__init__.py`
```python
# monitor package
```

#### File: `learning/__init__.py`
```python
# learning package
```

#### File: `features/__init__.py`
```python
# features package
```


==================================================
