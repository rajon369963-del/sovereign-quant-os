# ⚡ [QUANT-SOURCE-230] Consolidated Quant & Algo Trading Repositories
**Category**: `INDICATORS_FEATURE_ENGINEERING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_230_INDICATORS_FEATURE_ENGINEERING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: tulipindicators (`WHEEL_tulipindicators`)
- **Full Name**: `tulipindicators`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
[![Build Status](https://travis-ci.com/TulipCharts/tulipindicators.svg?branch=master)](https://travis-ci.com/TulipCharts/tulipindicators)

# Tulip Indicators

## Introduction

Tulip Indicators is a library of technical analysis functions written in ANSI C.

Lots of information is available on the website:
[https://tulipindicators.org](https://tulipindicators.org)

Bindings are available for Node.js, Go, Ruby, Python, and others. [See here](https://tulipindicators.org/bindings).

## Features

 - **C99 with no dependencies**.
 - Uses fast algorithms.
 - Easy to use programming interface.
 - Release under LGPL license.


## Building

Building is easy. You only need a decent C compiler. Tulip Indicators has no
other dependencies.

Just download the code and run `make`.

```
git clone https://github.com/TulipCharts/tulipindicators
cd tulipindicators
make
```

You should get a static library, `libindicators.a`. You'll need that library
and the header file `indicators.h` to use Tulip Indicators in your code.


## Not Building

If you don't want to build the library, you can simply add the
`tiamalgamation.c` file to your project, along with `indicators.h` and
`candles.h`. The amalgamation file contains all of Tulip Indicators - you don't
actually need any of the other source files.

This is the recommended method to import Tulip Indicators into code for
bindings to other languages, since it makes it very easy to update versions.

## Usage

For usage information, please see:
[https://tulipindicators.org/usage](https://tulipindicators.org/usage)


## Indicator Listing
```
104 total indicators

Overlay
   avgprice            Average Price
   bbands              Bollinger Bands
   dema                Double Exponential Moving Average
   ema                 Exponential Moving Average
   hma                 Hull Moving Average
   kama                Kaufman Adaptive Moving Average
   linreg              Linear Regression
   medprice            Median Price
   psar                Parabolic SAR
   sma                 Simple Moving Average
   tema                Triple Exponential Moving Average
   trima               Triangular Moving Average
   tsf                 Time Series Forecast
   typprice            Typical Price
   vidya               Variable Index Dynamic Average
   vwma                Volume Weighted Moving Average
   wcprice             Weighted Close Price
   wilders             Wilders Smoothing
   wma                 Weighted Moving Average
   zlema               Zero-Lag Exponential Moving Average

Indicator
   ad                  Accumulation/Distribution Line
   adosc               Accumulation/Distribution Oscillator
   adx                 Average Directional Movement Index
   adxr                Average Directional Movement Rating
   ao                  Awesome Oscillator
   apo                 Absolute Price Oscillator
   aroon               Aroon
   aroonosc            Aroon Oscillator
   atr                 Average True Range
   bop                 Balance of Power
   cci                 Commodity Channel Index
   cmo                 Chande Momentum Oscillator
   cvi                 Chaikins Volatility
   di                  Directional Indicator
   dm                  Directional Movement
   dpo                 Detrended Price Oscillator
   dx                  Directional Movement Index
   emv                 Ease of Movement
   fisher              Fisher Transform
   fosc                Forecast Oscillator
   kvo                 Klinger Volume Oscillator
   linregintercept     Linear Regression Intercept
   linregslope         Linear Regression Slope
   macd                Moving Average Convergence/Divergence
   marketfi            Market Facilitation Index
   mass                Mass Index
   mfi                 Money Flow Index
   mom                 Momentum
   msw                 Mesa Sine Wave
   natr                Normalized Average True Range
   nvi                 Negative Volume Index
   obv                 On Balance Volume
   ppo                 Percentage Price Oscillator
   pvi                 Positive Volume Index
   qstick              Qstick
   roc                 Rate of Change
   rocr                Rate of Change Ratio
   rsi                 Relative Strength Index
   stoch               Stochastic Oscillator
   stochrsi            Stochastic RSI
   tr                  True Range
   trix                Trix
   ultosc              Ultimate Oscillator
   vhf                 Vertical Horizontal Filter
   volatility          Annualized Historical Volatility
   vosc                Volume Oscillator
   wad                 Williams Accumulation/Distribution
   willr               Williams %R

