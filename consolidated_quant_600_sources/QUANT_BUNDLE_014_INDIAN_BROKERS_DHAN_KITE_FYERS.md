# ⚡ [QUANT-SOURCE-014] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_014_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Dhan_Integration (`WHEEL_Algo_Dhan_Integration`)
- **Full Name**: `Algo_Dhan_Integration`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Intraday Short Bot using Dhan API

This bot scans IT stocks on 15-min timeframe and shorts weak stocks based on price/volume logic.

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Configure your API keys in `config.py`

3. Run the bot:
```bash
python bot.py
```

### Core Implementation Code & Architecture
#### File: `strategy.py`
```python
# strategy.py - simple shorting strategy logic

def should_short(candle):
    # Basic logic: red candle + volume spike + new low
    if candle['close'] < candle['open'] and candle['low'] < candle['prev_low'] and candle['volume'] > candle['avg_vol']:
        return True
    return False
```

#### File: `config.py`
```python
# config.py - store API keys and settings

DHAN_API_KEY = "your_dhan_api_key"
DHAN_ACCESS_TOKEN = "your_dhan_access_token"

MODE = "paper"  # or "live"

WATCHLIST = ["INFY", "TCS", "WIPRO", "TECHM", "HCLTECH"]
MAX_RISK_PER_TRADE = 0.02  # 2% of capital
CAPITAL = 10000  # Total capital to risk
TIMEFRAME = "15m"
```

#### File: `dhan_api.py`
```python
# dhan_api.py - helper methods for placing orders

import requests
from config import DHAN_API_KEY, DHAN_ACCESS_TOKEN

BASE_URL = "https://api.dhan.co"

HEADERS = {
    "access-token": DHAN_ACCESS_TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json",
    "client-id": DHAN_API_KEY,
}

def place_order(symbol, qty, order_type="SELL"):
    # Stubbed for safety (use real endpoint when live)
    print(f"[MOCK] {order_type} order placed for {symbol} - Qty: {qty}")
```

#### File: `bot.py`
```python
# bot.py - main trading loop

import time
from config import WATCHLIST, CAPITAL, MAX_RISK_PER_TRADE
from dhan_api import place_order
from strategy import should_short

def get_mock_candle(symbol):
    import random
    return {
        "symbol": symbol,
        "open": random.uniform(900, 950),
        "close": random.uniform(850, 899),
        "low": random.uniform(840, 849),
        "prev_low": random.uniform(850, 860),
        "volume": random.randint(100000, 300000),
        "avg_vol": random.randint(80000, 150000),
    }

def run():
    print("Starting bot...")
    while True:
        print("Scanning...")
        for symbol in WATCHLIST:
            candle = get_mock_candle(symbol)
            if should_short(candle):
                qty = int((CAPITAL * MAX_RISK_PER_TRADE) / candle['close'])
                place_order(symbol, qty)
        time.sleep(60 * 15)  # Wait 15 minutes

if __name__ == "__main__":
    run()
```


==================================================


## [2/3] Repository: Algorithmic-Trading (`WHEEL_Algorithmic-Trading`)
- **Full Name**: `Algorithmic-Trading`
- **Description**: This is code base for a trading robot using Zerodha Kite Connect API and python
- **GitHub Stars**: 34
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Algorithmic Trading India — NSE/BSE Strategies, Articles & Software

Welcome to **Trade Vectors' Algorithmic Trading** repository — a comprehensive collection of articles, strategies, and resources for **algorithmic trading in India (NSE/BSE)**. Built by professional algo traders and software engineers based in Mumbai.

## What is Algorithmic Trading?

Algorithmic trading (also known as algo trading, automated trading, or black-box trading) is the process of using computer programs to execute trading orders based on predefined rules and strategies. In India, algo trading accounts for over 50% of NSE's total trading volume.

## Topics Covered

### Trading Strategies
- **Momentum Trading** — Riding price trends using moving averages
- **Mean Reversion** — Trading around statistical price equilibrium
- **Arbitrage Strategies** — Exploiting price differences across NSE/BSE
- **Index Rebalancing** — Trading Nifty 50 & Bank Nifty rebalancing events
- **Options Strategies** — Iron Condor, Straddle, Strangle automation

### Technical Indicators for Algo Trading
- EMA Crossover Systems
- RSI-based automated entry/exit
- MACD divergence detection
- Bollinger Band breakout strategies
- SuperTrend automated systems

