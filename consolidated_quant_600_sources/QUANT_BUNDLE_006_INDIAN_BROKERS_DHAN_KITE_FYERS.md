# ⚡ [QUANT-SOURCE-006] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_006_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: india-stocks-api (`VAULT_IN-QUANT-057_Apurv-Salunke__india-stocks-api`)
- **Full Name**: `IN-QUANT-057_Apurv-Salunke__india-stocks-api`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# India Stocks API v2.0

Type-safe Python client for Indian brokers with canonical responses and auto-provisioned instruments.

## What this solves
- Single, typed surface for orders, market data, history, streaming, funds, profile.
- Auto-downloads and normalizes the instruments DB; you always code with NSE-style symbols.
- Canonical response objects so downstream code stays broker-agnostic.

## Supported today
- Broker: Angel One (live). Zerodha in progress.
- Python: 3.10, 3.11, 3.12.
- CI: ruff, mypy, unit tests. Integration tests are opt-in (require creds).

## Install
```bash
git clone https://github.com/Apurv-Salunke/india-stocks-api.git
cd india-stocks-api
poetry install
# or: pip install india-stocks-api
```

## Quick start
```python
from india_stocks_api.brokers import AngelOne
from india_stocks_api.constants import TransactionType, OrderType, StreamMode
from india_stocks_api.instruments import Equity

broker = AngelOne(api_key, client_code, password, totp_key)
broker.authenticate()

# Market data (canonical QuoteResponse)
quote = broker.get_quote(Equity("RELIANCE"))
print("LTP:", quote.ltp)

# Place order
broker.place_order(
    instrument=Equity("RELIANCE"),
    transaction_type=TransactionType.BUY,
    quantity=1,
    order_type=OrderType.MARKET,
)

# Streaming (canonical WebSocketTick)
broker.on_tick = lambda tick: print("tick", tick.symbol, tick.ltp)
broker.subscribe([Equity("RELIANCE")], mode=StreamMode.QUOTE)
broker.start_streaming()  # blocking; run in a thread if needed
```

## Canonical responses
Returned from `india_stocks_api.responses`:
- **Market data:** `QuoteResponse`, `DepthResponse`, `HistoryResponse`
- **Account:** `FundsResponse`, `ProfileResponse`
- **Orders:** `OrderResponse`, `Order`, `Position`, `Holding`, `Trade`
- **Streaming:** `WebSocketTick` (normalized depth levels)

## Streaming behavior (Angel One)
- Subscriptions are buffered; sent on connect.
- Reconnects auto-resubscribe via SmartWebSocketV2; adapter maps frames → `WebSocketTick`.
- `unsubscribe(...)` and `stop_streaming()` are idempotent.

## Architecture (short)
1. Public adapter (`brokers/angel.py`) exposes typed methods and maps to canonical responses.
2. Shim (`internal/context.py`) supplies auth, symbols, HTTP to ported OpenAlgo code.
3. Ported internals (`internal/angel/*`) stay close to upstream for easier syncs.

## Testing

```bash
# Unit tests
poetry run pytest tests/unit/ -v

# Lint + type check
poetry run ruff check .
poetry run ruff format --check .
poetry run mypy india_stocks_api/

# Integration tests (require live Angel creds in .env)
# .env must contain: ANGEL_API_KEY, ANGEL_CLIENT_ID, ANGEL_PIN, ANGEL_TOTP_SECRET
poetry run pytest tests/integration/test_angel_auth_live.py -v
poetry run pytest tests/integration/test_data_methods_live.py -v
```

> **Note:** Run integration test files individually, not together — Angel's TOTP
> rate-limits duplicate auth calls within the same 30-second window.

## Publishing

Builds are managed with Poetry. The package is published as `india-stocks-api` on PyPI.

```bash
# Build sdist + wheel
poetry build

# Publish to TestPyPI (for verification before production release)
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi <your-test-pypi-token>
poetry publish --repository testpypi

# Install from TestPyPI to verify
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple/ \
            india-stocks-api==<version>

# Publish to production PyPI
poetry publish
```

TestPyPI tokens are separate from PyPI tokens. Generate one at
https://test.pypi.org/manage/account/token/.

## Contributing
- Install hooks: `pre-commit install`
- Before push: run unit tests + ruff + mypy.
- PRs target `dev`; include what changed, tests run, and any live-cred needs.

## Docs
A dedicated docs site is planned. Until then, this README + `tests/` and `internal/` act as reference.

### Core Implementation Code & Architecture
#### File: `india_stocks_api/internal/__init__.py`
```python

```

#### File: `india_stocks_api/internal/angel/api/__init__.py`
```python

```

#### File: `tests/__init__.py`
```python

```

#### File: `tests/unit/__init__.py`
```python

```

#### File: `tests/integration/__init__.py`
```python

```

#### File: `india_stocks_api/brokers/__init__.py`
```python
from .angel import AngelOne
from .base import BaseBroker

__all__ = ["BaseBroker", "AngelOne"]
```


==================================================


## [2/3] Repository: nsemine (`VAULT_IN-QUANT-058_kbizme__nsemine`)
- **Full Name**: `IN-QUANT-058_kbizme__nsemine`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
## Simplest, Cleanest and Efficient Python Library to Scrape Stocks, FnO & Indices Data From The NSEIndia(New) and NiftyIndices Website.

`nsemine` is a Python library designed to provide a clean and straightforward interface for scraping data from the National Stock Exchange of India (NSE) and the Nifty Indices website. It aims to simplify the process of retrieving various market data, including indices, stock information, futures & options data, and general NSE-related utilities. This library is built to be efficient and user-friendly, catering to **developers**, **traders**, **investors** who need reliable NSE data for financial analysis, algorithmic trading, and data visualization.

