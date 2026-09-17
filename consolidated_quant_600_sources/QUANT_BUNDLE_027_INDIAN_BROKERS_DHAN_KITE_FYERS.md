# ⚡ [QUANT-SOURCE-027] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_027_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: nifty-algo-trader (`WHEEL_nifty-algo-trader`)
- **Full Name**: `nifty-algo-trader`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# NSE/BSE Algorithmic Trading System (Python)

A production-style, phased-gate algorithmic trading system engineered for the Indian stock market (NSE). Built in strict modular phases with mathematical rigor, zero broker leakage, and institutional risk management.

---

## 🏛️ System Architecture

```
trading-system/
├── src/
│   ├── config.py                      # Global path constants & Nifty 50 universe
│   ├── data_pipeline/
│   │   ├── fetch.py                   # YFinance downloader (rate limiting, exponential backoff)
│   │   └── clean.py                   # Data validator, deduplicator, monotonic date sorter
│   ├── strategy/
│   │   ├── config.py                  # StrategyConfig dataclass (zero hardcoded magic numbers)
│   │   ├── indicators.py              # Vectorized EMA and Wilder's Smoothing RSI(14)
│   │   ├── signals.py                 # Pure-logic BUY/SELL/HOLD & dynamic SL/TP generator
│   │   └── runner.py                  # Batch dataset processor
│   ├── risk/
│   │   └── position_sizing.py         # 1% Capital Risk Rule & Max Position % Cap
│   ├── backtest/
│   │   ├── costs.py                   # Indian discount broker friction (₹20/0.03% + 0.05% slippage)
│   │   ├── metrics.py                 # CAGR, Sharpe, Win Rate, Max Drawdown, Profit Factor
│   │   ├── engine.py                  # Bar-by-bar simulator with train/test isolation
│   │   └── report.py                  # Matplotlib equity curves & underwater drawdowns
│   ├── portfolio/
│   │   └── paper_broker.py            # Persistent virtual broker (JSON state serialization)
│   ├── broker/
│   │   └── kite_client.py             # Guarded Zerodha Kite Connect live wrapper with hard caps
│   ├── app.py                         # Streamlit multi-tab trading dashboard
│   └── autonomous/
│       ├── preconditions.py           # Startup safety verification (Backtest, Paper, .env)
│       ├── market_calendar.py         # NSE trading hours (09:15–15:30 IST) & holiday calendar
│       ├── kill_switch.py             # File-backed emergency stop CLI & daemon
│       ├── risk_monitor.py            # Real-time daily loss tracker & position cap guardian
│       ├── alerts.py                  # Real-time Telegram alerts & console fallback
│       └── runner.py                  # Main autonomous scheduler & decision loop
└── tests/                             # 48 Unit & Integration tests covering all components
```

---

## 🚀 Phased Development Gates

1. **Step 1: Data Pipeline** — Clean historical OHLC daily data (2022–2025).
2. **Step 2: Strategy Engine** — EMA(20)/EMA(50) crossover with Wilder's RSI(14) filter and dynamic 2% SL / 4% TP.
3. **Step 3: Backtesting & Validation** — In-Sample (Train) vs Out-of-Sample (Test) evaluation with realistic Indian brokerage (₹20/0.03%) and slippage (0.05%).
4. **Step 4: Paper Trading Dashboard** — Streamlit app showing live signals alongside empirical backtest context, persistent balance/positions across restarts, and live equity curves.
5. **Step 5: Guarded Live Broker** — Official Zerodha Kite Connect integration with code-level hard caps (`MAX_ORDER_VALUE`, `MAX_DAILY_LOSS`), manual confirmation gates, and audit logs.
6. **Step 6: Autonomous Execution** — Continuous unattended market runner (09:15–15:30 IST), independent Kill Switch CLI, real-time Telegram alerts, and crash containment.

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anupmazumdar/nifty-algo-trader.git
   cd nifty-algo-trader
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```

---

## ⚡ Quickstart Guide

### 1. Fetch & Clean Market Data
```bash
python -m src.data_pipeline.fetch
python -m src.data_pipeline.clean
```

### 2. Run Strategy Backtester
```bash
python -m src.backtest.engine
python -m src.backtest.report
```

### 3. Launch Paper Trading Dashboard
```bash
streamlit run src/app.py
```

### 4. Emergency Kill Switch Controls
```bash
# Check status
python -m src.autonomous.kill_switch --status

# Engage emergency stop (blocks all new orders)
python -m src.autonomous.kill_switch --activate --reason "High Volatility"

# Disengage kill switch
python -m src.autonomous.kill_switch --deactivate
```

### 5. Autonomous Runner (Dry-Run & Live)
```bash
# Dry-run test cycle
python -m src.autonomous.runner --dry-run --ignore-market-hours --bypass-paper-gate --single-iteration

# Live autonomous market hours execution
python -m src.autonomous.runner
```

---

## 🧪 Testing

Run the comprehensive 48-test verification suite:
```bash
pytest tests/ -v
```

---

## 🛡️ Production Process Management
For 24/7 continuous operation on Windows, configure **NSSM (Non-Sucking Service Manager)**:
```powershell
nssm install NSETwoEmaRunner python.exe "-m src.autonomous.runner"
nssm start NSETwoEmaRunner
```
On Linux, configure `systemd` or `supervisor` to auto-restart the service if interrupted.

---

## 📄 License
MIT License.

### Core Implementation Code & Architecture
#### File: `src/__init__.py`
```python
"""
NSE/BSE Algorithmic Trading System Package.
"""
```

#### File: `tests/__init__.py`
```python
"""
Test Suite Package for Algorithmic Trading System.
"""
```

#### File: `src/broker/__init__.py`
```python
"""
Broker Integration Package.
"""

from src.broker.kite_client import KiteClient

__all__ = ["KiteClient"]
```

#### File: `src/portfolio/__init__.py`
```python
"""
Portfolio & Virtual Broker Package.
"""

from src.portfolio.paper_broker import PaperBroker

__all__ = ["PaperBroker"]
```

#### File: `src/risk/__init__.py`
```python
"""
Risk Management Package.
"""

from src.risk.position_sizing import calculate_position_size

__all__ = ["calculate_position_size"]
```

#### File: `src/data_pipeline/__init__.py`
```python
"""
Data Pipeline Package.
"""

from src.data_pipeline.fetch import fetch_symbol_data, fetch_all_symbols, fetch_latest_quote, refresh_symbol_data
from src.data_pipeline.clean import clean_ohlcv_dataframe, clean_file, clean_all_raw_files

__all__ = [
    "fetch_symbol_data",
    "fetch_all_symbols",
    "fetch_latest_quote",
    "refresh_symbol_data",
    "clean_ohlcv_dataframe",
    "clean_file",
    "clean_all_raw_files",
]
```


==================================================


## [2/3] Repository: nse-algo-bot (`WHEEL_nse-algo-bot`)
- **Full Name**: `nse-algo-bot`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# NSE Algo Bot

**A complete intraday trading bot for NSE equities — everything except the trading rule.**

One command before the bell and it runs the whole day on its own: refresh the candle database, log in, warm up indicator state for the whole watchlist, connect the market feed, evaluate each tick, size the trade against real broker leverage, place the order, then manage the stop, the trail and the exit until the position is squared off.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/python-3.11%2B-blue">
  <img alt="Flask" src="https://img.shields.io/badge/flask-2.3%2B-black">
  <img alt="Broker" src="https://img.shields.io/badge/broker-DhanHQ%20v2-orange">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
</p>

> [!IMPORTANT]
> **This repository ships no strategy — on purpose.** [`indicators.py`](indicators.py) and [`strategy.py`](strategy.py) are empty scaffolds: documented function signatures, every one of them `NotImplementedError`. No indicators, no thresholds, no entry rule. Everything *around* them is complete and is the point of this repository. Write those two files and the bot runs.

---

## Where your code goes

Two files, and nothing else needs touching.

**[`indicators.py`](indicators.py) — compute the numbers.** Six batch functions that run over a full DataFrame of completed candles, plus two that keep a small state dict moving forward one candle at a time. That split exists because a tick cannot afford to recompute history: the batch path runs once before the open, `extract_state()` folds it into a few values, and from then on each new candle only calls `increment_state()`.

> The contract that matters: walking a series with `increment_state()` must produce the same values as the batch functions over that same series. If they drift, the bot trades one thing and your backtest reports another.

**[`strategy.py`](strategy.py) — make the decision.** Two functions:

| Function | Called | Returns |
| :--- | :--- | :--- |
| `precompute_state(security_id, symbol)` | once per stock, before the open, in parallel | a cache dict — history loaded, indicators run |
| `check_signal_on_tick(cached, ltp, today_ohlc, ...)` | every tick, for every stock | `("LONG" \| "SHORT" \| None, state)` |

Whatever you put in `state` is printed when a signal fires and pushed to the dashboard, so put your condition flags there — that is what makes a fill explainable three weeks later. Both files carry a complete worked example in their header comments.

---

## What you get around it

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  BEFORE THE BELL                                                 │
  │    watchlist   symbols → security IDs from the instrument master │
  │    db          1H candles → aggregated to 4H, incrementally      │
  │    auto_login  fresh token over TOTP, verified against the API   │
  │    warm-up     indicator state per stock, in parallel, cached    │
  ├──────────────────────────────────────────────────────────────────┤
  │  DURING THE SESSION                                              │
  │    scanner_ws  market feed → running O/H/L → your rule, per tick │
  │    broker      live balance, real leverage, quantity, order      │
  │    monitor     stop · trail · profit lock · target · force exit  │
  │    frontend    live dashboard over SSE                           │
  │    telegram    alerts on every signal and fill                   │
  └──────────────────────────────────────────────────────────────────┘
```

