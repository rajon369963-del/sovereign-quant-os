# ⚡ [QUANT-SOURCE-108] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_108_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: adheera-algo-trader (`WHEEL_adheera-algo-trader`)
- **Full Name**: `adheera-algo-trader`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# adheera-algo-trader
Python app for NSE algo-trading. Uses LLM for predictions &amp; news analysis, along with technical indicators for buy/sell signals.  #algo-trading #python #NSE #AI #gpt-4 #gemini

### Core Implementation Code & Architecture
#### File: `algo_trader.py`
```python
import requests
import pandas as pd
import yfinance as yf
# from ta.trend import SMAIndicator
import talib
import datetime
from tqdm import tqdm


def fetch_nse_stocks():
    # Fetch list of stocks from NSE
    response = requests.get('https://api.kite.trade/instruments')
    # Parse the response as a CSV file and create a pandas DataFrame
    stocks = pd.DataFrame([line.split(',') for line in response.text.split('\n')])
    stocks.columns = stocks.iloc[0]
    stocks = stocks[1:]
   
    
    nse_stocks = stocks[stocks.segment == 'NSE']
    return nse_stocks

def get_history_data(symbol):
    # Fetch historical data for the given symbol
    data = yf.download(symbol, start="2022-01-01", end="2024-12-31", progress=False)
    return data

def pattern_analysis(symbol):
    print(f"------------ Pattern analysis for symbol: {symbol} -----------------", end="\n")
    # Getting historical data from yahoo finance
    hist_data = get_history_data(symbol)
    print("Historical data size:", hist_data.shape)
    if hist_data.shape[0] < 90:
        print("Insufficient data for analysis: expected at least 90 days of data.")
        return None
    
    # Create a list to store the data
    patterns_recognised = []
    rsi_trend = ""
    macd_trend = ""
    sma_value = 0.0
    wma_value = 0.0
    obv_value = 0.0

    pattern_names = talib.get_function_groups()['Pattern Recognition']
    for pattern_name in pattern_names:
        pattern = getattr(talib, pattern_name)
        patterns = pattern(hist_data['Open'], hist_data['High'], hist_data['Low'], hist_data['Close'])
        pattern_dates = hist_data.index[patterns != 0]
        today = datetime.date.today()
        last_five_days = [today - datetime.timedelta(days=i) for i in range(5)]
        for pattern_date in pattern_dates:
            if pattern_date.date() in last_five_days:
                patterns_recognised.append(pattern_name)

    # Calculate MACD
    macd, signal, hist = talib.MACD(hist_data['Close'])
    if macd[-1] > signal[-1]:
        macd_trend = "UP"
    elif macd[-1] < signal[-1]:
        macd_trend = "DOWN"
    else:
        macd_trend = "Sideways"

    # Calculate RSI
    rsi = talib.RSI(hist_data['Close'])
    if rsi[-1] > 70:
        rsi_trend = "UP"
    elif rsi[-1] < 30:
        rsi_trend = "DOWN"
    else:
        rsi_trend = "Sideways"

    # Calculate SMA
    sma = talib.SMA(hist_data['Close'], timeperiod=14)
    sma_value = sma[-1]

    # Calculate WMA
    wma = talib.WMA(hist_data['Close'], timeperiod=14)
    wma_value = wma[-1]

    # Calculate OBV
    obv = talib.OBV(hist_data['Close'], hist_data['Volume'])
    obv_value = obv[-1]

    # Return the analysis results as a list
    return [symbol, patterns_recognised, rsi_trend, macd_trend, sma_value, wma_value, obv_value]


def pattern_analysis_old(symbol):
    print(f"------------ Pattern analysis for symbol: {symbol} -----------------", end="\n")
    hist_data = get_history_data(symbol)
    print("Historical data size:", hist_data.shape)
    if hist_data.shape[0] < 90:
        print("Insufficient data for analysis: expected at least 90 days of data.")
        return
    # patterns = talib.CDLDOJI(hist_data['Open'], hist_data['High'], hist_data['Low'], hist_data['Close']) 
    pattern_names = talib.get_function_groups()['Pattern Recognition']
    for pattern_name in pattern_names:
        # print("Analyzing pattern:", pattern_name)
        pattern = getattr(talib, pattern_name)
        patterns = pattern(hist_data['Open'], hist_data['High'], hist_data['Low'], hist_data['Close'])
        pattern_dates = hist_data.index[patterns != 0]
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        last_five_days = [today - datetime.timedelta(days=i) for i in range(5)]
        for pattern_date in pattern_dates:
            if pattern_date.date() in last_five_days:
                # pattern_description = talib.get_function_groups().get('Pattern Descriptions', {}).get(pattern_name, 'No description available')
                print("Pattern occurred on", pattern_date.date(), ":", pattern_name)
                last_day_closing_price = hist_data['Close'].loc[pattern_date]
                print("Last day closing price:", last_day_closing_price)
                # print("Pattern description:", pattern_description)
                
    # Calculate MACD
    macd, signal, hist = talib.MACD(hist_data['Close'])
    if macd[-1] > signal[-1]:
        macd_trend = "UP"
    elif macd[-1] < signal[-1]:
        macd_trend = "DOWN"
    else:
        macd_trend = "Sideways"
    print("MACD Trend:", macd_trend)

    # Calculate RSI
    rsi = talib.RSI(hist_data['Close'])
    if rsi[-1] > 70:
        rsi_trend = "UP"
    elif rsi[-1] < 30:
        rsi_trend = "DOWN"
    else:
        rsi_trend = "Sideways"
    print("RSI Trend:", rsi_trend)

    # Calculate STOCHRSI
    fastk, fastd = talib.STOCHRSI(hist_data['Close'])
    if fastk[-1] > fastd[-1]:
        stochrsi_trend = "UP"
    elif fastk[-1] < fastd[-1]:
        stochrsi_trend = "DOWN"
    else:
        stochrsi_trend = "Sideways"
    print("STOCHRSI Trend:", stochrsi_trend)

    # Calculate SMA
    sma = talib.SMA(hist_data['Close'], timeperiod=14)
    print("SMA:", sma[-1])

    # Calculate OBV
    obv = talib.OBV(hist_data['Close'], hist_data['Volume'])
    print("OBV:", obv[-1])

    # Calculate WMA
    wma = talib.WMA(hist_data['Close'], timeperiod=14)
    print("WMA:", wma[-1])
   

def main():
    # Fetch list of NSE stocks
    nse_stocks = fetch_nse_stocks()
    print("NSE Stocks size:", nse_stocks.shape[0])

    data_list = []
    for index, row in tqdm(nse_stocks.iterrows(), total=nse_stocks.shape[0]):
        # Skip symbols that endswith "-SG"
        if row['tradingsymbol'].endswith("-SG"):
            continue
        symbol = row['tradingsymbol'] + ".NS" #"RELIANCE.NS" 
        analysis_result = pattern_analysis(symbol)
        if analysis_result:
            data_list.append(analysis_result)

    # Create a pandas DataFrame from the data list
    data_df = pd.DataFrame(data_list, columns=['Symbol', 'Recognised Pattern Names', 'RSI Trend', 'MACD Trend', 'SMA', 'WMA', 'OBV'])

    # Export the DataFrame to a CSV file
    data_df.to_csv('analysis_data.csv', index=False)


if __name__ == "__main__":
    main()
```


