# ⚡ [QUANT-SOURCE-192] Consolidated Quant & Algo Trading Repositories
**Category**: `EVENT_DRIVEN_BACKTESTERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_192_EVENT_DRIVEN_BACKTESTERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: dbt-core (`VAULT_IN-QUANT-044_dbt-labs__dbt-core`)
- **Full Name**: `IN-QUANT-044_dbt-labs__dbt-core`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<p align="center">
  <img width="750" alt="dbt logo" src="https://github.com/user-attachments/assets/26b0c2cd-70c1-4aa2-b66a-cda491ffa99c" />
</p>
<p align="center">
  <a href="https://github.com/dbt-labs/dbt-core/actions/workflows/main.yml">
    <img src="https://github.com/dbt-labs/dbt-core/actions/workflows/main.yml/badge.svg?event=push" alt="CI Badge"/>
  </a>
</p>

> [!WARNING]
> **dbt v1 development has moved to the [`1.latest`](https://github.com/dbt-labs/dbt/tree/1.latest) branch.**
> The `main` branch now contains all the Apache 2.0 source code of dbt v2.0 — a ground-up rewrite of dbt in Rust. If you're looking for the v1 Python implementation of the dbt framework, switch to [`1.latest`](https://github.com/dbt-labs/dbt/tree/1.latest).

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

![architecture](https://raw.githubusercontent.com/dbt-labs/dbt/202cb7e51e218c7b29eb3b11ad058bd56b7739de/etc/dbt-transform.png)

## About dbt v2.0

> 🚧 dbt v2.0 is in beta. Behavior, APIs, and on-disk formats may change before the stable release.

dbt v2.0 is engineered for performance at scale. It parses, compiles, and runs projects in a fraction of the time compared to v1. The source code in this repository is available to everyone under the standard Apache 2.0 license. [dbt](https://docs.getdbt.com/docs/introduction) is a distribution of the dbt repository with dbt-specific customizations released under a [dbt product license](https://www.getdbt.com/dbt-fusion-engine-license-agreement).

The big shifts from v1:

- **Faster** — parse and compile times are dramatically improved, especially on the largest dbt projects.
- **Stricter** — a tightly-defined language specification enforces correctness at parse time.
- **More scalable artifacts** — v2.0 produces Parquet artifacts that can be easily queried, joined, and analyzed to understand your dbt project. The artifacts encompass everything in the JSON artifacts (e.g. `manifest.json`), which continue to be produced for backwards compatibility.
- **Easier to install** — distributed as a single self-contained binary, with no Python runtime or dependency management required.
- **A completely revamped local documentation experience** — dbt docs is now powered by those new artifacts and capable of scaling to large projects.

### Supported operating systems and architectures

dbt v2.0 and its drivers are compiled per operating system and architecture.

Legend:
* 🟢 — Supported today
* 🟡 — Not yet supported

| Operating system | x86-64 | ARM |
|---|---|---|
| macOS | 🟢 | 🟢 |
| Linux | 🟢 | 🟢 |
| Windows | 🟢 | 🟡 |

## Understanding dbt

Analysts using dbt can transform their data by simply writing select statements, while dbt handles turning these statements into tables and views in a data warehouse.

These select statements, or "models", form a dbt project. Models frequently build on top of one another – dbt makes it easy to [manage relationships](https://docs.getdbt.com/docs/ref) between models, and [visualize these relationships](https://docs.getdbt.com/docs/documentation), as well as assure the quality of your transformations through [testing](https://docs.getdbt.com/docs/testing).

![dbt dag](https://raw.githubusercontent.com/dbt-labs/dbt/6c6649f9129d5d108aa3b0526f634cd8f3a9d1ed/etc/dbt-dag.png)

## Getting started

* [Install dbt](https://docs.getdbt.com/docs/local/install-dbt?version=2)
* Read the [introduction](https://docs.getdbt.com/docs/introduction/) and [viewpoint](https://docs.getdbt.com/docs/about/viewpoint/)
* Explore the [dbt platform](https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features) for an enhanced collaboration experience.


## Join the dbt Community

- Be part of the conversation in the [dbt Community Slack](http://community.getdbt.com/)
- Read more on the [dbt Community Discourse](https://discourse.getdbt.com)

## Reporting bugs and contributing code

- Want to report a bug or request a feature? Let us know and open [an issue](https://github.com/dbt-labs/dbt/issues/new/choose)
- Want to help us build dbt? Check out the [Contributing Guide](https://github.com/dbt-labs/dbt/blob/HEAD/CONTRIBUTING.md)

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://docs.getdbt.com/community/resources/code-of-conduct).

## License

The source code in this repository is licensed under the [Apache License 2.0](LICENSE).

### Core Implementation Code & Architecture
#### File: `crates/dbt-sa-python/python/dbt/__init__.py`
```python

