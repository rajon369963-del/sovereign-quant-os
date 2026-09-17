# ⚡ [QUANT-SOURCE-128] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_128_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: alphalens-reloaded (`WHEEL_alphalens-reloaded`)
- **Full Name**: `alphalens-reloaded`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
<a href="https://alphalens.ml4trading.io">
<img src="https://i.imgur.com/uf8PmQO.png" width="35%">
</a>
</p>

![PyPI](https://img.shields.io/pypi/v/alphalens-reloaded)
[![Anaconda](https://github.com/stefan-jansen/alphalens-reloaded/actions/workflows/conda_package.yml/badge.svg)](https://github.com/stefan-jansen/alphalens-reloaded/actions/workflows/conda_package.yml)
[![Tests](https://github.com/stefan-jansen/alphalens-reloaded/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/stefan-jansen/alphalens-reloaded/actions/workflows/unit_tests.yml)
[![PyPI](https://github.com/stefan-jansen/alphalens-reloaded/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/stefan-jansen/alphalens-reloaded/actions/workflows/build_wheels.yml)
[![Coverage Status](https://coveralls.io/repos/github/stefan-jansen/alphalens-reloaded/badge.svg?branch=main)](https://coveralls.io/github/stefan-jansen/alphalens-reloaded?branch=main)
![GitHub issues](https://img.shields.io/github/issues/stefan-jansen/alphalens-reloaded)
![PyPI - License](https://img.shields.io/pypi/l/alphalens-reloaded)
![Discourse users](https://img.shields.io/discourse/users?server=https%3A%2F%2Fexchange.ml4trading.io%2F)
![Twitter Follow](https://img.shields.io/twitter/follow/ml4trading?style=social)

Alphalens is a Python library for performance analysis of predictive
(alpha) stock factors. Alphalens works great with the
[Zipline](https://www.zipline.ml4trading.io/) open source backtesting library, and [Pyfolio](https://github.com/quantopian/pyfolio) which provides performance and risk analysis of financial portfolios.

The main function of Alphalens is to surface the most relevant statistics and plots about an alpha factor, including:

- Returns Analysis
- Information Coefficient Analysis
- Turnover Analysis
- Grouped Analysis

# Getting started

With a signal and pricing data creating a factor \"tear sheet\" is a two step process:

```python
import alphalens

# Ingest and format data
factor_data = alphalens.utils.get_clean_factor_and_forward_returns(my_factor,
                                                                   pricing,
                                                                   quantiles=5,
                                                                   groupby=ticker_sector,
                                                                   groupby_labels=sector_names)

# Run analysis
alphalens.tears.create_full_tear_sheet(factor_data)
```

# Learn more

Check out the [example notebooks](https://github.com/stefan-jansen/alphalens-reloaded/tree/master/alphalens/examples)
for more on how to read and use the factor tear sheet.

# Installation

Install with pip:

    pip install alphalens-reloaded

Install with conda:

    conda install -c ml4t alphalens-reloaded

Install from the master branch of Alphalens repository (development code):

    pip install git+https://github.com/stefan-jansen/alphalens-reloaded

Alphalens depends on:

- [matplotlib](https://github.com/matplotlib/matplotlib)
- [numpy](https://github.com/numpy/numpy)
- [pandas](https://github.com/pandas-dev/pandas)
- [scipy](https://github.com/scipy/scipy)
- [seaborn](https://github.com/mwaskom/seaborn)
- [statsmodels](https://github.com/statsmodels/statsmodels)

> Note that Numpy>=2.0 requires pandas>=2.2.2. If you are using an older version of pandas, you may need to upgrade
> accordingly, otherwise you may encounter compatibility issues.

# Usage

A good way to get started is to run the examples in a [Jupyter notebook](https://jupyter.org/).

To get set up with an example, you can:

Run a Jupyter notebook server via:

```bash
jupyter notebook
```

From the notebook list page(usually found at `http://localhost:8888/`), navigate over to the examples directory, and open any file with a .ipynb extension.

Execute the code in a notebook cell by clicking on it and hitting Shift+Enter.

# Questions?

If you find a bug, feel free to open an issue on our [github tracker](https://github.com/stefan-jansen/alphalens-reloaded/issues).

# Contribute

If you want to contribute, a great place to start would be the
[help-wanted issues](https://github.com/stefan-jansen/alphalens-reloaded/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).

# Credits

- [Andrew Campbell](https://github.com/a-campbell)
- [James Christopher](https://github.com/jameschristopher)
- [Thomas Wiecki](https://github.com/twiecki)
- [Jonathan Larkin](https://github.com/marketneutral)
- Jessica Stauth (<jstauth@quantopian.com>)
- [Taso Petridis](https://github.com/tasopetridis)

For a full list of contributors see the [contributors page.](https://github.com/stefan-jansen/alphalens-reloaded/graphs/contributors)

# Example Tear Sheets

Example factor courtesy of [ExtractAlpha](https://extractalpha.com/)

## Peformance Metrics Tables

![image](https://i.imgur.com/4T8cziG.png)

## Returns Tear Sheet

![image](https://i.imgur.com/aVs3KiM.png)

## Information Coefficient Tear Sheet

![image](https://i.imgur.com/vAm8okb.png)

## Sector Tear Sheet

![image](https://i.imgur.com/pnBs0ta.png)

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `src/alphalens/__init__.py`
```python
from . import performance
from . import plotting
from . import tears
from . import utils

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")


__all__ = ["performance", "plotting", "tears", "utils"]
```

#### File: `docs/deploy.py`
```python
#!/usr/bin/env python
from __future__ import print_function
from contextlib import contextmanager
from glob import glob
import os
from os.path import basename, exists, isfile
from pathlib import Path
from shutil import move, rmtree
from subprocess import check_call

HERE = Path(__file__).resolve(strict=True).parent
ALPHALENS_ROOT = HERE.parent
TEMP_LOCATION = "/tmp/alphalens-doc"
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

            print("Moving to '%s'" % ALPHALENS_ROOT)
            os.chdir(ALPHALENS_ROOT)

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
    print("Updated documentation branch in directory %s" % ALPHALENS_ROOT)
    print("If you are happy with these changes, commit and push to gh-pages.")


if __name__ == "__main__":
    main()
```

#### File: `docs/source/conf.py`
```python
# -*- coding: utf-8 -*-
import sys
import os
from pathlib import Path
import pydata_sphinx_theme
from alphalens import __version__ as version

sys.path.insert(0, Path("../..").resolve(strict=True).as_posix())

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

project = "Alphalens"
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
    "github_url": "https://github.com/stefan-jansen/alphalens-reloaded",
    "twitter_url": "https://twitter.com/ml4trading",
    "external_links": [
        {"name": "ML for Trading", "url": "https://ml4trading.io"},
        {"name": "Community", "url": "https://exchange.ml4trading.io"},
    ],
    "google_analytics_id": "UA-74956955-3",
    "use_edit_page_button": True,
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "assets/favicon16x16.ico",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "assets/favicon32x32.ico",
        },
    ],
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "stefan-jansen",
    "github_repo": "alphalens-reloaded",
    "github_version": "main",
    "doc_path": "docs/source",
}

html_static_path = []

htmlhelp_basename = "Alphalensdoc"

latex_elements = {}

latex_documents = [
    (
        master_doc,
        "Alphalens.tex",
        "Alphalens Documentation",
        "Quantopian, Inc.",
        "manual",
    )
]

man_pages = [(master_doc, "alphalens", "Alphalens Documentation", [author], 1)]

texinfo_documents = [
    (
        master_doc,
        "Alphalens",
        "Alphalens Documentation",
        author,
        "Alphalens",
        "One line description of project.",
        "Miscellaneous",
    )
]
```

#### File: `pyproject.toml`
```python
[project]
name = "alphalens-reloaded"
description = "Performance analysis of predictive (alpha) stock factors"
requires-python = '>=3.10'
dynamic = ["version"]
readme = "README.md"
authors = [
    { name = 'Quantopian Inc' },
    { email = 'pm@ml4trading.io' }
]
maintainers = [
    { name = 'Stefan Jansen' },
    { email = 'pm@ml4trading.io' }
]
license = { file = "LICENSE" }

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Topic :: Office/Business :: Financial :: Investment',
    'Topic :: Scientific/Engineering :: Information Analysis',
]

dependencies = [
    # following pandas
    "numpy>=1.23.5; python_version<'3.12'",
    "numpy>=1.26.0; python_version>='3.12'",
    "pandas >=1.5.0,<3.0",
    "matplotlib >=1.4.0",
    "scipy >=0.14.0",
    "seaborn >=0.6.0",
    "statsmodels >=0.6.1",
    "IPython >=3.2.3",
    "empyrical-reloaded>=0.5.7"
]

[project.urls]
homepage = 'https://ml4trading.io'
repository = 'https://github.com/stefan-jansen/alphalens-reloaded'
documentation = 'https://alphalens.ml4trading.io'

[build-system]
requires = [
    'setuptools>=54.0.0',
    "setuptools_scm[toml]>=6.2",
]

build-backend = 'setuptools.build_meta'


[project.optional-dependencies]
test = [
    "tox >=2.3.1",
    "coverage >=4.0.3",
    "coveralls ==3.0.1",
    "pytest >=6.2",
    'pytest-xdist >=2.5.0',
    "pytest-cov >=2.12",
    "parameterized >=0.6.1",
    "flake8 >=3.9.1",
    "black",
]
dev = [
    "flake8 >=3.9.1",
    "black",
    "pre-commit >=2.12.1",
]
docs = [
    'Cython',
    'Sphinx >=1.3.2',
    'numpydoc >=0.5.0',
    'sphinx-autobuild >=0.6.0',
    'pydata-sphinx-theme',
    'sphinx-markdown-tables',
    "sphinx_copybutton",
    'm2r2'
]

[tool.setuptools]
include-package-data = true
zip-safe = false

[tool.setuptools.packages.find]
where = ['src']
exclude = ['tests*']

[tool.setuptools_scm]
write_to = "src/alphalens/_version.py"
version_scheme = 'guess-next-dev'
local_scheme = 'dirty-tag'


[tool.pytest.ini_options]
pythonpath = ['src']
minversion = "6.0"
testpaths = 'tests'
addopts = '-v'

[tool.cibuildwheel]
test-extras = "test"
test-command = "pytest -n 2 {package}/tests"
build-verbosity = 3


[tool.cibuildwheel.macos]
archs = ["x86_64", "arm64", "universal2"]
test-skip = ["*universal2:arm64"]


[tool.cibuildwheel.linux]
archs = ["auto64"]
skip = "*musllinux*"


[tool.black]
line-length = 88
target-version = ['py39', 'py310', 'py311', 'py312']
include = '\.pyi?$'
extend-exclude = '''
\(
  docs/source/conf.py
\)
'''


[tool.tox]
legacy_tox_ini = """
[tox]

envlist =
    py310-pandas{15,20,21,22}-numpy1
    py311-pandas{15,20,21,22}-numpy1
    py312-pandas{15,20,21,22}-numpy1
    py310-pandas222-numpy2{0,1,2}
    py311-pandas222-numpy2{0,1,2}
    py312-pandas222-numpy2{0,1,2}

isolated_build = True
skip_missing_interpreters = True
minversion = 3.23.0

[gh-actions]
python =
    3.10: py310
    3.11: py311
    3.12: py312
    3.13: py313

[testenv]
usedevelop = True
setenv =
    MPLBACKEND = Agg

changedir = tmp
extras = test
deps =
    pandas15: pandas>=1.5.0,<1.6
    pandas20: pandas>=2.0,<2.1
    pandas21: pandas>=2.1,<2.2
    pandas22: pandas>=2.2,<2.3
    pandas222: pandas>=2.2.2,<2.3
    numpy1: numpy>=1.23.5,<2.0
    numpy20: numpy>=2.0.0,<2.1.0
    numpy21: numpy>=2.1.0,<2.2.0
    numpy22: numpy>=2.2.0,<2.3.0

commands =
    pytest -n 2 --cov={toxinidir}/src --cov-report term  --cov-report=xml --cov-report=html:htmlcov {toxinidir}/tests
"""
```

#### File: `tests/test_tears.py`
```python
#
# Copyright 2017 Quantopian, Inc.
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

from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from numpy import nan
from pandas import DataFrame, date_range, Timedelta, concat

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

from alphalens.tears import (  # noqa: E402
    create_returns_tear_sheet,
    create_information_tear_sheet,
    create_turnover_tear_sheet,
    create_summary_tear_sheet,
    create_full_tear_sheet,
    create_event_returns_tear_sheet,
    create_event_study_tear_sheet,
)  # noqa: E402

from alphalens.utils import get_clean_factor_and_forward_returns  # noqa: E402


@patch("matplotlib.pyplot.show", Mock())
class TearsTestCase(TestCase):
    tickers = ["A", "B", "C", "D", "E", "F"]

    factor_groups = {"A": 1, "B": 2, "C": 1, "D": 2, "E": 1, "F": 2}

    price_data = [
        [1.25**i, 1.50**i, 1.00**i, 0.50**i, 1.50**i, 1.00**i]
        for i in range(1, 51)
    ]

    factor_data = [
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, 4, 2, 1, nan, nan],
        [3, nan, nan, 1, 4, 2],
        [3, nan, nan, 1, 4, 2],
    ]

    event_data = [
        [1, nan, nan, nan, nan, nan],
        [4, nan, nan, 7, nan, nan],
        [nan, nan, nan, nan, nan, nan],
        [nan, 3, nan, 2, nan, nan],
        [1, nan, nan, nan, nan, nan],
        [nan, nan, 2, nan, nan, nan],
        [nan, nan, nan, 2, nan, nan],
        [nan, nan, nan, 1, nan, nan],
        [2, nan, nan, nan, nan, nan],
        [nan, nan, nan, nan, 5, nan],
        [nan, nan, nan, 2, nan, nan],
        [nan, nan, nan, nan, nan, nan],
        [2, nan, nan, nan, nan, nan],
        [nan, nan, nan, nan, nan, 5],
        [nan, nan, nan, 1, nan, nan],
        [nan, nan, nan, nan, 4, nan],
        [5, nan, nan, 4, nan, nan],
        [nan, nan, nan, 3, nan, nan],
        [nan, nan, nan, 4, nan, nan],
        [nan, nan, 2, nan, nan, nan],
        [5, nan, nan, nan, nan, nan],
        [nan, 1, nan, nan, nan, nan],
        [nan, nan, nan, nan, 4, nan],
        [0, nan, nan, nan, nan, nan],
        [nan, 5, nan, nan, nan, 4],
        [nan, nan, nan, nan, nan, nan],
        [nan, nan, 5, nan, nan, 3],
        [nan, nan, 1, 2, 3, nan],
        [nan, nan, nan, 5, nan, nan],
        [nan, nan, 1, nan, 3, nan],
    ]

    #
    # business days calendar
    #
    bprice_index = date_range(start="2015-1-10", end="2015-3-22", freq="B")
    bprice_index.name = "date"
    bprices = DataFrame(index=bprice_index, columns=tickers, data=price_data)

    bfactor_index = date_range(start="2015-1-15", end="2015-2-25", freq="B")
    bfactor_index.name = "date"
    bfactor = DataFrame(index=bfactor_index, columns=tickers, data=factor_data).stack()

    #
    # full calendar
    #
    price_index = date_range(start="2015-1-10", end="2015-2-28")
    price_index.name = "date"
    prices = DataFrame(index=price_index, columns=tickers, data=price_data)

    factor_index = date_range(start="2015-1-15", end="2015-2-13")
    factor_index.name = "date"
    factor = DataFrame(index=factor_index, columns=tickers, data=factor_data).stack()

    #
    # intraday factor
    #
    today_open = DataFrame(
        index=price_index + Timedelta("9h30m"),
        columns=tickers,
        data=price_data,
    )
    today_open_1h = DataFrame(
        index=price_index + Timedelta("10h30m"),
        columns=tickers,
        data=price_data,
    )
    today_open_1h += today_open_1h * 0.001
    today_open_3h = DataFrame(
        index=price_index + Timedelta("12h30m"),
        columns=tickers,
        data=price_data,
    )
    today_open_3h -= today_open_3h * 0.002
    intraday_prices = concat([today_open, today_open_1h, today_open_3h]).sort_index()

    intraday_factor = DataFrame(
        index=factor_index + Timedelta("9h30m"),
        columns=tickers,
        data=factor_data,
    ).stack()

    #
    # event factor
    #
    bevent_factor = DataFrame(
        index=bfactor_index, columns=tickers, data=event_data
    ).stack()

    event_factor = DataFrame(
        index=factor_index, columns=tickers, data=event_data
    ).stack()

    all_prices = [prices, bprices]
    all_factors = [factor, bfactor]
    all_events = [event_factor, bevent_factor]

    def __localize_prices_and_factor(self, prices, factor, tz):
        if tz is not None:
            factor = factor.unstack()
            factor.index = factor.index.tz_localize(tz)
            factor = factor.stack()
            prices = prices.copy()
            prices.index = prices.index.tz_localize(tz)
        return prices, factor

    @parameterized.expand([(2, (1, 5, 10), None), (3, (2, 4, 6), 20)])
    def test_create_returns_tear_sheet(self, quantiles, periods, filter_zscore):
        """
        Test no exceptions are thrown
        """

        factor_data = get_clean_factor_and_forward_returns(
            self.factor,
            self.prices,
            quantiles=quantiles,
            periods=periods,
            filter_zscore=filter_zscore,
        )

        create_returns_tear_sheet(
            factor_data, long_short=False, group_neutral=False, by_group=False
        )

    @parameterized.expand([(1, (1, 5, 10), None), (4, (1, 2, 3, 7), 20)])
    def test_create_information_tear_sheet(self, quantiles, periods, filter_zscore):
        """
        Test no exceptions are thrown
        """
        factor_data = get_clean_factor_and_forward_returns(
            self.factor,
            self.prices,
            quantiles=quantiles,
            periods=periods,
            filter_zscore=filter_zscore,
        )

        create_information_tear_sheet(factor_data, group_neutral=False, by_group=False)

    @parameterized.expand(
        [
            (2, (2, 3, 6), None, 20),
            (4, (1, 2, 3, 7), None, None),
            (2, (2, 3, 6), ["1D", "2D"], 20),
            (4, (1, 2, 3, 7), ["1D"], None),
        ]
    )
    def test_create_turnover_tear_sheet(
        self, quantiles, periods, turnover_periods, filter_zscore
    ):
        """
        Test no exceptions are thrown
        """
        factor_data = get_clean_factor_and_forward_returns(
            self.factor,
            self.prices,
            quantiles=quantiles,
            periods=periods,
            filter_zscore=filter_zscore,
        )

        create_turnover_tear_sheet(factor_data, turnover_periods)

    @parameterized.expand([(2, (1, 5, 10), None), (3, (1, 2, 3, 7), 20)])
    def test_create_summary_tear_sheet(self, quantiles, periods, filter_zscore):
        """
        Test no exceptions are thrown
        """
        factor_data = get_clean_factor_and_forward_returns(
            self.factor,
            self.prices,
            quantiles=quantiles,
            periods=periods,
            filter_zscore=filter_zscore,
        )

        create_summary_tear_sheet(factor_data, long_short=True, group_neutral=False)
        create_summary_tear_sheet(factor_data, long_short=False, group_neutral=False)

    @parameterized.expand(
        [
            (2, (1, 5, 10), None, None),
            (3, (2, 4, 6), 20, "US/Eastern"),
            (4, (1, 8), 20, None),
            (4, (1, 2, 3, 7), None, "US/Eastern"),
        ]
    )
    def test_create_full_tear_sheet(self, quantiles, periods, filter_zscore, tz):
        """
        Test no exceptions are thrown
        """
        for factor, prices in zip(self.all_factors, self.all_prices):
            prices, factor = self.__localize_prices_and_factor(prices, factor, tz)
            factor_data = get_clean_factor_and_forward_returns(
                factor,
                prices,
                groupby=self.factor_groups,
                quantiles=quantiles,
                periods=periods,
                filter_zscore=filter_zscore,
            )

            create_full_tear_sheet(
                factor_data,
                long_short=False,
                group_neutral=False,
                by_group=False,
            )
            create_full_tear_sheet(
                factor_data,
                long_short=True,
                group_neutral=False,
                by_group=True,
            )
            create_full_tear_sheet(
                factor_data, long_short=True, group_neutral=True, by_group=True
            )

    @parameterized.expand(
        [
            (2, (1, 5, 10), None, None),
            (3, (2, 4, 6), 20, None),
            (4, (3, 4), None, "US/Eastern"),
            (1, (2, 3, 6, 9), 20, "US/Eastern"),
        ]
    )
    def test_create_event_returns_tear_sheet(
        self, quantiles, periods, filter_zscore, tz
    ):
        """
        Test no exceptions are thrown
        """
        for factor, prices in zip(self.all_factors, self.all_prices):
            prices, factor = self.__localize_prices_and_factor(prices, factor, tz)
            factor_data = get_clean_factor_and_forward_returns(
                factor,
                prices,
                groupby=self.factor_groups,
                quantiles=quantiles,
                periods=periods,
                filter_zscore=filter_zscore,
            )

            create_event_returns_tear_sheet(
                factor_data,
                prices,
                avgretplot=(5, 11),
                long_short=False,
                group_neutral=False,
                by_group=False,
            )
            create_event_returns_tear_sheet(
                factor_data,
                prices,
                avgretplot=(5, 11),
                long_short=True,
                group_neutral=False,
                by_group=False,
            )
            create_event_returns_tear_sheet(
                factor_data,
                prices,
                avgretplot=(5, 11),
                long_short=False,
                group_neutral=True,
                by_group=False,
            )
            create_event_returns_tear_sheet(
                factor_data,
                prices,
                avgretplot=(5, 11),
                long_short=False,
                group_neutral=False,
                by_group=True,
            )
            create_event_returns_tear_sheet(
                factor_data,
                prices,
                avgretplot=(5, 11),
                long_short=True,
                group_neutral=False,
                by_group=True,
            )
            create_event_returns_tear_sheet(
                factor_data,
                prices,
                avgretplot=(5, 11),
                long_short=False,
                group_neutral=True,
                by_group=True,
            )

    @parameterized.expand(
        [
            ((6, 8), None, None),
            ((6, 8), None, None),
            ((6, 3), 20, None),
            # ((6, 3), 20, 'US/Eastern'), # TODO: these tests fail
            ((0, 3), None, None),
            # ((3, 0), 20, 'US/Eastern') # TODO: these tests fail
        ]
    )
    def test_create_event_study_tear_sheet(self, avgretplot, filter_zscore, tz):
        """
        Test no exceptions are thrown
        """
        for factor, prices in zip(self.all_events, self.all_prices):
            prices, factor = self.__localize_prices_and_factor(prices, factor, tz)
            factor_data = get_clean_factor_and_forward_returns(
                factor,
                prices,
                bins=1,
                quantiles=None,
                periods=(1, 2),
                filter_zscore=filter_zscore,
            )

            create_event_study_tear_sheet(factor_data, prices, avgretplot=avgretplot)
```


==================================================


## [2/3] Repository: deep-reinforcement-learning-for-finance (`WHEEL_deep-reinforcement-learning-for-finance`)
- **Full Name**: `deep-reinforcement-learning-for-finance`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<div align="center">
<img align="center" src=https://github.com/AI4Finance-Foundation/FinRL/blob/master/figs/FinRL_Tutorials.png>
</div>

**Mission**: creating hundreds of user-friendly demos.

Note that we provide tutorials for [FinRL-meta](https://github.com/AI4Finance-Foundation/FinRL-Meta/tree/master/tutorials) and [FinRL](https://github.com/AI4Finance-Foundation/FinRL/tree/master/tutorials).


## File Structure

### **1-Introduction**		
**notebooks for beginners, introduction step-by-step**

+ **FinRL_StockTrading_NeurIPS_2018:** first tutorial notebook that trades Dow 30 using 5 DRL algorithms.
+ **FinRL_PortfolioAllocation_NeurIPS_2020:** provides basic settings to do portfolio allocation on Dow 30.
+ **FinRL_StockTrading_Fundamental:** merges fundamental indicators in earnings reports such as 'ROA', 'ROE', 'PE' with technical indicators.

### **2-Advance**
**notebooks for intermediate users**

+ **FinRL_PortfolioAllocation_Explainable_DRL:** this notebook uses an empirical approach to explain the strategies of DRL agents for the portfolio management task. 1) it uses feature weights of a trained DRL agent, 2) histogram of correlation coefficient, 3) Z-statistics to explain the strategies.
+ **FinRL_Compare_ElegantRL_RLlib_Stablebaseline3:** compares popular DRL libraries, namely ElegantRL, RLlib and Stablebaseline3.
+ **FinRL_Ensemble_StockTrading_ICAIF_2020:** uses an ensemble strategy to combine multiple DRL agents to form an adaptive one to improve the robustness.

### **3-Practical**
**notebooks for users to explore paper trading and more financial markets**
+ **FinRL_PaperTrading_Demo:** paper trading using FinRL through Alpaca.
+ **FinRL_MultiCrypto_Trading:** trading top 10 market cap cryptocurrencies.
+ **FinRL_China_A_Share_Market:** trading on China A Share market.

### **4-Optimization**
**notebooks for users interested in hyperparameter optimizations**

### **5-Others** 
**other related notebooks**

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `5-Others/FinRL_demo_docker.py`
```python

```

#### File: `DQN-DDPG_Stock_Trading/__init__.py`
```python

```

#### File: `DQN-DDPG_Stock_Trading/gym/wrappers/tests/__init__.py`
```python

```

#### File: `DQN-DDPG_Stock_Trading/gym/wrappers/monitoring/__init__.py`
```python

```

#### File: `DQN-DDPG_Stock_Trading/gym/wrappers/monitoring/tests/__init__.py`
```python

```


==================================================


## [3/3] Repository: ml-trading-screener (`WHEEL_ml-trading-screener`)
- **Full Name**: `ml-trading-screener`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# 🎯 ML Trading Agent - NSE500 Daily Screener

## 🚀 **First Time Setup (One Time Only)**
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Make scripts executable
chmod +x run_dashboard.sh mobile_launcher.sh

# 3. Test the system
python daily_automation.py
```

## 📅 **DAILY WORKFLOW - What to Run Every Day**

### 🌅 **Morning Routine (Before Market Opens - 9:15 AM)**
```bash
# ONE COMMAND DOES EVERYTHING:
python daily_automation.py
```
**This single command:**
- ✅ Fetches fresh NSE500 OHLC data
- ✅ Runs daily screening for all signals
- ✅ Launches interactive dashboard
- ✅ Makes it accessible on your iPhone

### 📱 **iPhone Access Throughout the Day**
```bash
# Start dashboard with mobile access
./mobile_launcher.sh
```
**Then access:** `http://YOUR_MAC_IP:8501` on iPhone Safari

### 🔄 **Optional: Midday/Evening Updates**
```bash
# Just update data (skip screening)
python daily_automation.py --skip-screen

# Just run screening (use existing data)
python daily_automation.py --skip-fetch

# Dashboard only (no data fetch/screening)
python daily_automation.py --dashboard-only

# 🔴 NEW: Update portfolio with real-time prices
python portfolio_realtime_tracker.py
```

### 📊 **Quick Status Check**
```bash
# See what you should do right now
python daily_workflow.py
```

### 🆘 **Emergency Commands**
```bash
# Check if dashboard is running
curl http://localhost:8501

# Find your Mac's IP for iPhone access
ifconfig | grep "inet " | grep -v 127.0.0.1

# Kill any stuck processes
pkill -f streamlit
pkill -f "python daily_automation.py"
```

## ⚡ **Quick Reference**

| **Scenario** | **Command** | **When to Use** |
|-------------|-------------|-----------------|
| 🌅 **Full Morning Setup** | `python daily_automation.py` | Every morning before market opens |
| 📱 **iPhone Access** | `./mobile_launcher.sh` | To access dashboard on phone |
| 🔄 **Data Update Only** | `python daily_automation.py --skip-screen` | Midday data refresh |
| 🎯 **Screening Only** | `python daily_automation.py --skip-fetch` | When data is fresh |
| 📊 **Dashboard Only** | `python daily_automation.py --dashboard-only` | Just view results |
| 🔴 **Live Portfolio** | `python portfolio_realtime_tracker.py` | Real-time returns tracking |
| ❓ **What Should I Do?** | `python daily_workflow.py` | When unsure |

**💡 Pro Tip:** Bookmark `http://YOUR_MAC_IP:8501` on iPhone for instant access!

## 📱 **Mobile Access & Documentation**

- **📱 Mobile Guide:** [`MOBILE_ACCESS_GUIDE.md`](MOBILE_ACCESS_GUIDE.md) - Complete iPhone setup
- **📊 Dashboard Guide:** [`DASHBOARD_README.md`](DASHBOARD_README.md) - Dashboard features
- **🚀 Daily Workflow:** [`daily_workflow.py`](daily_workflow.py) - Smart status checker

---

# 🎯 Trading System Overview

## Option 1: 🚀 **Automated Dashboard** (Recommended)

```bash
# One-command automation (fetches data + screens + launches dashboard)
python daily_automation.py

# Or just launch the dashboard
./run_dashboard.sh
```

**Dashboard Features:**
- 📊 **Auto-fetch NSE500 data** with smart caching
- 🎯 **One-click daily screening** with progress tracking
- 💰 **Portfolio tracking** with exit recommendations
- � **Real-time portfolio updates** with live prices & returns
- �📈 **Interactive analytics** with charts and insights
- 🔄 **Auto-refresh** every 30 minutes (optional)

**Access:** [http://localhost:8501](http://localhost:8501)

## Option 2: 📝 **Manual Command Line**

```bash
# 1. Activate your environment
source .venv/bin/activate

# 2. (Optional) Update OHLC data for all NSE 500 stocks
python equity_screener/utils/fetch_nse500_ohlc.py

# 3. Run the daily screener
python daily_screener/daily_screener.py

# 4. Review output files in daily_screener/ for BUY signals
#   - last_10_buy_signals.csv (your portfolio tracking)
#   - buy_security_ids_today.csv
#   - buy_security_ids_last_7_days.csv
#   - buy_security_ids_last_15_days.csv
#   - buy_security_ids_last_30_days.csv
#   - stale_buy_signals.csv
```

## 📋 How to Add a New Company for Screening

To manually add a new company for daily OHLC fetching and screening:

1. Open `equity_screener/utils/nse500_with_id.csv` in Excel or a text editor.
2. Add a new row with the required details for the company:
   - `Symbol` (e.g., ABFRL)
   - `Series` (usually `EQ`)
   - `Security_ID` (from Dhan master contract)
   - Other columns as in the existing rows (e.g., Company Name, ISIN, etc.)
3. Save the file.

Your fetch and screening scripts will now automatically include this company in all future runs.

> **Note:**
> You do NOT need to run the indicator, labeling, or model training scripts every day.
> - Run them only when you want to retrain or update your ML model (e.g., after several weeks or months, or after a major market change).
> - For daily use, just fetch new OHLC data and run the daily screener as shown above.

---

## 🧩 How the Daily Screener Works

The `daily_screener.py` script processes your latest OHLC data and generates actionable signals. Here's what it does:

1. **Loads existing OHLC data** from `daily_screener/latest_ohlc.csv` (no fetching from the internet).
2. **Adds technical indicators** (RSI, MACD, SMA, etc.) to the data.
3. **Loads your trained ML model** and predicts BUY/SELL signals for each stock-date row.
4. **Exports all signals** to `daily_signals.csv` and prints top BUY/SELL examples.
5. **Shortlists BUY stocks** for the last 7 trading days and saves to `buy_shortlist.csv`.
6. **Identifies stale BUY signals** (older than 7 days) and saves to `stale_buy_signals.csv`.
7. **Counts BUY signals in the last 30 days** for each stock and updates the stale list.
8. **Exports BUY signals** for today, last 7, 15, and 30 days (with Security_ID, Symbol, date, and company name) to separate CSVs.
9. **Prints debug info** about signal counts and unique symbols for transparency.

> **Important:** The script only processes what is already in `latest_ohlc.csv`. To keep your signals up to date, always run your OHLC fetch script before running the daily screener.

---

# ML-Based Equity Screener & Trade Signal Generator using Dhan API

A modular Python-based trading assistant that:
- Scans all NSE equities
- Applies technical indicators
- Uses a trained ML model to predict trade signals
- Exports filtered opportunities
- Offers a separate pipeline for manual stock testing (e.g., Reliance)

---

## 📌 Features

- 🔎 Scans **all NSE stocks** using Dhan API
- 📊 Applies technical indicators (SMA, MACD, RSI, etc.)
- 🧠 Predicts signals using **trained Random Forest model**
- 🧪 Separate module for manual stock backtesting
- ☁️ Ready for automation via cloud (AWS Lambda, Streamlit)
- 🔐 Credentials handled securely via `.env`

---

## 📁 Project Structure

```
ml_trading_agent/
│
├── 🎯 DASHBOARD & AUTOMATION
│   ├── streamlit_daily_dashboard.py     ← main dashboard app
│   ├── daily_automation.py             ← complete automation script
│   ├── run_dashboard.sh                ← dashboard launcher
│   ├── requirements_dashboard.txt      ← dashboard dependencies
│   └── DASHBOARD_README.md             ← detailed dashboard docs
│
├── daily_screener/                     ← ✅ Main daily screening outputs
│   ├── daily_screener.py               ← main daily screener script
│   ├── latest_ohlc_indicators.csv      ← OHLC + indicators
│   ├── daily_signals.csv               ← all signals (BUY/SELL)
│   ├── last_10_buy_signals.csv         ← 💰 YOUR PORTFOLIO TRACKING
│   ├── last_10_hold_signals.csv        ← latest HOLD opportunities
│   ├── last_10_sell_signals.csv        ← latest SELL signals
│   ├── buy_security_ids_today.csv      ← BUY signals for today
│   ├── buy_security_ids_last_7_days.csv
│   ├── buy_security_ids_last_15_days.csv
│   ├── buy_security_ids_last_30_days.csv
│   ├── buy_shortlist.csv               ← BUY shortlist (last 7 days)
│   ├── stale_buy_signals.csv           ← stocks with stale BUY signals
│   ├── returns_summary.csv             ← 📈 PERFORMANCE ANALYTICS
│   └── unified_signals_summary.csv     ← overall signal statistics
│
├── equity_screener/                 ← Bulk screener for NSE 500
│   ├── utils/
│   │   ├── fetch_nse500_ohlc.py
│   │   ├── add_nse500_indicators.py
│   │   ├── label_nse500_signals.py
│   │   ├── train_nse500_model.py
│   │   ├── nse500_with_id.csv       ← master NSE 500 list
│   │   └── ...
│   └── ...
│
├── manual_stock_analysis/           ← Manual/single stock pipeline
│   └── ...
│
├── models/
│   └── dhan_rf_model.joblib
│
├── pipeline_config.yaml             ← central config for all scripts
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

- Python 3.13+
- DhanHQ API (live/historical data)
- Scikit-learn (ML model)
- Pandas, NumPy, Joblib
- dotenv (for secure credentials)

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repo
https://github.com/holda440/ml-trading-screener.git

# 2. Create environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Dhan credentials in a .env file
```

---

## 🔐 .env File Format

```
CLIENT_ID=your_dhan_client_id
ACCESS_TOKEN=your_access_token
```

**⚠️ This file is ignored using `.gitignore` and should NEVER be pushed to GitHub.**

---

## 👨‍⚕️ Author

**Dr. Varis Ali**  
Dentist | Quant Learner | AI Enthusiast  
GitHub: [@holda440](https://github.com/holda440)  
Website: [https://finiva.in](https://finiva.in)  
Email: holda_440@hotmail.com  
Mobile: +91 9428832429

---

Feel free to fork, contribute, or reach out with questions!

### Core Implementation Code & Architecture
#### File: `daily_screener_streamlit.py`
```python

```

#### File: `streamlit_demo.py`
```python

```

#### File: `equity_screener/__init__.py`
```python

```

#### File: `equity_screener/utils/__init__.py`
```python

```

#### File: `position_manager/__init__.py`
```python
# Position Manager Module
# Handles portfolio tracking, exit strategies, and backtesting
```

#### File: `.streamlit/config.toml`
```python
[general]
email = "holda_440@hotmail.com"

[server]
headless = true
enableCORS = false
port = 8501

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```


==================================================
