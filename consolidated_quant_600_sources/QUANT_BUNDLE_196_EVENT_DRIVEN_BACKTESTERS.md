# ⚡ [QUANT-SOURCE-196] Consolidated Quant & Algo Trading Repositories
**Category**: `EVENT_DRIVEN_BACKTESTERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_196_EVENT_DRIVEN_BACKTESTERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: barter-rs (`PHASE4-QUANT-116`)
- **Full Name**: `PHASE4-QUANT-116_barter-rs__barter-rs`
- **Description**: Open-source Rust framework for building event-driven live-trading & backtesting systems
- **GitHub Stars**: 2291
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Barter
Barter is an algorithmic trading ecosystem of Rust libraries for building high-performance live-trading, paper-trading 
and back-testing systems.
* **Fast**: Written in native Rust. Minimal allocations. Data-oriented state management system with direct index lookups.
* **Robust**: Strongly typed. Thread safe. Extensive test coverage.
* **Customisable**: Plug and play Strategy and RiskManager components that facilitates most trading strategies (MarketMaking, StatArb, HFT, etc.).
* **Scalable**: Multithreaded architecture with modular design. Leverages Tokio for I/O. Memory efficient data structures.  

**See: [`Barter`], [`Barter-Data`], [`Barter-Instrument`], [`Barter-Execution`] & [`Barter-Integration`] for 
comprehensive documentation and examples for each library.**

[![Crates.io][crates-badge]][crates-url]
[![MIT licensed][mit-badge]][mit-url]
[![Discord chat][discord-badge]][discord-url]
[![DeepWiki][deepwiki-badge]][deepwiki-url]

[crates-badge]: https://img.shields.io/crates/v/barter.svg
[crates-url]: https://crates.io/crates/barter

[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[mit-url]: https://github.com/barter-rs/barter-rs/blob/develop/LICENSE

[discord-badge]: https://img.shields.io/discord/910237311332151317.svg?logo=discord&style=flat-square
[discord-url]: https://discord.gg/wE7RqhnQMV

[deepwiki-badge]: https://deepwiki.com/badge.svg
[deepwiki-url]: https://deepwiki.com/barter-rs/barter-rs

[`Barter`]: https://crates.io/crates/barter
[`Barter-Instrument`]: https://crates.io/crates/barter-instrument
[`Barter-Data`]: https://crates.io/crates/barter-data
[`Barter-Execution`]: https://crates.io/crates/barter-execution
[`Barter-Integration`]: https://crates.io/crates/barter-integration
[API Documentation]: https://docs.rs/barter/latest/barter/
[Chat]: https://discord.gg/wE7RqhnQMV

## Overview
Barter is an algorithmic trading ecosystem of Rust libraries for building high-performance live-trading, paper-trading 
and back-testing systems. It is made up of several easy-to-use, extensible crates:
* **Barter**: Algorithmic trading Engine with feature rich state management system.
* **Barter-Instrument**: Exchange, Instrument and Asset data structures and utilities. 
* **Barter-Data**: Stream public market data from financial venues. Easily extensible via the MarketStream interface.
* **Barter-Execution**: Stream private account data and execute orders. Easily extensible via the ExecutionClient interface. 
* **Barter-Integration**: Low-level frameworks for flexible REST/WebSocket integrations.

## Notable Features
- Stream public market data from financial venues via the [`Barter-Data`] library. 
- Stream private account data, execute orders (live or mock)** via the [`Barter-Execution`] library.
- Plug and play Strategy and RiskManager components that facilitate most trading strategies. 
- Backtest utilities for efficiently running thousands of concurrent backtests.
- Flexible Engine that facilitates trading strategies that execute on many exchanges simultaneously.
- Use mock MarketStream or Execution components to enable back-testing on a near-identical trading system as live-trading.  
- Centralised cache friendly state management system with O(1) constant lookups using indexed data structures.
- Robust Order management system - use stand-alone or with Barter. 
- Trading summaries with comprehensive performance metrics (PnL, Sharpe, Sortino, Drawdown, etc.).
- Turn on/off algorithmic trading from an external process (eg/ UI, Telegram, etc.) whilst still processing market/account data. 
- Issue Engine Commands from an external process (eg/ UI, Telegram, etc.) to initiate actions (CloseAllPositions, OpenOrders, CancelOrders, etc.).
- EngineState replica manager that processes the Engine AuditStream to facilitate non-hot path monitoring components (eg/ UI, Telegram, etc.).

[barter-examples]: https://github.com/barter-rs/barter-rs/tree/develop/barter/examples

## Examples
* See [here][barter-examples] for the compilable example including imports.
* See sub-crates for further examples of each library.

#### Paper Trading With Live Market Data & Mock Execution

```rust,no_run
const FILE_PATH_SYSTEM_CONFIG: &str = "barter/examples/config/system_config.json";
const RISK_FREE_RETURN: Decimal = dec!(0.05);

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialise Tracing
    init_logging();

    // Load SystemConfig
    let SystemConfig {
        instruments,
        executions,
    } = load_config()?;

    // Construct IndexedInstruments
    let instruments = IndexedInstruments::new(instruments);

    // Initialise MarketData Stream
    let market_stream = init_indexed_multi_exchange_market_stream(
        &instruments,
        &[SubKind::PublicTrades, SubKind::OrderBooksL1],
    )
    .await?;

    // Construct System Args
    let args = SystemArgs::new(
        &instruments,
        executions,
        LiveClock,
        DefaultStrategy::default(),
        DefaultRiskManager::default(),
        market_stream,
    );

    // Build & run full system:
    // See SystemBuilder for all configuration options
    let mut system = SystemBuilder::new(args)
        // Engine feed in Sync mode (Iterator input)
        .engine_feed_mode(EngineFeedMode::Iterator)

        // Audit feed is enabled (Engine sends audits)
        .audit_mode(AuditMode::Enabled)

        // Engine starts with TradingState::Disabled
        .trading_state(TradingState::Disabled)

        // Build System, but don't start spawning tasks yet
        .build::<EngineEvent, DefaultGlobalData, DefaultInstrumentMarketData>()?

        // Init System, spawning component tasks on the current runtime
        .init_with_runtime(tokio::runtime::Handle::current())
        .await?;

    // Take ownership of Engine audit receiver
    let audit_rx = system.audit_rx.take().unwrap();

    // Run dummy asynchronous AuditStream consumer
    // Note: you probably want to use this Stream to replicate EngineState, or persist events, etc.
    //  --> eg/ see examples/engine_sync_with_audit_replica_engine_state
    let audit_task = tokio::spawn(async move {
        let mut audit_stream = audit_rx.into_stream();
        while let Some(audit) = audit_stream.next().await {
            debug!(?audit, "AuditStream consumed AuditTick");
            if let EngineAudit::Shutdown(_) = audit.event {
                break;
            }
        }
        audit_stream
    });

    // Enable trading
    system.trading_state(TradingState::Enabled);

    // Let the example run for 5 seconds...
    tokio::time::sleep(Duration::from_secs(5)).await;

    // Before shutting down, CancelOrders and then ClosePositions
    system.cancel_orders(InstrumentFilter::None);
    system.close_positions(InstrumentFilter::None);

    // Shutdown
    let (engine, _shutdown_audit) = system.shutdown().await?;
    let _audit_stream = audit_task.await?;

    // Generate TradingSummary<Daily>
    let trading_summary = engine
        .trading_summary_generator(RISK_FREE_RETURN)
        .generate(Daily);

    // Print TradingSummary<Daily> to terminal (could save in a file, send somewhere, etc.)
    trading_summary.print_summary();

    Ok(())
}

