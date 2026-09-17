# ⚡ [QUANT-SOURCE-122] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_122_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: py5paisa (`VAULT_IN-QUANT-010_OpenApi-5p__py5paisa`)
- **Full Name**: `IN-QUANT-010_OpenApi-5p__py5paisa`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# 5paisa Python SDK

Python SDK for 5paisa APIs natively written in VB .NET

![PyPI](https://img.shields.io/pypi/v/py5paisa)
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/5paisa/py5paisa/Publish%20package/master)

![5paisa logo](./docs/images/5-paisa-img.jpg)

#### Documentation

Read the docs hosted [here](https://www.5paisa.com/developerapi/overview)

#### Features

-   Order placement, modification and cancellation
-   Fetching user info including holdings, positions, margin and order book.
-   Fetching live market streaming.
-   Placing, modifying and deleting Bracket Order.
-   Fetching order status and trade information.
-   Getting live data streaming using websockets.

### Installation

`pip install py5paisa`

### Usage

#### Configuring API keys

Get your API keys from [here](https://xstream.5paisa.com/dashboard)

Note:- We have deprecated the existing method which involved the use of login credentials.
       Kindly go through this updated documentation of using Access token for API Access.

#### Scrip codes reference:
```py
Note : Use these Links for getting scrip codes

Scrip Master - Downaload ScripMaster [here](https://openapi.5paisa.com/VendorsAPI/Service1.svc/ScripMaster/segment/All)

[API Documentation](https://xstream.5paisa.com/dev-docs/docFundamentals/scrip-master)

#Fetch Scrip Codes

scrips = client.get_scrips()

#Query Script Data Inputs sequence- exchange, exchangetype, symbol, strike, type, expiry

#Strike to be 0 for cash stocks , Actual Strike for Derivatives 

#type to be XX for Cash stocks and Futures, EQ for indices, CE/PE for Options

#Fetch Scrip Data for Cash
record = client.query_scrips("N","C","ITC","0","XX","")
#Fetch Scrip Data for Options
record = client.query_scrips("N","D","NIFTY","22300","CE","2024-04-25")
#Fetch Scrip Data for Futures
record = client.query_scrips("N","C","INFY","0","XX","")
```

#### AUTHENTICATION USING OAUTH
```py
from py5paisa import FivePaisaClient
cred={
    "APP_NAME":"YOUR APP_NAME",
    "APP_SOURCE":"YOUR APP_SOURCE",
    "USER_ID":"YOUR USER_ID",
    "PASSWORD":"YOUR PASSWORD",
    "USER_KEY":"YOUR USERKEY",
    "ENCRYPTION_KEY":"YOUR ENCRYPTION_KEY"
    }

#This function will automatically take care of generating and sending access token for all your API's

client = FivePaisaClient(cred=cred)

# OAUTH Approach
# First get a token by logging in to -> https://dev-openapi.5paisa.com/WebVendorLogin/VLogin/Index?VendorKey=<Your Vendor Key>&ResponseURL=<Redirect URL>
# VendorKey is UesrKey for individuals user
# for e.g. you can use ResponseURL as https://www.5paisa.com/technology/developer-apis
# Pass the token received in the response url after successful login to get an access token (this also sets the token for all the APIs you use)-

# Please note that you need to copy the request token from URL and paste in this code and start the code within 30s.

client.get_oauth_session('Your Response Token')

After successful authentication, you should get a `Logged in!!` message in console

#Function to fetch access token after successful login
print(client.get_access_token())

#Login with Access Token
client.set_access_token('accessToken','clientCode')

```

#### Market Feed

```py
#NOTE : ScripData and ScripCode you can find from new Scripmaster as mentioned above


req_list_ = [{"Exch": "N", "ExchType": "C", "ScripData": "ITC_EQ"}]
              {"Exch": "N", "ExchType": "C", "ScripCode": "2885"}]

print(client.fetch_market_feed_scrip(req_list_))

```
#### Market Status
```py
print(client.get_market_status())
```

#### Fetching user info

```py
# Fetches holdings
client.holdings()

# Fetches margin
client.margin()

# Fetches positions
client.positions()

# Fetches the order book of the client
client.order_book()

# Fetches Trade book
client.get_tradebook()

```

#### Position Conversion

```py
# Convert positions
# client.position_convertion(<Exchange>,<Exchange Type>,<Scrip Name>,<Buy/Sell>,<Qty>,<From Delivery/Intraday>,<From Delivery/Intraday>)
client.position_convertion("N","C","BPCL_EQ","B",5,"D","I")
```


#### Placing an order

```py
# Note: This is an indicative order.

from py5paisa.order import Order, OrderType, Exchange

#You can pass scripdata either you can pass scripcode also.
# please use price = 0 for market Order
#use IsIntraday= true for intraday orders

#Using Scrip Data :-

#Using Scrip Code :-
client.place_order(OrderType='B',Exchange='N',ExchangeType='C', ScripCode = 1660, Qty=1, Price=260)
#Sample For SL order (for order to be treated as SL order just pass StopLossPrice)
client.place_order(OrderType='B',Exchange='N',ExchangeType='C', ScripCode = 1660, Qty=1, Price=350, IsIntraday=False, StopLossPrice=345)
#Derivative Order
client.place_order(OrderType='B',Exchange='N',ExchangeType='D', ScripCode = 57633, Qty=50, Price=1.5)

Please refer below documentation link for paramaters to be passed in cleint.place_order function
https://www.5paisa.com/developerapi/order-request-place-order

```
#### Placing offline orders (After Market Orders)

By default all orders are normal orders, pass `AHPlaced=Y` to place offline orders.

```py
client.place_order(OrderType='B',Exchange='N',ExchangeType='C', ScripCode = 1660, Qty=1, Price=325, AHPlaced="Y")
```

#### Modifying an order

```py
client.modify_order(ExchOrderID="1100000017861430", Qty=2,Price=261)
```

#### Cancelling an order

```py
client.cancel_order(exch_order_id="1100000017795041")
```
```py
cancel_bulk=[
            {
                "ExchOrderID": "<Exchange Order ID 1>"
            },
            {
                "ExchOrderID": "<Exchange Order ID 2>"
            },
client.cancel_bulk_order(cancel_bulk)
```

#### Order Margin Calculation
-   This function can help calculate
-   Margin required for single or multileg order
-   Margin required considering existing positions( CoverPosition = Y/N)

```py
Orders2 =[

             {
                "Exch": "N",
                "ExchType": "C",
                "ScripCode": 2885,
                "ScripData": "",
                "PlaceModifyCancel": "P",
                "OrderType": "B",
                "Price": 0,
                "Qty": 1,
                "IsIntraday": False
            },
            {
                "Exch": "B",
                "ExchType": "C",
                "ScripCode": 512070,
                "ScripData": "",
                "PlaceModifyCancel": "P",
                "OrderType": "S",
                "Price": 0,
                "Qty": 1,
                "IsIntraday": True
            }
        ]
a=client.multi_order_Margin(CoverPositions='Y',Orders=Orders2)

```
#### SquareOffAll Orders

```py
client.squareoff_all()
```
#### Bracket Order 

For placing Braket order
```py
client.bo_order(OrderType='B',Exchange='N',ExchangeType='C', ScripCode = 1660, Qty=1, LimitPrice=330,TargetPrice=345,StopLossPrice=320,LimitPriceForSL=319,TrailingSL=1.5)

```
For placing Cover order
```py
client.cover_order(OrderType='B',Exchange='N',ExchangeType='C', ScripCode = 1660, Qty=1, LimitPrice=330,StopLossPrice=320,TrailingSL=1.5)
```

Note:For placing Bracket order in FNO segment pass ExchType='D'

For Modifying Bracket/Cover Order only for Initial order (entry)
```py

client.modify_bo_order(ExchOrderID="1100000017861430",LimitPrice=330)
client.modify_cover_order(ExchOrderID="1100000017861430",LimitPrice=330)

#Note : For cover order just pass LimitPriceProfitOrder equal to Zero.
```

For Modifying LimitPriceProfitOrder 
```py
client.modify_bo_order(ExchOrderID="1100000017861430",TargetPrice=330)
client.modify_cover_order(ExchOrderID="1100000017861430",TargetPrice=330)
```
For Modifying TriggerPriceForSL
```py

client.modify_bo_order(ExchOrderID="1100000017861430",LimitPriceForSL=330)
client.modify_bo_order(ExchOrderID="1100000017861430",LimitPriceForSL=330)

#Note : You have pass atmarket=true while modifying stoploss price, Pass ExchorderId for the particular leg to modify.
```
#### Basket Orders

```py
# Create a new Basket
client.create_basket("<New Basket Name>")

# Rename existing basket
client.rename_basket("<Modified Basket Name>",<Exisiting Basket ID>)

# Clone existing basket
client.clone_basket(<Exisiting Basket ID>)

# Delete bulk baskets
delete_basket_list=[{"BasketID":"<Exisiting Basket ID>"},{"BasketID":"<Exisiting Basket ID>"}]
client.delete_basket(delete_basket_list)


# Get list of all baskets (Open/Closed)
client.get_basket()

basket_list= [
            {
                "BasketID": "<Exisiting Basket ID>"
            },
            {
                "BasketID": "<Exisiting Basket ID>"
            }
        ]
order_to_basket=Basket_order("N","C",23000,"BUY",1,"1660","I")
client.add_basket_order(order_to_basket,basket_list)

# Get orders in basket
client.get_order_in_basket(<Exisiting Basket ID>)

```

#### Fetching Order Status and Trade Information

```py
from py5paisa.order import  Exchange

req_list= [
        {
            "Exch": "N",
            "ExchType": "C",
            "ScripCode": 20374,
            "ExchOrderID": "1000000015310807"
        }]

# Fetches the trade details
client.fetch_trade_info(req_list)

req_list_= [

        {
            "Exch": "N",
            "RemoteOrderID": "90980441"
        }]
# Fetches the order status
client.fetch_order_status(req_list_)

# Fetch Trade History

print(client.get_trade_history("PASS EXCHANGE ORDER ID"))

```
#### Live Market Feed Streaming - Websocket
#NOTE : Webscoket only works with ScripCode
```py
req_list=[
            { "Exch":"N","ExchType":"C","ScripCode":1660},
            ]

req_data=client.Request_Feed('mf','s',req_list)
def on_message(ws, message):
    print(message)


client.connect(req_data)

client.receive_data(on_message)
```
Note: Use the following abbreviations :

Market Feed=mf

Market Depth (upto 5)=md

Indices (Spot Feed) =i

Open Interest=oi

Subscribe= s

Unsubscribe=u

#### Live Market Depth Streaming (Depth 20)

```py
a={
                "method":"subscribe",
                "operation":"20depth",
                "instruments":["NC2885"]
            }
print(client.socket_20_depth(a))
def on_message(ws, message):
    print(message)
client.receive_data(on_message)

Note:- Instruments in payload above is a list(array) in format as <exchange><exchange type><scrip code>
```

#### Level 5 Market Depth 
```py
print(client.fetch_market_depth_by_scrip(Exchange="N",ExchangeType="C",ScripCode="1660"))
print(client.fetch_market_depth_by_scrip(Exchange="N",ExchangeType="C",ScripData="RELIANCE_EQ"))
```

#### Full Market Snapshot 
```py
a=[{"Exchange":"N","ExchangeType":"C","ScripCode":"2885"},
   {"Exchange":"N","ExchangeType":"C","ScripData":"ITC_EQ"},
   ]
print(client.fetch_market_snapshot(a))
```


#### Option Chain
```py
client.get_expiry("N","NIFTY")
# Returns list of all active expiries

# client.get_option_chain("N","NIFTY",<Pass expiry timestamp from get_expiry response>)
client.get_option_chain("N","NIFTY",1647507600000)
```

#### Historical Data
```py
#historical_data(<Exchange>,<Exchange Type>,<Scrip Code>,<Time Frame>,<From Data>,<To Date>)

df=client.historical_data('N','C',1660,'15m','2021-05-25','2021-06-16')
print(df)

# Note : TimeFrame Should be from this list ['1m','5m','10m','15m','30m','60m','1d']
```


#### Bulk Order Placement

```py

bulk_order=[{
        "Exchange":"N", "ExchangeType":"C", "ScripCode":0, "ScripData":"ITC_EQ", "Price": "440", "OrderType": "Buy", "Qty": 1, "DisQty": "0", "StopLossPrice": "0", "IsIntraday": True, "iOrderValidity": "0", "RemoteOrderID":"50000091_220620"
    },{
        "Exchange":"N", "ExchangeType":"C", "ScripCode":0, "ScripData":"IDEA_EQ", "Price": "15", "OrderType": "Buy", "Qty": 1, "DisQty": "0", "StopLossPrice": "0", "IsIntraday": True, "iOrderValidity": "0", "RemoteOrderID":"50000091_220620"
    }
]
client.place_order_bulk(OrderList=bulk_order)
```

#### Strategy Execution
#### List Of Strategies Available
 - Short Straddle
 - Short Strangle
 - Long Straddle
 - Long Strangle
 - Iron Fly(Butterfly)
 - Iron Condor
 - Call Calendar Spread
 - Put Calendar Spread
 - Call Ladder
 - Put Ladder
 - Ladder
```py
#Import strategy package
from py5paisa.strategy import *
```
Note: These single-commands are capable of trading multiple legs of pre-defined strategies.
Like :- Short/Long Straddles and Strangles, Iron Fly and Iron Condor (many more to come)
Please use these at your own risk.
```py
#Create an Object:-
cred={
    "APP_NAME":"YOUR APP_NAME",
    "APP_SOURCE":YOUR APP_SOURCE,
    "USER_ID":"YOUR USER_ID",
    "PASSWORD":"YOUR PASSWORD",
    "USER_KEY":"YOUR USERKEY",
    "ENCRYPTION_KEY":"YOUR ENCRYPTION_KEY"
    }
--Old approach
strategy=strategies(user="random_email@xyz.com", passw="password", dob="YYYYMMDD",cred=cred)
--New Approach
strategy=strategies(cred=cred,request_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUwMDUyNzcwIiwicm9sZSI6ImdpUUlvYXR5R2NYQUR3eFYwNXVXSGlPVzJRT1dOTGNzIiwibmJmIjoxNjY3ODMwODczLCJleHAiOjE2Njc4MzA5MDMsImlhdCI6MTY2NzgzMDg3M30.iP_FZtFy-nj6QeRd0sEhaKS-jr-wu-pCwtcdYCGPeO4")

```
Use the following to execute the strategy (note:- they are executed at market price only)
```py
#short_straddle(<symbol>,<strike price>,<qty>,<expiry>,<Order Type>)
strategy.short_straddle("banknifty",'37000','50','20210610','I',tag='<Your strategy Name>')

#Using tag is optional
```
```py
#short_strangle(<symbol>,<List of sell strike price>,<qty>,<expiry>,<Order Type>)
strategy.short_strangle("banknifty",['35300','37000'],'50','20210610','D')
```
```py
#long_straddle(<symbol>,<strike price>,<qty>,<expiry>,<Order Type>)
strategy.long_straddle("banknifty",'37000','50','20210610','I',tag='<Your strategy Name>')

#Using tag is optional
```
```py
#long_strangle(<symbol>,<List of sell strike price>,<qty>,<expiry>,<Order Type>)
strategy.long_strangle("banknifty",['35300','37000'],'50','20210610','D')
```

```py
#iron_condor(<symbol>,<List of buy strike prices>,<List of sell strike price>,<qty>,<expiry>,<Order Type>)
strategy.iron_condor("NIFTY",["15000","15200"],["15100","15150"],"75","20210603","I")
```

```py
#iron_fly(<symbol>,<List of buy strike prices>,<Sell strike price>,<qty>,<expiry>,<Order Type>)
strategy.iron_fly("NIFTY",["15000","15200"],"15100","75","20210610","I",tag='<Your strategy Name>')

#Using tag is optional
```

```py
#call_calendar(<symbol>,<List of sell strike price>,<qty>,<list of expiry(first one will be bought and the second sold based on expiry)>,<Order Type>)
strategy.call_calendar("nifty",'15600','75',['20210603','20210610'],'I')
```

```py
#put_calendar(<symbol>,<List of sell strike price>,<qty>,<list of expiry(first one will be bought and the second sold based on expiry)>,<Order Type>)
strategy.put_calendar("nifty",'15600','75',['20210603','20210610'],'I')
```

```py
#call_ladder(<symbol>,<Buy strike prices>,<List of Sell strike price>,<qty>,<expiry>,<Order Type>)
strategy.call_ladder("NIFTY","15100",["15300","15400"],"75","20210610","I")
```

```py
#put_ladder(<symbol>,<Buy strike prices>,<List of Sell strike price>,<qty>,<expiry>,<Order Type>)
strategy.put_ladder("NIFTY","15000",["14800","14500"],"75","20210610","I",tag='<Your strategy Name>')

#Using tag is optional
```

```py
#ladder(<symbol>,<List of Buy strike prices>,<List of Sell strike price>,<qty>,<expiry>,<Order Type>)
strategy.ladder("sbin",["400","420"],["350","370","450","500"],"1500","20210729","D")
```

```py
Squareoff a strategy Using tags
strategy.squareoff('tag')

# Use the same tag as used while executing the strategies
```



#### REPORTS

```py
TAX Report
a=client.tax_report("2024-01-01",'2024-06-26')
print(a)

# to fetch Tax report
```
```py
Ledger Report
a=client.fetch_ledger("2024-01-01",'2024-06-26')
print(a)

# to fetch Ledger report
```

#### TODO
 - Write tests.


#### Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python
"""Unit test package for py5paisa."""
```

#### File: `py5paisa/__init__.py`
```python
from py5paisa.py5paisa import FivePaisaClient

__all__ = ["FivePaisaClient"]
```

#### File: `py5paisa/logging.py`
```python
"""
Uses loguru for formatting responses
TODO:
 - Add more extensive logging
"""

import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO",
           format="<green>{time: HH:mm:ss}</green> | <bold>{message}</bold>")


def log_response(message: str) -> None:
    logger.info(message)
```

#### File: `tests/test_py5paisa.py`
```python
#!/usr/bin/env python

"""Tests for `py5paisa` package."""


import unittest

from py5paisa import py5paisa


class TestPy5paisa(unittest.TestCase):
    """Tests for `py5paisa` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
```

#### File: `py5paisa/auth.py`
```python
"""
Contains the core encryption logic
"""

from Crypto.Cipher import AES
import base64
from pbkdf2 import PBKDF2



class EncryptionClient:

    def __init__(self,ENCRYPTION_KEY): 
        self.iv = bytes([83, 71, 26, 58, 54, 35, 22, 11,
                         83, 71, 26, 58, 54, 35, 22, 11])
        self.enc_key = ENCRYPTION_KEY 

    def _pad_and_convert_to_bytes(self, text):
        return bytes(text+chr(16-len(text) % 16)*(16-len(text) % 16), encoding="utf-8")

    def encrypt(self, text):
        padded_text = self._pad_and_convert_to_bytes(text)
        key_gen = PBKDF2(self.enc_key, self.iv)

        aesiv = key_gen.read(16)
        aeskey = key_gen.read(32)
        cipher = AES.new(aeskey, AES.MODE_CBC, aesiv)
    
        return str(base64.b64encode(cipher.encrypt(padded_text)), encoding="utf-8")
```

#### File: `setup.py`
```python
#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "requests",
    "pycryptodome>=3.9.8",
    "certifi>=2020.4.5.1",
    "chardet>=3.0.4",
    "pbkdf2>=1.3",
    "urllib3>=1.25.8",
    "idna>=2.9",
    "loguru>=0.5.1",
    "websocket-client>=0.58.0",
    "pandas>=1.2.4",
    "pyjwt==2.3.0",
    "httpx>=0.28.1,<0.29.0"  # Recommended (allows minor updates)
]

setup_requirements = []

test_requirements = []

setup(
    author="5paisa",
    author_email='coreteam@5paisa.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6'
    ],
    description=" Python SDK for 5paisa APIs natively written in VB.NET",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='py5paisa',
    name='py5paisa',
    packages=find_packages(include=['py5paisa', 'py5paisa.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/5paisa/py5paisa',
    version='0.7.21.2',
    zip_safe=False,
)
```


==================================================


## [2/3] Repository: groww (`VAULT_IN-QUANT-018_kuldeepverma__groww`)
- **Full Name**: `IN-QUANT-018_kuldeepverma__groww`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Groww Trading API

A FastAPI application for interacting with the Groww trading platform with enhanced features including portfolio management, stock quotes, and market status.

## 🚀 Features

- **Order Management**: Place BUY/SELL orders with automatic market/limit detection
- **Stock Quotes**: Get real-time quotes for single or multiple stocks
- **Portfolio Tracking**: View current holdings and P&L (placeholder)
- **Market Status**: Check if markets are open/closed
- **Health Monitoring**: API health checks and status monitoring
- **Push Notifications**: Get notified about order status via Pushbullet
- **Auto-retry**: Automatic token refresh and retry logic

## 🛠️ Local Development

### Prerequisites

1. Python 3.8+ installed
2. Docker installed (for containerized deployment)
3. AWS CLI configured with your credentials

### Quick Start

1. **Clone and setup**:
   ```bash
   git clone <your-repo>
   cd Groww
   ```

2. **Create environment file**:
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

3. **Start development server**:
   ```bash
   ./run-local.sh
   ```

4. **Access your API**:
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

### Development Workflow

Use the interactive development menu:
```bash
./dev-workflow.sh
```

This provides options for:
- 🚀 Starting local server
- 🧪 Running API tests  
- 🐳 Building Docker images
- 📦 Deploying to Lambda
- 📊 Viewing logs
- 🔄 Updating environment variables

### Manual Commands

**Start local server**:
```bash
./run-local.sh
```

**Test API endpoints**:
```bash
./test-api.sh
```

**Build Docker image**:
```bash
sudo docker build -t groww-trading-api:dev .
```

## 📡 API Endpoints

### Basic Endpoints
- `GET /` - Welcome message
- `GET /hello` - Hello message
- `GET /health` - Health check
- `GET /market-status` - Market open/closed status

### Stock Data
- `GET /quote/{ticker}` - Get single stock quote
- `POST /quotes` - Get multiple stock quotes

### Trading
- `POST /order` - Place trading order
- `GET /orders_list` - Get order history
- `POST /stop-loss/sell` - Place stop loss sell order
- `POST /gtt/buy` - Place GTT buy order

### GTT (Good Till Triggered) Orders
- `POST /gtt/order` - Place GTT order (buy/sell)
- `PUT /gtt/order` - Modify existing GTT order
- `GET /gtt/orders` - Get all GTT orders
- `DELETE /gtt/order/{gtt_id}` - Cancel GTT order

### Portfolio
- `GET /portfolio` - Get portfolio holdings (placeholder)

### Utilities
- `POST /test-notification` - Test push notifications

### Example Usage

**Get stock quote**:
```bash
curl http://localhost:8000/quote/SBIN
```

**Get multiple quotes**:
```bash
curl -X POST http://localhost:8000/quotes \
  -H "Content-Type: application/json" \
  -d '["SBIN", "RELIANCE", "TCS"]'
```

**Place order**:
```bash
curl -X POST http://localhost:8000/order \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "SBIN",
    "quantity": 1,
    "transaction_type": "BUY",
    "price": 800
  }'
```

**Place stop loss sell order**:
```bash
curl -X POST http://localhost:8000/stop-loss/sell \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "SBIN",
    "quantity": 10,
    "stop_loss_price": 750,
    "limit_price": 745
  }'
```

**Place GTT buy order**:
```bash
curl -X POST http://localhost:8000/gtt/buy \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "RELIANCE",
    "quantity": 5,
    "transaction_type": "BUY",
    "trigger_price": 2800,
    "limit_price": 2805
  }'
```

**Get GTT orders**:
```bash
curl http://localhost:8000/gtt/orders
```

## 🚀 Deployment Options

### Option 1: AWS Lambda (Container) - Recommended

This deployment method uses Docker containers to deploy to AWS Lambda, which is ideal for applications larger than 50MB.

#### Prerequisites

1. Install Docker and ensure it's running
2. Install the AWS CLI and configure it with your credentials:
   ```
   pip install awscli
   aws configure
   ```

#### Deployment Steps

1. Create your `.env` file with required environment variables:
   ```
   API_KEY=your_api_key_here
   TOTP_SECRET=your_totp_secret_here
   PUSH_TOKEN=your_push_token_here
   ```

2. Deploy to Lambda:
   ```
   ./deploy-lambda.sh
   ```

3. Set environment variables:
   ```
   ./set-env-vars.sh
   ```

#### Monitoring and Management

- View function logs:
  ```
  aws logs tail /aws/lambda/groww-trading-api --follow --region us-east-1
  ```

- Update function code (after making changes):
  ```
  ./deploy-lambda.sh
  ```

- Delete the function:
  ```
  aws lambda delete-function --function-name groww-trading-api --region us-east-1
  ```

### Option 2: AWS Elastic Beanstalk (Legacy)

#### Prerequisites

1. Install the AWS CLI and configure it with your credentials:
   ```
   pip install awscli
   aws configure
   ```

2. Install the Elastic Beanstalk CLI:
   ```
   pip install awsebcli
   ```

#### Deployment Steps

1. Initialize your Elastic Beanstalk application (first time only):
   ```
   eb init -p python-3.8 groww-api --region <your-region>
   ```

2. Create an environment (first time only):
   ```
   eb create groww-api-env
   ```

3. Set up environment variables in the Elastic Beanstalk console:
   - API_KEY
   - TOTP_SECRET
   - PUSH_TOKEN

4. Deploy your application:
   ```
   eb deploy
   ```

Alternatively, you can use the provided deploy.sh script:
```
./deploy.sh
```

#### Monitoring and Management

- To view the application status:
  ```
  eb status
  ```

- To view application logs:
  ```
  eb logs
  ```

- To open the application in a browser:
  ```
  eb open
  ```

- To terminate the environment when no longer needed:
  ```
  eb terminate groww-api-env
  ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```env
API_KEY=your_groww_api_key
TOTP_SECRET=your_totp_secret_key
PUSH_TOKEN=your_pushbullet_token
```

### Development vs Production

- **Local Development**: Uses `uvicorn` with auto-reload
- **Lambda Deployment**: Uses `mangum` adapter for serverless
- **Environment**: Automatically detected based on runtime

## 🧪 Testing

### Automated Testing
```bash
./test-api.sh
```

### Manual Testing
Visit http://localhost:8000/docs for interactive API documentation.

### Load Testing
```bash
# Install hey (HTTP load testing tool)
sudo apt install hey

# Test with 100 requests, 10 concurrent
hey -n 100 -c 10 http://localhost:8000/health
```

## 📊 Monitoring

### Local Development
- Server logs appear in terminal
- Access logs via uvicorn output

### Lambda Production
```bash
# View real-time logs
aws logs tail /aws/lambda/groww-trading-api --follow --region us-east-1

# View specific time range
aws logs tail /aws/lambda/groww-trading-api --since 1h --region us-east-1
```

## 🔒 Security

- Environment variables stored securely in Lambda
- API keys never logged or exposed
- HTTPS enforced in production
- Input validation on all endpoints

## 💰 Cost Optimization

### Lambda Benefits
- Pay only for actual usage
- Automatic scaling
- No idle costs
- ~85-95% cost savings vs traditional servers

### Estimated Costs
- 1,000 requests/month: ~$0.04
- 10,000 requests/month: ~$0.40
- 100,000 requests/month: ~$4.00

## 🚨 Troubleshooting

### Common Issues

**Token Authentication Errors**:
- Check your API_KEY and TOTP_SECRET
- Ensure TOTP is generating correctly
- Token auto-refreshes on failure

**Local Server Won't Start**:
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill existing processes
pkill -f uvicorn
```

**Docker Build Issues**:
```bash
# Clean Docker cache
sudo docker system prune -f

# Rebuild without cache
sudo docker build --no-cache -t groww-trading-api:dev .
```

**Lambda Deployment Issues**:
```bash
# Check AWS credentials
aws sts get-caller-identity

# Verify ECR permissions
aws ecr describe-repositories --region us-east-1
```

## 📝 Development Notes

### Adding New Features

1. **Add endpoint to `app.py`**
2. **Test locally with `./run-local.sh`**
3. **Test with `./test-api.sh`**
4. **Deploy with `./deploy-lambda.sh`**

### Code Structure
```
├── app.py              # Main FastAPI application
├── lambda_handler.py   # Lambda adapter
├── requirements.txt    # Python dependencies
├── Dockerfile         # Container definition
├── .env               # Environment variables (local)
├── run-local.sh       # Local development server
├── test-api.sh        # API testing script
├── dev-workflow.sh    # Development workflow menu
├── deploy-lambda.sh   # Lambda deployment
└── set-env-vars.sh    # Environment variable setup
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Test locally with `./dev-workflow.sh`
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

### Core Implementation Code & Architecture
#### File: `lambda_handler.py`
```python
import json
from mangum import Mangum
from app import app

# Create the Mangum handler
handler = Mangum(app, lifespan="off")

def lambda_handler(event, context):
    """
    AWS Lambda handler function
    """
    # Log the incoming event payload
    print(f"Lambda Event: {json.dumps(event, indent=2)}")
    return handler(event, context)
```

#### File: `app.py`
```python
"""
Groww Trading API
=================
FastAPI application for interacting with the Groww trading platform.
"""

from __future__ import annotations

import contextvars
import logging
import logging.handlers
import math
import os
import re
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, date
from typing import Optional, List

import pyotp
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Security, status
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel, Field, field_validator

from growwapi import GrowwAPI
from growwapi.groww.exceptions import GrowwAPIRateLimitException

_ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(_ENV_PATH)

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
_IS_LAMBDA = bool(os.environ.get("AWS_LAMBDA_FUNCTION_NAME"))

# ContextVar carries the current request's correlation ID into every log line,
# including lines emitted by helpers called from route handlers.
_request_id_var: contextvars.ContextVar[str] = contextvars.ContextVar(
    "request_id", default="-"
)

_log_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - [%(request_id)s] %(message)s"
)

_root_logger = logging.getLogger()
_root_logger.setLevel(logging.INFO)

def _has_handler(logger: logging.Logger, *, handler_type: type, target_name: str | None = None) -> bool:
    normalized_target = os.path.abspath(target_name) if target_name else None
    for handler in logger.handlers:
        if not isinstance(handler, handler_type):
            continue
        if normalized_target is None:
            return True
        handler_target = getattr(handler, "baseFilename", None)
        if handler_target and os.path.abspath(handler_target) == normalized_target:
            return True
    return False


if not _has_handler(_root_logger, handler_type=logging.StreamHandler):
    _stream_handler = logging.StreamHandler()
    _stream_handler.setFormatter(_log_formatter)
    _root_logger.addHandler(_stream_handler)

# On Lambda stdout → CloudWatch; skip the rotating file handler.
# Locally write to /tmp/app.log so the path is always writable.
if not _IS_LAMBDA and not _has_handler(
    _root_logger,
    handler_type=logging.handlers.RotatingFileHandler,
    target_name="/tmp/app.log",
):
    _file_handler = logging.handlers.RotatingFileHandler(
        "/tmp/app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    _file_handler.setFormatter(_log_formatter)
    _root_logger.addHandler(_file_handler)

# Inject request_id from the ContextVar into every log record, but only once.
_current_factory = logging.getLogRecordFactory()
if not getattr(_current_factory, "_groww_request_id_wrapped", False):
    _old_factory = _current_factory

    def _record_factory(*args, **kwargs):
        record = _old_factory(*args, **kwargs)
        record.request_id = _request_id_var.get()
        return record

    _record_factory._groww_request_id_wrapped = True
    logging.setLogRecordFactory(_record_factory)

logger = logging.getLogger(__name__)

# Module-level thread pool — created once, reused across Lambda warm invocations.
# max_workers=5 balances parallelism against Lambda's single-vCPU constraint and
# avoids all threads piling up on the token-refresh lock simultaneously.
_executor = ThreadPoolExecutor(max_workers=5)

# ---------------------------------------------------------------------------
# Indian NSE trading holidays (update annually)
# ---------------------------------------------------------------------------
# Source: NSE circular — add/remove dates each year as published.
_NSE_HOLIDAYS_2026: set[date] = {
    date(2026, 1, 26),   # Republic Day
    date(2026, 3, 2),    # Mahashivratri
    date(2026, 3, 25),   # Holi
    date(2026, 4, 2),    # Ram Navami
    date(2026, 4, 3),    # Good Friday
    date(2026, 4, 14),   # Dr. Ambedkar Jayanti
    date(2026, 5, 1),    # Maharashtra Day
    date(2026, 8, 15),   # Independence Day
    date(2026, 10, 2),   # Gandhi Jayanti
    date(2026, 10, 21),  # Diwali (Laxmi Pujan) — tentative
    date(2026, 10, 22),  # Diwali (Balipratipada) — tentative
    date(2026, 11, 4),   # Guru Nanak Jayanti — tentative
    date(2026, 12, 25),  # Christmas
}

_NSE_HOLIDAYS_2025: set[date] = {
    date(2025, 1, 26),
    date(2025, 2, 26),
    date(2025, 3, 14),
    date(2025, 3, 31),
    date(2025, 4, 10),
    date(2025, 4, 14),
    date(2025, 4, 18),
    date(2025, 5, 1),
    date(2025, 8, 15),
    date(2025, 10, 2),
    date(2025, 10, 20),
    date(2025, 10, 21),
    date(2025, 11, 5),
    date(2025, 12, 25),
}

_ALL_NSE_HOLIDAYS: set[date] = _NSE_HOLIDAYS_2025 | _NSE_HOLIDAYS_2026

# ---------------------------------------------------------------------------
# Ticker validation
# ---------------------------------------------------------------------------
_TICKER_RE = re.compile(r"^[A-Z0-9\-&]{1,20}$")


def normalise_ticker(ticker: str) -> str:
    """Strip leading 'NSE:' prefix and validate the ticker format."""
    clean = ticker.removeprefix("NSE:").strip().upper()
    if not _TICKER_RE.match(clean):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid ticker format: '{ticker}'. Must be 1–20 uppercase letters/digits/hyphens.",
        )
    return clean


# ---------------------------------------------------------------------------
# Tick-size adjustment
# ---------------------------------------------------------------------------
def adjust_to_tick_size(price: float, round_down: bool = False) -> float:
    """Adjust price to the nearest valid NSE tick size.

    Args:
        price: The price to adjust.
        round_down: If True, floor to the nearest valid tick (conservative for stop-loss).
    """
    if price < 250:
        tick_size = 0.01
    elif price <= 1000:
        tick_size = 0.05
    elif price <= 5000:
        tick_size = 0.10
    elif price <= 10000:
        tick_size = 0.50
    elif price <= 20000:
        tick_size = 1.00
    else:
        tick_size = 5.00

    if round_down:
        adjusted = math.floor(price / tick_size) * tick_size
    else:
        adjusted = round(price / tick_size) * tick_size

    if tick_size < 1:
        decimal_places = len(str(tick_size).split(".")[-1]) if "." in str(tick_size) else 0
        adjusted = round(adjusted, decimal_places)

    return adjusted


# ---------------------------------------------------------------------------
# Service-level API key authentication
# ---------------------------------------------------------------------------
_SERVICE_API_KEY = os.getenv("SERVICE_API_KEY", "")

_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def verify_service_api_key(api_key: Optional[str] = Security(_api_key_header)):
    """FastAPI dependency that validates the X-API-Key header."""
    if not _SERVICE_API_KEY:
        # Warn loudly — every request gets through unauthenticated
        logger.warning(
            "SERVICE_API_KEY is not set. All endpoints are publicly accessible! "
            "Set SERVICE_API_KEY in your environment to enable authentication."
        )
        return
    if api_key != _SERVICE_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing X-API-Key header.",
        )


# ---------------------------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Groww Trading API",
    version="2.1.0",
    description="Enhanced Trading API with portfolio management",
    dependencies=[Security(verify_service_api_key)],
)


# ---------------------------------------------------------------------------
# Request/response logging middleware with correlation ID
# ---------------------------------------------------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    # Set the ContextVar so ALL log lines emitted during this request
    # (including from helpers and thread-pool workers) carry the same ID.
    token = _request_id_var.set(request_id)
    request.state.request_id = request_id

    start = time.monotonic()
    logger.info("%s %s", request.method, request.url.path)

    try:
        response = await call_next(request)
        elapsed_ms = (time.monotonic() - start) * 1000
        logger.info(
            "%s %s → %d (%.1f ms)",
            request.method,
            request.url.path,
            response.status_code,
            elapsed_ms,
        )
        response.headers["X-Request-ID"] = request_id
        return response
    finally:
        _request_id_var.reset(token)


# ---------------------------------------------------------------------------
# GrowwState — token management
# ---------------------------------------------------------------------------
class GrowwState:
    def __init__(self):
        load_dotenv()
        try:
            self.api_key = os.environ["API_KEY"]
            self.totp_secret = os.environ["TOTP_SECRET"]
            self.push_token = os.environ["PUSH_TOKEN"]
        except KeyError as e:
            logger.error("Missing required environment variable: %s", e)
            raise SystemExit(1)

        # Log only a static confirmation — never log actual key material
        logger.info("API_KEY loaded successfully.")
        logger.info("TOTP_SECRET loaded.")
        logger.info("PUSH_TOKEN loaded.")

        if not _SERVICE_API_KEY:
            logger.warning(
                "SERVICE_API_KEY is not configured. "
                "All API endpoints are publicly accessible!"
            )

        self.totp_gen = pyotp.TOTP(self.totp_secret)
        self._access_token: Optional[str] = None
        # /tmp is the only writable directory on Lambda
        self.cache_file = "/tmp/.groww_cache.json"
        # RLock (re-entrant) prevents deadlock if refresh_token is called
        # from within a call stack that already holds the lock.
        self._lock = threading.RLock()
        self._auth_cooldown_until: float = 0.0
        self._last_auth_error: Optional[str] = None
        self.auth_cooldown_seconds = int(
            os.getenv("GROWW_AUTH_COOLDOWN_SECONDS", "300") or 300
        )

        self._load_cache()

    # ------------------------------------------------------------------
    # Token property
    # ------------------------------------------------------------------
    @property
    def access_token(self) -> str:
        if self._access_token is None:
            self.refresh_token()
        return self._access_token  # type: ignore[return-value]

    @access_token.setter
    def access_token(self, value: str):
        self._access_token = value

    # ------------------------------------------------------------------
    # Cache helpers
    # ------------------------------------------------------------------
    def _load_cache(self):
        import json

        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r") as f:
                    cache = json.load(f)
                    self._access_token = cache.get("access_token")
                    logger.info("Loaded access token from cache.")
            except Exception as e:
                logger.warning("Failed to load token from cache: %s", e)

    def _save_cache(self):
        import json

        try:
            with open(self.cache_file, "w") as f:
                json.dump(
                    {
                        "access_token": self._access_token,
                        "updated_at": _utcnow(),
                    },
                    f,
                )
            # Restrict permissions so only the owner can read the token file
            try:
                os.chmod(self.cache_file, 0o600)
            except OSError:
                pass  # Windows — chmod is a no-op; acceptable
            logger.info("Saved access token to cache.")
        except Exception as e:
            logger.warning("Failed to save token to cache: %s", e)

    # ------------------------------------------------------------------
    # Token refresh
    # ------------------------------------------------------------------
    def refresh_token(self, current_token: Optional[str] = None) -> str:
        with self._lock:
            # Another thread may have already refreshed it
            if current_token and self._access_token != current_token:
                logger.info("Access token already refreshed by another thread.")
                return self._access_token  # type: ignore[return-value]

            now = time.time()
            if self._auth_cooldown_until and now < self._auth_cooldown_until:
                remaining = max(1, int(math.ceil(self._auth_cooldown_until - now)))
                raise HTTPException(
                    status_code=429,
                    detail=f"Groww auth cooldown active. Retry in {remaining}s.",
                )

            logger.info("Refreshing access token…")
            totp = self.totp_gen.now()
            try:
                self._access_token = GrowwAPI.get_access_token(self.api_key, totp)
                logger.info("Access token refreshed successfully.")
                self._auth_cooldown_until = 0.0
                self._last_auth_error = None
                self._save_cache()
            except GrowwAPIRateLimitException:
                logger.error("Groww API rate limit exceeded during token refresh.")
                self._auth_cooldown_until = time.time() + self.auth_cooldown_seconds
                self._last_auth_error = "Groww API rate limit exceeded"
                raise HTTPException(
                    status_code=429,
                    detail="Groww API rate limit exceeded. Please wait.",
                )
            except Exception as e:
                logger.error("Token refresh failed: %s", e)
                self._auth_cooldown_until = time.time() + min(60, self.auth_cooldown_seconds)
                self._last_auth_error = str(e)
                raise
            return self._access_token  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Auth-failure detection
# ---------------------------------------------------------------------------
def _is_auth_failure(exc: Exception) -> bool:
    text = str(exc or "").lower()
    return (
        "authentication failed" in text
        or "expired or is invalid" in text
        or ("token" in text and "inv
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [3/3] Repository: alphatrade (`VAULT_IN-QUANT-025_algo2t__alphatrade`)
- **Full Name**: `IN-QUANT-025_algo2t__alphatrade`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Python APIs for SAS Online Alpha Trade Web Platform

# MAJOR CHANGES : NEW VERSION 1.0.0

## API endpoints are changed to match the new ones, bugs expected

1. Removed check for enabled exchanges, you can now download or search symbols from MCX as well if it is not enabled
2. TOTP SECRET or TOTP both can be given as argument while creating AlphaTrade object (if it is 6 digits it will conside TOTP else TOTP SECRET)
3. Added new search function to search scrips which will return json for found scrips, you need to process it further
4. More functions to come.
5. Check whether streaming websocket is working or not
6. The `examples` folder is removed and examples are renamed and kept in root directory for ease of development

# STEPS to work

1. Clone the repo locally - `git clone https://github.com/algo2t/alphatrade.git` 
2. Create a virtualenv - `python -m pip install virtualenv` and then `python -m virtualenv venv` and activate the `venv` environment.
3. Install dev-requirement.txt - `python -m pip install -r dev-requirements.txt` - this is to ensure `setuptools==57.5.0` is installed. There is a bug with `protlib`, target is to get reed of `protlib` in future
4. Install requirement.txt - `python -m pip install -r requirement.txt`
5. Create the `config.py` file in root of cloned repo with `login_id`, `password` and `TOTP` SECRET, you can add the `access_token.txt` if you want to use existing `access_token`.
6. Try the examples `python zlogin_example.py`, `python zexample_sas_login.py`, `python zhistorical_data.py` and `python zstreaming_data.py`
7. Expecting issues with the streaming data !!! :P


# NOTE:: This is Unofficial python module, don't ask SAS support team for help, use it AS-IS

The Python APIs for communicating with the SAS Online Alpha Trade Web Platform.

Alpha Trade Python library provides an easy to use python wrapper over the HTTPS APIs.

The HTTP calls have been converted to methods and JSON responses are wrapped into Python-compatible objects.

Websocket connections are handled automatically within the library.

This work is completely based on Python SDK / APIs for [AliceBlueOnline](https://github.com/krishnavelu/alice_blue.git).  
Thanks to [krishnavelu](https://github.com/krishnavelu/).  

- **Author: [algo2t](https://github.com/algo2t/)**
- **Github Repository: [alphatrade](https://github.com/algo2t/alphatrade.git)**

## Installation

This module is installed via pip:

```
pip install git+https://github.com/algo2t/alphatrade.git
```

It can also be installed from [pypi](https://pypi.org/project/alphatrade/1.0.0/)  

```
pip install alphatrade
```

To force upgrade existing installations:

```
pip uninstall alphatrade
pip --no-cache-dir install --upgrade alphatrade
```

### Prerequisites

Python 3.x

## Make sure to install `setuptools==57.5.0` for `protlib==1.5.0` to work properly

Also, you need the following modules:

- `setuptools==57.5.0`
- `protlib==1.5.0`
- `websocket-client==1.6.1`
- `requests==2.31.0`
- `pandas==2.0.3`
- `pyotp==2.8.0`

The modules can also be installed using `pip`

## Examples - Start Here - Important 

Please clone this repository and check the examples folder to get started.  
Check [here](https://algo2t.github.io/alphatrade/#working-with-examples)

## Getting started with API

### Overview

There is only one class in the whole library: `AlphaTrade`. When the `AlphaTrade` object is created an access token from the SAS Online alpha trade server is stored in text file `access_token.txt` in the same directory. An access token is valid for 24 hours. See the examples folder with `config.py` file to see how to store your credentials.
With an access token, you can instantiate an AlphaTrade object again. Ideally you only need to create an access_token once every day.

### REST Documentation

The original REST API that this SDK is based on is available online.
[Tradelabs API documentation](http://primusapi.tradelab.in/webapi/)

## Using the API

### Logging

The whole library is equipped with python‘s `logging` module for debugging. If more debug information is needed, enable logging using the following code.

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Get an access token

1. Import alphatrade

```python
from alphatrade import *
```

2. Create `config.py` file  
Always keep credentials in a separate file
```python
login_id = "XXXXX"
password = "XXXXXXXX"
Totp = 'XXXXXXXXXXXXXXXX'

try:
    access_token = open('access_token.txt', 'r').read().rstrip()
except Exception as e:
    print('Exception occurred :: {}'.format(e))
    access_token = None
```

3. Import the config
```python
import config
```

### Create AlphaTrade Object

1. Create `AlphaTrade` object with your `login_id`, `password`, `TOTP` / `TOTP_SECRET` and/or `access_token`.

Use `config` object to get `login_id`, `password`, `TOTP` and `access_token`.  

```python
from alphatrade import AlphaTrade
import config
import pyotp
Totp = config.Totp
pin = pyotp.TOTP(Totp).now()
totp = f"{int(pin):06d}" if len(pin) <=5 else pin   
sas = AlphaTrade(login_id=config.login_id, password=config.password, twofa=totp, access_token=config.access_token)

```

## OR

```python
## filename config.py

login_id = "RR24XX"
password = "SuperSecretPassword!!!"
TOTP_SECRET = 'YOURTOTPSECRETEXTERNALAUTH'

try:
    access_token = open('access_token.txt', 'r').read().rstrip()
except Exception as e:
    print(f'Exception occurred :: {e}')
    access_token = None

```


```python
from alphatrade import AlphaTrade
import config
import pyotp
sas = AlphaTrade(login_id=config.login_id, password=config.password, twofa=config.TOTP_SECRET, access_token=config.access_token)

```


2. You can run commands here to check your connectivity

```python
print(sas.get_balance()) # get balance / margin limits
print(sas.get_profile()) # get profile
print(sas.get_daywise_positions()) # get daywise positions
print(sas.get_netwise_positions()) # get netwise positions
print(sas.get_holding_positions()) # get holding positions
```

### Get master contracts

Getting master contracts allow you to search for instruments by symbol name and place orders.
Master contracts are stored as an OrderedDict by token number and by symbol name. Whenever you get a trade update, order update, or quote update, the library will check if master contracts are loaded. If they are, it will attach the instrument object directly to the update. By default all master contracts of all enabled exchanges in your personal profile will be downloaded. i.e. If your profile contains the following as enabled exchanges `['NSE', 'BSE', 'CDS', 'MCX', NFO']` all contract notes of all exchanges will be downloaded by default. If you feel it takes too much time to download all exchange, or if you don‘t need all exchanges to be downloaded, you can specify which exchange to download contract notes while creating the AlphaTrade object.

```python
sas = AlphaTrade(login_id=config.login_id, password=config.password, twofa=totp, access_token=config.access_token, master_contracts_to_download=['NSE', 'BSE'])
```

This will reduce a few milliseconds in object creation time of AlphaTrade object.

### Get tradable instruments

Symbols can be retrieved in multiple ways. Once you have the master contract loaded for an exchange, you can get an instrument in many ways.

Get a single instrument by it‘s name:

```python
tatasteel_nse_eq = sas.get_instrument_by_symbol('NSE', 'TATASTEEL')
reliance_nse_eq = sas.get_instrument_by_symbol('NSE', 'RELIANCE')
ongc_bse_eq = sas.get_instrument_by_symbol('BSE', 'ONGC')
india_vix_nse_index = sas.get_instrument_by_symbol('NSE', 'India VIX')
sensex_nse_index = sas.get_instrument_by_symbol('BSE', 'SENSEX')
```

Get a single instrument by it‘s token number (generally useful only for BSE Equities):

```python
ongc_bse_eq = sas.get_instrument_by_token('BSE', 500312)
reliance_bse_eq = sas.get_instrument_by_token('BSE', 500325)
acc_nse_eq = sas.get_instrument_by_token('NSE', 22)
```

Get FNO instruments easily by mentioning expiry, strike & call or put.

```python
bn_fut = sas.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=True, strike=None, is_call = False)
bn_call = sas.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=False, strike=30000, is_call = True)
bn_put = sas.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=False, strike=30000, is_call = False)
```

### Search for symbols

Search for multiple instruments by matching the name. This works case insensitive and returns all instrument which has the name in its symbol.

```python
all_sensex_scrips = sas.search_instruments('BSE', 'sEnSeX')
print(all_sensex_scrips)
```

The above code results multiple symbol which has ‘sensex’ in its symbol.

```
[Instrument(exchange='BSE', token=1, symbol='SENSEX', name='SENSEX', expiry=None, lot_size=None), Instrument(exchange='BSE', token=540154, symbol='IDFSENSEXE B', name='IDFC Mutual Fund', expiry=None, lot_size=None), Instrument(exchange='BSE', token=532985, symbol='KTKSENSEX B', name='KOTAK MAHINDRA MUTUAL FUND', expiry=None, lot_size=None), Instrument(exchange='BSE', token=538683, symbol='NETFSENSEX B', name='NIPPON INDIA ETF SENSEX', expiry=None, lot_size=None), Instrument(exchange='BSE', token=535276, symbol='SBISENSEX B', name='SBI MUTUAL FUND - SBI ETF SENS', expiry=None, lot_size=None)]
```

Search for multiple instruments by matching multiple names

```python
multiple_underlying = ['BANKNIFTY','NIFTY','INFY','BHEL']
all_scripts = sas.search_instruments('NFO', multiple_underlying)
```

#### Instrument object

Instruments are represented by instrument objects. These are named-tuples that are created while getting the master contracts. They are used when placing an order and searching for an instrument. The structure of an instrument tuple is as follows:

```python
Instrument = namedtuple('Instrument', ['exchange', 'token', 'symbol',
                                      'name', 'expiry', 'lot_size'])
```

All instruments have the fields mentioned above. Wherever a field is not applicable for an instrument (for example, equity instruments don‘t have strike prices), that value will be `None`

### Quote update

Once you have master contracts loaded, you can easily subscribe to quote updates.

#### Four types of feed data are available

You can subscribe any one type of quote update for a given scrip. Using the `LiveFeedType` enum, you can specify what type of live feed you need.

- `LiveFeedType.MARKET_DATA`
- `LiveFeedType.COMPACT`
- `LiveFeedType.SNAPQUOTE`
- `LiveFeedType.FULL_SNAPQUOTE`

Please refer to the original documentation [here](http://primusapi.tradelab.in/webapi/) for more details of different types of quote update.

#### Subscribe to a live feed

```python
sas.subscribe(sas.get_instrument_by_symbol('NSE', 'TATASTEEL'), LiveFeedType.MARKET_DATA)
sas.subscribe(sas.get_instrument_by_symbol('BSE', 'RELIANCE'), LiveFeedType.COMPACT)
```

Subscribe to multiple instruments in a single call. Give an array of instruments to be subscribed.

```python
sas.subscribe([sas.get_instrument_by_symbol('NSE', 'TATASTEEL'), sas.get_instrument_by_symbol('NSE', 'ACC')], LiveFeedType.MARKET_DATA)
```

Note: There is a limit of 250 scrips that can be subscribed on total. Beyond this point the server may disconnect web-socket connection.

Start getting live feed via socket

```python
socket_opened = False
def event_handler_quote_update(message):
    print(f"quote update {message}")

def open_callback():
    global socket_opened
    socket_opened = True

sas.start_websocket(subscribe_callback=event_handler_quote_update,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while(socket_opened==False):
    pass
sas.subscribe(sas.get_instrument_by_symbol('NSE', 'ONGC'), LiveFeedType.MARKET_DATA)
sleep(10)
```

#### Unsubscribe to a live feed

Unsubscribe to an existing live feed

```python
sas.unsubscribe(sas.get_instrument_by_symbol('NSE', 'TATASTEEL'), LiveFeedType.MARKET_DATA)
sas.unsubscribe(sas.get_instrument_by_symbol('BSE', 'RELIANCE'), LiveFeedType.COMPACT)
```

Unsubscribe to multiple instruments in a single call. Give an array of instruments to be unsubscribed.

```python
sas.unsubscribe([sas.get_instrument_by_symbol('NSE', 'TATASTEEL'), sas.get_instrument_by_symbol('NSE', 'ACC')], LiveFeedType.MARKET_DATA)
```

#### Get All Subscribed Symbols

```python
sas.get_all_subscriptions() # All
```

### Market Status messages & Exchange messages.

Subscribe to market status messages

```python
sas.subscribe_market_status_messages()
```

Getting market status messages.

```python
print(sas.get_market_status_messages())
```

Example result of `get_market_status_messages()`

```
[{'exchange': 'NSE', 'length_of_market_type': 6, 'market_type': b'NORMAL', 'length_of_status': 31, 'status': b'The Closing Session has closed.'}, {'exchange': 'NFO', 'length_of_market_type': 6, 'market_type': b'NORMAL', 'length_of_status': 45, 'status': b'The Normal market has closed for 22 MAY 2020.'}, {'exchange': 'CDS', 'length_of_market_type': 6, 'market_type': b'NORMAL', 'length_of_status': 45, 'status': b'The Normal market has closed for 22 MAY 2020.'}, {'exchange': 'BSE', 'length_of_market_type': 13, 'market_type': b'OTHER SESSION', 'length_of_status': 0, 'status': b''}]
```

Note: As per `alice blue` [documentation](http://antplus.aliceblueonline.com/#market-status) all market status messages should be having a timestamp. But in actual the server doesn‘t send timestamp, so the library is unable to get timestamp for now.

Subscribe to exchange messages

```python
sas.subscribe_exchange_messages()
```

Getting market status messages.

```python
print(sas.get_exchange_messages())
```

Example result of `get_exchange_messages()`

```
[{'exchange': 'NSE', 'length': 32, 'message': b'DS : Bulk upload can be started.', 'exchange_time_stamp': 1590148595}, {'exchange': 'NFO', 'length': 200, 'message': b'MARKET WIDE LIMIT FOR VEDL IS 183919959. OPEN POSITIONS IN VEDL HAVE REACHED 84 PERCENT OF THE MARKET WIDE LIMIT.                                                                                       ', 'exchange_time_stamp': 1590146132}, {'exchange': 'CDS', 'length': 54, 'message': b'DS : Regular segment Bhav copy broadcast successfully.', 'exchange_time_stamp': 1590148932}, {'exchange': 'MCX', 'length': 7, 'message': b'.......', 'exchange_time_stamp': 1590196159}]
```

#### Market Status messages & Exchange messages through callbacks

```python
socket_opened = False
def market_status_messages(message):
    print(f"market status messages {message}")

def exchange_messages(message):
    print(f"exchange messages {message}")

def open_callback():
    global socket_opened
    socket_opened = True

sas.start_websocket(market_status_messages_callback=market_status_messages,
					  exchange_messages_callback=exchange_messages,
                      socket_open_callback=open_callback,
                      run_in_background=True)
while(socket_opened==False):
    pass
sas.subscribe_market_status_messages()
sas.subscribe_exchange_messages()
sleep(10)
```

### Place an order

Place limit, market, SL, SL-M, AMO, BO, CO orders

```python
print (sas.get_profile())

# TransactionType.Buy, OrderType.Market, ProductType.Delivery

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.Market,
                     product_type = ProductType.Delivery,
                     price = 0.0,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
   )

# TransactionType.Buy, OrderType.Market, ProductType.Intraday

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%2%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.Market,
                     product_type = ProductType.Intraday,
                     price = 0.0,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)

# TransactionType.Buy, OrderType.Market, ProductType.CoverOrder

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%3%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.Market,
                     product_type = ProductType.CoverOrder,
                     price = 0.0,
                     trigger_price = 7.5, # trigger_price Here the trigger_price is taken as stop loss (provide stop loss in actual amount)
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)


# TransactionType.Buy, OrderType.Limit, ProductType.BracketOrder
# OCO Order can't be of type market

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%4%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.Limit,
                     product_type = ProductType.BracketOrder,
                     price = 8.0,
                     trigger_price = None,
                     stop_loss = 6.0,
                     square_off = 10.0,
                     trailing_sl = None,
                     is_amo = False)
)

# TransactionType.Buy, OrderType.Limit, ProductType.Intraday

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%5%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.Limit,
                     product_type = ProductType.Intraday,
                     price = 8.0,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)


# TransactionType.Buy, OrderType.Limit, ProductType.CoverOrder

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%6%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.Limit,
                     product_type = ProductType.CoverOrder,
                     price = 7.0,
                     trigger_price = 6.5, # trigger_price Here the trigger_price is taken as stop loss (provide stop loss in actual amount)
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)

###############################

# TransactionType.Buy, OrderType.StopLossMarket, ProductType.Delivery

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%7%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.StopLossMarket,
                     product_type = ProductType.Delivery,
                     price = 0.0,
                     trigger_price = 8.0,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)


# TransactionType.Buy, OrderType.StopLossMarket, ProductType.Intraday

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%8%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.StopLossMarket,
                     product_type = ProductType.Intraday,
                     price = 0.0,
                     trigger_price = 8.0,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)



# TransactionType.Buy, OrderType.StopLossMarket, ProductType.CoverOrder
# CO order is of type Limit and And Market Only

# TransactionType.Buy, OrderType.StopLossMarket, ProductType.BO
# BO order is of type Limit and And Market Only

###################################

# TransactionType.Buy, OrderType.StopLossLimit, ProductType.Delivery

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%9%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.StopLossMarket,
                     product_type = ProductType.Delivery,
                     price = 8.0,
                     trigger_price = 8.0,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)


# TransactionType.Buy, OrderType.StopLossLimit, ProductType.Intraday

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%10%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.StopLossLimit,
                     product_type = ProductType.Intraday,
                     price = 8.0,
                     trigger_price = 8.0,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False)
)



# TransactionType.Buy, OrderType.StopLossLimit, ProductType.CoverOrder
# CO order is of type Limit and And Market Only


# TransactionType.Buy, OrderType.StopLossLimit, ProductType.BracketOrder

print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%11%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(
   sas.place_order(transaction_type = TransactionType.Buy,
                     instrument = sas.get_instrument_by_symbol('NSE', 'INFY'),
                     quantity = 1,
                     order_type = OrderType.StopLossLimit,
                     product_type = ProductType.BracketOrder,
                     price = 8.0,
                     trigger_price = 8.0,
                     stop_loss = 1.0,
                     square_off = 1.0,
                     trailing_sl = 20,
                     is_amo = False)
)
```

### Place basket order

Basket order is used to buy or sell group of securities simultaneously.

```python
order1 = {  "instrument"        : sas.get_instrument_by_symbol('NSE', 'INFY'),
            "order_type"        : OrderType.Market,
            "quantity"          : 1,
            "transaction_type"  : TransactionType.Buy,
            "product_type"      : ProductType.Delivery}
order2 = {  "instrument"        : sas.get_instrument_by_symbol('NSE', 'SBIN'),
            "order_type"        : OrderType.Limit,
            "quantity"          : 2,
            "price"             : 280.0,
            "transaction_type"  : TransactionType.Sell,
            "product_type"      : ProductType.Intraday}
order = [order1, order2]
print(sas.place_basket_order(orders))
```

### Cancel an order

```python
sas.cancel_order('170713000075481') #Cancel an open order
```

### Getting order history and trade details

#### Get order history of a particular order

```python
print(sas.get_order_history('170713000075481'))
```

#### Get order history of all orders.

```python
print(sas.get_order_history())
```

#### Get trade book

```python
print(sas.get_trade_book())
```

#### Get historical candles data

This will provide historical data but **not for current day**.  
This returns a `pandas` `DataFrame` object which be used with `pandas_ta` to get various indicators values.  

```python
from datetime import datetime
print(sas.get_historical_candles('MCX', 'NATURALGAS NOV FUT', datetime(2020, 10, 19), datetime.now() ,interval=30))
```

Output 

```console
Instrument(exchange='MCX', token=224365, symbol='NATURALGAS NOV FUT', name='', expiry=datetime.date(202
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `.vscode/settings.json`
```python
{
    "python.linting.pylintEnabled": true,
    "python.linting.banditEnabled": false,
    "python.linting.enabled": true,
    "cSpell.words": [
        "TOTP",
        "twofa"
    ],
    "python.linting.flake8Enabled": false
}
```

#### File: `alphatrade/__init__.py`
```python
from __future__ import unicode_literals, absolute_import

from .alphatrade import AlphaTrade, TransactionType, OrderType, ProductType, LiveFeedType, Instrument
from alphatrade import exceptions

__all__ = ['AlphaTrade', 'TransactionType', 'OrderType',
           'ProductType', 'LiveFeedType', 'Instrument', 'exceptions']
```

#### File: `zlogin_example.py`
```python
from alphatrade import AlphaTrade
import config
import pyotp
Totp = config.TOTP
pin = pyotp.TOTP(Totp).now()
totp = f"{int(pin):06d}" if len(pin) <= 5 else pin
print(totp)
sas = AlphaTrade(login_id=config.login_id, password=config.password,
                 twofa=totp, access_token=config.access_token, master_contracts_to_download=['MCX', 'NFO'])
# print(sas.get_profile())
print(sas.get_balance())
print(sas.get_trade_book())
# print(sas.orders('complete'))
# print(sas.orders('pending'))
print(sas.orders())
# print(sas.get_daywise_positions())
# print(sas.get_holding_positions())
# print(sas.get_netwise_positions())
print(sas.search('Nifty Bank','NSE'))
print(sas.search('TCS','BSE'))
print(sas.search('TCS', 'NFO'))
print(sas.search('TCS-EQ'))
print(sas.positions())
print(sas.positions('historical'))

print(sas.get_exchanges())
print(sas.get_master_contract('MCX'))
```

#### File: `zexample_sas_login.py`
```python
import datetime
import json
from time import sleep

# pip install https://github.com/algo2t/alphatrade

from alphatrade import AlphaTrade, LiveFeedType

import config
# NOTE create a config.py file in the same directory as sas_login_eg.py file
# Contents of the config.py must be as below, config.py is used for storing credentials
#### config.py START ####
# login_id = "RR"
# password = "SAS@131"
# TOTP = "EXAMPLETOTPSECRET"

# try:
#     access_token = open('zaccess_token.txt', 'r').read().rstrip()
# except Exception as e:
#     print('Exception occurred :: {}'.format(e))
#     access_token = None
#### config.py END ####

sas = AlphaTrade(login_id=config.login_id, password=config.password, twofa=config.TOTP)

# NOTE access_token can be supplied if already available
# sas = AlphaTrade(login_id=config.login_id, password=config.password,
#                  twofa=config.twofa, access_token=config.access_token)

# NOTE access_token can be supplied if already available and master_contracts to download
# sas = AlphaTrade(login_id=config.login_id, password=config.password,
#                  twofa=config.twofa, access_token=config.access_token, master_contracts_to_download=['CDS'])


print(sas.get_profile())
usd_inr = sas.get_instrument_by_symbol('NSE', 'PAYTM')
print(usd_inr)
print(sas.get_balance())
```

#### File: `setup.py`
```python
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='alphatrade',
    packages=setuptools.find_packages(),
    version='1.0.0',
    include_package_data=True,
    description='Python APIs for SAS Online Alpha Trade Web Platform',
    long_description=long_description,
    long_description_content_type='text/markdown',  author='Algo 2 Trade',
    author_email='help@algo2.trade',
    url='https://github.com/algo2t/alphatrade',
    install_requires=['setuptools==70.0.0','requests', 'websocket_client', 'protlib', 'pandas','pyotp'],
    keywords=['alphatrade', 'alpha-trade', 'sasonline',
              'python', 'sdk', 'trading', 'stock markets'],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries'
    ],
)
```

#### File: `zhistorical_data.py`
```python
import json
from time import sleep
from datetime import datetime, timedelta

# pip install https://github.com/algo2t/alphatrade

from alphatrade import AlphaTrade

import config as config

sas = AlphaTrade(login_id=config.login_id,
                 password=config.password, twofa=config.TOTP)

usd_inr = sas.get_instrument_by_symbol('CDS', 'USDINR SEP FUT')
print(usd_inr)
# print(sas.get_balance())
start_time = datetime(2022, 1, 9, 9, 15, 0)
end_time = datetime.now()

# df = sas.get_historical_candles(
#     'MCX', 'NATURALGAS MAY FUT', start_time, end_time, 5)
# print(df)
# end_time = start_time + timedelta(days=5)
# df = sas.get_historical_candles(
#     'MCX', 'NATURALGAS APR FUT', start_time, end_time, 15)
# print(df)

# # Get Intraday Candles data based on interval - default 5 minute
# df = sas.get_intraday_candles('MCX', 'NATURALGAS MAY FUT')
# print(df)
df = sas.get_intraday_candles('MCX', 'NATURALGAS AUG FUT', 15)
print(df)

# # Get Historical candles data
# print(sas.get_historical_candles('MCX', 'NATURALGAS APR FUT',
#                                  datetime(2020, 10, 19), datetime.now(), interval=30))

# # Get Historical candle for Nifty Bank and India VIX
# india_vix_nse_index = sas.get_instrument_by_symbol('NSE', 'India VIX')
# print(sas.get_historical_candles(india_vix_nse_index.exchange,
#                                  india_vix_nse_index.symbol, datetime(2020, 11, 30), datetime.now(), interval=30, is_index=True))

nifty_bank_nse_index = sas.get_instrument_by_symbol('NSE', 'Nifty Bank')
# print(nifty_bank_nse_index)
print(sas.history(nifty_bank_nse_index, datetime(2022, 2, 2, 9, 15, 0), datetime.now(), interval=30, is_index=True))
```


==================================================
