# ⚡ [QUANT-SOURCE-193] Consolidated Quant & Algo Trading Repositories
**Category**: `EVENT_DRIVEN_BACKTESTERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_193_EVENT_DRIVEN_BACKTESTERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: nautilus_trader (`VAULT_IN-QUANT-098_nautechsystems__nautilus_trader`)
- **Full Name**: `IN-QUANT-098_nautechsystems__nautilus_trader`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# <img src="https://github.com/nautechsystems/nautilus_trader/raw/develop/assets/nautilus-trader-logo.png" alt="NautilusTrader" width="500">

[![rustc](https://img.shields.io/crates/msrv/nautilus-core?color=ea7233&logo=rust&label=rustc)](https://crates.io/crates/nautilus-core)
[![crates.io](https://img.shields.io/crates/v/nautilus-core?logo=rust)](https://crates.io/crates/nautilus-core)
[![codspeed](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://codspeed.io/nautechsystems/nautilus_trader)
![pythons](https://img.shields.io/pypi/pyversions/nautilus_trader)
![pypi-version](https://img.shields.io/pypi/v/nautilus_trader)
[![Downloads](https://img.shields.io/pepy/dt/nautilus-trader?color=blue)](https://pepy.tech/projects/nautilus-trader)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.gg/NautilusTrader)

| Branch    | Version                                                                                                                                                                                                                     | Status                                                                                                                                                                                            |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `master`  | [![version](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnautechsystems%2Fnautilus_trader%2Fmaster%2Fversion.json)](https://packages.nautechsystems.io/simple/nautilus-trader/index.html)  | [![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml)  |
| `nightly` | [![version](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnautechsystems%2Fnautilus_trader%2Fnightly%2Fversion.json)](https://packages.nautechsystems.io/simple/nautilus-trader/index.html) | [![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=nightly)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml) |
| `develop` | [![version](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnautechsystems%2Fnautilus_trader%2Fdevelop%2Fversion.json)](https://packages.nautechsystems.io/simple/nautilus-trader/index.html) | [![build](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml/badge.svg?branch=develop)](https://github.com/nautechsystems/nautilus_trader/actions/workflows/build.yml) |

| Platform           | Rust   | Python    |
| :----------------- | :----- | :-------- |
| `Linux (x86_64)`   | 1.98.1 | 3.12-3.14 |
| `Linux (ARM64)`    | 1.98.1 | 3.12-3.14 |
| `macOS (ARM64)`    | 1.98.1 | 3.12-3.14 |
| `Windows (x86_64)` | 1.98.1 | 3.12-3.14 |

- **Docs**: <https://nautilustrader.io/docs/>
- **Website**: <https://nautilustrader.io>
- **Support**: [support@nautilustrader.io](mailto:support@nautilustrader.io)

## Introduction

NautilusTrader is an open-source, production-grade, Rust-native engine for multi-asset,
multi-venue trading systems.

The system spans research, deterministic simulation, and live execution within a single
event-driven architecture, with Python serving as the control plane for strategy logic,
configuration, and orchestration.

This separation provides the performance and safety of a compiled trading engine with
the flexibility of Python for system composition and strategy development.
Trading systems can also be written entirely in Rust for mission-critical workloads.

The same strategy and execution-algorithm code can run across backtest and live systems, reducing
deployment divergence. Live execution still introduces venue, transport, timing, persistence,
external-activity, and reconciliation behavior that a simulation may not reproduce. See
[Backtest and live differences](docs/concepts/live.md#backtest-and-live-differences).

NautilusTrader is asset-class-agnostic. Any venue with a REST API or WebSocket feed can be
integrated through modular adapters. Current integrations span crypto exchanges (CEX and
DEX), traditional markets (FX, equities, futures, options), and betting exchanges.

![nautilus-trader](https://github.com/nautechsystems/nautilus_trader/raw/develop/assets/nautilus-trader.png "nautilus-trader")

## Features

- **Fast**: Rust core with the [mimalloc](https://crates.io/crates/mimalloc) allocator and asynchronous networking using [tokio](https://crates.io/crates/tokio).
- **Reliable**: Type- and thread-safety backed by Rust, with optional Redis-backed state persistence.
- **Portable**: Runs on Linux, macOS, and Windows. Deploy using Docker.
- **Flexible**: Modular adapters integrate any REST API or WebSocket feed.
- **Advanced**: Time in force `IOC`, `FOK`, `GTC`, `GTD`, `DAY`, `AT_THE_OPEN`, `AT_THE_CLOSE`, advanced order types and conditional triggers. Execution instructions `post-only`, `reduce-only`, and icebergs. Contingency orders including `OCO`, `OUO`, `OTO`.
- **Customizable**: User-defined components, or assemble entire systems from scratch using the [cache](https://nautilustrader.io/docs/latest/concepts/cache) and [message bus](https://nautilustrader.io/docs/latest/concepts/message_bus).
- **Backtesting**: Multiple venues, instruments, and strategies simultaneously using historical quote tick, trade tick, bar, order book, and custom data with nanosecond resolution.
- **Live**: Identical strategy implementations between research and live deployment.
- **Multi-venue**: Run market-making and cross-venue strategies across multiple venues simultaneously.
- **AI Training**: Engine fast enough to train AI trading agents (RL/ES).

![nautilus](https://github.com/nautechsystems/nautilus_trader/raw/develop/assets/nautilus-art.png "nautilus")

> *nautilus - from ancient Greek 'sailor' and naus 'ship'.*
>
> *The nautilus shell consists of modular chambers with a growth factor which approximates a logarithmic spiral.
> The idea is that this can be translated to the aesthetics of design and architecture.*

## Why NautilusTrader?

Trading strategy research is often conducted in Python using vectorized approaches, while
production trading systems are implemented separately using event-driven architectures in
compiled languages.

NautilusTrader removes this separation.

A Rust-native core provides a deterministic event-driven runtime for both research and live
execution, while Python serves as the control plane. The same architecture, execution
semantics, and time model operate across both environments, allowing strategies to move
from research to production without reimplementation.

Python bindings are provided via [PyO3](https://pyo3.rs) for the Rust-native v2 runtime.
During the v2 transition, v1 receives only critical security backports on the `develop_v1` branch.
See the [v2 migration guide](https://github.com/nautechsystems/nautilus_trader/blob/develop/MIGRATION_V2.md) for migration steps and compatibility details.
No Rust toolchain is required to install prebuilt wheels.

This project makes the [Soundness Pledge](https://raphlinus.github.io/rust/2020/01/18/soundness-pledge.html):

> "The intent of this project is to be free of soundness bugs.
> The developers will do their best to avoid them, and welcome help in analyzing and fixing them."

> [!NOTE]
>
> **MSRV:** NautilusTrader relies heavily on improvements in the Rust language and compiler.
> As a result, the Minimum Supported Rust Version (MSRV) is generally equal to the latest stable release of Rust.

## Integrations

NautilusTrader is modularly designed to work with *adapters*, enabling connectivity to trading venues
and data providers by translating their raw APIs into a unified interface and normalized domain model.

The following integrations are currently supported; see [docs/integrations/](https://nautilustrader.io/docs/latest/integrations/) for details:

| Name                                                       | ID                    | Type                    | Status                                               | Docs                                              |
| :--------------------------------------------------------- | :-------------------- | :---------------------- | :--------------------------------------------------- | :------------------------------------------------ |
| [AX Exchange](https://architect.exchange)                  | `AX`                  | Perpetuals Exchange     | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/architect_ax.md)        |
| [Betfair](https://betfair.com)                             | `BETFAIR`             | Sports Betting Exchange | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/betfair.md)             |
| [Binance](https://binance.com)                             | `BINANCE`             | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/binance.md)             |
| [BitMEX](https://www.bitmex.com)                           | `BITMEX`              | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/bitmex.md)              |
| [Bybit](https://www.bybit.com)                             | `BYBIT`               | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/bybit.md)               |
| [Coinbase](https://coinbase.com)                           | `COINBASE`            | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/coinbase.md)            |
| [Databento](https://databento.com)                         | `DATABENTO`           | Data Provider           | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/databento.md)           |
| [Deribit](https://www.deribit.com)                         | `DERIBIT`             | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/deribit.md)             |
| [Derive](https://www.derive.xyz)                           | `DERIVE`              | Crypto Exchange (DEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/derive.md)              |
| [dYdX](https://dydx.trade)                                 | `DYDX`                | Crypto Exchange (DEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/dydx.md)                |
| [Hyperliquid](https://hyperliquid.xyz)                     | `HYPERLIQUID`         | Crypto Exchange (DEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/hyperliquid.md)         |
| [Interactive Brokers](https://www.interactivebrokers.com)  | `INTERACTIVE_BROKERS` | Brokerage (multi-venue) | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/interactive_brokers.md) |
| [Kraken](https://kraken.com)                               | `KRAKEN`              | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/kraken.md)              |
| [Lighter](https://lighter.xyz)                             | `LIGHTER`             | Crypto Exchange (DEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/lighter.md)             |
| [Lighter on Robinhood](https://robinhoodchain.lighter.xyz) | `LIGHTER_ROBINHOOD`   | Crypto Exchange (DEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/lighter.md)             |
| [OKX](https://okx.com)                                     | `OKX`                 | Crypto Exchange (CEX)   | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/okx.md)                 |
| [Polymarket](https://polymarket.com)                       | `POLYMARKET`          | Prediction Market (DEX) | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/polymarket.md)          |
| [Tardis](https://tardis.dev)                               | `TARDIS`              | Crypto Data Provider    | ![status](https://img.shields.io/badge/stable-green) | [Guide](docs/integrations/tardis.md)              |

- **ID**: The default client ID for the integrations adapter clients.
- **Type**: The type of integration (often the venue type).

For Lighter on Robinhood, `LIGHTER_ROBINHOOD` is the venue and explicit client ID to register. The
shared Lighter factory keeps `LIGHTER` as its compatibility default.

### Status

- `planned`: Planned for future development.
- `building`: Under construction and likely not in a usable state.
- `beta`: Completed to a minimally working state and in a beta testing phase.
- `stable`: Stabilized feature set and API, the integration has been tested by both developers and users to a reasonable level (some bugs may still remain).

See the [Integrations](https://nautilustrader.io/docs/latest/integrations/) documentation for further details.

## Roadmap

The [Roadmap](https://github.com/nautechsystems/nautilus_trader/blob/develop/ROADMAP.md) outlines NautilusTrader's strategic direction.
Current priorities include stabilizing the Rust-native core, improving documentation, and enhancing code ergonomics.

The open-source project focuses on single-node backtesting and live trading for individual and small-team quantitative traders.
UI dashboards, distributed orchestration, and built-in AI/ML tooling are out of scope to maintain focus on the core engine and ecosystem sustainability.

New integration proposals should start with an RFC issue to discuss suitability before submitting a PR.
See [Community-contributed integrations](https://github.com/nautechsystems/nautilus_trader/blob/develop/ROADMAP.md#community-contributed-integrations) for guidelines.

## Security

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/nautechsystems/nautilus_trader/badge)](https://scorecard.dev/viewer/?uri=github.com/nautechsystems/nautilus_trader)

Security is a priority for the NautilusTrader project, and we value the work of those who help
identify and resolve vulnerabilities. We apply layered controls across the development and release
lifecycle, with signed releases, continuous vulnerability management, and transparent development
practices:

- **Source and review controls**: CODEOWNERS gate critical infrastructure, dependency manifests, and
  lock files; protected branches require signed commits and passing CI; release tags are immutable;
  and Rust dependencies are sourced only from crates.io.
- **Dependency intake**: lock files pin every dependency with cryptographic checksums, third-party
  Python packages install from wheels only, new dependency and tooling versions observe a
  publication cooldown before adoption, cargo-vet audits Rust provenance, and cargo-deny checks Rust
  dependencies against an allow list of licenses compatible with NautilusTrader's `LGPL-3.0-only`
  license.
- **Scanning and fuzzing**: Gitleaks secret screening and Zizmor Actions auditing run pre-commit;
  CodeQL runs on PRs to `master` and pushes to `nightly`; cargo-audit, cargo-deny, cargo-vet,
  OSV Scanner, and pip-audit run on audit-relevant PRs and daily schedules; cargo-fuzz targets cover
  selected adapter and signing surfaces.
- **Build and release integrity**: GitHub Actions are pinned to commit SHAs, CI runners are hardened
  with egress allow-listing, Python artifacts carry SLSA build provenance, container images are
  Sigstore-signed with attested SPDX SBOMs, and PyPI and crates.io publishing uses OIDC Trusted
  Publishing gated to a protected `release` environment that never runs pull request or fork code.
- **Runtime cryptography**: TLS and most runtime cryptography use
  [aws-lc-rs](https://github.com/aws/aws-lc-rs), the Rust binding for AWS-LC, with Ed25519 signing
  via [ed25519-dalek](https://github.com/dalek-cryptography/curve25519-dalek).

The OpenSSF Scorecard badge above is one automated repository-health signal; it complements manual
review, CI hardening, and security audits rather than replacing them.

### Reporting a vulnerability

Report privately through
[GitHub Security Advisories](https://github.com/nautechsystems/nautilus_trader/security/advisories/new),
or email <security@nautechsystems.io> (PGP key available on request). We acknowledge reports within
48 hours and patch critical vulnerabilities within 30 days.

A careful vulnerability report takes real time and effort. We appreciate that, and unless you prefer
to remain anonymous, we credit reporters in the relevant security advisory and release notes.

The [Security Policy](SECURITY.md) details scope, coordinated disclosure, and step-by-step release
verification. The [Security Architecture](docs/developer_guide/security.md)
describes the release supply chain end-to-end. For the full policies, see the
[Responsible Disclosure](https://nautilustrader.io/security/responsible-disclosure/) and
[Supply Chain Security](https://nautilustrader.io/security/supply-chain/) policies; CI/CD security is
documented in [.github/OVERVIEW.md](.github/OVERVIEW.md#security).

## Versioning and releases

> [!WARNING]
>
> **NautilusTrader is still under active development**. Some features may be incomplete, and while
> the API is becoming more stable, breaking changes can occur between releases.
> We strive to document these changes in the release notes on a **best-effort basis**.

We aim to follow a **bi-weekly release schedule**, though experimental or larger features may cause delays.

### Branches

We aim to maintain a stable, passing build across all branches.

- `master`: Reflects the source code for the latest released version; recommended for production use.
- `nightly`: Daily snapshots of the `develop` branch for early testing; merged at **14:00 UTC** and as required.
- `develop`: Active development branch for contributors and feature work.

> [!NOTE]
>
> The v2 release-candidate line is the transition toward a **stable API for version 2.x**.
> Once this milestone is reached, we plan to implement a formal deprecation process for any API changes.
> This approach allows us to maintain a rapid development pace for now.

## Precision mode

NautilusTrader supports two precision modes for its core value types (`Price`, `Quantity`, `Money`),
which differ in their internal bit-width and maximum decimal precision.

- **High-precision**: 128-bit integers with up to 16 decimals of precision, and a larger value range.
- **Standard-precision**: 64-bit integers with up to 9 decimals of precision, and a smaller value range.

> [!NOTE]
>
> By default, the official Python wheels ship in high-precision (128-bit) mode on all supported platforms.
>
> For pure Rust crates, high-precision works on all platforms (including Windows) since Rust handles
> `i128`/`u128` via software emulation. The default is standard-precision unless you explicitly enable
> the `high-precision` feature flag.

See the [Installation Guide](https://nautilustrader.io/docs/latest/getting_started/installation) for further details.

**Rust feature flag**: To enable high-precision mode in Rust, add the `high-precision` feature to your Cargo.toml:

```toml
[dependencies]
nautilus_model = { version = "*", features = ["high-precision"] }
```

## Installation

We recommend using the latest supported version of Python and installing [nautilus_trader](https://pypi.org/project/nautilus_trader/) inside a virtual environment to isolate dependencies.

**There are two supported ways to install**:

1. Pre-built binary wheel from PyPI *or* the Nautech Systems package index.
2. Build from source.

> [!TIP]
>
> We highly recommend installing using the [uv](https://docs.astral.sh/uv) package manager with a "vanilla" CPython.
>
> Conda and other Python distributions *may* work but aren't officially supported.

### From PyPI

This repository and the [documentation](https://nautilustrader.io/docs/latest) cover v2. To install
the v2 release-candidate wheels from PyPI using Python's pip package manager:

```bash
pip install -U nautilus_trader --pre
```

The v2 release-candidate wheels use `2.0.0rcN` versions and are intended for community testing
before the final `2.0.0` release. We do not recommend using release candidates in production
environments, such as live trading controlling real capital.

The `--pre` flag is required until `2.0.0` is released. Without it, pip installs the latest stable
v1 wheel, whose Python API differs from the v2 documentation:

```bash
# Installs the latest stable v1 wheel, which cannot run the v2 documentation
pip install -U nautilus_trader
```

Install optional dependencies for interactive tearsheets and charts with the `visualization` extra:

```bash
pip install -U "nautilus_trader[visualization]" --pre
```

See the [Installation Guide](https://nautilustrader.io/docs/latest/getting_started/installation#extras) for details.

### From the Nautech Systems package index

The Nautech Systems package index (`packages.nautechsystems.io`) complies with [PEP-503](https://peps.python.org/pep-0503/) and hosts both stable and development binary wheels for `nautilus_trader`.
This enables users to install either the latest stable release or pre-release versions for testing.

#### Stable wheels

Stable wheels correspond to official releases of `nautilus_trader` on PyPI, and use standard versioning.

To install the latest stable release:

```bash
pip install -U nautilus_trader --index-url=https://packages.nautechsystems.io/simple
```

> [!TIP]
>
> Use `--extra-index-url` instead of `--index-url` if you want pip to fall back to PyPI automatically.

#### Development wheels

The main package index publishes v2 development wheels from both the `nightly` and `develop`
branches, allowing users to test features and fixes ahead of stable releases.

This process also helps preserve compute resources and provides easy access to the exact binaries tested in CI pipelines,
while adhering to [PEP-440](https://peps.python.org/pep-0440/) versioning standards:

- `develop` wheels use the version suffix `.devYYYYMMDD+run`.
- `nightly` wheels use `.devYYYYMMDD` when the base version is already a pre-release, and
  `aYYYYMMDD` otherwise.

| Platform           | Develop | Nightly |
| :----------------- | :------ | :------ |
| `Linux (x86_64)`   | ✓       | ✓       |
| `Linux (ARM64)`    | -       | ✓       |
| `macOS (ARM64)`    | -       | ✓       |
| `Windows (x86_64)` | -       | ✓       |

> [!WARNING]
>
> We do not recommend using development wheels in production environments, such as live trading controlling real capital.

#### Installation commands

By default, pip will install the latest stable release. Adding the `--pre` flag ensures that pre-release versions, including development wheels, are considered.

To install the latest available pre-release (including development wheels):

```bash
pip install -U nautilus_trader --pre --index-url=https://packages.nautechsystems.io/simple
```

#### Available versions

You can view all available versions of `nautilus_trader` on the [package index](https://packages.nautechsystems.io/simple/nautilus-trader/index.html).

To programmatically fetch and list available versions:

```bash
curl -s https://packages.nautechsystems.io/simple/nautilus-trader/index.html | sed -n 's/.*<a href="\([^"]*\)".*/\1/p' | awk -F'#' '{print $1}' | sort
```

> [!IMPORTANT]
>
> On Linux, confirm your glibc version with `ldd --version` and ensure it reports **2.35** or newer before installing binary wheels.

#### Branch updates

- `develop` branch wheels (`.devYYYYMMDD+run`): Build and publish continuously with every merged commit.
- `nightly` branch wheels (`.devYYYYMMDD` or `aYYYYMMDD`): Build and publish daily when we
  automatically merge the `develop` branch at **14:00 UTC** (if there are changes).

#### Retention policies

- `develop` branch wheels: We retain only the most recent wheel build.
- `nightly` branch wheels: We retain only the 30 most recent publication dates per platform.

#### Verifying build provenance

All release artifacts published by the project carry cryptographic attestations
generated by the CI/CD pipeline:

- Python wheels and source distribution (PyPI, GitHub Releases, Nautech Systems package index): [SLSA](https://slsa.dev/) build provenance.
- Docker images (`ghcr.io/nautechsystems/nautilus_t
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `crates/adapters/architect_ax/test_data/http_cancel_all_orders.json`
```python
{}
```