```

#### File: `crates/dbt-sa-python/python/dbt/artifacts/__init__.py`
```python

```

#### File: `crates/dbt-sa-python/python/dbt/artifacts/schemas/__init__.py`
```python

```

#### File: `crates/dbt-sa-python/python/dbt/contracts/__init__.py`
```python

```

#### File: `crates/dbt-sa-python/python/dbt/contracts/graph/__init__.py`
```python

```

#### File: `crates/dbt-sa-python/python/dbt/cli/__init__.py`
```python

```


==================================================


## [2/3] Repository: backtrader (`WHEEL_backtrader`)
- **Full Name**: `backtrader`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
backtrader
==========

.. image:: https://img.shields.io/pypi/v/backtrader.svg
   :alt: PyPi Version
   :scale: 100%
   :target: https://pypi.python.org/pypi/backtrader/

..  .. image:: https://img.shields.io/pypi/dm/backtrader.svg
       :alt: PyPi Monthly Donwloads
       :scale: 100%
       :target: https://pypi.python.org/pypi/backtrader/

.. image:: https://img.shields.io/pypi/l/backtrader.svg
   :alt: License
   :scale: 100%
   :target: https://github.com/backtrader/backtrader/blob/master/LICENSE
.. image:: https://travis-ci.org/backtrader/backtrader.png?branch=master
   :alt: Travis-ci Build Status
   :scale: 100%
   :target: https://travis-ci.org/backtrader/backtrader
.. image:: https://img.shields.io/pypi/pyversions/backtrader.svg
   :alt: Python versions
   :scale: 100%
   :target: https://pypi.python.org/pypi/backtrader/

**Yahoo API Note**:

  [2018-11-16] After some testing it would seem that data downloads can be
  again relied upon over the web interface (or API ``v7``)

**Tickets**

  The ticket system is (was, actually) more often than not abused to ask for
  advice about samples.

For **feedback/questions/...** use the `Community <https://community.backtrader.com>`_

Here a snippet of a Simple Moving Average CrossOver. It can be done in several
different ways. Use the docs (and examples) Luke!
::

  from datetime import datetime
  import backtrader as bt

  class SmaCross(bt.SignalStrategy):
      def __init__(self):
          sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
          crossover = bt.ind.CrossOver(sma1, sma2)
          self.signal_add(bt.SIGNAL_LONG, crossover)

  cerebro = bt.Cerebro()
  cerebro.addstrategy(SmaCross)

  data0 = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime(2011, 1, 1),
                                    todate=datetime(2012, 12, 31))
  cerebro.adddata(data0)

  cerebro.run()
  cerebro.plot()

Including a full featured chart. Give it a try! This is included in the samples
as ``sigsmacross/sigsmacross2.py``. Along it is ``sigsmacross.py`` which can be
parametrized from the command line.

Features:
=========

Live Trading and backtesting platform written in Python.

  - Live Data Feed and Trading with

    - Interactive Brokers (needs ``IbPy`` and benefits greatly from an
      installed ``pytz``)
    - *Visual Chart* (needs a fork of ``comtypes`` until a pull request is
      integrated in the release and benefits from ``pytz``)
    - *Oanda* (needs ``oandapy``) (REST API Only - v20 did not support
      streaming when implemented)

  - Data feeds from csv/files, online sources or from *pandas* and *blaze*
  - Filters for datas, like breaking a daily bar into chunks to simulate
    intraday or working with Renko bricks
  - Multiple data feeds and multiple strategies supported
  - Multiple timeframes at once
  - Integrated Resampling and Replaying
  - Step by Step backtesting or at once (except in the evaluation of the Strategy)
  - Integrated battery of indicators
  - *TA-Lib* indicator support (needs python *ta-lib* / check the docs)
  - Easy development of custom indicators
  - Analyzers (for example: TimeReturn, Sharpe Ratio, SQN) and ``pyfolio``
    integration (**deprecated**)
  - Flexible definition of commission schemes
  - Integrated broker simulation with *Market*, *Close*, *Limit*, *Stop*,
    *StopLimit*, *StopTrail*, *StopTrailLimit*and *OCO* orders, bracket order,
    slippage, volume filling strategies and continuous cash adjustmet for
    future-like instruments
  - Sizers for automated staking
  - Cheat-on-Close and Cheat-on-Open modes
  - Schedulers
  - Trading Calendars
  - Plotting (requires matplotlib)

