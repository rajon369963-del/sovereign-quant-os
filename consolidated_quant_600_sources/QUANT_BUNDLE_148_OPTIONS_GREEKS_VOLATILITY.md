# ⚡ [QUANT-SOURCE-148] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_148_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Extract-Historical-Data-from-NSE-for-FUTURE-OPTION (`VAULT_IN-QUANT-056_Khushalsawant__Extract-Historical-Data-from-NSE-for-FUTURE-OPTION`)
- **Full Name**: `IN-QUANT-056_Khushalsawant__Extract-Historical-Data-from-NSE-for-FUTURE-OPTION`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Extract-Historical-Data-from-NSE-for-FUTURE-OPTION
Extract Historical Data from NSE for FUTURE/OPTION

### Core Implementation Code & Architecture
#### File: `Historical_data_NSE_FUTURE_OPTION.py`
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:08:08 2019

@author: khushal
"""


import time
start_time = time.time()


from urllib.request import build_opener, HTTPCookieProcessor, Request
from urllib.parse import urlencode
from http.cookiejar import CookieJar

import datetime
import zipfile

import io
import pandas as pd
import numpy as np
import requests

from io import StringIO


"https://www.nseindia.com/content/historical/DERIVATIVES/2019/JUN/fo03JUN2019bhav.csv.zip"

def get_bhavcopy_url(d):
    """take date and return bhavcopy url"""
    bhavcopy_base_url = "https://www.nseindia.com/content/historical/DERIVATIVES/%s/%s/fo%sbhav.csv.zip"
    
    year = d.strftime('%Y')
    #print(year)
    month = d.strftime('%b').upper()
    #print(month)
    date = d.strftime('%d%b%Y').upper()
    #print(date)
    url = bhavcopy_base_url % (year, month, date)
    return url

def exract_NSE_FO_historical_data(date_value_df,FO_historical_data_df):
    ''' exract_NSE_FO_historical_data '''
    path_for_zip_extract = "C:/Users/khushal/Downloads/FO_Historical_data"
    opener = nse_opener()
    #print("date_value_df = ",date_value_df)
    for d in date_value_df:
        NSE_URL = get_bhavcopy_url(d)
        response = requests.get(NSE_URL)        # To execute get request 
        if response.status_code == 200:
            response = opener.open(Request(NSE_URL, None, headers))
            
            zip_file_handle = io.BytesIO(response.read())
            zf = zipfile.ZipFile(zip_file_handle)
            filename = "fo"+d.strftime('%d%b%Y').upper()+"bhav.csv"
            
            bytes_data = zf.read(filename)
            s=str(bytes_data,'utf-8')
            
            #print(type(bytes_data))
            
            # Access file from memory space
            data = StringIO(s) 
            df=pd.read_csv(data)
            
            #print(df)
            FO_historical_data_df = FO_historical_data_df.append(df)
            # printing all the contents of the zip file 
            #zf.printdir('File Name') 
            
            # extracting all the files 
            #zf.extractall(path_for_zip_extract)
            print(" Extractig file for %s" %d.strftime('%d%b%Y').upper())
        elif response.status_code != 200:
            print("status_code = ",response.status_code)
            print("For %s  , NSE_URL is Un-reachable " %d.strftime('%d%b%Y').upper())
    
    #print(FO_historical_data_df)
    final_file_details = path_for_zip_extract + "FO_historical_data.csv"
    FO_historical_data_df.to_csv(final_file_details)
    return FO_historical_data_df
    

def nse_opener():
    """
    builds opener for urllib2
    :return: opener object
    """
    cj = CookieJar()
    return build_opener(HTTPCookieProcessor(cj))

def convert_sec(n): 
    return str(datetime.timedelta(seconds = n))

if __name__ == "__main__":
    FO_historical_data_df = pd.DataFrame()    
    headers = {'Accept' : '*/*',
                'Accept-Language' : 'en-US,en;q=0.5',
                'Host': 'nseindia.com',
                'Referer': "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=INFY&illiquid=0&smeFlag=0&itpFlag=0",
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
                'X-Requested-With': 'XMLHttpRequest'
                }
    Start_date = datetime.datetime.now() + datetime.timedelta(-8)
    Current_date = datetime.datetime.now() + datetime.timedelta(-1)
    date_value_df = pd.date_range(start=Start_date, end=Current_date)
    
    FO_historical_data_df = exract_NSE_FO_historical_data(date_value_df,FO_historical_data_df)
    '''
    URL = get_bhavcopy_url(d)
    response = requests.get(URL,verify=False)        # To execute get request 

    print("status_code = ",response.status_code) 
    #.strftime("%d%b%Y")
    '''
    n =  time.time() - start_time
    print("---Execution Time ---",convert_sec(n))
```


==================================================


## [2/3] Repository: nse-options-data-collector (`VAULT_IN-QUANT-064_BarathGB007__nse-options-data-collector`)
- **Full Name**: `IN-QUANT-064_BarathGB007__nse-options-data-collector`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# NSE Options Data Collector

Automated data collection pipeline for NSE F&O — collects OI, full option chains (Greeks, IV, bid/ask), global cues, and EOD data for **37 symbols** (2 indices + 35 stocks). Saves to parquet files ready for ML/analysis.

Built for Upstox API. Uses the analytics token (valid 1 year, no daily refresh).
Instrument keys and lot sizes are resolved automatically from the API — just add a stock name and it works.

## What It Collects

| Collector | Schedule (IST) | Data |
|-----------|---------------|------|
| **Pre-market** | 8:45 AM, 10:00 AM | S&P 500, NASDAQ, Dow, US VIX, crude, gold, USDINR, DXY, Hang Seng, Nikkei |
| **OI Snapshot** | Every 15 min 9:20-15:29 (26/day) | OI summary, PCR, ATM bid/ask, max OI strikes, OI signals (long build/short cover) |
| **Option Chain** | Every 15 min 9:20-15:29 (26/day) | All strikes x CE/PE: OI, volume, LTP, bid, ask, IV, delta, theta, gamma, vega |
| **CAS Closing** | 15:42 | CAS-determined closing price + divergence from continuous close |
| **EOD** | 16:00 | 5-min candles (37 symbols), sector indices, FII/DII flows, VIX intraday, futures basis, market breadth |

### Symbols (37)

**Indices:** NIFTY, BANKNIFTY

**Stocks:** RELIANCE, TCS, HDFCBANK, INFY, ICICIBANK, BHARTIARTL, SBIN, ITC, LT, HINDUNILVR, KOTAKBANK, AXISBANK, MARUTI, SUNPHARMA, TITAN, BAJFINANCE, WIPRO, HCLTECH, ADANIENT, TATAMOTORS, TATASTEEL, POWERGRID, NTPC, ONGC, COALINDIA, JSWSTEEL, DRREDDY, BAJAJFINSV, ASIANPAINT, TECHM, INDUSINDBK, M&M, CIPLA, EICHERMOT, SBILIFE

## Quick Setup

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/nse-options-data-collector.git
cd nse-options-data-collector

# Install
pip install -r requirements.txt

# Configure — get token from https://account.upstox.com/developer/apps
cp .env.example .env
# Edit .env and paste your Upstox analytics token

# Test — collect a single snapshot
python examples/quick_start.py

# Run all collectors (full day)
python start_collectors.py
```

## Usage

### Automated daily collection
```bash
python start_collectors.py
```
Launches all 3 collectors in parallel. Runs from 8:45 AM to 4:15 PM IST. Press Ctrl+C to stop.

### Individual collectors
```bash
# OI + Chain (every 15 min)
python -m collectors.oi_collector --schedule

# Single snapshot
python -m collectors.oi_collector              # OI only
python -m collectors.oi_collector --chain      # Full chain only
python -m collectors.oi_collector --cas        # CAS closing only

# Pre-market global cues
python -m collectors.premarket_collector --schedule
python -m collectors.premarket_collector       # Single fetch

# EOD data
python -m collectors.eod_collector --schedule  # Wait for 16:00 then run
python -m collectors.eod_collector             # Run immediately
python -m collectors.eod_collector --candles   # 5-min candles only
python -m collectors.eod_collector --fii       # FII/DII only
python -m collectors.eod_collector --sectors   # Sector indices only
```

### Check collected data
```bash
python -m collectors.oi_collector --info
python -m collectors.eod_collector --info
python examples/explore_data.py
```

## Data Format

All data is saved as **parquet** files in `data/`:

```
data/
├── oi_snapshots/
│   ├── oi_2025-08-05.parquet        # 26 snapshots x 37 symbols/day
│   └── cas_2025-08-05.parquet       # CAS closing prices
├── option_chain/
│   └── chain_2025-08-05.parquet     # ~1400 strikes x 26 snapshots/day
├── global_cues/
│   └── global_2025-08-05.parquet    # Pre-market + Asian data
└── eod/
    ├── candles_5min/
    │   ├── NIFTY_2025-08-05.parquet
    │   └── RELIANCE_2025-08-05.parquet
    ├── sectors_2025-08-05.parquet
    ├── fii_dii_2025-08-05.parquet
    ├── futures_basis_2025-08-05.parquet
    └── breadth_2025-08-05.parquet
```

### OI Snapshot columns (26 per symbol per day)
`timestamp, symbol, expiry, spot, total_ce_oi, total_pe_oi, pcr, max_ce_oi, max_ce_oi_strike, max_pe_oi, max_pe_oi_strike, atm_strike, atm_ce_ltp, atm_ce_bid, atm_ce_ask, atm_pe_ltp, atm_pe_bid, atm_pe_ask, ce_oi_signal, pe_oi_signal, oi_change_pct, ce_oi_change_pct, pe_oi_change_pct, pcr_change`

### Option Chain columns (per strike row)
`timestamp, symbol, expiry, spot, strike, ce_oi, ce_volume, ce_ltp, ce_bid, ce_ask, ce_iv, ce_delta, ce_theta, ce_gamma, ce_vega, pe_oi, pe_volume, pe_ltp, pe_bid, pe_ask, pe_iv, pe_delta, pe_theta, pe_gamma, pe_vega`

### Sample Data

Check `examples/sample_data/` for real CSV snapshots so you can see exactly what the collectors produce before running them:

| File | Description |
|------|-------------|
| `oi_snapshot_sample.csv` | 5-symbol OI snapshot (BANKNIFTY, RELIANCE, TCS, HDFCBANK, INFY) |
| `option_chain_sample.csv` | NIFTY ATM ±2 strikes with full Greeks (delta, theta, gamma, vega, IV) |
| `global_cues_sample.csv` | Pre-market (S&P, NASDAQ, crude, gold, USDINR) + Asian session (Hang Seng, Nikkei) |

## Adding Your Own Symbols

Just add the stock's NSE trading symbol to the `STOCKS` list in `config.py`:

```python
STOCKS = [
    "RELIANCE", "TCS", "HDFCBANK",
    # ... existing stocks ...
    "BAJAJ-AUTO",   # <-- add your symbol here
    "TATAPOWER",
]
```

That's it. The collector automatically:
1. **Resolves instrument keys** via Upstox Symbol Search API (`/v2/instruments/search`) — no need to look up ISINs
2. **Fetches lot sizes** from the API (`/v2/option/contract`) — no hardcoded lot size tables
3. **Caches keys** to `data/oi_snapshots/_instrument_keys.json` so it only searches once per symbol

Also add the symbol to the `SYMBOLS` list in `collectors/eod_collector.py` if you want EOD candles for it.

## VPS Deployment (Oracle Cloud Free Tier)

Deploy to a free Oracle Cloud VM for automated daily collection without keeping your PC on.

### 1. Create VM
- Oracle Cloud Console → Compute → Instances → Create
- **Image:** Ubuntu 22.04
- **Shape:** VM.Standard.E2.1.Micro (free tier — 1 OCPU, 1GB RAM)
- **Boot volume:** 50GB (free tier, ~19 years of data)

### 2. Deploy
```bash
# From local PC — copy code to VPS
scp -i ~/.ssh/oracle_vps -r . ubuntu@YOUR_VPS_IP:~/nse-collector/

# SSH into VPS
ssh -i ~/.ssh/oracle_vps ubuntu@YOUR_VPS_IP

# Run setup
bash ~/nse-collector/deploy/setup_vps.sh

# Set token (NEVER copy your full .env)
echo "UPSTOX_ACCESS_TOKEN=your_token_here" > ~/nse-collector/.env

# Test
~/nse-collector/deploy/run_collectors.sh
```

### 3. Sync data to local PC
```bash
# Edit deploy/sync_data.sh — set your VPS_IP
bash deploy/sync_data.sh
```

Cron runs automatically: start at 8:15 AM, stop at 4:15 PM, weekdays only.

## Storage Estimate

| Data | Per Day | Per Month | Per Year |
|------|---------|-----------|----------|
| OI snapshots | ~250 KB | ~5.5 MB | ~65 MB |
| Option chain | ~9 MB | ~200 MB | ~2.4 GB |
| Global cues | ~5 KB | ~110 KB | ~1.3 MB |
| EOD data | ~500 KB | ~11 MB | ~130 MB |
| **Total** | **~10 MB** | **~220 MB** | **~2.6 GB** |

## API Notes

- Uses Upstox **analytics token** — valid for 1 year, no daily OAuth refresh
- Market data endpoints only — no order placement functions included
- Rate limiting handled automatically (429 backoff + retry)
- Network timeout retry with exponential backoff (up to 3 retries)
- NSE market hours: 9:15-15:30 IST. Pre-market 9:00-9:08 has limited data
- CAS auction: 15:30-15:40 IST. CAS closing price available after 15:40

## License

MIT

### Core Implementation Code & Architecture
#### File: `collectors/__init__.py`
```python

```

#### File: `utils/__init__.py`
```python

```

#### File: `start_collectors.py`
```python
"""
Data Collection Launcher — starts all 3 collectors in parallel.

  1. premarket_collector  — 8:45 AM (global cues) + 10:00 AM (Asian)
  2. oi_collector         — every 15 min 9:20-15:29 (OI + chain) + 15:42 (CAS close + divergence)
  3. eod_collector        — 16:00 (candles, sectors, FII/DII, VIX, basis, breadth)

