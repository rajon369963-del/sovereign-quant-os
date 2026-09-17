# ⚡ [QUANT-SOURCE-195] Consolidated Quant & Algo Trading Repositories
**Category**: `EVENT_DRIVEN_BACKTESTERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_195_EVENT_DRIVEN_BACKTESTERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: zipline-trader (`WHEEL_zipline-trader`)
- **Full Name**: `zipline-trader`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
.. image:: https://readthedocs.org/projects/zipline-trader/badge/?version=latest
   :target: https://zipline-trader.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://github.com/shlomikushchi/zipline-trader/workflows/Zipline%20CI%20(Ubuntu)/badge.svg
   :target: https://github.com/shlomikushchi/zipline-trader/workflows/Zipline%20CI%20(Ubuntu)/badge.svg
   :alt: Github Actions
.. image:: https://github.com/shlomikushchi/zipline-trader/workflows/Zipline%20CI%20(Windows)/badge.svg
   :target: https://github.com/shlomikushchi/zipline-trader/workflows/Zipline%20CI%20(Windows)/badge.svg
   :alt: Github Actions
.. image:: https://github.com/shlomikushchi/zipline-trader/workflows/Zipline%20CI%20(macOS)/badge.svg
   :target: https://github.com/shlomikushchi/zipline-trader/workflows/Zipline%20CI%20(macOS)/badge.svg
   :alt: Github Actions

|

.. image:: ./images/zipline-live2.small.png
    :target: https://github.com/shlomikushchi/zipline-trader
    :width: 212px
    :align: center
    :alt: zipline-live

zipline-trader
==============

Welcome to zipline-trader, the on-premise trading platform built on top of Quantopian's
`zipline <https://github.com/quantopian/zipline>`_.

This project is meant to be used for backtesting/paper/live trading with one the following brokers:
 * Interactive Brokers
 * Alpaca


Please `Read The Docs <https://zipline-trader.readthedocs.io/en/latest/index.html#>`_

And you could find us on `slack <https://join.slack.com/t/zipline-live/shared_invite/zt-mrsrfhky-usB0SEU4st1SuMUCErUevA>`_

### Core Implementation Code & Architecture
#### File: `tests/metrics/__init__.py`
```python

```

#### File: `tests/pipeline/__init__.py`
```python

```

#### File: `tests/resources/__init__.py`
```python

```

#### File: `tests/resources/fetcher_inputs/__init__.py`
```python

```

#### File: `tests/utils/__init__.py`
```python

```

#### File: `tests/live/__init__.py`
```python

```


==================================================


## [2/3] Repository: trademind (`PHASE4-QUANT-062`)
- **Full Name**: `PHASE4-QUANT-062_jialuechen__trademind`
- **Description**: Hybrid Event-driven and Vectorized Strategy Backtesting Library
- **GitHub Stars**: 128
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# TradeMind: C++ Algorithmic Trading and Backtesting Framework

TradeMind is a high-performance, professional-grade quantitative trading platform designed for algorithmic trading, with a focus on low-latency execution, advanced strategy development, and real-time market microstructure visualization analysis.

## System Architecture

![Quantitative Trading Platform System Architecture](assets/architecture.png)

The platform consists of five key layers:

1. **Exchanges and Data Sources Layer**
   - Connects to stock and futures exchanges
   - Integrates with data vendors and real-time feeds
   - Provides raw market data for processing

2. **Trading and Data Connectivity Layer**
   - FIX Engine for low-latency exchange communication
   - WebSocket APIs for modern connectivity
   - Data collectors and market data adapters

3. **Core Engine Layer (C++)**
   - High-performance order book engine
   - Sophisticated order management system
   - Strategy execution engine
   - Real-time risk management

4. **Strategy Development Layer (Python)**
   - Flexible strategy framework for algorithm development
   - Comprehensive backtesting engine for strategy evaluation

5. **Analysis & Visualization Layer**
   - Transaction cost analysis to optimize trading performance
   - Real-time visualization of market data and system metrics

All these components are supported by a robust **Distributed Infrastructure** layer that includes:
   - ZeroMQ message bus for low-latency inter-component communication
   - Docker containerization for deployment flexibility
   - Kubernetes orchestration for scaling and management
   - Comprehensive monitoring and automatic recovery systems

