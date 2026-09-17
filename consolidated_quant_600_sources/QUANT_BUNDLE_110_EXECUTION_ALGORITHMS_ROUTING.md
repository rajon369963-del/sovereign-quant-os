# ⚡ [QUANT-SOURCE-110] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_110_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: hummingbot (`WHEEL_hummingbot`)
- **Full Name**: `hummingbot`
- **Description**: Open source software that helps you create and deploy high-frequency crypto trading bots
- **GitHub Stars**: 20023
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
![Hummingbot](https://github.com/user-attachments/assets/3213d7f8-414b-4df8-8c1b-a0cd142a82d8)

----
[![License](https://img.shields.io/badge/License-Apache%202.0-informational.svg)](https://github.com/hummingbot/hummingbot/blob/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/url?url=https://twitter.com/_hummingbot?style=social&label=_hummingbot)](https://twitter.com/_hummingbot)
[![Youtube](https://img.shields.io/youtube/channel/subscribers/UCxzzdEnDRbylLMWmaMjywOA)](https://www.youtube.com/@hummingbot)
[![Discord](https://img.shields.io/discord/530578568154054663?logo=discord&logoColor=white&style=flat-square)](https://discord.gg/hummingbot)

Hummingbot is an open-source framework that helps you design and deploy automated trading strategies, or **bots**, that can run on many centralized or decentralized exchanges. Over the past year, Hummingbot users have generated over $34 billion in trading volume across 140+ unique trading venues.

The Hummingbot codebase is free and publicly available under the Apache 2.0 open-source license. Our mission is to **democratize high-frequency trading** by creating a global community of algorithmic traders and developers that share knowledge and contribute to the codebase.

## Quick Links

* [Website and Docs](https://hummingbot.org): Official Hummingbot website and documentation
* [Installation](https://hummingbot.org/installation/): Install Hummingbot on various platforms
* [Discord](https://discord.gg/hummingbot): The main gathering spot for the global Hummingbot community
* [YouTube](https://www.youtube.com/c/hummingbot): Videos that teach you how to get the most out of Hummingbot
* [Twitter](https://twitter.com/_hummingbot): Get the latest announcements about Hummingbot
* [Reported Volumes](https://reporting.hummingbot.org/): Reported trading volumes across all Hummingbot instances
* [Newsletter](https://hummingbot.substack.com): Get our newsletter whenever we ship a new release

## Getting Started

### Condor (AI harness)

**[Condor](https://github.com/hummingbot/condor)** is the AI harness for building and running agentic strategies and bot instances. It connects LLM-powered decision-making to deterministic trade execution via the Hummingbot API, controlled through Telegram or its web dashboard. See **[condor.hummingbot.org](https://condor.hummingbot.org/)** to get started.

### `hbot` CLI

The recommended way to run the Hummingbot client directly is the **`hbot` command-line interface**, installed from
source. `hbot` runs, controls, and monitors a trading bot non-interactively: start/stop a bot, author
and tune configs, and read trades, PnL, logs, and status — all scriptable, as compact Markdown with
stable exit codes. See the **[hbot CLI guide](hummingbot/cli/README.md)** for the full reference.

Requires [Anaconda or Miniconda](https://www.anaconda.com/download).

```bash
# Clone the repository
git clone https://github.com/hummingbot/hummingbot.git
cd hummingbot

# Create the conda environment, build extensions, and expose the `hbot` CLI
make install

# Activate the environment
conda activate hummingbot
hbot --help
```

To use `hbot` outside the conda environment, run `make link-cli` to add it to your host PATH.

On first use, `hbot` prompts for a keystore password that encrypts your exchange API keys — set `HBOT_PASSWORD` or pass `--password-stdin` to run non-interactively (e.g. in scripts or agent workflows).

Then create a config and run the `simple_pmm` **paper trading script** — it simulates trading against live Binance market data, so no API keys are required:

```bash
hbot create simple_pmm --name conf_paper_bot.yml \
     --set exchange=binance_paper_trade --set trading_pair=BTC-USDT
hbot start conf_paper_bot.yml                          # run it (one bot per install)
hbot status                                            # check on it
hbot stop                                              # stop gracefully
```

To trade **live**, connect your exchange API keys and run a **strategy controller** like `pmm_mister` — a reusable V2 strategy whose settings can be tuned live while the bot runs:

```bash
hbot connect binance                                   # store API keys (encrypted)
hbot create pmm_mister --name conf_my_bot.yml \
     --set connector_name=binance --set trading_pair=BTC-USDT --set total_amount_quote=100
hbot start conf_my_bot.yml                             # run it (one bot per install)
```

Full command reference and ontology: **[hbot CLI guide](hummingbot/cli/README.md)**.

### Docker

Prefer containers? `hbot` works the same way — install [Docker Compose](https://docs.docker.com/compose/install/), then:

```bash
git clone https://github.com/hummingbot/hummingbot.git
cd hummingbot
make setup            # answer `y` to "Include Gateway?" to add the DEX middleware
make deploy           # start the container (interactive client by default)
make link-cli         # put the `hbot` command on your host PATH (dispatches into the container)

hbot --help           # same commands as the source install above
```

`make link-cli` installs a small wrapper that runs `hbot` inside the container, so every command
above is identical whether you installed from source or Docker. (Or skip it and use
`docker exec -it hummingbot hbot <command>`.) To dedicate the container to `hbot` instead of the
interactive client, uncomment `command: tail -f /dev/null` in `docker-compose.yml` before
`make deploy` — see [Running in Docker](hummingbot/cli/README.md#running-in-docker).

### Interactive Client (TUI)

The classic full-screen client is the Docker default:
`make deploy`, then `docker attach hummingbot` — or run it from source with
`make install && make run`. With Gateway included it starts in development mode
(unencrypted HTTP); for production HTTPS use the `DEV=false` flag and run `gateway generate-certs`.
See [Development vs Production Modes](https://hummingbot.org/gateway/installation/#development-vs-production-modes).

---

For comprehensive installation instructions and troubleshooting, visit our [Installation](https://hummingbot.org/installation/) documentation.

## Strategies

Hummingbot offers several frameworks for building and running algorithmic trading strategies — see the [Strategies docs](https://hummingbot.org/strategies/) for a full overview:

* **[Scripts](./scripts)**: Single-file Python strategies — the easiest way to build and customize your own bot. Example: [`simple_pmm.py`](./scripts/simple_pmm.py), a basic market making script.
* **[Controllers](./controllers)**: Reusable V2 strategies whose configs can be backtested, deployed, and tuned live while running. Example: [`pmm_mister.py`](./controllers/generic/pmm_mister.py), a full-featured market making controller.
* **[Executors](./hummingbot/strategy_v2/executors)**: Self-contained building blocks that manage order lifecycles for common patterns — position, DCA, grid, arbitrage, XEMM, TWAP, and LP. Example: [`position_executor`](./hummingbot/strategy_v2/executors/position_executor), which manages a directional position with triple-barrier risk controls.
* **[V1 Strategies](./hummingbot/strategy)**: Classic legacy strategies such as Pure Market Making, Avellaneda Market Making, and Cross-Exchange Market Making. Example: [`cross_exchange_market_making`](./hummingbot/strategy/cross_exchange_market_making), which market makes on one exchange and hedges fills on another.

## Exchange Connectors

Hummingbot connectors standardize REST and WebSocket API interfaces to different types of exchanges, enabling you to build sophisticated trading strategies that can be deployed across many exchanges with minimal changes.

### Connector Types

We classify exchange connectors into three main categories:

* **CLOB CEX**: Centralized exchanges with central limit order books that take custody of your funds. Connect via API keys.
  - **Spot**: Trading spot markets
  - **Perpetual**: Trading perpetual futures markets

* **CLOB DEX**: Decentralized exchanges with on-chain central limit order books. Non-custodial, connect via wallet keys.
  - **Spot**: Trading spot markets on-chain
  - **Perpetual**: Trading perpetual futures on-chain

* **AMM DEX**: Decentralized exchanges using Automated Market Maker protocols. Non-custodial, connect via Gateway middleware.
  - **Router**: DEX aggregators that find optimal swap routes
  - **AMM**: Traditional constant product (x*y=k) pools
  - **CLMM**: Concentrated Liquidity Market Maker pools with custom price ranges

### Exchange Sponsors

We are grateful for the following exchanges that support the development and maintenance of Hummingbot via broker partnerships and sponsorships.

| Exchange | Type | Sub-Type(s) | Connector ID(s) | Discount |
|------|------|------|-------|----------|
| [Backpack](https://hummingbot.org/exchanges/backpack/) | CLOB CEX | Spot, Perpetual | `backpack`, `backpack_perpetual` | [![Sign up for Backpack using Hummingbot's referral link!](https://img.shields.io/static/v1?label=Sponsor&message=Link&color=orange)](https://backpack.exchange/join/1tvdqfkk) |
| [Binance](https://hummingbot.org/exchanges/binance/) | CLOB CEX | Spot, Perpetual | `binance`, `binance_perpetual` | [![Sign up for Binance using Hummingbot's referral link for a 10% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d10%25&color=orange)](https://accounts.binance.com/register?ref=CBWO4LU6) |
| [Bitget](https://hummingbot.org/exchanges/bitget/) | CLOB CEX | Spot, Perpetual | `bitget`, `bitget_perpetual` | [![Sign up for Bitget using Hummingbot's referral link!](https://img.shields.io/static/v1?label=Sponsor&message=Link&color=orange)](https://www.bitget.com/expressly?channelCode=v9cb&vipCode=26rr&languageType=0) |
| [Derive](https://hummingbot.org/exchanges/derive/) | CLOB DEX | Spot, Perpetual | `derive`, `derive_perpetual` | [![Sign up for Derive using Hummingbot's referral link!](https://img.shields.io/static/v1?label=Sponsor&message=Link&color=orange)](https://www.derive.xyz/invite/7SA0V) |
| [Gate.io](https://hummingbot.org/exchanges/gate-io/) | CLOB CEX | Spot, Perpetual | `gate_io`, `gate_io_perpetual` | [![Sign up for Gate.io using Hummingbot's referral link for a 20% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d20%25&color=orange)](https://www.gate.io/referral/invite/HBOTGATE_0_103) |
| [Hyperliquid](https://hummingbot.org/exchanges/hyperliquid/) | CLOB DEX | Spot, Perpetual | `hyperliquid`, `hyperliquid_perpetual` | - |
| [KuCoin](https://hummingbot.org/exchanges/kucoin/) | CLOB CEX | Spot, Perpetual | `kucoin`, `kucoin_perpetual` | [![Sign up for Kucoin using Hummingbot's referral link for a 20% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d20%25&color=orange)](https://www.kucoin.com/r/af/hummingbot) |
| [Meteora](https://hummingbot.org/exchanges/gateway/meteora/) | AMM DEX | CLMM | `meteora` | - |
| [OKX](https://hummingbot.org/exchanges/okx/) | CLOB CEX | Spot, Perpetual | `okx`, `okx_perpetual` | [![Sign up for OKX using Hummingbot's referral link for a 20% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d20%25&color=orange)](https://www.okx.com/join/1931920269) |
| [Orca](https://hummingbot.org/exchanges/gateway/orca/) | AMM DEX | CLMM | `orca` | - |
| [XRP Ledger](https://hummingbot.org/exchanges/xrpl/) | CLOB DEX | Spot | `xrpl` | - |

### Other Exchange Connectors

Currently, the master branch of Hummingbot also includes the following exchange connectors, which are maintained and updated through the Hummingbot Foundation governance process. See [Governance](https://hummingbot.org/about/governance/) for more information.

| Exchange | Type | Sub-Type(s) | Connector ID(s) | Discount |
|------|------|------|-------|----------|
| [0x Protocol](https://hummingbot.org/gateway/connectors/) | AMM DEX | Router | `0x` | - |
| [Aevo](https://hummingbot.org/exchanges/aevo/) | CLOB CEX | Perpetual | `aevo_perpetual` | - |
| [Architect](https://hummingbot.org/exchanges/architect/) | CLOB CEX | Perpetual | `architect_perpetual` | - |
| [Balancer](https://hummingbot.org/exchanges/gateway/balancer/) | AMM DEX | AMM | `balancer` | - |
| [BingX](https://hummingbot.org/exchanges/bing_x/) | CLOB CEX | Spot | `bing_x` | - |
| [Bitrue](https://hummingbot.org/exchanges/bitrue/) | CLOB CEX | Spot | `bitrue` | - |
| [Bitstamp](https://hummingbot.org/exchanges/bitstamp/) | CLOB CEX | Spot | `bitstamp` | - |
| [BTC Markets](https://hummingbot.org/exchanges/btc-markets/) | CLOB CEX | Spot | `btc_markets` | - |
| [Bybit](https://hummingbot.org/exchanges/bybit/) | CLOB CEX | Spot, Perpetual | `bybit`, `bybit_perpetual` | - |
| [Coinbase](https://hummingbot.org/exchanges/coinbase/) | CLOB CEX | Spot | `coinbase_advanced_trade` | - |
| [Curve](https://hummingbot.org/exchanges/gateway/curve/) | AMM DEX | AMM | `curve` | - |
| [Decibel](https://hummingbot.org/exchanges/decibel/) | CLOB CEX | Perpetual | `decibel_perpetual` | - |
| [Dexalot](https://hummingbot.org/exchanges/dexalot/) | CLOB DEX | Spot | `dexalot` | - |
| [DFlow](https://hummingbot.org/exchanges/gateway/jupiter/#other-solana-routers) | AMM DEX | Router | `dflow` | - |
| [dYdX](https://hummingbot.org/exchanges/dydx/) | CLOB DEX | Perpetual | `dydx_v4_perpetual` | - |
| [EVEDEX](https://hummingbot.org/exchanges/evedex/) | CLOB CEX | Perpetual | `evedex_perpetual` | - |
| [Foxbit](https://hummingbot.org/exchanges/foxbit/) | CLOB CEX | Spot | `foxbit` | - |
| [Gemini](https://hummingbot.org/exchanges/gemini/) | CLOB CEX | Spot | `gemini` | - |
| [GRVT](https://hummingbot.org/exchanges/grvt/) | CLOB CEX | Perpetual | `grvt_perpetual` | - |
| [HTX (Huobi)](https://hummingbot.org/exchanges/htx/) | CLOB CEX | Spot | `htx` | - |
| [Injective Helix](https://hummingbot.org/exchanges/injective/) | CLOB DEX | Spot, Perpetual | `injective_v2`, `injective_v2_perpetual` | - |
| [Jupiter](https://hummingbot.org/exchanges/gateway/jupiter/) | AMM DEX | Router | `jupiter` | - |
| [Kraken](https://hummingbot.org/exchanges/kraken/) | CLOB CEX | Spot | `kraken` | - |
| [Lambdaplex](https://hummingbot.org/exchanges/lambdaplex/) | CLOB DEX | Spot | `lambdaplex` | - |
| [Lighter](https://hummingbot.org/exchanges/lighter/) | CLOB DEX | Spot, Perpetual | `lighter`, `lighter_perpetual` | - |
| [MEXC](https://hummingbot.org/exchanges/mexc/) | CLOB CEX | Spot | `mexc` | - |
| [NDAX](https://hummingbot.org/exchanges/ndax/) | CLOB CEX | Spot | `ndax` | - |
| [OKX DEX](https://hummingbot.org/exchanges/gateway/jupiter/#other-solana-routers) | AMM DEX | Router | `okx` | - |
| [Pacifica](https://hummingbot.org/exchanges/pacifica/) | CLOB CEX | Perpetual | `pacifica_perpetual` | - |
| [PancakeSwap](https://hummingbot.org/exchanges/gateway/pancakeswap/) | AMM DEX | AMM | `pancakeswap` | - |
| [Raydium](https://hummingbot.org/exchanges/gateway/raydium/) | AMM DEX | AMM, CLMM | `raydium` | - |
| [Titan](https://hummingbot.org/exchanges/gateway/jupiter/#other-solana-routers) | AMM DEX | Router | `titan` | - |
| [Uniswap](https://hummingbot.org/exchanges/gateway/uniswap/) | AMM DEX | Router, AMM, CLMM | `uniswap` | - |

## Other Hummingbot Repos

* [Condor](https://github.com/hummingbot/condor): AI harness for building and running agentic strategies and bot instances
* [Hummingbot API](https://github.com/hummingbot/hummingbot-api): The central hub for running Hummingbot trading bots
* [Gateway](https://github.com/hummingbot/gateway): Typescript based API client for DEX connectors
* [Hummingbot Site](https://github.com/hummingbot/hummingbot-site): Official documentation for Hummingbot - we welcome contributions here too!

## Getting Help

If you encounter issues or have questions, here's how you can get assistance:

* Consult our [FAQ](https://hummingbot.org/faq/), [Troubleshooting Guide](https://hummingbot.org/troubleshooting/), or [Glossary](https://hummingbot.org/glossary/)
* To report bugs or suggest features, submit a [GitHub issue](https://github.com/hummingbot/hummingbot/issues)
* Join our [Discord community](https://discord.gg/hummingbot) and ask questions in the #support channel

We pledge that we will not use the information/data you provide us for trading purposes nor share them with third parties.

## Contributions

The Hummingbot architecture features modular components that can be maintained and extended by individual community members.

We welcome contributions from the community! Please review these [guidelines](./CONTRIBUTING.md) before submitting a pull request.

If you represent an exchange that wants an official Hummingbot connector, see [How to Add a Hummingbot Connector](https://hummingbot.org/exchanges/#how-to-add-a-hummingbot-connector) for the available integration options.

## Legal

* **License**: Hummingbot is open source and licensed under [Apache 2.0](./LICENSE).
* **Data collection**: See [Reporting](https://hummingbot.org/reporting/) for information on anonymous data collection and reporting in Hummingbot.

### Core Implementation Code & Architecture
#### File: `hummingbot/core/__init__.py`
```python

```

#### File: `hummingbot/core/management/__init__.py`
```python

```

#### File: `hummingbot/core/web_assistant/__init__.py`
```python

```

#### File: `hummingbot/core/web_assistant/connections/__init__.py`
```python

```

#### File: `hummingbot/core/rate_oracle/__init__.py`
```python

```

#### File: `hummingbot/core/rate_oracle/sources/__init__.py`
```python

```


==================================================


## [2/3] Repository: machine-learning-for-trading (`WHEEL_machine-learning-for-trading`)
- **Full Name**: `machine-learning-for-trading`
- **Description**: Code for Machine Learning for Trading, 3rd edition — from data sourcing to live execution.
- **GitHub Stars**: 20913
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Machine Learning for Trading — 3rd Edition

**Build, test, and deploy ML-driven trading strategies — from data sourcing to live execution.**

This repository hosts the code for [*Machine Learning for Trading, 3rd Edition*](https://amzn.to/4eigy2F)
by [Stefan Jansen](https://www.linkedin.com/in/applied-ai/) — a ground-up
rebuild, organized around one end-to-end workflow: how you define a research idea and develop it iteratively into a
strategy you can actually run, and keep running, in a live market.

- [Nine case studies](https://www.ml4trading.io/case-studies/) illustrate the workflow throughout the 27 chapters of the
  book, from raw data through features, models, backtests, costs, and risk to deployment.
- **Generative AI** and **autonomous agents** are new to this edition and cut across that workflow, bringing
  retrieval-augmented generation, knowledge graphs, and multi-agent systems to financial research.
- The [companion website](https://ml4trading.io) features [112 primers](https://ml4trading.io/primer/),
  [61 agent skills](https://ml4trading.io/skills/),
  and [six production Python libraries](https://ml4trading.io/libraries/)
  that facilitate substantial parts of the workflow.

**Start here: [Installation](docs/installation.md)** walks a blank Linux, Windows or macOS
machine to a running notebook, prerequisites included. The short version is under
[Quick Start](#quick-start) below.

<!-- offerings:next start -->
> **Next free session:** [How to Be Productive with Coding Agents, Beyond Code](https://maven.com/p/efe730), a 30-minute live session on **Wednesday, September 30, 2026, 11:00 AM ET / 15:00 UTC**. [All courses, workshops, and free lessons](https://ml4trading.io/courses/?utm_source=github&utm_medium=readme&utm_campaign=ml4t3e&utm_content=offerings).
<!-- offerings:next end -->

<p align="center">
  <a href="https://amzn.to/4eigy2F"><img src="assets/cover.png" width="45%" alt="Machine Learning for Trading, 3rd Edition"></a>
</p>

---

## What's New in the Third Edition

The whole book traces one path: from data infrastructure and strategy research, across an *evidence boundary* that
separates tuning from evaluation, to deployment and monitoring — with a feedback loop that retrains, pauses, or
retires a strategy as its edge decays.

<p align="center">
  <img src="assets/workflow.png" width="90%" alt="The ML4T workflow: data infrastructure and strategy research, an evidence boundary separating tuning from evaluation, and deployment with a retrain/pause/retire feedback loop">
</p>

Where earlier editions moved technique by technique, the third edition runs that one process end to end — and adds
substantial new material:

- **A wider model toolkit**: from gradient boosting (XGBoost, LightGBM, CatBoost) to deep time-series architectures
  (PatchTST, iTransformer, TSMixer, TCN, Mamba) and newer tabular and latent-factor models (TabPFN, TabM, conditional
  and supervised autoencoders).
- **Dedicated strategy-design chapters**: transaction costs and risk management are now full chapters, neither of
  which existed before, joining portfolio construction and strategy synthesis so a raw signal is carried through to a
  sized, cost- and risk-aware portfolio.
- **A full production track**: live trading systems (Interactive Brokers, Alpaca, QuantConnect), MLOps and governance
  (drift detection, safe rollout, circuit breakers, feature stores, experiment tracking), and the operational reality
  of *running* strategies, not just building them.
- **Generative AI**: retrieval-augmented generation grounded in SEC filings, knowledge graphs and Graph RAG, and
  autonomous, multi-agent research systems.
- **Causal machine learning**: Double ML, Bayesian structural time series, and causal discovery for separating real
  effects from spurious correlation.
- **Reinforcement learning**: optimal execution, market making with inventory, and deep hedging.
- **Synthetic financial data**: TimeGAN, Tail-GAN, Sig-CWGAN, and diffusion-based generators for validation when
  history is short.

Methodological rigor is treated as a first-class topic rather than an afterthought. The book draws an explicit line
between exploration and confirmation — the *evidence boundary* — uses walk-forward cross-validation throughout, and
confronts the multiple-testing and overfitting problems that quietly invalidate most backtests, with tools like the
Deflated Sharpe Ratio, the Rademacher Anti-Serum, and White's Reality Check, plus conformal prediction for honest
uncertainty estimates.

The data layer moves to **Polars** for fast, expression-based manipulation, and every chapter ships in **reproducible
Docker environments** so results repeat across machines; PyTorch, LightGBM, Optuna, and Plotly round out the modeling
and visualization stack.

### Nine Case Studies

The structural centerpiece of the third edition is **[nine case studies](case_studies/)** that run the length of the
book. ETFs, crypto
perpetuals, intraday equities, options, FX, futures, and equity factor panels are each carried through the *same*
pipeline — from raw data and labels to features, models, backtests, costs, risk overlays, and a final deployment
assessment. One disciplined process applied to nine very different markets shows where it works, where it breaks, and
why.

| Case Study                                                              | Asset Class        | Frequency | What It Explores                                                             |
|-------------------------------------------------------------------------|--------------------|-----------|------------------------------------------------------------------------------|
| [ETFs](case_studies/etfs/)                                              | Multi-asset ETFs   | Daily     | Cross-asset momentum and mean-reversion across 100 ETFs                      |
| [Crypto Perps](case_studies/crypto_perps_funding/)                      | Crypto             | 8-hourly  | Funding-rate arbitrage on perpetual futures                                  |
| [NASDAQ-100](case_studies/nasdaq100_microstructure/)                    | Equities           | 15-min    | Intraday microstructure signals from order flow and the LOB                  |
| [S&P 500 Equity + Options](case_studies/sp500_equity_option_analytics/) | Equities + Options | Daily     | Equity selection enhanced with implied-volatility features                   |
| [US Firm Characteristics](case_studies/us_firm_characteristics/)        | Equities           | Monthly   | Firm-level characteristics panel (size, value, momentum, quality)            |
| [FX Pairs](case_studies/fx_pairs/)                                      | FX                 | Daily     | Carry and momentum across major currency pairs                               |
| [CME Futures](case_studies/cme_futures/)                                | Futures            | Daily     | Term-structure and roll-yield signals across commodity and financial futures |
| [S&P 500 Options](case_studies/sp500_options/)                          | Options            | Daily     | Options-only strategies (straddles, delta-hedged positions)                  |
| [US Equities](case_studies/us_equities_panel/)                          | Equities           | Daily     | Broad cross-section of US stocks with classic factor exposures               |

### Companion Resources

The [companion website](https://ml4trading.io) carries three things the chapters
lean on but do not reprint.

- **[112 primers](https://ml4trading.io/primer/)** are free, open explainers, one
  page per concept, covering what a chapter assumes you already know: limit order
  book mechanics, bitemporal data models, fractional differencing, multiple
  testing in factor research, conformal prediction, the deflated Sharpe ratio,
  hierarchical risk parity, Almgren-Chriss execution, walk-forward validation.
  Nothing to install and nothing to sign up for.
- **[61 agent skills](https://ml4trading.io/skills/)** are task recipes for coding
  agents, each carrying the same guards against lookahead bias, leakage, and
  multiple testing that the task needs when a person does it by hand. They span
  the research loop: building bars and triple-barrier labels, feature selection,
  purged walk-forward CV, cost models and tear sheets, position sizing, kill
  switches, live monitoring. Browsing the catalog is free; opening a skill's
  detail requires a website account.
- **[Six Python libraries](https://ml4trading.io/libraries/)** carry the pipeline
  the notebooks are built on, one per stage of the workflow. They are listed
  below and each is documented and usable on its own.

---

## The ML4T Libraries

The notebooks are built on six production Python packages, each documented and usable on its own — one per stage of
the workflow:

| Library                                                     | Stage      | What it does                                                                   |
|-------------------------------------------------------------|------------|--------------------------------------------------------------------------------|
| [`ml4t-data`](https://ml4trading.io/docs/data/)             | Data       | Unified market-data acquisition from 19+ providers behind one interface        |
| [`ml4t-engineer`](https://ml4trading.io/docs/engineer/)     | Signal     | Features, labels, alternative bars, and leakage-safe dataset preparation       |
| [`ml4t-models`](https://ml4trading.io/docs/models/)         | Models     | Finance-native latent factors, SDFs, direct prediction, and portfolio learning |
| [`ml4t-diagnostic`](https://ml4trading.io/docs/diagnostic/) | Evaluation | Feature validation, strategy diagnostics, and the Deflated Sharpe Ratio        |
| [`ml4t-backtest`](https://ml4trading.io/docs/backtest/)     | Strategy   | Event-driven backtesting with realistic execution                              |
| [`ml4t-live`](https://ml4trading.io/docs/live/)             | Deployment | Production trading with broker integrations                                    |

---

## Courses, Workshops, and Free Lessons

<!-- offerings:all start -->
**Cohorts and workshops.** Live, scheduled, and worked through with direct feedback on your own research.

| Starts | Offering | What you leave with |
|--------|----------|---------------------|
| Sep 16 – Dec 2, 2026 | [ML for Trading: From Research to Production](https://maven.com/stefan-jansen/research-to-production) | Take one research idea from a question to a costed, monitored strategy, with the evidence trail that makes the result checkable. |
| Sep 26, 2026 | [Engineering a Multi-Agent Forecasting System](https://maven.com/stefan-jansen/agent-engineering) | Build a multi-agent forecasting system whose reasoning is auditable end to end. |
| Oct 10, 2026 | [ML for Trading in the Age of AI Agents](https://maven.com/stefan-jansen/ml4t-ai-agents) | Run the whole ML for Trading workflow once, end to end, in a single session. |
| Oct 24, 2026 | [Loop Engineering: Reliable Work From Coding Agents](https://maven.com/stefan-jansen/loop-engineering) | Get reliable work out of coding agents: harness design, verification, and recovery from a bad run. |

**Free live sessions.** Thirty minutes to an hour, no cost, recording sent to everyone who registers.

| When | Session |
|------|---------|
| Wed, Sep 30, 11:00 AM ET / 15:00 UTC | [How to Be Productive with Coding Agents, Beyond Code](https://maven.com/p/efe730) |
| Wed, Oct 7, 11:00 AM ET / 15:00 UTC | [How AI Agents Change the ML for Trading Workflow](https://maven.com/p/222e36) |
| Wed, Nov 4, 11:00 AM ET / 16:00 UTC | [Why Multi-Agent Systems Break, and How To Fix It](https://maven.com/p/393eee) |

*Between cohorts, the [**Insights** newsletter](https://insights.ml4trading.io/) covers the same ground weekly, source by source.*
<!-- offerings:all end -->

---

## The Book, Chapter by Chapter

An introduction and a closing chapter bookend six workflow-aligned parts. Every
chapter title links to its own guide, which carries the full description, the
notebooks, and the data each one needs.

### Introduction

| Chapter | What it covers |
|---------|----------------|
| **[1. The Process Is Your Edge](01_process_is_edge/)** | Why process discipline beats model sophistication: the ML4T workflow as a research-to-production system, regime detection on factor returns and macro indicators, and the evidence boundary that separates exploration from confirmation. |

### Part I - Financial Data (Chapters 2-5)

The markets, instruments, and infrastructure the rest of the book builds on: a taxonomy of sources, raw exchange messages turned into feature-ready bars, point-in-time fundamentals, and synthetic histories for robust validation.

| Chapter | What it covers |
|---------|----------------|
| **[2. The Financial Data Universe](02_financial_data_universe/)** | Eight asset classes surveyed, survivorship bias quantified, storage formats benchmarked (Parquet, DuckDB, kdb+, TimescaleDB), and the data-quality framework used throughout the book. |
| **[3. Market Microstructure](03_market_microstructure/)** | NASDAQ ITCH parsing, limit order book reconstruction from several sources, Lee-Ready trade classification validated, and bar-sampling methods compared; dollar bars deliver the best return normality. |
| **[4. Fundamental and Alternative Data](04_fundamental_alternative_data/)** | Point-in-time SEC EDGAR pipelines, entity resolution across identifier systems, macro and commodity fundamentals, and alternative-data evaluation including on-chain crypto and prediction markets (Kalshi, Polymarket). |
| **[5. Synthetic Financial Data](05_synthetic_data/)** | TimeGAN, Tail-GAN, Sig-CWGAN, Diffusion-TS, and LLM-based tabular generation, each evaluated through a fidelity, utility, and privacy framework. |

### Part II - Research Design and Feature Engineering (Chapters 6-10)

Define the trading problem, then turn data into model-ready signals: research design, labels, features, and the evaluation that determines what any model can learn.

| Chapter | What it covers |
|---------|----------------|
| **[6. Strategy Research Framework](06_strategy_definition/)** | Universe rules, decision schedule, cost model, evaluation protocol, and run logging. Introduces the nine case studies and the walk-forward cross-validation discipline that anchors Chapters 7 to 20. |
| **[7. Defining the Learning Task](07_defining_the_learning_task/)** | Forward-return, triple-barrier, and trend-scanning labels; information coefficients, quantile analysis, and feasibility screens; multiple-testing control with BH-FDR and the Deflated Sharpe Ratio; causal plausibility checks. |
| **[8. Financial Feature Engineering](08_financial_features/)** | Five feature families from price (momentum, reversal, volatility, liquidity, microstructure), structural and cross-instrument features, macro and calendar context, and selection with robustness testing. |
| **[9. Model-Based Feature Extraction](09_model_based_features/)** | Features from fitted models: stationarity diagnostics, Kalman filters, Fourier and wavelet spectral features, GARCH volatility, and HMM regime probabilities, all point-in-time correct. |
| **[10. Text Feature Engineering](10_text_feature_engineering/)** | Bag-of-words through transformers: TF-IDF, Word2Vec and GloVe embeddings, LSTM sequence models, FinBERT sentiment, financial NER fine-tuning, and news-return signal construction. |

### Part III - Model Development (Chapters 11-15)

Five model families applied to the same nine case studies, each building on the linear baseline.

| Chapter | What it covers |
|---------|----------------|
| **[11. The ML Pipeline](11_ml_pipeline/)** | Ridge, LASSO, and Elastic Net as the baseline every later model must beat, logistic regression for direction, SHAP interpretability, conformal prediction for uncertainty, and a comparison across all nine case studies. |
| **[12. Gradient Boosting and Advanced Tabular Models](12_gradient_boosting/)** | XGBoost, LightGBM, and CatBoost with Optuna multi-objective tuning, plus the deep tabular alternatives TabPFN and TabM. TreeSHAP explainability, and gradient boosting the strongest tabular model in most case studies. |
| **[13. Deep Learning for Time Series](13_dl_time_series/)** | LSTM, N-BEATS, PatchTST, iTransformer, TFT, TSMixer, TCN, and Mamba set against the LTSF-Linear debate, with a selection framework and cross-dataset evidence on when depth helps. |
| **[14. Latent Factor Models](14_latent_factors/)** | PCA eigenportfolios, IPCA with time-varying loadings, conditional and supervised autoencoders, adversarial SDF estimation, and yield-curve decomposition. |
| **[15. Causal Machine Learning](15_causal_estimation/)** | Double Machine Learning for isolating factor treatment effects, Bayesian Structural Time Series for event impact, and causal discovery with PCMCI, NOTEARS, and VAR-LiNGAM. |

### Part IV - Strategy Implementation (Chapters 16-20)

From predictions to deployable strategies: backtesting, portfolio construction, costs, risk, and synthesis.

| Chapter | What it covers |
|---------|----------------|
| **[16. Strategy Simulation](16_strategy_simulation/)** | Backtesting as falsification: trading-protocol specification, vectorized against event-driven engines, an ETF baseline, regime diagnostics, and overfitting control with the Deflated Sharpe Ratio, the Rademacher Anti-Serum, and White's Reality Check. |
| **[17. Portfolio Construction](17_portfolio_construction/)** | From scores to portfolios: mean-variance optimization and its pitfalls, Hierarchical Risk Parity, the Kelly criterion, conformal position sizing, deep allocation, and a controlled allocator comparison. |
| **[18. Transaction Costs](18_transaction_costs/)** | Cost taxonomy, spread estimation, market-impact calibration, execution algorithms (VWAP, TWAP, Almgren-Chriss), transaction-cost analysis, and breakeven costs that vary widely by asset class. |
| **[19. Risk Management](19_risk_management/)** | VaR and CVaR tail measurement, drawdown and path-risk controls, factor and sector decomposition, stress testing, adaptive risk overlays, deep hedging, and kill switches; overlay effectiveness turns out to be strategy-specific. |
| **[20. Strategy Synthesis](20_strategy_synthesis/)** | What nine experiments reveal about turning predictions into strategies: IC-Sharpe decorrelation, Fundamental Law diagnostics, the model-family cascade, cost-survival analysis, and holdout failure modes. |

### Part V - Advanced AI (Chapters 21-24)

Reinforcement learning, large language models, knowledge graphs, and autonomous agents for finance.

| Chapter | What it covers |
|---------|----------------|
| **[21. Reinforcement Learning for Execution and Hedging](21_rl_execution_hedging/)** | MDP formulation for finance, DQN, PPO and SAC, optimal execution, market making with inventory management, deep hedging with PFHedge, inverse RL for strategy recovery, and the sim-to-real gap. |
| **[22. RAG for Financial Research](22_rag_financial_research/)** | Retrieval-augmented generation grounded in SEC filings: ingestion, domain-specific embeddings, hybrid retrieval with re-ranking, constraint-based prompting, evaluation and failure diagnostics, and the move to agentic workflows. |
| **[23. Knowledge Graphs](23_knowledge_graphs/)** | When graphs earn their infrastructure cost: construction from SEC filings, Graph RAG for multi-hop reasoning, GNN embeddings and centrality as ML features, financial networks, and temporal-leakage prevention. |
| **[24. Autonomous Agents](24_autonomous_agents/)** | ReAct, Tree of Thoughts, and Reflexion architectures, memory systems, tool contracts, the engineering stack (LangGraph, Claude SDK), a stateful equity-research agent, multi-agent forecasting with adversarial debate, and production reliability. |

### Part VI - Production (Chapters 25-26)

Taking strategies live: trading systems and the operational infrastructure that keeps them running.

| Chapter | What it covers |
|---------|----------------|
| **[25. Live Trading Systems](25_live_trading/)** | A framework bridging research and production: Interactive Brokers and Alpaca integration, managed platforms (QuantConnect), order-lifecycle management, pipeline verification, and operational readiness. |
| **[26. MLOps and Governance](26_mlops_governance/)** | A failure taxonomy separating pipeline divergence from performance decay, drift detection, safe model rollout, circuit breakers, feature stores, and experiment tracking. |

### Conclusion

| Chapter | What it covers |
|---------|----------------|
| **[27. The Systematic Edge](27_systematic_edge/)** | The systematic philosophy, quant career paths, learning resources, research frontiers, and how to build your own edge. The closing bookend to Chapter 1: the process is the edge. |

---

## Quick Start

**New here? Read these three, in order.**

1. **[What this repository is, and what it is not](docs/what-this-is.md)** - what reproduces with
   one command, what a configuration change buys you, what needs real compute or licensed data,
   and what is not promised. Five minutes, before you install anything.
2. **[Installation](docs/installation.md)** - Linux, Windows WSL2, macOS, Docker, and GPU, in full.
3. **[Running notebooks](docs/running-notebooks.md)** - the case-study pipeline, the run log, and
   how to experiment without disturbing the downloaded results.

Everything below is typed into a terminal on your own computer, not into GitHub, and run **from the
repository root**. New to the command line? Start with
**[Before You Begin](docs/installation.md#before-you-begin)**.

### 1. Clone and install

```bash
git clone https://github.com/stefan-jansen/machine-learning-for-trading.git
cd machine-learning-for-trading
cp .env.example .env   # the defaults work as-is; nothing in it needs editing to start
```

Then pick one environment. **Option A, Docker**, carries every dependency and needs no compiler:

```bash
docker compose pull ml4t
```

**Option B, a local `uv` environment**, on macOS, Linux, or inside WSL2. Install `uv` with its own
installer, not with `pip`, which is missing or refuses to install on most current systems:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env   # the installer's own line; puts uv on PATH here and now
uv sync
```

Option B compiles several dependencies from source, `scikit-learn` among them, so it needs a C/C++
compiler and the Python headers: `sudo apt install build-essential python3-dev` on Ubuntu, Debian
and WSL2, `xcode-select --install` on macOS. Budget about **16 GB** of disk (11 GB environment,
4 GB free datasets, 0.9 GB of git history).

| Platform | Take | Why |
|----------|------|-----|
| Linux | either | Both paths are exercised on every release |
| macOS, Apple Silicon | **B** | Walked on real hardware before each release. Docker there earns its disk only for the twelve pre-executed `ml4t-py312` notebooks, which have no arm64 build, and Chapter 2's containerized database benchmarks |
| macOS, Intel | **A** | PyTorch publishes no macOS x86_64 wheel, so the local path cannot resolve |
| Windows | either, **inside WSL2** | Run `wsl --install -d Ubuntu` from an Administrator PowerShell, restart, then run it a second time: the first run usually installs the WSL runtime without a distribution. Then follow the Linux instructions in the Ubuntu terminal. Installing into Windows Python is unsupported and does not work |

### 2. Download data

Most notebooks need datasets. Start with the free ones, which need no API keys:

```bash
uv run python data/download_all.py --free-only
```

That fetches seven datasets, about **4 GB** and twelve minutes, almost all of it the
firm-characteristics panel first needed in Chapter 4. To start in about 75 MB and fetch it when a
chapter asks:

```bash
uv run python data/download_all.py --free-only --skip-firm-characteristics
```

On the Docker path there is no host Python: run the same command without `uv run`, in the Jupyter
Lab terminal (**File → New → Terminal**). The **[data guide](data/README.md)** documents every
dataset, API-key setup, the loaders, and the storage tiers.

**Optional: pre-computed results.** To explore the nine released Chapter 11-20 case studies without
retraining, download their verified registries, predictions, model files, and backtest artifacts:

```bash
uv run python scripts/download_artifacts.py
```

### 3. Run notebooks

First confirm the install, with the one command that answers it. It prints a
PASS or FAIL line per component and exits non-zero on any required failure:

```bash
uv run python scripts/verify_installation.py                     # Option B
docker compose run --rm ml4t python scripts/verify_installation.py   # Option A
```

Notebooks are paired [Jupytext](https://jupytext.readthedocs.io/) files, a `.py` source and a
gene
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/fixtures/__init__.py`
```python

```

#### File: `scripts/__init__.py`
```python

```

#### File: `envs/__init__.py`
```python

```

#### File: `data/alternative/__init__.py`
```python

```

#### File: `case_studies/__init__.py`
```python

```


==================================================


## [3/3] Repository: quant-trading-bot (`WHEEL_quant-trading-bot`)
- **Full Name**: `quant-trading-bot`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Quant-trading

&nbsp;

## Intro

&nbsp;

> We’re right 50.75 percent of the time... but we’re 100 percent right 50.75 percent of the time, you can make billions that way. <br><br>
> --- Robert Mercer, co-CEO of Renaissance Technologies

> If you trade a lot, you only need to be right 51 percent of the time, we need a smaller edge on each trade. <br><br>
> --- Elwyn Berlekamp, co-Founder of Combinatorial Game Theory

###### *The quotes above come from a book by Gregory Zuckerman, a book every quant must read, THE MAN WHO SOLVED THE MARKET.*

&nbsp;

Most scripts inside this repository are technical indicator automated trading. These scripts include various types of momentum trading, opening range breakout, reversal of support & resistance and statistical arbitrage strategies. Yet, quantitative trading is not only about technical analysis. It can refer to computational finance to exploit derivative price mismatch, pattern recognition on alternative datasets to generate alphas or low latency order execution in the market microstructure. Hence, there are a few ongoing projects inside this repository. These projects are mostly quantamental analysis on some strange ideas I come up with to beat the market (or so I thought). There is no HFT strategy simply because ultra high frequency data are very expensive to acquire (even consider platforms like Quantopian or Quandl). Additionally, please note that, all scripts are historical data backtesting/forward testing (basically via Python, not C++, maybe Julia in the near future). The assumption is that all trades are frictionless. No slippage, no surcharge, no illiquidity. Last but not least, all scripts contain a global function named main so that you can embed the scripts directly into you trading system (although too lazy to write docstring).

### Table of Contents

&nbsp;

#### Options Strategy

* <a href=https://github.com/je-suis-tm/quant-trading#12-options-straddle>Options Straddle</a>
* <a href=https://github.com/je-suis-tm/quant-trading#15-vix-calculator>VIX Calculator</a>

&nbsp;

#### Quantamental Analysis

* <a href=https://github.com/je-suis-tm/quant-trading#11-monte-carlo-project>Monte Carlo Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#6-oil-money-project>Oil Money Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#2-pair-trading>Pair Trading</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#13-portfolio-optimization-project>Portfolio Optimization Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#14-smart-farmers-project>Smart Farmers Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#16-wisdom-of-crowds-project>Wisdom of Crowd Project</a>

&nbsp;

#### Technical Indicators

* <a href=https://github.com/je-suis-tm/quant-trading#5-awesome-oscillator>Awesome Oscillator</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#9-bollinger-bands-pattern-recognition>Bollinger Bands Pattern Recognition</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#7-dual-thrust>Dual Thrust</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#3-heikin-ashi-candlestick>Heikin-Ashi Candlestick</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#4-london-breakout>London Breakout</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#1-macd-oscillator>MACD Oscillator</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#8-parabolic-sar>Parabolic SAR</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#10-relative-strength-index-pattern-recognition>Relative Strength Index Pattern Recognition</a>

* <a href=https://github.com/je-suis-tm/quant-trading#17-shooting-star>Shooting Star</a>

&nbsp;

### Data Source

* Bloomberg/Eikon

* <a href=https://github.com/je-suis-tm/web-scraping/blob/master/CME3.py>CME</a>/<a href=https://github.com/je-suis-tm/web-scraping/blob/master/LME.py>LME</a>

* <a href=https://www.histdata.com/>Histdata</a>/<a href=https://fxhistoricaldata.com>FX Historical Data</a>

* <a href=https://github.com/je-suis-tm/web-scraping/blob/master/Macrotrends.py>Macrotrends</a>

* <a href=https://stooq.com>Stooq</a>/<a href=https://www.quandl.com>Quandl</a>

* <a href=https://github.com/je-suis-tm/web-scraping/blob/master/WallStreetBets.py>Reddit WallStreetBets</a>

* <a href=https://github.com/je-suis-tm/web-scraping>Web Scraping</a>

* <a href=https://finance.yahoo.com>Yahoo Finance</a>/<a href=https://pypi.org/project/fix-yahoo-finance>fix_yahoo_finance package</a>/<a href=https://pypi.org/project/yfinance>yfinance package</a> 

<br>

## Strategies:

### 1. MACD oscillator

MACD oscillator is trading strategy 101. MACD refers to Moving Average Convergence/Divergence. It is a momentum trading strategy which holds the belief that upward/downward momentum has more impact on short term moving average than long term moving average. It only takes 5 minutes for any bloke with no background in finance to trade with MACD signals. Regarding the simplicity of MACD oscillator, it is the most common strategy among the non-professionals in the market. In behavioral economics, the more people believe in the strategy, the more effective the strategy becomes (not always true, e.g. 2008). Therefore, we should not underestimate the power of MACD oscillator.

For the strategy itself, we compute long term moving average and short term moving average on the close price of a given stock. To generate the trading signal, we implement a comparison between the moving averages of different time horizons. When short term moving average is above long term moving average, we long the given stock accordingly. Vice versa.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/MACD%20Oscillator%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/macd%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/macd%20oscillator.png)

### 2. Pair trading

Pair trading is the basic form of statistics arbitrage. It relies on the assumption that two cointegrated stocks would not drift too far away from each other. First step, we select two stocks and run <a href=https://en.wikipedia.org/wiki/Error_correction_model#Engle_and_Granger_2-step_approach>Engle-Granger two step analysis</a>. Once the criteria of cointegration is met, we standardize the residual and set one sigma away (two tailed) as the threshold. After that, we compute the current standardized residual of the selected stocks accordingly. When the standardized residual exceeds the threshold, it generates the trading signal. The simple rule is we always long the cheap stock and short the expensive stock. 

The core idea of pair trading is <a href=https://en.wikipedia.org/wiki/Cointegration>cointegration</a>. Metaphorically speaking, cointegration is like a couple in a clingy relationship where two parties are crazy-glued together. Yet, most relationships break sooner or later, and only the very few can make it to the marriage (from a statistics perspective, not being pessimistic). Hence, it is important to frequently check on the status quo of cointegration before any pair trading order execution (the same applies to relationships).

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Pair%20trading%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/pair%20trading%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/pair%20trading%20asset.png)

### 3. Heikin-Ashi candlestick

Heikin-Ashi, the exotic name actually referring to 'Average Bar' in Japanese, is an alternative style of candlestick chart. The sophisticated rules of Heiki-Ashi are designed to filter out the noise for momentum trading. Hence, Heikin-Ashi shows more consecutive bars in contrast to the standard candlestick, which makes price momentum and reverse points more distinguishable in figures. Arguably it should outperform the standard candlestick in sideways and choppy markets. 

For the strategy itself, initially we make a few transformations on four vital benchmarks - Open, Close, High, Low. The next step is to apply unique Heikin-Ashi rules on Heikin-Ashi Open, Close, High, Low to generate trading signals. The downside of Heikin-Ashi (or any momentum trading strategies) is the slow response. Thus, we should set up the stop loss position accordingly so that we don't get caught up in any flash crash.

The rules of Heikin-Ashi can be found in <a href=https://quantiacs.com/Blog/Intro-to-Algorithmic-Trading-with-Heikin-Ashi.aspx>Quantiacs</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Heikin-Ashi%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/heikin-ashi%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/heikin-ashi%20asset%20value.png)

### 4. London Breakout

To one of my favourite cities in the world! Proud to be a Londoner!

London Breakout is an intra daily opening range breakout strategy. Basically, it is a fascinating information arbitrage across different markets in different time zones. FX market runs 24/7 globally. For instance, you cannot long the stock of Ford in ASX simply because Ford is listed in NYSE. As FX market is decentralised, you can long any currency pair in any market as long as the market is open. That leaves a door to take a peek at the activity in a closed foreign FX market before the opening of domestic FX market.

Back to London Breakout, London and Tokyo are two of the largest FX markets in the world. Tokyo FX trading hour is GMT 0:00 a.m. - GMT 8:59am. London FX trading hour (no summer daylight saving) begins at GMT 8:00 a.m. Even though there is an hour of overlap, the crucial timeframe of London Breakout is GMT 7:00 a.m. - GMT 7:59 a.m. a.k.a. the last trading hour before the opening of London market. The price movement of the crucial timeframe incorporates the information of all the overnight activities of financial market (from the perspective of the current time zone).

For the strategy itself, we establish upper and lower thresholds prior to the high and low of the crucial timeframe. Once London FX market opens, we spend the first couple of minutes to check if the price would breach the preset boundaries. If it is above threshold, we long the currency pair accordingly. Vice versa. Nevertheless, we should set up a limit to prevent us from trading in the case of abnormal opening volatility. Normally, we clear our positions based on our target stop loss or stop profit respectively. By the end of the trading hour (still from the perspective of the current time zone), if there are any open positions, we clear them out.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/London%20Breakout%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/london%20breakout%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/london%20breakout%20thresholds.png)

### 5. Awesome oscillator

Awesome oscillator is an upgraded version of MACD oscillator. It is one of those momentum strategies focusing on the game of moving average. Instead of taking simple moving average on close price, awesome moving average is derived from the mean of high and low price. Similar to MACD oscillator, it takes both short term and long term moving averages to construct the oscillator.

There are various strategies for awesome oscillator to generate signals, such as traditional moving average divergence, twin peaks and saucer. Twin peaks is just one of the many names of bottom W pattern. The pattern recognition will be covered in another chapter so the main focus of this chapter is saucer. Saucer is slightly more complex to implement than the traditional divergence. In return, saucer has the power to beat the slow response of the traditional divergence. Generally speaking, a faster response may sound awesome, but it does not guarantee a less risky outcome or a more profitable outcome. Hence, we will take MACD oscillator as a control group, to test if awesome oscillator can actually outperform MACD oscillator.

The rules of awesome oscillator could be found in <a href=https://www.tradingview.com/wiki/Awesome_Oscillator_(AO)>TradingView</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Awesome%20Oscillator%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20oscillator.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20ma.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20asset.png)

### 6. Oil Money project

This project is inspired by an <a href=https://www.bloomberg.com/news/articles/2018-05-20/crude-oil-s-surge-is-putting-the-petro-back-in-petrocurrencies>article</a> on oil-backed foreign exchange. Amid the bullish outlook for crude oil, the currency exchange of oil producing countries would also bounce back. Does this statement really hold? 

According to the article by Bloomberg (or many other similar research), researchers examine the correlation between petrocurrency and oil price, instead of the causality. But correlation does not equal to causality. Correlation could be a coincidence of a math game. We simply cannot draw the conclusion that oil price moves the currency. Some researchers even use bootstrapping which greatly destroys the autocorrelation of a time series. Thus, it is vital to apply academic analysis and computer simulation on some petrocurrencies to test the causality of oil.

*For more details, please refer to the <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Oil%20Money%20project/README.md>read me page</a> of a separate directory or <a href=https://je-suis-tm.github.io/quant-trading/oil-money>quant trading section</a> on my personal blog.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/Oil%20Money%20project/preview/oil%20production%20bubble%20map.png)

### 7. Dual Thrust

If you search dual thrust on google, you will end up with results of rocket engine. Don't panic yet, you can rest assured that dual thrust strategy is nowhere near rocket science. It is just an opening range breakout strategy developed by the founder of Universal Technical Systems. The mathematics involved in this strategy is merely primary school level.

Initially we establish upper and lower thresholds based on previous days' open, close, high and low. When the market opens and the price exceeds certain thresholds, we would take long/short positions prior to upper/lower thresholds. The strategy is quite useful in intra daily trading. However, there is no stop loss/profit position in this strategy. We reverse our positions when the price goes from one threshold to the other. We need to clear all positions by the end of the day.

Rules of dual thrust can be found in <a href=https://www.quantconnect.com/tutorials/dual-thrust-trading-algorithm>QuantConnect</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Dual%20Thrust%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/dual%20thrust%20positions.png)

### 8. Parabolic SAR

Parabolic SAR is an indicator to identify stop and reverse of a trend. Usually, Parabolic SAR is presented as dotted line either above or below the price in charts. When the price is an uptrend, SAR curve would sit below the price. When the price is downtrend, SAR curve would rise above the price. Parabolic SAR is always considered as a symbol of resistance to the price momentum. When SAR curve and the price curve cross over, it is when trade orders are supposed to be executed. 

The building of this strategy seems very simple, but the construction of the indicator is extremely painful due to the involvement of recursive calculation. Illustration on how to compute Parabolic SAR can be found in <a href=https://en.wikipedia.org/wiki/Parabolic_SAR>Wikipedia</a> but it is not very well explained. To get a clear idea of the calculation, my personal recommendation is to take a look at the <a href=https://www.box.com/s/gbtrjuoktgyag56j6lv0>spreadsheet</a> made by joeu2004.

It is worth mentioning that SAR and RSI (which will be featured in a later chapter) shares the same founder, Welles Wilder. The guy is a real legend who used to work as mechanical engineer and real estate developer and later became a technical analyst. His book on technical trading system is a must-read for anyone that wants to elevate quant trading system to the next level.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Parabolic%20SAR%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/parabolic%20sar%20positions.png)

### 9. Bollinger Bands Pattern Recognition

Bollinger Bands is a very simple but powerful indicator. There are three bands of this indicator. The mid band is the moving average on the price series (usually takes 20 lags). The upper and lower bands are two moving standard deviations away from the mid band. Bollinger Bands can be used to test for various types of strategies. 

For volatility trading, contraction and expansion of the band width are crucial elements. Any distinct momentum clustering (it can take form of either upward or downward) would result in a Bollinger Bands expansion. And the oscillation in a horizontal channel would result in a Bollinger Bands contraction. 

For momentum trading, the phenomenon of 'walking the band' indicates the resistance and support level of the underlying asset. In a strong trend, the price constantly attempts to touch or break through the upper/lower band along with Bollinger Bands moving towards the same direction.

For pattern recognition, Bollinger Bands has the capability of testing bottom W, top M, head-shoulder patterns, etc. With upper and lower bands served as an interval, it is easier to identify the hidden pattern in the historical data.

More details of Bollinger Bands can be found in <a href=https://www.tradingview.com/wiki/Bollinger_Bands_(BB)>TradingView</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Bollinger%20Bands%20Pattern%20Recognition%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/bollinger%20bands%20positions.png)

### 10. Relative Strength Index Pattern Recognition

RSI (Relative Strength Index) is also a popular indicator. It reflects the current strength/weakness of the stock price momentum. The calculation is pretty straight forward. We use 14 days of smoothed moving average (or other moving average methods) to separately calculate the intra daily uptrend and downtrend. We denote uptrend moving average divided by downtrend moving average as the relative strength. We normalize the relative strength by 100 which becomes an index called RSI. It is commonly believed that RSI above 70 is overbought and RSI below 30 is oversold. This is the simplest way to trade on RSI (as shown in the pictures below). Nonetheless, there could be divergence between RSI momentum and price momentum which will not be covered in the script. The effectiveness of any divergence strategy on RSI is rather debatable.

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20oscillator.png)

If you are looking for something slightly more complex, well, we can apply pattern recognition technique to RSI as well. Unlike strategy No.9 Bollinger Bands, we can directly look at the patterns of RSI itself instead of the price. Since we have tested double bottom pattern in Bollinger Bands, we would test head-shoulder pattern on RSI this time.

For details of head-shoulder pattern, please refer to <a href=https://www.investopedia.com/terms/h/head-shoulders.asp>Investopedia</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/RSI%20Pattern%20Recognition%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20pattern%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20pattern%20oscillator.png)

### 11. Monte Carlo project

Monte Carlo, my first thought on these two words is the grand casino, where you meet Famke Janssen in tuxedo and introduce yourself, 'Bond, James Bond'. Indeed, the simulation is named after the infamous casino. It actually refers to the computer simulation of massive amount of random events. This unconventional mathematical method is extremely powerful in the study of stochastic process. 

Here comes the argument on Linkedin that caught my eyes the other day. "Stock price can be seemed as a Wiener Process. Hence, we can use Monte Carlo simulation to predict the stock price." said a data science blog. Well, in order to be a Wiener Process, we have to assume the stock price is continuous in time. In reality, the market closes. The overnight volatility exists. But that is not the biggest issue here. The biggest issue is, can we really use Monte Carlo simulation to predict the stock price, even a range or its direction?

*For more details, please refer to the <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Monte%20Carlo%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/quant-trading/monte-carlo>quant trading</a> section on my personal blog.*

![alt text](https://raw.githubusercontent.com/je-suis-tm/quant-trading/master/Monte%20Carlo%20project/preview/ge%20simulation2.png)

### 12. Options Straddle

Here marks the debut of options strategy in this repository. Straddle refers to the shape of compasses in the payoff diagram of the strategy. A long straddle involves buying a call option and a put option at the same strike price, the same expiration date and preferably the same price. In reality, the same price is not always feasible (call options price higher implies higher upside risk, vice versa). It is recommended to trade when the price disparity between call and put options is converging.

Long straddle is commonly seen in event driven strategy, e.g. political referendum, company earning release. It profits from the uncertainty of both-side risk. For upside risk, the potential profit is unlimited. The potential loss does not come from the downside risk (there is limited gain from downside risk). Instead, it comes from the stagnant price due to insufficient volatility. In this case, short straddle is more suitable for sideways choppy market.

The crucial element of options straddle is the selection of the strike price. As the price of options contains the market consensus, the only way to maximize the profit is to find the optimal strike price to shrink the loss bandwidth. This is where the economists kick in and offer base case outlook plus best/worst scenarios. In contrast to the common misunderstanding of quantitative trading, Option Greeks are no silver bullet. Quantitative combined with fundamental in one, so-called quantamental, makes the portfolio impeccable.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Options%20Straddle%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/options%20straddle%20payoff%20diagram.png)

### 13. Portfolio Optimization project

Modern portfolio theory was introduced in 1952 by Nobel laureate Harry Markowitz. It is part of investment class 101. But I watched a video by <a href=https://www.wolfram.com/training/videos/FIN015>Wolfram</a> recently. It challenged the traditional approach and introduced graph theory to asset diversification. There are plenty of quant shops deploying fancy mathematic tools to solve the market. The real question for us is, as fancy as it sounds, does graph theory work on portfolio optimization?

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Portfolio%20Optimization%20project/preview/outta%20sample%20mean%20variance.png)

*This project is documented in the repository of <a href=https://github.com/je-suis-tm/graph-theory>Graph Theory</a>. For more details, please refer to the <a href=https://github.com/je-suis-t
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `Ore Money project/iron ore production/iron ore production bubble map.py`
```python
# coding: utf-8

# In[1]:


#installing basemap is pretty painful for anaconda
#try conda install -c conda-forge basemap
#if there is filenotfounderror
#try conda install -c conda-forge proj4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
os.chdir('d:/')


# In[2]:


#need data with value and coordinates to plot
#the iron ore production data of 2015 comes from wikipedia
# https://en.wikipedia.org/wiki/List_of_countries_by_iron_ore_production
#the coordinates of each country's capital come from someone's personal blog
# https://lab.lmnixon.org/4th/worldcapitals.html
#note that the capital doesnt necessarily locate at the centre of a country
#to make the figure look better, i slightly change the coordinates
df=pd.read_csv('iron ore production bubble map.csv')


# In[3]:


ax=plt.figure(figsize=(50,20)).add_subplot(111)

#draw up a world map
#fill continents, lakes and country boundaries
m = Basemap()
m.drawmapboundary(fill_color='white', linewidth=0)
m.fillcontinents(color='#c0c0c0',alpha=0.5, lake_color='white')
m.drawcountries(linewidth=1,color='#a79c93')

size=df['iron ore production']/max(df['iron ore production'])*40000

#this is crucial if we use a different map projection
x,y=m(df['longitude'].tolist(),df['latitude'].tolist())

m.scatter(x,y, s=size, linewidths=2, edgecolors="#6c6b74",           
          alpha=0.8,c=df['iron ore production'],cmap='autumn_r')

for i in range(len(x)):
    plt.text(x[i],y[i],               
             '%s '%(df['region'][i]),              
             horizontalalignment='center', 
            verticalalignment='center', 
             size=25)

cb=plt.colorbar(ticks=[10000,800000])
cb.ax.set_yticklabels(cb.ax.get_yticklabels(), fontsize=20)
cb.ax.set_ylabel('Iron Ore Production 1000 Tonnes per Year',fontsize=20,rotation=270)
plt.title('Iron Ore Production by Countries', fontsize=42)

plt.show()
```

#### File: `Oil Money project/oil production/oil production choropleth.py`
```python
# coding: utf-8

# In[1]:


import folium
import os
os.chdir('h:/')
import pandas as pd


# In[2]:


#this table comes from wikipedia
# https://en.wikipedia.org/wiki/List_of_countries_by_oil_production
#but i have changed the names of some countries
#try to keep names consistent with geojson file
df=pd.read_csv('oil production choropleth.csv')


# In[3]:


df['Oil Production']=df['Oil Production'].apply(lambda x: x/1000)


# In[4]:


#location takes two arguments, latitude and longitude
#zoom_start implies zoom level
#1 is world map, 2 is continent map, 3 is region map
#4 is country map, 5 is county map etc
m=folium.Map(location=(30,50), zoom_start=4)

#geo_data is a geojson file
#its a file that indicates country shape on a map
#we can download country and even more detailed level from the first link
#the second link converts all the files in first link to geojson
#https://gadm.org/download_country_v3.html
#https://mapshaper.org/
#here i found the map shape from github
#i just cannot find the original link
#so i just upload it to the repo

#data is the dataframe
#columns would be the columns we use in that dataframe
#we need one column for the region name and the other one for value
#the region name should be consistent with the region name in geojson
#and key_on denotes the key in geojson for region names
#fill_color is just matplotlib cmap
#fill_opacity,line_opacity are plotting options
#legend_name is just the name of the label in matplotlib
#threshold_scale can only take up to six values in a list
#for simplicity, we can use from branca.utilities import split_six
#to get the quantile data equally divided into six parts
m.choropleth(
 geo_data=(open("worldmapshape.json",encoding = "utf_8_sig").read()),
 name='choropleth',
 data=df,
 columns=['Country', 'Oil Production'],
 key_on='properties.name',
 fill_color='YlOrRd',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Oil Production Thousand Barrels/Day',
 threshold_scale=[0.0,1.0, 150.0, 800.0, 2000.0, 4000.0]
)

#layout control is just a map filter
#we can unselect choropleth any time
folium.LayerControl().add_to(m)
display(m)

#in general, folium is a really good wrap up for leaflet.js
#it saves me a lot of time from learning javascript
#it is very straight forward, a very flat learning curve
#there is only one thing i hate about it
#which is the location name is always in local language
#at least google map provides english plus local language
#this is quite annoying, other than that, its pretty cool
```

#### File: `Smart Farmers project/check consistency.py`
```python
# coding: utf-8

# In[1]:


import os
os.chdir('H:/')
import pandas as pd


# In[2]:


prod=pd.read_csv('Production_Crops_E_All_Data_(Normalized).csv',
                 encoding='latin-1')

prix=pd.read_csv('Prices_E_All_Data_(Normalized).csv',
                 encoding='latin-1')

land=pd.read_csv('Inputs_LandUse_E_All_Data_(Normalized).csv',
                 encoding='latin-1')


# In[3]:


global beginyear,endyear
beginyear=2012;
endyear=2019


# In[4]:


mapping=pd.read_csv('mapping.csv')


# In[5]:


#select malaysia from 2012-2018
malay_land=land[land['Year'].isin(range(beginyear,endyear))][land['Area']=='Malaysia'][land['Element'].isin(['Area'])][land['Item'].isin(['Cropland'])]

malay_prod=prod[prod['Year'].isin(range(beginyear,endyear))][prod['Area']=='Malaysia'][prod['Element'].isin(['Area harvested','Production'])]

malay_prod=malay_prod.merge(mapping,on=['Item Code', 'Item'],how='left')


# In[6]:


#remove redundant cols
for i in ['Area Code','Element Code','Year Code',
         'Flag','COMMODITY','Item Code',
          'subclass code','class code',
          'DEFINITIONS, COVERAGE, REMARKS',]:
    del malay_prod[i]


# In[7]:


#select crops with available data
a=set(malay_prod['Item'][malay_prod['Element']=='Area harvested'])

b=set(malay_prod['Item'][malay_prod['Element']=='Production'])

target_crops=a.intersection(b)


# In[8]:


#exclude land usage<1% without price data
exclude=['Areca nuts',
 'Bastfibres, other',
 'Cashew nuts, with shell',
 'Cereals, Total',
 'Chillies and peppers, dry',
 'Citrus Fruit, Total',
 'Cloves',
 'Coarse Grain, Total',
 'Coffee, green',
 'Coir',
 'Fibre Crops Primary',
 'Fruit Primary',
 'Fruit, citrus nes',
 'Fruit, fresh nes',
 'Fruit, tropical fresh nes',
 'Groundnuts, with shell',
 'Manila fibre (abaca)',
 'Nutmeg, mace and cardamoms',
 'Oilcrops',
 'Oilcrops, Cake Equivalent',
 'Oilcrops, Oil Equivalent',
 'Roots and Tubers, Total',
 'Roots and tubers nes',
 'Soybeans',
 'Spices nes',
 'Tea',
 'Treenuts, Total',
 'Vegetables Primary',
 'Vegetables, fresh nes']


# In[9]:


#finalize the target
targets=[i for i in target_crops if i not in exclude]


# In[10]:


#cleanse
malay_crops=malay_prod[malay_prod['Item'].isin(targets)]


# In[11]:


#subtotal
total=malay_prod[malay_prod['class'].isnull()]


# In[12]:


#compare sum of area by crops with sum of area by subclass
sss=total[total['Element']=='Area harvested'].groupby(['Item','Year']).sum()

ttt=malay_crops[malay_crops['Element']=='Area harvested'].groupby(['class','Year']).sum()


# In[13]:


#compare sum of area by crops
malay_crops[malay_crops['Element']=='Area harvested'].groupby(['Year']).sum()


# In[14]:


#with cropland
malay_land
```

#### File: `Smart Farmers project/country selection.py`
```python
# coding: utf-8

# In[1]:


target_country=['Australia','Spain',
 'Morocco',
 'United Kingdom',
 'Poland',
 'France',
 'Mexico',
 'Bangladesh',
 'Canada',
 'Viet Nam',
 'Thailand',
 'Guatemala',
 'Colombia',
 'Germany',
 'China',
 'Brazil',
 'India',
 'United States of America',
 'Malaysia',
 'Indonesia']


# In[2]:


target_year=[2000,
 2001,
 2002,
 2003,
 2004,
 2005,
 2006,
 2007,
 2008,
 2009,
 2010,
 2011,
 2012,
 2013,
 2014,
 2015,
 2016,
 2017]


# In[3]:


import pandas as pd
import numpy as np
import os
os.chdir('H:/')


# In[4]:


prod=pd.read_csv('Production_Crops_E_All_Data_(Normalized).csv',encoding='latin-1')


# In[5]:


prix=pd.read_csv('Prices_E_All_Data_(Normalized).csv',encoding='latin-1')


# In[6]:


echanger=pd.read_csv('Trade_Crops_Livestock_E_All_Data_(Normalized).csv',encoding='latin-1')


# In[7]:


#only compare crops with available data
target_crops=set(prod['Item']).intersection(set(prix['Item'])).intersection(set(echanger['Item']))


# # volume

# In[8]:


#extract export volume
trade=echanger[echanger['Element']=='Export Quantity']


# In[9]:


#cleanse
trade=trade[trade['Item'].isin(target_crops)]

trade=trade[trade['Area'].isin(target_country)]

trade=trade[trade['Year'].isin(target_year)]

trade=trade[['Area','Year','Item','Value']]


# In[10]:


#extract production data
prod=prod[prod['Element']=='Production']


# In[11]:


#cleanse
prod=prod[prod['Item'].isin(target_crops)]

prod=prod[prod['Area'].isin(target_country)]

prod=prod[prod['Year'].isin(target_year)]

prod=prod[['Area','Year','Item','Value']]


# In[12]:


#group by sum
export=trade.groupby(['Area','Year']).sum()


# In[13]:


#group by sum
supply=prod.groupby(['Area','Year']).sum()


# In[14]:


#create new dataframe to compute export volume percentage
pourcent=pd.DataFrame(index=export.index)


# In[15]:


#compute percentage
pourcent['value']=np.divide(export['Value'].tolist(),supply['Value'].tolist())


# In[16]:


#clean up index
pourcent.reset_index(inplace=True)


# In[17]:


#historical average
mean_pourcent=pourcent[['Area','value']].groupby('Area').mean()


# In[18]:


#sort by percentage
mean_pourcent=mean_pourcent.sort_values('value')


# In[19]:


#export percentage for a particular year
pourcent[pourcent['Year'].isin([2017])].sort_values('value')


# # price

# In[20]:


#get usd price
prix=prix[prix['Element']=='Producer Price (USD/tonne)']


# In[21]:


#cleanse
prix=prix[prix['Item'].isin(target_crops)]

prix=prix[prix['Area'].isin(target_country)]

prix=prix[prix['Year'].isin(target_year)]

prix=prix[['Area','Year','Item','Value']]


# In[22]:


#previously we examine the volume
#now we focus on value
value=prod.merge(prix,on=['Area','Year','Item'],how='inner')


# In[23]:


#volume times unit price equals to total value
value['Value']=np.multiply(value['Value_x'],value['Value_y'])


# In[24]:


#cleanse
value=value[['Area','Year','Item','Value']]


# In[25]:


#get export price
exchange=echanger[echanger['Element']=='Export Value']


# In[26]:


#cleanse
exchange=exchange[exchange['Item'].isin(target_crops)]

exchange=exchange[exchange['Area'].isin(target_country)]

exchange=exchange[exchange['Year'].isin(target_year)]

exchange=exchange[['Area','Year','Item','Value']]


# In[27]:


#group by sum
temp1=exchange.groupby(['Area','Year']).sum()


# In[28]:


#group by sum
temp2=value.groupby(['Area','Year']).sum()


# In[29]:


#inner join
temp=temp1.merge(temp2,on=['Area','Year'],how='inner')


# In[30]:


#create dataframe to compute export value percentage
percentage=pd.DataFrame(index=temp.index)


# In[31]:


#compute export value percentage
percentage['value']=np.divide(temp['Value_x'],temp['Value_y'])


# In[32]:


#clean up
percentage.reset_index(inplace=True)


# In[33]:


#historical average
mean_percentage=percentage[['Area','value']].groupby('Area').mean()


# In[34]:


#sort by percentage
mean_percentage=mean_percentage.sort_values('value')


# In[35]:


#export percentage for a particular year
percentage[percentage['Year'].isin([2016])].sort_values('value')
```

#### File: `MACD Oscillator backtest.py`
```python
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:57:46 2018

@author: Administrator
"""

# In[1]:

#need to get fix yahoo finance package first

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fix_yahoo_finance as yf



# In[2]:

#simple moving average
def macd(signals):
    
    
    signals['ma1']=signals['Close'].rolling(window=ma1,min_periods=1,center=False).mean()
    signals['ma2']=signals['Close'].rolling(window=ma2,min_periods=1,center=False).mean()
    
    return signals



# In[3]:

#signal generation
#when the short moving average is larger than long moving average, we long and hold
#when the short moving average is smaller than long moving average, we clear positions
#the logic behind this is that the momentum has more impact on short moving average
#we can subtract short moving average from long moving average
#the difference between is sometimes positive, it sometimes becomes negative
#thats why it is named as moving average converge/diverge oscillator
def signal_generation(df,method):
    
    signals=method(df)
    signals['positions']=0

    #positions becomes and stays one once the short moving average is above long moving average
    signals['positions'][ma1:]=np.where(signals['ma1'][ma1:]>=signals['ma2'][ma1:],1,0)

    #as positions only imply the holding
    #we take the difference to generate real trade signal
    signals['signals']=signals['positions'].diff()

    #oscillator is the difference between two moving average
    #when it is positive, we long, vice versa
    signals['oscillator']=signals['ma1']-signals['ma2']

    return signals



# In[4]:

#plotting the backtesting result
def plot(new, ticker):
    
    #the first plot is the actual close price with long/short positions
    fig=plt.figure()
    ax=fig.add_subplot(111)
    
    new['Close'].plot(label=ticker)
    ax.plot(new.loc[new['signals']==1].index,new['Close'][new['signals']==1],label='LONG',lw=0,marker='^',c='g')
    ax.plot(new.loc[new['signals']==-1].index,new['Close'][new['signals']==-1],label='SHORT',lw=0,marker='v',c='r')

    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Positions')
    
    plt.show()
    
    #the second plot is long/short moving average with oscillator
    #note that i use bar chart for oscillator
    fig=plt.figure()
    cx=fig.add_subplot(211)

    new['oscillator'].plot(kind='bar',color='r')

    plt.legend(loc='best')
    plt.grid(True)
    plt.xticks([])
    plt.xlabel('')
    plt.title('MACD Oscillator')

    bx=fig.add_subplot(212)

    new['ma1'].plot(label='ma1')
    new['ma2'].plot(label='ma2',linestyle=':')
    
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

    
# In[5]:

def main():
    
    #input the long moving average and short moving average period
    #for the classic MACD, it is 12 and 26
    #once a upon a time you got six trading days in a week
    #so it is two week moving average versus one month moving average
    #for now, the ideal choice would be 10 and 21
    
    global ma1,ma2,stdate,eddate,ticker,slicer

    #macd is easy and effective
    #there is just one issue
    #entry signal is always late
    #watch out for downward EMA spirals!
    ma1=int(input('ma1:'))
    ma2=int(input('ma2:'))
    stdate=input('start date in format yyyy-mm-dd:')
    eddate=input('end date in format yyyy-mm-dd:')
    ticker=input('ticker:')

    #slicing the downloaded dataset
    #if the dataset is too large, backtesting plot would look messy
    #you get too many markers cluster together
    slicer=int(input('slicing:'))

    #downloading data
    df=yf.download(ticker,start=stdate,end=eddate)
    
    new=signal_generation(df,macd)
    new=new[slicer:]
    plot(new, ticker)


#how to calculate stats could be found from my other code called Heikin-Ashi
# https://github.com/je-suis-tm/quant-trading/blob/master/heikin%20ashi%20backtest.py


if __name__ == '__main__':
    main()
```

#### File: `Oil Money project/oil production/oil production cost curve.py`
```python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:/')
import pandas as pd


# In[2]:


#traditional commodity cost curve
#input two pandas series, the third one is optional
def cost_curve(x,y1,y2=None,
               hline_var=0,hline_color='k',hline_name='',
               colormap='tab20c',legends=None,notes=None,
               ylabel='',xlabel='',title='',fig_size=(10,5)):
    y2 = [] if y2 is None else y2
    legends = [] if legends is None else legends
    notes = [] if notes is None else notes
    
    ax=plt.figure(figsize=fig_size).add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    #set bar location on x axis
    wid=x
    cumwid=[0]
    for i in range(1,len(wid)):
        cumwid.append(wid[i-1]+cumwid[-1])

    #assign colors to different bars from cmap
    cmap=plt.cm.get_cmap(colormap)
    colors=[cmap(i) for i in np.linspace(0,1,len(y1))]
    colors2=[tuple([i/1.3 for i in j if i!=1]+[1.0]) for j in colors]
    
    for i in range(len(y1)):
        plt.bar(cumwid[i],            
                y1[i],width=wid[i],label=legends[i] if len(legends)>0 else '',
                   color=colors[i],align='edge')
        
        if len(y2)>0:
            plt.bar(cumwid[i],            
                    y2[i],width=wid[i],
                   color=colors2[i],bottom=y1[i],align='edge'
                   )
    
    #plot percentile line if needed
    plt.axhline(y=hline_var, linestyle='--',
                c=hline_color,label=hline_name)

    plt.title(title,pad=20)
    ax.yaxis.labelpad=10
    ax.xaxis.labelpad=10
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    #slightly expand x axis to look nicer
    plt.xlim(min(cumwid),max(cumwid)+list(wid)[-1])
    plt.xticks([min(cumwid),
                np.mean([min(cumwid),
                         max(cumwid)+list(wid)[-1]]),
                1.01*max(cumwid)+list(wid)[-1]])
    
    #if cost curve breakdown is provided
    #add legends to the right
    if len(y2)>0:
        plt.text(1.1*max(cumwid)+list(wid)[-1],
             list(y1)[-1]/2,notes[0],
                 verticalalignment='center', horizontalalignment='center')
        plt.text(1.1*max(cumwid)+list(wid)[-1],
             list(y1)[-1]+list(y2)[-1]/2,notes[1],
                verticalalignment='center', horizontalalignment='center')
    
    #legends of cost curve for different entities is plotted below the chart
    plt.legend(loc=6,bbox_to_anchor=(0.12, -0.4), ncol=4)    
    
    plt.show()
    


# In[3]:

#why there is only 2015 data?
#well, they said data is the new oil
#especially true when it comes to oil data

#i can only find oil production cost data of 2015 from the below address
# https://www.statista.com/statistics/597669/cost-breakdown-of-producing-one-barrel-of-oil-in-the-worlds-leading-oil-producing-countries/
#and i have to do some scraping to actually get the data
#if u dont know scraping, that will be a problem
#data scientists cant wait for engineers to feed you data
#maybe its time for you to learn
# https://github.com/je-suis-tm/web-scraping

#also you can use oil breakeven price to replace cost data
#the following two links contain quite a lot of information
#sadly, fiscal breakeven price is widely used by opec countries
#if u have other countries in mind, you will be disappointed
# https://www.cfr.org/report/interactive-oil-exporters-external-breakeven-prices
# http://graphics.wsj.com/oil-barrel-breakdown/

#daily production data and proven reserve comes from bp
# https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html
#production capacity is a typical x axis for cost curve
#you can find them from imf or eia, but again, only for opec countries
#therefore, i used daily production data as alternative
# https://www.imf.org/~/media/Files/Publications/REO/MCD-CCA/2018/May/English/mreo0518-statisticalappendix-elsx.ashx
# https://www.eia.gov/opendata/qb.php?sdid=STEO.COPC_AG.A

df=pd.read_csv('global oil cost curve.csv')


# In[4]:


cost_curve(df['Daily production mil barrels'],
           df['Operational cost dollar per barrel'],
           df['Capital cost dollar per barrel'],
           legends=df['Country'],
           notes=['Operational Cost','Capital Cost'],
           hline_var=np.percentile(df['Total cost dollar per barrel'],90),
           hline_color='#e08314',
           hline_name='90% Percentile',
           xlabel='Daily Production, Million Barrels',
           ylabel='US Dollar per Barrel',
           title='2015 Global Oil Cost Curve')
```


==================================================
