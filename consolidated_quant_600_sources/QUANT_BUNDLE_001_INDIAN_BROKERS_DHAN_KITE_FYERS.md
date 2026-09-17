# ⚡ [QUANT-SOURCE-001] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_001_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: pykiteconnect (`WHEEL_pykiteconnect`)
- **Full Name**: `pykiteconnect`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# The Kite Connect API Python client - v4

[![PyPI](https://img.shields.io/pypi/v/kiteconnect.svg)](https://pypi.python.org/pypi/kiteconnect)
[![Build Status](https://travis-ci.org/zerodhatech/pykiteconnect.svg?branch=kite3)](https://travis-ci.org/zerodhatech/pykiteconnect)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/zerodhatech/pykiteconnect?svg=true)](https://ci.appveyor.com/project/rainmattertech/pykiteconnect)
[![codecov.io](https://codecov.io/gh/zerodhatech/pykiteconnect/branch/kite3/graphs/badge.svg?branch=kite3)](https://codecov.io/gh/zerodhatech/pykiteconnect/branch/kite3)

The official Python client for communicating with the [Kite Connect API](https://kite.trade).

Kite Connect is a set of REST-like APIs that expose many capabilities required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (WebSockets), and more, with the simple HTTP API collection.

[Zerodha Technology](https://zerodha.com) (c) 2021. Licensed under the MIT License.

## Documentation

- [Python client documentation](https://kite.trade/docs/pykiteconnect/v4)
- [Kite Connect HTTP API documentation](https://kite.trade/docs/connect/v3)

## v4 - Breaking changes

- Renamed ticker fields as per [kite connect doc](https://kite.trade/docs/connect/v3/websocket/#quote-packet-structure)
- Renamed `bsecds` to `bcd` in `ticker.EXCHANGE_MAP`

## v5 - Breaking changes

- **Drop Support for Python 2.7**: Starting from version v5, support for Python 2.7 has been discontinued. This decision was made due to the [announcement](https://github.com/actions/setup-python/issues/672) by `setup-python`, which stopped supporting Python 2.x since May 2023.

- **For Python 2.x Users**: If you are using Python 2.x, you can continue using the `kiteconnect` library, but please stick to the <= 4.x.x versions of the library. You can find the previous releases on the [PyKiteConnect GitHub Releases](https://github.com/zerodha/pykiteconnect/releases) page.

## v5.2 - Auto slice orders

- Added `place_autoslice_order()` for placing orders that exceed exchange freeze limits. The order is automatically split into multiple smaller orders internally and the response contains the parent `order_id` along with a `children` list, where each child is either a placed order (`order_id`) or an `error` payload.

  ```python
  response = kite.place_autoslice_order(
      variety=kite.VARIETY_REGULAR,
      exchange=kite.EXCHANGE_NFO,
      tradingsymbol="NIFTY25APRFUT",
      transaction_type=kite.TRANSACTION_TYPE_BUY,
      quantity=100000,
      product=kite.PRODUCT_MIS,
      order_type=kite.ORDER_TYPE_MARKET,
  )

  parent_order_id = response["order_id"]
  for child in response.get("children", []):
      if "order_id" in child:
          ...  # child placed
      else:
          ...  # child["error"] payload
  ```

## Installing the client

You can install the pre release via pip

```
pip install --upgrade kiteconnect
```

Its recommended to update `setuptools` to latest if you are facing any issue while installing

```
pip install -U pip setuptools
```

Since some of the dependencies uses C extensions it has to compiled before installing the package.

### Linux, BSD and macOS

- On Linux, and BSDs, you will need a C compiler (such as GCC).

#### Debian/Ubuntu

```
apt-get install libffi-dev python-dev python3-dev
```

#### Centos/RHEL/Fedora

```
yum install libffi-devel python3-devel python-devel
```

#### macOS/OSx

```
xcode-select --install
```

### Microsoft Windows

Each Python version uses a specific compiler version (e.g. CPython 2.7 uses Visual C++ 9.0, CPython 3.3 uses Visual C++ 10.0, etc). So, you need to install the compiler version that corresponds to your Python version

- Python 2.6, 2.7, 3.0, 3.1, 3.2 - [Microsoft Visual C++ 9.0](https://wiki.python.org/moin/WindowsCompilers#Microsoft_Visual_C.2B-.2B-_9.0_standalone:_Visual_C.2B-.2B-_Compiler_for_Python_2.7_.28x86.2C_x64.29)
- Python 3.3, 3.4 - [Microsoft Visual C++ 10.0](https://wiki.python.org/moin/WindowsCompilers#Microsoft_Visual_C.2B-.2B-_10.0_standalone:_Windows_SDK_7.1_.28x86.2C_x64.2C_ia64.29)
- Python 3.5, 3.6 - [Microsoft Visual C++ 14.0](https://wiki.python.org/moin/WindowsCompilers#Microsoft_Visual_C.2B-.2B-_14.0_standalone:_Visual_C.2B-.2B-_Build_Tools_2015_.28x86.2C_x64.2C_ARM.29)

For more details check [official Python documentation](https://wiki.python.org/moin/WindowsCompilers).

## API usage

```python
import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

data = kite.generate_session("request_token_here", api_secret="your_secret")
kite.set_access_token(data["access_token"])

# Place an order
try:
    order_id = kite.place_order(tradingsymbol="INFY",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=1,
                                variety=kite.VARIETY_AMO,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)

    logging.info("Order placed. ID is: {}".format(order_id))
except Exception as e:
    logging.info("Order placement failed: {}".format(e.message))

# Fetch all orders
kite.orders()

# Get instruments
kite.instruments()

# Place an mutual fund order
kite.place_mf_order(
    tradingsymbol="INF090I01239",
    transaction_type=kite.TRANSACTION_TYPE_BUY,
    amount=5000,
    tag="mytag"
)

# Cancel a mutual fund order
kite.cancel_mf_order(order_id="order_id")

# Get mutual fund instruments
kite.mf_instruments()
```

Refer to the [Python client documentation](https://kite.trade/docs/pykiteconnect/v4) for the complete list of supported methods.

## WebSocket usage

```python
import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)

# Initialise
kws = KiteTicker("your_api_key", "your_access_token")

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([738561, 5633])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [738561])

def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
```

## Run unit tests

```sh
python setup.py test
```

or

```sh
pytest -s tests/unit --cov-report html:cov_html --cov=./
```

## Run integration tests

```sh
pytest -s tests/integration/ --cov-report html:cov_html --cov=./  --api-key api_key --access-token access_token
```

## Generate documentation

```sh
pip install pdoc

pdoc --html --html-dir docs kiteconnect
```

## Changelog

[Check release notes](https://github.com/zerodha/pykiteconnect/releases)

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/unit/__init__.py`
```python

```

#### File: `tests/integration/__init__.py`
```python

```

#### File: `tests/helpers/__init__.py`
```python

```

#### File: `kiteconnect/__version__.py`
```python
__title__ = "kiteconnect"
__description__ = "The official Python client for the Kite Connect trading API"
__url__ = "https://kite.trade"
__download_url__ = "https://github.com/zerodhatech/pykiteconnect"
__version__ = "5.2.1"
__author__ = "Zerodha Technology Pvt. Ltd. (India)"
__author_email__ = "talk@zerodha.tech"
__license__ = "MIT"
```

#### File: `examples/ticker.py`
```python
###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Zerodha Technology Pvt. Ltd.
#
# This example shows how to subscribe and get ticks from Kite Connect ticker,
# For more info read documentation - https://kite.trade/docs/connect/v1/#streaming-websocket
###############################################################################

import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)

# Initialise
kws = KiteTicker("your_api_key", "your_access_token")

def on_ticks(ws, ticks):  # noqa
    # Callback to receive ticks.
    logging.info("Ticks: {}".format(ticks))

def on_connect(ws, response):  # noqa
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([738561, 5633])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [738561])

def on_order_update(ws, data):
    logging.debug("Order update : {}".format(data))

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_order_update = on_order_update

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
```


==================================================


## [2/3] Repository: Mastering-AlgoTrading-A-Beginners-Guide-using-KiteConnect-API (`VAULT_IN-QUANT-004_aeron7__Mastering-AlgoTrading-A-Beginners-Guide-using-KiteConnect-API`)
- **Full Name**: `IN-QUANT-004_aeron7__Mastering-AlgoTrading-A-Beginners-Guide-using-KiteConnect-API`
- **Description**: Launch into the realm of algorithmic trading with this beginner's guide. Explore the intricacies of the Indian Stock Market through practical examples and hands-on experience. This guide is tailored for those looking to harness the power of Zerodha's KiteConnect API for effective and efficient trading strategies.
- **GitHub Stars**: 61
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# 🌟 Mastering AlgoTrading: A Beginner's Guide using KiteConnect API 🌟

> 🚀 Launch into the realm of algorithmic trading with this beginner's guide. Explore the intricacies of the Indian Stock Market through practical examples and hands-on experience. This guide is tailored for those looking to harness the power of Zerodha's KiteConnect API for effective and efficient trading strategies.

## 🌐 Overview

- **Zerodha KiteConnect**
  - 🤖 Immerse yourself in the world of algorithmic trading with Zerodha's feature-rich trading platform, offering comprehensive functionalities for an enhanced trading experience.
- **Complete Course**
  - 📘 Dive deeper into algorithmic trading by exploring the full course content [here](https://unofficed.com/courses/mastering-algotrading-a-beginners-guide-using-kiteconnect-api/).

## 📚 Table of Contents

1. **Getting Instrument Token of a Scrip Using Python and Zerodha API**
2. **Getting Instrument Token of a Scrip Using Python and Zerodha Kite LTP Method**
3. **Getting Historical Data of Reliance Using Python and Zerodha API**
4. **Getting Historical Data of Reliance In Pandas Using Python and Zerodha API**
5. **Organizing Expiry Dates of Financial Instruments with Python**
6. **Buy on RSI Strategy Coding in Python using Zerodha**
7. **Guppy Strategy Screener Using Python and Zerodha**
8. **Guppy Strategy Trading Bot Using Python and Zerodha**
9. **Guppy Indicator Trading Bot Using Python and Zerodha**
10. **Plotting OHLC to Candlestick Chart**
11. **Plotting Zerodha OHLC to Candlestick Chart**
12. **Converting Candles to Heikin Ashi Using Zerodha KiteConnect**
13. **Creating TimeFrames from Minute-Based Data Using Python**
14. **Multi-Stock Bot Using Guppy Strategy with Screener and Backtesting**
15. **RSI Based Trading Bot with Python using Zerodha API**
16. **Multi-Timeframe Bot Using Guppy Strategy and Screener**
17. **Backtesting Guppy Multiple Moving Average (GMMA) with Python using Zerodha API**
18. **Exploring Technical Indicators in the Indian Stock Market with Zerodha API and Python**

## 📜 Descriptions

### 1. Getting Instrument Token of a Scrip Using Python and Zerodha API
   - Learn how to retrieve the instrument token for a specific scrip using Python in conjunction with the Zerodha API.

### 2. Getting Instrument Token of a Scrip Using Python and Zerodha Kite LTP Method
   - A guide to acquiring instrument tokens using the Kite LTP (Last Traded Price) method in Python with Zerodha's API.

### 3. Getting Historical Data of Reliance Using Python and Zerodha API
   - Discover the method to fetch historical data for Reliance stocks using Python through the Zerodha API.

### 4. Getting Historical Data of Reliance In Pandas Using Python and Zerodha API
   - Explore how to process and analyze Reliance's historical data using Pandas in Python, leveraging Zerodha's API.

### 5. Organizing Expiry Dates of Financial Instruments with Python
   - Learn to organize and manage the expiry dates of various financial instruments using Python.

### 6. Buy on RSI Strategy Coding in Python using Zerodha
   - Implement the RSI (Relative Strength Index) strategy in Python for trading decisions on the Zerodha platform.

### 7. Guppy Strategy Screener Using Python and Zerodha
   - A comprehensive guide to using the Guppy strategy for screening stocks with Python on Zerodha.

### 8. Guppy Strategy Trading Bot Using Python and Zerodha
   - Develop an automated trading bot that employs the Guppy strategy in Python with Zerodha's API.

### 9. Guppy Indicator Trading Bot Using Python and Zerodha
   - Create a trading bot focused on the Guppy indicator, utilizing Python and Zerodha's tools for automated trading.

### 10. Plotting OHLC to Candlestick Chart
   - Understand the process of transforming OHLC (Open, High, Low, Close) data into intuitive candlestick charts.

### 11. Plotting Zerodha OHLC to Candlestick Chart
   - Learn to convert Zerodha's OHLC data into candlestick charts for better visualization and analysis.

### 12. Converting Candles to Heikin Ashi Using Zerodha KiteConnect
   - Master the technique of converting candlestick charts to Heikin Ashi format using Zerodha KiteConnect.

### 13. Creating TimeFrames from Minute-Based Data Using Python
   - A guide to creating various timeframes from minute-based data for comprehensive market analysis using Python.

### 14. Multi-Stock Bot Using Guppy Strategy with Screener and Backtesting
   - Build a multi-stock trading bot that incorporates the Guppy strategy, complete with screening and backtesting functionalities.

### 15. RSI Based Trading Bot with Python using Zerodha API
   - Develop a trading bot in Python that operates based on the RSI strategy, integrated with Zerodha's API.

### 16. Multi-Timeframe Bot Using Guppy Strategy and Screener
   - Create an advanced bot that operates across multiple timeframes using the Guppy strategy, along with stock screening.

### 17. Backtesting Guppy Multiple Moving Average (GMMA) with Python using Zerodha API
   - Learn the nuances of backtesting the Guppy Multiple Moving Average strategy using Python with Zerodha's API.

### 18. Exploring Technical Indicators in the Indian Stock Market with Zerodha API and Python
   - Dive into various technical indicators and their application in the Indian stock market using Python and Zerodha's API.


## 🚀 Conclusion

Step into the exciting world of Algo Trading. This guide is your gateway to understanding and applying effective trading strategies in the Indian stock market, leveraging the technological prowess of Zerodha’s KiteConnect API.


==================================================


## [3/3] Repository: dhanhq-py (`WHEEL_dhanhq-py`)
- **Full Name**: `dhanhq-py`
- **Description**: The official Python client for communicating with the Dhan API.
- **GitHub Stars**: 196
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# DhanHQ-py : v2.3.0-rc1 (Pre-release)

[![PyPI](https://img.shields.io/pypi/v/dhanhq.svg)](https://pypi.org/project/dhanhq/)

> ⚠️ **Pre-release / Release Candidate.** `v2.3.0rc1` is a release candidate for testing the new features below. It is not the latest stable release, so `pip install dhanhq` will not pick it up. Install it explicitly:
```bash
pip install --pre dhanhq==2.3.0rc1
```

The official Python client for communicating with the [Dhan API](https://api.dhan.co/v2/)  

DhanHQ-py Rest API is used to automate investing and trading. Execute orders in real time along with position management, live and historical data, tradebook and more with simple API collection.

Not just this, you also get real-time market data via DhanHQ Live Market Feed.


[Dhan](https://dhan.co) (c) 2026. Licensed under the [MIT License](https://github.com/dhan-oss/DhanHQ-py/blob/main/LICENSE)

### Documentation

- [DhanHQ Python Documentation](https://docs.dhanhq.co/api/v2/guides/sdks/python)
- [DhanHQ Developer Kit](https://api.dhan.co/v2/)
- [DhanHQ API Documentation](https://docs.dhanhq.co/api/v2/)

## v2.3.0-rc1 - What's new (Pre-release)
> This is a **release candidate**. APIs in this section are new and may change before the final `v2.3.0` release. Install with `pip install --pre dhanhq==2.3.0rc1`.

- **Conditional Orders** - place one or more orders automatically when a price or technical-indicator condition is met (Equities & Indices).
- **Global Stocks** - trade US stocks: orders, trades, holdings, fund limit, market status, order/charge estimate and margin. A separate Global Stocks instrument list is available too.
- **Global Stocks Live Feed** - real-time US stock Trade and OHLC packets over WebSocket via the new `GlobalStocksFeed`.
- **P&L based Exit** - auto square-off when cumulative profit or loss hits the configured absolute value thresholds (Trader's Control).
- **Multi-leg Margin Calculator** - compute combined margin for multiple orders with hedge benefits.

And a lot more is available directly on DhanHQ Python Library now.

---


## v2.2.0 - What's new
- You can now access the entire full market depth (200 Level) via DhanHQ APIs and part of the python library.
- Expired Options Data are now directly available on the library and you can fetch for all NSE & BSE instruments
- Super Orders - smart orders for managing risk and profits is now introduced with DhanHQ
- You can set, modify and change IP for your account, right from the python library - the code for the same is available under example.

And a lot more is available directly on DhanHQ Python Library now.

You can read about all other updates from DhanHQ V2 here: [DhanHQ Releases](https://docs.dhanhq.co/api/v2/guides/releases/).

---

## Features

* **Order Management**  
The order management APIs lets you place a new order, cancel or modify the pending order, retrieve the order status, trade status, order book & tradebook.

* **Live Market Feed**  
Get real-time market data to power your trading systems, with easy to implement functions and data across exchanges.

* **Market Quote**  
REST APIs based market quotes which given you snapshot of ticker mode, quote mode or full mode.

* **Option Chain**  
Single function which gives entire Option Chain across exchanges and segments, giving OI, greeks, volume, top bid/ask and price data.

* **Forever Order**  
Place, modify or delete Forever Orders, whether single or OCO to better manage your swing trades.

* **Conditional Orders**  
Place one or more orders automatically when a price or technical-indicator condition is met, for Equities & Indices.

* **Global Stocks**  
Trade US stocks - place, modify and cancel orders, fetch trades, holdings, fund limit and market status, plus order/charge and margin estimates. A live feed for US stocks is available too.

* **P&L based Exit & Multi-leg Margin**  
Auto square-off on cumulative profit/loss thresholds and calculate combined margin for multiple orders with hedge benefits.

* **Portfolio Management**  
With this set of APIs, retrieve your holdings and positions in your portfolio as well as manage them.

* **Historical Data**  
Get historical candle data for the desired scrip across segments & exchange, both multiple minute timeframe OHLC and Daily OHLC.

* **Fund Details**  
Get all information of your trading account like balance, margin utilised, collateral, etc as well margin required for any order.

* **eDIS Authorisation**  
To sell holding stocks, one needs to complete the CDSL eDIS flow, generate T-PIN & mark stock to complete the sell action.

## Quickstart

You can install the package via pip

```
pip install dhanhq
```



### Authentication

You can now generate access tokens using the `DhanLogin` class.

#### Method 1: OAuth Flow
```python
from dhanhq import DhanLogin

dhan_login = DhanLogin("YOUR_CLIENT_ID")
app_id = "YOUR_APP_ID"
app_secret = "YOUR_APP_SECRET"

# Step 1: Generate Consent and Open Browser for Login
consent_id = dhan_login.generate_login_session(app_id, app_secret)

# Step 2: Consume Token ID (After user logs in and gets Token ID from redirect URL)
token_id = "TOKEN_ID_FROM_REDIRECT_URL"
access_token = dhan_login.consume_token_id(token_id, app_id, app_secret)
print(access_token)
```

#### Method 2: PIN & TOTP Flow
```python
from dhanhq import DhanLogin

dhan_login = DhanLogin("YOUR_CLIENT_ID")
pin = "YOUR_PIN"
totp = "YOUR_TOTP"

access_token_data = dhan_login.generate_token(pin, totp)
print(access_token_data)
```

#### Renew Token
``` python
dhan_login.renew_token(access_token)
```

#### User Profile
``` python
# Check validity of access token and account setup
user_info = dhan_login.user_profile(access_token)
print(user_info)
```

### IP Management
You can manage your Static IP (whitelisting) using `set_ip`, `modify_ip`, and `get_ip`.
```python
# Set Primary IP
response = dhan_login.set_ip(access_token, "10.200.10.10", "PRIMARY")
print(response)
# Modify Primary IP
response = dhan_login.modify_ip(access_token, "10.200.10.11", "PRIMARY")
print(response)
# Get Configured IPs
ip_list = dhan_login.get_ip(access_token)
print(ip_list)
```

### Hands-on API

```python
from dhanhq import DhanContext, dhanhq

dhan_context = DhanContext("client_id","access_token")
dhan = dhanhq(dhan_context)

# Place an order for Equity Cash
dhan.place_order(security_id='1333',            # HDFC Bank
    exchange_segment=dhan.NSE,
    transaction_type=dhan.BUY,
    quantity=10,
    order_type=dhan.MARKET,
    product_type=dhan.INTRA,
    price=0)
    
# Place an order for NSE Futures & Options
dhan.place_order(security_id='52175',           # Nifty PE
    exchange_segment=dhan.NSE_FNO,
    transaction_type=dhan.BUY,
    quantity=550,
    order_type=dhan.MARKET,
    product_type=dhan.INTRA,
    price=0)
  
# Fetch all orders
dhan.get_order_list()

# Get order by id
dhan.get_order_by_id(order_id)

# Modify order
dhan.modify_order(order_id, order_type, leg_name, quantity, price, trigger_price, disclosed_quantity, validity)

# Cancel order
dhan.cancel_order(order_id)

# Get order by correlation id
dhan.get_order_by_correlationID(correlationID)

# Get Instrument List
dhan.fetch_security_list("compact")

# Get positions
dhan.get_positions()

# Get holdings
dhan.get_holdings()

# Intraday Minute Data 
dhan.intraday_minute_data(security_id, exchange_segment, instrument_type, from_date, to_date)

# Historical Daily Data
dhan.historical_daily_data(security_id, exchange_segment, instrument_type, from_date, to_date)

# Expired Options Data
dhan.expired_options_data(
    security_id=13,
    exchange_segment="NSE_FNO",
    instrument_type="INDEX",
    expiry_flag="MONTH",
    expiry_code=1,
    strike="ATM",
    drv_option_type="CALL",
    required_data=["open", "high", "low", "close", "volume"],
    from_date="2023-01-01",
    to_date="2023-01-31"
)

# Time Converter
dhan.convert_to_date_time(epoch_date)

# Get trade book
dhan.get_trade_book(order_id)

# Get trade history
dhan.get_trade_history(from_date,to_date,page_number=0)

# Get fund limits
dhan.get_fund_limits()

# Generate TPIN
dhan.generate_tpin()

# Enter TPIN in Form
dhan.open_browser_for_tpin(isin='INE00IN01015',
    qty=1,
    exchange='NSE')

# EDIS Status and Inquiry
dhan.edis_inquiry(isin='INE00IN01015')

# Expiry List of Underlying
dhan.expiry_list(
    under_security_id=13,                       # Nifty
    under_exchange_segment="IDX_I"
)

# Option Chain
dhan.option_chain(
    under_security_id=13,                       # Nifty
    under_exchange_segment="IDX_I",
    expiry="2024-10-31"
)

# Market Quote Data                     # LTP - ticker_data, OHLC - ohlc_data, Full Packet - quote_data
dhan.ohlc_data(
    securities = {"NSE_EQ":[1333]}
)

# Place Forever Order (SINGLE)
dhan.place_forever(
    security_id="1333",
    exchange_segment= dhan.NSE,
    transaction_type= dhan.BUY,
    order_type=dhan.LIMIT,
    product_type=dhan.CNC,
    quantity= 10,
    price= 1900,
    trigger_Price= 1950
)

# Place a Conditional Order (triggers orders when condition is met; Equities & Indices only)
dhan.place_conditional_order(
    condition={
        "comparisonType": "PRICE_WITH_VALUE",
        "exchangeSegment": dhan.NSE,
        "securityId": "1333",
        "operator": "GREATER_THAN",
        "comparingValue": 250,
        "frequency": "ONCE"                 # ONCE or ALWAYS
    },
    orders=[{
        "transactionType": dhan.BUY,
        "exchangeSegment": dhan.NSE,
        "productType": dhan.CNC,
        "orderType": dhan.LIMIT,
        "securityId": "1333",
        "quantity": 10,
        "validity": dhan.DAY,
        "price": "250.00"
    }]
)
dhan.get_conditional_orders()
dhan.cancel_conditional_order("12345")

# Global Stocks (US) - prices in USD
dhan.place_global_order(
    security_id="AAPL_SECURITY_ID",
    transaction_type=dhan.BUY,
    order_type=dhan.LIMIT,
    quantity=5,
    price=150.50
)
dhan.get_global_holdings()
dhan.get_global_fund_limit()
dhan.get_global_market_status()

# Fetch the Global Stocks (US) instrument list (distinct from the Indian list)
dhan.fetch_global_security_list()

# P&L based Exit (values are absolute amounts, not percentages)
dhan.set_pnl_exit(profit_value=1500, loss_value=500,
    product_type=["INTRADAY", "DELIVERY"], enable_kill_switch=True)
dhan.get_pnl_exit()
dhan.stop_pnl_exit()

# Multi-leg Margin Calculator
dhan.margin_calculator_multi(
    scrip_list=[
        {"securityId": "26009", "exchangeSegment": dhan.NSE_FNO, "transactionType": dhan.BUY,
         "quantity": 50, "productType": dhan.INTRA, "price": 45000.00},
        {"securityId": "26010", "exchangeSegment": dhan.NSE_FNO, "transactionType": dhan.SELL,
         "quantity": 50, "productType": dhan.INTRA, "price": 45500.00}
    ]
)
```

### Market Feed Usage
```python
from dhanhq import DhanContext, MarketFeed

# Define and use your dhan_context if you haven't already done so like below:
dhan_context = DhanContext("client_id","access_token")

# Structure for subscribing is (exchange_segment, "security_id", subscription_type)

instruments = [(MarketFeed.NSE, "1333", MarketFeed.Ticker),   # Ticker - Ticker Data
    (MarketFeed.NSE, "1333", MarketFeed.Quote),     # Quote - Quote Data
    (MarketFeed.NSE, "1333", MarketFeed.Full),      # Full - Full Packet
    (MarketFeed.NSE, "11915", MarketFeed.Ticker),
    (MarketFeed.NSE, "11915", MarketFeed.Full)]

version = "v2"          # Mention Version and set to latest version 'v2'

# In case subscription_type is left as blank, by default Ticker mode will be subscribed.

try:
    data = MarketFeed(dhan_context, instruments, version)
    data.run_forever()
    
    while True:
        response = data.get_data()
        print(response)

except Exception as e:
    print(e)
```

```
# Close Connection
data.close_connection()

# Subscribe instruments while connection is open
sub_instruments = [(MarketFeed.NSE, "14436", MarketFeed.Ticker)]

data.subscribe_symbols(sub_instruments)

# Unsubscribe instruments which are already active on connection
unsub_instruments = [(MarketFeed.NSE, "1333", 16)]

data.unsubscribe_symbols(unsub_instruments)
```

### Global Stocks Live Feed Usage
```python
from dhanhq import DhanContext, GlobalStocksFeed

# Define and use your dhan_context if you haven't already done so like below:
dhan_context = DhanContext("client_id","access_token")

# Structure for subscribing is (exchange_segment, "security_id", request_code)
# request_code is GlobalStocksFeed.SubscribeTrade (15) or GlobalStocksFeed.SubscribeOHLC (17).
# A 2-tuple defaults to the Trade feed.
instruments = [
    (GlobalStocksFeed.INX_EQ, "1234"),                                  # Trade
    (GlobalStocksFeed.INX_EQ, "5678", GlobalStocksFeed.SubscribeOHLC),  # OHLC
]

try:
    feed = GlobalStocksFeed(dhan_context, instruments, auth_type=GlobalStocksFeed.AUTH_SELF)
    feed.run_forever()

    while True:
        response = feed.get_data()
        print(response)

except Exception as e:
    print(e)
```

### Live Order Update Usage
```python
from dhanhq import DhanContext, OrderUpdate
import time

# Define and use your dhan_context if you haven't already done so like below:
dhan_context = DhanContext("client_id","access_token")

def on_order_update(order_data: dict):
    """Optional callback function to process order data"""
    print(order_data["Data"])

def run_order_update():
    order_client = OrderUpdate(dhan_context)

    # Optional: Attach a callback function to receive and process order data.
    order_client.on_update = on_order_update

    while True:
        try:
            order_client.connect_to_dhan_websocket_sync()
        except Exception as e:
            print(f"Error connecting to Dhan WebSocket: {e}. Reconnecting in 5 seconds...")
            time.sleep(5)

run_order_update()
```

### Full Market Depth
```python
from dhanhq import DhanContext, FullDepth

dhan_context = DhanContext(client_id, access_token)

instruments = [(1, "1333")]                     #[(1, "1333"),(2,"")] for 20 depth, upto 50 instruments
depth_level = 200                               # 20 or 200, default 20 in case this is not passed

try:
    response = FullDepth(dhan_context, instruments, depth_level)          #depth_level is non mandatory for 20 depth
    response.run_forever()
    
    while True:
        response.get_data()
        
        if response.on_close:
            print("Server disconnection detected. Kindly try again.")
            break

except Exception as e:
    print(e)

```

## Changelog

[Check release notes](https://github.com/dhan-oss/DhanHQ-py/releases)

### Core Implementation Code & Architecture
#### File: `tests/data/a-template-response.json`
```python
{
  "status": "success",
  "remarks": "",
  "data": {}
}
```

#### File: `tests/data/convert_position.json`
```python
{
  "status": "success",
  "remarks": "",
  "data": {}
}
```

#### File: `tests/data/expired_options_data.json`
```python
{
    "status": "success",
    "remarks": "",
    "data": {}
}
```

#### File: `tests/data/historical_daily_data.json`
```python
{
    "status": "success",
    "remarks": "",
    "data": {}
}
```

#### File: `tests/data/intraday_minute_data.json`
```python
{
    "status": "success",
    "remarks": "",
    "data": {}
}
```

#### File: `tests/data/cancel_given_order.json`
```python
{
  "status": "success",
  "remarks": "",
  "data": {
    "orderId": "string",
    "orderStatus": "TRANSIT"
  }
}
```


==================================================
