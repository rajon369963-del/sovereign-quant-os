# ⚡ [QUANT-SOURCE-157] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_157_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: zerodha-algorithmic-trader (`PHASE4-QUANT-155`)
- **Full Name**: `PHASE4-QUANT-155_xzaviourr__zerodha-algorithmic-trader`
- **Description**: Archived Flask trading-server prototype integrating Zerodha Kite Connect with five-EMA and Bank NIFTY short-straddle strategies; not investment advice.
- **GitHub Stars**: 8
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Zerodha Algorithmic Trading Server

A Python/Flask prototype for controlling two Zerodha Kite Connect strategies:
a five-EMA futures strategy and a Bank NIFTY short straddle. It exposes
development API endpoints for strategy parameters, status, positions, and a
CSV-backed tradebook, with paper-trading support in the strategy properties.

> **Financial risk warning:** this archived software can place real orders when
> configured for live trading. It is unmaintained, unaudited, and not investment
> advice. Do not connect it to a funded account without independent review,
> current broker/API compliance, extensive testing, and explicit risk controls.

## Components

- `API/api_connect.py` — Flask/CORS control API
- `Broker/main_broker.py` — Kite Connect authentication, market data, and order
  adapter
- `Strategy/five_ema.py` — five-EMA futures signal and position management
- `Strategy/short_straddle.py` — timed options straddle workflow
- `Strategy/properties.json` — target, stop-loss, trailing stop, size, and
  paper-trading parameters
- `main.py` — development server on port 12345

The short-straddle worker starts when the API module is imported. The five-EMA
worker is toggled through `/make_bot_active`.

## Historical setup

Use an isolated environment compatible with the pinned 2022 dependencies:

```bash
git clone https://github.com/xzaviourr/zerodha-algorithmic-trader.git
cd zerodha-algorithmic-trader
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Populate `Broker/credentials.json` locally with your Zerodha credentials. The
checked-in file is an empty template. Never commit API keys, passwords, TOTP
secrets, access tokens, or generated trade logs. Review
`Strategy/properties.json` and keep `paper_trading` enabled during evaluation.

## API outline

- `GET /` — server status
- `POST /change_params` — update strategy settings
- `POST /make_bot_active` — start/stop the five-EMA worker
- `GET /get_bot_status` — five-EMA activity flag
- `GET /fetch_attributes` — supported instrument/strategy values
- `GET /positions` — combined strategy positions
- `GET /tradebook` — CSV trade history

These endpoints have no authentication or authorization and must not be exposed
to an untrusted network.

## Limitations

- Strategies rely on hard-coded market times and Bank NIFTY symbol conventions
  that may no longer match current Zerodha APIs or exchange rules.
- There is no reproducible backtest, slippage/cost model, automated test suite,
  durable job control, or production-grade error recovery.
- Threads are created as module side effects.
- Historical performance is not documented and no profitability claim is made.

## Maintenance and license

Development stopped in January 2023 and the repository is archived. The
original source code is available under the [MIT License](LICENSE); Zerodha
APIs, market data, and third-party dependencies retain their own terms.

### Core Implementation Code & Architecture
#### File: `main.py`
```python
from API.api_connect import app

app.run('0.0.0.0', port=12345)
```

#### File: `Broker/credentials.json`
```python
{
    "name": "",
    "user_id": "",
    "password": "",
    "api_key": "",
    "api_secret": "",
    "totp_code": ""
}
```

#### File: `Strategy/properties.json`
```python
{
    "target": 200,
    "trailing_stoploss": 20,
    "quantity": 1,
    "lot_size": 25,
    "stoploss": 200,
    "paper_trading": 1
}
```

#### File: `settings.py`
```python
import os
import json

# GLOBAL PATHS
# ===========================================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BROKER_DIR = os.path.join(BASE_DIR, "Broker")
STRATEGY_DIR = os.path.join(BASE_DIR, "Strategy")

BROKER_CREDENTIALS_FILE = os.path.join(BROKER_DIR, "credentials.json")
INSTRUMENTS_FILE = os.path.join(BROKER_DIR, "instruments.csv")
ACTION_PROPERTIES_FILE = os.path.join(STRATEGY_DIR, "properties.json")

LOGS_FOLDER = os.path.join(BASE_DIR, "Logs")
CSV_LOGS_FILE = os.path.join(LOGS_FOLDER, "order_log.csv")
SHORT_STRADDLE_ORDER_LOG_FILE = os.path.join(BASE_DIR, "short_straddle_orders.csv")

