# ⚡ [QUANT-SOURCE-204] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_204_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: hftbacktest (`PHASE4-QUANT-032`)
- **Full Name**: `PHASE4-QUANT-032_nkaz001__hftbacktest`
- **Description**: Free, open source, a high frequency trading and market making backtesting and trading bot, which accounts for limit orders, queue positions, and latencies, utilizing full tick data for trades and order books(Level-2 and Level-3), with real-world crypto trading examples for Binance and Bybit
- **GitHub Stars**: 4697
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
===========
HftBacktest
===========

|codeql| |python| |pypi| |downloads| |rustc| |crates| |license| |docs| |roadmap| |github|

High-Frequency Trading Backtesting Tool
=======================================

This framework is designed for developing high frequency trading and market making strategies. It focuses on accounting for both feed and order latencies, as well as the order queue position for order fill simulation. The framework aims to provide more accurate market replay-based backtesting, based on full order book and trade tick feed data.

Key Features
============

* Working in `Numba <https://numba.pydata.org/>`_ JIT function (Python).
* Complete tick-by-tick simulation with a customizable time interval or based on the feed and order receipt.
* Full order book reconstruction based on Level-2 Market-By-Price and Level-3 Market-By-Order feeds.
* Backtest accounting for both feed and order latency, using provided models or your own custom model.
* Order fill simulation that takes into account the order queue position, using provided models or your own custom model.
* Backtesting of multi-asset and multi-exchange models
* Deployment of a live trading bot for quick prototyping and testing using the same algorithm code: currently for Binance Futures and Bybit. (Rust-only)

Documentation
=============

See `full document here <https://hftbacktest.readthedocs.io/>`_.

Tutorials you’ll likely find interesting:

* `High-Frequency Grid Trading - Simplified from GLFT <https://hftbacktest.readthedocs.io/en/latest/tutorials/High-Frequency%20Grid%20Trading%20-%20Simplified%20from%20GLFT.html>`_
* `Market Making with Alpha - Order Book Imbalance <https://hftbacktest.readthedocs.io/en/latest/tutorials/Market%20Making%20with%20Alpha%20-%20Order%20Book%20Imbalance.html>`_
* `Market Making with Alpha - APT <https://hftbacktest.readthedocs.io/en/latest/tutorials/Market%20Making%20with%20Alpha%20-%20APT.html>`_
* `Accelerated Backtesting <https://hftbacktest.readthedocs.io/en/latest/tutorials/Accelerated%20Backtesting.html>`_
* `Pricing Framework <https://hftbacktest.readthedocs.io/en/latest/tutorials/Pricing%20Framework.html>`_

Why Accurate Backtesting Matters — Not Just Conservative Approach
=================================================================

Trading is a highly competitive field where only the small edges usually exist, but they can still make a significant
difference. Because of this, backtesting must accurately simulate real-world conditions.: It should neither rely on an
overly pessimistic approach that hides these small edges and profit opportunities, nor on an overly optimistic one that
overstates them through unrealistic simulation. Or at the very least, you should clearly understand what differs from
live trading and by how much, since sometimes fully accurate backtesting is not practical due to the time it requires.

This is not about overfitting at the start—before you even consider issues like overfitting, you need confidence that
your backtesting truly reflects real-world execution. For example, if you run a live trading strategy in January 2025,
the backtest for that exact period should produce results that closely align with the actual results. Once you’ve
validated that your backtesting can accurately reproduce live trading results, then you can proceed to deeper research,
optimization, and considerations around overfitting.

Accurate backtesting is the foundation. Without it, all further analysis—whether conservative or aggressive—becomes
unreliable.

Getting started
===============

Installation
------------

hftbacktest supports Python 3.11+. You can install hftbacktest using ``pip``:

.. code-block:: console

 pip install hftbacktest

Or you can clone the latest development version from the Git repository with:

.. code-block:: console

 git clone https://github.com/nkaz001/hftbacktest

Data Source & Format
--------------------

Please see `Data <https://hftbacktest.readthedocs.io/en/latest/data.html>`_ or `Data Preparation <https://hftbacktest.readthedocs.io/en/latest/tutorials/Data%20Preparation.html>`_.

You can also find some data `here <https://reach.stratosphere.capital/data/usdm/>`_, hosted by the supporter.

A Quick Example
---------------

Get a glimpse of what backtesting with hftbacktest looks like with these code snippets:

