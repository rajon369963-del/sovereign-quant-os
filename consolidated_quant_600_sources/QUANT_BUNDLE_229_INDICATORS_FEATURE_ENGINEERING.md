# ⚡ [QUANT-SOURCE-229] Consolidated Quant & Algo Trading Repositories
**Category**: `INDICATORS_FEATURE_ENGINEERING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_229_INDICATORS_FEATURE_ENGINEERING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ta-lib-python (`VAULT_IN-QUANT-095_TA-Lib__ta-lib-python`)
- **Full Name**: `IN-QUANT-095_TA-Lib__ta-lib-python`
- **Description**: Python wrapper for TA-Lib (http://ta-lib.org/).
- **GitHub Stars**: 12247
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# TA-Lib 📈

<!-- Badges -->
![Tests](https://github.com/ta-lib/ta-lib-python/actions/workflows/tests.yml/badge.svg)
[![Release](https://img.shields.io/github/v/release/ta-lib/ta-lib-python?label=Release)](https://github.com/ta-lib/ta-lib-python/releases)
[![PyPI](https://img.shields.io/pypi/v/TA-Lib?label=PyPI)](https://pypi.org/project/TA-Lib/)
[![Wheels](https://img.shields.io/pypi/wheel/TA-Lib?label=Wheels)](https://pypi.org/project/TA-Lib/#files)
[![Python Versions](https://img.shields.io/pypi/pyversions/TA-Lib?label=Python)](https://pypi.org/project/TA-Lib/)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](https://opensource.org/licenses/BSD-2-Clause)

This is a Python wrapper for [TA-LIB](http://ta-lib.org) based on Cython
instead of SWIG. From the homepage:

> TA-Lib is widely used by trading software developers requiring to perform
> technical analysis of financial market data.
>
> * Includes 150+ indicators such as ADX, MACD, RSI, Stochastic, Bollinger
>   Bands, etc.
> * Candlestick pattern recognition
> * Open-source API for C/C++, Java, Perl, Python and 100% Managed .NET

The original Python bindings included with TA-Lib use
[SWIG](http://swig.org) which unfortunately are difficult to install and
aren't as efficient as they could be. Therefore this project uses
[Cython](https://cython.org) and [Numpy](https://numpy.org) to efficiently
and cleanly bind to TA-Lib - producing results 2-4 times faster than the
SWIG interface.

In addition, this project also supports the use of the
[Polars](https://www.pola.rs) and [Pandas](https://pandas.pydata.org)
libraries.

## Versions 🗂️

The upstream TA-Lib C library released version 0.6.1 and changed the library
name to `-lta-lib` from `-lta_lib`. After trying to support both via
autodetect and having some issues, we have decided to currently support three
feature branches:

* `ta-lib-python` 0.4.x (supports `ta-lib` 0.4.x and `numpy` 1)
* `ta-lib-python` 0.5.x (supports `ta-lib` 0.4.x and `numpy` 2)
* `ta-lib-python` 0.6.x (supports `ta-lib` 0.6.x and `numpy` 2)
* `ta-lib-python` 0.7.x (supports `ta-lib` 0.7.x and `numpy` 2)
* `ta-lib-python` 0.8.x (supports `ta-lib` 0.8.x and `numpy` 2)

## Installation 💾

You can install from PyPI:

```shell
python -m pip install TA-Lib
```

Or checkout the sources and run `setup.py` yourself:

```shell
python setup.py install
```

It also appears possible to install via [Conda Forge](https://anaconda.org/conda-forge/ta-lib):

```shell
conda install -c conda-forge ta-lib
```

### Dependencies 🧩

To use TA-Lib for python, you need to have the [TA-Lib](http://ta-lib.org)
already installed. You should probably follow their [installation
directions](https://ta-lib.org/install/) for your platform, but some
suggestions are included below for reference.

> Some Conda Forge users have reported success installing the underlying TA-Lib C
> library using [the libta-lib package](https://anaconda.org/conda-forge/libta-lib):
>
> ``$ conda install -c conda-forge libta-lib``

#### Mac OS X

You can simply install using Homebrew:

```shell
brew install ta-lib
```

If you are using Apple Silicon, such as the M1 processors, and building mixed
architecture Homebrew projects, you might want to make sure it's being built
for your architecture:

```shell
arch -arm64 brew install ta-lib
```

And perhaps you can set these before installing with `pip`:

```shell
export TA_INCLUDE_PATH="$(brew --prefix ta-lib)/include"
export TA_LIBRARY_PATH="$(brew --prefix ta-lib)/lib"
```

You might also find this helpful, particularly if you have tried several
different installations without success:

```shell
your-arm64-python -m pip install --no-cache-dir ta-lib
```

#### Windows

For 64-bit Windows, the easiest way is to get the *executable installer*:

1. Download [ta-lib-0.7.1-windows-x86_64.msi](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-windows-x86_64.msi).
2. Run the Installer or run `msiexec` [from the command-line](https://learn.microsoft.com/en-us/windows/win32/msi/standard-installer-command-line-options).

Alternatively, if you prefer to get the libraries without installing, or
would like to use the 32-bit version:

* Intel/AMD 64-bit [ta-lib-0.7.1-windows-x86_64.zip](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-windows-x86_64.zip)
* Intel/AMD 32-bit [ta-lib-0.7.1-windows-x86_32.zip](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-windows-x86_32.zip)

#### Linux

Download
[ta-lib-0.7.1-src.tar.gz](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-src.tar.gz)
and:

```shell
tar -xzf ta-lib-0.7.1-src.tar.gz
cd ta-lib-0.7.1/
./configure --prefix=/usr
make
sudo make install
```

> If you build `TA-Lib` using `make -jX` it will fail but that's OK!
> Simply rerun ``make -jX`` followed by ``[sudo] make install``.

Note: if your directory path includes spaces, the installation will probably
fail with ``No such file or directory`` errors.

### Wheels ⚙️

For convenience, and starting with version 0.6.5, we now build binary wheels
for different operating systems, architectures, and Python versions using
GitHub Actions which include the underlying TA-Lib C library and are easy to
install.

Supported platforms:

* Linux
  * x86_64
  * arm64
* macOS
  * x86_64
  * arm64
* Windows
  * x86_64
  * x86
  * arm64

Supported Python versions:

* 3.9
* 3.10
* 3.11
* 3.12
* 3.13
* 3.14

In the event that your operating system, architecture, or Python version are
not available as a binary wheel, it is fairly easy to install from source
using the instructions above.

### Troubleshooting 🛠️

If you get a warning that looks like this:

```shell
setup.py:79: UserWarning: Cannot find ta-lib library, installation may fail.
warnings.warn('Cannot find ta-lib library, installation may fail.')
```

This typically means `setup.py` can't find the underlying `TA-Lib`
library, a dependency which needs to be installed.

---

If you installed the underlying `TA-Lib` library with a custom prefix
(e.g., with `./configure --prefix=$PREFIX`), then when you go to install
this python wrapper you can specify additional search paths to find the
library and include files for the underlying `TA-Lib` library using the
`TA_LIBRARY_PATH` and `TA_INCLUDE_PATH` environment variables:

```shell
export TA_LIBRARY_PATH=$PREFIX/lib
export TA_INCLUDE_PATH=$PREFIX/include
python setup.py install # or pip install ta-lib
```

---

Sometimes installation will produce build errors like this:

```shell
talib/_ta_lib.c:601:10: fatal error: ta-lib/ta_defs.h: No such file or directory
  601 | #include "ta-lib/ta_defs.h"
      |          ^~~~~~~~~~~~~~~~~~
compilation terminated.
```

or:

```shell
common.obj : error LNK2001: unresolved external symbol TA_SetUnstablePeriod
common.obj : error LNK2001: unresolved external symbol TA_Shutdown
common.obj : error LNK2001: unresolved external symbol TA_Initialize
common.obj : error LNK2001: unresolved external symbol TA_GetUnstablePeriod
common.obj : error LNK2001: unresolved external symbol TA_GetVersionString
```

This typically means that it can't find the underlying `TA-Lib` library, a
dependency which needs to be installed.  On Windows, this could be caused by
installing the 32-bit binary distribution of the underlying `TA-Lib` library,
but trying to use it with 64-bit Python.

---

Sometimes installation will fail with errors like this:

```shell
talib/common.c:8:22: fatal error: pyconfig.h: No such file or directory
 #include "pyconfig.h"
                      ^
compilation terminated.
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```

This typically means that you need the Python headers, and should run
something like:

```shell
sudo apt-get install python3-dev
```

---

Sometimes building the underlying `TA-Lib` library has errors running
`make` that look like this:

```shell
../libtool: line 1717: cd: .libs/libta_lib.lax/libta_abstract.a: No such file or directory
make[2]: *** [libta_lib.la] Error 1
make[1]: *** [all-recursive] Error 1
make: *** [all-recursive] Error 1
```

This might mean that the directory path to the underlying `TA-Lib` library
has spaces in the directory names.  Try putting it in a path that does not have
any spaces and trying again.

---

Sometimes you might get this error running `setup.py`:

```shell
/usr/include/limits.h:26:10: fatal error: bits/libc-header-start.h: No such file or directory
#include <bits/libc-header-start.h>
         ^~~~~~~~~~~~~~~~~~~~~~~~~~