Usage:
    python start_collectors.py
"""

import subprocess
import sys
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def main():
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    collectors = [
        ("premarket_collector", [sys.executable, "-m", "collectors.premarket_collector", "--schedule"]),
        ("oi_collector",        [sys.executable, "-m", "collectors.oi_collector", "--schedule"]),
        ("eod_collector",       [sys.executable, "-m", "collectors.eod_collector", "--schedule"]),
    ]

    procs = []
    for name, cmd in collectors:
        print(f"[LAUNCH] {name}: {' '.join(cmd)}")
        p = subprocess.Popen(cmd, cwd=BASE, env=env)
        procs.append((name, p))

    print(f"\n[OK] All {len(procs)} collectors running. Ctrl+C to stop.\n")

    try:
        for name, p in procs:
            p.wait()
            print(f"[DONE] {name} (exit {p.returncode})")
    except KeyboardInterrupt:
        print("\n[STOP] Shutting down...")
        for name, p in procs:
            p.terminate()
        for name, p in procs:
            p.wait()
        print("[STOPPED]")


if __name__ == "__main__":
    main()
```

#### File: `utils/expiry_manager.py`
```python
"""
Expiry Manager — DTE calculation, expiry classification.
"""

from datetime import date, timedelta

import utils.upstox_data as ud
from utils.logger import get_logger

log = get_logger("expiry_mgr")


def get_dte(expiry_str: str) -> int:
    """Days to expiry from today. 0 = expiring today, negative = expired."""
    return (date.fromisoformat(expiry_str) - date.today()).days


def is_expiry_day(symbol: str) -> bool:
    nearest = ud.get_nearest_expiry(symbol)
    if not nearest:
        return False
    return get_dte(nearest) == 0


def get_next_expiry(symbol: str) -> str | None:
    """Get the expiry after the nearest one."""
    expiries = ud.get_expiry_dates(symbol)
    if len(expiries) >= 2:
        return expiries[1]
    return _fallback_next_expiry(symbol)


WEEKLY_SYMBOLS = {"NIFTY"}


def _last_tuesday_of_month(year: int, month: int) -> date:
    if month == 12:
        first_next = date(year + 1, 1, 1)
    else:
        first_next = date(year, month + 1, 1)
    d = first_next - timedelta(days=1)
    while d.weekday() != 1:
        d -= timedelta(days=1)
    return d


def _fallback_next_expiry(symbol: str) -> str:
    d = date.today() + timedelta(days=2)
    if symbol in WEEKLY_SYMBOLS:
        while d.weekday() != 1:
            d += timedelta(days=1)
        return d.isoformat()
    exp = _last_tuesday_of_month(d.year, d.month)
    if exp >= d:
        return exp.isoformat()
    if d.month == 12:
        return _last_tuesday_of_month(d.year + 1, 1).isoformat()
    return _last_tuesday_of_month(d.year, d.month + 1).isoformat()
```

#### File: `examples/quick_start.py`
```python
"""
Quick Start — collect a single OI + chain snapshot and display results.