## Features

* **Asynchronous Data Retrieval:**  &nbsp;Experience non-blocking, asynchronous data retrieval for optimal performance. Leverage the power of `asyncio` to fetch market data without delays, ensuring your applications remain responsive.

* **High-Speed Data Acquisition:**  &nbsp;Utilize the speed and efficiency of `aiohttp` and `requests` under the hood. This library is designed for rapid data acquisition, enabling you to get the latest market insights quickly.

* **Unparalleled Data Flexibility:** &nbsp; `nsemine` empowers you with the complete data manipulation. Choose between the raw, unfiltered API response for maximum customization, OR leverage our intelligently processed data structures for streamlined analysis and immediate insights.

* **Intelligent Built-in Caching:**  &nbsp;Minimize API requests with the intelligent built-in caching mechanism. Reduce your reliance on the NSE API and save you from getting blocked by the NSE Anti-Scraper Robots.

* **Clean and Intuitive API:**  &nbsp;Designed for simplicity and ease of use, the library provides a clean and intuitive API, allowing developers to quickly integrate NSE data into their projects.

* **Comprehensive Data Coverage:**  &nbsp;Access a wide range of NSE data, including indices, stocks, futures, and options, all within a single, unified library.

* **Robust Error Handling:**  &nbsp;Built with robust error handling to ensure your applications remain stable and resilient, even in challenging network conditions.

## Installation

You can install `nsemine` by pip or via github.

>  ``pip install nsemine``

OR

>``pip install git+https://github.com/kbizme/nsemine.git``

## Why I Built This Library

Well, there are several Python libraries available for scraping NSE data, I developed this library to address specific needs that were not adequately met by the existing solutions. I have used this library in my project. You can use it in yours.

* **Custom Data Requirements:**  &nbsp;&nbsp;``nsemine`` is tailored to retrieve specific data points and formats that were essential for the project, which may not be available in other libraries.

*  **Unique Data Structures:** The project required data in a particular structure and format, which this library delivers directly, eliminating the need for extensive post-processing.

* **Data Availability:**&nbsp;&nbsp;  ``nsemine`` is designed to access and provide data that may not be available or easily accessible through other existing NSE scraping libraries.

* **Performance and Reliability:** Optimized for speed and stability, ensuring reliable data retrieval, especially for real-time and high-frequency data. It uses ``numpy`` and ``pandas`` vectorized operations for faster data pre-processing. Most of the possible errors are handled with Exceptions, thus, even if any error occurs the application will remain stable.

* **Ease of Use:**  &nbsp;&nbsp;``nsemine`` aims to provide a simple and intuitive interface, making it easy for developers to integrate NSE data into their applications. This library is designed to offer a more specialized and efficient solution for users who require precise and customized NSE data.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes, feature requests, or improvements.

## Documentation

_Work in progress..._ Meanwhile, you may explore the library. ReadTheDocs style documentation will be added upon complete library build.

Basic Usage Example:
`from nsemine import nse, live, historical, fno`

1. get live stock and index quotes
 - quotes = `live.get_stock_live_quotes(stock_symbol='TCS')`
 - index_quote = `live.get_index_live_price(index='NIFTY 50')`

2. You can download stock and index historical data from the `historical` module.
3. NSE related any data is available on the `nse` module.
4. FNO related data functions are available on `fno` module [in development].

TIP:  You may get all the available function in each modules, by using a dot afte the module name, like this -> live.   or -> nse.   [Your IDE may highlight all the available functions, all functions contains comprehensive docstring]
This is a workaround while the full documentation is ready.

## WARNING

Still in Maturing phase, so expect frequent updates..

# Documentation

Basic import:

```python
from datetime import datetime
from nsemine import live, historical, nse, fno
```

## Module 1:  `live.py` 

#### `get_stock_live_quotes(stock_symbol: str, series: str | None = None, raw: bool = False)`

Fetches the live quote for a stock symbol.

- `stock_symbol`: NSE stock symbol, such as `"TCS"` or `"INFY"`.
- `series`: NSE series to query. Defaults to `"EQ"` when not provided.
- `raw`: When `True`, returns the raw NSE JSON response. When `False`, returns a cleaned dictionary.
- Returns: `dict` for quote data, or `None` if the request or processing fails.

Example:

```python
quote = live.get_stock_live_quotes("TCS")
raw_quote = live.get_stock_live_quotes("TCS", raw=True)
```

#### `get_index_live_price(index: str = "NIFTY 50", raw: bool = False)`

Fetches live price data for a single NSE index.

- `index`: Index name, such as `"NIFTY 50"` or `"NIFTY BANK"`.
- `raw`: When `True`, returns the raw index watch JSON response.
- Returns: a dictionary with `symbol`, `open`, `high`, `low`, `close`, `previous_close`, `change`, `changepct`, `year_high`, `year_low`, and sometimes `datetime`; returns `None` if the index is not found or an error occurs.

Example:

```python
nifty = live.get_index_live_price()
bank_nifty_raw = live.get_index_live_price("NIFTY BANK", raw=True)
```

#### `get_all_indices_live_snapshot(raw: bool = False)`

Fetches a live snapshot of all available NSE indices.

- `raw`: When `True`, returns the raw JSON response.
- Returns: a `pandas.DataFrame` with columns including `key`, `index`, `symbol`, `open`, `high`, `low`, `close`, `previous_close`, `change`, `changepct`, `year_high`, `year_low`, `advances`, `declines`, `unchanged`, `one_week_ago`, `one_month_ago`, and `one_year_ago`; returns `None` on failure.
- Note: processed output drops rows containing missing values.