Documentation
=============

The blog:

  - `Blog <http://www.backtrader.com/blog>`_

Read the full documentation at:

  - `Documentation <http://www.backtrader.com/docu>`_

List of built-in Indicators (122)

  - `Indicators Reference <http://www.backtrader.com/docu/indautoref.html>`_

Python 2/3 Support
==================

  - Python >= ``3.2``

  - It also works with ``pypy`` and ``pypy3`` (no plotting - ``matplotlib`` is
    not supported under *pypy*)

Installation
============

``backtrader`` is self-contained with no external dependencies (except if you
want to plot)

From *pypi*:

  - ``pip install backtrader``

  - ``pip install backtrader[plotting]``

    If ``matplotlib`` is not installed and you wish to do some plotting

.. note:: The minimum matplotlib version is ``1.4.1``

An example for *IB* Data Feeds/Trading:

  - ``IbPy`` doesn't seem to be in PyPi. Do either::

      pip install git+https://github.com/blampe/IbPy.git

    or (if ``git`` is not available in your system)::

      pip install https://github.com/blampe/IbPy/archive/master.zip

For other functionalities like: ``Visual Chart``, ``Oanda``, ``TA-Lib``, check
the dependencies in the documentation.

From source:

  - Place the *backtrader* directory found in the sources inside your project

Version numbering
=================

X.Y.Z.I

  - X: Major version number. Should stay stable unless something big is changed
    like an overhaul to use ``numpy``
  - Y: Minor version number. To be changed upon adding a complete new feature or
    (god forbids) an incompatible API change.
  - Z: Revision version number. To be changed for documentation updates, small
    changes, small bug fixes
  - I: Number of Indicators already built into the platform

### Core Implementation Code & Architecture
#### File: `backtrader/signals/__init__.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
```

#### File: `backtrader/btrun/__init__.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .btrun import btrun
```

#### File: `backtrader/strategies/__init__.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from .sma_crossover import *
```

#### File: `backtrader/studies/__init__.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


from backtrader import Indicator
```

#### File: `tools/bt-run.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader.btrun as btrun


if __name__ == '__main__':
    btrun.btrun()
```

#### File: `backtrader/version.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


__version__ = '1.9.78.123'

__btversion__ = tuple(int(x) for x in __version__.split('.'))
```


==================================================


## [3/3] Repository: backtesting.py (`WHEEL_backtesting.py`)
- **Full Name**: `backtesting.py`
- **Description**: 🔎 📈 🐍 💰  Backtest trading strategies in Python.
- **GitHub Stars**: 8966
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
[![](https://i.imgur.com/E8Kj69Y.png)](https://kernc.github.io/backtesting.py/)

Backtesting.py
==============
[![Build Status](https://img.shields.io/github/actions/workflow/status/kernc/backtesting.py/ci.yml?branch=master&style=for-the-badge)](https://github.com/kernc/backtesting.py/actions)
[![Code Coverage](https://img.shields.io/codecov/c/gh/kernc/backtesting.py.svg?style=for-the-badge&label=Covr)](https://codecov.io/gh/kernc/backtesting.py)
[![Source lines of code](https://img.shields.io/endpoint?url=https%3A%2F%2Fghloc.vercel.app%2Fapi%2Fkernc%2Fbacktesting.py%2Fbadge?filter=.py%26format=human&style=for-the-badge&label=SLOC&color=skyblue)](https://ghloc.vercel.app/kernc/backtesting.py)
[![Backtesting on PyPI](https://img.shields.io/pypi/v/backtesting.svg?color=blue&style=for-the-badge)](https://pypi.org/project/backtesting)
[![PyPI downloads](https://img.shields.io/pypi/dd/backtesting.svg?style=for-the-badge&label=D/L&color=skyblue)](https://pypistats.org/packages/backtesting)
[![Total downloads](https://img.shields.io/pepy/dt/backtesting?style=for-the-badge&label=%E2%88%91&color=skyblue)](https://pypistats.org/packages/backtesting)
[![Stars](https://img.shields.io/github/stars/kernc/backtesting.py?color=silver&style=for-the-badge&label=%e2%ad%90)](https://github.com/kernc/backtesting.py)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/kernc?color=pink&style=for-the-badge&label=%E2%99%A5)](https://github.com/sponsors/kernc)

Backtest trading strategies with Python.

[**Project website**](https://kernc.github.io/backtesting.py) + [Documentation] &nbsp;&nbsp;|&nbsp; [YouTube]

[Documentation]: https://kernc.github.io/backtesting.py/doc/backtesting/
[YouTube]: https://www.youtube.com/results?q=%22backtesting.py%22

Installation
------------

    $ pip install backtesting

Or if you prefer the bleeding edge:

    $ pip install git+https://github.com/kernc/backtesting.py


Usage
-----
```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


