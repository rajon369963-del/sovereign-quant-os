# ⚡ [QUANT-SOURCE-010] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_010_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: nse-query-builder (`VAULT_IN-QUANT-084_Shubhamshah007__nse-query-builder`)
- **Full Name**: `IN-QUANT-084_Shubhamshah007__nse-query-builder`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<p align="center">
  <a href="http://nestjs.com/" target="blank"><img src="https://nestjs.com/img/logo-small.svg" width="120" alt="Nest Logo" /></a>
</p>

[circleci-image]: https://img.shields.io/circleci/build/github/nestjs/nest/master?token=abc123def456
[circleci-url]: https://circleci.com/gh/nestjs/nest

  <p align="center">A progressive <a href="http://nodejs.org" target="_blank">Node.js</a> framework for building efficient and scalable server-side applications.</p>
    <p align="center">
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/v/@nestjs/core.svg" alt="NPM Version" /></a>
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/l/@nestjs/core.svg" alt="Package License" /></a>
<a href="https://www.npmjs.com/~nestjscore" target="_blank"><img src="https://img.shields.io/npm/dm/@nestjs/common.svg" alt="NPM Downloads" /></a>
<a href="https://circleci.com/gh/nestjs/nest" target="_blank"><img src="https://img.shields.io/circleci/build/github/nestjs/nest/master" alt="CircleCI" /></a>
<a href="https://discord.gg/G7Qnnhy" target="_blank"><img src="https://img.shields.io/badge/discord-online-brightgreen.svg" alt="Discord"/></a>
<a href="https://opencollective.com/nest#backer" target="_blank"><img src="https://opencollective.com/nest/backers/badge.svg" alt="Backers on Open Collective" /></a>
<a href="https://opencollective.com/nest#sponsor" target="_blank"><img src="https://opencollective.com/nest/sponsors/badge.svg" alt="Sponsors on Open Collective" /></a>
  <a href="https://paypal.me/kamilmysliwiec" target="_blank"><img src="https://img.shields.io/badge/Donate-PayPal-ff3f59.svg" alt="Donate us"/></a>
    <a href="https://opencollective.com/nest#sponsor"  target="_blank"><img src="https://img.shields.io/badge/Support%20us-Open%20Collective-41B883.svg" alt="Support us"></a>
  <a href="https://twitter.com/nestframework" target="_blank"><img src="https://img.shields.io/twitter/follow/nestframework.svg?style=social&label=Follow" alt="Follow us on Twitter"></a>
