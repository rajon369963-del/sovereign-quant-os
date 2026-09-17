# ⚡ [QUANT-SOURCE-113] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_113_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: tradingagents (`WHEEL_tradingagents`)
- **Full Name**: `tradingagents`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
  <img src="assets/TauricResearch.png" style="width: 60%; height: auto;">
</p>

<div align="center" style="line-height: 1;">
  <a href="https://arxiv.org/abs/2412.20138" target="_blank"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2412.20138-B31B1B?logo=arxiv"/></a>
  <a href="https://discord.com/invite/hk9PGKShPK" target="_blank"><img alt="Discord" src="https://img.shields.io/badge/Discord-TradingResearch-7289da?logo=discord&logoColor=white&color=7289da"/></a>
  <a href="https://x.com/TauricResearch" target="_blank"><img alt="X Follow" src="https://img.shields.io/badge/X-TauricResearch-white?logo=x&logoColor=white"/></a>
  <a href="https://github.com/TauricResearch/" target="_blank"><img alt="Community" src="https://img.shields.io/badge/GitHub_Community-TauricResearch-14C290?logo=discourse"/></a>
</div>
<br>
<div align="center">
  <a href="https://github.com/TauricResearch" target="_blank"><img alt="TradingAgents #1 Repository of the Day" src="https://trendshift.io/api/badge/repositories/16192" width="250" height="55"/></a>
</div>
<br>
<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=de">Deutsch</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=es">Español</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=fr">français</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ja">日本語</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ko">한국어</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=pt">Português</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=ru">Русский</a> | 
  <a href="https://www.readme-i18n.com/TauricResearch/TradingAgents?lang=zh">中文</a>
</div>

---

# TradingAgents: Multi-Agents LLM Financial Trading Framework

