# ⚡ [QUANT-SOURCE-011] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_011_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Indian-Stock-Market_BEL.NS-and-IITL.NS-Dataset-2014-2024 (`VAULT_IN-QUANT-090_deepakdharrao__Indian-Stock-Market_BEL.NS-and-IITL.NS-Dataset-2014-2024`)
- **Full Name**: `IN-QUANT-090_deepakdharrao__Indian-Stock-Market_BEL.NS-and-IITL.NS-Dataset-2014-2024`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
Indian Stock Market Dataset (BEL.NS & IITL.NS) – 2014 to 2024
📌 Overview

This repository contains historical daily stock market data for two Indian companies listed on the National Stock Exchange (NSE), India:

BEL.NS – Bharat Electronics Limited

IITL.NS – Indian Infotech and Software Limited

The dataset spans January 2014 to December 2024 and is intended for financial analysis, time-series modeling, and machine learning research.

📊 Dataset Description

Each dataset is provided in CSV format and includes the following attributes:

Column	Description
Date	Trading date
Open	Opening price (INR)
High	Highest price of the day (INR)
Low	Lowest price of the day (INR)
Close	Closing price (INR)
Adj Close	Adjusted closing price (INR)
Volume	Number of shares traded

Frequency: Daily (excluding weekends and NSE holidays)

Currency: Indian Rupees (INR)

🏢 Companies Covered

Bharat Electronics Limited (BEL.NS): A leading public sector enterprise in defense electronics.

Indian Infotech and Software Limited (IITL.NS): A small-cap company operating in IT and financial services.

The combination enables comparative analysis across different market capitalizations and volatility profiles.

📁 Repository Structure
Indian-Stock-Market-Dataset
│
├── data
│   ├── BEL.NS_2014_2024.csv
│   └── IITL.NS_2014_2024.csv
│
└── README.md

🔍 Data Source

The data was collected from publicly available financial sources such as Yahoo Finance, using official NSE ticker symbols.

🧠 Potential Use Cases

Stock price trend analysis

Time-series forecasting (ARIMA, LSTM, GRU, Transformers)

Volatility and risk analysis

Algorithmic trading research

Financial data exploration and visualization

Academic and educational projects

⚙️ Preprocessing Notes

No normalization or feature engineering applied

Missing dates correspond to non-trading days only

Ready for direct use in ML/DL pipelines

📜 License & Disclaimer

This dataset is provided for educational and research purposes only.
It does not constitute financial or investment advice. Users should verify data accuracy before real-world usage.


==================================================


## [2/3] Repository: IndianStockMarket (`VAULT_IN-QUANT-092_almaastaj__IndianStockMarket`)
- **Full Name**: `IN-QUANT-092_almaastaj__IndianStockMarket`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Indian Stock Market Analysis

This Repo contains two projects related to **Indian Stock Market Analysis**. Here is a short description of these projects:

1. [SENSEX Analysis:](./SensexAnalysis.ipynb) This **SENSEX Analysis Project** is related to performing various financial analysis on the **SENSEX Index** using the data from a period of **10 years** from **2014-2024**.  
   ![SENSEX Analysis](./Images/SENSEXAnalysis.png)
2. [IT Index Creation And Analysis:](./IndianITIndex.ipynb) In this project of **IT Index Creation And Analysis** we create an Index of Top 5 IT Stocks in Indian Stock Market and Analyse the created Index returns.  
   ![IT Index Analysis](./Images/ITIndexAnalysis.png)


==================================================


## [3/3] Repository: zipline-reloaded (`VAULT_IN-QUANT-103_stefan-jansen__zipline-reloaded`)
- **Full Name**: `IN-QUANT-103_stefan-jansen__zipline-reloaded`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<p align="center">
<a href="https://zipline.ml4trading.io">
<img src="https://i.imgur.com/DDetr8I.png" width="25%">
</a>
</p>

# Backtest your Trading Strategies

