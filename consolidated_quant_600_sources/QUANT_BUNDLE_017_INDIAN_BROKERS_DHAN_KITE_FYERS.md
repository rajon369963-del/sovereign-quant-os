# ⚡ [QUANT-SOURCE-017] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_017_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: DhaneyBot (`WHEEL_DhaneyBot`)
- **Full Name**: `DhaneyBot`
- **Description**: DhaneyBot is a premium, fully autonomous algorithmic trading system designed for the Indian Stock Market (NSE). It scans markets for opportunities, scores candidates using multi-signal quantitative metrics, uses an AI Council of Five investor personas to critique and vote on candidate setups, and executes orders automatically via the Dhan API.
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# DhaneyBot — Autonomous AI Trading Agent v4

DhaneyBot is a premium, fully autonomous algorithmic trading system designed for the Indian Stock Market (NSE). It scans markets for opportunities, scores candidates using multi-signal quantitative metrics, uses an AI Council of Five investor personas (Buffett, Simons, Tudor Jones, Lynch, and Soros) to critique and vote on candidate setups, and executes orders automatically via the Dhan API.

The platform is designed to run 24/7 as a Windows Service, featuring a dynamic regime-based capital allocator, strict multi-layered risk management, SQLite-backed ledger tracking, feedback-driven reinforcement learning, and a real-time web dashboard with an interactive AI chat interface.

---

## Core Capabilities

- **Regime-Aware Capital Allocation**: Detects current market regimes (BULL / NEUTRAL / BEAR / CRASH) based on broad-market indices (NIFTY 50 trend, RSI, India VIX) and dynamically redistributes cash reserves across three separate asset tiers.
- **Three-Tier Universe Strategy**:
  - **Tier 1 (Momentum Smallcaps)**: Scans NSE momentum gainers in the Rs 20–Rs 250 price corridor.
  - **Tier 2 (Growth Midcaps)**: Trades liquid midcaps in the Rs 250–Rs 1,500 price corridor.
  - **Tier 3 (Blue Chips & ETFs)**: Trades liquid large caps and sectors/ETFs (NIFTYBEES, ITBEES, GOLDBEES) for defensive hedging.
- **Council of Five AI Vetting**: Evaluates trade entries by simulating five legendary investment styles. Supported modes include:
  - `dual`: Computes local rules, queries OpenRouter models (e.g., Gemini 2.5 Flash), and compares outcomes.
  - `local`: Offline, deterministic rules using structural technical and trend inputs.
  - `openrouter`: Full LLM voting engine with API-driven reasoning.
- **Opening Range Breakout (ORB) Strategy**: A specialized intraday breakout model that monitors early-morning price candles (9:15–9:45 IST) and executes long breakouts with strict technical confirmations (VWAP, ATR expansion, volume triggers, and EMA filters).
- **SQLite Ledger & Performance Learning**:
  - Records every trade event, side, quantity, price, P&L, strategy, and execution reasoning into a local database (`trade_log.sqlite3`).
  - Implements a feedback loop via `LearningEngine` to track performance metrics by ticker and strategy, dynamically raising/lowering AI conviction voting thresholds.
- **Premium Live Dashboard**:
  - Serves real-time positions, system status, cash reserves, equity curves, win rates, and drawdowns.
  - Features an interactive chat panel connected to a lightweight server (`chat_server.py`) to query portfolio statistics, audit trading decisions, or manually queue buy/sell override commands.
- **Automated Windows Services**: Configured with NSSM to start automatically at PC boot without requiring a user login.

---

## File Structure & Modules

```
DhaneyBot/
├── agent/
│   ├── trader_v4.py          # Compatibility launcher / Entry point
│   ├── bot.py                # Main orchestration loop (scans, scores, calls council, executes)
│   ├── alpha.py              # Scanners, 8-signal alpha scoring, and fundamental quality filters
│   ├── regime.py             # Market regime detection engine (Nifty SMA, RSI, VIX levels)
│   ├── council.py            # AI council simulation and multi-mind voting logic
│   ├── orb.py                # Intraday Opening Range Breakout (ORB) strategy implementation
│   ├── risk.py               # RiskManager (safeguards), AlertManager, LearningEngine, and TradeLedger
│   ├── execution.py          # Live execution client (Dhan API wrapper) & SimExecutor (paper simulator)
│   ├── scheduler.py          # Market-hours time scheduler (IST-based)
│   ├── reporting.py          # Performance tracker & live dashboard signal exporter
│   ├── models.py             # Shared data models (Portfolio, Position, ScoredStock, StockSignal)
│   ├── settings.py           # Configuration parser, logging handler, and universes
│   ├── market_data.py        # TradingView scanner helper methods and symbol normalization
│   └── watchdog_ntfy.py      # Health watchdog that monitors the agent and sends push notifications
├── dashboard/
│   └── dashboard_v6.html     # Premium live trading dashboard template v6
├── services/
│   └── install_service_nssm.py # Windows Service installer utility using NSSM
├── scripts/
│   ├── save_password.py      # Secure credential utility
│   └── test_email.py         # SMTP email notifications test utility
├── docs/
│   └── SYSTEM_OVERVIEW.html  # In-depth system documentation and visual workflows
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies manifest
├── symbol_map.json           # Map of NSE ticker symbols to Dhan security IDs
└── README.md                 # System overview and usage guide (this file)
```

---

## Setup & Installation

