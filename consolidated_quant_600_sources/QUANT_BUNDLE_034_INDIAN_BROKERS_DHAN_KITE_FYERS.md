# ⚡ [QUANT-SOURCE-034] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_034_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: KiteConnect.jl (`PHASE4-QUANT-071`)
- **Full Name**: `PHASE4-QUANT-071_arcofdescent__KiteConnect.jl`
- **Description**: Julia package for interfacing with Zerodha's KiteConnect API
- **GitHub Stars**: 6
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# KiteConnect.jl

A Julia module to interface with Zerodha's KiteConnect API

## Installation

Using Julia's package manager

```
pkg> add KiteConnect
```

## API keys

Create a `.env` file to store your API key and secret. Look at `.env.sample` for an example.

## Get LTP of an instrument

```julia
using KiteConnect

access_token = KiteConnect.gen_access_token(request_token)
KiteConnect.ltp("NSE:INFY", access_token)
```

### Core Implementation Code & Architecture
#### File: `Project.toml`
```python
name = "KiteConnect"
uuid = "09e18e8d-40f5-4176-baf5-9239a33e36dd"
authors = ["Rohan Almeida <rohan.almeida@gmail.com>"]
version = "0.5.0"

[deps]
CSV = "336ed68f-0bac-5ca0-87d4-7b16caf5d00b"
DataFrames = "a93c6f00-e57d-5684-b7b6-d8193f3e46c0"
Dates = "ade2ca70-3891-5945-98fb-dc099432e06a"
HTTP = "cd3eb016-35fb-5094-929b-558a96fad6f3"
JSON3 = "0f8b85d8-7281-11e9-16c2-39a750bddbf1"
Parsers = "69de0a69-1ddd-5017-9359-2bf0b02dc9f0"
SHA = "ea8e919c-243c-51af-8825-aaa63cd721ce"
StructTypes = "856f2bd8-1eba-4b0a-8007-ebc267875bd4"

[compat]
HTTP = "~0.9"
julia = "1.0"

[extras]
Test = "8dfed614-e22c-5e08-85e1-65c5234f0b40"

[targets]
test = ["Test"]
```


==================================================


## [2/3] Repository: AlgoTrade-API (`PHASE4-QUANT-072`)
- **Full Name**: `PHASE4-QUANT-072_vinay-ram1999__AlgoTrade-API`
- **Description**: Fully automated NSE Stock/Equity trading-bot for Kotak Securities API with integrated back testing and ML algorithms.
- **GitHub Stars**: 24
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AlgoTrade-API
Fully automated NSE Stock/Equity trading Bot integrated with Kotak Securities Broker API.

## Under Development

### Core Implementation Code & Architecture
#### File: `python/backtesting_bt.py`
```python
import pandas as pd
import yfinance as yf
import backtrader as bt
import matplotlib.pyplot as plt


#WARNING backtrader is not available for python version 3.10.4 so we should continue with vectorbt using the available code.
```

#### File: `python/test.py`
```python
import pandas as pd
import yfinance as yf
from LSTM import LSTM_DL
import matplotlib.pyplot as plt


ticker = yf.Ticker("MRF.NS")
data = ticker.history(start = "2022-04-01", end = "2022-05-25", interval = "5m")
#print(data)


lstm = LSTM_DL("MRF", data, time_step = 75, epochs=100)
model = lstm.RNN
a = lstm.Prediction(model, 75)


daterange = pd.date_range(start ='2022-05-25 09:15', freq ='5min', periods = 75, tz ='Asia/Calcutta')
new = pd.DataFrame({"Pred_Close" : a}, index = pd.DatetimeIndex(daterange))



print(data)
print(new)

plt.plot(data["Close"], label="closing")
plt.plot(new["Pred_Close"], label="nextday_prediction")
plt.legend()
plt.show()
```

#### File: `python/vbt_test.py`
```python
import vectorbt as vbt
import numpy as np

btc_price_1d = vbt.YFData.download("BTC-USD", missing_index='drop', interval="1D").get('Close')


class MA():
    def __init__(self):
        return

    def ma_strategy(self,close, window = 730, lower_multiplier=1, upper_multiplier=4):
        signal = np.full(close.shape, np.nan)
        for x in range(len(close)):
            if x >= window:
                mavg = np.mean( close[x-window:x])
                if close[x] < mavg*lower_multiplier:
                    signal[x] = 1
                elif close[x] > mavg*upper_multiplier:
                    signal[x] = -1
                else:
                    signal[x] = 0

        return signal

ma = MA()

my_indicator = vbt.IndicatorFactory(
         class_name="ma_strategy",
         short_name="ma",
         input_names=["close"],
         param_names=["window","lower_multiplier","upper_multiplier"],
         output_names=["signal"]
         ).from_apply_func(
             ma.ma_strategy,
             window=730,
             lower_multiplier=1,
             upper_multiplier=4
         )

results = my_indicator.run(btc_price_1d)
print(results.signal)
```

