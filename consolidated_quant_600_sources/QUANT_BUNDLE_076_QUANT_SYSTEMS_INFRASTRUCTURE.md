# ⚡ [QUANT-SOURCE-076] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_076_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: edge (`WHEEL_edge`)
- **Full Name**: `edge`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# EDGE

*Exhaustively Documented, Generally Experimental*

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A broker-agnostic intraday algo trading engine for Indian markets (AngelOne / Kotak Neo), built
around a plug-and-play strategy-plugin core: every strategy is a self-contained class + config
file, discovered automatically, so adding a new one touches no other file. See
[docs/architecture.md](docs/architecture.md) for the full design.

**Execution / data:** AngelOne SmartAPI (Kotak Neo supported for execution, see hybrid setup below)
**Exchanges:** MCX commodity futures · NSE equities (via options signal) · NFO options
**Deployed on:** EC2 (SEBI static-IP requirement for both brokers)

---

## Status

| Strategy | Instrument | Status | Result |
|:---------|:-----------|:-------|:-------|
| `momentum_breakout` | SILVERM MCX 15m | ✅ **Live winner** | Walk-forward OOS +0.218R (85 trades), BUY_ONLY |
| `sr_fvg_breakout` | SILVERM MCX 15m | 🔶 Research in progress | OOS +0.132R but IS fee-negative; needs tuning |
| `options_directional` | NIFTY/BANKNIFTY | 🔴 Framework, paper-only | Not wired into live order placement |

Every other strategy tried (Supertrend, Opening Drive, VWAP-Fade, VWAP-Pullback, Range Scalp) was
backtested, found to have no edge, and deleted — see
[docs/strategy_research_log.md](docs/strategy_research_log.md) for the full record of what was
tried and why it didn't work. Nothing here is a guess; every "abandoned" verdict is backed by a
walk-forward out-of-sample test.

All configs currently ship with `paper_trade: true`. Nothing here places real orders until you
change that deliberately — see [docs/trading_roadmap.md](docs/trading_roadmap.md) for the gate
criteria before doing so.

---

## Quick start

```bash
git clone https://github.com/ajxv/edge.git && cd edge
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
nano .env   # fill in API keys, client IDs, MPIN, TOTP secrets

# Run the example strategy (paper mode, no validated edge — see configs/examples/sma_crossover.yaml).
# This is the fastest way to see the engine run end to end against your own broker login.
python src/bot.py --config configs/examples/sma_crossover.yaml
```

List every registered strategy:
```bash
python -c "from src.strategies.registry import available_strategies; print(available_strategies())"
```