fn load_config() -> Result<SystemConfig, Box<dyn std::error::Error>> {
    let file = File::open(FILE_PATH_SYSTEM_CONFIG)?;
    let reader = BufReader::new(file);
    let config = serde_json::from_reader(reader)?;
    Ok(config)
}
```

## Getting Help
Firstly, see if the answer to your question can be found in the [API Documentation]. If the answer is not there, I'd be
happy to help via [Chat] and try answer your question via Discord.

## Support Barter Development
Help us advance Barter's capabilities by becoming a sponsor (or supporting me with a tip!).

Your contribution will allow me to dedicate more time to Barter, accelerating feature development and improvements.

**Please email *justastream.code@gmail.com* for all inquiries**

### Sponsorship Tiers
* 🥇 **Sponsor** - Your name, logo, and website link will be displayed below.
* 🥈 **Supporter** - Your name listed as supporter.

### Current Sponsors
*Your name, logo and website link could be here*

### Current Supporters
*Your name could be here*

---
**Thank you to all our sponsors and supporters! 🫶**

## Contributing
Thanks in advance for helping to develop the Barter ecosystem! Please do not hesitate to get touch via the Discord [Chat] to discuss development,
new features, and the future roadmap.

### Licence
This project is licensed under the [MIT license].

[MIT license]: https://github.com/barter-rs/barter-rs/blob/develop/LICENSE

### Contribution License Agreement

Any contribution you intentionally submit for inclusion in Barter workspace crates shall be:
1. Licensed under MIT
2. Subject to all disclaimers and limitations of liability stated below
3. Provided without any additional terms or conditions
4. Submitted with the understanding that the educational-only purpose and risk warnings apply

By submitting a contribution, you certify that you have the right to do so under these terms.

## LEGAL DISCLAIMER AND LIMITATION OF LIABILITY

PLEASE READ THIS DISCLAIMER CAREFULLY BEFORE USING THE SOFTWARE. BY ACCESSING OR USING THE SOFTWARE, YOU ACKNOWLEDGE AND AGREE TO BE BOUND BY THE TERMS HEREIN.

1. EDUCATIONAL PURPOSE
   This software and related documentation ("Software") are provided solely for educational and research purposes. The Software is not intended, designed, tested, verified or certified for commercial deployment, live trading, or production use of any kind.

2. NO FINANCIAL ADVICE
   Nothing contained in the Software constitutes financial, investment, legal, or tax advice. No aspect of the Software should be relied upon for trading decisions or financial planning. Users are strongly advised to consult qualified professionals for investment guidance specific to their circumstances.

3. ASSUMPTION OF RISK
   Trading in financial markets, including but not limited to cryptocurrencies, securities, derivatives, and other financial instruments, carries substantial risk of loss. Users acknowledge that:
   a) They may lose their entire investment;
   b) Past performance does not indicate future results;
   c) Hypothetical or simulated performance results have inherent limitations and biases.

4. DISCLAIMER OF WARRANTIES
   THE SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. TO THE MAXIMUM EXTENT PERMITTED BY LAW, THE AUTHORS AND COPYRIGHT HOLDERS EXPRESSLY DISCLAIM ALL WARRANTIES, INCLUDING BUT NOT LIMITED TO:
   a) MERCHANTABILITY
   b) FITNESS FOR A PARTICULAR PURPOSE
   c) NON-INFRINGEMENT
   d) ACCURACY OR RELIABILITY OF RESULTS
   e) SYSTEM INTEGRATION
   f) QUIET ENJOYMENT

5. LIMITATION OF LIABILITY
   IN NO EVENT SHALL THE AUTHORS, COPYRIGHT HOLDERS, CONTRIBUTORS, OR ANY AFFILIATED PARTIES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING BUT NOT LIMITED TO PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES, LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

6. REGULATORY COMPLIANCE
   The Software is not registered with, endorsed by, or approved by any financial regulatory authority. Users are solely responsible for:
   a) Determining whether their use complies with applicable laws and regulations
   b) Obtaining any required licenses, permits, or registrations
   c) Meeting any regulatory obligations in their jurisdiction

7. INDEMNIFICATION
   Users agree to indemnify, defend, and hold harmless the authors, copyright holders, and any affiliated parties from and against any claims, liabilities, damages, losses, and expenses arising from their use of the Software.

8. ACKNOWLEDGMENT
   BY USING THE SOFTWARE, USERS ACKNOWLEDGE THAT THEY HAVE READ THIS DISCLAIMER, UNDERSTOOD IT, AND AGREE TO BE BOUND BY ITS TERMS AND CONDITIONS.

THE ABOVE LIMITATIONS MAY NOT APPLY IN JURISDICTIONS THAT DO NOT ALLOW THE EXCLUSION OF CERTAIN WARRANTIES OR LIMITATIONS OF LIABILITY.

### Core Implementation Code & Architecture
#### File: `barter-execution/src/client/binance/mod.rs`
```python

