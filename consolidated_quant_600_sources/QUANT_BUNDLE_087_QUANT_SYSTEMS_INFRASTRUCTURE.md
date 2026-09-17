# ⚡ [QUANT-SOURCE-087] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_087_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: wallstreet-core (`WHEEL_wallstreet-core`)
- **Full Name**: `wallstreet-core`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
Wallstreet: Real time Stock and Option tools
--------------------------------------------

Wallstreet is a Python 3 library for monitoring and analyzing real time Stock and
Option data. Quotes are provided from the Google Finance API. Wallstreet requires
minimal input from the user, it uses available online data to calculate option
greeks and even scrapes the US Treasury website to get the current risk free rate.


Usage
-----

Stocks:

.. code-block:: Python

  from wallstreet import Stock, Call, Put

  >>> s = Stock('AAPL')
  >>> s.price
  96.44
  >>> s.price
  96.48
  >>> s.change
  -0.35
  >>> s.last_trade
  '21 Jan 2016 13:32:12'

Options:

.. code-block:: Python

  >>> g = Call('GOOG', d=12, m=2, y=2016, strike=700)
  >>> g.price
  38.2
  >>> g.implied_volatility()
  0.49222968442691889
  >>> g.delta()
  0.56522039722040063
  >>> g.vega()
  0.685034827159825
  >>> g.underlying.price
  706.59

Alternative construction:

.. code-block:: Python

  >>> g = Call('GOOG', d=12, m=2, y=2016)
  >>> g
  Call(ticker=GOOG, expiration='12-02-2016')
  >>> g.strikes
  (580, 610, 620, 630, 640, 650, 660, 670, 680, 690, 697.5, 700, 702.5, 707.5, 710, 712.5, 715, 720, ...)
  >>> g.set_strike(712.5)
  >>> g
  Call(ticker=GOOG, expiration='12-02-2016', strike=712.5)

or

.. code-block:: Python

  >>> g = Put("GOOG")
  'No options listed for given date, using 22-01-2016 instead'
  >>> g.expirations
  ['22-01-2016', '29-01-2016', '05-02-2016', '12-02-2016', '19-02-2016', '26-02-2016', '04-03-2016', ...]
  >>> g
  Put(ticker=GOOG, expiration='22-01-2016')

Yahoo Finance Support (keep in mind that YF quotes might be delayed):

.. code-block:: Python

    >>> apple = Stock('AAPL', source='yahoo')
    >>> call = Call('AAPL', strike=apple.price, source='yahoo')
    No options listed for given date, using '26-05-2017' instead
    No option for given strike, using 155 instead

Download historical data (requires pandas)

.. code-block:: Python

    s = Stock('BTC-USD')
    >>> df = s.historical(days_back=30, frequency='d')
    >>> df
             Date          Open          High           Low         Close     Adj Close      Volume
    0  2019-07-10  12567.019531  13183.730469  11569.940430  12099.120117  12099.120117  1554955347
    1  2019-07-11  12099.120117  12099.910156  11002.389648  11343.120117  11343.120117  1185222449
    2  2019-07-12  11343.120117  11931.910156  11096.610352  11797.370117  11797.370117   647690095
    3  2019-07-13  11797.370117  11835.870117  10827.530273  11363.969727  11363.969727   668325183
    4  2019-07-14  11363.969727  11447.919922  10118.849609  10204.410156  10204.410156   814667763
    5  2019-07-15  10204.410156  11070.179688   9877.019531  10850.259766  10850.259766   965178341
    6  2019-07-16  10850.259766  11025.759766   9366.820313   9423.440430   9423.440430  1140137759
    7  2019-07-17   9423.440430   9982.240234   9086.509766   9696.150391   9696.150391   965256823
    8  2019-07-18   9696.150391  10776.540039   9292.610352  10638.349609  10638.349609  1033842556
    9  2019-07-19  10638.349609  10757.410156  10135.160156  10532.940430  10532.940430   658190962
    10 2019-07-20  10532.940430  11094.320313  10379.190430  10759.419922  10759.419922   608954333
    11 2019-07-21  10759.419922  10833.990234  10329.889648  10586.709961  10586.709961   405339891
    12 2019-07-22  10586.709961  10676.599609  10072.070313  10325.870117  10325.870117   524442852
    13 2019-07-23  10325.870117  10328.440430   9820.610352   9854.150391   9854.150391   529438124
    14 2019-07-24   9854.150391   9920.540039   9535.780273   9772.139648   9772.139648   531611909
    15 2019-07-25   9772.139648  10184.429688   9744.700195   9882.429688   9882.429688   403576364
    16 2019-07-26   9882.429688   9890.049805   9668.519531   9847.450195   9847.450195   312717110
    17 2019-07-27   9847.450195  10202.950195   9310.469727   9478.320313   9478.320313   512612117
    18 2019-07-28   9478.320313   9591.519531   9135.639648   9531.769531   9531.769531   267243770
    19 2019-07-29   9531.769531   9717.690430   9386.900391   9506.929688   9506.929688   299936368
    20 2019-07-30   9506.929688   9749.530273   9391.780273   9595.519531   9595.519531   276402322
    21 2019-07-31   9595.519531  10123.940430   9581.599609  10089.250000  10089.250000   416343142
    22 2019-08-01  10089.250000  10488.809570   9890.490234  10409.790039  10409.790039   442037342
    23 2019-08-02  10409.790039  10666.639648  10340.820313  10528.990234  10528.990234   463688251
    24 2019-08-03  10528.990234  10915.000000  10509.349609  10820.410156  10820.410156   367536516
    25 2019-08-04  10820.410156  11074.950195  10572.240234  10978.910156  10978.910156   431699306
    26 2019-08-05  10978.910156  11945.379883  10978.889648  11807.959961  11807.959961   870917186
    27 2019-08-06  11807.959961  12316.849609  11224.099609  11467.099609  11467.099609   949534020
    28 2019-08-07  11467.099609  12138.549805  11393.980469  11974.280273  11974.280273   834719365
    29 2019-08-08  11974.280273  12042.870117  11498.040039  11982.799805  11982.799805   588463519
    30 2019-08-09  11983.620117  12027.570313  11674.059570  11810.679688  11810.679688   366160288

Installation
------------
Simply

.. code-block:: bash

    $ pip install wallstreet


Stock Attributes
----------------

- ticker
- price
- id
- exchange
- last_trade
- change   (change in currency)
- cp   (percentage change)


Option Attributes and Methods
-----------------------------

- strike
- expiration
- underlying  (underlying stock object)
- ticker
- bid
- ask
- price (option price)
- id
- exchange
- change  (in currency)
- cp  (percentage change)
- volume
- open_interest
- code
- expirations (list of possible expiration dates for option chain)
- strikes (list of possible strike prices)

- set_strike()
- implied_volatility()
- delta()
- gamma()
- vega()
- theta()
- rho()

### Core Implementation Code & Architecture
#### File: `wallstreet/__init__.py`
```python
from wallstreet.wallstreet import Stock, Call, Put

__all__ = ['Stock', 'Call', 'Put']

__version__ = "0.4.0"
```

#### File: `tests/mockrequests/mockrequests/__init__.py`
```python
from .mockrequests import get, post, Request, save, Session

__all__ = ['get', 'post', 'Request', 'save', 'Session']
```

#### File: `pyproject.toml`
```python
[tool.poetry]
name = "wallstreet"
version = "0.4.0"
description = "Stock and Option tools"
authors = ["Mike Dallas <mcdallas@protonmail.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.31"
scipy = "^1.12"
yfinance = "^0.2.37"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

#### File: `wallstreet/constants.py`
```python
DATE_FORMAT = '%d-%m-%Y'
DATETIME_FORMAT = '%d %b %Y %H:%M:%S'

TREASURY_URL = "https://home.treasury.gov/sites/default/files/interest-rates/yield.xml"
DELTA_DIFFERENTIAL = 1.e-3
VEGA_DIFFERENTIAL = 1.e-4
GAMMA_DIFFERENTIAL = 1.e-3
RHO_DIFFERENTIAL = 1.e-4
THETA_DIFFERENTIAL = 1.e-5

IMPLIED_VOLATILITY_TOLERANCE = 1.e-6
SOLVER_STARTING_VALUE = 0.27

OVERNIGHT_RATE = 0
FALLBACK_RISK_FREE_RATE = 0.02
```

#### File: `tests/mockrequests/response/GET/map.json`
```python
{"response1.p": ["http://finance.google.com/finance/info?client=ig&q=GOOG", null, false], "response2.p": ["https://query2.finance.yahoo.com/v7/finance/options/GOOG", null, false], "response3.p": ["http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield", null, false], "response4.p": ["https://www.google.com/finance/option_chain?q=GOOG&expd=16&expm=6&expy=2017&output=json", null, false], "response5.p": ["https://query2.finance.yahoo.com/v7/finance/options/GOOG?date=1497571200", null, false], "response6.p": ["https://www.google.com/finance/option_chain?q=GOOG&expd=15&expm=6&expy=2017&output=json", null, false]}
```

#### File: `tests/test_stock.py`
```python
import unittest
from wallstreet import wallstreet
from tests.mockrequests import mockrequests


