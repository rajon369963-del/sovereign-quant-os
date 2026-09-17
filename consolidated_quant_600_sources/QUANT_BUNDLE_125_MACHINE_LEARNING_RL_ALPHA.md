# ⚡ [QUANT-SOURCE-125] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_125_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: vectorbt (`VAULT_IN-QUANT-096_polakowo__vectorbt`)
- **Full Name**: `IN-QUANT-096_polakowo__vectorbt`
- **Description**: The backtesting engine that gives you an unfair advantage. Run thousands of trading ideas before others finish one.
- **GitHub Stars**: 9100
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<div align="center">
    <a href="https://vectorbt.pro/" title="VectorBT PRO">
        <img src="https://raw.githubusercontent.com/polakowo/vectorbt/master/docs/docs/assets/logo/header-pro.svg" />
    </a>
</div>
<div align="center">
    <a href="https://vectorbt.dev/" title="vectorbt">
        <img src="https://raw.githubusercontent.com/polakowo/vectorbt/master/docs/docs/assets/logo/header.svg" />
    </a>
</div>

<br>

<p align="center">
    <a href="https://pepy.tech/project/vectorbt" title="Downloads">
        <img src="https://img.shields.io/pepy/dt/vectorbt?label=downloads&color=blue" />
    </a>
    <a href="https://pypi.org/project/vectorbt" title="PyPI">
        <img src="https://img.shields.io/pypi/v/vectorbt" />
    </a>
    <a href="https://pypi.org/project/vectorbt" title="Supported Python versions">
        <img src="https://img.shields.io/pypi/pyversions/vectorbt" />
    </a>
    <a href="https://hub.docker.com/r/polakowo/vectorbt" title="Docker image version">
        <img src="https://img.shields.io/docker/v/polakowo/vectorbt?sort=semver&label=docker&color=2496ed&logo=docker&logoColor=white" />
    </a>
    <a href="https://hub.docker.com/r/polakowo/vectorbt" title="Docker pulls">
        <img src="https://img.shields.io/docker/pulls/polakowo/vectorbt?label=docker%20pulls&color=2496ed&logo=docker&logoColor=white" />
    </a>
    <a href="https://github.com/polakowo/vectorbt/actions/workflows/tests.yml" title="Tests">
        <img src="https://img.shields.io/github/actions/workflow/status/polakowo/vectorbt/tests.yml?branch=master&label=tests&logo=githubactions&logoColor=white" />
    </a>
    <a href="https://github.com/polakowo/vectorbt/actions/workflows/pypi.yml" title="PyPI release">
        <img src="https://img.shields.io/github/actions/workflow/status/polakowo/vectorbt/pypi.yml?label=release&logo=githubactions&logoColor=white" />
    </a>
    <a href="https://vectorbt.dev/" title="Website">
        <img src="https://img.shields.io/website?url=https%3A%2F%2Fvectorbt.dev%2F&label=website" />
    </a>
    <a href="https://pypi.org/project/vectorbt-rust" title="Rust engine">
        <img src="https://img.shields.io/pypi/v/vectorbt-rust?label=rust%20engine&color=dea584&logo=rust" />
    </a>
    <a href="https://github.com/polakowo/vectorbt/blob/master/LICENSE.md" title="License">
        <img src="https://img.shields.io/badge/license-Fair%20Code-yellow" />
    </a>
</p>

<h3 align="center"><b>Thinks in matrices, backtests at scale.</b></h3>

<p align="center">VectorBT takes a radically different approach to backtesting: instead of looping through bars one strategy at a time, it packs thousands of configurations into NumPy arrays, accelerates the hot path with Numba and Rust, and runs them all at once, turning hours of grid search into seconds.</p>

---

Explore thousands of trading ideas across assets and timeframes, analyze portfolio performance down to individual trades, and visualize results interactively, all in a few lines of code. Built for both human researchers and AI agents, VectorBT combines large-scale experimentation with a mature, battle-tested backtesting stack refined through years of community use.

