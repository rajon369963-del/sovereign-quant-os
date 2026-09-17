# ⚡ [QUANT-SOURCE-115] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_115_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: catalyst (`PHASE4-QUANT-106`)
- **Full Name**: `PHASE4-QUANT-106_scrtlabs__catalyst`
- **Description**: An Algorithmic Trading Library for Crypto-Assets in Python
- **GitHub Stars**: 2558
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
.. image:: https://s3.amazonaws.com/enigmaco-docs/catalyst-crypto.png
    :target: https://enigmampc.github.io/catalyst
    :align: center
    :alt: Enigma | Catalyst

|version tag|
|version status|
|forum|
|discord|
|twitter|

=========  ===============           ================
Service    Master                    Develop
---------  ---------------           ----------------
CI Badge   |travis-master|           |travis-develop|
=========  ===============           ================

⚠️ DEPRECATION WARNING ⚠️
=========================

This repo is no longer actively maintained since the end of 2018. If you wish to use this project or get support for it, there are many forks that may be more active. If any of those is still active, please get in touch with them, as we can no longer provide support for it.

----

Catalyst is an algorithmic trading library for crypto-assets written in Python.
It allows trading strategies to be easily expressed and backtested against 
historical data (with daily and minute resolution), providing analytics and 
insights regarding a particular strategy's performance. Catalyst also supports
live-trading of crypto-assets starting with four exchanges (Binance, Bitfinex, Bittrex,
and Poloniex) with more being added over time. Catalyst empowers users to share 
and curate data and build profitable, data-driven investment strategies. Please 
visit `catalystcrypto.io <https://www.catalystcrypto.io>`_ to learn more about Catalyst.

Catalyst builds on top of the well-established 
`Zipline <https://github.com/quantopian/zipline>`_ project. We did our best to 
minimize structural changes to the general API to maximize compatibility with 
existing trading algorithms, developer knowledge, and tutorials. Join us on the 
`Catalyst Forum <https://forum.catalystcrypto.io/>`_ for questions around Catalyst,
algorithmic trading and technical support. We also have a 
`Discord <https://discord.gg/SJK32GY>`_ group with the *#catalyst_dev* and 
*#catalyst_setup* dedicated channels.

Overview
========

-  Ease of use: Catalyst tries to get out of your way so that you can 
   focus on algorithm development. See 
   `examples of trading strategies <https://github.com/enigmampc/catalyst/tree/master/catalyst/examples>`_ 
   provided.
-  Support for several of the top crypto-exchanges by trading volume:
   `Bitfinex <https://www.bitfinex.com>`_, `Bittrex <http://www.bittrex.com>`_,
   `Poloniex <https://www.poloniex.com>`_ and `Binance <https://www.binance.com/>`_.
-  Secure: You and only you have access to each exchange API keys for your accounts.
-  Input of historical pricing data of all crypto-assets by exchange, 
   with daily and minute resolution. See 
   `Catalyst Market Coverage Overview <https://www.enigma.co/catalyst/status>`_.
-  Backtesting and live-trading functionality, with a seamless transition
   between the two modes.
-  Output of performance statistics are based on Pandas DataFrames to 
   integrate nicely into the existing PyData eco-system.
-  Statistic and machine learning libraries like matplotlib, scipy, 
   statsmodels, and sklearn support development, analysis, and 
   visualization of state-of-the-art trading systems.
-  Addition of Bitcoin price (btc_usdt) as a benchmark for comparing 
   performance across trading algorithms.

Go to our `Documentation Website <https://enigmampc.github.io/catalyst/>`_.




.. |version tag| image:: https://img.shields.io/pypi/v/enigma-catalyst.svg
   :target: https://pypi.python.org/pypi/enigma-catalyst

.. |version status| image:: https://img.shields.io/pypi/pyversions/enigma-catalyst.svg
   :target: https://pypi.python.org/pypi/enigma-catalyst
   
.. |forum| image:: https://img.shields.io/badge/forum-join-green.svg
   :target: https://forum.catalystcrypto.io/

.. |discord| image:: https://img.shields.io/badge/discord-join%20chat-green.svg
   :target: https://discordapp.com/invite/SJK32GY