==================================================


## [2/3] Repository: algo-fno-trading-bot (`WHEEL_algo-fno-trading-bot`)
- **Full Name**: `algo-fno-trading-bot`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# 🤖 Algorithmic Options Trading Bot — NSE F&O (NIFTY / BANKNIFTY)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/status-educational-orange)

Fully automated algo trading system for the Indian derivatives market,
featuring HMM-based market regime detection and three intraday
strategies + BTST. Currently integrated with the **Dhan API** as its
broker backend. Adapted from the AI Pathways YouTube tutorial.

---

## 🗂️ Project Structure

```
dhan-trading-bot/
├── config/
│   └── config.py           ← All settings: API keys, risk, strategies
├── broker/
│   └── dhan_broker.py      ← Dhan API wrapper (orders, data, option chain)
├── core/
│   └── hmm_engine.py       ← HMM market regime detection (Bull/Bear/Sideways)
├── strategies/
│   ├── intraday.py         ← ORB + VWAP + EMA Momentum strategies
│   └── btst.py             ← BTST (Buy Today Sell Tomorrow) strategy
├── risk/
│   └── risk_manager.py     ← Position sizing, kill switch, trailing SL, P&L
├── backtest/
│   └── backtester.py       ← Walk-forward backtesting engine
├── main.py                 ← Master orchestrator (main loop)
├── requirements.txt
└── README.md
```