.. code-block:: python

    @njit
    def market_making_algo(hbt):
        asset_no = 0
        tick_size = hbt.depth(asset_no).tick_size
        lot_size = hbt.depth(asset_no).lot_size

        # in nanoseconds
        while hbt.elapse(10_000_000) == 0:
            hbt.clear_inactive_orders(asset_no)

            a = 1
            b = 1
            c = 1
            hs = 1

            # Alpha, it can be a combination of several indicators.
            forecast = 0
            # In HFT, it can be various measurements of short-term market movements,
            # such as the high-low range in the last X minutes.
            volatility = 0
            # Delta risk, it can be a combination of several risks.
            position = hbt.position(asset_no)
            risk = (c + volatility) * position
            half_spread = (c + volatility) * hs

            max_notional_position = 1000
            notional_qty = 100

            depth = hbt.depth(asset_no)

            mid_price = (depth.best_bid + depth.best_ask) / 2.0

            # fair value pricing = mid_price + a * forecast
            #                      or underlying(correlated asset) + adjustment(basis + cost + etc) + a * forecast
            # risk skewing = -b * risk
            reservation_price = mid_price + a * forecast - b * risk
            new_bid = reservation_price - half_spread
            new_ask = reservation_price + half_spread

            new_bid_tick = min(np.round(new_bid / tick_size), depth.best_bid_tick)
            new_ask_tick = max(np.round(new_ask / tick_size), depth.best_ask_tick)

            order_qty = np.round(notional_qty / mid_price / lot_size) * lot_size

            # Elapses a process time.
            if not hbt.elapse(1_000_000) != 0:
                return False

            last_order_id = -1
            update_bid = True
            update_ask = True
            buy_limit_exceeded = position * mid_price > max_notional_position
            sell_limit_exceeded = position * mid_price < -max_notional_position
            orders = hbt.orders(asset_no)
            order_values = orders.values()
            while order_values.has_next():
                order = order_values.get()
                if order.side == BUY:
                    if order.price_tick == new_bid_tick or buy_limit_exceeded:
                        update_bid = False
                    if order.cancellable and (update_bid or buy_limit_exceeded):
                        hbt.cancel(asset_no, order.order_id, False)
                        last_order_id = order.order_id
                elif order.side == SELL:
                    if order.price_tick == new_ask_tick or sell_limit_exceeded:
                        update_ask = False
                    if order.cancellable and (update_ask or sell_limit_exceeded):
                        hbt.cancel(asset_no, order.order_id, False)
                        last_order_id = order.order_id

            # It can be combined with a grid trading strategy by submitting multiple orders to capture better spreads and
            # have queue position.
            # This approach requires more sophisticated logic to efficiently manage resting orders in the order book.
            if update_bid:
                # There is only one order at a given price, with new_bid_tick used as the order ID.
                order_id = new_bid_tick
                hbt.submit_buy_order(asset_no, order_id, new_bid_tick * tick_size, order_qty, GTX, LIMIT, False)
                last_order_id = order_id
            if update_ask:
                # There is only one order at a given price, with new_ask_tick used as the order ID.
                order_id = new_ask_tick
                hbt.submit_sell_order(asset_no, order_id, new_ask_tick * tick_size, order_qty, GTX, LIMIT, False)
                last_order_id = order_id

            # All order requests are considered to be requested at the same time.
            # Waits until one of the order responses is received.
            if last_order_id >= 0:
                # Waits for the order response for a maximum of 5 seconds.
                timeout = 5_000_000_000
                if not hbt.wait_order_response(asset_no, last_order_id, timeout):
                    return False

        return True


Tutorials
=========
* `Data Preparation <https://hftbacktest.readthedocs.io/en/latest/tutorials/Data%20Preparation.html>`_
* `Getting Started <https://hftbacktest.readthedocs.io/en/latest/tutorials/Getting%20Started.html>`_
* `Working with Market Depth and Trades <https://hftbacktest.readthedocs.io/en/latest/tutorials/Working%20with%20Market%20Depth%20and%20Trades.html>`_
* `Integrating Custom Data <https://hftbacktest.readthedocs.io/en/latest/tutorials/Integrating%20Custom%20Data.html>`_
* `Making Multiple Markets - Introduction <https://hftbacktest.readthedocs.io/en/latest/tutorials/Making%20Multiple%20Markets%20-%20Introduction.html>`_
* `High-Frequency Grid Trading <https://hftbacktest.readthedocs.io/en/latest/tutorials/High-Frequency%20Grid%20Trading.html>`_
* `High-Frequency Grid Trading - Comparison Across Other Exchanges <https://hftbacktest.readthedocs.io/en/latest/tutorials/High-Frequency%20Grid%20Trading%20-%20Comparison%20Across%20Other%20Exchanges.html>`_
* `High-Frequency Grid Trading - Simplified from GLFT <https://hftbacktest.readthedocs.io/en/latest/tutorials/High-Frequency%20Grid%20Trading%20-%20Simplified%20from%20GLFT.html>`_
* `Impact of Order Latency <https://hftbacktest.readthedocs.io/en/latest/tutorials/Impact%20of%20Order%20Latency.html>`_
* `Order Latency Data <https://hftbacktest.readthedocs.io/en/latest/tutorials/Order%20Latency%20Data.html>`_
* `Guéant–Lehalle–Fernandez-Tapia Market Making Model and Grid Trading <https://hftbacktest.readthedocs.io/en/latest/tutorials/GLFT%20Market%20Making%20Model%20and%20Grid%20Trading.html>`_
* `Making Multiple Markets <https://hftbacktest.readthedocs.io/en/latest/tutorials/Making%20Multiple%20Markets.html>`_
* `Risk Mitigation through Price Protection in Extreme Market Conditions <https://hftbacktest.readthedocs.io/en/latest/tutorials/Risk%20Mitigation%20through%20Price%20Protection%20in%20Extreme%20Market%20Conditions.html>`_
* `Level-3 Backtesting <https://hftbacktest.readthedocs.io/en/latest/tutorials/Level-3%20Backtesting.html>`_
* `Market Making with Alpha - Order Book Imbalance <https://hftbacktest.readthedocs.io/en/latest/tutorials/Market%20Making%20with%20Alpha%20-%20Order%20Book%20Imbalance.html>`_
* `Market Making with Alpha - Basis <https://hftbacktest.readthedocs.io/en/latest/tutorials/Market%20Making%20with%20Alpha%20-%20Basis.html>`_
* `Market Making with Alpha - APT <https://hftbacktest.readthedocs.io/en/latest/tutorials/Market%20Making%20with%20Alpha%20-%20APT.html>`_
* `Queue-Based Market Making in Large Tick Size Assets <https://hftbacktest.readthedocs.io/en/latest/tutorials/Queue-Based%20Market%20Making%20in%20Large%20Tick%20Size%20Assets.html>`_
* `Fusing Depth Data <https://hftbacktest.readthedocs.io/en/latest/tutorials/Fusing%20Depth%20Data.html>`_
* `Accelerated Backtesting <https://hftbacktest.readthedocs.io/en/latest/tutorials/Accelerated%20Backtesting.html>`_
* `Pricing Framework <https://hftbacktest.readthedocs.io/en/latest/tutorials/Pricing%20Framework.html>`_

