# ⚡ [QUANT-SOURCE-134] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_134_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: jesse (`PHASE4-QUANT-102`)
- **Full Name**: `PHASE4-QUANT-102_jesse-ai__jesse`
- **Description**: An advanced crypto trading bot written in Python
- **GitHub Stars**: 8521
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">
<br>
<p align="center">
<img src="assets/jesse-logo.png" alt="Jesse" height="72" />
</p>

<p align="center">
Algo-trading was 😵‍💫, we made it 🤩
</p>
</div>

# Jesse
[![PyPI](https://img.shields.io/pypi/v/jesse)](https://pypi.org/project/jesse)
[![Downloads](https://pepy.tech/badge/jesse)](https://pepy.tech/project/jesse)
[![Docker Pulls](https://img.shields.io/docker/pulls/salehmir/jesse)](https://hub.docker.com/r/salehmir/jesse)
[![GitHub](https://img.shields.io/github/license/jesse-ai/jesse)](https://github.com/jesse-ai/jesse)
[![coverage](https://codecov.io/gh/jesse-ai/jesse/graph/badge.svg)](https://codecov.io/gh/jesse-ai/jesse)

---

Jesse is an advanced crypto trading framework that aims to **simplify** **researching** and defining **YOUR OWN trading strategies** for backtesting, optimizing, and live trading.

## What is Jesse?
Watch this video to get a quick overview of Jesse:

[![Jesse Overview](https://img.youtube.com/vi/0EqN3OOqeJM/0.jpg)](https://www.youtube.com/watch?v=0EqN3OOqeJM)

## Why Jesse?
In short, Jesse is more **accurate** than other solutions, and way more **simple**. 
In fact, it is so simple that in case you already know Python, you can get started today, in **matter of minutes**, instead of **weeks and months**. 

## Key Features

- 📝 **Simple Syntax**: Define both simple and advanced trading strategies with the simplest syntax in the fastest time.
- 📊 **Comprehensive Indicator Library**: Access a complete library of technical indicators with easy-to-use syntax.
- 📈 **Smart Ordering**: Supports market, limit, and stop orders, automatically choosing the best one for you.
- ⏰ **Multiple Timeframes and Symbols**: Backtest and livetrade multiple timeframes and symbols simultaneously without look-ahead bias.
- 🔒 **Self-Hosted and Privacy-First**: Designed with your privacy in mind, fully self-hosted to ensure your trading strategies and data remain secure.
- 🛡️ **Risk Management**: Built-in helper functions for robust risk management.
- 📋 **Metrics System**: A comprehensive metrics system to evaluate your trading strategy's performance.
- 🔍 **Debug Mode**: Observe your strategy in action with a detailed debug mode.
- 🔧 **Optimize Mode**: Search strategy parameters efficiently with Optuna and parallel processing powered by Ray.
- 📈 **Leveraged and Short-Selling**: First-class support for leveraged trading and short-selling.
- 🔀 **Partial Fills**: Supports entering and exiting positions in multiple orders, allowing for greater flexibility.
- 🔔 **Advanced Alerts**: Create real-time alerts within your strategies for effective monitoring.
- 🔌 **Jesse MCP**: Connect Claude, Codex, Cursor, VS Code, Zed, and other MCP-compatible AI assistants directly to your local Jesse project.
- 🔧 **Built-in Code Editor**: Write, edit, and debug your strategies with a built-in code editor.
- 📊 **Interactive Trading Charts**: Inspect candles, strategy indicators, horizontal levels, orders, and completed trades across backtest, paper, and live sessions.
- 🔬 **Rule Significance Testing**: Test whether an entry rule shows genuine historical edge or could have appeared by chance.
- 🎲 **Monte Carlo Analysis**: Stress-test your strategies with trade-order shuffling and candles-based simulations to distinguish skill from luck and guard against overfitting.
- 🧠 **Machine Learning**: A built-in ML pipeline — gather labelled training data from backtests, train scikit-learn models (binary, multiclass, or regression), and deploy predictions directly inside your strategies.
- 🧪 **Research API and Jupyter**: Run backtests, optimization, significance tests, Monte Carlo analysis, candle workflows, and machine learning from Python scripts or notebooks.
- 🦀 **Rust-Powered Indicators**: Native Rust implementations make indicator-heavy strategies and large research runs substantially faster.
- 🤖 **Reinforcement Learning — Coming Soon**: First-class reinforcement-learning workflows built on Jesse's simulation and research stack are on the way.
- 📺 **Youtube Channel**: Jesse has a Youtube channel with screencast tutorials that go through example strategies step by step.

## Dive Deeper into Jesse's Capabilities

### Stupid Simple
Craft complex trading strategies with remarkably simple Python. Access 300+ indicators, multi-symbol/timeframe support, spot/futures trading, partial fills, and risk management tools. Focus on logic, not boilerplate.

```python
class GoldenCross(Strategy):
    def should_long(self):
        # go long when the EMA 8 is above the EMA 21
        short_ema = ta.ema(self.candles, 8)
        long_ema = ta.ema(self.candles, 21)
        return short_ema > long_ema

    def go_long(self):
        entry_price = self.price - 10        # limit buy order at $10 below the current price
        qty = utils.size_to_qty(self.balance*0.05, entry_price) # spend only 5% of my total capital
        self.buy = qty, entry_price                 # submit entry order
        self.take_profit = qty, entry_price*1.2  # take profit at 20% above the entry price
        self.stop_loss = qty, entry_price*0.9   # stop loss at 10% below the entry price
```

### Backtest
Execute highly accurate and fast backtests without look-ahead bias. Utilize debugging logs, interactive charts with indicator support, and detailed performance metrics to validate your strategies thoroughly.

![Backtest](https://raw.githubusercontent.com/jesse-ai/storage/refs/heads/master/backtest.gif)

### Interactive Trading Charts
Inspect your strategy where its decisions happened. Jesse combines candlesticks, strategy-added indicators and levels, executed orders, and completed trades in synchronized interactive charts. The same charting workflow is available for backtests and for running or completed paper/live sessions.

![Jesse Trade Chart with completed trades and indicator panes](https://cdn.jesse.trade/images/148b8772-9356-45f6-941e-bdda119c8e7b.png)

Expand a trade to inspect every execution, collapse or isolate indicator panes, follow OHLC and indicator values under the cursor, reset the view, use fullscreen mode, or export the chart as an image.

![Jesse Trade Chart showing individual executions](https://cdn.jesse.trade/images/43a766d9-a9e7-47cb-b8ed-7112bdda3a13.png)

[Explore Jesse's interactive charts →](https://docs.jesse.trade/docs/charts/interactive-charts)

### Live/Paper Trading
Deploy strategies live with robust monitoring tools. Supports paper trading, multiple accounts, real-time logs & notifications (Telegram, Slack, Discord), interactive charts, spot/futures, DEX, and a built-in code editor.

![Live/Paper Trading](https://raw.githubusercontent.com/jesse-ai/storage/refs/heads/master/live.gif)

### Benchmark
Accelerate research using the benchmark feature. Run batch backtests, compare across timeframes, symbols, and strategies. Filter and sort results by key performance metrics for efficient analysis.

![Benchmark](https://raw.githubusercontent.com/jesse-ai/storage/refs/heads/master/benchmark.gif)

### Jesse MCP: Your AI Assistant, Connected to Jesse
Jesse includes a local [Model Context Protocol (MCP)](https://docs.jesse.trade/docs/mcp/) server. Connect your preferred AI assistant and let it work with Jesse's real tools and project context instead of merely guessing how your trading framework behaves.

Through Jesse MCP, an assistant can help you write and improve strategies, manage candle data, run and inspect backtests, perform rule significance tests, optimize parameters, run Monte Carlo simulations, and link you directly to the saved results in the Jesse dashboard. Your strategies and data remain under your control in your self-hosted Jesse setup.

For example, you can ask:

> Check whether my new entry rule is statistically significant, backtest it, optimize the promising parameters, and run a candles-based Monte Carlo analysis before we consider paper trading.

[Connect Claude, Codex, Cursor, VS Code, or Zed to Jesse →](https://docs.jesse.trade/docs/mcp/setup)

### Rule Significance Testing
Before spending hours building and tuning a complete strategy, test whether its entry rule has a measurable historical edge. Jesse compares the rule against a bootstrap distribution of random entries on the same market history, helping you reject noisy ideas early and focus your research on signals worth developing.

[Learn about Rule Significance Testing →](https://docs.jesse.trade/docs/rule-significance-testing/)

### Monte Carlo Analysis
Stress-test your strategies beyond a single historical path. Jesse's Monte Carlo mode runs hundreds of simulations using **trade-order shuffling** (tests whether trade timing drove your results) and **candles-based** (tests robustness under slightly different market conditions) methods. Use it to distinguish skill from luck, understand the range of outcomes you can realistically expect, and catch overfitting early.

### Machine Learning
Jesse includes a complete, end-to-end ML pipeline built for trading strategies:

1. **Gather data** — run a backtest in gather mode; call `record_features({...})` at each signal bar and `record_label(name, value)` when the outcome is known. Data is auto-saved to CSV.
2. **Train a model** — call `train_model()` with any scikit-learn–compatible estimator and choose a task type: `"binary"` classification, `"multiclass"` classification, or `"regression"`. Get a full report with feature importance, calibration, and metrics.
3. **Deploy** — switch to deploy mode and call `ml_predict()` or `ml_predict_proba()` inside your strategy. Model loading, scaling, and feature ordering are handled automatically.

```python
# Gather phase — inside your strategy
def before(self):
    self.record_features({
        'rsi': ta.rsi(self.candles),
        'adx': ta.adx(self.candles),
    })

# Deploy phase — gate entries with model confidence
def should_long(self):
    proba = self.ml_predict_proba()
    return proba['long'] > 0.65
```

[Explore Jesse's machine-learning pipeline →](https://docs.jesse.trade/docs/research/ml/)

### Research API and Jupyter Notebooks
Everything does not have to happen through the dashboard. Jesse's Research API exposes candle management, backtesting, optimization, Rule Significance Testing, Monte Carlo analysis, indicators, and machine learning to ordinary Python scripts and Jupyter notebooks. Use it for reproducible experiments, custom reports, batch research, or integration with your existing data-science workflow.

[Explore the Research API →](https://docs.jesse.trade/docs/research/)

### Rust-Powered Performance
Jesse's indicators are powered by native Rust, making them significantly faster than common alternatives such as TA-Lib.

### Reinforcement Learning — Coming Soon
We are working on first-class reinforcement-learning support built on Jesse's simulation and research stack. The goal is to make training, evaluating, and deploying reinforcement-learning agents feel as integrated as Jesse's existing backtesting, optimization, Monte Carlo, and machine-learning workflows.

### Optimize Your Strategies
Unsure about optimal parameters? Let the optimization mode decide using simple syntax. Fine-tune any strategy parameter with the Optuna library and easy cross-validation.

```python
@property
def slow_sma(self):
    return ta.sma(self.candles, self.hp['slow_sma_period'])

@property
def fast_sma(self):
    return ta.sma(self.candles, self.hp['fast_sma_period'])

def hyperparameters(self):
    return [
        {'name': 'slow_sma_period', 'type': int, 'min': 150, 'max': 210, 'default': 200},
        {'name': 'fast_sma_period', 'type': int, 'min': 20, 'max': 100, 'default': 50},
    ]
```

## Getting Started
Head over to the "getting started" section of the [documentation](https://docs.jesse.trade/docs/getting-started). The 
documentation is **short yet very informative**. 

## Resources

- [⚡️ Website](https://jesse.trade)
- [🎓 Documentation](https://docs.jesse.trade)
- [🎥 Youtube channel (screencast tutorials)](https://jesse.trade/youtube)
- [🛟 Help center](https://jesse.trade/help)
- [💬 Discord community](https://jesse.trade/discord)
- [🔌 Jesse MCP](https://docs.jesse.trade/docs/mcp/)

## What's next?

You can see the project's **[roadmap here](https://docs.jesse.trade/docs/roadmap.html)**. **Subscribe** to our mailing list at [jesse.trade](https://jesse.trade) to get the good stuff as soon they're released. Don't worry, We won't send you spam—Pinky promise.

## Disclaimer
This software is for educational purposes only. USE THE SOFTWARE AT **YOUR OWN RISK**. THE AUTHORS AND ALL AFFILIATES ASSUME **NO RESPONSIBILITY FOR YOUR TRADING RESULTS**. **Do not risk money that you are afraid to lose**. There might be **bugs** in the code - this software DOES NOT come with **ANY warranty**.

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `jesse/modes/__init__.py`
```python

```

#### File: `jesse/modes/import_candles_mode/drivers/Apex/__init__.py`
```python

```

#### File: `jesse/modes/import_candles_mode/drivers/Apex/omni_files/__init__.py`
```python

```

#### File: `jesse/modes/import_candles_mode/drivers/Bitfinex/__init__.py`
```python

```

#### File: `jesse/modes/import_candles_mode/drivers/Coinbase/__init__.py`
```python

```


==================================================


## [2/3] Repository: passivbot (`PHASE4-QUANT-110`)
- **Full Name**: `PHASE4-QUANT-110_enarjord__passivbot`
- **Description**: Trading bot running on Bybit, Bitget, OKX, GateIO, Binance, Kucoin, WEEX and Hyperliquid
- **GitHub Stars**: 2100
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
![Passivbot](docs/images/pbot_logo_full.svg)

# Trading bot running on Bybit, OKX, Bitget, Bitunix, GateIO, Binance, Kucoin, Hyperliquid and WEEX

:warning: **Used at one's own risk** :warning:

Latest tagged release: **[v8.1.0](docs/release_notes_v8.1.0.md)**.
A clone of `master` includes subsequent changes listed under
[Unreleased](CHANGELOG.md#unreleased). See [release status and version meanings](docs/releases.md)
before choosing a revision; these docs describe the revision you are viewing.

> **Upgrading from v7:** v8 is a breaking config and strategy release. Do not
> start v8 live with an unreviewed v7 config. Read the
> [v8.0.0 upgrade notes](docs/release_notes_v8.0.0.md) and use the explicit
> `passivbot tool migrate-config-v7` helper when preserving v7 trailing-grid
> behavior.


## Overview

Passivbot is a cryptocurrency trading bot written in Python and Rust, intended to require minimal user intervention.  

It operates on perpetual futures derivatives markets, automatically creating and cancelling limit buy and sell orders on behalf of the user. It does not try to predict future price movements or follow trends. Rather, it is a contrarian market maker, using price bands, EMA-derived context, and risk controls to provide resistance to price changes in both directions, thereby "serving the market" as a price stabilizer.

Order planning is computed by a shared Rust orchestrator used by both live trading and backtesting for speed and consistency. Also included is an optimizer, which finds better configurations by iterating thousands of backtests with different candidates, converging on the optimal ones with an evolutionary algorithm.  

## Strategy

The default `trailing_martingale` strategy starts with a small entry and can add to a position
as price moves against it, subject to configured exposure and risk limits. Re-entries change the
average entry price, while closes seek a configured profit margin or use trailing confirmation.
Entry sizes, distances, and trailing behavior are configurable.

The `ema_anchor` strategy is also available. `trailing_grid_v7` is a deprecated compatibility
strategy for explicit v7 migrations. See the [bot configuration guide](docs/config.bot.md) for
strategy-specific parameters.

### Trailing Orders
In addition to grid-based entries and closes, Passivbot may be configured to utilize trailing entries and trailing closes.

For trailing entries, the bot waits for the price to move beyond a specified threshold and then retrace by a defined percentage before placing a re-entry order. Similarly, for trailing closes, the bot waits before placing its closing orders until after the price has moved favorably by a threshold percentage and then retraced by a specified percentage. This may result in the bot locking in profits more effectively by exiting positions when the market shows signs of reversing instead of at a fixed distance from average entry price.

Grid and trailing orders may be combined, such that the robot enters or closes a whole or a part of the position as grid orders and/or as trailing orders.

### Forager
The Forager feature dynamically chooses which approved markets may open positions. It first prunes low relative-volume candidates, then ranks the remaining markets with configurable weights for quote volume, EMA readiness, and 1m log-range volatility.

### Unstucking Mechanism
Passivbot manages underperforming, or "stuck", positions by realizing small losses over time. If multiple positions are stuck, the bot prioritizes positions with the smallest gap between the entry price and current market price for "unstucking". Losses are limited by ensuring that the account balance does not fall under a set percentage below the past peak balance.  

## Installation

To install Passivbot and its dependencies, follow the steps below.

Passivbot supports **Python 3.12 and Python 3.14**. Python 3.13 is not supported by the pinned
dependency set.

### Upgrading a v7 config

V8 does not silently reinterpret v7 strategy fields. To preserve v7
trailing-grid behavior while moving the config into canonical v8 shape, run:

```sh
passivbot tool migrate-config-v7 \
  path/to/config_v7.json \
  path/to/config_v8_trailing_grid_v7.json \
  --report path/to/v7_migration_report.json
```

The helper writes the deprecated compatibility strategy `trailing_grid_v7`;
it does not translate the config into the new `trailing_martingale` strategy.
If unsupported or ambiguous fields require manual review, the command returns
nonzero and does not write the output config unless
`--allow-manual-review-output` is explicitly supplied. Review the report and
backtest the result before considering a live run. New configs and new
optimization work should start from
`configs/examples/default_trailing_martingale_long.json`.

### Step 1: Clone the Repository

First, clone the Passivbot repository to the local machine:

```sh
git clone https://github.com/enarjord/passivbot.git
cd passivbot
```

This checks out `master`. For a fixed tagged version, follow [release selection](docs/releases.md).


### Step 2: Install Rust
Passivbot uses Rust for some of its components. Install Rust by following these steps:

Visit https://www.rust-lang.org/tools/install
Follow the instructions to install Rustup, the Rust installer and version management tool.
After installation, restart the terminal or command prompt.

### Step 3: Create and Activate a Virtual Environment

Create a virtual environment to manage dependencies:

 **Linux/macOS:**
```sh
# Replace python3.14 with the installed supported executable (python3.12 or python3.14).
PYTHON_BIN=python3.14
"$PYTHON_BIN" --version
"$PYTHON_BIN" -m venv venv
```

 **Windows (Command Prompt or PowerShell):**
```cmd
py -3.12 -m venv venv
```

Activate the virtual environment:

 **Linux/macOS:**
```sh
source venv/bin/activate
```

 **Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

 **Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Passivbot

Choose the install profile that matches your use case:

- **Live-only VPS**: `python3 -m pip install -e .`
- **Backtesting / optimization / research workstation**: `python3 -m pip install -e ".[full]"`
- **Contributing / docs / lint tooling**: `python3 -m pip install -e ".[dev]"`

All profiles build the Rust extension and register the `passivbot` command.

Typical live-only install:

```sh
python3 -m pip install -e .
```

### Step 5 (optional): Build Rust Extensions

Passivbot will attempt to build the necessary Rust extensions automatically, but they can also be built manually by navigating to the `passivbot-rust` directory and using `maturin`:

```sh
cd passivbot-rust
maturin develop --release
cd ..
```

If changes in the Rust source are detected, recompilation is needed, which Passivbot will attempt to do automatically when starting. To manually recompile, use the commands given above.

### Step 6: Add API keys

Make a copy of the api-keys template file:

```sh
cp api-keys.json.example api-keys.json
```

Add your keys to api-keys.json.

### Step 7: Run Passivbot

> **Hint:**  
> To ensure cache folder names are Windows-compatible (even outside Windows), set the environment variable `WINDOWS_COMPATIBILITY=1`.   
> This is only required in certain scenarios, e.g., running under Docker (Linux) while mounting the `caches` folder to a Windows host.

To start the bot with the default settings, run:

```sh
passivbot live -u {account_name_from_api-keys.json}
```

or make a new configuration file, using `configs/examples/default_trailing_martingale_long.json` as a starting point, and start the bot with:


```sh
passivbot live path/to/config.json
```

Legacy direct-script entrypoints such as `python3 src/main.py ...`, `python3 src/backtest.py ...`,
and `python3 src/optimize.py ...` still work unchanged for backwards compatibility.

The canonical hardcoded defaults live in `src/config/schema.py`. The example config
`configs/examples/default_trailing_martingale_long.json` provides the maintained default strategy profile, so
copying it is the recommended starting point for new configs.

### Logging

Passivbot uses Python's logging module throughout the bot, backtester, and supporting tools.

- Use `--log-level {warning|info|debug|trace}` or `--log-level {0-3}` on `passivbot live` or `passivbot backtest` to adjust verbosity at runtime: `0 = warnings only`, `1 = info`, `2 = debug`, `3 = trace`.
- Use `--verbose` on `passivbot live` to force debug logging (`--log-level debug`).  
- Persist a default by adding a top-level section to your config: `"logging": {"level": 2}`. The CLI flag always overrides the config value for that run.
- `passivbot live` now writes a timestamped logfile under `logs/` by default and refreshes `logs/{user}.log` as a stable alias to the current run. On Windows without symlink privileges, that path is a small pointer file which Passivbot's monitor tooling follows automatically. Control this with `config.logging.persist_to_file`, `config.logging.dir`, and the optional rotation settings in `config.logging`.
- CandlestickManager and other subsystems inherit the chosen level so EMA warm-up, data fetching, and cache behaviour can be inspected consistently.

### Running Multiple Bots

Running several Passivbot instances on one machine is supported when each uses a separate
exchange account or subaccount. Do not run competing bots on the same account; see
[concurrent bot protection](docs/live.md#concurrent-passivbot-protection). Each process shares the same on-disk OHLCV cache, and the candlestick manager now uses short-lived, self-healing locks with automatic stale cleanup so that one stalled process cannot block the rest. No manual deletion of lock files is required; the bot removes stale locks on startup and logs whenever a lock acquisition times out.

## Jupyter Lab

JupyterLab is an optional separate install. Activate the bot virtual environment, then install and
launch it from the repository root:

```shell
python3 -m pip install jupyterlab
python3 -m jupyter lab
```

## Requirements

- Python 3.12 or 3.14 (Python 3.13 is not supported)
- `python3 -m pip install -e .` for live trading only
- `python3 -m pip install -e ".[full]"` for backtesting, optimization, downloader, and advanced tools
- `python3 -m pip install -e ".[dev]"` for contributor tooling on top of the full install

## Example configurations

Start from a maintained [example config](configs/examples/) and follow the
[config workflow](docs/config_workflow.md) to backtest and tune it for your use case.
Community configurations are also available at https://pbconfigdb.scud.dedyn.io/.

## Documentation

For more detailed information about Passivbot, see the [documentation index](docs/index.md).

Useful entry points:

- [Release status and upgrades](docs/releases.md)
- [Installation](docs/installation.md)
- [Config workflow](docs/config_workflow.md)
- [Configuration reference](docs/configuration.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Backtesting](docs/backtesting.md)
- [Optimizing](docs/optimizing.md)
- [Metrics reference](docs/metrics.md)
- [Equity Hard Stop Loss](docs/equity_hard_stop_loss.md)
- [Monitor output](docs/monitor.md)

## Support

[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/QAF2H2UmzZ)

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/passivbot_futures)

## Third Party Links, Referrals and Tip Jar

**Hyperliquid Reference Vault**
Passivbot's reference long-only config profile running on a Hyperliquid Vault:
https://app.hyperliquid.xyz/vaults/0x490af7d4a048a81db0f677517ed6373565b42349

**Passivbot GUI**
A graphical user interface for Passivbot:  
https://github.com/msei99/pbgui

**Referrals:**  
Signing up using these referrals is appreciated:  
https://accounts.binance.com/register?ref=TII4B07C  
https://partner.bybit.com/b/passivbot  
https://partner.bitget.com/bg/Y8FU1W  
https://www.okx.com/join/PASSIVBOT  
https://app.hyperliquid.xyz/join/PASSIVBOT  
https://www.kucoin.com/r/broker/CX8QZQJX  
https://www.weex.com/en/register?vipCode=ppc8

**Note on Binance**  
To support continued Passivbot development, please use a Binance account which  
1) was created after 2024-09-21 and  
2) either:  
  a) was created without a referral link, or  
  b) was created with referral ID: "TII4B07C".  
                                                                                      
Passivbot receives commissions from trades only for accounts meeting these criteria.  


**BuyMeACoffee:**  
https://www.buymeacoffee.com/enarjord  

**Donations:**  
If the robot is profitable, consider donating as showing gratitude for its development:  

- USDT or USDC Binance Smart Chain BEP20:  
0x4b7b5bf6bea228052b775c052843fde1c63ec530  
- USDT or USDC Arbitrum One:  
0x4b7b5bf6bea228052b775c052843fde1c63ec530  
- Zcash (ZEC):  
u1jlans93rrqusqx2wp5020aezyt0q22l4tuy7ezkna06fuyaa2gxzremf50wsj3k83a4cm0cncs6zt9urlpte7a3nzvq992z48jxzem455acmhmhhwfwjcjwl8z79vlznla0r3jln6ety565254h96whnllcmepmpqu3ft9hxtqvkn0m7  

Bitcoin (BTC) via Strike:  
enarjord@strike.me

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org/>

### Core Implementation Code & Architecture
#### File: `src/__init__.py`
```python

```

#### File: `src/exchanges/__init__.py`
```python

```

#### File: `src/optimization/__init__.py`
```python

```

#### File: `src/passivbot_version.py`
```python
__version__ = "8.1.0"
```

#### File: `src/tools/__init__.py`
```python
"""Passivbot auxiliary tools."""
```

#### File: `src/passivbot_cli/__init__.py`
```python
"""Unified Passivbot CLI package."""
```


==================================================


## [3/3] Repository: exploring-order-book-predictability (`PHASE4-QUANT-105`)
- **Full Name**: `PHASE4-QUANT-105_toma-x__exploring-order-book-predictability`
- **Description**: Deep learning approach for market price prediction, in JAX
- **GitHub Stars**: 60
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Exploring order book predictability in cryptocurrency markets in a deep learning perspective using JAX

[![](https://img.shields.io/badge/Open%20in%20Colab-View%20Notebook-blue?logo=google-colab)](https://colab.research.google.com/github/toma-x/exploring-order-book-predictability/blob/main/Exploring-book-predictability.ipynb)

## Overview

This project explores predictability in cryptocurrency markets, focusing on Bitcoin, the most widely known and liquid cryptocurrency. We use a Convolutional Neural Network (CNN), implemented with FLAX and [JAX](https://jax.readthedocs.io/en/latest/).
Our experiment shows clear sign of short/mid term predictability in a trading perspective.

## Business understanding

The [order book](https://www.investopedia.com/terms/o/order-book.asp) contains the bid and ask orders placed by all the market participants, this book convolve a lot of information on the current state of a given market. While this is difficult to use the order book and read it with the naked eye, a machine can efficiently read and extract crucial information from the order book. The objective of our analysis is to identify which books are leading to movements in the market.

## Data dowload and processing

The study referenced in [5] implies that the initial level provides the most valuable information. In line with this perspective, the data used is the BTCUSDT book ticker (the first level of the order book), publicly available for the first day of each month on [Tardis.dev](https://tardis.dev).
The notebook will automatically fetch historical order book data for BTCUSDT for the past six months, process the data, and prepare it for training.

## Training the Model

Recent developments in [1,2,3] show that a CNN can accurately learn from time series data, our model is also a CNN implemented with Flax and JAX.
Hyperparameters are tuned using the framework [Optuna](https://optuna.readthedocs.io/en/stable/index.html) and the model is trained on 10 epochs.
We log the metrics of the evaluation of the unseen test dataset, achieving 86% accuracy.

## Evaluation and Trading Strategy

The trading strategy is implemented based on the predictions, considering latency, slippage, and fees. The performance of the strategy is discussed and visualized, including wallet value over time and the Sharpe ratio, as in [4].
We present the results for difference confidence levels, and the impact of latency, slippage, and fees on the trading strategy is underlined.

## Conclusion

This project provides good insights into the predictability of order book data in cryptocurrency markets using a deep learning approach. It demonstrates the implementation of a trading strategy based on the model's predictions and evaluates its performance under realistic trading conditions. The use of such a predictive system could easily be wrapped within a trading bot for automated use, if able of consistently producing reliable predictions. 

## References

 - [1] [DeepLOB: Deep convolutional neural networks for limit order books](https://arxiv.org/abs/1808.03668) - Zhang Z, Zohren S, Roberts S.
 - [2] [Deep Order Flow Imbalance: Extracting Alpha at Multiple Horizons from the Limit Order Book](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3900141) - Kolm, Petter N. et al.
 - [3] [THE SHORT-TERM PREDICTABILITY OF RETURNS IN ORDER BOOK MARKETS: A DEEP LEARNING PERSPECTIVE](https://arxiv.org/pdf/2211.13777.pdf) - Lucchese L, S.Pankkanen M, E.D.Veraart A.
 - [4] [Order Flow Imbalance - A High-Frequency Trading Signal](https://dm13450.github.io/2022/02/02/Order-Flow-Imbalance.html) - Dean Markwick.
 - [5] [How informative is the Order Book Beyond the Best Levels? Machine Learning Perspective](https://arxiv.org/pdf/2203.07922.pdf) - Tran D, Kanniainen J, Iosifidis A.


==================================================