Math
   crossany            Crossany
   crossover           Crossover
   decay               Linear Decay
   edecay              Exponential Decay
   lag                 Lag
   max                 Maximum In Period
   md                  Mean Deviation Over Period
   min                 Minimum In Period
   stddev              Standard Deviation Over Period
   stderr              Standard Error Over Period
   sum                 Sum Over Period
   var                 Variance Over Period

Simple
   abs                 Vector Absolute Value
   acos                Vector Arccosine
   add                 Vector Addition
   asin                Vector Arcsine
   atan                Vector Arctangent
   ceil                Vector Ceiling
   cos                 Vector Cosine
   cosh                Vector Hyperbolic Cosine
   div                 Vector Division
   exp                 Vector Exponential
   floor               Vector Floor
   ln                  Vector Natural Log
   log10               Vector Base-10 Log
   mul                 Vector Multiplication
   round               Vector Round
   sin                 Vector Sine
   sinh                Vector Hyperbolic Sine
   sqrt                Vector Square Root
   sub                 Vector Subtraction
   tan                 Vector Tangent
   tanh                Vector Hyperbolic Tangent
   todeg               Vector Degree Conversion
   torad               Vector Radian Conversion
   trunc               Vector Truncate

```


## Special Thanks

The stochrsi indicator was sponsored by: [Gunthy](https://gunthy.org).

The candle pattern recognition was sponsored by: [Algorum](https://algorumsoftware.com)


==================================================


## [2/3] Repository: Crypto-Signal (`PHASE4-QUANT-019`)
- **Full Name**: `PHASE4-QUANT-019_CryptoSignal__Crypto-Signal`
- **Description**: Github.com/CryptoSignal - Trading & Technical Analysis Bot - 4,100+ stars, 1,100+ forks
- **GitHub Stars**: 5639
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# CryptoSignal - #1 Quant Trading & Technical Analysis Bot - 4,100+ stars & 1,000+ forks https://github.com/CryptoSignal/Crypto-Signal

### Development state: Beta (Code is stable, documentation is often lagging)

### Join our community [Discord](https://discord.gg/MWTJVFf) channel! (2,100+ members)

Crypto Signals is a command line tool that automates your crypto currency Technical Analysis (TA). It is maintained by a community of traders, engineers, data scientists, PMs, & countless generous individuals who wish to democratize the equal & open access to the greatest wealth re-distribution experiment in human and monetary policy history - Bitcoin

## Track over 500 coins across Bittrex, Binance, Bittrex, Bitfinex, Coinbase, Gemini and more!
(Subject to local financial regulations under the jurisdiction you and your financial activities are under. Marketing or enabling does not imply nor justify the facilitation or condoning of any activity - financial or otherwise. You assume and bare all risk. Be careful & act wisely.)

## Technical Analysis Automated:
* Momentum
* Relative Strength Index (RSI)
* Ichimoku Cloud (Leading Span A, Leading Span B, Conversion Line, Base Line)
* Simple Moving Average
* Exponential Moving Average
* MACD
* MFI
* OBV
* VWAP

## Alerts:
* SMS via Twilio
* Email
* Slack
* Telegram
* Discord

## Features:
* Modular code for easy trading strategy implementation
* Easy install with Docker

You can build on top of this tool and implement algorithm trading and some machine learning models to experiment with predictive analysis.

### Founded by Abenezer Mamo @ www.Mamo.io & www.linkedin.com/in/AbenezerMamo

## Installing And Running
The commands listed below are intended to be run in a terminal.

1. Install [docker CE](https://docs.docker.com/install/)

1. Create a config.yml file in your current directory. See the Configuring config.yml section below for customizing settings.

1. In a terminal run the application. `docker run --rm -v $PWD/config.yml:/app/config.yml shadowreaver/crypto-signal:master`.

1. When you want to update the application run `docker pull shadowreaver/crypto-signal:master`

### Configuring config.yml

For a list of all possible options for config.yml and some example configurations look [here](docs/config.md)

# FAQ

## Common Questions

### Why does Tradingview show me different information than crypto-signal?
There are a number of reasons why the information crypto-signal provides could be different from tradingview and the truth is we have no way to be 100% certain of why the differences exist. Below are some things that affect the indicators that _may_ differ between crypto-signal and tradingview.

- tradingview will have more historical data and for some indicators this can make a [big difference](https://ta-lib.org/d_api/ta_setunstableperiod.html).

- tradingview uses a rolling 15 minute timeframe which means that the data they are analyzing can be more recent than ours by a factor of minutes or hours depending on what candlestick timeframe you are using.

- tradingview may collect data in a way that means the timeperiods we have may not line up with theirs, which can have an effect on the analysis. This seems unlikely to us, but stranger things have happened.

### So if it doesn't match Tradingview how do you know your information is accurate?
Underpinning crypto-signal for most of our technical analysis is [TA-Lib](https://ta-lib.org/index.html) which is an open source technical analysis project started in 1999. This project has been used in a rather large number of technical analysis projects over the last two decades and is one of the most trusted open source libraries for analyzing candlestick data.

# Liability
I am not your financial adviser, nor is this tool. Use this program as an educational tool, and nothing more. None of the contributors to this project are liable for any losses you may incur. Be wise and always do your own research.

We recommend you begin by learning the core principles used in traditional asset classes since they are less volatile & apply your knowledge in simulated trading before liquidating your dreams.

### Core Implementation Code & Architecture
#### File: `app/__init__.py`
```python