Startup prints every one of those settings before it touches the market, so what the bot is about to do is on screen and arguable rather than buried in a config file:

![The startup banner — capital, leverage, indicator slots, stop, trail, target and the session windows](docs/startup.png)

The client ID is masked to its last four digits, because that line is the one that ends up in screenshots.

**Sizing is checked against the broker, not assumed.** Quantity comes from live balance, a reserve buffer, and the exchange's *actual* intraday leverage for that instrument. If a stock has been flagged (ASM/GSM/T2T) and leverage drops below what the sizing assumed, the trade is skipped rather than silently resized into something you did not intend.

**Stops are placed off the fill, not the signal.** The entry price is read back from the order after it fills. Assuming the signal price is how a stop ends up somewhere you never chose.

**Position size is read from the broker.** Monitoring tracks the net position the broker reports, not what the program believes it sent — those two can disagree, and only one of them is real.

**Exits are layered.** Initial stop, a trail that moves to breakeven once the trade is working, profit locked in tiers, a hard target, and a force square-off before the close so nothing drifts into delivery by accident.

**Copy trading is built in.** Every entry and exit can be mirrored onto follower accounts, each logging in independently and sized off its *own* capital rather than as a multiple of the master's quantity.

![The dashboard, showing fills from real sessions replayed into it](docs/dashboard.png)

Those rows are real. They are the fills a private rule produced while running on this infrastructure — 52 of them across 25 sessions — replayed into the dashboard here so the page has something to show. **The rule that generated them is not in this repository**; what is here is everything underneath it: the feed, the sizing, the orders, the exit management, and this page. Write `strategy.py` and your own rows appear the same way, live.

---

## Setup