## News
- [2026-08] **TradingAgents v0.4.0** released with look-ahead / point-in-time fixes across FRED macro, social sentiment, and the decision-log memory; clearer decision signals; working CLI checkpoint resume; Trader price grounding; and the GPT-5.6 and GLM-5.3 models. See [CHANGELOG.md](CHANGELOG.md) for the full list.
- [2026-07] **TradingAgents v0.3.1** released with correctness and stability fixes: Alpha Vantage look-ahead filtering, graph-router crash-safety, graph-shape-aware checkpoint resume, working crypto sentiment sources, a configurable LLM retry budget, Bedrock API-key auth, and Claude Sonnet 5 / Fable 5 support.
- [2026-06] **TradingAgents v0.3.0** released with a verified data-access contract, an expanded provider registry (NVIDIA, Kimi, Groq, Mistral, Bedrock, and any OpenAI-compatible endpoint), FRED and Polymarket data vendors, a current-generation model catalog, and a CI gate.
- [2026-05] **TradingAgents v0.2.5** released with the grounded Sentiment Analyst, GPT-5.5 etc. model coverage, Qwen/GLM/MiniMax dual-region support, `TRADINGAGENTS_*` env-var configurability with API-key auto-detection, remote Ollama support, non-US alpha benchmarks, and ticker path-traversal hardening.
- [2026-04] **TradingAgents v0.2.4** released with structured-output agents (Research Manager, Trader, Portfolio Manager), LangGraph checkpoint resume, persistent decision log, DeepSeek/Qwen/GLM/Azure provider support, Docker, and a Windows UTF-8 encoding fix.
- [2026-03] **TradingAgents v0.2.3** released with multi-language support, GPT-5.4 family models, unified model catalog, backtesting date fidelity, and proxy support.
- [2026-03] **TradingAgents v0.2.2** released with GPT-5.4/Gemini 3.1/Claude 4.6 model coverage, five-tier rating scale, OpenAI Responses API, Anthropic effort control, and cross-platform stability.
- [2026-02] **TradingAgents v0.2.0** released with multi-provider LLM support (GPT-5.x, Gemini 3.x, Claude 4.x, Grok 4.x) and improved system architecture.
- [2026-01] **Trading-R1** [Technical Report](https://arxiv.org/abs/2509.11420) released, with [Terminal](https://github.com/TauricResearch/Trading-R1) expected to land soon.

<div align="center">

🚀 [TradingAgents](#tradingagents-framework) | ⚡ [Installation & CLI](#installation-and-cli) | 🎬 [Demo](https://www.youtube.com/watch?v=90gr5lwjIho) | 📦 [Package Usage](#tradingagents-package) | 🤝 [Contributing](#contributing) | 📄 [Citation](#citation)

</div>

> 🎉 **TradingAgents** officially released! We have received numerous inquiries about the work, and we would like to express our thanks for the enthusiasm in our community.
>
> So we decided to fully open-source the framework. Looking forward to building impactful projects with you!

## TradingAgents Framework

TradingAgents is a multi-agent trading framework that mirrors the dynamics of real-world trading firms. By deploying specialized LLM-powered agents: from fundamental analysts, sentiment experts, and technical analysts, to trader, risk management team, the platform collaboratively evaluates market conditions and informs trading decisions. Moreover, these agents engage in dynamic discussions to pinpoint the optimal strategy.

<p align="center">
  <img src="assets/schema.png" style="width: 100%; height: auto;">
</p>

> TradingAgents framework is designed for research purposes. Trading performance may vary based on many factors, including the chosen backbone language models, model temperature, trading periods, the quality of data, and other non-deterministic factors. [It is not intended as financial, investment, or trading advice.](https://tauric.ai/disclaimer/)

Our framework decomposes complex trading tasks into specialized roles.

### Analyst Team
- Fundamentals Analyst: Evaluates company financials and performance metrics, identifying intrinsic values and potential red flags.
- Sentiment Analyst: Aggregates news headlines, StockTwits, and Reddit chatter into a single sentiment read to gauge short-term market mood.
- News Analyst: Monitors global news and macroeconomic indicators, interpreting the impact of events on market conditions.
- Technical Analyst: Utilizes technical indicators (like MACD and RSI) to detect trading patterns and forecast price movements.

<p align="center">
  <img src="assets/analyst.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

### Researcher Team
- Comprises both bullish and bearish researchers who critically assess the insights provided by the Analyst Team. Through structured debates, they balance potential gains against inherent risks.

<p align="center">
  <img src="assets/researcher.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### Trader Agent
- Composes reports from the analysts and researchers to make informed trading decisions, determining the timing and magnitude of trades.

<p align="center">
  <img src="assets/trader.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### Risk Management and Portfolio Manager
- Continuously evaluates portfolio risk by assessing market volatility, liquidity, and other risk factors. The risk management team evaluates and adjusts trading strategies, providing assessment reports to the Portfolio Manager for final decision.
- The Portfolio Manager approves/rejects the transaction proposal. If approved, the order will be sent to the simulated exchange and executed.

<p align="center">
  <img src="assets/risk.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

## Installation and CLI

### Installation

Clone TradingAgents:
```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
```

Create a virtual environment in any of your favorite environment managers:
```bash
conda create -n tradingagents python=3.12
conda activate tradingagents
```

Install the package and its dependencies:
```bash
pip install .
```

### Docker

Alternatively, run with Docker:
```bash
cp .env.example .env  # add your API keys
docker compose run --rm tradingagents
```

For local models with Ollama:
```bash
docker compose --profile ollama run --rm tradingagents-ollama
```

### Required APIs

TradingAgents supports multiple LLM providers. Set the API key for your chosen provider:

```bash
export OPENAI_API_KEY=...          # OpenAI (GPT)
export GOOGLE_API_KEY=...          # Google (Gemini)
export ANTHROPIC_API_KEY=...       # Anthropic (Claude)
export XAI_API_KEY=...             # xAI (Grok)
export DEEPSEEK_API_KEY=...        # DeepSeek
export DASHSCOPE_API_KEY=...       # Qwen — International (dashscope-intl.aliyuncs.com)
export DASHSCOPE_CN_API_KEY=...    # Qwen — China (dashscope.aliyuncs.com)
export ZHIPU_API_KEY=...           # GLM via Z.AI (international)
export ZHIPU_CN_API_KEY=...        # GLM via BigModel (China, open.bigmodel.cn)
export MINIMAX_API_KEY=...         # MiniMax — Global (api.minimax.io)
export MINIMAX_CN_API_KEY=...      # MiniMax — China (api.minimaxi.com)
export OPENROUTER_API_KEY=...      # OpenRouter
export ALPHA_VANTAGE_API_KEY=...   # Alpha Vantage
```

For Azure OpenAI, copy `.env.enterprise.example` to `.env.enterprise` and fill in your credentials.

For AWS Bedrock, install the extra with `pip install ".[bedrock]"`, set `llm_provider: "bedrock"`, configure AWS credentials (environment variables, `~/.aws/credentials`, or an IAM role) and `AWS_DEFAULT_REGION`, and use a Bedrock model ID, e.g. `us.anthropic.claude-opus-4-8-v1:0`.

For local models, configure Ollama with `llm_provider: "ollama"`. The default endpoint is `http://localhost:11434/v1`; set `OLLAMA_BASE_URL` to point at a remote `ollama-serve`. Pull models with `ollama pull <name>`, and pick "Custom model ID" in the CLI for any model not listed by default.

For any other OpenAI-compatible server (vLLM, LM Studio, llama.cpp, or a custom relay), use `llm_provider: "openai_compatible"` and set the endpoint via `backend_url` (or `TRADINGAGENTS_LLM_BACKEND_URL`), e.g. `http://localhost:8000/v1` for vLLM or `http://localhost:1234/v1` for LM Studio. The model is whatever your server serves. No key is needed for local servers; set `OPENAI_COMPATIBLE_API_KEY` when the endpoint requires one.

Alternatively, copy `.env.example` to `.env` and fill in your keys:
```bash
cp .env.example .env
```

### CLI Usage

Launch the interactive CLI:
```bash
tradingagents          # installed command
python -m cli.main     # alternative: run directly from source
```
You will see a screen where you can select your desired tickers, analysis date, LLM provider, research depth, and more.

### Markets and tickers

TradingAgents works with any market Yahoo Finance covers, using the exchange-suffixed ticker. Company identity and the alpha benchmark resolve automatically per market.

- US: `AAPL`, `SPY`
- Hong Kong: `0700.HK` · Tokyo: `7203.T` · London: `AZN.L`
- India: `RELIANCE.NS`, `.BO` · Canada: `.TO` · Australia: `.AX`
- China A-shares: Shanghai `.SS`, Shenzhen `.SZ` (e.g. `600519.SS` for Kweichow Moutai)
- Crypto: `BTC-USD`, `ETH-USD`

<p align="center">
  <img src="assets/cli/cli_init.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

An interface will appear showing results as they load, letting you track the agent's progress as it runs.

<p align="center">
  <img src="assets/cli/cli_news.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

<p align="center">
  <img src="assets/cli/cli_transaction.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

## TradingAgents Package

### Implementation Details

We built TradingAgents with LangGraph to ensure flexibility and modularity. The framework supports multiple LLM providers: OpenAI, Google, Anthropic, xAI, DeepSeek, Qwen (Alibaba DashScope, international and China endpoints), GLM (Zhipu), MiniMax (global + China), OpenRouter, Ollama for local models, and Azure OpenAI for enterprise.

### Python Usage

To use TradingAgents inside your code, you can import the `tradingagents` module and initialize a `TradingAgentsGraph()` object. The `.propagate()` function will return a decision. You can run `main.py`, here's also a quick example:

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# forward propagate
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

You can also adjust the default configuration to set your own choice of LLMs, debate rounds, etc.

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"        # e.g. openai, google, anthropic, deepseek, groq, ollama; openai_compatible covers any OpenAI-compatible endpoint (vLLM, LM Studio, llama.cpp, ...)
config["deep_think_llm"] = "gpt-5.6"      # Model for complex reasoning
config["quick_think_llm"] = "gpt-5.6-luna" # Model for quick tasks
config["max_debate_rounds"] = 2

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

See `tradingagents/default_config.py` for all configuration options.

## Persistence and Recovery

TradingAgents persists two kinds of state across runs.

### Decision log

The decision log is always on. Each completed run appends its decision to `~/.tradingagents/memory/trading_memory.md`. On the next run for the same ticker, TradingAgents fetches the realised return (raw and alpha vs SPY), generates a one-paragraph reflection, and injects the most recent same-ticker decisions plus recent cross-ticker lessons into the Portfolio Manager prompt, so each analysis carries forward what worked and what didn't.

Override the path with `TRADINGAGENTS_MEMORY_LOG_PATH`.

### Checkpoint resume

Checkpoint resume is opt-in via `--checkpoint`. When enabled, LangGraph saves state after each node so a crashed or interrupted run resumes from the last successful step instead of starting over. On a resume run you will see `Resuming from step N for <TICKER> on <date>` in the logs; on a new run you will see `Starting fresh`. Checkpoints are cleared automatically on successful completion.

Per-ticker SQLite databases live at `~/.tradingagents/cache/checkpoints/<TICKER>.db` (override the base with `TRADINGAGENTS_CACHE_DIR`). Use `--clear-checkpoints` to reset all of them before a run.

```bash
tradingagents analyze --checkpoint           # enable for this run
tradingagents analyze --clear-checkpoints    # reset before running
```

```python
config = DEFAULT_CONFIG.copy()
config["checkpoint_enabled"] = True
ta = TradingAgentsGraph(config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
```

## Reproducibility

TradingAgents is LLM-driven, so two runs of the same ticker and date can differ. This is expected for a research tool built on language models, not a defect. The variation comes from a few distinct sources, and it helps to separate them.

Language model sampling is non-deterministic. Even at a fixed temperature, providers do not guarantee byte-identical output across calls, and reasoning models (the default GPT-5.x family, and any thinking-mode model) vary the most because their internal reasoning is itself sampled.

Live data moves. News, StockTwits, and Reddit return different content as time passes, so a run today sees different inputs than a run last week even for the same historical trade date. Pin the analysis date to hold the price and indicator window fixed, but the social and news sources still reflect "now".

To reduce variation you can lower the sampling temperature. Set `temperature` in your config (or `TRADINGAGENTS_TEMPERATURE` in `.env`); lower values make models that honor it more repeatable. The current curated models are reasoning-first and largely ignore temperature, so for tighter reproducibility use a non-reasoning model, which you can set explicitly via the Custom model ID option.

```python
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"
config["temperature"] = 0.0
# Reasoning models ignore temperature. For tighter reproducibility, set a
# non-reasoning deep/quick model explicitly (e.g. via the Custom model ID option).
```

What does not vary anymore: the analyzed company identity is resolved deterministically from the ticker before any agent runs, and the market analyst grounds exact price and indicator claims in a verified data snapshot. Earlier reports of "different companies" or fabricated price levels across runs are addressed by these two mechanisms.

Backtest results are not guaranteed to match any published figure. Returns depend on the model, the temperature, the date range, data quality, and the sampling above. Treat the framework as a research scaffold for studying multi-agent analysis, not as a strategy with a fixed, replicable return.

## Contributing

Contributions are welcome: bug fixes, documentation, and feature ideas; past contributions are credited per release in [`CHANGELOG.md`](CHANGELOG.md).

## Citation

Please reference our work if you find *TradingAgents* provides you with some help :)

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework}, 
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138}, 
}
```

### Core Implementation Code & Architecture
#### File: `cli/__init__.py`
```python

