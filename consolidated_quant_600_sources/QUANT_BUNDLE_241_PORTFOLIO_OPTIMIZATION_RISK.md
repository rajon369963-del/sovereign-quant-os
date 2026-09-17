# ⚡ [QUANT-SOURCE-241] Consolidated Quant & Algo Trading Repositories
**Category**: `PORTFOLIO_OPTIMIZATION_RISK` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_241_PORTFOLIO_OPTIMIZATION_RISK.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: okama (`PHASE4-QUANT-171`)
- **Full Name**: `PHASE4-QUANT-171_mbk-dev__okama`
- **Description**: Investment portfolio and stocks analyzing tools for Python with free historical data
- **GitHub Stars**: 273
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<p align="center">
  <img src="https://raw.githubusercontent.com/mbk-dev/okama/images/images/Okama2.jpg" alt="okama — investment portfolio analysis and optimization library" width="600">
</p>

# Okama

[![Documentation Status](https://img.shields.io/readthedocs/okama.svg?style=popout)](https://okama.readthedocs.io/)
[![Python](https://img.shields.io/pypi/pyversions/okama.svg)](https://www.python.org/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/okama.svg)](https://pypi.org/project/okama/)
[![Downloads](https://static.pepy.tech/badge/okama)](https://pepy.tech/project/okama)
[![Coverage](https://coveralls.io/repos/github/mbk-dev/okama/badge.svg?branch=master)](https://coveralls.io/github/mbk-dev/okama?branch=master)
[![License](https://img.shields.io/pypi/l/okama.svg)](https://opensource.org/licenses/MIT)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mbk-dev/okama/blob/master/examples/01%20howto.ipynb)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

_okama_ is a Python library for investment portfolio analysis and optimization. It applies concepts commonly used in quantitative finance.

_okama_ provides access to **free** end-of-day historical market data and macroeconomic indicators through an API.

> ...entities should not be multiplied without necessity
>
> -- <cite>William of Ockham (c. 1287–1347)</cite>

## Table of contents

- [Okama main features](#okama-main-features)
- [Financial data and macroeconomic indicators](#financial-data-and-macroeconomic-indicators)
  - [End of day historical data](#end-of-day-historical-data)
  - [Currencies](#currencies)
  - [Macroeconomic indicators](#macroeconomic-indicators)
  - [Other historical data](#other-historical-data)
- [Installation](#installation)
- [Getting started](#getting-started)
- [Examples](#examples)
- [Documentation](#documentation)
- [Financial Widgets](#financial-widgets)
- [MCP server](#mcp-server)
- [Roadmap](#roadmap)
- [Contributing to okama](#contributing-to-okama)
- [Communication](#communication)

## Okama main features

- Investment portfolio constrained Markowitz Mean-Variance Analysis (MVA) and optimization
- Rebalanced portfolio optimization with constraints (multi-period Efficient Frontier)
- Advanced rebalancing strategies: Rebalancing-bands (threshold-based), Calendar-based or hybrid
- Investment portfolios with complex contributions / withdrawals cash flows (DCF)
- Money-weighted internal rate of return (IRR/MWRR) for portfolio cash flows — on historical data and across Monte Carlo forecast paths
- Monte Carlo Simulations for financial assets and investment portfolios, reproducible with a random `seed`
- Forecasting with popular theoretical distributions: normal, lognormal and Student's (T)
- Degrees of freedom optimization for Student's t-distribution to fit well at a given confidence level
- Testing distributions on historical data
- Popular risk metrics: VAR, CVaR, semi-deviation, variance and drawdowns
- Different financial ratios: CAPE10, Sharpe ratio, Sortino ratio, Diversification ratio
- Dividend yield and other dividend indicators for stocks
- Backtesting and comparing historical performance of a broad range of assets and indexes in multiple currencies
- Methods to track the performance of index funds (ETF) and compare them with benchmarks
- Main macroeconomic indicators: inflation, central banks rates
- Matplotlib visualization scripts for the Efficient Frontier, Transition map and assets risk / return performance

## Financial data and macroeconomic indicators

### End of day historical data

- Stocks and ETF for main world markets
- Mutual funds
- Commodities
- Stock indexes

### Currencies

- FX currencies
- Crypto currencies
- Central bank exchange rates

### Macroeconomic indicators
For many countries (China, USA, United Kingdom, European Union, Russia, Israel etc.):  

- Inflation
- Central bank rates
- CAPE10 (Shiller P/E) Cyclically adjusted price-to-earnings ratios

### Other historical data

- Real estate prices
- Top bank rates

## Installation

### Requirements

- Python **3.11** or newer
- Core dependencies: [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/), [scipy](https://scipy.org/) (plus `matplotlib`, `pyarrow`, `statsmodels`, `arch` and others). See [pyproject.toml](pyproject.toml) for the full list of dependencies and version constraints.

### Install from PyPI

```bash
pip install okama
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add okama          # add to a uv-managed project
uv pip install okama  # or pip-style install into the active environment
```

### Install the latest development version from GitHub

```bash
git clone -b dev https://github.com/mbk-dev/okama.git
cd okama
poetry install
```

## Getting started

> [!NOTE]
> All examples below are written for Jupyter Notebook / IPython. In a plain Python interpreter, wrap the displayed objects in `print(...)`.

### 1. Compare several assets from different stock markets. Get USD-adjusted performance

```python
import okama as ok

x = ok.AssetList(["SPY.US", "BND.US", "DBXD.XFRA"], ccy="USD")
x
```
![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi01.jpg)

Get the main parameters for the set:
```python
x.describe()
```
![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi02.jpg)

Get the assets accumulated return, plot it and compare with the USD inflation:
```python
x.wealth_indexes.plot()
```
![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi03.jpg)

### 2. Create a dividend stocks portfolio with base currency EUR

```python
weights = [0.3, 0.2, 0.2, 0.2, 0.1]
assets = ["T.US", "XOM.US", "FRE.XFRA", "SNW.XFRA", "LKOH.MOEX"]
pf = ok.Portfolio(assets, weights=weights, ccy="EUR")
pf.table
```
![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi04.jpg)

Plot the dividend yield of the portfolio (adjusted to the base currency).

```python
pf.dividend_yield.plot()
```
![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi05.png)

### 3. Draw an Efficient Frontier for 2 popular ETF: SPY and GLD

```python
ls = ["SPY.US", "GLD.US"]
curr = "USD"
last_date = "2020-10"
# Rebalancing period is one year (default value)
frontier = ok.EfficientFrontier(ls, last_date=last_date, ccy=curr, rebalancing_strategy=ok.Rebalance(period="year"))
frontier.names
```
![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi06.jpg)

Get the Efficient Frontier points for rebalanced portfolios and plot the chart with the assets risk/CAGR points:
```python
import matplotlib.pyplot as plt

points = frontier.ef_points

fig = plt.figure(figsize=(12, 6))
fig.subplots_adjust(bottom=0.2, top=1.5)
frontier.plot_assets(kind="cagr")  # plots the assets points on the chart
ax = plt.gca()
ax.plot(points.Risk, points.CAGR)
```
![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi07.jpg)

### 4. Get a Transition Map for allocations

```python
ls = ["SPY.US", "GLD.US", "BND.US"]
ok.EfficientFrontier(ls, ccy="USD").plot_transition_map(x_axe="risk")
```
![Transition map](https://raw.githubusercontent.com/mbk-dev/okama/images/images/readmi08.jpg)

## Examples

More examples are available as [Jupyter Notebooks](https://github.com/mbk-dev/okama/tree/master/examples):

1. [howto](https://github.com/mbk-dev/okama/blob/master/examples/01%20howto.ipynb) — main features of the _okama_ package: `Asset`, `AssetList`, and `Portfolio` objects.
2. [index funds performance](https://github.com/mbk-dev/okama/blob/master/examples/02%20index%20funds%20perfomance.ipynb) — compare ETFs and mutual funds with their benchmarks: tracking difference, tracking error, beta, and correlation.
3. [investment portfolios](https://github.com/mbk-dev/okama/blob/master/examples/03%20investment%20portfolios.ipynb) — portfolio properties and comparison of multiple portfolios.
4. [investment portfolios with DCF](https://github.com/mbk-dev/okama/blob/master/examples/04%20investment%20portfolios%20with%20DCF.ipynb) — portfolio strategies with cash flows (withdrawals and contributions), backtesting and longevity forecasts with Monte Carlo simulation.
5. [macroeconomics](https://github.com/mbk-dev/okama/blob/master/examples/05%20macroeconomics%20-%20inflation%20rates.ipynb) — historical inflation, key rates, and other macroeconomic indicators.
6. [efficient frontier single period](https://github.com/mbk-dev/okama/blob/master/examples/06%20efficient%20frontier%20single%20period.ipynb) — classic Markowitz frontiers with monthly rebalanced portfolios (`EfficientFrontierSingle`).
7. [efficient frontier multi-period](https://github.com/mbk-dev/okama/blob/master/examples/07%20efficient%20frontier%20multi-period.ipynb) — multi-period optimization with custom rebalancing frequencies or without rebalancing.
8. [backtesting distribution](https://github.com/mbk-dev/okama/blob/master/examples/08%20backtesting%20distribution.ipynb) — backtest portfolio return distributions with Jarque-Bera, Kolmogorov-Smirnov, and related diagnostics.
9. [financial database](https://github.com/mbk-dev/okama/blob/master/examples/09%20financial%20database.ipynb) — query the okama database for stocks, ETFs, mutual funds, indexes, currencies, and macroeconomic data.
10. [forecasting](https://github.com/mbk-dev/okama/blob/master/examples/10%20forecasting.ipynb) — forecast portfolio performance with normal, lognormal, Student's t, and historical distributions.
11. [rebalancing portfolio](https://github.com/mbk-dev/okama/blob/master/examples/11%20rebalancing%20portfolio.ipynb) — compare calendar-based, threshold-based, and hybrid portfolio rebalancing strategies.

> [!TIP]
> You can try the notebooks on Google Colab without installing anything: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mbk-dev/okama/blob/master/examples/01%20howto.ipynb)

## Documentation

The official documentation is hosted on readthedocs.org: [https://okama.readthedocs.io/](https://okama.readthedocs.io/)

## Financial Widgets
[okama.io](https://okama.io) offers interactive financial widgets (multi-page web application) 
built with the _okama_ package and [Dash (plotly)](https://github.com/plotly/dash) framework. Working example is available at 
[okama.io](https://okama.io/).

![](https://raw.githubusercontent.com/mbk-dev/okama/images/images/main_page.jpg) 

## MCP server

[okama-mcp](https://github.com/mbk-dev/okama-mcp) is an MCP (Model Context Protocol) server that exposes
the _okama_ toolkit to AI assistants — Claude Desktop, Claude Code, Cursor, and any other MCP-compatible
client. Ask the AI to backtest a portfolio, build an efficient frontier, or run a Monte Carlo retirement
forecast — it calls _okama_ directly, no Python code needed.

```bash
uvx okama-mcp stdio  # run straight from PyPI
```

okama-mcp is free and open source — no hosted service, no registration; you run it yourself, locally or
on your own server. See [mcp.okama.io](https://mcp.okama.io) for installation and client configuration.

## Roadmap

The plan for _okama_ is to add more functions that will be useful to investors and asset managers.

- Add support for a series of investment portfolios (a financial plan comprising multiple investment strategies, each active until a specific date, after which it transitions to another).
- Add multidimensional Monte Carlo with Ledoit-Wolf shrinkage
- Add Omega ratio to EfficientFrontier and Portfolio classes.
- Add Black-Litterman asset allocation 
- Add different utility functions for optimizers: IRR, portfolio survival period, semi-deviation, VaR, CVaR, drawdowns etc.
- Add more functions based on suggestions from users.

## Contributing to okama

Contributions are *most welcome*. Have a look at the [Contribution Guide](https://github.com/mbk-dev/okama/blob/master/CONTRIBUTING.md) for more.  
Feel free to ask questions on [Discussions](https://github.com/mbk-dev/okama/discussions).  
As contributors and maintainers to this project, you are expected to abide by okama's code of conduct. More information can be found at: [Contributor Code of Conduct](https://github.com/mbk-dev/okama/blob/master/CODE_OF_CONDUCT.md)

## Communication

For basic usage questions (e.g., "_Is XXX currency supported by okama?_") and for sharing ideas please use [GitHub Discussions](https://github.com/mbk-dev/okama/discussions).
Russian language community is available at [okama.io forums](https://community.okama.io).

### Core Implementation Code & Architecture
#### File: `okama/portfolios/__init__.py`
```python

```

#### File: `okama/common/__init__.py`
```python

```

#### File: `okama/common/helpers/__init__.py`
```python

```

#### File: `okama/api/__init__.py`
```python

```

#### File: `okama/frontier/__init__.py`
```python

```

#### File: `tests/__init__.py`
```python

```


==================================================


## [2/3] Repository: ml-quant-trading (`PHASE4-QUANT-178`)
- **Full Name**: `PHASE4-QUANT-178_initial-d__ml-quant-trading`
- **Description**: PyTorch research stack for ML multi-factor trading: 213 factors, bias correction, portfolio optimization, and vectorized backtesting.
- **GitHub Stars**: 86
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# ml-quant-trading

**A reproducible PyTorch stack for cross-sectional factor research — from 213
mask-aware factors to cost-aware portfolios, backtests, and auditable reports.**

[![CI](https://github.com/initial-d/ml-quant-trading/actions/workflows/ci.yml/badge.svg)](https://github.com/initial-d/ml-quant-trading/actions/workflows/ci.yml)
[![GitHub stars](https://img.shields.io/github/stars/initial-d/ml-quant-trading?style=flat&logo=github&label=Stars)](https://github.com/initial-d/ml-quant-trading/stargazers)
[![Release](https://img.shields.io/github/v/release/initial-d/ml-quant-trading?display_name=tag)](https://github.com/initial-d/ml-quant-trading/releases)
[![PyPI](https://img.shields.io/pypi/v/mlquantx.svg)](https://pypi.org/project/mlquantx/)
[![arXiv](https://img.shields.io/badge/arXiv-2507.07107-b31b1b.svg)](https://arxiv.org/abs/2507.07107)
[![DSH benchmark plugin](https://img.shields.io/badge/DSH-benchmark%20plugin-0f766e)](https://github.com/initial-d/dsh-plugin-mlquant-benchmark)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Languages: [English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

[**Run in Colab**](https://colab.research.google.com/github/initial-d/ml-quant-trading/blob/main/notebooks/quickstart_colab.ipynb)
· [**Project facts**](docs/answer_index.md)
· [**Agent benchmark challenge**](docs/agent_quant_benchmark_challenge.md)
· [**Inspect the benchmark**](docs/benchmark_board.md)
· [**Run with DSH**](docs/deepseek_harness_recipe.md)
· [**See cost-aware results**](docs/validation_dashboard.md)
· [**Read the paper**](https://arxiv.org/abs/2507.07107)

## Quick Start

```bash
python -m pip install mlquantx
mlquant demo
```

No market-data account or API key is required. In 30–90 seconds, the
deterministic demo runs data → factors → model → portfolio → backtest and writes
shareable Markdown and JSON reports.

Once it runs, you can [inspect the benchmark](docs/benchmark_board.md) or
[share a reproduction report](https://github.com/initial-d/ml-quant-trading/issues/new?template=reproduction_report.yml).
If the baseline is useful, a Star helps other researchers find it.
Evaluating privately? Use the
[private evaluation checklist](docs/private_evaluation_checklist.md) or submit a
[redacted evaluation note](https://github.com/initial-d/ml-quant-trading/issues/new?template=private_evaluation_note.yml)
without exposing proprietary data, positions, or strategy details.

| 213 factors | 4 data paths | 100 tests | CPU/GPU benchmark |
|---:|---:|---:|---:|
| Mask-aware PyTorch tensors | Synthetic, AkShare, Baostock, yfinance | Deterministic engineering checks | Reproducible across machines |

See the [benchmark board](docs/benchmark_board.md) for complete environments,
commands, and raw results. Cross-machine snapshots are reported separately and
are not presented as controlled hardware rankings.

---

## Why this repository?

| You get | Why it matters |
|---|---|
| **213 factor dimensions** | Mask-aware PyTorch factors with documented families and tensor primitives |
| **One end-to-end path** | Data → factors → models → portfolio → cost-aware backtest → report |
| **Public and synthetic data** | Start without proprietary data or an API key, then move to AkShare, Baostock, or yfinance |
| **Evidence, including failures** | Costs, turnover, baselines, caveats, and negative results stay visible |
| **A contribution path** | CI, tests, report templates, Colab, and newcomer-sized research tasks |

Try the live Hugging Face artifacts: the
[100,000-row synthetic dataset](https://huggingface.co/datasets/dddyym/ml-quant-trading-synthetic)
and [213-input MLP checkpoint](https://huggingface.co/dddyym/ml-quant-trading-synthetic-mlp).
Both come from the deterministic quick start and explicitly exclude real and
proprietary market data; see the [artifact guide](docs/huggingface_artifacts.md).

Ready to modify factors, models, data sources, or backtest assumptions? Install
from a source checkout:

```bash
git clone https://github.com/initial-d/ml-quant-trading.git
cd ml-quant-trading
python -m pip install -e '.[dev]'
```

## Fast Path

| If you want to... | Start here | What you get |
|---|---|---|
| See the project run | [`mlquant demo`](#quick-start) | A 30–90 second synthetic end-to-end smoke test |
| Summarize or cite the project | [Project Facts](docs/answer_index.md) | Canonical facts, links, evidence boundaries, and citation context |
| Audit implementation semantics | [Six Pipeline Invariants](docs/article_en_six_pipeline_invariants.md) | A deterministic check of factors, masks, labels, execution timing, and cost arithmetic |
| Understand the claims | [Research Card](docs/research_card.md) | Intended use, non-goals, validation status, and data caveats |
| Try public data | [Public-Data Mini Reproduction](docs/public_data_mini_reproduction.md) | A small yfinance factor-IC check with documented outputs |
| Run a larger validation | [Public-Data Validation](docs/public_data_validation.md) | Walk-forward baselines, costs, turnover, bootstrap CIs, and report artifacts |
| Run A-share validation | [AkShare CSI 300 Report](docs/validation_akshare_csi300_20260729.md) | Zero-auth A-share validation on the current CSI 300 public universe |
| Run paper-style public validation | [AkShare CSI 300 Daily 213-Factor Report](docs/validation_akshare_csi300_full_pipeline_20260729.md) | Daily 213-factor public-data approximation with turnover control |
| Test a coding or quant agent | [Agent Quant Benchmark Challenge](docs/agent_quant_benchmark_challenge.md) | A zero-account challenge for agent reproducibility, evidence preservation, and caveat discipline |
| Use DeepSeek Harness or a coding agent | [DeepSeek Harness Recipe](docs/deepseek_harness_recipe.md) · [optional DSH plugin](https://github.com/initial-d/dsh-plugin-mlquant-benchmark) · [Agent Reproducibility Guide](docs/agent_reproducibility.md) | Agent-ready benchmark and validation workflows without adding an agent runtime dependency |
| Evaluate a quant agent | [Quant Agent Reproducibility Target](docs/quant_agent_reproducibility_target.md) | A fixed benchmark/reporting target for agent harnesses without live trading claims |
| Evaluate privately | [Private Evaluation Checklist](docs/private_evaluation_checklist.md) | A redaction-safe way to record private or institutional runs |
| Contribute one run | [Reproduction report form](https://github.com/initial-d/ml-quant-trading/issues/new?template=reproduction_report.yml) | Run Colab, submit the generated report, and receive README credit |

## Validation Dashboard

Latest maintained public-data snapshot: [AkShare CSI 300 Daily 213-Factor Validation](docs/validation_dashboard.md).
The detailed dashboard includes cost-sensitivity charts, caveats, and reproduction commands.

| Run | Universe | Frequency | Factor set | Main result at 7 bps effective cost |
|---|---|---:|---:|---|
| Daily 213-factor public approximation | Current CSI 300, 2021-01-04 to 2024-12-31 | Daily | 213 | Buffered factor portfolio: 22.20% ann. return, 0.919 Sharpe, 2.1616 final equity |
| Equal-weight baseline | Same panel | Daily | n/a | 17.75% ann. return, 0.882 Sharpe, 1.8744 final equity |
| Naive daily factor selection | Same panel | Daily | 213 | Positive gross edge, but high turnover reduces net performance |

The dashboard is intentionally cost-aware: daily factor selection is evaluated
with turnover and transaction costs, not just gross returns. The run is a
public-data approximation, not an exact paper reproduction or investment claim.

Acknowledgement: the AkShare zero-auth A-share data path was added through
contributor work from [@redamancy231-create](https://github.com/redamancy231-create)
in [PR #42](https://github.com/initial-d/ml-quant-trading/pull/42).

## Community Evidence

| External contribution | What it added |
|---|---|
| [PR #18](https://github.com/initial-d/ml-quant-trading/pull/18) | ETF cross-asset public-data reproduction |
| [PR #34](https://github.com/initial-d/ml-quant-trading/pull/34) | Windows/Baostock A-share validation on 25 stocks |
| [PR #35](https://github.com/initial-d/ml-quant-trading/pull/35) | Neutralization and Baostock robustness fixes |
| [PR #36](https://github.com/initial-d/ml-quant-trading/pull/36) | English handbook for all factor families |
| [PR #42](https://github.com/initial-d/ml-quant-trading/pull/42) | Zero-account AkShare loader enabling CSI 300 validation |
| [PR #47](https://github.com/initial-d/ml-quant-trading/pull/47) | Clarified cumulative cost-drag units across code, reports, tests, and documentation |
| [Issue #59](https://github.com/initial-d/ml-quant-trading/issues/59) | Community Apple M4 protocol v1 CPU benchmark with raw caveats preserved |
| [DSH benchmark report #61](https://github.com/initial-d/ml-quant-trading/issues/61) | Seed DeepSeek Harness benchmark report with prompt, environment, artifact, and caveats |
| [Agent Quant Benchmark Challenge #66](https://github.com/initial-d/ml-quant-trading/discussions/66) | Challenge thread for coding agents, quant agents, DSH runs, and redacted private evaluations |
| [Issue #67](https://github.com/initial-d/ml-quant-trading/issues/67) | Community Windows CPU protocol v1 benchmark, archived on the benchmark board |
| [PR #68](https://github.com/initial-d/ml-quant-trading/pull/68) | Masked tensor factor regression coverage from a first-time contributor |
| [Awesome AI Trading Research review](https://github.com/ohselab/awesome-ai-trading-research/issues/1#issuecomment-5406093265) | Full-text curated-list evaluation: A-tier listing, with reproducibility and cross-market caveats |

Independent results are linked to their pull requests so the environment,
commands, limitations, and review history remain inspectable. Want to add
another machine or universe? [Run the zero-account Colab and submit the generated report](https://colab.research.google.com/github/initial-d/ml-quant-trading/blob/main/notebooks/quickstart_colab.ipynb).

DeepSeek Harness users can install the
[optional benchmark plugin](https://github.com/initial-d/dsh-plugin-mlquant-benchmark),
which is listed in
[Awesome DSH Plugin](https://awesome-dsh-plugin.com/#development--runtime), then
submit a structured
[DSH benchmark report](https://github.com/initial-d/ml-quant-trading/issues/new?template=deepseek_harness_benchmark.yml).

This repository is validation-first: simple baselines, transaction costs,
public-data failure modes, and negative results are documented alongside the
research pipeline.

**One useful contribution takes about ten minutes:** run the
[zero-account Colab](https://colab.research.google.com/github/initial-d/ml-quant-trading/blob/main/notebooks/quickstart_colab.ipynb),
then submit the generated report through the
[structured form](https://github.com/initial-d/ml-quant-trading/issues/new?template=reproduction_report.yml).
Successful and failed runs are both useful and credited.

**Other current calls for contributors**

- Join the [August 2026 reproduction challenge](https://github.com/initial-d/ml-quant-trading/discussions/43): run Colab once, then use the [structured report form](https://github.com/initial-d/ml-quant-trading/issues/new?template=reproduction_report.yml), whether it succeeds or fails.
- Try the [`v0.3.0` release](https://github.com/initial-d/ml-quant-trading/releases/tag/v0.3.0).
- Read the [Research Card](docs/research_card.md) for intended use, current evidence, and non-goals.
- Read the [public-data mini reproduction](docs/public_data_mini_reproduction.md).
- Share benchmark or public-data results in [Discussions #13](https://github.com/initial-d/ml-quant-trading/discussions/13).
- Pick up a newcomer task: [more benchmark reports](https://github.com/initial-d/ml-quant-trading/issues/7) or a [paired public-data validation or benchmark contribution](https://github.com/initial-d/ml-quant-trading/issues/22).
- Read the [Reality Check and Validation Status](docs/reality_check.md) before interpreting any backtest as evidence of deployable alpha.

> **Research and educational use only.** This project is not investment
> advice and is not production-ready. Backtest results do not represent live
> trading performance; they depend on data quality, transaction costs,
> slippage, and modeling assumptions that differ from real markets. Treat all
> results as research validation, not verified out-of-sample performance
> claims. See [Reality Check](docs/reality_check.md) for known limitations.

<details>
<summary>中文说明</summary>

> **仅用于研究和教学。** 本项目不构成投资建议，也不是可直接用于实盘交易的
> 生产系统。回测结果会受到数据质量、交易成本、滑点和建模假设影响，不代表
> 真实交易表现。请先阅读 [Reality Check](docs/reality_check.md) 中的限制说明。

</details>

| Module | What it does |
|--------|-------------|
| `features.tensor_factors` | GPU-vectorised masked primitives (`rank`, `corr`, `ewma`, `ts_*`) |
| `features.legacy_factors` | **204 hand-crafted alpha factors** ([English handbook](docs/factor_handbook_en.md) · [中文](docs/factor_handbook.md)) |
| `features.alpha101` | Alpha101-style formulaic factors |
| `features.neutralize` | Cross-sectional & industry neutralisation |
| `features.bias` | Limit-up / limit-down / halt bias correction |
| `training.augment` | GBM data augmentation |
| `models.nets` | MLP / Transformer |
| `models.losses` | AdjMSE, IC, RankIC losses |
| `portfolio.markowitz` | Cross-sectional Markowitz (shrunk cov, no-short) |
| `backtest.engine` | Vectorised backtest → Sharpe / IC / IR / DD |

## Data Sources

| Source | Market | Access | Notes |
|--------|--------|--------|-------|
| [AkShare](https://akshare.akfamily.xyz/) | A-shares | Public, no API key | Zero-auth loader backed by public upstream interfaces that may change or rate-limit |
| [Baostock](http://baostock.com) | A-shares | Free registration | Supported A-share loader; requires account |
| [yfinance](https://pypi.org/project/yfinance/) | US equities / ETFs | Public, rate-limited | Used for public-data validation and cross-market examples |
| Synthetic | N/A | Zero-config | Deterministic GBM panel for smoke testing the pipeline |

The repository does not redistribute market data. AkShare, Baostock, and
yfinance data are downloaded on-demand by the loader scripts. Public upstream
interfaces can change or rate-limit requests. Synthetic data is generated
deterministically from a fixed seed.

## Installation and Demos

```bash
python -m pip install mlquantx

# One-command smoke test (synthetic data; no API key required)
mlquant demo
```

The command prints a stage-by-stage run and writes shareable
`artifacts/small/summary.md` and `summary.json` reports alongside the model and
backtest artifacts. The demo is a deterministic engineering smoke test, not a
performance claim.

For development or optional extras, install from a source checkout:

```bash
git clone https://github.com/initial-d/ml-quant-trading.git
cd ml-quant-trading
python -m pip install -e '.[dev]'  # add ,gpu for CUDA; add ,mosek for MOSEK solver
```

### Google Colab Quick Start

Run the deterministic end-to-end pipeline in Google Colab without a market-data
account or local setup:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/initial-d/ml-quant-trading/blob/main/notebooks/quickstart_colab.ipynb)

The account-based [Baostock A-share notebook](demo_baostock.ipynb) remains
available for users who want that data route.

### Public-Data Factor IC Demo

For a lightweight public-data walkthrough, open [`notebooks/public_factor_ic.ipynb`](notebooks/public_factor_ic.ipynb). It downloads a small yfinance universe, computes a factor subset, and plots one-day forward rank IC. If public data download fails, the notebook falls back to the synthetic panel so the workflow remains runnable.

For a larger public-data validation run with walk-forward baselines, costs,
slippage, cost-sensitivity reports, optional bootstrap confidence intervals,
turnover, drawdown, and equal-weight / momentum / Alpha101 / MLP / Transformer
comparisons:

```bash
python scripts/public_data_validation.py \
  --source yfinance \
  --preset us-large-100 \
  --max-tickers 100
```

See [`docs/public_data_validation.md`](docs/public_data_validation.md). Treat
these runs as validation diagnostics, not trading recommendations. The script
writes `summary.md`, `summary.csv`, `summary.json`, `metadata.json`, and a
copy-ready `submission.md` for community reports. Add `--cost-grid-bps 0,7,15,30`
to generate `cost_sensitivity.*` files, and add `--bootstrap-samples 500` to
include return and Sharpe uncertainty intervals. Maintainers can aggregate
multiple `summary.json` files with `scripts/aggregate_validation_reports.py` and
audit individual reports with `scripts/audit_validation_report.py`.

### Tensor Factor Benchmark

To benchmark core tensor primitives and a small factor subset on CPU/GPU, run:

```bash
make benchmark
```

See [`docs/benchmarking.md`](docs/benchmarking.md) for larger-panel commands and reporting guidance.
Benchmark reports from different machines are welcome through the
[`Benchmark result`](.github/ISSUE_TEMPLATE/benchmark_result.yml) issue template.

### Reproducible Dev Environment

For a Docker-based CPU environment:

```bash
docker build -t ml-quant-trading .
docker run --rm ml-quant-trading make test
```

See [`docs/docker.md`](docs/docker.md) for Docker benchmark, synthetic pipeline,
and public-data validation commands.

For VS Code or GitHub Codespaces, use the included Dev Container:

```text
.devcontainer/devcontainer.json
```

It installs Python 3.11 and the project with `python -m pip install -e '.[dev]'`.

<details>
<summary><b>Maintainer, launch, and community resources</b></summary>

- [`CHANGELOG.md`](CHANGELOG.md) summarizes the public baseline release.
- [`docs/launch_playbook.md`](docs/launch_playbook.md) contains the launch checklist,
  recommended repository topics, and social preview guidance.
- [`docs/start_here.md`](docs/start_here.md) gives new users a fast path through the project.
- [`docs/research_card.md`](docs/research_card.md) summarizes intended use, validation status, data assumptions, and known risks.
- [`docs/architecture.md`](docs/architecture.md) shows the factor → model → portfolio → backtest pipeline.
- [`docs/reality_check.md`](docs/reality_check.md) explains what is real, what is still a smoke test, and what is not claimed.
- [`docs/faq.md`](docs/faq.md) answers common setup, data, and reproducibility questions.
- [`docs/docker.md`](docs/docker.md) documents the Docker and Dev Container setup.
- [`docs/benchmark_board.md`](docs/benchmark_board.md) tracks community benchmark reports.
- [`docs/public_data_mini_reproduction.md`](docs/public_data_mini_reproduction.md) records a small yfinance factor IC reproduction.
- [`docs/public_data_validation.md`](docs/public_data_validation.md) documents larger public-data walk-forward validation runs.
- [`docs/validation_akshare_csi300_20260729.md`](docs/validation_akshare_csi300_20260729.md) records the AkShare CSI 300 public A-share validation run for `v0.2.2`.
- [`docs/validation_akshare_csi300_full_pipeline_20260729.md`](docs/validation_akshare_csi300_full_pipeline_20260729.md) records the daily 213-factor AkShare CSI 300 public-data approximation.
- [`docs/validation_digest_20260727.md`](docs/validation_digest_20260727.md) summarizes the current public validation and discovery surface for `v0.2.1`.
- [`docs/community.md`](docs/community.md) explains contribution lanes and maintainer response rules.
- [`docs/release_draft_v0.1.0.md`](docs/release_draft_v0.1.0.md) is a copy-ready first release draft.
- [`docs/release_draft_v0.2.0.md`](docs/release_draft_v0.2.0.md) is the public validation and contributor-workflow release draft.
- [`docs/release_draft_v0.2.1.md`](docs/release_draft_v0.2.1.md) is the validation entrypoint and outreach follow-through release draft.
- [`docs/release_draft_v0.2.2.md`](docs/release_draft_v0.2.2.md) is the AkShare public A-share validation release draft.
- [`docs/release_draft_v0.3.0.md`](docs/release_draft_v0.3.0.md) is the Agent Quant Benchmark Challenge release draft.
- [`docs/promotion_kit.md`](docs/promotion_kit.md) contains copy-ready social and community posts.
- [`docs/article_zh_213_factor_csi300.md`](docs/article_zh_213_factor_csi300.md) is the
  long-form Chinese technical launch article.
- [`docs/community_posts_zh.md`](docs/community_posts_zh.md) adapts the article for
  Zhihu, Juejin, V2EX, JoinQuant, and Ricequant.
- [`docs/community_outreach.md`](docs/community_outreach.md) lists target communities and copy-ready outreach posts.
- [`docs/content_calendar.md`](docs/content_calendar.md) turns real updates into a four-week launch rhythm.
- [`docs/visibility_status.md`](docs/visibility_status.md) tracks live launch links, contributor calls, and next outreach steps.
- [`v0.1.0`](https://github.com/initial-d/ml-quant-trading/releases/tag/v0.1.0) is the first public research baseline release.
- [`v0.2.0`](https://github.com/initial-d/ml-quant-trading/releases/tag/v0.2.0) is the public validation and contributor-workflow release.
- [`v0.2.1`](https://github.com/initial-d/ml-quant-trading/releases/tag/v0.2.1) is the validation entrypoint and outreach follow-through release.
- [`v0.2.2`](https://github.com/initial-d/ml-quant-trading/releases/tag/v0.2.2) is the AkShare public A-share validation release.
- [Benchmark and reproduction discussion](https://github.com/initial-d/ml-quant-trading/discussions/13) is open for community reports.

</details>

---

## Factor Library (213 factors: 9 Alpha101 + 204 legacy)

The full feature set comprises **9 curated Alpha101 formulas** (`features.alpha101`) plus **204 hand-crafted legacy factors** (`features.legacy_factors`) for a total of **213 dimensions**. All factors are mask-aware PyTorch tensors with signature `Panel → (values[T,N], mask[T,N])`.

📖 **Factor Handbook:** [English](docs/factor_handbook_en.md) · [中文](docs/factor_handbook.md) — design notes and implementation rationale for each factor.

| Family | Count | Description |
|--------|-------|-------------|
| `better_001` – `better_028` | 28 | VWAP deviation + volume-weighted momentum |
| `best_001` – `best_021` | 21 | Close-location momentum variants |
| `old_027` – `old_076` | 50 | Classic alpha signals (corr/rank composites) |
| `stock_001` – `stock_022` | 22 | Per-stock derived series (volume, range, price) |
| `extra_001` – `extra_014` | 14 | Turnover + amount features |
| `add_001` – `add_030` | 30 | Additional composite factors |
| `change_001` – `change_005` | 5 | Short-window change-of-velocity |
| `original_001` – `original_028` | 28 | Close/volume direct statistics |
| `cs_rank_*` | 6 | Market breadth (cross-sectional rank signals) |

<details>
<summary><b>Full factor list (click to expand)</b></summary>

```
add_001    add_002    add_003    add_004    add_005    add_006
add_007    add_008    add_009    add_010    add_011    add_012
add_013    add_014    add_015    add_016    add_017    add_018
add_019    add_020    add_021    add_022    add_023    add_024
add_025    add_026    add_027    add_028    add_029    add_030
best_001   best_002   best_003   best_004   best_005   best_006
best_007   best_008   best_009   best_010   best_011   best_012
best_013   best_014   best_015   best_016   best_017   best_018
best_019   best_020   best_021
change_001 change_002 change_003 change_004 change_005
extra_001  extra_002  extra_003  extra_004  extra_005  extra_006
extra_007  extra_008  extra_009  extra_010  extra_011  extra_012
extra_013  extra_014
old_027    old_028    old_029    old_030    old_031    old_032
old_033    old_034    old_035    old_036    old_037    old_038
old_039    old_040    old_041    old_042    old_043    old_044
old_045    old_046    old_047    old_048    old_049    old_050
old_051    old_052    old_053    old_054    old_055    old_056
old_057    old_058    old_059    old_060    old_061    old_062
old_063    old_064    old_065    old_066    old_067    old_068
old_069    old_070    old_071    old_072    old_073    old_074
old_075    old_076
original_001 original_002 original_003 original_004 original_005
original_006 original_007 original_008 original_009 original_010
original_011 original_012 original_013 original_014 original_015
original_016 original_017 original_018 original_019 original_020
original_021 original_022 original_023 original_024 original_025
original_026 original_027 original_028
stock_001  stock_002  stock_003  stock_004  stock_005  stock_006
stock_007  stock_008  stock_009  stock_010  stock_011  stock_012
stock_013  stock_014  stock_015  stock_016  stock_017  stock_018
stock_019  stock_020  stock_021  stock_022
```

</details>

### Data Sources

You can directly fetch stock data from Yahoo Finance, Baostock, or AkShare.

**yfinance:**
```python
from mlquant.data im
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `src/mlquant/configs/__init__.py`
```python
"""Packaged configuration files for zero-setup CLI entry points."""
```

#### File: `src/mlquant/cli/__init__.py`
```python
"""``mlquant`` Click entry points (``mlquant gen-data``, ``mlquant features`` ...)."""
```

#### File: `.claude/settings.local.json`
```python
{
  "permissions": {
    "allow": [
      "Read(//d/fasttext/workspace//**)",
      "Read(//d/fasttext/workspace/**)"
    ]
  }
}
```

#### File: `src/mlquant/utils/__init__.py`
```python
"""Cross-cutting utilities: config loading, seeding, logging."""
from .config import Config, load_config
from .seed import seed_everything

__all__ = ["Config", "load_config", "seed_everything"]
```

#### File: `src/mlquant/training/__init__.py`
```python
"""Datasets, GBM augmentation, and the training loop."""
from .dataset import FactorDataset
from .augment import gbm_augment
from .trainer import Trainer, TrainConfig

__all__ = ["FactorDataset", "gbm_augment", "Trainer", "TrainConfig"]
```


==================================================


## [3/3] Repository: OptimalPortfolios (`PHASE4-QUANT-177`)
- **Full Name**: `PHASE4-QUANT-177_ArturSepp__OptimalPortfolios`
- **Description**: Production multi-asset portfolio construction and rolling backtesting in Python
- **GitHub Stars**: 94
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
---
myst:
  html_meta:
    description: >-
      Multi-asset portfolio construction and rolling backtesting in Python, with
      offline examples, constrained optimization, covariance models and analytics.
---

# optimalportfolios

*[author / affiliation / date — placeholder]*

Source: [OptimalPortfolios](https://github.com/ArturSepp/OptimalPortfolios).
Software citation: [CITATION.cff](https://github.com/ArturSepp/OptimalPortfolios/blob/main/CITATION.cff).
Analytics and holdings simulation use [qis](https://github.com/ArturSepp/QuantInvestStrats);
cite its [software record](https://github.com/ArturSepp/QuantInvestStrats/blob/main/CITATION.cff).

Explore the [analytics gallery](docs/analytics_gallery.md) for reproducible synthetic examples
with sample dates, conventions, producer links and reviewed provenance.

**Production multi-asset portfolio construction and rolling backtesting in Python — from
point-in-time covariance and alpha estimation through constrained optimisation, rebalancing,
transaction costs, and reporting.**

**Install:** `pip install optimalportfolios` · **Import:** `optimalportfolios` · **Status:** Stable

[![PyPI](https://img.shields.io/pypi/v/optimalportfolios?style=flat-square)](https://pypi.org/project/optimalportfolios/)
[![Python](https://img.shields.io/pypi/pyversions/optimalportfolios?style=flat-square)](https://pypi.org/project/optimalportfolios/)
[![CI](https://github.com/ArturSepp/OptimalPortfolios/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ArturSepp/OptimalPortfolios/actions/workflows/ci.yml)
[![Docs](https://readthedocs.org/projects/optimalportfolios/badge/?version=latest)](https://optimalportfolios.readthedocs.io/en/latest/)
[![License](https://img.shields.io/github/license/ArturSepp/OptimalPortfolios.svg?style=flat-square)](LICENSE.txt)
[![Downloads](https://static.pepy.tech/badge/optimalportfolios)](https://pepy.tech/project/optimalportfolios)
[![Monthly](https://static.pepy.tech/badge/optimalportfolios/month)](https://pepy.tech/project/optimalportfolios)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArturSepp/OptimalPortfolios/blob/main/examples/getting_started/production_quickstart.ipynb)

**Papers:** Sepp, A. (2023), *Optimal Allocation to Cryptocurrencies in Diversified Portfolios*, Risk Magazine — [SSRN 4217841](https://ssrn.com/abstract=4217841) · Sepp, A., Ossa, I. and Kastenholz, M. (2026), *Robust Optimization of Strategic and Tactical Asset Allocation for Multi-Asset Portfolios*, [The Journal of Portfolio Management, 52(4), 86–120](https://www.pm-research.com/content/iijpormgmt/52/4/86) · Sepp, A., Hansen, E. and Kastenholz, M. (2026), *Capital Market Assumptions and Strategic Asset Allocation Using Multi-Asset Tradable Factors* — [SSRN 6785958](https://ssrn.com/abstract=6785958). See [References](#references).

---

## Why optimalportfolios

PyPortfolioOpt, Riskfolio-Lib, and skfolio all provide substantial portfolio
optimisation capabilities. Their documented design centres emphasise, respectively,
compact classical allocation, breadth across risk measures and portfolio families,
and scikit-learn-compatible model selection. `optimalportfolios` is organised around
a different primary abstraction: a dated state transition from estimates and current
holdings to constrained targets and realised backtests.

**optimalportfolios solves the production problem end-to-end:**
estimate covariance → compute alpha signals → optimise with constraints →
rebalance on schedule → backtest with transaction costs — all in a single
roll-forward pipeline that handles incomplete data, mixed-frequency assets,
and illiquid positions.

### Key differentiators

**Production multi-asset portfolio construction.**
The package implements the full pipeline from the ROSAA framework: factor model
covariance estimation (via [`factorlasso`](https://github.com/ArturSepp/factorlasso))
→ risk-budgeted SAA → alpha signal computation →
TE-constrained TAA → rolling backtest. In this pipeline, equities can rebalance
monthly while alternatives rebalance quarterly, and an asset can enter the
allocation set only when sufficient return history is available. Weight bounds,
group allocation limits, tracking error budgets, turnover controls, and rebalancing
indicators for frozen positions share the same dated roll-forward state.

**HCGL factor covariance estimation.**
The Hierarchical Clustering Group LASSO factor model (published in JPM, 2026)
produces sparse, structured covariance matrices for heterogeneous multi-asset
universes. The LASSO/Group LASSO/HCGL solver is implemented in the standalone
[`factorlasso`](https://github.com/ArturSepp/factorlasso) package — a
general-purpose sparse factor model estimator with sign constraints,
prior-centred regularisation, and scikit-learn-compatible API.
`optimalportfolios` builds on top of `factorlasso` with finance-specific
functionality: `FactorCovarEstimator` handles multi-frequency asset returns,
rolling estimation schedules, factor covariance assembly
(Σ_y = β Σ_x β' + D), and integration with `qis` for performance attribution.
The separation means the LASSO solver can be used independently for any
multi-output regression problem (genomics, macro-econometrics), while the
portfolio-specific rolling pipeline stays in `optimalportfolios`.

**Cluster-aware risk allocation.**
Statistical clusters can be used after covariance estimation as an allocation
structure rather than only as a modelling diagnostic. `compute_group_risk_budgets()`
maps point-in-time clusters, sectors, or asset classes into asset-level risk
budgets; `rolling_risk_budgeting()` accepts either one static budget Series or a
date-by-asset budget panel; and `compute_hierarchical_risk_parity_weights()`
implements canonical HRP from an externally supplied linkage. Cluster formation,
distance transforms, De-PC1 diagnostics, and linkage estimation remain in
[`factorlasso`](https://github.com/ArturSepp/factorlasso); OptimalPortfolios owns
the conversion from that structure into portfolio weights and risk attribution.

**Drift-aware rolling backtests (new in v5.3.1).**
Turnover constraints and transaction-cost penalties act on the realised
current holdings, not the previous target. This eliminates the "phantom
turnover budget" issue where the optimiser thinks it's trading X but the
NAV simulator actually trades X·(1 + drift fraction). Controlled by
`OptimiserConfig.use_drifted_weights_0` (default `True`); set to `False`
to reproduce pre-v5.3.1 behaviour for legacy comparisons.

**NaN-aware rolling backtesting.**
The three-layer architecture (solver / wrapper / rolling) automatically handles
real-world data: assets with missing prices receive zero weight, assets entering
the universe mid-sample are included when sufficient history is available, and
the rebalancing indicator system freezes illiquid positions at their current
weight while re-optimising the liquid portion. When the freeze produces
group-constraint overshoots due to drift, the constraint is relaxed for that
rebalance with a logged warning rather than aborting. No data cleaning or
pre-filtering required.

**Research-backed methodology.**
The package is the reference implementation for the ROSAA framework published in
*The Journal of Portfolio Management* (Sepp, Ossa, Kastenholz, 2026). Its
optimisation solvers, covariance estimators, and alpha signals are covered by
offline tests and public worked examples.

<a id="quick-start-offline-rolling-backtest"></a>

## Five-minute quickstart

The [production quickstart](examples/getting_started/production_quickstart.py) is the authoritative
source for the first-use workflow. It runs entirely offline on the multi-asset fixture shipped in
the wheel and writes no files:

```bash
pip install optimalportfolios
python examples/getting_started/production_quickstart.py
```

For a zero-setup trial, [open the mechanically checked mirror in
Colab](https://colab.research.google.com/github/ArturSepp/OptimalPortfolios/blob/main/examples/getting_started/production_quickstart.ipynb).
The notebook installs the latest PyPI release, prints its version, and adds no notebook dependency
to the package.

The script uses a documented six-asset slice, a point-in-time 24-month EWMA covariance estimator,
quarterly constrained minimum-variance weights, a one-month implementation lag, and 10 basis
points of transaction costs. It prints the data range, rolling-weight dimensions, final weights,
final NAV, and measured runtime. The
[rendered quickstart documentation](https://optimalportfolios.readthedocs.io/en/latest/quickstart.html)
includes this same file directly, so the example and documentation cannot drift.

### A minimal executable example

The script above remains the authoritative first-use workflow. The shorter version below exists so
that the README's own code is executed rather than trusted:

```python
import qis
from optimalportfolios import (
    Constraints,
    EwmaCovarEstimator,
    PortfolioObjective,
    compute_rolling_optimal_weights,
)
from optimalportfolios.tests.data.multiasset import load_multiasset_data

prices = load_multiasset_data().prices.iloc[-120:, :4]
time_period = qis.TimePeriod(prices.index[0], prices.index[-1])

# estimate covariance → optimise → get rolling weights
estimator = EwmaCovarEstimator(returns_freq='ME', span=24, rebalancing_freq='QE')
covar_dict = estimator.fit_rolling_covars(prices=prices, time_period=time_period)
weights = compute_rolling_optimal_weights(prices=prices,
                                          portfolio_objective=PortfolioObjective.MAX_DIVERSIFICATION,
                                          constraints=Constraints(is_long_only=True),
                                          time_period=time_period,
                                          covar_dict=covar_dict)

# backtest with transaction costs
portfolio = qis.backtest_model_portfolio(prices=prices.loc[weights.index[0]:], weights=weights,
                                         rebalancing_costs=0.001, ticker='MaxDiv')

print(f"assets: {list(weights.columns)}")
print(f"rebalance dates: {len(weights.index)}")
print(f"long only: {bool((weights >= -1e-6).all().all())}")
print(f"fully invested: {bool(weights.sum(axis=1).round(6).eq(1.0).all())}")
print(f"nav name: {portfolio.nav.name}")
```

```result
assets: ['Global Bonds', 'Global IG Bonds', 'US Treasuries', 'US TIPs']
rebalance dates: 39
long only: True
fully invested: True
nav name: MaxDiv
```

`readme_test.py` executes the block above and diffs its output against that
`result` fence, so this example cannot drift from what the package actually
does. Structural facts are asserted rather than weights: a solver-version change
may move an allocation by 1e-9, but it must not change the rebalance schedule,
break long-only, or stop the book being fully invested.

The committed multi-asset fixture keeps this example offline. The same pipeline
supports price panels with NaNs and different start dates, while preserving
roll-forward estimation (no hindsight bias) and drift-aware turnover accounting.

### Design scope

The optimisation solvers use quadratic and conic objective functions (variance,
tracking error, Sharpe ratio, diversification ratio, CARA utility). The package
does not implement non-quadratic risk measures (CVaR, MAD, drawdown constraints).
For these, use Riskfolio-Lib or skfolio. The solver architecture (three-layer:
mathematical / wrapper / rolling) makes it straightforward to add new solvers —
each solver lives in its own module in `optimization/general`,
`optimization/risk_allocation`, `optimization/saa`, or `optimization/taa` and
plugs into the rolling backtester via a single dispatch function. The
[software-design guide](https://optimalportfolios.readthedocs.io/en/latest/software_design.html)
explains these boundaries and the alternatives considered; the
[package comparison](https://optimalportfolios.readthedocs.io/en/latest/package_comparison.html)
records the versioned evidence for the field comparison.

## When to use it — and when not

Use `optimalportfolios` when you need a dated roll-forward pipeline from point-in-time covariance
and alpha estimates to constrained targets, scheduled rebalancing, and drift-aware backtests with
transaction costs across incomplete or mixed-frequency multi-asset panels.

Choose another package when the core problem is a non-quadratic risk measure such as CVaR, MAD,
or drawdown constraints; the package comparison points to Riskfolio-Lib and skfolio for those
workflows. Use `factorlasso` directly when you need its standalone sparse multi-output factor-model
estimator rather than portfolio construction.

## Package overview

```
src/optimalportfolios/
├── config.py                      # PortfolioObjective enum
├── alphas/                        # Alpha signal computation
│   ├── signals/                   # risk-adjusted/classic momentum, carry, low_beta,
│   │                              #   residual momentum/reversal, managers_alpha, rolling_ewma_mean
│   ├── profile/                   # Signal profiling
│   ├── alpha_data.py              # AlphasData container
│   ├── backtest_alphas.py         # Signal backtesting tool
│   └── signal_diagnostics.py      # Signal IC-IR and risk-contribution diagnostics
├── covar_estimation/              # Covariance matrix estimation
│   ├── covar_estimator.py         # CovarEstimator ABC
│   ├── ewma_covar_estimator.py    # EwmaCovarEstimator
│   ├── factor_covar_estimator.py  # FactorCovarEstimator (uses factorlasso)
│   ├── risk_model_adapter.py      # Canonical qis.RiskModel adapter
│   ├── risk_labelling.py          # Deprecated shim; canonical lineage is in factorlasso
│   └── covar_reporting.py         # Rolling covariance diagnostics
├── optimization/                  # Portfolio optimisation
│   ├── constraints/               # Canonical public facade and constraint owners
│   │   ├── core.py                # Constraints aggregate and enforcement enum
│   │   ├── alignment.py           # Universe alignment and frozen-bound relaxation
│   │   ├── analytics.py           # Pure residual and feasibility analytics
│   │   ├── backends.py            # CVXPY, SciPy and risk-budgeting translations
│   │   ├── benchmarks.py          # Benchmark-deviation and beta constraints
│   │   ├── expressions.py         # Shared CVXPY risk and objective expressions
│   │   └── groups.py              # Group allocation, TRE and turnover constraints
│   ├── config.py                  # OptimiserConfig (incl. use_drifted_weights_0)
│   ├── covar_factorization.py     # Stabilised covariance and square-root factor
│   ├── solver_diagnostics.py      # Input contracts, outcomes, fallback and run summaries
│   ├── portfolio_result.py        # PortfolioOptimisationResult
│   ├── wrapper_rolling_portfolios.py  # compute_rolling_optimal_weights()
│   ├── general/                   # Objective-driven solvers
│   │   ├── quadratic.py           # min variance, max quadratic utility
│   │   ├── minimum_tracking_error.py  # closest feasible portfolio to benchmark
│   │   ├── max_sharpe.py          # maximum Sharpe ratio
│   │   ├── max_diversification.py # maximum diversification ratio
│   │   └── carra_mixture.py       # CARA utility under Gaussian mixture
│   ├── risk_allocation/           # Risk-based portfolio construction
│   │   ├── risk_budgeting.py      # constrained and rolling risk budgeting
│   │   ├── risk_budgeting_solver.py  # internal CCD/ADMM solver
│   │   ├── group_risk_budgeting.py   # group-to-asset risk budgets
│   │   └── hierarchical_risk_parity.py  # external-linkage HRP
│   ├── saa/                       # Strategic solvers with return/vol targets
│   │   ├── min_variance_target_return.py
│   │   └── max_return_target_vol.py
│   └── taa/                       # Tactical solvers with alpha and TE constraints
│       ├── maximise_alpha_over_tre.py
│       └── maximise_alpha_with_target_yield.py
├── universe/                      # Validated universe data containers and transforms
│   ├── universe_data.py           # UniverseData: prices, metadata and group loadings
│   └── universe_transforms.py     # e.g. copy with unsmoothed prices
├── utils/                         # Auxiliary analytics
│   ├── benchmark_beta.py          # Benchmark-beta loadings and dated portfolio beta
│   ├── filter_nans.py             # NaN-aware covariance/vector filtering
│   ├── portfolio_funcs.py         # Risk contributions, diversification ratio
│   ├── weights_drift.py           # apply_drift_to_weights_0
│   └── gaussian_mixture.py        # Gaussian mixture fitting (numpy/scipy EM)
└── reports/                       # Performance reporting
    ├── marginal_backtest.py       # Marginal asset contribution analysis
    ├── portfolio_result_plots.py  # Optimisation result plots
    └── portfolio_result_pybloqs.py  # Optional HTML/PDF result reports
examples/                          # Repository-only worked examples
├── data/                          # Shared universe fixtures
├── solvers/                       # One demo per single-objective solver
├── backtests/                     # End-to-end rolling workflows
├── comparisons/                   # A-vs-B sweeps (incl. drift_policy)
├── covar_estimation/              # Covariance estimator demos
└── alphas/                        # Alpha signal profiling demos
# factorlasso (pip install factorlasso)
#   └── LassoModel, solve_lasso_cvx_problem, solve_group_lasso_cvx_problem
#       Sign-constrained LASSO/Group LASSO/HCGL solver (domain-agnostic)
#       https://github.com/ArturSepp/factorlasso
```

### Analytics at a glance

| Area | Current user-facing analytics |
| --- | --- |
| Alpha construction | Momentum, low beta, risk-adjusted carry, managers alpha, residual momentum, residual reversal and rolling EWMA means; fixed-group and time-varying cluster scoring are supported. |
| Alpha evaluation | Rank-portfolio profiling, cross-backtests, `AlphasData`, IC/IR panels, component diagnostics and comparison tables. |
| Covariance and dependence | Current/rolling EWMA and HCGL sparse factor covariance; Pearson, Spearman and Gerber dependence choices, configurable correlation-distance transforms through `factorlasso`, and current/rolling covariance diagnostic reports. |
| Risk-cluster analytics | Persistent cluster lineage, births/deaths/splits/merges and report tables/figures through `analyze_risk_clusters()` and `run_risk_label_report()`. |
| General optimisation | Minimum variance, quadratic utility, maximum Sharpe, maximum diversification, CARA Gaussian-mixture utility and minimum tracking error. |
| Risk allocation | Constrained risk budgeting, point-in-time group risk budgets, date-varying rolling budgets, group Euler-risk attribution and external-linkage hierarchical risk parity. |
| SAA and TAA optimisation | Minimum variance at target return, maximum return at target volatility, alpha over tracking error and alpha at target portfolio return. |
| Constraints and implementation | Instrument/group bounds, exposure, turnover, tracking error, target return/volatility, benchmark-relative sector/style/beta limits, frozen holdings and current-to-model eligibility corridors. |
| Solver controls and diagnostics | One covariance factorization per compatible CVXPY solve, input-contract validation, structured `OptimizationOutcome`/`ConstraintResidual` output, infeasibility diagnosis and run-level warning summaries. |
| Portfolio and risk results | `PortfolioOptimisationResult` provides weights/trades, volatility, turnover, tracking error, factor/residual risk, group attribution, factor exposures, efficient-frontier data and report tables using `qis.RiskModel`. |
| Universe, backtest and reporting | Validated `UniverseData`, metadata/group-loadings persistence and transforms, drift-aware rolling weights, transaction-cost backtests through `qis`, efficient-frontier plots, marginal portfolio backtests and optional PyBloqs HTML/PDF reports. |

This table groups the analytics by workflow. The exact package-root import inventory and callable
signatures are maintained in the [API reference](docs/api.rst).

**Architecture: factorlasso vs optimalportfolios**

[`factorlasso`](https://github.com/ArturSepp/factorlasso) is the **domain-agnostic
LASSO solver** — it estimates sparse factor loadings β in Y_t = α + β X_t + ε_t with sign
constraints, prior-centered regularisation, and HCGL clustering. It provides
`LassoModel` (scikit-learn compatible estimator), `CurrentFactorCovarData`
(single-date covariance decomposition Σ_y = β Σ_x β' + D), and
`RollingFactorCovarData` (time-indexed collection). It knows nothing about
finance, asset returns, frequencies, or rebalancing schedules.

`optimalportfolios` adds two finance-specific covariance-integration layers on top:

**`estimate_lasso_factor_covar_data()`** — the core estimation function in
`covar_estimation/factor_covar_estimator.py`. It handles everything between
raw market data and the `factorlasso` solver:

* Computes factor returns from prices at the specified frequency
* Estimates annualised factor covariance Σ_x via EWMA
* Calls `factorlasso.LassoModel.fit()` separately per frequency for
  mixed-frequency universes (e.g., monthly equities + quarterly alternatives)
* Annualises residual variances, R², and alphas across frequencies
* Merges multi-frequency betas into a single (N × M) loading matrix
* Returns a `factorlasso.CurrentFactorCovarData` with the full decomposition

**`FactorCovarEstimator`** — a `CovarEstimator` subclass that wraps
`estimate_lasso_factor_covar_data()` in a rolling estimation schedule using
`qis.TimePeriod` and `qis.generate_dates_schedule`. It provides two APIs:

* `fit_rolling_covars()` → `Dict[Timestamp, DataFrame]` (plain covariance
  matrices, plug into any solver)
* `fit_rolling_factor_covars()` → `RollingFactorCovarData` (full
  decomposition with betas, R², clusters, residuals over time)

## Cluster-aware risk allocation

<a id="group-risk-budgets"></a>
<a id="hierarchical-risk-parity"></a>

See the [risk-budgeting guide](https://optimalportfolios.readthedocs.io/en/latest/risk_budgeting.html) for group risk budgets and hierarchical risk parity, including rolling cluster labels.

## Alpha signals module

<a id="naming-convention"></a>
<a id="available-signals"></a>
<a id="mixed-frequency-support"></a>
<a id="alphasdata-container"></a>

See the [alpha signals guide](https://optimalportfolios.readthedocs.io/en/latest/alphas_module_readme.html) for the signal catalogue, mixed-frequency inputs, cluster scoring, and the `AlphasData` container.

## Table of contents

1. [Why optimalportfolios](#why-optimalportfolios)
2. [Package overview](#package-overview)
3. [Cluster-aware risk allocation](#cluster-aware-risk-allocation)
4. [Alpha signals module](#alpha-signals-module)
5. [Installation](#installation)
6. [Portfolio Optimisers](#portfolio-optimisers)
7. [Examples](#examples)
8. [Updates](#updates)
9. [Disclaimer](#disclaimer)

## Installation

Install from PyPI:

```bash
pip install optimalportfolios
```

After installing `pytest`, verify the installed wheel with `python -m pytest --pyargs optimalportfolios`.

Upgrade with:

```bash
pip install --upgrade optimalportfolios
```

Clone the repository with:

```bash
git clone https://github.com/ArturSepp/OptimalPortfolios.git
```

The core package supports Python >=3.10. Its current dependency floors are NumPy >=2.0,
SciPy >=1.12, pandas >=2.2, Matplotlib >=3.8, seaborn >=0.13, openpyxl >=3.1,
PyYAML >=6.0, CVXPY >=1.5.2, SCS >=3.2.4.post3 (excluding 3.3.0),
quadprog >=0.1.11, `qis` >=5.26.0 and
`factorlasso` >=0.17.0. `pyproject.toml` is the source of truth.

Optional extras keep network-data and reporting integrations out of the core
installation. The default risk-lineage matcher is implemented with core NumPy/SciPy code.

| Extra | Adds |
| --- | --- |
| `data` | `yfinance` for free-data example loaders. |
| `reports` | `pybloqs` for HTML/PDF report backends. |
| `docs` | Sphinx, Furo and MyST for documentation builds. |

The runtime integration extras, `data` and `reports`, correspond to features that import their
dependencies. There is no `jupyter` extra: the package imports none of the Jupyter stack, and the
repository-only Colab quickstart uses Google's hosted runtime. Install notebook tooling separately
for local notebooks. The `docs` extra is the documentation toolchain. Tests and static checks are
contributor tooling in the PEP 735 `test` and `lint` dependency groups; there is no `dev` extra.

From a repository checkout, reproduce the locked test and lint environments with:

```bash
uv sync --locked --group test
uv run --no-sync pytest
uv run --locked --only-group lint ruff check src/optimalportfolios/
```

To run the repository-root examples that use free Yahoo data, add `--extra data` to the sync
command. For a user installation with both runtime integrati
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `src/optimalportfolios/utils/tests/__init__.py`
```python
"""Tests for ``optimalportfolios.utils``."""
```

#### File: `src/optimalportfolios/alphas/tests/__init__.py`
```python
"""Tests for ``optimalportfolios.alphas``."""
```

#### File: `src/optimalportfolios/alphas/profile/tests/__init__.py`
```python
"""Tests for the rank-based alpha profiler."""
```

#### File: `src/optimalportfolios/universe/tests/__init__.py`
```python
"""Tests for ``optimalportfolios.universe``."""
```

#### File: `src/optimalportfolios/optimization/tests/__init__.py`
```python
"""Tests for ``optimalportfolios.optimization``."""
```

#### File: `src/optimalportfolios/tests/__init__.py`
```python
"""Cross-cutting tests for ``optimalportfolios``."""
```


==================================================