## Key Features

- **High-Performance Core Engine**: C++ implementation of critical components ensures microsecond-level response time
- **Real-time Market Microstructure Analysis**: Capture and analyze order book dynamics and liquidity metrics
- **Flexible Strategy Development**: Python API for rapid strategy development using machine learning and quantitative models
- **Comprehensive Backtesting**: Event-driven backtesting engine with realistic market simulation
- **Low-Latency Order Execution**: FIX protocol integration for direct exchange connectivity
- **Distributed Architecture**: Microservices design with ZeroMQ messaging for horizontal scalability
- **Cloud-Ready Deployment**: Containerized services that can be deployed in cloud environments

## Getting Started

### Prerequisites

- C++17 compatible compiler (GCC 7+, Clang 5+, MSVC 2019+)
- CMake 3.15+
- Python 3.8+
- ZeroMQ 4.3+
- Boost 1.70+
- Fix8 (for FIX protocol support)
- YAML-CPP

### Building from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/jialuechen/trademind.git
   cd trademind
   ```

2. Build the C++ components:
   ```bash
   mkdir build && cd build
   cmake ..
   make -j$(nproc)
   ```

3. Install the Python package:
   ```bash
   cd python
   pip install -e .
   ```

### Configuration

Edit the configuration files in the `config` directory to set up:

- Exchange connections
- Market data sources
- Risk parameters
- Logging preferences
- Performance settings

Example configuration is provided in `config/config.yaml`.

### Running the Platform

To start the platform with default settings:

```bash
./bin/trademind
```

To specify a custom configuration file:

```bash
./bin/trademind --config /path/to/custom_config.yaml
```

## Strategy Development

TradeMind provides a powerful Python API for developing trading strategies. Here's a minimal example:

```python
from pyquant import Strategy, Context, OrderSide, OrderType

class SmaStrategy(Strategy):
    def initialize(self) -> None:
        # Set strategy parameters
        self.parameters = {
            "symbol": "AAPL",
            "fast_period": 10,
            "slow_period": 30,
            "trade_size": 100
        }
        
        # Add symbols to trade
        self.context.symbols = [self.parameters["symbol"]]
        
    def on_bar(self, context: Context, bar_dict) -> None:
        symbol = self.parameters["symbol"]
        bars = bar_dict[symbol]
        
        # Calculate moving averages
        fast_ma = bars['close'].rolling(self.parameters["fast_period"]).mean()
        slow_ma = bars['close'].rolling(self.parameters["slow_period"]).mean()
        
        # Get current position
        position = context.get_position(symbol)
        
        # Trading logic: Buy when fast MA crosses above slow MA
        if fast_ma.iloc[-2] <= slow_ma.iloc[-2] and fast_ma.iloc[-1] > slow_ma.iloc[-1]:
            if position.quantity <= 0:
                self.buy(symbol, self.parameters["trade_size"])
                
        # Sell when fast MA crosses below slow MA
        elif fast_ma.iloc[-2] >= slow_ma.iloc[-2] and fast_ma.iloc[-1] < slow_ma.iloc[-1]:
            if position.quantity >= 0:
                self.sell(symbol, self.parameters["trade_size"])
```

## Backtesting

To backtest a strategy:

```python
from pyquant import BacktestEngine, BacktestVisualizer, Timeframe
import pandas as pd

# Load historical data
data = pd.read_csv("data/AAPL_daily.csv", index_col='date', parse_dates=True)

# Create and configure strategy
strategy = SmaStrategy()

# Set up backtest engine
backtest = BacktestEngine()
backtest.add_strategy(strategy)
backtest.add_bar_data("AAPL", Timeframe.D1, data)

# Run backtest
results = backtest.run(
    start_time=data.index[100],
    end_time=data.index[-1],
    initial_capital=100000.0
)

# Visualize results
visualizer = BacktestVisualizer()
visualizer.generate_report(results)
```

## Parameter Optimization

TradeMind includes tools for strategy parameter optimization:

```python
from pyquant import StrategyOptimizer

# Create optimizer
optimizer = StrategyOptimizer(SmaStrategy)
optimizer.add_bar_data("AAPL", Timeframe.D1, data)

