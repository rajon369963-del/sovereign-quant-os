# ⚡ [QUANT-SOURCE-105] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_105_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: pyalgotrading (`VAULT_IN-QUANT-116_algobulls__pyalgotrading`)
- **Full Name**: `IN-QUANT-116_algobulls__pyalgotrading`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# pyalgotrading

Official Python Package for Algorithmic Trading APIs powered by AlgoBulls!

### Features

- Powered by the [AlgoBulls Platform]([https://app.algobulls.com](https://algobulls.com/build/))
- Everything related to Algorithmic Trading Strategies!
    - Free pool of Strategies are available at [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool)!
    - Create & upload strategies easily on the cloud
    - Support for all 150+ Technical Indicators provided by [TA-Lib](https://pypi.org/project/TA-Lib/)
    - Support for multiple candlesticks patterns - Japanese OHLC, Renko, Heikin-Ashi, Linebreak
    - Support for multiple candle intervals - 1 minute, 3 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, 1 hour, 1 day.
    - Support for **Regular Orders**, **Bracket Orders** and **Cover Orders**
    - Support for **MARKET**, **LIMIT**, **STOPLOSS-LIMIT**, **STOPLOSS-MARKET** orders
    - Support for **INTRADAY** and **DELIVERY** orders
- Support for **Backtesting**
- Support for **Paper Trading**
- Support for **Live Trading** / **Real Trading**
- Support for multiple brokers for Live Trading. Check list of supported brokers [here](https://app.algobulls.com/user/brokerlogin).
- Real-time Logs for Backtesting, Paper Trading, Live Trading
- Multiple real-time Reports available for Backtesting, Paper Trading and Live Trading:
    - Profit-&-Loss report (P&L report)
    - Statistics Report
    - Order History Log for each order with state transitions & timestamps
    - Detailed analytics with charts
- Support for calculating Slippage
- Support for calculating Brokerage
- Support for importing external P&L table and generating analytics on the same
- Plot Candlestick charts using [plotly.py](https://github.com/plotly/plotly.py)

Backtesting, Paper Trading and Real Trading can be performed on the same strategy code base!

### Documentation

You can find the docs [here](https://algobulls.github.io/pyalgotrading/).

### Jupyter Notebooks

Easily access and use complete Jupyter Notebook for NASDSAQ and NSE markets [here](https://github.com/algobulls/pyalgotrading/tree/master/jupyter).
You can:
- Easily view them on the web using [nbviewer](https://nbviewer.org/), without installing Python or Jupyter Notebooks.
- Easily execute them on the web using [Binder](https://mybinder.org/), without installing Python or Jupyter Notebooks.
- Download and use them on your local machine, and installing Python & Jupyter Notebooks

### Python

- Python Support: `Python 3.8+`.
- Python Requirements: See [requirements.txt](https://github.com/algobulls/pyalgotrading/blob/master/requirements.txt).
- We recommend you to use the latest version of Python (v3.8+) to enjoy better performance benefits, especially for pandas.

### Installation

Package can be easily installed using `pip` -

```
pip install pyalgotrading
```

### Support / Getting Help

- *Bug Reporting / New Feature Request*: Please [create a new issue](https://github.com/algobulls/pyalgotrading/issues/new) here on GitHub.
- *Discussion Community*: [Slack](https://join.slack.com/t/algotradingninjas/shared_invite/zt-234npz3lu-A1f55maTr~j0tOIoxWA5hA) 
- *Additional Support*: If none of the above help, please contact [pushpak@algobulls.com](mailto:pushpak@algobulls.com).

### Contribution Guidelines

Here’s how we suggest you go about proposing a change to this project:

1. [Fork this project][fork] to your account.
2. [Create a branch][branch] for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request][pr] from your fork’s branch to our `master` branch.

### Rewards

If you are interested in contributing to this repo, **pyalgotrading** or [**pyalgostrategypool**](https://github.com/algobulls/pyalgostrategypool), our official pool of FREE algorithmic trading strategies, please join our official [Slack](https://join.slack.com/t/algotradingninjas/shared_invite/zt-234npz3lu-A1f55maTr~j0tOIoxWA5hA) community.
You would be provided with credits for unlimited trading access on the AlgoBulls platform.


[fork]: https://help.github.com/articles/fork-a-repo/

[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository

[pr]: https://help.github.com/articles/using-pull-requests/

### Changelog

See [CHANGELOG.md](https://github.com/algobulls/pyalgotrading/blob/master/CHANGELOG.md).

### License

See [LICENSE](https://github.com/algobulls/pyalgotrading/blob/master/LICENSE).

### Core Implementation Code & Architecture
#### File: `pyalgotrading/talib/__init__.py`
```python

```

#### File: `pyalgotrading/order/__init__.py`
```python

```

#### File: `pyalgotrading/indicator/__init__.py`
```python

```

#### File: `pyalgotrading/instrument/__init__.py`
```python

```

#### File: `pyalgotrading/utils/__init__.py`
```python

```

#### File: `pyalgotrading/broker/__init__.py`
```python
"""

"""
from . import broker_connection_base
from . import utils
```


==================================================


## [2/3] Repository: Algo-Trading-with-python (`WHEEL_Algo-Trading-with-python`)
- **Full Name**: `Algo-Trading-with-python`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Algo-Trading-with-python

Data : NSE live and historical data

Tool : Pycharm, kiteconnect, kite.trade

Packages: numpy,pandas,datetime,talib,tsf

Objective:
Get the data from live API, Using python(Zerodha Documentation) Automated trade calls (buy,sell) 
when the given condition is satisfied

BUY/SELL Condtion:
Intraday Simple moving average strategy:
SMA20,SMA5

buy when sma5 > sma20
sell when sma5 < sma 20

Calcualted the sma for both live data and historic data in real time for the past 100 days 

TIME Condition:
Interval is given as 5 and the program runs in a continuos while loop where the condition satisfies
every five minutes.

Results

The sma is a very good strategy for intraday however picking the stock is whole different scenario.
I'm gonna update this repository with more interesting strategies and continue to implement advanced
algorithms in addition to the current stratagies.

connect on linkedin for questions:
https://www.linkedin.com/in/muthurishikesh/

### Core Implementation Code & Architecture
#### File: `main.py`
```python
from kiteconnect import KiteConnect
import pandas as pd
import talib
from datetime import datetime, timedelta

if __name__ == '__main__':
    api_key = open('api_key.txt', 'r').read()
    api_secret = open('api_secret.txt', 'r').read()

    kite = KiteConnect(api_key=api_key)
    print('a')

    # first time connection

    # print(kite.login_url())
    # data = kite.generate_session("",api_secret=api_secret)
    # print(data['access_token'])
    # kite.set_access_token(data['access_token'])
    #
    # with open('access_token.txt', 'w' ) as ak:
    #    ak.write(data['access_token'])
    access_token = open('access_token.txt','r').read()
    kite.set_access_token(access_token)
    # from date
    from_date = datetime.strftime(datetime.now() - timedelta(100),'%Y-%m-%d')

    ##yyyy-mm-dd
    to_date = datetime.today().strftime('%Y-%m-%d')

    ## time interval between data
    interval = '5minute'

    tokens = {486657: 'CUMMINSIND', 779521:'SBIN'}
    print('b')
    while True:
        if (datetime.now().second == 0) and (datetime.now().minute % 5 == 0):
         for token in tokens:
            records = kite.historical_data(token, from_date= from_date,to_date=to_date,interval=interval)
            df = pd.DataFrame(records)
            df.drop(df.tail(1).index,inplace=True)


            open = df['open'].values
            high = df['high'].values
            low = df['low'].values
            close = df['close'].values
            volume = df['volume'].values

            sma5 = talib.SMA(close,5)
            sma20 = talib.SMA(close,20)


            price = kite.ltp('NSE:' + tokens[token])


            ltp = price['NSE:'+ tokens[token]]['last_price']

            #Buy Sell Conditions
            if (sma5[-2]<sma20[-2]) and (sma5[-1]>sma20[-1]):

                buy_order_id = kite.place_order(variety= kite.VARIETY_REGULAR,
                                                exchange= kite.EXCHANGE_NSE,
                                                order_type= kite.ORDER_TYPE_MARKET,
                                                tradingsymbol=tokens[token],
                                                transaction_type= kite.TRANSACTION_TYPE_BUY,
                                                quantity= 10,
                                                validity= kite.VALIDITY_DAY,
                                                product= kite.PRODUCT_MIS,
                                                )
            if (sma5[-2]>sma20[-2]) and (sma5[-1]<sma20[-1]):
                sell_order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                                exchange=kite.EXCHANGE_NSE,
                                                order_type=kite.ORDER_TYPE_MARKET,
                                                tradingsymbol=tokens[token],
                                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                                quantity=10,
                                                validity=kite.VALIDITY_DAY,
                                                product=kite.PRODUCT_MIS,
                                                )

            print(kite.orders())
            print(sma5[-2])
            print(sma5[-1])
            print(sma20[-2])
            print(sma20[-1])
```


==================================================


## [3/3] Repository: Algorithmic (`WHEEL_Algorithmic`)
- **Full Name**: `Algorithmic`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# QuantLab

A backtesting research framework for Indian equities (NSE, daily bars), built to answer one question honestly: **which trading claims survive out-of-sample testing after real Indian transaction costs?**

This is a research framework, not a trading system. There is no live execution, no broker integration, and none is planned.

## What's here

| Layer | Location | Purpose |
|---|---|---|
| Data | `quant/data/` | NSE bhavcopy ingestion, corporate-action adjustment, point-in-time universe |
| Engine | `quant/engine/` | Vectorized backtest with next-bar execution, full Indian cost stack, risk limits |
| Strategies | `quant/strategies/` | Momentum, MA crossover, mean reversion — one shared interface |
| Signals | `quant/signals/` | Free alt-data signals (Google Trends, news sentiment) behind the same interface |
| Analytics | `quant/analytics/` | Metrics, walk-forward harness, run export |
| Dashboard | `dashboard/` | Next.js app that renders exported runs from `results/` |
| Research | `research/` | Notebooks and the final writeup — they use the library, never contain logic |

## Methodology commitments

- **No lookahead**: signals computed on day T's close execute at day T+1's open; tested, not assumed.
- **No survivorship bias**: the universe is the index membership *as of each date*, not today's list.
- **Full cost model**: brokerage, STT, exchange charges, GST, stamp duty, plus slippage. All results shown gross vs net.
- **Out-of-sample only**: every strategy is tuned and reported through a walk-forward harness.

## Data sources

Only official, freely published channels: NSE daily reports (bhavcopy, corporate actions), niftyindices.com (index levels, constituent history), manual CSV exports from Google Trends, and public RSS feeds (headlines scored locally with the Loughran-McDonald dictionary; only derived scores are stored). Raw downloads are gitignored and never redistributed through this repository.

Deliberately excluded: yfinance and pytrends (unofficial scraping), any LLM or paid API, satellite/card-panel data (institutional-only versions of the alt-data idea).

## Headline findings (out of sample, net of costs — full note in `research/report.md`)

| Strategy | CAGR net | vs gross | Verdict |
|---|---|---|---|
| Buy & hold NIFTYBEES | +11.9% | −0.1 pt | the bar to beat (also the engine-validation run) |
| Momentum 12-1, monthly | **+26.8%** | −2.2 pt | survives costs |
| MA crossover, monthly | +6.3% | −1.5 pt | loses to the index |
| Mean reversion, weekly | **−17.7%** | −15.6 pt | destroyed by 41× turnover costs |

Exactly one canonical strategy survives its own contract note.

## Setup

```bash
pip install -e ".[dev]"   # Python engine
pytest                    # run the test suite (integration tests need local data)
cd dashboard && pnpm install && pnpm dev     # results dashboard
```

Works on Python 3.9+; a 3.11+ virtualenv is recommended (3.9 is past end-of-life).

## Reproduce

```bash
# 1. pull official NSE history (rate-limited, idempotent; ~15 min for 5 years)
python -m quant.data.bhavcopy --start 2021-01-01 --end 2026-07-07

# 2. (optional, improves adjustment coverage) download the CF-CA corporate
#    actions CSV from nseindia.com -> Corporate Filings -> Corporate Actions
#    into data/raw/corporate_actions/

# 3. run and export backtests
python -m quant.runner buy-and-hold --symbol NIFTYBEES
python -m quant.runner walk-forward --strategy momentum
python -m quant.runner walk-forward --strategy ma-crossover
python -m quant.runner walk-forward --strategy mean-reversion

# 4. view them
cd dashboard && pnpm dev
```

For the alt-data signals: export Google Trends CSVs (region India, 5 years)
into `data/raw/trends/` with a `mapping.csv` (term,symbol), and run the news
collector periodically — `python -m quant.signals.sentiment` (RSS has no
archive, so sentiment history only exists from the day collection starts).

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `quant/__init__.py`
```python
"""QuantLab — backtesting research framework for Indian equities (NSE, daily bars)."""

__version__ = "0.1.0"
```

#### File: `quant/analytics/__init__.py`
```python
"""Analytics: performance metrics, walk-forward harness, run export.

All reported numbers are out-of-sample and shown gross vs net of costs.
"""
```

#### File: `quant/strategies/__init__.py`
```python
"""Rule-based strategies. Every strategy is an adapter at the one seam:

    generate_signals(data) -> target weights

The walk-forward harness and engine only ever see that interface.
"""
```

#### File: `quant/data/__init__.py`
```python
"""Data layer: bhavcopy ingestion, corporate-action adjustment, point-in-time universe.

The rest of the codebase reads market data through one interface: `DataStore`.
No CSV reads outside this package.
"""
```

#### File: `quant/signals/__init__.py`
```python
"""Alt-data signal generators (Google Trends, news sentiment).

Same interface as strategies — `generate_signals(data) -> weights` — so they
run through the identical walk-forward harness with no special-casing.
"""
```


==================================================