Examples
========

You can find more examples in `examples <https://github.com/nkaz001/hftbacktest/tree/master/examples>`_ directory and `Rust examples <https://github.com/nkaz001/hftbacktest/blob/master/hftbacktest/examples/>`_.

The complete process of backtesting Binance Futures
---------------------------------------------------
`high-frequency gridtrading <https://github.com/nkaz001/hftbacktest/blob/master/hftbacktest/examples/gridtrading.ipynb>`_: The complete process of backtesting Binance Futures using a high-frequency grid trading strategy implemented in Rust.

Migration to V2
===============
Please see the `migration guide <https://hftbacktest.readthedocs.io/en/latest/migration2.html>`_.

Roadmap
=======

Please see the `roadmap <https://github.com/nkaz001/hftbacktest/blob/master/ROADMAP.md>`_.

Contributing
============

Thank you for considering contributing to hftbacktest! Welcome any and all help to improve the project. If you have an
idea for an enhancement or a bug fix, please open an issue or discussion on GitHub to discuss it.

The following items are examples of contributions you can make to this project:

Please see the `roadmap <https://github.com/nkaz001/hftbacktest/blob/master/ROADMAP.md>`_.

.. |python| image:: https://shields.io/badge/python-3.11+-blue
    :alt: Python Version
    :target: https://www.python.org/

.. |codeql| image:: https://github.com/nkaz001/hftbacktest/actions/workflows/codeql.yml/badge.svg?branch=master&event=push
    :alt: CodeQL
    :target: https://github.com/nkaz001/hftbacktest/actions/workflows/codeql.yml

.. |pypi| image:: https://badge.fury.io/py/hftbacktest.svg
    :alt: Package Version
    :target: https://pypi.org/project/hftbacktest

.. |downloads| image:: https://static.pepy.tech/badge/hftbacktest
    :alt: Downloads
    :target: https://pepy.tech/project/hftbacktest

.. |crates| image:: https://img.shields.io/crates/v/hftbacktest.svg
    :alt: Rust crates.io version
    :target: https://crates.io/crates/hftbacktest

.. |license| image:: https://img.shields.io/badge/License-MIT-green.svg
    :alt: License
    :target: https://github.com/nkaz001/hftbacktest/blob/master/LICENSE

.. |docs| image:: https://readthedocs.org/projects/hftbacktest/badge/?version=latest
    :target: https://hftbacktest.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |roadmap| image:: https://img.shields.io/badge/Roadmap-gray
    :target: https://github.com/nkaz001/hftbacktest/blob/master/ROADMAP.md
    :alt: Roadmap

.. |github| image:: https://img.shields.io/github/stars/nkaz001/hftbacktest?style=social
    :target: https://github.com/nkaz001/hftbacktest
    :alt: Github

.. |rustc| image:: https://shields.io/badge/rustc-1.90-blue
    :alt: Rust Version
    :target: https://www.rust-lang.org/

### Core Implementation Code & Architecture
#### File: `py-hftbacktest/hftbacktest/data/utils/__init__.py`
```python

```

#### File: `hftbacktest/src/prelude.rs`
```python
pub use crate::{depth::*, types::*, utils::*};
```

#### File: `.cargo/config.toml`
```python
[target.aarch64-apple-darwin]
rustflags = [
  "-C", "link-arg=-undefined",
  "-C", "link-arg=dynamic_lookup",
]
```

#### File: `rustfmt.toml`
```python
imports_layout = "HorizontalVertical"
imports_granularity = "Crate"
group_imports = "StdExternalCrate"
newline_style = "Unix"
```

#### File: `py-hftbacktest/rustfmt.toml`
```python
imports_layout = "HorizontalVertical"
imports_granularity = "Crate"
group_imports = "StdExternalCrate"
newline_style = "Unix"
match_block_trailing_comma = true
```

#### File: `collector/src/error.rs`
```python
use thiserror::Error;

#[derive(Error, Debug)]
pub enum ConnectorError {
    #[error("SerdeError: {0}")]
    SerdeError(#[from] serde_json::Error),
    #[error("format error")]
    FormatError,
    #[error("connection abort")]
    ConnectionAbort,
}
```


==================================================


## [2/3] Repository: HFT-Orderbook (`PHASE4-QUANT-024`)
- **Full Name**: `PHASE4-QUANT-024_Crypto-toolbox__HFT-Orderbook`
- **Description**: Limit Order Book for high-frequency trading (HFT), as described by WK Selph, implemented in Python3 and C
- **GitHub Stars**: 1387
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# HFT-Orderbook
Limit Order Book for high-frequency trading (HFT), as described by WK Selph, implemented in C.

Based on WK Selph's Blogpost:

http://howtohft.wordpress.com/2011/02/15/how-to-build-a-fast-limit-order-book/

Available at Archive.org's WayBackMachine:

