# ⚡ [QUANT-SOURCE-210] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_210_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Crypto_Trader (`PHASE4-QUANT-093`)
- **Full Name**: `PHASE4-QUANT-093_bshaw2019__Crypto_Trader`
- **Description**: Q-Learning Based Cryptocurrency Trader and Portfolio Optimizer for the Poloniex Exchange
- **GitHub Stars**: 192
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Crypto_Trader
**A Live Machine-Learning based Cryptocurrency Trader for the Poloniex Exchange**

If you would like to follow our progress or reach out to developers, feel free to join our discord channel at:
https://discord.gg/UPNV2fH

The goal of the project is to create an open sourced, machine learning based cryptocurrency portfolio optimizer including as many relevant variables as possible. 

These will include:

- **Community Sentiment** (such as forum and twitter sentiment analysis)
- **Analyst Opinions** (notable twitter account/analyst feeds with a history of winning strategies - ex. "Haejin" a successful elliot wave trader with an established history)
- **Global Economic Indexes** (DOW, Nikkei225, FOREX data, etc.)
- **Open/Close/High/Low/Volume**
- **Live Orderbook Data** (spread, bid, ask, order size) 
- **Technical Indicators** (MACD's, MA's, VWAPS, etc.)
- **Any Other Variable** of interest found to be important (Please feel free to brainstorm and send suggestions)


A **Boruta Analysis** (variation of Random forest) will be used to reduce these input variables by removing "unimportant" features. 

Using this input dataset, a machine learning **Binary Classifier** will be created to assign trading pairs on Poloniex a confidence score from 0 to 1. This value will represent the confidence that the trading pair will increase over a certain timeframe. Multiple machines may be constructed to score for a 5 minute window, 10 minute, 15 minute, 30 minute, 1 hour, etc. 

Using these scores, a **Q-Learning Bot** ("reinforcement learning") will be created that will optimize a trading strategy based on the binary classifier scores. The machine will read the amount of capital in the users Poloniex Account, and automatically place trades to optimize the portfolios holdings. These strategies will use stop losses and sell limits. Because it is q learning based, the machine will receive, and use live data to make decisions in a live auto-updating context with a reward that optimizes profit. This will allow the machine to continue to train and optimize itself over time while feeding in live data and placing trades.


Ultimately, the program will have the ability to be run 24 hours a day while optimizing a portfolio using live data, while taking into account fees in order to identify and take advantage of all trading opportunities accross the entire cryptocurrency market on Poloniex. Because of the decimal based system of cryptocurrencies, in theory a portfolio of any size should be able to be used as long as the user has the minimum trade size on Poloniex.



| Major Design Features |         Purpose          |
| --------------------- |:------------------------:|
| Identified Variables  | Related to Price Action  |
| Data Scraper          | Live Variables to Array  |
| Binary Classifers     | Score Trading Pairs Live |
| Q-Learning Bot        | Optimize Trade Strategy  |
| Poloniex API Link     | Allow Bot to Make Trades |



If you would like to donate to the project, please do so at the following Bitcoin/Litecoin/Ethereum addresses. All donations appreciated :)

**DONATIONS**

| Currency |                  Address                   |
| -------- |:-----------------------------------------: |
| Bitcoin  |     1GjVgMUDfKHzhxgeauRagVfp1GCrSJXijb     |
| Litecoin | 0x9852389Bd431A90A9AEcb48EdA50Da1ac05Bd4d8 |
| Ethereum |     M9oJaUnCB6Soistk3wSETziFDzz8gAaJCU     |

### Core Implementation Code & Architecture
#### File: `Variable_Functions/__init__.py`
```python

```

#### File: `got3/models/__init__.py`
```python
from .Tweet import Tweet
```

#### File: `got3/__init__.py`
```python
from . import models
from . import manager
```

#### File: `got3/models/Tweet.py`
```python
class Tweet:
	
	def __init__(self):
		pass
```

#### File: `got3/manager/__init__.py`
```python
from .TweetCriteria import TweetCriteria
from .TweetManager import TweetManager
```

