# ⚡ [QUANT-SOURCE-081] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_081_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: polars (`WHEEL_polars`)
- **Full Name**: `polars`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<h1 align="center">
  <a href="https://pola.rs">
    <img src="https://raw.githubusercontent.com/pola-rs/polars-static/master/banner/polars_github_banner.svg" alt="Polars logo">
  </a>
</h1>

<div align="center">
  <a href="https://crates.io/crates/polars">
    <img src="https://img.shields.io/crates/v/polars.svg" alt="crates.io Latest Release"/>
  </a>
  <a href="https://pypi.org/project/polars/">
    <img src="https://img.shields.io/pypi/v/polars.svg" alt="PyPi Latest Release"/>
  </a>
  <a href="https://www.npmjs.com/package/nodejs-polars">
    <img src="https://img.shields.io/npm/v/nodejs-polars.svg" alt="NPM Latest Release"/>
  </a>
  <a href="https://community.r-multiverse.org/polars">
    <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcommunity.r-multiverse.org%2Fapi%2Fpackages%2Fpolars&query=%24.Version&label=r-multiverse" alt="R-multiverse Latest Release"/>
  </a>
  <a href="https://doi.org/10.5281/zenodo.7697217">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.7697217.svg" alt="DOI Latest Release"/>
  </a>
</div>

<p align="center">
  <b>Documentation</b>:
  <a href="https://docs.pola.rs/api/python/stable/reference/index.html">Python</a>
  -
  <a href="https://docs.rs/polars/latest/polars/">Rust</a>
  -
  <a href="https://pola-rs.github.io/nodejs-polars/index.html">Node.js</a>
  -
  <a href="https://pola-rs.github.io/r-polars/index.html">R</a>
  |
  <b>Agents</b>:
  <a href="https://github.com/polars-inc/skills/tree/main/polars">Skill</a>
  -
  <a href="https://docs.pola.rs/user-guide/misc/polars_llms/">MCP</a>
  |
  <a href="https://docs.pola.rs/">User guide</a>
  |
  <a href="https://discord.gg/4UfP5cfBE7">Discord</a>
</p>

## Polars: Extremely fast Query Engine for DataFrames

Polars is an analytical query engine for DataFrames, written in Rust. It is designed to be fast,
easy to use and expressive. Key features are:

