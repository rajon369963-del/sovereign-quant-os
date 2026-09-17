# ⚡ [QUANT-SOURCE-031] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_031_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: upx-momentum-nse (`WHEEL_upx-momentum-nse`)
- **Full Name**: `upx-momentum-nse`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Upstox Intraday Momentum Algo

A production‑ready Python framework for **intraday momentum trading** on **NSE EQ, F&O, and Nifty/BankNifty options** via **Upstox** APIs.

**Highlights**
- **Data**: LTPC mode over **Market Data Feed V3** (WebSocket + Protobuf)
- **Strategy**: EMA‑based momentum on 1‑minute bars (customizable)
- **Risk**: Max portfolio drawdown **4%**, **1% risk per trade**
- **Exits**: Server‑side **GTT** (ENTRY/TARGET/STOP, optional trailing) or **exchange SL/SL‑M + LIMIT TP** with OCO via Portfolio Stream
- **Ops**: **Auto square‑off @ 15:12 IST**, daily **BOD instruments** refresh (lot/tick enforcement), OAuth helper
- **Modes**: **Paper**, **Backtest**, **Live** (sandbox → real)
- **Tooling**: Mode switch CLI, validation script, schedulers (**cron/systemd/Windows**), **GitHub Actions CI** at **08:50 IST**

## Why this repo?
Intraday momentum requires low‑latency data, clean risk boundaries, and reliable exits even when clients disconnect. This framework wires Upstox’s latest APIs end‑to‑end: lightweight LTPC streaming, robust order management (GTT or SL/SL‑M), portfolio stream for real‑time OCO, and a daily instrument master workflow so lot/tick rules are always respected.

## Core Features
- **Market Data V3 (LTPC)**: WebSocket + Protobuf decoding for efficient tick ingestion  
- **Bar Aggregation**: 1‑min OHLC driven by LTPC ticks  
- **Strategy Module**: Pluggable EMA momentum with configurable SL/TP  
- **Risk Manager**: High‑water mark drawdown and per‑trade sizing (1% risk)  
- **Order Flow**:  
  - **GTT multi‑leg** (ENTRY/TARGET/STOP, optional trailing)  
  - **SL/SL‑M + LIMIT TP** (exchange orders) with **OCO** via Portfolio Stream  
- **Daily Instruments (BOD)**: Loader + enforcement for **lot_size**/**tick_size**; ATM strike selection for NIFTY/BANKNIFTY  
- **Automation**: cron/systemd/Windows tasks; **CI** refresh + validation  
- **Utilities**: OAuth helper, mode switch CLI, post‑refresh validator, docs (Markdown + PDF)

## Quick Start
1. `python -m venv .venv && source .venv/bin/activate`  
2. `pip install -r upx_algo/requirements.txt`  
3. Put `MarketDataFeedV3.proto` in `upx_algo/proto` and compile:  
   `protoc --python_out=upx_algo/proto upx_algo/proto/MarketDataFeedV3.proto`  
4. `cp upx_algo/.env.sample upx_algo/.env` → set `UPX_API_KEY`, `UPX_API_SECRET`, `UPX_REDIRECT_URI`  
5. Get access token: `python upx_algo/tools/oauth_get_token.py --open`  
6. Daily instruments: `python upx_algo/tools/bod_refresh.py --download --update-env --select atm --count 1`  
7. Validate: `python upx_algo/tools/validate_post_refresh.py`  
8. Run:  
   - PAPER: `python upx_algo/tools/mode_switch.py --target paper && python upx_algo/main.py`  
   - LIVE (sandbox): `python upx_algo/tools/mode_switch.py --target live-sandbox && python upx_algo/main.py`  
   - LIVE (real): `python upx_algo/tools/mode_switch.py --target live-real && python upx_algo/main.py`

## Scheduling & CI
- **cron (Linux/macOS)**: `tools/schedule_bod.sh` → 08:50 IST  
- **systemd (Linux)**: `ops/systemd/upx-bod-refresh.service/.timer`  
- **Windows Task Scheduler**: `tools/register_bod_task.ps1` or `register_bod_task.bat`  
- **GitHub Actions**: `.github/workflows/upx-ci.yml` (daily, 08:50 IST).  
  Set secrets: `UPX_API_KEY`, `UPX_API_SECRET`, `UPX_REDIRECT_URI`, `UPX_ACCESS_TOKEN`.

## Safety & Notes
- Start in **PAPER** → **LIVE (sandbox)** → **LIVE (real)**  
- Always use BOD instrument master to honor **lot_size**/**tick_size** and avoid rejections  
- Keep secrets out of source—use `.env` locally and **GitHub Secrets** for CI  
- Markets are risky; test thoroughly before live deployment

---

# Upstox Intraday Momentum Algo – Conversation & Setup Notes
**Saved:** 2026-01-02T14:05:53.262398 (IST)
This document captures the outcome of our conversation and provides a consolidated, ready‑to‑run guide for the Python algo built for **Upstox** with:
- Segments: **NSE EQ, F&O, Nifty & BankNIFTY options**
- Data mode: **LTPC** via **WebSocket V3** (binary Protobuf)
- Strategy: **Intraday momentum** (EMA‑based on 1‑minute bars)
- Risk: **Max drawdown 4%**, **1% per trade**
- Exits: **SL/TP**—either **GTT multi‑leg** or **exchange SL/SL‑M + LIMIT TP** with OCO via Portfolio Stream
- Auto **square‑off @ 15:12 IST**
- Modes: **Paper**, **Backtest**, **Live**

---

## Repository Structure (generated)