### NSE/BSE Market Specifics
- **Nifty 50 Algo Strategies** — Index trading automation
- **Bank Nifty F&O** — High-volatility options strategies
- **Equity Intraday** — BTST and MIS automated strategies
- **MCX Commodities** — Gold, Silver, Crude Oil algo systems

## Advantages of Algorithmic Trading

| Advantage | Description |
|---|---|
| Speed | Orders executed in milliseconds |
| Emotion-Free | No fear or greed in decision-making |
| Backtesting | Validate strategy before live trading |
| Consistency | Same rules applied every single trade |
| Multi-Market | Trade NSE, BSE, MCX simultaneously |
| Risk Management | Automated stop-losses and position sizing |

## Getting Started with Algo Trading in India

1. **Choose a broker** with an API (Zerodha, Upstox, Angel One)
2. **Learn Python** for algo trading
3. **Build a strategy** and backtest it on historical NSE data
4. **Paper trade** before going live
5. **Automate** and monitor your live algo system

## Recommended Tools & Libraries

```python
# Essential Python libraries for algo trading
pip install kiteconnect     # Zerodha API
pip install pandas          # Data manipulation
pip install numpy           # Numerical computing
pip install ta              # Technical indicators
pip install backtrader      # Backtesting framework
pip install matplotlib      # Charts and visualization
```

## About Trade Vectors

**Trade Vectors** is a Mumbai-based algorithmic trading firm specializing in automated trading software, quantitative strategy research, and algo trading education for the Indian financial markets (NSE/BSE/MCX).

Our services include:
- **Custom Algo Trading Software** development for NSE/BSE
- **Strategy Research & Backtesting** services
- **F&O Automated Trading** system development
- **Corporate Algo Trading Training** (NSE Academy programs)
- **Consulting** for hedge funds, proprietary trading firms

