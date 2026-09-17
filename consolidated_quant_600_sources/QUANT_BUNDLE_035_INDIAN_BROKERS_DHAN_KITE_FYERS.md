# ⚡ [QUANT-SOURCE-035] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_035_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ORBBacktesting (`PHASE4-QUANT-075`)
- **Full Name**: `PHASE4-QUANT-075_SoRalenka__ORBBacktesting`
- **Description**: Run Back testing algorithm on algo trading strategies like opening range breakout with historical data collected from Zerodha kite connect api to get performance metrics of said strategy on the particular stocks.
- **GitHub Stars**: 4
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# ORBBacktesting
Run Back testing algorithm on algo trading strategies like opening range breakout with historical data collected from Zerodha kite connect api to get performance metrics of said strategy on the particular stocks.


==================================================


## [2/3] Repository: Stocks-Algo-Trading (`PHASE4-QUANT-076`)
- **Full Name**: `PHASE4-QUANT-076_pratikj37__Stocks-Algo-Trading`
- **Description**: Algorithmic Trading System for NSE Stocks and Derivatives
- **GitHub Stars**: 3
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Stocks-Algo-Trading-
Algorithmic Trading System for NSE Stocks and Derivatives

### Core Implementation Code & Architecture
#### File: `login.py`
```python
import zrd_login

kite = zrd_login.kite

print(kite.margins())
```

#### File: `get_data.py`
```python
import zrd_login
import pdb
import talib

kite = zrd_login.kite

watchlist = ['ADANIGAS' , 'ASAINPAINT' , 'AXISBANK' , 'BAJAJFINANCE']


for name in watchlist:

    data = zrd_login.get_data(naem= name, segment = 'NSE:', delta= 5, interval= '5minute', continuous= False, oi = False)

    data['ema9'] = talib.EMA(data['close'], timeperiod=9, ematype=0)
    data['ema21'] = talib.EMA(data['close'], timeperiod=21, ematype=0)



    pdb.set_trace()
```

#### File: `scan.py`
```python
import zrd_login
import pdb
import talib

kite = zrd_login.kite

watchlist = ['ADANIGAS' , 'ASAINPAINT' , 'AXISBANK' , 'BAJAJFINANCE']

for name in watchlist:

    print(name)
    data = zrd_login.get_data(name = name, segment = 'NSE:', delta = 5, interval = '5minute', continuous = False, oi = False)

    data['ema9'] = talib.EMA(data['close'], timeperiod=15, ematype=0)
    data['ema21'] = talib.EMA(data['close'], timeperiod=15, ematype=0)

    last_candle = data.iloc[-2]

    if (last_candle['ema9'] > last_candle['ema21']):
        print(f"buy {name}")
        pdb.set_trace()
        kite.place_order(variety= kite.VARIETY_REGULAR, exchange = kite.EXCHANGE_NSE, tradingsymbol= name[4:], transaction_type= kite.TRANSACTION_TYPE_SELL, quantity = 1, 
        product= kite.PRODUCT_MIS, order_type= kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)


    if (last_candle['ema21'] > last_candle['ema9']):
        print(f"sell {name}")
        pdb.set_trace
```

#### File: `order_exe.py`
```python
import zrd_login
import pdb
import talib

kite = zrd_login.kite

watchlist = ['ADANIGAS' , 'ASAINPAINT' , 'AXISBANK' , 'BAJAJFINANCE']

traded_scripts = []

while True:
    for name in watchlist:

        print(name)
        data = zrd_login.get_data(name= name , segment = 'NSE:' , delta = 5, interval = '5minute', continuous = False, oi = False)

        data['ema9'] = talib.EMA(data['close'], timeperiod=9, matype=0)
        data['ema21'] = talib.EMA(data['close'], timeperiod=21, matype=0)

        last_candle = data.iloc[-2]

        if last_candle['close'] > 500:
            continue

        try:
                if(last_candle['ema9'] > last_candle['ema21']) and (name not in traded_scripts):
                    print(f"buy {name}")
                    kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_BUY , quantity = 1 , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_MARKET , price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
                    traded_scripts.append(name)
				    

                if(last_candle['ema9'] < last_candle['ema21']) and (name not in traded_scripts):
                    print(f"buy {name}")
                    kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_SELL , quantity = 1 , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_MARKET , price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
                    traded_scripts.append(name)
                
        except Exception as e:
            pass
```

