# ⚡ [QUANT-SOURCE-160] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_160_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: OptionsLab (`PHASE4-QUANT-188`)
- **Full Name**: `PHASE4-QUANT-188_diegourda__OptionsLab`
- **Description**: A modular Python toolkit for advanced options pricing, volatility modeling, Greeks computation, and risk analysis. Includes Monte Carlo and Black-Scholes models, machine learning volatility surfaces, and interactive visualizations via Streamlit.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Options Lab

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/Diegotistical/OptionsLab)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Diegotistical/OptionsLab)](https://github.com/Diegotistical/quant-options-toolkit/commits/main)
[![Streamlit](https://img.shields.io/badge/Open%20in%20Streamlit-App-red?logo=streamlit&logoColor=white)](https://optionslab.streamlit.app/)

**OptionsLab** is a modular quantitative research framework focused on **volatility surface modeling**, **Options Pricing using different models**, and **risk analysis** for derivatives pricing and trading strategy development.  
It provides a unified interface for building, fitting, and evaluating option pricing models — from classical methods (Binomial Trees, Black-Scholes) to machine learning–based volatility surface models (MLP, SVR, Random Forest & XGBoost).

---

## 🚀 Key Features

- **Volatility Surface Modeling**
  - Parametric and non-parametric surface fitting.
  - ML-based volatility modeling using PyTorch and Scikit-learn.
  - Support for arbitrage-free enforcement and surface regularization.
  
- **Monte Carlo Engine**
  - Classic stochastic simulation with configurable paths and payoffs.
  - ML-augmented Monte Carlo models for accelerated pricing and scenario analysis.
  - Unified API across stochastic and ML-based simulations.

- **Pricing Models**
  - Black-Scholes, Binomial Trees, and Monte Carlo (standard and ML-driven).
  - Support for greeks computation and sensitivity analysis.

- **Risk Analysis Tools**
  - Value at Risk (VaR), Expected Shortfall (ES), and Stress Testing.
  - Scenario-based risk metrics for portfolios and individual instruments.

- **Streamlit App**
  - Interactive dashboards for pricing, visualization, and volatility surface exploration.
  - Modular page system (Monte Carlo, Binomial Tree, Vol Surface, Risk Analysis).

---

## 🧩 Project Highlights

- Fully modular **`src/`** structure with clear separation between models, utils, and core logic.
- Robust **exception handling** and **validation layers** across all modules.
- Comprehensive **unit testing suite** (`pytest`) for model reliability.
- Compatible with **CI/CD workflows** via GitHub Actions (coming soon)
- Ready-to-deploy **Streamlit app** for interactive exploration and demonstrations.


---

## 🏗️ Project Structure

    |   LICENSE
    |   README.md
    |   requirements.txt
    |   runtime.txt
    |   setup.py
    |   structure.txt
    |   
    +---.devcontainer
    |       devcontainer.json
    |       
    +---.github
    |   \---workflows
    |           ci.yml
    |           
    +---data
    |   +---processed
    |   |       .gitkeep
    |   |       
    |   \---raw
    |           .gitkeep
    |           
    +---docs
    |       .gitkeep
    |       
    +---models
    |   +---my_models
    |   +---saved_models
    |   |       .gitkeep
    |   |       
    |   \---training_logs
    |           .gitkeep
    |           
    +---notebooks
    |       .gitkeep
    |       backtesting.ipynb
    |       binomial_tree.ipynb
    |       exploratory_data_analysis.ipynb
    |       learnings.ipynb
    |       volatility_model_tuning.ipynb
    |       
    +---src
    |   |   __init__.py
    |   |   
    |   +---common
    |   |       config.py
    |   |       helpers.py
    |   |       logging_config.py
    |   |       validation.py
    |   |       __init__.py
    |   |       
    |   +---exceptions
    |   |       data_exceptions.py
    |   |       greek_exceptions.py
    |   |       model_exceptions.py
    |   |       montecarlo_exceptions.py
    |   |       pricing_exceptions.py
    |   |       risk_exceptions.py
    |   |       __init__.py
    |   |       
    |   +---greeks
    |   |       .gitkeep
    |   |       greeks.py
    |   |       
    |   +---pricing_models
    |   |       .gitkeep
    |   |       binomial_tree.py
    |   |       black_scholes.py
    |   |       monte_carlo.py
    |   |       monte_carlo_ml.py
    |   |       monte_carlo_unified.py
    |   |       __init__.py
    |   |       
    |   +---risk_analysis
    |   |       .gitkeep
    |   |       expected_shortfall.py
    |   |       sensitivity_analysis.py
    |   |       stress_testing.py
    |   |       var.py
    |   |       __init__.py
    |   |       
    |   +---utils
    |   |   |   .gitkeep
    |   |   |   utils.py
    |   |   |   __init__.py
    |   |   |   
    |   |   \---decorators
    |   |           caching.py
    |   |           timing.py
    |   |           __init__.py
    |   |           
    |   \---volatility_surface
    |       |   .gitkeep
    |       |   base.py
    |       |   surface_generator.py
    |       |   __init__.py
    |       |   
    |       +---common
    |       |       validation.py
    |       |       __init__.py
    |       |       
    |       +---models
    |       |       mlp_model.py
    |       |       random_forest.py
    |       |       svr_model.py
    |       |       xgboost_model.py
    |       |       __init__.py
    |       |       
    |       \---utils
    |               arbitrage.py
    |               arbitrage_enforcement.py
    |               arbitrage_utils.py
    |               data_preprocessing.py
    |               feature_engineering.py
    |               grid_search.py
    |               tensor_utils.py
    |               __init__.py
    |               
    +---streamlit_app
    |   |   app.py
    |   |   st_utils.py
    |   |   __init__.py
    |   |   
    |   \---pages
    |           .gitkeep
    |           1_MonteCarlo_Basic.py
    |           2_MonteCarlo_ML.py
    |           3_MonteCarlo_Unified.py
    |           4_Binomial_Tree.py
    |           benchmarks.py
    |           risk_analysis.py
    |           volatility_surface.py
    |           __init__.py
    |           
    \---tests
            .gitkeep
            test_benchmarks.py
            test_benchmarks2.py
            test_black_scholes.py
            test_models.py
            test_monte_carlo.py
            test_risk_analysis.py
            test_var.py
            test_vol_surface.py
---

## 🚀 Getting Started

### Requirements

- Python ≥ 3.10 (Recommended 3.13)
- Recommended: virtual environment (venv, conda, etc.)

### Installation

Clone the repository:

    git clone https://github.com/Diegotistical/OptionsLab.git
    cd OptionsLab
    
*(Note: Ensure you fill in `requirements.txt` as you add dependencies.)*

Install requirements:

    pip install -r requirements.txt

---

## 🛠️ Usage Examples

# Monte Carlo Option Pricer Tutorial

This tutorial demonstrates how to use the `MonteCarloPricer` class to price European options and compute Greeks. Optional Numba acceleration is supported for faster simulations.

---

## 1. Import the Pricer

```bash
from src.pricing_models.monte_carlo import MonteCarloPricer
```

---

## 2. Initialize a Pricer

```bash
pricer = MonteCarloPricer(
    num_simulations=100_000,
    num_steps=100,
    seed=42,
    use_numba=False
)
```

---

## 3. Price a European Option

```bash
S, K, T, r, sigma, q = 100, 110, 1, 0.01, 0.2, 0.0

call_price = pricer.price(S, K, T, r, sigma, option_type="call", q=q)
put_price  = pricer.price(S, K, T, r, sigma, option_type="put", q=q)

print(f"Call Price: {call_price:.4f}")
print(f"Put Price: {put_price:.4f}")
```

---

## 4. Compute Greeks

```bash
delta = pricer.delta(S, K, T, r, sigma, option_type="call")
gamma = pricer.gamma(S, K, T, r, sigma, option_type="call")
vega  = pricer.vega(S, K, T, r, sigma, option_type="call")
theta = pricer.theta(S, K, T, r, sigma, option_type="call")
rho   = pricer.rho(S, K, T, r, sigma, option_type="call")

print(f"Delta: {delta:.4f}, Gamma: {gamma:.4f}, Vega: {vega:.4f}, Theta: {theta:.4f}, Rho: {rho:.4f}")
```

---

## 5. Enable Numba Acceleration (Optional)

```bash
pricer_numba = MonteCarloPricer(
    num_simulations=100_000,
    num_steps=100,
    use_numba=True
)

fast_price = pricer_numba.price(S, K, T, r, sigma, option_type="call")
print(f"Call Price with Numba: {fast_price:.4f}")
```

---

## 🤝 Contributing

Contributions are welcome!

- Fork the repository
- Create a feature branch: `git checkout -b feature/MyFeature`
- Commit your changes: `git commit -m "Add MyFeature"`
- Push to your branch: `git push origin feature/MyFeature`
- Open a pull request

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

Project maintained by [Diegotistical](https://github.com/Diegotistical).

---

*Note: This project is in active development. Expect breaking changes as new features are added.*

### Core Implementation Code & Architecture
#### File: `tests/test_vol_surface.py`
```python

```

#### File: `streamlit_app/__init__.py`
```python

```

#### File: `streamlit_app/pages/__init__.py`
```python

```

#### File: `src/volatility_surface/common/__init__.py`
```python

```

#### File: `src/experiments/__init__.py`
```python
# src/experiments/__init__.py
"""Experiment modules for volatility surface research."""
```

#### File: `src/utils/decorators/__init__.py`
```python
from src.utils.decorators.caching import cached_data, cached_resource
from src.utils.decorators.timing import timeit

__all__ = ["cached_resource", "cached_data", "timeit"]
```


==================================================


## [2/3] Repository: crypto_options_desk_mcp (`PHASE4-QUANT-190`)
- **Full Name**: `PHASE4-QUANT-190_dasein108__crypto_options_desk_mcp`
- **Description**: MCP server giving an LLM a typed, read-only tool surface over crypto-options analytics — GEX, vanna, skew, vol surface, greeks, IV-RV, live positions. Point Claude at Bybit data.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Crypto Options Desk MCP

A **Model Context Protocol (MCP)** server that gives an LLM agent one typed, audited, read-only-by-default
tool surface over a quant crypto-options desk's analytics: gamma exposure, vanna, skew, vol surface,
options flow, technicals, portfolio greeks, scenario analysis, vol-selling signals, and live positions.

Point Claude (Desktop or Code) at it and ask *"give me a BTC options market memo"* — the agent calls the
tools itself and reasons over real Bybit data.

**What it actually does, end to end:** the LLM drives the whole desk. It calls the flow tools (GEX, vanna,
skew, vol surface) to read dealer positioning, the sentiment/funding/OI tools to read the crowd, the
technicals for trend, and the IV-RV / vol-selling / strategy tools to find an edge — then it cross-checks
those numbers against each other and writes a trader-grade memo: regime call, the structural shifts that
matter, defined-risk trade ideas with strikes/breakevens, an allocation, and a risk checklist. With a
read-only API key it also pulls your live book and folds current positions into the same analysis. The
math is identical to what the (private) strategy bots run — the agent just narrates and reasons over it.

See the [`examples/`](examples/) folder for real outputs: full market memos from both Claude and Codex
(`*_market_analysis_2026-06-07.md`) and the **delta updates** they produced ~11h later
(`*_market_analysis_2026-06-08.md`) — each diffs the new snapshot against the prior one (spot, IV, GEX,
funding, OI) and tells you what *changed* and why it matters, not just where the market is.

> Extracted from a private multi-strategy trading desk. This is the **analytics surface** only — no
> strategy signals, thresholds, or alpha. The server is a *thin facade*; all math lives in the bundled
> libraries (`options_lib`, `indicators_lib`, `portfolio_lib`, `bybit_api`) — the same code the (private)
> strategy bots import directly. One implementation, surfaced two ways.

---

## Contents
- [Install](#install)
- [Use with Claude](#use-with-claude) (Desktop & Code)
- [Keep the session rolling](#keep-the-session-rolling) ⭐
- [Example outputs](#example-outputs)
- [API key setup](#api-key-setup-optional) (optional)
- [The 22 tools](#the-22-tools)
- [Bonus: the research prompt](#bonus-the-research-prompt)
- [Configuration](#configuration)
- [Safety model](#safety-model)
- [Architecture](#architecture)

---

## Install

Requires Python ≥ 3.11.

```bash
# with uv (recommended)
uv venv && uv pip install -e .

# or plain pip
pip install -e .
```

This installs the `trading-mcp` console command (it speaks MCP over stdio).

Smoke-test it:

```bash
trading-mcp            # starts the server (Ctrl-C to stop) — no output is normal; logs go to a file
pytest                 # after: pip install -e ".[dev]"
```

---

## Use with Claude

The server communicates over **stdio**, so any MCP client launches it as a subprocess.

### Claude Desktop

Edit your MCP config file:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```jsonc
{
  "mcpServers": {
    "trading-mcp": {
      "command": "trading-mcp"
    }
  }
}
```

If `trading-mcp` isn't on Claude's PATH, use the venv's absolute path instead:

```jsonc
{
  "mcpServers": {
    "trading-mcp": {
      "command": "/abs/path/to/trading-mcp/.venv/bin/trading-mcp"
    }
  }
}
```

Or run it as a module (no console script needed):

```jsonc
{
  "mcpServers": {
    "trading-mcp": {
      "command": "/abs/path/to/.venv/bin/python",
      "args": ["-m", "mcp_trading"]
    }
  }
}
```

Restart Claude Desktop — you'll see the 🔌 tools appear. Try: *"Use trading-mcp to analyze BTC gamma
exposure and the vol surface, then summarize the regime."*

### Claude Code (CLI)

```bash
# from anywhere, register the installed command
claude mcp add trading-mcp -- trading-mcp

# or pin to a specific venv / module form
claude mcp add trading-mcp -- /abs/path/to/.venv/bin/python -m mcp_trading

# with an API key for the position tools (see below)
claude mcp add trading-mcp --env BYBIT_API_KEY=xxx --env BYBIT_API_SECRET=yyy -- trading-mcp

claude mcp list          # verify it's connected
```

Then in a Claude Code session: *"call get_gex_analysis for ETH and explain the key levels."*

---

## Keep the session rolling

**The single biggest win: don't treat each query as one-shot. Keep one long-lived chat and let market data
accumulate in it over time.** A single snapshot tells the model where the market *is*; a session that has
seen several snapshots tells it where the market is *going* — and that's where the analysis gets sharp.

Why it works:

- **Deltas beat levels.** "IV is 93%" is noise; "ETH IV went +6.6 pts into an up-move while GEX short
  gamma halved" is a tradable signal. The model can only compute that second sentence if the earlier
  snapshot is still in context. See the `2026-06-08` example memos — they're *entirely* a diff against the
  `2026-06-07` snapshot taken ~11h earlier.
- **Positions get tracked in time.** Re-run the position tools (or paste your book) into the same session
  and the agent follows each leg across snapshots — PnL drift, greeks decay, whether the original thesis
  still holds, when premium has bled enough to exit. It remembers what it recommended and grades it.
- **Theses carry forward.** The trade ideas, strikes, and risk levels from the first memo become the
  reference frame for the next one ("the ETH put-spread thesis is *stronger* now — wider premium, less
  short gamma, price lifted off support"), instead of starting cold every time.

Practical loop:

1. Start a memo: *"pull BTC + ETH flow, sentiment, technicals, IV-RV and write a market memo."*
2. Hours/days later, **in the same chat**: *"re-pull everything and give me a delta update vs the last
   snapshot — what changed, and does it change the trade?"*
3. With an API key add: *"also pull my positions and track them against the thesis."*

A real multi-day position-tracking history (Claude following a book across snapshots) is published here:

**→ https://claude.ai/share/cdb4169c-2656-42b9-99e1-6b6b23469ace**

---

## Example outputs

The [`examples/`](examples/) folder holds real, unedited memos generated through this server:

| File | What it is |
|------|------------|
| [`claude_market_analysis_2026-06-07.md`](examples/claude_market_analysis_2026-06-07.md) | Full BTC/ETH options memo — snapshot, IV-RV edge, GEX structure, ranked trade ideas |
| [`codex_market_analysis_2026-06-07.md`](examples/codex_market_analysis_2026-06-07.md) | Same day via Codex — straddle/strangle picks with strikes, breakevens, allocation |
| [`claude_market_analysis_2026-06-08.md`](examples/claude_market_analysis_2026-06-08.md) | **Delta update** ~11h later — a `Then → Now → Δ` table and what the shifts mean for the thesis |
| [`codex_market_analysis_2026-06-08.md`](examples/codex_market_analysis_2026-06-08.md) | Codex delta update — re-ranked trades, updated allocation, risk controls |

The `06-08` files only exist *because* the `06-07` snapshot was still in the session — that's the rolling
workflow above, captured on disk.

---

## API key setup (optional)

**Most tools need no credentials** — GEX, vanna, skew, flow, vol surface, indicators, klines, funding,
OI, options chain, IV-RV, and all strategy-analysis tools use Bybit **public** market data.

Only the **two user-position tools** (`get_user_options_positions`, `get_user_all_positions`) require a
Bybit API key. A **read-only** key is enough and recommended.

Provide the key by env var (`BYBIT_API_KEY`, `BYBIT_API_SECRET`) any of these ways:

```bash
# 1) .env file (copy the template, fill in)
cp .env.example .env

# 2) inline in the Claude Desktop config
#    "trading-mcp": { "command": "trading-mcp",
#      "env": { "BYBIT_API_KEY": "xxx", "BYBIT_API_SECRET": "yyy" } }

# 3) Claude Code flags
claude mcp add trading-mcp --env BYBIT_API_KEY=xxx --env BYBIT_API_SECRET=yyy -- trading-mcp
```

Without a key the position tools return a structured error; everything else works.

---

## The 22 tools

Every tool returns a uniform envelope — `{ "success": bool, "data": …, "timestamp": … }` (or a
tool-specific structured object). Defaults shown in `()`.

### Options flow (5)
| Tool | Params | Returns |
|------|--------|---------|
| `get_gex_analysis` | `base_coin`(BTC), `min_oi`(1.0) | Gamma-exposure profile: net GEX, gamma walls, flip level, dealer-positioning market impact |
| `get_vanna_analysis` | `base_coin`(BTC), `price_move`(0.05) | Vanna exposure and the implied-vol impact of a given % price move |
| `get_flow_analysis` | `base_coin`(BTC) | Options flow: volume, put/call ratios, unusual-activity flags |
| `get_skew_analysis` | `base_coin`(BTC) | Volatility skew + term structure across strikes and expiries |
| `get_vol_surface_metrics` | `base_coin`(BTC) | Surface diagnostics: 25Δ risk-reversal, 10Δ skew, vol-of-vol, variance-risk premium |

### Technical analysis (1)
| Tool | Params | Returns |
|------|--------|---------|
| `get_technical_indicators` | `symbol`, `interval`(1h), `hours_back`(720) | EMA stack, RSI, MACD, ATR, Bollinger, ADX, Hurst exponent, Z-score |

### Market data (2)
| Tool | Params | Returns |
|------|--------|---------|
| `get_historical_data` | `symbol`, `interval`(1h), `hours_back`(720) | Kline count, latest price, last 10 OHLCV candles |
| `get_options_chain` | `base_coin`(BTC), `min_oi`(1.0) | Live options chain, OI-filtered, with a sample slice |

### Sentiment & positioning (3)
| Tool | Params | Returns |
|------|--------|---------|
| `get_market_sentiment_analysis` | `symbol`(BTCUSDT) | Long/short ratios, positioning bias, sentiment extremes |
| `get_open_interest_analysis` | `symbol`(BTCUSDT) | Open-interest level + trend |
| `get_funding_rate_analysis` | `symbol`(BTCUSDT) | Funding rate, carry cost, funding extremes |

### Portfolio (2)
| Tool | Params | Returns |
|------|--------|---------|
| `analyze_portfolio_greeks` | `portfolio_data` | Aggregate Δ/Γ/Θ/Vega + risk metrics for a set of option positions |
| `run_scenario_analysis` | `portfolio_data`, `scenarios` | Portfolio PnL across supplied price/vol scenarios |

### Vol selling (2)
| Tool | Params | Returns |
|------|--------|---------|
| `get_iv_rv_spread` | `base_coin`(BTC), `rv_window`(30) | ATM implied vol vs Garman-Klass realized vol spread — the vol-selling edge metric |
| `get_covered_call_signal` | `base_coin`(BTC), `target_delta`(0.10), `iv_rv_threshold`(10.0), `max_dte`(14) | Covered-call go/no-go: IV-RV check, vol regime, term structure, skew, recommended OTM strike |

### Strategy analysis (4)
| Tool | Params | Returns |
|------|--------|---------|
| `analyze_straddles` | `base_coin`(BTC), `min_oi`(10.0) | Straddle candidates ranked by profitability |
| `analyze_strangles` | `base_coin`(BTC), `min_oi`(10.0) | Strangle optimization |
| `analyze_spreads` | `base_coin`(BTC), `min_oi`(10.0), `spread_types`([call_spread,put_spread]) | Vertical call/put spread analysis |
| `analyze_portfolio_strategies` | `portfolio_positions` | Classifies existing multi-leg strategies in a portfolio (legs, confidence, net cost, breakevens) |

### User positions (2) — *API-key gated*
| Tool | Params | Returns |
|------|--------|---------|
| `get_user_options_positions` | `base_coin`(BTC, or `all`), `position_type`(option) | Live option positions + total unrealised PnL |
| `get_user_all_positions` | `base_coin`(BTC), `position_type`(option/linear/inverse/all) | All positions, per-category breakdown + summary |

### Meta (1)
| Tool | Params | Returns |
|------|--------|---------|
| `get_server_info` | — | Server name, version, tool count, categories |

---

## Bonus: the research prompt

The server also ships one MCP **prompt**, `quant_research_prompt(asset)`, that primes Claude with a
senior-quant options-research workflow — it tells the model which tools to call and how to structure a
market memo (snapshot → sentiment/flow → microstructure → strategy proposals → risk checklist). In Claude
Desktop it appears in the prompt picker; just pass an asset like `BTC`.

---

## Configuration

| Env var | Default | Purpose |
|---------|---------|---------|
| `BYBIT_API_KEY` / `BYBIT_API_SECRET` | — | Only for the two user-position tools (read-only key recommended) |
| `MCP_LOG_FILE` | `/tmp/mcp-trading.log` | Where the server logs (never stdout — stdio is the JSON-RPC channel) |
| `DEBUG_MCP` | unset | Set to `1` for DEBUG-level logs |

---

## Safety model

- **Uniform envelope** — every tool returns structured `{success, data, timestamp}`; failures are never free text.
- **Read-first** — the analytics surface has no side effects; nothing places or modifies orders.
- **Key-gated** — only the position tools touch authenticated endpoints; an unconfigured agent physically can't read your book, let alone move money. Use a **read-only** key.
- **Logs off the wire** — MCP uses stdio for JSON-RPC, so all logging is file-only by design.

---

## Architecture

```
mcp_trading/            thin MCP facade — server.py = 22 @mcp.tool wrappers + 1 prompt
  ├─ orchestrator.py    routes tool calls to the libs; holds the Bybit client + vol analyzer
  ├─ options_lib/       GEX · vanna · skew · flow · vol surface · strategy classification · pricing
  ├─ indicators_lib/    technicals + sentiment
  ├─ portfolio_lib/     portfolio engine · greeks · scenario analysis
  └─ bybit_api/         exchange client (klines, options chain, funding, OI, positions)
```

The facade holds **no business logic** — it validates inputs (Pydantic models) and delegates. That's why
the agent and the bots compute identical numbers from identical code.

## License

MIT — see [LICENSE](LICENSE).

### Core Implementation Code & Architecture
#### File: `src/bybit_api/__main__.py`
```python
from .cli import main

main()
```

#### File: `src/indicators_lib/__main__.py`
```python
from .cli import main

main()
```

#### File: `src/options_lib/__main__.py`
```python
from .cli import main

main()
```

#### File: `src/mcp_trading/__init__.py`
```python
"""MCP Trading Server — quantitative options analysis tools for Claude."""

from .orchestrator import MCPOrchestrator, get_orchestrator
```

#### File: `src/options_lib/pricing/__init__.py`
```python
"""Options pricing engines."""

from .black_scholes import ProfessionalOptionsEngine, OptionSpec, OptionMetrics

__all__ = ['ProfessionalOptionsEngine', 'OptionSpec', 'OptionMetrics']
```

#### File: `src/bybit_api/constants.py`
```python
"""
Constants for Bybit API client.
"""

from pathlib import Path

# Timeframe intervals in minutes
TIMEFRAME_INTERVALS = {
    "1m": 1,
    "3m": 3,
    "5m": 5,
    "15m": 15,
    "30m": 30,
    "1h": 60,
    "2h": 120,
    "4h": 240,
    "6h": 360,
    "12h": 720,
    "1d": 1440,
    "1w": 10080,
    "1M": 43200,
}

CACHE_DIR = str(Path.home() / ".cache" / "bybit-api")
```


==================================================


## [3/3] Repository: fx-volatility-trading-system (`PHASE4-QUANT-187`)
- **Full Name**: `PHASE4-QUANT-187_valerian-drmt__fx-volatility-trading-system`
- **Description**: EUR/USD FX options trading desk: live IB feed → SVI/SSVI surface, GARCH/HAR-RV fair vol, GMM regime   + PCA signals → delta-hedged execution. FastAPI · React · Postgres · Redis on AWS.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# FX Volatility Trading System

**End-to-end trading platform for EUR/USD FX options — a microservices pipeline
that turns a live Interactive Brokers feed into research-grade volatility signals,
executes delta-hedged option structures, and serves it all through a real-time web
desk.**

[![CI](https://github.com/valerian-drmt/fx-volatility-trading-system/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/valerian-drmt/fx-volatility-trading-system/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-async-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-compose-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

<p align="center">
  <img src="docs/pictures/dashboard.png" alt="The voldesk trading cockpit — live vol surface, PCA signals, positions and greeks" width="900">
</p>

A 7-view React trading desk on top of 5 async Python engines: live IB tick stream →
vol-surface fit (SVI / SSVI, GARCH, HAR-RV) → GMM regime + PCA signal z-scores →
delta-hedged order submission → versioned audit trail in Postgres.

## 🔴 Live demo

**[valeriandarmente.dev/fx-volatility-trading-system](https://valeriandarmente.dev/fx-volatility-trading-system/)** — the full stack running live on AWS (paper account).

The public site is **read-only**: browse live positions, the vol surface, PCA
signals, greeks and P&L. Trading, the config editor, and the developer console are
behind an auth boundary. Every push to `main` redeploys it automatically (see
[Deployment](#deployment)).

## 📸 Screenshots

| | |
|:---:|:---:|
| ![Live vol surface, regime & PCA signals](docs/pictures/vol-surface.png) | ![Portfolio risk — greeks, VaR & P&L distribution](docs/pictures/risk.png) |
| *Vol surface, regime & PCA signals* | *Risk — greeks, VaR & P&L distribution* |
| ![Structured options book](docs/pictures/positions.png) | ![Microservices architecture](docs/pictures/architecture.png) |
| *Structured options book* | *Microservices architecture (11 services)* |

> More views in [`docs/pictures/`](docs/pictures/).

---

## Features

### Market data + execution
- IB Gateway container (gnzsnz fork) serving the EUR/USD FOP chains
- Real-time tick stream published on Redis (throttled ~200 ms)
- Structure factory: **straddle**, **strangle**, **risk reversal**, **butterfly**,
  **calendar** — built by delta pillar + tenor, delta-hedged via a 6E futures leg
- Marketable-limit pricing off the live touch; full order lifecycle (submit → fills
  → booked position) with idempotency and reconciliation against the IB mirror

### Volatility analytics
- **Regime detector** — GMM on `[vol_of_vol, vol_level, term_slope]` → 3 regimes
  (calm / stressed / pre-event) driving sizing multipliers
- **Surface fit** — SVI per tenor + SSVI global, butterfly + calendar no-arb checks,
  fair smile via EWMA on historical SVI params
- **Signal** — PCA(3) on the 30-D surface snapshot (6 tenors × 5 delta pillars),
  z-scoring each PC (level / slope / curvature) vs a rolling distribution
- **VRP** — realized forward vol vs ATM implied, conditional on regime

### Risk + P&L
- Greeks aggregation (Δ / Γ / V / Θ / vanna / volga) across open structures, per-tenor vega
- P&L attribution — Taylor decomposition (δ·dS + ½Γ·dS² + V·dσ + Θ·dt + residual)
- Delta hedge modes: static / threshold / scheduled; computed greek limits; VaR

### Admin & observability
- Versioned vol config in Postgres (append-only), edited in the web desk and
  hot-reloaded into the engines via Redis pub/sub
- Secrets in AWS SSM Parameter Store (KMS-encrypted) — never on disk, never echoed
- Structured JSON logs (structlog), Prometheus metrics, OpenTelemetry traces, and an
  opt-in Grafana / Loki / Tempo observability stack

---

## Architecture

**11-container core stack** (6 ship our Python code) **+ an optional 7-container
observability stack** (Prometheus / cAdvisor / Loki / Tempo / Grafana / promtail /
otel-collector, opt-in via `--profile obs`).

```
                          ┌────────────────┐
                          │  React cockpit │   ←──── Users
                          │   (frontend)   │
                          └────────┬───────┘
                                   │ HTTP + WS
                          ┌────────▼───────┐
                          │     nginx      │  reverse proxy (80/443)
                          └────────┬───────┘
                                   │
                          ┌────────▼───────┐
                          │    FastAPI     │  REST + WS bridge (8000)
                          │     (api)      │
                          └─┬────────────┬─┘
                            │            │
            ┌───────────────┘            └──────────────────┐
            ▼                                               ▼
    ┌─────────────┐                                ┌────────────────┐
    │  Postgres   │◄───── db-writer ─────┐         │     Redis      │
    │   (16)      │  (Redis → DB sink)   │         │ pub/sub + cache│
    └─────────────┘                      │         └─┬────┬──┬───┬──┘
                                         └───────────┤    │  │   │
       ┌────────────┐  ticks/bars     ┌──────────────▼┐   │  │   │
       │ ib-gateway │◄────────────────│ market-data    │───┘  │   │
       │  (IB API)  │  (clientID 1)   │   engine       │      │   │
       └─────┬──────┘                 └────────────────┘      │   │
             │     option chains       ┌────────────────┐     │   │
             ├─────(clientID 2)───────►│   vol-engine   │─────┘   │
             │                         │ SVI/SSVI/GARCH │         │
             │                         │ HAR/PCA/GMM    │         │
             │                         └────────────────┘         │
             │     positions+greeks    ┌────────────────┐         │
             ├─────(clientID 3)───────►│   risk-engine  │─────────┘
             │                         │ Δ/Γ/V aggreg.  │
             │                         └────────────────┘
             │     order submission    ┌────────────────┐
             └─────(clientID 5)───────►│ execution-eng. │  HTTP (:8001)
                                       │ orders+hedger  │
                                       └────────────────┘
```

| Container | Runs | Source |
|---|---|---|
| `postgres` | DB 16 | — |
| `redis` | Bus + cache | — |
| `nginx` | Reverse proxy | `infrastructure/nginx/` |
| `ib-gateway` | IB API | — (`gnzsnz/ib-gateway`) |
| `frontend` | React SPA | `frontend/` |
| **`api`** | FastAPI REST + WS | `src/api/` + shared libs |
| **`market-data`** | IB ticks → Redis (clientID 1) | `src/engines/market_data/` |
| **`vol-engine`** | SVI/SSVI/GARCH/HAR/PCA/GMM (clientID 2) | `src/engines/vol/` |
| **`risk-engine`** | Greeks + delta hedge (clientID 3) | `src/engines/risk/` |
| **`db-writer`** | Redis → Postgres async sink | `src/engines/db_writer/` |
| **`execution-engine`** | Order submission (clientID 5, :8001) | `src/engines/execution/` |

Networks: `fxvol-public` (nginx), `fxvol-internal` (services), `fxvol-external` (IB
outbound). The 5 Python engines live behind the `engines` compose profile.

Shared Python libs under `src/` (no container of their own):
- **`core/`** — pure pricing + vol + risk algorithms (no I/O)
- **`persistence/`** — SQLAlchemy 2 ORM (27 classes) + Alembic revisions + `AsyncDatabaseWriter`
- **`bus/`** — Redis pub/sub helpers + channel/key constants
- **`shared/`** — config, structlog, IB connection wrapper, observability

Dependency direction is enforced by [`import-linter`](.importlinter) in CI (5 layered
contracts: `core` pure, `bus`/`persistence` as adapters, `engines` never import `api`).
Full diagrams live in [`docs/architecture/`](docs/architecture/).

---

## Tech stack

| Layer | Tech |
|---|---|
| Language | Python 3.11 + TypeScript 5 |
| Packaging | `pyproject.toml` (PEP 621) — single source of truth; `uv` recommended |
| API | FastAPI + uvicorn + pydantic v2 + slowapi |
| Frontend | React 18 + Vite + TypeScript strict + zustand + plotly.js |
| Persistence | PostgreSQL 16 + SQLAlchemy 2 async + Alembic |
| Cache + bus | Redis 7 (pub/sub + cache) |
| IB connectivity | ib_insync (async) |
| Vol models | numpy, scipy, arch (GARCH), scikit-learn (GMM), custom SVI/SSVI |
| Secrets | AWS SSM Parameter Store + KMS |
| CI / CD | GitHub Actions — ruff, pytest, import-linter, OpenAPI drift, vitest, Playwright; OIDC deploy to AWS EC2 |

---

## Quickstart

**Prerequisites**: Docker Desktop + Python 3.11 + Node 20.

```powershell
# 1. venv + deps (one-off)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,api,quant,ib,writer]"      # or: uv sync --extra dev --extra api --extra quant --extra ib --extra writer

# 2. Load secrets from SSM into the shell (dot-sourced — every PS session)
. .\scripts\local\load_secrets.ps1

# 3. Start the full stack (build + up + alembic upgrade head)
.\scripts\local\stack.ps1
.\scripts\local\stack.ps1 -NoBuild     # reuse cached images
```

Then:
- Cockpit — http://localhost/
- API health — http://localhost/api/v1/health
- Extended health (DB + Redis + engines) — http://localhost/api/v1/health/extended

PyCharm run configurations ship under [`.idea/runConfigurations/`](.idea/runConfigurations)
(version-controlled, grouped **Local** and **EC2**) — no setup needed.

---

## Deployment

Prod runs on a single AWS EC2 box, deployed **continuously from `main`** with no SSH
and no stored AWS keys:

```
push to main → GitHub Actions "build-and-push" (7 images → GHCR, tagged sha-<commit>)
             → "deploy-prod": OIDC into AWS → S3 config payload → SSM RunShellScript
             → the host pulls the images, renders .env from SSM, migrates, restarts
             → smoke-checks the live /health endpoint
```

The VM never builds — it only pulls. Secrets are read on the host from SSM via its
instance role; they never touch GitHub. Deploys are gated by a `DEPLOY_ENABLED` repo
variable, and `.idea`/`scripts`/`docs`-only pushes are `paths-ignore`d so they don't
redeploy. See [`docs/ops/deployment.md`](docs/ops/deployment.md).

---

## Testing

```powershell
python -m ruff check src tests                       # lint
PYTHONPATH=src python -m pytest                       # ~730 unit tests, < 15s
PYTHONPATH=src lint-imports                           # architecture contracts

# Integration suites (gated by env)
$env:DB_RUN_INTEGRATION = "1";    python -m pytest -m db_integration
$env:REDIS_RUN_INTEGRATION = "1"; python -m pytest -m redis_integration
$env:IB_RUN_INTEGRATION = "1";    python -m pytest -m integration

# Frontend
cd frontend
npm run lint && npm run typecheck && npm test         # ESLint + tsc + vitest
npm run test:e2e                                       # Playwright
```

Test layout mirrors `src/` 1-to-1 — see [`tests/STRUCTURE.md`](tests/STRUCTURE.md).

---

## Project structure

```
fx-volatility-trading-system/
├── pyproject.toml                 single source of truth (deps + ruff + pytest + mypy)
├── .importlinter                  architecture contracts (5 layered rules)
├── docker-compose.yml
├── .github/workflows/             ci · build · deploy · codeql · security-scan
├── src/                           (PyPA src-layout, all Python)
│   ├── api/                       → api container: main, 16 routers, ws, middleware, schemas, orchestration/events
│   ├── engines/                   5 long-running services (market_data, vol, risk, db_writer, execution)
│   ├── core/                      pure algos — vol (svi/ssvi/garch/har_rv/pca/gmm/…), pricing/bs, risk/greeks
│   ├── persistence/               DB adapter — models (27 ORM classes), db, writer, migrations/
│   ├── bus/                       Redis adapter — client, publisher, channels, keys
│   └── shared/                    config, logging, ib_connection, observability
├── frontend/                      React + TS + Vite — 7 voldesk views + a dev console (/dev)
├── infrastructure/
│   ├── docker/                    api / web / execution Dockerfiles
│   ├── nginx/                     nginx confs (dev + prod TLS)
│   ├── postgres/ redis/           init.sql + hardened redis.conf
│   ├── ec2/                       host bootstrap + remote-deploy
│   └── aws/                       OIDC / IAM / SSM setup
├── scripts/
│   ├── local/                     stack.ps1 + load_secrets.ps1 (user-run)
│   └── aws/                        ec2.ps1 + load_secrets.sh
├── obs/                           Prometheus / Loki / Tempo / OTel + Grafana dashboards
├── tests/                         unit/ + integration/ (mirrors src/) + fixtures/
└── docs/                          architecture · vol-modeling · strategy · execution · ops (+ diagrams/)
```

---

## Documentation

Full docs live in [`docs/`](docs/):

| Section | Covers |
|---|---|
| [architecture/](docs/architecture/) | System overview, backend layout, data flow, frontend, database schema |
| [vol-modeling/](docs/vol-modeling/) | PCA signals, SVI/SSVI surface, GARCH/HAR-RV forecasting, GMM regime (+ the runnable [PCA notebook](docs/vol-modeling/notebooks/pca_signal_pipeline_explained.ipynb)) |
| [strategy/](docs/strategy/) | Vol structures, signal→trade mapping, risk & P&L attribution |
| [execution/](docs/execution/) | OMS, order lifecycle, IB integration |
| [observability/](docs/observability/) | Metric conventions + operator runbooks |
| [ops/](docs/ops/) | Local stack, AWS deployment, secrets |

The `/dev` console (live on the site) also renders the container graph + health, the
DB schema, and the migration chain directly from the running system.

---

## Contributing

The GitHub project protocol (issue → PR → squash-merge, Conventional Commits, CI
gates) is under [`.github/`](.github/) — see
[`CONTRIBUTING.md`](.github/CONTRIBUTING.md) and [`WORKFLOW.md`](.github/WORKFLOW.md).

Reproduce CI locally:

```powershell
python -m compileall -q src
python -m ruff check src tests
PYTHONPATH=src lint-imports
PYTHONPATH=src python -m pytest
cd frontend; npm run typecheck && npm run lint && npm test && npm run build
```

---

## License

[MIT](LICENSE)

### Core Implementation Code & Architecture
#### File: `src/engines/db_writer/__init__.py`
```python

```

#### File: `src/engines/market_data/__init__.py`
```python

```

#### File: `src/engines/vol/__init__.py`
```python

```

#### File: `src/engines/risk/__init__.py`
```python

```

#### File: `src/api/schemas/__init__.py`
```python
"""Pydantic request/response models — one module per domain."""
```

#### File: `src/api/middleware/__init__.py`
```python
"""Request/response middlewares : logging, timing, rate limiting."""
```


==================================================