class StockTest(unittest.TestCase):
    def setUp(self):
        self.oldrequests = wallstreet.requests
        wallstreet.requests = mockrequests

    def test_price(self):
        s = wallstreet.Stock('GOOG')
        self.assertEqual(s.price, 834.34)

    def test_last_trade(self):
        s = wallstreet.Stock('GOOG')
        self.assertEqual(s.last_trade, '22 Mar 2017 11:38:12')

    def test_yahoo_price(self):
        s = wallstreet.Stock('GOOG', source='yahoo')
        self.assertEqual(s.price, 833.65)

    def test_yahoo_last_trade(self):
        s = wallstreet.Stock('GOOG', source='yahoo')
        self.assertEqual(s.last_trade, '22 Mar 2017 15:53:24')

    def tearDown(self):
        wallstreet.requests = self.oldrequests
```


==================================================


## [2/3] Repository: quant-ashare (`PHASE4-QUANT-002`)
- **Full Name**: `PHASE4-QUANT-002_wangpage__quant-ashare`
- **Description**: 机构级 A股量化系统 - Hermes 多智能体 + Barra 中性化 + Level2 微结构 + 15 个圈内 tricks 完整实现
- **GitHub Stars**: 26
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# quant-ashare

> **机构级 A股量化研究框架** — 融合多智能体 LLM 决策、事件驱动 Stock Radar、Barra 风格中性化、Almgren-Chriss 冲击成本建模的开源实现.

[![Tests](https://img.shields.io/badge/numerical%20tests-65%2F65-brightgreen)](tests/test_numerical_correctness.py) [![Smoke](https://img.shields.io/badge/smoke%20tests-~120-blue)](tests/)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

不是又一个抄 Alpha158 的项目. 本项目致力于实现 **头部私募在用但很少公开的圈内技巧**, 覆盖从数据清洗到执行层的完整量化链路, 并配套一套**事件驱动 + 多智能体 LLM** 的实盘辅助决策系统.

**当前状态**: 圈内暗门核心模块已实装 12+, 详解见 [ADVANCED_TRICKS.md](ADVANCED_TRICKS.md); 实盘辅助侧已落地 klineshare 实时数据源、Stock Radar 新闻事件流水线、paper trade 自动账户、微信推送闭环. 实装/规划见 [功能矩阵](#-已实装-vs-规划功能矩阵).

> ⚠️ **诚实定位**: 本项目是**研究框架 + 实盘辅助工具**, 不是已验证的盈利策略. 用 klineshare 真实数据做过严格实证后的结论是 **2024-2026 A股牛市中没有可落地的公开因子 alpha** — 详见 [真实回测](#-真实回测--含严格-oos-修正记录).

---

## 🏗️ 架构

```
┌──────────────────────────────────────────────────────────────┐
│  实盘辅助决策层                                                  │
│  ┌────────────────────────┐  ┌─────────────────────────────┐  │
│  │ 多智能体 LLM 决策         │  │ Stock Radar 事件流水线         │  │
│  │ [基本面][技术][情绪][事件]│←─│ 东财快讯定时拉取 radar_pull   │  │
│  │  →[Bull vs Bear]→[交易]  │  │ → 分诊(qwen-turbo)→深挖(qwen-plus)│  │
│  │  →[风控]                 │  │ → memory.db → 简报/候选注入    │  │
│  └────────────────────────┘  └─────────────────────────────┘  │
├──────────────────────────────────────────────────────────────┤
│  因子层: Alpha158-lite + 反转/低波 + 涨停连板 + 席位网络 +        │
│          日内犹豫度 + 大盘 regime  (pandas 向量化, 喂 LightGBM)   │
├──────────────────────────────────────────────────────────────┤
│  【圈内暗门模块 — 已实装】                                        │
│  标签工程 / 微结构因子 / 因子衰减监控 / 事件屏蔽                    │
│  Barra 中性化 / 组合优化 / 数据清洗 / 主题投资 / 执行层             │
├──────────────────────────────────────────────────────────────┤
│  数据源三分:                                                     │
│   · 实时/历史行情 = klineshare.cn (主) + 东财/新浪直连 (兜底)      │
│   · 情绪新闻 = 东财个股新闻 (akshare stock_news_em)              │
│   · Radar 事件 = 东财快讯定时拉取 (radar_pull.py, 无需插件)       │
│   · 龙虎榜/资金流/基本面 = 东财 datacenter + akshare; Level2 NATS │
├──────────────────────────────────────────────────────────────┤
│  风控: 涨跌停 / T+1 / 凯利 / 回撤熔断 / PreTradeGate / Regime 乘数 │
└──────────────────────────────────────────────────────────────┘
```

## ✨ 核心特性

### 🧠 多智能体 LLM 决策
- Hermes-3 风格 **XML 结构化推理** (`<THINKING>`, `<REASONING>`, `<REFLECTION>`)
- **Bull vs Bear 多轮辩论**, 由 Judge agent 最终裁决
- 分析师并行 (asyncio), 分析师阶段延迟 ~3x; 支持第 4 位 **事件分析师** (由 Radar 摘要驱动)
- **明日操作台辩论层**: 因子粗筛候选池 → 多智能体辩论**否决 + 重排 + 赞同**(全否决则从池补票, 绝不空榜), 并**双榜 A/B**(辩论榜 vs 纯因子)用命中率闭环实测有效性. `daily_advisor.py --debate` 开启, 默认关. 见 `llm_layer/advisor_debate.py`.
- 统一多后端 `_LLMBackend`: **Qwen / DeepSeek / DMXAPI 聚合 / Claude / GPT / Kimi / GLM / OpenRouter / 智增增 / mock**
- 后端由 `--backend` / `LLM_BACKEND` 等环境变量选择, **实际用哪个取决于 `.env` 里配了哪个 key**. 本项目 **2026-07 起主用千问 Qwen** (backend `qwen`/`qwen-plus`, 读 `DASHSCOPE_API_KEY`); **DeepSeek** (`deepseek-chat`) 与 **DMXAPI 聚合器** (`dmxapi`, `DMXAPI_API_KEY`, 一个 key 转 GPT/Claude/Gemini) 作备选. 无 Anthropic key.
- 切 Gemini 走 DMXAPI 一行搞定: `LLM_BACKEND=dmx-gemini`(→`gemini-3-flash-preview`)/ `dmx-gemini-pro`(→`gemini-2.5-pro`)/ `dmx-gpt`(→`gpt-4o-mini`). ⚠️ Gemini 是 thinking 模型, `max_tokens` 需 ≥600 否则推理烧光预算返回空串.
- `TradingAgentTeam`/radar 里 `anthropic`/`claude-*` 只是**代码内历史默认值**, 未配 `ANTHROPIC_API_KEY` 不生效; radar 分诊/深挖与辩论层默认均已切到 `qwen`.

### 📡 Stock Radar — 事件驱动新闻流水线
新闻源是**东财全球财经快讯** (无鉴权公开 JSON), 由后台定时拉取器直接抓取, **无需浏览器插件、无需常驻 FastAPI**. 后台 daemon 分诊 (qwen-turbo) + 深挖 (qwen-plus), 结果注入交易决策. 深挖判断"已 price-in"时读本地 parquet 行情缓存, code↔name 反幻觉校验走 akshare:

```
scripts/radar_pull.py (定时拉东财快讯 → 归一化 → add_radar_events)
                          │ 幂等写入 cache/memory.db (kind='radar_event')
                          ▼
              scripts/radar_worker.py (daemon, 轮询 needs_analysis)
                  1. triage      每条事件  qwen-turbo (event_type/entities/tradability)
                  2. gate        噪音跳过, 高价值强制深挖
                  3. deep_analyze 高价值   qwen-plus  (thesis/targets/priced_in/供应链/风险)
                          │ 写回 metadata.analysis  (含 code↔name 反幻觉校验)
                          ├─▶ radar_briefing.py    → 微信简报
                          ├─▶ radar_candidates.py  → paper trade top-K 前插/规避
                          └─▶ radar_events_helper.py → 交易 Agent 的"事件分析师"
