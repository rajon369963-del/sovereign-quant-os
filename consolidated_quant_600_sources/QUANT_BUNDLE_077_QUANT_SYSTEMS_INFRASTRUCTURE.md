# ⚡ [QUANT-SOURCE-077] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_077_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: fastquant (`WHEEL_fastquant`)
- **Full Name**: `fastquant`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# fastquant :nerd_face:
[![Build Status](https://travis-ci.com/enzoampil/fastquant.svg?branch=master)](https://travis-ci.com/enzoampil/fastquant)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/enzoampil/fastquant/master/LICENSE)
[![Downloads](https://pepy.tech/badge/fastquant)](https://pepy.tech/project/fastquant)
## Bringing backtesting to the mainstream

**fastquant** allows you to easily backtest investment strategies with as few as 3 lines of python code. Its goal is to promote data driven investments by making quantitative analysis in finance accessible to everyone.

To do this type of analysis without coding, you can also try out [Hawksight](https://hawksight.co/), which was just recently launched! :smile:

If you want to interact with us directly, you can also reach us on the [Hawksight discord](https://discord.gg/BHMCw2C6VP). Feel free to ask about fastquant in the #feedback-suggestions and #bug-report channels.


## Features
1. Easily access historical stock data
2. Backtest and optimize trading strategies with only 3 lines of code

<sup>`*` - Both Yahoo Finance and Philippine stock data data are accessible straight from fastquant<sup>

Check out our blog posts in the fastquant [website](https://enzoampil.github.io/fastquant-blog/) and this intro [article](https://towardsdatascience.com/backtest-your-trading-strategy-with-only-3-lines-of-python-3859b4a4ab44?source=friends_link&sk=ec647b6bb43fe322013248fd1d473015) on Medium!

## Installation

### Python

```
pip install fastquant
or
python -m pip install fastquant
```

## Get stock data
All symbols from [Yahoo Finance](https://finance.yahoo.com/) and Philippine Stock Exchange ([PSE](https://www.pesobility.com/stock)) are accessible via `get_stock_data`.

### Python

```
from fastquant import get_stock_data
df = get_stock_data("JFC", "2018-01-01", "2019-01-01")
print(df.head())

#           dt  close
#   2019-01-01  293.0
#   2019-01-02  292.0
#   2019-01-03  309.0
#   2019-01-06  323.0
#   2019-01-07  321.0
```

## Get crypto data
The data is pulled from Binance, and all the available tickers are found [here](https://coinmarketcap.com/exchanges/binance/).

### Python

```
from fastquant import get_crypto_data
crypto = get_crypto_data("BTC/USDT", "2018-12-01", "2019-12-31")
crypto.head()

#             open    high     low     close    volume
# dt                                                          
# 2018-12-01  4041.27  4299.99  3963.01  4190.02  44840.073481
# 2018-12-02  4190.98  4312.99  4103.04  4161.01  38912.154790
# 2018-12-03  4160.55  4179.00  3827.00  3884.01  49094.369163
# 2018-12-04  3884.76  4085.00  3781.00  3951.64  48489.551613
# 2018-12-05  3950.98  3970.00  3745.00  3769.84  44004.799448
```

## Backtest trading strategies

### Simple Moving Average Crossover (15 day MA vs 40 day MA)
Daily Jollibee prices from 2018-01-01 to 2019-01-01
```
from fastquant import backtest
backtest('smac', df, fast_period=15, slow_period=40)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 102272.90
```
![](./docs/assets/smac_sample.png)

## Want to do this without coding at all?

If you want to make this kind of analysis even more simple without having to code at all (or want to avoid the pain of doing all of the setup required), you can signup for free and try out [Hawksight](https://hawksight.co/) - this new no-code tool I’m building to democratize data driven investments.

Hoping to make these kinds of powerful analyses accessible to more people!

## Optimize trading strategies with automated grid search

fastquant allows you to automatically measure the performance of your trading strategy on multiple combinations of parameters. All you need to do is to input the values as iterators (like as a `list` or `range`).

### Simple Moving Average Crossover (15 to 30 day MA vs 40 to 55 day MA)
Daily Jollibee prices from 2018-01-01 to 2019-01-01

```
from fastquant import backtest
res = backtest("smac", df, fast_period=range(15, 30, 3), slow_period=range(40, 55, 3), verbose=False)

# Optimal parameters: {'init_cash': 100000, 'buy_prop': 1, 'sell_prop': 1, 'execution_type': 'close', 'fast_period': 15, 'slow_period': 40}
# Optimal metrics: {'rtot': 0.022, 'ravg': 9.25e-05, 'rnorm': 0.024, 'rnorm100': 2.36, 'sharperatio': None, 'pnl': 2272.9, 'final_value': 102272.90}

print(res[['fast_period', 'slow_period', 'final_value']].head())

#	fast_period	slow_period	final_value
#0	15	        40	        102272.90
#1	21	        40	         98847.00
#2	21	        52	         98796.09
#3	24	        46	         98008.79
#4	15	        46	         97452.92

```

## Library of trading strategies

| Strategy | Alias | Parameters |
| --- | --- | --- |
| Relative Strength Index (RSI) | rsi | `rsi_period`, `rsi_upper`,  `rsi_lower` |
| Simple moving average crossover (SMAC) | smac | `fast_period`, `slow_period` |
| Exponential moving average crossover (EMAC) | emac | `fast_period`, `slow_period` |
| Moving Average Convergence Divergence (MACD) | macd | `fast_perod`, `slow_upper`, `signal_period`, `sma_period`, `dir_period` |
| Bollinger Bands | bbands | `period`, `devfactor` |
| Buy and Hold | buynhold | `N/A` |
| Sentiment Strategy | sentiment | `keyword` , `page_nums`, `senti` |
| Custom Prediction Strategy | custom | `upper_limit`, `lower_limit`, `custom_column` |
| Custom Ternary Strategy | ternary | `buy_int`, `sell_int`, `custom_column` |

### Relative Strength Index (RSI) Strategy
```
backtest('rsi', df, rsi_period=14, rsi_upper=70, rsi_lower=30)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 132967.87
```
![](./docs/assets/rsi.png)

### Simple moving average crossover (SMAC) Strategy
```
backtest('smac', df, fast_period=10, slow_period=30)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 95902.74
```
![](./docs/assets/smac.png)

### Exponential moving average crossover (EMAC) Strategy
```
backtest('emac', df, fast_period=10, slow_period=30)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 90976.00
```
![](./docs/assets/emac.png)

### Moving Average Convergence Divergence (MACD) Strategy
```
backtest('macd', df, fast_period=12, slow_period=26, signal_period=9, sma_period=30, dir_period=10)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 96229.58
```
![](./docs/assets/macd.png)

### Bollinger Bands Strategy
```
backtest('bbands', df, period=20, devfactor=2.0)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 97060.30
```
![](./docs/assets/bbands.png)

### News Sentiment Strategy
Use Tesla (TSLA) stock from yahoo finance and news articles from [Business Times](https://www.businesstimes.com.sg/)
```
from fastquant import get_yahoo_data, get_bt_news_sentiment
data = get_yahoo_data("TSLA", "2020-01-01", "2020-07-04")
sentiments = get_bt_news_sentiment(keyword="tesla", page_nums=3)
backtest("sentiment", data, sentiments=sentiments, senti=0.2)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 313198.37
# Note: Unfortunately, you can't recreate this scenario due to inconsistencies in the dates and sentiments that is scraped by get_bt_news_sentiment. In order to have a quickstart with News Sentiment Strategy you need to make the dates consistent with the sentiments that you are scraping.

from fastquant import get_yahoo_data, get_bt_news_sentiment
from datetime import datetime, timedelta

# we get the current date and delta time of 30 days
current_date = datetime.now().strftime("%Y-%m-%d")
delta_date = (datetime.now() - timedelta(30)).strftime("%Y-%m-%d")
data = get_yahoo_data("TSLA", delta_date, current_date)
sentiments = get_bt_news_sentiment(keyword="tesla", page_nums=3)
backtest("sentiment", data, sentiments=sentiments, senti=0.2)
```
![](./docs/assets/sentiment.png)

### Multi Strategy

Multiple registered strategies can be utilized together in an OR fashion, where buy or sell signals are applied when at least one of the strategies trigger them.

```
df = get_stock_data("JFC", "2018-01-01", "2019-01-01")

# Utilize single set of parameters
strats = { 
    "smac": {"fast_period": 35, "slow_period": 50}, 
    "rsi": {"rsi_lower": 30, "rsi_upper": 70} 
} 
res = backtest("multi", df, strats=strats)
res.shape
# (1, 16)


# Utilize auto grid search
strats_opt = { 
    "smac": {"fast_period": 35, "slow_period": [40, 50]}, 
    "rsi": {"rsi_lower": [15, 30], "rsi_upper": 70} 
} 

res_opt = backtest("multi", df, strats=strats_opt)
res_opt.shape
# (4, 16)
```

### Custom Strategy for Backtesting Machine Learning & Statistics Based Predictions

This powerful strategy allows you to backtest your own trading strategies using any type of model w/ as few as 3 lines of code after the forecast!

Predictions based on any model can be used as a custom indicator to be backtested using fastquant. You just need to add a `custom` column in the input dataframe, and set values for `upper_limit` and `lower_limit`.

The strategy is structured similar to `RSIStrategy` where you can set an `upper_limit`, above which the asset is sold (considered "overbought"), and a `lower_limit`, below which the asset is bought (considered "underbought). `upper_limit` is set to 95 by default, while `lower_limit` is set to 5 by default.

In the example below, we show how to use the custom strategy to backtest a custom indicator based on out-of-sample time series forecasts. The forecasts were generated using Facebook's [Prophet](https://github.com/facebook/prophet) package on Bitcoin prices.

```
from fastquant import get_crypto_data, backtest
from fbprophet import Prophet
import pandas as pd
from matplotlib import pyplot as plt

# Pull crypto data
df = get_crypto_data("BTC/USDT", "2019-01-01", "2020-05-31")

# Fit model on closing prices
ts = df.reset_index()[["dt", "close"]]
ts.columns = ['ds', 'y']
m = Prophet(daily_seasonality=True, yearly_seasonality=True).fit(ts)
forecast = m.make_future_dataframe(periods=0, freq='D')

# Predict and plot
pred = m.predict(forecast)
fig1 = m.plot(pred)
plt.title('BTC/USDT: Forecasted Daily Closing Price', fontsize=25)
```

![](./docs/assets/bitcoin_forecasts.png)

```
# Convert predictions to expected 1 day returns
expected_1day_return = pred.set_index("ds").yhat.pct_change().shift(-1).multiply(100)

# Backtest the predictions, given that we buy bitcoin when the predicted next day return is > +1.5%, and sell when it's < -1.5%.
df["custom"] = expected_1day_return.multiply(-1)
backtest("custom", df.dropna(),upper_limit=1.5, lower_limit=-1.5)
```

![](./docs/assets/bitcoin_prophet_backtest.png)

See more examples [here](https://nbviewer.jupyter.org/github/enzoampil/fastquant/tree/master/examples/).

## fastquant API
View full list of fastquan API [here](API.md)

## Be part of the growing fastquant community

Want to discuss more about fastquant with other users, and our team of developers?

You can reach us on the [Hawksight discord](https://discord.gg/BHMCw2C6VP). Feel free to ask about fastquant in the #feedback-suggestions and #bug-report channels.

## Run fastquant in a Docker Container

```
# Build the image
docker build -t myimage .

# Run the container
docker run -t -d -p 5000:5000 myimage

# Get the container id
docker ps

# SSH into the fastquant container
docker exec -it <CONTAINER_ID> /bin/bash

# Run python and use fastquant
python

>>> from fastquant import get_stock_data
>>> df = get_stock_data("TSLA", "2019-01-01", "2020-01-01")
>>> df.head()
```

### Core Implementation Code & Architecture
#### File: `python/tests/__init__.py`
```python

```

#### File: `python/fastquant/utils/__init__.py`
```python

```

#### File: `python/fastquant/data/crypto/__init__.py`
```python

```

#### File: `python/fastquant/data/web/__init__.py`
```python

```

#### File: `python/fastquant/data/stocks/__init__.py`
```python

```

#### File: `python/fastquant/backtest/__init__.py`
```python
# Modules available for fastquant.backtest.*

from fastquant.backtest.backtest import backtest
from fastquant.backtest.backtest import STRATEGY_MAPPING
```


==================================================


## [2/3] Repository: fd (`WHEEL_fd`)
- **Full Name**: `fd`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# fd

[![CICD](https://github.com/sharkdp/fd/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/fd/actions/workflows/CICD.yml)
[![Version info](https://img.shields.io/crates/v/fd-find.svg)](https://crates.io/crates/fd-find)
[[中文](https://github.com/cha0ran/fd-zh)]
[[한국어](https://github.com/spearkkk/fd-kor)]

`fd` is a program to find entries in your filesystem.
It is a simple, fast and user-friendly alternative to [`find`](https://www.gnu.org/software/findutils/).
While it does not aim to support all of `find`'s powerful functionality, it provides sensible
(opinionated) defaults for a majority of use cases.

[Installation](#installation) • [How to use](#how-to-use) • [Troubleshooting](#troubleshooting)

## Features

* Intuitive syntax: `fd PATTERN` instead of `find -iname '*PATTERN*'`.
* Regular expression (default) and glob-based patterns.
* [Very fast](#benchmark) due to parallelized directory traversal.
* Uses colors to highlight different file types (same as `ls`).
* Supports [parallel command execution](#command-execution)
* Smart case: the search is case-insensitive by default. It switches to
  case-sensitive if the pattern contains an uppercase
  character[\*](http://vimdoc.sourceforge.net/htmldoc/options.html#'smartcase').
* Ignores hidden directories and files, by default.
* Ignores patterns from your `.gitignore`, by default.
* The command name is *50%* shorter[\*](https://github.com/ggreer/the_silver_searcher) than
  `find` :-).

## Demo

![Demo](doc/screencast.svg)

## How to use

First, to get an overview of all available command line options, you can either run
[`fd -h`](#command-line-options) for a concise help message or `fd --help` for a more detailed
version.

### Simple search

*fd* is designed to find entries in your filesystem. The most basic search you can perform is to
run *fd* with a single argument: the search pattern. For example, assume that you want to find an
old script of yours (the name included `netflix`):
``` bash
> fd netfl
Software/python/imdb-ratings/netflix-details.py
```
If called with just a single argument like this, *fd* searches the current directory recursively
for any entries that *contain* the pattern `netfl`.

### Regular expression search

The search pattern is treated as a regular expression. Here, we search for entries that start
with `x` and end with `rc`:
``` bash
> cd /etc
> fd '^x.*rc$'
X11/xinit/xinitrc
X11/xinit/xserverrc
```

The regular expression syntax used by `fd` is [documented here](https://docs.rs/regex/latest/regex/#syntax).

### Specifying the root directory

If we want to search a specific directory, it can be given as a second argument to *fd*:
``` bash
> fd passwd /etc
/etc/default/passwd
/etc/pam.d/passwd
/etc/passwd
```

### List all files, recursively

*fd* can be called with no arguments. This is very useful to get a quick overview of all entries
in the current directory, recursively (similar to `ls -R`):
``` bash
> cd fd/tests
> fd
testenv
testenv/mod.rs
tests.rs
```

If you want to use this functionality to list all files in a given directory, you have to use
a catch-all pattern such as `.` or `^`:
``` bash
> fd . fd/tests/
testenv
testenv/mod.rs
tests.rs
```

### Searching for a particular file extension

Often, we are interested in all files of a particular type. This can be done with the `-e` (or
`--extension`) option. Here, we search for all Markdown files in the fd repository:
``` bash
> cd fd
> fd -e md
CONTRIBUTING.md
README.md
```

The `-e` option can be used in combination with a search pattern:
``` bash
> fd -e rs mod
src/fshelper/mod.rs
src/lscolors/mod.rs
tests/testenv/mod.rs
```

### Searching for a particular file name

 To find files with exactly the provided search pattern, use the `-g` (or `--glob`) option:
``` bash
> fd -g libc.so /usr
/usr/lib32/libc.so
/usr/lib/libc.so
```

### Hidden and ignored files
By default, *fd* does not search hidden directories and does not show hidden files in the
search results. To disable this behavior, we can use the `-H` (or `--hidden`) option:
``` bash
> fd pre-commit
> fd -H pre-commit
.git/hooks/pre-commit.sample
```

If we work in a directory that is a Git repository (or includes Git repositories), *fd* does not
search folders (and does not show files) that match one of the `.gitignore` patterns. To disable
this behavior, we can use the `-I` (or `--no-ignore`) option:
``` bash
> fd num_cpu
> fd -I num_cpu
target/debug/deps/libnum_cpus-f5ce7ef99006aa05.rlib
```

To really search *all* files and directories, simply combine the hidden and ignore features to show
everything (`-HI`) or use `-u`/`--unrestricted`.

### Matching the full path
By default, *fd* only matches the filename of each file. However, using the `--full-path` or `-p` option,
you can match against the full path.

```bash
> fd -u -p -g '**/.git/config'
> fd -p '.*/lesson-\d+/[a-z]+.(jpg|png)'
```

### Command execution

Instead of just showing the search results, you often want to *do something* with them. `fd`
provides two ways to execute external commands for each of your search results:

* The `-x`/`--exec` option runs an external command *for each of the search results* (in parallel).
* The `-X`/`--exec-batch` option launches the external command once, with *all search results as arguments*.

#### Examples

Recursively find all zip archives and unpack them:
``` bash
fd -e zip -x unzip
```
If there are two such files, `file1.zip` and `backup/file2.zip`, this would execute
`unzip file1.zip` and `unzip backup/file2.zip`. The two `unzip` processes run in parallel
(if the files are found fast enough).

Find all `*.h` and `*.cpp` files and auto-format them inplace with `clang-format -i`:
``` bash
fd -e h -e cpp -x clang-format -i
```
Note how the `-i` option to `clang-format` can be passed as a separate argument. This is why
we put the `-x` option last.

Any positional arguments after `-x` belong to the command template, not to `fd` itself. If you
also want to pass a pattern or search path, put `-x` last:
``` bash
fd pattern path -x echo
```

Find all `test_*.py` files and open them in your favorite editor:
``` bash
fd -g 'test_*.py' -X vim
```
Note that we use capital `-X` here to open a single `vim` instance. If there are two such files,
`test_basic.py` and `lib/test_advanced.py`, this will run `vim test_basic.py lib/test_advanced.py`.

To see details like file permissions, owners, file sizes etc., you can tell `fd` to show them
by running `ls` for each result:
``` bash
fd … -X ls -lhd --color=always
```
This pattern is so useful that `fd` provides a shortcut. You can use the `-l`/`--list-details`
option to execute `ls` in this way: `fd … -l`.

The `-X` option is also useful when combining `fd` with [ripgrep](https://github.com/BurntSushi/ripgrep/) (`rg`) in order to search within a certain class of files, like all C++ source files:
```bash
fd -e cpp -e cxx -e h -e hpp -X rg 'std::cout'
```

Convert all `*.jpg` files to `*.png` files:
``` bash
fd -e jpg -x convert {} {.}.png
```
Here, `{}` is a placeholder for the search result. `{.}` is the same, without the file extension.
See below for more details on the placeholder syntax.

The terminal output of commands run from parallel threads using `-x` will not be interlaced or garbled,
so `fd -x` can be used to rudimentarily parallelize a task run over many files.
An example of this is calculating the checksum of each individual file within a directory.
``` bash
fd -tf -x md5sum > file_checksums.txt
```

#### Placeholder syntax

The `-x` and `-X` options take a *command template* as a series of arguments (instead of a single string).
If you want to add additional options to `fd` after the command template, you can terminate it with a `\;`.

For example, `fd -x echo \; pattern path` treats `pattern path` as `fd` arguments instead of
passing them to `echo`. In practice, it is often clearer to write `fd pattern path -x echo`.

The syntax for generating commands is similar to that of [GNU Parallel](https://www.gnu.org/software/parallel/):

- `{}`: A placeholder token that will be replaced with the path of the search result
  (`documents/images/party.jpg`).
- `{.}`: Like `{}`, but without the file extension (`documents/images/party`).
- `{/}`: A placeholder that will be replaced by the basename of the search result (`party.jpg`).
- `{//}`: The parent of the discovered path (`documents/images`).
- `{/.}`: The basename, with the extension removed (`party`).

If you do not include a placeholder, *fd* automatically adds a `{}` at the end.

#### Parallel vs. serial execution

For `-x`/`--exec`, you can control the number of parallel jobs by using the `-j`/`--threads` option.
Use `--threads=1` for serial execution.

### Excluding specific files or directories

Sometimes we want to ignore search results from a specific subdirectory. For example, we might
want to search all hidden files and directories (`-H`) but exclude all matches from `.git`
directories. We can use the `-E` (or `--exclude`) option for this. It takes an arbitrary glob
pattern as an argument:
``` bash
> fd -H -E .git …
```

We can also use this to skip mounted directories:
``` bash
> fd -E /mnt/external-drive …
```

.. or to skip certain file types:
``` bash
> fd -E '*.bak' …
```

To make exclude-patterns like these permanent, you can create a `.fdignore` file. They work like
`.gitignore` files, but are specific to `fd`. For example:
``` bash
> cat ~/.fdignore
/mnt/external-drive
*.bak
```

> [!NOTE]
> `fd` also supports `.ignore` files that are used by other programs such as `rg` or `ag`.

If you want `fd` to ignore these patterns globally, you can put them in `fd`'s global ignore file.
This is usually located in `~/.config/fd/ignore` in macOS or Linux, and `%APPDATA%\fd\ignore` in
Windows.

You may wish to include `.git/` in your `fd/ignore` file so that `.git` directories, and their contents
are not included in output if you use the `--hidden` option.

### Deleting files

You can use `fd` to remove all files and directories that are matched by your search pattern.
If you only want to remove files, you can use the `--exec-batch`/`-X` option to call `rm`. For
example, to recursively remove all `.DS_Store` files, run:
``` bash
> fd -H '^\.DS_Store$' -tf -X rm
```
If you are unsure, always call `fd` without `-X rm` first. Alternatively, use `rm`s "interactive"
option:
``` bash
> fd -H '^\.DS_Store$' -tf -X rm -i
```

If you also want to remove a certain class of directories, you can use the same technique. You will
have to use `rm`s `--recursive`/`-r` flag to remove directories.

> [!NOTE]
> There are scenarios where using `fd … -X rm -r` can cause race conditions: if you have a
path like `…/foo/bar/foo/…` and want to remove all directories named `foo`, you can end up in a
situation where the outer `foo` directory is removed first, leading to (harmless) *"'foo/bar/foo':
No such file or directory"* errors in the `rm` call.

### Command-line options

This is the output of `fd -h`. To see the full set of command-line options, use `fd --help` which
also includes a much more detailed help text.

```
Usage: fd [OPTIONS] [pattern [path]...]

Arguments:
  [pattern]  the search pattern (a regular expression, unless '--glob' is used; optional)
  [path]...  the root directories for the filesystem search (optional)

Options:
  -H, --hidden                     Search hidden files and directories
  -I, --no-ignore                  Do not respect .(git|fd)ignore files
  -s, --case-sensitive             Case-sensitive search (default: smart case)
  -i, --ignore-case                Case-insensitive search (default: smart case)
  -g, --glob                       Glob-based search (default: regular expression)
  -a, --absolute-path              Show absolute instead of relative paths
  -l, --list-details               Use a long listing format with file metadata
  -L, --follow                     Follow symbolic links
  -p, --full-path                  Search full abs. path (default: filename only)
  -d, --max-depth <depth>          Set maximum search depth (default: none)
  -E, --exclude <glob>             Exclude entries that match the given glob pattern
  -t, --type <filetype>            Filter by type: file (f), directory (d/dir), symlink (l),
                                   executable (x), empty (e), socket (s), pipe (p), char-device
                                   (c), block-device (b)
  -e, --extension <ext>            Filter by extension
  -S, --size <size>                Limit results based on the size of files
      --changed-within <date|dur>  Filter by file modification time (newer than)
      --changed-before <date|dur>  Filter by file modification time (older than)
  -o, --owner <user:group>         Filter by owning user and/or group
      --format <fmt>               Print results according to template
  -x, --exec <cmd>...              Execute a command for each search result
  -X, --exec-batch <cmd>...        Execute a command with all search results at once
  -c, --color <when>               When to use colors [default: auto] [possible values: auto,
                                   always, never]
      --hyperlink[=<when>]         Add hyperlinks to output paths [default: never] [possible
                                   values: auto, always, never]
      --ignore-contain <name>      Ignore directories containing the named entry
  -h, --help                       Print help (see more with '--help')
  -V, --version                    Print version
```

Note that options can be given after the pattern and/or path as well.

## Benchmark

Let's search my home folder for files that end in `[0-9].jpg`. It contains ~750,000
subdirectories and about a 4 million files. For averaging and statistical analysis, I'm using
[hyperfine](https://github.com/sharkdp/hyperfine). The following benchmarks are performed
with a "warm"/pre-filled disk-cache (results for a "cold" disk-cache show the same trends).

Let's start with `find`:
```
Benchmark 1: find ~ -iregex '.*[0-9]\.jpg$'
  Time (mean ± σ):     19.922 s ±  0.109 s
  Range (min … max):   19.765 s … 20.065 s
```

`find` is much faster if it does not need to perform a regular-expression search:
```
Benchmark 2: find ~ -iname '*[0-9].jpg'
  Time (mean ± σ):     11.226 s ±  0.104 s
  Range (min … max):   11.119 s … 11.466 s
```

Now let's try the same for `fd`. Note that `fd` performs a regular expression
search by default. The options `-u`/`--unrestricted` option is needed here for
a fair comparison. Otherwise `fd` does not have to traverse hidden folders and
ignored paths (see below):
```
Benchmark 3: fd -u '[0-9]\.jpg$' ~
  Time (mean ± σ):     854.8 ms ±  10.0 ms
  Range (min … max):   839.2 ms … 868.9 ms
```
For this particular example, `fd` is approximately **23 times faster** than `find -iregex`
and about **13 times faster** than `find -iname`. By the way, both tools found the exact
same 546 files :smile:.

**Note**: This is *one particular* benchmark on *one particular* machine. While we have
performed a lot of different tests (and found consistent results), things might
be different for you! We encourage everyone to try it out on their own. See
[this repository](https://github.com/sharkdp/fd-benchmarks) for all necessary scripts.

Concerning *fd*'s speed, a lot of credit goes to the `regex` and `ignore` crates that are
also used in [ripgrep](https://github.com/BurntSushi/ripgrep) (check it out!).

## Troubleshooting

### `fd` does not find my file!

Remember that `fd` ignores hidden directories and files by default. It also ignores patterns
from `.gitignore` files. If you want to make sure to find absolutely every possible file, always
use the options `-u`/`--unrestricted` option (or `-HI` to enable hidden and ignored files):
``` bash
> fd -u …
```

Also remember that by default, `fd` only searches based on the filename and
doesn't compare the pattern to the full path. If you want to search based on the
full path (similar to the `-path` option of `find`) you need to use the `--full-path`
(or `-p`) option.

### Colorized output

`fd` can colorize files by extension, just like `ls`. In order for this to work, the environment
variable [`LS_COLORS`](https://linux.die.net/man/5/dir_colors) has to be set. Typically, the value
of this variable is set by the `dircolors` command which provides a convenient configuration format
to define colors for different file formats.
On most distributions, `LS_COLORS` should be set already. If you are on Windows or if you are looking
for alternative, more complete (or more colorful) variants, see [here](https://github.com/sharkdp/vivid),
[here](https://github.com/seebi/dircolors-solarized) or
[here](https://github.com/trapd00r/LS_COLORS).

`fd` also honors the [`NO_COLOR`](https://no-color.org/) environment variable.

### `fd` doesn't seem to interpret my regex pattern correctly

A lot of special regex characters (like `[]`, `^`, `$`, ..) are also special characters in your
shell. If in doubt, always make sure to put single quotes around the regex pattern:

``` bash
> fd '^[A-Z][0-9]+$'
```

If your pattern starts with a dash, you have to add `--` to signal the end of command line
options. Otherwise, the pattern will be interpreted as a command-line option. Alternatively,
use a character class with a single hyphen character:

``` bash
> fd -- '-pattern'
> fd '[-]pattern'
```

### "Command not found" for `alias`es or shell functions

Shell `alias`es and shell functions can not be used for command execution via `fd -x` or
`fd -X`. In `zsh`, you can make the alias global via `alias -g myalias="…"`. In `bash`,
you can use `export -f my_function` to make available to child processes. You would still
need to call `fd -x bash -c 'my_function "$1"' bash`. For other use cases or shells, use
a (temporary) shell script.

### Placeholders in `-x`/`-X`

Depending on your shell, you may need to quote the placeholders (`{}`, `{/}`, `{//}`,
`{.}`, `{/.}`) to prevent the shell from interpreting them before `fd` sees them.

## Integration with other programs

### Using fd with `fzf`

You can use *fd* to generate input for the command-line fuzzy finder [fzf](https://github.com/junegunn/fzf):
``` bash
export FZF_DEFAULT_COMMAND='fd --type file'
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
```

Then, you can type `vim <Ctrl-T>` on your terminal to open fzf and search through the fd-results.

Alternatively, you might like to follow symbolic links and include hidden files (but exclude `.git` folders):
``` bash
export FZF_DEFAULT_COMMAND='fd --type file --follow --hidden --exclude .git'
```

You can even use fd's colored output inside fzf by setting:
``` bash
export FZF_DEFAULT_COMMAND="fd --type file --color=always"
export FZF_DEFAULT_OPTS="--ansi"
```

For more details, see the [Tips section](https://github.com/junegunn/fzf#tips) of the fzf README.

### Using fd with `rofi`

[*rofi*](https://github.com/davatorium/rofi) is a graphical launch menu application that is able to create menus by reading from *stdin*. Piping `fd` output into `rofi`s `-dmenu` mode creates fuzzy-searchable lists of files and directories.

#### Example

Create a case-insensitive searchable multi-select list of *PDF* files under your `$HOME` directory and open the selection with your configured PDF viewer. To list all file types, drop the `-e pdf` argument.

``` bash
fd --type f -e pdf . $HOME | rofi -keep-right -dmenu -i -p FILES -multi-select | xargs -I {} xdg-open {}
```

To modify the list that is presented by rofi, add arguments to the `fd` command. To modify the search behaviour of rofi, add arguments to the `rofi` command.

### Using fd with `emacs`

The emacs package [find-file-in-project](https://github.com/technomancy/find-file-in-project) can
use *fd* to find files.

After installing `find-file-in-project`, add the line `(setq ffip-use-rust-fd t)` to your
`~/.emacs` or `~/.emacs.d/init.el` file.

In emacs, run `M-x find-file-in-project-by-selected` to find matching files. Alternatively, run
`M-x find-file-in-project` to list all available files in the project.

### Printing the output as a tree

To format the output of `fd` as a file-tree you can use the `tree` command with
`--fromfile`:
```bash
❯ fd | tree --fromfile
```

This can be more useful than running `tree` by itself because `tree` does not
ignore any files by default, nor does it support as rich a set of options as
`fd` does to control what to print:
```bash
❯ fd --extension rs | tree --fromfile
.
├── build.rs
└── src
    ├── app.rs
    └── error.rs
```

On bash and similar you can simply create an alias:
```bash
❯ alias as-tree='tree --fromfile'
```

### Using fd with `xargs` or `parallel`

Note that `fd` has a builtin feature for [command execution](#command-execution) with
its `-x`/`--exec` and `-X`/`--exec-batch` options. If you prefer, you can still use
it in combination with `xargs`:
``` bash
> fd -0 -e rs | xargs -0 wc -l
```
Here, the `-0` option tells *fd* to separate search results by the NULL character (instead of
newlines). In the same way, the `-0` option of `xargs` tells it to read the input in this way.

## Installation

[![Packaging status](https://repology.org/badge/vertical-allrepos/fd-find.svg)](https://repology.org/project/fd-find/versions)

### On Ubuntu
*... and other Debian-based Linux distributions.*

If you run Ubuntu 19.04 (Disco Dingo) or newer, you can install the
[officially maintained package](https://packages.ubuntu.com/fd-find):
```
apt install fd-find
```
Note that the binary is called `fdfind` as the binary name `fd` is already used by another package.
It is recommended that after installation, you add a link to `fd` by executing command
`ln -s $(which fdfind) ~/.local/bin/fd`, in order to use `fd` in the same way as in this documentation.
Make sure that `$HOME/.local/bin` is in your `$PATH`.

If you use an older version of Ubuntu, you can download the latest `.deb` package from the
[release page](https://github.com/sharkdp/fd/releases) and install it via:
``` bash
dpkg -i fd_9.0.0_amd64.deb # adapt version number and architecture
```

Note that the .deb packages on the release page for this project still name the executable `fd`.

### On Debian

If you run Debian Buster or newer, you can install the
[officially maintained Debian package](https://tracker.debian.org/pkg/rust-fd-find):
```
apt-get install fd-find
```
Note that the binary is called `fdfind` as the binary name `fd` is already used by another package.
It is recommended that after installation, you add a link to `fd` by executing command
`ln -s $(which fdfind) ~/.local/bin/fd`, in order to use `fd` in the same way as in this documentation.
Make sure that `$HOME/.local/bin` is in your `$PATH`.

Note that the .deb packages on the release page for this project still name the executable `fd`.

### On Fedora

Starting with Fedora 28, you can install `fd` from the official package sources:
``` bash
dnf install fd-find
```

### On Alpine Linux

You can install [the fd package](https://pkgs.alpinelinux.org/packages?name=fd)
from the official sources, provided you have the appropriate repository enabled:
```
apk add fd
```

### On Arch Linux

You can install [the fd package](https://www.archlinux.org/packages/extra/x86_64/fd/) from the official repos:
```
pacman -S fd
```
You can also install fd [from the AUR](https://aur.archlinux.org/packages/fd-git).

### On Gentoo Linux

You can use [the fd ebuild](https://packages.gentoo.org/packages/sys-apps/fd) from the official repo:
```
emerge -av fd
```

### On openSUSE Linux

You can install [the fd package](https://software.opensuse.org/package/fd) from the official repo:
```
zypper in fd
```

### On Void Linux

You can install `fd` via xbps-install:
```
xbps-install -S fd
```

### On ALT Linux

You can install [the fd package](https://packages.altlinux.org/en/sisyphus/srpms/fd/) from the official repo:
```
apt-get install fd
```

### On Solus

You can install [the fd package](https://github.com/getsolus/packages/tree/main/packages/f/fd) from the official repo:
```
eopkg install fd
```

### On RedHat Enterprise Linux (RHEL) 8/9/10, Almalinux 8/9/10, EuroLinux 8/9 or Rocky Linux 8/9/10

You can install [the `fd` package](https://copr.fedorainfracloud.org/coprs/tkbcopr/fd/) from Fedora Copr.

```bash
dnf copr enable tkbcopr/fd
dnf install fd
```

A different version using the [slower](https://github.com/sharkdp/fd/pull/481#issuecomment-534494592) malloc [instead of jemalloc](https://bugzilla.redhat.com/show_bug.cgi?id=2216193#c1) is also available from the EPEL8/9 repo as the package `fd-find`.

### On macOS

You can install `fd` with [Homebrew](https://formulae.brew.sh/formula/fd):
```
brew install fd
```

… or with MacPorts:
```
port install fd
```

### On Windows

You can download pre-built binaries from the [release page](https://github.com/sharkdp/fd/releases).

Alternatively, you can install `fd` via [Scoop](http://scoop.sh):
```
scoop install fd
```

Or via [Chocolatey](http
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `rustfmt.toml`
```python
# Defaults are used
```

#### File: `src/error.rs`
```python
pub fn print_error(msg: impl std::fmt::Display) {
    eprintln!("[fd error]: {msg}");
}
```

#### File: `src/filter/mod.rs`
```python
pub use self::size::SizeFilter;
pub use self::time::TimeFilter;

#[cfg(unix)]
pub use self::owner::OwnerFilter;

mod size;
mod time;

#[cfg(unix)]
mod owner;
```

#### File: `Cross.toml`
```python
# https://github.com/sharkdp/fd/issues/1085
[target.aarch64-unknown-linux-gnu.env]
passthrough = ["JEMALLOC_SYS_WITH_LG_PAGE=16"]

[target.aarch64-unknown-linux-musl.env]
passthrough = ["JEMALLOC_SYS_WITH_LG_PAGE=16"]
```

#### File: `.cargo/config.toml`
```python
# On Windows MSVC, statically link the C runtime so that the resulting EXE does
# not depend on the vcruntime DLL.
#
# See: https://github.com/sharkdp/fd/issues/1874

[target.x86_64-pc-windows-msvc]
rustflags = ["-C", "target-feature=+crt-static"]
[target.i686-pc-windows-msvc]
rustflags = ["-C", "target-feature=+crt-static"]
```

#### File: `src/filetypes.rs`
```python
use crate::dir_entry;
use crate::filesystem;

use faccess::PathExt;

/// Whether or not to show
#[derive(Default)]
pub struct FileTypes {
    pub files: bool,
    pub directories: bool,
    pub symlinks: bool,
    pub block_devices: bool,
    pub char_devices: bool,
    pub sockets: bool,
    pub pipes: bool,
    pub executables_only: bool,
    pub empty_only: bool,
}

impl FileTypes {
    pub fn should_ignore(&self, entry: &dir_entry::DirEntry) -> bool {
        if let Some(ref entry_type) = entry.file_type() {
            (!self.files && entry_type.is_file())
                || (!self.directories && entry_type.is_dir())
                || (!self.symlinks && entry_type.is_symlink())
                || (!self.block_devices && filesystem::is_block_device(*entry_type))
                || (!self.char_devices && filesystem::is_char_device(*entry_type))
                || (!self.sockets && filesystem::is_socket(*entry_type))
                || (!self.pipes && filesystem::is_pipe(*entry_type))
                || (self.executables_only && !entry.path().executable())
                || (self.empty_only && !filesystem::is_empty(entry))
                || !(entry_type.is_file()
                    || entry_type.is_dir()
                    || entry_type.is_symlink()
                    || filesystem::is_block_device(*entry_type)
                    || filesystem::is_char_device(*entry_type)
                    || filesystem::is_socket(*entry_type)
                    || filesystem::is_pipe(*entry_type))
        } else {
            true
        }
    }
}
```


==================================================


## [3/3] Repository: findatapy (`WHEEL_findatapy`)
- **Full Name**: `findatapy`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<img src="findatapy_logo.png?raw=true" width="300"/>

# [findatapy](https://github.com/cuemacro/findatapy)

[![Downloads](https://pepy.tech/badge/findatapy)](https://pepy.tech/project/findatapy)

findatapy creates an easy to use Python API to download market data from many sources including ALFRED/FRED, Bloomberg, Yahoo, Google etc. using
a unified high level interface. Users can also define their own custom tickers, using configuration files. There is also functionality which
is particularly useful for those downloading FX market data. Below example shows how to download AUDJPY data from Quandl (and automatically 
calculates this via USD crosses).

*Contributors for the project are very much welcome, see below!*

```
from findatapy.market import Market, MarketDataRequest, MarketDataGenerator

market = Market(market_data_generator=MarketDataGenerator())

# Get you FRED API key from https://fred.stlouisfed.org/docs/api/api_key.html
fred_api_key = "WRITE YOUR KEY HERE" 

md_request = MarketDataRequest(start_date='year', category='fx', data_source='alfred', tickers=['AUDJPY'],
                               fred_api_key=fred_api_key)

df = market.fetch_market(md_request)
print(df.tail(n=10))
```

Here we see how to download tick data from DukasCopy, wih the same API calls and minimal changes in the code.

```
md_request = MarketDataRequest(start_date='14 Jun 2016', finish_date='15 Jun 2016',
                                   category='fx', fields=['bid', 'ask'], freq='tick', 
                                   data_source='dukascopy', tickers=['EURUSD'])

df = market.fetch_market(md_request)
print(df.tail(n=10))
```

I had previously written the open source PyThalesians financial library. This new findatapy library has similar functionality to the 
market data part of that library. However, I've totally rewritten the API to make it much cleaner and easier to use. It is also now a fully
standalone package, so you can more easily use it with whatever libraries you have for analysing market data or doing your backtesting (although I'd recommend
my own finmarketpy package if you are doing backtesting of trading strategies!).

A few things to note:
* Please bear in mind at present findatapy is currently a highly experimental alpha project and isn't yet fully 
documented
* Uses Apache 2.0 licence

# Contributors

Contributors are always welcome for finmarketpy, findatapy and chartpy. If you'd like to contribute, have a look at
[Planned Features](PLANNED_FEATURES.md) for areas we're looking for help on. Or if you have any ideas for improvements
to the libriares please let us know too!

# Gallery

To appear

# Requirements

Major requirements
* Required: Python 3.10 (Python 2 is not supported)
* Required: pandas, numpy etc.
* Recommended: blpapi - Bloomberg Python Open API - install by separately running `pip install --index-url=https://blpapi.bloomberg.com/repository/releases/python/simple blpapi`
* Recommended: chartpy - for funky interactive plots ([https://github.com/cuemacro/chartpy](https://github.com/cuemacro/chartpy)) and

# Installation

For detailed installation instructions for chartpy, findatapy & finmarketpy and its associated Python libraries go to
[https://github.com/cuemacro/finmarketpy/blob/master/INSTALL.md](https://github.com/cuemacro/finmarketpy/blob/master/INSTALL.md). The tutorial includes details on how to setup your entire Python environment.

You can install the library using the below. After installation:
* Make sure you edit the dataconstants class for the correct Eikon API, Quandl API and Twitter API keys etc.
* Or you can run set_api_keys.py script to set the API keys via storing in your keyring
* Or you can create a datacred.py file which overwrites these keys
* Or some of these API keys can be passed via MarketDataRequest on demand

To install via pip (latest release):
```
pip install findatapy
```

To install newest repo copy:
```
pip install git+https://github.com/cuemacro/findatapy.git
```

# Couldn't push MarketDataRequest message

You might often get an error like the below, when you are downloading market data with
findatapy, and you don't have Redis installed.

```
Couldn't push MarketDataRequest
```

findatapy includes an in-memory caching mechanism, which uses Redis
a key/value in-memory store. The idea is that if we do exactly the same data download
call with the same parameters of a MarketDataRequest it will check this volatile cache
first, before going out to our external data provider (eg. Quandl).

Note, that Redis is usually set up as volatile cache, so once your computer is turned off, this cache
will be lost.

If Redis is not installed, this caching will fail and you'll
get this error. However, all other functionality aside from the caching will be fine. All
findatapy will do is to always go externally to download market data. Redis is available for Linux.
There is also an unsupported (older) Windows version available, which I've found works fine, 
although it lacks some functionality of later Redis versions.

# findatapy examples

In findatapy/examples you will find several demos on how to download data from many different sources. Note, 
for some such as Bloomberg or Eikon, you'll need to have a licence/subscription for it to work. Also there might be 
certain limits of the history you can download for intraday data from certain sources (you will need to check with
individual data providers)

# Release Notes

* 0.1.42 - findatapy (20 Mar 2026)
* 0.1.41 - findatapy (02 Jan 2026)
* 0.1.40 - findatapy (08 Mar 2025)
* 0.1.39 - findatapy (08 Mar 2025)
* 0.1.38 - findatapy (19 Feb 2025)
* 0.1.37 - findatapy (15 Jan 2025)
* 0.1.36 - findatapy (27 Apr 2024)
* 0.1.35 - findatapy (10 Apr 2024)
* 0.1.34 - findatapy (08 Apr 2024)
* 0.1.33 - findatapy (01 Apr 2024)
* 0.1.32 - findatapy (17 Feb 2024)
* 0.1.31 - findatapy (01 Dec 2023)
* 0.1.30 - findatapy (12 Oct 2023)
* 0.1.29 - findatapy (14 May 2023)
* 0.1.28 - findatapy (19 Jul 2022)
* 0.1.27 - findatapy (20 May 2022)
* 0.1.26 - findatapy (07 Oct 2021)
* 0.1.25 - findatapy (07 Oct 2021)
* 0.1.24 - findatapy (06 Oct 2021)
* 0.1.23 - findatapy (03 Jun 2021)
* 0.1.22 - findatapy (01 Jun 2021)
* 0.1.21 - findatapy (04 May 2021)
* 0.1.20 - findatapy (11 Feb 2021)
* 0.1.19 - findatapy (22 Jan 2021)
* 0.1.18 - findatapy (02 Oct 2020)
* 0.1.17 - findatapy (01 Oct 2020)
* 0.1.16 - findatapy (13 Sep 2020)
* 0.1.15 - findatapy (10 Sep 2020)
* 0.1.14 - findatapy (25 Aug 2020)
* 0.1.13 - findatapy (24 Aug 2020)
* 0.1.12 - findatapy (06 May 2020)

# Coding log

* 02 Jul 2027
  * Added error messages around Parquet reading
* 11 Apr 2026
  * Changed s3 so it uses pyarrow instead of s3fs, so can use Python 3.14
* 27 Mar 2026
  * Added UTC default for timezone in get_file_properties in IOEngine & tests
* 20 Mar 2026
  * Improved caching of Parquet files in IOEngine (and via MarketDataRequest)
* 11 Jan 2026
  * Speeding up ticker parsing in ConfigManager
* 02 Jan 2026
  * Refactored ConfigManager so it can take DataFrames as input (not just CSVs)
* 29 Oct 2025
  * Added flag for conversion of datetime in IOEngine
* 18 Jul 2025
  * Speeded up Redis read/write of DataFrames
* 08 Mar 2025
  * Fixed various deprecation warnings for Pandas
* 19 Feb 2025
  * Fixed bug with Yahoo
* 15 Jan 2024
  * Fixed various issues accessing data on s3 related to credentials
* 09 Nov 2024
  * Added ALFRED/FRED FX tickers to time series mapping CSV files
  * Fixed bug when downloading ALFRED/FRED FX tickers
  * Added intraday downloading for Yahoo (and example for FX)
  * Refactored out crypto downloaders into datavendorcrypto.py
  * Refactored out ALFRED/FRED into datavendorfred.py
  * Starting to add Databento Historical API
  * Fixed deprecation error in calculations.py for 
* 27 Apr 2024
  * Removed additional list typecheck (to make code Python 3.8 compatible)
* 09 Apr 2024
  * Bugfix for reading Parquet files with columns
* 08 Apr 2024
  * Removed list typecheck (to make code Python 3.8 compatible)
* 01 Apr 2024
  * Added support for ArcticDB to store market data with findatapy
* 17 Feb 2024
  * Fixed ALFRED/FRED wrapper so now compatible with Python 3.10
* 01 Dec 2023
  * Remove fxcmpy dependency (package no longer exists?)
  * Added type hinting in ioengine.py
* 26 Jul 2023
  * Fixed overrides for BBG
* 12 May 2023
  * Fixed Dukascopy downloader
* 29 Aug 2022
  * Reformatted text for line length
* 23 Aug 2022
  * Simplified MarketDataRequest
* 12 Aug 2022
  * Minor changes in MarketDataGenerator for non-standard columns
* 11 Aug 2022
  * Fixed various bug in MarketDataRequest, when updating constants and 
  freeform str ticker queries with kwargs
* 19 Jul 2022
  * Various fixes for data download
* 20 May 2022
  * Added more customisation for data vendors
* 25 Jan 2022
  * Fixed delete key problem with Redis
* 20 Jan 2022
  * Fixed path join for s3
* 17 Jan 2022
  * Fixed bug in BBG wrapper
* 16 Jan 2022
  * Started to refactor code for PEP8 standards
  * Added BBG tests
* 15 Jan 2022
  * Changed read/write on Redis to use Pickle instead of Arrow
* 14 Dec 2021
  * Fixed bug in overrides for BBG
  * Patched ticker for EUR1Y deposit rate
* 07 Oct 2021
  * Fixed bug in downloading data for unusual categories 
  * Fixed missing ticker in time_series_tickers.csv
* 27 Sep 2021
  * Fixed bug in numeric conversion in DataFrame
  * Error trapping when downloading web pages to DataFrame
  * Added ignore case in filter columns
  * Removed lz4 compression for Arrow caching
* 23 Sep 2021
  * Fixed bug in YoY calculation
* 29 Jul 2021
  * Minor changes to `Market` for managing tickers
* 28 Jul 2021
  * Improved freeform ticker queries and fixed bug with downloading whole categories
* 22 Jul 2021
  * Fixed S3 credentials management and added S3 file copy method
  * Added roll costs
* 19 Jul 2021
  * Added delete file method in `IOEngine` for S3
* 12 Jul 2021
  * Can now read CSV conf files for tickers from S3 buckets and improved S3 support (can now specify AWS credentials, as parameter)
  * Additional file functions (eg. list_files)
* 05 Jul 2021
  * Now (optionally) writes Parquet files in chunks (user specified size) to avoid memory issues with pyarrow
  * Default is to use pandas.to_parquet (with pyarrow), and to fall back on chunked writing if that fails
  * Added multithreaded reading for DataVendorFlatFile
* 04 Jul 2021
  * Added extra support for reading/writing to S3 buckets of Parquet files
* 02 Jul 2021
  * Can download multiple CSVs in ZIP with time series data (DataVendorWeb) 
* 29 Jun 2021
  * Added downloads badge
* 17 Jun 2021
  * Can download different GDP releases from Bloomberg, without having to specify overrides
* 03 Jun 2021
  * Fix bug in ConfigManager
* 29 May 2021
  * Improved freeform queries for MarketDataRequest
* 26 May 2021
  * Added more flexible ticker calls (with a '_' prefix)
* 23 May 2021
  * Fixed various bugs with reading ECO_RELEASE_DT etc. dates from Bloomberg
  * Fixed bugs when predefined ticker is defined differently in different categories  
  * Can now write Parquet without date truncation errors (eg. ns to us)
  * Reads/writes Parquet from S3
* 22 May 2021
  * Better reading/writing of files to disk
* 21 May 2021
  * Added revision periods to config tickers
* 20 May 2021
  * Added ability to query stored tickers by regular expressions
  * Made field names/code consistent for tickers/vendor_tickers etc.
* 17 May 2021
  * Changed named conventions for CSV conf ticker files to be consistent with MarketDataRequest
* 08 May 2021
  * Added more ways to create a market data request
* 07 May 2021
  * Fixed freeform market data requests when contain different file formats
* 06 May 2021
  * Fixed bug when querying from files with dot in them for parquet
* 04 May 2021
  * Made fetching market data more flexible (can use a string for tickers which are not predefined)
  * Added ability to call predefined tickers with a string
* 29 Apr 2021
  * Bug fix when getting empty ticker from Bloomberg
* 22 Apr 2021
  * Added 404 error for downloading from Dukascopy
* 15 Apr 2021
  * Constant overrides now persist
* 13 Apr 2021
  * Fix issue when conversion of date/time releases for certain Bloomberg economic events
* 25 Mar 2021
  * Fixed empty column download from data vendor downloading as object (rather than NaN)
* 20 Mar 2021
  * Improved Redis caching
  * Can now fetch multiple MarketDataRequests
* 11 Feb 2021
  * Fixed timezone issues in Seasonality
  * Add extra Dukascopy error checking/retry functionality/parameters
  * Added Parquet to MarketDataRequest
  * Started to write Numba implementations for join and align
  * Added fields for downloading eg. FX vol data
* 22 Jan 2021
  * Fixed caching for tick
* 14 Jan 2021
  * Fixed ON FX option date expiry
* 10 Jan 2021
  * Added Dukascopy non-equities example
* 08 Jan 2021
  * Added extra calendar example
* 05 Jan 2021
  * MarketDataRequest accepts parsing of full month names
* 28 Dec 2020
  * Spun out Calendar into separate Python script
* 26 Dec 2020
  * Added missing holiday file
  * Refactored Calendar (so is no longer dependent on Filter)
* 24 Dec 2020
  * Remove logger as field variable in IOEngine
  * Fixed Calendar methods so can take single input
* 19 Dec 2020
  * Added functionality to download FX forwards based total indices from BBG
  * Fixed downloading of forward points for NDFs
  * Fixed missing timestamp issue with DukasCopy
  * Adding holidays functionality and calculation of FX options expiries (and FX delivery dates)
* 10 Dec 2020
    * Added resample method on Calculations for tick data
    * Fixed logger in DataVendorWeb
    * Fixed setting no timezone method
* 11 Nov 2020
    * Added cumulative additive index returns 
    * Removed log as field variable in DataVendorBBG
    * Added 10am NYC cut for FX vol surface download
* 02 Oct 2020
    * Fix vol ticker mapping for 4M points
    * Fix Bloomberg downloader for events
* 30 Sep 2020
    * Fix crypto downloaders (added tickers, fields etc. to CSV files)
* 24 Sep 2020
    * Refactoring of Calculations
* 13 Sep 2020
    * Removed multiprocessing_on_dill as dependency, which is no longer being used
* 10 Sep 2020
    * Adding Eikon as a market data source (daily, intraday and tick market data)
* 25 Aug 2020
    * Fixes for newer Pandas eg. 1.0.5
    * Fixes for ALFRED downloading of economic data
* 24 Aug 2020
    * Removed .ix references (to work with newer Pandas)
* 06 May 2020
    * Amended function to remove points outside FX hours to exclude 1 Jan every year
    * RetStats can now resample time series (removed kurtosis)
    * Tidy up some code comments
* 07 Apr 2020
    * Bug fix in constants
* 06 Apr 2020
    * Minor changes to ConfigManager
* 05 Apr 2020
    * Added push to cache parameter for MarketDataRequest
* 04 Apr 2020
    * Added timeout for Dukascopy download
* 14 Mar 2020
    * Fixed bug with downloading short intervals of Dukascopy tick data
* 20 Feb 2020
    * Made Redis optional dependency
* 30 Dec 2019
    * Added message about lack of Redis
* 17 Dec 2019
    * Fix issue with Redis cache if two similar elements cached (takes the last now)
* 16 Dec 2019
    * Fix problem with missing Redis dependency when reading from market
* 04 Dec 2019
    * Allow usage on Azure Notebooks, by making keyring dependency optional
* 03 Nov 2019
    * Added script to set API keys with keyring
* 02 Nov 2019
    * Added BoE as a data source
    * Removed blosc/msgpack (msgpack deprecated in pandas) and replaced with pyarrow for caching 
    * Uses keyring library for API keys (unless specified in DataCred)
    * Began to add tests for IO and market data download
* 03 Oct 2019
    * Remove API key from cache
    * Remove timezone when storing in Arctic (can cause issues with later versions of Pandas)
* 14 Aug 2019
    * Bloomberg downloaders now works with Pandas 0.25
    * Fixed Yahoo downloader to work with yfinance (replacing pandas_datareader for Yahoo)
* 06 Aug 2019
    * Adding parameters to MarketDataRequest for user specified API keys (Quandl, FRED & Alpha Vantage)
* 23 Jul 2019
    * Changed some rolling calculations in Calculation class to work with newer pandas
* 12 Jul 2019
    * Fixed issues with DukasCopy downloading when using multi-threading
* 01 Mar 2019
    * Added read/write Parquet
    * Added concat dataframes
* 15 Nov 2018
    * Fixed aggregation by hour/day etc. with pandas > 0.23
    * Filter data frame columns by multiple keywords
* 20 Sep 2018 - Fixed bug in ALFRED
* 25 Jul 2018 - Better timezone handling when filtering by holidays
* 23 Jul 2018 - Fixed additional bug in filter
* 27 Jun 2018 - Added note about installing blpapi via pip
* 23 Jun 2018 - Fixed bug filtering dataframes with timezones
* 29 May 2018 - Added port
* 11 May 2018
    * Allow filtering of dataframes by user defined holidays
* 25 Apr 2018
    * Added transaction costs by asset
    * Fixed bug with Redis caching
* 21 Apr 2018 - New features
    * use CSV/HDF5 files with MarketDataRequest (includes flatfile_example.py)
    * allow resample parameter for MarketDataRequest
    * added AlphaVantage as a data source
    * added fxcmpy as a a data source (unfinished)
* 20 Apr 2018 - Remove rows where all NaNs for daily data when returning from MarketDataGenerator
* 26 Mar 2018 - Change logging level for downloading dates of DukasCopy
* 20 Mar 2018 - Added insert_sparse_time_series in Calculation, and mask_time_series_by_time in Filter.
* 07 Mar 2018 - Fixed bugs for date_parser.
* 20 Feb 2018 - Added cryptocurrency data generators and example
* 22 Jan 2018 - Added function to remove duplicate consecutive data
* 05 Jan 2018 - Fixed bug when downloading BBG reference data
* 18 Dec 2017 - Fixed FXCM downloader bug
* 24 Nov 2017 - Minor bug fixes for DukasCopy downloader
* 10 Oct 2017 - Added handling of username and password for arctic
* 26 Aug 2017 - Improved threading for FXCM and DukasCopy downloaders
* 25 Aug 2017 - Added FXCM downloader (partially finished)
* 23 Aug 2017 - Improved overwritting of constants by cred file
* 10 Jul 2017 - Added method for calculation of autocorrelation in Calculations
* 07 Jun 2017 - Added methods for calendar day seasonality in Calculations
* 25 May 2017 - Removed unneeded dependency in DataQuality
* 22 May 2017 - Began to replace pandas OLS with statsmodels
* 03 May 2017 - Added section for contributors
* 28 Apr 2017 - Issues with returning weekend data for FX spot fixed
* 18 Apr 2017 - Fixed FX spot calc
* 13 Apr 2017 - Fixed issues with FX cross calculations (and refactored)
* 07 Apr 2017 - Fix issue with returned Quandl labels in returned time series, downloading of Bloomberg tick data
* 06 Apr 2017 - Fixed issue with not specifying field
* 13 Mar 2017 - Changed examples to use SwimPool
* 08 Mar 2017 - Fixed bug with DukasCopy data (was getting wrong month) and added blpapi pre-built
* 28 Feb 2017 - Added passthrough for BBG overrides via MarketDataRequest
* 23 Feb 2017 - Added ability to specify tickers with wildcards
* 21 Feb 2017 - Optimised code to speed up downloading Bloomberg data considerably
* 17 Feb 2017 - Added switch between multiprocess and multiprocessing on dill libraries in SpeedCache
* 15 Feb 2017 - Added multiprocessing_example, switched to using multiprocess library and improved SpeedCache (for deletion of keys)
* 14 Feb 2017 - Speeded up returns statistic computation and created DataQuality class
* 13 Feb 2017 - Added SwimPool class
* 12 Feb 2017 - Fixed small filtering bug (for start/finish date) and began adding tests
* 11 Feb 2017 - Added example to show how to use Redis caching
* 09 Feb 2017 - Added in-memory caching when loading market data (via Redis)
* 08 Feb 2017 - Pad columns now returns columns in same order as input
* 07 Feb 2017 - Added Redis to IOEngine
* 05 Feb 2017 - Added openpyxl as a dependency
* 01 Feb 2017 - Added method for aligning left and right dataframes (with fill down) and rolling_corr (to work with pandas <= 0.13)
* 25 Jan 2017 - Work on stop losses for multiple assets in DataFrame and extra documentation for IOEngine
* 24 Jan 2017 - Extra method for calculating signal * returns (multiplying matrices)
* 19 Jan 2017 - Changed examples location in project, added future based variables to Market
* 18 Jan 2017 - Fixed returning of bid/ask in DukasCopy
* 16 Jan 2017 - Added override for stop/take profit signals (& allow dynamic levels), speed up for filtering of time series by column
* 13 Jan 2017 - Added "expiry" for tickers (optional to add), so can handle futures data better when downloading
and various bugs fixed for getting Bloomberg reference data fetching
* 11 Jan 2017 - Added extra documentation and method for assessing stop loss/take profit
* 10 Jan 2017 - Added better handling for downloading of Bloomberg reference requests
* 05 Jan 2017 - Fixed fxspotdata_example example, fixed singleton mechanism in ConfigManager
* 24 Dec 2016 - Added more error handling for Quandl
* 20 Dec 2016 - Updated deprecated some pandas deprecated methods in Calculations class & various bug fixes
* 14 Dec 2016 - Bug fixes for DukasCopy downloader (@kalaytan) and added delete ticker from disk (Arctic)
* 09 Dec 2016 - Speeded up ALFRED/FRED downloader
* 30 Nov 2016 - Rewrote fredapi downloader (added helped methods) and added to project
* 29 Nov 2016 - Added ALFRED/FRED as a data source
* 28 Nov 2016 - Bug fixes on MarketDataGenerator and BBGLowLevelTemplate (@spyamine)
* 04 Nov 2016 - Added extra field converters for Quandl
* 02 Nov 2016 - Changed timeouts for accessing MongoDB via arctic
* 17 Oct 2016 - Functions for filtering time series by period
* 13 Oct 2016 - Added YoY metric in RetStats, by default pad missing returned columns for MarketDataGenerator
* 07 Oct 2016 - Add .idea from .gitignore
* 06 Oct 2016 - Fixed downloading of tick count for FX
* 04 Oct 2016 - Added arctic_example for writing pandas DataFrames
* 02 Oct 2016 - Added read/write dataframes via AHL's Arctic (MongoDB), added multi-threaded outer join, speeded up downloading intraday FX
* 28 Sep 2016 - Added more data types to download for vol
* 23 Sep 2016 - Fixed issue with downloading events
* 20 Sep 2016 - Removed deco dependency, fixed issue downloading Quandl fields, fixed issue with setup files
* 02 Sep 2016 - Edits around Bloomberg event download, fixed issues with data downloading threading
* 23 Aug 2016 - Added skeletons for ONS and BOE data
* 22 Aug 2016 - Added credentials file
* 17 Aug 2016 - Uploaded first code

End of note

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `findatapy_examples/__init__.py`
```python

```

#### File: `findatapy_examples/notebooks/__init__.py`
```python

```

#### File: `doc/__init__.py`
```python

```

#### File: `findatapy/conf/__init__.py`
```python
__author__ = 'saeedamen'
```

#### File: `findatapy/util/compat.py`
```python
import sys
import datetime

if sys.version_info >= (3, 12):
    def utcnow():
        """Replacement for datetime.datetime.utcnow() that works on Python 3.12+.
        Returns a naive UTC datetime (no tzinfo), same as the old utcnow()."""
        return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
else:
    def utcnow():
        """Returns a naive UTC datetime."""
        return datetime.datetime.utcnow()
```


==================================================
