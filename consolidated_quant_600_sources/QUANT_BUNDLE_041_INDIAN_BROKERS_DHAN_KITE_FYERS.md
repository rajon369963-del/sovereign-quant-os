# ⚡ [QUANT-SOURCE-041] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_041_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ZerodhaStrikesAllowedToTrade (`PHASE4-QUANT-152`)
- **Full Name**: `PHASE4-QUANT-152_TechfaneTechnologies__ZerodhaStrikesAllowedToTrade`
- **Description**: A Python Script To Fetch The Nifty, BankNifty And FinNifty Contracts Allowed For Trading At Zerodha Kite Platform.
- **GitHub Stars**: 30
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Zerodha Strikes Allowed To Trade
A Python Script To Fetch The Nifty, BankNifty And FinNifty Contracts Allowed For Trading At Zerodha Kite Platform.

## Update Frequency
Check for updates daily at 08:00 AM IST and 08:00 PM IST

## Raw JSON Files
- [StrikesAllowed.json](https://techfanetechnologies.github.io/ZerodhaStrikesAllowedToTrade/StrikesAllowed.json)

## _If You have liked the work, Do Star This Repository and Stay-Up-To-Date_
<p align="center">
  <img src="https://user-images.githubusercontent.com/96371033/180197157-aabda812-828b-4cf7-97a6-a4b9bdd8b151.gif" alt="How To Star A Repository">
</p>

### Core Implementation Code & Architecture
#### File: `StrikesAllowed.json`
```python
{"BankNifty": {"30/09/2025": {"NRML": "All Strikes Allowed ", "MIS": "All Strikes Allowed"}, "28/10/2025": {"NRML": "All Strikes Allowed ", "MIS": "All Strikes Allowed"}, "25/11/2025": {"NRML": "All Strikes Allowed ", "MIS": "All Strikes Allowed"}}, "Nifty": {"23/09/2025": {"NRML": "All Strikes Allowed ", "MIS": "All Strikes Allowed"}, "30/09/2025": {"NRML": "All Strikes Allowed ", "MIS": "All Strikes Allowed"}, "07/10/2025": {"NRML": "All Strikes Allowed ", "MIS": "All Strikes Allowed"}}, "FinNifty": {"30/09/2025": {"NRML": "All Strikes Allowed  ", "MIS": "All Strikes With Oi Over 500 Lots Allowed"}}}
```

#### File: `main.py`
```python
# -*- coding: utf-8 -*-
"""
    :description: A Python Script To Fetch The Nifty, Bank Nifty & Fin Nifty Contracts Allowed For Trading At Zerodha Kite Platform.
    :license: MIT.
    :author: Dr June Moone
    :created: On Monday November 28, 2022 11:17:53 GMT+05:30
"""
__author__ = "Dr June Moone"
__webpage__ = "https://github.com/MooneDrJune"
__license__ = "MIT"

try:
    import json
    import requests
    from lxml import html
    from typing import Tuple, List, Dict, Union
except (ImportError, ModuleNotFoundError):
    __import__("os").system(
        f"{__import__('sys').executable} -m pip install -U requests lxml json"
    )
finally:
    import json
    import requests
    from lxml import html
    from typing import Tuple, List, Dict, Union


def fetchAllowedLists(
    url: str = "https://zerodha.com/margin-calculator/SPAN/",
) -> Tuple[List[str], List[str], List[str]]:
    table_data = [
        item.strip()
        for item in html.fromstring(requests.get(url=url).content)
        .xpath('//*[@id="remove_container"]/section[2]/div[2]')[0]
        .text_content()
        .strip()
        .splitlines()
        if item.strip() != ""
    ]

    sec_under_ban = table_data[
        table_data.index("Securities under ban")
        + 1 : table_data.index("Bank Nifty contracts allowed for trading")
    ]
    sec_under_ban = (
        sec_under_ban[: sec_under_ban.index("More information")]
        if "More information" in sec_under_ban
        else sec_under_ban
    )
    bnf_allowed = table_data[
        table_data.index("Bank Nifty contracts allowed for trading")
        + 1 : table_data.index("Nifty contracts allowed for trading")
    ]
    bnf_allowed = (
        bnf_allowed[: bnf_allowed.index("More information")]
        if "More information" in bnf_allowed
        else bnf_allowed
    )
    nf_allowed = table_data[
        table_data.index("Nifty contracts allowed for trading")
        + 1 : table_data.index("Finnifty contracts allowed for trading")
    ]
    nf_allowed = (
        nf_allowed[: nf_allowed.index("More information")]
        if "More information" in nf_allowed
        else nf_allowed
    )
    fnf_allowed = table_data[
        table_data.index("Finnifty contracts allowed for trading") + 1 :
    ]
    fnf_allowed = (
        fnf_allowed[: fnf_allowed.index("More information")]
        if "More information" in fnf_allowed
        else fnf_allowed
    )
    return bnf_allowed, nf_allowed, fnf_allowed


def updateDict(
    allowedList: List[str],
) -> Dict[str, Dict[str, Union[List[float], str]]]:
    StrikesAllowed = {}
    if len(allowedList) == 1:
        if "More information" in allowedList[0]:
            text = allowedList[0].split("More information")[0].strip()
        else:
            text = allowedList[0]
        allowedList = [
            "Ne" + i if i.startswith("xt") else "Cu" + i if i.startswith("rrent") else i
            for i in [
                _item
                for item in [item.split(" Ne") for item in text.split(" Cu")]
                for _item in item
            ]
        ]
    for item in allowedList:
        ((nrml, mis,), prd,) = (
            tuple(
                [
                    item.split(" to ") if " to " in item else item
                    for item in item.split("NRML:")[-1].split("MIS:")
                ]
            ),
            item.split("-")[0].strip(),
        )
        StrikesAllowed[prd] = {
            "NRML": (
                {"from": float(nrml[0]), "to": float(nrml[-1])}
                if isinstance(nrml, list)
                else nrml.title()
            ),
            "MIS": (
                {"from": float(mis[0]), "to": float(mis[-1])}
                if isinstance(mis, list)
                else mis.title()
            ),
        }
    return StrikesAllowed


if __name__ == "__main__":
    StrikesAllowed = dict(
        zip(
            ("BankNifty", "Nifty", "FinNifty"),
            tuple(map(updateDict, fetchAllowedLists())),
        )
    )
    with open("StrikesAllowed.json", "w") as jsonFile:
        jsonFile.write(json.dumps(StrikesAllowed))
```


==================================================


## [2/3] Repository: Auto_Trader (`PHASE4-QUANT-151`)
- **Full Name**: `PHASE4-QUANT-151_The-Great-One__Auto_Trader`
- **Description**: AutoTrader Bot is a Python-based stock trading bot for Indian markets, using indicators like MACD, RSI, and EMA. It integrates with Zerodha Kite for real-time trading and supports customizable strategies.
- **GitHub Stars**: 35
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Auto_Trader

Auto_Trader is the live **paper-only RSI momentum rotation pipeline** for NSE equities. It consumes yfinance-fed historical and intraday prices, generates champion-strategy signals, maintains a simulated ledger, and reports status through Hermes.

No real orders are placed. Zerodha Kite is retired and is not a supported price, login, or execution path; the Kite engine service is masked on the server.

## Live data and execution flow

1. A Mac-side Hermes cron fetches NSE quotes with yfinance (Tickertape REST as fallback) and writes `reports/live_prices.json` on the server.
2. `scripts/rsi_momentum_paper_shadow.py` refreshes the paper signal at 10:15 on weekdays. It fails closed: stale (>5d) or thin (<80% coverage) data, or a malformed pick list, suppresses publication and preserves the previous signal file.
3. `scripts/rsi_momentum_paper_ledger.py` marks positions to market every five minutes from 09:00–15:59, rebalancing when it sees a newer signal. Writers are serialized with `/tmp/rsi_ledger.lock`.
4. A Hermes cron reads the latest ledger output and delivers Telegram status.
5. Historical feathers are rebuilt on the Mac with yfinance and synced to the server; Yahoo is not queried from Oracle Cloud.

Nightly strategy research lives in the separate `Trader_Labs` repository (auto-iteration lab, independent of this repository).

### Correct paper execution contract

The shadow publishes a versioned D-close intent with target weights (including inverse-volatility weights), target cash, a stable signal ID, and nullable modeled D+1 opens. The ledger fills whole-share target deltas only from one complete, timezone-aware, strictly fresh `paper_quote_snapshot_v1`; historical opens are slippage diagnostics and never retroactive fills. Fees use actual traded notional, residual cash and target-weight deviations are retained, and consumed signal IDs are idempotent. Authoritative state is atomically committed before its same-revision rebuildable output. This remains paper-only: no live orders are placed.

## Repository contents

- `scripts/rsi_momentum_paper_shadow.py` — champion signal generator.
- `scripts/rsi_momentum_paper_ledger.py` — simulated portfolio, MTM, and rebalance ledger.
- `scripts/rsi_momentum_report.py` and `scripts/rsi_224466_rotation_lab.py` — retained signal/backtest support.
- `scripts/nightly_cleanup.py` and `scripts/prune_report_clutter.py` — generated-report cleanup.
- `tests/` — safety tests for the shadow and ledger.

Generated reports, logs, market data, databases, and secrets are ignored by Git.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The production checkout is `/home/ubuntu/Auto_Trader`. Run tests without invoking the live paper jobs:

```bash
pytest -q
```

Do not manually run the ledger or shadow against production state without an explicit operational reason and the shared ledger lock.

## Deployment

Edit and verify locally, commit to `main`, push to GitHub, then update production with a fast-forward-only pull:

```bash
cd /home/ubuntu/Auto_Trader
git pull --ff-only origin main
```

See `PROJECT_MAP.md` for schedules and operational ownership.

### Core Implementation Code & Architecture
#### File: `tests/fixtures/parity_ohlc.json`
```python
{
  "schema_version": "parity_ohlc_v1",
  "signal_date": "2026-07-17",
  "modeled_execution_date": "2026-07-20",
  "closes": {
    "AAA": [100.0, 101.0, 102.0, 103.0],
    "BBB": [200.0, 198.0, 202.0, 204.0]
  },
  "modeled_opens": {"AAA": 98.0, "BBB": 205.0}
}
```

#### File: `tests/fixtures/live_prices_v1.json`
```python
{
  "schema_version": "paper_quote_snapshot_v1",
  "snapshot_id": "quotes-2026-07-21T10:00:00+05:30",
  "generated_at": "2026-07-21T10:00:00+05:30",
  "prices": {
    "AAA": 100.0,
    "BBB": 200.0,
    "CCC": 50.0
  },
  "price_times": {
    "AAA": "2026-07-21T09:59:58+05:30",
    "BBB": "2026-07-21T09:59:57+05:30",
    "CCC": "2026-07-21T09:59:56+05:30"
  }
}
```

#### File: `tests/fixtures/paper_signal_v2.json`
```python
{
  "schema_version": "paper_signal_v2_target_weights",
  "signal_id": "2bb87437200b05bb8ddaab199bfca073ca30c5fbed28828e5561b897e1eec82b",
  "params_fingerprint": "c896e3bf2dd04ceb14e74289f5197de259253e3ffcf2936e9ac6db233c210128",
  "signal_date": "2026-07-17",
  "modeled_execution_date": "2026-07-20",
  "modeled_execution_open": {
    "AAA": 111.0,
    "BBB": 222.0
  },
  "target_weights": {
    "AAA": 0.6,
    "BBB": 0.3
  },
  "target_cash_weight": 0.1,
  "metadata": {
    "vol_lookback": 10
  }
}
```

#### File: `tests/fixtures/expected_signal_v2.json`
```python
{
  "metadata": {"vol_lookback": 10, "weighting_method": "inverse_volatility"},
  "modeled_execution_date": "2026-07-20",
  "modeled_execution_open": {"AAA": 98.0, "BBB": 205.0},
  "params_fingerprint": "f84d342460dfcb68465f9326ce33ce13c80ed621a208e59f38c73f31b2791304",
  "schema_version": "paper_signal_v2_target_weights",
  "signal_date": "2026-07-17",
  "signal_id": "0146d232795bfd091e5b1521004d35ee2bfd4195600a5e30cb4fbab3d80ba07f",
  "target_cash_weight": 0.1,
  "target_weights": {"AAA": 0.6, "BBB": 0.3}
}
```

#### File: `tests/test_paper_signal_contract.py`
```python
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.signal_schema import build_paper_signal

FIXTURES = Path(__file__).parent / "fixtures"


def test_local_signal_builder_matches_versioned_golden_contract() -> None:
    ohlc = json.loads((FIXTURES / "parity_ohlc.json").read_text())
    expected = json.loads((FIXTURES / "expected_signal_v2.json").read_text())
    actual = build_paper_signal(
        params={"top_n": 2, "vol_weight": True, "vol_lookback": 10},
        signal_date=ohlc["signal_date"],
        target_weights={"AAA": 0.6, "BBB": 0.3},
        target_cash_weight=0.1,
        modeled_execution_date=ohlc["modeled_execution_date"],
        modeled_execution_open=ohlc["modeled_opens"],
        metadata={"weighting_method": "inverse_volatility", "vol_lookback": 10},
    )
    assert actual == expected
```

#### File: `scripts/atomic_io.py`
```python
"""Durable atomic file publication helpers."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any


def atomic_write_json(path: Path, value: Any) -> None:
    """Write JSON beside *path* and atomically replace it after fsync.

    A failed replacement leaves the prior destination untouched and removes the
    unpublished temporary file.
    """
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(
        dir=destination.parent, prefix=f".{destination.name}.", suffix=".tmp"
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
```


==================================================


## [3/3] Repository: zerodha-mcp (`PHASE4-QUANT-150`)
- **Full Name**: `PHASE4-QUANT-150_aptro__zerodha-mcp`
- **Description**: Mcp server to connect with zerodha's kite trade apis
- **GitHub Stars**: 46
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Zerodha MCP Integration
[![smithery badge](https://smithery.ai/badge/@aptro/zerodha-mcp)](https://smithery.ai/server/@aptro/zerodha-mcp)

This project integrates Zerodha's trading platform with Claude AI using the Multi-Cloud Plugin (MCP) framework, allowing you to interact with your Zerodha trading account directly through Claude.

## Setup Instructions

### Installing via Smithery

To install zerodha-mcp for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@aptro/zerodha-mcp):

```bash
npx -y @smithery/cli install @aptro/zerodha-mcp --client claude
```

### 1. Create a Zerodha Developer Account

1. Go to [Kite Connect](https://developers.kite.trade/) and sign up for a developer account
2. Log in to your account at [developers.kite.trade](https://developers.kite.trade/)

### 2. Create a New App

1. Navigate to the "Apps" section in your Kite Developer dashboard
2. Click on "Create a new app"
3. Fill in the required details:
   - App Name: Choose a descriptive name (e.g., "Claude Zerodha Integration")
   - App Category: Select "Personal" or appropriate category
   - Redirect URL: Set to `http://127.0.0.1:5000/zerodha/auth/redirect`
   - Description: Briefly describe your application's purpose
4. Submit the form to create your app

### 3. Get API Credentials

After creating your app, you'll receive:
- API Key (also called Consumer Key)
- API Secret (also called Consumer Secret)

These credentials will be displayed on your app's details page.

### 4. Configure Environment Variables

1. Create a `.env` file in the root directory of this project
2. Add your API credentials to the file:

```
KITE_API_KEY=your_api_key_here
KITE_API_SECRET=your_api_secret_here
```

Replace `your_api_key_here` and `your_api_secret_here` with the actual credentials from step 3.

### 5. Install Dependencies

Make sure you have all required dependencies installed:

```bash
uv pip install kiteconnect fastapi uvicorn python-dotenv httpx
```

### 6. Install MCP config on your Claude desktop app

Install the MCP config on your Claude desktop app:

```bash
mcp install main.py
```

This command registers the Zerodha plugin with Claude, making all trading functionality available to the AI.

## Usage

After setup, you can interact with your Zerodha account via Claude using the following features:

### Authentication

```
Can you please check if I'm logged into my Zerodha account and authenticate if needed?
```

### Stocks and General Trading

- Check account margins: `What are my current margins on Zerodha?`
- View portfolio holdings: `Show me my current holdings on Zerodha`
- Check current positions: `What positions do I currently have open on Zerodha?`
- Get quotes for symbols: `What's the current price of RELIANCE and INFY on NSE?`
- Place an order: `Place a buy order for 10 shares of INFY at market price on NSE`
- Get historical data: `Can you show me the historical price data for SBIN for the last 30 days?`

### Mutual Funds

- View mutual fund holdings: `Show me my mutual fund holdings on Zerodha`
- Get mutual fund orders: `List all my mutual fund orders on Zerodha`
- Place a mutual fund order: `Place a buy order for ₹5000 in the mutual fund with symbol INF090I01239`
- Cancel a mutual fund order: `Cancel my mutual fund order with order ID 123456789`
- View SIP details: `Show all my active SIPs on Zerodha`
- Create a new SIP: `Set up a monthly SIP of ₹2000 for the fund with symbol INF090I01239 for 12 installments`
- Modify an existing SIP: `Change my SIP with ID 987654321 to ₹3000 per month`
- Cancel a SIP: `Cancel my SIP with ID 987654321`
- Browse available mutual funds: `Show me a list of available mutual funds on Zerodha`

## Authentication Flow

The first time you use any Zerodha functionality, Claude will:
1. Start a local server on port 5000
2. Open a browser window for Zerodha login
3. After successful login, store the access token for future sessions

Your session will remain active until the token expires (typically 24 hours). When the token expires, Claude will automatically initiate the login flow again.

## Available MCP Tools

This plugin offers the following MCP tools that Claude can use:

### Authentication
- `check_and_authenticate` - Verifies authentication status and initiates login if needed
- `initiate_login` - Starts the Zerodha login flow
- `get_request_token` - Retrieves the request token after login

### Stock/General Trading
- `get_holdings` - Retrieves portfolio holdings
- `get_positions` - Gets current positions
- `get_margins` - Retrieves account margins
- `place_order` - Places a trading order
- `get_quote` - Gets quotes for specified symbols
- `get_historical_data` - Retrieves historical price data

### Mutual Funds
- `get_mf_orders` - Retrieves mutual fund orders
- `place_mf_order` - Places a mutual fund order
- `cancel_mf_order` - Cancels a mutual fund order
- `get_mf_instruments` - Gets available mutual fund instruments
- `get_mf_holdings` - Retrieves mutual fund holdings
- `get_mf_sips` - Gets active SIPs
- `place_mf_sip` - Creates a new SIP
- `modify_mf_sip` - Modifies an existing SIP
- `cancel_mf_sip` - Cancels a SIP

## Troubleshooting

- If you encounter authentication issues, try removing the `.tokens` file and restart the authentication process
- Make sure your Zerodha credentials in the `.env` file are correct
- Ensure port 5000 is not being used by another application
- For persistent issues, check Zerodha's API status at [status.zerodha.com](https://status.zerodha.com)

## Security Notes

- Your Zerodha API credentials are stored only in your local `.env` file
- Access tokens are stored in the `.tokens` file in the project directory
- No credentials are transmitted to Claude or any third parties
- All authentication happens directly between you and Zerodha's servers

### Core Implementation Code & Architecture
#### File: `pyproject.toml`
```python
[project]
name = "zerodha-mcp"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "fastapi>=0.115.11",
    "httpx>=0.28.1",
    "kiteconnect>=5.0.1",
    "mcp[cli]>=1.3.0",
    "python-dotenv>=1.0.1",
    "uvicorn>=0.34.0",
]
```

#### File: `main.py`
```python
from typing import Any, Dict, List, Optional, AsyncIterator
import os
import httpx
from contextlib import asynccontextmanager
from dataclasses import dataclass
from threading import Thread
import webbrowser
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from mcp.server.fastmcp import FastMCP, Context
from kiteconnect import KiteConnect
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
KITE_API_KEY = os.getenv("KITE_API_KEY")
KITE_API_SECRET = os.getenv("KITE_API_SECRET")
REDIRECT_URL = "http://127.0.0.1:5000/zerodha/auth/redirect"
TOKEN_STORE_PATH = os.path.join(os.path.dirname(__file__), ".tokens")

# Initialize FastAPI app for handling redirect
app = FastAPI(title="Zerodha Login Handler")

# Global variables for auth flow
_request_token: Optional[str] = None


@dataclass
class ZerodhaContext:
    """Typed context for the Zerodha MCP server"""

    kite: KiteConnect
    api_key: str
    api_secret: str
    app: FastAPI
    server_thread: Optional[Thread] = None


def load_stored_token() -> Optional[str]:
    """Load stored access token if it exists"""
    try:
        if os.path.exists(TOKEN_STORE_PATH):
            with open(TOKEN_STORE_PATH, "r") as f:
                return f.read().strip()
    except Exception:
        return None
    return None


def save_access_token(token: str):
    """Save access token to file"""
    try:
        with open(TOKEN_STORE_PATH, "w") as f:
            f.write(token)
    except Exception as e:
        print(f"Warning: Could not save access token: {e}")


def start_server():
    """Start the FastAPI server"""
    print("Starting FastAPI server on http://127.0.0.1:5000")
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="error")


@asynccontextmanager
async def zerodha_lifespan(server: FastMCP) -> AsyncIterator[ZerodhaContext]:
    """Manage application lifecycle for Zerodha integration"""
    # Initialize Kite Connect
    print("Initializing Zerodha context...")

    if not KITE_API_KEY or not KITE_API_SECRET:
        raise ValueError(
            "KITE_API_KEY and KITE_API_SECRET must be set in the .env file"
        )

    kite = KiteConnect(api_key=KITE_API_KEY)

    # Try to load existing token
    stored_token = load_stored_token()
    if stored_token:
        try:
            kite.set_access_token(stored_token)
            # Verify token is still valid with a simple API call
            kite.margins()
            print("Successfully restored previous session")
        except Exception:
            print("Stored token is invalid, will wait for new login...")
            if os.path.exists(TOKEN_STORE_PATH):
                os.remove(TOKEN_STORE_PATH)

    # Create context
    ctx = ZerodhaContext(
        kite=kite,
        api_key=KITE_API_KEY,
        api_secret=KITE_API_SECRET,
        app=app,
    )

    try:
        # Setup FastAPI endpoint for auth callback
        @app.get("/zerodha/auth/redirect")
        async def callback(request_token: str = None, status: str = None):
            """Handle the redirect from Zerodha login"""
            global _request_token

            if status != "success":
                print(f"Login failed with status: {status}")
                raise HTTPException(
                    status_code=400, detail=f"Login failed with status: {status}"
                )
            if not request_token:
                print("No request token received")
                raise HTTPException(status_code=400, detail="No request token received")

            try:
                # Generate session
                print("Generating session with request token")
                data = ctx.kite.generate_session(
                    request_token, api_secret=ctx.api_secret
                )
                access_token = data["access_token"]

                # Save and set the access token
                print("Saving and setting access token")
                save_access_token(access_token)
                ctx.kite.set_access_token(access_token)
                _request_token = request_token
                print("Login successful")

                return HTMLResponse(
                    content="""
                    <html>
                        <body style="font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f5f5f5;">
                            <div style="text-align: center; padding: 2rem; background-color: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                                <h1 style="color: #2ecc71;">Login Successful!</h1>
                                <p>You can close this window now.</p>
                            </div>
                        </body>
                    </html>
                    """
                )
            except Exception as e:
                error_msg = f"Failed to generate session: {str(e)}"
                print(error_msg)
                raise HTTPException(status_code=500, detail=error_msg)

        # Yield the context to the tools
        yield ctx
    finally:
        # Cleanup on shutdown
        print("Shutting down Zerodha context...")
        # Additional cleanup could go here if needed


# Initialize FastMCP server with lifespan and dependencies
mcp = FastMCP(
    "zerodha",
    lifespan=zerodha_lifespan,
    dependencies=["kiteconnect", "fastapi", "uvicorn", "python-dotenv", "httpx"],
)


@mcp.tool()
def initiate_login(ctx: Context) -> Dict[str, Any]:
    """
    Start the Zerodha login flow by opening the login URL in a browser
    and starting a local server to handle the redirect
    """
    try:
        # Reset the request token
        global _request_token
        _request_token = None
        print("Initiating Zerodha login flow")

        # Get strongly typed context
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context

        # Start the local server in a separate thread if not already running
        if not zerodha_ctx.server_thread or not zerodha_ctx.server_thread.is_alive():
            server_thread = Thread(target=start_server)
            server_thread.daemon = True
            server_thread.start()
            zerodha_ctx.server_thread = server_thread

        # Get the login URL
        login_url = zerodha_ctx.kite.login_url()
        print(f"Generated login URL: {login_url}")

        # Open the login URL in browser
        webbrowser.open(login_url)
        print("Opened login URL in browser")

        return {
            "message": "Login page opened in browser. Please complete the login process."
        }
    except Exception as e:
        error_msg = f"Error initiating login: {str(e)}"
        print(error_msg)
        return {"error": error_msg}


@mcp.tool()
def get_request_token(ctx: Context) -> Dict[str, Any]:
    """Get the current request token after login redirect"""
    if _request_token:
        return {"request_token": _request_token}
    return {
        "error": "No request token available. Please complete the login process first."
    }


@mcp.tool()
def get_holdings(ctx: Context) -> List[Dict[str, Any]]:
    """Get user's holdings/portfolio"""
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.holdings()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_positions(ctx: Context) -> Dict[str, Any]:
    """Get user's positions"""
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.positions()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_margins(ctx: Context) -> Dict[str, Any]:
    """Get account margins"""
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.margins()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def place_order(
    ctx: Context,
    tradingsymbol: str,
    exchange: str,
    transaction_type: str,
    quantity: int,
    product: str,
    order_type: str,
    price: Optional[float] = None,
    trigger_price: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Place an order on Zerodha

    Args:
        tradingsymbol: Trading symbol (e.g., 'INFY')
        exchange: Exchange (NSE, BSE, NFO, etc.)
        transaction_type: BUY or SELL
        quantity: Number of shares/units
        product: Product code (CNC, MIS, NRML)
        order_type: Order type (MARKET, LIMIT, SL, SL-M)
        price: Price for LIMIT orders
        trigger_price: Trigger price for SL orders
    """
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.place_order(
            variety="regular",
            exchange=exchange,
            tradingsymbol=tradingsymbol,
            transaction_type=transaction_type,
            quantity=quantity,
            product=product,
            order_type=order_type,
            price=price,
            trigger_price=trigger_price,
        )
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_quote(ctx: Context, symbols: List[str]) -> Dict[str, Any]:
    """
    Get quote for symbols

    Args:
        symbols: List of symbols (e.g., ['NSE:INFY', 'BSE:RELIANCE'])
    """
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.quote(symbols)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_historical_data(
    ctx: Context, instrument_token: int, from_date: str, to_date: str, interval: str
) -> List[Dict[str, Any]]:
    """
    Get historical data for an instrument

    Args:
        instrument_token: Instrument token
        from_date: From date (format: 2024-01-01)
        to_date: To date (format: 2024-03-13)
        interval: Candle interval (minute, day, 3minute, etc.)
    """
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.historical_data(
            instrument_token=instrument_token,
            from_date=from_date,
            to_date=to_date,
            interval=interval,
        )
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def check_and_authenticate(ctx: Context) -> Dict[str, Any]:
    """
    Check if Kite is authenticated and initiate authentication if needed.
    Returns the authentication status and any relevant messages.
    """
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context

        # First try to load existing token
        stored_token = load_stored_token()
        if stored_token:
            try:
                zerodha_ctx.kite.set_access_token(stored_token)
                # Verify token is still valid with a simple API call
                zerodha_ctx.kite.margins()
                return {
                    "status": "authenticated",
                    "message": "Already authenticated with valid token",
                }
            except Exception:
                print("Stored token is invalid, will initiate new login...")
                if os.path.exists(TOKEN_STORE_PATH):
                    os.remove(TOKEN_STORE_PATH)

        # If we reach here, we need to authenticate
        # Call the existing initiate_login function
        login_result = initiate_login(ctx)

        if "error" in login_result:
            return {"status": "error", "message": login_result["error"]}

        return {"status": "login_initiated", "message": login_result["message"]}

    except Exception as e:
        error_msg = f"Error checking/initiating authentication: {str(e)}"
        print(error_msg)
        return {"status": "error", "message": error_msg}


# Mutual Fund Tools


@mcp.tool()
def get_mf_orders(ctx: Context) -> List[Dict[str, Any]]:
    """Get all mutual fund orders"""
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.mf_orders()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def place_mf_order(
    ctx: Context,
    tradingsymbol: str,
    transaction_type: str,
    amount: float,
    tag: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Place a mutual fund order

    Args:
        tradingsymbol: Trading symbol (e.g., 'INF090I01239')
        transaction_type: BUY or SELL
        amount: Amount to invest or redeem
        tag: Optional tag for the order
    """
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.place_mf_order(
            tradingsymbol=tradingsymbol,
            transaction_type=transaction_type,
            amount=amount,
            tag=tag,
        )
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def cancel_mf_order(ctx: Context, order_id: str) -> Dict[str, Any]:
    """
    Cancel a mutual fund order

    Args:
        order_id: Order ID to cancel
    """
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.cancel_mf_order(order_id=order_id)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_mf_instruments(ctx: Context) -> List[Dict[str, Any]]:
    """Get all available mutual fund instruments"""
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.mf_instruments()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_mf_holdings(ctx: Context) -> List[Dict[str, Any]]:
    """Get user's mutual fund holdings"""
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.mf_holdings()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_mf_sips(ctx: Context) -> List[Dict[str, Any]]:
    """Get all mutual fund SIPs"""
    try:
        zerodha_ctx: ZerodhaContext = ctx.request_context.lifespan_context
        return zerodha_ctx.kite.mf_sips()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def place_mf_sip(
    ctx: Context,
    tradingsymbol: str,
    amount: float,
    instalments: int,
    frequency: str,
    initial_amount: Optional[float] = None,
    instalment_day: Optional[int] = None,
    tag: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Place a mutual fund SIP (Systematic Investment Plan)

    Args:
        tradingsymbol: Trading symbol (e.g., 'INF090I01239')
        amount: Amount per instalment
        instalments: Number of instalments (minimum 6)
        frequency: weekly, monthly, or quarterly
        initial_amount: Optional initial amount
        instalment_day: Optional day of month/week for instalment (1-31 for monthly, 1-7 for weekly
# ... [TRUNCATED FILE CONTENT]
```


==================================================