```

一键拉起整条链路 (拉取器 + worker):

```bash
python scripts/start_all.py          # 或 Windows: scripts\start_all.bat
```

数据源可扩展 (`data_adapter/news_feed.py` 留了 `fetch_news(sources=...)` 分发壳, 日后可加财联社/同花顺). 交互式复盘见技能 [.claude/skills/radar-analyze.md](.claude/skills/radar-analyze.md).

### 🧬 记忆与自进化
- **Memory Curator**: 每笔交易后 LLM 提炼反思存 SQLite + FTS5 (`cache/memory.db`)
- **Skill Factory**: 自动从成功交易聚类生成复用规则 (condition→action)
- **Weekly Nudge / Monthly Audit**: 定期合并去重记忆、剪枝低价值反思

### 📊 已实装 vs 规划功能矩阵

✅ = 已有代码 + 测试/实盘调用; 🟡 = 已实装但仅测试或旁路使用; 🚧 = 骨架/规划

| # | 技巧 | 状态 | 大众盲点 → 本项目实现 |
|---|---|:---:|---|
| 1 | 标签工程 | ✅ | `close/close` → 多 horizon + vol 归一化 + CSRank + **停牌/一字板屏蔽** |
| 2 | 涨跌停 / 停牌屏蔽 | ✅ | 全量训练 → 自动屏蔽 (回测 IC 虚高 20-30%) |
| 3 | Level2 微结构 alpha | 🟡 | OIR / **VPIN** / Cancel Ratio / Kyle's λ (已实装, 离线可跑; 实盘 NATS 已修连接 bug, 待真实 broker 验证) |
| 4 | 冲击成本建模 | ✅ | 固定 2bps → **Almgren-Chriss + sqrt 律** (执行层实盘路由已接) |
| 5 | Barra 风格中性化 | ✅ | Size+Industry → **CNE5 六风格因子** (分层正交 + ridge) |
| 6 | 因子衰减监控 | ✅ | 训完不管 → rolling IC + 半衰期 + 健康分自动下线 |
| 7 | 组合优化 | 🟡 | Top-K 等权 → 风险平价 (实盘用) + MVO/Black-Litterman (已实装, 测试用) |
| 8 | 事件屏蔽 | ✅ | 无 → 解禁/财报/大宗自动屏蔽 |
| 9 | 数据清洗 | ✅ | 幸存 / 前视 / 复权 (含**小幅分红/累计漂移**) + audit 报告 |
| 10 | 主题投资识别 | 🟡 | 纯涨幅 → 萌芽/扩散/拥挤三阶段 + 龙头排序 |
| 11 | Regime 自适应 | ✅ | 8 种市场状态分类器 + 仓位乘数 + LLM 上下文注入 |
| 12 | Level2 时序保护 | ✅ | 指数退避 / 时钟漂移监控 / 乱序检测 (离线) |
| 13 | 资金流因子 | ✅ | 主力/超大单 12 因子 (V8 已用) + 高管增减持 + 龙虎榜席位 |
| 14 | 涨停连板因子 | ✅ | **16 个** A股独有因子 (连板高度/炸板率/一字板/量能压缩), `factors/alpha_limit.py` |
| 15 | 龙虎榜游资特征 | ✅ | **13 个** 席位网络因子 (游资联动图/机构主导/接力), `factors/seat_network.py` |

详解见 [ADVANCED_TRICKS.md](ADVANCED_TRICKS.md). 进度会随每次 release 更新.

### 🚀 端到端 Pipeline
- **ResearchPipeline** (`pipeline/research.py`): 数据体检 → 标签 → 屏蔽 → 因子 → 前视扫描 → Barra → IC/衰减 → 带冲击回测 (强制过 `PreTradeGate`) → 报告
- **DailyTradingPipeline** (`pipeline/daily_trading.py`): Regime → 筛选 → Agent 辩论 → 风控 → 冲击路由

---

## 📈 真实回测 — 含严格 OOS 修正记录

> ⚠️ **重要诚实声明**: 早期版本 (V3-V5) 的"夏普 1.86 / IR 1.21"包含了 **训练集 label 泄露**(label horizon=30, 但训练截止 = train_end, 后 30 天 label 在真实时点不可观测). **修复 leak 后** OOS IR 跌至 **-0.13 ~ +0.2** 之间. **本项目当前定位为研究框架, 不是已验证的实盘策略.**

### 演化记录(全部 walk-forward 严格 OOS)

| 版本 | 因子构成 | Hold-out IR(干净) | 关键发现 |
|---|---|---|---|
| V1 baseline | 10 大蓝筹 + 3 玩具因子 | 0.79(其实是纯 beta) | 蓝筹无 alpha,Sharpe 来自市场 |
| V3 | 500 中小盘 + 龙虎榜 5 因子 | — | 含 leak,数字不再呈报 |
| V4 | + IC 聚类去共线 + 动态滑点 | — | 框架修正 |
| V5 | + 涨停/连板 + 高管增减持 | — | 含 leak |
| V6 (B+ 自适应极性) | + IC 时序 z-score 极性切换 | **+0.96 → 修复后 -0.13** | leak 暴露 |
| V7 (+ regime 因子) | + 大盘动量/广度 | -1.38 | 加 regime 反加剧过拟合 |
| V8 (+ 主力资金流) | + 超大单/大单/散户净流入 | **-0.75** | 牛市 regime 中无效 |

### 🔬 klineshare 真实数据的三轮收敛实证 (最新, 2026-07)

接入 klineshare 真实行情后, 用 **Top300 成交额大盘池 (295 股, 2024-2026)** 做了三轮严格实证, 结论比早期更硬:

1. **LightGBM 揉 36 个 pandas 因子, 严格防泄露 (`label_cut = t - horizon`)**: OOS IC≈0, t=-0.24 **不显著** → ML 堆公开因子没 alpha, 把信号淹在噪声里.
2. **反转族因子日频 IC 看似显著** (REV5 t=2.39, 过 Barra 中性化残差 t 甚至升到 3.53) → ⚠️ **这是重叠样本假象**: 日频"未来 5 日收益"相邻重叠 4/5, IC 序列强自相关, `t = mean/std×√n` 把重叠当独立, t 值系统性虚高.
3. **反转组合换非重叠周频 + 扣 sqrt 冲击成本回测**: 同样 ~0.02 的 IC, t 塌到 **0.97 不显著**; Top30 扣费后**跑输等权 55%/年**; 多空 t=-0.99.

> **关键教训**: **"重叠样本 t 值虚高"是量化最常见的自欺**. 判显著必须用非重叠样本 / Newey-West. IC 幅度真实 (~0.02) ≠ 统计稳健 ≠ 扣费能赚钱, 三码事.
> 复现脚本: [walkforward_lgbm_barra.py](scripts/walkforward_lgbm_barra.py) (模型+中性化) / [rev5_barra_check.py](scripts/rev5_barra_check.py) (因子中性化, 其日频 t 虚高) / [backtest_klineshare.py](scripts/backtest_klineshare.py) (`--factor reversal|momrev`, 扣费回测).

### 真 alpha 在哪里(不再粉饰)

公开因子 + LightGBM + 月频选股,**真实 OOS 夏普天花板 0.5-1.0**. 想突破需要:
- ✅ Wind/Choice 付费数据(¥5-20 万/年)
- ✅ Level2 tick 数据(券商开户送) + 分钟级回测框架
- ✅ 自监督模型(Kronos 等)取代手工因子
- ✅ 等待 regime 切换(单边牛市里多头选股本就是 worst case)
- ❌ 继续堆公开因子 — 已被 4000+ 量化机构挖干净

---

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/wangpage/quant-ashare.git
cd quant-ashare
pip install -r requirements.txt

# 最小裸环境实测只需:
#   requests pandas numpy lightgbm loguru pyyaml scikit-learn
# akshare / pyqlib / streamlit / anthropic 按需再装 (见 requirements.txt 注释)
```

### 配置数据源与密钥 (`.env`)

仓库提供了脱敏模板 [`.env.example`](.env.example)。真实 `.env` 保留在本地，不提交到 GitHub。

主行情走 **klineshare.cn** 实时 API (无需 akshare 即可跑核心研究/回测):

```bash
# .env (已 gitignore — 因为每日 cron 会 auto-push 到 GitHub)
KLINESHARE_API_KEY=tg_xxxxxxxx        # klineshare 实时行情 (主数据源)
# KLINESHARE_HOST=http://120.77.200.82  # 可选, 覆盖默认 host

# LLM (至少配一个; 本项目 2026-07 起主用 Qwen, radar/辩论默认走 qwen)
DASHSCOPE_API_KEY=sk-xxx             # 千问 Qwen (主用)
DEEPSEEK_API_KEY=sk-xxx              # DeepSeek (备选, 便宜)
# DMXAPI_API_KEY / DMXAPI_BASE_URL   # DMXAPI 聚合网关 (备选, 一 key 转 GPT/Claude/Gemini)
# ANTHROPIC_API_KEY=sk-ant-xxx       # 可选; 未配则 radar/辩论走 qwen (本部署未配)

# 推送 (Server酱 微信, 唯一在用的推送通道)
SERVERCHAN_SENDKEY=SCTxxxxxx
```

> **套餐边界 (klineshare 基础版)**: realtime / kline / trend / stock / corp / calendar 可用, limit_up 每日试用 2 次; **lhb / hot_money / moneyflow / etf 需专业版** (基础版调用返回 403). 因此龙虎榜/资金流走 akshare/东财兜底路径.

**MCP 集成**: 项目根 `.mcp.json` 已配 `market-data-api` MCP server (`http://120.77.200.82/mcp`, `X-API-Key` 头), 可让 Claude Code 直接查行情/K线/涨停/龙虎榜.

