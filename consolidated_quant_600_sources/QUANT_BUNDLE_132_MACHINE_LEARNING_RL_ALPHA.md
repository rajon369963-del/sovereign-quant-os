# ⚡ [QUANT-SOURCE-132] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_132_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ArcticDB (`PHASE4-QUANT-021`)
- **Full Name**: `PHASE4-QUANT-021_man-group__ArcticDB`
- **Description**: ArcticDB is a high performance, serverless DataFrame database built for the Python Data Science ecosystem.
- **GitHub Stars**: 2511
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<p align="center">
  <img src="static/ArcticDB Logo Purple Horizontal.svg">
</p>

---

<div align="center">
  <p><b>Three minute ArcticDB demo from PyQuantNews</b></p>
  <a href="https://www.youtube.com/watch?v=5_AjD7aVEEM">
    <img src="static/pqn_video_thumbnail.png" alt="Options data in ArcticDB" width="33%">
  </a>
</div>

---
<p align="center">
:earth_americas: <a href="http://arcticdb.io">ArcticDB Website</a> | 📘 <a href="https://docs.arcticdb.com">ArcticDB Docs</a> | 📰: <a href="https://medium.com/arcticdb">ArcticDB Blog</a> | :mega: <a href="https://www.man.com/man-group-brings-powerful-dataframe-database-product-arcticdb-to-market-with-bloomberg">Press Release</a> | :mega: <a href="https://www.bloomberg.com/company/press/man-group-brings-powerful-dataframe-database-product-arcticdb-to-market-with-bloomberg/">Press Release</a> | :busts_in_silhouette: <a href="#community">Community</a>
<br /><br />
<a href="https://github.com/man-group/ArcticDB/actions"><img src="https://github.com/man-group/ArcticDB/actions/workflows/build.yml/badge.svg"/></a>
</p>

---