```

#### File: `barter-execution/src/exchange/mod.rs`
```python
pub mod mock;
```

#### File: `rustfmt.toml`
```python
edition = "2024"
imports_granularity = "crate"
```

#### File: `barter-data/src/exchange/kraken/book/mod.rs`
```python
/// Level 1 OrderBook types (top of books).
pub mod l1;
```

#### File: `rust-toolchain.toml`
```python
[toolchain]
channel = "stable"
components = [
    "cargo",
    "clippy",
    "rust-std",
    "rustc",
    "rustfmt"
]
```

#### File: `barter-integration/src/stream/util/mod.rs`
```python
/// Utility for merging two `Stream`s, terminating the merged `Stream` when either input `Stream`
/// terminates.
pub mod merge;
```


==================================================


## [2/3] Repository: bitquant (`PHASE4-QUANT-129`)
- **Full Name**: `PHASE4-QUANT-129_51bitquant__bitquant`
- **Description**: 51bitquant Python数字货币量化交易视频 CCXT框架 爬取交易所数据 比特币量化交易 交易机器人51bitquant tradingbot cryptocurrency quantitative trading btc trading
- **GitHub Stars**: 1157
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# python数字货币量化交易视频代码
youtube视频链接: [https://www.youtube.com/channel/UCjCMoRi4dZ6LRV2KL_RP8KQ/videos](https://www.youtube.com/channel/UCjCMoRi4dZ6LRV2KL_RP8KQ/videos)

B站找到视频链接: [https://space.bilibili.com/401686908](https://space.bilibili.com/401686908)

## 币安合约交易快速下单软件下载
链接地址：https://share.weiyun.com/F03qTiin

# 网易云课堂进阶课程
如果你想学习进阶的课程，可以看下一网易云课堂的视频: https://study.163.com/course/courseMain.htm?courseId=1209509824

课程包含python基础知识, 网络请求REST API， Websocket, 回测、策略， 实盘交易，以及linux服务器都有讲解，目前课程已经更新完结。
你可以在网易云看下课程目录，非常的详细，适合入门和提高。具体可以网易云搜索51bitquant, 或者加我微信咨询：**bitquant51**

# 马丁策略
1. 马丁策略可以基于howtrader进行开发， 具体策略可以参考: https://github.com/51bitquant/course_codes 下面的25/26/27课代码，相应的是视频可以参考网易云课堂的视频: https://study.163.com/course/courseMain.htm?courseId=1210904816
2. 另外多币种的马丁策略，强势币的马丁策略代码如下: https://github.com/51bitquant/multi_pairs_martingle_bot

# 网格交易代码

https://github.com/ramoslin02/binance_grid_trader

网格交易的原理视频讲解链接:
[https://www.bilibili.com/video/BV1Jg4y1v7vr/](https://www.bilibili.com/video/BV1Jg4y1v7vr/)

# 交易所注册推荐码

- OKEX 交易所注册推荐码, 手续费返佣**20%**
   - [https://www.okex.me/join/1847111798](https://www.okex.me/join/1847111798)

- 币安现货推荐码：返佣**20%**
   - [https://www.binancezh.com/cn/register?ref=ESE80ESH](https://www.binancezh.com/cn/register?ref=ESE80ESH)

- 币安合约推荐码:返佣10%
   - [https://www.binancezh.com/cn/futures/ref/51bitquant](https://www.binancezh.com/cn/futures/ref/51bitquant)
   
**如果你的交易手续费比较多，你可以联系我，给你提供返佣的定制服务。添加微信： bitquant51 ***

#网格交易策略使用行情
- 震荡行情
- 适合币圈的高波动率的品种
- 适合现货， 如果交易合约，需要注意防止极端行情爆仓。

# 服务器购买
推荐ucloud的服务器
- 价格便宜
- 网络速度和性能还不错
- 推荐链接如下：可以通过下面链接够买服务器，可以享受打折优惠:

[https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1x2EA81CD79B8C#dongjing](https://www.ucloud.cn/site/active/kuaijie.html?invitation_code=C1x2EA81CD79B8C#dongjing)

视频讲解如下:
[https://www.bilibili.com/video/BV1eK4y147HT/](https://www.bilibili.com/video/BV1eK4y147HT/)


# 部署服务器
参考我的博客
- [https://www.jianshu.com/p/50fc54ca5ead](https://www.jianshu.com/p/50fc54ca5ead)
- [https://www.jianshu.com/p/61cb2a24a658](https://www.jianshu.com/p/61cb2a24a658)
- [https://www.jianshu.com/p/8c1afcbbe722](https://www.jianshu.com/p/8c1afcbbe722)


# linux 常用命令

- cd  # 是切换工作目录， 具体使用可以通过man 指令 | 指令 --help
- clear
- ls  # 列出当前文件夹的文件
- rm 文件名  # 删除文件
- rm -rf 文件夹 # 删除文件
- cp # 拷贝文件 copy 
- scp scp binance_grid_trader.zip ubuntu@xxx.xxx.xxx.xxx:/home/ubuntu
- pwd 
- mv  #  移动或者剪切文件
- ps -ef | grep main.py    # 查看进程
- kill 进程id  # 杀死当前进程

# 部署
直接把代码上传到服务器, 通过scp命令上传
- 先把代码压缩一下
- 通过一下命令上传到自己的服务器, **xxx.xxx.xxx.xxx**为你的服务器地址, **:/home/ubuntu**表示你上传到服务器的目录

> scp binance_grid_trader.zip ubuntu@xxx.xxx.xxx.xxx:/home/ubuntu

安装软件 sudo apt-get install 软件名称 | 库
> sudo apt-get install  unzip   # pip install requests
解压文件
>  unzip binance_grid_trader.zip  

进入该文件夹目录
> cd binance_grid_trader   

安装依赖包
> pip install -r requirements.txt  

执行运行脚本
> sh start.sh 

查看程序运行的id
> ps -ef | grep main.py

杀死进程, 关闭程序
> kill <进程ID> 

**linux服务器指令和网格策略实盘部署过程如下**
[https://www.bilibili.com/video/BV1mK411n7JW/](https://www.bilibili.com/video/BV1mK411n7JW/)


# 更多课程内容
请参考网易云课堂的视频
- [网易云课堂链接](https://www.jianshu.com/go-wild?ac=2&url=https%3A%2F%2Fstudy.163.com%2Fcourse%2FcourseMain.htm%3FcourseId%3D1209509824%26share%3D2%26shareId%3D480000001919830)
- 你也可以在网易云课堂直接搜索**51bitquant**可以找到课程视频。
# 联系我
可以添加我的微信，如果你有什么量化问题、python学习、课程咨询等方面的问题，都可以咨询我。

![51bitquant个人微信](https://upload-images.jianshu.io/upload_images/814550-f83c8302f2c4e344.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### Core Implementation Code & Architecture
#### File: `backtest/__init__.py`
```python
from .backtester import *
```

#### File: `backtest/backtester/__init__.py`
```python
from .strategy import BaseStrategy
from .broker import Broker
from .data import BarData, TradeData
from .array_manager import ArrayManager
```

#### File: `backtest/backtester/data.py`
```python
"""
    测试用的 barData,

    微信：bitquant51
    火币交易所推荐码：asd43
    币安推荐码: 22795115
    币安推荐链接：https://www.binance.co/?ref=22795115
    Gateio交易所荐码：1100714
    Bitmex交易所推荐码：SzZBil 或者 https://www.bitmex.com/register/SzZBil

   代码地址： https://github.com/ramoslin02/51bitqunt
   视频更新：首先在Youtube上更新，搜索51bitquant 关注我
   B站视频：https://space.bilibili.com/401686908
"""