#### File: `got3/manager/TweetCriteria.py`
```python
class TweetCriteria:

	def __init__(self):
		self.maxTweets = 0

	def setUsername(self, username):
		self.username = username
		return self

	def setSince(self, since):
		self.since = since
		return self

	def setUntil(self, until):
		self.until = until
		return self

	def setQuerySearch(self, querySearch):
		self.querySearch = querySearch
		return self

	def setMaxTweets(self, maxTweets):
		self.maxTweets = maxTweets
		return self

	def setLang(self, Lang):
		self.lang = Lang
		return self

	def setTopTweets(self, topTweets):
 		self.topTweets = topTweets
 		return self
```


==================================================


## [2/3] Repository: SGX-Full-OrderBook-Tick-Data-Trading-Strategy (`PHASE4-QUANT-109`)
- **Full Name**: `PHASE4-QUANT-109_rorysroes__SGX-Full-OrderBook-Tick-Data-Trading-Strategy`
- **Description**: Providing the solutions for high-frequency trading (HFT) strategies using data science approaches (Machine Learning) on Full Orderbook Tick Data.
- **GitHub Stars**: 2338
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
## Modeling High-Frequency Limit Order Book Dynamics Using Machine Learning 

* Framework to capture the dynamics of high-frequency limit order books.

  <img src="./Graph/pipline.png" width="650">
  
#### Overview

In this project I used machine learning methods to capture the high-frequency limit order book dynamics and simple trading strategy to get the P&L outcomes.

* Feature Extractor

  * Rise Ratio
  
    <img src="./Graph/Price_B1A1.png" width="650">

  * Depth Ratio
  
    <img src="./Graph/depth.png" width="650">
    
    [Note] : [Feature_Selection] (Feature_Selection) 
 
* Learning Model Trainer
  
  *  RandomForestClassifier
  *  ExtraTreesClassifier
  *  AdaBoostClassifier
  *  GradientBoostingClassifier
  *  SVM
  
*  Use best model to predict next 10 seconds

   <img src="./Graph/CV_Best_Model.png" width="650">
   
*  Prediction outcome

   <img src="./Graph/prediction.png" width="650">
   
*  Profit & Loss

   <img src="./Graph/P_L.png" width="650">
   
   [Note] : [Model_Selection] (Model_Selection)


==================================================