Requires a [Dhan](https://dhanhq.co) account with API access — the bot reads live data and places live orders.

```bash
git clone https://github.com/tejgohel/nse-algo-bot.git
cd nse-algo-bot

python -m venv .venv
# Windows:  .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env        # Windows: copy .env.example .env
```

Fill in `.env`:

```ini
PAPER_TRADING=1             # leave this ON
SCANNER_MODE=1

DHAN_CLIENT_ID=your_client_id
DHAN_ACCESS_TOKEN=your_access_token

# Optional — TOTP auto-login, mints a fresh token every run
DHAN_PIN=your_login_pin
DHAN_TOTP_SECRET=your_base32_2fa_seed
```

Then seed the candle database and start:

```bash
python tools/seed_db.py         # 1H → 4H history for the watchlist
python tools/seed_daily_db.py   # daily bars
python tools/seed_state.py      # fold history into indicator state
python main.py
```

The dashboard opens automatically. Until you write `indicators.py` and `strategy.py`, startup will stop with a clear `NotImplementedError` telling you which function is missing — that is expected.

### About login

Access tokens last about a day, and **the broker invalidates the previous token the moment a new one is issued** — so two programs logging in on the same account keep killing each other's feed. Token generation is also throttled to roughly one per two minutes, and a refusal arrives as a dropped TLS connection that reads exactly like a network fault. [`auto_login.py`](auto_login.py) recognises that, backs off past the window, and verifies any fallback token against a live endpoint before trusting it.

---

## The safety switch

```python
PAPER_TRADING = True     # signals found, sized and logged — no order is sent
PAPER_TRADING = False    # LIVE. Real orders. No confirmation prompt.
```

There is no dry-run flag hiding behind that one. With `PAPER_TRADING=0` and `SCANNER_MODE=0`, a signal becomes an order in the same tick it fires.

Stay on paper until live signals match what your own backtest said they would be. Then start with capital you can afford to lose entirely, because you will find out what your rule actually does only after it has been running for a while.

---

## Configuration

Everything is in [`config.py`](config.py), documented inline.

| Setting | Default | Meaning |
| :--- | :--- | :--- |
| `PAPER_TRADING` | `True` | the switch above |
| `SCANNER_MODE` | `True` | scan and alert only, never trade |
| `DEPLOYED_CAPITAL` | `50,000` | ₹ you intend to deploy per trade |
| `LEVERAGE` / `MIN_LEVERAGE_REQUIRED` | `5` / `5.0` | expected leverage, and the floor below which a trade is skipped |
| `INITIAL_SL_PCT` | `5` | max rupee risk on entry, as % of capital |
| `TRAIL_STEP_PCT` | `0.5` | move from entry that pulls the stop to breakeven |
| `PROFIT_LOCK_PCT` / `_TRIGGER_PCT` | `10` / `11` | how much profit is protected, and where it arms |
| `TP_PCT` | `20` | hard exit |
| `MAX_MOVE_PCT` | `5.0` | skip an entry if the stock has already run this far today |
| `MAX_ENTRY_TIME` / `MARKET_EXIT_TIME` | `14:30` / `15:15` | last entry, and force square-off |
| `INDICATOR_1/2/3_LENGTH` / `_MULT` | placeholders | passed straight into your `calculate_indicator_*` functions |
| `WATCHLIST_SYMBOLS` | 25 large caps | any NSE symbols; resolved to security IDs automatically |

Risk is expressed as a percentage of **capital**, not of price. A 1% move on a ₹200 stock and on a ₹4,000 stock are not the same risk, and sizing off price alone is how a "small" loss turns out not to be.

---

## Project layout

```
nse-algo-bot/
├── main.py                 orchestration — the whole day, start to finish
├── indicators.py           EMPTY scaffold — your indicators   ← write this
├── strategy.py             EMPTY scaffold — your entry rule   ← write this
├── scanner_ws.py           market feed, running O/H/L, per-tick evaluation
├── broker.py               balance, leverage, sizing, orders, fills
├── monitor.py              stop · trail · profit lock · target · force exit
├── copy_trading.py         mirror entries and exits onto follower accounts
├── db.py                   1H → 2H/4H candle store
├── daily_db.py             daily candle store
├── incremental_updater.py  advance saved indicator state to the latest bar
├── watchlist.py            symbols → security IDs from the instrument master
├── nse_holidays.py         trading calendar
├── login.py                API headers, always built from the current token
├── auto_login.py           TOTP token generation, expiry and liveness checks
├── frontend.py             Flask + SSE dashboard
├── signal_store.py         per-day record of what actually fired
├── telegram_notify.py      alerts
└── tools/                  one-off seeding and maintenance scripts
```

---

## Security

- **No credential is in source.** `config.py` reads everything from environment variables or a local `.env`, and documents what to set and where to find it.
- `.env`, `access_token.txt`, the instrument master and every `*.db` are git-ignored.
- Follower-account credentials for copy trading live in `.env` as JSON, never in a tracked file.

---

## Disclaimer

For research and education. **This code can place real orders with real money.** It ships without a trading rule, so it cannot trade until you write one — and once you do, whatever it does is your responsibility, not this repository's.

Nothing here is investment advice. No rule is provided, none is implied, and no backtested or live result is claimed. Intraday leveraged trading loses money for most people who try it. Validate anything you write over a meaningful sample, keep `PAPER_TRADING` on far longer than feels necessary, and never deploy capital you cannot afford to lose entirely.

---

## License

[MIT](LICENSE)

### Core Implementation Code & Architecture
#### File: `tools/update_watchlist.py`
```python
import os, sys
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
import re

# Read EQ-only symbols
df = pd.read_csv(os.path.join(_ROOT, 'equity_watchlist_resolved.txt'))
eq = df[df['intraday_leverage'] == True]['symbol'].tolist()

# Build new WATCHLIST_SYMBOLS block (50 per line)
lines = []
for i in range(0, len(eq), 50):
    chunk = eq[i:i+50]
    quoted = [f"'{s}'" for s in chunk]
    lines.append(','.join(quoted))

new_value = 'WATCHLIST_SYMBOLS = [' + ',\n'.join(lines) + ']\n'

# Read config.py
with open(os.path.join(_ROOT, 'config.py'), 'r', encoding='utf-8') as f:
    content = f.read()

# Replace WATCHLIST_SYMBOLS block (handles multi-line list)
new_content = re.sub(
    r'WATCHLIST_SYMBOLS\s*=\s*\[.*?\]',
    new_value.strip(),
    content,
    flags=re.DOTALL
)

with open(os.path.join(_ROOT, 'config.py'), 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Done. {len(eq)} EQ symbols written to WATCHLIST_SYMBOLS in config.py")
```

#### File: `tools/resolve_watchlist.py`
```python
import os, sys
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd

with open(os.path.join(_ROOT, 'equity_watchlist.txt')) as f:
    user_symbols = [line.strip() for line in f if line.strip()]

df = pd.read_csv(os.path.join(_ROOT, 'security_id_list.csv'), low_memory=False)
nse_eq = df[(df['SEM_EXM_EXCH_ID'] == 'NSE') & (df['SEM_INSTRUMENT_NAME'] == 'EQUITY')]

symbol_to_id      = dict(zip(nse_eq['SEM_TRADING_SYMBOL'], nse_eq['SEM_SMST_SECURITY_ID']))
symbol_to_listing = dict(zip(nse_eq['SEM_TRADING_SYMBOL'], nse_eq.get('SEM_LISTING_DATE', '')))
eq_symbols        = set(nse_eq[nse_eq['SEM_SERIES'] == 'EQ']['SEM_TRADING_SYMBOL'].tolist())

resolved  = []
not_found = []
t2t_list  = []

for symbol in user_symbols:
    sid = symbol_to_id.get(symbol)
    if sid is None:
        not_found.append(symbol)
        continue

    try:
        listing_date = pd.to_datetime(str(symbol_to_listing.get(symbol, ''))).strftime('%Y-%m-%d')
    except Exception:
        listing_date = '1995-01-01'

    intraday = symbol in eq_symbols
    if not intraday:
        t2t_list.append(symbol)

    resolved.append({
        'symbol'      : symbol,
        'security_id' : str(int(sid)),
        'listing_date': listing_date,
        'intraday'    : intraday,
    })

out = os.path.join(_ROOT, 'equity_watchlist_resolved.txt')
with open(out, 'w') as f:
    f.write('symbol,security_id,listing_date,intraday_leverage\n')
    for r in resolved:
        f.write(f"{r['symbol']},{r['security_id']},{r['listing_date']},{r['intraday']}\n")

print(f"Total in txt        : {len(user_symbols)}")
print(f"Resolved with SID   : {len(resolved)}")
print(f"EQ (intraday OK)    : {len([r for r in resolved if r['intraday']])}")
print(f"T2T / BE / BZ       : {len(t2t_list)}")
print(f"Not found in CSV    : {len(not_found)}")
if not_found:
    print(f"Not found           : {not_found}")
print(f"Saved -> {out}")
```

#### File: `signal_store.py`
```python
# ─────────────────────────────────────────────────────────────────────────────
#  signal_store.py  —  persists a session's LIVE signals to disk, per trade day.
#
#  WHY:
#    When the scanner is re-run POST-MARKET (or on a holiday/weekend), we want to
#    show the SAME signals that actually fired during that day's LIVE session —
#    NOT a freshly recomputed replay. Each trading day's signals live in their
#    own JSON file under signal_store/, so they persist until the next live
#    session overwrites that day's file (i.e. valid "until the next 09:15").
#
#  FILES:
#    signal_store/<YYYY-MM-DD>.json  →  list of signal entry dicts for that day
# ─────────────────────────────────────────────────────────────────────────────

import json
import os
from datetime import date

_HERE = os.path.dirname(os.path.abspath(__file__))
_DIR  = os.path.join(_HERE, "signal_store")


def _path(trade_day: date) -> str:
    return os.path.join(_DIR, f"{trade_day.isoformat()}.json")


def reset(trade_day: date) -> None:
    """
    Start a FRESH store for a live session (overwrites any prior file for the
    day). Call once at the start of the live scan loop so the store reflects
    only the current session's signals.
    """
    os.makedirs(_DIR, exist_ok=True)
    with open(_path(trade_day), "w", encoding="utf-8") as f:
        json.dump([], f)


def append(trade_day: date, entry: dict) -> None:
    """Append one signal entry to the day's store (creates file if missing)."""
    os.makedirs(_DIR, exist_ok=True)
    signals = load(trade_day)
    signals.append(entry)
    with open(_path(trade_day), "w", encoding="utf-8") as f:
        json.dump(signals, f, ensure_ascii=False, default=str)


def load(trade_day: date) -> list[dict]:
    """Return the day's stored signal entries ([] if file missing/empty/corrupt)."""
    try:
        with open(_path(trade_day), "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def exists(trade_day: date) -> bool:
    """True if a store file was written for this trade day (a live session ran)."""
    return os.path.exists(_path(trade_day))
```

#### File: `login.py`
```python
# ─────────────────────────────────────────────────────────────────────────────
#  login.py  —  Shared broker connection
#
#  NOTE: the request headers are built by a function (get_headers), NOT a
#  module-level dict. A static dict would be built at import time — before
#  auto_login patches config.ACCESS_TOKEN — so every API call would use the
#  old, expired token (HTTP 401 / DH-906).
#
#  By calling get_headers() inside every request we always pick up whatever
#  token is currently in config.ACCESS_TOKEN.
#
#  ⚠️  No credentials live here. config.CLIENT_ID / config.ACCESS_TOKEN come
#      from your own `.env` file — see config.py for the full setup steps.
# ─────────────────────────────────────────────────────────────────────────────

import config

dhan = None


def mask_client_id(cid: str = "") -> str:
    """Client ID with all but the last 4 digits hidden.

    The startup line ends up in terminal screenshots, shared logs and bug
    reports far more often than anyone intends, and a client ID is half of
    what an attacker needs. The tail is kept so you can still tell which
    account a run used.
    """
    cid = str(cid or config.CLIENT_ID or "")
    return "*" * max(len(cid) - 4, 0) + cid[-4:] if cid else "(not set)"


def reload_dhan():
    """
    (Re)creates the broker SDK client with the current config.ACCESS_TOKEN.
    Safe to call when credentials are missing — it leaves `dhan` as None
    instead of raising at import time.
    """
    global dhan
    if not (config.CLIENT_ID and config.ACCESS_TOKEN):
        dhan = None
        return None
    try:
        from dhanhq import dhanhq
        dhan = dhanhq(config.CLIENT_ID, config.ACCESS_TOKEN)
        print(f"[OK] Broker client ready | Client: {mask_client_id()}")
    except Exception as e:
        dhan = None
        print(f"[WARN] Broker SDK unavailable: {e}")
    return dhan


def get_headers() -> dict:
    """
    Returns the API request headers using the CURRENT access token.

    Always call this right before each request. Do NOT cache the result.
    """
    return {
        "Accept"       : "application/json",
        "Content-Type" : "application/json",
        "access-token" : config.ACCESS_TOKEN,
        "client-id"    : config.CLIENT_ID,
    }


if config.CLIENT_ID and config.ACCESS_TOKEN:
    reload_dhan()
```

#### File: `nse_holidays.py`
```python
# ─────────────────────────────────────────────────────────────────────────────
#  nse_holidays.py  —  NSE Trading Holiday Calendar
#
#  Used by db.py and daily_db.py to determine the last valid trading day.
#  When today (or a candidate day) is a weekend OR a listed NSE holiday,
#  _last_biz_day() steps back further to find the most recent trading session.
#
#  ⚠️  UPDATE THIS LIST EACH YEAR with the official NSE holiday schedule.
# ─────────────────────────────────────────────────────────────────────────────

from datetime import date, timedelta

# ── NSE Trading Holidays 2026 ─────────────────────────────────────────────────
NSE_HOLIDAYS_2026: set[date] = {
    date(2026,  1, 15),   # Municipal Corporation Election - Maharashtra
    date(2026,  1, 26),   # Republic Day
    date(2026,  3,  3),   # Holi
    date(2026,  3, 26),   # Shri Ram Navami
    date(2026,  3, 31),   # Shri Mahavir Jayanti
    date(2026,  4,  3),   # Good Friday
    date(2026,  4, 14),   # Dr. Baba Saheb Ambedkar Jayanti
    date(2026,  4, 25),   # Dr. Baba Saheb Ambedkar Jayanti (observed / NSE holiday)
    date(2026,  5,  1),   # Maharashtra Day
    date(2026,  5, 28),   # Bakri Id
    date(2026,  6, 26),   # Muharram
    date(2026,  9, 14),   # Ganesh Chaturthi
    date(2026, 10,  2),   # Mahatma Gandhi Jayanti
    date(2026, 10, 20),   # Dussehra
    date(2026, 11, 10),   # Diwali-Balipratipada
    date(2026, 11, 24),   # Prakash Gurpurb Sri Guru Nanak Dev
    date(2026, 12, 25),   # Christmas
}

# Master set — add future years here
NSE_HOLIDAYS: set[date] = set()
NSE_HOLIDAYS.update(NSE_HOLIDAYS_2026)


def is_trading_day(d: date) -> bool:
    """
    Returns True if `d` is a valid NSE trading day:
      • Not a Saturday (weekday == 5)
      • Not a Sunday  (weekday == 6)
      • Not a listed NSE holiday
    """
    if d.weekday() >= 5:       # Saturday=5, Sunday=6
        return False
    if d in NSE_HOLIDAYS:
        return False
    return True


def last_trading_day(ref: date | None = None) -> date:
    """
    Returns the most recent NSE trading day STRICTLY BEFORE `ref`.
    If `ref` is None, uses today's date.

    Handles all of: weekends, NSE holidays, and long holiday streaks.

    Examples (run date shown on left → result on right):
      Friday  24-Apr-2026 (today)   → Thursday 23-Apr-2026
      Monday  27-Apr-2026           → Friday   24-Apr-2026  ✅ (skips Sat+Sun)
      Tuesday 28-Apr-2026           → Monday   27-Apr-2026
      Saturday 25-Apr-2026          → Friday   24-Apr-2026
      Sunday  26-Apr-2026           → Friday   24-Apr-2026
      Tuesday 29-May-2026           → Monday   29-May-2026
        wait — Bakri Id is 28-May (Thu) → so last trading day = Wed 27-May-2026
    """
    d = (ref if ref is not None else date.today()) - timedelta(days=1)
    while not is_trading_day(d):
        d -= timedelta(days=1)
    return d
```

#### File: `tools/fetch_15min.py`
```python
"""
fetch_15min.py  —  Fetch today's first 15-min candle (the 09:15 bar) for ICICIAMC

Usage:
    python fetch_15min.py

Token : taken from config.ACCESS_TOKEN automatically
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import datetime
from dhanhq import dhanhq
import config

# ── Config ────────────────────────────────────────────────────────────────────
SECURITY_ID = "760407"          # ICICIAMC
SYMBOL      = "ICICIAMC"
TODAY       = datetime.now().strftime("%Y-%m-%d")

dhan = dhanhq(config.CLIENT_ID, config.ACCESS_TOKEN)

# ── API Call ──────────────────────────────────────────────────────────────────
print(f"\n{'='*55}")
print(f"  Dhan Intraday API — {SYMBOL}  ({TODAY})")
print(f"  Fetching 09:15 first 15-min candle...")
print(f"{'='*55}\n")

result = dhan.intraday_minute_data(
    security_id    = SECURITY_ID,
    exchange_segment = dhan.NSE,
    instrument_type  = "EQUITY",
    interval         = 15,
    from_date        = TODAY,
    to_date          = TODAY,
)

if result.get("status") != "success":
    print(f"  ERROR: {result.get('remarks', result)}")
    sys.exit(1)

data = result["data"]

# ── Parse candles ─────────────────────────────────────────────────────────────
timestamps = data.get("timestamp", [])
opens      = data.get("open",      [])
highs      = data.get("high",      [])
lows       = data.get("low",       [])
closes     = data.get("close",     [])
volumes    = data.get("volume",    [])

if not timestamps:
    print("  No data returned. Market may not be open yet, or holiday.")
    sys.exit(0)

print(f"  Total candles returned : {len(timestamps)}\n")
print(f"  {'Time':<12} {'Open':>10} {'High':>10} {'Low':>10} {'Close':>10} {'Volume':>12}")
print(f"  {'-'*66}")

target_candle = None

for i, ts in enumerate(timestamps):
    dt   = datetime.fromtimestamp(ts)
    o, h, l, c, v = opens[i], highs[i], lows[i], closes[i], volumes[i]
    time_str = dt.strftime("%H:%M:%S")
    marker = "  <-- 09:15 bar (FIRST 15MIN)" if (dt.hour == 9 and dt.minute == 15) else ""
    print(f"  {time_str:<12} {o:>10.2f} {h:>10.2f} {l:>10.2f} {c:>10.2f} {v:>12,.0f}{marker}")
    if dt.hour == 9 and dt.minute == 15:
        target_candle = {"time": time_str, "open": o, "high": h, "low": l, "close": c, "volume": v}

print()

if target_candle:
    print(f"{'='*55}")
    print(f"  First 15-min Candle (09:15 bar)  —  {SYMBOL}")
    print(f"{'='*55}")
    print(f"  Open   : Rs{target_candle['open']:.2f}")
    print(f"  High   : Rs{target_candle['high']:.2f}")
    print(f"  Low    : Rs{target_candle['low']:.2f}")
    print(f"  Close  : Rs{target_candle['close']:.2f}")
    print(f"  Volume :  {target_candle['volume']:,.0f}")
else:
    dt = datetime.fromtimestamp(timestamps[0])
    print(f"  09:15 bar not found exactly — using first candle ({dt.strftime('%H:%M:%S')})")
    print(f"  Open   : Rs{opens[0]:.2f}")
    print(f"  High   : Rs{highs[0]:.2f}")
    print(f"  Low    : Rs{lows[0]:.2f}")
    print(f"  Close  : Rs{closes[0]:.2f}")
    print(f"  Volume :  {volumes[0]:,.0f}")

print(f"{'='*55}\n")
```


==================================================


## [3/3] Repository: nse-bse-algo-strategies (`WHEEL_nse-bse-algo-strategies`)
- **Full Name**: `nse-bse-algo-strategies`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Algo Trading - Option Selling Trading Strategies India

[![GitHub stars](https://img.shields.io/github/stars/buzzsubash/algo_trading_strategies_india?style=social)](https://github.com/buzzsubash/algo_trading_strategies_india/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/buzzsubash/algo_trading_strategies_india?style=social)](https://github.com/buzzsubash/algo_trading_strategies_india/network/members)
[![License](https://img.shields.io/github/license/buzzsubash/algo_trading_strategies_india)](LICENSE)

## About
This repository is an **open-source** collection of **algorithmic trading strategies** for the Indian stock market, with a primary focus on **option selling** in:
- **NIFTY 50**
- **BANK NIFTY**
- **SENSEX**
- **MIDCAP NIFTY**
- **FIN NIFTY**

### 🔹 **Current Broker Support**
- ✅ **Zerodha** (Live & Ready to Deploy)
- ⚙️ **AngelOne, Upstox, Fyers, AliceBlue, etc.** *(Coming Soon!)*

## 🚀 Features
✅ **Multiple short-straddle strategies** with different risk management techniques  
✅ **Multiple short-strangle strategies** — OTM selling across BankNifty, Nifty50, FinNifty & Sensex  
✅ **Iron-fly strategies** for hedged option selling  
✅ **Stop-loss mechanisms** including **fixed, percentage-based, and trailing stops**  
✅ **Mark-to-market (MTM) based target execution**  
✅ **Copy trading** — automatically mirror a master account's positions across multiple client accounts with capital-proportional scaling  
✅ Future expansion for **multi-broker support**

---

## 📂 Repository Structure

| Strategy Category | Sub-Category | Strategy Name | Zerodha | AngelOne | Upstox | Fyers | GitHub Link |
|------------------|-------------|---------------|---------|----------|--------|-------|-------------|
| **Short Straddle** | 0920 Expiry | FINNIFTY 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/0920_short_straddle/finnifty_0920_short_straddle.py) |
|  |  | NIFTY50 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/0920_short_straddle/nifty50_0920_short_straddle.py) |
|  |  | BANKNIFTY 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/0920_short_straddle/banknifty_0920_short_straddle.py) |
|  |  | SENSEX 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/0920_short_straddle/sensex_0920_short_straddle.py) |
|  | Combined Premium | BANK NIFTY Combined Premium | ✅ | ✅ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/combined_premium/bank_nifty_combined_premium_short_straddle.py) |
|  |  | FINNIFTY Combined Premium | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/combined_premium/finnifty_combined_premium_short_straddle.py) |
|  |  | NIFTY50 Combined Premium | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/combined_premium/nifty50_combined_premium_short_straddle.py) |
|  |  | SENSEX Combined Premium | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/combined_premium/sensex_combined_premium_short_straddle.py) |
|  | Fixed Stop Loss | BANK NIFTY Fixed SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/fixed_stop_loss/bank_nifty_fixed_stop_loss_short_straddle.py) |
|  |  | BANK NIFTY Account-Level MTM SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/fixed_stop_loss/bank_nifty_account_level_mtm_with_fixed_stop_loss_short_straddle.py) |
|  | MTM Based Target | BANK NIFTY MTM-Based | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/mtm_based_target/bank_nifty_mtm_based_short_straddle.py) |
|  |  | NIFTY50 MTM-Based | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/mtm_based_target/nifty50_mtm_based_short_straddle.py) |
|  | Percentage-Based Stop Loss | BANK NIFTY Percentage-Based SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/percentage_based_stop_loss/bank_nifty_percentage_based_stop_loss_short_straddle.py) |
|  | Trailing Stop Loss | BANK NIFTY Trailing Percentage-Based SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-straddle/trailing_stop_loss/bank_nifty_trailing_percentage_based_stop_loss_short_straddle.py) |
| **Iron-Fly** | | | ⚙️ In Development | | | | *(Coming Soon!)* |
| **Short Strangle** | 0920 Expiry | BANKNIFTY 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/0920_short_strangle/banknifty_0920_short_strangle.py) |
|  |  | NIFTY50 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/0920_short_strangle/nifty50_0920_short_strangle.py) |
|  |  | FINNIFTY 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/0920_short_strangle/finnifty_0920_short_strangle.py) |
|  |  | SENSEX 0920 | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/0920_short_strangle/sensex_0920_short_strangle.py) |
|  | Combined Premium | BANK NIFTY Combined Premium | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/combined_premium/bank_nifty_combined_premium_short_strangle.py) |
|  | Fixed Stop Loss | BANK NIFTY Fixed SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/fixed_stop_loss/bank_nifty_fixed_stop_loss_short_strangle.py) |
|  |  | BANK NIFTY Account-Level MTM SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/fixed_stop_loss/bank_nifty_account_level_mtm_with_fixed_stop_loss_short_strangle.py) |
|  | MTM Based Target | BANK NIFTY MTM-Based | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/mtm_based_target/bank_nifty_mtm_based_short_strangle.py) |
|  |  | NIFTY50 MTM-Based | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/mtm_based_target/nifty50_mtm_based_short_strangle.py) |
|  | Percentage-Based Stop Loss | BANK NIFTY Percentage-Based SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/percentage_based_stop_loss/bank_nifty_percentage_based_stop_loss_short_strangle.py) |
|  | Trailing Stop Loss | BANK NIFTY Trailing Percentage-Based SL | ✅ | ❌ | ❌ | ❌ | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/short-strangle/trailing_stop_loss/bank_nifty_trailing_percentage_based_stop_loss_short_strangle.py) |