---

## ⚡ Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set environment variables
```bash
export DHAN_CLIENT_ID="your_client_id"
export DHAN_ACCESS_TOKEN="your_access_token"

# Optional: Telegram alerts
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
```

### 3. Run backtest first
```bash
python main.py --backtest --instrument NIFTY
```

### 4. Paper trade (safe mode)
```bash
python main.py --instrument NIFTY --paper
```

### 5. Live trading
```bash
python main.py --instrument BANKNIFTY
```

---

## 🧠 System Architecture

```
Market Data (Dhan API)
        │
        ▼
   HMM Engine  ──→  Regime (Bull/Bear/Sideways)
        │                    │
        ▼                    ▼
  Strategy Engine      Position Size Multiplier
  ┌─────────────┐
  │  ORB        │
  │  VWAP       │──→ TradeSetup (entry/SL/target)
  │  EMA Momentum│
  └─────────────┘
        │
        ▼
  Risk Manager
  ├─ Kill switch check
  ├─ Position sizing
  ├─ Max positions check
        │
        ▼
  Dhan Broker API
  ├─ Place order
  ├─ Place SL order
  └─ Monitor position (TSL)
        │
        ▼
  Notifications (Telegram)
```

---

## 📋 Strategies

### 1. Opening Range Breakout (ORB)
- Opening range = first 3 × 5-min candles (9:15–9:30)
- Buy CE on breakout above range high + buffer
- Buy PE on breakdown below range low − buffer
- SL = opposite end of range; Target = 2× risk

### 2. VWAP Mean Reversion
- Entry when price deviates ≥0.3% from VWAP
- RSI confirmation (oversold for buy, overbought for sell)
- Target = 50% reversion to VWAP

### 3. EMA Momentum
- Fast EMA (9) / Slow EMA (21) crossover
- ADX > 25 required (filters sideways markets)
- SuperTrend confirmation
- RSI not at extremes

### 4. BTST (Buy Today Sell Tomorrow)
- Entry window: 14:30 – 15:10
- Scores 5 factors: VWAP position, RSI, ADX, 15-min EMA alignment, SuperTrend
- Minimum score 4/5 required
- 1-OTM option (weekly expiry)
- Exit: next morning 09:35 – 09:45

---

## 🛡️ Risk Management

| Parameter | Value |
|-----------|-------|
| Capital | ₹5,00,000 |
| Max risk per trade | 1.5% |
| Daily loss limit | 3% (kill switch) |
| Max open positions | 3 |
| Max lots per trade | 2 |
| Min reward:risk | 2.0 |
| Trailing SL trigger | +1% profit |
| Trailing SL distance | 0.5% |

---

## 🔄 HMM Regime Engine

- **3 states**: Bull, Bear, Sideways
- **Features**: Returns, Volatility, RSI, ADX
- **Training**: 60 days daily data
- **Retrain**: Every 5 trading days
- **Effect on trading**:
  - Bull → LONG entries only, 1.0× position size
  - Sideways → both directions, 0.7× size
  - Bear → SHORT entries only, 0.5× size
  - Unknown → no new trades

---

## 📊 Walk-Forward Backtest

Splits historical data into 6 windows, each with 70% in-sample
(parameter selection) and 30% out-of-sample (real test).

```bash
python main.py --backtest --instrument NIFTY
```

Sample results (synthetic data):
```
ORB:  Trades=34  WR=68%  Net P&L=+₹42,800  Sharpe=1.51
VWAP: Trades=28  WR=61%  Net P&L=+₹31,200  Sharpe=1.22
EMA:  Trades=41  WR=65%  Net P&L=+₹38,600  Sharpe=1.38
```

