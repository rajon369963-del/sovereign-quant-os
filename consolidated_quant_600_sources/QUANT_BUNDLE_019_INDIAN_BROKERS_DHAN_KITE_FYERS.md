# ⚡ [QUANT-SOURCE-019] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_019_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: NIFTY50-Fno-AI-Decision-Engine (`WHEEL_NIFTY50-Fno-AI-Decision-Engine`)
- **Full Name**: `NIFTY50-Fno-AI-Decision-Engine`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
## 🤖 NIFTY50-FnO-AI-Decision-Engine: Real-Time Algorithmic Trading System

---

### **Overview** 🚀

The **NIFTY50-FnO-AI-Decision-Engine** is a high-frequency, real-time algorithmic trading pipeline designed to execute trades on the National Stock Exchange (NSE) Futures & Options (F&O) segment for the NIFTY 50 index.

This project integrates a **Finvasia Shoonya API** for market data and order execution with a **Large Language Model (LLM)** via the **OpenAI Assistant API** to generate minute-by-minute trading decisions. It showcases a robust, low-latency system capable of automated financial market operations.

---

### **Key Features** ✨

* **Real-Time Data Pipeline:** Fetches and processes **live NIFTY 50** spot data and **At-The-Money (ATM)** option chain data (Call/Put premiums) every minute.
* **Finvasia Shoonya Integration:** Uses the official API for secure login, market data retrieval (quotes, time-series candles), and market order placement/exit.
* **AI-Driven Decision Making:** A custom-trained **OpenAI Assistant** analyzes the market data (including 1-minute candlestick charts and option premiums) to determine the optimal action: `buy_call_option`, `buy_put_option`, `exit_option`, or `wait_and_watch`.
* **Automated Trade Execution:** Executes market orders (buy/sell) for NIFTY FnO options based on the AI's recommendations.
* **Position Management:** Tracks open positions, calculates real-time Profit & Loss (P&L), and manages potential reversals (e.g., exiting a Put to enter a Call).
* **Time-Synchronous Operations:** Employs a precise `wait_for_next()` function to ensure the trading cycle aligns exactly with the start of every minute for high-frequency strategy implementation.

---

### **Technology Stack** 🛠️

| Category | Component | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core programming language for the engine. |
| **Trading API** | Finvasia Shoonya API (via `NorenRestApiPy`) | Used for market connectivity, data feeds, and order execution. |
| **AI/ML** | OpenAI Assistant API (GPT-3.5/4) | The core decision-making engine; customized for trading logic. |
| **Data Processing** | `pandas` | Efficient handling and filtering of large NFO symbol data files. |
| **Security/Auth** | `pyotp` | Implementation of Time-based One-Time Password (TOTP) for secure login. |
| **Environment** | `json`, `datetime`, `time` | Modules for data serialization, time synchronization, and program flow control. |

---

### **System Architecture** 🏗️

The system operates in a continuous loop, executing a precise workflow every minute:

1.  **Initialization:** Establish a connection with the Finvasia Shoonya API and fetch the complete NFO symbol master data.
2.  **Data Acquisition:** Every minute, fetch the current NIFTY spot price, calculate the **At-The-Money (ATM) strike price**, and retrieve the live premiums and 1-minute historical candles for the corresponding Call and Put options.
3.  **Position Update:** If a position is open, update its current premium and calculate the running P&L.
4.  **AI Decision Phase:** The structured market data (including P&L context) is sent to the **OpenAI Assistant**. The assistant returns an action (`buy_call_option`, `exit_put_option`, etc.).
5.  **Execution & Management:** The returned action is executed via the `BuyOption` or `ExitOption` functions, placing a market order through the Shoonya API. The position state is updated accordingly.
6.  **Synchronization:** The `wait_for_next()` function pauses the execution until the exact start of the next minute, ensuring the trading logic runs on a consistent, timely basis.

---

