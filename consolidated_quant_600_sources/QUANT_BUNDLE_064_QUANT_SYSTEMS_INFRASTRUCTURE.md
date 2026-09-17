# ⚡ [QUANT-SOURCE-064] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_064_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: jugaad-data (`WHEEL_jugaad-data`)
- **Full Name**: `jugaad-data`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Documentation

https://marketsetup.in/documentation/jugaad-data/

# Introduction

`jugaad-data` is a python library to download historical/live stock, index as well as economic data from NSE and RBI website using.

![Build Badge](https://github.com/jugaad-py/jugaad-data/actions/workflows/run-tests.yml/badge.svg)


# Features

* Supports [new NSE website](https://www.nseindia.com/), (All libraries based on old NSE website might stop working)
* Powerful CLI (Command line interface), Even non-coders can use it easily
* Built-in caching mechanism to play nice with NSE. Avoid making un-necessary requests to NSE's website and getting blocked
* Optional `pandas` support 

**Road map**

| Website  | Segment    | Supported? |
|----------|------------|------------|
| NSE      | Stocks     | Yes        |
| NSE      | Stocks F&O | Yes        |
| NSE      | Index      | Yes    |
| NSE      | Index F&O  | Yes        |
| RBI	   | Current Rates| Yes |

# Installation

`pip install jugaad-data` 

# Getting started

## Python inteface

### Historical data

```python
from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save

# Download bhavcopy
bhavcopy_save(date(2020,1,1), "/path/to/directory")

# Download bhavcopy for futures and options
bhavcopy_fo_save(date(2020,1,1), "/path/to/directory")

# Download stock data to pandas dataframe
from jugaad_data.nse import stock_df
df = stock_df(symbol="SBIN", from_date=date(2020,1,1),
            to_date=date(2020,1,30), series="EQ")
```
### Live data

```python
from jugaad_data.nse import NSELive
n = NSELive()
q = n.stock_quote("HDFC")
print(q['priceInfo'])
```

```
{'lastPrice': 2635,
 'change': -49.05000000000018,
 'pChange': -1.8274622305843848,
 'previousClose': 2684.05,
 'open': 2661,
 'close': 2632.75,
 'vwap': 2645.57,
 'lowerCP': '2415.65',
 'upperCP': '2952.45',
 'pPriceBand': 'No Band',
 'basePrice': 2684.05,
 'intraDayHighLow': {'min': 2615.6, 'max': 2688.45, 'value': 2635},
 'weekHighLow': {'min': 1473.45,
  'minDate': '24-Mar-2020',
  'max': 2777.15,
  'maxDate': '13-Jan-2021',
  'value': 2635}}
```

## Command line interface

```
$ jdata stock --help

Usage: jdata stock [OPTIONS]

  Download historical stock data

  $jdata stock --symbol STOCK1 -f yyyy-mm-dd -t yyyy-mm-dd --o file_name.csv

Options:
  -s, --symbol TEXT  [required]
  -f, --from TEXT    [required]
  -t, --to TEXT      [required]
  -S, --series TEXT  [default: EQ]
  -o, --output TEXT
  --help             Show this message and exit.
```

```
$ jdata stock -s SBIN -f 2020-01-01 -t 2020-01-31 -o SBIN-Jan.csv
SBIN  [####################################]  100%

Saved file to : SBIN-Jan.csv
```

## Download historical index data (niftyindices.com)

```python
from datetime import date
from jugaad_data.nse import (index_raw, index_pe_raw, index_tri_raw,
                              index_type_list, index_subtype_list, index_name_list)

# OHLC data for an index
data = index_raw("NIFTY 50", date(2026, 1, 1), date(2026, 7, 31))

# P/E, P/B and Dividend Yield
pe_data = index_pe_raw("NIFTY 50", date(2026, 1, 1), date(2026, 7, 31))

# Total Return Index values
# For standard indices name == index_name; for strategy indices use the short code as name
tri_data = index_tri_raw("NIFTY 50", "NIFTY 50", date(2026, 1, 1), date(2026, 7, 31))

# Discover available indices (3-level hierarchy)
index_type_list()                                              # ['Equity', 'Fixed Income', 'Multi Asset']
index_subtype_list('Equity', 'Historical Index Data')          # ['Broad Market Indices', 'Sectoral Indices', ...]
index_name_list('Broad Market Indices', 'Historical Index Data')  # ['NIFTY 50', 'NIFTY 100', ...]

# index_group options:
#   'Historical Index Data'
#   'Total returns Index Values '
#   'P/E, P/B & Div.Yield values'
```

## Download historical derivatives (F&O) data

```
$ jdata deriviatives --help
Usage: cli.py derivatives [OPTIONS]

  Sample usage-

  Download stock futures-

  jdata derivatives -s SBIN -f 2020-01-01 -t 2020-01-30 -e 2020-01-30 -i FUTSTK -o file_name.csv

  Download index futures-

  jdata derivatives -s NIFTY -f 2020-01-01 -t 2020-01-30 -e 2020-01-30 -i FUTIDX -o file_name.csv

  Download stock options-

  jdata derivatives -s SBIN -f 2020-01-01 -t 2020-01-30 -e 2020-01-30 -i OPTSTK -p 330 --ce -o file_name.csv

  Download index options-

  jdata derivatives -s NIFTY -f 2020-01-01 -t 2020-01-30 -e 2020-01-23 -i OPTIDX -p 11000 --pe -o file_name.csv

Options:
  -s, --symbol TEXT  Stock/Index symbol  [required]
  -f, --from TEXT    From date - yyyy-mm-dd  [required]
  -t, --to TEXT      To date - yyyy-mm-dd  [required]
  -e, --expiry TEXT  Expiry date - yyyy-mm-dd  [required]
  -i, --instru TEXT  FUTSTK - Stock futures, FUTIDX - Index Futures, OPTSTK -
                     Stock Options, OPTIDX - Index Options  [required]

  -p, --price TEXT   Strike price (Only for OPTSTK and OPTIDX)
  --ce / --pe        --ce for call and --pe for put (Only for OPTSTK and
                     OPTIDX)

  -o, --output TEXT  Full path of output file
  --help             Show this message and exit.
```

## Buy me a coffee

If my work has helped you in anyway, you can buy me a coffee 

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/Jugaader)

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `jugaad_data/__init__.py`
```python
__version__ = "0.35.5"
```

#### File: `jugaad_data/bse/__init__.py`
```python
from .live import BSELive

__all__ = ['BSELive']
```

#### File: `jugaad_data/nse/__init__.py`
```python
from .history import *
from .archives import *
from .live import *
```

#### File: `tests/test_rbi.py`
```python
from jugaad_data.rbi import RBI
import pytest

def test_current_rates():
    r = RBI()
    rates = r.current_rates()
    assert '91 day T-bills' in rates
    assert 'Policy Repo Rate' in rates
    assert 'Savings Deposit Rate' in rates
    # Below should not raise exception
    val = float(rates['91 day T-bills'].replace('%',""))
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["setuptools >= 61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "jugaad-data"
version = "0.35.5"
requires-python = ">= 3.9"
authors = [{name = "jugaad-coder", email = "abc@xyz.com"}]
description = "Free Zerodha API python library"
readme = "README.md"
license = {text = "YOLO"}
keywords = ["NSE", "Live", "Bhavcopy", "History", "Futures", "Options", "Stock Data"]
dynamic = ["dependencies"]


[project.scripts]
jdata = "jugaad_data.cli:cli"

[project.urls]
Homepage = "https://marketsetup.in/documentation/jugaad-data/"
Documentation = "https://marketsetup.in/documentation/jugaad-data/"
Repository = "https://github.com/jugaad-py/jugaad-data"
Issues = "https://github.com/jugaad-py/jugaad-data/issues"

[tool.setuptools.dynamic]
dependencies = {file = ["requirements.txt"]}
```


==================================================


## [2/3] Repository: mftool (`VAULT_IN-QUANT-050_NayakwadiS__mftool`)
- **Full Name**: `IN-QUANT-050_NayakwadiS__mftool`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<img src="/docs/mftool.png"  height="150">

Python library for getting Mutual Funds data in India

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
[![Pypi](https://img.shields.io/badge/pypi-v3.3-green)](https://pypi.python.org/pypi/mftool)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![License](https://img.shields.io/pypi/l/selenium-wire.svg)
[![Documentation](https://img.shields.io/badge/Documantation-latest-brightgreen)](https://mftool.readthedocs.io/en/latest/)
[![Downloads](https://pepy.tech/badge/mftool/month)](https://pepy.tech/project/mftool)


Introduction
============
mftool is a library for getting publically available Mutual Funds data in India. It can be used in various types of projects which requires getting live quotes for a given mutual fund scheme or build large data sets for further data analytics.

Features
=============

* Getting last updated quotes for Mutual fund scheme using scheme codes.
* Return data in Dataframe, json and dictionary formats.
* Getting quotes for all the schemes available with AMFI.
* Helper APIs to check whether a given Scheme code is correct.
* Getting all historical NAVs for a schemes.
* Getting list of all schemes with there Scheme codes.
* Get daily scheme performance.
* Support GenAI with mftool-mcp

<!---*[**Documentation**](https://61836947349d9.site123.me/)*--->


Related Projects -

1. Forecasting Indian Stocks *[NSE-Neuron](https://github.com/NayakwadiS/NSE-Neuron)*
2. Forecasting of Mutual Funds *[here](https://github.com/NayakwadiS/Forecasting_Mutual_Funds)*
3. Predict Cryptocurrency in Indian Rupees *[here](https://github.com/NayakwadiS/Predict_Cryptocurrency_INR)*
4. MCP server for GenAI apps *[mftool-mcp](https://github.com/NayakwadiS/mftool-mcp)*

<a href="https://www.buymeacoffee.com/nayakwadis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="29" width="174">
</a>

### Core Implementation Code & Architecture
#### File: `docs/conf.py`
```python
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

# -- Project information -----------------------------------------------------

project = 'mftool'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '3.3'

# The master toctree document.
master_doc = 'index'

html_favicon = 'mftool.png'

html_static_path = ['_static']

def setup(app):
    app.add_css_file('css/custom.css?v20260519')
```

#### File: `setup.py`
```python
from setuptools import setup, Extension, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mftool",
    version="3.3",
    author="SujitN",
    author_email="nayakwadi_sujit@rediffmail.com",
    description="Library for getting real time Mutual funds info",
    license="MIT",
    keywords="amfi, quote, mutual-funds, funds, bse, nse, market, stock, stocks",
    install_requires=['requests', 'bs4', 'httpx', 'pandas', 'yfinance', 'matplotlib','deprecated'],
    url="https://github.com/NayakwadiS/mftool",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={'': ['*.json']}
)
```

#### File: `__init__.py`
```python
"""
    The MIT License (MIT)

    Copyright (c) 2025 Sujit Nayakwadi

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
__VERSION__='3.3'
from .mftool import Mftool
```

#### File: `utils.py`
```python
import json
import os
import json
import pandas as pd
from datetime import date, timedelta


def is_holiday():
    if date.today().strftime("%a") in ['Sat', 'Sun', 'Mon']:
        return True
    else:
        return False


def get_friday():
    days = {'Sat': 1, 'Sun': 2, 'Mon': 3}
    diff = int(days[date.today().strftime("%a")])
    return (date.today() - timedelta(days=diff)).strftime("%d-%b-%Y")


def get_today():
    return (date.today() - timedelta(days=1)).strftime("%d-%b-%Y")


def get_52_week_friday():
    return (date.today() - timedelta(weeks=52)).strftime("%d-%m-%Y")


def get_52_week_high_low(data):
    friday = pd.to_datetime(get_52_week_friday(), dayfirst=True)
    df = pd.DataFrame.from_records(data)
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df_high = df[df['date'] >= friday].sort_values(by='nav', ascending=False).head(1)
    df_low = df[df['date'] >= friday].sort_values(by='nav', ascending=True).head(1)
    return {"52_week_high": df_high['nav'].values[0], "52_week_low": df_low['nav'].values[0]}


def render_response(data, as_json=False, as_Dataframe=False):
    if as_json is True:
        return json.dumps(data)
    # parameter 'as_Dataframe' only works with get_scheme_historical_nav()
    elif as_Dataframe is True:
        df = pd.DataFrame.from_records(data['data'])
        df['dayChange'] = df['nav'].astype(float).diff(periods=-1)
        df = df.set_index('date')
        return df
    else:
        return data


class Utilities:

    def __init__(self):
        self._filepath = str(os.path.dirname(os.path.abspath(__file__))) + '/const.json'
        with open(self._filepath, 'r') as f:
            self.values = json.load(f)
```

#### File: `tests/mftool_tests.py`
```python
"""
    This is a test module for testing
"""
import unittest
import logging
import json
import six
from mftool import Mftool
from utils import is_holiday, get_friday, get_today

log = logging.getLogger('mftool')
logging.basicConfig(level=logging.DEBUG)


class TestAPIs(unittest.TestCase):
    def setUp(self):
        self.mftool = Mftool()

    def test_get_scheme_codes(self):
        sc = self.mftool.get_scheme_codes()
        self.assertIsNotNone(sc)
        self.assertIsInstance(sc, dict)
        # test the json format return
        sc_json = self.mftool.get_scheme_codes(as_json=True)
        self.assertIsInstance(sc_json, str)
        # reconstruct the dict from json and compare
        six.assertCountEqual(self, sc, json.loads(sc_json))
        result = self.mftool.get_available_schemes('ICICI')
        self.assertNotIn(result[next(iter(result))], "Axis")

    def test_is_valid_code(self):
        code = '119598'
        self.assertTrue(self.mftool.is_valid_code(code))

    def test_negative_is_valid_code(self):
        wrong_code = '1195'
        self.assertFalse(self.mftool.is_valid_code(wrong_code))

    def test_get_scheme_quote(self):
        code = '101305'
        self.assertIsInstance(self.mftool.get_scheme_quote(code), dict)
        # with json respomftool
        self.assertIsInstance(self.mftool.get_scheme_quote(code, as_json=True), str)
        # with wrong code
        code = 'wrong code'
        self.assertIsNone(self.mftool.get_scheme_quote(code))
        # with code in 'int' format
        code = 101305
        self.assertIsInstance(self.mftool.get_scheme_quote(code), dict)
        # verify data present
        result = self.mftool.get_scheme_quote(code)
        self.assertIsNotNone(result)

    def test_get_scheme_historical_nav(self):
        code = '101305'
        self.assertIsInstance(self.mftool.get_scheme_historical_nav(code), dict)
        # with json respomftool
        self.assertIsInstance(self.mftool.get_scheme_historical_nav(code, as_json=True), str)
        # with wrong code
        code = 'wrong code'
        self.assertIsNone(self.mftool.get_scheme_historical_nav(code))
        # with code in 'int' format
        code = 101305
        self.assertIsInstance(self.mftool.get_scheme_historical_nav(code), dict)
        # verify data present
        result = self.mftool.get_scheme_historical_nav(code)
        self.assertIsNotNone(result)

    def test_get_scheme_details(self):
        code = '101305'
        self.assertIsInstance(self.mftool.get_scheme_details(code), dict)
        # with json respomftool
        self.assertIsInstance(self.mftool.get_scheme_details(code, as_json=True), str)
        # with wrong code
        code = 'wrong code'
        self.assertIsNone(self.mftool.get_scheme_details(code))
        # with code in 'int' format
        code = 101305
        self.assertIsInstance(self.mftool.get_scheme_details(code), dict)
        # verify data present
        result = self.mftool.get_scheme_details(code)
        self.assertIsNotNone(result)

    def test_calculate_balance_units_value(self):
        code = '101305'
        result = self.mftool.calculate_balance_units_value(code, 221)
        self.assertIsNotNone(result)

    def test_get_scheme_historical_nav_year(self):
        code = '101305'
        self.assertIsInstance(self.mftool.get_scheme_historical_nav_year(code, 2018), dict)
        # with json respomftool
        self.assertIsInstance(self.mftool.get_scheme_historical_nav_year(code, 2018, as_json=True), str)
        # with wrong code
        code = 'wrong code'
        self.assertIsNone(self.mftool.get_scheme_historical_nav_year(code, 2018))
        # with code in 'int' format
        code = 101305
        self.assertIsInstance(self.mftool.get_scheme_historical_nav_year(code, 2018), dict)
        # verify data present
        result = self.mftool.get_scheme_historical_nav_year(code, 2018)
        self.assertIsNotNone(result)

    def test_get_day(self):
        if is_holiday():
            self.assertTrue(get_friday())
        else:
            self.assertTrue(get_today())

    def test_get_scheme_historical_nav_for_dates(self):
        code = '101305'
        self.assertIsInstance(self.mftool.get_scheme_historical_nav_for_dates(code,'1-1-2018','31-12-2018'), dict)
        # with json respomftool
        self.assertIsInstance(self.mftool.get_scheme_historical_nav_for_dates(code,'1-1-2018','31-12-2018', as_json=True), str)
        # with wrong code
        code = 'wrong code'
        self.assertIsNone(self.mftool.get_scheme_historical_nav_for_dates(code,'1-1-2018','31-12-2018'))
        # with code in 'int' format
        code = 101305
        self.assertIsInstance(self.mftool.get_scheme_historical_nav_for_dates(code,'1-1-2018','31-12-2018'), dict)
        # verify data present
        result = self.mftool.get_scheme_historical_nav_for_dates(code,'1-1-2018','31-12-2018')
        self.assertIsNotNone(result)

    def test_get_open_ended_equity_scheme_performance(self):
        self.assertIsInstance(self.mftool.get_open_ended_equity_scheme_performance(False), dict)
        # verify data present
        result = self.mftool.get_open_ended_equity_scheme_performance(False)
        self.assertNotEqual(result,{'Large Cap': [],'Large & Mid Cap': [],'Multi Cap': [],'Mid Cap': [],
                                    'Small Cap': [],'Value': [],'ELSS': [],'Contra': [],'Dividend Yield': [],
                                    'Focused': []})

# ToDO : Add remaining test

if __name__ == '__main__':
    unittest.main()
```

#### File: `tests/test_bulk_quotes.py`
```python
"""
Test script demonstrating bulk/batch quote fetching performance
Shows the massive speed improvements with concurrent fetching
"""
import time
from mftool import Mftool


def test_bulk_quotes():
    """Demonstrate bulk quote fetching performance"""

    print("=" * 70)
    print("BULK QUOTE FETCHING DEMONSTRATION")
    print("=" * 70)

    mf = Mftool()

    # Portfolio of 20 schemes
    portfolio_codes = [
        '119597', '119062', '119061', '119060', '119551',
        '119552', '119553', '119554', '119555', '119556',
        '120503', '120504', '120505', '120506', '120507',
        '118989', '118990', '118991', '118992', '118993'
    ]

    print(f"\nTesting with {len(portfolio_codes)} schemes")
    print("=" * 70)

    # Test 1: Sequential fetching (old way)
    print("\n[Test 1] Sequential Fetching (one by one)")
    print("-" * 70)
    mf.clear_cache()  # Start fresh

    start = time.time()
    sequential_results = {}
    for code in portfolio_codes:
        quote = mf.get_scheme_quote(code)
        if quote:
            sequential_results[code] = quote
    sequential_time = time.time() - start

    print(f"✓ Fetched {len(sequential_results)} quotes sequentially")
    print(f"  Time taken: {sequential_time:.2f} seconds")
    print(f"  Average per quote: {sequential_time/len(portfolio_codes):.2f}s")

    # Test 2: Bulk fetching (new way)
    print("\n[Test 2] Bulk Fetching (concurrent)")
    print("-" * 70)
    mf.clear_cache()  # Start fresh

    start = time.time()
    bulk_results = mf.get_bulk_quotes(portfolio_codes, show_progress=True)
    bulk_time = time.time() - start

    print(f"\n✓ Fetched {len(bulk_results)} quotes with bulk method")
    print(f"  Time taken: {bulk_time:.2f} seconds")
    print(f"  Average per quote: {bulk_time/len(portfolio_codes):.2f}s")

    # Show performance comparison
    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    speedup = sequential_time / bulk_time if bulk_time > 0 else float('inf')
    improvement = ((sequential_time - bulk_time) / sequential_time) * 100

    print(f"Sequential time:  {sequential_time:.2f}s")
    print(f"Bulk time:        {bulk_time:.2f}s")
    print(f"Time saved:       {sequential_time - bulk_time:.2f}s")
    print(f"Speedup:          {speedup:.1f}x faster")
    print(f"Improvement:      {improvement:.1f}%")

    # Test 3: Show sample data
    print("\n[Test 3] Sample Quotes")
    print("-" * 70)
    sample_codes = list(bulk_results.keys())[:3]
    for code in sample_codes:
        quote = bulk_results[code]
        if quote:
            print(f"{code}: {quote.get('scheme_name', 'N/A')[:50]}")
            print(f"  NAV: {quote.get('nav', 'N/A')}, Updated: {quote.get('last_updated', 'N/A')}")


def test_portfolio_calculation():
    """Demonstrate portfolio value calculation"""

    print("\n\n" + "=" * 70)
    print("PORTFOLIO VALUE CALCULATION")
    print("=" * 70)

    mf = Mftool()

    # Example portfolio
    holdings = [
        {'scheme_code': '119597', 'units': 100.5},
        {'scheme_code': '119062', 'units': 250.75},
        {'scheme_code': '119061', 'units': 50.25},
        {'scheme_code': '119060', 'units': 175.0},
        {'scheme_code': '119551', 'units': 300.0},
    ]

    print(f"\nCalculating value for portfolio of {len(holdings)} schemes...")
    print("-" * 70)

    start = time.time()
    portfolio = mf.calculate_portfolio_value(holdings)
    calc_time = time.time() - start

    print(f"\n✓ Portfolio calculated in {calc_time:.2f} seconds")
    print("\nPortfolio Summary:")
    print(f"  Total Schemes: {portfolio['total_schemes']}")
    print(f"  Total Value:   ₹{portfolio['total_value']:,.2f}")
    print(f"  Currency:      {portfolio['currency']}")

    print("\nHoldings Breakdown:")
    print("-" * 70)
    for holding in portfolio['holdings'][:5]:  # Show first 5
        print(f"\n{holding['scheme_code']}: {holding['scheme_name'][:45]}")
        print(f"  Units: {holding['units']:.2f}")
        print(f"  NAV:   ₹{holding['nav']}")
        print(f"  Value: ₹{holding['current_value']:,.2f}")

def test_with_caching():
    """Demonstrate how caching improves bulk fetching even more"""

    print("\n\n" + "=" * 70)
    print("BULK FETCHING WITH CACHING")
    print("=" * 70)

    mf = Mftool()
    codes = ['119597', '119062', '119061', '119060', '119551'] * 4  # 20 codes

    print(f"\nFetching {len(codes)} quotes (with duplicates)...")

    # First run - no cache
    print("\n[Run 1] No cache")
    mf.clear_cache()
    start = time.time()
    quotes1 = mf.get_bulk_quotes(codes, show_progress=True)
    time1 = time.time() - start
    print(f"Time: {time1:.2f}s")

    # Second run - with cache
    print("\n[Run 2] With cache")
    start = time.time()
    quotes2 = mf.get_bulk_quotes(codes, show_progress=True)
    time2 = time.time() - start
    print(f"Time: {time2:.2f}s")

    if time2 > 0:
        print(f"\n✓ Second run {time1/time2:.1f}x faster with cache!")
    else:
        print(f"\n✓ Second run instantly faster with cache!")


if __name__ == "__main__":
    try:
        test_bulk_quotes()
        test_portfolio_calculation()
        test_with_caching()

        print("\n\n" + "=" * 70)
        print("ALL BULK FETCHING TESTS COMPLETED!")
        print("=" * 70)
        print("\nKey Benefits:")
        print("• 5-10x faster for portfolio operations")
        print("• Concurrent API calls (default: 10 workers)")
        print("• Automatic caching integration")
        print("• Progress tracking available")
        print("• Perfect for portfolio management tools")

    except KeyboardInterrupt:
        print("\n\n  Tests interrupted by user")
    except Exception as e:
        print(f"\n\n Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()
```


==================================================


## [3/3] Repository: MoneyControl-Stock-Data-News-Scraper (`VAULT_IN-QUANT-062_anubhavv15__MoneyControl-Stock-Data-News-Scraper`)
- **Full Name**: `IN-QUANT-062_anubhavv15__MoneyControl-Stock-Data-News-Scraper`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# stock-market-analyzer-python

## Install Dependencies
```
pip install -r requirements.txt
```

## Use
1. Package to Scrap and Analyze stock market data, market sentiment, news and stocks swot analysis
2. Helpful for stock-market-analysis and investment

## [Individual Stocks data scrapping](https://github.com/MageshDominator/stock-market-analyzer-python/blob/master/companyDataScrapper.py)
Code to scrap following data from moneycontrol
* Technical analysis
* valuation
* community sentiment
* SWOT Analysis

## [Market News Scrapper](https://github.com/MageshDominator/stock-market-analyzer-python/blob/master/newsScrapper.py)
* Scrap news for individual stocks from money control
* Stores scrapped news as excel report

## [Fetch data for stock analysis](https://github.com/MageshDominator/stock-market-analyzer-python/blob/master/fetchOnlyNeededData.py)
* Takes symbols as input
* Fetches the above 2 types of data (stock data and news) for listed symbols

## [Insights from SWOT analysis](https://github.com/MageshDominator/stock-market-analyzer-python/blob/master/swot_analyzer.ipynb)
* Gain insights from SWOT analysis data of listed companies

* skills used
* Python
Web Scraping
Requests
BeautifulSoup (bs4)
Pandas
TQDM
HTML Parsing
Data Extraction & Processing
Data Cleaning
Exception Handling
File Handling
Excel Data Export
Automation
Object-Oriented Programming (OOP)
Web Data Analysis

### Core Implementation Code & Architecture
#### File: `stock-market-analyzer-python-master/fetchOnlyNeededData.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from companyDataScrapper import MoneyControlScrapper
from newsScrapper import MoneyControlNews
from tqdm import tqdm
import pandas as pd


filterSymbols = True

with open("symbols.txt", "r") as fp:
    symbolsNeeded = fp.readlines()

df = pd.read_csv("symlinks.csv")

symbols = list(df["Symbol"])
urls = list(df["symbol_url"])

moneycontrol = MoneyControlScrapper()
allCompanyData = {}
allCompanyNews = {}

for symbol, url in tqdm(zip(symbols, urls)):
    allow = False
    if not filterSymbols:
        allow = True
        
    if filterSymbols and symbol in symbolsNeeded:
        allow = True
    
    if allow:
        temp = moneycontrol.get_analysis(url)
        if temp:
            allCompanyData[symbol] = temp
        
        try:
            scrappe = MoneyControlNews(symbol)
            allCompanyNews[symbol] = scrappe.fetch_a()
        
        except Exception as e:
            print(str(e))
            allCompanyNews[symbol] = str(e)

df = pd.DataFrame(allCompanyData).transpose()

df.to_excel("selectiveStocksData.xlsx")

news_df = pd.DataFrame(allCompanyNews)
news_df.to_excel("selectiveStocksNews.xlsx")
```

#### File: `fetchOnlyNeededData.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:38:59 2020

@author: MAGESHWARAN
"""

from companyDataScrapper import MoneyControlScrapper
from newsScrapper import MoneyControlNews
from tqdm import tqdm
import pandas as pd


filterSymbols = True

with open("symbols.txt", "r") as fp:
    symbolsNeeded = fp.readlines()

df = pd.read_csv("symlinks.csv")

symbols = list(df["Symbol"])
urls = list(df["symbol_url"])

moneycontrol = MoneyControlScrapper()
allCompanyData = {}
allCompanyNews = {}

for symbol, url in tqdm(zip(symbols, urls)):
    allow = False
    if not filterSymbols:
        allow = True
        
    if filterSymbols and symbol in symbolsNeeded:
        allow = True
    
    if allow:
        temp = moneycontrol.get_analysis(url)
        if temp:
            allCompanyData[symbol] = temp
        
        try:
            scrappe = MoneyControlNews(symbol)
            allCompanyNews[symbol] = scrappe.fetch_a()
        
        except Exception as e:
            print(str(e))
            allCompanyNews[symbol] = str(e)

df = pd.DataFrame(allCompanyData).transpose()

df.to_excel("selectiveStocksData.xlsx")

news_df = pd.DataFrame(allCompanyNews)
news_df.to_excel("selectiveStocksNews.xlsx")
```

#### File: `stock-market-analyzer-python-master/companyDataScrapper.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""

import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm
import pandas as pd
import ast
import signal
from contextlib import contextmanager

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


class MoneyControlScrapper(object):
    
    def get_response(self, aurl):
        hdr= {'User-Agent':'Mozilla/5.0'}
        retry = 0
        while retry < 5:
            try: 
                # Waiting 60 seconds to recieve a responser object
                with time_limit(30):
                    content = requests.get(aurl,headers=hdr).content
                break
            
            except Exception:
                print("Error opening url!!")
                print(aurl)
                retry += 1
                continue
        
        if retry == 5:
            return None
        return content
    
    # Procedure to return a parseable BeautifulSoup object of a given url
    def get_soup(self, aurl):
        response = self.get_response(aurl)
        if response:
            soup = BeautifulSoup(response,'html.parser')
        else:
            return None
        return soup
    
    
    def handle_no_swot_data(self, swot, data):
        for type_ in swot.keys():
            data[swot[type_]] = "Data Not Available"
            data["Symbol"] = "Symbol Unavailable"
            return data
    
    
    def get_symbol(self, soup, data):
        symbol_finder = soup.find("p", {"class":"bsns_pcst disin"})
        if not symbol_finder or "NSE:" not in symbol_finder.get_text():
            data["Symbol"] = "Symbol Unavailable"
            return data
        
        print(symbol_finder.get_text().split("NSE:")[1].split()[0].strip().lstrip())
        data["Symbol"] = symbol_finder.get_text().split("NSE:")[1].split()[0].strip().lstrip()
        return data
        
    def get_swot_analysis(self, soup, data):
        swot = {"S":"Strengths", "W": "Weaknesses", "O": "Opportunities",
                "T": "Threats"}
        
        swot_div = soup.find("div", {"class": "swot_feature"})
        if not swot_div:
            data = self.handle_no_swot_data(swot, data)
            return data
        
        link = swot_div.find("a")["href"]
        
        new_soup = self.get_soup(link)
        
        if new_soup == None:
            data = self.handle_no_swot_data(swot, data)
            return data
        
        data = self.get_symbol(new_soup, data)
        swot_points = new_soup.find("section", {"id": "swot_details"}).find("input")["value"]
        
        if not swot_points:
            data = self.handle_no_swot_data(swot, data)
            return data
        
        swot_points = ast.literal_eval(swot_points)
        for type_ in swot.keys():
            try:
                if swot_points[type_]["count"]:
                    data[swot[type_]] = swot_points[type_]["info"]
                else:
                    data[swot[type_]] = "No {} found".format(swot[type_])
            except:
               data[swot[type_]] = "Exception, No {} found".format(swot[type_])
               
        
        data["swot_url"] = link
        return data
        
    def get_technical_analysis(self, soup):
        data = {'Moving Averages': '', 'Technical Indicators': '',
                'Moving Averages Crossovers': ''}
        
        ta = soup.find("div", {"id": "techan_daily"})
        table = ta.find("table", {"class": "mctable1"})
        
        for row in table.find_all("tr"):
            values = row.find_all("td")
            
            if values:
                try:
                    data[values[0].get_text().lstrip().strip()] = values[1].get_text()
                except:
                    pass
                
        return data
    
    def get_valuation(self, soup, data):
        ta = soup.find("div", {"id": "standalone_valuation"})
        lists = ta.find_all("li", {"class": "clearfix"})
        
        for row in lists[:-1]:
            data[row.find("div", {"class":"value_txtfl"}).get_text()] = row.find("div", {"class":"value_txtfr"}).get_text()
        
        return data
    
    def get_community_sentiment(self, soup, data):
        chart = soup.find("ul", {"class": "buy_sellper"})
        if chart:
            lists = chart.find_all("li")
            if lists:
                for row in lists:
                    if "Sentiment" not in data.keys():
                        data["Sentiment"] = row.get_text()
                    else:
                        data["Sentiment"] = data["Sentiment"] + ", " + row.get_text()
            else:
                data["Sentiment"] = "Data Unavailable"
        else:
            data["Sentiment"] = "Data Unavailable"
        return data
    
    def get_analysis(self, url):
        soup= self.get_soup(url)
        
        if soup == None:
            return None
        
        data = self.get_technical_analysis(soup)
        data["symbol_url"] = url
        data = self.get_valuation(soup, data)
        data = self.get_community_sentiment(soup, data)
        data = self.get_swot_analysis(soup, data)
        
        return data
        
    def get_alpha_quotes(self, aurl):
        soup = self.get_soup(aurl)
        allStocksData = {}
        # print(aurl)
        
        list_ = soup.find('table',{'class':'pcq_tbl MT10'})
        
        companies = list_.find_all('a')
        print(len(companies))
        for company in tqdm(companies):
            if company.get_text() != '':
                report = self.get_analysis(company['href'])
                if report:
                    allStocksData[company.get_text()] = report
                    
        return allStocksData
            

if __name__ == '__main__':
    url = 'http://www.moneycontrol.com/india/stockpricequote'
    
    print("Initializing")
    moneycontrol = MoneyControlScrapper()
    allStocksData = moneycontrol.get_alpha_quotes(url)
    
    with open("allData.json", "w") as fp:
        json.dump(allStocksData, fp)
    
    df = pd.DataFrame(allStocksData).transpose()
    
    df.to_excel("overallData_temp.xlsx")
```

#### File: `companyDataScrapper.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:51:09 2020

@author: MAGESHWARAN
"""

import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm
import pandas as pd
import ast
import signal
from contextlib import contextmanager

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


class MoneyControlScrapper(object):
    
    def get_response(self, aurl):
        hdr= {'User-Agent':'Mozilla/5.0'}
        retry = 0
        while retry < 5:
            try: 
                # Waiting 60 seconds to recieve a responser object
                with time_limit(30):
                    content = requests.get(aurl,headers=hdr).content
                break
            
            except Exception:
                print("Error opening url!!")
                print(aurl)
                retry += 1
                continue
        
        if retry == 5:
            return None
        return content
    
    # Procedure to return a parseable BeautifulSoup object of a given url
    def get_soup(self, aurl):
        response = self.get_response(aurl)
        if response:
            soup = BeautifulSoup(response,'html.parser')
        else:
            return None
        return soup
    
    
    def handle_no_swot_data(self, swot, data):
        for type_ in swot.keys():
            data[swot[type_]] = "Data Not Available"
            data["Symbol"] = "Symbol Unavailable"
            return data
    
    
    def get_symbol(self, soup, data):
        symbol_finder = soup.find("p", {"class":"bsns_pcst disin"})
        if not symbol_finder or "NSE:" not in symbol_finder.get_text():
            data["Symbol"] = "Symbol Unavailable"
            return data
        
        print(symbol_finder.get_text().split("NSE:")[1].split()[0].strip().lstrip())
        data["Symbol"] = symbol_finder.get_text().split("NSE:")[1].split()[0].strip().lstrip()
        return data
        
    def get_swot_analysis(self, soup, data):
        swot = {"S":"Strengths", "W": "Weaknesses", "O": "Opportunities",
                "T": "Threats"}
        
        swot_div = soup.find("div", {"class": "swot_feature"})
        if not swot_div:
            data = self.handle_no_swot_data(swot, data)
            return data
        
        link = swot_div.find("a")["href"]
        
        new_soup = self.get_soup(link)
        
        if new_soup == None:
            data = self.handle_no_swot_data(swot, data)
            return data
        
        data = self.get_symbol(new_soup, data)
        swot_points = new_soup.find("section", {"id": "swot_details"}).find("input")["value"]
        
        if not swot_points:
            data = self.handle_no_swot_data(swot, data)
            return data
        
        swot_points = ast.literal_eval(swot_points)
        for type_ in swot.keys():
            try:
                if swot_points[type_]["count"]:
                    data[swot[type_]] = swot_points[type_]["info"]
                else:
                    data[swot[type_]] = "No {} found".format(swot[type_])
            except:
               data[swot[type_]] = "Exception, No {} found".format(swot[type_])
               
        
        data["swot_url"] = link
        return data
        
    def get_technical_analysis(self, soup):
        data = {'Moving Averages': '', 'Technical Indicators': '',
                'Moving Averages Crossovers': ''}
        
        ta = soup.find("div", {"id": "techan_daily"})
        table = ta.find("table", {"class": "mctable1"})
        
        for row in table.find_all("tr"):
            values = row.find_all("td")
            
            if values:
                try:
                    data[values[0].get_text().lstrip().strip()] = values[1].get_text()
                except:
                    pass
                
        return data
    
    def get_valuation(self, soup, data):
        ta = soup.find("div", {"id": "standalone_valuation"})
        lists = ta.find_all("li", {"class": "clearfix"})
        
        for row in lists[:-1]:
            data[row.find("div", {"class":"value_txtfl"}).get_text()] = row.find("div", {"class":"value_txtfr"}).get_text()
        
        return data
    
    def get_community_sentiment(self, soup, data):
        chart = soup.find("ul", {"class": "buy_sellper"})
        if chart:
            lists = chart.find_all("li")
            if lists:
                for row in lists:
                    if "Sentiment" not in data.keys():
                        data["Sentiment"] = row.get_text()
                    else:
                        data["Sentiment"] = data["Sentiment"] + ", " + row.get_text()
            else:
                data["Sentiment"] = "Data Unavailable"
        else:
            data["Sentiment"] = "Data Unavailable"
        return data
    
    def get_analysis(self, url):
        soup= self.get_soup(url)
        
        if soup == None:
            return None
        
        data = self.get_technical_analysis(soup)
        data["symbol_url"] = url
        data = self.get_valuation(soup, data)
        data = self.get_community_sentiment(soup, data)
        data = self.get_swot_analysis(soup, data)
        
        return data
        
    def get_alpha_quotes(self, aurl):
        soup = self.get_soup(aurl)
        allStocksData = {}
        # print(aurl)
        
        list_ = soup.find('table',{'class':'pcq_tbl MT10'})
        
        companies = list_.find_all('a')
        print(len(companies))
        for company in tqdm(companies):
            if company.get_text() != '':
                report = self.get_analysis(company['href'])
                if report:
                    allStocksData[company.get_text()] = report
                    
        return allStocksData
            

if __name__ == '__main__':
    url = 'http://www.moneycontrol.com/india/stockpricequote'
    
    print("Initializing")
    moneycontrol = MoneyControlScrapper()
    allStocksData = moneycontrol.get_alpha_quotes(url)
    
    with open("allData.json", "w") as fp:
        json.dump(allStocksData, fp)
    
    df = pd.DataFrame(allStocksData).transpose()
    
    df.to_excel("overallData_temp.xlsx")
```

#### File: `stock-market-analyzer-python-master/newsScrapper.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import bs4
from tqdm import tqdm

SEARCH_URL = "http://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str="
PREFIX_URL = "http://www.moneycontrol.com"


class MoneyControlNews(object):

    def __init__(self, ticker):
        
        # Declaring all the instance variable for the class
        self.ticker = ticker
        self.a = []     # Stores the announcements listed on the given page
        self.more_anno_link = ""    # Link of the announcement page for the company
        self.more_news_link = ""    # Link of news page for the company
        self.anno_page = "https://www.moneycontrol.com/stocks/company_info/stock_notices.php?sc_did="
        self.template_next_a_page = ""     # For storing the link of the next page of the announcement
        self.a_page_links = []    # Stores the list of links all the announcement pages.
        self.link = ""      # Link to the front page of the company we are looking for on moneycontrol
        self.present_a_page = 0

        self.fetch_ticker()
        self.__fetch_a_next_page_link()


    def fetch_ticker(self):
        try:
            self.link = SEARCH_URL+self.ticker
            r = requests.get(self.link)
            if r.status_code==200:
                print("Fetched page for ticker : "+self.ticker)
                # Creating a bs4 object to store the contents of the requested page
                self.soup = bs4.BeautifulSoup(r.content, 'html.parser')
                try:
                    self.more_anno_link = str(self.soup.find("div", attrs={"class":"clearfix viewmore brdtp"}).find("a", {"title": "View More"})["href"]) # class name extracted after looking at the document
                except:
                    self.more_anno_link = str(self.soup.find("div", attrs={"class":"col_right"}).find("a", {"title": "View More"})["href"]) # class name extracted after looking at the document
                    
                # self.more_news_link = str(self.soup.find("div", attrs={"class":"col_right"}).find("a", {"title": "View More"})["href"]) # class name extracted after looking at the document
                self.anno_page = self.anno_page + self.more_anno_link.split("/")[-1]
                
            elif r.status_code==404:
                print("Page not found")
            else:
                print("A different status code received : "+str(r.status_code))

        except requests.ConnectionError as ce:
            print("There is a network problem (DNS Failure, refused connectionn etc.). Error : "+str(ce))
            raise Exception
        
        except requests.Timeout as te:
            print("Request timed out. Error : "+str(te))
            raise Exception
        
        except requests.TooManyRedirects as tmre:
            print("The request exceeded the maximum no. of redirections. Error : "+str(tmre))
            raise Exception
        
        except requests.exceptions.RequestException as oe:
            print("Any type of request related error : "+str(oe))
            raise Exception
        
        except Exception as e:
            print(e)

    def __fetch_a_next_page_link(self):
        print(self.anno_page)
        # self.template_next_a_page = self.more_anno_link
        # Fetches the template URL for fetching different announcement pages
        r = requests.get(self.anno_page)
        
        announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        # print(announcement_soup)
        # print(announcement_soup.find("div", attrs={"class":"brd_top MT20 MB20"}).find_all("a"))
        # Checking whether the link for the next page is available or not
        if len(announcement_soup.find("div", attrs={"class":"brd_top MT20 MB20"}).find_all("a")) > 0:
            # a = announcement_soup.find("div", attrs={"class":"brd_top MT20 MB20"}).find_all("a")[2]["href"]
            self.template_next_a_page = self.anno_page + "&pno="

    def fetch_a(self, page_no=""):

        # Clear all the previous data in "a" instance variable
        self.a = []

        r = requests.get(self.template_next_a_page + str(page_no))

        if page_no:
            self.present_a_page = page_no

        announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        announcement_soup = announcement_soup.find("ul", attrs={"class":"announe_list MT20"})
        # print(announcement_soup)
        
        raw_links = announcement_soup.find_all("a")
        
        # List of links of all the announcements on the given page
        list_of_links = []
        for x in tqdm(raw_links):
            
            if ".pdf" not in x["href"] and "autono" in x["href"]:
                link = x['href']
                list_of_links.append(link)
                try:
                    a = requests.get(x['href'])
                    anno_page = bs4.BeautifulSoup(a.content, "html.parser")
    
                    title = ""
                    content = ""
    
                    date = next(anno_page.find("p", attrs={"class":"gL_10"}).children)
                    date = self.format_date(date)
    
                    
                    # Checking whether the title of the announcement is available or not
                    if anno_page.find("span", attrs={"class":"bl_15"}):
                        title = anno_page.find("span", attrs={"class":"bl_15"}).text
    
                    # Checking whether content is available or not
                    if anno_page.find("p", attrs={"class":"PT10 b_12"}):
                        content = anno_page.find("p", attrs={"class":"PT10 b_12"}).text
                     
                    anno = {"link":link, "content":content, "title":title, "date":date}
                    self.a.append(anno)
                except:
                    pass
        
        return self.a

    def format_date(self,datetime):
        datetime = datetime.split(" ")
        
        date = datetime[0].split("-")
        time = datetime[1]

        date[0] = date[0][:-2]
        month = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12'
        }
        date[1] = month[date[1]]
        date.reverse()
        date = '-'.join(date)
        final = date+" "+time
        return final


if __name__ == "__main__":
    allNews = {}
    
    import pandas as pd
    df = pd.read_excel("overallData_latest.xlsx")
    
    symbols = df["Symbol"]
    for symbol in tqdm(symbols):
        try:
            scrappe = MoneyControlNews(symbol)
            
            allNews[symbol] = scrappe.fetch_a()
        except Exception as e:
            print(str(e))
            allNews[symbol] = str(e)

    news_df = pd.DataFrame(allNews)
    
    news_df.to_excel("overallNews.xlsx")
```

#### File: `newsScrapper.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 07:36:47 2020

@author: MAGESHWARAN
"""

import requests
import bs4
from tqdm import tqdm

SEARCH_URL = "http://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str="
PREFIX_URL = "http://www.moneycontrol.com"


class MoneyControlNews(object):

    def __init__(self, ticker):
        
        # Declaring all the instance variable for the class
        self.ticker = ticker
        self.a = []     # Stores the announcements listed on the given page
        self.more_anno_link = ""    # Link of the announcement page for the company
        self.more_news_link = ""    # Link of news page for the company
        self.anno_page = "https://www.moneycontrol.com/stocks/company_info/stock_notices.php?sc_did="
        self.template_next_a_page = ""     # For storing the link of the next page of the announcement
        self.a_page_links = []    # Stores the list of links all the announcement pages.
        self.link = ""      # Link to the front page of the company we are looking for on moneycontrol
        self.present_a_page = 0

        self.fetch_ticker()
        self.__fetch_a_next_page_link()


    def fetch_ticker(self):
        try:
            self.link = SEARCH_URL+self.ticker
            r = requests.get(self.link)
            if r.status_code==200:
                print("Fetched page for ticker : "+self.ticker)
                # Creating a bs4 object to store the contents of the requested page
                self.soup = bs4.BeautifulSoup(r.content, 'html.parser')
                try:
                    self.more_anno_link = str(self.soup.find("div", attrs={"class":"clearfix viewmore brdtp"}).find("a", {"title": "View More"})["href"]) # class name extracted after looking at the document
                except:
                    self.more_anno_link = str(self.soup.find("div", attrs={"class":"col_right"}).find("a", {"title": "View More"})["href"]) # class name extracted after looking at the document
                    
                # self.more_news_link = str(self.soup.find("div", attrs={"class":"col_right"}).find("a", {"title": "View More"})["href"]) # class name extracted after looking at the document
                self.anno_page = self.anno_page + self.more_anno_link.split("/")[-1]
                
            elif r.status_code==404:
                print("Page not found")
            else:
                print("A different status code received : "+str(r.status_code))

        except requests.ConnectionError as ce:
            print("There is a network problem (DNS Failure, refused connectionn etc.). Error : "+str(ce))
            raise Exception
        
        except requests.Timeout as te:
            print("Request timed out. Error : "+str(te))
            raise Exception
        
        except requests.TooManyRedirects as tmre:
            print("The request exceeded the maximum no. of redirections. Error : "+str(tmre))
            raise Exception
        
        except requests.exceptions.RequestException as oe:
            print("Any type of request related error : "+str(oe))
            raise Exception
        
        except Exception as e:
            print(e)

    def __fetch_a_next_page_link(self):
        print(self.anno_page)
        # self.template_next_a_page = self.more_anno_link
        # Fetches the template URL for fetching different announcement pages
        r = requests.get(self.anno_page)
        
        announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        # print(announcement_soup)
        # print(announcement_soup.find("div", attrs={"class":"brd_top MT20 MB20"}).find_all("a"))
        # Checking whether the link for the next page is available or not
        if len(announcement_soup.find("div", attrs={"class":"brd_top MT20 MB20"}).find_all("a")) > 0:
            # a = announcement_soup.find("div", attrs={"class":"brd_top MT20 MB20"}).find_all("a")[2]["href"]
            self.template_next_a_page = self.anno_page + "&pno="

    def fetch_a(self, page_no=""):

        # Clear all the previous data in "a" instance variable
        self.a = []

        r = requests.get(self.template_next_a_page + str(page_no))

        if page_no:
            self.present_a_page = page_no

        announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        announcement_soup = announcement_soup.find("ul", attrs={"class":"announe_list MT20"})
        # print(announcement_soup)
        
        raw_links = announcement_soup.find_all("a")
        
        # List of links of all the announcements on the given page
        list_of_links = []
        for x in tqdm(raw_links):
            
            if ".pdf" not in x["href"] and "autono" in x["href"]:
                link = x['href']
                list_of_links.append(link)
                try:
                    a = requests.get(x['href'])
                    anno_page = bs4.BeautifulSoup(a.content, "html.parser")
    
                    title = ""
                    content = ""
    
                    date = next(anno_page.find("p", attrs={"class":"gL_10"}).children)
                    date = self.format_date(date)
    
                    
                    # Checking whether the title of the announcement is available or not
                    if anno_page.find("span", attrs={"class":"bl_15"}):
                        title = anno_page.find("span", attrs={"class":"bl_15"}).text
    
                    # Checking whether content is available or not
                    if anno_page.find("p", attrs={"class":"PT10 b_12"}):
                        content = anno_page.find("p", attrs={"class":"PT10 b_12"}).text
                     
                    anno = {"link":link, "content":content, "title":title, "date":date}
                    self.a.append(anno)
                except:
                    pass
        
        return self.a

    def format_date(self,datetime):
        datetime = datetime.split(" ")
        
        date = datetime[0].split("-")
        time = datetime[1]

        date[0] = date[0][:-2]
        month = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12'
        }
        date[1] = month[date[1]]
        date.reverse()
        date = '-'.join(date)
        final = date+" "+time
        return final


if __name__ == "__main__":
    allNews = {}
    
    import pandas as pd
    df = pd.read_excel("overallData_latest.xlsx")
    
    symbols = df["Symbol"]
    for symbol in tqdm(symbols):
        try:
            scrappe = MoneyControlNews(symbol)
            
            allNews[symbol] = scrappe.fetch_a()
        except Exception as e:
            print(str(e))
            allNews[symbol] = str(e)

    news_df = pd.DataFrame(allNews)
    
    news_df.to_excel("overallNews.xlsx")
```


==================================================