</p>
  <!--[![Backers on Open Collective](https://opencollective.com/nest/backers/badge.svg)](https://opencollective.com/nest#backer)
  [![Sponsors on Open Collective](https://opencollective.com/nest/sponsors/badge.svg)](https://opencollective.com/nest#sponsor)-->

## Description

[Nest](https://github.com/nestjs/nest) framework TypeScript starter repository.

## Project setup

```bash
$ npm install
```

## Compile and run the project

```bash
# development
$ npm run start

# watch mode
$ npm run start:dev

# production mode
$ npm run start:prod
```

## Run tests

```bash
# unit tests
$ npm run test

# e2e tests
$ npm run test:e2e

# test coverage
$ npm run test:cov
```

## Deployment

When you're ready to deploy your NestJS application to production, there are some key steps you can take to ensure it runs as efficiently as possible. Check out the [deployment documentation](https://docs.nestjs.com/deployment) for more information.

If you are looking for a cloud-based platform to deploy your NestJS application, check out [Mau](https://mau.nestjs.com), our official platform for deploying NestJS applications on AWS. Mau makes deployment straightforward and fast, requiring just a few simple steps:

```bash
$ npm install -g @nestjs/mau
$ mau deploy
```

With Mau, you can deploy your application in just a few clicks, allowing you to focus on building features rather than managing infrastructure.

## Resources

Check out a few resources that may come in handy when working with NestJS:

- Visit the [NestJS Documentation](https://docs.nestjs.com) to learn more about the framework.
- For questions and support, please visit our [Discord channel](https://discord.gg/G7Qnnhy).
- To dive deeper and get more hands-on experience, check out our official video [courses](https://courses.nestjs.com/).
- Deploy your application to AWS with the help of [NestJS Mau](https://mau.nestjs.com) in just a few clicks.
- Visualize your application graph and interact with the NestJS application in real-time using [NestJS Devtools](https://devtools.nestjs.com).
- Need help with your project (part-time to full-time)? Check out our official [enterprise support](https://enterprise.nestjs.com).
- To stay in the loop and get updates, follow us on [X](https://x.com/nestframework) and [LinkedIn](https://linkedin.com/company/nestjs).
- Looking for a job, or have a job to offer? Check out our official [Jobs board](https://jobs.nestjs.com).

## Support

Nest is an MIT-licensed open source project. It can grow thanks to the sponsors and support by the amazing backers. If you'd like to join them, please [read more here](https://docs.nestjs.com/support).

## Stay in touch

- Author - [Kamil Myśliwiec](https://twitter.com/kammysliwiec)
- Website - [https://nestjs.com](https://nestjs.com/)
- Twitter - [@nestframework](https://twitter.com/nestframework)

## License

Nest is [MIT licensed](https://github.com/nestjs/nest/blob/master/LICENSE).

### Core Implementation Code & Architecture
#### File: `tsconfig.build.json`
```python
{
  "extends": "./tsconfig.json",
  "exclude": ["node_modules", "test", "dist", "**/*spec.ts"]
}
```

#### File: `frontend/tsconfig.json`
```python
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
```

#### File: `railway.json`
```python
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "npm run start:prod",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100
  }
}
```

#### File: `nest-cli.json`
```python
{
  "$schema": "https://json.schemastore.org/nest-cli",
  "collection": "@nestjs/schematics",
  "sourceRoot": "src",
  "compilerOptions": {
    "deleteOutDir": true
  }
}
```

#### File: `test/jest-e2e.json`
```python
{
  "moduleFileExtensions": ["js", "json", "ts"],
  "rootDir": ".",
  "testEnvironment": "node",
  "testRegex": ".e2e-spec.ts$",
  "transform": {
    "^.+\\.(t|j)s$": "ts-jest"
  }
}
```

#### File: `frontend/vercel.json`
```python
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "*"
        }
      ]
    }
  ]
}
```


==================================================


## [2/3] Repository: Indian-Stock-Markets (`VAULT_IN-QUANT-087_vijayshinva__Indian-Stock-Markets`)
- **Full Name**: `IN-QUANT-087_vijayshinva__Indian-Stock-Markets`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Indian-Stock-Markets
![PyPI](https://img.shields.io/pypi/v/indian-stock-markets) ![PyPI - Format](https://img.shields.io/pypi/format/indian-stock-markets) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/indian-stock-markets)

[![Build Status](https://travis-ci.org/vijayshinva/Indian-Stock-Markets.svg?branch=master)](https://travis-ci.org/vijayshinva/Indian-Stock-Markets) [![CodeFactor](https://www.codefactor.io/repository/github/vijayshinva/indian-stock-markets/badge)](https://www.codefactor.io/repository/github/vijayshinva/indian-stock-markets) [![Coverage Status](https://coveralls.io/repos/github/vijayshinva/Indian-Stock-Markets/badge.svg?branch=master)](https://coveralls.io/github/vijayshinva/Indian-Stock-Markets?branch=master)

A Python package for analyzing Indian Stock Markets



## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fvijayshinva%2FIndian-Stock-Markets.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fvijayshinva%2FIndian-Stock-Markets?ref=badge_shield)

Copyright 2019 Vijayshinva B Karnure

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### Core Implementation Code & Architecture
#### File: `src/tests/__init__.py`
```python

```

#### File: `src/indian_stock_markets/__init__.py`
```python
name = 'indian_stock-markets'
```

#### File: `src/indian_stock_markets/nse/__init__.py`
```python
from indian_stock_markets.nse.bhavcopy import BhavCopy
from indian_stock_markets.nse.nse import Nse
from indian_stock_markets.nse.futstk import FutStk
```

#### File: `src/tests/test_futstk.py`
```python
import unittest
import sys
sys.path.append(".")

from indian_stock_markets.nse import BhavCopy


class TestFutStk(unittest.TestCase):
    def test_open(self):
        pass
```

#### File: `src/setup.py`
```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="indian_stock_markets",
                 version="0.0.6",
                 author="Vijayshinva B Karnure",
                 author_email="vijayshinva@outlook.com",
                 description="A Python package for analyzing Indian Stock Markets",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/vijayshinva/Indian-Stock-Markets",
                 packages=setuptools.find_packages(),
                 include_package_data=True,
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: Apache Software License",
                              "Operating System :: OS Independent", ],
                 python_requires='>=3.6',
                 install_requires=[
                     'requests',
                     'pandas'
                 ])
```

#### File: `src/tests/test_nse.py`
```python
from indian_stock_markets.nse import Nse
from datetime import date
import sqlite3
import unittest
import sys
import os

sys.path.append(".")


class TestFutStk(unittest.TestCase):

    def test_tables(self):
        with Nse() as nse:
            db = sqlite3.connect('nse.db')
            cursor = db.cursor()
            cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
            tables = cursor.fetchall()
            self.assertTrue(any('FUTIDX' in t for t in tables))
            self.assertTrue(any('FUTSTK' in t for t in tables))
            self.assertTrue(any('OPTIDX' in t for t in tables))
            self.assertTrue(any('OPTSTK' in t for t in tables))
            cursor.close()
            db.close()

    def test_load(self):
        with Nse() as nse:
            nse.load(date(2019, 9, 2), date(2019, 9, 3))

    def tearDown(self):
        try:
            os.remove('nse.db')
            os.removedirs('content')
            os.removedirs('archive')
        except OSError as e:
            print("Error: ", e.strerror)
```


==================================================


## [3/3] Repository: nse-data (`VAULT_IN-QUANT-088_joshiadvait8__nse-data`)
- **Full Name**: `IN-QUANT-088_joshiadvait8__nse-data`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Core Implementation Code & Architecture
#### File: `app.py`
```python
from bs4 import BeautifulSoup
import requests

headers = {
    'Host': 'www1.nseindia.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'
}

def getprice(symbol):
    url = 'https://www.nse-india.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?&symbol='+symbol+'&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17'
    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html,'lxml')
    l=soup.select('div#container >div.content_big>div#wrapper_btm>table span b')
    price = l[0].text.split()
    print(l[0].text)
    # Actual price of equity derivative
    print(price[1])
    # print(l[0].text)
    # print(l[1].text)

def get_values_from_option_chain(symbol):

    # Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=" + expdate
    Base_url = f'https://www.nse-india.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?&symbol={symbol}&instrument=OPTSTK&date=-&segmentLink=17&segmentLink=17'
    page = requests.get(Base_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_cls_2 = soup.find(id="octable")
    req_row = table_cls_2.find_all('tr')

    strike_price_list = []
    OI_calls_list = []
    OI_puts_list =[]

    for row_number, tr_nos in enumerate(req_row):
        # print(row_number)
        # print(tr_nos)
        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row) - 1:
            continue

        td_columns = tr_nos.find_all('td')
        # print(BeautifulSoup(str(td_columns[11]),'html.parser').get_text())

        #append strike price
        strike_price = int(float(BeautifulSoup(str(td_columns[11]), 'html.parser').get_text()))
        strike_price_list.append(strike_price)
        #append oi calls
        OI_calls = BeautifulSoup(str(td_columns[1]), 'html.parser').get_text()
        OI_calls_list.append(OI_calls)
        #append oi puts
        OI_puts = BeautifulSoup(str(td_columns[21]), 'html.parser').get_text()
        OI_puts_list.append(OI_puts)
        
    # print()
    # print("-------------strike_price-------------")
    # print (strike_price_list)
    # print("*****OI Calls******")
    # print(OI_calls_list)
    # print("*****OI puts******")
    # print(OI_puts_list)
    return strike_price_list

get_values_from_option_chain('INFY')
getprice('INFY')
```

#### File: `NSE_option_chain_to excel.py`
```python
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
import xlwt 
from xlwt import Workbook 


def get_strike_price_from_option_chain(symbol, expdate):
# Workbook is created 
    wb = Workbook() 
    sheet1 = wb.add_sheet('Sheet 1')
    Base_url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=" + expdate
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
          "X-Requested-With": "XMLHttpRequest"}

    page = requests.get(Base_url,headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_cls_2 = soup.find(id="octable")
    req_row = table_cls_2.find_all('tr')

    strike_price_list = []
    calls_OI_list = []
    calls_OI_change_list = []
    puts_OI_list = []
    puts_OI_change_list = []
    

    for row_number, tr_nos in enumerate(req_row):

        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row) - 1:
            continue

        td_columns = tr_nos.find_all('td')
        
        strike_price = int(float(BeautifulSoup(str(td_columns[11]), 'html.parser').get_text()))
        strike_price_list.append(strike_price)
        
        calls_OI = (BeautifulSoup(str(td_columns[1]), 'html.parser').get_text())
        if calls_OI=='-':
            calls_OI=0
        calls_OI_list.append(calls_OI)
        calls_OI_change = (BeautifulSoup(str(td_columns[2]), 'html.parser').get_text())
        calls_OI_change_list.append(calls_OI_change)
        
        puts_OI = (BeautifulSoup(str(td_columns[21]), 'html.parser').get_text())
        puts_OI_list.append(puts_OI)
        puts_OI_change = (BeautifulSoup(str(td_columns[20]), 'html.parser').get_text())
        puts_OI_change_list.append(puts_OI_change)
#         #print ("Number of items in the list = ",len(calls_OI_list))
#         j = len(calls_OI_list)
# #         print (j)
#         i=len(calls_OI_list)
        
# #     print (i)
    
    
    print ("Strike Price",strike_price_list)
    print ("CALLS OI",calls_OI_list)
#     print ("Change In CALLS OI",calls_OI_change_list)
#     print ("PUTS OI",puts_OI_list)
#     print ("Change In PUTS OI",puts_OI_change_list)    
      
#     for idx in range(len(strike_price_list)):
#         print(strike_price_list[10])
#         sheet1.write(idx, 0, strike_price_list[idx])
#         sheet1.write(idx, 0, idx)

    sheet1.write(0, 0, "calls_OI_list")
    sheet1.write(0, 1, "calls_OI_change_list")
    sheet1.write(0, 2, "strike_price_list")
    sheet1.write(0, 3, "puts_OI_change_list")
    sheet1.write(0, 4, "puts_OI_list")

    for x in range(len(strike_price_list)):
        sheet1.write(x+1, 0, calls_OI_list[x])
        sheet1.write(x+1, 1, calls_OI_change_list[x])
        sheet1.write(x+1, 2, strike_price_list[x])
        sheet1.write(x+1, 3, puts_OI_change_list[x])
        sheet1.write(x+1, 4, puts_OI_list[x])
   
    wb.save(r"C:\Users\Personal\Desktop\FNO\\"+symbol+".xls") 
        
# here end of functionbasically


f = open(r'FNO.csv')
lines = [line.strip() for line in f]
# print(lines[1])
for i in range(1,len(lines)):
    print(lines[i])
    get_strike_price_from_option_chain(lines[i], "30APR2020")
    
    
        
# wait apan pahile fakt 5 script taky karan 144 loopmadhe
#     wb.save(i.xls) 
#     sheet1 = wb.add_sheet(symbol[]) 
        #print(symbol[row])
#     get_strike_price_from_option_chain(symbol[i], "30APR2020")
```


==================================================