# CREATING CREDENTIAL FILE TEMPLATES
# ===========================================================================================
if not os.path.exists(BROKER_CREDENTIALS_FILE):
    broker_cred = {
        "name": "zerodha",
        "user_id": "",
        "password": "",
        "api_key": "",
        "api_secret": "",
        "totp_code": ""
    }
    with open(BROKER_CREDENTIALS_FILE, 'w') as file:
        json.dump(broker_cred, file)

# GLOBAL VARIABLES
# ===========================================================================================
SLEEP_TIME_BETWEEN_ATTEMPTS = 1   # Time (in sec) for which the process will sleep before retyring

MAX_BROKER_LOGIN_ATTEMPT_COUNT = 5  # Number of attempts made to login with the broker
MAX_FETCH_INSTRUMENT_FILE_ATTEMPT_COUNT = 3 # Number of attempts made to fetch and load the instruments file
MAX_ORDER_PLACEMENT_RETRIES = 5 # Number of attempts to place the order
MAX_ORDER_CANCELLATION_RETRIES = 5  # Number of attempts to cancel an order
HISTORICAL_DATA_FETCH_MAX_RETRY = 10    # Number of retries to fetch historical data

TICKER_RETRY_TIMEOUT = 5    # Time (in sec) till we will wait for ticker to start
DATA_UPDATE_TIME = 3    # Time after which live data is updated
```

#### File: `API/api_connect.py`
```python
from crypt import methods
from flask import Flask, request, jsonify
import json
import threading
import datetime
import pandas as pd
from time import sleep
from flask_cors import CORS, cross_origin

from Strategy.five_ema import FiveEMA
from Strategy.short_straddle import ShortStraddle
from Broker.main_broker import Zerodha
import settings

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

broker_instance = Zerodha()
five_ema_strategy_instance = FiveEMA(broker_instance)
short_straddle_strategy_instance = ShortStraddle(broker_instance)
short_straddle_thread = threading.Thread(target=short_straddle_strategy_instance.run_short_straddle)
short_straddle_thread.start()

def update_broker_instance_on_new_day():
    """
    Updates broker instance at the start of the day
    """
    global broker_instance
    while True:
        if datetime.datetime.now().time() >= datetime.time(9, 15, 15, 0) and datetime.datetime.now().time() <= datetime.time(9, 16, 0, 0):
            broker_instance = Zerodha()
        sleep(20)

broker_replacement_thread = threading.Thread(target=update_broker_instance_on_new_day)
broker_replacement_thread.start()


@app.route("/", methods=['GET'])
@cross_origin()
def check_server_active():
    return "SERVER RUNNING", 200

@app.route("/change_params", methods=['POST'])
@cross_origin()
def change_params():
    new_params = json.loads(request.data)
    new_properties = {
    "target": new_params['TARGET'],
    "trailing_stoploss": new_params['TRAILING_STOPLOSS'],
    "quantity": new_params['QUANTITY'],
    "lot_size": new_params['LOT_SIZE'],
    "stoploss": new_params['STOPLOSS'],
    "paper_trading": new_params['PAPER_TRADING']
    }   
    with open(settings.ACTION_PROPERTIES_FILE, 'w') as file:
        file.write(json.dumps(new_properties, indent=4))
    return "PARAMS UPDATED", 200

@app.route("/make_bot_active", methods=['POST'])
@cross_origin()
def make_bot_active():
    global five_ema_strategy_instance
    bot_status = json.loads(request.data)
    if bot_status['STATUS'] == "ACTIVE":
        strategy_instance_thread = threading.Thread(target=five_ema_strategy_instance.run_5ema)
        strategy_instance_thread.start()
    else:
        if five_ema_strategy_instance != None:
            five_ema_strategy_instance.strategy_active_flag = False
    return "BOT STATUS UPDATED", 200

@app.route("/get_bot_status", methods=['GET'])
def get_bot_status():
    global five_ema_strategy_instance
    if five_ema_strategy_instance == None:
        return "0", 200
    if five_ema_strategy_instance.strategy_active_flag == True:
        return "1", 200
    else:
        return "0", 200