#### File: `crates/adapters/binance/test_data/spot/http_json/ping_response.json`
```python
{}
```

#### File: `crates/adapters/polymarket/test_data/http_version_response.json`
```python
{
  "version": 2
}
```

#### File: `crates/adapters/architect_ax/test_data/http_cancel_order.json`
```python
{
  "cxl_rx": true
}
```

#### File: `crates/adapters/architect_ax/test_data/http_initial_margin_requirement.json`
```python
{
  "im": "1250.50"
}
```

#### File: `crates/adapters/polymarket/test_data/clob_fee_rate_response_zero.json`
```python
{
    "base_fee": "0"
}
```


==================================================


## [2/3] Repository: bt (`VAULT_IN-QUANT-105_pmorissette__bt`)
- **Full Name**: `IN-QUANT-105_pmorissette__bt`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# bt — Flexible Backtesting for Python

[![Build Status](https://github.com/pmorissette/bt/workflows/Build%20Status/badge.svg)](https://github.com/pmorissette/bt/actions/)
[![PyPI Version](https://img.shields.io/pypi/v/bt)](https://pypi.org/project/bt/)
[![PyPI License](https://img.shields.io/pypi/l/bt)](https://pypi.org/project/bt/)

<a id="what-is-bt"></a>

Build, test, and compare investment strategies from reusable Python components.
bt combines strategy logic with historical price data, tracks portfolio positions
and transactions, and provides performance statistics and charts through
[ffn](https://github.com/pmorissette/ffn).

<a id="features"></a>

- **Compose strategy logic:** combine algorithms for scheduling, security selection, weighting, and rebalancing.
- **Build portfolios of strategies:** nest strategies and securities in a common tree.
- **Model trading costs:** configure commissions and transaction cost models.
- **Compare results:** inspect returns, weights, transactions, drawdowns, and other statistics.

## Install

```bash
pip install bt
```

See the [installation guide](docs/source/install.md) for additional details.

<a id="a-quick-example"></a>
<a id="a-simple-strategy-backtest"></a>

## A first backtest

This example uses synthetic prices, so it runs without downloading market data:

```python
import numpy as np
import pandas as pd

import bt

prices = pd.DataFrame(
    {
        "asset_a": np.linspace(100, 120, 252),
        "asset_b": np.linspace(100, 110, 252),
    },
    index=pd.bdate_range("2020-01-01", periods=252),
)

strategy = bt.Strategy(
    "equal_weight",
    [
        bt.algos.RunMonthly(),
        bt.algos.SelectAll(),
        bt.algos.WeighEqually(),
        bt.algos.Rebalance(),
    ],
)
result = bt.run(bt.Backtest(strategy, prices))
result.display()
```

The strategy selects both assets, gives each equal weight, and rebalances monthly.
Replace the synthetic prices with your own data to explore a strategy. Backtest
results depend on data quality and modeling assumptions; they do not predict
future performance.

<a id="modifying-a-strategy"></a>

## Explore the documentation

- [First strategy tutorial](docs/source/intro.md): walk through a backtest and inspect its results.
- [Algorithms](docs/source/algos.md): compose and customize strategy logic.
- [Portfolio trees](docs/source/tree.md): combine securities and nested strategies.
- [Examples](docs/source/examples.md): explore momentum, risk allocation, and fixed-income strategies.
- [API overview](docs/source/overview.md): find strategy, algorithm, and backtest interfaces.

The published documentation is at <https://pmorissette.github.io/bt/>.

<a id="roadmap"></a>

## Contribute

See the [development guide](docs/development.md) for environment setup, tests,
documentation builds, and Copier template updates. Report bugs and propose
improvements through [GitHub issues](https://github.com/pmorissette/bt/issues).

bt is released under the [MIT license](LICENSE).

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `bt/__init__.py`
```python
import ffn
from ffn import data, get, merge, utils

from . import algos, backtest, core
from .backtest import Backtest, run
from .core import (
    Algo,
    AlgoStack,
    AlmgrenChrissCostModel,
    CostModel,
    CouponPayingHedgeSecurity,
    CouponPayingSecurity,
    FixedIncomeSecurity,
    FixedIncomeStrategy,
    HedgeSecurity,
    Security,
    SqrtCostModel,
    Strategy,
)

__version__ = "1.2.3"
```

#### File: `examples/buy_and_hold.py`
```python
if __name__ == "__main__":

    import numpy as np
    import pandas as pd

    import ffn
    import bt


    names = ['foo','bar','rf']
    dates = pd.date_range(start='2017-01-01',end='2017-12-31', freq=pd.tseries.offsets.BDay())
    n = len(dates)
    rdf = pd.DataFrame(
        np.zeros((n, len(names))),
        index = dates,
        columns = names
    )

    np.random.seed(1)
    rdf['foo'] = np.random.normal(loc = 0.1/n,scale=0.2/np.sqrt(n),size=n)
    rdf['bar'] = np.random.normal(loc = 0.04/n,scale=0.05/np.sqrt(n),size=n)
    rdf['rf'] = np.random.normal(loc=0.02/ n, scale=0.01 / np.sqrt(n), size=n)

    pdf = 100*np.cumprod(1+rdf)

    # algo to fire on the beginning of every month and to run on the first date
    runMonthlyAlgo = bt.algos.RunMonthly(
        run_on_first_date=True,
        run_on_end_of_period=True
    )

    # algo to set the weights in the temp dictionary\
    weights = pd.Series([0.6,0.4,0.],index = rdf.columns)
    weighSpecifiedAlgo = bt.algos.WeighSpecified(**weights)


    # algo to rebalance the current weights to weights set in temp dictionary
    rebalAlgo = bt.algos.Rebalance()

    # a strategy that rebalances monthly to specified weights
    s = 'monthly'
    strat = bt.Strategy(s,
                    [
                        runMonthlyAlgo,
                        weighSpecifiedAlgo,
                        rebalAlgo
                    ]
    )
    """
    runMonthlyAlgo will return True on the last day of the month.
    If runMonthlyAlgo returns True, then weighSpecifiedAlgo will set the weights and return True.
    If weighSpecifiedAlgo returns True, then rebalAlgo will rebalance the portfolio to match the
        target weights.
    """

    # set integer_positions=False when positions are not required to be integers(round numbers)
    backtest = bt.Backtest(
        strat,
        pdf,
        integer_positions=False
    )

    res = bt.run(backtest)

    # set riskfree as the rf index
    res.set_riskfree_rate(pdf['rf'])


    wait=1
```

#### File: `tests/bench.py`
```python
"""
Performance benchmarks
"""
import numpy as np
import pandas as pd
import bt
import cProfile


def benchmark_1():
    x = np.random.randn(10000, 1000) * 0.01
    idx = pd.date_range("1990-01-01", freq="B", periods=x.shape[0])
    data = np.exp(pd.DataFrame(x, index=idx).cumsum())

    s = bt.Strategy(
        "s",
        [
            bt.algos.RunMonthly(),
            bt.algos.SelectRandomly(len(data.columns) / 2),
            bt.algos.WeighRandomly(),
            bt.algos.Rebalance(),
        ],
    )

    t = bt.Backtest(s, data)
    return bt.run(t)


def benchmark_2():
    x = np.random.randn(10000, 1000) * 0.01
    idx = pd.date_range("1990-01-01", freq="B", periods=x.shape[0])
    data = np.exp(pd.DataFrame(x, index=idx).cumsum())
    bidoffer = data * 0.01
    coupons = data * 0.0
    s = bt.FixedIncomeStrategy(
        "s",
        algos=[
            bt.algos.RunMonthly(),
            bt.algos.SelectRandomly(len(data.columns) / 2),
            bt.algos.WeighRandomly(),
            bt.algos.Rebalance(),
        ],
        children=[bt.CouponPayingSecurity(c) for c in data],
    )

    t = bt.Backtest(s, data, additional_data={"bidoffer": bidoffer, "coupons": coupons})
    return bt.run(t)


def benchmark_3():
    # Similar to benchmark_1, but with trading in only a small subset of assets
    # However, because the "multipier" is used, we can't just pass the string
    # names to the constructor, and so the solution is to use the lazy_add flag.
    # Changing lazy_add to False demonstrates the performance gain.
    # i.e. on Win32, it went from 4.3s with the flag to 10.9s without.

    x = np.random.randn(10000, 1000) * 0.01
    idx = pd.date_range("1990-01-01", freq="B", periods=x.shape[0])
    data = np.exp(pd.DataFrame(x, index=idx).cumsum())
    children = [bt.Security(name=i, multiplier=10, lazy_add=False) for i in range(1000)]
    s = bt.Strategy(
        "s",
        [
            bt.algos.RunMonthly(),
            bt.algos.SelectThese([0, 1]),
            bt.algos.WeighRandomly(),
            bt.algos.Rebalance(),
        ],
        children=children,
    )

    t = bt.Backtest(s, data)
    return bt.run(t)


if __name__ == "__main__":
    print("\n\n\n================= Benchmark 1 =======================\n")
    cProfile.run("benchmark_1()", sort="tottime")
    print("\n----------------- Benchmark 1 -----------------------\n\n\n")

    print("\n\n\n================= Benchmark 2 =======================\n")
    cProfile.run("benchmark_2()", sort="tottime")
    print("\n----------------- Benchmark 2 -----------------------\n\n\n")

    print("\n\n\n================= Benchmark 3 =======================\n")
    cProfile.run("benchmark_3()", sort="cumtime")
    print("\n----------------- Benchmark 3 -----------------------\n\n\n")
```

#### File: `benchmarks/test_backtest.py`
```python
import numpy as np
import pandas as pd
import pytest

import bt


@pytest.fixture(
    scope="module",
    params=[(252, 10), (1000, 50)],
    ids=["1y-10-assets", "4y-50-assets"],
)
def prices(request):
    periods, assets = request.param
    rng = np.random.default_rng(42)
    returns = rng.normal(0.0002, 0.01, size=(periods, assets))
    return pd.DataFrame(
        100.0 * np.exp(returns.cumsum(axis=0)),
        index=pd.date_range("2010-01-01", periods=periods, freq="B"),
        columns=[f"asset_{index}" for index in range(assets)],
    )


@pytest.fixture(scope="module")
def fixed_income_data(prices):
    return {
        "bidoffer": prices * 0.001,
        "coupons": prices * 0.0001,
    }


def make_strategy(name):
    return bt.Strategy(
        name,
        [
            bt.algos.RunMonthly(),
            bt.algos.SelectAll(),
            bt.algos.WeighEqually(),
            bt.algos.Rebalance(),
        ],
    )


def run_equity_backtest(prices):
    backtest = bt.Backtest(make_strategy("equity"), prices)
    return bt.run(backtest, progress_bar=False)


def run_fixed_income_backtest(prices, additional_data, funded=False):
    strategy = bt.FixedIncomeStrategy(
        "fixed-income",
        [
            bt.algos.RunMonthly(),
            bt.algos.SelectAll(),
            bt.algos.WeighEqually(),
            *([bt.algos.SetNotional("notional")] if funded else []),
            bt.algos.Rebalance(),
        ],
        children=[bt.CouponPayingSecurity(column) for column in prices.columns],
    )
    backtest = bt.Backtest(strategy, prices, additional_data=additional_data)
    return bt.run(backtest, progress_bar=False)


@pytest.fixture(scope="module")
def completed_strategy(prices):
    backtest = bt.Backtest(make_strategy("history"), prices)
    backtest.run()
    return backtest.strategy


@pytest.mark.benchmark(group="backtest")
def test_equity_backtest(benchmark, prices):
    result = benchmark(run_equity_backtest, prices)

    assert result.prices.shape[0] == prices.shape[0] + 1


@pytest.mark.benchmark(group="backtest")
def test_fixed_income_backtest(benchmark, prices, fixed_income_data):
    result = benchmark(run_fixed_income_backtest, prices, fixed_income_data)

    assert result.prices.shape[0] == prices.shape[0] + 1


@pytest.mark.benchmark(group="backtest")
def test_funded_fixed_income_backtest(benchmark, prices, fixed_income_data):
    additional_data = {**fixed_income_data, "notional": pd.Series(10000.0, index=prices.index)}
    result = benchmark(run_fixed_income_backtest, prices, additional_data, funded=True)

    strategy = result.backtests["fixed-income"].strategy
    assert strategy.notional_value > 0
    assert sum(security.coupons.sum() for security in strategy.securities) > 0


@pytest.mark.benchmark(group="history")
def test_strategy_prices(benchmark, prices, completed_strategy):
    result = benchmark(getattr, completed_strategy, "prices")

    assert result.index[-1] == prices.index[-1]


@pytest.mark.benchmark(group="history")
def test_strategy_data(benchmark, prices, completed_strategy):
    result = benchmark(getattr, completed_strategy, "data")

    assert result.index[-1] == prices.index[-1]
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["hatchling", "hatch-cython", "Cython>=0.29.25", "setuptools"]
build-backend = "hatchling.build"

[project]
name = "bt"
version = "1.2.3"
description = "A flexible backtesting framework for Python"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.9"
authors = [
    { name = "Philippe Morissette", email = "morissette.philippe@gmail.com" },
]
keywords = [
    "python",
    "finance",
    "quant",
    "backtesting",
    "strategies",
    "algotrading",
    "algorithmic",
    "trading",
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries",
    "License :: OSI Approved :: MIT License",
]
dependencies = [
    "ffn>=1.1.2",
    "pyprind>=2.11",
    "tqdm>=4",
]

[project.optional-dependencies]
develop = [
    "build",
    "bump-my-version",
    "check-dist",
    "cibuildwheel",
    "codespell",
    "cython>=0.29.25",
    "ffn>=1.1.2",
    "hatchling",
    "hatch-cython",
    "klink>=0.1.13",
    "matplotlib>=2",
    "mdformat",
    "mdformat-myst",
    "mdformat-tables>=1",
    "numpy>=1",
    "pandas>=0.19",
    "pyprind>=2.11",
    "pytest",
    "pytest-benchmark",
    "pytest-cov",
    "ruff",
    "setuptools",
    "twine>=6.1",
    "ty",
    "uv",
    "wheel",
    "yardang>=0.10.0",
]
dev = ["bt[develop]"]

[project.urls]
Homepage = "https://github.com/pmorissette/bt"
Repository = "https://github.com/pmorissette/bt"
Documentation = "https://pmorissette.github.io/bt/"

[tool.bumpversion]
current_version = "1.2.3"
commit = true
tag = true
commit_args = "-s"

[[tool.bumpversion.files]]
filename = "bt/__init__.py"
search = '__version__ = "{current_version}"'
replace = '__version__ = "{new_version}"'

[[tool.bumpversion.files]]
filename = "pyproject.toml"
search = 'version = "{current_version}"'
replace = 'version = "{new_version}"'

[tool.pytest.ini_options]
addopts = ["-vvv", "--junitxml=junit.xml"]
testpaths = ["tests"]

[tool.coverage.run]
branch = true
omit = ["bt/core.py"]

[tool.coverage.report]
exclude_also = ["raise NotImplementedError", "if __name__ == .__main__.:", "@(abc\\.)?abstractmethod"]
fail_under = 50

[tool.hatch.build.targets.sdist]
include = [
    "/bt",
    "/LICENSE",
    "/README.md",
    "/pyproject.toml",
]

[tool.hatch.build.targets.wheel]
packages = ["bt"]
artifacts = [
    "bt/*.so",
    "bt/*.pyd",
    "bt/*.dylib",
]

[tool.hatch.build.targets.wheel.hooks.cython]
dependencies = ["hatch-cython"]

[tool.hatch.build.targets.wheel.hooks.cython.options.files]
targets = ["*/core.py"]
exclude = [
    "*/__init__.py",
    "*/algos.py",
    "*/backtest.py",
]

[tool.setuptools]
packages = ["bt"]

[tool.check-dist]
present = ["bt/__init__.py", "bt/algos.py", "bt/backtest.py", "bt/core.py"]
absent = ["klink/*", "tests/*", "docs/*"]

[tool.check-dist.sdist]
present = ["LICENSE", "README.md", "pyproject.toml"]
absent = ["bt/*.so", "bt/*.pyd", "bt/*.dylib"]

[tool.check-dist.wheel]
present = ["bt/core*.so"]

[tool.cibuildwheel]
test-command = "python -c \"import bt.core; from importlib.machinery import EXTENSION_SUFFIXES; assert any(bt.core.__file__.endswith(s) for s in EXTENSION_SUFFIXES)\""

[tool.cibuildwheel.linux]
manylinux-aarch64-image = "manylinux_2_28"
manylinux-x86_64-image = "manylinux_2_28"
archs = "native"
skip = "*i686* *musllinux*"

[tool.cibuildwheel.macos]
environment = {MACOSX_DEPLOYMENT_TARGET="11.0"}
archs = "arm64"

[tool.cibuildwheel.windows]
archs = "AMD64"
skip = "*win32 *arm64"

[tool.codespell]
ignore-words-list = "strat"

[tool.ruff]
line-length = 180

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401", "F403"]

[tool.yardang]
title = "bt - Flexible Backtesting for Python"
theme = "klink"
docs-host = "https://pmorissette.github.io/bt/"
root = "README.md"
pages = [
    "docs/source/install.md",
    "docs/source/intro.md",
    "docs/source/algos.md",
    "docs/source/tree.md",
    "docs/source/examples.md",
    "docs/source/overview.md",
    "docs/development.md",
]
use-autoapi = false
use-search = false
nb-execution-mode = "off"
exclude-patterns = ["**/*.ipynb", "docs/source/_themes", "TODO.md", "base", "benched", "github", "klink", "python-template-cython", "yardang"]
extensions = ["sphinx.ext.intersphinx"]

[tool.yardang.html-theme-options]
github = "pmorissette/bt"

[tool.yardang.intersphinx-mapping]
ffn = ["https://pmorissette.github.io/ffn/", "https://pmorissette.github.io/ffn/objects.inv"]

[tool.yardang.redirects]
bt = "docs/source/overview.html"
"docs/source/bt" = "overview.html"
install = "docs/source/install.html"
algos = "docs/source/algos.html"
tree = "docs/source/tree.html"
examples = "docs/source/examples.html"
intro = "docs/source/intro.html"
modules = "docs/source/modules.html"
Buy_and_hold = "docs/source/Buy_and_hold.html"
Cost_Models = "docs/source/Cost_Models.html"
ERC = "docs/source/ERC.html"
Fixed_Income = "docs/source/Fixed_Income.html"
PTE = "docs/source/PTE.html"
Strategy_Combination = "docs/source/Strategy_Combination.html"
Target_Volatility = "docs/source/Target_Volatility.html"
Trend_1 = "docs/source/Trend_1.html"
Trend_2 = "docs/source/Trend_2.html"
examples-nb = "docs/source/examples-nb.html"
```


==================================================


## [3/3] Repository: survivorship-free-backtester (`VAULT_IN-QUANT-111_ReaperOAK__survivorship-free-backtester`)
- **Full Name**: `IN-QUANT-111_ReaperOAK__survivorship-free-backtester`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# AI-Trader Lab

**Honest, survivorship-corrected backtesting + paper trading for Indian equities — built entirely on free data.**

This is a personal research lab, not investment advice. Everything here is educational,
runs on pretend money, and shows drawdowns as loudly as returns. *Past performance is not
indicative of future results.*

---

## Why this exists

Most retail backtests quietly lie — they test the *past* using *today's* winning stocks
(survivorship bias), assume fractional shares that don't exist, and ignore tax. This lab
was built to do the honest version, using only free data sources, and to run a live paper
account against the result.

## What's genuinely built here

| Piece | File | What it does |
|---|---|---|
| **Data store** | `trading-lab/data_store.py` | DuckDB store of ~2,800 NSE stocks × 26 years. Bulk **NSE bhavcopy** ingest (1 request/day = whole market) + gentle yfinance deep-history seed. Zero repeat API calls. |
| **Survivorship correction** | `trading-lab/wayback_membership.py`, `fetch_delisted.py`, `survivorship_pit.py` | Reconstructs *point-in-time* Nifty 100/200/500 membership from the Internet Archive, recovers delisted-loser prices, and re-runs backtests honestly. The correction is real: raw momentum "Sharpe ~1.5" → **~1.0 corrected**. |
| **Strategy tournament** | `trading-lab/strategy_tournament.py` | ~15 strategies + ensembles/overlays, all survivorship-corrected. Winner: **ensemble + regime-cash** (blend momentum/low-vol/risk-adjusted-momentum, go to cash below the 200-day trend). |
| **After-tax simulator** | `trading-lab/aftertax_sim.py` | Lot-level FIFO with real Indian tax (20% STCG / 12.5% LTCG). Shows tax is the great equalizer between active strategies and buy-and-hold. |
| **Signal engine** | `trading-lab/signal_engine.py` | App-ready "what to hold now" from the store, with the corrected + after-tax stats attached so a fantasy number can't be shown. |
| **Live paper accounts** | `trading-lab/fund_sip.py`, `india_ledger.py` | (1) Two-fund monthly SIP into real Nifty 500 index + Momentum 50 funds (fractional units, real NAVs from mfapi.in). (2) Direct-stock ensemble-regime ledger. Both idempotent, cron-driven. |
| **SIP strategy research** | `trading-lab/sip_strategies.py`, `sip_robustness.py` | Tests dip-buying / rebalancing / regime overlays on a monthly SIP, after tax — and stress-tests whether the "edge" is real or just factor exposure. |

## Honest headline findings

- Survivorship inflates momentum by roughly **+0.4 to +0.9 Sharpe** depending on universe.
- Corrected, the best universe is **Nifty 500** (breadth survives the correction), ~1.0–1.2 Sharpe.
- **Ensemble + regime-cash** roughly halves drawdown (−38% → ~−18%) — insurance, not free alpha.
- After Indian tax, high-turnover strategies barely out-earn buy-and-hold; the win is a *smoother ride*.
- Intraday and daily "buy-the-dip" tricks die under honest testing (costs / factor-exposure in disguise).

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
# build the data store (first run pulls history; then it's local + free forever)
.venv/bin/python trading-lab/data_store.py backfill
.venv/bin/python trading-lab/data_store.py indexes
# see the current honest signal
.venv/bin/python trading-lab/signal_engine.py nifty500 ensemble_regime
```

Live paper accounts run via cron (see the `*.sh` wrappers — adjust the hard-coded paths
for your machine). Account state and the data store live under `~/.vibe-trading/` and are
**git-ignored** — never commit them.

## Data sources (all free)

NSE bhavcopy · Yahoo Finance (`yfinance`) · [mfapi.in](https://www.mfapi.in) fund NAVs ·
Internet Archive (point-in-time index membership) · Kaggle historical Nifty-50 weights.

## Standing on other people's shoulders (credits)

This lab was prototyped while studying these excellent open-source projects. The genuine
work here is the honest data pipeline, survivorship correction, and the tests above — but
the ideas were sharpened against:

- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)
- [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading)
- [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading)
- [polakowo/vectorbt](https://github.com/polakowo/vectorbt)

## Disclaimer

**Educational research only. This is not investment advice.** The author is **not** a
SEBI-registered investment adviser, and nothing here is a solicitation, a personalized
recommendation, or a promise of returns. Any funds, ETFs, or stocks named are **illustrative
examples of a methodology**, not recommendations to buy or sell. There are **no forward
return projections** — all figures are historical backtests (which overfit) on a strong
market era, and *past performance is not indicative of future results*. Everything runs on
**paper money**. Do your own research and consult a SEBI-registered adviser before investing
real money. Use at your own risk.

## License

**Source-available, not "open source."** Licensed under the **PolyForm Noncommercial
License 1.0.0** (see [`LICENSE`](LICENSE)):

- ✅ **Free for noncommercial use** — personal projects, research, learning, hobby use,
  and nonprofit / educational / government organizations.
- 💼 **Commercial use requires a paid license** from the author. If you or your company
  want to use this in a product, service, or anything directed toward commercial
  advantage, contact [@ReaperOAK](https://github.com/ReaperOAK) first to arrange terms.

Deliberate choice: share the work so people can learn from it — but nobody monetizes it
without the author.

### Core Implementation Code & Architecture
#### File: `trading-lab/ta_india_run.py`
```python
"""
ta_india_run.py — run TradingAgents (multi-agent LLM) on an INDIAN stock,
wired to our free OpenRouter model. Proof-of-concept that it CAN analyze
Indian stocks (yfinance .NS data flows in). Minimal rounds to limit LLM calls.
"""
import os, sys

# load OpenRouter key from our env file
envp = os.path.expanduser("~/.vibe-trading/.env")
for line in open(envp):
    line = line.strip()
    if line.startswith("OPENROUTER_API_KEY="):
        key = line.split("=", 1)[1]
        os.environ["OPENAI_API_KEY"] = key
        os.environ["OPENROUTER_API_KEY"] = key

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "ollama"
config["backend_url"] = "http://127.0.0.1:11434/v1"   # local Ollama, no rate limits
config["deep_think_llm"] = "qwen2.5:7b-instruct"
config["quick_think_llm"] = "qwen2.5:7b-instruct"
config["max_debate_rounds"] = 1
config["max_risk_discuss_rounds"] = 1
config["online_tools"] = True

ticker = sys.argv[1] if len(sys.argv) > 1 else "RELIANCE.NS"
date = sys.argv[2] if len(sys.argv) > 2 else "2025-06-30"
print(f"Analyzing {ticker} as of {date} with free model {config['deep_think_llm']}...\n", flush=True)

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate(ticker, date)
print("\n================ FINAL DECISION ================")
print(decision)
```

#### File: `trading-lab/min_balance.py`
```python
"""
min_balance.py — the minimum balance to actually RUN a whole-share strategy.

Two thresholds per strategy (whole shares, NSE):
  * BARE minimum   = can hold >=1 whole share of each of the N held names
                     (worst case = the N most expensive names).
  * COMFORTABLE min = capital where whole-share rounding wastes < ~10% as idle
                     cash (positions roughly match target weights).
Uses the current cached universe prices.
"""
from __future__ import annotations
import os, sys, warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(__file__))
import india_signal as strat

def universe_prices():
    df, held, weights, cash = strat.compute_targets()
    return df["price"].astype(float).sort_values()  # Series: symbol -> price

def comfortable_min(prices_of_held, target_frac=0.90):
    """Smallest capital where equal-weight whole-share deploys >= target_frac."""
    n = len(prices_of_held)
    for C in range(5000, 2_000_001, 5000):
        per = C / n
        shares = np.floor(per / prices_of_held)
        deployed = float((shares * prices_of_held).sum())
        if deployed / C >= target_frac and (shares >= 1).all():
            return C
    return None

def main():
    prices = universe_prices()
    print(f"Universe: {len(prices)} stocks, price range Rs {prices.min():,.0f}-{prices.max():,.0f}\n")
    print(f"{'strategy (hold N)':20}{'bare min':>14}{'comfortable min':>18}")
    print("-" * 52)
    for N in [6, 12]:
        priciest = prices.tail(N)                 # worst-case selection
        bare = float(priciest.sum())              # 1 share of each of the N priciest
        comf = comfortable_min(priciest.values)
        comf_s = f"Rs {comf:,.0f}" if comf else ">Rs 20L"
        print(f"hold-{N:<15}Rs {bare:>10,.0f}{comf_s:>18}")
    print("\nInterpretation for a Rs 10,000 account:")
    print("  -> below the bare minimum for BOTH -> can't run diversified stocks.")
    print("  -> honest path: Nifty index fund/ETF (fractional units) until the")
    print("     SIP grows the balance past the comfortable minimum.")

if __name__ == "__main__":
    main()
```

#### File: `trading-lab/wait_and_trade.py`
```python
"""
wait_and_trade.py — wait out the Yahoo data block, then trade automatically.

Every ~20 min: gently probe one US symbol. Once the feed responds, fetch the
whole universe into the CSV cache, then run the $100 paper rebalance and print
a plain-English report. Gives up after a few hours if still blocked.

Gentle by design (1 probe per cycle) so we don't keep re-arming the block.
"""
from __future__ import annotations
import os, sys, time
sys.path.insert(0, os.path.dirname(__file__))
import momentum_signal as strat
import warm_cache
import paper_ledger as pl

PROBE = "SPY"
MAX_ATTEMPTS = 6
WAIT = 1200          # 20 min between attempts
GAP = 6              # between symbols once unblocked


def main():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\n[attempt {attempt}/{MAX_ATTEMPTS}] probing {PROBE} ...", flush=True)
        unblocked = warm_cache.have_fresh(PROBE) or warm_cache.fetch_one(PROBE, "yfinance")
        if unblocked:
            print("Data feed is responding -> fetching the full universe (gently).", flush=True)
            for c in strat.US:
                if not warm_cache.have_fresh(c):
                    ok = warm_cache.fetch_one(c, "yfinance")
                    print(f"  {'ok ' if ok else 'miss'} {c}", flush=True)
                    time.sleep(GAP)
            for ls in strat.CRYPTO:
                if not warm_cache.have_fresh(ls):
                    warm_cache.fetch_one(ls, "ccxt"); time.sleep(2)
            cached = sum(1 for c in strat.US if warm_cache.have_fresh(c))
            print(f"US symbols cached: {cached}/{len(strat.US)}", flush=True)
            if cached >= 12:
                a = pl.load_acct() or pl.start(100.0)
                print("\n" + "=" * 50 + "\nRUNNING THE STRATEGY ON YOUR $100 ACCOUNT\n" + "=" * 50, flush=True)
                pl.rebalance(a)
                print("\n[wait_and_trade] TRADE_COMPLETE", flush=True)
                return
            print("Not enough symbols cached yet; will retry.", flush=True)
        else:
            print("Still blocked.", flush=True)
        if attempt < MAX_ATTEMPTS:
            print(f"Sleeping {WAIT // 60} min before next try...", flush=True)
            time.sleep(WAIT)
    print("\n[wait_and_trade] GAVE_UP — data feed still blocked after all attempts. "
          "Re-run trading-lab/wait_and_trade.py later.", flush=True)


if __name__ == "__main__":
    main()
```

#### File: `trading-lab/survivorship_500.py`
```python
"""
survivorship_500.py — Nifty 500 momentum, point-in-time (survivorship-corrected)
vs biased (current list), using FREE Wayback membership + our store prices.
Window 2019-2026 (Wayback snapshots 2018-2026, 90% price coverage).
"""
from __future__ import annotations
import os, sys, warnings
import numpy as np
import pandas as pd
import duckdb

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(__file__))
from survivorship_test import momentum_trend_weights, perf, stats  # reuse engine
DB = os.path.expanduser("~/.vibe-trading/market.duckdb")


def main():
    con = duckdb.connect(DB, read_only=True)
    hist = con.execute("SELECT snap_date, symbol FROM index_members_hist WHERE idx='nifty500'").df()
    hist["snap_date"] = pd.to_datetime(hist["snap_date"])
    snaps = {d: set(g["symbol"]) for d, g in hist.groupby("snap_date")}
    snap_dates = sorted(snaps)
    ever = sorted(set(hist["symbol"]))
    store = {r[0] for r in con.execute("SELECT DISTINCT symbol FROM prices").fetchall()}
    have = [s for s in ever if s in store]
    ph = ",".join(["?"] * len(have))
    df = con.execute(f"SELECT date,symbol,close FROM prices WHERE symbol IN ({ph}) "
                     f"AND date>='2018-01-01' ORDER BY date", have).df()
    con.close()
    px = df.pivot(index="date", columns="symbol", values="close").ffill(limit=5)
    px.index = pd.to_datetime(px.index)

    current = snaps[snap_dates[-1]]                    # biased = today's list

    def pit(t):                                        # point-in-time: nearest-prior snapshot
        prior = [d for d in snap_dates if d <= t]
        return snaps[prior[-1]] if prior else snaps[snap_dates[0]]

    def biased(t):
        return current

    r_bias = perf(px, momentum_trend_weights(px, biased))
    r_pit = perf(px, momentum_trend_weights(px, pit))
    print(f"Nifty 500 momentum (top-20), 2019-2026 — {len(have)}/{len(ever)} members priced\n")
    print(f"{'version':34}{'CAGR':>8}{'Sharpe':>8}{'MaxDD':>8}")
    print("-" * 58)
    s1, s2 = stats(r_bias), stats(r_pit)
    print(f"{'BIASED (today list)':34}{s1['cagr']:>7.1%}{s1['sharpe']:>8.2f}{s1['maxdd']:>7.0%}")
    print(f"{'CORRECTED (Wayback point-in-time)':34}{s2['cagr']:>7.1%}{s2['sharpe']:>8.2f}{s2['maxdd']:>7.0%}")
    print(f"\nSurvivorship inflation (Nifty 500, 7y): CAGR {(s1['cagr']-s2['cagr'])*100:+.1f}pp, "
          f"Sharpe {s1['sharpe']-s2['sharpe']:+.2f}")
    print("(90% price coverage; 10% missing delisted -> true bias slightly larger.)")


if __name__ == "__main__":
    main()
```

#### File: `trading-lab/momentum_full.py`
```python
"""
momentum_full.py — momentum across the FULL Indian market, from the local store.

No API calls: reads the DuckDB store (whole market, 2y). Uses DuckDB to pick a
liquid universe fast (top-N by turnover), then computes the same validated
momentum signal on ALL of them — the real universe, not 23 hand-picked names.
"""
from __future__ import annotations
import os
import numpy as np
import pandas as pd
import duckdb

DB = os.path.expanduser("~/.vibe-trading/market.duckdb")
TOPK, N_LIQUID = 15, 300


def main():
    con = duckdb.connect(DB, read_only=True)
    maxd = con.execute("SELECT MAX(date) FROM prices").fetchone()[0]
    cutoff = pd.Timestamp(maxd) - pd.Timedelta(days=90)

    # 1) liquid universe: top-N by avg daily turnover (close*volume) — fast SQL over 1M rows
    liquid = con.execute("""
        SELECT symbol, AVG(close*volume) AS turnover, COUNT(*) AS n
        FROM prices WHERE date >= ? GROUP BY symbol
        HAVING n >= 40 AND AVG(close) > 20
        ORDER BY turnover DESC LIMIT ?""", [cutoff.date(), N_LIQUID]).df()
    syms = liquid["symbol"].tolist()
    total_market = con.execute("SELECT COUNT(DISTINCT symbol) FROM prices").fetchone()[0]

    # 2) pull their close history from the store (still zero network)
    ph = ",".join(["?"] * len(syms))
    px = con.execute(f"SELECT date, symbol, close FROM prices WHERE symbol IN ({ph}) "
                     f"ORDER BY date", syms).df().pivot(index="date", columns="symbol", values="close")
    con.close()
    px.index = pd.to_datetime(px.index)

    # 3) momentum signal on each (same rules as validated strategy)
    rows = []
    for s in px.columns:
        c = px[s].dropna()
        if len(c) < 252:
            continue
        price = c.iloc[-1]
        sma200 = c.rolling(200).mean().iloc[-1]
        ret6m = c.iloc[-1] / c.iloc[-126] - 1
        carhart = c.iloc[-21] / c.iloc[-252] - 1
        vol = c.pct_change().iloc[-60:].std() * np.sqrt(252)
        eligible = (price > sma200) and (ret6m > 0)
        rows.append((s, price, eligible, ret6m, carhart, vol))
    df = pd.DataFrame(rows, columns=["sym", "price", "elig", "ret6m", "carhart", "vol"])

    print(f"Scanned {len(df)} liquid stocks (from {total_market:,} in the store), "
          f"data through {maxd}. ALL from local DuckDB — zero API calls.\n")
    top = df[df["elig"]].sort_values("carhart", ascending=False).head(TOPK)
    print(f"=== Top {TOPK} momentum stocks across the FULL market ===")
    print(f"{'stock':14}{'price(Rs)':>11}{'6m ret':>9}{'12-1 mom':>10}{'ann.vol':>9}")
    print("-" * 53)
    for _, r in top.iterrows():
        print(f"{r['sym']:14}{r['price']:>11,.0f}{r['ret6m']:>8.0%}{r['carhart']:>10.0%}{r['vol']:>9.0%}")
    print(f"\n{int(df['elig'].sum())}/{len(df)} liquid stocks currently in an uptrend "
          f"(above 200-day avg + positive 6m momentum).")


if __name__ == "__main__":
    main()
```

#### File: `trading-lab/india_intraday_vbt.py`
```python
"""
india_intraday_vbt.py — intraday on Indian stocks, tested in vectorbt with
REAL Indian costs. Settles the intraday question with the proper engine.

Hourly bars (RELIANCE, HDFCBANK, Nifty). Three intraday strategies. Three cost
levels via vectorbt's from_signals:
  1) GROSS            — no costs (the fantasy)
  2) %-only (0.05%)   — STT + exchange/GST/SEBI, IGNORING brokerage
  3) REAL small acct  — the above PLUS Rs 20 flat brokerage PER ORDER on a
                        Rs 10,000 account (fixed_fees=20) — the actual killer.
"""
from __future__ import annotations
import os, glob, warnings
import numpy as np
import pandas as pd
import vectorbt as vbt

warnings.filterwarnings("ignore")
CACHE = os.path.expanduser("~/.vibe-trading/intraday_cache")
INIT = 10000


def rsi(s, n):
    d = s.diff(); up = d.clip(lower=0).rolling(n).mean(); dn = (-d.clip(upper=0)).rolling(n).mean()
    return 100 - 100/(1 + up/dn.replace(0, np.nan))


def signals(c):
    out = {}
    out["mom_ema12"] = (c > c.ewm(span=12).mean())
    hi = c.rolling(24).max(); lo = c.rolling(24).min()
    br = pd.Series(np.nan, index=c.index); br[c >= hi] = 1; br[c <= lo] = 0
    out["breakout24"] = br.ffill().fillna(0).astype(bool)
    r = rsi(c, 6); mr = pd.Series(np.nan, index=c.index); mr[r < 25] = 1; mr[r > 60] = 0
    out["rsi_meanrev"] = mr.ffill().fillna(0).astype(bool)
    return out


def run(close, entries, exits, fees, fixed):
    pf = vbt.Portfolio.from_signals(close, entries, exits, init_cash=INIT,
                                    fees=fees, fixed_fees=fixed, freq="1H")
    return float(pf.total_return()) * 100, float(pf.sharpe_ratio()), int(pf.trades.count())


def main():
    files = sorted(glob.glob(f"{CACHE}/*_1H.csv"))
    for f in files:
        name = os.path.basename(f).replace("_1H.csv", "").replace("_NSEI", "NIFTY").replace("_NS", "")
        df = pd.read_csv(f, index_col=0, parse_dates=True)
        close = df["close"].dropna()
        # buy & hold benchmark
        bh = float((close.iloc[-1]/close.iloc[0]-1)*100)
        print(f"\n===== {name}  (hourly, {len(close)} bars; buy&hold {bh:+.0f}%) =====")
        print(f"  {'strategy':13}{'trades':>8}{'GROSS ret':>11}{'net %-only':>12}{'net +Rs20/order':>16}")
        for sname, ent in signals(close).items():
            ex = ~ent  # exit when signal off
            g_ret, g_sh, n = run(close, ent, ex, 0.0, 0.0)
            p_ret, p_sh, _ = run(close, ent, ex, 0.0005, 0.0)
            r_ret, r_sh, _ = run(close, ent, ex, 0.0005, 20.0)
            print(f"  {sname:13}{n:>8}{g_ret:>10.0f}%{p_ret:>11.0f}%{r_ret:>15.0f}%")
    print("\nRead the last column: that's what a Rs 10,000 account actually keeps")
    print("after the Rs 20/order brokerage. If it's deeply negative, intraday is a")
    print("guaranteed loss here regardless of how good the signal looks gross.")


if __name__ == "__main__":
    main()
```


==================================================