https://goo.gl/KF1SRm


    "There are three main operations that a limit order book (LOB) has to
    implement: add, cancel, and execute.  The goal is to implement these
    operations in O(1) time while making it possible for the trading model to
    efficiently ask questions like “what are the best bid and offer?”, “how much
    volume is there between prices A and B?” or “what is order X’s current
    position in the book?”.

    The vast majority of the activity in a book is usually made up of add and
    cancel operations as market makers jockey for position, with executions a
    distant third (in fact I would argue that the bulk of the useful information
    on many stocks, particularly in the morning, is in the pattern of adds and
    cancels, not executions, but that is a topic for another post).  An add
    operation places an order at the end of a list of orders to be executed at
    a particular limit price, a cancel operation removes an order from anywhere
    in the book, and an execution removes an order from the inside of the book
    (the inside of the book is defined as the oldest buy order at the highest
    buying price and the oldest sell order at the lowest selling price).  Each
    of these operations is keyed off an id number (Order.idNumber in the
    pseudo-code below), making a hash table a natural structure for tracking
    them.

    Depending on the expected sparsity of the book (sparsity being the
    average distance in cents between limits that have volume, which is
    generally positively correlated with the instrument price), there are a
    number of slightly different implementations I’ve used.  First it will help
    to define a few objects:

        Order
          int idNumber;
          bool buyOrSell;
          int shares; // order size
          int limit;
          int entryTime;
          int eventTime;
          Order *nextOrder;
          Order *prevOrder;
          Limit *parentLimit;

        Limit  // representing a single limit price
          int limitPrice;
          int size;
          int totalVolume;
          Limit *parent;
          Limit *leftChild;
          Limit *rightChild;
          Order *headOrder;
          Order *tailOrder;

        Book
          Limit *buyTree;
          Limit *sellTree;
          Limit *lowestSell;
          Limit *highestBuy;

    The idea is to have a binary tree of Limit objects sorted by limitPrice,
    each of which is itself a doubly linked list of Order objects.  Each side
    of the book, the buy Limits and the sell Limits, should be in separate trees
    so that the inside of the book corresponds to the end and beginning of the
    buy Limit tree and sell Limit tree, respectively.  Each order is also an
    entry in a map keyed off idNumber, and each Limit is also an entry in a
    map keyed off limitPrice.

    With this structure you can easily implement these key operations with
    good performance:

    Add – O(log M) for the first order at a limit, O(1) for all others
    Cancel – O(1)
    Execute – O(1)
    GetVolumeAtLimit – O(1)
    GetBestBid/Offer – O(1)

    where M is the number of price Limits (generally << N the number of orders).
    Some strategy for keeping the limit tree balanced should be used because the
    nature of markets is such that orders will be being removed from one side
    of the tree as they’re being added to the other.  Keep in mind, though,
    that it is important to be able to update Book.lowestSell/highestBuy
    in O(1) time when a limit is deleted (which is why each Limit has a Limit
    *parent) so that GetBestBid/Offer can remain O(1)."

### Core Implementation Code & Architecture
#### File: `orderbook_tests.py`
```python
# Import Built-Ins
import logging
from unittest import TestCase

# Import Third-Party

# Import Homebrew
from lob import LimitOrderBook, Order

# Init Logging Facilities
log = logging.getLogger(__name__)


class OrderTests(TestCase):

    def test_adding_a_new_order_works(self):
        lob = LimitOrderBook()
        bid_order = Order(uid=1, is_bid=True, size=5, price=100)
        ask_order = Order(uid=2, is_bid=False, size=5, price=200)
        lob.process(bid_order)
        lob.process(ask_order)
        self.assertEqual(lob.best_ask.price, 200)
        self.assertEqual(lob.best_bid.price, 100)
        self.assertEqual(lob.best_bid.volume, 500)

        # Assert that the best bid (bid_order) has no previous and no next item,
        # since it is the only one in the book on the bid size at the moment.
        self.assertEqual(len(lob.best_bid), 1)
        self.assertEqual(len(lob.best_ask), 1)
        self.assertIsNone(bid_order.next_item)
        self.assertIsNone(bid_order.previous_item)
        self.assertEqual(lob.best_bid.orders.head, bid_order)
        self.assertEqual(lob.best_ask.orders.head, ask_order)
        self.assertIn(1, lob._orders)

        # Assert that updating an order works
        updated_bid_order = Order(uid=1, is_bid=True, size=4, price=100, timestamp=bid_order.timestamp)
        lob.process(updated_bid_order)
        self.assertEqual(lob.best_bid.orders.head.size, 4)
        self.assertEqual(lob.best_bid.volume, 400)

        updated_ask_order = Order(uid=2, is_bid=True, size=4, price=200, timestamp=ask_order.timestamp)
        lob.process(updated_ask_order)
        self.assertEqual(lob.best_ask.orders.head.size, 4)
        self.assertEqual(lob.best_ask.volume, 800)

        # Assert that adding an additional order to a limit level updates the
        # doubly linked list correctly
        bid_order_2 = Order(uid=3, is_bid=True, size=5, price=100)
        lob.process(bid_order_2)
        self.assertEqual(lob.best_bid.orders.head.next_item, bid_order_2)
        self.assertEqual(lob.best_bid.orders.tail, bid_order_2)
        self.assertEqual(len(lob.best_bid), 2)
        
    def test_removing_orders_works(self):
        lob = LimitOrderBook()
        bid_order = Order(uid=1, is_bid=True, size=5, price=100)
        bid_order_2 = Order(uid=2, is_bid=True, size=10, price=100)
        ask_order = Order(uid=3, is_bid=False, size=10, price=200)
        ask_order_2 = Order(uid=4, is_bid=False, size=10, price=200)
        lob.process(bid_order)
        lob.process(bid_order_2)
        lob.process(ask_order)
        lob.process(ask_order_2)

        # Assert that removing an order from a limit level with several
        # orders resets the tail, head and previous / next items accordingly
        removed_bid_order = Order(uid=1, is_bid=True, size=0, price=100)
        self.assertEqual(len(lob.best_bid), 2)
        self.assertEqual(lob.best_bid.orders.head, bid_order)
        self.assertEqual(lob.best_bid.orders.tail, bid_order_2)
        lob.process(removed_bid_order)
        self.assertEqual(len(lob.best_bid), 1)
        self.assertEqual(lob.best_bid.orders.head, bid_order_2)
        self.assertEqual(lob.best_bid.orders.tail, bid_order_2)
        self.assertIsNone(lob.best_bid.orders.head.next_item)
        self.assertIsNone(lob.best_bid.orders.head.previous_item)
        self.assertNotIn(removed_bid_order.uid, lob._orders)
        self.assertIn(removed_bid_order.price, lob._price_levels)

        # Assert that removing the last Order in a price level removes its
        # limit Level accordingly
        removed_bid_order_2 = Order(uid=2, is_bid=True, size=0, price=100)
        lob.process(removed_bid_order_2)
        self.assertIsNone(lob.best_bid)

        self.assertNotIn(removed_bid_order_2.uid, lob._orders)
        self.assertNotIn(removed_bid_order_2.price, lob._price_levels)
    
    def load_book(self, lob):
        orders = [
            Order(uid=1, is_bid=True, size=5, price=100),
            Order(uid=2, is_bid=True, size=5, price=95),
            Order(uid=3, is_bid=True, size=5, price=90),
            Order(uid=4, is_bid=False, size=5, price=200),
            Order(uid=5, is_bid=False, size=5, price=205),
            Order(uid=6, is_bid=False, size=5, price=210),
            ]
        for order in orders:
             lob.process(order)
    
    def check_levels_format(self, levels):
        self.assertIsInstance(levels, dict)
        for side in ('bids', 'asks'):
            self.assertIsInstance(levels[side], list)
            for i, price_level in enumerate(levels[side]):
                price = price_level.price
                last_price = price if i < 1 else levels[side][i - 1].price
                if side == 'bids':
                    self.assertTrue(price <= last_price)
                else:
                    self.assertTrue(price >= last_price)
        
    def test_querying_levels_works(self):
        lob = LimitOrderBook()
        self.load_book(lob)
        levels = lob.levels()
        self.check_levels_format(levels)
    
    def test_querying_levels_limit_depth(self):
        lob = LimitOrderBook()
        self.load_book(lob)
        levels = lob.levels(depth=2)
        self.check_levels_format(levels)
        for side in ('bids', 'asks'):
            self.assertEqual(len(levels[side]), 2)
```

