# ⚡ [QUANT-SOURCE-075] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_075_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ccxt (`WHEEL_ccxt`)
- **Full Name**: `ccxt`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# CCXT – CryptoCurrency eXchange Trading Library

[![NPM Downloads](https://img.shields.io/npm/dy/ccxt.svg)](https://www.npmjs.com/package/ccxt) [![npm](https://img.shields.io/npm/v/ccxt.svg)](https://npmjs.com/package/ccxt) [![PyPI](https://img.shields.io/pypi/v/ccxt.svg)](https://pypi.python.org/pypi/ccxt) [![NuGet version](https://img.shields.io/nuget/v/ccxt)](https://www.nuget.org/packages/ccxt) [![GoDoc](https://img.shields.io/github/v/tag/ccxt/ccxt?label=go)](https://godoc.org/github.com/ccxt/ccxt/go/v4) [![Mvn](https://badges.mvnrepository.com/badge/io.github.ccxt/ccxt/badge.svg?label=mvn)](https://mvnrepository.com/artifact/io.github.ccxt/ccxt) [![Packagist](https://img.shields.io/packagist/v/ccxt/ccxt)](https://packagist.org/packages/ccxt/ccxt) [![Crates.io](https://img.shields.io/crates/v/ccxt.svg)](https://crates.io/crates/ccxt) [![Supported Exchanges](https://img.shields.io/badge/exchanges-104-blue.svg)](https://github.com/ccxt/ccxt/wiki/Exchange-Markets) [![CCXT Chat in Telegram](https://telegram-badge.vercel.app/api/telegram-badge?channelId=@ccxt_chat&label=chat)](https://t.me/ccxt_chat) [![CCXT Discord Server](https://img.shields.io/discord/690203284119617602?logo=discord&logoColor=white)](https://discord.gg/ccxt) [![Follow CCXT at x.com](https://img.shields.io/twitter/follow/ccxt_official.svg?style=social&label=CCXT)](https://x.com/ccxt_official)

A crypto trading API with more than 100 exchanges and prediction markets in JavaScript / TypeScript / Python / C# / PHP / Go / Java / Rust.

### [Install](#install) · [Usage](#usage) · [Manual](https://github.com/ccxt/ccxt/wiki) · [FAQ](https://github.com/ccxt/ccxt/wiki/FAQ) · [Examples](https://github.com/ccxt/ccxt/tree/master/examples) · [Contributing](https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md) · [Disclaimer](#disclaimer) · [Social](#social)

The **CCXT** library is used to connect and trade with cryptocurrency exchanges worldwide. It provides quick access to market data for storage, analysis, visualization, indicator development, algorithmic trading, strategy backtesting, bot programming, and related software engineering.

It is intended to be used by **coders, developers, technically-skilled traders, data-scientists and financial analysts** for building trading algorithms.

Current feature list:
- supports 100+ cryptocurrency exchanges and prediction markets:
  - Polymarket
  - Kalshi
  - Hyperliquid
  - Limitless
  - Myriad
  - more coming soon!
- implements public and private APIs, both REST and WebSocket
- optionally normalizes data for cross-exchange analytics and arbitrage
- has an out of the box unified API that is extremely easy to integrate
- ideal for AI agents, LLMs and vibe coding
- works in Node 18+, Python 3, PHP 8.1+, netstandard2.0/2.1, Go 1.20+, Java 21+ and web browsers

## Sponsored Promotion

[![Enjoy VIP+2 tier on Bitget when migrating from BitMEX](https://github.com/user-attachments/assets/51386fa3-a95c-4bef-aa3b-2d4ee1d8f5c3)](https://forms.gle/VLDTR7ushknvsUGH7)

[![Unlock VIP3 on BTSE and earn up to $2,500 in the BTSE × CCXT Trading Competition](https://github.com/user-attachments/assets/5acdc47c-6e49-429b-bda7-dc0628a00971)](https://www.btse.com/en/events/btsexccxt20260831?ref=o2tjIXx5)

## See Also

- <sub>[![Freqtrade](https://user-images.githubusercontent.com/1294454/114340585-8e35fa80-9b60-11eb-860f-4379125e2db6.png)](https://www.freqtrade.io)</sub> **[Freqtrade](https://www.freqtrade.io)** – leading opensource cryptocurrency algorithmic trading software!
- <sub>[![OctoBot](https://user-images.githubusercontent.com/1294454/132113722-007fc092-7530-4b41-b929-b8ed380b7b2e.png)](https://www.octobot.online)</sub> **[OctoBot](https://www.octobot.online)** – cryptocurrency trading bot with an advanced web interface.
- <sub>[![TokenBot](https://user-images.githubusercontent.com/1294454/152720975-0522b803-70f0-4f18-a305-3c99b37cd990.png)](https://tokenbot.com/?utm_source=github&utm_medium=ccxt&utm_campaign=algodevs)</sub> **[TokenBot](https://tokenbot.com/?utm_source=github&utm_medium=ccxt&utm_campaign=algodevs)** – discover and copy the best algorithmic traders in the world.

## Certified Cryptocurrency Exchanges


|logo                                                                                                                                                                         |id             |name                                                                                     |ver                                                                                                                                  |type                                                                                                    |certified                                                                                                                    |pro                                                                                                |discount                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![binance](https://github.com/user-attachments/assets/e9419b93-ccb0-46aa-9bff-c883f096274b)](https://accounts.binance.com/register?ref=CCXTCOM)                            | binance       | [Binance](https://accounts.binance.com/register?ref=CCXTCOM)                            | [![API Version *](https://img.shields.io/badge/*-lightgray)](https://developers.binance.com/en)                                     | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with Binance using CCXT's referral link for a 10% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d10%25&color=orange)](https://accounts.binance.com/register?ref=CCXTCOM)        |
| [![binanceusdm](https://github.com/user-attachments/assets/871cbea7-eebb-4b28-b260-c1c91df0487a)](https://accounts.binance.com/register?ref=CCXTCOM)                        | binanceusdm   | [Binance USDⓈ-M](https://accounts.binance.com/register?ref=CCXTCOM)                     | [![API Version *](https://img.shields.io/badge/*-lightgray)](https://binance-docs.github.io/apidocs/futures/en/)                    | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with Binance USDⓈ-M using CCXT's referral link for a 10% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d10%25&color=orange)](https://accounts.binance.com/register?ref=CCXTCOM) |
| [![binancecoinm](https://github.com/user-attachments/assets/387cfc4e-5f33-48cd-8f5c-cd4854dabf0c)](https://accounts.binance.com/register?ref=CCXTCOM)                       | binancecoinm  | [Binance COIN-M](https://accounts.binance.com/register?ref=CCXTCOM)                     | [![API Version *](https://img.shields.io/badge/*-lightgray)](https://binance-docs.github.io/apidocs/delivery/en/)                   | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with Binance COIN-M using CCXT's referral link for a 10% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d10%25&color=orange)](https://accounts.binance.com/register?ref=CCXTCOM) |
| [![bybit](https://github.com/user-attachments/assets/97a5d0b3-de10-423d-90e1-6620960025ed)](https://www.bybit.com/invite?ref=XDK12WP)                                       | bybit         | [Bybit](https://www.bybit.com/invite?ref=XDK12WP)                                       | [![API Version 5](https://img.shields.io/badge/5-lightgray)](https://bybit-exchange.github.io/docs/inverse/)                        | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![okx](https://user-images.githubusercontent.com/1294454/152485636-38b19e4a-bece-4dec-979a-5982859ffc04.jpg)](https://www.okx.com/join/CCXTCOM)                            | okx           | [OKX](https://www.okx.com/join/CCXTCOM)                                                 | [![API Version 5](https://img.shields.io/badge/5-lightgray)](https://www.okx.com/docs-v5/en/)                                       | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with OKX using CCXT's referral link for a 20% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d20%25&color=orange)](https://www.okx.com/join/CCXTCOM)                             |
| [![gate](https://github.com/user-attachments/assets/b4fd9d41-eaed-46fe-8a7b-b2677edface0)](https://www.gate.com/share/CCXTGATE)                                             | gate          | [Gate](https://www.gate.com/share/CCXTGATE)                                             | [![API Version 4](https://img.shields.io/badge/4-lightgray)](https://www.gate.com/docs/developers/apiv4/en)                         | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with Gate using CCXT's referral link for a 20% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d20%25&color=orange)](https://www.gate.com/share/CCXTGATE)                         |
| [![kucoin](https://user-images.githubusercontent.com/51840849/87295558-132aaf80-c50e-11ea-9801-a2fb0c57c799.jpg)](https://www.kucoin.com/ucenter/signup?rcode=E5wkqe)       | kucoin        | [KuCoin](https://www.kucoin.com/ucenter/signup?rcode=E5wkqe)                            | [![API Version 2](https://img.shields.io/badge/2-lightgray)](https://docs.kucoin.com)                                               | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![kucoinfutures](https://user-images.githubusercontent.com/1294454/147508995-9e35030a-d046-43a1-a006-6fabd981b554.jpg)](https://futures.kucoin.com/?rcode=E5wkqe)          | kucoinfutures | [KuCoin Futures](https://futures.kucoin.com/?rcode=E5wkqe)                              | [![API Version 2](https://img.shields.io/badge/2-lightgray)](https://docs.kucoin.com)                                               | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![bitget](https://github.com/user-attachments/assets/b54bb4c2-416d-4231-8968-85a77748ba45)](https://www.bitget.com/expressly?languageType=0&channelCode=ccxt&vipCode=tg9j) | bitget        | [Bitget](https://www.bitget.com/expressly?languageType=0&channelCode=ccxt&vipCode=tg9j) | [![API Version 2](https://img.shields.io/badge/2-lightgray)](https://www.bitget.com/api-doc/common/intro)                           | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![hyperliquid](https://github.com/user-attachments/assets/550769b3-d270-461e-9e02-8e8b8c0210b8)](https://app.hyperliquid.xyz/)                                             | hyperliquid   | [Hyperliquid](https://app.hyperliquid.xyz/)                                             | [![API Version 1](https://img.shields.io/badge/1-lightgray)](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api)    | ![DEX - Distributed EXchange](https://img.shields.io/badge/DEX-blue.svg "DEX - Distributed EXchange")  | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![bitmex](https://github.com/user-attachments/assets/3360333d-35a6-4503-bbba-92a6bc0c174f)](https://www.bitmex.com/app/register/NZTR1q)                                    | bitmex        | [BitMEX](https://www.bitmex.com/app/register/NZTR1q)                                    | [![API Version 1](https://img.shields.io/badge/1-lightgray)](https://www.bitmex.com/app/apiOverview)                                | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with BitMEX using CCXT's referral link for a 10% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d10%25&color=orange)](https://www.bitmex.com/app/register/NZTR1q)                |
| [![bingx](https://github-production-user-asset-6210df.s3.amazonaws.com/1294454/253675376-6983b72e-4999-4549-b177-33b374c195e3.jpg)](https://bingx.com/invite/OHETOM)        | bingx         | [BingX](https://bingx.com/invite/OHETOM)                                                | [![API Version 1](https://img.shields.io/badge/1-lightgray)](https://bingx-api.github.io/docs/)                                     | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![htx](https://user-images.githubusercontent.com/1294454/76137448-22748a80-604e-11ea-8069-6e389271911d.jpg)](https://www.htx.com/invite/en-us/1h?invite_code=6rmm2223)     | htx           | [HTX](https://www.htx.com/invite/en-us/1h?invite_code=6rmm2223)                         | [![API Version 1](https://img.shields.io/badge/1-lightgray)](https://huobiapi.github.io/docs/spot/v1/en/)                           | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with HTX using CCXT's referral link for a 15% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d15%25&color=orange)](https://www.htx.com/invite/en-us/1h?invite_code=6rmm2223)     |
| [![mexc](https://user-images.githubusercontent.com/1294454/137283979-8b2a818d-8633-461b-bfca-de89e8c446b2.jpg)](https://www.mexc.com/register?inviteCode=mexc-1FQ1GNu1)     | mexc          | [MEXC Global](https://www.mexc.com/register?inviteCode=mexc-1FQ1GNu1)                   | [![API Version 3](https://img.shields.io/badge/3-lightgray)](https://www.mexc.com/api-docs/spot-v3/introduction)                    | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![cryptocom](https://user-images.githubusercontent.com/1294454/147792121-38ed5e36-c229-48d6-b49a-48d05fc19ed4.jpeg)](https://crypto.com/exch/kdacthrnxt)                   | cryptocom     | [Crypto.com](https://crypto.com/exch/kdacthrnxt)                                        | [![API Version 2](https://img.shields.io/badge/2-lightgray)](https://exchange-docs.crypto.com/exchange/v1/rest-ws/index.html)       | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with Crypto.com using CCXT's referral link for a 75% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d75%25&color=orange)](https://crypto.com/exch/kdacthrnxt)                    |
| [![coinex](https://user-images.githubusercontent.com/51840849/87182089-1e05fa00-c2ec-11ea-8da9-cc73b45abbbc.jpg)](https://www.coinex.com/register?refer_code=yw5fz)         | coinex        | [CoinEx](https://www.coinex.com/register?refer_code=yw5fz)                              | [![API Version 2](https://img.shields.io/badge/2-lightgray)](https://docs.coinex.com/api/v2)                                        | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![hashkey](https://github.com/user-attachments/assets/3dd65db2-5da9-4ecc-93ac-6d420f36261c)](https://global.hashkey.com/en-US/register/invite?invite_code=82FQUN)          | hashkey       | [HashKey Global](https://global.hashkey.com/en-US/register/invite?invite_code=82FQUN)   | [![API Version 1](https://img.shields.io/badge/1-lightgray)](https://hashkeyglobal-apidoc.readme.io/)                               | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) |                                                                                                                                                                                                              |
| [![woo](https://user-images.githubusercontent.com/1294454/150730761-1a00e5e0-d28c-480f-9e65-089ce3e6ef3b.jpg)](https://woox.io/register?ref=DIJT0CNL)                       | woo           | [WOO X](https://woox.io/register?ref=DIJT0CNL)                                          | [![API Version 1](https://img.shields.io/badge/1-lightgray)](https://developer.woox.io/)                                            | ![CEX – Centralized EXchange](https://img.shields.io/badge/CEX-green.svg "CEX – Centralized EXchange") | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with WOO X using CCXT's referral link for a 35% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d35%25&color=orange)](https://woox.io/register?ref=DIJT0CNL)                      |
| [![woofipro](https://github.com/user-attachments/assets/9ba21b8a-a9c7-4770-b7f1-ce3bcbde68c1)](https://dex.woo.org/en/trade?ref=CCXT)                                       | woofipro      | [WOOFI PRO](https://dex.woo.org/en/trade?ref=CCXT)                                      | [![API Version 1](https://img.shields.io/badge/1-lightgray)](https://orderly.network/docs/build-on-omnichain/building-on-omnichain) | ![DEX - Distributed EXchange](https://img.shields.io/badge/DEX-blue.svg "DEX - Distributed EXchange")  | [![CCXT Certified](https://img.shields.io/badge/CCXT-Certified-green.svg)](https://github.com/ccxt/ccxt/wiki/Certification) | [![CCXT Pro](https://img.shields.io/badge/CCXT-Pro-black)](https://docs.ccxt.com/docs/pro-manual) | [![Sign up with WOOFI PRO using CCXT's referral link for a 5% discount!](https://img.shields.io/static/v1?label=Fee&message=%2d5%25&color=orange)](https://dex.woo.org/en/trade?ref=CCXT)                    |

## Supported Cryptocurrency Exchanges
<!--- init list -->The CCXT library currently supports the following 104 cryptocurrency exchange markets and trading APIs:

|logo                                                                                                                                                                                                 |id                     |name                                                                                         |ver                                                                                                                                               |type                                                                                                    |certified                                  
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `python/ccxt/abstract/__init__.py`
```python

```

#### File: `python/ccxt/abstract/prediction/__init__.py`
```python

```

#### File: `python/ccxt/static_dependencies/starknet/__init__.py`
```python

```

#### File: `python/ccxt/static_dependencies/starknet/hash/__init__.py`
```python

```

#### File: `python/ccxt/static_dependencies/starknet/utils/__init__.py`
```python

```

#### File: `python/ccxt/static_dependencies/starknet/models/__init__.py`
```python

```


==================================================


## [2/3] Repository: cooc (`WHEEL_cooc`)
- **Full Name**: `cooc`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Trade Decomposition
Trade Co-occurrence, Trade Flow Decomposition, and Conditional Order Imbalance

This package contains tools based on the paper [Trade Co-occurrence, Trade Flow Decomposition, and Conditional Order Imbalance in Equity Markets](https://arxiv.org/pdf/2209.10334) by Yutong Lu, Gesine Reinert and Mihai Cucuringu. The package is managed using [uv](https://docs.astral.sh/uv/). To install, use 

```uv sync```

![Sample decomposition](https://github.com/Tripudium/tradedecomp/blob/main/doc/images/trades_2025-02-23%2009%3A00%3A00_0%3A00%3A30.png)

An example of how to use this package, how to load book and trade data and carry out the trade classification is found in this [notebook](examples/intro.ipynb).

To handle data, this package makes use of ```dspy```:

```git clone git@github.com:Tripudium/dspy.git
cd /path/to/dspy/
uv sync
uv build
uv pip install -e /path/to/dspy```

Then in the current path

```uv add /path/to/dspy```

There is probably a more elegant way of doing this using paths.

### Core Implementation Code & Architecture
#### File: `src/cooc/__init__.py`
```python
#from . import polars_ext

#__all__ = ['polars_ext']
```

#### File: `pyproject.toml`
```python
[project]
name = "cooc"
version = "0.1.0"
description = "Trade Co-occurrence and Conditional Order Imbalance"
readme = "README.md"
authors = [
    { name = "Martin", email = "martin@tripudium.tech" }
]
requires-python = ">=3.13"
dependencies = [
    "bybit-bulk-downloader>=1.2.0",
    "cython>=3.0.12",
    "dspy",
    "hawkes>=1.0.0",
    "ipykernel>=6.29.5",
    "matplotlib>=3.10.0",
    "pandas>=2.2.3",
    "pathlib>=1.0.1",
    "polars>=1.22.0",
    "polugins>=0.5.1",
    "pyarrow>=19.0.1",
    "pybit>=5.9.0",
    "pytest>=8.3.4",
    "pytz>=2025.1",
    "seaborn>=0.13.2",
    "tqdm>=4.67.1",
]

[project.scripts]
cooc = "cooc:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = ["pytest"]

[tool.uv.sources]
dspy = { path = "../dspy/dist/dspy-0.1.0-py3-none-any.whl" }

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "--maxfail=1 --disable-warnings -q"
testpaths = [
    "tests",
]
```

#### File: `tests/test_classify.py`
```python
import pytest
import polars as pl
from cooc.classify import classify_trades

@pytest.fixture
def df():
    data = {
        "ts": [
            "2025-02-23 09:00:00",
            "2025-02-23 09:00:00",
            "2025-02-23 09:00:10",
            "2025-02-23 09:00:20",
            "2025-02-23 09:00:40",
            "2025-02-23 09:01:40",
            "2025-02-23 09:02:30",
            "2025-02-23 09:02:40",
            "2025-02-23 09:03:30",
            "2025-02-23 09:03:40"
        ],
        "product": [
            "BTCUSDT", "SOLUSDT", "SOLUSDT", "ETHUSDT", "BTCUSDT",
            "ETHUSDT", "ETHUSDT", "BTCUSDT", "SOLUSDT", "SOLUSDT"
        ],
        "trade_id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "prc": [100, 102, 101, 103, 104, 103, 101, 100, 99, 98],
        "qty": [10, 15, 12, 20, -18, 21, -15, 12, -10, 10]
    }

    df = pl.DataFrame(data)
    df = df.with_columns(
        pl.col("ts").str.strptime(pl.Datetime, format="%Y-%m-%d %H:%M:%S")
    )
    return df

@pytest.fixture
def expected():
    return ['nis-c', 'nis-b', 'nis-b', 'nis-c', 'nis-c', 'iso', 'nis-c', 'nis-c', 'nis-s', 'nis-s']

def test_classify_trades(df, expected):
    prods = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT']
    delta = "30s"

    df = classify_trades(df, prods, "ts", delta)
    assert df.shape[0] == 10
    assert df.shape[1] == 6
    assert df.columns == ['ts', 'product', 'trade_id', 'prc', 'qty', 'trade_type']
    assert df['trade_type'].to_list() == expected
```

#### File: `scripts/rename.py`
```python
#!/usr/bin/env python3
import re
import sys
from pathlib import Path

def transform_filename(filename):
    """
    Replace any substring enclosed within underscores (e.g., _text_)
    with the same text prefixed by '24' (resulting in _24text_).
    """
    return re.sub(r'_(.*?)_', lambda m: f"_24{m.group(1)}_", filename)

def rename_files_in_directory(directory_path):
    """
    Iterate over all files in the specified directory and rename each file
    based on the transformation provided by transform_filename().
    """
    directory = Path(directory_path)
    for file in directory.iterdir():
        if file.is_file():
            new_name = transform_filename(file.name)
            # Only rename if transformation changes the filename.
            if new_name != file.name:
                new_file = file.with_name(new_name)
                try:
                    file.rename(new_file)
                    print(f"Renamed: {file.name} -> {new_name}")
                except Exception as e:
                    print(f"Error renaming {file.name} to {new_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    
    if not Path(directory_path).is_dir():
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)

    rename_files_in_directory(directory_path)
    print("Renaming process completed.")
```

#### File: `src/cooc/classify.py`
```python
"""
Trade classification module
"""

import polars as pl
from datetime import timedelta
from cooc.utils import str_to_timedelta

def classify_trades(df: pl.DataFrame, products: list, ts_col: str, delta: str | timedelta, mapping: dict = {0: "iso", 1: "nis-c", 2: "nis-s", 3: "nis-b"}):
    """
    Label trades based on co-trading relationships

    Args:
        df (pl.DataFrame): The dataframe containing the trades
        prods (list): The list of products to label
        delta (str): The time delta to use for the rolling window
        mapping (dict): The mapping of condition codes to trade types
    Returns:
        pl.DataFrame: The dataframe with the labeled trades
    """
    if isinstance(delta, str):
        delta = str_to_timedelta(delta)

    df = df.with_columns([
        (pl.col("product") == prod).cast(pl.Int64).alias(f"{prod}_flag") for prod in products
        ])
    
    df = df.with_columns([
        pl.sum(f"{prod}_flag").rolling(
            index_column=ts_col,
            period=2*delta,
            offset=-delta,
            closed="both"
            ).alias(f"{prod}_count") for prod in products
        ])

    flag_columns = [pl.col(f"{prod}_flag")  for prod in products]
    count_columns = [pl.col(f"{prod}_count") for prod in products]
    adjusted_counts = [(count - flag).alias(f"{prod}_count") for count, flag, prod in zip(count_columns, flag_columns, products)]
    product_exprs = [count * flag for count, flag in zip(count_columns, flag_columns)]

    df = df.with_columns(
        adjusted_counts
    ).with_columns(
        pl.sum_horizontal(count_columns).alias("total_count")
    ).with_columns(
        pl.sum_horizontal(product_exprs).alias("same_count")
    ).with_columns(
        (pl.col("total_count")-pl.col("same_count")).alias("other_count")
    ).drop(count_columns + flag_columns + ["total_count"])

    mapping_str = {str(i): v for i, v in mapping.items()}
    df = df.with_columns(
        (2 * (pl.col("same_count") > 0).cast(pl.Int8) +
        (pl.col("other_count") > 0).cast(pl.Int8)).cast(pl.Utf8).alias("trade_code")
    ).with_columns(
        pl.col("trade_code").replace(mapping_str).alias("trade_type")
    ).drop(["same_count", "other_count", "trade_code"])

    return df
```

#### File: `src/cooc/features.py`
```python
"""
Functions for calculating features from trade data.
"""

from datetime import timedelta
from cooc.utils import str_to_timedelta, timedelta_to_str
import polars as pl

# Freatures for trades

def add_side(df: pl.DataFrame, col: str='qty') -> pl.DataFrame:
    """
    Add a side column to the DataFrame.
    """
    df = df.with_columns(
        pl.when(pl.col(col) > 0).then(1).otherwise(-1).alias('side'))
    return df

def add_size(df: pl.DataFrame, col: str='qty') -> pl.DataFrame:
    """
    Add a size column to the DataFrame.
    """
    df = df.with_columns(
        pl.col(col).abs().alias('size'))
    return df

def coi(df: pl.DataFrame, ts_col: str, delta: str | timedelta, type: str) -> pl.DataFrame:
    """
    Calculate the Conditional Order Imbalance (COI) for a given dataframe.
    """
    if isinstance(delta, str):
        delta = str_to_timedelta(delta)
    delta_str = timedelta_to_str(delta)

    assert ts_col in df.columns
    assert "qty" in df.columns
    assert type in ["nis", "nis-c", "nis-b", "nis-s"]
    
    has_side, has_size = True, True
    if "side" not in df.columns:
        has_side = False    
        df = add_side(df)
    if "size" not in df.columns:
        has_size = False
        df = add_size(df)

    df = df.with_columns([
        pl.when((pl.col("side") == 1) & (pl.col("trade_type") == type))
          .then(pl.col("size"))
          .otherwise(pl.lit(0))
          .alias("buy_filter"),
        pl.when((pl.col("side") == -1) & (pl.col("trade_type") == type))
          .then(pl.col("size"))
          .otherwise(pl.lit(0))
          .alias("sell_filter")
    ])

    buy_col = f"N_buy_{type}_{delta_str}"
    sell_col = f"N_sell_{type}_{delta_str}"

    df = df.with_columns([  
        pl.sum("buy_filter").rolling(
            index_column=ts_col,
            period=delta,
            closed="left" # don't include the current row in the sum / don't look back
            ).alias(buy_col),
        pl.sum("sell_filter").rolling(
            index_column=ts_col,
            period=delta,
            closed="left" # don't include the current row in the sum / don't look back
            ).alias(sell_col)
    ]).drop(["buy_filter", "sell_filter"])
    
    df = df.with_columns(
        pl.when(pl.col(buy_col) + pl.col(sell_col) > 0)
          .then((pl.col(buy_col) - pl.col(sell_col)) / (pl.col(buy_col) + pl.col(sell_col))
         ).otherwise(pl.lit(0)).alias(f"coi_{type}_{delta_str}")
    ).drop([buy_col, sell_col])

    if not has_side:
        df = df.drop(["side"])
    if not has_size:
        df = df.drop(["size"])

    return df
```


==================================================


## [3/3] Repository: cvxpy (`WHEEL_cvxpy`)
- **Full Name**: `cvxpy`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
CVXPY
=====================
[![Build Status](https://github.com/cvxpy/cvxpy/actions/workflows/build.yml/badge.svg?event=push)](https://github.com/cvxpy/cvxpy/actions/workflows/build.yml)
![PyPI - downloads](https://img.shields.io/pypi/dm/cvxpy.svg?label=Pypi%20downloads)
![Conda - downloads](https://img.shields.io/conda/dn/conda-forge/cvxpy.svg?label=Conda%20downloads)
[![Discord](https://img.shields.io/badge/Chat-Discord-Blue?color=5865f2)](https://discord.gg/4urRQeGBCr)
[![Benchmarks](http://img.shields.io/badge/benchmarked%20by-asv-blue.svg?style=flat)](https://cvxpy.github.io/benchmarks/)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/cvxpy/cvxpy/badge)](https://api.securityscorecards.dev/projects/github.com/cvxpy/cvxpy)

**The CVXPY documentation is at [cvxpy.org](https://www.cvxpy.org/).**

*We are building a CVXPY community on [Discord](https://discord.gg/4urRQeGBCr). Join the conversation! For issues and long-form discussions, use [Github Issues](https://github.com/cvxpy/cvxpy/issues) and [Github Discussions](https://github.com/cvxpy/cvxpy/discussions).*

**Contents**
- [Installation](#installation)
- [Getting started](#getting-started)
- [Issues](#issues)
- [Community](#community)
- [Contributing](#contributing)
- [Team](#team)
- [Citing](#citing)


CVXPY is a Python-embedded modeling language for convex optimization problems. It allows you to express your problem in a natural way that follows the math, rather than in the restrictive standard form required by solvers.

For example, the following code solves a least-squares problem where the variable is constrained by lower and upper bounds:

```python3
import cvxpy as cp
import numpy

# Problem data.
m = 30
n = 20
numpy.random.seed(1)
A = numpy.random.randn(m, n)
b = numpy.random.randn(m)

# Construct the problem.
x = cp.Variable(n)
objective = cp.Minimize(cp.sum_squares(A @ x - b))
constraints = [0 <= x, x <= 1]
prob = cp.Problem(objective, constraints)

# The optimal objective is returned by prob.solve().
result = prob.solve()
# The optimal value for x is stored in x.value.
print(x.value)
# The optimal Lagrange multiplier for a constraint
# is stored in constraint.dual_value.
print(constraints[0].dual_value)
```

With CVXPY, you can model
* convex optimization problems,
* mixed-integer convex optimization problems,
* geometric programs,
* quasiconvex programs, and
* nonlinear programs

CVXPY is not a solver. It relies upon the open source solvers 
[Clarabel](https://github.com/oxfordcontrol/Clarabel.rs), [SCS](https://github.com/bodono/scs-python),
[OSQP](https://github.com/oxfordcontrol/osqp) and [HiGHS](https://github.com/ERGO-Code/HiGHS).
Additional solvers are [available](https://www.cvxpy.org/tutorial/solvers/index.html#choosing-a-solver),
but must be installed separately.

CVXPY began as a Stanford University research project. It is now developed by
many people, across many institutions and countries.


## Installation
CVXPY is available on PyPI, and can be installed with
```
pip install cvxpy
```

CVXPY can also be installed with conda, using
```
conda install -c conda-forge cvxpy
```

CVXPY has the following dependencies:

- Python >= 3.11
- Clarabel >= 0.5.0
- OSQP >= 1.0.0
- SCS >= 3.2.4.post1
- NumPy >= 2.0.0
- SciPy >= 1.13.0
- highspy >= 1.11.0
- sparsediffpy >= 0.2.2

For detailed instructions, see the [installation
guide](https://www.cvxpy.org/install/index.html).

## Getting started
To get started with CVXPY, check out the following:
* [official CVXPY tutorial](https://www.cvxpy.org/tutorial/index.html)
* [example library](https://www.cvxpy.org/examples/index.html)
* [API reference](https://www.cvxpy.org/api_reference/cvxpy.html)

## Issues
We encourage you to report issues using the [Github tracker](https://github.com/cvxpy/cvxpy/issues). We welcome all kinds of issues, especially those related to correctness, documentation, performance, and feature requests.

For basic usage questions (e.g., "Why isn't my problem DCP?"), please use [StackOverflow](https://stackoverflow.com/questions/tagged/cvxpy) instead.

## Community
The CVXPY community consists of researchers, data scientists, software engineers, and students from all over the world. We welcome you to join us!

* To chat with the CVXPY community in real-time, join us on [Discord](https://discord.gg/4urRQeGBCr).
* To have longer, in-depth discussions with the CVXPY community, use [Github Discussions](https://github.com/cvxpy/cvxpy/discussions).
* To share feature requests and bug reports, use [Github Issues](https://github.com/cvxpy/cvxpy/issues).

Please be respectful in your communications with the CVXPY community, and make sure to abide by our [code of conduct](https://github.com/cvxpy/cvxpy/blob/master/CODE_OF_CONDUCT.md).

## Contributing
We appreciate all contributions. You don't need to be an expert in convex
optimization to help out.

You should first
install [CVXPY from source](https://www.cvxpy.org/install/index.html#install-from-source).
Here are some simple ways to start contributing immediately:
* Read the CVXPY source code and improve the documentation, or address TODOs
* Enhance the [website documentation](https://github.com/cvxpy/cvxpy/tree/master/doc)
* Browse the [issue tracker](https://github.com/cvxpy/cvxpy/issues), and look for issues tagged as "help wanted"
* Polish the [example library](https://github.com/cvxpy/examples)
* Add a [benchmark](https://github.com/cvxpy/benchmarks)

If you'd like to add a new example to our library, or implement a new feature,
please get in touch with us first to make sure that your priorities align with
ours. 

Contributions should be submitted as [pull requests](https://github.com/cvxpy/cvxpy/pulls).
A member of the CVXPY development team will review the pull request and guide
you through the contributing process.

Before starting work on your contribution, please read the [contributing guide](https://github.com/cvxpy/cvxpy/blob/master/CONTRIBUTING.md).

## Team
CVXPY is a community project, built from the contributions of many
researchers and engineers.

CVXPY is developed and maintained by [Steven
Diamond](https://stevendiamond.me/), [Akshay
Agrawal](https://akshayagrawal.com), [Riley Murray](https://rileyjmurray.wordpress.com/), 
[Philipp Schiele](https://www.philippschiele.com/),
[Bartolomeo Stellato](https://stellato.io/),
and [Parth Nobel](https://ptnobel.github.io), with many others contributing
significantly.
A non-exhaustive list of people who have shaped CVXPY over the
years includes Stephen Boyd, Eric Chu, Robin Verschueren,
Jaehyun Park, Enzo Busseti, AJ Friend, Judson Wilson, Chris Dembia, and
William Zhang.

For more information about the team and our processes, see our [governance document](https://github.com/cvxpy/org/blob/main/governance.md).

## Citing
If you use CVXPY for academic work, we encourage you to [cite our papers](https://www.cvxpy.org/resources/citing/index.html). If you use CVXPY in industry, we'd love to hear from you as well, on Discord or over email.

### Core Implementation Code & Architecture
#### File: `cvxpy/cvxcore/__init__.py`
```python

```

#### File: `cvxpy/reductions/cone2cone/__init__.py`
```python

```

#### File: `cvxpy/reductions/dgp2dcp/__init__.py`
```python

```

#### File: `setup/__init__.py`
```python

```

#### File: `cvxpy/utilities/cpp/__init__.py`
```python

```

#### File: `cvxpy/reductions/discrete2mixedint/__init__.py`
```python

```


==================================================