## [3/3] Repository: CppTrader (`PHASE4-QUANT-111`)
- **Full Name**: `PHASE4-QUANT-111_chronoxor__CppTrader`
- **Description**: High performance components for building Trading Platform such as ultra fast matching engine, order book processor
- **GitHub Stars**: 1070
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# CppTrader

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/release/chronoxor/CppTrader.svg?sort=semver)](https://github.com/chronoxor/CppTrader/releases)
<br/>
[![Linux (clang)](https://github.com/chronoxor/CppTrader/actions/workflows/build-linux-clang.yml/badge.svg)](https://github.com/chronoxor/CppTrader/actions/workflows/build-linux-clang.yml)
[![Linux (gcc)](https://github.com/chronoxor/CppTrader/actions/workflows/build-linux-gcc.yml/badge.svg)](https://github.com/chronoxor/CppTrader/actions/workflows/build-linux-gcc.yml)
[![MacOS](https://github.com/chronoxor/CppTrader/actions/workflows/build-macos.yml/badge.svg)](https://github.com/chronoxor/CppTrader/actions/workflows/build-macos.yml)
<br/>
[![Windows (Cygwin)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-cygwin.yml/badge.svg)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-cygwin.yml)
[![Windows (MSYS2)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-msys2.yml/badge.svg)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-msys2.yml)
[![Windows (MinGW)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-mingw.yml/badge.svg)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-mingw.yml)
[![Windows (Visual Studio)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-vs.yml/badge.svg)](https://github.com/chronoxor/CppTrader/actions/workflows/build-windows-vs.yml)

C++ Trader is a set of components for building high performance Trading Platform:
* Ultra fast matching engine
* Order book processor
* NASDAQ ITCH handler

[CppTrader API reference](https://chronoxor.github.io/CppTrader/index.html)

# Contents
  * [Features](#features)
  * [Requirements](#requirements)
  * [How to build?](#how-to-build)
  * [Performance](#performance)
    * [NASDAQ ITCH handler](#nasdaq-itch-handler)
    * [Market manager](#market-manager)
    * [Market manager (optimized version)](#market-manager-optimized-version)
    * [Market manager (aggressive optimized version)](#market-manager-aggressive-optimized-version)

# Features
* Cross platform (Linux, MacOS, Windows)
* Benchmarks
* Examples
* Tests
* [Doxygen](http://www.doxygen.org) API documentation
* Continuous integration ([Travis CI](https://travis-ci.com), [AppVeyor](https://www.appveyor.com))

# Requirements
* Linux
* MacOS
* Windows
* [cmake](https://www.cmake.org)
* [gcc](https://gcc.gnu.org)
* [git](https://git-scm.com)
* [gil](https://github.com/chronoxor/gil.git)
* [python3](https://www.python.org)

Optional:
* [clang](https://clang.llvm.org)
* [CLion](https://www.jetbrains.com/clion)
* [Cygwin](https://cygwin.com)
* [MSYS2](https://www.msys2.org)
* [MinGW](https://mingw-w64.org/doku.php)
* [Visual Studio](https://www.visualstudio.com)

# How to build?

### Linux: install required packages
```shell
sudo apt-get install -y binutils-dev uuid-dev
```

### Install [gil (git links) tool](https://github.com/chronoxor/gil)
```shell
pip3 install gil
```

### Setup repository
```shell
git clone https://github.com/chronoxor/CppTrader.git
cd CppTrader
gil update
```

### Linux
```shell
cd build
./unix.sh
```

### MacOS
```shell
cd build
./unix.sh
```

### Windows (Cygwin)
```shell
cd build
unix.bat
```

### Windows (MSYS2)
```shell
cd build
unix.bat
```

### Windows (MinGW)
```shell
cd build
mingw.bat
```

### Windows (Visual Studio)
```shell
cd build
vs.bat
```

# Performance

Here comes several micro-benchmarks for trading components.

Benchmark environment is the following:
```
CPU architecutre: Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz
CPU logical cores: 8
CPU physical cores: 4
CPU clock speed: 3.998 GHz
CPU Hyper-Threading: enabled
RAM total: 31.962 GiB
RAM free: 21.623 GiB

OS version: Microsoft Windows 8 Enterprise Edition (build 9200), 64-bit
OS bits: 64-bit
Process bits: 64-bit
Process configuaraion: release
```

## NASDAQ ITCH handler

Benchmark measures the performance of the [NASDAQ ITCH handler](https://github.com/chronoxor/CppTrader/blob/master/include/trader/providers/nasdaq/itch_handler.h).
It shows how fast it can parse and handle ITCH messages from the input stream.

Sample ITCH file could be downloaded from https://emi.nasdaq.com/ITCH

* [cpptrader-performance-itch_handler](https://github.com/chronoxor/CppTrader/blob/master/performance/itch_handler.cpp) < 01302017.NASDAQ_ITCH50
```
ITCH processing...Done!

Errors: 0

Processing time: 6.831 s
Total ITCH messages: 283238832
ITCH message latency: 24 ns
ITCH message throughput: 41460256 msg/s
```

## Market manager

Benchmark measures the performance of the [Market manager](https://github.com/chronoxor/CppTrader/blob/master/include/trader/matching/market_manager.h ).
It shows how fast it can handle orders operations (add, reduce, modify, delete,
execute) and build an order book.

Sample ITCH file could be downloaded from https://emi.nasdaq.com/ITCH

* [cpptrader-performance-market_manager](https://github.com/chronoxor/CppTrader/blob/master/performance/market_manager.cpp) < 01302017.NASDAQ_ITCH50
```
ITCH processing...Done!

Errors: 0

Processing time: 1:27.616 m
Total ITCH messages: 283238832
ITCH message latency: 309 ns
ITCH message throughput: 3232727 msg/s
Total market updates: 631217516
Market update latency: 138 ns
Market update throughput: 7204359 upd/s

Market statistics:
Max symbols: 8371
Max order books: 8371
Max order book levels: 2422
Max order book orders: 2975
Max orders: 1647972

Order statistics:
Add order operations: 152865456
Update order operations: 7037619
Delete order operations: 152865456
Execute order operations: 5663712
```

## Market manager (optimized version)

This is an optimized version of the Market manager. Optimization tricks are the
following:

* Symbols and order books are stored in fixed size pre-allocated arrays.
* Orders are stored in the pre-allocated array instead of HashMap. This gives
O(1) for all orders operations with no overhead (get, insert, update, delete).
* Orders linked list is not maintained for price levels, just orders count.
* Price levels are stored in sorted arrays instead of Red-Black trees. The sort
order keeps best prices (best bid / best ask) at the end of arrays which gives
good CPU cache locality and near to O(1) search time for orders with close to
market prices, but has a penalty for orders with far from market prices!
* Price levels are taken from the pool, which is implemented using a
pre-allocated array with O(1) for create and delete each price level.

Sample ITCH file could be downloaded from https://emi.nasdaq.com/ITCH

* [cpptrader-performance-market_manager_optimized](https://github.com/chronoxor/CppTrader/blob/master/performance/market_manager_optimized.cpp) < 01302017.NASDAQ_ITCH50
```
ITCH processing...Done!

Errors: 0

Processing time: 34.150 s
Total ITCH messages: 283238832
ITCH message latency: 120 ns
ITCH message throughput: 8293747 msg/s
Total market updates: 631217516
Market update latency: 54 ns
Market update throughput: 18483195 upd/s

Market statistics:
Max symbols: 8371
Max order books: 8371
Max order book levels: 38
Max orders: 1647972

Order statistics:
Add order operations: 152865456
Update order operations: 7037619
Delete order operations: 152865456
Execute order operations: 5663712
```

## Market manager (aggressive optimized version)

This is a very aggressive optimized version of the Market manager. It shows
values of latency and throughput close to optimal with the cost of some more
optimization tricks which might be hard to keep in real trading platforms:

* Symbols are not maintained
* Orders and price limits structures are optimized to be optimal. Most of useful
filds are removed.
* Price values are stored as signed 32-bit integer values. Positive values for
bids and negative values for asks.
* Market handler is not used. No way to receive notifications from the Market
manager.

Sample ITCH file could be downloaded from https://emi.nasdaq.com/ITCH

* [cpptrader-performance-market_manager_optimized_aggressive](https://github.com/chronoxor/CppTrader/blob/master/performance/market_manager_optimized_aggressive.cpp) < 01302017.NASDAQ_ITCH50
```
ITCH processing...Done!

Errors: 0
Processing time: 29.047 s
Total ITCH messages: 283238832
ITCH messages latency: 102 ns
ITCH messages throughput: 9751044 msg/s
```

### Core Implementation Code & Architecture
#### File: `tests/test.cpp`
```python
//
// Created by Ivan Shynkarenka on 26.05.2016
//

#include "test.h"
```

#### File: `examples/itch_handler.cpp`
```python
/*!
    \file itch_handler.cpp
    \brief NASDAQ ITCH handler example
    \author Ivan Shynkarenka
    \date 23.07.2017
    \copyright MIT License
*/

#include "trader/providers/nasdaq/itch_handler.h"

#include "system/stream.h"

#include <iostream>

using namespace CppTrader::ITCH;

class MyITCHHandler : public ITCHHandler
{
protected:
    bool onMessage(const SystemEventMessage& message) override { return OutputMessage(message); }
    bool onMessage(const StockDirectoryMessage& message) override { return OutputMessage(message); }
    bool onMessage(const StockTradingActionMessage& message) override { return OutputMessage(message); }
    bool onMessage(const RegSHOMessage& message) override { return OutputMessage(message); }
    bool onMessage(const MarketParticipantPositionMessage& message) override { return OutputMessage(message); }
    bool onMessage(const MWCBDeclineMessage& message) override { return OutputMessage(message); }
    bool onMessage(const MWCBStatusMessage& message) override { return OutputMessage(message); }
    bool onMessage(const IPOQuotingMessage& message) override { return OutputMessage(message); }
    bool onMessage(const AddOrderMessage& message) override { return OutputMessage(message); }
    bool onMessage(const AddOrderMPIDMessage& message) override { return OutputMessage(message); }
    bool onMessage(const OrderExecutedMessage& message) override { return OutputMessage(message); }
    bool onMessage(const OrderExecutedWithPriceMessage& message) override { return OutputMessage(message); }
    bool onMessage(const OrderCancelMessage& message) override { return OutputMessage(message); }
    bool onMessage(const OrderDeleteMessage& message) override { return OutputMessage(message); }
    bool onMessage(const OrderReplaceMessage& message) override { return OutputMessage(message); }
    bool onMessage(const TradeMessage& message) override { return OutputMessage(message); }
    bool onMessage(const CrossTradeMessage& message) override { return OutputMessage(message); }
    bool onMessage(const BrokenTradeMessage& message) override { return OutputMessage(message); }
    bool onMessage(const NOIIMessage& message) override { return OutputMessage(message); }
    bool onMessage(const RPIIMessage& message) override { return OutputMessage(message); }
    bool onMessage(const LULDAuctionCollarMessage& message) override { return OutputMessage(message); }
    bool onMessage(const UnknownMessage& message) override { return OutputMessage(message); }

private:
    template <class TMessage>
    static bool OutputMessage(const TMessage& message)
    {
        std::cout << message << std::endl;
        return true;
    }
};

int main(int argc, char** argv)
{
    MyITCHHandler itch_handler;

    // Perform input
    size_t size;
    uint8_t buffer[8192];
    CppCommon::StdInput input;
    while ((size = input.Read(buffer, sizeof(buffer))) > 0)
    {
        // Process the buffer
        itch_handler.Process(buffer, size);
    }

    return 0;
}
```

#### File: `tests/test_itch_handler.cpp`
```python
//
// Created by Ivan Shynkarenka on 24.07.2017
//

#include "test.h"

#include "trader/providers/nasdaq/itch_handler.h"

#include "filesystem/file.h"

using namespace CppCommon;
using namespace CppTrader::ITCH;

namespace {

class MyITCHHandler : public ITCHHandler
{
public:
    MyITCHHandler()
        : _messages(0),
          _errors(0)
    {}

    size_t messages() const { return _messages; }
    size_t errors() const { return _errors; }

protected:
    bool onMessage(const SystemEventMessage& message) override { ++_messages; return true; }
    bool onMessage(const StockDirectoryMessage& message) override { ++_messages; return true; }
    bool onMessage(const StockTradingActionMessage& message) override { ++_messages; return true; }
    bool onMessage(const RegSHOMessage& message) override { ++_messages; return true; }
    bool onMessage(const MarketParticipantPositionMessage& message) override { ++_messages; return true; }
    bool onMessage(const MWCBDeclineMessage& message) override { ++_messages; return true; }
    bool onMessage(const MWCBStatusMessage& message) override { ++_messages; return true; }
    bool onMessage(const IPOQuotingMessage& message) override { ++_messages; return true; }
    bool onMessage(const AddOrderMessage& message) override { ++_messages; return true; }
    bool onMessage(const AddOrderMPIDMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderExecutedMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderExecutedWithPriceMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderCancelMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderDeleteMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderReplaceMessage& message) override { ++_messages; return true; }
    bool onMessage(const TradeMessage& message) override { ++_messages; return true; }
    bool onMessage(const CrossTradeMessage& message) override { ++_messages; return true; }
    bool onMessage(const BrokenTradeMessage& message) override { ++_messages; return true; }
    bool onMessage(const NOIIMessage& message) override { ++_messages; return true; }
    bool onMessage(const RPIIMessage& message) override { ++_messages; return true; }
    bool onMessage(const LULDAuctionCollarMessage& message) override { ++_messages; return true; }
    bool onMessage(const UnknownMessage& message) override { ++_errors; return true; }

private:
    size_t _messages;
    size_t _errors;
};

} // namespace

TEST_CASE("ITCHHandler", "[CppTrader][Providers][NASDAQ]")
{
    MyITCHHandler itch_handler;

    // Open the input file
    File input("../../tools/itch/sample.itch");
    if (!input.IsExists())
        input = File("../tools/itch/sample.itch");
    REQUIRE(input.IsExists());
    input.Open(true, false);

    // Perform input
    size_t size;
    uint8_t buffer[8192];
    while ((size = input.Read(buffer, sizeof(buffer))) > 0)
    {
        // Process the buffer
        itch_handler.Process(buffer, size);
    }

    // Check results
    REQUIRE(itch_handler.errors() == 0);
    REQUIRE(itch_handler.messages() == 1563071);
}
```

#### File: `source/trader/matching/order.cpp`
```python
/*!
    \file order.cpp
    \brief Order implementation
    \author Ivan Shynkarenka
    \date 31.07.2017
    \copyright MIT License
*/

#include "trader/matching/order.h"

namespace CppTrader {
namespace Matching {

ErrorCode Order::Validate() const noexcept
{
    // Validate order Id
    assert((Id > 0) && "Order Id must be greater than zero!");
    if (Id == 0)
        return ErrorCode::ORDER_ID_INVALID;

    // Validate order quantity
    assert((Quantity >= LeavesQuantity) && "Order quantity must be greater than or equal to order leaves quantity!");
    if (Quantity < LeavesQuantity)
        return ErrorCode::ORDER_QUANTITY_INVALID;
    assert((LeavesQuantity > 0) && "Order leaves quantity must be greater than zero!");
    if (LeavesQuantity == 0)
        return ErrorCode::ORDER_QUANTITY_INVALID;

    // Validate market order
    if (IsMarket())
    {
        assert((IsIOC() || IsFOK()) && "Market order must have 'Immediate-Or-Cancel' or 'Fill-Or-Kill' parameter!");
        if (!IsIOC() && !IsFOK())
            return ErrorCode::ORDER_PARAMETER_INVALID;
        assert(!IsIceberg() && "Market order cannot be 'Iceberg'!");
        if (IsIceberg())
            return ErrorCode::ORDER_PARAMETER_INVALID;
    }

    // Validate limit order
    if (IsLimit())
    {
        assert(!IsSlippage() && "Limit order cannot have slippage parameter!");
        if (IsSlippage())
            return ErrorCode::ORDER_PARAMETER_INVALID;
    }

    // Validate stop order
    if (IsStop() || IsTrailingStop())
    {
        assert(!IsAON() && "Stop order cannot have 'All-Or-None' parameter!");
        if (IsAON())
            return ErrorCode::ORDER_PARAMETER_INVALID;
        assert(!IsIceberg() && "Stop order cannot be 'Iceberg'!");
        if (IsIceberg())
            return ErrorCode::ORDER_PARAMETER_INVALID;
    }

    // Validate stop-limit order
    if (IsStopLimit() || IsTrailingStopLimit())
    {
        assert(!IsSlippage() && "Stop-limit order cannot have slippage!");
        if (IsSlippage())
            return ErrorCode::ORDER_PARAMETER_INVALID;
    }

    // Validate trailing order
    if (IsTrailingStop() || IsTrailingStopLimit())
    {
        assert((TrailingDistance != 0) && "Trailing stop order must have non zero distance to the market!");
        if (TrailingDistance == 0)
            return ErrorCode::ORDER_PARAMETER_INVALID;

        if (TrailingDistance > 0)
        {
            assert(((TrailingStep >= 0) && (TrailingStep < TrailingDistance)) && "Trailing step must be less than trailing distance!");
            if ((TrailingStep < 0) || (TrailingStep >= TrailingDistance))
                return ErrorCode::ORDER_PARAMETER_INVALID;
        }
        else
        {
            assert(((TrailingDistance <= -1) && (TrailingDistance >= -1000)) && "Trailing percentage distance must be in the range [0.01, 100%] (from -1 down to -10000)!");
            if ((TrailingDistance > -1) || (TrailingDistance < -1000))
                return ErrorCode::ORDER_PARAMETER_INVALID;
            assert(((TrailingStep <= 0) && (TrailingStep > TrailingDistance)) && "Trailing step must be less than trailing distance!");
            if ((TrailingStep > 0) || (TrailingStep <= TrailingDistance))
                return ErrorCode::ORDER_PARAMETER_INVALID;
        }
    }

    return ErrorCode::OK;
}

} // namespace Matching
} // namespace CppTrader
```

#### File: `performance/itch_handler.cpp`
```python
//
// Created by Ivan Shynkarenka on 24.07.2017
//

#include "trader/providers/nasdaq/itch_handler.h"

#include "benchmark/reporter_console.h"
#include "filesystem/file.h"
#include "system/stream.h"
#include "time/timestamp.h"

#include <OptionParser.h>

using namespace CppCommon;
using namespace CppTrader::ITCH;

class MyITCHHandler : public ITCHHandler
{
public:
    MyITCHHandler()
        : _messages(0),
          _errors(0)
    {}

    size_t messages() const { return _messages; }
    size_t errors() const { return _errors; }

protected:
    bool onMessage(const SystemEventMessage& message) override { ++_messages; return true; }
    bool onMessage(const StockDirectoryMessage& message) override { ++_messages; return true; }
    bool onMessage(const StockTradingActionMessage& message) override { ++_messages; return true; }
    bool onMessage(const RegSHOMessage& message) override { ++_messages; return true; }
    bool onMessage(const MarketParticipantPositionMessage& message) override { ++_messages; return true; }
    bool onMessage(const MWCBDeclineMessage& message) override { ++_messages; return true; }
    bool onMessage(const MWCBStatusMessage& message) override { ++_messages; return true; }
    bool onMessage(const IPOQuotingMessage& message) override { ++_messages; return true; }
    bool onMessage(const AddOrderMessage& message) override { ++_messages; return true; }
    bool onMessage(const AddOrderMPIDMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderExecutedMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderExecutedWithPriceMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderCancelMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderDeleteMessage& message) override { ++_messages; return true; }
    bool onMessage(const OrderReplaceMessage& message) override { ++_messages; return true; }
    bool onMessage(const TradeMessage& message) override { ++_messages; return true; }
    bool onMessage(const CrossTradeMessage& message) override { ++_messages; return true; }
    bool onMessage(const BrokenTradeMessage& message) override { ++_messages; return true; }
    bool onMessage(const NOIIMessage& message) override { ++_messages; return true; }
    bool onMessage(const RPIIMessage& message) override { ++_messages; return true; }
    bool onMessage(const LULDAuctionCollarMessage& message) override { ++_messages; return true; }
    bool onMessage(const UnknownMessage& message) override { ++_errors; return true; }

private:
    size_t _messages;
    size_t _errors;
};

int main(int argc, char** argv)
{
    auto parser = optparse::OptionParser().version("1.0.0.0");

    parser.add_option("-i", "--input").dest("input").help("Input file name");

    optparse::Values options = parser.parse_args(argc, argv);

    // Print help
    if (options.get("help"))
    {
        parser.print_help();
        return 0;
    }

    MyITCHHandler itch_handler;

    // Open the input file or stdin
    std::unique_ptr<Reader> input(new StdInput());
    if (options.is_set("input"))
    {
        File* file = new File(Path(options.get("input")));
        file->Open(true, false);
        input.reset(file);
    }

    // Perform input
    size_t size;
    uint8_t buffer[8192];
    std::cout << "ITCH processing...";
    uint64_t timestamp_start = Timestamp::nano();
    while ((size = input->Read(buffer, sizeof(buffer))) > 0)
    {
        // Process the buffer
        itch_handler.Process(buffer, size);
    }
    uint64_t timestamp_stop = Timestamp::nano();
    std::cout << "Done!" << std::endl;

    std::cout << std::endl;

    std::cout << "Errors: " << itch_handler.errors() << std::endl;

    std::cout << std::endl;

    size_t total_messages = itch_handler.messages();

    std::cout << "Processing time: " << CppBenchmark::ReporterConsole::GenerateTimePeriod(timestamp_stop - timestamp_start) << std::endl;
    std::cout << "Total ITCH messages: " << total_messages << std::endl;
    std::cout << "ITCH message latency: " << CppBenchmark::ReporterConsole::GenerateTimePeriod((timestamp_stop - timestamp_start) / total_messages) << std::endl;
    std::cout << "ITCH message throughput: " << total_messages * 1000000000 / (timestamp_stop - timestamp_start) << " msg/s" << std::endl;

    return 0;
}
```

#### File: `examples/market_manager.cpp`
```python
/*!
    \file market_manager.cpp
    \brief Market manager example
    \author Ivan Shynkarenka
    \date 04.08.2017
    \copyright MIT License
*/

#include "trader/matching/market_manager.h"
#include "trader/providers/nasdaq/itch_handler.h"

#include "system/stream.h"

#include <iostream>

using namespace CppTrader::ITCH;
using namespace CppTrader::Matching;

class MyMarketHandler : public MarketHandler
{
protected:
    void onAddSymbol(const Symbol& symbol) override
    { std::cout << "Add symbol: " << symbol << std::endl; }
    void onDeleteSymbol(const Symbol& symbol) override
    { std::cout << "Delete symbol: " << symbol << std::endl; }

    void onAddOrderBook(const OrderBook& order_book) override
    { std::cout << "Add order book: " << order_book << std::endl; }
    void onUpdateOrderBook(const OrderBook& order_book, bool top) override
    { std::cout << "Update order book: " << order_book << (top ? " - Top of the book!" : "") << std::endl; }
    void onDeleteOrderBook(const OrderBook& order_book) override
    { std::cout << "Delete order book: " << order_book << std::endl; }

    void onAddLevel(const OrderBook& order_book, const Level& level, bool top) override
    { std::cout << "Add level: " << level << (top ? " - Top of the book!" : "") << std::endl; }
    void onUpdateLevel(const OrderBook& order_book, const Level& level, bool top) override
    { std::cout << "Update level: " << level << (top ? " - Top of the book!" : "") << std::endl; }
    void onDeleteLevel(const OrderBook& order_book, const Level& level, bool top) override
    { std::cout << "Delete level: " << level << (top ? " - Top of the book!" : "") << std::endl; }

    void onAddOrder(const Order& order) override
    { std::cout << "Add order: " << order << std::endl; }
    void onUpdateOrder(const Order& order) override
    { std::cout << "Update order: " << order << std::endl; }
    void onDeleteOrder(const Order& order) override
    { std::cout << "Delete order: " << order << std::endl; }

    void onExecuteOrder(const Order& order, uint64_t price, uint64_t quantity) override
    { std::cout << "Execute order: " << order << " with price " << price << " and quantity " << quantity << std::endl; }
};

class MyITCHHandler : public ITCHHandler
{
public:
    MyITCHHandler(MarketManager& market) : _market(market) {}

protected:
    bool onMessage(const StockDirectoryMessage& message) override
    {
        Symbol symbol(message.StockLocate, message.Stock);
        _market.AddSymbol(symbol);
        _market.AddOrderBook(symbol);
        return true;
    }

    bool onMessage(const AddOrderMessage& message) override
    {
        _market.AddOrder(Order::Limit(message.OrderReferenceNumber, message.StockLocate, (message.BuySellIndicator == 'B') ? OrderSide::BUY : OrderSide::SELL, message.Price, message.Shares));
        return true;
    }

    bool onMessage(const AddOrderMPIDMessage& message) override
    {
        _market.AddOrder(Order::Limit(message.OrderReferenceNumber, message.StockLocate, (message.BuySellIndicator == 'B') ? OrderSide::BUY : OrderSide::SELL, message.Price, message.Shares));
        return true;
    }

    bool onMessage(const OrderExecutedMessage& message) override
    {
        _market.ExecuteOrder(message.OrderReferenceNumber, message.ExecutedShares);
        return true;
    }

    bool onMessage(const OrderExecutedWithPriceMessage& message) override
    {
        _market.ExecuteOrder(message.OrderReferenceNumber, message.ExecutionPrice, message.ExecutedShares);
        return true;
    }

    bool onMessage(const OrderCancelMessage& message) override
    {
        _market.ReduceOrder(message.OrderReferenceNumber, message.CanceledShares);
        return true;
    }

    bool onMessage(const OrderDeleteMessage& message) override
    {
        _market.DeleteOrder(message.OrderReferenceNumber);
        return true;
    }

    bool onMessage(const OrderReplaceMessage& message) override
    {
        _market.ReplaceOrder(message.OriginalOrderReferenceNumber, message.NewOrderReferenceNumber, message.Price, message.Shares);
        return true;
    }

private:
    MarketManager& _market;
};

int main(int argc, char** argv)
{
    MyMarketHandler market_handler;
    MarketManager market(market_handler);
    MyITCHHandler itch_handler(market);

    // Perform input
    size_t size;
    uint8_t buffer[8192];
    CppCommon::StdInput input;
    while ((size = input.Read(buffer, sizeof(buffer))) > 0)
    {
        // Process the buffer
        itch_handler.Process(buffer, size);
    }

    return 0;
}
```


==================================================
