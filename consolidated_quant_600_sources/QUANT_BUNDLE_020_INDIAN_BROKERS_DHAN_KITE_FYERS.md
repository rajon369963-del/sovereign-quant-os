# ⚡ [QUANT-SOURCE-020] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_020_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Streamlit-Scanner-App (`WHEEL_Streamlit-Scanner-App`)
- **Full Name**: `Streamlit-Scanner-App`
- **Description**: Pluggable daily-candle stock screener for Indian (NSE) equities, with DhanHQ data and interactive TradingView-style charts. Also contains Claude-based AI agents for fundamental and technical analysis
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Streamlit Scanner App

A pluggable **daily-candle stock scanner** for Indian equities. It downloads
historical price data from [DhanHQ](https://dhanhq.co/), runs technical-analysis
**screeners** over a universe of stocks, and shows the shortlisted symbols in a
[Streamlit](https://streamlit.io/) web app with interactive charts.

It is designed to be easy to extend: a "screener" is just a small Python file
dropped into the `screeners/` folder.

Shortlisted stocks can also be sent to a built-in **"Check Fundamentals"
agent** (powered by the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview)
running on your Claude subscription). The agent scrapes [screener.in](https://www.screener.in/) for the
selected stock and returns a structured fundamental analysis — pass/fail on
user-defined criteria (nine for the Hemant Super 45 / Nifty 100 universe, seven
for every other stock), a 0–10 holistic rating, peer / margin / governance
observations, and a three-part forward outlook (announcements signal + concall
transcript signal + integrated view).

Access is gated behind **Google sign-in with an email allowlist**, and the app
ships with a **scan-history persistence foundation** (SQLAlchemy + Alembic; SQLite
by default or Postgres) that is ready to record every run for later replay and audit.

> **Disclaimer:** This is an educational / personal research tool. Nothing here
> is financial advice. Always do your own research before trading.

---

## Features

- **Ten built-in screeners**, all built on a common `BaseScanner` abstract
  base class so adding new ones is a single-file change.
  - **Heikin Ashi SuperTrend** — F&O stocks where the daily Heikin Ashi close
    crosses the SuperTrend line.
  - **Bollinger Band Reversal** — F&O stocks printing a daily Bollinger Band
    rejection candle.
  - **Bollinger Lower Band** — Hemant Super 45 stocks whose latest close is at,
    below, or within a small buffer of the lower Bollinger Band(200, 2.5).
    (Distinct from *Bollinger Band Reversal* above, which scans F&O stocks for
    outer-band rejection candles.)
  - **Envelope** — Hemant Super 45 stocks whose latest close is at or below the
    lower Envelope band (200-EMA basis, 14% bands) — i.e. ≥14% below the 200 EMA.
  - **Envelope + Knoxville** — Hemant Super 45 stocks near the lower Envelope
    band (200-EMA basis, 14% bands) with a recent bullish Knoxville Divergence
    (Bars Back 20, RSI 14).
  - **Stochastic Swing** — NIFTY 500 stocks with a fresh Stochastic swing entry
    (a `%K`/`%D` cross out of the oversold/overbought zone, confirmed by the
    200 SMA trend and a recent 5 EMA / 200 SMA crossover).
  - **52 Week High/Low (Ceyhun)** — Hemant Super 45 stocks whose close came
    within a tolerance (default 2%) of the trailing 252-day low on any of the
    last 10 trading days.
  - **20% Up Green Candles (Lovevanshi)** — Hemant Super 45 ∪ Good 45 stocks
    whose latest candle caps a run of consecutive green candles (up to 20) that
    moved more than 20% from the run's lowest low to its highest high.
  - **67 Ka Funda (AI)** — Hemant Super 45 + Good 45 + Good 200 stocks that have
    fallen at least 67% from their available-history all-time high (with ≥100%
    upside back to it). A cheap deterministic drawdown gate shortlists candidates,
    then a **Claude Agent SDK** verifier researches each survivor (Screener.in data
    + SerpAPI Google snippets, all treated as untrusted evidence) and approves a
    BUY only when the fall is explained, appears resolved, and the profit / growth
    / quarterly-improvement checks pass. Needs a `SERPAPI_API_KEY`; degrades
    gracefully (skips the AI step) when the SDK or SerpAPI is unavailable.
  - **Technical Analysis (AI)** — Hemant Super 45 ∪ Good 45 stocks with an
    AI-confirmed bullish setup: major support, breakout-confirmed classical
    pattern, confirmed double bottom, bullish Fair Value Gap retest, or bullish
    order-block tap. A cheap deterministic gate prefilters candidates, then a
    **Claude Agent SDK** agent confirms with level, pattern, and structure tools.
- **Per-stock Check Fundamentals AI agent** — see the
  [dedicated section below](#check-fundamentals-agent). One click on a
  shortlisted row runs a Claude Agent SDK agent that scrapes screener.in (peer
  table via HTMX, recent announcements, the latest concall transcript via
  `pdfplumber`) and returns a structured verdict with a 0–10 rating, a
  Valuation observation comparing current vs median P/E, and a three-part
  forward outlook.
- **Hardened AI screeners** — all three Claude agents (Check Fundamentals,
  Technical Analysis, 67 Ka Funda) treat scraped/search text as untrusted. A
  shared quarantine (**TEST-003**, `backend/security/prompt_injection.py`) scans
  external evidence (Screener.in scrapes, SerpAPI snippets, concall transcripts)
  for model-directed instructions and **fails closed before the model sees it**,
  and every AI verdict is parsed against a strict Pydantic schema with a bounded
  retry budget — malformed output is rejected, never persisted (**AI-004**,
  `SCANNER_AI_MAX_ATTEMPTS`).
- **Candle data-quality checks (DATA-001)** — every OHLCV frame is validated at
  the loader boundary before any screener runs. Structurally impossible candles
  (high < low, NaN/inf, duplicate dates, negative volume) are **quarantined** and
  downgrade the run to `PARTIAL`/`FAILED`, while stale or gappy data is recorded
  as a warning. Findings persist in a per-run `data_quality_json` receipt and are
  summarized on the Admin health page.
- **Automatic data prefetch** — running `python app.py` first downloads the
  stock universes and ~10 years of daily candles, *then* opens the UI, so the
  app never blocks on downloads. Each successful prefetch keeps only the latest
  Dhan instrument-master snapshot in `Dependencies/`.
- **Reusable scanner universes** — built-in universe keys include `nifty_100`,
  `nifty_500`, `fno`, `hemant_super_45`, `hemant_good_45`,
  `hemant_good_200`, and the composites `hemant_super_good_union`
  (Hemant Super 45 ∪ Good 45) and `hemant_super_good_200_union`
  (Hemant Super 45 ∪ Good 45 ∪ Good 200), both deduped.
- **Interactive TradingView Lightweight Charts** — click any shortlisted stock
  to see a candlestick chart (with a drag-to-scale price axis) showing the
  screener's own indicator overlaid (Heikin Ashi candles for HA-based screeners;
  a dedicated oscillator panel for Stochastic).
- **Library-backed indicators** — indicators run through `TA-Lib` / `pandas_ta`
  when installed, and fall back to pure-pandas implementations otherwise.
- **Local Parquet cache** — candles are cached on disk; subsequent runs only
  fetch the days that are missing.
- **Authentication & access control** — every page sits behind a Google SSO
  (OIDC) sign-in gate (`backend/auth/`). An **email allowlist** (`ALLOWED_EMAILS`)
  restricts who may use the app, and a database-driven **role model**
  (viewer / analyst / admin) gates features by capability, assignable at runtime
  from the admin **Roles** page (`ADMIN_EMAILS` is the bootstrap admin). In
  production the gate fails closed when SSO config or the allowlist is missing.
- **Scan-run persistence + history page** — every scan (from the UI or the
  headless daily job) is recorded into a SQLAlchemy `scan_runs` / `scan_results`
  schema (`backend/storage/`) with a local SQLite default (`data/scanner.db`) or
  Postgres via `DATABASE_URL`, managed by **Alembic** migrations and a small
  repository API. A built-in **Scan history** view lists recent runs (status,
  started/finished timestamps, symbols scanned, shortlisted count, who triggered
  it, error state) with screener/universe/status/date/trigger/symbol filters and
  click-through to each run's persisted results. A read-only **Scan comparison**
  view compares the latest finalized shortlist against the immediately previous
  finalized shortlist for each screener/universe pair, with new, repeated,
  dropped, improved-score, degraded-score, and CSV export sections. Historical
  validation stores
  per-signal forward returns and exposes backend aggregate metrics by screener,
  universe, and horizon, surfaced in a read-only **Validation / Signal
  Performance** dashboard (filters, summary table, return distribution, win
  rate by horizon, benchmark-relative rows, monthly signal counts, sector
  concentration with an `Unknown` fallback, best/worst signals, and CSV export).
  Benchmark-relative (excess) returns compare each signal against its universe's
  index (NIFTY 50 / 100 / 500) using verified Dhan `IDX_I` instrument IDs
  configured in `config/benchmarks.yaml` (VALID-002B); an unconfigured benchmark
  stays null rather than guessing. Operators can fill pending rows with
  `python -m backend.jobs.compute_forward_returns --limit 500`.
- **Tested** — a `pytest` suite covers the indicators, data loader, universe
  builder, screener registry, the screeners themselves, the auth gate, the
  persistence layer, forward-return validation metrics, benchmark-index
  resolution, candle data-quality validation, the AI prompt-injection quarantine
  corpus, structured AI-output validation, and the Docker artifacts —
  plus **golden-snapshot** tests that catch screener output drift and an Alembic
  migration drift-guard.

---

## How it works

```
python app.py
   │
   ├─ 1. Prefetch (plain Python, before the UI)
   │     • refresh the universe CSVs (NIFTY 100 / 500 / F&O / Hemant lists)
   │     • download ~10 years of daily candles for every mapped stock
   │
   └─ 2. Launch the Streamlit UI
         • pick a screener, press "Run screener"
         • browse the shortlist, click a row to open its chart
```

The prefetch is what makes the app feel instant once it opens — all the slow
network work happens up front in the terminal.

---

## Requirements

- **Python 3.11+**
- The core packages in [`requirements.txt`](requirements.txt), installed with
  the verified direct pins in [`constraints.txt`](constraints.txt):
  `pip install -r requirements.txt -c constraints.txt`
- A **DhanHQ account** with API access — needed to download candle data.
- Optional indicator accelerators in
  [`requirements-optional.txt`](requirements-optional.txt). `TA-Lib` needs its
  native C library installed first (see [ta-lib.org](https://ta-lib.org/)).
  If `TA-Lib` or `pandas_ta` is missing, the app automatically falls back to
  pure-pandas indicator maths; it just runs a little slower.

---

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/DoRmAmMu1997/Streamlit-Scanner-App.git
   cd Streamlit-Scanner-App
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt -c constraints.txt
   ```

   Optional, only after installing any native prerequisites you need:

   ```bash
   pip install -r requirements-optional.txt
   ```

3. **Create the local scan-history database** (optional)

   By default, persisted scan runs live in `data/scanner.db`, which is
   generated locally and git-ignored. `DATA_DIR` can point the whole runtime
   data folder somewhere else, and `DATABASE_URL` can point the app at Postgres
   or another SQLAlchemy-supported database in deployed environments.

   The app and the daily scan command apply migrations automatically on
   startup, so a fresh checkout needs no manual step. Running the upgrade
   yourself is still useful to pre-provision a database or debug migrations:

   ```bash
   python -m alembic upgrade head
   ```

4. **Review runtime settings**

   The app reads runtime config through `backend.config.settings`. Local
   development has safe defaults:

   ```env
   APP_ENV=development
   LOG_LEVEL=WARNING
   AUTH_REQUIRED=false
   # DATA_DIR defaults to ./data
   # DATABASE_URL defaults to sqlite:///data/scanner.db
   ```

   Production should set these in the hosting environment, not in committed
   files:

   ```env
   APP_ENV=production
   DATA_DIR=/persistent/data
   DATABASE_URL=postgresql+psycopg://scanner:password@host:5432/scanner
   AUTH_REQUIRED=true
   ALLOWED_EMAILS=you@gmail.com
   ADMIN_EMAILS=you@gmail.com
   ```

   Production fails clearly if `DATABASE_URL`, `DATA_DIR`, Dhan credentials, or
   an authorized/admin email is missing. It also rejects
   `AUTH_REQUIRED=false`. `backend.security.redaction` masks configured
   secret-like values plus common token/API-key/password formats before text
   reaches UI errors, scan failure details, or configured logs. Redaction is a
   safety net only; do not paste real secrets into issues, screenshots, or PRs.

5. **Add your DhanHQ credentials**

   Copy the template and fill in your details:

   ```bash
   cp Dependencies/.env.example Dependencies/.env          # macOS/Linux/Git Bash
   ```

   ```powershell
   Copy-Item Dependencies\.env.example Dependencies\.env   # Windows PowerShell
   ```

   > Why is this folder called `Dependencies/`? Historical accident — it holds
   > credentials and setup helpers, not Python packages (those live in
   > `requirements*.txt`). It keeps the name because renaming would break
   > every existing local `.env` setup for zero functional gain.

   Open `Dependencies/.env` and set `DHAN_CLIENT_ID`, `DHAN_API_KEY`, and
   `DHAN_API_SECRET` (from web.dhan.co → My Profile → DhanHQ Trading APIs).
   Leave `DHAN_ACCESS_TOKEN` blank for now. Existing `.env` files that still
   use the legacy `DHAN_CLIENT_CODE` name continue to work.

6. **Generate the access token** (one-time, valid 12 months)

   ```bash
   python Dependencies/dhan_token_setup.py
   ```

   This walks you through the DhanHQ OAuth login and writes
   `DHAN_ACCESS_TOKEN` back into `Dependencies/.env` for you.

7. **Configure Google SSO for the Streamlit app**

   Create a Google OAuth/OIDC client with this local redirect URI:

   ```text
   http://localhost:8501/oauth2callback
   ```

   For a deployed app, add the same callback path on the deployed base URL:

   ```text
   https://your-app.example.com/oauth2callback
   ```

   Then copy the Streamlit secrets template and fill in the Google client
   values:

   ```bash
   cp .streamlit/secrets.example.toml .streamlit/secrets.toml
   ```

   Required keys:

   ```toml
   [auth]
   redirect_uri = "http://localhost:8501/oauth2callback"
   cookie_secret = "a-long-random-secret"

   [auth.google]
   client_id = "your-google-oauth-client-id"
   client_secret = "your-google-oauth-client-secret"
   server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
   ```

   Set `APP_ENV=production` and `AUTH_REQUIRED=true` in the deployment
   environment for production. If SSO config is missing in production, the app
   fails closed before loading any scanner controls. `SCANNER_ENV` is still
   accepted as a legacy alias for older local files.

   **Restrict who can use the app (email allowlist).** Once Google SSO works,
   limit access by email in `Dependencies/.env`:

   ```env
   # Comma-separated; case and surrounding spaces don't matter.
   ALLOWED_EMAILS=you@gmail.com, teammate@gmail.com
   ADMIN_EMAILS=you@gmail.com
   ```

   - `ADMIN_EMAILS` are always allowed and are admins — the bootstrap admins who
     can then assign viewer/analyst/admin roles to others from the in-app **Admin
     roles** page (AUTH-003). An authorized user with no assigned role defaults to
     **analyst** (can run scans and export); admins can add **viewer** (read-only)
     accounts there. Role assignments live in the `user_roles` table, so no
     redeploy is needed to change them.
   - If `ALLOWED_EMAILS` is **empty**, development permits any signed-in Google
     user when auth is enabled, but production (`APP_ENV=production`) requires
     either `ALLOWED_EMAILS` or `ADMIN_EMAILS`. A signed-in user who is not
     allowed sees an "unauthorized" message instead of the scanner.

8. **(Optional) Enable the Check Fundamentals agent** — it runs on the
   [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview) using
   your Claude subscription (Pro/Max), not an API key:

   ```bash
   pip install claude-agent-sdk        # already in requirements.txt
   ```

   Then sign in once with the bundled Claude CLI (uses your Claude plan), and
   make sure `ANTHROPIC_API_KEY` is **not** set in your environment — if it is,
   the SDK bills your API account instead of your plan's monthly Agent SDK
   credit. Optionally override the model in `Dependencies/.env`:

   ```env
   CLAUDE_AGENT_MODEL=claude-sonnet-4-6
   ```

   The **67 Ka Funda (AI)** screener additionally needs a
   [SerpAPI](https://serpapi.com/) key for its Google web research — add it to
   `Dependencies/.env`:

   ```env
   SERPAPI_API_KEY=your-serpapi-key
   ```

   Most screeners run fine without any of this; only the Check Fundamentals
   panel, the Technical Analysis (AI) confirmation step, and the 67 Ka Funda (AI)
   verifier need it.

> `Dependencies/.env` and `.streamlit/secrets.toml` are git-ignored — your
> credentials never leave your machine.

---

## Running the app

```bash
python app.py
```

This downloads the data first, then opens the Streamlit app in your browser.
Local development skips Google SSO unless `AUTH_REQUIRED=true` is set. When
auth is required, only allow-listed or admin emails (see step 7) may proceed
past sign-in before scanner controls, results, charts, or CSV downloads load.

> **First run is slow** — expect roughly 10–30 minutes depending on your
> connection: it backfills ~10 years of candles for ~500 stocks at a polite
> request pace. Setting `SCANNER_DHAN_FETCH_WORKERS=4` in `Dependencies/.env`
> overlaps download latency with disk writes **without** increasing the
> request rate Dhan sees (see [docs/operations.md](docs/operations.md)).
> Every later run only fetches the days added since you last ran it, so it is
> fast.

You can also start the UI directly with `streamlit run app.py` — but then it
uses whatever data is already cached locally (no prefetch).

---

## Running with Docker

The recommended local production-like path is Docker Compose: it starts the
Streamlit app plus a private Postgres database, uses named volumes for durable
runtime state, and keeps secrets outside the image.

```bash
cp .env.example .env
cp .streamlit/secrets.example.toml .streamlit/secrets.toml
# Edit .env and .streamlit/secrets.toml before running with real credentials.
docker compose up --build
```

Open <http://localhost:8501>. Compose publishes only the UI with
`-p 8501:8501` behavior via `SCANNER_UI_PORT=8501`; Postgres has no host port
and is reachable only inside the Compose network as `postgres:5432`.

Compose uses two named volumes:

- `scanner-data` mounted at `/data` for candles, caches, SQLite fallback files,
  and other app-generated state.
- `postgres-data` mounted at `/var/lib/postgresql/data` for the local Postgres
  cluster.

Stop the stack without deleting data:

```bash
docker compose down
```

Reset both named volumes when you deliberately want a clean local production
environment:

```bash
docker compose down --volumes
```

Run the daily scan job against the same Compose database and `/data` volume
without adding a long-lived scheduler service:

```bash
docker compose run --rm scanner-ui python -m backend.jobs.run_daily_scan --config config/daily_scans.yaml
```

To send ALERT-001 notifications from that Compose-run job, fill the optional
notification variables in the root `.env` before running it: `APP_URL`,
`TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`, and/or `SMTP_HOST`, `SMTP_USER`,
`SMTP_PASSWORD`, `ALERT_EMAIL_TO`. Leaving them blank keeps alerts disabled and
the scan still runs normally.

Use the single-container commands below when you only want to build or smoke-test
the image without starting Postgres.

Build the deployment image from the repository root:

```bash
docker build -t streamlit-scanner-app .
```

For a local container smoke test, keep auth disabled and persist generated data
in a named Docker volume:

```bash
docker run --rm \
  -p 8501:8501 \
  -e APP_ENV=development \
  -e AUTH_REQUIRED=false \
  -e DATA_DIR=/data \
  -v streamlit-scanner-data:/data \
  streamlit-scanner-app
```

Open <http://localhost:8501>. The image starts with `streamlit run app.py`
instead of `python app.py`, so it serves the UI directly and does not run the
local prefetch/relaunch wrapper at container boot.

Production containers default to fail-closed settings (`APP_ENV=production`,
`AUTH_REQUIRED=true`, `DATA_DIR=/data`). Supply the same runtime environment the
non-container app expects, mount a persistent `/data` volume, and provide
Streamlit's Google OIDC secrets file. Put `DATABASE_URL`, `DHAN_CLIENT_ID`, and
`DHAN_ACCESS_TOKEN` in the already-ignored `Dependencies/.env`, run
`chmod 600 Dependencies/.env`, and load it with `--env-file` so credentials do
not enter shell history or process arguments. Prefer your host's managed secret
injection for long-lived deployments:

```bash
docker run -d --name streamlit-scanner-app \
  -p 8501:8501 \
  --env-file Dependencies/.env \
  -e APP_ENV=production \
  -e AUTH_REQUIRED=true \
  -e DATA_DIR=/data \
  -e ALLOWED_EMAILS=you@gmail.com \
  -e ADMIN_EMAILS=you@gmail.com \
  -e LOG_FORMAT=json \
  -v streamlit-scanner-data:/data \
  -v /absolute/path/secrets.toml:/app/.streamlit/secrets.toml:ro \
  streamlit-scanner-app
```

`Dockerfile` exposes port `8501` and includes a health check against
`/_stcore/health`. `.dockerignore` keeps local secrets (`Dependencies/.env`,
`.streamlit/secrets.toml`) and generated cache/database files out of the build
context. See [docs/operations.md](docs/operations.md#docker--container-deployment)
for container runbook details and daily-job commands.

---

## Running the daily scan job

JOB-001 adds a headless command for schedulers, terminals, and hosting
platforms that need to run scans without opening Streamlit:

```bash
python -m backend.jobs.run_daily_scan
```

By default it runs the deterministic daily set:
`bollinger_band_reversal`, `heikin_ashi_supertrend`, and
`envelope_knoxville_buy`. Each screener uses the universe declared in its
registry metadata, so F&O screeners run on `fno` and the Envelope + Knoxville
screener runs on `hemant_super_45`.

The command expects the normal runtime setup to exist first: keep the
universe CSVs under `DATA_DIR/universes` and configure Dhan credentials so the
daily data loader can fetch/cache candles. Scan-history tables are created
automatically — the command applies Alembic migrations on startup before any
screener runs. Local scan history defaults to
`data/scanner.db`; deployments can point `DATABASE_URL` at Postgres or another
SQLAlchemy-supported database.

To run a custom set, repeat `--screener`:

```bash
python -m backend.jobs.run_daily_scan --screener technical_analysis --screener envelope
```

For a fixed, named schedule that cron or a hosting platform can run without long
flag lists, point the command at a YAML config (JOB-002):

```bash
python -m backend.jobs.run_daily_scan --config config/daily_scans.yaml
```

`config/daily_scans.yaml` is the committed Render/default schedule used by the
Blueprint cron. It contains no secrets, enables the deterministic daily set, and
keeps AI-heavy jobs disabled by default. Copy/edit it for your deployment, or
point `--config` at another repo-available file. Keep
`config/daily_scans.example.yaml` as the documented template when you want more
inline guidance. Each entry under `daily_scans` is one named scan batch:

```yaml
daily_scans:
  - name: Bollinger Band Reversal (daily)
    screener_key: bollinger_band_reversal
    enabled: true

  - name: Envelope Knoxville Buy (daily)
    screener_key: envelope_knoxville_buy
    enabled: true
    universe_key: hemant_super_45   # optional; defaults to the screener's universe
    params:                         # optional; merged over the screener defaults
      percent: 14.0

  - name: 67 Ka Funda (AI)
    screener_key: sixty_seven_ka_funda
    enabled: false                  # AI-heavy: opt in deliberately (see below)
```

Only `name` and `screener_key` are required; `enabled` defaults to `true`.
Disabled entries are skipped (and logged as skipped). `--config` and `--screener`
cannot be combined. A malformed YAML file, an unknown `screener_key` or
`universe_key`, or a config with no enabled entries each exit non-zero so a
scheduler notices the problem.

> **AI-heavy jobs are opt-in.** The `sixty_seven_ka_funda` and
> `technical_analysis` screeners call the Claude Agent SDK (and SerpAPI), so they
> cost API quota and depend on optional external services. They ship **disabled**
> in the committed Render/default schedule and the example config; enable them
> deliberately and consider lowering `max_ai_candidates` to cap per-run cost.

Exit code `0` means every selected scan persisted history and finished
`success` or `partial`. Exit code `1` means a fatal problem occurred, such as an
unknown screener key, missing setup, a failed screener, or 
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `backend/auth/__init__.py`
```python
"""Authentication helpers for the Streamlit app."""
```

#### File: `backend/__init__.py`
```python
"""Backend package for the Streamlit scanner app."""
```

#### File: `backend/ipo/sources/__init__.py`
```python
"""External source adapters for IPO ingestion.

Only modules in this package may perform network I/O for the IPO subsystem.
"""
```

#### File: `screeners/__init__.py`
```python
"""Pluggable screener modules.

Preferred screeners expose a `BaseScanner` subclass; legacy module-level
`SCREENER`, `run(...)`, and `build_chart(...)` aliases remain supported by the
registry for backwards compatibility.
"""
```

#### File: `backend/ipo/documents/__init__.py`
```python
"""Safe IPO prospectus download and local-cache services."""

from backend.ipo.documents.downloader import (
    IpoDocumentDownloadError,
    IpoDocumentDownloadErrorCode,
    IpoDocumentDownloadResult,
    download_document_file,
)

__all__ = [
    "IpoDocumentDownloadError",
    "IpoDocumentDownloadErrorCode",
    "IpoDocumentDownloadResult",
    "download_document_file",
]
```

#### File: `.streamlit/config.toml`
```python
# Streamlit theme for the Scanner App.
#
# The colors are chosen to match the embedded Lightweight Charts widget
# (see backend/charts.py): the page background equals the chart background,
# so the chart iframe blends seamlessly into the page, and the accent color
# is the chart's bullish-candle teal.
[theme]
base = "dark"
primaryColor = "#26a69a"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#161b26"
textColor = "#d0d4dc"
font = "sans serif"
```


==================================================


## [2/3] Repository: VWAP-HMA-RSI-NSE-Algorithm-Python (`WHEEL_VWAP-HMA-RSI-NSE-Algorithm-Python`)
- **Full Name**: `VWAP-HMA-RSI-NSE-Algorithm-Python`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Core Implementation Code & Architecture
#### File: `main.py`
```python
import pandas as pd
import numpy as np

def vwap(df):
    pv = (df['Close'] * df['Volume']).cumsum()
    vol = df['Volume'].cumsum()
    return pv / vol

def wma(s, p):
    w = np.arange(1, p + 1)
    return s.rolling(p).apply(lambda x: np.dot(x, w) / w.sum(), raw=True)

def hma(s, p):
    return wma(wma(s, int(p / 2)) * 2 - wma(s, p), int(np.sqrt(p)))

def rsi(s, p=14):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.rolling(p).mean()
    ma_down = down.rolling(p).mean()
    rs = ma_up / ma_down
    return 100 - (100 / (1 + rs))

def gen_signals(df, hma_period=55, rsi_period=14, stop_loss=0.02, take_profit=0.04):
    df['VWAP'] = vwap(df)
    df['HMA'] = hma(df['Close'], hma_period)
    df['RSI'] = rsi(df['Close'], rsi_period)

    df['Signal'] = 0
    df['SL'] = np.nan
    df['TP'] = np.nan

    pos = False
    entry = 0

    for i in range(len(df)):
        if not pos:
            if df['Close'].iloc[i] > df['VWAP'].iloc[i] and df['HMA'].iloc[i] > df['Close'].iloc[i-1] and df['RSI'].iloc[i] < 70:
                df.at[df.index[i], 'Signal'] = 1
                pos = True
                entry = df['Close'].iloc[i]
                df.at[df.index[i], 'SL'] = entry * (1 - stop_loss)
                df.at[df.index[i], 'TP'] = entry * (1 + take_profit)
        else:
            if df['Close'].iloc[i] <= entry * (1 - stop_loss) or df['Close'].iloc[i] >= entry * (1 + take_profit) or df['RSI'].iloc[i] > 70:
                df.at[df.index[i], 'Signal'] = -1
                pos = False
                entry = 0
    return df
```


==================================================


## [3/3] Repository: algo-trading-bot-fyers (`WHEEL_algo-trading-bot-fyers`)
- **Full Name**: `algo-trading-bot-fyers`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# algo-trading-bot-fyers
Python algorithmic trading bot for NSE — EMA+VWAP strategies, ATR-based stop loss, Fyers API v3
# Python Algorithmic Trading Bot — Fyers API v3 (NSE India)

> Fully automated intraday + swing trading bot for the Indian stock market. Built with Python and Fyers API v3. Capital under ₹50,000.

---

## ⚡ Strategies

### 1. EMA + VWAP Momentum
- Entry when price crosses above EMA and is trading above VWAP
- Confirms trend direction before entry
- Designed for trending intraday sessions

### 2. VWAP Reversal
- Entry when price deviates significantly from VWAP and shows reversal signal
- Targets mean-reversion moves
- Best used in range-bound sessions

### 3. Daily EMA Crossover Swing
- Swing strategy based on daily timeframe EMA crossovers
- Holds positions overnight
- Lower trade frequency, higher R:R target

---

## 🛡️ Risk Management

| Parameter | Value |
|---|---|
| Risk per trade | ~1% of capital |
| Daily loss halt | Triggers auto-stop for the day |
| Weekly loss halt | Triggers auto-stop for the week |
| Intraday square-off | Automatic before market close |
| Capital | < ₹50,000 |

---

## 🧠 ATR-Based Anti-Stop-Hunt Stop Loss

Standard fixed stop losses get hunted by smart money. This bot places SLs intelligently:

```
SL Logic:
1. Calculate ATR for the timeframe
2. Identify nearest swing high (short) or swing low (long)
3. Place SL beyond the swing level + ATR buffer
4. Shift SL away from round price numbers (e.g. avoid exactly 500.00)
```

This reduces the chance of being stopped out by stop-hunting wicks before the trade moves in your direction.

---

## 🏗️ Architecture

```
algo-trading-bot/
├── main.py               ← Entry point, scheduler
├── strategies/
│   ├── ema_vwap.py       ← Strategy 1
│   ├── vwap_reversal.py  ← Strategy 2
│   └── ema_crossover.py  ← Strategy 3
├── risk/
│   ├── stop_loss.py      ← ATR-based SL logic
│   └── position_size.py  ← 1% risk per trade sizing
├── broker/
│   └── fyers_api.py      ← Fyers API v3 wrapper
├── utils/
│   ├── indicators.py     ← EMA, VWAP, ATR calculations
│   └── scheduler.py      ← Intraday auto square-off
└── config.py             ← API keys, symbols, parameters
```

---

## ⏰ Scheduling

- Market open: strategies activate at 9:20 AM IST (post-opening volatility settles)
- Auto square-off: all intraday positions closed by 3:15 PM IST
- Swing positions: held overnight, reviewed pre-market next day

---

## 🔧 Setup

```bash
# Clone the repo
git clone https://github.com/aayushawadhiya07-code/algo-trading-bot-fyers.git
cd algo-trading-bot-fyers

# Install dependencies
pip install fyers-apiv3 pandas numpy schedule

# Configure
cp config_sample.py config.py
# Add your Fyers API credentials in config.py

# Run
python main.py
```

---

## ⚠️ Disclaimer

This bot is for **educational and personal use only**. Trading in financial markets involves substantial risk. Past performance does not guarantee future results. Use at your own risk. This is not financial advice.

---

## 🛠️ Tech

`Python 3.10+` `Fyers API v3` `Pandas` `NumPy` `ATR` `EMA` `VWAP` `Schedule`

---

## 👤 Author

**Aayush Awadhiya** — [LinkedIn](https://linkedin.com/in/aayushawadhiya) | [GitHub](https://github.com/aayushawadhiya07-code)


==================================================
