# ⚡ [QUANT-SOURCE-206] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_206_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: matching-engine (`PHASE4-QUANT-044`)
- **Full Name**: `PHASE4-QUANT-044_AsthaMishra__matching-engine`
- **Description**: From-scratch limit order book + matching engine in Rust. ~100 ns book ops replaying 104M operations from real NASDAQ ITCH 5.0 data; 143-fill sweeps in 2 µs. Binary OUCH order entry, 10 µs order-to-ack.
- **GitHub Stars**: 47
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Rust Matching Engine

A from-scratch limit-order-book **matching engine** with a NASDAQ **OUCH/ITCH-style binary gateway**, in Rust. Built to learn low-latency systems design from first principles.

> **On the numbers:** every figure below is labeled with *exactly what it measures and how*. The nanosecond figures are **isolated, in-process microbenchmarks of the order book** - one component, no network, no protocol. They are **not** order-to-ack system latency. The end-to-end number (order entry → ack, including the OUCH codec + TCP) is reported separately and is **microseconds, not nanoseconds**. See [Measurement scope](#measurement-scope).

---

## Layout

Four layered crates - dependencies point downward only (`core ← runtime ← adapters ← binary`):

| Crate | Role | README |
|---|---|---|
| [`matching-core`](matching-core/) | Pure engine: order book, matching, types. No threads, async, or I/O. | [↗](matching-core/README.md) |
| [`matching-engine`](matching-engine/) | Runtime: sharded worker threads, lock-free routing, response slot pool. | [↗](matching-engine/README.md) |
| [`ouch-gateway`](ouch-gateway/) | OUCH/ITCH binary protocol: TCP sessions, codec, order-to-ack latency harness. | [↗](ouch-gateway/README.md) |
| [`rest-gateway`](rest-gateway/) | REST adapter (Axum) - convenience/queries only, **not** the low-latency path. | [↗](rest-gateway/README.md) |
| [`server`](server/) | Binary entry point - wires engine + gateways together. | [↗](server/README.md) |

```
TCP (OUCH binary) ──► ouch-gateway ──► matching-engine (sharded workers) ──► matching-core (OrderBook)
                                            ▲ lock-free channel + slot pool ▲
HTTP (REST, queries) ─► rest-gateway ───────┘
```

**Threading model:** each symbol's book is single-threaded (one owner, no locks inside a book); symbols are *sharded* across a fixed worker pool (`symbol_id % num_workers`), e.g. 100 symbols over 8 workers ≈ 12–13 symbols/worker. It is **not** a thread-per-symbol design.

## Quickstart

```bash
cargo build --release

# Terminal 1 - server (OUCH binary OE on 127.0.0.1:8080)
cargo run --release -p server

# Terminal 2 - load test (1M orders, order-to-ack latency over loopback)
cargo run --release -p ouch-gateway --bin load_client -- 1000000

cargo test            # unit + property tests
cargo bench           # Criterion microbenchmarks (matching-core)
```

## Measurement scope

Three different things are measured three different ways. **Don't compare them to each other.**

| Measurement | What it covers | Excludes | How it's measured | Result |
|---|---|---|---|---|
| **Order book op** | A single book operation in isolation | Network, protocol, threading, syscalls | Criterion (synthetic), warm cache, in-process, book allocated outside the timer | **51 ns** top-of-book match · **58 ns** cancel at depth-1000 · **0.90 ns** BBO · ~30M warm inserts/s |
| **ITCH replay** | Book reacting to a real trading day | Same as above (book only) | `Instant` around each op, 104.6M ops / top-100 symbols | p50 **99 ns**, p99 502 ns, **~5.9M ops/s** (book management; 96% deletes, 0 trades) |
| **Matching path** | Large marketable orders sweeping a deep book | Same as above (book only) | `Instant` per op, 1M synthetic ops, 731k executions | sweep of ~143 fills in **2.0 µs** (~14 ns/fill) |
| **Order-to-ack** | OUCH Enter → Accept, codec + TCP included | - | Client `hdrhistogram`, **loopback**, single session, 1M orders | p50 **10.4 µs** · p99 **19.6 µs** · pipelined **2.0M orders/s** |

Caveats, stated plainly:
- The order-to-ack number is **localhost loopback with software timestamps** - not external/hardware wire-to-wire. A real NIC + switch path would add latency; this is the floor, not a production figure.
- The load generator is **closed-loop** (one order in flight, blocking on each ack), so those are service-time percentiles and the tail is understated by construction. Not offered-load percentiles.
- ITCH Add messages are passive resting quotes (0 trades), so the replay measures **book management** (insert/cancel/modify), not matching throughput. Matching is measured separately by `synthetic_replay` and the Criterion benches.
- Order-book microbenchmarks allocate the book **outside** the measured window. Earlier revisions did not, which inflated every figure 4–15× and made runs vary by up to 2.4×; see [benchmark methodology](matching-core/README.md#benchmark-methodology).
- `Instant` resolution here is ~100 ns, so per-op percentile tables are quantised at that granularity. The BBO figure is the only genuinely sub-nanosecond measurement, and it comes from Criterion's sampling rather than wall-clock timing.
- Everything runs on **x86-64 WSL2**, whose VM scheduler injects 100 µs–ms pauses; the p99.9/max tail is partly environmental, not code.

> A matching engine lives exchange-side; the point of this project is the data-structure and systems work, not a claim of HFT-grade end-to-end latency.

## Stack

Rust 2024 · Tokio · Axum · crossbeam-channel / -queue · Criterion · proptest · cargo-fuzz · hdrhistogram

### Core Implementation Code & Architecture
#### File: `matching-core/src/error.rs`
```python
pub enum Error {
    
}
```

#### File: `matching-engine/src/client/mod.rs`
```python
pub mod order;
pub use order::*;
```

#### File: `ouch-gateway/src/types/mod.rs`
```python
pub mod session;
pub use session::*;
```

#### File: `matching-core/src/types/mod.rs`
```python
pub mod order;
pub use order::*;

pub mod trade;
pub use trade::*;
```

#### File: `ouch-gateway/src/codec/mod.rs`
```python
pub mod inbound;
pub use inbound::*;

pub mod outbound;
pub use outbound::*;

pub mod types;
pub use types::*;
```

#### File: `Cargo.toml`
```python
[workspace]
members = ["matching-core",
    "matching-engine",
    "ouch-gateway", "rest-gateway",
    "server",
]
resolver = "2"
```


==================================================


## [2/3] Repository: mercury (`PHASE4-QUANT-045`)
- **Full Name**: `PHASE4-QUANT-045_eelixir__mercury`
- **Description**: High-performance C++ matching engine with unified market simulation, live market data streaming, and a browser-based dashboard
- **GitHub Stars**: 41
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# <img src="https://github.com/user-attachments/assets/7ee41ddf-cf24-42fb-953b-d44c55e9f352" width="400">

> Market-making and order-book simulation lab built around a high-performance C++ matching engine, custom intrusive order-book core, instant backtests, real-time WebSocket streaming, and bounded agent-based microstructure dynamics.

## Overview

Mercury is a local market-making and order-book simulation lab. Its core is a full limit order book with price-time priority matching, wrapped by a unified runtime where manual browser orders, replayed flow, built-in agents, instant backtests, and live real-time simulation all trade through the same engine thread.

The intended use case is experimentation: compare liquidity-provision settings, stress order-flow regimes, inspect queue and P&L behavior, and produce repeatable backtest artifacts without connecting to a live broker or venue.

**Key Metrics:**
- **3.2M+ orders/sec** sustained throughput
- **~320 ns** average order insertion latency
- **O(1)** order lookup, insertion, and cancellation
- **249** backend tests, all passing
- **Nanosecond** gateway-to-engine latency instrumentation

## Features

- **Order Types:** Limit, Market, Cancel, Modify
- **Time-in-Force:** GTC (Good-til-Canceled), IOC (Immediate-or-Cancel), FOK (Fill-or-Kill)
- **Price-Time Priority:** FIFO matching at each price level
- **Self-Trade Prevention:** Client ID based filtering
- **Risk Management:** Pre-trade risk checks with position/exposure limits
- **P&L Tracking:** Realized and unrealized P&L with FIFO cost basis
- **Unified Market Runtime:** One runtime for manual orders, replay, built-in agents, instant backtests, and live real-time simulation
- **Browser Lab Runner:** Start instant backtests, headless runs, sweeps, and replay calibration from the Lab tab or `/api/lab/run`
- **Backtest Artifacts:** Local JSON/CSV output for run summary, config, trades, stats, P&L, simulation state, agent attribution, and queue analytics
- **Parameter Sweeps:** JSON-driven batch runner for comparing market-maker counts, volatility presets, seeds, flow mixes, P&L, drawdown, and fill quality
- **Scenario Presets:** Versioned JSON scenarios for calm books, toxic flow, thin-book stress, high-cancel churn, and momentum bursts
- **Market-Maker Tuning:** Runtime and file-driven controls for quote levels, spread, size, wake interval, toxicity sensitivity, and inventory skew
- **Replay Calibration:** Replay CSV calibration reports comparing target order mix and quantity profile with observed simulated output
- **Built-In Agents:** Passive market maker, aggressive momentum trader, mean-reversion bot, Poisson-flow noise trader
- **Advanced Microstructure:** Queue-position-aware agents, deeper multi-level market-maker quoting, and toxicity-driven spread widening
- **Regime Manager:** Auto-detected `calm`/`normal`/`stressed` regimes with explicit Poisson lambda controls for limit, cancel, and marketable arrival rates, plus Pareto order-size dispersion for whale-vs-retail flow
- **Live Server:** HTTP order entry + dual WebSocket market data (JSON and binary)
- **React Dashboard:** Real-time ladder, trade tape, mid-price chart, order entry, P&L, simulation controls, system health
- **Latency Telemetry:** Nanosecond-precision tracking from gateway entry through engine to publication
- **Throughput Monitoring:** Messages-per-second counter broadcast to the dashboard
- **Bounded Volatility Presets:** `low`, `normal`, and `high` widen spread and increase activity without runaway 100% to 1000% price jumps in seconds
- **Binary Protocol:** Packed wire-format structs for high-throughput market data consumers

## Architecture

```text
+------------------------------------------------------------------------------+
|                              React Dashboard                                 |
|  Order Entry | PnL | Sim Controls | Ladder | Tape | Chart | System Health    |
|                    Zustand Store <- WebSocket <- /ws/market                  |
+-----------------------------------+------------------------------------------+
                                    | HTTP POST /api/orders
+-----------------------------------v------------------------------------------+
|                             OrderEntryGateway                                |
|              JSON parse -> latency stamp -> MarketRuntime::submitOrder()     |
+-----------------------------------+------------------------------------------+
                                    |
+-----------------------------------v------------------------------------------+
|                               MarketRuntime                                  |
|  Simulation loop | Environment | Agent registry | Replay | Runtime fanout     |
|  manual orders + replay + built-in agents -> shared submission path          |
+-----------------------------------+------------------------------------------+
                                    |
+-----------------------------------v------------------------------------------+
|                               EngineService                                  |
|   Engine thread (single writer) | PnL tracker | stats | sequencing           |
+-----------------------------------+------------------------------------------+
                                    |
+-----------------------------------v------------------------------------------+
|                              MatchingEngine                                  |
|      Validation -> Matching -> Book mutations -> trade/execution callbacks   |
+-----------------------------------+------------------------------------------+
                                    |
+-----------------------------------v------------------------------------------+
|                            MarketDataPublisher                               |
|       JSON /ws/market                     Binary /ws/market/bin              |
+------------------------------------------------------------------------------+
```

### Core Data Structures

The core book keeps intrusive FIFO queues inside each price level while using `absl::btree_map` for sorted bid/ask ladders and an Abseil-backed `HashMap` wrapper for O(1) average order lookup.

| Component | Purpose | Complexity |
|-----------|---------|------------|
| **HashMap** | Abseil-backed `flat_hash_map` wrapper for order lookup | O(1) avg |
| **btree_map ladders** | Sorted bid/ask price ladders with cache-friendly traversal | O(log N) level ops |
| **IntrusiveList** | Order queue at each price level | O(1) insert/remove |
| **ObjectPool** | Pre-allocated order nodes | O(1) alloc/free |
| **PriceLevel** | Orders + cached aggregate quantity | O(1) quantity query |
| **ThreadPool** | Task scheduling for parallel work | O(1) submit |

### Server Components

| Component | Purpose |
|-----------|---------|
| **MarketRuntime** | Simulation loop, environment state, built-in agents, replay coordination, runtime fanout |
| **EngineService** | Engine thread serialization, sequencing, P&L, latency/MPS telemetry |
| **OrderEntryGateway** | HTTP POST parsing, latency stamping, sync runtime roundtrip |
| **MarketDataPublisher** | JSON + binary WebSocket broadcast via uWS loop defer |
| **ServerApp** | HTTP/WS route registration, lifecycle management |
| **BinaryProtocol** | Packed `#pragma pack(push,1)` structs for wire-efficient streaming |

## Dashboard

The React frontend (`/frontend`) provides a real-time market-operations interface:

| Panel | Description |
|-------|-------------|
| **Top Bar** | Symbol, mid-price, spread, connection badge, runtime status |
| **Stats Strip** | Bid, ask, mid, spread, trades, volume, orders, levels |
| **Order Entry** | Limit/market/cancel/modify with buy/sell toggle, price, qty, TIF |
| **PnL Card** | Net position plus total/realized/unrealized P&L marked live to the current mid |
| **Simulation Controls** | Pause/resume, restart, clock speed, replay, volatility/regime, scenarios, agent counts, market-maker tuning |
| **Lab View** | Run instant/headless backtests, sweeps, and replay calibration, or import saved artifacts for P&L, inventory, mid/spread, toxicity, queue metrics, and agent attribution |
| **System Health** | Engine latency, throughput, connection state |
| **Mid-Price Chart** | Lightweight-charts 1s candlestick view with zoom/pan |
| **Order Book Ladder** | L2 depth, asks above and bids below |
| **Trade Tape** | Time and sales with self-trade highlighting |
| **Status Bar** | WS state, active client, trade count, volume, levels, timezone |

## Project Structure

```text
mercury/
|-- include/                    # Headers
|   |-- Order.h                 # Order, Trade, ExecutionResult types
|   |-- OrderBook.h             # Order book with Abseil ladders + intrusive FIFO levels
|   |-- MatchingEngine.h        # Price-time priority matching
|   |-- EngineService.h         # Live engine thread + telemetry
|   |-- MarketRuntime.h         # Unified simulation/runtime layer
|   |-- MarketData.h            # Market-data DTOs and sink interfaces
|   |-- BacktestReport.h        # Backtest summary and artifact writers
|   |-- BacktestRunner.h        # Shared CLI/server lab runner
|   |-- MarketDataPublisher.h   # JSON + binary WebSocket publisher
|   |-- OrderEntryGateway.h     # HTTP order entry handler
|   |-- BinaryProtocol.h        # Packed binary wire-format structs
|   |-- ServerApp.h             # Server entrypoint
|   `-- ...
|-- src/                        # Implementations
|   |-- MatchingEngine.cpp
|   |-- EngineService.cpp
|   |-- MarketRuntime.cpp
|   |-- BacktestRunner.cpp
|   |-- OrderEntryGateway.cpp
|   |-- MarketDataPublisher.cpp
|   |-- ServerApp.cpp
|   `-- main.cpp
|-- scenarios/                  # Versioned market-making lab scenarios
|-- tests/                      # Google Test suites (249 tests)
|-- benchmarks/                 # Optional benchmark target
|-- frontend/                   # React/Vite/TypeScript dashboard
|-- data/                       # Sample CSV inputs
|-- docs/                       # ARCHITECTURE.md, WORKFLOWS.md
`-- AGENTS.md                   # Agent guidance
```

## Quick Start

### Build

```powershell
cmake -B build -G Ninja
cmake --build build
```

The backend pulls third-party dependencies with CMake `FetchContent`, including Abseil for the ladder and lookup containers.

### Run The Live Stack

Terminal 1 - backend:
```powershell
.\build\mercury.exe --server --sim --host 127.0.0.1 --port 9001 --symbol SIM
```

Terminal 2 - frontend:
```powershell
Set-Location frontend
npm install
npm run dev
```

Open `http://127.0.0.1:5173`. Vite proxies `/api` and `/ws` to the backend.

### Run With Replay

```powershell
.\build\mercury.exe --server --sim --host 127.0.0.1 --port 9001 --symbol SIM --replay data\sample_orders_with_clients.csv --replay-speed 10
```

### Run Headless Accelerated Simulation

```powershell
.\build\mercury.exe --sim --headless --sim-speed 25 --sim-seed 42 --sim-duration-ms 30000 --sim-volatility normal
```

### Run An Instant Backtest

```powershell
.\build\mercury.exe --backtest --sim-seed 42 --sim-duration-ms 30000 --sim-volatility normal --backtest-output runs\baseline
```

Artifacts include `summary.json`, `config.json`, `trades.csv`, `stats.csv`, `pnl.csv`, `sim_state.csv`, `agent_metrics.csv`, and `agent_summary.csv`.

Run a preset scenario:

```powershell
.\build\mercury.exe --backtest --scenario scenarios\toxic-flow.json --backtest-output runs\toxic-flow
```

Run with a market-maker config file:

```powershell
.\build\mercury.exe --backtest --mm-config scenarios\calm-two-sided-market.json --backtest-output runs\custom-mm
```

Calibrate against replay flow:

```powershell
.\build\mercury.exe --calibrate-replay data\sample_orders_with_clients.csv --backtest-output runs\replay-calibration
```

### Run A Parameter Sweep

Create a sweep file:

```json
{
  "runs": [
    { "name": "baseline", "seed": 42, "volatility": "normal", "marketMakerCount": 2, "noiseTraderCount": 1 },
    { "name": "stressed-flow", "seed": 42, "volatility": "high", "marketMakerCount": 3, "noiseTraderCount": 4 }
  ]
}
```

Run the sweep as instant backtests:

```powershell
.\build\mercury.exe --sweep runs\sweep.json --sim-duration-ms 30000 --backtest-output runs\sweep
```

## HTTP API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Server liveness and runtime status |
| `/api/state` | GET | Engine metadata, market summary, and simulation state |
| `/api/scenarios` | GET | Built-in live scenario IDs and display names |
| `/api/orders` | POST | Submit order (limit, market, cancel, modify) |
| `/api/simulation/control` | POST | Pause/resume/restart, change timing, volatility/regime, scenarios, agent counts, market-maker quoting |
| `/api/replay/control` | POST | Start or stop local CSV replay against the running simulator |
| `/api/lab/run` | POST | Run instant/headless backtests, sweeps, or replay calibration and return renderable artifacts |

Example order submission:

```json
{
  "type": "limit",
  "side": "buy",
  "price": 101,
  "quantity": 10,
  "clientId": 1,
  "tif": "GTC"
}
```

Simulation control example:

```json
{
  "action": "set_volatility",
  "volatility": "high"
}
```

Accelerate or return the live simulator clock to realtime:

```json
{
  "action": "set_timing",
  "clockMode": "accelerated",
  "speed": 25
}
```

Force a specific market regime (`calm`, `normal`, or `stressed`):

```json
{
  "action": "set_regime",
  "volatility": "stressed"
}
```

Start local replay flow from the browser or API:

```json
{
  "action": "start",
  "replayFile": "data\\sample_orders_with_clients.csv",
  "speed": 10,
  "loop": false,
  "loopPauseMs": 1000
}
```

Run an instant lab backtest from the browser or API:

```json
{
  "mode": "backtest",
  "name": "ui-baseline",
  "symbol": "SIM",
  "scenarioFile": "scenarios\\calm-two-sided-market.json",
  "durationMs": 30000,
  "seed": 42,
  "volatility": "normal",
  "marketMakerCount": 2,
  "momentumCount": 2,
  "meanReversionCount": 2,
  "noiseTraderCount": 1,
  "outputDir": "runs\\ui-baseline"
}
```

`mode` can be `backtest`, `headless`, `sweep`, or `calibrate_replay`. The response includes summary JSON and chart/table-ready artifacts; when `outputDir` is supplied, the normal local JSON/CSV files are written as well.

Apply a built-in live scenario:

```json
{
  "action": "apply_scenario",
  "scenario": "toxic-flow"
}
```

Tune the simulated market-maker population and quote shape:

```json
{
  "action": "set_market_maker",
  "marketMaker": {
    "levels": 4,
    "quoteQuantity": 90,
    "minQuantity": 20,
    "baseSpreadTicks": 3,
    "toxicitySensitivity": 1.2,
    "wakeIntervalMs": 80
  }
}
```

## WebSocket API

| Path | Format | Snapshot | Events |
|------|--------|----------|--------|
| `/ws/market` | JSON text | Yes, on connect | `book_delta`, `trade`, `execution`, `stats`, `pnl`, `sim_state`, `agent_metrics` |
| `/ws/market/bin` | Binary packed | No | `book_delta`, `trade` |

### Envelope Shape (JSON)

```json
{
  "type": "book_delta",
  "sequence": 42,
  "symbol": "SIM",
  "payload": {
    "side": "buy",
    "price": 100,
    "quantity": 5,
    "orderCount": 1
  }
}
```

### Telemetry Fields

| Field | Location | Description |
|-------|----------|-------------|
| `engineLatencyNs` | `book_delta`, `trade` payloads | Gateway-to-engine latency in nanoseconds |
| `messagesPerSecond` | `stats` payload | Engine-thread throughput sampled every ~1 second |

### Simulation State

`/api/state` and `sim_state` frames expose:

- running and paused state
- clock mode and speed multiplier
- current volatility preset
- simulation timestamp
- market-maker, momentum, mean-reversion, and noise-trader agent counts
- realized volatility and average spread summaries
- toxicity score, measuring recent sweep-like flow versus displayed top-book liquidity
- current market regime (`calm`, `normal`, `stressed`) and the active Poisson arrival intensities (`limitLambda`, `cancelLambda`, `marketableLambda`), all expressed as expected events per millisecond
- live market-maker configuration and latest agent attribution metrics

### Binary Protocol

Messages on `/ws/market/bin` use packed structs from `include/BinaryProtocol.h`:

| Struct | Size | Header Type |
|--------|------|-------------|
| `BinaryBookDelta` | 61 bytes | `1` |
| `BinaryTradeEvent` | 85 bytes | `2` |

All fields are little-endian (x86/x64 host order).

## Other Runtime Modes

### File Processing

```powershell
.\build\mercury.exe data\sample_orders_with_clients.csv trades.csv executions.csv riskevents.csv pnl.csv
.\build\mercury.exe data\sample_orders_with_clients.csv --concurrent --async-io
```

### CLI Flags

| Flag | Short | Description |
|------|-------|-------------|
| `--server` | `-S` | Start HTTP/WebSocket server |
| `--sim` | | Enable the living market simulation runtime |
| `--headless` | | Run the same simulation runtime without the browser server |
| `--backtest` | | Run headless simulation as fast as possible |
| `--backtest-output <dir>` | | Write backtest summary/config/trade/stat/PnL/simulation-state artifacts |
| `--sweep <file>` | | Run multiple instant backtests from a JSON sweep file |
| `--scenario <file>` | | Apply a scenario JSON file to server, headless, backtest, or sweep base settings |
| `--mm-config <file>` | | Apply market-maker quote configuration from JSON |
| `--calibrate-replay <file>` | | Run instant replay calibration and write `calibration.json` when output is enabled |
| `--host <addr>` | | Bind address (default `127.0.0.1`) |
| `--port <port>` | `-p` | Listen port (default `9001`) |
| `--symbol <name>` | | Comma-separated list of symbols (default `SIM`) |
| `--replay <file>` | | CSV replay file |
| `--replay-speed <x>` | | Replay speed multiplier |
| `--replay-loop` | | Loop the replay file continuously |
| `--replay-loop-pause <ms>` | | Pause between replay loops |
| `--sim-speed <x>` | | Simulation clock speed multiplier |
| `--sim-seed <n>` | | Deterministic simulation seed |
| `--sim-volatility <low\|normal\|high>` | | Volatility preset |
| `--mm-count <n>` | | Passive market-maker count |
| `--mom-count <n>` | | Aggressive momentum-agent count |
| `--mr-count <n>` | | Mean-reversion-agent count |
| `--noise-count <n>` | | Poisson-flow noise-trader count |
| `--sim-duration-ms <n>` | | Bounded headless run duration in simulated milliseconds |

## Performance

Benchmarks run on 12-core CPU @ 3.6GHz (Release build):

| Operation | Latency | Throughput |
|-----------|---------|------------|
| Order Insert | 321 ns | 3.1M/sec |
| Order Match (10 levels) | 1.9 us | 526K/sec |
| Order Cancel | 2.7 us | 370K/sec |
| Market Sweep (5 levels) | 1.8 us | 556K/sec |
| **Sustained Mixed Load** | 312 ns | **3.2M/sec** |

```powershell
cmake -B build -DMERCURY_BUILD_BENCHMARKS=ON -DCMAKE_BUILD_TYPE=Release -G Ninja
cmake --build build
.\build\mercury_benchmarks.exe
```

## Testing

249 unit tests covering:
- Order book operations (insert, remove, update)
- Matching engine (limit, market, IOC, FOK)
- Risk manager (position limits, exposure limits)
- P&L tracker (realized, unrealized, FIFO cost basis)
- Market data (sequencing, snapshots, deltas)
- Server/API contract smoke tests for state JSON, order parsing, order responses, and WebSocket envelopes
- Unified simulation runtime and agent fanout
- Instant backtest clock behavior without real-time pacing
- Backtest report metrics, agent attribution, queue analytics, Lab API JSON artifacts, and CSV escaping
- Bounded volatility excursion and long-run two-sided book maintenance
- Trading strategies and legacy migration coverage
- Concurrency (thread pool, async writers)
- Stress tests (100K+ orders, deep books)
- Core data structures and container behavior

```powershell
# Backend
ctest --test-dir build --output-on-failure

# Frontend
Set-Location frontend
npm run test:run
npm run build
```

## Future Updates

Mercury's current release is focused on local, repeatable market-making simulation. Good next steps are:

- [ ] Add optional broker or paper-trading adapters while keeping the simulator usable without external accounts.
- [ ] Add authentication, multi-user permissions, and deployment hardening for non-localhost operation.
- [ ] Add durable run storage so backtests, sweeps, calibration reports, and agent attribution can be queried across sessions.
- [ ] Package the dashboard for production use, including an option to serve the built React app from the C++ server.
- [ ] Add Python strategy loading or an external strategy sandbox with explicit safety and performance boundaries.
- [ ] Extend the binary WebSocket protocol beyond book deltas and trades if low-latency consumers need full event parity.
- [ ] Add richer scenario authoring tools for stress testing quote behavior, toxic flow, queue priority, and inventory limits.
- [ ] Add deeper replay calibration reports that compare simulated fill quality, spread capture, and adverse selection against target datasets.

## License

AGPL-3.0

### Core Implementation Code & Architecture
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

#### File: `frontend/components.json`
```python
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/index.css",
    "baseColor": "slate",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

#### File: `src/OrderBook.cpp`
```python
/**
 * @file OrderBook.cpp
 * @brief OrderBook implementation (now header-only)
 * 
 * The OrderBook is now implemented as a header-only class in OrderBook.h
 * to take advantage of template inlining and reduce function call overhead.
 * 
 * This file is kept for backwards compatibility with the build system.
 */

#include "OrderBook.h"

// All implementation is now in the header file for better inlining
// and template instantiation.

namespace Mercury {
    // Empty - implementation is header-only
}
```

#### File: `frontend/tsconfig.node.json`
```python
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "es2023",
    "lib": ["ES2023"],
    "module": "esnext",
    "types": ["node"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["vite.config.ts"]
}
```

#### File: `scenarios/high-cancel-rate.json`
```python
{
  "name": "high-cancel-rate",
  "description": "Noisy order flow with frequent cancels to test book churn and queue decay.",
  "symbols": ["SIM"],
  "simulation": {
    "seed": 168,
    "volatility": "normal",
    "durationMs": 30000,
    "marketMakerCount": 3,
    "momentumCount": 1,
    "meanReversionCount": 2,
    "noiseTraderCount": 5,
    "stepMs": 50,
    "publishIntervalMs": 250
  },
  "marketMaker": {
    "levels": 3,
    "quoteQuantity": 90,
    "minQuantity": 20,
    "baseSpreadTicks": 3,
    "toxicitySensitivity": 1.1,
    "wakeIntervalMs": 80,
    "inventorySkewDivisor": 50
  }
}
```

#### File: `scenarios/toxic-flow.json`
```python
{
  "name": "toxic-flow",
  "description": "High marketable flow and momentum pressure to test adverse selection and spread widening.",
  "symbols": ["SIM"],
  "simulation": {
    "seed": 84,
    "volatility": "high",
    "durationMs": 30000,
    "marketMakerCount": 2,
    "momentumCount": 4,
    "meanReversionCount": 1,
    "noiseTraderCount": 4,
    "stepMs": 50,
    "publishIntervalMs": 250
  },
  "marketMaker": {
    "levels": 4,
    "quoteQuantity": 80,
    "minQuantity": 15,
    "baseSpreadTicks": 5,
    "toxicitySensitivity": 1.8,
    "wakeIntervalMs": 70,
    "inventorySkewDivisor": 45
  }
}
```


==================================================


## [3/3] Repository: orderbook-imbalance-indicator-hft (`PHASE4-QUANT-051`)
- **Full Name**: `PHASE4-QUANT-051_leionion__orderbook-imbalance-indicator-hft`
- **Description**: A high-frequency tool that monitors the "Bid-Ask" spread and order book depth to predict the next 10-second price move.
- **GitHub Stars**: 19
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Orderbook Imbalance Indicator HFT

A Python project for short-horizon market microstructure signals from L2 order book depth.

This implementation is built from the "future version" direction: configurable signal pipeline, replay mode, local orderbook reconstruction, spread guard, refill detection, JSONL output, optional webhook fan-out, and automated tests.

## What Is Implemented

- Local orderbook engine with snapshot + delta handling.
- Weighted depth imbalance feature extraction.
- Bid/ask spread normalization and 10-second horizon signal scoring.
- Signal suppression controls:
  - Spread guard.
  - Refill detection penalty.
  - Minimum confidence threshold.
- Replay-driven paper mode for deterministic local testing.
- Outputs:
  - Console JSON events.
  - JSONL file sink.
  - Optional webhook POST.
- Test suite for orderbook math, signal behavior, and runner integration.

## Project Structure

```text
.
├── main.py
├── config.example.yaml
├── requirements.txt
├── data/
│   └── replay_book_events.jsonl
├── hft_indicator/
│   ├── config.py
│   ├── feed.py
│   ├── features.py
│   ├── io.py
│   ├── orderbook.py
│   ├── runner.py
│   └── signal_engine.py
└── tests/
    ├── test_orderbook.py
    ├── test_runner.py
    └── test_signal_engine.py
```

## Signal Model

At each book update:

1. Reconstruct current L2 state.
2. Compute weighted bid and ask depth over `depth_levels`.
3. Compute imbalance:

```python
imbalance = (weighted_bid - weighted_ask) / max(weighted_bid + weighted_ask, 1e-9)
```

4. Normalize by spread (bps) to produce pressure score.
5. Map score to direction: `up`, `down`, or `flat`.
6. Apply suppression logic (spread guard, refill, confidence floor).
7. Emit `microstructure.signal` or `signal.blocked`.

## Quick Start

### 1) Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### 2) Configure

```bash
cp config.example.yaml config.yaml
```

Default config is ready for local replay mode.

### 3) Run (paper mode)

```bash
python3 main.py --config config.yaml --mode paper
```

### 4) Run tests

```bash
python3 -m pytest -q
```

## Configuration Reference

`config.yaml` sections:

- `feed`
  - `venue`: label for source venue.
  - `symbol`: market symbol.
  - `depth_levels`: top N levels used in features.
  - `heartbeat_timeout_ms`: reserved control for feed health checks.
  - `replay_file`: JSONL event source.
  - `tick_interval_ms`: replay pacing.
- `signal`
  - `horizon_sec`: forecast horizon metadata (default 10).
  - `imbalance_method`: currently `weighted_l2`.
  - `min_confidence`: suppress weak signals.
  - `spread_guard_bps`: block during wide spreads.
  - `refill_penalty`: enable refill suppression.
  - `refill_window`: sample window for refill detector.
  - `refill_threshold`: trigger multiplier for refill detection.
- `output`
  - `console`: print JSON events.
  - `jsonl_path`: append output path.
  - `webhook_url`: optional POST target.
  - `mode`: expected `paper`.

## Replay Event Format

Snapshot event:

```json
{"type":"snapshot","bids":[[100.0,10.0]],"asks":[[100.5,9.0]]}
```

Delta event:

```json
{"type":"delta","side":"bid","price":100.0,"size":11.5}
```

`side` must be `bid` or `ask`. A `size <= 0` removes the level.

## Current vs Planned

The old "initial version" is intentionally superseded.

### Current (Implemented)

- Single-symbol replay-to-signal pipeline.
- Weighted L2 imbalance scoring.
- Spread guard and refill-aware suppression.
- JSONL + webhook publishing path.
- Unit/integration tests.

### Next Improvements

- Live WebSocket adapters for exchange-native feeds.
- Multi-symbol scheduling.
- Regime-aware adaptive thresholds.
- Latency instrumentation and per-stage timing metrics.
- Optional lightweight monitoring dashboard.

## Risk Notice

This software is for research and engineering workflows. It is not financial advice. Always validate on paper/replay first, then harden feed quality checks, risk limits, and deployment controls before any production trading.

## Contact

- GitHub: [@leionion](https://github.com/leionion)

### Core Implementation Code & Architecture
#### File: `hft_indicator/__init__.py`
```python
"""Orderbook Imbalance Indicator HFT package."""

__all__ = [
    "config",
    "orderbook",
    "features",
    "signal_engine",
    "runner",
]
```

#### File: `hft_indicator/feed.py`
```python
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Iterator

from hft_indicator.config import FeedConfig


def replay_events(config: FeedConfig) -> Iterator[dict]:
    path = Path(config.replay_file)
    if not path.exists():
        raise FileNotFoundError(f"Replay file not found: {path}")

    with path.open("r", encoding="utf-8") as fp:
        for line in fp:
            row = line.strip()
            if not row:
                continue
            event = json.loads(row)
            yield event
            time.sleep(config.tick_interval_ms / 1000.0)
```

#### File: `tests/test_orderbook.py`
```python
from hft_indicator.orderbook import OrderBook


def test_spread_and_mid() -> None:
    book = OrderBook(symbol="BTCUSDT")
    book.apply_snapshot(
        bids=[[100.0, 10.0], [99.5, 8.0]],
        asks=[[100.5, 9.0], [101.0, 8.0]],
    )
    assert book.best_bid() == 100.0
    assert book.best_ask() == 100.5
    assert book.mid_price() == 100.25
    assert round(book.spread_bps() or 0, 4) == 49.8753


def test_delta_removes_level() -> None:
    book = OrderBook(symbol="BTCUSDT")
    book.apply_snapshot(bids=[[100.0, 10.0]], asks=[[100.5, 9.0]])
    book.apply_delta("bid", 100.0, 0.0)
    assert book.best_bid() is None
```

#### File: `main.py`
```python
from __future__ import annotations

import argparse
import sys

from hft_indicator.config import load_config
from hft_indicator.runner import AppRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Orderbook Imbalance Indicator HFT")
    parser.add_argument("--config", required=True, help="Path to YAML config")
    parser.add_argument("--mode", default="paper", choices=["paper"], help="Execution mode")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_config(args.config)
    runner = AppRunner(config)
    emitted = runner.run_replay()
    print(f"completed mode={args.mode} emitted_signals={emitted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

#### File: `hft_indicator/io.py`
```python
from __future__ import annotations

import json
from pathlib import Path

import requests

from hft_indicator.config import OutputConfig


class SignalSink:
    def __init__(self, config: OutputConfig) -> None:
        self.config = config
        self.jsonl_path = Path(config.jsonl_path)
        self.jsonl_path.parent.mkdir(parents=True, exist_ok=True)

    def publish(self, payload: dict) -> None:
        if self.config.console:
            print(json.dumps(payload, separators=(",", ":")))

        with self.jsonl_path.open("a", encoding="utf-8") as fp:
            fp.write(json.dumps(payload) + "\n")

        if self.config.webhook_url:
            try:
                requests.post(self.config.webhook_url, json=payload, timeout=0.5)
            except requests.RequestException:
                # Webhook failures should not stop signal generation in paper mode.
                pass
```

#### File: `tests/test_runner.py`
```python
from pathlib import Path

from hft_indicator.config import FeedConfig, OutputConfig, SignalConfig, AppConfig
from hft_indicator.runner import AppRunner


def test_runner_emits_signals(tmp_path: Path) -> None:
    replay_file = tmp_path / "events.jsonl"
    replay_file.write_text(
        "\n".join(
            [
                '{"type":"snapshot","bids":[[100.0,10.0]],"asks":[[100.5,9.0]]}',
                '{"type":"delta","side":"bid","price":100.0,"size":11.0}',
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    out_file = tmp_path / "signals.jsonl"
    cfg = AppConfig(
        feed=FeedConfig(replay_file=str(replay_file), tick_interval_ms=0),
        signal=SignalConfig(min_confidence=0.0, refill_penalty=False, spread_guard_bps=99.0),
        output=OutputConfig(console=False, jsonl_path=str(out_file), webhook_url="", mode="paper"),
    )
    emitted = AppRunner(cfg).run_replay()
    assert emitted >= 1
    assert out_file.exists()
    assert len(out_file.read_text(encoding="utf-8").strip().splitlines()) == emitted
```


==================================================
