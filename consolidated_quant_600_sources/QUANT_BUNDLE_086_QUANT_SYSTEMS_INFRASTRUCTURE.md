# ⚡ [QUANT-SOURCE-086] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_086_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: uv (`WHEEL_uv`)
- **Full Name**: `uv`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# uv

<a href="https://pypi.python.org/pypi/uv"><img src="https://img.shields.io/pypi/v/uv.svg" alt="Latest PyPI version" /></a>
<a href="https://pypi.python.org/pypi/uv"><img src="https://img.shields.io/pypi/pyversions/uv.svg" alt="Supported Python versions" /></a>
<a href="https://discord.gg/astral-sh"><img src="https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white" alt="Discord" /></a>

An extremely fast Python package and project manager, written in Rust.

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
    <img alt="Shows a bar chart with benchmark results." src="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
  </picture>
</p>

<p align="center">
  <i>Installing <a href="https://trio.readthedocs.io/">Trio</a>'s dependencies with a warm cache.</i>
</p>

## Highlights

- A single tool to replace `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and
  more.
- [10-100x faster](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md) than `pip`.
- Provides [comprehensive project management](#projects), with a
  [universal lockfile](https://docs.astral.sh/uv/concepts/projects/layout#the-lockfile).
- [Runs scripts](#scripts), with support for
  [inline dependency metadata](https://docs.astral.sh/uv/guides/scripts#declaring-script-dependencies).
- [Installs and manages](#python-versions) Python versions.
- [Runs and installs](#tools) tools published as Python packages.
- Includes a [pip-compatible interface](#the-pip-interface) for a performance boost with a familiar
  CLI.
- Supports Cargo-style [workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces) for
  scalable projects.
- Disk-space efficient, with a [global cache](https://docs.astral.sh/uv/concepts/cache) for
  dependency deduplication.
- Installable without Rust or Python via `curl` or `pip`.
- Supports macOS, Linux, and Windows.

uv is backed by [Astral](https://astral.sh), the creators of
[Ruff](https://github.com/astral-sh/ruff) and [ty](https://github.com/astral-sh/ty).

## Installation

Install uv with our standalone installers:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, from [PyPI](https://pypi.org/project/uv/):

```bash
# With pip.
pip install uv
```

```bash
# Or pipx.
pipx install uv
```

If installed via the standalone installer, uv can update itself to the latest version:

```bash
uv self update
```

See the [installation documentation](https://docs.astral.sh/uv/getting-started/installation/) for
details and alternative installation methods.

## Documentation

uv's documentation is available at [docs.astral.sh/uv](https://docs.astral.sh/uv).

Additionally, the command line reference documentation can be viewed with `uv help`.

## Features

### Projects

uv manages project dependencies and environments, with support for lockfiles, workspaces, and more,
similar to `rye` or `poetry`:

```console
$ uv init example
Initialized project `example` at `/home/user/example`

$ cd example

$ uv add ruff
Creating virtual environment at: .venv
Resolved 2 packages in 170ms
   Built example @ file:///home/user/example