**ArcticDB** is a high performance, serverless **DataFrame database** built for the Python Data Science ecosystem.
Launched in March 2023, it is the successor to [Arctic](https://github.com/man-group/arctic).

Use of ArcticDB in production (including business or commercial environments) or for a Database Service requires a paid for license from ArcticDB Limited . Please contact info@arcticdb.io for further details.

ArcticDB offers an intuitive Python-centric API enabling you to read and write Pandas DataFrames to S3 or LMDB utilising a fast C++ data-processing and compression engine.

ArcticDB allows you to:

 * **Pandas in, Pandas out**: Read and write Pandas DataFrames, NumPy arrays and native types to S3 and LMDB without leaving Python.
 * **Built for time-series data**: Efficiently index and query time-series data across _billions_ of rows
 * **Time travel**: Travel back in time to see previous versions of your data and create customizable snapshots of the database
 * **Schemaless Database**: Append, update and modify data without being constrained by the existing schema
 * **Optimised for streaming data**: Built in support for efficient sparse data storage
 * **Powerful processing**: Filter, aggregate and create new columns on-the-fly with a Pandas-like syntax
 * **C++ efficiency**: Accelerate analytics though concurrency in the C++ data-processing engine

ArcticDB handles data that is big in both row count and column count, so a 20-year history of more than 400,000 unique securities can be stored in a single *symbol*. Each *symbol* is maintained as a separate entity with no shared data which means ArcticDB can scale horizontally across *symbols*, maximising the performance potential of your compute, storage and network.

ArcticDB is designed from the outset to be resilient; there is no single point of failure, and persistent data structures in the storage mean that once a version of a *symbol* has been written, it can never be corrupted by subsequent updates. Pulling compressed data directly from  storage to the client means that there is no server to overload, so your data is always available when you need it.

## Quickstart

### Prebuilt binary availability (for the current version)

|                       | [PyPI (Python 3.9 - 3.14)](https://pypi.org/project/arcticdb/) | [conda-forge (Python 3.10 - 3.14)](https://github.com/conda-forge/arcticdb-feedstock/?tab=readme-ov-file#current-release-info) |
| --------------------- | -- | -- |
| Linux `x86_64`        | ✔️ | ✔️ |
| Linux `arm64`         | ➖ | ✔️ |
| Windows `x86_64`      | ✔️ | ✔️ |
| MacOS `x86_64`        | ➖ | ✔️ |
| MacOS `arm64`         | ✔️ | ✔️ |

### Storage compatibility

|                       | Linux | Windows | Mac |
| --------------------- | - | - | - |
| S3                 | ✔️ | ✔️ | ✔️ |
| LMDB               | ✔️ | ✔️ | ✔️ |
| Azure Blob Storage | ✔️ | ✔️ | ✔️ |

We have tested against the following S3 backends:
- AWS S3
- Ceph
- MinIO on Linux
- Pure Storage S3
- Scality S3
- VAST Data S3

### Installation

Install ArcticDB:

```bash
$ pip install arcticdb
```
or using conda-forge
```bash
$ conda install -c conda-forge arcticdb
```

Import ArcticDB:

```Python
>>> import arcticdb as adb
```

Create an instance on your S3 storage (with or without explicit credentials):

```Python
# Leave AWS to derive credential information
>>> ac = adb.Arctic('s3://MY_ENDPOINT:MY_BUCKET?aws_auth=true')

# Manually specify creds
>>> ac = adb.Arctic('s3://MY_ENDPOINT:MY_BUCKET?region=YOUR_REGION&access=ABCD&secret=DCBA')
```

Or create an instance on your local disk:

```Python
>>> ac = adb.Arctic("lmdb:///<path>")
```

Create your first library and list the libraries in the instance:

```Python
>>> ac.create_library('travel_data')
>>> ac.list_libraries()
```

Create a test dataframe:
```Python
>>> import numpy as np
>>> import pandas as pd
>>> NUM_COLUMNS=10
>>> NUM_ROWS=100_000
>>> df = pd.DataFrame(np.random.randint(0,100,size=(NUM_ROWS, NUM_COLUMNS)), columns=[f"COL_{i}" for i in range(NUM_COLUMNS)], index=pd.date_range('2000', periods=NUM_ROWS, freq='h'))
```

Get the library, write some data to it, and read it back:

```Python
>>> lib = ac['travel_data']
>>> lib.write("my_data", df)
>>> data = lib.read("my_data")
```

To find out more about working with data, visit our [docs](https://docs.arcticdb.io)

---

## Documentation

The source code for the ArcticDB docs are located in the [docs](https://github.com/man-group/ArcticDB/tree/master/docs) folder, and are hosted at [docs.arcticdb.io](https://docs.arcticdb.io).

## License

ArcticDB is released under a [Business Source License 1.1 (BSL)](https://github.com/man-group/ArcticDB/blob/master/LICENSE.txt)

BSL features are free to use and the source code is available, but users may not use ArcticDB for production use or for
a Database Service, without agreement with Man Group Operations Limited.

Use of ArcticDB in production or for a Database Service requires a paid for license from ArcticDB Limited
and is licensed under the ArcticDB Software License Agreement. For more information please contact [info@arcticdb.io](mailto:info@arcticdb.io).

The BSL is not certified as an open-source license, but most of the [Open Source Initiative (OSI)](https://opensource.org/) criteria are met.
Please see version conversion dates in the below table:

| ArcticDB Version | License | Converts to Apache 2.0 |
| ------------- | ------------- | ------------- |
| 1.0 | Business Source License 1.1 | Mar 16, 2025 |
| 1.2 | Business Source License 1.1 | May 22, 2025 |
| 1.3 | Business Source License 1.1 | Jun 9, 2025 |
| 1.4 | Business Source License 1.1 | Jun 23, 2025 |
| 1.5 | Business Source License 1.1 | Jul 11, 2025 |
| 1.6 | Business Source License 1.1 | Jul 25, 2025 |
| 2.0 | Business Source License 1.1 | Aug 29, 2025 |
| 3.0 | Business Source License 1.1 | Sep 13, 2025 |
| 4.0 | Business Source License 1.1 | Sep 27, 2025 |
| 4.1 | Business Source License 1.1 | Nov 1, 2025 |
| 4.2 | Business Source License 1.1 | Nov 12, 2025 |
| 4.3 | Business Source License 1.1 | Feb 7, 2026 |
| 4.4 | Business Source License 1.1 | Apr 5, 2026 |
| 4.5 | Business Source License 1.1 | Aug 14, 2026 |
| 5.0 | Business Source License 1.1 | Oct 31, 2026 |
| 5.1 | Business Source License 1.1 | Nov 15, 2026 |
| 5.2 | Business Source License 1.1 | Jan 27, 2027 |
| 5.3 | Business Source License 1.1 | Mar 24, 2027 |
| 5.4 | Business Source License 1.1 | Apr 28, 2027 |
| 5.5 | Business Source License 1.1 | May 13, 2027 |
| 5.6 | Business Source License 1.1 | May 26, 2027 |
| 5.7 | Business Source License 1.1 | Jun 2, 2027 |
| 5.8 | Business Source License 1.1 | Jun 9, 2027 |
| 5.9 | Business Source License 1.1 | Jul 7, 2027 |
| 5.10 | Business Source License 1.1 | Jul 29, 2027 |
| 6.1 | Business Source License 1.1 | Aug 20, 2027 |
| 6.2 | Business Source License 1.1 | Sep 8, 2027 |
| 6.3 | Business Source License 1.1 | Nov 3, 2027 |
| 6.5 | Business Source License 1.1 | Dec 11, 2027 |
| 6.6 | Business Source License 1.1 | Jan 6, 2028 |
| 6.7 | Business Source License 1.1 | Jan 12, 2028 |
| 6.8 | Business Source License 1.1 | Jan 28, 2028 |
| 6.9 | Business Source License 1.1 | Feb 2, 2028 |
| 6.10 | Business Source License 1.1 | Mar 2, 2028 |
| 6.11 | Business Source License 1.1 | Mar 23, 2028 |
| 6.12 | Business Source License 1.1 | Apr 15, 2028 |
| 6.13 | Business Source License 1.1 | Apr 21, 2028 |
| 6.14 | Business Source License 1.1 | Apr 29, 2028 |
| 6.15 | Business Source License 1.1 | May 4, 2028 |
| 6.16 | Business Source License 1.1 | May 11, 2028 |
| 6.17 | Business Source License 1.1 | May 18, 2028 |
| 6.18 | Business Source License 1.1 | Jun 1, 2028 |
| 6.19 | Business Source License 1.1 | Jul 21, 2028 |
| 6.20 | Business Source License 1.1 | Jul 27, 2028 |
| 6.21 | Business Source License 1.1 | Aug 4, 2028 |

## Code of Conduct

[Code of Conduct](https://github.com/man-group/ArcticDB/blob/master/CODE_OF_CONDUCT.md)

This project has adopted a Code of Conduct. If you have any concerns about the Code, or behaviour that you have
experienced in the project, please contact us at [info@arcticdb.io](mailto:info@arcticdb.io).

## Contributing/Building From Source

We welcome your contributions to help us improve and extend this project!

Please refer to the [Contributing](https://github.com/man-group/ArcticDB/blob/master/docs/mkdocs/docs/technical/contributing.md)
page and feel free to open issues on GitHub.

We are also always looking for feedback from our dedicated community! If you have used ArcticDB please let us know, we would love to hear about your experience!

Our release process is [documented here](https://github.com/man-group/ArcticDB/wiki/Releasing).

## Community

We would love to hear how your ArcticDB journey evolves, email us at [info@arcticdb.io](mailto:info@arcticdb.io) or come chat to us on [Twitter](https://www.twitter.com/arcticdb)!

Interested in learning more about ArcticDB? Head over to our [blog](https://medium.com/arcticdb)!

Do you have any questions or issues? Chat to us and other users through our dedicated Slack Workspace - sign up for Slack access on [our website](https://arcticdb.io).

### Community projects

The following independently maintained community projects extend the ArcticDB ecosystem:

- [arcticdb-mcp](https://github.com/YMuskrat/arcticdb_mcp): A community-maintained Model Context Protocol server that enables compatible AI assistants and agents to interact with ArcticDB libraries, symbols, versions, snapshots, batch operations and queries.

### Core Implementation Code & Architecture
#### File: `python/tests/__init__.py`
```python

```

#### File: `python/tests/unit/__init__.py`
```python

```

#### File: `python/tests/unit/arcticdb/__init__.py`
```python

```

#### File: `python/tests/unit/arcticdb/version_store/__init__.py`
```python

```

#### File: `python/tests/sanitizers/__init__.py`
```python

```

#### File: `python/tests/sanitizers/arcticdb/__init__.py`
```python

```


==================================================


## [2/3] Repository: gym-trading (`PHASE4-QUANT-053`)
- **Full Name**: `PHASE4-QUANT-053_drewstone__gym-trading`
- **Description**: Reinforcement learning environment for trading
- **GitHub Stars**: 15
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# gym-trading

### Core Implementation Code & Architecture
#### File: `ob/__init__.py`
```python

```

#### File: `tests/__init__.py`
```python

```

#### File: `agents/__init__.py`
```python

```

#### File: `envs/__init__.py`
```python

```

#### File: `tests/test_simulator.py`
```python
from envs.simulator import Simulator


class MockAgent():

    def __init__(self):
        self.initialized = False

    def initialize(self):
        self.initialized = True

    def grid(self, data):
        print("Agent: {}".format(data))
        return data


def test_simulator():
    options = {
        "exchange": "GEMINI",
        "symbol": "ETHUSD",
        "data_dir": "./data/gemini",
        "data_format": "raw",
        "input_orders": 30,
        "dates": [20171201],
        "delta": 0,
        "grid_step_length": 100  # in milliseconds
    }

    Simulator(options)
```

#### File: `envs/main.py`
```python
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime
from envs import simulator

if __name__ == '__main__':
    options = {
        "exchange": "GEMINI",
        "symbol": "ETHUSD",
        "data_dir": "./data/gemini",
        "data_format": "raw",
        "input_orders": 30,
        "dates": [20171201, 20171202],
        "delta": 0,
        "grid_step_length": 100  # in milliseconds
    }
    sim = simulator.Simulator(options)
    while not sim.is_finished():
        ob = sim.next()
    print(sim.orderbook.last_datetime, sim.orderbook.state())
```


==================================================


## [3/3] Repository: outsmart-cli (`PHASE4-QUANT-057`)
- **Full Name**: `PHASE4-QUANT-057_outsmartchad__outsmart-cli`
- **Description**: Agent-first CLI for trading on Solana — 18 DEX adapters, 12 SWQoS TX landing processors. Buy, sell, lp, snipe, create pool, launch coin, and stream real-time onchain events from your terminal.
- **GitHub Stars**: 582
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# outsmart

**The most complete Solana DEX CLI and toolkit for builders, traders, and AI agents**

**[Documentation](https://outsmartchad.github.io/outsmart-cli/)** | **[npm](https://www.npmjs.com/package/outsmart)** | **[Discord](https://discord.gg/dc3Kh3Y3yJ)**

## Table of Contents

- [About](#about)
- [Quick Start](#quick-start)
- [Commands](#commands)
  - [Trading](#trading)
  - [Liquidity](#liquidity)
  - [Event Streaming](#event-streaming)
  - [Wallet Management](#wallet-management)
  - [Balances](#balances)
  - [Utilities](#utilities)
  - [Perpetual Futures (Percolator)](#perpetual-futures-percolator)
- [Shared Swap Options](#shared-swap-options)
- [Stablecoin Auto-Swap](#stablecoin-auto-swap)
- [DEX Adapters](#dex-adapters)
- [Programmatic API](#programmatic-api)
- [Event Streaming (Programmatic)](#event-streaming-1)
- [LP Manager](#lp-manager)
- [TX Landing Providers](#tx-landing-providers)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## About

outsmart unifies every major Solana DEX protocol into a single CLI and Node.js library. 18 on-chain adapters (Raydium, Meteora, Orca, PumpFun, PumpSwap, and more), 2 swap aggregators (Jupiter Ultra, DFlow), 12 concurrent TX landing providers, real-time event streaming via Yellowstone gRPC or WebSocket, and an LP manager with auto-rebalancing and fee compounding — all from one package.

**For builders** — `import { getDexAdapter, LpManager, EventStream } from "outsmart"` and ship your own strategies. Typed event streams, per-DEX vault parsing, and a unified adapter interface mean you write the logic — outsmart handles the protocol plumbing across 18 DEXes.

**For AI agents** — use the CLI to interact with any major Solana DeFi protocol autonomously. Swap, manage LP positions, stream real-time events, and execute complex strategies — all from a single command.

---

## Quick Start

### 1. Install

```bash
# From npm (recommended)
npm install -g outsmart@alpha

# Or from source
git clone https://github.com/outsmartchad/outsmart-cli.git
cd outsmart-cli
npm install --legacy-peer-deps
npm run build
```

### 2. Configure

```bash
outsmart init
```

Prompts for your wallet key and RPC endpoint. Writes config to `~/.outsmart/config.env`. You only need to do this once.

### 3. Trade

```bash
# Buy 0.1 SOL worth of a token (token auto-detected from pool)
outsmart buy --dex raydium-cpmm --pool <POOL> --amount 0.1

# Sell 100% of held balance
outsmart sell --dex raydium-cpmm --pool <POOL> --pct 100

# Swap aggregator (no pool needed, just token mint)
outsmart buy --dex jupiter-ultra --token <MINT> --amount 0.1

# Check your balances
outsmart balance
```

**Example output:**

```
  buying on raydium-cpmm...
  TX sent: 5zwjta... — confirming...

  dex:       raydium-cpmm
  tx:        5zwjtaMj8LCzf4cY7Kt2QU2CAcAn3BAwvpVCbTjsR3qJ...
  confirmed: true
  in:        0.001 SOL
  out:       2.001886 USELESS
  pool:      Q2sPHPdUWFMg7M7wwrQKLrn619cAucfRsmhVJffodSp
```

---

## Commands

### Trading

#### buy

Buy tokens with SOL (or a quote token).

```bash
outsmart buy --dex <name> --pool <POOL> --amount <SOL>
outsmart buy --dex raydium-cpmm --pool <POOL> --amount 0.1
outsmart buy --dex jupiter-ultra --token <MINT> --amount 0.5
```

| Flag | Description |
|------|-------------|
| `-d, --dex <name>` | DEX adapter name (required) |
| `-a, --amount <sol>` | SOL amount to spend (required) |
| `-p, --pool <address>` | Pool address (required for on-chain DEXes) |
| `-t, --token <mint>` | Token mint (auto-detected from pool; required for aggregators) |

#### sell

Sell tokens for SOL. Specify what percentage of your balance to sell.

```bash
outsmart sell --dex <name> --pool <POOL> --pct <1-100>
outsmart sell --dex raydium-cpmm --pool <POOL> --pct 100
outsmart sell --dex jupiter-ultra --token <MINT> --pct 50
```

| Flag | Description |
|------|-------------|
| `-d, --dex <name>` | DEX adapter name (required) |
| `--pct <percentage>` | Percentage of balance to sell, 1-100 (required) |
| `-p, --pool <address>` | Pool address (required for on-chain DEXes) |
| `-t, --token <mint>` | Token mint (auto-detected from pool; required for aggregators) |

#### quote

Get the current on-chain price from a pool.

```bash
outsmart quote --dex raydium-cpmm --pool <POOL>
```

#### find-pool

Discover a pool for a token pair on a specific DEX.

```bash
outsmart find-pool --dex raydium-cpmm --token <MINT>
```

### Liquidity

#### add-liq

Add liquidity to a pool.

```bash
outsmart add-liq --dex meteora-damm-v2 --pool <POOL> --amount-sol 1.0
outsmart add-liq --dex meteora-dlmm --pool <POOL> --amount-sol 0.5 --amount-token 1000
```

| Flag | Description |
|------|-------------|
| `-d, --dex <name>` | DEX adapter name (required) |
| `-p, --pool <address>` | Pool address (required) |
| `--amount-sol <amount>` | Amount of SOL to deposit |
| `--amount-token <amount>` | Amount of non-SOL token to deposit |
| `--strategy <type>` | Distribution: `spot` \| `curve` \| `bid-ask` (DLMM only, default: spot) |
| `--bins <count>` | Number of bins (DLMM only, default: 50, max: 70) |

#### remove-liq

Remove liquidity from a pool.

```bash
outsmart remove-liq --dex meteora-damm-v2 --pool <POOL> --pct 100
```

#### claim-fees

Claim accumulated swap fees from LP positions.

```bash
outsmart claim-fees --dex meteora-damm-v2 --pool <POOL>
```

#### positions

List LP positions in a pool.

```bash
outsmart positions --dex meteora-damm-v2 --pool <POOL>
```

#### lp-manage

Start LP position management. See [LP Manager](#lp-manager) for full details and programmatic API.

```bash
# Start managing a DLMM position (auto-rebalance + compound)
outsmart lp-manage --dex meteora-dlmm --pool <POOL> --dry-run

# Manage a specific position
outsmart lp-manage --dex meteora-dlmm --pool <POOL> --position <POSITION>

# DAMM v2 — compound-only (full-range, no rebalancing needed)
outsmart lp-manage --dex meteora-damm-v2 --pool <POOL>

# Custom thresholds
outsmart lp-manage --dex meteora-dlmm --pool <POOL> \
  --bins 30 --strategy curve --compound-interval 15 \
  --il-threshold 5 --stop-loss 20
```

| Flag | Description | Default |
|------|-------------|---------|
| `--dex <name>` | `meteora-dlmm` or `meteora-damm-v2` (required) | |
| `--pool <address>` | Pool address (required) | |
| `--position <address>` | Specific position (default: all in pool) | |
| `--bins <count>` | Bins for new position after rebalance (DLMM) | 50 |
| `--strategy <type>` | `spot` \| `curve` \| `bid-ask` (DLMM) | `spot` |
| `--compound-interval <min>` | Compound fees every N minutes (0=off) | 30 |
| `--il-threshold <pct>` | Exit if IL exceeds N% | 10 |
| `--stop-loss <pct>` | Exit if price drops N% from entry (0=off) | 0 |
| `--dry-run` | Log actions without executing | false |
| `--ws` | Use WebSocket streaming (free) | auto |

#### lp-find

Find the best LP pool for a token.

```bash
outsmart lp-find --token <MINT>
outsmart lp-find --token <MINT> --dex meteora-dlmm --json
```

#### create-pump-coin

Create a new PumpFun token with a bonding curve.

```bash
outsmart create-pump-coin --name "My Token" --symbol "MYTKN" --uri "https://ipfs.io/ipfs/Qm..."
```

#### create-pool

Create a new PumpSwap AMM pool with initial liquidity.

```bash
outsmart create-pool --base <MINT> --quote So111...112 --base-amount 1000000 --quote-amount 1
```

#### create-damm-pool

Create a Meteora DAMM v2 custom pool with full fee configuration.

```bash
outsmart create-damm-pool --base <MINT> --base-amount 1000000 --quote-amount 0.5
outsmart create-damm-pool --base <MINT> --base-amount 1000000 --quote-amount 0.5 \
  --max-fee 5000 --min-fee 100 --fee-mode 1 --dynamic-fee
```

#### create-damm-config-pool

Create a Meteora DAMM v2 pool using an existing on-chain config.

```bash
outsmart create-damm-config-pool --base <MINT> --base-amount 1000000 --quote-amount 0.5 \
  --config <CONFIG_ADDRESS>
```

### Event Streaming

See [Event Streaming](#event-streaming) for full details, programmatic API, and supported DEXes.

```bash
# Stream all DEX swaps (auto-selects WebSocket if no gRPC endpoint configured)
outsmart stream --preset all-dex-swaps

# Force WebSocket mode (free, no gRPC endpoint needed)
outsmart stream --preset all-dex-swaps --ws

# Stream specific DEXes
outsmart stream --preset pumpswap
outsmart stream --preset raydium
outsmart stream --preset meteora

# Stream new pool creations
outsmart stream --preset new-pools

# Stream PumpFun bonding curve events
outsmart stream --preset pumpfun-bonding
```

Available presets: `all-dex-swaps`, `new-pools`, `pumpfun-bonding`, `pumpswap`, `raydium`, `meteora`, `other-dexes`, `wallet-trades`

**gRPC mode** (default if configured): requires `GRPC_URL` and `GRPC_XTOKEN` env vars. Lowest latency (~200ms).

**WebSocket mode** (`--ws` flag or auto-selected): uses your standard `MAINNET_ENDPOINT` RPC. Free, higher latency (~1-3s).

### Wallet Management

#### wallet

Show the active wallet address and SOL balance.

```bash
outsmart wallet
```

```
  label:   default
  address: tstXr3NbiMd6FFZF2qbPzxJqxCGXuSjpZVvdjeXiPv1
  balance: 0.377743 SOL
```

#### wallet list

Show all saved wallets with their balances. Active wallet marked with `*`.

```bash
outsmart wallet list
```

```
  LABEL              ADDRESS                                         SOL
  ──────────────────────────────────────────────────────────────────────────
 * default            tstXr3NbiMd6FFZF2qbPzxJqxCGXuSjpZVvdjeXiPv1  0.3777
   trading            7xKXt...                                       1.2340

  * = active wallet
```

#### wallet add

Add a new wallet. Prompts for the private key.

```bash
outsmart wallet add --label trading
```

#### wallet switch

Switch the active wallet. All subsequent commands use the new wallet.

```bash
outsmart wallet switch trading
```

#### wallet remove

Remove a saved wallet (with confirmation prompt).

```bash
outsmart wallet remove trading
```

### Balances

#### balance

Show SOL + stablecoin balances for the active wallet.

```bash
outsmart balance
```

```
  Wallet: tstXr3NbiMd6FFZF2qbPzxJqxCGXuSjpZVvdjeXiPv1

  SOL        0.377743
  USDC       0.000001
  USDT       0
  USD1       0
```

#### balance --token

Check the balance of a specific token.

```bash
outsmart balance --token <MINT>
```

### Utilities

#### list-dex

List all registered DEX adapters and their capabilities.

```bash
outsmart list-dex
outsmart list-dex --cap canSell
```

#### config

View or generate configuration.

```bash
outsmart config show        # Show current env config (sensitive values masked)
outsmart config env         # Print a .env template
```

#### init

Interactive setup — prompts for wallet key and RPC endpoint.

```bash
outsmart init
```

### Perpetual Futures (Percolator)

> Warning: Work in progress — currently devnet only. See [PERCOLATOR.md](./PERCOLATOR.md) for full CLI reference and programmatic API.

```bash
outsmart perp create-market --price 150 --lp 2
outsmart perp long -m <MARKET> -s 0.1
outsmart perp keeper --pool <POOL> --market <MARKET> --dex raydium-cpmm
```

---

## Shared Swap Options

All swap commands (`buy`, `sell`) accept these options:

| Option | Description | Default |
|--------|-------------|---------|
| `--slippage <bps>` | Slippage tolerance in basis points | 300 (3%) |
| `--priority <microLamports>` | Priority fee per compute unit | from env |
| `--tip <sol>` | MEV tip in SOL | 0.001 |
| `--cu <units>` | Compute unit limit | auto |
| `--jito` | Use Jito bundle submission | false |
| `--quote <mint>` | Quote token mint | WSOL |

---

## Stablecoin Auto-Swap

Some pools use stablecoins (USDC, USDT, USD1) as the quote token instead of SOL. The CLI handles this automatically — no extra steps needed.

**On buy:** detects the stablecoin quote from the pool, swaps SOL → stablecoin, then buys the token.

**On sell:** sells the token for stablecoin, then swaps the proceeds back to SOL.

```bash
# LaunchLab pool quoted in USD1 — just specify SOL amount as usual
outsmart buy --dex raydium-launchlab --pool <POOL> --amount 0.1
# → auto-swaps 0.1 SOL → USD1 → buys token

outsmart sell --dex raydium-launchlab --pool <POOL> --pct 100
# → sells token → USD1 → auto-swaps USD1 → SOL
```

Uses Jupiter Ultra if `JUPITER_API_KEY` is set, otherwise falls back to on-chain DEX pools. Get a free key at [portal.jup.ag](https://portal.jup.ag) (optional).

---

## DEX Adapters

18 adapters covering every major Solana DEX protocol:

| Adapter | Protocol | Buy | Sell | Price | LP | Extra | Tested |
|---------|----------|:---:|:----:|:-----:|:--:|-------|:------:|
| raydium-amm-v4 | AMM v4 | ✅ | ✅ | ✅ | | findpool | ✅ |
| raydium-cpmm | CPMM | ✅ | ✅ | ✅ | | findpool | ✅ |
| raydium-clmm | CLMM | ✅ | ✅ | ✅ | | findpool | ✅ |
| raydium-launchlab | Launchlab | ✅ | ✅ | ✅ | | findpool, auto-swap | ✅ |
| meteora-damm-v1 | Dynamic AMM | ✅ | ✅ | ✅ | | findpool | — |
| meteora-damm-v2 | CpAmm | ✅ | ✅ | ✅ | full | findpool, create pool | ✅ |
| meteora-dlmm | DLMM | ✅ | ✅ | ✅ | full | | ✅ |
| meteora-dbc | DBC | ✅ | ✅ | ✅ | | | ✅ |
| pumpfun | Bonding Curve | ✅ | ✅ | ✅ | | create coin | ✅ |
| pumpfun-amm | PumpSwap AMM | ✅ | ✅ | ✅ | | create pool | ✅ |
| orca | Whirlpool | ✅ | ✅ | ✅ | | | ✅ |
| byreal-clmm | CLMM | ✅ | ✅ | ✅ | | auto-swap | ✅ |
| pancakeswap-clmm | CLMM | ✅ | ✅ | ✅ | | | ✅ |
| fusion-amm | Fusion | ✅ | ✅ | ✅ | | | ✅ |
| futarchy-amm | Futarchy | ✅ | ✅ | ✅ | | auto-swap | ✅ |
| futarchy-launchpad | Launchpad | | | | | fund/claim | — |
| jupiter-ultra | Ultra API | ✅ | ✅ | | | aggregator | ✅ |
| dflow | Intent API | ✅ | ✅ | | | aggregator | ✅ |

All ✅ adapters confirmed on Solana mainnet with real transactions.

---

## Programmatic API

Use outsmart as a library in your own bots:

```typescript
import { getDexAdapter, listDexAdapters } from "outsmart";

// Import only the adapters you need
import "outsmart/dist/dex/raydium-cpmm";
import "outsmart/dist/dex/jupiter-ultra";

const cpmm = getDexAdapter("raydium-cpmm");

// Buy
const result = await cpmm.buy({
  tokenMint: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
  amountSol: 0.1,
  opts: { slippageBps: 300, tipSol: 0.001 },
});
console.log("TX:", result.txSignature);
console.log("Received:", result.amountOut);

// Sell
const sellResult = await cpmm.sell({
  tokenMint: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
  percentage: 100,
  opts: { slippageBps: 300 },
});

// Get price
const price = await cpmm.getPrice!("POOL_ADDRESS");
console.log("Price:", price.price);

// List adapters
const adapters = listDexAdapters();
```

For AI agent integration (MCP server, OpenClaw workflows), see [outsmart-agent](https://github.com/outsmartchad/outsmart-agent).

---

## Event Streaming

Real-time DEX event streaming with two backends — **gRPC** (Yellowstone/Geyser, lowest latency) and **WebSocket** (free, uses standard RPC). Both produce the same typed events from 18+ DEX programs.

### Programmatic API

```typescript
// gRPC mode (fastest, requires Yellowstone endpoint)
import { EventStream } from "outsmart";

const stream = new EventStream({
  grpcUrl: process.env.GRPC_URL,
  grpcXToken: process.env.GRPC_XTOKEN,
});

// WebSocket mode (free, uses standard RPC)
import { WsEventStream } from "outsmart";

const stream = new WsEventStream({
  rpcUrl: process.env.MAINNET_ENDPOINT, // any Solana RPC
});

// Both emit the same events with the same API:
stream.on("Swap", (event) => {
  console.log(`${event.dex} ${event.direction} ${event.mint}`);
  console.log(`  in: ${event.amountIn}, out: ${event.amountOut}`);
  console.log(`  pool: ${event.pool}, trader: ${event.trader}`);
});

stream.on("NewPool", (event) => {
  console.log(`New pool on ${event.dex}: ${event.pool}`);
  console.log(`  ${event.tokenA} / ${event.tokenB}`);
});

stream.on("BondingComplete", (event) => {
  console.log(`Bonding complete: ${event.mint} → ${event.migrationPool}`);
});

// Large swap alerts (configurable threshold, default 10 SOL)
stream.on("LargeSwap", (event) => {
  console.log(`Whale alert: ${event.swap.amountIn} on ${event.swap.dex}`);
});

// Catch-all listener
stream.on("*", (event) => { /* any event */ });

await stream.start("all-dex-swaps");

// Custom subscriptions (gRPC only)
import { subscribePoolActivity } from "outsmart";
await stream.startCustom(subscribePoolActivity(["POOL_ADDRESS"]));

// Stop
await stream.stop();
```

### Event Types

| Event | Fields |
|-------|--------|
| `Swap` | `dex`, `pool`, `trader`, `direction`, `mint`, `amountIn`, `amountOut`, `priceAfter`, `reserveBase`, `reserveQuote`, `isAggregated` |
| `NewPool` | `dex`, `pool`, `tokenA`, `tokenB`, `initialReserveA`, `initialReserveB`, `creator` |
| `BondingComplete` | `mint`, `bondingCurve`, `migrationPool` |
| `LargeSwap` | `swap` (full SwapEvent), `estimatedUsdValue` |

### Supported DEXes

All swap events use per-DEX vault account layouts with pre/post token balance diffing for accurate amounts:

- **PumpSwap** — buy/sell/create pool (sequential discriminator pairing)
- **PumpFun** — buy/sell/create/bonding complete (BuyExactSolIn, CreateV2 discriminators)
- **Raydium** — CLMM, CPMM, AMM V4, LaunchLab
- **Meteora** — DAMM V2, DLMM, DBC, DAMM V1
- **Orca** — Whirlpool swap v1 & v2
- **PancakeSwap** — CLMM
- **Byreal** — CLMM
- **Fusion AMM**
- **Futarchy AMM**

---

## LP Manager

Automated liquidity position management for **Meteora DLMM** (concentrated, bin-based) and **DAMM v2** (full-range). Monitors positions, auto-rebalances when out of range, compounds fees, and exits on risk thresholds.

### Programmatic API

```typescript
import { LpManager, selectBestPool } from "outsmart";
import "outsmart/dist/dex/meteora-dlmm";

// Find best pool for a token
const pools = await selectBestPool("DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263");
console.log("Top pool:", pools[0].pair, "APR:", pools[0].estimatedApr + "%");

// Start management
const manager = new LpManager({
  poolAddress: "POOL_ADDRESS",
  dex: "meteora-dlmm",
  rebalanceBins: 50,
  compoundIntervalMin: 30,
  ilThresholdPct: 10,
  dryRun: false,
});

manager.on("event", (event) => {
  console.log(`[${event.type}] ${event.message}`);
});

await manager.start();

// Check stats
const stats = manager.getStats();
console.log("Rebalances:", stats.totalRebalances, "Compounds:", stats.totalCompounds);

// Stop
await manager.stop();
```

### How It Works

**DLMM strategy** — Monitors bin positions for out-of-range. When price exits the active bins, removes liquidity, claims fees, and opens a new position centered on current price. Cooldown prevents thrashing.

**DAMM v2 strategy** — Full-range positions never go out of range, so no rebalancing needed. Periodically claims accumulated fees and re-deposits them to compound returns.

**Risk management** — Estimates impermanent loss from entry price; exits position if IL exceeds threshold. Optional stop-loss exits on price drops.

**Pool selector** — Scores Meteora pools by volume/TVL ratio, estimated fee APR, TVL sweet spot ($10k-$1M), and pool age. Returns ranked results.

---

## TX Landing Providers

12 providers with concurrent, race, random, and sequential submission strategies:

| Provider | Env Var |
|----------|---------|
| Jito | `JITO_API_KEY` |
| bloXroute | `BLOXROUTE_AUTH_HEADER` |
| Helius Sender | `HELIUS_API_KEY` |
| Nozomi | `NOZOMI_API_KEY` |
| Blockrazor | `BLOCKRAZOR_API_KEY` |
| NextBlock | `NEXTBLOCK_API_KEY` |
| 0slot | `ZERO_SLOT_API_KEY` |
| Soyas | `SOYAS_API_KEY` |
| Astralane | `ASTRALANE_API_KEY` |
| Stellium | `STELLIUM_API_KEY` |
| Flashblock | `FLASHBLOCK_API_KEY` |
| Node1 | `NODE1_API_KEY` |

Set any provider's API key and it's automatically enabled. The orchestrator sends your transaction through all enabled providers simultaneously for the fastest possible landing.

---

## Environment Variables

### Required

| Variable | Description |
|----------|-------------|
| `PRIVATE_KEY` | Base58-encoded wallet private key |
| `MAINNET_ENDPOINT` | Solana mainnet RPC endpoint |

### Optional

| Variable | Description | Default |
|----------|-------------|---------|
| `TX_LANDING_MODE` | `concurrent` \| `race` \| `random` \| `sequential` | `concurrent` |
| `DEFAULT_TIP_SOL` | MEV tip in SOL | `0.001` |
| `DEFAULT_SLIPPAGE_BPS` | Slippage in basis points | `300` |
| `DEFAULT_PRIORITY_FEE` | Priority fee in microLamports per CU | `4000` |
| `DEVNET_ENDPOINT` | Solana devnet RPC endpoint (for [Percolator](./PERCOLATOR.md)) | not set |
| `JUPITER_API_KEY` | Jupiter Ultra API key ([portal.jup.ag](https://portal.jup.ag)) | works without key |
| `DFLOW_API_KEY` | DFlow intent API key ([pond.dflow.net](https://pond.dflow.net/build/api-key)) | required for dflow |
| `GRPC_URL` | Yellowstone gRPC endpoint (for gRPC keeper) | not set |
| `GRPC_XTOKEN` | Yellowstone gRPC auth token | not set |

---

## Testing

```bash
npm run test:unit        # 43 CI-safe unit tests (no RPC/SOL needed)
npm run test:registry    # Registry smoke test
npm run test:raydium     # Raydium adapters (mainnet)
npm run test:meteora     # Meteora adapters (mainnet)
npm run test:pumpfun     # PumpFun + PumpSwap (mainnet)
npm run test:orca        # Orca Whirlpool (mainnet)
npm run test:clmm        # Byreal + PancakeSwap CLMM (mainnet)
npm run test:fusion      # Fusion + Futarchy AMM (mainnet)
npm run test:api         # Jupiter Ultra + DFlow (mainnet)
npm run test:percolator  # Percolator perps (devnet) — see PERCOLATOR.md
```

Mainnet tests require `PRIVATE_KEY` and `MAINNET_ENDPOINT` env vars. Tests use tiny amounts (0.002 SOL per buy). Run suites one at a time — tests share a wallet and cannot run in parallel.

---

## Project Structure

```
src/
├── cli.ts                 # CLI entry point (Commander.js)
├── index.ts               # Library entry point
├── dex/
│   ├── types.ts           # IDexAdapter interface
│   ├── index.ts           # DexRegistry singleton
│   ├── shared/clmm-base.ts
│   ├── percolator/
│   │   ├── adapter.ts     # PercolatorAdapter (20 methods)
│   │   ├── ws-keeper.ts   # WebSocket oracle keeper (8 DEX types)
│   │   ├── grpc-keeper.ts # gRPC oracle keeper (Yellowstone/Geyser)
│   │   └── core/          # Vendored @percolator/core SDK
│   └── 18 adapter files
├── lp-manager/
│   ├── index.ts           # LpManager orchestrator (action loop, event emission)
│   ├── types.ts           # Config, strategy, position state types
│   ├── monitor.ts         # Position monitoring (poll + stream hybrid)
│   ├── risk.ts            # IL threshold, stop-loss exit
│   ├── pool-selector.ts   # Pool scoring by volume/TVL/APR
│   └── strategies/
│       ├── dlmm-strategy.ts  # DLMM rebalance + compound
│       └── damm-strategy.ts  # DAMM v2 compound
├── streaming/
│   ├── event-stream.ts    # EventStream class (auto-reconnect, ping keepalive)
│   ├── ws-event-stream.ts # WsEventStream class (free WebSocket alternative)
│   ├── tx-formatter.ts    # Raw gRPC protobuf → FormattedTransaction
│   ├── tx-parser.ts       # Per-DEX swap/pool/bonding parsers
│   ├── programs.ts        # 18 DEX program IDs
│   ├── subscriptions.ts   # 11 subscription preset builders
│   ├── discriminators.ts  # Instruction discriminator constants
│   └── types.ts           # Typed event interfaces
├── helpers/
│   ├── config.ts          # Wallet, connection, env loading
│   ├── wallets.ts         # Multi-wallet management
│   └── logger.ts          # Structured logger
└── transactions/
    ├── send-rpc.ts        # sendAndConfirmVtx (standard swaps)
    └── landing/
        ├── orchestrator.ts    # Multi-provider concurrent submission
        ├── nonce-manager.ts   # Durable nonce for dedup
        ├── tip-accounts.ts    # Tip account registry
        └── providers/         # 12 provider implementations
```

## Discord

https://discord.gg/dc3Kh3Y3yJ

## Contributing

Contributions welcome. Fork, branch, PR.

## Disclaimer

This software is provided "as is", without warranty of any kind. Use at your own risk. The authors take no responsibility for any financial loss. Users are responsible for ensuring compliance with applicable laws.

Never share your private keys. Wallet keys are stored in `~/.outsmart/` with owner-only permissions.

## License

ISC

### Core Implementation Code & Architecture
#### File: `tsconfig.build.json`
```python
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./dist",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "rootDir": "./src"
  },
  "include": ["src/**/*.ts"],
  "exclude": ["src/**/*.test.ts", "src/**/*.spec.ts", "node_modules"]
}
```

#### File: `package.json`
```python
{
  "name": "outsmart",
  "version": "2.0.0-alpha.16",
  "description": "The most complete Solana DEX toolkit for autonomous agents, bots, and builders — 18 adapters, event streaming, LP manager, perp engine.",
  "engines": {
    "node": ">=20.0.0"
  },
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "bin": {
    "outsmart": "./dist/cli.js"
  },
  "files": [
    "dist/",
    "bin/",
    "README.md",
    "LICENSE"
  ],
  "scripts": {
    "build": "npm run clean && npm run build:ts && npm run build:chmod",
    "build:ts": "tsc -p tsconfig.build.json",
    "build:chmod": "chmod +x dist/cli.js || true",
    "clean": "rm -rf dist/",
    "dev": "ts-node src/cli.ts",
    "prepublishOnly": "npm run build",
    "typecheck": "tsc --noEmit",
    "test": "jest",
    "test:registry": "jest --testPathPattern=registry",
    "test:raydium": "jest --testPathPattern=raydium",
    "test:meteora": "jest --testPathPattern=meteora",
    "test:pumpfun": "jest --testPathPattern=pumpfun",
    "test:orca": "jest --testPathPattern=orca",
    "test:clmm": "jest --testPathPattern=clmm",
    "test:fusion": "jest --testPathPattern=fusion-futarchy",
    "test:api": "jest --testPathPattern=api-adapters",
    "test:unit": "jest --testPathPattern=unit",
    "test:percolator": "jest --testPathPattern=percolator",
    "keeper": "npx tsx scripts/keeper.ts",
    "keeper:ws": "npx tsx scripts/ws-keeper.ts",
    "keeper:grpc": "npx tsx scripts/grpc-keeper.ts"
  },
  "keywords": [
    "solana",
    "trading",
    "cli",
    "dex",
    "raydium",
    "meteora",
    "orca",
    "jupiter",
    "pancakeswap",
    "sniper",
    "swap",
    "outsmart"
  ],
  "author": "vincentso",
  "url": "https://github.com/outsmartchad/solana-trading-cli/issues",
  "homepage": "https://github.com/outsmartchad/solana-trading-cli",
  "license": "ISC",
  "dependencies": {
    "@coral-xyz/anchor": "^0.29.0",
    "@crypticdot/fusionamm-client": "^1.0.81",
    "@crypticdot/fusionamm-core": "^1.0.81",
    "@metaplex-foundation/mpl-token-metadata": "^3.2.1",
    "@metaplex-foundation/umi": "^0.9.1",
    "@metaplex-foundation/umi-bundle-defaults": "^0.9.1",
    "@meteora-ag/cp-amm-sdk": "^1.3.4",
    "@meteora-ag/dlmm": "^1.0.54",
    "@meteora-ag/dynamic-amm-sdk": "^1.4.1",
    "@meteora-ag/dynamic-bonding-curve-sdk": "^1.5.3",
    "@orca-so/whirlpools": "^7.0.1",
    "@raydium-io/raydium-sdk": "^1.3.1-beta.47",
    "@raydium-io/raydium-sdk-v2": "^0.1.23-alpha",
    "@shyft-to/solana-transaction-parser": "^1.1.17",
    "@solana-program/memo": "^0.11.0",
    "@solana-program/token": "^0.11.0",
    "@solana-program/token-2022": "^0.9.0",
    "@solana/kit": "^6.1.0",
    "@solana/spl-token": "^0.4.0",
    "@solana/web3.js": "^1.95.0",
    "@triton-one/yellowstone-grpc": "^0.4.0",
    "async-mutex": "^0.5.0",
    "axios": "^1.7.9",
    "bigint-buffer": "^1.1.5",
    "bn.js": "^5.2.1",
    "bs58": "^5.0.0",
    "commander": "^12.1.0",
    "decimal.js": "^10.4.3",
    "dotenv": "^16.4.5",
    "jito-ts": "^4.2.1",
    "pino": "^8.18.0",
    "pino-pretty": "^10.3.1",
    "pumpdotfun-sdk": "^1.3.2",
    "rpc-websockets": "7.10.0"
  },
  "overrides": {
    "@solana/web3.js": "^1.95.0",
    "axios": "^1.7.9",
    "bigint-buffer": "^1.1.5",
    "qs": "^6.13.0",
    "brace-expansion": "^2.0.1"
  },
  "resolutions": {
    "@solana/web3.js": "^1.95.0",
    "axios": "^1.7.9",
    "bigint-buffer": "^1.1.5",
    "qs": "^6.13.0",
    "brace-expansion": "^2.0.1"
  },
  "devDependencies": {
    "@types/bn.js": "^5.2.0",
    "@types/jest": "^30.0.0",
    "@types/node": "^20.0.0",
    "jest": "^29.7.0",
    "ts-jest": "^29.4.6",
    "ts-node": "^10.9.2",
    "typescript": "^5.5.4"
  }
}
```

#### File: `tsconfig.json`
```python
{
  "include": ["./src/**/*.ts"],
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig to read more about this file */

    /* Projects */
    // "incremental": true,                              /* Save .tsbuildinfo files to allow for incremental compilation of projects. */
    // "composite": true,                                /* Enable constraints that allow a TypeScript project to be used with project references. */
    // "tsBuildInfoFile": "./.tsbuildinfo",              /* Specify the path to .tsbuildinfo incremental compilation file. */
    // "disableSourceOfProjectReferenceRedirect": true,  /* Disable preferring source files instead of declaration files when referencing composite projects. */
    // "disableSolutionSearching": true,                 /* Opt a project out of multi-project reference checking when editing. */
    // "disableReferencedProjectLoad": true,             /* Reduce the number of projects loaded automatically by TypeScript. */

    /* Language and Environment */
    "target": "es2022",                                  /* Set the JavaScript language version for emitted JavaScript and include compatible library declarations. */
    // "lib": [],                                        /* Specify a set of bundled library declaration files that describe the target runtime environment. */
    // "jsx": "preserve",                                /* Specify what JSX code is generated. */
    // "experimentalDecorators": true,                   /* Enable experimental support for legacy experimental decorators. */
    // "emitDecoratorMetadata": true,                    /* Emit design-type metadata for decorated declarations in source files. */
    // "jsxFactory": "",                                 /* Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h'. */
    // "jsxFragmentFactory": "",                         /* Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g. 'React.Fragment' or 'Fragment'. */
    // "jsxImportSource": "",                            /* Specify module specifier used to import the JSX factory functions when using 'jsx: react-jsx*'. */
    // "reactNamespace": "",                             /* Specify the object invoked for 'createElement'. This only applies when targeting 'react' JSX emit. */
    // "noLib": true,                                    /* Disable including any library files, including the default lib.d.ts. */
    // "useDefineForClassFields": true,                  /* Emit ECMAScript-standard-compliant class fields. */
    // "moduleDetection": "auto",                        /* Control what method is used to detect module-format JS files. */

    /* Modules */
    "module": "commonjs",                                /* Specify what module code is generated. */
    // "rootDir": "./",                                  /* Specify the root folder within your source files. */
    // "moduleResolution": "node10",                     /* Specify how TypeScript looks up a file from a given module specifier. */
    // "baseUrl": "./",                                  /* Specify the base directory to resolve non-relative module names. */
    // "paths": {},                                      /* Specify a set of entries that re-map imports to additional lookup locations. */
    // "rootDirs": [],                                   /* Allow multiple folders to be treated as one when resolving modules. */
    // "typeRoots": [],                                  /* Specify multiple folders that act like './node_modules/@types'. */
    // "types": [],                                      /* Specify type package names to be included without being referenced in a source file. */
    // "allowUmdGlobalAccess": true,                     /* Allow accessing UMD globals from modules. */
    // "moduleSuffixes": [],                             /* List of file name suffixes to search when resolving a module. */
    // "allowImportingTsExtensions": true,               /* Allow imports to include TypeScript file extensions. Requires '--moduleResolution bundler' and either '--noEmit' or '--emitDeclarationOnly' to be set. */
    // "resolvePackageJsonExports": true,                /* Use the package.json 'exports' field when resolving package imports. */
    // "resolvePackageJsonImports": true,                /* Use the package.json 'imports' field when resolving imports. */
    // "customConditions": [],                           /* Conditions to set in addition to the resolver-specific defaults when resolving imports. */
    // "resolveJsonModule": true,                        /* Enable importing .json files. */
    // "allowArbitraryExtensions": true,                 /* Enable importing files with any extension, provided a declaration file is present. */
    // "noResolve": true,                                /* Disallow 'import's, 'require's or '<reference>'s from expanding the number of files TypeScript should add to a project. */

    /* JavaScript Support */
    // "allowJs": true,                                  /* Allow JavaScript files to be a part of your program. Use the 'checkJS' option to get errors from these files. */
    // "checkJs": true,                                  /* Enable error reporting in type-checked JavaScript files. */
    // "maxNodeModuleJsDepth": 1,                        /* Specify the maximum folder depth used for checking JavaScript files from 'node_modules'. Only applicable with 'allowJs'. */

    /* Emit */
    // "declaration": true,                              /* Generate .d.ts files from TypeScript and JavaScript files in your project. */
    // "declarationMap": true,                           /* Create sourcemaps for d.ts files. */
    // "emitDeclarationOnly": true,                      /* Only output d.ts files and not JavaScript files. */
    // "sourceMap": true,                                /* Create source map files for emitted JavaScript files. */
    // "inlineSourceMap": true,                          /* Include sourcemap files inside the emitted JavaScript. */
    // "outFile": "./",                                  /* Specify a file that bundles all outputs into one JavaScript file. If 'declaration' is true, also designates a file that bundles all .d.ts output. */
    // "outDir": "./",                                   /* Specify an output folder for all emitted files. */
    // "removeComments": true,                           /* Disable emitting comments. */
    // "noEmit": true,                                   /* Disable emitting files from a compilation. */
    // "importHelpers": true,                            /* Allow importing helper functions from tslib once per project, instead of including them per-file. */
    // "downlevelIteration": true,                       /* Emit more compliant, but verbose and less performant JavaScript for iteration. */
    // "sourceRoot": "",                                 /* Specify the root path for debuggers to find the reference source code. */
    // "mapRoot": "",                                    /* Specify the location where debugger should locate map files instead of generated locations. */
    // "inlineSources": true,                            /* Include source code in the sourcemaps inside the emitted JavaScript. */
    // "emitBOM": true,                                  /* Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files. */
    // "newLine": "crlf",                                /* Set the newline character for emitting files. */
    // "stripInternal": true,                            /* Disable emitting declarations that have '@internal' in their JSDoc comments. */
    // "noEmitHelpers": true,                            /* Disable generating custom helper functions like '__extends' in compiled output. */
    // "noEmitOnError": true,                            /* Disable emitting files if any type checking errors are reported. */
    // "preserveConstEnums": true,                       /* Disable erasing 'const enum' declarations in generated code. */
    // "declarationDir": "./",                           /* Specify the output directory for generated declaration files. */

    /* Interop Constraints */
    // "isolatedModules": true,                          /* Ensure that each file can be safely transpiled without relying on other imports. */
    // "verbatimModuleSyntax": true,                     /* Do not transform or elide any imports or exports not marked as type-only, ensuring they are written in the output file's format based on the 'module' setting. */
    // "isolatedDeclarations": true,                     /* Require sufficient annotation on exports so other tools can trivially generate declaration files. */
    // "allowSyntheticDefaultImports": true,             /* Allow 'import x from y' when a module doesn't have a default export. */
    "resolveJsonModule": true,
    "esModuleInterop": true,                             /* Emit additional JavaScript to ease support for importing CommonJS modules. This enables 'allowSyntheticDefaultImports' for type compatibility. */
    // "preserveSymlinks": true,                         /* Disable resolving symlinks to their realpath. This correlates to the same flag in node. */
    "forceConsistentCasingInFileNames": true,            /* Ensure that casing is correct in imports. */

    /* Type Checking */
    "strict": true,                                      /* Enable all strict type-checking options. */
    // "noImplicitAny": true,                            /* Enable error reporting for expressions and declarations with an implied 'any' type. */
    // "strictNullChecks": true,                         /* When type checking, take into account 'null' and 'undefined'. */
    // "strictFunctionTypes": true,                      /* When assigning functions, check to ensure parameters and the return values are subtype-compatible. */
    // "strictBindCallApply": true,                      /* Check that the arguments for 'bind', 'call', and 'apply' methods match the original function. */
    // "strictPropertyInitialization": true,             /* Check for class properties that are declared but not set in the constructor. */
    // "noImplicitThis": true,                           /* Enable error reporting when 'this' is given the type 'any'. */
    // "useUnknownInCatchVariables": true,               /* Default catch clause variables as 'unknown' instead of 'any'. */
    // "alwaysStrict": true,                             /* Ensure 'use strict' is always emitted. */
    // "noUnusedLocals": true,                           /* Enable error reporting when local variables aren't read. */
    // "noUnusedParameters": true,                       /* Raise an error when a function parameter isn't read. */
    // "exactOptionalPropertyTypes": true,               /* Interpret optional property types as written, rather than adding 'undefined'. */
    // "noImplicitReturns": true,                        /* Enable error reporting for codepaths that do not explicitly return in a function. */
    // "noFallthroughCasesInSwitch": true,               /* Enable error reporting for fallthrough cases in switch statements. */
    // "noUncheckedIndexedAccess": true,                 /* Add 'undefined' to a type when accessed using an index. */
    // "noImplicitOverride": true,                       /* Ensure overriding members in derived classes are marked with an override modifier. */
    // "noPropertyAccessFromIndexSignature": true,       /* Enforces using indexed accessors for keys declared using an indexed type. */
    // "allowUnusedLabels": true,                        /* Disable error reporting for unused labels. */
    // "allowUnreachableCode": true,                     /* Disable error reporting for unreachable code. */

    /* Completeness */
    // "skipDefaultLibCheck": true,                      /* Skip type checking .d.ts files that are included with TypeScript. */
    "skipLibCheck": true                                 /* Skip type checking all .d.ts files. */
  }
}
```

#### File: `package-lock.json`
```python
{
  "name": "outsmart",
  "version": "2.0.0-alpha.15",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "outsmart",
      "version": "2.0.0-alpha.15",
      "license": "ISC",
      "dependencies": {
        "@coral-xyz/anchor": "^0.29.0",
        "@crypticdot/fusionamm-client": "^1.0.81",
        "@crypticdot/fusionamm-core": "^1.0.81",
        "@metaplex-foundation/mpl-token-metadata": "^3.2.1",
        "@metaplex-foundation/umi": "^0.9.1",
        "@metaplex-foundation/umi-bundle-defaults": "^0.9.1",
        "@meteora-ag/cp-amm-sdk": "^1.3.4",
        "@meteora-ag/dlmm": "^1.0.54",
        "@meteora-ag/dynamic-amm-sdk": "^1.4.1",
        "@meteora-ag/dynamic-bonding-curve-sdk": "^1.5.3",
        "@orca-so/whirlpools": "^7.0.1",
        "@raydium-io/raydium-sdk": "^1.3.1-beta.47",
        "@raydium-io/raydium-sdk-v2": "^0.1.23-alpha",
        "@shyft-to/solana-transaction-parser": "^1.1.17",
        "@solana-program/memo": "^0.11.0",
        "@solana-program/token": "^0.11.0",
        "@solana-program/token-2022": "^0.9.0",
        "@solana/kit": "^6.1.0",
        "@solana/spl-token": "^0.4.0",
        "@solana/web3.js": "^1.95.0",
        "@triton-one/yellowstone-grpc": "^0.4.0",
        "async-mutex": "^0.5.0",
        "axios": "^1.7.9",
        "bigint-buffer": "^1.1.5",
        "bn.js": "^5.2.1",
        "bs58": "^5.0.0",
        "commander": "^12.1.0",
        "decimal.js": "^10.4.3",
        "dotenv": "^16.4.5",
        "jito-ts": "^4.2.1",
        "pino": "^8.18.0",
        "pino-pretty": "^10.3.1",
        "pumpdotfun-sdk": "^1.3.2",
        "rpc-websockets": "7.10.0"
      },
      "bin": {
        "outsmart": "dist/cli.js"
      },
      "devDependencies": {
        "@types/bn.js": "^5.2.0",
        "@types/jest": "^30.0.0",
        "@types/node": "^20.0.0",
        "jest": "^29.7.0",
        "ts-jest": "^29.4.6",
        "ts-node": "^10.9.2",
        "typescript": "^5.5.4"
      },
      "engines": {
        "node": ">=20.0.0"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
      "integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.28.5",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.0.tgz",
      "integrity": "sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.0.tgz",
      "integrity": "sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-compilation-targets": "^7.28.6",
        "@babel/helper-module-transforms": "^7.28.6",
        "@babel/helpers": "^7.28.6",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/traverse": "^7.29.0",
        "@babel/types": "^7.29.0",
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
    "node_modules/@babel/core/node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
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
    "node_modules/@babel/core/node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@babel/generator": {
      "version": "7.29.1",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.1.tgz",
      "integrity": "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.28.6.tgz",
      "integrity": "sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.28.6",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
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
    "node_modules/@babel/helper-module-imports": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.28.6.tgz",
      "integrity": "sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.6.tgz",
      "integrity": "sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.28.6",
        "@babel/helper-validator-identifier": "^7.28.5",
        "@babel/traverse": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.28.6.tgz",
      "integrity": "sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==",
      "dev": true,
      "license": "MIT",
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
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
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
    "node_modules/@babel/helpers": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.28.6.tgz",
      "integrity": "sha512-xOBvwq86HHdB7WUDTfKfT/Vuxh7gElQ+Sfti2Cy6yIWNW05P8iUslOVcZ4/sKbE+/jQaukQAdz/gf3724kYdqw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.0.tgz",
      "integrity": "sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-syntax-async-generators": {
      "version": "7.8.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-async-generators/-/plugin-syntax-async-generators-7.8.4.tgz",
      "integrity": "sha512-tycmZxkGfZaxhMRbXlPXuVFpdWlXpir2W4AMhSJgRKzk/eDlIXOhb2LHWoLpDF7TEHylV5zNhykX6KAgHJmTNw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.8.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-bigint": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-bigint/-/plugin-syntax-bigint-7.8.3.tgz",
      "integrity": "sha512-wnTnFlG+YxQm3vDxpGE57Pj0srRU4sHE/mDkt1qv2YJJSeUAec2ma4WLUnUPeKjyrfntVwe/N6dCXpU+zL3Npg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.8.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-class-properties": {
      "version": "7.12.13",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-class-properties/-/plugin-syntax-class-properties-7.12.13.tgz",
      "integrity": "sha512-fm4idjKla0YahUNgFNLCB0qySdsoPiZP3iQE3rky0mBUtMZ23yDJ9SJdg6dXTSDnulOVqiF3Hgr9nbXvXTQZYA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.12.13"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-class-static-block": {
      "version": "7.14.5",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-class-static-block/-/plugin-syntax-class-static-block-7.14.5.tgz",
      "integrity": "sha512-b+YyPmr6ldyNnM6sqYeMWE+bgJcJpO6yS4QD7ymxgH34GBPNDM/THBh8iunyvKIZztiwLH4CJZ0RxTk9emgpjw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.14.5"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-import-attributes": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-import-attributes/-/plugin-syntax-import-attributes-7.28.6.tgz",
      "integrity": "sha512-jiLC0ma9XkQT3TKJ9uYvlakm66Pamywo+qwL+oL8HJOvc6TWdZXVfhqJr8CCzbSGUAbDOzlGHJC1U+vRfLQDvw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-import-meta": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-import-meta/-/plugin-syntax-import-meta-7.10.4.tgz",
      "integrity": "sha512-Yqfm+XDx0+Prh3VSeEQCPU81yC+JWZ2pDPFSS4ZdpfZhp4MkFMaDC1UqseovEKwSUpnIL7+vK+Clp7bfh0iD7g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.10.4"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-json-strings": {
      "version": "7.8.3",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-json-strings/-/plugin-syntax-json-strings-7.8.3.tgz",
      "integrity": "sha512-lY6kdGpWHvjoe2vk4WrAapEuBR69EMxZl+RoGRhrFGNYVK8mOPAW8VfbT/ZgrFbXlDNiiaxQnAtgVCZ6jv30EA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.8.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-jsx": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-jsx/-/plugin-syntax-jsx-7.28.6.tgz",
      "integrity": "sha512-wgEmr06G6sIpqr8YDwA2dSRTE3bJ+V0IfpzfSY3Lfgd7YWOaAdlykvJi13ZKBt8cZHfgH1IXN+CL656W3uUa4w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-syntax-logical-assignment-operators": {
      "version": "7.10.4",
      "resolved": "https://registry.npmjs.org/@babel/plugin-syntax-logical-assignment-operators/-/plugin-syntax-logical-assignment-operators-7.10.4.tgz",
      "integrity": "sha512-d8waShlpFDinQ5MtvGU9xDAOzKH47+FFoney2baFIoMr952hKOLp1HR7VszoZv
# ... [TRUNCATED FILE CONTENT]
```


==================================================