Example:

```python
indices = live.get_all_indices_live_snapshot()
```

#### `get_all_securities_live_snapshot(series: str | list | None = None, raw: bool = False)`

Fetches a live snapshot for all NSE securities.

- `series`: Optional series filter, such as `"EQ"` or `["EQ", "SM"]`.
- `raw`: When `True`, returns the raw JSON response.
- Returns: a `pandas.DataFrame` with `symbol`, `series`, `close`, `previous_close`, `change`, `changepct`, `volume`, `traded_value`, and `market_cap`; returns `None` on failure.
- Note: processed `volume`, `traded_value`, and `market_cap` are scaled to absolute values.

Example:

```python
all_securities = live.get_all_securities_live_snapshot()
eq_securities = live.get_all_securities_live_snapshot(series="EQ")
```

#### `get_index_constituents_live_snapshot(index: str = "NIFTY 50", raw: bool = False)`

Fetches live constituent data for an NSE index.

- `index`: Index name, such as `"NIFTY 50"`, `"NIFTY BANK"`, or `"NIFTY NEXT 50"`.
- `raw`: When `True`, returns the raw JSON response.
- Returns: a `pandas.DataFrame` with `symbol`, `ltp`, `previous_close`, `change`, `changepct`, `weightage`, `volume`, and `turnover`; returns `None` on failure.
- Note: NSE-provided `volume` and `turnover` units are preserved.

Example:

```python
constituents = live.get_index_constituents_live_snapshot("NIFTY 50")
```

#### `get_fno_indices_live_snapshot(df: bool = True)`

Fetches live data for the NSE F&O indices.

- `df`: When `True`, returns a `pandas.DataFrame`. When `False`, returns a dictionary keyed by derivative symbols such as `NIFTY`, `BANKNIFTY`, `FINNIFTY`, `MIDCPNIFTY`, and `NIFTYNXT50`.
- Returns: index snapshot data with `datetime`, `open`, `high`, `low`, `close`, `previous_close`, `change`, `changepct`, `year_high`, and `year_low`; returns `None` on failure.

Example:

```python
fno_indices = live.get_fno_indices_live_snapshot()
fno_indices_dict = live.get_fno_indices_live_snapshot(df=False)
```

#### `get_stock_intraday_tick_by_tick_data(stock_symbol: str, candle_interval: int | None = None, raw: bool = False)`

Fetches current-day intraday tick data for a stock and can convert it into OHLC candles.

- `stock_symbol`: NSE stock symbol.
- `candle_interval`: Optional candle interval in minutes. If omitted, tick data is returned.
- `raw`: When `True` and `candle_interval` is not provided, returns the raw JSON response.
- Returns: a tick `pandas.DataFrame`, an OHLC `pandas.DataFrame` when `candle_interval` is provided, raw JSON when requested, or `None` on failure.

Example:

```python
ticks = live.get_stock_intraday_tick_by_tick_data("INFY")
five_minute = live.get_stock_intraday_tick_by_tick_data("INFY", candle_interval=5)
```

## Module 2: `historical.py`

#### `get_stock_historical_data(stock_symbol: str, start_datetime: datetime, end_datetime: datetime = datetime.now(), interval: int | str = 1, raw: bool = False)`

Fetches historical chart data for an equity symbol.

- `stock_symbol`: NSE stock symbol.
- `start_datetime`: Start of the requested period.
- `end_datetime`: End of the requested period. Defaults to the time at module import.
- `interval`: Intraday interval in minutes, or `"D"`, `"W"`, or `"M"` for daily, weekly, or monthly data.
- `raw`: When `True`, returns the raw chart API response.
- Returns: a processed `pandas.DataFrame`, raw dictionary, or `None` on failure.

Example:

```python
df = historical.get_stock_historical_data("TCS", datetime(2025, 1, 1), interval="D")
```

#### `get_index_historical_data(index: str, start_datetime: datetime, end_datetime: datetime = datetime.now(), interval: int | str = "3", raw: bool = False)`

Fetches historical chart data for an NSE index.

- `index`: Index name, such as `"NIFTY 50"` or `"NIFTY BANK"`.
- `start_datetime`: Start of the requested period.
- `end_datetime`: End of the requested period. Defaults to the time at module import.
- `interval`: Intraday interval in minutes, or `"D"`, `"W"`, or `"M"` for daily, weekly, or monthly data.
- `raw`: When `True`, returns the raw chart API response.
- Returns: a processed `pandas.DataFrame`, raw dictionary, or `None` on failure.

Example:

```python
df = historical.get_index_historical_data("NIFTY 50", datetime(2025, 1, 1), interval="D")
```

## Module 3: `nse.py`

#### `get_market_status(market_name: str | None = None)`

Fetches current NSE market status.

- `market_name`: Optional market code. Supported shortcuts include `CM`, `CUR`, `COM`, `DB`, and `CURF`.
- Returns: raw market status list when no market is supplied, `True` or `False` for a matched market, the raw list when no shortcut matches, or `None` on failure.

Example:

```python
status = nse.get_market_status()
is_cm_open = nse.get_market_status("CM")
```

#### `get_market_stats()`

Fetches NSE market statistics such as yearly highs/lows, circuit-breaker counts, and positive/negative stock counts.

- Returns: a dictionary containing market statistics with `asOnDate` converted to `datetime`, or `None` on failure.

#### `get_holiday_lists()`

Fetches NSE capital market holidays.

- Returns: a `pandas.DataFrame` with `date`, `day`, and `description`, or `None` on failure.

#### `get_all_indices_list()`

Fetches the list of available NSE indices.

