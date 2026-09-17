# ⚡ [QUANT-SOURCE-104] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_104_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: pyalgotrade (`VAULT_IN-QUANT-102_gbeced__pyalgotrade`)
- **Full Name**: `IN-QUANT-102_gbeced__pyalgotrade`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
PyAlgoTrade
===========

***
**This project is deprecated and is no longer mantained. You may be interested in taking a look at [Basana](https://github.com/gbeced/basana).**
***

[![Build Status](https://travis-ci.org/gbeced/pyalgotrade.png?branch=master)](https://travis-ci.org/gbeced/pyalgotrade)
[![Coverage Status](https://coveralls.io/repos/gbeced/pyalgotrade/badge.svg?branch=master)](https://coveralls.io/r/gbeced/pyalgotrade?branch=master)


PyAlgoTrade is an **event driven algorithmic trading** Python library. Although the initial focus
was on **backtesting**, **paper trading** is now possible using:

 * [Bitstamp](https://www.bitstamp.net/) for Bitcoins

and **live trading** is now possible using:

 * [Bitstamp](https://www.bitstamp.net/) for Bitcoins

To get started with PyAlgoTrade take a look at the [tutorial](http://gbeced.github.io/pyalgotrade/docs/v0.20/html/tutorial.html) and the [full documentation](http://gbeced.github.io/pyalgotrade/docs/v0.20/html/index.html).

Main Features
-------------

 * Event driven.
 * Supports Market, Limit, Stop and StopLimit orders.
 * Supports any type of time-series data in CSV format like Yahoo! Finance, Google Finance, Quandl and NinjaTrader.
 * Bitcoin trading support through [Bitstamp](https://www.bitstamp.net/).
 * Technical indicators and filters like SMA, WMA, EMA, RSI, Bollinger Bands, Hurst exponent and others.
 * Performance metrics like Sharpe ratio and drawdown analysis.
 * Handling Twitter events in realtime.
 * Event profiler.
 * TA-Lib integration.

Installation
------------

PyAlgoTrade is developed and tested using Python 2.7/3.7 and depends on:

 * [NumPy and SciPy](http://numpy.scipy.org/).
 * [pytz](http://pytz.sourceforge.net/).
 * [dateutil](https://dateutil.readthedocs.org/en/latest/).
 * [requests](http://docs.python-requests.org/en/latest/).
 * [matplotlib](http://matplotlib.sourceforge.net/) for plotting support.
 * [ws4py](https://github.com/Lawouach/WebSocket-for-Python) for Bitstamp support.
 * [tornado](http://www.tornadoweb.org/en/stable/) for Bitstamp support.
 * [tweepy](https://github.com/tweepy/tweepy) for Twitter support.

You can install PyAlgoTrade using pip like this:

```
pip install pyalgotrade
```

### Core Implementation Code & Architecture
#### File: `samples/__init__.py`
```python

```

#### File: `pyalgotrade/dispatchprio.py`
```python
FIRST = 0

# We want to process order events before bar feed events.
BROKER = 1000
BAR_FEED = 2000

LAST = None
```

#### File: `samples/csvfeed_1.py`
```python
from __future__ import print_function

from pyalgotrade.feed import csvfeed

feed = csvfeed.Feed("Date", "%Y-%m-%d")
feed.addValuesFromCSV("quandl_gold_2.csv")
for dateTime, value in feed:
    print(dateTime, value)
```

#### File: `samples/tutorial-optimizer-worker.py`
```python
from pyalgotrade.optimizer import worker
import rsi2

# The if __name__ == '__main__' part is necessary if running on Windows.
if __name__ == '__main__':
    worker.run(rsi2.RSI2, "localhost", 5000, workerName="localworker")
```

#### File: `samples/bccharts_example_1.py`
```python
from pyalgotrade.bitcoincharts import barfeed
from pyalgotrade.tools import resample
from pyalgotrade import bar

import datetime


def main():
    barFeed = barfeed.CSVTradeFeed()
    barFeed.addBarsFromCSV("bitstampUSD.csv", fromDateTime=datetime.datetime(2014, 1, 1))
    resample.resample_to_csv(barFeed, bar.Frequency.MINUTE*30, "30min-bitstampUSD.csv")


if __name__ == "__main__":
    main()
```

#### File: `samples/tutorial-1.py`
```python
from pyalgotrade import strategy
from pyalgotrade.barfeed import quandlfeed


class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(MyStrategy, self).__init__(feed)
        self.__instrument = instrument

    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info(bar.getClose())

# Load the bar feed from the CSV file
feed = quandlfeed.Feed()
feed.addBarsFromCSV("orcl", "WIKI-ORCL-2000-quandl.csv")

# Evaluate the strategy with the feed's bars.
myStrategy = MyStrategy(feed, "orcl")
myStrategy.run()
```


==================================================


## [2/3] Repository: qstrader (`WHEEL_qstrader`)
- **Full Name**: `qstrader`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# QSTrader

| Development   | Details       |
| ------------- | ------------- |
| Test Status   | [![Build Status](https://img.shields.io/travis/mhallsmoore/qstrader?label=TravisCI&style=flat-square)](https://travis-ci.org/mhallsmoore/qstrader) [![Coverage Status](https://img.shields.io/coveralls/github/mhallsmoore/qstrader?style=flat-square&label=Coverage)](https://coveralls.io/github/mhallsmoore/qstrader?branch=master) |
| Version Info  | [![PyPI](https://img.shields.io/pypi/v/qstrader?style=flat-square&label=PyPI&color=blue)](https://pypi.org/project/qstrader) [![PyPI Downloads](https://img.shields.io/pypi/dm/qstrader?style=flat-square&label=PyPI%20Downloads)](https://pypi.org/project/qstrader) |
| Compatibility | [![Python Version](https://img.shields.io/pypi/pyversions/qstrader?style=flat-square&label=Python%20Versions)](https://pypi.org/project/qstrader) |
| License       | ![GitHub](https://img.shields.io/github/license/mhallsmoore/qstrader?style=flat-square&label=License) |

QSTrader is a free Python-based open-source modular schedule-driven backtesting framework for long-short equities and ETF based systematic trading strategies.

QSTrader can be best described as a loosely-coupled collection of modules for carrying out end-to-end backtests with realistic trading mechanics.

The default modules provide useful functionality for certain types of systematic trading strategies and can be utilised without modification. However the intent of QSTrader is for the users to extend, inherit or fully replace each module in order to provide custom functionality for their own use case.

The software is currently under active development and is provided under a permissive "MIT" license.

# Previous Version and Advanced Algorithmic Trading

Please note that the previous version of QSTrader, which is utilised through the **Advanced Algorithmic Trading** ebook, can be found along with the appropriate installation instructions [here](https://github.com/mhallsmoore/qstrader/tree/advanced-algorithmic-trading).

It has recently been updated to support Python 3.9, 3.10, 3.11 and 3.12 with up to date package dependencies.

# Installation

Installation requires a Python3 environment. The simplest approach is to download a self-contained scientific Python distribution such as the [Anaconda Individual Edition](https://www.anaconda.com/products/individual#Downloads). You can then install QSTrader into an isolated [virtual environment](https://docs.python.org/3/tutorial/venv.html#virtual-environments-and-packages) using pip as shown below.

Any issues with installation should be reported to the development team as issues [here](https://github.com/mhallsmoore/qstrader/issues).

## conda

[conda](https://docs.conda.io/projects/conda/en/latest/) is a command-line tool that comes with the Anaconda distribution. It allows you to manage virtual environments as well as packages _using the same tool_.

The following command will create a brand new environment called `backtest`.

```
conda create -n backtest python
```
This will use the conda default Python version. At time of writing this was Python 3.12. QSTrader currently supports Python 3.9, 3.10, 3.11 and 3.12. Optionally you can specify a python version by substituting python==3.9 into the command as follows:

```
conda create -n backtest python==3.9
```

In order to start using QSTrader, you need to activate this new environment and install QSTrader using pip.

```
conda activate backtest
pip3 install qstrader
```

## pip

Alternatively, you can use [venv](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) to handle the environment creation and [pip](https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip) to handle the package installation.

```
python -m venv backtest
source backtest/bin/activate  # Need to activate environment before installing package
pip3 install qstrader
```

# Full Documentation

Comprehensive documentation and beginner tutorials for QSTrader can be found on QuantStart.com at [https://www.quantstart.com/qstrader/](https://www.quantstart.com/qstrader/).

# Quickstart

The QSTrader repository provides some simple example strategies at [/examples](https://github.com/mhallsmoore/qstrader/tree/master/examples).

Within this quickstart section a classic 60/40 equities/bonds portfolio will be backtested with monthly rebalancing on the last day of the calendar month.

To get started download the [sixty_forty.py](https://github.com/mhallsmoore/qstrader/blob/master/examples/sixty_forty.py) file and place into the directory of your choice.

The 60/40 script makes use of OHLC 'daily bar' data from Yahoo Finance. In particular it requires the [SPY](https://finance.yahoo.com/quote/SPY/history?p=SPY) and [AGG](https://finance.yahoo.com/quote/AGG/history?p=AGG) ETFs data. Download the full history for each and save as CSV files in same directory as ``sixty_forty.py``.

Assuming that an appropriate Python environment exists and QSTrader has been installed (see **Installation** above), make sure to activate the virtual environment, navigate to the directory with ``sixty_forty.py`` and type:

```
python sixty_forty.py
```

You will then see some console output as the backtest simulation engine runs through each day and carries out the rebalancing logic once per month. Once the backtest is complete a tearsheet will appear:

![Image of 60/40 Backtest](https://quantstartmedia.s3.amazonaws.com/images/qstrader_sixty_forty_backtest.png)

You can examine the commented ``sixty_forty.py`` file to see the current QSTrader backtesting API.

If you have any questions about the installation or example usage then please feel free to email [support@quantstart.com](mailto:support@quantstart.com) or raise an issue [here](https://github.com/mhallsmoore/qstrader/issues).

# Current Features

* **Backtesting Engine** - QSTrader employs a schedule-based portfolio construction approach to systematic trading. Signal generation is decoupled from portfolio construction, risk management, execution and simulated brokerage accounting in a modular, object-oriented fashion.

* **Performance Statistics** - QSTrader provides typical 'tearsheet' performance assessment of strategies. It also supports statistics export via JSON to allow external software to consume metrics from backtests.

* **Free Open-Source Software** - QSTrader has been released under a permissive open-source MIT License. This allows full usage in both research and commercial applications, without restriction, but with no warranty of any kind whatsoever (see **License** below). QSTrader is completely free and costs nothing to download or use.

* **Software Development** - QSTrader is written in the Python programming language for straightforward cross-platform support. QSTrader contains a suite of unit and integration tests for the majority of its modules. Tests are continually added for new features.

# License Terms

Copyright (c) 2015-2024 QuantStart.com, QuarkGluon Ltd

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Trading Disclaimer

Trading equities on margin carries a high level of risk, and may not be suitable for all investors. Past performance is not indicative of future results. The high degree of leverage can work against you as well as for you. Before deciding to invest in equities you should carefully consider your investment objectives, level of experience, and risk appetite. The possibility exists that you could sustain a loss of some or all of your initial investment and therefore you should not invest money that you cannot afford to lose. You should be aware of all the risks associated with equities trading, and seek advice from an independent financial advisor if you have any doubts.

### Core Implementation Code & Architecture
#### File: `scripts/__init__.py`
```python

```

#### File: `qstrader/__init__.py`
```python

```

#### File: `qstrader/statistics/__init__.py`
```python

```

#### File: `qstrader/portcon/__init__.py`
```python

```

#### File: `qstrader/portcon/optimiser/__init__.py`
```python

```

#### File: `qstrader/portcon/order_sizer/__init__.py`
```python

```


==================================================


## [3/3] Repository: pycon2017_algo_trading (`VAULT_IN-QUANT-115_Praxal__pycon2017_algo_trading`)
- **Full Name**: `IN-QUANT-115_Praxal__pycon2017_algo_trading`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
This GitHub repository is created for proposal of my talk at PyCon India 2017 - 
### Introduction to Algorithmic Trading at Indian Stock Markets using Python

(It hasn't been announed yet if this talk is selected)

------------------------------

**For what audience is this talk intended?**

For those interested in using the power of Python to book profits and save time by automating their trading strategies at Indian Stock Markets.

**What is Algorithmic Trading?**

Imagine if you can write a Python script which can, for example, *automatically BUY 100 shares of company 'X' when its price hits 52 week low and SELL it when its price hits 52 week high* or based on some other different strategy which suits you. Sounds cool, right? 

Algorithmic Trading is the process of using computer programs, based on a predefined algorithm, for placing a trade in order to generate profits at a speed and frequency that is impossible for a human trader.

*(The above example is very basic. You can code very complex strategies!)*

**Tell me the advantages of Algorithmic Trading over Conventional Trading**

*Here are a few reasons why algorithmic trading can lead to high chances of success -*


 - Ability to take into account large number of factors for decision making, which can be practically impossible for a human
 - Trades can be timed correctly. Manually placing trade involves delay which may result in significant price change by the time trade is placed
 - Human error eliminated while placing trades

And lastly, you can use your precious time for something else! Just let your computer monitor the stock markets 24x7 and place trade orders for you.

----------


**Ok. Now that you have got me interested, tell me quickly what this TALK will cover.**

For implementing Algorithmic Trading in Python, you need the following -

 - Ability to query current price of a stock in Python
 - Ability to query historical price of a stock in Python
 - Ability to place BUY/SELL trade order at Indian Stock Exchanges (NSE/BSE) using Python
 - A strategy (ie the *Algorithm*), which based on current price and historic data gives out predictions whether to BUY, SELL or HOLD.

**This TALK will demonstrate a simple yet working trading strategy along with backtesting, in Python, covering all the above points.**

*Please note, I have put the target audience as "Beginners" and hence keeping it simple. I agree there is a lot more that can be done in this space.*


Jupyter Notebook for my PyCon 2017 proposal - 
https://in.pycon.org/cfp/2017/proposals/introduction-to-algorithmic-trading-at-indian-stock-markets-using-python~bY0Wa/

### Core Implementation Code & Architecture
#### File: `pycon-strategy-backtesting.py`
```python
import datetime as dt
import pandas
from matplotlib import animation
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from IPython.display import HTML
import time


PATH_DATA_POINTS = r'pycon-tatasteel-data.csv'

class AlgoTrading:
    def __init__(self, sampling_points=-1):
        self.sampling_points = sampling_points
        self.buy_trades = []
        self.sell_trades = []
        self.collect_data()
        self.initialize_crossover()
        self.trade_history = []
        self.qty = 0
        self.previous_profit_percent = 0

    def collect_data(self):
        self.csv = pandas.read_csv(PATH_DATA_POINTS)
        self.dates = [dt.datetime.strptime(date,'%d/%m/%y %H:%M') for date in self.csv['Date']][::-1][:self.sampling_points]
        self.data_points = self.csv['TATASTEEL-EQ C'].tolist()[::-1][:self.sampling_points]

    def update_trade_history(self, stock_price, trade_buy=False, trade_sell=False, profit_percent=-1):
        "Should be called on every data point processed"
        if trade_buy:
            self.qty += 1
            pp = profit_percent
        elif trade_sell:
            self.qty -= 1
            pp = profit_percent
        else:
            pp = self.previous_profit_percent
        self.trade_history.append({'stock_price': stock_price,
                                   'quantity': self.qty,
                                   'profit_percent': pp
                                    })
        self.previous_profit_percent = pp

    def sma(self, data, window):
        """
        Calculates Simple Moving Average
        http://fxtrade.oanda.com/learn/forex-indicators/simple-moving-average
        """
        if len(data) < window:
            return None
        return sum(data[-window:]) / float(window)
    
    def ema(self, data, window):
        if len(data) < 2 * window:
            raise ValueError("data is too short")
        c = 2.0 / (window + 1)
        current_ema = self.sma(data[-window*2:-window], window)
        for value in data[-window:]:
            current_ema = (c * value) + ((1 - c) * current_ema)
        return current_ema

    def initialize_crossover(self):
        self.prev_val1 = 0
        self.prev_val2 = 0

    def crossover(self, val1, val2):
        cmp1 = cmp(val1, val2)
        cmp2 = cmp(self.prev_val1, self.prev_val2)
        if (not (self.prev_val1 == 0 and self.prev_val2 == 0)):         # don't trigger crossover when called first time
            self.prev_val1, self.prev_val2 = val1, val2
            if cmp1 > cmp2:
                return 1
            elif cmp1 < cmp2:
                return -1
            else:
                return 0
        else:
            self.prev_val1, self.prev_val2 = val1, val2
            return 0

    def strategy1(self):
        for i, data in enumerate(self.data_points):
            crossover = 0
            profit_percent = 0
            if i >= 29:      # ema(15) needs atleast 30 points
                crossover = self.crossover(self.ema(self.data_points[:i+1], 3), self.ema(self.data_points[:i+1], 15))
                if (crossover == 1):
                    # Buy crossover
                    print "Buy (Value: %.2f)" % data
                    self.buy_trades.append(data)
                elif (crossover == -1):
                    # Sell crossover
                    print "Sell (Value: %.2f)" % data
                    self.sell_trades.append(data)

                # If crossover happens...
                if (crossover is not 0):
                    buy_qty = len(self.buy_trades)
                    sell_qty = len(self.sell_trades)
                    qty = min(buy_qty, sell_qty)
                    if qty:
                        sell = sum(self.sell_trades[:qty])
                        buy = sum(self.buy_trades[:qty])
                        profit = sell - buy
                        profit_percent = profit*100.0/(buy/len(self.buy_trades))
    #                    self.profit_percents.append(profit_percent)
    #                print 'Buy_qty:%s, Sell qty:%s, Min qty:%s' %(buy_qty, sell_qty, qty)
    #                print 'Buy trades:', [("%.2f" % trade) for trade in self.buy_trades[:qty]]
    #                print 'Sell trades:', [("%.2f" % trade) for trade in self.sell_trades[:qty]]
    #                print 'Total buy: %s' % buy
    #                print 'Total sell: %s' % sell
    #                print 'Total profit: %s' % profit
    #                print 'Total profit_percent: %s' % profit_percent
                        yield profit_percent

            # update history
            self.update_trade_history(data, crossover == 1, crossover == -1, profit_percent)

    def trade(self):
        for profit_percent in self.strategy1():
            print profit_percent

    def animate(self):
        """
        Animates 2 plots -
        1. Stock Price vs Date
        2. Profit percentage vs Date

        Speed of animation can be controlle by playing with 3rd argument of xrange
        """
        df = pandas.DataFrame(self.trade_history)

        plt.ion()
        plt.figure(1)
        plt.hold(True)
        ylim1_min = min(df['stock_price'])
        ylim1_max = max(df['stock_price'])
        ylim2_min = min(df['profit_percent'])
        ylim2_max = max(df['profit_percent'])

        for i in xrange(0, df.shape[0], df.shape[0]/100):
            # Stock price
            plt.subplot(211).cla()
            plt.ylabel('Stock price')
            plt.xlim([self.dates[0], self.dates[-1]])
            plt.ylim([ylim1_min, ylim1_max])
            plt.plot(self.dates[:i], df['stock_price'][:i], color='b')

            # Percentage profit
            plt.subplot(212).cla()
            plt.xlim([self.dates[0], self.dates[-1]])
            plt.ylim([ylim2_min, ylim2_max])
            plt.ylabel('Percentage profit')
            plt.xlabel('Date')
            plt.plot(self.dates[:i], df['profit_percent'][:i], color='b')

            plt.pause(0.01)

            if i == 0:
                time.sleep(5)

        while True:
            time.sleep(1)

    def plot(self):
        """
        Creates 2 plots -
        1. Stock Price vs Date
        2. Profit percentage vs Date
        """

        df = pandas.DataFrame(self.trade_history)

        ylim1_min = min(df['stock_price'])
        ylim1_max = max(df['stock_price'])
        ylim2_min = min(df['profit_percent'])
        ylim2_max = max(df['profit_percent'])

        # Stock price
        plt.subplot(211)
        plt.ylabel('Stock price')
        plt.xlim([self.dates[0], self.dates[-1]])
        plt.ylim([ylim1_min, ylim1_max])
        plt.plot(self.dates, df['stock_price'], color='b')

        # Percentage profit
        plt.subplot(212).cla()
        plt.xlim([self.dates[0], self.dates[-1]])
        plt.ylim([ylim2_min, ylim2_max])
        plt.ylabel('Percentage profit')
        plt.xlabel('Date')
        plt.plot(self.dates, df['profit_percent'], color='b')

        plt.show()


if __name__ == "__main__":
    algotrading = AlgoTrading()
    algotrading.trade()
    algotrading.plot()
#    algotrading.animate()
```


==================================================