### **Installation and Setup** ⚙️

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/NIFTY50-Fno-AI-Decision-Engine.git](https://github.com/YourUsername/NIFTY50-Fno-AI-Decision-Engine.git)
    cd NIFTY50-Fno-AI-Decision-Engine
    ```
2.  **Install Dependencies:**
    ```bash
    pip install NorenRestApiPy pyotp openai pandas requests
    ```
3.  **API Key Configuration:**
    Create a file named `keys.py` and populate it with your confidential API keys:
    ```python
    # keys.py
    openaikey = "YOUR_OPENAI_API_KEY"
    ```
    Update the `Login()` function in your `login.py` file with your Finvasia Shoonya credentials:
    ```python
    # login.py
    def Login():
        user = 'YOUR_USER_ID'
        pwd = 'YOUR_PASSWORD'
        factor2 = 'YOUR_TOTP_SECRET_KEY'
        # ... other credentials ...
    ```
4.  **OpenAI Assistant Setup:**
    You must pre-create an Assistant in the OpenAI playground with your desired trading strategy prompt and ensure its ID is added to the `main.py` file:
    ```python
    # main.py
    assistant_id = "asst_xxxxxxxxxxxxxxxxxxxxxxxxxxx" # <--- YOUR ASSISTANT ID HERE
    ```
5.  **Run the Engine:**
    ```bash
    python main.py
    ```

---

### **Future Enhancements** 💡

* **Risk Management Module:** Implement automated Stop-Loss (SL) and Target Profit (TP) orders.
* **Websocket Integration:** Switch from polling (`get_quotes`) to live data streaming via WebSockets for sub-second latency.
* **Tool Complexity:** Enhance the LLM's toolset with functions for dynamic strike price selection (e.g., slightly Out-of-the-Money).
* **Backtesting & Simulation:** Develop a module to simulate the trading logic against historical data to evaluate performance metrics (Sharpe Ratio, Max Drawdown).

---


### **Disclaimer** ⚠️

> **This project is for educational and portfolio demonstration purposes only.**
>
> **It is NOT intended for real-world production trading.** The author is not a financial advisor. All code provided here is based on technical logic and AI models, which are prone to errors and market unpredictability.
>
> **Trading in Futures and Options carries a high level of risk.** By using or adapting this code, you acknowledge and accept that you are solely responsible for any financial outcomes, losses, or gains that may result. **DO NOT** trade with capital you cannot afford to lose. Use this system only in a paper trading or simulation environment.

### Core Implementation Code & Architecture
#### File: `login.py`
```python
from NorenRestApiPy.NorenApi import NorenApi
from pyotp import TOTP
import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

def Login():
    user = ''
    pwd = ''
    factor2 = ''
    vc = ''
    app_key = ''
    imei = ""

    class ShoonyaApiPy(NorenApi):
        def __init__(self):
            super().__init__(
                host='https://api.shoonya.com/NorenWClientTP/',
                websocket='wss://api.shoonya.com/NorenWSTP/'
            )

    api = ShoonyaApiPy()
    otp = TOTP(factor2).now().zfill(6)
    login_response = api.login(
        userid=user,
        password=pwd,
        twoFA=otp,
        vendor_code=vc,
        api_secret=app_key,
        imei=imei
    )
    print(login_response)

    return api
```

#### File: `place_order.py`
```python
import time

def BuyOption(api, symbol, token, place=True):
    if place is True:
        api.place_order(buy_or_sell='B', product_type='M', exchange='NFO', tradingsymbol=symbol,
                        quantity=75, discloseqty=0, price_type='MKT', price=0, trigger_price=None,
                        retention='DAY', remarks='my_order_001')
    buying_premium = api.get_quotes(exchange="NFO", token=str(token))['lp']
    print(f"Bought {symbol} at {buying_premium}")
    time.sleep(1)

    return buying_premium


def ExitOption(api, symbol, token, place=True):
    if place is True:
        api.place_order(buy_or_sell='S', product_type='M', exchange='NFO', tradingsymbol=symbol,
                        quantity=75, discloseqty=0, price_type='MKT', price=0, trigger_price=None,
                        retention='DAY', remarks='my_order_001')
    selling_premium = api.get_quotes(exchange="NFO", token=str(token))['lp']
    print(f"Sold {symbol} at {selling_premium}")
    time.sleep(1)

    return selling_premium
```

#### File: `get_option_data.py`
```python
from datetime import datetime
import requests, zipfile
from io import BytesIO
import pandas as pd


def NiftyOptions():
    def NFO_filedata():
        url = "https://api.shoonya.com/NFO_symbols.txt.zip"
        response = requests.get(url)
        if response.status_code == 200:
            with zipfile.ZipFile(BytesIO(response.content)) as z:
                file_name = z.namelist()[0]
                with z.open(file_name) as file:
                    df = pd.read_csv(file)
                    return df
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")

    def weekly_option(df, index):
        current_date = datetime.now()
        df['Expiry'] = pd.to_datetime(df['Expiry'], format='%d-%b-%Y')
        df = df[df['Symbol'] == index]
        exp = list(df['Expiry'].unique())
        cur_exp = min(exp)

        df = df[df['Expiry'] == cur_exp]
        df = df.reset_index(drop=True)
        return df

    print("gotten Option data")
    return weekly_option(NFO_filedata(), 'NIFTY')
```

#### File: `get_latest_data.py`
```python
import datetime

def LatestData(api, options_df, candles_limit=3):
    nifty_data = api.get_quotes(exchange="NSE", token="26000")

    timestamp = nifty_data['request_time']
    nifty_price = nifty_data['lp']
    strike_price = round(float(nifty_price) / 50) * 50

    tokens = options_df[options_df['StrikePrice'] == strike_price]['Token'].to_list()
    TradingSymbol = options_df[options_df['StrikePrice'] == strike_price]['TradingSymbol'].to_list()
    put_token, put_symbol = tokens[0], TradingSymbol[0]
    call_token, call_symbol = tokens[1], TradingSymbol[1]

    call_premium = api.get_quotes(exchange="NFO", token=str(call_token))['lp']
    put_premium = api.get_quotes(exchange="NFO", token=str(put_token))['lp']

    lastBusDay = datetime.datetime.today()
    lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)
    candles_data = api.get_time_price_series(exchange='NSE', token='26000', starttime=lastBusDay.timestamp(), interval=1)

    MarketData = f"""time: {timestamp}
    nifty: {float(nifty_price)}
    ATM strike: {strike_price}
    Call Premium: {call_premium}
    Put Premium: {put_premium}
    Last {candles_limit} candles:
    """

    for candle in candles_data[:candles_limit]:
        MarketData += f"[{candle['into']}, {candle['inth']}, {candle['intl']}, {candle['intc']}] \n"

    OptionSymbol = {
        'call_symbol': call_symbol,
        'put_symbol': put_symbol,
        'put_token': put_token,
        'call_token': call_token
    }

    return MarketData, OptionSymbol
