# ⚡ [QUANT-SOURCE-068] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_068_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: empyrical (`WHEEL_empyrical`)
- **Full Name**: `empyrical`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
[![Build Status](https://travis-ci.org/quantopian/empyrical.svg?branch=master)](https://travis-ci.org/quantopian/empyrical)

[![PyPI](https://img.shields.io/pypi/v/empyrical?color=%234ec726&style=flat-square)](https://pypi.org/project/empyrical/)

# empyrical

Common financial risk metrics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)
- [Testing](#testing)

## Installation
```
pip install empyrical
```

## Usage

Simple Statistics
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

Rolling Measures
```python
import numpy as np
from empyrical import roll_max_drawdown

returns = np.array([.01, .02, .03, -.4, -.06, -.02])

# calculate the rolling max drawdown
roll_max_drawdown(returns, window=3)

```

Pandas Support
```python
import pandas as pd
from empyrical import roll_up_capture, capture

returns = pd.Series([.01, .02, .03, -.4, -.06, -.02])

# calculate a capture ratio
capture(returns)

# calculate capture for up markets on a rolling 60 day basis
roll_up_capture(returns, window=60)
```

## Support

Please [open an issue](https://github.com/quantopian/empyrical/issues/new) for support.

### Deprecated: Data Reading via `pandas-datareader`

As of early 2018, Yahoo Finance has suffered major API breaks with no stable
replacement, and the Google Finance API has not been stable since late 2017
[(source)](https://github.com/pydata/pandas-datareader/blob/da18fbd7621d473828d7fa81dfa5e0f9516b6793/README.rst).
In recent months it has become a greater and greater strain on the `empyrical`
development team to maintain support for fetching data through
`pandas-datareader` and other third-party libraries, as these APIs are known to
be unstable.

As a result, all `empyrical` support for data reading functionality has been
deprecated and will be removed in a future version.

Users should beware that the following functions are now deprecated:

- `empyrical.utils.cache_dir`
- `empyrical.utils.data_path`
- `empyrical.utils.ensure_directory`
- `empyrical.utils.get_fama_french`
- `empyrical.utils.load_portfolio_risk_factors`
- `empyrical.utils.default_returns_func`
- `empyrical.utils.get_symbol_returns_from_yahoo`

Users should expect regular failures from the following functions, pending
patches to the Yahoo or Google Finance API:

- `empyrical.utils.default_returns_func`
- `empyrical.utils.get_symbol_returns_from_yahoo`

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/quantopian/empyrical/compare/).

## Testing
- install requirements
  - "nose>=1.3.7",
  - "parameterized>=0.6.1"

```
./runtests.py
```

### Core Implementation Code & Architecture
#### File: `empyrical/tests/__init__.py`
```python

```

#### File: `runtests.py`
```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import warnings


if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=RuntimeWarning)
        loader = unittest.TestLoader()
        tests = loader.discover('.')
        testRunner = unittest.runner.TextTestRunner()
        testRunner.run(tests)
```

#### File: `empyrical/periods.py`
```python
APPROX_BDAYS_PER_MONTH = 21
APPROX_BDAYS_PER_YEAR = 252

MONTHS_PER_YEAR = 12
WEEKS_PER_YEAR = 52
QTRS_PER_YEAR = 4

DAILY = 'daily'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
QUARTERLY = 'quarterly'
YEARLY = 'yearly'

ANNUALIZATION_FACTORS = {
    DAILY: APPROX_BDAYS_PER_YEAR,
    WEEKLY: WEEKS_PER_YEAR,
    MONTHLY: MONTHS_PER_YEAR,
    QUARTERLY: QTRS_PER_YEAR,
    YEARLY: 1
}
```

#### File: `empyrical/deprecate.py`
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
                stacklevel=stacklevel
            )
            return fn(*args, **kwargs)
        return wrapper
    return deprecated_dec
```

#### File: `empyrical/__init__.py`
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

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

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
    value_at_risk,
)

from .periods import (
    DAILY,
    WEEKLY,
    MONTHLY,
    QUARTERLY,
    YEARLY
)


from .perf_attrib import (
    perf_attrib,
    compute_exposures,
)
```

#### File: `setup.py`
```python
#!/usr/bin/env python
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
from setuptools import setup
import versioneer


DISTNAME = "empyrical"
DESCRIPTION = """empyrical is a Python library with performance and risk \
statistics commonly used in quantitative finance"""
LONG_DESCRIPTION = """empyrical is a Python library with performance and risk
statistics commonly used in quantitative finance by `Quantopian Inc`_.

.. _Quantopian Inc: https://www.quantopian.com
.. _Zipline: https://zipline.io
.. _pyfolio: https://quantopian.github.io/pyfolio/
"""
MAINTAINER = "Quantopian Inc"
MAINTAINER_EMAIL = "opensource@quantopian.com"
AUTHOR = "Quantopian Inc"
AUTHOR_EMAIL = "opensource@quantopian.com"
URL = "https://github.com/quantopian/empyrical"
LICENSE = "Apache License, Version 2.0"

classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "License :: OSI Approved :: Apache Software License",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Operating System :: OS Independent"
]


test_reqs = [
    "nose>=1.3.7",
    "parameterized>=0.6.1"
]


requirements = [
    'numpy>=1.9.2',
    'pandas>=0.16.1',
    'scipy>=0.15.1',
    'six',
    "pandas-datareader>=0.2"
]

extras_requirements = {
    "dev": [
        "nose==1.3.7",
        "parameterized==0.6.1",
        "flake8==2.5.1"
    ]
}


if __name__ == "__main__":
    setup(
        name=DISTNAME,
        cmdclass=versioneer.get_cmdclass(),
        version=versioneer.get_version(),
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        long_description=LONG_DESCRIPTION,
        packages=["empyrical", "empyrical.tests"],
        classifiers=classifiers,
        install_requires=requirements,
        extras_require=extras_requirements,
        tests_require=test_reqs,
        test_suite="nose.collector"
    )
```


==================================================


## [2/3] Repository: ffn (`WHEEL_ffn`)
- **Full Name**: `ffn`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# ffn - Financial Functions for Python

![ffn](docs/source/_static/logo.png)

[![Build Status](https://github.com/pmorissette/ffn/workflows/Build%20Status/badge.svg)](https://github.com/pmorissette/ffn/actions/)
[![PyPI Version](https://img.shields.io/pypi/v/ffn)](https://pypi.org/project/ffn/)
[![PyPI License](https://img.shields.io/pypi/l/ffn)](https://pypi.org/project/ffn/)

If you are looking for a full backtesting framework, please check out [bt](https://github.com/pmorissette/bt).
bt is built atop ffn and makes it easy and fast to backtest quantitative strategies.

## Overview

<a id="a-brief-introduction"></a>

ffn is a library that contains many useful functions for those who work in **quantitative
finance**. It stands on the shoulders of giants (Pandas, Numpy, Scipy, etc.) and provides
a vast array of utilities, from performance measurement and evaluation to
graphing and common data transformations.

```python
import ffn
returns = ffn.get('aapl,msft,c,gs,ge', start='2010-01-01').to_returns().dropna()
print(returns.calc_mean_var_weights().as_format('.2%'))
```

Example output:

```text
    aapl    62.54%
    c       -0.00%
    ge      36.19%
    gs      -0.00%
    msft     1.26%
    dtype: object
```

## Installation

The easiest way to install `ffn` is from the [Python Package Index](https://pypi.python.org/pypi/ffn/)
using `pip`.

```bash
pip install ffn
```

Since ffn has many dependencies, we strongly recommend installing the [Anaconda Scientific Python Distribution](https://store.continuum.io/cshop/anaconda/). This distribution comes with many of the required packages pre-installed, including pip. Once Anaconda is installed, the above command should complete the installation.

## Documentation

Read the docs at <https://pmorissette.github.io/ffn/>.

- [Introduction](docs/source/introduction.rst)
- [Installation guide](docs/source/install.rst)
- [Quickstart](docs/source/quick.rst)
- [Full API](docs/source/ffn.rst)

## Contribute

See the [development guide](docs/development.md) for setup, tests, documentation builds, and Copier template updates.

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `ffn/__init__.py`
```python
from . import core, data
from .core import *
from .data import get

core.extend_pandas()

__version__ = "1.2.1"
```

#### File: `docs/build.py`
```python
"""Build documentation with released Yardang and Klink packages."""

from pathlib import Path

import klink
from sphinx.application import Sphinx
from yardang.build import generate_docs_configuration


def main():
    with generate_docs_configuration() as config_dir:
        app = Sphinx(
            srcdir=".",
            confdir=config_dir,
            outdir="docs/html",
            doctreedir="docs/html/.doctrees",
            buildername="html",
            confoverrides={
                # Klink 0.1.10 predates Sphinx theme entry-point registration.
                "html_theme_path": [klink.get_html_theme_path()],
                "html_static_path": [str(Path("docs/source/_static").resolve())],
                "html_favicon": str(Path("docs/source/_static/favicon.ico").resolve()),
                "html_title": "ffn — Financial Functions for Python",
            },
            warningiserror=True,
        )
        app.build()
        return app.statuscode


if __name__ == "__main__":
    raise SystemExit(main())
```

#### File: `tests/test_data.py`
```python
import numpy as np
import pandas as pd
import pytest

import ffn


def sample_provider(ticker, field):
    prices = {"ABC": [np.nan, 10.0, np.nan, 12.0], "DEF": [20.0, np.nan, 22.0, 23.0]}
    return pd.Series(prices[ticker], index=pd.date_range("2024-01-01", periods=4))


@pytest.mark.parametrize("forward_fill", [False, True])
@pytest.mark.parametrize("common_dates", [False, True])
def test_get_forward_fill(forward_fill, common_dates):
    result = ffn.get(
        "ABC,DEF",
        provider=sample_provider,
        common_dates=common_dates,
        forward_fill=forward_fill,
        mrefresh=True,
    )

    if common_dates:
        expected = pd.DataFrame({"abc": [12.0], "def": [23.0]}, index=pd.date_range("2024-01-04", periods=1))
    else:
        expected = pd.DataFrame(
            {"abc": [np.nan, 10.0, 10.0 if forward_fill else np.nan, 12.0], "def": [20.0, 20.0 if forward_fill else np.nan, 22.0, 23.0]},
            index=pd.date_range("2024-01-01", periods=4),
        )
    pd.testing.assert_frame_equal(result, expected, check_freq=False)
```

#### File: `tests/test_asfreq_actual.py`
```python
import pandas as pd
import pytest

import ffn


@pytest.mark.parametrize("freq", ["D", ffn.core._MonthEnd])
@pytest.mark.parametrize("periods", [0, 2, 8])
@pytest.mark.parametrize("timezone", [None, "UTC", "America/New_York"])
@pytest.mark.parametrize("as_frame", [False, True])
def test_asfreq_actual_preserves_regular_frequency(freq, periods, timezone, as_frame):
    index = pd.date_range("2020-01-31", periods=periods, freq=freq, tz=timezone, name="date")
    prices = pd.Series(range(periods), index=index, dtype="Float64", name=0)
    if as_frame:
        prices = pd.concat([prices, prices.rename("dt")], axis=1)
        prices.columns.name = "assets"
    original = prices.copy()
    assert_equal = pd.testing.assert_frame_equal if as_frame else pd.testing.assert_series_equal

    results = [ffn.asfreq_actual(prices, freq), prices.asfreq_actual(freq)]
    if freq == ffn.core._MonthEnd:
        results.append(prices.to_monthly())

    for result in results:
        assert_equal(result, original, check_exact=True)
        if periods == 2:
            assert_equal(result.shift(freq="infer"), original.shift(freq=freq), check_exact=True)
    assert_equal(prices, original, check_exact=True)
```

#### File: `.github/scripts/test-distributions.py`
```python
"""Smoke-test installed distributions outside the source checkout."""

import os
import subprocess
import sys
import venv
from pathlib import Path
from tempfile import TemporaryDirectory


def main():
    dist = Path("dist")
    wheels = sorted(dist.glob("*.whl"))
    sdists = sorted(dist.glob("*.tar.gz"))
    if not wheels or not sdists:
        raise SystemExit("Build both wheel and sdist with make dist first")

    for archive in wheels + sdists:
        with TemporaryDirectory(prefix="ffn-dist-") as directory:
            environment = Path(directory) / "venv"
            venv.EnvBuilder().create(environment)
            python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
            subprocess.run(
                [sys.executable, "-m", "uv", "pip", "install", "--python", str(python), str(archive.resolve())],
                check=True,
                cwd=directory,
            )
            subprocess.run(
                [str(python), "-I", "-c", "import ffn; import pandas as pd; assert pd.Series([100.0, 110.0]).to_returns().iloc[1] > 0"],
                check=True,
                cwd=directory,
            )
        print(f"Passed: {archive}", flush=True)


if __name__ == "__main__":
    main()
```


==================================================


## [3/3] Repository: StockVizGit (`VAULT_IN-QUANT-112_stockviz__StockVizGit`)
- **Full Name**: `IN-QUANT-112_stockviz__StockVizGit`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# StockVizGit
Analyze Indian markets with R

Most DIY quants find it difficult to subscribe to Indian market data, set up a database, jobs to download, etc. If you are a hobbyist programmer, you shouldn't be rquired to go through all this before you even get started.

StockViz will now start making most of our internal data accessible to programmeres through APIs. Here's how it works:

1. Data will remain within the confines of StockViz - there is no "shipping" of data.
2. Programmers do what they do best - write code. We will pull to code onto our servers and run them. The output should be piped to files in the "report" folder.
3. Both code and output will be public.


==================================================
