# ⚡ [QUANT-SOURCE-107] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_107_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: SwingTradingAlgorithm (`WHEEL_SwingTradingAlgorithm`)
- **Full Name**: `SwingTradingAlgorithm`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)


### Core Implementation Code & Architecture
#### File: `swingtrend_strategy.py`
```python
import argparse
import pandas as pd
import numpy as np
from math import floor

# Indicator implementations including sma, ema, rsi, atr(stoploss), adx

def sma(series, period):
    return series.rolling(period, min_periods=period).mean()

def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()

def rsi(series, period=14):
    delta = series.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.ewm(alpha=1/period, adjust=False).mean()
    ma_down = down.ewm(alpha=1/period, adjust=False).mean()
    rs = ma_up / (ma_down.replace(0, np.nan))
    return 100 - (100 / (1 + rs))

def atr(df, period=14):
    high = df['High']; low = df['Low']; close = df['Close']
    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(window=period, min_periods=1).mean()

def adx(df, period=14):
    # Returns ADX, +DI, -DI (all series)
    high = df['High']; low = df['Low']; close = df['Close']
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = ((up_move > down_move) & (up_move > 0)) * up_move
    minus_dm = ((down_move > up_move) & (down_move > 0)) * down_move
    tr1 = high - low # True Range
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr_series = tr.rolling(window=period, min_periods=1).mean()
    # Smooth DM
    plus_dm_sm = plus_dm.rolling(window=period, min_periods=1).sum()
    minus_dm_sm = minus_dm.rolling(window=period, min_periods=1).sum()
    plus_di = 100 * (plus_dm_sm / atr_series.replace(0, np.nan))
    minus_di = 100 * (minus_dm_sm / atr_series.replace(0, np.nan))
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
    adx_series = dx.rolling(window=period, min_periods=1).mean()
    return adx_series, plus_di, minus_di

# Strategy logic by setting indicator conditions 

def generate_indicators(df):
    df = df.copy()
    df['SMA_44'] = sma(df['Close'], 44) # sma length 44 close
    df['EMA_50'] = ema(df['Close'], 50) # ema length 50 
    df['RSI_14'] = rsi(df['Close'], 14) # rsi length 14
    df['ATR_14'] = atr(df, 14) # atr length 14
    df['ADX_14'], df['+DI'], df['-DI'] = adx(df, 14) # adx length 14
    return df
# Entry/Exit signal generation

def generate_signals(df):
    """
    Signals:
     - Long entry when:
         Close > SMA_44 for 2 consecutive days
         EMA_50 > SMA_44
         55 <= RSI_14 <= 68
         ADX_14 > 25 and +DI > -DI
     - Short entry symmetrical
     Exits:
         - TP = +10% from entry
         - Initial SL = 3 * ATR
         - After +5% move, trail by 2 * ATR (handled in backtester)
         - Exit also when EMA_50 crosses SMA_44 opposite
    """
    df = df.copy()
    # boolean conditions per row
    df['cond_close_above_sma'] = df['Close'] > df['SMA_44']
    df['cond_close_below_sma'] = df['Close'] < df['SMA_44']
    # require 2 consecutive closes above/below sma
    df['above_sma_2'] = df['cond_close_above_sma'] & df['cond_close_above_sma'].shift(1).fillna(False)
    df['below_sma_2'] = df['cond_close_below_sma'] & df['cond_close_below_sma'].shift(1).fillna(False)

    df['ema_gt_sma'] = df['EMA_50'] > df['SMA_44']
    df['ema_lt_sma'] = df['EMA_50'] < df['SMA_44']

    df['rsi_long_ok'] = (df['RSI_14'] >= 55) & (df['RSI_14'] <= 68)
    df['rsi_short_ok'] = (df['RSI_14'] >= 32) & (df['RSI_14'] <= 45)

    df['adx_ok'] = df['ADX_14'] > 25
    df['plus_di_gt_minus'] = df['+DI'] > df['-DI']
    df['minus_di_gt_plus'] = df['-DI'] > df['+DI']

    df['long_signal'] = df['above_sma_2'] & df['ema_gt_sma'] & df['rsi_long_ok'] & df['adx_ok'] & df['plus_di_gt_minus']
    df['short_signal'] = df['below_sma_2'] & df['ema_lt_sma'] & df['rsi_short_ok'] & df['adx_ok'] & df['minus_di_gt_plus']

    return df

# Long/Short position sizing 

def position_size(capital, risk_pct, entry_price, atr, sl_multiplier=3):
    """
    Returns number of shares to buy/sell given risk (percentage of capital)
    SL distance = sl_multiplier * atr
    """
    risk_money = capital * risk_pct
    stop_distance = sl_multiplier * atr
    if stop_distance <= 0 or np.isnan(stop_distance):
        return 0, stop_distance
    qty = floor(risk_money / stop_distance)
    return int(qty), stop_distance

# Simple backtester (vectorized loop-based for trade execution)

def backtest(df, capital=1_000_000, risk_pct=0.01, sl_multiplier=3, tp_pct=0.10, trail_at_gain=0.05, trail_multiplier=2.0, commission_per_trade=0.0, slippage_pct=0.0005):
    """
    Runs a simple backtest. Assumptions:
     - Enter at next day's Open after signal True on day t
     - Exit on TP or SL intraday (simulated using next-day open & daily high/low)
     - Trailing stop enforced by updating stop price each day once price has moved in favor
    """
    trades = []
    equity = capital
    cash = capital
    position = None  # dict with keys: 'side','entry_price','qty','sl','tp','entry_index','max_favourable_price'
    equity_curve = [] # used to write daily equity values into a csv file

    for i in range(len(df)-1):  # we reference i and i+1 for entry at next open
        row = df.iloc[i]
        next_row = df.iloc[i+1]
        date = next_row.name  # use next day as execution day

        # record current equity
        if position is None:
            equity_curve.append({'Date': next_row.name, 'Equity': equity})
        else:
            # mark-to-market using close price
            mtm = position['qty'] * (next_row['Close'] - position['entry_price']) * (1 if position['side']=='long' else -1)
            equity_curve.append({'Date': next_row.name, 'Equity': equity + mtm})

        # If no position, check for signal at i
        if position is None:
            if row.get('long_signal', False):
                # compute sizing
                qty, stop_distance = position_size(equity, risk_pct, next_row['Open'], row['ATR_14'], sl_multiplier=sl_multiplier)
                if qty > 0:
                    entry_price = next_row['Open'] * (1 + slippage_pct)  # assume slippage on entry
                    sl_price = entry_price - stop_distance
                    tp_price = entry_price * (1 + tp_pct)
                    position = {
                        'side': 'long', 'entry_price': entry_price, 'qty': qty,
                        'sl': sl_price, 'tp': tp_price, 'entry_index': i+1,
                        'max_favourable': entry_price, 'sl_multiplier': sl_multiplier
                    }
                    cash -= qty * entry_price + commission_per_trade
                    trades.append({'EntryDate': next_row.name, 'Side': 'Long', 'Entry': entry_price, 'Qty': qty, 'SL': sl_price, 'TP': tp_price})
            elif row.get('short_signal', False):
                qty, stop_distance = position_size(equity, risk_pct, next_row['Open'], row['ATR_14'], sl_multiplier=sl_multiplier)
                if qty > 0:
                    entry_price = next_row['Open'] * (1 - slippage_pct)
                    sl_price = entry_price + stop_distance
                    tp_price = entry_price * (1 - tp_pct)
                    position = {
                        'side': 'short', 'entry_price': entry_price, 'qty': qty,
                        'sl': sl_price, 'tp': tp_price, 'entry_index': i+1,
                        'max_favourable': entry_price, 'sl_multiplier': sl_multiplier
                    }
                    cash += qty * entry_price - commission_per_trade  # short proceeds
                    trades.append({'EntryDate': next_row.name, 'Side': 'Short', 'Entry': entry_price, 'Qty': qty, 'SL': sl_price, 'TP': tp_price})

        else:
            # manage existing position using next_row's high/low to check TP/SL intraday
            # update max_favourable price
            if position['side'] == 'long':
                # update max favourable
                if next_row['High'] > position['max_favourable']:
                    position['max_favourable'] = next_row['High']
                # trailing stoploss activation
                if (position['max_favourable'] / position['entry_price'] - 1) >= trail_at_gain:
                    # compute new trailing stoploss
                    new_stop = position['max_favourable'] - trail_multiplier * next_row['ATR_14']
                    if new_stop > position['sl']:
                        position['sl'] = new_stop
                # check TP hit intraday
                if next_row['High'] >= position['tp']:
                    exit_price = position['tp'] * (1 - slippage_pct)
                    profit = (exit_price - position['entry_price']) * position['qty']
                    equity += profit - commission_per_trade
                    trades[-1].update({'ExitDate': next_row.name, 'Exit': exit_price, 'P&L': profit})
                    position = None
                    continue
                # check SL hit
                if next_row['Low'] <= position['sl']:
                    exit_price = position['sl'] * (1 - slippage_pct)
                    profit = (exit_price - position['entry_price']) * position['qty']
                    equity += profit - commission_per_trade
                    trades[-1].update({'ExitDate': next_row.name, 'Exit': exit_price, 'P&L': profit})
                    position = None
                    continue
                # check EMA/SMA flip exit on close
                if next_row['EMA_50'] < next_row['SMA_44']:
                    exit_price = next_row['Close'] * (1 - slippage_pct)
                    profit = (exit_price - position['entry_price']) * position['qty']
                    equity += profit - commission_per_trade
                    trades[-1].update({'ExitDate': next_row.name, 'Exit': exit_price, 'P&L': profit, 'ExitReason': 'EMA_SMA_flip'})
                    position = None
                    continue

            else:  # short
                if next_row['Low'] < position['max_favourable']:
                    position['max_favourable'] = next_row['Low']
                if (1 - position['max_favourable'] / position['entry_price']) >= trail_at_gain:
                    new_stop = position['max_favourable'] + trail_multiplier * next_row['ATR_14']
                    if new_stop < position['sl']:
                        position['sl'] = new_stop
                # TP
                if next_row['Low'] <= position['tp']:
                    exit_price = position['tp'] * (1 + slippage_pct)
                    profit = (position['entry_price'] - exit_price) * position['qty']
                    equity += profit - commission_per_trade
                    trades[-1].update({'ExitDate': next_row.name, 'Exit': exit_price, 'P&L': profit})
                    position = None
                    continue
                # SL
                if next_row['High'] >= position['sl']:
                    exit_price = position['sl'] * (1 + slippage_pct)
                    profit = (position['entry_price'] - exit_price) * position['qty']
                    equity += profit - commission_per_trade
                    trades[-1].update({'ExitDate': next_row.name, 'Exit': exit_price, 'P&L': profit})
                    position = None
                    continue
                # EMA/SMA flip exit
                if next_row['EMA_50'] > next_row['SMA_44']:
                    exit_price = next_row['Close'] * (1 + slippage_pct)
                    profit = (position['entry_price'] - exit_price) * position['qty']
                    equity += profit - commission_per_trade
                    trades[-1].update({'ExitDate': next_row.name, 'Exit': exit_price, 'P&L': profit, 'ExitReason': 'EMA_SMA_flip'})
                    position = None
                    continue

    # close any open position at final close price
    if position is not None:
        final = df.iloc[-1]
        if position['side']=='long':
            exit_price = final['Close'] * (1 - slippage_pct)
            profit = (exit_price - position['entry_price']) * position['qty']
            equity += profit - commission_per_trade
            trades[-1].update({'ExitDate': final.name, 'Exit': exit_price, 'P&L': profit, 'ExitReason': 'EndClose'})
        else:
            exit_price = final['Close'] * (1 + slippage_pct)
            profit = (position['entry_price'] - exit_price) * position['qty']
            equity += profit - commission_per_trade
            trades[-1].update({'ExitDate': final.name, 'Exit': exit_price, 'P&L': profit, 'ExitReason': 'EndClose'})
        position = None
        equity_curve.append({'Date': final.name, 'Equity': equity})

    trades_df = pd.DataFrame(trades)
    equity_df = pd.DataFrame(equity_curve).set_index('Date')
    return trades_df, equity_df

# Utilities

def perf_summary(trades_df, equity_df, capital):
    if trades_df.empty:
        print("No trades executed.")
        return
    wins = trades_df[trades_df['P&L']>0]
    losses = trades_df[trades_df['P&L']<=0]
    total_return = (equity_df['Equity'].iloc[-1] / capital - 1) * 100
    win_rate = len(wins) / len(trades_df) * 100
    avg_win = wins['P&L'].mean() if not wins.empty else 0
    avg_loss = losses['P&L'].mean() if not losses.empty else 0
    avg_rr = (wins['P&L'].mean() / -losses['P&L'].mean()) if (not wins.empty and not losses.empty and losses['P&L'].mean()!=0) else np.nan
    print("Trades:", len(trades_df))
    print(f"Total return: {total_return:.2f}%")
    print(f"Win rate: {win_rate:.2f}%")
    print(f"Avg win: {avg_win:.2f}, Avg loss: {avg_loss:.2f}, Avg W/L ratio: {avg_rr:.2f}")

# Main (CLI)

def main():
    parser = argparse.ArgumentParser(description='SwingTrend strategy backtester')
    parser.add_argument('--data', required=True, help='CSV file with OHLCV data (Date,Open,High,Low,Close,Volume)')
    parser.add_argument('--capital', type=float, default=1_000_000, help='Starting capital in INR')
    parser.add_argument('--risk', type=float, default=0.01, help='Risk per trade (fraction of capital)')
    parser.add_argument('--sl_mult', type=float, default=3.0, help='Stop-loss multiplier times ATR')
    parser.add_argument('--tp', type=float, default=0.10, help='Take-profit fraction (10% default)')
    args = parser.parse_args()

    df = pd.read_csv(args.data, parse_dates=['Date'], index_col='Date').sort_index()
    df = generate_indicators(df)
    df = generate_signals(df)
    trades_df, equity_df = backtest(df, capital=args.capital, risk_pct=args.risk, sl_multiplier=args.sl_mult, tp_pct=args.tp)
    trades_df.to_csv('trades.csv', index=False)
    equity_df.to_csv('equity_curve.csv')
    perf_summary(trades_df, equity_df, args.capital)
    print("Wrote trades.csv and equity_curve.csv to current directory.")

if __name__ == '__main__':
    main()
```