- **Fast**: written from the ground up in Rust with multi-threaded, vectorized (SIMD) execution
- **Lazy & eager execution**: with query optimization out of the box
- **Larger-than-RAM**: the streaming engine processes datasets that don't fit in memory
- **Expressive API**: compose complex queries with powerful expressions
- **Extensible**: extend Polars natively with custom code through
  [I/O and Expression plugins](https://docs.pola.rs/user-guide/plugins/)
- **Multi-language**: bindings for Python, Rust, Node.js, R, and SQL
- **GPU support**: optionally accelerate queries on NVIDIA GPUs
- **Interoperable**: uses the
  [Apache Arrow Columnar Format](https://arrow.apache.org/docs/format/Columnar.html) for zero-copy
  data sharing

To learn more, read the [user guide](https://docs.pola.rs/).

## Polars in action

Queries are composed from expressions. This lazy query gets optimized out of the box and runs in
parallel across all available cores:

```python
import polars as pl

df = (
    pl.scan_parquet("orders.parquet")
    .filter(pl.col("status") == "shipped")
    .group_by("customer_id")
    .agg(
        pl.col("amount").sum().alias("total"),
        pl.len().alias("n_orders"),
    )
    .sort("total", descending=True)
    .collect()
)
```

## Performance

Polars is very fast. In fact, it is one of the best performing Dataframe solutions available. See
the [PDS-H benchmarks](https://www.pola.rs/benchmarks.html) results.

### Handles larger-than-RAM data

If you have data that does not fit into memory, Polars' query engine is able to process your query
(or parts of your query) in a streaming fashion. This drastically reduces memory requirements, so
you might be able to process your 250GB dataset on your laptop. Collect with
`collect(engine='streaming')` to run the query streaming.

## Installation

### Python

Install the latest Polars version with:

```sh
pip install polars
```

See the [User Guide](https://docs.pola.rs/user-guide/installation/#feature-flags) for more details
on optional dependencies

<details>
<summary><b>Compile Polars from source</b></summary>

If you want a bleeding edge release you should compile Polars from source. Advanced users can also
compile for maximum performance for their architecture.

This can be done by going through the following steps in sequence:

1. Install the latest [Rust compiler](https://www.rust-lang.org/tools/install)
2. Install [maturin](https://maturin.rs/): `pip install maturin`
3. `cd py-polars` and choose one of the following:
   - `make build`, slow binary with debug assertions and limited symbols, fast compile times
   - `make build-debug`, same as `make build`, but with all symbols, produces large binaries
   - `make build-release`, fast binary without debug assertions, minimal debug symbols, long compile
     times
   - `make build-nodebug-release`, same as build-release but without any debug symbols, slightly
     faster to compile
   - `make build-debug-release`, same as build-release but with full debug symbols, slightly slower
     to compile
   - `make build-dist-release`, fastest binary, extreme compile times

By default the binary is compiled with optimizations turned on for a modern CPU. Specify `LTS_CPU=1`
with the command if your CPU is older and does not support e.g. AVX2.

Note that the Rust crate implementing the Python bindings is called `py-polars` to distinguish from
the wrapped Rust crate `polars` itself. However, both the Python package and the Python module are
named `polars`, so you can `pip install polars` and `import polars`.

</details>

Check the [Installation guide](https://docs.pola.rs/user-guide/installation/) for more advanced
installations. For example when you expect more than 2^32 (~4.2 billion) rows, run on an old CPU
(e.g. dating from before 2011), or on an `x86-64` build of Python on Apple Silicon under Rosetta.

## Contributing

Want to contribute? Read our [contributing guide](https://docs.pola.rs/development/contributing/)
and check the issue tracker for accepted issues.

Contributors new to the codebase can look for the `good first issue` label to get familiar with the
project.

You can [join the Polars Discord server](https://discord.gg/4UfP5cfBE7) for any help along the way.

## Distributed Polars

Running into hardware limitations executing your queries? Read how you can
[horizontally scale your Polars query on a cluster](https://docs.pola.rs/polars-cloud/).

## License

Polars is licensed under the [MIT License](LICENSE) (SPDX: `MIT`).

### Core Implementation Code & Architecture
#### File: `py-polars/src/polars/catalog/__init__.py`
```python

```

#### File: `py-polars/src/polars/ml/__init__.py`
```python

```

#### File: `pyo3-polars/example/derive_expression/expression_lib/expression_lib/__init__.py`
```python

```

#### File: `crates/polars/tests/it/lazy/schema.rs`
```python

```

#### File: `crates/polars/tests/it/arrow/io/mod.rs`
```python
mod ipc;
```

#### File: `crates/polars/tests/it/arrow/compute/aggregate/mod.rs`
```python
mod memory;
```


==================================================


## [2/3] Repository: pyfolio (`WHEEL_pyfolio`)
- **Full Name**: `pyfolio`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
![pyfolio](https://media.quantopian.com/logos/open_source/pyfolio-logo-03.png "pyfolio")

# pyfolio

[![Join the chat at https://gitter.im/quantopian/pyfolio](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/quantopian/pyfolio?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![build status](https://travis-ci.org/quantopian/pyfolio.png?branch=master)](https://travis-ci.org/quantopian/pyfolio)

pyfolio is a Python library for performance and risk analysis of
financial portfolios developed by
[Quantopian Inc](https://www.quantopian.com). It works well with the
[Zipline](https://www.zipline.io/) open source backtesting library.
Quantopian also offers a [fully managed service for professionals](https://factset.quantopian.com) 
that includes Zipline, Alphalens, Pyfolio, FactSet data, and more.

At the core of pyfolio is a so-called tear sheet that consists of
various individual plots that provide a comprehensive image of the
performance of a trading algorithm. Here's an example of a simple tear
sheet analyzing a strategy:

![simple tear 0](https://github.com/quantopian/pyfolio/raw/master/docs/simple_tear_0.png "Example tear sheet created from a Zipline algo")
![simple tear 1](https://github.com/quantopian/pyfolio/raw/master/docs/simple_tear_1.png "Example tear sheet created from a Zipline algo")

Also see [slides of a talk about
pyfolio](https://nbviewer.jupyter.org/format/slides/github/quantopian/pyfolio/blob/master/pyfolio/examples/pyfolio_talk_slides.ipynb#/).

## Installation

To install pyfolio, run:

```bash
pip install pyfolio
```

#### Development

For development, you may want to use a [virtual environment](https://docs.python-guide.org/en/latest/dev/virtualenvs/) to avoid dependency conflicts between pyfolio and other Python projects you have. To get set up with a virtual env, run:
```bash
mkvirtualenv pyfolio
```

Next, clone this git repository and run `python setup.py develop`
and edit the library files directly.

#### Matplotlib on OSX

If you are on OSX and using a non-framework build of Python, you may need to set your backend:
``` bash
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```

## Usage

A good way to get started is to run the pyfolio examples in
a [Jupyter notebook](https://jupyter.org/). To do this, you first want to
start a Jupyter notebook server:

```bash
jupyter notebook
```

From the notebook list page, navigate to the pyfolio examples directory
and open a notebook. Execute the code in a notebook cell by clicking on it
and hitting Shift+Enter.


## Questions?

If you find a bug, feel free to [open an issue](https://github.com/quantopian/pyfolio/issues) in this repository.

You can also join our [mailing list](https://groups.google.com/forum/#!forum/pyfolio) or
our [Gitter channel](https://gitter.im/quantopian/pyfolio).

## Support

Please [open an issue](https://github.com/quantopian/pyfolio/issues/new) for support.

## Contributing

If you'd like to contribute, a great place to look is the [issues marked with help-wanted](https://github.com/quantopian/pyfolio/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).

For a list of core developers and outside collaborators, see [the GitHub contributors list](https://github.com/quantopian/pyfolio/graphs/contributors).

### Core Implementation Code & Architecture
#### File: `pyfolio/tests/__init__.py`
```python

```

#### File: `pyfolio/_seaborn.py`
```python
"""Wrapper module around seaborn to suppress warnings on import.

This should be removed when seaborn stops raising:

UserWarning: axes.color_cycle is deprecated and replaced with axes.prop_cycle;
please use the latter.
"""
import warnings


with warnings.catch_warnings():
    warnings.filterwarnings(
        'ignore',
        'axes.color_cycle is deprecated',
        UserWarning,
        'matplotlib',
    )
    from seaborn import *  # noqa
```

#### File: `pyfolio/__init__.py`
```python
from . import utils
from . import timeseries
from . import pos
from . import txn
from . import interesting_periods
from . import capacity
from . import round_trips
from . import perf_attrib

from .tears import *  # noqa
from .plotting import *  # noqa
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

__all__ = ['utils', 'timeseries', 'pos', 'txn',
           'interesting_periods', 'capacity', 'round_trips',
           'perf_attrib']
```

#### File: `pyfolio/ipycompat.py`
```python
import IPython

IPY_MAJOR = IPython.version_info[0]
if IPY_MAJOR < 3:
    raise ImportError("IPython version %d is not supported." % IPY_MAJOR)

IPY3 = (IPY_MAJOR == 3)

# IPython underwent a major refactor between versions 3 and 4.  Many of the
# imports in version 4 have aliases to their old locations in 3, but they raise
# noisy deprecation warnings.  By conditionally importing here, we can support
# older versions without triggering warnings for users on new versions.
if IPY3:
    from IPython.nbformat import read
else:
    from nbformat import read


__all__ = ['read']
```

#### File: `pyfolio/tests/test_nbs.py`
```python
#!/usr/bin/env python
"""
simple example script for running notebooks and reporting exceptions.
Usage: `checkipnb.py foo.ipynb [bar.ipynb [...]]`
Each cell is submitted to the kernel, and checked for errors.
"""

import os
import glob
from runipy.notebook_runner import NotebookRunner

from pyfolio.utils import pyfolio_root
from pyfolio.ipycompat import read as read_notebook


def test_nbs():
    path = os.path.join(pyfolio_root(), 'examples', '*.ipynb')
    for ipynb in glob.glob(path):
        with open(ipynb) as f:
            nb = read_notebook(f, 'json')
            nb_runner = NotebookRunner(nb)
            nb_runner.run_notebook(skip_exceptions=False)
```

#### File: `pyfolio/deprecate.py`
```python
"""Utilities for marking deprecated functions."""
# Copyright 2018 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings
from functools import wraps


def deprecated(msg=None, stacklevel=2):
    """
    Used to mark a function as deprecated.
    Parameters
    ----------
    msg : str
        The message to display in the deprecation warning.
    stacklevel : int
        How far up the stack the warning needs to go, before
        showing the relevant calling lines.
    Usage
    -----
    @deprecated(msg='function_a is deprecated! Use function_b instead.')
    def function_a(*args, **kwargs):
    """
    def deprecated_dec(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            warnings.warn(
                msg or "Function %s is deprecated." % fn.__name__,
                category=DeprecationWarning,
                stacklevel=stacklevel
            )
            return fn(*args, **kwargs)
        return wrapper
    return deprecated_dec
```


==================================================


## [3/3] Repository: pyfolio-reloaded (`WHEEL_pyfolio-reloaded`)
- **Full Name**: `pyfolio-reloaded`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
<a href="https://pyfolio.ml4trading.io">
<img src="https://i.imgur.com/GD6TZ0D.png" width="35%">
</a>
</p>

![PyPI](https://img.shields.io/pypi/v/pyfolio-reloaded)
[![Tests](https://github.com/stefan-jansen/pyfolio-reloaded/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/stefan-jansen/pyfolio-reloaded/actions/workflows/unit_tests.yml)
[![conda](https://github.com/stefan-jansen/pyfolio-reloaded/actions/workflows/conda_package.yml/badge.svg)](https://github.com/stefan-jansen/pyfolio-reloaded/actions/workflows/conda_package.yml)
[![PyPI](https://github.com/stefan-jansen/pyfolio-reloaded/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/stefan-jansen/pyfolio-reloaded/actions/workflows/build_wheels.yml)
[![Coverage Status](https://coveralls.io/repos/github/stefan-jansen/pyfolio-reloaded/badge.svg?branch=main)](https://coveralls.io/github/stefan-jansen/pyfolio-reloaded?branch=main)
![GitHub issues](https://img.shields.io/github/issues/stefan-jansen/pyfolio-reloaded)
![Discourse users](https://img.shields.io/discourse/users?server=https%3A%2F%2Fexchange.ml4trading.io%2F)
![Twitter Follow](https://img.shields.io/twitter/follow/ml4trading?style=social)

pyfolio is a Python library for performance and risk analysis of financial portfolios that works well with the [Zipline](https://zipline.ml4trading.io/) open source backtesting library.

## Trading Strategy Analysis with pyfolio

At the core of pyfolio are various tear sheets that combine various individual plots and summary statistics to
provide a comprehensive view of the performance of a trading algorithm.

Here's an example of a simple tear sheet analyzing a strategy executed with the Zipline backtesting engine:

### Performance Metrics

The tear sheet presents performance and risk metrics for the strategy separately during the backtest and out-of-sample periods:

<p align="center">
<a href="#">
<img src="https://i.imgur.com/bfwMeIV.png" width="50%">
</a>
</p>

### Performance Plots

In addition, it visualizes how several risk and return metrics behave over time:

<p align="center">
<a href="#">
<img src="https://i.imgur.com/5Hyuet3.png" width="85%">
</a>
</p>

## Installation

To install pyfolio, run:

```bash
pip install pyfolio-reloaded
```
or

```bash
conda install -c ml4t pyfolio-reloaded
```

#### Development

For development, you may want to use a [virtual environment](https://docs.python-guide.org/en/latest/dev/virtualenvs/) to avoid dependency conflicts between pyfolio and other Python projects you have.

To get set up with a virtual env, run:
```bash
mkvirtualenv pyfolio
```

Next, clone this git repository and run `python -m pip install .[all]` and edit the library files directly.

## Usage

A good way to get started is to run the pyfolio examples in a
[Jupyter notebook](https://jupyter.org/). To do this, you first want to
start a Jupyter notebook server:

```bash
jupyter notebook
```

From the notebook list page, navigate to the pyfolio examples directory
and open a notebook. Execute the code in a notebook cell by clicking on it
and hitting Shift+Enter.


## Questions?

If you find a bug, feel free to [open an issue](https://github.com/stefan-jansen/pyfolio-reloaded/issues) in this repository.

You can also join our [community](https://exchange.ml4trading.io).

## Support

Please [open an issue](https://github.com/stefan-jansen/pyfolio-reloaded/issues/new) for support.

## Contributing

If you'd like to contribute, a great place to look is the [issues marked with help-wanted](https://github.com/stefan-jansen/pyfolio-reloaded/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).

For a list of core developers and outside collaborators, see [the GitHub contributors list](https://github.com/stefan-jansen/pyfolio-reloaded/graphs/contributors).

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `src/pyfolio/ipycompat.py`
```python
import IPython

IPY_MAJOR = IPython.version_info[0]
if IPY_MAJOR < 3:
    raise ImportError("IPython version %d is not supported." % IPY_MAJOR)

IPY3 = IPY_MAJOR == 3

# IPython underwent a major refactor between versions 3 and 4.  Many of the
# imports in version 4 have aliases to their old locations in 3, but they raise
# noisy deprecation warnings.  By conditionally importing here, we can support
# older versions without triggering warnings for users on new versions.
if IPY3:
    from IPython.nbformat import read
else:
    from nbformat import read


__all__ = ["read"]
```

#### File: `src/pyfolio/__init__.py`
```python
from . import capacity
from . import interesting_periods
from . import perf_attrib
from . import pos
from . import round_trips
from . import timeseries
from . import txn
from . import utils
from .plotting import *  # noqa
from .tears import *  # noqa

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")

__all__ = [
    "utils",
    "timeseries",
    "pos",
    "txn",
    "interesting_periods",
    "capacity",
    "round_trips",
    "perf_attrib",
]
```

#### File: `src/pyfolio/deprecate.py`
```python
"""Utilities for marking deprecated functions."""
# Copyright 2018 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings
from functools import wraps


def deprecated(msg=None, stacklevel=2):
    """
    Used to mark a function as deprecated.
    Parameters
    ----------
    msg : str
        The message to display in the deprecation warning.
    stacklevel : int
        How far up the stack the warning needs to go, before
        showing the relevant calling lines.
    Usage
    -----
    @deprecated(msg='function_a is deprecated! Use function_b instead.')
    def function_a(*args, **kwargs):
    """

    def deprecated_dec(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            warnings.warn(
                msg or "Function %s is deprecated." % fn.__name__,
                category=DeprecationWarning,
                stacklevel=stacklevel,
            )
            return fn(*args, **kwargs)

        return wrapper

    return deprecated_dec
```

#### File: `docs/source/conf.py`
```python
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import pydata_sphinx_theme
from pyfolio import __version__ as version

sys.path.insert(0, Path("../..").resolve(strict=True).as_posix())

extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "m2r2",
    "sphinx_markdown_tables",
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
]

templates_path = ["_templates"]

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

master_doc = "index"

project = "pyfolio"
copyright = "2016, Quantopian, Inc."
author = "Quantopian, Inc."

release = version
language = None

exclude_patterns = []

highlight_language = "python"

pygments_style = "sphinx"

todo_include_todos = False

html_theme = "pydata_sphinx_theme"
html_theme_path = pydata_sphinx_theme.get_html_theme_path()

html_theme_options = {
    "github_url": "https://github.com/stefan-jansen/pyfolio-reloaded",
    "twitter_url": "https://twitter.com/ml4trading",
    "external_links": [
        {"name": "ML for Trading", "url": "https://ml4trading.io"},
        {"name": "Community", "url": "https://exchange.ml4trading.io"},
    ],
    "google_analytics_id": "UA-74956955-3",
    "use_edit_page_button": True,
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "assets/favicon16x16.ico",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "assets/favicon32x32.ico",
        },
    ],
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "stefan-jansen",
    "github_repo": "pyfolio-reloaded",
    "github_version": "main",
    "doc_path": "docs/source",
}

html_static_path = []

htmlhelp_basename = "Pyfoliodoc"

latex_elements = {}

latex_documents = [
    (
        master_doc,
        "Pyfolio.tex",
        "Pyfolio Documentation",
        "Quantopian, Inc.",
        "manual",
    )
]

man_pages = [(master_doc, "pyfolio", "Pyfolio Documentation", [author], 1)]

texinfo_documents = [
    (
        master_doc,
        "Pyfolio",
        "Pyfolio Documentation",
        author,
        "Pyfolio",
        "One line description of project.",
        "Miscellaneous",
    )
]
```

#### File: `docs/deploy.py`
```python
#!/usr/bin/env python
from __future__ import print_function
from contextlib import contextmanager
from glob import glob
import os
from os.path import basename, exists, isfile
from pathlib import Path
from shutil import move, rmtree
from subprocess import check_call

HERE = Path(__file__).resolve(strict=True).parent
PYFOLIO_ROOT = HERE.parent
TEMP_LOCATION = "/tmp/pyfolio-doc"
TEMP_LOCATION_GLOB = TEMP_LOCATION + "/*"


@contextmanager
def removing(path):
    try:
        yield
    finally:
        rmtree(path)


def ensure_not_exists(path):
    if not exists(path):
        return
    if isfile(path):
        os.unlink(path)
    else:
        rmtree(path)


def main():
    old_dir = Path.cwd()
    print("Moving to %s." % HERE)
    os.chdir(HERE)

    try:
        print("Cleaning docs with 'make clean'")
        check_call(["make", "clean"])
        print("Building docs with 'make html'")
        check_call(["make", "html"])

        print("Clearing temp location '%s'" % TEMP_LOCATION)
        rmtree(TEMP_LOCATION, ignore_errors=True)

        with removing(TEMP_LOCATION):
            print("Copying built files to temp location.")
            move("build/html", TEMP_LOCATION)

            print("Moving to '%s'" % PYFOLIO_ROOT)
            os.chdir(PYFOLIO_ROOT)

            print("Checking out gh-pages branch.")
            check_call(
                [
                    "git",
                    "branch",
                    "-f",
                    "--track",
                    "gh-pages",
                    "origin/gh-pages",
                ]
            )
            check_call(["git", "checkout", "gh-pages"])
            check_call(["git", "reset", "--hard", "origin/gh-pages"])

            print("Copying built files:")
            for file_ in glob(TEMP_LOCATION_GLOB):
                base = basename(file_)

                print("%s -> %s" % (file_, base))
                ensure_not_exists(base)
                move(file_, ".")
    finally:
        os.chdir(old_dir)

    print()
    print("Updated documentation branch in directory %s" % PYFOLIO_ROOT)
    print("If you are happy with these changes, commit and push to gh-pages.")


if __name__ == "__main__":
    main()
```


==================================================