```

#### File: `main.py`
```python
import json
import time
import datetime
from login import Login
from get_option_data import NiftyOptions
from get_latest_data import LatestData
from place_order import BuyOption, ExitOption
from openai import OpenAI
from keys import openaikey


def wait_for_next():
    now = datetime.datetime.now()
    next_run = (now + datetime.timedelta(minutes=1)).replace(second=2, microsecond=0)
    sleep_seconds = (next_run - now).total_seconds()
    print(f"Sleeping for {sleep_seconds:.2f} seconds until {next_run.time()}")
    time.sleep(sleep_seconds)


def main():
    api = Login()
    df = NiftyOptions()
    position_open = False

    position_token = None
    position_symbol = None
    output = None
    position_detail = None

    client = OpenAI(api_key=openaikey)
    assistant_id = ""
    thread = client.beta.threads.create()

    c = 0
    while True:
        if c == 0:
            MarketData, TradingSymbols = LatestData(api, df, candles_limit=30)
        else:
            MarketData, TradingSymbols = LatestData(api, df)

        c += 1
        print(f"Round {c}")

        call_symbol = TradingSymbols['call_symbol']
        put_symbol = TradingSymbols['put_symbol']
        call_token = TradingSymbols['call_token']
        put_token = TradingSymbols['put_token']

        if position_open is True:
            position_detail['current_premium'] = float(api.get_quotes(exchange="NFO", token=str(position_token))['lp'])
            position_detail['pl'] = (position_detail['current_premium'] - float(position_detail['buying_premium'])) * 75
            MarketData += f"\n Current Position: {position_symbol} | PL: {position_detail['pl']}"

            print(position_detail)

        # Send updated market data to the AI assistant
        message_content = json.dumps(MarketData)
        client.beta.threads.messages.create(thread_id=thread.id, role="user", content=message_content)
        run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant_id)

        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            last_msg = messages.data[0]
            response_text = last_msg.content[0].text.value

            print("Assistant final function call or response:", response_text)

            response_dict = json.loads(response_text)
            fn_name = response_dict.get("name")
            fn_name = fn_name.replace("()", "")

            if fn_name == "buy_call_option":
                if position_open:
                    if position_symbol[12:13] == "C":
                        buying_premium = BuyOption(api, call_symbol, call_token, place=False)
                        print("NOTICE: AI Buying Call Despite Having Call")
                    else:
                        print("NOTICE: AI Exiting Call and Buying Put")
                        ExitOption(api, position_symbol, position_token)
                        buying_premium = BuyOption(api, call_symbol, call_token)
                else:
                    buying_premium = BuyOption(api, call_symbol, call_token)

                position_token = call_token
                position_symbol = call_symbol
                position_open = True
                position_detail = {
                    'type': position_symbol,
                    'buying_premium': buying_premium,
                    'current_premium': buying_premium,
                    'pl': 0
                }
                output = "Call option bought successfully."

            elif fn_name == "buy_put_option":
                if position_open:
                    if position_symbol[12:13] == "P":
                        buying_premium = BuyOption(api, put_symbol, put_token, place=False)
                        print("NOTICE: AI Buying Put Despite Having Put")
                    else:
                        print("NOTICE: AI Exiting Put and Buying Call")
                        ExitOption(api, position_symbol, position_token)
                        buying_premium = BuyOption(api, put_symbol, put_token)
                else:
                    buying_premium = BuyOption(api, put_symbol, put_token)

                position_token = put_token
                position_symbol = put_symbol
                position_open = True
                position_detail = {
                    'type': position_symbol,
                    'buying_premium': buying_premium,
                    'current_premium': buying_premium,
                    'pl': 0
                }
                output = "Put option bought successfully."

            elif fn_name in ("exit_call_option", "exit_put_option"):
                if position_open is not False:
                    ExitOption(api, position_symbol, position_token)
                    position_open = False
                    position_token = None
                    position_detail = None
                    output = "Call option exited." if fn_name == "exit_call_option" else "Put option exited."

            elif fn_name == "wait_and_watch":
                output = "Waiting to get get better opportunity"

            elif fn_name in ("hold_call_option", "hold_put_option"):
                output = "holding the current position"

            else:
                output = f"Function not recognized - {fn_name}."

            print(output)

        wait_for_next()
        print()