# Define parameter grid
param_grid = {
    "fast_period": [5, 10, 15, 20],
    "slow_period": [20, 30, 40, 50],
}

# Run grid search
best_params = optimizer.grid_search(
    param_grid=param_grid,
    start_time=data.index[100],
    end_time=data.index[-1],
    optimize_metric='sharpe_ratio'
)

print(f"Best parameters: {best_params}")
```

## Distributed Deployment

For production environments, TradeMind can be deployed as a distributed system using Docker and Kubernetes:

```bash
cd docker
docker-compose up -d
```

For Kubernetes deployment:

```bash
kubectl apply -f kubernetes/trademind.yaml
```

## Contributing

Contributions are welcome! Please check out our [contributing guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, or suggest improvements.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Core Implementation Code & Architecture
#### File: `examples/quantum_regression_example.py`
```python
import numpy as np
from tfq_finance.ml.quantum_regression import train_quantum_regression_model

train_data = np.random.randn(100, 4)
train_labels = np.random.randn(100)

model = train_quantum_regression_model(train_data, train_labels)
print("Quantum Regression Model Trained")
```

#### File: `examples/order_placement_example.py`
```python
from tfq_finance.execution.order_placement import place_order

def order_placement_example():
    order_details = {'symbol': 'AAPL', 'quantity': 100, 'order_type': 'market'}

    order_confirmation = place_order(order_details)
    print("Order Confirmation:", order_confirmation)

if __name__ == "__main__":
    order_placement_example()
```

#### File: `examples/high_frequency_trading_example.py`
```python
import numpy as np
from tfq_finance.execution.high_frequency_trading import high_frequency_trading_signal

def high_frequency_trading_example():
    prices = np.array([100, 101, 102, 101, 100, 99, 100])

    signal = high_frequency_trading_signal(prices)
    print("High Frequency Trading Signal:", signal)

if __name__ == "__main__":
    high_frequency_trading_example()
```

#### File: `examples/liquidity_management_example.py`
```python
import numpy as np
from tfq_finance.optimization.liquidity_management import manage_liquidity

def liquidity_management_example():
    cash_flows = np.random.randn(100)
    liquidity_needs = 0.05

    liquidity_plan = manage_liquidity(cash_flows, liquidity_needs)
    print("Liquidity Management Plan:", liquidity_plan)

if __name__ == "__main__":
    liquidity_management_example()
```

#### File: `examples/credit_risk_example.py`
```python
from tfq_finance.risk_management.credit_risk import calculate_credit_value_at_risk

def credit_risk_example():
    exposure = 1000000
    probability_of_default = 0.02
    confidence_level = 0.95

    cvar = calculate_credit_value_at_risk(exposure, probability_of_default, confidence_level)
    print("Credit Value at Risk:", cvar)

if __name__ == "__main__":
    credit_risk_example()
```

#### File: `examples/portfolio_optimization_example.py`
```python
import numpy as np
from tfq_finance.optimization.portfolio_optimization import optimize_portfolio

def portfolio_optimization_example():
    returns = np.random.randn(100, 4)
    risk_aversion = 0.5

    optimal_weights = optimize_portfolio(returns, risk_aversion)
    print("Optimal Portfolio Weights:", optimal_weights)

if __name__ == "__main__":
    portfolio_optimization_example()
```


==================================================


## [3/3] Repository: intelligent-trading-bot (`PHASE4-QUANT-112`)
- **Full Name**: `PHASE4-QUANT-112_asavinov__intelligent-trading-bot`
- **Description**: Intelligent Trading Bot: Automatically generating signals and trading based on machine learning and feature engineering
- **GitHub Stars**: 1874
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
```
 ___       _       _ _ _                  _     _____              _ _               ____        _ 