.. |twitter| image:: https://img.shields.io/twitter/follow/enigmampc.svg?style=social&label=Follow&style=flat-square
   :target: https://twitter.com/catalystcrypto

.. |travis-develop| image:: https://travis-ci.com/enigmampc/catalyst.svg?branch=develop
   :target: https://travis-ci.com/enigmampc/catalyst

.. |travis-master| image:: https://travis-ci.com/enigmampc/catalyst.svg?branch=master
   :target: https://travis-ci.com/enigmampc/catalyst

### Core Implementation Code & Architecture
#### File: `catalyst/exchange/__init__.py`
```python

```

#### File: `catalyst/exchange/ccxt/__init__.py`
```python

```

#### File: `catalyst/exchange/utils/__init__.py`
```python

```

#### File: `catalyst/patches/__init__.py`
```python

```

#### File: `catalyst/marketplace/__init__.py`
```python

```

#### File: `catalyst/marketplace/utils/__init__.py`
```python

```


==================================================


## [2/3] Repository: qtpylib (`PHASE4-QUANT-107`)
- **Full Name**: `PHASE4-QUANT-107_ranaroussi__qtpylib`
- **Description**: QTPyLib, Pythonic Algorithmic Trading 
- **GitHub Stars**: 2267
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
QTPyLib, Pythonic Algorithmic Trading
=====================================

.. image:: https://img.shields.io/badge/python-3.4+-blue.svg?style=flat
    :target: https://pypi.python.org/pypi/qtpylib
    :alt: Python version

.. image:: https://img.shields.io/pypi/v/qtpylib.svg?maxAge=60
    :target: https://pypi.python.org/pypi/qtpylib
    :alt: PyPi version

.. image:: https://img.shields.io/pypi/status/qtpylib.svg?maxAge=60
    :target: https://pypi.python.org/pypi/qtpylib
    :alt: PyPi status

.. image:: https://img.shields.io/travis/ranaroussi/qtpylib/main.svg?maxAge=1
    :target: https://travis-ci.org/ranaroussi/qtpylib
    :alt: Travis-CI build status

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
    :target: http://qtpylib.io/docs/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Chat-Discord-%237289d6.svg?style=flat&logo=discord&maxAge=60
    :target: https://discord.gg/7wEzsuV
    :alt: Chat on Discord

.. image:: https://img.shields.io/github/stars/ranaroussi/qtpylib.svg?style=social&label=Star&maxAge=60
    :target: https://github.com/ranaroussi/qtpylib
    :alt: Star this repo

.. image:: https://img.shields.io/twitter/follow/aroussi.svg?style=social&label=Follow&maxAge=60
    :target: https://twitter.com/aroussi
    :alt: Follow me on twitter

\

QTPyLib (**Q**\ uantitative **T**\ rading **Py**\ thon **Lib**\ rary)
is a simple, **event-driven algorithmic trading library** written in Python,
that supports backtesting, as well as paper and live trading via
`Interactive Brokers <https://www.interactivebrokers.com>`_.

I developed QTPyLib because I wanted for a simple,
yet powerful, trading library that will let me focus on the
trading logic itself and ignore everything else.

`Full Documentation » <http://www.qtpylib.io/>`_

`Changelog » <./CHANGELOG.rst>`_

-----

**Read about the future of QTPyLib here:**
https://aroussi.com/post/the-future-of-qtpylib

-----

Features
========

- A continuously-running Blotter that lets you capture market data even when your algos aren't running.
- Tick, Bar and Trade data is stored in MySQL for later analysis and backtesting.
- Using pub/sub architecture using `ØMQ <http://zeromq.org>`_ (ZeroMQ) for communicating between the Algo and the Blotter allows for a single Blotter/multiple Algos running on the same machine.
- **Support for Order Book, Quote, Time, Tick or Volume based strategy resolutions**.
- Includes many common indicators that you can seamlessly use in your algorithm.
- **Market data events use asynchronous, non-blocking architecture**.
- Have orders delivered to your mobile via SMS (requires a `Nexmo <https://www.nexmo.com/>`_ or `Twilio <https://www.twilio.com/>`_ account).
- Full integration with `TA-Lib <http://ta-lib.org>`_ via dedicated module (`see documentation <http://qtpylib.io/docs/latest/indicators.html#ta-lib-integration>`_).
- Ability to import any Python library (such as `scikit-learn <http://scikit-learn.org>`_ or `TensorFlow <https://www.tensorflow.org>`_) to use them in your algorithms.