```
upx_algo/
├─ proto/                       # Protobufs (MarketDataFeedV3.proto + generated *_pb2.py)
├─ decoders/market_v3.py        # Protobuf decoder (LTPC)
├─ examples/query_chain.py      # BANKNIFTY option chain sample
├─ tools/
│  ├─ check_market_v3_decode.py # LTPC sanity test
│  ├─ mode_switch.py            # PAPER / LIVE (sandbox/real) toggle CLI
│  ├─ oauth_get_token.py        # OAuth helper (capture code, token exchange, update .env)
│  ├─ bod_refresh.py            # Daily BOD loader + ATM selection; updates .env
│  ├─ validate_post_refresh.py  # Post‑refresh validator; emits JSON summary
│  ├─ schedule_bod.sh           # (Option A) cron wrapper for daily refresh
│  ├─ bod_refresh.ps1           # (Option C) Windows PowerShell wrapper
│  ├─ register_bod_task.ps1     # (Option C) Register Windows Scheduled Task (PowerShell)
│  └─ register_bod_task.bat     # (Option C) Register Scheduled Task via schtasks (cmd)
├─ ops/systemd/                 # (Option B) systemd service & timer templates
│  ├─ upx-bod-refresh.service   # edit absolute paths; oneshot service
│  └─ upx-bod-refresh.timer     # Mon–Fri 08:50 IST
├─ data/                        # BOD cache, validation JSON, CI sample
│  └─ sample_instruments.json   # CI fallback sample instruments
├─ logs/                        # Rotating logs
├─ .github/workflows/upx-ci.yml # GitHub Actions: daily refresh & validation
├─ config.py                    # Loads .env
├─ auth.py                      # OAuth/token helper
├─ instrument_loader.py         # BOD loader + indexes
├─ enforce.py                   # lot/tick enforcement
├─ market_data.py               # WS V3 LTPC stream + bar aggregator
├─ portfolio_stream.py          # WS portfolio updates
├─ strategy_momentum.py         # EMA momentum signals
├─ risk.py                      # drawdown & sizing (1% per trade)
├─ broker_live.py               # OrderApiV3
├─ broker_paper.py              # paper simulator
├─ sl_tp_manager.py             # SL/SL‑M + LIMIT TP, OCO via portfolio
├─ gtt_manager.py               # Bracket via GTT multi‑leg
├─ engine.py                    # Orchestrator + square‑off @ 15:12 IST
├─ main.py                      # Entrypoint
├─ requirements.txt             # Dependencies
├─ README.md                    # Quick start & references
└─ .env.sample                  # Sample environment config
```

---

## Quick Start

```bash
# 1) Create venv
python -m venv .venv
source .venv/bin/activate

# 2) Install deps
pip install -r upx_algo/requirements.txt

# 3) Compile Protobuf classes for Market Data V3
#   Place MarketDataFeedV3.proto in upx_algo/proto (download from Upstox examples)
protoc --python_out=upx_algo/proto upx_algo/proto/MarketDataFeedV3.proto

# 4) Configure environment
cp upx_algo/.env.sample upx_algo/.env
# Edit UPX_API_KEY, UPX_API_SECRET, UPX_REDIRECT_URI

# 5) Obtain access token (OAuth)
python upx_algo/tools/oauth_get_token.py --open

# 6) Refresh BOD instruments & select ATM
python upx_algo/tools/bod_refresh.py --download --update-env --select atm --count 1

# 7) Validate
python upx_algo/tools/validate_post_refresh.py

# 8) Run (PAPER)
python upx_algo/tools/mode_switch.py --target paper
python upx_algo/main.py

# 9) LIVE (sandbox), then LIVE (real)
python upx_algo/tools/mode_switch.py --target live-sandbox
python upx_algo/main.py
python upx_algo/tools/mode_switch.py --target live-real
python upx_algo/main.py
```

---

## OAuth Helper

Use `tools/oauth_get_token.py` to:
- Build the Upstox authorization URL (`response_type=code`)
- Open your browser for login & consent
- Capture the `code` via a tiny local HTTP server (e.g., `http://127.0.0.1:5000/callback`)
- Exchange the `code` for `access_token` via SDK, then update `.env`

> Ensure your developer app’s **Redirect URI** exactly matches the `.env` value.

---

## Daily BOD Refresh & Instrument Selection

Run `tools/bod_refresh.py` each morning (before market open) to:
- Download & cache BOD instruments (`data/instruments_YYYYMMDD.json.gz`)
- Update `.env` → `UPX_BOD_PATH`
- Auto‑select `UPX_INSTRUMENT_KEYS` (NIFTY/BANKNIFTY index + ATM CE/PE for nearest weekly expiry) using the current LTP

Post‑refresh validation:

```bash
python upx_algo/tools/validate_post_refresh.py
```
- Confirms all selected keys exist in BOD data and have valid `lot_size` & `tick_size`
- Checks options fields (`option_type`, `strike_price`, `expiry`)
- Dry‑runs lot/tick enforcement; outputs `data/validation_YYYYMMDD.json`

---

## Scheduling (Option A/B/C)

**A) Cron (Linux/macOS)**
- File: `tools/schedule_bod.sh`
- Crontab:
  ```cron
  50 8 * * 1-5 /bin/bash /absolute/path/to/upx_algo/tools/schedule_bod.sh
  ```

**B) systemd (Linux)**
- Files: `ops/systemd/upx-bod-refresh.service`, `ops/systemd/upx-bod-refresh.timer`
- Install:
  ```bash
  sudo cp upx_algo/ops/systemd/upx-bod-refresh.* /etc/systemd/system/
  sudo systemctl daemon-reload
  sudo systemctl enable upx-bod-refresh.timer
  sudo systemctl start upx-bod-refresh.timer
  ```

**C) Windows Task Scheduler**
- PowerShell wrapper: `tools/bod_refresh.ps1`
- Register task:
  ```powershell
  powershell -ExecutionPolicy Bypass -File .\upx_algo\tools\register_bod_task.ps1 -TaskName "UpxBodRefresh"
  ```