Prepared 2 packages in 627ms
Installed 2 packages in 1ms
 + example==0.1.0 (from file:///home/user/example)
 + ruff==0.5.0

$ uv run ruff check
All checks passed!

$ uv lock
Resolved 2 packages in 0.33ms

$ uv sync
Resolved 2 packages in 0.70ms
Checked 1 package in 0.02ms
```

See the [project documentation](https://docs.astral.sh/uv/guides/projects/) to get started.

uv also supports building and publishing projects, even if they're not managed with uv. See the
[publish guide](https://docs.astral.sh/uv/guides/publish/) to learn more.

### Scripts

uv manages dependencies and environments for single-file scripts.

Create a new script and add inline metadata declaring its dependencies:

```console
$ echo 'import requests; print(requests.get("https://astral.sh"))' > example.py

$ uv add --script example.py requests
Updated `example.py`
```

Then, run the script in an isolated virtual environment:

```console
$ uv run example.py
Reading inline script metadata from: example.py
Installed 5 packages in 12ms
<Response [200]>
```

See the [scripts documentation](https://docs.astral.sh/uv/guides/scripts/) to get started.

### Tools

uv executes and installs command-line tools provided by Python packages, similar to `pipx`.

Run a tool in an ephemeral environment using `uvx` (an alias for `uv tool run`):

```console
$ uvx pycowsay 'hello world!'
Resolved 1 package in 167ms
Installed 1 package in 9ms
 + pycowsay==0.0.0.2
  """

  ------------
< hello world! >
  ------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
```

Install a tool with `uv tool install`:

```console
$ uv tool install ruff
Resolved 1 package in 6ms
Installed 1 package in 2ms
 + ruff==0.5.0
Installed 1 executable: ruff

$ ruff --version
ruff 0.5.0
```

See the [tools documentation](https://docs.astral.sh/uv/guides/tools/) to get started.

### Python versions

uv installs Python and allows quickly switching between versions.

Install multiple Python versions:

```console
$ uv python install 3.12 3.13 3.14
Installed 3 versions in 972ms
 + cpython-3.12.12-macos-aarch64-none (python3.12)
 + cpython-3.13.9-macos-aarch64-none (python3.13)
 + cpython-3.14.0-macos-aarch64-none (python3.14)

```

Download Python versions as needed:

```console
$ uv venv --python 3.12.0
Using Python 3.12.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

$ uv run --python pypy@3.8 -- python --version
Python 3.8.16 (a9dbdca6fc3286b0addd2240f11d97d8e8de187a, Dec 29 2022, 11:45:30)
[PyPy 7.3.11 with GCC Apple LLVM 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>>
```

Use a specific Python version in the current directory:

```console
$ uv python pin 3.11
Pinned `.python-version` to `3.11`
```

See the [Python installation documentation](https://docs.astral.sh/uv/guides/install-python/) to get
started.

### The pip interface

uv provides a drop-in replacement for common `pip`, `pip-tools`, and `virtualenv` commands.

uv extends their interfaces with advanced features, such as dependency version overrides,
platform-independent resolutions, reproducible resolutions, alternative resolution strategies, and
more.

Migrate to uv without changing your existing workflows — and experience a 10-100x speedup — with the
`uv pip` interface.

Compile requirements into a platform-independent requirements file:

```console
$ uv pip compile requirements.in \
   --universal \
   --output-file requirements.txt
Resolved 43 packages in 12ms
```

Create a virtual environment:

```console
$ uv venv
Using Python 3.12.3
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

Install the locked requirements:

```console
$ uv pip sync requirements.txt
Resolved 43 packages in 11ms
Installed 43 packages in 208ms
 + babel==2.15.0
 + black==24.4.2
 + certifi==2024.7.4
 ...
```

See the [pip interface documentation](https://docs.astral.sh/uv/pip/index/) to get started.

## Contributing

We are passionate about supporting contributors of all levels of experience and would love to see
you get involved in the project. See the
[contributing guide](https://github.com/astral-sh/uv?tab=contributing-ov-file#contributing) to get
started.

## FAQ

#### How do you pronounce uv?

It's pronounced as "you - vee" ([`/juː viː/`](https://en.wikipedia.org/wiki/Help:IPA/English#Key))

#### How should I stylize uv?

Just "uv", please. See the [style guide](./STYLE.md#styling-uv) for details.

#### What platforms does uv support?

See uv's [platform support](https://docs.astral.sh/uv/reference/platforms/) document.

#### Is uv ready for production?

Yes, uv is stable and widely used in production. See uv's
[versioning policy](https://docs.astral.sh/uv/reference/versioning/) document for details.

## Acknowledgements

uv's dependency resolver uses [PubGrub](https://github.com/pubgrub-rs/pubgrub) under the hood. We're
grateful to the PubGrub maintainers, especially [Jacob Finkelman](https://github.com/Eh2406), for
their support.

uv's Git implementation is based on [Cargo](https://github.com/rust-lang/cargo).

Some of uv's optimizations are inspired by the great work we've seen in [pnpm](https://pnpm.io/),
[Orogene](https://github.com/orogene/orogene), and [Bun](https://github.com/oven-sh/bun). We've also
learned a lot from Nathaniel J. Smith's [Posy](https://github.com/njsmith/posy) and adapted its
[trampoline](https://github.com/njsmith/posy/tree/main/src/trampolines/windows-trampolines/posy-trampoline)
for Windows support.

## License

uv is licensed under either of

- Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or
  <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)

at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in uv
by you, as defined in the Apache-2.0 license, shall be dually licensed as above, without any
additional terms or conditions.

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/uv/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>

### Core Implementation Code & Architecture
#### File: `crates/uv-python/python/__init__.py`
```python

```

#### File: `test/packages/setup_cfg_editable/setup_cfg_editable/__init__.py`
```python

```

#### File: `test/packages/deptry_reproducer/python/deptry_reproducer/foo.py`
```python

```

#### File: `test/packages/setup_py_editable/setup_py_editable/__init__.py`
```python

```

#### File: `test/packages/keyring_test_plugin/keyrings/__init__.py`
```python

```

#### File: `test/packages/hatchling_editable/logging/__init__.py`
```python

```


==================================================


## [2/3] Repository: vollib (`WHEEL_vollib`)
- **Full Name**: `vollib`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# `vollib`

`vollib` is a python library for calculating option prices, 
implied volatility and greeks. At its core is Peter Jäckel's 
source code for `LetsBeRational`, an extremely fast and accurate algorithm 
for obtaining Black's implied volatility from option prices.

Building on this solid foundation, `vollib` provides functions 
to calculate option prices, implied volatility and greeks using 
Black, Black-Scholes, and Black-Scholes-Merton. `vollib` 
implements both analytical and numerical greeks for each of the three pricing formulae.

### About the initial release

This is the initial release of `vollib`.  Tests and documentation are still incomplete.

### Dependencies

`vollib` was written in Python 2.7.  It depends on the ```lets_be_rational``` package, a simple (SWIG) wrapper around Peter Jäckel's original C source code.  

To install via pip, type the following:

```
>>> pip install vollib
```

Installing `vollib` via pip will automatically install the necessary dependencies,
except for SWIG, pip, and Python.  This has been tested to work on Windows, Linux and Macintosh OS X.

Python, pip and SWIG must be installed prior to installing ```vollib```. 


`lets_be_rational` is quite stable compared to `vollib`, which is likely to be updated frequently.

For those who wish to clone the vollib repo, you might prefer to install `lets_be_rational` 
separately with pip, since this takes care of the C compilation.

### About "Let's be Rational":

["Let's Be Rational"](http://www.pjaeckel.webspace.virginmedia.com/LetsBeRational.pdf) is a paper by [Peter Jäckel](http://jaeckel.org) showing *"how Black's volatility can be implied from option prices with as little as two iterations to maximum attainable precision on standard (64 bit floating point) hardware for all possible inputs."*

The paper is accompanied by the full C source code, which resides at [www.jaeckel.org/LetsBeRational.7z](www.jaeckel.org/LetsBeRational.7z).

```
Copyright © 2013-2014 Peter Jäckel.

Permission to use, copy, modify, and distribute this software is freely granted,
provided that this notice is preserved.

WARRANTY DISCLAIMER
The Software is provided "as is" without warranty of any kind, either express or implied,
including without limitation any implied warranties of condition, uninterrupted use,
merchantability, fitness for a particular purpose, or non-infringement.
```

### Links:


  * [Let's Be Rational](http://www.pjaeckel.webspace.virginmedia.com/LetsBeRational.pdf)

  *  [pip](https://pypi.python.org/pypi/pip)

  *  [SWIG](http://www.swig.org/download.html)
  
  * [Licence](http://vollib.org/license)

  * [Vollib Home](http://vollib.org)

### Core Implementation Code & Architecture
#### File: `vollib/black_scholes/greeks/__init__.py`
```python

```

#### File: `vollib/tests/__init__.py`
```python

```

#### File: `vollib/black_scholes_merton/greeks/__init__.py`
```python

```

#### File: `vollib/black/greeks/__init__.py`
```python

```

#### File: `setup.py`
```python
#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages


setup(
    name='vollib',
    version='0.1.5',
    description='',
    url='http://vollib.org',
    # download_url='git+https://github.com/vollib/vollib.git#egg=vollib',
    maintainer='vollib',
    maintainer_email='support@quantycarlo.com',
    license='MIT',
    install_requires = [
        'lets_be_rational',
        'simplejson',
        'numpy',
        'pandas'
    ],
    packages=find_packages(exclude=['docs', 'vollib/tests'])
)
```

#### File: `vollib/tests/test_utils.py`
```python
from collections import OrderedDict
import simplejson as json
import pandas



def almost_equal(a,b,epsilon = 1.0e-7):
    return abs(a-b)< epsilon


class TestDataIterator(object):

    """
    >>> data_iterator = TestDataIterator()
    >>> print data_iterator.has_next()
    True
    >>> r = data_iterator.next_row()
    >>> print r['S']
    100.0
    """
    
    def __init__(self):
        self.data = json.load(open('test_data.json','rb'))
        columns = self.data['columns']
        grid_data = OrderedDict()

        for header in columns:
            grid_data[header]=[]

        for col in self.data['data']:
            for i in range(len(columns)):
                grid_data[columns[i]].append(col[i])

        self.df = pandas.DataFrame(grid_data)
        self.row_id = 0
        self.row_count = self.df.S.count()

    def next_row(self):
        if self.has_next():
            row = self.df.ix[self.row_id].to_dict()
            self.row_id +=1
            return row

    def has_next(self):
        return self.row_id < self.row_count
    
    
# -----------------------------------------------------------------------------
# MAIN
if __name__=='__main__':  
    import doctest
    if not doctest.testmod().failed:
        print "Doctest passed"
```


==================================================


## [3/3] Repository: wallstreet (`WHEEL_wallstreet`)
- **Full Name**: `wallstreet`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
Wallstreet: Real time Stock and Option tools
--------------------------------------------

Wallstreet is a Python 3 library for monitoring and analyzing real time Stock and
Option data. Quotes are provided from the Google Finance API. Wallstreet requires
minimal input from the user, it uses available online data to calculate option
greeks and even scrapes the US Treasury website to get the current risk free rate.


Usage
-----

Stocks:

.. code-block:: Python

  from wallstreet import Stock, Call, Put

  >>> s = Stock('AAPL')
  >>> s.price
  96.44
  >>> s.price
  96.48
  >>> s.change
  -0.35
  >>> s.last_trade
  '21 Jan 2016 13:32:12'

Options:

.. code-block:: Python

  >>> g = Call('GOOG', d=12, m=2, y=2016, strike=700)
  >>> g.price
  38.2
  >>> g.implied_volatility()
  0.49222968442691889
  >>> g.delta()
  0.56522039722040063
  >>> g.vega()
  0.685034827159825
  >>> g.underlying.price
  706.59

Alternative construction:

.. code-block:: Python

  >>> g = Call('GOOG', d=12, m=2, y=2016)
  >>> g
  Call(ticker=GOOG, expiration='12-02-2016')
  >>> g.strikes
  (580, 610, 620, 630, 640, 650, 660, 670, 680, 690, 697.5, 700, 702.5, 707.5, 710, 712.5, 715, 720, ...)
  >>> g.set_strike(712.5)
  >>> g
  Call(ticker=GOOG, expiration='12-02-2016', strike=712.5)

or

.. code-block:: Python

  >>> g = Put("GOOG")
  'No options listed for given date, using 22-01-2016 instead'
  >>> g.expirations
  ['22-01-2016', '29-01-2016', '05-02-2016', '12-02-2016', '19-02-2016', '26-02-2016', '04-03-2016', ...]
  >>> g
  Put(ticker=GOOG, expiration='22-01-2016')

Yahoo Finance Support (keep in mind that YF quotes might be delayed):

.. code-block:: Python

    >>> apple = Stock('AAPL', source='yahoo')
    >>> call = Call('AAPL', strike=apple.price, source='yahoo')
    No options listed for given date, using '26-05-2017' instead
    No option for given strike, using 155 instead

Download historical data (requires pandas)

.. code-block:: Python

    s = Stock('BTC-USD')
    >>> df = s.historical(days_back=30, frequency='d')
    >>> df
             Date          Open          High           Low         Close     Adj Close      Volume
    0  2019-07-10  12567.019531  13183.730469  11569.940430  12099.120117  12099.120117  1554955347
    1  2019-07-11  12099.120117  12099.910156  11002.389648  11343.120117  11343.120117  1185222449
    2  2019-07-12  11343.120117  11931.910156  11096.610352  11797.370117  11797.370117   647690095
    3  2019-07-13  11797.370117  11835.870117  10827.530273  11363.969727  11363.969727   668325183
    4  2019-07-14  11363.969727  11447.919922  10118.849609  10204.410156  10204.410156   814667763
    5  2019-07-15  10204.410156  11070.179688   9877.019531  10850.259766  10850.259766   965178341
    6  2019-07-16  10850.259766  11025.759766   9366.820313   9423.440430   9423.440430  1140137759
    7  2019-07-17   9423.440430   9982.240234   9086.509766   9696.150391   9696.150391   965256823
    8  2019-07-18   9696.150391  10776.540039   9292.610352  10638.349609  10638.349609  1033842556
    9  2019-07-19  10638.349609  10757.410156  10135.160156  10532.940430  10532.940430   658190962
    10 2019-07-20  10532.940430  11094.320313  10379.190430  10759.419922  10759.419922   608954333
    11 2019-07-21  10759.419922  10833.990234  10329.889648  10586.709961  10586.709961   405339891
    12 2019-07-22  10586.709961  10676.599609  10072.070313  10325.870117  10325.870117   524442852
    13 2019-07-23  10325.870117  10328.440430   9820.610352   9854.150391   9854.150391   529438124
    14 2019-07-24   9854.150391   9920.540039   9535.780273   9772.139648   9772.139648   531611909
    15 2019-07-25   9772.139648  10184.429688   9744.700195   9882.429688   9882.429688   403576364
    16 2019-07-26   9882.429688   9890.049805   9668.519531   9847.450195   9847.450195   312717110
    17 2019-07-27   9847.450195  10202.950195   9310.469727   9478.320313   9478.320313   512612117
    18 2019-07-28   9478.320313   9591.519531   9135.639648   9531.769531   9531.769531   267243770
    19 2019-07-29   9531.769531   9717.690430   9386.900391   9506.929688   9506.929688   299936368
    20 2019-07-30   9506.929688   9749.530273   9391.780273   9595.519531   9595.519531   276402322
    21 2019-07-31   9595.519531  10123.940430   9581.599609  10089.250000  10089.250000   416343142
    22 2019-08-01  10089.250000  10488.809570   9890.490234  10409.790039  10409.790039   442037342
    23 2019-08-02  10409.790039  10666.639648  10340.820313  10528.990234  10528.990234   463688251
    24 2019-08-03  10528.990234  10915.000000  10509.349609  10820.410156  10820.410156   367536516
    25 2019-08-04  10820.410156  11074.950195  10572.240234  10978.910156  10978.910156   431699306
    26 2019-08-05  10978.910156  11945.379883  10978.889648  11807.959961  11807.959961   870917186
    27 2019-08-06  11807.959961  12316.849609  11224.099609  11467.099609  11467.099609   949534020
    28 2019-08-07  11467.099609  12138.549805  11393.980469  11974.280273  11974.280273   834719365
    29 2019-08-08  11974.280273  12042.870117  11498.040039  11982.799805  11982.799805   588463519
    30 2019-08-09  11983.620117  12027.570313  11674.059570  11810.679688  11810.679688   366160288

Installation
------------
Simply

.. code-block:: bash

    $ pip install wallstreet


Stock Attributes
----------------

- ticker
- price
- id
- exchange
- last_trade
- change   (change in currency)
- cp   (percentage change)


Option Attributes and Methods
-----------------------------

- strike
- expiration
- underlying  (underlying stock object)
- ticker
- bid
- ask
- price (option price)
- id
- exchange
- change  (in currency)
- cp  (percentage change)
- volume
- open_interest
- code
- expirations (list of possible expiration dates for option chain)
- strikes (list of possible strike prices)

- set_strike()
- implied_volatility()
- delta()
- gamma()
- vega()
- theta()
- rho()

### Core Implementation Code & Architecture
#### File: `wallstreet/__init__.py`
```python
from wallstreet.wallstreet import Stock, Call, Put

__all__ = ['Stock', 'Call', 'Put']

__version__ = "0.4.0"
```

#### File: `tests/mockrequests/mockrequests/__init__.py`
```python
from .mockrequests import get, post, Request, save, Session

__all__ = ['get', 'post', 'Request', 'save', 'Session']
```

#### File: `pyproject.toml`
```python
[tool.poetry]
name = "wallstreet"
version = "0.4.0"
description = "Stock and Option tools"
authors = ["Mike Dallas <mcdallas@protonmail.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.31"
scipy = "^1.12"
yfinance = "^0.2.37"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

#### File: `wallstreet/constants.py`
```python
DATE_FORMAT = '%d-%m-%Y'
DATETIME_FORMAT = '%d %b %Y %H:%M:%S'

TREASURY_URL = "https://home.treasury.gov/sites/default/files/interest-rates/yield.xml"
DELTA_DIFFERENTIAL = 1.e-3
VEGA_DIFFERENTIAL = 1.e-4
GAMMA_DIFFERENTIAL = 1.e-3
RHO_DIFFERENTIAL = 1.e-4
THETA_DIFFERENTIAL = 1.e-5

IMPLIED_VOLATILITY_TOLERANCE = 1.e-6
SOLVER_STARTING_VALUE = 0.27

OVERNIGHT_RATE = 0
FALLBACK_RISK_FREE_RATE = 0.02
```

#### File: `tests/mockrequests/response/GET/map.json`
```python
{"response1.p": ["http://finance.google.com/finance/info?client=ig&q=GOOG", null, false], "response2.p": ["https://query2.finance.yahoo.com/v7/finance/options/GOOG", null, false], "response3.p": ["http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield", null, false], "response4.p": ["https://www.google.com/finance/option_chain?q=GOOG&expd=16&expm=6&expy=2017&output=json", null, false], "response5.p": ["https://query2.finance.yahoo.com/v7/finance/options/GOOG?date=1497571200", null, false], "response6.p": ["https://www.google.com/finance/option_chain?q=GOOG&expd=15&expm=6&expy=2017&output=json", null, false]}
```

#### File: `tests/test_stock.py`
```python
import unittest
from wallstreet import wallstreet
from tests.mockrequests import mockrequests


class StockTest(unittest.TestCase):
    def setUp(self):
        self.oldrequests = wallstreet.requests
        wallstreet.requests = mockrequests

    def test_price(self):
        s = wallstreet.Stock('GOOG')
        self.assertEqual(s.price, 834.34)

    def test_last_trade(self):
        s = wallstreet.Stock('GOOG')
        self.assertEqual(s.last_trade, '22 Mar 2017 11:38:12')

    def test_yahoo_price(self):
        s = wallstreet.Stock('GOOG', source='yahoo')
        self.assertEqual(s.price, 833.65)

    def test_yahoo_last_trade(self):
        s = wallstreet.Stock('GOOG', source='yahoo')
        self.assertEqual(s.last_trade, '22 Mar 2017 15:53:24')

    def tearDown(self):
        wallstreet.requests = self.oldrequests
```


==================================================
