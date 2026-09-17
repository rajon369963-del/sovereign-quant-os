# ⚡ [QUANT-SOURCE-116] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_116_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: futu_algo (`PHASE4-QUANT-134`)
- **Full Name**: `PHASE4-QUANT-134_billpwchan__futu_algo`
- **Description**: Futu Algorithmic Trading Solution (Python) 基於富途OpenAPI所開發量化交易程序
- **GitHub Stars**: 590
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">
  <img alt="FutuAlgo Logo" src="https://raw.githubusercontent.com/billpwchan/futu_algo/master/images/logo.png" width="400px" />

**billpwchan/futu-algo API Reference Documentation**

<a href="https://www.buymeacoffee.com/billpwchan98" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9bd8017de7e94474aa5254c5061f17d6)](https://app.codacy.com/gh/billpwchan/futu_algo?utm_source=github.com&utm_medium=referral&utm_content=billpwchan/futu_algo&utm_campaign=Badge_Grade_Settings)

[![Issues](https://img.shields.io/github/issues/billpwchan/futu_algo?style=for-the-badge)](https://github.com/billpwchan/futu_algo/issues)
[![License](https://img.shields.io/github/license/billpwchan/futu_algo?style=for-the-badge)](https://github.com/billpwchan/futu_algo/blob/master/LICENSE)
[![LastCommit](https://img.shields.io/github/last-commit/billpwchan/futu_algo?style=for-the-badge)](https://github.com/billpwchan/futu_algo/blob/master/LICENSE)
[![CommitActivity](https://img.shields.io/github/commit-activity/y/billpwchan/futu_algo?style=for-the-badge)](https://github.com/billpwchan/futu_algo/commits/master)
[![WorkflowStatus](https://img.shields.io/github/workflow/status/billpwchan/futu_algo/CodeQL?style=for-the-badge)](https://github.com/billpwchan/futu_algo/commits/master)
[![RepoSize](https://img.shields.io/github/repo-size/billpwchan/futu_algo?style=for-the-badge)](https://github.com/billpwchan/futu_algo)
[![Languages](https://img.shields.io/github/languages/top/billpwchan/futu_algo?style=for-the-badge)](https://github.com/billpwchan/futu_algo)

</div>

## Highlights

- **Supported Platforms and Markets**

  Futu_algo is a algorithmic trading solution developed based on FutuOpenD and FutuOpenAPI. Fully support FutuNiuNiu and
  FutuMooMoo users in Hong Kong stock market. *(More market support is coming soon)*
- **Historical K-Line Data**

  Allow users to automatically downloading historical data for your interested stocks into CSV and storing to SQLite
  database for backtesting. *(up to 1M level for max. 2 years, or 1D level for max. 10 years)*
- **Backtesting Trading Strategies (BETA)**

  Backtest your own trading strategies on historical data with a summarized reports and visualizations using Pyfolio.
  For more demanding users, feel free to other commercial solutions such as Amibroker for backtesting.
- **Algorithmic Trading**

  Real-time low-latency trading features that allows applying your own basket of trading strategies on your stock pool.
  User can specify the trading strategy to be used for each stock based on their preference.

  ***EXAMPLE: 0.01s/STOCK TO DECIDE BUY/SELL ORDER WITH A 3-TECHNICAL INDICATORS STRATEGY (MACD, KDJ AND CLOSE PRICE)***

- **Advanced Stock Screener**

  Screens high-quality stocks using your own stock screening strategies, and notify your friends using the email
  subscription feature. **Feel free to subscribe by submitting this Google Form! https://forms.gle/C9y4kyYUArKmFzu86**
- **Trading Strategy Editor**

  Write your own trading strategy following a simple template (buy, sell, calculate technical indicators). Common
  strategies such as MACD and KDJ-based trading rules are provided as guidelines.
- **GUI Support (Upcoming)**

  Easy-to-use GUI for users to adjust their configurations, trading, downloading data and filtering stocks within one
  application. No longer need to type any command for trading!

## Version Guidance

| FutuAlgo Release | Futu OpenAPI Specification |
|:-----------------|:---------------------------|
| 1.0              | 6.1                        |

## Deployment

### Pre-Requisite: Configuration File (Config.ini)

```ini
[FutuOpenD.Config]
Host = <OpenD Host>
Port = <OpenD Port>
WebSocketPort = <OpenD WebSocketPort>
WebSocketKey = <OpenD WebSocketKey>
TrdEnv = <SIMULATE or REAL>

[FutuOpenD.Credential]
Username = <Futu Login Username>
Password_md5 = <Futu Login Password Md5 Value>

[FutuOpenD.DataFormat]
HistoryDataFormat = ["code","time_key","open","close","high","low","pe_ratio","turnover_rate","volume","turnover","change_rate","last_close"]
SubscribedDataFormat = None

[TradePreference]
LotSizeMultiplier = <# of Stocks to Buy per Signal>
MaxPercPerAsset = <Maximum % of Capital Allocated per Asset>
StockList = <Subscribed Stocks in List Format>

[Backtesting.Commission.HK]
FixedCharge = <Fixed Transaction Fee and Tax in HKD - 15.5>
PercCharge = <Percentage Transaction Fee in % - 0.1097>

[Email]
Port = <Server SMTP Setting>
SmtpServer = <Server SMTP Setting>
Sender = <Sender Email Address - account1@example.com>
Login = <Sender Email Address - account1@example.com>
Password = <Sender Email Password>
SubscriptionList = ["account1@example.com", "account2@example.com"]

[TuShare.Credential]
token = 2134342ABC2D03780772038A7816
```

**IMPORTANT NOTE:** The format may be changed in later commits. Please refer to this README if exception is raised.

### 1. Install Dependencies

Install using [conda](https://docs.conda.io/en/latest/):

```bash
conda env create -f environment.yml
```

To export current environment, use the following command

```bash
conda env export > environment.yml
```

To update current environment with the latest dependencies, use the following command

```bash
conda env update --name futu_trade --file environment.yml --prune
```

For GitHub Actions - with pip dependencies, use the following command

```bash
pip list --format=freeze > requirements.txt
```

### 2. Install FutuOpenD

For **Windows/MacOS/CentOS/Ubuntu**:

https://www.futunn.com/download/OpenAPI

Please do make sure that you have at least a LV1 subscription level on your interested quotes. For details, please refer
to https://openapi.futunn.com/futu-api-doc/qa/quote.html

**MAKE SURE YOU LOGIN TO FUTU OPEND FIRST BEFORE STARTING FUTU_ALGO!**

### 4. Download Data (e.g. 1M Data for max. 2 Years)

For **Windows**:

    python main_backend.py --force_update

For **MacOS/Linux**:

    python3 main_backend.py --force_update

### 4. Enjoy :smile:

## Command-line Interface Usages

### Historical Data Download & Processing

Update all `K_1M` and `K_DAY` interval historical K-line data

    python main_backend.py -u   /   python main_backend.py --update

**IMPORTANT NOTE:** This will not override existing historical data if the file exists. It will automatically detect
the latest stock data you have downloaded in the folder and resume from there.

If you want to refresh all data, use the following command instead (WITH CAUTION!)

    python main_backend.py -fu   /   python main_backend.py --force_update

### Algorithmic Trading

Execute Algorithmic Trading with a Pre-defined Strategy (By default use **1M data**)

    python main_backend.py -s MACD_Cross   /   python main_backend.py --strategy MACD_Cross

If you would like to use another time interval based date (e.g., Day data), use the following command

    python main_backend.py -s MACD_Cross --time_interval K_DAY

If you do not have a pre-defined stock list in `config.ini`, then you can just trade the Top 30 HSI stocks

    python main_backend.py -s MACD_Cross --include_hsi --time_interval K_DAY

**IMPORTANT NOTE:** The supported time intervals are: K_1M, K_30M, K_5M, K_15M, K_30M, K_60M, K_DAY, K_WEEK, K_MON,
K_YEAR.

### Stock Filtering and Email Subscription

Execute Stock Filtering with Pre-defined Filtering Strategies with Email Title "MACD_Cross_Technique" in HK and
China (Shanghai and Shenzhen) Stock Market

    python main_backend.py -f Volume_Threshold Price_Threshold -en MACD_Cross_Technique -m HK CHINA

## GUI Usages

Start the GUI with `main.py` (**NOT FINISHED YET**)

    python main.py

## Future Plans

- [ ] [NEED A GREAT NAME FOR THIS ALGO TRADE!!](https://github.com/billpwchan/futu_algo/issues/23)
- [x] [Custom Backtesting Time Interval]()
- [x] [Dynamic Instantiation](https://github.com/billpwchan/futu_algo/issues/18)

-----------

## Contributor

[Bill Chan -- Main Developer](https://github.com/billpwchan/)

## Disclaimer

Futures, stocks and options trading involves substantial risk of loss and is not suitable for every investor. The
valuation of futures, stocks and options may fluctuate, and, as a result, clients may lose more than their original
investment. The impact of seasonal and geopolitical events is already factored into market prices. The highly leveraged
nature of futures trading means that small market movements will have a great impact on your trading account and this
can work against you, leading to large losses or can work for you, leading to large gains.

If the market moves against you, you may sustain a total loss greater than the amount you deposited into your account.
You are responsible for all the risks and financial resources you use and for the chosen trading system. You should not
engage in trading unless you fully understand the nature of the transactions you are entering into and the extent of
your exposure to loss. If you do not fully understand these risks you must seek independent advice from your financial
advisor.

All trading strategies are used at your own risk.

Any content in this repository should not be relied upon as advice or construed as providing recommendations of any
kind. It is your responsibility to confirm and decide which trades to make. Trade only with risk capital; that is, trade
with money that, if lost, will not adversely impact your lifestyle and your ability to meet your financial obligations.
Past results are no indication of future performance. In no event should the content of this correspondence be construed
as an express or implied promise or guarantee.

This repository and its author are not responsible for any losses incurred as a result of using any of our trading
strategies. Loss-limiting strategies such as stop loss orders may not be effective because market conditions or
technological issues may make it impossible to execute such orders. Likewise, strategies using combinations of options
and/or futures positions such as “spread” or “straddle” trades may be just as risky as simple long and short positions.
Information provided in this correspondence is intended solely for informational purposes and is obtained from sources
believed to be reliable. Information is in no way guaranteed. No guarantee of any kind is implied or possible where
projections of future conditions are attempted.

### Core Implementation Code & Architecture
#### File: `filters/__init__.py`
```python
#  Futu Algo: Algorithmic High-Frequency Trading Framework
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Written by Bill Chan <billpwchan@hotmail.com>, 2021
#  Copyright (c)  billpwchan - All Rights Reserved
```

#### File: `tests/__init__.py`
```python
#  Futu Algo: Algorithmic High-Frequency Trading Framework
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Written by Bill Chan <billpwchan@hotmail.com>, 2021
#  Copyright (c)  billpwchan - All Rights Reserved
```

#### File: `strategies/__init__.py`
```python
#  Futu Algo: Algorithmic High-Frequency Trading Framework
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# 
#  Written by Bill Chan <billpwchan@hotmail.com>, 2021
#  Copyright (c)  billpwchan - All Rights Reserved
```

#### File: `widgets/py_toggle/__init__.py`
```python
#  Futu Algo: Algorithmic High-Frequency Trading Framework
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# 
#  Written by Bill Chan <billpwchan@hotmail.com>, 2021
#  Copyright (c)  billpwchan - All Rights Reserved


from .py_toggle import PyToggle
```

#### File: `widgets/custom_grips/__init__.py`
```python
#  Futu Algo: Algorithmic High-Frequency Trading Framework
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# 
#  Written by Bill Chan <billpwchan@hotmail.com>, 2021
#  Copyright (c)  billpwchan - All Rights Reserved


from .custom_grips import CustomGrip
```

#### File: `widgets/circular_progress/__init__.py`
```python
#  Futu Algo: Algorithmic High-Frequency Trading Framework
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# 
#  Written by Bill Chan <billpwchan@hotmail.com>, 2021
#  Copyright (c)  billpwchan - All Rights Reserved


from .circular_progress import CircularProgress
```


==================================================


## [2/3] Repository: stocklook (`PHASE4-QUANT-138`)
- **Full Name**: `PHASE4-QUANT-138_zbarge__stocklook`
- **Description**: crypto currency library for trading & market making bots, account management, and data analysis
- **GitHub Stars**: 174
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
stocklook
=========

A collection of utilities for working with cryptocurrency APIs.

Goal: Painless automated spread and target trading, account management, and data analysis.

APIs:
---------
- BitMex (stocklook.crypto.bitmex): trading, account management, websocket feed
- Bittrex (stocklook.crypto.bittrex): account management, buy/sell
- blockchain.io (stocklook.crypto.bitcoin): BTC blockchain stats
- blockcypher.com (stocklook.crypto.etherium): ETH blockchain stats
- CoinBase (stocklook.crypto.coinbase_api): account management, buy/sell
- CoinMarketCap (stocklook.crypto.coinmarketcap): price history, market stats
- Cryptopia (stocklook.crypto.cryptopia): price history, buy/sell, market stats
- Gdax (stocklook.crypto.gdax):  trading, account management, price history, websocket feed
- Poloniex (stocklook.crypto.poloniex): price history
- Twitter (stocklook.apis.twitah): tweet scanning
- Yahoo Finance (broken): price history

Examples
--------

Accessing Coinbase to view accounts:

    from stocklook.crypto.coinbase_api import CoinbaseClient

    c = CoinbaseClient()

    # method 1 - access accounts via coinbase library
    obj = c.get_accounts()
    accounts = obj.response.json['data']
    for account in accounts:
        print("{}: {}".format(account['currency']: account['id'])

    # method 2 - parses accounts into dictionary upon access.
    usd_account = c.accounts['USD']


Accessing Gdax to buy some coin:

    from stocklook.crypto.gdax import Gdax, GdaxOrder

    g = Gdax()
    g.deposit_from_coinbase('USD', 100)

    o = GdaxOrder(g, 'LTC-USD', order_type='market', amount=100)
    o.post()

Market making spreads on Gdax:

    from stocklook.crypto.gdax.market_maker import GdaxMarketMaker

    m = GdaxMarketMaker(product_id='ETH-USD',
                        min_spread=0.10,
                        max_spread=0.30,
                        max_buy_orders=10,
                        max_sell_orders=30,)
    m.run()

Accessing Poloniex chart data:

    # In progress


Configuration:
--------------
Configuration variables are stored in global variable stocklook.config.config(dict). User input may be required
on Object initialization to figure out credentials unless they've been previously cached or added to this dictionary.
Passwords & secrets are always cached safely using the keyring library.

Update os.environ with the following credentials to have them auto-update config:

- coinbase: COINBASE_KEY
- poloniex: POLONIEX_KEY
- GDAX: GDAX_KEY
- GMAIL: STOCKLOOK_EMAIL

You can update global configuration like so:

    from stocklook.config import update_config, config
    my_config = {
        'DATA_DIRECTORY': 'C:/Users/me/stocklook_data'
        'COINBASE_KEY': 'mycoinbasekey',
        'COINBASE_SECRET': 'mycoinbasesecret',
        'GDAX_KEY': 'mygdaxkey',
        'GDAX_SECRET': 'mygdaxsecret',
        'GDAX_PASSPHRASE': 'mygdaxpassphrase',
        'GMAIL_EMAIL': 'mygmailemail@gmail.com',
        'GMAIL_PASSWORD': 'mygmailpassword',
        'LOG_LEVEL': logging.DEBUG,
        'PYTZ_TIMEZONE': 'US/Pacific',

        # SQLAlchemy URL kwargs
        'GDAX_FEED_URL_KWARGS': {
                                'drivername': 'mysql+pymysql',
                                'host': 'localhost',
                                'port': None,
                                'username': 'dbuser',
                                'password': 'dbpass',
                                'database': 'dbname'
                               },
    }

    # method 1
    update_config(my_config)

    # method 2 (same as method 1)
    config.update(my_config)


To-do List:
-----------

- [] Add tests for gdax, coinbase
- [] fix yahoo api
- [] add Poloniex account management code

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `stocklook/crypto/bittrex/__init__.py`
```python

```

#### File: `stocklook/crypto/bittrex/tests/__init__.py`
```python

```

#### File: `stocklook/crypto/bittrex/scripts/__init__.py`
```python

```

#### File: `stocklook/crypto/bitmex/tests/__init__.py`
```python

```

#### File: `stocklook/crypto/bitmex/utils/__init__.py`
```python

```


==================================================


## [3/3] Repository: 448Project (`PHASE4-QUANT-130`)
- **Full Name**: `PHASE4-QUANT-130_HujiaYuYoyo__448Project`
- **Description**: High Frequency Trading 
- **GitHub Stars**: 110
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# High Frequency Trading 
Build a High Frequency Price Movement Strategy
## for project outline:
See [Google Docs](https://docs.google.com/document/d/1Z4FFSi-gdo4nPoU1fX_DmOnnwUuNf2T-Uu8DBZrS5A4/edit#heading=h.oeuzasjmd8cv) for the outline of what we need to do/have done, useful papers, or links related to project.

### Core Implementation Code & Architecture
#### File: `LSTM/src/orderbook_rnn.py`
```python
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.recurrent import LSTM
import tensorflow as tf

class OrderBookRNN:
    '''
    Inputs:
        - timesteps: number of time sequence inputs
        - layer_neurons: number of neurons in each LSTM layer
        - input_shape: shape of input
        - output_shape: shape of output (e.g. num classes)
        - num_hidden_layers: number of 'vertical' hidden LSTM layers
        - dropout: dropout rate
    '''
    def __init__(self, timesteps, layer_neurons, input_shape, output_shape, num_hidden_layers, response_type, dropout = None):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.timesteps = timesteps
        self.layer_neurons = layer_neurons
        self.dropout = dropout
        self.num_hidden_layers = num_hidden_layers
        self.response_type = response_type
        self.model = self.createRNN()

    def createRNN(self):
        tf.reset_default_graph()
        if self.response_type.upper() == 'CLASSIFICATION':
            print('Building classification model...')
            model = Sequential()
            model.add(LSTM(self.layer_neurons, input_shape=self.input_shape, return_sequences=True))
            for i in range(self.num_hidden_layers):
                if i == self.num_hidden_layers-1:
                    model.add(LSTM(self.layer_neurons, return_sequences=True)) # False?
                else:
                    model.add(LSTM(self.layer_neurons, return_sequences=True))

            if self.dropout is not None:
                model.add(Dropout(self.dropout))
            model.add(Flatten())
            model.add(Dense(self.output_shape, activation='softmax'))

            print('Compiling model...')
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])

        elif self.response_type.upper() == 'REGRESSION':
            print('Building regression model...')
            model = Sequential()
            model.add(LSTM(self.layer_neurons, input_shape=self.input_shape, return_sequences=True))
            for i in range(self.num_hidden_layers):
                if i == self.num_hidden_layers-1:
                    model.add(LSTM(self.layer_neurons, return_sequences=True)) # False?
                else:
                    model.add(LSTM(self.layer_neurons, return_sequences=True))

            if self.dropout is not None:
                model.add(Dropout(self.dropout))

            model.add(Flatten())
            model.add(Dense(1))

            print('Compiling model...')
            model.compile(loss='mean_squared_error', optimizer='adam')

        return model

    def get_model(self):
        return self.model
```

#### File: `LSTM/src/orderbook_lstm.py`
```python
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.recurrent import LSTM
import tensorflow as tf

class OrderBookLSTM:
    '''
    Inputs:
        - timesteps: number of time sequence inputs
        - layer_neurons: number of neurons in each LSTM layer
        - input_shape: shape of input
        - output_shape: shape of output (e.g. num classes)
        - num_hidden_layers: number of 'vertical' hidden LSTM layers
        - dropout: dropout rate
    '''
    def __init__(self, timesteps, layer_neurons, input_shape, output_shape, num_hidden_layers, response_type, dropout = None):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.timesteps = timesteps
        self.layer_neurons = layer_neurons
        self.dropout = dropout
        self.num_hidden_layers = num_hidden_layers
        self.response_type = response_type
        self.model = self.createLSTM()

    def createLSTM(self):
        tf.reset_default_graph()
        if self.response_type.upper() == 'CLASSIFICATION':
            print('Building classification model...')
            model = Sequential()
            model.add(LSTM(self.layer_neurons, input_shape=self.input_shape, return_sequences=True))
            for i in range(self.num_hidden_layers):
                if i == self.num_hidden_layers-1:
                    model.add(LSTM(self.layer_neurons, return_sequences=True)) # False?
                else:
                    model.add(LSTM(self.layer_neurons, return_sequences=True))

            if self.dropout is not None:
                model.add(Dropout(self.dropout))
            model.add(Flatten())
            model.add(Dense(self.output_shape, activation='softmax'))

            print('Compiling model...')
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])

        elif self.response_type.upper() == 'REGRESSION':
            print('Building regression model...')
            model = Sequential()
            model.add(LSTM(self.layer_neurons, input_shape=self.input_shape, return_sequences=True))
            for i in range(self.num_hidden_layers):
                if i == self.num_hidden_layers-1:
                    model.add(LSTM(self.layer_neurons, return_sequences=True)) # False?
                else:
                    model.add(LSTM(self.layer_neurons, return_sequences=True))

            if self.dropout is not None:
                model.add(Dropout(self.dropout))

            model.add(Flatten())
            model.add(Dense(1))

            print('Compiling model...')
            model.compile(loss='mean_squared_error', optimizer='adam')

        return model

    def get_model(self):
        return self.model
```

#### File: `avellaneda-lee/thresholds.py`
```python
import numpy as np
from scipy import integrate 
from scipy import optimize

kappa = 1
rho = 0.01
c = 0.01
theta = 1
sigma = 0.5

def fplus(u,rho,epsilon,kappa, theta, sigma):
    return u**(rho/kappa-1)*np.exp(-np.sqrt(2*kappa/sigma**2)*(theta-epsilon)*u-u**2/2)

def fplus_der(u,rho,epsilon,kappa, theta, sigma):
    return np.sqrt(2*kappa/sigma**2)*u**(rho/kappa)*np.exp(-np.sqrt(2*kappa/sigma**2)*(theta-epsilon)*u-u**2/2)

def fminus(u,rho,epsilon,kappa, theta, sigma):
    return u**(rho/kappa-1)*np.exp(np.sqrt(2*kappa/sigma**2)*(theta-epsilon)*u-u**2/2)

def fminus_der(u,rho,epsilon,kappa, theta, sigma):
    return -np.sqrt(2*kappa/sigma**2)*u**(rho/kappa)*np.exp(np.sqrt(2*kappa/sigma**2)*(theta-epsilon)*u-u**2/2)

def Fplus(epsilon,rho, kappa, theta, sigma):
    integral,error = integrate.quad(fplus,0, np.inf, args = (rho,epsilon,kappa,theta,sigma,))
    return integral

def Fminus(epsilon,rho, kappa, theta, sigma):
    integral,error = integrate.quad(fminus,0, np.inf, args = (rho,epsilon,kappa,theta,sigma,))
    return integral

def Fplus_der(epsilon,rho, kappa, theta, sigma):
    integral,error = integrate.quad(fplus_der,0, np.inf, args = (rho,epsilon,kappa,theta,sigma,))
    return integral

def Fminus_der(epsilon,rho, kappa, theta, sigma):
    integral,error = integrate.quad(fminus_der,0, np.inf, args = (rho,epsilon,kappa,theta,sigma,))
    return integral

def long_close_function(epsilon,rho, kappa, theta, sigma,c):
    return (epsilon[0] - c)*Fplus_der(epsilon[0],rho, kappa, theta, sigma)-Fplus(epsilon[0],rho, kappa, theta, sigma)

def long_close(rho, kappa, theta, sigma, c): #epsilon^*+
    return optimize.root(long_close_function,[1.8], args=(rho, kappa, theta, sigma, c,), method = 'lm').x[0]

def short_close_function(epsilon,rho, kappa, theta, sigma,c):
    return (epsilon[0] + c)*Fminus_der(epsilon[0],rho, kappa, theta, sigma)-Fminus(epsilon[0],rho, kappa, theta, sigma)

def short_close(rho, kappa, theta, sigma, c): #epsilon^*-
    return optimize.root(short_close_function,[-1], args=(rho, kappa, theta, sigma, c,), method = 'lm').x[0]

def Hplus(epsilon,kappa,theta, sigma,rho,c):
    epsilonplus = long_close(rho, kappa, theta, sigma,c)
    if epsilon >= epsilonplus:
        return epsilon - c
    else:
        return (epsilonplus - c)*Fplus(epsilon,rho, kappa, theta, sigma)/Fplus(epsilonplus,rho, kappa, theta, sigma)
    
def Hplus_der(epsilon,kappa,theta, sigma,rho,c):
    epsilonplus = long_close(rho, kappa, theta, sigma,c)
    if epsilon >= epsilonplus:
        return 1
    else:
        return (epsilonplus - c)*Fplus_der(epsilon,rho, kappa, theta, sigma)/Fplus(epsilonplus,rho, kappa, theta, sigma)

def Hminus(epsilon,kappa,theta, sigma,rho, c):
    epsilonminus = short_close(rho, kappa, theta, sigma,c)
    if epsilon <= epsilonminus:
        return -epsilon - c
    else:
        return -(epsilonminus + c)*Fminus(epsilon,rho, kappa, theta, sigma)/Fminus(epsilonminus,rho, kappa, theta, sigma)
    
    
def Hminus_der(epsilon,kappa,theta, sigma,rho, c):
    epsilonminus = short_close(rho, kappa, theta, sigma,c)
    if epsilon <= epsilonminus:
        return -1
    else:
        return -(epsilonminus + c)*Fminus_der(epsilon,rho, kappa, theta, sigma)/Fminus(epsilonminus,rho, kappa, theta, sigma)

def long_short_open_function(epsilon,rho,kappa,theta,sigma, c):
    minusepsilon = epsilon[0]
    plusepsilon = epsilon[1]
    
    numA = Fminus(minusepsilon,rho, kappa, theta, sigma)*(Hplus(plusepsilon,kappa,theta,sigma,rho,c)-plusepsilon-c)-Fminus(plusepsilon,rho, kappa, theta, sigma)*(Hminus(minusepsilon,kappa,theta,sigma,rho,c)+minusepsilon-c)
    denA = Fplus(plusepsilon,rho, kappa, theta, sigma)*Fminus(minusepsilon,rho, kappa, theta, sigma)-Fplus(minusepsilon,rho, kappa, theta, sigma)*Fminus(plusepsilon,rho, kappa, theta, sigma)
    A = numA/denA

    numB = Fplus(minusepsilon,rho, kappa, theta, sigma)*(Hplus(plusepsilon,kappa,theta,sigma,rho,c)-plusepsilon-c)-Fplus(plusepsilon,rho, kappa, theta, sigma)*(Hminus(minusepsilon,kappa,theta,sigma,rho,c)+minusepsilon-c)
    denB = Fminus(plusepsilon,rho, kappa, theta, sigma)*Fplus(minusepsilon,rho, kappa, theta, sigma)-Fminus(minusepsilon,rho, kappa, theta, sigma)*Fplus(plusepsilon,rho, kappa, theta, sigma)
    B = numB/denB
    
    y_0 = A*Fplus_der(plusepsilon,rho, kappa, theta, sigma)+B*Fminus_der(plusepsilon,rho, kappa, theta, sigma)+1-Hplus_der(plusepsilon,kappa,theta, sigma,rho, c)
    y_1 = A*Fplus_der(minusepsilon,rho, kappa, theta, sigma)+B*Fminus_der(minusepsilon,rho, kappa, theta, sigma)-1-Hminus_der(minusepsilon,kappa,theta, sigma,rho, c)
    
    return [y_0,y_1]

def long_short_open(rho,kappa,theta,sigma, c):
    return optimize.root(long_short_open_function,[-0.18,1.5 ], args=(rho, kappa, theta, sigma, c,), method = 'hybr').x

def long_open(rho,kappa,theta,sigma, c):
    return short_close(rho,kappa,theta,sigma, c)

def short_open(rho,kappa,theta,sigma, c):
    return long_close(rho,kappa,theta,sigma, c)
```

#### File: `avellaneda-lee.py`
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima_model import ARMA

#Parameters
dt = 1#/252
long_open = -1.25
long_close = -0.50
short_open = 1.25;
short_close = 0.75
risk_free = 0
tran_cost = 0.0005
leverage = 1
training_size = 100

#returns1 = np.array([0.0,0.1,-0.1,0,0,0.2])
#returns2 = 2*returns1


def standardized_returns(midprices):
    log_midprices = np.log(midprices)
    logreturns = np.diff(log_midprices)
    return (logreturns-np.mean(logreturns))/np.sd(logreturns)

def regress(returns1,returns2):
    x = returns1.reshape(-1,1)
    y = returns2.reshape(-1,1)
    model = LinearRegression()
    model.fit(x,y)
    a = model.intercept_[0]
    b = model.coef_[0,0]
    residuals = y-model.predict(x)
    return residuals, a,b

def fitOU(residual):
    ou = np.cumsum(residual)
    model = ARMA(ou, order=(1, 0)) 
    fittedmodel = model.fit(disp=-1)  
    a = fittedmodel.params[0]
    b = fittedmodel.params[1]
    var =  fittedmodel.sigma2
    kappa = -np.log(b)/dt
    m = a/(1-np.exp(-kappa*dt))
    sigma = np.sqrt(var*2*kappa/(1-np.exp(-2*kappa*dt)))
    sigmaeq = np.sqrt(var/(1-np.exp(-2*kappa*dt)));
    return kappa, m, sigma, sigmaeq

def sscore(m, sigmaeq):
    if sigmaeq != 0:
        return -m/sigmaeq
    elif m>0:
        return 10000000
    else:
        return -10000000

def metrics(wealth):
    n = len(wealth)
    times = range(n)
    plt.plot(times, wealth, c='blue')
    plt.title('Evolution of the wealth')
    plt.xlabel('Seconds')
    plt.ylabel('Dollars')
    plt.show()
    
    log_wealth = np.log(wealth)
    list_logreturns = np.diff(log_wealth)
    
    plt.plot(range(n-1),list_logreturns, c='blue')
    plt.title('Evolution of the log-returns')
    plt.xlabel('Seconds')
    plt.show()
    
    plt.hist(list_logreturns, bins='auto')
    plt.title('Distribution of the log-returns')
    plt.show() 
    
    #Maybe do montecarlo and compute VaR = np.percentile(montecarlo_logreturns,5)
    
    sharpe = np.mean(list_logreturns)/np.sd(list_logreturns)
    print('The Sharpe ratio is:', sharpe)
    
    cum_return = (wealth[n-1]-wealth[0])/wealth[0]
    print('The total cumulative return is:', cum_return)
    return

def plots(scores, long_open, long_close, short_open, short_close, n, training_size):
    times = range(n-training_size+1)
    plt.plot(times, scores, c='blue')
    plt.plot(times, long_open*np.ones(n-training_size+1), c='green', label='long_open')
    plt.plot(times, long_close*np.ones(n-training_size+1), c='red', label='long_close')
    plt.plot(times, short_open*np.ones(n-training_size+1), c='olive', label='short_open')
    plt.plot(times, short_close*np.ones(n-training_size+1), c='brown', label='short_close')
    plt.title('Evolution of the s-score')
    plt.xlabel('Seconds')
    plt.ylabel('S-score')
    plt.legend()
    plt.show()
    return


def main():
    #Get data
    #get 1 second midprices, sellprice, buyprice of a (good) pair of stocks during all period
    #n= len(midprices)
    position = np.zeros((n-training_size+1,2))
    wealth = [0]   
    scores = []
    
    for t in range(n-training_size):
        #Preprocess data in the training period
        returns1 = standardized_returns(midprices1[t:training_size+t])
        returns2 = standardized_returns(midprices2[t:training_size+t])
        residuals, a,b = regress(returns1,returns2)
    
        #Calibrate model in the training period
        kappa, m, sigma, sigmaeq = fitOU(residual)
        #print("The mean reversion time is", 1/kappa)
        #print("Is the reversion time short enough?", kappa > 1/(2*dt*training_size))
        s = sscore(m,sigmaeq)
        scores += [s]
        
        #Execute trading 
        increment = 0
        if position[t,0] == 0:
            if s < -long_open:
                position[t+1,0] = leverage
                position[t+1,1] = -leverage * b
                increment = leverage*(-buyprice[training_size+t+1,0]+b*sellprice[training_size+t+1,1])
            elif s > short_open:
                position[t+1,0] = - leverage
                position[t+1,1] = leverage * b
                increment = leverage*(sellprice[training_size+t+1,0]-b*buyprice[training_size+t+1,1])
        elif position[t,0] > 0 and s > -short_close:
            position[t+1,:] = np.zeros(2)
            increment = leverage*(sellprice[training_size+t+1,0]+b*buyprice[training_size+t+1,1])
        elif position[t,0] < 0 and s < long_close:
            position[t+1,:] = np.zeros(2)
            increment = leverage*(-buyprice[training_size+t+1,0]+b*sellprice[training_size+t+1,1])
            
        #Compute change in wealth    
        wealth += [-tran_cost*abs(position[t+1,0]-position[t,0])+increment]
        
        #Metrics and plots
        metrics(wealth)
        plots(scores, long_open, long_close, short_open, short_close, n, training_size)        
    
    return

if __name__ == "__main__":
    main()
```

#### File: `LSTM/Utils/featureGenerator.py`
```python
'''
Generates features from Order Book data
Data format:
    - data_dir folder contains CSVs with order book data for a given stock
    (msft, goog, amzn, aapl) at a given depth (1-10)
    - Order book data is second-by-second
'''
import pandas as pd
import numpy as np
import os
import sys
'''
Raw Data Format:
    columns (n=1:10):
        - datetime (YYYY-MM-DD H:M:S)
        - bid{n}
        - ask{n}
        - bsize{n}
        - asize{n}
        - bnum{n}
        - anum{n}
        - vwap
        - notional
        - volume
        - last_price
        - mid
        - spread
        - wmid
        - last_size
        - last_SRO
'''

data_dir = '../../ProjectData/'


def mergeOrderBookDays(data_dir, out_path, prefixes):
    '''
    Raw data is separated into files by date (e.g. msft-20170417)
    Merge files with the same prefix (ticker) by day
    '''
    files = os.listdir(data_dir)

    for prefix in prefixes:
        data = pd.DataFrame()
        fnames = [f for f in files if (str(f).startswith(prefix) and str(f).endswith('orderbook.csv'))]
        print(fnames)
        for f in fnames:
            print(data_dir + str(f))
            data = data.append(pd.read_csv(data_dir + str(f)))
        data.to_csv(out_path, index = False)
    #return data

def createResponseVariable(data, response_type = 'Classification', look_forward = 0):
    '''
    Generates response variable for raw input data.
    Response variable will be:
        - mid price of next tick order book (response_type = 'Regression')
        - Up , Down, No Change (response_type = 'Classification')
    '''
    if response_type.upper() == 'REGRESSION':
        response_col = [data.loc[i+1, 'direct.vwap'] for i in range(len(data)-1)]

    elif response_type.upper() == 'CLASSIFICATION':
        #response_col = [data.loc[i+1, 'direct.vwap'] for i in range(len(data)-(1))]
        
        response_col = []
        for i in range(len(data)-1):
            current_price = data.loc[i, 'direct.vwap']
            next_price = data.loc[i+1, 'direct.vwap']
            diff = next_price - current_price
            if diff == 0:
                response_col.append(0)
            elif diff > 0:
                response_col.append(1)
            elif diff < 0:
                response_col.append(2)
        
    data = data[:-1] # get rid of last row, which won't have a response variable
    data['Response'] = response_col
    return data

def calculateImbalance(data):
    '''
    Calulate Order Book imbalance
    '''
    pass



def calculatePriceDiffs(data):
    '''
    (V2)

    1. P_ask_n - P_ask_1 (ask diff)
    2. P_bid_n - P_bid_1 (bid diff)
    3. abs(P_ask_i+1 - P_ask_i) {i = 1 : n}
    4.
    '''
    # 1. Ask Diff



def calculateMeanPricesAndVolumes(data):
    '''
    (V4)
    Mean Bid/Ask, Prices/Volumes
    sum(Price_i)/n
    sum(Volumes_i)/n
    '''
    #data['meanBid'] = 'NA'
    bid_col_list = ['direct.bid{}'.format(i) for i in range(1,11)]
    data['meanBid'] = data[bid_col_list].sum(axis=1)/10

    #data['meanAsk'] = 'NA'
    ask_col_list = ['direct.ask{}'.format(i) for i in range(1,11)]
    data['meanAsk'] = data[ask_col_list].sum(axis=1)/10

    #data['meanBidNum'] = 'NA'
    bidNum_col_list = ['direct.bnum{}'.format(i) for i in range(1,11)]
    data['meanBidNum'] = data[bidNum_col_list].sum(axis=1)/10

    #data['meanAskNum'] = 'NA'
    askNum_col_list = ['direct.anum{}'.format(i) for i in range(1,11)]
    data['meanAskNum'] = data[askNum_col_list].sum(axis=1)/10


    bidVol_col_list = ['direct.bsize{}'.format(i) for i in range(1,11)]
    data['meanBidVol'] = data[bidVol_col_list].sum(axis=1)/10

    askVol_col_list = ['direct.asize{}'.format(i) for i in range(1,11)]
    data['meanAskVol'] = data[askVol_col_list].sum(axis=1)/10

    #var_cols = bid_col_list + ask_col_list + bidNum_col_list + askNum_col_list +bidVol_col_list+askVol_col_list
    var_cols = ['meanBid', 'meanAsk', 'meanBidNum', 'meanAskNum', 'meanBidVol','meanAskVol']
    return data, var_cols

def calculateSpreadsAndMidPrices(data):
    '''
    (V2)
    bid-ask spreads and mid-prices

    P_ask - P_bid{i=1,...,n}
    P_ask + P_bid{i=1,...,n}
    '''
    # calculate spreads
    for i in range(1,11):
        spread = [data.loc[j, 'direct.ask{}'.format(i)] - data.loc[j, 'direct.bid{}'.format(i)] for j in range(len(data))]
        data['spread_{}'.format(i)] = spread

    # calculate mid prices
    for i in range(1,11):
        midPrice = [(data.loc[j, 'direct.ask{}'.format(i)] + data.loc[j, 'direct.bid{}'.format(i)])/2 for j in range(len(data))]
        data['midPrice_{}'.format(i)] = midPrice

    var_cols_spread = ['spread_{}'.format(i) for i in range(1,11)]
    var_cols_mp = ['midPrice_{}'.format(i) for i in range(1,11)]
    var_cols = var_cols_spread + var_cols_mp
    return data, var_cols

def calculateAccumulatedDifferences(data):
    '''
    (V5 (= V7 ?))
    sum(P_ask_i - P_bid_i)
    sum(V_ask_i - V_bid_i)
    '''
    askPrice_cols = ['direct.ask{}'.format(i) for i in range(1,11)]
    bidPrice_cols = ['direct.bid{}'.format(i) for i in range(1,11)]
    data['accumulatedPriceDiff'] = data[askPrice_cols].sum(axis=1) - data[bidPrice_cols].sum(axis=1)

    askVolume_cols = ['direct.asize{}'.format(i) for i in range(1,11)]
    bidVolume_cols = ['direct.bsize{}'.format(i) for i in range(1,11)]
    data['accumulatedVolumeDiff'] = data[askVolume_cols].sum(axis=1) - data[bidVolume_cols].sum(axis=1)

    var_cols = ['accumulatedPriceDiff', 'accumulatedVolumeDiff']
    return data, var_cols

def createFeatures(data_path, out_path, response_type, look_forward):
    '''
    Generates features from Order Book Data

    Inputs:
        - data_path: path to order book data
        - out_path: path to place generated file
    Output:
        - featureMatrix: data frame containing original data and features
    '''
    askPrice_vars = ['direct.ask{}'.format(i) for i in range(1,11)]
    bidPrice_vars = ['direct.bid{}'.format(i) for i in range(1,11)]
    askVolume_vars = ['direct.asize{}'.format(i) for i in range(1,11)]
    bidVolume_vars = ['direct.bsize{}'.format(i) for i in range(1,11)]
    orig_vars = askPrice_vars + bidPrice_vars +  askVolume_vars + bidVolume_vars

    data = pd.read_csv(data_path)
    data, meanPriceVol_vars = calculateMeanPricesAndVolumes(data) # V4
    data, spreadMidPrice_vars = calculateSpreadsAndMidPrices(data) # V2
    data, accumlatedDiff_vars = calculateAccumulatedDifferences(data) # V5
    data = createResponseVariable(data, response_type, look_forward)

    # vwap = V6
    feature_vars =  ['direct.vwap'] + orig_vars + meanPriceVol_vars + spreadMidPrice_vars + accumlatedDiff_vars + ['Response']
    feature_vars = ['direct.vwap'] + meanPriceVol_vars + accumlatedDiff_vars + spreadMidPrice_vars + ['Response']
    data = data[feature_vars]
    data.to_csv(out_path, index = False)
```

#### File: `avellaneda-lee/avellaneda-lee.py`
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima_model import AR

# Parameters
dt = 1  #training interval, in seconds
training_size = 100

long_open = -1.25 #when to buy/sell
long_close = -0.50
short_open = 1.25;
short_close = 0.75

risk_free = 0 #exogeneous parameters
tran_cost = 2


leverage = 1 #risk parameters
initial_wealth = 1000
limit_wealth = 100


def standardized_returns(midprices):
    log_midprices = np.log(midprices)
    logreturns = np.diff(log_midprices)
    if np.std(logreturns) > 0.0000001:
        return (logreturns - np.mean(logreturns)) / np.std(logreturns)
    else:
        return np.zeros((logreturns.shape))


def regress(returns1, returns2):
    x = returns1.reshape(-1, 1)
    y = returns2.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    a = model.intercept_[0]
    b = model.coef_[0, 0]
    residuals = y - model.predict(x)
    return residuals, a, b


def fitOU(residual):
    training_size = len(residual)
    ou = np.cumsum(residual)
    model = AR(ou)
    fittedmodel = model.fit(maxlag=1,disp=-1)
    a = fittedmodel.params[0]
    b = fittedmodel.params[1]
    var = fittedmodel.sigma2 #b should be in (0,1) so the mean reversion time (1/kappa) is >0
    #The reversion time is short enough if kappa > 2/(dt*training_size), i.e, at least half the training-period
    #This means  0 < b < np.exp(-2/training_size)

    if b > 0 and b < np.exp(-2/training_size):
        kappa = -np.log(b) / dt    
        m = a / (1 - np.exp(-kappa * dt))
        sigma = np.sqrt(var * 2 * kappa / (1 - np.exp(-2 * kappa * dt)))
        sigmaeq = np.sqrt(var / (1 - np.exp(-2 * kappa * dt)));
        return kappa, m, sigma, sigmaeq

    else:
        return -1,0,0,0


def sscore(m, sigmaeq):
    if sigmaeq != 0:
        return -m / sigmaeq
    elif m > 0:
        return 10000000
    else:
        return -10000000


def metrics(wealth):
    n = len(wealth)
    times = range(n)
    plt.plot(times, wealth, c='blue')
    plt.title('Evolution of wealth')
    plt.xlabel('Seconds')
    plt.ylabel('Dollars')
    plt.show()

    log_wealth = np.log(wealth)
    list_logreturns = np.diff(log_wealth, axis=0)

    plt.plot(range(n - 1), list_logreturns, c='blue')
    plt.title('Evolution of the log-returns')
    plt.xlabel('Seconds')
    plt.show()

    plt.hist(list_logreturns, bins='auto')
    plt.title('Distribution of the log-returns')
    plt.show()

    # Maybe do montecarlo and compute VaR = np.percentile(montecarlo_logreturns,5)

    sharpe = np.mean(list_logreturns) / np.std(list_logreturns)*np.sqrt(6*60*60) #6 hours of trading second-by-second
    print('The (daily) Sharpe ratio is:', sharpe)

    cum_return = (wealth[n - 1] - wealth[0]) / wealth[0]
    print('The total cumulative return is:', cum_return)
    return


def plots(scores, long_open, long_close, short_open, short_close):
    n = len(scores)
    times = range(n)
    plt.plot(times, scores, c='blue')
    plt.plot(times, np.full(n,long_open), c='green', label='long_open')
    plt.plot(times, np.full(n,long_close), c='red', label='long_close')
    plt.plot(times, np.full(n,short_open), c='olive', label='short_open')
    plt.plot(times, np.full(n,short_close), c='brown', label='short_close')
    plt.title('Evolution of the s-score')
    plt.xlabel('Seconds')
    plt.ylabel('S-score')
    plt.legend()
    plt.show()
    return


def tickers_to_dict(tickers):
    '''Function that take in a list of tickers and returns a dictionare with the prices (bid, ask, midprices), returns
    and normalized returns of that ticker.
    Assumes that there is a csv in the same folder named "ticker"-1.csv'''
    stocks = {}
    for ticker in tickers:
        stocks[ticker] = pd.read_csv('{}-1.csv'.format(ticker), parse_dates=True, index_col=0)
        stocks[ticker]['midprice'] = midprice(stocks[ticker]['direct.bid1'], stocks[ticker]['direct.ask1'])
    return stocks


def midprice(bid, ask):
    """ function to calculate midprice using the best bid and ask prices and no volume weighting """
    midprice = np.add(bid, ask) / 2.0
    return midprice


def execute(tickers):
    # get data of the pair of tickers during all period 

    stocks = tickers_to_dict(tickers)

    midprices1 = stocks[tickers[0]]['midprice']
    midprices2 = stocks[tickers[1]]['midprice']
    sellprice = np.column_stack((stocks[tickers[0]]['direct.bid1'], stocks[tickers[1]]['direct.bid1']))  # sell prices
    buyprice = np.column_stack((stocks[tickers[0]]['direct.ask1'], stocks[tickers[1]]['direct.ask1']))  # buy prices

    #initialize vectors storing the evolution of the strategy
    n = len(midprices1)
    position = np.zeros((n - training_size + 1, 2))
    wealth = np.full((n - training_size + 1, 1), initial_wealth)
    scores = [0]

    for t in range(n - training_size):
        if wealth[t] > limit_wealth:
            # Preprocess data in the training period
            returns1 = standardized_returns(midprices1[t:t + training_size])
            returns2 = standardized_returns(midprices2[t:t + training_size])

            residuals, a, b = regress(returns1, returns2)

            # Calibrate model in the training period
            kappa, m, sigma, sigmaeq = fitOU(residuals)
            increment = 0
            
        
            if kappa > 0: #sufficiently fast and non-degenerate mean-reversion, checked in the fitOU function
                s = sscore(m, sigmaeq)

                # Execute trading
                if position[t, 0] == 0:
                    if s < -long_open:
                        position[t + 1, 0] = leverage
                        position[t + 1, 1] = -leverage * np.ceil(b) #we round b to order an integer amount of stocks
                        increment = leverage * (-buyprice[training_size + t, 0] + np.ceil(b) * sellprice[training_size + t, 1])
                    elif s > short_open:
                        position[t + 1, 0] = - leverage
                        position[t + 1, 1] = leverage * np.ceil(b)
                        increment = leverage * (sellprice[training_size + t, 0] - np.ceil(b) * buyprice[training_size + t, 1])
                elif position[t, 0] > 0 and s > -short_close:
                    position[t + 1, :] = np.zeros(2)
                    increment = leverage * (-buyprice[training_size + t, 0] + np.ceil(b) * sellprice[training_size + t, 1])
                elif position[t, 0] < 0 and s < long_close:
                    position[t + 1, :] = np.zeros(2)
                    increment = leverage * (sellprice[training_size + t, 0] - np.ceil(b) * buyprice[training_size + t, 1])
                else:
                    position[t + 1, :] = position[t, :]  

            else:
                position[t + 1, :] = position[t, :]
                s = scores[t]

        else:
            position[t + 1, :] = position[t, :]
            s = scores[t]
            increment = 0

        # Compute change in wealth and score
        scores += [s]
        wealth[t+1] = wealth[t] - tran_cost * abs(position[t + 1, 0] - position[t, 0]) + increment

    print(wealth)
    print(position)

    # Metrics and plots
    metrics(wealth)
    plots(scores, long_open, long_close, short_open, short_close)

    return


tickers = ['csco', 'aapl']  # define the pair here
execute(tickers)

#if __name__ == "__main__":
#    main()
```


==================================================