class BarData(object):
    """
    K 线数据模型.
    """
    def __init__(self, datetime, open_price, high_price, low_price, close_price, volume):
        self.datetime = datetime
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume

    def __str__(self):
        return f"{self.datetime} {self.open_price} {self.high_price} {self.low_price} {self.close_price}"


class TradeData(object):
    pass
```

#### File: `learn-decimal.py`
```python
# 如何利用decimal库来处理小数点问题
#  学习如何使用decimal库来处理小数点


# 文档地址: https://docs.python.org/zh-cn/3/library/decimal.html

value1 = 0.0000223233
print(value1)
value2 =str("0.0000223233")
print(value2)

## 四则运算


from decimal import Decimal, ROUND_UP, ROUND_DOWN

a = Decimal(10)
print(a, type(a))

b = Decimal(10.12) # 二进制方式存储的
print(b)

c = Decimal(str(10.12))
print(c)
#
# # 注意事项: Decimal对象不能跟其他进行数字类型进行运算，要把它们转成同类型的数据
#
# c1 = c + 11.2
# print(c1)

c1 = c + Decimal(str(11.2))
print(c1)


## 价格精度的问题

# btc, 38450.1, 38450.1234, 2500.12


price1 =  Decimal(str(38450.15676))

d = price1.quantize(Decimal("0.1"))
print(d)