| Version Info        | [![Python](https://img.shields.io/pypi/pyversions/zipline-reloaded.svg?cacheSeconds=2592000)](https://pypi.python.org/pypi/zipline-reloaded) [![Anaconda-Server Badge](https://anaconda.org/ml4t/zipline-reloaded/badges/platforms.svg)](https://anaconda.org/ml4t/zipline-reloaded) ![PyPI](https://img.shields.io/pypi/v/zipline-reloaded) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/zipline-reloaded/badges/version.svg)](https://anaconda.org/conda-forge/zipline-reloaded)                                                                                                                                                                                                 |
| ------------------- | ---------- |
| **Test** **Status** | [![CI Tests](https://github.com/stefan-jansen/zipline-reloaded/actions/workflows/ci_tests_full.yml/badge.svg)](https://github.com/stefan-jansen/zipline-reloaded/actions/workflows/unit_tests.yml) [![PyPI](https://github.com/stefan-jansen/zipline-reloaded/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/stefan-jansen/zipline-reloaded/actions/workflows/build_wheels.yml)  [![codecov](https://codecov.io/gh/stefan-jansen/zipline-reloaded/branch/main/graph/badge.svg)](https://codecov.io/gh/stefan-jansen/zipline-reloaded) |
| **Community**       | [![Discourse](https://img.shields.io/discourse/topics?server=https%3A%2F%2Fexchange.ml4trading.io%2F)](https://exchange.ml4trading.io) [![ML4T](https://img.shields.io/badge/Powered%20by-ML4Trading-blue)](https://ml4trading.io) [![Twitter](https://img.shields.io/twitter/follow/ml4trading.svg?style=social)](https://twitter.com/ml4trading)                                                                                                                                                                                                                                                                                                                                                                                                          |

Zipline is a Pythonic event-driven system for backtesting, developed and used as the backtesting and live-trading engine by [crowd-sourced investment fund Quantopian](https://www.bizjournals.com/boston/news/2020/11/10/quantopian-shuts-down-cofounders-head-elsewhere.html). Since it closed late 2020, the domain that had hosted these docs expired. The library is used extensively in the book [Machine Larning for Algorithmic Trading](https://ml4trading.io)
by [Stefan Jansen](https://www.linkedin.com/in/applied-ai/) who is trying to keep the library up to date and available to his readers and the wider Python algotrading community.
- [Join our Community!](https://exchange.ml4trading.io)
- [Documentation](https://zipline.ml4trading.io)

## Features

- **Ease of Use:** Zipline tries to get out of your way so that you can focus on algorithm development. See below for a code example.
- **Batteries Included:** many common statistics like moving average and linear regression can be readily accessed from within a user-written algorithm.
- **PyData Integration:** Input of historical data and output of performance statistics are based on Pandas DataFrames to integrate nicely into the existing PyData ecosystem.
- **Statistics and Machine Learning Libraries:** You can use libraries like matplotlib, scipy, statsmodels, and scikit-klearn to support development, analysis, and visualization of state-of-the-art trading systems.

> **Note:** Release 3.05 makes Zipline compatible with Numpy 2.0, which requires Pandas 2.2.2 or higher. If you are using an older version of Pandas, you will need to upgrade it. Other packages may also still take more time to catch up with the latest Numpy release.

> **Note:** Release 3.0 updates Zipline to use [pandas](https://pandas.pydata.org/pandas-docs/stable/whatsnew/v2.0.0.html) >= 2.0 and [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) > 2.0. These are major version updates that may break existing code; please review the linked docs.

> **Note:** Release 2.4 updates Zipline to use [exchange_calendars](https://github.com/gerrymanoim/exchange_calendars) >= 4.2. This is a major version update and may break existing code (which we have tried to avoid but cannot guarantee). Please review the changes [here](https://github.com/gerrymanoim/exchange_calendars/issues/61).

## Installation

Zipline supports Python >= 3.9 and is compatible with current versions of the relevant [NumFOCUS](https://numfocus.org/sponsored-projects?_sft_project_category=python-interface) libraries, including [pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/stable/index.html).

### Using `pip`

If your system meets the pre-requisites described in the [installation instructions](https://zipline.ml4trading.io/install.html), you can install Zipline using `pip` by running:

```bash
pip install zipline-reloaded
```

### Using `conda`

If you are using the [Anaconda](https://www.anaconda.com/products/individual) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) distributions, you install `zipline-reloaded` from the channel `conda-forge` like so:

```bash
conda install -c conda-forge zipline-reloaded
```

You can also [enable](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html) `conda-forge` by listing it in your `.condarc`.

In case you are installing `zipline-reloaded` alongside other packages and encounter [conflict errors](https://github.com/conda/conda/issues/9707), consider using [mamba](https://github.com/mamba-org/mamba) instead.

See the [installation](https://zipline.ml4trading.io/install.html) section of the docs for more detailed instructions and the corresponding [conda-forge site](https://github.com/conda-forge/zipline-reloaded-feedstock).

## Quickstart

See our [getting started tutorial](https://zipline.ml4trading.io/beginner-tutorial).

The following code implements a simple dual moving average algorithm.

```python
from zipline.api import order_target, record, symbol


def initialize(context):
    context.i = 0
    context.asset = symbol('AAPL')


def handle_data(context, data):
    # Skip first 300 days to get full windows
    context.i += 1
    if context.i < 300:
        return

    # Compute averages
    # data.history() has to be called with the same params
    # from above and returns a pandas dataframe.
    short_mavg = data.history(context.asset, 'price', bar_count=100, frequency="1d").mean()
    long_mavg = data.history(context.asset, 'price', bar_count=300, frequency="1d").mean()

    # Trading logic
    if short_mavg > long_mavg:
        # order_target orders as many shares as needed to
        # achieve the desired number of shares.
        order_target(context.asset, 100)
    elif short_mavg < long_mavg:
        order_target(context.asset, 0)

    # Save values for later inspection
    record(AAPL=data.current(context.asset, 'price'),
           short_mavg=short_mavg,
           long_mavg=long_mavg)
```

You can then run this algorithm using the Zipline CLI. But first, you need to download some market data with historical prices and trading volumes.

This will download asset pricing data from [NASDAQ](https://data.nasdaq.com/databases/WIKIP) (formerly [Quandl](https://www.nasdaq.com/about/press-center/nasdaq-acquires-quandl-advance-use-alternative-data)).

> This requires an API key, which you can get for free by signing up at [NASDAQ Data Link](https://data.nasdaq.com).

```bash
$ export QUANDL_API_KEY="your_key_here"
$ zipline ingest -b quandl
````

The following will 
- stream the through the algorithm over the specified time range. 
- save the resulting performance DataFrame as `dma.pickle`, which you can load and analyze from Python using, e.g., [pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded).

```bash
$ zipline run -f dual_moving_average.py --start 2014-1-1 --end 2018-1-1 -o dma.pickle --no-benchmark
```

You can find other examples in the [zipline/examples](https://github.com/stefan-jansen/zipline-reloaded/tree/main/src/zipline/examples) directory.

## Questions, suggestions, bugs?

If you find a bug or have other questions about the library, feel free to [open an issue](https://github.com/stefan-jansen/zipline/issues/new) and fill out the template.

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/pipeline/__init__.py`
```python

```

#### File: `tests/resources/__init__.py`
```python

```

#### File: `tests/utils/__init__.py`
```python

```

#### File: `tests/history/__init__.py`
```python

```

#### File: `tests/events/__init__.py`
```python

```


==================================================