#### File: `lob.py`
```python
"""
MIT License

Copyright (c) 2017 Nils Diefenbach

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

--------------------------------------------------------------------------------

HFT-Orderbook

Limit Order Book for high-frequency trading (HFT), as described by WK Selph,
implemented in Python3.

Based on WK Selph's Blogpost:
http://howtohft.wordpress.com/2011/02/15/how-to-build-a-fast-limit-order-book/

Available at Archive.org's WayBackMachine:
(https://goo.gl/KF1SRm)


    "There are three main operations that a limit order book (LOB) has to
    implement: add, cancel, and execute.  The goal is to implement these
    operations in O(1) time while making it possible for the trading model to
    efficiently ask questions like “what are the best bid and offer?”, “how much
    volume is there between prices A and B?” or “what is order X’s current
    position in the book?”.

    The vast majority of the activity in a book is usually made up of add and
    cancel operations as market makers jockey for position, with executions a
    distant third (in fact I would argue that the bulk of the useful information
    on many stocks, particularly in the morning, is in the pattern of adds and
    cancels, not executions, but that is a topic for another post).  An add
    operation places an order at the end of a list of orders to be executed at
    a particular limit price, a cancel operation removes an order from anywhere
    in the book, and an execution removes an order from the inside of the book
    (the inside of the book is defined as the oldest buy order at the highest
    buying price and the oldest sell order at the lowest selling price).  Each
    of these operations is keyed off an id number (Order.idNumber in the
    pseudo-code below), making a hash table a natural structure for tracking
    them.

    Depending on the expected sparsity of the book (sparsity being the
    average distance in cents between limits that have volume, which is
    generally positively correlated with the instrument price), there are a
    number of slightly different implementations I’ve used.  First it will help
    to define a few objects:

        Order
          int idNumber;
          bool buyOrSell;
          int shares; // order size
          int limit;
          int entryTime;
          int eventTime;
          Order *nextOrder;
          Order *prevOrder;
          Limit *parentLimit;

        Limit  // representing a single limit price
          int limitPrice;
          int size;
          int totalVolume;
          Limit *parent;
          Limit *leftChild;
          Limit *rightChild;
          Order *headOrder;
          Order *tailOrder;

        Book
          Limit *buyTree;
          Limit *sellTree;
          Limit *lowestSell;
          Limit *highestBuy;

    The idea is to have a binary tree of Limit objects sorted by limitPrice,
    each of which is itself a doubly linked list of Order objects.  Each side
    of the book, the buy Limits and the sell Limits, should be in separate trees
    so that the inside of the book corresponds to the end and beginning of the
    buy Limit tree and sell Limit tree, respectively.  Each order is also an
    entry in a map keyed off idNumber, and each Limit is also an entry in a
    map keyed off limitPrice.

    With this structure you can easily implement these key operations with
    good performance:

    Add – O(log M) for the first order at a limit, O(1) for all others
    Cancel – O(1)
    Execute – O(1)
    GetVolumeAtLimit – O(1)
    GetBestBid/Offer – O(1)

    where M is the number of price Limits (generally << N the number of orders).
    Some strategy for keeping the limit tree balanced should be used because the
    nature of markets is such that orders will be being removed from one side
    of the tree as they’re being added to the other.  Keep in mind, though,
    that it is important to be able to update Book.lowestSell/highestBuy
    in O(1) time when a limit is deleted (which is why each Limit has a Limit
    *parent) so that GetBestBid/Offer can remain O(1)."

"""

# Import Built-Ins
import logging
import time
from itertools import islice
# Import Third-Party

# Import Homebrew


# Init Logging Facilities
log = logging.getLogger(__name__)


class LimitOrderBook:
    """Limit Order Book (LOB) implementation for High Frequency Trading

    Implementation as described by WK Selph (see header doc string for link).

    """
    def __init__(self):
        self.bids = LimitLevelTree()
        self.asks = LimitLevelTree()
        self.best_bid = None
        self.best_ask = None
        self._price_levels = {}
        self._orders = {}

    @property
    def top_level(self):
        """Returns the best available bid and ask.

        :return:
        """
        return self.best_bid, self.best_ask

    def process(self, order):
        """Processes the given order.

        If the order's size is 0, it is removed from the book.

        If its size isn't zero and it exists within the book, the order is updated.

        If it doesn't exist, it will be added.

        :param order:
        :return:
        """
        if order.size == 0:
            self.remove(order)
        else:
            try:
                self.update(order)
            except KeyError:
                self.add(order)

    def update(self, order):
        """Updates an existing order in the book.

        It also updates the order's related LimitLevel's size, accordingly.

        :param order:
        :return:
        """
        size_diff = self._orders[order.uid].size - order.size
        self._orders[order.uid].size = order.size
        self._orders[order.uid].parent_limit.size -= size_diff

    def remove(self, order):
        """Removes an order from the book.

        If the Limit Level is then empty, it is also removed from the book's
        relevant tree.

        If the removed LimitLevel was either the top bid or ask, it is replaced
        by the next best value (which is the LimitLevel's parent in an
        AVL tree).

        :param order:
        :return:
        """
        # Remove Order from self._orders
        try:
            popped_item = self._orders.pop(order.uid)
        except KeyError:
            return False

        # Remove order from its doubly linked list
        popped_item.pop_from_list()

        # Remove Limit Level from self._price_levels and tree, if no orders are
        # left within that limit level
        try:
            if len(self._price_levels[popped_item.price]) == 0:
                popped_limit_level = self._price_levels.pop(popped_item.price)
                # Remove Limit Level from LimitLevelTree
                if popped_item.is_bid:
                    if popped_limit_level == self.best_bid:
                        if not isinstance(popped_limit_level.parent, LimitLevelTree):
                            self.best_bid = popped_limit_level.parent
                        else:
                            self.best_bid = None

                    popped_limit_level.remove()
                else:
                    if popped_limit_level == self.best_ask:
                        if not isinstance(popped_limit_level.parent, LimitLevelTree):
                            self.best_ask = popped_limit_level.parent
                        else:
                            self.best_ask = None
                    popped_limit_level.remove()
        except KeyError:
            pass

        return popped_item

    def add(self, order):
        """Adds a new LimitLevel to the book and appends the given order to it.

        :param order: Order() Instance
        :return:
        """

        if order.price not in self._price_levels:
            limit_level = LimitLevel(order)
            self._orders[order.uid] = order
            self._price_levels[limit_level.price] = limit_level

            if order.is_bid:
                self.bids.insert(limit_level)
                if self.best_bid is None or limit_level.price > self.best_bid.price:
                    self.best_bid = limit_level

            else:
                self.asks.insert(limit_level)
                if self.best_ask is None or limit_level.price < self.best_ask.price:
                    self.best_ask = limit_level
        else:
            # The price level already exists, hence we need to append the order
            # to that price level
            self._orders[order.uid] = order
            self._price_levels[order.price].append(order)
    
    
    def levels(self, depth=None):
        """Returns the price levels as a dict {'bids': [bid1, ...], 'asks': [ask1, ...]}
        
        :param depth: Desired number of levels on each side to return.
        :return:
        """
        levels_sorted = sorted(self._price_levels.keys())
        bids_all = reversed([price_level for price_level in levels_sorted if price_level < self.best_ask.price])
        bids = list(islice(bids_all, depth)) if depth else list(bids_all)
        asks_all = (price_level for price_level in levels_sorted if price_level > self.best_bid.price)
        asks = list(islice(asks_all, depth)) if depth else list(asks_all)
        levels_dict = {
            'bids' : [self._price_levels[price] for price in bids],
            'asks' : [self._price_levels[price] for price in asks],
            }
        return levels_dict

class LimitLevel:
    """AVL BST node.

    This Binary Tree implementation balances on each insert.

    If performance is of concern to you, implementing a bulk-balance
    method may be of interest (c-based implementations aside).

    Attributes:
        parent: Parent node of this Node
        is_root: Boolean, to determine if this Node is root
        left_child: Left child of this Node; Values smaller than price
        right_child: Right child of this Node; Values greater than price

    Properties:
        height: Height of this Node
        balance: Balance factor of this Node
    """
    __slots__ = ['price', 'size', 'parent', 'left_child',
                 'right_child', 'head', 'tail', 'count', 'orders']

    def __init__(self, order):
        """Initialize a Node() instance.

        :param order:
        """
        # Data Values
        self.price = order.price
        self.size = order.size

        # BST Attributes
        self.parent = None
        self.left_child = None
        self.right_child = None

        # Doubly-Linked-list attributes
        self.orders = OrderList(self)
        self.append(order)

    @property
    def is_root(self):
        return isinstance(self.parent, LimitLevelTree)

    @property
    def volume(self):
        return self.price * self.size

    @property
    def balance_factor(self):
        """Calculate and return the balance of this Node.

        Calculate balance by dividing the right child's height from
        the left child's height. Children which evaluate to False (None)
        are treated as zeros.
        :return:
        """
        right_height = self.right_child.height if self.right_child else 0
        left_height = self.left_child.height if self.left_child else 0

        return right_height - left_height

    @property
    def grandpa(self):
        try:
            if self.parent:
                return self.parent.parent
            else:
                return None
        except AttributeError:
            return None

    @property
    def height(self):
        """Calculates the height of the tree up to this Node.

        :return: int, max height among children.
        """
        left_height = self.left_child.height if self.left_child else 0
        right_height = self.right_child.height if self.right_child else 0
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    @property
    def min(self):
        """Returns the smallest node under this node.

        :return:
        """
        minimum = self
        while minimum.left_child:
            minimum = minimum.left_child
        return minimum

    def append(self, order):
        """Wrapper function to make appending to Order List simpler.

        :param order: Order() Instance
        :return:
        """
        return self.orders.append(order)

    def _replace_node_in_parent(self, new_value=None):
        """Replaces Node in parent on a delete() call.

        :param new_value: LimitLevel() instance
        :return:
        """
        if not self.is_root:
            if self == self.parent.left_child:
                self.parent.left_child = new_value
            else:
                self.parent.right_child = new_value
        if new_value:
            new_value.parent = self.parent

    def remove(self):
        """Deletes this limit level.

        :return:
        """

        if self.left_child and self.right_child:
            # We have two kids
            succ = self.right_child.min

            # Swap Successor and current node
            self.left_child, succ.left_child = succ.left_child, self.left_child
            self.right_child, succ.right_child = succ.right_child, self.right_child
            self.parent, succ.parent = succ.parent, self.parent
            self.remove()
            self.balance_grandpa()
        elif self.left_child:
            # Only left child
            self._replace_node_in_parent(self.left_child)
        elif self.right_child:
            # Only right child
            self._replace_node_in_parent(self.right_child)
        else:
            # No children
            self._replace_node_in_parent(None)

    def balance_grandpa(self):
        """Checks if our grandparent needs rebalancing.

        :return:
        """
        if self.grandpa and self.grandpa.is_root:
            # If our grandpa is root, we do nothing.
            pass
        elif self.grandpa and not self.grandpa.is_root:
            # Tell the grandpa to check his balance.
            self.grandpa.balance()
       
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [3/3] Repository: crypto-rl (`PHASE4-QUANT-036`)
- **Full Name**: `PHASE4-QUANT-036_sadighian__crypto-rl`
- **Description**: Deep Reinforcement Learning toolkit: record and replay cryptocurrency limit order book data & train a DDQN agent
- **GitHub Stars**: 965
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Deep Reinforcement Learning Toolkit for Cryptocurrencies


**Table of contents:**

1. Purpose
2. Scope
3. Dependencies
4. Project structure
5. Design patterns
6. Getting started
7. Citing this project
8. Appendix 

## 1. Purpose
The purpose of this application is to provide a toolkit to:
 - **Record** full limit order book and trade tick data from two 
 exchanges (**Coinbase Pro** and **Bitfinex**) into an [Arctic](https://github.com/manahl/arctic) 
 Tickstore database (i.e., MongoDB), 
 - **Replay** recorded historical data to derive feature sets for training
 - **Train** an agent to trade cryptocurrencies using the DQN algorithm (note: this agent
  implementation is intended to be an example for users to reference)

![High_Level_Overview](./design_patterns/design-pattern-high-level.PNG)


## 2. Scope
- **Research only:** there is no capability for live-trading at exchanges.
- **Reproducing RL paper results:** the dataset used for [this](https://arxiv.org/abs/2004.06985) article is available on [Kaggle Datasets](https://www.kaggle.com/jsadighian/cryptorl).


## 3. Dependencies
See `requirements.txt`

*Note*: to run and train the DQN Agent (`./agent/dqn.py`) tensorflow and Keras-RL
need to be installed manually and are not listed in the `requirements.txt` 
in order to keep this project compatible with other open 
sourced reinforcement learning platforms 
(e.g., [OpenAI Baselines](https://github.com/openai/baselines)).

Pip install the following:

```
git+https://github.com/manahl/arctic.git