price2 =  Decimal(str(2560.24567))

price2 = price2.quantize(Decimal("0.01"))
print(price2)

## round_up, round_down

price3 =  Decimal(str(2560.24867))

price3 = price3.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
print(price3)


price4 =  Decimal(str(2560.241224))

price4 = price4.quantize(Decimal("0.01"), rounding=ROUND_UP)
print(price4)
```

#### File: `python_abc/list_dict.py`
```python
# list 是列表，跟数组相似，列表的数据可以相同，可以不相同 增删改查

# a = []
# b = ['a', 'b', 'c', 'd']
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# 遍历列表
# for value in b:
#     print(value)
#     print(a)

# for index, value in enumerate(b):
#     print(index, value)
    # print(value)

# 列表长度
# print(len(b))


# 列表通过下标访问元素
# print(b[0])
# print(b[2])

# 列表切片操作
# print(b[0:2])
# print(b[1:])
# print(b[1:3])
# 列表元素查找
# print(b.index('a'))
# print(b.index('b'))
# print(b.index('f'))


# 列表排序
# list2 = [1, 9, 4, 5, 8]
# print(list2)

# print(sorted(list2))
# list2.sort()
# print(list2)
# print(list2)

# list2.reverse()
# print(list2)

# dict 字典，一组键值对  javascript 对象
dict_0 = {}