==================================================


## [2/3] Repository: Trading-APIs (`WHEEL_Trading-APIs`)
- **Full Name**: `Trading-APIs`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Trading APIs for NSE/BSE India — Zerodha, IBKR, Upstox & More

A comprehensive guide to **trading platform APIs** used for algorithmic trading in the **Indian stock market (NSE/BSE)**. This repository covers API integration, documentation, and code examples for building automated trading systems.

## Covered Trading APIs

### Indian Brokers
- **Zerodha Kite Connect API** — Most popular algo trading API in India for NSE/BSE
- **Upstox API** — REST-based trading API for equity and F&O
- **Angel One SmartAPI** — Full-stack trading API with WebSocket support
- **Fyers API** — Trading and data API for Indian markets
- **5Paisa API** — REST API for order placement and market data

### International Brokers
- **Interactive Brokers TWS API** — Professional-grade API for global markets
- **Alpaca API** — Commission-free trading API

## Key API Capabilities

| Feature | Description |
|---|---|
| Order Placement | Market, Limit, SL, SL-M orders via API |
| Live Market Data | Real-time quotes, OHLCV data streaming |
| Historical Data | Candle data for backtesting strategies |
| Portfolio Management | Positions, holdings, P&L via API |
| WebSocket Streaming | Live tick-by-tick data feeds |
| Options Chain | F&O contract data and Greeks |

