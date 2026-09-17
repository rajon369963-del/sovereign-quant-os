# ⚡ [QUANT-SOURCE-203] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_203_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: OrderFlowMap (`PHASE4-QUANT-004`)
- **Full Name**: `PHASE4-QUANT-004_Azhagesan-dev__OrderFlowMap`
- **Description**: Bookmap-style order flow visualizer in a single HTML file — real-time heatmaps, trade bubbles, DOM ladder, volume profile, CVD, and liquidity wall detection. Works with OpenAlgo WebSocket for live Indian market data (NSE/NFO/BSE/MCX).
- **GitHub Stars**: 70
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<p align="center">
  <img src="screenshot.png" alt="OrderFlowMap Screenshot" width="900"/>
</p>

<h1 align="center">OrderFlowMap</h1>

<p align="center">
  <b>A Bookmap-style order flow visualization tool built entirely in the browser.</b><br>
  Real-time heatmaps · Trade bubbles · DOM ladder · Volume profile · CVD · Liquidity wall detection
</p>

<p align="center">
  <a href="https://azhagesan-dev.github.io/OrderFlowMap/"><img src="https://img.shields.io/badge/🚀_Live_Demo-Try_It_Now-blue?style=for-the-badge" alt="Live Demo"/></a>
  <a href="https://github.com/Azhagesan-dev/OrderFlowMap/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/></a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#live-demo">Live Demo</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#live-mode">Live Mode</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#keyboard-shortcuts">Shortcuts</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## What is OrderFlowMap?