if __name__ == "__main__":
    main()
```


==================================================


## [2/3] Repository: ML_algo (`WHEEL_NSE_ML_algo`)
- **Full Name**: `NSE_ML_algo`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# QuasarML: Institutional-Grade Algorithmic Swing Trading for the NSE 🇮🇳

QuasarML is a high-performance, strictly quantitative machine learning pipeline built to extract pure alpha from the National Stock Exchange of India (NSE). 

Unlike conventional time-series forecasting models which attempt to predict absolute price targets, QuasarML frames the market as a zero-sum, cross-sectional ranking problem. By utilizing the **LightGBM LambdaRank** algorithm—a Learning-to-Rank (LTR) framework originally designed for search engines—the model learns to sort a highly liquid, point-in-time universe of equities by their expected short-term returns.

## Key Features

*   **Zero Lookahead & Survivorship Bias**: Built on a strictly historical Point-in-Time (PiT) filter. The system dynamically trades only stocks with a rolling 30-day average turnover of ₹5 Crores+, computed exclusively using $t-1$ data.
*   **LambdaRank Optimization**: Directly minimizes ranking errors by optimizing Normalized Discounted Cumulative Gain (NDCG), ensuring the model correctly identifies the top outperforming assets in the cross-section rather than attempting to predict arbitrary absolute returns.
*   **Cross-Sectional Feature Normalization**: Automatically converts all technical indicators (RSI, Volatility, Momentum) into cross-sectional Z-Scores. This stationary transformation isolates pure relative strength, immunizing the model against absolute market regimes.
*   **Dynamic Slippage & Risk Parity**: Accounts for real-world impact costs. Large-cap stocks incur minimal slippage (3 bps) while illiquid F&O names are penalized (up to 20 bps). Risk management modules limit daily drawdowns and halt trading during severe VIX expansions.
*   **Expanding-Window Walk-Forward CV**: Implements strict purge gaps to prevent autocorrelation leakage between training sequences, ensuring that historical backtests mathematically mirror out-of-sample live performance.

## Strategy Performance 📈
Based on the final Optuna hyperparameter grid search and aggressive position-sizing Engine tuning (15% per position, Top 4 picks, Volatility Squeeze Pyramiding):
*   **Target Annualized Return (CAGR)**: 35% - 40%+
*   **Win Rate**: ~58%
*   **Max Drawdown**: -18%
*   **Sharpe Ratio**: 1.45+

## Repository Structure
*   `src/features/` - PiT Cross-Sectional Z-Scoring & Feature compilation
*   `src/model/` - LightGBM LambdaRank Walk-Forward training loop
*   `src/backtest/` - Institutional execution engine with dynamic slippage & VIX filters
*   `config.yaml` - Centralized hyperparameter and risk configuration module

## Setup
1. Clone the repository.
2. Ensure you have the necessary data fetched via `yfinance` or your preferred data vendor.
3. Execute `scratch/phase4_pipeline.py` to initiate the full feature building, model training, and Walk-Forward backtest loop.

### Core Implementation Code & Architecture
#### File: `src/dashboard/__init__.py`
```python
# Dashboard module
from src.dashboard.app import create_app

__all__ = ["create_app"]
```

#### File: `src/model/__init__.py`
```python
# Model module
from src.model.trainer import LGBMModel, train_walk_forward
from src.model.baseline import LinearBaseline

__all__ = ["LGBMModel", "train_walk_forward", "LinearBaseline"]
```

#### File: `src/features/__init__.py`
```python
# Features module
from src.features.engineering import build_features, build_all_features
from src.features.validation import validate_no_leakage