- Returns: a `pandas.DataFrame` with `trading_index` and `full_name`, or `None` on failure.

#### `get_all_equities_list(raw: bool = False)`

Fetches the NSE equity master list.

- `raw`: When `True`, returns the raw CSV-loaded DataFrame.
- Returns: a processed `pandas.DataFrame` with `symbol`, `name`, `series`, `date_of_listing`, `isin_number`, and `face_value`, or `None` on failure.

#### `get_all_sme_stocks_list(raw: bool = False)`

Fetches NSE SME-listed securities.

- `raw`: When `True`, returns the raw CSV-loaded DataFrame.
- Returns: a processed `pandas.DataFrame` with `symbol`, `name`, `series`, `date_of_listing`, `isin_number`, and `face_value`, or `None` on failure.

#### `get_fno_stocks_lists(raw: bool = False)`

Fetches NSE F&O underlying stock symbols.

- `raw`: When `True`, returns the raw JSON response.
- Returns: a `pandas.DataFrame` with `name` and `symbol`, or `None` on failure.

#### `get_pre_open_data(key: str = "NIFTY", raw: bool = False)`

Fetches NSE pre-open market data.

- `key`: Pre-open group key, such as `"NIFTY"`, `"BANKNIFTY"`, `"SME"`, `"FO"`, `"OTHERS"`, or `"ALL"`.
- `raw`: When `True`, returns the raw JSON response.
- Returns: a `pandas.DataFrame` with `datetime`, `symbol`, `previous_close`, `close`, `change`, `changepct`, `volume`, `turnover`, `market_cap`, `year_high`, and `year_low`, or `None` on failure.

#### `get_securities_at_52_weeks_high(raw: bool = False, need_timestamp: bool = False)`

Fetches securities trading at a 52-week high.

- `raw`: When `True`, returns the raw JSON response.
- `need_timestamp`: When `True`, returns `(df, timestamp)`.
- Returns: a `pandas.DataFrame`, `(DataFrame, datetime)`, raw dictionary, or `None`.

#### `get_securities_at_52_weeks_low(raw: bool = False, need_timestamp: bool = False)`

Fetches securities trading at a 52-week low.

- `raw`: When `True`, returns the raw JSON response.
- `need_timestamp`: When `True`, returns `(df, timestamp)`.
- Returns: a `pandas.DataFrame`, `(DataFrame, datetime)`, raw dictionary, or `None`.

#### `get_securities_above_previous_close(raw: bool = False, need_timestamp: bool = False)`

Fetches securities currently trading above their previous close.

- `raw`: When `True`, returns the raw JSON response.
- `need_timestamp`: When `True`, returns `(df, timestamp)`.
- Returns: a processed `pandas.DataFrame`, `(DataFrame, datetime)`, raw dictionary, or `None`.

#### `get_securities_below_previous_close(raw: bool = False, need_timestamp: bool = False)`

Fetches securities currently trading below their previous close.

- `raw`: When `True`, returns the raw JSON response.
- `need_timestamp`: When `True`, returns `(df, timestamp)`.
- Returns: a processed `pandas.DataFrame`, `(DataFrame, datetime)`, raw dictionary, or `None`.

#### `get_securities_same_as_previous_close(raw: bool = False, need_timestamp: bool = False)`

Fetches securities currently trading at the same price as their previous close.

- `raw`: When `True`, returns the raw JSON response.
- `need_timestamp`: When `True`, returns `(df, timestamp)`.
- Returns: a processed `pandas.DataFrame`, `(DataFrame, datetime)`, raw dictionary, or `None`.

#### `get_most_liquid_stocks(raw: bool = False)`

Fetches the top 20 NSE stocks by traded volume.

- `raw`: When `True`, returns the raw JSON response.
- Returns: a `pandas.DataFrame` with `datetime`, `symbol`, `open`, `high`, `low`, `close`, `previous_close`, `change`, `changepct`, `volume`, `traded_value`, `year_high`, and `year_low`, or `None`.

#### `get_most_value_traded_stocks(raw: bool = False)`

Fetches the top 20 NSE stocks by traded value.

- `raw`: When `True`, returns the raw JSON response.
- Returns: a `pandas.DataFrame` with `datetime`, `symbol`, `open`, `high`, `low`, `close`, `previous_close`, `change`, `changepct`, `volume`, `traded_value`, `year_high`, and `year_low`, or `None`.

#### `get_todays_gainers(key: str = "ALL", raw: bool = False)`

Fetches top gainers for the current trading session.

- `key`: Group selector. Supported values include `ALL`, `NIFTY`, `NIFTYNEXT50`, `NIFTYNXT50`, `BANKNIFTY`, `FNO`, `GT20`, and `LT20`.
- `raw`: When `True`, returns the raw JSON response.
- Returns: a processed movers `pandas.DataFrame`, or `None` on failure.

#### `get_todays_losers(key: str = "ALL", raw: bool = False)`

Fetches top losers for the current trading session.

- `key`: Group selector. Supported values include `ALL`, `NIFTY`, `NIFTYNEXT50`, `NIFTYNXT50`, `BANKNIFTY`, `FNO`, `GT20`, and `LT20`.
- `raw`: When `True`, returns the raw JSON response.
- Returns: a processed movers `pandas.DataFrame`, or `None` on failure.

## Module 4: `fno.py` [WIP]

#### `get_oi_spurts(raw: bool = False, sentiment_analysis: bool = True)`

Fetches NSE open-interest spurt data.

- `raw`: When `True`, returns the raw JSON response.
- `sentiment_analysis`: When `True`, merges OI data with NIFTY 500 live constituent prices and adds `market_action` and `interpretation`.
- Returns: a `pandas.DataFrame`, raw dictionary, or `None` on failure.
- Sentiment labels include `Long Buildup`, `Short Buildup`, `Short Covering`, `Long Unwinding`, and `Neutral`.