```

This is likely an issue with trying to compile for 32-bit platform but
without the appropriate headers.  You might find some success looking at the
first answer to [this question](https://stackoverflow.com/questions/54082459/fatal-error-bits-libc-header-start-h-no-such-file-or-directory-while-compili).

---

If you get an error on macOS like this:

```shell
code signature in <141BC883-189B-322C-AE90-CBF6B5206F67>
'python3.9/site-packages/talib/_ta_lib.cpython-39-darwin.so' not valid for
use in process: Trying to load an unsigned library)
```

You might look at [this question](https://stackoverflow.com/questions/69610572/how-can-i-solve-the-below-error-while-importing-nltk-package)
and use ``xcrun codesign`` to fix it.

---

If you wonder why `STOCHRSI` gives you different results than you expect,
probably you want `STOCH` applied to `RSI`, which is a little different
than the `STOCHRSI` which is `STOCHF` applied to `RSI`:

```python
>>> import talib
>>> import numpy as np
>>> c = np.random.randn(100)

# this is the library function
>>> k, d = talib.STOCHRSI(c)

# this produces the same result, calling STOCHF
>>> rsi = talib.RSI(c)
>>> k, d = talib.STOCHF(rsi, rsi, rsi)

# you might want this instead, calling STOCH
>>> rsi = talib.RSI(c)
>>> k, d = talib.STOCH(rsi, rsi, rsi)
```

---

If the build appears to hang, you might be running on a VM with not enough memory - try 1 GB or 2 GB.

It has also been reported that using a swapfile could help, for example:

```shell
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

---

If you get "permission denied" errors such as this, you might need to give
your user access to the location where the underlying TA-Lib C library is
installed -- or install it to a user-accessible location.

```shell
talib/_ta_lib.c:747:28: fatal error: /usr/include/ta-lib/ta_defs.h: Permission denied
 #include "ta-lib/ta-defs.h"
                            ^
compilation terminated
error: command 'gcc' failed with exit status 1
```

---

If you're having trouble compiling the underlying TA-Lib C library on ARM64,
you might need to configure it with an explicit build type before running
`make` and `make install`, for example:

```shell
./configure --build=aarch64-unknown-linux-gnu
```

This is caused by old `config.guess` file, so another way to solve this is
to copy a newer version of config.guess into the underlying TA-Lib C library
sources:

```shell
cp /usr/share/automake-1.16/config.guess /path/to/extracted/ta-lib/config.guess
```

And then re-run configure:

```shell
./configure
```

---

If you're having trouble using [PyInstaller](https://pyinstaller.org) and
get an error that looks like this:

```shell
...site-packages\PyInstaller\loader\pyimod03_importers.py", line 493, in exec_module
    exec(bytecode, module.__dict__)
  File "talib\__init__.py", line 72, in <module>
ModuleNotFoundError: No module named 'talib.stream'
```

Then, perhaps you can use the `--hidden-import` argument to fix this:

```shell
pyinstaller --hidden-import talib.stream "replaceToYourFileName.py"
```

---

If you want to use `numpy<2`, then you should use `ta-lib<0.5`.

If you want to use `numpy>=2`, then you should use `ta-lib>=0.5`.

---

