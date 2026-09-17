# ⚡ [QUANT-SOURCE-186] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_186_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: flowforge (`PHASE4-QUANT-026`)
- **Full Name**: `PHASE4-QUANT-026_jialuechen__flowforge`
- **Description**: Algo Library for Order Flow Inference and TCA
- **GitHub Stars**: 143
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# FlowForge

Python package pairing two engines for metaorder research: a **generation
engine** that forward-simulates institutional order flow via mean-variance
optimization on tunable alpha signals,
producing millions of labeled orders switchable between informed and
uninformed flow for execution algo testing and causal A/B experiments at
zero trading cost; and an **impact engine** that reconstructs realistic
metaorders from public trade data via randomized trader mapping, recovering
proprietary-grade stylized facts (Square Root Law, concave execution
profiles, impact decay) and removing the proprietary-data barrier to
impact research.

## Install

```bash
pip install -e .
```

Dependencies: numpy, pandas, scipy.

## Engine 1 — order flow generation (`flowforge.generate`)

Each period a bootstrap alpha vector `alpha = rho * r + sqrt(1-rho^2) * z`
(information coefficient ≈ `rho` by construction) feeds a mean-variance
problem with quadratic transaction costs. The closed-form solution is a
Garleanu-Pedersen partial adjustment toward the Markowitz target, so
order splitting and sign autocorrelation emerge endogenously. Setting
`rho=0` flips the same machinery to uninformed (randomized) flow — the
switch used for interventional data in causal A/B testing of impact models.

```python
from flowforge import OrderFlowSimulator, SimulationConfig

sim = OrderFlowSimulator(SimulationConfig(
    n_assets=100, n_periods=750,
    rho=0.05,             # information coefficient; 0 = uninformed flow
    alpha_half_life=5.0,  # signal persistence, periods
    risk_aversion=5.0,
    tcost=5e-3,           # quadratic transaction cost -> trading rate
    seed=7,
))
orders = sim.run()        # long-format tape: period, asset, notional, sign,
                          # participation, adv, market_cap, informed, ...
print(sim.realized_ic(orders))
```

Flow diagnostics:

```python
from flowforge import sign_autocorrelation, participation_stats

sign_autocorrelation(orders, max_lag=10)   # order-splitting persistence
participation_stats(orders)                # size/participation/cap relations
```

## Engine 2 — metaorder reconstruction (`flowforge.reconstruct`)

Takes any public tape (`timestamp, price, size, sign`, plus a session
column), randomly assigns trades to `n_traders` synthetic traders drawn
from a homogeneous or power-law frequency distribution (the mapping's only
two degrees of freedom), and defines a metaorder as a same-trader,
same-sign run of trades. Impact is measured from the trade before the
first child to the trade after the last child, normalized by daily
volatility and volume.

```python
from flowforge import build_metaorders, MappingConfig, synthetic_tape

tape = synthetic_tape(n_sessions=40, trades_per_session=3000, seed=11)
# or your own data: DataFrame with date, timestamp, price, size, sign

meta, children = build_metaorders(
    tape, MappingConfig(n_traders=20, freq_dist="homogeneous"), seed=11
)
```

Impact diagnostics:

```python
from flowforge import square_root_law, execution_profile, impact_decay

sql = square_root_law(meta)          # fits I/sigma = Y * (Q/V)^gamma
profile = execution_profile(children)  # vs sqrt(phi) concave benchmark
decay = impact_decay(meta, tape)     # rescaled impact at z = 1 + dt/T
```

Benchmarks from the literature: exponent ≈ 0.5 with prefactor
Y ∈ [0.5, 1]; concave `sqrt(phi)` in-execution profile; impact decaying
after execution on the timescale of the metaorder itself.

## Quickstart

```bash
python examples/quickstart.py
python -m pytest tests/
```

## Package layout

```
flowforge/
├── generate/       Kolm-Westray engine: alpha.py, mvo.py, market.py, simulator.py
├── reconstruct/    Maitrier-Bouchaud engine: mapping.py, metaorders.py, tape.py
└── diagnostics/    shared stylized-fact tests: impact.py, flow.py
```

## Disclaimer

Research software for simulation and diagnostics; not investment advice.

### Core Implementation Code & Architecture
#### File: `flowforge/diagnostics/__init__.py`
```python
"""Stylized-fact diagnostics shared by both engines."""

from flowforge.diagnostics.flow import participation_stats, sign_autocorrelation
from flowforge.diagnostics.impact import (
    execution_profile,
    impact_decay,
    square_root_law,
)

__all__ = [
    "square_root_law",
    "execution_profile",
    "impact_decay",
    "sign_autocorrelation",
    "participation_stats",
]
```

#### File: `flowforge/reconstruct/__init__.py`
```python
"""Synthetic metaorder reconstruction from public trade data
(Maitrier-Loeper-Bouchaud engine)."""

from flowforge.reconstruct.mapping import (
    MappingConfig,
    assign_traders,
    sample_trader_frequencies,
)
from flowforge.reconstruct.metaorders import build_metaorders
from flowforge.reconstruct.tape import synthetic_tape

__all__ = [
    "MappingConfig",
    "assign_traders",
    "sample_trader_frequencies",
    "build_metaorders",
    "synthetic_tape",
]
```

#### File: `flowforge/generate/__init__.py`
```python
"""Forward simulation of institutional order flow (Kolm-Westray engine)."""

from flowforge.generate.alpha import BootstrapAlpha
from flowforge.generate.market import MarketModel
from flowforge.generate.mvo import (
    markowitz_target,
    partial_adjustment_trades,
    trading_rate,
)
from flowforge.generate.simulator import OrderFlowSimulator, SimulationConfig

__all__ = [
    "BootstrapAlpha",
    "MarketModel",
    "OrderFlowSimulator",
    "SimulationConfig",
    "markowitz_target",
    "partial_adjustment_trades",
    "trading_rate",
]
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "flowforge"
version = "0.1.0"
description = "Metaorder simulation and market impact research: MVO-based order flow generation (Kolm-Westray) and synthetic metaorder reconstruction from public trade data (Maitrier-Loeper-Bouchaud)."
readme = "README.md"
requires-python = ">=3.9"
license = { text = "MIT" }
authors = [{ name = "FlowForge contributors" }]
keywords = ["algorithmic-trading", "market-microstructure", "metaorders", "price-impact", "simulation"]
dependencies = [
    "numpy>=1.22",
    "pandas>=1.4",
    "scipy>=1.8",
]

[project.optional-dependencies]
dev = ["pytest>=7.0"]

[tool.hatch.build.targets.wheel]
packages = ["flowforge"]
```

#### File: `flowforge/__init__.py`
```python
"""FlowForge: metaorder simulation and market impact research.

Two engines:

- ``flowforge.generate``  -- forward-simulates institutional order flow by
  feeding bootstrap alpha signals into mean-variance optimization with
  quadratic transaction costs (Kolm & Westray, JPM 2022).
- ``flowforge.reconstruct`` -- builds synthetic metaorders from public trade
  data via randomized trader-mapping functions
  (Maitrier, Loeper & Bouchaud, 2025, arXiv:2503.18199).

A shared ``flowforge.diagnostics`` module validates the stylized facts of
both order flow (sign autocorrelation, participation) and impact
(Square Root Law, concave execution profile, post-execution decay).
"""

from flowforge.generate import (
    BootstrapAlpha,
    MarketModel,
    OrderFlowSimulator,
    SimulationConfig,
    markowitz_target,
    partial_adjustment_trades,
)
from flowforge.reconstruct import (
    MappingConfig,
    build_metaorders,
    sample_trader_frequencies,
    synthetic_tape,
)
from flowforge.diagnostics import (
    execution_profile,
    impact_decay,
    participation_stats,
    sign_autocorrelation,
    square_root_law,
)

__version__ = "0.1.0"

__all__ = [
    "BootstrapAlpha",
    "MarketModel",
    "OrderFlowSimulator",
    "SimulationConfig",
    "markowitz_target",
    "partial_adjustment_trades",
    "MappingConfig",
    "build_metaorders",
    "sample_trader_frequencies",
    "synthetic_tape",
    "square_root_law",
    "execution_profile",
    "impact_decay",
    "sign_autocorrelation",
    "participation_stats",
]
```