Example:

```python
oi = fno.get_oi_spurts()
oi_without_sentiment = fno.get_oi_spurts(sentiment_analysis=False)
```

#### `get_stock_option_details(symbol: str, only_expiry: bool = False, only_strikes: bool = False, raw: bool = False)`

Fetches available stock option expiry dates and strike prices for a symbol.

- `symbol`: F&O stock symbol, such as `"TCS"` or `"AUBANK"`.
- `only_expiry`: When `True`, returns only available expiry dates as `datetime.date` values.
- `only_strikes`: When `True`, returns only available strike prices as integers.
- `raw`: When `True`, returns the raw JSON response.
- Returns: a dictionary containing `expiry_dates` and `strike_prices`, a list of expiry dates, a list of strike prices, raw dictionary, or `None`.

Example:

```python
details = fno.get_stock_option_details("TCS")
expiries = fno.get_stock_option_details("TCS", only_expiry=True)
strikes = fno.get_stock_option_details("TCS", only_strikes=True)
```

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `nsemine/bin/__init__.py`
```python

```

#### File: `nsemine/utilities/__init__.py`
```python

```

#### File: `nsemine/__init__.py`
```python
from nsemine import generic, historical, live, fno, nse
```

#### File: `playground.py`
```python
from nsemine import live, nse
from nsemine.utilities import urls
import requests, random

x = urls.get_nse_headers()
print(x)

x = live.get_stock_live_quotes('TCS')
print(x)
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "nsemine"
version = "1.6"
authors = [
    { name = "kbizme", email = "kbhowmik.eduz@gmail.com" }
]

maintainers = [
    { name = "kbizme", email = "kbhowmik.eduz@gmail.com" },
]

description = "Efficient and Reliable Python Library for Scraping Real-Time and Historical Data of Stocks, Futures, Options and Indices From The NSE Exchange."
keywords = ["nse", "nsemine", "indian stock data", "stock market", "financial data", "scraping", "indices", 
"stocks", "futures", "options", "trading", "investment", "nse exchange", "nifty data", "nse scrapers", "stock data", "nse python library"]
readme = "README.md"
requires-python = ">=3.6"  
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Office/Business :: Financial",
    "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    "Topic :: Software Development :: Libraries",
    "Intended Audience :: Developers",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Education",
]

license = "MIT"

dependencies = [
    "aiohttp",
    "asyncio",
    "certifi",
    "charset-normalizer",
    "idna",
    "numpy",
    "pandas",
    "python-dateutil",
    "pytz",
    "requests",
    "six",
    "tzdata",
    "urllib3",
    "brotli",
    "zstandard",
    "yarl",
]


[tool.setuptools]
packages = ["nsemine", "nsemine.bin", "nsemine.utilities"]

[project.urls]
"Homepage" = "https://github.com/kbizme/nsemine"
"Bug Tracker" = "https://github.com/kbizme/nsemine/issues"
```


==================================================


## [3/3] Repository: nse-rs (`VAULT_IN-QUANT-059_ratan00__nse-rs`)
- **Full Name**: `IN-QUANT-059_ratan00__nse-rs`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<p align="center">
  <img src="assets/banner.png" alt="nse-rs banner" width="90%" />
</p>

<p align="center">
  <a href="https://github.com/ratan00/nse-rs"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License" /></a>
  <img src="https://img.shields.io/badge/Rust-1.75%2B-orange.svg" alt="Rust Version" />
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" />
</p>

# nse-rs

An async Rust library for fetching live market data from the National Stock Exchange of India (NSE) — no API key or account required.

Provides live equity quotes, index quotes, structured option chains, futures, intraday & historical candles, polling feed loops, and EOD bhavcopy archives.

---

## Features

- **Live equity quotes** — flat `NseQuote` with LTP, OHLCV, change, volume
- **Live index quotes** — NIFTY 50, NIFTY BANK, FINNIFTY etc. via `get_index_quote()`
- **Structured option chain** — `OptionChain` grouped by expiry date → strike → CE/PE
- **Futures** — all contracts for a symbol filtered from derivatives
- **Historical candles** — 1/3/5/15/30/60 min intraday (30-day window) or D/W/M (25+ years)
- **Polling feed** — `poll_quote()` and `poll_index()` loops for simulated live streaming
- **EOD bhavcopy** — equity and F&O archives parsed into typed structs
- **Script token cache** — symbol → charting token cached in memory; no double-requests
- **Auto session retry** — cookie refresh on 403/decode failures, disk-cached for 1 hour
- **No OpenSSL** — uses `rustls-tls-native-roots`; cross-compiles cleanly

---

## Installation

```toml
[dependencies]
nse-rs = { git = "https://github.com/ratan00/nse-rs.git" }
tokio  = { version = "1", features = ["full"] }
chrono = "0.4"
```

---

## Quick Start

```rust
use nse_rs::NseClient;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = NseClient::new();
    client.init_session().await?;

    // Flat live quote
    let quote = client.get_stock_quote("RELIANCE").await?;
    println!("{}: LTP ₹{:.2}  vol {}", quote.symbol, quote.ltp, quote.volume);

    // Index spot price
    let nifty = client.get_index_quote("NIFTY 50").await?;
    println!("NIFTY 50: {:.2}  ({:+.2}%)", nifty.last, nifty.change_pct);

    // Structured option chain
    let chain = client.get_option_chain("NIFTY").await?;
    for (expiry, rows) in &chain.expiries {
        println!("=== {} ===", expiry);
        for row in rows.iter().take(3) {
            println!("  {:>8.0}  CE {:.2}  PE {:.2}",
                row.strike, row.ce.ltp, row.pe.ltp);
        }
    }

    Ok(())
}
```