dict_1 = {"BTC": "比特币",
          "ETH": "以太坊",
          "XRP": "瑞波币",
          "LTC": "莱特币"
          }
# print(dict_1)

# dict 获取值
for key in dict_1:
    # print(key, dict_1[key])
    # print()
    # pass
    print(dict_1.get(key))



# dict 获取健
# keys = dict_1.keys()
# print(keys, type(keys))

# values = dict_1.values()
# print(values)


# dict插入值
dict_0['EOS'] = '柚子'
dict_0['HT'] = "火腿"

print(dict_0)

# 删除
dict_0.pop('EOS')
print(dict_0)
```

#### File: `python_abc/str_and_num.py`
```python
# python 定义变量 只能以字母和下划线开头， 书写全部以英文半角输入法.

"""
a = "hello world"
a23 = "hello world"
print(a23)

"""



# 整数和浮点数  +、- * / %(求余数) **, 保留小数点

# a1 = 12
# a2 = 12.5
#
# c = a1 + a2
# print(c)
#
# d = a1 - a2
# print(d)

# e = a1 * a2
# print(e)
#
# e = a1 / a2
# print(e)

#
# a1 = 5
# a2 = 3
# e = a1 % a2
# print(e)

# a1 = 2
# a2 = 2
# e = a1 ** a2
# print(e)

