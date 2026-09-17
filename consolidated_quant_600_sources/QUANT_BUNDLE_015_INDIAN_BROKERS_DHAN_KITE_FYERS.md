# ⚡ [QUANT-SOURCE-015] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_015_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Dhan-React-Engine (`WHEEL_Dhan-React-Engine`)
- **Full Name**: `Dhan-React-Engine`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Nifty Algo Bot & Live Dashboard

An automated algorithmic trading bot for Nifty 50 options using the DhanHQ API. This project includes a core Python-based execution algorithm and a beautiful real-time React dashboard to monitor trades.

## Features
- **Automated Trading**: Identifies trends using intraday Nifty Index candle data and executes option trades automatically.
- **Dynamic Strike Selection**: Automatically selects At-The-Money (ATM) strikes.
- **FastAPI Backend**: A lightweight Python API to keep track of the current algorithmic state.
- **React Glassmorphism Dashboard**: A polished real-time UI that tracks your Entry, Stop-Loss, Target, and running P&L.

---

## Prerequisites
Before running this project, ensure you have the following installed on your machine:
- **Python 3.8+**
- **Node.js** (v14 or higher) & **npm**
- A **DhanHQ API Account** (You will need your Client ID and Access Token).

---

## Setup Instructions

### 1. Configure Python Environment (Bot & Backend)
Open a terminal in the root directory and create a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On MacOS/Linux:
source venv/bin/activate

# Install the necessary Python packages
pip install -r requirements.txt
```

### 2. Add API Credentials
Open `config.py` in the root directory and replace the placeholder text with your actual Dhan credentials:
```python
CLIENT_ID = "YOUR_CLIENT_ID"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
```
*(Optional: verify `LOT_SIZE` and execution timings inside `config.py`)*

### 3. Configure Node Environment (React Frontend)
Open a new terminal and install the frontend dependencies:
```bash
cd frontend
npm install
```

---

## Running the Application

To run the full suite successfully, you will need **three separate terminals**, all pointing to the root directory `Nifty_algo_bot`.

### Step 1: Start the State Backend
Open the **First Terminal**, activate your `venv`, and start the local API:
```bash
uvicorn backend.main:app --reload
```
*The backend will run on `http://127.0.0.1:8000`.*

### Step 2: Start the Dashboard
Open the **Second Terminal**, navigate to the frontend folder, and boot the UI:
```bash
cd frontend
npm start
```
*A browser tab will automatically open at `http://localhost:3000` showing your dashboard.*

### Step 3: Run the Trading Algorithm
Open the **Third Terminal**, activate your `venv`, and start the main trading intelligence script:
```bash
python main.py
```
*The script will run infinitely, syncing its state to the dashboard and waiting for the right moment to execute trades!*

### Core Implementation Code & Architecture
#### File: `dhan_client.py`
```python
from dhanhq import dhanhq
from config import CLIENT_ID, ACCESS_TOKEN

dhan = dhanhq(CLIENT_ID, ACCESS_TOKEN)
```

#### File: `backend/state.py`
```python
STATE = {
    "status": "IDLE",
    "trade": None,
    "entry": None,
    "sl": None,
    "target": None,
    "pnl": 0
}
```

#### File: `config.py`
```python
CLIENT_ID = "YOUR_CLIENT_ID"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

LOT_SIZE = 65

ENTRY_CUTOFF = (14, 0)   # 2 PM
EXIT_TIME = (15, 0)      # 3 PM
```

#### File: `data.py`
```python
import pandas as pd
from dhan_client import dhan

def get_nifty_candles():
    data = dhan.intraday_minute_data(
        security_id="13",  # NIFTY INDEX
        exchange_segment="NSE_INDEX",
        interval=5
    )

    df = pd.DataFrame(data['data'])
    return df
```

#### File: `frontend/public/manifest.json`
```python
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
```

#### File: `strategy.py`
```python
def check_signal(df):
    if len(df) < 3:
        return None

    first = df.iloc[-3]
    second = df.iloc[-2]

    first_green = first['close'] > first['open']
    first_red = first['close'] < first['open']

    second_green = second['close'] > second['open']
    second_red = second['close'] < second['open']

    return {
        "first_green": first_green,
        "first_red": first_red,
        "second_green": second_green,
        "second_red": second_red,
        "second_high": second['high'],
        "second_low": second['low']
    }
```


==================================================