```

#### File: `tradingagents/dataflows/__init__.py`
```python

```

#### File: `tests/__init__.py`
```python

```

#### File: `tradingagents/llm_clients/__init__.py`
```python
from .base_client import BaseLLMClient
from .factory import create_llm_client

__all__ = ["BaseLLMClient", "create_llm_client"]
```

#### File: `cli/config.py`
```python
CLI_CONFIG = {
    # Announcements
    "announcements_url": "https://api.tauric.ai/v1/announcements",
    "announcements_timeout": 1.0,
    "announcements_fallback": "[cyan]For more information, please visit[/cyan] [link=https://github.com/TauricResearch]https://github.com/TauricResearch[/link]",
}
```

#### File: `cli/models.py`
```python
from enum import Enum


class AnalystType(str, Enum):
    MARKET = "market"
    # Wire value stays "social" for saved-config and string-keyed-caller
    # back-compat; the user-facing label is "Sentiment Analyst".
    SOCIAL = "social"
    NEWS = "news"
    FUNDAMENTALS = "fundamentals"


class AssetType(str, Enum):
    STOCK = "stock"
    CRYPTO = "crypto"
```


==================================================


## [2/3] Repository: tradingbots (`WHEEL_tradingbots`)
- **Full Name**: `tradingbots`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Python Trading Bots for NSE/BSE India — Automated Trading Software

Welcome to **Trade Vectors' Trading Bots** repository — a curated collection of automated trading robots, algo trading scripts, and quantitative strategies designed specifically for the **Indian stock market (NSE/BSE)**.

## What Are Trading Bots?

Trading bots (automated trading robots) are software programs that execute buy and sell orders in the stock market automatically, based on pre-defined rules, technical indicators, and algorithmic logic — without requiring manual intervention. They are widely used in NSE F&O, equity, and commodity markets.

## What This Repository Covers

- **Python-based automated trading bots** for NSE and BSE
- **Algo trading scripts** using Zerodha Kite API, Interactive Brokers (IBKR), and other platforms
- **Strategy templates** for index trading (Nifty 50, Bank Nifty)
- **F&O (Futures & Options) automated execution** scripts
- **Risk management modules** for position sizing and stop-loss automation
- **Backtesting frameworks** to test strategies on historical NSE data

## Why Use Automated Trading Bots?

| Benefit | Description |
|---|---|
| Speed | Execute orders in milliseconds, faster than manual trading |
| Discipline | Remove emotions from trading decisions |
| Backtesting | Test strategies on historical data before going live |
| 24/7 Monitoring | Bots can monitor markets continuously |
| Scalability | Run multiple strategies simultaneously |

## Technologies Used

- **Language:** Python 3.x
- **APIs:** Zerodha Kite Connect, Interactive Brokers TWS API, NSE Data APIs
- **Libraries:** pandas, numpy, ta-lib, backtrader, zipline
- **Platforms:** NSE, BSE, MCX

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your broker API credentials
4. Run the strategy of your choice

## About Trade Vectors

**Trade Vectors** is a Mumbai-based algorithmic trading company specializing in automated trading software, quantitative strategies, and algo trading education for NSE/BSE India.

We offer:
- Custom algorithmic trading software development
- Algo trading consulting and strategy research
- Corporate training programs in algorithmic trading (NSE-certified)
- Backtesting and strategy optimization services

Visit **[tradevectors.com](https://tradevectors.com)** to learn more about our services, trading courses, and automated trading solutions.

**Contact:** [tradevectors.com](https://tradevectors.com) | [@tradevectors](https://twitter.com/tradevectors)

---
*Keywords: algorithmic trading India, trading bots NSE, Python trading automation, automated trading software NSE BSE, algo trading Mumbai, quantitative trading India*


==================================================


## [3/3] Repository: eiten (`PHASE4-QUANT-007`)
- **Full Name**: `PHASE4-QUANT-007_tradytics__eiten`
- **Description**: Statistical and Algorithmic Investing Strategies for Everyone
- **GitHub Stars**: 3298
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<p align="center">
  <img width="325" src="figures/normal-512x512.png">
</p>

# Eiten - Algorithmic Investing Strategies for Everyone
Eiten is an open source toolkit by [Tradytics](https://www.tradytics.com/) that implements various statistical and algorithmic investing strategies such as **Eigen Portfolios**, **Minimum Variance Portfolios**, **Maximum Sharpe Ratio Portfolios**, and **Genetic Algorithms** based Portfolios. It allows you to build your own portfolios with your own set of stocks that can beat the market. The rigorous testing framework included in Eiten enables you to have confidence in your portfolios.

If you are looking to discuss these tools in depth and talk about more tools that we are working on, please feel free to join our [Discord](https://discord.gg/QuvE2Z8) channel where we have a bunch of more tools too.

### Files Description
| Path | Description
| :--- | :----------
| eiten | Main folder.
| &boxur;&nbsp; figures | Figures for this github repositories.
| &boxur;&nbsp; stocks | Folder to keep your stock lists that you want to use to create your portfolios.
| &boxur;&nbsp; strategies | A bunch of strategies implemented in python.
| backtester.py | Backtesting module that both backtests and forward tests all portfolios.
| data_loader.py | Module for loading data from yahoo finance.
| portfolio_manager.py | Main file that takes in a bunch of arguments and generates several portfolios for you.
| simulator.py | Simulator that uses historical returns and monte carlo to simulate future prices for the portfolios.
| strategy_manager.py | Manages the strategies implemented in the 'strategies' folder.

## Required Packages 
You will need to install the following package to train and test the models.
- [Scikit-learn](https://scikit-learn.org/)
- [Numpy](https://numpy.org/)
- [Tqdm](https://github.com/tqdm/tqdm)
- [Yfinance](https://github.com/ranaroussi/yfinance)
- [Pandas](https://pandas.pydata.org/)
- [Scipy](https://www.scipy.org/install.html)

You can install all packages using the following command. Please note that the script was written using python3.

```
pip install -r requirements.txt
```

## Build your portfolios
Let us see how we can use all the strategies given in the toolkit to build our portfolios. The first thing you need to do is modify the **stocks.txt** file in the **stocks** folder and add the stocks of your choice. It is recommended to keep the list small i.e anywhere between **5 to 50** stocks should be fine. We have already put a small stocks list containing a bunch of tech stocks like AAPL, MSFT, TSLA etc. Let us build our portfolios now. This is the main command that you need to run.

```
python portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 1 --market_index QQQ --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```

This command will use last 5 years of daily data excluding the last 90 days and build several portfolios for you. Based on those portfolios, it will then test them on the out of sample data of 90 days and show you the performance of each portfolio. Finally, it will also compare the performance with your choice of market index which is **QQQ** here. Let's dive into each of the parameters in detail.
- **is_test**: The value determined if the program is going to keep some separate data for future testing. When this is enabled, the value of **future_bars** should be larger than 5.
- **future_bars**: These are the bars that the tool will exclude during portfolio building and will forward test the portfolios on the excluded set. This is also called out of sample data.
- **data_granularity_minutes**: How much granular data do you want to use to build your portfolios. For long term portfolios, you should use daily data but for short term, you can use hourly or minute level data. The possible values here are **3600, 60, 30, 15, 5, 1.** 3600 means daily.
- **history_to_use**: Whether to use a specific number of historical bars or use everything that we receive from yahoo finance. For minute level data, we only receive up to one month of historical data. For daily, we receive 5 years worth of historical data. If you want to use all available data, the value should be **all** but if you want to use smaller history, you can set it to an integer value e.g **100** which will only use the last 100 bars to build the portfolios.
- **apply_noise_filtering**: This uses [random matrix theory](http://faculty.baruch.cuny.edu/jgatheral/randommatrixcovariance2008.pdf) to filter out the covariance matrix from randomness thus yielding better portfolios. A value of 1 will enable it and 0 will disable it.
- **market_index**: Which index do you want to use to compare your portfolios. This should mostly be **SPY** but since we analyzed tech stocks, we used **QQQ**.
- **only_long**: Whether to use long only portfolio or enable short selling as well. Long only portfolios have shown to have better performance using algorithmic techniques.
- **eigen_portfolio_number**: Which eigen portfolio to use. Any value between 1-5 should work. The first eigen portfolio (1) represents the market portfolio and should act just like the underlying index such as SPY or QQQ. The second one is orthogonal and uncorrelated to the market and poses the greatest risk and reward. The following ones have reduced risk and reward. Read more on [eigen-portfolios](https://srome.github.io/Eigenvesting-I-Linear-Algebra-Can-Help-You-Choose-Your-Stock-Portfolio/).
- **stocks_file_path**: File that contains the list of stocks that you want to use to build your portfolio.

### Some Portfolio Building Examples
Here are a few examples for building different types of portfolios.
- Both **long and short** portfolios by analyzing last **90 days** data and keeping the **last 30 days** as testing data. This will give us 60 days of portfolio construction data and 30 days of testing.
```
python portfolio_manager.py --is_test 1 --future_bars 30 --data_granularity_minutes 3600 --history_to_use 90 --apply_noise_filtering 1 --market_index QQQ --only_long 0 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```
- Only **long portfolio** on **60 minute bars** of the last **30 days**. **No future testing**. Compare the results with **SPY** index instead of QQQ.
```
python portfolio_manager.py --is_test 0 --future_bars 0 --data_granularity_minutes 60 --history_to_use all --apply_noise_filtering 1 --market_index SPY --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```
- **Do not apply noise filtering** on the covariance matrix. Use the **first eigen portfolio** (market portfolio) and compare with SQQQ,
```
python portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 0 --market_index SQQQ --only_long 1 --eigen_portfolio_number 1 --stocks_file_path stocks/stocks.txt
```

## Portfolio Strategies
Four different portfolio strategies are currently supported by the toolkit.
1. **Eigen Portfolios**
	1. These portfolios are orthogonal and uncorrelated to the market in general thus yielding high reward and alpha. However, since they are uncorrelated to the market, they can also provide great risk. The first eigen portfolio is considered to be a market portfolio which is often ignored. The second one is uncorrelated to the others and provides the highest risk and reward. As we go down the numbering, the risk as well as the reward are reduced.
2. **Minimum Variance Portfolio (MVP)**
	1. MVP tries to minimize the variance of the portfolio. These portfolios are lowest risk and reward.
3. **Maximum Sharpe Ratio Portfolio (MSR)**
	1. MSR solves an optimization problem that tries to maximize the sharpe ratio of the portfolio. It uses past returns during the optimization process which means if past returns are not the same as future returns, the results can vary in future.
4. **Genetic Algorithm (GA) based Portfolio**
	1. This is our own implementation of a GA based portfolio that again tries to maximize the sharpe ratio but in a slightly more robust way. This usually provides more robust portfolios than the others.

When you run the command above, our tool will generate portfolios from all these strategies and give them to you. Let us look at some resulting portfolios.

## Resulting Portfolios
For the purpose these results, we will use the 9 stocks in the stocks/stocks.txt file. When we run the above command, we first get the portfolio weights for all four strategies. For testing purposes, the above command used last five years of daily data up till April 29th. The remaining data for this year was used for forward testing i.e the portfolio strategies had no access to it when building the portfolios.

**What if my portfolio needs different stocks?**: All you need to do is change the stocks in the stocks.txt file and run the tool again. Here is the final command again that we run in order to get our portfolios:

```
python portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 1 --market_index QQQ --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```

### Portfolio Weights
<p align="center">
  <img src="figures/portfolio_weights.png">
</p>

We can see that the eigen portfolio is giving a large weight to TSLA while the others are dividing their weights more uniformly. An interesting phenomena happening here is the hedging with **SQQQ** that all the strategies have learned automatically. Every tool is assigning some positive weight to SQQQ while also assigning positive weights to other stocks which indicates that the strategies are automatically trying to hedge the portfolios from risk. Obviously this is not perfect, but just the fact that it's happening is fascinating. Let us look at the backtest results on the last five years prior to April 29, 2020.

### Backtest Results
<p align="center">
  <img src="figures/backtest_results.png">
</p>

The backtests look pretty encouraging. The black dotted line is the market index i.e **QQQ**. Other lines are the strategies. Our custom genetic algorithm implementation seems to have the best backtest results because it's an advanced version of other strategies. The eigen portfolio that weighed TSLA the most have the most volatility but its profits are also very high. Finally, as expected, the MVP has the minimum variance and ultimately the least profits. However, since the variance is extremely low, it is a good portfolio for those who want to stay safe. The most interesting part comes next, let us look at the forward or future test results for these portfolios. 

### Forward Test Results
<p align="center">
  <img src="figures/future_test_results.png">
</p>

These results are from April 29th, 2020 to September 4th, 2020. The eigen portfolio performed the best but it also had a lot of volatility. Moreover, most of those returns are due to TSLA rocketing in the last few months. After that, our GA algorithm worked quite effectively as it beat the market index. Again, as expected, the MVP had the lowest risk and reward and slowly went up in 4-5 months. This shows the effectiveness and power of these algorithmic portfolio optimization strategies where we've developed different portfolios for different kinds of risk and reward profiles.


## Conclusion and Discussion
We are happy to share this toolkit with the trading community and hope that people will like and contribute to it. As is the case with everything in trading, these strategies are not perfect but they are based on rigorous theory and some great empirical results. Please take care when trading with these strategies and always manage your risk. The above results were not cherry picked but the market has been highly bullish in the last few months which has led to the strong results shown above. We would love for the community to try out different strategies and share them with us.

#### Special Thanks
Special thanks to [Scott Rome's](https://srome.github.io/) blog. The eigen portfolios and minimum variance portfolio concepts came from his blog posts. The code for filtering eigen values of the covariance matrix was also mostly obtained from one of his posts.

## License
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A product by [Tradytics](https://www.tradytics.com/)

Copyright (c) 2020-present, Tradytics.com

### Core Implementation Code & Architecture
#### File: `strategies/minimum_variance_strategy.py`
```python
# Basic libraries
import os
import random
import warnings
import numpy as np
warnings.filterwarnings("ignore")

