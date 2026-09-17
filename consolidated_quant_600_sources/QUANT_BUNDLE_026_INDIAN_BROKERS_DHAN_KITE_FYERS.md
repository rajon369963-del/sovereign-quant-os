# ⚡ [QUANT-SOURCE-026] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_026_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: indian-algo-ai-skill (`WHEEL_indian-algo-ai-skill`)
- **Full Name**: `indian-algo-ai-skill`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Indian Algo Trading

**Production-quality Python trading strategies for Indian markets — AI-assisted, from backtest to live.**

## Overview

This plugin helps you build algorithmic trading strategies for Indian markets (NSE, BSE, MCX) with best practices baked in. It doesn't ship pre-built strategies — instead, it teaches AI how to help you design safe, realistic, and compliant strategies from scratch.

Covers the full lifecycle: backtesting → optimization → paper trading → live deployment, across equity, F&O, currency derivatives, and MCX commodities.

---

## Installation

### Claude Code Plugin

```bash
# Register the marketplace (one-time)
claude plugin marketplace add RupeezyTech/algo_ai_skill

# Install
claude plugin install indian-algo-trading@rupeezy
```

### Standalone Skill

Download from [Releases](https://github.com/RupeezyTech/algo_ai_skill/releases) and extract:

```bash
unzip indian-algo-trading-*.skill -d ~/.claude/skills/indian-algo-trading/
```

### Local dev / testing

```bash
git clone https://github.com/RupeezyTech/algo_ai_skill.git
claude --plugin-dir ./algo_ai_skill
```

---

## Usage

Once installed, the skill activates automatically when you ask about:

- Writing a strategy (`"write a moving average crossover for Nifty"`)
- Backtesting (`"backtest this on 2022-2024 data with realistic costs"`)
- Live trading (`"make this strategy production-ready for live deployment"`)
- F&O automation (`"iron condor strategy for weekly expiry"`)
- Risk management (`"add position sizing and daily loss limits"`)

The skill will ask clarifying questions (asset class, live vs backtest, broker, risk tolerance) before generating code.

---

## What Gets Generated

Every strategy follows a strict separation of concerns:

```
my_strategy/
├── main.py          # Entry point, scheduling, SIGTERM handler
├── strategy.py      # Signal generation only
├── execution.py     # Order placement, fill tracking
├── risk_manager.py  # Position sizing, exposure checks, drawdown limits
├── config.py        # All parameters — no hardcoded values
└── requirements.txt
```

Every strategy includes: stop-losses, margin checks, tick size rounding, IST timezone, structured logging, and graceful shutdown. No exceptions.

---

## Reference Library (16 files)

| File | Covers |
|------|--------|
| `strategy-patterns.md` | Momentum, mean reversion, options, pairs trading |
| `risk-management.md` | Position sizing, drawdown controls, margin monitoring |
| `indian-market.md` | Timings, expiry calendar, STT, circuit limits, auction risk |
| `backtesting.md` | Library selection, realistic costs, parameter optimization |
| `error-handling.md` | Order state machine, partial fills, graceful shutdown |
| `code-quality.md` | Project structure, logging, testing, type hints |
| `options-greeks.md` | Delta-neutral, gamma scalping, theta harvesting, IV vs RV |
| `regime-detection.md` | HMM for trending/volatile/sideways, strategy decay |
| `india-data-edge.md` | FII/DII flows, OI analysis, PCR, max pain, delivery % |
| `execution-alpha.md` | TWAP, VWAP, iceberg, impact cost, intraday timing |
| `robustness-testing.md` | Walk-forward, Monte Carlo, sensitivity analysis |
| `portfolio-construction.md` | Multi-strategy allocation, correlation-aware sizing |
| `psychological-guardrails.md` | Daily loss breaker, consecutive loss pause, killswitch |
| `tax-optimization.md` | STCG vs LTCG, tax-loss harvesting, F&O business income |
| `python-performance.md` | Vectorization, Numba, Polars, async, profiling |
| `brokers/rupeezy-vortex.md` | Full Vortex SDK reference for live trading |

---

## Repository Structure

```
algo_ai_skill/
├── .claude-plugin/
│   └── marketplace.json              # Marketplace catalog (GitHub sync)
│
├── plugins/
│   └── indian-algo-trading/
│       ├── .claude-plugin/
│       │   └── plugin.json           # Plugin manifest
│       ├── .mcp.json                 # Rupeezy MCP server config
│       └── skills/
│           └── indian-algo-trading/
│               ├── SKILL.md          # Skill instructions + routing logic
│               ├── references/       # 16 reference files
│               └── scripts/
│                   ├── scaffold_strategy.py      # Generate strategy skeleton
│                   └── validate_strategy.py      # AST linter for common mistakes
│
├── evals/
│   └── evals.json                    # 10 skill evaluation test cases
│
├── build/                            # Generated — gitignored
│   ├── *.skill                       # Standalone skill zip (GitHub release)
│   └── *.plugin                      # Full plugin zip (Anthropic marketplace)
│
└── Makefile                          # Build, validate, release
```

---

## Developer Commands

```bash
# Build both artifacts
make all

# Build standalone skill zip only
make skill

# Build full plugin zip only
make plugin

# Validate JSON manifests and SKILL.md frontmatter
make validate

# Test scaffold script generates valid output
make test-scaffold

# Scaffold a new strategy project
python plugins/indian-algo-trading/skills/indian-algo-trading/scripts/scaffold_strategy.py my_strategy

# Validate strategy code against best practices
python plugins/indian-algo-trading/skills/indian-algo-trading/scripts/validate_strategy.py path/to/strategy.py

# Cut a release (requires git tag + gh CLI)
git tag -a v1.1.4 -m "Release v1.1.4"
make release
```

---

## Contributing

Contributions are welcome and encouraged. The most impactful areas:

- **Broker adapters** — add support for Zerodha, AngelOne, Fyers, Upstox, or any other broker using the [BROKER_TEMPLATE](plugins/indian-algo-trading/skills/indian-algo-trading/references/brokers/BROKER_TEMPLATE.md). Step-by-step guide in [CONTRIBUTING_BROKER.md](plugins/indian-algo-trading/skills/indian-algo-trading/references/brokers/CONTRIBUTING_BROKER.md).
- **Reference file improvements** — corrections, new sections, updated regulations (SEBI circulars, lot size changes, STT rates)
- **Scripts and tooling** — backtesting utilities, data analysis tools, strategy validators

See [CONTRIBUTING.md](CONTRIBUTING.md) for review requirements and timelines.

> **High-stakes project**: incorrect market data or unsafe code patterns can cost real money. All contributions require maintainer review before merge.

---

## License

Apache License 2.0 — see [LICENSE](LICENSE).

## Disclaimer

For educational and research purposes. Trading carries risk of loss. Backtest results do not guarantee future performance. Always paper trade before going live. Consult a financial advisor.

### Core Implementation Code & Architecture
#### File: `assets/strategy_template/tests/__init__.py`
```python
"""
Test suite for Indian algo trading strategy.

This package contains unit tests for strategy components including signal generation,
order execution, risk management, and market health checks.
"""
```

#### File: `plugins/indian-algo-trading/.claude-plugin/plugin.json`
```python
{
  "name": "indian-algo-trading",
  "version": "1.2.1",
  "description": "Indian algo trading skill suite for strategy design, backtesting, risk management, execution, and broker integration.",
  "author": {
    "name": "Rupeezy"
  },
  "keywords": [
    "algo-trading",
    "india",
    "backtesting",
    "risk-management",
    "options",
    "rupeezy",
    "vortex"
  ]
}
```

#### File: `.claude-plugin/plugin.json`
```python
{
  "name": "indian-algo-trading",
  "version": "1.1.4",
  "description": "Write production-quality Python algo trading strategies for Indian markets (NSE, BSE, MCX). Includes AI skill with 16 reference files + Rupeezy MCP servers for live trading, strategy deployment, backtesting, and portfolio management.",
  "author": {
    "name": "Rupeezy"
  },
  "keywords": ["algo-trading", "indian-stock-market", "nse", "bse", "mcx", "python", "backtesting", "rupeezy", "vortex-api", "options-trading", "quantitative-trading"]
}
```

#### File: `.claude-plugin/marketplace.json`
```python
{
  "name": "rupeezy",
  "owner": {
    "name": "Rupeezy"
  },
  "metadata": {
    "description": "Write production-quality Python algo trading strategies for Indian markets (NSE, BSE, MCX). AI skill with 16 reference files + Rupeezy MCP servers for live trading, strategy deployment, backtesting, and portfolio management.",
    "version": "1.2.1",
    "pluginRoot": "./plugins/indian-algo-trading"
  },
  "plugins": [
    {
      "name": "indian-algo-trading",
      "source": "./plugins/indian-algo-trading",
      "description": "Write production-quality Python algo trading strategies for Indian markets. Full suite: AI skill + Rupeezy MCP servers for live trading, strategy deployment, backtesting, and portfolio management.",
      "version": "1.2.1",
      "keywords": [
        "algo-trading",
        "indian-stock-market",
        "nse",
        "bse",
        "mcx",
        "python",
        "backtesting",
        "rupeezy",
        "vortex-api",
        "options-trading",
        "quantitative-trading",
        "strategy-writing"
      ]
    }
  ]
}
```

#### File: `assets/strategy_template/main.py`
```python
"""
Main strategy entry point with graceful shutdown, logging, and IST timezone support.

This module initializes the trading strategy, sets up signal handlers for graceful shutdown,
configures logging with IST timestamps, and orchestrates the overall strategy lifecycle.
"""

import signal
import logging
import logging.handlers
from datetime import datetime
from pathlib import Path
from typing import Optional

import pytz

from config import Config
from strategy import Strategy
from risk_manager import RiskManager
from guardrails import CircuitBreaker


# Configure IST timezone
IST = pytz.timezone("Asia/Kolkata")

# Configure logging with IST timestamps
class ISTFormatter(logging.Formatter):
    """Custom formatter to use IST timestamps in logs."""

    def formatTime(self, record, datefmt=None):
        """Format timestamp in IST."""
        ct = datetime.fromtimestamp(record.created, tz=IST)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = f"{t}.{int(ct.microsecond / 1000):03d}"
        return s


def setup_logging(config: Config) -> logging.Logger:
    """
    Set up logging with both file and console handlers, using IST timestamps.

    Args:
        config: Configuration object containing log settings.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, config.log_level))

    # Create formatters
    formatter = ISTFormatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, config.log_level))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    log_dir = Path(config.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"strategy_{datetime.now(tz=IST).strftime('%Y%m%d_%H%M%S')}.log"

    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=5
    )
    file_handler.setLevel(getattr(logging, config.log_level))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f"Logging initialized. Log file: {log_file}")
    return logger


class StrategyRunner:
    """Manages strategy lifecycle including initialization, execution, and graceful shutdown."""

    def __init__(self, config: Config):
        """
        Initialize the strategy runner.

        Args:
            config: Configuration object containing strategy and risk parameters.
        """
        self.config = config
        self.logger = setup_logging(config)
        self.strategy: Optional[Strategy] = None
        self.running = False

        # Register signal handlers for graceful shutdown
        signal.signal(signal.SIGTERM, self._handle_shutdown)
        signal.signal(signal.SIGINT, self._handle_shutdown)

    def _handle_shutdown(self, signum, frame):
        """
        Handle shutdown signals (SIGTERM, SIGINT) gracefully.

        Args:
            signum: Signal number.
            frame: Current stack frame.
        """
        self.logger.info(f"Received signal {signum}. Initiating graceful shutdown...")
        self.running = False
        if self.strategy:
            self.strategy.shutdown()
        self.logger.info("Strategy shutdown complete.")
        exit(0)

    def run(self):
        """
        Initialize and run the strategy.

        Raises:
            ValueError: If configuration validation fails.
        """
        try:
            # Validate configuration
            self.config.validate()
            self.logger.info("Configuration validated successfully.")

            # Initialize risk manager and circuit breaker
            risk_manager = RiskManager(self.config)
            circuit_breaker = CircuitBreaker(self.config)
            self.logger.info("Risk manager and circuit breaker initialized.")

            # Initialize strategy
            self.strategy = Strategy(self.config, risk_manager, circuit_breaker)
            self.logger.info("Strategy initialized.")

            # Run strategy
            self.running = True
            self.logger.info("Starting strategy execution...")
            self.strategy.run()

        except Exception as e:
            self.logger.error(f"Strategy execution failed: {e}", exc_info=True)
            raise


def main():
    """Main entry point for the strategy."""
    # TODO: Load configuration from environment or config file
    config = Config()

    runner = StrategyRunner(config)
    runner.run()


if __name__ == "__main__":
    main()
```

#### File: `assets/strategy_template/guardrails.py`
```python
"""
Guardrails module implementing market health checks and slippage detection.

This module contains the CircuitBreaker class which monitors market conditions
and can halt trading if anomalies are detected.
"""

import logging
from dataclasses import dataclass
from typing import Optional

from config import Config


@dataclass
class MarketHealth:
    """Represents current market health status."""

    is_healthy: bool
    bid_ask_valid: bool
    spread_within_limit: bool
    halted: bool = False
    reason: str = ""


class CircuitBreaker:
    """
    Monitors market conditions and implements circuit breaker logic.

    Detects anomalies such as zero bid/ask spreads, extreme spreads, or market halts.
    """

    def __init__(self, config: Config):
        """
        Initialize the circuit breaker.

        Args:
            config: Configuration object with guardrail parameters.
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.halted = False
        self.halt_reason = ""

        self.logger.info("CircuitBreaker initialized.")

    def check_market_health(self, tick) -> MarketHealth:
        """
        Check overall market health based on current tick.

        Validates:
        - Bid/ask prices are non-zero
        - Bid price < ask price
        - Spread is within acceptable limits

        Args:
            tick: Current market tick with bid/ask data.

        Returns:
            MarketHealth object indicating health status.
        """
        health = MarketHealth(is_healthy=True, bid_ask_valid=True, spread_within_limit=True)

        # Check if bid/ask are valid (non-zero and bid < ask)
        if not tick.bid_price or not tick.ask_price:
            health.bid_ask_valid = False
            health.is_healthy = False
            health.reason = "Invalid bid/ask prices (zero or missing)"
            self.logger.warning(f"Market health check failed: {health.reason} for {tick.symbol}")
            return health

        if tick.bid_price >= tick.ask_price:
            health.bid_ask_valid = False
            health.is_healthy = False
            health.reason = f"Invalid bid/ask: bid({tick.bid_price}) >= ask({tick.ask_price})"
            self.logger.warning(f"Market health check failed: {health.reason} for {tick.symbol}")
            return health

        # Check if spread is within limits
        if not self._check_spread_limit(tick):
            health.spread_within_limit = False
            health.is_healthy = False
            spread = tick.ask_price - tick.bid_price
            health.reason = f"Spread exceeded: {spread} for {tick.symbol}"
            self.logger.warning(f"Market health check failed: {health.reason}")
            return health

        self.logger.debug(f"Market health OK for {tick.symbol}")
        return health

    def _check_spread_limit(self, tick) -> bool:
        """
        Check if bid-ask spread is within acceptable limits.

        Spread limit is typically defined as percentage of mid price.

        Args:
            tick: Current market tick.

        Returns:
            True if spread is within limit, False otherwise.
        """
        # TODO: Get spread limit from config
        max_spread_percent = 0.5  # 0.5% of mid price

        mid_price = (tick.bid_price + tick.ask_price) / 2
        spread = tick.ask_price - tick.bid_price
        spread_percent = (spread / mid_price) * 100

        return spread_percent <= max_spread_percent

    def check_slippage(
        self,
        symbol: str,
        expected_price: float,
        actual_price: float,
        max_slippage_percent: float = 0.1,
    ) -> bool:
        """
        Check if actual execution price has excessive slippage.

        Args:
            symbol: Trading symbol.
            expected_price: Expected execution price.
            actual_price: Actual execution price.
            max_slippage_percent: Maximum acceptable slippage as percentage. Default 0.1%.

        Returns:
            True if slippage is within limit, False if excessive.
        """
        if expected_price == 0:
            self.logger.warning(f"Cannot check slippage for {symbol}: expected_price is 0")
            return True

        slippage_percent = abs((actual_price - expected_price) / expected_price) * 100

        if slippage_percent > max_slippage_percent:
            self.logger.warning(
                f"Excessive slippage detected for {symbol}: "
                f"expected={expected_price}, actual={actual_price}, "
                f"slippage={slippage_percent:.4f}%"
            )
            return False

        self.logger.debug(
            f"Slippage acceptable for {symbol}: {slippage_percent:.4f}% "
            f"(limit: {max_slippage_percent}%)"
        )
        return True

    def halt_trading(self, reason: str):
        """
        Halt all trading activity.

        Args:
            reason: Reason for halt (logged for audit trail).
        """
        self.halted = True
        self.halt_reason = reason
        self.logger.error(f"TRADING HALTED: {reason}")

    def resume_trading(self):
        """Resume trading activity after halt."""
        self.halted = False
        self.halt_reason = ""
        self.logger.info("Trading resumed.")

    def is_trading_halted(self) -> bool:
        """
        Check if trading is currently halted.

        Returns:
            True if halted, False otherwise.
        """
        return self.halted
```


==================================================


## [2/3] Repository: marketwatch (`WHEEL_marketwatch`)
- **Full Name**: `marketwatch`
- **Description**: A beautiful, privacy-first Chrome extension to instantly view your Dhan trading portfolio, real-time net P&L, and open/closed positions—right from your browser. Features a modern UI, one-click reload, and local proxy for secure API access. Open source, easy to set up, and perfect for active traders!
- **GitHub Stars**: 2
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# 🚀 Dhan Portfolio Viewer

[![Chrome Web Store](https://img.shields.io/chrome-web-store/v/your-extension-id.svg?logo=google-chrome&label=Chrome%20Web%20Store)](https://chrome.google.com/webstore/detail/your-extension-id)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **The best way to view your Dhan trading portfolio, PnL, and positions right from your browser!**

---

## ✨ Features

- 🔥 **Instant Net PnL**: See your real-time net profit & loss for the day
- 📈 **Open & Closed Positions**: Beautifully organized, always up-to-date
- 🛡️ **Privacy-first**: Your token stays on your device
- ⚡ **One-click Reload**: Refresh your data instantly
- 🎨 **Gorgeous UI**: Modern, clean, and responsive design
- 🛠️ **Easy Setup**: Just paste your Dhan access token and go

---

## 📸 Screenshots

| Popup View | Settings |
|---|---|
| ![Popup Screenshot](./screenshots/popup.png) | ![Settings Screenshot](./screenshots/settings.png) |

---

## 🧑‍💻 Installation

### From Chrome Web Store
1. [Install from Chrome Web Store](https://chrome.google.com/webstore/detail/your-extension-id)
2. Click the extension icon and open the popup
3. Go to **Settings** and paste your Dhan access token

### Developer Mode (Local)
1. Clone this repo:
   ```sh
   git clone https://github.com/abhisheksoni27/marketwatch.git
   cd marketwatch
   ```
2. Install dependencies and start the proxy server:
   ```sh
   pnpm install
   pnpm start
   # Proxy runs at http://localhost:3001
   ```
3. For automatic extension rebuilds on file changes, run:
   ```sh
   pnpm build:watch
   ```
   This will keep the dist folder up to date. Refresh the extension in Chrome to see changes.
4. In Chrome, go to `chrome://extensions` > Enable **Developer mode**
5. Click **Load unpacked** and select this folder
6. Open the extension popup, go to **Settings**, and paste your Dhan access token

---

## 🌐 Proxy Server Setup (CORS Fix)

Dhan's API does not support CORS for browser extensions. This project includes a simple Node.js proxy server:

- Start it with `pnpm start` (see above)
- The extension will automatically use `http://localhost:3001/positions` for API calls
- **Never share your access token**

---

## 🔒 Security & Privacy
- Your Dhan access token is stored only in your browser (Chrome sync storage)
- All API calls are proxied locally; your data never leaves your machine
- **Open source**: Review the code yourself!

---

## 🤝 Contributing

Pull requests, issues, and feature suggestions are welcome!

1. Fork this repo
2. Create a feature branch
3. Submit a PR

---

## 📄 License

MIT License. See [LICENSE](./LICENSE).

---

> _Made with ❤️ for traders by [Abhishek Soni](https://github.com/abhisheksoni27)_

### Core Implementation Code & Architecture
#### File: `manifest.json`
```python
{
  "manifest_version": 3,
  "name": "Dhan Portfolio Viewer",
  "version": "1.0",
  "description": "View your open/closed positions and net PnL for the day using Dhan APIs.",
  "permissions": ["storage", "activeTab"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "dist/index.html"
  },
  "options_page": "options.html"
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ESNext",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ESNext"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

#### File: `package.json`
```python
{
  "name": "dhan-proxy-server",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "vite",
    "build": "vite build",
    "build:watch": "vite build --watch"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.18.2",
    "node-fetch": "^2.6.7",
    "react": "^19.1.0",
    "react-dom": "^19.1.0"
  },
  "packageManager": "pnpm@8.15.5",
  "type": "module",
  "devDependencies": {
    "@types/react": "^19.1.6",
    "@types/react-dom": "^19.1.5",
    "@vitejs/plugin-react": "^4.5.0",
    "vite": "^6.3.5"
  }
}
```


==================================================


## [3/3] Repository: nifty-930-breakout-trading-system (`WHEEL_nifty-930-breakout-trading-system`)
- **Full Name**: `nifty-930-breakout-trading-system`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# 9:30 AM Nifty Premium Strategy — Backtest / Paper / Live

A Flask web desk that runs one intraday options idea: at 9:25 pick the ITM CE and
PE strike trading closest to **₹180**; from 9:30 the first side to break above ₹180
and hold it is your entry; **SL 20 pts (160)**, **target 40 pts (220)**, flat by 9:45.

The same rule engine (`strategy.py`) drives all three modes, so what you backtest is
exactly what paper and live do.

```
nifty_930/
├── app.py             Flask dashboard + routes
├── config.py          every tunable number (levels, times, lots) — edit here
├── strategy.py        the shared rule engine (no Dhan, no I/O)
├── dhan_client.py     all Dhan API calls live here
├── engine_paper.py    live prices, simulated fills
├── engine_live.py     real Dhan Super Orders (double-gated)
├── engine_backtest.py replay past sessions through the same rules
├── engine_base.py     shared status/threading scaffolding
├── templates/index.html
├── requirements.txt
└── .env.example
```

## Setup

```bash
cd nifty_930
python -m venv venv
venv\Scripts\activate            # Windows  (mac/linux: source venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env           # then edit .env
python app.py
```

Open http://127.0.0.1:5000

`.env` needs a **fresh** Dhan access token (they expire every 24h). Paper and live
need it; backtest sample does not.

## The three modes

**Backtest** — press *Run sample backtest* to see the engine work immediately with
synthetic data (no token). For real numbers, feed it Dhan expired-options minute data
(needs the ₹499/mo Data API subscription) via `engine_backtest.load_session_from_dhan`,
or your own CSVs via `load_session_from_csv` (columns: `time,open,high,low,close`).

**Paper** — real live premiums from Dhan, fully simulated entries/exits. **Live here
for 30+ sessions first.**

**Live** — places a real Dhan **Super Order** (entry + target + SL in one, so your stop
sits at the exchange). Gated twice: `LIVE_TRADING_ENABLED=true` in `.env` **and** the
confirm box in the UI.

## Tuning

Everything is in `config.py`: `TRIGGER_PREMIUM`, `SL_POINTS`, `TARGET_POINTS`, the
timing windows, `LOTS`, and `ADVANCED_MODE` (hold to 10:00 + trail SL to cost, off by
default).

## SDK note

Calls in `dhan_client.py` marked `# VERIFY` match DhanHQ v2.x. If one errors with
"no attribute", check your installed version's README (`pip show dhanhq`) — Dhan
occasionally renames methods — and adjust just that line.

## Reality check

This is software that does what the rules say; it is **not** a promise that the rules
make money. The 70–75% figure is one creator's personal claim. Options buying loses
fast when wrong. Backtest on real data, size small, and only you own the risk. Not
financial advice.

### Core Implementation Code & Architecture
#### File: `engine_base.py`
```python
"""
engine_base.py — shared scaffolding for the three engines.

Holds a thread-safe status snapshot that the Flask dashboard polls, plus the
common session shape (prep -> watch -> manage -> done).
"""
import threading
import datetime as dt
from zoneinfo import ZoneInfo
import config
from strategy import StrategyState, select_strikes

IST = ZoneInfo("Asia/Kolkata")


def now_ist() -> dt.datetime:
    return dt.datetime.now(IST)


class EngineBase:
    mode = "base"

    def __init__(self):
        self.state = StrategyState()
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._status = {
            "mode": self.mode, "phase": "idle", "message": "Not started",
            "strikes": {}, "ltps": {}, "position": None, "pnl": 0.0,
            "log": [], "running": False, "spot": None,
        }

    # -- status the web UI reads -----------------------------------------
    def snapshot(self) -> dict:
        with self._lock:
            return dict(self._status)

    def _push(self, **kw):
        with self._lock:
            self._status.update(kw)
            self._status["log"] = self.state.log[-40:]
            p = self.state.position
            if p:
                self._status["position"] = {
                    "side": p.side, "strike": p.strike, "entry": round(p.entry, 1),
                    "sl": round(p.stop_loss, 1), "target": round(p.target, 1),
                    "open": p.is_open, "exit": p.exit, "reason": p.exit_reason,
                }

    def stop(self):
        self._stop.set()

    # -- helper: turn StrikeChoice dict into status-friendly dict ---------
    def _strikes_for_status(self) -> dict:
        return {s: {"strike": c.strike, "premium": round(c.premium_at_pick, 1),
                    "security_id": c.security_id}
                for s, c in self.state.strikes.items()}
```

#### File: `engine_paper.py`
```python
"""
engine_paper.py — PAPER trading. Uses REAL live premiums from Dhan but places
NO real orders. Entries/exits are simulated in StrategyState. This is the mode
you should live in for 30+ sessions before risking a rupee.
"""
import time
from engine_base import EngineBase, now_ist
from strategy import select_strikes
import config


class PaperEngine(EngineBase):
    mode = "paper"

    def __init__(self, dhan):
        super().__init__()
        self.dhan = dhan

    def run(self):
        self._push(running=True, phase="prep", message="Fetching option chain…")
        try:
            expiry = self.dhan.nearest_weekly_expiry()
            spot, rows = self.dhan.option_chain(expiry)
            self.state.strikes = select_strikes(rows, spot)
            if "CE" not in self.state.strikes or "PE" not in self.state.strikes:
                self._push(phase="error", running=False,
                           message="Could not find ITM strikes near ₹180.")
                return
            self._push(phase="watch", spot=spot, strikes=self._strikes_for_status(),
                       message=f"Watching for ₹{config.TRIGGER_PREMIUM:.0f} break "
                               f"(expiry {expiry})")
        except Exception as e:
            self._push(phase="error", running=False, message=f"Setup failed: {e}")
            return

        sids = {s: c.security_id for s, c in self.state.strikes.items()}

        while not self._stop.is_set() and not self.state.finished:
            now = now_ist()
            try:
                quotes = self.dhan.ltp(list(sids.values()))
            except Exception as e:
                self._push(message=f"Quote error (retrying): {e}")
                time.sleep(config.POLL_SECONDS)
                continue

            ltps = {s: quotes.get(sid) for s, sid in sids.items()}
            self._push(ltps={s: v for s, v in ltps.items() if v is not None})

            if self.state.position is None:
                self.state.check_entry(now, {k: v for k, v in ltps.items() if v})
            else:
                live = ltps.get(self.state.position.side)
                if live:
                    self.state.manage(now, live)
                    self._push(pnl=round(self.state.position.pnl_at(live), 0))

            if now.time() >= config.HARD_EXIT_TIME and not config.ADVANCED_MODE:
                if self.state.position and self.state.position.is_open:
                    live = ltps.get(self.state.position.side)
                    if live:
                        self.state.force_flat(now, live)

            self._push(phase="manage" if self.state.position else "watch")
            time.sleep(config.POLL_SECONDS)

        self._push(running=False, phase="done", message="Session over.")
```

#### File: `config.py`
```python
"""
config.py — every tunable number for the 9:30 AM Nifty premium strategy lives here.
Change values here only; the engines and strategy read from this file.
"""
import os
from datetime import time
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Dhan credentials (kept in .env, NEVER hard-coded — your token leaked before)
# ---------------------------------------------------------------------------
DHAN_CLIENT_ID    = os.getenv("DHAN_CLIENT_ID", "")
DHAN_ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN", "")

# Hard safety gate. Live orders are only ever placed when this is the literal
# string "true" in your .env AND you confirm again in the web UI.
LIVE_TRADING_ENABLED = os.getenv("LIVE_TRADING_ENABLED", "false").strip().lower() == "true"

# ---------------------------------------------------------------------------
# Instrument — NIFTY index on Dhan
# ---------------------------------------------------------------------------
NIFTY_UNDERLYING_SECURITY_ID = 13          # NIFTY 50 index
NIFTY_UNDERLYING_SEGMENT     = "IDX_I"     # index segment
OPTION_EXCHANGE_SEGMENT      = "NSE_FNO"   # where the option contracts trade
LOT_SIZE                     = 65          # NIFTY lot size (effective Jan 2026)
LOTS                         = 1           # how many lots to trade -> quantity = LOTS * LOT_SIZE

# ---------------------------------------------------------------------------
# The strategy rules (from the video)
# ---------------------------------------------------------------------------
TRIGGER_PREMIUM   = 180.0   # the ₹180 breakout level
SL_POINTS         = 20.0    # stop-loss distance below entry  -> 160
TARGET_POINTS     = 40.0    # target distance above entry     -> 220  (1:2 R:R)

# How we pick the strike at 9:25: an ITM strike whose premium is closest to this.
STRIKE_SELECT_TARGET = 180.0

# "Break above 180 AND sustain it." For live/paper, sustain = price stays above
# the trigger for this many seconds. For backtest = the 1-min candle closes above.
SUSTAIN_SECONDS = 15

# ---------------------------------------------------------------------------
# Timing (IST). The whole trade lives inside a 15-30 min window.
# ---------------------------------------------------------------------------
PREP_TIME        = time(9, 25)   # select strikes
ENTRY_START_TIME = time(9, 30)   # start watching for the 180 break
HARD_EXIT_TIME   = time(9, 45)   # beginner rule: close no matter what
ADVANCED_EXIT    = time(10, 0)   # advanced rule: hold till here IF in profit

# ---------------------------------------------------------------------------
# Advanced management (only used when ADVANCED_MODE = True)
# ---------------------------------------------------------------------------
ADVANCED_MODE       = False  # beginners: keep False. Closes everything by 9:45.
TRAIL_TO_COST_TIME  = time(9, 45)  # if profitable at 9:45, move SL to entry (risk-free)

# ---------------------------------------------------------------------------
# Polling
# ---------------------------------------------------------------------------
POLL_SECONDS = 1.0   # how often live/paper engines re-check the two premiums
```

#### File: `backtest_dhan.py`
```python
"""
backtest_dhan.py — run the REAL backtest over Dhan's expired-options data.

For every trading day in the range it auto-picks the ITM CE and PE strike whose
9:25 premium was closest to ₹180, then replays 9:30–9:45 (or 10:00) through the
exact same rule engine paper/live use.

Examples
--------
# last 5 years, full
python backtest_dhan.py --from 2021-06-20 --to 2026-06-20

# a quick 2-month sanity run first (recommended before the full pull)
python backtest_dhan.py --from 2026-04-01 --to 2026-06-01 --depth 5

Needs a FRESH Dhan token in .env and the Data API subscription active.
Data is cached in ./cache/ so re-runs are instant and don't re-bill the API.
"""
import argparse
import csv
import datetime as dt

import config
from dhan_client import DhanClient
from engine_backtest import build_sessions_from_dhan, run_backtest


def _date(s):
    return dt.datetime.strptime(s, "%Y-%m-%d").date()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="frm", required=True, help="YYYY-MM-DD")
    ap.add_argument("--to", dest="to", required=True, help="YYYY-MM-DD")
    ap.add_argument("--depth", type=int, default=5,
                    help="how many ITM strikes deep to scan each side (default 5)")
    ap.add_argument("--out", default="backtest_results.csv")
    ap.add_argument("--cache", default="cache")
    ap.add_argument("--sleep", type=float, default=0.4,
                    help="seconds between API calls (respect rate limits)")
    args = ap.parse_args()

    print("=" * 64)
    print(f" Backtest  {args.frm} → {args.to}   "
          f"(₹{config.TRIGGER_PREMIUM:.0f} trigger, SL "
          f"₹{config.TRIGGER_PREMIUM - config.SL_POINTS:.0f}, target "
          f"₹{config.TRIGGER_PREMIUM + config.TARGET_POINTS:.0f}, "
          f"{config.LOTS} lot = {config.LOTS * config.LOT_SIZE} qty)")
    print("=" * 64)

    dhan = DhanClient()
    sessions = build_sessions_from_dhan(dhan, _date(args.frm), _date(args.to),
                                        depth=args.depth, cache_dir=args.cache,
                                        sleep=args.sleep)
    if not sessions:
        print("No sessions built. Check token, Data API subscription, and dates.")
        return

    r = run_backtest(sessions)

    print("\n" + "-" * 64)
    print(f" Sessions scanned : {r['sessions']}")
    print(f" Trades taken     : {r['trades_taken']}   "
          f"(no-trade days: {r['sessions'] - r['trades_taken']})")
    print(f" Wins / Losses    : {r['wins']} / {r['losses']}")
    print(f" WIN RATE         : {r['win_rate']} %")
    print(f" Total points     : {r['total_points']}")
    print(f" Total ₹          : {r['total_rupees']:,.0f}")
    print(f" Avg / trade      : {r['avg_points']} pts")
    print("-" * 64)

    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "side", "strike_offset", "entry", "exit",
                    "reason", "points", "rupees", "result"])
        for t in r["trades"]:
            w.writerow([t["date"], t.get("side", ""), t.get("strike", ""),
                        t.get("entry", ""), t.get("exit", ""), t.get("reason", ""),
                        t.get("points", 0), t.get("rupees", 0), t["result"]])
    print(f" Per-trade detail written to {args.out}")
    print("\n Reminder: a good backtest number is necessary, not sufficient. "
          "Forward-test in paper mode before going live.")


if __name__ == "__main__":
    main()
```

#### File: `app.py`
```python
"""
app.py — Flask dashboard tying the three engines together.

Run:  python app.py    then open  http://127.0.0.1:5000

Paper is the default and the safe place to live. Live is gated twice (env + UI
confirm). Backtest runs on your CSVs or a built-in synthetic sample so you can
see the rules working with no token.
"""
import threading
import datetime as dt
from flask import Flask, render_template, request, jsonify

import config
from engine_paper import PaperEngine
from engine_live import LiveEngine
from engine_backtest import run_backtest, replay_session

app = Flask(__name__)

_engine = None          # the currently running paper/live engine
_thread = None
_lock = threading.Lock()


def _dhan():
    from dhan_client import DhanClient
    return DhanClient()


@app.route("/")
def index():
    return render_template("index.html",
                           trigger=config.TRIGGER_PREMIUM,
                           sl=config.TRIGGER_PREMIUM - config.SL_POINTS,
                           tgt=config.TRIGGER_PREMIUM + config.TARGET_POINTS,
                           lots=config.LOTS, lot_size=config.LOT_SIZE,
                           live_enabled=config.LIVE_TRADING_ENABLED,
                           advanced=config.ADVANCED_MODE)


@app.route("/api/start", methods=["POST"])
def start():
    global _engine, _thread
    mode = (request.json or {}).get("mode", "paper")
    armed = bool((request.json or {}).get("confirm_live"))
    with _lock:
        if _engine and _engine.snapshot().get("running"):
            return jsonify({"ok": False, "error": "Already running. Stop first."})
        try:
            if mode == "live":
                _engine = LiveEngine(_dhan(), armed=armed)
            else:
                _engine = PaperEngine(_dhan())
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)})
        _thread = threading.Thread(target=_engine.run, daemon=True)
        _thread.start()
    return jsonify({"ok": True, "mode": mode})


@app.route("/api/stop", methods=["POST"])
def stop():
    with _lock:
        if _engine:
            _engine.stop()
    return jsonify({"ok": True})


@app.route("/api/status")
def status():
    with _lock:
        if not _engine:
            return jsonify({"phase": "idle", "running": False,
                            "message": "Pick a mode and press Start."})
        return jsonify(_engine.snapshot())


@app.route("/api/backtest/sample", methods=["POST"])
def backtest_sample():
    """Synthetic 10-session backtest so you can see the engine work with no token."""
    import random
    random.seed(7)
    sessions = []
    base = dt.date(2026, 6, 1)
    for d in range(10):
        date = base + dt.timedelta(days=d)
        ce, pe = _synthetic_series(date, random)
        sessions.append({"date": date, "ce_series": ce, "pe_series": pe,
                         "ce_strike": 24800, "pe_strike": 25000})
    return jsonify(run_backtest(sessions))


def _synthetic_series(date, rng):
    """
    A plausible 9:29–10:01 minute path for a CE and PE around ₹176, with enough
    volatility that some sessions hit the +40 target, some the -20 SL, and some
    time out — so the sample shows a realistic mix, not a fake 100% win rate.
    """
    start = dt.datetime.combine(date, dt.time(9, 29))
    ce_p, pe_p = 176.0, 176.0
    ce, pe = [], []
    breaker = rng.choice(["CE", "PE", "none"])  # sometimes neither breaks cleanly
    # after breaking, the move may continue (winner) or reverse (loser)
    follow = rng.random() < 0.62
    for i in range(33):
        t = start + dt.timedelta(minutes=i)
        bias_ce = (3.0 if breaker == "CE" else -1.5) if i < 4 else \
                  ((4.0 if follow else -5.0) if breaker == "CE" else -1.5)
        bias_pe = (3.0 if breaker == "PE" else -1.5) if i < 4 else \
                  ((4.0 if follow else -5.0) if breaker == "PE" else -1.5)
        ce_p = max(30, ce_p + bias_ce + rng.uniform(-4, 4))
        pe_p = max(30, pe_p + bias_pe + rng.uniform(-4, 4))
        ce.append(_candle(t, ce_p, rng))
        pe.append(_candle(t, pe_p, rng))
    return ce, pe


def _candle(t, mid, rng):
    spread = rng.uniform(1.0, 4.0)
    o = mid + rng.uniform(-spread, spread)
    c = mid + rng.uniform(-spread, spread)
    return {"time": t, "open": round(o, 1), "high": round(max(o, c) + spread, 1),
            "low": round(min(o, c) - spread, 1), "close": round(c, 1)}


if __name__ == "__main__":
    print("=" * 60)
    print(" 9:30 AM Nifty premium strategy  —  http://127.0.0.1:5000")
    print(f" Trigger ₹{config.TRIGGER_PREMIUM:.0f} | SL "
          f"₹{config.TRIGGER_PREMIUM - config.SL_POINTS:.0f} | "
          f"Target ₹{config.TRIGGER_PREMIUM + config.TARGET_POINTS:.0f} | "
          f"{config.LOTS} lot ({config.LOTS * config.LOT_SIZE} qty)")
    print(f" Live trading enabled: {config.LIVE_TRADING_ENABLED}")
    print("=" * 60)
    app.run(host="127.0.0.1", port=5000, debug=False, threaded=True)
```

#### File: `engine_live.py`
```python
"""
engine_live.py — LIVE trading. Places REAL Dhan Super Orders with real money.

Guards (all must pass before a single order goes out):
  1. config.LIVE_TRADING_ENABLED must be True (set in .env)
  2. the caller must pass armed=True (the web UI sets this only after you confirm)

The Super Order carries entry + target + stop-loss to the exchange, so your SL
is safe even if this process dies. The app still watches the clock for the 9:45 /
10:00 time exits and the trail-to-cost rule.
"""
import time
from engine_base import EngineBase, now_ist
from strategy import select_strikes
import config


class LiveEngine(EngineBase):
    mode = "live"

    def __init__(self, dhan, armed: bool = False):
        super().__init__()
        self.dhan = dhan
        self.armed = armed
        self.order_id = None

    def _can_trade(self) -> (bool, str):
        if not config.LIVE_TRADING_ENABLED:
            return False, "LIVE_TRADING_ENABLED is false in .env. Live disabled."
        if not self.armed:
            return False, "Live engine not armed. Confirm in the UI to arm."
        return True, ""

    def run(self):
        ok, why = self._can_trade()
        if not ok:
            self._push(phase="blocked", running=False, message=why)
            return

        self._push(running=True, phase="prep", message="Fetching option chain…")
        try:
            expiry = self.dhan.nearest_weekly_expiry()
            spot, rows = self.dhan.option_chain(expiry)
            self.state.strikes = select_strikes(rows, spot)
            if "CE" not in self.state.strikes or "PE" not in self.state.strikes:
                self._push(phase="error", running=False,
                           message="Could not find ITM strikes near ₹180.")
                return
            self._push(phase="watch", spot=spot, strikes=self._strikes_for_status(),
                       message=f"LIVE — watching for ₹{config.TRIGGER_PREMIUM:.0f} break")
        except Exception as e:
            self._push(phase="error", running=False, message=f"Setup failed: {e}")
            return

        sids = {s: c.security_id for s, c in self.state.strikes.items()}
        trailed = False

        while not self._stop.is_set() and not self.state.finished:
            now = now_ist()
            try:
                quotes = self.dhan.ltp(list(sids.values()))
            except Exception as e:
                self._push(message=f"Quote error (retrying): {e}")
                time.sleep(config.POLL_SECONDS)
                continue

            ltps = {s: quotes.get(sid) for s, sid in sids.items()}
            self._push(ltps={s: v for s, v in ltps.items() if v is not None})

            # ENTRY — place the real super order the instant the brain says go
            if self.state.position is None:
                before = self.state.position
                self.state.check_entry(now, {k: v for k, v in ltps.items() if v})
                if self.state.position is not None and before is None:
                    p = self.state.position
                    try:
                        resp = self.dhan.place_super_order(
                            security_id=p.security_id, qty=p.qty,
                            entry=p.entry, target=p.target, stop_loss=p.stop_loss)
                        self.order_id = (resp.get("data", {}) or {}).get("orderId") \
                            or resp.get("orderId")
                        self.state.log.append(
                            f"{now.strftime('%H:%M:%S')}  REAL super order sent "
                            f"(id {self.order_id})")
                    except Exception as e:
                        self.state.log.append(
                            f"{now.strftime('%H:%M:%S')}  ORDER FAILED: {e}")
                        self._push(phase="error", running=False,
                                   message=f"Order failed: {e}")
                        return

            # MANAGE — broker holds target/SL; we own the clock + trail
            else:
                live = ltps.get(self.state.position.side)
                if live:
                    p = self.state.position
                    # trail to cost
                    if (config.ADVANCED_MODE and not trailed and self.order_id
                            and now.time() >= config.TRAIL_TO_COST_TIME
                            and live > p.entry):
                        try:
                            self.dhan.modify_super_order_sl(self.order_id, p.entry)
                            trailed = True
                            self.state.log.append(
                                f"{now.strftime('%H:%M:%S')}  SL trailed to cost "
                                f"({p.entry:.1f})")
                        except Exception as e:
                            self.state.log.append(f"trail failed: {e}")
                    # time exit -> cancel super order legs and we're flat
                    self.state.manage(now, live)
                    if self.state.finished and self.order_id:
                        try:
                            self.dhan.cancel_super_order(self.order_id)
                        except Exception:
                            pass
                    self._push(pnl=round(p.pnl_at(live), 0))

            self._push(phase="manage" if self.state.position else "watch")
            time.sleep(config.POLL_SECONDS)

        self._push(running=False, phase="done", message="Live session over.")
```


==================================================