---

### 📊 **Historical Data**

| **Data Source** | **Finvasia Shoonya** | **Zerodha Kite**                                                                                               | **AngelOne** | **Upstox** | **Fyers** |
|----------------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------|------------|-----------|
| **Equity Data (NSE/BSE)** | ✅ **Ready** | ✅ **Ready**                                                                                                    | ⚙️ Coming Soon | ⚙️ Coming Soon | ⚙️ Coming Soon |
| **Options Data** | ⚙️ In Development | ⚙️ In Development                                                                                              | ⚙️ Coming Soon | ⚙️ Coming Soon | ⚙️ Coming Soon |
| **Futures Data** | ⚙️ In Development | ⚙️ In Development                                                                                              | ⚙️ Coming Soon | ⚙️ Coming Soon | ⚙️ Coming Soon |
| **Database Storage** | ✅ PostgreSQL | ✅ PostgreSQL                                                                                                   | ⚙️ Coming Soon | ⚙️ Coming Soon | ⚙️ Coming Soon |
| **API Cost** | 🆓 **Free** | 💰 ₹2000/month                                                                                                 | 💰 Paid | 💰 Paid | 💰 Paid |
| **GitHub Link** | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/tree/main/historical-data-collection/shoonya-finvasia) | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/tree/main/historical-data-collection/zerodha-kite-api) | *Coming Soon* | *Coming Soon* | *Coming Soon* |

