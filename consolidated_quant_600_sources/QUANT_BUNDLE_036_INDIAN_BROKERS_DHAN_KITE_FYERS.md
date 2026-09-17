# ⚡ [QUANT-SOURCE-036] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_036_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Finstreet (`PHASE4-QUANT-080`)
- **Full Name**: `PHASE4-QUANT-080_beingamanforever__Finstreet`
- **Description**: Algorithmic trading engine for NSE. Regime-Adaptive Ensemble ML (XGBoost + LightGBM). Features automated bias auditing (CI/CD), Triple-Barrier Labeling, and dynamic risk management
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">

# Finstreet Trading System

**ML-Driven Trend-Following Strategy for NSE Equities**


[![Strategy Audit](https://github.com/beingamanforever/Finstreet/actions/workflows/sanity_check.yml/badge.svg)](https://github.com/beingamanforever/Finstreet/actions/workflows/sanity_check.yml)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-FFC107?style=for-the-badge)](LICENSE)

</div>

---

### Performance Summary

| Win Rate | Sharpe Ratio | Total Return | Max Drawdown | Profit Factor |
|:--------:|:------------:|:------------:|:------------:|:-------------:|
| **88.9%** | **6.62** | **1.31%** | **0.05%** | **29.27** |

*9 trades · NSE:SONATSOFTW-EQ · Nov-Dec 2025 · INR 100,000 → INR 101,314*

</div>

---

## Methodology

### Data Pipeline

```
Warmup:     Jan 1 - Oct 31, 2025 (indicators only, no training)
Training:   Nov 1 - Dec 31, 2025
Prediction: Jan 1 - 8, 2026 (out-of-sample)
```

- Triple-barrier labeling with T+2 to T+5 forward returns
- Walk-forward cross-validation
- Data integrity verified via `audit_bias.py`

### Strategy Logic

| Step | Action |
|------|--------|
| Trend ID | EMA(10)/SMA(20) crossover + ADX strength |
| Entry | Wait for 6% pullback within trend |
| Validate | ML ensemble confirms direction |
| Size | Scale position by confidence |
| Exit | ATR-based stops (1.5x SL, 3x TP) |

### Risk Controls

| Control | Rule |
|---------|------|
| Position Size | `risk = base_risk * (confidence / 0.70)` |
| Max Position | 15% of capital |
| Stop Loss | 1.5x ATR (EOD exit if not hit) |
| Regime Filter | ADX < 15 → skip trade |
| Signal Gate | Technical + ML must align |

---

## Results

### Backtest Metrics (Nov-Dec 2025)

| Metric | Value | Metric | Value |
|--------|------:|--------|------:|
| Total Trades | 9 | Win Rate | 88.9% |
| Winners | 8 | Sharpe Ratio | 6.62 |
| Losers | 1 | Calmar Ratio | 180.43 |
| Avg Win | INR 170 | Profit Factor | 29.27 |
| Avg Loss | INR 46 | Max Drawdown | 0.05% |

*All trades exited at EOD (daily bars); stop/target rarely reached intraday.*

### Equity Curve
<img src="reports/figures/equity_drawdown_dual.png" width="800">

### Trade Execution
<img src="reports/figures/price_with_trades.png" width="800">

### Trade Distribution
<img src="reports/figures/trade_distribution.png" width="600">

### Model Performance

<img src="reports/figures/confusion_matrix.png" width="450"> <img src="reports/figures/feature_importance.png" width="450">

**Feature Importance:** Volatility features dominate (ATR z-score: 39%, ATR percentile: 28%, returns_std: 20%). The model identifies *regime conditions* rather than predicting direction directly.

---

## Forward Predictions (Jan 1-8, 2026)

| Date | Signal | Direction | Confidence | Regime |
|:----:|:------:|:---------:|:----------:|:------:|
| Jan 1 | HOLD | DOWN | 77.6% | Uptrend Strong |
| Jan 2 | HOLD | DOWN | 77.6% | Uptrend Strong |
| Jan 5 | HOLD | DOWN | 54.6% | Transitional |
| Jan 6 | HOLD | DOWN | 54.6% | Uptrend Weak |
| Jan 7 | HOLD | DOWN | 54.6% | Transitional |
| Jan 8 | HOLD | DOWN | 50.4% | Transitional |

<img src="reports/figures/predictions_chart.png" width="700">

**Signal Logic:** All HOLD signals because ML predicts DOWN while regime shows Uptrend/Transitional. Conservative approach preserves capital rather than betting against trend.

---

## Quick Start

### Option 1: Local Setup (Recommended)

```bash
# Clone repository
git clone <repository>
cd finstreet

# Run automated setup
chmod +x setup.sh
./setup.sh

# Activate environment
source venv/bin/activate

# Run full pipeline
python run.py all
```

The `setup.sh` script automatically:
- Creates Python virtual environment
- Installs all dependencies from `requirements.txt`
- Creates necessary directories (`data/`, `models/`, `reports/`)
- Generates `.env` template for FYERS API credentials

### Option 2: Docker

```bash
# Build image
docker build -t finstreet .

# Run full pipeline (mount volumes for output)
docker run -v $(pwd)/data:/app/data -v $(pwd)/reports:/app/reports finstreet all

# Run specific commands
docker run -v $(pwd)/data:/app/data finstreet backtest
docker run -v $(pwd)/reports:/app/reports finstreet visualize
docker run finstreet predict
```

The `Dockerfile` provides:
- Multi-stage build for optimized image size
- Python 3.11 slim base image
- All dependencies pre-installed
- Health check for container monitoring

### Available Commands

```bash
python run.py fetch      # Fetch data from FYERS API
python run.py train      # Train XGBoost model only
python run.py ensemble   # Train XGBoost + LightGBM ensemble
python run.py backtest   # Run backtest simulation
python run.py predict    # Generate Jan 1-8 predictions
python run.py visualize  # Create performance charts
python run.py all        # Full pipeline
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      TRADING PIPELINE                           │
├─────────────────────────────────────────────────────────────────┤
│  FYERS API ──► Features ──► ML Ensemble ──► Signal Gate ──► Trade
│      │            │              │              │             │
│   OHLCV        RSI, MACD      XGBoost +     Tech + ML      Risk
│   Daily        ADX, ATR       LightGBM      Aligned       Mgmt
│                KER, Z-Score    (60/40)                       │
└─────────────────────────────────────────────────────────────────┘
```

## Project Structure

```
finstreet/
├── run.py                  # Entry point
├── audit_bias.py           # Data leakage verification
├── sensitivity_analysis.py # Parameter robustness testing
├── Dockerfile              # Container configuration
├── setup.sh                # Local setup script
├── requirements.txt        # Python dependencies
├── config/settings.py      # Configuration
├── src/
│   ├── data/               # FYERS API integration
│   ├── features/           # Technical indicators, preprocessing
│   ├── model/              # XGBoost + LightGBM ensemble
│   ├── strategy/           # Trading logic
│   ├── backtest/           # Simulation engine
│   ├── forecast/           # Daily predictions
│   ├── execution/          # Trade execution
│   └── visualization/      # Chart generation
├── data/
│   ├── raw/                # OHLCV from FYERS
│   └── processed/          # Trades, equity curve
├── models/                 # Trained model artifacts
└── reports/
    ├── figures/            # Performance charts
    └── daily_predictions.csv
```

---

## Competition Compliance

| Requirement | Status |
|-------------|--------|
| FYERS API for data | `src/data/fyers_client.py` |
| FYERS API for execution | `src/execution/trader.py` |
| Daily OHLCV only | No intraday data |
| Nov-Dec 2025 trading window | All trades in window |
| Jan 1-8, 2026 predictions | `reports/daily_predictions.csv` |
| No look-ahead bias | Verified via `audit_bias.py` |
| Walk-forward validation | Chronological execution |

---

## License

MIT License - See [LICENSE](LICENSE) for details.

### Core Implementation Code & Architecture
#### File: `src/forecast/__init__.py`
```python
"""Forecast generation module."""
```

#### File: `src/visualization/__init__.py`
```python
from .performance import PerformanceVisualizer

__all__ = ["PerformanceVisualizer"]
```

#### File: `src/utils/__init__.py`
```python
from .logger import get_logger, LoggerFactory, TradeLogger, trade_logger

__all__ = ["get_logger", "LoggerFactory", "TradeLogger", "trade_logger"]
```

#### File: `config/__init__.py`
```python
from .settings import (
    Settings,
    DataConfig,
    FeatureConfig,
    ModelConfig,
    BacktestConfig,
    ExecutionConfig,
    VisualizationConfig,
    ConfigLoader,
    settings
)

__all__ = [
    "Settings",
    "DataConfig",
    "FeatureConfig",
    "ModelConfig",
    "BacktestConfig",
    "ExecutionConfig",
    "VisualizationConfig",
    "ConfigLoader",
    "settings"
]
```

#### File: `src/features/preprocessing.py`
```python
import logging
from typing import List

import pandas as pd
import numpy as np

from src.features.indicators import add_indicators
from src.features.advanced_features import add_all_features
from src.features.labeling import triple_barrier_labeling, calculate_sample_weights

logger = logging.getLogger(__name__)


def preprocess_pipeline(df: pd.DataFrame, is_training: bool = True, min_hold: int = 2, max_hold: int = 5) -> pd.DataFrame:
    df = add_indicators(df)
    df = add_all_features(df)

    initial_len = len(df)
    df = df.dropna(subset=["close", "volume"])

    if is_training:
        df = triple_barrier_labeling(df, min_hold=min_hold, max_hold=max_hold)
        df["sample_weight"] = calculate_sample_weights(df)
        df = df.dropna(subset=["label", "t1", "sample_weight"])
    else:
        feature_cols = get_feature_columns(df)
        df[feature_cols] = df[feature_cols].ffill().fillna(0)

    return df


def get_feature_columns(df: pd.DataFrame) -> List[str]:
    exclude = [
        "date", "open", "high", "low", "close", "volume",
        "label", "label_3class", "t1", "future_return",
        "barrier_touched", "sample_weight", "typical_price",
        "raw_label", "atr", "significance_threshold"
    ]
    return [col for col in df.columns if col not in exclude]
```

#### File: `src/data/fetch_data.py`
```python
import os
import sys
import logging
from typing import Optional

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.data.fyers_client import FyersClient
from config.settings import settings

logger = logging.getLogger(__name__)


def fetch_and_save(
    start_date: str = "2025-11-01",
    end_date: str = "2025-12-31",
    symbol: str = None
) -> Optional[pd.DataFrame]:
    symbol = symbol or settings.data.default_symbol
    output_file = str(settings.data.data_path)
    
    os.makedirs(str(settings.data.raw_data_dir), exist_ok=True)
    client = FyersClient()

    if not client.is_connected:
        logger.error("FYERS client not connected")
        return None

    df = client.fetch_historical_data(symbol, start_date, end_date)
    if df is None or df.empty:
        logger.error("Failed to fetch data")
        return None

    df['date'] = pd.to_datetime(df['date'])
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
    df = df.sort_values('date').reset_index(drop=True)

    df.to_csv(output_file, index=False)
    logger.info(f"Saved {len(df)} rows to {output_file}")
    return df


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    fetch_and_save()
```


==================================================


## [2/3] Repository: AI-ML (`PHASE4-QUANT-082`)
- **Full Name**: `PHASE4-QUANT-082_tradevectorsrobots__AI-ML`
- **Description**: AI & Machine Learning for algorithmic trading India | Python ML trading models | Predictive analytics for NSE/BSE markets
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AI & Machine Learning in Algorithmic Trading — NSE/BSE India

Exploring the application of **Artificial Intelligence (AI)** and **Machine Learning (ML)** in algorithmic trading for **Indian financial markets (NSE/BSE)**. This repository covers ML models, predictive analytics, and AI-powered trading strategies.

## Why AI/ML in Algorithmic Trading?

Traditional rule-based algorithms follow fixed conditions. AI and ML-powered trading systems can:
- **Learn from patterns** in historical price data
- **Adapt** to changing market conditions
- **Predict** price movements with greater accuracy
- **Optimize** entry/exit points automatically
- **Detect anomalies** and unusual market behavior

## ML Techniques Used in Algo Trading

### Supervised Learning
| Model | Trading Application |
|---|---|
| **Linear Regression** | Price trend prediction |
| **Random Forest** | Multi-factor stock classification |
| **XGBoost** | High-accuracy trade signal generation |
| **LSTM (Neural Network)** | Time-series price forecasting |
| **Support Vector Machines** | Pattern classification in price data |

### Unsupervised Learning
| Model | Trading Application |
|---|---|
| **K-Means Clustering** | Market regime detection |
| **PCA** | Dimensionality reduction for factor models |
| **Anomaly Detection** | Identifying unusual trading patterns |

### Reinforcement Learning
- Training trading agents to maximize returns
- Dynamic position sizing based on market feedback
- Q-Learning and Deep Q-Networks (DQN) for trading

## Python Libraries for ML Trading

```python
# Core ML & Data Science
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Financial Data
import yfinance as yf
from nsepy import get_history
```

## Sample LSTM Price Prediction Architecture

```python
# LSTM model for NSE stock price prediction
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(60, 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)  # Predicted price
])
model.compile(optimizer='adam', loss='mean_squared_error')
```

## Applications in Indian Markets

- **Nifty 50 Direction Prediction** using ML classifiers
- **Bank Nifty Options Strategy** optimization with reinforcement learning
- **Sentiment Analysis** on NSE stock news using NLP
- **Volatility Forecasting** for F&O premium pricing
- **Portfolio Optimization** using modern portfolio theory + ML

## About Trade Vectors

**Trade Vectors** is a Mumbai-based algorithmic trading company at the forefront of AI-powered trading systems and quantitative finance solutions for NSE/BSE India.

We offer:
- AI/ML-based trading strategy development
- Custom algorithmic trading software
- Quantitative analysis and backtesting
- Corporate training in algorithmic trading and AI for finance

Visit **[tradevectors.com](https://tradevectors.com)** for AI-powered trading solutions, algo trading courses, and machine learning applications in Indian financial markets.

**Contact:** [tradevectors.com](https://tradevectors.com) | [@tradevectors](https://twitter.com/tradevectors)

---
*Keywords: AI algorithmic trading India, machine learning stock market NSE, Python ML trading model, LSTM stock prediction, deep learning NSE/BSE, quantitative trading AI India*


==================================================


## [3/3] Repository: ShortCircuit (`PHASE4-QUANT-083`)
- **Full Name**: `PHASE4-QUANT-083_nabrahma__ShortCircuit`
- **Description**: Institutional-Grade Algorithmic Trading System for NSE.
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# ShortCircuit

> Live intraday NSE execution engine: WebSocket-first market data with freshness
> tracking, sequential gate validation, broker-verified fills, capital-aware
> sizing, and automated state reconciliation.

[![CI](https://github.com/nabrahma/ShortCircuit/actions/workflows/ci.yaml/badge.svg)](https://github.com/nabrahma/ShortCircuit/actions/workflows/ci.yaml)
[![Security](https://github.com/nabrahma/ShortCircuit/actions/workflows/security.yaml/badge.svg)](https://github.com/nabrahma/ShortCircuit/actions/workflows/security.yaml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](pyproject.toml)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](LICENSE)

> ⚠️ **Not investment advice. No performance claims.** This repository documents
> the engineering of a personal execution system. See [DISCLOSURE.md](docs/DISCLOSURE.md).

---

## What this is

**ShortCircuit is a live intraday NSE execution engine for detecting and trading
momentum exhaustion.**

It is not a chart pattern script. It is not a notification bot with a broker
wrapper bolted on. ShortCircuit is a trading system covering market data
ingestion, microstructure filtering, sequential gate evaluation, capital-aware
sizing, broker-side risk placement, reconciliation, audit logging, Telegram
command and control, and parquet-based ML feedback loops.

The design premise:

> Setups are only acted on when extension, rejection, and liquidity decay
> coincide, and only once execution can be verified.

It is built around one operating principle:

> **If the system cannot prove the setup, prove the fill, prove the stop, and
> prove the state, it should not trade.**

---

## Executive summary

ShortCircuit scans thousands of NSE equity symbols during the live session and
hunts for a specific event:

**an overextended intraday mover failing at or above value while momentum buyers
are trapped and upward auction quality is degrading.**

When the setup appears, the system does not immediately trade. It promotes the
symbol into a staged gate pipeline. The analyzer passes the data to the "Brain"
(the `BackToVWAPShort` strategy) to approve structure, momentum, volume, profile,
confluence, and higher-timeframe context. The focus engine then waits for a real
structural trigger: a break of the entry level, with invalidation above the setup
high.

Only after that does the order layer engage.

At runtime the bot coordinates Fyers REST and WebSocket connectivity, the NSE-EQ
scanner universe, a WebSocket-first quote cache with freshness tracking, a single
exhaustion strategy, signal validation, a single-position capital slot,
broker-side stop placement, an active trade monitor, Telegram control, a
PostgreSQL audit trail, ML parquet logging, EOD reporting, and broker/DB
reconciliation.

---

## The Brain vs Muscle architecture

ShortCircuit is split into two components with an **enforced dependency
boundary**: `strategy/` imports nothing from the runtime layer, and a test
asserts it.

### The Brain (`src/shortcircuit/strategy/`)

All trading intelligence is physically sealed inside `strategy/`. It knows
nothing about brokers, websockets, or Telegram. It only knows math, risk, and
logic.

- `strategy/back_to_vwap.py`: the single unified execution logic
- `strategy/features.py`: stateless math (VWAP, RSI, volume fade, ATR)
- `strategy/market_profile.py`: Dalton value areas (VAH/VAL/POC)
- `strategy/market_context.py`: Nifty regime and broader trend
- `strategy/htf_confluence.py`: higher-timeframe risk gates

That boundary is verified, not asserted:
[`tests/unit/test_brain_isolation.py`](tests/unit/test_brain_isolation.py) parses
the AST of every strategy module and fails if one imports the runtime layer, an
I/O library, or opens a file.

### The Muscle (the rest of the package)

The rest of the repository is the muscle, nervous system, and immune system. It
fetches data, asks the Brain for decisions, and pulls the physical triggers.

- `execution/analyzer.py`: the orchestrator that asks the Brain what to do
- `execution/order_manager.py` / `broker/fyers_broker_interface.py`: the hands that execute
- `state/reconciliation.py`: the immune system verifying local state against the broker

---

## Strategy model: BackToVWAPShort

A single strategy: **BackToVWAPShort**.

It is primarily a short-side mean-reversion and exhaustion engine (it natively
supports `/mode buy` via Telegram for inverse logic), built around three
observations:

1. Strong intraday gain creates unstable positioning.
2. Momentum becomes tradable only when extension meets rejection.
3. A signal is not an entry until price confirms structural failure.

The bot is interested in stocks that have already moved aggressively, usually
above VWAP and value, where late momentum participants are vulnerable. It then
looks for evidence that the move is no longer being accepted:

- Intraday gain expansion
- VWAP standard-deviation stretch
- Value Area High or profile rejection
- VWAP flattening or momentum decay
- Volume fade after surge
- Failed continuation structure
- Higher-timeframe stall or fail-open guard
- Candle trigger through the signal low

It is not "short everything that is up." It is "short only when an up-move has
become statistically stretched, structurally rejected, and execution-confirmed."

The mechanism behind each filter is described in
[docs/STRATEGY.md](docs/STRATEGY.md). Tuned thresholds live in `config.py` and
are not published, and nor is any statistic describing how the filter behaves.

---

## Data plane

WebSocket-first, with an explicit freshness state machine.

```text
UNINITIALIZED → PRIMING → READY → DEGRADED → REPRIME/RECOVER
```

- REST seed gives cold-start coverage.
- **REST seed does not count as true freshness.**
- WebSocket tick freshness determines readiness.
- Startup waits for cache readiness before scanning.
- Degraded cache can reprime. REST fallback is available during data stress.

The system separates **"known" from "fresh."** A stale cached quote is not live
market data. The bot treats that distinction as a first-class safety property.
It exists because a reconnect once looked healthy while no tick had arrived for
the affected symbols ([D-002](docs/DISCOVERIES.md)).

---

## Execution plane

```text
Signal detected by the Brain
  → Telegram alert / ML observation / gate audit
  → Pending validation (Focus Engine)
  → Trigger break
  → Capital slot check (dynamic 4x/5x leverage)
  → Entry order (graceful margin fallback)
  → WebSocket fill confirmation, REST verification fallback
  → Broker-side stop placement
  → Active focus monitor
```

Exits: a staged take-profit, the broker-side stop, or the 15:10 IST square-off.
Under the default `TP_MODE='SCALE'` the position sheds half at the midpoint
between entry and the VWAP target and runs the remainder to that target, moving
the stop to breakeven once the partial fills. `'SINGLE'` closes fully at the
midpoint; `'OFF'` leaves the stop and the square-off as the only exits.

The take-profit was removed in August and restored on 2026-08-30 after a replay
of every live trade reversed the original reading. [ADR-009](docs/DECISIONS.md)
records the removal, [ADR-011](docs/DECISIONS.md) the reversal and why the
evidence for it is a point estimate rather than a proven result.

**Manual override.** If the operator changes a stop directly at the broker, the
bot detects the structural change, sets `manual_override` and backs off. It
stops managing the stop and hands over without exiting the trade.

The system holds one position at a time. This bounds the state space that
reconciliation, capital control, and recovery must handle
([ADR-002](docs/DECISIONS.md)).

---

## Capital model

Sizing comes from live broker funds, not a hardcoded number. The capital manager
reads Fyers funds, parses multiple response shapes, derives real margin, applies
dynamic intraday leverage (5x primary, auto-scaling to 4x on margin rejection),
reserves one active slot, prevents concurrent entries, releases only after a
confirmed close, and resyncs after fills and exits.

The bot can scan continuously, but entry is blocked while capital is occupied.

---

## Operator surface

Telegram is the only operator interface: startup and status alerts, signal
discovery, validation updates, `/auto on|off`, `/mode buy|sell`, `/status`,
`/health`, broker health alerts, trade notifications, risk alerts, and EOD
reports.

There is no web UI in the runtime path. Fewer services, fewer sockets, one
control plane ([ADR-001](docs/DECISIONS.md)).

---

## Persistence and auditability

PostgreSQL for orders, positions, reconciliation events and gate results; a CSV
signal log; daily session logs; a daily rejection summary; ML parquet
observations; and an EOD markdown report.

**Every candidate that reaches analyzer evaluation produces a gate result.** This
matters because the bot is not only an execution engine. It is also a research
instrument. Schema: [docs/DATA_MODEL.md](docs/DATA_MODEL.md).

---

## Reconciliation and recovery

Live trading systems fail when internal state and broker state diverge.
Reconciliation is a core runtime service, not a maintenance script.

It detects orphaned broker positions, phantom internal positions, quantity
mismatches, manual closes, and broker-side fills missed by the internal loop.
Recovery adopts orphans with emergency protection, releases capital for phantoms,
updates DB state, marks the cache dirty, alerts the operator, and avoids
duplicate adoption.

**Seven divergence categories, each with a test.** Plus an eighth asserting
adoption is idempotent, and two safety properties: a degraded broker API must not
be classified as flat, and settlement lag must not raise a false orphan. The full
table is in [docs/TESTING.md](docs/TESTING.md).

---

## Engineering practices

A system that places real orders gets built differently. A bug here does not raise an exception in CI. It loses money during a live
session, days later, in a way that looks like bad luck.

### Testing

344 unit, property-based and strategy tests. Coverage is concentrated where an
error is hardest to notice: the `strategy/` package sits at 86% overall, with
`back_to_vwap.py` and `htf_confluence.py` at 100% on statements and branches and
`market_context.py` at 97%. `market_profile.py` (40%) and the capital layer (75%)
are both below their floors, and that is stated in
[docs/KNOWN_GAPS.md](docs/KNOWN_GAPS.md) rather than hidden behind a global
average.

The reconciliation divergence table is the highest-value file in the suite.
Property-based tests assert invariants over generated series rather than
examples: that VWAP stays inside the traded range, that a zero-volume bar does
not move it, and that read-only feature calls never mutate their input frame.

Deliberately not tested: live broker connectivity, WebSocket transport, Telegram
delivery, and **the strategy's profitability**. A test suite cannot validate an
edge, and claiming otherwise would be dishonest.

### Continuous integration

Lint, tests across Python 3.11 and 3.12, integration against a real PostgreSQL
service, and a container build that asserts no `.env` is baked into the image.
Every GitHub Action is pinned to a commit SHA rather than a tag.

### Failure handling

WebSocket drop, margin rejection, orphan detection, process death with a position
open. Each has a documented procedure in
[docs/OPERATIONS.md](docs/OPERATIONS.md). Stops are placed broker-side
specifically so protection survives local process death.

### Reproducibility

`docker compose -f deploy/docker-compose.test.yml up --exit-code-from tests`
builds the system and runs the full suite on any machine with Docker, **with no
credentials**. Dependencies are pinned.

### Secret handling

Credentials come from `.env` only, never logged. `gitleaks` runs pre-commit and
in CI over the **full git history**, because a deleted credential still lives
there. Findings are disclosed in [docs/SECURITY.md](docs/SECURITY.md) rather
than quietly resolved.

### Auditability

Every gate evaluation produces a record. Structured session logs, parquet
observations with outcome labelling, and a daily rejection breakdown.

---

## Key discoveries

Eight real problems found while building and operating this system, with
evidence: [docs/DISCOVERIES.md](docs/DISCOVERIES.md).

Six of the eight share a shape: **something reported success while doing
nothing.** A websocket handler that parsed no messages. A cache with no writer. A
connection-pool fix applied to an attribute that does not exist. A timeout that
abandoned the request it was meant to bound.

None raised an exception. All were found by reading logs against the code and
asking whether the numbers agreed: 48 versus 0, 42 versus 42, 41 versus 41.

---

## System measurements

Engineering metrics only. No performance, profitability or return figures. See
[DISCLOSURE.md](docs/DISCLOSURE.md). All traceable to
[`docs/evidence/system-measurements.txt`](docs/evidence/system-measurements.txt).

| Metric | Value |
|---|---|
| Session logs analysed | 28 |
| Scan cycles recorded | 4,776 |
| Scanner universe | ~2,400 symbols |
| Scan latency (p50 / p99) | 9 ms / 501 ms |
| Cache priming, cold start | 4 to 25 s observed |
| Reconciliation cadence | every 6 s during market hours |
| Tests / runtime | 344 / ~7 s |

These describe how the system runs, not how the strategy performs. Gate
thresholds, rejection distributions and anything else that characterises the
filter are deliberately not published.

---

## Running it

**Prerequisites:** Python 3.11+, PostgreSQL 14+ (tested on 16), a Fyers API app,
and a Telegram bot. There is no way to run this without a broker account.

```bash
python -m venv .venv && source .venv/bin/activate
make install
```

Copy [`.env.example`](.env.example) to `.env` and fill it in. Variable names
matter — `DB_PASS`, not `DB_PASSWORD`, is what `deploy/docker-compose.yml`
requires, and `AUTO_MODE` there is documentation only: it is a constant in
`config.py`, armed on boot, and disarmed at runtime with `/auto off`.

Create the database and apply the schema. **Migrations are not applied
automatically** — run them once, in lexical order:

```bash
createdb shortcircuit_trading
for f in migrations/*.sql; do psql -d shortcircuit_trading -v ON_ERROR_STOP=1 -f "$f"; done
```

The role you connect as should own the database; `v42_1_0_postgresql.sql` creates
the `uuid-ossp` extension, which a database owner may do on PostgreSQL 14+.

```bash
make test           # 344 tests, no credentials or database needed
make demo           # the same suite in a container, no credentials needed
python main.py      # live — requires credentials and a migrated database
```

**Live operation requires broker credentials.** There is no offline or paper
mode, and one has not been faked for demonstration purposes. What is reproducible
without credentials is the build and the full test suite.

---

## Project layout

```text
main.py                       Entry-point shim, so `python main.py` still works
src/shortcircuit/
├── config.py                 Strategy, risk, mode and infrastructure parameters
├── paths.py                  Repository-anchored runtime paths
├── runtime/                  Supervisor, market session, startup recovery
├── marketdata/               Scanner, symbols, session helpers
├── broker/                   Fyers REST + WebSocket, auth, rate limiter
├── execution/                Analyzer, focus engine, order/signal/trade managers
├── capital/                  Funds sync, sizing, capital slot
├── state/                    PostgreSQL access, reconciliation
├── observability/            Telegram, gate audit, ML logger
├── eod/                      EOD analyzer, scheduler, watchdog
└── strategy/                 The Brain: logic and math only
    ├── back_to_vwap.py       Single unified strategy
    ├── features.py           VWAP, RSI, volume, ATR, patterns
    ├── market_profile.py     Dalton value areas
    ├── market_context.py     Nifty regime
    └── htf_confluence.py     Higher-timeframe gates

tests/                        344 unit, property and strategy tests
docs/                         Architecture, strategy, operations, decisions, evidence
deploy/                       Dockerfile and compose stacks
scripts/                      Operational scripts
migrations/                   PostgreSQL schema migrations
```

---

## Limitations

Worth stating plainly. A repo with no limitations section usually just has undocumented ones.

- **One position at a time.** Deliberate ([ADR-002](docs/DECISIONS.md)), but it
  means concurrent opportunities are logged and skipped.
- **One broker.** Fyers-specific. The broker interface is not abstracted behind a
  generic protocol.
- **No backtester in this repository.** Historical evaluation is done separately;
  nothing here validates the strategy against past data.
- **Coverage is uneven.** Concentrated in strategy math and the capital layer;
  three strategy modules are untested, and the order and focus engines are
  covered only indirectly ([KNOWN_GAPS.md](docs/KNOWN_GAPS.md)).
- **No offline mode.** Live operation requires real credentials.
- **Single operator, single account.** No multi-user or multi-account concept.

---

## Documentation

| Document | Contents |
|---|---|
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design and runtime model |
| [STRATEGY.md](docs/STRATEGY.md) | Gate methodology and the quantitative work behind it |
| [OPERATIONS.md](docs/OPERATIONS.md) | Runbook: what to do when things fail |
| [TESTING.md](docs/TESTING.md) | Test levels, divergence table, invariants, non-goals |
| [DATA_MODEL.md](docs/DATA_MODEL.md) | PostgreSQL schema and parquet observation schema |
| [DECISIONS.md](docs/DECISIONS.md) | Architectural decision records |
| [DISCOVERIES.md](docs/DISCOVERIES.md) | Real problems hit, with evidence |
| [KNOWN_GAPS.md](docs/KNOWN_GAPS.md) | What is not done, honestly |
| [SECURITY.md](docs/SECURITY.md) | Credential handling and scan results |
| [DISCLOSURE.md](docs/DISCLOSURE.md) | Regulatory posture and non-claims |

---

## Related work

The reconciliation problem here, where local records and an external system's
records disagree without either side raising an error, turns out to generalise.
[driftwatch](https://github.com/nabrahma/driftwatch) is a Go tool that detects the
same divergence class in event-sourced caches.

---

## Risk statement

ShortCircuit is live trading infrastructure. It can place real orders, create
real exposure, and lose real money.

It is engineered for discipline, observability, and fast recovery. It is not
engineered to guarantee outcomes. Markets are adversarial, broker APIs fail,
liquidity disappears, and no gate stack can eliminate risk.

Use it like a production system:
- monitor it
- audit it
- keep secrets out of logs
- verify broker state
- review every EOD report
- never assume a green process means a flat broker account

---

## Disclosure

This repository is published as software, not as a recommendation. It publishes
no performance, profitability, or return figures, and none should be inferred.
The author is not a registered Investment Adviser or Research Analyst. Full
terms: [docs/DISCLOSURE.md](docs/DISCLOSURE.md).

---

## License

[Apache-2.0](LICENSE).

### Core Implementation Code & Architecture
#### File: `src/shortcircuit/broker/__init__.py`
```python

```

#### File: `src/shortcircuit/capital/__init__.py`
```python

```

#### File: `src/shortcircuit/marketdata/__init__.py`
```python

```

#### File: `src/shortcircuit/runtime/__init__.py`
```python

```

#### File: `src/shortcircuit/observability/__init__.py`
```python

```

#### File: `src/shortcircuit/state/__init__.py`
```python

```


==================================================
