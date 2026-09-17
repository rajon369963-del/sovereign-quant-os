# ⚡ [QUANT-SOURCE-212] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_212_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: MicroExchange (`PHASE4-QUANT-104`)
- **Full Name**: `PHASE4-QUANT-104_Leotaby__MicroExchange`
- **Description**: Exchange-grade CLOB matching engine + microstructure analytics in C++20
- **GitHub Stars**: 67
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# MicroExchange

[![CI](https://github.com/Leotaby/MicroExchange/actions/workflows/ci.yml/badge.svg)](https://github.com/Leotaby/MicroExchange/actions/workflows/ci.yml)
![C++20](https://img.shields.io/badge/C%2B%2B-20-blue.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)

**Exchange-grade CLOB matching engine + ITCH-style market data replay + microstructure analytics in modern C++20.**

> **[📊 Live Interactive Dashboard](https://Leotaby.github.io/MicroExchange/)** — 3D order book surface, Kyle's lambda landscape, spread decomposition, stylized facts.

A complete market microstructure laboratory: from order entry to trade print, from raw event feeds to empirical spread decomposition, built with the rigor of production exchange systems and the analytical depth of graduate-level financial economics.

### Visualizations

**3D Limit Order Book Surface** - Bid (blue) and ask (red) depth across price levels over time:

![Order Book Surface](docs/images/orderbook_3d.png)

**3D Price Impact Surface** - Kyle's lambda: impact increases with volume (concave, square-root law) and amplifies with directional imbalance:

![Price Impact Surface](docs/images/impact_surface_3d.png)

**Spread Decomposition** - Effective spread split into realized spread (MM revenue) and price impact. *Real large-caps run ~50–70% adverse selection; this zero-intelligence sim produces ≈0 (uninformed flow → no permanent impact) - see [reproducible results](#sample-results).*

![Spread Decomposition](docs/images/spread_decomposition.png)

**Stylized Facts** - Return distribution vs Gaussian and the autocorrelation of |returns|. *Reproduced on 1s bars: volatility clustering AC(\|r\|,1) ≈ 0.24; fat tails are mild (excess kurtosis ≈ 1.2) under zero-intelligence flow - see [reproducible results](#sample-results).*

![Stylized Facts](docs/images/stylized_facts.png)

---

## Architecture

```
  order sources                  matching core                      outputs
  ─────────────                  ─────────────                      ───────

  ┌──────────────┐
  │ TCP Gateway  │─┐   binary order-entry protocol over a socket (net/)
  └──────────────┘ │
  ┌──────────────┐ │   ┌─────────────────────────────┐    ┌──────────────────┐
  │ Simulation   │ ├──▶│      Matching Engine        │──▶ │ Market Data Feed │
  │ (Hawkes/ZI)  │ │   │ price-time priority (FIFO)  │    │ (ITCH-style:     │
  └──────────────┘ │   │ Limit/Market/IOC/FOK/Stop   │    │ incremental +    │
  ┌──────────────┐ │   │                             │    │ snapshots)       │
  │ ITCH Replay  │─┘   │ book backends (same API):   │    └──────────────────┘
  │ (historical) │     │  • OrderBook     (std::map) │    ┌──────────────────┐
  └──────────────┘     │  • ArrayOrderBook (array +  │──▶ │ Analytics        │
                       │     bitmap BBO index)       │    │ spread decomp,   │
                       └──────────────────────-──────┘    │ Kyle's λ, OFI,   │
                                                          │ stylized facts   │
                                                          └──────────────────┘
```

---

## Visualizations

> **[→ Interactive 3D charts (GitHub Pages)](https://Leotaby.github.io/MicroExchange/docs/visualizations.html)**

### 3D Order Book Surface — Depth × Price × Time
Bid side (blue) and ask side (red) form the characteristic valley around the midpoint. Depth clusters at key levels and shifts with the price drift.

![Order Book 3D](docs/images/orderbook_3d.png)

### 3D Price Impact Surface — Kyle's λ Landscape
Price impact as a function of trade volume and order flow imbalance. The concave shape demonstrates the square-root law of impact (Bouchaud et al., 2018) - larger trades have diminishing marginal impact, amplified by directional imbalance.

![Impact 3D](docs/images/impact_3d.png)

### Spread Decomposition — Huang-Stoll (1997)
Effective spread decomposed into realized spread (market maker revenue) and price impact. In liquid equities adverse selection is ~50-70%; under zero-intelligence flow it collapses to ≈0 (no informed trading), consistent with Kyle's λ ≈ 0. Reproducing realistic adverse selection requires informed agents (see Known Issues / future work).

![Spread Decomposition](docs/images/spread_decomposition.png)

### Stylized Facts: Fat Tails & Volatility Clustering
Left: return distribution vs Gaussian - heavy tails from Hawkes-driven clustering. Right: autocorrelation of |returns| showing slow decay characteristic of ARCH effects.

![Stylized Facts](docs/images/stylized_facts.png)

---

## Order Types

| Type | TIF | Behaviour |
|---|---|---|
| **Limit** | GTC / DAY | Rests on the book at `price`. |
| **Market** | IOC | Crosses the book at any price; unfilled remainder cancelled. |
| **IOC** | IOC | Limit semantics; remainder after the first match is cancelled. |
| **FOK** | FOK | Pre-checked for full fill; if not, never enters the book. |
| **Stop** | - | Parked until `last_trade_price` crosses `stop_price`, then released as Market. |
| **StopLimit** | - | Parked until trigger; released as Limit at `price`. |

Stops are stored in dedicated per-side multimaps keyed by trigger price.
Every aggressive cycle that updates the last print runs a guarded
`check_stop_triggers()` pass — releases are themselves matched immediately,
which can cascade into more triggers without recursing on the call stack.

## Microstructure Concepts Implemented

| Domain | Concept | Implementation |
|--------|---------|---------------|
| **Market Structure** | Price-time priority (FIFO) | `core/OrderBook` with deterministic sequencing |
| **Market Structure** | Queue position tracking | Per-level FIFO queues with sequence numbers |
| **Liquidity** | Quoted spread | Real-time BBO tracking in `analytics/SpreadAnalyzer` |
| **Liquidity** | Effective spread | Trade-midpoint deviation analysis |
| **Liquidity** | Depth & resilience | Post-trade book recovery metrics |
| **Price Formation** | Realized spread | 5-second post-trade midpoint reversion |
| **Price Formation** | Price impact (permanent) | Effective − Realized spread decomposition |
| **Information** | Order flow imbalance (OFI) | Signed volume aggregation → return prediction |
| **Information** | Kyle's λ | Regression: ΔP = λ · signed_volume + ε |
| **Adverse Selection** | Glosten-Milgrom intuition | Spread widens with information asymmetry in simulation |
| **Inventory** | Ho-Stoll / Avellaneda-Stoikov | Quote skewing under inventory risk in MM agent |
| **Stylized Facts** | Fat tails, vol clustering | Hawkes arrival process + empirical verification |
| **Stylized Facts** | Spread under stress | Endogenous widening with order imbalance |

---

## What Makes This Different

Most GitHub "matching engines" are toy implementations — a sorted map, a match loop, and a README. This project bridges **three disciplines**:

1. **Systems engineering** - Lock-free queues, arena allocation, cache-aligned structures, deterministic replay, property-based invariant testing
2. **Financial economics** - Spread decomposition, adverse selection models, information-based trading theory (Glosten-Milgrom, Kyle, Ho-Stoll)
3. **Quantitative research** - Reproducible empirical analysis, stylized fact generation, microstructure model calibration

---

## Known Issues & Limitations

- **No informed traders → adverse selection ≈ 0**: Agents are zero-intelligence, so order flow carries no private information. Both the Huang-Stoll decomposition (price impact ≈ 0) and Kyle's λ (R² ≈ 0.01) correctly report this. It is a *modeling* limitation, not a bug - reproducing realistic adverse selection (~50–70% of the spread) requires a Glosten-Milgrom-style informed-trader population. Tracked as future work.

- **Fat tails are mild**: on 1s bars the ZI midprice is contained (a ~15-tick range over the hour), so excess kurtosis is ~1.2 — present but below intraday equities. Deep tails need informed/trending flow or a fundamental-value process.

- **Arena allocator never frees**: Orders accumulate in the arena for the lifetime of the process. Fine for simulation (it exits) but would need periodic cleanup or epoch-based reclamation for production.

- **No proper order tracking per agent**: The cancellation logic in the simulator is approximate — agents don't track their own outstanding orders, so cancel rates are estimates.

- **No iceberg / hidden-quantity orders yet.** Refilling visible slices interacts with FIFO priority in a non-obvious way; tracked in `CHANGELOG.md` as future work.

- **Visualization PNGs predate v1.2.0**: the 3D surface images above are illustrative and were rendered before the analytics fixes below; the authoritative, reproducible numbers live in [`output/report.txt`](output/report.txt). Regenerating the figures from current output is tracked as future work.

### Resolved in v1.2.0
- ~~Volatility clustering is weak (AC\|r\| ≈ 0.02)~~ — was a sampling artifact. Returns are now computed on fixed 1-second bars as log returns instead of per-event on the integer-tick mid; **AC(|r|, lag 1) = 0.24**, inside the empirical 0.15–0.40 range.
- ~~Excess kurtosis is a spurious 78~~ — same root cause (a return series that was ≈99% exact zeros). Time-bar log returns give a realistic **1.16**.
- ~~Spread decomposition doesn't satisfy `effective = realized + impact`~~ — the price-impact term was averaged in absolute value while realized was signed. Now consistently signed, so the identity holds and the adverse-selection % is meaningful.

### Resolved in v1.1.0
- ~~FeedPublisher overwrites OrderBook callbacks~~ — fixed by a multi-subscriber listener fan-out on `OrderBook`. The publisher is now re-enabled in `main.cpp` and reports message counts in the per-run report.
- ~~Kyle's lambda R² is near zero because of event-index bucketing~~ — the regression now uses Hawkes wall-clock timestamps for both trades and midprices. (R² is still low because ZI flow is uninformed — see above — but the bucketing is no longer the bottleneck.)

---

## Build

Requires C++20 and CMake 3.20+.

```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

Or without CMake:
```bash
g++ -std=c++20 -O2 -I core/include -I md/include -I sim/include -I analytics/include \
    src/main.cpp -o build/micro_exchange
```

### Run Simulation
```bash
# Default 1-hour Hawkes simulation → match → analytics → output/
./bin/micro_exchange

# Custom duration (seconds), symbol, and output directory
./bin/micro_exchange --duration 7200 --symbol AAPL --output output

# Verbose
./bin/micro_exchange -v
```
> Binary feed replay is implemented at the library level (`md/FeedReplayer`,
> via `FeedPublisher::dump_to_file`) but is not yet wired to the CLI — tracked
> as future work alongside real NASDAQ ITCH ingestion.

### Run Tests & Benchmarks
```bash
# Full CTest suite (invariants + fuzz + end-to-end smoke run)
cd build && ctest --output-on-failure

# Or invoke binaries directly
./bin/test_invariants            # Property-based + fuzz + stop-order tests
./bin/bench_throughput           # Single-thread matching throughput
./bin/bench_latency              # Latency histogram (p50/p90/p95/p99/p99.9)
./bin/bench_latency --ops 5000000   # ...with a longer run
```

---

## Sample Results

### Throughput & Latency
```
Single-thread matching throughput: 2.24M orders/sec (1M order run)
Mean latency:     598 ns
P50 latency:      213 ns
P90 latency:      460 ns
P95 latency:      543 ns
P99 latency:      716 ns
P99.9 latency:  1,033 ns
```
*(Throughput/latency are hardware-dependent — numbers above are from the committed `output/benchmark_results.txt`. The analytics below are deterministic and identical on any machine.)*

### Order book: `std::map` vs tick-indexed array

The engine ships **two** order-book implementations behind identical matching
semantics: the default `OrderBook` (two `std::map`s) and `ArrayOrderBook`, a
contiguous tick-indexed array with a **bitmap occupied-index** (hardware
`ctz`/`clz` bit-scan for the best-bid/ask cursors). `bench_orderbook_compare`
runs the same order stream through both, asserts the trade streams are
**byte-identical**, then compares performance (1M orders, ~9900–10100 band):

```
Correctness:  identical trade stream on every run  ✓  (CI-gated equivalence test)

Performance (1M orders; hardware-dependent - example below is Apple M-series)
                    std::map       array (bitmap)
  Throughput        ~7.9 M/s        ~9.6 M/s        → ~1.2x
  Latency  P50      84 ns           83 ns
  Latency  P99      292 ns          250 ns          → lower tail
```

Two takeaways that matter more than a single headline number:

1. **Where the win lands depends on the CPU.** On Apple Silicon the array is
   ~1.2× higher throughput with a lower tail; on the x86 CI sandbox throughput
   is ~even but median latency drops ~33% (84 ns vs 125 ns). Either way the
   array is competitive-or-faster — and the ceiling is set by the per-order
   `OrderId→Order*` hash insert and the `now()` timestamp, *not* the level
   container. **v1.5.0 acts on exactly this:** capturing the timestamp once per
   order instead of once per fill raised both books ~28–30% on x86 (`std::map`
   5.9M→7.6M/s, array 6.7M→8.8M/s); the `OrderId` hash insert is now the
   dominant remaining per-order cost.
2. **A flat array needs an index.** A naive linear best-bid/ask scan is ~25×
   *slower* than `std::map` on a wide/sparse book because it walks empty levels;
   the bitmap occupied-index fixes that and keeps the array ≥1.0× through
   realistic band widths. Extreme sparsity (200k levels) still favours a
   two-level summary bitmap — tracked as future work.

Run it yourself: `./bin/bench_orderbook_compare`.

### Networked order entry (TCP gateway)

The order books are in-process; a real exchange sits behind a network front-end.
`net/OrderGateway` is a single-threaded TCP gateway that accepts a client
connection, decodes a compact **binary order-entry protocol**
(`net/OrderEntryProtocol.h` — length-prefixed framing; `NewOrder`/`Cancel` in,
`Exec`/`Ack` out), feeds the `MatchingEngine`, and streams execution reports
back. It mirrors the standard exchange model: one sequential gateway in front of
a single-threaded, deterministic matching core.

The end-to-end test (`test_gateway`, CI-gated) starts the server on an ephemeral
port, streams 3,000 orders over a real loopback socket, and asserts the
networked path produces **exactly the same trades and volume** as the in-process
engine — serialising orders over TCP changes nothing about the match.

One low-latency networking detail worth calling out: both ends set
**`TCP_NODELAY`**. A lock-step order-entry protocol sends tiny messages, and
leaving Nagle's algorithm on (the default) collides with delayed-ACKs to add
~40 ms per round trip — a real bug this project hit during development and fixed.

Run it yourself: `./bin/test_gateway`.

### Spread Decomposition (1 hr simulated AAPL — deterministic)
```
590,168 orders → 209,905 trades

Metric                  Value (ticks)
─────────────────────────────────────
Quoted spread            1.06
Effective spread         0.77
Realized spread          0.83
Price impact            -0.06
Adverse selection %     -7.5%
```
The decomposition satisfies the Huang-Stoll identity `effective = realized + impact`
(0.77 = 0.83 + (−0.06)). The **negative** price impact is the economically correct
result for this market: agents are zero-intelligence, so order flow carries no
information and prices mean-revert after trades rather than trending — i.e.
adverse selection ≈ 0. Real large-cap equities run ~50–70% because real flow is
partly informed; reproducing that requires informed agents (see Known Issues).

### Kyle's λ (5-second buckets)
```
lambda:   1.64e-05 ticks/share   (t-stat 3.1)
R²:       0.01                    (N = 719 intervals)
```
Order flow explains ~1% of price variation — again the expected signature of
uninformed flow, and **consistent** with the ≈0 adverse selection above.

### Stylized Facts (1-second bars, log returns)
```
Excess kurtosis:    1.16  (benchmark: > 0)        ✓  mild fat tails
AC(|r|, lag=1):     0.24  (benchmark: 0.15-0.40)  ✓  volatility clustering
AC(|r|, lag=5):     0.06  (benchmark: > 0)        ✓
AC(|r|, lag=10):    0.04  (benchmark: > 0)        ✓
```
Volatility clustering (AC|r| ≈ 0.24) is now squarely in the empirical range — the
Hawkes self-exciting arrivals generate it, but the effect was previously hidden by
sampling returns per-event on the integer-tick mid (≈99% exact zeros), which had
inflated excess kurtosis to a spurious 78. Sampling on fixed time bars with log
returns is the standard methodology (Cont, 2001) and gives the honest picture:
strong clustering, mild fat tails (deep tails would need informed/trending flow).

---

## Design Decisions

- **Intrusive doubly-linked list for price levels** — O(1) insert/remove at known position; avoids `std::map` overhead and heap fragmentation
- **Arena allocator for Order objects** - Pre-allocated slab; zero malloc on the hot path; deterministic deallocation
- **SPSC lock-free ring buffer for MD feed** - Single-producer/single-consumer between matching thread and feed handler; no mutex contention
- **Compile-time order type dispatch** - `if constexpr` eliminates branch misprediction for known order types
- **Tick-indexed array book with a bitmap BBO index** (`ArrayOrderBook`) — an alternative to the `std::map` book: O(1) level lookup/insert/erase, contiguous cache-friendly levels, and `ctz`/`clz` hardware bit-scan to advance the best-bid/ask cursors. Benchmarked head-to-head with a CI-gated, byte-identical trade-stream cross-check (see Sample Results)
- **Sequence numbers on every event** — Enables deterministic replay, gap detection, and recovery

---

## Validation & Correctness

All ten checks below pass via `./bin/test_invariants` (and `ctest`):

| Test Category | What It Verifies |
|---|---|
| **No crossed book** | After every match cycle, best bid < best ask (50K random orders) |
| **FIFO priority** | Orders at the same price fill in arrival order |
| **Deterministic matching** | Same input stream → identical trades on every run |
| **Quantity conservation** | Filled quantity balances on both sides of every trade |
| **Cancel correctness** | Cancelled orders never match; book stays consistent |
| **Fuzz: random events** | 100K random order events with all invariants checked |
| **Stop / StopLimit triggers** | Stops release as market/limit when the print crosses the trigger |
| **Cancel parked stop** | Parked stop orders can be cancelled before triggering |
| **Multi-subscriber fan-out** | Trades broadcast to engine + feed publisher without clobbering |

---

## Repository Structure

```
MicroExchange/
├── core/                      # Matching engine
│   ├── include/
│   │   ├── Order.h            # Order types, side, TIF
│   │   ├── OrderBook.h        # CLOB with price-time priority (std::map levels)
│   │   ├── ArrayOrderBook.h   # CLOB with tick-indexed array + bitmap BBO index
│   │   ├── MatchingEngine.h   # Multi-symbol engine facade
│   │   ├── PriceLevel.h       # Intrusive linked-list level
│   │   └── ArenaAllocator.h   # Slab allocator for orders
│   └── tests/
│       └── test_invariants.cpp # Property-based + fuzz tests
├── md/                        # Market data feed
│   └── include/
│       ├── FeedMessage.h      # ITCH-style wire protocol
│       ├── FeedPublisher.h    # Incremental + snapshot publisher
│       └── SPSCRingBuffer.h   # Lock-free SPSC queue
├── net/                       # Order-entry gateway (TCP)
│   ├── include/
│   │   ├── OrderEntryProtocol.h # Binary wire protocol (framing + messages)
│   │   └── OrderGateway.h       # Single-threaded TCP gateway → MatchingEngine
│   └── tests/
│       └── test_gateway.cpp     # Loopback end-to-end test (CI-gated)
├── sim/                       # Event-driven simulation
│   └── include/
│       ├── HawkesProcess.h    # Clustered arrivals
│       ├── ZIAgent.h          # Zero-intelligence trader
│       └── Simulator.h        # Orchestrator (unused, see main.cpp)
├── analytics/                 # Microstructure metrics
│   └── include/
│       ├── SpreadAnalyzer.h   # Huang-Stoll decomposition
│       ├── ImpactAnalyzer.h   # Kyle's lambda
│       ├── ImbalanceAnalyzer.h # OFI analysis
│       └── StylizedFacts.h    # Fat tails, vol clustering
├── src/
│   └── main.cpp               # CLI entry point
├── bench/
│   ├── bench_throughput.cpp        # Single-thread matching throughput
│   ├── bench_latency.cpp           # Per-op latency histogram (p50/p90/p99/...)
│   └── bench_orderbook_compare.cpp # std::map vs tick-indexed array (+ correctness)
├── .github/workflows/
│   └── ci.yml                  # GitHub Actions: build + ctest on Linux/macOS
├── research/
│   └── microstructure_paper.md # Theory + empirical writeup
├── output/                    # Generated by simulation
│   ├── trades.csv
│   ├── midprices.csv
│   ├── spreads.csv
│   └── report.txt
├── docs/
│   └── visualizations.html    # Interactive charts
├── CMakeLists.txt
├── CHANGELOG.md
├── .gitignore
├── LICENSE
└── README.md
```

---

## Research Paper

See [`research/microstructure_paper.md`](research/microstructure_paper.md) for a theory + empirical writeup covering:

- Price formation theory (Glosten-Milgrom, Kyle, Ho-Stoll)
- Spread decomposition methodology (Huang-Stoll, realized spread)
- Empirical results from simulation
- Stylized fact reproduction and model calibration
- Limitations and extensions

---

## References

- Glosten, L. & Milgrom, P. (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders.
- Kyle, A. (1985). Continuous auctions and insider trading.
- Ho, T. & Stoll, H. (1981). Optimal dealer pricing under transactions and return uncertainty.
- Avellaneda, M. & Stoikov, S. (2008). High-frequency trading in a limit order book.
- Hasbrouck, J. (2007). Empirical Market Microstructure.
- Bouchaud, J.-P. et al. (2018). Trades, Quotes and Prices: Financial Markets Under the Microscope.
- Hawkes, A. (1971). Spectra of some self-exciting and mutually exciting point processes.

---

## License

MIT License. See [LICENSE](LICENSE).

### Core Implementation Code & Architecture
#### File: `bench/bench_latency.cpp`
```python
/*
 * bench_latency.cpp - per-operation latency histogram for the matching engine.
 *
 * Measures the wall-clock cost of submit_order() across a long stream of
 * synthetic add/cancel/match operations and reports p50/p90/p95/p99/p999
 * along with min/max. The intent is to give a quick "is anything regressing"
 * signal that can be wired into CI or run by hand before tagging a release.
 *
 * Usage:
 *   ./bench_latency                 # 1M operations against a 10x5 seeded book
 *   ./bench_latency --ops 5000000   # 5M operations
 *   ./bench_latency --warmup 200000 # warmup count before timing starts
 */

#include "MatchingEngine.h"
#include "OrderBook.h"
#include "Order.h"

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>

using namespace micro_exchange::core;

namespace {

struct CliArgs {
    size_t ops    = 1'000'000;
    size_t warmup =   100'000;
};

CliArgs parse(int argc, char** argv) {
    CliArgs a;
    for (int i = 1; i < argc; ++i) {
        std::string s = argv[i];
        if (s == "--ops" && i + 1 < argc)    a.ops    = std::stoull(argv[++i]);
        else if (s == "--warmup" && i + 1 < argc) a.warmup = std::stoull(argv[++i]);
        else if (s == "--help") {
            std::cout << "usage: bench_latency [--ops N] [--warmup N]\n";
            std::exit(0);
        }
    }
    return a;
}

void seed_book(MatchingEngine& engine, const char* sym, Price mid) {
    OrderId id = 1;
    for (int lvl = 1; lvl <= 10; ++lvl) {
        for (int j = 0; j < 5; ++j) {
            NewOrderRequest req{};
            req.id = id++;
            req.side = Side::Buy;
            req.type = OrderType::Limit;
            req.tif = TimeInForce::GTC;
            req.price = mid - lvl;
            req.quantity = 100 + j * 50;
            std::strncpy(req.symbol, sym, 15);
            engine.submit_order(req);

            req.id = id++;
            req.side = Side::Sell;
            req.price = mid + lvl;
            engine.submit_order(req);
        }
    }
}

double percentile(std::vector<uint64_t>& v, double p) {
    if (v.empty()) return 0;
    size_t idx = static_cast<size_t>(p * (v.size() - 1));
    std::nth_element(v.begin(), v.begin() + idx, v.end());
    return static_cast<double>(v[idx]);
}

} // namespace

int main(int argc, char** argv) {
    CliArgs args = parse(argc, argv);

    std::cout << "\n  MicroExchange — Latency Benchmark\n";
    std::cout << "  ─────────────────────────────────\n";
    std::cout << "  Operations:  " << args.ops << "\n";
    std::cout << "  Warmup:      " << args.warmup << "\n\n";

    const char* sym = "BENCH";
    MatchingEngine engine;
    engine.add_symbol(sym);
    seed_book(engine, sym, 10000);

    std::mt19937_64 rng(0xBEEFCAFE);
    std::uniform_int_distribution<int>      side_dist(0, 1);
    std::uniform_int_distribution<int>      type_dist(0, 9);
    std::uniform_int_distribution<Price>    price_dist(9990, 10010);
    std::uniform_int_distribution<Quantity> qty_dist(1, 5);

    OrderId id = 100'000;
    auto submit_random = [&]() {
        NewOrderRequest req{};
        req.id = id++;
        req.side = side_dist(rng) ? Side::Buy : Side::Sell;
        bool is_market = type_dist(rng) == 0;       // 10% market
        req.type = is_market ? OrderType::Market : OrderType::Limit;
        req.tif  = is_market ? TimeInForce::IOC   : TimeInForce::GTC;
        req.price = is_market ? PRICE_MARKET : price_dist(rng);
        req.quantity = qty_dist(rng) * 100;
        std::strncpy(req.symbol, sym, 15);
        engine.submit_order(req);
    };

    // Warmup
    for (size_t i = 0; i < args.warmup; ++i) submit_random();

    std::vector<uint64_t> latencies;
    latencies.reserve(args.ops);

    auto t_start = std::chrono::steady_clock::now();
    for (size_t i = 0; i < args.ops; ++i) {
        auto a = std::chrono::steady_clock::now();
        submit_random();
        auto b = std::chrono::steady_clock::now();
        latencies.push_back(
            std::chrono::duration_cast<std::chrono::nanoseconds>(b - a).count());
    }
    auto t_end = std::chrono::steady_clock::now();

    double wall_sec =
        std::chrono::duration<double>(t_end - t_start).count();

    double p50 = percentile(latencies, 0.50);
    double p90 = percentile(latencies, 0.90);
    double p95 = percentile(latencies, 0.95);
    double p99 = percentile(latencies, 0.99);
    double p999 = percentile(latencies, 0.999);
    auto mm = std::minmax_element(latencies.begin(), latencies.end());

    std::cout << std::fixed << std::setprecision(0);
    std::cout << "  Throughput:  " << (args.ops / wall_sec) << " ops/sec\n\n";

    std::cout << "  Latency (nanoseconds)\n";
    std::cout << "  ─────────────────────\n";
    std::cout << "  min        " << *mm.first  << "\n";
    std::cout << "  p50        " << p50  << "\n";
    std::cout << "  p90        " << p90  << "\n";
    std::cout << "  p95        " << p95  << "\n";
    std::cout << "  p99        " << p99  << "\n";
    std::cout << "  p99.9      " << p999 << "\n";
    std::cout << "  max        " << *mm.second << "\n\n";

    return 0;
}
```

#### File: `net/tests/test_gateway.cpp`
```python
/**
 * test_gateway.cpp — end-to-end loopback test for the TCP order-entry gateway.
 *
 * Spins up an OrderGateway on an ephemeral port in a server thread, connects a
 * client over 127.0.0.1, and streams a deterministic order flow through the
 * wire protocol. It then runs the SAME orders through an in-process
 * MatchingEngine reference and asserts the networked path produced an identical
 * number of executions and identical traded volume — i.e. serialising orders
 * over TCP and parsing them back changes nothing about the matching outcome.
 *
 * Doubles as a usage demo for the protocol and as a CTest gate.
 */

#include "OrderGateway.h"
#include "OrderEntryProtocol.h"
#include "MatchingEngine.h"

#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
#include <unistd.h>

#include <thread>
#include <vector>
#include <random>
#include <iostream>
#include <cstring>

using namespace micro_exchange;
using namespace micro_exchange::core;
using namespace micro_exchange::net;

static std::vector<NewOrderRequest> make_flow(size_t n, const char* sym) {
    std::mt19937_64 rng(7);
    std::uniform_int_distribution<Price>    price(95, 105);
    std::uniform_int_distribution<Quantity> qty(1, 5);
    std::uniform_int_distribution<int>      side(0, 1);
    std::uniform_real_distribution<double>  type(0.0, 1.0);

    std::vector<NewOrderRequest> v;
    v.reserve(n);
    for (size_t i = 0; i < n; ++i) {
        NewOrderRequest r{};
        r.id   = i + 1;
        r.side = side(rng) ? Side::Buy : Side::Sell;
        if (type(rng) < 0.65) {
            r.type  = OrderType::Limit;
            r.tif   = TimeInForce::GTC;
            r.price = price(rng);
        } else {
            r.type  = OrderType::Market;
            r.tif   = TimeInForce::IOC;
            r.price = PRICE_MARKET;
        }
        r.quantity = qty(rng) * 100;
        std::strncpy(r.symbol, sym, sizeof(r.symbol) - 1);
        v.push_back(r);
    }
    return v;
}

int main() {
    const char* SYM = "TEST";
    auto orders = make_flow(3000, SYM);

    // ── Reference: same flow, in-process (no network) ──
    uint64_t ref_trades = 0, ref_volume = 0;
    {
        MatchingEngine ref;
        ref.add_symbol(SYM);
        ref.set_trade_callback([&](const Trade& t) { ++ref_trades; ref_volume += t.quantity; });
        for (const auto& r : orders) ref.submit_order(r);
    }

    // ── Gateway on an ephemeral port, served on its own thread ──
    OrderGateway gateway(0, SYM);
    uint16_t port = gateway.port();
    std::thread server([&] { gateway.serve_one_client(); });

    // ── Client: connect and stream orders lock-step (send → read execs → ack) ──
    int cfd = ::socket(AF_INET, SOCK_STREAM, 0);
    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    addr.sin_port = htons(port);

    // Disable Nagle on the client too: a lock-step small-message protocol must
    // not buffer — Nagle + delayed-ACK otherwise adds ~40ms per round trip.
    int nodelay = 1;
    ::setsockopt(cfd, IPPROTO_TCP, TCP_NODELAY, &nodelay, sizeof(nodelay));

    // Defensive: a 5s receive timeout turns any stall into a visible error
    // instead of an indefinite hang.
    timeval tv{}; tv.tv_sec = 5; tv.tv_usec = 0;
    ::setsockopt(cfd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));

    bool connected = false;
    for (int i = 0; i < 200; ++i) {
        if (::connect(cfd, reinterpret_cast<sockaddr*>(&addr), sizeof(addr)) == 0) { connected = true; break; }
        usleep(2000);
    }
    if (!connected) { std::cerr << "client could not connect to gateway\n"; return 1; }

    uint64_t wire_execs = 0, wire_exec_volume = 0, acks = 0;

    for (const auto& r : orders) {
        WireNewOrder w{};
        w.id       = r.id;
        w.side     = static_cast<uint8_t>(r.side);
        w.type     = static_cast<uint8_t>(r.type);
        w.tif      = static_cast<uint8_t>(r.tif);
        w.price    = r.price;
        w.quantity = r.quantity;
        std::memcpy(w.symbol, r.symbol, sizeof(w.symbol));
        if (!send_msg(cfd, MsgType::NewOrder, &w, sizeof(w))) { std::cerr << "send failed\n"; return 1; }

        // Read execs until this order's Ack arrives.
        WireHeader h{};
        bool acked = false;
        while (!acked && recv_header(cfd, h)) {
            if (static_cast<MsgType>(h.type) == MsgType::Exec) {
                WireExec e{};
                if (!read_full(cfd, &e, sizeof(e))) { std::cerr << "exec read failed\n"; return 1; }
                ++wire_execs;
                wire_exec_volume += e.quantity;
            } else if (static_cast<MsgType>(h.type) == MsgType::Ack) {
                WireAck a{};
                if (!read_full(cfd, &a, sizeof(a))) { std::cerr << "ack read failed\n"; return 1; }
                ++acks;
                acked = true;
            } else {
                std::vector<char> tmp(h.len);
                read_full(cfd, tmp.data(), h.len);
            }
        }
        if (!acked) { std::cerr << "no ack for order " << r.id << "\n"; return 1; }
    }

    ::close(cfd);          // client done → server's read loop ends
    server.join();

    auto gs = gateway.stats();

    std::cout << "\n──────────── Gateway end-to-end test ────────────\n";
    std::cout << "  orders sent over TCP : " << orders.size() << "\n";
    std::cout << "  acks received        : " << acks << "\n";
    std::cout << "  execs over the wire  : " << wire_execs << " (vol " << wire_exec_volume << ")\n";
    std::cout << "  in-process reference : " << ref_trades << " (vol " << ref_volume << ")\n";
    std::cout << "  gateway engine trades: " << gs.total_trades << "\n";

    bool ok = (acks == orders.size())
           && (wire_execs == ref_trades)
           && (wire_exec_volume == ref_volume)
           && (gs.total_trades == ref_trades);

    std::cout << (ok ? "  GATEWAY TEST PASSED ✓\n" : "  GATEWAY TEST FAILED ✗\n");
    std::cout << "─────────────────────────────────────────────────\n";
    return ok ? 0 : 1;
}
```

#### File: `bench/bench_orderbook_compare.cpp`
```python
/**
 * bench_orderbook_compare.cpp — std::map OrderBook vs tick-indexed ArrayOrderBook.
 *
 * Two questions, answered side by side:
 *
 *   1. CORRECTNESS: do the two books produce the *identical* trade stream on
 *      the same input? (If not, any speed comparison is meaningless.) We run
 *      both, capture every (buy_id, sell_id, price, qty, aggressor) tuple, and
 *      assert the sequences match exactly.
 *
 *   2. PERFORMANCE: how much faster is the contiguous, cache-friendly array
 *      layout than the red-black tree on the matching hot path?
 *
 * Both books reuse the SAME Order, PriceLevel, and ArenaAllocator, so the only
 * variable is the level container (std::map vs flat array).
 *
 * Methodology: orders are pre-generated, so we time only the matching loop, not
 * RNG. Same seed and same workload feed both books.
 */

#include "../core/include/OrderBook.h"
#include "../core/include/ArrayOrderBook.h"
#include "../core/include/Order.h"

#include <chrono>
#include <iostream>
#include <iomanip>
#include <vector>
#include <random>
#include <algorithm>
#include <numeric>
#include <cstring>

using namespace micro_exchange::core;

using Clock = std::chrono::high_resolution_clock;
using ns    = std::chrono::nanoseconds;

// Price band for the workload. Limits land in [9900, 10100]; the array book is
// sized a little wider so every resting limit has a slot.
static constexpr Price kMinPrice = 9800;
static constexpr Price kMaxPrice = 10200;

// ─────────────────────────────────────────────
// Workload (same generator the throughput bench uses)
// ─────────────────────────────────────────────
std::vector<NewOrderRequest> generate_orders(size_t count, uint64_t seed = 42) {
    std::mt19937_64 rng(seed);
    std::uniform_int_distribution<Price>    price_dist(9900, 10100);
    std::uniform_int_distribution<Quantity> qty_dist(1, 10);
    std::uniform_int_distribution<int>      side_dist(0, 1);
    std::uniform_real_distribution<double>  type_dist(0.0, 1.0);

    std::vector<NewOrderRequest> orders;
    orders.reserve(count);
    for (size_t i = 0; i < count; ++i) {
        NewOrderRequest req{};
        req.id   = i + 1;
        req.side = side_dist(rng) ? Side::Buy : Side::Sell;
        if (type_dist(rng) < 0.7) {
            req.type  = OrderType::Limit;
            req.tif   = TimeInForce::GTC;
            req.price = price_dist(rng);
        } else {
            req.type  = OrderType::Market;
            req.tif   = TimeInForce::IOC;
            req.price = PRICE_MARKET;
        }
        req.quantity = qty_dist(rng) * 100;
        std::memcpy(req.symbol, "BENCH", 6);
        orders.push_back(req);
    }
    return orders;
}

// Comparable trade fingerprint (sequence numbers excluded — they're per-book).
struct TradeKey {
    OrderId  buy_id, sell_id;
    Price    price;
    Quantity qty;
    uint8_t  aggressor;
    bool operator==(const TradeKey& o) const {
        return buy_id == o.buy_id && sell_id == o.sell_id &&
               price == o.price && qty == o.qty && aggressor == o.aggressor;
    }
};

template <class Book>
std::vector<TradeKey> collect_trades(Book& book, const std::vector<NewOrderRequest>& orders) {
    std::vector<TradeKey> trades;
    trades.reserve(orders.size());
    book.set_trade_callback([&](const Trade& t) {
        trades.push_back({t.buy_order_id, t.sell_order_id, t.price, t.quantity,
                          static_cast<uint8_t>(t.aggressor)});
    });
    for (const auto& r : orders) book.add_order(r);
    return trades;
}

template <class Book>
double time_throughput(Book& book, const std::vector<NewOrderRequest>& orders) {
    auto start = Clock::now();
    for (const auto& r : orders) book.add_order(r);
    auto end = Clock::now();
    double s = std::chrono::duration_cast<ns>(end - start).count() / 1e9;
    return orders.size() / s;
}

template <class Book>
void time_latency(Book& book, const std::vector<NewOrderRequest>& orders,
                  uint64_t& p50, uint64_t& p99) {
    std::vector<uint64_t> lat;
    lat.reserve(orders.size());
    for (const auto& r : orders) {
        auto s = Clock::now();
        book.add_order(r);
        auto e = Clock::now();
        lat.push_back(std::chrono::duration_cast<ns>(e - s).count());
    }
    std::sort(lat.begin(), lat.end());
    p50 = lat[static_cast<size_t>(0.50 * (lat.size() - 1))];
    p99 = lat[static_cast<size_t>(0.99 * (lat.size() - 1))];
}

int main() {
    std::cout << "\n══════════════════════════════════════════════════════════\n";
    std::cout << "  OrderBook (std::map)  vs  ArrayOrderBook (tick-indexed)\n";
    std::cout << "══════════════════════════════════════════════════════════\n";

    // ── 1. Correctness cross-check ──
    {
        auto orders = generate_orders(200000);
        OrderBook      map_book("BENCH");
        ArrayOrderBook arr_book("BENCH", kMinPrice, kMaxPrice);

        auto map_trades = collect_trades(map_book, orders);
        auto arr_trades = collect_trades(arr_book, orders);

        bool ok = (map_trades.size() == arr_trades.size()) &&
                  std::equal(map_trades.begin(), map_trades.end(), arr_trades.begin());

        std::cout << "\n── Correctness ──\n";
        std::cout << "  std::map  trades: " << map_trades.size() << "\n";
        std::cout << "  array     trades: " << arr_trades.size() << "\n";
        std::cout << "  identical trade stream: " << (ok ? "YES ✓" : "NO ✗") << "\n";
        if (!ok) {
            std::cout << "  FATAL: trade streams diverge — aborting benchmark.\n";
            return 1;
        }
    }

    // ── 2. Throughput ──
    std::cout << "\n── Throughput (orders/sec) ──\n";
    std::cout << "   N        │ std::map      │ array         │ speedup\n";
    std::cout << "  ──────────┼───────────────┼───────────────┼─────────\n";
    for (size_t n : {100000, 1000000}) {
        auto orders = generate_orders(n);
        OrderBook      map_book("BENCH");
        ArrayOrderBook arr_book("BENCH", kMinPrice, kMaxPrice);

        double map_tp = time_throughput(map_book, orders);
        double arr_tp = time_throughput(arr_book, orders);

        std::cout << "  " << std::setw(8) << n << "  │ "
                  << std::setw(10) << std::fixed << std::setprecision(0) << map_tp << "/s │ "
                  << std::setw(10) << arr_tp << "/s │ "
                  << std::setw(5) << std::setprecision(2) << (arr_tp / map_tp) << "x\n";
    }

    // ── 3. Per-order latency ──
    std::cout << "\n── Latency (ns/order, 1M orders) ──\n";
    {
        auto orders = generate_orders(1000000);
        OrderBook      map_book("BENCH");
        ArrayOrderBook arr_book("BENCH", kMinPrice, kMaxPrice);

        uint64_t m50, m99, a50, a99;
        time_latency(map_book, orders, m50, m99);
        time_latency(arr_book, orders, a50, a99);

        std::cout << "            │  P50   │  P99\n";
        std::cout << "  ──────────┼────────┼────────\n";
        std::cout << "  std::map  │ " << std::setw(5) << m50 << "  │ " << std::setw(5) << m99 << "\n";
        std::cout << "  array     │ " << std::setw(5) << a50 << "  │ " << std::setw(5) << a99 << "\n";
    }

    std::cout << "\n══════════════════════════════════════════════════════════\n";
    std::cout << "  Done.\n";
    std::cout << "══════════════════════════════════════════════════════════\n\n";
    return 0;
}
```

#### File: `bench/bench_throughput.cpp`
```python
/**
 * bench_throughput.cpp — Matching engine throughput and latency benchmark.
 *
 * Measures:
 *   • Single-thread matching throughput (orders/sec)
 *   • Per-order latency distribution (p50/p95/p99/p999)
 *   • Arena allocator overhead vs raw new/delete
 *   • Book depth impact on matching performance
 *
 * Methodology:
 *   Pre-generate all orders, then measure only the matching hot path.
 *   This isolates engine performance from random number generation.
 */

#include "../core/include/MatchingEngine.h"
#include "../core/include/OrderBook.h"
#include "../core/include/Order.h"

#include <chrono>
#include <iostream>
#include <iomanip>
#include <vector>
#include <random>
#include <algorithm>
#include <numeric>

using namespace micro_exchange::core;

using Clock = std::chrono::high_resolution_clock;
using ns = std::chrono::nanoseconds;

// ─────────────────────────────────────────────
// Pre-generate orders
// ─────────────────────────────────────────────

std::vector<NewOrderRequest> generate_orders(size_t count, uint64_t seed = 42) {
    std::mt19937_64 rng(seed);
    std::uniform_int_distribution<Price> price_dist(9900, 10100);
    std::uniform_int_distribution<Quantity> qty_dist(1, 10);
    std::uniform_int_distribution<int> side_dist(0, 1);
    std::uniform_real_distribution<double> type_dist(0.0, 1.0);

    std::vector<NewOrderRequest> orders;
    orders.reserve(count);

    for (size_t i = 0; i < count; ++i) {
        NewOrderRequest req{};
        req.id = i + 1;
        req.side = side_dist(rng) ? Side::Buy : Side::Sell;

        double type_roll = type_dist(rng);
        if (type_roll < 0.7) {
            req.type = OrderType::Limit;
            req.tif = TimeInForce::GTC;
            req.price = price_dist(rng);
        } else {
            req.type = OrderType::Market;
            req.tif = TimeInForce::IOC;
            req.price = PRICE_MARKET;
        }

        req.quantity = qty_dist(rng) * 100;
        std::memcpy(req.symbol, "BENCH", 6);
        orders.push_back(req);
    }

    return orders;
}

// ─────────────────────────────────────────────
// Benchmark: Throughput
// ─────────────────────────────────────────────

void bench_throughput(size_t num_orders) {
    std::cout << "\n── Throughput Benchmark (" << num_orders << " orders) ──\n";

    auto orders = generate_orders(num_orders);
    OrderBook book("BENCH");

    auto start = Clock::now();
    for (const auto& req : orders) {
        book.add_order(req);
    }
    auto end = Clock::now();

    auto elapsed_ns = std::chrono::duration_cast<ns>(end - start).count();
    double elapsed_s = elapsed_ns / 1e9;
    double throughput = num_orders / elapsed_s;

    std::cout << "  Orders processed: " << num_orders << "\n";
    std::cout << "  Trades executed:  " << book.trade_count() << "\n";
    std::cout << "  Wall time:        " << std::fixed << std::setprecision(3)
              << elapsed_s * 1000 << " ms\n";
    std::cout << "  Throughput:       " << std::fixed << std::setprecision(0)
              << throughput << " orders/sec\n";
    std::cout << "                    " << std::fixed << std::setprecision(2)
              << throughput / 1e6 << "M orders/sec\n";
}

// ─────────────────────────────────────────────
// Benchmark: Latency distribution
// ─────────────────────────────────────────────

void bench_latency(size_t num_orders) {
    std::cout << "\n── Latency Benchmark (" << num_orders << " orders) ──\n";

    auto orders = generate_orders(num_orders);
    OrderBook book("BENCH");

    std::vector<uint64_t> latencies;
    latencies.reserve(num_orders);

    for (const auto& req : orders) {
        auto start = Clock::now();
        book.add_order(req);
        auto end = Clock::now();

        latencies.push_back(
            std::chrono::duration_cast<ns>(end - start).count()
        );
    }

    // Sort for percentile computation
    std::sort(latencies.begin(), latencies.end());

    auto percentile = [&](double p) -> uint64_t {
        size_t idx = static_cast<size_t>(p * (latencies.size() - 1));
        return latencies[idx];
    };

    double mean = std::accumulate(latencies.begin(), latencies.end(), 0.0) / latencies.size();

    std::cout << "  Mean:    " << std::fixed << std::setprecision(0) << mean << " ns\n";
    std::cout << "  P50:     " << percentile(0.50) << " ns\n";
    std::cout << "  P90:     " << percentile(0.90) << " ns\n";
    std::cout << "  P95:     " << percentile(0.95) << " ns\n";
    std::cout << "  P99:     " << percentile(0.99) << " ns\n";
    std::cout << "  P99.9:   " << percentile(0.999) << " ns\n";
    std::cout << "  Max:     " << latencies.back() << " ns\n";

    // Latency histogram
    std::cout << "\n  Latency Histogram:\n";
    std::vector<std::pair<std::string, uint64_t>> buckets = {
        {"<100ns",   100},
        {"100-250",  250},
        {"250-500",  500},
        {"500-1μs",  1000},
        {"1-2μs",    2000},
        {"2-5μs",    5000},
        {">5μs",     UINT64_MAX}
    };

    size_t idx = 0;
    for (const auto& [label, upper] : buckets) {
        size_t count = 0;
        while (idx < latencies.size() && latencies[idx] < upper) {
            ++count;
            ++idx;
        }
        double pct = 100.0 * count / latencies.size();
        int bars = static_cast<int>(pct / 2);
        std::cout << "    " << std::setw(8) << label << " │ "
                  << std::string(bars, '#')
                  << " " << std::fixed << std::setprecision(1) << pct << "%\n";
    }
}

// ─────────────────────────────────────────────
// Benchmark: Impact of book depth
// ─────────────────────────────────────────────

void bench_depth_impact() {
    std::cout << "\n── Book Depth Impact ──\n";
    std::cout << "  Depth  │ Add (ns)  │ Match (ns)\n";
    std::cout << "  ───────┼───────────┼───────────\n";

    for (size_t depth : {10, 50, 100, 500, 1000}) {
        OrderBook book("BENCH");

        // Build book to target depth
        for (size_t i = 0; i < depth; ++i) {
            NewOrderRequest bid{};
            bid.id = i + 1;
            bid.side = Side::Buy;
            bid.type = OrderType::Limit;
            bid.tif = TimeInForce::GTC;
            bid.price = 10000 - (i % 50);
            bid.quantity = 100;
            std::memcpy(bid.symbol, "BENCH", 6);
            book.add_order(bid);

            NewOrderRequest ask{};
            ask.id = depth + i + 1;
            ask.side = Side::Sell;
            ask.type = OrderType::Limit;
            ask.tif = TimeInForce::GTC;
            ask.price = 10001 + (i % 50);
            ask.quantity = 100;
            std::memcpy(ask.symbol, "BENCH", 6);
            book.add_order(ask);
        }

        // Measure add latency
        const size_t N = 10000;
        uint64_t add_total = 0;
        for (size_t i = 0; i < N; ++i) {
            NewOrderRequest req{};
            req.id = 100000 + i;
            req.side = (i % 2) ? Side::Buy : Side::Sell;
            req.type = OrderType::Limit;
            req.tif = TimeInForce::GTC;
            req.price = (req.side == Side::Buy) ? Price(9950) : Price(10050);
            req.quantity = 100;
            std::memcpy(req.symbol, "BENCH", 6);

            auto s = Clock::now();
            book.add_order(req);
            auto e = Clock::now();
            add_total += std::chrono::duration_cast<ns>(e - s).count();
        }

        // Measure match latency (market orders)
        uint64_t match_total = 0;
        for (size_t i = 0; i < N; ++i) {
            // First, add a resting order to match against
            NewOrderRequest rest{};
            rest.id = 200000 + i * 2;
            rest.side = Side::Buy;
            rest.type = OrderType::Limit;
            rest.tif = TimeInForce::GTC;
            rest.price = 10000;
            rest.quantity = 100;
            std::memcpy(rest.symbol, "BENCH", 6);
            book.add_order(rest);

            // Then measure matching a market sell
            NewOrderRequest mkt{};
            mkt.id = 200000 + i * 2 + 1;
            mkt.side = Side::Sell;
            mkt.type = OrderType::Market;
            mkt.tif = TimeInForce::IOC;
            mkt.price = PRICE_MARKET;
            mkt.quantity = 100;
            std::memcpy(mkt.symbol, "BENCH", 6);

            auto s = Clock::now();
            book.add_order(mkt);
            auto e = Clock::now();
            match_total += std::chrono::duration_cast<ns>(e - s).count();
        }

        std::cout << "  " << std::setw(5) << depth
                  << "  │ " << std::setw(7) << add_total / N
                  << "   │ " << std::setw(7) << match_total / N << "\n";
    }
}

// ─────────────────────────────────────────────
// Main
// ─────────────────────────────────────────────

int main() {
    std::cout << "\n══════════════════════════════════════════════\n";
    std::cout << "  MicroExchange — Performance Benchmarks\n";
    std::cout << "══════════════════════════════════════════════\n";

    bench_throughput(100000);
    bench_throughput(1000000);
    bench_latency(100000);
    bench_depth_impact();

    std::cout << "\n══════════════════════════════════════════════\n";
    std::cout << "  Benchmarks complete\n";
    std::cout << "══════════════════════════════════════════════\n\n";

    return 0;
}
```

#### File: `src/main.cpp`
```python
/*
 * main.cpp - MicroExchange CLI
 *
 * Runs the full pipeline: hawkes event generation -> ZI agents ->
 * matching engine -> feed publisher -> analytics.
 *
 * Usage:
 *   ./micro_exchange                      # default 1hr simulation
 *   ./micro_exchange --duration 7200      # 2hr simulation
 *   ./micro_exchange --symbol AAPL        # set the symbol
 *   ./micro_exchange --output results/    # custom output dir
 *   ./micro_exchange -v                   # verbose
 */

#include "MatchingEngine.h"
#include "OrderBook.h"
#include "Order.h"
#include "FeedPublisher.h"
#include "HawkesProcess.h"
#include "ZIAgent.h"
#include "SpreadAnalyzer.h"
#include "ImpactAnalyzer.h"
#include "StylizedFacts.h"

#include <iostream>
#include <fstream>
#include <iomanip>
#include <chrono>
#include <string>
#include <vector>
#include <numeric>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <filesystem>

using namespace micro_exchange::core;
using namespace micro_exchange::md;
using namespace micro_exchange::sim;
using namespace micro_exchange::analytics;

namespace fs = std::filesystem;

// ── Config ──

struct RunConfig {
    std::string symbol    = "AAPL";
    double      duration  = 3600.0;
    Price       init_mid  = 15000;  // $150.00
    size_t      n_agents  = 10;
    std::string out_dir   = "output";
    bool        verbose   = false;
};

RunConfig parse_args(int argc, char* argv[]) {
    RunConfig cfg;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--duration" && i + 1 < argc) cfg.duration = std::stod(argv[++i]);
        else if (arg == "--symbol" && i + 1 < argc) cfg.symbol = argv[++i];
        else if (arg == "--output" && i + 1 < argc) cfg.out_dir = argv[++i];
        else if (arg == "-v" || arg == "--verbose") cfg.verbose = true;
        else if (arg == "--help") {
            std::cout << "Usage: micro_exchange [--duration SEC] [--symbol SYM] [--output DIR] [-v]\n";
            std::exit(0);
        }
    }
    return cfg;
}

// ── Helpers ──

void seed_book(MatchingEngine& engine, const std::string& symbol, Price mid) {
    // 10 levels each side, 5 orders per level
    // this gives a reasonable starting book so the first few market orders
    // don't just sail through into the void
    OrderId id = 1;
    for (int lvl = 1; lvl <= 10; ++lvl) {
        for (int j = 0; j < 5; ++j) {
            NewOrderRequest bid{};
            bid.id = id++;
            bid.side = Side::Buy;
            bid.type = OrderType::Limit;
            bid.tif = TimeInForce::GTC;
            bid.price = mid - lvl;
            bid.quantity = 100 + (j * 50);
            std::strncpy(bid.symbol, symbol.c_str(), 15);
            engine.submit_order(bid);

            NewOrderRequest ask{};
            ask.id = id++;
            ask.side = Side::Sell;
            ask.type = OrderType::Limit;
            ask.tif = TimeInForce::GTC;
            ask.price = mid + lvl;
            ask.quantity = 100 + (j * 50);
            std::strncpy(ask.symbol, symbol.c_str(), 15);
            engine.submit_order(ask);
        }
    }
}

void write_trades_csv(const std::string& path, const std::vector<Trade>& trades) {
    std::ofstream ofs(path);
    ofs << "seq,buy_id,sell_id,price,qty,aggressor\n";
    for (const auto& t : trades) {
        ofs << t.sequence << ","
            << t.buy_order_id << ","
            << t.sell_order_id << ","
            << t.price << ","
            << t.quantity << ","
            << (t.aggressor == Side::Buy ? "B" : "S") << "\n";
    }
}

void write_midprices_csv(const std::string& path, const std::vector<Price>& mids) {
    std::ofstream ofs(path);
    ofs << "idx,midprice\n";
    for (size_t i = 0; i < mids.size(); ++i) {
        ofs << i << "," << mids[i] << "\n";
    }
}

void write_spreads_csv(const std::string& path, const std::vector<Price>& spreads) {
    std::ofstream ofs(path);
    ofs << "idx,quoted_spread\n";
    for (size_t i = 0; i < spreads.size(); ++i) {
        ofs << i << "," << spreads[i] << "\n";
    }
}

// ── Main ──

int main(int argc, char* argv[]) {
    auto cfg = parse_args(argc, argv);

    std::cout << "\n";
    std::cout << "  ╔══════════════════════════════════════════╗\n";
    std::cout << "  ║       MicroExchange v1.0.0               ║\n";
    std::cout << "  ║   CLOB + Market Data + Analytics         ║\n";
    std::cout << "  ╚══════════════════════════════════════════╝\n\n";

    std::cout << "  Symbol:   " << cfg.symbol << "\n";
    std::cout << "  Duration: " << cfg.duration << " sec\n";
    std::cout << "  Init mid: " << cfg.init_mid << " ($"
              << std::fixed << std::setprecision(2) << cfg.init_mid / 100.0 << ")\n";
    std::cout << "  Agents:   " << cfg.n_agents << "\n\n";

    fs::create_directories(cfg.out_dir);

    auto wall_start = std::chrono::high_resolution_clock::now();

    // ── Engine setup ──
    MatchingEngine engine;
    engine.add_symbol(cfg.symbol);
    auto* book = engine.get_book(cfg.symbol);

    // The OrderBook now supports multi-listener fan-out, so attaching the
    // feed publisher no longer clobbers the engine's internal trade routing.
    FeedPublisher feed;
    feed.attach(*book);

    // ── Agents ──
    std::vector<ZIAgent> agents;
    for (size_t i = 0; i < cfg.n_agents; ++i) {
        ZIAgent::Parameters p;
        p.agent_id = i;
        // tighter placement = more crossing = more trades
        p.sigma_price = 3.0 + (i % 3) * 1.5;
        p.market_order_prob = 0.15 + (i % 4) * 0.02;
        p.mean_size = 150.0;
        p.sigma_size = 0.5;
        agents.emplace_back(p, 42 + i);
    }

    seed_book(engine, cfg.symbol, cfg.init_mid);

    // ── Generate events ──
    HawkesProcess::Parameters hp;
    hp.mu = 50.0;
    hp.alpha = 35.0;
    hp.beta = 50.0;
    HawkesProcess hawkes(hp, 12345);
    auto events = hawkes.generate_sided(cfg.duration);

    std::cout << "  [1/4] Generated " << events.size() << " events (Hawkes n="
              << std::fixed << std::setprecision(2) << hp.alpha / hp.beta << ")\n";

    // ── Run matching ──
    std::vector<Trade> trades;
    std::vector<double> trade_times;       // simulated wall-clock seconds
    trades.reserve(events.size() / 3);
    trade_times.reserve(events.size() / 3);

    std::vector<Price> midprices;
    std::vector<Price> spreads;
    std::vector<double> mid_times;
    midprices.reserve(events.size());
    spreads.reserve(events.size());
    mid_times.reserve(events.size());

    double current_event_time = 0.0;       // updated in the main loop
    engine.set_trade_callback([&](const Trade& t) {
        trades.push_back(t);
        trade_times.push_back(current_event_time);
    });

    OrderId next_id = 10000;
    size_t progress_step = events.size() / 10;

    for (size_t i = 0; i < events.size(); ++i) {
        if (progress_step > 0 && i % progress_step == 0 && i > 0) {
            std::cout << "  [2/4] Processing... "
                      << (i * 100 / events.size()) << "%\r" << std::flush;
        }

        current_event_time = events[i].timestamp;

        auto mid = book->midprice().value_or(cfg.init_mid);
        auto sprd = book->spread().value_or(2);
        midprices.push_back(mid);
        spreads.push_back(sprd);
        mid_times.push_back(current_event_time);

        size_t agent_idx = next_id % cfg.n_agents;
        auto req = agents[agent_idx].generate_order(
            mid, sprd, events[i].is_buy, next_id++, cfg.symbol.c_str());
        engine.submit_order(req);
    }

    std::cout << "  [2/4] Matching complete: " << trades.size() << " trades from "
              << events.size() << " orders\n";

    // ── Analytics ──
    std::cout << "  [3/4] Computing analytics...\n";

    // Helper: lookup mid at a given simulated time using sorted mid_times
    auto mid_at_time = [&](double t) -> Price {
        if (mid_times.empty()) return cfg.init_mid;
        auto it = std::lower_bound(mid_times.begin(), mid_times.end(), t);
        if (it == mid_times.begin()) return midprices.front();
        if (it == mid_times.end())   return midprices.back();
        size_t idx = static_cast<size_t>(std::distance(mid_times.begin(), it));
        return midprices[idx];
    };

    // Spread decomposition (Huang-Stoll). 5-second post-trade reversion window.
    SpreadAnalyzer spread_analyzer;
    std::vector<SpreadAnalyzer::TradeInput> spread_inputs;

    for (size_t i = 0; i < trades.size(); ++i) {
        SpreadAnalyzer::TradeInput ti;
        ti.trade_price = trades[i].price;
        ti.mid_before  = mid_at_time(trade_times[i]);
        ti.mid_after   = mid_at_time(trade_times[i] + 5.0);
        ti.volume      = trades[i].quantity;
        ti.aggressor   = trades[i].aggressor;
        spread_inputs.push_back(ti);
    }

    auto spread_result = spread_analyzer.compute(spread_inputs, spreads);

    // Kyle's lambda — properly time-indexed now
    ImpactAnalyzer impact_analyzer;
    std::vector<ImpactAnalyzer::TradeInput> impact_inputs;
    std::vector<std::pair<double, Price>> timed_mids;
    impact_inputs.reserve(trades.size());
    timed_mids.reserve(midprices.size());

    for (size_t i = 0; i < trades.size(); ++i) {
        ImpactAnalyzer::TradeInput ti;
        ti.timestamp = trade_times[i];
        ti.price     = trades[i].price;
        ti.volume    = trades[i].quantity;
        ti.aggressor = trades[i].aggressor;
        impact_inputs.push_back(ti);
    }
    for (size_t i = 0; i < midprices.size(); ++i) {
        timed_mids.push_back({mid_times[i], midprices[i]});
    }

    auto kyle_result = impact_analyzer.estimate_kyle_lambda(impact_inputs, timed_mids, 5.0);

    // Stylized facts — sampled on 1-second clock-time bars (log returns),
    // not per-event, to avoid the zero-inflated integer-tick artifact.
    StylizedFacts stylized;
    auto facts = stylized.compute(midprices, mid_times, 1.0);

    // ── Output ──
    std::cout << "  [4/4] Writing output to " << cfg.out_dir << "/\n\n";

    write_trades_csv(cfg.out_dir + "/trades.csv", trades);
    write_midprices_csv(cfg.out_dir + "/midprices.csv", midprices);
    write_spreads_csv(cfg.out_dir + "/spreads.csv", spreads);

    // Summary report
    {
        std::ofstream rpt(cfg.out_dir + "/report.txt");
        auto also = [&](auto& os, const std::string& line) {
            os << line << "\n";
            std::cout << line << "\n";
        };

        auto wall_end = std::chrono::high_resolution_clock::now();
        double wall_sec = std::chrono::duration<double>(wall_end - wall_start).count();

        also(rpt, "  ═══════════════════════════════════════════");
        also(rpt, "  MicroExchange — Simulation Report");
        also(rpt, "  ═══════════════════════════════════════════");
        also(rpt, "");
        also(rpt, "  Engine Statistics");
        also(rpt, "  ─────────────────────────────────────────");

        auto stats = engine.get_stats();
        also(rpt, "  Total orders:    " + std::to_string(stats.total_orders));
        also(rpt, "  Total trades:    " + std::to_string(stats.total_trades));
        also(rpt, "  Total volume:    " + std::to_string(stats.total_volume));
        also(rpt, "  Active orders:   " + std::to_string(stats.active_orders));

        auto fstats = feed.get_stats();
        also(rpt, "  Feed messages:   " + std::to_string(fstats.total_messages)
                  + " (A=" + std::to_string(fstats.add_count)
                  + " T=" + std::to_string(fstats.trade_count)
                  + " D=" + std::to_string(fstats.delete_count)
                  + " Q=" + std::to_string(fstats.quote_count) + ")");

        {
            std::ostringstream oss;
            oss << std::fixed << std::setprecision(2) << wall_sec;
            also(rpt, "  Wall time:       " + oss.str() + " sec");
        }
        {
            std::ostringstream oss;
            oss << std::fixed << std::setprecision(0) << events.size() / wall_sec;
            also(rpt, "  Throughput:      " + oss.str() + " events/sec");
        }

        also(rpt, "");
        also(rpt, "  Spread Decomposition (Huang-Stoll)");
        also(rpt, "  ─────────────────────────────────────────");

        auto fmt = [](double v) {
            std::ostringstream oss;
            oss << std::fixed << std::setprecision(2) << v;
            return oss.str();
        };

        also(rpt, "  Quoted spread:      " + fmt(spread_result.avg_quoted_spread) + " ticks");
        also(rpt, "  Effective spread:   " + fmt(spread_result.avg_effective_spread) + " ticks");
        also(rpt, "  Realized spread:    " + fmt(spread_result.avg_realized_spread) + " ticks");
        also(rpt, "  Price impact:       " + fmt(spread_result.avg_price_impact) + " ticks");
        also(rpt, "  Adverse selection:  " + fmt(spread_result.adverse_selection_pct) + "%");

        also(rpt, "");
        also(rpt, "  Kyle's Lambda");
        also(rpt, "  ─────────────────────────────────────────");
        {
            std::ostringstream oss;
            oss << std::scientific << std::setprecision(3) << kyle_result.lambda;
            also(rpt, "  lambda:   " + oss.str() + " (ticks per share, signed)");
        }
        also(rpt, "  R²:       " + fmt(kyle_result.r_squared));

        {
            std::ostringstream oss;
            oss << std::fixed << std::setprecision(1) << kyle_result.t_statistic;
            also(rpt, "  t-stat:   " + oss.str());
        }

        also(rpt, "  N:        " + std::to_string(kyle_result.num_intervals));

        also(rpt, "");
        also(rpt, "  Stylized Facts");
        also(rpt, "  ─────────────────────────────────────────");
        also(rpt, "  Excess kurtosis:     " + fmt(facts.return_kurtosis));
        also(rpt, "  AC(|r|, lag=1):      " + fmt(facts.abs_return_ac_lag1));
        also(rpt, "  AC(|r|, lag=5):      " + fmt(facts.abs_return_ac_lag5));
        also(rpt, "  AC(|r|, lag=10):     " + fmt(facts.abs_return_ac_lag10));

        also(rpt, "");
        for (const auto& fc : facts.fact_checks) {
            std::string status = fc.reproduced ? "  ✓ " : "  ✗ ";
            also(rpt, status + fc.name + " → " + fmt(fc.value) + " (benchmark: " + fc.benchmark + ")");
        }

        also(rpt, "");
        also(rpt, "  ═══════════════════════════════════════════");

        also(rpt, "");
        also(rpt, "  Output files:");
        also(rpt, "    " + cfg.out_dir + "/trades.csv");
        also(rpt, "    " + cfg.out_dir + "/midprices.csv");
        also(rpt, "    " + cfg.out_dir + "/spreads.csv");
        also(rpt, "    " + cfg.out_dir + "/report.txt");
        also(rpt, "");
    }

    return 0;
}
```

#### File: `core/tests/test_invariants.cpp`
```python
/**
 * test_invariants.cpp — Property-based tests for matching engine invariants.
 *
 * Tests verify the three core invariants that define a correct CLOB:
 *
 *   1. No crossed book: After every operation, best_bid < best_ask
 *   2. FIFO preserved: Within a price level, earlier orders fill first
 *   3. Determinism: Identical input → identical output on every run
 *
 * Additionally:
 *   4. Conservation: Trade qty matches on both sides
 *   5. Quantity consistency: filled_qty + leaves_qty == original qty
 *   6. No phantom orders: cancelled orders don't participate in matching
 *
 * Test methodology: property-based testing with random order streams.
 * Each test generates thousands of random events and checks invariants
 * after every single operation — not just at the end.
 */

#include "../include/MatchingEngine.h"
#include "../include/OrderBook.h"
#include "../include/Order.h"

#include <cassert>
#include <iostream>
#include <random>
#include <vector>
#include <string>
#include <algorithm>

using namespace micro_exchange::core;

// ─────────────────────────────────────────────
// Test helpers
// ─────────────────────────────────────────────

class RandomOrderGenerator {
public:
    explicit RandomOrderGenerator(uint64_t seed = 42)
        : rng_(seed), price_dist_(9900, 10100), qty_dist_(100, 1000),
          side_dist_(0, 1), type_dist_(0.0, 1.0)
    {}

    NewOrderRequest generate(OrderId id) {
        NewOrderRequest req{};
        req.id = id;
        req.side = side_dist_(rng_) ? Side::Buy : Side::Sell;
        req.price = price_dist_(rng_);
        req.quantity = (qty_dist_(rng_) / 100) * 100;  // Round to 100
        if (req.quantity == 0) req.quantity = 100;

        double type_roll = type_dist_(rng_);
        if (type_roll < 0.7) {
            req.type = OrderType::Limit;
            req.tif = TimeInForce::GTC;
        } else if (type_roll < 0.85) {
            req.type = OrderType::Market;
            req.tif = TimeInForce::IOC;
            req.price = PRICE_MARKET;
        } else {
            req.type = OrderType::IOC;
            req.tif = TimeInForce::IOC;
        }

        std::memcpy(req.symbol, "TEST", 5);
        return req;
    }

private:
    std::mt19937_64 rng_;
    std::uniform_int_distribution<Price> price_dist_;
    std::uniform_int_distribution<Quantity> qty_dist_;
    std::uniform_int_distribution<int> side_dist_;
    std::uniform_real_distribution<double> type_dist_;
};

// ─────────────────────────────────────────────
// Test 1: No Crossed Book
// ─────────────────────────────────────────────

void test_no_crossed_book() {
    std::cout << "TEST: No crossed book invariant... ";

    OrderBook book("TEST");
    RandomOrderGenerator gen(12345);

    for (OrderId id = 1; id <= 50000; ++id) {
        auto req = gen.generate(id);
        book.add_order(req);

        // Check invariant after EVERY operation
        assert(book.check_no_crossed_book() &&
               "INVARIANT VIOLATED: Book is crossed after add_order!");
    }

    std::cout << "PASSED (50,000 random orders)\n";
}

// ─────────────────────────────────────────────
// Test 2: FIFO Priority
// ─────────────────────────────────────────────

void test_fifo_priority() {
    std::cout << "TEST: FIFO priority invariant... ";

    OrderBook book("TEST");

    // Place multiple orders at the same price
    for (OrderId id = 1; id <= 10; ++id) {
        NewOrderRequest req{};
        req.id = id;
        req.side = Side::Buy;
        req.type = OrderType::Limit;
        req.tif = TimeInForce::GTC;
        req.price = 10000;
        req.quantity = 100;
        std::memcpy(req.symbol, "TEST", 5);
        book.add_order(req);
    }

    // Send a sell market order that partially fills
    std::vector<OrderId> fill_order;
    book.set_trade_callback([&](const Trade& trade) {
        fill_order.push_back(trade.buy_order_id);
    });

    NewOrderRequest sell{};
    sell.id = 100;
    sell.side = Side::Sell;
    sell.type = OrderType::Market;
    sell.tif = TimeInForce::IOC;
    sell.price = PRICE_MARKET;
    sell.quantity = 300;  // Fill first 3 orders
    std::memcpy(sell.symbol, "TEST", 5);
    book.add_order(sell);

    // Verify FIFO: orders 1, 2, 3 should have filled (in that order)
    assert(fill_order.size() == 3);
    assert(fill_order[0] == 1);
    assert(fill_order[1] == 2);
    assert(fill_order[2] == 3);

    // Verify FIFO invariant in remaining book
    assert(book.check_fifo_invariant());

    std::cout << "PASSED\n";
}

// ─────────────────────────────────────────────
// Test 3: Determinism
// ─────────────────────────────────────────────

void test_determinism() {
    std::cout << "TEST: Deterministic matching... ";

    auto run_simulation = [](uint64_t seed) -> std::vector<Trade> {
        OrderBook book("TEST");
        RandomOrderGenerator gen(seed);
        std::vector<Trade> trades;

        book.set_trade_callback([&](const Trade& trade) {
            trades.push_back(trade);
        });

        for (OrderId id = 1; id <= 10000; ++id) {
            auto req = gen.generate(id);
            book.add_order(req);
        }

        return trades;
    };

    // Run twice with same seed
    auto trades1 = run_simulation(999);
    auto trades2 = run_simulation(999);

    // Must produce identical results
    assert(trades1.size() == trades2.size() &&
           "Determinism failed: different number of trades");

    for (size_t i = 0; i < trades1.size(); ++i) {
        assert(trades1[i].price == trades2[i].price &&
               "Determinism failed: different trade prices");
        assert(trades1[i].quantity == trades2[i].quantity &&
               "Determinism failed: different trade quantities");
        assert(trades1[i].buy_order_id == trades2[i].buy_order_id &&
               "Determinism failed: different buyer");
        assert(trades1[i].sell_order_id == trades2[i].sell_order_id &&
               "Determinism failed: different seller");
    }

    std::cout << "PASSED (" << trades1.size() << " trades matched identically)\n";
}

// ─────────────────────────────────────────────
// Test 4: Conservation of Quantity
// ─────────────────────────────────────────────

void test_conservation() {
    std::cout << "TEST: Quantity conservation... ";

    OrderBook book("TEST");
    RandomOrderGenerator gen(777);

    uint64_t total_trade_volume = 0;
    book.set_trade_callback([&](const Trade& trade) {
        total_trade_volume += trade.quantity;
    });

    std::vector<Order*> all_orders;
    for (OrderId id = 1; id <= 20000; ++id) {
        auto req = gen.generate(id);
        Order* order = book.add_order(req);
        all_orders.push_back(order);
    }

    // Verify: total volume from trade callbacks == total filled across all orders
    // (marked maybe_unused: only read inside assert(), which NDEBUG compiles out)
    [[maybe_unused]] uint64_t total_filled = 0;
    for (const auto* order : all_orders) {
        assert(order->filled_qty + order->leaves_qty <= order->quantity ||
               order->status == OrderStatus::Cancelled);
        total_filled += order->filled_qty;
    }

    // Each trade fills two sides, so total_filled should be 2 * total_trade_volume
    assert(total_filled == 2 * total_trade_volume &&
           "Conservation violated: filled qty != 2 * trade volume");

    std::cout << "PASSED (volume conserved across " << total_trade_volume << " units)\n";
}

// ─────────────────────────────────────────────
// Test 5: Cancel correctness
// ─────────────────────────────────────────────

void test_cancel_correctness() {
    std::cout << "TEST: Cancel correctness... ";

    OrderBook book("TEST");

    // Place a buy order
    NewOrderRequest buy{};
    buy.id = 1;
    buy.side = Side::Buy;
    buy.type = OrderType::Limit;
    buy.tif = TimeInForce::GTC;
    buy.price = 10000;
    buy.quantity = 500;
    std::memcpy(buy.symbol, "TEST", 5);
    book.add_order(buy);

    assert(book.active_orders() == 1);

    // Cancel it
    bool cancelled = book.cancel_order(1);
    (void)cancelled;
    assert(cancelled && "Cancel should succeed");
    assert(book.active_orders() == 0 && "No active orders after cancel");

    // Try to fill the cancelled order — should not match
    bool any_trade = false;
    book.set_trade_callback([&](const Trade&) { any_trade = true; });

    NewOrderRequest sell{};
    sell.id = 2;
    sell.side = Side::Sell;
    sell.type = OrderType::Market;
    sell.tif = TimeInForce::IOC;
    sell.price = PRICE_MARKET;
    sell.quantity = 500;
    std::memcpy(sell.symbol, "TEST", 5);
    book.add_order(sell);

    assert(!any_trade && "Cancelled order should not be filled");

    // Double cancel should fail
    assert(!book.cancel_order(1) && "Double cancel should return false");

    std::cout << "PASSED\n";
}

// ─────────────────────────────────────────────
// Test 6: Fuzz test with invariant checks
// ─────────────────────────────────────────────

void test_fuzz_random_sequence() {
    std::cout << "TEST: Fuzz random event sequence... ";

    OrderBook book("TEST");
    std::mt19937_64 rng(54321);
    std::uniform_int_distribution<int> action_dist(0, 9);
    std::uniform_int_distribution<Price> price_dist(9950, 10050);
    std::uniform_int_distribution<Quantity> qty_dist(1, 10);

    OrderId next_id = 1;
    std::vector<OrderId> active_ids;

    for (int i = 0; i < 100000; ++i) {
        int action = action_dist(rng);

        if (action < 7) {
            // 70%: new order
            NewOrderRequest req{};
            req.id = next_id++;
            req.side = (rng() % 2) ? Side::Buy : Side::Sell;
            req.type = (rng() % 5 == 0) ? OrderType::Market : OrderType::Limit;
            req.tif = (req.type == OrderType::Market) ? TimeInForce::IOC : TimeInForce::GTC;
            req.price = (req.type == OrderType::Market) ? PRICE_MARKET : price_dist(rng);
            req.quantity = qty_dist(rng) * 100;
            std::memcpy(req.symbol, "TEST", 5);

            Order* order = book.add_order(req);
            if (order->is_active()) {
                active_ids.push_back(order->id);
            }
        } else if (action < 9 && !active_ids.empty()) {
            // 20%: cancel
            size_t idx = rng() % active_ids.size();
            book.cancel_order(active_ids[idx]);
            active_ids.erase(active_ids.begin() + idx);
        } else if (!active_ids.empty()) {
            // 10%: amend
            size_t idx = rng() % active_ids.size();
            AmendRequest amend{};
            amend.order_id = active_ids[idx];
            amend.new_quantity = qty_dist(rng) * 100;
            std::memcpy(amend.symbol, "TEST", 5);
            book.amend_order(amend);
        }

        // Check invariants after every operation
        assert(book.check_no_crossed_book() &&
               "FUZZ: Book crossed!");
    }

    std::cout << "PASSED (100,000 random events, invariants held)\n";
}

// ─────────────────────────────────────────────
// Test 7: Stop and StopLimit triggering
// ─────────────────────────────────────────────

namespace {

void seed_two_sided_book(OrderBook& book) {
    // Ten levels each side around 10000
    OrderId id = 1;
    for (int lvl = 1; lvl <= 10; ++lvl) {
        NewOrderRequest bid{};
        bid.id = id++;
        bid.side = Side::Buy;
        bid.type = OrderType::Limit;
        bid.tif = TimeInForce::GTC;
        bid.price = 10000 - lvl;
        bid.quantity = 500;
        std::memcpy(bid.symbol, "TEST", 5);
        book.add_order(bid);

        NewOrderRequest ask{};
        ask.id = id++;
        ask.side = Side::Sell;
        ask.type = OrderType::Limit;
        ask.tif = TimeInForce::GTC;
        ask.price = 10000 + lvl;
        ask.quantity = 500;
        std::memcpy(ask.symbol, "TEST", 5);
        book.add_order(ask);
    }
}

NewOrderRequest mk(OrderId id, Side s, OrderType t, Price p, Quantity q,
                   Price stop = 0) {
    NewOrderRequest r{};
    r.id = id;
    r.side = s;
    r.type = t;
    r.tif = (t == OrderType::Market || t == OrderType::IOC)
                ? TimeInForce::IOC : TimeInForce::GTC;
    r.price = p;
    r.stop_price = stop;
    r.quantity = q;
    std::memcpy(r.symbol, "TEST", 5);
    return r;
}

} // anon

void test_stop_market_triggers() {
    std::cout << "TEST: Stop (market) trigger... ";

    OrderBook book("TEST");
    seed_two_sided_book(book);

    // Buy stop @ 10005 — should arm but not fire (last trade = 0)
    book.add_order(mk(1000, Side::Buy, OrderType::Stop, 0, 200, 10005));
    assert(book.parked_stop_count() == 1);

    // Walk the print up through asks 10001..10005 (each level = 500 shares).
    // Two market buys of 1500 shares takes us to a print at 10005, which
    // crosses the 10005 stop trigger.
    book.add_order(mk(1001, Side::Buy, OrderType::Market, PRICE_MARKET, 1500));
    book.add_order(mk(1010, Side::Buy, OrderType::Market, PRICE_MARKET, 1100));

    assert(book.last_trade_price() >= 10005);
    assert(book.parked_stop_count() == 0 && "Stop should have unparked");
    assert(book.stop_triggered_count() == 1 && "Stop should have triggered exactly once");

    // Sell stop @ 9996 — should arm but not fire yet
    book.add_order(mk(1002, Side::Sell, OrderType::Stop, 0, 200, 9996));
    assert(book.parked_stop_count() == 1);

    // Walk the print down through bids until we cross 9996. The seeded
    // book had bids at 9999..9990 with 500 each — selling 2000 shares
    // takes us from 9999 down to a print at 9996.
    book.add_order(mk(1003, Side::Sell, OrderType::Market, PRICE_MARKET, 2000));
    assert(book.last_trade_price() <= 9996);
    assert(book.parked_stop_count() == 0);
    assert(book.stop_triggered_count() == 2);

    std::cout << "PASSED\n";
}

void test_stop_limit_triggers_and_rests() {
    std::cout << "TEST: StopLimit converts to resting limit... ";

    OrderBook book("TEST");
    seed_two_sided_book(book);

    // Buy StopLimit: trigger at 10004, limit price 10003. After triggering
    // we want it to rest as a passive bid at 10003 (i.e. *not* crossing the
    // book), which is the most interesting state to verify.
    book.add_order(mk(2000, Side::Buy, OrderType::StopLimit, 10003, 200, 10004));
    assert(book.parked_stop_count() == 1);

    // Walk the print up to 10004 by consuming asks at 10001..10003 (500 each)
    // and partially consuming 10004.
    book.add_order(mk(2001, Side::Buy, OrderType::Market, PRICE_MARKET, 1500));
    book.add_order(mk(2002, Side::Buy, OrderType::Market, PRICE_MARKET, 100));
    assert(book.last_trade_price() >= 10004);
    assert(book.parked_stop_count() == 0);
    assert(book.stop_triggered_count() == 1);

    // The released order has limit price 10003. Best ask now is 10004,
    // so the limit cannot cross — it should rest as the new best bid.
    assert(book.best_bid().value_or(0) == 10003 &&
           "StopLimit should rest at its limit price");

    std::cout << "PASSED\n";
}

void test_stop_cancel() {
   
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: HFT-Races (`PHASE4-QUANT-108`)
- **Full Name**: `PHASE4-QUANT-108_ericbudish__HFT-Races`
- **Description**: Code package to analyze high-frequency trading (HFT) races using financial-exchange message data, following Aquilina, Budish and O'Neill (2021).
- **GitHub Stars**: 47
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# HFT-Races

This repository contains code for researchers, regulators or practitioners who wish to use financial-exchange message data to quantify latency arbitrage and study other aspects of speed-sensitive trading, following Matteo Aquilina, Eric Budish and Peter O’Neill, [“Quantifying the High-Frequency Trading ‘Arms Race’”](https://faculty.chicagobooth.edu/eric.budish/research/Quantifying-HFT-Races.pdf), Quarterly Journal of Economics, 2021 (hereafter, “ABO”). The Python code processes the user's message data, detects trading races, and outputs a race-level statistical dataset along with complementary trading data. The R code produces race summary statistics, tables and figures analogous to all reported results in ABO. We also provide a small artificial data set that can be used to understand the data structure and to test one's configuration.

This code should be used in conjunction with the detailed documentation linked below. 

## About

Version 1.1 (November 2021). Please visit [https://github.com/ericbudish/HFT-Races](https://github.com/ericbudish/HFT-Races) to check for updates. 

## Documentation

Please refer to [ABO Code and Data Appendix](Code_and_Data_Appendix.pdf) for detailed documentation and instructions.

## Quick Start

1. Download and unzip this repository. Obtain the exchange message data and pre-process the data following Sections 2 and 3 of the [ABO Code and Data Appendix](Code_and_Data_Appendix.pdf). You may want to use the artificial dataset provided [here](ArtificialTestData/2000-01-01) to test your configuration first. 
2. Decide on the set of race detection parameters as instructed in Section 4 of the appendix. You can use the sample race detection parameters provided [here](ArtificialTestData/Sample_Input_Race_Parameters.csv) for testing.
3. Make sure Python 3 is installed on your MacOS/Linux system. For Windows users, we recommend using the Windows Subsystem for Linux. Please refer to Section 5 of the appendix for a complete guide on computational environment setup. Install Pandas and Numpy using the following command if you have not.
```
pip install -r requirements.txt # Install the required Python packages
``` 
4. Specify the parameters and file paths in [`process_msg_data_main.py`](PythonCode/process_msg_data_main.py) and run the script in the console using the command below. To test your configuration, set the file paths accordingly to use the artificial test data provided [here](ArtificialTestData). Please refer to Section 6 of the ABO Code and Data Appendix.  
```
nohup python3 path/to/code/process_msg_data_main.py > path/to/main/log/run.log 2>&1&
```
5. Specify the parameters and file paths in [`race_detection_main.py`](PythonCode/race_detection_main.py) and run the script in the console using the command below. To test your configuration, set the file paths accordingly to use the artificial test data provided [here](ArtificialTestData).  Please refer to Section 7 of the ABO Code and Data Appendix. 
```
nohup python3 path/to/code/race_detection_main.py > path/to/main/log/run.log 2>&1&
```
6. Use [`log_monitor.py`](PythonCode/log_monitor.py) to make sure all data have been processed. Follow the instructions in `log_monitor.py` and execute the code interactively or in a console.
```
python3 path/to/code/log_monitor.py
``` 
7. Specify the parameters and file paths in [`MainResults.R`](RCode/MainResults.R) and [`Sensitivity.R`](RCode/Sensitivity.R) and source the scripts. If you have multiple sets of race detection parameters, you may need to repeat this step multiple times for different sets of race detection results.
```
Rscript /path/to/MainResults.R
Rscript /path/to/RCode.R
```

## Feedback 

We would be grateful for feedback or comments on the code, and are especially eager to hear from early users. Please address comments, questions, and any other feedback to [eric.budish@chicagobooth.edu](mailto:eric.budish@chicagobooth.edu) and [hft.races.code.package@gmail.com](mailto:hft.races.code.package@gmail.com).

## Credits 

Code credits: Jiahao Chen, Natalia Drozdoff, Matthew O'Keefe, Jaume Vives, Zizhe Xia, Matteo Aquilina, Eric Budish, Peter O'Neill 

Documentation credits: Jiahao Chen, Zizhe Xia, Matteo Aquilina, Eric Budish, Peter O'Neill

## License

The Python code and documentation are licensed under the BSD 3-Clause license. License is available [here](LICENSE).

The R code is licensed under the GNU General Public License version 3 due to the use of GNU GPL licensed R packages. License is available [here](RCode/LICENSE-RCode)

### Core Implementation Code & Architecture
#### File: `PythonCode/LatencyArbitrageAnalysis/__init__.py`
```python

```

#### File: `PythonCode/LatencyArbitrageAnalysis/utils/__init__.py`
```python

```

#### File: `PythonCode/LatencyArbitrageAnalysis/OrderBook/__init__.py`
```python

```

#### File: `PythonCode/LatencyArbitrageAnalysis/RaceDetection/__init__.py`
```python

```

#### File: `PythonCode/LatencyArbitrageAnalysis/utils/Logger.py`
```python
'''
Logger.py

Defines the logger object.
'''

import logging
import sys

class LoggerWriter(object):
    def __init__(self, logger, level = logging.WARNING):
        self.logger = logger
        self.level = level
        
    def write(self, message):
        for line in message.rstrip().splitlines():
            self.logger.log(self.level, line.rstrip())
    
    def flush(self):
        pass

def getLogger(logpath, logfile, name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(logpath + logfile)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    sys.stdout = LoggerWriter(logger, logging.WARNING)
    sys.stderr = LoggerWriter(logger, logging.ERROR)
    return logger
```

#### File: `PythonCode/data_validation.py`
```python
'''
data_validation.py

This script checks whether the pre-processed data meets the requirements of 
the package. We strongly recommend users validate the pre-processed data before 
applying the package.

Reference: 
Code and Data Appendix for “Quantifying the High-Frequency Trading
‘Arms Race’: A Simple New Methodology and Estimates” 
by Matteo Aquilina, Eric Budish and Peter O’Neill

Please follow the instructions in this file and 
Section 5.3 of the Code and Data Appendix.

'''
###################################################################################
### Load modules
from LatencyArbitrageAnalysis.utils.Validate_Data import ValidateData
###################################################################################
### Specify paths and symbol-date pairs to be checked
# Path to the pre-processed data files
path_data = '/path/to/pre-processed/RawData/'
# Symbol-dates to be checked
# testing_pairs - list of (date, sym) pairs to be checked
# Each item in the list is a python 2-tuple: e.g., 
# [('2000-01-01', 'ABCD'), ('2000-01-01', 'EFGH')].
# You can first obtain all symbol-date pairs and then 
# choose to validate all or a subset of symbol-dates:
# pairs = pd.read_csv(file_symdates, dtype={'Date':'O','Symbol':'O'})[['Date','Symbol']].dropna().to_records(index=False).tolist()
# testing_pairs = # All or a subset of pairs
testing_pairs = [('2000-01-01','ABCD')] 
###################################################################################
### Data Validation
failed = []
for date, sym in testing_pairs:
      test = ValidateData(date, sym, path_data)
      failed.append(test.validate())
if any(failed):
      print('Data failed to pass some validation tests. Please check the data requirements and be careful to proceed.')
else:
      print('Data validated.')
```


==================================================


## [3/3] Repository: crypto-liquidity-ai-trading-bot (`PHASE4-QUANT-103`)
- **Full Name**: `PHASE4-QUANT-103_aitradingbotspro__crypto-liquidity-ai-trading-bot`
- **Description**: Crypto liquidity detection & algorithmic trading bot. Order book analysis, stop-loss clusters, liquidity sweeps. Multi-exchange (Binance, Bybit, Kraken, OKX). Trading signals, quant research, market microstructure.
- **GitHub Stars**: 68
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Crypto Liquidity AI Trading Bot 🚀

**AI trading bot** for liquidity detection and algorithmic trading in crypto markets. Detect order book gaps, hidden walls, and liquidity sweeps across exchanges—then act on signals manually or via your own execution layer.

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![Stars](https://img.shields.io/github/stars/asonglin/crypto-liquidity-ai-trading-bot)](https://github.com/asonglin/crypto-liquidity-ai-trading-bot/stargazers)

![Crypto Liquidity AI Trading Bot](assets/image.png)

<details>
<summary><strong>📋 Table of contents</strong></summary>

- [Why liquidity matters](#why-liquidity-matters)
- [Who this is for](#who-this-is-for)
- [Commercial use](#commercial-use)
- [Backtest performance](#backtest-performance)
- [Strategy concept](#strategy-concept)
- [Architecture](#architecture)
- [Quick start](#quick-start)
- [What you get](#what-you-get)
- [How liquidity hunting works](#how-liquidity-hunting-works)
- [Installation](#installation)
- [Supported exchanges](#supported-exchanges)
- [Project layout](#project-layout)
- [Use cases](#use-cases)
- [Related projects](#related-projects)
- [FAQ](#faq)
- [Contributing](#contributing)

</details>

---

## Why liquidity matters

Most crypto trading bots rely only on **price and technical indicators**. Professional traders, however, monitor **order book liquidity**, because price often moves toward zones where liquidity is concentrated—and away when that liquidity is swept.

This project focuses on **liquidity-aware trading signals** instead of lagging indicators: it detects gaps, walls, and sweeps so you can act on structure, not just price.

---

## Who this is for

This project may be useful for:

- **Crypto trading firms** building in-house liquidity and execution tools  
- **Quant researchers** studying order book and market microstructure  
- **Exchanges** building surveillance or liquidity analytics  
- **Developers** building AI trading agents or signal systems  

---

## Commercial use

If you are interested in **custom crypto trading bots** (liquidity, arbitrage, execution), **AI trading signal systems**, or **liquidity detection algorithms** and exchange API integrations:

**For collaboration or development work:**

- **GitHub** — [Open an issue](https://github.com/asonglin/crypto-liquidity-ai-trading-bot/issues)
- **Telegram** — [@jjcunningham](https://t.me/jjcunningham)
- **Email** — jj.cunningham1129@gmail.com

---

## Backtest performance

Results below are from a **historical** backtest using order-book and liquidity-sweep signals on major spot pairs. They are not live trading results.

**Test configuration**

| Parameter | Value |
|-----------|--------|
| Window | Jan 2024 – Dec 2024 |
| Length | 12 months |
| Asset class | Cryptocurrency (spot) |
| Approach | Liquidity-sweep & order-book imbalance |
| Style | Medium frequency, signal-driven |
| Pairs | BTC/USDT, ETH/USDT, selected alts |
| Execution | Simulated limit/market fills |

**Performance metrics**

| Metric | Result |
|--------|--------|
| Win rate | 58.2% |
| Profit factor | 1.42 |
| Max drawdown | −12.4% |
| Sharpe ratio (daily) | 1.18 |

**What this suggests**

- **Win rate &gt; 50%** suggests the liquidity-based signals add information over a random baseline.
- **Profit factor &gt; 1.2** indicates positive expectancy in the simulated period.
- **Sharpe &gt; 1.0** points to reasonable risk-adjusted returns in the backtest; **max drawdown −12.4%** is a measure of tail risk in the tested period.

**Limitations**

Actual results can differ from backtests due to fees, slippage, execution delay, and changing liquidity. Run your own tests and risk checks before any live use.

**Example signal (conceptual)**

```json
{
  "symbol": "BTC/USDT",
  "direction": "LONG",
  "strength": 0.61,
  "reason": "liquidity_sweep_detected",
  "ts": "2024-11-15T08:44:02Z"
}
```

---

## Strategy concept

**Price indicators lag. Liquidity moves first.**

Large orders and stop-loss clusters sit in the order book before price reaches them. When price sweeps those levels, liquidity is consumed and moves tend to accelerate. This bot identifies those levels and signals sweep events so you can trade with the flow instead of chasing price.

---

## Architecture

```
Market data (REST/WS)
        ↓
Order book analyzer
        ↓
Liquidity detector (gaps, walls, sweeps)
        ↓
Signal engine
        ↓
Alerts / optional execution layer
```

The codebase separates **data** (`modules/`, exchange APIs), **analysis** (`trade/` — orderbook, liquidity), and **signals/alerts** so you can plug in your own execution or research tools.

---

## Quick start

### Quick start (Node)

Run the main app with Node:

```bash
git clone https://github.com/asonglin/crypto-liquidity-ai-trading-bot.git && cd crypto-liquidity-ai-trading-bot
npm install
```

Edit `config.default.jsonc`, then:

```bash
node app.js
```

### Advanced research (Python optional)

For research, backtests, or a custom Python wrapper, use a venv and `requirements.txt`. See **Installation** below.

---

## What you get

| Capability | Description |
|------------|-------------|
| **Liquidity detection** | Scans order books and pools for depth, gaps, and imbalance. |
| **Hidden walls** | Surfaces large buy/sell walls and their changes. |
| **Multi-exchange** | Built to plug into Binance, Bybit, Kraken, OKX, and others. |
| **Alerts** | Configurable notifications when liquidity events fire. |
| **Trading framework** | Modular so you can add execution, risk, or dashboards. |

Use it for **liquidity grabs**, **order book imbalance strategies**, **market microstructure research**, and **algorithmic trading**—whether you trade manually or automate.

---

## How liquidity hunting works

Liquidity hunting targets zones where lots of orders sit (e.g. stop-loss clusters). When price sweeps those levels, liquidity is “taken” and price can move fast. This bot helps you find and watch those zones.

1. **Find** where large stop-loss clusters or thin book zones sit.  
2. **Detect** liquidity sweeps and wall removals in real time.  
3. **Alert** so you can enter when liquidity is taken or book vacuum appears.  
4. **Extend** with your own execution (manual or automated).

Signals you can get: *stop-loss clusters*, *sudden order book vacuum*, *liquidity wall removal*, *aggressive market order flow*.

---

## Installation

```bash
git clone https://github.com/asonglin/crypto-liquidity-ai-trading-bot.git
cd crypto-liquidity-ai-trading-bot
```

**Quick start (Node)** — main engine:

```bash
npm install
# Edit config.default.jsonc, then:
node app.js
```

**Advanced research (Python optional)** — venv and scripts:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Example: scanning and alerts

```javascript
// App entry is app.js; configure API keys and exchanges in config.
// Core logic lives in trade/ (liquidity, orderbook) and modules/ (api, DB).
```

```python
# If using a Python wrapper:
from liquidity_hunting import LiquidityBot
bot = LiquidityBot(api_key="YOUR_API_KEY", secret="YOUR_SECRET")
bot.scan_liquidity()
bot.generate_alerts()
```

---

## Supported exchanges

Extensible to any exchange with a REST/WS API. Commonly used with:

| Exchange | Notes |
|----------|--------|
| Binance | Spot & futures. |
| Bybit | Derivatives. |
| Kraken | Spot. |
| OKX | Spot & derivatives. |
| Coinbase | Spot. |
| Hyperliquid | Perps. |

---

## Project layout

```
crypto-liquidity-ai-trading-bot/
├── app.js                 # entry point
├── config.default.jsonc   # config template
├── package.json
├── helpers/               # shared utils, crypto helpers
├── modules/               # api, DB, config, transactions
├── routes/                # debug, health, init
├── trade/                 # liquidity provider, orderbook, traders, exchange APIs
├── types/                 # TypeScript declarations
├── utils/
└── assets/
```

---

## Use cases

- **Crypto algorithmic trading** — Feed signals into your execution engine.  
- **Quant research** — Order book and liquidity analysis.  
- **AI/ML strategy dev** — Use liquidity events as features or triggers.  
- **Market microstructure** — Study gaps, walls, and sweep behavior.

---

## Related projects

Part of the same AI trading bot suite:

- [Crypto Futures AI Trading Bot](https://github.com/asonglin/crypto-futures-ai-trading-bot) — AI trading bot for funding arbitrage and smart-money monitoring
- [Cross-Exchange AI Arbitrage Bot](https://github.com/asonglin/cross-exchange-ai-arbitrage-bot) — AI trading bot for CEX/DEX spread detection and execution

---

## FAQ

**What is liquidity hunting?**  
A strategy that focuses on levels where lots of stop-loss or passive orders sit; when those levels are hit, liquidity is consumed and price often moves sharply.

**Is the bot fully automated?**  
It focuses on **detection and alerts**. You can add automated execution yourself or use signals for manual trading.

**Who is it for?**  
Developers, quants, and algo traders who want liquidity-aware signals and a clear, extensible codebase (Node/JS, optional Python).

---

## Contributing

We welcome pull requests and issues. Fork → branch → PR. See CONTRIBUTING.md if present.

**License:** MIT © 2026

### Core Implementation Code & Architecture
#### File: `tsconfig.json`
```python
jsconfig.json
```

#### File: `babel.config.json`
```python
{
  "presets": ["@babel/preset-env"],
  "plugins": [
      ["@babel/transform-runtime"]
  ]
}
```

#### File: `jsconfig.json`
```python
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true,
    "lib": [
      "es5", "es6", "dom", "dom.iterable"
    ],
    "module": "Node16",
    "moduleResolution": "Node16",
    "paths": {
      "types/*": ["./types/*"]
    },
    "target": "ES6"
  },
  "exclude": ["node_modules"],
  "include": ["**/*.js"]
}
```

#### File: `package.json`
```python
{
  "name": "adamant-tradebot",
  "version": "7.0.1",
  "description": "ADAMANT's self-hosted market-making bot for crypto projects & token issuers. Volume, spread, liquidity, price ranges, and dynamic order books.",
  "main": "index.js",
  "scripts": {
    "lint": "npx eslint -f visualstudio .",
    "lint:fix": "npx eslint -f visualstudio --fix",
    "lint:fixrule": "npx eslint -f visualstudio --no-eslintrc --fix --env node,es2021,commonjs --parser-options=ecmaVersion:12 --rule",
    "start": "node app.js",
    "start:dev": "node app.js dev",
    "clear": "node app.js dev clear_db",
    "test": "jest"
  },
  "keywords": [
    "market-making",
    "market making",
    "trading bot",
    "self-hosted",
    "trading volume",
    "bot",
    "bitcoin",
    "ethereum",
    "trading",
    "trade",
    "order book",
    "orderbook",
    "exchange",
    "arbitrage",
    "crypto",
    "cryptocurrency",
    "spread",
    "liquidity",
    "target price",
    "price watching",
    "making price"
  ],
  "author": "ADAMANT Developer Community <devs@adamant.im> (https://adamant.im)",
  "license": "GPL-3.0",
  "dependencies": {
    "adamant-api": "^2.4.0",
    "axios": "^1.11.0",
    "deep-object-diff": "^1.1.9",
    "express": "^4.21.2",
    "fast-deep-equal": "^3.1.3",
    "form-data": "^4.0.4",
    "jsonminify": "^0.4.2",
    "mongodb": "^6.19.0",
    "uuid": "^12.0.0"
  },
  "devDependencies": {
    "@babel/core": "^7.28.4",
    "@babel/eslint-parser": "^7.28.4",
    "@babel/plugin-transform-runtime": "^7.28.3",
    "@babel/preset-env": "^7.28.3",
    "@eslint/js": "^9.35.0",
    "eslint": "^9.35.0",
    "eslint-config-google": "^0.14.0",
    "eslint-formatter-visualstudio": "^8.40.0",
    "globals": "^16.3.0",
    "jest": "^30.1.3",
    "nodemon": "^3.1.10"
  },
  "engines": {
    "node": ">=18.18",
    "npm": ">=9.0.1"
  },
  "publishConfig": {
    "access": "public"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Adamant-im/adamant-tradebot.git"
  },
  "bugs": {
    "url": "https://github.com/Adamant-im/adamant-tradebot/issues"
  },
  "homepage": "https://marketmaking.app"
}
```

#### File: `package-lock.json`
```python
{
  "name": "adamant-tradebot",
  "version": "7.0.1",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "adamant-tradebot",
      "version": "7.0.1",
      "license": "GPL-3.0",
      "dependencies": {
        "adamant-api": "^2.4.0",
        "axios": "^1.11.0",
        "deep-object-diff": "^1.1.9",
        "express": "^4.21.2",
        "fast-deep-equal": "^3.1.3",
        "form-data": "^4.0.4",
        "jsonminify": "^0.4.2",
        "mongodb": "^6.19.0",
        "uuid": "^12.0.0"
      },
      "devDependencies": {
        "@babel/core": "^7.28.4",
        "@babel/eslint-parser": "^7.28.4",
        "@babel/plugin-transform-runtime": "^7.28.3",
        "@babel/preset-env": "^7.28.3",
        "@eslint/js": "^9.35.0",
        "eslint": "^9.35.0",
        "eslint-config-google": "^0.14.0",
        "eslint-formatter-visualstudio": "^8.40.0",
        "globals": "^16.3.0",
        "jest": "^30.1.3",
        "nodemon": "^3.1.10"
      },
      "engines": {
        "node": ">=18.18",
        "npm": ">=9.0.1"
      }
    },
    "node_modules/@aashutoshrathi/word-wrap": {
      "version": "1.2.6",
      "resolved": "https://registry.npmjs.org/@aashutoshrathi/word-wrap/-/word-wrap-1.2.6.tgz",
      "integrity": "sha512-1Yjs2SvM8TflER/OD3cOjhWWOZb58A2t7wpE2S9XfBYTiIl+XFhQG2bjy4Pu1I+EAlCNUzRDYDdFwFYUKvXcIA==",
      "dev": true,
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.27.1.tgz",
      "integrity": "sha512-cjQ7ZlQ0Mv3b47hABuTevyTuYN4i+loJKGeV9flcCgIK37cCXRh+L1bd3iBHlynerhQ7BhCkn2BPbQUL+rGqFg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.27.1",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.28.4.tgz",
      "integrity": "sha512-YsmSKC29MJwf0gF8Rjjrg5LQCmyh+j/nD8/eP7f+BeoQTKYqs9RoWbjGOdy0+1Ekr68RJZMUOPVQaQisnIo4Rw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.28.4.tgz",
      "integrity": "sha512-2BCOP7TN8M+gVDj7/ht3hsaO/B/n5oDbiAyyvnRlNOs+u1o+JWNYTQrmpuNp1/Wq2gcFrI01JAW+paEKDMx/CA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.3",
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-module-transforms": "^7.28.3",
        "@babel/helpers": "^7.28.4",
        "@babel/parser": "^7.28.4",
        "@babel/template": "^7.27.2",
        "@babel/traverse": "^7.28.4",
        "@babel/types": "^7.28.4",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/eslint-parser": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/eslint-parser/-/eslint-parser-7.28.4.tgz",
      "integrity": "sha512-Aa+yDiH87980jR6zvRfFuCR1+dLb00vBydhTL+zI992Rz/wQhSvuxjmOOuJOgO3XmakO6RykRGD2S1mq1AtgHA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nicolo-ribaudo/eslint-scope-5-internals": "5.1.1-v1",
        "eslint-visitor-keys": "^2.1.0",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": "^10.13.0 || ^12.13.0 || >=14.0.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.11.0",
        "eslint": "^7.5.0 || ^8.0.0 || ^9.0.0"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.28.3.tgz",
      "integrity": "sha512-3lSpxGgvnmZznmBkCRnVREPUFJv2wrv9iAoFDvADJc0ypmdOxdUtcLeBgBJ6zE0PMeTKnxeQzyk0xTBq4Ep7zw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.3",
        "@babel/types": "^7.28.2",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-annotate-as-pure": {
      "version": "7.27.3",
      "resolved": "https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.27.3.tgz",
      "integrity": "sha512-fXSwMQqitTGeHLBC08Eq5yXz2m37E4pJX1qAU1+2cNedz/ifv/bVXft90VeSav5nFO61EcNgwr0aJxbyPaWBPg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.27.3"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.27.2",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.27.2.tgz",
      "integrity": "sha512-2+1thGUUWWjLTYTHZWK1n8Yga0ijBz1XAhUXcKy81rd5g6yh7hGqMp45v7cadSbEHc9G3OTv45SyneRN3ps4DQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.27.2",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-create-class-features-plugin": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/helper-create-class-features-plugin/-/helper-create-class-features-plugin-7.28.3.tgz",
      "integrity": "sha512-V9f6ZFIYSLNEbuGA/92uOvYsGCJNsuA8ESZ4ldc09bWk/j8H8TKiPw8Mk1eG6olpnO0ALHJmYfZvF4MEE4gajg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-annotate-as-pure": "^7.27.3",
        "@babel/helper-member-expression-to-functions": "^7.27.1",
        "@babel/helper-optimise-call-expression": "^7.27.1",
        "@babel/helper-replace-supers": "^7.27.1",
        "@babel/helper-skip-transparent-expression-wrappers": "^7.27.1",
        "@babel/traverse": "^7.28.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-create-regexp-features-plugin": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.27.1.tgz",
      "integrity": "sha512-uVDC72XVf8UbrH5qQTc18Agb8emwjTiZrQE11Nv3CuBEZmVvTwwE9CBUEvHku06gQCAyYf8Nv6ja1IN+6LMbxQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-annotate-as-pure": "^7.27.1",
        "regexpu-core": "^6.2.0",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-define-polyfill-provider": {
      "version": "0.6.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-define-polyfill-provider/-/helper-define-polyfill-provider-0.6.5.tgz",
      "integrity": "sha512-uJnGFcPsWQK8fvjgGP5LZUZZsYGIoPeRjSF5PGwrelYgq7Q15/Ft9NGFp1zglwgIv//W0uG4BevRuSJRyylZPg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-plugin-utils": "^7.27.1",
        "debug": "^4.4.1",
        "lodash.debounce": "^4.0.8",
        "resolve": "^1.22.10"
      },
      "peerDependencies": {
        "@babel/core": "^7.4.0 || ^8.0.0-0 <8.0.0"
      }
    },
    "node_modules/@babel/helper-define-polyfill-provider/node_modules/debug": {
      "version": "4.4.1",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.1.tgz",
      "integrity": "sha512-KcKCqiftBJcZr++7ykoDIEwSa3XWowTfNPo92BYxjXiyYEVrUQh2aLyhxBCwww+heortUFxEJYcRzosstTEBYQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-member-expression-to-functions": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.27.1.tgz",
      "integrity": "sha512-E5chM8eWjTp/aNoVpcbfM7mLxu9XGLWYise2eBKGQomAk/Mb4XoxyqXTZbuTohbsl8EKqdlMhnDI2CCLfcs9wA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.27.1.tgz",
      "integrity": "sha512-0gSFWUPNXNopqtIPQvlD5WgXYI5GY2kP2cCvoT8kczjbfcfuIljTbcWrulD1CIPIX2gt1wghbDy08yE1p+/r3w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.3.tgz",
      "integrity": "sha512-gytXUbs8k2sXS9PnQptz5o0QnpLL51SwASIORY6XaBKF88nsOT0Zw9szLqlSGQDP/4TljBAD5y98p2U1fqkdsw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1",
        "@babel/traverse": "^7.28.3"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-optimise-call-expression": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.27.1.tgz",
      "integrity": "sha512-URMGH08NzYFhubNSGJrpUEphGKQwMQYBySzat5cAByY1/YgIRkULnIy3tAMeszlL/so2HbeilYloUmSpd7GdVw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.27.1.tgz",
      "integrity": "sha512-1gn1Up5YXka3YYAHGKpbideQ5Yjf1tDa9qYcgysz+cNCXukyLl6DjPXhD3VRwSb8c0J9tA4b2+rHEZtc6R0tlw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-remap-async-to-generator": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.27.1.tgz",
      "integrity": "sha512-7fiA521aVw8lSPeI4ZOD3vRFkoqkJcS+z4hFo82bFSH/2tNd6eJ5qCVMS5OzDmZh/kaHQeBaeyxK6wljcPtveA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-annotate-as-pure": "^7.27.1",
        "@babel/helper-wrap-function": "^7.27.1",
        "@babel/traverse": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-replace-supers": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.27.1.tgz",
      "integrity": "sha512-7EHz6qDZc8RYS5ElPoShMheWvEgERonFCs7IAonWLLUTXW59DP14bCZt89/GKyreYn8g3S83m21FelHKbeDCKA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-member-expression-to-functions": "^7.27.1",
        "@babel/helper-optimise-call-expression": "^7.27.1",
        "@babel/traverse": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-skip-transparent-expression-wrappers": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-skip-transparent-expression-wrappers/-/helper-skip-transparent-expression-wrappers-7.27.1.tgz",
      "integrity": "sha512-Tub4ZKEXqbPjXgWLl2+3JpQAYBJ8+ikpQ2Ocj/q/r0LwE3UhENh7EUabyHjz2kCEsrRY83ew2DQdHluuiDQFzg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.27.1.tgz",
      "integrity": "sha512-D2hP9eA+Sqx1kBZgzxZh0y1trbuU+JoDkiEwqhQ36nodYqJwyEIhPSdMNd7lOm/4io72luTPWH20Yda0xOuUow==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
      "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-wrap-function
# ... [TRUNCATED FILE CONTENT]
```


==================================================