---

## API Reference

### `NseClient`

Create with `NseClient::new()`, then call `init_session().await?` before any data fetch.

#### Live data

| Method | Returns | Description |
|---|---|---|
| `get_stock_quote(symbol)` | `NseQuote` | Flat live quote for an equity (e.g. `"SBIN"`) |
| `get_index_quote(index_name)` | `NseIndexQuote` | Spot for an index (e.g. `"NIFTY 50"`, `"NIFTY BANK"`) |
| `get_option_chain(symbol)` | `OptionChain` | All options grouped by expiry/strike with CE+PE |
| `get_futures(symbol)` | `Vec<DerivativeContract>` | All futures contracts |
| `get_option_contracts(symbol)` | `Vec<DerivativeContract>` | Raw option contracts (unstructured) |
| `get_derivatives_quote(symbol)` | `NextApiDerivativesResponse` | Full raw derivatives response |
| `get_market_status()` | `MarketStatusResponse` | Open / Closed / Pre-market |

#### Polling feed

```rust
use tokio::sync::mpsc;

let (tx, mut rx) = mpsc::channel(64);

// Spawn a polling loop — sends a NseQuote every 3 seconds
tokio::spawn(async move {
    client.poll_quote("INFY", 3_000, tx).await;
});

while let Some(q) = rx.recv().await {
    println!("{}: ₹{:.2}", q.symbol, q.ltp);
}
```

`poll_index("NIFTY 50", interval_ms, tx)` works the same way for indices.

Both loops stop automatically when the receiver is dropped.

#### Historical candles

```rust
use chrono::Utc;

let end   = Utc::now();
let start = end - chrono::Duration::days(5);

// 5-minute intraday candles (market hours only, auto-filtered)
let candles = client.get_historical_candles("SBIN", start, end, "5").await?;

// Daily candles going back years
let daily = client.get_historical_candles("NIFTY", start, end, "D").await?;
```

Supported intervals: `"1"` `"3"` `"5"` `"15"` `"30"` `"60"` (minutes, max 30-day window) or `"D"` `"W"` `"M"` (unlimited history).

Intraday candles are automatically filtered to 09:15–15:30 IST.

#### EOD archives

```rust
use chrono::NaiveDate;

let date = NaiveDate::from_ymd_opt(2025, 6, 20).unwrap();

// Equity bhavcopy
let records = client.fetch_full_bhavcopy(date).await?;

// All actively trading symbol names for a date
let symbols = client.fetch_symbol_list(date).await?;

// F&O bhavcopy — typed structs, both pre/post July-2024 formats
let fo = client.fetch_fo_bhavcopy(date).await?;
for rec in fo.iter().take(5) {
    println!("{} {} {} @ {:.2}  OI {}", rec.symbol, rec.expiry, rec.option_type, rec.strike, rec.oi);
}
```

---

## Key Types

### `NseQuote`
```rust
pub struct NseQuote {
    pub symbol:       String,
    pub company_name: String,
    pub ltp:          f64,
    pub open:         f64,
    pub high:         f64,
    pub low:          f64,
    pub prev_close:   f64,
    pub close:        f64,
    pub change:       f64,
    pub change_pct:   f64,
    pub volume:       f64,
    pub traded_value: f64,
    pub year_high:    f64,
    pub year_low:     f64,
    pub last_update:  String,
}
```

### `OptionChain`
```rust
pub struct OptionChain {
    pub symbol:   String,
    // expiry date string → rows sorted by strike ascending
    pub expiries: BTreeMap<String, Vec<OptionChainRow>>,
}

pub struct OptionChainRow {
    pub strike: f64,
    pub ce:     OptionSide,
    pub pe:     OptionSide,
}

pub struct OptionSide {
    pub ltp:          f64,
    pub oi:           f64,
    pub change_in_oi: f64,
    pub volume:       f64,
}
```

### `FoBhavRecord`
```rust
pub struct FoBhavRecord {
    pub symbol:          String,
    pub expiry:          String,
    pub instrument_type: String, // "FUTIDX", "OPTIDX", "FUTSTK", "OPTSTK"
    pub option_type:     String, // "CE", "PE", or "-"
    pub strike:          f64,
    pub open:            f64,
    pub high:            f64,
    pub low:             f64,
    pub close:           f64,
    pub settle_price:    f64,
    pub contracts:       u64,
    pub oi:              u64,
    pub change_in_oi:    i64,
}
```

---

## Session & Cookie Management

NSE's web APIs require browser cookies (`nsit`, `nseappid`, etc.) obtained by hitting their landing page. `nse-rs` handles this transparently:

1. **Disk cache** at `~/.cache/nse-rs/session.json` — reused for up to 1 hour across process restarts
2. **Auto-refresh** — if a request returns a 403 or a decode error, the session is refreshed once and the request retried automatically
3. **Force refresh** — call `client.force_refresh_session().await?` to discard and re-fetch

---

## ⚠️ Cloud & Geo Restrictions

`www.nseindia.com` (live quotes, option chains, charting) enforces strict firewall rules:

- **Geo-blocking** — requests from IPs outside India are frequently rejected with 403 or TCP resets
- **Cloud IP blocking** — AWS, GCP, Azure, DigitalOcean and similar data-centre ranges are blocked even within India

**Run from a residential Indian internet connection.** Residential proxies are an alternative.

The archive domain `nsearchives.nseindia.com` (bhavcopy downloads) does **not** have these restrictions and works globally.

