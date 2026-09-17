# ⚡ [QUANT-SOURCE-074] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_074_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: awesome-quant (`WHEEL_awesome-quant`)
- **Full Name**: `awesome-quant`
- **Description**: A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance)
- **GitHub Stars**: 29619
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Awesome Quant

A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance).

[![](https://awesome.re/badge.svg)](https://awesome.re)

## Contents

- [Numerical Libraries & Data Structures](#numerical-libraries-data-structures)
- [Financial Instruments & Pricing](#financial-instruments-pricing)
- [Technical Indicators](#technical-indicators)
- [Trading & Backtesting](#trading-backtesting)
- [Portfolio Optimization & Risk Analysis](#portfolio-optimization-risk-analysis)
- [Factor Analysis](#factor-analysis)
- [Sentiment Analysis & Alternative Data](#sentiment-analysis-alternative-data)
- [Time Series Analysis](#time-series-analysis)
- [Market Data & Data Sources](#market-data--data-sources)
- [Prediction Markets](#prediction-markets)
- [Calendars & Market Hours](#calendars-market-hours)
- [Visualization](#visualization)
- [Excel & Spreadsheet Integration](#excel-spreadsheet-integration)
- [Quant Research Environments](#quant-research-environments)
- [Cross-Language Frameworks](#cross-language-frameworks)
- [Reproducing Works, Training & Books](#reproducing-works-training-books)
- [Commercial & Proprietary Services](#commercial-proprietary-services)
- [Historical & Archived Projects](#historical-archived-projects)
- [Related Lists](#related-lists)

## Numerical Libraries & Data Structures

- [numpy](https://www.numpy.org) - `Python` - NumPy is the fundamental package for scientific computing with Python. [GitHub](https://github.com/numpy/numpy)
- [scipy](https://www.scipy.org) - `Python` - SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of open-source software for mathematics, science, and engineering. [GitHub](https://github.com/scipy/scipy)
- [pandas](https://pandas.pydata.org) - `Python` - pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. [GitHub](https://github.com/pandas-dev/pandas)
- [polars](https://docs.pola.rs/) - `Python` - Polars is a blazingly fast DataFrame library for manipulating structured data. [GitHub](https://github.com/pola-rs/polars)
- [quantdsl](https://github.com/johnbywater/quantdsl) - `Python` - Domain specific language for quantitative analytics in finance and trading.
- [statistics](https://docs.python.org/3/library/statistics.html) - `Python` - Builtin Python library for all basic statistical calculations.
- [sympy](https://www.sympy.org/) - `Python` - SymPy is a Python library for symbolic mathematics. [GitHub](https://github.com/sympy/sympy)
- [pymc3](https://docs.pymc.io/) - `Python` - Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with Theano. [GitHub](https://github.com/pymc-devs/pymc)
- [modelx](https://docs.modelx.io/) - `Python` - Python reimagination of spreadsheets as formula-centric objects that are interoperable with pandas. [GitHub](https://github.com/fumitoh/modelx)
- [ArcticDB](https://github.com/man-group/ArcticDB) - `Python` - High performance datastore for time series and tick data.
- [CRNG](https://github.com/brotto/crng) - `Python` - Contingency Random Number Generator that produces random numbers with real financial market statistical signatures (fat tails, volatility clustering, kurtosis). Matches 86% of real market metrics vs 14% for NumPy.
- [xts](https://github.com/joshuaulrich/xts) - `R` - eXtensible Time Series: Provide for uniform handling of R's different time-based data classes by extending zoo, maximizing native format information preservation and allowing for user level customization and extension, while simplifying cross-class interoperability.
- [data.table](https://github.com/Rdatatable/data.table) - `R` - Extension of data.frame: Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins, fast add/modify/delete of columns by group using no copies at all, list columns and a fast file reader (fread). Offers a natural and flexible syntax, for faster development.
- [sparseEigen](https://github.com/dppalomar/sparseEigen) - `R` - Sparse principal component analysis.
- [TSdbi](http://tsdbi.r-forge.r-project.org/) - `R` - Provides a common interface to time series databases.
- [tseries](https://cran.r-project.org/web/packages/tseries/index.html) - `R` - Time Series Analysis and Computational Finance.
- [zoo](https://cran.r-project.org/web/packages/zoo/index.html) - `R` - S3 Infrastructure for Regular and Irregular Time Series (Z's Ordered Observations).
- [tis](https://cran.r-project.org/web/packages/tis/index.html) - `R` - Functions and S3 classes for time indexes and time indexed series, which are compatible with FAME frequencies.
- [tfplot](https://cran.r-project.org/web/packages/tfplot/index.html) - `R` - Utilities for simple manipulation and quick plotting of time series data.
- [tframe](https://cran.r-project.org/web/packages/tframe/index.html) - `R` - A kernel of functions for programming time series methods in a way that is relatively independently of the representation of time.
- [Temporal.jl](https://github.com/dysonance/Temporal.jl) - `Julia` - Flexible and efficient time series class & methods.
- [DataFrames.jl](https://github.com/JuliaData/DataFrames.jl) - `Julia` - In-memory tabular data in Julia.
- [TSFrames.jl](https://github.com/xKDR/TSFrames.jl) - `Julia` - Handle timeseries data on top of the powerful and mature DataFrames.jl.
- [TimeArrays.jl](https://github.com/bhftbootcamp/TimeArrays.jl) - `Julia` - Time series handling for Julia.
- [jacobian](https://github.com/morluto/jacobian) - `Python` `MCP` - Exact computation and conjecture testing across polynomial maps, linear algebra, and graph algorithms for agent-driven mathematical research.

## Financial Instruments & Pricing

- [PyQL](https://github.com/enthought/pyql) - `Python` - QuantLib's Python port.
- [pyfin](https://github.com/opendoor-labs/pyfin) - `Python` - Basic options pricing in Python. *ARCHIVED*.
- [vollib](https://github.com/vollib/vollib) - `Python` - vollib is a python library for calculating option prices, implied volatility and greeks.
- [py_vollib](https://github.com/vollib/py_vollib) - `Python` - vollib Python implementation.
- [vanilla-option-pricers](https://github.com/ArturSepp/VanillaOptionPricers) - `Python` - Fast, vectorised Black-Scholes-Merton and Bachelier pricers and implied volatility fitters, including inverse options for crypto derivatives.
- [StochVolModels](https://github.com/ArturSepp/StochVolModels) - `Python` - Pricing analytics and Monte Carlo simulation for stochastic volatility models, including the log-normal SV model and the Heston model.
- [QuantPy](https://github.com/jsmidt/QuantPy) - `Python` - A framework for quantitative finance In python.
- [Finance-Python](https://github.com/alpha-miner/Finance-Python) - `Python` - Python tools for Finance.
- [ffn](https://github.com/pmorissette/ffn) - `Python` - A financial function library for Python.
- [pynance](https://github.com/GriffinAustin/pynance) - `Python` - Lightweight Python library for assembling and analyzing financial data.
- [tia](https://github.com/bpsmith/tia) - `Python` - Toolkit for integration and analysis.
- [pysabr](https://github.com/ynouri/pysabr) - `Python` - SABR model Python implementation.
- [FinancePy](https://github.com/domokane/FinancePy) - `Python` - A Python Finance Library that focuses on the pricing and risk-management of Financial Derivatives, including fixed-income, equity, FX and credit derivatives.
- [gs-quant](https://github.com/goldmansachs/gs-quant) - `Python` - Python toolkit for quantitative finance.
- [willowtree](https://github.com/federicomariamassari/willowtree) - `Python` - Robust and flexible Python implementation of the willow tree lattice for derivatives pricing.
- [financial-engineering](https://github.com/federicomariamassari/financial-engineering) - `Python` - Applications of Monte Carlo methods to financial engineering projects, in Python.
- [optlib](https://github.com/dbrojas/optlib) - `Python` - A library for financial options pricing written in Python.
- [tf-quant-finance](https://github.com/google/tf-quant-finance) - `Python` - High-performance TensorFlow library for quantitative finance.
- [Q-Fin](https://github.com/RomanMichaelPaolucci/Q-Fin) - `Python` - A Python library for mathematical finance.
- [Quantsbin](https://github.com/quantsbin/Quantsbin) - `Python` - Tools for pricing and plotting of vanilla option prices, greeks and various other analysis around them.
- [finoptions](https://github.com/bbcho/finoptions-dev) - `Python` - Complete python implementation of R package fOptions with partial implementation of fExoticOptions for pricing various options.
- [pypme](https://github.com/ymyke/pypme) - `Python` - PME (Public Market Equivalent) calculation.
- [AbsBox](https://github.com/yellowbean/AbsBox) - `Python` - A Python based library to model cashflow for structured product like Asset-backed securities (ABS) and Mortgage-backed securities (MBS).
- [mortgagemath](https://github.com/murraystokely/mortgagemath) - `Python` - Cent-accurate mortgage amortization schedules with Decimal arithmetic and published-source validation across six countries.
- [Intrinsic-Value-Calculator](https://github.com/akashaero/Intrinsic-Value-Calculator) - `Python` - A Python tool for quick calculations of a stock's fair value using Discounted Cash Flow analysis.
- [Kelly-Criterion](https://github.com/deltaray-io/kelly-criterion) - `Python` - Kelly Criterion implemented in Python to size portfolios based on J. L. Kelly Jr's formula.
- [rateslib](https://github.com/attack68/rateslib) - `Python` - A fixed income library for pricing bonds and bond futures, and derivatives such as IRS, cross-currency and FX swaps.
- [fypy](https://github.com/jkirkby3/fypy) - `Python` - Vanilla and exotic option pricing library to support quantitative R&D. Focus on pricing interesting/useful models and contracts (including and beyond Black-Scholes), as well as calibration of financial models to market data.
- [Pyderivatives](https://github.com/Julian-Beatty/Pyderivatives) - `Python` - Toolkit for option pricing, implied volatility surfaces, risk-neutral densities, and pricing kernel surfaces with support for advanced models including Heston, Kou, and Bates.
- [quantra](https://github.com/joseprupi/quantraserver) - `Python` - High-performance pricing engine built on QuantLib. It exposes QuantLib's functionality through gRPC and REST APIs, enabling distributed computations with FlatBuffers serialization.
- [optionlab](https://github.com/rgaveiga/optionlab) - `Python` - A Python library for evaluating option trading strategies.
- [flashalpha](https://github.com/FlashAlpha-lab/flashalpha-python) - `Python` - Python client for the FlashAlpha options analytics API.
- [QuantOracle](https://github.com/QuantOracledev/quantoracle) - `Python` - Free quant finance API with 63 deterministic endpoints + 15 free interactive calculators at [quantoracle.dev](https://quantoracle.dev). Options pricing with full Greeks, Monte Carlo, Kelly, VaR, Sharpe, CAGR, crypto liquidation, impermanent loss, plus live crypto volatility/funding data and 24/7 position monitoring with webhook alerts. 1,000 free calls/day, no API key.
- [BDE Score](https://github.com/hbhqq9/bde-score) - `Python` - Multi-factor quantitative stock analysis MCP server for US, HK, and CN A-share markets. Transparent 0-100 scoring from 40+ indicators. Listed on Official MCP Registry.
- [implied-expectations](https://github.com/Keenan-ux/implied-expectations) - `Python` - Reverse DCF that solves for the revenue growth, duration, and operating margin a stock price implies, from SEC EDGAR fundamentals.
- [RQuantLib](https://github.com/eddelbuettel/rquantlib) - `R` - RQuantLib connects GNU R with QuantLib.
- [quantmod](https://cran.r-project.org/web/packages/quantmod/index.html) - `R` - Quantitative Financial Modelling Framework. [GitHub](https://github.com/joshuaulrich/quantmod)
- [Rmetrics](https://www.rmetrics.org) - `R` - The premier open source software solution for teaching and training quantitative finance.
  - [fAsianOptions](https://cran.r-project.org/web/packages/fAsianOptions/index.html) - EBM and Asian Option Valuation.
  - [fAssets](https://cran.r-project.org/web/packages/fAssets/index.html) - Analysing and Modelling Financial Assets.
  - [fBasics](https://cran.r-project.org/web/packages/fBasics/index.html) - Markets and Basic Statistics.
  - [fBonds](https://cran.r-project.org/web/packages/fBonds/index.html) - Bonds and Interest Rate Models.
  - [fExoticOptions](https://cran.r-project.org/web/packages/fExoticOptions/index.html) - Exotic Option Valuation.
  - [fOptions](https://cran.r-project.org/web/packages/fOptions/index.html) - Pricing and Evaluating Basic Options.
  - [fPortfolio](https://cran.r-project.org/web/packages/fPortfolio/index.html) - Portfolio Selection and Optimization.
- [sde](https://cran.r-project.org/web/packages/sde/index.html) - `R` - Simulation and Inference for Stochastic Differential Equations.
- [YieldCurve](https://cran.r-project.org/web/packages/YieldCurve/index.html) - `R` - Modelling and estimation of the yield curve.
- [SmithWilsonYieldCurve](https://cran.r-project.org/web/packages/SmithWilsonYieldCurve/index.html) - `R` - Constructs a yield curve by the Smith-Wilson method from a table of LIBOR and SWAP rates.
- [ycinterextra](https://cran.r-project.org/web/packages/ycinterextra/index.html) - `R` - Yield curve or zero-coupon prices interpolation and extrapolation.
- [AmericanCallOpt](https://cran.r-project.org/web/packages/AmericanCallOpt/index.html) - `R` - This package includes pricing function for selected American call options with underlying assets that generate payouts.
- [VarSwapPrice](https://cran.r-project.org/web/packages/VarSwapPrice/index.html) - `R` - Pricing a variance swap on an equity index.
- [RND](https://cran.r-project.org/web/packages/RND/index.html) - `R` - Risk Neutral Density Extraction Package.
- [LSMonteCarlo](https://cran.r-project.org/web/packages/LSMonteCarlo/index.html) - `R` - American options pricing with Least Squares Monte Carlo method.
- [OptHedging](https://cran.r-project.org/web/packages/OptHedging/index.html) - `R` - Estimation of value and hedging strategy of call and put options.
- [tvm](https://cran.r-project.org/web/packages/tvm/index.html) - `R` - Time Value of Money Functions.
- [OptionPricing](https://cran.r-project.org/web/packages/OptionPricing/index.html) - `R` - Option Pricing with Efficient Simulation Algorithms.
- [credule](https://github.com/blenezet/credule) - `R` - Credit Default Swap Functions.
- [derivmkts](https://cran.r-project.org/web/packages/derivmkts/index.html) - `R` - Functions and R Code to Accompany Derivatives Markets. [GitHub](https://github.com/rmcd1024/derivmkts)
- [FinCal](https://github.com/felixfan/FinCal) - `R` - Package for time value of money calculation, time series analysis and computational finance.
- [r-quant](https://github.com/artyyouth/r-quant) - `R` - R code for quantitative analysis in finance.
- [options.studies](https://github.com/taylorizing/options.studies) - `R` - options trading studies functions for use with options.data package and shiny.
- [fmbasics](https://github.com/imanuelcostigan/fmbasics) - `R` - Financial Market Building Blocks.
- [R-fixedincome](https://github.com/wilsonfreitas/R-fixedincome) - `R` - Fixed income tools for R.
- [QuantLib.jl](https://github.com/pazzo83/QuantLib.jl) - `Julia` - Quantlib implementation in pure Julia.
- [Ito.jl](https://github.com/aviks/Ito.jl) - `Julia` - A Julia package for quantitative finance.
- [Miletus.jl](https://github.com/JuliaComputing/Miletus.jl) - `Julia` - A financial contract definition, modeling language, and valuation framework.
- [Strata](http://strata.opengamma.io/) - `Java` - Modern open-source analytics and market risk library designed and written in Java. [GitHub](https://github.com/OpenGamma/Strata)
- [JQuantLib](https://github.com/frgomes/jquantlib) - `Java` - JQuantLib is a free, open-source, comprehensive framework for quantitative finance, written in 100% Java.
- [finmath.net](http://finmath.net) - `Java` - Java library with algorithms and methodologies related to mathematical finance. [GitHub](https://github.com/finmath/finmath-lib)
- [quantcomponents](https://github.com/lsgro/quantcomponents) - `Java` - Free Java components for Quantitative Finance and Algorithmic Trading.
- [DRIP](https://lakshmidrip.github.io/DRIP) - `Java` - Fixed Income, Asset Allocation, Transaction Cost Analysis, XVA Metrics Libraries.
- [finance.js](https://github.com/ebradyjobory/finance.js) - `JavaScript` - A JavaScript library for common financial calculations.
- [hagan-sabr](https://github.com/moshejs/hagan-sabr) - `TypeScript` - SABR stochastic-volatility model (Hagan 2002 lognormal/normal expansions, Obłój correction, smile calibration); zero dependencies, matches QuantLib's sabrVolatility to 1e-9.
- [svi-vol-surface](https://github.com/moshejs/svi-vol-surface) - `TypeScript` - Gatheral SVI volatility surface (raw/natural/jump-wings), butterfly and calendar arbitrage checks, slice calibration; zero dependencies.
- [compounded-sofr](https://github.com/moshejs/compounded-sofr) - `TypeScript` - SOFR compounding-in-arrears per ARRC/ISDA conventions (lookback, observation shift, lockout) and the SOFR Index method; reproduces the NY Fed's published averages.
- [day-count-conventions](https://github.com/moshejs/day-count) - `TypeScript` - ISDA 2006 day-count conventions (30/360 family, ACT/360, ACT/365F, ACT/ACT ISDA and ICMA); zero dependencies.
- [tips-index-ratio](https://github.com/moshejs/tips-index-ratio) - `TypeScript` - US TIPS inflation math per 31 CFR 356 Appendix B (reference-CPI interpolation, index ratios); reproduces TreasuryDirect's published values.
- [32nds](https://github.com/moshejs/32nds) - `TypeScript` - US Treasury price quote math: parse and format 32nds quotes (105-16+), ticks, and basis points; zero dependencies.
- [quantfin](https://github.com/boundedvariation/quantfin) - `Haskell` - quant finance in pure haskell.
- [Haxcel](https://github.com/MarcusRainbow/Haxcel) - `Haskell` - Excel Addin for Haskell.
- [Ffinar](https://github.com/MarcusRainbow/Ffinar) - `Haskell` - A financial maths library in Haskell.
- [QuantScale](https://github.com/choucrifahed/quantscale) - `Scala` - Scala Quantitative Finance Library.
- [Scala Quant](https://github.com/frankcash/Scala-Quant) - `Scala` - Scala library for working with stock data from IFTTT recipes or Google Finance.
- [QuantMath](https://github.com/MarcusRainbow/QuantMath) - `Rust` - Financial maths library for risk-neutral pricing and risk.
- [RustQuant](https://github.com/avhz/RustQuant) - `Rust` - Quantitative finance library written in Rust.
- [QoX](https://github.com/bboutelje/qox-python-samples) - `Python` - Finite difference pricing library written in Rust.

## Technical Indicators

- [pandas_talib](https://github.com/femtotrader/pandas_talib) - `Python` - A Python Pandas implementation of technical analysis indicators.
- [finta](https://github.com/peerchemist/finta) - `Python` - Common financial technical analysis indicators implemented in Pandas.
- [Tulipy](https://github.com/cirla/tulipy) - `Python` - Financial Technical Analysis Indicator Library (Python bindings for [tulipindicators](https://github.com/TulipCharts/tulipindicators)).
- [lppls](https://github.com/Boulder-Investment-Technologies/lppls) - `Python` - A Python module for fitting the [Log-Periodic Power Law Singularity (LPPLS)](https://en.wikipedia.org/wiki/Didier_Sornette#The_JLS_and_LPPLS_models) model.
- [talipp](https://github.com/nardew/talipp) - `Python` - Incremental technical analysis library for Python.
- [streaming_indicators](https://github.com/mr-easy/streaming_indicators) - `Python` - A python library for computing technical analysis indicators on streaming data.
- [QuantWave](https://github.com/lavs9/quantwave) - `Python` `Rust` `Polars` - Polars-native technical analysis and backtesting with bit-identical batch and streaming parity, plus an agent skill for consistent research-to-live strategy code.
- [TA-Lib](https://github.com/mrjbq7/ta-lib) - `Python` - Python wrapper for TA-Lib (<http://ta-lib.org/>).
- [ta](https://github.com/bukosabino/ta) - `Python` - Technical Analysis Library using Pandas (Python).
- [bta-lib](https://github.com/mementum/bta-lib) - `Python` - Technical Analysis library in pandas for backtesting algotrading and quantitative analysis.
- [TuneTA](https://github.com/jmrichardson/tuneta) - `Python` - TuneTA optimizes technical indicators using a distance correlation measure to a user defined target feature such as next day return.
- [TTR](https://github.com/joshuaulrich/TTR) - `R` - Technical Trading Rules.
- [TALib.jl](https://github.com/femtotrader/TALib.jl) - `Julia` - A Julia wrapper for TA-Lib.
- [Indicators.jl](https://github.com/dysonance/Indicators.jl) - `Julia` - Financial market technical analysis & indicators on top of Temporal.
- [TechnicalIndicatorCharts.jl](https://github.com/g-gundam/TechnicalIndicatorCharts.jl) - `Julia` - Visualize OnlineTechnicalIndicators.jl using LightweightCharts.jl.
- [MarketTechnicals.jl](https://github.com/JuliaQuant/MarketTechnicals.jl) - `Julia` - Technical analysis of financial time series on top of TimeSeries.
- [OnlineTechnicalIndicators.jl](https://github.com/femtotrader/OnlineTechnicalIndicators.jl) - `Julia` - Julia Technical Analysis Indicators via online algorithms.
- [ta4j](https://github.com/ta4j/ta4j) - `Java` - A Java library for technical analysis.
- [IndicatorTS](https://github.com/cinar/indicatorts) - `JavaScript` - Indicator is a TypeScript module providing various stock technical analysis indicators, strategies, and a backtest framework for trading.
- [orderflow](https://github.com/focus1691/orderflow) - `JavaScript` - Orderflow trade aggregator for building Footprint Candles from exchange websocket data.
- [IndicatorGo](https://github.com/cinar/indicator) - `Golang` - IndicatorGo is a Golang module providing various stock technical analysis indicators, strategies, and a backtest framework for trading.
- [TradeAggregation](https://github.com/MathisWellmann/trade_aggregation-rs) - `Rust` - Aggregate trades into user-defined candles using information driven rules.
- [SlidingFeatures](https://github.com/MathisWellmann/sliding_features-rs) - `Rust` - Chainable tree-like sliding windows for signal processing and technical analysis.
- [fin-primitives](https://github.com/Mattbusel/fin-primitives) - `Rust` - Financial market primitives in Rust: Price/Quantity/Symbol newtypes, BTreeMap order book, OHLCV aggregation, SMA/EMA/RSI indicators, position ledger with PnL, and composable risk monitor.
- [Wickra](https://github.com/wickra-lib/wickra) - `Rust` `Python` `JavaScript` `C++` `C#` `Golang` `Java` `R` - Streaming-first technical-analysis library with a Rust core: 514 indicators updating in O(1) per tick, with bit-exact batch-vs-streaming results.
- [wickworks](https://github.com/psyb0t/docker-wickworks) - `REST` `MCP` - Stateless OHLC analyzer: POST bars and requested indicators, get back RSI/MACD/Bollinger/ADX/ATR/VWAP/Ichimoku plus smart-money-concept primitives (order blocks, FVGs, BOS/CHoCH, swing structure). No database, no AI signals.

## Trading & Backtesting
- [exitkit](https://github.com/charlieyanhx/exitkit) - `Python` - Catalogue of twenty-seven position-exit policies (stop-loss, take-profit, time, volatility, signal-reversal and convergence) behind one interface, with a drop-in adapter for backtesting.py.
- [lesson-book](https://github.com/holdout-labs/lesson-book) - `Python` - Local-first deterministic tuition memory for traders: pattern-matched reminders, no LLM, overridable rule tables.
- [cl-lp-rotation-scanner](https://github.com/donnywin85/cl-lp-rotation-scanner) - `Python` - Estimates fees and impermanent loss for concentrated-liquidity pools whose volatile assets can be hedged, then backtests whether rotating capital among pools outperforms remaining in one pool. It does not execute trades or manage liquidity.
- [orderbook](https://github.com/intrepidkarthi/orderbook) - `Go` `WebAssembly` - Embeddable limit order book and matching engine with integer-exact pricing, a single-writer core and write-ahead-log crash recovery, plus a microstructure research harness whose order-flow-imbalance, Kyle's lambda and CVD studies are measured against simulator ground truth.
- [ERN-WO Options Backtester](https://github.com/Javier-Garzo/ern-wo-options-backtester) - `Java` `Spring Boot` - Streaming backtesting engine for short-duration index options with conservative five-minute execution modeling and reproducible Early Retirement Now and WealthyOption strategy replication results.
- [midas-core](https://github.com/w2ur/midas-core) - `Python` - Multi-agent paper-trading framework where LLM agents author orders and a separate brok
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python
"""Tests for awesome-quant maintenance tooling."""
```

#### File: `pyproject.toml`
```python
[project]
name = "awesome-quant"
version = "0.1.0"
description = ""
authors = [{ name = "Wilson Freitas", email = "wilson.freitas@gmail.com" }]
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "PyGithub>=2.2.0",
    "pandas>=2.2.0",
    "mypy>=1.14.0",
]

[tool.mypy]
explicit_package_bases = true
```

#### File: `topic.py`
```python
import os
from github import Github

# using an access token
g = Github(os.environ['GITHUB_ACCESS_TOKEN'])

# ts = g.search_topics('trading')

# for t in ts:
#     print(t)

# t = ts[0]
# print(t)
# print(t.name)
# print(t.updated_at)
# print(t.score)

topic = 'quant'
repos = g.search_repositories(query=f'topic:{topic}')
for repo in repos:
    if repo.stargazers_count < 1000:
        break
    print(repo.name, repo.stargazers_count, repo.language, repo.html_url,
          repo.description, repo.updated_at, repo.archived)
```

#### File: `tests/test_readme_audit_workflow.py`
```python
import unittest
from pathlib import Path


WORKFLOW_PATH = Path(__file__).parents[1] / ".github/workflows/readme-audit.yml"


class ReadmeAuditWorkflowTests(unittest.TestCase):
    def test_workflow_matches_the_scheduled_audit_contract(self):
        expected = """name: README Audit

on:
    schedule:
        - cron: "0 9 * * 1"
    workflow_dispatch:

permissions:
    contents: read
    issues: write

concurrency:
    group: readme-audit
    cancel-in-progress: false

jobs:
    audit:
        runs-on: ubuntu-latest
        timeout-minutes: 30
        steps:
            - uses: actions/checkout@v4
              with:
                  fetch-depth: 1
                  persist-credentials: false
            - uses: astral-sh/setup-uv@v6
            - uses: actions/setup-python@v5
              with:
                  python-version: "3.11"
            - name: Install dependencies
              run: uv sync --frozen --no-install-project
            - name: Audit README links and repositories
              env:
                  GITHUB_TOKEN: ${{ github.token }}
                  GITHUB_REPOSITORY: ${{ github.repository }}
              run: uv run python scripts/audit_readme.py --readme README.md
"""

        self.assertEqual(WORKFLOW_PATH.read_text(encoding="utf-8"), expected)


if __name__ == "__main__":
    unittest.main()
```

#### File: `tests/test_readme_entries.py`
```python
import tempfile
import unittest
from pathlib import Path

from scripts.readme_entries import iter_readme_entries


class ReadmeEntryUrlTests(unittest.TestCase):
    def test_external_urls_extracts_all_urls_in_source_order_without_duplicates(self):
        readme = (
            "## Trading & Backtesting\n\n"
            "- [Primary](https://example.com/primary) - `Python` - "
            "<https://example.com/autolink> then Suffix "
            "[Docs](https://example.com/suffix) repeated "
            "[Again](https://example.com/suffix).\n"
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            path.write_text(readme, encoding="utf-8")

            entry = next(iter_readme_entries(path))

        self.assertEqual(
            entry.external_urls,
            [
                "https://example.com/primary",
                "https://example.com/autolink",
                "https://example.com/suffix",
            ],
        )

    def test_external_urls_includes_legacy_http_urls(self):
        readme = (
            "## Trading & Backtesting\n\n"
            "- [Legacy](http://example.com/primary) - `Python` - "
            "<http://example.com/autolink> entry.\n"
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            path.write_text(readme, encoding="utf-8")

            entry = next(iter_readme_entries(path))

        self.assertEqual(
            entry.external_urls,
            ["http://example.com/primary", "http://example.com/autolink"],
        )
```

#### File: `tests/test_pr_review_workflow.py`
```python
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "pr-review.yml"
EXPECTED_WORKFLOW = """name: PR Review

on:
    pull_request_target:
        branches: [main]
        types: [opened, synchronize, reopened, edited]

permissions:
    contents: read
    pull-requests: read

concurrency:
    group: ${{ github.workflow }}-${{ github.event.pull_request.number }}
    cancel-in-progress: true

jobs:
    validate:
        runs-on: ubuntu-latest
        timeout-minutes: 10
        steps:
            - uses: actions/checkout@v4
              with:
                  ref: ${{ github.event.pull_request.base.ref }}
                  fetch-depth: 1
                  persist-credentials: false
            - uses: astral-sh/setup-uv@v6
            - uses: actions/setup-python@v5
              with:
                  python-version: "3.11"
            - name: Install dependencies
              run: uv sync --frozen --no-install-project
            - name: Review pull request
              env:
                  GITHUB_TOKEN: ${{ github.token }}
                  GITHUB_REPOSITORY: ${{ github.repository }}
                  PR_NUMBER: ${{ github.event.pull_request.number }}
              run: uv run python scripts/review_pr.py --skip-pull-request-duplicates
"""


class PullRequestReviewWorkflowContractTests(unittest.TestCase):
    def test_matches_the_complete_read_only_security_contract(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertEqual(workflow, EXPECTED_WORKFLOW)


if __name__ == "__main__":
    unittest.main()
```


==================================================


## [2/3] Repository: bat (`WHEEL_bat`)
- **Full Name**: `bat`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
  <img src="doc/logo-header.svg" alt="bat - a cat clone with wings"><br>
  <a href="https://github.com/sharkdp/bat/actions?query=workflow%3ACICD"><img src="https://github.com/sharkdp/bat/workflows/CICD/badge.svg" alt="Build Status"></a>
  <img src="https://img.shields.io/crates/l/bat.svg" alt="license">
  <a href="https://crates.io/crates/bat"><img src="https://img.shields.io/crates/v/bat.svg?colorB=319e8c" alt="Version info"></a><br>
  A <i>cat(1)</i> clone with syntax highlighting and Git integration.
</p>

<p align="center">
  <a href="#syntax-highlighting">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#installation">Installation</a> •
  <a href="#customization">Customization</a> •
  <a href="#project-goals-and-alternatives">Project goals, alternatives</a><br>
  [English]
  [<a href="doc/README-zh.md">中文</a>]
  [<a href="doc/README-ja.md">日本語</a>]
  [<a href="doc/README-ko.md">한국어</a>]
  [<a href="doc/README-ru.md">Русский</a>]
</p>

### Syntax highlighting

`bat` supports syntax highlighting for a large number of programming and markup
languages:

![Syntax highlighting example](https://imgur.com/rGsdnDe.png)

### Git integration

`bat` communicates with `git` to show modifications with respect to the index
(see left sidebar):

![Git integration example](https://i.imgur.com/2lSW4RE.png)

### Show non-printable characters

You can use the `-A`/`--show-all` option to show and highlight non-printable
characters:

![Non-printable character example](https://i.imgur.com/WndGp9H.png)

### Automatic paging

By default, `bat` pipes its own output to a pager (e.g. `less`) if the output is too large for one screen.
If you would rather `bat` work like `cat` all the time (never page output), you can set `--paging=never` as an option, either on the command line or in your configuration file.
If you intend to alias `cat` to `bat` in your shell configuration, you can use `alias cat='bat --paging=never'` to preserve the default behavior.

#### File concatenation

Even with a pager set, you can still use `bat` to concatenate files :wink:.
Whenever `bat` detects a non-interactive terminal (i.e. when you pipe into another process or into a file), `bat` will act as a drop-in replacement for `cat` and fall back to printing the plain file contents, regardless of the `--pager` option's value.

## How to use

Display a single file on the terminal

```bash
bat README.md
```

Display multiple files at once

```bash
bat src/*.rs
```

Read from stdin, determine the syntax automatically (note, highlighting will
only work if the syntax can be determined from the first line of the file,
usually through a shebang such as `#!/bin/sh`)

```bash
curl -s https://sh.rustup.rs | bat
```

Read from stdin, specify the language explicitly

```bash
yaml2json .travis.yml | json_pp | bat -l json
```

Show and highlight non-printable characters:
```bash
bat -A /etc/hosts
```

Use it as a `cat` replacement:

```bash
bat > note.md  # quickly create a new file

bat header.md content.md footer.md > document.md

bat -n main.rs  # show line numbers (only)

bat f - g  # output 'f', then stdin, then 'g'.
```

### Integration with other tools

#### `fzf`

You can use `bat` as a previewer for [`fzf`](https://github.com/junegunn/fzf). To do this,
use `bat`'s `--color=always` option to force colorized output. You can also use `--line-range`
option to restrict the load times for long files:

```bash
fzf --preview "bat --color=always --style=numbers --line-range=:500 {}"
```

For more information, see [`fzf`'s `README`](https://github.com/junegunn/fzf#preview-window).

#### `find` or `fd`

You can use the `-exec` option of `find` to preview all search results with `bat`:

```bash
find … -exec bat {} +
```

If you happen to use [`fd`](https://github.com/sharkdp/fd), you can use the `-X`/`--exec-batch` option to do the same:

```bash
fd … -X bat
```

#### `ripgrep`

With [`batgrep`](https://github.com/eth-p/bat-extras/blob/master/doc/batgrep.md), `bat` can be used as the printer for [`ripgrep`](https://github.com/BurntSushi/ripgrep) search results.

```bash
batgrep needle src/
```

#### `tail -f`

`bat` can be combined with `tail -f` to continuously monitor a given file with syntax highlighting.

```bash
tail -f /var/log/pacman.log | bat --paging=never -l log
```

Note that we have to switch off paging in order for this to work. We have also specified the syntax
explicitly (`-l log`), as it can not be auto-detected in this case.

#### `git`

You can combine `bat` with `git show` to view an older version of a given file with proper syntax
highlighting:

```bash
git show v0.6.0:src/main.rs | bat -l rs
```

#### `git diff`

You can combine `bat` with `git diff` to view lines around code changes with proper syntax
highlighting:
```bash
batdiff() {
    git diff --name-only --relative --diff-filter=d -z | xargs -0 bat --diff
}
```
If you prefer to use this as a separate tool, check out `batdiff` in [`bat-extras`](https://github.com/eth-p/bat-extras).

If you are looking for more support for git and diff operations, check out [`delta`](https://github.com/dandavison/delta).

#### `xclip`

The line numbers and Git modification markers in the output of `bat` can make it hard to copy
the contents of a file. To prevent this, you can call `bat` with the `-p`/`--plain` option or
simply pipe the output into `xclip`:
```bash
bat main.cpp | xclip
```
`bat` will detect that the output is being redirected and print the plain file contents.

#### `man`

`bat` can be used as a colorizing pager for `man`, by setting the
`MANPAGER` environment variable:

```bash
export MANPAGER="bat -plman"
man 2 select
```
(on some older Debian or Ubuntu releases, the executable is named `batcat` instead of `bat`)

If you prefer to have this bundled in a new command, you can also use [`batman`](https://github.com/eth-p/bat-extras/blob/master/doc/batman.md).

Note that the [Manpage syntax](assets/syntaxes/02_Extra/Manpage.sublime-syntax) is developed in this repository and still needs some work.

#### `prettier` / `shfmt` / `rustfmt`

The [`prettybat`](https://github.com/eth-p/bat-extras/blob/master/doc/prettybat.md) script is a wrapper that will format code and print it with `bat`.

#### Highlighting `--help` messages

You can use `bat` to colorize help text: `$ cp --help | bat -plhelp`

You can also use a wrapper around this:

```bash
# in your .bashrc/.zshrc/*rc
alias bathelp='bat --plain --language=help'
help() {
    "$@" --help 2>&1 | bathelp
}
```

Then you can do `$ help cp` or `$ help git commit`.

When you are using `zsh`, you can also use global aliases to override `-h` and `--help` entirely:

```bash
alias -g -- -h='-h 2>&1 | bat --language=help --style=plain'
alias -g -- --help='--help 2>&1 | bat --language=help --style=plain'
```

For `fish`, you can use abbreviations:

```fish
abbr -a --position anywhere -- --help '--help | bat -plhelp'
abbr -a --position anywhere -- -h '-h | bat -plhelp'
```

This way, you can keep on using `cp --help`, but get colorized help pages.

> [!TIP]
> To remove these abbreviations later, run:
> ```fish
> abbr -e -- --help
> abbr -e -- -h
> ```
> The `--` before the abbreviation name is required because `--help` and `-h` start with dashes, which would otherwise be interpreted as flags to `abbr` itself.

Be aware that in some cases, `-h` may not be a shorthand of `--help` (for example with `ls`). In cases where you need to use `-h` 
as a command argument you can prepend `\` to the argument (eg. `ls \-h`) to escape the aliasing defined above. 

Please report any issues with the help syntax in [this repository](https://github.com/victor-gp/cmd-help-sublime-syntax).


## Installation

<!--

Installation instructions need to:
* be for widely used systems
* be non-obvious
* be from somewhat official sources

-->

[![Packaging status](https://repology.org/badge/vertical-allrepos/bat-cat.svg?columns=3&exclude_unsupported=1)](https://repology.org/project/bat-cat/versions)

### On Ubuntu (using `apt`)
*... and other Debian-based Linux distributions.*

`bat` is available on [Ubuntu since 20.04 ("Focal")](https://packages.ubuntu.com/search?keywords=bat&exact=1) and [Debian since August 2021 (Debian 11 - "Bullseye")](https://packages.debian.org/bullseye/bat).

If your Ubuntu/Debian installation is new enough you can simply run:

```bash
sudo apt install bat
```

**Important**: On some older Ubuntu/Debian releases, the executable is installed as `batcat` instead of `bat` (due to [a name
clash with another package](https://github.com/sharkdp/bat/issues/982)). On newer releases, the executable is available as `bat`. If `bat --version` does not work after installation, try `batcat --version` instead. You can set up a `bat -> batcat` symlink or alias to prevent any issues that may come up because of this and to be consistent with other distributions:
``` bash
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat
```

an example alias for `batcat` as `bat`:
```bash
alias bat="batcat"
```

### On Ubuntu (using most recent `.deb` packages)
*... and other Debian-based Linux distributions.*

If the package has not yet been promoted to your Ubuntu/Debian installation, or you want
the most recent release of `bat`, download the latest `.deb` package from the
[release page](https://github.com/sharkdp/bat/releases) and install it via:

```bash
sudo dpkg -i bat_0.18.3_amd64.deb  # adapt version number and architecture
```

### On Alpine Linux

You can install [the `bat` package](https://pkgs.alpinelinux.org/packages?name=bat)
from the official sources, provided you have the appropriate repository enabled:

```bash
apk add bat
```

### On Arch Linux

You can install [the `bat` package](https://www.archlinux.org/packages/extra/x86_64/bat/)
from the official sources:

```bash
pacman -S bat
```

### On Fedora

You can install [the `bat` package](https://packages.fedoraproject.org/pkgs/rust-bat/bat/) from the official sources:

```bash
dnf install bat
```

### On Gentoo Linux

You can install [the `bat` package](https://packages.gentoo.org/packages/sys-apps/bat)
from the official sources:

```bash
emerge sys-apps/bat
```

### On FreeBSD

You can install a precompiled [`bat` package](https://www.freshports.org/textproc/bat) with pkg:

```bash
pkg install bat
```

or build it on your own from the FreeBSD ports:

```bash
cd /usr/ports/textproc/bat
make install
```

### On OpenBSD

You can install `bat` package using [`pkg_add(1)`](https://man.openbsd.org/pkg_add.1):

```bash
pkg_add bat
```

### Via nix

You can install `bat` using the [nix package manager](https://nixos.org/nix):

```bash
nix-env -i bat
```

### On openSUSE

You can install `bat` with zypper:

```bash
zypper install bat
```

### Via snap package

There is currently no recommended snap package available.
Existing packages may be available, but are not officially supported and may contain [issues](https://github.com/sharkdp/bat/issues/1519).

### On macOS (or Linux) via Homebrew

You can install `bat` with [Homebrew](https://formulae.brew.sh/formula/bat):

```bash
brew install bat
```

### On macOS via MacPorts

Or install `bat` with [MacPorts](https://ports.macports.org/port/bat/summary):

```bash
port install bat
```

### On Windows

There are a few options to install `bat` on Windows. Once you have installed `bat`,
take a look at the ["Using `bat` on Windows"](#using-bat-on-windows) section.

#### Prerequisites

You will need to install the [Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist#latest-microsoft-visual-c-redistributable-version)

#### With WinGet

You can install `bat` via [WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget):

```bash
winget install sharkdp.bat
```

#### With Chocolatey

You can install `bat` via [Chocolatey](https://chocolatey.org/packages/Bat):
```bash
choco install bat
```

#### With Scoop

You can install `bat` via [scoop](https://scoop.sh/):
```bash
scoop install bat
```

#### From prebuilt binaries:

You can download prebuilt binaries from the [Release page](https://github.com/sharkdp/bat/releases),

You will need to install the [Visual C++ Redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) package.

### From binaries

Check out the [Release page](https://github.com/sharkdp/bat/releases) for
prebuilt versions of `bat` for many different architectures. Statically-linked
binaries are also available: look for archives with `musl` in the file name.

### From source

If you want to build `bat` from source, you need Rust 1.79.0 or
higher. You can then use `cargo` to build everything:

#### From local source
```bash
cargo install --path . --locked
```
> [!NOTE]
> The `--path .` above specifies the directory of the source code and NOT where `bat` will be installed.
> For more information see the docs for [`cargo install`](https://doc.rust-lang.org/cargo/commands/cargo-install.html).

#### From `crates.io`
```bash
cargo install --locked bat
```

Note that additional files like the man page or shell completion
files can not be installed automatically in both these ways.
If installing from a local source, they will be generated by `cargo`
and should be available in the cargo target folder under `build`.

Furthermore, shell completions are also available by running:
```bash
bat --completion <shell>
# see --help for supported shells
```

## Customization

### Highlighting theme

Use `bat --list-themes` to get a list of all available themes for syntax
highlighting. By default, `bat` uses `Monokai Extended` or `Monokai Extended Light`
for dark and light themes respectively. To select the `TwoDark` theme, call `bat`
with the `--theme=TwoDark` option or set the `BAT_THEME` environment variable to
`TwoDark`. Use `export BAT_THEME="TwoDark"` in your shell's startup file to
make the change permanent. Alternatively, use `bat`'s
[configuration file](#configuration-file).

If you want to preview the different themes on a custom file, you can use
the following command (you need [`fzf`](https://github.com/junegunn/fzf) for this):
```bash
bat --list-themes | fzf --preview="bat --theme={} --color=always /path/to/file"
```

`bat` automatically picks a fitting theme depending on your terminal's background color.
You can use the `--theme-dark` / `--theme-light` options or the `BAT_THEME_DARK` / `BAT_THEME_LIGHT` environment variables
to customize the themes used. This is especially useful if you frequently switch between dark and light mode.

You can also use a custom theme by following the
['Adding new themes' section below](#adding-new-themes).

### 8-bit themes

`bat` has three themes that always use [8-bit colors](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors),
even when truecolor support is available:

- `ansi` looks decent on any terminal. It uses 3-bit colors: black, red, green,
  yellow, blue, magenta, cyan, and white.
- `base16` is designed for [base16](https://github.com/tinted-theming/home) terminal themes. It uses
  4-bit colors (3-bit colors plus bright variants) in accordance with the
  [base16 styling guidelines](https://github.com/tinted-theming/home/blob/main/styling.md).
- `base16-256` is designed for [tinted-shell](https://github.com/tinted-theming/tinted-shell).
  It replaces certain bright colors with 8-bit colors from 16 to 21. **Do not** use this simply
  because you have a 256-color terminal but are not using tinted-shell.

Although these themes are more restricted, they have three advantages over truecolor themes. They:

- Enjoy maximum compatibility. Some terminal utilities do not support more than 3-bit colors.
- Adapt to terminal theme changes. Even for already printed output.
- Visually harmonize better with other terminal software.

### Output style

You can use the `--style` option to control the appearance of `bat`'s output.
You can use `--style=numbers,changes`, for example, to show only Git changes
and line numbers but no grid and no file header. Set the `BAT_STYLE` environment
variable to make these changes permanent or use `bat`'s
[configuration file](#configuration-file).

By default, `bat` enables `changes`, `grid`, `header-filename`, `numbers`, and `snip`.

The available pre-defined styles are:

| Style | Description |
|-------|-------------|
| `default` | Enables the recommended style components listed above. |
| `full` | Enables all available components. |
| `auto` | Same as `default`, unless the output is piped. |
| `plain` | Disables all available components. |

The available individual components are:

| Component | Description |
|-----------|-------------|
| `changes` | Show Git modification markers. |
| `header` | Alias for `header-filename`. |
| `header-filename` | Show filenames before the content. |
| `header-filesize` | Show file sizes before the content. |
| `grid` | Vertical/horizontal lines to separate the side bar and header from the content. |
| `rule` | Horizontal lines to delimit files. |
| `numbers` | Show line numbers in the side bar. |
| `snip` | Draw separation lines between distinct line ranges. |

>[!tip]
> If you specify a default style in `bat`'s config file, you can change which components
> are displayed during a single run of `bat` using the `--style` command-line argument.
> By prefixing a component with `+` or `-`, it can be added or removed from the current style.
>
> For example, if your config contains `--style=full,-snip`, you can run bat with
> `--style=-grid,+snip` to remove the grid and add back the `snip` component.
> Or, if you want to override the styles completely, you use `--style=numbers` to
> only show the line numbers.

### Decorations

By default, `bat` only shows decorations (such as line numbers, file headers, grid borders, etc.) when outputting to an interactive terminal. You can control this behavior with the `--decorations` option. Use `--decorations=always` to show decorations even when piping output to another command, or `--decorations=never` to disable them entirely. Possible values are `auto` (default), `never`, and `always`.

There is also the `--force-colorization` option, which is an alias for `--decorations=always --color=always`. This is useful if you want to keep colorization and decorations when piping `bat`'s output to another program.

### Adding new syntaxes / language definitions

Should you find that a particular syntax is not available within `bat`, you can follow these
instructions to easily add new syntaxes to your current `bat` installation.

`bat` uses the excellent [`syntect`](https://github.com/trishume/syntect/)
library for syntax highlighting. `syntect` can read any
[Sublime Text `.sublime-syntax` file](https://www.sublimetext.com/docs/3/syntax.html)
and theme.

A good resource for finding Sublime Syntax packages is [Package Control](https://packagecontrol.io/). Once you found a
syntax:

1. Create a folder with syntax definition files:

   ```bash
   mkdir -p "$(bat --config-dir)/syntaxes"
   cd "$(bat --config-dir)/syntaxes"

   # Put new '.sublime-syntax' language definition files
   # in this folder (or its subdirectories), for example:
   git clone https://github.com/tellnobody1/sublime-purescript-syntax
   ```

2. Now use the following command to parse these files into a binary cache:

   ```bash
   bat cache --build
   ```

3. Finally, use `bat --list-languages` to check if the new languages are available.

   If you ever want to go back to the default settings, call:

   ```bash
   bat cache --clear
   ```

4. If you think that a specific syntax should be included in `bat` by default, please
   consider opening a "syntax request" ticket after reading the policies and
   instructions [here](doc/assets.md): [Open Syntax Request](https://github.com/sharkdp/bat/issues/new?labels=syntax-request&template=syntax_request.md).

### Adding new themes

This works very similar to how we add new syntax definitions.
> [!NOTE]
> Custom themes must be stored in [`.tmTheme` files](https://www.sublimetext.com/docs/color_schemes_tmtheme.html).
> Newer `.sublime-color-scheme` files are currently not supported.

First, create a folder with the new syntax highlighting themes:
```bash
mkdir -p "$(bat --config-dir)/themes"
cd "$(bat --config-dir)/themes"

# Download a theme in '.tmTheme' format, for example:
git clone https://github.com/greggb/sublime-snazzy

# Update the binary cache
bat cache --build
```

Finally, use `bat --list-themes` to check if the new themes are available.
> [!NOTE]
> `bat` uses the name of the `.tmTheme` file for the theme's name. 

### Adding or changing file type associations

You can add new (or change existing) file name patterns using the `--map-syntax`
command line option. The option takes an argument of the form `pattern:syntax` where
`pattern` is a glob pattern that is matched against the file name and
the absolute file path. The `syntax` part is the full name of a supported language
(use `bat --list-languages` for an overview).

**Note:** You probably want to use this option as [an entry in `bat`'s configuration file](#configuration-file)
for persistence instead of passing it on the command line as a one-off. Generally
you'd just use `-l` if you want to manually specify a language for a file.

Example: To use "INI" syntax highlighting for all files with a `.conf` file extension, use
```bash
--map-syntax='*.conf:INI'
```

Example: To open all files called `.ignore` (exact match) with the "Git Ignore" syntax, use:
```bash
--map-syntax='.ignore:Git Ignore'
```

Example: To open all `.conf` files in subfolders of `/etc/apache2` with the "Apache Conf"
syntax, use (this mapping is already built in):
```bash
--map-syntax='/etc/apache2/**/*.conf:Apache Conf'
```

### Using a different pager

`bat` uses the pager that is specified in the `PAGER` environment variable. If this variable is not
set, `less` is used by default. You can also use bat's built-in pager with `--pager=builtin` or
by setting the `BAT_PAGER` environment variable to "builtin".

If you want to use a different pager, you can either modify the `PAGER` variable or set the
`BAT_PAGER` environment variable to override what is specified in `PAGER`.

>[!NOTE]
> If `PAGER` is `more` or `most`, `bat` will silently use `less` instead to ensure support for colors.

If you want to pass command-line arguments to the pager, you can also set them via the
`PAGER`/`BAT_PAGER` variables:

```bash
export BAT_PAGER="less -RFK"
```

Instead of using environment variables, you can also use `bat`'s [configuration file](#configuration-file) to configure the pager (`--pager` option).


### Using `less` as a pager

When using `less` as a pager, `bat` will automatically pass extra options along to `less`
to improve the experience. Specifically, `-R`/`--RAW-CONTROL-CHARS`, `-F`/`--quit-if-one-screen`,
`-K`/`--quit-on-intr` and under certain conditions, `-X`/`--no-init` and/or `-S`/`--chop-long-lines`.

>[!IMPORTANT]
> These options will not be added if:
> - The pager is not named `less`.
> - The `--pager` argument contains any command-line arguments (e.g. `--pager="less -R"`).
> - The `BAT_PAGER` environment variable contains any command-line arguments (e.g. `export BAT_PAGER="less -R"`)
>
> The `--quit-if-one-screen` option will not be added when:
> - The `--paging=always` argument is used.
> - The `BAT_PAGING` environment is set to `always`.

The `-R`/`--RAW-CONTROL-CHARS` option is needed to interpret ANSI colors correctly.

The `-F`/`--quit-if-one-screen` option instructs `less` to exit immediately if the output size is smaller than
the vertical size of the terminal. This is convenient for small files because you do not
have to press `q` to quit the pager.

The `-K`/`--quit-on-intr` option instructs `less` to exit immediately when an interrupt signal is received.
This is useful to ensure that `less` quits together with `bat` on SIGINT.

The `-X`/`--no-init` option is added to versions of `less` older than version 530 (older than 558 on Windows) to
fix a bug with the `-F`/`--quit-if-one-screen` feature. Unfortunately, it also breaks mouse-wheel support in `less`.
If you want to enable mouse-wheel scrolling on older versions of `less` and do not mind losing
the quit-if-one-screen feature, you can set the pager (via `--pager` or `BAT_PAGER`) to `less -R`.
For `less` 530 or newer, it should work out of the box.

The `-S`/`--chop-long-lines` option is added when `bat`'s `-S`/`--chop-long-lines` option is used. This tells `less`
to truncate any lines larger than the terminal width.

### Indentation

`bat` expands tabs to 4 spaces by itself, not relying on the pager. To change this, simply add the
`--tabs` argument with the number of spaces you want to be displayed.

**Note**: Defining tab stops for the pager (via the `--pager` argument by `bat`, or via the `LESS`
environment variable for `less`) won't be taken into account because the pager will already get
expanded spaces instead of tabs
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `rustfmt.toml`
```python
# Defaults are used
```

#### File: `src/syntax_mapping/builtins/common/50-f-sharp.toml`
```python
[mappings]
"F#" = ["*.fs"]
```

#### File: `src/syntax_mapping/builtins/common/50-mill.toml`
```python
[mappings]
"Scala" = ["*.mill"]
```

#### File: `src/syntax_mapping/builtins/common/50-markdown.toml`
```python
[mappings]
"Markdown" = ["*.mkd"]
```

#### File: `src/syntax_mapping/builtins/common/50-nix.toml`
```python
[mappings]
"JSON" = ["flake.lock"]
```

#### File: `src/syntax_mapping/builtins/unix-family/50-fish-shell.toml`
```python
[mappings]
"YAML" = ["fish_history"]
```


==================================================


## [3/3] Repository: bulls-vs-bears (`WHEEL_bulls-vs-bears`)
- **Full Name**: `bulls-vs-bears`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# bulls-vs-bears
AI-powered trading strategy generator for Indian stocks (NSE). Analyzes your risk profile &amp; automatically creates optimized algo strategies. Real backtesting on historical data with performance metrics. React + Python FastAPI + AI API. Academic project - paper trading only.

### Core Implementation Code & Architecture
#### File: `metadata.json`
```python
{
  "name": "Bulls vs Bears: India Trading Quest",
  "description": "A gamified Indian stock market trading application featuring real-time NSE/BSE data simulation, AI-driven strategy generation, and backtesting capabilities.",
  "requestFramePermissions": [
    "geolocation"
  ]
}
```

#### File: `package.json`
```python
{
  "name": "bulls-vs-bears:-india-trading-quest",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^19.2.3",
    "recharts": "^3.6.0",
    "react-dom": "^19.2.3",
    "@google/genai": "^1.35.0"
  },
  "devDependencies": {
    "@types/node": "^22.14.0",
    "@vitejs/plugin-react": "^5.0.0",
    "typescript": "~5.8.2",
    "vite": "^6.2.0"
  }
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2022",
    "experimentalDecorators": true,
    "useDefineForClassFields": false,
    "module": "ESNext",
    "lib": [
      "ES2022",
      "DOM",
      "DOM.Iterable"
    ],
    "skipLibCheck": true,
    "types": [
      "node"
    ],
    "moduleResolution": "bundler",
    "isolatedModules": true,
    "moduleDetection": "force",
    "allowJs": true,
    "jsx": "react-jsx",
    "paths": {
      "@/*": [
        "./*"
      ]
    },
    "allowImportingTsExtensions": true,
    "noEmit": true
  }
}
```


==================================================