#### File: `zrd_login.py`
```python
from kiteconnect import KiteConnect, KiteTicker
import pdb
import kiteconnect
import pandas as pd
import datetime
import os

api_key = "insert_key_here"                  #api_key
api_secret = "inser_secret_key_here"         #secret_key
filename = str(datetime.datetime.now().date()) + 'token' + '.txt'

def read_access_token_from_file():
    file = open(filename, 'r+')
    access_token = file.read()
    file.close()
    return access_token

def send_access_token_to_file(access_token):
    file = open(filename, 'w')
    file.write(access_token)
    file.close()


def get_login(api_key, api_secret):
    global kwa, kite
    kite = KiteConnect(api_key=api_key)
    print("Logging into Zerodha")

    if filename not in os.listdir():

        print("[*] Generate Request Token : ", kite.login_url())
        request_tkn = input("[*] Enter Your Request Token Here: ")
        data = kite.generate_session(request_tkn, api_secret=api_secret)
        access_token = data["access_token"]
        kite.set_access_token(access_token)
        kws = KiteTicker(api_key, access_token)
        send_access_token_to_file(access_token)

    elif filename in os.listdir():
        print("Already Logged In for Today")
        access_token = read_access_token_from_file()
        kite.set_access_token(access_token)
        kws = KiteTicker(api_key, access_token)

    return kite

kite = get_login(api_key, api_secret)


def get_good_values(name):

    zrd_name = 'NSE:' + name
    data = kite.quote([zrd_name])

    ltp = data[zrd_name]['last_price']
    openx = data[zrd_name]['ohlc']['open'] 
    high = data[zrd_name]['ohlc']['high'] 
    low = data[zrd_name]['ohlc']['low'] 
    close = data[zrd_name]['ohlc']['close']
    volume = data[zrd_name]['volume']

    return ltp, openx, high, low, close, volume


def get_data(name, segment, delta, interval, continuous, oi):

    token = kite.ltp([segment + name])[segment + name]['instrument_token']
    to_date = datetime.datetime.now().date()
    from_date = to_date - datetime.timedelta(days=delta)

    data = kite.historical_data(instrument_token=token, from_date=from_date, to_date=to_date, interval=interval, continuous=False, oi=False)
    df = pd.DataFrame(data)
    # df = df.set_index(df['date'])
    return df
```


==================================================


## [3/3] Repository: StockTradingBot (`PHASE4-QUANT-078`)
- **Full Name**: `PHASE4-QUANT-078_nimishj3__StockTradingBot`
- **Description**: algorithmic trading bot for Indian equity and F&O markets, built on Zerodha KiteConnect. Scans 200+ NSE symbols every 5 minutes, detects high-probability intraday setups using multi-strategy technical analysis, and delivers trade signals with entry, stop-loss, and target directly to Telegram.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# 🤖 Millionaire Trading Bot

A production-ready, semi-automated algorithmic trading assistant for Indian equity and F&O markets. Connects with **Zerodha KiteConnect**, runs **multi-strategy analysis**, scores signals with an **AI confidence engine**, and notifies you via **Telegram** before placing any trade.

---

## 🏗️ Architecture Overview

```
User
 └── Telegram Interface
      └── Trading Engine
           ├── Market Scanner (continuous)
           │    └── Universe Builder (F&O stocks)
           ├── Strategy Engine
           │    ├── EMA Pullback Strategy
           │    ├── Momentum Breakout Strategy
           │    └── Swing Fibonacci Strategy
           ├── AI Confidence Engine (0–100 score)
           ├── Signal Generator (>75% threshold)
           ├── User Confirmation (Telegram reply)
           └── Trade Executor (Zerodha API)
```

---

## 📁 Project Structure