class MinimumVarianceStrategy:
	def __init__(self):
		print("Minimum Variance strategy has been created")
		
	def generate_portfolio(self, symbols, covariance_matrix):
		"""
		Inspired by: https://srome.github.io/Eigenvesting-II-Optimize-Your-Portfolio-With-Optimization/
		"""
		inverse_cov_matrix = np.linalg.pinv(covariance_matrix)
		ones = np.ones(len(inverse_cov_matrix))
		inverse_dot_ones = np.dot(inverse_cov_matrix, ones)
		min_var_weights = inverse_dot_ones / np.dot( inverse_dot_ones, ones)
		portfolio_weights_dictionary = dict([(symbols[x], min_var_weights[x]) for x in range(0, len(min_var_weights))])
		return portfolio_weights_dictionary
```

#### File: `strategies/maximum_sharpe_ratio_strategy.py`
```python
# Basic libraries
import os
import random
import warnings
import numpy as np
warnings.filterwarnings("ignore")

class MaximumSharpeRatioStrategy:
	def __init__(self):
		print("Maximum sharpe ratio strategy has been created")
		
	def generate_portfolio(self, symbols, covariance_matrix, returns_vector):
		"""
		Inspired by: Eigen Portfolio Selection: A Robust Approach to Sharpe Ratio Maximization, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3070416
		"""
		inverse_cov_matrix = np.linalg.pinv(covariance_matrix)
		ones = np.ones(len(inverse_cov_matrix))

		numerator = np.dot(inverse_cov_matrix, returns_vector)
		denominator = np.dot(np.dot(ones.transpose(), inverse_cov_matrix), returns_vector)
		msr_portfolio_weights = numerator / denominator
		
		portfolio_weights_dictionary = dict([(symbols[x], msr_portfolio_weights[x]) for x in range(0, len(msr_portfolio_weights))])
		return portfolio_weights_dictionary