bt = Backtest(GOOG, SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
bt.plot()
```

Results in:

```text
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                       94.27
Equity Final [$]                     68935.12
Equity Peak [$]                      68991.22
Return [%]                             589.35
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                       25.42
Volatility (Ann.) [%]                   38.43
CAGR [%]                                16.80
Sharpe Ratio                             0.66
Sortino Ratio                            1.30
Calmar Ratio                             0.77
Alpha [%]                              450.62
Beta                                     0.02
Max. Drawdown [%]                      -33.08
Avg. Drawdown [%]                       -5.58
Max. Drawdown Duration      688 days 00:00:00
Avg. Drawdown Duration       41 days 00:00:00
# Trades                                   93
Win Rate [%]                            53.76
Best Trade [%]                          57.12
Worst Trade [%]                        -16.63
Avg. Trade [%]                           1.96
Max. Trade Duration         121 days 00:00:00
Avg. Trade Duration          32 days 00:00:00
Profit Factor                            2.13
Expectancy [%]                           6.91
SQN                                      1.78
Kelly Criterion                        0.6134
_strategy              SmaCross(n1=10, n2=20)
_equity_curve                          Equ...
_trades                       Size  EntryB...
dtype: object
```
[![plot of trading simulation](https://i.imgur.com/xRFNHfg.png)](https://kernc.github.io/backtesting.py/#example)

Find more usage examples in the [documentation].


Features
--------
* Simple, [well-documented API](https://kernc.github.io/backtesting.py/doc/backtesting/backtesting.html)
* Blazing fast execution
* Built-in [optimizer](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html#Optimization)
  based on [SAMBO](https://sambo-optimization.github.io)
* [Library of composable base strategies](https://kernc.github.io/backtesting.py/doc/examples/Strategies%20Library.html)
  and related utilities
* Indicator-library-agnostic (BYO)
* Supports _any_ financial instrument with OHLC(V) candlestick data
* [Detailed trade results](https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html#Trade-data)
  provided as simple Series/DataFrame objects
* [Interactive visualizations](https://kernc.github.io/backtesting.py/#example)

![xkcd.com/1570](https://imgs.xkcd.com/comics/engineer_syllogism.png)


Bugs
----
Before reporting bugs or posting to the
[discussion board](https://github.com/kernc/backtesting.py/discussions),
please read [contributing guidelines](CONTRIBUTING.md), particularly the section
about crafting useful bug reports and ```` ``` ````-fencing your code.
The maintainers thank you!


Alternatives
------------
See [alternatives.md] for a list of alternative Python
backtesting frameworks and related packages.

[alternatives.md]: https://github.com/kernc/backtesting.py/blob/master/doc/alternatives.md

### Core Implementation Code & Architecture
#### File: `doc/scripts/ipython_config.py`
```python
# In build.sh, this file is copied into (and removed from)
# ~/.ipython/profile_default/startup/

import pandas as pd
pd.set_option("display.max_rows", 30)
# This an alternative to setting display.preceision=2,
# which doesn't work well for our dtype=object Series.
pd.set_option('display.float_format', '{:.2f}'.format)
del pd
```

#### File: `backtesting/test/__main__.py`
```python
import sys
import unittest
import warnings


if __name__ == '__main__':
    warnings.filterwarnings('error')
    # But avoid multiprocessing RuntimeWarning on Widnose
    if sys.platform.startswith('win'):
        warnings.filterwarnings('ignore', message='.*multi-process', category=RuntimeWarning)

    unittest.main(module='backtesting.test._test', verbosity=2)
```

#### File: `pyproject.toml`
```python
[tool.ruff]
exclude = [
    '.git',
    '.eggs',
    '__pycache__',
    'doc/examples',
]
ignore = [
    'UP006',
    'UP007',
    'UP009',
    'N802',
    'N806',
    'C901',
    'B008',
    'B011',
    'RUF002',
]
line-length = 100
select = [
    'I',
    'E',
    'F',
    'W',
    'UP',
    'N',
    'C',
    'B',
    'T',
    'RUF',
    'YTT',
]

[tool.ruff.pep8-naming]
ignore-names = [
    'l',
    'h',
]
```

#### File: `backtesting/test/__init__.py`
```python
"""Data and utilities for testing."""

from __future__ import annotations

import pandas as pd


def _read_file(filename):
    from os.path import dirname, join

    return pd.read_csv(join(dirname(__file__), filename),
                       index_col=0, parse_dates=True)


BTCUSD = _read_file('BTCUSD.csv')
"""DataFrame of monthly BTC/USD histrical index data from 2012 through 2024 (12 years)."""

GOOG = _read_file('GOOG.csv')
"""DataFrame of daily NASDAQ:GOOG (Google/Alphabet) stock price data from 2004 to 2013."""

EURUSD = _read_file('EURUSD.csv')
"""DataFrame of hourly EUR/USD forex data from April 2017 to February 2018."""


def SMA(arr: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return pd.Series(arr).rolling(n).mean()
```

#### File: `doc/scripts/logo.py`
```python
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

output_file("backtesting_logo.html")

source = ColumnDataSource(data=dict(
    colors=[['#00a618', '#d0d000', 'tomato'][i]
            for i in [0, 0, 1, 0, 1, 0, 0, 1, 0, 2]],
    x=list(range(10)),
    bottom=[1, 3, 4, 3, 2, 3, 5, 5, 7, 6.5],
    top=   [4, 7, 6, 5, 4, 6, 8, 7, 9, 8]))   # noqa: E222,E251


p = figure(plot_height=800, plot_width=1200, tools='wheel_zoom,save')
p.vbar('x', .6, 'bottom', 'top', source=source,
       line_color='black', line_width=2,
       fill_color='colors')

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.y_range.start = -2
p.y_range.end = 12
p.x_range.start = -2
p.x_range.end = 11
p.background_fill_color = None
p.border_fill_color = None

show(p)
```

#### File: `setup.py`
```python
import os
import sys

if sys.version_info < (3, 9):
    sys.exit('ERROR: Backtesting.py requires Python 3.9+')


if __name__ == '__main__':
    from setuptools import setup, find_packages

    setup(
        name='backtesting',
        description="Backtest trading strategies in Python",
        license='AGPL-3.0',
        url='https://kernc.github.io/backtesting.py/',
        project_urls={
            'Documentation': 'https://kernc.github.io/backtesting.py/doc/backtesting/',
            'Source': 'https://github.com/kernc/backtesting.py/',
            'Tracker': 'https://github.com/kernc/backtesting.py/issues',
        },
        long_description=open(os.path.join(os.path.dirname(__file__), 'README.md'),
                              encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        include_package_data=True,
        setup_requires=[
            'setuptools_git',
            'setuptools_scm',
        ],
        use_scm_version={
            'write_to': os.path.join('backtesting', '_version.py'),
        },
        install_requires=[
            'numpy >= 1.17.0',
            'pandas >= 0.25.0, != 0.25.0',
            'bokeh >= 3.0.0, != 3.0.*, != 3.2.*',
        ],
        extras_require={
            'doc': [
                'pdoc3',
                'jupytext >= 1.3',
                'nbconvert',
                'ipykernel',       # for nbconvert
                'jupyter_client',  # for nbconvert
            ],
            'test': [
                'matplotlib',
                'scikit-learn',
                'sambo',
                'tqdm',
                'ipywidgets',  # for tqdm
            ],
            'dev': [
                'flake8',
                'coverage',
                'mypy',
            ],
        },
        test_suite="backtesting.test",
        python_requires='>=3.9',
        author='Zach Lûster',
        classifiers=[
            'Intended Audience :: Financial and Insurance Industry',
            'Intended Audience :: Science/Research',
            'Framework :: Jupyter',
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3 :: Only',
            'Topic :: Office/Business :: Financial :: Investment',
            'Topic :: Scientific/Engineering :: Visualization',
        ],
        keywords=[
            'algo',
            'algorithmic',
            'ashi',
            'backtest',
            'backtesting',
            'bitcoin',
            'bokeh',
            'bonds',
            'candle',
            'candlestick',
            'cboe',
            'chart',
            'cme',
            'commodities',
            'crash',
            'crypto',
            'currency',
            'doji',
            'drawdown',
            'equity',
            'etf',
            'ethereum',
            'exchange',
            'finance',
            'financial',
            'forecast',
            'forex',
            'fund',
            'futures',
            'fx',
            'fxpro',
            'gold',
            'heiken',
            'historical',
            'indicator',
            'invest',
            'investing',
            'investment',
            'macd',
            'market',
            'mechanical',
            'money',
            'oanda',
            'ohlc',
            'ohlcv',
            'order',
            'price',
            'profit',
            'quant',
            'quantitative',
            'rsi',
            'silver',
            'simulation',
            'stocks',
            'strategy',
            'ticker',
            'trader',
            'trading',
            'tradingview',
            'usd',
        ],
    )
```


==================================================