Visit **[tradevectors.com](https://tradevectors.com)** for algo trading courses, custom software development, and quantitative strategy consulting for Indian markets.

**Contact:** [tradevectors.com](https://tradevectors.com) | [@tradevectors](https://twitter.com/tradevectors) | Mumbai, India

---
*Keywords: algorithmic trading India, algo trading NSE BSE, automated trading software India, Python trading NSE, backtesting strategies India, F&O algo trading, quantitative trading India, Mumbai algo trading company*


==================================================


## [3/3] Repository: trading_dhan (`WHEEL_Automate_trading_dhan`)
- **Full Name**: `Automate_trading_dhan`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Automate Trading Dhan

Fully automated Indian options trading system using Dhan API. Monitors Nifty/BankNifty live, analyses global market intelligence + news + macro, detects breakout/breakdown signals, and executes CE/PE orders automatically. Sends Telegram alerts at every step.

## Quick Start

```bash
cd /Users/makamamarender/repo/Automate_trading_dhan/

python3 orchestrator.py status     # Check current state
python3 orchestrator.py briefing  # Morning briefing
python3 intraday_agent.py          # Start persistent agent (9:15 AM → 3:30 PM)
python3 market_intel.py            # Full market intelligence report
```

## Architecture

```
market_intel.py       Global markets + Indian macro + news + sentiment
market_data.py        Yahoo Finance (Nifty, BN, VIX, candles)
signal_generator.py   Breakout/breakdown signal logic
dhan_client.py        Dhan API wrapper (orders, positions, funds)
intraday_agent.py     Persistent loop (5-min, 9:15 AM → 3:30 PM)
chart_watcher.py      Playwright TradingView chart + candlestick patterns
orchestrator.py       Main brain (briefing, trading, squareoff, status)
notifier.py           Telegram alerts
state_manager.py      JSON state persistence
trade_journal.py      SQLite trade journal
config.py             All credentials and constants
```

## Cron Schedule (Mon–Fri)

| Time | Job | Purpose |
|------|-----|---------|
| 8:30 AM | Morning Intel | Global markets + macro + news → Telegram |
| 9:00 AM | Briefing | Nifty, VIX, PDH/PDL, signal check |
| 9:15 AM | Persistent Agent | Starts looping every 5 mins |
| 9:30 AM | Chart Watcher | TradingView screenshot + patterns |
| Every 5 min | Trading Signal | Lightweight signal check |
| Every 30 min | Chart Watcher | TradingView screenshot |
| 12:00 PM | Midday Check | Positions + funds |
| 12:30 PM | Midday Intel | Macro + news update |
| 3:10 PM | Square-Off | Auto-close all positions |
| 3:30 PM | Agent Exit | Persistent agent terminates |

## Database (trades.db)

| Table | Content |
|-------|---------|
| `trades` | Entry/exit price, qty, P&L, order ID |
| `daily_summary` | Day's P&L, win rate, trades count |
| `market_levels` | Nifty, BN, VIX, PDH, PDL, ATM |
| `global_indicators` | S&P 500, Nasdaq, Dow, Gold, Oil, DXY |
| `sentiment_log` | Score -3→+3, label, factors, override |
| `macro_snapshot` | RBI rate, CPI, GDP, Fiscal deficit, USD/INR |
| `news_headlines` | Top headlines with source + timestamp |

## Signal Logic

- **BUY_CE**: Nifty breaks above PD High by >0.3% + 5-min candle confirms bullish
- **BUY_PE**: Nifty breaks below PD Low by >0.3% + 5-min candle confirms bearish
- **Sentiment Override**: Macro environment can cancel or force trades
  - Bearish sentiment (score ≤ -2) → CE trades cancelled
  - Bullish sentiment (score ≥ +2) → PE trades cancelled
  - Strong bullish mood + no signal → Force BUY_CE

## Dhan Credentials

All credentials are loaded from `.env` file (never commit this file):

```
DHAN_CLIENT_ID=your_client_id
DHAN_TOKEN=your_jwt_token
DHAN_API_KEY=your_api_key
DHAN_API_SECRET=your_api_secret
TELEGRAM_BOT=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

See `.env.example` for the required variables.

## Setup Notes

- Token expires ~Aug 2026 — regenerate from web.dhan.co if needed
- Add funds before trading
- Market hours: 9:15 AM – 3:30 PM IST
- Next expiry: see config.py WEEKLY_EXPIRY

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `scripts/fetch_option_chain.py`
```python
#!/usr/bin/env python3
"""Fetch Nifty option chain from Hermes and save to JSON."""
import json
import sys
sys.path.insert(0, ".")

try:
    from hermes_client import HermesClient
except ImportError:
    print("ERROR: hermes_client not installed.")
    print("Try: pip3 install hermes-client")
    print("Or: python3 -m pip install hermes-client")
    sys.exit(1)

api_key = "YOUR_KEY"  # Replace with your API key

client = HermesClient(api_key=api_key)
option_chain = client.get_option_chain("SYMBOL:NIFTY")

output_path = "tests/fixtures/hermes/nifty_option_chain_24may.json"
with open(output_path, "w") as f:
    json.dump(option_chain, f, indent=2)

print(f"Saved option chain to {output_path}")
```

#### File: `src/main.py`
```python
#!/usr/local/bin/python3.10
"""
src/main.py — CLI entry point for cron jobs and manual runs.
Supports --mode=scan and --mode=brief.
"""
import sys, os

# Ensure project root is on path for all imports
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Automate_trading_dhan")
    parser.add_argument("--mode", required=True, choices=["scan", "brief", "help"],
                        help="scan: run signal scan | brief: pre-market briefing")
    args = parser.parse_args()

    if args.mode == "help":
        parser.print_help()
        sys.exit(0)

    if args.mode == "brief":
        from config import CAPITAL, LOT_NIFTY, WEEKLY_EXPIRY
        from utils import now_ist
        now = now_ist()
        print(f"📊 Pre-Market Briefing — {now.strftime('%Y-%m-%d %H:%M IST')}")
        print(f"Capital: ₹{CAPITAL:,}")
        print(f"Lot size: {LOT_NIFTY}")
        print(f"Weekly expiry: {WEEKLY_EXPIRY}")
        print("VIX check skipped (market closed / pre-market)")
        sys.exit(0)

    if args.mode == "scan":
        # Delegate to intraday_agent_v2 which runs its full trading loop
        import runpy
        runpy.run_path("intraday_agent_v2.py", run_name="__main__")
```

#### File: `scan_signal.py`
```python
#!/usr/local/bin/python3.10
"""Inline signal scan — replicate intraday_agent_v2 signal logic with live candle fetching."""
import sys, sqlite3, json
from datetime import datetime, date, timezone, timedelta

sys.path.insert(0, "/Users/makamamarender/repo/Automate_trading_dhan")

from config import (
    DB_PATH, CAPITAL, RISK_PER_TRADE_PCT,
    STOP_ATR, T1_ATR, T2_ATR,
    EMA_FAST, EMA_SLOW, RSI_PERIOD,
    RSI_ENTRY_MIN, RSI_ENTRY_MAX,
    TRADING_WINDOW_START_HR, TRADING_WINDOW_START_MIN,
    TRADING_WINDOW_END_HR, TRADING_WINDOW_END_MIN,
    PAPER_MODE, EXECUTION_MODE,
    LOT_NIFTY,
)
from dhan_client import get_nifty_5m_candles

IST = timezone(timedelta(hours=5, minutes=30), "IST")

def ema_calc(series, n):
    k = 2/(n+1)
    out = [series[0]]
    for v in series[1:]: out.append(v*k + out[-1]*(1-k))
    return out

def rsi_calc(prices, n=14):
    warmup = [50.0] * (n-1)
    deltas = [prices[i]-prices[i-1] for i in range(1, len(prices))]
    gains  = [max(d,0) for d in deltas]
    losses = [-min(d,0) for d in deltas]
    ag = sum(gains[:n])/n; al = sum(losses[:n])/n
    valid = [50.0]
    for i in range(n, len(deltas)):
        rs = ag/al if al else 999
        valid.append(100 - 100/(1+rs))
        ag = (ag*n - ag + gains[i])/n
        al = (al*n - al + losses[i])/n
    result = warmup + valid
    if len(result) < len(prices): result.extend([result[-1]] * (len(prices)-len(result)))
    return result[:len(prices)]

# ── Convert 5m candles → 15m candles ──────────────────────────
def convert_5m_to_15m(open_5m, high_5m, low_5m, close_5m, ts_5m):
    """Aggregate every 3 × 5m candles into one 15m candle."""
    n = len(open_5m)
    o, h, l, cl, ts = [], [], [], [], []
    for i in range(0, n, 3):
        chunk = close_5m[i:i+3]
        if not chunk:
            break
        o.append(open_5m[i])
        h.append(max(high_5m[i:i+3]))
        l.append(min(low_5m[i:i+3]))
        cl.append(chunk[-1])
        ts.append(ts_5m[i])
    return o, h, l, cl, ts

# Fetch live 5m candles from Dhan (3-day range to ensure enough candles for EMA21 warmup)
from datetime import timedelta
today_obj = date.today()
d1 = (today_obj - timedelta(days=3)).strftime('%Y-%m-%d')
d2 = today_obj.strftime('%Y-%m-%d')
data = get_nifty_5m_candles(d1, d2)

if data['count'] == 0:
    print("=== NO LIVE DATA ===")
    print("Could not fetch 5m candles from Dhan API.")
    sys.exit(1)

open_5m  = data['open']
high_5m  = data['high']
low_5m   = data['low']
close_5m = data['close']
ts_5m    = data['timestamp']

# Convert to 15m
o, h, l, cl, ts = convert_5m_to_15m(open_5m, high_5m, low_5m, close_5m, ts_5m)

# Convert Unix ts → IST datetime strings
ts_dt = []
for t in ts:
    dt_utc = datetime.utcfromtimestamp(t)
    dt_ist = dt_utc.replace(tzinfo=timezone.utc).astimezone(IST)
    ts_dt.append(dt_ist.strftime('%Y-%m-%d %H:%M:%S'))

n = len(cl)
if n < 50:
    print(f"=== NOT ENOUGH DATA: {n} candles ===")
    sys.exit(1)

# ATR
tr = [max(h[i]-l[i], abs(h[i]-cl[i-1]), abs(l[i]-cl[i-1])) for i in range(1, n)]
raw_atr = [sum(tr[:14])/14]
for i in range(14, len(tr)):
    raw_atr.append((raw_atr[-1]*13 + tr[i])/14)

ef = ema_calc(cl, EMA_FAST)
es = ema_calc(cl, EMA_SLOW)
rs = rsi_calc(cl, RSI_PERIOD)

now = datetime.now(IST)
now_hm = now.hour * 60 + now.minute
start_hm = TRADING_WINDOW_START_HR * 60 + TRADING_WINDOW_START_MIN
end_hm   = TRADING_WINDOW_END_HR * 60 + TRADING_WINDOW_END_MIN
in_window = start_hm <= now_hm <= end_hm

i = n - 1
pf_ef = ef[i-1]; pf_es = es[i-1]
cf_ef = ef[i];   cf_es = es[i]
rs_i  = rs[i]
nfty  = cl[i]
atr_i = raw_atr[i] if i < len(raw_atr) else 50

bullish = pf_ef <= pf_es and cf_ef > cf_es
bearish = pf_ef >= pf_es and cf_ef < cf_es

direction = None
opt_type  = None

if bullish and RSI_ENTRY_MIN < rs_i < RSI_ENTRY_MAX:
    direction = 'LONG'; opt_type = 'CE'
elif bearish and RSI_ENTRY_MIN < rs_i < RSI_ENTRY_MAX:
    direction = 'SHORT'; opt_type = 'PE'

print("=== NIFTY SIGNAL SCAN (LIVE) ===")
print(f"Time (IST): {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Candle: {ts_dt[i]} | Nifty: {nfty:.1f}")
print(f"EMA9: {cf_ef:.1f} | EMA21: {cf_es:.1f} | RSI: {rs_i:.1f} | ATR: {atr_i:.1f}")
print(f"Prev EMA9: {pf_ef:.1f} | Prev EMA21: {pf_es:.1f}")
print(f"In window: {in_window} | 5m candles fetched: {data['count']}")
print()

if direction:
    sd   = max(atr_i * STOP_ATR, nfty * 0.01)
    sl   = nfty - sd if direction == 'LONG' else nfty + sd
    t1   = nfty + atr_i * T1_ATR if direction == 'LONG' else nfty - atr_i * T1_ATR
    t2   = nfty + atr_i * T2_ATR if direction == 'LONG' else nfty - atr_i * T2_ATR
    risk = CAPITAL * RISK_PER_TRADE_PCT / 100
    lots = max(int(risk / sd), 1)
    atm_strike = round(nfty / 50) * 50

    # Tier
    if opt_type == 'CE' and rs_i > 60: tier = 'T1'
    elif opt_type == 'PE' and rs_i < 40: tier = 'T1'
    elif opt_type == 'CE' and rs_i > 50: tier = 'T2'
    elif opt_type == 'PE' and rs_i < 50: tier = 'T2'
    else: tier = 'T3'

    print(f"✅ SIGNAL: {direction} {opt_type} | TIER: { tier }")
    print(f"Entry: {nfty:.1f} | SL: {sl:.1f} | T1: {t1:.1f} | T2: {t2:.1f}")
    print(f"ATM Strike: {atm_strike} | Lots: {lots} | Risk ₹: {sd:.1f}")
    print(f"Reason: EMA crossover | RSI={rs_i:.1f} | ATR={atr_i:.1f}")

    # Send alert via notifier
    from notifier import alert_signal
    sig_name = f"BUY_{opt_type}"
    reason = f"EMA crossover | RSI={rs_i:.1f} | ATR={atr_i:.1f} | Nifty={nfty:.1f}"
    try:
        alert_signal(sig_name, nfty, atm_strike, nfty, lots, CAPITAL, reason,
                     confirm_timeout_sec=120)
        print("Telegram alert: SENT")
    except Exception as e:
        print(f"Telegram alert FAILED: {e}")
else:
    print("❌ NO SIGNAL")
    print(f"  Bullish crossover: {bullish} | Bearish crossover: {bearish}")
    print(f"  RSI {rs_i:.1f} in range [{RSI_ENTRY_MIN},{RSI_ENTRY_MAX}]: {RSI_ENTRY_MIN < rs_i < RSI_ENTRY_MAX}")
    print(f"  In window: {in_window}")
```

#### File: `tests/test_perfect_trades.py`
```python
"""
Verification tests for the "Perfect Trade" fixes:
1. Directional fix: Support bounce -> CE, Resistance rejection -> PE.
2. RSI Filter: Avoid CE if overbought, PE if oversold.
3. EMA Filter: Only CE if above EMA200, PE if below EMA200.
"""

import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import signal_generator
import config

# Force config for tests
config.USE_TREND_FILTER = True
config.USE_RSI_FILTER = True
config.USE_FIB_FILTER = False
config.RSI_OVERBOUGHT = 70
config.RSI_OVERSOLD = 30
config.EMA_PERIOD = 200

def _make_candle(close, time_str="2026-05-27 10:00"):
    return {"time": time_str, "open": close, "high": close, "low": close, "close": close}

@patch("market_data.get_candles")
@patch("signal_generator.USE_FIB_FILTER", False)
def test_support_bounce_triggers_ce(mock_get_candles):
    """Bouncing off support should trigger CE, not PE."""
    # Mock daily candles for EMA/RSI (bullish context: price > EMA200, RSI normal)
    daily_prices = [24000] * 250
    daily_candles = [_make_candle(p) for p in daily_prices]
    
    # Mock 5m candles (bullish momentum)
    candles_5m = [_make_candle(23500) for _ in range(10)]
    candles_5m.append(_make_candle(23550, "2026-05-27 10:15"))
    
    mock_get_candles.side_effect = lambda sym, inter, rng: daily_candles if inter == "1d" else candles_5m

    # Bullish Hammer at Support (PDL = 24500)
    with patch("signal_generator.get_candle_confirmation") as mock_candle_conf:
        mock_candle_conf.return_value = {
            "pattern": "HAMMER",
            "near_support": True,
            "near_resistance": False,
            "bullish_signal": True,
            "bearish_signal": False
        }
        
        signal, reason = signal_generator.generate_signal(
            nifty_spot=24508,
            pd_high=25000,
            pd_low=24500,
            vix=14,
            candles_5m=candles_5m,
            candles_15m=candles_5m
        )
        
        assert signal == "BUY_CE", f"Expected BUY_CE on support bounce, got {signal}: {reason}"

@patch("market_data.get_candles")
@patch("signal_generator.USE_FIB_FILTER", False)
def test_resistance_rejection_triggers_pe(mock_get_candles):
    """Rejecting resistance should trigger PE, not CE."""
    # Bearish context: price < EMA200, RSI normal
    daily_candles = [_make_candle(25000) for _ in range(250)]
    daily_candles[-1] = _make_candle(24000) # price below EMA200
    
    candles_5m = [_make_candle(24500) for _ in range(10)]
    
    mock_get_candles.side_effect = lambda sym, inter, rng: daily_candles if inter == "1d" else candles_5m

    # Bearish Shooting Star at Resistance (PDH = 24500)
    with patch("signal_generator.get_candle_confirmation") as mock_candle_conf:
        mock_candle_conf.return_value = {
            "pattern": "SHOOTING_STAR",
            "near_support": False,
            "near_resistance": True,
            "bullish_signal": False,
            "bearish_signal": True
        }
        
        signal, reason = signal_generator.generate_signal(
            nifty_spot=24495,
            pd_high=24500,
            pd_low=24000,
            vix=14,
            candles_5m=candles_5m,
            candles_15m=candles_5m
        )
        
        assert signal == "BUY_PE", f"Expected BUY_PE on resistance rejection, got {signal}: {reason}"

@patch("market_data.get_candles")
@patch("signal_generator.USE_FIB_FILTER", False)
def test_rsi_filter_blocks_overbought_ce(mock_get_candles):
    """RSI > 70 should block CE entries."""
    # Price > EMA200 but RSI very high
    # Generate prices that will result in high RSI
    daily_prices = [100] * 200 + [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    daily_candles = [_make_candle(p) for p in daily_prices]
    
    candles_5m = [_make_candle(200) for _ in range(10)]
    mock_get_candles.side_effect = lambda sym, inter, rng: daily_candles if inter == "1d" else candles_5m

    with patch("signal_generator.get_candle_confirmation") as mock_candle_conf:
        mock_candle_conf.return_value = {
            "pattern": "HAMMER",
            "near_support": True,
            "near_resistance": False,
            "bullish_signal": True,
            "bearish_signal": False
        }
        
        # Spot near "support" in a crazy rally
        signal, reason = signal_generator.generate_signal(
            nifty_spot=190,
            pd_high=250,
            pd_low=180,
            vix=14,
            candles_5m=candles_5m,
            candles_15m=candles_5m
        )
        
        assert signal is None, f"Expected signal to be blocked by RSI filter, got {signal}: {reason}"
        assert "RSI overbought" in reason

@patch("market_data.get_candles")
@patch("signal_generator.USE_FIB_FILTER", False)
def test_trend_filter_blocks_counter_trend(mock_get_candles):
    """Price below EMA200 should block CE entries."""
    # Price < EMA200
    daily_candles = [_make_candle(25000) for _ in range(250)]
    daily_candles[-1] = _make_candle(24000) # price below EMA200 (25000 avg)
    
    candles_5m = [_make_candle(24000) for _ in range(10)]
    mock_get_candles.side_effect = lambda sym, inter, rng: daily_candles if inter == "1d" else candles_5m

    with patch("signal_generator.get_candle_confirmation") as mock_candle_conf:
        mock_candle_conf.return_value = {
            "pattern": "HAMMER",
            "near_support": True,
            "near_resistance": False,
            "bullish_signal": True,
            "bearish_signal": False
        }
        
        signal, reason = signal_generator.generate_signal(
            nifty_spot=24005,
            pd_high=24500,
            pd_low=24000,
            vix=14,
            candles_5m=candles_5m,
            candles_15m=candles_5m
        )
        
        assert signal is None, f"Expected signal to be blocked by Trend filter, got {signal}: {reason}"
        assert "Trend is bearish" in reason
```

#### File: `signal_generator_v2.py`
```python
#!/usr/local/bin/python3.10
"""
Fresh CE/PE Options Signal Generator
Only trend-following entries. No reversal, no spread.
Exit: SL → T1 → T2 → market_close (no theta cut before targets)
"""
import sqlite3, json
from datetime import datetime, time as dtime

DB = 'trades.db'
conn = sqlite3.connect(DB)
db = conn.cursor()

# ── Config ────────────────────────────────────────────────────
RISK_PCT       = 1.0          # % of 1L capital per trade
STOP_ATR       = 1.5          # stop = ATR × this
T1_ATR         = 0.75         # T1 = ATR × this  (achievable in 1-2 candles)
T2_ATR         = 1.25         # T2 = ATR × this
ATR_PERIOD     = 14
EMA_FAST       = 9
EMA_SLOW       = 21
RSI_PERIOD     = 14
MKTS_OPEN      = dtime(9, 20)
MKTS_CLOSE     = dtime(15, 25)
ENTRY_START    = dtime(9, 30)  # no entries before 9:30 AM
ENTRY_END      = dtime(14, 00) # no new entries after 2 PM
THETA_END      = dtime(15, 00) # auto-close all at 3 PM

# ── Indicator helpers ────────────────────────────────────────
def ema(series, n):
    k = 2/(n+1)
    out = [series[0]]
    for v in series[1:]:
        out.append(v*k + out[-1]*(1-k))
    return out

def rsi(prices, n=14):
    warmup = [50.0] * (n-1)
    deltas = [prices[i]-prices[i-1] for i in range(1, len(prices))]
    gains  = [max(d,0) for d in deltas]
    losses = [-min(d,0) for d in deltas]
    ag = sum(gains[:n])/n
    al = sum(losses[:n])/n
    valid = [50.0]
    for i in range(n, len(deltas)):
        rs = ag/al if al else 999
        valid.append(100 - 100/(1+rs))
        ag = (ag*n - ag + gains[i])/n
        al = (al*n - al + losses[i])/n
    result = warmup + valid
    if len(result) < len(prices):
        result.extend([result[-1]] * (len(prices)-len(result)))
    return result[:len(prices)]

def true_range(h, l, prev_c, i):
    return max(h[i]-l[i], abs(h[i]-prev_c), abs(l[i]-prev_c))

# ── Load 5m candles ────────────────────────────────────────────
def load_candles(start_ts, end_ts):
    db.execute("SELECT timestamp,open,high,low,close FROM candles_5m WHERE timestamp>=? AND timestamp<=? ORDER BY timestamp", (start_ts, end_ts))
    rows = db.fetchall()
    if not rows:
        return [], [], [], [], []
    ts  = [r[0] for r in rows]
    o   = [float(r[1]) for r in rows]
    h   = [float(r[2]) for r in rows]
    l   = [float(r[3]) for r in rows]
    c   = [float(r[4]) for r in rows]
    return ts, o, h, l, c

# ── Main signal function ──────────────────────────────────────
def generate_signal(nifty_price=None, lookback_candles=50):
    """
    Returns dict with signal or None.
    Loads recent 5m data, computes EMA crossover, checks filters.
    """
    end_ts   = int(datetime.now().timestamp())
    start_ts = end_ts - (8 * 3600)  # last 8 hours

    ts, o, h, l, c = load_candles(start_ts, end_ts)
    if len(ts) < ATR_PERIOD + EMA_SLOW + RSI_PERIOD + 20:
        return None

    n = len(c)

    # ATR
    tr = [true_range(h, l, c[i-1], i) for i in range(1, n)]
    raw_atr = [sum(tr[:ATR_PERIOD])/ATR_PERIOD]
    for i in range(ATR_PERIOD, len(tr)):
        raw_atr.append((raw_atr[-1]*(ATR_PERIOD-1) + tr[i])/ATR_PERIOD)
    raw_atr.append(raw_atr[-1])
    atr = raw_atr

    # EMAs
    ema_f = ema(c, EMA_FAST)
    ema_s = ema(c, EMA_SLOW)

    # RSI
    rsi_val = rsi(c, RSI_PERIOD)

    # Use last completed candle for signal (not current running candle)
    i = n - 1  # last completed candle

    # Time check
    bt  = datetime.fromtimestamp(ts[i])
    now = datetime.now()
    if not (ENTRY_START <= bt.time() <= ENTRY_END):
        return None  # outside entry window

    # Trend-follow: EMA crossover
    prev_fast = ema_f[i-1]
    prev_slow = ema_s[i-1]
    curr_fast = ema_f[i]
    curr_slow = ema_s[i]

    sig = None

    # Bullish: fast crosses above slow → BUY CE
    if prev_fast <= prev_slow and curr_fast > curr_slow:
        if 40 < rsi_val[i] < 70:  # not overbought
            sig = ('CE', 'LONG')

    # Bearish: fast crosses below slow → BUY PE
    elif prev_fast >= prev_slow and curr_fast < curr_slow:
        if 30 < rsi_val[i] < 60:  # not oversold
            sig = ('PE', 'SHORT')

    if not sig:
        return None

    opt_type, direction = sig
    nfty = c[i]
    sd   = max(atr[i] * STOP_ATR, nfty * 0.01)  # at least 1% stop

    sl   = nfty - sd if direction == 'LONG' else nfty + sd
    t1   = nfty + atr[i] * T1_ATR if direction == 'LONG' else nfty - atr[i] * T1_ATR
    t2   = nfty + atr[i] * T2_ATR if direction == 'LONG' else nfty - atr[i] * T2_ATR

    risk     = 100000 * (RISK_PCT / 100)
    lot_size = max(int(risk / sd), 1)

    # ATR in points and as %
    atr_pct  = atr[i] / nfty * 100

    return {
        'option':    opt_type,
        'direction': direction,
        'entry':     round(nfty, 1),
        'sl':        round(sl, 1),
        't1':        round(t1, 1),
        't2':        round(t2, 1),
        'atr':       round(atr[i], 1),
        'atr_pct':   round(atr_pct, 2),
        'stop_dist': round(sd, 1),
        'lot_size':  lot_size,
        'rsi':       round(rsi_val[i], 1),
        'ema_fast':  round(curr_fast, 1),
        'ema_slow':  round(curr_slow, 1),
        'timestamp': ts[i],
        'time':      bt.strftime('%H:%M'),
    }

# ── Live signal check ────────────────────────────────────────
if __name__ == '__main__':
    sig = generate_signal()
    if sig:
        print(f"\nSIGNAL: BUY {sig['option']}")
        print(f"  Entry:   {sig['entry']}")
        print(f"  SL:      {sig['sl']}  ({sig['stop_dist']} pts, {sig['atr']} ATR)")
        print(f"  T1:      {sig['t1']}  ({sig['atr']} × {T1_ATR})")
        print(f"  T2:      {sig['t2']}  ({sig['atr']} × {T2_ATR})")
        print(f"  Size:    {sig['lot_size']} lots")
        print(f"  RSI:     {sig['rsi']}")
        print(f"  ATR:     {sig['atr']} pts ({sig['atr_pct']}%)")
        print(f"  EMA:     {sig['ema_fast']} / {sig['ema_slow']}")
        print(f"  Time:    {sig['time']}")
    else:
        print("No signal right now")
```


==================================================