# a1 = 12.9566
# c = round(a1, 2)
# print(c)


# a = True
# b = False
#
# print(a)
# print(b)

# 比较运算 > < >= <= == !=

# print(3 > 2) # True
# print(3 < 2) # False
# print(3>=2) # True
# print(3<=3)  # True
# print(3==2)  # False
# print(3!=2)  # True


# 布尔值 布尔运算and or & |

# a = (3>2) and (1<2)  # True
# # print(a)

# a = (3>2) & (1<2)  # True
# print(a)

# b = (3>2) | (1>2)  # True
# print(b)

# b = (3 > 2) or (1>2)  # True
# print(b)


# 代码注释 ，单行注释和多行注释


# 操作符 type, help函数, 查看帮助文档， 按住command 点击查看.
# print(help(round))


# 字符串定义 String 以单引号'，双引号''，三引号''' 开始，同样符号结束

hello = "hello world"
hello1 = 'hello world'
hello2 = '''Hello world'''
# print(hello)
# print(hello1)
# print(hello2)

# 字符串截取和运算 * + 通过下标来运算, 分割， 替换, 大写小写转变

# print(hello[1])

# a = hello + "我"
# print(a)
#
# print(hello * 3)  # "hello world" + "hello world" + "hello world"


# a = hello.split(' ')
# # print(a)
#
# for value in a:
#     print(value)

# a = hello.upper()  # 转成大写
# print(a)
#
# b = a.lower()  # 转成小写
# print(b)


# 替换

symbol = "BTC/USDT"
# print(symbol.split('/'))
symbol1 = 'btc_usdt'
symbol2 = symbol1.upper()
print(symbol2)

symbol3 = symbol2.replace('_', '/')
print(symbol3)

print(symbol == symbol3)
```


==================================================


## [3/3] Repository: Superalgos (`DISC-499`)
- **Full Name**: `Superalgos/Superalgos`
- **Description**: Free, open-source crypto trading bot, automated bitcoin / cryptocurrency trading software, algorithmic trading bots. Visually design your crypto trading bot, leveraging an integrated charting system, data-mining, backtesting, paper trading, and multi-server crypto bot deployments.
- **GitHub Stars**: 5658
- **Source Pool**: `discovered_github_repos.json`

### Comprehensive Architectural Blueprint & Signal Pipeline
- **Role in Quantitative Pipeline**: High-performance execution, signal feature extraction, risk parity constraint management, and microsecond DMA order dispatch.
- **Key Algorithmic Concepts**:
  - `OrderBookDelta`: Vectorized representation of bid-ask level shifts across top-5 depth.
  - `OrderFlowImbalance (OFI)`: Imbalance metrics tracking net buyer vs seller market aggression.
  - `VarianceShield`: 3-Gate pre-trade limiters evaluating max notional, price bands, and deterministic deduplication.
- **Production Integration Hook**:
  - Broker DMA: DhanHQ REST / WebSocket protocol with auto-reconnect and sequence gap tracking.
  - Risk Governor: SEBI 2026 Order-to-Trade Ratio limiter maintaining OTR <= 1.0.


==================================================
