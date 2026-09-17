# ⚡ [QUANT-SOURCE-043] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_043_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: kiteconnect-ts (`PHASE4-QUANT-154`)
- **Full Name**: `PHASE4-QUANT-154_anurag-roy__kiteconnect-ts`
- **Description**: Unofficial library for the Kite Connect trading APIs, written in TypeScript
- **GitHub Stars**: 12
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# kiteconnect-ts

Unofficial library for the Kite Connect trading APIs, written in [TypeScript](https://www.typescriptlang.org/).

All classes and APIs are one-to-one with Zerodha's [official kiteconnectjs library](https://github.com/zerodha/kiteconnectjs), so your existing code should work as is but with the added benefit of types! You will notice TypeScript's type safety as soon as you initialize a new `KiteConnect` or `KiteTicker` class. A bunch of extra types/interfaces are also available and can be used where the type cannot be inferred by TypeScript. See the docs section for more information.

If you notice a bug, please [open an issue](https://github.com/anurag-roy/kiteconnect-ts/issues/new) or consider [contributing](./CONTRIBUTING.md).

## Documentation

Docs are auto-generated from TsDoc comments using [TypeDoc](https://typedoc.org/), [typedoc-plugin-markdown](https://github.com/tgreyuk/typedoc-plugin-markdown) and [Nextra](https://nextra.site/).

Browse the full docs [here](https://kiteconnect.anuragroy.dev) or go to a specific part:

### kiteconnect-ts

- [KiteConnect Class, properties and methods](https://kiteconnect.anuragroy.dev/classes/KiteConnect)
- [KiteTicker Class, properties and methods](https://kiteconnect.anuragroy.dev/classes/KiteTicker)
- [Enums](https://kiteconnect.anuragroy.dev/modules#enumerations)
- [Interfaces](https://kiteconnect.anuragroy.dev/modules#interfaces)

### Other

- [Zerodha's kiteconnectjs docs](https://kite.trade/docs/kiteconnectjs/v3)
- [Kite Connect HTTP API documentation](https://kite.trade/docs/connect/v3)

## Supported runtimes

- Node.js `v24+`
- Bun `v1.3+`
- Deno `v2+`

The HTTP and WebSocket clients use each runtime's native `fetch` and `WebSocket` implementations.

Please note: Browser environments are not supported. See [Browser Support](#browser-support) for more details.

## Installation

#### npm

```
npm install kiteconnect-ts
```

#### yarn

```
yarn add kiteconnect-ts
```

#### pnpm

```
pnpm add kiteconnect-ts
```

#### Bun

```
bun add kiteconnect-ts
```

#### Deno

```
deno add npm:kiteconnect-ts
```

## KiteConnect

```typescript
import { KiteConnect } from 'kiteconnect-ts';

const kc = new KiteConnect({
  api_key: 'YOUR_API_KEY',
});

// Get access token
try {
  const { access_token } = await kc.generateSession(
    'request_token',
    'YOUR_API_SECRET'
  );
  console.log('Access token:', access_token);
} catch (error) {
  console.error('Error while generating session', error);
  process.exit(1);
}

  // Get equity margins
  try {
    const margins = await kc.getMargins('equity');
    console.log('Equity margins', margins);
  } catch (error) {
  console.error('Error while fetching equity margins', error);
}
```

## KiteTicker

```typescript
import { KiteTicker, Tick } from 'kiteconnect-ts';

const ticker: KiteTicker = new KiteTicker({
  api_key: 'YOUR_API_KEY',
  access_token: 'YOUR_ACCESS_TOKEN',
});

ticker.on('ticks', (ticks: Tick[]) => {
  console.log('Ticks', ticks);
});

ticker.on('connect', () => {
  const items = [738561];
  ticker.subscribe(items);
});

ticker.connect();
```

## Using provided enums

This library does not export Typescript enums, but rather JavaScript const objects. This was a design decision taken consciously to allow using the value from the object as well as a string literal, which has a better dx in my opinion. Constants are also present in the classes as readonly members, mainly for backwards compatibility with kiteconnectjs. So in total there are 3 ways you can these, pick one that works for you!

### Option 1: As a string

All params which accept specific values provide type validation and autocomplete. So a simple string literal works as follows:

```typescript
import { KiteConnect } from 'kiteconnect-ts';
import env from './env.json';

const kc = new KiteConnect({
  api_key: env.API_KEY,
});

const instruments = await kc.getInstruments(['NSE']);
```

### Option 2: As an enum

You could also import the enum and use as follows:

```typescript
import { Exchange, KiteConnect } from 'kiteconnect-ts';
import env from './env.json';

const kc = new KiteConnect({
  api_key: env.API_KEY,
});

const instruments = await kc.getInstruments([Exchange.NSE]);
```

### Option 3: As a class member

This is mainly for backwards compatibility if you are migrating `kiteconnectjs` code to `kiteconnect-ts`.

```typescript
import { KiteConnect } from 'kiteconnect-ts';
import env from './env.json';

const kc = new KiteConnect({
  api_key: env.API_KEY,
});

const instruments = await kc.getInstruments([kc.EXCHANGE_NSE]);
```

## Browser Support

Unfortunately this library does not work on the browser, so you cannot use it on your Angular, React, Vue, etc front-ends. However, if you use a meta/full-stack framework (Next.js, Nuxt, etc) with SSR, you can definitely install and use it on the server side.

This is not a limitation of this library per say, rather a limitation from Zerodha as they [do not want you to use Kite APIs directly from the browser](https://kite.trade/forum/discussion/comment/25372/#Comment_25372). This is also evident once you try to access any Kite API endpoint from your browser and you are greeted with a CORS error.

However, you can connect to [Kite Websocket](https://kite.trade/docs/connect/v3/websocket/) from your browser using `WebSocket`. You'd need to write your own parser or adapt the code from [here](https://github.com/anurag-roy/kiteconnect-ts/blob/main/lib/ticker/index.ts#L87).

Here's an extremely simple full tick parser that just gets the `token`, `firstBid` and `firstAsk`.

```typescript
// Tick structure reference: https://kite.trade/docs/connect/v3/websocket/#message-structure
const parseBinary = (dataView: DataView) => {
  const numberOfPackets = dataView.getInt16(0);
  let index = 4;
  const ticks: { token: number; firstBid: number; firstAsk: number }[] = [];

  for (let i = 0; i < numberOfPackets; i++) {
    const size = dataView.getInt16(index - 2);

    // Parse whatever you need
    ticks.push({
      token: dataView.getInt32(index),
      firstBid: dataView.getInt32(index + 68) / 100,
      firstAsk: dataView.getInt32(index + 128) / 100,
    });

    index = index + 2 + size;
  }

  return ticks;
};

const API_KEY = 'INSERT_API_KEY_HERE';
const ACCESS_TOKEN = 'INSERT_ACCESS_TOKEN_HERE';

const ws = new WebSocket(
  `wss://ws.kite.trade?api_key=${API_KEY}&access_token=${ACCESS_TOKEN}`
);

ws.onopen = (_event) => {
  console.log('Connected to Zerodha Kite Socket!');

  const setModeMessage = { a: 'mode', v: ['full', [61512711]] };
  ws.send(JSON.stringify(setModeMessage));
};

ws.onerror = (error) => {
  console.log('Some error occurred', error);
};

ws.onmessage = async (message) => {
  if (message.data instanceof Blob && message.data.size > 2) {
    const arrayBuffer = await message.data.arrayBuffer();
    const dataView = new DataView(arrayBuffer);
    const ticks = parseBinary(dataView);
    console.log(ticks);
  }
};
```

## Todos

- Add more examples
- Add tests

## Changelog

Check the [changelog](./CHANGELOG.md).

## Contributing

See the [Contribution Guide](./CONTRIBUTING.md).

## License

[MIT](./LICENSE) © [Anurag Roy](https://github.com/anurag-roy)

## Credits

Code was adapted from [kiteconnectjs](https://github.com/zerodha/kiteconnectjs), MIT License, Copyright 2018 [Zerodha Technology](http://zerodha.com)

### Core Implementation Code & Architecture
#### File: `tsconfig.lint.json`
```python
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "paths": {
      "kiteconnect-ts": ["./lib/index.ts"]
    }
  }
}
```

#### File: `.changeset/config.json`
```python
{
  "$schema": "https://unpkg.com/@changesets/config@2.3.0/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "public",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2024",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "lib": ["ES2024"],
    "types": ["node"],
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true,
    "noUncheckedIndexedAccess": true,
    "noEmit": true,
    "resolveJsonModule": true
  },
  "exclude": ["dist", "docs", "node_modules"]
}
```

#### File: `typedoc.json`
```python
{
  "$schema": "https://typedoc.org/schema.json",
  "entryPoints": ["./lib/index.ts"],
  "readme": "typedoc/index.md",
  "out": "docs/content",
  "plugin": ["typedoc-plugin-markdown"],
  "excludePrivate": true,
  "disableSources": true,
  "githubPages": false,
  "kindSortOrder": [
    "Reference",
    "Project",
    "Module",
    "Namespace",
    "Enum",
    "EnumMember",
    "Class",
    "Interface",
    "TypeAlias",
    "Constructor",
    "Method",
    "Property",
    "Variable",
    "Function",
    "Accessor",
    "Parameter",
    "TypeParameter",
    "TypeLiteral",
    "CallSignature",
    "ConstructorSignature",
    "IndexSignature",
    "GetSignature",
    "SetSignature"
  ],
  "entryFileName": "index",
  "modulesFileName": "modules",
  "hideBreadcrumbs": true,
  "hidePageHeader": true
}
```

#### File: `docs/package.json`
```python
{
	"name": "docs",
	"private": true,
	"type": "module",
	"version": "1.0.0",
	"description": "Docs for kiteconnect-ts using Nextra",
	"main": "index.js",
	"scripts": {
		"dev": "next",
		"build": "next build",
		"postbuild": "pagefind --site .next/server/app --output-path public/_pagefind",
		"start": "next start"
	},
	"keywords": [],
	"author": "Anurag Roy <anuragroy@duck.com> (https://anuragroy.dev/)",
	"license": "MIT",
	"engines": {
		"node": ">=24"
	},
	"dependencies": {
		"geist": "^1.7.1",
		"next": "^16.2.6",
		"nextra": "^4.6.1",
		"nextra-theme-docs": "^4.6.1",
		"react": "^19.2.6",
		"react-dom": "^19.2.6"
	},
	"packageManager": "bun@1.3.14",
	"devDependencies": {
		"pagefind": "^1.5.2"
	},
	"patchedDependencies": {
		"nextra-theme-docs@4.6.1": "patches/nextra-theme-docs@4.6.1.patch"
	}
}
```

#### File: `package.json`
```python
{
  "name": "kiteconnect-ts",
  "author": "Anurag Roy",
  "description": "Unofficial library for the Kite Connect trading APIs, written in TypeScript.",
  "license": "MIT",
  "version": "3.0.0",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.cts",
  "files": [
    "dist"
  ],
  "sideEffects": false,
  "engines": {
    "node": ">=24"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/anurag-roy/kiteconnect-ts.git"
  },
  "homepage": "https://kiteconnect.anuragroy.dev",
  "bugs": {
    "url": "https://github.com/anurag-roy/kiteconnect-ts/issues"
  },
  "keywords": [
    "Zerodha",
    "KiteConnect",
    "KiteTicker",
    "TypeScript"
  ],
  "scripts": {
    "lint": "tsc -p tsconfig.lint.json",
    "build": "tsdown",
    "release": "bun run build && bun run changeset publish",
    "generateDocs": "bun typedoc/generateDocs.ts",
    "test": "bun run test:bun",
    "test:node": "bun run build && node --test tests/*.test.ts",
    "test:bun": "bun run build && bun test",
    "test:deno": "bun run build && deno test --allow-read --allow-net tests",
    "smoke:node": "node tests/package-smoke.cjs",
    "package:check": "publint",
    "pack:dry-run": "npm --cache /tmp/kiteconnect-ts-npm-cache pack --dry-run"
  },
  "devDependencies": {
    "@changesets/cli": "^2.31.0",
    "@types/node": "^24.12.4",
    "@types/papaparse": "^5.5.2",
    "publint": "^0.3.21",
    "tsdown": "^0.22.0",
    "typedoc": "^0.28.19",
    "typedoc-plugin-markdown": "^4.11.0",
    "typescript": "^5.9.3"
  },
  "dependencies": {
    "papaparse": "^5.5.3"
  },
  "publishConfig": {
    "access": "public",
    "provenance": true
  },
  "packageManager": "bun@1.3.14",
  "exports": {
    ".": {
      "import": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      },
      "require": {
        "types": "./dist/index.d.cts",
        "default": "./dist/index.cjs"
      }
    },
    "./package.json": "./package.json"
  }
}
```


==================================================


## [2/3] Repository: chartink_kite_amo_mean_reversion (`PHASE4-QUANT-135`)
- **Full Name**: `PHASE4-QUANT-135_bogadib__chartink_kite_amo_mean_reversion`
- **Description**: Python Algorithmic Trading code for using zerodha kite to place AMO orders based on Chartink scanner 
- **GitHub Stars**: 24
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Chartink Vishal Mehta Mean Reversion Scanner

This python script gets the stocks scanned by Mean Reversion scanner from Vishal Mehta. Once the stocks are available, it places AMO (After Market Order) in Zerodha Trading account using `kiteconnect` APIs.

The scanner can be located on chartink [https://chartink.com/screener/vishal-mehta-mean-reversion](https://chartink.com/screener/vishal-mehta-mean-reversion)

If available stocks are more than 10 then the stocks are sorted according to latest close price _ascending_ and only 10 orders are placed.



## How to use this repository

### Get the code

* Download the repository as zip
* Unzip / extract it in a folder preferably on `D:\trading` Avoid extracting on Desktop
 

### Installation

* Install Python 3.9.4 latest version as of today (25th April 2021)
* It can work on python 3.6 and above but it is not tested

### Virtual Environment Creation

* `python -m pip install virtualenv` on Windows or `python3 -m pip install --user virtualenv` on Linux 
* Go to the folder `D:\trading` and then create virtualenv as `venv` using command as `python -m virtualenv venv` on Windows or `python3 -m virtualenv -p py3 venv` on Linux
* Activate the virtual environment using `.\venv\Scripts\activate` on Windows or `source ./venv/bin/activate` on Linux/Mac. 
* Upgrade packages using command `python -m pip install -U pip wheel setuptools`


* `pip install .\Twisted-21.2.0-py3-none-any.whl` (MANDATORY on Windows, to install kiteconnect successfully.)
* `pip install .\TA_Lib-0.4.19-cp39-cp39-win_amd64.whl` (OPTIONAL on Windows)
* `pip install -r requirements.txt` (NOTE : There is issue while installing pandas on python 3.6.9 downgrade pandas version to 1.1.5)


## Important

* Before running the script, it is very important to generate the `enctoken.txt` file which is used in `config.py` file
* There are 2 ways to do this
    1. Copy Paste the enctoken from Zerodha Web Session using Chrome DevTools, check images in useful snapshots
    2. Another way to do this is to run the `login_and_generate_enctoken.py` script, this must be done once. 
       May have to run again if you invalidate the session.
       Run this again if you face any issues.
       This step will invalidate your web session if you have logged in through browser.


### Running the Script

* Before running the actual script `chartink_kite.py` you must create .env file same folder
* Copy the .env.example file or rename it to create a new .env file in the same folder
* Change the values for USERNAME, PASSWORD and PIN with your own credentials
* Finally you can run the script using `python chartink.py` or `python3 chartink.py`

## Note

* Some lines are commented since this code is not tested in Live Market
* Stop Loss for the Strategy is not implemented in the script, **3%** Stop Loss recommended by Vishal Mehta, people have posted that **4%** works better but some people keep Stop Loss based on their own Risk e.g. **2%** to **2.5%**
* Similarly, Target or Profit must be kept accordingly to your own Risk Management. Vishal Mehta recommends **6%** while some keep it at **4.5%** 
* Also, some people exit when the overall MTM / PnL reaches approximately **5%** or **6%** of invested capital.
* More images will be added in future. Please check existing images.
* Coding is still in progress, for any suggestions please open discussions [here](https://github.com/algo2t/chartink_kite_amo_mean_reversion/discussions/1#discussion-3336072).


### Useful snapshots

* Cloning repository, creating virutalenv and installing packages
  
  ![2021-04-25 05_01_48-WSL-Ubuntu](https://user-images.githubusercontent.com/73125182/115976343-aeb37b00-a58a-11eb-964f-c547cc329aac.png)

* Activating Virtual environment venv
  
  ![image](https://user-images.githubusercontent.com/73125182/115976649-aad52800-a58d-11eb-95cb-e919bc7850d0.png)

* Installing all requirements from `requirements.txt` using pip
  
  ![image](https://user-images.githubusercontent.com/73125182/115976685-fee00c80-a58d-11eb-93eb-92c55cbab47a.png)
  
  ![image](https://user-images.githubusercontent.com/73125182/115976708-57afa500-a58e-11eb-853a-2b3bbd8d0763.png)

* Below images there is an error which occurred because the session was expired. New enctoken was added to `enctoken.txt` file
  
  ![image](https://user-images.githubusercontent.com/73125182/115976802-4adf8100-a58f-11eb-8d26-0477e9083c9f.png)

* Getting the enctoken from the kite dashboard using Chrome DevTool. Copy paste it to enctoken.txt
  This will help to keep both web session running and script execution will not invalidate web session

  ![image](https://user-images.githubusercontent.com/73125182/115994306-15b94a00-a5f4-11eb-972e-41e9f1ad1a0f.png)


* Kite dashboard orders page before placing AMO orders.
 
 ![image](https://user-images.githubusercontent.com/73125182/115976365-f0442600-a58a-11eb-8e6f-19e2bd29a773.png)

* Executing script and checking output in console

  ![image](https://user-images.githubusercontent.com/73125182/115976385-2f727700-a58b-11eb-948c-83546fc1a2dd.png)

  ![image](https://user-images.githubusercontent.com/73125182/115976391-42854700-a58b-11eb-96a1-37ae39dcc1ab.png)

* Finally checking the orders on the kite dashboard

  ![image](https://user-images.githubusercontent.com/73125182/115976373-110c7b80-a58b-11eb-9f25-fadd2f7c5f15.png)

### Core Implementation Code & Architecture
#### File: `.vscode/settings.json`
```python
{
    "python.pythonPath": "venv\\Scripts\\python.exe"
}
```

#### File: `config.py`
```python
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


username = os.getenv('USERID')
password = os.getenv('PASSWORD')
pin = os.getenv('PIN')

try:
    enctoken = open('enctoken.txt', 'r').read().rstrip()
except Exception as e:
    print('Exception occurred :: {}'.format(e))
    enctoken = None
```

#### File: `login_and_generate_enctoken.py`
```python
import logging
import os
from datetime import datetime as dt
from datetime import timedelta as td
from time import sleep

import pandas as pd
import pytz
import requests
from bs4 import BeautifulSoup

import config
from kiteext import KiteExt

log = logging.getLogger(__name__)
# NOTE while creating date objects you can use zone info which is very helpful when you are running scripts on outside India location
zone = pytz.timezone('Asia/Kolkata')

if __name__ == "__main__":
    global kite

    begin_time = dt.now(tz=zone)
    print(begin_time)

    kite = KiteExt(userid=config.username)
    kite.login_with_credentials(config.username, config.password, config.pin)
    margins = kite.margins()
    net_balance_equity = margins['equity']['net']
    live_balance_equity = margins['equity']['available']['live_balance']

    print(net_balance_equity)
    print(live_balance_equity)

    end_time = dt.now(tz=zone)
    print(end_time)
    duration = (end_time - begin_time)

    print(f'Total time taken by script :: {duration}')
```

#### File: `chartink_kite.py`
```python
import logging
import os
from datetime import datetime as dt
from datetime import timedelta as td
from time import sleep

import pandas as pd
import pytz
import requests
from bs4 import BeautifulSoup

import config
from kiteext import KiteExt

log = logging.getLogger(__name__)
# NOTE while creating date objects you can use zone info which is very helpful when you are running scripts on outside India location
zone = pytz.timezone('Asia/Kolkata')


def get_stocks():

    with requests.Session() as s:
        scanner_url = 'https://chartink.com/screener/vishal-mehta-mean-reversion'
        r = s.get(scanner_url)
        soup = BeautifulSoup(r.text, "html.parser")
        csrf = soup.select_one("[name='csrf-token']")['content']
        s.headers['x-csrf-token'] = csrf

        process_url = 'https://chartink.com/screener/process'
        payload = {
            # NOTE Vishal Mehta Mean Reversion Selling - Place Limit Order at 1% of Latest Close Price 3% SL and 6% Target Exit all positions at 3PM
            'scan_clause': '( {33489} ( latest close > latest sma( close, 200 ) and latest rsi( 2 ) > 50 and '\
            'latest close > 1 day ago close * 1.03 and latest close > 200 and latest close < 5000 and latest close > ( 4 days ago close * 1.0 ) ) ) '
        }

        r = s.post(process_url, data=payload)
        df = pd.DataFrame()
        for item in r.json()['data']:
            df = df.append(item, ignore_index=True)
        # NOTE Sorting done by ascending price so that stock with less price can be purchased before
        # Costly stocks may be rejected if there is no capital
        df.sort_values(by=['close'], inplace=True)
        df.drop('sr', axis=1, inplace=True)
        df.reset_index(inplace=True)
        df.drop('index', axis=1, inplace=True)

        print(f'number of stocks :: {len(df)}')
        if len(df) > 10:
            print('returning only first 10 stocks')
            df = df.head(10)
        return df


def capital_per_stock(balance, factor):
    return round(float(balance / factor), 0)


# variety, exchange, tradingsymbol, transaction_type, quantity, product, order_type, price=None,
# validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)


def place_amo_limit_order(symbol, price, qty):
    global kite
    # NOTE :: Need to place Limit Sell Order, Change PRODUCT to NRML to avoid leverage
    price = round((price * 1.01), 1)

    return kite.place_order(transaction_type=kite.TRANSACTION_TYPE_SELL, tradingsymbol=symbol, quantity=qty, price=price,
                            product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_LIMIT, variety=kite.VARIETY_AMO, exchange=kite.EXCHANGE_NSE)


def place_amo_orders(stocks):
    order_ids = []
    stocks.rename(columns={'nsecode': 'symbol',
                  'close': 'price'}, inplace=True)
    # print(stocks)
    for stock in stocks.itertuples():
        print(stock.symbol, stock.price, stock.qty)
        order = place_amo_limit_order(stock.symbol, stock.price, stock.qty)
        order_ids.append(order)

    return order_ids


def get_amo_orders():
    global kite
    data = kite.orders()
    df = pd.DataFrame(data, index=None)
    df = df[['exchange', 'tradingsymbol', 'order_type', 'quantity', 'variety',
             'status', 'order_id', 'order_timestamp', 'product', 'transaction_type']]
    df = df.loc[df['status'] == 'AMO REQ RECEIVED']
    return df


if __name__ == "__main__":
    global kite

    begin_time = dt.now(tz=zone)
    print(begin_time)

    stocks = get_stocks()
    print(stocks)

    kite = KiteExt(userid=config.username)
    kite.set_headers(config.enctoken)
    margins = kite.margins()
    net_balance_equity = margins['equity']['net']
    live_balance_equity = margins['equity']['available']['live_balance']

    print(net_balance_equity)
    print(live_balance_equity)

    # capital = capital_per_stock(net_balance_equity, len(stocks)) # If you want to allocate as per stock
    net_balance_equity = 50000.0  # for the sake of calculation
    capital = capital_per_stock(net_balance_equity, 10)

    stocks['qty'] = capital / stocks['close']
    stocks['qty'] = stocks['qty'].astype(int).round(0)
    stocks = stocks[['nsecode', 'close', 'qty', 'per_chg', 'volume']]

    print(stocks)
    orders_ids = place_amo_orders(stocks)
    print(orders_ids)
    print(get_amo_orders())

    end_time = dt.now(tz=zone)
    print(end_time)
    duration = (end_time - begin_time)

    print(f'Total time taken by script :: {duration}')
```

#### File: `kiteext.py`
```python
import json
import kiteconnect.exceptions as ex
import logging
from six.moves.urllib.parse import urljoin
import requests
import pandas as pd
from os import path

from kiteconnect import KiteConnect, KiteTicker

log = logging.getLogger(__name__)


class KiteExt(KiteConnect):

    def login_with_credentials(self, userid, password, pin):
        self.headers = {
            'x-kite-version': '3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }
        self.user_id = userid
        self.password = password
        self.twofa = pin
        self.reqsession = requests.Session()
        r = self.reqsession.post(self.root + self._routes['api.login'], data={
            'user_id': self.user_id,
            'password': self.password
        })

        r = self.reqsession.post(self.root + self._routes['api.twofa'], data={
            'request_id': r.json()['data']['request_id'],
            'twofa_value': self.twofa,
            'user_id': r.json()['data']['user_id']
        })

        
        self.enctoken = r.cookies.get('enctoken')

        with open('enctoken.txt', 'w') as wr:
            wr.write(self.enctoken)

        self.public_token = r.cookies.get('public_token')
        self.user_id = r.cookies.get('user_id')

        self.headers['Authorization'] = 'enctoken {}'.format(self.enctoken)

    def __init__(self, api_key='kitefront', userid=None, *args, **kw):
        KiteConnect.__init__(self, api_key=api_key,
                             *args, **kw)

        if userid is not None:
            self.user_id = userid

        self._routes.update({
            'api.login': '/api/login',
            'api.twofa': '/api/twofa',
            'api.misdata': '/margins/equity'
        })

    def set_headers(self, enctoken, userid=None):
        self.public_token = enctoken
        self.enctoken = enctoken
        if userid is not None:
            self.user_id = userid
        if self.user_id is None:
            raise Exception(
                f'userid cannot be none, either login with credentials first or set userid here')
        self.headers = {
            'x-kite-version': '3',
            'Authorization': 'enctoken {}'.format(self.enctoken)
        }

    def kws(self, api_key='kitefront'):
        return KiteTicker(api_key=api_key, access_token=self.public_token+'&user_id='+self.user_id, root='wss://ws.zerodha.com')

    def ticker(self, api_key='kitefront', enctoken=None, userid=None):
        if enctoken is not None:
            self.enctoken = enctoken
        if userid is not None:
            self.user_id = userid
        if self.user_id is None:
            raise Exception(
                f'userid cannot be none, either login with credentials first or set userid here')
        return KiteTicker(api_key=api_key, access_token=self.enctoken+'&user_id='+self.user_id, root='wss://ws.zerodha.com')

    def get_mis_data(self, symbol=None):
        df = pd.DataFrame()
        if path.exists('misdata.csv'):
            df = pd.read_csv('misdata.csv', index_col=0)
        else:
            r = self.reqsession.get(
                self._default_root_uri + self._routes['api.misdata'])
            df = pd.DataFrame(r.json(), index=None)
            df.to_csv('misdata.csv')
        if symbol is not None:
            return df.loc[df.tradingsymbol == symbol].head(1)
        return df

# NOTE NEW
    def _request(self, route, method, url_args=None, params=None, is_json=False):
        '''Make an HTTP request.'''
        # Form a restful URL
        if url_args:
            uri = self._routes[route].format(**url_args)
        else:
            uri = self._routes[route]

        url = urljoin(self.root, uri)

        headers = self.headers

        # Custom headers
        # headers = {
        #     'X-Kite-Version': '3',  # For version 3
        #     'User-Agent': self._user_agent()
        # }

        # if self.api_key and self.access_token:
        #     # set authorization header
        #     auth_header = self.api_key + ':' + self.access_token
        #     headers['Authorization'] = 'token {}'.format(auth_header)

        if self.debug:
            log.debug('Request: {method} {url} {params} {headers}'.format(
                method=method, url=url, params=params, headers=headers))

        try:
            r = self.reqsession.request(method,
                                        url,
                                        json=params if (
                                            method in ['POST', 'PUT'] and is_json) else None,
                                        data=params if (
                                            method in ['POST', 'PUT'] and not is_json) else None,
                                        params=params if method in [
                                            'GET', 'DELETE'] else None,
                                        headers=headers,
                                        verify=not self.disable_ssl,
                                        allow_redirects=True,
                                        timeout=self.timeout,
                                        proxies=self.proxies)
        # Any requests lib related exceptions are raised here - http://docs.python-requests.org/en/master/_modules/requests/exceptions/
        except Exception as e:
            raise e

        if self.debug:
            log.debug('Response: {code} {content}'.format(
                code=r.status_code, content=r.content))

        # Validate the content type.
        if 'json' in r.headers['content-type']:
            try:
                data = json.loads(r.content.decode('utf8'))
            except ValueError:
                raise ex.DataException('Could not parse the JSON response received from the server: {content}'.format(
                    content=r.content))

            # api error
            if data.get('error_type'):
                # Call session hook if its registered and TokenException is raised
                if self.session_expiry_hook and r.status_code == 403 and data['error_type'] == 'TokenException':
                    self.session_expiry_hook()

                # native Kite errors
                exp = getattr(ex, data['error_type'], ex.GeneralException)
                raise exp(data['message'], code=r.status_code)

            return data['data']
        elif 'csv' in r.headers['content-type']:
            return r.content
        else:
            raise ex.DataException('Unknown Content-Type ({content_type}) with response: ({content})'.format(
                content_type=r.headers['content-type'],
                content=r.content))
```


==================================================


## [3/3] Repository: kite-mcp (`PHASE4-QUANT-162`)
- **Full Name**: `PHASE4-QUANT-162_linkwithjoydeep__kite-mcp`
- **Description**: MCP server for Zerodha Kite -- trade Indian stocks via any MCP-compatible AI assistant
- **GitHub Stars**: 6
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Kite MCP Server

A Model Context Protocol (MCP) server for integrating with Zerodha Kite API. This server provides Claude with tools to interact with your Kite trading account.

## Features

- **Portfolio Management**: Get positions, holdings, and orders
- **Market Data**: Real-time quotes, LTP, and instrument data
- **Order Management**: Place, modify, and cancel orders
- **Account Info**: Profile, margins, and authentication status
- **Secure Authentication**: OAuth 2.0 flow with token persistence

## Prerequisites

1. **Zerodha Kite Connect App**: Create an app at [Kite Connect](https://kite.trade/)
2. **API Credentials**: Get your API Key and Secret
3. **Bun**: Latest version of Bun runtime

## Installation

1. Clone and install dependencies:

```bash
bun install
```

2. Set up environment variables:

```bash
# Edit .env with your API credentials
```

3. Configure your Kite Connect app with redirect URL:

```
http://localhost:50000/zerodha/auth/redirect
```

## Quick Start

### 1. Authenticate with Kite API

```bash
bun run auth
```

This will:

- Start a local OAuth server
- Open your browser to Kite login
- Save your access token securely

### 2. Start the MCP Server

```bash
bun start
```

### 3. Configure Claude Desktop

Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "kite": {
      "command": "bun",
      "args": ["run", "/path/to/kite-mcp/src/index.ts"]
    }
  }
}
```

## Available Tools

### Portfolio Tools

- `get_profile` - Get user profile information
- `get_positions` - Get current trading positions
- `get_holdings` - Get long-term holdings
- `get_margins` - Get account margins and funds

### Order Tools

- `get_orders` - Get today's orders
- `place_order` - Place a new trading order
- `cancel_order` - Cancel an existing order

### Market Data Tools

- `get_ltp` - Get Last Traded Price for instruments
- `get_quote` - Get detailed market quotes
- `get_instruments` - Get tradable instruments list

### Utility Tools

- `get_auth_status` - Check authentication status

## Project Structure

```
src/
├── config/
│   └── environment.ts          # Configuration management
├── auth/
│   ├── token-manager.ts        # Token storage and validation
│   └── oauth-server.ts         # OAuth flow handling
├── api/
│   └── kite-client.ts          # Kite API wrapper
├── mcp/
│   ├── server.ts               # MCP server implementation
│   └── tools/
│       └── index.ts            # MCP tools definitions
├── auth.ts                     # Authentication entry point
└── index.ts                    # MCP server entry point
```

## Development

### Build (Optional)

```bash
bun run build
```

### Development Mode

```bash
bun run dev          # Watch mode for MCP server
bun run dev:auth     # Watch mode for auth server
```

### Architecture

The project follows the Single Responsibility Principle:

- **ConfigManager**: Environment and configuration handling
- **TokenManager**: Token persistence and validation
- **OAuthServer**: OAuth 2.0 authentication flow
- **KiteClient**: Kite API wrapper with error handling
- **KiteMCPServer**: MCP protocol implementation
- **Tools**: Individual MCP tool implementations

## Environment Variables

```bash
API_KEY=your_kite_api_key        # Required: Kite Connect API Key
API_SECRET=your_kite_api_secret  # Required: Kite Connect API Secret
OAUTH_PORT=50000                 # Optional: OAuth server port (default: 50000)
```

## Security

- Tokens are stored locally in `access_token.json`
- OAuth flow uses secure redirect handling
- API credentials are never logged or exposed
- Tokens auto-expire for security

## Troubleshooting

### Authentication Issues

1. Verify API credentials in `.env`
2. Check redirect URL in Kite Connect app settings
3. Ensure OAuth port (50000) is available

### Token Expiry

- Kite tokens expire every ~6 hours
- Re-run `bun run auth` when expired
- Server will notify you of authentication status

### MCP Connection Issues

1. Verify Claude Desktop configuration
2. Check server is running: `bun start`
3. Look for errors in Claude Desktop logs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow the existing code structure and patterns
4. Add appropriate error handling
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Disclaimer

This is an unofficial integration with Zerodha Kite API. Use at your own risk. Always verify trades and orders before execution.

### Core Implementation Code & Architecture
#### File: `package.json`
```python
{
  "name": "kite-mcp",
  "version": "1.0.0",
  "type": "module",
  "private": true,
  "scripts": {
    "build": "bun build src/index.ts --outdir=dist --target=bun",
    "start": "bun run src/index.ts",
    "auth": "bun run src/auth.ts",
    "dev": "bun --watch src/index.ts",
    "dev:auth": "bun --watch src/auth.ts"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.12.1",
    "dotenv": "^16.5.0",
    "kiteconnect": "^5.0.1"
  },
  "devDependencies": {
    "@types/bun": "^1.2.15",
    "typescript": "^5.8.3"
  }
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": [
      "ESNext"
    ],
    "target": "ESNext",
    "module": "ESNext",
    "moduleDetection": "force",
    "allowJs": true,
    // Bundler mode
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,
    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    // Some stricter flags (disabled by default)
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noPropertyAccessFromIndexSignature": false,
    // For MCP types
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "resolveJsonModule": true
  },
  "include": [
    "src/**/*"
  ],
  "exclude": [
    "node_modules",
    "dist"
  ]
}
```


==================================================