__all__ = ["build_features", "build_all_features", "validate_no_leakage"]
```

#### File: `scratch/best_optuna_params.json`
```python
{
    "num_leaves": 81,
    "learning_rate": 0.009909292081139207,
    "min_child_samples": 27,
    "reg_alpha": 0.3598649513766684,
    "reg_lambda": 0.7130007105678667,
    "n_estimators": 847,
    "subsample": 0.9848999400692978,
    "colsample_bytree": 0.7268767524594641
}
```

#### File: `src/backtest/__init__.py`
```python
# Backtest module
from src.backtest.engine import run_backtest
from src.backtest.tearsheet import generate_tearsheet
from src.backtest.costs import dynamic_slippage
from src.backtest.risk import RiskManager

__all__ = ["run_backtest", "generate_tearsheet", "dynamic_slippage", "RiskManager"]
```

#### File: `src/data/__init__.py`
```python
# Data module — Universe definition, ingestion, and caching
from src.data.universe import get_fno_universe, SECTOR_MAP
from src.data.ingestion import (
    fetch_all_data,
    validate_ohlc,
    filter_universe,
)

__all__ = [
    "get_fno_universe",
    "SECTOR_MAP",
    "fetch_all_data",
    "validate_ohlc",
    "filter_universe",
]
```


==================================================


## [3/3] Repository: SMACrossoverStrategy-DhanAPI (`WHEEL_SMACrossoverStrategy-DhanAPI`)
- **Full Name**: `SMACrossoverStrategy-DhanAPI`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# 📈 SMA Crossover Strategy (Dhan API)

A polling-based paper-trading bot for NSE stocks, built on the Dhan API. It
runs a simple moving-average crossover strategy end to end — pulling live
prices, generating signals, managing simulated positions, and tracking PnL —
without ever sending a real order. Built to understand how a trading loop
actually behaves once you have to deal with forming candles, per-symbol
state, and risk cutoffs, rather than a backtest that already knows the whole
timeline.

It only paper trades. Orders are simulated in memory and logged; nothing is
ever sent to the exchange. Strategy logic and execution are kept separate, so
this could be pointed at real order placement later without rewriting the
signal logic.

## 🧠 The problem this is actually solving

A naive crossover bot checking `if fast_sma > slow_sma` every second has a bug
most people don't notice until live: the **current forming candle** changes
price every tick, so its SMA flickers, and a naive check can fire the same
signal multiple times on one candle, or fire on a value that never actually
closes that way.

The fix here is to only ever evaluate the **last fully closed candle**
(index `-2`, never `-1`), and lock a per-symbol pointer once a decision is
made for that candle:

```python
last_completed_time = chart.index[-2]
if last_candle_processed[name] != last_completed_time:
    # evaluate the crossover — this only runs once per closed candle