Usage:
    cd nse-options-data-collector
    python examples/quick_start.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

from collectors.oi_collector import collect_snapshot, save_snapshot
from collectors.oi_collector import collect_chain_snapshot, save_chain_snapshot

print("=== Collecting OI Snapshot (37 symbols) ===\n")
oi_df = collect_snapshot()
if not oi_df.empty:
    save_snapshot(oi_df)
    print(f"\nCollected {len(oi_df)} symbols:")
    print(oi_df[["symbol", "spot", "total_ce_oi", "total_pe_oi", "pcr"]].to_string(index=False))
else:
    print("No OI data collected — check your UPSTOX_ACCESS_TOKEN")
    sys.exit(1)

print("\n=== Collecting Full Option Chain (all strikes) ===\n")
chain_df = collect_chain_snapshot()
if not chain_df.empty:
    save_chain_snapshot(chain_df)
    symbols = chain_df["symbol"].nunique()
    strikes = len(chain_df)
    print(f"\nCollected: {symbols} symbols, {strikes} strike rows")
    print(f"\nSample (NIFTY ATM +/- 2 strikes):")
    nifty = chain_df[chain_df["symbol"] == "NIFTY"]
    if not nifty.empty:
        spot = nifty["spot"].iloc[0]
        near_atm = nifty.iloc[(nifty["strike"] - spot).abs().argsort()[:5]]
        print(near_atm[["strike", "ce_ltp", "ce_iv", "ce_delta", "ce_oi",
                         "pe_ltp", "pe_iv", "pe_delta", "pe_oi"]].to_string(index=False))
