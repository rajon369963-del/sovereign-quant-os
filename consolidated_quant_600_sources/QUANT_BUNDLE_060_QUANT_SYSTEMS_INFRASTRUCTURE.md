# ⚡ [QUANT-SOURCE-060] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_060_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: alice_blue (`VAULT_IN-QUANT-013_krishnavelu__alice_blue`)
- **Full Name**: `IN-QUANT-013_krishnavelu__alice_blue`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Official Python SDK for Alice Blue API

The Official Python library for communicating with the Alice Blue APIs.

Alice Blue Python library provides an easy to use wrapper over the HTTPS APIs.

The HTTP calls have been converted to methods and JSON responses are wrapped into Python-compatible objects.

Websocket connections are handled automatically within the library.

* __Author: [krishnavelu](https://github.com/krishnavelu/)__
* [Unofficed](https://www.unofficed.com/) is strategic partner of Alice Blue responsible for this git.
* Alice Blue API trading is free for [Unofficed](https://www.unofficed.com/) members. Follow [this](https://unofficed.com/alice-blue/) to get API free.

## Installation

This module is installed via pip:

```
pip install alice_blue
```

To force upgrade existing installations:
```
pip uninstall alice_blue
pip --no-cache-dir install --upgrade alice_blue
```

## Getting started with API

### Overview
There is only one class in the whole library: `AliceBlue`. The `login_and_get_sessionID()` static method is used to retrieve session ID from alice blue server. A session ID is valid for 24 hours.
With session ID, you can instantiate an AliceBlue object. Ideally you only need to create a session ID once every day. Once the session ID is created new, it'll be stored in a temporary location. Next time, the same session ID will be used.

### REST Documentation
The original REST API documentation is available [here](https://v2api.aliceblueonline.com/).

## Using the API

### Logging
The whole library is equipped with python's `logging` module for debugging. If more debug information is needed, enable logging using the following code.

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Geting API Id and API secret
api_secret is unique for each and every account. You need to enable api trading and get api_secret from alice blue.
1. Login to [developer console](http://developers.aliceblueonline.com).
1. Click on 'Create New App'.
1. Enter 'App Name' as you like. Enter 'Redirect URL' and 'Post Back URL' as `https://ant.aliceblueonline.com/plugin/callback`.
1. Click on 'Save'.
1. Copy the 'App Code' and 'App Secret'. You will need these to generate a session ID.

### Getting an session ID
1. Import alice_blue
```python
from alice_blue import *
```

2. Create `session_id` using `login_and_get_sessionID()` function  with your `username`, `password`, `2FA (2fa is now year of birth)`, `app_id` and `api_secret`.
```python
session_id = AliceBlue.login_and_get_sessionID(   username    = "username", 
                                                    password    = "password", 
                                                    twoFA       = "1993",
                                                    app_id      = "app_id",
                                                    api_secret  = "api_secret")
```

### Problem getting access token
If you are facing problem getting access token, make sure the following are correct.
1. username.
1. password.
1. 2FA.
1. api secret.
1. app id.

Even after verifying all these, if you are facing problem, contact alice customer care. They should enable the API access in their end. Don't create a new issue in this library for OAuth Error.

### Create AliceBlue Object
Once you have your `session_id`, you can create an AliceBlue object with your `session_id` and `username`.
```python
alice = AliceBlue(username = "username", session_id = session_id)
```

You can run these commands to check your newly created alice blue object.
1. [Get Balance](#get-balance)
1. [Get Profile](#get-profile)
1. [Get Daywise positions](#get-daywise-positions)
1. [Get Netwise positions](#get-netwise-positions)
1. [Get Holding positions](#get-holding-positions)

### Get Balance
Code:
```python
print(alice.get_balance()) # get balance / margin limits
```
Sample response
```
[{'symbol': 'ALL', 'cncMarginUsed': '0', 'spanmargin': '159440.00', 'branchAdhoc': '0.000000', 'adhocMargin': '0.000000', 'payoutamount': '0.00', 'cdsSpreadBenefit': '0', 'adhocscripmargin': '0.00', 'exposuremargin': '7774.30', 'scripbasketmargin': '0.00', 'credits': '114028.29', 'segment': 'ALL', 'net': '95012.20', 'turnover': '0.00', 'grossexposurevalue': '0.00', 'mfssAmountUsed': '0.00', 'realizedMtomPrsnt': '-6075.80', 'product': 'ALL', 'stat': 'Ok', 'cncSellCrditPrsnt': '0', 'debits': '243846.09', 'varmargin': '0.00', 'multiplier': '10.00', 'elm': '0.00', 'mfamount': '0.00', 'cashmarginavailable': '119428.29', 'brokeragePrsnt': '355.990260', 'cncRealizedMtomPrsnt': '0', 'notionalCash': '0.000000', 'directcollateralvalue': '0.00', 'cncBrokeragePrsnt': '0', 'valueindelivery': '0', 'nfoSpreadBenefit': '0', 'losslimit': '0', 'subtotal': '243846.09', 'rmsPayInAmnt': '0', 'unrealizedMtomPrsnt': '-0.00', 'coverOrderMarginPrsnt': '0', 'exchange': 'ALL', 'category': 'ABFS-COMMON', 'collateralvalue': '0.00', 'rmsIpoAmnt': '0', 'cncUnrealizedMtomPrsnt': '0', 'premiumPrsnt': '0'}, {'symbol': 'ALL', 'cncMarginUsed': '0', 'spanmargin': '0.00', 'branchAdhoc': '0.000000', 'adhocMargin': '0.000000', 'payoutamount': '0.00', 'cdsSpreadBenefit': '0', 'adhocscripmargin': '0.00', 'exposuremargin': '0.00', 'scripbasketmargin': '0.00', 'credits': '0.00', 'segment': 'COM', 'net': '0.00', 'turnover': '0.00', 'grossexposurevalue': '0.00', 'mfssAmountUsed': '0.00', 'realizedMtomPrsnt': '-0.00', 'product': 'ALL', 'stat': 'Ok', 'cncSellCrditPrsnt': '0', 'debits': '0.00', 'varmargin': '0.00', 'multiplier': '1.00', 'elm': '0.00', 'mfamount': '0.00', 'cashmarginavailable': '0.00', 'brokeragePrsnt': '0', 'cncRealizedMtomPrsnt': '0', 'notionalCash': '0.000000', 'directcollateralvalue': '0.00', 'cncBrokeragePrsnt': '0', 'valueindelivery': '0', 'nfoSpreadBenefit': '0', 'losslimit': '0', 'subtotal': '0.00', 'rmsPayInAmnt': '0', 'unrealizedMtomPrsnt': '-0.00', 'coverOrderMarginPrsnt': '0', 'exchange': 'ALL', 'category': 'NO_VAL', 'collateralvalue': '0.00', 'rmsIpoAmnt': '0', 'cncUnrealizedMtomPrsnt': '0', 'premiumPrsnt': '0'}]
```

### Get Profile
Code
```python
print(alice.get_profile()) # get profile
```
Sample response
```
{'accountStatus': 'Activated', 'dpType': 'CDSL', 'accountId': 'SP220xx', 'sBrokerName': 'ALICEBLUE', 'product': ['NRML', 'MIS', 'CNC', 'CO', 'BO'], 'accountName': 'xxxx xxxx', 'cellAddr': 'xxxxxxxxxx', 'emailAddr': 'xxxxxx@xxx.com', 'exchEnabled': 'bcs_fo|mcx_fo|nse_cm|bse_cm|nse_fo'}
```

### Get Daywise Positions
Code
```python
print(alice.get_daywise_positions()) # get daywise positions
```
Sample response
```
[{'realisedprofitloss': '-7,217.50', 'Fillsellamt': '292,062.50', 'Netqty': '0', 'Symbol': 'EICHERMOT', 'Instname': 'NA', 'Expdate': 'NA', 'LTP': '3,355.10', 'Opttype': 'XX', 'BLQty': 1.0, 'Token': '910', 'Fillbuyamt': '299,280.00', 'Fillsellqty': '87', 'Tsym': 'EICHERMOT-EQ', 'sSqrflg': 'Y', 'unrealisedprofitloss': '0.00', 'Buyavgprc': '3,440.00', 'MtoM': '-7,217.50', 'stat': 'Ok', 's_NetQtyPosConv': 'N', 'Sqty': '87', 'Sellavgprc': '3,357.04', 'PriceDenomenator': '1', 'PriceNumerator': '1', 'actid': 'SP220xx', 'posflag': 'true', 'Pcode': 'MIS', 'Stikeprc': '0', 'Bqty': '87', 'BEP': '0.00', 'Exchange': 'NSE', 'Series': 'EQ', 'GeneralDenomenator': '1', 'Type': 'DAY1', 'Netamt': '-7,217.50', 'companyname': 'EICHER MOTORS LTD', 'Fillbuyqty': '87', 'GeneralNumerator': '1', 'Exchangeseg': 'nse_cm', 'discQty': '10'}, {'realisedprofitloss': '1,141.70', 'Fillsellamt': '298,216.70', 'Netqty': '0', 'Symbol': 'M&M', 'Instname': 'NA', 'Expdate': 'NA', 'LTP': '1,274.65', 'Opttype': 'XX', 'BLQty': 1.0, 'Token': '2031', 'Fillbuyamt': '297,075.00', 'Fillsellqty': '233', 'Tsym': 'M&M-EQ', 'sSqrflg': 'Y', 'unrealisedprofitloss': '0.00', 'Buyavgprc': '1,275.00', 'MtoM': '1,141.70', 'stat': 'Ok', 's_NetQtyPosConv': 'N', 'Sqty': '233', 'Sellavgprc': '1,279.90', 'PriceDenomenator': '1', 'PriceNumerator': '1', 'actid': 'SP220xx', 'posflag': 'true', 'Pcode': 'MIS', 'Stikeprc': '0', 'Bqty': '233', 'BEP': '0.00', 'Exchange': 'NSE', 'Series': 'EQ', 'GeneralDenomenator': '1', 'Type': 'DAY1', 'Netamt': '1,141.70', 'companyname': 'MAHINDRA & MAHINDRA LTD', 'Fillbuyqty': '233', 'GeneralNumerator': '1', 'Exchangeseg': 'nse_cm', 'discQty': '10'}]
```

### Get Netwise Positions
Code
```python
print(alice.get_netwise_positions()) # get netwise positions
```
Sample response
```
[{'Instname': 'NA', 'Expdate': 'NA', 'CFsellqty': '0', 'Opttype': 'XX', 'Token': '910', 'CFSellavgprc': '0.00', 'sSqrflg': 'Y', 'unrealisedprofitloss': '0.00', 's_NetQtyPosConv': 'N', 'FillbuyamtCF': '0.00', 'Sqty': '87', 'Sellavgprc': '3,357.04', 'actid': 'SP220xx', 'netbuyamt': '299,280.00', 'Pcode': 'MIS', 'Bqty': '87', 'NetBuyavgprc': '3440.0', 'Exchange': 'NSE', 'companyname': 'EICHER MOTORS LTD', 'netbuyqty': '87', 'realisedprofitloss': '-7,217.50', 'Fillsellamt': '292,062.50', 'Netqty': '0', 'Symbol': 'EICHERMOT', 'LTP': '3,355.10', 'BLQty': 1.0, 'Fillbuyamt': '299,280.00', 'Fillsellqty': '87', 'Tsym': 'EICHERMOT-EQ', 'CFbuyqty': '0', 'Buyavgprc': '3,440.00', 'netSellamt': '292,062.50', 'MtoM': '-7,217.50', 'stat': 'Ok', 'FillsellamtCF': '0.00', 'PriceDenomenator': '1', 'netsellqty': '87', 'PriceNumerator': '1', 'posflag': 'true', 'Stikeprc': '0', 'BEP': '0.00', 'Series': 'EQ', 'GeneralDenomenator': '1', 'Type': 'DAY1', 'Netamt': '-7,217.50', 'NetSellavgprc': '3357.04', 'CFBuyavgprc': '0.00', 'Fillbuyqty': '87', 'GeneralNumerator': '1', 'Exchangeseg': 'nse_cm', 'discQty': '10'}, {'Instname': 'NA', 'Expdate': 'NA', 'CFsellqty': '0', 'Opttype': 'XX', 'Token': '2031', 'CFSellavgprc': '0.00', 'sSqrflg': 'Y', 'unrealisedprofitloss': '0.00', 's_NetQtyPosConv': 'N', 'FillbuyamtCF': '0.00', 'Sqty': '233', 'Sellavgprc': '1,279.90', 'actid': 'SP220xx', 'netbuyamt': '297,075.00', 'Pcode': 'MIS', 'Bqty': '233', 'NetBuyavgprc': '1275.0', 'Exchange': 'NSE', 'companyname': 'MAHINDRA & MAHINDRA LTD', 'netbuyqty': '233', 'realisedprofitloss': '1,141.70', 'Fillsellamt': '298,216.70', 'Netqty': '0', 'Symbol': 'M&M', 'LTP': '1,274.65', 'BLQty': 1.0, 'Fillbuyamt': '297,075.00', 'Fillsellqty': '233', 'Tsym': 'M&M-EQ', 'CFbuyqty': '0', 'Buyavgprc': '1,275.00', 'netSellamt': '298,216.70', 'MtoM': '1,141.70', 'stat': 'Ok', 'FillsellamtCF': '0.00', 'PriceDenomenator': '1', 'netsellqty': '233', 'PriceNumerator': '1', 'posflag': 'true', 'Stikeprc': '0', 'BEP': '0.00', 'Series': 'EQ', 'GeneralDenomenator': '1', 'Type': 'DAY1', 'Netamt': '1,141.70', 'NetSellavgprc': '1279.9', 'CFBuyavgprc': '0.00', 'Fillbuyqty': '233', 'GeneralNumerator': '1', 'Exchangeseg': 'nse_cm', 'discQty': '10'}, {'Instname': 'OPTIDX', 'Expdate': '1 Sep, 2022', 'CFsellqty': '0', 'Opttype': 'CE', 'Token': '51698', 'CFSellavgprc': '0.00', 'sSqrflg': 'Y', 'unrealisedprofitloss': '555.00', 's_NetQtyPosConv': 'N', 'FillbuyamtCF': '18,570.00', 'Sqty': '0', 'Sellavgprc': '0.00', 'actid': 'SP220xx', 'netbuyamt': '18,570.00', 'Pcode': 'NRML', 'Bqty': '0', 'NetBuyavgprc': '441.0', 'Exchange': 'NFO', 'companyname': '', 'netbuyqty': '50', 'realisedprofitloss': '0.00', 'Fillsellamt': '0.00', 'Netqty': '50', 'Symbol': 'BANKNIFTY', 'LTP': '382.50', 'BLQty': 25.0, 'Fillbuyamt': '0.00', 'Fillsellqty': '0', 'Tsym': 'BANKNIFTY2290139100CE', 'CFbuyqty': '50', 'Buyavgprc': '0.00', 'netSellamt': '0.00', 'MtoM': '555.00', 'stat': 'Ok', 'FillsellamtCF': '0.00', 'PriceDenomenator': '1', 'netsellqty': '0', 'PriceNumerator': '1', 'posflag': 'false', 'Stikeprc': '39100.0', 'BEP': '371.40', 'Series': 'XX', 'GeneralDenomenator': '1', 'Type': 'NET1', 'Netamt': '-18,570.00', 'NetSellavgprc': '0.00', 'CFBuyavgprc': '441.0', 'Fillbuyqty': '0', 'GeneralNumerator': '1', 'Exchangeseg': 'nse_fo', 'discQty': 'NA'}, {'Instname': 'OPTIDX', 'Expdate': '1 Sep, 2022', 'CFsellqty': '100', 'Opttype': 'CE', 'Token': '51731', 'CFSellavgprc': '128.45', 'sSqrflg': 'Y', 'unrealisedprofitloss': '-150.00', 's_NetQtyPosConv': 'N', 'FillbuyamtCF': '0.00', 'Sqty': '0', 'Sellavgprc': '0.00', 'actid': 'SP220xx', 'netbuyamt': '0.00', 'Pcode': 'NRML', 'Bqty': '0', 'NetBuyavgprc': '0.00', 'Exchange': 'NFO', 'companyname': '', 'netbuyqty': '0', 'realisedprofitloss': '0.00', 'Fillsellamt': '0.00', 'Netqty': '-100', 'Symbol': 'BANKNIFTY', 'LTP': '96.00', 'BLQty': 25.0, 'Fillbuyamt': '0.00', 'Fillsellqty': '0', 'Tsym': 'BANKNIFTY2290139900CE', 'CFbuyqty': '0', 'Buyavgprc': '0.00', 'netSellamt': '9,450.00', 'MtoM': '-150.00', 'stat': 'Ok', 'FillsellamtCF': '9,450.00', 'PriceDenomenator': '1', 'netsellqty': '100', 'PriceNumerator': '1', 'posflag': 'false', 'Stikeprc': '39900.0', 'BEP': '94.50', 'Series': 'XX', 'GeneralDenomenator': '1', 'Type': 'NET1', 'Netamt': '9,450.00', 'NetSellavgprc': '128.45', 'CFBuyavgprc': '0.00', 'Fillbuyqty': '0', 'GeneralNumerator': '1', 'Exchangeseg': 'nse_fo', 'discQty': 'NA'}]
```

### Get Holding Positions
Code
```python
print(alice.get_holding_positions()) # get holding positions
```
Sample response
```
{'stat': 'Ok', 'HoldingVal': [{'WCqty': '0', 'BSEHOldingValue': '25700.00', 'hsflag': 'Y', 'Series1': 'A', 'HUqty': '200', 'authQty': '0', 'YSXHOldingValue': '0.00', 'CSEHOldingValue': '0.00', 'Ttrind': 'N', 'DaysMTM': '0', 'csflag': 'Y', 'WHqty': '0', 'Pcode': 'CNC', 'Price': '102.78', 'Exch4': '0', 'BuyQty': '0', 'Bsetsym': 'BANKBARODA', 'Exch5': '0', 'LTcse': '0.00', 'MCXHOldingValue': '0.00', 'Holdqty': '0', 'Exch1': 'nse_cm', 'Exch2': 'bse_cm', 'Exch3': '0', 'LTysx': '0.00', 'Haircut': '0.00', 'Scripcode': '532134', 'LTPValuation': '0', 'NSEHOldingValue': '25660.00', 'Ysxtsym': '0', 'Ltp': '128.50', 'Coltype': '--', 'Btst': '0', 'LTmcxsxcm': '0.00', 'Usedqty': '0', 'poaStatus': 'Y', 'Token5': '0', 'Nsetsym': 'BANKBARODA-EQ', 'CUqty': '0', 'Token2': '532134', 'Token1': '4668', 'Token4': '0', 'Token3': '0', 'SellableQty': '200', 'Mcxsxcmsym': '0', 'Csetsym': '0', 'authFlag': True, 'LTnse': '128.30', 'pdc': '125.9', 'Series': 'EQ', 'Colqty': '0', 'ExchSeg5': None, 'ExchSeg2': 'BSE', 'ExchSeg1': 'NSE', 'LTbse': '128.50', 'ExchSeg4': None, 'ExchSeg3': None, 'isin': 'INE028A01039', 'Tprod': 'NA'}, {'WCqty': '0', 'BSEHOldingValue': '772832.75', 'hsflag': 'Y', 'Series1': 'X', 'HUqty': '19345', 'authQty': '0', 'YSXHOldingValue': '0.00', 'CSEHOldingValue': '0.00', 'Ttrind': 'N', 'DaysMTM': '0', 'csflag': 'Y', 'WHqty': '0', 'Pcode': 'CNC', 'Price': '44.60', 'Exch4': '0', 'BuyQty': '0', 'Bsetsym': 'SMIFS', 'Exch5': '0', 'LTcse': '0.00', 'MCXHOldingValue': '0.00', 'Holdqty': '0', 'Exch1': '0', 'Exch2': 'bse_cm', 'Exch3': '0', 'LTysx': '0.00', 'Haircut': '0.00', 'Scripcode': '508905', 'LTPValuation': '0', 'NSEHOldingValue': '0.00', 'Ysxtsym': '0', 'Ltp': '39.95', 'Coltype': '--', 'Btst': '0', 'LTmcxsxcm': '0.00', 'Usedqty': '0', 'poaStatus': 'Y', 'Token5': '0', 'Nsetsym': '0', 'CUqty': '0', 'Token2': '508905', 'Token1': '0', 'Token4': '0', 'Token3': '0', 'SellableQty': '19345', 'Mcxsxcmsym': '0', 'Csetsym': '0', 'authFlag': True, 'LTnse': '0.00', 'pdc': '41.95', 'Series': '---', 'Colqty': '0', 'ExchSeg5': None, 'ExchSeg2': 'BSE', 'ExchSeg1': None, 'LTbse': '39.95', 'ExchSeg4': None, 'ExchSeg3': None, 'isin': 'INE641A01013', 'Tprod': 'NA'}], 'clientid': 'WBK293', 'Totalval': {'TotalMCXHoldingValue': '0.00', 'TotalCSEHoldingValue': '0.00', 'TotalNSEHoldingValue': '25660.00', 'TotalYSXHoldingValue': '0.00', 'TotalBSEHoldingValue': '798532.75'}}
```

### Get master contracts
Getting master contracts allow you to search for instruments by symbol name and place orders.
Master contracts are stored as an OrderedDict by token number and by symbol name in a local file. Whenever you get a trade update, order update, or quote update, the library will check if master contracts are loaded. If they are, it will attach the instrument object directly to the update. By default all master contracts of all enabled exchanges in your personal profile will be downloaded. i.e. If your profile contains the following as enabled exchanges `['NSE', 'BSE', 'MCX', NFO']` all contract notes of all exchanges will be downloaded by default. If you feel it takes too much time to download all exchange, or if you don't need all exchanges to be downloaded, you can specify which exchange to download contract notes while creating the AliceBlue object. Master contracts once downloaded is stored in temp location and reused the subsequent times. Master contracts are downloaded newly once a day (because new master contracts are updated everyday around 8:00am).

Code
```python
alice = AliceBlue(username = "username", session_id = session_id, master_contracts_to_download=['NSE', 'BSE'])
```
This will reduce a few seconds in object creation time of AliceBlue object.

#### Get Scrip info
Get Scrip info from alice server (this is different from instrument object).
```python
print(alice.get_scrip_info(alice.get_instrument_by_symbol("NSE", "INFY-EQ")))
```
```
{'optiontype': 'XX', 'SQty': 55, 'vwapAveragePrice': '1499.38', 'LTQ': '40', 'Ltp': '1511.65', 'LTP': '1511.65', 'DecimalPrecision': 2, 'openPrice': '1488.00', 'BRate': '00.00', 'defmktproval': '3', 'BQty': 0, 'symbolname': 'INFY', 'noMktPro': '0', 'LTT': '09/09/2022 15:59:32', 'mktpro': '1', 'TickSize': '5', 'Multiplier': 1, 'strikeprice': '00.00', 'TotalSell': '55', 'High': '1520.00', 'stat': 'Ok', 'BodLotQty': 1, 'yearlyHighPrice': '1953.90', 'yearlyLowPrice': '1367.15', 'exchFeedTime': '09-Sep-2022 16:18:43', 'PrvClose': '1511.65', 'SRate': '1511.65', 'Change': '00.00', 'Series': 'EQ', 'TotalBuy': 'NA', 'Low': '1480.00', 'UniqueKey': 'INFY', 'PerChange': '00.00', 'companyname': 'INFOSYS LIMITED', 'TradeVolume': '4816910', 'TSymbl': 'INFY-EQ', 'Exp': 'NA', 'LTD': 'NA'}
```
#### Instrument object
Instruments are represented by instrument objects. These are named-tuples that are created while getting the master contracts. They are used when placing an order and subscribing to a symbol. The structure of an instrument tuple is as follows:

```python
Instrument = namedtuple('Instrument', ['exchange', 'token', 'symbol',
                                      'name', 'expiry', 'lot_size'])
```

All instruments have the fields mentioned above. Wherever a field is not applicable for an instrument (for example, equity instruments don't have strike prices), that value will be `None`.

### Get tradable instruments
Symbols can be retrieved in multiple ways. Once you have the master contract loaded for an exchange, you can get an instrument in many ways.

#### Get a single instrument by it's name:
Code
```python
tatasteel_nse_eq = alice.get_instrument_by_symbol('NSE', 'TATASTEEL-EQ')
reliance_nse_eq = alice.get_instrument_by_symbol('NSE', 'RELIANCE-EQ')
ongc_bse_eq = alice.get_instrument_by_symbol('BSE', 'ONGC-EQ')
india_vix_nse_index = alice.get_instrument_by_symbol('NSE', 'India VIX')
sensex_nse_index = alice.get_instrument_by_symbol('BSE', 'SENSEX')
nifty50_nse_index = alice.get_instrument_by_symbol('NSE', 'NIFTY 50')
banknifty_nse_index = alice.get_instrument_by_symbol('NSE', 'NIFTY Bank')
```

#### Get a single instrument by it's token number (generally useful only for BSE Equities):
Code
```python
ongc_bse_eq = alice.get_instrument_by_token('BSE', 500312)
reliance_bse_eq = alice.get_instrument_by_token('BSE', 500325)
acc_nse_eq = alice.get_instrument_by_token('NSE', 22)
```

#### Get FNO instruments easily by mentioning expiry, strike & call or put.
Code
```python
bn_fut = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=True, strike=None, is_CE = False)
bn_call = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=False, strike=30000, is_CE = True)
bn_put = alice.get_instrument_for_fno(symbol = 'BANKNIFTY', expiry_date=datetime.date(2019, 6, 27), is_fut=False, strike=30000, is_CE = False)
```

### Search for symbols
Search for multiple instruments by matching the name. This works case insensitive and returns all instrument which has the name in its symbol.
Code
```python
all_sensex_scrips = alice.search_instruments('BSE', 'sEnSeX')
print(all_sensex_scrips)
```
The above code results multiple symbol which has 'sensex' in its symbol.
Sample response
```
[Instrument(exchange='BSE', token=532985, symbol='KTKSENSEX', name='KOTAK MAHINDRA MUTUAL FUND', expiry=None, lot_size='1'), Instrument(exchange='BSE', token=535276, symbol='SBISENSEX', name='SBI MUTUAL FUND - SBI ETF SENS', expiry=None, lot_size='1'), Instrument(exchange='BSE', token=538683, symbol='SENSEXBEES', name='NIPPON INDIA ETF SENSEX', expiry=None, lot_size='1'), Instrument(exchange='BSE', token=540154, symbol='IDFSENSEXE', name='IDFC Mutual Fund', expiry=None, lot_size='1'), Instrument(exchange='BSE', token=199040, symbol='SENSEXBINAV', name='INAV NIPPO INDIA ETF SENSE', expiry=None, lot_size='1')]
```

#### Search for multiple instruments by matching multiple names
Code
```python
multiple_underlying = ["INFY", "SBIN", "BHEL"]
all_scripts = alice.search_instruments('NFO', multiple_underlying)
print(all_scripts)
```

### Live Feed Data and Market Depth Data
Once you have master contracts loaded & a tradable instrument, you can easily subscribe to market feedd/depth data.

#### Two types of Live data are available
You can subscribe any one type of live data for a given scrip. Using the `LiveFeedType` enum, you can specify what type of live feed you need.
* `LiveFeedType.TICK_DATA`
* `LiveFeedType.DEPTH_DATA`

Please refer to the original documentation [here](https://v2api.aliceblueonline.com/websocket) for more details of different types of live feeds.

#### Subscribe to a live feed
Code
```python
alice.subscribe(alice.get_instrument_by_symbol('NSE', 'TATASTEEL-EQ'), LiveFeedType.TICK_DATA)
alice.subscribe(alice.get_instrument_by_symbol('BSE', 'RELIANCE-EQ'), LiveFeedType.DEPTH_DATA)
```
#### Subscribe to multiple instruments in a single call. Give an array of instruments to be subscribed.
Code
```python
alice.subscribe([alice.get_instrument_by_symbol('NSE', 'TATASTEEL-EQ'), alice.get_instrument_by_symbol('NSE', 'ACC-EQ')], LiveFeedType.TICK_DATA)
```

#### Start getting live feed via websocket
Code
```python
def event_handler_quote_update(message):
    print(f"quote update {message}")

alice.start_websocket(subscribe_callback=event_handler_quote_update)

alice.subscribe(alice.get_instrument_by_symbol('NSE', 'ONGC-EQ'), LiveFeedType.TICK_DATA)
sleep(10)
```

#### Unsubscribe to a live feed
Unsubscribe to an existing live feed.

Code
```python
alice.unsubscribe(alice.get_instrument_by_symbol('NSE', 'TATASTEEL-EQ'), LiveFeedType.TICK_DATA)
alice.unsubscribe(alice.get_instrument_by_symbol('BSE', 'RELIANCE-EQ'), LiveFeedType.DEPTH_DATA)
```
#### Unsubscribe to multiple instruments in a single call. Give an array of instruments to be unsubscribed.
Code
```python
alice.unsubscribe([alice.get_instrument_by_symbol('NSE', 'TATASTEEL-EQ'), alice.get_instrument_by_symbol('NSE', 'ACC-EQ')], LiveFeedType.TICK_DATA)
```

#### Get All Subscribed Symbols
Code
```python
alice.get_all_subscriptions() # All
```

### Market Status messages & Exchange messages.
Subscribe to market status & Exchange messages coming soon.

#### Subscribe to Market Status messages
Code
```python
alice.subscribe_market_status_messages()
```

#### Getting market status messages.
Code
```python
print(alice.get_market_status_messages())
```

Sample Response of `get_market_status_messages()`
```
[{'exchange': 'NSE', 'length_of_market_type': 6, 'market_type': b'NORMAL', 'length_of_status': 31, 'status': b'The Closing Session has closed.'}, {'exchange': 'NFO', 'length_of_market_type': 6, 'market_type': b'NORMAL', 'length_of_status': 45, 'status': b'The Normal market has closed for 22 MAY 2020.'}, {'exchange': 'CDS', 'length_of_market_type': 6, 'market_type': b'NORMAL', 'length_of_status': 45, 'status': b'The Normal market has closed for 22 MAY 2020.'}, {'exchange': 'BSE', 'length_of_market_type': 13, 'market_type': b'OTHER SESSION', 'length_of_status': 0, 'status': b''}]
```

#### Subscribe to exchange messages
Code
```python
alice.subscribe_exchange_messages()
```

#### Getting market status messages.
Code
```python
print(alice.get_exchange_messages())
```

Sample Response of `get_exchange_messages()`
```
[{'exchange': 'NSE', 'length': 32, 'message': b'DS : Bulk upload can be started.', 'exchange_time_stamp': 1590148595}, {'exchange': 'NFO', 'length': 200, 'message': b'MARKET WIDE LIMIT FOR VEDL IS 183919959. OPEN POSITIONS IN VEDL HAVE REACHED 84 PERCENT OF THE MARKET WIDE LIMIT.                                                                                       ', 'exchange_time_stamp': 1590146132}, {'exchange': 'CDS', 'length': 54, 'message': b'DS : Regular segment Bhav copy broadcast successfully.', 'exchange_time_stamp': 1590148932}, {'exchange': 'MCX', 'length': 7, 'message': b'.......', 'exchange_time_stamp': 1590196159}]
```

#### Market Status messages & Exchange messages through callbacks
Code
```python
socket_opened = False
def market_status_messages(message):
    print(f"market status messages {message}")

def exchange_messages(message):
    print(f"exchange messages {message}")

alice.start_websocket(market_status_messages_callback=market_status_me
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `alice_blue/__init__.py`
```python
from .alice_blue import AliceBlue, TransactionType, OrderType, ProductType, LiveFeedType, Instrument, HistoricalDataType, CryptoJsAES
__all__ = ['AliceBlue', 'TransactionType', 'OrderType', 'ProductType', 'LiveFeedType', 'Instrument', 'HistoricalDataType', 'CryptoJsAES']
```

#### File: `setup.py`
```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = 'alice_blue',
    packages=setuptools.find_packages(),
    version = '2.0.4',
    include_package_data=True,
    description = 'Official Python library for Alice Blue APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",  author = 'Krishna Velu',
    author_email = 'krishnajvelu@gmail.com',
    url = 'https://github.com/krishnavelu/alice_blue',
    install_requires=['cryptography', 'pytz', 'requests', 'websocket_client'],
    keywords = ['alice', 'alice-blue', 'python', 'sdk', 'trading', 'stock markets'],
    python_requires='>=3.6',
    classifiers=[
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
```

#### File: `alice_blue/alice_blue.py`
```python
from collections import namedtuple
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from time import sleep
from urllib.parse import urlparse, parse_qs
import base64
import datetime
import enum
import hashlib
import json
import logging
import os
import pytz
import requests
import tempfile
import threading
import websocket

Instrument = namedtuple('Instrument', ['exchange', 'token', 'symbol',
                                       'name', 'expiry', 'lot_size'])
logger = logging.getLogger(__name__)

class Requests(enum.IntEnum):
    PUT     = 1
    DELETE  = 2
    GET     = 3
    POST    = 4

class TransactionType(enum.Enum):
    Buy = 'BUY'
    Sell = 'SELL'

class OrderType(enum.Enum):
    Market = 'MKT'
    Limit = 'L'
    StopLossLimit = 'SL'
    StopLossMarket = 'SL-M'
    BracketOrder = "BO"
    AfterMarketOrder = "AMO"

class ProductType(enum.Enum):
    Intraday = 0
    Delivery = 1

class LiveFeedType(enum.IntEnum):
    TICK_DATA     = 1
    DEPTH_DATA      = 2

class HistoricalDataType(enum.Enum):
    Day = '1D'
    Minute = '1'

class CryptoJsAES:
    @staticmethod
    def __pad(data):
        BLOCK_SIZE = 16
        length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
        return data + (chr(length)*length).encode()

    @staticmethod
    def __unpad(data):
        return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]

    @staticmethod
    def __bytes_to_key(data, salt, output=48):
        assert len(salt) == 8, len(salt)
        data += salt
        key = hashlib.md5(data).digest()
        final_key = key
        while len(final_key) < output:
            key = hashlib.md5(key + data).digest()
            final_key += key
        return final_key[:output]

    @staticmethod
    def encrypt(message, passphrase):
        salt = os.urandom(8)
        key_iv = CryptoJsAES.__bytes_to_key(passphrase, salt, 32+16)
        key = key_iv[:32]
        iv = key_iv[32:]
        aes = Cipher(algorithms.AES(key), modes.CBC(iv))
        return base64.b64encode(b"Salted__" + salt + aes.encryptor().update(CryptoJsAES.__pad(message)) + aes.encryptor().finalize())

    @staticmethod
    def decrypt(encrypted, passphrase):
        encrypted = base64.b64decode(encrypted)
        assert encrypted[0:8] == b"Salted__"
        salt = encrypted[8:16]
        key_iv = CryptoJsAES.__bytes_to_key(passphrase, salt, 32+16)
        key = key_iv[:32]
        iv = key_iv[32:]
        aes = Cipher(algorithms.AES(key), modes.CBC(iv))
        return CryptoJsAES.__unpad(aes.decryptor.update(encrypted[16:]) + aes.decryptor().finalize())

class AliceBlue:
    """ AliceBlue Class for all operations related to AliceBlue Server"""

    # URLs
    host = "https://ant.aliceblueonline.com/rest/AliceBlueAPIService"
    __urls = {  "webLogin"              :   f"{host}/customer/webLogin",
                "twoFA"                 :   f"{host}/sso/validAnswer",
                "sessionID"             :   f"{host}/sso/getUserDetails",
                "getEncKey"             :   f"{host}/customer/getEncryptionKey",
                "authorizeVendor"       :   f"{host}/sso/authorizeVendor",
                "apiGetEncKey"          :   f"{host}/api/customer/getAPIEncpkey",
                "profile"               :   f"{host}/api/customer/accountDetails",
                "placeOrder"            :   f"{host}/api/placeOrder/executePlaceOrder",
                "logout"                :   f"{host}/api/customer/logout",
                "logoutFromAllDevices"  :   f"{host}/api/customer/logOutFromAllDevice",
                "fetchMWList"           :   f"{host}/api/marketWatch/fetchMWList",
                "fetchMWScrips"         :   f"{host}/api/marketWatch/fetchMWScrips",
                "addScripToMW"          :   f"{host}/api/marketWatch/addScripToMW",
                "deleteMWScrip"         :   f"{host}/api/marketWatch/deleteMWScrip",
                "scripDetails"          :   f"{host}/api/ScripDetails/getScripQuoteDetails",
                "positions"             :   f"{host}/api/positionAndHoldings/positionBook",
                "holdings"              :   f"{host}/api/positionAndHoldings/holdings",
                "sqrOfPosition"         :   f"{host}/api/positionAndHoldings/sqrOofPosition",
                "fetchOrder"            :   f"{host}/api/placeOrder/fetchOrderBook",
                "fetchTrade"            :   f"{host}/api/placeOrder/fetchTradeBook",
                "exitBracketOrder"      :   f"{host}/api/placeOrder/exitBracketOrder",
                "modifyOrder"           :   f"{host}/api/placeOrder/modifyOrder",
                "cancelOrder"           :   f"{host}/api/placeOrder/cancelOrder",
                "orderHistory"          :   f"{host}/api/placeOrder/orderHistory",
                "getRmsLimits"          :   f"{host}/api/limits/getRmsLimits",
                "createWsSession"       :   f"{host}/api/ws/createSocketSess",
                "history"               :   f"{host}/api/chart/history",
                "master_contract"       :   "https://v2api.aliceblueonline.com/restpy/contract_master?exch={exchange}",
                "ws"                    :   "wss://ws2.aliceblueonline.com/NorenWS/"
            }

    def __init__(self, username, session_id, master_contracts_to_download = None):
        """ Create Alice Blue object, get enabled exchanges and products for user """
        self.__username = username
        self.__session_id = session_id
        self.__websocket = None
        self.__websocket_connected = False
        self.__ws_mutex = threading.Lock()
        self.__on_error = None
        self.__on_disconnect = None
        self.__on_open = None
        self.__subscribe_callback = None
        self.__order_tag = 1
        self.__order_update_callback = None
        self.__market_status_messages_callback = None
        self.__exchange_messages_callback = None
        self.__subscribers = {}
        self.__market_status_messages = []
        self.__exchange_messages = []
        # Initialize Depth data
        self.__depth_data = {} 
        self.__tick_data = {} 

        try:
            self.get_profile()
        except Exception as e:
            raise Exception(f"Couldn't get profile info with credentials provided '{e}'")
        self.__master_contracts_by_token = {}
        self.__master_contracts_by_symbol = {}
        self.__get_master_contract("INDICES")
        if(master_contracts_to_download == None):
            for e in self.__enabled_exchanges:
                self.__get_master_contract(e)
        else:
            for e in master_contracts_to_download:
                self.__get_master_contract(e)
        self.ws_thread = None

    @staticmethod
    def login_and_get_sessionID(username, password, twoFA, app_id, api_secret):
        """ Login and get Session ID """
        header = {"Content-Type" : "application/json"}
        try:
            dr = tempfile.gettempdir()
            tmp_file = os.path.join(dr, f"alice_blue_key_{username}.json")
            if(os.path.isfile(tmp_file) == True):
                d = {}
                with open(tmp_file, 'r') as fo:
                    d = json.loads(fo.read())
                if(len(d["session_id"])):
                    # Try getting profile/account details
                    data = {"userId" : username}
                    hdr = { "Content-Type" : "application/json",
                            "Authorization" : f"Bearer {username} {d['session_id']}"}
                    r = requests.get(AliceBlue.__urls["profile"], headers=hdr, data=json.dumps(data))
                    logging.info(f"Get Account details response {r.text}")
                    if(r.status_code == 200):
                        if("stat" not in r.json()):
                            logging.info(f"Using stored session_id {d['session_id']}")
                            return d['session_id']
            with open(tmp_file, 'w') as fo:
                d = {"session_id" : ""}
                fo.write(json.dumps(d))
        except Exception as e:
            logging.warn(f"Getting session_id from temp file ended in exception {e}")
        # Get Encryption Key
        data = {"userId" : username}
        r = requests.post(AliceBlue.__urls['getEncKey'], headers=header, json=data)
        logging.info(f"Get Encryption Key response {r.text}")
        encKey = r.json()["encKey"]

        # Web Login
        checksum = CryptoJsAES.encrypt(password.encode(), encKey.encode())
        checksum = checksum.decode("utf-8")
        data = {"userId" : username,
                "userData" : checksum}
        r = requests.post(AliceBlue.__urls["webLogin"], json=data)
        logging.info(f"Web Login response {r.text}")

        # Web Login 2FA
        data = {"answer1" : twoFA,
                "sCount" : "1",
                "sIndex" : "1",
                "userId" : username,
                "vendor" : app_id}
        r = requests.post(AliceBlue.__urls["twoFA"], json=data)
        logging.info(f"Web Login 2FA response {r.text}")
        isAuthorized = r.json()['isAuthorized']
        authCode = parse_qs(urlparse(r.json()["redirectUrl"]).query)['authCode'][0]
        logging.info(f"isAuthorized {isAuthorized}")
        logging.info(f"authCode {authCode}")

        # Get API Encryption Key
        data = {"userId" : username}
        r = requests.post(AliceBlue.__urls["apiGetEncKey"], headers=header, data=json.dumps(data))
        logging.info(f"Get API Encryption Key response {r.text}")

        # Get User Details/Session ID
        checksum = hashlib.sha256(f"{username}{authCode}{api_secret}".encode()).hexdigest()
        data = {"checkSum" : checksum}
        r = requests.post(AliceBlue.__urls["sessionID"], headers=header, data=json.dumps(data))
        logging.info(f"Session ID response {r.text}")
        session_id = r.json()['userSession']
        logging.info(f"Session ID is {session_id}")

        # Authorize vendor app
        if(isAuthorized == False):
            data = {"userId" : username,
                    "vendor" : app_id}
            print("Authorizing vendor app")
            r = requests.post(AliceBlue.__urls["authorizeVendor"], headers=header, data=json.dumps(data))

        # Write session_id in temp file for next time usage
        with open(tmp_file, 'w') as fo:
            d = {"session_id" : session_id}
            fo.write(json.dumps(d))
        return session_id

    def __extract_tick_data(self, data):
        if("tk" in data):               # Token
            data["instrument"] = self.get_instrument_by_token(data.pop("e"), int(data.pop("tk")))
        if("ts" in data):               # Symbol
            data.pop("ts")
        if(data["instrument"].symbol not in self.__tick_data):
            self.__tick_data[data["instrument"].symbol] = {}
            self.__tick_data[data["instrument"].symbol]["ltp"] = 0
            self.__tick_data[data["instrument"].symbol]["percent_change"] = 0
            self.__tick_data[data["instrument"].symbol]["change_value"] = 0
            self.__tick_data[data["instrument"].symbol]["volume"] = 0
            self.__tick_data[data["instrument"].symbol]["open"] = 0
            self.__tick_data[data["instrument"].symbol]["high"] = 0
            self.__tick_data[data["instrument"].symbol]["low"] = 0
            self.__tick_data[data["instrument"].symbol]["close"] = 0
            self.__tick_data[data["instrument"].symbol]["exchange_time_stamp"] = None
            self.__tick_data[data["instrument"].symbol]["atp"] = 0
            self.__tick_data[data["instrument"].symbol]["tick_increment"] = 0
            self.__tick_data[data["instrument"].symbol]["lot_size"] = 0
            self.__tick_data[data["instrument"].symbol]["price_precision"] = 0
            self.__tick_data[data["instrument"].symbol]["total_open_interest"] = 0
        if("lp" in data):               # Last Traded Price
            self.__tick_data[data["instrument"].symbol]["ltp"] = float(data.pop("lp"))
        if("pc" in data):               # percentage change
            self.__tick_data[data["instrument"].symbol]["percent_change"] = float(data.pop("pc"))
        if("cv" in data):               # change value (absolute change in price)
            self.__tick_data[data["instrument"].symbol]["change_value"] = float(data.pop("cv"))
        if("v" in data):                # Volume
            self.__tick_data[data["instrument"].symbol]["volume"] = int(data.pop("v"))
        if("o" in data):                # Open
            self.__tick_data[data["instrument"].symbol]["open"] = float(data.pop("o"))
        if("h" in data):                # High
            self.__tick_data[data["instrument"].symbol]["high"] = float(data.pop("h"))
        if("l" in data):                # Low
            self.__tick_data[data["instrument"].symbol]["low"] = float(data.pop("l"))
        if("c" in data):                # Close
            self.__tick_data[data["instrument"].symbol]["close"] = float(data.pop("c"))
        if("ft" in data):               # Feed Time
            self.__tick_data[data["instrument"].symbol]["exchange_time_stamp"] = datetime.datetime.fromtimestamp(int(data.pop("ft")))
        if("ap" in data):               # Average Price
            self.__tick_data[data["instrument"].symbol]["atp"] = float(data.pop("ap"))
        if("ti" in data):               # Tick Increment
            self.__tick_data[data["instrument"].symbol]["tick_increment"] = float(data.pop("ti"))
        if("ls" in data):               # Lot Size
            self.__tick_data[data["instrument"].symbol]["lot_size"] = int(data.pop("ls"))
        if(data["instrument"].symbol not in self.__depth_data):                # Initialize depth data
            self.__depth_data[data["instrument"].symbol] = {}
            self.__depth_data[data["instrument"].symbol]["bid_prices"]          = [None, None, None, None, None]
            self.__depth_data[data["instrument"].symbol]["ask_prices"]          = [None, None, None, None, None]
            self.__depth_data[data["instrument"].symbol]["bid_quantities"]      = [None, None, None, None, None]
            self.__depth_data[data["instrument"].symbol]["ask_quantities"]      = [None, None, None, None, None]
            self.__depth_data[data["instrument"].symbol]["buy_orders"]          = [None, None, None, None, None]
            self.__depth_data[data["instrument"].symbol]["sell_orders"]         = [None, None, None, None, None]
            self.__depth_data[data["instrument"].symbol]["open_interest"]       = 0
            self.__depth_data[data["instrument"].symbol]["last_traded_quantity"]= 0
            self.__depth_data[data["instrument"].symbol]["last_traded_time"]    = None
            self.__depth_data[data["instrument"].symbol]["total_buy_quantity"]  = 0
            self.__depth_data[data["instrument"].symbol]["total_sell_quantity"] = 0
            self.__depth_data[data["instrument"].symbol]["upper_circuit"]       = 0
            self.__depth_data[data
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: pythonAPI (`VAULT_IN-QUANT-014_flattrade__pythonAPI`)
- **Full Name**: `IN-QUANT-014_flattrade__pythonAPI`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# 🚀 FLATTRADE Python API

> A powerful Python interface to connect with **`FLATTRADE OMS`** – place orders, fetch quotes, stream market data, and more.

---

## 📦 Getting Started

⚡ **Start Here:** **[`Set Up Flattrade API & Generate Token Fast`](token_generator/setup.md)**
*Step-by-step guide to install, configure, and authenticate your API connection in minutes!*

---

## 📚 API Reference

### 📊 Symbols

* 🔍 [`searchscrip`](#md-searchscrip) – Search instruments
* 🧾 [`get_security_info`](#md-get_security_info) – Get instrument metadata
* 💬 [`get_quotes`](#md-get_quotes) – Live market quotes
* ⏱️ [`get_time_price_series`](#md-get_time_price_series) – Intraday price data
* 📅 [`get_daily_price_series`](#md-get_daily_price_series) – Daily price history
* 🧠 [`get_option_chain`](#md-get_optionchain) – Option chain data

---

### 📈 Orders & Trades

* 🛒 [`place_order`](#md-place_order) – Place a new order
* ✏️ [`modify_order`](#md-modify_order) – Edit existing order
* ❌ [`cancel_order`](#md-cancel_order) – Cancel open order
* 🚪 [`exit_order`](#md-exit_order) – Exit existing position
* 🔄 [`product_convertion`](#md-prd_convert) – Convert product type
* 📑 [`get_orderbook`](#md-get_orderbook) – View all orders
* 📘 [`get_tradebook`](#md-get_tradebook) – View all trades
* 🧾 [`get_singleorderhistory`](#md-get_singleorderhistory) – Full order history

---

### 🗃️ Holdings & Limits

* 📦 [`get_holdings`](#md-get_holdings) – View stock holdings
* 📊 [`get_positions`](#md-get_positions) – Check open positions
* 💰 [`get_limits`](#md-get_limits) – View available margins

---

### 🌐 WebSocket API

* 🔌 [`start_websocket`](#md-start_websocket) – Initialize socket connection
* 📡 [`subscribe`](#md-subscribe) – Subscribe to live feeds
* 📴 [`unsubscribe`](#md-unsubscribe) – Unsubscribe from feeds

---

### 💡 Examples

* 🚀 [`getting started`](#md-example-basic) – Quick usage demo
* 📈 [`Market Functions`](#md-example-market) – Quote & data examples
* 🛒 [`Orders and Trade`](#md-example-orders) – Order placement & tracking

---
#### <a name="md-place_order"></a> place_order(buy_or_sell, product_type,exchange, tradingsymbol, quantity, discloseqty, price_type, price=0.0, trigger_price=None, retention='DAY', amo='NO', remarks=None)
place an order to oms

Example: 

```
ret = api.place_order(buy_or_sell='B', product_type='C',
                        exchange='NSE', tradingsymbol='CANBK-EQ', 
                        quantity=1, discloseqty=0,price_type='SL-LMT', price=200.00, trigger_price=199.50,
                        retention='DAY', remarks='my_order_001')
```
Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|uid*||Logged in User Id|
|actid*||Login users account ID|
|exch*|NSE  / NFO / BSE / MCX|Exchange (Select from ‘exarr’ Array provided in User Details response)|
|tsym*||Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)|
|qty*||Order Quantity |
|prc*||Order Price|
|trgprc||Only to be sent in case of SL / SL-M order.|
|dscqty||Disclosed quantity (Max 10% for NSE, and 50% for MCX)|
|prd*|C / M / H|Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call)|
|trantype*|B / S|B -> BUY, S -> SELL|
|prctyp*|LMT / MKT  / SL-LMT / SL-MKT / DS / 2L / 3L||||
|ret*|DAY / EOS / IOC |Retention type (Show options as per allowed exchanges) |
|remarks||Any tag by user to mark order.|
|ordersource|MOB / WEB / TT |Used to generate exchange info fields.|
|bpprc||Book Profit Price applicable only if product is selected as B (Bracket order ) |
|blprc||Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
|trailprc||Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
|amo||Yes , If not sent, of Not “Yes”, will be treated as Regular order. |
|tsym2||Trading symbol of second leg, mandatory for price type 2L and 3L (use url encoding to avoid special char error for symbols like M&M)|
|trantype2||Transaction type of second leg, mandatory for price type 2L and 3L|
|qty2||Quantity for second leg, mandatory for price type 2L and 3L|
|prc2||Price for second leg, mandatory for price type 2L and 3L|
|tsym3||Trading symbol of third leg, mandatory for price type 3L (use url encoding to avoid special char error for symbols like M&M)|
|trantype3||Transaction type of third leg, mandatory for price type 3L|
|qty3||Quantity for third leg, mandatory for price type 3L|
|prc3||Price for third leg, mandatory for price type 3L|


Response Details :

Response data will be in json format with below fields.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Place order success or failure indication.|
|request_time||Response received time.|
|norenordno||It will be present only on successful Order placement to OMS.|
|emsg||This will be present only if Order placement fails|

Sample Success Response:
{
    "request_time": "10:48:03 20-05-2020",
    "stat": "Ok",
    "norenordno": "20052000000017"
}

Sample Error Response :
{
    "stat": "Not_Ok",
    "request_time": "20:40:01 19-05-2020",
    "emsg": "Error Occurred : 2 \"invalid input\""
}

#### <a name="md-modify_order"></a> modify_order(orderno, exchange, tradingsymbol, newquantity,newprice_type, newprice, newtrigger_price, amo):
modify the quantity pricetype or price of an order

Example: 

```
orderno = ret['norenordno'] #from placeorder return value
ret = api.modify_order(exchange='NSE', tradingsymbol='CANBK-EQ', orderno=orderno,
                                   newquantity=2, newprice_type='MKT', newprice=0.00)
## sl modification
ret = api.modify_order(exchange='NSE', tradingsymbol='CANBK-EQ', orderno=orderno,
                                   newquantity=2, newprice_type='SL-LMT', newprice=201.00, newtrigger_price=200.00)
```

Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|exch*||Exchange|
|norenordno*||Noren order number, which needs to be modified|
|prctyp|LMT / MKT / SL-MKT / SL-LMT|This can be modified.|
|prc||Modified / New price|
|qty||Modified / New Quantity||Quantity to Fill / Order Qty - This is the total qty to be filled for the order. Its Open Qty/Pending Qty plus Filled Shares (cumulative for the order) for the order.|* Please do not send only the pending qty in this field|
|tsym*||Unque id of contract on which order was placed. Can’t be modified, must be the same as that of original order. (use url encoding to avoid special char error for symbols like M&M)|
|ret|DAY / IOC / EOS|New Retention type of the order |
||||
|trgprc||New trigger price in case of SL-MKT or SL-LMT|
|uid*||User id of the logged in user.|
|bpprc||Book Profit Price applicable only if product is selected as B (Bracket order ) |
|blprc||Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
|trailprc||Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |

Response Details :

Response data will be in json format with below fields.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Modify order success or failure indication.|
|result||Noren Order number of the order modified.|
|request_time||Response received time.|
|emsg||This will be present only if Order modification fails|

Sample Success Response :
{
     "request_time":"14:14:08 26-05-2020",
     "stat":"Ok",
     "result":"20052600000103"
}

Sample Failure Response :
{
   "request_time":"16:03:29 28-05-2020",
   "stat":"Not_Ok",
   "emsg":"Rejected : ORA:Order not found"
}

#### <a name="md-cancel_order"></a> cancel_order(orderno)
cancel an order

Example:

```
orderno = ret['norenordno'] #from placeorder return value
ret = api.cancel_order(orderno=orderno)
```

Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|norenordno*||Noren order number, which needs to be modified|
|uid*||User id of the logged in user.|

Response Details :

Response data will be in json format with below fields.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Cancel order success or failure indication.|
|result||Noren Order number of the canceled order.|
|request_time||Response received time.|
|emsg||This will be present only if Order cancelation fails|

Sample Success Response :
{
   "request_time":"14:14:10 26-05-2020",
   "stat":"Ok",
   "result":"20052600000103"
}

Sample Failure Response :
{
   "request_time":"16:01:48 28-05-2020",
   "stat":"Not_Ok",
   "emsg":"Rejected : ORA:Order not found to Cancel"
}


#### <a name="md-exit_order"></a> exit_order(orderno)
exits a cover or bracket order

Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|norenordno*||Noren order number, which needs to be modified|
|prd*|H / B |Allowed for only H and B products (Cover order and bracket order)|
|uid*||User id of the logged in user.|

Response Details :

Response data will be in json format with below fields.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Cancel order success or failure indication.|
|dmsg||Display message, (will be present only in case of success).|
|request_time||Response received time.|
|emsg||This will be present only if Order cancelation fails|


#### <a name="md-prd_convert"></a> position_product_conversion(exchange, tradingsymbol, quantity, new_product_type, previous_product_type, buy_or_sell, day_or_cf)

Convert a product of a position 

Example:

```
ret = api.get_positions()
#converts the first position from existing product to intraday
p = ret[0]
ret = api.position_product_conversion(p['exch'], p['tsym'], p['netqty'], 'I', p['prd'], 'B', 'DAY')
```

Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|exch*||Exchange|
|tsym*||Unique id of contract on which order was placed. Can’t be modified, must be the same as that of original order. (use url encoding to avoid special char error for symbols like M&M)|
|qty*||Quantity to be converted.|
|uid*||User id of the logged in user.|
|actid*||Account id|
|prd*||Product to which the user wants to convert position. |
|prevprd*||Original product of the position.|
|trantype*||Transaction type|
|postype*|Day / CF|Converting Day or Carry forward position|
|ordersource|MOB |For Logging|

Response Details :

Response data will be in json format with below fields.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Position conversion success or failure indication.|
|emsg||This will be present only if Position conversion fails.|

Sample Success Response :
{
   "request_time":"10:52:12 02-06-2020",
   "stat":"Ok"
}

Sample Failure Response :
{
   "stat":"Not_Ok",
   "emsg":"Invalid Input :  Invalid Position Type"
}

#### <a name="md-get_orderbook"></a>  Order Book
List of Orders placed for the account

Example :
```
ret = api.get_order_book()
print(ret)
```
Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|uid*||Logged in User Id|
|prd|H / M / ...|Product name|

Response Details :

Response data will be in json Array of objects with below fields in case of success.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Order book success or failure indication.|
|exch||Exchange Segment|
|tsym||Trading symbol / contract on which order is placed.|
|norenordno||Noren Order Number|
|prc||Order Price|
|qty||Order Quantity|
|prd||Display product alias name, using prarr returned in user details.|
|status|||
|trantype|B / S|Transaction type of the order|
|prctyp|LMT / MKT|Price type|
|fillshares||Total Traded Quantity of this order|
|avgprc||Average trade price of total traded quantity |
|rejreason||If order is rejected, reason in text form|
|exchordid||Exchange Order Number|
|cancelqty||Canceled quantity for order which is in status cancelled.|
|remarks||Any message Entered during order entry.|
|dscqty||Order disclosed quantity.|
|trgprc||Order trigger price|
|ret|DAY / IOC / EOS|Order validity|
|uid|||
|actid|||
|bpprc||Book Profit Price applicable only if product is selected as B (Bracket order ) |
|blprc||Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
|trailprc||Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
|amo||Yes / No|
|pp||Price precision|
|ti||Tick size|
|ls||Lot size|
|token||Contract Token|
|norentm|||
|ordenttm|||
|exch_tm|||
|snoordt||0 for profit leg and 1 for stoploss leg|
|snonum||This field will be present for product H and B; and only if it is profit/sl order.|

Response data will be in json format with below fields in case of failure:

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Not_Ok|Order book failure indication.|
|request_time||Response received time.|
|emsg||Error message|

Sample Success Output :
Success response :
[
      {
“stat” : “Ok”,
“exch” : “NSE” ,
“tsym” : “ACC-EQ” ,
“norenordno” : “20062500000001223”,
               “prc” : “127230”,
               “qty” : “100”,
               “prd” : “C”,
“status”: “Open”,
               “trantype” : “B”,
 “prctyp” : ”LMT”,
               “fillshares” : “0”,
               “avgprc” : “0”,
“exchordid” : “250620000000343421”,
 “uid” : “VIDYA”, 
 “actid” : “CLIENT1”,
 “ret” : “DAY”,
 “amo” : “Yes”
     },
    {
“stat” : “Ok”,
“exch” : “NSE” ,
“tsym” : “ABB-EQ” ,
“norenordno” : “20062500000002543”,
               “prc” : “127830”,
            “qty” : “50”,
               “prd” : “C”,
“status”: “REJECT”,
              “trantype” : “B”,
“prctyp” : ”LMT”,
             “fillshares” : “0”,
             “avgprc” : “0”,
              “rejreason” : “Insufficient funds”
“uid” : “VIDYA”, 
“actid” : “CLIENT1”,
“ret” : “DAY”,
“amo” : “No”
    }
]

Sample Failure Response :
{
   "stat":"Not_Ok",
   "emsg":"Session Expired : Invalid Session Key"
}

#### <a name="md-get_tradebook"></a>  Trade Book 
List of Trades of the account

Example:
```
ret = api.get_trade_book()
print(ret)
```

Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|uid*||Logged in User Id|
|actid*||Account Id of logged in user|

Response Details :

Response data will be in json Array of objects with below fields in case of success.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Order book success or failure indication.|
|exch||Exchange Segment|
|tsym||Trading symbol / contract on which order is placed.|
|norenordno||Noren Order Number|
|qty||Order Quantity|
|prd||Display product alias name, using prarr returned in user details.|
|trantype|B / S|Transaction type of the order|
|prctyp|LMT / MKT|Price type|
|fillshares||Total Traded Quantity of this order|
|avgprc||Average trade price of total traded quantity |
|exchordid||Exchange Order Number|
|remarks||Any message Entered during order entry.|
|ret|DAY / IOC / EOS|Order validity|
|uid|||
|actid|||
|pp||Price precision|
|ti||Tick size|
|ls||Lot size|
|cstFrm||Custom Firm|
|fltm||Fill Time|
|flid||Fill ID|
|flqty||Fill Qty|
|flprc||Fill Price|
|ordersource||Order Source|
|token||Token|

Response data will be in json format with below fields in case of failure:

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Not_Ok|Order book failure indication.|
|request_time||Response received time.|
|emsg||Error message|

Sample Success Output :

[
   {
       "stat": "Ok",
       "norenordno": "20121300065715",
       "uid": "GURURAJ",
       "actid": "GURURAJ",
       "exch": "NSE",
       "prctyp": "LMT",
       "ret": "DAY",
       "prd": "M",
       "flid": "102",
       "fltm": "01-01-1980 00:00:00",
       "trantype": "S",
       "tsym": "ACCELYA-EQ",
       "qty": "180",
       "token": "7053",
       "fillshares": "180",
       "flqty": "180",
       "pp": "2",
       "ls": "1",
       "ti": "0.05",
       "prc": "800.00",
       "flprc": "800.00",
       "norentm": "19:59:32 13-12-2020",
       "exch_tm": "00:00:00 01-01-1980",
       "remarks": "WC TEST Order",
       "exchordid": "6857"
   },
   {
       "stat": "Ok",
       "norenordno": "20121300065716",
       "uid": "GURURAJ",
       "actid": "GURURAJ",
       "exch": "NSE",
       "prctyp": "LMT",
       "ret": "DAY",
       "prd": "M",
       "flid": "101",
       "fltm": "01-01-1980 00:00:00",
       "trantype": "B",
       "tsym": "ACCELYA-EQ",
       "qty": "180",
       "token": "7053",
       "fillshares": "180",
       "flqty": "180",
       "pp": "2",
       "ls": "1",
       "ti": "0.05",
       "prc": "800.00",
       "flprc": "800.00",
       "norentm": "19:59:32 13-12-2020",
       "exch_tm": "00:00:00 01-01-1980",
       "remarks": "WC TEST Order",
       "exchordid": "6858"
   }
]

#### <a name="md-get_singleorderhistory"></a>  single order history(orderno)
history an order

```
orderno = ret['norenordno'] #from placeorder return value
ret = api.single_order_history(orderno=orderno)
```
Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|uid*||Logged in User Id|
|norenordno*||Noren Order Number|


Response Details :

Response data will be in json Array of objects with below fields in case of success.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Order book success or failure indication.|
|exch||Exchange Segment|
|tsym||Trading symbol / contract on which order is placed.|
|norenordno||Noren Order Number|
|prc||Order Price|
|qty||Order Quantity|
|prd||Display product alias name, using prarr returned in user details.|
|status|||
|rpt|| (fill/complete etc)|
|trantype|B / S|Transaction type of the order|
|prctyp|LMT / MKT|Price type|
|fillshares||Total Traded Quantity of this order|
|avgprc||Average trade price of total traded quantity |
|rejreason||If order is rejected, reason in text form|
|exchordid||Exchange Order Number|
|cancelqty||Canceled quantity for order which is in status cancelled.|
|remarks||Any message Entered during order entry.|
|dscqty||Order disclosed quantity.|
|trgprc||Order trigger price|
|ret|DAY / IOC / EOS|Order validity|
|uid|||
|actid|||
|bpprc||Book Profit Price applicable only if product is selected as B (Bracket order ) |
|blprc||Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
|trailprc||Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
|amo||Yes / No|
|pp||Price precision|
|ti||Tick size|
|ls||Lot size|
|token||Contract Token|
|norentm|||
|ordenttm|||
|exch_tm|||

Response data will be in json format with below fields in case of failure:

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Not_Ok|Order book failure indication.|
|request_time||Response received time.|
|emsg||Error message|

Sample Success Output :

[
   {
       "stat": "Ok",
       "norenordno": "20121300065716",
       "uid": "DEMO1",
       "actid": "DEMO1",
       "exch": "NSE",
       "tsym": "ACCELYA-EQ",
       "qty": "180",
       "trantype": "B",
       "prctyp": "LMT",
       "ret": "DAY",
       "token": "7053",
       "pp": "2",
       "ls": "1",
       "ti": "0.05",
       "prc": "800.00",
       "avgprc": "800.00",
       "dscqty": "0",
       "prd": "M",
       "status": "COMPLETE",
       "rpt": "Fill",
       "fillshares": "180",
       "norentm": "19:59:32 13-12-2020",
       "exch_tm": "00:00:00 01-01-1980",
       "remarks": "WC TEST Order",
       "exchordid": "6858"
   },
   {
       "stat": "Ok",
       "norenordno": "20121300065716",
       "uid": "DEMO1",
       "actid": "DEMO1",
       "exch": "NSE",
       "tsym": "ACCELYA-EQ",
       "qty": "180",
       "trantype": "B",
       "prctyp": "LMT",
       "ret": "DAY",
       "token": "7053",
       "pp": "2",
       "ls": "1",
       "ti": "0.05",
       "prc": "800.00",
       "dscqty": "0",
       "prd": "M",
       "status": "OPEN",
       "rpt": "New",
       "norentm": "19:59:32 13-12-2020",
       "exch_tm": "00:00:00 01-01-1980",
       "remarks": "WC TEST Order",
       "exchordid": "6858"
   },
   {
       "stat": "Ok",
       "norenordno": "20121300065716",
       "uid": "DEMO1",
       "actid": "DEMO1",
       "exch": "NSE",
       "tsym": "ACCELYA-EQ",
       "qty": "180",
       "trantype": "B",
       "prctyp": "LMT",
       "ret": "DAY",
       "token": "7053",
       "pp": "2",
       "ls": "1",
       "ti": "0.05",
       "prc": "800.00",
       "dscqty": "0",
       "prd": "M",
       "status": "PENDING",
       "rpt": "PendingNew",
       "norentm": "19:59:32 13-12-2020",
       "remarks": "WC TEST Order"
   },
   {
       "stat": "Ok",
       "norenordno": "20121300065716",
       "uid": "DEMO1",
       "actid": "DEMO1",
       "exch": "NSE",
       "tsym": "ACCELYA-EQ",
       "qty": "180",
       "trantype": "B",
       "prctyp": "LMT",
       "ret": "DAY",
       "token": "7053",
       "pp": "2",
       "ls": "1",
       "ti": "0.05",
       "prc": "800.00",
       "prd": "M",
       "status": "PENDING",
       "rpt": "NewAck",
       "norentm": "19:59:32 13-12-2020",
       "remarks": "WC TEST Order"
   }
]

#### <a name="md-get_holdings"></a> get_holdings(product_type)
retrieves the holdings as a list

Example:
```
ret = api.get_holdings()
```
Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|uid*||Logged in User Id|
|actid*||Account id of the logged in user.|
|prd*||Product name|

Response Details :
Response data will be in json format with below fields in case of Success:

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Holding request success or failure indication.|
|exch_tsym||Array of objects exch_tsym objects as defined below.|
|holdqty||Holding quantity|
|dpqty||DP Holding quantity|
|npoadqty||Non Poa display quantity|
|colqty||Collateral quantity|
|benqty||Beneficiary quantity|
|unplgdqty||Unpledged quantity|
|brkcolqty||Broker Collateral|
|btstqty||BTST quantity|
|btstcolqty||BTST Collateral quantity|
|usedqty||Holding used today|
|upldprc||Average price uploaded along with holdings|
Notes:
Valuation : btstqty + holdqty + brkcolqty + unplgdqty + benqty + Max(npoadqty, dpqty) - usedqty
Salable: btstqty + holdqty + unplgdqty + benqty + dpqty - usedqty


Exch_tsym object:
|Json Fields of object in values Array|Possible value|Description|
| --- | --- | ---|
|exch|NSE, BSE, NFO ...|Exchange |
|tsym||Trading symbol of the scrip (contract)|
|token||Token of the scrip (contract)|
|pp||Price precision|
|ti||Tick size|
|ls||Lot size|

Response data will be in json format with below fields in case of failure:

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Not_Ok|Position book request failure indication.|
|request_time||Response received time.|
|emsg||Error message|

Sample Success Response :
[   
      {
            "stat":"Ok", 
            "exch_tsym":[
                                      {
                                            "exch":"NSE",
                                            "token":"13",
                     "tsym":"ABB-EQ"
   }
         ],
            "holdqty":"2000000",
            "colqty":"200",
            "btstqty":"0",
            "btstcolqty":"0",
            "usedqty":"0",
            "upldprc" : "1800.00"
      },
      {
"stat":"Ok",
"exch_tsym":[
   {
          "exch":"NSE",
          "token":"22",
          "tsym":"ACC-EQ"
   }
         ],
"holdqty":"2000000",
"colqty":"200",
"btstqty":"0",
"btstcolqty":"0",
"usedqty":"0",
               "upldprc" : "1400.00"
        }
]

Sample Failure Response :
{
   "stat":"Not_Ok",
   "emsg":"Invalid Input : Missing uid or actid or prd."
}

#### <a name="md-get_positions"></a> get_positions()

retrieves the overnight and day positions as a list

Example: 
```
ret = api.get_positions()
mtm = 0
pnl = 0
for i in ret:
    mtm += float(i['urmtom'])
    pnl += float(i['rpnl'])
    day_m2m = mtm + pnl
print(f'{day_m2m} is your Daily MTM')
```

Request Details :

|Json Fields|Possible value|Description|
| --- | --- | ---|
|uid*||Logged in User Id|
|actid*||Account id of the logged in user.|

Response Details :

Response data will be in json format with Array of Objects with below fields in case of success.

|Json Fields|Possible value|Description|
| --- | --- | ---|
|stat|Ok or Not_Ok|Position book success or failure indication.|
|exch||Exchange segment|
|tsym||Trading symbol / contract.|
|token||Contract token|
|uid||User Id|
|actid||Account Id|
|prd||Product name to be shown.|
|netqty||Net Position quantity|
|netavgprc||Net position average price|
|daybuyqty||Day Buy Quantity|
|daysellqty||Day Sell Quantity|
|daybuyavgprc||Day Buy average price|
|daysellavgprc||Day buy average price|
|daybuyamt||Day Buy Amount|
|daysellamt||Day Sell Amount|
|cfbuyqty||Carry Forward Buy Quantity
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `test_api.py`
```python
from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

ret = api.get_limits()
 
print(ret)
```

#### File: `tests/test_product_convertion.py`
```python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

ret = api.get_positions()

p = ret[0]
ret = api.position_product_conversion(p['exch'], p['tsym'], p['netqty'], 'I', p['prd'], 'B', 'DAY')

print(ret)
```

#### File: `tests/test_basket_order.py`
```python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy, Order
import logging
import yaml
import timeit

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

orders = []

for index in range(1,5):
    order = Order()
    order.buy_or_sell = 'B'
    order.product_type='C'
    order.exchange='NSE'
    order.tradingsymbol='INFY-EQ'
    order.quantity=index
    order.discloseqty=0
    order.price_type='LMT'
    order.price=1500.00
    order.trigger_price=None
    order.retention='DAY'
    order.remarks='my_order_001'

    orders.append(order)

starttime = timeit.default_timer()
ret = api.place_basket(orders)
print("The time difference is :", timeit.default_timer() - starttime)


print(ret)
```

#### File: `tests/test_watchlist.py`
```python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging 

#supress debug messages for prod/tests
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

if ret != None:   
    wlnames = api.get_watch_list_names()

    for wl in wlnames['values']:
        print(80*'=')        
        scrips = api.get_watch_list(wlname=wl)
        print(scrips)
        print(80*'=')        

    wltest = wlnames['values'][0]
    ret = api.add_watch_list_scrip(wlname=wltest, instrument='NSE|22')
    wlscrips = api.get_watch_list(wlname=wltest)

    for scrip in wlscrips['values']:
        print(f"{scrip['exch']} - {scrip['token']} {scrip['tsym']}")
    
    print(80*'=')
    ret = api.delete_watch_list_scrip(wlname=wltest, instrument='NSE|22')
    wlscrips = api.get_watch_list(wlname=wltest)

    for scrip in wlscrips['values']:
        print(f"{scrip['exch']} - {scrip['token']} {scrip['tsym']}")
```

#### File: `tests/test_place_order.py`
```python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

ret = api.place_order(buy_or_sell='B', product_type='C',
                        exchange='NSE', tradingsymbol='CANBK-EQ', 
                        quantity=1, discloseqty=0,price_type='SL-LMT', price=200.00, trigger_price=199.50,
                        retention='DAY', remarks='my_order_001')

print(ret)

## check sl modification
orderno = ret['norenordno']

ret = api.modify_order(exchange='NSE', tradingsymbol='CANBK-EQ', orderno=orderno,
                                   newquantity=2, newprice_type='SL-LMT', newprice=201.00, newtrigger_price=200.00)


print(ret)

ret = api.modify_order(exchange='NSE', tradingsymbol='CANBK-EQ', orderno=orderno,
                                   newquantity=2, newprice_type='MKT', newprice=0.00)

print(ret)

ret = api.single_order_history(orderno=orderno)

for ord in ret:
    
    print(f"{ord['qty']} prc: {ord['prc']} trgprc: {ord['trgprc']} {ord['rpt']}")
```

#### File: `tests/test_tpseries.py`
```python
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging
import datetime
import timeit

#supress debug messages for prod/tests
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

if ret != None:   
    lastBusDay = datetime.datetime.today()
    lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)

    if datetime.date.weekday(lastBusDay) == 5:      #if it's Saturday
     lastBusDay = lastBusDay - datetime.timedelta(days = 1) #then make it Friday
    elif datetime.date.weekday(lastBusDay) == 6:      #if it's Sunday
     lastBusDay = lastBusDay - datetime.timedelta(days = 2); #then make it Friday

    print(lastBusDay.timestamp())
    #lastBusDay = 1639098000

    starttime = timeit.default_timer()
    print("The start time is :",starttime)
    #get one day's data

    #ret = api.get_time_price_series(exchange='NSE', token='22', starttime=lastBusDay.timestamp())
    ret = api.get_time_price_series(exchange='NSE', token='2885')
    print("The time difference is :", timeit.default_timer() - starttime)

    if ret != None:
        print(len(ret))
        print(ret[0])
        print(ret[-1])
```


==================================================


## [3/3] Repository: hdfcsec-strapi (`VAULT_IN-QUANT-015_11Lost__hdfcsec-strapi`)
- **Full Name**: `IN-QUANT-015_11Lost__hdfcsec-strapi`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Core Implementation Code & Architecture
#### File: `package-lock.json`
```python
{
  "name": "hdfcsec-strapi",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {}
}
```

#### File: `backend/src/components/main/calendar.json`
```python
{
  "collectionName": "components_main_calendars",
  "info": {
    "displayName": "Calendar",
    "icon": "calendar"
  },
  "options": {},
  "attributes": {
    "Title": {
      "type": "string"
    }
  },
  "config": {}
}
```

#### File: `backend/src/components/main/count-cont.json`
```python
{
  "collectionName": "components_main_count_conts",
  "info": {
    "displayName": "countCont"
  },
  "options": {},
  "attributes": {
    "title": {
      "type": "string"
    },
    "Count": {
      "type": "string"
    }
  },
  "config": {}
}
```

#### File: `backend/src/components/menus/menu-link.json`
```python
{
  "collectionName": "components_menus_menu_links",
  "info": {
    "displayName": "MenuLink"
  },
  "options": {},
  "attributes": {
    "label": {
      "type": "string"
    },
    "link": {
      "type": "string"
    },
    "target": {
      "type": "string"
    }
  },
  "config": {}
}
```

#### File: `backend/src/api/home2/content-types/home2/schema.json`
```python
{
  "kind": "singleType",
  "collectionName": "home2s",
  "info": {
    "singularName": "home2",
    "pluralName": "home2s",
    "displayName": "Home2"
  },
  "options": {
    "draftAndPublish": true
  },
  "pluginOptions": {},
  "attributes": {
    "text": {
      "type": "string"
    }
  }
}
```

#### File: `backend/src/components/menus/menu.json`
```python
{
  "collectionName": "components_menus_menus",
  "info": {
    "displayName": "menu"
  },
  "options": {},
  "attributes": {
    "title": {
      "type": "string"
    },
    "subMenus": {
      "type": "component",
      "component": "menus.sub-menus",
      "repeatable": true
    }
  },
  "config": {}
}
```


==================================================