Keras==2.2.4
Keras-Applications==1.0.7
Keras-Preprocessing==1.0.9
keras-rl==0.4.2

tensorboard==1.13.1
tensorflow-estimator==1.13.0
tensorflow-gpu==1.13.1
```


## 4. Project Structure
The key elements in this project and brief descriptions.
```
crypto-rl/
	agent/
				...reinforcement learning algorithm implementations
	data_recorder/
				...tools to connect, download, and retrieve limit order book data
	gym_trading/
				...extended openai.gym environment to observe limit order book data
	indicators/
				...technical indicators implemented to be O(1) time complexity
	design-patterns/
				...visual diagrams module architecture
	venv/
				...virtual environment for local deployments
	experiment.py          # Entry point for running reinforcement learning experiments
	recorder.py            # Entry point to start recording limit order book data
	configurations.py      # Constants used throughout this project
	requirements.txt       # List of project dependencies
	setup.py               # Run the command `python3 setup.py install` to 
	                       #    install the extended gym environment i.e., gym_trading.py
```


## 5. Design Patterns
Refer to each individual module for design pattern specifications:

- [Limit Order Book, Data Recorder, and Database](./data_recorder/README.md)
- [Stationary LOB Features](https://arxiv.org/abs/1810.09965v1)
- [POMDP Environment](./gym_trading/README.md)
- [Learning Algorithms and Neural Networks](./agent/README.md)

Sample snapshot of Limit Order Book levels:
![plot_lob_levels](./design_patterns/plot_lob_levels.png)

Sample snapshot of Order Arrival flow metrics:
![plot_order_arrivals](./design_patterns/plot_order_arrivals.png)


## 6. Getting Started

Install the project on your machine:
```
# Clone the project from github
git clone https://github.com/sadighian/crypto-rl.git
cd crypto-rl