If you have trouble getting the code autocompletions to work in Visual
Studio Code, a suggestion was made to look for the `Python` extension
settings, and an option for `Language Server`, and change it from
`Default` (which means `Pylance if it is installed, Jedi otherwise`), to
manually set `Jedi` and the completions should work. It is possible that
you might need to [install it manually](https://github.com/pappasam/jedi-language-server) for this to
work.

## Function API

Similar to TA-Lib, the Function API provides a lightweight wrapper of the
exposed TA-Lib indicators.

Each function returns an output array and have default values for their
parameters, unless specified as keyword arguments. Typically, these functions
will have an initial "lookback" period (a required number of observations
before an output is generated) set to `NaN`.

The lookback is function-specific and does not always match the value passed
to `timeperiod`. For example, `RSI(timeperiod=14)` needs 15 price observations
because the first RSI value depends on 14 price changes between consecutive
bars, not just 14 raw prices.

For convenience, the Function API supports both `numpy.ndarray` and
`pandas.Series` and `polars.Series` inputs.

All of the following examples use the Function API:

```python
import numpy as np
import talib

close = np.random.random(100)
```

Calculate a simple moving average of the close prices:

```python
output = talib.SMA(close)
```

Calculating bollinger bands, with triple exponential moving average:

```python
from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
```

Calculating momentum of the close prices, with a time period of 5:

```python
output = talib.MOM(close, timeperiod=5)
```

Functions marked in the docs as having an unstable period start with that
extra unstable-period setting at `0`. In other words, `get_unstable_period()`
returns `0` until you explicitly change it with `set_unstable_period()`.

### NaN's

The underlying TA-Lib C library handles NaN's in a sometimes surprising manner
by typically propagating NaN's to the end of the output, for example:

```python
>>> c = np.array([1.0, 2.0, 3.0, np.nan, 4.0, 5.0, 6.0])

>>> talib.SMA(c, 3)
array([nan, nan,  2., nan, nan, nan, nan])
```

You can compare that to a Pandas rolling mean, where their approach is to
output NaN until enough "lookback" values are observed to generate new outputs:

```python
>>> c = pandas.Series([1.0, 2.0, 3.0, np.nan, 4.0, 5.0, 6.0])

>>> c.rolling(3).mean()
0    NaN
1    NaN
2    2.0
3    NaN
4    NaN
5    NaN
6    5.0
dtype: float64
```

## Abstract API

If you're already familiar with using the function API, you should feel right
at home using the Abstract API.

Every function takes a collection of named inputs, either a ``dict`` of
``numpy.ndarray`` or ``pandas.Series`` or ``polars.Series``, or a
``pandas.DataFrame`` or ``polars.DataFrame``. If a ``pandas.DataFrame`` or
``polars.DataFrame`` is provided, the output is returned as the same type
with named output columns.

For example, inputs could be provided for the typical "OHLCV" data:

```python
import numpy as np

# note that all ndarrays must be the same length!
inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}
```

Functions can either be imported directly or instantiated by name:

```python
from talib import abstract

# directly
SMA = abstract.SMA

# or by name
SMA = abstract.Function('sma')
```

From there, calling functions is basically the same as the function API:

```python
from talib.abstract import *

# uses close prices (default)
output = SMA(inputs, timeperiod=25)

# uses open prices
output = SMA(inputs, timeperiod=25, price='open')

# uses close prices (default)
upper, middle, lower = BBANDS(inputs, 20, 2.0, 2.0)

# uses high, low, close (default)
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0) # uses high, low, close by default

# uses high, low, open instead
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0, prices=['high', 'low', 'open'])
```

## Streaming API

An experimental Streaming API was added that allows users to compute the latest
value of an indicator.  This can be faster than using the Function API, for
example in an application that receives streaming data, and wants to know just
the most recent updated indicator value.

```python
import talib
from talib import stream

close = np.random.random(100)

# the Function API
output = talib.SMA(close)

# the Streaming API
latest = stream.SMA(close)

# the latest value is the same as the last output value
assert (output[-1] - latest) < 0.00001
```

## Supported Indicators and Functions 📋

We can show all the TA functions supported by TA-Lib, either as a `list` or
as a `dict` sorted by group (e.g. "Overlap Studies", "Momentum Indicators",
etc):

```python
import talib

# list of functions
for name in talib.get_functions():
    print(name)

# dict of functions by group
for group, names in talib.get_function_groups().items():
    print(group)
    for name in names:
        print(f"  {name}")
```

### Indicator Groups 🏷️

* Overlap Studies
* Momentum Indicators
* Volume Indicators
* Volatility Indicators
* Price Transform
* Cycle Indicators
* Pattern Recognition

#### Overlap Studies

```text
BBANDS               Bollinger Bands
DEMA                 Double Exponential Moving Average
EMA                  Exponential Moving Average
HT_TRENDLINE         Hilbert Transform - Instantaneous Trendline
KAMA                 Kaufman Adaptive Moving Average
MA                   Moving average
MAMA                 MESA Adaptive Moving Average
MAVP                 Moving average with variable period
MIDPOINT             MidPoint over period
MIDPRICE             Midpoint Price over period
SAR                  Parabolic SAR
SAREXT               Parabolic SAR - Extended
SMA                  Simple Moving Average
T3                   Triple Exponential Moving Average (T3)
TEMA                 Triple Exponential Moving Average
TRIMA                Triangular Moving Average
WMA                  Weighted Moving Average
```

#### Momentum Indicators

```text
ADX                  Average Directional Movement Index
ADXR                 Average Directional Movement Index Rating
APO                  Absolute Price Oscillator
AROON                Aroon
AROONOSC             Aroon Oscillator
BOP                  Balance Of Power
CCI                  Commodity Channel Index
CMO                  Chande Momentum Oscillator
DX                   Directional Movement Index
MACD                 Moving Average Convergence/Divergence
MACDEXT              MACD with controllable MA type
MACDFIX              Moving Average Convergence/Divergence Fix 12/26
MFI                  Money Flow Index
MINUS_DI             Minus Directional Indicator
MINUS_DM             Minus Directional Movement
MOM                  Momentum
PLUS_DI              Plus Directional Indicator
PLUS_DM              Plus Directional Movement
PPO                  Percentage Price Oscillator
ROC                  Rate of change : ((price/prevPrice)-1)*100
ROCP                 Rate of change Percentage: (price-prevPrice)/prevPrice
ROCR                 Rate of change ratio: (price/prevPrice)
ROCR100              Rate of change ratio 100 scale: (price/prevPrice)*100
RSI                  Relative Strength Index
STOCH                Stochastic
STOCHF               Stochastic Fast
STOCHRSI             Stochastic Relative Strength Index
TRIX                 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
ULTOSC               Ultimate Oscillator
WILLR                Williams' %R
```

#### Volume Indicators

```text
AD                   Chaikin A/D Line
ADOSC                Chaikin A/D Oscillator
OBV                  On Balance Volume
```

#### Cycle Indicators

```text
HT_DCPERIOD          Hilbert Transform - Dominant Cycle Period
HT_DCPHASE           Hilbert Transform - Dominant Cycle Phase
HT_PHASOR            Hilbert Transform - Phasor Components
HT_SINE              Hilbert Transform - SineWave
HT_TRENDMODE         Hilbert Transform - Trend vs Cycle Mode
```

#### Price Transform

```text
AVGPRICE             Average Price
MEDPRICE             Median Price
TYPPRICE             Typical Price
WCLPRICE             Weighted Close Price
```

#### Volatility Indicators

```text
ATR                  Average True Range
NATR                 Normalized Average True Range
TRANGE               True Range
```

#### Pattern Recognition

```text
CDL2CROWS            Two Crows
CDL3BLACKCROWS       Three Black Crows
CDL3INSIDE           Three Inside Up/Down
CDL3LINESTRIKE       Three-Line Strike
CDL3OUTSIDE          Three Outside Up/Down
CDL3STARSINSOUTH     Three Stars In The South
CDL3WHITESOLDIERS    Three Advancing White Soldiers
CDLABANDONEDBABY     Abandoned Baby
CDLADVANCEBLOCK      Advance Block
CDLBELTHOLD          Belt-hold
CDLBREAKAWAY         Breakaway
CDLCLOSINGMARUBOZU   Closing Marubozu
CDLCONCEALBABYSWALL  Concealing Baby Swallow
CDLCOUNTERATTACK     Counterattack
CDLDARKCLOUDCOVER    Dark Cloud Cover
CDLDOJI              Doji
CDLDOJISTAR          Doji Star
CDLDRAGONFLYDOJI     Dragonfly Doji
CDLENGULFING         Engulfing Pattern
CDLEVENINGDOJISTAR   Evening Doji Star
CDLEVENINGSTAR       Evening Star
CDLGAPSIDESIDEWHITE  Up/Down-gap side-by-side white lines
CDLGRAVESTONEDOJI    Gravestone Doji
CDLHAMMER            Hammer
CDLHANGINGMAN        Hanging Man
CDLHARAMI            Harami Pattern
CDLHARAMICROSS       Harami Cross Pattern
CDLHIGHWAVE          High-Wave Candle
CDLHIKKAKE           Hikkake Pattern
CDLHIKKAKEMOD        Modified Hikkake Pattern
CDLHOMINGPIGEON      Homing Pigeon
CDLIDENTICAL3CROWS   Identical Three Crows
CDLINNECK            In-Neck Pattern
CDLINVERTEDHAMMER    Inverted Hammer
CDLKICKING           Kicking
CDLKICKINGBYLENGTH   Kicking - bull/bear determined by the longer marubozu
CDLLADDERBOTTOM      Ladder Bottom
CDLLONGLEGGEDDOJI    Long Legged Doji
CDLLONGLINE          Long Line Candle
CDLMARUBOZU          Marubozu
CDLMATCHINGLOW       Matching Low
CDLMATHOLD           Mat Hold
CDLMORNINGDOJISTAR   Morning Doji Star
CDLMORNINGSTAR       Morning Star
CDLONNECK            On-Neck Pattern
CDLPIERCING          Piercing Pattern
CDLRICKSHAWMAN       Rickshaw Man
CDLRISEFALL3METHODS  Rising/Falling Three Methods
CDLSEPARATINGLINES   Separating Lines
CDLSHOOTINGSTAR      Shooting Star
CDLSHORTLINE         Short Line Candle
CDLSPINNINGTOP       Spinning Top
CDLSTALLEDPATTERN    Stalled Pattern
CDLSTICKSANDWICH     Stick Sandwich
CDLTAKURI            Takuri (Dragonfly Doji with very long lower shadow)
CDLTASUKIGAP         Tasuki Gap
CDLTHRUSTING         Thrusting Pattern
CDLTRISTAR           Tristar Pattern
CDLUNIQUE3RIVER      Unique 3 River
CDLUPSIDEGAP2CROWS   Upside Gap Two Crows
CDLXSIDEGAP3METHODS  Upside/Downside Gap Three Methods
```

#### Statistic Functions

```text
BETA                 Beta
CORREL               Pearson's Correlation Coefficient (r)
LINEARREG            Linear Regression
LINEARREG_ANGLE      Linear Regression Angle
LINEARREG_INTERCEPT  Linear Regression Intercept
LINEARREG_SLOPE      Linear Regression Slope
STDDEV               Standard Deviation
TSF                  Time Series Forecast
VAR                  Variance
```

### Core Implementation Code & Architecture
#### File: `talib/deprecated.py`
```python
# TA_MAType enums
MA_SMA, MA_EMA, MA_WMA, MA_DEMA, MA_TEMA, MA_TRIMA, MA_KAMA, MA_MAMA, MA_T3, \
    MA_HMA, MA_DISABLED, MA_DEFAULT, MA_ZLEMA, MA_RMA = range(14)
```

#### File: `talib/stream.py`
```python
import talib._ta_lib as _ta_lib
from ._ta_lib import __TA_FUNCTION_NAMES__


for func_name in __TA_FUNCTION_NAMES__:
    globals()[func_name] = getattr(_ta_lib, "stream_%s" % func_name)
```

#### File: `tools/perf_talib.py`
```python
import numpy
import talib
import time
import sys

TEST_LEN = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
LOOPS = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

data = numpy.random.random(TEST_LEN)

if False: # fill array with nans
    data[:-1] = numpy.nan

t0 = time.time()
for _ in range(LOOPS):
    talib.MA(data)
    talib.BBANDS(data)
    talib.KAMA(data)
    talib.CDLMORNINGDOJISTAR(data, data, data, data)
t1 = time.time()
print('test_len: %d, loops: %d' % (TEST_LEN, LOOPS))
print('%.6f' % (t1 - t0))
print('%.6f' % ((t1 - t0) / LOOPS))
```

#### File: `talib/abstract.py`
```python
import talib._ta_lib as _ta_lib
from ._ta_lib import Function as _Function, __TA_FUNCTION_NAMES__, _get_defaults_and_docs

# add some backwards compat for backtrader
from ._ta_lib import TA_FUNC_FLAGS, TA_INPUT_FLAGS, TA_OUTPUT_FLAGS

_func_obj_mapping = {
    func_name: getattr(_ta_lib, func_name)
    for func_name in __TA_FUNCTION_NAMES__
}


def Function(function_name, *args, **kwargs):
    func_name = function_name.upper()
    if func_name not in _func_obj_mapping:
        raise Exception('%s not supported by TA-LIB.' % func_name)

    return _Function(
        func_name, _func_obj_mapping[func_name], *args, **kwargs
    )


for func_name in __TA_FUNCTION_NAMES__:
    globals()[func_name] = Function(func_name)


__all__ = ["Function", "_get_defaults_and_docs"] + __TA_FUNCTION_NAMES__
```

#### File: `tests/test_stubs.py`
```python
import ast
import os

import talib

STUBS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'talib')


def _stub(name):
    with open(os.path.join(STUBS, name)) as f:
        return f.read()


# The stubs ship as package data beside py.typed, and nothing else in the build
# reads them, so a broken one reaches every downstream type checker in silence.
def test_stubs_parse():
    for name in ('_ta_lib.pyi', 'abstract.pyi'):
        ast.parse(_stub(name), filename=name)


def test_stubs_cover_every_function():
    stub = _stub('_ta_lib.pyi')
    declared = {node.name for node in ast.parse(stub).body
                if isinstance(node, ast.FunctionDef)}
    for name in talib.__TA_FUNCTION_NAMES__:
        assert name in declared, name
        assert 'stream_%s' % name in declared, name
```

#### File: `tools/threads_talib.py`
```python
import time
import threading

import numpy
import copy
from talib.abstract import RSI
import sys
import pandas as pd

TEST_LEN_SHORT = int(sys.argv[1]) if len(sys.argv) > 1 else 999
TEST_LEN_LONG = int(sys.argv[1]) if len(sys.argv) > 1 else 4005
LOOPS = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

data_short = numpy.random.rand(TEST_LEN_SHORT, 5)
data_long = numpy.random.rand(TEST_LEN_LONG, 5)

df_short = pd.DataFrame(data_short, columns={
                        'open', 'high', 'low', 'close', 'volume'})
df_long = pd.DataFrame(data_long, columns={
                       'open', 'high', 'low', 'close', 'volume'})

total = 0


def loop():
    global total
    if threading.get_native_id() % 2 == 0:
        df = copy.deepcopy(df_short)
    else:
        df = copy.deepcopy(df_long)

    while total < LOOPS:
        total += 1
        try:
            df['RSI'] = RSI(df)
        except ValueError as msg:
            raise ValueError(msg)


t0 = time.time()

threads = []
for i in range(4):
    t = threading.Thread(target=loop)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
t1 = time.time()
print('test_len: %d, loops: %d' % (TEST_LEN_LONG, LOOPS))
print('%.6f' % (t1 - t0))
print('%.6f' % ((t1 - t0) / LOOPS))
```


==================================================


## [2/3] Repository: finta (`WHEEL_finta`)
- **Full Name**: `finta`
- **Description**: Common financial technical indicators implemented in Pandas.
- **GitHub Stars**: 2264
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# FinTA (Financial Technical Analysis)

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![PyPI](https://img.shields.io/pypi/v/finta.svg?style=flat-square)](https://pypi.python.org/pypi/finta/)
[![Downloads](https://pepy.tech/badge/finta/month)](https://pepy.tech/project/finta/month)
[![](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/download/releases/3.6.0/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Build Status](https://travis-ci.org/peerchemist/finta.svg?branch=master)](https://travis-ci.org/peerchemist/finta)
[![Patrons](https://img.shields.io/liberapay/patrons/peerchemist.svg?logo=liberapay)](https://img.shields.io/liberapay/patrons/peerchemist.svg?logo=liberapay)
[![Bitcoin Donate](https://badgen.net/badge/Bitcoin/Donate/F19537?icon=bitcoin)](https://blockstream.info/address/3Jp1RjKZdQjb1Ui4o5MVqhfch3rD1xUynn)
[![Peercoin Donate](https://badgen.net/badge/peercoin/Donate/green?icon=https://raw.githubusercontent.com/peercoin/media/84710cca6c3c8d2d79676e5260cc8d1cd729a427/Peercoin%202020%20Logo%20Files/01.%20Icon%20Only/Inside%20Circle/Transparent/Green%20Icon/peercoin-icon-green-transparent.svg)](https://chainz.cryptoid.info/ppc/address.dws?PWzpZ5igHDSA76gNZ9DwE7aeCbfLsZbDkJ)

Common financial technical indicators implemented in Pandas.

![example](examples/plot.png)

*This is work in progress, bugs are expected and results of some indicators
may not be accurate.*

## Supported indicators:

Finta supports over 80 trading indicators:

```
* Simple Moving Average 'SMA'
* Simple Moving Median 'SMM'
* Smoothed Simple Moving Average 'SSMA'
* Exponential Moving Average 'EMA'
* Double Exponential Moving Average 'DEMA'
* Triple Exponential Moving Average 'TEMA'
* Triangular Moving Average 'TRIMA'
* Triple Exponential Moving Average Oscillator 'TRIX'
* Volume Adjusted Moving Average 'VAMA'
* Kaufman Efficiency Indicator 'ER'
* Kaufman's Adaptive Moving Average 'KAMA'
* Zero Lag Exponential Moving Average 'ZLEMA'
* Weighted Moving Average 'WMA'
* Hull Moving Average 'HMA'
* Elastic Volume Moving Average 'EVWMA'
* Volume Weighted Average Price 'VWAP'
* Smoothed Moving Average 'SMMA'
* Fractal Adaptive Moving Average 'FRAMA'
* Moving Average Convergence Divergence 'MACD'
* Percentage Price Oscillator 'PPO'
* Volume-Weighted MACD 'VW_MACD'
* Elastic-Volume weighted MACD 'EV_MACD'
* Market Momentum 'MOM'
* Rate-of-Change 'ROC'
* Relative Strenght Index 'RSI'
* Inverse Fisher Transform RSI 'IFT_RSI'
* True Range 'TR'
* Average True Range 'ATR'
* Stop-and-Reverse 'SAR'
* Bollinger Bands 'BBANDS'
* Bollinger Bands Width 'BBWIDTH'
* Momentum Breakout Bands 'MOBO'
* Percent B 'PERCENT_B'
* Keltner Channels 'KC'
* Donchian Channel 'DO'
* Directional Movement Indicator 'DMI'
* Average Directional Index 'ADX'
* Pivot Points 'PIVOT'
* Fibonacci Pivot Points 'PIVOT_FIB'
* Stochastic Oscillator %K 'STOCH'
* Stochastic oscillator %D 'STOCHD'
* Stochastic RSI 'STOCHRSI'
* Williams %R 'WILLIAMS'
* Ultimate Oscillator 'UO'
* Awesome Oscillator 'AO'
* Mass Index 'MI'
* Vortex Indicator 'VORTEX'
* Know Sure Thing 'KST'
* True Strength Index 'TSI'
* Typical Price 'TP'
* Accumulation-Distribution Line 'ADL'
* Chaikin Oscillator 'CHAIKIN'
* Money Flow Index 'MFI'
* On Balance Volume 'OBV'
* Weighter OBV 'WOBV'
* Volume Zone Oscillator 'VZO'
* Price Zone Oscillator 'PZO'
* Elder's Force Index 'EFI'
* Cummulative Force Index 'CFI'
* Bull power and Bear Power 'EBBP'
* Ease of Movement 'EMV'
* Commodity Channel Index 'CCI'
* Coppock Curve 'COPP'
* Buy and Sell Pressure 'BASP'
* Normalized BASP 'BASPN'
* Chande Momentum Oscillator 'CMO'
* Chandelier Exit 'CHANDELIER'
* Qstick 'QSTICK'
* Twiggs Money Index 'TMF'
* Wave Trend Oscillator 'WTO'
* Fisher Transform 'FISH'
* Ichimoku Cloud 'ICHIMOKU'
* Adaptive Price Zone 'APZ'
* Squeeze Momentum Indicator 'SQZMI'
* Volume Price Trend 'VPT'
* Finite Volume Element 'FVE'
* Volume Flow Indicator 'VFI'
* Moving Standard deviation 'MSD'
* Schaff Trend Cycle 'STC'
* Mark Whistler's WAVE PM 'WAVEPM'
```

## Dependencies:

-   python (3.6+)
-   pandas (1.0.0+)

TA class is very well documented and there should be no trouble
exploring it and using with your data. Each class method expects proper `ohlc` DataFrame as input.

## Install:

`pip install finta`

or latest development version:

`pip install git+git://github.com/peerchemist/finta.git`

## Import

`from finta import TA`

Prepare data to use with finta:

finta expects properly formated `ohlc` DataFrame, with column names in `lowercase`:
["open", "high", "low", "close"] and ["volume"] for indicators that expect `ohlcv` input.

### to resample by time period (you can choose different time period)
`ohlc = resample(df, "24h")`

### You can also load a ohlc DataFrame from .csv file

`data_file = ("data/bittrex:btc-usdt.csv")`

`ohlc = pd.read_csv(data_file, index_col="date", parse_dates=True)`

____________________________________________________________________________

## Examples:

### will return Pandas Series object with the Simple moving average for 42 periods
`TA.SMA(ohlc, 42)`

### will return Pandas Series object with "Awesome oscillator" values
`TA.AO(ohlc)`

### expects ["volume"] column as input
`TA.OBV(ohlc)`

### will return Series with Bollinger Bands columns [BB_UPPER, BB_LOWER]
`TA.BBANDS(ohlc)`

### will return Series with calculated BBANDS values but will use KAMA instead of MA for calculation, other types of Moving Averages are allowed as well.
`TA.BBANDS(ohlc, MA=TA.KAMA(ohlc, 20))`


For more examples see examples directory.

------------------------------------------------------------------------

I welcome pull requests with new indicators or fixes for existing ones.
Please submit only indicators that belong in public domain and are
royalty free.

## Contributing

1. Fork it (https://github.com/peerchemist/finta/fork)
2. Study how it's implemented.
3. Create your feature branch (`git checkout -b my-new-feature`).
4. Run [black](https://github.com/ambv/black) code formatter on the finta.py to ensure uniform code style.
5. Commit your changes (`git commit -am 'Add some feature'`).
6. Push to the branch (`git push origin my-new-feature`).
7. Create a new Pull Request.

------------------------------------------------------------------------

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `finta/__init__.py`
```python
from finta.finta import TA
```

#### File: `setup.py`
```python
from setuptools import setup
from os import path

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Financial and Insurance Industry",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
]

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="finta",
    version="1.3",
    description=" Common financial technical indicators implemented in Pandas.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["technical analysis", "ta", "pandas", "finance", "numpy", "analysis"],
    url="https://github.com/peerchemist/finta",
    author="Peerchemist",
    author_email="peerchemist@protonmail.ch",
    license="LGPLv3+",
    packages=["finta"],
    install_requires=["pandas", "numpy"],
    license_files=["LICENSE"]
)
```

#### File: `tests/test_utils_unit.py`
```python
import pytest
import os
from pandas import DataFrame, Series
from finta import TA
from finta.utils import to_dataframe, resample, trending_down, trending_up
import numpy
import json


def rootdir():

    return os.path.dirname(os.path.abspath(__file__))


data_file = os.path.join(rootdir(), "data/poloniex_xrp-btc.json")

with open(data_file, "r") as outfile:
    data = json.load(outfile)


def test_to_dataframe():

    assert isinstance(to_dataframe(data), DataFrame)


def test_resample():

    df = to_dataframe(data)
    assert isinstance(resample(df, "2d"), DataFrame)
    assert list(resample(df, "2d").index.values[-2:]) == [
        numpy.datetime64("2019-05-05T00:00:00.000000000"),
        numpy.datetime64("2019-05-07T00:00:00.000000000"),
    ]


def test_resample_calendar():

    df = to_dataframe(data)
    assert isinstance(resample(df, "W-Mon"), DataFrame)
    assert list(resample(df, "W-Mon").index.values[-2:]) == [
        numpy.datetime64("2019-05-06T00:00:00.000000000"),
        numpy.datetime64("2019-05-13T00:00:00.000000000"),
    ]


def test_trending_up():

    df = to_dataframe(data)
    ma = TA.HMA(df)
    assert isinstance(trending_up(ma, 10), Series)

    assert not trending_up(ma, 10).values[-1]


def test_trending_down():

    df = to_dataframe(data)
    ma = TA.HMA(df)
    assert isinstance(trending_down(ma, 10), Series)

    assert trending_down(ma, 10).values[-1]
```

#### File: `finta/utils.py`
```python
import pandas as pd


def to_dataframe(ticks: list) -> pd.DataFrame:
    """Convert list to Series compatible with the library."""

    df = pd.DataFrame(ticks)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df.set_index("time", inplace=True)

    return df


def resample(df: pd.DataFrame, interval: str) -> pd.DataFrame:
    """Resample DataFrame by <interval>."""

    d = {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}

    return df.resample(interval).agg(d)


def resample_calendar(df: pd.DataFrame, offset: str) -> pd.DataFrame:
    """Resample the DataFrame by calendar offset.
    See http://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#anchored-offsets for compatible offsets.
    :param df: data
    :param offset: calendar offset
    :return: result DataFrame
    """

    d = {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}

    return df.resample(offset).agg(d)


def trending_up(df: pd.Series, period: int) -> pd.Series:
    """returns boolean Series if the inputs Series is trending up over last n periods.
    :param df: data
    :param period: range
    :return: result Series
    """

    return pd.Series(df.diff(period) > 0, name="trending_up {}".format(period))


def trending_down(df: pd.Series, period: int) -> pd.Series:
    """returns boolean Series if the input Series is trending up over last n periods.
    :param df: data
    :param period: range
    :return: result Series
    """

    return pd.Series(df.diff(period) < 0, name="trending_down {}".format(period))
```

#### File: `tests/test_reg.py`
```python
import pytest
import os
import pandas as pd
from finta import TA
import talib


def rootdir():

    return os.path.dirname(os.path.abspath(__file__))


data_file = os.path.join(rootdir(), 'data/xau-usd.json')

# using tail 500 rows only
ohlc = pd.read_json(data_file, orient=["time"]).set_index("time").tail(500)


def test_sma():
    '''test TA.SMA'''

    ma = TA.SMA(ohlc, 14)
    talib_ma = talib.SMA(ohlc['close'], timeperiod=14)

    assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)


def test_ema():
    '''test TA.EMA'''

    ma = TA.EMA(ohlc, 50)
    talib_ma = talib.EMA(ohlc['close'], timeperiod=50)

    assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)


def test_dema():
    '''test TA.DEMA'''

    ma = TA.DEMA(ohlc, 20)
    talib_ma = talib.DEMA(ohlc['close'], timeperiod=20)

    assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)


def test_wma():
    '''test TA.WVMA'''

    ma = TA.WMA(ohlc, period=20)
    talib_ma = talib.WMA(ohlc['close'], timeperiod=20)

    # assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)
    # assert 1511.96547 == 1497.22193
    pass  # close enough


def test_kama():
    '''test TA.KAMA'''

    ma = TA.KAMA(ohlc, period=30)
    talib_ma = talib.KAMA(ohlc['close'], timeperiod=30)

    # assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)
    # assert 1519.60321 == 1524.26954
    pass  # close enough


def test_tema():
    '''test TA.TEMA'''

    ma = TA.TEMA(ohlc, 50)
    talib_ma = talib.TEMA(ohlc['close'], timeperiod=50)

    assert round(talib_ma[-1], 2) == round(ma.values[-1], 2)


def test_trima():
    '''test TA.TRIMA'''

    ma = TA.TRIMA(ohlc, 30)
    talib_ma = talib.TRIMA(ohlc['close'])

    #assert round(talib_ma[-1], 5) == round(ma.values[-1], 5)
    # assert 1509.0876041666781 == 1560.25056
    pass  # close enough


def test_trix():
    '''test TA.TRIX'''

    ma = TA.TRIX(ohlc, 20)
    talib_ma = talib.TRIX(ohlc['close'], timeperiod=20)

    assert round(talib_ma[-1], 2) == round(ma.values[-1], 2)


def test_tr():
    '''test TA.TR'''

    tr = TA.TR(ohlc)
    talib_tr = talib.TRANGE(ohlc['high'], ohlc['low'], ohlc['close'])

    assert round(talib_tr[-1], 5) == round(tr.values[-1], 5)


def test_macd():
    """test MACD"""

    macd = TA.MACD(ohlc)
    talib_macd = talib.MACD(ohlc['close'])

    assert round(talib_macd[0][-1], 3) == round(macd["MACD"].values[-1], 3)
    assert round(talib_macd[1][-1], 3) == round(macd["SIGNAL"].values[-1], 3)


def test_atr():
    '''test TA.ATR'''

    tr = TA.ATR(ohlc, 14)
    talib_tr = talib.ATR(ohlc['high'], ohlc['low'], ohlc['close'],
                         timeperiod=14)

    # it is close enough
    # 336.403776 == 328.568904
    #assert round(talib_tr[-1], 5) == round(tr.values[-1], 5)
    assert True


def test_mom():
    '''test TA.MOM'''

    mom = TA.MOM(ohlc, 15)
    talib_mom = talib.MOM(ohlc['close'], 15)

    assert round(talib_mom[-1], 5) == round(mom.values[-1], 5)


def test_roc():
    """test TA.ROC"""

    roc = TA.ROC(ohlc, 10)
    talib_roc = talib.ROC(ohlc["close"], 10)

    assert round(talib_roc[-1], 5) == round(roc.values[-1], 5)


def test_rsi():
    '''test TA.RSI'''

    rsi = TA.RSI(ohlc, 9)
    talib_rsi = talib.RSI(ohlc['close'], 9)

    assert int(talib_rsi[-1]) == int(rsi.values[-1])


def test_mfi():
    '''test TA.MFI'''

    mfi = TA.MFI(ohlc, 9)
    talib_mfi = talib.MFI(ohlc['high'], ohlc['low'], ohlc['close'], ohlc['volume'], 9)

    assert int(talib_mfi[-1]) == int(mfi.values[-1])


def test_bbands():
    '''test TA.BBANDS'''

    bb = TA.BBANDS(ohlc, 20)
    talib_bb = talib.BBANDS(ohlc['close'], timeperiod=20)

    # assert int(bb['BB_UPPER'][-1]) == int(talib_bb[0].values[-1])
    # assert 8212 == 8184

    # assert int(bb['BB_LOWER'][-1]) == int(talib_bb[2].values[-1])
    # assert 6008 == 6036

    pass  # close enough


def test_dmi():
    '''test TA.DMI'''

    dmp = TA.DMI(ohlc, 14, True)["DI+"]
    talib_dmp = talib.PLUS_DI(ohlc["high"], ohlc["low"], ohlc["close"], timeperiod=14)

    # assert talib_dmp[-1] == dmp.values[-1]
    # assert 25.399441371241316 == 22.867910021116124
    pass  #  close enough

    dmn = TA.DMI(ohlc, 14, True)["DI-"]
    talib_dmn = talib.MINUS_DI(ohlc["high"], ohlc["low"], ohlc["close"], timeperiod=14)

    # assert talib_dmn[-1] == dmn.values[-1]
    # assert 20.123182007302802 == 19.249274328040045
    pass  # close enough


def test_adx():
    '''test TA.ADX'''

    adx = TA.ADX(ohlc, period=12)
    ta_adx = talib.ADX(ohlc["high"], ohlc["low"], ohlc["close"], timeperiod=12)

    # assert int(ta_adx[-1]) == int(adx.values[-1])
    # assert 26 == 27
    pass  # close enough


def test_obv():
    """test OBC"""

    obv = TA.OBV(ohlc)
    talib_obv = talib.OBV(ohlc["close"], ohlc["volume"])

    #assert obv.values[-1] == talib_obv[-1]
    #assert -149123.0 == -148628.0
    pass  # close enough


def test_cmo():
    """test TA.CMO"""

    cmo = TA.CMO(ohlc, period=9)
    talib_cmo = talib.CMO(ohlc["close"], timeperiod=9)

    # assert round(talib_cmo[-1], 2) == round(cmo.values[-1], 2)
    # assert -35.99 == -35.66
    pass  # close enough


def test_stoch():
    """test TA.STOCH"""

    stoch = TA.STOCH(ohlc, 9)
    talib_stoch = talib.STOCH(ohlc["high"], ohlc["low"], ohlc["close"], 9)

    #  talib_stoch[0] is "slowk"
    # assert talib_stoch[0][-1] == stoch.values[-1]
    # assert 76.27794470586021 == 80.7982311922445
    pass  # close enough


def test_sar():
    """test TA.SAR"""

    sar = TA.SAR(ohlc)
    talib_sar = talib.SAR(ohlc.high, ohlc.low)

    # assert sar.values[-1] == talib_sar.values[-1]
    # 1466.88618052864 == 1468.3663877395456
    # close enough
    pass


def test_williams():
    """test TA.WILLIAMS"""

    will = TA.WILLIAMS(ohlc, 14)
    talib_will = talib.WILLR(ohlc["high"], ohlc["low"], ohlc["close"], 14)

    assert round(talib_will[-1], 5) == round(will.values[-1], 5)


def test_uo():
    """test TA.UO"""

    uo = TA.UO(ohlc)
    talib_uo = talib.ULTOSC(ohlc["high"], ohlc["low"], ohlc["close"])

    assert round(talib_uo[-1], 5) == round(uo.values[-1], 5)
```


==================================================


## [3/3] Repository: ta-lib (`WHEEL_ta-lib`)
- **Full Name**: `ta-lib`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# TA-Lib 📈

<!-- Badges -->
![Tests](https://github.com/ta-lib/ta-lib-python/actions/workflows/tests.yml/badge.svg)
[![Release](https://img.shields.io/github/v/release/ta-lib/ta-lib-python?label=Release)](https://github.com/ta-lib/ta-lib-python/releases)
[![PyPI](https://img.shields.io/pypi/v/TA-Lib?label=PyPI)](https://pypi.org/project/TA-Lib/)
[![Wheels](https://img.shields.io/pypi/wheel/TA-Lib?label=Wheels)](https://pypi.org/project/TA-Lib/#files)
[![Python Versions](https://img.shields.io/pypi/pyversions/TA-Lib?label=Python)](https://pypi.org/project/TA-Lib/)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](https://opensource.org/licenses/BSD-2-Clause)

This is a Python wrapper for [TA-LIB](http://ta-lib.org) based on Cython
instead of SWIG. From the homepage:

> TA-Lib is widely used by trading software developers requiring to perform
> technical analysis of financial market data.
>
> * Includes 150+ indicators such as ADX, MACD, RSI, Stochastic, Bollinger
>   Bands, etc.
> * Candlestick pattern recognition
> * Open-source API for C/C++, Java, Perl, Python and 100% Managed .NET

The original Python bindings included with TA-Lib use
[SWIG](http://swig.org) which unfortunately are difficult to install and
aren't as efficient as they could be. Therefore this project uses
[Cython](https://cython.org) and [Numpy](https://numpy.org) to efficiently
and cleanly bind to TA-Lib - producing results 2-4 times faster than the
SWIG interface.

In addition, this project also supports the use of the
[Polars](https://www.pola.rs) and [Pandas](https://pandas.pydata.org)
libraries.

## Versions 🗂️

The upstream TA-Lib C library released version 0.6.1 and changed the library
name to `-lta-lib` from `-lta_lib`. After trying to support both via
autodetect and having some issues, we have decided to currently support three
feature branches:

* `ta-lib-python` 0.4.x (supports `ta-lib` 0.4.x and `numpy` 1)
* `ta-lib-python` 0.5.x (supports `ta-lib` 0.4.x and `numpy` 2)
* `ta-lib-python` 0.6.x (supports `ta-lib` 0.6.x and `numpy` 2)

## Installation 💾

You can install from PyPI:

```shell
python -m pip install TA-Lib
```

Or checkout the sources and run `setup.py` yourself:

```shell
python setup.py install
```

It also appears possible to install via [Conda Forge](https://anaconda.org/conda-forge/ta-lib):

```shell
conda install -c conda-forge ta-lib
```

### Dependencies 🧩

To use TA-Lib for python, you need to have the [TA-Lib](http://ta-lib.org)
already installed. You should probably follow their [installation
directions](https://ta-lib.org/install/) for your platform, but some
suggestions are included below for reference.

> Some Conda Forge users have reported success installing the underlying TA-Lib C
> library using [the libta-lib package](https://anaconda.org/conda-forge/libta-lib):
>
> ``$ conda install -c conda-forge libta-lib``

#### Mac OS X

You can simply install using Homebrew:

```shell
brew install ta-lib
```

If you are using Apple Silicon, such as the M1 processors, and building mixed
architecture Homebrew projects, you might want to make sure it's being built
for your architecture:

```shell
arch -arm64 brew install ta-lib
```

And perhaps you can set these before installing with `pip`:

```shell
export TA_INCLUDE_PATH="$(brew --prefix ta-lib)/include"
export TA_LIBRARY_PATH="$(brew --prefix ta-lib)/lib"
```

You might also find this helpful, particularly if you have tried several
different installations without success:

```shell
your-arm64-python -m pip install --no-cache-dir ta-lib
```

#### Windows

For 64-bit Windows, the easiest way is to get the *executable installer*:

1. Download [ta-lib-0.7.1-windows-x86_64.msi](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-windows-x86_64.msi).
2. Run the Installer or run `msiexec` [from the command-line](https://learn.microsoft.com/en-us/windows/win32/msi/standard-installer-command-line-options).

Alternatively, if you prefer to get the libraries without installing, or
would like to use the 32-bit version:

* Intel/AMD 64-bit [ta-lib-0.7.1-windows-x86_64.zip](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-windows-x86_64.zip)
* Intel/AMD 32-bit [ta-lib-0.7.1-windows-x86_32.zip](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-windows-x86_32.zip)

#### Linux

Download
[ta-lib-0.7.1-src.tar.gz](https://github.com/ta-lib/ta-lib/releases/download/v0.7.1/ta-lib-0.7.1-src.tar.gz)
and:

```shell
tar -xzf ta-lib-0.7.1-src.tar.gz
cd ta-lib-0.7.1/
./configure --prefix=/usr
make
sudo make install
```

> If you build `TA-Lib` using `make -jX` it will fail but that's OK!
> Simply rerun ``make -jX`` followed by ``[sudo] make install``.

Note: if your directory path includes spaces, the installation will probably
fail with ``No such file or directory`` errors.

### Wheels ⚙️

For convenience, and starting with version 0.6.5, we now build binary wheels
for different operating systems, architectures, and Python versions using
GitHub Actions which include the underlying TA-Lib C library and are easy to
install.

Supported platforms:

* Linux
  * x86_64
  * arm64
* macOS
  * x86_64
  * arm64
* Windows
  * x86_64
  * x86
  * arm64

Supported Python versions:

* 3.9
* 3.10
* 3.11
* 3.12
* 3.13
* 3.14

In the event that your operating system, architecture, or Python version are
not available as a binary wheel, it is fairly easy to install from source
using the instructions above.

### Troubleshooting 🛠️

If you get a warning that looks like this:

```shell
setup.py:79: UserWarning: Cannot find ta-lib library, installation may fail.
warnings.warn('Cannot find ta-lib library, installation may fail.')
```

This typically means `setup.py` can't find the underlying `TA-Lib`
library, a dependency which needs to be installed.

---

If you installed the underlying `TA-Lib` library with a custom prefix
(e.g., with `./configure --prefix=$PREFIX`), then when you go to install
this python wrapper you can specify additional search paths to find the
library and include files for the underlying `TA-Lib` library using the
`TA_LIBRARY_PATH` and `TA_INCLUDE_PATH` environment variables:

```shell
export TA_LIBRARY_PATH=$PREFIX/lib
export TA_INCLUDE_PATH=$PREFIX/include
python setup.py install # or pip install ta-lib
```

---

Sometimes installation will produce build errors like this:

```shell
talib/_ta_lib.c:601:10: fatal error: ta-lib/ta_defs.h: No such file or directory
  601 | #include "ta-lib/ta_defs.h"
      |          ^~~~~~~~~~~~~~~~~~
compilation terminated.
```

or:

```shell
common.obj : error LNK2001: unresolved external symbol TA_SetUnstablePeriod
common.obj : error LNK2001: unresolved external symbol TA_Shutdown
common.obj : error LNK2001: unresolved external symbol TA_Initialize
common.obj : error LNK2001: unresolved external symbol TA_GetUnstablePeriod
common.obj : error LNK2001: unresolved external symbol TA_GetVersionString
```

This typically means that it can't find the underlying `TA-Lib` library, a
dependency which needs to be installed.  On Windows, this could be caused by
installing the 32-bit binary distribution of the underlying `TA-Lib` library,
but trying to use it with 64-bit Python.

---

Sometimes installation will fail with errors like this:

```shell
talib/common.c:8:22: fatal error: pyconfig.h: No such file or directory
 #include "pyconfig.h"
                      ^
compilation terminated.
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```

This typically means that you need the Python headers, and should run
something like:

```shell
sudo apt-get install python3-dev
```

---

Sometimes building the underlying `TA-Lib` library has errors running
`make` that look like this:

```shell
../libtool: line 1717: cd: .libs/libta_lib.lax/libta_abstract.a: No such file or directory
make[2]: *** [libta_lib.la] Error 1
make[1]: *** [all-recursive] Error 1
make: *** [all-recursive] Error 1
```

This might mean that the directory path to the underlying `TA-Lib` library
has spaces in the directory names.  Try putting it in a path that does not have
any spaces and trying again.

---

Sometimes you might get this error running `setup.py`:

```shell
/usr/include/limits.h:26:10: fatal error: bits/libc-header-start.h: No such file or directory
#include <bits/libc-header-start.h>
         ^~~~~~~~~~~~~~~~~~~~~~~~~~
```

This is likely an issue with trying to compile for 32-bit platform but
without the appropriate headers.  You might find some success looking at the
first answer to [this question](https://stackoverflow.com/questions/54082459/fatal-error-bits-libc-header-start-h-no-such-file-or-directory-while-compili).

---

If you get an error on macOS like this:

```shell
code signature in <141BC883-189B-322C-AE90-CBF6B5206F67>
'python3.9/site-packages/talib/_ta_lib.cpython-39-darwin.so' not valid for
use in process: Trying to load an unsigned library)
```

You might look at [this question](https://stackoverflow.com/questions/69610572/how-can-i-solve-the-below-error-while-importing-nltk-package)
and use ``xcrun codesign`` to fix it.

---

If you wonder why `STOCHRSI` gives you different results than you expect,
probably you want `STOCH` applied to `RSI`, which is a little different
than the `STOCHRSI` which is `STOCHF` applied to `RSI`:

```python
>>> import talib
>>> import numpy as np
>>> c = np.random.randn(100)

# this is the library function
>>> k, d = talib.STOCHRSI(c)

# this produces the same result, calling STOCHF
>>> rsi = talib.RSI(c)
>>> k, d = talib.STOCHF(rsi, rsi, rsi)

# you might want this instead, calling STOCH
>>> rsi = talib.RSI(c)
>>> k, d = talib.STOCH(rsi, rsi, rsi)
```

---

If the build appears to hang, you might be running on a VM with not enough memory - try 1 GB or 2 GB.

It has also been reported that using a swapfile could help, for example:

```shell
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

---

If you get "permission denied" errors such as this, you might need to give
your user access to the location where the underlying TA-Lib C library is
installed -- or install it to a user-accessible location.

```shell
talib/_ta_lib.c:747:28: fatal error: /usr/include/ta-lib/ta_defs.h: Permission denied
 #include "ta-lib/ta-defs.h"
                            ^
compilation terminated
error: command 'gcc' failed with exit status 1
```

---

If you're having trouble compiling the underlying TA-Lib C library on ARM64,
you might need to configure it with an explicit build type before running
`make` and `make install`, for example:

```shell
./configure --build=aarch64-unknown-linux-gnu
```

This is caused by old `config.guess` file, so another way to solve this is
to copy a newer version of config.guess into the underlying TA-Lib C library
sources:

```shell
cp /usr/share/automake-1.16/config.guess /path/to/extracted/ta-lib/config.guess
```

And then re-run configure:

```shell
./configure
```

---

If you're having trouble using [PyInstaller](https://pyinstaller.org) and
get an error that looks like this:

```shell
...site-packages\PyInstaller\loader\pyimod03_importers.py", line 493, in exec_module
    exec(bytecode, module.__dict__)
  File "talib\__init__.py", line 72, in <module>
ModuleNotFoundError: No module named 'talib.stream'
```

Then, perhaps you can use the `--hidden-import` argument to fix this:

```shell
pyinstaller --hidden-import talib.stream "replaceToYourFileName.py"
```

---

If you want to use `numpy<2`, then you should use `ta-lib<0.5`.

If you want to use `numpy>=2`, then you should use `ta-lib>=0.5`.

---

If you have trouble getting the code autocompletions to work in Visual
Studio Code, a suggestion was made to look for the `Python` extension
settings, and an option for `Language Server`, and change it from
`Default` (which means `Pylance if it is installed, Jedi otherwise`), to
manually set `Jedi` and the completions should work. It is possible that
you might need to [install it manually](https://github.com/pappasam/jedi-language-server) for this to
work.

## Function API

Similar to TA-Lib, the Function API provides a lightweight wrapper of the
exposed TA-Lib indicators.

Each function returns an output array and have default values for their
parameters, unless specified as keyword arguments. Typically, these functions
will have an initial "lookback" period (a required number of observations
before an output is generated) set to `NaN`.

The lookback is function-specific and does not always match the value passed
to `timeperiod`. For example, `RSI(timeperiod=14)` needs 15 price observations
because the first RSI value depends on 14 price changes between consecutive
bars, not just 14 raw prices.

For convenience, the Function API supports both `numpy.ndarray` and
`pandas.Series` and `polars.Series` inputs.

All of the following examples use the Function API:

```python
import numpy as np
import talib

close = np.random.random(100)
```

Calculate a simple moving average of the close prices:

```python
output = talib.SMA(close)
```

Calculating bollinger bands, with triple exponential moving average:

```python
from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)
```

Calculating momentum of the close prices, with a time period of 5:

```python
output = talib.MOM(close, timeperiod=5)
```

Functions marked in the docs as having an unstable period start with that
extra unstable-period setting at `0`. In other words, `get_unstable_period()`
returns `0` until you explicitly change it with `set_unstable_period()`.

### NaN's

The underlying TA-Lib C library handles NaN's in a sometimes surprising manner
by typically propagating NaN's to the end of the output, for example:

```python
>>> c = np.array([1.0, 2.0, 3.0, np.nan, 4.0, 5.0, 6.0])

>>> talib.SMA(c, 3)
array([nan, nan,  2., nan, nan, nan, nan])
```

You can compare that to a Pandas rolling mean, where their approach is to
output NaN until enough "lookback" values are observed to generate new outputs:

```python
>>> c = pandas.Series([1.0, 2.0, 3.0, np.nan, 4.0, 5.0, 6.0])

>>> c.rolling(3).mean()
0    NaN
1    NaN
2    2.0
3    NaN
4    NaN
5    NaN
6    5.0
dtype: float64
```

## Abstract API

If you're already familiar with using the function API, you should feel right
at home using the Abstract API.

Every function takes a collection of named inputs, either a ``dict`` of
``numpy.ndarray`` or ``pandas.Series`` or ``polars.Series``, or a
``pandas.DataFrame`` or ``polars.DataFrame``. If a ``pandas.DataFrame`` or
``polars.DataFrame`` is provided, the output is returned as the same type
with named output columns.

For example, inputs could be provided for the typical "OHLCV" data:

```python
import numpy as np

# note that all ndarrays must be the same length!
inputs = {
    'open': np.random.random(100),
    'high': np.random.random(100),
    'low': np.random.random(100),
    'close': np.random.random(100),
    'volume': np.random.random(100)
}
```

Functions can either be imported directly or instantiated by name:

```python
from talib import abstract

# directly
SMA = abstract.SMA

# or by name
SMA = abstract.Function('sma')
```

From there, calling functions is basically the same as the function API:

```python
from talib.abstract import *

# uses close prices (default)
output = SMA(inputs, timeperiod=25)

# uses open prices
output = SMA(inputs, timeperiod=25, price='open')

# uses close prices (default)
upper, middle, lower = BBANDS(inputs, 20, 2.0, 2.0)

# uses high, low, close (default)
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0) # uses high, low, close by default

# uses high, low, open instead
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0, prices=['high', 'low', 'open'])
```

## Streaming API

An experimental Streaming API was added that allows users to compute the latest
value of an indicator.  This can be faster than using the Function API, for
example in an application that receives streaming data, and wants to know just
the most recent updated indicator value.

```python
import talib
from talib import stream

close = np.random.random(100)

# the Function API
output = talib.SMA(close)

# the Streaming API
latest = stream.SMA(close)

# the latest value is the same as the last output value
assert (output[-1] - latest) < 0.00001
```

## Supported Indicators and Functions 📋

We can show all the TA functions supported by TA-Lib, either as a `list` or
as a `dict` sorted by group (e.g. "Overlap Studies", "Momentum Indicators",
etc):

```python
import talib

# list of functions
for name in talib.get_functions():
    print(name)

# dict of functions by group
for group, names in talib.get_function_groups().items():
    print(group)
    for name in names:
        print(f"  {name}")
```

### Indicator Groups 🏷️

* Overlap Studies
* Momentum Indicators
* Volume Indicators
* Volatility Indicators
* Price Transform
* Cycle Indicators
* Pattern Recognition

#### Overlap Studies

```text
BBANDS               Bollinger Bands
DEMA                 Double Exponential Moving Average
EMA                  Exponential Moving Average
HT_TRENDLINE         Hilbert Transform - Instantaneous Trendline
KAMA                 Kaufman Adaptive Moving Average
MA                   Moving average
MAMA                 MESA Adaptive Moving Average
MAVP                 Moving average with variable period
MIDPOINT             MidPoint over period
MIDPRICE             Midpoint Price over period
SAR                  Parabolic SAR
SAREXT               Parabolic SAR - Extended
SMA                  Simple Moving Average
T3                   Triple Exponential Moving Average (T3)
TEMA                 Triple Exponential Moving Average
TRIMA                Triangular Moving Average
WMA                  Weighted Moving Average
```

#### Momentum Indicators

```text
ADX                  Average Directional Movement Index
ADXR                 Average Directional Movement Index Rating
APO                  Absolute Price Oscillator
AROON                Aroon
AROONOSC             Aroon Oscillator
BOP                  Balance Of Power
CCI                  Commodity Channel Index
CMO                  Chande Momentum Oscillator
DX                   Directional Movement Index
MACD                 Moving Average Convergence/Divergence
MACDEXT              MACD with controllable MA type
MACDFIX              Moving Average Convergence/Divergence Fix 12/26
MFI                  Money Flow Index
MINUS_DI             Minus Directional Indicator
MINUS_DM             Minus Directional Movement
MOM                  Momentum
PLUS_DI              Plus Directional Indicator
PLUS_DM              Plus Directional Movement
PPO                  Percentage Price Oscillator
ROC                  Rate of change : ((price/prevPrice)-1)*100
ROCP                 Rate of change Percentage: (price-prevPrice)/prevPrice
ROCR                 Rate of change ratio: (price/prevPrice)
ROCR100              Rate of change ratio 100 scale: (price/prevPrice)*100
RSI                  Relative Strength Index
STOCH                Stochastic
STOCHF               Stochastic Fast
STOCHRSI             Stochastic Relative Strength Index
TRIX                 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
ULTOSC               Ultimate Oscillator
WILLR                Williams' %R
```

#### Volume Indicators

```text
AD                   Chaikin A/D Line
ADOSC                Chaikin A/D Oscillator
OBV                  On Balance Volume
```

#### Cycle Indicators

```text
HT_DCPERIOD          Hilbert Transform - Dominant Cycle Period
HT_DCPHASE           Hilbert Transform - Dominant Cycle Phase
HT_PHASOR            Hilbert Transform - Phasor Components
HT_SINE              Hilbert Transform - SineWave
HT_TRENDMODE         Hilbert Transform - Trend vs Cycle Mode
```

#### Price Transform

```text
AVGPRICE             Average Price
MEDPRICE             Median Price
TYPPRICE             Typical Price
WCLPRICE             Weighted Close Price
```

#### Volatility Indicators

```text
ATR                  Average True Range
NATR                 Normalized Average True Range
TRANGE               True Range
```

#### Pattern Recognition

```text
CDL2CROWS            Two Crows
CDL3BLACKCROWS       Three Black Crows
CDL3INSIDE           Three Inside Up/Down
CDL3LINESTRIKE       Three-Line Strike
CDL3OUTSIDE          Three Outside Up/Down
CDL3STARSINSOUTH     Three Stars In The South
CDL3WHITESOLDIERS    Three Advancing White Soldiers
CDLABANDONEDBABY     Abandoned Baby
CDLADVANCEBLOCK      Advance Block
CDLBELTHOLD          Belt-hold
CDLBREAKAWAY         Breakaway
CDLCLOSINGMARUBOZU   Closing Marubozu
CDLCONCEALBABYSWALL  Concealing Baby Swallow
CDLCOUNTERATTACK     Counterattack
CDLDARKCLOUDCOVER    Dark Cloud Cover
CDLDOJI              Doji
CDLDOJISTAR          Doji Star
CDLDRAGONFLYDOJI     Dragonfly Doji
CDLENGULFING         Engulfing Pattern
CDLEVENINGDOJISTAR   Evening Doji Star
CDLEVENINGSTAR       Evening Star
CDLGAPSIDESIDEWHITE  Up/Down-gap side-by-side white lines
CDLGRAVESTONEDOJI    Gravestone Doji
CDLHAMMER            Hammer
CDLHANGINGMAN        Hanging Man
CDLHARAMI            Harami Pattern
CDLHARAMICROSS       Harami Cross Pattern
CDLHIGHWAVE          High-Wave Candle
CDLHIKKAKE           Hikkake Pattern
CDLHIKKAKEMOD        Modified Hikkake Pattern
CDLHOMINGPIGEON      Homing Pigeon
CDLIDENTICAL3CROWS   Identical Three Crows
CDLINNECK            In-Neck Pattern
CDLINVERTEDHAMMER    Inverted Hammer
CDLKICKING           Kicking
CDLKICKINGBYLENGTH   Kicking - bull/bear determined by the longer marubozu
CDLLADDERBOTTOM      Ladder Bottom
CDLLONGLEGGEDDOJI    Long Legged Doji
CDLLONGLINE          Long Line Candle
CDLMARUBOZU          Marubozu
CDLMATCHINGLOW       Matching Low
CDLMATHOLD           Mat Hold
CDLMORNINGDOJISTAR   Morning Doji Star
CDLMORNINGSTAR       Morning Star
CDLONNECK            On-Neck Pattern
CDLPIERCING          Piercing Pattern
CDLRICKSHAWMAN       Rickshaw Man
CDLRISEFALL3METHODS  Rising/Falling Three Methods
CDLSEPARATINGLINES   Separating Lines
CDLSHOOTINGSTAR      Shooting Star
CDLSHORTLINE         Short Line Candle
CDLSPINNINGTOP       Spinning Top
CDLSTALLEDPATTERN    Stalled Pattern
CDLSTICKSANDWICH     Stick Sandwich
CDLTAKURI            Takuri (Dragonfly Doji with very long lower shadow)
CDLTASUKIGAP         Tasuki Gap
CDLTHRUSTING         Thrusting Pattern
CDLTRISTAR           Tristar Pattern
CDLUNIQUE3RIVER      Unique 3 River
CDLUPSIDEGAP2CROWS   Upside Gap Two Crows
CDLXSIDEGAP3METHODS  Upside/Downside Gap Three Methods
```

#### Statistic Functions

```text
BETA                 Beta
CORREL               Pearson's Correlation Coefficient (r)
LINEARREG            Linear Regression
LINEARREG_ANGLE      Linear Regression Angle
LINEARREG_INTERCEPT  Linear Regression Intercept
LINEARREG_SLOPE      Linear Regression Slope
STDDEV               Standard Deviation
TSF                  Time Series Forecast
VAR                  Variance
```

### Core Implementation Code & Architecture
#### File: `talib/deprecated.py`
```python
# TA_MAType enums
MA_SMA, MA_EMA, MA_WMA, MA_DEMA, MA_TEMA, MA_TRIMA, MA_KAMA, MA_MAMA, MA_T3 = range(9)
```

#### File: `talib/stream.py`
```python
import talib._ta_lib as _ta_lib
from ._ta_lib import __TA_FUNCTION_NAMES__


for func_name in __TA_FUNCTION_NAMES__:
    globals()[func_name] = getattr(_ta_lib, "stream_%s" % func_name)
```

#### File: `tools/perf_talib.py`
```python
import numpy
import talib
import time
import sys

TEST_LEN = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
LOOPS = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

data = numpy.random.random(TEST_LEN)

if False: # fill array with nans
    data[:-1] = numpy.nan

t0 = time.time()
for _ in range(LOOPS):
    talib.MA(data)
    talib.BBANDS(data)
    talib.KAMA(data)
    talib.CDLMORNINGDOJISTAR(data, data, data, data)
t1 = time.time()
print('test_len: %d, loops: %d' % (TEST_LEN, LOOPS))
print('%.6f' % (t1 - t0))
print('%.6f' % ((t1 - t0) / LOOPS))
```

#### File: `talib/abstract.py`
```python
import talib._ta_lib as _ta_lib
from ._ta_lib import Function as _Function, __TA_FUNCTION_NAMES__, _get_defaults_and_docs

# add some backwards compat for backtrader
from ._ta_lib import TA_FUNC_FLAGS, TA_INPUT_FLAGS, TA_OUTPUT_FLAGS

_func_obj_mapping = {
    func_name: getattr(_ta_lib, func_name)
    for func_name in __TA_FUNCTION_NAMES__
}


def Function(function_name, *args, **kwargs):
    func_name = function_name.upper()
    if func_name not in _func_obj_mapping:
        raise Exception('%s not supported by TA-LIB.' % func_name)

    return _Function(
        func_name, _func_obj_mapping[func_name], *args, **kwargs
    )


for func_name in __TA_FUNCTION_NAMES__:
    globals()[func_name] = Function(func_name)


__all__ = ["Function", "_get_defaults_and_docs"] + __TA_FUNCTION_NAMES__
```

#### File: `tools/threads_talib.py`
```python
import time
import threading

import numpy
import copy
from talib.abstract import RSI
import sys
import pandas as pd

TEST_LEN_SHORT = int(sys.argv[1]) if len(sys.argv) > 1 else 999
TEST_LEN_LONG = int(sys.argv[1]) if len(sys.argv) > 1 else 4005
LOOPS = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

data_short = numpy.random.rand(TEST_LEN_SHORT, 5)
data_long = numpy.random.rand(TEST_LEN_LONG, 5)

df_short = pd.DataFrame(data_short, columns={
                        'open', 'high', 'low', 'close', 'volume'})
df_long = pd.DataFrame(data_long, columns={
                       'open', 'high', 'low', 'close', 'volume'})

total = 0


def loop():
    global total
    if threading.get_native_id() % 2 == 0:
        df = copy.deepcopy(df_short)
    else:
        df = copy.deepcopy(df_long)

    while total < LOOPS:
        total += 1
        try:
            df['RSI'] = RSI(df)
        except ValueError as msg:
            raise ValueError(msg)


t0 = time.time()

threads = []
for i in range(4):
    t = threading.Thread(target=loop)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
t1 = time.time()
print('test_len: %d, loops: %d' % (TEST_LEN_LONG, LOOPS))
print('%.6f' % (t1 - t0))
print('%.6f' % ((t1 - t0) / LOOPS))
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["setuptools", "Cython", "numpy"]
build-backend = "setuptools.build_meta"

[project]
name = "TA-Lib"
version = "0.7.1"
description = "Python wrapper for TA-Lib"
readme = "README.md"
license-files = ["LICENSE"]
authors = [
    {name = "John Benediktsson", email = "mrjbq7@gmail.com"}
]
urls = {homepage = "http://github.com/ta-lib/ta-lib-python", download = "https://github.com/ta-lib/ta-lib-python/releases"}
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Operating System :: Unix",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Programming Language :: Cython",
    "Topic :: Office/Business :: Financial",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Financial and Insurance Industry",
]
dependencies = [
    "numpy",
]
requires-python = '>=3.9'

[tool.setuptools]
packages = ["talib"]
package-data = {"talib" = ["_ta_lib.pyi", "py.typed", "abstract.pyi"]}
```


==================================================