#### File: `python/program.py`
```python
import time
import pandas as pd
from ks_API import KSTrade_API
import matplotlib.pyplot as plt
from datetime import datetime as dt
#from backtesting import BackTestingEngine
from trading_strategy import TradingStrategy
from nsepy.symbols import get_index_constituents_list


def Main(broker_API, tickers):
    strategy = {}
    OHLCV_NSE = {}
    Analysis_NSE = TradingStrategy()
    Analysis_NSE.Exchange = "NSE"
    Analysis_NSE.Dataset = "Close"
    for ticker in tickers:
        df = Analysis_NSE.HistoricData(ticker, interval = "5m")
        OHLCV_NSE[ticker] = df[["Open", "High", "Low", "Close", "Volume"]].copy()
    for ticker in OHLCV_NSE:
        strategy[ticker] = Analysis_NSE.MA_Crossover(OHLCV_NSE[ticker], MA_type = "HMA")
    broker_API.TickersData = strategy
    orders = broker_API.Run()
    return



if __name__ == "__main__":
    Nifty50 = get_index_constituents_list(index = "Nifty50")["Symbol"].to_list()
    Nifty100 = get_index_constituents_list(index = "Nifty100")["Symbol"].to_list()
    Broker_API = KSTrade_API()
    start = time.time()
    timeout = time.time() + 60*11
    print("waiting...!")
    print(Nifty50)
    while time.time() <= timeout:
        try:
            if (dt.now().second == 0) and (dt.now().minute % 5 == 0):
                print(dt.now())
                st_time = time.time()
                Trade = Main(Broker_API, Nifty50)
                ed_time = time.time()
                time.sleep((60*5) - (ed_time - st_time + 2))
                print(dt.now())
        except Exception as ex:
            print(ex)
            break

    Broker_API.Client.logout()
```

#### File: `python/nse_py.py`
```python
import pandas as pd
from nsepy import get_history
from nsepy.symbols import get_symbol_list
from nsepy.symbols import get_index_constituents_list
from datetime import date


sbin = get_history(symbol='SBIN', start=date(2015,1,1), end=date(2015,1,10))
print(sbin)


NSE_INDICES = ["NIFTY 50","NIFTY NEXT 50","NIFTY100 LIQ 15","NIFTY 100","NIFTY 200","NIFTY 500","NIFTY MIDCAP 50","NIFTY MIDCAP 100","NIFTY SMALL 100","NIFTY AUTO","NIFTY BANK","NIFTY ENERGY","NIFTY FIN SERVICE","NIFTY FMCG","NIFTY IT","NIFTY MEDIA","NIFTY METAL","NIFTY PHARMA","NIFTY PSU BANK","NIFTY REALTY","NIFTY COMMODITIES","NIFTY CONSUMPTION","NIFTY CPSE","NIFTY INFRA","NIFTY MNC","NIFTY PSE","NIFTY SERV SECTOR","NIFTY SHARIAH 25","NIFTY50 SHARIAH","NIFTY500 SHARIAH","NIFTY100 EQUAL WEIGHT","NIFTY50 USD","NIFTY50 DIV POINT","NIFTY DIV OPPS 50","NIFTY ALPHA 50","NIFTY HIGH BETA 50","NIFTY LOW VOLATILITY 50","NIFTY QUALITY 30","NIFTY50 VALUE 20","NIFTY GROWSECT 15","NIFTY50 TR 2X LEV","NIFTY50 TR 1X INV"]


symbol_list = get_symbol_list()
#print(symbol_list)

nifty50 = get_index_constituents_list(index="NIFTY50")["Symbol"].to_list()
nifty100 = get_index_constituents_list(index="NIFTY100")["Symbol"].to_list()
nifty500 = get_index_constituents_list(index="NIFTY500")["Symbol"].to_list()


path = "~/Downloads/"

n_50 = pd.read_csv(path + "NIFTY-50.csv")
#n_50.drop(n_50.index[0], axis = 0, inplace=True)
syms_50_nse = n_50["SYMBOL \n"].to_list()

n_100 = pd.read_csv(path + "NIFTY-100.csv")
#n_100.drop(n_100.index[0], axis = 0, inplace=True)
syms_100_nse = n_100["SYMBOL \n"].to_list()


n_500 = pd.read_csv(path + "NIFTY-500.csv")
#n_500.drop(n_500.index[0], axis = 0, inplace=True)
syms_500_nse = n_500["SYMBOL \n"].to_list()





for sym in syms_50_nse:
    if sym in nifty50:
        pass
    else:
        print(sym, "is not there in NSEpy")


for sym in syms_100_nse:
    if sym in nifty100:
        pass
    else:
        print(sym, "is not there in NSEpy")


for sym in syms_500_nse:
    if sym in nifty500:
        pass
    else:
        print(sym, "is not there in NSEpy")
```