# Install a virtual environment for the project's dependencies
python3 -m venv ./venv

# Turn on the virtual environment
source venv/bin/activate

# Install keras-rl dependencies
pip3 install Keras==2.2.4 Keras-Applications==1.0.7 Keras-Preprocessing==1.0.9 keras-rl==0.4.2
 tensorboard==1.13.1 tensorflow-estimator==1.13.0 tensorflow-gpu==1.13.1
 
# Install database
pip3 install git+https://github.com/manahl/arctic.git

# Install the project
pip3 install -e .
```

### 6.1 Record limit order book data from exchanges

**Step 1:**
Go to the `configurations.py` and define the crypto currencies which
you would like to subscribe and record. 

Note: basket list format is as follows `[(Coinbase_Instrument_Name, Bitfinex_Instrument_Name), ...]`
```
SNAPSHOT_RATE = 5  # I.e., every 5 seconds
BASKET = [('BTC-USD', 'tBTCUSD'),
         ('ETH-USD', 'tETHUSD'),
         ('LTC-USD', 'tLTCUSD'),
         ('BCH-USD', 'tBCHUSD'),
         ('ETC-USD', 'tETCUSD')]
RECORD_DATA = True
```

**Step 2:**
Open a CLI/terminal and execute the command to start recording 
full limit order book and trade data.
 ```
 python3 recorder.py
 ```

### 6.2 Replay recorded data to export stationary feature set

**Step 1:**
Ensure that you have data in your database. 

Check with MongoDB shell or [Compass](https://www.mongodb.com/products/compass). 
If you do not have data, see refer to the section above 
**6.1 Record limit order book data from exchanges**.

**Step 2:**
Run a historial data simulation to take snapshots of the
limit order book(s) and export their stationary features
to a compressed csv.

To do this, you can leverage the test cases in `data_recorder/tests/`
or write your own logic. When using the test case methods, make sure
to change the query parameters to match what you've actually recorded and
is in your database.

Example to export features to a compressed csv:
```
python3 data_recorder/tests/test_extract_features.py
```

### 6.3 Train an agent

**Step 1:**
Ensure you have data in the `data_recorder/database/data_exports/` folder.
This is where the agent loads data from. If you do not have data exported
into that folder, see refer to the section above 
**6.2 Replay recorded data to export stationary feature set**.

**Step 2:**
Open a CLI/terminal and start learning/training the agent. 
```
python3 experiment.py --window_size=50 --weights=False --fitting_file=...
```
Refer to `experiment.py` to see all the keyword arguments.


## 7. Citing this project

Please remember to cite this repository if used in your research:
```
    @misc{Crypto-RL,
        author = {Jonathan Sadighian},
        title = {Deep Reinforcement Learning Toolkit for Cryptocurrencies},
        year = {2019},
        publisher = {GitHub},
        journal = {GitHub repository},
        howpublished = {\url{https://github.com/sadighian/crypto-rl}},
    }
```


## 8. Appendix
### 8.1 Branches
There are multiple branches of this project, each with a different implementation pattern 
for persisting data:
 - **FULL** branch is intended to be the foundation for a fully automated trading system 
 (i.e., implementation of design patterns that are ideal for a trading system that requires 
 parallel processing) and persists streaming tick data into an **Arctic Tick Store**
 
 **Note:** the branches below (i.e., lightweight, order book snapshot, mongo integration) 
 are no longer actively maintained as of October 2018, and are here for reference.
 
 - **LIGHT WEIGHT** branch is intended to record streaming data more efficiently than 
 the __full__ branch (i.e., all websocket connections are made from a single process 
 __and__ the limit order book is not maintained) and persists streaming tick data into 
 an **Arctic tick store**
 - **ORDER BOOK SNAPSHOT** branch has the same design pattern as the __full__ branch, 
 but instead of recording streaming ticks, snapshots of the limit order book are taken 
 every **N** seconds and persisted into an **Arctic tick store**
 - **MONGO INTEGRATION** branch is the same implementation as **ORDER BOOK SNAPSHOT**, 
 with the difference being a standard MongoDB is used, rather than Arctic. 
 This branch was originally used to benchmark Arctic's performance and is not up to 
 date with the **FULL** branch.

### 8.2 Assumptions
- You have installed a virtual environment and installed the project to that venv 
(e.g., `pip3 install -e .`)
- You have mongoDB already installed
- You know how to use a cli to start python scripts
- You are running an ubuntu 18+ os

### 8.3 Change Log
- 2021-09-25: Updated `requirements.txt`: going forward the database requires a manual 
  installation via `pip install git+https://github.com/manahl/arctic.git`
- 2019-12-12: Added docstrings and refactored many classes to improve code readability
- 2019-09-18: Refactored `env`s and `broker`s for simplification and
  added different `reward` approaches.
- 2019-09-13: Created and implemented 'order arrival' flow metrics,
  inspired by
  [Multi-Level Order-Flow Imbalance in a Limit Order Book](https://arxiv.org/abs/1907.06230v1)
  by Xu, Ke; Gould, Martin D.; Howison, Sam D.
- 2019-09-06: Created and implemented `Indicator.py` base class
- 2019-04-28: Reorganized project structure for simplicity

### Core Implementation Code & Architecture
#### File: `data_recorder/database/__init__.py`
```python
from . import *
```

#### File: `data_recorder/connector_components/__init__.py`
```python
from . import *
```

#### File: `data_recorder/coinbase_connector/__init__.py`
```python
from . import *
```

#### File: `data_recorder/bitfinex_connector/__init__.py`
```python
from . import *
```

#### File: `agent/__init__.py`
```python
from agent.dqn import DQNAgent
```

#### File: `data_recorder/__init__.py`
```python
from data_recorder.bitfinex_connector import *
from data_recorder.coinbase_connector import *
from data_recorder.database import *
```


==================================================