```

`last_candle_processed` stays pinned to the 9:15 candle's timestamp until the
9:20 candle closes, so a signal can't double-fire on the same bar no matter
how many times the loop polls in between.

## 🧩 State machine, not a flag

Each symbol in the watchlist is tracked as a small state machine —
`EMPTY` → `ACTIVE` → `CLOSED` — via the `orderbook` dict in
[`trade_utils.py`](trade_utils.py). This is what keeps entry and exit logic
from ever overlapping: a symbol in `ACTIVE` only ever gets exit checks (stop
loss, take profit, time-based), a symbol in `EMPTY` only ever gets entry
checks. No shared branch has to remember which case it's in.

## 🛡️ Risk cutoffs

| Setting | Meaning | Default |
|---|---|---|
| `SL_PERCENT` | Stop loss | `0.5%` |
| `TP_PERCENT` | Take profit | `1.0%` |
| `MAX_HOLDING_MINUTES` | Time-based exit, regardless of price | `180` |
| `GLOBAL_MAX_LOSS` | Realized + unrealized PnL cutoff — shuts the whole engine down if breached | `2000` |
| `MAX_TRADES_PER_DAY` | Per-symbol cap | `5` |

`trade_utils.check_global_max_loss` sums realized PnL from closed trades and
unrealized PnL from anything still open, every loop — so a single stock
gapping against an open position can still trip the account-wide breaker
before the day-loss limit would otherwise be hit symbol-by-symbol.

## 🚀 Running it

```bash
pip install -r requirements.txt   # TA-Lib needs a separate binary install on most OSes
cp .env.template .env             # fill in DHAN_CLIENT_ID and DHAN_ACCESS_TOKEN
python app_v1.0.2.py
```

Credentials load from `.env` via [`credentials.py`](credentials.py) — never
hardcoded, never committed (`.env` is gitignored). Set the watchlist and risk
parameters at the top of `app_v1.0.2.py` before running.

It runs during market hours (9:15–15:30 IST by default) and prints signals
and fills as they happen. On exit — clean shutdown, `Ctrl+C`, or the max-loss
breaker tripping — it writes the full trade history to a timestamped
`TradeLog_*.csv`. While running, live positions and closed trades are pushed
to an Excel dashboard (`PaperTrade_{date}.xlsx`) via `xlwings`.

## 🛠️ How it's built

- **`app_v1.0.2.py`** — the loop. Runs every second during market hours,
  pulls last price for the whole watchlist in one call (`tsl.get_ltp`,
  cheaper than one call per symbol), then per symbol either checks exits (if
  active) or looks for an entry (if flat).
- **`trade_utils.py`** — stateless helpers, no state of their own: the
  crossover check, paper entry/exit (`json.dumps`-logs the full order state
  on every fill so a stop or target firing can be traced back after the
  fact), global-loss check, and CSV/Excel export.
- **`credentials.py`** — loads `DHAN_CLIENT_ID` / `DHAN_ACCESS_TOKEN` from a
  local `.env` file into the environment, then reads them via `os.getenv`.
  Raises loudly on startup if either is missing, rather than letting the API
  client fail confusingly later.

See [`Documentation.md`](Documentation.md) for a full pass-by-pass walkthrough
of one loop iteration.

## ⚠️ Note

Educational and paper-trading only. It simulates fills, PnL, and risk limits
but does not model slippage, partial fills, liquidity, or broker/network
latency — none of which are optional in real markets. Do not point this at
live order placement without understanding exactly what it doesn't account
for.

## 📁 Repository structure

```
├── app_v1.0.2.py       # main loop — market hours, polling, state dispatch
├── trade_utils.py      # strategy logic + simulated broker (stateless helpers)
├── credentials.py      # loads Dhan API credentials from .env
├── .env.template        # DHAN_CLIENT_ID / DHAN_ACCESS_TOKEN, fill in and rename to .env
├── requirements.txt
├── Documentation.md    # loop-by-loop internals walkthrough
└── todo.md
```

### Core Implementation Code & Architecture
#### File: `credentials.py`
```python
import os
from pathlib import Path


def _load_dotenv():
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]

        os.environ.setdefault(key, value)


def _required(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


_load_dotenv()

client_id = _required("DHAN_CLIENT_ID")
access_token = _required("DHAN_ACCESS_TOKEN")
```

#### File: `app_v1.0.2.py`
```python
import datetime as dt
import time
import logging
from Dhan_Tradehull import Tradehull
import credentials
import trade_utils as tu 
import talib

# ==========================================
#        USER CONFIGURATION SECTION
# ==========================================

# 1. Strategy Settings
WATCHLIST           = ['NIFTY', 'RELIANCE'] 
EXCHANGE            = 'NSE'
TIMEFRAME           = '5'       # Candle timeframe
MAX_TRADES_PER_DAY  = 5         # Per stock
SMA_PERIOD_1        = 10        # Period for first SMA
SMA_PERIOD_2        = 20        # Period for second SMA
USE_EXCEL_OUTPUT    = True
MARGIN_CHECK        = True

# 2. Risk Management
QUANTITY            = 50        
SL_PERCENT          = 0.5       
TP_PERCENT          = 1.0       
GLOBAL_MAX_LOSS     = 2000      
MAX_HOLDING_MINUTES = 180       

# 3. Market Hours
START_TIME          = dt.time(9, 15)
END_TIME            = dt.time(15, 30)

# ==========================================

# Configure Logging to File and Console
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("strategy_logs.log"),
        logging.StreamHandler()
    ]
)

tsl = Tradehull(client_id=credentials.client_id, access_token=credentials.access_token)

# Setup
if USE_EXCEL_OUTPUT:
    live_sheet, comp_sheet = tu.setup_sheets()
completed_orders = []
orderbook = {name: tu.get_empty_order_template() for name in WATCHLIST}
last_candle_processed = {name: None for name in WATCHLIST}