```

#### File: `app/notifiers/__init__.py`
```python

```

#### File: `app/analyzers/__init__.py`
```python
__all__ = ['crossover']
```

#### File: `app/analyzers/informants/__init__.py`
```python
__all__ = [
    'bollinger_bands',
    'ema',
    'sma',
    'vwap',
    'ohlcv'
]
```

#### File: `app/analyzers/indicators/__init__.py`
```python
__all__ = [
    'ichimoku',
    'macd',
    'momentum',
    'rsi',
    'stoch_rsi',
    'mfi',
    'obv'
]
```

#### File: `app/notifiers/stdout_client.py`
```python
"""Notify a user via stdout
"""

import structlog
#from tenacity import retry, retry_if_exception_type, stop_after_attempt

from notifiers.utils import NotifierUtils

class StdoutNotifier(NotifierUtils):
    """Class for handling stdout notifications
    """

    def __init__(self):
        """Initialize StdoutNotifier class
        """


    def notify(self, message):
        """stdout send the message.

        Args:
            message (str): The message to print.
        """

        print(message)
```


==================================================


## [3/3] Repository: Algo-Trading (`DISC-524`)
- **Full Name**: `Manudecara/Algo-Trading`
- **Description**: This is my github repository where I post trading strategies, tutorials and research on quantitative finance with R, C++ and Python. Some of the topics explored include: machine learning, high frequency trading, NLP, technical analysis and more. Hope you enjoy it!
- **GitHub Stars**: 150
- **Source Pool**: `discovered_github_repos.json`

### Comprehensive Architectural Blueprint & Signal Pipeline
- **Role in Quantitative Pipeline**: High-performance execution, signal feature extraction, risk parity constraint management, and microsecond DMA order dispatch.
- **Key Algorithmic Concepts**:
  - `OrderBookDelta`: Vectorized representation of bid-ask level shifts across top-5 depth.
  - `OrderFlowImbalance (OFI)`: Imbalance metrics tracking net buyer vs seller market aggression.
  - `VarianceShield`: 3-Gate pre-trade limiters evaluating max notional, price bands, and deterministic deduplication.
- **Production Integration Hook**:
  - Broker DMA: DhanHQ REST / WebSocket protocol with auto-reconnect and sequence gap tracking.
  - Risk Governor: SEBI 2026 Order-to-Trade Ratio limiter maintaining OTR <= 1.0.


==================================================