#### File: `flowforge/reconstruct/mapping.py`
```python
"""The randomized trader-mapping function (Algorithm 2 of the paper).

The mapping assigns a synthetic trader ID to every public trade of a
session while preserving the true chronological order of trades.  It has
exactly two degrees of freedom, as in Maitrier, Loeper & Bouchaud (2025):
the number of traders ``n_traders`` and the distribution ``F`` of their
trading frequencies (homogeneous, or power-law ``P(f) ~ f^{-exponent}`` --
the empirically realistic choice, where a few traders account for most of
the volume).  Each trade is then drawn to a trader with probability
proportional to that trader's frequency.  Because every real trade is
assigned to exactly one synthetic trader, the mapping is a sampling
*without replacement* of the tape -- the feature the authors flag as
essential for recovering the Square Root Law.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class MappingConfig:
    """Degrees of freedom of the mapping function."""

    n_traders: int = 20
    freq_dist: str = "homogeneous"  # "homogeneous" or "powerlaw"
    exponent: float = 2.0           # power-law exponent (freq_dist="powerlaw")
    f_min: float = 1.0              # lower cutoff of the power law


def sample_trader_frequencies(
    config: MappingConfig, rng: np.random.Generator
) -> np.ndarray:
    """Draw f_i ~ F for each synthetic trader and normalize to probabilities."""
    if config.n_traders < 2:
        raise ValueError("n_traders must be >= 2")
    if config.freq_dist == "homogeneous":
        f = np.ones(config.n_traders)
    elif config.freq_dist == "powerlaw":
        if config.exponent <= 1.0:
            raise ValueError("power-law exponent must be > 1")
        # Inverse-CDF sampling of a Pareto with the given tail exponent.
        u = rng.uniform(size=config.n_traders)
        f = config.f_min * (1.0 - u) ** (-1.0 / (config.exponent - 1.0))
    else:
        raise ValueError(f"unknown freq_dist: {config.freq_dist!r}")
    return f / f.sum()


def assign_traders(
    n_trades: int, probabilities: np.ndarray, rng: np.random.Generator
) -> np.ndarray:
    """Assign each of ``n_trades`` chronologically ordered trades a trader ID.

    Vectorized version of the paper's loop: draw U ~ Uniform(0,1) per trade
    and locate it in the cumulative frequency table.
    """
    cumulative = np.cumsum(probabilities)
    cumulative[-1] = 1.0  # guard against floating-point undershoot
    u = rng.uniform(size=n_trades)
    return np.searchsorted(cumulative, u, side="right")
```


==================================================


## [2/3] Repository: OpenBook (`PHASE4-QUANT-047`)
- **Full Name**: `PHASE4-QUANT-047_DegenSugarBoo__OpenBook`
- **Description**: Real-time Crypto Futures depth heatmap in Rust (egui/eframe) with live order flow and trade tape.
- **GitHub Stars**: 181
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# OpenBook : Real-Time Crypto Order Book GUI

A high-performance, Rust desktop app for visualizing **Binance Futures** market microstructure in real time. It streams live depth + trade data, renders a Bookmap-style depth heatmap, and includes dockable analytics panes for order flow and execution impact.

![Preview of the app showing the heatmap, order book, trade tape, and market impact panes](assets/preview.png)

---

## Features

- **Real-time Binance Futures streaming** via WebSocket (`@depth@100ms`, `@aggTrade`)
- **Order book sync engine** with REST snapshot + contiguous diff-depth update handling
- **Bookmap-style depth heatmap** with event-driven history replay (checkpoint + delta model)
- **Live trade tape** with side coloring, min-notional filter, and adjustable row cap
- **Market impact estimator** for configurable notional and buy/sell side
- **Fill:Kill analytics** pane with event chart, cumulative chart, ratio states, and overfill highlighting
- **Dockable multi-pane workspace** (Heatmap, Order Book, Market Impact, Fill:Kill, Trades Tape)
- **Layout profiles** with save/load/save-as/rename/delete and automatic migration from legacy layout formats
- **Symbol picker** with searchable USDT perpetual catalog + live 24h mini-ticker data
- **Adaptive rendering cadence** (higher FPS during interaction, lower FPS when idle)
- **Performance overlay** for frame timing and heatmap rebuild metrics

## Getting Started

### Prerequisites