**OrderFlowMap** is a **zero-dependency, single-file** order flow visualization tool inspired by [Bookmap](https://bookmap.com/). It renders a real-time heatmap of the order book depth alongside trade executions, giving you an institutional-grade view of market microstructure — all inside a single HTML file.

It works in two modes:

| Mode | Description |
|------|-------------|
| **Simulate** | Generates synthetic NIFTY futures data with realistic market dynamics including sweeps, icebergs, and regime shifts. Perfect for learning and experimentation. |
| **Live** | Connects to a self-hosted [OpenAlgo](https://github.com/marketcalls/openalgo) WebSocket server running on your machine to stream real market data from Indian exchanges (NSE, NFO, BSE, MCX, CDS). |

---

## Features

### 🔥 Order Book Heatmap
- Real-time L2 depth visualization with configurable intensity, gamma correction, and row height
- Four color schemes: **Bookmap** (bi-color bid/ask), **Mono**, **Inferno**, **Viridis**
- Per-tick bucketing ensures accurate price-level aggregation
- Interactive colorbar legend with HIGH/LOW indicators

### 🫧 Trade Bubbles
- Every trade is plotted as a circle at its exact price and time
- Bubble size scales with quantity (sqrt, log, or linear)
- Large trades get a glowing halo effect for instant visibility
- Small trades can be rendered as hollow circles to reduce visual noise
- Configurable thresholds for minimum trade size and "large" trade classification

### 📊 Overlays & Analytics
- **Best Bid/Ask lines** — real-time BBO tracking with color-coded series
- **Session VWAP** — volume-weighted average price tracked across the session
- **Volume Profile** — horizontal histogram anchored to the right edge with POC (Point of Control) highlighted
- **CVD (Cumulative Volume Delta)** — separate pane with baseline coloring (green above zero, red below)
- **Large-trade arrows** — marker arrows on the price chart for significant executions
- **Liquidity wall detection** — algorithmic identification of persistent, abnormally large resting orders with dashed-line annotations and labeled tags
- **Sweep flash alerts** — on-chart banner when aggressive sweeps are detected in simulation

### 📋 DOM Ladder
- 5-level depth-of-market ladder with bid/ask quantities, order counts, and proportional bars
- Spread row with real-time spread calculation
- Crosshair-linked price highlighting

### 🖨️ Time & Sales (Tape)
- Scrollable trade tape showing the last 80 prints
- Color-coded by side (buy/sell) with large-trade highlighting
- Tabular-nums font for aligned, scannable data

### 📈 Microstructure Stats
- Trades per second, average trade size
- Buy/Sell percentage split (60-second rolling window)
- 1-minute delta display in the header

### ⌨️ Presets & Keyboard Shortcuts
- One-click presets: **Scalper**, **Swing**, **HFT**, **Clean**
- Full keyboard control (see [Keyboard Shortcuts](#keyboard-shortcuts))

---

## Live Demo

### 👉 [**Try it live in your browser →**](https://azhagesan-dev.github.io/OrderFlowMap/)

No installation required — the simulation mode works instantly. Just open and explore.

Or run it locally:

```bash
# Clone the repo
git clone https://github.com/Azhagesan-dev/OrderFlowMap.git

# Open in browser
start OrderFlowMap/index.html        # Windows
open OrderFlowMap/index.html          # macOS
xdg-open OrderFlowMap/index.html      # Linux
```

The app starts in **Simulate** mode with 3 minutes of pre-seeded NIFTY data streaming at 4× speed.

---

## Quick Start

### Simulation Mode (Default)

1. Open `index.html` in your browser
2. The simulator auto-starts with synthetic NIFTY data at ~24,500
3. Use the left panel to tweak heatmap intensity, bubble sizes, and toggle overlays
4. Use the speed selector (top-right) to control simulation speed (1× to 20×)
5. Press **Space** to pause/resume, **F** to fit the chart

### Live Mode

1. Click **Live** in the Data Source panel
2. Enter your WebSocket URL (default: `ws://127.0.0.1:8765`)
3. Enter your [OpenAlgo](https://github.com/marketcalls/openalgo) API key
4. Set the symbol (e.g., `RELIANCE`, `NIFTY28APR26FUT`), exchange, and tick size
5. Click **⚡ Connect**

See [Live Mode Setup](#live-mode) for detailed instructions.

---

## Live Mode

### Prerequisites

OrderFlowMap connects to live market data through a **self-hosted WebSocket server**. You must run [OpenAlgo](https://github.com/marketcalls/openalgo) on your own machine — OrderFlowMap connects to this local endpoint and renders the incoming data.

> **Important:** OrderFlowMap is a pure front-end visualizer. It does **not** include a data server. You need to set up and run the OpenAlgo WebSocket server yourself.

### Setting Up OpenAlgo (WebSocket Server)

1. **Clone the OpenAlgo repository:**
   ```bash
   git clone https://github.com/marketcalls/openalgo.git
   cd openalgo
   ```

2. **Follow the OpenAlgo setup instructions** in their [README](https://github.com/marketcalls/openalgo#readme) to:
   - Install dependencies
   - Configure your broker credentials
   - Start the WebSocket server (default: `ws://127.0.0.1:8765`)

3. **Verify the server is running** — the OpenAlgo WebSocket server should be listening on port `8765`

4. **Open OrderFlowMap** → switch to **Live** mode → click **⚡ Connect**

### Connection Flow

```
Browser (OrderFlowMap)                        Your Machine
    │                                    ┌──────────────────────┐
    │  WebSocket (ws://127.0.0.1:8765)   │                      │
    └───────────────────────────────────► │  OpenAlgo Server     │
                                         │  (self-hosted)       │
                                         │       │              │
                                         │       │ Broker API   │
                                         │       ▼              │
                                         │  Exchange Data Feed  │
                                         │  (NSE/NFO/BSE/MCX)   │
                                         └──────────────────────┘
```

### WebSocket Protocol

**1. Authentication**
```json
{ "action": "authenticate", "api_key": "YOUR_API_KEY" }
```
Response:
```json
{ "message": "Authentication successful" }
```

**2. Subscribe**
```json
{
  "action": "subscribe",
  "symbol": "RELIANCE",
  "exchange": "NSE",
  "mode": 3,
  "depth": 5
}
```

**3. Market Data (incoming)**
```json
{
  "type": "market_data",
  "data": {
    "ltp": 2450.50,
    "volume": 1234567,
    "ltt": 1713345678000,
    "depth": {
      "buy": [
        { "price": 2450.45, "quantity": 500, "orders": 12 },
        ...
      ],
      "sell": [
        { "price": 2450.55, "quantity": 300, "orders": 8 },
        ...
      ]
    }
  }
}
```

### Trade Detection

Since the WebSocket feed provides snapshots (not individual trade prints), OrderFlowMap reconstructs trades using **volume delta analysis**:

1. Compare `volume` between consecutive ticks
2. If `volume` increased → a trade occurred with `qty = volumeDelta`
3. Side is inferred by comparing current `ltp` with previous `ltp`:
   - LTP went **up** → classified as a **buy** (aggressive buyer lifted the ask)
   - LTP went **down** → classified as a **sell** (aggressive seller hit the bid)
   - LTP **unchanged** → side carries forward from the previous trade

### Supported Exchanges

| Exchange | Code | Description |
|----------|------|-------------|
| NSE | `NSE` | National Stock Exchange (Equity) |
| NFO | `NFO` | NSE Futures & Options |
| BSE | `BSE` | Bombay Stock Exchange |
| BFO | `BFO` | BSE Futures & Options |
| MCX | `MCX` | Multi Commodity Exchange |
| CDS | `CDS` | Currency Derivatives |

### Tick Size Configuration

Set the correct tick size for your instrument:

| Instrument | Tick Size |
|------------|-----------|
| NIFTY / BANKNIFTY Futures | `0.05` |
| Equity (NSE) | `0.05` |
| NIFTY / BANKNIFTY Options | `0.05` |
| MCX Gold | `1.00` |
| MCX Crude Oil | `1.00` |

---

## Architecture

OrderFlowMap is a **single HTML file** (~1,700 lines) with no build tooling, no framework, and a single external dependency:

### Dependency

| Library | Version | Purpose |
|---------|---------|---------|
| [Lightweight Charts™](https://tradingview.github.io/lightweight-charts/) | v5.0.9 | High-performance financial charting (via CDN) |

### Internal Structure

```
index.html
├── <style>          — Complete CSS design system (~210 lines)
├── <body>           — HTML layout with header, 3-column grid, footer
└── <script>         — Application logic (~1,250 lines)
    ├── Config & State
    ├── Utilities (clamp, mix, rgba, roundTick, gauss)
    ├── Color Maps (bookmap, mono, inferno, viridis)
    ├── Chart Setup (Lightweight Charts v5 initialization)
    ├── Custom Primitives
    │   ├── HeatmapPrimitive — L2 depth rendering + volume profile
    │   ├── WallsPrimitive   — Liquidity wall detection & annotation
    │   └── BubblesPrimitive — Trade bubble rendering with halo effects
    ├── Simulator Engine
    │   ├── Regime model (drift, volatility, sweeps, icebergs)
    │   └── Synthetic order book & trade generation
    ├── Live WebSocket Client
    │   ├── OpenAlgo auth/subscribe protocol
    │   ├── Trade detection via volume delta
    │   └── Real-time VWAP computation
    ├── Renderers (DOM ladder, tape, colorbar, alerts)
    ├── UI Controls (range sliders, checkboxes, presets)
    └── Boot sequence (seed history → start loop)
```

### Custom Primitives (Lightweight Charts v5 API)

OrderFlowMap uses the [Custom Series Primitives API](https://tradingview.github.io/lightweight-charts/docs/plugins/custom_primitives) to render the heatmap, bubbles, and walls directly on the chart canvas:

| Primitive | Render Layer | Description |
|-----------|-------------|-------------|
| `HeatmapPrimitive` | `bottom` | Renders L2 depth as colored rectangles + volume profile bars |
| `WallsPrimitive` | `top` | Detects and draws liquidity walls with labels |
| `BubblesPrimitive` | `top` | Draws trade circles with size ∝ quantity |

### Data Model

| Array | Per-second | Fields |
|-------|-----------|--------|
| `bars[]` | ✅ | `time`, `mid`, `bbid`, `bask`, `vwap`, `_vN`, `_vD` |
| `depth[]` | ✅ | `time`, `bids[{p, q, o}]`, `asks[{p, q, o}]` |
| `cvdBars[]` | ✅ | `time`, `value` (running cumulative delta) |
| `trades[]` | Per-tick | `time`, `price`, `qty`, `side` |
| `tradeVolByPrice` | Map | `price → cumulative volume` (for volume profile) |

### Simulator

The built-in simulator generates realistic market dynamics:

- **Regime model**: drift, volatility, sweep events, and iceberg orders evolve over time
- **Order book**: 5 levels per side with Poisson-like quantity distributions
- **Trade generation**: side probability is influenced by imbalance, drift, and sweep direction
- **Fat-tail trade sizes**: log-normal distribution with occasional 3–8× multiplier spikes
- **Sweep events**: ~1.2% chance per tick, creating aggressive directional pressure for 8–30 ticks
- **Iceberg orders**: ~0.8% chance per tick, adding hidden refill liquidity at a specific level

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Space` | Play / Pause simulation |
| `F` | Fit chart to content |
| `H` | Toggle heatmap |
| `B` | Toggle trade bubbles |
| `V` | Toggle VWAP |
| `C` | Toggle CVD pane |

---

## Configuration Reference

### Heatmap Settings

| Setting | Range | Default | Description |
|---------|-------|---------|-------------|
| Intensity | 0.1 – 3.0 | 1.2 | Overall brightness multiplier for depth colors |
| Gamma | 0.3 – 2.5 | 0.65 | Non-linear contrast curve (lower = more contrast) |
| Row px | 2 – 14 | 5 | Pixel height of each price level row |
| Min qty | 0+ | 0 | Minimum quantity to render (noise filter) |
| Color | — | Bookmap | Color scheme selection |

### Bubble Settings

| Setting | Range | Default | Description |
|---------|-------|---------|-------------|
| Min px | 1 – 10 | 2 | Minimum bubble radius in pixels |
| Max px | 6 – 60 | 26 | Maximum bubble radius in pixels |
| Scale | — | Sqrt | Size scaling function (sqrt / log / linear) |
| Large ≥ | 1+ | 500 | Quantity threshold for "large trade" treatment |
| Min trade | 0+ | 0 | Minimum quantity to show any bubble |
| Hollow small | — | On | Render small trades as hollow circles |

### Presets

| Preset | Use Case | Key Settings |
|--------|----------|-------------|
| **Scalper** | Short-term intraday | High intensity, smaller large threshold (300) |
| **Swing** | Multi-hour holds | Lower intensity, bubbles off, high large threshold (1000) |
| **HFT** | Ultra-short frequency | Maximum intensity, big rows, walls/VP off |
| **Clean** | Minimal view | Heatmap/bubbles off, VP and CVD only |

---

## Browser Compatibility

OrderFlowMap requires a modern browser with ES2020+ support:

| Browser | Minimum Version |
|---------|----------------|
| Chrome / Edge | 88+ |
| Firefox | 85+ |
| Safari | 14+ |

> **Note**: The app uses Canvas 2D rendering via Lightweight Charts. WebGL is not required.

---

## Performance Notes

- **History window** is configurable (60s – 7200s, default 600s). Longer windows increase memory and CPU usage.
- **Heatmap rendering** iterates over all visible depth snapshots per frame. At 4× speed with 600s history, this is ~2,400 snapshots per frame.
- **Trade bubbles** cap iteration at the most recent 3,000 trades for performance.
- **DOM/Tape rendering** uses `innerHTML` batch updates for efficiency.
- **Auto-trimming** keeps all arrays bounded to the history window.

For best performance with large history windows (>1800s), use Chrome/Edge and a dedicated GPU.

---

## Roadmap

- [ ] Multi-symbol support with tabbed charts
- [ ] Recorded session playback (import/export JSON)
- [ ] Configurable depth levels (currently fixed at 5)
- [ ] WebSocket reconnection with backoff
- [ ] Additional data source adapters (Binance, Zerodha Kite)
- [ ] Dark/light theme toggle
- [ ] Snapshot export (PNG / SVG)

---

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [TradingView Lightweight Charts](https://tradingview.github.io/lightweight-charts/) — the high-performance charting library powering the visualization
- [Bookmap](https://bookmap.com/) — inspiration for the heatmap visualization concept
- [OpenAlgo](https://github.com/marketcalls/openalgo) by [@marketcalls](https://github.com/marketcalls) — self-hosted WebSocket server for Indian market data feeds

---

<p align="center">
  <sub>Built with ❤️ for the Indian trading community</sub>
</p>


==================================================


## [2/3] Repository: exchange-core (`PHASE4-QUANT-009`)
- **Full Name**: `PHASE4-QUANT-009_exchange-core__exchange-core`
- **Description**: Ultra-fast matching engine written in Java based on LMAX Disruptor, Eclipse Collections, Real Logic Agrona, OpenHFT, LZ4 Java, and Adaptive Radix Trees.
- **GitHub Stars**: 2627
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# exchange-core
[![Build Status](https://travis-ci.org/mzheravin/exchange-core.svg?branch=master)](https://travis-ci.org/mzheravin/exchange-core)
[![Javadocs](https://www.javadoc.io/badge/exchange.core2/exchange-core.svg)](https://www.javadoc.io/doc/exchange.core2/exchange-core)
[![Language grade: Java](https://img.shields.io/lgtm/grade/java/g/mzheravin/exchange-core.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mzheravin/exchange-core/context:java)
[![][license img]][license]

Exchange-core is an **open source market exchange core** based on 
[LMAX Disruptor](https://github.com/LMAX-Exchange/disruptor), 
[Eclipse Collections](https://www.eclipse.org/collections/) (ex. Goldman Sachs GS Collections), 
[Real Logic Agrona](https://github.com/real-logic/agrona),
[OpenHFT Chronicle-Wire](https://github.com/OpenHFT/Chronicle-Wire),
[LZ4 Java](https://github.com/lz4/lz4-java),
and [Adaptive Radix Trees](https://db.in.tum.de/~leis/papers/ART.pdf).

Exchange-core includes:
- orders matching engine
- risk control and accounting module
- disk journaling and snapshots module
- trading, admin and reports API

Designed for high scalability and pauseless 24/7 operation under high-load conditions and providing low-latency responses:
- 3M users having 10M accounts in total
- 100K order books (symbols) having 4M pending orders in total
- less than 1ms worst wire-to-wire target latency for 1M+ operations per second throughput
- 150ns per matching for large market orders

Single order book configuration is capable to process 5M operations per second on 10-years old hardware (Intel® Xeon® X5690) with moderate latency degradation:

|rate|50.0%|90.0%|95.0%|99.0%|99.9%|99.99%|worst|
|----|-----|-----|-----|-----|-----|------|-----|
|125K|0.6µs|0.9µs|1.0µs|1.4µs|4µs  |24µs  |41µs |
|250K|0.6µs|0.9µs|1.0µs|1.4µs|9µs  |27µs  |41µs |
|500K|0.6µs|0.9µs|1.0µs|1.6µs|14µs |29µs  |42µs |
|  1M|0.5µs|0.9µs|1.2µs|4µs  |22µs |31µs  |45µs |
|  2M|0.5µs|1.2µs|3.9µs|10µs |30µs |39µs  |60µs |
|  3M|0.7µs|3.6µs|6.2µs|15µs |36µs |45µs  |60µs |
|  4M|1.0µs|6.0µs|9µs  |25µs |45µs |55µs  |70µs |
|  5M|1.5µs|9.5µs|16µs |42µs |150µs|170µs |190µs|
|  6M|5µs  |30µs |45µs |300µs|500µs|520µs |540µs|
|  7M|60µs |1.3ms|1.5ms|1.8ms|1.9ms|1.9ms |1.9ms|

![Latencies HDR Histogram](hdr-histogram.png)

Benchmark configuration:
- Single symbol order book.
- 3,000,000 inbound messages are distributed as follows: 9% GTC orders, 3% IOC orders, 6% cancel commands, 82% move commands. About 6% of all messages are triggering one or more trades.
- 1,000 active user accounts.
- In average ~1,000 limit orders are active, placed in ~750 different price slots.
- Latency results are only for risk processing and orders matching. Other stuff like network interface latency, IPC, journaling is not included.
- Test data is not bursty, meaning constant interval between commands (0.2~8µs depending on target throughput).
- BBO prices are not changing significantly throughout the test. No avalanche orders.
- No coordinated omission effect for latency benchmark. Any processing delay affects measurements for next following messages.
- GC is triggered prior/after running every benchmark cycle (3,000,000 messages).
- RHEL 7.5, network-latency tuned-adm profile, dual X5690 6 cores 3.47GHz, one socket isolated and tickless, spectre/meltdown protection disabled.
- Java version 8u192, newer Java 8 versions can have a [performance bug](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=JDK-8221355)

### Features
- HFT optimized. Priority is a limit-order-move operation mean latency (currently ~0.5µs). Cancel operation takes ~0.7µs, placing new order ~1.0µs;
- In-memory working state for accounting data and order books.
- Event-sourcing - disk journaling and journal replay support, state snapshots (serialization) and restore operations, LZ4 compression.
- Lock-free and contention-free orders matching and risk control algorithms.
- No floating-point arithmetic, no loss of significance is possible.
- Matching engine and risk control operations are atomic and deterministic.
- Pipelined multi-core processing (based on LMAX Disruptor): each CPU core is responsible for certain processing stage, user accounts shard, or symbol order books shard.
- Two different risk processing modes (specified per symbol): direct-exchange and margin-trade.
- Maker/taker fees (defined in quote currency units).
- Two order books implementations: simple implementation ("Naive") and performance implementation ("Direct").
- Order types: Immediate-or-Cancel (IOC), Good-till-Cancel (GTC), Fill-or-Kill Budget (FOK-B)
- Testing - unit-tests, integration tests, stress tests, integrity/consistency tests.
- Low GC pressure, objects pooling, single ring-buffer.
- Threads affinity (requires JNA).
- User suspend/resume operation (reduces memory consumption).
- Core reports API (user balances, open interest).

### Installation
1. Install library into your Maven's local repository by running `mvn install`
2. Add the following Maven dependency to your project's `pom.xml`:
```
<dependency>
    <groupId>exchange.core2</groupId>
    <artifactId>exchange-core</artifactId>
    <version>0.5.3</version>
</dependency>
```

Alternatively, you can clone this repository and run the [example test](https://github.com/mzheravin/exchange-core/tree/master/src/test/java/exchange/core2/tests/examples/ITCoreExample.java).

### Usage examples
Create and start empty exchange core:
```java
// simple async events handler
SimpleEventsProcessor eventsProcessor = new SimpleEventsProcessor(new IEventsHandler() {
    @Override
    public void tradeEvent(TradeEvent tradeEvent) {
        System.out.println("Trade event: " + tradeEvent);
    }

    @Override
    public void reduceEvent(ReduceEvent reduceEvent) {
        System.out.println("Reduce event: " + reduceEvent);
    }

    @Override
    public void rejectEvent(RejectEvent rejectEvent) {
        System.out.println("Reject event: " + rejectEvent);
    }

    @Override
    public void commandResult(ApiCommandResult commandResult) {
        System.out.println("Command result: " + commandResult);
    }

    @Override
    public void orderBook(OrderBook orderBook) {
        System.out.println("OrderBook event: " + orderBook);
    }
});

// default exchange configuration
ExchangeConfiguration conf = ExchangeConfiguration.defaultBuilder().build();

// no serialization
Supplier<ISerializationProcessor> serializationProcessorFactory = () -> DummySerializationProcessor.INSTANCE;

// build exchange core
ExchangeCore exchangeCore = ExchangeCore.builder()
        .resultsConsumer(eventsProcessor)
        .serializationProcessorFactory(serializationProcessorFactory)
        .exchangeConfiguration(conf)
        .build();

// start up disruptor threads
exchangeCore.startup();

// get exchange API for publishing commands
ExchangeApi api = exchangeCore.getApi();
```

Create new symbol:
```java
// currency code constants
final int currencyCodeXbt = 11;
final int currencyCodeLtc = 15;

// symbol constants
final int symbolXbtLtc = 241;

// create symbol specification and publish it
CoreSymbolSpecification symbolSpecXbtLtc = CoreSymbolSpecification.builder()
        .symbolId(symbolXbtLtc)         // symbol id
        .type(SymbolType.CURRENCY_EXCHANGE_PAIR)
        .baseCurrency(currencyCodeXbt)    // base = satoshi (1E-8)
        .quoteCurrency(currencyCodeLtc)   // quote = litoshi (1E-8)
        .baseScaleK(1_000_000L) // 1 lot = 1M satoshi (0.01 BTC)
        .quoteScaleK(10_000L)   // 1 price step = 10K litoshi
        .takerFee(1900L)        // taker fee 1900 litoshi per 1 lot
        .makerFee(700L)         // maker fee 700 litoshi per 1 lot
        .build();

future = api.submitBinaryDataAsync(new BatchAddSymbolsCommand(symbolSpecXbtLtc));
```

Create new users:
```java
// create user uid=301
future = api.submitCommandAsync(ApiAddUser.builder()
        .uid(301L)
        .build());

// create user uid=302
future = api.submitCommandAsync(ApiAddUser.builder()
        .uid(302L)
        .build());
```

Perform deposits:
```java
// first user deposits 20 LTC
future = api.submitCommandAsync(ApiAdjustUserBalance.builder()
        .uid(301L)
        .currency(currencyCodeLtc)
        .amount(2_000_000_000L)
        .transactionId(1L)
        .build());

// second user deposits 0.10 BTC
future = api.submitCommandAsync(ApiAdjustUserBalance.builder()
        .uid(302L)
        .currency(currencyCodeXbt)
        .amount(10_000_000L)
        .transactionId(2L)
        .build());
```

Place orders:
```java
// first user places Good-till-Cancel Bid order
// he assumes BTCLTC exchange rate 154 LTC for 1 BTC
// bid price for 1 lot (0.01BTC) is 1.54 LTC => 1_5400_0000 litoshi => 10K * 15_400 (in price steps)
future = api.submitCommandAsync(ApiPlaceOrder.builder()
        .uid(301L)
        .orderId(5001L)
        .price(15_400L)
        .reservePrice(15_600L) // can move bid order up to the 1.56 LTC, without replacing it
        .size(12L) // order size is 12 lots
        .action(OrderAction.BID)
        .orderType(OrderType.GTC) // Good-till-Cancel
        .symbol(symbolXbtLtc)
        .build());

// second user places Immediate-or-Cancel Ask (Sell) order
// he assumes wost rate to sell 152.5 LTC for 1 BTC
future = api.submitCommandAsync(ApiPlaceOrder.builder()
        .uid(302L)
        .orderId(5002L)
        .price(15_250L)
        .size(10L) // order size is 10 lots
        .action(OrderAction.ASK)
        .orderType(OrderType.IOC) // Immediate-or-Cancel
        .symbol(symbolXbtLtc)
        .build());
```

Request order book:
```java
future = api.requestOrderBookAsync(symbolXbtLtc, 10);
```

GtC orders manipulations:
```java
// first user moves remaining order to price 1.53 LTC
future = api.submitCommandAsync(ApiMoveOrder.builder()
        .uid(301L)
        .orderId(5001L)
        .newPrice(15_300L)
        .symbol(symbolXbtLtc)
        .build());
        
// first user cancel remaining order
future = api.submitCommandAsync(ApiCancelOrder.builder()
        .uid(301L)
        .orderId(5001L)
        .symbol(symbolXbtLtc)
        .build());
```

Check user balance and GtC orders:
```java
Future<SingleUserReportResult> report = api.processReport(new SingleUserReportQuery(301), 0);
```

Check system balance:
```java
// check fees collected
Future<TotalCurrencyBalanceReportResult> totalsReport = api.processReport(new TotalCurrencyBalanceReportQuery(), 0);
System.out.println("LTC fees collected: " + totalsReport.get().getFees().get(currencyCodeLtc));
```

### Testing
- latency test: mvn -Dtest=PerfLatency#testLatencyMargin test
- throughput test: mvn -Dtest=PerfThroughput#testThroughputMargin test
- hiccups test: mvn -Dtest=PerfHiccups#testHiccups test
- serialization test: mvn -Dtest=PerfPersistence#testPersistenceMargin test

### TODOs
- market data feeds (full order log, L2 market data, BBO, trades)
- clearing and settlement
- reporting
- clustering
- FIX and REST API gateways
- cryptocurrency payment gateway
- more tests and benchmarks
- NUMA-aware and CPU layout custom configuration

### Contributing
Exchange-core is an open-source project and contributions are welcome!

### Support
- [Discussion group in Telegram (t.me/exchangecoretalks)](https://t.me/exchangecoretalks)
- [News channel in Telegram (t.me/exchangecore)](https://t.me/exchangecore)

[license]:LICENSE.txt
[license img]:https://img.shields.io/badge/License-Apache%202-blue.svg


==================================================


## [3/3] Repository: LOBFrame (`PHASE4-QUANT-020`)
- **Full Name**: `PHASE4-QUANT-020_FinancialComputingUCL__LOBFrame`
- **Description**: We release `LOBFrame', a novel, open-source code base which presents a renewed way to process large-scale Limit Order Book (LOB) data.
- **GitHub Stars**: 259
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# LOBFrame

We release `LOBFrame` (see the two papers [`Deep Limit Order Book Forecasting`](https://arxiv.org/abs/2403.09267) and [`HLOB - Information Persistence and Structure in Limit Order Books`](https://arxiv.org/abs/2405.18938)), a novel, open-source code base which presents a renewed way to process large-scale Limit Order Book (LOB) data. This framework integrates all the latest cutting-edge insights from scientific research (see [Lucchese et al.](https://www.sciencedirect.com/science/article/pii/S0169207024000062), [Prata et al.](https://arxiv.org/pdf/2308.01915.pdf)) into a cohesive system. Its strength lies in the comprehensive nature of the implemented pipeline, which includes the data transformation and processing stage, an ultra-fast implementation of the training, validation, and testing steps, as well as the evaluation of the quality of a model's outputs through trading simulations. Moreover, it offers flexibility by accommodating the integration of new models, ensuring adaptability to future advancements in the field.

## Introduction

In this tutorial, we show how to replicate the experiments presented in the two papers titled __"Deep Limit Order Book Forecasting: A microstructural guide"__ and __"HLOB - Information Persistence and Structure in Limit Order Books"__.

Before starting, please remember to **ALWAYS CITE OUR WORKS** as follows:

```
@article{briola2024deep,
  title={Deep Limit Order Book Forecasting},
  author={Briola, Antonio and Bartolucci, Silvia and Aste, Tomaso},
  journal={arXiv preprint arXiv:2403.09267},
  year={2024}
}
```

```
@misc{briola2024hlob,
      title={HLOB -- Information Persistence and Structure in Limit Order Books}, 
      author={Antonio Briola and Silvia Bartolucci and Tomaso Aste},
      year={2024},
      eprint={2405.18938},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR}
}
```

## Pre-requisites

Install the required packages:

```bash
pip3 install -r requirements.txt
```

If you are using a MacOS operating system, please proceed as follows:

```bash
pip3 install -r requirements_mac_os.txt
```

## Data
All the code in this repository exploits [LOBSTER](https://lobsterdata.com) data. To have an overview on their structure, please refer
to the official documentation available at the following [link](https://lobsterdata.com/info/DataStructure.php).

# Preliminary operations
Before starting any experiment:
- Open the ```lightning_batch_gd.py``` file and insert the [Weights & Biases](https://wandb.ai/site) project's name and API key (search for TODOs).
- Open the ```utils.py``` file and set the default values of the parameters.

## Usage
To start an experiment from scratch, you need to follow these steps:
- Place the raw data in the `data/nasdaq/raw` folder. The data must be in the LOBSTER format and each folder must be named with the asset's name (e.g. AAPL for Apple stock).
- Run the following command to pre-process data:
  ```bash
    python3 main --training_stocks "CSCO" --target_stocks "CSCO" --stages "data_processing"
  ```
- Run the following command to prepare the torch datasets (this allows to reduce the training time):
  ```bash
    python3 main --training_stocks "CSCO" --target_stocks "CSCO" --stages "torch_dataset_preparation" --prediction_horizon 10
  ```
  If you are interested also in performing the backtest stage, run the following command:
  ```bash
    python3 main --training_stocks "CSCO" --target_stocks "CSCO" --stages "torch_dataset_preparation,torch_dataset_preparation_backtest" --prediction_horizon 10
  ```
- If you are planning to use the HLOB model (see the paper titled [`HLOB - Structure and Persistence of Information in Limit Order Books`](https://arxiv.org/abs/2405.18938)), it is mandatory to execute the following command:
  ```bash
    python3 main --training_stocks "CSCO" --target_stocks "CSCO" --stages "complete_homological_structures_preparation"
  ```
- Run the following command to train the model:
  ```bash
    python3 main --training_stocks "CSCO" --target_stocks "CSCO" --stages "training"
  ```
  Currently available models are:
    - deeplob
    - transformer
    - itransformer
    - lobtransformer
    - dla
    - cnn1
    - cnn2
    - binbtabl
    - binctabl
    - axiallob
    - hlob
- Run the following command to evaluate the model:
  ```bash
    python3 main --training_stocks "CSCO" --target_stocks "CSCO" --experiment_id "<experiment_id_generated_in_the_training_stage>" --stages "evaluation"
  ```
- Run the following command to analyze the results:
  ```bash
    python3 main --training_stocks "CSCO" --target_stocks "CSCO" --experiment_id "<experiment_id_generated_in_the_training_stage>" --stages "backtest,post_trading_analysis"
  ```

Multiple (compatible) stages can be executed at the same time. Consider the following example:
```bash
python3 main --training_stocks "CSCO" --target_stocks "CSCO" --stages "data_processing,torch_dataset_preparation,torch_dataset_preparation_backtest,training,evaluation,backtest,post_trading_analysis"
```

Each experiment can be resumed and re-run by specifying its ID in the `experiment_id` parameter.

We now provide the typical structure of a folder before an experiment's run:

```bash
.
├── README.md
├── data
│   └── nasdaq
│        ├── raw_data
│             ├── <Stock1_Name>
│             └── <Stock1_Name>
│        ├── scaled_data
│             ├── test
│             ├── training
│             └── validation
│        └── unscaled_data
│             ├── test
│             ├── training
│             └── validation
├── data_processing
│   ├── data_process.py
│   └── data_process_utils.py
│   └── complete_homological_utils.py
├── loaders
│   └── custom_dataset.py
├── loggers
│   ├── logger.py
│   └── results
├── main.py
├── models
│   ├── AxialLob
│         └── axiallob.py
│   ├── CNN1
│         └── cnn1.py
│   ├── CNN2
│         └── cnn2.py
│   ├── DeepLob
│         └── deeplob.py
│   ├── DLA
│         └── DLA.py
│   ├── iTransformer
│         └── itransformer.py
│   ├── LobTransformer
│         └── lobtransformer.py
│   ├── TABL
│         ├── bin_nn.py
│         ├── bin_tabl.py
│         ├── bl_layer.py
│         └── tabl_layer.py
│   ├── Transformer
│         └── transformer.py
|   ├── CompleteHCNN
│         └── complete_hcnn.py
├── optimizers
│   ├── executor.py
│   └── lightning_batch_gd.py
├── requirements.txt
├── simulator
│   ├── market_sim.py
│   ├── post_trading_analysis.py
│   └── trading_agent.py
├── torch_datasets
│   └── threshold_1e-05
│       └── batch_size_32
│           └── 10
│               ├── test_dataset.pt
│               ├── test_dataset_backtest.pt
│               ├── training_dataset.pt
│               └── validation_dataset.pt
├── results
└── utils.py
```

# License

Copyright 2024 Antonio Briola, Silvia Bartolucci, Tomaso Aste.

Licensed under the CC BY-NC-ND 4.0 Licence (the "Licence"); you may not use this file except in compliance with the License. You may obtain a copy of the License at:

```
https://creativecommons.org/licenses/by-nc-nd/4.0/
```

Software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the provided link for the specific language governing permissions and limitations under the License.

### Core Implementation Code & Architecture
#### File: `models/TABL/bl_layer.py`
```python
import pytorch_lightning as pl
from torch import nn
import torch


class BL_layer(pl.LightningModule):
    def __init__(self, d2, d1, t1, t2):
        super().__init__()
        weight1 = torch.Tensor(d2, d1)
        self.W1 = nn.Parameter(weight1)
        nn.init.kaiming_uniform_(self.W1, nonlinearity='relu')

        weight2 = torch.Tensor(t1, t2)
        self.W2 = nn.Parameter(weight2)
        nn.init.kaiming_uniform_(self.W2, nonlinearity='relu')

        bias1 = torch.zeros((d2, t2))
        self.B = nn.Parameter(bias1)
        nn.init.constant_(self.B, 0)

        self.activation = nn.ReLU()

    def forward(self, x):

        x = self.activation(self.W1 @ x @ self.W2 + self.B)

        return x
```

#### File: `simulator/trading_agent.py`
```python
class Trading:
    def __init__(self, trading_hyperparameters):
        self.long_inventory = 0
        self.short_inventory = 0
        self.long_price = 0
        self.short_price = 0
        self.date_time_entry_long = None
        self.date_time_exit_long = None
        self.date_time_entry_short = None
        self.date_time_exit_short = None
        self.trading_history = []

    def long(self, price, datetime=None):
        amount = 1
        self.long_inventory += amount
        self.long_price = price
        self.date_time_entry_long = datetime

    def short(self, price, datetime=None):
        amount = 1
        self.short_inventory += amount
        self.short_price = price
        self.date_time_entry_short = datetime

    def exit_long(self, price, datetime=None):
        self.trading_history.append({'Type': 'Long', 'Entry_Long': self.date_time_entry_long, 'Price_Entry_Long': self.long_price,
                                     'Exit_Long': datetime, 'Price_Exit_Long': price})

        self.long_inventory = 0
        self.long_price = 0
        self.date_time_entry_long = None

    def exit_short(self, price, datetime=None):
        self.trading_history.append({'Type': 'Short', 'Entry_Short': self.date_time_entry_short, 'Price_Entry_Short': self.short_price,
                                     'Exit_Short': datetime, 'Price_Exit_Short': price})

        self.short_inventory = 0
        self.short_price = 0
        self.date_time_entry_short = None
```

#### File: `models/iTransformer/itransformer.py`
```python
import pytorch_lightning as pl
import torch
import torch.nn as nn


class ITransformer(pl.LightningModule):
    def __init__(
        self,
        lighten,
        dropout: float = 0.1,
        activation: str = "relu",
        norm_first: bool = False,
    ):
        super().__init__()
        self.name = "itransformer"
        if lighten:
            self.name += "-lighten"

        d_model = 64 if not lighten else 32
        dim_feedforward = 256 if not lighten else 128
        nhead = 8 if not lighten else 4
        num_layers = 2 if not lighten else 1

        self.embed = nn.Linear(100, d_model, bias=False)
        layer_norm_eps: float = 1e-5
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            activation=activation,
            layer_norm_eps=layer_norm_eps,
            norm_first=norm_first,
            batch_first=True,
        )
        encoder_norm = nn.LayerNorm(d_model, eps=layer_norm_eps)
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers, norm=encoder_norm
        )
        self.cat_head = nn.Linear(d_model, 3)

    def forward(self, x):
        x = x.squeeze(1)
        # transpose
        x = x.permute(0, 2, 1)
        x = self.embed(x)

        # transformer encoder
        x = self.transformer_encoder(x)

        # mean pool for classification
        x = torch.mean(x, dim=1)

        logits = self.cat_head(x)
        return logits
```

#### File: `models/DLA/DLA.py`
```python
import pytorch_lightning as pl
from torch import nn
import torch


class DLA(pl.LightningModule):
    def __init__(self, lighten, num_snapshots=100, hidden_size=128):
        super().__init__()
        self.name = "mlp"
        num_features = 40
        if lighten:
            self.name += "-lighten"
            num_features = 20

        self.W1 = nn.Linear(num_features, num_features, bias=False)

        self.softmax = nn.Softmax(dim=1)

        self.gru = nn.GRU(
            input_size=num_features,
            hidden_size=hidden_size,
            num_layers=2,
            batch_first=True,
            dropout=0.5
        )

        self.W2 = nn.Linear(hidden_size, hidden_size, bias=False)
        self.W3 = nn.Linear(num_snapshots*hidden_size, 3)

    def forward(self, x):
        # x.shape = [batch_size, num_snapshots, num_features]
        x = x.squeeze(1)

        X_tilde = self.W1(x)
        # alpha.shape = [batch_size, num_snapshots, num_features]

        alpha = self.softmax(X_tilde)
        # alpha.shape = [batch_size, num_snapshots, num_features]

        alpha = torch.mean(alpha, dim=2)
        # alpha.shape = [batch_size, num_snapshots]

        x_tilde = torch.einsum('ij,ijk->ijk', [alpha, x])
        # x_tilde.shape = [batch_size, num_snapshots, num_features]

        H, _ = self.gru(x_tilde)
        # o.shape = [batch_size, num_snapshots, hidden_size]

        H_tilde = self.W2(H)
        # o.shape = [batch_size, num_snapshots, hidden_size]

        beta = self.softmax(H_tilde)
        # o.shape = [batch_size, num_snapshots, hidden_size]

        beta = torch.mean(beta, dim=2)
        # beta.shape = [batch_size, num_snapshots]

        h_tilde = torch.einsum('ij,ijk->ijk', [beta, H])
        # h_tilde.shape = [batch_size, num_snapshots, hidden_size]

        h_tilde = torch.flatten(h_tilde, start_dim=1)
        # h_tilde.shape = [batch_size, hidden_size*num_snapshots]

        logits = self.W3(h_tilde)
        # out.shape = [batch_size, 3]

        return logits
```

#### File: `models/TABL/tabl_layer.py`
```python
import pytorch_lightning as pl
import torch
from torch import nn


class TABL_layer(pl.LightningModule):
    def __init__(self, d2, d1, t1, t2):
        super().__init__()
        self.t1 = t1

        weight = torch.Tensor(d2, d1)
        self.W1 = nn.Parameter(weight)
        nn.init.kaiming_uniform_(self.W1, nonlinearity='relu')

        weight2 = torch.Tensor(t1, t1)
        self.W = nn.Parameter(weight2)
        nn.init.constant_(self.W, 1 / t1)

        weight3 = torch.Tensor(t1, t2)
        self.W2 = nn.Parameter(weight3)
        nn.init.kaiming_uniform_(self.W2, nonlinearity='relu')

        bias1 = torch.Tensor(d2, t2)
        self.B = nn.Parameter(bias1)
        nn.init.constant_(self.B, 0)

        l = torch.Tensor(1, )
        self.l = nn.Parameter(l)
        nn.init.constant_(self.l, 0.5)

        self.activation = nn.ReLU()

    def forward(self, X):

        # maintaining the weight parameter between 0 and 1.
        if (self.l[0] < 0):
            l = torch.Tensor(1, )
            self.l = nn.Parameter(l)
            nn.init.constant_(self.l, 0.0)

        if (self.l[0] > 1):
            l = torch.Tensor(1, )
            self.l = nn.Parameter(l)
            nn.init.constant_(self.l, 1.0)

        # modelling the dependence along the first mode of X while keeping the temporal order intact (7)
        X = self.W1 @ X

        # enforcing constant (1) on the diagonal
        W = self.W - self.W * torch.eye(self.t1, dtype=torch.float32, device="cuda") + torch.eye(self.t1, dtype=torch.float32, device="cuda") / self.t1

        # attention, the aim of the second step is to learn how important the temporal instances are to each other (8)
        E = X @ W

        # computing the attention mask  (9)
        A = torch.softmax(E, dim=-1)

        # applying a soft attention mechanism  (10)
        # he attention mask A obtained from the third step is used to zero out the effect of unimportant elements
        X = self.l[0] * (X) + (1.0 - self.l[0]) * X * A

        # the final step of the proposed layer estimates the temporal mapping W2, after the bias shift (11)
        y = X @ self.W2 + self.B
        return y
```

#### File: `models/CNN1/cnn1.py`
```python
import pytorch_lightning as pl
from torch import nn


class CNN1(pl.LightningModule):
    def __init__(self, num_features=40, num_classes=3, temp=26):
        super().__init__()

        # Convolution 1
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=(4, num_features), padding=(3, 0), dilation=(2, 1))
        self.relu1 = nn.LeakyReLU()

        # Convolution 2
        self.conv2 = nn.Conv1d(in_channels=16, out_channels=16, kernel_size=(4,))
        self.relu2 = nn.LeakyReLU()

        # Max pool 1
        self.maxpool1 = nn.MaxPool1d(kernel_size=2)

        # Convolution 3
        self.conv3 = nn.Conv1d(in_channels=16, out_channels=32, kernel_size=(3,), padding=2)
        self.relu3 = nn.LeakyReLU()

        # Convolution 4
        self.conv4 = nn.Conv1d(in_channels=32, out_channels=32, kernel_size=(3,), padding=2)
        self.relu4 = nn.LeakyReLU()

        # Max pool 2
        self.maxpool2 = nn.MaxPool1d(kernel_size=2)

        # Fully connected 1
        self.fc1 = nn.Linear(temp*32, 32)
        self.relu5 = nn.LeakyReLU()

        # Fully connected 2
        self.fc2 = nn.Linear(32, num_classes)

    def forward(self, x):
        # Convolution 1
        out = self.conv1(x)
        out = self.relu1(out)
        out = out.reshape(out.shape[0], out.shape[1], -1)
        # print('After convolution1:', out.shape)

        # Convolution 2
        out = self.conv2(out)
        out = self.relu2(out)
        # print('After convolution2:', out.shape)

        # Max pool 1
        out = self.maxpool1(out)
        # print('After maxpool1:', out.shape)

        # Convolution 3
        out = self.conv3(out)
        out = self.relu3(out)
        # print('After convolution3:', out.shape)

        # Convolution 4
        out = self.conv4(out)
        out = self.relu4(out)
        # print('After convolution4:', out.shape)

        # Max pool 2
        out = self.maxpool2(out)
        # print('After maxcpool2:', out.shape)

        # flatten
        out = out.view(out.size(0), -1)
        # print('After flatten:', out.shape)

        # Linear function 1
        out = self.fc1(out)
        out = self.relu5(out)
        # print('After linear1:', out.shape)

        # Linear function (readout)
        out = self.fc2(out)
        # print('After linear2:', out.shape)

        return out
```


==================================================
