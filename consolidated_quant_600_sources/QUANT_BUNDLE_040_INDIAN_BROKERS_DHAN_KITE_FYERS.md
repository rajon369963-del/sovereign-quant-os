# ⚡ [QUANT-SOURCE-040] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_040_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Stock_Market_Live_Trading_using_AI (`PHASE4-QUANT-146`)
- **Full Name**: `PHASE4-QUANT-146_ashishkumar30__Stock_Market_Live_Trading_using_AI`
- **Description**: The apex of my CSE tenure at UIET Kurukshetra University in 2018, This project focuses on Zerodha, involving live online trading in the NSE-BSE with real money, utilizing Artificial Intelligence techniques. The project employs Python programming, incorporating live trading bots, indicator screeners, and back testers through REST API and websockets.
- **GitHub Stars**: 222
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Zerodha Trading Strategies and Backtesting

## About the Project
This repository is a collection of Python-based trading strategies and backtesting programs, developed as part of my Computer Science Engineering (CSE) tenure at UIET Kurukshetra University in 2018. The project focuses on automated and manual live trading on the NSE-BSE markets using Zerodha's API. It incorporates Artificial Intelligence techniques to execute trades based on various technical indicators.

The repository consists of:
- **Live trading bots**
- **Backtesting programs**
- **Stock screeners**
- **Technical indicator implementations**
- **Historical data downloaders**

## Features
- **Live Trading Bots:** Automated and manual trading bots utilizing technical strategies.
- **Backtesting Programs:** Test trading strategies on historical data.
- **Stock Screener:** Scans stocks based on Guppy and other technical indicators.
- **Technical Indicators:** Implementation of popular stock market indicators.
- **Data Conversion:** Converts candlestick data to Heikin-Ashi format.
- **Time Frame Adjustments:** Custom time frame modifications for analysis.

## Files and Notebooks

| File Name | Description |
|-----------|-------------|
| **1)_Getting_Started_with_Zerodha_.ipynb** | Introduction and setup guide for Zerodha API |
| **BACKTESTIG_PROGRAM_.ipynb** | Backtesting any stock's buy/sell strategy on historical data |
| **Buy on RSI when the current high of candle is more than previous high of candle.ipynb** | Buy order based on RSI when RSI > 50 |
| **Hisorical_Data_Download_of_stocks.ipynb** | Code to download historical data for any stock |
| **Live_BOT_(1)_on_RSI_.ipynb** | Live trading bot based on RSI strategy |
| **Live_BOT_(2)_on_GUPPY_with_screener.ipynb** | Manual input Guppy strategy bot |
| **Live_BOT_(3)_Guppy_Automated_.ipynb** | Fully automated Guppy strategy bot |
| **Live_BOT_(4)_advance_bot_multiple_bot_working_in_single_bot_.ipynb** | Mini Guppy bot with backtesting, screener, and indicators |
| **Live_BOT_(5).ipynb** | Mini Guppy bot with stock tracking features |
| **Stock_Screener_(GUPPY)_.ipynb** | Stock screener scanning multiple stocks based on Guppy strategy |
| **Technical_Indicator's_of_Indian_Stock_market.ipynb** | Implementation of key technical indicators for Indian stock market |
| **change time frame.ipynb** | Adjusts time frames for Zerodha trading |
| **conversion code of Candles to hikenashi.ipynb** | Converts candlestick data into Heikin-Ashi format |
| **order_information.jpg** | Image related to order placement |

## Technologies Used
- **Python**
- **Zerodha API (Kite Connect)**
- **Pandas & NumPy**
- **Matplotlib & Seaborn**
- **TA-Lib (Technical Analysis Library)**
- **REST API & Websockets**

## Setup Instructions
1. Install required dependencies:
   ```sh
   pip install kiteconnect pandas numpy matplotlib seaborn TA-Lib
   ```
2. Get API credentials from Zerodha and configure them.
3. Run the desired Jupyter Notebook.

## License
This project is for educational and research purposes only. Live trading involves financial risks, and users should trade responsibly.

## Author
Developed as part of my academic and professional exploration into AI-driven stock trading strategies.

Feel free to explore and contribute! 🚀


==================================================


## [2/3] Repository: ZerodhaAtom (`PHASE4-QUANT-148`)
- **Full Name**: `PHASE4-QUANT-148_harpalnain__ZerodhaAtom`
- **Description**: Zerodha Browser Atomation for Algo trading without subscribing Kite API
- **GitHub Stars**: 112
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Web Automation Based api Algo Trading for Broker Zerodha