---

## Running the Example

```bash
cargo run --example demo
```

---

Credits: inspired by Python's `jugaad-data` and `nsemine` — rewritten in Rust for type safety, zero-cost abstractions, and no runtime overhead.

## License

MIT

### Core Implementation Code & Architecture
#### File: `Cargo.toml`
```python
[package]
name = "nse-rs"
version = "0.1.0"
edition = "2024"

[dependencies]
tokio = { version = "1.38", features = ["full"] }
reqwest = { version = "0.12", default-features = false, features = ["rustls-tls-webpki-roots", "json", "cookies", "gzip", "brotli", "deflate"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
csv = "1.3"
zip = "2.1"
chrono = { version = "0.4", features = ["serde"] }
dirs = "5.0"
anyhow = "1"
```

#### File: `src/lib.rs`
```python
pub mod models;
pub mod session;
pub mod live;
pub mod historical;
pub mod archives;
pub mod client;

pub use client::NseClient;
pub use models::{
    // Session
    SessionCache,
    // Live quotes
    NseQuote, NseIndexQuote,
    // Raw API types (for callers that need the full response)
    NextApiQuoteResponse, NextApiDerivativesResponse, DerivativeContract,
    // Option chain
    OptionChain, OptionChainRow, OptionSide,
    // Historical
    ChartCandle, HistoricalRecord,
    // F&O EOD
    FoBhavRecord,
    // Market status
    MarketStatusResponse,
};
```

#### File: `examples/test_market_status.rs`
```python
use nse_rs::NseClient;
use chrono::{Utc, Duration};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    println!("Initializing NseClient...");
    let client = NseClient::new();
    client.init_session().await?;
    println!("Session initialized.");

    println!("\n--- Test: get_historical_candles(\"Nifty Midcap Select\") ---");
    let end_time = Utc::now();
    let start_time = end_time - Duration::days(5);
    match client.get_historical_candles("Nifty Midcap Select", start_time, end_time, "5").await {
        Ok(candles) => {
            println!("Success! Retrieved {} candles.", candles.len());
            if !candles.is_empty() {
                println!("First: {:?}", candles.first().unwrap());
                println!("Last: {:?}", candles.last().unwrap());
            }
        }
        Err(e) => println!("Failed: {:?}", e),
    }

    Ok(())
}
```

#### File: `examples/fetch_symbols.rs`
```python
use chrono::{Local, Datelike, Duration};
use nse_rs::NseClient;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let client = NseClient::new();
    
    // Note: Archives/bhavcopy endpoints do not require session cookie initialization.
    // Try dates going backwards to find the latest available bhavcopy
    let current_date = Local::now().date_naive();
    let mut symbols = Vec::new();
    
    for i in 0..10 {
        let date = current_date - Duration::days(i);
        // Skip weekends
        if date.weekday() == chrono::Weekday::Sat || date.weekday() == chrono::Weekday::Sun {
            continue;
        }
        
        println!("Trying to fetch symbol list for {}", date);
        match client.fetch_symbol_list(date).await {
            Ok(s) => {
                symbols = s;
                println!("Successfully fetched symbols for {}", date);
                break;
            }
            Err(e) => {
                println!("Failed for {}: {}", date, e);
            }
        }
    }
    
    if symbols.is_empty() {
        println!("Could not fetch symbol list for recent dates.");
        return Ok(());
    }
    
    println!("Found {} symbols.", symbols.len());
    println!("First 20 symbols:");
    for (i, symbol) in symbols.iter().take(20).enumerate() {
        println!("{}. {}", i + 1, symbol);
    }
    
    Ok(())
}
```

#### File: `src/session.rs`
```python
use std::collections::HashMap;
use std::fs;
use std::path::PathBuf;
use chrono::Utc;
use reqwest::header::{HeaderValue, SET_COOKIE};
use reqwest::Client;
use crate::models::SessionCache;

const SESSION_WARMUP_URL: &str = "https://www.nseindia.com/get-quote/equity/RELIANCE/Reliance-Industries-Limited";

/// Get cache file path in standard local cache directory
pub fn get_cache_path() -> Option<PathBuf> {
    let mut base = if let Ok(xdg) = std::env::var("XDG_CACHE_HOME") {
        if !xdg.is_empty() {
            Some(PathBuf::from(xdg))
        } else {
            None
        }
    } else {
        None
    };
    if base.is_none() {
        base = dirs::cache_dir();
    }
    base.map(|mut p| {
        p.push("nse-rs");
        p.push("session.json");
        p
    })
}

/// Load session cache from disk
pub fn load_session_cache() -> Option<SessionCache> {
    let path = get_cache_path()?;
    if !path.exists() {
        return None;
    }
    
    let content = fs::read_to_string(path).ok()?;
    let cache: SessionCache = serde_json::from_str(&content).ok()?;
    
    // Check if session has expired (TTL of 1 hour)
    let elapsed = Utc::now() - cache.updated_on;
    if elapsed < chrono::Duration::hours(1) {
        Some(cache)
    } else {
        None
    }
}

/// Save session cache to disk
pub fn save_session_cache(cookies: &HashMap<String, String>) -> Option<()> {
    let path = get_cache_path()?;
    
    // Ensure parent directory exists
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent).ok()?;
    }
    
    let cache = SessionCache {
        cookies: cookies.clone(),
        updated_on: Utc::now(),
    };
    
    let serialized = serde_json::to_string_pretty(&cache).ok()?;
    fs::write(path, serialized).ok()?;
    Some(())
}

/// Extract cookies from SET_COOKIE headers
pub fn extract_cookies(response: &reqwest::Response) -> HashMap<String, String> {
    let mut cookies = HashMap::new();
    for header_val in response.headers().get_all(SET_COOKIE) {
        if let Ok(cookie_str) = header_val.to_str() {
            if let Some(first_part) = cookie_str.split(';').next() {
                let mut parts = first_part.splitn(2, '=');
                if let (Some(name), Some(val)) = (parts.next(), parts.next()) {
                    cookies.insert(name.trim().to_string(), val.trim().to_string());
                }
            }
        }
    }
    cookies
}

/// Formats a HashMap of cookies into a single Cookie header value
pub fn format_cookie_header(cookies: &HashMap<String, String>) -> HeaderValue {
    let cookie_str = cookies.iter()
        .map(|(k, v)| format!("{}={}", k, v))
        .collect::<Vec<_>>()
        .join("; ");
    HeaderValue::from_str(&cookie_str).unwrap_or_else(|_| HeaderValue::from_static(""))
}

/// Helper to request cookies from the landing page.
/// Visits the NSE India homepage first to establish the cookie jar context.
pub async fn fetch_new_cookies(client: &Client) -> Result<HashMap<String, String>, reqwest::Error> {
    let mut cookies = HashMap::new();
    if let Ok(resp1) = client.get("https://www.nseindia.com/").send().await {
        cookies.extend(extract_cookies(&resp1));
    }
    let resp2 = client.get(SESSION_WARMUP_URL).send().await?;
    cookies.extend(extract_cookies(&resp2));
    Ok(cookies)
}
```