-----

Quickstart
==========

There are 5 main components to QTPyLib:

1. ``Blotter`` - handles market data retrieval and processing.
2. ``Broker`` - sends and process orders/positions (abstracted layer).
3. ``Algo`` - (sub-class of ``Broker``) communicates with the ``Blotter`` to pass market data to your strategies, and process/positions orders via ``Broker``.
4. ``Reports`` - provides real-time monitoring of trades and open positions via Web App, as well as a simple REST API for trades, open positions, and market data.
5. Lastly, **Your Strategies**, which are sub-classes of ``Algo``, handle the trading logic/rules. This is where you'll write most of your code.


1. Get Market Data
------------------

To get started, you need to first create a Blotter script:

.. code:: python

    # blotter.py
    from qtpylib.blotter import Blotter

    class MainBlotter(Blotter):
        pass # we just need the name

    if __name__ == "__main__":
        blotter = MainBlotter()
        blotter.run()

Then, with IB TWS/GW running, run the Blotter from the command line:

.. code:: bash

    $ python blotter.py

If your strategy needs order book / market depth data, add the ``--orderbook`` flag to the command:

.. code:: bash

    $ python blotter.py --orderbook


2. Write your Algorithm
-----------------------

While the Blotter running in the background, write and execute your algorithm:

.. code:: python

    # strategy.py
    from qtpylib.algo import Algo

    class CrossOver(Algo):

        def on_start(self):
            pass

        def on_fill(self, instrument, order):
            pass

        def on_quote(self, instrument):
            pass

        def on_orderbook(self, instrument):
            pass

        def on_tick(self, instrument):
            pass

        def on_bar(self, instrument):
            # get instrument history
            bars = instrument.get_bars(window=100)

            # or get all instruments history
            # bars = self.bars[-20:]

            # skip first 20 days to get full windows
            if len(bars) < 20:
                return

            # compute averages using internal rolling_mean
            bars['short_ma'] = bars['close'].rolling(window=10).mean()
            bars['long_ma']  = bars['close'].rolling(window=20).mean()

            # get current position data
            positions = instrument.get_positions()

            # trading logic - entry signal
            if bars['short_ma'].crossed_above(bars['long_ma'])[-1]:
                if not instrument.pending_orders and positions["position"] == 0:

                    # buy one contract
                    instrument.buy(1)

                    # record values for later analysis
                    self.record(ma_cross=1)

            # trading logic - exit signal
            elif bars['short_ma'].crossed_below(bars['long_ma'])[-1]:
                if positions["position"] != 0:

                    # exit / flatten position
                    instrument.exit()

                    # record values for later analysis
                    self.record(ma_cross=-1)


    if __name__ == "__main__":
        strategy = CrossOver(
            instruments = [ ("ES", "FUT", "GLOBEX", "USD", 201609, 0.0, "") ], # ib tuples
            resolution  = "1T", # Pandas resolution (use "K" for tick bars)
            tick_window = 20, # no. of ticks to keep
            bar_window  = 5, # no. of bars to keep
            preload     = "1D", # preload 1 day history when starting
            timezone    = "US/Central" # convert all ticks/bars to this timezone
        )
        strategy.run()


To run your algo in a **live** enviroment, from the command line, type:

.. code:: bash

    $ python strategy.py --logpath ~/qtpy/


The resulting trades be saved in ``~/qtpy/STRATEGY_YYYYMMDD.csv`` for later analysis.


3. Viewing Live Trades
----------------------

While the Blotter running in the background, write the dashboard:

.. code:: python

    # dashboard.py
    from qtpylib.reports import Reports

    class Dashboard(Reports):
        pass # we just need the name

    if __name__ == "__main__":
        dashboard = Dashboard(port = 5000)
        dashboard.run()


To run your dashboard, run it from the command line:

.. code:: bash

    $ python dashboard.py

    >>> Dashboard password is: a0f36d95a9
    >>> Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Now, point your browser to http://localhost:5000 and use the password generated to access your dashboard.

