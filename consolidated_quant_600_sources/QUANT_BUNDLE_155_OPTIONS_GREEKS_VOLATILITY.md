# ⚡ [QUANT-SOURCE-155] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_155_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ui-trading-system (`PHASE4-QUANT-069`)
- **Full Name**: `PHASE4-QUANT-069_Raahi-Bhushan__ui-trading-system`
- **Description**: Self-hosted algorithmic options-trading dashboard for Zerodha Kite Connect (NIFTY/SENSEX)
- **GitHub Stars**: 52
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# UI Trading System

A self-hosted algorithmic options-trading dashboard for NIFTY and SENSEX,
built on the [Zerodha Kite Connect API](https://kite.trade). Flask web UI,
real-time positions with Greeks, GTT monitoring, and several automated
strategies (gap trading, survivor, expiry trades) — everything runs on your
own machine against your own Zerodha account.

> ## ⚠️ Read First
>
> **This software can trade real money.** It is experimental, may contain
> bugs, and may not behave as intended. The authors accept **no
> responsibility for any financial loss** caused by using it. Fresh installs
> start in **dry-run mode** (orders are simulated, nothing reaches the
> broker) — read **[DISCLAIMER.md](DISCLAIMER.md)** in full before enabling
> live trading.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Features

| Module | What it does |
|--------|--------------|
| **Positions** | Live NIFTY/SENSEX option positions with delta/theta Greeks and margin (embedded Black-Scholes) |
| **Wave Extractor** | Gap-trading automation: linked BUY+SELL order pairs re-placed as price waves move |
| **Survivor** | Single-leg index strategy with delta-based rebalancing |
| **Expiry Trade** | Expiry-day strategy on 3-minute candles with Stochastic RSI signals |
| **Early Exit** | Pre-market fair-value GTT exit orders for NIFTY/SENSEX options |
| **GTT Monitor** | Watches GTT triggers, detects duplicates, suppresses stale orders when market is closed |
| **Position Guard** | Flags symbols with unreviewed long exposure across positions, orders, and GTTs |
| **Trade Journal** | FIFO buy/sell pairing, per-algo P&L attribution, Zerodha reconciliation |
| **Covered Calls** | Sell OTM calls against held equity to earn premium |
| **Notifications** | Telegram bot + browser Web Push for fills, margin alerts, and system events |
| **API Monitor** | Every Kite API call logged with caller, latency, and errors |

## Requirements

- Python 3.11+
- A Zerodha account with a [Kite Connect](https://developers.kite.trade/)
  app subscription (paid; needed for the API key/secret)

## Quickstart

```bash
git clone https://github.com/Raahi-Bhushan/ui-trading-system.git
cd ui-trading-system
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python flask_app.py
```

Open <http://127.0.0.1:5010/> — a **setup wizard** walks you through the
Kite API credentials and dashboard login, then writes `configfile.ini` for
you. Restart the app and log in.

The app binds to `127.0.0.1` only. **Never expose it to the internet
without a TLS-terminating reverse proxy in front** — see the
[security notes](docs/security.md).

## Dry-run vs live trading

New installs run with `[safety] live_trading = false`: every order-placement
call is logged with full details but **nothing is sent to Zerodha**. The
header shows a 🟡 DRY-RUN badge. When you are ready, set
`live_trading = true` in `configfile.ini` and restart — the badge turns
🔴 LIVE.

## Documentation

Full docs (configuration reference, architecture, per-module guides, FAQ)
live in [`docs/`](docs/) and are published as a website — see the repository
description for the hosted URL.

## Using the core library without the dashboard

The trading primitives (order placement with retries, instrument cache,
Greeks, GTT monitoring) are pip-installable:

```bash
pip install .
python -c "import instrument_cache, positions_lib, greeks_lib"
```

## Tests

```bash
pytest tests/
```

Tests use real SQLite (no DB mocking) — see
[CONTRIBUTING.md](CONTRIBUTING.md) for conventions.

## Contributing & Security

- Contributions welcome — read [CONTRIBUTING.md](CONTRIBUTING.md) first.
- Found a vulnerability? Please follow [SECURITY.md](SECURITY.md) instead of
  opening a public issue.

## License

[MIT](LICENSE) — with the additional trading-risk terms in
[DISCLAIMER.md](DISCLAIMER.md). Not affiliated with Zerodha.

### Core Implementation Code & Architecture
#### File: `position_guard/__init__.py`
```python

```

#### File: `cas_tracker/__init__.py`
```python

```

#### File: `covered_calls/__init__.py`
```python

```

#### File: `notifications/__init__.py`
```python
# Notifications package
```

#### File: `firebase.json`
```python
{
  "hosting": {
    "public": "site",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "cleanUrls": true
  }
}
```

#### File: `vendor/pykiteconnect/kiteconnect/__version__.py`
```python
__title__ = "kiteconnect"
__description__ = "The official Python client for the Kite Connect trading API"
__url__ = "https://kite.trade"
__download_url__ = "https://github.com/zerodhatech/pykiteconnect"
__version__ = "4.1.0"
__author__ = "Zerodha Technology Pvt. Ltd. (India)"
__author_email__ = "talk@zerodha.tech"
__license__ = "MIT"
```


==================================================


## [2/3] Repository: TradeProject (`PHASE4-QUANT-079`)
- **Full Name**: `PHASE4-QUANT-079_Algo-Ankit__TradeProject`
- **Description**: Production-grade, event-driven algorithmic trading infrastructure for NSE India. Features real-time microstructure   analysis (OFI, VPIN), Options Greeks/IV surface calibration, institutional risk controls (Kill Switch), and   high-fidelity backtesting with Deflated Sharpe Ratio (DSR) validation
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Systematic Algorithmic Trading Infrastructure (NSE India)

## Technical Specification & Operational Documentation

This repository contains a production-grade, low-latency algorithmic trading infrastructure optimized for the National Stock Exchange (NSE) of India. The system is architected as an event-driven distributed system, integrating institutional-grade risk controls, multi-asset quantitative strategies, and a high-fidelity research environment.

---

## 1. System Architecture

The infrastructure follows a decoupled, event-driven architecture designed for high throughput and fault tolerance.

### 1.1 Core Components
*   **Event Orchestration**: A central `EventBus` facilitates asynchronous communication between data feeds, strategy engines, and execution clients using `asyncio` for non-blocking I/O.
*   **Data Ingestion Layer**: Multi-threaded WebSocket consumers for Zerodha (Kite) and Shoonya (Noren), featuring automated failover and tick-level quality validation.
*   **Persistence Layer**: 
    *   **OLAP (ClickHouse)**: High-performance time-series storage for multi-year tick data, feature logs, and execution traces.
    *   **State (Redis)**: Low-latency in-memory store for real-time positions, feature states, and risk utilization metrics.
*   **Message Broker (Kafka)**: Decouples high-volume raw ticks from downstream feature computation and monitoring services.

### 1.2 Quantitative Framework
*   **Microstructure Features**: Real-time calculation of Order Flow Imbalance (OFI), Volume-Synchronized Probability of Informed Trading (VPIN), and Microprice dynamics.
*   **Options Engine**: High-performance Greeks calculation (Delta, Gamma, Vega, Theta) and IV surface calibration using Black-Scholes and Heston model abstractions.
*   **Regime Detection**: Statistical regime identification using Gaussian Hidden Markov Models (HMM) to adapt strategy parameters to market volatility states.

---

## 2. Risk Management & Compliance

The system implements a multi-layered safety framework to ensure capital preservation and regulatory compliance.

### 2.1 Pre-Trade Control Layer
Every signal must pass through the `PreTradeChecker` which validates:
*   **Order Size Limits**: Maximum INR value per clip.
*   **Liquidity Constraints**: Order-to-ADV (Average Daily Volume) percentage limits.
*   **Buying Power**: Real-time margin utilization checks against broker-reported capital.

### 2.2 Real-Time Risk Monitor
*   **Portfolio Drawdown**: Automated kill-switch activation if peak-to-trough drawdown exceeds defined thresholds.
*   **Exposure Management**: Gross and net exposure limits tracked across all sub-strategies.
*   **Kill Switch**: A global safety mechanism that cancels all pending orders and flattens active positions across all legs upon breach.

---

## 3. Execution Logic

The execution layer abstracts broker-specific APIs into a unified interface, supporting sophisticated routing logic.

*   **Smart Executor**: Implements order slicing (Time-Weighted or Volume-Weighted style) to minimize market impact.
*   **Passive-to-Active Upgrades**: Automated limit order management that upgrades to market execution if fill-latency exceeds specified timeouts.
*   **Slippage Profiling**: Detailed tracking of expected vs. realized fill prices to optimize execution parameters.

---

## 4. Research & Backtesting

The infrastructure includes a high-fidelity backtesting engine designed to eliminate look-ahead bias and simulate realistic market conditions.

*   **Engine**: Event-driven simulator that processes historical ClickHouse data as if it were a live feed.
*   **Fill Model**: Incorporates market impact (using Square-root impact models) and variable slippage based on depth-at-best.
*   **Validation**: Implementation of the **Deflated Sharpe Ratio (DSR)** to account for multiple testing bias and reduce the probability of false discoveries.
*   **Walk-Forward**: Automated runner for out-of-sample validation and parameter stability testing.

---

## 5. Operational Deployment

### 5.1 Prerequisites
*   Linux/Windows (Docker-enabled)
*   Python 3.11+
*   Kite Connect / Shoonya API Credentials
*   Minimum 8GB RAM for ClickHouse/Kafka stack

### 5.2 Infrastructure Initialization (The "Big Three")
The system relies on three primary distributed services. These are **fully containerized** via Docker—you do not need to install Redis, Kafka, or ClickHouse directly on your host machine.

Run the bootstrap script to pull and initialize the stack:
```powershell
./scripts/bootstrap.sh
```
This command manages the lifecycle of:
*   **Redis**: (Port 6379) - Used for real-time state and risk tracking.
*   **Kafka**: (Port 9092) - High-throughput tick distribution.
*   **ClickHouse**: (Port 8123/9000) - Analytical storage for historical research.

---

## 6. Execution Guide

This section provides the exact commands required to operate the system.

### 6.1 Data Preparation (ETL)
To populate the analytical database with historical NSE data for backtesting:
```bash
# Downloads and loads Bhavcopy data into ClickHouse
python scripts/backfill.py --from 2024-01-01 --to 2024-12-31
```

### 6.2 Research & Strategy Validation
To execute a backtest for the Statistical Arbitrage strategy:
```bash
# Runs the event-driven simulator and generates a performance report
python scripts/run_backtest.py --months 6 --symbols RELIANCE,TCS,HDFCBANK,INFY
```
*Output: `reports/backtest.html`*

### 6.3 Real-Time Monitoring
To launch the institutional-grade dashboard for PnL and Risk oversight:
```bash
# Requires Redis to be running via Step 5.2
streamlit run monitoring/dashboard/app.py
```

---

## 7. Directory Structure Overview

```text
trading-system/
├── core/               # System kernel: EventBus, MarketClock, AppConfig
├── data/               # Ingestion: Feed clients, Quality Validators, Storage Drivers
├── execution/          # OMS: Broker abstractions, Order Managers, Smart Exec
├── features/           # Alpha: Pipeline, Microstructure, Greeks, Stats
├── infra/              # DevOps: Docker, SQL Init, Kafka Config
├── monitoring/         # Ops: Telegram Alerters, Streamlit Dashboard
├── research/           # Analytics: Backtester, Performance Metrics, DSR Validation
├── risk/               # Safety: Pre-Trade, Real-Time Monitoring, Kill Switch
├── strategies/         # Quant: StatArb, ML Directional, Options RV
└── scripts/            # Utils: Bootstrap, Data Backfill, Backtest Runners
```

---

## 7. Development & Testing
Unit tests are mandatory for all core components. The suite covers data validation, mathematical greeks, and event-bus integrity.
```bash
pytest tests/
```

---
*Disclaimer: This software is for institutional research and trading purposes. Use at your own risk. The developers assume no liability for financial losses.*

### Core Implementation Code & Architecture
#### File: `research/__init__.py`
```python

```

#### File: `research/reporting/__init__.py`
```python

```

#### File: `research/walk_forward/__init__.py`
```python

```

#### File: `research/validation/__init__.py`
```python

```

#### File: `research/backtester/__init__.py`
```python

```

#### File: `core/__init__.py`
```python

```


==================================================


## [3/3] Repository: trade-frame (`PHASE4-QUANT-132`)
- **Full Name**: `PHASE4-QUANT-132_rburkholder__trade-frame`
- **Description**: C++ 17 based library (with sample applications) for testing equities, futures, currencies, etfs & options based automated trading ideas using DTN IQFeed real time data feed and Interactive Brokers (IB TWS API) for trade execution. libtorch/lstm/cuda demo. Support for Alpaca & Phemex. Notifications via Telegram.
- **GitHub Stars**: 677
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# trade-frame

## Introduction

This is a:
* library of functions to sink market data, organize time series, build indicators, author algorithms, and issue orders to a broker for high-capacity, low-latency trading applications
* collection of projects using the libraries to carry out various manual & automated trading scenarios

A primary goal of this solution is to provide a means of tracking an [Option Combo Order](lib/TFTrading/Order_Combo.hpp) through the birth to death life-cycle.  It is easy to enter into a option combo with Interactive Brokers with their user interface, but there does not seem to be an effective way to keep the legs grouped for tracking overall profit/loss.

This library provides a means of ![Tracking](lib/TFOptionCombos/Tracker.h) a ![Combo](lib/TFOptionCombos/Combo.h) ![Leg](lib/TFOptionCombos/Leg.h) with a ![Position](lib/TFTrading/Position.h).  Positions can be grouped together to form ![Portfolios](lib/TFTrading/Portfolio.h).  Portfolios representing Combos can be grouped together to represent the overall profit/loss of a trading Portfolio.

Positions are composed of a ![Watch](lib/TFTrading/Watch.h) class to record bid/ask/tick of ![Instruments](lib/TFTrading/Instrument.h).

![Options](lib/TFOptions/Option.h) inherit from the Watch class to provide ![Greeks](lib/TFTimeSeries/DatedDatum.h), which are computed in real time with an ![Option Engine](lib/TFOptions/Engine.h).

A [Simulation Interface](lib/TFSimulation/SimulationInterface.hpp) is provided for testing strategies off-line.  The simulator will accept [Orders](lib/TFTrading/Order.h) of type Market and Limit assuming bid/ask data has been captured from the exchange during a live session.  A 50ms - 100ms delay queue has been implemented to better simulate round-trip and slippage effects of order submission.

## Example

Picture from the ComboTrading project showing an instrument list, with a chart for one of the listed instruments.  Bid, ask, spread, and greeks are charted for the option (charted real-time).

![Option Greeks Timeline](notes/pictures/qgc-20180925-c-1195_2018-08-16_12-55-40.png)

More pictures under ![ComboTrading](ComboTrading)

## Template

The AutoTrade project can be used as a template to building your own automated high-frequency trading application.

## Build Environment

A C++17 compiler is used to build the libraries and code. Initially, it was built on Windows a number of years ago,
but the focus changed towards supporting a Linux environment.  Some work will be needed to make it build on Windows again.

CMake is used for build management.

Note the use of '-march=native' in the root CMakeFiles.txt.  This will cause code to be not necessarily transportable across CPU types.  Comment out the option if you intend to compile across CPU types, ie, various releases of the Intel instruction set.
See the referenced URL for the variety of instructions across CPU releases.

## Building

Scripts are library version specific.  Build notes are as of 2021/11/22.
There are some wxWidget requirements for using a GTK variation of video drivers (I've used Nvidia and Radeon cards successfully).

You'll need to have about 10G drive space free to build the project, the related libraries,
as well as the installs (from my libs-build repository).

Debian Bookworm is used as the platform.  The library installer is specific to this distribution.
The installer may or may not work with other distributions or flavours.

DTN/IQFeed requires Wine to run.  Starting with the 6.2 release of IQFeed, wine32 is no longer required.
An x64-only installation of wine may generate some wine32 messages and errors, but they can be ignored.


```
# run with bash
# git for latest code, wine for IQFeed daemon
sudo apt-get update && sudo apt-get install git wine64 wget ttf-mscorefonts-installer
wget http://www.iqfeed.net/iqfeed_client_6_2_0_25.exe
wine64 iqfeed_client_6_2_0_25.exe

# interactive brokers TWS for linux
wget https://download2.interactivebrokers.com/installers/tws/stable/tws-stable-linux-x64.sh
sh tws-stable-linux-x64.sh

# install and build initial environment and libraries
git clone https://github.com/rburkholder/libs-build.git
pushd libs-build
./build.sh tradeframe
# rdaf is required for the projects in the rdaf subdirectory - optional
# this is a large install, so recommended only for those interested in the CERN toolset
# will require manual installation of libtorch: https://pytorch.org/cppdocs/installing.html
./build.sh rdaf
# one example uses Wt web library as an interface - optional
# not a recommended install, but provided here as a reference web based app
./build.sh wt
popd

# main trade-frame code
git clone https://github.com/rburkholder/trade-frame.git
# if you have access to the up-to-date private library, use this instead:
# git clone https://github.com/rburkholder/tf2.git

# if you build manually (this is not required if you load the folder into vscode):
cd trade-frame
mkdir build
cd build
cmake ..
# use parallel to use more cpu cores
cmake --build . --parallel 4 --config Debug
# cmake --build . --parallel 4 --config Release   # alternate build flavour
# cmake --build . --target clean  # clean for rebuild
```

I use Visual Studio Code as my IDE.  I have the following extensions installed:
* C/C++ [Microsoft]
* clangd [LLVM Extensions]
* CMake [twxs]
* CMake Tools [Microsoft]

The clangd extension provides the language library to provide symbol lookup and cross-referencing.

I have notes for this combination at
  [Visual Studio Code with CMake and Clangd](https://blog.raymond.burkholder.net/index.php?/archives/1037-Visual-Studio-Code-with-CMake-and-Clangd.html)


## Starting Up

* Start the IQFeed daemon by starting Apps -> Wine -> Programs -> IQFeed -> Watchlist [or from the command line: wine ~/.wine/drive_c/Program\ Files/DTN/IQFeed/iqconnect.exe -autoconnect & ] Login with your credentials and checkbox the Save Username/Password and Autoconnect the first time
* Start Interactive Brokers TWS and connect to a paper trading account
  * Do Not use an active account for testing
  * when connecting via an application, you will need to go into the settings to enable the API, and to activate the port
* IQFeedMarketSymbols project:
  * run the app:
    * Actions -> New Symbol List Remote
    * the program will spend a few minutes downloading, parsing, and saving the latest IQFeed symbol list
    * lots of messages will be generated, no need to evaluate them, other than the summary stats at the end
    * File -> Exit
* IQFeedGetHistory project:
  * obtains daily ohlc values, used to refresh data
  * repeats the symbol download, which was done with IQFeedMarketSymbols
  * run the app:
    * ensure the iqfeed daemon is running (you should see active updates in the quote monitor)
    * 'turn on' IQF
    * Actions -> download n # of days:
      * 0 to download full history of symbol, can take a while
      * 10 to try a test
      * a symbol download will commence
      * there will be a couple of minutes of no activity while the symbol list is scanned
      * data for a series of symbols will start
      * once the message 'Process Complete' shows, the download is complete
    * 'turn off' IQF
    * File -> Exit
* more apps to be described here ...

## Background

Current Market Data Providers and Execution vendors:

* IQFeed: real time market data and historical data
* Interactive Brokers:  real time market data, real time order execution
* Alpaca: real time data and order execution
* Phemex: real time data, order execution (work in progress)

Securities types:

* Equities
* Options
* Futures
* Futures Options

Libraries used (use my lib-build respository to download and build the various dependencies):

* wxWidgets
* boost
* curl
* zlib
* hdf5
* sqlite (included in source)
* exelformat (included in source)
* rdaf aka ROOT - library from CERN providing the clang C++ interpreter - optional

NOTE: The code started out on Windows using Visual Studio, and is now predominately tested on Linux Debian.  Some work is required
to port back to Windows.  There are various Windows based artifacts in various directories.  They are not fully functional at this time.

The lib directory has a series of libraries I use throughout the various projects/applications.  Primary libraries include:

* ![TFTimeSeries](lib/TFTimeSeries) - manage trades, quotes, greeks, ![level II order book](lib/TFIQFeed/Level2)
* ![TFSimulation](lib/TFSimulation) - simulation engine
* ![TFIQFeed](lib/TFIQFeed) - engine to talk to DTNIQ Feed for Level1 & Level2 data (ask me for a referral)
* ![TFInteractiveBrokers](lib/TFInteractiveBrokers) - engine to talk to IB
* ![TFIndicators](lib/TFIndicators) - some indicators
* ![TFHDF5TimeSeries](lib/TFHDF5TimeSeries) - wraps the HDF5 library for storing time series
* ![TFOptions](lib/TFOptions) - options calculations
* ![TFTrading](lib/TFTrading) - manages orders, executions, portfolios, positions, accounts,
* ![TFVuTrading](lib/TFVuTrading) - provides a number of forms, panels, and related user-interface elements
* ![OUCharting](lib/OUCharting) - wrapper around ChartDirector for plots and charts
* ![OUSQL](lib/OUSQL) - which is an ORM wrapper around a sqlite database for maintaining trading records

These are some of the currently supported applications:

* ![AutoTrade](AutoTrade/README.md) - code as template for automated trading - start of some ML based work
* ![BarChart](BarChart/README.md) - tag instruments by interest and review last 200 daily bars
* ![BasketTrading](BasketTrading/README.md) - a work in progress for trading futures based options combinations
* ![Collector](Collector/README.md) - stream real time bid/ask/tick data to disk for use in backtesting and training
* ![ComboTrading](ComboTrading/README.md) - basics of trading multiple securities, such as various options strategies
* ![CurrencyTrader](CurrencyTrader/README.md) - exploratory code for understanding currency trading concepts
* ![Dividend](Dividend/README.md) - console app to query IQFeed for possible dividend based equity investments
* ![DepthOfMarket](DepthOfMarket/README.md) - use a level II ladder to trade futures
* ![Hdf5Chart](Hdf5Chart/README.md) - view the contents of the hdf5 data set
* ![IndicatorTrading](IndicatorTrading/README.md) - view and trade with futures level II data
* ![IQFeedMarketSymbols](IQFeedMarketSymbols/README.md) - automatically download and decompress the latest mkt_symbol.txt file from dtn/iqfeed
* ![IQFeedGetHistory](IQFeedGetHistory/README.md) - load up with historical data for looking for trading ideas
* ![LiveChart](LiveChart/README.md) - view instruments in real time
* ![SP500](SP500/README.md) - Backtest SPY symbol with support of ticks_ratio using libtorch LSTM based model to train/predict on Collector data

Sample code, not supported:

* StickShift2 - some rough code for some option trading ideas
* HedgedBollinger - some experiments in futures, mostly tracking at the money implied volatility

The announcement on my blog:  http://blog.raymond.burkholder.net/index.php?/archives/679-trade-frame-c++-securities-trading-software-development-framework.html

Some other, possibly, related entries:  http://blog.raymond.burkholder.net/index.php?/categories/23-Trading

NOTE: During its infancy, the code used MFC (Microsoft Foundation Classes), some Berkeley DB code, and various other modules,
which I now no longer support.  The code remains in the repository for historical value, and for the time it might be
re-written for current use.

## Testing

* IQFeed testing: you can utilize the symbol TST$Y, this symbol sends a loop of data 24/7. (2019/03/12)

## Miscellandous

* 2022/07/16 additional package requirement (incorporated into libs-build/build.sh):
  * sudo apt install portaudio19-dev

* 2022/07/25 additional package requirement (incorporated into libs-build/build.sh);
  * sudo apt install libcrypto++-dev

### Core Implementation Code & Architecture
#### File: `SP500/Torch.hpp`
```python
void TorchTest_v1();
void TorchTest_v2();
```

#### File: `Unsorted/mfc/BookTrader/TradeFrameController.cpp`
```python
#include "StdAfx.h"
#include "TradeFrameController.h"

CTradeFrameController::CTradeFrameController(void) {
}

CTradeFrameController::~CTradeFrameController(void) {
}
```

#### File: `Unsorted/mfc/GTScalp/stdafx.cpp`
```python
// stdafx.cpp : source file that includes just the standard includes
// GTScalp.pch will be the pre-compiled header
// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"
```

#### File: `Unsorted/PositionOptionDeltasControl.cpp`
```python
#include "StdAfx.h"
#include "PositionOptionDeltasControl.h"

CPositionOptionDeltasControl::CPositionOptionDeltasControl(void) {
}

CPositionOptionDeltasControl::~CPositionOptionDeltasControl(void) {
}
```

#### File: `Unsorted/mfc/BookTrader/stdafx.cpp`
```python
// stdafx.cpp : source file that includes just the standard includes
// TradeFrame.pch will be the pre-compiled header
// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"
```

#### File: `lib/TFInteractiveBrokers/client/StdAfx.cpp`
```python
﻿/* Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 * and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable. */

#include "StdAfx.h"
```


==================================================