- Or via `schtasks`: `tools/register_bod_task.bat`

---

## GitHub Actions CI (Daily at 08:50 IST)

- Workflow: `.github/workflows/upx-ci.yml`
- Secrets required: `UPX_API_KEY`, `UPX_API_SECRET`, `UPX_REDIRECT_URI`, `UPX_ACCESS_TOKEN`
- Fallback sample instruments: `data/sample_instruments.json` (used if public URL blocks automation)

---

## Notes & Tips

- **Proto compilation** is mandatory for Market Data V3 (binary Protobuf)
- Always rely on **BOD instruments JSON** (daily) and enforce `lot_size`/`tick_size` before placing orders
- Use **Portfolio Stream** to implement OCO (when SL or TP fills, cancel the other)
- Start with **PAPER**, then **LIVE (sandbox)**, and only then **LIVE (real)**

---

## Next Steps

- Add instrument filters for your watchlist (EQ, F&O, specific strikes)
- Extend ATM selection to pick multiple bands (ATM ± 1/2/3)
- Add reporting (PnL curve, drawdowns) for backtests
- Harden reconnection logic for WebSockets and add alerting

---

*Document generated automatically from our setup conversation for quick reference.*


==================================================


## [2/3] Repository: zerodha-algo-trading (`WHEEL_zerodha-algo-trading`)
- **Full Name**: `zerodha-algo-trading`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
[![Python version](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat)](https://pypi.python.org/pypi/quantstats)
[![PyPi version](https://img.shields.io/pypi/v/quantstats.svg?maxAge=60)](https://pypi.python.org/pypi/quantstats)
[![PyPi status](https://img.shields.io/pypi/status/quantstats.svg?maxAge=60)](https://pypi.python.org/pypi/quantstats)
[![PyPi downloads](https://img.shields.io/pypi/dm/quantstats.svg?maxAge=2592000&label=installs&color=%2327B1FF)](https://pypi.python.org/pypi/quantstats)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ranaroussi/quantstats)
[![Star this repo](https://img.shields.io/github/stars/ranaroussi/quantstats.svg?style=social&label=Star&maxAge=60)](https://github.com/ranaroussi/quantstats)
[![Follow me on twitter](https://img.shields.io/twitter/follow/aroussi.svg?style=social&label=Follow&maxAge=60)](https://twitter.com/aroussi)

# QuantStats: Portfolio analytics for quants

**QuantStats** Python library that performs portfolio profiling, allowing quants and portfolio managers to understand their performance better by providing them with in-depth analytics and risk metrics.

[Changelog »](./CHANGELOG.md)

### QuantStats is comprised of 3 main modules:

1. `quantstats.stats` - for calculating various performance metrics, like Sharpe ratio, Win rate, Volatility, etc.
2. `quantstats.plots` - for visualizing performance, drawdowns, rolling statistics, monthly returns, etc.
3. `quantstats.reports` - for generating metrics reports, batch plotting, and creating tear sheets that can be saved as an HTML file.

---

### **NEW! Monte Carlo Simulations**

<img src="https://raw.githubusercontent.com/ranaroussi/pandas-montecarlo/master/demo.png" alt="Monte Carlo Simulation" width="640">

Run probabilistic risk analysis with built-in Monte Carlo simulations:

```python
mc = qs.stats.montecarlo(returns, sims=1000, bust=-0.20, goal=0.50)
print(f"Bust probability: {mc.bust_probability:.1%}")
print(f"Goal probability: {mc.goal_probability:.1%}")
mc.plot()
```

[Full Monte Carlo documentation »](./docs/montecarlo.md)

---

## Quick Start

```python
%matplotlib inline
import quantstats as qs

# extend pandas functionality with metrics, etc.
qs.extend_pandas()

# fetch the daily returns for a stock
stock = qs.utils.download_returns('META')

# show sharpe ratio
qs.stats.sharpe(stock)

# or using extend_pandas() :)
stock.sharpe()
```

Output:

```
0.7604779884378278
```

### Visualize stock performance

```python
qs.plots.snapshot(stock, title='Facebook Performance', show=True)

# can also be called via:
# stock.plot_snapshot(title='Facebook Performance', show=True)
```

Output:

![Snapshot plot](https://github.com/ranaroussi/quantstats/blob/main/docs/snapshot.webp?raw=true)

### Creating a report

You can create 7 different report tearsheets:

1. `qs.reports.metrics(mode='basic|full", ...)` - shows basic/full metrics
2. `qs.reports.plots(mode='basic|full", ...)` - shows basic/full plots
3. `qs.reports.basic(...)` - shows basic metrics and plots
4. `qs.reports.full(...)` - shows full metrics and plots
5. `qs.reports.html(...)` - generates a complete report as html

Let's create an html tearsheet:

```python
# benchmark can be a pandas Series or ticker
qs.reports.html(stock, "SPY")
```

Output will generate something like this:

![HTML tearsheet](https://github.com/ranaroussi/quantstats/blob/main/docs/report.webp?raw=true)

[View original html file](https://rawcdn.githack.com/ranaroussi/quantstats/main/docs/tearsheet.html)

### Available methods

To view a complete list of available methods, run:

```python
[f for f in dir(qs.stats) if f[0] != '_']
```

```python
['avg_loss',
 'avg_return',
 'avg_win',
 'best',
 'cagr',
 'calmar',
 'common_sense_ratio',
 'comp',
 'compare',
 'compsum',
 'conditional_value_at_risk',
 'consecutive_losses',
 'consecutive_wins',
 'cpc_index',
 'cvar',
 'drawdown_details',
 'expected_return',
 'expected_shortfall',
 'exposure',
 'gain_to_pain_ratio',
 'geometric_mean',
 'ghpr',
 'greeks',
 'implied_volatility',
 'information_ratio',
 'kelly_criterion',
 'kurtosis',
 'max_drawdown',
 'monthly_returns',
 'montecarlo',
 'montecarlo_cagr',
 'montecarlo_drawdown',
 'montecarlo_sharpe',
 'outlier_loss_ratio',
 'outlier_win_ratio',
 'outliers',
 'payoff_ratio',
 'profit_factor',
 'profit_ratio',
 'r2',
 'r_squared',
 'rar',
 'recovery_factor',
 'remove_outliers',
 'risk_of_ruin',
 'risk_return_ratio',
 'rolling_greeks',
 'ror',
 'sharpe',
 'skew',
 'sortino',
 'adjusted_sortino',
 'tail_ratio',
 'to_drawdown_series',
 'ulcer_index',
 'ulcer_performance_index',
 'upi',
 'value_at_risk',
 'var',
 'volatility',
 'win_loss_ratio',
 'win_rate',
 'worst']
```

```python
[f for f in dir(qs.plots) if f[0] != '_']
```

```python
['daily_returns',
 'distribution',
 'drawdown',
 'drawdowns_periods',
 'earnings',
 'histogram',
 'log_returns',
 'monthly_heatmap',
 'montecarlo',
 'montecarlo_distribution',
 'returns',
 'rolling_beta',
 'rolling_sharpe',
 'rolling_sortino',
 'rolling_volatility',
 'snapshot',
 'yearly_returns']
```

**\*\*\* Full documentation coming soon \*\*\***

### Important: Period-Based vs Trade-Based Metrics

QuantStats analyzes **return series** (daily, weekly, monthly returns), not discrete trade data. This means:

- **Win Rate** = percentage of periods with positive returns
- **Consecutive Wins/Losses** = consecutive positive/negative return periods
- **Payoff Ratio** = average winning period return / average losing period return
- **Profit Factor** = sum of positive returns / sum of negative returns

These metrics are **valid and useful** for:
- Systematic/algorithmic strategies with regular rebalancing
- Analyzing return-series behavior over time
- Comparing strategies on a period-by-period basis

For **discretionary traders** with multi-day trades, these period-based metrics may differ from trade-level statistics. A single 5-day trade might span 3 positive days and 2 negative days - QuantStats would count these as 3 "wins" and 2 "losses" at the daily level.

This is consistent with how all return-based analytics work (Sharpe ratio, Sortino ratio, drawdown analysis, etc.) - they operate on return periods, not discrete trade entries/exits.

---

In the meantime, you can get insights as to optional parameters for each method, by using Python's `help` method:

```python
help(qs.stats.conditional_value_at_risk)
```

```
Help on function conditional_value_at_risk in module quantstats.stats:

conditional_value_at_risk(returns, sigma=1, confidence=0.99)
    calculates the conditional daily value-at-risk (aka expected shortfall)
    quantifies the amount of tail risk an investment
```

## Installation

Install using `pip`:

```bash
$ pip install quantstats --upgrade --no-cache-dir
```

Install using `conda`:

```bash
$ conda install -c ranaroussi quantstats
```

## Requirements

* [Python](https://www.python.org) >= 3.10
* [pandas](https://github.com/pydata/pandas) >= 1.5.0
* [numpy](http://www.numpy.org) >= 1.24.0
* [scipy](https://www.scipy.org) >= 1.11.0
* [matplotlib](https://matplotlib.org) >= 3.7.0
* [seaborn](https://seaborn.pydata.org) >= 0.13.0
* [tabulate](https://bitbucket.org/astanin/python-tabulate) >= 0.9.0
* [yfinance](https://github.com/ranaroussi/yfinance) >= 0.2.40
* [plotly](https://plot.ly/) >= 5.0.0 (optional, for using `plots.to_plotly()`)

## Questions?

This is a new library... If you find a bug, please
[open an issue](https://github.com/ranaroussi/quantstats/issues).

If you'd like to contribute, a great place to look is the
[issues marked with help-wanted](https://github.com/ranaroussi/quantstats/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).

## Known Issues

For some reason, I couldn't find a way to tell seaborn not to return the
monthly returns heatmap when instructed to save - so even if you save the plot (by passing `savefig={...}`) it will still show the plot.

## Legal Stuff

**QuantStats** is distributed under the **Apache Software License**. See the [LICENSE.txt](./LICENSE.txt) file in the release for details.

## P.S.

Please drop me a note with any feedback you have.

**Ran Aroussi**

### Core Implementation Code & Architecture
#### File: `quantstats/_plotting/__init__.py`
```python

```

#### File: `quantstats/version.py`
```python
version = "0.0.81"
```

#### File: `tests/__init__.py`
```python
# QuantStats test suite
```

#### File: `quantstats/plots.py`
```python
#!/usr/bin/env python
#
# QuantStats: Portfolio analytics for quants
# https://github.com/ranaroussi/quantstats
#
# Copyright 2019-2025 Ran Aroussi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from pandas.plotting import register_matplotlib_converters as _rmc

    _rmc()
except ImportError:
    pass

from quantstats._plotting.wrappers import *
```

#### File: `tests/test_extend_pandas.py`
```python
"""
Tests for quantstats.extend_pandas functionality
"""

import pytest
import pandas as pd
import numpy as np

import quantstats as qs


@pytest.fixture
def sample_returns():
    """Generate sample returns as a pandas Series."""
    np.random.seed(42)
    dates = pd.date_range("2020-01-01", periods=252, freq="D")
    returns = pd.Series(np.random.randn(252) * 0.02, index=dates, name="Strategy")
    return returns


class TestExtendPandas:
    """Test extend_pandas functionality."""

    def test_extend_pandas_adds_methods(self, sample_returns):
        """Test that extend_pandas adds methods to Series."""
        qs.extend_pandas()

        # Check that quantstats methods are now available on Series
        assert hasattr(sample_returns, "sharpe")
        assert hasattr(sample_returns, "sortino")
        assert hasattr(sample_returns, "max_drawdown")
        assert hasattr(sample_returns, "cagr")

    def test_sharpe_via_pandas(self, sample_returns):
        """Test Sharpe ratio via pandas extension."""
        qs.extend_pandas()
        result = sample_returns.sharpe()
        assert np.isfinite(result)

    def test_sortino_via_pandas(self, sample_returns):
        """Test Sortino ratio via pandas extension."""
        qs.extend_pandas()
        result = sample_returns.sortino()
        assert np.isfinite(result)

    def test_max_drawdown_via_pandas(self, sample_returns):
        """Test max drawdown via pandas extension."""
        qs.extend_pandas()
        result = sample_returns.max_drawdown()
        assert result <= 0

    def test_cagr_via_pandas(self, sample_returns):
        """Test CAGR via pandas extension."""
        qs.extend_pandas()
        result = sample_returns.cagr()
        assert np.isfinite(result)

    def test_volatility_via_pandas(self, sample_returns):
        """Test volatility via pandas extension."""
        qs.extend_pandas()
        result = sample_returns.volatility()
        assert result > 0

    def test_calmar_via_pandas(self, sample_returns):
        """Test Calmar ratio via pandas extension."""
        qs.extend_pandas()
        result = sample_returns.calmar()
        assert np.isfinite(result)


class TestExtendPandasWithParams:
    """Test extend_pandas with parameters."""

    def test_sharpe_with_rf(self, sample_returns):
        """Test Sharpe with risk-free rate via pandas."""
        qs.extend_pandas()
        result_no_rf = sample_returns.sharpe(rf=0)
        result_with_rf = sample_returns.sharpe(rf=0.02)
        # Should be different
        assert result_no_rf != result_with_rf

    def test_cagr_compounded(self, sample_returns):
        """Test CAGR with compounded option via pandas."""
        qs.extend_pandas()
        result_comp = sample_returns.cagr(compounded=True)
        result_simple = sample_returns.cagr(compounded=False)
        # May or may not be different depending on returns
        assert np.isfinite(result_comp)
        assert np.isfinite(result_simple)
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "quantstats"
dynamic = ["version"]
description = "Portfolio analytics for quants"
readme = "README.md"
license = "Apache-2.0"
requires-python = ">=3.10"
authors = [
    { name = "Ran Aroussi", email = "ran@aroussi.com" },
]
keywords = [
    "quant",
    "algotrading",
    "algorithmic-trading",
    "quantitative-trading",
    "quantitative-analysis",
    "algo-trading",
    "visualization",
    "plotting",
    "portfolio",
    "finance",
]
classifiers = [
    "License :: OSI Approved :: Apache Software License",
    "Development Status :: 5 - Production/Stable",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Science/Research",
    "Topic :: Office/Business :: Financial",
    "Topic :: Office/Business :: Financial :: Investment",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
]
dependencies = [
    "pandas>=1.5.0",
    "numpy>=1.24.0",
    "scipy>=1.11.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.13.0",
    "tabulate>=0.9.0",
    "yfinance>=0.2.40",
    "python-dateutil>=2.8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "pyright>=1.1.0",
    "ruff>=0.1.0",
]
plotly = [
    "plotly>=5.0.0",
]

[project.urls]
Homepage = "https://github.com/ranaroussi/quantstats"
Documentation = "https://github.com/ranaroussi/quantstats"
Repository = "https://github.com/ranaroussi/quantstats"
Changelog = "https://github.com/ranaroussi/quantstats/blob/main/CHANGELOG.md"

[tool.hatch.version]
path = "quantstats/version.py"
pattern = 'version = "(?P<version>[^"]+)"'

[tool.hatch.build.targets.sdist]
include = [
    "/quantstats",
    "/README.md",
    "/CHANGELOG.md",
    "/LICENSE.txt",
]

[tool.hatch.build.targets.wheel]
packages = ["quantstats"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"

[tool.pyright]
include = ["quantstats"]
exclude = ["tests"]
pythonVersion = "3.10"
typeCheckingMode = "basic"

[tool.ruff]
target-version = "py310"
line-length = 88

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "UP",     # pyupgrade
    "B",      # flake8-bugbear
    "SIM",    # flake8-simplify
]
ignore = [
    "E501",   # line too long (handled by formatter)
    "B008",   # function call in default argument
    "SIM108", # ternary operator
]

[tool.ruff.lint.isort]
known-first-party = ["quantstats"]
```


==================================================


## [3/3] Repository: Stock_Trade_CLI (`PHASE4-QUANT-028`)
- **Full Name**: `PHASE4-QUANT-028_Aniket-16-S__Stock_Trade_CLI`
- **Description**: lightweight CLI application designed to place and manage equity and derivatives orders and view profile details with Dhan's api.
- **GitHub Stars**: 4
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Stock Trading CLI Tool

## What is Stock Trading CLI Tool?

**Stock Trading CLI Tool** is a lightweight, modular command-line interface (CLI) application designed to place and manage equity and derivatives orders via [Dhan's API](https://dhan.co). This project simulates a microservice-like architecture and supports multiple order types such as market, limit, stop-loss, intraday, and F&O, with built-in logging and secure token handling.

This tool is designed for developers and traders who want a programmable interface to interact with their Dhan account for basic trading operations.

---

## Features

- Simple CLI-based interface for order placement and management.
- Supports **Market**, **Limit**, **Stop Loss**, **SL-M**, **IOC**, **CNC**, **Intraday**, **Futures**, and **Options** order types.

- Easy to set up—just add your Dhan credentials to get started.
- Lightweight and dependency-minimal.

---
## Structure 
```bash 
dhan-trading-cli/
|
├── input_handler.py     # Takes and validates user inputs
├── config.py            # Loads and manages credentials securely
├── dhan_trader.py       # Core logic for Dhan API communication
├── main.py              # CLI launcher and user authentication
├── logger.py            # Logs placed orders to CSV
├── requirements.txt     # Python package dependencies
└── .env                 # stores ClientID and Token (excluded from version control - User Specific )
```

---

## Requirements

- A valid [Dhan Trading Account](https://login.dhan.co/?location=DH_WEB&refer=DHAN_WEBSITE)
- Generate your **Client ID** and **Access Token** from the **APIs** section in your Dhan dashboard.

---

## Installation & Setup


1. **Clone the repository**  
```bash
git clone https://github.com/Aniket-16-S/Stock_Trade_CLI.git

```

```bash
cd Stock_Trade_CLI
```

2. **Install the required packages**  
```bash
pip install -r requirements.txt
```


3. **Create `.env` file**  
In the project root dir ( `Stock_Trade_CLI` ) , create a `.env` file and add:

```bash
DHAN_CLIENT_ID=your_client_id_here
DHAN_ACCESS_TOKEN=your_access_token_here
```


4. **Run the application**  
```bash
python main.py
```

The tool will place the order via Dhan API and log successful transactions in a CSV file (`order_log.csv`).


---

## Terms of Use

- This tool uses [Dhan’s  API](https://dhanhq.co/algo-trading/) in accordance with their terms and conditions.
- By using this CLI, you agree to [Dhan’s Terms & Conditions](https://dhan.co) and their [security](https://dhan.co/safety-security/) requirements .
- This project is intended for **educational and demonstrational purposes** only.
- **The developer is not responsible for any financial loss, API issues, or damage arising from use of this tool.**
- Always use caution when placing real trades—validate all inputs carefully.

---

## Notes & Recommendations

- Use this tool with your **main account credentials**, not sandbox/partner accounts.
- Never commit your `.env` file to any version control system.
- You can extend this project to support:
  - GTT orders
  - Portfolio performance tracking
  - Telegram/email alerts
  - Strategy-based bulk orders

---

## Future Goals

- Add support to fetch live market price (LTP).
- Integrate a user-friendly GUI.
- Implement better error handling and retry logic.
- Include additional analytics (PnL reports, portfolio breakdown, etc.).

## License

This project is under internal evaluation as part of an internship program and does not currently use an open-source license.

---

### ⚠️ Disclaimer: 
Use this tool at your own risk. The developer is not responsible for any financial loss, errors, or damages caused by using this code. No guarantees are provided. This project is for educational purposes only.

---

### Core Implementation Code & Architecture
#### File: `Dhan_CLI/__init__.py`
```python

```

#### File: `Dhan_CLI/config.py`
```python
import os
from dotenv import load_dotenv

# Load environment variables from a .env file and update variables if changes were made.
load_dotenv(override=True)

# Fetch DhanHQ credentials
CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

# Validate credentials :
if not CLIENT_ID or not ACCESS_TOKEN:
    raise ValueError("Error: DHAN_CLIENT_ID and DHAN_ACCESS_TOKEN must be set in the .env file.")
    
# CSV Log file :
LOG_FILE = 'order_log.csv'
```

#### File: `Dhan_CLI/order_logger.py`
```python
import csv
from datetime import datetime
import os
from config import LOG_FILE

def log_order_to_csv(order_details, api_response):
    """
    Logs the details of a placed order and its result to a CSV file.

    Args:
        order_details (dict): The dictionary of user-provided order inputs.
        api_response (dict): The response dictionary from <- main <- dhan_trader.
    """

    file_exists = os.path.isfile(LOG_FILE)
    
    # Extract status and order_id from the response
    
    status = api_response.get('status', 'error')
    order_id = api_response.get('orderId', 'N/A')
    
    if status == 'Failed':
        status = f"ERROR: {api_response.get('reason', 'Unknown')}"

    log_data = {
        "Timestamp"   : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Symbol"      : order_details.get('symbol', 'NoSymbolDetected'),
        "Quantity"    : order_details.get('quantity', 'NoQTYdetected'),
        "Order Type"  : order_details.get('order_type', 'OrdTypNotDetected'),
        "Price"       : order_details.get('price', 0) if order_details.get('price', 0) > 0 else "MARKET", 
        "Product Type": order_details.get('trade_type', 'TrdTypNotDetected'),
        "Exchange"    : order_details.get('exchange_segment', 'ExchgSegNotDetected'),
        "Order ID"    : order_id,
        "Status"      : status
    }
    
    headers = log_data.keys()

    try:
        with open(LOG_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            if not file_exists:
                writer.writeheader()  # Write header only if file is newly created when opened.
            writer.writerow(log_data)

        print(f"Order successfully logged to {LOG_FILE}")
    except Exception as e:
        print(f"Error: Could not write to log file {LOG_FILE}. Reason: {e}")
```

#### File: `main.py`
```python
from Dhan_CLI.config import *
from Dhan_CLI.dhan_trader import *
from Dhan_CLI.input_handler import *
from Dhan_CLI.order_logger import *
import sys

def authenticate_user() :
    try:
        global trader # making trader accessiblr to all functions

        #  Initializing the trader with credentials from config
        trader = DhanTrader(client_id=CLIENT_ID, access_token=ACCESS_TOKEN)
        
        if not trader.tradehull :
            print("Exiting application due to authentication failure.")
            sys.exit()  
    except Exception as e :
        print(f"Error : {e}")



def start_order():
    """
    Main function to run the Dhan trading CLI.
    """
    try:

        while True:
            # Geting order details from the user
            order_details = get_order_inputs()

            # Sending the order to the Dhan API
            api_response = trader.place_order(order_details)
            status = trader.get_status(order_id=order_id)
            # Display the outcome to the user
            print("\n--- Order Response ---")
            if api_response and api_response.get('status') == 'success':
                order_id = api_response.get('orderId', 'N/A')
                print(f"   Order placed successfully!")
                print(f"   Order ID  : {order_id}")
                print(f"   Status    : {status}")
            else:
                reason = api_response.get('reason', 'No reason provided.')
                print(f"   Order placement failed. Reason: {reason}")
            
            # Save the transaction record in Log CSV
            log_order_to_csv(order_details, api_response)

            # Ask user if they want to place another order
            another = input("\nDo you want to place another order? (yes/no): ").strip().lower()
            if another != 'yes' or another != 'y':
                break

    except ValueError as ve:
        print(f"\nConfiguration Error in main : {ve}")
    except Exception as e:
        print(f"\nAn unexpected error occurred in main: {e}")

def show_options() :
    print("\n------- Select Operation : -------")
    print("\n1. Place new Oders\n2. Get Order details (requires : Order_ID) \n3. Show current Holdings\n4. Cancel Order (requires : Order_ID)\n5. Cancel ALL Orders\n6. Show Balance\n7. Exit")
    opt = None
    while True :
        try :
            opt = int(input("\n : "))
            if opt in range(1, 8) :
                break
            print("Enter Valid option for operation") # If number is not in correct range
        except Exception :
            print("Enter Valid option for operation") # if user sends characters instead of numbers
    return opt

if __name__ == "__main__":
     
    authenticate_user()

    

    while True :
        opration = show_options()
        if opration == 1 :
            start_order()
        
        elif opration == 2 :
            try :
                order_id = int(input("Enter Order_ID : "))
            except ValueError :
                print("Please ENter correct order id")
                continue
            # We may place logic to verify order id with log file but order can be placed from different systems so . . .
            print(trader.get_order_details(order_id=order_id))
        
        elif opration == 3 :
            print(trader.get_holds())
        
        elif opration == 4 :
            try :
                order_id = int(input("Enter Order_ID : "))
            except ValueError :
                print("Please ENter correct order id")
                continue
            print(trader.cancel_specific_order(order_id=order_id))
        elif opration == 5 :
            print(trader.cancel_orders())
        elif opration == 6 :
            trader.get_balance()
        else :
            break
    
    print("\n\n . . . Thank You for using Dhan CLI Tool . . . \n\n")
```

#### File: `Dhan_CLI/input_handler.py`
```python
def get_order_inputs():
    """
    Collects and validates all necessary order details from the user,
    including specific details for derivative instruments.
    
    """
    print("\n--- Place a New Order ---")

    # Symbol & Exchange
    symbol = input("Enter Symbol (e.g., RELIANCE, NIFTY, BANKNIFTY): ").strip().upper()
    while True:
        segment = input("Enter Exchange Segment (NSE, BSE, NFO): ").strip().upper()
        if segment in {"NSE", "BSE", "NFO"}:
            break
        print("Invalid segment. Please choose from NSE, BSE, NFO.")

    # Derivative Specific Inputs (if NFO) 
    instrument_type = None
    expiry_date = None
    strike_price = 0.0
    option_type = 'NONE'

    if segment == 'NFO':
        while True:
            instrument_type = input("Enter Instrument Type (FUT for Futures, OPT for Options): ").strip().upper()
            if instrument_type in {"FUT", "OPT"}:
                break
            print("Invalid instrument type. Please choose FUT or OPT.")

        expiry_date = input("Enter Expiry Date (YYYY-MM-DD): ").strip()
        
        if instrument_type == 'OPT':
            while True:
                try:
                    strike_price = float(input("Enter Strike Price: ").strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a numerical strike price.")
            
            while True:
                option_type = input("Enter Option Type (CE for Call, PE for Put): ").strip().upper()
                if option_type in {"CE", "PE"}:
                    break
                print("Invalid option type. Please choose CE or PE.")

    # Common Order Details 
    
    #Buy or Sell
    while True:
        side = input("Enter Order Side (BUY, SELL): ").strip().upper()
        if side in {"BUY", "SELL"}:
            break
        print("Invalid side. Please choose BUY or SELL.")

    # Type : Limit / MArket / Stoploss / stoploss-m
    while True:
        order_type = input("Enter Order Type (MARKET, LIMIT, SL, SL-M): ").strip().upper()
        if order_type in {"MARKET", "LIMIT", "SL", "SL-M"}:
            break
        print("Invalid order type. Please choose from MARKET, LIMIT, SL, SL-M.")

    # QTY
    while True:
        try:
            quantity = int(input("Enter Quantity: ").strip())
            if quantity > 0:
                break
            print("Quantity must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")

    price = 0.0

    # Price not applicable if order is for makert price
    if order_type in ["LIMIT", "SL", "SL-M"]:
        while True:
            try:
                price = float(input(f"Enter Price for {order_type} order: ").strip())
                if price > 0:
                    break
                print("Price must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the price.")

    # Share type : intraday / cnc /etc.
    while True:
        product_type = input("Enter Product Type (INTRADAY, CNC, NRML): ").strip().upper()
        if product_type in {"INTRADAY", "CNC", "NRML"}:
            break
        print("Invalid product type. Please choose from INTRADAY, CNC, NRML.")

    # order validity : day / ioc : Immediate or Cancel
    while True:
        validity = input("Enter Order Validity (DAY, IOC): ").strip().upper()
        if validity in {"DAY", "IOC"}:
            break
        print("Invalid validity. Please choose DAY or IOC.")

    # Return a dictionary of responce
    return {
        "symbol": symbol,
        "exchange_segment": segment,
        "instrument_type": instrument_type,
        "expiry_date": expiry_date,
        "strike_price": strike_price,
        "option_type": option_type,
        "transaction_type": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price,
        "trade_type": product_type,
        "validity": validity,
    }

"""
while placing order we use this :
                tradingsymbol       =  order_details ['symbol'],
                exchange            =  order_details ['exchange_segment'],
                quantity            =  order_details ['quantity'],
                price               =  order_details.get('price', 0), # Using .get() with a default for optional parameters
                trigger_price       =  order_details.get('trigger_price', 0),
                order_type          =  order_details ['order_type'],
                transaction_type    =  order_details ['transaction_type'],
                trade_type          =  order_details ['trade_type'], 
                disclosed_quantity  =  order_details.get('disclosed_quantity', 0),
                after_market_order  =  order_details.get('after_market_order', False),
                validity            =  order_details.get('validity', 'DAY'),
                amo_time            =  order_details.get('amo_time', 'OPEN'),
                bo_profit_value     =  order_details.get('bo_profit_value', None),
                bo_stop_loss_Value  =  order_details.get('bo_stop_loss_Value', None)
"""
```

#### File: `Dhan_CLI/dhan_trader.py`
```python
import Dhan_Tradehull as dhan_tradehull 

class DhanTrader:
    def __init__(self, client_id, access_token):
        try:
            #self.dhan = dhanhq(client_id, access_token)   test if not req as tradehull has built in fnc to make this obj.

            # Initialize Dhan_Tradehull with the dhanhq instance
            self.tradehull = dhan_tradehull.Tradehull(client_id, access_token)
            print("DhanHQ client authenticated successfully.")

            self.client_id = client_id
            self.access_token = access_token

        except Exception as e:
            print(f"Failed authenticating or initializing: {e}")
            self.tradehull = None # Ensure tradehull is also None if initialization fails

    def place_order(self, order_details):
        if not self.tradehull: # Check if tradehull is initialized
            return {
                    "status": "Failed", 
                    "reason": "Dhan_Tradehull client not initialized."
                    }

        try:
            print(f"\nPlacing order for {order_details['symbol']} on {order_details['exchange_segment']}")

            response = self.tradehull.order_placement(

                tradingsymbol   =  order_details['symbol'],
                
                exchange        =  order_details['exchange_segment'],
                
                quantity        =  order_details['quantity'],
                
                price           =  order_details.get('price', 0), # Using .get() with a default for optional parameters
                
                trigger_price   =  order_details.get('trigger_price', 0),
                
                order_type      =  order_details['order_type'],
                
                transaction_type    =  order_details['transaction_type'],
                
                trade_type          =  order_details['trade_type'], 
                
                disclosed_quantity  =  order_details.get('disclosed_quantity', 0),
                
                after_market_order  =  order_details.get('after_market_order', False),
                
                validity            =  order_details.get('validity', 'DAY'),
                
                amo_time            =  order_details.get('amo_time', 'OPEN'),
                
                bo_profit_value     =  order_details.get('bo_profit_value', None),
                
                bo_stop_loss_Value  =  order_details.get('bo_stop_loss_Value', None)
            )

            
            # Wraping the response to dic
            if response :
                return {
                        "status": "success",
                        "orderId": response
                        } 
            else :
                return {
                        "status": "Failed", 
                        "reason": response
                        } 

        except Exception as e:
            return {
                    "status": "Failed", 
                    "reason": str(e)
                    }
        
    def get_report(self) :
        # order_report() returns shares report from porfolio in 2 dict s
        order_details, order_exe_price =  self.tradehull.order_report()

        print("Order Details : ")
        for k, v in  order_details.items() :
            print(f"{k} : {v}")

        print("Order exe price : ")
        for k, v in  order_exe_price.items() :
            print(f"{k} : {v}")
    
    def get_status(self, order_id) :
        
        responce = self.tradehull.get_order_status(orderid=order_id)
        responce = responce['data']
        # As responce is like {'status': 'failure', 'remarks': 'list index out of range', 'data': {'status': 'success', 'remarks': '', 'data': []}}
        # i.e. Dic inside Dic

        data = responce.get('data', 'N/A')
        status = responce.get('status', 'Error')
        rem = responce.get('remarks', 'None') 
             
        print(f"Status : {status} \nRemarks : {rem} \nData : {data}")
    
    def get_order_details(self, order_id) :
        
        responce = self.tradehull.get_order_detail(order_id==order_id)
        # As responce is like {'status': 'failure', 'remarks': 'list index out of range', 'data': {'status': 'success', 'remarks': '', 'data': []}}
        # i.e. Dic inside Dic
        responce = responce['data']

        data = responce.get('data', 'N/A')
        status = responce.get('status', 'Error')
        rem = responce.get('remarks', 'None') 
               
        print(f"Status : {status} \nRemarks : {rem} \nData : {data}")


    def get_holds(self) :
        # returns holdings of the day
        responce = self.tradehull.get_holdings()
        for k, v in responce.items() :
            if  "No holdings available" in f" {v} " :
                print("Note : You Have No Holdings Available")
                break
            print(f"\n{k} : {v}")
    
    def cancel_orders(self) :
        # cancels all orders of the dat
        print(self.get_holds())
        sure = input("\n Are you sure to cancel all above orders (y/n) : ")
        if sure.lower() == 'y' :
            responce = self.tradehull.cancel_all_orders()
            for k, v in responce.items() :
                print(f"{k} : {v}")

        
    def cancel_specific_order(self, order_id) :
        # Cancels specific order
        responce =   self.tradehull.cancel_order(OrderID=order_id)
        print(f"responce : {responce}")
        
    
    def get_balance(self) :
        amt = self.tradehull.get_balance()
        print(f"\n Client ID : {self.client_id} \n Balance : {amt}")
```


==================================================