else:
    print("No chain data collected")

print("\n=== Data saved to data/ directory ===")
```

#### File: `utils/logger.py`
```python
"""
Logging — daily file + console.

Usage:
    from utils.logger import get_logger
    log = get_logger("oi_collector")
    log.info("message")
"""

import logging
import sys
import os
from datetime import datetime
from pathlib import Path


_setup_done = False


def setup_logging(log_dir: str = None, process_name: str = "collector") -> None:
    """One-time setup: root logger with console + daily file handlers."""
    global _setup_done
    if _setup_done:
        return

    if log_dir is None:
        log_dir = str(Path(__file__).parent.parent / "logs")
    os.makedirs(log_dir, exist_ok=True)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    if sys.platform == "win32":
        stream = open(sys.stdout.fileno(), mode="w", encoding="utf-8", closefd=False)
    else:
        stream = sys.stdout

    console = logging.StreamHandler(stream=stream)
    console.setLevel(logging.INFO)
    console.setFormatter(fmt)
    root.addHandler(console)

    log_file = os.path.join(log_dir, f"{process_name}_{datetime.now().strftime('%Y%m%d')}.log")
    file_h = logging.FileHandler(log_file, encoding="utf-8")
    file_h.setLevel(logging.DEBUG)
    file_h.setFormatter(fmt)
    root.addHandler(file_h)

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    _setup_done = True