```
millionaire_trading_bot/
├── main.py                   ← Entry point
├── token_generator.py        ← Daily Zerodha token helper
├── requirements.txt
├── .env.example              ← Environment template
│
├── core/
│   ├── config.py             ← Centralized configuration
│   └── logger.py             ← Colored rotating logger
│
├── data/
│   ├── zerodha_client.py     ← KiteConnect API wrapper (rate-limited)
│   ├── historical_loader.py  ← OHLCV data with disk cache
│   └── websocket_feed.py     ← Real-time tick data (auto-reconnect)
│
├── scanner/
│   ├── universe_builder.py   ← F&O symbol → token mapping
│   └── market_scanner.py     ← Continuous multi-symbol scanner
│
├── strategies/
│   ├── ema_strategy.py       ← EMA 9/21/50/200 pullback logic
│   ├── momentum_strategy.py  ← Volume breakout + RSI
│   └── swing_strategy.py     ← Fibonacci retracement + trend
│
├── ai/
│   └── confidence_engine.py  ← Multi-factor scoring (0–100)
│
├── execution/
│   ├── telegram_bot.py       ← Signal sender + command listener
│   └── trade_executor.py     ← Order placement + position monitor
│
├── risk/
│   └── position_size.py      ← Capital-based + risk-based sizing
│
├── reports/
│   ├── trade_logger.py       ← CSV + JSON trade persistence
│   └── performance_report.py ← Daily/monthly analytics
│
└── engine/
    └── trading_engine.py     ← Central orchestrator
```

---

## ⚡ Quick Start

### 1. Install Dependencies

```bash
# Python 3.10+ required
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
ZERODHA_API_KEY=your_api_key
ZERODHA_API_SECRET=your_api_secret
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
TRADING_MODE=PAPER          # Start with PAPER mode!
```

### 3. Generate Daily Access Token

> **Run this every trading day before market opens (9:00 AM IST)**

```bash
python token_generator.py
```

This will:
1. Generate a Zerodha login URL
2. Open your browser
3. After login, paste the request token
4. Save the access token to `.env` automatically

### 4. Start the Bot

```bash
python main.py
```

---

## 📱 Telegram Commands

Once running, control the bot from Telegram:

| Command | Description |
|---|---|
| `EXECUTE RELIANCE` | Execute the pending signal for RELIANCE |
| `SKIP HINDALCO` | Skip/dismiss the signal for HINDALCO |
| `/status` | Show bot status and mode |
| `/pending` | List all pending signals |
| `/help` | Show all commands |

### Example Signal Message

```
========================================
🎯 TRADE SETUP DETECTED
========================================

📈 HINDALCO | BUY
📋 Strategy: Momentum_Breakout
⏱ Timeframe: 5minute

💰 Trade Parameters:
  Entry:      ₹956.00
  Stop Loss:  ₹944.00
  Target:     ₹990.00
  Quantity:   104 shares

📊 Risk/Reward:
  R/R Ratio:  1:2.8
  Max Risk:   ₹1,248
  Max Profit: ₹3,536

🧠 AI Confidence: 84.0%
[████████░░]

─────────────────────────────────────────
✅ Reply: EXECUTE HINDALCO
❌ Reply: SKIP HINDALCO
─────────────────────────────────────────
```

---

## 🧠 Strategy Details

### 1. EMA Pullback Strategy
| Condition | Rule |
|---|---|
| Trend Filter | Price > EMA 200 |
| Intermediate Trend | EMA 21 > EMA 50 |
| Entry Trigger | Price pulls back to EMA 21 (±0.3%) |
| Confirmation | Bullish candle (close > open) |
| Volume | ≥ 0.8× 20-period average |

### 2. Momentum Breakout Strategy
| Condition | Rule |
|---|---|
| Breakout | Price > recent 20-bar resistance |
| Volume Spike | ≥ 1.5× 20-period average |
| Trend Filter | Price > EMA 50 |
| RSI Zone | 55–80 (strong, not overbought) |
| Candle Strength | Close in upper 40% of range |

### 3. Swing Fibonacci Strategy
| Condition | Rule |
|---|---|
| Major Trend | Price > EMA 200 |
| EMA Alignment | EMA 21 > EMA 50 |
| Fibonacci Zone | Price in 38.2%–61.8% retracement |
| Volume Pattern | Contraction during pullback |
| Breakout | Volume expansion on signal candle |

---

## 🔢 AI Confidence Scoring

| Factor | Weight |
|---|---|
| Trend Strength (EMA alignment) | 25% |
| Volume Confirmation | 25% |
| Momentum Strength (RSI/candle) | 25% |
| Support/Resistance Alignment | 25% |
| Multi-strategy consensus bonus | +5% each |

Signals with **confidence < 75%** are silently discarded. Only high-quality setups reach Telegram.

---

## ⚖️ Risk Management