```

#### File: `strategies/eigen_portfolio_strategy.py`
```python
# Basic libraries
import os
import warnings
import numpy as np
warnings.filterwarnings("ignore")

class EigenPortfolioStrategy:
	def __init__(self):
		print("Eigen portfolio strategy has been created")
		
	def generate_portfolio(self, symbols, covariance_matrix, eigen_portfolio_number):
		"""
		Inspired by: https://srome.github.io/Eigenvesting-I-Linear-Algebra-Can-Help-You-Choose-Your-Stock-Portfolio/
		"""
		eig_values, eig_vectors = np.linalg.eigh(covariance_matrix)
		market_eigen_portfolio = eig_vectors[:,-1] / np.sum(eig_vectors[:,-1]) # We don't need this but in case someone wants to analyze
		eigen_portfolio = eig_vectors[:,-eigen_portfolio_number] / np.sum(eig_vectors[:,-eigen_portfolio_number]) # This is a portfolio that is uncorrelated to market and still yields good returns

		portfolio_weights_dictionary = dict([(symbols[x], eigen_portfolio[x]) for x in range(0, len(eigen_portfolio))])
		return portfolio_weights_dictionary
```

#### File: `portfolio_manager.py`
```python
# Basic libraries
import argparse
import json
from eiten import Eiten
from argchecker import ArgChecker

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

