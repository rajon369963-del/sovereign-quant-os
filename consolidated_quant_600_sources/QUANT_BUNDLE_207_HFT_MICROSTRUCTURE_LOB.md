# ⚡ [QUANT-SOURCE-207] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_207_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: matchbook (`PHASE4-QUANT-052`)
- **Full Name**: `PHASE4-QUANT-052_joaquinbejar__matchbook`
- **Description**: Decentralized exchange infrastructure on Solana: on-chain order book, real-time WebSocket streaming, REST API, Geyser indexer, and Rust SDK. Non-custodial and optimized for high-frequency trading.
- **GitHub Stars**: 19
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Matchbook

[![CI](https://github.com/joaquinbejar/matchbook/actions/workflows/ci.yml/badge.svg)](https://github.com/joaquinbejar/matchbook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance, non-custodial Central Limit Order Book (CLOB) on Solana.

## Overview

Matchbook is a decentralized exchange infrastructure that provides:

- **On-chain order book**: Fully transparent order matching on Solana
- **Non-custodial**: Users maintain control of their funds at all times
- **High performance**: Optimized for Solana's parallel transaction processing
- **Real-time data**: WebSocket streaming for live market updates
- **Developer-friendly**: REST API, WebSocket API, and SDKs for Rust and TypeScript

## Architecture

```mermaid
flowchart TB
    subgraph Clients["Clients"]
        C1[Web Apps]
        C2[Trading Bots]
        C3[SDKs]
    end

    subgraph API["API Layer"]
        REST["REST API<br/>:8080"]
        WS["WebSocket<br/>:8081"]
        Direct["Direct<br/>On-chain"]
    end

    subgraph Backend["Backend Services"]
        Indexer["Indexer<br/>(Geyser)"]
        Program["Solana Program<br/>(On-chain)"]
        DB["Database<br/>(TimescaleDB)"]
    end

    Clients --> REST
    Clients --> WS
    Clients --> Direct

    REST --> Indexer
    REST --> Program
    WS --> Indexer
    Direct --> Program

    Program --> Indexer
    Indexer --> DB
```

## Quick Start

### Prerequisites

- Rust 1.75+
- Solana CLI 1.18+
- Node.js 18+ (for TypeScript SDK)
- Docker (for local development)

### Local Development

```bash
# Clone the repository
git clone https://github.com/joaquinbejar/matchbook.git
cd matchbook

# Start local infrastructure
docker-compose -f Docker/docker-compose.yml up -d

# Build the on-chain program
cargo build-sbf

# Run tests
cargo test --all-features

# Deploy to localnet
solana-test-validator &
solana program deploy target/deploy/matchbook_program.so
```

### Using the SDK

#### Rust

```rust
use matchbook_sdk::{Client, PlaceOrderParams, Side, OrderType};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new("https://api.matchbook.taunais.com")?;
    
    // Get markets
    let markets = client.get_markets().await?;
    
    // Place an order
    let tx = client.place_order(PlaceOrderParams {
        market: markets[0].address,
        side: Side::Bid,
        price: 100_000_000, // $100.00 in base units
        quantity: 1_000_000_000, // 1 SOL in lamports
        order_type: OrderType::Limit,
        ..Default::default()
    }).await?;
    
    println!("Order placed: {}", tx.signature);
    Ok(())
}
```

#### TypeScript

```typescript
import { MatchbookClient, Side, OrderType } from '@matchbook/sdk';

const client = new MatchbookClient('https://api.matchbook.taunais.com');

// Get markets
const markets = await client.getMarkets();

// Place an order
const tx = await client.placeOrder({
  market: markets[0].address,
  side: Side.Bid,
  price: '100.00',
  quantity: '1.0',
  orderType: OrderType.Limit,
});

console.log('Order placed:', tx.signature);
```

## Documentation

| Document | Description |
|----------|-------------|
| [Architecture](docs/architecture.md) | System architecture and design |
| [Getting Started](docs/getting-started.md) | Step-by-step integration guide |
| [API Reference](docs/api-reference.md) | REST API documentation |
| [WebSocket Reference](docs/websocket-reference.md) | WebSocket API documentation |
| [SDK Guide](docs/sdk-guide.md) | SDK usage for Rust and TypeScript |
| [Deployment](docs/docker.md) | Docker and Kubernetes deployment |
| [Monitoring](docs/monitoring.md) | Prometheus and Grafana setup |
| [FAQ](docs/faq.md) | Frequently asked questions |

## Project Structure

```
matchbook/
├── program/           # Solana on-chain program
├── sdk/               # Rust client SDK
├── ts-sdk/            # TypeScript client SDK
├── indexer/           # Geyser-based indexer service
├── api/               # REST and WebSocket API server
├── crank/             # Order matching crank service
├── k8s/               # Kubernetes manifests
├── monitoring/        # Prometheus and Grafana configs
└── docs/              # Documentation
```

## Crates

| Crate | Description |
|-------|-------------|
| `matchbook_program` | On-chain Solana program |
| `matchbook_sdk` | Rust client SDK |
| `matchbook_types` | Shared types and utilities |

## API Endpoints

### REST API

| Endpoint | Description |
|----------|-------------|
| `GET /v1/markets` | List all markets |
| `GET /v1/markets/{address}/orderbook` | Get order book snapshot |
| `GET /v1/markets/{address}/trades` | Get recent trades |
| `POST /v1/tx/place-order` | Build place order transaction |
| `POST /v1/tx/cancel-order` | Build cancel order transaction |

### WebSocket Channels

| Channel | Description |
|---------|-------------|
| `book` | Order book updates |
| `trades` | Trade stream |
| `ticker` | Price ticker |
| `orders` | User order updates (authenticated) |

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run tests: `cargo test --all-features`
5. Run lints: `cargo clippy --all-targets --all-features -- -D warnings`
6. Submit a pull request

## Security

For security concerns, please see [SECURITY.md](SECURITY.md) or email security@matchbook.taunais.com.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

See [GitHub Issues](https://github.com/joaquinbejar/matchbook/issues) for detailed progress.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b M[N]/issue-[NUM]-description`
3. Follow the [Rust coding guidelines](.internalDoc/09-rust-guidelines.md)
4. Run `make pre-push` before committing
5. Submit a pull request

## Contact

- **Author**: Joaquín Béjar García
- **Email**: jb@taunais.com
- **Telegram**: [@joaquin_bejar](https://t.me/joaquin_bejar)
- **Repository**: https://github.com/joaquinbejar/matchbook

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

### Core Implementation Code & Architecture
#### File: `rust-toolchain.toml`
```python
[toolchain]
channel = "stable"
```

#### File: `ts-sdk/tsconfig.esm.json`
```python
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "module": "NodeNext",
    "outDir": "./dist/esm",
    "declaration": false,
    "declarationMap": false
  }
}
```

#### File: `ts-sdk/tsconfig.types.json`
```python
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./dist/types",
    "declaration": true,
    "declarationMap": true,
    "emitDeclarationOnly": true
  }
}
```

#### File: `api/src/models/mod.rs`
```python
//! Request and response models for the API.
//!
//! Provides typed structures for API requests and responses.

pub mod request;
pub mod response;

pub use request::*;
pub use response::*;
```

#### File: `api/src/handlers/mod.rs`
```python
//! Request handlers for the API.
//!
//! Provides handler functions for all API endpoints.

pub mod accounts;
pub mod markets;
pub mod tx;

pub use accounts::*;
pub use markets::*;
pub use tx::*;
```

#### File: `ts-sdk/tsconfig.cjs.json`
```python
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "module": "CommonJS",
    "moduleResolution": "bundler",
    "outDir": "./dist/cjs",
    "declaration": false,
    "declarationMap": false
  }
}
```


==================================================


## [2/3] Repository: lob-regime-scanner (`PHASE4-QUANT-054`)
- **Full Name**: `PHASE4-QUANT-054_CameronScarpati__lob-regime-scanner`
- **Description**: HMM-based market microstructure regime detection for cryptocurrency order books — 30+ features, Gaussian HMM, C++/pybind11 LOB engine, interactive Plotly Dash dashboard
- **GitHub Stars**: 16
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">

# LOB Regime Scanner

### Hidden Markov Model Regime Detection for Cryptocurrency Order Books

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C?style=flat&logo=cplusplus&logoColor=white)](https://isocpp.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-230-brightgreen?style=flat&logo=pytest&logoColor=white)]()

*A learning project exploring latent market microstructure regimes in Level 2*
*order book data using Gaussian HMMs, microstructure features (OFI, VPIN, Kyle's*
*&lambda;), and an interactive four-panel Plotly Dash dashboard. Exploratory, not a*
*production trading signal.*

---

**[Methodology](docs/methodology.md)** &middot; **[Results](docs/results.md)** &middot; **[Notebooks](#-notebooks)** &middot; **[Quick Start](#-quick-start)**

</div>

<br>

<p align="center">
  <img src="docs/dashboard_screenshot.png" alt="LOB Regime Scanner Dashboard" width="95%"/>
</p>

<p align="center"><i>
  Four-panel interactive dashboard: Bookmap-style LOB heatmap with regime overlay,
  HMM state probabilities, 3D depth surface, and toxicity diagnostics (VPIN, OFI, spread, PnL).
</i></p>

<br>

## Overview

An end-to-end pipeline, built as a learning project, that infers **hidden regimes** from noisy order book signals. The core flow:

```
Tardis L2 Snapshots ──▸ 30+ Microstructure Features ──▸ Gaussian HMM ──▸ Regime Detection ──▸ Dashboard
   (25 levels/side)       (OFI, VPIN, Kyle's λ,          (Baum-Welch       (causal filtered      (4 synced
    100ms sampling)        spread, vol, autocorr)          EM fitting)        decode)               panels)
```

The model separates the data into **three hidden states**, which I label Quiet, Trending, and Toxic by ordering them on variance. On the synthetic and sample data used here they show different volatility and liquidity characteristics. The labels are interpretive, and the separation has not been validated on real market data.

**Author:** Cameron Scarpati

<br>

## What the Model Produces

After fitting, the three states sort cleanly by variance, and on the synthetic and sample data used here they line up with an intuitive reading of the order book:

- **Quiet** is the lowest-variance state: tighter spreads, balanced order flow, near-zero return autocorrelation.
- **Trending** sits in the middle: directional order flow imbalance and positive short-horizon return autocorrelation, a momentum signature.
- **Toxic** is the highest-variance state: wider spreads, elevated VPIN, and negative return autocorrelation, a mean-reversion signature.

The learned transition matrix is strongly diagonal, so each state tends to persist rather than flip every step. A simple regime-conditional rule (enter on Quiet to Trending in the order-flow direction, flatten on Toxic) is included to visualize how the regimes behave over time.

These are qualitative observations on synthetic and sample data, not validated results. Please read **[Scope and Limitations](#scope-and-limitations)** before reading anything quantitative into them.

<br>

## Scope and Limitations

This is a personal learning project for getting hands-on with Hidden Markov Models and order book microstructure. It is exploratory rather than a production trading signal. Several early methodological weaknesses have since been fixed — full-sample scaling, a fully in-sample fit, a cost-free same-bar backtest, and a non-causal smoothed decode driving the signal — and the remaining limitations are stated plainly so nothing here is mistaken for a validated result:

- **No real-market validation.** The regime behavior shown above comes from synthetic and free sample data. None of it has been validated at scale on real market data, and the regime labels (Quiet/Trending/Toxic) remain an interpretive reading.
- **Walk-forward split, but a short one.** The default pipeline fits the HMM (and its feature scaler) on the first 70% of the data only and reports headline backtest statistics on the held-out 30%. That makes the numbers out-of-sample rather than in-sample, but the sample itself is short (single instrument, limited dates), so out-of-sample here still does not mean robust.
- **Causal decoding for the signal, smoothed for the picture.** The states the backtest trades on come from the forward algorithm alone (`predict_filtered`), so the label at bar *t* uses no observation after *t*. The Viterbi path (`predict`) is a smoother whose label at *t* depends on the whole series, which makes it the better retrospective picture but invalid as a signal; it is computed for visualization and returned separately as `states_smoothed`.
- **Standardization is causal in the default pipeline.** The HMM's `StandardScaler` and VPIN's volume-bucket sizing are both derived from the train segment only, and feature NaN handling forward-fills without back-filling, so no feature row draws on future data. The legacy fully in-sample mode (`train_frac=None`) uses full-sample statistics by design.
- **Backtest is more realistic, still illustrative.** Execution is next-bar (a signal never earns the bar it fires on) and results are net of configurable taker fees and slippage (default 5.5 bps fee + 0.5 bps slippage per side), with gross figures reported alongside. Fills are still modeled naively (a full fill at the decision bar's mid, with returns accruing from the next bar; no queue position, no partial fills, no market impact). It exists to visualize regime behavior, not to demonstrate a tradeable edge.
- **Two OFI formulations.** Both the simple volume-delta proxy and the canonical price-conditioned formulation of Cont, Kukanov & Stoikov (2014) are implemented; the HMM uses the canonical one, and the proxy is kept for comparison.
- **Curated feature subset, diagonal covariance.** The pipeline computes roughly 30 candidate features but feeds a curated subset of 8 to the HMM, fit with diagonal covariance, to keep the parameter count manageable.
- **C++ engine is optional; throughput is measurable, not guaranteed.** A reproducible benchmark (`make bench`) is included. On a sample cloud VM it measured roughly 4-9M synthetic updates/sec through the C++ batch path and roughly 4M/sec through the per-call Python bindings, single-threaded. Run-to-run variance on shared hardware is large, so these are indicative measurements to re-run locally, not a validated performance claim.

<br>

## Architecture

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                              LOB REGIME SCANNER                                      │
├────────────────────┬────────────────────┬──────────────────┬─────────────────────────┤
│                    │                    │                  │                         │
│   DATA LAYER       │   FEATURE ENGINE   │   HMM ENGINE     │   DASHBOARD             │
│                    │                    │                  │                         │
│  Tardis.dev        │  OFI (depth 1,5,10)│  Gaussian HMM    │  ┌──────┬──────-┐       │
│  Direct HTTP       │  VPIN (flowrisk)   │  3-state (BIC)   │  │Book- │Regime │       │
│  40+ exchanges     │  Kyle's λ (OLS)    │                  │  │map   │Probs  │       │
│  Free 1st/mo       │  Spread dynamics   │  Baum-Welch EM   │  │Heat- │Stacked│       │
│                    │  Book imbalance    │  (200 iter max)  │  │map   │Area   │       │
│  book_snapshot_25  │  Realized vol (4x) │                  │  ├──────┼───────┤       │
│  100ms subsampling │  Ret autocorr (10) │  Filtered decode │  │3D    │Toxi-  │       │
│                    │  Trade aggression  │  (causal signal) │  │Depth │city   │       │
│  C++ LOB Engine    │  Cancel ratio      │  + Viterbi (viz) │  │Surf. │Diag.  │       │
│  (pybind11, opt.)  │                    │                  │  └──────┴───────┘       │
│  high-throughput   │  30+ features      │  BIC/AIC model   │  Synchronized panels    │
│                    │  Rolling z-score   │  selection       │  Crosshair + slider     │
│                    │                    │                  │                         │
└────────────────────┴────────────────────┴──────────────────┴─────────────────────────┘
```

<br>

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Core** | Python 3.11+, NumPy, Pandas | Feature computation, data pipeline |
| **Performance** | C++17, pybind11 | LOB reconstruction engine (optional, benchmark via `make bench`) |
| **Statistics** | hmmlearn, scikit-learn, flowrisk | Gaussian HMM, VPIN computation |
| **Visualization** | Plotly, Dash, Dash Mantine | Interactive 4-panel dashboard |
| **Data** | Tardis.dev (direct HTTP) | Tick-level L2 snapshots, 40+ exchanges |
| **Testing** | pytest (230 tests) | Unit tests across all modules |

<br>

## Quick Start

```bash
# Clone & setup
git clone https://github.com/CameronScarpati/lob-regime-scanner.git
cd lob-regime-scanner
make install-dev
source .venv/bin/activate

# Launch with synthetic data (no download needed)
python -m dashboard.app --demo

# Or download free sample data (1st of any month, no API key)
python data/download.py --symbol BTCUSDT --start 2024-01-01 --end 2024-01-01
python -m dashboard.app --symbol BTCUSDT --start 2024-01-01 --end 2024-01-01
```

<br>

## Downloading Data

Data is sourced from [Tardis.dev](https://tardis.dev) — professional-grade tick-level order book data for 40+ crypto exchanges. Free sample data for the **1st of each month** is available without an API key.

```bash
# Free sample data (no API key needed)
python data/download.py --symbol BTCUSDT --start 2024-01-01 --end 2024-01-01

# Multiple free months
python data/download.py --symbol BTCUSDT --start 2024-01-01 --end 2024-03-01

# Full API access (any date, requires paid key)
python data/download.py --symbol BTCUSDT --start 2024-06-15 --end 2024-06-21 \
  --tardis-api-key YOUR_KEY
```

<details>
<summary><b>Download Options &amp; Supported Exchanges</b></summary>
<br>

```bash
python data/download.py [OPTIONS]

  --symbol TEXT          Trading pair (default: BTCUSDT)
  --start DATE          Start date YYYY-MM-DD (required)
  --end DATE            End date YYYY-MM-DD (required)
  --exchange NAME       Exchange source (default: bybit)
  --data-type TYPE      Tardis data type (default: book_snapshot_25)
  --output-dir PATH     Output directory (default: data/raw/)
  --tardis-api-key KEY  Tardis.dev API key (or set TARDIS_API_KEY env var)
```

| Exchange | `--exchange` | Description |
|----------|:--------:|-------------|
| Bybit | `bybit` | Bybit derivatives (default) |
| Binance Futures | `binance` | Binance USD-M Futures |
| Binance Spot | `binance-spot` | Binance spot market |
| OKX | `okx` | OKX perpetual swaps |
| Deribit | `deribit` | Deribit options/futures |

</details>

<br>

## Dashboard

```bash
python -m dashboard.app [OPTIONS]

  --symbol TEXT        Trading pair (default: BTCUSDT)
  --start DATE         Start date (e.g. 2024-01-01)
  --end DATE           End date (e.g. 2024-01-01)
  --sample-interval N  Snapshot subsampling in ms (default: 100)
  --demo               Use synthetic mock data
  --host HOST          Bind address (default: 0.0.0.0)
  --port PORT          Port (default: 8050)
  --debug              Enable Dash debug mode
```

The `--sample-interval` flag controls temporal resolution. Tardis `book_snapshot_25` files contain a snapshot on every book change (potentially millions per day). The default 100ms interval captures microstructure dynamics while keeping memory usage reasonable (~864k snapshots/day). Use `10` for near-tick-level resolution or `1000` for faster loading on large date ranges.

<br>

## Project Structure

```
lob-regime-scanner/
│
├── src/                           Core library
│   ├── data_loader.py                 Tardis CSV parser + snapshot loader
│   ├── book_reconstructor.py          LOB reconstruction (C++ accelerated)
│   ├── features.py                    OFI, VPIN, Kyle's λ — 30+ features
│   ├── hmm_model.py                   Gaussian HMM regime detection
│   ├── backtest.py                    Regime-conditional strategy validation
│   └── cpp/                           C++17 LOB engine (pybind11)
│       ├── lob_engine.hpp/cpp             Sparse order book (std::map)
│       └── bindings.cpp                   Python bindings
│
├── dashboard/                     Plotly Dash app — 4 synchronized panels
│   ├── app.py                         Main app + CLI entry point
│   ├── pipeline.py                    End-to-end data → model → viz
│   ├── callbacks.py                   Dash interactivity callbacks
│   └── components/                    Visualization panels
│       ├── heatmap.py                     Bookmap-style LOB heatmap
│       ├── regime_probs.py                Regime probability areas
│       ├── depth_surface.py               3D order book surface
│       └── diagnostics.py                 VPIN, OFI, spread, PnL
│
├── data/                          Data acquisition
│   ├── download.py                    Tardis.dev HTTP downloader
│   └── generate_realistic.py          Synthetic data generator
│
├── notebooks/                     Analysis notebooks (4)
├── tests/                         pytest suite (230 tests)
├── docs/                          Methodology + results writeups
└── pyproject.toml                 Dependencies & package config
```

<br>

## Notebooks

| # | Notebook | Description |
|:-:|----------|-------------|
| 1 | [Data Exploration](notebooks/01_data_exploration.ipynb) | Raw L2 data statistics, order book shape analysis, spread distributions |
| 2 | [Feature Engineering](notebooks/02_feature_engineering.ipynb) | Feature distributions, correlations, OFI/VPIN time series |
| 3 | [HMM Fitting](notebooks/03_hmm_fitting.ipynb) | BIC/AIC model selection, EM convergence, state interpretation |
| 4 | [Regime Analysis](notebooks/04_regime_analysis.ipynb) | Regime-conditional statistics, transition dynamics, backtest results |

<br>

## Methodology

> For the full mathematical formulation, see [docs/methodology.md](docs/methodology.md).

The pipeline computes roughly **30 candidate microstructure features** from Level 2 snapshots, feeds a curated subset to a **Gaussian Hidden Markov Model**, and decodes regimes via the **Viterbi algorithm**:

**Feature Engineering** — order flow imbalance in two formulations (a simple multi-level volume-delta proxy and the canonical price-conditioned Cont, Kukanov & Stoikov (2014) version, which the HMM uses), VPIN (Easley, L&oacute;pez de Prado & O'Hara, 2012), Kyle's &lambda; via rolling OLS, book imbalance, realized volatility at 4 horizons, return autocorrelation at 10 lags, spread dynamics, trade aggression, and cancellation ratio. NaN handling is forward-fill only (no backward fill), and VPIN's volume-bucket size — a full-sample statistic of whatever frame it sees — is estimated from the training segment alone, so no feature row draws on future data.

**HMM Regime Detection** — a 3-state Gaussian HMM, fit via Baum-Welch EM (up to 200 iterations) with diagonal covariance in the default pipeline (full covariance is also supported). The default pipeline is walk-forward: the model and its `StandardScaler` are fit on the first 70% of the series only. Regimes are then decoded **causally** with the forward algorithm (`predict_filtered`), so the state at bar *t* conditions only on observations up to *t*; the smoothed Viterbi path is kept alongside for visualization. States are auto-sorted by covariance trace (a volatility proxy) for deterministic labeling. A BIC/AIC sweep over K &isin; {2, 3, 4, 5} is implemented; the default uses K = 3, chosen for interpretability.

**Backtest** — a regime-conditional rule (enter on Quiet to Trending in the OFI direction, flatten on Toxic) driven by causally decoded states, with next-bar execution, taker fees and slippage (defaults: 5.5 + 0.5 bps per side), Sharpe annualized from the actual bar interval, and drawdown reported as a fraction of peak equity measured from starting capital. Headline statistics come from the held-out segment, net of costs, with in-sample and gross figures reported alongside. It exists to visualize regime behavior, not to demonstrate a tradeable edge.

<br>

## Development

```bash
make install-dev       # Create venv + install all dependencies
make test              # Run pytest suite (230 tests)
make lint              # Run ruff linter
make format            # Auto-format with ruff
```

<br>

## References

<table>
<tr><td>1</td><td>Cont, R., Kukanov, A., Stoikov, S. (2014). "The Price Impact of Order Book Events." <i>Journal of Financial Econometrics</i>, 12(1), 47–88.</td></tr>
<tr><td>2</td><td>Easley, D., López de Prado, M., O'Hara, M. (2012). "Flow Toxicity and Liquidity in a High Frequency World." <i>Review of Financial Studies</i>, 25(5), 1457–1493.</td></tr>
<tr><td>3</td><td>Hamilton, J.D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle." <i>Econometrica</i>, 57(2), 357–384.</td></tr>
<tr><td>4</td><td>Kyle, A.S. (1985). "Continuous Auctions and Insider Trading." <i>Econometrica</i>, 53(6), 1315–1335.</td></tr>
</table>

<br>

<div align="center">

---

*Built with Python, C++, and quantitative curiosity.*

</div>

### Core Implementation Code & Architecture
#### File: `data/__init__.py`
```python

```

#### File: `dashboard/components/__init__.py`
```python
"""Dashboard visualization components."""
```

#### File: `dashboard/__init__.py`
```python
"""LOB Regime Scanner Dashboard package."""
```

#### File: `src/cpp/__init__.py`
```python
"""C++ LOB engine — optional high-performance order book reconstructor."""

try:
    from src.cpp._lob_cpp import LOBEngine, batch_reconstruct  # noqa: F401

    CPP_AVAILABLE = True
except ImportError:
    CPP_AVAILABLE = False
```

#### File: `src/__init__.py`
```python
"""LOB Regime Scanner - Market microstructure analytics platform."""

from src.book_reconstructor import (  # noqa: F401
    OrderBook,
    load_parquet,
    process_events_to_parquet,
    reconstruct,
    resample_snapshots,
    save_parquet,
    snapshots_to_dataframe,
)
from src.data_loader import (  # noqa: F401
    load,
    load_directory,
    load_snapshots,
    load_snapshots_directory,
)
```

#### File: `dashboard/__main__.py`
```python
"""Allow running the dashboard with ``python -m dashboard``.

CLI usage:
    python -m dashboard --symbol BTCUSDT --start 2025-01-01 --end 2025-01-14
    python -m dashboard --demo
"""

import logging

from dashboard.app import create_app, parse_args

if __name__ == "__main__":
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    app = create_app(args)
    app.run(debug=args.debug, host=args.host, port=args.port)
```


==================================================


## [3/3] Repository: lob-world-models (`PHASE4-QUANT-055`)
- **Full Name**: `PHASE4-QUANT-055_Jeonghwan-Cheon__lob-world-models`
- **Description**: Implementation of the paper <Model-based Reinforcement Learning for Predictions and Control for Limit Order Books (Wei et al., J.P. Morgan AI Research, 2019)>.
- **GitHub Stars**: 12
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# mbrl-lob
Implementation of the paper <Model-based Reinforcement Learning for Predictions and Control for Limit Order Books (Wei et al., 2019)>.

## Datasets
![Market microstructure and limit order book](./sources/market_microstructure_and_limit_order_book.png)

## Neural networks
![Three neural networks model of financial world](./sources/three_neural_networks_model_of_financial_world.png)

## Model-based reinforcement learning
![Model based reinforcement learning.png](./sources/model_based_reinforcement_learning.png)


==================================================
