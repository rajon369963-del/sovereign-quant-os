# ⚡ [QUANT-SOURCE-028] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_028_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: nse-data-resources (`WHEEL_nse-data-resources`)
- **Full Name**: `nse-data-resources`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# NSE BSE Market Data Resources for Algorithmic Trading India

A comprehensive guide to **NSE/BSE market data sources**, APIs, tools, and providers for **algorithmic trading in India**. Maintained by [Trade Vectors](https://tradevectors.com) — Mumbai's algo trading specialists.

---

## Contents
- [Official Data Sources](#official-data-sources)
- [Free Data APIs](#free-data-apis)
- [Paid Data Providers](#paid-data-providers)
- [Python Data Libraries](#python-data-libraries)
- [Historical Data Sources](#historical-data-sources)
- [Real-Time Data Feeds](#real-time-data-feeds)
- [Options & F&O Data](#options--fo-data)
- [Commodity Data MCX](#commodity-data-mcx)

---

## Official Data Sources

| Source | Type | URL | Cost |
|---|---|---|---|
| NSE India | Official equities data | nseindia.com | Free |
| BSE India | Official equities data | bseindia.com | Free |
| SEBI | Regulatory + market data | sebi.gov.in | Free |
| RBI | Macro/economic data | rbi.org.in | Free |
| MCX India | Commodity data | mcxindia.com | Free |
| NCDEX | Agricultural commodity data | ncdex.com | Free |

---

## Free Data APIs

### Python Libraries for Free NSE/BSE Data

```python
# 1. nsepy — NSE historical data
pip install nsepy

from nsepy import get_history
from datetime import date

# Get Nifty 50 historical data
nifty_data = get_history(
    symbol="NIFTY",
    start=date(2023, 1, 1),
    end=date(2024, 12, 31),
    index=True
)
print(nifty_data.head())
```

```python
# 2. yfinance — Yahoo Finance data for Indian stocks
pip install yfinance

import yfinance as yf

# Download Reliance Industries data
reliance = yf.download("RELIANCE.NS", start="2023-01-01", end="2024-12-31")
print(reliance.tail())

# Nifty 50 index
nifty = yf.download("^NSEI", period="1y", interval="1d")
```

```python
# 3. nsetools — Live NSE quotes
pip install nsetools

from nsetools import Nse
nse = Nse()

# Get live stock quote
quote = nse.get_quote('infy')  # Infosys
print(quote)

# Get top gainers
gainers = nse.get_top_gainers()
```

---

## Paid Data Providers

| Provider | Data Type | Markets | Price Range |
|---|---|---|---|
| **TrueData** | Real-time + Historical | NSE, BSE, MCX | ₹3,000-15,000/month |
| **Global DataFeeds** | Tick data + OHLCV | NSE, BSE, MCX | ₹2,000-10,000/month |
| **iQuesta** | Market data platform | NSE, BSE | ₹5,000+/month |
| **Quandl (Nasdaq DL)** | Historical data | Multiple | $50+/month |
| **Refinitiv (Reuters)** | Premium financial data | Global | Enterprise |
| **Bloomberg Terminal** | Comprehensive data | Global | Enterprise |

---

## Historical Data Sources

### Free Historical Data
- **NSE Website**: Bhavcopy files (daily OHLCV for all stocks)
- **BSE Website**: Daily bhavcopy download
- **Yahoo Finance**: Up to 10+ years via `yfinance`
- **Zerodha Kite API**: 60-day candle data (free with account)

### Downloading NSE Bhavcopy (Free Daily OHLCV)

```python
import requests
import pandas as pd
from datetime import datetime, timedelta

def download_nse_bhavcopy(date_str):
    """Download NSE bhavcopy for a given date (DDMMYYYY format)"""
    url = f"https://www.nseindia.com/content/historical/EQUITIES/{date_str[:4]}/{date_str[2:5].upper()}/cm{date_str}bhav.csv.zip"
    # Note: NSE requires session cookies for download
    print(f"Bhavcopy URL for {date_str}: {url}")
    return url

# Example usage
download_nse_bhavcopy("10MAR2026")
```

---

## Real-Time Data Feeds

### WebSocket Data via Zerodha Kite

```python
from kiteconnect import KiteTicker

kws = KiteTicker("your_api_key", "your_access_token")

def on_ticks(ws, ticks):
    """Callback to receive ticks"""
    for tick in ticks:
        print(f"Token: {tick['instrument_token']}, LTP: {tick['last_price']}")

def on_connect(ws, response):
    """Subscribe to Nifty 50 on connect"""
    ws.subscribe([256265])  # Nifty 50 token
    ws.set_mode(ws.MODE_FULL, [256265])

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()
```

---

## Options & F&O Data

| Source | Type | Data Available |
|---|---|---|
| NSE Official | Free | Options chain, OI, PCR |
| Sensibull | Freemium | Options analytics, Greeks |
| Opstra | Freemium | Strategy builder, OI analysis |
| Zerodha Kite API | With account | Live F&O quotes, OI |
| Upstox API | With account | F&O OHLCV, OI data |

```python
# Fetch NSE Options Chain
import requests

def get_nifty_options_chain():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.nseindia.com"
    }
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)
    response = session.get(url, headers=headers)
    return response.json()
```

---

## Commodity Data MCX

- **MCX Official**: [mcxindia.com](https://www.mcxindia.com) — Free daily prices
- **Gold/Silver**: Live prices via MCX API or broker APIs
- **Crude Oil**: NYMEX prices via global data providers
- **Agricultural**: NCDEX data for agri commodities

---

## About Trade Vectors

**Trade Vectors** is a Mumbai-based algorithmic trading company specializing in data-driven trading strategies, automated systems, and algo trading education for NSE/BSE/MCX India.

We help traders build reliable data pipelines for their trading systems.

Visit **[tradevectors.com](https://tradevectors.com)** for algo trading courses, consulting, and automated trading solutions.

**Contact:** [tradevectors.com](https://tradevectors.com) | [@tradevectors](https://twitter.com/tradevectors)

---
*Keywords: NSE data API India, BSE market data, NSE historical data Python, free stock market data India, real-time NSE data, options chain data India, NSE bhavcopy download, algo trading data India*


==================================================


## [2/3] Repository: nse-derivatives-warehouse (`WHEEL_nse-derivatives-warehouse`)
- **Full Name**: `nse-derivatives-warehouse`
- **Description**: Reproducible NSE derivatives market-data warehouse over the DhanHQ API — 98M rows, with the audit layer that proves it correct.
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# NSE Derivatives Data Warehouse

A reproducible market-data warehouse for Indian equity and options data, built
on the DhanHQ API. It ingests five years of 15-minute option bars, daily and
intraday equity bars, and NSE bhavcopy reference data into a single queryable
store — and, just as importantly, it ships the tooling that proves the store is
correct.

**Current contents**

| | |
|---|---|
| Rows | 98,011,926 |
| On disk | ~37 GB (SQLite) |
| Stock option chains | 207 underlyings |
| Index option chains | 2 (NIFTY, BANKNIFTY) |
| Equity series | 500 (Nifty 500) |
| Index series | 2 |
| Coverage | Aug 2021 → Aug 2026 |

> **Note on scope.** This repository contains the data platform only. The
> trading strategies, backtest engines and performance reports built on top of
> it are private and are not published here.

---

## What it can reconstruct

Both figures below are generated directly from the warehouse by
[`make_figures.py`](make_figures.py) — no cached numbers, no hand-entered
values. Re-run it against your own copy and it redraws from whatever the
database holds.

![NIFTY weekly volatility smile](docs/volatility_smile.png)

The smile steepens sharply into expiry: at-the-money implied volatility sits
near 13% on expiry day while strikes 2% away price above 30%, whereas four to
seven days out the curve is almost flat.

The expiry dates behind that chart are **detected from the data**, not read
from a calendar — `expiry.py` finds the sessions where the at-the-money
straddle collapses toward zero. That is not over-engineering: NSE moved the
weekly expiry weekday during 2025 and discontinued BANKNIFTY weeklies
entirely, and a hardcoded calendar would keep running while silently reading
the wrong contract.

![Implied volatility across the NSE single-stock universe](docs/iv_universe.png)

Coverage is the whole listed universe rather than a sample — 207 single-stock
underlyings, from ITC near 17% to IDEA near 50%, against a universe median of
27.9%.

![One NSE trading session at 15-minute resolution](docs/intraday_session.png)

Resolution goes down to 15 minutes, so a single session resolves: implied
volatility decays steadily from the open, and turnover traces the familiar
U-shape, heaviest at the open, thinnest around midday, rising again into the
close.

Expiry sessions are excluded from that average on purpose. In the last bar
before expiry the at-the-money premium is nearly gone, and implied volatility
inverted from a near-zero premium is ill-conditioned — the expiry-day mean at
15:15 is 55.6% against 13.3% on every other day. That is arithmetic, not
volatility, and it is the kind of thing worth knowing before it ends up in a
result.

---

## Why this exists

Vendor market data is not clean, and the ways it is unclean are quiet. A
download that reports success can still leave you with another symbol's prices
under your symbol's name, a series that ends silently in 2023, or a strike that
means something different from the spot price sitting in the same row.

None of those announce themselves. They surface later as a backtest result that
is wrong in a direction you cannot detect from the result alone.

So the goal here was never just "download the data". It was to build an
ingestion layer that fails loudly, plus an audit layer that can answer *"is this
still true?"* on demand — and to write down every defect found along the way.

## Defects found and fixed

Each of these was live in the pipeline and silently wrong before it was caught.

| Defect | Consequence |
|---|---|
| `instrument` hardcoded to `OPTIDX` | `securityId` collides across segments — ADANIENT was storing BANKNIFTY's tape, ABB was storing NIFTY's. 1.36M rows destroyed and re-pulled. |
| HTTP 429 not retried | Rate-limited chunks were dropped, and because resume works off `MAX(timestamp)` the watermark moved past them. Permanent, invisible holes. |
| Early-exit probed the **oldest** chunk | Recently listed names (LICI, HYUNDAI) returned nothing for 2021 and were marked "no data", discarding their entire real history. |
| `securityId` resolved to the wrong series | MOTHERSON and CHOLAFIN matched a `D1` row instead of `EQ`, returning zero rows. |
| Adjusted equity price used for strike selection | Back-adjusted spot against raw strikes picks nonsense strikes — one case selected strike 370 for a stock trading near 1,840. |
| Per-symbol expiry inference | Stock tapes are too sparse to infer expiry from straddle collapse; measured 3.7–122 expiries/year where 12 are due. |
| Concurrent scrip-master downloads | Four workers pulling the same 26 MB file hung each other and risked a torn cache. |
| Lot-size parsing split on the first hyphen | `BAJAJ-AUTO` silently had no lot size. |
| 26 failed chunks across 8 symbols | Refilled by `backfill.py`, which ignores the resume watermark. 2,460,619 rows recovered. |

Full detail, including the limitations that remain, is in
**[DATA_QUALITY.md](DATA_QUALITY.md)**.

---

## Design notes

**One wide table.** Everything lands in a single `candles` table keyed by
`(underlying, exchange_segment, instrument_type, timeframe, expiry_flag,
strike_offset, option_type, timestamp)`. Options, equities and indices differ
only in which key columns are populated, so one schema and one upsert path
serve all of them, and a join across instrument types is a plain `WHERE`.

**Idempotent by construction.** Every write is an upsert on that key. Re-running
any download is free, which is what makes the whole pipeline safely resumable —
a crashed run is fixed by running it again.

**Resume by watermark, repair by override.** Normal downloads skip to
`MAX(timestamp)` per series. That is fast but structurally unable to see a hole
*behind* the watermark, so `backfill.py` exists as the deliberate override that
re-pulls a stated range regardless.

**Sharded parallelism.** `download_options.py --shards N --shard i` partitions
the watchlist so several processes can run concurrently. SQLite handles the
contention through WAL mode and a 60-second busy timeout.

**Failures name themselves.** When a request finally gives up, it prints the
exact series and date window it lost, so the gap can be refilled rather than
discovered months later.

## Repository map

**Ingestion**

| File | Role |
|---|---|
| `dhan_client.py` | API client — auth, pagination, 429 backoff, gap-naming on failure |
| `download_options.py` | Option chain downloader, shardable and resumable |
| `download_spot_futures.py` | Equity and index series |
| `scrip_master.py` | Symbol → `securityId` resolution, atomic cache swap |
| `backfill.py` | Watermark-ignoring repair tool |
| `backfill_deep_strikes.py` | Widens strike coverage on existing series |
| `fetch_bhavcopy.py` / `parse_bhavcopy.py` | NSE bhavcopy archive → Parquet |
| `build_lot_history.py` | Point-in-time contract sizes from bhavcopy |

**Transformation**

| File | Role |
|---|---|
| `db.py` | Connection setup, schema, WAL and busy-timeout policy |
| `option_chain.py` | Pivots the tape into fixed-strike panels, flags gaps |
| `expiry.py` | Expiry calendar derived from the index |
| `resample_timeframes.py` | Higher timeframes from stored bars |
| `load_chain_daily.py` | Daily option bars from the 15-minute tape |
| `rsi.py` | Wilder RSI |

**Data quality**

| File | Role |
|---|---|
| `audit_data.py` | Strike coverage, timeframes, spot integrity, density, nulls |
| `audit_gaps.py` | Mid-series holes against a derived market calendar |
| `verify_warehouse.py` | End-to-end consistency check |

---

## Setup

Requires Python 3.10+ and a DhanHQ API subscription.

```bash
git clone https://github.com/<your-username>/nse-derivatives-warehouse.git
cd nse-derivatives-warehouse
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Add your credential — it is read from the environment and is never committed:

```bash
cp .env.example .env
```

Then put your token in `.env` as `DHAN_ACCESS_TOKEN=...`. Dhan tokens expire in
roughly 24 hours, so regenerate before a long run.

Edit the watchlists in `config.py`, then:

```bash
python download_spot_futures.py
```

Options take considerably longer, so run them sharded:

```bash
python download_options.py --shards 4 --shard 0
```

Repeat for shards 1–3 in separate processes. On macOS, prefix long runs with
`caffeinate -i` so the machine does not sleep mid-download.

Full operational detail — resuming, repairing a gap, troubleshooting — is in
**[SETUP.md](SETUP.md)**.

## Auditing

```bash
python audit_data.py
python audit_gaps.py --min-gap 2
```

Both are read-only (`PRAGMA query_only`) and write their findings to `audit/`
as CSVs. Run them after any large ingestion — that is the point of them.

## Known limitations

The warehouse is not complete, and the gaps are documented rather than hidden.
The short version: strike coverage is ATM-relative rather than a full chain,
some series begin late because the vendor has no earlier history, thirteen
mid-series holes are absent at source, and futures are not yet ingested.

**[DATA_QUALITY.md](DATA_QUALITY.md)** states each one with the query that
demonstrates it. Read it before trusting a result computed on this data.

**[DATA_INTEGRITY_FINDINGS.md](DATA_INTEGRITY_FINDINGS.md)** covers an
independent re-audit run against the database rather than against the
documentation — including the case where the documentation was the thing that
turned out to be wrong.

## License

MIT — see [LICENSE](LICENSE).

### Core Implementation Code & Architecture
#### File: `rsi.py`
```python
"""
Wilder's RSI (the standard RSI everyone means when they say "RSI(14)") —
uses Wilder's smoothing (equivalent to an EMA with alpha=1/period), not
a simple moving average. This matches TradingView/broker RSI values.
"""

import pandas as pd


def wilder_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    rsi[avg_loss == 0] = 100
    rsi[(avg_gain == 0) & (avg_loss == 0)] = 50
    return rsi
```

#### File: `main.py`
```python
"""
Run this to update the entire local warehouse:
    python main.py

Safe to re-run daily/weekly — every downloader resumes from the last
stored timestamp per series instead of re-pulling everything.
"""

import config
import db
import download_spot_futures
import download_options


def print_summary():
    with db.get_conn(config.DB_PATH) as conn:
        rows = db.series_summary(conn)
        print("\n" + "=" * 90)
        print("WAREHOUSE SUMMARY")
        print("=" * 90)
        print(f"{'Underlying':<12}{'Type':<9}{'TF':<5}{'Expiry':<7}{'Strike':<8}{'Opt':<4}{'Rows':>9}   Range")
        for r in rows:
            underlying, seg, itype, tf, expf, off, opt, cnt, first, last = r
            print(f"{underlying:<12}{itype:<9}{tf:<5}{expf:<7}{off:<8}{opt:<4}{cnt:>9}   {first} -> {last}")
        print("=" * 90)


if __name__ == "__main__":
    print(">>> Updating spot / index / equity / futures data ...")
    download_spot_futures.main()

    print("\n>>> Updating options data ...")
    download_options.main()

    print_summary()
```

#### File: `backfill.py`
```python
"""
Force-refetches a symbol's option series over an explicit date range.

The normal download resumes from each series' latest stored bar, so a hole in
the middle is never revisited — the watermark already sits past it. This ignores
the watermark and re-pulls the range outright. Writes are upserts, so re-pulling
data that is already present is harmless.

    python backfill.py --symbol PATANJALI --from 2025-09-01 --to 2025-09-30
"""

import argparse
from datetime import datetime

import config
import db
from dhan_client import DhanClient, date_chunks, parse_rolling_option
from scrip_master import ensure_scrip_master, find_security_id


def strike_label(offset):
    return "ATM" if offset == 0 else f"ATM{'+' if offset > 0 else ''}{offset}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", required=True)
    ap.add_argument("--from", dest="start", required=True)
    ap.add_argument("--to", dest="end", required=True)
    ap.add_argument("--sleep", type=float, default=1.0)
    args = ap.parse_args()

    start = datetime.strptime(args.start, "%Y-%m-%d")
    end = datetime.strptime(args.end, "%Y-%m-%d")
    sym = args.symbol.upper()

    entry = next((w for w in config.OPTIONS_WATCHLIST if w[0].upper() == sym), None)
    if entry is None:
        raise SystemExit(f"{sym} is not in OPTIONS_WATCHLIST")
    _, seg, expiry_flags, offsets = entry

    itype = "OPTIDX" if sym in ("NIFTY", "BANKNIFTY") else "OPTSTK"
    lookup = "INDEX" if itype == "OPTIDX" else "EQUITY"

    master = ensure_scrip_master(config.SCRIP_MASTER_CACHE, config.SCRIP_MASTER_MAX_AGE_DAYS)
    sid = find_security_id(master, sym, seg, lookup)
    client = DhanClient(config.ACCESS_TOKEN, args.sleep)
    db.init_db(config.DB_PATH)

    print(f"backfilling {sym} (securityId={sid}) {start.date()} -> {end.date()}", flush=True)
    total = 0
    with db.get_conn(config.DB_PATH) as conn:
        for flag in expiry_flags:
            for off in offsets:
                label = strike_label(off)
                for opt in config.OPTIONS_TYPES:
                    suffix = "CE" if opt == "CALL" else "PE"
                    got = 0
                    for a, b in date_chunks(start, end, chunk_days=28):
                        resp = client.rolling_option(
                            sid, seg, flag, expiry_code=1, strike_label=label,
                            option_type=opt, from_date=a, to_date=b, instrument=itype)
                        rows = parse_rolling_option(resp, opt, {
                            "underlying": sym, "exchange_segment": seg,
                            "instrument_type": itype, "timeframe": "15",
                            "expiry_flag": flag, "strike_offset": label,
                            "option_type": suffix,
                        }, verbose_on_empty=False)
                        got += db.upsert_candles(conn, rows)
                    total += got
                    print(f"  {flag} {label} {suffix}: {got} rows", flush=True)
        print(f"\nbackfilled {total} rows for {sym}", flush=True)


if __name__ == "__main__":
    main()
```

#### File: `resample_timeframes.py`
```python
"""
Builds WEEK and MONTH candles from already-downloaded DAY data.

Dhan's API does not offer weekly/monthly candles directly (only
1/5/15/25/60-min intraday and daily). Run this AFTER main.py has
pulled daily data — it aggregates 5 daily bars into 1 weekly bar
(Mon-Fri), and all daily bars in a calendar month into 1 monthly bar,
then stores them back into the same `candles` table with
timeframe='WEEK' / 'MONTH' so they're queryable the same way as
everything else.

Safe to re-run — it recomputes and upserts, never duplicates.

USAGE:
    python resample_timeframes.py
"""

import pandas as pd
import config
import db


def fetch_daily(conn, underlying, exchange_segment, instrument_type):
    query = """
        SELECT timestamp, open, high, low, close, volume, oi
        FROM candles
        WHERE underlying=? AND exchange_segment=? AND instrument_type=? AND timeframe='DAY'
        ORDER BY timestamp
    """
    df = pd.read_sql(query, conn, params=(underlying, exchange_segment, instrument_type))
    if df.empty:
        return df
    df["dt"] = pd.to_datetime(df["timestamp"], unit="s")
    df.set_index("dt", inplace=True)
    return df


def resample(df, rule):
    agg = df.resample(rule).agg({
        "open": "first", "high": "max", "low": "min", "close": "last",
        "volume": "sum", "oi": "last",
    }).dropna(subset=["open"])
    # dtype-independent epoch-seconds conversion (pandas' datetime64 unit
    # varies by version/platform — us vs ns — so don't assume nanoseconds)
    agg["timestamp"] = (agg.index - pd.Timestamp("1970-01-01")) // pd.Timedelta("1s")
    return agg.reset_index(drop=True)


def build_rows(agg_df, underlying, exchange_segment, instrument_type, timeframe):
    rows = []
    for _, r in agg_df.iterrows():
        rows.append({
            "underlying": underlying, "exchange_segment": exchange_segment,
            "instrument_type": instrument_type, "timeframe": timeframe,
            "timestamp": int(r["timestamp"]),
            "open": r["open"], "high": r["high"], "low": r["low"], "close": r["close"],
            "volume": r["volume"], "oi": r["oi"],
        })
    return rows


def main():
    with db.get_conn(config.DB_PATH) as conn:
        series = conn.execute("""
            SELECT DISTINCT underlying, exchange_segment, instrument_type
            FROM candles WHERE timeframe='DAY'
        """).fetchall()

        for underlying, seg, itype in series:
            daily = fetch_daily(conn, underlying, seg, itype)
            if daily.empty:
                continue

            weekly = resample(daily, "W-FRI")   # Indian markets: Mon-Fri week, close Friday
            monthly = resample(daily, "ME")

            w_rows = build_rows(weekly, underlying, seg, itype, "WEEK")
            m_rows = build_rows(monthly, underlying, seg, itype, "MONTH")

            n = db.upsert_candles(conn, w_rows) + db.upsert_candles(conn, m_rows)
            print(f"{underlying:<12} {itype:<9}: {len(w_rows)} weekly + {len(m_rows)} monthly bars ({n} upserted)")

    print("\nDone. Query timeframe='WEEK' or timeframe='MONTH' just like any other series.")


if __name__ == "__main__":
    main()
```

#### File: `audit_data.py`
```python
"""Full data-quality audit of market_data.db."""
import sqlite3, pandas as pd
import config as cfgmod
conn=sqlite3.connect("market_data.db")
q=lambda s: pd.read_sql(s,conn)
print("="*84); print("1. STRIKE COVERAGE"); print("="*84)
d=q("""SELECT underlying, COUNT(DISTINCT strike_offset) offs FROM candles
       WHERE instrument_type='OPTSTK' GROUP BY 1""")
print(f"  stock symbols with 11 offsets (ATM+-5): {(d.offs==11).sum()}")
print(f"  stock symbols with  9 offsets (ATM+-4): {(d.offs==9).sum()}")
print(f"  stock symbols with  7 offsets (ATM+-3): {(d.offs==7).sum()}")
print(f"  other: {(~d.offs.isin([7,9,11])).sum()}")
i=q("""SELECT underlying, expiry_flag, COUNT(DISTINCT strike_offset) offs FROM candles
       WHERE instrument_type='OPTIDX' GROUP BY 1,2""")
print("  index:"); print(i.to_string(index=False))

print("\n"+"="*84); print("2. MISSING TIMEFRAMES"); print("="*84)
tf=q("""SELECT instrument_type, timeframe, COUNT(*) n FROM candles GROUP BY 1,2""")
have=set(zip(tf.instrument_type,tf.timeframe))
for it in ("OPTSTK","OPTIDX"):
    for t in ("1","5","15","25","60","DAY"):
        if (it,t) not in have: print(f"  MISSING: {it} timeframe={t}")
print("  -> options exist ONLY at 15-min. No daily/hourly option bars stored.")

print("\n"+"="*84); print("3. WATCHLIST vs DATABASE"); print("="*84)
wl=[w[0] for w in cfgmod.OPTIONS_WATCHLIST]
got=set(q("SELECT DISTINCT underlying FROM candles WHERE instrument_type IN ('OPTSTK','OPTIDX')").underlying)
missing=[s for s in wl if s not in got]
print(f"  watchlist: {len(wl)}   with option data: {len(got)}   MISSING: {len(missing)}")
if missing: print("  "+", ".join(missing))

print("\n"+"="*84); print("4. SPOT SERIES INTEGRITY (equity close vs option-tape spot)"); print("="*84)
qq="""SELECT underlying, AVG(spot) s FROM candles WHERE instrument_type='OPTSTK'
      AND strike_offset='ATM' AND spot IS NOT NULL
      AND timestamp>=strftime('%s','2025-01-01') AND timestamp<strftime('%s','2026-01-01')
      GROUP BY 1"""
opt=q(qq).set_index("underlying").s
eq=q("""SELECT underlying, AVG(close) c FROM candles WHERE instrument_type='EQUITY'
        AND timeframe='DAY' AND timestamp>=strftime('%s','2025-01-01')
        AND timestamp<strftime('%s','2026-01-01') GROUP BY 1""").set_index("underlying").c
j=pd.concat([opt,eq],axis=1).dropna(); j["ratio"]=j.c/j.s
bad=j[(j.ratio<0.97)|(j.ratio>1.03)].sort_values("ratio")
print(f"  compared {len(j)} symbols | MISMATCHED: {len(bad)}")
for s,r in bad.iterrows():
    print(f"    {s:14s} option-spot {r.s:>9,.1f}   equity-close {r.c:>9,.1f}   ratio {r.ratio:.3f}")

print("\n"+"="*84); print("5. DATA DENSITY — thinnest stock option tapes"); print("="*84)
den=q("""SELECT underlying, COUNT(DISTINCT date(timestamp,'unixepoch')) days,
         COUNT(*) rows FROM candles WHERE instrument_type='OPTSTK' AND strike_offset='ATM'
         GROUP BY 1 ORDER BY days ASC LIMIT 15""")
print(den.to_string(index=False))
med=q("""SELECT COUNT(DISTINCT date(timestamp,'unixepoch')) d FROM candles
         WHERE instrument_type='OPTSTK' AND strike_offset='ATM' GROUP BY underlying""")
print(f"  median trading days per symbol: {med.d.median():.0f}   max: {med.d.max()}")

print("\n"+"="*84); print("6. ROW INTEGRITY"); print("="*84)
for label,cond in [("close IS NULL","close IS NULL"),("close<=0","close<=0"),
                   ("strike IS NULL","strike IS NULL"),("spot IS NULL","spot IS NULL"),
                   ("oi IS NULL","oi IS NULL"),("iv IS NULL","iv IS NULL")]:
    n=q(f"SELECT COUNT(*) n FROM candles WHERE instrument_type='OPTSTK' AND {cond}").n[0]
    print(f"  OPTSTK {label:18s} {n:>12,}")
conn.close()
```

#### File: `option_chain.py`
```python
"""
Fixed-strike option series reconstruction from the ATM-relative warehouse.

WHY THIS EXISTS
---------------
Dhan's rolling-option endpoint stores series by ATM-relative offset
("ATM", "ATM+3", ...), and the strike behind each offset CHANGES every bar as
spot moves. So `strike_offset='ATM'` is NOT a tradeable instrument — it is a
synthetic series that re-anchors continuously. Measured on 2025 NIFTY 15-min
data, its returns correlate +0.04 with spot; a real ATM call correlates ~+0.89.

However, every row also stores its ACTUAL `strike`. So a genuine fixed-strike
series can be reconstructed by pivoting on `strike` and slicing one column —
that is what a trader actually holds after picking a strike at entry.

LIMITATION: the warehouse only stores ATM-10..ATM+10. If spot travels more than
10 strikes away from the chosen strike, that strike falls out of the stored
window and its series ends (or gaps). Callers see this via `gap_before` and
should close the trade rather than silently stepping across the discontinuity.
"""

import pandas as pd


class OptionChain:
    """Pivoted option chain for one (symbol, expiry_flag, option_type)."""

    def __init__(self, conn, symbol, option_type, expiry_flag="WEEK", instrument_type="OPTIDX"):
        q = """
            SELECT timestamp, strike, open, high, low, close, volume, strike_offset
            FROM candles
            WHERE underlying=? AND instrument_type=? AND timeframe='15'
              AND expiry_flag=? AND option_type=? AND strike IS NOT NULL
            ORDER BY timestamp
        """
        df = pd.read_sql(q, conn, params=(symbol, instrument_type, expiry_flag, option_type))
        self.empty = df.empty
        if self.empty:
            return

        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        self.symbol = symbol
        self.option_type = option_type
        self.expiry_flag = expiry_flag

        # timestamp -> the strike that was ATM at that bar
        atm = df[df["strike_offset"] == "ATM"][["timestamp", "strike"]]
        self.atm_by_ts = atm.drop_duplicates("timestamp").set_index("timestamp")["strike"]

        # strike x timestamp panels
        self._panels = {
            f: df.pivot_table(index="timestamp", columns="strike", values=f)
            for f in ("open", "high", "low", "close", "volume")
        }
        self.index = self._panels["close"].index          # master bar clock
        self._pos = {ts: i for i, ts in enumerate(self.index)}

    def atm_strike_at(self, ts):
        """The strike that was ATM at (or just before) ts. None if unavailable."""
        s = self.atm_by_ts[self.atm_by_ts.index <= ts]
        return float(s.iloc[-1]) if len(s) else None

    def series(self, strike):
        """Full OHLCV history for one fixed strike.

        Rows where this strike had no data (outside the stored ATM+-10 window)
        are dropped, and `gap_before` marks each row whose immediately preceding
        master bar was missing — i.e. the series is discontinuous there.
        """
        close_panel = self._panels["close"]
        if strike not in close_panel.columns:
            return pd.DataFrame()

        out = pd.DataFrame({
            "timestamp": self.index,
            **{f: self._panels[f][strike].values for f in ("open", "high", "low", "close", "volume")},
        })
        out["_pos"] = range(len(out))
        out = out.dropna(subset=["close"]).reset_index(drop=True)
        if out.empty:
            return out

        # gap_before: previous surviving row was not the previous master bar
        out["gap_before"] = out["_pos"].diff() != 1
        out.loc[0, "gap_before"] = False
        return out.drop(columns="_pos")
```


==================================================


## [3/3] Repository: nselib (`WHEEL_nselib`)
- **Full Name**: `nselib`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
  <h1 align="center">nselib</h1>
  <p align="center">
    A Python library to fetch publicly available data from <a href="https://www.nseindia.com">NSE India</a>.
  </p>
</p>

<p align="center">
  <a href="https://pypi.org/project/nselib/"><img src="https://img.shields.io/pypi/v/nselib?color=blue" alt="PyPI Version"></a>
  <a href="https://pypi.org/project/nselib/"><img src="https://img.shields.io/pypi/pyversions/nselib" alt="Python Versions"></a>
  <a href="https://github.com/RuchiTanmay/nselib/blob/main/LICENSE"><img src="https://img.shields.io/github/license/RuchiTanmay/nselib" alt="License"></a>
  <a href="https://pypi.org/project/nselib/"><img src="https://img.shields.io/pypi/dm/nselib?color=green" alt="Downloads"></a>
</p>

---

## ✨ Features

- **Capital Market** — Price volume data, deliverable positions, bhav copies, bulk/block deals, short selling, VaR margins, PE ratios, 52-week highs/lows, and more
- **Cash Market** — NSDL FPI investment and derivative activity plus AMFI monthly archive reports
- **Derivatives** — Futures & options price volume data, bhav copies, participant-wise OI & volume, live option chains, FII statistics, ban period securities
- **Indices** — Index constituent lists, live index performances across Broad Market, Sectoral, Thematic, and Strategy categories
- **Debt** — Securities available for trading
- **Corporate Filings** — Financial results, corporate actions, event calendars
- **Market Activity** — Top gainers/losers, most active equities, total traded stocks, FII/DII activity
- **Utilities** — Trading holiday calendar, India VIX historical data

## 📦 Installation

**Fresh install:**

```bash
pip install nselib
```

**Upgrade to latest:**

```bash
pip install nselib --upgrade
```

> **Note:** Compatible and tested with Python 3.8 and above.

## 🚀 Quick Start

```python
from nselib import capital_market

# Get price volume data for a stock (last 1 month)
df = capital_market.price_volume_data(symbol='SBIN', period='1M')
print(df.head())

# Or specify a custom date range
df = capital_market.price_volume_and_deliverable_position_data(
    symbol='SBIN',
    from_date='01-01-2024',
    to_date='31-01-2024'
)
print(df)
```

## 📖 API Reference

### Date Parameters

Most functions accept dates in two ways:

| Parameter | Format | Example |
|---|---|---|
| `from_date` / `to_date` | `dd-mm-YYYY` | `'01-06-2024'` |
| `period` | Shorthand code | `'1D'`, `'1W'`, `'1M'`, `'6M'`, `'1Y'` |

> You must provide **either** `from_date` + `to_date` **or** `period`, not both.

---

### Capital Market

```python
from nselib import capital_market
```

| Function | Description | Key Parameters                                            |
|---|---|-----------------------------------------------------------|
| `price_volume_and_deliverable_position_data()` | OHLCV + delivery data | `symbol`, `from_date`/`to_date` or `period`               |
| `price_volume_data()` | OHLCV price volume data | `symbol`, `from_date`/`to_date` or `period`               |
| `deliverable_position_data()` | Delivery position data | `symbol`, `from_date`/`to_date` or `period`               |
| `bulk_deal_data()` | Bulk deal transactions | `from_date`/`to_date` or `period`                         |
| `block_deals_data()` | Block deal transactions | `from_date`/`to_date` or `period`                         |
| `short_selling_data()` | Short selling reports | `from_date`/`to_date` or `period`                         |
| `bhav_copy_with_delivery()` | Daily bhav copy with delivery | `trade_date`                                              |
| `bhav_copy_equities()` | CM-UDiFF bhav copy | `trade_date`                                              |
| `bhav_copy_sme()` | SME bhav copy | `trade_date`                                              |
| `equity_list()` | All listed equities | —                                                         |
| `fno_equity_list()` | F&O equity list with lot sizes | —                                                         |
| `fno_index_list()` | F&O index list with lot sizes | —                                                         |
| `nifty50_equity_list()` | Nifty 50 constituents | —                                                         |
| `niftynext50_equity_list()` | Nifty Next 50 constituents | —                                                         |
| `niftymidcap150_equity_list()` | Nifty Midcap 150 constituents | —                                                         |
| `niftysmallcap250_equity_list()` | Nifty Smallcap 250 constituents | —                                                         |
| `india_vix_data()` | India VIX historical data | `from_date`/`to_date` or `period`                         |
| `index_data()` | Historical index OHLC data | `index`, `from_date`/`to_date` or `period`                |
| `market_watch_all_indices()` | Live snapshot of all indices | —                                                         |
| `daily_volatility()` | CM daily volatility report | `trade_date`                                              |
| `fii_dii_trading_activity()` | FII/DII buy-sell activity | —                                                         |
| `var_begin_day()` | VaR — begin of day | `trade_date`                                              |
| `var_1st_intra_day()` | VaR — 1st intraday | `trade_date`                                              |
| `var_2nd_intra_day()` | VaR — 2nd intraday | `trade_date`                                              |
| `var_3rd_intra_day()` | VaR — 3rd intraday | `trade_date`                                              |
| `var_4th_intra_day()` | VaR — 4th intraday | `trade_date`                                              |
| `var_end_of_day()` | VaR — end of day | `trade_date`                                              |
| `sme_bhav_copy()` | SME bhav copy | `trade_date`                                              |
| `sme_band_complete()` | SME band complete data | `trade_date`                                              |
| `week_52_high_low_report()` | 52-week high/low report | `trade_date`                                              |
| `financial_results_for_equity()` | Quarterly/annual financials | `from_date`/`to_date` or `period`, `fin_period`, `fo_sec` |
| `corporate_bond_trade_report()` | Corporate bond trades | `trade_date`                                              |
| `pe_ratio()` | PE ratio for all equities | `trade_date`                                              |
| `corporate_actions_for_equity()` | Corporate actions | `from_date`/`to_date` or `period`, `fno_only`             |
| `event_calendar_for_equity()` | Event calendar | `from_date`/`to_date` or `period`, `fno_only`             |
| `top_gainers_or_losers()` | Top gainers or losers | `to_get` (`'gainers'` / `'loosers'`)                      |
| `most_active_equities()` | Most active by value/volume | `fetch_by` (`'value'` / `'volume'`)                       |
| `total_traded_stocks()` | All traded stocks summary | —                                                         |
| `category_turnover_cash()` | category-wise turnover data | `trade_date`                                              |
| `business_growth_cm_segment()` | business growth data for the NSE capital market | `data_type`, `from_year` , `to_year` |


**Examples:**

```python
# Bhav copy for a specific date
df = capital_market.bhav_copy_with_delivery(trade_date='20-06-2024')

# India VIX for last 1 week
df = capital_market.india_vix_data(period='1W')

# CM daily volatility report
df = capital_market.daily_volatility(trade_date='17-04-2026')

# Historical index data
df = capital_market.index_data(index='NIFTY 50', from_date='01-01-2024', to_date='31-03-2024')

# Financial results (quarterly, F&O securities only)
df = capital_market.financial_results_for_equity(period='6M', fo_sec=True, fin_period='Quarterly')

# Top gainers in live market
df = capital_market.top_gainers_or_losers('gainers')
```

---

### Derivatives

```python
from nselib import derivatives
```

| Function                            | Description | Key Parameters |
|-------------------------------------|---|---|
| `future_price_volume_data()`        | Futures price & volume | `symbol`, `instrument` (`FUTIDX`/`FUTSTK`), dates |
| `option_price_volume_data()`        | Options price & volume | `symbol`, `instrument` (`OPTIDX`/`OPTSTK`), `option_type` (`PE`/`CE`), dates |
| `fno_bhav_copy()`                   | F&O daily bhav copy | `trade_date` |
| `participant_wise_open_interest()`  | OI by participant category | `trade_date` |
| `participant_wise_trading_volume()` | Volume by participant category | `trade_date` |
| `daily_volatility()`                | F&O daily volatility report | `trade_date` |
| `expiry_dates_future()`             | Upcoming futures expiry dates | — |
| `expiry_dates_option_index()`       | Upcoming options expiry dates | — |
| `nse_live_option_chain()`           | Live option chain | `symbol`, `expiry_date` (optional), `oi_mode` |
| `fii_derivatives_statistics()`      | FII derivatives stats | `trade_date` |
| `fno_security_in_ban_period()`      | Securities in F&O ban | `trade_date` |
| `live_most_active_underlying()`     | Most active underlyings | — |
| `category_turnover_fo()`            | derivatives category-wise turnover data | `trade_date` |
| `business_growth_fo_segment()`      | business growth data for the NSE F&O segment | `data_type`, `from_year` , `to_year` |

**Instrument Types:**

| Code | Description |
|---|---|
| `FUTIDX` | Future Index |
| `FUTSTK` | Future Stock |
| `OPTIDX` | Option Index |
| `OPTSTK` | Option Stock |

**Examples:**

```python
# Futures price data
df = derivatives.future_price_volume_data(
    symbol='SBIN', instrument='FUTSTK', period='1M'
)

# Live option chain
df = derivatives.nse_live_option_chain(symbol='BANKNIFTY', expiry_date='27-03-2025')

# Compact option chain (fewer columns)
df = derivatives.nse_live_option_chain(symbol='NIFTY', oi_mode='compact')

# FII derivatives statistics
df = derivatives.fii_derivatives_statistics(trade_date='20-12-2025')

# F&O daily volatility report
df = derivatives.daily_volatility(trade_date='17-04-2026')
```

---

### Cash Market

```python
from nselib import cash_market
```

| Function | Description | Key Parameters |
|---|---|---|
| `nsdl_fpi_investment_activity()` | NSDL FPI investment activity for a reporting date | `trade_date` |
| `nsdl_fpi_latest_investment_activity()` | Latest NSDL FPI investment activity | — |
| `nsdl_fpi_derivative_activity()` | NSDL FPI derivative activity for a reporting date | `trade_date` |
| `nsdl_fpi_latest_derivative_activity()` | Latest NSDL FPI derivative activity | — |
| `amfi_monthly_report_links()` | List AMFI monthly archive links | — |
| `amfi_monthly_data()` | Parse one AMFI monthly report | `report_month`, `file_type_priority` |
| `amfi_monthly_historical_data()` | Parse AMFI monthly reports across a range | `from_month`, `to_month`, `file_type_priority` |

**Examples:**

```python
# NSDL FPI investment activity for a specific reporting date
df = cash_market.nsdl_fpi_investment_activity(trade_date='30-10-2025')

# Latest NSDL FPI derivative activity
df = cash_market.nsdl_fpi_latest_derivative_activity()

# List available AMFI archive reports
links = cash_market.amfi_monthly_report_links()

# Parse a single AMFI monthly report
df = cash_market.amfi_monthly_data(report_month='01-03-2026')

# Parse AMFI history for a month range
history = cash_market.amfi_monthly_historical_data(from_month='01-01-2024', to_month='01-03-2026')
```

---

### Indices

```python
from nselib import indices
```

| Function | Description | Key Parameters |
|---|---|---|
| `index_list()` | Available indices by category | `index_category` |
| `constituent_stock_list()` | Stocks in a given index | `index_category`, `index_name` |
| `live_index_performances()` | Live performance of all indices | — |

**Index Categories:** `BroadMarketIndices`, `SectoralIndices`, `ThematicIndices`, `StrategyIndices`

**Examples:**

```python
# List all broad market indices
index_names = indices.index_list(index_category='BroadMarketIndices')

# Get Nifty 50 constituents
df = indices.constituent_stock_list(index_category='BroadMarketIndices', index_name='Nifty 50')

# Live index performances
df = indices.live_index_performances()
```

---

### Debt

```python
from nselib import debt
```

| Function | Description | Key Parameters |
|---|---|---|
| `securities_available_for_trading()` | Debt securities available | `trade_date` |

**Example:**

```python
df = debt.securities_available_for_trading(trade_date='20-12-2025')
```

---

### Utilities

```python
import nselib
```

| Function | Description |
|---|---|
| `trading_holiday_calendar()` | NSE trading holidays for all segments |

**Example:**

```python
df = nselib.trading_holiday_calendar()
```

---

## 🐞 Logging & Debugging

`nselib` comes with a built-in logger that is silent by default so it doesn't pollute your application's logs. If you want to see detailed network requests, API responses, or debug errors while working with the library, you can easily enable it.

```python
import nselib
import logging

# Enable the logger to output to the console
nselib.enable_logging(level=logging.DEBUG)

# Now, function calls will emit helpful trace logs
df = nselib.capital_market.price_volume_data('SBIN', period='1W')
```

---

## 🤝 How to Contribute

There are multiple ways to contribute to nselib:

### Report Issues & Suggest Features

Found a bug or have a feature request? Please open an issue on the [GitHub Issues page](https://github.com/RuchiTanmay/nselib/issues).

### Submit Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Write About nselib

Help the community by writing tutorials, blog posts, or example projects using nselib.

### Contact

- **Original Author:** [Ruchi Tanmay](https://www.linkedin.com/in/ruchi-tanmay-61848219)
- **GitHub:** [RuchiTanmay/nselib](https://github.com/RuchiTanmay/nselib)

## 📄 License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `nselib/debt/__init__.py`
```python
from .debt_data import securities_available_for_trading
```

#### File: `nselib/indices/__init__.py`
```python
from .index_data import index_list, constituent_stock_list, live_index_performances
```

#### File: `nselib/mutual_funds/__init__.py`
```python
from .mutual_fund_data import amfi_monthly_data, amfi_monthly_historical_data, amfi_monthly_report_links
```

#### File: `nselib/__init__.py`
```python
import logging

from .libutil import trading_holiday_calendar
from .logger import enable_logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = "2.5.1"
__all__ = ["trading_holiday_calendar", "enable_logging"]
```

#### File: `nselib/cash_market/__init__.py`
```python
from .cash_market_data import (
    amfi_monthly_data,
    amfi_monthly_historical_data,
    amfi_monthly_report_links,
    nsdl_fpi_derivative_activity,
    nsdl_fpi_investment_activity,
    nsdl_fpi_latest_derivative_activity,
    nsdl_fpi_latest_investment_activity,
)
```


==================================================