### ⚡ 一键启动 Radar 事件流水线

删掉了旧的浏览器插件依赖 — 现在新闻由后台定时器直接抓东财快讯. 一条命令拉起「新闻拉取 + 分诊/深挖」全链路:

```bash
python scripts/start_all.py          # 或 Windows 双击 scripts\start_all.bat
# 单独调试: python scripts/radar_pull.py --once   (拉一次东财快讯写入 memory.db)
```

分诊/深挖需要 LLM key (默认走 `DASHSCOPE_API_KEY` 的 Qwen); 只拉新闻入库不需要任何 key.

### 🌐 启动 Web UI (推荐)

最快看到项目效果的方式. Streamlit 多页应用, **7 个交互页面**:

| 页面 | 内容 |
|---|---|
| 📡 今日信号仪表盘 | 大盘 regime + 主题评分 + top-K 信号 + 资金分配 |
| 🔍 个股详情 | K 线 / 因子画像 / 主题归属 |
| 🧠 Agent 辩论记录 | 三分析师 + Bull vs Bear + 交易员 + 风控 |
| 📈 回测与策略曲线 | 净值 / 回撤 / IC 衰减 / Barra 分解 |
| 💼 我的持仓 | 持仓监控 + 止损/冲高提醒 (持仓手工录入, 行情/资料实时) |
| 📄 研究报告 | 研究 pipeline 产出的 HTML 报告 |
| 🎯 明日操作台 | 明日 Top-N 计划 + 买点/止损/目标 (开辩论则显示辩论榜 + 双命中率 A/B) |

```bash
# 默认 real 模式: 全部页面真实数据 (klineshare + 东财 HTTP + daily_report json + 现场回测)
bash scripts/run_webapp.sh              # 或 Windows: scripts\run_webapp.bat
# 浏览器打开 http://localhost:8501

# 无网络 / 演示: 强制 mock
QUANT_WEB_MODE=mock bash scripts/run_webapp.sh
```

> 真实数据经 `webapp/real_data.py` 适配 (每个 provider 失败自动回退 mock)。今日信号池/主题评分/资金分配由当日 `daily_report` 派生, K线/资料/概念走 klineshare, regime 走东财 (涨停家数用 klineshare limit_up 按日缓存), 回测现场重跑并缓存。⚠️ 改了 `webapp/*.py` 模块须**整个重启 streamlit 进程**(浏览器刷新不重导入已缓存模块)。

### 🧪 测试诚实说明

测试分两层, 不要混淆:

| 类型 | 文件 | 数量 | 说明 |
|---|---|---|---|
| **数值正确性 (单元)** | `tests/test_numerical_correctness.py` | **65** | 真数值断言: IC/ICIR 精确匹配, 最大回撤闭式公式, ATR 止损 3 种情况, Barra 残差正交性 (corr<0.05), AC 冲击 sqrt 律单调性, VPIN/OIR 边界, URL 占位符识别, Regime 崩盘/狂热识别, alpha 衰减监控单调性 |
| **冒烟/契约 (集成)** | 其他 `tests/test_*.py` | ~120 | 主要验证"非空 / 字段存在 / 函数可跑通", 不做数值校对 |

```bash
python3 tests/test_numerical_correctness.py           # 65/65  ← 最该看的
python3 tests/test_parser.py                          # Level2 CSV 解析 60/60
python3 tests/test_phase1_xml.py                      # Hermes XML 34/34
python3 tests/test_phase2_memory_regime.py            # Memory+Regime 35/35
python3 tests/test_advanced_tricks.py                 # 6 暗门 55/55
```

### 跑真实数据研究 / 回测 (klineshare)

```bash
# 拉 Top300 成交额大盘池 + 因子筛选 + IC 合成 + OOS 验证
python3 scripts/factor_train_klineshare.py

# 严格 walk-forward LightGBM + Barra 残差 IC + 衰减
python3 scripts/walkforward_lgbm_barra.py

# 单因子扣费回测 (反转 / 动量反转), 复现"扣费跑输等权"的结论
python3 scripts/backtest_klineshare.py --factor reversal
```

### LLM Agent 决策 (默认千问 Qwen)

```bash
export DASHSCOPE_API_KEY="sk-xxxxx"          # 千问 (主用); 或 DEEPSEEK_API_KEY 走备选
# 单只股票跑完整多智能体辩论 (默认 backend=qwen)
python3 scripts/agent_debate.py --code 600519
# 明日操作台叠加辩论层 (否决+重排+赞同, 双榜 A/B)
python3 scripts/daily_advisor.py --scope watch --top 20 --debate --dry-run
```

### Level2 实时行情接入

离线模拟器 (parser + simulator + validator) 已完整可跑并通过测试; 实盘 NATS 客户端 `connect()` 的未绑定变量 bug **已修复**, 但尚未对真实 broker 做端到端验证, 上线前请先用测试账号 (300750/600519) 跑通握手.

```bash
python3 tests/test_parser.py            # Level2 CSV 解析 (离线)
```

详细计划见 [LEVEL2_LIVE_TEST_PLAN.md](LEVEL2_LIVE_TEST_PLAN.md) 与 [tests/LEVEL2_GUIDE.md](tests/LEVEL2_GUIDE.md).

---

## 📁 项目结构

```
quant-ashare/
├── config/                    # YAML 配置 (config / level2 / qlib_workflow / user_watchlist)
├── data_adapter/          ⭐ klineshare(主) + 东财/新浪(兜底) + akshare 专用适配
│                              (fundflow / insider / lhb / announcements / theme / sentiment 源)
│                              + news_feed.py (东财快讯拉取, 替代 Radar 插件)
├── data_hygiene/          ⭐ 数据清洗暗门 (幸存/前视/复权/停牌/时钟) + audit 报告
├── factors/                   # 因子: alpha_pandas(37) + reversal(20) + limit(16) +
│                              # seat_network(13) + intraday(19) + regime(5) + 自适应极性
├── label_engineering/     ⭐ 标签工程 (多 horizon + vol 归一化 + 可交易屏蔽)
├── market_microstructure/ ⭐ OIR / VPIN / Kyle's λ / Almgren-Chriss / micro-price
├── corporate_actions/     ⭐ 解禁/财报/大宗事件 屏蔽 + 事件因子
├── barra_neutralize/      ⭐ CNE5 六风格因子 + 分层正交中性化
├── alpha_decay/           ⭐ IC 衰减 + 半衰期 + 拥挤度监控
├── portfolio_opt/         ⭐ 风险平价 + MVO + Black-Litterman
├── execution/             ⭐ TWAP/VWAP/POV + 冲击感知路由 + 时段避让 + 回测撮合
├── risk/                      # A股风控 (a_share_rules) + PreTradeGate 统一闸门
├── market_regime/             # 8 种市场状态分类器 (仓位乘数 + LLM 上下文)
├── thematic_investing/        # 主题投资识别 (萌芽/扩散/拥挤 + 龙头排序)
├── level2/                    # NATS Level2 接入 (离线模拟完整, 实盘路径待修)
├── llm_layer/                 # Hermes XML + 多智能体 + Radar 分诊/深挖 + 情绪
├── memory/                    # 交易记忆 + Skill Factory + radar 事件存储 (SQLite+FTS5)
├── analyst/              ⭐ 分析师简报层 (市场全景 + 因子聚合 → 微信简报, 含合规改写)
├── notifier/             ⭐ 推送统一出口 (notifier/wechat.py = Server酱; 飞书已下线)
├── pipeline/              ⭐ 研究 + 实盘 + 报告 (含 HTML/对比报告)
├── webapp/                    # Streamlit 7 页可视化 (mock/real 双模)
├── utils/                     # 配置加载 + 日志封装
├── scripts/                   # 一键脚本 (start_all / cron_daily / radar_pull / dazi_* 等)
└── ADVANCED_TRICKS.md    ⭐ 圈内 tricks 详解 + 上线 checklist
```

---

## 🔬 核心技术文档

| 文档 | 内容 |
|---|---|
| [ADVANCED_TRICKS.md](ADVANCED_TRICKS.md) | 15 个头部私募在用的 tricks + 上线 checklist |
| [LEVEL2_LIVE_TEST_PLAN.md](LEVEL2_LIVE_TEST_PLAN.md) | Level2 NATS 盘中接入作战手册 |
| [tests/LEVEL2_GUIDE.md](tests/LEVEL2_GUIDE.md) | 本地 NATS + 生产环境接入指南 |
| [.claude/skills/radar-analyze.md](.claude/skills/radar-analyze.md) | Radar 事件交互式复盘技能 |

---

## 🔔 每日自动化 (定时任务 + 微信通知)

> **推送通道**: 全部走 **Server酱 微信** (`notifier/wechat.py`, `SERVERCHAN_SENDKEY`). 早期的飞书 / lark-cli 通道已**整体下线**, 代码里残留的"飞书"字样是历史命名, 实际都发到微信.

### 主流水线 — `cron_daily.py` (7 步)