def main():
    logging.info("Initializing Strategy Engine...")
    
    while True:
        try:
            now = dt.datetime.now()
            
            # 1. Market Hours
            if now.time() < START_TIME or now.time() > END_TIME:
                print(f"Market Closed ({now.strftime('%H:%M:%S')})...", end='\r')
                time.sleep(10)
                continue

            # 2. Update Data
            all_ltp = tsl.get_ltp(names=WATCHLIST)
            update_excel = False
            
            for name in WATCHLIST:
                if name not in all_ltp: continue
                ltp = float(all_ltp[name])
                
                # --- A. EXIT LOGIC (If Position exists) ---
                if orderbook[name]['status'] == 'ACTIVE':
                    exit_triggered, orderbook, remark = tu.check_sl_tp_exit(orderbook, name, ltp, now)
                    if exit_triggered:
                        tu.paper_exit(orderbook, completed_orders, name, ltp, now, remark)
                        update_excel = True
                    continue 

                # --- B. ENTRY LOGIC (If No Position) ---
                chart = tu.get_historical_data_safe(tsl, name, EXCHANGE, TIMEFRAME)
                chart['sma{SMA_PERIOD_1}'] = talib.SMA(chart['close'], timeperiod=SMA_PERIOD_1)
                chart['sma{SMA_PERIOD_2}'] = talib.SMA(chart['close'], timeperiod=SMA_PERIOD_2)  
                if chart is None: continue
                last_completed_time = chart.index[-2]
                

                #Entry Conditions
                if last_candle_processed[name] != last_completed_time:
                    is_crossover = tu.check_sma_crossover(chart, SMA_PERIOD_1, SMA_PERIOD_2)
                    trades_today = len([o for o in completed_orders if o['name'] == name])
                    can_trade    = trades_today < MAX_TRADES_PER_DAY
                    
                    if is_crossover and can_trade:
                        tu.paper_entry(
                            orderbook, name, ltp, 'BUY', 
                            QUANTITY, SL_PERCENT, TP_PERCENT, MAX_HOLDING_MINUTES
                        )
                        update_excel = True
                    
                    last_candle_processed[name] = last_completed_time

            # 3. Global Risk
            if tu.check_global_max_loss(completed_orders, orderbook, all_ltp, GLOBAL_MAX_LOSS):
                tu.save_to_csv(completed_orders) # Export before breaking
                break

            # 4. Excel Update
            if update_excel and USE_EXCEL_OUTPUT:
                tu.update_sheets(live_sheet, comp_sheet, orderbook, completed_orders)
            
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nStrategy Stopped by User.")
            tu.save_to_csv(completed_orders) # Export on Ctrl+C
            break
        except Exception as e:
            logging.error(f"Critical Loop Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
```

#### File: `trade_utils.py`
```python
import datetime as dt
import xlwings as xw
import pandas as pd
import talib
import logging
import json

# ==========================================
#          DATA & EXCEL MANAGEMENT
# ==========================================

def get_empty_order_template():
    return {
        'name': None, 'date': None, 'entry_signal': None, 'entry_time': None,
        'entry_price': None, 'qty': 0, 'target_price': None, 'stoploss': None,
        'exit_signal': None, 'exit_time': None, 'exit_price': None, 
        'pnl': 0.0, 'remark': None, 'status': 'EMPTY', 'max_holding_time': None
    }

def setup_sheets():
    """Initializes the Excel dashboard safely."""
    filename = f'PaperTrade_{dt.date.today()}.xlsx'
    try:
        wb = xw.Book(filename)
    except:
        wb = xw.Book()
        wb.save(filename)
    
    for sheet in ['live_trading', 'completed_orders']:
        if sheet not in [s.name for s in wb.sheets]:
            wb.sheets.add(sheet)

    live = wb.sheets['live_trading']
    comp = wb.sheets['completed_orders']
    live.clear()
    comp.clear()
    
    # Init Headers
    headers = pd.DataFrame([get_empty_order_template()])
    live.range('A1').value = headers
    comp.range('A1').value = headers
    
    return live, comp

def update_sheets(live_sheet, comp_sheet, orderbook, completed_orders):
    """Updates Excel without overwriting headers."""
    # Active Orders
    active_data = [v for k, v in orderbook.items() if v['status'] == 'ACTIVE']
    if active_data:
        live_sheet.range('A2').value = pd.DataFrame(active_data).values
    else:
        live_sheet.range('A2:Z100').clear_contents()

    # Completed Orders
    if completed_orders:
        comp_sheet.range('A2').value = pd.DataFrame(completed_orders).values

def save_to_csv(completed_orders):
    """Exports all completed trades to a timestamped CSV file."""
    if not completed_orders:
        logging.info("No trades executed. Skipping CSV export.")
        return
    
    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"TradeLog_{timestamp}.csv"
    
    try:
        df = pd.DataFrame(completed_orders)
        df.to_csv(filename, index=False)
        logging.info(f"Successfully exported trade data to {filename}")
        print(f"\n[INFO] Data saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save CSV: {e}")

def get_historical_data_safe(tsl, name, exchange, timeframe):
    """Fetches data, calculates Indicators, and handles API errors."""
    try:
        chart = tsl.get_historical_data(tradingsymbol=name, exchange=exchange, timeframe=timeframe)
        if chart is None or chart.empty: 
            return None
        return chart
    except Exception as e:
        logging.error(f"Data Fetch Error {name}: {e}")
        return None

# ==========================================
#          STRATEGY LOGIC
# ==========================================

def check_sma_crossover(chart, n1, n2):
    """
    Checks for SMA Crossover on the LAST COMPLETED candle.
    Index -1 = Current forming candle (IGNORE)
    Index -2 = Last completed candle (USE THIS)
    Index -3 = Previous completed candle (USE THIS)
    """
    try:
        sma10_prev = chart['sma{n1}'].iloc[-3]
        sma20_prev = chart['sma{n2}'].iloc[-3]
        sma10_curr = chart['sma{n1}'].iloc[-2]
        sma20_curr = chart['sma{n2}'].iloc[-2]
        
        return sma10_prev < sma20_prev and sma10_curr > sma20_curr
    except IndexError:
        return False

def check_global_max_loss(completed_orders, orderbook, all_ltp, max_loss):
    """Calculates Realized + Unrealized PnL to protect account."""
    realized = sum(o['pnl'] for o in completed_orders)
    unrealized = 0
    
    for name, order in orderbook.items():
        if order['status'] == 'ACTIVE':
            try:
                ltp = float(all_ltp[name])
                if order['entry_signal'] == 'BUY':
                    unrealized += (ltp - order['entry_price']) * order['qty']
            except:
                continue 
            
    total_pnl = realized + unrealized
    if total_pnl <= -max_loss:
        logging.warning(f"CRITICAL: GLOBAL MAX LOSS HIT | Net PnL: {total_pnl}")
        return True
    return False

# ==========================================
#          ORDER EXECUTION (PAPER)
# ==========================================

def paper_entry(orderbook, name, ltp, signal, qty, sl_perc, tp_perc, hold_min):
    """Opens a virtual position and logs full state."""
    current_time = dt.datetime.now()
    
    # Calc Risk Levels
    sl_points = ltp * (sl_perc / 100)
    tg_points = ltp * (tp_perc / 100)
    
    if signal == 'BUY':
        sl = ltp - sl_points
        tp = ltp + tg_points
        exit_sig = 'SELL'
    
    # Update Orderbook
    order = orderbook[name]
    order.update({
        'name': name,
        'date': current_time.strftime('%Y-%m-%d'),
        'entry_time': current_time.strftime('%H:%M:%S'),
        'entry_price': ltp,
        'entry_signal': signal,
        'exit_signal': exit_sig,
        'qty': qty,
        'target_price': round(tp, 2),
        'stoploss': round(sl, 2),
        'max_holding_time': current_time + dt.timedelta(minutes=hold_min),
        'status': 'ACTIVE',
        'remark': 'Open',
        'pnl': 0.0
    })
    
    # VERBOSE LOGGING
    log_payload = {
        "event": "ENTRY_EXECUTION",
        "symbol": name,
        "price": ltp,
        "time": str(current_time),
        "risk_metrics": {"stoploss": sl, "target": tp},
        "full_order_state": order
    }
    logging.info(f"ENTRY SIGNAL | {json.dumps(log_payload, default=str)}")
    return True

def paper_exit(orderbook, completed_orders, name, ltp, current_time, remark):
    """Closes a virtual position and logs full state."""
    order = orderbook[name]
    
    order['exit_time'] = current_time.strftime('%H:%M:%S')
    order['exit_price'] = ltp
    
    # Calc PnL
    if order['entry_signal'] == 'BUY':
        order['pnl'] = (ltp - order['entry_price']) * order['qty']
    
    order['pnl'] = round(order['pnl'], 2)
    order['remark'] = remark
    order['status'] = 'CLOSED'
    
    # Archive
    completed_orders.append(order.copy())
    
    # VERBOSE LOGGING
    log_payload = {
        "event": "EXIT_EXECUTION",
        "symbol": name,
        "exit_price": ltp,
        "pnl": order['pnl'],
        "reason": remark,
        "final_trade_record": order
    }
    logging.info(f"EXIT SIGNAL | {json.dumps(log_payload, default=str)}")
    
    # Reset Slot
    orderbook[name] = get_empty_order_template()
    return True

def check_sl_tp_exit(orderbook, name, ltp, current_time):
    """Checks active orders for Exit conditions."""
    order = orderbook[name]
    if order['status'] != 'ACTIVE': return False

    exit_triggered = False
    remark = ""

    # 1. Price Checks
    if order['entry_signal'] == 'BUY':
        if ltp <= order['stoploss']: exit_triggered, remark = True, "SL Hit"
        elif ltp >= order['target_price']: exit_triggered, remark = True, "Target Hit"
    
    # 2. Time Checks
    if current_time > order['max_holding_time']:
        exit_triggered, remark = True, "Time Exit"

    return exit_triggered, orderbook, remark
```


==================================================