## [2/3] Repository: DhanHQ-Ticker-py (`WHEEL_DhanHQ-Ticker-py`)
- **Full Name**: `DhanHQ-Ticker-py`
- **Description**: The Unofficial Python Websocket Client For Communicating With The Dhan API.
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# DhanHQ-Ticker-py
The Unofficial Python Websocket Client For Communicating With The [Dhan API](https://api.dhan.co)

DhanHQ-Ticker-py is a set of Websocket API that expose many capabilities required to build a complete investment and trading platform. Stream extended set of realtime market datas s well as order updates and more.


## Quickstart
You can install the package via `pip install -U git+https://github.com/Indian-Algorithmic-Trading-Community/DhanHQ-Ticker-py.git` or `pip install dhanhq_ticker_py-0.1.0-py3-none-any.whl`

## Demo Video Showcasing The Data Streaming To Excel
https://github.com/Indian-Algorithmic-Trading-Community/DhanHQ-Ticker-py/assets/96371033/f4be6f6d-21f2-4770-bf35-118aa6157c65



## WebSocket Usage

*Example -1 =>*  [login_with_credentials_ticker.py](https://github.com/Indian-Algorithmic-Trading-Community/DhanHQ-Ticker-py/blob/main/examples/login_with_credentials_ticker.py)

```python
import signal
from time import sleep
from dhanhq_ticker_py import (
    DhanTicker,
    get_option_chain,
    get_expiry_dates,
    get_instruments_details,
)

login_id = "Paste Your User User Id / Login Id Here"
password = "Paste Your User Password Here"
# Or You Can Read From A Plain Text File / Config / TOML / YAML Files.

# Define The Callbacks / Method Hooks
def on_ticks(tick):
    print(tick, end="\n" * 2)

def on_order_update(order_update):
    print(order_update, end="\n" * 2)

# Assign The Callbacks / Method Hooks
callbacks = DhanTicker.default_callbacks()
callbacks.update({"on_tick": on_ticks, "on_order_update": on_order_update})

ticker = DhanTicker(
    callbacks=callbacks,
    # debug=False, # Uncomment This For Debugging
    # debug_verbose=False, # Uncomment This For Verbose Debugging
)

ticker.login_with_credentials(login_id, password)

# As Dhan Doesn't Offer Provisions To Use TOTP, Instead It Send OTP On
# The Registered Mobile Number And Email ID. The Program Will Wait For
# The User To Key In The Received OTP In The Terminal / Console And Press
# Enter To Continue Completing A Successfull Login With Credentials.

# Fetch Instrument Details For Which We Want To Subscribe For Market Data
bnf_expiry, nf_expiry = [get_expiry_dates(idx, "NSE") for idx in {"BANKNIFTY", "NIFTY"}]
nearest_bnf_expiry, nearest_nf_expiry = (
    bnf_expiry["ExpiryDate"][0],
    nf_expiry["ExpiryDate"][0],
)

instruments = get_instruments_details(
    ["NIFTY", "BANKNIFTY"],
    "NSE",
    is_optidx=True,
    expiry_dates=[nearest_bnf_expiry, nearest_nf_expiry],
    strikes=[20000, 45000],
    opt_types=["CE", "PE"],
)
finnifty_all_nearest_expiry_options = get_option_chain("FINNIFTY", "NSE")

# Subscribe / Unsubscribe To The Instruments, It Can Be At Any Point
# After Instantiation of `DhanTicker` Class Object With Either `userdata`
# Or Login With Credentials.

# There Are Only Two Modes, Quote Mode and Full Mode.

if instruments is not None:
    ticker.subscribe(instruments, mode=ticker.FULL)
ticker.subscribe(finnifty_all_nearest_expiry_options, mode=ticker.FULL)

# The Ticker is fully asynchronous and runs in a background thread event loop.
# So We Need To Keep The Main Thread Alive.

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ticker._handle_stop_signals)
    signal.signal(signal.SIGTERM, ticker._handle_stop_signals)

    while True:
        try:
            # Do Any Operation In This Thread, And It Won't
            # Effect The Market Data Feed And Order Update Feed.

            # Or If You do not want to do any operation but only
            # want the updateds to keep printing in the console /
            # terminal, then print anything or put `pass` in this
            # block and keep the rest lines as is.

            print("Dr June Moone Say's Hi! From Main Thread")
        except KeyboardInterrupt:
            break
        else:
            sleep(5)
```

*Example - 2 =>*  [login_with_userdata_ticker.py](https://github.com/Indian-Algorithmic-Trading-Community/DhanHQ-Ticker-py/blob/main/examples/login_with_userdata_ticker.py)

```python
import signal
from time import sleep
from dhanhq_ticker_py import (
    DhanTicker,
    get_option_chain,
    get_expiry_dates,
    get_instruments_details,
)

userdata = "Paste Your User Data Here"
# Or You Can Read From A Plain Text File / Config / TOML / YAML Files.

# Define The Callbacks / Method Hooks
def on_ticks(tick):
    print(tick, end="\n" * 2)

def on_order_update(order_update):
    print(order_update, end="\n" * 2)

# Assign The Callbacks / Method Hooks
callbacks = DhanTicker.default_callbacks()
callbacks.update({"on_tick": on_ticks, "on_order_update": on_order_update})

ticker = DhanTicker(
    userdata=userdata,
    callbacks=callbacks,
    # debug=False, # Uncomment This For Debugging
    # debug_verbose=False, # Uncomment This For Verbose Debugging
)

# Fetch Instrument Details For Which We Want To Subscribe For Market Data
bnf_expiry, nf_expiry = [get_expiry_dates(idx, "NSE") for idx in {"BANKNIFTY", "NIFTY"}]
nearest_bnf_expiry, nearest_nf_expiry = (
    bnf_expiry["ExpiryDate"][0],
    nf_expiry["ExpiryDate"][0],
)

instruments = get_instruments_details(
    ["NIFTY", "BANKNIFTY"],
    "NSE",
    is_optidx=True,
    expiry_dates=[nearest_bnf_expiry, nearest_nf_expiry],
    strikes=[20000, 45000],
    opt_types=["CE", "PE"],
)
finnifty_all_nearest_expiry_options = get_option_chain("FINNIFTY", "NSE")

# Subscribe / Unsubscribe To The Instruments, It Can Be At Any Point
# After Instantiation of `DhanTicker` Class Object With Either `userdata`
# Or Login With Credentials.

# There Are Only Two Modes, Quote Mode and Full Mode.

if instruments is not None:
    ticker.subscribe(instruments, mode=ticker.FULL)
ticker.subscribe(finnifty_all_nearest_expiry_options, mode=ticker.FULL)

# The Ticker is fully asynchronous and runs in a background thread event loop.
# So We Need To Keep The Main Thread Alive.

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ticker._handle_stop_signals)
    signal.signal(signal.SIGTERM, ticker._handle_stop_signals)

    while True:
        try:
            # Do Any Operation In This Thread, And It Won't
            # Effect The Market Data Feed And Order Update Feed.

            # Or If You do not want to do any operation but only
            # want the updateds to keep printing in the console /
            # terminal, then print anything or put `pass` in this
            # block and keep the rest lines as is.

            print("Dr June Moone Say's Hi! From Main Thread")
        except KeyboardInterrupt:
            break
        else:
            sleep(5)
```

*Example - 2 =>*  [get_instrument_details.py](https://github.com/Indian-Algorithmic-Trading-Community/DhanHQ-Ticker-py/blob/main/examples/get_instrument_details.py)

```python
from dhanhq_ticker_py import (
    get_option_chain,
    get_expiry_dates,
    get_instrument_details,
    get_instruments_details,
    fetch_and_save_latest_dhan_master_scrip_feather,
)

fetch_and_save_latest_dhan_master_scrip_feather()

get_instrument_details("RELIANCE", "BSE", is_equity=True, pretty_print=True)

get_instrument_details(
    "USDINR",
    "BSE",
    is_optcur=True,
    expiry_date="2023-12-08",
    strike=82.5,
    opt_type="CE",
    pretty_print=True,
)

get_instruments_details(
    ["RELIANCE", "HDFCBANK"], "BSE", is_equity=True, pretty_print=True
)

get_instruments_details(["SENSEX", "BANKEX"], "BSE", is_index=True, pretty_print=True)

get_instruments_details(
    ["NIFTY", "BANKNIFTY", "FINNNIFTY", "MIDCPNIFTY"],
    "NSE",
    is_index=True,
    pretty_print=True,
)

print(get_expiry_dates("NIFTY", "NSE"))

print(get_option_chain("NIFTY", "NSE"))
print(get_option_chain("NIFTY", "NSE", "2023-12-14"))

print(get_expiry_dates("BANKNIFTY", "NSE"))

print(get_option_chain("BANKNIFTY", "NSE"))
print(get_option_chain("BANKNIFTY", "NSE", "2023-12-13"))


bnf_expiry, nf_expiry = [get_expiry_dates(idx, "NSE") for idx in {"BANKNIFTY", "NIFTY"}]

print(bnf_expiry, nf_expiry, sep="\n" * 2, end="\n" * 2)

nearest_bnf_expiry, nearest_nf_expiry = (
    bnf_expiry["ExpiryDate"][0],
    nf_expiry["ExpiryDate"][0],
)
print(nearest_bnf_expiry, nearest_nf_expiry, sep="\n" * 2, end="\n" * 2)

instruments = get_instruments_details(
    ["NIFTY", "BANKNIFTY"],
    "NSE",
    is_optidx=True,
    expiry_dates=[nearest_bnf_expiry, nearest_nf_expiry],
    strikes=[20000, 45000],
    opt_types=["CE", "PE"],
)
print(instruments, end="\n" * 2)

finnifty_all_nearest_expiry_options = get_option_chain("FINNIFTY", "NSE")
print(finnifty_all_nearest_expiry_options, end="\n" * 2)
```

## Code Statistics
<img src=".assets/LinesOfCode.png" alt="LinesOfCode" width="1000" height="250" border="10" />

## License
<sup>
Licensed under either of <a href="LICENSE-APACHE">Apache License, Version
2.0</a> or <a href="LICENSE-MIT">MIT license</a> at your option.
</sup>

<br>

<sub>
Unless you explicitly state otherwise, any contribution intent

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `src/dhanhq_ticker_py/__version.__.py`
```python
__title__ = "dhanhq-ticker-py"
__description__ = (
    "The Unofficial Python Websocket Client For Communicating With The Dhan API."
)
__url__ = "https://dhanhq.co/"
__download_url__ = (
    "https://github.com/Indian-Algorithmic-Trading-Community/DhanHQ-Ticker-py"
)
__version__ = "0.1.0"
__author__ = "Dr June Moone"
__author_email__ = "96371033+MooneDrJune@users.noreply.github.com"
__license__ = "MIT"
```

#### File: `pyproject.toml`
```python
[project]
name = "dhanhq-ticker-py"
version = "0.1.0"
description = "The Unofficial Python Websocket Client For Communicating With The Dhan API."
authors = [
    { name = "Dr June Moone", email = "96371033+MooneDrJune@users.noreply.github.com" }
]
dependencies = [
    "pycryptodome>=3.19.0",
    "websockets>=12.0",
    "aiohttp[speedups]>=3.9.1",
    "polars>=0.19.19",
]
readme = "README.md"
requires-python = ">= 3.11"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.rye]
managed = true
dev-dependencies = [
    "black>=23.11.0",
    "ruff>=0.1.6",
    "mypy>=1.7.1",
]

[tool.hatch.metadata]
allow-direct-references = true
```

#### File: `src/dhanhq_ticker_py/__init__.py`
```python
from __future__ import unicode_literals, absolute_import
from .ticker import DhanTicker
from .utils import (
    Utils,
    AttrDict,
    Callback,
    get_expiry_dates,
    get_option_chain,
    get_instrument_type,
    get_instrument_details,
    get_instruments_details,
    get_dhan_trading_symbol,
    get_parsed_instruments_attrdict,
    fetch_and_save_latest_dhan_master_scrip_feather,
)

__all__ = [
    "Utils",
    "AttrDict",
    "Callback",
    "DhanTicker",
    "get_expiry_dates",
    "get_option_chain",
    "get_instrument_type",
    "get_instrument_details",
    "get_instruments_details",
    "get_dhan_trading_symbol",
    "get_parsed_instruments_attrdict",
    "fetch_and_save_latest_dhan_master_scrip_feather",
]
```

#### File: `examples/get_instrument_details.py`
```python
from dhanhq_ticker_py import (
    get_option_chain,
    get_expiry_dates,
    get_instrument_details,
    get_instruments_details,
    fetch_and_save_latest_dhan_master_scrip_feather,
)

fetch_and_save_latest_dhan_master_scrip_feather()

get_instrument_details("RELIANCE", "BSE", is_equity=True, pretty_print=True)

get_instrument_details(
    "USDINR",
    "BSE",
    is_optcur=True,
    expiry_date="2023-12-08",
    strike=82.5,
    opt_type="CE",
    pretty_print=True,
)

get_instruments_details(
    ["RELIANCE", "HDFCBANK"], "BSE", is_equity=True, pretty_print=True
)

get_instruments_details(["SENSEX", "BANKEX"], "BSE", is_index=True, pretty_print=True)

get_instruments_details(
    ["NIFTY", "BANKNIFTY", "FINNNIFTY", "MIDCPNIFTY"],
    "NSE",
    is_index=True,
    pretty_print=True,
)

print(get_expiry_dates("NIFTY", "NSE"))

print(get_option_chain("NIFTY", "NSE"))
print(get_option_chain("NIFTY", "NSE", "2023-12-14"))

print(get_expiry_dates("BANKNIFTY", "NSE"))

print(get_option_chain("BANKNIFTY", "NSE"))
print(get_option_chain("BANKNIFTY", "NSE", "2023-12-13"))


bnf_expiry, nf_expiry = [get_expiry_dates(idx, "NSE") for idx in {"BANKNIFTY", "NIFTY"}]

print(bnf_expiry, nf_expiry, sep="\n" * 2, end="\n" * 2)

nearest_bnf_expiry, nearest_nf_expiry = (
    bnf_expiry["ExpiryDate"][0],
    nf_expiry["ExpiryDate"][0],
)
print(nearest_bnf_expiry, nearest_nf_expiry, sep="\n" * 2, end="\n" * 2)

instruments = get_instruments_details(
    ["NIFTY", "BANKNIFTY"],
    "NSE",
    is_optidx=True,
    expiry_dates=[nearest_bnf_expiry, nearest_nf_expiry],
    strikes=[20000, 45000],
    opt_types=["CE", "PE"],
)
print(instruments, end="\n" * 2)

finnifty_all_nearest_expiry_options = get_option_chain("FINNIFTY", "NSE")
print(finnifty_all_nearest_expiry_options, end="\n" * 2)
```

#### File: `examples/login_with_userdata_ticker.py`
```python
import signal
from time import sleep
from dhanhq_ticker_py import (
    DhanTicker,
    get_option_chain,
    get_expiry_dates,
    get_instruments_details,
)

userdata = "Paste Your User Data Here"
# Or You Can Read From A Plain Text File / Config / TOML / YAML Files.

# Define The Callbacks / Method Hooks


def on_ticks(tick):
    print("Tick Update =>", tick, sep=" ", end="\n" * 2)


def on_order_update(order_update):
    print("Order Update =>", order_update, sep=" ", end="\n" * 2)


# Assign The Callbacks / Method Hooks

callbacks = DhanTicker.default_callbacks()
callbacks.update({"on_tick": on_ticks, "on_order_update": on_order_update})

ticker = DhanTicker(
    userdata=userdata,
    callbacks=callbacks,
    # debug=False, # Uncomment This For Debugging
    # debug_verbose=False, # Uncomment This For Verbose Debugging
)

# Fetch Instrument Details For Which We Want To Subscribe For Market Data
bnf_expiry, nf_expiry = [get_expiry_dates(idx, "NSE") for idx in {"BANKNIFTY", "NIFTY"}]
nearest_bnf_expiry, nearest_nf_expiry = (
    bnf_expiry["ExpiryDate"][0],
    nf_expiry["ExpiryDate"][0],
)

instruments = get_instruments_details(
    ["NIFTY", "BANKNIFTY"],
    "NSE",
    is_optidx=True,
    expiry_dates=[nearest_bnf_expiry, nearest_nf_expiry],
    strikes=[20000, 45000],
    opt_types=["CE", "PE"],
)
finnifty_all_nearest_expiry_options = get_option_chain("FINNIFTY", "NSE")

# Subscribe / Unsubscribe To The Instruments, It Can Be At Any Point
# After Instantiation of `DhanTicker` Class Object With Either `userdata`
# Or Login With Credentials.

# There Are Only Two Modes, Quote Mode and Full Mode.

if instruments is not None:
    ticker.subscribe(instruments, mode=ticker.FULL)
ticker.subscribe(finnifty_all_nearest_expiry_options, mode=ticker.FULL)


# The Ticker is fully asynchronous and runs in a backgroung thread event loop.
# So We Need To Keep The Main Thread Alive.

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ticker._handle_stop_signals)
    signal.signal(signal.SIGTERM, ticker._handle_stop_signals)

    while True:
        try:
            # Do Any Operation In This Thread, And It Wont
            # Effect The Market Data Feed And Order Update Feed.

            # Or If You do not want to do any operation but only
            # want the updateds to keep printing in the console /
            # terminal, then print anything or put `pass` in this
            # block and keep the rest lines as is.

            print("Dr June Moone Say's Hi! From Main Thread")
        except KeyboardInterrupt:
            break
        else:
            sleep(5)
```


==================================================


## [3/3] Repository: DhanMCP (`WHEEL_DhanMCP`)
- **Full Name**: `DhanMCP`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# DhanHQ MCP Server

An MCP (Model Context Protocol) server for DhanHQ APIs with OAuth-based authentication for Individual Traders.

## Overview

This server implements the complete three-step DhanHQ authentication flow that generates a JWT access token for API requests. The authentication process involves:

1. **Step 1**: Generate Consent - Creates a temporary session ID
2. **Step 2**: Browser-Based Login - User authenticates with 2FA
3. **Step 3**: Consume Consent - Exchanges tokenId for access token

## Prerequisites

Before you begin, you need to generate your API Key and Secret:

1. Log in to [web.dhan.co](https://web.dhan.co)
2. Navigate to **My Profile** → **'Access DhanHQ APIs'**
3. Toggle to **'API key'**
4. Enter your:
   - App name
   - Redirect URL (e.g., `http://localhost:3000/callback`)
   - Optional Postback URL

Note: Generated API Keys and Secrets are valid for 12 months.

## Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

```env
DHAN_CLIENT_ID=your_dhan_client_id
DHAN_API_KEY=your_api_key
DHAN_API_SECRET=your_api_secret
REDIRECT_URL=http://localhost:3000/callback
```

### 3. Build the Project

```bash
npm run build
```

## Usage

### Development Mode

```bash
npm run dev
```

### Using MCP Inspector (Recommended for Debugging)

The MCP Inspector provides an interactive interface to test the MCP tools:

```bash
npm run inspector
```

This will:
1. Start the MCP server
2. Open the MCP Inspector in your browser
3. Allow you to call tools and see responses in real-time

## Authentication Flow

### Step 1: Start Authentication

Call the `start_authentication` tool. This will:
- Validate your API credentials
- Create a temporary session (consentAppId)
- Return a login URL

### Step 2: Browser Login

Open the provided login URL in your browser:
- Log in with your Dhan credentials
- Complete 2FA verification (OTP/PIN/Password)
- You'll be redirected to your configured Redirect URL with a `tokenId` parameter

Example redirect URL:
```
http://localhost:3000/callback?tokenId=abc123def456...
```

### Step 3: Complete Authentication

Call the `complete_authentication` tool with the `tokenId` from Step 2:
- Exchanges the tokenId for a JWT access token
- Stores token details (expiry, client info, etc.)
- Returns the access token for use in subsequent API calls

### Check Status

Use `check_auth_status` to view:
- Current authentication state
- Token validity
- Client information
- Token expiry time

## Available MCP Tools

### `start_authentication`
Initiates the DhanHQ authentication flow (Step 1).
- **Input**: None
- **Output**: consentAppId, loginUrl, instructions

### `get_login_instructions`
Gets the login instructions and URL for Step 2.
- **Input**: consentAppId (optional)
- **Output**: loginUrl, detailed instructions

### `complete_authentication`
Completes authentication with the tokenId from Step 2 (Step 3).
- **Input**: tokenId (required)
- **Output**: authToken with accessToken and client details

### `check_auth_status`
Checks the current authentication status.
- **Input**: None
- **Output**: Authentication state and token validity

### `reset_authentication`
Clears the current authentication state.
- **Input**: None
- **Output**: Success message

## API Architecture

- **Framework**: Node.js with TypeScript
- **Protocol**: Model Context Protocol (MCP)
- **Transport**: Stdio
- **Auth API**: DhanHQ OAuth endpoints
- **HTTP Client**: Axios

## Project Structure

```
src/
├── index.ts           # MCP server and tool handlers
├── authentication.ts  # Authentication logic (3-step flow)
├── config.ts         # Configuration management
└── types.ts          # TypeScript interfaces
```

## Security Considerations

- API credentials are stored in environment variables
- Access tokens are stored in-memory (session-based)
- For production, use:
  - Secure credential storage
  - Database for token persistence
  - Token refresh mechanisms
  - HTTPS for callbacks
- The MCP Inspector output redacts sensitive tokens

## Error Handling

The server includes comprehensive error handling:
- API request validation
- Network error handling
- Configuration validation
- Token expiry checking

## Next Steps

After authentication is working:
1. Add API tools for trading operations
2. Implement token refresh logic
3. Add portfolio/holdings endpoints
4. Implement order placement tools
5. Add market data tools

## Development Notes

- Logs are printed to stderr for debugging
- Authentication state is stored in-memory (lost on restart)
- For production, migrate to persistent storage
- MCP Inspector is recommended for interactive testing and debugging

## License

MIT

### Core Implementation Code & Architecture
#### File: `package.json`
```python
{
  "name": "dhan-mcp-server",
  "version": "1.0.0",
  "description": "MCP Server for DhanHQ APIs with OAuth-based authentication",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsc && node dist/index.js",
    "watch": "tsc --watch",
    "inspector": "npx @modelcontextprotocol/inspector node dist/index.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0",
    "axios": "^1.6.0",
    "dotenv": "^16.3.1"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.3.0"
  }
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ES2020",
    "lib": ["ES2020"],
    "moduleResolution": "node",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

#### File: `package-lock.json`
```python
{
  "name": "dhan-mcp-server",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "dhan-mcp-server",
      "version": "1.0.0",
      "dependencies": {
        "@modelcontextprotocol/sdk": "^1.0.0",
        "axios": "^1.6.0",
        "dotenv": "^16.3.1"
      },
      "devDependencies": {
        "@types/node": "^20.0.0",
        "typescript": "^5.3.0"
      }
    },
    "node_modules/@modelcontextprotocol/sdk": {
      "version": "1.24.3",
      "resolved": "https://registry.npmjs.org/@modelcontextprotocol/sdk/-/sdk-1.24.3.tgz",
      "integrity": "sha512-YgSHW29fuzKKAHTGe9zjNoo+yF8KaQPzDC2W9Pv41E7/57IfY+AMGJ/aDFlgTLcVVELoggKE4syABCE75u3NCw==",
      "license": "MIT",
      "dependencies": {
        "ajv": "^8.17.1",
        "ajv-formats": "^3.0.1",
        "content-type": "^1.0.5",
        "cors": "^2.8.5",
        "cross-spawn": "^7.0.5",
        "eventsource": "^3.0.2",
        "eventsource-parser": "^3.0.0",
        "express": "^5.0.1",
        "express-rate-limit": "^7.5.0",
        "jose": "^6.1.1",
        "pkce-challenge": "^5.0.0",
        "raw-body": "^3.0.0",
        "zod": "^3.25 || ^4.0",
        "zod-to-json-schema": "^3.25.0"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "@cfworker/json-schema": "^4.1.1",
        "zod": "^3.25 || ^4.0"
      },
      "peerDependenciesMeta": {
        "@cfworker/json-schema": {
          "optional": true
        },
        "zod": {
          "optional": false
        }
      }
    },
    "node_modules/@types/node": {
      "version": "20.19.25",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-20.19.25.tgz",
      "integrity": "sha512-ZsJzA5thDQMSQO788d7IocwwQbI8B5OPzmqNvpf3NY/+MHDAS759Wo0gd2WQeXYt5AAAQjzcrTVC6SKCuYgoCQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "undici-types": "~6.21.0"
      }
    },
    "node_modules/accepts": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-2.0.0.tgz",
      "integrity": "sha512-5cvg6CtKwfgdmVqY1WIiXKc3Q1bkRqGLi+2W/6ao+6Y7gu/RCwRuAhGEzh5B4KlszSuTLgZYuqFqo5bImjNKng==",
      "license": "MIT",
      "dependencies": {
        "mime-types": "^3.0.0",
        "negotiator": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/ajv": {
      "version": "8.17.1",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-8.17.1.tgz",
      "integrity": "sha512-B/gBuNg5SiMTrPkC+A2+cW0RszwxYmn6VYxB/inlBStS5nx6xHIt/ehKRhIMhqusl7a8LjQoZnjCs5vhwxOQ1g==",
      "license": "MIT",
      "dependencies": {
        "fast-deep-equal": "^3.1.3",
        "fast-uri": "^3.0.1",
        "json-schema-traverse": "^1.0.0",
        "require-from-string": "^2.0.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/ajv-formats": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/ajv-formats/-/ajv-formats-3.0.1.tgz",
      "integrity": "sha512-8iUql50EUR+uUcdRQ3HDqa6EVyo3docL8g5WJ3FNcWmu62IbkGUue/pEyLBW8VGKKucTPgqeks4fIU1DA4yowQ==",
      "license": "MIT",
      "dependencies": {
        "ajv": "^8.0.0"
      },
      "peerDependencies": {
        "ajv": "^8.0.0"
      },
      "peerDependenciesMeta": {
        "ajv": {
          "optional": true
        }
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
      "license": "MIT"
    },
    "node_modules/axios": {
      "version": "1.13.2",
      "resolved": "https://registry.npmjs.org/axios/-/axios-1.13.2.tgz",
      "integrity": "sha512-VPk9ebNqPcy5lRGuSlKx752IlDatOjT9paPlm8A7yOuW2Fbvp4X3JznJtT4f0GzGLLiWE9W8onz51SqLYwzGaA==",
      "license": "MIT",
      "dependencies": {
        "follow-redirects": "^1.15.6",
        "form-data": "^4.0.4",
        "proxy-from-env": "^1.1.0"
      }
    },
    "node_modules/body-parser": {
      "version": "2.2.1",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-2.2.1.tgz",
      "integrity": "sha512-nfDwkulwiZYQIGwxdy0RUmowMhKcFVcYXUU7m4QlKYim1rUtg83xm2yjZ40QjDuc291AJjjeSc9b++AWHSgSHw==",
      "license": "MIT",
      "dependencies": {
        "bytes": "^3.1.2",
        "content-type": "^1.0.5",
        "debug": "^4.4.3",
        "http-errors": "^2.0.0",
        "iconv-lite": "^0.7.0",
        "on-finished": "^2.4.1",
        "qs": "^6.14.0",
        "raw-body": "^3.0.1",
        "type-is": "^2.0.1"
      },
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/bytes": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.1.2.tgz",
      "integrity": "sha512-/Nf7TyzTx6S3yRJObOAV7956r8cr2+Oj8AC5dt8wSP3BQAoeX58NoHyCU8P8zGkNXStjTSi6fzO6F0pBdcYbEg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/call-bound": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz",
      "integrity": "sha512-+ys997U96po4Kx/ABpBCqhA9EuxJaQWDQg7295H4hBphv3IZg0boBKuwYpt4YXp6MZ5AmZQnU/tyMTlRpaSejg==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "get-intrinsic": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "license": "MIT",
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/content-disposition": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-1.0.1.tgz",
      "integrity": "sha512-oIXISMynqSqm241k6kcQ5UwttDILMK4BiurCfGEREw6+X9jkkpEe5T9FZaApyLGGOnFuyMWZpdolTXMtvEJ08Q==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/content-type": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.5.tgz",
      "integrity": "sha512-nTjqfcBFEipKdXCv4YDQWCfmcLZKm81ldF0pAopTvyrFGVbcR6P/VAAd5G7N+0tTr8QqiU0tFadD6FK4NtJwOA==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.7.2.tgz",
      "integrity": "sha512-yki5XnKuf750l50uGTllt6kKILY4nQ1eNIQatoXEByZ5dWgnKqbnqmTrBE5B4N7lrMJKQ2ytWMiTO2o0v6Ew/w==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/cookie-signature": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.2.2.tgz",
      "integrity": "sha512-D76uU73ulSXrD1UXF4KE2TMxVVwhsnCgfAyTg9k8P6KGZjlXKrOLe4dJQKI3Bxi5wjesZoFXJWElNWBjPZMbhg==",
      "license": "MIT",
      "engines": {
        "node": ">=6.6.0"
      }
    },
    "node_modules/cors": {
      "version": "2.8.5",
      "resolved": "https://registry.npmjs.org/cors/-/cors-2.8.5.tgz",
      "integrity": "sha512-KIHbLJqu73RGr/hnbrO9uBeixNGuvSQjul/jdFvS/KFSIH1hWVd1ng7zOHx+YrEfInLG7q4n6GHQ9cDtxv/P6g==",
      "license": "MIT",
      "dependencies": {
        "object-assign": "^4",
        "vary": "^1"
      },
      "engines": {
        "node": ">= 0.10"
      }
    },
    "node_modules/cross-spawn": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
      "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
      "license": "MIT",
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/depd": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-2.0.0.tgz",
      "integrity": "sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/dotenv": {
      "version": "16.6.1",
      "resolved": "https://registry.npmjs.org/dotenv/-/dotenv-16.6.1.tgz",
      "integrity": "sha512-uBq4egWHTcTt33a72vpSG0z3HnPuIl6NqYcTrKEg2azoEyl2hpW0zqlxysq2pK9HlDIHyHyakeYaYnSAwd8bow==",
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://dotenvx.com"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha512-WMwm9LhRUo+WUaRN+vRuETqG89IgZphVSNkdFgeb6sS/E4OrDIN7t48CAewSHXc6C8lefD8KKfr5vY61brQlow==",
      "license": "MIT"
    },
    "node_modules/encodeurl": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-2.0.0.tgz",
      "integrity": "sha512-Q0n9HRi4m6JuGIV1eFlmvJB7ZEVxu93IrMyiMsGC0lrMJMWzRgx6WGquyfQgZVb31vhGgXnfmPNNXmxnOkRBrg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz",
      "integrity": "sha512-FGgH2h8zKNim9ljj7dankFPcICIK9Cp5bm+c2gQSYePhpaG5+esrLODihIorn+Pe6FGJzWhXQotPv73jTaldXA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-set-tostringtag": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
      "integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha512-NiSupZ4OeuGwr68lGIeym/ksIZMJodUGOSCZ/FSnTxcrekbvqrgdUxlJOMpijaKZVjAJrWrGs/6Jy8OMuyj9ow==",
      "license": "MIT"
    },
    "node_modules/etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha512-aIL5Fx7mawVa300al2BnEE4iNvo1qETxLrPI/o05L7z6go7fCw1J6EQmbK4FmJ2AS7kgVF/KEZWufBfdClMcPg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/eventsource": {
      "version": "3.0.7",
      "resolved": "https://registry.npmjs.org/eventsource/-/eventsource-3.0.7.tgz",
      "integrity": "sha512-CRT1WTyuQoD771GW56XEZFQ/ZoSfWid1alKGDYMmkt2yl8UXrVR4pspqWNEcqKvVIzg6PAltWjxcSSPrboA4iA==",
      "license": "MIT",
      "dependencies": {
        "eventsource-parser": "^3.0.1"
      },
      "engines": {
        "node": ">=18.0.0"
      }
    },
    "node_modules/eventsource-parser": {
      "version": "3.0.6",
      "resolved": "https://registry.npmjs.org/eventsource-parser/-/eventsource-parser-3.0.6.tgz",
      "integrity": "sha512-Vo1ab+QXPzZ4tCa8SwIHJFaSzy4R6SHf7BY79rFBDf0idraZWAkYrDjDj8uWaSm3S2TK+hJ7/t1CEmZ7jXw+pg==",
      "license": "MIT",
      "engines": {
        "node": ">=18.0.0"
      }
    },
    "node_modules/express": {
      "version": "5.2.1",
      "resolved": "https://registry.npmjs.org/express/-/express-5.2.1.tgz",
      "integrity": "sha512-hIS4idWWai69NezIdRt2xFVofaF4j+6INOpJlVOLDO8zXGpUVEVzIYk
# ... [TRUNCATED FILE CONTENT]
```


==================================================