每日 15:30 自动跑, 约 5-8 分钟完成 (见 [scripts/cron_daily.py](scripts/cron_daily.py)):

```
1/7 数据增量更新     (daily_data_updater.py — kline/龙虎榜/insider/fundflow 增量)
2/7 Paper Trade     (paper_trade_runner.py — 可 --use-radar 注入 radar 候选)
3/7 Watchlist 信号   (watchlist_signal.py  ← 自选池 z-score 因子)
4/7 Git Commit/Push (同步 paper trade 产物到 GitHub)
5/7 账户通知         → 微信 (NAV + 持仓 + 当日 P&L)
6/7 分析师简报       → 微信 (python -m notifier.dispatch, 市场全景 + 明日 Top-N + 昨日命中)
7/7 批量扫描         → 微信 (batch_scan --top 20 --bottom 10, 246 只候选池 + LLM 精分析)
```

任一环节失败会发错误告警到微信,不阻塞后续步骤. `rc==10` (LLM/推送鉴权过期) 会打标跳过而非中断.

### 其它定时任务 (独立于 7 步主流水线)

| 任务 | 脚本 | 时机 | 作用 |
|---|---|---|---|
| Radar 拉取 | `radar_pull.py --once` | 盘中每 5 分钟 | 抓东财快讯 → 写 memory.db |
| Radar daemon | `radar_worker.py --once` | 盘中每 5 分钟 | 消费新闻事件 → 分诊/深挖 |
| Radar 简报 | `radar_briefing.py` | 12:01 / 14:33 / 15:37 | 当日事件情报 → 微信 |
| 打板监控 | `dazi_monitor.py` | 盘中常驻 | 大单异动扫描 (见下) |
| 明日操作台 | `daily_advisor.py` (Win 任务 QuantAdvisor) | **08:50 / 14:30** | 早盘+午盘各更新一次 Top-N + 买点/止损/目标 (+ 可选 `--debate` 辩论层) |
| 盘后复盘 | `daily_review.py` (Win 任务 QuantReview) | **次日收盘后** | 上午/午盘分别算命中率闭环 + IC 自适应因子重加权 |
| 持仓跟踪 | `track_picks.py` | 09:25→15:05 | 盘中触发买/止损/止盈 |
| Leak 自检 | `cron_daily.py --leak-check` | 周日 20:00 | 跑 leak detector 回归 |

### 安装定时任务

**Linux / macOS** — `scripts/install_cron.sh` (幂等):

```bash
bash scripts/install_cron.sh              # 安装 (含 15:30 主流水线 + radar + 周日 leak-check)
bash scripts/install_cron.sh --dry-run    # 预览
bash scripts/install_cron.sh --uninstall  # 卸载
```

**Windows** — `.bat` + 任务计划程序, 用 `scripts/harden_tasks.ps1` 让任务"唤醒执行/错过即补/失败重试":

```
run_advisor.bat am (daily_advisor 08:50)  run_advisor.bat pm (daily_advisor 14:30)
run_review.bat     (次日收盘后复盘)
run_track.bat    (持仓跟踪 09:25)         run_dazi.bat   (打板监控常驻)
run_webapp.bat   (Streamlit 8501)         run_weekly.bat (周报 周五 ~15:45)
powershell -File scripts/harden_tasks.ps1   # 加固 QuantAdvisor/QuantReview 任务
```

> ⚠️ **任务须设为「不管用户是否登录都运行」(LogonType S4U)**。否则任务在交互式控制台会话里跑, 会话一被打扰 (关窗口 / Ctrl+C / 会话中断) 进程即被杀, 退出码 `0xC000013A` (STATUS_CONTROL_C_EXIT), 报告不生成。`harden_tasks.ps1` 只调重试设置**不改登录类型**, 需另设 (无需密码):
> ```powershell
> $p = New-ScheduledTaskPrincipal -UserId Administrator -LogonType S4U -RunLevel Limited
> foreach ($t in 'QuantAdvisor','QuantReview','QuantTrack','QuantWeekly') { Set-ScheduledTask -TaskName $t -Principal $p }
> ```

### 打板监控 `dazi_monitor.py` — 大单异动扫描

盘中扫描"刚启动"的个股供打板参考. 模型 **"BOS 大单异动指数 V3"** = 量能异动 (35%) × 价格确认 (30%) × 资金确认 (25%) × 活跃度过滤 (10%), 需 ≥2 根 1 分钟连续确认后分级 **S/A/B/C**:

- **量比** = 近 5 分钟量 / 前 30 分钟 5 分钟均量 (滚动基线)
- **涨速+结构** = 5 分钟涨幅 且 站上 VWAP 且 创日内新高 (滤洗盘/派发)
- **资金确认** = 近 5 分钟主力净流入 > 0 且 当日累计外盘占比达标
- **活跃度** = 换手 + 近 5 分钟成交额门槛 (滤"低价股 × 大手数"假信号)
- **regime** = 上证在 5 日线上用基准阈值, 弱市抬高量比/涨幅要求

数据 100% 东财免费实时接口 (快照 / 1 分钟 K / 分钟主力净流入), 推送 Server酱, 状态存 `output/real_positions/dazi_state.json`.

---

## 🔬 研究档案 (V6-V8 严格 OOS 实验)

**[scripts/run_holdout_v6.py](scripts/run_holdout_v6.py)**: B+ 自适应极性 (IC z-score + 显著性过滤 + 惯性 + 横截面归一化), 暴露了早期版本的 label leak.

**[scripts/run_holdout_v8.py](scripts/run_holdout_v8.py)**: V8 主力资金流驱动 - 集成超大单/大单/中单/小单 12 个资金流因子. 在 2025-2026 单边牛市里 IR 仍负 (-0.75), 证明: **多头选股策略在 FOMO 牛市天生劣势, 不是技术问题**.

**[factors/adaptive_polarity.py](factors/adaptive_polarity.py)**: 4+1 层防护的因子极性自适应:
1. IC 时序 z-score (置信度, 不是绝对值)
2. 显著性过滤 (|z|<0.8 weight=0)
3. 惯性 EMA (防 regime 抖动)
4. 横截面归一化 (Σ|w|=1)
5. IC 衰减加权 (近期权重大)

**[factors/alpha_regime.py](factors/alpha_regime.py)**: 大盘 regime 因子 (动量/广度/波动率), 时序 z-score, 不走截面 z.

**[factors/alpha_limit.py](factors/alpha_limit.py)**: 涨停/连板/炸板/一字板/启动期压缩 等 16 个 A股独有因子.

**[factors/seat_network.py](factors/seat_network.py)**: 龙虎榜席位网络 13 因子 (游资联动图/机构主导/接力 vs 一日游).

**[data_adapter/insider.py](data_adapter/insider.py)**: 高管/大股东增减持事件因子.

**[data_adapter/fundflow.py](data_adapter/fundflow.py)**: 主力资金流 (akshare 个股近 120 日明细, 12 因子).

**[scripts/paper_trade_runner.py](scripts/paper_trade_runner.py)**: 每日自动化 paper trade - 维护真账户 + T+1 买卖 + 硬止损(亏 5%/破 MA5)+ 持仓档案.

---

## 🛡️ 免责声明

**本项目仅供学习与研究**, 不构成任何投资建议.

量化投资存在**实质性风险**. 任何 "95% 胜率"、"夏普 5+" 的宣传都是**过拟合或话术**.
真实量化 alpha 的核心是 (胜率-50%) × 盈亏比 × 高频次, 不是单次准度.

**本项目自身的诚实记录**: V3-V5 早期 README 写的"夏普 1.86 / IR 1.21"含 label leak,
修复后 OOS IR ≈ 0; 用 klineshare 真实数据复测后, 反转族因子的"显著"也被证明是**重叠样本假象**,
扣费后跑输等权. 这恰好印证了 — 任何"漂亮回测"都要严格 OOS + 非重叠样本 + 扣费验证.

实盘前必须:
1. ✅ 至少 6 个月样本外回测 (非重叠样本 / Newey-West 判显著)
2. ✅ 3 个月模拟盘验证
3. ✅ 从小资金起步 (< 预计规模 10%)
4. ✅ 严守风控规则 (最大回撤 / 熔断 / 止损)

---

## 🙏 致谢的开源项目