- [Rust](https://rustup.rs/) (stable toolchain)
- Desktop environment capable of running native `eframe` windows (macOS/Linux/Windows)

### Build & Run

```bash
# Clone the repo
git clone https://github.com/<your-username>/cli_ob.git
cd cli_ob

# Build (release mode recommended)
cargo build --release

# Run
cargo run --release
```

### Dev Commands

```bash
# Compile check
cargo check

# Lint (warnings denied)
cargo clippy -- -D warnings

# Format
cargo fmt

# Tests
cargo test
```

On startup, the app auto-connects to `btcusdt` and opens the default workspace layout.

## Controls

| Area | Interaction |
|-----|--------|
| Header | Enter symbol in picker, then `Connect` |
| Symbol picker | `ArrowUp` / `ArrowDown` navigate, `Enter` select/connect, `Esc` close |
| Layout menu | Toggle pane visibility, save/load layout profiles, reset layout |
| Heatmap | Mouse wheel zoom (price/time), drag pan, double-click reset view |
| Trades tape | Configure row cap and minimum notional filter |
| Market impact | Edit notional and switch Buy/Sell side |

## Architecture

```
src/
├── main.rs       # Entry point + WS orchestration + snapshot sync + reconnect logic
├── models.rs     # Core data models (OrderBook, trade/depth history, shared state, WS/REST types)
├── ui.rs         # egui/eframe UI, pane rendering, heatmap image build, snapshot cloning
├── micro.rs      # Fill:Kill burst logic, rolling KPIs, cumulative series math
└── workspace.rs  # Dock layout tree, pane definitions, profile persistence + migration
```

### Data Flow

```
Binance WS/REST ──► background tokio runtime (std::thread)
                       │
                       ├─ depth updates ─► order book apply + depth event history
                       ├─ agg trades   ─► trade history + micro metrics (Fill:Kill)
                       └─ miniTicker   ─► symbol picker live catalog rows

UI thread (egui) ──► clone_snapshot() ──► pane rendering + heatmap texture updates
```

1. **Connection task (`spawn_ws_task`)** connects to Binance depth/trade streams.
2. **Snapshot sync** fetches REST depth snapshot, bridges buffered WS diffs, then enforces contiguous updates.
3. **State updates** mutate `SharedState` (`OrderBook`, `EventDepthHistory`, `TradeHistory`, `MicroMetrics`) behind `Arc<Mutex<_>>`.
4. **UI frame loop** clones immutable snapshot data and renders panes; heatmap texture rebuilds only when render inputs change.

## Dependencies

| Crate | Purpose |
|-------|---------|
| `eframe` / `egui` | Native GUI framework and rendering |
| `egui_tiles` | Dockable pane layout/workspace management |
| `tokio` | Async runtime for WS/HTTP background tasks |
| `tokio-tungstenite` | WebSocket connectivity |
| `reqwest` | Binance REST API calls (snapshot, exchange info, time, ticker snapshot) |
| `serde` / `serde_json` | JSON deserialization |
| `ordered-float` | Ordered `f64` keys for `BTreeMap` price levels |
| `futures-util` | Stream utilities |
| `dhat` (optional feature) | Heap profiling support |

## Known Issues

- Advanced zoom/pan ergonomics can still be improved for dense books.
- Hover detail and visual ergonomics are still being iterated.
- Memory bloat issues still persist,on active markets memory usage climbs to ~600MB on my device
- Depth updated sometimes lag when a burst order appears,which I really cant help with cause trades data is realtime,while depth data has a 100ms update interval
## License

This project is licensed under the [MIT License](LICENSE).

### Core Implementation Code & Architecture
#### File: `Cargo.toml`
```python
[package]
name = "cli_ob"
version = "0.2.0"
edition = "2021"
description = "Real-time Binance Futures order book viewer with egui GUI"
license = "MIT"
readme = "README.md"

[features]
default = []
dhat-heap = ["dep:dhat"]

[dependencies]
tokio = { version = "1", features = ["full"] }
tokio-tungstenite = { version = "0.21", features = ["native-tls"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
futures-util = "0.3"
ordered-float = "4.0"
reqwest = { version = "0.11", features = ["json", "native-tls"] }
eframe = { version = "0.33", features = ["persistence"] }
egui_tiles = { version = "0.14", features = ["serde"] }
dhat = { version = "0.3", optional = true }

[profile.release]
opt-level = 3
lto = true
```

#### File: `tests/unit/workspace_tests.rs`
```python
use super::*;

#[test]
fn default_tree_contains_all_panes() {
    let tree = build_default_tree();
    let ids = pane_tile_map(&tree);
    for pane in PaneKind::ALL {
        assert!(ids.contains_key(&pane), "missing pane: {:?}", pane);
    }
}

#[test]
fn migrate_from_legacy_layout_store_keeps_visibility() {
    let store = LegacyLayoutStore {
        schema_version: 1,
        active_profile: "Default".to_string(),
        profiles: vec![LegacyLayoutProfile {
            name: "Default".to_string(),
            prefs: LegacyLayoutPrefs {
                show_heatmap_window: false,
                show_order_book_window: true,
                show_impact_window: false,
                show_fill_kill_window: true,
                show_trades_tape_window: false,
            },
        }],
    };

    let migrated = migrate_v1_store(store);
    let mut tree = migrated.profiles[0].dock_tree.clone();
    let pane_ids = ensure_all_panes(&mut tree);
    assert!(!tree.tiles.is_visible(pane_ids[&PaneKind::Heatmap]));
    assert!(tree.tiles.is_visible(pane_ids[&PaneKind::OrderBook]));
    assert!(!tree.tiles.is_visible(pane_ids[&PaneKind::MarketImpact]));
    assert!(tree.tiles.is_visible(pane_ids[&PaneKind::FillKill]));
    assert!(!tree.tiles.is_visible(pane_ids[&PaneKind::TradesTape]));
}

#[test]
fn cannot_delete_last_profile() {
    let mut store = LayoutStoreV2::default();
    let result = store.delete_profile(0);
    assert!(result.is_err());
}
```

#### File: `tests/unit/main_tests.rs`
```python
use super::*;
use crate::micro::{BurstDirection, FillKillSample, RatioValue};

fn make_depth_update(
    first_update_id: u64,
    final_update_id: u64,
    prev_final_update_id: u64,
) -> WsDepthUpdate {
    WsDepthUpdate {
        event_type: "depthUpdate".to_string(),
        event_time: 0,
        transaction_time: 0,
        symbol: "TESTUSDT".to_string(),
        first_update_id,
        final_update_id,
        prev_final_update_id,
        bids: Vec::new(),
        asks: Vec::new(),
    }
}

#[test]
fn can_bridge_when_final_equals_snapshot() {
    let update = make_depth_update(100, 110, 99);
    assert!(can_bridge_snapshot(&update, 110));
}

#[test]
fn can_bridge_when_final_exceeds_snapshot() {
    let update = make_depth_update(100, 120, 99);
    assert!(can_bridge_snapshot(&update, 110));
}

#[test]
fn cannot_bridge_when_final_below_snapshot() {
    let update = make_depth_update(100, 109, 99);
    assert!(!can_bridge_snapshot(&update, 110));
}

#[test]
fn cannot_bridge_when_first_after_snapshot() {
    let update = make_depth_update(111, 120, 110);
    assert!(!can_bridge_snapshot(&update, 110));
}

#[test]
fn contiguous_only_when_prev_equals_last_u() {
    let update = make_depth_update(0, 0, 200);
    assert!(is_contiguous(&update, 200));
}

#[test]
fn not_contiguous_when_prev_greater_than_last_u() {
    let update = make_depth_update(0, 0, 201);
    assert!(!is_contiguous(&update, 200));
}

#[test]
fn not_contiguous_when_prev_less_than_last_u() {
    let update = make_depth_update(0, 0, 199);
    assert!(!is_contiguous(&update, 200));
}

#[test]
fn derive_decimals_from_tick_size() {
    assert_eq!(derive_price_decimals("0.1"), 1);
    assert_eq!(derive_price_decimals("0.01"), 2);
    assert_eq!(derive_price_decimals("0.01000000"), 2);
    assert_eq!(derive_price_decimals("1.00000000"), 0);
}

#[test]
fn integer_tick_size_has_zero_decimals() {
    assert_eq!(derive_price_decimals("1"), 0);
    assert_eq!(derive_price_decimals("10.00000000"), 0);
}

#[test]
fn invalid_tick_size_uses_fallback_precision() {
    let decimals = parse_tick_size_and_decimals("invalid")
        .map(|(_, decimals)| decimals)
        .unwrap_or(DEFAULT_PRICE_DECIMALS);
    assert_eq!(decimals, DEFAULT_PRICE_DECIMALS);
}

#[test]
fn depth_epoch_increments_when_depth_update_applied() {
    let mut state = SharedState::new();
    state.tick_size = 1.0;
    state
        .order_book
        .bids
        .insert(ordered_float::OrderedFloat(100.0), 1.0);
    state
        .order_book
        .asks
        .insert(ordered_float::OrderedFloat(101.0), 1.0);

    let mut update = make_depth_update(1, 2, 0);
    update.event_time = 10;
    update.bids = vec![["100.0".to_string(), "0.0".to_string()]];

    apply_depth_update(&mut state, &update);

    assert_eq!(state.depth_epoch, 1);
}

#[test]
fn reset_fill_kill_clears_event_and_cumulative_histories() {
    let mut state = SharedState::new();
    let sample = FillKillSample {
        timestamp_ms: 1_000,
        fill_qty: 2.0,
        kill_qty: 1.0,
        pre_resting_walked_qty: 3.0,
        levels_moved: 1,
        ratio: RatioValue::Finite(2.0),
        direction: BurstDirection::Buy,
        signed_log_ratio: Some(0.3),
        overfill: true,
    };

    state
        .micro_metrics
        .fill_kill_history
        .samples
        .push_back(sample.clone());
    state.micro_metrics.on_fill_kill_sample(&sample);
    state.micro_metrics.reset_fill_kill();

    assert!(state.micro_metrics.fill_kill_history.samples.is_empty());
    assert!(state.micro_metrics.cumulative_history.samples.is_empty());
    assert_eq!(state.micro_metrics.cum_event_count, 0);
    assert_eq!(state.micro_metrics.cum_overfill_count, 0);
}
```

#### File: `tests/unit/ui_tests.rs`
```python
use super::{build_tape_rows, format_hms_millis, OrderBookApp};
use crate::models::{DepthLevelDelta, DepthSide, DepthSlice, SharedState};
use eframe::egui;
use ordered_float::OrderedFloat;
use std::sync::Arc;

fn assert_close(actual: f64, expected: f64) {
    assert!(
        (actual - expected).abs() <= 1e-9,
        "expected {expected}, got {actual}"
    );
}

#[test]
fn build_tape_rows_returns_newest_first() {
    let trades = vec![
        (1_000, 100.0, 1.0, true),
        (2_000, 101.0, 1.0, false),
        (3_000, 102.0, 1.0, true),
    ];

    let rows = build_tape_rows(&trades, None, 10);

    assert_eq!(rows.len(), 3);
    assert_eq!(rows[0].timestamp_ms, 3_000);
    assert_eq!(rows[1].timestamp_ms, 2_000);
    assert_eq!(rows[2].timestamp_ms, 1_000);
}

#[test]
fn build_tape_rows_min_filter_is_inclusive() {
    let trades = vec![
        (1_000, 10.0, 9.0, true),   // 90
        (2_000, 10.0, 10.0, false), // 100
        (3_000, 10.0, 12.0, true),  // 120
    ];

    let rows = build_tape_rows(&trades, Some(100.0), 10);

    assert_eq!(rows.len(), 2);
    assert_eq!(rows[0].timestamp_ms, 3_000);
    assert_eq!(rows[1].timestamp_ms, 2_000);
    assert!(rows.iter().all(|row| row.notional_usd >= 100.0));
}

#[test]
fn build_tape_rows_without_filter_returns_all_rows() {
    let trades = vec![
        (1_000, 10.0, 1.0, true),
        (2_000, 11.0, 1.0, false),
        (3_000, 12.0, 1.0, true),
    ];

    let rows = build_tape_rows(&trades, None, 10);

    assert_eq!(rows.len(), 3);
}

#[test]
fn build_tape_rows_applies_row_cap() {
    let trades = vec![
        (1_000, 10.0, 1.0, true),
        (2_000, 11.0, 1.0, false),
        (3_000, 12.0, 1.0, true),
    ];

    let rows = build_tape_rows(&trades, None, 2);

    assert_eq!(rows.len(), 2);
    assert_eq!(rows[0].timestamp_ms, 3_000);
    assert_eq!(rows[1].timestamp_ms, 2_000);
}

#[test]
fn build_tape_rows_with_zero_row_cap_returns_empty() {
    let trades = vec![
        (1_000, 10.0, 1.0, true),
        (2_000, 11.0, 1.0, false),
        (3_000, 12.0, 1.0, true),
    ];
    let rows = build_tape_rows(&trades, None, 0);
    assert!(rows.is_empty());
}

#[test]
fn build_tape_rows_handles_empty_input() {
    let rows = build_tape_rows(&[], Some(100.0), 100);
    assert!(rows.is_empty());
}

#[test]
fn format_hms_millis_formats_known_timestamps() {
    assert_eq!(format_hms_millis(0), "00:00:00.000");
    assert_eq!(format_hms_millis(3_723_004), "01:02:03.004");
}

#[test]
fn format_hms_millis_handles_boundaries() {
    assert_eq!(format_hms_millis(59_999), "00:00:59.999");
    assert_eq!(format_hms_millis(60_000), "00:01:00.000");
    assert_eq!(format_hms_millis(3_599_999), "00:59:59.999");
    assert_eq!(format_hms_millis(3_600_000), "01:00:00.000");
    assert_eq!(format_hms_millis(86_400_001), "00:00:00.001");
}

#[test]
fn nearest_depth_slice_index_picks_closest() {
    let slices = vec![
        Arc::new(DepthSlice {
            timestamp_ms: 1_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
        Arc::new(DepthSlice {
            timestamp_ms: 2_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
        Arc::new(DepthSlice {
            timestamp_ms: 4_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
    ];

    assert_eq!(
        OrderBookApp::nearest_depth_slice_index_from_slices(&slices, 500),
        0
    );
    assert_eq!(
        OrderBookApp::nearest_depth_slice_index_from_slices(&slices, 1_500),
        0
    );
    assert_eq!(
        OrderBookApp::nearest_depth_slice_index_from_slices(&slices, 3_500),
        2
    );
    assert_eq!(
        OrderBookApp::nearest_depth_slice_index_from_slices(&slices, 9_000),
        2
    );
}

#[test]
fn build_slice_index_map_matches_binary_search() {
    let slices = vec![
        Arc::new(DepthSlice {
            timestamp_ms: 1_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
        Arc::new(DepthSlice {
            timestamp_ms: 2_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
        Arc::new(DepthSlice {
            timestamp_ms: 4_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
        Arc::new(DepthSlice {
            timestamp_ms: 8_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
    ];
    let img_width: usize = 17;
    let view_time_start = 750.0;
    let time_span = 8_300.0;
    let x_denom = (img_width.saturating_sub(1)).max(1) as f64;

    let map = OrderBookApp::build_slice_index_map(&slices, img_width, view_time_start, time_span);

    assert_eq!(map.len(), img_width);
    for (x, &idx) in map.iter().enumerate() {
        let t_ms = (view_time_start + (x as f64 / x_denom) * time_span).max(0.0) as u64;
        let expected = OrderBookApp::nearest_depth_slice_index_from_slices(&slices, t_ms);
        assert_eq!(idx, expected);
    }
}

#[test]
fn clone_snapshot_reuses_depth_slices_until_epoch_changes() {
    let mut state = SharedState::new();
    state.order_book.bids.insert(OrderedFloat(100.0), 5.0);
    state.order_book.asks.insert(OrderedFloat(101.0), 3.0);
    state
        .depth_history
        .reset_from_book(&state.order_book, 1_000, 1);
    state.depth_history_epoch = 1;

    let snapshot_1 = state.clone_snapshot(1_000.0);
    let snapshot_2 = state.clone_snapshot(1_000.0);

    assert!(Arc::ptr_eq(
        &snapshot_1.depth_slices,
        &snapshot_2.depth_slices
    ));

    state.order_book.bids.insert(OrderedFloat(100.0), 7.0);
    state.depth_history.push_event(
        1_500,
        2,
        vec![DepthLevelDelta {
            side: DepthSide::Bid,
            price: 100.0,
            qty: 7.0,
        }],
        &state.order_book,
    );
    state.depth_history_epoch = 2;

    let snapshot_3 = state.clone_snapshot(1_000.0);
    assert!(!Arc::ptr_eq(
        &snapshot_2.depth_slices,
        &snapshot_3.depth_slices
    ));
}

#[test]
fn hover_row_price_mapping_is_centered() {
    let img_h = 4;
    let price_min = 100.0;
    let price_max = 200.0;

    assert_close(
        OrderBookApp::price_at_row(0, img_h, price_min, price_max),
        187.5,
    );
    assert_close(
        OrderBookApp::price_at_row(2, img_h, price_min, price_max),
        137.5,
    );
    assert_close(
        OrderBookApp::price_at_row(3, img_h, price_min, price_max),
        112.5,
    );
}

#[test]
fn split_side_grids_preserve_overlap() {
    let img_h = 8;
    let mut bid_grid = vec![0.0_f32; img_h];
    let mut ask_grid = vec![0.0_f32; img_h];
    let idx = OrderBookApp::heatmap_cell_idx(0, 3, img_h);

    let total_after_bid =
        OrderBookApp::accumulate_side_qty(&mut bid_grid, &mut ask_grid, idx, 6.0, true);
    let total_after_ask =
        OrderBookApp::accumulate_side_qty(&mut bid_grid, &mut ask_grid, idx, 4.0, false);

    assert_close(bid_grid[idx] as f64, 6.0);
    assert_close(ask_grid[idx] as f64, 4.0);
    assert_close(total_after_bid as f64, 6.0);
    assert_close(total_after_ask as f64, 10.0);
}

#[test]
fn latest_trade_for_pointer_returns_newest_timestamp() {
    let trades = vec![
        (1_000, 100.0, 1.0, true),
        (2_500, 101.0, 2.0, false),
        (2_000, 99.5, 3.0, true),
    ];
    assert_eq!(
        OrderBookApp::latest_trade_for_pointer(&trades),
        Some((2_500, 101.0))
    );
}

#[test]
fn latest_trade_for_pointer_returns_none_for_empty_input() {
    assert_eq!(OrderBookApp::latest_trade_for_pointer(&[]), None);
}

#[test]
fn is_live_time_view_uses_explicit_tolerance_ms() {
    assert!(OrderBookApp::is_live_time_view(99_999.5, 100_000.0, 1.0));
    assert!(!OrderBookApp::is_live_time_view(99_998.0, 100_000.0, 1.0));
}

#[test]
fn latest_trade_auto_center_price_returns_latest_when_live_follow() {
    let price = OrderBookApp::latest_trade_auto_center_price(true, Some((2_500, 101.25_f64)));
    assert_eq!(price, Some(101.25));
}

#[test]
fn latest_trade_auto_center_price_returns_none_when_not_live_follow() {
    let price = OrderBookApp::latest_trade_auto_center_price(false, Some((2_500, 101.25_f64)));
    assert_eq!(price, None);
}

#[test]
fn latest_trade_auto_center_price_returns_none_when_no_trades() {
    let price = OrderBookApp::latest_trade_auto_center_price(true, None);
    assert_eq!(price, None);
}

#[test]
fn latest_trade_auto_center_price_returns_none_when_price_is_non_finite() {
    let price = OrderBookApp::latest_trade_auto_center_price(true, Some((2_500, f64::NAN)));
    assert_eq!(price, None);
}

#[test]
fn pointer_y_fraction_filters_out_of_range_price() {
    assert_eq!(OrderBookApp::pointer_y_fraction(95.0, 100.0, 110.0), None);
    let inside = OrderBookApp::pointer_y_fraction(105.0, 100.0, 110.0);
    assert!(inside.is_some());
}

#[test]
fn live_strip_width_scales_and_clamps() {
    assert_close(OrderBookApp::live_strip_width(100.0) as f64, 28.0);
    assert!((OrderBookApp::live_strip_width(240.0) - 38.4).abs() < 1e-4);
    assert_close(OrderBookApp::live_strip_width(1000.0) as f64, 88.0);
}

#[test]
fn split_heatmap_rects_preserves_dimensions() {
    let rect = egui::Rect::from_min_size(egui::pos2(10.0, 20.0), egui::vec2(300.0, 120.0));
    let (data_rect, live_strip_rect) = OrderBookApp::split_heatmap_rects(rect);

    assert_close(data_rect.height() as f64, rect.height() as f64);
    assert_close(live_strip_rect.height() as f64, rect.height() as f64);
    assert_close(
        (data_rect.width() + live_strip_rect.width()) as f64,
        rect.width() as f64,
    );
    assert_close(data_rect.left() as f64, rect.left() as f64);
    assert_close(live_strip_rect.right() as f64, rect.right() as f64);
}

#[test]
fn depth_time_bounds_uses_latest_depth_timestamp_for_end() {
    let slices = vec![
        Arc::new(DepthSlice {
            timestamp_ms: 10_000,
            levels: Vec::new(),
            bids_len: 0,
        }),
        Arc::new(DepthSlice {
            timestamp_ms: 10_500,
            levels: Vec::new(),
            bids_len: 0,
        }),
        Arc::new(DepthSlice {
            timestamp_ms: 11_250,
            levels: Vec::new(),
            bids_len: 0,
        }),
    ];
    let (start, end) = OrderBookApp::depth_time_bounds(&slices).expect("time bounds");
    assert_eq!(start, 10_000.0);
    assert_eq!(end, 11_250.0);
}

#[test]
fn depth_time_bounds_returns_none_for_empty_input() {
    assert!(OrderBookApp::depth_time_bounds(&[]).is_none());
}
```

#### File: `tests/unit/models_tests.rs`
```python
use super::{
    DepthLevelDelta, DepthSide, EventDepthHistory, MarketImpact, OrderBook, Trade, TradeHistory,
    HISTORY_MAX_AGE_MS,
};
use ordered_float::OrderedFloat;

fn assert_close(left: f64, right: f64, tol: f64) {
    assert!(
        (left - right).abs() <= tol,
        "left={left}, right={right}, tol={tol}"
    );
}

#[test]
fn estimate_market_impact_buy_with_partial_last_level() {
    let mut book = OrderBook::new();
    book.asks.insert(OrderedFloat(100.0), 1.0);
    book.asks.insert(OrderedFloat(101.0), 2.0);

    let impact = book.estimate_market_impact(150.0, true, 100.0);

    assert!(impact.fully_filled);
    assert_eq!(impact.levels_consumed, 2);
    assert_close(impact.total_notional, 150.0, 1e-9);
    assert_close(impact.total_qty_filled, 1.495049504950495, 1e-12);
    assert_close(impact.avg_fill_price, 100.33112582781457, 1e-10);
    assert_close(impact.worst_fill_price, 101.0, 1e-9);
    assert_close(impact.slippage_bps, 33.11258278145695, 1e-9);
}

#[test]
fn estimate_market_impact_sell_partial_when_book_is_thin() {
    let mut book = OrderBook::new();
    book.bids.insert(OrderedFloat(99.0), 1.0);
    book.bids.insert(OrderedFloat(98.0), 1.0);

    let impact = book.estimate_market_impact(300.0, false, 100.0);

    assert!(!impact.fully_filled);
    assert_eq!(impact.levels_consumed, 2);
    assert_close(impact.total_notional, 197.0, 1e-9);
    assert_close(impact.total_qty_filled, 2.0, 1e-9);
    assert_close(impact.avg_fill_price, 98.5, 1e-9);
    assert_close(impact.worst_fill_price, 98.0, 1e-9);
    assert_close(impact.slippage_pct, 1.5, 1e-9);
}

#[test]
fn estimate_market_impact_zero_notional_returns_default() {
    let book = OrderBook::new();
    let impact = book.estimate_market_impact(0.0, true, 100.0);
    assert_eq!(
        impact,
        MarketImpact {
            avg_fill_price: 0.0,
            worst_fill_price: 0.0,
            slippage_bps: 0.0,
            slippage_pct: 0.0,
            levels_consumed: 0,
            total_qty_filled: 0.0,
            total_notional: 0.0,
            fully_filled: false,
        }
    );
}

#[test]
fn rolling_tps_returns_zero_for_empty_history() {
    let history = TradeHistory::new(300_000);
    assert_eq!(history.rolling_tps(100_000, 10_000), 0.0);
}

#[test]
fn rolling_tps_returns_zero_when_all_trades_are_older_than_window() {
    let mut history = TradeHistory::new(300_000);
    history.trades.push_back(Trade {
        timestamp_ms: 89_000,
        received_at_ms: 89_000,
        price: 100.0,
        quantity: 1.0,
        is_buy: true,
    });
    history.trades.push_back(Trade {
        timestamp_ms: 89_500,
        received_at_ms: 89_500,
        price: 100.0,
        quantity: 1.0,
        is_buy: false,
    });

    assert_eq!(history.rolling_tps(100_000, 10_000), 0.0);
}

#[test]
fn rolling_tps_counts_only_trades_inside_window() {
    let mut history = TradeHistory::new(300_000);
    history.trades.push_back(Trade {
        timestamp_ms: 89_999,
        received_at_ms: 89_999,
        price: 100.0,
        quantity: 1.0,
        is_buy: true,
    });
    history.trades.push_back(Trade {
        timestamp_ms: 90_000,
        received_at_ms: 90_000,
        price: 101.0,
        quantity: 2.0,
        is_buy: false,
    });
    history.trades.push_back(Trade {
        timestamp_ms: 95_000,
        received_at_ms: 95_000,
        price: 102.0,
        quantity: 1.0,
        is_buy: true,
    });
    history.trades.push_back(Trade {
        timestamp_ms: 99_500,
        received_at_ms: 99_500,
        price: 103.0,
        quantity: 3.0,
        is_buy: false,
    });

    let tps = history.rolling_tps(100_000, 10_000);
    assert_close(tps, 0.3, 1e-12);
}

#[test]
fn rolling_tps_includes_trade_at_exact_cutoff() {
    let mut history = TradeHistory::new(300_000);
    history.trades.push_back(Trade {
        timestamp_ms: 90_000,
        received_at_ms: 90_000,
        price: 100.0,
        quantity: 1.0,
        is_buy: true,
    });

    let tps = history.rolling_tps(100_000, 10_000);
    assert_close(tps, 0.1, 1e-12);
}

#[test]
fn rolling_tps_handles_dense_burst_with_decimal_result() {
    let mut history = TradeHistory::new(300_000);
    for i in 0..37_u64 {
        history.trades.push_back(Trade {
            timestamp_ms: 90_000 + i,
            received_at_ms: 90_000 + i,
            price: 100.0,
            quantity: 1.0,
            is_buy: i % 2 == 0,
        });
    }

    let tps = history.rolling_tps(100_000, 10_000);
    assert_close(tps, 3.7, 1e-12);
}

#[test]
fn event_depth_history_push_and_prune_by_age() {
    let mut book = OrderBook::new();
    book.bids.insert(OrderedFloat(100.0), 1.0);
    book.asks.insert(OrderedFloat(101.0), 1.0);

    let mut history = EventDepthHistory::new();
    history.reset_from_book(&book, 100_000, 1);

    // Push deltas at various times
    history.push_event(
        200_000,
        2,
        vec![DepthLevelDelta {
            side: DepthSide::Bid,
            price: 99.0,
            qty: 2.0,
        }],
        &book,
    );
    history.push_event(
        350_000,
        3,
        vec![DepthLevelDelta {
            side: DepthSide::Ask,
            price: 102.0,
            qty: 3.0,
        }],
        &book,
    );

    // Prune at 600_000 → cutoff = 420_000. Both deltas are old.
    history.prune(600_000);

    // All deltas are pruned under the 180s retention window.
    assert!(history.deltas.is_empty());
    // At least one checkpoint should remain (never drop the last one)
    assert!(!history.checkpoints.is_empty());
}

#[test]
fn event_depth_history_enforces_memory_cap() {
    let mut book = OrderBook::new();
    for i in 0..500 {
        book.bids.insert(OrderedFloat(100.0 + i as f64), 1000.0);
        book.asks.insert(OrderedFloat(200.0 + i as f64), 1000.0);
    }

    let mut history = EventDepthHistory::new();
    history.max_bytes = 1024; // artificially low
    history.reset_from_book(&book, 1_000, 1);

    // Push many events to exceed budget
    for i in 0..100 {
        history.push_event(
            2_000 + i * 100,
            2 + i,
            vec![DepthLevelDelta {
                side: DepthSide::Bid,
                price: 99.0,
                qty: i as f64,
            }],
            &book,
        );
    }

    history.prune(100_000);

    // After pruning under memory pressure, at least one checkpoint must remain
    assert!(!history.checkpoints.is_empty());
}

#[test]
fn delta_threshold_promotes_checkpoint() {
    let mut book = OrderBook::new();
    book.bids.insert(OrderedFloat(100.0), 1.0);
    book.asks.insert(OrderedFloat(101.0), 1.0);

    let mut history = EventDepthHistory::new();
    history.reset_from_book(&book, 1_000, 1);
    let initial_checkpoints = history.checkpoints.len();

    // Push a delta event with changes >= threshold
    let large_changes: Vec<DepthLevelDelta> = (0..super::DEPTH_DELTA_TO_CHECKPOINT_THRESHOLD)
        .map(|i| DepthLevelDelta {
            side: DepthSide::Bid,
            price: 50.0 + i as f64 * 0.01,
            qty: 1.0,
        })
        .collect();

    history.push_event(2_000, 2, large_changes, &book);

    // Should have added a checkpoint, not a delta
    assert_eq!(history.checkpoints.len(), initial_checkpoints + 1);
    // No new delta should have been added for this event
    assert!(history.deltas.is_empty());
}

#[test]
fn materialize_columns_replays_deltas_correctly() {
    let mut book = OrderBook::new();
    book.bids.insert(OrderedFloat(100.0), 5.0);
    book.asks.insert(OrderedFloat(101.0), 3.0);

    let mut history = EventDepthHistory::new();
    history.reset_from_book(&book, 1_000, 1);

    // Apply a delta that changes bid qty
    book.bids.insert(OrderedFloat(100.0), 10.0);
    history.push_event(
        1_500,
        2,
        vec![DepthLevelDelta {
            side: DepthSide::Bid,
            price: 100.0,
            qty: 10.0,
        }],
        &book,
    );

    let columns = history.materialize_columns(1_000, 2_000, 2);
    assert_eq!(columns.len(), 2);

    // First column at t=1000: bid qty should be 5.0
    let col0 = &columns[0];
    let bid_qty_0: f64 = col0.levels[..col0.bids_len]
        .iter()
        .find(|(p, _)| (*p - 100.0).abs() < 1e-9)
        .map(|(_, q)| *q)
        .unwrap_or(0.0);
    assert_close(bid_qty_0, 5.0, 1e-9);

    // Second column at t=1500: bid qty should be 10.0
    let col1 = &columns[1];
    let bid_qty_1: f64 = col1.levels[..col1.bids_len]
        .iter()
        .find(|(p, _)| (*p - 100.0).abs() < 1e-9)
        .map(|(_, q)| *q)
        .unwrap_or(0.0);
    assert_close(bid_qty_1, 10.0, 1e-9);
}

#[test]
fn reset_from_book_clears_old_state() {
    let mut book = OrderBook::new();
    book.bids.insert(OrderedFloat(100.0), 1.0);

    let mut history = EventDepthHistory::new();
    history.reset_from_book(&book, 1_000, 1);
    history.push_event(
        2_000,
        2,
        vec![DepthLevelDelta {
            side: DepthSide::Bid,
            price: 99.0,
            qty: 2.0,
        }],
        &book,
    );

    // Reset should clear everything
    let mut new_book = OrderBook::new();
    new_book.bids.insert(OrderedFloat(200.0), 5.0);
    history.reset_from_book(&new_book, 10_000, 100);

    assert_eq!(history.checkpoints.len(), 1);
    assert!(history.deltas.is_empty());
    assert_eq!(history.checkpoints[0].timestamp_ms, 10_000);
}

#[test]
fn trade_history_prunes_without_new_trades() {
    let mut history = TradeHistory::new(HISTORY_MAX_AGE_MS);
    history.trades.push_back(Trade {
        timestamp_ms: 1_000,
        received_at_ms: 1_000,
        price: 100.0,
        quantity: 1.0,
        is_buy: true,
    });
    history.trades.push_back(Trade {
        timestamp_ms: 2_000,
        received_at_ms: 2_000,
        price: 101.0,
        quantity: 1.0,
        is_buy: false,
    });
    history.trades.push_back(Trade {
        timestamp_ms: 310_000,
        received_at_ms: 310_000,
        price: 102.0,
        quantity: 1.0,
        is_buy: true,
    });

    let removed = history.prune_now(400_000);

    assert_eq!(removed, 2);
    assert_eq!(history.trades.len(), 1);
    assert_eq!(
        history.trades.front().map(|trade| trade.received_at_ms),
        Some(310_000)
    );
}

#[test]
fn trade_history_uses_received_at_for_retention() {
    let mut history = TradeHistory::new(HISTORY_MAX_AGE_MS);
    history.trades.push_back(Trade {
        timestamp_ms: 399_000,  // recent exchange timestamp
        received_at_ms: 90_000, // stale local timestamp
        price: 101.0,
        quantity: 1.0,
        is_buy: false,
    });
    history.trades.push_back(Trade {
        timestamp_ms: 1_000,     // old exchange timestamp
        received_at_ms: 350_000, // recent local timestamp
        price: 100.0,
        quantity: 1.0,
        is_buy: true,
    });

    let removed = history.prune_now(400_000);

    assert_eq!(removed, 1);
    assert_eq!(history.trades.len(), 1);
    assert_eq!(
        history.trades.front().map(|trade| trade.timestamp_ms),
        Some(1_000)
    );
    assert_eq!(
        history.trades.front().map(|trade| trade.received_at_ms),
        Some(350_000)
    );
}
```

#### File: `tests/unit/micro_tests.rs`
```python
use super::*;
use crate::models::OrderBook;

fn assert_close(left: f64, right: f64, tol: f64) {
    assert!(
        (left - right).abs() <= tol,
        "left={left}, right={right}, tol={tol}"
    );
}

fn make_book(bids: &[(f64, f64)], asks: &[(f64, f64)]) -> OrderBook {
    let mut book = OrderBook::new();
    for (price, qty) in bids {
        book.bids.insert(OrderedFloat(*price), *qty);
    }
    for (price, qty) in asks {
        book.asks.insert(OrderedFloat(*price), *qty);
    }
    book.last_event_time = 1_000;
    book
}

fn make_trade(timestamp_ms: u64, price: f64, quantity: f64, is_buy: bool) -> Trade {
    Trade {
        timestamp_ms,
        received_at_ms: timestamp_ms,
        price,
        quantity,
        is_buy,
    }
}

fn make_sample(timestamp_ms: u64, fill_qty: f64, kill_qty: f64, overfill: bool) -> FillKillSample {
    FillKillSample {
        timestamp_ms,
        fill_qty,
        kill_qty,
        pre_resting_walked_qty: fill_qty + kill_qty,
        levels_moved: 1,
        ratio: compute_fill_kill_ratio(fill_qty, kill_qty),
        direction: BurstDirection::Buy,
        signed_log_ratio: compute_signed_log_ratio(fill_qty, kill_qty),
        overfill,
    }
}

fn record_sample(metrics: &mut MicroMetrics, sample: FillKillSample) {
    metrics.fill_kill_history.samples.push_back(sample.clone());
    metrics.on_fill_kill_sample(&sample);
}

#[test]
fn burst_flush_on_side_flip() {
    let mut history = FillKillHistory::default();
    let book = make_book(&[(100.0, 3.0)], &[(101.0, 3.0)]);

    history.on_trade(&make_trade(1_000, 101.0, 1.0, true), 10, 1.0, &book);
    history.on_trade(&make_trade(1_010, 100.0, 2.0, false), 10, 1.0, &book);

    assert_eq!(history.samples.len(), 1);
    let sample = history.samples.back().expect("sample");
    assert_close(sample.fill_qty, 1.0, 1e-12);
}

#[test]
fn burst_flush_on_gap() {
    let mut history = FillKillHistory::default();
    let book = make_book(&[(100.0, 3.0)], &[(101.0, 3.0)]);

    history.on_trade(&make_trade(1_000, 101.0, 1.0, true), 1, 1.0, &book);
    history.on_trade(&make_trade(1_081, 101.0, 1.0, true), 1, 1.0, &book);

    assert_eq!(history.samples.len(), 1);
    let sample = history.samples.back().expect("sample");
    assert_eq!(sample.timestamp_ms, 1_000);
}

#[test]
fn burst_flush_on_epoch_advance() {
    let mut history = FillKillHistory::default();
    let book = make_book(&[(100.0, 3.0)], &[(101.0, 3.0)]);

    history.on_trade(&make_trade(1_000, 101.0, 1.0, true), 1, 1.0, &book);
    history.on_depth_epoch_advance(1_010, 2, 1.0);

    assert_eq!(history.samples.len(), 1);
    assert!(history.active_burst.is_none());
}

#[test]
fn levels_moved_and_walked_qty_buy() {
    let mut history = FillKillHistory::default();
    let book = make_book(&[(99.0, 5.0)], &[(100.0, 2.0), (101.0, 3.0), (102.0, 4.0)]);

    history.on_trade(&make_trade(1_000, 102.0, 5.0, true), 1, 1.0, &book);
    history.on_depth_epoch_advance(1_001, 2, 1.0);

    let sample = history.samples.back().expect("sample");
    assert_eq!(sample.levels_moved, 2);
    assert_close(sample.pre_resting_walked_qty, 9.0, 1e-12);
    assert_close(sample.fill_qty, 5.0, 1e-12);
    assert_close(sample.kill_qty, 4.0, 1e-12);
    assert_eq!(sample.direction, BurstDirection::Buy);
    let RatioValue::Finite(ratio) = sample.ratio else {
        panic!("expected finite ratio");
    };
    assert_close(ratio, 1.25, 1e-12);
    assert!(sample.signed_log_ratio.is_some());
    assert!(!sample.overfill);
}

#[test]
fn levels_moved_and_walked_qty_sell() {
    let mut history = FillKillHistory::default();
    let book = make_book(&[(100.0, 2.0), (99.0, 3.0), (98.0, 4.0)], &[(101.0, 5.0)]);

    history.on_trade(&make_trade(1_000, 98.0, 5.0, false), 1, 1.0, &book);
    history.on_depth_epoch_advance(1_001, 2, 1.0);

    let sample = history.samples.back().expect("sample");
    assert_eq!(sample.levels_moved, 2);
    assert_close(sample.pre_resting_walked_qty, 9.0, 1e-12);
    assert_close(sample.fill_qty, 5.0, 1e-12);
    assert_close(sample.kill_qty, 4.0, 1e-12);
    assert_eq!(sample.direction, BurstDirection::Sell);
    let RatioValue::Finite(ratio) = sample.ratio else {
        panic!("expected finite ratio");
    };
    assert_close(ratio, 1.25, 1e-12);
}

#[test]
fn ratio_infinite_when_kill_zero() {
    let mut history = FillKillHistory::default();
    let book = make_book(&[(99.0, 1.0)], &[(100.0, 1.0), (101.0, 1.0)]);

    history.on_trade(&make_trade(1_000, 101.0, 3.0, true), 1, 1.0, &book);
    history.on_depth_epoch_advance(1_001, 2, 1.0);

    let sample = history.samples.back().expect("sample");
    assert_close(sample.kill_qty, 0.0, 1e-12);
    assert_eq!(sample.ratio, RatioValue::Infinite);
    assert!(sample.signed_log_ratio.is_none());
}

#[test]
fn ratio_na_when_no_signal() {
    assert_eq!(compute_fill_kill_ratio(0.0, 0.0), RatioValue::Na);
}

#[test]
fn signed_log_ratio_is_none_for_infinite_and_clamped_for_finite() {
    assert!(compute_signed_log_ratio(1.0, 0.0).is_none());

    let value = compute_signed_log_ratio(1000.0, 0.0001).expect("finite log ratio");
    assert!(value <= 3.0);
    assert!(value > 0.0);

    let negative = compute_signed_log_ratio(0.0, 1000.0).expect("negative log ratio");
    assert!(negative >= -3.0);
    assert!(negative < 0.0);
}

#[test]
fn overfill_flag_when_fill_exceeds_walked_by_threshold() {
    let mut history = FillKillHistory::default();
    let book = make_book(&[(99.0, 1.0)], &[(100.0, 10.0)]);

    history.on_trade(&make_trade(1_000, 100.0, 10.21, true), 1, 1.0, &book);
    history.on_depth_epoch_advance(1_001, 2, 1.0);

    let sample = history.samples.back().expect("sample");
    assert!(sample.overfill);
    assert_eq!(sample.ratio, RatioValue::Infinite);
}

#[test]
fn history_retention_max_samples() {
    let mut history = FillKillHistory::default();
    history.max_samples = 5;
    let book = make_book(&[(99.0, 1.0)], &[(100.0, 1.0)]);

    for i in 0..20 {
        let ts = i * 1_000;
        history.on_trade(&make_trade(ts, 100.0, 1.0, true), i as u64, 1.0, &book);
        history.on_depth_epoch_advance(ts + 1, i as u64 + 1, 1.0);
    }

    assert_eq!(history.samples.len(), 5);
    let first_ts = history.samples.front().map(|s| s.timestamp_ms).unwrap_or(0);
    let last_ts = history.samples.back().map(|s| s.timestamp_ms).unwrap_or(0);
    assert!(first_ts > 0);
    assert!(last_ts > first_ts);
}

#[test]
fn cumulative_accumulates_and_kpi_snapshot_matches() {
    let mut metrics = MicroMetrics::default();
    metrics.on_fill_kill_sample(&make_sample(1_000, 3.0, 1.0, false));
    metrics.on_fill_kill_sample(&make_sample(1_100, 2.0, 0.0, true));

    assert_close(metrics.cum_fill_qty, 5.0, 1e-12);
    assert_close(metrics.cum_kill_qty, 1.0, 1e-12);
    assert_eq!(metrics.cum_event_count, 2);
    assert_eq!(metrics.cum_overfill_count, 1);
    assert_eq!(metrics.cumulative_history.samples.len(), 2);

    let latest = metrics
        .cumulative_history
        .latest()
        .expect("latest cumulative");
    assert_close(latest.cum_net_qty, 4.0, 1e-12);
    let RatioValue::Finite(ratio) = latest.cum_ratio else {
        panic!("expected finite cumulative ratio");
    };
    assert_close(ratio, 5.0, 1e-12);

    let kpis = metrics.kpi_snapshot();
    assert_close(kpis.overfill_pct, 50.0, 1e-12);
    assert_eq!(kpis.cum_event_count, 2);
    assert_eq!(kpis.cum_overfill_count, 1);
}

#[test]
fn cumulative_ratio_infinite_when_no_cumulative_kill() {
    let mut metrics = MicroMetrics::default();
    metrics.on_fill_kill_sample(&make_sample(1_000, 2.0, 0.0, false));

    let kpis = metrics.kpi_snapshot();
    assert_eq!(kpis.cum_ratio, RatioValue::Infinite);
    assert_eq!(
        metrics
            .cumulative_history
            .latest()
            .expect("latest")
            .cum_ratio,
        RatioValue::Infinite
    );
}

#[test]
fn sample_cumulative_adds_carry_forward_points() {
    let mut metrics = MicroMetrics::default();
    metrics.on_fill_kill_sample(&make_sample(1_000, 2.0, 1.0, false));

    metrics.sample_cumulative(1_200);
    assert_eq!(metrics.cumulative_history.samples.len(), 1);

    metrics.sample_cumulative(1_500);
    assert_eq!(metrics.cumulative_history.samples.len(), 2);
    let latest = metrics.cumulative_history.latest().expect("latest");
    assert_eq!(latest.timestamp_ms, 1_500);
    assert_close(latest.cum_fill_qty, 2.0, 1e-12);
    assert_close(latest.cum_kill_qty, 1.0, 1e-12);
}

#[test]
fn reset_fill_kill_clears_event_and_cumulative_state() {
    let mut metrics = MicroMetrics::default();
    let sample = make_sample(1_000, 2.0, 1.0, true);
    metrics.fill_kill_history.samples.push_back(sample.clone());
    metrics.on_fill_kill_sample(&sample);

    metrics.reset_fill_kill();

    assert!(metrics.fill_kill_history.samples.is_empty());
    assert!(metrics.fill_kill_history.active_burst.is_none());
    assert!(metrics.cumulative_history.samples.is_empty());
    assert_close(metrics.cum_fill_qty, 0.0, 1e-12);
    assert_close(metrics.cum_kill_qty, 0.0, 1e-12);
    assert_eq!(metrics.cum_event_count, 0);
    assert_eq!(metrics.cum_overfill_count, 0);
}

#[test]
fn prune_rolling_window_keeps_cutoff_sample_and_updates_kpis() {
    let mut metrics = MicroMetrics::default();
    record_sample(&mut metrics, make_sample(1_000, 3.0, 1.0, false));
    metrics.sample_cumulative(1_500);
    record_sample(&mut metrics, make_sample(2_000, 2.0, 1.0, true));
    metrics.sample_cumulative(2_500);
    record_sample(&mut metrics, make_sample(250_000, 4.0, 2.0, false));
    metrics.sample_cumulative(250_500);

    let fill_epoch_before = metrics.fill_kill_epoch;
    let cumulative_epoch_before = metrics.cumulative_epoch;

    metrics.prune_rolling_window(302_000);

    assert_eq!(metrics.fill_kill_history.samples.len(), 1);
    assert_eq!(
        metrics
            .fill_kill_history
            .samples
            .front()
            .expect("first sample")
            .timestamp_ms,
        250_000
    );
    assert_close(metrics.cum_fill_qty, 4.0, 1e-12);
    assert_close(metrics.cum_kill_qty, 2.0, 1e-12);
    assert_eq!(metrics.cum_event_count, 1);
    assert_eq!(metrics.cum_overfill_count, 0);
    assert!(metrics
        .cumulative_history
        .samples
        .iter()
        .all(|sample| sample.timestamp_ms >= 250_000));
    let latest = metrics.cumulative_history.latest().expect("latest");
    assert_close(latest.cum_fill_qty, 4.0, 1e-12);
    assert_close(latest.cum_kill_qty, 2.0, 1e-12);
    assert!(metrics.fill_kill_epoch > fill_epoch_before);
    assert!(metrics.cumulative_epoch > cumulative_epoch_before);
}

#[test]
fn prune_rolling_window_expires_all_data_and_resets_kpis() {
    let mut metrics = MicroMetrics::default();
    record_sample(&mut metrics, make_sample(1_000, 2.0, 1.0, true));
    metrics.sample_cumulative(1_500);
    record_sample(&mut metrics, make_sample(2_000, 1.0, 1.0, false));
    metrics.sample_cumulative(2_500);

    metrics.prune_rolling_window(700_000);

    assert!(metrics.fill_kill_history.samples.is_empty());
    assert!(metrics.cumulative_history.samples.is_empty());
    assert_close(metrics.cum_fill_qty, 0.0, 1e-12);
    assert_close(metrics.cum_kill_qty, 0.0, 1e-12);
    assert_eq!(metrics.cum_event_count, 0);
    assert_eq!(metrics.cum_overfill_count, 0);
    let kpis = metrics.kpi_snapshot();
    assert_close(kpis.cum_fill_qty, 0.0, 1e-12);
    assert_close(kpis.cum_kill_qty, 0.0, 1e-12);
    assert_eq!(kpis.cum_ratio, RatioValue::Na);
    assert_eq!(kpis.cum_event_count, 0);
    assert_eq!(kpis.cum_overfill_count, 0);
}

#[test]
fn rolling_window_trim_helper_is_non_destructive_when_used_on_clone() {
    let mut canonical = CumulativeHistory::default();
    canonical.push(CumulativeSample {
        timestamp_ms: 0,
        cum_fill_qty: 1.0,
        cum_kill_qty: 0.5,
        cum_net_qty: 0.5,
        cum_ratio: RatioValue::Finite(2.0),
    });
    canonical.push(CumulativeSample {
        timestamp_ms: 100_000,
        cum_fill_qty: 2.0,
        cum_kill_qty: 1.0,
        cum_net_qty: 1.0,
        cum_ratio: RatioValue::Finite(2.0),
    });
    canonical.push(CumulativeSample {
        timestamp_ms: 400_000,
        cum_fill_qty: 3.0,
        cum_kill_qty: 1.5,
        cum_net_qty: 1.5,
        cum_ratio: RatioValue::Finite(2.0),
    });

    let mut rolling = canonical.clone();
    rolling.trim_window(400_000, ROLLING_WINDOW_MS);

    assert_eq!(canonical.samples.len(), 3);
    assert_eq!(rolling.samples.len(), 1);
    assert_eq!(
        rolling.samples.front().expect("first").timestamp_ms,
        400_000
    );
}
```


==================================================


## [3/3] Repository: ITCH (`DISC-512`)
- **Full Name**: `martinobdl/ITCH`
- **Description**: Nasdaq Order Book Reconstructor
- **GitHub Stars**: 285
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
