# ⚡ [QUANT-SOURCE-084] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_084_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: simdjson (`WHEEL_simdjson`)
- **Full Name**: `simdjson`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
[![][license img]][license] [![][licensemit img]][licensemit]


[![Doxygen Documentation](https://img.shields.io/badge/docs-doxygen-green.svg)](https://simdjson.github.io/simdjson/)

simdjson : Parsing gigabytes of JSON per second
===============================================

<img src="images/official_logo/logo_noir/SVG/logo_simdjson_noir.svg" width="40%" style="float: right">

JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it. We need a fresh
approach. The simdjson library uses commonly available SIMD instructions and microparallel algorithms
to parse JSON 4x  faster than RapidJSON and 25x faster than JSON for Modern C++.

* **Fast:** Over 4x faster than commonly used production-grade JSON parsers.
* **Record Breaking Features:** Minify JSON  at 6 GB/s, validate UTF-8  at 13 GB/s,  NDJSON at 3.5 GB/s.
* **Easy:** First-class, easy to use and carefully documented APIs.
* **Strict:** Full JSON and UTF-8 validation, lossless parsing. Performance with no compromises.
* **Automatic:** Selects a CPU-tailored parser at runtime. No configuration needed.
* **Reliable:** From memory allocation to error handling, simdjson's design avoids surprises.
* **Peer Reviewed:** Our research appears in venues like VLDB Journal, Software: Practice and Experience.

This library is part of the [Awesome Modern C++](https://awesomecpp.com) list.

Table of Contents
-----------------

* [Real-world usage](#real-world-usage)
* [Quick Start](#quick-start)
* [Documentation](#documentation)
* [Godbolt](#godbolt)
* [Performance results](#performance-results)
* [Packages](#packages)
* [Bindings and Ports of simdjson](#bindings-and-ports-of-simdjson)
* [About simdjson](#about-simdjson)
* [Funding](#funding)
* [Contributing to simdjson](#contributing-to-simdjson)
* [License](#license)


Real-world usage
----------------

- [Node.js](https://nodejs.org/)
- [ClickHouse](https://github.com/ClickHouse/ClickHouse)
- [Meta Velox](https://velox-lib.io)
- [Google Pax](https://github.com/google/paxml)
- [milvus](https://github.com/milvus-io/milvus)
- [QuestDB](https://questdb.io/blog/questdb-release-8-0-3/)
- [Clang Build Analyzer](https://github.com/aras-p/ClangBuildAnalyzer)
- [Shopify HeapProfiler](https://github.com/Shopify/heap-profiler)
- [StarRocks](https://github.com/StarRocks/starrocks)
- [Microsoft FishStore](https://github.com/microsoft/FishStore)
- [Intel PCM](https://github.com/intel/pcm)
- [WatermelonDB](https://github.com/Nozbe/WatermelonDB)
- [Apache Doris](https://github.com/apache/doris)
- [Dgraph](https://github.com/dgraph-io/dgraph)
- [UCall](https://github.com/unum-cloud/UCall)
- [fastgltf](https://github.com/spnda/fastgltf)
- [tenzir](https://github.com/tenzir/tenzir)
- [ada-url](https://github.com/ada-url/ada)
- [fastgron](https://github.com/adamritter/fastgron)
- [WasmEdge](https://wasmedge.org)
- [RonDB](https://github.com/logicalclocks/rondb)
- [GreptimeDB](https://github.com/GreptimeTeam/greptimedb)
- [mamba](https://github.com/mamba-org/mamba)
- [Ladybird Browser](https://ladybird.org)
- [SereneDB](https://github.com/serenedb/serenedb)


If you are planning to use simdjson in a product, please work from one of our releases.




Quick Start
-----------

The simdjson library is easily consumable with a single .h and .cpp file.

0. Prerequisites: `g++` (version 7 or better) or `clang++` (version 6 or better), and a 64-bit
   system with a command-line shell (e.g., Linux, macOS, freeBSD). We also support programming
   environments like Visual Studio and Xcode, but different steps are needed. Users of clang++ may need to specify the C++ version (e.g., `c++ -std=c++17`) since clang++ tends to default on C++98.
1. Pull [simdjson.h](singleheader/simdjson.h) and [simdjson.cpp](singleheader/simdjson.cpp) into a
   directory, along with the sample file [twitter.json](jsonexamples/twitter.json). You can download them with the `wget` utility:

   ```
   wget https://raw.githubusercontent.com/simdjson/simdjson/master/singleheader/simdjson.h https://raw.githubusercontent.com/simdjson/simdjson/master/singleheader/simdjson.cpp https://raw.githubusercontent.com/simdjson/simdjson/master/jsonexamples/twitter.json
   ```
2. Create `quickstart.cpp`:

```cpp
#include <iostream>
#include "simdjson.h"
using namespace simdjson;
int main(void) {
    ondemand::parser parser;
    padded_string json = padded_string::load("twitter.json");
    ondemand::document tweets = parser.iterate(json);
    std::cout << uint64_t(tweets["search_metadata"]["count"]) << " results." << std::endl;
}
```
3. `c++ -o quickstart quickstart.cpp simdjson.cpp`
4. `./quickstart`

  ```
   100 results.
  ```


Documentation
-------------

Usage documentation is available:

* [Basics](doc/basics.md) is an overview of how to use simdjson and its APIs.
* [Builder](doc/builder.md) is an overview of how to efficiently write JSON strings using simdjson.
* [Performance](doc/performance.md) shows some more advanced scenarios and how to tune for them.
* [Implementation Selection](doc/implementation-selection.md) describes runtime CPU detection and
  how you can work with it.
* [API](https://simdjson.github.io/simdjson/) contains the automatically generated API documentation.
* [Compile-Time Parsing](doc/compile_time.md) presents our compile-time parsing function (C++26 only).


Godbolt
-------------

Some users may want to browse code along with the compiled assembly. You want to check out the following lists of examples:
* [C++26 reflection example](https://godbolt.org/z/K3Px64TqK)
* [simdjson examples with errors handled through exceptions](https://godbolt.org/z/7G5qE4sr9)
* [simdjson examples with errors without exceptions](https://godbolt.org/z/e9dWb9E4v)

Performance results
-------------------

The simdjson library uses three-quarters less instructions than state-of-the-art parser [RapidJSON](https://rapidjson.org). To our knowledge, simdjson is the first fully-validating JSON parser
to run at [gigabytes per second](https://en.wikipedia.org/wiki/Gigabyte) (GB/s) on commodity processors. It can parse millions of JSON documents per second on a single core.

The following figure represents parsing speed in GB/s for parsing various files
on an Intel Skylake processor (3.4 GHz) using the GNU GCC 10 compiler (with the -O3 flag).
We compare against the best and fastest C++ libraries on benchmarks that load and process the data.
The simdjson library offers full unicode ([UTF-8](https://en.wikipedia.org/wiki/UTF-8)) validation and exact
number parsing.

<img src="doc/rome.png" width="60%">

The simdjson library offers high speed whether it processes tiny files (e.g., 300 bytes)
or larger files (e.g., 3MB). The following plot presents parsing
speed for [synthetic files over various sizes generated with a script](https://github.com/simdjson/simdjson_experiments_vldb2019/blob/master/experiments/growing/gen.py) on a 3.4 GHz Skylake processor (GNU GCC 9, -O3).

<img src="doc/growing.png" width="60%">

[All our experiments are reproducible](https://github.com/simdjson/simdjson_experiments_vldb2019).


For NDJSON files, we can exceed 3 GB/s with [our  multithreaded parsing functions](https://github.com/simdjson/simdjson/blob/master/doc/parse_many.md).


Packages
------------------------------
[![Packaging status](https://repology.org/badge/vertical-allrepos/simdjson.svg)](https://repology.org/project/simdjson/versions)


Bindings and Ports of simdjson
------------------------------

We distinguish between "bindings" (which just wrap the C++ code) and a port to another programming language (which reimplements everything).

- [ZippyJSON](https://github.com/michaeleisel/zippyjson): Swift bindings for the simdjson project.
- [libpy_simdjson](https://github.com/gerrymanoim/libpy_simdjson/): high-speed Python bindings for simdjson using [libpy](https://github.com/quantopian/libpy).
- [pysimdjson](https://github.com/TkTech/pysimdjson): Python bindings for the simdjson project.
- [cysimdjson](https://github.com/TeskaLabs/cysimdjson): high-speed Python bindings for the simdjson project.
- [simdjson-rs](https://github.com/simd-lite): Rust port.
- [simdjson-rust](https://github.com/SunDoge/simdjson-rust): Rust wrapper (bindings).
- [SimdJsonSharp](https://github.com/EgorBo/SimdJsonSharp): C# version for .NET Core (bindings and full port).
- [simdjson_nodejs](https://github.com/luizperes/simdjson_nodejs): Node.js bindings for the simdjson project.
- [simdjson_php](https://github.com/crazyxman/simdjson_php): PHP bindings for the simdjson project.
- [simdjson_ruby](https://github.com/saka1/simdjson_ruby): Ruby bindings for the simdjson project.
- [fast_jsonparser](https://github.com/anilmaurya/fast_jsonparser): Ruby bindings for the simdjson project.
- [simdjson-go](https://github.com/minio/simdjson-go): Go port using Golang assembly.
- [rcppsimdjson](https://github.com/eddelbuettel/rcppsimdjson): R bindings.
- [simdjson_erlang](https://github.com/ChomperT/simdjson_erlang): erlang bindings.
- [simdjsone](https://github.com/saleyn/simdjsone): erlang bindings.
- [lua-simdjson](https://github.com/FourierTransformer/lua-simdjson): lua bindings.
- [hermes-json](https://hackage.haskell.org/package/hermes-json): haskell bindings.
- [zimdjson](https://github.com/EzequielRamis/zimdjson): Zig port.
- [simdjzon](https://github.com/travisstaloch/simdjzon): Zig port.
- [JSON-Simd](https://github.com/rawleyfowler/JSON-simd): Raku bindings.
- [JSON::SIMD](https://metacpan.org/pod/JSON::SIMD): Perl bindings; fully-featured JSON module that uses simdjson for decoding.
- [gemmaJSON](https://github.com/sainttttt/gemmaJSON): Nim JSON parser based on simdjson bindings.
- [simdjson-java](https://github.com/simdjson/simdjson-java): Java port.
- [mruby-fast-json](https://github.com/Asmod4n/mruby-fast-json): mruby binding with high API coverage.
- [simdjson-dart](https://github.com/xaldarof/simdjson-dart): Dart bindings for the simdjson project.

About simdjson
--------------

The simdjson library takes advantage of modern microarchitectures, parallelizing with SIMD vector
instructions, reducing branch misprediction, and reducing data dependency to take advantage of each
CPU's multiple execution cores.

Our default front-end is called On-Demand, and we wrote a paper about it:

- John Keiser, Daniel Lemire, [On-Demand JSON: A Better Way to Parse Documents?](https://arxiv.org/abs/2312.17149), Software: Practice and Experience 54 (6), 2024.

Some people [enjoy reading the first (2019) simdjson paper](https://arxiv.org/abs/1902.08318): A description of the design
and implementation of simdjson is in our research article:
- Geoff Langdale, Daniel Lemire, [Parsing Gigabytes of JSON per Second](https://arxiv.org/abs/1902.08318), VLDB Journal 28 (6), 2019.

We have an in-depth paper focused on the UTF-8 validation:

- John Keiser, Daniel Lemire, [Validating UTF-8 In Less Than One Instruction Per Byte](https://arxiv.org/abs/2010.03090), Software: Practice & Experience 51 (5), 2021.

We also have an informal [blog post providing some background and context](https://branchfree.org/2019/02/25/paper-parsing-gigabytes-of-json-per-second/).

For the video inclined, we had a talk at QCon San Francisco 2019<br />
[![simdjson at QCon San Francisco 2019](https://img.youtube.com/vi/wlvKAT7SZIQ/0.jpg)](https://www.youtube.com/watch?v=wlvKAT7SZIQ)<br />
(It was the best voted talk, we're kinda proud of it.)

We also had a CppCon 2025 talk. We show how C++26 reflection allows for one-line serialization (to_json(player)) or deserialization—without invasive macros or manual mapping—using nothing but the C++ standard library. Whether you’re a performance junkie or simply interested in the roadmap for the next decade of C++ development, watch our full talk!

[![simdjson at CppCon 2025](https://img.youtube.com/vi/Mcgk3CxHYMs/0.jpg)](https://www.youtube.com/watch?v=Mcgk3CxHYMs)<br />



Citing this work
-----------------

If you use simdjson in published research, please cite the software library. A suitable BibTeX entry is:

```bibtex
@misc{simdjson,
  title={{The simdjson library: Parsing Gigabytes of JSON per Second}},
  author={Daniel Lemire and Geoff Langdale and John Keiser and Paul Dreik and Francisco Thiesen and others},
  year={2019},
  howpublished={Software library},
  note={https://github.com/simdjson/simdjson}
}
```

Funding
-------

The work is supported by the Natural Sciences and Engineering Research Council of Canada under grants
RGPIN-2017-03910 and RGPIN-2024-03787.

[license]: LICENSE
[license img]: https://img.shields.io/badge/License-Apache%202-blue.svg


[licensemit]: LICENSE-MIT
[licensemit img]: https://img.shields.io/badge/License-MIT-blue.svg


Contributing to simdjson
------------------------

Head over to [CONTRIBUTING.md](CONTRIBUTING.md) for information on contributing to simdjson, and
[HACKING.md](HACKING.md) for information on source, building, and architecture/design.


License
-------

This code is made available under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html) as well as under the MIT License. As a user, you can pick the license you prefer.

Under Windows, we build some tools using the windows/dirent_portable.h file (which is outside our library code): it is under the liberal (business-friendly) MIT license.

For compilers that do not support [C++17](https://en.wikipedia.org/wiki/C%2B%2B17), we bundle the string-view library which is published under the [Boost license](https://www.boost.org/LICENSE_1_0.txt). Like the Apache license, the Boost license is a permissive license allowing commercial redistribution.

For efficient number serialization, we bundle Junekey Jeon's implementation of the Dragonbox algorithm for binary to decimal floating-point numbers (https://github.com/jk-jeon/dragonbox). The Dragonbox implementation is provided under the Apache License Version 2.0 with LLVM Exceptions (LICENSE-Apache2-LLVM or https://llvm.org/foundation/relicensing/LICENSE.txt) or the Boost Software License Version 1.0 (LICENSE-Boost or https://www.boost.org/LICENSE_1_0.txt).

For runtime dispatching, we use some code from the PyTorch project licensed under 3-clause BSD.

### Core Implementation Code & Architecture
#### File: `jsonexamples/example_config.json`
```python
{
  "app_name": "MyApp",
  "version": "1.0.0",
  "port": 8080,
  "debug": true,
  "features": ["logging", "caching"],
  "database": {
    "host": "localhost",
    "port": 5432
  }
}
```

#### File: `examples/quickstart/quickstart2.cpp`
```python
#include <iostream>
#include "simdjson.h"

int main(void) {
  simdjson::dom::parser parser;
  simdjson::dom::element tweets = parser.load("twitter.json");
  std::cout << "ID: " << tweets["statuses"].at(0)["id"] << std::endl;
}
```

#### File: `examples/quickstart/quickstart.cpp`
```python
#include <iostream>
#include "simdjson.h"

int main(void) {
  simdjson::dom::parser parser;
  simdjson::dom::element tweets = parser.load("twitter.json");
  std::cout << tweets["search_metadata"]["count"] << " results." << std::endl;
}
```

#### File: `benchmark/static_reflect/serde-benchmark/Cargo.toml`
```python
[package]
name = "serde-benchmark"
version = "0.1.0"

[lib]
path = "lib.rs"
crate-type = ["cdylib"]

[dependencies]
serde = { version = "1.0", features = ["derive"] }
libc = "0.2"
serde_json = "1.0"

[profile.release]
opt-level = 3
debug = false
lto = true
```

#### File: `fuzz/fuzz_parser.cpp`
```python
#include "simdjson.h"
#include <cstddef>
#include <cstdint>
#include <string>
extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
  simdjson::dom::parser parser;
  simdjson_unused simdjson::dom::element elem;
  simdjson_unused auto error = parser.parse(Data, Size).get(elem);
  return 0;
}
```

#### File: `examples/quickstart/quickstart_ondemand.cpp`
```python
#include <iostream>
#include "simdjson.h"
using namespace simdjson;
int main(void) {
    ondemand::parser parser;
    padded_string json = padded_string::load("twitter.json");
    ondemand::document tweets = parser.iterate(json);
    std::cout << uint64_t(tweets["search_metadata"]["count"]) << " results." << std::endl;
}
```


==================================================


## [2/3] Repository: statsmodels (`WHEEL_statsmodels`)
- **Full Name**: `statsmodels`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
![Statsmodels logo](docs/source/images/statsmodels-logo-v2-horizontal.svg)

[![PyPI
Version](https://img.shields.io/pypi/v/statsmodels.svg)](https://pypi.org/project/statsmodels/)
[![Conda
Version](https://anaconda.org/conda-forge/statsmodels/badges/version.svg)](https://anaconda.org/conda-forge/statsmodels/)
[![License](https://img.shields.io/pypi/l/statsmodels.svg)](https://github.com/statsmodels/statsmodels/blob/main/LICENSE.txt)
[![Azure CI Build
Status](https://dev.azure.com/statsmodels/statsmodels-testing/_apis/build/status/statsmodels.statsmodels?branchName=main)](https://dev.azure.com/statsmodels/statsmodels-testing/_build/latest?definitionId=1&branchName=main)
[![Codecov
Coverage](https://codecov.io/gh/statsmodels/statsmodels/branch/main/graph/badge.svg)](https://codecov.io/gh/statsmodels/statsmodels)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/statsmodels?label=PyPI%20Downloads)](https://pypi.org/project/statsmodels/)
[![Conda
downloads](https://img.shields.io/conda/dn/conda-forge/statsmodels.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/statsmodels/)

# About statsmodels

statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

# Documentation

The documentation for the latest release is at

<https://www.statsmodels.org/stable/>

The documentation for the development version is at

<https://www.statsmodels.org/dev/>

Recent improvements are highlighted in the release notes

<https://www.statsmodels.org/stable/release/>

Backups of documentation are available at
<https://statsmodels.github.io/stable/> and
<https://statsmodels.github.io/dev/>.

# Main Features

- Linear regression models:
  - Ordinary least squares
  - Generalized least squares
  - Weighted least squares
  - Least squares with autoregressive errors
  - Quantile regression
  - Recursive least squares
- Mixed Linear Model with mixed effects and variance components
- GLM: Generalized linear models with support for all of the
  one-parameter exponential family distributions
- Bayesian Mixed GLM for Binomial and Poisson
- GEE: Generalized Estimating Equations for one-way clustered or
  longitudinal data
- Discrete models:
  - Logit and Probit
  - Multinomial logit (MNLogit)
  - Poisson and Generalized Poisson regression
  - Negative Binomial regression
  - Zero-Inflated Count models
- RLM: Robust linear models with support for several M-estimators.
- Time Series Analysis: models for time series analysis
  - Complete StateSpace modeling framework
    - Seasonal ARIMA and ARIMAX models
    - VARMA and VARMAX models
    - Dynamic Factor models
    - Unobserved Component models
  - Markov switching models (MSAR), also known as Hidden Markov Models
    (HMM)
  - Univariate time series analysis: AR, ARIMA
  - Vector autoregressive models, VAR and structural VAR
  - Vector error correction model, VECM
  - exponential smoothing, Holt-Winters
  - Hypothesis tests for time series: unit root, cointegration and
    others
  - Descriptive statistics and process models for time series analysis
- Survival analysis:
  - Proportional hazards regression (Cox models)
  - Survivor function estimation (Kaplan-Meier)
  - Cumulative incidence function estimation
- Multivariate:
  - Principal Component Analysis with missing data
  - Factor Analysis with rotation
  - MANOVA
  - Canonical Correlation
- Nonparametric statistics: Univariate and multivariate kernel density
  estimators
- Datasets: Datasets used for examples and in testing
- Statistics: a wide range of statistical tests
  - diagnostics and specification tests
  - goodness-of-fit and normality tests
  - functions for multiple testing
  - various additional statistical tests
- Imputation with MICE, regression on order statistic and Gaussian
  imputation
- Mediation analysis
- Graphics includes plot functions for visual analysis of data and model
  results
- I/O
  - Tools for reading Stata .dta files, but pandas has a more recent
    version
  - Table output to ascii, latex, and html
- Miscellaneous models
- Sandbox: statsmodels contains a sandbox folder with code in various
  stages of development and testing which is not considered \"production
  ready\". This covers among others
  - Generalized method of moments (GMM) estimators
  - Kernel regression
  - Various extensions to scipy.stats.distributions
  - Panel data models
  - Information theoretic measures

# How to get it

The main branch on GitHub is the most up to date code

<https://www.github.com/statsmodels/statsmodels>

Source download of release tags are available on GitHub

<https://github.com/statsmodels/statsmodels/tags>

Binaries and source distributions are available from PyPi

<https://pypi.org/project/statsmodels/>

Binaries can be installed in Anaconda

conda install statsmodels

# Getting the latest code

## Installing the most recent nightly wheel

The most recent nightly wheel can be installed using pip.

``` bash
python -m pip install -i https://pypi.anaconda.org/scientific-python-nightly-wheels/simple statsmodels --upgrade --use-deprecated=legacy-resolver
```

## Installing from sources

See INSTALL.txt for requirements or see the documentation

<https://statsmodels.github.io/dev/install.html>

# Contributing

Contributions in any form are welcome, including:

- Documentation improvements
- Additional tests
- New features to existing models
- New models

<https://www.statsmodels.org/stable/dev/test_notes>

for instructions on installing statsmodels in *editable* mode.

# License

Modified BSD (3-clause)

# Discussion and Development

Discussions take place on the mailing list

<https://groups.google.com/group/pystatsmodels>

and in the issue tracker. We are very interested in feedback about
usability and suggestions for improvements.

# Bug Reports

Bug reports can be submitted to the issue tracker at

<https://github.com/statsmodels/statsmodels/issues>

### Core Implementation Code & Architecture
#### File: `archive/examples/tests/__init__.py`
```python

```

#### File: `archive/mcevaluate/__init__.py`
```python

```

#### File: `archive/distributions/examples/__init__.py`
```python

```

#### File: `statsmodels/robust/tests/__init__.py`
```python

```

#### File: `statsmodels/robust/tests/results/__init__.py`
```python

```

#### File: `statsmodels/nonparametric/tests/__init__.py`
```python

```


==================================================


## [3/3] Repository: tardis-python-private (`WHEEL_tardis-python-private`)
- **Full Name**: `tardis-python-private`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Crypto HFT Microstructure Project (BTCUSDT, Binance) — OFI + Flow-Control Strategy

This repository implements an **OFI-based microstructure trading strategy** for BTCUSDT using reconstructed order book data. The project is structured as a **research-to-production pipeline**:

1) **Fetch raw exchange data**  
2) **Reconstruct order book + generate features**  
3) **Run in-sample (IS) evaluation & tune parameters**  
4) **Freeze parameters (no look-ahead)**  
5) **Run out-of-sample (OOS) evaluation**  
6) **Add live-readiness checks (latency stress, monitoring metrics, risk controls)**

---

## 1. Strategy Overview

### Signal: Order Flow Imbalance (OFI)
The core predictive input is **Order Flow Imbalance (OFI)** computed from changes in best bid/ask queue sizes (L1). We compute:

- **OFI z-score** (`ofi_z`) using rolling mean/std  
- A **simple alpha proxy**: regression-like beta estimate linking next returns to lagged `ofi_z`  
- **Trading intent** in `[-1, 1]`:  
  `sig_intent = clip(sig_strength * ofi_z, -1, 1)`

### Execution model: Maker/Taker mixture (fill-aware)
Instead of assuming perfect fills, we approximate maker fill probability using **queue imbalance (QI)**:

- Convert QI to a signed measure when needed, then use `|QI|` to approximate difficulty of passive fills
- `p_maker_fill = (1 - |QI|)^1.5`
- Maker participation is used when expected edge exceeds a join threshold:
  `join_maker = alpha_bps - join_thresh * half_spread_bps >= 0`

This produces:
- `f_maker` and `f_taker` fractions (maker + taker sum to 1)

### Risk controls
- **Inventory cap**: hard position limit in units  
- **Inventory decay**: mild mean reversion of inventory over time  
- **Kill-switch** (causal, persistent): if day-to-date or rolling PnL breaches thresholds, trading halts and inventory is flattened linearly over N bars using taker costs.

### Flow-Control overlay (regime scalers)
To reduce performance inflation from toxic regimes, we apply **regime scalers** to trading intent:

- Volatility scaler (high vol → reduce risk)
- Spread scaler (abnormally tight spread → reduce risk)
- Toxicity scaler (abnormally large OFI vs rolling baseline → reduce risk)

Scalers can be combined via:
- `min` (most conservative)
- `weighted` (tunable weights)

Final intent:
- `sig_intent_scaled = sig_intent * scale`

---

## 2. Repository Layout (Essential Files)

### Core building blocks

#### `ob_core.py`
Minimal order book ladder + parsing helpers.
- Maintains best bid/ask and sizes efficiently
- Computes:
  - mid / spread
  - microprice (L1)
  - queue imbalance (QI)
- Used by feature reconstruction to turn raw book updates into consistent microstructure features.

#### `reconstruct_and_features.py`
Feature generation pipeline (multi-day).
- Loads:
  - book snapshots (initial state)
  - incremental L2 updates (depth deltas)
  - trades
- Reconstructs book over time grid (e.g. `100ms`)
- Outputs daily parquet + merged parquet under:
  `data/binance/features/...parquet`

#### `strategy_core.py`
**Single source of truth** for strategy logic.
Implements:
- feature engineering (`build_base_features`)
- flow-control overlay (`apply_regime_scalers`)
- execution & transaction costs (`execute_account`)
- kill-switch & flatten (`apply_killswitch_and_flatten`)
- reporting:
  - `compute_attribution_table` (daily Sharpe, drawdown, worst day, etc.)
  - `compute_live_metrics` (turnover, edge bps on traded notional, inventory utilization)
- utilities:
  - `assert_invariants` (sanity checks)
  - `freeze_dict` (serialize params for OOS)
  - optional `apply_latency` helper (stress testing)

### Thin wrappers (experiments / runs)

#### `IS_backtest.py`
In-sample evaluation.
- Reads IS features parquet
- Runs:
  - baseline (fill-aware)
  - flow-control strategy
- Outputs:
  - IS attribution CSV
  - live-style metrics JSON
  - cumulative PnL plot
  - frozen parameter JSON (`freeze_*.json`) used by OOS

#### `oos_backtest.py`
Out-of-sample evaluation.
- Loads the frozen JSON from IS
- Re-runs the same pipeline on OOS parquet
- Outputs:
  - OOS attribution CSV (daily Sharpe)
  - live-style metrics JSON
  - cumulative PnL plot

#### `fetch_binance_data.py` 
Download Binance data into `data/binance/...` layout.

---

## 3. End-to-End Workflow (How to Run)
### Step 0 — Environment setup
You need parquet support and standard numeric stack:

- `numpy` (recommend `<2.0` if your pandas/pyarrow stack is older)
- `pandas`
- `pyarrow` (recommended parquet engine) or `fastparquet`
- `sortedcontainers`
- `matplotlib`

### Core Implementation Code & Architecture
#### File: `IS_reports_BTCUSDT_PERP/live_metrics_flow_control.json`
```python
{
  "turnover_usd": 604770.7091716779,
  "avg_abs_intent": 0.007623205166158301,
  "inv_utilization": 0.13856936824201924,
  "gross_edge_bps_on_traded": 13.573607050368398,
  "cost_bps_on_traded": 4.962130488407672,
  "net_edge_bps_on_traded": 8.611476561960725,
  "total_pnl_after_usd": 520.796878739227,
  "total_pnl_after_bps_on_capital": 86.79947978987117
}
```

#### File: `OOS-Backtest_reports/live_metrics_oos.json`
```python
{
  "executed_notional_usd": 413333.5438245301,
  "intent_turnover_usd": 207900.0,
  "avg_abs_intent": 2.2280543876756762e-05,
  "inv_utilization": 0.00020571779814777743,
  "gross_edge_bps_on_executed": 5.69204800750581,
  "cost_bps_on_executed": 1.8269698475593619,
  "net_edge_bps_on_executed": 3.86507815994645,
  "total_pnl_after_usd": 159.756645300946,
  "total_pnl_after_bps_on_capital": 31.951329060189202
}
```

#### File: `IS_reports/live_metrics_flow_control.json`
```python
{
  "executed_notional_usd": 394590.3526240724,
  "intent_turnover_usd": 198450.0,
  "avg_abs_intent": 1.8229401768078358e-05,
  "inv_utilization": 0.00016268311248386941,
  "gross_edge_bps_on_executed": 6.708250739643934,
  "cost_bps_on_executed": 1.8485285616502696,
  "net_edge_bps_on_executed": 4.859722177993665,
  "total_pnl_after_usd": 191.75994878695454,
  "total_pnl_after_bps_on_capital": 38.35198975739092
}
```

#### File: `IS_reports/freeze_2025-12-13.json`
```python
{
  "version": "core-refactor",
  "fees": {
    "taker_fee_bps": 1.725,
    "maker_rebate_bps": -0.6,
    "slip_bps_maker": 0.2,
    "slip_bps_taker": 0.5
  },
  "timing": {
    "bar_ms": 100
  },
  "signal": {
    "z_win": 500,
    "beta_win": 2000,
    "sig_strength": 0.2,
    "join_thresh": 0.55
  },
  "filters": {
    "vol_win": 200,
    "flow_win": 400,
    "vol_pct_hi": 97,
    "spread_pct_lo": 5.0,
    "toxic_mult": 2.6,
    "toxic_scale": 0.7
  },
  "scaler": {
    "combine": "weighted",
    "weights": [
      0.4,
      0.3,
      0.3
    ]
  },
  "risk": {
    "capital_usd": 50000.0,
    "notional_usd": 1800,
    "inv_cap_units": 4.0,
    "inv_decay_lambda": 0.0005555555555555556,
    "flatten_n_bars": 60
  },
  "killswitch": {
    "dd_kill_day_usd": -500.0,
    "dd_kill_roll_usd": -400.0,
    "roll_window_min": 60,
    "flatten_n_bars": 60
  }
}
```

#### File: `IS_reports_BTCUSDT_PERP/freeze_is.json`
```python
{
  "version": "core-refactor",
  "fees": {
    "taker_fee_bps": 1.5,
    "maker_rebate_bps": -0.4,
    "slip_bps_maker": 0.2,
    "slip_bps_taker": 0.5,
    "funding_rate_bps": 0.0,
    "funding_interval_hours": 8
  },
  "timing": {
    "bar_ms": 100
  },
  "signal": {
    "z_win": 500,
    "beta_win": 2000,
    "sig_strength": 1.0,
    "join_thresh": 0.55
  },
  "filters": {
    "vol_win": 200,
    "flow_win": 400,
    "vol_pct_hi": 97,
    "spread_pct_lo": 5.0,
    "toxic_mult": 2.6,
    "toxic_scale": 0.3
  },
  "scaler": {
    "combine": "weighted",
    "weights": [
      0.4,
      0.3,
      0.3
    ]
  },
  "risk": {
    "capital_usd": 60000.0,
    "notional_usd": 30000,
    "inv_cap_units": 5.0,
    "inv_decay_lambda": 0.0005555555555555556,
    "flatten_n_bars": 60
  },
  "killswitch": {
    "dd_kill_day_usd": -500.0,
    "dd_kill_roll_usd": -400.0,
    "roll_window_min": 60,
    "flatten_n_bars": 60
  },
  "alpha_modules": {
    "microprice_ofi": {
      "alpha_scale_bps": 10.0,
      "mp_clip": 2.0,
      "ofi_fast_span": 3,
      "ofi_slow_span": 30,
      "alpha_clip_bps": 12.0,
      "trend_strength_thresh": 0.35,
      "one_sided": true,
      "mp_deadzone_hs": 0.15
    },
    "intent": {
      "denom_bps": 1.0,
      "hold_bars": 3
    },
    "maker": {
      "maker_min": 0.02,
      "penalty_power": 0.3
    },
    "latency_ms": 100
  }
}
```

#### File: `fetch_binance_data.py`
```python
import os
import requests
import gzip
import pandas as pd
from datetime import datetime, timedelta

EXCHANGE = "binance"           
DATA_TYPES = ["book_snapshot_25", "incremental_book_L2", "trades"] 
SYMBOL = "BTCUSDT"
FROM_DATE = "2025-10-20"         
TO_DATE = "2025-10-27"         
API_KEY = os.getenv("TARDIS_API_KEY", "API_key(hidden on purpose)")

def download_tardis_csv(exchange, data_type, symbol, date, api_key):
    """Download a single Tardis CSV file and save it under data/{exchange}/{data_type}/"""
    year, month, day = date.split("-")
    url = f"https://datasets.tardis.dev/v1/{exchange}/{data_type}/{year}/{month}/{day}/{symbol}.csv.gz"
    headers = {"Authorization": f"Bearer {api_key}"}

    save_dir = f"data/{exchange}/{data_type}"
    os.makedirs(save_dir, exist_ok=True)
    filename = os.path.join(save_dir, f"{date}_{symbol}.csv.gz")

    print(f" Downloading {data_type} for {date} → {filename}")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f" Saved: {filename}")
        return filename
    else:
        print(f" Failed {date} ({data_type}): {response.status_code} - {response.text}")
        return None


def main():
    start = datetime.fromisoformat(FROM_DATE)
    end   = datetime.fromisoformat(TO_DATE)

    for data_type in DATA_TYPES:
        print(f"\n Fetching {data_type} data for {SYMBOL} ({FROM_DATE} to {TO_DATE})")
        current = start
        downloaded_files = []

        while current < end:
            date_str = current.strftime("%Y-%m-%d")
            f = download_tardis_csv(EXCHANGE, data_type, SYMBOL, date_str, API_KEY)
            if f:
                downloaded_files.append(f)
            current += timedelta(days=1)

        # Quick preview for sanity check
        if downloaded_files:
            print(f"\n Preview for {data_type}: {downloaded_files[0]}")
            try:
                df = pd.read_csv(gzip.open(downloaded_files[0]), nrows=5)
                print(df.head())
            except Exception as e:
                print(f" Could not preview {data_type}: {e}")

    print("\n All downloads complete. Data saved under ./data/binance/")


# --------------------------------------------------
if __name__ == "__main__":
    main()
```


==================================================