VectorBT is the open-source community edition of [VectorBT PRO](https://vectorbt.pro/), a state-of-the-art hybrid backtesting library.

## Features

- **Fast, vectorized backtesting** and strategy research built on pandas, NumPy, and Numba
- **Optional Rust engine** for precompiled speed without JIT overhead
- **Pandas-native API** with custom accessors and high-performance operations
- **Flexible broadcasting** for multi-asset analysis and large-scale parameter sweeps
- **Rich indicator ecosystem** with custom indicators and integrations for TA-Lib, Pandas TA, and more
- **Portfolio backtesting** with trade, drawdown, and performance analytics, including QuantStats integration
- **Signal tooling** for generation, ranking, mapping, and distribution analysis
- **Built-in data access** with preprocessing and synthetic data generation
- **Robustness testing** with walk-forward optimization and label generation for ML workflows
- **Interactive visualization** with Plotly, Jupyter widgets, and browser-friendly dashboards
- **Automation tools** for scheduled updates and Telegram notifications
- **Composable Python API** for rapid experimentation and AI agent-driven workflows

## Installation

```sh
pip install -U vectorbt
```

To install the optional Rust engine:

```sh
pip install -U "vectorbt[rust]"
```

To install all optional integrations (TA-Lib, Pandas TA, etc.):

```sh
pip install -U "vectorbt[full]"
```

To install all optional integrations together with the Rust engine:

```sh
pip install -U "vectorbt[full,rust]"
```

## Examples

### Invest $100 in Bitcoin since 2014

```python
import vectorbt as vbt

data = vbt.YFData.download("BTC-USD")
price = data.get("Close")

pf = vbt.Portfolio.from_holding(price, init_cash=100)
print(pf.total_profit())
```

```plaintext
19501.10906763755
```

### Trade a dual-SMA crossover strategy

```python
fast_ma = vbt.MA.run(price, 10)
slow_ma = vbt.MA.run(price, 50)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf = vbt.Portfolio.from_signals(price, entries, exits, init_cash=100)
print(pf.total_profit())
```

```plaintext
34417.80960086067
```

### Generate 1,000 random strategies

```python
import numpy as np

symbols = ["BTC-USD", "ETH-USD"]
data = vbt.YFData.download(symbols, missing_index="drop")
price = data.get("Close")

n = np.random.randint(10, 101, size=1000).tolist()
pf = vbt.Portfolio.from_random_signals(price, n=n, init_cash=100, seed=42)

mean_expectancy = pf.trades.expectancy().groupby(["randnx_n", "symbol"]).mean()
fig = mean_expectancy.unstack().vbt.scatterplot(xaxis_title="randnx_n", yaxis_title="mean_expectancy")
fig.show()
```

![](https://raw.githubusercontent.com/polakowo/vectorbt/master/docs/docs/assets/images/usage_rand_scatter.svg)

### Test 10,000 dual-SMA window combinations

```python
symbols = ["BTC-USD", "ETH-USD", "XRP-USD"]
data = vbt.YFData.download(symbols, missing_index="drop")
price = data.get("Close")

windows = np.arange(2, 101)
fast_ma, slow_ma = vbt.MA.run_combs(price, window=windows, r=2, short_names=["fast", "slow"])
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

pf = vbt.Portfolio.from_signals(price, entries, exits, size=np.inf, fees=0.001, freq="1D")

fig = pf.total_return().vbt.heatmap(
    x_level="fast_window", y_level="slow_window", slider_level="symbol", symmetric=True,
    trace_kwargs=dict(colorbar=dict(title="Total return", tickformat="%")))
fig.show()
```

<img width="750" src="https://raw.githubusercontent.com/polakowo/vectorbt/master/docs/docs/assets/images/usage_dmac_heatmap.gif">

### Inspect any strategy configuration

```python
print(pf[(10, 20, "ETH-USD")].stats())
```

```plaintext
Start                          2017-11-09 00:00:00+00:00
End                            2026-01-03 00:00:00+00:00
Period                                2978 days 00:00:00
Start Value                                        100.0
End Value                                    1604.093789
Total Return [%]                             1504.093789
Benchmark Return [%]                          866.094127
Max Gross Exposure [%]                             100.0
Total Fees Paid                               204.226289
Max Drawdown [%]                               70.734951
Max Drawdown Duration                 1095 days 00:00:00
Total Trades                                          81
Total Closed Trades                                   80
Total Open Trades                                      1
Open Trade PnL                                -14.232533
Win Rate [%]                                       41.25
Best Trade [%]                                120.511071
Worst Trade [%]                               -27.772271
Avg Winning Trade [%]                          27.265519
Avg Losing Trade [%]                           -9.022864
Avg Winning Trade Duration    32 days 20:21:49.090909091
Avg Losing Trade Duration      8 days 16:51:03.829787234
Profit Factor                                   1.275515
Expectancy                                     18.979079
Sharpe Ratio                                    0.861945
Calmar Ratio                                    0.572758
Omega Ratio                                      1.20277
Sortino Ratio                                   1.301377
Name: (10, 20, ETH-USD), dtype: object
```

### Plot any strategy configuration

```python
pf[(10, 20, "ETH-USD")].plot().show()
```

![](https://raw.githubusercontent.com/polakowo/vectorbt/master/docs/docs/assets/images/usage_dmac_portfolio.svg)

### Animate Bollinger Bands across multiple symbols

VectorBT goes beyond backtesting, with tools for financial data analysis and visualization:

```python
symbols = ["BTC-USD", "ETH-USD", "XRP-USD"]
data = vbt.YFData.download(symbols, period="6mo", missing_index="drop")
price = data.get("Close")
bbands = vbt.BBANDS.run(price)

def plot(index, bbands):
    bbands = bbands.loc[index]
    fig = vbt.make_subplots(
        rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.15,
        subplot_titles=("%B", "Bandwidth"))
    fig.update_layout(showlegend=False, width=750, height=400)
    bbands.percent_b.vbt.ts_heatmap(
        trace_kwargs=dict(zmin=0, zmid=0.5, zmax=1, colorscale="Spectral", colorbar=dict(
            y=(fig.layout.yaxis.domain[0] + fig.layout.yaxis.domain[1]) / 2, len=0.5
        )), add_trace_kwargs=dict(row=1, col=1), fig=fig)
    bbands.bandwidth.vbt.ts_heatmap(
        trace_kwargs=dict(colorbar=dict(
            y=(fig.layout.yaxis2.domain[0] + fig.layout.yaxis2.domain[1]) / 2, len=0.5
        )), add_trace_kwargs=dict(row=2, col=1), fig=fig)
    return fig

vbt.save_animation("bbands.gif", bbands.wrapper.index, plot, bbands, delta=90, step=3, fps=3)
```

```plaintext
100%|██████████| 31/31 [00:21<00:00,  1.21it/s]
```

<img width="750" src="https://raw.githubusercontent.com/polakowo/vectorbt/master/docs/docs/assets/images/usage_bbands.gif">

Visit the [website](https://vectorbt.dev/) for more examples, documentation, and guides.

## Example apps

### [Candlestick Patterns](https://github.com/polakowo/vectorbt/blob/master/apps/candlestick-patterns/)

Explore candlestick patterns interactively and backtest their signals with VectorBT.

[![teaser.png](https://raw.githubusercontent.com/polakowo/vectorbt/master/apps/candlestick-patterns/assets/teaser.png)](https://github.com/polakowo/vectorbt/blob/master/apps/candlestick-patterns/)

## Links

* [Website](https://vectorbt.dev/)
* [Docker images](https://hub.docker.com/r/polakowo/vectorbt)
* [Colab notebook](https://colab.research.google.com/drive/1ibqyrf6LPFlzRb6mkPpl3hxqL6ryNBXI?usp=sharing)

## License

This work is [fair-code](http://faircode.io/) distributed under the [Apache 2.0 with Commons Clause](https://github.com/polakowo/vectorbt/blob/master/LICENSE.md) license.

The source code is publicly available, and everyone (individuals and organizations) may use it for free. However, you may not sell products or services that are primarily this software.

If you have questions or want to request a license exception, please [contact the author](mailto:olegpolakow@vectorbt.pro).

Installing optional dependencies may be subject to a more restrictive license.

## Star History

<a href="https://www.star-history.com/?repos=polakowo%2Fvectorbt&type=timeline&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=polakowo/vectorbt&type=timeline&theme=dark&legend=top-left&sealed_token=482an5rek002Q4c3VCaRd7goV3LwR6GP6m56UOqTunBJKoEq19_RkbQldrL-OP4f5XnDtU9tOOTrs-NTtnqFoQoUZJdWPQEQ-eO2q1McxpYu-STLc1fj9tY60p-spkcSQ9bxs7WJkumrqYI1LSc3mBd7CIu2K7IuYNAgv1pYuFJOQaN1yD5p3wWNgcFM" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=polakowo/vectorbt&type=timeline&legend=top-left&sealed_token=482an5rek002Q4c3VCaRd7goV3LwR6GP6m56UOqTunBJKoEq19_RkbQldrL-OP4f5XnDtU9tOOTrs-NTtnqFoQoUZJdWPQEQ-eO2q1McxpYu-STLc1fj9tY60p-spkcSQ9bxs7WJkumrqYI1LSc3mBd7CIu2K7IuYNAgv1pYuFJOQaN1yD5p3wWNgcFM" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=polakowo/vectorbt&type=timeline&legend=top-left&sealed_token=482an5rek002Q4c3VCaRd7goV3LwR6GP6m56UOqTunBJKoEq19_RkbQldrL-OP4f5XnDtU9tOOTrs-NTtnqFoQoUZJdWPQEQ-eO2q1McxpYu-STLc1fj9tY60p-spkcSQ9bxs7WJkumrqYI1LSc3mBd7CIu2K7IuYNAgv1pYuFJOQaN1yD5p3wWNgcFM" />
 </picture>
</a>

## Disclaimer

This software is for educational purposes only. Do not risk money you cannot afford to lose.

Use the software at your own risk. The authors and affiliates assume no responsibility for your trading results.

### Core Implementation Code & Architecture
#### File: `conftest.py`
```python

```

#### File: `tests/__init__.py`
```python

```

#### File: `rust/rustfmt.toml`
```python
max_width = 120
```

#### File: `setup.py`
```python
from setuptools import setup


def main():
    setup()


if __name__ == "__main__":
    main()
```

#### File: `docs/docs/context7.json`
```python
{
  "url": "https://context7.com/websites/vectorbt_dev",
  "public_key": "pk_mUI0GJgI77UfY6eC4BMJT"
}
```

#### File: `vectorbt/_version.py`
```python
# Copyright (c) 2017-2026 Oleg Polakow. All rights reserved.
# This code is licensed under Apache 2.0 with Commons Clause license (see LICENSE.md for details)

__version__ = "1.1.0"
```


==================================================


## [2/3] Repository: raptorbt (`VAULT_IN-QUANT-109_alphabench__raptorbt`)
- **Full Name**: `IN-QUANT-109_alphabench__raptorbt`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# RaptorBT

[![PyPI](https://img.shields.io/pypi/v/raptorbt.svg)](https://pypi.org/project/raptorbt/)
[![Python](https://img.shields.io/pypi/pyversions/raptorbt.svg)](https://pypi.org/project/raptorbt/)
[![Rust](https://img.shields.io/badge/Rust-powered-orange?logo=rust)](https://www.rust-lang.org/)
[![Downloads](https://api.pepy.tech/badge/raptorbt/month)](https://pepy.tech/projects/raptorbt)
[![License](https://img.shields.io/pypi/l/raptorbt.svg)](https://opensource.org/licenses/MIT)
[![Support](https://img.shields.io/badge/Support-the%20project-ff69b4)](https://checkout.dodopayments.com/buy/pdt_0NmIpbPfM2KlwPVgZ6kMX?redirect_url=https%3A%2F%2Fwww.alphabench.in%2Fraptorbt%2Fthanks)

**Blazing-fast backtesting for the modern quant.**

RaptorBT is a high-performance backtesting engine written in Rust with Python bindings via PyO3. It runs single-instrument, basket, pairs, options, spread, multi-strategy, and tick-level backtests over any OHLCV or tick arrays — from any broker, market, or asset class — and returns a full performance report in sub-millisecond time.

<p align="center">
  <strong>~13M bars/sec</strong> · <strong>Sweeps across every core</strong> · <strong>Bit-for-bit deterministic</strong>
</p>

---

### Quick Install

```bash
pip install raptorbt
```

> **Upgrading from 0.6.x or 0.7.x?** Public classes dropped their `Py` prefix in
> 0.7.0 — `PyBacktestConfig` is now `BacktestConfig`, `PyTrade` is `Trade`, and
> so on. The old names resolved with a `DeprecationWarning` through 0.7.x and
> **are removed in 0.8.0**: they now raise `AttributeError`. Rename them, or
> pin `raptorbt<0.8`.
>
> Two other changes alter results. In 0.7.0, `BarAggregator` began honouring
> `brick_size` (Renko backtests through it were wrong) and tick backtests
> stopped truncating at 50 trades by default. In 0.8.0, each leg of a spread
> settles on its own expiry date, so calendar and diagonal spreads are measured
> correctly for the first time; same-expiry structures are unaffected. See the
> [CHANGELOG](CHANGELOG.md#080---2026-08-14).

### 30-Second Example

```python
import numpy as np
import raptorbt

# Configure
config = raptorbt.BacktestConfig(initial_capital=100000, fees=0.001)

# Run backtest
result = raptorbt.run_single_backtest(
    timestamps=timestamps,
    open=open,
    high=high,
    low=low,
    close=close,
    volume=volume,
    entries=entries,
    exits=exits,
    direction=1,
    weight=1.0,
    symbol="AAPL",
    config=config,
)

# Results
print(f"Return: {result.metrics.total_return_pct:.2f}%")
print(f"Sharpe: {result.metrics.sharpe_ratio:.2f}")
```

RaptorBT is open source (MIT) and developed by the [Alphabench](https://alphabench.in) team.

---

## Table of Contents

- [Overview](#overview)
- [Performance](#performance)
- [Class-Based Strategies](#class-based-strategies)
- [Strategy Types](#strategy-types)
- [Metrics](#metrics)
- [Indicators](#indicators)
- [Stop-Loss & Take-Profit](#stop-loss--take-profit)
- [Monte Carlo Portfolio Simulation](#monte-carlo-portfolio-simulation)
- [API Reference](#api-reference)
- [Building from Source](#building-from-source)

---

## Overview

RaptorBT compiles to a single native extension and runs entirely in Rust, so a
full backtest with all 48 metrics finishes in under a millisecond at the bar
counts most strategies use. Measured on an Apple M4 (raptorbt 0.13.2,
Python 3.12):

| Metric                           | RaptorBT      |
| -------------------------------- | ------------- |
| **Compiled engine size**         | 1.75 MB       |
| **Backtest speed (1K bars)**     | ~0.075 ms     |
| **Backtest speed (10K bars)**    | ~0.77 ms      |
| **Backtest speed (50K bars)**    | ~3.85 ms      |
| **Sustained throughput**         | ~13M bars/sec |
| **184-combo sweep, 10 cores**    | 170 ms, 7.7x  |
| **Peak memory, 184-combo sweep** | 56 MB         |

See [Performance](#performance) for the full method and how to reproduce these
numbers on your own hardware.

### Key Features

- **8 Strategy Types**: Single instrument, basket/collective, pairs trading, options, spreads, multi-strategy, tick-level, and shared-capital portfolio
- **Two ways to write a strategy**: precomputed signal arrays (the vectorized fast path), or a `Strategy` class with lifecycle hooks driven by bars, ticks, or a live feed
- **Asset- and broker-agnostic**: Pass NumPy OHLCV or tick arrays from any source — equities, futures, FX, crypto, options — RaptorBT never assumes a market or data vendor
- **Tick-Level Simulation**: Full tick resolution for intraday options momentum, scalping, and microstructure strategies
- **Live-feed ready**: Push events as they arrive with `TickStrategyStream`, and seed a run with positions the account already holds via position adoption
- **Portfolio Construction**: Ledoit-Wolf covariance, a constrained optimizer — long-only by default, long/short with gross and net exposure budgets (v0.6.3) — factor panels with rank-IC validation, risk contributions, and rebalance-cost simulation
- **Parallel Parameter Sweeps**: `batch_single_backtest` runs many signal sets over one price series across every core — 7.7x on ten cores, bit-identical to a serial loop
- **Batch Spread Backtesting**: Run multiple spread backtests in parallel via Rayon with GIL released
- **Monte Carlo Simulation**: Correlated multi-asset forward projection via GBM + Cholesky decomposition
- **48 Metrics**: Sharpe, Sortino, Calmar, Omega, Ulcer Index, Time Under Water, SQN, Payoff Ratio, Recovery Factor, and more
- **Diagnostics that say *why***: return skew and excess kurtosis (is a high Sharpe really a short-vol payoff?), cost-to-gross-profit and breakeven cost multiple (do fees eat the edge, and how much room is left?), average MAE and MFE capture (where should the stop sit, and is the exit giving the move back?)
- **20 Indicator & Tick Functions**: 12 classic technical indicators (SMA, EMA, RSI, MACD, Stochastic, ATR, Bollinger Bands, ADX, VWAP, Supertrend, Rolling Min/Max) plus 8 tick microstructure/feature functions
- **Stop/Target Management**: Fixed, ATR-based, and trailing stops with risk-reward targets
- **Deterministic**: Identical inputs produce bit-for-bit identical results across runs — no JIT compilation variance
- **Native Parallelism**: Rayon-based parallel processing with explicit SIMD optimizations

---

## Performance

### Benchmark Results

Measured on an Apple M4 (10 cores, 24 GB, raptorbt 0.13.2, Python 3.12) with
random-walk price data and an SMA-crossover strategy. Each figure is the fastest
of several hundred `run_single_backtest` repetitions, so it reflects engine time
rather than scheduler noise. Reproduce any row with `uv run python
benches/python/run_all.py` — the harness is in the repo precisely so these are
checkable.

| Data size       | Time     | Throughput   |
| --------------- | -------- | ------------ |
| 1,000 bars      | 0.075 ms | 13M bars/sec |
| 5,000 bars      | 0.38 ms  | 13M bars/sec |
| 10,000 bars     | 0.77 ms  | 13M bars/sec |
| 50,000 bars     | 3.85 ms  | 13M bars/sec |
| 93,750 bars     | 7.19 ms  | 13M bars/sec |
| 1,875,000 bars  | 158 ms   | 12M bars/sec |
| 25,000,000 bars | 1.92 s   | 13M bars/sec |

The 1,875,000-bar row is the one worth dwelling on: that is roughly **twenty
years of Indian one-minute intraday data**, backtested in about a sixth of a
second. Throughput holds between 11M and 13M bars/sec across the whole range,
from a thousand bars to twenty-five million — a spread of about 15%, against a
25,000x change in input size. Scaling is linear: the engine does not fall off a
cliff when the data stops fitting in cache.

Every row runs the full metric set — all 48 fields, including the return-shape
and cost diagnostics added in 0.13.2. Against the published 0.13.1 wheel on this
same harness, small runs are unchanged (0.072 → 0.075 ms at 1,000 bars) and
large ones are faster: **1.875M bars 165 → 158 ms, and 25M bars 2.43 s → 1.92 s,
a 21% improvement**. Trade counts are identical at every size. The large-run
gain is the binding no longer duplicating its input — see **Memory** below.

Other paths, measured the same way:

| Path                                                 | Result                                                           |
| ---------------------------------------------------- | ---------------------------------------------------------------- |
| Tick engine                                          | 107–221M ticks/sec, every tick traversed to the end of the array |
| 500 option spreads in parallel                       | 40,817/sec, 7.6x faster than serial, bit-for-bit identical to it |
| 184-combo sweep, one Python loop                     | 1.51 s wall, 56 MB peak RSS                                      |
| 184-combo sweep, `batch_single_backtest`             | 170 ms, **7.7x faster**, bit-identical to the serial loop        |
| 25M-bar run, peak memory over a 1.25 GB input        | 1.13 GB (was 2.16 GB before the input copy was removed)          |
| Determinism                                          | 20 runs → one SHA-256                                            |
| Compiled engine                                      | 1.75 MB                                                          |
| Metrics per backtest                                 | 48 attributes (31 in `to_dict()`)                                |

The tick row is a range because tick throughput, unlike bar throughput, does
not stay flat: ~197M ticks/sec at 10,000 ticks and ~221M at 100,000, falling to
~164M at a million and 100–130M at ten million as the arrays outgrow cache. The
ten-million row is also the least repeatable — it is the one measurement here
that varies by more than a few percent between runs. Every figure is verified to
traverse to the last tick before it is published: a truncated run would time a
prefix of the array and report an inflated ticks/sec, so the harness asserts the
final trade's exit index lands at the end of the input.

> **Compare within one harness only.** These figures come from
> `benches/python/run_all.py` at 0.13.2. Numbers published against 0.6.4 and
> earlier came from a one-off script that was not kept and are not comparable to
> them — that is why the harness now ships with the code. The `spreads` and
> `sweep` rows are measured standalone (`run_all.py spreads`, `run_all.py
> sweep`): the first competes with Rayon for the same cores, and the second
> reads a whole-process peak-RSS high-water mark that anything running before it
> would inflate.

Timings will vary with your CPU, data, and signal density.

### Memory

The engine reads NumPy's buffers directly rather than copying them, so a run's
peak memory is roughly its input plus the curves it produces, not twice its
input. On a 25-million-bar backtest over a 1.25 GB input, peak RSS is **1.13 GB
above baseline, down from 2.16 GB** — close to exactly the duplicate that is no
longer made. The same change is most of why that run got 21% faster.

Two consequences worth knowing:

- Arrays must be **C-contiguous**, which is what ordinary NumPy code produces.
  A non-contiguous view (a strided slice, a transpose) is rejected rather than
  silently copied — `np.ascontiguousarray` fixes it.
- The arrays must stay alive and unmodified for the duration of the call. That
  is automatic in normal use, since the call holds the GIL.

The tick path and the spread path's premium arrays still copy; converting them
is the same fix and has not been done yet.

### Determinism

RaptorBT is fully deterministic: the same inputs produce bit-for-bit identical
results across runs (no JIT warmup, no nondeterministic reductions). Running the
[Verification Test](#verification-test) five times in a row on this machine
produced the same total return every time, to the last decimal:

```
Total return:           -30.6192%  (seed=42, 500 bars, periodic entries/exits)
Max difference across 5 runs: 0.0000000000%
```

The harness makes the stronger version of this claim: it hashes the full equity
curve and every trade's entry index, exit index and P&L on a 50,000-bar run, and
20 repetitions collapse to a single SHA-256 digest. Not just a stable summary
number — a stable curve, trade for trade.

(The exact return depends on your data and signals — the point is that it does
not change between runs.)

---

## Class-Based Strategies

New in 0.5.0: strategies can be written as event-driven classes instead of
precomputed signal arrays. Subclass `raptorbt.Strategy`, override lifecycle
hooks, and emit order intents; the engine simulates fills and routes events
back into your hooks. Both paths share one execution core, so identical
decisions produce identical results — the class contract is the recommended
way to write new strategies, while the array runners remain the fast path
for vectorized workloads.

```python
import numpy as np
import raptorbt


class SmaCross(raptorbt.Strategy):
    def on_start(self, ctx):
        # Full OHLCV arrays are available for indicator precomputation.
        self.fast = raptorbt.sma(ctx.close, 10)
        self.slow = raptorbt.sma(ctx.close, 30)

    def on_bar(self, ctx):
        i = ctx.idx
        if i == 0 or np.isnan(self.slow[i]) or np.isnan(self.slow[i - 1]):
            return
        crossed_up = self.fast[i] > self.slow[i] and self.fast[i - 1] <= self.slow[i - 1]
        crossed_dn = self.fast[i] < self.slow[i] and self.fast[i - 1] >= self.slow[i - 1]
        if crossed_up and ctx.position is None:
            self.enter()                      # optional: size_frac=, stop_price=, target_price=
        elif crossed_dn and ctx.position is not None:
            self.close_position()

    def on_position_closed(self, ctx, event):
        self.log.info("closed: pnl=%.2f", event.trade.pnl)


result = raptorbt.run_strategy_backtest(
    SmaCross(), timestamps, open_, high, low, close, volume,
    symbol="EXAMPLE", config=raptorbt.BacktestConfig(fees=0.001),
)
print(result.metrics.total_return_pct, len(result.trades()))
```

Hooks: `on_start`, `on_bar`, `on_stop`, `on_order_filled`,
`on_order_rejected`, `on_position_opened`, `on_position_closed`. Inside
`on_bar`, `ctx` provides the current `bar`, `position` snapshot, `equity`,
`cash`, `history(n)`, and `set_stop_price()` / `set_target_price()` for
programmatic exits. Decision logic must only read array values at `ctx.idx`
or earlier — indexing past the current bar reads the future.

Engine-level stop/target/sizing configuration (`BacktestConfig`,
`InstrumentConfig`) applies to both paths. `run_strategy_backtest` returns
the same `BacktestResult` as `run_single_backtest`. For advanced drivers
(live feeds, custom loops), `KernelSession` exposes the per-bar engine
step directly.

Note: one Python hook call per bar makes the class path slower than the
array path — fine for typical bar counts, but prefer arrays for large
parameter sweeps.

### Instrument Definitions

New in 0.5.0: `InstrumentSpec` describes the market being traded — tick
size, lot size, contract multiplier, expiry — separately from the per-run
allocation knobs in `InstrumentConfig`. Attach one to a class-based run
via `run_strategy_backtest(..., instrument=...)` (or directly on
`KernelSession`):

```python
import raptorbt

# NIFTY monthly future: 50-unit lots, expiry settlement at the contract's
# expiration timestamp, entries refused before activation / after expiry.
fut = raptorbt.InstrumentSpec.futures_contract(
    "NIFTY24AUGFUT",
    expiration_ns=1724839200_000_000_000,
    lot_size=50.0,
    price_increment=0.05,
    underlying="NIFTY",
)

result = raptorbt.run_strategy_backtest(
    MyStrategy, ts, o, h, l, c, v, instrument=fut,
)
```

Constructors: `equity`, `futures_contract`, `perpetual`, `option` (vanilla
and binary; settles to intrinsic value when an underlying price is known),
`currency_pair`, and `index` (non-tradable reference). With a spec attached
the engine:

- scales notional by the contract `multiplier` — sizing, cash, PnL, and
  value-based fees charge on `price * size * multiplier`, while
  per-share/per-contract fee models keep charging per contract;
- floors sizes to `lot_size` / `size_increment` (an explicit
  `InstrumentConfig.lot_size` still wins — it is the per-run override);
- rounds engine-derived stop/target prices onto the `price_increment` grid,
  conservatively (never in the strategy's favor);
- force-settles open positions at expiry (`Settlement` exit reason) and
  rejects entries outside the activation/expiration window.

Without a spec, behavior is unchanged — existing results reproduce
bit-for-bit. `margin_init`/`margin_maint` feed the margin account layer
(see *Margin accounts* below); `maker_fee`/`taker_fee` are carried for fee
models that distinguish liquidity roles.

Since 0.12.0 an option spec can also model the deposit an exchange blocks
against a **sold** option: `InstrumentSpec.option(..., span_pct=0.0975,
exposure_pct=0.02)` reserves `(span_pct + exposure_pct) × strike ×
multiplier` per contract instead of the premium, so a book too small to
carry the deposit books no trade and reports `InsufficientMargin`. Both
default to `0.0` (premium-funded, as before); bought options always stay
funded at their premium. Since 0.12.1, sold legs that share an `underlying`
and expiry are re-priced as one position group once they are open together
— a straddle pays its scenario deposit once, a vertical or condor pays
exposure plus its width — so a hedged book keeps the capital a real account
would. A new sold leg still sizes on its naked deposit; the group benefit
lands after the leg is on.

### Choosing a side

New in 0.6.0. `enter()` opens in the session's configured `direction`, as it
always has. To decide the side in code, call `enter_long()` / `enter_short()`
(or `enter(side="buy"/"sell")`) — they take the same arguments and ignore the
configured direction, so one run can hold long and short legs and a leg can
flip side once it is flat:

```python
class CrossSectional(raptorbt.Strategy):
    def on_bar(self, ctx):
        if ctx.position is not None:
            self.close_position()      # flat before flipping
            return
        if ctx.symbol in winners:
            self.enter_long(size_frac=0.1)
        elif ctx.symbol in losers:
            self.enter_short(size_frac=0.1)
```

Under the default netting policy an order's side is authoritative for
_opening_: with no position it opens in that side, while an order opposing an
open position closes it (so bracket legs and take-profits behave as before).
Mark an order `reduce_only` to guarantee it can only ever close.

### Typed Orders

New in 0.5.0: alongside the `enter()`/`close_position()` sugar, strategies
can submit typed orders that rest across bars and report a full lifecycle:

```python
from raptorbt.strategy import orders

class Breakout(raptorbt.Strategy):
    def on_bar(self, ctx):
        if ctx.idx == 20 and ctx.position is None:
            # Buy stop above the market, protective stop attached.
            self.oid = self.submit_order(orders.StopMarket(
                side="buy",
                trigger=float(ctx.high[:20].max()),
                size_frac=0.5,
                stop_price=float(ctx.close[ctx.idx] * 0.97),
                tif="day",
            ))
        if ctx.position is not None:
            self.submit_order(orders.Limit(side="sell", price=ctx.position.entry_price * 1.1))
```

- **Kinds**: `orders.Market`, `orders.Limit` (with `post_only=`),
  `orders.StopMarket`, `orders.StopLimit` (trigger fires, then rests as a
  limit from the next bar), `orders.MarketIfTouched` / `orders.LimitIfTouched`
  (favorable-touch triggers — a buy fires when price _falls_ to the
  trigger), `orders.MarketToLimit` (fills at the next bar's open), and
  `orders.TrailingStopMarket` / `orders.TrailingStopLimit` (trigger trails
  the running favorable extreme; `offset_kind` is `"price"`, `"bps"`, or
  `"ticks"` — ticks need an instrument `price_increment`).
- **Time-in-force**: `gtc` (default), `day` (UTC-date rollover), `gtd`
  (with `expire_ns`), `ioc`, `fok`, plus `at_open` / `at_close` for market
  orders queued to a bar phase.
- **Flags**: `post_only` (limit rejects if marketable at its first resting
  open), `reduce_only` (a fill may never increase exposure).
- **Brackets**: `self.submit_bracket(entry, stop_trigger=…, target_price=…,
  stop_limit_price=None)` — the protective legs are held until the entry
  fills (one-triggers-other), then linked one-cancels-other: the first leg
  to fill cancels its sibling, and both die if the entry never fills.
  Generic linkage: `submit_order(order, parent=other_id)` and
  `self.link_oco(id_a, id_b, …)`. One-updates-other reduces to
  one-cancels-other while fills are all-or-nothing (partial fills arrive
  with book depth). Netting policy only — under hedging every order opens,
  so protect positions with per-position `stop_price`/`target_price`
  attachments instead.
- **Sizing**: `units=` (explicit contracts; refused if it exceeds available
  capital) or `size_frac=` (fraction of capital, resolved at fill time);
  omit both on a closing-side order to close the full position.
- **Semantics**: market orders fill on the submission bar at the configured
  fill-price model — the same contract as `enter()`. Resting orders begin
  matching on the _next_ bar (an order cannot rest into a bar that had
  already closed), with gap-throughs filling at the open.
- **Lifecycle hooks**: `on_order_accepted`, `on_order_triggered`,
  `on_order_filled`, `on_order_canceled`, `on_order_expired`,
  `on_order_rejected`, plus catch-all `on_order_event`. Events carry
  `client_order_id` (deterministic `"{order_id_tag}-{seq}"`).
- **Management**: `self.cancel_order(client_id)`,
  `self.cancel_all_orders()`, `self.modify_order(client_id, limit_price=…,
  trigger_price=…, units=…)`.
- Order-driven exits report `exit_reason == "Order"` on the trade record.
  One position at a time: an opening order while a position is open rejects
  with `"position_open"` (independent concurrent positions arrive in a
  later 0.5.x release).

The signal-array runners do not interact with the order book and are
unaffected.

### Bar Aggregation and Multi-Timeframe Strategies

New in 0.5.0. Streaming and batch aggregation of bars (and raw ticks) into
coarser bars — time (`"ms"`/`"s"`/`"m"`/`"h"`/`"d"`/`"w"`), `"tick"`,
`"volume"`, and `"value"` units. Time bars use left-open epoch-aligned
windows and are stamped with the window-_end_ timestamp, so a bar labeled
`t` contains only data strictly before `t` — no look-ahead by construction.
Beyond time, tick, volume and value windows, two families sample on
something other than the clock:

**Renko** (`"renko"`) emits a brick per full brick-height price move and
ignores time and volume entirely — a quiet hour produces nothing, a fast
move produces several bricks at once. Set the height with `brick_size`;
without it, `step` reads as whole price units. Because one record can
complete several bricks, `push` returns only the first and the rest must be
drained:

```python
agg = raptorbt.BarAggregator(1, "renko", brick_size=0.05)
bar = agg.push_trade(ts, price, size)
while bar is not None:
    handle(bar)
    bar = agg.next_pending()      # drain, or bricks are silently lost
```

Bricks carry no wicks, and a partial brick is discarded at end of data
rather than flushed — an incomplete brick is not a brick.

**Signed-flow bars** (`"{tick,volume,value}_imbalance"` and
`"{tick,volume,value}_runs"`) sample by order-flow direction. _Imbalance_
closes on net signed flow, so balanced two-sided trading never closes a bar
however heavy it is; _runs_ closes on the larger one-sided accumulation, so
the same tape does close bars. `step` is the threshold — fixed, rather than
the adaptive estimate in the literature, so runs stay reproducible.

Direction comes from the buy/sell quantity deltas when you supply them
(`bars_from_ticks`), and otherwise from the tick rule, which is what lets
these units work over plain OHLC bars.

```python
# Batch: 1-minute bars -> 5-minute bars (or ticks -> bars).
ts5, o5, h5, l5, c5, v5 = raptorbt.aggregate_bars(ts, o, h, l, c, v, 5, "m")
bts, bo, bh, bl, bc, bv = raptorbt.bars_from_ticks(ts, ltp, buys, sells, 1000, "volume")
# Signed flow: close a bar every 10,000 shares of net buying or selling.
its = raptorbt.bars_from_ticks(ts, ltp, buys, sells, 10_000, "volume_imbalance")

# In a strategy: a 5-minute trend filter gating 1-minute entries.
class TrendGated(raptorbt.Strategy):
    def on_start(self, ctx):
        self.h5 = self.subscribe_bars(5, "m")
        self.trend_up = False

    def on_composite_bar(self, ctx, bar):   # fires when a 5m bar completes
        self.trend_up = bar.close > bar.open

    def on_bar(self, ctx):                  # every 1m bar
        if self.trend_up and ctx.position is None:
            self.enter()
```

`on_composite_bar` dispatches _before_ the `on_bar` of the primary bar that
completed
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `src/instruments/mod.rs`
```python
//! Instrument market definitions.

pub mod spec;

pub use spec::{InstrumentKind, InstrumentSpec, OptionRight};
```

#### File: `rustfmt.toml`
```python
edition = "2021"
max_width = 100
use_small_heuristics = "Max"
# Note: imports_granularity and group_imports require nightly Rust
# imports_granularity = "Module"
# group_imports = "StdExternalCrate"
```

#### File: `src/python/mod.rs`
```python
//! Python bindings for RaptorBT.

pub mod bindings;
pub mod data_bindings;
pub mod indicator_bindings;
pub mod instrument_bindings;
pub mod numpy_bridge;
pub mod portfolio_bindings;
pub mod session_bindings;
pub mod strategy_bindings;
```

#### File: `src/core/mod.rs`
```python
//! Core types and utilities for RaptorBT.

pub mod error;
pub mod session;
pub mod timeseries;
pub mod types;

pub use error::{RaptorError, Result};
pub use session::{SessionConfig, SessionTracker};
pub use timeseries::TimeSeries;
pub use types::*;
```

#### File: `src/signals/mod.rs`
```python
//! Signal processing for RaptorBT.
//!

pub mod processor;
pub mod synchronizer;
pub mod tick_signals;

pub use processor::SignalProcessor;
pub use synchronizer::{SignalSynchronizer, SyncMode};
pub use tick_signals::{tick_momentum_entry, tick_momentum_exit};
```

#### File: `src/metrics/mod.rs`
```python
//! Performance metrics for RaptorBT.

pub mod annualization;
pub mod drawdown;
pub mod streaming;
pub mod trade_stats;

pub use annualization::{elapsed_years, infer_periods_per_year, resolve_periods_per_year};
pub use drawdown::DrawdownTracker;
pub use streaming::StreamingMetrics;
pub use trade_stats::TradeStatistics;
```


==================================================


## [3/3] Repository: Clairvoyant (`WHEEL_Clairvoyant`)
- **Full Name**: `Clairvoyant`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
## Deprecated

This project is no longer maintained.

### Core Implementation Code & Architecture
#### File: `clairvoyant/helpers.py`
```python
def change(d1, d2):
    return (d2-d1)/d1

def profit(capital, multiplier):
    return capital*(multiplier+1.0)-capital
```

#### File: `tests/testexchange.py`
```python
import unittest

# Local imports
import sys
sys.path.append("../.")
from clairvoyant import exchange, helpers

class Methods(unittest.TestCase):

    def test_errors(self):
        a = exchange.Account(1000)
        self.assertRaises(ValueError, a.EnterPosition, 'Long',  2000, 10)
        self.assertRaises(ValueError, a.EnterPosition, 'Long',  -500, 10)       
        self.assertRaises(ValueError, a.EnterPosition, 'Long', 500, -10)
        # Enter valid position
        a.EnterPosition('Long', 250, 10)
        a.EnterPosition('Short', 250, 10)
        Long  = a.Positions[0]
        Short = a.Positions[1]
        self.assertRaises(ValueError, a.ClosePosition, Long, 0.5, -20)
        self.assertRaises(ValueError, a.ClosePosition, Long, 1.01, 20)
        self.assertRaises(ValueError, a.ClosePosition, Long, -0.5, 20)
        self.assertRaises(ValueError, a.ClosePosition, Short, 1.01, 20)
        self.assertRaises(ValueError, a.ClosePosition, Short, -0.5, 20)

    def test_long(self):
        a = exchange.Account(1000)
        # Win on a long
        a.EnterPosition('Long', 500, 10)
        a.EnterPosition('Long', 500, 10)
        self.assertEqual(a.BuyingPower, 0)
        self.assertEqual(a.TotalValue(10), 1000)
        L0 = a.Positions[0]
        L1 = a.Positions[1]
        a.ClosePosition(L0, 0.5, 20)
        a.ClosePosition(L1, 0.5, 20)
        self.assertEqual(a.BuyingPower, 1000)
        self.assertEqual(a.TotalValue(20), 2000)
        a.ClosePosition(L0, 0.5, 40)
        a.ClosePosition(L1, 0.5, 40)
        self.assertEqual(a.BuyingPower, 2000)
        self.assertEqual(a.TotalValue(40), 3000)
        # Lose on a long
        a.EnterPosition('Long', 1000, 50)
        L2 = a.Positions[2]
        a.ClosePosition(L2, 0.5, 25)
        self.assertEqual(a.BuyingPower, 1250)
        self.assertEqual(a.TotalValue(25), 2125)

    def test_short(self):
        a = exchange.Account(1000)
        # Win on a short        
        a.EnterPosition('Short', 500, 10)
        a.EnterPosition('Short', 500, 10)
        self.assertEqual(a.BuyingPower, 0)
        self.assertEqual(a.TotalValue(10), 1000)
        S0 = a.Positions[0]
        S1 = a.Positions[1]
        a.ClosePosition(S0, 0.5, 5)
        a.ClosePosition(S1, 0.5, 5)
        self.assertEqual(a.BuyingPower, 750)
        self.assertEqual(a.TotalValue(5), 1500)
        a.ClosePosition(S0, 0.5, 2.5)
        a.ClosePosition(S1, 0.5, 2.5)
        self.assertEqual(a.BuyingPower, 1187.5)
        self.assertEqual(a.TotalValue(2.5), 1625)
        # Lose on a short   
        a.EnterPosition('Short', 1000, 2)
        S2 = a.Positions[2]
        a.ClosePosition(S2, 0.5, 4)
        self.assertEqual(a.BuyingPower, 187.5)
        self.assertEqual(a.TotalValue(4), 587.5)

    def test_both(self):
        a = exchange.Account(1000)
        a.EnterPosition('Long',  200, 20)
        a.EnterPosition('Short', 250, 25)
        self.assertEqual(a.BuyingPower, 550)
        self.assertEqual(a.TotalValue(25), 1050)
        Long  = a.Positions[0]
        Short = a.Positions[1]
        a.ClosePosition(Long,  0.5, 40)
        a.ClosePosition(Short, 0.5, 12.5)
        self.assertEqual(a.BuyingPower, 937.5)
        self.assertEqual(a.TotalValue(12.5), 1187.5)
        a.ClosePosition(Long,  1.0, 50)
        a.ClosePosition(Short, 1.0, 50)
        self.assertEqual(a.BuyingPower, 1187.5)
        self.assertEqual(a.TotalValue(100), 1187.5)

    def test_decimals(self):
        # Long with decimals
        a = exchange.Account(2)
        a.EnterPosition('Long', 1, 0.00000001)
        self.assertEqual(a.TotalValue(0.00000002), 3)
        a.ClosePosition(a.Positions[0], 1, 0.00000002)
        self.assertEqual(a.BuyingPower, 3)
        # Short with decimals 
        a = exchange.Account(2)
        a.EnterPosition('Short', 1, 0.00000002)
        self.assertEqual(a.TotalValue(0.00000001), 2.5)
        a.ClosePosition(a.Positions[0], 1, 0.00000001)
        self.assertEqual(a.BuyingPower, 2.5)

if __name__ == '__main__':
    unittest.main()
```

#### File: `clairvoyant/exchange.py`
```python
import copy

class OpenedTrade():
    def __init__(self, Type, Date):
        self.Type = Type
        self.Date = Date    
    def __str__(self):
        return "{0}\n{1}".format(self.Type, self.Date)

class ClosedTrade(OpenedTrade):
    def __init__(self, Type, Date, Shares, Entry, Exit):
        super().__init__(Type, Date)
        self.Shares = float(Shares)
        self.Entry  = float(Entry)
        self.Exit   = float(Exit)
    def __str__(self):
        return "{0}\n{1}\n{2}\n{3}\n{4}".format(self.Type, self.Date, self.Shares, self.Entry, self.Exit)

class Position:
    def __init__(self, No, EntryPrice, Shares, ExitPrice=0, StopLoss=0):
        self.No         = No
        self.Type       = "None"
        self.EntryPrice = float(EntryPrice)
        self.Shares     = float(Shares)
        self.ExitPrice  = float(ExitPrice)
        self.StopLoss   = float(StopLoss)   
    
    def Show(self):
        print("No. {0}".format(self.No))
        print("Type:   {0}".format(self.Type))
        print("Entry:  {0}".format(self.EntryPrice))
        print("Shares: {0}".format(self.Shares))
        print("Exit:   {0}".format(self.ExitPrice))
        print("Stop:   {0}\n".format(self.StopLoss))

class LongPosition(Position):
    def __init__(self, No, EntryPrice, Shares, ExitPrice=0, StopLoss=0):
        super().__init__(No, EntryPrice, Shares, ExitPrice, StopLoss)
        self.Type = 'Long'

    def Close(self, Percent, CurrentPrice):
        Shares = self.Shares
        self.Shares *= 1.0-Percent
        return Shares*Percent*CurrentPrice

class ShortPosition(Position):
    def __init__(self, No, EntryPrice, Shares, ExitPrice=0, StopLoss=0):
        super().__init__(No, EntryPrice, Shares, ExitPrice, StopLoss)
        self.Type = 'Short' 

    def Close(self, Percent, CurrentPrice):
        Entry = self.Shares*Percent*self.EntryPrice
        Exit = self.Shares*Percent*CurrentPrice
        self.Shares *= 1.0-Percent
        if Entry-Exit+Entry <= 0: return 0
        else: return Entry-Exit+Entry

class Account():
    def __init__(self, InitialCapital):
        self.InitialCapital = float(InitialCapital)
        self.BuyingPower    = float(InitialCapital)
        self.No             = 0
        self.Date           = None
        self.Equity         = []
        self.Positions      = []
        self.OpenedTrades   = []
        self.ClosedTrades   = []

    def EnterPosition(self, Type, EntryCapital, EntryPrice, ExitPrice=0, StopLoss=0):
        EntryCapital = float(EntryCapital)
        if EntryCapital < 0: raise ValueError("Error: Entry capital must be positive")          
        elif EntryPrice < 0: raise ValueError("Error: Entry price cannot be negative.")
        elif self.BuyingPower < EntryCapital: raise ValueError("Error: Not enough buying power to enter position")          
        else: 
            self.BuyingPower -= EntryCapital
            Shares = EntryCapital/EntryPrice 
            if Type == 'Long': self.Positions.append(LongPosition(self.No, EntryPrice, Shares, ExitPrice, StopLoss))
            elif Type == 'Short': self.Positions.append(ShortPosition(self.No, EntryPrice, Shares, ExitPrice, StopLoss))    
            else: raise TypeError("Error: Invalid position type.")

            self.OpenedTrades.append(OpenedTrade(Type, self.Date))
            self.No += 1    

    def ClosePosition(self, Position, Percent, CurrentPrice):
        if Percent > 1 or Percent < 0: 
            raise ValueError("Error: Percent must range between 0-1.")
        elif CurrentPrice < 0:
            raise ValueError("Error: Current price cannot be negative.")                
        else: 
            self.ClosedTrades.append(ClosedTrade(Position.Type, self.Date, Position.Shares*Percent, Position.EntryPrice, CurrentPrice))
            self.BuyingPower += Position.Close(Percent, CurrentPrice)

    def PurgePositions(self):
        self.Positions = [p for p in self.Positions if p.Shares > 0]        
            
    def ShowPositions(self):
        for p in self.Positions: p.Show()

    def TotalValue(self, CurrentPrice):
        Temporary = copy.deepcopy(self)
        for Position in Temporary.Positions:
            Temporary.ClosePosition(Position, 1.0, CurrentPrice)
        return Temporary.BuyingPower
```

#### File: `clairvoyant/engine.py`
```python
from sklearn.svm           import SVC
from sklearn.preprocessing import RobustScaler
from matplotlib.colors     import ListedColormap
from matplotlib            import pyplot
from bokeh.plotting        import output_file, figure, show
from numpy                 import vstack, hstack, meshgrid, arange, c_, where

# Local imports
import sys
sys.path.append("..")
from clairvoyant import exchange, helpers

class Model:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.svc = SVC(probability=True, **kwargs)

    def fit(self, X, y):
        self.XX = vstack(X)
        self.yy = hstack(y)
        self.scaler = RobustScaler().fit(self.XX)
        self.svc.fit(self.scaler.transform(self.XX), self.yy)

    def predict(self, Xs):
        prediction = self.svc.predict_proba(self.scaler.transform([Xs]))[0]
        return prediction[0], prediction[1] # Negative, Positive

class Engine:
    def __init__(self, features, trainStr, trainEnd, testStr, testEnd, buyThreshold=0.65, sellThreshold=0.65, continueTraining=False):
        self.model            = None
        self.account          = None
        self.features         = features
        self.trainStr         = trainStr
        self.trainEnd         = trainEnd
        self.testStr          = testStr
        self.testEnd          = testEnd
        self.buyThreshold     = buyThreshold
        self.sellThreshold    = sellThreshold
        self.continueTraining = continueTraining

    def start(self, data, capital=None, logic=None, simulation=False, **kwargs):
        self.data = data
        self.model = Model(**kwargs)

        # ====================== #
        #    Initial Training    #
        # ====================== #
        
        X, y = [], []                                   
        for i in range(self.trainStr, self.trainEnd+1):

            Xs = [data.iloc[i][var] for var in self.features]
            X.append(Xs)                             
            
            # Find the stock price movement for day 2
            y1 = helpers.change(data.iloc[i+1].open, data.iloc[i+1].close)
            if y1 > 0: y.append(1)  # If it went up, classify as 1
            else:      y.append(-1) # If it went down, classify as -1
        
        self.model.fit(X, y)

        # ====================== #
        #         Testing        #
        # ====================== #       
        
        if simulation:
            self.account = exchange.Account(capital)

        for i in range(self.testStr, self.testEnd):
            
            # ==================================== #
            #  DAY 1 @ 8:00 PM | Markets closed    #
            #  Make prediction for DAY 2           #
            #  Update Buy/Sell count (or neither)  #
            # ==================================== #        
            
            Xs = [data.iloc[i][var] for var in self.features]
            neg, pos = self.model.predict(Xs)
            
            if pos >= self.buyThreshold:  # Positive confidence >= buyThreshold
                prediction =  1 
                confidence = pos
            
            elif neg >= self.sellThreshold: # If negative confidence >= sellThreshold
                prediction = -1
                confidence = neg

            else: prediction = confidence = 0
            
            if simulation:
                # Update account variables
                self.account.Date = data.iloc[i]['date']
                self.account.Equity.append(self.account.TotalValue(data.iloc[i]['close']))

                # Execute trading logic
                logic(self.account, data.iloc[i], prediction, confidence)

                # Cleanup empty positions
                self.account.PurgePositions()

            if not simulation:
                # ==================================== #
                #  DAY 2 @ 4:30 PM | Markets closed    #
                #  Analyze results from DAY 2          #
                #  Record if prediction was correct    #
                # ==================================== #
                
                # Case 1/2: Prediction is positive (buy), next day performance is/isn't positive 
                if prediction == 1:
                    self.totalBuys += 1
                    if helpers.change(data.iloc[i+1].open, data.iloc[i+1].close) > 0:
                        self.correctBuys += 1
                
                # Case 3/4: Prediction is negative (sell), next day performance is/isn't negative
                elif prediction == -1:
                    self.totalSells += 1
                    if helpers.change(data.iloc[i+1].open, data.iloc[i+1].close) < 0:
                        self.correctSells += 1
            
            # ====================== #
            #     Update Model       #
            #     if specified       #
            # ====================== #
            
            if self.continueTraining:
                X.append(Xs)     
                
                if change(data, i+1) > 0: y.append(1)
                else:                     y.append(-1)
                
                self.model.fit(X, y)

    def conditions(self):
        if self.model == None:
            print("Error: Please start model to generate conditions")
            return

        print("------------ Data Features ------------\n")
        for i, var in enumerate(self.features):
            print("X{0}: {1}".format(i+1, var))
        print("\n---------------------------------------\n")

        print("----------- Model Arguments -----------\n")
        for kwarg in self.model.kwargs: 
            print("{0}: {1}".format(kwarg, self.model.kwargs[kwarg]))
        print("\n---------------------------------------\n")

        print("---------  Engine Conditions ----------\n")
        print("Training: {0} -- {1}".format(self.data.iloc[self.trainStr].date, self.data.iloc[self.trainEnd].date))
        print("Testing:  {0} -- {1}".format(self.data.iloc[self.testStr].date, self.data.iloc[self.testEnd].date))
        print("Buy Threshold: {0}%".format(self.buyThreshold*100))
        print("Sell Threshold: {0}%".format(self.sellThreshold*100))
        print("Continued Training: {0}".format(self.continueTraining))
        print("\n---------------------------------------\n")

    def visualize(self, name, width=5, height=5, stepsize=0.02):
        if len(self.features) != 2:
            print("Error: Plotting is restricted to 2 dimensions")
            return
        if self.model == None:
            print("Error: Please start model before visualizing")
            return
            
        X, y = self.model.XX, self.model.yy # Retrieve previous XX and yy                                      
        X = self.model.scaler.transform(X)  # Normalize X values
        self.model.svc.fit(X, y)            # Refit model
        
        x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5    
        y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5     
        xx, yy = meshgrid(arange(x_min, x_max, stepsize), arange(y_min, y_max, stepsize))
        
        pyplot.figure(figsize=(width, height))
        cm = pyplot.cm.RdBu  # Red/Blue gradients
        rb = ListedColormap(['#FF312E', '#6E8894']) # Red = 0 (Negative) / Blue = 1 (Positve)
        Z = self.model.svc.decision_function(c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        
        Axes = pyplot.subplot(1,1,1)
        Axes.set_title(name)
        Axes.contourf(xx, yy, Z, cmap=cm, alpha=0.75)
        Axes.scatter(X[:, 0], X[:, 1], s=20, c=y, cmap=rb, edgecolors='black') 
        Axes.set_xlim(xx.min(), xx.max())
        Axes.set_ylim(yy.min(), yy.max())
        pyplot.savefig("{0}.png".format(name))

class Backtest(Engine):
    def __init__(self, features, trainStr, trainEnd, testStr, testEnd, buyThreshold=0.65, sellThreshold=0.65, continueTraining=False):
        Engine.__init__(self, features, trainStr, trainEnd, testStr, testEnd, buyThreshold, sellThreshold, continueTraining)

        # Statistics
        self.totalBuys    = 0
        self.correctBuys  = 0
        self.totalSells   = 0
        self.correctSells = 0
        
    def start(self, data, **kwargs):
        Engine.start(self, data, **kwargs)
                        
    def buyStats(self):
        try: return round((float(self.correctBuys)/self.totalBuys)*100,2)
        except ZeroDivisionError: return float(0)
        
    def sellStats(self):
        try: return round((float(self.correctSells)/self.totalSells)*100,2)
        except ZeroDivisionError: return float(0)

    def statistics(self):        
        if self.model == None:
            print("Error: Please start model to generate statistics")
            return

        print("------------- Statistics --------------\n")
        print("Total Buys: {0}".format(self.totalBuys))
        print("Buy Accuracy: {0}%".format(self.buyStats()))
        print("Total Sells: {0}".format(self.totalSells))
        print("Sell Accuracy: {0}%".format(self.sellStats()))
        print("\n---------------------------------------\n")

class Simulation(Engine):
    def __init__(self, features, trainStr, trainEnd, testStr, testEnd, buyThreshold=0.65, sellThreshold=0.65, continueTraining=False):
        Engine.__init__(self, features, trainStr, trainEnd, testStr, testEnd, buyThreshold, sellThreshold, continueTraining)

    def start(self, data, capital, logic, **kwargs):
        Engine.start(self, data, capital=capital, logic=logic, simulation=True, **kwargs)        

    def statistics(self):          
        print("------------- Statistics --------------\n")
        BeginPrice = self.data.iloc[self.testStr]['open']
        FinalPrice = self.data.iloc[self.testEnd]['close']

        percentchange = helpers.change(BeginPrice, FinalPrice)
        print("Buy and Hold : {0}%".format(round(percentchange*100, 2)))
        print("Net Profit   : {0}".format(round(helpers.profit(self.account.InitialCapital, percentchange), 2)))
        
        percentchange = helpers.change(self.account.InitialCapital, self.account.TotalValue(FinalPrice))
        print("Strategy     : {0}%".format(round(percentchange*100, 2)))
        print("Net Profit   : {0}".format(round(helpers.profit(self.account.InitialCapital, percentchange), 2)))

        Longs  = len([T for T in self.account.OpenedTrades if T.Type == 'Long'])
        Sells  = len([T for T in self.account.ClosedTrades if T.Type == 'Long'])
        Shorts = len([T for T in self.account.OpenedTrades if T.Type == 'Short'])
        Covers = len([T for T in self.account.ClosedTrades if T.Type == 'Short'])

        print("Longs        : {0}".format(Longs))
        print("Sells        : {0}".format(Sells))
        print("Shorts       : {0}".format(Shorts))
        print("Covers       : {0}".format(Covers))
        print("--------------------")
        print("Total Trades : {0}".format(Longs+Sells+Shorts+Covers))
        print("\n---------------------------------------\n")

    def chart(self, name):
        output_file("{0}.html".format(name), title="Equity Curve")
        p = figure(x_axis_type="datetime", plot_width=1000, plot_height=400, title="Equity Curve")
        p.grid.grid_line_alpha = 0.3
        p.xaxis.axis_label = 'Date'
        p.yaxis.axis_label = 'Equity'
        
        Shares = self.account.InitialCapital/self.data.iloc[self.testStr].open
        BaseEquity = [Price*Shares for Price in self.data[self.testStr:self.testEnd].open]      
        
        p.line(self.data[self.testStr:self.testEnd].date, BaseEquity, color='#CAD8DE', legend='Buy and Hold')
        p.line(self.data[self.testStr:self.testEnd].date, self.account.Equity, color='#49516F', legend='Strategy')
        p.legend.location = "top_left"
        show(p)
```


==================================================