-----


.. note::

    You can find other examples in the ``qtpylib/examples directory``.
    Please refer to the `Full Documentation <http://www.qtpylib.io/>`_ to learn
    how to enable SMS notifications, use the bundled Indicators, and more.



Installation
============

Install using ``pip``:

.. code:: bash

    $ pip install qtpylib --upgrade --no-cache-dir


Requirements
------------

* `Python <https://www.python.org>`_ >=3.4
* `Pandas <https://github.com/pydata/pandas>`_ (tested to work with >=0.18.1)
* `Numpy <https://github.com/numpy/numpy>`_ (tested to work with >=1.11.1)
* `PyZMQ <https://github.com/zeromq/pyzmq>`_ (tested to work with >=15.2.1)
* `PyMySQL <https://github.com/PyMySQL/PyMySQL>`_ (tested to work with >=0.7.6)
* `pytz <http://pytz.sourceforge.net>`_ (tested to work with >=2016.6.1)
* `dateutil <https://pypi.python.org/pypi/python-dateutil>`_ (tested to work with >=2.5.1)
* `Nexmo-Python <https://github.com/Nexmo/nexmo-python>`_ for SMS support (tested to work with >=1.2.0)
* `Twilio-Python <https://github.com/twilio/twilio-python>`_ for SMS support (tested to work with >=5.4.0)
* `Flask <http://flask.pocoo.org>`_ for the Dashboard (tested to work with >=0.11)
* `Requests <https://github.com/kennethreitz/requests>`_ (tested to work with >=2.10.0)
* `IbPy2 <https://github.com/blampe/IbPy>`_ (tested to work with >=0.8.0)
* `ezIBpy <https://github.com/ranaroussi/ezibpy>`_ (IbPy wrapper, tested to work with >=1.12.66)
* Latest Interactive Brokers’ `TWS <https://www.interactivebrokers.com/en/index.php?f=15875>`_ or `IB Gateway <https://www.interactivebrokers.com/en/index.php?f=16457>`_ installed and running on the machine
* `MySQL Server <https://www.mysql.com/>`_ installed and running with a database for QTPyLib

-----

Legal Stuff
===========

QTPyLib is licensed under the **Apache License, Version 2.0**. A copy of which is included in LICENSE.txt.

QTPyLib is not a product of Interactive Brokers, nor is it affiliated with Interactive Brokers.



P.S.
----

I'm very interested in your experience with QTPyLib. Please drop me a note with any feedback you have.

**Ran**

### Core Implementation Code & Architecture
#### File: `examples/dashboard.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QTPyLib: Quantitative Trading Python Library
# https://github.com/ranaroussi/qtpylib
#
# Copyright 2016-2018 Ran Aroussi
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

from qtpylib.reports import Reports


class Dashboard(Reports):
    pass  # we just need the name


# ===========================================
if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()
```

#### File: `examples/blotter.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QTPyLib: Quantitative Trading Python Library
# https://github.com/ranaroussi/qtpylib
#
# Copyright 2016-2018 Ran Aroussi
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

from qtpylib.blotter import Blotter


class MainBlotter(Blotter):
    pass  # we just need the name


# ===========================================
if __name__ == "__main__":
    blotter = MainBlotter()
    blotter.run()
```

#### File: `qtpylib/__init__.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QTPyLib: Quantitative Trading Python Library
# https://github.com/ranaroussi/qtpylib
#
# Copyright 2016-2018 Ran Aroussi
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
#

__version__ = '1.5.84'
__author__ = 'Ran Aroussi'

import os
import sys

# make indicators available as pandas extentions
import qtpylib.indicators as indicators

from . import *

path = {
    "library": os.path.dirname(os.path.realpath(__file__)),
    "caller": os.path.dirname(os.path.realpath(sys.argv[0]))
}

__all__ = [
    'blotter',
    'algo',
    'broker',
    'tools',
    'sms',
    'indicators',
    'talib_indicators',
    'futures',
    'path'
]
```

#### File: `qtpylib/tests/test_indicators.py`
```python
from nose.tools import eq_
import pandas as pd
import numpy as np
from qtpylib import indicators as qtind