#### File: `python/trading_platform.py`
```python
import numpy as np
import pandas as pd
from collections import deque
from technical_analysis import TechnicalAnalysis


class TradingPlatform(object):
    def __init__(self):
        self.Data = None
        self.Tickers = list()
        self.long_dataset = "long"
        self.short_dataset = "short"
        self.TickerPosition = dict()
        self.x = deque(maxlen = 10) #
        self.position = None
        self.order_pending = None
        return


    @property
    def TickersData(self):
        if self.Data:
            return self.Data
        else:
            raise ValueError("Set the TickersData")


    @TickersData.setter
    def TickersData(self, data):
        self.Data = data


    @property
    def Get_Tickers(self):
        data = self.TickersData
        for ticker in data:
            self.Tickers += [ticker]
        return self.Tickers


    def SignalParser(self, Data):
        self.is_long = None
        self.is_short = None
        self.signal_parsed = None
        try:
            if Data[self.long_dataset][-1] == 1.0:
                self.is_long = True
                delattr(self, "is_short")
            elif Data[self.short_dataset][-1] == 1.0:
                self.is_short = True
                delattr(self, "is_long")
            else:
                delattr(self, "is_long")
                delattr(self, "is_short")
            self.signal_parsed = True
        except Exception as ex:
            print("SignalParser error:", type(ex).__name__, ex)
            print("Please provide the Strategy implemented Data")
            pass
        return self.signal_parsed


    def PositionType(self, Data):
        signal = self.SignalParser(Data)
        if signal:
            if hasattr(self, "is_long") and self.is_long:
                self.position = "BUY"
            elif hasattr(self, "is_short") and self.is_short:
                self.position = "SELL"
            else:
                self.position = None
        else:
            print("Signal is not parsed. Check SignalParser")
        return self.position


    @property
    def Get_TickerPosition(self):
        data = self.TickersData
        for ticker in data:
            position = self.PositionType(data[ticker])
            price = data[ticker]["Close"][-1]
            self.TickerPosition[ticker] = [position, price]
        return self.TickerPosition
```


==================================================


## [3/3] Repository: TradingView-Extension (`PHASE4-QUANT-074`)
- **Full Name**: `PHASE4-QUANT-074_boudhayan-dev__TradingView-Extension`
- **Description**: A chrome extension that extends tradingview charts by facilitating order creation in Zerodha Kite.
- **GitHub Stars**: 4
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# TradingView-Extension
A chrome extension that extends tradingview charts by facilitating order creation in Zerodha Kite.


## Capabilities
Currently, the extension takes in your intraday budget (mandatory) and profit target (option) as the input parameters. Based on the input, it calculates the stocks that can be alloted (long)/sold off (short). It takes a single button click to place the order in Zerodha Kite platform.

Supports Nifty 200 stocks only.

## Installation
1. Clone project
2. Create a API key from Kite Developer platform.
3. Replace `API_KEY` value in `index.html`.
4. Open `chrome:\\extensions` and enable developer mode.
5. Upload the extension using `Load unpacked`.
6. Go to tradingview charts, select a nifty 200 stock and click on thee extension.

## Screenshots

Trading view -

![Screenshot1](./screenshot1.png)

Order view -

![Screenshot2](./screenshot2.png)

### Core Implementation Code & Architecture
#### File: `mappings.json`
```python
{
    "M_MFIN":"M&MFIN",
    "MCDOWELL_N":"MCDOWELL-N",
    "NAME_INDIA":"NAM-INDIA",
    "M_M":"M&M",
    "BAJAJ_AUTO":"BAJAJ-AUTO",
    "L_TFH":"L&TFH"
}
```

#### File: `manifest.json`
```python
{
    "name": "Nifty 200 Intraday Marketwatch",
    "description": "Nifty 200 Intraday Marketwatch",
    "permissions": [
        "storage",
        "activeTab",
        "scripting",
        "tabs"
    ],
    "version": "1.0",
    "manifest_version": 3,
    "action": {
        "default_popup": "index.html"
    },
    "default_icon": {
        "16": "/tradingview-logo-3.png",
        "32": "/tradingview-logo-3.png",
        "48": "/tradingview-logo-3.png",
        "128": "/tradingview-logo-3.png"
    },
    "icons": {
        "16": "/tradingview-logo-3.png",
        "32": "/tradingview-logo-3.png",
        "48": "/tradingview-logo-3.png",
        "128": "/tradingview-logo-3.png"
    }
}
```


==================================================
