# ⚡ [QUANT-SOURCE-067] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_067_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: bhav (`VAULT_IN-QUANT-085_rajmaurya0904__bhav`)
- **Full Name**: `IN-QUANT-085_rajmaurya0904__bhav`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<div align="center">

<img src="docs/assets/logo.svg" alt="Bhav" width="116" />

# Bhav ( `bhav` )

**Open-source options backtesting engine for NSE (India).** Write a strategy in Python, run it against real 1-minute spot + option data, and get a deterministic Parquet result with a full metrics dashboard.

[Install](#install) · [Quickstart](#quickstart--cli) · [Generate with Claude](#generate-with-claude-no-api-key) · [Writing strategies](docs/writing-strategies.md) · [How it works](#how-it-works) · [License](#license)

<br/>

<img src="docs/assets/hero.svg" alt="bhav run — NIFTY short-straddle backtest with Monte Carlo robustness bands" width="840" />

<sub>The <code>bhav</code> CLI — one command, deterministic Parquet output with a full metrics + Monte&nbsp;Carlo summary.</sub>

<br/><br/>

<img src="docs/assets/dashboard.png" alt="Bhav web dashboard — KPI grid and equity curve for a 6-month NIFTY short-straddle backtest" width="840" />

<sub>The web UI — KPI grid, equity curve, drawdown, P&amp;L distribution, and the full trade log.</sub>

<br/>

<em>Hindi / Marathi / Gujarati for “market rate” — what every Indian trader means by “aaj ka bhav kya hai?”</em>

</div>

Open-source and built specifically around Upstox's historical-data endpoints — expired option chains included, so you can backtest premiums for contracts that expired months or years ago, not just currently-listed ones.

- Bar-by-bar simulation on 1-minute NIFTY/BANKNIFTY/SENSEX (and other index) spot + option chain data
- Strategy API modeled on lifecycle hooks (`on_bar`, `on_day_start`, `on_day_end`, ...) — write plain Python, get deterministic Parquet output
- Pulls expired option contracts directly from Upstox's `expired-instruments` endpoints, so you can backtest premiums for contracts that expired months or years ago, not just currently-listed ones
- Realistic Indian cost model: STT (sell + exercised ITM), brokerage, exchange txn charge, SEBI charges, stamp duty, GST
- Engine-level `warmup_days` so lookback strategies (rolling S/R, moving averages) get correct history from day one of the window
- Futures-aware ATM selection: `--atm-reference futures` picks the ATM strike off the future (which NIFTY options actually price against) instead of the raw spot index, removing the basis bias — the front-month future is auto-rolled per day from Upstox's instrument master, so no per-expiry key to hand-feed (or pin one with `--futures-key`)
- Partial (tranche) closes: `ctx.close(key, lots=N)` peels off one slice of a position that accumulated from several entries, instead of dumping the whole key
- Local Parquet cache — every Upstox candle is fetched once, then reused across runs
- Per-underlying lot size / ATM-step table (NIFTY, BANKNIFTY, FINNIFTY, MIDCPNIFTY, NIFTYNXT50, SENSEX, BANKEX, SENSEX50) with auto-lookup
- FastAPI backend + Next.js frontend: upload a strategy file, set token/dates/capital, run a real backtest, see equity curve, drawdown, P&L distribution, and full trade log
- **Generate strategies with Claude, no API key** — `bhav generate "your idea"` (or the "Generate with Claude" panel on `/new`) drives the locally installed `claude` CLI to turn plain English into a contract-compliant strategy file
- **Static safety gate** — every uploaded or AI-generated strategy is scanned by an AST validator (`bhav/ai/validate.py`) that rejects `os`/`subprocess`/`eval`/`open`/network imports before the file is ever executed
- **Monte Carlo robustness** — each backtest bootstraps its trade sequence 1000× to report a 5–95% return band, worst-case (p95) drawdown, probability of profit, and risk of ruin
- No Upstox access? A bundled 1-year NIFTY sample dataset (`sample_data/nifty_1y_1min.xlsx`) lets anyone backtest offline with no token, any strategy: the bundled examples, hand-written, or AI-generated via `docs/ai-prompt.md`

## Status

**v0.2.** Multi-leg strategies now work: CE+PE combinations (straddles, strangles) and same-side multi-strike spreads (verticals, iron condors, ratios) in live Upstox mode — and offline wherever the bundled workbook carries a strike chain. Margin/SPAN modeling and multi-underlying portfolios are still to come. Upstox-only for live data; more brokers (Zerodha Kite, Angel One, Fyers, ...) are on the roadmap — the data layer (`bhav/data/upstox_client.py`) is a single swappable client, so adding another broker means implementing the same 4-endpoint interface, not touching the engine.

### New in v0.2

- **Generate strategies from plain English** with the local Claude CLI — no API key — gated by an AST validator that rejects unsafe code before it runs.
- **Monte Carlo robustness bands** on every run: return/drawdown confidence intervals, probability of profit, risk of ruin.
- **Futures-basis ATM** with per-day front-month **auto-roll** — `--atm-reference futures` removes the spot-vs-future basis bias without a hand-fed key.
- **Partial/tranche closes** — `ctx.close(key, lots=N)` scales out one slice of an aggregated position.
- **Strike-aware offline dataset** — same-side spreads are now testable without a broker account (bundled ±2 chain across June 2026; regenerate/widen with `scripts/build_sample_data.py`).

## Requirements

- Python 3.11+
- Node.js 20+ (only needed for the frontend)
- To backtest with live/full data: an Upstox Pro account with historical data API access, and an access token (expires daily around 03:30 IST — generate a fresh one each session)
- To try Bhav without a broker account: nothing extra. Use `--data-source excel` (CLI) or "Sample data" (web UI) to run against the bundled NIFTY dataset

## Install

One command (clones the repo, installs the Python package, installs frontend deps):

```powershell
npx @rajmaurya0904/create-bhav
```

Or manually:

```powershell
git clone https://github.com/rajmaurya0904/bhav.git
cd bhav

# backend
pip install -e .

# frontend (optional, only if you want the web UI)
cd frontend
npm install
```

## Quickstart — CLI

With a live Upstox token:

```powershell
$env:UPSTOX_TOKEN = "your_token"
bhav run examples/orb_v1.py --start 2025-08-01 --end 2025-11-30
```

Or with no broker account at all, using the bundled sample dataset:

```powershell
bhav run examples/orb_v1.py --start 2025-08-01 --end 2025-11-30 --data-source excel
```

Useful flags:

```
--underlying "NSE_INDEX|Nifty 50"   # default; see lot-size table below for others (upstox mode only)
--capital 500000                    # starting capital, default 500000
--lot-size 0                        # 0 = auto-lookup per underlying, or set explicitly
--warmup-days 3                     # pre-window replay so lookback strategies have history from day 1
--data-source upstox|excel          # default upstox; excel = bundled offline NIFTY dataset, no token needed
--excel-path path/to/file.xlsx      # only with --data-source excel; defaults to sample_data/nifty_1y_1min.xlsx
--atm-reference spot|futures        # default spot; 'futures' picks the ATM strike off the future, not spot
--futures-key "NSE_FO|..."          # optional; pin one future. Omit to auto-roll the front month per day (upstox mode only)
```

Results are written to `runs/<run_id>/` as `trades.parquet`, `equity_curve.parquet`, `metrics.json`, and `manifest.json` (with a SHA256 checksum of the metrics for reproducibility).

## Quickstart — Web UI

```powershell
# terminal 1: API server
bhav-server

# terminal 2: frontend
cd frontend
npm run dev
```

Open `http://localhost:3000`. Go to `/new`, upload a strategy `.py` file, pick a data source (Upstox live, or the bundled sample data — no token needed), set dates/underlying/capital/lot size/warmup days, and run. The results page polls until the run completes and shows total return, CAGR, Sharpe/Sortino, max drawdown, win rate, profit factor, expectancy, an equity curve, a drawdown curve, a P&L distribution, and the full trade log.

## Offline sample dataset

`sample_data/nifty_1y_1min.xlsx` bundles a year of NIFTY 50 data (Jul 2025-Jun 2026) so anyone can try Bhav without an Upstox account:

- `Spot_1min`: 1-minute NIFTY 50 spot candles
- `ATM_Options_1min`: 1-minute option candles (nearest weekly expiry). Most days carry the real ATM CE and PE; the most recent month (**June 2026**) carries a ±2-strike chain (ATM and two strikes either side) so multi-strike spreads are testable offline

`--data-source excel` (or the "Sample data" option in the web UI) works with **any** strategy file, not just the ones in `examples/` — hand-written, or generated by an AI following `docs/ai-prompt.md`. Point it at your own `.py` file exactly like you would with live Upstox data; the engine doesn't care where the strategy came from, only where the candles come from.

Strike coverage is whatever the workbook holds for each day. `strike_offset` in `ctx.buy_option()` is **honored on chain days** (so verticals/iron condors resolve to distinct strikes) and **falls back to the nearest available strike on ATM-only days** (so a same-side spread's legs collapse onto the ATM contract there). Good enough to validate strategy logic, spread mechanics, and cost modeling end to end; switch to `--data-source upstox` for the full chain on every day, other underlyings, and date ranges beyond what's bundled. Regenerate or widen the offline chain yourself with `scripts/build_sample_data.py` (needs a live token).

## Write your own strategy

A strategy is one Python file that exposes a `strategy` variable. Minimum viable example:

```python
from bhav.engine.strategy import Context, Strategy

class BuyATMCallAtOpen(Strategy):
    name = "buy_atm_call_at_open"

    def on_bar(self, ctx: Context) -> None:
        hhmm = f"{ctx.bar.timestamp.hour:02d}:{ctx.bar.timestamp.minute:02d}"
        if hhmm == "09:30" and not ctx.portfolio.positions:
            ctx.buy_option(option_type="CE", strike_offset=0, lots=1)

strategy = BuyATMCallAtOpen()
```

Full guide with API reference, worked examples, common patterns, and common mistakes (including the broker-candle-order gotcha): [docs/writing-strategies.md](docs/writing-strategies.md).

Don't want to write the Python yourself? [docs/ai-prompt.md](docs/ai-prompt.md) has a copy-pasteable prompt block that gets ChatGPT/Claude/Gemini to generate a strategy following Bhav's contract — the `/new` page in the frontend has the same prompt with a one-click copy button.

### Generate with Claude (no API key)

If you have [Claude Code](https://claude.com/claude-code) installed and signed in, Bhav can drive it for you — no `ANTHROPIC_API_KEY` needed. It shells out to the local `claude` CLI, feeds it the strategy contract plus your description, and writes back a validated `.py`:

```powershell
bhav generate "Sell an ATM straddle at 09:20. Cut both legs if the combined premium loss hits 30%. Otherwise hold to the 15:15 square-off." --out my_straddle.py
bhav run my_straddle.py --start 2025-08-01 --end 2025-09-30 --data-source excel
```

The `/new` page in the web UI has the same thing as a "Generate with Claude" panel: type your idea, click generate, review the code, and it's auto-attached to the run form. A CLI-connected / not-detected badge tells you whether the backend can reach `claude`.

Whether written by hand, generated, or uploaded, every strategy passes through an AST validator before it runs — a hallucinated `import os` or a stray `eval()` is rejected with a clear error rather than silently executed. It raises the bar; it is not a full sandbox, so still read AI-generated code before trusting it with real money.

### Reference strategies

All in [examples/](examples/), runnable as-is:

| File | Idea |
|---|---|
| [orb_v1.py](examples/orb_v1.py) | Opening-range breakout/fade on ATM options, SL/target/trailing-SL ladder, hard time exit |
| [morning_3min_momentum.py](examples/morning_3min_momentum.py) | First two 3-min candles at open; second candle's color picks CE/PE |
| [morning_momentum.py](examples/morning_momentum.py) | Point-move threshold from day open by 09:30 |
| [straddle_sell_920.py](examples/straddle_sell_920.py) | Short straddle sold shortly after open |
| [spike_fade.py](examples/spike_fade.py) | Fade a fast spot spike |

## Lot sizes (Jan 2026 revision)

| Underlying | Lot size | ATM step |
|---|---|---|
| NIFTY 50 | 65 | 50 |
| BANK NIFTY | 25 | 100 |
| FIN NIFTY | 65 | 50 |
| MIDCAP NIFTY | 120 | 25 |
| NIFTY NEXT 50 | 25 | 100 |
| SENSEX | 20 | 100 |
| BANKEX | 30 | 100 |
| SENSEX 50 | 60 | 100 |

Pass `--lot-size 0` (CLI) or leave lot size on auto (UI) to use this table automatically per underlying.

## How it works

1. `bhav.data.upstox_client.UpstoxClient` wraps Upstox's 4 relevant endpoints: `historical-candle` (spot), `expired-instruments/expiries`, `expired-instruments/option/contract`, `expired-instruments/historical-candle` (expired option premiums).
2. `bhav.data.cache.ParquetCache` caches every candle series to `~/.bhav/cache`, keyed by instrument + interval + date, always sorted ascending by timestamp.
3. `bhav.engine.bar_engine.BarEngine` replays 1-minute bars in order, calling your strategy's lifecycle hooks, optionally preceded by `warmup_days` of no-op replay so lookback state is built before live trading starts.
4. `bhav.engine.portfolio.Portfolio` tracks positions and realized trades, applying `bhav.engine.costs.IndianCostModel` on every fill.
5. `bhav.metrics.report` computes CAGR, Sharpe, Sortino, max drawdown, win rate, profit factor, and expectancy from the equity curve and trade log. `bhav.metrics.montecarlo` then bootstraps the trade sequence to produce return/drawdown confidence bands and risk of ruin.
6. `bhav.output.writer.ResultWriter` writes everything to `runs/<run_id>/` as Parquet + JSON (`trades`, `equity_curve`, `metrics`, `montecarlo`) with a manifest and checksum.

Strategy generation and safety live in `bhav.ai`: `prompt.py` (the canonical contract), `claude_generator.py` (the `claude` CLI subprocess wrapper), and `validate.py` (the AST gate applied to every strategy before execution).

## License

MIT.

### Core Implementation Code & Architecture
#### File: `bhav/api/__init__.py`
```python
from bhav.api.server import app

__all__ = ["app"]
```

#### File: `bhav/output/__init__.py`
```python
from bhav.output.writer import ResultWriter

__all__ = ["ResultWriter"]
```

#### File: `bhav/__init__.py`
```python
"""Bhav: NSE options backtesting engine, Upstox-native."""

__version__ = "0.1.0-alpha"
```

#### File: `bhav/metrics/__init__.py`
```python
from bhav.metrics.report import MetricsReport, compute_metrics

__all__ = ["MetricsReport", "compute_metrics"]
```

#### File: `bhav/engine/__init__.py`
```python
from bhav.engine.bar_engine import BarEngine, EngineConfig
from bhav.engine.costs import CostModel, IndianCostModel
from bhav.engine.portfolio import Portfolio, Position, Trade
from bhav.engine.strategy import Context, Strategy

__all__ = [
    "BarEngine",
    "Context",
    "CostModel",
    "EngineConfig",
    "IndianCostModel",
    "Portfolio",
    "Position",
    "Strategy",
    "Trade",
]
```

#### File: `create-bhav/package.json`
```python
{
  "name": "@rajmaurya0904/create-bhav",
  "version": "0.1.0",
  "description": "Scaffold Bhav, an open-source NSE options backtesting engine, with one command",
  "license": "MIT",
  "author": "Raj Maurya",
  "repository": {
    "type": "git",
    "url": "https://github.com/rajmaurya0904/bhav.git"
  },
  "homepage": "https://github.com/rajmaurya0904/bhav",
  "keywords": ["nse", "options", "backtesting", "trading", "upstox", "india"],
  "bin": {
    "create-bhav": "./bin/create-bhav.js"
  },
  "files": ["bin"],
  "engines": {
    "node": ">=18"
  },
  "publishConfig": {
    "access": "public"
  }
}
```


==================================================


## [2/3] Repository: stock_data_analyzer (`VAULT_IN-QUANT-091_hhemanth__stock_data_analyzer`)
- **Full Name**: `IN-QUANT-091_hhemanth__stock_data_analyzer`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)



==================================================


## [3/3] Repository: ta (`WHEEL_ta`)
- **Full Name**: `ta`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
![CircleCI](https://img.shields.io/circleci/build/github/bukosabino/ta/master)
[![Documentation Status](https://readthedocs.org/projects/technical-analysis-library-in-python/badge/?version=latest)](https://technical-analysis-library-in-python.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/bukosabino/ta/badge.svg)](https://coveralls.io/github/bukosabino/ta)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linter: Prospector](https://img.shields.io/badge/Linter-Prospector-coral.svg)](http://prospector.landscape.io/en/master/)
![PyPI](https://img.shields.io/pypi/v/ta)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ta)
[![Donate PayPal](https://img.shields.io/badge/Donate%20%24-PayPal-brightgreen.svg)](https://www.paypal.me/guau/3)

# Technical Analysis Library in Python

It is a Technical Analysis library useful to do feature engineering from financial time series datasets (Open, Close, High, Low, Volume). It is built on Pandas and Numpy.

![Bollinger Bands graph example](static/figure.png)

The library has implemented 43 indicators:

## Volume


ID | Name | Class | defs
-- |-- |-- |-- |
1 | Money Flow Index (MFI) | [MFIIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.MFIIndicator) | [money_flow_index](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.money_flow_index)
2 | Accumulation/Distribution Index (ADI) | [AccDistIndexIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.AccDistIndexIndicator) | [acc_dist_index](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.acc_dist_index)
3 | On-Balance Volume (OBV) | [OnBalanceVolumeIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.OnBalanceVolumeIndicator) | [on_balance_volume](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.on_balance_volume)
4 | Chaikin Money Flow (CMF) | [ChaikinMoneyFlowIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.ChaikinMoneyFlowIndicator) | [chaikin_money_flow](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.chaikin_money_flow)
5 | Force Index (FI) | [ForceIndexIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.ForceIndexIndicator) | [force_index](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.force_index)
6 | Ease of Movement (EoM, EMV) | [EaseOfMovementIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.EaseOfMovementIndicator) | [ease_of_movement](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.ease_of_movement)<br>[sma_ease_of_movement](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.sma_ease_of_movement)
7 | Volume-price Trend (VPT) | [VolumePriceTrendIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.VolumePriceTrendIndicator)| [volume_price_trend](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.volume_price_trend)
8 | Negative Volume Index (NVI) | [NegativeVolumeIndexIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.NegativeVolumeIndexIndicator)| [negative_volume_index](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.negative_volume_index)
9 | Volume Weighted Average Price (VWAP) | [VolumeWeightedAveragePrice](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.VolumeWeightedAveragePrice) | [volume_weighted_average_price](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volume.volume_weighted_average_price)



<br>

## Volatility

ID | Name | Class | defs
-- |-- |-- |-- |
10 | Average True Range (ATR) | [AverageTrueRange](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.AverageTrueRange) | [average_true_range](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.average_true_range)
11 | Bollinger Bands (BB) | [BollingerBands](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.BollingerBands) | [bollinger_hband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.bollinger_hband)<br>[bollinger_hband_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.bollinger_hband_indicator)<br>[bollinger_lband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.bollinger_lband)<br>[bollinger_lband_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.bollinger_lband_indicator)<br>[bollinger_mavg](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.bollinger_mavg)<br>[bollinger_pband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.bollinger_pband)<br>[bollinger_wband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.bollinger_wband)
12 | Keltner Channel (KC) | [KeltnerChannel](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.KeltnerChannel) |  [keltner_channel_hband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.keltner_channel_hband)<br>[keltner_channel_hband_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.keltner_channel_hband_indicator)<br>[keltner_channel_lband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.keltner_channel_lband)<br>[keltner_channel_lband_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.keltner_channel_lband_indicator)<br>[keltner_channel_mband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.keltner_channel_mband)<br>[keltner_channel_pband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.keltner_channel_pband)<br>[keltner_channel_wband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.keltner_channel_wband)
13 | Donchian Channel (DC) | [DonchianChannel](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.DonchianChannel)| [donchian_channel_hband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.donchian_channel_hband)<br>[donchian_channel_lband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.donchian_channel_lband)<br>[donchian_channel_mban](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.donchian_channel_mband)<br>[donchian_channel_pband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.donchian_channel_pband)<br>[donchian_channel_wband](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.donchian_channel_wband)
14 | Ulcer Index (UI) | [UlcerIndex](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.UlcerIndex)|  [ulcer_index](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.ulcer_index)

<br>

## Trend

ID | Name | Class | defs
-- |-- |-- |-- |
15 | Simple Moving Average (SMA) | [SMAIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.SMAIndicator) | [sma_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.sma_indicator)
16 | Exponential Moving Average (EMA) | [EMAIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.EMAIndicator)  | [ema_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.ema_indicator) | Trend
17 | Weighted Moving Average (WMA) | [WMAIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.WMAIndicator) | [wma_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.wma_indicator)
18 | Moving Average Convergence Divergence (MACD) | [MACD](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.MACD) | [macd](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.macd) <br>[macd_diff](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.macd_diff)<br>[macd_signal](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.macd_signal)
19 | Average Directional Movement Index (ADX) | [ADXIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.ADXIndicator) | [adx](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.adx)<br>[adx_neg](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.adx_neg)<br>[adx_pos](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.adx_pos)
20 | Vortex Indicator (VI) | [VortexIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.VortexIndicator) | [vortex_indicator_neg](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.vortex_indicator_neg) <br>[vortex_indicator_pos](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.vortex_indicator_pos)
21 | Trix (TRIX) | [TRIXIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.TRIXIndicator) | [trix](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.trix)
22 | Mass Index (MI) | [MassIndex](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.MassIndex) | [mass_index](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.mass_index)
23 | Commodity Channel Index (CCI) | [CCIIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.CCIIndicator)| [cci](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.cci)
24 | Detrended Price Oscillator (DPO) | [DPOIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.DPOIndicator) | [dpo](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.dpo)
25 | KST Oscillator (KST) | [KSTIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.KSTIndicator)  | [kst](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.kst)<br>[kst_sig](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.kst_sig)
26 | Ichimoku Kinkō Hyō (Ichimoku) | [IchimokuIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.IchimokuIndicator) | [ichimoku_a](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.ichimoku_a)<br>[ichimoku_b](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.ichimoku_b)<br>[ichimoku_base_line](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.ichimoku_base_line)<br>[ichimoku_conversion_line](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.ichimoku_conversion_line)
27 | Parabolic Stop And Reverse (Parabolic SAR) | [PSARIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.PSARIndicator) | [psar_down](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.psar_down) <br>[psar_down_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.psar_down_indicator)<br>[psar_up](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.psar_up)<br>[psar_up_indicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.psar_up_indicator)
28 | Schaff Trend Cycle (STC) | [STCIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.STCIndicator) | [stc](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.stc)
29 | Aroon Indicator | [AroonIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.AroonIndicator) | [aroon_down](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.aroon_down)<br>[aroon_up](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.aroon_up)




<br>

## Momentum

ID | Name | Class | defs
-- |-- |-- |-- |
30 | Relative Strength Index (RSI) | [RSIIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.RSIIndicator) | [rsi](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.rsi)
31 | Stochastic RSI (SRSI) | [StochRSIIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.StochRSIIndicator) | [stochrsi](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.stochrsi)<br>[stochrsi_d](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.stochrsi_d)<br>[stochrsi_k](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.stochrsi_k)
32 | True strength index (TSI) | [TSIIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.TSIIndicator) | [tsi](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.tsi)
33 | Ultimate Oscillator (UO) | [UltimateOscillator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.UltimateOscillator) | [ultimate_oscillator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.ultimate_oscillator)
34 | Stochastic Oscillator (SR) | [StochasticOscillator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.StochasticOscillator) | [stoch](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.stoch)<br>[stoch_signal](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.stoch_signal)
35 | Williams %R (WR) | [WilliamsRIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.WilliamsRIndicator) | [williams_r](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.williams_r)
36 | Awesome Oscillator (AO) | [AwesomeOscillatorIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.AwesomeOscillatorIndicator) | [awesome_oscillator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.awesome_oscillator)
37 | Kaufman's Adaptive Moving Average (KAMA) | [KAMAIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.KAMAIndicator) | [kama](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.kama)
38 | Rate of Change (ROC) | [ROCIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.ROCIndicator) | [roc](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.roc)
39 | Percentage Price Oscillator (PPO) | [PercentagePriceOscillator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.PercentagePriceOscillator) | [ppo](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.ppo)<br>[ppo_hist](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.ppo_hist)<br>[ppo_signal](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.ppo_signal)
40 | Percentage Volume Oscillator (PVO) | [PercentageVolumeOscillator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.PercentageVolumeOscillator) | [pvo](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.pvo)<br>[pvo_hist](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.pvo_hist)<br>[pvo_signal](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.pvo_signal)


<br>

## Others

ID | Name | Class | defs
-- |-- |-- |-- |
41 | Daily Return (DR) | [DailyReturnIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.others.DailyReturnIndicator) | [daily_return](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.others.daily_return)
42 | Daily Log Return (DLR) | [DailyLogReturnIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.others.DailyLogReturnIndicator) | [daily_log_return](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.others.daily_log_return)
43 | Cumulative Return (CR) | [CumulativeReturnIndicator](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.others.CumulativeReturnIndicator) | [cumulative_return](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.others.cumulative_return)

<br>


# Documentation

https://technical-analysis-library-in-python.readthedocs.io/en/latest/


# Motivation to use

* [English](https://towardsdatascience.com/technical-analysis-library-to-financial-datasets-with-pandas-python-4b2b390d3543)
* [Spanish](https://medium.com/datos-y-ciencia/biblioteca-de-an%C3%A1lisis-t%C3%A9cnico-sobre-series-temporales-financieras-para-machine-learning-con-cb28f9427d0)


# How to use (Python 3)

```sh
$ pip install --upgrade ta
```

To use this library you should have a financial time series dataset including `Timestamp`, `Open`, `High`, `Low`, `Close` and `Volume` columns.

You should clean or fill NaN values in your dataset before add technical analysis features.

You can get code examples in [examples_to_use](https://github.com/bukosabino/ta/tree/master/examples_to_use) folder.

You can visualize the features in [this notebook](https://github.com/bukosabino/ta/blob/master/examples_to_use/visualize_features.ipynb).


#### Example adding all features

```python
import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna


# Load datas
df = pd.read_csv('ta/tests/data/datas.csv', sep=',')

# Clean NaN values
df = dropna(df)

# Add all ta features
df = add_all_ta_features(
    df, open="Open", high="High", low="Low", close="Close", volume="Volume_BTC")
```


#### Example adding particular feature

```python
import pandas as pd
from ta.utils import dropna
from ta.volatility import BollingerBands


# Load datas
df = pd.read_csv('ta/tests/data/datas.csv', sep=',')

# Clean NaN values
df = dropna(df)

# Initialize Bollinger Bands Indicator
indicator_bb = BollingerBands(close=df["Close"], window=20, window_dev=2)

# Add Bollinger Bands features
df['bb_bbm'] = indicator_bb.bollinger_mavg()
df['bb_bbh'] = indicator_bb.bollinger_hband()
df['bb_bbl'] = indicator_bb.bollinger_lband()

# Add Bollinger Band high indicator
df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

# Add Bollinger Band low indicator
df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()

# Add Width Size Bollinger Bands
df['bb_bbw'] = indicator_bb.bollinger_wband()

# Add Percentage Bollinger Bands
df['bb_bbp'] = indicator_bb.bollinger_pband()
```


# Deploy and develop (for developers)

```sh
$ git clone https://github.com/bukosabino/ta.git
$ cd ta
$ pip install -r requirements-play.txt
$ make test
```


# Sponsor

![Logo OpenSistemas](static/logo_neuroons_byOS_blue.png)

Thank you to [OpenSistemas](https://opensistemas.com)! It is because of your contribution that I am able to continue the development of this open source library.


# Based on

* https://en.wikipedia.org/wiki/Technical_analysis
* https://pandas.pydata.org
* https://github.com/FreddieWitherden/ta
* https://github.com/femtotrader/pandas_talib


# In Progress

* Automated tests for all the indicators.


# TODO

* Use [NumExpr](https://github.com/pydata/numexpr) to speed up the NumPy/Pandas operations? [Article Motivation](https://towardsdatascience.com/speed-up-your-numpy-and-pandas-with-numexpr-package-25bd1ab0836b)
* Add [more technical analysis features](https://en.wikipedia.org/wiki/Technical_analysis).
* Wrapper to get financial data.
* Use of the Pandas multi-indexing techniques to calculate several indicators at the same time.
* Use Plotly/Streamlit to visualize features


# Changelog

Check the [changelog](https://github.com/bukosabino/ta/blob/master/RELEASE.md) of project.


# Donation

If you think `ta` library help you, please consider [buying me a coffee](https://www.paypal.me/guau/3).



# Credits

Developed by Darío López Padial (aka Bukosabino) and [other contributors](https://github.com/bukosabino/ta/graphs/contributors).

Please, let me know about any comment or feedback.

Also, I am a software engineer freelance focused on Data Science using Python tools such as Pandas, Scikit-Learn, Backtrader, Zipline or Catalyst. Don't hesitate to contact me if you need to develop something related with this library, Python, Technical Analysis, AlgoTrading, Machine Learning, etc.

### Core Implementation Code & Architecture
#### File: `examples_to_use/roc.py`
```python
"""This is a example adding volume features.
"""
import pandas as pd
import ta

# Load data
df = pd.read_csv("../test/data/datas.csv", sep=",")

# Clean nan values
df = ta.utils.dropna(df)

window = 12
df[f"roc_{window}"] = ta.momentum.ROCIndicator(close=df["Close"], window=window).roc()
```

#### File: `examples_to_use/volume_features_example.py`
```python
"""This is a example adding volume features.
"""
import pandas as pd
import ta

# Load data
df = pd.read_csv("../test/data/datas.csv", sep=",")

# Clean nan values
df = ta.utils.dropna(df)

print(df.columns)

# Add all volume features filling nans values
df = ta.add_volume_ta(df, "High", "Low", "Close", "Volume_BTC", fillna=True)

print(df.columns)
```

#### File: `examples_to_use/all_features_example.py`
```python
"""This is a example adding all technical analysis features implemented in
this library.
"""
import pandas as pd
import ta

# Load data
df = pd.read_csv("../test/data/datas.csv", sep=",")

# Clean nan values
df = ta.utils.dropna(df)

print(df.columns)

# Add all ta features filling nans values
df = ta.add_all_ta_features(
    df, "Open", "High", "Low", "Close", "Volume_BTC", fillna=True
)

print(df.columns)
print(len(df.columns))
```

#### File: `ta/__init__.py`
```python
"""It is a Technical Analysis library useful to do feature
engineering from financial time series datasets (Open,
Close, High, Low, Volume). It is built on Pandas and Numpy.

.. moduleauthor:: Dario Lopez Padial (Bukosabino)

"""
from ta.wrapper import (
    add_all_ta_features,
    add_momentum_ta,
    add_others_ta,
    add_trend_ta,
    add_volatility_ta,
    add_volume_ta,
)

__all__ = [
    "add_all_ta_features",
    "add_momentum_ta",
    "add_others_ta",
    "add_trend_ta",
    "add_volatility_ta",
    "add_volume_ta",
]
```

#### File: `examples_to_use/bollinger_band_features_example.py`
```python
"""This is a example adding bollinger band features.
"""
import pandas as pd
import ta

# Load data
df = pd.read_csv("../test/data/datas.csv", sep=",")

# Clean nan values
df = ta.utils.dropna(df)

print(df.columns)

# Add bollinger band high indicator filling nans values
df["bb_high_indicator"] = ta.volatility.bollinger_hband_indicator(
    df["Close"], window=20, window_dev=2, fillna=True
)

# Add bollinger band low indicator filling nans values
df["bb_low_indicator"] = ta.volatility.bollinger_lband_indicator(
    df["Close"], window=20, window_dev=2, fillna=True
)

print(df.columns)
```

#### File: `setup.py`
```python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name="ta",
    packages=["ta"],
    version="0.11.0",
    description="Technical Analysis Library in Python",
    long_description="It is a Technical Analysis library to financial time series datasets. You can use to do feature engineering. It is built on Python Pandas library.",
    author="Dario Lopez Padial (Bukosabino)",
    author_email="Bukosabino@gmail.com",
    url="https://github.com/bukosabino/ta",
    maintainer="Dario Lopez Padial (Bukosabino)",
    maintainer_email="Bukosabino@gmail.com",
    install_requires=[
        "numpy",
        "pandas",
    ],
    download_url="https://github.com/bukosabino/ta/tarball/0.11.0",
    keywords=["technical analysis", "python3", "pandas"],
    license="The MIT License (MIT)",
    license_files=["LICENSE"],
    classifiers=[
        "Intended Audience :: Financial and Insurance Industry",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Documentation": "https://technical-analysis-library-in-python.readthedocs.io/en/latest/",
        "Bug Reports": "https://github.com/bukosabino/ta/issues",
        "Source": "https://github.com/bukosabino/ta",
    },
)
```


==================================================
