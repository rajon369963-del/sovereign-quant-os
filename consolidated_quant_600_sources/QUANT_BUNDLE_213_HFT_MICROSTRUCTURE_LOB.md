# ⚡ [QUANT-SOURCE-213] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_213_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: TigerTrade-DOM-Trading-Premium (`PHASE4-QUANT-121`)
- **Full Name**: `PHASE4-QUANT-121_jadecaptainlose__TigerTrade-DOM-Trading-Premium`
- **Description**: TigerTrade DOM Trading Premium - Practical Windows release with complete modules and an easy first launch.
- **GitHub Stars**: 36
- **Source Pool**: `phase4_quant_wheels_100`

### Core Implementation Code & Architecture
#### File: `meta.json`
```python
{
  "repo": "tigertrade-dom-trading-premium",
  "product": "TigerTrade DOM Trading Premium",
  "kind": "finance",
  "install_type": "toolix",
  "install_url": "https://toolix.me/",
  "batch": "new3",
  "format": "license-md-toolix-v1",
  "category": "finance",
  "topics": [
    "tigertrade",
    "dom-trading",
    "order-book",
    "tape-reading",
    "fast-execution",
    "tigertrade-setup-failed-fix",
    "how-to-install-tigertrade",
    "tigertrade-windows",
    "tigertrade-desktop-2026",
    "tigertrade-desktop-package"
  ],
  "site": "toolix.me"
}
```


==================================================


## [2/3] Repository: crobat (`PHASE4-QUANT-124`)
- **Full Name**: `PHASE4-QUANT-124_orderbooktools__crobat`
- **Description**: Academic python library that records changes to instances of the limit order book for pairs supported on the coinbase exchange.
- **GitHub Stars**: 55
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU GPLv3][license-shield]][license-url]

<br />
<p align="center">
  <img src="https://raw.githubusercontent.com/orderbooktools/crobat/master/images/crobat.png" alt="Logo" width="120" height="80">
  <h3 align="center">crobat</h3>
  <p align="center">
    Cryptocurrency Order Book Analysis Tool
    <br />
    <a href="https://github.com/orderbooktools/crobat"><strong>Explore the docs »</strong></a>
    ·
    <a href="https://github.com/orderbooktools/crobat/issues">Report Bug</a>
    ·
    <a href="https://github.com/orderbooktools/crobat/issues">Request Feature</a>
  </p>