@app.route('/fetch_attributes', methods=['GET'])
@cross_origin()
def fetch_attributes():
    global broker_instance

    month_mapping = {1:"JAN", 2:"FEB", 3:"MAR", 4:"APR", 5:"MAY", 6:"JUN", 7:"JUL", 8:"AUG", 9:"SEP", 10:"OCT", 11:"NOV", 12:"DEC"}
    month = month_mapping[datetime.date.today().month]
    year = (datetime.date.today().year)%100
    tradingsymbol = f"BANKNIFTY{year}{month}FUT"
    if broker_instance.check_trading_symbol(tradingsymbol) != True:
        month = month_mapping[(datetime.date.today().month + 1)%12]
        if datetime.date.today().month == 12:
            year = year+1
    
    response = {
        "FUTURE": ["BANKNIFTY FUT"],
        "EXPIRY": [f"{month} {year}"],
        "CANDLE_TIME": ["5 MINUTE"],
        "BUY_OR_SELL": ["BUY"],
        "STRATEGY": ['Five EMA']
    }
    return jsonify(response), 200

@app.route('/positions', methods=['GET'])
@cross_origin()
def fetch_positions():
    global five_ema_strategy_instance, short_straddle_strategy_instance
    response_five_ema = five_ema_strategy_instance.get_positions()
    response_short_straddle = short_straddle_strategy_instance.get_positions()
    response = response_five_ema + response_short_straddle
    response = [x for x in response if x != None]
    return jsonify(response), 200

@app.route('/tradebook', methods=['GET'])
@cross_origin()
def fetch_tradebook():
    import csv
    with open(settings.CSV_LOGS_FILE, mode='r') as infile:
        reader = csv.reader(infile)
        counter = 0
        response = []

        keys = ['orderID', 'dateTimes', 'instrumentType', 'orderType', 'quantity', 'target', 'stoploss', 'trailingSL', 'bankFutPrice', 'paperTrade']
        for row in reader:
            if counter == 0:
                pass
            else:
                new_dict = {}
                for i in range(len(keys)):
                    new_dict[keys[i]] = row[i]
                response.append(new_dict)
            counter += 1

    json_response = json.dumps(response, indent=4)
    print(json_response)
    return json_response, 200
```

#### File: `Strategy/five_ema.py`
```python
# SYSTEM
import logging
import os
import datetime
import threading
from time import sleep

#DATA
import pandas_ta as ta
import json

# CUSTOM 
from Broker.main_broker import Zerodha
import settings