"""
Sample run:
python portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 1 --market_index QQQ --only_long 1 --eigen_portfolio_number 3 --save_plot False
"""

def main():

    argParser = argparse.ArgumentParser()
    commands = json.load(open("commands.json", "r"))
    for i in commands:
        arg_types = {"str": str, "int": int, "bool": bool}
        argParser.add_argument(i["comm"], type=arg_types[i["type"]],
                               default=i["default"], help=i["help"])

    # Get arguments
    args = argParser.parse_args()

    # Check arguments
    ArgChecker(args)

    # Run strategies
    eiten = Eiten(args)
    eiten.run_strategies()


if __name__ == '__main__':
    main()
```

#### File: `argchecker.py`
```python
class ArgChecker:
    """
    Argument checker
    """

    def __init__(self, args):
        print("Checking arguments...")
        self.check_arguments(args)

    def check_arguments(self, args):
        granularity_constraints_list = [1, 5, 10, 15, 30, 60, 3600]
        granularity_constraints_list_string = ''.join(
            str(value) + "," for value in granularity_constraints_list).strip(",")

        assert not(args.data_granularity_minutes not in granularity_constraints_list), "You can only choose the following values for 'data_granularity_minutes' argument -> %s\nExiting now..." % granularity_constraints_list_string

        assert not(args.is_test == 1 and args.future_bars <
                   2), "You want to test but the future bars are less than 2. That does not give us enough data to test the model properly. Please use a value larger than 2.\nExiting now..."

        assert not(args.history_to_use != "all" and int(args.history_to_use) <
                   args.future_bars), "It is a good idea to use more history and less future bars. Please change these two values and try again.\nExiting now..."

        args.market_index = str(args.market_index).upper()
        if args.history_to_use != "all":
            args.history_to_use = int(args.history_to_use)