---

### 🔧 **Broker Utilities & Auto-Login Scripts**

| **Utility Type** | **Broker** | **Description** | **Status** | **Features** | **GitHub Link** |
|------------------|------------|-----------------|------------|--------------|-----------------|
| **Auto-Login** | **Zerodha Kite** | Automated login with 2FA support | ✅ **Ready** | • TOTP Authentication<br>• Token Management<br>• Telegram Notifications<br>• Retry Mechanism<br>• Error Handling | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/blob/main/broker-utilities/zerodha-kite-connect-auto-login.py) |
| **MTM Square-off System** | **Zerodha Kite** | Real-time MTM monitoring with automated square-off | ✅ **Ready** | • Real-time Position Monitoring<br>• Loss Threshold Protection<br>• Daily Profit Target Management<br>• Bulletproof Order Execution<br>• Trading Discipline Mode<br>• Volume Freeze Handling<br>• Comprehensive Logging | [View Code](https://github.com/buzzsubash/algo_trading_strategies_india/tree/main/broker-utilities/mtm_square_off_zerodha) |

---

## 📌 How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/buzzsubash/algo_trading_strategies_india.git
   

---

## 📩 Contact & Collaboration  

I'm always open to discussions on **algo trading**, whether it's:  
✅ Enhancing existing strategies  
✅ Designing new trading algorithms  
✅ Deep-diving into strategy backtesting  
✅ Exploring advanced risk management techniques  

If you're interested in collaborating or discussing algo trading strategies, feel free to connect with me!  

### 🔗 **Let's Connect!**  

- 📱 **WhatsApp:** [https://wa.me/919605006699](https://wa.me/919605006699) [https://wa.me/6594675969](https://wa.me/6594675969)  
- 🐦 **Twitter (X):** [https://x.com/buzzsubash](https://x.com/buzzsubash)  
- 📍 **LinkedIn:** [https://www.linkedin.com/in/buzzsubash](https://www.linkedin.com/in/buzzsubash)
- 💻 **GitHub:** [https://github.com/buzzsubash](https://github.com/buzzsubash)  
- 📘 **Facebook:** [https://www.facebook.com/buzzsubash/](https://www.facebook.com/buzzsubash/)  
- 🏆 **Credly Certifications:** [https://www.credly.com/users/subash-krishnan](https://www.credly.com/users/subash-krishnan)  
- 👾 **Reddit:** [https://www.reddit.com/user/buzzsubash/](https://www.reddit.com/user/buzzsubash/)  
- 📝 **Blog:** [https://emcsaninfo.wordpress.com/](https://emcsaninfo.wordpress.com/)  


🚀 **Let's build, test, and innovate in the algo trading space together!**  


## ⚠️ Disclaimer & Risk Warning

This repository contains my **personal work** and is intended **purely for educational purposes**.  
These strategies are **not** financial or investment advice. And I am **not a SEBI registered** investment advisor or a research analyst.

Trading in derivatives, particularly in options, carries **significant risk** and can result in substantial financial losses. **Over 90% of traders in index options incur losses**, as highlighted by financial regulators and experts.


🔥 **Trade Responsibly. Invest Wisely. Stay Safe.** 🔥

### Core Implementation Code & Architecture
#### File: `historical-data-collection/shoonya-finvasia/api_helper.py`
```python
from NorenRestApiPy.NorenApi import  NorenApi
from threading import Timer
import pandas as pd
import time
import concurrent.futures

api = None
class Order:
     def __init__(self, buy_or_sell:str = None, product_type:str = None,
                 exchange: str = None, tradingsymbol:str =None, 
                 price_type: str = None, quantity: int = None, 
                 price: float = None,trigger_price:float = None, discloseqty: int = 0,
                 retention:str = 'DAY', remarks: str = "tag",
                 order_id:str = None):
        self.buy_or_sell=buy_or_sell
        self.product_type=product_type
        self.exchange=exchange
        self.tradingsymbol=tradingsymbol
        self.quantity=quantity
        self.discloseqty=discloseqty
        self.price_type=price_type
        self.price=price
        self.trigger_price=trigger_price
        self.retention=retention
        self.remarks=remarks
        self.order_id=None


    #print(ret)

    


def get_time(time_string):
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')

    return time.mktime(data)


class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/', websocket='wss://api.shoonya.com/NorenWSTP/')        
        global api
        api = self

    def place_basket(self, orders):

        resp_err = 0
        resp_ok  = 0
        result   = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

            future_to_url = {executor.submit(self.place_order, order): order for order in  orders}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
            try:
                result.append(future.result())
            except Exception as exc:
                print(exc)
                resp_err = resp_err + 1
            else:
                resp_ok = resp_ok + 1

        return result
                
    def placeOrder(self,order: Order):
        ret = NorenApi.place_order(self, buy_or_sell=order.buy_or_sell, product_type=order.product_type,
                            exchange=order.exchange, tradingsymbol=order.tradingsymbol, 
                            quantity=order.quantity, discloseqty=order.discloseqty, price_type=order.price_type, 
                            price=order.price, trigger_price=order.trigger_price,
                            retention=order.retention, remarks=order.remarks)
        #print(ret)

        return ret
```

#### File: `copy-trading/zerodha_kite_api/login_single_account.py`
```python
import os
import yaml
import requests
import threading
import argparse
from flask import Flask
from kiteconnect import KiteConnect
import pyotp
import logging
from werkzeug.serving import make_server
import psycopg2
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PORT = 5000
HOST = "127.0.0.1"

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'clients_config.yaml')


def load_account_config(account_name):
    with open(CONFIG_PATH) as f:
        config = yaml.safe_load(f)

    master = config['master_account']
    if master['name'] == account_name:
        return config, master

    for client in config.get('clients', []):
        if client['name'] == account_name:
            return config, client

    raise ValueError(f"Account '{account_name}' not found in clients_config.yaml")


class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server(HOST, PORT, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()


def autologin(config, account):
    db = config['database']
    tg = config.get('telegram', {})
    telegram_token = tg.get('token', '')
    chat_id = tg.get('error_chat_id', '')

    conn_params = {
        'host': db['host'],
        'port': db['port'],
        'dbname': db['name'],
        'user': db['user'],
        'password': db['password'],
    }

    def notify(text):
        if not telegram_token or not chat_id:
            return
        try:
            requests.post(
                f"https://api.telegram.org/bot{telegram_token}/sendMessage",
                json={'chat_id': chat_id, 'text': text},
                timeout=5,
            )
        except Exception:
            pass

    def save_token_to_db(access_token, request_token):
        sql = """
            INSERT INTO master_accounts (name, user_id, api_key, api_secret, totp_key, password,
                                         access_token, request_token, token_generated_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (name) DO UPDATE SET
                access_token       = EXCLUDED.access_token,
                request_token      = EXCLUDED.request_token,
                token_generated_at = EXCLUDED.token_generated_at,
                updated_at         = EXCLUDED.updated_at
        """
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute(sql, (
            account['name'], account['user_id'], account['api_key'],
            account['api_secret'], account['totp_key'], account['password'],
            access_token, request_token, now, now,
        ))
        conn.commit()
        cursor.close()
        conn.close()

    while True:
        try:
            session = requests.Session()
            twofa = pyotp.TOTP(account['totp_key']).now()
            login_resp = session.post(
                "https://kite.zerodha.com/api/login",
                data={"user_id": account['user_id'], "password": account['password']},
            ).json()
            request_id = login_resp["data"]["request_id"]
            session.post(
                "https://kite.zerodha.com/api/twofa",
                data={"user_id": account['user_id'], "request_id": request_id, "twofa_value": twofa},
            )
            api_session = session.get(f"https://kite.trade/connect/login?api_key={account['api_key']}")
            request_token = api_session.url.split("request_token=")[1].split("&")[0]

            kite = KiteConnect(api_key=account['api_key'])
            data = kite.generate_session(request_token, api_secret=account['api_secret'])
            access_token = data["access_token"]

            token_file = account['access_token_file']
            os.makedirs(os.path.dirname(os.path.abspath(token_file)), exist_ok=True)
            with open(token_file, 'w') as f:
                f.write(access_token)

            save_token_to_db(access_token, request_token)
            notify(f"✅ {account['name']}: Access token generated")
            logging.info(f"Login successful for {account['name']}")
            return request_token, access_token, kite

        except Exception as e:
            logging.error(f"Login error for {account['name']}: {e}")
            notify(f"❌ {account['name']} login error: {e}")
            continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Kite single account login')
    parser.add_argument('--account', required=True, help='Account name as defined in clients_config.yaml')
    args = parser.parse_args()

    config, account = load_account_config(args.account)

    app = Flask(__name__)
    server = ServerThread(app)
    server.start()

    try:
        request_token, access_token, kite = autologin(config, account)
        print(f"Access token: {access_token}")
        print(f"Profile: {kite.profile()}")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        server.shutdown()
```

#### File: `short-strangle/fixed_stop_loss/bank_nifty_fixed_stop_loss_short_strangle.py`
```python
from kiteconnect import KiteConnect
import pandas as pd
import datetime as dt
import time


lots = 5  # quantity
strangle_width = 100  # points away from ATM (BankNifty strikes in 100-point intervals)
ce_stoploss_value = 50
pe_stoploss_value = 60


nse_holidays = [dt.date(2021, 7, 21), dt.date(2021, 8, 19), dt.date(2021, 9, 10), dt.date(2021, 10, 15), dt.date(2021, 11, 4), dt.date(2021, 11, 5), dt.date(2021, 11, 19)]


api_key = ""
api_secret = ""

access_token = open('/home/ec2-user/keyfiles/', 'r').read()

open_time = dt.time(hour=9, minute=15)
trade_entry_time = dt.time(hour=9, minute=59)
re_entry_time = dt.time(hour=12, minute=30)
sqf_time = dt.time(hour=15, minute=6)


kite = KiteConnect(api_key=api_key)

kite.set_access_token(access_token)


def get_expiry_date():
    current_date = dt.date.today()
    wd = current_date.weekday()
    x = 0
    if wd <= 3:
        x = (3 - wd)
    else:
        x = 6

    exp_date = current_date + dt.timedelta(days=x)

    if exp_date in nse_holidays:
        exp_date = exp_date - dt.timedelta(days=1)

    if exp_date in nse_holidays:
        exp_date = exp_date - dt.timedelta(days=1)
    return exp_date

def get_banknifty_atm_strike(ltp):
    r = ltp % 100
    if r < 50:
        atm = ltp - r
    else:
        atm = ltp - r + 100
    return int(atm)

def get_trading_symbol(df, strike, CE_or_PE):
    df_1 = df[df.strike == strike]
    ce_name = df_1[df_1.instrument_type == 'CE'].tradingsymbol.values[0]
    pe_name = df_1[df_1.instrument_type == 'PE'].tradingsymbol.values[0]
    if CE_or_PE == 'CE':
        symbol = ce_name
    elif CE_or_PE == 'PE':
        symbol = pe_name
    return symbol

def get_banknifty_ltp():
    a = 0
    while a < 10:
        try:
            bn = kite.ltp('NSE:NIFTY BANK')
            bn_ltp = bn['NSE:NIFTY BANK']['last_price']
            break
        except:
            print("can't extract LTP data..retrying")
            time.sleep(1)
            a += 1
    return bn_ltp


def marketorder_buy(symbol, quantity):
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def marketorder_sell(symbol, quantity):
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def stoploss_order_buy(symbol, quantity, trig_price):
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_SLM,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR,
                    trigger_price=trig_price)


def get_trade_price(order_id):
    a = 0
    while a < 10:
        try:
            tb_df = pd.DataFrame(kite.trades())
            trade_price = tb_df[tb_df.order_id == order_id].average_price.values[0]
            break
        except:
            print("can't extract order data..retrying")
            time.sleep(1)
            a += 1
    return trade_price

def get_order_status(order_id):
    a = 0
    while a < 10:
        try:
            tb_df = pd.DataFrame(kite.trades())
            break
        except:
            print("can't extract order data..retrying")
            time.sleep(1)
            a += 1

    df = tb_df[tb_df.order_id == order_id]

    if len(df) > 0:
        return 'executed'
    else:
        return 'pending'

def round_5ps(price):
    r = round(price % .05, 2)
    rp = round(price - r, 2)
    return float(rp)

def cancel_order(order_id):
    kite.cancel_order(order_id=order_id,
                    variety=kite.VARIETY_REGULAR)


def calculate_atm_and_place_order():
    global bn_ltp, atm_strike, ce_symbol, pe_symbol, ce_order_id, pe_order_id
    global ce_sell_price, pe_sell_price, ce_sl_orderid, pe_sl_orderid

    bn_ltp = get_banknifty_ltp()

    atm_strike = get_banknifty_atm_strike(bn_ltp)

    # Strangle: sell OTM call above ATM, OTM put below ATM
    ce_symbol = get_trading_symbol(bn_exp_df, atm_strike + strangle_width, 'CE')
    pe_symbol = get_trading_symbol(bn_exp_df, atm_strike - strangle_width, 'PE')
    print(ce_symbol)
    print(pe_symbol)

    ce_order_id = marketorder_sell(ce_symbol, lots * 25)
    pe_order_id = marketorder_sell(pe_symbol, lots * 25)

    ce_sell_price = get_trade_price(ce_order_id)
    pe_sell_price = get_trade_price(pe_order_id)

    ce_sl_orderid = stoploss_order_buy(ce_symbol, lots * 25, float(round_5ps(ce_sell_price + ce_stoploss_value)))
    pe_sl_orderid = stoploss_order_buy(pe_symbol, lots * 25, float(round_5ps(pe_sell_price + pe_stoploss_value)))


# downloading instrument dump
a = 0
while a <= 10:
    try:
        instrument_dump = kite.instruments("NFO")
        break
    except:
        print("can't instrument data..retrying")
        time.sleep(1)
        a += 1

instrument_df = pd.DataFrame(instrument_dump)

expiry_date = get_expiry_date()

bn = instrument_df[instrument_df.name == 'BANKNIFTY']
bn_exp_df = bn[bn.expiry == expiry_date]

while dt.datetime.now().time() < trade_entry_time:
    time.sleep(1)

calculate_atm_and_place_order()

while dt.datetime.now().time() < re_entry_time:
    time.sleep(1)

ce_sl_status = get_order_status(ce_sl_orderid)
pe_sl_status = get_order_status(pe_sl_orderid)

if ce_sl_status == 'executed' and pe_sl_status == 'executed':
    calculate_atm_and_place_order()


while dt.datetime.now().time() < sqf_time:
    time.sleep(1)

ce_sl_status = get_order_status(ce_sl_orderid)
pe_sl_status = get_order_status(pe_sl_orderid)

if ce_sl_status == 'pending':
    cancel_order(ce_sl_orderid)
    marketorder_buy(ce_symbol, lots * 25)

if pe_sl_status == 'pending':
    cancel_order(pe_sl_orderid)
    marketorder_buy(pe_symbol, lots * 25)
```

#### File: `short-straddle/fixed_stop_loss/bank_nifty_fixed_stop_loss_short_straddle.py`
```python
from kiteconnect import KiteConnect
import pandas as pd
import datetime as dt
import time


lots=5  # quanity
ce_stoploss_value=50
pe_stoploss_value=60


nse_holidays=[dt.date(2021,7,21),dt.date(2021,8,19),dt.date(2021,9,10),dt.date(2021,10,15),dt.date(2021,11,4),dt.date(2021,11,5),dt.date(2021,11,19)]


api_key = ""
api_secret = ""

access_token=open('/home/ec2-user/keyfiles/','r').read()

open_time=dt.time(hour=9,minute=15)
trade_entry_time=dt.time(hour=9,minute=59)
re_entry_time=dt.time(hour=12,minute=30)
sqf_time=dt.time(hour=15,minute=6)


kite = KiteConnect(api_key=api_key)

kite.set_access_token(access_token)


def get_expiry_date():
    #this module will not work in sunday or saturday
    current_date=dt.date.today()
    wd=current_date.weekday()
    #print(wd)   # 0 Monday, 6 sunday
    #this module will not work on sunday and saturday
    #calculating value of x ('current date' + 'x' will be next weekly exp day)
    x=0
    if wd<=3:
        x=(3-wd)
    else:
        x=6
    
    exp_date=current_date+dt.timedelta(days=x)
   
    if exp_date in nse_holidays:
        exp_date=exp_date-dt.timedelta(days=1)
        
    if exp_date in nse_holidays:
        exp_date=exp_date-dt.timedelta(days=1)
    return exp_date

def get_banknifty_atm_strike(ltp):
    r=ltp%100
    if r<50:
       atm=ltp-r
    else:
        atm=ltp-r+100
    return int(atm)

def get_trading_symbol(df,strike,CE_or_PE):
    
    df_1=df[df.strike==strike]
    ce_name=df_1[df_1.instrument_type=='CE'].tradingsymbol.values[0]
    pe_name=df_1[df_1.instrument_type=='PE'].tradingsymbol.values[0]
    if CE_or_PE=='CE':
        symbol=ce_name
    elif CE_or_PE=='PE':
        symbol=pe_name
    return symbol
    
def get_banknifty_ltp():
 
    a = 0
    while a < 10:
        try:
            bn=kite.ltp('NSE:NIFTY BANK')
            bn_ltp=bn['NSE:NIFTY BANK']['last_price']
            break
        except:
            print("can't extract LTP data..retrying")
            time.sleep(1)
            a+=1
    return bn_ltp


def marketorder_buy(symbol,quantity):    
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def marketorder_sell(symbol,quantity):    
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def stoploss_order_buy(symbol,quantity,trig_price):    
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_SLM,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR,
                    trigger_price=trig_price)


def get_trade_price(order_id):
    a=0
    while a < 10:
        try:
            tb_df=pd.DataFrame(kite.trades())
            trade_price=tb_df[tb_df.order_id==order_id].average_price.values[0]
            break
        except:
            print("can't extract oreder data..retrying")
            time.sleep(1)
            a+=1
    return trade_price

def get_order_status(order_id):
    a=0
    while a < 10:
        try:
            tb_df=pd.DataFrame(kite.trades())
            break
        except:
            print("can't extract oreder data..retrying")
            time.sleep(1)
            a+=1

    df=tb_df[tb_df.order_id==order_id]
    
    if len(df)>0:
        return 'executed'
    else:
        return 'pending'

def round_5ps(price):
        r = round(price % .05, 2)
        rp = round(price - r, 2)
        return float(rp)

def cancel_order(order_id):    
    kite.cancel_order(order_id=order_id,
                    variety=kite.VARIETY_REGULAR)



def calculate_atm_and_place_order():
    global bn_ltp, atm_strike, ce_symbol, pe_symbol, ce_order_id, pe_order_id
    global ce_sell_price, pe_sell_price, ce_sl_orderid, pe_sl_orderid
#######################################################################
     
    bn_ltp=get_banknifty_ltp()
    
    atm_strike=get_banknifty_atm_strike(bn_ltp)
    
    ce_symbol=get_trading_symbol(bn_exp_df, atm_strike,'CE')
    
    pe_symbol=get_trading_symbol(bn_exp_df, atm_strike,'PE')
    print(ce_symbol)
    print(pe_symbol)
    
    ce_order_id=marketorder_sell(ce_symbol, lots*25)
    
    pe_order_id=marketorder_sell(pe_symbol, lots*25)
    
    ce_sell_price=get_trade_price(ce_order_id)
    pe_sell_price=get_trade_price(pe_order_id)
    
    ce_sl_orderid=stoploss_order_buy(ce_symbol, lots*25,float(round_5ps(ce_sell_price+ce_stoploss_value)))
    pe_sl_orderid=stoploss_order_buy(pe_symbol, lots*25,float(round_5ps(pe_sell_price+pe_stoploss_value)))

#######################################################



#downloading instrument dump 
a=0
while a<=10:
    try:
        instrument_dump = kite.instruments("NFO")
        break
    except:
        print("can't instrument data..retrying")
        time.sleep(1)
        a+=1

instrument_df = pd.DataFrame(instrument_dump)

expiry_date=get_expiry_date()

bn=instrument_df[instrument_df.name=='BANKNIFTY']
bn_exp_df=bn[bn.expiry==expiry_date]

while dt.datetime.now().time()<trade_entry_time:
    time.sleep(1)
###############################

calculate_atm_and_place_order()

###############################

while dt.datetime.now().time()<re_entry_time:
    time.sleep(1)

ce_sl_status=get_order_status(ce_sl_orderid)
pe_sl_status=get_order_status(pe_sl_orderid)

if ce_sl_status=='executed' and pe_sl_status=='executed':
    calculate_atm_and_place_order()


while dt.datetime.now().time()<sqf_time:
    time.sleep(1)

ce_sl_status=get_order_status(ce_sl_orderid)
pe_sl_status=get_order_status(pe_sl_orderid)

if ce_sl_status=='pending':
    cancel_order(ce_sl_orderid)
    marketorder_buy(ce_symbol,lots*25)
    
if pe_sl_status=='pending':
    cancel_order(pe_sl_orderid)
    marketorder_buy(pe_symbol,lots*25)
```

#### File: `short-strangle/0920_short_strangle/finnifty_0920_short_strangle.py`
```python
#  FIN NIFTY 0920 Short strangle, % based SL

from kiteconnect import KiteConnect
import pandas as pd
import datetime as dt
import time


lots = 1  # quantity
strangle_width = 50  # points away from ATM (FinNifty strikes in 50-point intervals)
ce_stoploss_per = 25
pe_stoploss_per = 25


nse_holidays = [dt.date(2023, 7, 21), dt.date(2023, 8, 19), dt.date(2023, 9, 10), dt.date(2023, 10, 15), dt.date(2023, 11, 4), dt.date(2023, 11, 5), dt.date(2023, 11, 19)]


api_key = ""
api_secret = ""

access_token = open('C:/downloads/access_token.txt', 'r').read()

open_time = dt.time(hour=9, minute=15)
trade_entry_time = dt.time(hour=9, minute=20)
re_entry_time = dt.time(hour=12, minute=30)
sqf_time = dt.time(hour=15, minute=6)


kite = KiteConnect(api_key=api_key)

kite.set_access_token(access_token)

def get_expiry_date():
    current_date = dt.date.today()
    wd = current_date.weekday()
    x = 0
    if wd <= 3:
        x = (3 - wd)
    else:
        x = 6

    exp_date = current_date + dt.timedelta(days=x)

    if exp_date in nse_holidays:
        exp_date = exp_date - dt.timedelta(days=1)

    if exp_date in nse_holidays:
        exp_date = exp_date - dt.timedelta(days=1)
    return exp_date

def get_finnifty_atm_strike(ltp):
    r = ltp % 50
    if r < 25:
        atm = ltp - r
    else:
        atm = ltp - r + 50
    return int(atm)

def get_trading_symbol(df, strike, CE_or_PE):
    df_1 = df[df.strike == strike]
    ce_name = df_1[df_1.instrument_type == 'CE'].tradingsymbol.values[0]
    pe_name = df_1[df_1.instrument_type == 'PE'].tradingsymbol.values[0]
    if CE_or_PE == 'CE':
        symbol = ce_name
    elif CE_or_PE == 'PE':
        symbol = pe_name
    return symbol

def get_finnifty_ltp():
    a = 0
    while a < 10:
        try:
            bn = kite.ltp('NSE:FINNIFTY')
            bn_ltp = bn['NSE:FINNIFTY']['last_price']
            break
        except:
            print("can't extract LTP data..retrying")
            time.sleep(1)
            a += 1
    return bn_ltp


def marketorder_buy(symbol, quantity):
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def marketorder_sell(symbol, quantity):
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def stoploss_order_buy(symbol, quantity, trig_price):
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_SLM,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR,
                    trigger_price=trig_price)


def get_trade_price(order_id):
    a = 0
    while a < 10:
        try:
            tb_df = pd.DataFrame(kite.trades())
            trade_price = tb_df[tb_df.order_id == order_id].average_price.values[0]
            break
        except:
            print("can't extract order data..retrying")
            time.sleep(1)
            a += 1
    return trade_price

def get_order_status(order_id):
    a = 0
    while a < 10:
        try:
            tb_df = pd.DataFrame(kite.trades())
            break
        except:
            print("can't extract order data..retrying")
            time.sleep(1)
            a += 1

    df = tb_df[tb_df.order_id == order_id]

    if len(df) > 0:
        return 'executed'
    else:
        return 'pending'


def cancel_order(order_id):
    kite.cancel_order(order_id=order_id,
                    variety=kite.VARIETY_REGULAR)

def round_5ps(price):
    r = round(price % .05, 2)
    rp = round(price - r, 2)
    return float(rp)


def calculate_atm_and_place_order():
    global bn_ltp, atm_strike, ce_symbol, pe_symbol, ce_order_id, pe_order_id
    global ce_sell_price, pe_sell_price, ce_sl_orderid, pe_sl_orderid

    bn_ltp = get_finnifty_ltp()

    atm_strike = get_finnifty_atm_strike(bn_ltp)

    # Strangle: sell OTM call above ATM, OTM put below ATM
    ce_symbol = get_trading_symbol(bn_exp_df, atm_strike + strangle_width, 'CE')
    pe_symbol = get_trading_symbol(bn_exp_df, atm_strike - strangle_width, 'PE')
    print(ce_symbol)
    print(pe_symbol)

    ce_order_id = marketorder_sell(ce_symbol, lots * 40)
    pe_order_id = marketorder_sell(pe_symbol, lots * 40)

    ce_sell_price = get_trade_price(ce_order_id)
    pe_sell_price = get_trade_price(pe_order_id)

    ce_stoploss_value = round_5ps(ce_sell_price * ce_stoploss_per / 100)
    pe_stoploss_value = round_5ps(pe_sell_price * pe_stoploss_per / 100)

    ce_sl_orderid = stoploss_order_buy(ce_symbol, lots * 40, float(round_5ps(ce_sell_price + ce_stoploss_value)))
    pe_sl_orderid = stoploss_order_buy(pe_symbol, lots * 40, float(round_5ps(pe_sell_price + pe_stoploss_value)))


# downloading instrument dump
a = 0
while a <= 10:
    try:
        instrument_dump = kite.instruments("NFO")
        break
    except:
        print("can't instrument data..retrying")
        time.sleep(1)
        a += 1

instrument_df = pd.DataFrame(instrument_dump)

expiry_date = get_expiry_date()

bn = instrument_df[instrument_df.name == 'FINNIFTY']
bn_exp_df = bn[bn.expiry == expiry_date]

while dt.datetime.now().time() < trade_entry_time:
    time.sleep(1)

calculate_atm_and_place_order()

while dt.datetime.now().time() < re_entry_time:
    time.sleep(1)

ce_sl_status = get_order_status(ce_sl_orderid)
pe_sl_status = get_order_status(pe_sl_orderid)

if ce_sl_status == 'executed' and pe_sl_status == 'executed':
    calculate_atm_and_place_order()


while dt.datetime.now().time() < sqf_time:
    time.sleep(1)

ce_sl_status = get_order_status(ce_sl_orderid)
pe_sl_status = get_order_status(pe_sl_orderid)

if ce_sl_status == 'pending':
    cancel_order(ce_sl_orderid)
    marketorder_buy(ce_symbol, lots * 40)

if pe_sl_status == 'pending':
    cancel_order(pe_sl_orderid)
    marketorder_buy(pe_symbol, lots * 40)
```

#### File: `short-straddle/0920_short_straddle/finnifty_0920_short_straddle.py`
```python
#  FIN NIFTY 0920 Short straddle, % based SL

from kiteconnect import KiteConnect
import pandas as pd
import datetime as dt
import time


lots=1  # quanity
ce_stoploss_per=25
pe_stoploss_per=25


nse_holidays=[dt.date(2023,7,21),dt.date(2023,8,19),dt.date(2023,9,10),dt.date(2023,10,15),dt.date(2023,11,4),dt.date(2023,11,5),dt.date(2023,11,19)]


api_key = ""
api_secret = ""

access_token=open('C:/downloads/access_token.txt','r').read()

open_time=dt.time(hour=9,minute=15)
trade_entry_time=dt.time(hour=9,minute=20)
re_entry_time=dt.time(hour=12,minute=30)
sqf_time=dt.time(hour=15,minute=6)


kite = KiteConnect(api_key=api_key)

kite.set_access_token(access_token)

def get_expiry_date():
    #this module will not work in sunday or saturday
    current_date=dt.date.today()
    wd=current_date.weekday()
    #print(wd)   # 0 Monday, 6 sunday
    #this module will not work on sunday and saturday
    #calculating value of x ('current date' + 'x' will be next weekly exp day)
    x=0
    if wd<=3:
        x=(3-wd)
    else:
        x=6
    
    exp_date=current_date+dt.timedelta(days=x)
   
    if exp_date in nse_holidays:
        exp_date=exp_date-dt.timedelta(days=1)
        
    if exp_date in nse_holidays:
        exp_date=exp_date-dt.timedelta(days=1)
    return exp_date

def get_banknifty_atm_strike(ltp):
    r=ltp%50
    if r<25:
       atm=ltp-r
    else:
        atm=ltp-r+50
    return int(atm)

def get_trading_symbol(df,strike,CE_or_PE):
    
    df_1=df[df.strike==strike]
    ce_name=df_1[df_1.instrument_type=='CE'].tradingsymbol.values[0]
    pe_name=df_1[df_1.instrument_type=='PE'].tradingsymbol.values[0]
    if CE_or_PE=='CE':
        symbol=ce_name
    elif CE_or_PE=='PE':
        symbol=pe_name
    return symbol
    
def get_banknifty_ltp():
 
    a = 0
    while a < 10:
        try:
            bn=kite.ltp('NSE:FINNIFTY')
            bn_ltp=bn['NSE:FINNIFTY']['last_price']
            break
        except:
            print("can't extract LTP data..retrying")
            time.sleep(1)
            a+=1
    return bn_ltp


def marketorder_buy(symbol,quantity):    
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def marketorder_sell(symbol,quantity):    
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)

def stoploss_order_buy(symbol,quantity,trig_price):    
    return kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NFO,
                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_SLM,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR,
                    trigger_price=trig_price)


def get_trade_price(order_id):
    a=0
    while a < 10:
        try:
            tb_df=pd.DataFrame(kite.trades())
            trade_price=tb_df[tb_df.order_id==order_id].average_price.values[0]
            break
        except:
            print("can't extract oreder data..retrying")
            time.sleep(1)
            a+=1
    return trade_price

def get_order_status(order_id):
    a=0
    while a < 10:
        try:
            tb_df=pd.DataFrame(kite.trades())
            break
        except:
            print("can't extract oreder data..retrying")
            time.sleep(1)
            a+=1

    df=tb_df[tb_df.order_id==order_id]
    
    if len(df)>0:
        return 'executed'
    else:
        return 'pending'



def cancel_order(order_id):    
    kite.cancel_order(order_id=order_id,
                    variety=kite.VARIETY_REGULAR)
def round_5ps(price):
    r=round(price%.05,2)
    rp=round(price-r,2)
    return float(rp) 


def calculate_atm_and_place_order():
    global bn_ltp, atm_strike, ce_symbol, pe_symbol, ce_order_id, pe_order_id
    global ce_sell_price, pe_sell_price, ce_sl_orderid, pe_sl_orderid
#######################################################################
     
    bn_ltp=get_banknifty_ltp()
    
    atm_strike=get_banknifty_atm_strike(bn_ltp)
    
    ce_symbol=get_trading_symbol(bn_exp_df, atm_strike,'CE')
    
    pe_symbol=get_trading_symbol(bn_exp_df, atm_strike,'PE')
    print(ce_symbol)
    print(pe_symbol)
    
    ce_order_id=marketorder_sell(ce_symbol, lots*40)
    
    pe_order_id=marketorder_sell(pe_symbol, lots*40)
    
    ce_sell_price=get_trade_price(ce_order_id)
    pe_sell_price=get_trade_price(pe_order_id)
   
   
    ce_stoploss_value=round_5ps(ce_sell_price*ce_stoploss_per/100)
    pe_stoploss_value=round_5ps(pe_sell_price*pe_stoploss_per/100)
    
    ce_sl_orderid=stoploss_order_buy(ce_symbol, lots*40,float(round_5ps(ce_sell_price+ce_stoploss_value)))
    pe_sl_orderid=stoploss_order_buy(pe_symbol, lots*40,float(round_5ps(pe_sell_price+pe_stoploss_value)))

#######################################################



#downloading instrument dump 
a=0
while a<=10:
    try:
        instrument_dump = kite.instruments("NFO")
        break
    except:
        print("can't instrument data..retrying")
        time.sleep(1)
        a+=1

instrument_df = pd.DataFrame(instrument_dump)

expiry_date=get_expiry_date()

bn=instrument_df[instrument_df.name=='FINNIFTY']
bn_exp_df=bn[bn.expiry==expiry_date]

while dt.datetime.now().time()<trade_entry_time:
    time.sleep(1)
###############################

calculate_atm_and_place_order()

###############################

while dt.datetime.now().time()<re_entry_time:
    time.sleep(1)

ce_sl_status=get_order_status(ce_sl_orderid)
pe_sl_status=get_order_status(pe_sl_orderid)

if ce_sl_status=='executed' and pe_sl_status=='executed':
    calculate_atm_and_place_order()


while dt.datetime.now().time()<sqf_time:
    time.sleep(1)

ce_sl_status=get_order_status(ce_sl_orderid)
pe_sl_status=get_order_status(pe_sl_orderid)

if ce_sl_status=='pending':
    cancel_order(ce_sl_orderid)
    marketorder_buy(ce_symbol,lots*40)
    
if pe_sl_status=='pending':
    cancel_order(pe_sl_orderid)
    marketorder_buy(pe_symbol,lots*40)
```


==================================================