---

## 🔧 Configuration

Edit `config/config.py`:

```python
# Capital
RiskConfig.total_capital = 500_000   # ₹5 Lakh

# Instruments
INSTRUMENTS["NIFTY"]["lot_size"] = 75    # Update if NSE changes lot size

# Strategy tuning
IntradayConfig.orb_candles = 3           # 3×5min = 15min ORB
IntradayConfig.adx_min = 25              # Trend strength filter
BTSTConfig.entry_time_start = "14:30"    # BTST entry window

# VIX filter for BTST
BTSTStrategy: vix > 20 → skip           # No overnight trades in high vol
```

---

## ⚠️ Important Notes

1. **Get Dhan API access**: Register at https://dhanhq.co and enable trading API
2. **Paper trade first**: Always test with `--paper` flag for at least 1 month
3. **Update lot sizes**: SEBI changes F&O lot sizes periodically
4. **Check margins**: Ensure sufficient margin in account before live trading
5. **Not financial advice**: This is a learning project — trade at your own risk

---

## 📦 Dependencies

- `dhanhq` — Dhan broker SDK
- `hmmlearn` — Hidden Markov Model
- `scikit-learn` — Feature scaling
- `pandas` / `numpy` — Data processing
- `pytz` — IST timezone handling
- `python-telegram-bot` — Notifications

---

*Built for educational purposes. Always test thoroughly before live deployment.*

### Core Implementation Code & Architecture
#### File: `broker/__init__.py`
```python

```

#### File: `core/__init__.py`
```python

```

#### File: `config/__init__.py`
```python

```

#### File: `strategies/__init__.py`
```python

```

#### File: `backtest/__init__.py`
```python

```

#### File: `risk/__init__.py`
```python

```


==================================================


## [3/3] Repository: algorithmic-trading-samples (`WHEEL_algorithmic-trading-samples`)
- **Full Name**: `algorithmic-trading-samples`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
---

## Join Our Newsletters 📬

### DataPro  
*The future of AI is unfolding. Don’t fall behind.*

<p><a href="https://landing.packtpub.com/subscribe-datapronewsletter/?link_from_packtlink=yes"><img src="https://static.packt-cdn.com/assets/images/DataPro NL QR Code.png" alt="DataPro QR" width="150"/></a></p>