#### File: `src/live.rs`
```python
use std::collections::HashMap;
use anyhow::{Context, Result};
use reqwest::Client;
use reqwest::header::COOKIE;
use crate::models::{
    NextApiQuoteResponse, NextApiDerivativesResponse, IndexApiResponse, NseIndexQuote,
};
use crate::session::format_cookie_header;

const NEXT_API_URL: &str    = "https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi";
const MARKET_STATUS_URL: &str = "https://www.nseindia.com/api/marketStatus";
const INDEX_API_URL: &str   = "https://www.nseindia.com/api/allIndices";

/// Millisecond epoch string used as a `_=` query param to defeat NSE's
/// CDN/server response cache — without it these endpoints return a stale
/// snapshot (LTP/volume frozen for tens of seconds), which starves the live
/// candle feed of the price/volume changes it needs to build bars.
fn cache_buster() -> String {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_millis())
        .unwrap_or(0)
        .to_string()
}

pub async fn get_market_status(
    client: &Client,
    cookies: &HashMap<String, String>,
) -> Result<crate::models::MarketStatusResponse> {
    let cookie_val = format_cookie_header(cookies);
    client
        .get(MARKET_STATUS_URL)
        .header(COOKIE, cookie_val)
        .send()
        .await
        .context("market status request")?
        .json()
        .await
        .context("market status decode")
}

/// Fetch live equity quote for a symbol (e.g. "SBIN", "RELIANCE").
pub async fn get_stock_quote(
    client: &Client,
    cookies: &HashMap<String, String>,
    symbol: &str,
) -> Result<NextApiQuoteResponse> {
    let cookie_val = format_cookie_header(cookies);
    let bust = cache_buster();
    client
        .get(NEXT_API_URL)
        .header(COOKIE, cookie_val)
        .header(reqwest::header::CACHE_CONTROL, "no-cache")
        .query(&[
            ("functionName", "getSymbolData"),
            ("marketType", "N"),
            ("series", "EQ"),
            ("symbol", symbol),
            ("_", &bust),
        ])
        .send()
        .await
        .context("quote request")?
        .json()
        .await
        .context("quote decode")
}

/// Fetch live derivatives (futures & options) for a symbol (e.g. "NIFTY", "SBIN").
pub async fn get_derivatives_quote(
    client: &Client,
    cookies: &HashMap<String, String>,
    symbol: &str,
) -> Result<NextApiDerivativesResponse> {
    let cookie_val = format_cookie_header(cookies);
    let bust = cache_buster();
    client
        .get(NEXT_API_URL)
        .header(COOKIE, cookie_val)
        .header(reqwest::header::CACHE_CONTROL, "no-cache")
        .query(&[
            ("functionName", "getSymbolDerivativesData"),
            ("symbol", symbol),
            ("_", &bust),
        ])
        .send()
        .await
        .context("derivatives request")?
        .json()
        .await
        .context("derivatives decode")
}

/// Fetch LTP and OHLC for an NSE index.
/// `index_name` is the display name as used by NSE, e.g. `"NIFTY 50"`, `"NIFTY BANK"`.
pub async fn get_index_quote(
    client: &Client,
    cookies: &HashMap<String, String>,
    index_name: &str,
) -> Result<NseIndexQuote> {
    let cookie_val = format_cookie_header(cookies);
    let url = format!("{INDEX_API_URL}?_={}", cache_buster());
    let resp: IndexApiResponse = client
        .get(&url)
        .header(COOKIE, cookie_val)
        .header(reqwest::header::CACHE_CONTROL, "no-cache")
        .send()
        .await
        .context("index request")?
        .json()
        .await
        .context("index decode")?;

    let entry = resp
        .data
        .unwrap_or_default()
        .into_iter()
        .find(|e| e.index_symbol.eq_ignore_ascii_case(index_name))
        .with_context(|| format!("no data for index '{index_name}'"))?;

    Ok(NseIndexQuote {
        name:       entry.index_symbol,
        last:       entry.last,
        open:       entry.open,
        high:       entry.high,
        low:        entry.low,
        prev_close: entry.prev_close,
        change:     entry.change,
        change_pct: entry.change_pct,
    })
}
```


==================================================