### Requirements
- Python 3.10+
- Windows 10/11 (for service daemons)
- Dhan Trading Account (Client ID and API Access Token)
- [OpenRouter API Key](https://openrouter.ai)
- [ntfy app](https://ntfy.sh) installed on your phone (for mobile notifications)
- [NSSM](https://nssm.cc/download) (Win64 build, place `nssm.exe` in the root folder)

### 1. Install Dependencies
```cmd
py -3.11 -m pip install -r requirements.txt
```

### 2. Configure Environment
Rename `.env.example` to `.env` and configure the following variables:
```ini
# --- Broker Configuration ---
DHAN_CLIENT_ID=your_client_id
DHAN_ACCESS_TOKEN=your_access_token
BROKER_PAPER=true               # Set to true for paper testing, false for live trading
EXECUTION_MODE=broker           # broker (executes orders) or signals_only (exports JSON only)
PAPER_SIGNAL_FILE=paper_signals.json

# --- AI & LLM Settings ---
COUNCIL_MODE=dual               # dual (compares local + remote), local, or openrouter
OPENROUTER_API_KEY=your_key
OPENROUTER_MODEL=nvidia/nemotron-3-super-120b-a12b:free
CHAT_OPENROUTER_MODEL=nvidia/nemotron-3-super-120b-a12b:free

# --- Risk Parameters ---
MAX_DAILY_LOSS=8000             # Max loss in Rs before halting trades for the day
WEEKLY_DRAWDOWN_LIMIT=0.10      # Max 10% drawdown from peak weekly equity
MAX_CONSECUTIVE_LOSSES=3        # Cooldown trigger on consecutive losses
LOSS_COOLDOWN_MINUTES=20        # Length of cooldown period

# --- Notifications ---
NTFY_TOPIC=your-unique-topic-name
TELEGRAM_BOT_TOKEN=             # Optional
TELEGRAM_CHAT_ID=               # Optional
```

### 3. Initialize Symbol Map
Dhan requires order placements to use numerical `security_id` mappings instead of raw symbols. Create or update `symbol_map.json` in the root folder containing the securities you plan to trade:
```json
{
  "RELIANCE": "2885",
  "TCS": "11536",
  "INFY": "1594",
  "NIFTYBEES": "10576",
  "GOLDBEES": "14451"
}
```

---

## Intelligent Scheduling (IST)

The agent operates in accordance with National Stock Exchange of India (NSE) market hours:

| Session | Time Range (IST) | Cycle Interval | AI Council Vetting |
|---|---|---|---|
| **Weekend** | Saturday – Sunday | Sleep | No |
| **Pre-Market** | 9:00 AM – 9:15 AM | Runs once | No |
| **Power Open** | 9:15 AM – 10:45 AM | Every 5 mins | Yes |
| **Mid-Session** | 10:45 AM – 3:00 PM | Every 15 mins | Yes |
| **Power Close** | 3:00 PM – 3:30 PM | Every 5 mins | Yes |
| **After Hours** | 3:30 PM+ | Sleep | No |

---

## Risk Management & Rules

DhaneyBot features a multi-tiered safety system to protect capital:
- **Intraday Limits**: If daily realized losses exceed `MAX_DAILY_LOSS` or the system encounters `MAX_CONSECUTIVE_LOSSES`, trading is halted.
- **Drawdown Guards**: A weekly drawdown of `WEEKLY_DRAWDOWN_LIMIT` (default 10%) from peak weekly equity halts all new entries.
- **Re-Entry Protection**: Ticker-specific loss exits activate a cooldown (default 1 day), blocking immediate re-entries on that ticker.
- **Dynamic Sizing**: Automatically adjusts position size percentages depending on the account's total wallet size.
- **Multi-Stage Exit Policies**:
  - **Hard Stop-Loss**: Triggered if the stock falls past its tier threshold (e.g. T1 -8%, T2 -3.5%, T3 -2.5%).
  - **Fast-Loss Exit**: Evaluates trend health. Exit triggers if a position loses more than 1.5% and the trend is weakening.
  - **Max Losing Hold Days**: Exits losing positions held longer than 1 day to free up capital.
  - **Trailing Stop**: Locks in gains when a stock reverses from its peak price.

---

## Running the Platform

### Option A: Manual Terminal Execution
1. **Launch the Agent Loop**:
   ```cmd
   py -3.11 agent/trader_v4.py
   ```
2. **Launch the Chat & Static Server**:
   ```cmd
   py -3.11 chat_server.py
   ```
3. **Open the Dashboard**:
   Open `dashboard/dashboard_v6.html` or navigate to `http://localhost:3000` in your browser.

### Option B: Running as Windows Services (Recommended)
```cmd
py -3.11 services/install_service_nssm.py install
```

---

## Interactive AI Chat Panel

The live dashboard's prompt section allows you to interact directly with the agent. You can:
- **Query Status**: Type `portfolio` or `status` for a formatted breakdown of holdings, P&L, win rates, and current market regime.
- **Ask AI Questions**: Ask open-ended questions like `"Why did we buy RELIANCE?"` or `"Should I sell TCS?"`.
- **Manual Overrides**:
  - Buy orders: Type `buy 10 TCS` or `buy RELIANCE`.
  - Sell orders: Type `sell TCS` or `sell 5 INFY`.

---

## Disclaimer
This system is an autonomous AI trading agent. Algorithmic trading involves substantial financial risk. Start with a mock/paper trading account (`BROKER_PAPER=true`) for at least 2–4 weeks before committing real capital.

### Core Implementation Code & Architecture
#### File: `agent/__init__.py`
```python

```

#### File: `symbol_map.json`
```python
{
  "RELIANCE": "2885",
  "TCS": "11536",
  "INFY": "1594",
  "HDFCBANK": "1333"
}
```

#### File: `agent/trader_v4.py`
```python
#!/usr/bin/env python3
"""Compatibility launcher for the modular DhaneyBot trading agent."""

try:
    from .bot import DhaneyBot, check, startup_prompt
except ImportError:
    from bot import DhaneyBot, check, startup_prompt


def main():
    check()
    run_mode, budget = startup_prompt()
    DhaneyBot(budget=budget, run_mode=run_mode).run()


if __name__ == "__main__":
    main()
```

#### File: `scripts/save_password.py`
```python
"""
DHANEYBOT — Secure Password Setup
===================================
Run this ONCE to securely store your Outlook password
in Windows Credential Manager (the same encrypted vault
your browser uses to save passwords).

After running this, your password never appears in any file.
The watchdog reads it securely from Windows at runtime.

HOW TO RUN:
  python save_password.py
"""

import sys

def save_password():
    try:
        import keyring
    except ImportError:
        print("Installing keyring (secure password storage)...")
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "keyring"], check=True)
        import keyring

    print()
    print("=" * 54)
    print("  DHANEYBOT — Secure Password Setup")
    print("=" * 54)
    print()
    print("  This stores your Outlook password securely")
    print("  in Windows Credential Manager.")
    print("  It will NOT be saved in any file.")
    print()

    import getpass
    print("  Email: jitreddy@toughtechies.com")
    print()
    password = getpass.getpass("  Enter your Outlook password (hidden): ")

    if not password:
        print("\n  No password entered. Exiting.")
        return

    # Confirm
    confirm = getpass.getpass("  Confirm password (hidden): ")
    if password != confirm:
        print("\n  Passwords do not match. Run again.")
        return

    # Save to Windows Credential Manager
    keyring.set_password(
        "DhaneyBotOutlook",           # service name
        "jitreddy@toughtechies.com", # username
        password
    )

    print()
    print("  Password saved securely to Windows Credential Manager.")
    print()
    print("  To verify it saved correctly, run:")
    print("    python save_password.py verify")
    print()
    print("  You can now run the watchdog safely.")
    print("  Your password is NOT stored in any file.")
    print("=" * 54)
    print()


def verify_password():
    try:
        import keyring
    except ImportError:
        print("keyring not installed. Run: python save_password.py")
        return

    pw = keyring.get_password("DhaneyBotOutlook", "jitreddy@toughtechies.com")
    if pw:
        print()
        print("  Password found in Windows Credential Manager.")
        print(f"  Length: {len(pw)} characters")
        print(f"  Starts with: {pw[0]}{'*' * (len(pw)-2)}{pw[-1]}")
        print("  Watchdog will use this automatically.")
        print()
    else:
        print()
        print("  No password found. Run: python save_password.py")
        print()


def delete_password():
    try:
        import keyring
        keyring.delete_password("DhaneyBotOutlook", "jitreddy@toughtechies.com")
        print("  Password removed from Windows Credential Manager.")
    except Exception as e:
        print(f"  Error: {e}")


if __name__ == "__main__":
    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "save"
    if cmd == "verify":
        verify_password()
    elif cmd == "delete":
        delete_password()
    else:
        save_password()
```

#### File: `agent/scheduler.py`
```python
import datetime
from typing import Tuple

try:
    from .settings import CONFIG, IST
except ImportError:
    from settings import CONFIG, IST

class SmartScheduler:

    MARKET_OPEN  = (9, 15)   # IST
    MARKET_CLOSE = (15, 30)  # IST
    PRE_MARKET   = (9,  0)   # IST

    def __init__(self):
        self._last_pre = None

    def _now(self):
        n = datetime.datetime.now(IST)
        return n.weekday(), n.hour*60+n.minute, n

    def is_weekend(self):
        d,_,_ = self._now()
        return d >= 5

    def is_market_open(self):
        d,m,_ = self._now()
        o = self.MARKET_OPEN[0]*60+self.MARKET_OPEN[1]
        c = self.MARKET_CLOSE[0]*60+self.MARKET_CLOSE[1]
        return 0<=d<=4 and o<=m<c

    def is_premarket(self):
        d,m,_ = self._now()
        p = self.PRE_MARKET[0]*60+self.PRE_MARKET[1]
        o = self.MARKET_OPEN[0]*60+self.MARKET_OPEN[1]
        return 0<=d<=4 and p<=m<o

    def is_power_open(self):
        d,m,_ = self._now()
        o = self.MARKET_OPEN[0]*60+self.MARKET_OPEN[1]
        return 0<=d<=4 and o<=m<o+90

    def is_power_close(self):
        d,m,_ = self._now()
        c = self.MARKET_CLOSE[0]*60+self.MARKET_CLOSE[1]
        return 0<=d<=4 and c-30<=m<c

    def next_interval(self) -> Tuple[int, str, bool]:
        """Returns (sleep_secs, label, should_call_claude)"""
        if self.is_weekend():
            return self._secs_to_monday(), "Weekend â€” sleeping until Mon pre-market", False
        if self.is_premarket():
            today = datetime.datetime.now(IST).date()
            if self._last_pre != today:
                self._last_pre = today
                return 0, "Pre-market scan (no Claude)", False
            return self._secs_to_open(), "Waiting for market open", False
        if self.is_power_open():
            return CONFIG["power_open_interval"],  "Power open  â€” 5 min cycles", True
        if self.is_power_close():
            return CONFIG["power_close_interval"], "Power close â€” 5 min cycles", True
        if self.is_market_open():
            return CONFIG["mid_session_interval"], "Mid-session â€” 15 min cycles", True
        return self._secs_to_premarket(), "After hours â€” sleeping", False

    def _secs_to_open(self):
        n = datetime.datetime.now(IST)
        t = n.replace(hour=self.MARKET_OPEN[0], minute=self.MARKET_OPEN[1], second=0, microsecond=0)
        if n >= t: t += datetime.timedelta(days=1)
        return max(60, int((t-n).total_seconds()))

    def _secs_to_premarket(self):
        n = datetime.datetime.now(IST)
        t = n.replace(hour=self.PRE_MARKET[0], minute=self.PRE_MARKET[1], second=0, microsecond=0)
        if n >= t: t += datetime.timedelta(days=1)
        while t.weekday() >= 5: t += datetime.timedelta(days=1)
        return max(60, int((t-n).total_seconds()))

    def _secs_to_monday(self):
        n = datetime.datetime.now(IST)
        days = (7-n.weekday()) % 7 or 7
        t = (n + datetime.timedelta(days=days)).replace(
            hour=self.PRE_MARKET[0], minute=self.PRE_MARKET[1], second=0, microsecond=0)
        return max(60, int((t-n).total_seconds()))

    def status(self) -> str:
        ist = datetime.datetime.now(IST)
        ts   = ist.strftime("%a %d %b %H:%M IST")
        if self.is_weekend():     return f"{ts} â€” Weekend"
        if self.is_power_open():  return f"{ts} â€” POWER OPEN (5-min)"
        if self.is_power_close(): return f"{ts} â€” POWER CLOSE (5-min)"
        if self.is_market_open(): return f"{ts} â€” Market open (15-min)"
        if self.is_premarket():   return f"{ts} â€” Pre-market"
        return f"{ts} â€” After hours"
```

#### File: `agent/models.py`
```python
from dataclasses import dataclass, field
from typing import Dict, List

try:
    from .settings import CONFIG
except ImportError:
    from settings import CONFIG

@dataclass
class MarketRegime:
    state: str          # BULL / NEUTRAL / BEAR / CRASH
    score: float        # 0â€“1 composite score
    spy_trend: str      # uptrend / downtrend / sideways
    spy_rsi: float
    vix_level: str      # low / elevated / high / extreme
    breadth: float      # % stocks above 50-day MA (0â€“1)
    momentum: float     # NIFTY 20-day return
    allocation: Dict[str, float]
    reasoning: str

@dataclass
class StockSignal:
    ticker: str
    tier: int           # 1, 2, or 3
    action: str         # BUY / SELL / HOLD
    consensus: float
    price: float
    qty: int
    value_usd: float
    stop_loss: float
    take_profit: float
    trail_stop: float
    strategy: str
    reasoning: str
    alpha_score: float
    fundamental_quality: str = "DATA_UNAVAILABLE"
    data_confidence: str = "VERY_LOW"
    target_1: float = 0.0
    hard_exit_time: str = ""

@dataclass
class Position:
    ticker: str
    tier: int
    qty: int
    avg_cost: float
    current_price: float
    market_value: float
    unrealized_pnl: float
    peak_price: float
    buy_date: str = ""
    strategy: str = ""
    stop_loss: float = 0.0
    take_profit: float = 0.0
    target_1: float = 0.0
    hard_exit_time: str = ""
    t1_hit: bool = False

@dataclass
class FundamentalView:
    valuation: str
    growth: str
    health: str
    returns: str
    ownership: str
    overall_quality: str
    data_confidence: str
    score: float
    sources: Dict[str, str] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)

@dataclass
class Portfolio:
    total_usd: float
    cash_usd: float
    invested_usd: float
    positions: Dict[str, Position]
    open_count: int
    # Tier breakdowns
    tier1_value: float = 0.0
    tier2_value: float = 0.0
    tier3_value: float = 0.0
    initial_budget: float = 0.0

    @property
    def deployable_cash(self) -> float:
        """Cash available to deploy — keeps min_cash_reserve and separate profits."""
        separated_profit = 0.0
        if self.initial_budget > 0:
            separated_profit = max(0.0, self.total_usd - self.initial_budget)
        
        effective_total = min(self.total_usd, self.initial_budget) if self.initial_budget > 0 else self.total_usd
        effective_cash = self.cash_usd - separated_profit
        
        reserve = effective_total * CONFIG["min_cash_reserve"]
        return max(0.0, effective_cash - reserve)

    def tier_capacity(self, tier: int, regime: MarketRegime) -> float:
        """How much more USD can go into this tier given regime allocations."""
        alloc = regime.allocation.get(f"tier{tier}", 0)
        effective_total = min(self.total_usd, self.initial_budget) if self.initial_budget > 0 else self.total_usd
        target = effective_total * alloc
        current = getattr(self, f"tier{tier}_value", 0)
        return max(0, target - current)

@dataclass
class ScoredStock:
    ticker: str
    tier: int
    price: float
    alpha_score: float
    rsi: float
    macd_signal: str
    trend: str
    rel_volume: float
    volume: int
    change_1d: float
    change_5d: float
    gap_pct: float
    squeeze_score: float
    bb_squeeze: bool
    near_52w_high: bool
    has_news: bool
    news_headlines: List[str]
    short_pct: float
    market_cap: float
    sector: str
    pe_ratio: float
    dividend_yield: float
    price_to_book: float
    debt_to_equity: float
    current_ratio: float
    roe: float
    revenue_growth: float
    earnings_growth: float
    fundamental: FundamentalView
    strategy_setup: str = ""
    strategy_direction: str = ""
    strategy_stop_loss: float = 0.0
    strategy_target_1: float = 0.0
    strategy_take_profit: float = 0.0
    strategy_hard_exit_time: str = ""
    strategy_notes: str = ""
    history_pattern: str = "unknown"
    recovery_score: float = 0.0
    downtrend_risk: float = 1.0
```


==================================================


## [2/3] Repository: Jiraiya (`WHEEL_Jiraiya`)
- **Full Name**: `Jiraiya`
- **Description**: Backtesting and strategy-research workspace for NSE trading ideas using Streamlit, Yahoo Finance, Dhan, and Kite data. Use your Own API
- **GitHub Stars**: 4
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Jiraiya AI BackTester

Jiraiya AI BackTester is a trading research project for building, testing, and presenting automated NSE-market trading workflows.

## About

Jiraiya AI BackTester is a backtesting and strategy-research workspace for experimenting with NSE trading ideas before any real-world deployment. It combines a Streamlit Strategy Lab, historical market-data connectors, configurable strategy rules, and a static product presentation.

The project is designed to help users compare strategy behavior across different symbols, timeframes, and data sources. It is intentionally focused on research and backtesting, not live order execution.

The repository currently includes:

- A static investor/product presentation in `index.html`
- A Streamlit Strategy Lab in `trading_web/`
- Historical-data support through Yahoo Finance, with optional Dhan and Kite data connectors
- A safe backtesting workflow for testing strategies before any live trading work

> Important: This project is not financial advice. Trading involves risk. Backtest results, paper-trading results, and presentation claims do not guarantee future profit.

## Current Status

This repo is currently a **research, presentation, and backtesting repo**.

It does **not** currently include a production live-order execution engine inside this GitHub repository. The Streamlit app is intentionally backtest-focused and does not place live orders.

## Repository Structure

```text
.
+-- index.html
+-- README.md
+-- requirements.txt
+-- .env.example
+-- trading_web/
|   +-- app.py
|   +-- assets/
|   |   +-- psy_bg.png
|   |   `-- styles.css
|   `-- components/
|       +-- broker_data.py
|       +-- chart.py
|       +-- data.py
|       +-- layout.py
|       `-- strategy.py
```

## What Each Part Does

### `index.html`

A static presentation page for the Jiraiya AI BackTester concept. It describes the larger product vision, including:

- Automated NSE F&O trading workflows
- Dhan API integration concept
- Risk-management design
- Paper-trading validation
- Launch-readiness checklist
- System architecture overview

Open it directly in a browser or host it with GitHub Pages.

### `trading_web/`

A Streamlit Strategy Lab for researching and backtesting strategy rules.

It supports:

- Symbol input
- Yahoo Finance, Dhan, or Kite as data-source options
- Intraday and daily modes
- Candlestick charts
- Strategy-generated buy/sell markers
- Backtest metrics
- Trade table export as CSV

Included strategies:

- Moving Average Crossover
- RSI Reversion
- Breakout

## Run Locally

Clone the repo:

```bash
git clone https://github.com/Marketing-Studios/Jiraiya.git
cd Jiraiya
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Strategy Lab:

```bash
streamlit run trading_web/app.py
```

## Quick Windows Commands

PowerShell:

```powershell
Set-Location "D:\work\Jiraiya"
python -m pip install -r requirements.txt
streamlit run trading_web/app.py
```

## Default Data Source

The app works out of the box with Yahoo Finance.

Example symbols:

```text
RELIANCE.NS
TCS.NS
INFY.NS
```

Yahoo Finance is useful for quick research, but broker data should be used before serious paper-trading validation.

## Optional Broker Data Setup

Broker credentials are optional and should only be stored locally.

Create a local `.env` file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Then fill the provider you want.

### Dhan

```text
DHAN_CLIENT_ID=your_client_id
DHAN_TOKEN=your_access_token
DHAN_SECURITY_ID=your_security_id
DHAN_EXCHANGE_SEGMENT=NSE_EQ
DHAN_INSTRUMENT_TYPE=EQUITY
```

### Kite / Zerodha

```text
KITE_API_KEY=your_api_key
KITE_ACCESS_TOKEN=your_access_token
KITE_EXCHANGE=NSE
```

Never commit `.env` or real credentials.

## Strategy Lab Workflow

1. Choose a data source.
2. Enter a symbol.
3. Select intraday or daily data.
4. Choose a strategy.
5. Tune strategy parameters.
6. Set capital, quantity, and brokerage.
7. Click **Run Backtest**.
8. Review chart markers, P&L, return, win rate, drawdown, and trades.

The app is designed for research first. A strategy should be tested across multiple symbols, periods, and market regimes before it is trusted.

## What This Repo Does Not Do Yet

The current Streamlit app does not:

- Place live orders
- Manage live broker positions
- Run automated live trading
- Guarantee profitable signals
- Store real account credentials
- Replace broker-side risk controls

Live order placement should only be added after tests, paper trading, risk limits, and manual override flows are complete.

## Safety Rules

Before any live-trading feature is added:

- Keep real credentials out of Git.
- Use `.env` locally and `.env.example` publicly.
- Use paper trading first.
- Add tests for every risk rule.
- Keep manual broker access ready.
- Start with the smallest possible size.
- Verify stop-loss, target, and exit behavior independently.
- Assume APIs, internet, and local machines can fail.

The `.gitignore` is configured to ignore common secret files such as:

```text
.env
*.key
*.pem
credentials.json
.streamlit/secrets.toml
```

## GitHub Pages

The static presentation can be hosted using GitHub Pages:

```text
Settings -> Pages -> Deploy from a branch
Branch: main
Folder: /root
```

Expected URL format:

```text
https://marketing-studios.github.io/Jiraiya/
```

## Roadmap

Planned improvements:

1. Add more strategy templates.
2. Add proper paper-trading state.
3. Add tests for all strategy calculations.
4. Add Dhan/Kite historical-data examples.
5. Add dashboard screenshots.
6. Add a trade journal.
7. Add portfolio-level backtesting.
8. Add risk-control simulation.
9. Add broker execution only after paper-trading validation is complete.

## License

This project is released under the MIT License.

That means the code can be used, copied, modified, and shared freely, as long as the license notice is included. The software is provided without warranty.

See [LICENSE](LICENSE) for details.

## Disclaimer And Liability

This project is for **education, research, historical-data analysis, backtesting, and product presentation only**.

It is **not** a live-trading system, not financial advice, not investment advice, and not a recommendation to buy, sell, hold, or trade any instrument.

Backtesting has serious limitations:

- Backtest results are not guaranteed.
- Backtest results are not 100% accurate.
- Historical performance does not guarantee future performance.
- Data may be delayed, incomplete, adjusted, missing, or incorrect.
- Broker data, Yahoo Finance data, Dhan data, Kite data, and local calculations can all contain errors.
- Strategy outputs, chart signals, P&L, win rate, drawdown, and trade tables are only research outputs.
- Slippage, brokerage, taxes, liquidity, spread, order rejection, latency, outages, and real market execution may differ from backtest assumptions.

Marketing Studios, the repository owner, and contributors are **not responsible** for:

- trading losses
- financial decisions
- incorrect backtest outputs
- inaccurate signals
- software bugs
- data-provider errors
- broker/API failures
- missed trades
- unexpected trades
- misuse of this project
- any direct or indirect damages caused by using this repository

Use this project at your own risk. Always verify results independently before making any financial decision. Options trading and leveraged trading can lead to significant losses, including loss of capital.

### Core Implementation Code & Architecture
#### File: `trading_web/components/layout.py`
```python
# components/layout.py
import streamlit as st
import pandas as pd

def top_metrics(df: pd.DataFrame):
    st.markdown("#### Overview")
    col1, col2 = st.columns(2)
    last_px = float(df["Close"].iloc[-1]) if not df.empty else 0.0
    st.metric("Last Price", f"{last_px:,.2f}")
    with col1:
        st.metric("P&L Today", "₹0", delta="+0.0%")
    with col2:
        st.metric("Positions", "0")

def right_controls():
    st.markdown("#### Controls")
    st.checkbox("Show signals", value=True)
    st.checkbox("Show volume", value=False)
    st.selectbox("Theme", ["Light", "Dark"], index=0)
    st.button("Reset zoom")

def bottom_log():
    st.markdown("---")
    st.markdown("##### Activity")
    logs = st.session_state.get("logs", [])
    if logs:
        st.code("\n".join(logs[-10:]), language="text")
    else:
        st.caption("No recent activity.")
```

#### File: `trading_web/components/data.py`
```python
# components/data.py
from datetime import datetime, timedelta, timezone
import numpy as np
import pandas as pd
import yfinance as yf

SUPPORTED_INTRADAY = ["1m", "2m", "5m", "15m"]

def list_supported_intervals():
    return SUPPORTED_INTRADAY

def _clean(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return df
    df = df.replace([np.inf, -np.inf], np.nan).dropna()
    for c in ["Open", "High", "Low", "Close"]:
        if c in df:
            df = df[df[c] > 0]
    return df

def fetch_intraday(sym: str, ivl: str, days: int) -> pd.DataFrame:
    end_dt = datetime.now(timezone.utc)
    start_dt = end_dt - timedelta(days=days)
    df = yf.Ticker(sym).history(
        start=start_dt, end=end_dt, interval=ivl,
        auto_adjust=False, actions=False
    )
    return _clean(df)

def fetch_daily(sym: str, period: str) -> pd.DataFrame:
    df = yf.Ticker(sym).history(
        period=period, interval="1d",
        auto_adjust=False, actions=False
    )
    return _clean(df)
```

#### File: `trading_web/components/chart.py`
```python
# components/chart.py
import numpy as np
import plotly.graph_objects as go
import pandas as pd

def _fake_signals(df: pd.DataFrame):
    # Simple demo signals: green every 12th bar, red 6 bars after
    n = len(df.index)
    buys = list(range(3, n, 12))
    sells = list(range(9, n, 12))
    return buys, sells

def make_candles_with_signals(df: pd.DataFrame, title: str = ""):
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df["Open"], high=df["High"],
        low=df["Low"], close=df["Close"]
    )])
    buys, sells = _fake_signals(df)
    if buys:
        fig.add_scatter(
            x=df.index[buys], y=df["Low"].iloc[buys],
            mode="markers", marker=dict(color="green", size=8),
            name="Buy"
        )
    if sells:
        fig.add_scatter(
            x=df.index[sells], y=df["High"].iloc[sells],
            mode="markers", marker=dict(color="red", size=8),
            name="Sell"
        )
    fig.update_layout(
        title=title,
        height=520,
        xaxis_rangeslider_visible=False,
        margin=dict(l=10, r=10, t=40, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig
```

#### File: `trading_web/components/strategy.py`
```python
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class BacktestResult:
    frame: pd.DataFrame
    trades: pd.DataFrame
    metrics: dict


def build_signals(df: pd.DataFrame, strategy: str, params: dict) -> pd.DataFrame:
    out = df.copy()
    out["signal"] = 0
    out["strategy_note"] = ""
    close = out["Close"].astype(float)

    if strategy == "Moving Average Crossover":
        short_window = int(params.get("short_window", 9))
        long_window = int(params.get("long_window", 21))
        short_ma = close.rolling(short_window).mean()
        long_ma = close.rolling(long_window).mean()
        prev_short = short_ma.shift(1)
        prev_long = long_ma.shift(1)
        out["short_ma"] = short_ma
        out["long_ma"] = long_ma
        out.loc[(short_ma > long_ma) & (prev_short <= prev_long), "signal"] = 1
        out.loc[(short_ma < long_ma) & (prev_short >= prev_long), "signal"] = -1
        out["strategy_note"] = f"MA {short_window}/{long_window}"

    elif strategy == "RSI Reversion":
        period = int(params.get("rsi_period", 14))
        lower = float(params.get("rsi_lower", 30))
        upper = float(params.get("rsi_upper", 70))
        rsi = _rsi(close, period)
        out["rsi"] = rsi
        out.loc[(rsi > lower) & (rsi.shift(1) <= lower), "signal"] = 1
        out.loc[(rsi < upper) & (rsi.shift(1) >= upper), "signal"] = -1
        out["strategy_note"] = f"RSI {period} lower={lower:g} upper={upper:g}"

    elif strategy == "Breakout":
        lookback = int(params.get("breakout_lookback", 20))
        prior_high = out["High"].rolling(lookback).max().shift(1)
        prior_low = out["Low"].rolling(lookback).min().shift(1)
        out["breakout_high"] = prior_high
        out["breakout_low"] = prior_low
        out.loc[close > prior_high, "signal"] = 1
        out.loc[close < prior_low, "signal"] = -1
        out["strategy_note"] = f"Breakout {lookback}"

    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    return out


def run_backtest(
    df: pd.DataFrame,
    strategy: str,
    params: dict,
    capital: float,
    quantity: int,
    brokerage_per_trade: float,
) -> BacktestResult:
    signals = build_signals(df, strategy, params)
    trades = []
    in_position = False
    entry_time = None
    entry_price = 0.0
    qty = max(1, int(quantity or 1))
    brokerage = max(0.0, float(brokerage_per_trade or 0.0))

    for ts, row in signals.iterrows():
        sig = int(row.get("signal", 0))
        close = float(row["Close"])
        if sig == 1 and not in_position:
            in_position = True
            entry_time = ts
            entry_price = close
        elif sig == -1 and in_position:
            gross = (close - entry_price) * qty
            costs = brokerage * 2
            pnl = gross - costs
            trades.append(
                {
                    "entry_time": entry_time,
                    "exit_time": ts,
                    "entry_price": entry_price,
                    "exit_price": close,
                    "quantity": qty,
                    "gross_pnl": gross,
                    "costs": costs,
                    "pnl": pnl,
                    "return_pct": (close - entry_price) / entry_price * 100 if entry_price else 0,
                }
            )
            in_position = False

    if in_position and not signals.empty:
        last = signals.iloc[-1]
        close = float(last["Close"])
        gross = (close - entry_price) * qty
        costs = brokerage * 2
        pnl = gross - costs
        trades.append(
            {
                "entry_time": entry_time,
                "exit_time": signals.index[-1],
                "entry_price": entry_price,
                "exit_price": close,
                "quantity": qty,
                "gross_pnl": gross,
                "costs": costs,
                "pnl": pnl,
                "return_pct": (close - entry_price) / entry_price * 100 if entry_price else 0,
            }
        )

    trades_df = pd.DataFrame(trades)
    metrics = _metrics(trades_df, capital)
    return BacktestResult(signals, trades_df, metrics)


def _metrics(trades: pd.DataFrame, capital: float) -> dict:
    cap = max(float(capital or 1.0), 1.0)
    if trades.empty:
        return {
            "trades": 0,
            "total_pnl": 0.0,
            "return_pct": 0.0,
            "win_rate": 0.0,
            "avg_pnl": 0.0,
            "max_drawdown": 0.0,
        }
    pnl = trades["pnl"].astype(float)
    equity = pnl.cumsum()
    peak = equity.cummax()
    drawdown = equity - peak
    wins = int((pnl > 0).sum())
    total = int(len(trades))
    total_pnl = float(pnl.sum())
    return {
        "trades": total,
        "total_pnl": total_pnl,
        "return_pct": total_pnl / cap * 100,
        "win_rate": wins / total * 100 if total else 0.0,
        "avg_pnl": float(pnl.mean()),
        "max_drawdown": float(drawdown.min()) if len(drawdown) else 0.0,
    }


def _rsi(close: pd.Series, period: int) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))
```

#### File: `trading_web/components/broker_data.py`
```python
import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Optional

import numpy as np
import pandas as pd
import yfinance as yf

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None

if load_dotenv:
    load_dotenv()


@dataclass
class DataResult:
    frame: pd.DataFrame
    source: str
    message: str


def clean_ohlc(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    df = df.copy()
    df = df.replace([np.inf, -np.inf], np.nan).dropna()
    rename = {
        "open": "Open",
        "high": "High",
        "low": "Low",
        "close": "Close",
        "volume": "Volume",
    }
    df = df.rename(columns={c: rename.get(str(c).lower(), c) for c in df.columns})
    keep = [c for c in ["Open", "High", "Low", "Close", "Volume"] if c in df.columns]
    df = df[keep]
    for col in ["Open", "High", "Low", "Close"]:
        if col in df:
            df = df[pd.to_numeric(df[col], errors="coerce") > 0]
    return df.dropna()


def fetch_market_data(
    source: str,
    symbol: str,
    mode: str,
    interval: str,
    lookback_days: int,
    daily_period: str,
) -> DataResult:
    source_key = str(source or "Yahoo").lower()
    if source_key.startswith("kite"):
        return fetch_kite(symbol, mode, interval, lookback_days, daily_period)
    if source_key.startswith("dhan"):
        return fetch_dhan(symbol, mode, interval, lookback_days, daily_period)
    return fetch_yahoo(symbol, mode, interval, lookback_days, daily_period)


def fetch_yahoo(symbol: str, mode: str, interval: str, lookback_days: int, daily_period: str) -> DataResult:
    if mode == "Intraday":
        end_dt = datetime.now(timezone.utc)
        start_dt = end_dt - timedelta(days=int(lookback_days or 5))
        df = yf.Ticker(symbol).history(
            start=start_dt,
            end=end_dt,
            interval=interval,
            auto_adjust=False,
            actions=False,
        )
        msg = f"Yahoo Finance intraday {interval}, last {lookback_days} day(s)"
    else:
        df = yf.Ticker(symbol).history(
            period=daily_period,
            interval="1d",
            auto_adjust=False,
            actions=False,
        )
        msg = f"Yahoo Finance daily {daily_period}"
    return DataResult(clean_ohlc(df), "Yahoo Finance", msg)


def fetch_kite(symbol: str, mode: str, interval: str, lookback_days: int, daily_period: str) -> DataResult:
    try:
        from kiteconnect import KiteConnect
    except Exception as exc:
        raise RuntimeError("KiteConnect is not installed. Run: pip install kiteconnect") from exc

    api_key = os.getenv("KITE_API_KEY")
    access_token = os.getenv("KITE_ACCESS_TOKEN")
    if not api_key or not access_token:
        raise RuntimeError("Missing KITE_API_KEY or KITE_ACCESS_TOKEN in environment.")

    kite = KiteConnect(api_key=api_key)
    kite.set_access_token(access_token)

    exchange = os.getenv("KITE_EXCHANGE", "NSE")
    token = _kite_find_instrument_token(kite, exchange, symbol)
    if token is None:
        raise RuntimeError(f"Could not find Kite instrument token for {exchange}:{symbol}.")

    end_dt = datetime.now()
    if mode == "Intraday":
        start_dt = end_dt - timedelta(days=int(lookback_days or 5))
        kite_interval = _kite_interval(interval)
    else:
        start_dt = end_dt - _period_to_timedelta(daily_period)
        kite_interval = "day"

    rows = kite.historical_data(token, start_dt, end_dt, kite_interval)
    df = pd.DataFrame(rows)
    if "date" in df:
        df = df.set_index("date")
    return DataResult(clean_ohlc(df), "Kite", f"Kite historical {kite_interval} for {exchange}:{symbol}")


def fetch_dhan(symbol: str, mode: str, interval: str, lookback_days: int, daily_period: str) -> DataResult:
    try:
        from dhanhq import DhanContext, dhanhq
    except Exception:
        try:
            from dhanhq import dhanhq
            DhanContext = None
        except Exception as exc:
            raise RuntimeError("dhanhq is not installed. Run: pip install dhanhq") from exc

    client_id = os.getenv("DHAN_CLIENT_ID")
    token = os.getenv("DHAN_TOKEN")
    if not client_id or not token:
        raise RuntimeError("Missing DHAN_CLIENT_ID or DHAN_TOKEN in environment.")

    client = dhanhq(DhanContext(client_id, token)) if DhanContext else dhanhq(client_id, token)
    security_id = _dhan_security_id_for(symbol)
    if not security_id:
        raise RuntimeError(
            "Dhan historical data needs a security id. Set DHAN_SECURITY_ID or "
            f"DHAN_SECURITY_ID_{_env_symbol(symbol)} in your environment."
        )

    exchange_segment = os.getenv("DHAN_EXCHANGE_SEGMENT", "NSE_EQ")
    end_dt = datetime.now()
    if mode == "Intraday":
        start_dt = end_dt - timedelta(days=int(lookback_days or 5))
        if not hasattr(client, "intraday_minute_data"):
            raise RuntimeError("Installed dhanhq client does not expose intraday_minute_data.")
        payload = client.intraday_minute_data(
            security_id=str(security_id),
            exchange_segment=exchange_segment,
            instrument_type=os.getenv("DHAN_INSTRUMENT_TYPE", "EQUITY"),
            from_date=start_dt.strftime("%Y-%m-%d"),
            to_date=end_dt.strftime("%Y-%m-%d"),
            interval=int(str(interval).replace("m", "") or 1),
        )
    else:
        start_dt = end_dt - _period_to_timedelta(daily_period)
        if not hasattr(client, "historical_daily_data"):
            raise RuntimeError("Installed dhanhq client does not expose historical_daily_data.")
        payload = client.historical_daily_data(
            security_id=str(security_id),
            exchange_segment=exchange_segment,
            instrument_type=os.getenv("DHAN_INSTRUMENT_TYPE", "EQUITY"),
            from_date=start_dt.strftime("%Y-%m-%d"),
            to_date=end_dt.strftime("%Y-%m-%d"),
        )

    rows = payload.get("data", payload) if isinstance(payload, dict) else payload
    df = pd.DataFrame(rows)
    for date_col in ["date", "start_Time", "start_time", "timestamp"]:
        if date_col in df:
            df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
            df = df.set_index(date_col)
            break
    return DataResult(clean_ohlc(df), "Dhan", f"Dhan historical data for security_id={security_id}")


def credential_status() -> dict[str, str]:
    return {
        "Dhan": "ready" if os.getenv("DHAN_CLIENT_ID") and os.getenv("DHAN_TOKEN") else "missing env",
        "Kite": "ready" if os.getenv("KITE_API_KEY") and os.getenv("KITE_ACCESS_TOKEN") else "missing env",
    }


def _kite_find_instrument_token(kite, exchange: str, symbol: str) -> Optional[int]:
    rows = kite.instruments(exchange)
    target = str(symbol).upper().replace(".NS", "")
    for row in rows:
        trading_symbol = str(row.get("tradingsymbol", "")).upper()
        if trading_symbol == target:
            return int(row.get("instrument_token"))
    return None


def _kite_interval(interval: str) -> str:
    return {
        "1m": "minute",
        "2m": "2minute",
        "5m": "5minute",
        "15m": "15minute",
    }.get(interval, "5minute")


def _period_to_timedelta(period: str) -> timedelta:
    value = str(period or "6mo").lower()
    if value.endswith("mo"):
        return timedelta(days=30 * int(value[:-2] or 6))
    if value.endswith("y"):
        return timedelta(days=365 * int(value[:-1] or 1))
    if value.endswith("d"):
        return timedelta(days=int(value[:-1] or 30))
    return timedelta(days=180)


def _env_symbol(symbol: str) -> str:
    return str(symbol or "").upper().replace(".", "_").replace("-", "_")


def _dhan_security_id_for(symbol: str) -> Optional[str]:
    specific = os.getenv(f"DHAN_SECURITY_ID_{_env_symbol(symbol)}")
    return specific or os.getenv("DHAN_SECURITY_ID")
```

#### File: `trading_web/app.py`
```python
import base64
import os
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from components.broker_data import credential_status, fetch_market_data
from components.strategy import run_backtest


BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


st.set_page_config(page_title="PsYcGoD Strategy Lab", layout="wide")


def apply_css_file(path: Path) -> None:
    if path.exists():
        st.markdown(f"<style>{path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def set_background(img_path: Path) -> None:
    if not img_path.exists():
        return
    encoded = base64.b64encode(img_path.read_bytes()).decode("utf-8")
    st.markdown(
        f"""
        <style>
        .stApp::before {{
            content: "";
            position: fixed;
            inset: 0;
            background-image:
              radial-gradient(80% 120% at 10% 10%, rgba(120,0,255,0.20), transparent 40%),
              radial-gradient(80% 120% at 90% 90%, rgba(0,255,220,0.18), transparent 40%),
              url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            opacity: 0.22;
            z-index: -1;
            filter: saturate(120%) hue-rotate(8deg);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def strategy_params(strategy_name: str) -> dict:
    if strategy_name == "Moving Average Crossover":
        short_window = st.slider("Short MA", 3, 50, 9)
        long_window = st.slider("Long MA", 5, 200, 21)
        if long_window <= short_window:
            st.warning("Long MA should be greater than Short MA.")
        return {"short_window": short_window, "long_window": long_window}

    if strategy_name == "RSI Reversion":
        return {
            "rsi_period": st.slider("RSI Period", 5, 40, 14),
            "rsi_lower": st.slider("RSI Buy Level", 5, 45, 30),
            "rsi_upper": st.slider("RSI Sell Level", 55, 95, 70),
        }

    return {"breakout_lookback": st.slider("Breakout Lookback", 5, 100, 20)}


def make_chart(df: pd.DataFrame, title: str) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            increasing_line_color="#00e5a0",
            decreasing_line_color="#ff4d6d",
            increasing_fillcolor="#00e5a0",
            decreasing_fillcolor="#ff4d6d",
            name="Price",
        )
    )

    buys = df[df.get("signal", 0) == 1]
    sells = df[df.get("signal", 0) == -1]
    if not buys.empty:
        fig.add_scatter(
            x=buys.index,
            y=buys["Low"],
            mode="markers",
            name="Buy",
            marker=dict(color="#00ffd1", size=10, symbol="triangle-up", line=dict(width=1, color="#021b1f")),
        )
    if not sells.empty:
        fig.add_scatter(
            x=sells.index,
            y=sells["High"],
            mode="markers",
            name="Sell",
            marker=dict(color="#ff4d6d", size=10, symbol="triangle-down", line=dict(width=1, color="#2a0b13")),
        )

    for col, color in [
        ("short_ma", "#f7d154"),
        ("long_ma", "#7dd3fc"),
        ("breakout_high", "#22c55e"),
        ("breakout_low", "#ef4444"),
    ]:
        if col in df:
            fig.add_scatter(x=df.index, y=df[col], mode="lines", name=col, line=dict(color=color, width=1.4))

    fig.update_layout(
        template="plotly_dark",
        height=560,
        margin=dict(l=10, r=10, t=40, b=10),
        xaxis_rangeslider_visible=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        title=title,
        font=dict(color="#d8f3ff"),
    )
    return fig


apply_css_file(ASSETS_DIR / "styles.css")
set_background(ASSETS_DIR / "psy_bg.png")

st.markdown('<div class="app-header">PsYcGoD Strategy Lab</div>', unsafe_allow_html=True)
st.caption("Create strategy rules, fetch historical data, and backtest before any live trading.")

with st.sidebar:
    st.header("Data")
    source = st.selectbox("Source", ["Yahoo Finance", "Dhan", "Kite"], index=0)
    ticker = st.text_input("Symbol", "RELIANCE.NS").strip().upper()
    mode = st.selectbox("Mode", ["Intraday", "Daily"], index=0)
    if mode == "Intraday":
        interval = st.selectbox("Interval", ["1m", "2m", "5m", "15m"], index=2)
        lookback = st.selectbox("Lookback days", [1, 3, 5, 7, 10, 14], index=2)
        daily_period = "1mo"
    else:
        interval = "1d"
        lookback = 30
        daily_period = st.selectbox("Daily period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=2)

    st.header("Strategy")
    strategy = st.selectbox(
        "Strategy Builder",
        ["Moving Average Crossover", "RSI Reversion", "Breakout"],
        index=0,
    )
    params = strategy_params(strategy)

    st.header("Backtest")
    capital = st.number_input("Capital", min_value=1000.0, value=50000.0, step=1000.0)
    quantity = st.number_input("Quantity per trade", min_value=1, value=1, step=1)
    brokerage = st.number_input("Brokerage per side", min_value=0.0, value=20.0, step=1.0)
    run_btn = st.button("Run Backtest", type="primary")

    st.header("Credentials")
    status = credential_status()
    st.write(f"Dhan: {status['Dhan']}")
    st.write(f"Kite: {status['Kite']}")
    st.caption("Credentials are read from environment variables. Do not commit .env files.")

if "result" not in st.session_state:
    st.session_state["result"] = None

if run_btn:
    try:
        data = fetch_market_data(source, ticker, mode, interval, int(lookback), daily_period)
        if data.frame.empty:
            st.warning("No data returned. Try another symbol, source, interval, or period.")
        else:
            result = run_backtest(data.frame, strategy, params, capital, int(quantity), brokerage)
            st.session_state["result"] = {
                "data_source": data.source,
                "message": data.message,
                "strategy": strategy,
                "params": params,
                "result": result,
            }
    except Exception as exc:
        st.error(str(exc))

saved = st.session_state.get("result")

if not saved:
    st.info("Choose a data source and strategy, then click Run Backtest.")
else:
    result = saved["result"]
    metrics = result.metrics
    title = f"{ticker} | {saved['strategy']} | {saved['data_source']}"

    a, b, c, d, e = st.columns(5)
    a.metric("Trades", metrics["trades"])
    b.metric("Total P&L", f"Rs {metrics['total_pnl']:,.2f}")
    c.metric("Return", f"{metrics['return_pct']:.2f}%")
    d.metric("Win Rate", f"{metrics['win_rate']:.1f}%")
    e.metric("Max Drawdown", f"Rs {metrics['max_drawdown']:,.2f}")

    st.caption(saved["message"])
    st.markdown('<div class="panel chart-panel">', unsafe_allow_html=True)
    st.plotly_chart(make_chart(result.frame, title), width="stretch")
    st.markdown("</div>", unsafe_allow_html=True)

    left, right = st.columns([0.55, 0.45])
    with left:
        st.subheader("Trades")
        if result.trades.empty:
            st.write("No completed trades for these rules.")
        else:
            st.dataframe(result.trades, use_container_width=True)
            st.download_button(
                "Download trades CSV",
                result.trades.to_csv(index=False),
                file_name="jiraiya_backtest_trades.csv",
                mime="text/csv",
            )

    with right:
        st.subheader("Strategy Parameters")
        st.json(saved["params"])
        st.warning(
            "Backtesting is research only. It does not guarantee live profit. "
            "Use paper trading before any real order placement."
        )

st.markdown('<div class="footer-log">Strategy Lab ready | backtest-only | no live orders</div>', unsafe_allow_html=True)
```


==================================================


## [3/3] Repository: API_Based_Trading (`WHEEL_Kite-Dhan_API_Based_Trading`)
- **Full Name**: `Kite-Dhan_API_Based_Trading`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Core Implementation Code & Architecture
#### File: `package.json`
```python
{
  "name": "dhanapi",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "buffer": "^6.0.3",
    "dotenv": "^16.4.7",
    "node.js": "^0.0.1-security",
    "ws": "^8.18.0"
  }
}
```

#### File: `package-lock.json`
```python
{
  "name": "dhanapi",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "dhanapi",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "buffer": "^6.0.3",
        "dotenv": "^16.4.7",
        "node.js": "^0.0.1-security",
        "ws": "^8.18.0"
      }
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/buffer": {
      "version": "6.0.3",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-6.0.3.tgz",
      "integrity": "sha512-FTiCpNxtwiZZHEZbcbTIcZjERVICn9yq/pDFkTl95/AxzD1naBctN7YO68riM/gLSDY7sdrMby8hofADYuuqOA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "base64-js": "^1.3.1",
        "ieee754": "^1.2.1"
      }
    },
    "node_modules/dotenv": {
      "version": "16.4.7",
      "resolved": "https://registry.npmjs.org/dotenv/-/dotenv-16.4.7.tgz",
      "integrity": "sha512-47qPchRCykZC03FhkYAhrvwU4xDBFIj1QPqaarj6mdM/hgUzfPHcpkHJOn3mJAufFeeAxAzeGsr5X0M4k6fLZQ==",
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://dotenvx.com"
      }
    },
    "node_modules/ieee754": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz",
      "integrity": "sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "BSD-3-Clause"
    },
    "node_modules/node.js": {
      "version": "0.0.1-security",
      "resolved": "https://registry.npmjs.org/node.js/-/node.js-0.0.1-security.tgz",
      "integrity": "sha512-8tWQiyg/3ggdLTrtfgj/NxmZpC20eB1U5VNkqt2dbelpcr3NrfjpEE3DgifpBOCJ4Xu9Obvu8iju63ViQW3Hvg=="
    },
    "node_modules/ws": {
      "version": "8.18.0",
      "resolved": "https://registry.npmjs.org/ws/-/ws-8.18.0.tgz",
      "integrity": "sha512-8VbfWfHLbbwu3+N6OKsOMpBdT4kXPDDB9cJk2bJ6mh9ucxdlnNvH1e+roYkKmN9Nxw2yjz7VzeO9oOz2zJ04Pw==",
      "license": "MIT",
      "engines": {
        "node": ">=10.0.0"
      },
      "peerDependencies": {
        "bufferutil": "^4.0.1",
        "utf-8-validate": ">=5.0.2"
      },
      "peerDependenciesMeta": {
        "bufferutil": {
          "optional": true
        },
        "utf-8-validate": {
          "optional": true
        }
      }
    }
  }
}
```


==================================================