|_ _|_ __ | |_ ___| | (_) __ _  ___ _ __ | |_  |_   _| __ __ _  __| (_)_ __   __ _  | __ )  ___ | |_
 | || '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \| __|   | || '__/ _` |/ _` | | '_ \ / _` | |  _ \ / _ \| __|
 | || | | | ||  __/ | | | (_| |  __/ | | | |_    | || | | (_| | (_| | | | | | (_| | | |_) | (_) | |_ 
|___|_| |_|\__\___|_|_|_|\__, |\___|_| |_|\__|   |_||_|  \__,_|\__,_|_|_| |_|\__, | |____/ \___/ \__|
                         |___/                                               |___/                   
₿   Ξ   ₳   ₮   ✕   ◎   ●   Ð   Ł   Ƀ   Ⱥ   ∞   ξ   ◈   ꜩ   ɱ   ε   ɨ   Ɓ   Μ   Đ  ⓩ  Ο   Ӿ   Ɍ  ȿ
```

> [![https://t.me/intelligent_trading_signals](https://img.shields.io/badge/Telegram-2CA5E0?logo=telegram&style=for-the-badge&logoColor=white)](https://t.me/intelligent_trading_signals) 📈 **<span style="font-size:1.5em;">[Intelligent Trading Signals](https://t.me/intelligent_trading_signals)</span>** 📉 **<https://t.me/intelligent_trading_signals>**

# Intelligent trading bot

The aim of the project is to develop an intelligent trading bot for automated trading including cryptocurrencies using state-of-the-art machine learning (ML) algorithms and feature engineering. The project provides the following major functionalities:
* Clear and consistent separation between *offline* (batch) mode for training ML models and *online* (stream) mode for predicting based on the trained models. One of the main challenges here is to guarantee that the same (derived) features are used in both modes
* Extensible approach to defining *derived features* using (Python) functions including standard technical indicators as well as arbitrary custom features
* Providing possibility to work with different *trade frequencies* (time rasters), for example, 1 minute, 1 hour or 1 day
* Customizable functions for sending signals or predictions in online mode, for example, sending to Telegram channels, API end-point, storing in a database or executing real transactions
* Functions for *backtesting* and measuring trade performance on historic data which is more difficult because requires periodic re-train of the used ML models
* *Trading service* for online mode which uses a configuration file to regtularly retrieve data updates, do analysis and send signals or execute trade transactions

# Intelligent trading signals

The signaling service is running in cloud and sends its signals to this Telegram channel:

📈 **[Intelligent Trading Signals](https://t.me/intelligent_trading_signals)** 📉 **<https://t.me/intelligent_trading_signals>**

Everybody can subscribe to the channel to get the impression about the signals this bot can generate.

Currently, the bot is configured using the following parameters:
* Exchange: Binance
* Cryptocurrency: ₿ Bitcoin (BTCUSDT)
* Analysis frequency: 1 minute
* Intelligent indicator between -1 and +1. Negative values mean decrease, and positive values mean increase of the price

Example notification: 

> ₿ 24.518 📉📉📉 Score: -0.26

The first number is the latest close price. The score -0.26 means that it is very likely to see the price lower than the current close price. 

If the intelligent indicator exceeds some threshold specified in the model then buy or sell signal is generated:

> 〉〉〉📈 ₿ 74,896 Indicator: +0.12 ↑ BUY ZONE 1min

Here three arrows mean buy signal for bitcoin at the current price 74,896 and the indicator value 0.12. `1min` frequence (analysis every minute). Such messages can be customized using Python functions including diagrams.  

# Training machine learning models (offline)

![Batch data processing pipeline](docs/images/fig_1.png)

For the signaler service to work, a number of ML models must be trained and the model files available for the service. All scripts run in batch mode by loading some input data and storing some output files. The batch scripts are located in the `scripts` module.

If everything is configured, then the following scripts have to be executed:
* `python -m scripts.download -c config.json`
* `python -m scripts.merge -c config.json`
* `python -m scripts.features -c config.json`
* `python -m scripts.labels -c config.json`
* `python -m scripts.train -c config.json`
* `python -m scripts.predict -c config.json`
* `python -m scripts.signals -c config.json`
* `python -m scripts.output -c config.json`

All necessary parameters are provided in the configuration file. The project provides some sample configuration files in the `config` folder.

Some common parameters of the configuration file:
* `data_folder` - location of data files which are needed only for batch offline mode
* `symbol` it is a trading pair like `BTCUSDT`
* `description` Any text helping understand the purpose of this configuration file
* `freq` data frequency according to `pandas` conventions

## Download data 

This batch script will download historic data from one or more data sources and store them in separate files. The data sources are listed in the `data_sources` section. One entry in this list specifies a data source as well as `column_prefix` used to distinguish columns with the same name from different sources. Currently data sources are not extendable and it is possible only to download from Binance and Yahoo.

## Merging source data

The downloaded data are stored in multiple files. The system however works with only one data table therefore all these data entries (like candle lines) must be merged into one table. This is done by the `merge` script. It aligns all data entries according to their time stamp, that is, one record in the output file will merge records with the same time stamp from all input files. In addition, it will produce continuous raster in case there are gaps in the input files.  

## Generate features

This script is intended for computing derived features. These features will be added as additional columns to the data table. Feature definitions are provided in the `feature_sets` section of the configuration file. Each entry in this list specifies a *feature generator* as well as its parameters. The script loads one merged input file, applies feature generation procedures and stores all derived features in an output file. 

Here are some notes on the current implementation: 
* Not all generated features must be used for training and prediction. Some of them can be used as input to next features. Other feature could be used only for the feature selection process where we want to find which of them have better predictive power. For the train/predict phases, a separate explicit list of features is specified 
* Currently it runs in non-incremental model by computing features for *all* available input records (and not only for the latest update), and hence it may take hours for complex configurations. Yet, in online (stream) mode, features can be computed more efficiently if it is supported by the feature generator
* Feature generation functions get additional parameters like windows from the config section
* The same features must be used in online (stream) mode (in the service when they are applied to a micro-batch) and offline mode. This is guaranteed by design

Here are some pre-defined feature generators (although it is possible to define custom feature generation functions):
* `talib` feature generator relies on the TA-lib technical analysis library. Here an example of its configuration: `"config":  {"columns": ["close"], "functions": ["SMA"], "windows": [5, 10, 15]}`
* `itbstats` feature generator implements functions which can be found in tsfresh like `scipy_skew`, `scipy_kurtosis`, `lsbm` (longest strike below mean), `fmax` (first location of maximum), `mean`, `std`, `area`, `slope`. Here are typical parameters: `"config":  {"columns": ["close"], "functions": ["skew", "fmax"], "windows": [5, 10, 15]}`   
* `itblib` feature generator implemented in ITB but most of its features can be generated (much faster) via talib
* `tsfresh` generates functions from the tsfresh library

## Generate labels

This script is similar to feature generation because it adds new columns to the input file. However, these columns describe something that we want to predict and what is not known when executing in online mode. In other words, features are computed from previous (historic) data while labels are computed from future data which are not visible in online mode yet. For example, a label could find maximum price increase during next hour in percent. Computationally it is the same as computing features but this step is separate because we do not need (and cannot compute) this in online mode. This script will apply all labels defined in the `label_sets` section, add them as new columns and store the result in the output file. Just like for features, not all labels must be really used -- they could be generated for exploratory purposes. The really used labels are listed in the `labels` section.

Here are some pre-defined label generators:
* `highlow` label generator returns True if the price is higher than the specified threshold within some future horizon
* `highlow2` Computes future increases (decreases) with the conditions that there are no significant decreases (increases) before that. Here is its typical configuration: `"config":  {"columns": ["close", "high", "low"], "function": "high", "thresholds": [1.0, 1.5, 2.0], "tolerance": 0.2, "horizon": 10080, "names": ["first_high_10", "first_high_15", "first_high_20"]}`
* `topbot` Deprecated
* `topbot2` Computes maximum and minimum values (labeled as True). Every labelled maximum (minimum) is guaranteed to be surrounded by minimums (maximums) lower (higher) than the specified level. The required minimum difference between adjacent minimums and maximums is specified via `level` parameters. The tolerance parameter allows for including also points close to the maximum/minimum. Here is a typical configuration: `"config":  {"columns": "close", "function": "bot", "level": 0.02, "tolerances": [0.1, 0.2], "names": ["bot2_1", "bot2_2"]}`

## Train prediction models

This script is needed only in batch (offline) mode and its purpose is to analyze historic data and produce ML models as output files. These ML models store in a condensed form some knowledge about the time series and they are used then in online (stream) model for forecasting. More specifically, one ML model is trained to predict some label based on the generated features. When this model is applied to the latest data in online mode, it will predict the value of this label which is normally used to make some trade decision.

The parameters for the train script are specified in the `train_feature_sets` section. Currently classification and regression algorithms can be used. They can automatically scale input features if specified in the configuration. The trained models are applied to the train data set and the prediction scores are stored in this file `prediction-metrics.txt`.

## Post-processing

After ML models were applied and some predictions were generated as new columns (in online mode), we might want to compute something else based on these predictions. It is very similar to normal feature generation with the difference that it is done after predictions. Frequently we want to aggregate the predictions generated by ML algorithms for different labels and produce one *intelligent indicator* which is supposed to be used for making trade decisions. These computations are performed according to parameters in the `signal_sets` section which has same structure as feature generators. The result is one or more new columns.

## Output signal generation

Each previous step adds new columns to the data table with historic (in batch mode) or latest (in stream model) data table. Yet, we need to provide some functions for interacting with external systems, for example, sending messages, storing signals in the database or executing real transactions (buying or selling some assets). How it is done is configured in the `output_sets`. Each entry in this list specifies a function which is supposed to do some interaction with an external system. For example, the generator `score_notification_model` will send a message to the configured Telegram channel.

## Backtesting

When training ML models we need to find the best hyper-parameters. This is done in some traditional ways and is not explicitly supported by this framework. Yet, even if we find good hyper-parameters this does not guarantee that our trade performance will be good. The ultimate criterion for choosing among various features, labels, ML algorithms and their hyper-parameters is trade performance. Computing real (or close to real) trade performance is supported by the following two scripts working with historic data and helping to estimate trade performance of the whole pipeline. 

The `predict_rolling` script applies prediction to some data (similar to the `predict` script) but does it by regularly re-training ML models. This makes the predictions much more realistic because the models are applied to unseen data only (data which is was not used for training) but the models are regularly re-trained after enough new data was collected. It is precisely what is done in real system but this script applies this to historic data. The scripts implements rolling walk-forward splits by training the models for each using previous data and applying them for predicting the next predict interval.

The `simulate` script applies some (pre-defined) logic of trading to historic data which includes all data expected in online mode. Essentially, it scans the historic data by applying the trade rules and produces buy-sell transactions which are then aggregated.

# Online service

This script starts a service: `python -m service.server -c config.json`

The service will periodically (for example, every minute) execute these tasks:
* Retrieve the latest data from the server and update the current data window which includes some history (the history length is defined by a configuration parameter)
* Compute derived features based on the nearest history collected (which now includes the latest data). The features to be computed are described in the configuration file and are exactly the same as used in batch mode during model training
* Apply several (previously trained) ML models by predicting values of the labels which are also treated as (more complex) derived features. Trained models are loaded from the `MODELS` folder specified in the configuration file
* Aggregate the results of forecasting produced by different ML models and compute the final signal score which reflects the strength of the upward or downward trend. Here we use many previously computed scores as inputs and derive one output score. 
* Execute functions for interacting with external systems, for example, by sending notifications to a Telegram channel. It is also possible to configure a real trader which will execute buy or sell transactions

# Related projects

- https://github.com/CryptoSignal/Crypto-Signal Github.com/CryptoSignal - #1 Quant Trading & Technical Analysis Bot
- https://github.com/tensortrade-org/tensortrade An open source reinforcement learning framework for training, evaluating, and deploying robust trading agents
- https://github.com/Superalgos/Superalgos Free, open-source crypto trading bot, automated bitcoin / cryptocurrency trading software, algorithmic trading bots. Visually design your crypto trading bot, leveraging an integrated charting system, data-mining, backtesting, paper trading, and multi-server crypto bot deployments
- https://github.com/kieran-mackle/AutoTrader A Python-based development platform for automated trading systems - from backtesting to optimisation to livetrading
- https://github.com/areed1192/python-trading-robot A trading robot, that can submit basic orders in an automated fashion using the TD API
- https://github.com/jmrichardson/tuneta Intelligently optimizes technical indicators and optionally selects the least intercorrelated for use in machine learning models
- https://github.com/Erfaniaa/binance-futures-trading-bot Easy-to-use multi-strategic automatic trading for Binance Futures with Telegram integration
- https://github.com/smileinnovation/cryptocurrency-trading How to make profits in cryptocurrency trading with machine learning

Backtesting
- https://github.com/nautechsystems/nautilus_trader
- https://github.com/mementum/backtrader
- https://github.com/kernc/backtesting.py

External integrations
- https://github.com/ccxt/ccxt A JavaScript / Python / PHP cryptocurrency trading API with support for more than 100 bitcoin/altcoin exchanges
- https://github.com/aiogram/aiogram Is a pretty simple and fully asynchronous framework for Telegram Bot API
- https://github.com/sammchardy/python-binance

### Core Implementation Code & Architecture
#### File: `common/__init__.py`
```python

```

#### File: `scripts/__init__.py`
```python

```

#### File: `service/__init__.py`
```python
__version__ = '0.8.dev'
```

#### File: `common/types.py`
```python
from decimal import Decimal
from enum import Enum

class Venue(Enum):
    YAHOO = "yahoo"
    BINANCE = "binance"
    MT5 = "mt5"
    
class AccountBalances:
    """
    Available assets for trade
    """
    # Can be set by the sync/recover function or updated by the trading algorithm
    base_quantity = "0.04108219"  # BTC owned (on account, already bought, available for trade)
    quote_quantity = "1000.0"  # USDT owned (on account, available for trade)


# mt5.AccountInfo
class MT5AccountInfo:
    balance: Decimal = "10000"
    equity: Decimal = "10000"
    margin: Decimal = "0"
    margin_free: Decimal = "10000"
    margin_level: Decimal = "10000"
    profit: Decimal = "0"
    login: int = 0
    currency: str = "USD"
    name: str = ""
    server: str = ""
    leverage: int = 1
```

#### File: `inputs/__init__.py`
```python
from common.types import Venue

def get_collector_functions(venue: Venue):
    if venue == venue.BINANCE:
        from inputs.collector_binance import fetch_klines, health_check
        return fetch_klines, health_check
    elif venue == Venue.YAHOO:
        raise NotImplementedError(f"Collector functions not implemented for this venue: {venue}")
    elif venue == venue.MT5:
        from inputs.collector_mt5 import fetch_klines, health_check
        return fetch_klines, health_check
    else:
        raise ValueError(f"Unknown collector type: {venue}")

def get_download_functions(venue: Venue):
    if venue == venue.BINANCE:
        from inputs.collector_binance import download_klines
        return download_klines
    elif venue == Venue.YAHOO:
        from inputs.collector_yahoo import download_klines
        return download_klines
    elif venue == venue.MT5:
        from inputs.collector_mt5 import download_klines
        return download_klines
    else:
        raise ValueError(f"Unknown venue {venue} or downloader for the venue not implemented")
```

#### File: `tests/test_classifiers.py`
```python
import pytest

from common.utils import *
from common.classifier_gb import train_predict_gb
from common.classifier_nn import train_predict_nn
from common.classifier_lc import train_predict_lc

def test_nan_handling_predict():
	"""Predicted input has nans. These nans rows have to be removed before prediction but the output has to contain all rows including these nan rows."""

	is_scale = True  # Try with both False and True (explicitly)

	df_X = pd.DataFrame({"x": [1, 2, 3, 2, 1], "y": [0, 1, 0, 1, 0]})  # Input has no nans
	df_X_test = pd.DataFrame({"x": [1, 2, None, 2, np.nan], "y": [0, 1, 0, 1, 0]})  # Has nans

	test_hat = train_predict_gb(
		df_X[["x"]], df_X["y"], df_X_test[["x"]],
		model_config=dict(is_scale=is_scale, objective="cross_entropy", max_depth=1, learning_rate=0.1, num_boost_round=2),
	)
	assert 5 == len(test_hat)
	assert 2 == test_hat.isnull().sum()

	test_hat = train_predict_nn(
		df_X[["x"]], df_X["y"], df_X_test[["x"]],
		model_config=dict(is_scale=is_scale, learning_rate=0.5, n_epochs=1, bs=2),
	)
	assert 5 == len(test_hat)
	assert 2 == test_hat.isnull().sum()

	test_hat = train_predict_lc(
		df_X[["x"]], df_X["y"], df_X_test[["x"]],
		model_config=dict(is_scale=is_scale),
	)
	assert 5 == len(test_hat)
	assert 2 == test_hat.isnull().sum()

	pass
```


==================================================