Stay ahead with [**DataPro**](https://landing.packtpub.com/subscribe-datapronewsletter/?link_from_packtlink=yes), the free weekly newsletter for data scientists, AI/ML researchers, and data engineers.  
From trending tools like **PyTorch**, **scikit-learn**, **XGBoost**, and **BentoML** to hands-on insights on **database optimization** and real-world **ML workflows**, you’ll get what matters, fast.

> Stay sharp with [DataPro](https://landing.packtpub.com/subscribe-datapronewsletter/?link_from_packtlink=yes). Join **115K+ data professionals** who never miss a beat.

---

### BIPro  
*Business runs on data. Make sure yours tells the right story.*

<p><a href="https://landing.packtpub.com/subscribe-bipro-newsletter/?link_from_packtlink=yes"><img src="https://static.packt-cdn.com/assets/images/BIPro NL QR Code.png" alt="BIPro QR" width="150"/></a></p>

[**BIPro**](https://landing.packtpub.com/subscribe-bipro-newsletter/?link_from_packtlink=yes) is your free weekly newsletter for BI professionals, analysts, and data leaders.  
Get practical tips on **dashboarding**, **data visualization**, and **analytics strategy** with tools like **Power BI**, **Tableau**, **Looker**, **SQL**, and **dbt**.

> Get smarter with [BIPro](https://landing.packtpub.com/subscribe-bipro-newsletter/?link_from_packtlink=yes). Trusted by **35K+ BI professionals**, see what you’re missing.




# Hands-On Financial Trading with Python

<a href="https://www.packtpub.com/product/hands-on-financial-trading-with-python/9781838982881?utm_source=github&utm_medium=repository&utm_campaign=9781838982881"><img src="https://static.packt-cdn.com/products/9781838982881/cover/smaller" alt="Hands-On Financial Trading with Python" height="256px" align="right"></a>

This is the code repository for [Hands-On Financial Trading with Python](https://www.packtpub.com/product/hands-on-financial-trading-with-python/9781838982881?utm_source=github&utm_medium=repository&utm_campaign=9781838982881), published by Packt.

**A practical guide to using Zipline and other Python libraries for backtesting trading strategies**

## What is this book about?
Algorithmic trading helps you stay ahead of the markets by devising strategies in quantitative analysis to gain profits and cut losses.

The book starts by introducing you to algorithmic trading and explaining why Python is the best platform for developing trading strategies. You’ll then cover quantitative analysis using Python, and learn how to build algorithmic trading strategies with Zipline using various market data sources. Using Zipline as the backtesting library allows access to complimentary US historical daily market data until 2018. As you advance, you will gain an in-depth understanding of Python libraries such as NumPy and pandas for analyzing financial datasets, and explore Matplotlib, statsmodels, and scikit-learn libraries for advanced analytics. You’ll also focus on time series forecasting, covering pmdarima and Facebook Prophet.

By the end of this trading book, you will be able to build predictive trading signals, adopt basic and advanced algorithmic trading strategies, and perform portfolio optimization.

This book covers the following exciting features: 
* Discover how quantitative analysis works by covering financial statistics and ARIMA
* Use core Python libraries to perform quantitative research and strategy development using real datasets
* Understand how to access financial and economic data in Python
* Implement effective data visualization with Matplotlib
* Apply scientific computing and data visualization with popular Python libraries
* Build and deploy backtesting algorithmic trading strategies

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1838982884) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(12, 12), sharex=True)

x = np.linspace(0, 10, num=20)
y1 = np.exp(x)
y2 = x ** 3
y3 = np.sin(y2)
y4 = np.random.randn(20)

ax1.plot(x, y1, color='black', linestyle='--', linewidth=5, marker='x', markersize=15)
ax2.plot(x, y2, color='green', linestyle='-.', linewidth=2, marker='^', markersize=10, alpha=0.9)
ax3.plot(x, y3, color='red', linestyle=':', marker='*', markersize=15, drawstyle='steps')
ax4.plot(x, y4, color='green', linestyle='-', marker='s', markersize=15)

```

**Following is what you need for this book:**
This book is for data analysts and financial traders who want to explore how to design algorithmic trading strategies using Python’s core libraries. If you are looking for a practical guide to backtesting algorithmic trading strategies and building your own strategies, then this book is for you. Beginner-level working knowledge of Python programming and statistics will be helpful.

With the following software and hardware list you can run all code files present in the book (Chapter 1-9).

### Software and Hardware List

| Chapter  | Software required                                                                    | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
|  1 - 9   |   Anaconda, Python 3.6, JupyterLab                                           				| Windows, Mac OS X, and Linux (Any) |
|          |   List of packages and dependencies can be found in the environment.yml file         |                                    |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781838982881_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Python Algorithmic Trading Cookbook [[Packt]](https://www.packtpub.com/product/python-algorithmic-trading-cookbook/9781838989354) [[Amazon]](https://www.amazon.com/dp/1838989358)

* Python for Finance Cookbook [[Packt]](https://www.packtpub.com/product/python-for-finance-cookbook/9781789618518) [[Amazon]](https://www.amazon.com/dp/1789618517)

## Get to Know the Author
**Jiri Pik** is an artificial intelligence architect and strategist who works with major investment banks, hedge funds, and other players. He has architected and delivered breakthrough trading, portfolio, and risk management systems, as well as decision support systems, across numerous industries. His consulting firm, Jiri Pik—RocketEdge, provides its clients with certified expertise, judgment, and execution at lightspeed.

**Sourav Ghosh** has worked in several proprietary high-frequency algorithmic trading firms over the last decade. He has built and deployed extremely low-latency, highthroughput automated trading systems for trading exchanges around the world, across multiple asset classes. He specializes in statistical arbitrage market-making and pairs trading strategies for the most liquid global futures contracts. He works as a senior quantitative developer at a trading firm in Chicago. He holds a master's in computer science from the University of Southern California. His areas of interest include computer architecture, FinTech, probability theory and stochastic processes, statistical learning and inference methods, and natural language processing

### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781838982881">https://packt.link/free-ebook/9781838982881 </a> </p>

### Core Implementation Code & Architecture
#### File: `Chapter04/df.json`
```python
{"A":{"9":0.5936127527,"10":0.2769969051,"27":-0.0412638607,"39":-0.8209775777},"B":{"9":-0.5423635813,"10":0.7896671305,"27":0.2958843212,"39":-1.0997420126},"C":{"9":-1.7196723786,"10":0.3220741136,"27":-0.4252799881,"39":0.0867298289},"D":{"9":-0.5789087862,"10":0.700392377,"27":1.7276391202,"39":0.4562870104},"E":{"9":1.4269485506,"10":0.3887166323,"27":-0.8683525728,"39":0.4310333031}}
```

#### File: `Chapter08/quandl_eod.py`
```python
"""
Module for building a complete daily dataset from Quandl's EOD dataset.
Source Code Inspiration: https://github.com/quantopian/zipline/issues/2603
"""
from io import BytesIO
import tarfile
from zipfile import ZipFile

from click import progressbar
from logbook import Logger
import pandas as pd
import requests
from six.moves.urllib.parse import urlencode
from six import iteritems
from trading_calendars import register_calendar_alias

from . import core as bundles
import numpy as np

log = Logger(__name__)

ONE_MEGABYTE = 1024 * 1024
QUANDL_DATA_URL = "https://www.quandl.com/api/v3/databases/EOD/data?"


def format_metadata_url(api_key):
    """ Build the query URL for Quandl WIKI Prices metadata.
    """
    query_params = [("api_key", api_key), ("download_type", "full")]

    return QUANDL_DATA_URL + urlencode(query_params)


def load_data_table(file, index_col, show_progress=False):
    """ Load data table from zip file provided by Quandl.
    """
    with ZipFile(file) as zip_file:
        file_names = zip_file.namelist()
        assert len(file_names) == 1, "Expected a single file from Quandl."
        eod_prices = file_names.pop()
        with zip_file.open(eod_prices) as table_file:
            if show_progress:
                log.info("Parsing raw data.")
            data_table = pd.read_csv(
                table_file,
                header=None,
                names=[
                    "symbol",
                    "date",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "ex_dividend",
                    "split_ratio",
                    "adjusted_open",
                    "adjusted_high",
                    "adjusted_low",
                    "adjusted_close",
                    "adjusted_volume",
                ],
                parse_dates=["date"],
                index_col=index_col,
                usecols=[
                    "symbol",
                    "date",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "ex_dividend",
                    "split_ratio",
                ],
            )

    return data_table


def fetch_data_table(api_key, show_progress, retries):
    """ Fetch WIKI Prices data table from Quandl
    """
    for _ in range(retries):
        try:
            if show_progress:
                log.info("Downloading WIKI metadata.")

            # Extract link from metadata and download zip file.
            table_url = format_metadata_url(api_key)
            if show_progress:
                raw_file = download_with_progress(
                    table_url,
                    chunk_size=ONE_MEGABYTE,
                    label="Downloading WIKI Prices table from Quandl",
                )
            else:
                raw_file = download_without_progress(table_url)

            return load_data_table(
                file=raw_file, index_col=None, show_progress=show_progress
            )

        except Exception:
            log.exception("Exception raised reading Quandl data. Retrying.")

    else:
        raise ValueError(
            "Failed to download Quandl data after %d attempts." % (retries)
        )


def gen_asset_metadata(data, show_progress):
    if show_progress:
        log.info("Generating asset metadata.")

    data = data.groupby(by="symbol").agg({"date": [np.min, np.max]})
    data.reset_index(inplace=True)
    data["start_date"] = data.date.amin
    data["end_date"] = data.date.amax
    del data["date"]
    data.columns = data.columns.get_level_values(0)

    data["exchange"] = "QUANDL-EOD"
    data["auto_close_date"] = data["end_date"].values + pd.Timedelta(days=1)
    return data


def parse_splits(data, show_progress):
    if show_progress:
        log.info("Parsing split data.")

    data["split_ratio"] = 1.0 / data.split_ratio
    data.rename(
        columns={"split_ratio": "ratio", "date": "effective_date"},
        inplace=True,
        copy=False,
    )
    return data


def parse_dividends(data, show_progress):
    if show_progress:
        log.info("Parsing dividend data.")

    data["record_date"] = data["declared_date"] = data["pay_date"] = pd.NaT
    data.rename(
        columns={"ex_dividend": "amount", "date": "ex_date"}, inplace=True, copy=False
    )
    return data


def parse_pricing_and_vol(data, sessions, symbol_map):
    for asset_id, symbol in iteritems(symbol_map):
        asset_data = (
            data.xs(symbol, level=1).reindex(sessions.tz_localize(None)).fillna(0.0)
        )
        yield asset_id, asset_data


@bundles.register("quandl_eod")
def quandl_eod_bundle(environ,
                  asset_db_writer,
                  minute_bar_writer,
                  daily_bar_writer,
                  adjustment_writer,
                  calendar,
                  start_session,
                  end_session,
                  cache,
                  show_progress,
                  output_dir):
    """
    quandl_bundle builds a daily dataset using Quandl's WIKI Prices dataset.

    For more information on Quandl's API and how to obtain an API key,
    please visit https://docs.quandl.com/docs#section-authentication
    """
    api_key = environ.get("QUANDL_API_KEY")
    if api_key is None:
        raise ValueError(
            "Please set your QUANDL_API_KEY environment variable and retry."
        )

    raw_data = fetch_data_table(
        api_key, show_progress, environ.get("QUANDL_DOWNLOAD_ATTEMPTS", 5)
    )
    asset_metadata = gen_asset_metadata(raw_data[["symbol", "date"]], show_progress)
    asset_db_writer.write(asset_metadata)

    symbol_map = asset_metadata.symbol
    sessions = calendar.sessions_in_range(start_session, end_session)

    raw_data.set_index(["date", "symbol"], inplace=True)
    daily_bar_writer.write(
        parse_pricing_and_vol(raw_data, sessions, symbol_map),
        show_progress=show_progress,
    )

    raw_data.reset_index(inplace=True)
    raw_data["symbol"] = raw_data["symbol"].astype("category")
    raw_data["sid"] = raw_data.symbol.cat.codes
    adjustment_writer.write(
        splits=parse_splits(
            raw_data[["sid", "date", "split_ratio"]].loc[raw_data.split_ratio != 1],
            show_progress=show_progress,
        ),
        dividends=parse_dividends(
            raw_data[["sid", "date", "ex_dividend"]].loc[raw_data.ex_dividend != 0],
            show_progress=show_progress,
        ),
    )


def download_with_progress(url, chunk_size, **progress_kwargs):
    """
    Download streaming data from a URL, printing progress information to the
    terminal.

    Parameters
    ----------
    url : str
        A URL that can be understood by ``requests.get``.
    chunk_size : int
        Number of bytes to read at a time from requests.
    **progress_kwargs
        Forwarded to click.progressbar.

    Returns
    -------
    data : BytesIO
        A BytesIO containing the downloaded data.
    """
    resp = requests.get(url, stream=True)
    resp.raise_for_status()

    total_size = int(resp.headers["content-length"])
    data = BytesIO()
    with progressbar(length=total_size, **progress_kwargs) as pbar:
        for chunk in resp.iter_content(chunk_size=chunk_size):
            data.write(chunk)
            pbar.update(len(chunk))

    data.seek(0)
    return data


def download_without_progress(url):
    """
    Download data from a URL, returning a BytesIO containing the loaded data.

    Parameters
    ----------
    url : str
        A URL that can be understood by ``requests.get``.

    Returns
    -------
    data : BytesIO
        A BytesIO containing the downloaded data.
    """
    resp = requests.get(url)
    resp.raise_for_status()
    return BytesIO(resp.content)


register_calendar_alias("QUANDL-EOD", "NYSE")
```


==================================================