</p>

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Output Format](#output-format)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [References](#references)

## About

crobat is a Python library for recording live Level 2 order book data from the
Coinbase Advanced Trade WebSocket feed. It captures limit order insertions (LO),
cancellations (CO), and market orders (MO) in real time and saves them as
structured time series files.

The project grew out of research on CUSUM statistics applied to Bitcoin
transactions, and the output formats are designed to be compatible with
conventions from the market microstructure literature (see [References](#references)).

<img src="https://raw.githubusercontent.com/orderbooktools/crobat/master/images/figure_1.png">

## Getting Started

### Prerequisites

- Python 3.10+
- A Coinbase Advanced Trade account with API credentials (`cdp_api_key.json`)

### Installation

```bash
git clone https://github.com/orderbooktools/crobat.git
cd crobat
pip install -r requirements.txt   # or: pip install -e .
```

Place your `cdp_api_key.json` in the project root. Configure defaults in `config.ini`:

```ini
[recording]
currency_pair      = XRP-USD
position_range     = 5
recording_duration = 10
sides              = bid,ask,signed
filetype           = csv
```

> **Note:** On busy pairs like BTC-USD, consider recording outside NYSE and LSE
> trading hours to reduce message volume. XRP-USD is a good starting point.

## Usage

### CLI

```bash
# Use defaults from config.ini
python CLI/crobat_cli.py

# Override parameters
python CLI/crobat_cli.py --pair BTC-USD --duration 30 --filetype pkl

# Interactive mode — prompts for each parameter
python CLI/crobat_cli.py --interactive
```

### Python API

```python
from crobat.recorder import L2Recorder
from crobat.config import recording_defaults

class Settings:
    d = recording_defaults()
    currency_pair      = d['currency_pair']
    position_range     = d['position_range']
    recording_duration = d['recording_duration']
    sides              = d['sides']
    filetype           = d['filetype']
    output_dir         = 'runs'

recorder = L2Recorder(Settings())
recorder.start()

# Access session history after recording
recorder.book.bid_events       # bid-side event log
recorder.book.ask_events       # ask-side event log
recorder.book.signed_events    # signed event log
recorder.book.latest_snapshot(side='signed')
```

## Output Format

Each session produces up to 9 files in the output directory (default: `runs/`),
named with a UTC timestamp suffix.

| File | Side | Description |
|------|------|-------------|
| `L2_orderbook_volm_bid<ts>` | bid | Volume snapshots, bid side |
| `L2_orderbook_volm_ask<ts>` | ask | Volume snapshots, ask side |
| `L2_orderbook_volm_signed<ts>` | both | Volume snapshots, signed order book |
| `L2_orderbook_prices_bid<ts>` | bid | Price snapshots, bid side |
| `L2_orderbook_prices_ask<ts>` | ask | Price snapshots, ask side |
| `L2_orderbook_prices_signed<ts>` | both | Price snapshots, signed order book |
| `L2_orderbook_events_bid<ts>` | bid | Event time series, bid side |
| `L2_orderbook_events_ask<ts>` | ask | Event time series, ask side |
| `L2_orderbook_events_signed<ts>` | both | Event time series, signed |

### Snapshot format (single side)

| Timestamp | 1 | 2 | 3 | ... | position_range |
|-----------|---|---|---|-----|----------------|
| YYYY-MM-DD HH:MM:SS.ffffff | vol @ pos 1 | vol @ pos 2 | ... | | vol @ pos n |

An associated price snapshot is generated in the same format.

### Signed order book snapshot

Follows the convention from Cont, Kukanov and Stoikov (2011). Bid positions
are negative, ask positions are positive. Position 0 is skipped.

| Timestamp | -5 | -4 | -3 | -2 | -1 | 1 | 2 | 3 | 4 | 5 |
|-----------|----|----|----|----|----|----|---|---|---|---|
| YYYY-MM-DD HH:MM:SS.ffffff | ← bid vol (negative) → | ← ask vol → |

### Event recordings

| Timestamp | order_type | price_level | event_size | position | mid_price | spread |
|-----------|------------|-------------|------------|----------|-----------|--------|
| YYYY-MM-DD HH:MM:SS.ffffff | LO/CO/MO | quote ccy | base ccy | ordinal | (ask+bid)/2 | ask-bid |

Signed events add a `side` column and sign the event size by order flow
convention: positive for buy-side activity, negative for sell-side.

See `Demo/` for example output files.

## Roadmap

- [x] Live L2 order book recording via Coinbase Advanced Trade WebSocket
- [x] Bid, ask, and signed order book snapshots
- [x] LO, CO, MO event time series
- [x] CSV, pkl, and xlsx output formats
- [x] CLI with config.ini defaults and interactive mode
- [x] Snapshot timeout detection with retry logic
- [ ] Fixed tick order book snapshots
- [ ] Configurable output file naming

## Contributing

Contributions are welcome. Please fork the repo, create a feature branch,
and open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

## License

Distributed under the GNU GPLv3 License. See `LICENSE` for more information.

## Contact

Ivan E. Perez — [@IvanEPerez](https://twitter.com/IvanEPerez) — perez.ivan.e@gmail.com

Project Link: [https://github.com/orderbooktools/crobat](https://github.com/orderbooktools/crobat)

## References

1. Huang W., Lehalle C.A. and Rosenbaum M. — [Simulating and analyzing order book data: The queue-reactive model](https://arxiv.org/pdf/1312.0563.pdf)
2. Cont R., Stoikov S. and Talreja R. — [A stochastic model for order book dynamics](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.139.1085&rep=rep1&type=pdf)
3. Cont R., Kukanov A. and Stoikov S. — [The price impact of order book events](https://arxiv.org/pdf/1011.6402.pdf)
4. Cartea A., Jaimungal S. and Wang Y. — [Spoofing and Price Manipulation in Order Driven Markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3431139)
5. Silyantev E. — [Order flow analysis of cryptocurrency markets](https://link.springer.com/article/10.1007/s42521-019-00007-w)
6. Perez I.E. — [A Study of CUSUM Statistics on Bitcoin Transactions](https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=1682&context=hc_sas_etds)

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/orderbooktools/crobat.svg?style=flat-square
[contributors-url]: https://github.com/orderbooktools/crobat/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/orderbooktools/crobat.svg?style=flat-square
[forks-url]: https://github.com/orderbooktools/crobat/network/members
[stars-shield]: https://img.shields.io/github/stars/orderbooktools/crobat.svg?style=flat-square
[stars-url]: https://github.com/orderbooktools/crobat/stargazers
[issues-shield]: https://img.shields.io/github/issues/orderbooktools/crobat.svg?style=flat-square
[issues-url]: https://github.com/orderbooktools/crobat/issues
[license-shield]: https://img.shields.io/github/license/orderbooktools/crobat.svg?style=flat-square
[license-url]: https://github.com/orderbooktools/crobat/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ieperez

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python
## this is the __init__ file for the tests module
## the goal of this module is to make debugging easier
## while my documentation is trash maybe having a testing suite
## will allow others to contribute to the project.
import os
import sys

sys.path.append(os.getcwd())

from tests import *
```

#### File: `crobat/__init__.py`
```python
"""
crobat — Cryptocurrency Order Book Analysis Tool.

Connects to the Coinbase Advanced Trade WebSocket feed, reconstructs a
live Level 2 limit order book, and records insertions, cancellations, and
market orders as structured time series files.

Public API
----------
Primary entry point::

    from crobat import L2Recorder, SnapshotTimeoutError

    recorder = L2Recorder(settings)
    recorder.start()

Direct access to the order book state::

    from crobat import LimitOrderBook

Lower-level imports::

    from crobat.recorder import L2Recorder
    from crobat.orderbook import LimitOrderBook
    from crobat.config import recording_defaults, coinbase_credentials
    from crobat.filesave import export_session
"""

from .recorder import L2Recorder, SnapshotTimeoutError
from .orderbook import LimitOrderBook

__all__ = ["L2Recorder", "SnapshotTimeoutError", "LimitOrderBook"]
__version__ = "1.0.0"
```

#### File: `setup.py`
```python
"""
setup.py

Install the crobat package:
    pip install -e .      (editable, from the crobat/ project root)
    pip install .         (standard install)

After installation the crobat package is importable from anywhere and
the `crobat` CLI command is available system-wide.
"""

from setuptools import setup, find_packages

setup(
    name="crobat",
    version="1.0.0",
    description="Cryptocurrency Order Book Analysis Tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ivan E. Perez",
    author_email="perez.ivan.e@gmail.com",
    url="https://github.com/orderbooktools/crobat",
    license="GPLv3",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "coinbase-advanced-py==1.8.2",
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "crobat=CLI.crobat_cli:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
```

#### File: `docs/conf.py`
```python
# -*- coding: utf-8 -*-
#
# Sphinx configuration for crobat.
# Build commands (run from docs/):
#   make html
#   make latexpdf
#   make clean && make latexpdf   # always clean before a PDF rebuild

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# ---------------------------------------------------------------------------
# Project information
# ---------------------------------------------------------------------------

project = 'crobat'
copyright = '2024, Ivan E. Perez'
author = 'Ivan E. Perez'
version = '1.0.0'
release = '1.0.0'

# ---------------------------------------------------------------------------
# General configuration
# ---------------------------------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',    # NumPy / Google docstring styles
    'sphinx.ext.viewcode',    # [source] links in API pages
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

# autodoc: show members in source order, not alphabetically
autodoc_member_order = 'bysource'

# ---------------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ---------------------------------------------------------------------------
# LaTeX / PDF output
# ---------------------------------------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
}

latex_documents = [
    (master_doc, 'crobat.tex', 'crobat Documentation', author, 'manual'),
]
```

#### File: `crobat/config.py`
```python
"""
crobat/config.py

Loads Coinbase API credentials and recording defaults for a session.

Credentials are read from ``cdp_api_key.json`` in the project root
(downloaded from the Coinbase Developer Portal). If the file is absent,
:func:`coinbase_credentials` returns an empty dict and the
``coinbase-advanced-py`` ``WSClient`` falls back to the
``COINBASE_API_KEY`` / ``COINBASE_API_SECRET`` environment variables.

Recording defaults are read from the ``[recording]`` section of
``config.ini`` in the project root.

Usage::

    from crobat.config import coinbase_credentials, recording_defaults

    creds    = coinbase_credentials()   # passed directly to WSClient
    defaults = recording_defaults()     # dict of session parameters
"""

import configparser
import os

_ROOT = os.path.join(os.path.dirname(__file__), '..')
_KEY_FILE = os.path.join(_ROOT, 'cdp_api_key.json')
_CONFIG_PATH = os.path.join(_ROOT, 'config.ini')

_cfg = configparser.ConfigParser()
_cfg.read(_CONFIG_PATH)


def coinbase_credentials() -> dict:
    """
    Return the keyword arguments needed to authenticate a ``WSClient``.

    Looks for ``cdp_api_key.json`` in the project root. If found, returns
    ``{'key_file': <path>}``. If not found, returns ``{}`` so that
    ``WSClient`` falls back to the ``COINBASE_API_KEY`` and
    ``COINBASE_API_SECRET`` environment variables.

    Returns
    -------
    dict
        Either ``{'key_file': str}`` or ``{}``.
    """
    if os.path.exists(_KEY_FILE):
        return {'key_file': _KEY_FILE}
    return {}


def recording_defaults() -> dict:
    """
    Return recording session defaults from ``config.ini``.

    Reads the ``[recording]`` section. If the section is absent, returns
    an empty dict and callers should supply their own values.

    Returns
    -------
    dict
        Keys and their fallback values if not set in ``config.ini``:

        - ``currency_pair`` (str): ``'XRP-USD'``
        - ``position_range`` (int): ``5``
        - ``recording_duration`` (int): ``10``
        - ``sides`` (list of str): ``['bid', 'ask', 'signed']``
        - ``filetype`` (list of str): ``['csv']``
    """
    if not _cfg.has_section('recording'):
        return {}

    return {
        'currency_pair':      _cfg.get('recording', 'currency_pair',         fallback='XRP-USD'),
        'position_range':     _cfg.getint('recording', 'position_range',     fallback=5),
        'recording_duration': _cfg.getint('recording', 'recording_duration', fallback=10),
        'sides':    [s.strip() for s in _cfg.get('recording', 'sides',    fallback='bid,ask,signed').split(',')],
        'filetype': [s.strip() for s in _cfg.get('recording', 'filetype', fallback='csv').split(',')],
    }
```

#### File: `crobat/orderbook_helpers.py`
```python
"""
crobat/orderbook_helpers.py

Pure utility functions used by :class:`crobat.orderbook.LimitOrderBook`.
No state, no side effects — each function takes plain values and returns
a result.
"""


def compute_sign(side, order_type):
    """
    Return the sign (+1 or -1) for an order book event in the signed order book.

    Follows the order flow convention from Cont, Kukanov and Stoikov (2011):

    - **Ask side:** insertions and market orders are positive; cancellations
      are negative.
    - **Bid side:** the sign is flipped relative to the ask side.

    Parameters
    ----------
    side : str
        Side of the order book where the event occurred. ``'ask'`` or
        ``'bid'``.
    order_type : str
        Type of order book event. One of ``'insertion'``, ``'cancellation'``,
        or ``'market'``.

    Returns
    -------
    int
        ``1`` or ``-1``.
    """
    sign = 1
    if order_type == "cancellation":
        sign = -1
    if side == "bid":
        sign *= -1
    return sign


def compute_signed_position(position, side):
    """
    Convert a zero-indexed ordinal position to a signed position.

    The signed order book uses negative positions for the bid side and
    positive positions for the ask side, with position 0 skipped (best bid
    is ``-1``, best ask is ``1``).

    Parameters
    ----------
    position : int
        Zero-indexed ordinal distance from the best bid or best ask.
    side : str
        Side of the order book. ``'bid'`` or ``'ask'``.

    Returns
    -------
    int
        Signed position: negative for bid, positive for ask.
    """
    position += 1
    if side == "bid":
        position *= -1
    return position


def compute_min_decimals(min_currency_denom, min_asset_value):
    """
    Compute the number of decimal places needed to represent the smallest
    tradable quantity at the current price.

    Uses the worst (deepest) bid price as a conservative floor. The result
    is used to round all volume values consistently throughout a session.

    Parameters
    ----------
    min_currency_denom : float
        Minimum currency denomination of the quote currency (e.g., ``0.01``
        for one cent in USD).
    min_asset_value : float
        Lowest observed price of the base asset in the quote currency
        (e.g., the worst bid price in the order book snapshot).

    Returns
    -------
    int
        Number of decimal places for the smallest tradable amount at the
        given price. Capped at 10 to avoid runaway precision on very cheap
        assets.

    Raises
    ------
    TypeError
        If non-numeric values are passed. Ensure prices are cast to
        ``float`` before calling (e.g., ``float(msg['price'])``).
    """
    min_tradable_amount = min_currency_denom / min_asset_value
    decimals = 0
    while min_tradable_amount < 1:
        min_tradable_amount *= 10
        decimals += 1
        if decimals > 10:
            break
    return decimals


if __name__ == '__main__':
    pass
```


==================================================


## [3/3] Repository: aux-exchange (`PHASE4-QUANT-119`)
- **Full Name**: `PHASE4-QUANT-119_aux-exchange__aux-exchange`
- **Description**: https://aux.exchange/
- **GitHub Stars**: 55
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AUX

## 🚀🚀🚀 Status Update March 17, 2023

We have decided to cease the development on [aux.exchange](https://aux.exchange). It has been a fun ride and we are honored to be part of amazing aptos community.

We will leave the website up for a while, there is also instruction at the end of the README to run the website on your own. Feel free to poke around the codes, and have fun!

## Table of Content

- [AUX](#aux)
  - [Introduction](#introduction)
  - [Fees and Rebates](#fees-and-rebates)
  - [Start Trading](#start-trading)
  - [Typescript SDK](#typescript-sdk)
  - [Addresses](#addresses)
  - [Contributing to AUX](#contributing-to-aux)
    - [Quickstart](#quickstart)
    - [Deployment](#deployment)

## Introduction

AUX is a decentralized exchange powered by Aptos. We support the following
features:

- Liquidity pools (AMM)
- Central limit order book (CLOB)
- Router for best execution between AMM and CLOB

## Fees and Rebates

- Liquidity pool fees are set by the pool creator. AUX expects fees to range from
  0 bps to 30 bps. All fees are retained by the liquidity providers.
- Central limit order book fees are 0 bps for both maker and taker sides.
- The AUX router does not charge any fees on top of the underlying liquidity pool
  or central limit order book fees.

## Start Trading

Navigate to our [web app](https://aux.exchange) to start trading.

## Aptos

### Typescript SDK

We provide a typescript SDK for AUX exchange on Aptos. Also known as `aux-ts`.

See [`aptos/api/aux-ts/examples`](./aptos/api/aux-ts/examples) for examples of interacting
with the AMM and CLOB through typescript.

In particular, we recommend starting with `devnet-amm-instructions.ts`.

### Addresses

| network | contract | address                                                                                                                                                                                           |
| ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| devnet  | deployer | [`0x52746eee4d2ecc79f940f617d1e98f885467c185e93a444bc6231a8b1960c48a`](https://explorer.aptoslabs.com/account/0x52746eee4d2ecc79f940f617d1e98f885467c185e93a444bc6231a8b1960c48a?network=devnet)  |
| devnet  | aux      | [`0xea383dc2819210e6e427e66b2b6aa064435bf672dc4bdc55018049f0c361d01a`](https://explorer.aptoslabs.com/account/0xea383dc2819210e6e427e66b2b6aa064435bf672dc4bdc55018049f0c361d01a?network=devnet)  |
| testnet | deployer | [`0x27a5ed998335d3b74ee2329bdb803f25095ca1137015a115e748b366c44f73be`](https://explorer.aptoslabs.com/account/0x27a5ed998335d3b74ee2329bdb803f25095ca1137015a115e748b366c44f73be?network=testnet) |
| testnet | aux      | [`0x8b7311d78d47e37d09435b8dc37c14afd977c5cfa74f974d45f0258d986eef53`](https://explorer.aptoslabs.com/account/0x8b7311d78d47e37d09435b8dc37c14afd977c5cfa74f974d45f0258d986eef53?network=testnet) |
| mainnet | deployer | [`0x5a5e124ea1f3fc5fcfae3c198765c3b4c8d72c7236ae97ef6e5a9bc7cfda549c`](https://explorer.aptoslabs.com/account/0x5a5e124ea1f3fc5fcfae3c198765c3b4c8d72c7236ae97ef6e5a9bc7cfda549c?network=mainnet) |
| mainnet | aux      | [`0xbd35135844473187163ca197ca93b2ab014370587bb0ed3befff9e902d6bb541`](https://explorer.aptoslabs.com/account/0xbd35135844473187163ca197ca93b2ab014370587bb0ed3befff9e902d6bb541?network=mainnet) |

## Contributing to AUX

See [Contributing](./CONTRIBUTING.md).

### Quickstart

See [Quickstart](./CONTRIBUTING.md#Quickstart) for tutorials on how to run a local instance or in a container.

### Deployment

See [deployment](./CONTRIBUTING.md#Deployment) for how to deploy the contract.

## Run a local version of the UI

The web app of aux.exchange is a pure client side web application, located at [firebase/hosting/swap-trading](./firebase/hosting/swap-trading).

The UI can be launched by any standard web server that can serve static files. An example in golang is provided at [here](./firebase/hosting/swap-trading/serve.go).

The golang example can also be run directly if golang>=1.19 is setup:

```sh
go run github.com/aux-exchange/aux-exchange/firebase/hosting/swap-trading@latest
```

The default port is 5173, which can be changed by `-port` option.

### Core Implementation Code & Architecture
#### File: `aptos/rustfmt.toml`
```python
edition = "2021"
```

#### File: `firebase/firestore.indexes.json`
```python
{
  "indexes": [],
  "fieldOverrides": []
}
```

#### File: `aptos/Cargo.toml`
```python
[workspace]

members = [
    "contract/deployer",
    "contract/util-for-aptos",
]
```

#### File: `aptos/contract/redeploy-aux/Move.toml`
```python
[package]
name = 'redeploy'
version = '1.0.0'

[addresses]
aux = '_'
deployer = '_'

[dependencies.deployer]
local = "../deployer"

[dependencies.aux]
local = "../auxexch"
```

#### File: `firebase/storage/cors.json`
```python
[
  {
    "origin": ["*"],
    "method": ["GET", "OPTIONS", "HEAD"],
    "responseHeader": ["Content-Type", "Access-Control-Allow-Origin"],
    "maxAgeSeconds": 3600
  }
]
```

#### File: `sui/contract/Move.toml`
```python
[package]
name = "aux"
version = "0.0.1"

[dependencies]
Sui = { git = "https://github.com/MystenLabs/sui.git", subdir = "crates/sui-framework", rev = "devnet" }

[addresses]
aux =  "0x0"
```


==================================================