## Python Integration Examples

```python
# Zerodha Kite Connect — Sample Order Placement
from kiteconnect import KiteConnect

kite = KiteConnect(api_key="your_api_key")
kite.place_order(
    tradingsymbol="NIFTY",
    exchange=kite.EXCHANGE_NFO,
    transaction_type=kite.TRANSACTION_TYPE_BUY,
    quantity=50,
    order_type=kite.ORDER_TYPE_MARKET,
    product=kite.PRODUCT_MIS
)
```

## Use Cases for Trading APIs

- Building algorithmic trading systems for NSE/BSE
- Automating F&O strategies (Nifty 50, Bank Nifty)
- Creating custom dashboards with live market data
- Backtesting strategies with historical API data
- Paper trading before going live

## About Trade Vectors

**Trade Vectors** is a Mumbai-based algorithmic trading company specializing in building automated trading systems, API integrations, and algo trading software for the Indian market.

We provide:
- Custom trading API integration services
- Algorithmic trading software development for NSE/BSE
- Algo trading consulting and strategy research
- Corporate training in algorithmic trading

Visit **[tradevectors.com](https://tradevectors.com)** for trading API integration services, algo trading courses, and custom automated trading solutions for India.

**Contact:** [tradevectors.com](https://tradevectors.com) | [@tradevectors](https://twitter.com/tradevectors)

---
*Keywords: trading API India, Zerodha Kite API Python, NSE API integration, algo trading API India, automated trading NSE BSE API, IBKR India, fintech India trading*


==================================================


## [3/3] Repository: TradingView (`WHEEL_TradingView`)
- **Full Name**: `TradingView`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<div align="center">
  <a name="readme-top"></a>
  <img src="https://raw.githubusercontent.com/beto-group/beto.assets/main/BETO.logo.animated.svg?raw=true" alt="LOGO" width="160">
  <h1 align="center">TRADING VIEW</h1>
  <h3 align="center"> Lead-Lag Crypto Correlation Engine </h3>
</div>

<div align="center">
  <!-- TOP PURPLE LINKS -->
  <a href="https://beto.group"><img src="https://img.shields.io/badge/WEBSITE-7A46F1?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgY2xhc3M9Imx1Y2lkZSBsdWNpZGUtZXh0ZXJuYWwtbGluayI+PHBhdGggZD0iTTE4IDEzdjZhMiAyIDAgMCAxLTIgMkg1YTIgMiAwIDAgMS0yLTJWOGEyIDIgMCAwIDEgMi0yaDYiLz48cG9seWxpbmUgcG9pbnRzPSIxNSAzIDIxIDMgMjEgOSIvPjxsaW5lIHgxPSIxMCIgeDI9IjIxIiB5MT0iMTQiIHkyPSIzIi8+PC9zdmc+" alt="WEBSITE"></a>
  <a href="https://discord.com/invite/6rDp4q4Y2B"><img src="https://img.shields.io/badge/DISCORD-7A46F1?style=for-the-badge&logo=discord&logoColor=white" alt="JOIN OUR DISCORD"></a>
  <a href="https://github.com/sponsors/beto-group"><img src="https://img.shields.io/badge/Sponsor-7A46F1?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="SUPPORT US ON GITHUB"></a>
  <br/>
  <!-- BOTTOM GOLD TAXONOMY -->
  <img src="https://img.shields.io/badge/TARGET-DATACORE-000?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNGRkUxNjUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNIDMgNXYxNGE5IDMgMCAwIDAgMTggMHYtMTQiLz48cGF0aCBkPSJNIDMgMTJhOSAzIDAgMCAwIDE4IDAiLz48L3N2Zz4=" alt="TARGET">
  <img src="https://img.shields.io/badge/SECURITY-NODE__FS-000?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNGRkUxNjUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj4gPHBhdGggZD0iTTEyIDIyczgtNCA4LTEwVjVsLTgtMy04IDN2N2MwIDYgOCAxMCA4IDEweiIvPjwvc3ZnPg==" alt="SECURITY">
  <img src="https://img.shields.io/badge/RUNTIME-PUREJS-000?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNGRkUxNjUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTQuNSAySDZhMiAyIDAgMCAwLTIgMnYxNmEyIDIgMCAwIDAgMiAyaDEyYTIgMiAwIDAgMCAyLTJWNy5MMTQuNSAyeiIvPjxwb2x5bGluZSBwb2ludHM9IjE0IDIgMTQgOCAyMCA4Ii8%2BPGxpbmUgeDE9IjE2IiB4Mj0iOCIgeTE9IjEzIiB5Mj0iMTMiLz48bGluZSB4MT0iMTYiIHgyPSI4IiB5MT0iMTciIHkyPSIxNyIvPjxsaW5lIHgxPSIxMCIgeDI9IjgiIHkxPSI5IiB5Mj0iOSIvPjwvc3ZnPg%3D%3D" alt="RUNTIME">
  <hr>
</div>

<img src="assets/videos/preview.gif" alt="Walkthrough" width="100%">

<div align="center">
  <p>
    <i> A real-time, zero-cost proprietary trading dashboard that analyzes order flow and cross-correlation between leading and lagging crypto assets. </i>
  </p>
  <hr style="width:30%;">
</div>

Welcome to **Trading View**. This component provides a local, high-frequency dashboard designed to calculate statistical cross-correlation and order flow imbalance (OFI) on live cryptocurrency tick data via public WebSockets.

---

## Features

### Data Ingestion & Analysis
*   **Real-Time WebSocket Engine**: Streams tick-by-tick public trade and limit order book data directly from Binance at zero cost.
*   **Cross-Correlation Function (CCF)**: Continually measures the microsecond lag correlation between a Lead asset (BTC) and a Lag asset (SOL).
*   **Order Flow Imbalance (OFI)**: Evaluates bid/ask pressure at the top of the order book to confirm signal direction.

### Runtime & Performance
*   **In-Memory Ring Buffers**: Uses sliding windows to maintain high read/write performance on tick data directly in memory.
*   **Anti-Bleed Style Isolation**: Scopes layout components under rigid container class keys, preventing CSS leakage into host Obsidian workspace configurations.
*   **Immersive Full-Tab Dashboard**: Uses Datacore's native reparenting to present an edge-to-edge trading workspace overlay.

---

## Directory Index & Components

The package exposes the following compiled files:

| File | Description |
| :--- | :--- |
| **[TRADING VIEW.md](TRADING%20VIEW.md)** | The main entry point leaf designed to be loaded inside Obsidian panes. |
| **[src/index.jsx](src/index.jsx)** | Main bootstrap application loader and full-tab viewport injector. |
| **[METADATA.md](METADATA.md)** | Packaging manifest outlining indexing, target, and security configurations. |
| **[CONTRIBUTION.md](CONTRIBUTION.md)** | Contributor architecture standards and local compilation guidelines. |
| **[LICENSE.md](LICENSE.md)** | MIT open-source license. |

---

## AI Agent Integration (MCP Bridge)

The component includes a native **MCP Bridge** to allow AI coding assistants and autonomous agents to monitor market data and execute paper trades directly through the UI.

### 1. Monitoring Component State
AI agents can read [data/mcp_state.json](data/mcp_state.json) to retrieve real-time state:
*   **connectionStatus**: `'Connected'`, `'Connecting'`, or `'Disconnected'`.
*   **activeHost**: Current WebSocket connection node (`stream.binance.com` or fallback `stream.binance.us`).
*   **leadAsset (BTC)** & **lagAsset (SOL)**: Instantaneous prices, OFI (Order Flow Imbalance), and spreads.

### 2. AI-Triggered Trade Execution
To execute a trade or reload the component, the AI writes a command payload directly to [data/mcp_commands.json](data/mcp_commands.json). 

The component checks this file every 1.5 seconds. If it finds `executed: false`, it triggers the operation, locks the state to prevent duplicate fills, and writes back the execution results.

#### Buy Command Example:
```json
{
  "action": "buy",
  "qty": 5,
  "executed": false
}
```

#### Sell Command Example:
```json
{
  "action": "sell",
  "qty": 10,
  "executed": false
}
```

#### Reload UI Example:
```json
{
  "action": "reload",
  "executed": false
}
```
Once processed, the component automatically updates the command file to:
```json
{
  "action": "buy",
  "qty": 5,
  "executed": true,
  "executedAt": "2026-06-07T03:22:04.120Z",
  "status": "success",
  "result": {
    "id": "alpaca-order-uuid-here"
  }
}
```

---

## Quick Start

1. Download the Repository (cloning or downloading into the Obsidian vault folder).
2. Install Datacore (ensuring the plugin is active).
3. Open the Entry Note (specifying the exact loader note `TRADING VIEW.md`).

---

## Previews

| Preview                                   | Description                                                                |
| :---------------------------------------- | :------------------------------------------------------------------------- |
| ![Preview 1](assets/image/preview_1.webp) | Real-time normalized price tracking dashboard showing Lead and Lag assets. |

---

## Contributors

- beto.group

### Core Implementation Code & Architecture
#### File: `data/mcp_commands.json`
```python
{"action":"reload","timestamp":1780773000000,"executed":false}
```

#### File: `manifest.json`
```python
{
  "id": "eslint-verifier-dummy",
  "name": "ESLint Verifier Dummy",
  "version": "1.0.0",
  "minAppVersion": "1.4.11",
  "description": "Dummy manifest to satisfy eslint-plugin-obsidianmd load requirements.",
  "author": "beto.group",
  "isDesktopOnly": false
}
```

#### File: `data/macro_history.json`
```python
{
  "timestamp": 1780773423056,
  "host": "stream.binance.us:9443",
  "history": [
    {
      "leadO": 66005.5,
      "leadH": 69500,
      "leadL": 65871.43,
      "leadC": 68405,
      "lagO": 82.02,
      "lagH": 86.98,
      "lagL": 81.72,
      "lagC": 84.92,
      "time": "Mar 9"
    },
    {
      "leadO": 68439.28,
      "leadH": 71776.32,
      "leadL": 68439.28,
      "leadC": 69814.67,
      "lagO": 84.95,
      "lagH": 88.78,
      "lagL": 84.95,
      "lagC": 85.61,
      "time": "Mar 10"
    },
    {
      "leadO": 69790.8,
      "leadH": 70939.02,
      "leadL": 68895.45,
      "leadC": 70150,
      "lagO": 85.66,
      "lagH": 87.67,
      "lagL": 84.13,
      "lagC": 86.6,
      "time": "Mar 11"
    },
    {
      "leadO": 70177.32,
      "leadH": 70774.79,
      "leadL": 69150,
      "leadC": 70615.66,
      "lagO": 86.6,
      "lagH": 87.58,
      "lagL": 84.76,
      "lagC": 87,
      "time": "Mar 12"
    },
    {
      "leadO": 70462.2,
      "leadH": 73862.95,
      "leadL": 70462.2,
      "leadC": 70929.47,
      "lagO": 86.81,
      "lagH": 92.9,
      "lagL": 86.81,
      "lagC": 88.09,
      "time": "Mar 13"
    },
    {
      "leadO": 70929.47,
      "leadH": 71289.48,
      "leadL": 70361.45,
      "leadC": 71244.33,
      "lagO": 88.09,
      "lagH": 88.69,
      "lagL": 86.68,
      "lagC": 88.07,
      "time": "Mar 14"
    },
    {
      "leadO": 71213.39,
      "leadH": 73200,
      "leadL": 70900,
      "leadC": 72815.5,
      "lagO": 88.08,
      "lagH": 93.18,
      "lagL": 87.38,
      "lagC": 92.09,
      "time": "Mar 15"
    },
    {
      "leadO": 72815.5,
      "leadH": 74898.79,
      "leadL": 72329.97,
      "leadC": 74824.75,
      "lagO": 92.55,
      "lagH": 97.57,
      "lagL": 91.33,
      "lagC": 96.05,
      "time": "Mar 16"
    },
    {
      "leadO": 74851.35,
      "leadH": 76070.02,
      "leadL": 73447.59,
      "leadC": 73972.98,
      "lagO": 95.96,
      "lagH": 96.75,
      "lagL": 93.33,
      "lagC": 94.73,
      "time": "Mar 17"
    },
    {
      "leadO": 73978.2,
      "leadH": 74687.89,
      "leadL": 70521.39,
      "leadC": 71250.33,
      "lagO": 94.77,
      "lagH": 95.61,
      "lagL": 88.61,
      "lagC": 89.93,
      "time": "Mar 18"
    },
    {
      "leadO": 71250.24,
      "leadH": 71593.63,
      "leadL": 68800,
      "leadC": 69987.08,
      "lagO": 90.1,
      "lagH": 91.34,
      "lagL": 87.09,
      "lagC": 88.97,
      "time": "Mar 19"
    },
    {
      "leadO": 69905,
      "leadH": 71284.19,
      "leadL": 69451.99,
      "leadC": 70505.25,
      "lagO": 89.29,
      "lagH": 90.31,
      "lagL": 88.14,
      "lagC": 89.79,
      "time": "Mar 20"
    },
    {
      "leadO": 70527.86,
      "leadH": 71085.91,
      "leadL": 68600.67,
      "leadC": 68721.15,
      "lagO": 89.91,
      "lagH": 90.72,
      "lagL": 87.25,
      "lagC": 87.33,
      "time": "Mar 21"
    },
    {
      "leadO": 68903.5,
      "leadH": 69575.1,
      "leadL": 67404.24,
      "leadC": 67866.69,
      "lagO": 87.59,
      "lagH": 89.17,
      "lagL": 85.21,
      "lagC": 86.2,
      "time": "Mar 22"
    },
    {
      "leadO": 67861,
      "leadH": 71800,
      "leadL": 67500,
      "leadC": 70953.95,
      "lagO": 86.43,
      "lagH": 92.13,
      "lagL": 85.11,
      "lagC": 91.51,
      "time": "Mar 23"
    },
    {
      "leadO": 70958.97,
      "leadH": 71315.19,
      "leadL": 68959.8,
      "leadC": 70565.25,
      "lagO": 91.55,
      "lagH": 92.07,
      "lagL": 88.41,
      "lagC": 90.79,
      "time": "Mar 24"
    },
    {
      "leadO": 70507.11,
      "leadH": 71924.58,
      "leadL": 70400.25,
      "leadC": 71267.83,
      "lagO": 91.05,
      "lagH": 93.31,
      "lagL": 90.77,
      "lagC": 91.39,
      "time": "Mar 25"
    },
    {
      "leadO": 71259.69,
      "leadH": 71336.78,
      "leadL": 68119.38,
      "leadC": 68776.47,
      "lagO": 91.68,
      "lagH": 91.74,
      "lagL": 85.45,
      "lagC": 86.48,
      "time": "Mar 26"
    },
    {
      "leadO": 68775.25,
      "leadH": 69087.37,
      "leadL": 65555,
      "leadC": 66380.89,
      "lagO": 86.32,
      "lagH": 86.75,
      "lagL": 81.9,
      "lagC": 83.09,
      "time": "Mar 27"
    },
    {
      "leadO": 66380.25,
      "leadH": 67225.51,
      "leadL": 65900,
      "leadC": 66327.39,
      "lagO": 83.12,
      "lagH": 84.19,
      "lagL": 81.84,
      "lagC": 82.04,
      "time": "Mar 28"
    },
    {
      "leadO": 66440.45,
      "leadH": 67001.33,
      "leadL": 65025,
      "leadC": 66033.42,
      "lagO": 82.25,
      "lagH": 83.18,
      "lagL": 79.05,
      "lagC": 81.51,
      "time": "Mar 29"
    },
    {
      "leadO": 66016.03,
      "leadH": 68099.19,
      "leadL": 65845.42,
      "leadC": 66680.49,
      "lagO": 81.43,
      "lagH": 84.93,
      "lagL": 81.21,
      "lagC": 82.4,
      "time": "Mar 30"
    },
    {
      "leadO": 66680.5,
      "leadH": 68484.13,
      "leadL": 65955.25,
      "leadC": 68227.07,
      "lagO": 82.44,
      "lagH": 84.43,
      "lagL": 80,
      "lagC": 82.98,
      "time": "Mar 31"
    },
    {
      "leadO": 68227.07,
      "leadH": 69231.42,
      "leadL": 67547.62,
      "leadC": 68095.25,
      "lagO": 83.23,
      "lagH": 86.53,
      "lagL": 80.8,
      "lagC": 81.3,
      "time": "Apr 1"
    },
    {
      "leadO": 68090,
      "leadH": 68603.73,
      "leadL": 65770.25,
      "leadC": 66920.25,
      "lagO": 81.16,
      "lagH": 81.69,
      "lagL": 76.79,
      "lagC": 79,
      "time": "Apr 2"
    },
    {
      "leadO": 66832.02,
      "leadH": 67348.4,
      "leadL": 66328.73,
      "leadC": 66900,
      "lagO": 79,
      "lagH": 80.87,
      "lagL": 78.94,
      "lagC": 80.22,
      "time": "Apr 3"
    },
    {
      "leadO": 66948.29,
      "leadH": 67524.11,
      "leadL": 66696.03,
      "leadC": 67289.26,
      "lagO": 80.28,
      "lagH": 81.53,
      "lagL": 79.88,
      "lagC": 80.83,
      "time": "Apr 4"
    },
    {
      "leadO": 67287.56,
      "leadH": 69115.92,
      "leadL": 66629,
      "leadC": 69001,
      "lagO": 80.74,
      "lagH": 82.09,
      "lagL": 78.58,
      "lagC": 81.95,
      "time": "Apr 5"
    },
    {
      "leadO": 69001,
      "leadH": 70326.83,
      "leadL": 68469.52,
      "leadC": 68907.87,
      "lagO": 82.31,
      "lagH": 83.07,
      "lagL": 79.72,
      "lagC": 80.15,
      "time": "Apr 6"
    },
    {
      "leadO": 68908,
      "leadH": 72736.56,
      "leadL": 67800,
      "leadC": 71985.81,
      "lagO": 80.12,
      "lagH": 86.9,
      "lagL": 78.42,
      "lagC": 85.6,
      "time": "Apr 7"
    },
    {
      "leadO": 71925.86,
      "leadH": 72800,
      "leadL": 70702.87,
      "leadC": 71157.62,
      "lagO": 85.76,
      "lagH": 85.76,
      "lagL": 82.34,
      "lagC": 82.56,
      "time": "Apr 8"
    },
    {
      "leadO": 71008.2,
      "leadH": 73108.09,
      "leadL": 70482.75,
      "leadC": 71765.85,
      "lagO": 82.54,
      "lagH": 85.91,
      "lagL": 81.45,
      "lagC": 83.27,
      "time": "Apr 9"
    },
    {
      "leadO": 71805.97,
      "leadH": 73419.35,
      "leadL": 71468.13,
      "leadC": 72962.59,
      "lagO": 83.18,
      "lagH": 85.58,
      "lagL": 82.68,
      "lagC": 84.8,
      "time": "Apr 10"
    },
    {
      "leadO": 72980.29,
      "leadH": 73797.46,
      "leadL": 72561.19,
      "leadC": 73040.76,
      "lagO": 84.73,
      "lagH": 86.27,
      "lagL": 83.88,
      "lagC": 84.73,
      "time": "Apr 11"
    },
    {
      "leadO": 73040.25,
      "leadH": 73158.28,
      "leadL": 70600.25,
      "leadC": 70744.26,
      "lagO": 84.96,
      "lagH": 84.96,
      "lagL": 81.36,
      "lagC": 81.45,
      "time": "Apr 12"
    },
    {
      "leadO": 70740.25,
      "leadH": 74904.11,
      "leadL": 69500,
      "leadC": 74428.5,
      "lagO": 81.45,
      "lagH": 86.79,
      "lagL": 81.45,
      "lagC": 86.38,
      "time": "Apr 13"
    },
    {
      "leadO": 74455.45,
      "leadH": 76059.42,
      "leadL": 73872.46,
      "leadC": 74081.9,
      "lagO": 86.62,
      "lagH": 87.67,
      "lagL": 83.38,
      "lagC": 83.84,
      "time": "Apr 14"
    },
    {
      "leadO": 74270.89,
      "leadH": 75421.78,
      "leadL": 73574.39,
      "leadC": 74816.4,
      "lagO": 84.05,
      "lagH": 85.8,
      "lagL": 82.78,
      "lagC": 84.75,
      "time": "Apr 15"
    },
    {
      "leadO": 74837.9,
      "leadH": 75536.52,
      "leadL": 73343.38,
      "leadC": 75093.46,
      "lagO": 84.75,
      "lagH": 90.47,
      "lagL": 83.89,
      "lagC": 89.02,
      "time": "Apr 16"
    },
    {
      "leadO": 75168.22,
      "leadH": 78305.12,
      "leadL": 74561.72,
      "leadC": 77127.69,
      "lagO": 89.15,
      "lagH": 90.69,
      "lagL": 87.39,
      "lagC": 88.79,
      "time": "Apr 17"
    },
    {
      "leadO": 77100,
      "leadH": 77415.28,
      "leadL": 75388.81,
      "leadC": 75750,
      "lagO": 88.9,
      "lagH": 88.97,
      "lagL": 85.96,
      "lagC": 86.28,
      "time": "Apr 18"
    },
    {
      "leadO": 75730.32,
      "leadH": 76251.2,
      "leadL": 73816.48,
      "leadC": 73852.5,
      "lagO": 86.28,
      "lagH": 87.1,
      "lagL": 83.08,
      "lagC": 83.55,
      "time": "Apr 19"
    },
    {
      "leadO": 73814.98,
      "leadH": 76556.38,
      "leadL": 73800.84,
      "leadC": 75900,
      "lagO": 83.75,
      "lagH": 86.22,
      "lagL": 83.56,
      "lagC": 85.33,
      "time": "Apr 20"
    },
    {
      "leadO": 75857.71,
      "leadH": 76884.77,
      "leadL": 74882.08,
      "leadC": 76350.73,
      "lagO": 85.48,
      "lagH": 86.88,
      "lagL": 84.43,
      "lagC": 86.11,
      "time": "Apr 21"
    },
    {
      "leadO": 76367.68,
      "leadH": 79464.21,
      "leadL": 76093.99,
      "leadC": 78240.25,
      "lagO": 86.14,
      "lagH": 89.31,
      "lagL": 86.14,
      "lagC": 86.98,
      "time": "Apr 22"
    },
    {
      "leadO": 78269.01,
      "leadH": 78669,
      "leadL": 77037.61,
      "leadC": 78281.67,
      "lagO": 86.73,
      "lagH": 86.98,
      "lagL": 84.64,
      "lagC": 86.16,
      "time": "Apr 23"
    },
    {
      "leadO": 78287,
      "leadH": 78555.21,
      "leadL": 77299.46,
      "leadC": 77463,
      "lagO": 86.07,
      "lagH": 86.93,
      "lagL": 85,
      "lagC": 86.25,
      "time": "Apr 24"
    },
    {
      "leadO": 77468.83,
      "leadH": 77873.41,
      "leadL": 77192.71,
      "leadC": 77635.27,
      "lagO": 86.23,
      "lagH": 86.74,
      "lagL": 85.55,
      "lagC": 86.15,
      "time": "Apr 25"
    },
    {
      "leadO": 77635.27,
      "leadH": 78905.5,
      "leadL": 77374.46,
      "leadC": 78652.74,
      "lagO": 86.19,
      "lagH": 87.29,
      "lagL": 85.9,
      "lagC": 87.07,
      "time": "Apr 26"
    },
    {
      "leadO": 78709.38,
      "leadH": 79472.37,
      "leadL": 76500,
      "leadC": 77385.2,
      "lagO": 87.12,
      "lagH": 88.04,
      "lagL": 83.72,
      "lagC": 84.84,
      "time": "Apr 27"
    },
    {
      "leadO": 77381.86,
      "leadH": 77478.76,
      "leadL": 75710.53,
      "leadC": 76342.41,
      "lagO": 84.68,
      "lagH": 84.69,
      "lagL": 83.03,
      "lagC": 84.06,
      "time": "Apr 28"
    },
    {
      "leadO": 76342.41,
      "leadH": 77867.51,
      "leadL": 74952.89,
      "leadC": 75774.17,
      "lagO": 84.12,
      "lagH": 85.5,
      "lagL": 81.4,
      "lagC": 83.04,
      "time": "Apr 29"
    },
    {
      "leadO": 75804.65,
      "leadH": 76603.7,
      "leadL": 75386.56,
      "leadC": 76341.35,
      "lagO": 83.15,
      "lagH": 83.94,
      "lagL": 82.23,
      "lagC": 83.06,
      "time": "Apr 30"
    },
    {
      "leadO": 76418.32,
      "leadH": 78908.61,
      "leadL": 76418.32,
      "leadC": 78225.25,
      "lagO": 83.09,
      "lagH": 84.8,
      "lagL": 83.09,
      "lagC": 83.74,
      "time": "May 1"
    },
    {
      "leadO": 78225.25,
      "leadH": 79150,
      "leadL": 78070.54,
      "leadC": 78658.87,
      "lagO": 83.69,
      "lagH": 84.91,
      "lagL": 83.49,
      "lagC": 84.29,
      "time": "May 2"
    },
    {
      "leadO": 78732.75,
      "leadH": 79404.7,
      "leadL": 78052.81,
      "leadC": 78580.45,
      "lagO": 84.23,
      "lagH": 84.9,
      "lagL": 83.62,
      "lagC": 83.88,
      "time": "May 3"
    },
    {
      "leadO": 78580.43,
      "leadH": 80728.71,
      "leadL": 78250,
      "leadC": 79834.39,
      "lagO": 83.85,
      "lagH": 85.85,
      "lagL": 83.31,
      "lagC": 84.09,
      "time": "May 4"
    },
    {
      "leadO": 79872.63,
      "leadH": 81767.78,
      "leadL": 79811.97,
      "leadC": 80952.18,
      "lagO": 84.1,
      "lagH": 86.91,
      "lagL": 84.1,
      "lagC": 86.37,
      "time": "May 5"
    },
    {
      "leadO": 80937.18,
      "leadH": 82812.95,
      "leadL": 80761.98,
      "leadC": 81435.13,
      "lagO": 86.37,
      "lagH": 89.99,
      "lagL": 86.17,
      "lagC": 89.06,
      "time": "May 6"
    },
    {
      "leadO": 81435.67,
      "leadH": 81694.82,
      "leadL": 79501.03,
      "leadC": 80024.51,
      "lagO": 89.23,
      "lagH": 90.35,
      "lagL": 87.69,
      "lagC": 88.43,
      "time": "May 7"
    },
    {
      "leadO": 80009.57,
      "leadH": 80459.08,
      "leadL": 79228.35,
      "leadC": 80213.73,
      "lagO": 88.49,
      "lagH": 92.76,
      "lagL": 87.64,
      "lagC": 91.94,
      "time": "May 8"
    },
    {
      "leadO": 80204.14,
      "leadH": 81079.94,
      "leadL": 80163.45,
      "leadC": 80708.25,
      "lagO": 91.92,
      "lagH": 94.11,
      "lagL": 91.91,
      "lagC": 93.17,
      "time": "May 9"
    },
    {
      "leadO": 80651.39,
      "leadH": 82415.16,
      "leadL": 80337.76,
      "leadC": 82132.66,
      "lagO": 93.15,
      "lagH": 96.87,
      "lagL": 92.69,
      "lagC": 96.42,
      "time": "May 10"
    },
    {
      "leadO": 82247.13,
      "leadH": 82266.2,
      "leadL": 80500,
      "leadC": 81733.94,
      "lagO": 96.56,
      "lagH": 98.33,
      "lagL": 94.37,
      "lagC": 97.44,
      "time": "May 11"
    },
    {
      "leadO": 81733.87,
      "leadH": 81781.96,
      "leadL": 79500,
      "leadC": 80517.52,
      "lagO": 97.37,
      "lagH": 97.65,
      "lagL": 93.6,
      "lagC": 94.27,
      "time": "May 12"
    },
    {
      "leadO": 80514.91,
      "leadH": 81282.04,
      "leadL": 78761.54,
      "leadC": 79263.99,
      "lagO": 94.33,
      "lagH": 95.92,
      "lagL": 90.42,
      "lagC": 91.14,
      "time": "May 13"
    },
    {
      "leadO": 79317.82,
      "leadH": 82000,
      "leadL": 78932.79,
      "leadC": 81080.15,
      "lagO": 91.18,
      "lagH": 93.57,
      "lagL": 89.94,
      "lagC": 92.21,
      "time": "May 14"
    },
    {
      "leadO": 81148.84,
      "leadH": 81618.95,
      "leadL": 78656.31,
      "leadC": 79084.77,
      "lagO": 92.16,
      "lagH": 92.58,
      "lagL": 88.58,
      "lagC": 89.22,
      "time": "May 15"
    },
    {
      "leadO": 79072,
      "leadH": 79184.14,
      "leadL": 77654.32,
      "leadC": 78100,
      "lagO": 89.11,
      "lagH": 89.32,
 
# ... [TRUNCATED FILE CONTENT]
```


==================================================