The example above (`example_sma_crossover`) is a plain SMA-crossover template, included to show
the plugin architecture, not because it has any edge. The one strategy in this repo with an actual
walk-forward-validated result is `momentum_breakout` (see Status below and
[docs/strategy_research_log.md](docs/strategy_research_log.md)) — swap in
`configs/live/mcx_momentum.yaml` once you've read [docs/capital_guide.md](docs/capital_guide.md)
and [docs/trading_roadmap.md](docs/trading_roadmap.md). To build your own strategy instead, see
[docs/architecture.md](docs/architecture.md#2-strategy-plugin-system-the-plug-and-play-core) — two
files, no other file touched.

For the fuller step-by-step version of the above (own broker account, own instrument, own
strategy, validation before going live), see [docs/getting_started.md](docs/getting_started.md).

---

## Config layout

```
configs/
  examples/
    sma_crossover.yaml    template strategy, no validated edge, start here
  live/
    mcx_momentum.yaml     the SILVERM winner, paper_trade: true, ready to paper-run
    options.yaml          options_directional, paper-only framework
  research/
    sr_fvg/silverm.yaml   in-progress SR+FVG research config
```

A config's `strategy.type` selects the plugin; `strategy.params` holds that plugin's own
parameters, validated against its registered schema at load time. See
[docs/architecture.md](docs/architecture.md#2-strategy-plugin-system-the-plug-and-play-core) for
the full schema shape and how to add a new strategy (2 steps, no other file touched).

---

## Architecture

```
src/
  bot.py                    Live/paper main loop, strategy-agnostic
  broker_interface.py         BaseBroker abstract contract
  brokers/                    angel_one.py (data), kotak_neo.py (execution, hybrid data_provider)
  core/                       candle_manager, order_manager, state_manager
  services/                   entry_service, exit_service, risk_manager
  strategies/                 base_strategy, registry, example_sma_crossover, momentum_breakout, sr_fvg_breakout, options_directional
  models/config.py            Generic Pydantic config schema
  utils/                      config_loader, strategy_factory, mcx_contract_manager

backtest/
  backtest_engine.py           Bar-by-bar simulator, same strategy interface as live
  run_backtest.py               Single-config, single-symbol backtest CLI
  walk_forward.py               IS/OOS split + Go/No-Go verdict
  exit_matrix.py                Sweep exit variants on a fixed entry config
```

Full walkthrough (live loop data flow, strategy plugin contract, backtest workflow, broker
hybrid pattern and migration notes, state/risk management, deployment) in
[docs/architecture.md](docs/architecture.md).

### Hybrid broker setup

Kotak Neo executes orders (zero brokerage intraday) but has **no historical-data API**
(confirmed against their support docs). AngelOne supplies market data instead:

```
KotakNeoBroker(data_provider=AngelOneBroker)
  -> order placement, positions, margins   -> Kotak Neo
  -> get_ohlc (historical candles)          -> delegates to AngelOne
```

The currently shipped live config uses AngelOne for both data and execution (`active_broker_id:
angel_one`). The hybrid path is available but not required. Both brokers require a **static IP**
(SEBI regulation); the bot runs on EC2 with an Elastic IP — see
[deploy/README.md](deploy/README.md).

---

## Risk management

- **1% risk per trade** (configurable): position sized off the strategy's own structural stop
  (`strategy.get_stop_price`), the same call the backtest engine makes, so live sizing matches
  what was actually validated.
- **Daily circuit breakers**: daily loss %, max trades/day, max consecutive losses.
- **Paper trade mode**: all signals computed and logged, no real orders sent (`paper_trade: true`).
- **Guardrails**: max open positions, max attempts per trend, cautionary symbol list.

---

## Capital

MCX SILVERM (the validated strategy) needs real futures margin. See
[docs/capital_guide.md](docs/capital_guide.md) for current numbers and the honest math on why
smaller capital doesn't work for this domain. If you're capital-constrained, read that doc before
assuming you can just size down.

---

## Backtesting

```bash
# Full walk-forward verdict on the live config (the number that matters before going live)
python backtest/walk_forward.py --config configs/live/mcx_momentum.yaml --split 2026-01-01 --capital 500000

# Single-symbol backtest with a full trade log
python backtest/run_backtest.py --symbol SILVERM --exchange MCX --config configs/live/mcx_momentum.yaml

# Compare exit-structure variants on a fixed entry config
python backtest/exit_matrix.py --config configs/live/mcx_momentum.yaml --split 2026-01-01
```

Go/No-Go thresholds (`backtest/performance_reporter.py`): ≥80 trades, ≥45% win rate, ≥0.3R
expectancy, ≤20% max drawdown. Details in [docs/architecture.md](docs/architecture.md#4-backtest-workflow).

---

## Documentation

| File | Contents |
|:-----|:---------|
| [docs/getting_started.md](docs/getting_started.md) | Setting this up on your own broker account, own credentials, own strategy |
| [docs/architecture.md](docs/architecture.md) | Full system reference (read this first) |
| [docs/strategy_research_log.md](docs/strategy_research_log.md) | Every strategy tried, results, why abandoned |
| [docs/trading_roadmap.md](docs/trading_roadmap.md) | Paper → live gate criteria, current path |
| [docs/capital_guide.md](docs/capital_guide.md) | Capital requirements per domain, worked examples |
| [docs/tuning_guide.md](docs/tuning_guide.md) | Every config parameter, what it does, safe ranges |
| [docs/strategy_guide.md](docs/strategy_guide.md) | Momentum breakout mechanics, MCX fundamentals, log reading |
| [docs/options_guide.md](docs/options_guide.md) | Options education: Greeks, theta, IV, expiry structure |
| [deploy/README.md](deploy/README.md) | EC2 setup, Elastic IP, systemd service |

---

## EC2 deployment

```bash
sudo cp deploy/systemd/tradebot.service /etc/systemd/system/
sudo systemctl enable tradebot
sudo systemctl start tradebot
sudo journalctl -u tradebot -f
```

`deploy/systemd/tradebot.service`'s `ExecStart` pins a `--config` path. See
[deploy/README.md](deploy/README.md) for the full setup guide (Elastic IP is mandatory — both
brokers reject login without a whitelisted static IP).

---

## Contributing

Issues and PRs welcome, bug fixes and new broker adapters especially. Strategy contributions have
one extra bar: no PR adding a strategy gets merged without walk-forward backtest evidence and an
entry in the research log, GO or NO-GO. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License & disclaimer

MIT-licensed, see [LICENSE](LICENSE). This is a software engineering project, not investment
advice or a signal service; see [DISCLAIMER.md](DISCLAIMER.md) for the full terms before using
any part of it with real capital.

Only `momentum_breakout` on SILVERM MCX has a walk-forward-validated edge in this repo, everything
else is either research-in-progress or an unwired framework. Always backtest thoroughly, paper
trade for at least 30 days, and confirm strategy profitability before using real money. Read
[docs/capital_guide.md](docs/capital_guide.md) and
[docs/trading_roadmap.md](docs/trading_roadmap.md) before starting.

### Core Implementation Code & Architecture
#### File: `backtest/__init__.py`
```python

```

#### File: `src/core/__init__.py`
```python

```

#### File: `src/brokers/__init__.py`
```python
from .angel_one import AngelOneBroker
from .kotak_neo import KotakNeoBroker
```

#### File: `src/services/__init__.py`
```python
"""Services package for trading bot.

Provides modular services for risk management, entry, and exit logic.
"""

from .risk_manager import RiskManager
from .entry_service import EntryService
from .exit_service import ExitService

__all__ = ["RiskManager", "EntryService", "ExitService"]
```

#### File: `tests/conftest.py`
```python
"""tests/conftest.py

Shared pytest fixtures for this test suite. Currently empty — each test file
builds its own config/dataframe fixtures scoped to what it actually needs
(see e.g. tests/test_models.py for a full AppConfig builder, or
tests/test_entry_service.py for a MagicMock-based config). Add fixtures here
only once at least two test files would otherwise duplicate them.
"""
```

#### File: `src/strategies/__init__.py`
```python
"""src/strategies — Strategy plugin package.

Each strategy is a self-contained class implementing ``BaseStrategy``, plus
(optionally) a Pydantic params model, registered via ``@register_strategy``
in ``src/strategies/registry.py``. Dropping a new file into this package is
the entire integration step — see registry.py and strategy_factory.py for
the "add a strategy" walkthrough.

Run this to list what's currently registered:
    python -c "from src.strategies.registry import available_strategies; print(available_strategies())"

Status of registered strategies (see docs/strategy_research_log.md for detail):
  - momentum_breakout  : LIVE WINNER — N-bar breakout, SILVERM MCX OOS +0.218R
  - sr_fvg_breakout    : IN PROGRESS — S/R + Fair Value Gap entry, research
  - options_directional: FRAMEWORK / PAPER ONLY — CE/PE buying, not live-wired
"""

from src.strategies.base_strategy import BaseStrategy, Signal

__all__ = ["BaseStrategy", "Signal"]
```


==================================================


## [2/3] Repository: empyrical-reloaded (`WHEEL_empyrical-reloaded`)
- **Full Name**: `empyrical-reloaded`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
<a href="https://empyrical.ml4trading.io">
<img src="https://i.imgur.com/PbZNeud.png" width="35%">
</a>
</p>

![PyPI](https://img.shields.io/pypi/v/empyrical-reloaded)
![PyPI - Downloads](https://img.shields.io/pypi/dm/empyrical-reloaded)

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/empyrical-reloaded.svg)](https://anaconda.org/conda-forge/empyrical-reloaded)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/empyrical-reloaded.svg)](https://anaconda.org/conda-forge/empyrical-reloaded)

[![PyPI Wheels](https://github.com/stefan-jansen/empyrical-reloaded/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/stefan-jansen/empyrical-reloaded/actions/workflows/build_wheels.yml)
[![Conda packages](https://github.com/stefan-jansen/empyrical-reloaded/actions/workflows/conda_package.yml/badge.svg)](https://github.com/stefan-jansen/empyrical-reloaded/actions/workflows/conda_package.yml)
[![CI Tests](https://github.com/stefan-jansen/empyrical-reloaded/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/stefan-jansen/empyrical-reloaded/actions/workflows/unit_tests.yml)

Common financial return and risk metrics in Python.

## Installation

empyrical requires Python 3.10+. You can install it using `pip`:

```bash
pip install empyrical-reloaded
```

or `conda` from the `conda-forge` channel

```bash
conda install empyrical-reloaded -c conda-forge
```

empyrical requires and installs the following packages while executing the above commands:

- numpy>=1.23.5
- pandas>=1.3.0
- scipy>=0.15.1

> Note that Numpy>=2.0 requires pandas>=2.2.2. If you are using an older version of pandas, you may need to upgrade
> accordingly, otherwise you may encounter compatibility issues.

Optional dependencies include [yfinance](https://github.com/ranaroussi/yfinance) to download price data
from [Yahoo! Finance](https://finance.yahoo.com/)
and [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/) to
access [Fama-French](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) risk factors and FRED
treasury yields.

> Note that `pandas-datareader` is not compatible with Python>=3.12.

To install the optional dependencies, use:

```bash
pip install empyrical-reloaded[yfinance]
```

or

```bash
pip install empyrical-reloaded[datreader]
```

or

```bash
pip install empyrical-reloaded[yfinance,datreader]
```

## Usage

### Simple Statistics

Empyrical computes basic metrics from returns and volatility to alpha and beta, Value at Risk, and Sharpe or Sortino
ratios.

```python
import numpy as np
from empyrical import max_drawdown, alpha_beta

returns = np.array([.01, .02, .03, -.4, -.06, -.02])
benchmark_returns = np.array([.02, .02, .03, -.35, -.05, -.01])

# calculate the max drawdown
max_drawdown(returns)

# calculate alpha and beta
alpha, beta = alpha_beta(returns, benchmark_returns)
```

### Rolling Measures

Empyrical also aggregates return and risk metrics for rolling windows:

```python
import numpy as np
from empyrical import roll_max_drawdown

returns = np.array([.01, .02, .03, -.4, -.06, -.02])

# calculate the rolling max drawdown
roll_max_drawdown(returns, window=3)
```

### Pandas Support

Empyrical also works with both [NumPy](https://numpy.org/) arrays and [Pandas](https://pandas.pydata.org/) data
structures:

```python
import pandas as pd
from empyrical import roll_up_capture, capture

returns = pd.Series([.01, .02, .03, -.4, -.06, -.02])
factor_returns = pd.Series([.02, .01, .03, -.01, -.02, .02])

# calculate a capture ratio
capture(returns, factor_returns)
-0.147387712263491

```

### Fama-French Risk Factors

Empyrical downloads Fama-French risk factors from 1970 onward:

> Note: requires optional dependency `pandas-datareader` - see installation instructions above.gst

```python
import pandas as pd
import empyrical as emp

risk_factors = emp.utils.get_fama_french()

pd.concat([risk_factors.head(), risk_factors.tail()])

Mkt - RF
SMB
HML
RF
Mom
Date
1970 - 01 - 02
00: 00:00 + 00: 00
0.0118
0.0129
0.0101
0.00029 - 0.0340
1970 - 01 - 05
00: 00:00 + 00: 00
0.0059
0.0067
0.0072
0.00029 - 0.0153
1970 - 01 - 06
00: 00:00 + 00: 00 - 0.0074
0.0010
0.0021
0.00029
0.0038
1970 - 01 - 07
00: 00:00 + 00: 00 - 0.0015
0.0040 - 0.0033
0.00029
0.0011
1970 - 01 - 0
8
00: 00:00 + 00: 00
0.0004
0.0018 - 0.0017
0.00029
0.0033
2024 - 03 - 22
00: 00:00 + 00: 00 - 0.0023 - 0.0087 - 0.0053
0.00021
0.0043
2024 - 03 - 25
00: 00:00 + 00: 00 - 0.0026 - 0.0024
0.0088
0.00021 - 0.0034
2024 - 03 - 26
00: 00:00 + 00: 00 - 0.0026
0.0009 - 0.0013
0.00021
0.0009
2024 - 03 - 27
00: 00:00 + 00: 00
0.0088
0.0104
0.0091
0.00021 - 0.0134
2024 - 03 - 28
00: 00:00 + 00: 00
0.0010
0.0029
0.0048
0.00021 - 0.0044
```

### Asset Prices and Benchmark Returns

Empyrical use [yfinance](https://github.com/ranaroussi/yfinance) to download price data
from [Yahoo! Finance](https://finance.yahoo.com/). To obtain the S&P returns since 1950, use:

> Note: requires optional dependency `yfinance` - see installation instructions above.

```python
import empyrical as emp

symbol = '^GSPC'
returns = emp.utils.get_symbol_returns_from_yahoo(symbol,
                                                  start='1950-01-01')

import seaborn as sns  # requires separate installation
import matplotlib.pyplot as plt  # requires separate installation

fig, axes = plt.subplots(ncols=2, figsize=(14, 5))

with sns.axes_style('whitegrid'):
    returns.plot(ax=axes[0], rot=0, title='Time Series', legend=False)
    sns.histplot(returns, ax=axes[1], legend=False)
axes[1].set_title('Histogram')
sns.despine()
plt.tight_layout()
plt.suptitle('Daily S&P 500 Returns')
```

<a href="https://empyrical.ml4trading.io">
<img src="https://i.imgur.com/0PSxfSI.png" width="100%">
</a>

### Documentation

See the [documentation](https://empyrical.ml4trading.io) for details on the API.

## Support

Please [open an issue](https://github.com/stefan-jansen/empyrical-reloaded/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits,
and [open a pull request](https://github.com/stefan-jansen/empyrical-reloaded/compare/).

## Testing

- install requirements
    - "pytest>=6.2.0",

```bash
pytest tests
```

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `src/empyrical/periods.py`
```python
APPROX_BDAYS_PER_MONTH = 21
APPROX_BDAYS_PER_YEAR = 252

MONTHS_PER_YEAR = 12
WEEKS_PER_YEAR = 52
QTRS_PER_YEAR = 4

DAILY = "daily"
WEEKLY = "weekly"
MONTHLY = "monthly"
QUARTERLY = "quarterly"
YEARLY = "yearly"

ANNUALIZATION_FACTORS = {
    DAILY: APPROX_BDAYS_PER_YEAR,
    WEEKLY: WEEKS_PER_YEAR,
    MONTHLY: MONTHS_PER_YEAR,
    QUARTERLY: QTRS_PER_YEAR,
    YEARLY: 1,
}
```

#### File: `src/empyrical/deprecate.py`
```python
"""Utilities for marking deprecated functions."""

# Copyright 2018 Quantopian, Inc.
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

import warnings
from functools import wraps


def deprecated(msg=None, stacklevel=2):
    """
    Used to mark a function as deprecated.
    Parameters
    ----------
    msg : str
        The message to display in the deprecation warning.
    stacklevel : int
        How far up the stack the warning needs to go, before
        showing the relevant calling lines.
    Usage
    -----
    @deprecated(msg='function_a is deprecated! Use function_b instead.')
    def function_a(*args, **kwargs):
    """

    def deprecated_dec(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            warnings.warn(
                msg or "Function %s is deprecated." % fn.__name__,
                category=DeprecationWarning,
                stacklevel=stacklevel,
            )
            return fn(*args, **kwargs)

        return wrapper

    return deprecated_dec
```

#### File: `src/empyrical/__init__.py`
```python
#
# Copyright 2016 Quantopian, Inc.
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
# flake8: noqa

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")

from .stats import (
    aggregate_returns,
    alpha,
    alpha_aligned,
    alpha_beta,
    alpha_beta_aligned,
    annual_return,
    annual_volatility,
    beta,
    beta_aligned,
    cagr,
    beta_fragility_heuristic,
    beta_fragility_heuristic_aligned,
    gpd_risk_estimates,
    gpd_risk_estimates_aligned,
    calmar_ratio,
    capture,
    conditional_value_at_risk,
    cum_returns,
    cum_returns_final,
    down_alpha_beta,
    down_capture,
    downside_risk,
    excess_sharpe,
    max_drawdown,
    omega_ratio,
    roll_alpha,
    roll_alpha_aligned,
    roll_alpha_beta,
    roll_alpha_beta_aligned,
    roll_annual_volatility,
    roll_beta,
    roll_beta_aligned,
    roll_down_capture,
    roll_max_drawdown,
    roll_sharpe_ratio,
    roll_sortino_ratio,
    roll_up_capture,
    roll_up_down_capture,
    sharpe_ratio,
    simple_returns,
    sortino_ratio,
    stability_of_timeseries,
    tail_ratio,
    up_alpha_beta,
    up_capture,
    up_down_capture,
    batting_average,
    value_at_risk,
)

from .periods import DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY


from .perf_attrib import (
    perf_attrib,
    compute_exposures,
)
```

#### File: `docs/deploy.py`
```python
#!/usr/bin/env python
from contextlib import contextmanager
from glob import glob
import os
from os.path import basename, exists, isfile
from pathlib import Path
from shutil import move, rmtree
from subprocess import check_call

HERE = Path(__file__).resolve(strict=True).parent
EMPYRICAL_ROOT = HERE.parent
TEMP_LOCATION = "/tmp/empyrical-doc"
TEMP_LOCATION_GLOB = TEMP_LOCATION + "/*"


@contextmanager
def removing(path):
    try:
        yield
    finally:
        rmtree(path)


def ensure_not_exists(path):
    if not exists(path):
        return
    if isfile(path):
        os.unlink(path)
    else:
        rmtree(path)


def main():
    old_dir = Path.cwd()
    print("Moving to %s." % HERE)
    os.chdir(HERE)

    try:
        print("Cleaning docs with 'make clean'")
        check_call(["make", "clean"])
        print("Building docs with 'make html'")
        check_call(["make", "html"])

        print("Clearing temp location '%s'" % TEMP_LOCATION)
        rmtree(TEMP_LOCATION, ignore_errors=True)

        with removing(TEMP_LOCATION):
            print("Copying built files to temp location.")
            move("build/html", TEMP_LOCATION)

            print("Moving to '%s'" % EMPYRICAL_ROOT)
            os.chdir(EMPYRICAL_ROOT)

            print("Checking out gh-pages branch.")
            check_call(
                [
                    "git",
                    "branch",
                    "-f",
                    "--track",
                    "gh-pages",
                    "origin/gh-pages",
                ]
            )
            check_call(["git", "checkout", "gh-pages"])
            check_call(["git", "reset", "--hard", "origin/gh-pages"])

            print("Copying built files:")
            for file_ in glob(TEMP_LOCATION_GLOB):
                base = basename(file_)

                print("%s -> %s" % (file_, base))
                ensure_not_exists(base)
                move(file_, ".")
    finally:
        os.chdir(old_dir)

    print()
    print("Updated documentation branch in directory %s" % EMPYRICAL_ROOT)
    print("If you are happy with these changes, commit and push to gh-pages.")


if __name__ == "__main__":
    main()
```

#### File: `docs/source/conf.py`
```python
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import pydata_sphinx_theme
from empyrical import __version__ as version

sys.path.insert(0, Path("../..").resolve(strict=True).as_posix())


# This is the expected signature of the handler for this event, cf doc
def autodoc_skip_member_handler(app, what, name, obj, skip, options):
    # Basic approach; you might want a regex instead
    return name.startswith(("cache", "_"))


# Automatically called by sphinx at startup
def setup(app):
    # Connect the autodoc-skip-member event from apidoc to the callback
    app.connect("autodoc-skip-member", autodoc_skip_member_handler)


extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "m2r2",
    "sphinx_markdown_tables",
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
]

templates_path = ["_templates"]

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

master_doc = "index"

project = "empyrical"
copyright = "2016, Quantopian, Inc."
author = "Quantopian, Inc."

release = version
language = None

exclude_patterns = []

highlight_language = "python"

pygments_style = "sphinx"

todo_include_todos = False

html_theme = "pydata_sphinx_theme"
html_theme_path = pydata_sphinx_theme.get_html_theme_path()

html_theme_options = {
    "github_url": "https://github.com/stefan-jansen/empyrical-reloaded",
    "twitter_url": "https://twitter.com/ml4trading",
    "external_links": [
        {"name": "ML for Trading", "url": "https://ml4trading.io"},
        {"name": "Community", "url": "https://exchange.ml4trading.io"},
    ],
    "google_analytics_id": "UA-74956955-3",
    "use_edit_page_button": True,
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "stefan-jansen",
    "github_repo": "empyrical-reloaded",
    "github_version": "main",
    "doc_path": "docs/source",
}

html_static_path = []

htmlhelp_basename = "Empyricaldoc"

latex_elements = {}

latex_documents = [
    (
        master_doc,
        "Empyrical.tex",
        "Empyrical Documentation",
        "Quantopian, Inc.",
        "manual",
    )
]

man_pages = [(master_doc, "empyrical", "Empyrical Documentation", [author], 1)]

texinfo_documents = [
    (
        master_doc,
        "Empyrical",
        "Empyrical Documentation",
        author,
        "Empyrical",
        "One line description of project.",
        "Miscellaneous",
    )
]
```


==================================================


## [3/3] Repository: fastfetch (`WHEEL_fastfetch`)
- **Full Name**: `fastfetch`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Fastfetch

[![Benchmark](https://img.shields.io/badge/GitHub%20Pages-live-blue?logo=github)](https://fastfetch-cli.github.io/fastfetch/dev/bench)
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/fastfetch-cli/fastfetch/ci.yml)](https://github.com/fastfetch-cli/fastfetch/actions)
[![GitHub license](https://img.shields.io/github/license/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/blob/dev/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/graphs/contributors)
[![GitHub top language](https://img.shields.io/github/languages/top/fastfetch-cli/fastfetch?logo=c&label=)](https://github.com/fastfetch-cli/fastfetch/blob/dev/CMakeLists.txt#L5)
[![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/fastfetch-cli/fastfetch)](https://github.com/fastfetch-cli/fastfetch/commits)  
[![homebrew downloads](https://img.shields.io/homebrew/installs/dm/fastfetch?logo=homebrew)](https://formulae.brew.sh/formula/fastfetch#default)
[![GitHub all releases](https://img.shields.io/github/downloads/fastfetch-cli/fastfetch/total?logo=github)](https://github.com/fastfetch-cli/fastfetch/releases)  
[![GitHub release (with filter)](https://img.shields.io/github/v/release/fastfetch-cli/fastfetch?logo=github)](https://github.com/fastfetch-cli/fastfetch/releases)
[![latest packaged version(s)](https://repology.org/badge/latest-versions/fastfetch.svg)](https://repology.org/project/fastfetch/versions)
[![Packaging status](https://repology.org/badge/tiny-repos/fastfetch.svg)](https://repology.org/project/fastfetch/versions)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/fastfetch-cli/fastfetch)
[![中文README](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-README-red)](README-cn.md)

Fastfetch is a [neofetch](https://github.com/dylanaraps/neofetch)-like tool for fetching system information and displaying it in a visually appealing way. It is written mainly in C, with a focus on performance and customizability. Currently, it supports Linux, macOS, Windows 8.1+, Android, FreeBSD, OpenBSD, NetBSD, DragonFly, Haiku and SunOS (illumos, Solaris).

> Note: Fastfetch is only actively tested on x86-64 and aarch64 platforms. It may work on other platforms but is not guaranteed to do so.

<img src="screenshots/example1.png" width="49%" align="left" />
<img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Transparent_Square_Tiles_Texture.png" width="49%" height="16px" align="left" />
<img src="screenshots/example4.png" width="49%" align="left" />
<img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Transparent_Square_Tiles_Texture.png" width="49%" height="16px" align="left" />
<img src="screenshots/example2.png" width="48%" align="top" />
<img src="screenshots/example3.png" width="48%" align="top" />
<img src="screenshots/example5.png" height="15%" align="top" />

According configuration files for examples are located [here](https://github.com/fastfetch-cli/fastfetch/tree/dev/presets/examples).

There are [screenshots on different platforms](https://github.com/fastfetch-cli/fastfetch/wiki).

## Installation

### Linux

Some distributions package outdated versions of fastfetch. Older versions receive no support, so please always try to use the latest version.

<a href="https://repology.org/project/fastfetch/versions">
    <img src="https://repology.org/badge/vertical-allrepos/fastfetch.svg?columns=2" alt="Packaging status" align="right">
</a>

* Ubuntu: [`ppa:zhangsongcui3371/fastfetch`](https://launchpad.net/~zhangsongcui3371/+archive/ubuntu/fastfetch) (Ubuntu 22.04 or newer; latest version)
* Debian / Ubuntu: `apt install fastfetch` (Debian 13 or newer; Ubuntu 25.04 or newer)
* Debian / Ubuntu: Download `fastfetch-linux-<proper architecture>.deb` from [Github release page](https://github.com/fastfetch-cli/fastfetch/releases/latest) and double-click it (for Ubuntu 20.04 or newer and Debian 11 or newer).
* Arch Linux: `pacman -S fastfetch`
* Fedora: `dnf install fastfetch`
* Gentoo: `emerge --ask app-misc/fastfetch`
* Alpine: `apk add --upgrade fastfetch`
* NixOS: `nix-shell -p fastfetch`
* openSUSE: `zypper install fastfetch`
* ALT Linux: `apt-get install fastfetch`
* Exherbo: `cave resolve --execute app-misc/fastfetch`
* Solus: `eopkg install fastfetch`
* Slackware: `sbopkg -i fastfetch`
* Void Linux: `xbps-install fastfetch`
* Venom Linux: `scratch install fastfetch`

You may need `sudo`, `doas`, or `sup` to run these commands.

If fastfetch is not packaged for your distribution or an outdated version is packaged, [linuxbrew](https://brew.sh/) is a good alternative: `brew install fastfetch`

### macOS

* [Homebrew](https://formulae.brew.sh/formula/fastfetch#default): `brew install fastfetch`
* [MacPorts](https://ports.macports.org/port/fastfetch/): `sudo port install fastfetch`

### Windows

* [scoop](https://scoop.sh/#/apps?q=fastfetch): `scoop install fastfetch`
* [Chocolatey](https://community.chocolatey.org/packages/fastfetch): `choco install fastfetch`
* [winget](https://github.com/microsoft/winget-pkgs/tree/master/manifests/f/Fastfetch-cli/Fastfetch): `winget install fastfetch`
* [MSYS2 MinGW](https://packages.msys2.org/base/mingw-w64-fastfetch): `pacman -S mingw-w64-<subsystem>-<arch>-fastfetch`

You may also download the program directly from [the GitHub releases page](https://github.com/fastfetch-cli/fastfetch/releases/latest) in the form of an archive file.

### BSD systems

* FreeBSD: `pkg install fastfetch`
* NetBSD: `pkgin in fastfetch`
* OpenBSD: `pkg_add fastfetch` (Snapshots only)
* DragonFly BSD: `pkg install fastfetch` (Snapshots only)

### Android (Termux)

* `pkg install fastfetch`

### Nightly

<https://nightly.link/fastfetch-cli/fastfetch/workflows/ci/dev?preview>

## Build from source

See the Wiki: https://github.com/fastfetch-cli/fastfetch/wiki/Building

## Usage

* Run with default configuration: `fastfetch`
* Run with [all supported modules](https://github.com/fastfetch-cli/fastfetch/wiki/Support+Status#available-modules) to find what interests you: `fastfetch -c all.jsonc`
* View all data that fastfetch detects: `fastfetch -s <module1>[:<module2>][:<module3>] --format json`
* Display help messages: `fastfetch --help`
* Generate a minimal config file: `fastfetch [-s <module1>[:<module2>]] --gen-config [</path/to/config.jsonc>]`
    * Use [The online configuration generator](https://fastfetch-cli.github.io/fastfetch-config/) to generate a full config file with all optional options

## Customization

Fastfetch uses JSONC (JSON with comments) for configuration. [See the Wiki for details](https://github.com/fastfetch-cli/fastfetch/wiki/Configuration). There are some premade config files in the [`presets`](presets) directory, including those used for the screenshots above. You can load them using `-c <filename>`. These files can serve as examples of the configuration syntax.

Logos can also be heavily customized; see the [logo documentation](https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options) for more information.

### WARNING

Fastfetch supports a `Command` module that can run arbitrary shell commands. If you copy-paste a config file from an untrusted source, it may contain malicious commands that can harm your system or compromise your privacy. Please always review the config file before using it.

## FAQ

### Q: Neofetch is good enough. Why do I need fastfetch?

1. Fastfetch is actively maintained.
2. Fastfetch is faster, as the name suggests.
3. Fastfetch has a greater number of features, though by default it only has a few modules enabled; use `fastfetch -c all` to discover what you want.
4. Fastfetch is more configurable. You can find more information in the Wiki: <https://github.com/fastfetch-cli/fastfetch/wiki/Configuration>.
5. Fastfetch is more polished. For example, neofetch prints `555 MiB` in the Memory module and `23 G` in the Disk module, whereas fastfetch prints `555.00 MiB` and `22.97 GiB` respectively.
6. Fastfetch is more accurate. For example, [neofetch never actually supports the Wayland protocol](https://github.com/dylanaraps/neofetch/pull/2395).

### Q: Fastfetch shows my local IP address. Does it leak my privacy?

A local IP address (10.x.x.x, 172.x.x.x, 192.168.x.x) has nothing to do with privacy. It only has meaning if you are on the same network, for example, if you connect to the same Wi-Fi network.

Actually, the `Local IP` module is the most useful module for me personally. I (@CarterLi) have several VMs installed to test fastfetch and often need to SSH into them. With fastfetch running on shell startup, I never need to type `ip addr` manually.

If you really don't like it, you can disable the `Local IP` module in `config.jsonc`.

### Q: Where is the config file? I can't find it.

Fastfetch does not generate a config file automatically. You can use `fastfetch --gen-config` to generate one. The config file will be saved in `~/.config/fastfetch/config.jsonc` by default. See the [Wiki for details](https://github.com/fastfetch-cli/fastfetch/wiki/Configuration).

### Q: The configuration is so complex. Where is the documentation?

Fastfetch uses JSON (with comments) for configuration. I suggest using an IDE with JSON schema support (like VSCode) to edit it.

Alternatively, you can refer to the presets in the [`presets` directory](https://github.com/fastfetch-cli/fastfetch/tree/dev/presets).

The **correct** way to edit the configuration:

This is an example that [changes size prefix from MiB / GiB to MB / GB](https://github.com/fastfetch-cli/fastfetch/discussions/1014). Editor used: [helix](https://github.com/helix-editor/helix)

[![asciicast](https://asciinema.org/a/1uF6sTPGKrHKI1MVaFcikINSQ.svg)](https://asciinema.org/a/1uF6sTPGKrHKI1MVaFcikINSQ)

### Q: I WANT THE DOCUMENTATION!

[Here is the documentation](https://github.com/fastfetch-cli/fastfetch/wiki/Json-Schema). It is generated from the [JSON schema](https://github.com/fastfetch-cli/fastfetch/blob/dev/doc/json_schema.json), but you might not find it very user-friendly.

### Q: How can I customize the module output?

Fastfetch uses `format` to generate output. For example, to make the `GPU` module show only the GPU name (leaving other information undisplayed), you can use:

```jsonc
{
    "modules": [
        {
            "type": "gpu",
            "format": "{name}" // See `fastfetch -h gpu-format` for details
        }
    ]
}
```

...which is equivalent to `fastfetch -s gpu --gpu-format '{name}'`

See `fastfetch -h format` for information on basic usage. For module-specific formatting, see `fastfetch -h <module>-format`

### Q: I have my own ASCII art / image file. How can I show it with fastfetch?

Try `fastfetch -l /path/to/logo`. See the [logo documentation](https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options) for details.

If you just want to display the distro name in [FIGlet text](https://github.com/pwaller/pyfiglet):

```bash
# install pyfiglet and jq first
pyfiglet -s -f small_slant $(fastfetch -s os --format json | jq -r '.[0].result.name') && fastfetch -l none
```

![image](https://github.com/fastfetch-cli/fastfetch/assets/6134068/6466524e-ab8c-484f-848d-eec7ddeb7df2)

### Q: My image logo behaves strangely. How can I fix it?

See the troubleshooting section: <https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options#troubleshooting>

### Q: Fastfetch runs in black and white on shell startup. Why?

This issue usually occurs when using fastfetch with `p10k`. There are known incompatibilities between fastfetch and p10k instant prompt.
The p10k documentation clearly states that you should NOT print anything to stdout after `p10k-instant-prompt` is initialized. You should put `fastfetch` before the initialization of `p10k-instant-prompt` (recommended).

You can always use `fastfetch --pipe false` to force fastfetch to run in colorful mode.

### Q: Why do fastfetch and neofetch show different memory usage results?

See [#1096](https://github.com/fastfetch-cli/fastfetch/issues/1096).

### Q: Fastfetch shows fewer dpkg packages than neofetch. Is it a bug?

1. Neofetch incorrectly counts `rc` packages for apt (packages that have been removed but still have configuration files remaining). See bug: https://github.com/dylanaraps/neofetch/issues/2278
2. Neofetch incorrectly counts `gpg-pubkey` as packages for rpm. You may check the results of `dnf list --installed | wc -l` and `rpm -qa | wc -l` to see the difference.

### Q: I use Debian / Ubuntu / Debian-derived distro. My GPU is detected as `XXXX Device XXXX (VGA compatible)`. Is this a bug?

Try upgrading `pci.ids`: Download <https://pci-ids.ucw.cz/v2.2/pci.ids> and overwrite the file `/usr/share/hwdata/pci.ids`. For AMD GPUs, you should also upgrade `amdgpu.ids`: Download <https://gitlab.freedesktop.org/mesa/drm/-/raw/main/data/amdgpu.ids> and overwrite the file `/usr/share/libdrm/amdgpu.ids`

Alternatively, you may try using `fastfetch --gpu-driver-specific`, which will make fastfetch attempt to ask the driver for the GPU name if supported.

### Q: I get the error `Authorization required, but no authorization protocol specified` when running fastfetch as root

Try `export XAUTHORITY=$HOME/.Xauthority`

### Q: Fastfetch cannot detect my awesome 3rd-party macOS window manager!

Try `fastfetch --wm-detect-plugin`. See also [#984](https://github.com/fastfetch-cli/fastfetch/issues/984)

### Q: How can I change the colors of my ASCII logo?

Try `fastfetch --logo-color-[1-9] <color>`, where `[1-9]` is the index of color placeholders.

For example: `fastfetch --logo-color-1 red --logo-color-2 green`.

In JSONC, you can use:

```jsonc
{
    "logo": {
        "color": {
            "1": "red",
            "2": "green"
        }
    }
}
```

### Q: How do I hide a key?

Set the key to a white space.

```jsonc
{
    "key": " "
}
```

### Q: How can I display images on Windows?

As of April 2025:

#### mintty and Wezterm

mintty (used by Bash on Windows and MSYS2) and Wezterm (nightly build only) support the iTerm image protocol on Windows.

In `config.jsonc`:  
```json
{
  "logo": {
    "type": "iterm",
    "source": "C:/path/to/image.png",
    "width": <num-in-chars>
  }
}
```

#### Windows Terminal

Windows Terminal supports the sixel image protocol only.

* If you installed fastfetch through MSYS2:
    1. Install imagemagick: `pacman -S mingw-w64-<subsystem>-x86_64-imagemagick`
    2. In `config.jsonc`:  
```jsonc
{
  "logo": {
    "type": "sixel", // DO NOT USE "auto"
    "source": "C:/path/to/image.png", // Do NOT use `~` as fastfetch is a native Windows program and doesn't apply cygwin path conversion
    "width": <image-width-in-chars>, // Optional
    "height": <image-height-in-chars> // Optional
  }
}
```
* If you installed fastfetch via scoop or downloaded the binary directly from the GitHub Releases page:
    1. Convert your image manually to sixel format using [any online image conversion service](https://www.google.com/search?q=convert+image+to+sixel)
    2. In `config.jsonc`:  
```jsonc
{
  "logo": {
    "type": "raw", // DO NOT USE "auto"
    "source": "C:/path/to/image.sixel",
    "width": <image-width-in-chars>, // Required
    "height": <image-height-in-chars> // Required
  }
}
```

### Q: I want feature A / B / C. Will fastfetch support it?

Fastfetch is a system information tool. We only accept hardware or system-level software feature requests. For most personal uses, I recommend using the `Command` module to implement custom functionality, which can be used to grab output from a custom shell script:

```jsonc
// This module shows the default editor
{
    "modules": [
        {
            "type": "command",
            "text": "$EDITOR --version | head -1",
            "key": "Editor"
        }
    ]
}
```

Otherwise, please open a feature request in [GitHub Issues](https://github.com/fastfetch-cli/fastfetch/issues).

### Q: I have questions. Where can I get help?

* For usage questions, please start a discussion in [GitHub Discussions](https://github.com/fastfetch-cli/fastfetch/discussions).
* For possible bugs, please open an issue in [GitHub Issues](https://github.com/fastfetch-cli/fastfetch/issues). Be sure to fill out the bug report template carefully to help developers investigate.

## Donate

If you find Fastfetch useful, please consider donating.

* Current maintainer: [@CarterLi](https://paypal.me/zhangsongcui)
* Original author: [@LinusDierheimer](https://github.com/sponsors/LinusDierheimer)

## Code signing

* Free code signing provided by [SignPath.io](https://about.signpath.io/), certificate by [SignPath Foundation](https://signpath.org/)
* This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it

## Star History

Give us a star to show your support!

<a href="https://star-history.dera.page/#fastfetch-cli/fastfetch&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=fastfetch-cli/fastfetch&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=fastfetch-cli/fastfetch&type=Date" />
    <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=fastfetch-cli/fastfetch&type=Date" />
  </picture>
</a>

### Core Implementation Code & Architecture
#### File: `src/3rdparty/yyjson/repo.json`
```python
{
    "home": "https://github.com/ibireme/yyjson",
    "license": "MIT ( embed in source )",
    "version": "0.13.0",
    "author": "ibireme"
}
```

#### File: `src/3rdparty/widecharwidth/repo.json`
```python
{
    "home": "https://github.com/ridiculousfish/widecharwidth",
    "license": "Public domain",
    "version": "Unicode 17",
    "author": "ridiculousfish"
}
```

#### File: `src/3rdparty/display-library/repo.json`
```python
{
    "home": "https://github.com/GPUOpen-LibrariesAndSDKs/display-library",
    "license": "MIT (embeded in source)",
    "version": "ADL SDK 18.1",
    "author": "Advanced Micro Devices, Inc"
}
```

#### File: `src/detection/bootmgr/bootmgr_haiku.cpp`
```python
extern "C" {
    #include "bootmgr.h"
    #include "common/io.h"
}

const char* ffDetectBootmgr(FFBootmgrResult* result) {
    // TODO: glob haiku_loader.* + check EFI partition
    if (ffPathExists("/system/haiku_loader.bios_ia32", FF_PATHTYPE_FILE)) {
        ffStrbufSetStatic(&result->firmware, "/system/haiku_loader.bios_ia32");
    }

    ffStrbufSetStatic(&result->name, "haiku_loader");

    // TODO: detectSecureBoot(&result->secureBoot);

    return nullptr;
}
```

#### File: `src/common/windows/variant.cpp`
```python
#include "variant.hpp"

#include <oleauto.h>

FFWmiVariant::FFWmiVariant(std::initializer_list<PCWSTR> strings) : FFWmiVariant() {
    SAFEARRAYBOUND bound = {
        .cElements = (ULONG) strings.size(),
        .lLbound = 0,
    };
    SAFEARRAY* psa = SafeArrayCreate(VT_BSTR, 1, &bound);

    LONG i = 0;
    for (PCWSTR str : strings) {
        SafeArrayPutElement(psa, &i, bstr_t(str));
        ++i;
    }

    this->vt = VT_ARRAY | VT_BSTR;
    this->parray = psa;
}
```

#### File: `src/common/windows/util.hpp`
```python
#pragma once

#include <utility>
#include <type_traits>

template <typename Fn>
struct on_scope_exit {
    static_assert(std::is_nothrow_move_constructible<Fn>::value,
        "Fn must be nothrow move constructible");

    explicit on_scope_exit(Fn&& fn) noexcept
        : _fn(std::move(fn)) {};
    on_scope_exit(const on_scope_exit&) = delete;
    on_scope_exit& operator=(const on_scope_exit&) = delete;
    ~on_scope_exit() noexcept {
        this->_fn();
    }

  private:
    Fn _fn;
};
```


==================================================
