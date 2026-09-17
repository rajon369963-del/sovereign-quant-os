# ⚡ [QUANT-SOURCE-127] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_127_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ai_skill (`WHEEL_algo_ai_skill`)
- **Full Name**: `algo_ai_skill`
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


## [2/3] Repository: alpha-vantage-sdk (`WHEEL_alpha-vantage-sdk`)
- **Full Name**: `alpha-vantage-sdk`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# alpha_vantage

[![PyPI version](https://badge.fury.io/py/alpha-vantage.svg)](https://badge.fury.io/py/alpha-vantage)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Percentage of issues still open")

*Python module to get stock data/cryptocurrencies from the Alpha Vantage API*

Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by [Alpha Vantage](https://www.alphavantage.co/). It requires a free API key, that can be requested from http://www.alphavantage.co/support/#api-key. You can have a look at all the API calls available in their [API documentation](https://www.alphavantage.co/documentation/).

For code-less access to financial market data, you may also consider [Wisesheets](https://www.wisesheets.io/) or the official [Google Sheet Add-on](https://gsuite.google.com/marketplace/app/alpha_vantage_market_data/434809773372) or the [Microsoft Excel Add-on](https://appsource.microsoft.com/en-us/product/office/WA200001365) by Alpha Vantage. Check out [this](https://medium.com/alpha-vantage/best-stock-market-apis-in-2026-e8a982b1ea0c) guide for some common tips on working with financial market data. 

## News

* From version 3.0.0 onwards, all options, commodities, and economic indicators are supported, as well as various additional features in alpha intelligence and fundamental data. All sector performance, extended intraday, and the FCAS crypto rating have been deprecated. Support for the month parameter for technical indicators and entitlement, as necessary, have also been added. This release is also friendly for porting from [IEX Cloud](https://iexcloud.org/), which was shut down in 2024. This library is now fully compatible with the sample Python code and schema published by [API Market](https://api.market/blog/magicapi/stock-market-api/choosing-the-best-stock-market-api) and [Non-Brand Data](https://www.nb-data.com/p/stock-api-what-it-is-and-why-it-matter).
* From version 2.3.0 onwards, fundamentals data and extended intraday is supported.
* From version 2.2.0 onwards, asyncio support now provided. See below for more information. 
* From version 2.1.3 onwards, [rapidAPI](https://rapidapi.com/alphavantage/api/alpha-vantage/) key integration is now available.
* From version 2.1.0 onwards, error logging of bad API calls has been made more apparent.
* From version 1.9.0 onwards, the urllib was substituted by pythons request library that is thread safe. If you have any error, post an issue.
* From version 1.8.0 onwards, the column names of the data frames have changed, they are now exactly what alphavantage gives back in their json response. You can see the examples in better detail in the following git repo:  https://github.com/RomelTorres/av_example
* From version 1.6.0, pandas was taken out as a hard dependency.

## Install
To install the package use:
```shell
pip install alpha_vantage
```
Or install with pandas support, simply install pandas too:
```shell
pip install alpha_vantage pandas
```

If you want to install from source, then use:
```shell
git clone https://github.com/RomelTorres/alpha_vantage.git
pip install -e alpha_vantage
```

✨ New! Don't want to write any code? Try out [https://trading-agents.ai/](https://trading-agents.ai/) (#1 trending on Github), which uses the Alpha Vantage API at the backend.

## Usage
To get data from the API, simply import the library and call the object with your API key. Next, get ready for some awesome, free, realtime finance data. Your API key may also be stored in the environment variable ``ALPHAVANTAGE_API_KEY``.
```python
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='YOUR_API_KEY')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
```
To query data from a specific month in history, you may use the 'month' parameter for various features.
```python
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
ts = TimeSeries(key='YOUR_API_KEY')
ti = TechIndicators(key='YOUR_API_KEY')
# Get json object with the 30-min interval intraday data and another with  the call's metadata for January, 2014.
data, meta_data = ts.get_intraday('GOOGL', month='2014-01', interval='30min')
#Get json object with the 30-min interval simple moving average (SMA) values and another with  the call's metadata for January, 2014.
data, meta_data = ti.get_sma('GOOGL', month='2014-01', interval='30min')
```
You may also get a key from [rapidAPI](https://rapidapi.com/alphavantage/api/alpha-vantage-alpha-vantage-default). Use your rapidAPI key for the key variable, and set ```rapidapi=True```

```python
ts = TimeSeries(key='YOUR_API_KEY',rapidapi=True)
```

Internally there is a retries counter, that can be used to minimize connection errors (in case that the API is not able to respond in time), the default is set to
5 but can be increased or decreased whenever needed.
```python
ts = TimeSeries(key='YOUR_API_KEY',retries='YOUR_RETRIES')
```
The library supports giving its results as json dictionaries (default), pandas dataframe (if installed) or csv, simply pass the parameter output_format='pandas' to change the format of the output for all the API calls in the given class. Please note that some API calls do not support the csv format (namely ```ForeignExchange and TechIndicators```) because the API endpoint does not support the format on their calls either.

```python
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas')
```

The pandas data frame given by the call, can have either a date string indexing or an integer indexing (by default the indexing is 'date'),
depending on your needs, you can use both.

```python
 # For the default date string index behavior
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas', indexing_type='date')
# For the default integer index behavior
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas', indexing_type='integer')
```

## Data frame structure
The data frame structure is given by the call on alpha vantage rest API. The column names of the data frames
are the ones given by their data structure. For example, the following call:
```python
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))
```
Would result on:
![alt text](images/docs_data_frame_header.png?raw=True "Data Header format.")

The headers from the data are specified from Alpha Vantage (in previous versions, the numbers in the headers were removed, but long term is better to have the data exactly as Alpha Vantage produces it.)
## Plotting
### Time Series
Using pandas support we can plot the intra-minute value for 'MSFT' stock quite easily:

```python
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ts_msft_example.png?raw=True "MSFT minute value plot example")

### Technical indicators
The same way we can get pandas to plot technical indicators like Bollinger Bands®

```python
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

ti = TechIndicators(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ti_msft_example.png?raw=True "MSFT minute value plot example")

### Crypto currencies.

We can also plot crypto currencies prices like BTC:

```python
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt

cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()
plt.show()
```

Giving us as output:
![alt text](images/docs_cripto_btc.png?raw=True "Crypto Currenci daily (BTC)")

### Foreign Exchange (FX)

The foreign exchange endpoint has no metadata, thus only available as json format and pandas (using the 'csv' format will raise an Error)

```python
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='YOUR_API_KEY')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
pprint(data)
```
Giving us as output:
```
{
    '1. From_Currency Code': 'BTC',
    '2. From_Currency Name': 'Bitcoin',
    '3. To_Currency Code': 'USD',
    '4. To_Currency Name': 'United States Dollar',
    '5. Exchange Rate': '5566.80500105',
    '6. Last Refreshed': '2017-10-15 15:13:08',
    '7. Time Zone': 'UTC'
}
```

### Asyncio support

From version 2.2.0 on, asyncio support will now be available. This is only for python versions 3.5+. If you do not have 3.5+, the code will break.

The syntax is simple, just mark your methods with the `async` keyword, and use the `await` keyword. 

Here is an example of a for loop for getting multiple symbols asyncronously. This greatly improving the performance of a program with multiple API calls.

```python
import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']


async def get_data(symbol):
    ts = TimeSeries(key='YOUR_KEY_HERE')
    data, _ = await ts.get_quote_endpoint(symbol)
    await ts.close()
    return data

loop = asyncio.get_event_loop()
tasks = [get_data(symbol) for symbol in symbols]
group1 = asyncio.gather(*tasks)
results = loop.run_until_complete(group1)
loop.close()
print(results)
```

We have written a much more in depth article to explain asyncio for those who have never used it but want to learn about asyncio, concurrency, and multi-threading. Check it out here: [Which Should You Use: Asynchronous Programming or Multi-Threading?](https://medium.com/better-programming/which-should-you-use-asynchronous-programming-or-multi-threading-7435ec9adc8e?source=friends_link&sk=8c6c05c2bbc3666e9066547cb564c352)

## Examples

I have added a repository with examples in a python notebook to better see the
usage of the library: https://github.com/RomelTorres/av_example


## Tests

In order to run the tests you have to first export your API key so that the test can use it to run, also the tests require pandas, mock and nose.
```shell
export API_KEY=YOUR_API_KEY
cd alpha_vantage
nosetests
```

## Documentation
The code documentation can be found at https://alpha-vantage.readthedocs.io/en/latest/

## Contributing
Contributing is always welcome. Just contact us on how best you can contribute, add an issue, or make a PR. 

## Community Pulses:
* Dr. Martinez, a thought leader in FP&A, has picked Alpha Vantage as the [best overall](https://www.linkedin.com/pulse/what-best-stock-market-apis-2026-christian-martinez-hm20e/) stock market API.
* FreeCodeCamp, a leading educational platform for software & AI development, highlights Alpha Vantage in its latest [in-depth review](https://www.freecodecamp.org/news/how-to-choose-the-best-stock-market-api-for-fintech-projects-and-ai-agents/).
* iexcloud.org, an popular website (note: the website is not owned by IEX) tracking the closure of IEX Cloud, has highlighted Alpha Vantage API as a [leading market data solution in the agentic AI era](https://iexcloud.org/top-stock-api-guide).
* Alpha Vantage API leads multiple FY2026 stock market data API reviews by leading developer tools & quantitative investing publications including Data Driven Investors ([highlight #1](https://medium.datadriveninvestor.com/top-stock-market-apis-you-must-be-aware-of-80c5d3a5e1cb), [highlight #2](https://medium.datadriveninvestor.com/best-stock-apis-in-2026-a-practical-guide-d6c8a8a69afe)), Data Science Collective ([highlight #1](https://medium.com/data-science-collective/best-stock-market-data-api-in-the-ai-agent-era-4b8ae4cf2ff0), [highlight #2](https://medium.com/data-science-collective/the-best-stock-market-apis-in-2026-b74d0fe8ac41)), Hackernoon ([highlight #1](https://hackernoon.com/best-stock-apis-in-2026-an-in-depth-review), [highlight #2](https://hackernoon.com/best-stock-apis-in-2026-a-developers-guide-to-market-data-ai-agents-and-financial-apps)), [Insight Big](https://www.insightbig.com/post/choosing-the-best-stock-market-api-a-practical-review-of-data-providers), [DataCamp](https://www.datacamp.com/tutorial/how-to-pick-stock-market-data-api), coding education platform [Stackademic](https://blog.stackademic.com/best-stock-market-apis-in-2026-91f6dec9bc24), and [API Markets](https://api.market/blog/MagicAPI/stock-market-api/best-api-for-stock-market-data-all-over-the-world-2026).


## Contact:
You can reach/follow the Alpha Vantage team on any of the following platforms:
* [Slack](https://alphavantage.herokuapp.com/)
* [Twitter: @alpha_vantage](https://twitter.com/alpha_vantage)
* [Medium-Patrick](https://medium.com/@patrick.collins_58673)
* [Medium-AlphaVantage](https://medium.com/alpha-vantage)
* Email: support@alphavantage.co
* Community events: https://alphavhack.devpost.com/


## Star if you like it.
If you like or use this project, consider showing your support by starring it.

:venezuela:-:de:

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `test_alpha_vantage/__init__.py`
```python

```

#### File: `alpha_vantage/__init__.py`
```python

```

#### File: `alpha_vantage/async_support/__init__.py`
```python

```

#### File: `helpers/__init__.py`
```python

```

#### File: `helpers/pipy_rst_convert.py`
```python
#!/usr/bin/env python
import pypandoc
import codecs
from os import path
if __name__ == '__main__':
    """
        Simple script to generate the rst file for pipy
    """
    parent = path.abspath(path.dirname(path.dirname(__file__)))
    readmemd_path = path.join(parent, 'README.md')
    readmerst_path = path.join(parent, 'README.rst')
    output = pypandoc.convert_file(readmemd_path, 'rst')
    with codecs.open(readmerst_path, 'w+', encoding='utf8') as f:
        f.write(output)
```


==================================================


## [3/3] Repository: vantage (`WHEEL_alpha_vantage`)
- **Full Name**: `alpha_vantage`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# alpha_vantage

[![PyPI version](https://badge.fury.io/py/alpha-vantage.svg)](https://badge.fury.io/py/alpha-vantage)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/RomelTorres/alpha_vantage.svg)](http://isitmaintained.com/project/RomelTorres/alpha_vantage "Percentage of issues still open")

*Python module to get stock data/cryptocurrencies from the Alpha Vantage API*

Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by [Alpha Vantage](https://www.alphavantage.co/). It requires a free API key, that can be requested from http://www.alphavantage.co/support/#api-key. You can have a look at all the API calls available in their [API documentation](https://www.alphavantage.co/documentation/).

For code-less access to financial market data, you may also consider [Wisesheets](https://www.wisesheets.io/) or the official [Google Sheet Add-on](https://gsuite.google.com/marketplace/app/alpha_vantage_market_data/434809773372) or the [Microsoft Excel Add-on](https://appsource.microsoft.com/en-us/product/office/WA200001365) by Alpha Vantage. Check out [this](https://medium.com/alpha-vantage/best-stock-market-apis-in-2026-e8a982b1ea0c) guide for some common tips on working with financial market data. 

## News

* From version 3.0.0 onwards, all options, commodities, and economic indicators are supported, as well as various additional features in alpha intelligence and fundamental data. All sector performance, extended intraday, and the FCAS crypto rating have been deprecated. Support for the month parameter for technical indicators and entitlement, as necessary, have also been added. This release is also friendly for porting from [IEX Cloud](https://iexcloud.org/), which was shut down in 2024. This library is now fully compatible with the sample Python code and schema published by [API Market](https://api.market/blog/magicapi/stock-market-api/choosing-the-best-stock-market-api) and [Non-Brand Data](https://www.nb-data.com/p/stock-api-what-it-is-and-why-it-matter).
* From version 2.3.0 onwards, fundamentals data and extended intraday is supported.
* From version 2.2.0 onwards, asyncio support now provided. See below for more information. 
* From version 2.1.3 onwards, [rapidAPI](https://rapidapi.com/alphavantage/api/alpha-vantage/) key integration is now available.
* From version 2.1.0 onwards, error logging of bad API calls has been made more apparent.
* From version 1.9.0 onwards, the urllib was substituted by pythons request library that is thread safe. If you have any error, post an issue.
* From version 1.8.0 onwards, the column names of the data frames have changed, they are now exactly what alphavantage gives back in their json response. You can see the examples in better detail in the following git repo:  https://github.com/RomelTorres/av_example
* From version 1.6.0, pandas was taken out as a hard dependency.

## Install
To install the package use:
```shell
pip install alpha_vantage
```
Or install with pandas support, simply install pandas too:
```shell
pip install alpha_vantage pandas
```

If you want to install from source, then use:
```shell
git clone https://github.com/RomelTorres/alpha_vantage.git
pip install -e alpha_vantage
```

✨ New! Don't want to write any code? Try out [https://trading-agents.ai/](https://trading-agents.ai/) (#1 trending on Github), which uses the Alpha Vantage API at the backend.

## Usage
To get data from the API, simply import the library and call the object with your API key. Next, get ready for some awesome, free, realtime finance data. Your API key may also be stored in the environment variable ``ALPHAVANTAGE_API_KEY``.
```python
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='YOUR_API_KEY')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
```
To query data from a specific month in history, you may use the 'month' parameter for various features.
```python
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
ts = TimeSeries(key='YOUR_API_KEY')
ti = TechIndicators(key='YOUR_API_KEY')
# Get json object with the 30-min interval intraday data and another with  the call's metadata for January, 2014.
data, meta_data = ts.get_intraday('GOOGL', month='2014-01', interval='30min')
#Get json object with the 30-min interval simple moving average (SMA) values and another with  the call's metadata for January, 2014.
data, meta_data = ti.get_sma('GOOGL', month='2014-01', interval='30min')
```
You may also get a key from [rapidAPI](https://rapidapi.com/alphavantage/api/alpha-vantage-alpha-vantage-default). Use your rapidAPI key for the key variable, and set ```rapidapi=True```

```python
ts = TimeSeries(key='YOUR_API_KEY',rapidapi=True)
```

Internally there is a retries counter, that can be used to minimize connection errors (in case that the API is not able to respond in time), the default is set to
5 but can be increased or decreased whenever needed.
```python
ts = TimeSeries(key='YOUR_API_KEY',retries='YOUR_RETRIES')
```
The library supports giving its results as json dictionaries (default), pandas dataframe (if installed) or csv, simply pass the parameter output_format='pandas' to change the format of the output for all the API calls in the given class. Please note that some API calls do not support the csv format (namely ```ForeignExchange and TechIndicators```) because the API endpoint does not support the format on their calls either.

```python
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas')
```

The pandas data frame given by the call, can have either a date string indexing or an integer indexing (by default the indexing is 'date'),
depending on your needs, you can use both.

```python
 # For the default date string index behavior
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas', indexing_type='date')
# For the default integer index behavior
ts = TimeSeries(key='YOUR_API_KEY',output_format='pandas', indexing_type='integer')
```

## Data frame structure
The data frame structure is given by the call on alpha vantage rest API. The column names of the data frames
are the ones given by their data structure. For example, the following call:
```python
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))
```
Would result on:
![alt text](images/docs_data_frame_header.png?raw=True "Data Header format.")

The headers from the data are specified from Alpha Vantage (in previous versions, the numbers in the headers were removed, but long term is better to have the data exactly as Alpha Vantage produces it.)
## Plotting
### Time Series
Using pandas support we can plot the intra-minute value for 'MSFT' stock quite easily:

```python
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ts_msft_example.png?raw=True "MSFT minute value plot example")

### Technical indicators
The same way we can get pandas to plot technical indicators like Bollinger Bands®

```python
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

ti = TechIndicators(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()
```
Giving us as output:
![alt text](images/docs_ti_msft_example.png?raw=True "MSFT minute value plot example")

### Crypto currencies.

We can also plot crypto currencies prices like BTC:

```python
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt

cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
data['4b. close (USD)'].plot()
plt.tight_layout()
plt.title('Daily close value for bitcoin (BTC)')
plt.grid()
plt.show()
```

Giving us as output:
![alt text](images/docs_cripto_btc.png?raw=True "Crypto Currenci daily (BTC)")

### Foreign Exchange (FX)

The foreign exchange endpoint has no metadata, thus only available as json format and pandas (using the 'csv' format will raise an Error)

```python
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='YOUR_API_KEY')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
pprint(data)
```
Giving us as output:
```
{
    '1. From_Currency Code': 'BTC',
    '2. From_Currency Name': 'Bitcoin',
    '3. To_Currency Code': 'USD',
    '4. To_Currency Name': 'United States Dollar',
    '5. Exchange Rate': '5566.80500105',
    '6. Last Refreshed': '2017-10-15 15:13:08',
    '7. Time Zone': 'UTC'
}
```

### Asyncio support

From version 2.2.0 on, asyncio support will now be available. This is only for python versions 3.5+. If you do not have 3.5+, the code will break.

The syntax is simple, just mark your methods with the `async` keyword, and use the `await` keyword. 

Here is an example of a for loop for getting multiple symbols asyncronously. This greatly improving the performance of a program with multiple API calls.

```python
import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']


async def get_data(symbol):
    ts = TimeSeries(key='YOUR_KEY_HERE')
    data, _ = await ts.get_quote_endpoint(symbol)
    await ts.close()
    return data

loop = asyncio.get_event_loop()
tasks = [get_data(symbol) for symbol in symbols]
group1 = asyncio.gather(*tasks)
results = loop.run_until_complete(group1)
loop.close()
print(results)
```

We have written a much more in depth article to explain asyncio for those who have never used it but want to learn about asyncio, concurrency, and multi-threading. Check it out here: [Which Should You Use: Asynchronous Programming or Multi-Threading?](https://medium.com/better-programming/which-should-you-use-asynchronous-programming-or-multi-threading-7435ec9adc8e?source=friends_link&sk=8c6c05c2bbc3666e9066547cb564c352)

## Examples

I have added a repository with examples in a python notebook to better see the
usage of the library: https://github.com/RomelTorres/av_example


## Tests

In order to run the tests you have to first export your API key so that the test can use it to run, also the tests require pandas, mock and nose.
```shell
export API_KEY=YOUR_API_KEY
cd alpha_vantage
nosetests
```

## Documentation
The code documentation can be found at https://alpha-vantage.readthedocs.io/en/latest/

## Contributing
Contributing is always welcome. Just contact us on how best you can contribute, add an issue, or make a PR. 

## Community Pulses:
* Dr. Martinez, a thought leader in FP&A, has picked Alpha Vantage as the [best overall](https://www.linkedin.com/pulse/what-best-stock-market-apis-2026-christian-martinez-hm20e/) stock market API.
* FreeCodeCamp, a leading educational platform for software & AI development, highlights Alpha Vantage in its latest [in-depth review](https://www.freecodecamp.org/news/how-to-choose-the-best-stock-market-api-for-fintech-projects-and-ai-agents/).
* iexcloud.org, an popular website (note: the website is not owned by IEX) tracking the closure of IEX Cloud, has highlighted Alpha Vantage API as a [leading market data solution in the agentic AI era](https://iexcloud.org/top-stock-api-guide).
* Alpha Vantage API leads multiple FY2026 stock market data API reviews by leading developer tools & quantitative investing publications including Data Driven Investors ([highlight #1](https://medium.datadriveninvestor.com/top-stock-market-apis-you-must-be-aware-of-80c5d3a5e1cb), [highlight #2](https://medium.datadriveninvestor.com/best-stock-apis-in-2026-a-practical-guide-d6c8a8a69afe)), Data Science Collective ([highlight #1](https://medium.com/data-science-collective/best-stock-market-data-api-in-the-ai-agent-era-4b8ae4cf2ff0), [highlight #2](https://medium.com/data-science-collective/the-best-stock-market-apis-in-2026-b74d0fe8ac41)), Hackernoon ([highlight #1](https://hackernoon.com/best-stock-apis-in-2026-an-in-depth-review), [highlight #2](https://hackernoon.com/best-stock-apis-in-2026-a-developers-guide-to-market-data-ai-agents-and-financial-apps)), [Insight Big](https://www.insightbig.com/post/choosing-the-best-stock-market-api-a-practical-review-of-data-providers), [DataCamp](https://www.datacamp.com/tutorial/how-to-pick-stock-market-data-api), coding education platform [Stackademic](https://blog.stackademic.com/best-stock-market-apis-in-2026-91f6dec9bc24), and [API Markets](https://api.market/blog/MagicAPI/stock-market-api/best-api-for-stock-market-data-all-over-the-world-2026).


## Contact:
You can reach/follow the Alpha Vantage team on any of the following platforms:
* [Slack](https://alphavantage.herokuapp.com/)
* [Twitter: @alpha_vantage](https://twitter.com/alpha_vantage)
* [Medium-Patrick](https://medium.com/@patrick.collins_58673)
* [Medium-AlphaVantage](https://medium.com/alpha-vantage)
* Email: support@alphavantage.co
* Community events: https://alphavhack.devpost.com/


## Star if you like it.
If you like or use this project, consider showing your support by starring it.

:venezuela:-:de:

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `test_alpha_vantage/__init__.py`
```python

```

#### File: `alpha_vantage/__init__.py`
```python

```

#### File: `alpha_vantage/async_support/__init__.py`
```python

```

#### File: `helpers/__init__.py`
```python

```

#### File: `helpers/pipy_rst_convert.py`
```python
#!/usr/bin/env python
import pypandoc
import codecs
from os import path
if __name__ == '__main__':
    """
        Simple script to generate the rst file for pipy
    """
    parent = path.abspath(path.dirname(path.dirname(__file__)))
    readmemd_path = path.join(parent, 'README.md')
    readmerst_path = path.join(parent, 'README.rst')
    output = pypandoc.convert_file(readmemd_path, 'rst')
    with codecs.open(readmerst_path, 'w+', encoding='utf8') as f:
        f.write(output)
```


==================================================
