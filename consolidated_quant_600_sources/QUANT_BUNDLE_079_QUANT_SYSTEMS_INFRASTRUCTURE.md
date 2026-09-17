# ⚡ [QUANT-SOURCE-079] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_079_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: hyperfine (`WHEEL_hyperfine`)
- **Full Name**: `hyperfine`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# hyperfine
[![CICD](https://github.com/sharkdp/hyperfine/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/hyperfine/actions/workflows/CICD.yml)
[![Version info](https://img.shields.io/crates/v/hyperfine.svg)](https://crates.io/crates/hyperfine)
[中文](https://github.com/chinanf-boy/hyperfine-zh)

A command-line benchmarking tool.

**Demo**: Benchmarking [`fd`](https://github.com/sharkdp/fd) and
[`find`](https://www.gnu.org/software/findutils/):

![hyperfine](https://i.imgur.com/z19OYxE.gif)

## Features

* Statistical analysis across multiple runs.
* Support for arbitrary shell commands.
* Constant feedback about the benchmark progress and current estimates.
* Warmup runs can be executed before the actual benchmark.
* Cache-clearing commands can be set up before each timing run.
* Statistical outlier detection to detect interference from other programs and caching effects.
* Export results to various formats: CSV, JSON, Markdown, AsciiDoc.
* Parameterized benchmarks (e.g. vary the number of threads).
* Cross-platform

## Usage

### Basic benchmarks

To run a benchmark, you can simply call `hyperfine <command>...`. The argument(s) can be any
shell command. For example:
```sh
hyperfine 'sleep 0.3'
```

Hyperfine will automatically determine the number of runs to perform for each command. By default,
it will perform *at least* 10 benchmarking runs and measure for at least 3 seconds. To change this,
you can use the `-r`/`--runs` option:
```sh
hyperfine --runs 5 'sleep 0.3'
```

If you want to compare the runtimes of different programs, you can pass multiple commands:
```sh
hyperfine 'hexdump file' 'xxd file'
```

### Warmup runs and preparation commands

For programs that perform a lot of disk I/O, the benchmarking results can be heavily influenced
by disk caches and whether they are cold or warm.

If you want to run the benchmark on a warm cache, you can use the `-w`/`--warmup` option to
perform a certain number of program executions before the actual benchmark:
```sh
hyperfine --warmup 3 'grep -R TODO *'
```

Conversely, if you want to run the benchmark for a cold cache, you can use the `-p`/`--prepare`
option to run a special command before *each* timing run. For example, to clear harddisk caches
on Linux, you can run
```sh
sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
```
To use this specific command with hyperfine, call `sudo -v` to temporarily gain sudo permissions
and then call:
```sh
hyperfine --prepare 'sync; echo 3 | sudo tee /proc/sys/vm/drop_caches' 'grep -R TODO *'
```

### Parameterized benchmarks

If you want to run a series of benchmarks where a single parameter is varied (say, the number of
threads), you can use the `-P`/`--parameter-scan` option and call:
```sh
hyperfine --prepare 'make clean' --parameter-scan num_threads 1 12 'make -j {num_threads}'
```
This also works with decimal numbers. The `-D`/`--parameter-step-size` option can be used
to control the step size:
```sh
hyperfine --parameter-scan delay 0.3 0.7 -D 0.2 'sleep {delay}'
```
This runs `sleep 0.3`, `sleep 0.5` and `sleep 0.7`.

For non-numeric parameters, you can also supply a list of values with the `-L`/`--parameter-list`
option:
```
hyperfine -L compiler gcc,clang '{compiler} -O2 main.cpp'
```

### Intermediate shell

By default, commands are executed using a predefined shell (`/bin/sh` on Unix, `cmd.exe` on Windows).
If you want to use a different shell, you can use the `-S, --shell <SHELL>` option:
```sh
hyperfine --shell zsh 'for i in {1..10000}; do echo test; done'
```

Note that hyperfine always *corrects for the shell spawning time*. To do this, it performs a calibration
procedure where it runs the shell with an empty command (multiple times), to measure the startup time
of the shell. It will then subtract this time from the total to show the actual time used by the command
in question.

If you want to run a benchmark *without an intermediate shell*, you can use the `-N` or `--shell=none`
option. This is helpful for very fast commands (< 5 ms) where the shell startup overhead correction would
produce a significant amount of noise. Note that you cannot use shell syntax like `*` or `~` in this case.
```
hyperfine -N 'grep TODO /home/user'
```


### Shell functions and aliases

If you are using bash, you can export shell functions to directly benchmark them with hyperfine:

```bash
my_function() { sleep 1; }
export -f my_function
hyperfine --shell=bash my_function
```

Otherwise, inline them into or source them from the benchmarked program:

```sh
hyperfine 'my_function() { sleep 1; }; my_function'

echo 'alias my_alias="sleep 1"' > /tmp/my_alias.sh
hyperfine '. /tmp/my_alias.sh; my_alias'
```

### Exporting results

Hyperfine has multiple options for exporting benchmark results to CSV, JSON, Markdown and other
formats (see `--help` text for details).

#### Markdown

You can use the `--export-markdown <file>` option to create tables like the following:

| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `find . -iregex '.*[0-9]\.jpg$'` | 2.275 ± 0.046 | 2.243 | 2.397 | 9.79 ± 0.22 |
| `find . -iname '*[0-9].jpg'` | 1.427 ± 0.026 | 1.405 | 1.468 | 6.14 ± 0.13 |
| `fd -HI '.*[0-9]\.jpg$'` | 0.232 ± 0.002 | 0.230 | 0.236 | 1.00 |

#### JSON

The JSON output is useful if you want to analyze the benchmark results in more detail. The
[`scripts/`](https://github.com/sharkdp/hyperfine/tree/master/scripts) folder includes a lot
of helpful Python programs to further analyze benchmark results and create helpful
visualizations, like a histogram of runtimes or a whisker plot to compare
multiple benchmarks:

| ![](doc/histogram.png) | ![](doc/whisker.png) |
|---:|---:|


### Detailed benchmark flowchart

The following chart explains the execution order of various timing runs when using options
like `--warmup`, `--prepare <cmd>`, `--setup <cmd>` or `--cleanup <cmd>`:

![](doc/execution-order.png)

## Installation

[![Packaging status](https://repology.org/badge/vertical-allrepos/hyperfine.svg?columns=3&exclude_unsupported=1)](https://repology.org/project/hyperfine/versions)

### On Ubuntu

On Ubuntu, hyperfine can be installed [from the official repositories](https://launchpad.net/ubuntu/+source/rust-hyperfine):
```
apt install hyperfine
```

Alternatively, for the latest version, you can download the appropriate `.deb` package from the [Release page](https://github.com/sharkdp/hyperfine/releases) and install it via `dpkg`:
```
wget https://github.com/sharkdp/hyperfine/releases/download/v1.20.0/hyperfine_1.20.0_amd64.deb
sudo dpkg -i hyperfine_1.20.0_amd64.deb
```

### On Fedora

On Fedora, hyperfine can be installed from the official repositories:

```sh
dnf install hyperfine
```

### On Alpine Linux

On Alpine Linux, hyperfine can be installed [from the official repositories](https://pkgs.alpinelinux.org/packages?name=hyperfine):
```
apk add hyperfine
```

### On Arch Linux

On Arch Linux, hyperfine can be installed [from the official repositories](https://archlinux.org/packages/extra/x86_64/hyperfine/):
```
pacman -S hyperfine
```

### On Debian Linux

On Debian Linux, hyperfine can be installed [from the official repositories](https://packages.debian.org/hyperfine):
```
apt install hyperfine
```

### On Exherbo Linux

On Exherbo Linux, hyperfine can be installed [from the rust repositories](https://gitlab.exherbo.org/exherbo/rust/-/tree/master/packages/sys-apps/hyperfine):
```
cave resolve -x repository/rust
cave resolve -x hyperfine
```

### On Funtoo Linux

On Funtoo Linux, hyperfine can be installed [from core-kit](https://github.com/funtoo/core-kit/tree/1.4-release/app-benchmarks/hyperfine):
```
emerge app-benchmarks/hyperfine
```

### On NixOS

On NixOS, hyperfine can be installed [from the official repositories](https://nixos.org/nixos/packages.html?query=hyperfine):
```
nix-env -i hyperfine
```

### On Flox

On Flox, hyperfine can be installed as follows.
```
flox install hyperfine
```
Hyperfine's version in Flox follows that of Nix.

### On openSUSE

On openSUSE, hyperfine can be installed [from the official repositories](https://software.opensuse.org/package/hyperfine):
```
zypper install hyperfine
```

### On Void Linux

Hyperfine can be installed via xbps

```
xbps-install -S hyperfine
```

### On macOS

Hyperfine can be installed via [Homebrew](https://brew.sh):
```
brew install hyperfine
```

Or you can install using [MacPorts](https://www.macports.org):
```
sudo port selfupdate
sudo port install hyperfine
```

### On FreeBSD

Hyperfine can be installed via pkg:
```
pkg install hyperfine
```

### On OpenBSD

```
doas pkg_add hyperfine
```

### On Windows

Hyperfine can be installed via [Chocolatey](https://community.chocolatey.org/packages/hyperfine), [Scoop](https://scoop.sh/#/apps?q=hyperfine&s=0&d=1&o=true&id=8f7c10f75ecf5f9e42a862c615257328e2f70f61), or [Winget](https://github.com/microsoft/winget-pkgs/tree/master/manifests/s/sharkdp/hyperfine):
```
choco install hyperfine
```
```
scoop install hyperfine
```
```
winget install hyperfine
```

### With conda

Hyperfine can be installed via [`conda`](https://conda.io/en/latest/) from the [`conda-forge`](https://anaconda.org/conda-forge/hyperfine) channel:
```
conda install -c conda-forge hyperfine
```

### With cargo (Linux, macOS, Windows)

Hyperfine can be installed from source via [cargo](https://doc.rust-lang.org/cargo/):
```
cargo install --locked hyperfine
```

Make sure that you use Rust 1.76 or newer.

### From binaries (Linux, macOS, Windows)

Download the corresponding archive from the [Release page](https://github.com/sharkdp/hyperfine/releases).

## Alternative tools

Hyperfine is inspired by [bench](https://github.com/Gabriella439/bench).

## Integration with other tools

[Chronologer](https://github.com/dandavison/chronologer) is a tool that uses `hyperfine` to
visualize changes in benchmark timings across your Git history.

[Bencher](https://github.com/bencherdev/bencher) is a continuous benchmarking tool that supports `hyperfine` to
track benchmarks and catch performance regressions in CI.

Drop hyperfine JSON outputs onto the [Venz](https://try.venz.dev) chart to visualize the results,
and manage hyperfine configurations.

Make sure to check out the [`scripts` folder](https://github.com/sharkdp/hyperfine/tree/master/scripts)
in this repository for a set of tools to work with `hyperfine` benchmark results.

## Origin of the name

The name *hyperfine* was chosen in reference to the hyperfine levels of caesium 133 which play a crucial role in the
[definition of our base unit of time](https://en.wikipedia.org/wiki/Second#History_of_definition)
— the second.

## Citing hyperfine

Thank you for considering to cite hyperfine in your research work. Please see the information
in the sidebar on how to properly cite hyperfine.

## License

`hyperfine` is dual-licensed under the terms of the MIT License and the Apache License 2.0.

See the [LICENSE-APACHE](LICENSE-APACHE) and [LICENSE-MIT](LICENSE-MIT) files for details.

### Core Implementation Code & Architecture
#### File: `src/output/mod.rs`
```python
pub mod format;
pub mod progress_bar;
pub mod warnings;
```

#### File: `scripts/ruff.toml`
```python
target-version = "py310"

[lint]
extend-select = ["I", "UP", "RUF"]
```

#### File: `src/util/mod.rs`
```python
pub mod exit_code;
pub mod min_max;
pub mod number;
pub mod randomized_environment_offset;
pub mod units;
```

#### File: `tests/common.rs`
```python
use std::process::Command;

use assert_cmd::cargo::CommandCargoExt;

pub fn hyperfine_raw_command() -> Command {
    let mut cmd = Command::cargo_bin("hyperfine").unwrap();
    cmd.current_dir("tests/");
    cmd
}

pub fn hyperfine() -> assert_cmd::Command {
    assert_cmd::Command::from_std(hyperfine_raw_command())
}
```

#### File: `src/benchmark/timing_result.rs`
```python
use crate::util::units::Second;

/// Results from timing a single command
#[derive(Debug, Default, Copy, Clone)]
pub struct TimingResult {
    /// Wall clock time
    pub time_real: Second,

    /// Time spent in user mode
    pub time_user: Second,

    /// Time spent in kernel mode
    pub time_system: Second,

    /// Maximum amount of memory used, in bytes
    pub memory_usage_byte: u64,
}
```

#### File: `src/util/randomized_environment_offset.rs`
```python
/// Returns a string with a random length. This value will be set as an environment
/// variable to account for offset effects. See [1] for more details.
///
/// [1] Mytkowicz, 2009. Producing Wrong Data Without Doing Anything Obviously Wrong!.
///     Sigplan Notices - SIGPLAN. 44. 265-276. 10.1145/1508284.1508275.
pub fn value() -> String {
    "X".repeat(rand::random::<usize>() % 4096usize)
}
```


==================================================


## [2/3] Repository: investpy (`WHEEL_investpy`)
- **Full Name**: `investpy`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
  <img src="https://raw.githubusercontent.com/alvarobartt/investpy/master/docs/source/_static/logo.png" hspace="20">
</p>

## :warning: `investpy` is not working fine currently due to some Investing.com changes in their APIs, so please use [`investiny`](https://github.com/alvarobartt/investiny) in the meantime as I'm actively updating it and adding more and more features of some temporary solutions while we fix `investpy`. Thanks!

<h2 align="center">Financial Data Extraction from Investing.com with Python</h2>

investpy is a Python package to retrieve data from [Investing.com](https://www.investing.com/), which provides data retrieval 
from up to 39952 stocks, 82221 funds, 11403 ETFs, 2029 currency crosses, 7797 indices, 688 bonds, 66 commodities, 250 certificates, 
and 4697 cryptocurrencies.

investpy allows the user to download both recent and historical data from all the financial products indexed at Investing.com. 
**It includes data from all over the world**, from countries such as United States, France, India, Spain, Russia, or Germany, 
amongst many others.

investpy seeks to be one of the most complete Python packages when it comes to financial data extraction to stop relying 
on public/private APIs since investpy is **FREE** and has **NO LIMITATIONS**. These are some of the features that currently lead 
investpy to be one of the most consistent packages when it comes to financial data retrieval.

[![Python Version](https://img.shields.io/pypi/pyversions/investpy.svg)](https://pypi.org/project/investpy/)
[![PyPI Version](https://img.shields.io/pypi/v/investpy.svg)](https://pypi.org/project/investpy/)
[![Package Status](https://img.shields.io/pypi/status/investpy.svg)](https://pypi.org/project/investpy/)
[![Build Status](https://github.com/alvarobartt/investpy/workflows/run_tests/badge.svg)](https://github.com/alvarobartt/investpy/actions?query=workflow%3Arun_tests)
[![Documentation Status](https://readthedocs.org/projects/investpy/badge/?version=latest)](https://investpy.readthedocs.io/)

**If you want to support the project, you can buy the developer a coffee. More information at: [buy-me-a-coffee](https://github.com/alvarobartt/buy-me-a-coffee)**

<p align="center"><a href="https://www.buymeacoffee.com/alvarobartt" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></p>

---

## :hammer_and_wrench: Installation

To get this package working you will need to **install it via pip** (with a Python 3.6 version or higher) on the terminal by typing:

``$ pip install investpy``

Additionally, **if you want to use the latest investpy version instead of the stable one, you can install it from source** with the following command:

``$ pip install git+https://github.com/alvarobartt/investpy.git@master``

**The master branch ensures the user that the most updated version will always be working and fully operative** so as not to wait until the 
the stable release comes out (which eventually may take some time depending on the number of issues to solve).

---

## :computer: Usage

Even though some investpy usage examples are presented on the [docs](https://investpy.readthedocs.io/usage.html), 
some basic functionality will be sorted out with sample Python code blocks. Additionally, more usage examples 
can be found under [examples/](https://github.com/alvarobartt/investpy/tree/master/examples) directory, which 
contains a collection of Jupyter Notebooks on how to use investpy and handle its data.

:pushpin: __Note that `investpy.search_quotes` is the only function that ensures that the data is updated and aligned 1:1 with
the data provided by Investing.com!__

### :chart_with_upwards_trend: Recent/Historical Data Retrieval

investpy allows the user to **download both recent and historical data from any financial product indexed** 
(stocks, funds, ETFs, currency crosses, certificates, bonds, commodities, indices, and cryptos). In 
the example presented below, the historical data from the past years of a stock is retrieved. 

```python
import investpy

df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States',
                                        from_date='01/01/2010',
                                        to_date='01/01/2020')
print(df.head())
```
```{r, engine='python', count_lines}
             Open   High    Low  Close     Volume Currency
Date                                                      
2010-01-04  30.49  30.64  30.34  30.57  123432176      USD
2010-01-05  30.66  30.80  30.46  30.63  150476160      USD
2010-01-06  30.63  30.75  30.11  30.14  138039728      USD
2010-01-07  30.25  30.29  29.86  30.08  119282440      USD
2010-01-08  30.04  30.29  29.87  30.28  111969192      USD
```

To get to know all the available recent and historical data extraction functions provided by 
investpy, and also, parameter tuning, please read the docs.

### :mag: Search Live Data

**Investing.com search engine is completely integrated** with investpy, which means that any available 
financial product (quote) can be easily found. The search function allows the user to tune the parameters 
to adjust the search results to their needs, where both product types and countries from where the 
products are, can be specified. **All the search functionality can be easily used**, for example, as 
presented in the following piece of code:

```python
import investpy

search_result = investpy.search_quotes(text='apple', products=['stocks'],
                                       countries=['united states'], n_results=1)
print(search_result)
```
```json
{"id_": 6408, "name": "Apple Inc", "symbol": "AAPL", "country": "united states", "tag": "/equities/apple-computer-inc", "pair_type": "stocks", "exchange": "NASDAQ"}
```

Retrieved search results will be a `list` of `investpy.utils.search_obj.SearchObj` class instances, unless
`n_results` is set to 1, when just a single `investpy.utils.search_obj.SearchObj` class instance will be returned.
To get to know which are the available functions and attributes of the returned search results, please read the related 
documentation at [Search Engine Documentation](https://investpy.readthedocs.io/search_api.html). So on, those 
search results let the user retrieve both recent and historical data, its information, the technical indicators,
the default currency, etc., as presented in the piece of code below:

```python
recent_data = search_result.retrieve_recent_data()
historical_data = search_result.retrieve_historical_data(from_date='01/01/2019', to_date='01/01/2020')
information = search_result.retrieve_information()
default_currency = search_result.retrieve_currency()
technical_indicators = search_result.retrieve_technical_indicators(interval='daily')
```

### :money_with_wings: Crypto Currencies Data Retrieval

Cryptocurrencies support has recently been included, to let the user retrieve data and information from any 
available crypto at Investing.com. Please note that some cryptocurrencies do not have available data indexed 
at Investing.com so that it can not be retrieved using investpy either, even though they are just a few, 
consider it.

As already presented previously, **historical data retrieval using investpy is really easy**. The piece of code 
presented below shows how to retrieve the past years of historical data from Bitcoin (BTC).

```python
import investpy

data = investpy.get_crypto_historical_data(crypto='bitcoin',
                                           from_date='01/01/2014',
                                           to_date='01/01/2019')

print(data.head())
```
```{r, engine='python', count_lines}
             Open    High    Low   Close  Volume Currency
Date                                                     
2014-01-01  805.9   829.9  771.0   815.9   10757      USD
2014-01-02  815.9   886.2  810.5   856.9   12812      USD
2014-01-03  856.9   888.2  839.4   884.3    9709      USD
2014-01-04  884.3   932.2  848.3   924.7   14239      USD
2014-01-05  924.7  1029.9  911.4  1014.7   21374      USD
```

---

## :open_book: Documentation

You can find the **complete investpy documentation** at [Documentation](https://investpy.readthedocs.io/).

---

## :sparkles: Contribute

As this is an open-source project it is **open to contributions, bug reports, bug fixes, documentation improvements, 
enhancements, and ideas**. There is an open tab of [issues](https://github.com/alvarobartt/investpy/issues) where 
anyone can open new issues if needed or navigate through them to solve them or contribute to its solving. 
Remember that issues are not threads to describe multiple problems, this does not mean that issues can not 
be discussed, but so to keep structured project management, the same issue should not describe different 
problems, just the main one and some nested/related errors that may be found.

---

## :question: Discussions (Q&A, AMA)

GitHub recently released a new feature named __GitHub Discussions__ (still in beta). GitHub Discussions is a 
collaborative communication forum for the community around an open source project.

Check the investpy GitHub Discussions page at [Discussions](https://github.com/alvarobartt/investpy/discussions), 
and feel free to ask me (ar any developer) anything, share updates, have open-ended conversations, and follow along 
on decisions affecting the community's way of working.

:pushpin: __Note__. Usually I don't answer emails asking me questions about investpy, as we currently have the
GitHub Discussions tab, and I encourage you to use it. GitHub Discussions is the easiest way to contact me about 
investpy, so that I don't answer the same stuff more than once via email, as anyone can see the opened/answered
discussions.

---

## :card_index_dividers: Related projects

Since investpy is intended to retrieve data from different financial products as indexed in Investing.com, 
the **development of some support modules which implement an additional functionality based on investpy data**, 
is presented. Note that **anyone can contribute to this section** by creating any package, module, or utility that 
uses investpy. So on, the ones already created are going to be presented, since they are intended to be used 
combined with investpy:

- [pyrtfolio](https://github.com/alvarobartt/pyrtfolio/): is a Python package to generate stock portfolios.
- [trendet](https://github.com/alvarobartt/trendet/): is a Python package for trend detection on stock time-series data.
- [pypme](https://github.com/ymyke/pypme): is a Python package for PME (Public Market Equivalent) calculation

If you developed an interesting/useful project based on investpy data, please open an issue to let me know to 
include it in this section.

---

## :memo: Citation

When citing this repository on your scientific publications please use the following **BibTeX** citation:

```bibtex
@misc{investpy,
    author = {Alvaro Bartolome del Canto},
    title = {investpy - Financial Data Extraction from Investing.com with Python},
    year = {2018-2021},
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/alvarobartt/investpy}},
}
```

When citing this repository on any other social media, please use the following citation:

```
investpy - Financial Data Extraction from Investing.com with Python developed by Alvaro Bartolome del Canto
```

You should also mention the source from where the data is retrieved, Investing.com; even though it's already
included in the package short description title.

---

## :man_technologist: Contact Information

You can contact me at any of my social network profiles:

- :briefcase: LinkedIn: https://linkedin.com/in/alvarobartt
- :bird: Twitter: https://twitter.com/alvarobartt
- :octocat: GitHub: https://github.com/alvarobartt

Or via email at alvarobartt@yahoo.com.

---

## :warning: Disclaimer

This Python package has been made for **research purposes** to fit the needs that Investing.com does not cover, 
so this package works like an Application Programming Interface (API) of Investing.com developed in an **altruistic way**.

Conclude that **investpy is not affiliated in any way to Investing.com or any dependant company**, the only 
requirement specified by Investing.com to develop this package was to "mention the source where data is 
retrieved from".

### Core Implementation Code & Architecture
#### File: `investpy/utils/__init__.py`
```python
# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.
# (ノಠ益ಠ)ノ彡┻━┻
```

#### File: `investpy/data/__init__.py`
```python
# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.
# (ノಠ益ಠ)ノ彡┻━┻
```

#### File: `investpy/utils/extra.py`
```python
# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import random

import pandas as pd
import pkg_resources

from . import constant as cst


def resource_to_data(path_to_data):
    """
    This is an auxiliar function to read data from a given path, so as to wrap the load
    process of the static data files from investpy.

    Returns:
        :obj:`pandas.DataFrame` - data:
            This function returns a :obj:`pandas.DataFrame` object with all the static file's data
            retrieved from investpy.

    Raises:
        FileNotFoundError: raised if the static data file was not found.
        IOError: raised if the data file is empty or errored.

    """

    resource_package = "investpy"
    resource_path = "/".join(("resources", path_to_data))
    if pkg_resources.resource_exists(resource_package, resource_path):
        data = pd.read_csv(
            pkg_resources.resource_filename(resource_package, resource_path),
            keep_default_na=False,
        )
    else:
        raise FileNotFoundError("ERR#0115: data file not found or errored.")

    if data is None:
        raise IOError("ERR#0115: data file was empty or errored.")

    return data


def random_user_agent():
    """
    This function selects a random User-Agent from the User-Agent list, which is a constant
    variable that can be found at `investpy.utils.constant.USER_AGENTS`. User-Agents are used in
    order to avoid the limitations of the requests to Investing.com. The User-Agent is
    specified on the headers of the requests and is different for every request.

    Note that Investing.com, via changing the User-Agent on the headers of every request, allows
    a lot of requests, since it has been tested with over 10k consecutive requests without getting
    any HTTP error code from Investing.com.

    Returns:
        :obj:`str` - user_agent:
            The returned :obj:`str` is the name of a random User-Agent, which will be passed on the
            headers of a request so to avoid restrictions due to the use of multiple requests from the
            same User-Agent.

    """

    return random.choice(cst.USER_AGENTS)
```

#### File: `setup.py`
```python
# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

import io

from setuptools import setup, find_packages


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='investpy',
    version='1.0.8',
    packages=find_packages(),
    url='https://investpy.readthedocs.io/',
    download_url='https://github.com/alvarobartt/investpy/archive/1.0.8.tar.gz',
    license='MIT License',
    author='Alvaro Bartolome',
    author_email='alvarobdc@yahoo.com',
    description='Financial Data Extraction from Investing.com with Python',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements/requirements.txt'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.7',
    extras_require={
        "tests": requirements(filename='requirements/tests-requirements.txt'),
        "docs": requirements(filename='requirements/docs-requirements.txt')
    },
    keywords=', '.join([
        'investing', 'investing-api', 'historical-data',
        'financial-data', 'stocks', 'funds', 'etfs',
        'indices', 'currency crosses', 'bonds', 'commodities',
        'crypto currencies'
    ]),
    project_urls={
        'Bug Reports': 'https://github.com/alvarobartt/investpy/issues',
        'Source': 'https://github.com/alvarobartt/investpy',
        'Documentation': 'https://investpy.readthedocs.io/'
    },
)
```

#### File: `investpy/__init__.py`
```python
# Copyright 2018-2021 Alvaro Bartolome, alvarobartt @ GitHub
# See LICENSE for details.

__author__ = "Alvaro Bartolome @ alvarobartt in GitHub"
__version__ = "1.0.8"

from .bonds import (
    get_bond_countries,
    get_bond_historical_data,
    get_bond_information,
    get_bond_recent_data,
    get_bonds,
    get_bonds_dict,
    get_bonds_list,
    get_bonds_overview,
    search_bonds,
)
from .certificates import (
    get_certificate_countries,
    get_certificate_historical_data,
    get_certificate_information,
    get_certificate_recent_data,
    get_certificates,
    get_certificates_dict,
    get_certificates_list,
    get_certificates_overview,
    search_certificates,
)
from .commodities import (
    get_commodities,
    get_commodities_dict,
    get_commodities_list,
    get_commodities_overview,
    get_commodity_groups,
    get_commodity_historical_data,
    get_commodity_information,
    get_commodity_recent_data,
    search_commodities,
)
from .crypto import (
    get_crypto_historical_data,
    get_crypto_information,
    get_crypto_recent_data,
    get_cryptos,
    get_cryptos_dict,
    get_cryptos_list,
    get_cryptos_overview,
    search_cryptos,
)
from .currency_crosses import (
    get_available_currencies,
    get_currency_cross_historical_data,
    get_currency_cross_information,
    get_currency_cross_recent_data,
    get_currency_crosses,
    get_currency_crosses_dict,
    get_currency_crosses_list,
    get_currency_crosses_overview,
    search_currency_crosses,
)
from .etfs import (
    get_etf_countries,
    get_etf_historical_data,
    get_etf_information,
    get_etf_recent_data,
    get_etfs,
    get_etfs_dict,
    get_etfs_list,
    get_etfs_overview,
    search_etfs,
)
from .funds import (
    get_fund_countries,
    get_fund_historical_data,
    get_fund_information,
    get_fund_recent_data,
    get_funds,
    get_funds_dict,
    get_funds_list,
    get_funds_overview,
    search_funds,
)
from .indices import (
    get_index_countries,
    get_index_historical_data,
    get_index_information,
    get_index_recent_data,
    get_indices,
    get_indices_dict,
    get_indices_list,
    get_indices_overview,
    search_indices,
)
from .news import economic_calendar
from .search import search_quotes
from .stocks import (
    get_stock_company_profile,
    get_stock_countries,
    get_stock_dividends,
    get_stock_financial_summary,
    get_stock_historical_data,
    get_stock_information,
    get_stock_recent_data,
    get_stocks,
    get_stocks_dict,
    get_stocks_list,
    get_stocks_overview,
    search_stocks,
)
from .technical import moving_averages, pivot_points, technical_indicators

# from .search import search_events
```

#### File: `docs/source/conf.py`
```python
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'investpy'
copyright = '2021, Alvaro Bartolome del Canto'
author = 'Alvaro Bartolome del Canto'

# The full version, including alpha/beta/rc tags
release = '1.0.8'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '3.4.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Parser for md files
# source_parsers = {'.md': CommonMarkParser}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'
html_title = "investpy"

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "announcement": "<em>investpy v1.0.8 has just been released! 🔥</em>",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'investpydoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'investpy.tex', 'investpy Documentation',
     'Alvaro Bartolome', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'investpy', 'investpy Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'investpy', 'investpy Documentation',
     author, 'investpy', 'Financial Data Extraction from Investing.com with Python.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------
```


==================================================


## [3/3] Repository: numba (`WHEEL_numba`)
- **Full Name**: `numba`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
*****
Numba
*****

.. image:: https://img.shields.io/badge/discuss-on%20discourse-blue
   :target: https://numba.discourse.group/
   :alt: Discourse

.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.4343230.svg
   :target: https://doi.org/10.5281/zenodo.4343230
   :alt: Zenodo

.. image:: https://img.shields.io/pypi/v/numba.svg
   :target: https://pypi.python.org/pypi/numba/
   :alt: PyPI

.. image:: https://dev.azure.com/numba/numba/_apis/build/status/numba.numba?branchName=main
    :target: https://dev.azure.com/numba/numba/_build/latest?definitionId=1?branchName=main
    :alt: Azure Pipelines

A Just-In-Time Compiler for Numerical Functions in Python
#########################################################

Numba is an open source, NumPy-aware optimizing compiler for Python sponsored
by Anaconda, Inc.  It uses the LLVM compiler project to generate machine code
from Python syntax.

Numba can compile a large subset of numerically-focused Python, including many
NumPy functions.  Additionally, Numba has support for automatic
parallelization of loops, generation of GPU-accelerated code, and creation of
ufuncs and C callbacks.

For more information about Numba, see the Numba homepage:
https://numba.pydata.org and the online documentation:
https://numba.readthedocs.io/en/stable/index.html

Installation
============

Please follow the instructions:

https://numba.readthedocs.io/en/stable/user/installing.html

Demo
====

Please have a look and the demo notebooks via the mybinder service:

https://mybinder.org/v2/gh/numba/numba-examples/master?filepath=notebooks

Contact
=======

Numba has a discourse forum for discussions:

* https://numba.discourse.group

### Core Implementation Code & Architecture
#### File: `numba/misc/__init__.py`
```python

```

#### File: `numba/misc/help/__init__.py`
```python

```

#### File: `numba/core/__init__.py`
```python

```

#### File: `numba/core/annotations/__init__.py`
```python

```

#### File: `numba/core/unsafe/__init__.py`
```python

```

#### File: `numba/cuda/kernels/__init__.py`
```python

```


==================================================
