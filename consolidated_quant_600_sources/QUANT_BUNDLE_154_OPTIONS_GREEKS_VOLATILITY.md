# ⚡ [QUANT-SOURCE-154] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_154_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: awesome-institutional-trading (`PHASE4-QUANT-049`)
- **Full Name**: `PHASE4-QUANT-049_LabinatorSolutions__awesome-institutional-trading`
- **Description**: The ultimate collection of institutional trading resources: order flow, market microstructure, options GEX, and algorithmic frameworks.
- **GitHub Stars**: 33
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Awesome Institutional Trading Resources

> A curated collection of **institutional-grade** resources for serious futures, forex, and crypto traders.  
> Focused on **Order Flow**, **Volume Profile**, **Market Profile**, and the mechanics of how institutions actually move markets.

**Brought to you by [AlgoStorm](https://algostorm.com) — Master institutional order flow, volume profile, and systematic price action strategies.**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Maintained Status: Yes](https://img.shields.io/badge/Maintained-Yes-004d00?labelColor=1a1a1a)
[![Pull Requests Welcome](https://img.shields.io/badge/PRs-Welcome-003366?labelColor=1a1a1a)](CONTRIBUTING.md)
[![Zero Affiliate Links Guarantee](https://img.shields.io/badge/Affiliate_Links-Zero-004d00?labelColor=1a1a1a)](#philosophy)
[![License: Creative Commons BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-003366?labelColor=1a1a1a)](LICENSE)

---

## Philosophy

Most retail trading education teaches you to read *price*. Institutions trade *volume*. This list is built around one foundational truth:

> **Volume is the cause. Price is the effect.**

Everything curated here — books, tools, platforms, communities — is selected to help you understand *why* markets move, not just *where* they have been. If a resource relies primarily on lagging indicators, subjective chart patterns, or signal-based thinking, it does not belong here.

**Zero Affiliate Links Policy:** The trading industry is plagued by lists created solely to harvest affiliate commissions. This repository contains exactly **zero** affiliate links. Every resource listed here earned its spot purely based on institutional merit.

**Foundational Context:** Read our guide on [Why Trade Futures?](https://algostorm.com/why-trade-futures/) to understand the institutional advantages of centralized exchanges, tick data, and market microstructure before diving into the resources below.

This is a resource for traders who are serious about building a durable, data-driven edge.

---

## Table of Contents

- [Foundational Books](#foundational-books)
- [Options, Volatility & GEX](#options-volatility--gex)
- [Market Profile & Volume Profile](#market-profile--volume-profile)
- [Order Flow & Footprint Charts](#order-flow--footprint-charts)
- [Market Microstructure & Academic Reading](#market-microstructure--academic-reading)
- [Free Tools & Calculators](#free-tools--calculators)
- [Systematic & Algorithmic Trading](#systematic--algorithmic-trading)
- [Institutional Tech & Data Stack](#institutional-tech--data-stack)
- [Macro & Fixed Income Mechanics](#macro--fixed-income-mechanics)
- [Platforms & Charting Software](#platforms--charting-software)
- [Free Data Sources](#free-data-sources)
- [Podcasts & YouTube Channels](#podcasts--youtube-channels)
- [Glossary of Key Concepts](#glossary-of-key-concepts)
- [Contributing](#contributing)

---

## Foundational Books

Books that form the intellectual backbone of institutional trading. Read in the order listed for the best progression.

### Trading Psychology & Mindset

| Book | Author | Why It Matters |
| --- | --- | --- |
| [Trading in the Zone](https://www.amazon.com/Trading-Zone-Confidence-Discipline-Attitude/dp/0735201447) | Mark Douglas | The definitive text on trading psychology. Understand why discipline, not strategy, is the primary failure point for most traders. |
| [The Disciplined Trader](https://www.amazon.com/Disciplined-Trader-Developing-Winning-Attitudes/dp/0132157578) | Mark Douglas | Douglas's earlier and equally important work on the mental framework required for consistency. |

### Trader Interviews & Market History

| Book | Author | Why It Matters |
| --- | --- | --- |
| [Market Wizards (6 book series)](https://www.amazon.com/dp/B08R3SYBFS) | Jack D. Schwager | The definitive collection of interviews with top institutional traders and hedge fund managers. Essential for understanding risk management and strategy from market legends. |

### Risk Management & Portfolio Mathematics

| Book | Author | Why It Matters |
| --- | --- | --- |
| [Active Portfolio Management](https://www.amazon.com/Active-Portfolio-Management-Quantitative-Controlling/dp/0070248826) | Richard Grinold, Ronald Kahn | The absolute standard for institutional portfolio construction, risk attribution, and the Information Ratio. |
| [The Mathematics of Money Management](https://www.amazon.com/Mathematics-Money-Management-Risk-Analysis/dp/0471547387) | Ralph Vince | Deep mathematical dive into position sizing, optimal f, and drawdown probability. |
| [Antifragile](https://www.amazon.com/Antifragile-Things-That-Gain-Disorder/dp/0812979680) | Nassim Nicholas Taleb | Essential conceptual framework for understanding convex payoffs and surviving market tail risks. |

### Price, Volume & Market Structure

| Book | Author | Why It Matters |
| --- | --- | --- |
| [The Wyckoff Methodology in Depth](https://www.amazon.com/dp/B08W2X3TQY) | Rubén Villahermosa | The clearest modern explanation of Wyckoff's supply/demand and accumulation/distribution framework. |
| [Trades About to Happen](https://www.amazon.com/Trades-About-Happen-Wyckoff-Methodology/dp/0470487801) | David H. Weis | Applies Wyckoff principles to modern markets using real charts. Practical and precise. |
| [Jesse Livermore's Two Books of Market Wisdom](https://www.amazon.com/dp/B09648V5Z9) | Richard Demille Wyckoff, Jesse Lauriston Livermore, Edwin Lefevre | Two classic works attributed to Jesse Livermore. Provides foundational insights into market speculation and the realities of trading. |

### Market Profile & Auction Theory

| Book | Author | Why It Matters |
| --- | --- | --- |
| [Mind Over Markets](https://www.amazon.com/Mind-Over-Markets-Generated-Information-ebook/dp/B00DOSTEVG) | James F. Dalton, Eric T. Jones, Robert B. Dalton | The foundational text on Market Profile and auction market theory. Non-negotiable reading for order flow traders. |
| [Markets in Profile](https://www.amazon.com/Markets-Profile-Profiting-Auction-Process/dp/0470039094) | James F. Dalton | The follow-up to *Mind Over Markets*. Extends the framework to modern electronic markets. |
| [Steidlmayer on Markets](https://www.amazon.com/Steidlmayer-Markets-Trading-Market-Profile/dp/0471215562) | J. Peter Steidlmayer | The creator's own book developing the Market Profile concept. Dense but authoritative. |

### Algorithmic & Quantitative Context

| Book | Author | Why It Matters |
| --- | --- | --- |
| [Trading and Exchanges: Market Microstructure for Practitioners](https://www.amazon.com/Trading-Exchanges-Market-Microstructure-Practitioners/dp/0195144708) | Larry Harris | The most thorough academic treatment of how exchanges, order books, and market makers actually operate. Essential for understanding who you are trading against. |
| [Advances in Financial Machine Learning](https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089) | Marcos López de Prado | The absolute bible for modern institutional quantitative trading and machine learning applications in finance. |
| [Inside the Black Box](https://www.amazon.com/Inside-Black-Box-Quantitative-High-Frequency/dp/1118362411) | Rishi K. Narang | Demystifies algorithmic and quant trading. Helps retail traders understand the machine-driven liquidity landscape. |

### Options, Volatility & Dealer Positioning

| Book | Author | Why It Matters |
| --- | --- | --- |
| [Option Volatility and Pricing](https://www.amazon.com/Option-Volatility-Pricing-Strategies-Techniques/dp/0071818774) | Sheldon Natenberg | The absolute industry standard for options theory. Required reading on every institutional derivatives desk. |
| [Trading Volatility](https://www.amazon.com/Trading-Volatility-Correlation-Term-Structure/dp/1461108756) | Colin Bennett | Written by a former desk head at UBS and Santander. Deep dive into how banks trade variance swaps, volatility, and manage Greeks. |
| [Positional Option Trading](https://www.amazon.com/Positional-Option-Trading-Wiley/dp/1119583519) | Euan Sinclair | Focuses on trading volatility as a quantitative edge rather than directional gambling. |

---

## Options, Volatility & GEX

Options market makers (dealers) continuously hedge their exposure (Gamma, Delta, Vanna, Charm), which profoundly impacts the underlying futures market. Understanding Gamma Exposure (GEX) is essential for predicting market pinning, volatility expansion, and directional magnetism.

### Primary Documents & Whitepapers

- 📄 **[The Implied Order Book (Squeezemetrics)](https://squeezemetrics.com/monitor/download/pdf/short_is_long.pdf)** — A foundational whitepaper explaining how dealer gamma hedging acts as an implied order book, directly affecting S&P 500 liquidity and realized volatility.
- 📄 **[CBOE Whitepapers](https://www.cboe.com/insights/)** — Official research from the Chicago Board Options Exchange on volatility (VIX), options volume, and market impact.

### Core Options & GEX Concepts

| Concept | Description |
| --- | --- |
| **Gamma Exposure (GEX)** | The net gamma position of options market makers. High positive GEX suppresses volatility (dealers trade against the trend). High negative GEX expands volatility (dealers trade with the trend). |
| **Vanna** | The change in option Delta for a 1-point change in Implied Volatility. Drives significant hedging flows during market sell-offs as IV spikes. |
| **Charm (Delta Bleed)** | The change in option Delta as time passes (decay). Causes predictable dealer flows into the close, especially on OPEX (options expiration) days. |
| **0DTE Impact** | Zero-days-to-expiration options. Their massive volume has shifted intraday S&P 500 mechanics, creating localized gamma squeezes and intraday reversals. |
| **Pinning** | The tendency of the underlying asset to gravitate toward strikes with massive open interest (high gamma) as expiration approaches. |

### Free GEX & Options Data

- [SpotGamma](https://spotgamma.com/) — The industry leader in mapping options dealer positioning. Provides institutional-grade Gamma and Delta levels for index and equity traders.
- [Squeezemetrics DIX & GEX](https://squeezemetrics.com/monitor/dix) — Free daily data on the Dark Index (DIX) and Gamma Exposure (GEX) for the S&P 500.
- [Cboe Data Shop](https://datashop.cboe.com/) — Source for official options data, volume statistics, and historical VIX data.

---

## Market Profile & Volume Profile

### Concepts to Master (in order)

1. **Auction Market Theory (AMT)** — The foundational model explaining that all markets are driven by the auction process of finding fair value.
2. **Time Price Opportunity (TPO)** — The building block of Market Profile; how price and time combine to reveal value.
3. **Initial Balance (IB)** — The first hour's range, used to gauge the day type and expected volatility.
4. **Point of Control (POC)** — The price level with the highest traded volume; the market's most accepted fair value.
5. **Value Area (VA)** — The range containing approximately 70% of the session's volume.
6. **Profile Shapes** — Normal, P-shape, b-shape, Double Distribution — each signals a different market narrative.
7. **Day Types** — Trend, Normal, Normal Variation, Neutral — classifying the day type before it ends is the core skill.

---

## Order Flow & Footprint Charts

Order flow trading reads the *real-time battle* between buyers and sellers at the level of individual transactions — the tape. Footprint charts are the primary visualization tool.

### Core Order Flow Concepts

| Concept | Description |
| --- | --- |
| **Volume Delta** | Net difference between buy-side and sell-side aggression (Ask volume minus Bid volume) |
| **Cumulative Volume Delta (CVD)** | Rolling total of delta over a session; reveals macro order flow direction |
| **Absorption** | Large passive orders at a price level consuming aggressive flow — often signals reversal |
| **Exhaustion** | Aggressive buying or selling fails to push price further — trap move signal |
| **Footprint Imbalances** | Significant delta imbalances on the bid/ask within a single price level inside a candle |
| **Stacked Imbalances** | Multiple consecutive imbalances at adjacent price levels — signals directional conviction |
| **POC (Footprint)** | Highest volume node within a single candle, distinct from profile-level POC |
| **VWAP** | Volume-Weighted Average Price — the institutional benchmark for execution quality |

### Free Educational Resources

- [AlgoStorm Trading Academy](https://algostorm.com/trading-academy/) — Professional structured curriculum covering technical analysis and institutional order flow.
- [Jigsaw Trading Education](https://www.jigsawtrading.com/blog/) — The official Jigsaw trading blog that features a good list of lessons.
- [Bookmap Resources](https://bookmap.com/knowledgebase) — Comprehensive knowledge base on reading the heatmap, liquidity, and order flow dynamics.
- [Quantower Blog](https://help.quantower.com) — Technical documentation and educational content on footprint charts and volume analysis.

---

## Market Microstructure & Academic Reading

For traders who want to understand the *mechanics* of how orders flow through exchanges and who the market participants really are.

### Recommended Books

| Book | Author | Why It Matters |
| --- | --- | --- |
| [High-Frequency Trading](https://www.amazon.com/High-Frequency-Trading-Practical-Algorithmic-Strategies/dp/1118343506) | Irene Aldridge | Useful for understanding the liquidity environment created by HFT participants. |
| [Market Liquidity: Theory, Evidence, and Policy](https://www.amazon.com/Market-Liquidity-Theory-Evidence-Policy/dp/0199936242) | Thierry Foucault | The definitive text on how liquidity is provided and consumed in modern electronic markets. |
| [Empirical Market Microstructure](https://www.amazon.com/Empirical-Market-Microstructure-Institutions-Econometrics/dp/0195301641) | Joel Hasbrouck | The technical standard for the econometrics of securities trading. |

### Web Resources & Research

- [SSRN Finance Research](https://www.ssrn.com/en/) — Repository of free academic papers on market microstructure, order flow, and liquidity.
- [CME Group Education](https://www.cmegroup.com/education.html) — Official educational resources from the exchange itself. Includes contract specifications, margin documentation, and market mechanics.
- [Bank for International Settlements (BIS) Research](https://www.bis.org/) — The "Central Bank of Central Banks." Publishes quarterly reviews and working papers on global liquidity and market structure.
- [FIX Trading Community](https://www.fixtrading.org/) — The non-profit that manages the FIX Protocol, the technical messaging standard institutions use to execute order flow.

---

## Free Tools & Calculators

### From AlgoStorm

Professional-grade tools built specifically for institutional order flow traders. Free with no account required.

| Tool | Description | Link |
| --- | --- | --- |
| **Trading Journal App** | A structured journaling tool designed to help traders track setups, document decision rationale, and identify behavioral patterns over time. | [→ Open Tool](https://algostorm.com/trading-journal/) |
| **Trading Calculators Suite** | 7 professional calculators covering position sizing, risk-to-reward, prop firm drawdown limits, and more. | [→ Open Tool](https://algostorm.com/trading-tools/) |
| **Prop Firm Blueprint** | A structured framework for approaching prop firm evaluations with a systematic risk management plan. | [→ Open Tool](https://algostorm.com/prop-firm-blueprint/) |

### General Free Tools

| Tool | Description | Link |
| --- | --- | --- |
| **TradingView** | Free tier includes charting, replay, Pine Script access, and basic volume indicators. | [tradingview.com](https://www.tradingview.com) |
| **CME Group FedWatch** | Tracks interest rate expectations — important macro context for futures traders. | [cmegroup.com/fedwatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html) |

---

## Systematic & Algorithmic Trading

Institutional edges are rigorously backtested. These frameworks allow traders to move beyond discretionary chart reading and quantify their strategies.

| Framework | Language | Focus |
| --- | --- | --- |
| [NautilusTrader](https://nautilustrader.io/) | Rust / Python | Open-source, ultra-high-performance algorithmic trading platform. Designed for HFT and institutional-grade event-driven backtesting. |
| [QuantConnect](https://www.quantconnect.com/) | C# / Python | Cloud-based algorithmic trading engine with massive built-in institutional datasets (tick, fundamental, alternative). |
| [Backtrader](https://www.backtrader.com/) | Python | The most widely used open-source Python backtesting framework. Excellent for prototyping systematic strategies. |

### Pine Script & Custom Tooling

TradingView is the most accessible charting platform globally. Learning Pine Script allows you to code custom order flow tools and backtest systematic concepts, breaking reliance on black-box retail indicators.

- **[Pine Script User Manual](https://www.tradingview.com/pine-script-docs/)** — The official guide to building custom indicators and strategies.
- **[Pine Script Reference](https://www.tradingview.com/pine-script-reference/)** — The complete syntax dictionary for all Pine Script functions.

---

## Institutional Tech & Data Stack

Institutions do not rely solely on charting GUIs; they process raw Level 3 order book and tick data.

- **[kdb+/q (KX Systems)](https://kx.com/)** — The absolute industry standard time-series database for Tier-1 banks and high-frequency trading firms. Capable of analyzing billions of ticks per second.
- **[ArcticDB (Man AHL)](https://arcticdb.io/)** — An open-source DataFrame database built by the Man AHL hedge fund specifically for storing and analyzing massive amounts of tick data at blazing speeds.
- **[Apache Parquet](https://parquet.apache.org/)** — The standard columnar storage file format used by quants to store historical tick data efficiently.
- **Python Data Stack** — The core toolkit: **Pandas** (time-series analysis), **NumPy** (vectorized math), and **SciPy** (statistical functions).

---

## Macro & Fixed Income Mechanics

The largest volume in the world flows through fixed income. Understanding Central Bank liquidity, Treasury yields, and overnight funding is crucial for predicting equity indices and FX.

- **[Federal Reserve Repo Facility Data](https://fred.stlouisfed.org/series/RRPONTSYD)** — Tracking Reverse Repo (RRP) balances to understand institutional liquidity and cash reserves in the banking system.
- **[Treasury Direct / Auction Results](https://www.treasurydirect.gov/instit/instit.htm)** — Monitoring bond auction bid-to-cover ratios provides a pure read on global institutional demand for US debt.
- **[MacroVoices (Podcast)](https://www.macrovoices.com/)** — Professional-grade macro podcast frequently featuring hedge fund managers discussing Eurodollar/SOFR markets, yield curve control, and global liquidity mechanics.

---

## Platforms & Charting Software

Platforms that support genuine order flow analysis — footprint charts, volume profiles, DOM, and tape.

| Platform | Strengths | Cost | Markets |
| --- | --- | --- | --- |
| [Trading Technologies (TT)](https://www.tradingtechnologies.com/) | The undisputed institutional standard for futures execution, algorithmic routing, and DOM trading. | High (Institutional) | Futures, Options, Crypto |
| [CQG](https://www.cqg.com/) | Deeply entrenched institutional platform for charting, analytics, and ultra-low latency trade routing. | High (Institutional) | Futures, Options, Equities |
| [Sierra Chart](https://www.sierrachart.com) | Industry gold standard for footprint charts and depth-of-market. Extremely configurable, excellent data. | Low (subscription) | Futures, Forex, Stocks |
| [ATAS](https://atas.net/) | Advanced order flow and volume trading platform. Massive following among European prop firms and footprint traders. | Paid (Free crypto) | Futures, Crypto |
| [Bookmap](https://bookmap.com) | Best heatmap visualization of the order book. Ideal for seeing liquidity placement and absorption in real time. | Free tier available | Futures, Crypto, Stocks |
| [Jigsaw Trader](https://www.jigsawtrading.com) | Purpose-built for tape reading and DOM trading. Excellent for short-term futures traders. | Paid | Futures |
| [Exocharts](https://exocharts.com/) | The absolute standard for crypto order flow and footprint analysis. Built specifically for high-volatility digital assets. | Paid | Crypto |
| [Quantower](https://www.quantower.com) | Modern UI with footprint charts, volume profile, and multi-broker connectivity. Free version available. | Free tier available | Futures, Forex, Crypto |
| [NinjaTrader](https://ninjatrader.com) | Free for simulation. Extensive ecosystem of add-ons. Popular for US futures markets. | Free (simulation) | Futures |
| [MotiveWave](https://motivewave.com/) | Extremely powerful for Elliott Wave theory, harmonics, and volume footprint. Native macOS support. | Paid | Futures, Stocks, Forex, Crypto |
| [GoCharting](https://gocharting.com/) | Web-based order flow and volume profile platform. One of the easiest ways to access footprint charts without heavy desktop software. | Free tier available | Crypto, Stocks, Forex |
| [TradingView](https://www.tradingview.com) | Best-in-class for charting accessibility and Pine Script ecosystem. Limited native order flow tools, but powerful for volume profile and custom indicators. | Free tier available | All markets |

---

## Free Data Sources

| Source | What You Get | Link |
| --- | --- | --- |
| **CME Group Data** | Official futures specifications, volume, open interest, and historical data | [cmegroup.com](https://www.cmegroup.com/market-data.html) |
| **Databento** | The modern standard for institutional Level 3 PCAP and tick data. Pay-as-you-go API. Free tier and sample data available. | [databento.com](https://databento.com/) |
| **Nasdaq Data Link (Quandl)** | Extensive futures and financial datasets. Free tier available. | [data.nasdaq.com](https://data.nasdaq.com) |
| **Glassnode** | The institutional standard for on-chain Bitcoin and Ethereum analytics (active addresses, exchange flows). | [glassnode.com](https://glassnode.com/) |
| **CoinGlass** | Essential for crypto order flow: tracks liquidations, funding rates, and open interest across all major derivatives exchanges. | [coinglass.com](https://www.coinglass.com/) |
| **CoinGecko** | The most reliable macro tracker for crypto market capitalization, volume, and API data integration. | [coingecko.com](https://www.coingecko.com/) |
| **Polygon.io** | Real-time and historical market data with a generous free tier. REST and WebSocket APIs. | [polygon.io](https://polygon.io) |
| **FRED (St. Louis Fed)** | Macroeconomic data essential for understanding interest rate environments and institutional positioning. | [fred.stlouisfed.org](https://fred.stlouisfed.org) |
| **COT Data (CFTC)** | Commitments of Traders reports — shows the positioning of commercials, large speculators, and small speculators in futures. | [cftc.gov](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm) |

---

## Podcasts & YouTube Channels

Channels and podcasts that consistently produce content grounded in institutional mechanics — not retail indicator noise.

| Channel / Podcast | Focus |
| --- | --- |
| [CME Group](https://www.youtube.com/@CMEGroup) | Official exchange channel. Excellent for understanding futures products, margin, and market mechanics. |
| [ICE](https://www.youtube.com/@ICE_Markets) | Intercontinental Exchange. Official channel for Energy (Brent/WTI) and soft commodities. |
| [CBOE](https://www.youtube.com/@CboeGlobalMarkets) | Chicago Board Options Exchange. The authority on options mechanics and VIX. |
| [Chat With Traders](https://chatwithtraders.com/) | The audio equivalent of *Market Wizards*. Deep-dive interviews with proprietary traders, quant researchers, and institutional operators. |

---

## Glossary of Key Concepts

A quick-reference glossary for traders new to institutional methodology.

| Term | Definition |
| --- | --- |
| **Auction Market Theory (AMT)** | The framework describing all market movement as a continuous auction process seeking to facilitate trade at fair value. |
| **Value Area (VA)** | The price range containing approximately 70% of a session's traded volume. Prices outside the VA represent "unfair" prices for that session. |
| **Point of Control (POC)** | The single price level with the highest traded volume in a given period. Represents the market's accepted fair value. |
| **Volume Delta** | The difference between volume traded at the ask (buyers initiating) and volume traded at the bid (sellers initiating). |
| **Absorption** | When large passive limit orders absorb aggressive 
... [TRUNCATED README]


==================================================


## [2/3] Repository: Options-Flow-Predictor (`PHASE4-QUANT-050`)
- **Full Name**: `PHASE4-QUANT-050_NavnoorBawa__Options-Flow-Predictor`
- **Description**: Options-flow features, unusual activity, dealer positioning, and short-horizon forecasting.
- **GitHub Stars**: 24
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Options Flow Predictor

## Overview

The Options Flow Predictor is a machine learning system that forecasts short-term stock price movements by analyzing institutional options trading patterns. The model identifies when large traders are positioning for specific directional moves by examining unusual options activity, dealer positioning, and market sentiment indicators.

## How It Works

### Core Theory

Large institutional traders often reveal their market expectations through options trading before making moves in the underlying stock. When hedge funds, pension funds, or sophisticated traders expect a stock to move, they frequently establish options positions first due to leverage advantages and risk management benefits.

The model captures these "smart money" signals by monitoring:

**Put/Call Ratio Analysis**
- When institutional traders expect upward moves, call buying increases relative to put buying
- Heavy put buying often precedes downward price movements
- The model tracks volume-weighted put/call ratios to identify sentiment shifts

**Unusual Volume Detection**
- Compares current options volume to historical patterns
- Identifies when trading activity exceeds normal levels by significant margins
- High volume often precedes major price movements as institutions build positions

**Dealer Positioning Analysis**
- Options dealers (market makers) hedge their exposures by trading the underlying stock
- When dealers are net long gamma, they buy stocks as prices fall and sell as prices rise
- This creates support and resistance levels that the model identifies and exploits

**Volatility Structure Patterns**
- Examines implied volatility across different strike prices and expiration dates
- Identifies when institutions are paying up for specific directional exposure
- Detects volatility skew patterns that indicate expected price movements

### Machine Learning Approach

The system employs ensemble learning combining multiple algorithms:

**Random Forest Component**
- Captures non-linear relationships between options flow features and price movements
- Handles high-dimensional options data effectively
- Provides feature importance rankings to identify key predictive signals

**XGBoost Component**
- Optimized for sequential pattern recognition in time series data
- Handles missing data and outliers common in options markets
- Provides gradient-boosted predictions for enhanced accuracy

**Ensemble Integration**
- Combines predictions from multiple models to reduce overfitting
- Weights models based on historical performance
- Provides more robust signals than individual algorithms

### Feature Engineering

The model transforms raw options data into predictive features:

**Technical Indicators**
- Momentum indicators like RSI to capture price trend information
- Volatility forecasts using statistical models
- Volume patterns and trading intensity measures

**Options-Specific Features**
- Gamma exposure calculations showing dealer hedging pressures
- At-the-money implied volatility levels
- Risk reversal patterns indicating directional bias

**Market Regime Detection**
- Identifies different market conditions (low volatility, high volatility, trending, ranging)
- Adjusts predictions based on current market regime
- Incorporates economic indicators for broader context

## Model Outputs

**Price Movement Predictions**
- Forecasts 1-day, 3-day, and 5-day percentage price changes
- Provides probability estimates for directional moves
- Indicates expected magnitude of movements

**Trading Signals**
- Clear buy/sell/hold recommendations based on prediction confidence
- Risk assessment for each signal
- Position sizing suggestions based on signal strength

**Market Intelligence**
- Unusual activity alerts for specific symbols
- Dealer positioning summaries
- Volatility regime classifications

## Target Performance

The model aims to achieve:
- Daily returns exceeding 40 basis points on average
- Sharpe ratios above 2.0 through consistent performance
- High hit rates on directional predictions
- Minimal drawdown periods during adverse conditions

## Methodology Advantages

**Real-Time Analysis**
- Processes current options flow data for immediate insights
- Updates predictions as new trading information becomes available
- Provides actionable signals during market hours

**Multi-Asset Coverage**
- Analyzes major ETFs representing different market segments
- Identifies sector rotation patterns through relative signal strength
- Enables portfolio-level strategy implementation

**Risk-Aware Predictions**
- Incorporates volatility forecasts into position recommendations
- Provides confidence intervals around predictions
- Flags high-risk periods for reduced position sizing

The Options Flow Predictor transforms complex institutional trading patterns into actionable investment signals, providing retail and institutional traders with insights typically available only to market makers and sophisticated hedge funds.


==================================================


## [3/3] Repository: dhan-mcp-fw (`PHASE4-QUANT-067`)
- **Full Name**: `PHASE4-QUANT-067_harsh5i__dhan-mcp-fw`
- **Description**: MCP server for NSE stock analysis & NIFTY/BANKNIFTY options trading via Dhan. 39 tools + strategy framework. LGPL-3.0
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# DhanMCP-FW — NSE Stock Analysis & Options Trading via MCP

> **Disclaimer:** This is an experimental project built for personal use and learning. It is **not** financial advice, investment guidance, or a trading recommendation of any kind. Any real trades or trading decisions made using this tool are entirely at your own risk. The authors accept no responsibility for financial losses incurred through the use of this software. This project is **not affiliated with, endorsed by, or associated with Dhan, DhanHQ, or any other financial institution or organisation.** Always do your own research and consult a qualified financial advisor before trading. Feedback and contributions are welcome!

An MCP (Model Context Protocol) server for NSE stock analysis and NIFTY/BANKNIFTY options trading via [Dhan](https://dhan.co) broker, with a built-in **strategy framework** for creating, backtesting, and running automated trading strategies. Built from scratch. Any MCP-compatible AI client — Claude Code, OpenClaw, Codex CLI, Gemini CLI, Cursor, VS Code Copilot — can connect, analyse, and trade.

> **39 tools** covering stock analysis, market data, historical charts, technical indicators, portfolio, order management, options execution, and a full strategy framework — all safety-gated.

## Architecture

```
Any AI Client (Claude Code, OpenClaw/Olive, Codex, Gemini CLI)
    ↕ MCP Protocol (stdio)
dhan-nifty-mcp (this server) — 39 tools (27 trading + 12 framework)
    ├── Safety Layer (validates every write order)
    ├── Audit Logger (JSONL, every tool call)
    └── Dhan Client (thin SDK wrapper)
        ↕ HTTP/REST
    Dhan API (api.dhan.co/v2)
```

## Files

| File | Purpose |
|------|---------|
| `server.py` | FastMCP server, all 39 tool definitions, entry point |
| `safety.py` | 6-step validation chain: instrument whitelist, market hours, lot limit, position limit, value cap, price sanity |
| `dhan_client.py` | Thin wrapper around dhanhq SDK. All Dhan API calls live here. Stock alias map for common names (RIL→RELIANCE, SBI→SBIN, etc.) |
| `models.py` | Dataclasses: OrderRequest, SafetyResult, DryRunResponse, LiveResponse, ErrorResponse. Enums for OrderAction, OrderType (MARKET/LIMIT/SL/SLM), OptionType. Lot size lookup. |
| `logger.py` | AuditLogger class. Writes every tool call as JSONL to ~/.dhan-mcp/logs/trades.jsonl |
| `config.yaml` | Credentials, safety rules (mode, limits, whitelist, market hours), logging paths |
| `ollama_bridge.py` | Standalone bridge for connecting Ollama models to this MCP server |
| `requirements.txt` | dhanhq, mcp, pyyaml |

## Tools (27)

### Server & Auth (3)
| Tool | Purpose |
|------|---------|
| `server_status` | Check token validity, server mode, safety config. **Call this first in every session.** |
| `update_token` | Hot-swap expired Dhan access token without restarting. Saves to config.yaml. |
| `market_status` | Is market open/closed/holiday/pre-market? Time to open/close. Knows NSE holidays 2026. |

### Market Data — Quick Price (3, single-call, no chaining needed)
| Tool | Purpose |
|------|---------|
| `get_stock_price(name)` | Get any stock's live price by name/ticker. Handles aliases (RIL, SBI, HDFC, TATA, etc). Returns LTP, OHLC, 52wk range, volume. |
| `get_option_price(symbol, strike, expiry, option_type)` | Get any NIFTY/BANKNIFTY option price in one call. Returns LTP, bid/ask, IV, Greeks, OI, volume, spot price, security_id. |
| `get_bulk_prices(instruments)` | Multiple instruments in one API call. Format: `"INDEX:13,NSE_EQ:1333,NSE_FNO:40752"` |

### Market Data — Raw (3)
| Tool | Purpose |
|------|---------|
| `get_ltp(security_id, exchange_segment)` | Last traded price for any instrument by security_id. |
| `get_option_chain(symbol, expiry)` | Full option chain — all strikes, premiums, OI, Greeks, IV. |
| `get_market_depth(security_id, exchange_segment)` | 5-level bid/ask depth. |

### Historical Data (2)
| Tool | Purpose |
|------|---------|
| `get_historical_daily(security_id, from_date, to_date, ...)` | Daily OHLCV candles, any date range. |
| `get_intraday_candles(security_id, from_date, to_date, interval, ...)` | Minute candles (1/5/15/25/60 min). Last 5 trading days only. |

### Portfolio (4)
| Tool | Purpose |
|------|---------|
| `get_positions` | Open intraday/F&O positions with live P&L. |
| `get_holdings` | Long-term portfolio (stocks, ETFs, MFs). |
| `get_margins` | Available/used margin and fund limits. |
| `get_pnl_summary` | Today's total P&L — realized + unrealized, per-position breakdown. |

### Lookup (3)
| Tool | Purpose |
|------|---------|
| `search_stock(query)` | Find any NSE stock by name/ticker. Has alias map for 30+ popular shorthands. |
| `lookup_security_id(symbol, expiry, strike, option_type)` | Find Dhan security_id for a specific option contract. |
| `get_expiry_list(symbol)` | Get all valid expiry dates for NIFTY/BANKNIFTY. |

### Order Management (6)
| Tool | Purpose |
|------|---------|
| `get_order_book` | All orders placed today + status (PENDING/EXECUTED/CANCELLED/REJECTED). |
| `get_order_status(order_id)` | Detailed status of a specific order. |
| `get_trade_book` | All executed trades today with fill prices. |
| `get_trade_history(from_date, to_date)` | Historical trades over any date range. |
| `modify_order(order_id, order_type, quantity, price, ...)` | Change pending order's price, qty, or type. |
| `calculate_margin(security_id, transaction_type, quantity, price, ...)` | Check margin required before placing a trade. |

### Execution (3, safety-gated)
| Tool | Purpose |
|------|---------|
| `place_order(symbol, strike, expiry, option_type, lots, ...)` | Place options order. Supports MARKET, LIMIT, SL (stop-loss limit), SLM (stop-loss market). Goes through 6 safety checks. |
| `cancel_order(order_id)` | Cancel a pending order. |
| `exit_all(confirmation_phrase)` | **EMERGENCY KILL SWITCH.** Cancels all orders + market-exits all positions. Requires exact phrase `CONFIRM_EXIT_ALL`. |

## Common Workflows

### 1. Start of session (always do this first)
```
server_status → check token valid + mode
market_status → check if market is open
```

### 2. Get NIFTY option price (one call)
```
get_option_price(symbol="NIFTY", strike=22800, expiry="2026-04-07", option_type="CE")
→ LTP, bid/ask, IV, Greeks, OI, security_id — everything in one response
```

### 3. Get any stock price (one call)
```
get_stock_price(name="RIL")
→ RELIANCE LTP, OHLC, volume, 52wk range
```
Aliases work: RIL, SBI, HDFC, TATA, ICICI, KOTAK, AIRTEL, ADANI, etc.

### 4. Don't know the expiry date?
```
get_expiry_list(symbol="NIFTY")
→ list of all valid expiries, nearest weekly highlighted
```

### 5. Check NIFTY/BANKNIFTY spot price
```
get_ltp(security_id="13", exchange_segment="INDEX")    # NIFTY
get_ltp(security_id="25", exchange_segment="INDEX")    # BANKNIFTY
```

### 6. Historical analysis
```
# Daily candles — any date range
get_historical_daily(security_id="13", from_date="2026-01-01", to_date="2026-04-04", exchange_segment="INDEX", instrument_type="INDEX")

# Intraday 5-min candles — last 5 days only
get_intraday_candles(security_id="13", from_date="2026-04-02", to_date="2026-04-02", interval=5, exchange_segment="INDEX", instrument_type="INDEX")

# For stocks: use search_stock first to get security_id, then:
get_historical_daily(security_id="1333", ..., exchange_segment="NSE_EQ", instrument_type="EQUITY")

# For options: use get_option_price or lookup_security_id first, then:
get_historical_daily(security_id="40752", ..., exchange_segment="NSE_FNO", instrument_type="OPTIDX")
```

### 7. Place a trade (full flow)
```
market_status                         → confirm market is open
get_option_price(...)                 → get price + security_id
calculate_margin(security_id, ...)    → check if enough funds
place_order(symbol, strike, expiry, option_type, lots, security_id=...)  → execute
get_order_status(order_id)            → confirm fill
```

### 8. Place a stop-loss order
```
place_order(
    symbol="NIFTY", strike=22800, expiry="2026-04-07", option_type="CE",
    lots=1, action="SELL", order_type="SLM", trigger_price=180,
    security_id="40752"
)
→ Sells when price drops to 180 (stop-loss market)
```

### 9. Monitor during the day
```
get_pnl_summary     → total P&L
get_positions        → open positions detail
get_order_book       → pending orders
get_trade_book       → what filled today
```

### 10. Watch multiple instruments at once
```
get_bulk_prices(instruments="INDEX:13,INDEX:25,NSE_EQ:1333,NSE_FNO:40752")
→ NIFTY spot, BANKNIFTY spot, HDFC Bank, and a specific option — all in one call
```

### 11. Token expired mid-session
```
server_status           → sees TOKEN_EXPIRED
→ AI asks user to generate new token from Dhan dashboard
update_token("eyJ...")  → hot-swaps token, saves to config.yaml, no restart needed
server_status           → confirms new token is valid
```

### 12. Emergency exit
```
exit_all(confirmation_phrase="CONFIRM_EXIT_ALL")
→ Cancels ALL pending orders + market-exits ALL positions
```

## Instrument ID Reference

| Instrument | Security ID | Segment |
|-----------|-------------|---------|
| NIFTY 50 (spot) | 13 | INDEX |
| BANKNIFTY (spot) | 25 | INDEX |
| NIFTY/BANKNIFTY options | Use `get_option_price` or `lookup_security_id` | NSE_FNO |
| Any stock | Use `get_stock_price` or `search_stock` | NSE_EQ |

## Safety Rules (config.yaml)

- **mode**: `dry-run` (default) or `live` — dry-run logs what would happen, never hits Dhan
- **max_lots_per_order**: configurable (default 2)
- **max_open_positions**: configurable (default 5)
- **max_order_value**: INR cap per order (default 50000)
- **allowed_instruments**: NIFTY, BANKNIFTY only
- **market_hours**: 09:15-15:30 IST
- **price_deviation_pct**: 20% max from LTP for limit orders
- **kill_phrase**: `CONFIRM_EXIT_ALL`

## Key Design Decisions

1. **Single MCP server** (not per-tool) for shared state and speed
2. **Safety layer is non-bypassable**: every write tool goes through safety.py
3. **Dry-run first**: server starts safe, must explicitly switch to live
4. **Kill switch requires passphrase**: prevents accidental LLM triggers
5. **Audit everything**: every tool call logged with params, result, latency, errors
6. **One-call tools**: `get_stock_price`, `get_option_price` — no chaining needed for common tasks
7. **Stock aliases**: RIL→RELIANCE, SBI→SBIN, etc. — natural language works
8. **Hot-swap auth**: `update_token` replaces expired tokens without restart
9. **Market awareness**: `market_status` knows holidays, weekends, pre/post market
10. **Lot sizes**: NIFTY=75, BANKNIFTY=30
11. **Multi-strategy**: concurrent execution with independent state per strategy
12. **Auto-recovery**: running strategies survive server restarts via persistent state file
13. **Honest backtesting**: options backtests clearly disclose spot-based P&L limitation

## Dhan Specifics

- Underlying IDs: NIFTY=`13`, BANKNIFTY=`25`
- Exchange segments: `IDX_I` (index), `NSE_FNO` (options), `NSE_EQ` (equities)
- SDK: dhanhq Python package
- Access tokens: 24-hour validity, generated from Dhan dashboard, no auto-refresh
- Option chain: keyed by strike price (e.g. `"22800.000000"`), nested `ce`/`pe` objects
- Security master CSV: `https://images.dhan.co/api-data/api-scrip-master.csv`

## Setup

### Prerequisites
- Python 3.10+
- [Dhan](https://dhan.co) trading account with API access
- An MCP-compatible AI client

### Installation

```bash
git clone https://github.com/youruser/dhan-nifty-mcp.git
cd dhan-nifty-mcp
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### Configuration

Copy and edit the config:
```bash
cp config.yaml.example config.yaml
# Edit config.yaml with your Dhan client_id and access_token
```

Generate an access token from [Dhan API Dashboard](https://knowledge.dhan.co). Tokens are valid for 24 hours.

### Register with your AI client

```bash
# Claude Code
claude mcp add dhan-nifty -- python3 /path/to/dhan-nifty-mcp/server.py

# OpenClaw
mcporter config add dhan-nifty --stdio "python3 /path/to/dhan-nifty-mcp/server.py"

# Or run standalone
python3 server.py
```

### Ollama Bridge (optional)

Connect local Ollama models to the MCP server:
```bash
.venv/bin/python3 ollama_bridge.py --model qwen3:8b
```

### View Audit Logs

Every tool call is logged:
```bash
cat ~/.dhan-mcp/logs/trades.jsonl | python3 -m json.tool
```

## Roadmap

- [x] MCP server with 27 tools
- [x] Safety layer (6-step validation)
- [x] Dry-run mode
- [x] Audit logging
- [x] Stock alias resolution
- [x] Token hot-swap
- [x] Market status awareness
- [x] Ollama bridge
- [x] Strategy framework (exposed as additional MCP tools)
- [x] Multi-strategy concurrent execution
- [x] Auto-recovery on server restart
- [x] ATR-based and trailing stop loss types (with activate_after threshold)
- [x] Options-aware SL/target (uses live option premium)
- [x] Backtest with options limitations disclosure
- [x] Derived indicators (LAG, CHANGE, SLOPE) — two-pass computation
- [x] Direction-specific exits (conditions_ce / conditions_pe)
- [x] Time stop (max_bars)
- [ ] Partial exits (staged profit-taking)
- [ ] Multi-leg orders (straddles, strangles, spreads)
- [ ] WebSocket live feed integration

## Strategy Framework

The framework adds 12 strategy management tools to this same MCP server. Any connected AI can create, run, monitor, and improve trading strategies — all through the same MCP interface.

### How it works

```
Any AI client connects to DhanMCP
    → sees 27 trading tools + 12 framework tools
    → creates strategy via create_strategy tool (YAML)
    → starts strategy via start_strategy (paper or live)
    → framework runs internally: scheduler → data → indicators → engine → executor
    → strategy engine is pure code (deterministic, no AI judgment)
    → Gemma4/local LLM writes commentary on each trade (narrator role)
    → main AI analyses performance + commentary → improves strategy
```

### Framework tools

| Tool | Purpose |
|------|---------|
| `get_strategy_template` | Get YAML schema, supported indicators, condition syntax |
| `create_strategy` | Validate and save a strategy from YAML |
| `list_saved_strategies` | List all saved strategies |
| `get_strategy_details` | Get full config of a strategy |
| `start_strategy` | Start background scheduler (paper/live mode). Multiple strategies can run concurrently. |
| `stop_strategy` | Stop a running strategy by ID (or the only running one) |
| `get_strategy_status` | Live status for one or all strategies: phase, signals, position, P&L |
| `get_trade_log` | Trade history with reasons and performance stats |
| `get_strategy_commentary` | AI-generated daily summary via Ollama |
| `get_strategy_profile` | Version history, changes, performance snapshots |
| `log_strategy_change` | Record improvements or config changes to profile |
| `backtest_strategy` | Replay historical candles through strategy, simulate trades |
| `dhanwin` | Activation menu — returns the 5-option menu for any AI client |

### Three AI roles

1. **Main AI** (Claude, Gemini, etc.) — designs strategy with user, analyses performance, improves strategy
2. **Strategy engine** (pure Python code) — deterministic rules: `if rsi < 30 and ema_cross: BUY`. No AI judgment.
3. **Narrator AI** (Gemma4 via Ollama) — writes real-time commentary on each trade for later analysis

### Supported indicators (24 base + 3 derived)

**Base:** `EMA` `SMA` `RSI` `MACD` `MACD_SIGNAL` `MACD_DIFF` `BOLLINGER_HIGH` `BOLLINGER_LOW` `BOLLINGER_MID` `ATR` `VWAP` `SUPERTREND` `ADX` `STOCH_K` `STOCH_D` `OBV` `DPO` `DPO_SIGNAL` `OBV_HULL` `OBV_HULL_SIGNAL` `VORTEX_POS` `VORTEX_NEG` `VORTEX_SIGNAL` `HULL_MA` `CONFIDENCE`

**Derived** (reference other indicators, computed in second pass):
- `LAG` — value N bars ago. Config: `{name: adx_prev, type: LAG, source: adx, period: 1}`
- `CHANGE` — 1-bar delta. Config: `{name: ema_change, type: CHANGE, source: ema_trend}`
- `SLOPE` — rate of change over N bars. Config: `{name: ema_slope, type: SLOPE, source: ema_trend, period: 3}`

Use derived indicators to express "rising", "falling", or "compare to previous" conditions like `adx > adx_prev`.

### Strategy lifecycle

```
User discusses with AI → AI calls get_strategy_template
    → AI creates strategy YAML → create_strategy (validates + saves)
    → start_strategy mode=paper → monitor via get_strategy_status
    → get_trade_log for results → get_strategy_commentary for AI analysis
    → AI improves strategy → create new version → repeat
    → user approves → start_strategy mode=live
```

### Strategy YAML example

```yaml
id: rsi_ema_nifty_v1
name: "RSI + EMA Crossover on NIFTY"
instrument:
  index: NIFTY
  option_preference: ATM
  option_type: CE
  trade_type: BUY
  expiry_preference: nearest
interval: 5
indicators:
  - {name: ema_fast, type: EMA, period: 9}
  - {name: ema_slow, type: EMA, period: 21}
  - {name: rsi, type: RSI, period: 14}
  - {name: atr, type: ATR, period: 14}
  - {name: ema_slope, type: SLOPE, source: ema_fast, period: 3}  # derived
entry:
  conditions: ["rsi < 30", "ema_fast > ema_slow", "ema_slope > 0"]
  lots: 1
exit:
  conditions: ["rsi > 70", "ema_fast < ema_slow"]
  max_bars: 6  # time stop
stop_loss: {type: atr, multiplier: 2.0, atr_indicator: atr, min: 50, max: 120}
target: {type: points, value: 200}
risk:
  max_loss_per_day: 5000
  max_trades_per_day: 5
  cool_off_after_loss: 2
```

### Framework architecture

```
framework/
├── schema.py        # Strategy YAML validation + storage
├── database.py      # SQLite: candles, indicators, trades, state
├── data_manager.py  # OHLC fetch + 24 base indicators + 3 derived types (two-pass)
├── engine.py        # Condition evaluator + SL types (%, pts, ATR, trailing) + time stop + strike selector
├── risk.py          # Risk governor (daily loss, trade count, cool-off)
├── scheduler.py     # Multi-strategy background loop + trade execution + auto-recovery
├── narrator.py      # Gemma4/Ollama commentary bridge
└── backtester.py    # Historical replay + signal validation (options P&L disclaimer)
```

### Stop loss types

| Type | Config | Description |
|------|--------|-------------|
| `percentage` | `{type: percentage, value: 20}` | Fixed % from entry price |
| `points` | `{type: points, value: 150}` | Fixed points from entry price |
| `atr` | `{type: atr, multiplier: 2.0, atr_indicator: atr, min: 50, max: 120}` | Dynamic ATR-based SL with optional min/max clamps |
| `trailing` | `{type: trailing, value: 40, trail_type: points, activate_after: 80}` | Trails from peak favorable price. Optional `activate_after`: only starts trailing after N points profit. |

### Exit features

- **Direction-specific exits**: Use `exit.conditions_ce` and `exit.conditions_pe` for separate CE/PE exit logic
- **Time stop**: `exit.max_bars: 6` — force exit after N candles if trade hasn't moved

### Multi-strategy & persistence

- Multiple strategies can run concurrently
- Running strategies persist to `~/.dhan-mcp/running_strategies.json`
- Auto-restored on server restart — no manual re-deployment needed

### Backtesting limitations

Backtesting replays historical spot index candles through the strategy engine. For options strategies, the P&L is computed on spot movement, not actual option premiums (historical option premium data is unavailable via Dhan API). **Use paper trading for accurate options P&L.** Signal timing and direction from backtests remain valid.

### Risk controls (hard limits, strategy cannot override)

- **Max daily loss** — stops trading when cumulative P&L hits the limit
- **Max trades per day** — prevents overtrading
- **Cool-off period** — skips N signals after consecutive losses

## License

LGPL-3.0 — see [LICENSE](LICENSE)

### Core Implementation Code & Architecture
#### File: `framework/__init__.py`
```python

```

#### File: `logger.py`
```python
"""
Audit logger for dhan-nifty-mcp.
Every tool call is logged as a single JSON line.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


class AuditLogger:
    def __init__(self, config: dict):
        log_cfg = config.get("logging", {})
        log_dir = os.path.expanduser(log_cfg.get("dir", "~/.dhan-mcp/logs"))
        audit_file = log_cfg.get("audit_file", "trades.jsonl")

        Path(log_dir).mkdir(parents=True, exist_ok=True)
        self._path = os.path.join(log_dir, audit_file)

    def log(
        self,
        tool: str,
        params: dict,
        result: Any,
        mode: str,
        latency_ms: Optional[float] = None,
        error: Optional[str] = None,
    ):
        """Append a single audit entry."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "tool": tool,
            "mode": mode,
            "params": _safe_serialize(params),
            "result": _safe_serialize(result),
            "latency_ms": round(latency_ms, 1) if latency_ms else None,
            "error": error,
        }

        try:
            with open(self._path, "a") as f:
                f.write(json.dumps(entry, default=str) + "\n")
        except Exception as e:
            # logging should never crash the server
            print(f"[AUDIT LOG ERROR] {e}")

    @property
    def path(self) -> str:
        return self._path


def _safe_serialize(obj: Any) -> Any:
    """Convert to JSON-safe types."""
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if hasattr(obj, "__dict__"):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}
    return obj
```

#### File: `framework/risk.py`
```python
"""
Risk governor — enforces daily loss limits, trade count, and cool-off periods.
The strategy cannot override these. Hard stops.
"""

from framework.database import StrategyDB


class RiskGovernor:
    """Checks risk limits before allowing any trade."""

    def __init__(self, strategy: dict, db: StrategyDB):
        self.risk = strategy.get("risk", {})
        self.db = db
        self.max_loss = self.risk.get("max_loss_per_day", 5000)
        self.max_trades = self.risk.get("max_trades_per_day", 5)
        self.cool_off = self.risk.get("cool_off_after_loss", 0)

    def can_trade(self) -> dict:
        """Check if trading is allowed. Returns {allowed: bool, reason: str}."""

        # Check daily P&L
        perf = self.db.compute_performance()
        today_pnl = self._get_today_pnl()
        if today_pnl <= -self.max_loss:
            return {
                "allowed": False,
                "reason": f"Daily loss limit hit: {today_pnl:.2f} <= -{self.max_loss}",
            }

        # Check trade count
        today_trades = self._get_today_trade_count()
        if today_trades >= self.max_trades:
            return {
                "allowed": False,
                "reason": f"Max trades for today: {today_trades}/{self.max_trades}",
            }

        # Check cool-off
        if self.cool_off > 0:
            recent_losses = self._get_recent_consecutive_losses()
            if recent_losses >= self.cool_off:
                return {
                    "allowed": False,
                    "reason": f"Cool-off active: {recent_losses} consecutive losses (limit: {self.cool_off})",
                }

        return {"allowed": True, "reason": "OK"}

    def _get_today_pnl(self) -> float:
        """Sum of P&L for today's closed trades."""
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        trades = self.db.get_trades(limit=100)
        total = 0
        for t in trades:
            if t.get("timestamp", "").startswith(today) and t.get("pnl") is not None:
                total += t["pnl"]
        return total

    def _get_today_trade_count(self) -> int:
        """Count trades placed today."""
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        trades = self.db.get_trades(limit=100)
        return sum(1 for t in trades if t.get("timestamp", "").startswith(today))

    def _get_recent_consecutive_losses(self) -> int:
        """Count consecutive losses from most recent trade backwards."""
        trades = self.db.get_trades(limit=20)
        count = 0
        for t in reversed(trades):
            if t.get("pnl") is not None and t["pnl"] <= 0:
                count += 1
            else:
                break
        return count
```

#### File: `models.py`
```python
"""
Data models for dhan-nifty-mcp.
Plain dataclasses, no external dependencies.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum


# ── Enums ──────────────────────────────────────────────────

class OrderAction(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    SL = "SL"
    SLM = "SLM"


class OptionType(str, Enum):
    CE = "CE"
    PE = "PE"


class ProductType(str, Enum):
    INTRADAY = "INTRADAY"
    MARGIN = "MARGIN"
    CNC = "CNC"


class ServerMode(str, Enum):
    DRY_RUN = "dry-run"
    LIVE = "live"


# ── Order request ─────────────────────────────────────────

@dataclass
class OrderRequest:
    symbol: str               # "NIFTY" or "BANKNIFTY"
    strike: float             # 24500, 25000, etc.
    expiry: str               # "2026-04-09"
    option_type: OptionType   # CE or PE
    action: OrderAction       # BUY or SELL
    lots: int                 # number of lots (1 lot = 75 for NIFTY, 30 for BANKNIFTY)
    order_type: OrderType     # MARKET or LIMIT
    price: Optional[float] = None  # required for LIMIT orders


# ── Safety check result ───────────────────────────────────

@dataclass
class SafetyResult:
    passed: bool
    instrument_allowed: bool = True
    within_market_hours: bool = True
    within_lot_limit: bool = True
    within_position_limit: bool = True
    within_value_limit: bool = True
    price_sane: bool = True
    rejection_reason: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


# ── Responses ─────────────────────────────────────────────

@dataclass
class DryRunResponse:
    status: str = "DRY-RUN"
    would_execute: dict = field(default_factory=dict)
    safety_checks: dict = field(default_factory=dict)
    message: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class LiveResponse:
    status: str = "EXECUTED"
    order_id: Optional[str] = None
    details: dict = field(default_factory=dict)
    message: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ErrorResponse:
    status: str = "REJECTED"
    reason: str = ""
    safety_checks: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


# ── Lot size lookup ───────────────────────────────────────

LOT_SIZES = {
    "NIFTY": 75,
    "BANKNIFTY": 30,
}


def get_lot_size(symbol: str) -> int:
    return LOT_SIZES.get(symbol.upper(), 75)
```

#### File: `safety.py`
```python
"""
Safety layer for dhan-nifty-mcp.
Every order passes through validate_order() before reaching Dhan.
"""

from datetime import datetime, time
from typing import Optional
from models import OrderRequest, SafetyResult, get_lot_size


def validate_order(
    order: OrderRequest,
    config: dict,
    current_ltp: Optional[float] = None,
    open_position_count: int = 0,
) -> SafetyResult:
    """
    Run all safety checks on an order request.
    Returns SafetyResult with pass/fail and per-check details.
    """
    safety = config.get("safety", {})
    result = SafetyResult(passed=True)

    # ── 1. Instrument whitelist ────────────────────────
    allowed = [s.upper() for s in safety.get("allowed_instruments", [])]
    if order.symbol.upper() not in allowed:
        result.passed = False
        result.instrument_allowed = False
        result.rejection_reason = f"Instrument '{order.symbol}' not in allowed list: {allowed}"
        return result

    # ── 2. Market hours ───────────────────────────────
    now = datetime.now().time()
    hours = safety.get("market_hours", {})
    market_start = _parse_time(hours.get("start", "09:15"))
    market_end = _parse_time(hours.get("end", "15:30"))

    if not (market_start <= now <= market_end):
        result.passed = False
        result.within_market_hours = False
        result.rejection_reason = (
            f"Outside market hours. Current: {now.strftime('%H:%M')}, "
            f"Allowed: {hours.get('start')}-{hours.get('end')}"
        )
        return result

    # ── 3. Lot limit ──────────────────────────────────
    max_lots = safety.get("max_lots_per_order", 2)
    if order.lots > max_lots:
        result.passed = False
        result.within_lot_limit = False
        result.rejection_reason = f"Lots ({order.lots}) exceeds max ({max_lots})"
        return result

    # ── 4. Open position limit ────────────────────────
    max_positions = safety.get("max_open_positions", 5)
    if open_position_count >= max_positions:
        result.passed = False
        result.within_position_limit = False
        result.rejection_reason = (
            f"Open positions ({open_position_count}) "
            f"already at max ({max_positions})"
        )
        return result

    # ── 5. Order value cap ────────────────────────────
    max_value = safety.get("max_order_value", 50000)
    if current_ltp is not None:
        lot_size = get_lot_size(order.symbol)
        total_qty = order.lots * lot_size
        estimated_value = current_ltp * total_qty
        if estimated_value > max_value:
            result.passed = False
            result.within_value_limit = False
            result.rejection_reason = (
                f"Estimated order value Rs.{estimated_value:,.2f} "
                f"exceeds max Rs.{max_value:,.2f}"
            )
            return result

    # ── 6. Price sanity (limit orders only) ───────────
    if order.price is not None and current_ltp is not None:
        deviation_pct = safety.get("price_deviation_pct", 20)
        deviation = abs(order.price - current_ltp) / current_ltp * 100
        if deviation > deviation_pct:
            result.passed = False
            result.price_sane = False
            result.rejection_reason = (
                f"Limit price Rs.{order.price} deviates {deviation:.1f}% "
                f"from LTP Rs.{current_ltp} (max allowed: {deviation_pct}%)"
            )
            return result

    return result


def _parse_time(t: str) -> time:
    """Parse 'HH:MM' string to time object."""
    parts = t.strip().split(":")
    return time(int(parts[0]), int(parts[1]))
```

#### File: `framework/narrator.py`
```python
"""
Narrator — sends trade events to a local LLM (Gemma4 via Ollama) for commentary.
The narrator does NOT make trading decisions. It only provides human-readable
color commentary on what the strategy is doing and why.
"""

import json
import subprocess
from datetime import datetime
from typing import Optional

from framework.database import StrategyDB


class Narrator:
    """Generates trade commentary via a local LLM (Ollama)."""

    def __init__(self, strategy: dict, db: StrategyDB, model: str = "gemma3:4b"):
        self.strategy = strategy
        self.db = db
        self.model = model
        self.enabled = True

    def comment_on_entry(self, signal: dict, snapshot: dict, option: dict) -> str:
        """Generate commentary when a trade is entered."""
        prompt = self._build_prompt(
            event="ENTRY",
            details={
                "signal": signal["signal"],
                "reason": signal["reason"],
                "spot_price": snapshot.get("close"),
                "strike": option.get("strike"),
                "option_type": option.get("option_type"),
                "premium": option.get("ltp"),
                "indicators": snapshot.get("indicators", {}),
                "strategy_name": self.strategy.get("name"),
            },
        )
        return self._ask_llm(prompt)

    def comment_on_exit(self, signal: dict, position: dict, pnl: float) -> str:
        """Generate commentary when a trade is exited."""
        prompt = self._build_prompt(
            event="EXIT",
            details={
                "exit_type": signal["signal"],
                "reason": signal["reason"],
                "entry_price": position.get("entry_price"),
                "strike": position.get("strike"),
                "option_type": position.get("option_type"),
                "pnl": pnl,
                "hold_duration": self._hold_duration(position),
                "strategy_name": self.strategy.get("name"),
            },
        )
        return self._ask_llm(prompt)

    def comment_on_hold(self, snapshot: dict, position: dict) -> str:
        """Generate brief commentary on why we're holding."""
        entry_price = position.get("entry_price", 0)
        close = snapshot.get("close", 0)
        unrealized = close - entry_price if position.get("action") == "BUY" else entry_price - close

        prompt = self._build_prompt(
            event="HOLD",
            details={
                "spot_price": close,
                "entry_price": entry_price,
                "unrealized_pnl_per_unit": round(unrealized, 2),
                "indicators": snapshot.get("indicators", {}),
                "strategy_name": self.strategy.get("name"),
            },
        )
        return self._ask_llm(prompt)

    def daily_summary(self) -> str:
        """Generate end-of-day summary."""
        perf = self.db.compute_performance()
        trades = self.db.get_trades(limit=20)
        today = datetime.now().strftime("%Y-%m-%d")
        today_trades = [t for t in trades if t.get("timestamp", "").startswith(today)]

        prompt = self._build_prompt(
            event="DAILY_SUMMARY",
            details={
                "date": today,
                "strategy_name": self.strategy.get("name"),
                "total_trades_today": len(today_trades),
                "performance": perf,
                "trades": today_trades[:10],
            },
        )
        return self._ask_llm(prompt)

    def _build_prompt(self, event: str, details: dict) -> str:
        """Build a prompt for the narrator LLM."""
        system = (
            "You are a concise options trading commentator. "
            "Provide brief, insightful commentary on trade events. "
            "Keep responses under 3 sentences. Use plain language. "
            "Focus on what happened and why it matters."
        )

        user_msg = f"Event: {event}\n{json.dumps(details, indent=2, default=str)}"

        return json.dumps({
            "system": system,
            "user": user_msg,
        })

    def _ask_llm(self, prompt_json: str) -> str:
        """Call Ollama API via subprocess."""
        if not self.enabled:
            return ""

        try:
            prompt = json.loads(prompt_json)
            result = subprocess.run(
                [
                    "ollama", "run", self.model,
                    "--system", prompt["system"],
                    prompt["user"],
                ],
                capture_output=True,
                text=True,
                timeout=30,
            )
            commentary = result.stdout.strip()
            return commentary if commentary else "(no commentary)"
        except subprocess.TimeoutExpired:
            return "(narrator timeout)"
        except FileNotFoundError:
            return "(ollama not installed)"
        except Exception as e:
            return f"(narrator error: {e})"

    def _hold_duration(self, position: dict) -> str:
        """Calculate how long we've been in a position."""
        entered = position.get("entered_at")
        if not entered:
            return "unknown"
        try:
            entry_time = datetime.fromisoformat(entered)
            delta = datetime.now() - entry_time
            mins = int(delta.total_seconds() / 60)
            if mins < 60:
                return f"{mins}m"
            return f"{mins // 60}h {mins % 60}m"
        except Exception:
            return "unknown"
```


==================================================