class FiveEMA:
    def __init__(self, broker:Zerodha):
        self.__broker = broker
        if self.__broker == None:
            exit(1)
        self.logger = self.get_logger()

        self.month_mapping = {1:"JAN", 2:"FEB", 3:"MAR", 4:"APR", 5:"MAY", 6:"JUN", 7:"JUL", 8:"AUG", 9:"SEP", 10:"OCT", 11:"NOV", 12:"DEC"}
        self.last_fetched_record_time = None
        self.strategy_active_flag = False

        self.trade_region = False
        self.trigger_candle = None

        try:
            with open(settings.ACTION_PROPERTIES_FILE) as file:
                self.action_properties = json.load(file)
            self.logger.info("Action properties successfully loaded")
        except Exception as e:
            self.logger.critical("Action properties file cannot be found. Application exiting.\n")
    
    def get_logger(self):
        """
        Creates a logger with stream and file handlers, and returns it. 
        """
        logger = logging.getLogger('FiveEMA Logger')
        logger.setLevel(logging.DEBUG)
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(os.path.join(settings.LOGS_FOLDER, "FiveEMA.log"))
        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        logger.info("Logger initialized")
        return logger

    def get_ema(self, market_data):
        """
        Returns EMA field in the dataframe provided
        """
        no_of_records_fetched = market_data.shape[0]
        no_of_records_fetched = min(no_of_records_fetched, 5)
        market_data['EMA'] = ta.ema(market_data['close'], length=no_of_records_fetched)

    def get_atm_pe(self, price):
        """
        Returns selected BankNifty ATM PE for the price passed
        """
        if price%100 >= 50:
            price = ((price//100)+1)*100
        else:
            price = (price//100)*100

        bnf_fut = self.__broker.get_trading_symbol(self.__broker.bank_nifty_fut_instrument_token)[:-3]
        tradingsymbol = f"{bnf_fut}{int(price)}PE"
        return tradingsymbol

    def get_positions(self):
        """
        Returns the current positions
        """
        return self.__broker.get_positions()

    def update_broker_instance(self, broker):
        """
        Updates new broker instance
        """
        self.__broker = broker

    def run_5ema(self):
        """
        Run 5EMA strategy unless explicitely stopped
        """    
        self.logger.info("5EMA strategy started...")
        self.strategy_active_flag = True

        while True:
            self.logger.info("Waiting for market to start ...")
            while datetime.datetime.now().time() <= datetime.time(9, 16, 0, 0) or datetime.datetime.now().time() >= datetime.time(14, 30, 0, 0):
                sleep(settings.SLEEP_TIME_BETWEEN_ATTEMPTS)
                if self.strategy_active_flag == False:
                    return
            self.logger.info("Market in progress ...")

            while True: # Run this strategy unless stopped otherwise
                self.logger.info("Waiting for the next candle ...")
                mins = datetime.datetime.now().time().minute
                nearest_interval = ((mins//5 + 1)*5)%60
                while(datetime.datetime.now().time().minute != nearest_interval):    # Wait till the nearest 5 min interval
                    sleep(settings.SLEEP_TIME_BETWEEN_ATTEMPTS)

                if datetime.datetime.now().time() >= datetime.time(14, 30, 0, 0):  # Market Ended, so stop the strategy
                    self.strategy_active_flag = False
                    self.logger.info("Five EMA strategy stopped till next day. Market Closing.")
                    break
                
                while True:
                    if self.strategy_active_flag == 0:  # Strategy stopped by external event
                        return

                    market_data = self.__broker.fetch_BNF_historical_data()
                    latest_record_time = market_data['date'].iloc[-1]

                    if latest_record_time != self.last_fetched_record_time:  # New data available now
                        self.last_fetched_record_time = latest_record_time
                        break
                    sleep(settings.SLEEP_TIME_BETWEEN_ATTEMPTS)

                self.logger.info(f"TIME : {datetime.datetime.now()}\nNew Candle Fetched\n Candle TimeStamp : {latest_record_time}")

                self.get_ema(market_data)   # Get values of EMA
                new_candle = market_data.iloc[-1]

                # STRATEGY
                # ===========================================================
                if self.trade_region == False:  # If I am currently out of the trade region
                    if self.__broker.is_active_trade == True:   # Trade is already running
                        self.last_candle = new_candle
                    elif new_candle['low'] > new_candle['EMA']:
                        self.logger.info("Entered Trade Region")
                        self.logger.info(f"Current Candle Low : {new_candle['low']} | Current EMA : {new_candle['EMA']}")
                        self.trigger_candle = new_candle    # New trigger candle
                        self.last_candle = new_candle   # Last candle
                        self.trade_region = True    # Moved into the trade region
                    else:
                        self.logger.info("Candle below EMA, out of trade region")
                        self.logger.info(f"Current Candle Low : {new_candle['low']} | Current EMA : {new_candle['EMA']}")

                else:   # If I am currently in the trade region
                    if new_candle['close'] < self.trigger_candle['low']:    # Execute order
                        self.logger.info("Order Executing")
                        self.logger.info(f"Current Candle Close : {new_candle['close']} | Trigger Candle Low : {self.trigger_candle['low']}")
                        
                        # Fetch all the action properties
                        lot_size = self.action_properties['lot_size']
                        qty = self.action_properties['quantity']
                        target = self.action_properties['target']
                        stoploss = min(float(self.action_properties['stoploss']), float(self.trigger_candle['high'] - new_candle['close']))
                        trailingSL = self.action_properties['trailing_stoploss']
                        paper_trading = True if self.action_properties['paper_trading'] == 1 else False
                        
                        tradingsymbol = self.get_atm_pe(new_candle['close'])    # ATM PE TRADING SYMBOL

                        self.__broker.place_buy_order(
                            tradingsymbol = tradingsymbol,
                            quantity = lot_size * qty,
                            target = new_candle['close'] + min(target, 3*stoploss), 
                            stoploss = stoploss,
                            trailingSL = trailingSL,
                            price = new_candle['close'],
                            paper_trading=paper_trading
                        )
                        self.close_position_thread = threading.Thread(target=self.__broker.close_position)
                        self.close_position_thread.start()

                        self.trade_region = False   # Come out of trade region

                    elif new_candle['close'] > self.trigger_candle['low']:  # Shift to new trigger candle
                        if new_candle['low'] > new_candle['EMA'] and new_candle['low'] > self.last_candle['low']:
                            self.logger.info("Trigger candle shifted")
                            self.logger.info(f"Low : {new_candle['low']} EMA : {new_candle['EMA']} Last Low : {self.last_candle['low']}")
                            self.trigger_candle = new_candle
                        else:
                            self.logger.info("EMA touching candle, Waiting for next one ..")
                    self.last_candle = new_candle
```


==================================================


## [2/3] Repository: options-strats (`PHASE4-QUANT-166`)
- **Full Name**: `PHASE4-QUANT-166_vaibhavswaminathan__options-strats`
- **Description**: Algorithmic trading strategies for options on NSE/BSE (Indian stock markets)
- **GitHub Stars**: 7
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# options-strats
### Algorithmic trading strategies for options on NSE/BSE (Indian stock markets)
#### What this project is about
Algorithmic trading uses fundamental analysis of markets, financial instruments to assess the factors that lead to their performance over time. This can help in taking informed
trading decisions. Knowledge is power. Thus, this project does not aim to *'beat the market'* or *'boost returns'*; it is primarily to develop a deeper understanding of financial data
and to use programming to code potential strategies.

#### Motivation
- better understanding of finance, markets, trading
- become comfortable handling large timeseries data
- become comfortable with visualization, summarisation of data
- do a deployment and test it on live-data

### Core Implementation Code & Architecture
#### File: `drive_utility.py`
```python
# imports
import io
from googleapiclient.http import MediaIoBaseDownload

# initialising google drive api
from googleapiclient.discovery import build
drive_service = build('drive', 'v3')


FILE_ID = None
QUERY = "name = 'BANKNIFTYWK16500PE.csv' and mimeType = 'text/csv'"

def getFileList(service,query=None):
  """Search for file and retrieve file id
  Args:
    service: Google Drive API service instance
  Returns:
    file id
  """
  response = []
  page_token = None
  while True:
    param = {}
    param['q'] = query
    if page_token:
      param['pageToken'] = page_token
    files = service.files().list(**param).execute()
    response.extend(files['files'])
    page_token = files.get('nextPageToken')
    if not page_token:
      break
  return response

def downloadFromDrive(service,fileid):
  """Download file from Drive
  Args:
    service: Google Drive API service instance
    fileid: file id of file to be downloaded
  Returns:
    object of io class containing downloaded fie content as bytes
  """
  request = service.files().get_media(fileId=fileid)
  downloaded = io.BytesIO()
  downloader = MediaIoBaseDownload(downloaded, request)
  done = False
  while done is False:
      status, done = downloader.next_chunk()
      print("Download %d%%." % int(status.progress() * 100))
  return downloaded
```

#### File: `straddle_prep.py`
```python
# imports
import pandas as pd
import drive_utility as du
import io
from datetime import timedelta

# fetching stock price (for BANKNIFTY)
TICKER = 'BANKNIFTY'
TICKER_COLUMNS = ['Ticker','Date','Time','Open','High','Low','Close','Volume','OpenInterest']
ticker_data = pd.DataFrame()

ticker_query = "name = '%s' and mimeType = 'application/vnd.google-apps.folder'" % TICKER
FILE_LIST = du.getFileList(drive_service,ticker_query)
for file in FILE_LIST:
  FILE_ID = file['id']

filesinfolder_query = "'%s' in parents" % FILE_ID
FILE_LIST = du.getFileList(drive_service,filesinfolder_query)
for file in FILE_LIST:
  downloaded = du.downloadFromDrive(drive_service,file['id'])
  buffer_contents = downloaded.getvalue().decode(encoding='utf-8')
  data = io.StringIO(buffer_contents)
  ticker_data = ticker_data.append(pd.read_csv(data,sep=",",names=TICKER_COLUMNS,index_col=False),ignore_index=True)
ticker_data['DateTime'] = ""

# converting date, time values to the datetime dtype
for index in ticker_data.index:
  counter = 0
  ticker_year, ticker_month, ticker_day = '','',''
  for char in str(ticker_data['Date'][index]):
    counter += 1
    if counter<=4:
      ticker_year += char
    elif counter>4 and counter <=6:
      ticker_month += char
    else:
      ticker_day += char
  ticker_data['DateTime'][index] = pd.to_datetime(ticker_year+' '+ticker_month+' '+ticker_day+' '+ticker_data['Time'][index])
ticker_data = ticker_data.drop(['Date','Time'],axis=1)

# fetching folder for year (eg:2020)
YEAR_START = 2020
QUERY = "name = '%d' and mimeType = 'application/vnd.google-apps.folder'" % YEAR_START
FILE_LIST = getFileList(drive_service,QUERY)
for files in FILE_LIST:
  FILE_ID = files['id']
  
# fetching files in year folder
filesinfolder_query = "'%s' in parents" % FILE_ID
FILE_LIST = getFileList(drive_service,filesinfolder_query)

# fetching all dates when Straddle to be executed
dateinfile = []
allDaysForOptions = [] #to store calculable days for each weekly expiry
for file in FILE_LIST:
  dateinfile = file['name'].split(maxsplit=1)[-1]
  dateinfile += str(YEAR_START)
  rawdate = pd.to_datetime(dateinfile)
  dayCounter = rawdate.dayofweek + 1
  optionDaysForWeek = []
  insertCounter = 0
  while len(optionDaysForWeek) <= dayCounter:
    if (rawdate-(timedelta(insertCounter))).dayofweek != 5 and (rawdate-(timedelta(insertCounter))).dayofweek != 6: #accounting for Saturdays and Sundays
      optionDaysForWeek.append(rawdate-timedelta(insertCounter))
    insertCounter += 1
  allDaysForOptions.append(optionDaysForWeek)
  
# adding Date column to ticker data to make date comparisons easier
ticker_data['Date'] = ""
for index in ticker_data.index:
  ticker_data['Date'][index] = ticker_data['DateTime'][index].date()
```


==================================================


## [3/3] Repository: python-option-calculator (`PHASE4-QUANT-181`)
- **Full Name**: `PHASE4-QUANT-181_yzoz__python-option-calculator`
- **Description**: Vanilla option pricing and visualisation using Black-Scholes model in pure Python
- **GitHub Stars**: 135
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Vanilla options calculator
## Black-Scholes model in pure Python 
### Without SciPy, NumPy or other external dependencies

Use **example_greeks.py** to calculate *Theo, Delta, Theta, Vega, Gamma* for single option

Use **example_plot.py** to visualize your position with *Matplotlib*

### Core Implementation Code & Architecture
#### File: `example_greeks.py`
```python
from bsm import BSM

calc = BSM()

#Bitcoin example

S = 21000 #Underlying (price now)
K = 30000 #Strike
V = 0.75 #Implied Volatility (1 / 100%)
T = 30 / 365 #Expiration date (days from now / 365)
dT = "C" #Call / Put

print('Theo: ', round(calc.theo(S, K, V, T, dT), 2))
print('Delta: ', round(calc.delta(S, K, V, T, dT), 2))
print('Theta: ', round(calc.theta(S, K, V, T), 2))
print('Vega: ', round(calc.vega(S, K, V, T), 2))
print('Gamma: ', round(calc.gamma(S, K, V, T), 2))
```

#### File: `bsm.py`
```python
import math

class BSM():

    def pdf(self, x):
        return math.exp(-x**2/2) / math.sqrt(2*math.pi)

    def cdf(self, x):
        return (1 + math.erf(x / math.sqrt(2))) / 2

    def d1(self, S, K, V, T):
        return (math.log(S / float(K)) + (V**2 / 2) * T) / (V * math.sqrt(T))

    def d2(self, S, K, V, T):
        return self.d1(S, K, V, T) - (V * math.sqrt(T))

    def theo(self, S, K, V, T, dT):
        if dT == 'C':
            return S * self.cdf(self.d1(S, K, V, T)) - K * self.cdf(self.d2(S, K, V, T))
        else:
            return K * self.cdf(-self.d2(S, K, V, T)) - S * self.cdf(-self.d1(S, K, V, T))

    def delta(self, S, K, V, T, dT):
        if dT == 'C':
            delta = self.cdf(self.d1(S, K, V, T))
        elif dT == 'P':
            delta = self.cdf(self.d1(S, K, V, T)) - 1
        else:
            delta = 1
        return delta

    def vega(self, S, K, V, T):
        vega = (S * math.sqrt(T) * self.pdf(self.d1(S, K, V, T))) / 100
        return vega

    def theta(self, S, K, V, T):
        theta = -((S * V * self.pdf(self.d1(S, K, V, T))) / (2 * math.sqrt(T))) / 365
        return theta

    def gamma(self, S, K, V, T):
        gamma = self.pdf(self.d1(S, K, V, T))/(S * V * math.sqrt(T))
        return gamma
```

#### File: `plot.py`
```python
from pricing import Pricing
import matplotlib.pyplot as plt

god = 365

class Plot(Pricing):
    def plotPL(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        P_L = []
        for s in bePrice:
           P_L.append(self.p_l(s, params, exp))
        plt.plot(bePrice, P_L, label=int(exp*god))
        
    def plotDelta(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        D = []
        for s in bePrice:
           D.append(self.deltaFull(s, params, exp))  
        plt.plot(bePrice, D, label=int(exp*god))
        
    def plotTheta(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        T = []
        for s in bePrice:
           T.append(self.thetaFull(s, params, exp))
        plt.plot(bePrice, T, label=int(exp*god))
        
    def plotVega(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        V = []
        for s in bePrice:
           V.append(self.vegaFull(s, params, exp))
        plt.plot(bePrice, V, label=int(exp*god))
        
    def plotGamma(self, bePriceS, bePriceF, params, exp, step):
        bePrice = []
        i = bePriceS
        while i <= bePriceF:
            bePrice.append(i)
            i+=step
        V = []
        for s in bePrice:
           V.append(self.gammaFull(s, params, exp))
        plt.plot(bePrice, V, label=int(exp*god))
```

#### File: `pricing.py`
```python
from bsm import BSM

class Pricing(BSM):

    def deltaFull(self, fPrice, params, exp):
        i = 0
        n = len(params)
        deltaFull = 0
        while i < n:
            param = params[i]
            if exp:
                param['exp'] = exp
            deltaSingle = self.delta(fPrice, param['strike'], param['vola'], param['exp'], param['dType']) * param['quant']
            deltaFull = deltaFull + deltaSingle
            i+=1
        return deltaFull

    def vegaFull(self, fPrice, params, exp):
        i = 0
        n = len(params)
        vegaFull = 0
        while i < n:
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] != 'F':
                vegaSingle = self.vega(fPrice, param['strike'], param['vola'], param['exp']) * param['quant']
                vegaFull = vegaFull + vegaSingle
            i+=1
        return vegaFull

    def thetaFull(self, fPrice, params, exp):
        i = 0
        n = len(params)
        thetaFull = 0
        while i < n:
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] != 'F':
                thetaSingle = self.theta(fPrice, param['strike'], param['vola'], param['exp']) * param['quant']
                thetaFull = thetaFull + thetaSingle
            i+=1
        return thetaFull
        
    def gammaFull(self, fPrice, params, exp):
        i = 0
        n = len(params)
        gammaFull = 0
        while i < n:
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] != 'F':
                gammaSingle = self.gamma(fPrice, param['strike'], param['vola'], param['exp']) * param['quant']
                gammaFull = gammaFull + gammaSingle
            i+=1
        return gammaFull

    def p_l(self, fPrice, params, exp):
        i = 0
        n = len(params)
        plF = 0
        while i < n:
            param = params[i]
            if exp:
                param['exp'] = exp
            if param['dType'] == 'F':
                plS = (fPrice - param['price']) * param['quant']
            else:
                theo = round(self.theo(fPrice, param['strike'], param['vola'], param['exp'], param['dType']), 3)
                plS = (theo - param['price']) * param['quant']
            plF = plF + plS
            i+=1
        return plF
```

#### File: `example_plot.py`
```python
from plot import Plot
import matplotlib.pyplot as plt

plot = Plot()

god = 365
step = 10
deep = 7500

exp = 30 / god
exp2 = 15 / god
exp3 = 5 / god

fPrice = 21000

params = []

dType = 'F'
quant = 1
price = 20000
strike = 0
vola = 0
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

dType = 'C'
quant = 1
price = 500
strike = 25000
vola = 0.75
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

dType = 'P'
quant = 1
price = 100
strike = 15000
vola = 0.75
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

dType = 'P'
quant = -1
price = 25
strike = 10000
vola = 1.5
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

bePriceS = fPrice - deep
bePriceF = fPrice + deep

plot.plotPL(bePriceS, bePriceF, params, exp, step)
plot.plotPL(bePriceS, bePriceF, params, exp2, step)
plot.plotPL(bePriceS, bePriceF, params, exp3, step)
plt.ylabel("P/L")
plt.xlabel("Price")
plt.title("Option")
plt.grid(True)
plt.legend()
plt.show()

plot.plotDelta(bePriceS, bePriceF, params, exp, step)
plot.plotDelta(bePriceS, bePriceF, params, exp2, step)
plot.plotDelta(bePriceS, bePriceF, params, exp3, step)
plt.xlabel("Price")
plt.title("Option")
plt.grid(True)
plt.legend()
plt.ylabel("Delta")
plt.show()

plot.plotTheta(bePriceS, bePriceF, params, exp, step)
plot.plotTheta(bePriceS, bePriceF, params, exp2, step)
plot.plotTheta(bePriceS, bePriceF, params, exp3, step)
plt.xlabel("Price")
plt.title("Option")
plt.grid(True)
plt.legend()
plt.ylabel("Theta")
plt.show()

plot.plotVega(bePriceS, bePriceF, params, exp, step)
plot.plotVega(bePriceS, bePriceF, params, exp2, step)
plot.plotVega(bePriceS, bePriceF, params, exp3, step)
plt.xlabel("Price")
plt.title("Option")
plt.grid(True)
plt.legend()
plt.ylabel("Vega")
plt.show()

plot.plotGamma(bePriceS, bePriceF, params, exp, step)
plot.plotGamma(bePriceS, bePriceF, params, exp2, step)
plot.plotGamma(bePriceS, bePriceF, params, exp3, step)
plt.xlabel("Price")
plt.title("Option")
plt.grid(True)
plt.legend()
plt.ylabel("Gamma")
plt.show()


print('D:\t', round(plot.deltaFull(fPrice, params, exp), 2))

print('V:\t', round(plot.vegaFull(fPrice, params, exp), 2))

print('T:\t', round(plot.thetaFull(fPrice, params, exp), 2))

print('G:\t', round(plot.gammaFull(fPrice, params, exp), 2))

print('P/L:\t', plot.p_l(fPrice, params, exp))
```

#### File: `searching.py`
```python
from pricing import Pricing

#in deep development

class Search(Pricing):
    def searchDelta(self, fPrice, deep, acc, paramD, params):
        """if paramD['dType'] == 'C':
            if paramD['quant'] < 0:
                direct = 'U'
            else:
                direct = 'D'
        else:
            if paramD['quant'] < 0:
                direct = 'D'
            else:
                direct = 'U'
        if direct == 'U':
            start = fPrice
            finish = fPrice + deep
        else:
            start = fPrice - deep
            finish = fPrice"""
        matrix = []
        start = fPrice - deep
        finish = fPrice + deep
        while start <= finish:
            deltaD = round((self.delta(start, paramD['strike'], paramD['vola'], paramD['exp'], paramD['dType'])) * paramD['quant'], 4)
            deltaF = round(self.deltaFull(start, params, 0), 3)
            #print(start, '|', deltaD, '|', deltaF)
            if deltaD == -deltaF:
                if paramD['dType'] != 'F':
                    theo = round(self.theo(start, paramD['strike'], paramD['vola'], paramD['exp'], paramD['dType']), 3)
                else:
                    theo = 0
                matrix.append([round(start, 2), paramD['dType'], paramD['strike'], paramD['quant'], deltaD, deltaF , theo])
                #break
            start = start + acc
        i = 0
        n = len(matrix)
        prices = []
        while i < n:
            if prices:
                if matrix[i-1][4] != matrix[i][4]:
                    prices.append(matrix[i])
            else:
                prices.append(matrix[i])
            i = i + 1
        for j in prices:
            print(j[0], '|', j[1], '|', j[2], '|', j[3], '|', j[4], '|', j[5], '|', j[6])

search = Search()

god = 365
step = 10
deep = 7500

exp = 30 / god
exp2 = 15 / god
exp3 = 5 / god

fPrice = 21000

params = []

dType = 'F'
quant = 1
price = 20000
strike = 0
vola = 0
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

dType = 'C'
quant = 1
price = 500
strike = 25000
vola = 0.75
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

dType = 'P'
quant = 1
price = 100
strike = 15000
vola = 0.75
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

dType = 'P'
quant = -1
price = 25
strike = 10000
vola = 1.5
params.append({'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp})

bePriceS = fPrice - deep
bePriceF = fPrice + deep

acc = 0.1

dType = 'F'
strike = 0
price = 0
quant = -1
vola = 0
paramD_1 = {'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp}

dType = 'F'
strike = 0
price = 0
quant = 1
vola = 0
paramD1 = {'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp}

dType = 'F'
strike = 0
price = 0
quant = -2
vola = 0
paramD_2 = {'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp}

dType = 'F'
strike = 0
price = 0
quant = 2
vola = 0
paramD2 = {'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp}

dType = 'F'
strike = 0
price = 0
quant = -3
vola = 0
paramD_3 = {'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp}

dType = 'F'
strike = 0
price = 0
quant = 3
vola = 0
paramD3 = {'dType': dType, 'price': price, 'quant': quant, 'strike': strike, 'vola': vola, 'exp': exp}

search.searchDelta(fPrice, deep, acc, paramD1, params)
search.searchDelta(fPrice, deep, acc, paramD_1, params)
search.searchDelta(fPrice, deep, acc, paramD2, params)
search.searchDelta(fPrice, deep, acc, paramD_2, params)
search.searchDelta(fPrice, deep, acc, paramD3, params)
search.searchDelta(fPrice, deep, acc, paramD_3, params)
```


==================================================