def test_indicator_stoch_slow():
    """Test the stochastic indicator logic"""

    data = {'open': range(15, 150, 15),
            'high': range(20, 200, 20),
            'low': range(10, 100, 10),
            'close': range(10, 100, 10),
        }

    df = pd.DataFrame(data=data)
    my_stoch = qtind.stoch(df, window=5, d=3, k=3, fast=False)

    last_stoch_slow_k = int(my_stoch['slow_k'].tail(1)*1000)
    last_stoch_slow_d = int(my_stoch['slow_d'].tail(1)*1000)
    eq_(last_stoch_slow_k, 33488)
    eq_(last_stoch_slow_d, 36774)

def test_indicator_stoch_fast():
    """Test the stochastic indicator logic"""

    data = {'open': range(15, 150, 15),
            'high': range(20, 200, 20),
            'low': range(10, 100, 10),
            'close': range(10, 100, 10),
        }

    df = pd.DataFrame(data=data)
    my_stoch = qtind.stoch(df, window=5, d=3, k=3, fast=True)

    last_stoch_fast_k = int(my_stoch['fast_k'].tail(1)*1000)
    last_stoch_fast_d = int(my_stoch['fast_d'].tail(1)*1000)
    eq_(last_stoch_fast_k, 30769)
    eq_(last_stoch_fast_d, 33488)
```

#### File: `setup.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""QTPyLib: Quantitative Trading Python Library
(https://github.com/ranaroussi/qtpylib)
Simple, event-driven algorithmic trading system written in
Python 3, that supports backtesting and live trading using
Interactive Brokers for market data and order execution.
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='QTPyLib',
    version='1.5.84',
    description='Quantitative Trading Python Library',
    long_description=long_description,
    url='https://github.com/ranaroussi/qtpylib',
    author='Ran Aroussi',
    author_email='ran@aroussi.com',
    license='LGPL',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',

        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    platforms = ['any'],
    keywords='qtpylib qtpy algotrading algo trading interactive brokers tws ibgw ibpy ezibpy',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'demo', 'demos', 'examples']),
    install_requires=[
        'python-dateutil>=2.5.3','ezibpy>=1.12.66',
        'flask>=0.11.1','numpy>=1.11.1','pandas>=0.22.0','pymysql>=0.7.6',
        'pytz>=2016.6.1','requests>=2.10.0','pyzmq>=15.2.1',
        'nexmo>=1.2.0','twilio>=5.4.0','ibpy2>=0.8.0',
    ],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },

    include_package_data=True,
    package_data={
        'static': ['qtpylib/_webapp/*'],
        'db': ['qtpylib/schema.sql*']
    },
)
```

#### File: `examples/strategy.py`
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# QTPyLib: Quantitative Trading Python Library
# https://github.com/ranaroussi/qtpylib
#
# Copyright 2016-2018 Ran Aroussi
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

import random

from qtpylib.algo import Algo
from qtpylib import futures


class TestStrategy(Algo):
    """
    Example: This Strategy buys/sells single contract of the
    S&P E-mini Futures (ES) every 10th tick with a +/- 0.5
    tick target/stop using LIMIT order.

    If still in position for next 5 ticks, an exit order is issued.
    """

    count = 0

    # ---------------------------------------
    def on_start(self):
        """ initilize tick counter """
        self.count = 0

    # ---------------------------------------
    def on_quote(self, instrument):
        # quote = instrument.get_quote()
        # ^^ quote data available via get_quote()
        pass

    # ---------------------------------------
    def on_orderbook(self, instrument):
        pass

    # ---------------------------------------
    def on_fill(self, instrument, order):
        pass

    # ---------------------------------------
    def on_tick(self, instrument):

        # increase counter and do nothing if nor 10th tick
        self.count += 1

        if self.count % 10 != 0:
            return

        # continue ...

        # get last tick dict
        tick = instrument.get_ticks(lookback=1, as_dict=True)

        if instrument.positions['position']:
            print(instrument.symbol, "still in position. Exiting...")
            instrument.exit()
        else:
            if instrument.pending_orders:
                print(instrument.symbol, "has a pending order. Wait...")
            else:
                # random order direction
                direction = random.choice(["BUY", "SELL"])
                print(instrument.symbol,
                      'not in position. Sending a bracket ', direction, 'order...')

                if direction == "BUY":
                    target = tick['last'] + 0.5
                    stoploss = tick['last'] - 0.5
                else:
                    target = tick['last'] - 0.5
                    stoploss = tick['last'] + 0.5

                instrument.order(direction, 1,
                                 limit_price=tick['last'],
                                 target=target,
                                 initial_stop=stoploss,
                                 trail_stop_at=0,
                                 trail_stop_by=0,
                                 expiry=5
                                 )

                # record action
                self.record(take_action=1)

    # ---------------------------------------
    def on_bar(self, instrument):
        # nothing exiting here...
        bar = instrument.get_bars(lookback=1, as_dict=True)
        print("BAR:", bar)



# ===========================================
if __name__ == "__main__":
    # get most active ES contract to trade
    ACTIVE_MONTH = futures.get_active_contract("ES")
    print("Active month for ES is:", ACTIVE_MONTH)

    strategy = TestStrategy(
        instruments=[("ES", "FUT", "GLOBEX", "USD", ACTIVE_MONTH, 0.0, "")],
        resolution="1T",
        tick_window=10,
        bar_window=10
    )
    strategy.run()
```