```

#### File: `strategies/strategy_helper_functions.py`
```python
# Basic libraries
import os
import random
import warnings
import numpy as np
warnings.filterwarnings("ignore")

class StrategyHelperFunctions:
	def __init__(self):
		print("Helper functions have been created")
		
	def random_matrix_theory_based_cov(self, returns_matrix):
		"""
		This is inspired by the excellent post @ https://srome.github.io/Eigenvesting-III-Random-Matrix-Filtering-In-Finance/
		"""

		# Calculate variance and std, will come in handy during reconstruction
		variances = np.diag(np.cov(returns_matrix))
		standard_deviations = np.sqrt(variances)

		# Get correlation matrix and compute eigen vectors and values
		correlation_matrix = np.corrcoef(returns_matrix)
		eig_values, eig_vectors = np.linalg.eigh(correlation_matrix)
		
		# Get maximum theoretical eigen value for a random matrix
		sigma = 1 # The variance for all of the standardized log returns is 1
		Q = len(returns_matrix[0]) / len(returns_matrix)
		max_theoretical_eval = np.power(sigma*(1 + np.sqrt(1/Q)),2)
		
		# Prune random eigen values
		eig_values_pruned = eig_values[eig_values > max_theoretical_eval]
		eig_values[eig_values <= max_theoretical_eval] = 0

		# Reconstruct the covariance matrix from the correlation matrix and filtered eigen values
		temp = np.dot(eig_vectors, np.dot(np.diag(eig_values), np.transpose(eig_vectors)))
		np.fill_diagonal(temp, 1)
		filtered_matrix = temp
		filtered_cov_matrix = np.dot(np.diag(standard_deviations), 
                               np.dot(filtered_matrix,np.diag(standard_deviations)))
		
		return filtered_cov_matrix
```


==================================================
