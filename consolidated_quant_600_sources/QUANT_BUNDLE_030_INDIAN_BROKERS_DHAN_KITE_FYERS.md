# ⚡ [QUANT-SOURCE-030] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_030_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: tradehull-dhan-live-algo-skills (`WHEEL_tradehull-dhan-live-algo-skills`)
- **Full Name**: `tradehull-dhan-live-algo-skills`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Tradehull Dhan Live Algo Skills

> Agent skills for Indian algo trading with the [Dhan-Tradehull](https://pypi.org/project/Dhan-Tradehull/) Python library.
> Works with Claude Code, Cursor, Codex, and any [SKILL.md](https://agentskills.io)-compatible agent.

---

## Install

### Claude Code
```bash
npx skills add Imran-Tradehull/tradehull-dhan-live-algo-skills --skill dhan-tradehull
```

### Cursor
```bash
npx skills add Imran-Tradehull/tradehull-dhan-live-algo-skills --skill dhan-tradehull --agent cursor
```

### Codex
```bash
npx skills add Imran-Tradehull/tradehull-dhan-live-algo-skills --skill dhan-tradehull --agent codex
```

### Manual
```bash
git clone https://github.com/Imran-Tradehull/tradehull-dhan-live-algo-skills.git
cp -r tradehull-dhan-live-algo-skills/skills/dhan-tradehull .cursor/skills/
```

---

## Requirements

```bash
pip install dhanhq==2.2.0
pip install Dhan-Tradehull==3.3.2
```

---

## What's inside

```
skills/dhan-tradehull/
│
├── SKILL.md                              ← entry point · quick reference · routing table
│
├── references/
│   ├── coding-style.md                   ← TradeHull coding style · read before writing any code
│   ├── auth.md                           ← login modes · token validity · Dependencies folder
│   ├── market-data.md                    ← LTP · OHLC · quote · historical · long-term
│   ├── options.md                        ← option chain · ATM/OTM/ITM · greeks · expired data
│   ├── orders.md                         ← order placement · SEBI rules · super · forever orders
│   ├── portfolio.md                      ← holdings · positions · orderbook · balance · P&L
│   ├── utilities.md                      ← lot size · margin · Telegram · kill switch
│   ├── instruments.md                    ← 225k-row instrument file schema · security IDs
│   ├── common-patterns.md                ← real code patterns from student support sessions
│   ├── answer-patterns.md                ← common mistakes · FAQ · answer style
│   ├── algo-intraday-options.md          ← intraday algo anatomy (Supertrend + S/R)
│   ├── algo-positional-spread.md         ← positional spread algo anatomy (delta-based)
│   ├── dhanhq-raw.md                     ← raw dhanhq fallback (position convert · eDIS · exit all)
│   └── error-log.md                      ← known errors · SEBI regulations
│
└── examples/
    ├── intraday_options_algo.py          ← real production intraday algo
    └── positional_spread_algo.py        ← real production positional algo
```

---

## What the skill covers

| Domain | Details |
|--------|---------|
| **Authentication** | `access_token`, `pin_totp`, `api_key` modes · token validity rules |
| **Market Data** | LTP · OHLC · full quote · historical · long-term · sector indices · India VIX |
| **Options** | Option chain with greeks · ATM/OTM/ITM strike selection · expired options data |
| **Orders** | LIMIT · STOPLIMIT · super orders · forever/GTT orders · slicing · AMO |
| **SEBI Rules** | MARKET orders banned for F&O from Apr 2026 · correct LIMIT price patterns |
| **Portfolio** | Holdings · open positions · orderbook · tradebook · live P&L · balance |
| **Utilities** | Dynamic lot size · margin calculator · Telegram alerts · P&L exit · kill switch |
| **Instruments** | 225k-row CSV schema · security ID lookup · expiry flags · tick size |
| **Algo Patterns** | Completed candle · orderbook state machine · trailing SL · re-entry · JSON persistence |
| **Coding Style** | Vertical alignment · bc/sc conditions · block comments · flat structure |
| **Fallback** | Raw `dhanhq` access for position conversion · eDIS · exit-all · trade history |

---

## How it works

Skills are loaded progressively — `SKILL.md` is the entry point and routes the agent to specific reference files only when needed. This keeps context lean while giving the agent deep knowledge on demand.

```
Agent receives task
       ↓
Loads SKILL.md  (always)
       ↓
Loads relevant reference file(s)  (on demand)
  e.g. options.md + orders.md for a spread strategy task
       ↓
Writes code in TradeHull style with correct signatures
```

---

## Key rules baked into the skill

- **MARKET orders banned for F&O** — SEBI regulation Apr 1 2026. Skill always generates LIMIT orders for NFO/BFO
- **`get_option_chain()` returns two values** — `atm, chain = tsl.get_option_chain(...)` — skill enforces this
- **Lot size always dynamic** — `tsl.get_lot_size()` never hardcoded — SEBI revises periodically
- **`get_intraday_data()` deprecated** — skill always uses `get_historical_data()`
- **Conditional triggers not used** — TradeHull uses TA-Lib for all signal logic
- **Super orders for intraday · Forever orders for positional** — skill picks the right one

---

## About TradeHull

[TradeHull](https://tradehull.com) is India's algo trading education and tooling platform — building courses, frameworks, and tools for retail traders on the Dhan API.

- Website: [tradehull.com](https://tradehull.com)
- Python library: [pypi.org/project/Dhan-Tradehull](https://pypi.org/project/Dhan-Tradehull/)
- Dhan API docs: [docs.dhanhq.co](https://docs.dhanhq.co)

---

## License

MIT — free to use, modify, and distribute.

### Core Implementation Code & Architecture
#### File: `skills/dhan-tradehull/examples/nifty50_scanner_algo.py`
```python
# -------------------------------------------------------------------
# NIFTY 50 Scanner  —  EMA20/50 crossover confirmed by RSI
#
# Timeframe : 5 minute
# Bullish   : EMA20 crosses ABOVE EMA50  AND  RSI > 60
# Bearish   : EMA20 crosses BELOW EMA50  AND  RSI < 40
#
# Requires  : pip install Dhan-Tradehull TA-Lib
# See       : references/algo-scanner.md, references/flask-ui.md
# -------------------------------------------------------------------

import talib
from Dhan_Tradehull import Tradehull

# ---- credentials --------------------------------------------------
# Put these in a private config.py and `from config import ...` instead
# of hardcoding. access_token expires DAILY — regenerate each morning.
client_code = "YOUR_CLIENT_CODE"
token_id    = "YOUR_ACCESS_TOKEN"

# ---- single shared broker session ---------------------------------
tsl = Tradehull(client_code, token_id)

# ---- NIFTY 50 constituents (edit when the index reshuffles) -------
nifty50_stocks = [
    "ADANIENT",   "ADANIPORTS", "APOLLOHOSP", "ASIANPAINT", "AXISBANK",
    "BAJAJ-AUTO", "BAJFINANCE", "BAJAJFINSV", "BEL",        "BHARTIARTL",
    "CIPLA",      "COALINDIA",  "DRREDDY",    "EICHERMOT",  "GRASIM",
    "HCLTECH",    "HDFCBANK",   "HDFCLIFE",   "HEROMOTOCO", "HINDALCO",
    "HINDUNILVR", "ICICIBANK",  "INDUSINDBK", "INFY",       "ITC",
    "JSWSTEEL",   "KOTAKBANK",  "LT",         "M&M",        "MARUTI",
    "NESTLEIND",  "NTPC",       "ONGC",       "POWERGRID",  "RELIANCE",
    "SBILIFE",    "SBIN",       "SHRIRAMFIN", "SUNPHARMA",  "TATACONSUM",
    "TATAMOTORS", "TATASTEEL",  "TCS",        "TECHM",      "TITAN",
    "TRENT",      "ULTRACEMCO", "WIPRO",      "JIOFIN",
]


def scan_stock(symbol):
    """Scan one stock. Return a signal dict, or None if no signal / error."""

    # ---- pull 5-min candles, skip on error ------------------------
    try:
        chart = tsl.get_historical_data(tradingsymbol=symbol, exchange="NSE", timeframe="5")
    except Exception:
        return None

    if chart is None or len(chart) < 60:      # need enough bars for EMA50
        return None

    # ---- indicators -----------------------------------------------
    chart["ema20"] = talib.EMA(chart["close"], timeperiod=20)
    chart["ema50"] = talib.EMA(chart["close"], timeperiod=50)
    chart["rsi"]   = talib.RSI(chart["close"], timeperiod=14)

    rc             = chart.iloc[-1]     # last completed candle
    pc             = chart.iloc[-2]     # previous candle

    # ---- crossover state flip -------------------------------------
    bull_cross     = (pc["ema20"] <= pc["ema50"]) and (rc["ema20"] > rc["ema50"])
    bear_cross     = (pc["ema20"] >= pc["ema50"]) and (rc["ema20"] < rc["ema50"])

    # ---- buy conditions -------------------------------------------
    bc1            = bull_cross
    bc2            = rc["rsi"] > 60

    # ---- sell conditions ------------------------------------------
    sc1            = bear_cross
    sc2            = rc["rsi"] < 40

    if bc1 and bc2:
        signal = "BULLISH"
    elif sc1 and sc2:
        signal = "BEARISH"
    else:
        return None

    return {
        "symbol": symbol,
        "signal": signal,
        "ltp":    round(float(rc["close"]), 2),
        "ema20":  round(float(rc["ema20"]), 2),
        "ema50":  round(float(rc["ema50"]), 2),
        "rsi":    round(float(rc["rsi"]),   2),
    }


def run_scan():
    """Scan the whole NIFTY 50 list. Return list of signal dicts."""

    signals = []
    for symbol in nifty50_stocks:
        row = scan_stock(symbol)
        if row is not None:
            signals.append(row)
    return signals


if __name__ == "__main__":
    hits = run_scan()
    print(f"Signals found: {len(hits)}")
    for r in hits:
        print(r)
```

#### File: `skills/dhan-tradehull/examples/positional_spread_algo.py`
```python
from Dhan_Tradehull import Tradehull
from rich import print
import talib
import pandas as pd
import datetime
import xlwings as xw
import pretty_errors
import tradehull_backtesting as tb
import os
import pdb
import time
import json




client_code           = "YOUR_CLIENT_CODE"
access_token          = "YOUR_ACCESS_TOKEN"
tsl                   = Tradehull(client_code, access_token)
watchlist             = ['NIFTY','TCS', 'WIPRO']
status                = {'traded':None, 'options_name':None}
re_entry              = False
EXIT_TIME             = datetime.time(23, 35, 59)
ENTRY_TIME            = datetime.time(9, 35, 40)

with open("positional_orderbook.json", "r") as f:
	loaded_data = json.load(f)
	orderbook             = loaded_data['orderbook']
	complted_orderbook    = loaded_data['complted_orderbook']





while True:

	current_dt     = datetime.datetime.now()
	current_time   = current_dt.time()

	if current_time < ENTRY_TIME:
		print(f"{current_time}Waiting for the market to open")
		continue

	current_pnl  = tsl.get_live_pnl()
	market_over  = current_time > EXIT_TIME


	
	if market_over:
		print(f"{current_time} Exiting the Algo")


		with open("positional_orderbook.json", "w") as f:
			send_data = {'orderbook':orderbook, 'complted_orderbook':complted_orderbook}
			json.dump(send_data, f, indent=4)




		dhan_orderbook = tsl.get_orderbook()
		logs           = pd.DataFrame(orderbook).T
		positionbook   = tsl.get_positions()

		path = f"Logs/{str(datetime.datetime.now().date())}"
		os.makedirs(f"{path}", exist_ok=True)

		dhan_orderbook.to_csv(f"{path}/dhan_orderbook.csv")
		logs.to_csv(f"{path}/logs.csv")
		positionbook.to_csv(f"{path}/positionbook.csv")

		break






	for name in watchlist:        


		chart        = tsl.get_historical_data(tradingsymbol='NIFTY', exchange='INDEX', timeframe="60")
		chart        = chart.set_index('timestamp')
		chart        = tb.supertrend(df=chart, atr_period=10, atr_multiplier=3)
		comp_candle  = chart.iloc[-1]


		
		bc1 = comp_candle['STX_10_3'] == 'up'
		bc2 = orderbook[name]['traded'] is None

		sc1 = comp_candle['STX_10_3'] == 'down'
		sc2 = orderbook[name]['traded'] is None


		# -------------------------------------------- Bullish Block Sell Puts  --------------------------------------------

		if bc1 and bc2:
			print(f"{name}  Uptrend")

			expiry_no    = tsl.get_expiry_list('NIFTY', 'INDEX').index(tsl.get_expiry_list('NIFTY', 'NFO')[1])
			atm, oc      = tsl.get_option_chain(Underlying="NIFTY", exchange="INDEX", expiry=expiry_no, num_strikes=50)


			oc['PE Delta']           = abs(oc['PE Delta'])
			selling_strike           = str(int(oc[oc['PE Delta'].between(0.10, 0.16)].sort_values('PE OI').iloc[-1]['Strike Price']))
			hedging_strike           = str(int(oc[oc['PE Delta'].between(0.07, 0.09)].sort_values('PE OI').iloc[-1]['Strike Price']))

			ce_name, pe_name, strike = tsl.ATM_Strike_Selection(Underlying=name, Expiry=expiry_no)
			nap                      = ce_name.split(" ")  # name parts
			selling_name             = f"{name} {nap[1]} {nap[2]} {selling_strike} PUT"
			hedging_name             = f"{name} {nap[1]} {nap[2]} {hedging_strike} PUT"

			lot_size                 = tsl.get_lot_size(selling_name)


			options_ltp            = tsl.get_ltp_data(names=[selling_name, hedging_name])
			selling_ltp            = options_ltp[selling_name]
			hedging_ltp            = options_ltp[hedging_name]

			hedging_entry_price   = round(hedging_ltp * 1.03, 1)
			selling_entry_price   = round(selling_ltp * 0.97, 1)
			selling_exit_price    = round(selling_ltp * 1.03, 1)

			try:
				hedging_orderid  = tsl.order_placement(tradingsymbol=hedging_name, exchange='NFO', quantity=lot_size, price=hedging_entry_price, trigger_price=0,order_type='LIMIT', transaction_type='BUY', trade_type='MARGIN', amo_time='OPEN', after_market_order=True )
				time.sleep(1)
				hedging_status = tsl.get_order_status(orderid=hedging_orderid)

				if hedging_status == 'suscessfull':
					selling_orderid  = tsl.order_placement(tradingsymbol=selling_name, exchange='NFO', quantity=lot_size, price=selling_entry_price, trigger_price=0,order_type='LIMIT', transaction_type='SELL', trade_type='MARGIN', amo_time='OPEN', after_market_order=True)
					time.sleep(1)
					selling_status = tsl.get_order_status(orderid=selling_orderid)
					if selling_status == 'un-suscessfull':
						exit_hedging   = tsl.order_placement(tradingsymbol=hedging_name, exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='LIMIT', transaction_type='SELL', trade_type='MARGIN', amo_time='OPEN', after_market_order=True)
				else:
					continue

			except Exception as e:
				print(e)
				continue









			orderbook[name]['selling_name']      = selling_name
			orderbook[name]['hedging_name']      = hedging_name

			orderbook[name]['selling_orderid']    = selling_orderid
			orderbook[name]['hedging_orderid']    = hedging_orderid
			orderbook[name]['qty']                = lot_size

			orderbook[name]['selling_price']      = tsl.get_executed_price(orderid=orderbook[name]['selling_orderid'])
			orderbook[name]['hedging_price']      = tsl.get_executed_price(orderid=orderbook[name]['hedging_orderid'])
			orderbook[name]['max_profit']         = (orderbook[name]['selling_price'] - orderbook[name]['hedging_price'])*orderbook[name]['qty']

			orderbook[name]['sl_pnl']            = round(orderbook[name]['max_profit']*0.7*-1, 2)
			orderbook[name]['tg_pnl']            = round(orderbook[name]['max_profit']*0.7*1,  2)

			orderbook[name]['date']              = str(datetime.datetime.now())
			orderbook[name]['view']              = 'Bullish'
			orderbook[name]['traded']            = True
			orderbook[name]['expiry']            = tsl.get_expiry_list('NIFTY', 'NFO')[1]


		# -------------------------------------------- Bearish Block Sell Calls  --------------------------------------------

		if sc1 and sc2:
			print(f"{name}  Downtrend")

			expiry_no    = tsl.get_expiry_list('NIFTY', 'INDEX').index(tsl.get_expiry_list('NIFTY', 'NFO')[1])
			atm, oc      = tsl.get_option_chain(Underlying="NIFTY", exchange="INDEX", expiry=expiry_no, num_strikes=50)

			selling_strike           = str(int(oc[oc['CE Delta'].between(0.10, 0.16)].sort_values('CE OI').iloc[-1]['Strike Price']))
			hedging_strike           = str(int(oc[oc['CE Delta'].between(0.07, 0.09)].sort_values('CE OI').iloc[-1]['Strike Price']))

			ce_name, pe_name, strike = tsl.ATM_Strike_Selection(Underlying=name, Expiry=expiry_no)
			nap                      = ce_name.split(" ")  # name parts
			selling_name             = f"{name} {nap[1]} {nap[2]} {selling_strike} CALL"
			hedging_name             = f"{name} {nap[1]} {nap[2]} {hedging_strike} CALL"

			lot_size                 = tsl.get_lot_size(selling_name)


			options_ltp            = tsl.get_ltp_data(names=[selling_name, hedging_name])
			selling_ltp            = options_ltp[selling_name]
			hedging_ltp            = options_ltp[hedging_name]
			
			selling_entry_price    = selling_ltp * 0.995
			hedging_entry_price    = hedging_ltp * 1.005
			selling_exit_price     = selling_ltp * 1.005


			try:
				hedging_orderid  = tsl.order_placement(tradingsymbol=hedging_name, exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='LIMIT', transaction_type='BUY', trade_type='MARGIN')
				time.sleep(1)
				hedging_status = tsl.get_order_status(orderid=hedging_orderid)

				if hedging_status == 'TRADED':

					selling_orderid  = tsl.order_placement(tradingsymbol=selling_name, exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='LIMIT', transaction_type='SELL', trade_type='MARGIN')
					time.sleep(1)
					selling_status = tsl.get_order_status(orderid=selling_orderid)

					if selling_status != 'TRADED':
						exit_selling   = tsl.order_placement(tradingsymbol=selling_name, exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='LIMIT', transaction_type='BUY', trade_type='MARGIN')

			except Exception as e:
				print(e)
				continue




			orderbook[name]['selling_name']      = selling_name
			orderbook[name]['hedging_name']      = hedging_name

			orderbook[name]['selling_orderid']    = selling_orderid
			orderbook[name]['hedging_orderid']    = hedging_orderid
			orderbook[name]['qty']                = lot_size

			orderbook[name]['selling_price']      = tsl.get_executed_price(orderid=orderbook[name]['selling_orderid'])
			orderbook[name]['hedging_price']      = tsl.get_executed_price(orderid=orderbook[name]['hedging_orderid'])
			orderbook[name]['max_profit']         = (orderbook[name]['selling_price'] - orderbook[name]['hedging_price'])*orderbook[name]['qty']

			orderbook[name]['sl_pnl']            = round(orderbook[name]['max_profit']*0.7*-1, 2)
			orderbook[name]['tg_pnl']            = round(orderbook[name]['max_profit']*0.7*1,  2)

			orderbook[name]['date']              = str(datetime.datetime.now())
			orderbook[name]['view']              = 'Bearish'
			orderbook[name]['traded']            = True
			orderbook[name]['expiry']            = tsl.get_expiry_list('NIFTY', 'NFO')[1]


		# -------------------------------------------- Trailing Stop Loss and Take Profit  --------------------------------------------


		if orderbook[name]['traded']:

			bullish = orderbook[name]['view'] == 'Bullish'
			bearish = orderbook[name]['view'] == 'Bearish'

			if bullish or bearish:

				ltps                    = tsl.get_ltp_data(names=[orderbook[name]['selling_name'], orderbook[name]['hedging_name']])
				sold_ltp                = ltps[orderbook[name]['selling_name']]
				hedged_ltp              = ltps[orderbook[name]['hedging_name']]

				selling_pnl             = (orderbook[name]['selling_price'] - sold_ltp)*orderbook[name]['qty']
				hedging_pnl             = (hedged_ltp - orderbook[name]['hedging_price'])*orderbook[name]['qty']

				orderbook[name]['pnl']  = selling_pnl + hedging_pnl

				sl_hit                  = orderbook[name]['pnl'] <  orderbook[name]['sl_pnl']
				tg_hit                  = orderbook[name]['pnl'] >  orderbook[name]['tg_pnl']
				only_few_days_left      = ((pd.to_datetime(orderbook[name]['expiry']) - datetime.datetime.now()).days < 30) and  (datetime.datetime.now().time() > datetime.time(14, 30))



				if bullish:
					trailing_exit   = comp_candle['STX_10_3'] == 'down'
				if bearish:
					trailing_exit   = comp_candle['STX_10_3'] == 'up'


				if trailing_exit or sl_hit or tg_hit or only_few_days_left:


					selling_exit_orderid  = tsl.order_placement(tradingsymbol=orderbook[name]['selling_name'], exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='LIMIT', transaction_type='BUY', trade_type='MARGIN')
					time.sleep(2)
					hedging_exit_orderid  = tsl.order_placement(tradingsymbol=orderbook[name]['hedging_price'], exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='LIMIT', transaction_type='SELL', trade_type='MARGIN')


					orderbook[name]['selling_exit_orderid'] = selling_exit_orderid
					orderbook[name]['hedging_exit_orderid'] = hedging_exit_orderid

					remark                                 = "trailing_exit" if trailing_exit else "sl_hit" if sl_hit else "tg_hit" if tg_hit else "only_few_days_left" if only_few_days_left else None
					orderbook[name]['selling_exit_price']  = tsl.get_executed_price(orderid=orderbook[name]['selling_exit_orderid'])
					orderbook[name]['hedging_exit_price']  = tsl.get_executed_price(orderid=orderbook[name]['hedging_exit_orderid'])
					orderbook[name]['exit_time']           = str(datetime.datetime.now())
					orderbook[name]['remark']              = remark

					complted_orderbook.append(orderbook[name])						
					orderbook[name] = status.copy()
```

#### File: `skills/dhan-tradehull/examples/intraday_options_algo.py`
```python
# NOTE: This algo was written before the SEBI MARKET order ban (Apr 1 2026).
# order_type='MARKET' for NFO is now BANNED — must be replaced with LIMIT.
# Pattern: ltp = tsl.get_ltp_data([name])[name]; price = round(ltp * 1.02, 1)
# All logic, structure, and patterns remain valid — only order_type needs updating.
# See references/orders.md for the current LIMIT order pattern.

from Dhan_Tradehull import Tradehull
from rich import print
import talib
import pandas as pd
import datetime
import time
import xlwings as xw
import pretty_errors
import tradehull_backtesting as tb
import os
print()

book                  = xw.Book('Algo1.xlsx')
orderbook_sheet       = book.sheets['Live Orderbook']
completed_sheet       = book.sheets['Completed_Orderbook']
config_sheet          = book.sheets['Strategy Config']
client_code           = str(int(config_sheet.range('B1').value))
access_token          = config_sheet.range('B2').value.replace(" ", "")
tsl                   = Tradehull(client_code, access_token)
watchlist             = [name for name in config_sheet.range('D2:D1000').value if name is not None]
status                = {'traded':None, 'options_name':None}
re_entry              = True
max_orders            = int(config_sheet.range('B10').value)
orderbook             = {name:status.copy() for name in watchlist}
complted_orderbook    = []
EXIT_TIME             = datetime.time(15, 35, 59)
ENTRY_TIME            = datetime.time(9, 35, 40)
opening_balance       = 100000#tsl.get_balance()
max_loss_pct          = config_sheet.range('B9').value
max_loss              = opening_balance * max_loss_pct * -1


orderbook_sheet.range('A1:Z100').value = None
completed_sheet.range('A1:Z100').value = None


# Pre calculate data
sr_data = {}
for name in watchlist:
	print(f"Calculating data for support and resistance for {name}")
	daily         = tsl.get_historical_data(tradingsymbol=name, exchange='NSE', timeframe="DAY")
	sr            = tb.get_support_and_resistance(daily.iloc[-2])
	sr_data[name] = sr
	time.sleep(0.35)



while True:


	current_time = datetime.datetime.now().time()

	if current_time < ENTRY_TIME:
		print(f"{current_time}Waiting for the market to open")
		continue

	current_pnl  = tsl.get_live_pnl()
	market_over  = current_time > EXIT_TIME
	panic_exit   = config_sheet.range('B8').value is not None
	max_loss_hit = current_pnl < max_loss


	# Todo : Testing Pedning
	if market_over or panic_exit or max_loss_hit:
		print(f"{current_time} Exiting the Algo")


		order_details = tsl.cancel_all_orders()
		dhan_orderbook = tsl.get_orderbook()
		logs           = pd.DataFrame(orderbook).T
		positionbook   = tsl.get_positions()

		path = f"Logs/{str(datetime.datetime.now().date())}"
		os.makedirs(f"{path}", exist_ok=True)

		dhan_orderbook.to_csv(f"{path}/dhan_orderbook.csv")
		logs.to_csv(f"{path}/logs.csv")
		positionbook.to_csv(f"{path}/positionbook.csv")

		break






	for name in watchlist:        

		print(f"Scanning {name}")
		odf                               = pd.DataFrame(orderbook).T
		orderbook_sheet.range('A1').value = odf
		completed_sheet.range('A1').value = pd.DataFrame(complted_orderbook)
		current_dt                        = datetime.datetime.now()

		chart        = tsl.get_historical_data(tradingsymbol=name, exchange='NSE', timeframe="5") # in get_start_date.. use timedelta for 15 days only
		chart        = chart.set_index('timestamp')
		chart['rsi'] = talib.RSI(chart['close'], timeperiod=14)
		chart        = tb.supertrend(df=chart, atr_period=15, atr_multiplier=3)

		comp_candle  = pd.Series(datetime.datetime.now()).dt.floor('5min')[0] - datetime.timedelta(minutes=5)
		comp_candle  = comp_candle.strftime("%Y-%m-%d %H:%M:%S+05:30")
		comp_candle  = chart.loc[comp_candle]

		# comp_candle  = chart.iloc[-1]
		sr           = sr_data[name]


		
		bc1 = True#comp_candle['rsi'] > 60
		bc2 = comp_candle['STX_15_3'] == 'up'
		bc3 = orderbook[name]['traded'] is None
		bc4 = comp_candle['close'] > sr['r1']
		bc5 = (len(complted_orderbook) +  odf[odf["traded"].notna()].shape[0]) < max_orders

		sc1 = True#comp_candle['rsi'] < 40
		sc2 = comp_candle['STX_15_3'] == 'down'
		sc3 = orderbook[name]['traded'] is None
		sc4 = comp_candle['close'] < sr['s1']
		sc5 = (len(complted_orderbook) +  odf[odf["traded"].notna()].shape[0]) < max_orders




		# logger.info(f"{name} {bc1} {bc2} {bc3} {bc4} {bc5} {sc1} {sc2} {sc3} {sc4} {sc5}")
		# logger.info(f"{comp_candle}")


		if bc1 and bc2 and bc3 and bc4 and bc5:

			print(f"{name}  Uptrend")
			ce_name, pe_name, strike = tsl.ATM_Strike_Selection(Underlying=name, Expiry=0)
			lot_size                 = tsl.get_lot_size(ce_name)


			try:
				orderbook[name]['qty']               = lot_size*6
				entry_orderid                        = tsl.order_placement(tradingsymbol=ce_name, exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='MARKET', transaction_type='BUY', trade_type='MIS')
				orderbook[name]['entry_price']       = tsl.get_ltp_data(names=[ce_name])[ce_name] # tsl.get_executed_price(orderid=orderid)
			except Exception as e:
				print(f"Error placing entry order: {e}")
				continue
			
			
			try:
				trigger_price                  = round(orderbook[name]['entry_price']*0.7, 1)
				price                          = max(trigger_price - 0.5, 0.1)
				sl_orderid                     = tsl.order_placement(tradingsymbol=ce_name, exchange='NFO', quantity=lot_size, price=price, trigger_price=trigger_price,order_type='STOPLIMIT', transaction_type='SELL', trade_type='MIS')
			except Exception as e:
				print(f"Error placing SL order: {e}")
				cancel_entry_order             = tsl.cancel_order(OrderID=entry_orderid)
				orderbook[name]                = {'traded':"TRADE_NOT_POSSIBLE", 'options_name':None}
				continue





			orderbook[name]['options_name']      = ce_name
			orderbook[name]['date']              = str(current_dt.date())
			orderbook[name]['entry_time']        = str(current_dt.time())
			orderbook[name]['sl_price']          = trigger_price
			orderbook[name]['tg_price']          = round(orderbook[name]['entry_price']*1.3, 1)
			orderbook[name]['buy_sell']          = 'BUY_CE'
			orderbook[name]['traded']            = True
			orderbook[name]['entry_orderid']     = entry_orderid
			orderbook[name]['sl_orderid']         = sl_orderid
			orderbook[name]['entry_datetime']    = current_dt
			orderbook[name]['breaked_even']      = False



		if sc1 and sc2 and sc3 and sc4 and sc5:

			print(f"{name}  Downtrend")
			ce_name, pe_name, strike = tsl.ATM_Strike_Selection(Underlying=name, Expiry=0)
			lot_size                 = tsl.get_lot_size(pe_name)


			try:
				orderbook[name]['qty']               = lot_size*6
				orderid                              = tsl.order_placement(tradingsymbol=pe_name, exchange='NFO', quantity=lot_size, price=0, trigger_price=0,order_type='MARKET', transaction_type='BUY', trade_type='MIS')
				orderbook[name]['entry_price']       = tsl.get_ltp_data(names=[pe_name])[pe_name] # tsl.get_executed_price(orderid=orderid)
			except Exception as e:
				print(f"Error placing entry order: {e}")
				continue

			try:
				trigger_price            = round(orderbook[name]['entry_price']*0.7, 1)
				price                    = max(trigger_price - 0.5, 0.1)
				sl_orderid               = tsl.order_placement(tradingsymbol=pe_name, exchange='NFO', quantity=lot_size, price=price, trigger_price=trigger_price,order_type='STOPLIMIT', transaction_type='SELL', trade_type='MIS')
			except Exception as e:
				print(f"Error placing SL order: {e}")
				cancel_entry_order             = tsl.cancel_order(OrderID=entry_orderid)
				orderbook[name]                = {'traded':"TRADE_NOT_POSSIBLE", 'options_name':None}
				continue



			orderbook[name]['options_name']      = pe_name
			orderbook[name]['date']              = str(current_dt.date())
			orderbook[name]['entry_time']        = str(current_dt.time())
			orderbook[name]['sl_price']          = trigger_price
			orderbook[name]['tg_price']          = round(orderbook[name]['entry_price']*1.3, 1)
			orderbook[name]['buy_sell']          = 'BUY_PE'
			orderbook[name]['traded']            = True
			orderbook[name]['entry_orderid']     = orderid
			orderbook[name]['sl_orderid']         = sl_orderid
			orderbook[name]['entry_datetime']    = current_dt
			orderbook[name]['breaked_even']      = False




		if orderbook[name]['traded']:

			buy_call = orderbook[name]['buy_sell'] == 'BUY_CE'
			buy_put  = orderbook[name]['buy_sell'] == 'BUY_PE'

			if buy_call or buy_put:

				options_name    = orderbook[name]['options_name']

				options_ltp      = tsl.get_ltp_data(names=[options_name])[options_name]
				time_exit        = datetime.datetime.now() >  orderbook[name]['entry_datetime'] + datetime.timedelta(minutes=30)
				sl_hit           = options_ltp <  orderbook[name]['sl_price']
				tg_hit           = options_ltp >  orderbook[name]['tg_price']


				if buy_call:
					trailing_exit   = comp_candle['STX_15_3'] == 'down'
				if buy_put:
					trailing_exit   = comp_candle['STX_15_3'] == 'up'


				orderbook[name]['pnl']         = round((options_ltp - orderbook[name]['entry_price']) * orderbook[name]['qty'], 2)



				# Trailing Start 
				if orderbook[name]['breaked_even'] == False:
					if orderbook[name]['pnl'] > 2000:
						trigger_price     = round(orderbook[name]['entry_price'],1)
						price             = max(trigger_price - 0.5, 0.1)
						orderbook[name]['sl_price']          = trigger_price
						modified_order_id                    = tsl.modify_order(order_id=orderbook[name]['sl_orderid'],order_type="STOPLIMIT",quantity=50,price=price,trigger_price=trigger_price)
						orderbook[name]['breaked_even']      = True
						orderbook[name]['next_trailing_pnl'] = 2000 + 500


				if orderbook[name]['breaked_even']:
					if orderbook[name]['pnl'] > orderbook[name]['next_trailing_pnl']:
						
						trigger_price     = round(orderbook[name]['entry_price'] + (500/orderbook[name]['qty']),1)
						price             = max(trigger_price - 0.5, 0.1)
						orderbook[name]['sl_price']          = trigger_price

						try:
							modified_order_id = tsl.modify_order(order_id=orderbook[name]['sl_orderid'],order_type="STOPLIMIT",quantity=50,price=price,trigger_price=trigger_price)
						except Exception as e:
							print(f"Error modifying order: {e}")
							cancel_sl_order   = tsl.cancel_order(OrderID=orderbook[name]['sl_orderid'])
							sl_orderid        = tsl.order_placement(tradingsymbol=orderbook[name]['options_name'], exchange='NFO', quantity=orderbook[name]['qty'], price=price, trigger_price=trigger_price,order_type='STOPLIMIT', transaction_type='SELL', trade_type='MIS')
							orderbook[name]['sl_orderid'] = sl_orderid
							orderbook[name]['next_trailing_pnl'] = orderbook[name]['next_trailing_pnl'] + 500

				# Trailing End



				if trailing_exit or sl_hit:
					orderbook[name]['remark']                          = "trailing_exit" if trailing_exit else "sl_hit"
					orderbook[name]['exit_orderid'] = orderbook[name]['sl_orderid']


				if time_exit or tg_hit:
					orderbook[name]['remark']                          = "time_exit" if time_exit else "tg_hit"
					cancel_sl_order                 = tsl.cancel_order(OrderID=orderbook[name]['sl_orderid'])
					orderbook[name]['exit_orderid'] = tsl.order_placement(tradingsymbol=orderbook[name]['options_name'], exchange='NFO', quantity=orderbook[name]['qty'], price=0, trigger_price=0,order_type='MARKET', transaction_type='SELL', trade_type='MIS')


				if trailing_exit or sl_hit or time_exit or tg_hit:

					orderbook[name]['exit_price']  = tsl.get_ltp_data(names=[options_name])[options_name] # tsl.get_executed_price(orderid=orderbook[name]['exit_orderid'])
					orderbook[name]['exit_time']   = str(current_dt.time())
					orderbook[name]['pnl']         = round((orderbook[name]['exit_price'] - orderbook[name]['entry_price']) * orderbook[name]['qty'], 2)

					if re_entry:
						complted_orderbook.append(orderbook[name])						
						orderbook[name] = status.copy()
```


==================================================


## [2/3] Repository: trading-bot (`WHEEL_trading-bot`)
- **Full Name**: `trading-bot`
- **Description**: Statistically-validated algorithmic trading system for NSE equities — FastAPI + React, real Indian cost modeling, honest strategy rejection
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Core Implementation Code & Architecture
#### File: `reports/latest_report.json`
```python
{
  "total_trades": 56,
  "total_pnl": "\u20b9-690.70",
  "total_return_pct": "-0.69%",
  "win_rate": "32.1%",
  "profit_factor": "0.75",
  "expectancy": "\u20b9-12.33",
  "avg_win_loss_ratio": "1.57",
  "sharpe_ratio": "-8.68",
  "max_drawdown": "1.56%",
  "calmar_ratio": "-1.70",
  "monte_carlo": {
    "prob_profit": "18.3%",
    "median_return": "-0.70%",
    "p5_return": "-1.94%",
    "p95_return": "0.59%"
  },
  "statistical_significance": {
    "p_value": "0.3743",
    "significant_5pct": "False"
  },
  "backtest_meta": {
    "symbol": "RELIANCE",
    "bars": 22500,
    "warmup": 35,
    "duration_seconds": "7.79",
    "strategy": "ema_rsi_crossover"
  }
}
```

#### File: `run_stress_test.py`
```python
"""Run all stress tests and produce comparison report."""
import json, pandas as pd, os
from backtester import Backtester
from config import load_config
from pathlib import Path

config = load_config()
stress_dir = 'data/stress'
results = {}

print('=' * 85)
print('  AERIN v2 (HARDENED) STRESS TEST RESULTS')
print('=' * 85)
header = f"{'Scenario':16s} | {'Trades':>6s} | {'PnL':>12s} | {'Return':>8s} | {'WR':>6s} | {'MDD':>8s} | {'Filtered':>8s}"
print(header)
print('-' * 85)

for csv_file in sorted(os.listdir(stress_dir)):
    if not csv_file.endswith('.csv'):
        continue
    name = csv_file.replace('_1min.csv', '')
    path = os.path.join(stress_dir, csv_file)
    df = pd.read_csv(path, parse_dates=['timestamp'])
    bt = Backtester(config, 100000)
    report = bt.run(df, symbol=name)
    results[name] = report
    trades = report.get('total_trades', 0)
    pnl = str(report.get('total_pnl', '0'))
    ret = str(report.get('total_return_pct', '0%'))
    wr = str(report.get('win_rate', 'N/A'))
    mdd = str(report.get('max_drawdown', 'N/A'))
    filt = str(report.get('backtest_meta', {}).get('filter_rate', 'N/A'))
    print(f"{name:16s} | {trades:>6} | {pnl:>12s} | {ret:>8s} | {wr:>6s} | {mdd:>8s} | {filt:>8s}")

print('=' * 85)
Path('reports').mkdir(exist_ok=True)
with open('reports/stress_test_v2_results.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)
print('Results saved to reports/stress_test_v2_results.json')
```

#### File: `run_3_datasets.py`
```python
import json
import logging
import pandas as pd
from pathlib import Path
from backtester import Backtester
from config import load_config
import sys
import io

# Force utf-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

datasets = [
    "data/stress/WORST_CASE_1min.csv",
    "data/stress/FLASH_CRASH_1min.csv",
    "data/stress/WHIPSAW_1min.csv"
]

def main():
    config = load_config()
    results = {}
    
    print("=" * 85)
    print("Testing Strategy on 3 Edge-Case Datasets")
    print("=" * 85)
    header = f"{'Scenario':16s} | {'Trades':>6s} | {'PnL':>12s} | {'Return':>8s} | {'WR':>6s} | {'MDD':>8s}"
    print(header)
    print("-" * 85)
    
    for path in datasets:
        name = Path(path).stem.replace('_1min', '')
        df = pd.read_csv(path, parse_dates=['timestamp'])
        
        # Suppress verbose logging from backtester to keep output clean
        logger = logging.getLogger()
        logger.setLevel(logging.WARNING)
        
        bt = Backtester(config, 100000)
        report = bt.run(df, symbol=name)
        results[name] = report
        
        trades = report.get('total_trades', 0)
        pnl = str(report.get('total_pnl', '0'))
        ret = str(report.get('total_return_pct', '0%'))
        wr = str(report.get('win_rate', 'N/A'))
        mdd = str(report.get('max_drawdown', 'N/A'))
        print(f"{name:16s} | {trades:>6} | {pnl:>12s} | {ret:>8s} | {wr:>6s} | {mdd:>8s}")

    Path('reports').mkdir(exist_ok=True)
    with open('reports/3_dataset_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, default=str)
    print("=" * 85)
    print("Results saved to reports/3_dataset_results.json")

if __name__ == "__main__":
    main()
```

#### File: `reports/3_dataset_results.json`
```python
{
  "WORST_CASE": {
    "total_trades": 33,
    "total_pnl": "\u20b9-2,196.78",
    "total_return_pct": "-2.20%",
    "win_rate": "15.2%",
    "profit_factor": "0.14",
    "expectancy": "\u20b9-66.57",
    "avg_win_loss_ratio": "0.79",
    "sharpe_ratio": "-9.24",
    "max_drawdown": "2.35%",
    "calmar_ratio": "-6.93",
    "monte_carlo": {
      "prob_profit": "0.0%",
      "median_return": "-2.15%",
      "p5_return": "-3.74%",
      "p95_return": "-0.89%"
    },
    "statistical_significance": {
      "p_value": "0.0187",
      "significant_5pct": "True"
    },
    "backtest_meta": {
      "symbol": "WORST_CASE",
      "bars": 37500,
      "warmup": 50,
      "duration_seconds": "32.92",
      "strategy": "ema_rsi_crossover",
      "signals_generated": 2561,
      "signals_filtered": 2528,
      "filter_rate": "98.7%"
    }
  },
  "FLASH_CRASH": {
    "total_trades": 17,
    "total_pnl": "\u20b9-1,818.37",
    "total_return_pct": "-1.82%",
    "win_rate": "11.8%",
    "profit_factor": "0.12",
    "expectancy": "\u20b9-106.96",
    "avg_win_loss_ratio": "0.88",
    "sharpe_ratio": "-15.32",
    "max_drawdown": "1.54%",
    "calmar_ratio": "-13.34",
    "monte_carlo": {
      "prob_profit": "0.0%",
      "median_return": "-1.82%",
      "p5_return": "-2.62%",
      "p95_return": "-0.97%"
    },
    "statistical_significance": {
      "p_value": "0.0026",
      "significant_5pct": "True"
    },
    "backtest_meta": {
      "symbol": "FLASH_CRASH",
      "bars": 22500,
      "warmup": 50,
      "duration_seconds": "15.61",
      "strategy": "ema_rsi_crossover",
      "signals_generated": 1264,
      "signals_filtered": 1245,
      "filter_rate": "98.5%"
    }
  },
  "WHIPSAW": {
    "total_trades": 23,
    "total_pnl": "\u20b9512.30",
    "total_return_pct": "0.51%",
    "win_rate": "47.8%",
    "profit_factor": "1.46",
    "expectancy": "\u20b922.27",
    "avg_win_loss_ratio": "1.59",
    "sharpe_ratio": "-8.23",
    "max_drawdown": "0.47%",
    "calmar_ratio": "8.07",
    "monte_carlo": {
      "prob_profit": "78.9%",
      "median_return": "0.51%",
      "p5_return": "-0.53%",
      "p95_return": "1.59%"
    },
    "statistical_significance": {
      "p_value": "0.4506",
      "significant_5pct": "False"
    },
    "backtest_meta": {
      "symbol": "WHIPSAW",
      "bars": 22500,
      "warmup": 50,
      "duration_seconds": "9.28",
      "strategy": "ema_rsi_crossover",
      "signals_generated": 248,
      "signals_filtered": 225,
      "filter_rate": "90.7%"
    }
  }
}
```

#### File: `monitor.py`
```python
"""
AERIN HFT Bot — Live Monitor
Terminal-based real-time dashboard for trading sessions.
"""

import os
import sys
import time
import logging
from datetime import datetime

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False

logger = logging.getLogger(__name__)


class LiveMonitor:
    """
    Terminal dashboard showing live P&L, positions, risk state,
    and kill-switch status.
    """

    def __init__(self, risk_manager, config):
        self.risk = risk_manager
        self.config = config
        self._start_time = datetime.now()

    def display(self):
        """Print the current dashboard to terminal."""
        state = self.risk.state
        positions = self.risk.get_all_positions()
        summary = self.risk.get_summary()

        # Header
        now = datetime.now().strftime("%H:%M:%S")
        mode = self.config.execution.mode.upper()
        mode_color = self._color(Fore.YELLOW) if mode == "PAPER" else self._color(Fore.RED)

        lines = []
        lines.append("")
        lines.append(f"{'═' * 60}")
        lines.append(f"  🚀 AERIN HFT Bot │ {mode_color}{mode}{self._reset()} │ {now}")
        lines.append(f"  Strategy: {self.config.strategy.name} │ "
                      f"Uptime: {self._uptime()}")
        lines.append(f"{'═' * 60}")

        # P&L Section
        pnl = state.daily_pnl
        pnl_color = self._color(Fore.GREEN) if pnl >= 0 else self._color(Fore.RED)
        pnl_pct = pnl / state.starting_capital * 100

        lines.append(f"")
        lines.append(f"  {'─── P&L ───':^58}")
        lines.append(f"  Daily P&L:     {pnl_color}₹{pnl:+,.2f}{self._reset()} "
                      f"({pnl_color}{pnl_pct:+.2f}%{self._reset()})")
        lines.append(f"  Capital:       ₹{state.current_capital:,.2f}")
        lines.append(f"  Drawdown:      {summary['drawdown']}")

        # Positions
        lines.append(f"")
        lines.append(f"  {'─── Positions ───':^58}")
        if positions:
            lines.append(f"  {'Symbol':<12} {'Side':<6} {'Qty':>5} "
                          f"{'Entry':>10} {'SL':>10} {'TP':>10} {'uPnL':>10}")
            lines.append(f"  {'─' * 55}")
            for pos in positions:
                upnl_color = self._color(Fore.GREEN) if pos.unrealized_pnl >= 0 \
                    else self._color(Fore.RED)
                lines.append(
                    f"  {pos.symbol:<12} {pos.side.value:<6} {pos.quantity:>5} "
                    f"₹{pos.entry_price:>9.2f} ₹{pos.stop_loss:>9.2f} "
                    f"₹{pos.take_profit:>9.2f} "
                    f"{upnl_color}₹{pos.unrealized_pnl:>9.2f}{self._reset()}"
                )
        else:
            lines.append(f"  No open positions")

        # Stats
        lines.append(f"")
        lines.append(f"  {'─── Stats ───':^58}")
        lines.append(f"  Trades today:  {state.total_trades_today}  "
                      f"(W: {state.winning_trades} / L: {state.losing_trades})")
        lines.append(f"  Win Rate:      {summary['win_rate']}")
        lines.append(f"  Consec. Losses: {state.consecutive_losses}")

        # Kill Switch Status
        lines.append(f"")
        if state.is_halted:
            lines.append(f"  {self._color(Fore.RED)}🛑 TRADING HALTED: "
                          f"{state.halt_reason}{self._reset()}")
        else:
            lines.append(f"  {self._color(Fore.GREEN)}✅ Trading active{self._reset()}")

        # Rate / API health
        lines.append(f"  API errors: {state.api_error_count}  │  "
                      f"Max orders/s: {self.config.execution.max_orders_per_second}")

        lines.append(f"{'═' * 60}")
        lines.append("")

        # Print all at once
        output = "\n".join(lines)
        print(output)

    def display_compact(self):
        """One-line status update for inline logging."""
        state = self.risk.state
        pnl = state.daily_pnl
        pnl_sym = "▲" if pnl >= 0 else "▼"
        now = datetime.now().strftime("%H:%M:%S")
        print(
            f"  [{now}] P&L: ₹{pnl:+,.2f} {pnl_sym} │ "
            f"Positions: {len(self.risk.positions)} │ "
            f"Trades: {state.total_trades_today} │ "
            f"{'🛑 HALTED' if state.is_halted else '✅ Active'}"
        )

    def _uptime(self) -> str:
        delta = datetime.now() - self._start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def _color(self, color):
        return color if HAS_COLOR else ""

    def _reset(self):
        return Style.RESET_ALL if HAS_COLOR else ""


def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")
```

#### File: `generate_sample_data.py`
```python
"""
Generate realistic synthetic 1-minute OHLCV data for backtesting.
Models intraday patterns: opening volatility, midday lull, closing ramp.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta


def generate_intraday(base_price: float, date: datetime,
                      volatility: float = 0.015, drift: float = 0.0,
                      volume_base: int = 50000) -> pd.DataFrame:
    """Generate one day of 1-min bars with realistic intraday patterns."""

    # Trading session: 9:15 to 15:30 = 375 minutes
    minutes = 375
    timestamps = [
        datetime(date.year, date.month, date.day, 9, 15) + timedelta(minutes=i)
        for i in range(minutes)
    ]

    # Intraday volatility curve (U-shape: high open/close, low midday)
    x = np.linspace(0, 1, minutes)
    vol_curve = 0.4 + 1.2 * (4 * (x - 0.5) ** 2)  # U-shape

    # Generate minute returns with vol modulation
    minute_vol = volatility / np.sqrt(minutes)
    returns = np.random.randn(minutes) * minute_vol * vol_curve
    returns += drift / minutes  # daily drift

    # Build price series from returns
    prices = base_price * np.exp(np.cumsum(returns))

    # Generate OHLC from close prices
    close = prices
    noise = np.abs(np.random.randn(minutes)) * minute_vol * base_price * 0.3
    high = close + noise
    low = close - noise
    open_ = np.roll(close, 1)
    open_[0] = base_price * (1 + np.random.randn() * minute_vol * 2)

    # Ensure OHLC consistency
    high = np.maximum(high, np.maximum(open_, close))
    low = np.minimum(low, np.minimum(open_, close))

    # Volume: higher at open/close (U-shape), with random spikes
    vol_shape = 0.3 + 1.5 * (4 * (x - 0.5) ** 2)
    volume = (volume_base * vol_shape * (0.5 + np.random.rand(minutes))).astype(int)

    # Random volume spikes (news-like events)
    spike_indices = np.random.choice(minutes, size=5, replace=False)
    volume[spike_indices] *= np.random.randint(3, 8, size=5)

    return pd.DataFrame({
        "timestamp": timestamps,
        "open": np.round(open_, 2),
        "high": np.round(high, 2),
        "low": np.round(low, 2),
        "close": np.round(close, 2),
        "volume": volume,
    })


def generate_multiday(symbol: str, base_price: float, days: int = 60,
                      daily_vol: float = 0.018, trend: float = 0.0003,
                      volume_base: int = 50000) -> pd.DataFrame:
    """Generate multi-day 1-min data with day-to-day continuity."""

    all_days = []
    price = base_price
    current_date = datetime(2025, 1, 1)

    for d in range(days):
        # Skip weekends
        while current_date.weekday() >= 5:
            current_date += timedelta(days=1)

        # Random daily drift (slight trend + noise)
        daily_drift = trend + np.random.randn() * 0.003

        day_data = generate_intraday(
            base_price=price,
            date=current_date,
            volatility=daily_vol * (0.7 + 0.6 * np.random.rand()),  # daily vol variation
            drift=daily_drift,
            volume_base=volume_base,
        )

        all_days.append(day_data)

        # Next day opens near previous close (with overnight gap)
        price = day_data["close"].iloc[-1] * (1 + np.random.randn() * 0.005)
        current_date += timedelta(days=1)

    df = pd.concat(all_days, ignore_index=True)
    print(f"  {symbol}: {len(df)} bars, {days} days, "
          f"price range ₹{df['close'].min():.2f} – ₹{df['close'].max():.2f}")
    return df


def main():
    np.random.seed(42)
    Path("data").mkdir(exist_ok=True)

    print("Generating synthetic 1-min OHLCV data...\n")

    # RELIANCE (~₹2800, moderate volatility)
    rel = generate_multiday("RELIANCE", base_price=2800, days=60,
                            daily_vol=0.016, trend=0.0002, volume_base=80000)
    rel.to_csv("data/RELIANCE_1min.csv", index=False)

    # TCS (~₹4000, lower volatility)
    tcs = generate_multiday("TCS", base_price=4000, days=60,
                            daily_vol=0.012, trend=0.0001, volume_base=30000)
    tcs.to_csv("data/TCS_1min.csv", index=False)

    # HDFCBANK (~₹1700, moderate)
    hdfc = generate_multiday("HDFCBANK", base_price=1700, days=60,
                             daily_vol=0.014, trend=0.0003, volume_base=60000)
    hdfc.to_csv("data/HDFCBANK_1min.csv", index=False)

    # NIFTY50 Index (~₹22000, low single-stock vol)
    nifty = generate_multiday("NIFTY50", base_price=22000, days=60,
                              daily_vol=0.010, trend=0.0002, volume_base=200000)
    nifty.to_csv("data/NIFTY50_1min.csv", index=False)

    # SBIN (~₹750, higher volatility)
    sbin = generate_multiday("SBIN", base_price=750, days=60,
                             daily_vol=0.020, trend=-0.0001, volume_base=100000)
    sbin.to_csv("data/SBIN_1min.csv", index=False)

    print(f"\n✅ Data saved to data/ directory")
    print(f"   Files: RELIANCE_1min.csv, TCS_1min.csv, HDFCBANK_1min.csv, "
          f"NIFTY50_1min.csv, SBIN_1min.csv")
    print(f"\nRun backtest:")
    print(f"  python main.py --mode backtest --data data/RELIANCE_1min.csv")


if __name__ == "__main__":
    main()
```


==================================================


## [3/3] Repository: turtlestack-lite (`WHEEL_turtlestack-lite`)
- **Full Name**: `turtlestack-lite`
- **Description**: TurtleStack Trading MCP Server is a comprehensive Model Context Protocol (MCP) server that provides unified access to multiple Indian stock brokers through Claude AI. It enables seamless trading operations, portfolio management, and advanced technical analysis across Kite (Zerodha), Groww, Dhan, and AngelOne brokers.
- **GitHub Stars**: 6
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# 🚀 TurtleStack Lite - Multi-Broker Trading MCP Server

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)
[![MCP Server](https://img.shields.io/badge/MCP-Server-purple.svg)](https://modelcontextprotocol.io/)
[![Trading API](https://img.shields.io/badge/Trading-API-orange.svg)](https://github.com/turtlehq-tech/turtlestack-lite)
[![Kite Connect](https://img.shields.io/badge/Kite-Connect-red.svg)](https://kite.trade/)
[![Groww API](https://img.shields.io/badge/Groww-API-blue.svg)](https://groww.in/)
[![Dhan API](https://img.shields.io/badge/Dhan-API-green.svg)](https://dhan.co/)
[![Cloudflare Workers](https://img.shields.io/badge/Cloudflare-Workers-orange.svg)](https://workers.cloudflare.com/)
[![Claude AI](https://img.shields.io/badge/Claude-AI-purple.svg)](https://claude.ai/)

> **🏆 Most Advanced Multi-Broker Trading MCP Server for Claude AI** - Unified API for Kite (Zerodha), Groww, and Dhan with 40+ Technical Indicators, Real-time Trading, Portfolio Management, and Cloudflare Workers Support.

## ✨ Features

🎯 **Multi-Broker Support**: Seamlessly trade across Kite (Zerodha), Groww, and Dhan  
📊 **Advanced Technical Analysis**: 40+ indicators including RSI, MACD, Bollinger Bands, VWAP, ATR  
🔄 **Real-time Trading**: Live order placement, modification, and cancellation  
💼 **Portfolio Management**: Unified portfolio tracking across all brokers  
☁️ **Cloudflare Workers**: Deploy globally with edge computing  
🤖 **Claude AI Integration**: Natural language trading commands  
🔒 **Enterprise Security**: No stored credentials, session-based authentication  
⚡ **High Performance**: Optimized for speed and reliability  
🏗️ **Modular Architecture**: Easy to extend and customize  

## 🚀 Quick Start

```bash
git clone https://github.com/turtlehq-tech/turtlestack-lite.git
cd turtlestack-lite
npm install
npm start
```

### Claude AI Configuration

Add this configuration to your Claude Desktop settings (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "turtlestack-lite": {
      "command": "node",
      "args": ["/path/to/turtlestack-lite/src/index.js"]
    }
  }
}
```

**Replace `/path/to/turtlestack-lite/` with your actual installation path:**

```bash
# Example paths:
# macOS: "/Users/yourusername/Projects/turtlestack-lite/src/index.js"
# Linux: "/home/yourusername/turtlestack-lite/src/index.js"  
# Windows: "C:\\Users\\yourusername\\turtlestack-lite\\src\\index.js"
```

**🔒 Security Note**: No API keys or secrets are stored in the configuration. All credentials must be provided through Claude commands for maximum security.

## 🔧 Configuration Setup

**Important**: This repository contains dummy placeholder values for all sensitive IDs and tokens. Before using the project, you must replace these placeholders with your actual credentials.

### 📝 Required Replacements

The following files contain placeholder values that need to be replaced with your actual credentials:

#### 1. **Test Files** (for development/testing):
- `tests/debugAuthentication.js:16,17` - Replace `YOUR_CLIENT_ID_HERE` and `YOUR_PROGRESS_TOKEN_HERE` 
- `tests/testClaudeConnection.js:21,22` - Replace `YOUR_CLAUDE_SESSION_TOKEN_HERE` and `YOUR_CLAUDE_CLIENT_ID_HERE`
- `tests/testGrowwOrderFix.js:13` - Replace `YOUR_GROWW_API_KEY_HERE`
- `tests/testGrowwOrderReference.js:11` - Replace `YOUR_GROWW_API_KEY_HERE`
- `tests/debugAuthentication.js:44` - Replace `YOUR_GROWW_JWT_TOKEN_HERE`
- `tests/testClaudeConnection.js:40,52` - Replace `YOUR_GROWW_JWT_TOKEN_HERE`

#### 2. **Cloudflare Configuration** (for Cloudflare Workers deployment):
- `bridge.js:4` - Replace `YOUR_WORKER_SUBDOMAIN.YOUR_USERNAME.workers.dev`
- `cloudflare/wrangler.toml:17` - Replace `YOUR_KV_NAMESPACE_ID_HERE`
- `cloudflare/mcp-config-for-claude.json:5` - Replace worker URL in the embedded command

### 🔑 How to Get Your Credentials

#### **For Kite (Zerodha):**
1. Go to [Kite Connect Developer Console](https://developers.kite.trade/)
2. Create an app to get `api_key` and `api_secret`
3. Generate access token using the authentication flow

#### **For Groww:**
1. Use browser developer tools to inspect network requests on Groww web app
2. Extract JWT token from Authorization header
3. Token format: `eyJraWQiOiJ...` (long JWT string)

#### **For Dhan:**
1. Go to [Dhan API Portal](https://dhanhq.co/docs/)
2. Get your `access_token` and `client_id`

#### **For Cloudflare Workers:**
1. Create KV namespace: `wrangler kv:namespace create "SESSIONS_KV"`
2. Note the namespace ID from the output
3. Update your worker subdomain based on your Cloudflare account

### ⚠️ Security Best Practices

- **Never commit real credentials** to version control
- **Use environment variables** for production deployments  
- **Rotate tokens regularly** for security
- **Test with dummy data** first before using real credentials

### 🧪 Quick Setup for Testing

Replace these specific placeholders to get started quickly:

```bash
# 1. Update test files with your tokens
sed -i 's/YOUR_GROWW_JWT_TOKEN_HERE/your_actual_groww_token/g' tests/testClaudeConnection.js
sed -i 's/YOUR_GROWW_API_KEY_HERE/your_actual_api_key/g' tests/testGroww*.js

# 2. Update Cloudflare config (if using workers)
sed -i 's/YOUR_WORKER_SUBDOMAIN.YOUR_USERNAME.workers.dev/your-worker.your-account.workers.dev/g' bridge.js
sed -i 's/YOUR_KV_NAMESPACE_ID_HERE/your_actual_kv_id/g' cloudflare/wrangler.toml
```

## Installation

```bash
npm install
```

## Testing

```bash
# Run all tests
npm test

# Run unit tests only
npm run test:unit

# Run integration tests only  
npm run test:integration

# Run tests with watch mode
npm run test:watch

# Demo technical indicators
node tests/demo.js
```


## Project Structure

```
src/
├── brokers/
│   ├── BaseBroker.js      # Base interface for all brokers
│   ├── KiteBroker.js      # Kite (Zerodha) implementation
│   ├── GrowwBroker.js     # Groww implementation
│   ├── DhanBroker.js      # Dhan implementation
│   └── index.js           # Broker exports and factory
├── server/
│   └── UnifiedTradingServer.js  # Main MCP server (v2.0.0)
├── utils/
│   ├── logger.js          # Logging utility
│   ├── formatters.js      # Data formatting utilities
│   ├── technicalIndicators.js    # Backward compatibility wrapper
│   └── technicalIndicators/      # Modular technical analysis
│       ├── index.js              # Main aggregation file
│       ├── trendIndicators.js    # SMA, EMA, VWAP, ADX, Parabolic SAR
│       ├── momentumIndicators.js # RSI, MACD, Stochastic, Williams %R, CCI, MFI
│       ├── volatilityIndicators.js # Bollinger Bands, ATR
│       ├── volumeIndicators.js   # OBV
│       └── supportResistanceIndicators.js # Fibonacci, Support/Resistance
└── index.js               # Entry point
tests/
├── unit/
│   └── technicalIndicators.test.js  # Technical indicators unit tests
├── integration/
│   ├── brokers.test.js             # Broker integration tests
│   └── unifiedTradingServer.test.js # Server integration tests
├── fixtures/
│   └── mockData.js                 # Test data fixtures
└── demo.js                         # Technical indicators demo
```

## Usage

### Start Unified Trading Server
```bash
npm start
# or for development
npm run dev
```

## Features

### Multi-Broker Support
- **✅ Kite (Zerodha)** - Fully implemented with advanced features
- **✅ Groww** - Fully implemented with advanced features
- **✅ Dhan** - Fully implemented with advanced features

### Architecture Benefits
- **🏗️ Modular Design**: Each broker in separate file
- **🔌 Pluggable**: Easy to add new brokers
- **🧪 Testable**: Individual components can be tested
- **📝 Maintainable**: Clean separation of concerns
- **🔄 Scalable**: Supports unlimited brokers

### Key Commands

#### Broker Management
```
# List all available brokers
List brokers

# Set active broker
Set active broker to kite
```

#### Authentication (Secure - No Stored Credentials)
```
# Authenticate Kite with access token
Authenticate kite with api_key: your_api_key and access_token: your_access_token

# Authenticate Kite with request token
Authenticate kite with api_key: your_api_key, api_secret: your_api_secret, and request_token: your_request_token

# Authenticate Groww
Authenticate groww with access_token: your_groww_access_token

# Authenticate Dhan
Authenticate dhan with access_token: your_dhan_access_token and client_id: your_dhan_client_id
```

#### Trading Operations
```
# Get portfolio from active broker
Show my portfolio

# Get portfolio from specific broker
Show my groww portfolio

# Compare portfolios across brokers
Compare my portfolios across all brokers

# Place order using active broker
Create buy order for RELIANCE 10 shares at market price

# Get margins
Show my account margins
```

#### Advanced Features
```
# Get consolidated portfolio across all brokers
Show me my consolidated portfolio across all brokers

# Kite Advanced Features
Get my Kite mutual fund holdings
Place GTT order for RELIANCE
Get historical data for INFY

# Groww Advanced Features  
Get technical indicators RSI for RELIANCE
Search for instruments containing "TATA"
Get historical candle data for HDFC

# Dhan Advanced Features
Get option chain for NIFTY
Place bracket order with stop loss and target
Get live market feed for instruments

# Logout from specific broker
Logout from kite

# Logout from all brokers
Logout from all brokers

# Technical Analysis Operations
Get RSI for RELIANCE
Get MACD for INFY  
Get Bollinger Bands for HDFC
Get VWAP for TATA STEEL
Get ATR for NIFTY

# Cross-broker technical comparison
Compare RSI for RELIANCE across all brokers
Compare MACD for INFY across kite and groww
```

## Advanced Broker Features

### **🚀 Kite (Zerodha) Advanced Features:**
- **✅ Technical Analysis**: RSI, MACD, Bollinger Bands, SMA, EMA, Stochastic
- **Mutual Funds**: Holdings, orders, SIP management
- **GTT (Good Till Triggered)**: Advanced conditional orders
- **Historical Data**: OHLC data with custom intervals
- **Instruments**: Complete instrument master data
- **Order Management**: Modify, cancel, bracket orders
- **Profile & Margins**: Account details and fund limits

### **📊 Groww Advanced Features:**
- **✅ Technical Analysis**: RSI, MACD, Bollinger Bands (Native API support)
- **Historical Data**: Candlestick data for any time period
- **Advanced Search**: Complex instrument filtering
- **Order Management**: Create, modify, cancel orders
- **Market Data**: Real-time quotes and live feeds
- **Instrument Details**: Complete security information

### **⚡ Dhan Advanced Features:**
- **✅ Technical Analysis**: RSI, MACD, Bollinger Bands, SMA, EMA, Stochastic
- **Option Chain**: Complete options data with Greeks
- **Bracket/Cover Orders**: Advanced order types with SL/Target
- **Kill Switch**: Emergency stop for all trading activities
- **Live Market Feed**: Real-time price updates
- **Security Info**: Detailed instrument information
- **Order Book/Trade Book**: Complete trading history
- **Exchange Status**: Real-time market status updates

## Technical Indicator Support

### **📊 Unified Technical Analysis Commands:**

#### **Individual Indicators:**
```
# Get specific technical indicators
Get RSI for RELIANCE with period 14
Get MACD for INFY from kite broker
Get Bollinger Bands for HDFC with period 20
Get VWAP for TATA STEEL from groww
Get ATR for NIFTY with period 14
Get ADX for RELIANCE with period 14

# Multiple indicators at once
Get technical indicators RSI,MACD,BOLLINGER for RELIANCE
```

#### **Cross-Broker Comparison:**
```
# Compare same indicator across brokers
Compare RSI for RELIANCE across all brokers
Compare MACD for INFY across kite,groww,dhan
Compare Bollinger Bands for HDFC across authenticated brokers
```

#### **Advanced Parameters:**
```
# With custom periods and timeframes
Get RSI for RELIANCE with period 21 and interval 1h
Get MACD for INFY with fast_period 10, slow_period 20, signal_period 7
Get Bollinger Bands for HDFC with period 20 and standard_deviations 2.5
```

### **✅ All Brokers Support:**

#### **📊 Trend Indicators:**
- **SMA (Simple Moving Average)**: Any period
- **EMA (Exponential Moving Average)**: Any period  
- **VWAP (Volume Weighted Average Price)**: Intraday trading benchmark
- **Parabolic SAR**: Stop and Reverse trend following system
- **ADX (Average Directional Index)**: Trend strength indicator

#### **📈 Momentum Indicators:**
- **RSI (Relative Strength Index)**: 14-period default, overbought/oversold
- **MACD (Moving Average Convergence Divergence)**: 12,26,9 default parameters
- **Stochastic Oscillator**: %K and %D lines
- **Williams %R**: Momentum oscillator
- **CCI (Commodity Channel Index)**: Price deviation indicator
- **MFI (Money Flow Index)**: Volume-weighted RSI

#### **📊 Volatility Indicators:**
- **Bollinger Bands**: 20-period with 2 standard deviations default
- **ATR (Average True Range)**: Volatility measurement

#### **💰 Volume Indicators:**
- **OBV (On-Balance Volume)**: Volume flow indicator
- **MFI (Money Flow Index)**: Price and volume momentum

#### **🎯 Support & Resistance:**
- **Fibonacci Retracement**: Key retracement levels (23.6%, 38.2%, 50%, 61.8%)
- **Support/Resistance Levels**: Automated level detection

### **🔧 Implementation Details:**
- **Groww**: Native API support for technical indicators via `/technical/{indicator}` endpoints
- **Kite & Dhan**: Historical data + local calculation using comprehensive TechnicalIndicators utility class
- **Consistent API**: Unified command interface across all brokers regardless of implementation
- **Cross-Broker Comparison**: Compare same indicator across multiple brokers simultaneously
- **Real-time Calculation**: Indicators calculated from live historical data with customizable parameters
- **Intelligent Routing**: UnifiedTradingServer automatically routes requests to appropriate broker methods

### **📈 Available Technical Analysis Tools:**

#### **MCP Commands:**
- `get_technical_indicators` - Multiple indicators at once
- `get_rsi` - Relative Strength Index
- `get_macd` - Moving Average Convergence Divergence  
- `get_bollinger_bands` - Bollinger Bands
- `get_vwap` - Volume Weighted Average Price
- `get_atr` - Average True Range
- `get_adx` - Average Directional Index
- `compare_technical_indicators` - Cross-broker comparison

#### **Unified Command Examples:**
```bash
# Individual technical indicators
Get RSI for RELIANCE with period 14
Get MACD for INFY from kite
Get Bollinger Bands for HDFC with period 20 and standard_deviations 2
Get VWAP for TATASTEEL from groww  
Get ATR for NIFTY with period 14 from dhan
Get ADX for RELIANCE with period 14

# Multiple indicators
Get technical indicators RSI,MACD,BOLLINGER,VWAP for RELIANCE

# Cross-broker comparison
Compare RSI for RELIANCE across all brokers
Compare MACD for INFY across kite,groww
Compare VWAP for HDFC across authenticated brokers
```

#### Security Features
- ✅ **No stored credentials**: All API keys/tokens provided via commands
- ✅ **Session-based**: Credentials cleared when server restarts  
- ✅ **Broker isolation**: Each broker maintains separate credentials
- ✅ **Runtime authentication**: Authenticate only when needed
- ✅ **Modular security**: Each broker handles its own authentication

## Adding New Brokers

To add a new broker (e.g., Upstox):

1. **Create broker file**: `src/brokers/UpstoxBroker.js`
2. **Extend BaseBroker**: Implement all required methods
3. **Add to index**: Export in `src/brokers/index.js`
4. **Update server**: Add to broker registry in `UnifiedTradingServer.js`
5. **Test**: Authenticate and test all operations

The modular architecture makes adding new brokers straightforward and maintainable.

## 📁 Cloudflare Workers Deployment

For deploying to Cloudflare Workers, see the complete setup guide in `/cloudflare/README.md`.

## 📄 License

Apache 2.0 License - see LICENSE file for details.

### Core Implementation Code & Architecture
#### File: `mcp-config-for-claude.json`
```python
{
  "mcpServers": {
    "turtlestack-trading": {
      "command": "node",
      "args": ["/Users/shubham/Desktop/my-kite-mcp-server/src/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

#### File: `claude-desktop-config.json`
```python
{
  "mcpServers": {
    "turtlestack-trading-local": {
      "command": "node",
      "args": ["/Users/shubham/Desktop/my-kite-mcp-server/src/index.js"]
    },
    "turtlestack-trading-cloud": {
      "command": "node",
      "args": ["/Users/shubham/Desktop/my-kite-mcp-server/bridge.js"]
    }
  }
}
```

#### File: `cloudflare/wrangler-simple.toml`
```python
name = "turtle-stack-free"
main = "worker.js"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

# Free tier optimized settings
[limits]
cpu_ms = 10000

[vars]
NODE_ENV = "production"
DEBUG_MODE = "false"
SESSION_TIMEOUT_MS = "3600000"
MAX_CONCURRENT_SESSIONS = "50"

# Environment-specific configurations
[env.production]
name = "turtle-stack-free"

[env.production.vars]
NODE_ENV = "production"
DEBUG_MODE = "false"

[env.staging]
name = "turtle-stack-free-staging"

[env.staging.vars]
NODE_ENV = "staging"
DEBUG_MODE = "true"
```

#### File: `cloudflare/wrangler.toml`
```python
name = "turtle-stack-free"
main = "worker.js"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

# Free tier optimized settings (CPU limits not supported on free plan)

[vars]
NODE_ENV = "production"
DEBUG_MODE = "false"
SESSION_TIMEOUT_MS = "3600000"
MAX_CONCURRENT_SESSIONS = "50"

# KV namespace for session storage
[[kv_namespaces]]
binding = "SESSIONS_KV"
id = "YOUR_KV_NAMESPACE_ID_HERE"

# Environment-specific configurations
[env.production]
name = "turtle-stack-free"

[env.production.vars]
NODE_ENV = "production"
DEBUG_MODE = "false"

[env.staging]
name = "turtle-stack-free-staging"

[env.staging.vars]
NODE_ENV = "staging"
DEBUG_MODE = "true"
```

#### File: `cloudflare/package.json`
```python
{
  "name": "turtlestack-mcp-cloudflare-worker",
  "version": "2.0.0",
  "description": "TurtleStack MCP Server for Cloudflare Workers - Multi-broker trading platform",
  "main": "worker.js",
  "scripts": {
    "dev": "wrangler dev",
    "deploy": "wrangler deploy",
    "deploy:production": "wrangler deploy --env production",
    "deploy:staging": "wrangler deploy --env staging",
    "tail": "wrangler tail",
    "kv:create": "wrangler kv:namespace create SESSIONS_KV",
    "kv:create:preview": "wrangler kv:namespace create SESSIONS_KV --preview",
    "logs": "wrangler tail --format=pretty"
  },
  "keywords": [
    "trading",
    "mcp",
    "kite",
    "groww",
    "dhan",
    "cloudflare",
    "workers"
  ],
  "author": "TurtleStack Team",
  "license": "MIT",
  "devDependencies": {
    "wrangler": "^3.0.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

#### File: `cloudflare/claude-mcp-config.json`
```python
{
  "mcpServers": {
    "turtlestack-trading": {
      "command": "node",
      "args": [
        "-e",
        "const { Server } = require('@modelcontextprotocol/sdk/server/index.js'); const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio.js'); const server = new Server({ name: 'turtlestack-trading', version: '2.0.0' }, { capabilities: { tools: {} } }); const baseURL = 'https://your-worker.your-subdomain.workers.dev'; let sessionId = null; server.setRequestHandler('tools/list', async () => { const response = await fetch(`${baseURL}/mcp/tools`); const data = await response.json(); return data; }); server.setRequestHandler('tools/call', async (request) => { if (!sessionId) { const sessionResponse = await fetch(`${baseURL}/session/create`, { method: 'POST' }); const sessionData = await sessionResponse.json(); sessionId = sessionData.sessionId; } const response = await fetch(`${baseURL}/mcp/call`, { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-Session-ID': sessionId }, body: JSON.stringify({ tool: request.params.name, arguments: request.params.arguments }) }); const data = await response.json(); return { content: [{ type: 'text', text: JSON.stringify(data, null, 2) }] }; }); const transport = new StdioServerTransport(); server.connect(transport);"
      ],
      "env": {
        "WORKER_URL": "https://your-worker.your-subdomain.workers.dev"
      }
    }
  }
}
```


==================================================