本项目学习了以下优秀项目的思想:
- [microsoft/qlib](https://github.com/microsoft/qlib) - AI 量化平台基石
- [akfamily/akshare](https://github.com/akfamily/akshare) - A股免费数据源
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) - XML 结构化推理
- [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) - 多智能体辩论
- [AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL) - 强化学习金融
- [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) - 中文金融 agent

---

## 📮 贡献

欢迎 Issue / PR. 特别欢迎:
- 新的 A股特化因子实现
- 头部私募已公开的 tricks 补充
- 性能优化 (向量化 / Cython)
- 更多后端 LLM 支持 (本地 llama / vLLM)

## 📄 License

[MIT](LICENSE) - 详见 LICENSE 文件, 含金融软件专属免责条款.

### Core Implementation Code & Architecture
#### File: `webapp/__init__.py`
```python

```

#### File: `webapp/components/__init__.py`
```python

```

#### File: `tests/__init__.py`
```python

```

#### File: `utils/__init__.py`
```python

```

#### File: `scripts/__init__.py`
```python

```

#### File: `analyst/__init__.py`
```python
"""分析师叙事层: 聚合量化产物 + 市场全景 → 飞书推送内容."""
```


==================================================


## [3/3] Repository: vnstock (`PHASE4-QUANT-011`)
- **Full Name**: `PHASE4-QUANT-011_thinh-vu__vnstock`
- **Description**: A beginner-friendly yet powerful Python toolkit for financial analysis and automation — built to make modern investing accessible to everyone
- **GitHub Stars**: 1397
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Vnstock - Công Cụ Python Mã Nguồn Công Khai Cho Thị Trường Chứng Khoán Việt Nam

[![Vnstock Homepage](https://raw.githubusercontent.com/thinh-vu/vnstock/refs/heads/main/assets/images/vnstock-home-vi.png)](https://vnstocks.com/)

<div id="badges" align="center">
    <img src="https://img.shields.io/pypi/pyversions/vnstock?logoColor=brown&style=flat" alt="Version"/>
    <img src="https://img.shields.io/github/last-commit/thinh-vu/vnstock?style=flat" alt="Commit Badge"/>
    <img src="https://img.shields.io/badge/license-Custom%20License-red?style=flat" alt="Custom License Badge"/>
</div>

<div id="badges" align="center">
    <a href="https://pypi.org/project/vnstock/">
        <img src="https://img.shields.io/pypi/dm/vnstock?label=vnstock%20download&style=flat" alt="vnstock download badge"/>
    </a>
</div>

<div id="badges" align="center">
    <a href="https://vnstocks.com/insiders-program">
        <img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86" alt="vnstock3 download badge"/>
    </a>
</div>
---

> ⚠️ **Note**: This document begins in 🇻🇳 Vietnamese for our local community.
>
> 🌐 **English version available below** — scroll or use the TOC (top-right 🟰) to navigate.

***

## Một thư viện Python để bạn tự truy xuất và chuẩn hoá dữ liệu chứng khoán Việt Nam

> Chào mừng bạn đến với **Vnstock**, hệ sinh thái công cụ Python giúp bạn tự kết nối, chuẩn hoá và phân tích **dữ liệu thị trường tài chính Việt Nam** từ nguồn bên thứ ba, chạy trên hạ tầng do bạn kiểm soát. Vnstock cấp quyền sử dụng phần mềm, không cấp quyền sử dụng dữ liệu của nguồn và không vận hành kho dữ liệu thị trường để bán lại.

Dù bạn muốn dùng **vnstock python** để xây dựng mô hình định lượng, tích hợp vào nền tảng phân tích của mình hay chỉ để tìm hiểu **lịch sử giá cổ phiếu**, bạn đều có thể bắt đầu ngay hôm nay.

### Tại sao chọn Vnstock?

* **Miễn phí cho cá nhân, mã nguồn công khai**: Dễ dàng tiếp cận, phục vụ nhà đầu tư cá nhân và lập trình viên muốn truy xuất dữ liệu chứng khoán Việt Nam qua **vnstock**. Mã nguồn công khai để bạn đọc và kiểm chứng; điều kiện sử dụng theo [giấy phép](https://vnstocks.com/onboard/giay-phep-su-dung).
* **Giải quyết dữ liệu phân mảnh**: Không cần tự viết mã kết nối từng nguồn từ số 0. Bạn gọi một hàm, thư viện gửi yêu cầu từ chính kết nối mạng của bạn tới nguồn rồi chuẩn hoá kết quả về dạng DataFrame để bạn nối vào luồng phân tích hoặc lưu trữ.
* **Làm việc được với AI Agent**: Có sẵn tài liệu để trợ lý AI đọc và viết code dùng thư viện.

***

## Bắt đầu nhanh & Vibe Coding

Bạn không cần kiến thức sâu về code để sử dụng vnstock. Dự án có sẵn các hướng dẫn sau:

### 1. Trải nghiệm trực tiếp trên trình duyệt với Google Colab

Nếu bạn chỉ muốn thử nghiệm nhanh hoặc **chạy python online**, bạn có thể dùng Google Colab. Không cần thiết lập môi trường phức tạp!

[![Google Colab](https://img.shields.io/badge/Google_Colab-Xem_hướng_dẫn-F9AB00?style=for-the-badge\&logo=googlecolab\&logoColor=white)](https://vnstocks.com/onboard/trai-nghiem-vnstock?utm_source=github\&utm_medium=readme)

### 2. Vibe Coding với AI (Bạn Ra Lệnh, AI Làm)

Cách này phù hợp với cả người mới bắt đầu lẫn người đã quen việc. AI đọc tài liệu của thư viện để viết code, chạy chương trình và diễn giải kết quả — bạn vẫn nên kiểm tra lại trước khi dùng.

Để bắt đầu nhanh nhất, vui lòng tham khảo các hướng dẫn chi tiết sau:

* [![Vibe Coding Guide](https://img.shields.io/badge/Vibe_Coding-Xem_hướng_dẫn_nhanh-8B5CF6?style=for-the-badge\&logo=visualstudiocode\&logoColor=white)](https://vnstocks.com/onboard/vibe-coding)
* [![Agent Guide](https://img.shields.io/badge/Agent_Guide-Tài_liệu_chi_tiết-24292e?style=for-the-badge\&logo=gitbook\&logoColor=white)](https://vnstocks.com/onboard/agent-guide)
* [![Đăng ký API Key](https://img.shields.io/badge/vnstocks.com-Đăng_ký_API_Key-0066FF?style=for-the-badge\&logo=keycdn\&logoColor=white)](https://vnstocks.com/login)

***

## Cài đặt thư viện

Nếu bạn viết code thủ công, hãy cài đặt qua `pip`:

```bash
pip install -U vnstock
```

### Xác thực người dùng (API Key)

Thư viện tự giới hạn nhịp gọi để việc truy xuất không gây ảnh hưởng tới nguồn cấp công khai và tới cộng đồng người dùng. Mức giới hạn gắn với tài khoản:

* Khách (Guest): 20 lượt gọi/phút, không cần đăng ký
* Cộng đồng: 60 lượt gọi/phút, đăng ký miễn phí
* Tài trợ (Sponsor): 180–600 lượt gọi/phút

Tài trợ là khoản đóng góp cho dự án, đổi lại là giấy phép sử dụng bản mở rộng — không phải phí mua dữ liệu hay dung lượng truy vấn. Dữ liệu thuộc về nguồn công bố; điều kiện sử dụng của từng nguồn do bạn tự kiểm tra và tuân thủ.

```python
from vnstock import register_user
register_user() # Làm theo hướng dẫn trên terminal
```

***

## Giao diện Hợp nhất (Unified UI) - Vnstock v4+

Bạn không cần bận tâm hàm nào thuộc nguồn nào, chỉ cần tập trung vào nhóm dữ liệu.

```python
from vnstock import Market, Reference, Fundamental

market = Market()
ref = Reference()
fa = Fundamental()

# Lấy dữ liệu lịch sử giá cổ phiếu (OHLCV)
df_history = market.equity.ohlcv(symbol='VNM', start='2024-01-01', end='2024-05-01')

# Lấy thông tin hồ sơ doanh nghiệp tổng quan
df_profile = ref.company.info(symbol='FPT')

# Lấy báo cáo tài chính (Bảng cân đối kế toán) theo năm
df_balance = fa.equity.balance_sheet(symbol='TCB', period='year')
```

***

## Các nhóm dữ liệu Vnstock hỗ trợ

Các hàm truy xuất được chia thành 6 nhóm. Phạm vi dữ liệu phụ thuộc vào từng nguồn và có thể thay đổi:

1. **Dữ liệu Cổ phiếu (Equity):** Giá cổ phiếu trong phiên (có độ trễ theo nguồn cấp), **lịch sử giá cổ phiếu**, báo cáo tài chính, hồ sơ doanh nghiệp.
2. **Chỉ số thị trường (Index):** Biến động **lịch sử giá VNINDEX**, HNX, UPCOM và các chỉ số ngành.
3. **Chứng quyền (Warrant):** Thông tin chứng quyền, giá giao dịch, ngày đáo hạn, trạng thái giao dịch.
4. **Phái sinh (Futures):** Hợp đồng tương lai phái sinh VN30 và các kỳ hạn tương ứng.
5. **Quỹ đầu tư (Fund & ETF):** Thông tin danh mục, hiệu suất quỹ mở (FMarket) và các quỹ hoán đổi danh mục.
6. **Vĩ mô & Hàng hóa (Macro & Commodities):** Tỷ giá ngoại tệ (Forex), Giá vàng (SJC), Tiền điện tử (Crypto).

***

## Cấu trúc API (API Structure Tree)

Bạn có thể gọi hàm `show_api()` để in ra toàn bộ cấu trúc các hàm phục vụ cho việc lập chỉ mục AI hoặc tra cứu nhanh:

```text
API STRUCTURE TREE - Vnstock (Unified UI)
vnstock
├── Reference
│   ├── company # Access company-specific reference data.
│   │   ├── info() [KBS] -> DataFrame # Get company overview.
│   │   ├── shareholders() [KBS] -> DataFrame # List major shareholders.
│   │   ├── officers() [KBS] -> DataFrame # List company leadership.
│   │   ├── subsidiaries() [KBS] -> DataFrame # List subsidiaries.
│   │   ├── ownership() [KBS] -> DataFrame # Company ownership structure.
│   │   ├── insider_trading() [KBS] -> DataFrame # Insider trading history.
│   │   ├── capital_history() [KBS] -> DataFrame # Capital change history.
│   │   ├── news() [KBS] -> DataFrame # Company related news.
│   │   └── events() [KBS] -> DataFrame # Upcoming corporate events.
│   ├── equity # Equity symbols and grouping reference.
│   │   ├── list() [KBS] -> DataFrame # List all equity symbols.
│   │   ├── list_by_group() [KBS] -> DataFrame # List equities by group.
│   │   ├── list_by_industry() [VCI] -> DataFrame # List equities by industry.
│   │   └── list_by_exchange() [KBS] -> DataFrame # List symbols by exchange/board.
│   ├── index # Market index reference data.
│   │   ├── list() [KBS] -> DataFrame # List all market indices.
│   │   ├── members() [KBS] -> DataFrame # List constituents of an index.
│   │   ├── groups() [KBS] -> DataFrame # List supported index groups.
│   │   └── info() [KBS] -> DataFrame # Get all market indices metadata.
│   ├── etf # ETF reference data.
│   │   └── list() [KBS] -> DataFrame # List all trackers/ETFs.
│   ├── futures # Access index futures reference data.
│   │   ├── list() [KBS] -> DataFrame # List all futures instruments.
│   │   └── info() [KBS] -> Dict # Get futures specifications.
│   ├── warrant # Access covered warrant reference data.
│   │   ├── list() [KBS] -> DataFrame # List all covered warrants.
│   │   └── info() [KBS] -> Dict # Get warrant specifications.
│   ├── bond # Bond/Debt reference data.
│   │   └── list() # List all debt/bonds.
│   ├── fund # Mutual fund reference data.
│   │   ├── list() [FMarket] -> DataFrame # List all mutual funds.
│   │   ├── top_holding() [FMarket] -> DataFrame # Fund top holdings.
│   │   ├── industry_holding() [FMarket] -> DataFrame # Fund industry allocation.
│   │   ├── nav_report() [FMarket] -> DataFrame # Fund NAV performance.
│   │   └── asset_holding() [FMarket] -> DataFrame # Fund asset allocation.
│   ├── industry # Industry classification reference.
│   │   ├── list() [VCI] -> DataFrame # ICB industry classification.
│   │   └── sectors() [KBS] -> DataFrame # List symbols grouped by industry.
│   ├── market # Market status and metadata.
│   │   └── status() [KBS] -> Dict # Get live market status.
│   └── search # Search functionality.
│   │   ├── symbol() [MSN] -> DataFrame # Search for symbols globally.
│   │   └── info() [MSN] -> DataFrame # Search for detailed asset information.
├── Market
│   ├── quote() [KBS] -> DataFrame # Global in-session quote (source-delayed).
│   ├── equity # Access equity market data.
│   │   ├── ohlcv() [KBS] -> DataFrame # Historical OHLCV bars.
│   │   ├── quote() [KBS] -> DataFrame # In-session pricing board data (source-delayed).
│   │   └── trades() [KBS] -> DataFrame # Tick-by-tick trade tape.
│   ├── index # Access index market data.
│   │   └── ohlcv() [KBS] -> DataFrame # Historical OHLCV bars for indices.
│   ├── etf # Access ETF market data.
│   │   ├── ohlcv() [KBS] -> DataFrame # Historical OHLCV bars for ETFs.
│   │   ├── quote() [KBS] -> DataFrame # In-session pricing for ETFs (source-delayed).
│   │   └── trades() [KBS] -> DataFrame # Tick-by-tick trades for ETFs.
│   ├── futures # Access futures market data.
│   │   ├── ohlcv() [KBS] -> DataFrame # Historical OHLCV bars for Futures.
│   │   ├── quote() [KBS] -> DataFrame # In-session pricing for Futures (source-delayed).
│   │   └── trades() [KBS] -> DataFrame # Tick-by-tick trades for Futures.
│   ├── warrant # Access warrant market data.
│   │   ├── ohlcv() [KBS] -> DataFrame # Historical OHLCV bars for Warrants.
│   │   ├── quote() [KBS] -> DataFrame # In-session pricing for Warrants (source-delayed).
│   │   └── trades() [KBS] -> DataFrame # Tick-by-tick trades for Warrants.
│   ├── forex # Access forex market data.
│   │   └── ohlcv() [MSN] -> DataFrame # Historical OHLCV bars for forex.
│   ├── fund # Access Mutual Fund market data.
│   │   ├── history() [FMarket] -> DataFrame # Fund NAV history.
│   │   ├── nav() [FMarket] -> DataFrame # Fund NAV history.
│   │   ├── top_holding() [FMarket] -> DataFrame # Top holdings of the fund.
│   │   ├── industry_holding() [FMarket] -> DataFrame # Industry allocation of the fund.
│   │   └── asset_holding() [FMarket] -> DataFrame # Asset class allocation of the fund.
│   ├── commodity # Access commodity market data.
│   │   └── ohlcv() [MSN] -> DataFrame # Historical OHLCV for commodities.
│   └── crypto # Access crypto market data.
│   │   └── ohlcv() [MSN] -> DataFrame # Historical OHLCV for crypto.
├── Fundamental
│   └── equity # Access equity fundamental data.
│   │   ├── balance_sheet() [KBS] -> DataFrame # Get balance sheet.
│   │   ├── cash_flow() [KBS] -> DataFrame # Get cash flow.
│   │   ├── income_statement() [KBS] -> DataFrame # Get income statement.
│   │   └── ratios() [KBS] -> DataFrame # Financial ratios.
├── Retail
│   ├── gold() # Access gold price data.
│   └── exchange_rate() # Access exchange rate data.
```

***

## Hướng dẫn sử dụng chuyên sâu

Cách gọi hàm truyền thống riêng lẻ theo từng nguồn dữ liệu hiện không còn được khuyến nghị. Để sử dụng tài liệu hướng dẫn chuyên sâu cho AI Agent hoặc tự tuỳ biến chức năng, vui lòng tham khảo [Vnstock AI Agent Skills Hub](https://vnstocks.com/skill).

***

## Tuyên bố miễn trừ trách nhiệm

Dự án **Vnstock** là hệ sinh thái công cụ Python có mã nguồn công khai, giúp bạn tự kết nối và chuẩn hoá dữ liệu từ nguồn bên thứ ba, phục vụ **mục đích nghiên cứu và tham khảo**. Vnstock **không phải nhà cung cấp dữ liệu** và không vận hành kho dữ liệu thị trường để bán lại. Dữ liệu từ nguồn có thể không đầy đủ, không liên tục, bị trùng, sai lệch hoặc làm tròn; bạn phải đối soát với nguồn chính thức trước khi giao dịch hoặc công bố.

Phần mềm được cung cấp theo hiện trạng và theo khả năng sẵn có. Trong phạm vi pháp luật cho phép, Vnstock và người đóng góp không chịu trách nhiệm đối với tổn thất gián tiếp, ngẫu nhiên, đặc biệt hoặc hệ quả, bao gồm mất lợi nhuận hoặc thiệt hại uy tín. Vnstock không cung cấp tư vấn đầu tư hay tín hiệu giao dịch. Xem đầy đủ tại [Tuyên bố miễn trừ trách nhiệm](https://vnstocks.com/onboard/mien-tru-trach-nhiem).

**Không liên kết với các nguồn dữ liệu**: Vnstock **không có quan hệ liên kết, tài trợ hay chứng thực** với bất kỳ tổ chức nào được nhắc đến trong tài liệu hoặc mã nguồn. Mọi tên gọi, thương hiệu và nhãn hiệu được nêu chỉ nhằm chỉ dẫn nguồn gốc dữ liệu và thuộc về chủ sở hữu tương ứng. Nguồn bên thứ ba gồm cả nguồn truy cập công khai và nguồn yêu cầu tài khoản hoặc quyền truy cập riêng; tình trạng có thể truy cập không đồng nghĩa quyền sử dụng không giới hạn. Bạn tuân thủ điều kiện của từng nguồn và sử dụng thư viện trong giới hạn hợp lý — truy xuất quá mức gây ảnh hưởng tới nguồn và tới chính cộng đồng người dùng.

**Dữ liệu và quyền riêng tư**: Truy vấn, xử lý và lưu trữ nghiệp vụ diễn ra trên hạ tầng do bạn lựa chọn. Các dịch vụ do Vnstock vận hành xử lý dữ liệu tài khoản, thanh toán, giấy phép, thiết bị, hạn mức, bảo mật và đo lường kỹ thuật theo [Chính sách quyền riêng tư](https://vnstocks.com/onboard/chinh-sach-quyen-rieng-tu).

***

## Giấy phép sử dụng (License)

`Vnstock` công khai mã nguồn theo giấy phép riêng: miễn phí cho cá nhân, học tập và nghiên cứu. Mã nguồn được công khai để bạn đọc, nghiên cứu và kiểm chứng, nhưng **đây không phải giấy phép nguồn mở theo chuẩn OSI**. Phạm vi tính theo số người dùng, số thiết bị đã đăng ký và hạn mức của cấp, không theo mục đích — trong phạm vi đó bạn được dùng cho cả công việc có doanh thu. Chỉ hai việc cần thoả thuận riêng bằng văn bản: phân phối lại phần mềm, và làm sản phẩm mà giá trị chính là cấp cho bên thứ ba khả năng truy xuất dữ liệu. Bản có hiệu lực: [giấy phép sử dụng](https://vnstocks.com/onboard/giay-phep-su-dung) (license-2026.09).

**Pháp lý**: [Giấy phép sử dụng](https://vnstocks.com/onboard/giay-phep-su-dung) · [Chính sách quyền riêng tư](https://vnstocks.com/onboard/chinh-sach-quyen-rieng-tu) · [Tuyên bố miễn trừ trách nhiệm](https://vnstocks.com/onboard/mien-tru-trach-nhiem)

***

## Bạn đồng hành & Nhà tài trợ

Vnstock phát triển nhờ sự chung tay của cộng đồng những người yêu công nghệ và tài chính. Mỗi sự hỗ trợ (đóng góp code, đánh dấu yêu thích hay tài trợ) đều giúp dự án duy trì được máy chủ, bổ sung tính năng mới.

<div id="badges" align="center">
    <a href="https://vnstocks.com/insiders-program">
        <img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86" alt="vnstock3 download badge"/>
    </a>
</div>

<a href="https://github.com/thinh-vu/vnstock/graphs/contributors">
   <img src="https://contributors-img.web.app/image?repo=thinh-vu/vnstock" width="800"/>
</a>

***

# Vnstock - The Source-Available Stock Analysis Toolkit for Investors

[![Vnstock Homepage](https://raw.githubusercontent.com/thinh-vu/vnstock/refs/heads/main/assets/images/vnstock-home-en.png)](https://vnstocks.com/)

<div id="badges" align="center">
    <img src="https://img.shields.io/pypi/pyversions/vnstock?logoColor=brown&style=flat" alt="Version"/>
    <img src="https://img.shields.io/github/last-commit/thinh-vu/vnstock?style=flat" alt="Commit Badge"/>
    <img src="https://img.shields.io/badge/license-Custom%20License-red?style=flat" alt="Custom License Badge"/>
</div>

## Introduction to Vnstock

Welcome to **Vnstock**, an ecosystem of Python tools for financial-market data and research workflows in Vietnam: connectors and normalization for third-party sources, technical indicators, news processing, data pipelines and guides for AI agents. The software runs on infrastructure you control; market queries go straight from there to the source. Vnstock licenses software, does not license source data, and does not operate a centralized market-data store for resale.

### Why Vnstock?

* **Free for Personal Use, Source-Available**: An accessible data extraction tool for investors, analysts, researchers, and educators. The source is published so you can read and verify it; usage terms are set by the [licence](https://vnstocks.com/onboard/giay-phep-su-dung).
* **Full-Stack Python Support**: Easy-to-use functions for building research and analysis tools.
* **Unified Data Access**: Connect to stocks, warrants, indices, futures, bonds, forex and crypto through one interface. Coverage varies by source and may change. (Note: Vnstock is a client-side connector, not a data provider).

### Join the Community

<div id="badges" align="center">
  <a href="https://www.facebook.com/groups/vnstock.official" target="_blank">
    <img src="https://img.shields.io/badge/Join%20the%20Community-Vnstock-blue?style=for-the-badge&logo=facebook" alt="Join Vnstock Community"/>
  </a>
</div>

## Installation

```bash
pip install -U vnstock
```

## Rate limits and account

The library paces its own requests so that retrieval does not burden the public sources or the user community. The limit is tied to your account:

* Guest: 20 calls/minute, no registration
* Community: 60 calls/minute, free registration
* Sponsor: 180–600 calls/minute

Sponsorship is a contribution to the project, returned as a licence to use the extended edition — it is not a fee for data or for query volume. The data belongs to the source that publishes it; you are responsible for checking and complying with each source's own terms.

```python
from vnstock import register_user
register_user()  # follow the instructions in your terminal
```

***

## Quick Start: Unified UI (Vnstock v4+)

Vnstock v4+ introduces the **Unified UI**, allowing you to fetch data without worrying about which source it comes from.

```python
from vnstock import Market, Reference, Fundamental

# Initialize data domains
market = Market()
ref = Reference()
fa = Fundamental()

# 1. Fetch historical stock prices (OHLCV)
df_history = market.equity.ohlcv(symbol='VNM', start='2024-01-01', end='2024-05-01')

# 2. Fetch general company profile
df_profile = ref.company.info(symbol='FPT')

# 3. Fetch financial data
df_balance = fa.equity.balance_sheet(symbol='TCB', period='year')
```

For more documentation and Vibe Coding guides, please refer to:

* [![Vibe Coding Guide](https://img.shields.io/badge/Vibe_Coding-Quick_Start_Guide-8B5CF6?style=for-the-badge\&logo=visualstudiocode\&logoColor=white)](https://vnstocks.com/onboard/vibe-coding)
* [![Agent Guide](https://img.shields.io/badge/Agent_Guide-Full_Documentation-24292e?style=for-the-badge\&logo=gitbook\&logoColor=white)](https://vnstocks.com/onboard/agent-guide)
* [![Get API Key](https://img.shields.io/badge/vnstocks.com-Get_Free_API_Key-0066FF?style=for-the-badge\&logo=keycdn\&logoColor=white)](https://vnstocks.com/login)

***

## Disclaimer

**Vnstock** is a source-available Python toolkit that helps you connect to and normalize data from third-party sources, intended for **research and reference**. Vnstock **is not a data provider** and does not operate a centralized market-data store for resale. Source data may be incomplete, discontinuous, duplicated, inaccurate or rounded; verify against official sources before trading or publishing.

The software is provided as-is and as-available. To the extent permitted by law, Vnstock and its contributors are not liable for indirect, incidental, special or consequential loss, including lost profit or reputational harm. Vnstock does not provide investment advice or trading signals. See the full [Disclaimer](https://vnstocks.com/onboard/mien-tru-trach-nhiem).

**No affiliation with data sources**: Vnstock is **not affiliated with, sponsored by, or endorsed by** any organisation referenced in this documentation or in the source code. All names, brands and trademarks mentioned are used solely to indicate the origin of data and remain the property of their respective owners. Third-party sources include both publicly accessible ones and ones requiring an account or private access; being reachable does not imply unlimited rights of use. You comply with each source's terms and use the library within reasonable limits — excessive retrieval harms the sources and the user community alike.

**Data and privacy**: Business queries, processing and storage happen on infrastructure you choose. Vnstock-operated services process account, payment, licence, device, quota, security and telemetry data per the [Privacy Policy](https://vnstocks.com/onboard/chinh-sach-quyen-rieng-tu).

***

## Licence

`Vnstock` is source-available under Vnstock's own licence: free for personal, study and research use. It is **not an OSI-approved open-source licence**. Scope is measured by number of users, registered devices and the tier's quota — not by purpose; within that scope you may use Vnstock for revenue-generating work. Only two things need a separate written agreement: redistributing the software, and operating a product whose primary value is giving third parties access to market data. Effective version: [licence](https://vnstocks.com/onboard/giay-phep-su-dung) (license-2026.09).

**Legal**: [Licence](https://vnstocks.com/onboard/giay-phep-su-dung) · [Privacy Policy](https://vnstocks.com/onboard/chinh-sach-quyen-rieng-tu) · [Disclaimer](https://vnstocks.com/onboard/mien-tru-trach-nhiem)

### Core Implementation Code & Architecture
#### File: `vnstock/core/converter/__init__.py`
```python

```

#### File: `vnstock/core/config/__init__.py`
```python

```

#### File: `vnstock/api/__init__.py`
```python

```

#### File: `vnstock/explorer/fmarket/__init__.py`
```python
from .fund import Fund  # noqa: F401
```

#### File: `vnstock/connector/dnse/__init__.py`
```python
from .trade import Trade  # noqa: F401
```

#### File: `vnstock/explorer/msn/__init__.py`
```python
from .listing import *  # noqa: F403
from .quote import *  # noqa: F403
```


==================================================