| Rule | Value |
|---|---|
| Max capital per trade | ₹1,00,000 |
| Max concurrent trades | 5 |
| Max risk per trade | 2% of allocated capital |
| Minimum risk/reward | 1:2 |
| Stop loss | Mandatory (ATR-based) |
| Futures | 1 lot only |

---

## 🔧 Configuration Reference

All settings in `.env`:

```env
# Zerodha
ZERODHA_API_KEY=           # From Zerodha Developer Console
ZERODHA_API_SECRET=        # From Zerodha Developer Console
ZERODHA_ACCESS_TOKEN=      # Auto-set by token_generator.py

# Telegram
TELEGRAM_BOT_TOKEN=        # From @BotFather
TELEGRAM_CHAT_ID=          # Your personal chat ID

# Trading
TRADING_MODE=PAPER         # PAPER (safe) or LIVE (real money)
MAX_CAPITAL_PER_TRADE=100000
MIN_CONFIDENCE_SCORE=75
MAX_OPEN_TRADES=5
RISK_REWARD_RATIO=2

# Strategies (true/false)
ENABLE_INTRADAY=true
ENABLE_MOMENTUM=true
ENABLE_SWING=true

# Scanner
SCAN_INTERVAL_SECONDS=60
HISTORICAL_DAYS=60
CANDLE_TIMEFRAME=5minute
```

---

## 📊 Reports

All reports are saved to `reports_output/`:
- `trades_YYYY_MM.csv` – Monthly trade log (Excel-compatible)
- `trades_YYYY_MM.json` – JSON trade data
- `signals_YYYY_MM_DD.jsonl` – All generated signals (including skipped)

Daily performance report is auto-sent to Telegram at 3:35 PM IST.

---

## 🛡️ Safety Features

- **PAPER mode** – Default mode simulates trades without placing real orders
- **Human confirmation** – Every trade requires explicit Telegram reply
- **Stop loss mandatory** – No trade executes without a stop loss
- **Max trade limit** – Prevents over-exposure
- **Rate limiting** – Respects Zerodha's 3 req/sec API limit
- **Auto-reconnect** – WebSocket reconnects with exponential backoff
- **Disk cache** – Historical data cached to survive restarts

---

## ⚠️ Important Disclaimers

1. **Always start in PAPER mode** (`TRADING_MODE=PAPER`) until you're confident
2. This bot requires a **Zerodha account with API access** (₹2000/month subscription)
3. **Past performance does not guarantee future results**
4. Algorithmic trading carries significant financial risk
5. The authors are not responsible for any trading losses
6. Consult a SEBI-registered advisor before live trading

---

## 🔑 Getting API Credentials

### Zerodha KiteConnect
1. Login to [Zerodha Developer Console](https://developers.kite.trade/)
2. Create a new app
3. Set redirect URL (can be `https://127.0.0.1`)
4. Copy API Key and Secret to `.env`

### Telegram Bot
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` and follow instructions
3. Copy the bot token to `.env`
4. Message [@userinfobot](https://t.me/userinfobot) to get your Chat ID

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| `TokenException` | Run `token_generator.py` to refresh token |
| `No signals generated` | Check market hours (9:15–15:30 IST) |
| WebSocket disconnect | Auto-reconnects; check internet |
| `Universe: 0 symbols` | Check Zerodha API credentials |
| Telegram not responding | Verify BOT_TOKEN and CHAT_ID |

### Core Implementation Code & Architecture
#### File: `risk/__init__.py`
```python
from risk.position_size import PositionSizer

__all__ = ["PositionSizer"]
```

#### File: `engine/__init__.py`
```python
from engine.trading_engine import TradingEngine

__all__ = ["TradingEngine"]
```

#### File: `core/__init__.py`
```python
from core.config import Config
from core.logger import get_logger

__all__ = ["Config", "get_logger"]
```

#### File: `ai/__init__.py`
```python
from ai.confidence_engine import ConfidenceEngine, TradeSignal

__all__ = ["ConfidenceEngine", "TradeSignal"]
```

#### File: `scanner/__init__.py`
```python
from scanner.universe_builder import UniverseBuilder
from scanner.market_scanner import MarketScanner

__all__ = ["UniverseBuilder", "MarketScanner"]
```

#### File: `reports/__init__.py`
```python
from reports.trade_logger import TradeLogger
from reports.performance_report import PerformanceReport

__all__ = ["TradeLogger", "PerformanceReport"]
```


==================================================
