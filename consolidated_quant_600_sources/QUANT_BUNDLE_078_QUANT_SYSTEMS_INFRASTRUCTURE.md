# ⚡ [QUANT-SOURCE-078] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_078_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: finmarketpy (`WHEEL_finmarketpy`)
- **Full Name**: `finmarketpy`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<img src="finmarketpy_logo.png?raw=true" width="300"/>

# [finmarketpy (formerly pythalesians)](https://github.com/cuemacro/finmarketpy)

[![Downloads](https://pepy.tech/badge/finmarketpy)](https://pepy.tech/project/finmarketpy)

finmarketpy is a Python based library that enables you to analyze market data and also to backtest trading strategies using
a simple to use API, which has prebuilt templates for you to define backtest. Included in the library

* Prebuilt templates for backtesting trading strategies
* Display historical returns for trading strategies
* Investigate seasonality of trading strategies
* Conduct market event studies around data events
* In built calculator for risk weighting using volatility targeting
* Written in object oriented way to make code more reusable

*Contributors for the project are very much welcome, see below!*

# Merging with pythalesians
I had previously written the open source PyThalesians financial library (which has been merged with this - so can focus on maintaining
one set of libraries). This new finmarketpy library has
* Similar functionality to the trading part of pythalesians
* Rewritten the API to make it much cleaner and easier to use, as well as having many
new features.
* finmarketpy requires the libraries, which I've written chartpy (for charts) and findatapy (for loading market data) to function
* By splitting up into smaller more specialised libraries, it should make it easier for contributors
* Using findatapy, you can download market data easily from Bloomberg, Quandl, Yahoo etc
* Using chartpy, you can choose to have results displayed in matplotlib, plotly or bokeh by changing single keyword!

Points to note:
* Please bear in mind at present finmarketpy is under continual development. The API is heavily documented, but we are
looking to add more general documentation.
* Uses Apache 2.0 licence

# Gallery

Calculate the cumulative returns of a trading strategy historically (see finmarketpy_examples/tradingmodelfxtrend_example.py)

<img src="finmarketpy_examples/gallery/fx-trend-cumulative.png?raw=true" width="750"/>

Plot the leverage of the strategy over time

<img src="finmarketpy_examples/gallery/fx-trend-leverage.png?raw=true" width="750"/>

Plot the individual trade returns

<img src="finmarketpy_examples/gallery/fx-trend-trade-returns.png?raw=true" width="750"/>

Calculate seasonality of any asset: here we show gold and FX volatility seasonality (see examples/seasonality_examples.py)

<img src="finmarketpy_examples/gallery/gold-seasonality.png?raw=true" width="750"/>

<img src="finmarketpy_examples/gallery/fx-vol-seasonality.png?raw=true" width="750"/>

Calculate event study around events for asset (see examples/events_examples.py)

<img src="finmarketpy_examples/gallery/usdjpy-nfp.png?raw=true" width="750"/>


# Requirements

Major requirements
* Required: Python 3.10
* Required: pandas, numpy etc.
* Required: findatapy for downloading market data (https://github.com/cuemacro/findatapy)
* Required: chartpy for funky interactive plots (https://github.com/cuemacro/chartpy)

# Installation

For detailed installation instructions for finmarketpy and its associated Python libraries go to
https://github.com/cuemacro/finmarketpy/blob/master/INSTALL.md (which includes details on how to setup your entire Python environment).

Also take a look at https://github.com/cuemacro/teaching/blob/master/pythoncourse/installation/installing_anaconda_and_pycharm.ipynb
from my Python for finance workshop course, where I keep notes specifically about setting up your Anaconda environment
for data science (including for findatapy/chartpy/finmarketpy) etc.

You can install the library using the below (better to get the newest version from repo, as opposed to releases).

After installation:
* Make sure you edit the marketconstants.py file (or you can create a marketcred.py file to overwrite the settings)

```
pip install git+https://github.com/cuemacro/finmarketpy.git
```

But beforehand please make sure you have already installed both chartpy, findatapy and any other dependencies.
In chartpy you will need to change the chartconstants.py file (to add Plotly API key) and
for findatapy, you will also need to change the dataconstants.py file to add the Quandl API
(and possibly change other configuration settings there or add a datacred.py file in the util folder,
alternatively you will be prompted on your first run to input the API key which will be installed). If you do pip with git
you'll get the very latest commit.

```
pip install git+https://github.com/cuemacro/chartpy.git
pip install git+https://github.com/cuemacro/findatapy.git
```

However you can also pip install to get from PyPI (might be a slighter older version from that on GitHub)

```
pip install chartpy
pip install findatapy
```

FinancePy is an optional dependency for finmarketpy for option pricing. It is recommended
to install it separately from PyPI after installing finmarketpy, and without dependencies
otherwise it can cause clashes with other libraries (because of its strict version
dependencies on libraries like llvmlite, which in practice can be relaxed).
The API changes a lot so it recommended to install the specific version listed below.

```
pip install numba numpy scipy llvmlite ipython pandas prettytable
pip install financepy==0.370 --no-deps
```

# Binder and Jupyter - Run finmarketpy in your browser

You can run some of the Jupyter notebooks in Binder interactively in your browser to play around with finmarketpy. It might take a few minutes for the
Binder instance to start. We are currently working on having more notebooks in Binder, so stay tuned!

Note that you will need to get a Quandl
API key to download market data to use some of these, and you can sign up for a free account at https://www.quandl.com.

* [Backtesting an FX trend following strategy - backtest_example (Binder Link)](https://mybinder.org/v2/gh/cuemacro/finmarketpy/master?filepath=finmarketpy_examples/finmarketpy_notebooks/backtest_example.ipynb)
* [Downloading market data examples - market_data_example (Binder Link)](https://mybinder.org/v2/gh/cuemacro/finmarketpy/master?filepath=finmarketpy_examples/finmarketpy_notebooks/market_data_example.ipynb)

# Synchronizing your fork of finmarketpy with master

I found this [article useful](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository) for
explaining how to update your fork to match the master changes.

# Contributors

Contributors are always welcome for finmarketpy, findatapy and chartpy. If you'd like to contribute, have a look at
[Planned Features](PLANNED_FEATURES.md) for areas we're looking for help on. Or if you have any ideas for improvements
to the libriares please let us know too!

# Sponsorship, workshops and support for Cuemacro libraries

We have spent many years writing finmarketpy and other open source libraries at Cuemacro, and we are keen to do so
for many years into the future.

If you using our libraries and are interested in sponsoring Cuemacro's open source libraries, you can do so through the
GitHub sponsorship page at https://github.com/sponsors/cuemacro

We also offer commercial services for our Cuemacro libraries, which include:

* a 2 day Python for finance workshop, which can be taught at your firm, to teach you how to use Cuemacro's libraries
* extensive commercial technical support for our libraries

If you are interested in our commercial services please contact saeed@cuemacro.com

All these sources of funding, whether it is sponsorship or our commercial services, help us to maintain Cuemacro's libraries,
so we can improve our open source libraries for the community.

# Problems with Numba and doing options pricing in finmarketpy/financepy

Underneath finmarketpy uses financepy to do option pricing. It uses Numba to speed up the computation.

You may sometimes experience Numba errors like such as `Failed in nopython mode pipeline (step: nopython frontend)`

One possible way to fix this is to delete the `__pycache__` folders underneath wherever financepy is installed:

Eg. if you are using the `py310class` environment, if you've installed Anaconda in `C:\Anaconda3`, you might find the financepy
folder at the below location

`C:\Anaconda3\envs\py310class\Lib\site-packages\financepy`

# To upgrade only finmarketpy and other Cuemacro packages (and no dependencies)

pip install -U --no-deps finmarketpy findatapy chartpy

# finmarketpy examples

In finmarketpy/examples you will find several examples, including some simple trading models

# Release Notes

* 0.11.19 - finmarketpy (09 Mar 2025)
* 0.11.16 - finmarketpy (08 Mar 2025)
* 0.11.15 - finmarketpy (08 Mar 2025)
* 0.11.14 - finmarketpy (19 May 2024)
* 0.11.13 - finmarketpy (01 Jan 2024)
* 0.11.12 - finmarketpy (26 Apr 2023)
* 0.11.11 - finmarketpy (07 Oct 2021)
* 0.11.10 - finmarketpy (06 Oct 2021)
* 0.11.9 - finmarketpy (01 Jun 2021)
* 0.11.8 - finmarketpy (25 Jan 2021)
* 0.11.7 - finmarketpy (20 Oct 2020)
* 0.11.6 - finmarketpy (02 Oct 2020)
* 0.11.5 - finmarketpy (24 Aug 2020)
* 0.11.4 - finmarketpy (06 May 2020)
* 0.11.3 - finmarketpy (04 Dec 2019)
* 0.11.1 - finmarketpy (23 Oct 2019)
* 0.11 - finmarketpy
* First prerelease version

# Coding log

# finmarketpy log

* 09 Mar 2025
  * Removed FinancePy from pyproject.toml
* 08 Mar 2025
  * Make FinancePy an optional dependency
  * Fixed various deprecation messages related Pandas
  * Made Plotly charts look nicer (autoscale with latest ChartPy)
* 07 Mar 2025
  * Merge changes for pyproject.toml etc.
  * Formatting towards PEP8
* 09 Nov 2024
  * Changed trend following example to use FRED
* 19 May 2024
  * Fixed run in parallel bug on
* 01 Apr 2024
  * Added Jupyter notebook for new ArcticDB support from findatapy
* 01 Jan 2024
  * Helper code to reduce boiler plate code for TradingModel
  * Upgraded to FinancePy 0.310 and refactored FXVolSurface
* 26 Apr 2023
  * Changed sklearn to scikit-learn dependency
* 05 Apr 2022
  * Set FinancePy version required to 0.220 and refactored FXVolSurface for
  this
* 07 Oct 2021
  * Set FinancePy version required to 0.193
* 23 Sep 2021
  * Fixed bug in YoY plot
* 23 Jul 2021
  * Added roll costs in backtest
* 30 May 2021
  * Added S3 Jupyter notebook for use with findatapy
* 21 May 2021
  * Fix bug with plotting vol target charts when vol targeting is off
* 12 May 2021
  * Fixed bug when calculating benchmark return statistics in TradingModel with different start/finish date
* 04 May 2021
  * Revamped Jupyter notebook for downloading market data with findatapy
* 28 Apr 2021
  * Added signal multiplier parameter for charts
* 21 Apr 2021
  * Format changes to TradingModel charts
* 15 Apr 2021
  * Constant overrides now persist
* 13 Apr 2021
  * Replaced loc with iloc in TechIndicator to remove Pandas deprecated functionality
* 08 Apr 2021
  * Fixed EventStudy issue when start window is before time series
* 21 Mar 2021
  * Fixed issue with EventStudy
  * Refactored TradingModel when constructing weights
* 22 Feb 2021
  * Fix bug when plotting IR of strategies
* 16 Feb 2021
  * Added total returns in example for options indices construction
* 11 Feb 2021
  * Refactored to use join from Calculations instead of pandas_outer_join
  * Allowed backtesting by fields other than close
  * Customize strike range for extracting FX vol surface
* 22 Jan 2021
  * FX spot total returns now supports intraday data and added example
  * Fixed problem with Numba implementation of FX spot total returns
* 17 Jan 2021
  * Fix vol surface examples to work with new FXVolSurface
* 16 Jan 2021
  * Additional work on FXOptionPricer and total returns (FXOptionCurve)
    * Speed up and deal with non-convergence of solver
    * Allow options entry on user specified dates
  * Added more option examples
* 11 Jan 2021
  * Fixed issue with OTM strikes in FXOptionPricer
* 10 Jan 2021
  * Fixed incorrect pushing of 10d quotes on FX vol surface
  * Added extra parameters for FXOptionsCurve, freezing FX implied, calendar etc.
* 09 Jan 2021
  * Fixed dom/for rate in FX vol surface
  * Fixed additive index
  * Still sorting issues with total return indices for FX options
* 08 Jan 2021
  * Added total returns for straddle (with example)
  * Fixed positioning flip and expiring on day without market data on FXOptionsCurve
* 08 Jan 2021
  * Changed FXVolSurface to fit better with newest FinancePy
  * Added missing FXOptionsCurve class
* 07 Jan 2021
  * Added FX vanilla option pricing (via FinancePy)
  * Calculate total return indices for FX vanilla options
* 26 Dec 2020
    * Refactored classes to take into account new Calendar object from findatapy
* 24 Dec 2020
    * Added FX forwards pricer with examples
      * Interpolation of odd dates
      * Implied depo calculations
    * Added FX forwards total return calculator with examples
    * Rewrote FX spot indices construction to use Numba
* 20 Dec 2020
  * Changed typo in licence at top of scripts
* 19 Dec 2020
  * Added VolStats and examples to calculate realized vol, vol risk premium and implied vol addons
  * Added FX total return calculations for FX spot positions
  * Begun to add FX total return calculations for FX forwards (incomplete)
  * Adapted FX vol code to latest version of FinancePy (note, may need to download via GitHub instead of PyPI)
  * Also calculated implied PDF for FX vol surface using FinancePy underneath
* 04 Dec 2020
    * Fix imports in FX vol interpolation
* 02 Dec 2020
    * Added FX vol surface interpolation (using FinancePy library underneath) + animated example
* 12 Nov 2020
    * Added Binder, so can run notebooks interactively
    * Edited backtest_example Jupyter notebook with more description
* 11 Nov 2020
    * Added cumulative additive index flag for backtests
* 20 Oct 2020
    * Fixed missing GBP depo tickers
    * Fixed startup on newer MacOS
* 02 Oct 2020
    * Fixed vol surface calculation
* 24 Aug 2020
    * Replaced .ix to work with later versions of pandas
* 07 May 2020
    * Improved QuickChart, adding additional labels, fixing example
* 06 May 2020
    * Added QuickChart for one line download of market data and plotting
    * Added feature to resample returns
    * Allow more custom parameters in backtest
* 17 Dec 2019
    * Added link for Python for finance workshop installation notes for Anaconda
* 04 Dec 2019
    * Making blosc optional in BacktestEngine
* 14 Nov 2019
    * Added network plot
* 02 Nov 2019
    * Fixed bug running on Mac
    * Updated installation instructions
    * Added tests for technical indicators
    * Added backtestcomparison.py
* 29 Mar 2019 - Added variable transaction costs
* 14 Nov 2018 - Fixed contract bug in backtest_example
* 18 Sep 2018 - Fixed bug on writing PnL CSV
* 17 Sep 2018 - Added rounding for trade size display (otherwise trades can be ungrounded because of rounding errors)
* 11 Jun 2018 - Fixed bug with single threaded TradeAnalysis
* 29 May 2018 - Added port
* 25 Apr 2018
    * Added (some) parallel features for backtesting and sensitivity analysis (works better in Linux)
    * Added different transaction costs by assets
    * Fixed backtesting examples so work with "run_in_parallel" keyword and can customise BacktestRequest more
* 18 Apr 2018 - Fix bug with trade notional sizes
* 06 Apr 2018 - Added function to measure freq of trade notional sizes
* 29 Mar 2018 - Fix bug when dumping CSV of P&L
* 15 Mar 2018 - Added caching for event data
* 26 Feb 2018 - Added solution for replacing parameters under tech_params (in tradeanalysis.py).
* 30 Jan 2018 - Fix bug on backtest.example.py
* 25 Jan 2018 - Fix bug on class
* 04 Jan 2018 - Bug fix for Cred override of constants
* 16 Sep 2017 - Adding to planned features list
* 10 Jul 2017 - Added install instructions for conda
* 03 Jul 2017 - Fixed dependency on seasonal library
* 26 Jun 2017 - BacktestEngine can now handle weighted sum style portfolios
* 23 Jun 2017 - Downloads observation date for economic data (EventStudy)
* 21 Jun 2017 - Added trend following example using Bloomberg total return data
* 07 Jun 2017 - Added output of IR/Rets in sensitivity analysis (TradeAnalysis)
* 22 May 2017 - Output returns of strategy (to CSV file)
* 03 May 2017 - Added more planned features
* 13 Apr 2017 - Changed finish date on FX trend following model
* 12 Mar 2017 - Added FX vol surface animation example
* 25 Feb 2017 - Added signal delay parameter
* 24 Feb 2017 - Refactored backtesting classes so have consistent naming
* 21 Feb 2017 - Refactored BacktestEngine to use SwimPool
* 20 Feb 2017 - Extra install instructions
* 14 Feb 2017 - Added Planned Features page
* 08 Feb 2017 - Added SHOW_CHARTS parameter for TradingModel and made SMA work with old pandas
* 05 Feb 2017 - Added more installation notes and fixed Excel output in TradeAnalysis if notional not specified
* 02 Feb 2017 - Further changes to constraints on max long/shorts (with refactoring)
* 01 Feb 2017 - Added constraints for max longs/shorts and plots in BacktestEngine
* 25 Jan 2017 - Additional work on stops/take profit with multiple assets & plotting bug fixes for TradeAnalysis
* 24 Jan 2017 - Fixing issues around stops/take profits and adding fields in TechParams
* 19 Jan 2017 - Change location of examples in project
* 16 Jan 2017 - Added method in BacktestEngine for debugging of P&L (dumps table with signals/assets/returns)
* 12 Jan 2017 - Added detailed installation notes
* 11 Jan 2017 - Rewrote large number of comments, added ATR calculation and basic stop loss/take profit functionality
* 07 Jan 2017 - Now outputs position sizes scaled by notional & by user defined contract sizes
* 06 Jan 2017 - Added user defined weightings for strategies & general bug fixes
* 04 Jan 2017 - Added a period shift parameter for calculating leverage (in RiskEngine)
* 30 Nov 2016 - Added seasonality example for NFP
* 24 Nov 2016 - Added seasonality example for gasoline
* 17 Nov 2016 - Changed source to ChartConstants default for TradingModel
* 14 Oct 2016 - Fixed arctic references in MarketConstants
* 13 Oct 2016 - Fixed IR plotting for BacktestEngine, added YoY metric plots
* 11 Oct 2016 - Added to TradeAnalysis another way to plot return statistics for a portfolio
* 10 Oct 2016 - Added returns_example to show how to use PyFolio via finmarketpy, added dataframe input for TradeAnalysis, fixed typo in readme
* 07 Oct 2016 - Add .idea to .gitignore
* 06 Oct 2016 - Split out plotting of no of trades and position proportion
* 22 Sep 2016 - Fixed sorting of columns when signal plotting
* 21 Sep 2016 - Allow plotting of multiple signal days
* 15 Sep 2016 - Merged finmarketpy and pythalesians fully, released version 0.11
* 12 Sep 2016 - Fixed issue with TradeAnalysis (method names)
* 02 Sep 2016 - Fixed issue with external dataframe eco events, added event study example
* 01 Sep 2016 - Added seasonality example for FX vol
* 22 Aug 2016 - Fixed boot issue and added credentials
* 17 Aug 2016 - Uploaded first code

# pythalesians log

* 03 Aug 2016 - Fixed missing conf files
* 02 Aug 2016 - Changed default Plotly background color and fixed constants issue with AdapterTemplate
* 01 Aug 2016 - Renamed pythalesians_graphics as chartesians (preparing eventual spinout)
* 29 Jul 2016 - Created Jupyter notebook plot_market_data for plotting with multiple libraries, also fixed Bokeh sizing issue,
refactored library, spinning out chart functionality into pythalesians_graphics
* 28 Jul 2016 - Fixed issue with multiple fields returned by Quandl, added Quandl downloading example
* 26 Jul 2016 - Added more support for Plotly charts, added surface vol Plotly example
* 21 Jul 2016 - Refactor StrategyTemplate graph plotting functions
* 20 Jul 2016 - Return of figure handle for AdapterPyThalesians
* 08 Jun 2016 - Fix kurtosis issue, refactored vol scaling in CashBasktest, added resample wrapper in TimeSeriesFilter
* 03 Jun 2016 - Speed up CashBacktest (construct_strategy method)
* 02 Jun 2016 - Fixed missing StrategyTemplate file in installation, added auto-detection of path
to simplify installation and added methods for converting between pandas and bcolz
* 31 May 2016 - Got rid of deprecated Pandas methods in TechIndicator
* 27 May 2016 - Added ability to plot strategy signal at point in time
* 19 May 2016 - Updated Quandl wrapper to use new Quandl API
* 02 May 2016 - Tidied up BacktestRequest, added SPX seasonality example
* 28 Apr 2016 - Updated cashbacktest (for Pandas 0.18)
* 21 Apr 2016 - Got rid of deprecated Pandas methods in EventStudy
* 18 Apr 2016 - Fixed some incompatibility issues with Pandas 0.18
* 06 Apr 2016 - Added more trade statistics output
* 01 Apr 2016 - Speeded up joining operations, noticeable when fetching high freq time series
* 21 Mar 2016 - Added IPython notebook to demonstrate how to backtest simple FX trend following trading strategy
* 19 Mar 2016 - Tested with Python 3.5 64 bit (Anaconda 2.5 on Windows 10)
* 17 Mar 2016 - Refactored some of graph/time series functions and StrategyTemplate
* 11 Mar 2016 - Fixed warnings in matplotlib 1.5
* 09 Mar 2016 - Added more TradeAnalysis features (for sensitivity analysis of trading strategies)
* 01 Mar 2016 - Added IPython notebook to demonstrate how to download market data and plot
* 27 Feb 2016 - Fixed total returns FX example
* 20 Feb 2016 - Added more parameters for StrategyTemplate
* 13 Feb 2016 - Edited time series filter methods
* 11 Feb 2016 - Added example to plot BoJ interventions against USDJPY spot
* 10 Feb 2016 - Updated project description
* 01 Feb 2016 - Added LightEventsFactory to make it easier to deal with econ data events (stored as HDF5 files)
* 20 Jan 2016 - Added kurtosis measure for trading strategy results, fixed Quandl issue
* 19 Jan 2016 - Changed examples folder name
* 15 Jan 2016 - Added risk on/off FX correlation example
* 05 Jan 2016 - Added total return (spot) indices construction for FX and example
* 26 Dec 2015 - Fixed problem with econ data downloaders
* 24 Dec 2015 - Added datafactory templates for creating custom indicators
* 19 Dec 2015 - Refactored Dukascopy downloader
* 10 Dec 2015 - Various bug fixes
* 22 Nov 2015 - Increased vol targeting features for doing backtesting
* 07 Nov 2015 - Added feature to download tick data from Bloomberg (with example)
* 05 Nov 2015 - Added intraday event study class (and example)
* 02 Nov 2015 - Added easy wrapper for doing rolling correlations (and example)
* 28 Oct 2015 - Added more sensitivity analysis for trading strategies
* 26 Oct 2015 - Various bug fixes for Bloomberg Open API downloader
* 14 Oct 2015 - Added capability to do parallel downloading of market data (thread/multiprocessing library), with an
example for benchmarking and bug fixes for Bloomberg downloader
* 25 Sep 2015 - Refactored examples into different folders / more seasonality examples
* 19 Sep 2015 - Added support for Plotly choropleth map plots & easy downloading of economic data via FRED/Bloomberg/Quandl
* 12 Sep 2015 - Added basic support for PyFolio for statistical analysis of strategies
* 04 Sep 2015 - Added StrategyTemplate for backtesting (with example) & bug fixes
* 21 Aug 2015 - Added stacked charts (with matplotlib & bokeh) & several bug fixes
* 15 Aug 2015 - Added bar charts (with matplotlib & bokeh) & added more time series filter functions
* 09 Aug 2015 - Improved Bokeh support
* 07 Aug 2015 - Added Plotly support (via Jorge Santos Cufflinks wrapper)
* 04 Aug 2015 - Added ability to download from FRED and example for downloading from FRED.
* 29 Jul 2015 - Added backtesting functions (including simple FX trend following strategy) and various bug fixes/comments.
* 24 Jul 2015 - Added functions for doing simple seasonality studies and added examples.
* 17 Jul 2015 - Created example to show how to use technical indicators.
* 13 Jul 2015 - Changed location of conf, renamed examples folder to pythalesians_examples. Can now be installed using setup.py.
* 10 Jul 2015 - Added ability to download Dukascopy FX tick data (data is free for personal use - check Dukascopy terms & conditions). Note that past month of data is generally not made available by Dukascopy

End of note

### Core Implementation Code & Architecture
#### File: `tests/test_backtestengine.py`
```python

```

#### File: `tests/__init__.py`
```python

```

#### File: `finmarketpy_examples/__init__.py`
```python

```

#### File: `finmarketpy_examples/gallery/__init__.py`
```python

```

#### File: `finmarketpy_examples/finmarketpy_notebooks/__init__.py`
```python

```

#### File: `src/finmarketpy/util/__init__.py`
```python

```


==================================================


## [2/3] Repository: gluonts (`WHEEL_gluonts`)
- **Full Name**: `gluonts`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<img class="hide-on-website" height="100px" src="https://ts.gluon.ai/dev/_static/gluonts.svg">

# GluonTS - Probabilistic Time Series Modeling in Python

[![PyPI](https://img.shields.io/pypi/v/gluonts.svg?style=flat-square&color=b75347)](https://pypi.org/project/gluonts/)
[![GitHub](https://img.shields.io/github/license/awslabs/gluonts.svg?style=flat-square&color=df7e66)](./LICENSE)
[![Static](https://img.shields.io/static/v1?label=docs&message=stable&color=edc775&style=flat-square)](https://ts.gluon.ai/)
[![Static](https://img.shields.io/static/v1?label=docs&message=dev&color=edc775&style=flat-square)](https://ts.gluon.ai/dev/)
[![PyPI Downloads](https://static.pepy.tech/badge/gluonts/month)](https://pepy.tech/projects/gluonts)

**📢 BREAKING NEWS**: We released **Chronos**, a suite of pretrained models for zero-shot time series forecasting. Chronos can generate accurate probabilistic predictions for new time series not seen during training. Check it out [here](https://github.com/amazon-science/chronos-forecasting)!

GluonTS is a Python package for probabilistic time series modeling, focusing on deep learning based models,
based on [PyTorch](https://pytorch.org).


## Installation

GluonTS requires Python 3.10 to 3.14. We recommend using
[uv](https://github.com/astral-sh/uv) for managing environments:

```bash
# install with support for torch models
uv pip install "gluonts[torch]"
```

For development:

```bash
# clone the repository
git clone https://github.com/awslabs/gluonts.git
cd gluonts

# install with all development dependencies
uv sync --all-extras
```

You can also install via `pip`:

```bash
pip install "gluonts[torch]"
```

See the [documentation](https://ts.gluon.ai/stable/getting_started/install.html)
for more info on how GluonTS can be installed.

## Simple Example

To illustrate how to use GluonTS, we train a DeepAR-model and make predictions
using the airpassengers dataset. The dataset consists of a single time
series of monthly passenger numbers between 1949 and 1960. We train the model
on the first nine years and make predictions for the remaining three years.

```py
import pandas as pd
import matplotlib.pyplot as plt

from gluonts.dataset.pandas import PandasDataset
from gluonts.dataset.split import split
from gluonts.torch import DeepAREstimator

# Load data from a CSV file into a PandasDataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/AileenNielsen/"
    "TimeSeriesAnalysisWithPython/master/data/AirPassengers.csv",
    index_col=0,
    parse_dates=True,
)
dataset = PandasDataset(df, target="#Passengers")

# Split the data for training and testing
training_data, test_gen = split(dataset, offset=-36)
test_data = test_gen.generate_instances(prediction_length=12, windows=3)

# Train the model and make predictions
model = DeepAREstimator(
    prediction_length=12, freq="M", trainer_kwargs={"max_epochs": 5}
).train(training_data)

forecasts = list(model.predict(test_data.input))

# Plot predictions
plt.plot(df["1954":], color="black")
for forecast in forecasts:
  forecast.plot()
plt.legend(["True values"], loc="upper left", fontsize="xx-large")
plt.show()
```

![[train-test]](https://ts.gluon.ai/static/README/forecasts.png)

Note, the forecasts are displayed in terms of a probability distribution and
the shaded areas represent the 50% and 90% prediction intervals.


## Contributing

If you wish to contribute to the project, please refer to our
[contribution guidelines](https://github.com/awslabs/gluonts/tree/dev/CONTRIBUTING.md).

## Citing

If you use GluonTS in a scientific publication, we encourage you to add the following references to the related papers,
in addition to any model-specific references that are relevant for your work:

```bibtex
@article{gluonts_jmlr,
  author  = {Alexander Alexandrov and Konstantinos Benidis and Michael Bohlke-Schneider
    and Valentin Flunkert and Jan Gasthaus and Tim Januschowski and Danielle C. Maddix
    and Syama Rangapuram and David Salinas and Jasper Schulz and Lorenzo Stella and
    Ali Caner Türkmen and Yuyang Wang},
  title   = {{GluonTS: Probabilistic and Neural Time Series Modeling in Python}},
  journal = {Journal of Machine Learning Research},
  year    = {2020},
  volume  = {21},
  number  = {116},
  pages   = {1-6},
  url     = {http://jmlr.org/papers/v21/19-820.html}
}
```

```bibtex
@article{gluonts_arxiv,
  author  = {Alexandrov, A. and Benidis, K. and Bohlke-Schneider, M. and
    Flunkert, V. and Gasthaus, J. and Januschowski, T. and Maddix, D. C.
    and Rangapuram, S. and Salinas, D. and Schulz, J. and Stella, L. and
    Türkmen, A. C. and Wang, Y.},
  title   = {{GluonTS: Probabilistic Time Series Modeling in Python}},
  journal = {arXiv preprint arXiv:1906.05264},
  year    = {2019}
}
```

## Links

### Documentation

* [Documentation (stable)](https://ts.gluon.ai/stable/)
* [Documentation (development)](https://ts.gluon.ai/dev/)

### References

* [JMLR MLOSS Paper](http://www.jmlr.org/papers/v21/19-820.html)
* [ArXiv Paper](https://arxiv.org/abs/1906.05264)
* [Collected Papers from the group behind GluonTS](https://github.com/awslabs/gluonts/tree/dev/REFERENCES.md): a bibliography.

### Tutorials and Workshops

* [Tutorial at IJCAI 2021 (with videos)](https://lovvge.github.io/Forecasting-Tutorial-IJCAI-2021/) with [YouTube link](https://youtu.be/AB3I9pdT46c). 
* [Tutorial at WWW 2020 (with videos)](https://lovvge.github.io/Forecasting-Tutorial-WWW-2020/)
* [Tutorial at SIGMOD 2019](https://lovvge.github.io/Forecasting-Tutorials/SIGMOD-2019/)
* [Tutorial at KDD 2019](https://lovvge.github.io/Forecasting-Tutorial-KDD-2019/)
* [Tutorial at VLDB 2018](https://lovvge.github.io/Forecasting-Tutorial-VLDB-2018/)
* [Neural Time Series with GluonTS](https://youtu.be/beEJMIt9xJ8)
* [International Symposium of Forecasting: Deep Learning for Forecasting workshop](https://lostella.github.io/ISF-2020-Deep-Learning-Workshop/)

### Core Implementation Code & Architecture
#### File: `src/gluonts/nursery/robust-mts-attack/attack_params/attack_config_traffic_4.json`
```python
{ 
    "factor":
        2.0,
    "max_norm":
        0.5,
    "sparsity": [
        1,
        3,
        5,
        7,
        9
    ],
    "attack_items":[
        1,
        2,
        3,
        5,
        6,
        7,
        8,
        9
    ],
    "target_items": [
        0, 4
    ],
    "attack_idx": [
        -2, -1
    ],
    "n_iterations": 100,
    "learning_rate": 0.01,
    "modes": [
        "under",
        "over"
    ],
    "sigma": 0.1
}
```

#### File: `src/gluonts/nursery/robust-mts-attack/attack_params/attack_config_electricity_3.json`
```python
{
    "factor":
        2.0,
    "max_norm":
        0.5,
    "sparsity": [
        1,
        3,
        5,
        7,
        9
    ],
    "attack_items":[
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
    ],
    "target_items": [
        0
    ],
    "attack_idx": [
        -1
    ],
    "n_iterations": 100,
    "learning_rate": 0.01,
    "modes": [
        "under",
        "over"
    ],
    "sigma":
        0.1
}
```

#### File: `src/gluonts/nursery/robust-mts-attack/attack_params/attack_config_taxi_2.json`
```python
{
    "factor":
        2.0,
    "max_norm":
        0.5,
    "sparsity": [
        1,
        3,
        5,
        7,
        9
    ],
    "attack_items":[
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
    ],
    "target_items": [
        0
    ],
    "attack_idx": [
        -1
    ],
    "n_iterations": 100,
    "learning_rate": 0.01,
    "modes": [
        "under",
        "over"
    ],
    "sigma":
        0.1
}
```

#### File: `src/gluonts/nursery/robust-mts-attack/attack_params/attack_config_wiki_9.json`
```python
{
    "factor":
        2.0,
    "max_norm":
        2.0,
    "sparsity": [
        1,
        3,
        5,
        7,
        9
    ],
    "attack_items":[
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
    ],
    "target_items": [
        0
    ],
    "attack_idx": [
        -1
    ],
    "n_iterations": 100,
    "learning_rate": 0.01,
    "modes": [
        "under",
        "over"
    ],
    "sigma":
        0.1
}
```

#### File: `src/gluonts/nursery/robust-mts-attack/attack_modules/__init__.py`
```python
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
```

#### File: `src/gluonts/nursery/robust-mts-attack/multivariate/__init__.py`
```python
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
```


==================================================


## [3/3] Repository: hikyuu (`WHEEL_hikyuu`)
- **Full Name**: `hikyuu`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
![title](docs/source/_static/00000-title.png)

---

![img](https://static.pepy.tech/badge/hikyuu) ![img](https://static.pepy.tech/badge/hikyuu/month) ![img](https://static.pepy.tech/badge/hikyuu/week) ![img](https://github.com/fasiondog/hikyuu/workflows/win-build/badge.svg) ![img](https://github.com/fasiondog/hikyuu/workflows/ubuntu-build/badge.svg) ![License](https://img.shields.io/github/license/fasiondog/hikyuu.svg)

## ⚡ Hikyuu Ultra-Fast Quant Framework

> 基于 C++/Python 开发的开源超高速量化交易研究框架，聚焦策略分析、回测与实盘能力扩展（深度适配国内 A 股市场）。核心能力覆盖四大维度：**交易模型研发 · 极速计算引擎 · 高效回测体系 · 实盘交易拓展**。

框架依托成熟的系统化交易研究理念，将量化分析体系拆解为 **市场环境研判、策略生效条件判定、信号指标解析、盈亏风控模型、资金配比模型、收益目标测算、滑点模拟算法、多因子建模、投资组合分析、资金分配** 等独立模块化组件。用户可自由组合模块、搭建专属策略模型库，通过模拟回测验证策略稳定性与有效性，完成量化策略研究与数据分析工作。同时框架预留拓展接口，支持开发者自主开发、对接合规的第三方交易接口（如 QMT 等官方合规终端接口），满足个性化技术拓展与私有适配需求。

> ⚠️ **免责声明**：本项目为开源金融技术研究工具，仅供个人学习、学术研究与数据分析使用，不构成任何投资建议与交易指导，不提供、不内置证券交易服务。框架仅提供通用接口拓展能力，仅建议用户对接持牌机构提供的合规交易终端接口；用户自主新增、对接各类交易接口、开发拓展功能以及对应的实操行为，均由用户自行承担全部风险与法律责任，严禁对接非法交易通道、用于违规交易场景。

---

## 📊 关键数据

<p align="center">
  <table>
    <tr>
      <td align="center" width="33%">
        <strong><code>⚡ 166ms</code></strong><br>
        <sub>预热后 1913 万 K 线求和耗时（AMD 7950x）</sub>
      </td>
      <td align="center" width="33%">
        <strong><code>🧩 10+</code></strong><br>
        <sub>核心策略组件 · 自由组合构建资产库</sub>
      </td>
      <td align="center" width="33%">
        <strong><code>💾 4 种</code></strong><br>
        <sub>存储方式（HDF5 / MySQL / ClickHouse / SQLite）</sub>
      </td>
    </tr>
  </table>
</p>

---

## 🔗 快速导航

| 项目                          | 链接                                                                                                                                           |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 🏠**项目首页**          | [https://hikyuu.org/](https://hikyuu.org/)                                                                                                      |
| 📚**帮助文档**          | [https://hikyuu.readthedocs.io/zh-cn/latest/index.html](https://hikyuu.readthedocs.io/zh-cn/latest/index.html)                                  |
| 🚀**入门示例**          | [Jupyter Notebook 系列教程](https://nbviewer.org/github/fasiondog/hikyuu/blob/master/hikyuu/examples/notebook/000-Index.ipynb?flush_cache=True) |
| 🧰**策略部件库**        | [https://gitee.com/fasiondog/hikyuu_hub](https://gitee.com/fasiondog/hikyuu_hub)                                                                |
| 🐧**Ubuntu 虚拟机环境** | [百度网盘下载（提取码: ht8j）](https://pan.baidu.com/s/1CAiUWDdgV0c0VhPpe4AgVw?pwd=ht8j)                                                        |

---

## ⚡ 快速开始（跑通第一个回测）

### 环境要求

- **>= Python 3.10**（3.9 及以下自 2.8.0 起不再支持 pip 安装）
- 支持 Windows / Linux / macOS （Linux为Ubuntu24.04+）
- 主要依赖会自动安装：`numpy>=2.0`、`pandas>=2.3.0`、`matplotlib>=3.5.0`、`PySide6>=6.8.0`、`tables>=3.9.0` 等

### 第 1 步：安装

```bash
pip install hikyuu
```

国内用户若下载缓慢，可换用镜像源：

```bash
pip install hikyuu -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 第 2 步：导入行情数据

任选一种方式导入历史行情数据：

```bash
# 图形界面（推荐首次使用，会自动生成配置文件）
HikyuuTDX

# 命令行（需先运行过一次 HikyuuTDX 生成配置）
importdata
```

### 第 3 步：跑通第一个回测

```python
from hikyuu.interactive import *

# 创建模拟交易账户进行回测，初始资金 30 万
my_tm = crtTM(init_cash=300000)

# 创建信号指示器（以 5 日 EMA 为快线，其 10 日 EMA 为慢线）
# 快线向上穿越慢线时买入，反之卖出
my_sg = SG_Flex(EMA(CLOSE(), n=5), slow_n=10)

# 固定每次买入 1000 股
my_mm = MM_FixedCount(1000)

# 创建交易系统并运行
sys = SYS_Simple(tm=my_tm, sg=my_sg, mm=my_mm)
sys.run(sm['sz000001'], Query(-150))
```

> 📖 完整示例参见 [Jupyter Notebook 系列教程](https://nbviewer.org/github/fasiondog/hikyuu/blob/master/hikyuu/examples/notebook/000-Index.ipynb?flush_cache=True)

### ❓ 上手常见问题

| 现象                                              | 解决办法                                                                     |
| :------------------------------------------------ | :--------------------------------------------------------------------------- |
| Windows 下`pip install` 卡在下载 PyQt / PySide6 | 换清华源：`pip install hikyuu -i https://pypi.tuna.tsinghua.edu.cn/simple` |
| `HikyuuTDX` 图形界面无法导入数据                | 改用命令行`importdata`（需先运行过一次 GUI 以生成配置文件）                |
| 提示缺少 hdf5 / dll 相关错误                      | 执行`pip install tables` 重新安装 HDF5 支持                                |
| **从源码构建**时的构建工具                  | 本项目使用**xmake**，不是 cmake                                        |

> 💡 更多问题请查 [帮助文档](https://hikyuu.readthedocs.io/zh-cn/latest/index.html)，或在 [Gitee 提交 issue](https://gitee.com/fasiondog/hikyuu/issues)。

---

## 🚀 为什么选择 Hikyuu？

> 强大的功能特性，助力您的量化交易研究

### 💹 组合灵活，分类构建策略资产库

对系统化交易方法进行轻量化抽象，涵盖 **市场环境判断、系统有效条件、信号指示器、止损 / 止盈策略、资金管理、盈利目标、滑点算法、交易对象筛选、资金分配** 等核心组件。你可以基于这些组件自由搭建专属策略库，灵活组合、高效回测，并在策略探索时专注于单一模块的效果与影响，大幅提升研究效率。

<p align="center">
  <img src="docs/source/_static/10002-function-arc.png" alt="功能架构" width="800">
</p>

### 🚀 极致性能，轻松构建专属量化应用

项目由三大部分构成：**高性能 C++ 核心库**、**Python 接口层（hikyuu）**、以及**交互式探索工具**。

- **AMD 7950x 实测**：A 股全市场 1913 万日 K 线，首次加载 + 计算 20 日均线并求和，仅需 **6 秒**；数据预热后，同操作耗时仅需 **166 毫秒**。
  > [📊 性能实测详情](https://mp.weixin.qq.com/s?__biz=MzkwMzY1NzYxMA==&mid=2247483768&idx=1&sn=33e40aa9633857fa7b4c7ded51c95ae7&chksm=c093a09df7e4298b3f543121ba01334c0f8bf76e75c643afd6fc53aea1792ebb92de9a32c2be&mpshare=1&scene=23&srcid=05297ByHT6DEv6XAmyje1oOr&sharer_shareinfo=b38f5f91b4efd8fb60303a4ef4774748&sharer_shareinfo_first=b38f5f91b4efd8fb60303a4ef4774748#rd)
  >
- **C++ 核心库**：内置完整策略框架，原生支持多线程与多核加速，为超高算力场景预留扩展空间；核心库可独立剥离使用，帮助开发者快速构建自定义量化工具。
- **Python 接口层（hikyuu）**：对 C++ 核心进行轻量化封装，集成 TA-Lib，支持与 numpy、pandas 无缝互转，轻松对接主流 Python 数据分析生态。
- **hikyuu.interactive**：交互式探索工具，内置 K 线、指标、信号可视化能力，适合快速策略验证与回测分析。

### 🍳 语法简洁，策略探索更高效自由

同时支持 **面向对象** 与 **命令行** 两种编程范式。尤其在策略探索阶段，命令行风格语法极简、表达直观，让你更快验证想法、迭代策略。

### 🔐 自主可控，搭建专属云量化平台

结合 **Python + Jupyter** 与云服务器，即可搭建完全自主可控的云量化平台。部署后随时随地访问（手机、平板、电脑均可使用），快速落地新想法。同时可无缝对接 **numpy、scipy、pandas、TensorFlow** 等成熟 AI 与数据分析工具，构建智能量化系统。也可按需自定义界面、实现服务化部署。

### 🎁 模块化可扩展数据存储

目前支持 **本地 HDF5、MySQL、ClickHouse、SQLite** 四种存储方式，默认采用 HDF5（文件体积小、读写速度快、备份便捷）。截至 2017 年 4 月 21 日，沪市日线数据文件仅 149MB，深市 184MB，5 分钟线数据整体小于 2GB。通过插件可扩展 ClickHouse 存储，其读写速度优于 HDF5、空间占用远低于 MySQL，更适配分钟级及以下粒度的高频数据存储。

### 🔓 开源透明，数据安全可控

**Apache 2.0** 开源协议，代码透明审计无忧。核心数据、策略全量本地可控，C++ 核心库可独立剥离使用，自由打造专属客户端工具，无需担心第三方平台限制。

---

## 💻 简洁的 API 设计

几行代码即可创建一个完整的量化策略回测系统。Hikyuu 提供直观的 API，让策略开发更高效。

```python
from hikyuu.interactive import *

# 创建模拟交易账户进行回测，初始资金30万
my_tm = crtTM(init_cash=300000)

# 创建信号指示器（以5日EMA为快线，5日EMA自身的10日EMA作为慢线）
# 快线向上穿越慢线时买入，反之卖出
my_sg = SG_Flex(EMA(CLOSE(), n=5), slow_n=10)

# 固定每次买入1000股
my_mm = MM_FixedCount(1000)

# 创建交易系统并运行
sys = SYS_Simple(tm=my_tm, sg=my_sg, mm=my_mm)
sys.run(sm['sz000001'], Query(-150))
```

<p align="center">
  <img src="docs/source/_static/10000-overview.png" alt="回测结果示意" width="900">
</p>

> 📖 **完整示例参见**：[Jupyter Notebook 系列教程](https://nbviewer.jupyter.org/github/fasiondog/hikyuu/blob/master/hikyuu/examples/notebook/000-Index.ipynb?flush_cache=True)

---

## 🏗️ 交易系统化架构核心组件

> 遵循系统化交易理念严谨架构，每个组件可独立替换、自由组合

| 层级                   | 组件                             | 说明                             |
| :--------------------- | :------------------------------- | :------------------------------- |
| **投资组合层**   | <b> · PortfolioPF</a>           | 投资组合 - 多系统的策略调度      |
|                        | <b> · SelectorSE</a>            | 系统对象选择 - 系统策略筛选      |
|                        | <b> · AllocateFundsAF</a>       | 资金分配 - 多系统的资金分配      |
|                        | <b> · MultiFactorMF</a>         | 多因子模型 - 因子评分与排序      |
| **交易系统 SYS** | <b> · EnvironmentEV</a>         | 市场环境判断 - 大盘环境有效性    |
|                        | <b> · ConditionCN</a>           | 系统有效条件 - 系统适用条件      |
|                        | <b> · SignalSG</a>              | 信号指示器 - 产生买卖信号        |
|                        | <b> · Stoploss/StopprofitST</a> | 止损 / 止盈 - 风险控制退出       |
|                        | <b> · MoneyManagerMM</a>        | 资金管理 - 买卖数量控制          |
|                        | <b> · ProfitGoalPG</a>          | 盈利目标 - 目标达成退出          |
|                        | <b> · SlippageSP</a>            | 移滑价差 - 回测价格模拟          |
| **交易管理**     | <b> · TradeManagerTM</a>        | 交易管理 - 账户资金与持仓记录    |
|                        | <b> · OrderBrokerOB</a>         | 订单执行 - 实盘下单 broker 对接  |
| **数据层**       | <b> · StockManagerSM</a>        | 证券管理 - StockManager 统一管理 |
|                        | <b> · KDataKD</a>               | K 线数据 - KData 量价序列        |
|                        | <b> · QueryQ</a>                | 数据查询 - Query 时间范围筛选    |

---

## 📂 浏览源码

> 欢迎 **Star ⭐**、**Fork 🍴**，参与贡献

| 平台                 | 链接                                                                      | 推荐    |
| :------------------- | :------------------------------------------------------------------------ | :------ |
| **码云 Gitee** | [https://gitee.com/fasiondog/hikyuu](https://gitee.com/fasiondog/hikyuu)   | ✅ 推荐 |
| **GitHub**     | [https://github.com/fasiondog/hikyuu](https://github.com/fasiondog/hikyuu) |         |
| **GitCode**    | [https://gitcode.com/hikyuu/hikyuu](https://gitcode.com/hikyuu/hikyuu)     |         |

---

## ❤️ 感谢捐赠，让 Hikyuu 走得更远

<p align="center">
  <img src="docs/source/_static/dingyue.png" alt="订阅二维码" width="600">
</p>

| 方案                       | 说明                                                                                            | 方式               | 链接                                       |
| :------------------------- | :---------------------------------------------------------------------------------------------- | :----------------- | :----------------------------------------- |
| ☕**请作者喝杯咖啡** | ¥30 · 一次性的小小支持(赠历史日线)                                                            | 支付宝             | [前往捐赠](https://pay.ldxp.cn/item/gflv3v) |
| 📅**订阅 180 天**    | ¥50 · 半年期订阅权益(赠历史日线)                                                              | 支付宝             | [前往捐赠](https://pay.ldxp.cn/item/du4h8s) |
| 🗓️**订阅 365 天**  | ¥100 · 全年期订阅权益(赠历史日/分/时/笔数据)                                                  | 支付宝             | [前往捐赠](https://pay.ldxp.cn/item/ehbz9b) |
| 🌌**加入知识星球**   | ¥300/年 · 首年300元，续费半价。3台设备登录 · 专属微信群及策略部件库，(赠历史日/分/时/笔数据) | 微信 / 知识星球APP | [前往加入](https://t.zsxq.com/YSATD)        |

> 🎁 **捐赠计划与附赠详见**：[https://hikyuu.readthedocs.io/zh-cn/latest/vip/donate-plan.html](https://hikyuu.readthedocs.io/zh-cn/latest/vip/donate-plan.html)

捐赠用户支持群（仅接受捐赠用户，入群请注明： Hikyuu 订阅）

<p align="center">
  <img src="docs/source/_static/support.jpg" alt="捐赠用户支持" width="150">
</p>

## 🌟 需要的帮助

欢迎社区成员一起参与贡献：

- 🐛 测试反馈 BUG
- 📝 编写文档
- 🔧 开发新功能
- 🎨 网站优化

> 💡 **建议通过在Github/Gitee/Gitcode开 issue 方式来贡献以上内容**

---

## 📦 项目依赖说明

Hikyuu 的 C++ 核心模块直接依赖以下开源项目（间接依赖项及 Python 侧依赖未列出；Python 依赖可参考 requirements.txt 文件）。在此感谢所有开源作者的贡献 🙏

| 名称          | 项目地址                                                                            | License                                                                                 |
| :------------ | :---------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| xmake         | [https://github.com/xmake-io/xmake](https://github.com/xmake-io/xmake)               | Apache 2.0                                                                              |
| hdf5          | [https://github.com/HDFGroup/hdf5](https://github.com/HDFGroup/hdf5)                 | [hdf5 license](https://github.com/HDFGroup/hdf5?tab=License-1-ov-file#License-1-ov-file) |
| mysql(client) | [https://github.com/mysql/mysql-server](https://github.com/mysql/mysql-server)       | [mysql license](https://github.com/mysql/mysql-server?tab=License-1-ov-file#readme)      |
| fmt           | [https://github.com/fmtlib/fmt](https://github.com/fmtlib/fmt)                       | [fmt license](https://github.com/fmtlib/fmt?tab=License-1-ov-file#readme)                |
| spdlog        | [https://github.com/gabime/spdlog](https://github.com/gabime/spdlog)                 | MIT                                                                                     |
| sqlite        | [https://www.sqlite.org/](https://www.sqlite.org/)                                   | [sqlite license](https://www.sqlite.org/copyright.html)                                  |
| flatbuffers   | [https://github.com/google/flatbuffers](https://github.com/google/flatbuffers)       | Apache 2.0                                                                              |
| nng           | [https://github.com/nanomsg/nng](https://github.com/nanomsg/nng)                     | MIT                                                                                     |
| nlohmann_json | [https://github.com/nlohmann/json](https://github.com/nlohmann/json)                 | MIT                                                                                     |
| boost         | [https://www.boost.org/](https://www.boost.org/)                                     | [Boost Software License](https://www.boost.org/users/license.html)                       |
| python        | [https://www.python.org/](https://www.python.org/)                                   | [Python license](https://docs.python.org/3/license.html)                                 |
| pybind11      | [https://github.com/pybind/pybind11](https://github.com/pybind/pybind11)             | [pybind11 license](https://github.com/pybind/pybind11?tab=License-1-ov-file#readme)      |
| gzip-hpp      | [https://github.com/mapbox/gzip-hpp](https://github.com/mapbox/gzip-hpp)             | BSD-2-Clause license                                                                    |
| doctest       | [https://github.com/doctest/doctest](https://github.com/doctest/doctest)             | MIT                                                                                     |
| ta-lib        | [https://github.com/TA-Lib/ta-lib](https://github.com/TA-Lib/ta-lib)                 | BSD-3-Clause license                                                                    |
| clickhouse    | [https://github.com/ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | Apache 2.0                                                                              |
| xxhash        | [https://github.com/Cyan4973/xxHash](https://github.com/Cyan4973/xxHash)             | BSD 2-Clause License                                                                    |
| utf8proc      | [https://github.com/JuliaStrings/utf8proc](https://github.com/JuliaStrings/utf8proc) | MIT                                                                                     |
| arrow         | [https://github.com/apache/arrow](https://github.com/apache/arrow)                   | Apache 2.0                                                                              |
| eigen         | [https://gitlab.com/libeigen/eigen](https://gitlab.com/libeigen/eigen)               | Apache 2.0                                                                              |
| mimalloc      | [https://github.com/microsoft/mimalloc](https://github.com/microsoft/mimalloc)       | MIT                                                                                     |

---

<p align="center">
  <table>
    <tr>
      <td align="center" width="33%">
        <a href="https://hikyuu.readthedocs.io/zh-cn/latest/index.html">📚 文档</a>
      </td>
      <td align="center" width="33%">
        <a href="https://gitee.com/fasiondog/hikyuu">💻 Gitee</a>
      </td>
      <td align="center" width="33%">
        <a href="https://github.com/fasiondog/hikyuu">🐙 GitHub</a>
      </td>
    </tr>
  </table>
</p>

<p align="center">
  基于 <a href="https://github.com/fasiondog/hikyuu/blob/master/LICENSE">Apache License V2</a> 开源协议发布 · 由 <a href="https://github.com/fasiondog">fasiondog</a> 维护
</p>

### Core Implementation Code & Architecture
#### File: `hikyuu/test/__init__.py`
```python

```

#### File: `hikyuu/config/block/__init__.py`
```python

```

#### File: `hikyuu/shell/__init__.py`
```python

```

#### File: `hikyuu/cpp/i18n/__init__.py`
```python

```

#### File: `hikyuu/cpp/i18n/zh_CN/__init__.py`
```python

```

#### File: `hikyuu/draw/drawplot/icon/__init__.py`
```python

```


==================================================