==================================================


## [3/3] Repository: hummingbot_chinese (`PHASE4-QUANT-118`)
- **Full Name**: `PHASE4-QUANT-118_ttggs__hummingbot_chinese`
- **Description**: hummingbot中文资源
- **GitHub Stars**: 798
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
![Hummingbot](/images/blacklogo.png)
## 📌 Hummingbot 中文社区资源
🔗 **社交平台**
- 🏮 [知乎](https://www.zhihu.com/people/dao-mu-70-83)
- 📺 [Bilibili](https://space.bilibili.com/13166598)
- 🎥 [YouTube](https://www.youtube.com/@ttggs)

💬 **加入 Hummingbot 中文社区**
📩 **社区管理员微信 (WeChat)：**
- @amtf202004

🔗 **Discord 交流群**
- [加入 Discord](https://discord.com/invite/TPd7YXzw6D)

🔗 **QQ群**
- 714030802

# 目录
- [介绍](#介绍)
- [安装](#安装) 
- [原理](#原理) 
- [策略](#策略)
- [挖矿](#挖矿) 
- [技巧](#技巧)
- [开发](#开发)
- [问答](#问答)
- [社区](#社区)
- [致谢](#致谢)

## 介绍

>Hummingbot是一个**开源且免费**的数字货币量化策略交易软件，是让任何人都可以创造和使用高频交易机器人的一款交易工具，用以实现跨交易所或单交易所做市及套利。Hummingbot可以为散户、中小型交易公司或基金提供量化高频交易策略，亦可以为区块链项目发行的数字货币以及交易所本身提供流动性。

- [视频]hummingbot是什么？ ~~[Bilbili](https://www.bilibili.com/video/BV1oX4y1g7Kp/)~~ | [Youtube](https://youtu.be/_Y2aZr9LkXY)

- [文章] 数字货币量化交易机器人的比较 [Zhihu](https://zhuanlan.zhihu.com/p/405182553)
## 安装
- [视频] 快速创建Hummingbot量化交易机器人 ~~[Bilibili](https://www.bilibili.com/video/BV1nB4y1A7nZ/)~~ | [Youtube](https://youtu.be/gLC4wuMUpug)

- [文章] AWS账号注册指南 [Zhihu](https://zhuanlan.zhihu.com/p/421176276)
## 原理
- [视频] 什么是做市？ ~~[Bilbili](https://www.bilibili.com/video/BV1GU4y1L7BH/)~~ | [Youtube](https://youtu.be/OApUCwh0l-M)
- [视频] 如何选择正确的市场进行做市 ~~[Bilibili](https://www.bilibili.com/video/BV1264y1X7GM/)~~ | [Youtube](https://youtu.be/lxVsJcWDDe4)

- [文章] 什么是做市？ [Zhihu](https://zhuanlan.zhihu.com/p/412876608)
- [文章] 什么是套利？ [Zhihu](https://zhuanlan.zhihu.com/p/426858907)
- [文章] 什么是库存风险？ [Zhihu](https://zhuanlan.zhihu.com/p/427984248)
- [文章] 初学者对Hummingbot做市的最大误解 [mirror.xyz](https://mirror.xyz/0x7f2337F8E6bFd7Ce15Ea6c58c917D69Ac8402B1e/uqH-SVwS0BkDIwCODhhGr2rb8DBJwsn8NsK7fLhn4ns) 
## 策略
- [视频] 纯做市策略高级参数指南 ~~[Bilbili](https://www.bilibili.com/video/BV1Vy4y1u7sS/)~~ | [Youtube](https://youtu.be/zV8Wi0CJOlg)
- [视频] 跨交易所做市策略指南 ~~[Bilbili](https://www.bilibili.com/video/BV1fh411q7fP/)~~ | [Youtube](https://youtu.be/sS99DrIyIxA)
- [视频] Avellaneda & Stoikov做市策略指南 ~~[Bilbili](https://www.bilibili.com/video/BV1m64y1b7gS/)~~ | [Youtube](https://youtu.be/5RrHi6dXzME)
- [视频] 对冲策略指南 ~~[Bilbili](https://www.bilibili.com/video/BV1g34y197Pg)~~ | [Youtube](https://youtu.be/Y_nfr0PDnzY)

- [文章] Terra套利指南 [Zhihu](https://zhuanlan.zhihu.com/p/407956989)
- [文章] 跨交易所做市策略 [Zhihu](https://zhuanlan.zhihu.com/p/423357205)
- [文章] 现货-永续合约套利策略指南 [Zhihu](https://zhuanlan.zhihu.com/p/409244837)
- [文章] Avellaneda & Stoikov策略介绍 [Zhihu](https://zhuanlan.zhihu.com/p/399924066)
- [文章] 阿隆(Aroon)指标策略指南 [Zhihu](https://zhuanlan.zhihu.com/p/434971567)

## 挖矿
- [视频]流动性挖矿--理论篇 ~~[Bilbili](https://www.bilibili.com/video/BV1yK4y1P7SJ/)~~  | [Youtube](https://youtu.be/mswTft93_i0)
- [视频]流动性挖矿--实践篇 ~~[Bilbili](https://www.bilibili.com/video/BV1L5411u71y/)~~  | [Youtube](https://youtu.be/jYmHVI1lm_g) 
- [视频] 顶峰(AscendEX)交易所流动性挖矿入门指南 ~~[Bilibili](https://www.bilibili.com/video/BV1Dy4y137ow/)~~ | [Youtube](https://youtu.be/9My6J75WTjg)

- [文章]流动性挖矿的比较hummingbot vs. Defi(一) [Zhihu](https://zhuanlan.zhihu.com/p/402304253) 
- [文章]流动性挖矿的比较hummingbot vs. Defi(二) [Zhihu](https://zhuanlan.zhihu.com/p/404672369) 
- [文章]成功矿工的共同特征 [Zhihu](https://zhuanlan.zhihu.com/p/475828359) | [mirror.xyz](https://mirror.xyz/0x7f2337F8E6bFd7Ce15Ea6c58c917D69Ac8402B1e/uqH-SVwS0BkDIwCODhhGr2rb8DBJwsn8NsK7fLhn4ns)
- [文章] 最大化 Hummingbot 流动性挖矿收益的建议 [Zhihu](https://zhuanlan.zhihu.com/p/487238376) 
## 技巧
- [视频] DYDX交易所使用指南 [Youtube](https://youtu.be/c4guWkUC_5Y)
- [文章] 如何使用Telegram管理Hummingbot [Zhihu](https://zhuanlan.zhihu.com/p/410034371) 
## 开发
- [视频] 脚本(Script)功能使用指南 ~~[Bilbili](https://www.bilibili.com/video/BV1nM4y1G7Av/)~~ | [Youtube](https://youtu.be/0Y27_gMLt1w)


## 问答
- [常见问题解答](FAQ.md) 

## 致谢
感谢以下社区内容贡献者：

[syuukawa](https://github.com/syuukawa)

[yingdan](https://github.com/moraliang)

[dolm](https://github.com/whoareyou40)


==================================================