def get_logger(name: str) -> logging.Logger:
    """Get a named logger. Auto-calls setup_logging() on first use."""
    if not _setup_done:
        setup_logging()
    return logging.getLogger(name)
```


==================================================


## [3/3] Repository: option-chain-refresher (`VAULT_IN-QUANT-069_g-ravity__option-chain-refresher`)
- **Full Name**: `IN-QUANT-069_g-ravity__option-chain-refresher`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Option Chain Refresher

A simple web app to fetch NSE option chain values alongwith delta greek, every 1 min

### Core Implementation Code & Architecture
#### File: `.codesandbox/workspace.json`
```python
{
  "responsive-preview": {
    "Mobile": [
      320,
      675
    ],
    "Tablet": [
      1024,
      765
    ],
    "Desktop": [
      1400,
      800
    ],
    "Desktop  HD": [
      1920,
      1080
    ]
  }
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src"
  ]
}
```

#### File: `package.json`
```python
{
  "name": "react-typescript",
  "version": "1.0.0",
  "description": "React and TypeScript example starter project",
  "keywords": [
    "typescript",
    "react",
    "starter"
  ],
  "main": "src/index.tsx",
  "dependencies": {
    "rc-table": "7.17.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "^4.0.3"
  },
  "devDependencies": {
    "@types/react": "17.0.0",
    "@types/react-dom": "17.0.0",
    "typescript": "^4.1.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
  },
  "browserslist": [
    ">0.2%",
    "not dead",
    "not ie <= 11",
    "not op_mini all"
  ]
}
```


==================================================