This is python based library created for simple algo trading, It is developed using selenium. It helps for automatic data collection from [Zerotha Official Website](.https://kite.zerodha.com/)

These API can be user to place order in live market.

These api can be used to collect the data from website and save them in xml file and used for backtest.

* __Author: [Harpal](https://github.com/harpalnain)__
* These are unoffical api just created for fun.

### Prerequisites

Python 3.x

Also, you need the following modules:

* `selenium`
* `chromedriver`
* `websocket_client`
* `requests`
* `bs4`

You can clone this repo and install all preraquisites

## Getting started with API

### Overview
There are three public class `Zerodha`, `StockDataLogger` and `MarketSimulatore`. You can create instance of these class. For creating instance of `Zerodha` you need to pass Zeroda's credential as argument in constructor. `StockDataLogger` is used to save live data in xml files and `MarkerSimulator` class is used to backtest your stratergy using data saved in xml files.


### Getting Started

1. Create a dictonary contaning the credential and watch list no. that you want to subscibe for trading.
```python
creds = {	
          "trading":True,  
          "usr":"AB2111",
          "pswd":"Password@123",
          "pin":"124346",
          "trade_watchlist":1,
          "email":"lazypeople@gmail.com"
        }

```

2. Login and Subscibe: Create instance of Zerodha using credential.
ZC Call is used to define the Constant Value
* ZC.MODE_DEPTH_20 :- market depth 20 data
* ZC.MODE_DEPTH_5 :- market depth 5 data
* ZC.MODE_LTP :- Last Trading Price data
```python
from Brokers.Zerodha import ZC, ZerodhaConnect
z = ZerodhaConnect(usr=creds, headless = False)
#headless false means browser will open in backround
z.subscribe(time_interval = 1,mode = ZC.MODE_DEPTH_5)
```

3. Define a method where you implement your trading stratergy and register this methon with zerodha instance
```python
def on_ticks(ticks):
    print(ticks)
    #Add Stratergy Here 
z.on_ticks=on_ticks
```
 #### This tick data contains list of ticks in following example format.

```python    
    [{'timestamp': datetime.datetime(2021, 2, 14, 12, 26, 35), 'symbol': 'TCS', 'exchange': 'NSE', 'holdings': None, 'ltp': 3190.8, 'change': None, 'Prev. Close': '3206.00', 'Volume': 'NA', 'Avg. price': 'NA', 'LTQ': 'NA', 'LTT': '2021-02-12 15:58:42', 'Lower circuit': '2871.75', 'Upper circuit': '3509.85', 'total_bids': '0', 'total_offers': '0'}]
      
``` 
4. Place Order:-
```python
place_order(self,symbol = "IRCTC",
            exchange= 'NSE', 
            product = ZC.PRODUCT_TYPE_CNC,
            transaction_type =ZC.TRANSACTION_TYPE_BUY,
            order_type = ZC.ORDER_TYPE_MARKET,
            price = None, 
            qtn = 1 ):
```
### Following Constant are define in ZC Class for placing order
**_transaction_type_**  
* ZC.TRANSACTION_TYPE_BUY :- Buy Order
* ZC.TRANSACTION_TYPE_SELL :- Sell Order

**_product_**
* ZC.PRODUCT_TYPE_CNC :- "Cash and carry. Delivery based trades"
* ZC.PRODUCT_TYPE_MIS = "Intraday squareoff with extra leverage"

**_order_type_**

* ZC.ORDER_TYPE_MARKET = "Market Order"
* ZC.ORDER_TYPE_LIMIT = "Limit Order"


Price is kept none in case of market order and have some value in case of limit order.

5. Get Margins

```python
z.get_margin()

# This method return following example output format
{'equity': {'Available margin': 1465.21,
  'Used margin': 0.0,
  'Available cash': 1465.21,
  'Opening balance': 1465.21,
  'Payin': 0.0,
  'SPAN': 0.0,
  'Delivery margin': 0.0,
  'Exposure': 0.0,
  'Options premium': 0.0,
  'Collateral (Liquid funds)': 0.0,
  'Collateral (Equity)': 0.0,
  'Total collateral': 0.0},
 'commodity': {'Available margin': 0.01,
  'Used margin': 0.0,
  'Available cash': 0.01,
  'Opening balance': 0.01,
  'Payin': 0.0,
  'SPAN': 0.0,
  'Delivery margin': 0.0,
  'Exposure': 0.0,
  'Options premium': 0.0}}
```
6. Get Holdings 
```python
z.get_holdings()
#Return Folloing example output format
{'AVANTIFEED': {'Instrument': 'AVANTIFEED',
  'Qty.': '25',
  'Avg. cost': '483.34',
  'LTP': '499.15',
  'Cur. val': '12,478.75',
  'P&L': '395.20',
  'Net chg.': '+3.27%',
  'Day chg.': '-1.30%'},
 'BPCL EVENT': {'Instrument': 'BPCL EVENT',
  'Qty.': '15',
  'Avg. cost': '378.43',
  'LTP': '418.35',
  'Cur. val': '6,275.25',
  'P&L': '598.75',
  'Net chg.': '+10.55%',
  'Day chg.': '0.00%'}}
```
7. Save Data in xml file
```python
from Loggers.StockDataLogger import StockLogger
HsLogger = StockLogger(base_path ="path_for_data_to_be_saved",chunk_size = 100)
z.set_logger(hslogger=HsLogger)
```

8 Market Simulator:
Data Should be avalble for simulator that is saved by HsSimlator.
```python
from Brokers.MarketSimulator import TickSimulator
stocks =['SBICARD','TITAN','AARTIIND','IDEA', 'IRCTC','LT','SETFGOLD','PRINCEPIPE']
tick_sim = TickSimulator(time_interval = 1, usr = 'PAPER_TRADING')
tick_sim.subscribe(tickers = stocks, last_n_days = 60)
def on_ticks(ticks):
    print(ticks)
    #Add Stratergy Here 

tick_sim.on_ticks=on_ticks
```
Marker Simlator class will exactly behave real market only difference is that no real money and no real order will be place.This class not required broker accound but required data to be availble in xml format

### Core Implementation Code & Architecture
#### File: `Brokers/__init__.py`
```python
#
```

#### File: `Loggers/__init__.py`
```python
#
```

#### File: `Backtester.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:43:15 2020

@author: harpal
"""

from whatappAtom import WhatsApp
from MarketSimulator import TickSimulator
from signal import signal, SIGINT
from sys import exit
import threading
import time
import json
import datetime as dt
import pandas as pd
import numpy as np
from Strategies import StocksNStratergy

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objs as go

def handler(signal_received, frame):
    # Handle any cleanup here
    tick_sim.stop()
   
#signal(SIGINT, handler)

timeStamp =dt.datetime.now().replace(microsecond=0)
stocks =['TITAN','BAJAJFINSV']
#stocks =['SBICARD','TITAN','AARTIIND','IDEA', 'IRCTC','LT','SETFGOLD','PRINCEPIPE']
tick_sim = TickSimulator(time_interval = 0.01, usr = 'SIMU1')
tick_sim.subscribe(tickers = stocks, last_n_days = 60)
stg = StocksNStratergy(broker = tick_sim)
tick_sim.init_trade_setup(stg)

print('start',today)
#tick_sim.on_ticks = on_ticks    
tick_sim.start()
tick_sim.join()
today = dt.datetime.today()
print('stop',today)
'''
tick_sim.start()


tick_sim.stop()

#tick_sim.join()




'''
today = dt.datetime.today()
market_start_time = dt.datetime.combine(today, dt.time(9, 15, 0))
market_stop_time = dt.datetime.combine(today, dt.time(15, 29, 59))

print('start',today)
#tick_sim.on_ticks = on_ticks    
#tick_sim.start()
tick_sim.join()
today = dt.datetime.today()
print('stop',today)
'''
```

#### File: `ZerodhaAutomationExample.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:15:45 2020
@author: harpal
@email : hpl.nain@gmail.com
"""
from Brokers.Zerodha import ZC, ZerodhaConnect
from Loggers.StockDataLogger import StockLogger
from signal import signal, SIGINT
from sys import exit
import threading

import time
import json
import datetime as dt

import sys
if len(sys.argv) > 1:
    now = dt.datetime.now() 
    if now < ZerodhaConnect.start_time or now > ZerodhaConnect.close_time:
        print('This time Market ramain closed')
        exit(1)
        
def handler(signal_received, frame):
    print('Signler Handler is called')
    z.stop()

signal(SIGINT, handler)

'''
Put the credential in following format in credential_file
{"usr":"AB1234", "pswd":"abcdef@1234',"pin":"123456","trade_watchlist":1}
'''

#Get the crederntial from following Json File change the path if required
credential_file = '/home/harpal/Desktop/creds.json'
with open(credential_file, 'rb') as input:
    usr_creds= json.load(input)
today = dt.datetime.today()

hs_logger = StockLogger(chunk_size = 100)

z = ZerodhaConnect(usr=usr_creds, headless = True)  
z.subscribe(time_interval = 1,mode = ZC.MODE_DEPTH_5)    
z.set_logger(hslogger=hs_logger)

def on_ticks(ticks):
    #print(ticks)
    #Add Stratergy Here
    print(z.get_margins())
    print(z.get_holdings())
       
z.on_ticks=on_ticks


hs_logger.start()
z.start()
z.join()
hs_logger.stop()
now = dt.datetime.now() 

if now > ZerodhaConnect.start_time and now < ZerodhaConnect.close_time:
    print('Market is still open')
else:
    print('Thanks For Trade')
```

#### File: `Loggers/StockDataLogger.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 23:49:28 2020

@author: harpal
"""

import os
import threading
import datetime
import queue
import time
import pandas as pd
class TickLogger():
    def __init__(self, csv_file_name, tick):
        #No Need to save following
        del tick['symbol']
        del tick['exchange']
        if 'bid_table' in tick:
            tick['bid_table'] = str(tick['bid_table'].to_dict())
        if 'offer_table' in tick:
            tick['offer_table'] = str(tick['offer_table'].to_dict())
        self.csv_file_name = csv_file_name
        self.pd = pd.DataFrame()
        self.pd = self.pd.append(tick, ignore_index=True)
        #If Log file not created then only create log file
        if not os.path.exists(csv_file_name):
            self.pd.to_csv(self.csv_file_name, index = False) 
            self.pd = self.pd[0:0]
        
    def append(self,tick):
        del tick['symbol']
        del tick['exchange']
        if 'bid_table' in tick:
            tick['bid_table'] = str(tick['bid_table'].to_dict())
        if 'offer_table' in tick:
            tick['offer_table'] = str(tick['offer_table'].to_dict())
        self.pd = self.pd.append(tick, ignore_index=True)
        
    def save(self):
        self.pd.to_csv(self.csv_file_name, mode='a', header=False, index = False) 
        self.pd = self.pd[0:0]
        

class StockLogger(threading.Thread):
    def __init__(self, base_path='/home/harpal/Desktop/StockHistorical/data', chunk_size = 10):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.date = date = datetime.datetime.now().date()
        self.base_path = base_path
        self.ticks_queue = queue.Queue(500)
        if base_path:
            self.base_path = base_path
            
        self.__logger_dict = {'NSE':{},'BSE':{}}      
        self.stop_flag = False
        self.chunk_size = chunk_size
        self.count = 0
        self.last_ticks={}
        #self.cur_time = None
        
    
    def __log_into_panda(self,ticks):
        self.count += 1
        #print(self.count)
        for tick in ticks:
            #if self.cur_time == tick['timestamp']:
                #continue
            #self.cur_time = ticks['timestamp']
            symbol = tick['symbol']
            exchange = tick['exchange']
            
            # Don't save too much data 
            #last_tick = self.last_ticks.get(exchange+symbol)
            #if last_tick:
                # Don't save more then one tick per secound
                #if last_tick['timestamp'] == tick['timestamp'] :
                    #continue
                # Don't save repeating price tick
                #if last_tick['ltp'] == tick['ltp'] :
                    #continue
            #self.last_ticks[exchange+symbol] = tick
            if self.__logger_dict[exchange].get(symbol,None):
                self.__logger_dict[exchange][symbol].append(tick)
            else:
                log_path = self.base_path+'/'+exchange+'/'+symbol               
                if not os.path.exists(log_path):
                    os.makedirs(log_path)
                    
                log_file = log_path +'/'+str(self.date)+'.csv' 
                self.__logger_dict[exchange][symbol] = TickLogger(csv_file_name = log_file, tick=tick)
    
    def save_to_files(self):
        for exchange in self.__logger_dict:
            exchange_temp = self.__logger_dict[exchange]
            for tick_logger in exchange_temp:
                exchange_temp[tick_logger].save()
                
    def stop(self):
        self.stop_flag = True
        
    def log_ticks(self,ticks):
        if not self.ticks_queue.full():
            self.ticks_queue.put(ticks)
        else:
            print('Hs Logger Queue is Full')
        
                
    def run(self):
        while True:
            while not self.ticks_queue.empty():
                ticks = self.ticks_queue.get()
                self.__log_into_panda(ticks)
            
            if self.count >= self.chunk_size:
                self.count = 0
                self.save_to_files()
                 
            if self.stop_flag:
                self.save_to_files()
                break
            time.sleep(10)
```

#### File: `Stock.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:50:26 2020

@author: harpal
"""

import json
import time
import os
from Brokers.Zerodha import ZC
import datetime as dt
import pandas as pd
#from HPlots import Hplotter
import math
class AdDict(dict):
    def __setattr__(self, key, value):
        self[key]=value

    def __getattr__(self, item):
        return self.get(item)
    
class Stock:

    #broker = None  
    def __init__(self, exchange, symbol, broker):
        self.broker = broker
        self.log_path = "logs/"
        self.setup_path = self.broker.user_name + '/'
        self.state = AdDict()
        
        
        #Get Stats Data from log files
        self.exchange = exchange
        self.symbol = symbol
        self.file_name = exchange + '_' + symbol
        f_name =self.setup_path+ self.file_name + ".json"
        if os.path.exists(f_name):
            with open(f_name, 'rb') as input:
                self.state.update(json.load(input))
                self.stats= AdDict()
                self.stats.update(self.state['stats'])
                self.state['stats'] = self.stats
                #print(self.state)
        else: 
            self.state.charting = False
            self.state.stats = self.stats= AdDict()
            self.stats.equity_margin = None
            self.stats.budget = 50000
            self.stats.lot_value = 5000
            self.stats.holdings = 0
            self.stats.profit = 0
            self.stats.invested = 0
            self.stats.trades_count = 0
            self.stats.avg_price = 0
            self.stats.ltp = None
            self.state.buy_stack = [] #Format:- {'price':1000,'qtn':10}
            self.state.sell_stack = [] #Format:- {'price':1000,'qtn':10}
            self.state.active_stratergy = 'SimpleRenko'
        self.ltp = self.stats.ltp
        self.margin=self.stats.equity_margin
        self.update_margins()
        
    def update_margins(self):
        try:
            time.sleep(1)
            margins = self.broker.get_margins()
            print('Margins', margins)
            self.margin  =  margins['equity']['Available margin']
            print('Margin:', self.margin)
        except:
            print('Get Margin Failed')
        
    def square_off_buy_trade(self, trade):
        #price = trade['price'] 
        qtn = trade['qtn']        
        self.place_sell_order(qtn = qtn)
        pro = (self.ltp - trade['price']) * qtn
        self.stats.profit += pro
        self.stats.trades_count+=1
        self.state.buy_stack.remove(trade)
        msg = self.exchange+ '-' + self.symbol +str(self.ltp) + " Sell Qty "+str(qtn) + 'profit:' + str(pro)
        subject = self.broker.user_name + ' sell order placed'
        #self.broker.mailer.mail(subject=subject, text=msg)
        print(subject + msg)
        
        
    def square_off_sell_trade(self,trade):
        qtn = trade['qtn']    
        self.place_buy_order(qtn = qtn)
        self.state.sell_stack.remove(trade)
        #self.state.buy_stack.append(trade)

                
    def chart_it(self, data):
        if self.state.charting:
            pass
            #self.plotter = Hplotter(self.exchange, self.symbol, data)
            #self.plotter.start()

    #TODO pass parameters              
    def place_buy_order(self, qtn = None):
        if qtn is None:
            qtn = math.floor(self.stats.lot_value/self.ltp)
        if qtn > 0:
            self.broker.place_order(exchange = self.exchange, symbol = self.symbol,
                                    price = self.ltp, qtn=qtn)
            self.update_margins()
            self.stats.invested += self.ltp * qtn
        self.state.buy_stack.append({'price':self.ltp,'qtn':qtn})
        msg = self.exchange + '-' + self.symbol +str(self.ltp) + " Buy Qty "+str(qtn)
        subject = self.broker.user_name + ' buy order placed'
        #self.broker.mailer.mail(subject=subject, text=msg)
        print(subject + msg)
        

    #TODO pass parameters
    def place_sell_order(self, qtn = 1):
        if qtn > 0:
            self.broker.place_order(exchange = self.exchange, symbol = self.symbol,
                                    transaction_type =ZC.TRANSACTION_TYPE_SELL,
                                    price = self.ltp, qtn = qtn)   
            self.update_margins()
            self.stats.invested -= self.ltp * qtn
        self.state.sell_stack.append({'price':self.ltp,'qtn':qtn})

        
       
    def save(self):  
        self.stats.ltp = self.ltp
        self.stats.equity_margin = self.margin
        if self.state.charting:
            self.plotter.stop()
        f_name =self.setup_path+ self.file_name + ".json"
        if not os.path.exists(self.setup_path):
            os.makedirs(self.setup_path)
            
        with open(f_name, 'w') as output:
            #print(self.state)
            json.dump(self.state, output, indent=4)
            
    #def __del__(self):
    #    self.save()
    
'''
    def place_order(self,symbol = None,
                    exchange= None, 
                    product = ZC.PRODUCT_TYPE_CNC,
                    transaction_type =ZC.TRANSACTION_TYPE_BUY,
                    order_type = ZC.ORDER_TYPE_MARKET,
                    price = None, 
                    qtn = 1 ):
'''
```


==================================================


## [3/3] Repository: kite-automatic-trading (`PHASE4-QUANT-149`)
- **Full Name**: `PHASE4-QUANT-149_yash12392__kite-automatic-trading`
- **Description**: To automatic trade on Kite (By Zerodha) with a Simple Moving Average strategy
- **GitHub Stars**: 58
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# kite-automatic-trading
To trade automatically on Kite (By Zerodha) with a Simple Moving Average strategy

IMPORTANT: You need to be a client of Zerodha to use this Code on your system.
You need to be registered as a Kite Developer on www.kite.trade
You can access the tokens, secret key and public tokens after paying their fee and test this strategy and even make yours too.

This strategy is fairly simple and just for fun. I do no guarantee any profitable risks as an outcome of this strategy. 
Invest wisely and consult a financial advisor.

The strategy is based on 5-point Moving Average... This strategy was demonstrated in the Quantinsti Webinar which was hosted by Nithin Kamath and Satyajit Mukherjee.

Plug in your access tokens to use the code.
Plug in the to and from date accordingly to access the historical data.
Plug in the instrument on which you want to trade

You can refer to the Kite Documentation for Python for more strategies and tools: https://kite.trade/docs/pykiteconnect/

### Core Implementation Code & Architecture
#### File: `Kite_Trading.py`
```python
# coding: utf-8

#Making all the necessary imports
from kiteconnect import KiteConnect

#Initializing all the variables we need
api_key = ""
access_token = ""
client_id = ""

#Instrument Token of the security you want to trade using this program
instrument_token = ""

#Dates between which we need historical data
from_date = "2016-10-01"
to_date = "2016-10-21"

#Interval for the data to be fetched
interval = "5minute"

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

#A function to get historical data from Kite
def get_historical_data():
    return kite.historical(instrument_token , from_date , to_date , interval)
"""Implementation of this strategy is, we go to the fetched data collected using Kite, calculate the moving averages
and buy and sell according to the data"""


#Lets build a function for the strategy

def strategy(records):
    total_closing_price = 0
    record_count = 0
    order_placed = False
    last_order_placed = None
    last_order_price = 0
    profit = 0
    
    for record in records:
        record_count += 1
        total_closing_price += record['close']
        
        #Moving average is calculated for every 5 ticks
        if record_count >= 5:
            moving_average = total_closing_price/5
            
            #If moving average is greater than the last tick, we place a buy order
            if record['close'] > moving_average:
                if last_order_placed == "SELL" or last_order_placed is None:
                    
                    #If last order was Sell, we need to exit the stock first
                    if last_order_placed == "SELL":
                        print("Exit SELL")
                        
                        #Calculate Profit
                        profit += last_order_price - record['Close']
                        last_order_price = record['Close']
                        
                    #New Buy Order
                    print("Place a new BUY Order")
                    last_order_placed == "BUY"
                    
            #If moving average is less than the last tick and there is a position, place a sell order
            elif record['close'] < moving_average:
                if last_order_placed == "BUY":
                
                    #As last trade was a buy, lets exit it first
                    print("Exit BUY")
                
                #Calculate Profit again
                profit += record['close'] - last_order_price
                last_order_price = record['close']
                
                #Fresh SELL Order
                print("Place new SELL Order")
                last_order_placed == "SELL"
                
        total_closing_price == records[record_count - 5]['close']
    print("Gross Profit",profit)
    #Place the last order
    place_order(last_order_placed)
    

#Place an order based on the transaction type(BUY/SELL)
def place_order(transaction_type):
    kite.order_place(tradingsymbol = "KIRIINDUS", exchange = "NSE", quantity = 1, transaction_type=transaction_type,
                    order_type="MARKET",product="CNC")
    
def start():
    records = get_historical_data()
    strategy(records)

start()
```


==================================================
