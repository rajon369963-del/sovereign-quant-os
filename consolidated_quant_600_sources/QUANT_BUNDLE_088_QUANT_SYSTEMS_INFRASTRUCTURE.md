# ⚡ [QUANT-SOURCE-088] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_088_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: zvt (`PHASE4-QUANT-016`)
- **Full Name**: `PHASE4-QUANT-016_zvtvz__zvt`
- **Description**: modular quant framework.
- **GitHub Stars**: 4304
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
[![github](https://img.shields.io/github/stars/zvtvz/zvt.svg)](https://github.com/zvtvz/zvt)
[![image](https://img.shields.io/pypi/v/zvt.svg)](https://pypi.org/project/zvt/)
[![image](https://img.shields.io/pypi/l/zvt.svg)](https://pypi.org/project/zvt/)
[![image](https://img.shields.io/pypi/pyversions/zvt.svg)](https://pypi.org/project/zvt/)
[![build](https://github.com/zvtvz/zvt/actions/workflows/build.yaml/badge.svg)](https://github.com/zvtvz/zvt/actions/workflows/build.yml)
[![package](https://github.com/zvtvz/zvt/actions/workflows/package.yaml/badge.svg)](https://github.com/zvtvz/zvt/actions/workflows/package.yaml)
[![Documentation Status](https://readthedocs.org/projects/zvt/badge/?version=latest)](https://zvt.readthedocs.io/en/latest/?badge=latest)
[![codecov.io](https://codecov.io/github/zvtvz/zvt/coverage.svg?branch=master)](https://codecov.io/github/zvtvz/zvt)
[![Downloads](https://pepy.tech/badge/zvt/month)](https://pepy.tech/project/zvt)

**The origin of ZVT**

[The Three Major Principles of Stock Trading](https://mp.weixin.qq.com/s/FoFR63wFSQIE_AyFubkZ6Q)

**Declaration**

This project does not currently guarantee any backward compatibility, so please upgrade with caution.    
As the author's thoughts evolve, some things that were once considered important may become less so, and thus may not be maintained.    
Whether the addition of some new elements will be useful to you needs to be assessed by yourself.

**Read this in other languages: [中文](README-cn.md).**  

**Read the docs:[https://zvt.readthedocs.io/en/latest/](https://zvt.readthedocs.io/en/latest/)**

### Install
```
python3 -m pip install -U zvt
```

### Main ui

#### Dash & Plotly UI

> It's good for backtest and research, but it is not applicable for real-time market data and user interaction.

After the installation is complete, enter zvt on the command line
```shell
zvt
```
open [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

> The example shown here relies on data, factor, trader, please read [docs](https://zvt.readthedocs.io/en/latest/)

<p align="center"><img src='https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/zvt-factor.png'/></p>
<p align="center"><img src='https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/zvt-trader.png'/></p>

> The core concept of the system is visual, and the name of the interface corresponds to it one-to-one, so it is also uniform and extensible.

> You can write and run the strategy in your favorite ide, and then view its related targets, factor, signal and performance on the UI.

#### Rest api and standalone UI
> It is more flexible and more scalable, more suitable for handling real-time market data and user interaction. 
> Combined with the dynamic tag system provided by ZVT, it offers a trading approach that combines AI with human intervention.

- Init tag system

run following scripts:  

https://github.com/zvtvz/zvt/blob/master/src/zvt/tasks/init_tag_system.py
https://github.com/zvtvz/zvt/blob/master/src/zvt/tasks/stock_pool_runner.py
https://github.com/zvtvz/zvt/blob/master/src/zvt/tasks/qmt_data_runner.py
https://github.com/zvtvz/zvt/blob/master/src/zvt/tasks/qmt_tick_runner.py

- Install uvicorn
```shell
pip install uvicorn
```
- Run zvt server

After the installation is complete, enter zvt_server on the command line
```shell
zvt_server
```
Or run it from source code:
https://github.com/zvtvz/zvt/blob/master/src/zvt/zvt_server.py

- Check the api docs 

open [http://127.0.0.1:8090/docs](http://127.0.0.1:8090/docs)

- Deploy the front end service

Front end source code: https://github.com/zvtvz/zvt_ui

Change the env file:
https://github.com/zvtvz/zvt_ui/blob/main/.env

Set {your server IP} to zvt_server IP

```text
NEXT_PUBLIC_SERVER = {your server IP}
```

Then refer to the frontend's README to start the frontend service.

open [http://127.0.0.1:3000/trade](http://127.0.0.1:3000/trade)

<p align="center"><img src='https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/big-picture.jpg'/></p>

### Behold, the power of zvt:
```
>>> from zvt.domain import Stock, Stock1dHfqKdata
>>> from zvt.ml import MaStockMLMachine
>>> Stock.record_data(provider="em")
>>> entity_ids = ["stock_sz_000001", "stock_sz_000338", "stock_sh_601318"]
>>> Stock1dHfqKdata.record_data(provider="em", entity_ids=entity_ids, sleeping_time=1)
>>> machine = MaStockMLMachine(entity_ids=["stock_sz_000001"], data_provider="em")
>>> machine.train()
>>> machine.predict()
>>> machine.draw_result(entity_id="stock_sz_000001")
```
<p align="center"><img src='https://raw.githubusercontent.com/zvtvz/zvt/master/docs/imgs/pred_close.png'/></p>

> The few lines of code above has done: data capture, persistence, incremental update, machine learning, prediction, and display results.
> Once you are familiar with the core concepts of the system, you can apply it to any target in the market.

### Data

#### China stock
```
>>> from zvt.domain import *
>>> Stock.record_data(provider="em")
>>> df = Stock.query_data(provider="em", index='code')
>>> print(df)

                     id        entity_id  timestamp entity_type exchange    code   name  list_date end_date
code
000001  stock_sz_000001  stock_sz_000001 1991-04-03       stock       sz  000001   平安银行 1991-04-03     None
000002  stock_sz_000002  stock_sz_000002 1991-01-29       stock       sz  000002  万  科Ａ 1991-01-29     None
000004  stock_sz_000004  stock_sz_000004 1990-12-01       stock       sz  000004   国华网安 1990-12-01     None
000005  stock_sz_000005  stock_sz_000005 1990-12-10       stock       sz  000005   世纪星源 1990-12-10     None
000006  stock_sz_000006  stock_sz_000006 1992-04-27       stock       sz  000006   深振业Ａ 1992-04-27     None
...                 ...              ...        ...         ...      ...     ...    ...        ...      ...
605507  stock_sh_605507  stock_sh_605507 2021-08-02       stock       sh  605507   国邦医药 2021-08-02     None
605577  stock_sh_605577  stock_sh_605577 2021-08-24       stock       sh  605577   龙版传媒 2021-08-24     None
605580  stock_sh_605580  stock_sh_605580 2021-08-19       stock       sh  605580   恒盛能源 2021-08-19     None
605588  stock_sh_605588  stock_sh_605588 2021-08-12       stock       sh  605588   冠石科技 2021-08-12     None
605589  stock_sh_605589  stock_sh_605589 2021-08-10       stock       sh  605589   圣泉集团 2021-08-10     None

[4136 rows x 9 columns]
```

#### USA stock
```
>>> Stockus.record_data()
>>> df = Stockus.query_data(index='code')
>>> print(df)

                       id            entity_id timestamp entity_type exchange  code                         name list_date end_date
code
A          stockus_nyse_A       stockus_nyse_A       NaT     stockus     nyse     A                          安捷伦      None     None
AA        stockus_nyse_AA      stockus_nyse_AA       NaT     stockus     nyse    AA                         美国铝业      None     None
AAC      stockus_nyse_AAC     stockus_nyse_AAC       NaT     stockus     nyse   AAC      Ares Acquisition Corp-A      None     None
AACG  stockus_nasdaq_AACG  stockus_nasdaq_AACG       NaT     stockus   nasdaq  AACG    ATA Creativity Global ADR      None     None
AACG    stockus_nyse_AACG    stockus_nyse_AACG       NaT     stockus     nyse  AACG    ATA Creativity Global ADR      None     None
...                   ...                  ...       ...         ...      ...   ...                          ...       ...      ...
ZWRK  stockus_nasdaq_ZWRK  stockus_nasdaq_ZWRK       NaT     stockus   nasdaq  ZWRK    Z-Work Acquisition Corp-A      None     None
ZY      stockus_nasdaq_ZY    stockus_nasdaq_ZY       NaT     stockus   nasdaq    ZY                 Zymergen Inc      None     None
ZYME    stockus_nyse_ZYME    stockus_nyse_ZYME       NaT     stockus     nyse  ZYME                Zymeworks Inc      None     None
ZYNE  stockus_nasdaq_ZYNE  stockus_nasdaq_ZYNE       NaT     stockus   nasdaq  ZYNE  Zynerba Pharmaceuticals Inc      None     None
ZYXI  stockus_nasdaq_ZYXI  stockus_nasdaq_ZYXI       NaT     stockus   nasdaq  ZYXI                    Zynex Inc      None     None

[5826 rows x 9 columns]

>>> Stockus.query_data(code='AAPL')
                    id            entity_id timestamp entity_type exchange  code name list_date end_date
0  stockus_nasdaq_AAPL  stockus_nasdaq_AAPL      None     stockus   nasdaq  AAPL   苹果      None     None
```

#### Hong Kong stock
```
>>> Stockhk.record_data()
>>> df = Stockhk.query_data(index='code')
>>> print(df)

                     id         entity_id timestamp entity_type exchange   code    name list_date end_date
code
00001  stockhk_hk_00001  stockhk_hk_00001       NaT     stockhk       hk  00001      长和      None     None
00002  stockhk_hk_00002  stockhk_hk_00002       NaT     stockhk       hk  00002    中电控股      None     None
00003  stockhk_hk_00003  stockhk_hk_00003       NaT     stockhk       hk  00003  香港中华煤气      None     None
00004  stockhk_hk_00004  stockhk_hk_00004       NaT     stockhk       hk  00004   九龙仓集团      None     None
00005  stockhk_hk_00005  stockhk_hk_00005       NaT     stockhk       hk  00005    汇丰控股      None     None
...                 ...               ...       ...         ...      ...    ...     ...       ...      ...
09996  stockhk_hk_09996  stockhk_hk_09996       NaT     stockhk       hk  09996  沛嘉医疗-B      None     None
09997  stockhk_hk_09997  stockhk_hk_09997       NaT     stockhk       hk  09997    康基医疗      None     None
09998  stockhk_hk_09998  stockhk_hk_09998       NaT     stockhk       hk  09998    光荣控股      None     None
09999  stockhk_hk_09999  stockhk_hk_09999       NaT     stockhk       hk  09999    网易-S      None     None
80737  stockhk_hk_80737  stockhk_hk_80737       NaT     stockhk       hk  80737  湾区发展-R      None     None

[2597 rows x 9 columns]

>>> df[df.code=='00700']

                    id         entity_id timestamp entity_type exchange   code  name list_date end_date
2112  stockhk_hk_00700  stockhk_hk_00700      None     stockhk       hk  00700  腾讯控股      None     None

```

#### And more
```
>>> from zvt.contract import *
>>> zvt_context.tradable_schema_map

{'stockus': zvt.domain.meta.stockus_meta.Stockus,
 'stockhk': zvt.domain.meta.stockhk_meta.Stockhk,
 'index': zvt.domain.meta.index_meta.Index,
 'etf': zvt.domain.meta.etf_meta.Etf,
 'stock': zvt.domain.meta.stock_meta.Stock,
 'block': zvt.domain.meta.block_meta.Block,
 'fund': zvt.domain.meta.fund_meta.Fund}
```

The key is tradable entity type, and the value is the schema. The system provides unified **record (record_data)** and **query (query_data)** methods for the schema.

```
>>> Index.record_data()
>>> df=Index.query_data(filters=[Index.category=='scope',Index.exchange='sh'])
>>> print(df)
                 id        entity_id  timestamp entity_type exchange    code    name  list_date end_date publisher category  base_point
0   index_sh_000001  index_sh_000001 1990-12-19       index       sh  000001    上证指数 1991-07-15     None   csindex    scope      100.00
1   index_sh_000002  index_sh_000002 1990-12-19       index       sh  000002    Ａ股指数 1992-02-21     None   csindex    scope      100.00
2   index_sh_000003  index_sh_000003 1992-02-21       index       sh  000003    B股指数 1992-08-17     None   csindex    scope      100.00
3   index_sh_000010  index_sh_000010 2002-06-28       index       sh  000010   上证180 2002-07-01     None   csindex    scope     3299.06
4   index_sh_000016  index_sh_000016 2003-12-31       index       sh  000016    上证50 2004-01-02     None   csindex    scope     1000.00
..              ...              ...        ...         ...      ...     ...     ...        ...      ...       ...      ...         ...
25  index_sh_000020  index_sh_000020 2007-12-28       index       sh  000020    中型综指 2008-05-12     None   csindex    scope     1000.00
26  index_sh_000090  index_sh_000090 2009-12-31       index       sh  000090    上证流通 2010-12-02     None   csindex    scope     1000.00
27  index_sh_930903  index_sh_930903 2012-12-31       index       sh  930903    中证Ａ股 2016-10-18     None   csindex    scope     1000.00
28  index_sh_000688  index_sh_000688 2019-12-31       index       sh  000688    科创50 2020-07-23     None   csindex    scope     1000.00
29  index_sh_931643  index_sh_931643 2019-12-31       index       sh  931643  科创创业50 2021-06-01     None   csindex    scope     1000.00

[30 rows x 12 columns]

```

### EntityEvent
We have tradable entity and then events about them.

#### Market quotes
the TradableEntity quote schema follows the following rules:
```
{entity_shema}{level}{adjust_type}Kdata
```
* entity_schema

TradableEntity class，e.g., Stock,Stockus.

* level
```
>>> for level in IntervalLevel:
        print(level.value)
```

* adjust type
```
>>> for adjust_type in AdjustType:
        print(adjust_type.value)
```

> Note: In order to be compatible with historical data, the pre-reset is an exception, {adjust_type} is left empty

qfq
```
>>> Stock1dKdata.record_data(code='000338', provider='em')
>>> df = Stock1dKdata.query_data(code='000338', provider='em')
>>> print(df)

                              id        entity_id  timestamp provider    code  name level   open  close   high    low     volume      turnover  change_pct  turnover_rate
0     stock_sz_000338_2007-04-30  stock_sz_000338 2007-04-30     None  000338  潍柴动力    1d   2.33   2.00   2.40   1.87   207375.0  1.365189e+09      3.2472         0.1182
1     stock_sz_000338_2007-05-08  stock_sz_000338 2007-05-08     None  000338  潍柴动力    1d   2.11   1.94   2.20   1.87    86299.0  5.563198e+08     -0.0300         0.0492
2     stock_sz_000338_2007-05-09  stock_sz_000338 2007-05-09     None  000338  潍柴动力    1d   1.90   1.81   1.94   1.66    93823.0  5.782065e+08     -0.0670         0.0535
3     stock_sz_000338_2007-05-10  stock_sz_000338 2007-05-10     None  000338  潍柴动力    1d   1.78   1.85   1.98   1.75    47720.0  2.999226e+08      0.0221         0.0272
4     stock_sz_000338_2007-05-11  stock_sz_000338 2007-05-11     None  000338  潍柴动力    1d   1.81   1.73   1.81   1.66    39273.0  2.373126e+08     -0.0649         0.0224
...                          ...              ...        ...      ...     ...   ...   ...    ...    ...    ...    ...        ...           ...         ...            ...
3426  stock_sz_000338_2021-08-27  stock_sz_000338 2021-08-27     None  000338  潍柴动力    1d  19.39  20.30  20.30  19.25  1688497.0  3.370241e+09      0.0601         0.0398
3427  stock_sz_000338_2021-08-30  stock_sz_000338 2021-08-30     None  000338  潍柴动力    1d  20.30  20.09  20.31  19.78  1187601.0  2.377957e+09     -0.0103         0.0280
3428  stock_sz_000338_2021-08-31  stock_sz_000338 2021-08-31     None  000338  潍柴动力    1d  20.20  20.07  20.63  19.70  1143985.0  2.295195e+09     -0.0010         0.0270
3429  stock_sz_000338_2021-09-01  stock_sz_000338 2021-09-01     None  000338  潍柴动力    1d  19.98  19.68  19.98  19.15  1218697.0  2.383841e+09     -0.0194         0.0287
3430  stock_sz_000338_2021-09-02  stock_sz_000338 2021-09-02     None  000338  潍柴动力    1d  19.71  19.85  19.97  19.24  1023545.0  2.012006e+09      0.0086         0.0241

[3431 rows x 15 columns]

>>> Stockus1dKdata.record_data(code='AAPL', provider='em')
>>> df = Stockus1dKdata.query_data(code='AAPL', provider='em')
>>> print(df)

                                  id            entity_id  timestamp provider  code name level    open   close    high     low      volume      turnover  change_pct  turnover_rate
0     stockus_nasdaq_AAPL_1984-09-07  stockus_nasdaq_AAPL 1984-09-07     None  AAPL   苹果    1d   -5.59   -5.59   -5.58   -5.59   2981600.0  0.000000e+00      0.0000         0.0002
1     stockus_nasdaq_AAPL_1984-09-10  stockus_nasdaq_AAPL 1984-09-10     None  AAPL   苹果    1d   -5.59   -5.59   -5.58   -5.59   2346400.0  0.000000e+00      0.0000         0.0001
2     stockus_nasdaq_AAPL_1984-09-11  stockus_nasdaq_AAPL 1984-09-11     None  AAPL   苹果    1d   -5.58   -5.58   -5.58   -5.58   5444000.0  0.000000e+00      0.0018         0.0003
3     stockus_nasdaq_AAPL_1984-09-12  stockus_nasdaq_AAPL 1984-09-12     None  AAPL   苹果    1d   -5.58   -5.59   -5.58   -5.59   4773600.0  0.000000e+00     -0.0018         0.0003
4     stockus_nasdaq_AAPL_1984-09-13  stockus_nasdaq_AAPL 1984-09-13     None  AAPL   苹果    1d   -5.58   -5.58   -5.58   -5.58   7429600.0  0.000000e+00      0.0018         0.0004
...                              ...                  ...        ...      ...   ...  ...   ...     ...     ...     ...     ...         ...           ...         ...            ...
8765  stockus_nasdaq_AAPL_2021-08-27  stockus_nasdaq_AAPL 2021-08-27     None  AAPL   苹果    1d  147.48  148.60  148.75  146.83  55802388.0  8.265452e+09      0.0072         0.0034
8766  stockus_nasdaq_AAPL_2021-08-30  stockus_nasdaq_AAPL 2021-08-30     None  AAPL   苹果    1d  149.00  153.12  153.49  148.61  90956723.0  1.383762e+10      0.0304         0.0055
8767  stockus_nasdaq_AAPL_2021-08-31  stockus_nasdaq_AAPL 2021-08-31     None  AAPL   苹果    1d  152.66  151.83  152.80  151.29  86453117.0  1.314255e+10     -0.0084         0.0052
8768  stockus_nasdaq_AAPL_2021-09-01  stockus_nasdaq_AAPL 2021-09-01     None  AAPL   苹果    1d  152.83  152.51  154.98  152.34  80313711.0  1.235321e+10      0.0045         0.0049
8769  stockus_nasdaq_AAPL_2021-09-02  stockus_nasdaq_AAPL 2021-09-02     None  AAPL   苹果    1d  153.87  153.65  154.72  152.40  71171317.0  1.093251e+10      0.0075         0.0043

[8770 rows x 15 columns]
```

hfq
```
>>> Stock1dHfqKdata.record_data(code='000338', provider='em')
>>> df = Stock1dHfqKdata.query_data(code='000338', provider='em')
>>> print(df)

                              id        entity_id  timestamp provider    code  name level    open   close    high     low     volume      turnover  change_pct  turnover_rate
0     stock_sz_000338_2007-04-30  stock_sz_000338 2007-04-30     None  000338  潍柴动力    1d   70.00   64.93   71.00   62.88   207375.0  1.365189e+09      2.1720         0.1182
1     stock_sz_000338_2007-05-08  stock_sz_000338 2007-05-08     None  000338  潍柴动力    1d   66.60   64.00   68.00   62.88    86299.0  5.563198e+08     -0.0143         0.0492
2     stock_sz_000338_2007-05-09  stock_sz_000338 2007-05-09     None  000338  潍柴动力    1d   63.32   62.00   63.88   59.60    93823.0  5.782065e+08     -0.0313         0.0535
3     stock_sz_000338_2007-05-10  stock_sz_000338 2007-05-10     None  000338  潍柴动力    1d   61.50   62.49   64.48   61.01    47720.0  2.999226e+08      0.0079         0.0272
4     stock_sz_000338_2007-05-11  stock_sz_000338 2007-05-11     None  000338  潍柴动力    1d   61.90   60.65   61.90   59.70    39273.0  2.373126e+08     -0.0294         0.0224
...                          ...              ...        ...      ...     ...   ...   ...     ...     ...     ...     ...        ...           ...         ...            ...
3426  stock_sz_000338_2021-08-27  stock_sz_000338 2021-08-27     None  000338  潍柴动力    1d  331.97  345.95  345.95  329.82  1688497.0  3.370241e+09      0.0540         0.0398
3427  stock_sz_000338_2021-08-30  stock_sz_000338 2021-08-30     None  000338  潍柴动力    1d  345.95  342.72  346.10  337.96  1187601.0  2.377957e+09     -0.0093         0.0280
3428  stock_sz_000338_2021-08-31  stock_sz_000338 2021-08-31     None  000338  潍柴动力    1d  344.41  342.41  351.02  336.73  1143985.0  2.295195e+09     -0.0009         0.0270
3429  stock_sz_000338_2021-09-01  stock_sz_000338 2021-09-01     None  000338  潍柴动力    1d  341.03  336.42  341.03  328.28  1218697.0  2.383841e+09     -0.0175         0.0287
3430  stock_sz_000338_2021-09-02  stock_sz_000338 2021-09-02     None  000338  潍柴动力    1d  336.88  339.03  340.88  329.67  1023545.0  2.012006e+09      0.0078         0.0241

[3431 rows x 15 columns]
```

#### Finance factor
```
>>> FinanceFactor.record_data(code='000338')
>>> FinanceFactor.query_data(code='000338',columns=FinanceFactor.important_cols(),index='timestamp')

            basic_eps  total_op_income    net_profit  op_income_growth_yoy  net_profit_growth_yoy     roe    rota  gross_profit_margin  net_margin  timestamp
timestamp
2002-12-31        NaN     1.962000e+07  2.471000e+06                   NaN                    NaN     NaN     NaN               0.2068      0.1259 2002-12-31
2003-12-31       1.27     3.574000e+09  2.739000e+08              181.2022               109.8778  0.7729  0.1783               0.2551      0.0766 2003-12-31
2004-12-31       1.75     6.188000e+09  5.369000e+08                0.7313                 0.9598  0.3245  0.1474               0.2489      0.0868 2004-12-31
2005-12-31       0.93     5.283000e+09  3.065000e+08               -0.1463                -0.4291  0.1327  0.0603               0.2252      0.0583 2005-12-31
2006-03-31       0.33     1.859000e+09  1.079000e+08                   NaN                    NaN     NaN     NaN                  NaN      0.0598 2006-03-31
...               ...              ...           ...                   ...                    ...     ...     ...                  ...         ...        ...
2020-08-28       0.59     9.449000e+10  4.680000e+09                0.0400                -0.1148  0.0983  0.0229               0.1958      0.0603 2020-08-28
2020-10-31       0.90     1.474000e+11  7.106000e+09                0.1632                 0.0067  0.1502  0.0347               0.1949      0.0590 2020-10-31
2021-03-31       1.16     1.975000e+11  9.207000e+09                0.1327                 0.0112  0.1919  0.0444               0.1931      0.0571 2021-03-31
2021-04-30       0.42     6.547000e+10  3.344000e+09                0.6788                 0.6197  0.0622  0.0158               0.1916      0.0667 2021-04-30
2021-08-31       0.80     1.264000e+11  6.432000e+09                0.3375                 0.3742  0.1125  0.0287               0.1884      0.0653 2021-08-31

[66 rows x 10 columns]
```

#### Three financial tables
```
>>> BalanceSheet.record_data(code='000338')
>>> IncomeStatement.record_data(code='000338')
>>> CashFlowStatement.record_data(code='000338')
```

#### And more
```
>>> zvt_context.schemas
[zvt.domain.dividend_financing.DividendFinancing,
 zvt.domain.dividend_financing.DividendDetail,
 zvt.domain.dividend_financing.SpoDetail...]
```

All schemas is registered in zvt_context.schemas, **schema** is table, data structure.
The fields and meaning could be checked in following ways:

* help

type the schema. and press tab to show its fields or .help()
```
>>> FinanceFactor.help()
```

* source code

Schemas defined in [domain](https://github.com/zvtvz/zvt/tree/master/src/zvt/domain)

From above examples, you should know the unified way of recording data:

> Schema.record_data(provider='your provider',codes='the codes')

Note the optional parameter provider, which represents the data provider. 
A schema can have multiple providers, which is the cornerstone of system stability.

Check the provider has been implemented:
```
>>> Stock.provider_map_recorder
{'joinquant': zvt.recorders.joinquant.meta.jq_stock_meta_recorder.JqChinaStockRecorder,
 'exchange': zvt.recorders.exchange.exchange_stock_meta_recorder.ExchangeStockMetaRecorder,
 'em': zvt.recorders.em.meta.em_stock_meta_recorder.EMStockRecorder,
 'eastmoney': zvt.recorders.eastmoney.meta.eastmoney_stock_meta_recorder.EastmoneyChinaStockListRecorder}

```
You can use any provider to get the data, the first one is used by default.

One more example, the stock sector data recording:
```
>>> Block.provider_map_recorder
{'eastmoney': zvt.recorders.eastmoney.meta.eastmoney_block_meta_recorder.EastmoneyChinaBlockRecorder,
 'sina': zvt.recorders.sina.meta.sina_block_recorder.SinaBlockRecorder}

>>> Block.record_data(provider='sina')
Block registered recorders:{'eastmoney': <class 'zvt.recorders.eastmoney.meta.china_stock_category_recorder.EastmoneyChinaBlockRecorder'>, 'sina': <class 'zvt.recorders.sina.meta.sina_china_stock_category_recorder.SinaChinaBlockRecorder'>}
2020-03-04 23:56:48,931  INFO  MainThread  finish record sina blocks:industry
2020-03-04 23:56:49,450  INFO  MainThread  finish record sina blocks:concept
```

Learn more about record_data

* The parameter code[single], codes[multiple] represent the stock codes to be recorded
* Recording the whole market if not set code, codes
* This method will store the data locally and only do incremental updates

Refer to the scheduling recoding way[data runner](https://github.com/zvtvz/zvt/blob/master/examples/data_runner)

#### Market-wide stock selection

After recording the data of the whole market, you can quickly query the required data locally.

An example: the top 20 stocks with roe>8% and revenue growth>8% in the 2018 annual report
```
>>> df=FinanceFactor.query_data(filters=[FinanceFactor.roe>0.08,FinanceFactor.report_period=='year',FinanceFactor.op_income_growth_yoy>0.08],start_timestamp='2019-01-01',order=FinanceFactor.roe.desc(),limit=20,columns=["code"]+FinanceFactor.important_cols(),index='code')

          code  basic_eps  total_op_income    net_profit  op_income_growth_yoy  net_profit_growth_yoy 
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `examples/result.json`
```python
{}
```

#### File: `src/zvt/resources/missed_industry.json`
```python
[]
```

#### File: `examples/main_line_hidden_tags.json`
```python
[
  "次新股"
]
```

#### File: `tests/contract/__init__.py`
```python
# -*- coding: utf-8 -*-
```

#### File: `tests/trader/__init__.py`
```python
# -*- coding: utf-8 -*-
```

#### File: `tests/factors/__init__.py`
```python
# -*- coding: utf-8 -*-
```


==================================================


## [2/3] Repository: dtale (`PHASE4-QUANT-025`)
- **Full Name**: `PHASE4-QUANT-025_man-group__dtale`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
[![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/Title.png)](https://github.com/man-group/dtale)

* [Live Demo](http://alphatechadmin.pythonanywhere.com)
* [Animated US COVID-19 Deaths By State](http://alphatechadmin.pythonanywhere.com/dtale/charts/3?chart_type=maps&query=date+%3E+%2720200301%27&agg=raw&map_type=choropleth&loc_mode=USA-states&loc=state_code&map_val=deaths&colorscale=Reds&cpg=false&animate_by=date)
* [3D Scatter Chart](http://alphatechadmin.pythonanywhere.com/dtale/charts/4?chart_type=3d_scatter&query=&x=date&z=Col0&agg=raw&cpg=false&y=%5B%22security_id%22%5D)
* [Surface Chart](http://alphatechadmin.pythonanywhere.com/dtale/charts/4?chart_type=surface&query=&x=date&z=Col0&agg=raw&cpg=false&y=%5B%22security_id%22%5D)
* [Network Analysis](http://alphatechadmin.pythonanywhere.com/dtale/network/5?to=to&from=from&group=route_id&weight=)

-----------------

[![CircleCI](https://circleci.com/gh/man-group/dtale.svg?style=shield)](https://circleci.com/gh/man-group/dtale)
[![PyPI Python Versions](https://img.shields.io/pypi/pyversions/dtale.svg)](https://pypi.python.org/pypi/dtale/)
[![PyPI](https://img.shields.io/pypi/v/dtale)](https://pypi.org/project/dtale/)
[![Conda](https://img.shields.io/conda/v/conda-forge/dtale)](https://anaconda.org/conda-forge/dtale)
[![ReadTheDocs](https://readthedocs.org/projects/dtale/badge)](https://dtale.readthedocs.io)
[![codecov](https://codecov.io/gh/man-group/dtale/branch/master/graph/badge.svg)](https://codecov.io/gh/man-group/dtale)
[![Downloads](https://static.pepy.tech/badge/dtale)](https://pepy.tech/project/dtale)
[![Open in VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=flat&logo=visual%20studio%20code&logoColor=white)](https://open.vscode.dev/man-group/dtale)

## What is it?

D-Tale is the combination of a Flask back-end and a React front-end to bring you an easy way to view & analyze Pandas data structures.  It integrates seamlessly with ipython notebooks & python/ipython terminals.  Currently this tool supports such Pandas objects as DataFrame, Series, MultiIndex, DatetimeIndex & RangeIndex.

## Origins

D-Tale was the product of a SAS to Python conversion.  What was originally a perl script wrapper on top of SAS's `insight` function is now a lightweight web client on top of Pandas data structures.

## In The News

 - [4 Libraries that can perform EDA in one line of python code](https://towardsdatascience.com/4-libraries-that-can-perform-eda-in-one-line-of-python-code-b13938a06ae)
 - [React Status](https://react.statuscode.com/issues/204)
 - [KDNuggets](https://www.kdnuggets.com/2020/08/bring-pandas-dataframes-life-d-tale.html)
 - [Man Institute](https://www.man.com/maninstitute/d-tale) (warning: contains deprecated functionality)
 - [Python Bytes](https://pythonbytes.fm/episodes/show/169/jupyter-notebooks-natively-on-your-ipad)
 - [FlaskCon 2020](https://www.youtube.com/watch?v=BNgolmUWBp4&t=33s)
 - [San Diego Python](https://www.youtube.com/watch?v=fLsGur5YqeE&t=29s)
 - [Medium: towards data science](https://towardsdatascience.com/introduction-to-d-tale-5eddd81abe3f)
 - [Medium: Exploratory Data Analysis – Using D-Tale](https://medium.com/da-tum/exploratory-data-analysis-1-4-using-d-tale-99a2c267db79)
 - [EOD Notes: Using python and dtale to analyze correlations](https://www.google.com/amp/s/eod-notes.com/2020/05/07/using-python-and-dtale-to-analyze-correlations/amp/)
 - [Data Exploration is Now Super Easy w/ D-Tale](https://dibyendudeb.com/d-tale-data-exploration-tool/)
 - [Practical Business Python](https://pbpython.com/dataframe-gui-overview.html)

## Tutorials

 - [Pip Install Python YouTube Channel](https://m.youtube.com/watch?v=0RihZNdQc7k&feature=youtu.be)
 - [machine_learning_2019](https://www.youtube.com/watch?v=-egtEUVBy9c)
 - [D-Tale The Best Library To Perform Exploratory Data Analysis Using Single Line Of Code🔥🔥🔥🔥](https://www.youtube.com/watch?v=xSXGcuiEzUc)
 - [Explore and Analyze Pandas Data Structures w/ D-Tale](https://m.youtube.com/watch?v=JUu5IYVGqCg)
 - [Data Preprocessing simplest method 🔥](https://www.youtube.com/watch?v=Q2kMNPKgN4g)

 ## Related Resources

 - [Adventures In Flask While Developing D-Tale](https://github.com/man-group/dtale/blob/master/docs/FlaskCon/FlaskAdventures.md)
 - [Adding Range Selection to react-virtualized](https://github.com/man-group/dtale/blob/master/docs/RANGE_SELECTION.md)
 - [Building Draggable/Resizable Modals](https://github.com/man-group/dtale/blob/master/docs/DRAGGABLE_RESIZABLE_MODALS.md)
 - [Embedding Flask Apps within Streamlit](https://github.com/man-group/dtale/blob/master/docs/EMBEDDED_STREAMLIT.md)

## Contents

- [Where To Get It](#where-to-get-it)
- [Getting Started](#getting-started)
  - [Python Terminal](#python-terminal)
  - [As A Script](#as-a-script)
  - [Jupyter Notebook](#jupyter-notebook)
  - [Jupyterhub w/ Jupyter Server Proxy](#jupyterhub-w-jupyter-server-proxy)
  - [Jupyterhub w/ Kubernetes](https://github.com/man-group/dtale/blob/master/docs/JUPYTERHUB_KUBERNETES.md)
  - [Docker Container](#docker-container)
  - [Google Colab](#google-colab)
  - [Kaggle](#kaggle)
  - [Binder](#binder)
  - [R with Reticulate](#r-with-reticulate)
  - [Startup with No Data](#startup-with-no-data)
  - [Command-line](#command-line)
  - [Custom Command-line Loaders](#custom-command-line-loaders)
  - [Embedding Within Your Own Flask App](https://github.com/man-group/dtale/blob/master/docs/EMBEDDED_FLASK.md)
  - [Embedding Within Your Own Django App](https://github.com/man-group/dtale/blob/master/docs/EMBEDDED_DJANGO.md)
  - [Embedding Within Streamlit](https://github.com/man-group/dtale/blob/master/docs/EMBEDDED_DTALE_STREAMLIT.md)
  - [Running D-Tale On Gunicorn w/ Redis](https://github.com/man-group/dtale/blob/master/docs/GUNICORN_REDIS.md)
  - [Configuration](https://github.com/man-group/dtale/blob/master/docs/CONFIGURATION.md)
  - [Authentication](#authentication)
  - [Predefined Filters](#predefined-filters)
  - [Using Swifter](#using-swifter)
  - [Behavior for Wide Dataframes](#behavior-for-wide-dataframes)
- [UI](#ui)
  - [Dimensions/Ribbon Menu/Main Menu](#dimensionsribbon-menumain-menu)
  - [Header](#header)
  - [Resize Columns](#resize-columns)
  - [Editing Cells](#editing-cells)
  - [Copy Cells Into Clipboard](#copy-cells-into-clipboard)
  - [Main Menu Functions](#main-menu-functions)
    - [XArray Operations](#xarray-operations), [Describe](#describe), [Outlier Detection](#outlier-detection), [Custom Filter](#custom-filter), [Dataframe Functions](#dataframe-functions), [Merge & Stack](#merge--stack), [Summarize Data](#summarize-data), [Duplicates](#duplicates), [Missing Analysis](#missing-analysis), [Correlations](#correlations), [Predictive Power Score](#predictive-power-score), [Heat Map](#heat-map), [Highlight Dtypes](#highlight-dtypes), [Highlight Missing](#highlight-missing), [Highlight Outliers](#highlight-outliers), [Highlight Range](#highlight-range), [Low Variance Flag](#low-variance-flag), [Instances](#instances), [Code Exports](#code-exports), [Export CSV](#export-csv), [Load Data & Sample Datasets](#load-data--sample-datasets), [Refresh Widths](#refresh-widths), [About](#about), [Theme](#theme), [Reload Data](#reload-data), [Unpin/Pin Menu](#unpinpin-menu), [Language](#language), [Shutdown](#shutdown)
  - [Column Menu Functions](#column-menu-functions)
    - [Filtering](#filtering), [Moving Columns](#moving-columns), [Hiding Columns](#hiding-columns), [Delete](#delete), [Rename](#rename), [Replacements](#replacements), [Lock](#lock), [Unlock](#unlock), [Sorting](#sorting), [Formats](#formats), [Describe (Column Analysis)](#describe-column-analysis)
  - [Charts](#charts)
  - [Network Viewer](#network-viewer)
  - [Hotkeys](#hotkeys)
  - [Menu Functions Depending on Browser Dimensions](#menu-functions-depending-on-browser-dimensions)
- [For Developers](#for-developers)
  - [Cloning](#cloning)
  - [Running Tests](#running-tests)
  - [Linting](#linting)
  - [Formatting JS](#formatting-js)
  - [Docker Development](#docker-development)
  - [Adding Language Support](#adding-language-support)
- [Global State/Data Storage](https://github.com/man-group/dtale/blob/master/docs/GLOBAL_STATE.md)
- [Startup Behavior](#startup-behavior)
- [Documentation](#documentation)
- [Dependencies](#dependencies)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Where To get It
The source code is currently hosted on GitHub at:
https://github.com/man-group/dtale

Binary installers for the latest released version are available at the [Python
package index](https://pypi.org/project/dtale) and on conda using [conda-forge](https://github.com/conda-forge/dtale-feedstock).

```sh
# conda
conda install dtale -c conda-forge
# if you want to also use "Export to PNG" for charts
conda install -c plotly python-kaleido
```

```sh
# or PyPI
pip install dtale
```

## Getting Started

|PyCharm|jupyter|
|:------:|:------:|
|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/gifs/dtale_demo_mini.gif)|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/gifs/dtale_ipython.gif)|

### Python Terminal
This comes courtesy of PyCharm
![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/Python_Terminal.png)
Feel free to invoke `python` or `ipython` directly and use the commands in the screenshot above and it should work

#### Issues With Windows Firewall

If you run into issues with viewing D-Tale in your browser on Windows please try making Python public under "Allowed Apps" in your Firewall configuration.  Here is a nice article:
[How to Allow Apps to Communicate Through the Windows Firewall](https://www.howtogeek.com/howto/uncategorized/how-to-create-exceptions-in-windows-vista-firewall/)

#### Additional functions available programmatically
```python
import dtale
import pandas as pd

df = pd.DataFrame([dict(a=1,b=2,c=3)])

# Assigning a reference to a running D-Tale process.
d = dtale.show(df)

# Accessing data associated with D-Tale process.
tmp = d.data.copy()
tmp['d'] = 4

# Altering data associated with D-Tale process
# FYI: this will clear any front-end settings you have at the time for this process (filter, sorts, formatting)
d.data = tmp

# Get raw dataframe w/ any sorting or edits made through the UI
d.data

# Get raw dataframe similar to '.data' along with any filters applied using the UI
d.view_data

# Shutting down D-Tale process
d.kill()

# Using Python's `webbrowser` package it will try and open your server's default browser to this process.
d.open_browser()

# There is also some helpful metadata about the process.
d._data_id  # The process's data identifier.
d._url  # The url to access the process.

d2 = dtale.get_instance(d._data_id)  # Returns a new reference to the instance running at that data_id.

dtale.instances()  # Prints a list of all ids & urls of running D-Tale sessions.

```

#### Duplicate data check
To help guard against users loading the same data to D-Tale multiple times and thus eating up precious memory, we have a loose check for duplicate input data.  The check runs the following:
 * Are row & column count the same as a previously loaded piece of data?
 * Are the names and order of columns the same as a previously loaded piece of data?

If both these conditions are true then you will be presented with an error and a link to the previously loaded data.  Here is an example of how the interaction looks:
![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/Duplicate_data.png)


### As A Script

D-Tale can be run as script by adding `subprocess=False` to your `dtale.show` command.  Here is an example script:
```python
import dtale
import pandas as pd

if __name__ == '__main__':
      dtale.show(pd.DataFrame([1,2,3,4,5]), subprocess=False)
```

### Jupyter Notebook
Within any jupyter (ipython) notebook executing a cell like this will display a small instance of D-Tale in the output cell.  Here are some examples:

|`dtale.show`|assignment|instance|
|:------:|:------:|:------:|
|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/ipython1.png)|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/ipython2.png)|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/ipython3.png)|

If you are running ipython<=5.0 then you also have the ability to adjust the size of your output cell for the most recent instance displayed:

![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/ipython_adjust.png)

One thing of note is that a lot of the modal popups you see in the standard browser version will now open separate browser windows for spacial convienence:

|Column Menus|Correlations|Describe|Column Analysis|Instances|
|:------:|:------:|:------:|:------:|:------:|
|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/Column_menu.png)|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/correlations_popup.png)|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/describe_popup.png)|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/histogram_popup.png)|![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/instances_popup.png)|

### JupyterHub w/ Jupyter Server Proxy

JupyterHub has an extension that allows to proxy port for user, [JupyterHub Server Proxy](https://github.com/jupyterhub/jupyter-server-proxy)

To me it seems like this extension might be the best solution to getting D-Tale running within kubernetes.  Here's how to use it:

```python
import pandas as pd

import dtale
import dtale.app as dtale_app

dtale_app.JUPYTER_SERVER_PROXY = True

dtale.show(pd.DataFrame([1,2,3]))
```

Notice the command `dtale_app.JUPYTER_SERVER_PROXY = True` this will make sure that any D-Tale instance will be served with the jupyter server proxy application root prefix:

`/user/{jupyter username}/proxy/{dtale instance port}/`

One thing to note is that if you try to look at the `_main_url` of your D-Tale instance in your notebook it will not include the hostname or port:

```python
import pandas as pd

import dtale
import dtale.app as dtale_app

dtale_app.JUPYTER_SERVER_PROXY = True

d = dtale.show(pd.DataFrame([1,2,3]))
d._main_url # /user/johndoe/proxy/40000/dtale/main/1
```

 This is because it's very hard to promgramatically figure out the host/port that your notebook is running on.  So if you want to look at `_main_url` please be sure to preface it with:
 
 `http[s]://[jupyterhub host]:[jupyterhub port]`

If for some reason jupyterhub changes their API so that the application root changes you can also override D-Tale's application root by using the `app_root` parameter to the `show()` function:

```python
import pandas as pd

import dtale
import dtale.app as dtale_app

dtale.show(pd.DataFrame([1,2,3]), app_root='/user/johndoe/proxy/40000/`)
```

Using this parameter will only apply the application root to that specific instance so you would have to include it on every call to `show()`.

### JupyterHub w/ Kubernetes

Please read this [post](https://github.com/man-group/dtale/blob/master/docs/JUPYTERHUB_KUBERNETES.md)

### Docker Container

If you have D-Tale installed within your docker container please add the following parameters to your `docker run` command.

**On a Mac**:

```sh
docker run -h `hostname` -p 40000:40000
```

* `-h` this will allow the hostname (and not the PID of the docker container) to be available when building D-Tale URLs
* `-p` access to port 40000 which is the default port for running D-Tale

**On Windows**:

```sh
docker run -p 40000:40000
```

* `-p` access to port 40000 which is the default port for running D-Tale
* D-Tale URL will be http://127.0.0.1:40000/

**Everything Else**:

```sh
docker run -h `hostname` --network host
```

* `-h` this will allow the hostname (and not the PID of the docker container) to be available when building D-Tale URLs
* `--network host` this will allow access to as many ports as needed for running D-Tale processes

### Google Colab

This is a hosted notebook site and thanks to Colab's internal function `google.colab.output.eval_js` & the JS function `google.colab.kernel.proexyPort` users can run D-Tale within their notebooks.

**DISCLAIMER:** It is important that you set `USE_COLAB` to true when using D-Tale within this service.  Here is an example:

```python
import pandas as pd

import dtale
import dtale.app as dtale_app

dtale_app.USE_COLAB = True

dtale.show(pd.DataFrame([1,2,3]))
```

If this does not work for you try using `USE_NGROK` which is described in the next section.

### Kaggle

This is yet another hosted notebook site and thanks to the work of [flask_ngrok](https://github.com/gstaff/flask-ngrok) users can run D-Tale within their notebooks.

**DISCLAIMER:** It is import that you set `USE_NGROK` to true when using D-Tale within this service.  Please make sure to run `pip install flask-ngrok` before running this example. Here is an example:

```python
import pandas as pd

import dtale
import dtale.app as dtale_app

dtale_app.USE_NGROK = True

dtale.show(pd.DataFrame([1,2,3]))
```

Here are some video tutorials of each:

|Service|Tutorial|Addtl Notes|
|:------:|:------:|:------:|
|Google Colab|[![](http://img.youtube.com/vi/pOYl2M1clIw/0.jpg)](http://www.youtube.com/watch?v=pOYl2M1clIw "Google Colab")||
|Kaggle|[![](http://img.youtube.com/vi/8Il-2HHs2Mg/0.jpg)](http://www.youtube.com/watch?v=8Il-2HHs2Mg "Kaggle")|make sure you switch the "Internet" toggle to "On" under settings of your notebook so you can install the egg from pip|

It is important to note that using NGROK will limit you to 20 connections per mintue so if you see this error:

![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/ngrok_limit.png)

Wait a little while and it should allow you to do work again.  I am actively working on finding a more sustainable solution similar to what I did for google colab. :pray:

### Binder

I have built a repo which shows an example of how to run D-Tale within Binder [here](https://github.com/aschonfeld/dtale-binder).

The important take-aways are:
* you must have `jupyter-server-proxy` installed
* look at the `environment.yml` file to see how to add it to your environment
* look at the `postBuild` file for how to activate it on startup


### R with Reticulate

I was able to get D-Tale running in R using reticulate. Here is an example:

```
library('reticulate')
dtale <- import('dtale')
df <- read.csv('https://vincentarelbundock.github.io/Rdatasets/csv/boot/acme.csv')
dtale$show(df, subprocess=FALSE, open_browser=TRUE)
```

Now the problem with doing this is that D-Tale is not running as a subprocess so it will block your R console and you'll lose out the following functions:
 - manipulating the state of your data from your R console
 - adding more data to D-Tale

`open_browser=TRUE` isn't required and won't work if you don't have a default browser installed on your machine. If you don't use that parameter simply copy & paste the URL that gets printed to your console in the browser of your choice.

I'm going to do some more digging on why R doesn't seem to like using python subprocesses (not sure if it something with how reticulate manages the state of python) and post any findings to this thread.

Here's some helpful links for getting setup:

reticulate

installing python packages

### Startup with No Data

It is now possible to run D-Tale with no data loaded up front. So simply call `dtale.show()` and this will start the application for you and when you go to view it you will be presented with a screen where you can upload either a CSV or TSV file for data.

![](https://raw.githubusercontent.com/aschonfeld/dtale-media/master/images/no_data.png)

Once you've loaded a file it will take you directly to the standard data grid comprised of the data from the file you loaded.  This might make it easier to use this as an on demand application within a container management system like kubernetes. You start and stop these on demand and you'll be presented with a new instance to load any CSV or TSV file to!

### Command-line
Base CLI options (run `dtale --help` to see all options available)

|Prop     |Description|
|:--------|:-----------|
|`--host` |the name of the host you would like to use (most likely not needed since `socket.gethostname()` should figure this out)|
|`--port` |the port you would like to assign to your D-Tale instance|
|`--name` |an optional name you can assign to your D-Tale instance (this will be displayed in the `<title>` & Instances popup)|
|`--debug`|turn on Flask's "debug" mode for your D-Tale instance|
|`--no-reaper`|flag to turn off auto-reaping subprocess (kill D-Tale instances after an hour of inactivity), good for long-running displays |
|`--open-browser`|flag to automatically open up your server's default browser to your D-Tale instance|
|`--force`|flag to force D-Tale to try an kill any pre-existing process at the port you've specified so it can use it|

Loading data from [**ArcticDB**(high performance, serverless DataFrame database)](https://github.com/man-group/ArcticDB) (this requires either installing **arcticdb** or **dtale[arcticdb]**)
```bash
dtale --arcticdb-uri lmdb:///<path> --arcticdb-library jdoe.my_lib --arcticdb-symbol my_symbol
```
If you would like to change your storage mechanism to ArcticDB then add the `--arcticdb-use_store` flag
```bash
dtale --arcticdb-uri lmdb:///<path> --arcticdb-library my_lib --arcticdb-symbol my_symbol --arcticdb-use_store
```
Loading data from [**arctic**(high performance datastore for pandas dataframes)](https://github.com/man-group/arctic) (this requires either installing **arctic** or **dtale[arctic]**)
```bash
dtale --arctic-uri mongodb://localhost:27027 --arctic-library my_lib --arctic-symbol my_symbol --arctic-start 20130101 --arctic-end 20161231
```
Loading data from **CSV**
```bash
dtale --csv-path /home/jdoe/my_csv.csv --csv-parse_dates date
```
Loading data from **EXCEL**
```bash
dtale --excel-path /home/jdoe/my_csv.xlsx --excel-parse_dates date
dtale --excel-path /home/jdoe/my_csv.xls --excel-parse_dates date
```
Loading data from **JSON**
```bash
dtale --json-path /home/jdoe/my_json.json --json-parse_dates date
```
or
```bash
dtale --json-path http://json-endpoint --json-parse_dates date
```
Loading data from **R Datasets**
```bash
dtale --r-path /home/jdoe/my_dataset.rda
```
Loading data from **SQLite DB Files**
```bash
dtale --sqlite-path /home/jdoe/test.sqlite3 --sqlite-table test_table
```

### Custom Command-line Loaders

Loading data from a **Custom** loader
- Using the DTALE_CLI_LOADERS environment variable, specify a path to a location containing some python modules
- Any python module containing the global variables LOADER_KEY & LOADER_PROPS will be picked up as a custom loader
  - LOADER_KEY: the key that will be associated with your loader.  By default you are given **arctic** & **csv** (if you use one of these are your key it will override these)
  - LOADER_PROPS: the individual props available to be specified.
    - For example, with arctic we have host, library, symbol, start & end.
    - If you leave this property as an empty list your loader will be treated as a flag.  For example, instead of using all the arctic properties we would simply specify `--arctic` (this wouldn't work well in arctic's case since it depends on all those properties)
- You will also need to specify a function with the following signature `def find_loader(kwargs)` which returns a function that returns a dataframe or `None`
- Here is an example of a custom loader:
```python
from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'testdata'
LOADER_PROPS = ['rows', 'columns']


def test_data(rows, columns):
    import pandas as pd
    import numpy as np
    import random
    from past.utils import old_div
    from pandas.tseries.offsets import Day
    from dtale.utils import dict_merge
    import string

    now = pd.Timestamp(pd.Timestamp('now').date())
    dates = pd.date_range(now - Day(364), now)
    num_of_securities = max(old_div(rows, len(dates)), 1)  # always have at least one security
    securities = [
        dict(security_id=100000 + sec_id, int_val=random.randint(1, 100000000000),
             str_val=random.choice(string.ascii_letters) * 5)
        for sec_id in range(num_of_securities)
    ]
    data = pd.concat([
        pd.DataFrame([dict_merge(dict(date=date), sd) for sd in securities])
        for date in dates
    ], ignore_index=True)[['date', 'security_id', 'int_val', 'str_val']]

    col_names = ['Col{}'.format(c) for c in range(columns)]
    return pd.concat([data, pd.DataFrame(np.random.randn(len(data), columns),
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `dtale/dash_application/layout/__init__.py`
```python

```

#### File: `dtale/charts/__init__.py`
```python

```

#### File: `dtale/cli/__init__.py`
```python

```

#### File: `dtale/django/__init__.py`
```python

```

#### File: `tests/dtale/config/__init__.py`
```python

```

#### File: `tests/dtale/charts/__init__.py`
```python

```


==================================================


## [3/3] Repository: MachineLearningStocks (`PHASE4-QUANT-029`)
- **Full Name**: `PHASE4-QUANT-029_robertmartin8__MachineLearningStocks`
- **Description**: Using python and scikit-learn to make stock predictions
- **GitHub Stars**: 1960
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# MachineLearningStocks in python: a starter project and guide

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GitHub license](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square)](https://github.com/surelyourejoking/MachineLearningStocks/blob/master/LICENSE.txt)

*EDIT as of Feb 2021: MachineLearningStocks is no longer actively maintained*

MachineLearningStocks is designed to be an **intuitive** and **highly extensible** template project applying machine learning to making stock predictions. My hope is that this project will help you understand the overall workflow of using machine learning to predict stock movements and also appreciate some of its subtleties. And of course, after following this guide and playing around with the project, you should definitely **make your own improvements** – if you're struggling to think of what to do, at the end of this readme I've included a long list of possiblilities: take your pick.

Concretely, we will be cleaning and preparing a dataset of historical stock prices and fundamentals using `pandas`, after which we will apply a `scikit-learn` classifier to discover the relationship between stock fundamentals (e.g PE ratio, debt/equity, float, etc) and the subsequent annual price change (compared with the an index). We then conduct a simple backtest, before generating predictions on current data.

While I would not live trade based off of the predictions from this exact code, I do believe that you can use this project as starting point for a profitable trading system – I have actually used code based on this project to live trade, with pretty decent results (around 20% returns on backtest and 10-15% on live trading).

This project has quite a lot of personal significance for me. It was my first proper python project, one of my first real encounters with ML, and the first time I used git. At the start, my code was rife with bad practice and inefficiency: I have since tried to amend most of this, but please be warned that some minor issues may remain (feel free to raise an issue, or fork and submit a PR). Both the project and myself as a programmer have evolved a lot since the first iteration, but there is always room to improve.

*As a disclaimer, this is a purely educational project. Be aware that backtested performance may often be deceptive – trade at your own risk!*

*MachineLearningStocks predicts which stocks will outperform. But it does not suggest how best to combine them into a portfolio. I have just released [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt), a portfolio optimisation library which uses
classical efficient frontier techniques (with modern improvements) in order to generate risk-efficient portfolios. Generating optimal allocations from the predicted outperformers might be a great way to improve risk-adjusted returns.*

*This guide has been cross-posted at my academic blog, [reasonabledeviations.com](https://reasonabledeviations.com/)*

## Contents

- [Contents](#contents)
- [Overview](#overview)
  - [EDIT as of 24/5/18](#edit-as-of-24518)
  - [EDIT as of October 2019](#edit-as-of-october-2019)
- [Quickstart](#quickstart)
- [Preliminaries](#preliminaries)
- [Historical data](#historical-data)
  - [Historical stock fundamentals](#historical-stock-fundamentals)
  - [Historical price data](#historical-price-data)
- [Creating the training dataset](#creating-the-training-dataset)
  - [Preprocessing historical price data](#preprocessing-historical-price-data)
  - [Features](#features)
    - [Valuation measures](#valuation-measures)
    - [Financials](#financials)
    - [Trading information](#trading-information)
  - [Parsing](#parsing)
- [Backtesting](#backtesting)
- [Current fundamental data](#current-fundamental-data)
- [Stock prediction](#stock-prediction)
- [Unit testing](#unit-testing)
- [Where to go from here](#where-to-go-from-here)
  - [Data acquisition](#data-acquisition)
  - [Data preprocessing](#data-preprocessing)
  - [Machine learning](#machine-learning)
- [Contributing](#contributing)

## Overview

The overall workflow to use machine learning to make stocks prediction is as follows:

1. Acquire historical fundamental data – these are the *features* or *predictors*
2. Acquire historical stock price data – this is will make up the dependent variable, or label (what we are trying to predict).
3. Preprocess data
4. Use a machine learning model to learn from the data
5. Backtest the performance of the machine learning model
6. Acquire current fundamental data
7. Generate predictions from current fundamental data

This is a very generalised overview, but in principle this is all you need to build a fundamentals-based ML stock predictor.

### EDIT as of 24/5/18

This project uses pandas-datareader to download historical price data from Yahoo Finance. However, in the past few weeks this has become extremely inconsistent – it seems like Yahoo have added some measures to prevent the bulk download of their data. I will try to add a fix, but for now, take note that `download_historical_prices.py` may be deprecated.

As a temporary solution, I've uploaded `stock_prices.csv` and `sp500_index.csv`, so the rest of the project can still function.

### EDIT as of October 2019

I expect that after so much time there will be many data issues. To that end, I have decided to upload the other CSV files: `keystats.csv` (the output of `parsing_keystats.py`) and `forward_sample.csv` (the output of `current_data.py`).

## Quickstart

If you want to throw away the instruction manual and play immediately, clone this project, then download and unzip the [data file](https://pythonprogramming.net/data-acquisition-machine-learning/) into the same directory. Then, open an instance of terminal and cd to the project's file path, e.g

```bash
cd Users/User/Desktop/MachineLearningStocks
```

Then, run the following in terminal:

```bash
pip install -r requirements.txt
python download_historical_prices.py
python parsing_keystats.py
python backtesting.py
python current_data.py
pytest -v
python stock_prediction.py
```

Otherwise, follow the step-by-step guide below.

## Preliminaries

This project uses python 3.6, and the common data science libraries `pandas` and `scikit-learn`. If you are on python 3.x less than 3.6, you will find some syntax errors wherever f-strings have been used for string formatting. These are fortunately very easy to fix (just rebuild the string using your preferred method), but I do encourage you to upgrade to 3.6 to enjoy the elegance of f-strings. A full list of requirements is included in the `requirements.txt` file. To install all of the requirements at once, run the following code in terminal:

```bash
pip install -r requirements.txt
```

To get started, clone this project and unzip it. This folder will become our working directory, so make sure you `cd` your terminal instance into this directory.

## Historical data

Data acquisition and preprocessing is probably the hardest part of most machine learning projects. But it is a necessary evil, so it's best to not fret and just carry on.

For this project, we need three datasets:

1. Historical stock fundamentals
2. Historical stock prices
3. Historical S&P500 prices

We need the S&P500 index prices as a benchmark: a 5% stock growth does not mean much if the S&P500 grew 10% in that time period, so all stock returns must be compared to those of the index.

### Historical stock fundamentals

Historical fundamental data is actually very difficult to find (for free, at least). Although sites like [Quandl](https://www.quandl.com/) do have datasets available, you often have to pay a pretty steep fee.

It turns out that there is a way to parse this data, for free, from [Yahoo Finance](https://finance.yahoo.com/). I will not go into details, because [Sentdex has done it for us](https://pythonprogramming.net/data-acquisition-machine-learning/). On his page you will be able to find a file called `intraQuarter.zip`, which you should download, unzip, and place in your working directory. Relevant to this project is the subfolder called `_KeyStats`, which contains html files that hold stock fundamentals for all stocks in the S&P500 between 2003 and 2013, sorted by stock. However, at this stage, the data is unusable – we will have to parse it into a nice csv file before we can do any ML.

### Historical price data

In the first iteration of the project, I used `pandas-datareader`, an extremely convenient library which can load stock data straight into `pandas`. However, after Yahoo Finance changed their UI, `datareader` no longer worked, so I switched to [Quandl](https://www.quandl.com/), which has free stock price data for a few tickers, and a python API. However, as `pandas-datareader` has been [fixed](https://github.com/ranaroussi/fix-yahoo-finance), we will use that instead.

Likewise, we can easily use `pandas-datareader` to access data for the SPY ticker. Failing that, one could manually download it from [yahoo finance](https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC), place it into the project directory and rename it `sp500_index.csv`.

The code for downloading historical price data can be run by entering the following into terminal:

```bash
python download_historical_prices.py
```

## Creating the training dataset

Our ultimate goal for the training data is to have a 'snapshot' of a particular stock's fundamentals at a particular time, and the corresponding subsequent annual performance of the stock.

For example, if our 'snapshot' consists of all of the fundamental data for AAPL on the date 28/1/2005, then we also need to know the percentage price change of AAPL between 28/1/05 and 28/1/06. Thus our algorithm can learn how the fundamentals impact the annual change in the stock price.

In fact, this is a slight oversimplification. In fact, what the algorithm will eventually learn is how fundamentals impact the *outperformance of a stock relative to the S&P500 index*. This is why we also need index data.

### Preprocessing historical price data

When `pandas-datareader` downloads stock price data, it does not include rows for weekends and public holidays (when the market is closed).

However, referring to the example of AAPL above, if our snapshot includes fundamental data for 28/1/05 and we want to see the change in price a year later, we will get the nasty surprise that 28/1/2006 is a Saturday. Does this mean that we have to discard this snapshot?

By no means – data is too valuable to callously toss away. As a workaround, I instead decided to 'fill forward' the missing data, i.e we will assume that the stock price on Saturday 28/1/2006 is equal to the stock price on Friday 27/1/2006.

### Features

Below is a list of some of the interesting variables that are available on Yahoo Finance.

#### Valuation measures

- 'Market Cap'
- Enterprise Value
- Trailing P/E
- Forward P/E
- PEG Ratio
- Price/Sales
- Price/Book
- Enterprise Value/Revenue
- Enterprise Value/EBITDA

#### Financials

- Profit Margin
- Operating Margin
- Return on Assets
- Return on Equity
- Revenue
- Revenue Per Share
- Quarterly Revenue Growth
- Gross Profit
- EBITDA
- Net Income Avi to Common
- Diluted EPS
- Quarterly Earnings Growth
- Total Cash
- Total Cash Per Share
- Total Debt
- Total Debt/Equity
- Current Ratio
- Book Value Per Share
- Operating Cash Flow
- Levered Free Cash Flow

#### Trading information

- Beta
- 50-Day Moving Average
- 200-Day Moving Average
- Avg Vol (3 month)
- Shares Outstanding
- Float
- % Held by Insiders
- % Held by Institutions
- Shares Short
- Short Ratio
- Short % of Float
- Shares Short (prior month)

### Parsing

However, all of this data is locked up in HTML files. Thus, we need to build a parser. In this project, I did the parsing with regex, but please note that generally it is [really not recommended](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags) to use regex to parse HTML. However, I think regex probably wins out for ease of understanding (this project being educational in nature), and from experience regex works fine in this case.

This is the exact regex used:

```python
r'>' + re.escape(variable) + r'.*?(\-?\d+\.*\d*K?M?B?|N/A[\\n|\s]*|>0|NaN)%?(</td>|</span>)'
```

While it looks pretty arcane, all it is doing is searching for the first occurence of the feature (e.g "Market Cap"), then it looks forward until it finds a number immediately followed by a `</td>` or `</span>` (signifying the end of a table entry). The complexity of the expression above accounts for some subtleties in the parsing:

- the numbers could be preceeded by a minus sign
- Yahoo Finance sometimes uses K, M, and B as abbreviations for thousand, million and billion respectively.
- some data are given as percentages
- some datapoints are missing, so instead of a number we have to look for "N/A" or "NaN.

Both the preprocessing of price data and the parsing of keystats are included in `parsing_keystats.py`. Run the following in your terminal:

```bash
python parsing_keystats.py
```

You should see the file `keystats.csv` appear in your working directory. Now that we have the training data ready, we are ready to actually do some machine learning.

## Backtesting

Backtesting is arguably the most important part of any quantitative strategy: you must have some way of testing the performance of your algorithm before you live trade it.

Despite its importance, I originally did not want to include backtesting code in this repository. The reasons were as follows:

- Backtesting is messy and empirical. The code is not very pleasant to use, and in practice requires a lot of manual interaction.
- Backtesting is very difficult to get right, and if you do it wrong, you will be deceiving yourself with high returns.
- Developing and working with your backtest is probably the best way to learn about machine learning and stocks – you'll see what works, what doesn't, and what you don't understand.

Nevertheless, because of the importance of backtesting, I decided that I can't really call this a 'template machine learning stocks project' without backtesting. Thus, I have included a simplistic backtesting script. Please note that there is a fatal flaw with this backtesting implementation that will result in *much* higher backtesting returns. It is quite a subtle point, but I will let you figure that out :)

Run the following in terminal:

```bash
python backtesting.py
```

You should get something like this:

```txt
Classifier performance
======================
Accuracy score:  0.81
Precision score:  0.75

Stock prediction performance report
===================================
Total Trades: 177
Average return for stock predictions:  37.8 %
Average market return in the same period:  9.2%
Compared to the index, our strategy earns  28.6 percentage points more
```

Again, the performance looks too good to be true and almost certainly is.

## Current fundamental data

Now that we have trained and backtested a model on our data, we would like to generate actual predictions on current data.

As always, we can scrape the data from good old Yahoo Finance. My method is to literally just download the statistics page for each stock (here is the [page](https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL) for Apple), then to parse it using regex as before.

In fact, the regex should be almost identical, but because Yahoo has changed their UI a couple of times, there are some minor differences. This part of the projet has to be fixed whenever yahoo finance changes their UI, so if you can't get the project to work, the problem is most likely here.

Run the following in terminal:

```bash
python current_data.py
```

The script will then begin downloading the HTML into the `forward/` folder within your working directory, before parsing this data and outputting the file `forward_sample.csv`. You might see a few miscellaneous errors for certain tickers (e.g 'Exceeded 30 redirects.'), but this is to be expected.

## Stock prediction

Now that we have the training data and the current data, we can finally generate actual predictions. This part of the project is very simple: the only thing you have to decide is the value of the `OUTPERFORMANCE` parameter (the percentage by which a stock has to beat the S&P500 to be considered a 'buy'). I have set it to 10 by default, but it can easily be modified by changing the variable at the top of the file. Go ahead and run the script:

```bash
python stock_prediction.py
```

You should get something like this:

```txt
21 stocks predicted to outperform the S&P500 by more than 10%:
NOC FL SWK NFX LH NSC SCHL KSU DDS GWW AIZ ORLY R SFLY SHW GME DLX DIS AMP BBBY APD
```

## Unit testing

I have included a number of unit tests (in the `tests/` folder) which serve to check that things are working properly. However, due to the nature of the some of this projects functionality (downloading big datasets), you will have to run all the code once before running the tests. Otherwise, the tests themselves would have to download huge datasets (which I don't think is optimal).

I thus recommend that you run the tests after you have run all the other scripts (except, perhaps, `stock_prediction.py`).

To run the tests, simply enter the following into a terminal instance in the project directory:

```bash
pytest -v
```

Please note that it is not considered best practice to include an `__init__.py` file in the `tests/` directory (see [here](https://docs.pytest.org/en/latest/goodpractices.html) for more), but I have done it anyway because it is uncomplicated and functional.

## Where to go from here

I have stated that this project is extensible, so here are some ideas to get you started and possibly increase returns (no promises).

### Data acquisition

My personal belief is that better quality data is THE factor that will ultimately determine your performance. Here are some ideas:

- Explore the other subfolders in Sentdex's `intraQuarter.zip`.
- Parse the annual reports that all companies submit to the SEC (have a look at the [Edgar Database](https://www.sec.gov/edgar/searchedgar/companysearch.html))
- Try to find websites from which you can scrape fundamental data (this has been my solution).
- Ditch US stocks and go global – perhaps better results may be found in markets that are less-liquid. It'd be interesting to see whether the predictive power of features vary based on geography.
- Buy Quandl data, or experiment with alternative data.

### Data preprocessing

- Build a more robust parser using BeautifulSoup
- In this project, I have just ignored any rows with missing data, but this reduces the size of the dataset considerably. Are there any ways you can fill in some of this data?
  - hint: if the PE ratio is missing but you know the stock price and the earnings/share...
  - hint 2: how different is Apple's book value in March to its book value in June?
- Some form of feature engineering
  - e.g, calculate [Graham's number](https://www.investopedia.com/terms/g/graham-number.asp) and use it as a feature
  - some of the features are probably redundant. Why not remove them to speed up training?
- Speed up the construction of `keystats.csv`.
  - hint: don't keep appending to one growing dataframe! Split it into chunks

### Machine learning

Altering the machine learning stuff is probably the easiest and most fun to do.

- The most important thing if you're serious about results is to find the problem with the current backtesting setup and fix it. This will likely be quite a sobering experience, but if your backtest is done right, it should mean that any observed outperformance on your test set can be traded on (again, do so at your own discretion).
- Try a different classifier – there is plenty of research that advocates the use of SVMs, for example. Don't forget that other classifiers may require feature scaling etc.
- Hyperparameter tuning: use gridsearch to find the optimal hyperparameters for your classifier. But make sure you don't overfit!
- Make it *deep* – experiment with neural networks (an easy way to start is with `sklearn.neural_network`).
- Change the classification problem into a regression one: will we achieve better results if we try to predict the stock *return* rather than whether it outperformed?
- Run the prediction multiple times (perhaps using different hyperparameters?) and select the *k* most common stocks to invest in. This is especially important if the algorithm is not deterministic (as is the case for Random Forest)
- Experiment with different values of the `outperformance` parameter.
- Should we really be trying to predict raw returns? What happens if a stock achieves a 20% return but does so by being highly volatile?
- Try to plot the importance of different features to 'see what the machine sees'.

## Contributing

Feel free to fork, play around, and submit PRs. I would be very grateful for any bug fixes or more unit tests.

This project was originally based on Sentdex's excellent [machine learning tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3), but it has since evolved far beyond that and the code is almost completely different. The complete series is also on [his website](https://pythonprogramming.net/machine-learning-python-sklearn-intro/).

---

For more content like this, check out my academic blog at [reasonabledeviations.com/](https://reasonabledeviations.com).

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/test_variables.py`
```python
import os
import parsing_keystats
import current_data
import stock_prediction


def test_statspath():
    # Check that the statspath exists and is a directory
    assert os.path.exists(current_data.statspath)
    assert os.path.isdir(current_data.statspath)

    assert parsing_keystats.statspath == current_data.statspath


def test_features_same():
    # There are only four differences (intentionally)
    assert set(parsing_keystats.features) - set(current_data.features) == {'Net Income Avl to Common', 'Qtrly Earnings Growth',
                                                                           'Qtrly Revenue Growth', 'Shares Short (as of',
                                                                           'Shares Short (prior month)'}
    assert set(current_data.features) - set(parsing_keystats.features) == {'Net Income Avi to Common', 'Quarterly Earnings Growth',
                                                                           'Shares Short', 'Quarterly Revenue Growth',
                                                                           'Shares Short (prior month'}


def test_outperformance():
    assert stock_prediction.OUTPERFORMANCE >= 0
```

#### File: `tests/test_utils.py`
```python
import pytest
import utils


def test_status_calc():
    """
    Test the status_calc function which generates training labels
    """
    assert utils.status_calc(50, 20, 12.2) == 1
    assert utils.status_calc(12.003, 10, 15) == 0
    assert utils.status_calc(-10, -30, 5) == 1
    assert utils.status_calc(-31, -30, 15) == 0
    assert utils.status_calc(15, 5, 10) == 1

    with pytest.raises(ValueError):
        utils.status_calc(12, 10, -3)


def test_data_string_to_float():
    """
    data_string_to_float() is a function that needs to meet lots of empirical requirements
    owing to the idiosyncrasies of Yahoo Finance's HTML. The main jobs are parsing negatives and
    abbreviations of big numbers.
    """
    assert utils.data_string_to_float("asdfNaN") == "N/A"
    assert utils.data_string_to_float(">N/A\n</") == "N/A"
    assert utils.data_string_to_float(">0") == 0
    assert utils.data_string_to_float("-3") == -3
    assert utils.data_string_to_float("4K") == 4000
    assert utils.data_string_to_float("2M") == 2000000
    assert utils.data_string_to_float("0.07B") == 70000000
    assert utils.data_string_to_float("-100.1K") == -100100
    assert utils.data_string_to_float("-0.1M") == -100000
    assert utils.data_string_to_float("-0.02B") == -20000000
    assert utils.data_string_to_float("-0.00") == 0
    assert utils.data_string_to_float("0.00") == 0
    assert utils.data_string_to_float("0M") == 0
    assert utils.data_string_to_float("010K") == 10000

    with pytest.raises(ValueError):
        utils.data_string_to_float(">0x")
    with pytest.raises(ValueError):
        utils.data_string_to_float("10k")
    with pytest.raises(ValueError):
        utils.data_string_to_float("2KB")
```

#### File: `stock_prediction.py`
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from utils import data_string_to_float, status_calc


# The percentage by which a stock has to beat the S&P500 to be considered a 'buy'
OUTPERFORMANCE = 10


def build_data_set():
    """
    Reads the keystats.csv file and prepares it for scikit-learn
    :return: X_train and y_train numpy arrays
    """
    training_data = pd.read_csv("keystats.csv", index_col="Date")
    training_data.dropna(axis=0, how="any", inplace=True)
    features = training_data.columns[6:]

    X_train = training_data[features].values
    # Generate the labels: '1' if a stock beats the S&P500 by more than 10%, else '0'.
    y_train = list(
        status_calc(
            training_data["stock_p_change"],
            training_data["SP500_p_change"],
            OUTPERFORMANCE,
        )
    )

    return X_train, y_train


def predict_stocks():
    X_train, y_train = build_data_set()
    # Remove the random_state parameter to generate actual predictions
    clf = RandomForestClassifier(n_estimators=100, random_state=0)
    clf.fit(X_train, y_train)

    # Now we get the actual data from which we want to generate predictions.
    data = pd.read_csv("forward_sample.csv", index_col="Date")
    data.dropna(axis=0, how="any", inplace=True)
    features = data.columns[6:]
    X_test = data[features].values
    z = data["Ticker"].values

    # Get the predicted tickers
    y_pred = clf.predict(X_test)
    if sum(y_pred) == 0:
        print("No stocks predicted!")
    else:
        invest_list = z[y_pred].tolist()
        print(
            f"{len(invest_list)} stocks predicted to outperform the S&P500 by more than {OUTPERFORMANCE}%:"
        )
        print(" ".join(invest_list))
        return invest_list


if __name__ == "__main__":
    print("Building dataset and predicting stocks...")
    predict_stocks()
```

#### File: `download_historical_prices.py`
```python
import os
from pandas_datareader import data as pdr
import pandas as pd
import fix_yahoo_finance as yf

yf.pdr_override()

START_DATE = "2003-08-01"
END_DATE = "2015-01-01"


def build_stock_dataset(start=START_DATE, end=END_DATE):
    """
    Creates the dataset containing all stock prices
    :returns: stock_prices.csv
    """

    statspath = "intraQuarter/_KeyStats/"
    ticker_list = os.listdir(statspath)

    # Required on macOS
    if ".DS_Store" in ticker_list:
        os.remove(f"{statspath}/.DS_Store")
        ticker_list.remove(".DS_Store")

    # Get all Adjusted Close prices for all the tickers in our list,
    # between START_DATE and END_DATE
    all_data = pdr.get_data_yahoo(ticker_list, start, end)
    stock_data = all_data["Adj Close"]

    # Remove any columns that hold no data, and print their tickers.
    stock_data.dropna(how="all", axis=1, inplace=True)
    missing_tickers = [
        ticker for ticker in ticker_list if ticker.upper() not in stock_data.columns
    ]
    print(f"{len(missing_tickers)} tickers are missing: \n {missing_tickers} ")
    # If there are only some missing datapoints, forward fill.
    stock_data.ffill(inplace=True)
    stock_data.to_csv("stock_prices.csv")


def build_sp500_dataset(start=START_DATE, end=END_DATE):
    """
    Creates the dataset containing S&P500 prices
    :returns: sp500_index.csv
    """
    index_data = pdr.get_data_yahoo("SPY", start=START_DATE, end=END_DATE)
    index_data.to_csv("sp500_index.csv")


def build_dataset_iteratively(
    idx_start, idx_end, date_start=START_DATE, date_end=END_DATE
):
    """
    This is an alternative iterative solution to building the stock dataset, which may be necessary if the
    tickerlist is too big.
    Instead of downloading all at once, we download ticker by ticker and append to a dataframe.
    This will download data for tickerlist[idx_start:idx_end], which makes this method suitable
    for chunking data.

    :param idx_start: (int) the starting index of the tickerlist
    :param idx_end: (int) the end index of the tickerlist
    """

    statspath = "intraQuarter/_KeyStats/"
    ticker_list = os.listdir(statspath)

    df = pd.DataFrame()

    for ticker in ticker_list:
        ticker = ticker.upper()

        stock_ohlc = pdr.get_data_yahoo(ticker, start=date_start, end=date_end)
        if stock_ohlc.empty:
            print(f"No data for {ticker}")
            continue
        adj_close = stock_ohlc["Adj Close"].rename(ticker)
        df = pd.concat([df, adj_close], axis=1)
    df.to_csv("stock_prices.csv")


if __name__ == "__main__":
    build_stock_dataset()
    build_sp500_dataset()
```

#### File: `utils.py`
```python
def data_string_to_float(number_string):
    """
    The result of our regex search is a number stored as a string, but we need a float.
        - Some of these strings say things like '25M' instead of 25000000.
        - Some have 'N/A' in them.
        - Some are negative (have '-' in front of the numbers).
        - As an artifact of our regex, some values which were meant to be zero are instead '>0'.
    We must process all of these cases accordingly.
    :param number_string: the string output of our regex, which needs to be converted to a float.
    :return: a float representation of the string, taking into account minus sign, unit, etc.
    """
    # Deal with zeroes and the sign
    if ("N/A" in number_string) or ("NaN" in number_string):
        return "N/A"
    elif number_string == ">0":
        return 0
    elif "B" in number_string:
        return float(number_string.replace("B", "")) * 1000000000
    elif "M" in number_string:
        return float(number_string.replace("M", "")) * 1000000
    elif "K" in number_string:
        return float(number_string.replace("K", "")) * 1000
    else:
        return float(number_string)


def duplicate_error_check(df):
    """
    A common symptom of failed parsing is when there are consecutive duplicate values. This function was used
    to find the duplicates and tweak the regex. Any remaining duplicates are probably coincidences.
    :param df: the dataframe to be checked
    :return: Prints out a list of the rows containing duplicates, as well as the duplicated values.
    """
    # Some columns often (correctly) have the same value as other columns. Remove these.
    df.drop(
        [
            "Unix",
            "Price",
            "stock_p_change",
            "SP500",
            "SP500_p_change",
            "Float",
            "200-Day Moving Average",
            "Short Ratio",
            "Operating Margin",
        ],
        axis=1,
        inplace=True,
    )

    for i in range(len(df)):
        # Check if there are any duplicates.
        if pd.Series(df.iloc[i] == df.iloc[i].shift()).any():
            duplicates = set(
                [x for x in list(df.iloc[i]) if list(df.iloc[i]).count(x) > 1]
            )
            # A duplicate value of zero is quite common. We want other duplicates.
            if duplicates != {0}:
                print(i, df.iloc[i], duplicates, sep="\n")


def status_calc(stock, sp500, outperformance=10):
    """A simple function to classify whether a stock outperformed the S&P500
    :param stock: stock price
    :param sp500: S&P500 price
    :param outperformance: stock is classified 1 if stock price > S&P500 price + outperformance
    :return: true/false
    """
    if outperformance < 0:
        raise ValueError("outperformance must be positive")
    return stock - sp500 >= outperformance
```


==================================================
