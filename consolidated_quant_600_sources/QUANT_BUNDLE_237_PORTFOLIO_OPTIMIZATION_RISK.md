# ⚡ [QUANT-SOURCE-237] Consolidated Quant & Algo Trading Repositories
**Category**: `PORTFOLIO_OPTIMIZATION_RISK` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_237_PORTFOLIO_OPTIMIZATION_RISK.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: OptimalPortfolio (`PHASE4-QUANT-091`)
- **Full Name**: `PHASE4-QUANT-091_VivekPa__OptimalPortfolio`
- **Description**: An open source library for portfolio optimisation
- **GitHub Stars**: 373
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Optimal Portfolio

<p align="left">
    <a href="https://www.python.org/">
        <img src="https://ForTheBadge.com/images/badges/made-with-python.svg"
            alt="python"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square"
            alt="MIT license"></a> &nbsp;
</p>

**OptimalPortfolio** is an open source library for portfolio optimisation. This library implements classical portfolio optimisation techniques for equities, but is also extendable for non-equity products given the right adjustments in invariants. Furthermore, certain modern advances in portfolio optimisation, such as Hierarchical Risk Parity is also implemented. 

Regardless of whether you are a fundamental investor, or an algorithmic trader, this library can aid you in allocating your capital in the most risk efficient way, allowing to optimise your utility. *For more details on the project design and similar content, please check out [Engineer Quant](https://medium.com/engineer-quant)*

*Disclaimer: This is not trading or investment advice. Trading involves significant risk and do so at your risk.*


## Contents
- [Contents](#contents)
- [Overview](#overview)
- [Full Sequence](#full-sequence)
- [Functionality](#functionality)
  - [Expected Returns](#expected-returns)
  - [Risk Models](#risk-models)
  - [Objective Functions](#objective-functions)
  - [Constraints](#constraints)
- [Market Invariants](#market-invariants)
- [Moment Estimation](#moment-estimation)
    - [Nonparametric Estimators](#nonparametric-estimators)
    - [Maximum Likelihood Estimators](#maximum-likelihood-estimators)
    - [Shrinkage Estimators](#shrinkage-estimators)
- [Optimal Allocations](#optimal-allocations)
    - [Higher Moment Optimisation](#higher-moment-optimisation)
    - [Compared to Sharpe Ratio](#compared-to-sharpe-ratio)
- [Roadmap](#roadmap)

## Overview
This library aims to make optimising portfolios accessible to every trader and investor. To install this library, download it and run
```bash
bash install.sh
```

## Full Sequence
The pipeline for using this library is delibrately modular, so as to allow users to incorporate their own proprietary stacks and code into the optimisation. The full sequence from data to weights is in the ``examples/full_sequence.ipynb`` notebook, but for clarity, it is

- Acquire stock (or other asset class) data
- Calculate market invariants (for stocks is returns)
- Calculate moments of invariants (for simple mean-variance optimisation it is mean and covariance)
- Optimise weights according to a utility function, subject to constraints, with moments of invariants as inputs

```python
import pandas as pd
import numpy as np

import PortOpt.invariants as invs
import PortOpt.moment_est as moments
from PortOpt.opt_allocations import Optimiser
import PortOpt.utility_functions as utils

tickers = ['AAPL', 'MSFT', 'CVX', 'GE', 'GOOGL']
stock_data = utils.get_data(tickers, '1d', '2015-01-01', '2021-01-01')

# Compute market invariants

stock_returns = invs.stock_invariants(stock_data)

riskmodel = moments.RiskModel(tickers)
stock_cov = riskmodel.avg_hist_cov(stock_data)

# Optimise weights according to mean-variance

optimiser = Optimiser(tickers, exp_returns, stock_cov)
weights = optimiser.mean_variance(threshold=0.1, type='variance')
print(weights)
weight_tearsheet(weights)
```

This should have the following output:
```txt
AAPL     0.182566
MSFT     0.143655
CVX      0.190582
GE       0.117543
GOOGL    0.365654

Annual Return: 15.026
Annual Volatility: 23.203
Annual Sharpe: 0.561
```

## Functionality

Listed below is the current overall functionality of the library, split into the various parts of the pipeline.

### Expected Returns
- Nonparametric
  - Mean Historical Returns
  - Mean Exponentially Weighted Returns
  - Capital Asset Pricing Model (CAPM)
- Shrinkage
  - James-Stein Mean Shrinkage

### Risk Models
- Nonparametric
  - Historical Covariance
  - Exponentially Weighted Covariance
- Covariance Shrinkage
    - Identity Shrinkage
    - Scaled Variance Shrinkage
    - Ledoit-Wolf Single Index
    - Ledoit-Wolf Constant Correlation

### Objective Functions
- Mean-Variance Optimisation
  - Maximise Returns with a risk limit
  - Minimise risk with a returns limit
- Minimum Volatility
- Maximum Sharpe Ratio

### Constraints
- Long Short Neutral
- Maximum Position on an asset

### Adding Custom Constraints/Objectives
Since constraints are very case specific, I have added a functionality to be able to add your own constraints to the optimisation problem. We add a long/short neutral constraint using the custom method to demonstrate

```python
optimiser = Optimiser(tickers, exp_returns, stock_cov)

# Add LS neutral constraint
optimiser.add_constraints([lambda x: cp.sum(x) == 0])

# Optimise for mean-variance
weights = optimiser.mean_variance(threshold=0.1, type='variance')
print(weights)
weight_tearsheet(weights)
```

## Market Invariants
The first step to optimising any portfolio is calculating market invariants. Market invariants are defined as aspects of market prices that have some determinable statistical behaviour over time. For stock prices, the compounded returns are the market invariants. So when we calculate these invariants, we can statistically model them and gain useful insight into their behaviour. So far, calculating market invariants of stock prices. The same can be implemented for options and bonds, but data acquisition is an issue.

## Moment Estimation
Once the market invariants have been calculated, it is time to model the statistical properties of the invariants. This is an actively researched and studied field and due to the nature of the complexity involved in modelling the statistical properties of large market data, there are several limitations in estimating the moments of the distributions.

### Nonparametric Estimators
The simplest method of estimating the mean and covariance of invariants are the sample mean and covariance. However, this can be extended by introducing weightage for the timestamps, i.e giving more weight to recent data than older data. One interesting approach I have taken is introducing exponentially weighted mean and covariance, which I read about [here](https://reasonabledeviations.science/2018/08/15/exponential-covariance/).

<!-- ### Maximum Likelihood Estimators
Maximum likelihood estimators (MLE) are intended to maximise the probability that the data points occur within a prescribed distribution. The procedure hence involves choosing a distribution or a class of distributions and then fitting the data to the distribution such that the log probability of the data points are maximised by the parameters of the distributions. This will in turn give us the optimal estimators of the distribution for market invariants. MLE has been implemented for the following distributions:

- Multivariate Normal
- Multivariate Student t

The MLE estimate for Student-t distribution is computed using Expectation Maximisation (EM)
algorithm.  -->

### Shrinkage Estimators
Nonparametric estimators only converge to the population estimate as the number of independent, identically distribution (IID) data points tends to infinity. However, as anyone who has experimented with financial data will be aware, market data is everchaning, and in some cases the volume of data is minimal. In these circumstances, nonparametric estiamtors do not work as well as intended, and this will cause issues later on in the optimiser. 

One method to circumvent this is to impose some known structure in the market data. This is the essence of shrinkage estimation. We _shrink_ the sample moment towards a structure that we know _a-priori_. 

An example of shrinkage will be Ledoit-Wolf Single-Index Model Covariance Shrinkage. This approach assumes that stock returns are significantly influenced by market returns. So we model the stock returns as a linear regression of market returns:

$$
\hat{r}_{i,t} = \alpha_{i} + \beta_{i} \hat{r}_{m, t} + \epsilon_{i,t}
$$

We calculate \(\beta_i\) and \(\alpha_i\) from regression, and we assume the error \(\epsilon\) is independent and normally distributed, i.e., \(\text{Cov}(\epsilon_i, \epsilon_j) = 0\), \(\text{Cov}(\hat{r}_m, \epsilon_i) = 0\), and \(\mathbb{E}[\epsilon] = 0\), \(\text{Var}(\epsilon) = \sigma_i^2\). Given this, we let the shrinkage matrix be:

$$
F = \beta \beta^T \hat{\sigma}_m^2 + \Sigma_{\epsilon}
$$

where \(\Sigma_{\epsilon}\) is the diagonal matrix of error variances. We can now calculate the shrunk covariance matrix as:

$$
\Sigma = \alpha F + (1 - \alpha) S
$$

We can go a step further by choosing \(\alpha\) optimally, but for the sake of brevity, I will leave that to the interested reader to find. The source papers are in the references directory for those interested.

## Optimal Allocations
Classical asset allocation is the efficient frontier allocation. This is also known as the mean-variance optimisation as it takes into account the estimators of the mean and variance. The procedure of optimisation involves choosing an utility function and optimising it for portfolio weights. So far, I have implmented Mean-Variance, Minimum Volatility and Maximum Sharpe Optimisation. 

### Mean-Variance
Mean-variance optimisation can take on two forms: maximising returns with a variance limit, or minimising variance with a return limit. Both forms call the same ``mean_variance()`` method in the ``Optimiser`` class.

### Minimum Volatility
Minimum volatility optimisation minimises volatility whilst constraining the weights to fit a certain portfolio profile (Long only, Long/Short)

### Maximum Sharpe 
Maximum Sharpe optimisation requires a little more nuance as maximising sharpe ratio is not a convex optimisation problem. Hence, we have to do a variable transformation, with a few assumptions, to convert the problem into a convex optimisation one. 

<!-- ### Higher Moment Optimisation
The core principle of optimisation with higher moments is identical to any other optimisation: given some utility function and constraints, find the weights of each of the portfolio entries such that the utility function is maximised. The only difference is that the utility function in this case would contain as arguments, higher moments. Furthermore, by adding coefficients to each moment, we are able to take into account investor risk aversion and preferences.
This version of the package includes higher moment optimization based on higher co-moments, which makes much more statistical sense than the column-wise higher order moments in the original package.  -->

<!-- ### Compared to Sharpe Ratio
When doing backtests, higher moment optimisation works better than using Sharpe ratio to optimise allocations. -->

## Roadmap
I have the following planned out and am working on implementing them:

<!-- - Market Invariants
  - Calculating invariants for bonds and derivatives -->

- Nonparametric Estimators
  - Exponentially weighted skew and kurtosis
<!-- - Maximum Likelihood Estimators
  - Student-t Distribution
  - Stable Distributions -->
- Shrinkage Estimators
  - Shrinkage for higher moments
  - Optimal shrinkage coefficient for custom shrinkage matrices

- Optimisations
  - Extending Hierarchical Risk Parity
  - Higher Moment Optimisation
  - Backtesting optimisation

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `build/lib/optimalportfolio/__init__.py`
```python

```

#### File: `build/lib/optimalportfolio/risk.py`
```python

```

#### File: `PortOpt/__init__.py`
```python

```

#### File: `PortOpt/test.py`
```python
import pandas as pd
import numpy as np
```

#### File: `build/lib/optimalportfolio/test.py`
```python
import pandas as pd
import numpy as np

prices = pd.read_csv('data/stock_prices.csv')

print(prices.head())
```


==================================================


## [2/3] Repository: FactorHub (`PHASE4-QUANT-092`)
- **Full Name**: `PHASE4-QUANT-092_cn-vhql__FactorHub`
- **Description**: FactorHub is an open-source modern quantitative factor analysis platform designed specifically for the Chinese A-share market.  FactorHub = Factor + Hub  A full-stack quantitative investment research system integrating factor management, analysis, mining, portfolio optimization, and strategy backtesting.
- **GitHub Stars**: 416
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# FactorHub

**FactorHub** is an open-source modern quantitative factor analysis platform designed specifically for the Chinese A-share market.

> FactorHub = Factor + Hub

A full-stack quantitative investment research system integrating factor management, analysis, mining, portfolio optimization, and strategy backtesting.

---

## Language Options

- 🇨🇳 **中文 (Chinese)** - [README_ZH.md](README_ZH.md)
- 🇯🇵 **日本語 (Japanese)** - [README_JP.md](README_JP.md)

---

## Core Value Proposition

| Value Pillar | Description |
|--------------|-------------|
| 🎯 **Complete Factor Lifecycle Management** | Full support from factor creation, validation, analysis to deployment |
| 🧪 **Scientific Factor Evaluation System** | Professional indicators including IC/IR analysis, monotonicity test, turnover analysis |
| 🧬 **Intelligent Factor Mining** | Genetic algorithm-based automated factor mining to discover alpha signals |
| 🤖 **AI Research Assistant** | Supports natural-language factor generation, AI interpretation of analysis results, and report drafting |
| 📊 **Professional Backtesting Engine** | Support for multi-factor combination, strategy comparison, and performance attribution analysis |

---

## Core Features

![1773500695533](image/README_ZH/1773500695533.png)

### 1. Factor Management
- ✅ **Custom Factor Definition** - Supports Tongda Xinhua (MyLanguage) syntax and TALib functions
- ✅ **Formula Validation** - Real-time syntax checking and logical verification
- ✅ **Version Control** - Factor modification history and version rollback
- ✅ **Pre-built Factor Library** - Built-in common technical factors (MA, RSI, MACD, Bollinger Bands, etc.)

![1773500664940](image/README_ZH/1773500664940.png)

### 2. Factor Analysis
- ✅ **IC/IR Analysis** - Information Coefficient and Information Ratio calculation (supports 1-day, 5-day, 10-day prediction cycles)
- ✅ **Factor Exposure Analysis** - Analyze stock exposure distribution on factors
- ✅ **Factor Effectiveness Testing** - Multi-dimensional assessment of factor predictive power
- ✅ **Factor Attribution Analysis** - Decompose factor contribution to returns
- ✅ **Dynamic Monitoring** - Factor performance tracking across time series dimensions

![1773500638704](image/README_ZH/1773500638704.png)

### 3. Factor Mining
- ✅ **Genetic Algorithm Mining** - DEAP-based evolutionary algorithm for automatic factor search
- ✅ **Multi-objective Optimization** - Simultaneously optimize IC, IR, monotonicity, and other objectives
- ✅ **Factor Generation** - Supports basic operators, function calls, and time window operations
- ✅ **Parallel Computing** - Parallel population evaluation for acceleration

![1773500591756](image/README_ZH/1773500591756.png)

### 4. Portfolio Analysis
- ✅ **Multi-factor Portfolio** - Supports equal weight, market cap weighting, IC_IR maximization, etc.
- ✅ **Risk Modeling** - Factor neutralization processing
- ✅ **Optimization Configuration** - Factor weight optimization based on historical performance
- ✅ **Portfolio Performance** - Annual return, Sharpe ratio, maximum drawdown, and other metrics

![1773500498447](image/README_ZH/1773500498447.png)

### 5. Strategy Backtesting
- ✅ **Single Factor Backtesting** - Factor quantile-based stock selection backtesting
- ✅ **Multi-factor Strategies** - Composite factor signal generation
- ✅ **Strategy Comparison** - Multi-strategy parallel backtesting and comparison analysis
- ✅ **Performance Metrics** - Complete metric system including returns, risk, and turnover
- ✅ **Visualization Charts** - Equity curves, drawdowns, factor performance charts, etc.

![1773500440529](image/README_ZH/1773500440529.png)

### 6. AI Capabilities
- ✅ **AI Factor Generation** - Turn research ideas written in plain language into candidate factors for further validation
- ✅ **AI-assisted Formula Refinement** - Help improve factor expressions into clearer, library-ready definitions
- ✅ **AI Interpretation of Factor Analysis** - Produce structured research commentary based on factor definitions, analysis results, and chart context
- ✅ **AI Support for Use-case and Risk Review** - Help researchers quickly understand market intuition, limitations, and potential risks behind a factor
- ✅ **AI Report Export** - Organize AI interpretation output into shareable Markdown research notes

---

## Technical Architecture

### Tech Stack

**Backend:**
- FastAPI 0.135+ - High-performance web framework
- SQLAlchemy 2.0 - ORM database operations
- SQLite - Lightweight data storage
- Pandas 2.0+ / NumPy - Data processing
- TA-Lib - Technical analysis library
- VectorBT 0.25+ - Backtesting engine
- DEAP 1.3+ - Genetic algorithm framework
- XGBoost 2.0+ - Machine learning models
- SHAP 0.42+ - Model interpretation
- akshare 1.12+ - Chinese A-share data source

**Frontend:**
- React 19 - UI framework
- TypeScript - Type safety
- Ant Design 6 - UI component library
- ECharts 6 - Data visualization
- React Router 7 - Routing management
- Axios - HTTP client
- Vite - Build tool

---

## Project Structure

```
FactorHub/
├── backend/                    # Backend code
│   ├── api/                   # API layer
│   │   ├── main.py           # FastAPI main application
│   │   └── routers/          # API routers
│   │       ├── factors.py    # Factor management interface
│   │       ├── analysis.py   # Factor analysis interface
│   │       ├── mining.py     # Factor mining interface
│   │       ├── portfolio.py  # Portfolio analysis interface
│   │       ├── backtest.py   # Strategy backtesting interface
│   │       └── data.py       # Data management interface
│   ├── services/              # Business logic layer
│   ├── strategies/            # Strategy implementation
│   ├── repositories/          # Data access layer
│   ├── models/                # ORM models
│   └── core/                  # Core configuration
├── frontend/                   # Frontend code
│   └── react-antd/            # React + Ant Design version
├── config/                     # Configuration files
├── data/                       # Data directory
├── docs/                       # Documentation
├── tests/                      # Tests
├── scripts/                    # Utility scripts
└── README.md
```

---

## Quick Start

### Prerequisites

- **Python 3.11+**
- **Node.js 18+**
- **pnpm** (package manager)
- **TA-Lib** (technical analysis library)

### Installation

```bash
# Install pnpm
npm install -g pnpm

# Install Python dependencies (using uv)
uv sync

# Install frontend dependencies
cd frontend/react-antd
pnpm install
```

### One-click Startup

```bash
python start_all.py
```

This script will automatically:
1. Check environment prerequisites
2. Install dependencies if needed
3. Start backend service (http://localhost:8000)
4. Start frontend development server (http://localhost:5173)
5. Open browser automatically

### Manual Startup

#### Backend

```bash
uv run python start_api.py
# API available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

#### Frontend

```bash
cd frontend/react-antd
pnpm dev
# Frontend available at http://localhost:5173
```

### Docker Deployment

If you prefer to deploy the full application with Docker, use the built-in Docker configuration:

```bash
cd docker
docker compose build
docker compose up -d
```

After startup, access:

| Service | URL |
|---------|-----|
| Frontend | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |

Common commands:

```bash
# View logs
docker compose logs -f

# Stop services
docker compose down
```

Notes:
- The Docker image includes the application code and frontend build artifacts required for runtime
- The `data/` directory is mounted for persistent storage of factor data and runtime outputs
- Local AI model configuration, cache files, test logs, and database backups are not baked into the image

---

## License

### Dual License

**Personal Use:**

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

You are free to:
- ✅ Use this software for personal learning, research, and non-commercial purposes
- ✅ Modify and improve this software
- ✅ Distribute modified versions (must retain the same license)
- ✅ Reference this project in your own projects

**Commercial Use:**

⚠️ **Important Note:** Any commercial use (including but not limited to:
- Integrating this project into commercial products
- Using this project to provide paid services
- Using this project for production quantitative trading
- Using this project internally within companies for investment research)

**Requires separate commercial authorization.**

---

### Contact for Commercial Authorization

**Email:** yl_zhangqiang@foxmail.com

When contacting, please specify:
1. Your company/organization name
2. Your usage scenario and requirements
3. Expected scale of use
4. Contact information

We will respond within 3 business days.

---

## Contact

**Project Maintainer:** FactorHub Team

**Email:** yl_zhangqiang@foxmail.com

**Feedback Welcome:**
- Bug reports
- Feature suggestions
- Technical discussions
- Cooperation inquiries

---

**Last Updated:** 2026-03-14

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `utils/config.py`
```python

```

#### File: `utils/validators.py`
```python

```

#### File: `utils/__init__.py`
```python

```

#### File: `backend/__init__.py`
```python

```

#### File: `backend/core/__init__.py`
```python

```


==================================================


## [3/3] Repository: skfolio (`PHASE4-QUANT-094`)
- **Full Name**: `PHASE4-QUANT-094_skfolio__skfolio`
- **Description**: Python library for portfolio optimization built on top of scikit-learn
- **GitHub Stars**: 2405
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
.. -*- mode: rst -*-

.. The regions delimited by the `skfolio-shared-*-start` and `skfolio-shared-*-end`
   comments are included verbatim in `docs/index.rst`. Do not rename or remove them.
   Content placed outside those regions stays in the README only.

|Licence| |Codecov| |PythonVersion| |PyPi| |CI/CD| |Downloads| |Ruff| |Contribution| |Website| |JupyterLite| |Discord| |DOI|

.. |Licence| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://github.com/skfolio/skfolio/blob/main/LICENSE

.. |Codecov| image:: https://codecov.io/gh/skfolio/skfolio/graph/badge.svg?token=KJ0SE4LHPV
   :target: https://codecov.io/gh/skfolio/skfolio

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg
   :target: https://pypi.org/project/skfolio/

.. |PyPi| image:: https://img.shields.io/pypi/v/skfolio
   :target: https://pypi.org/project/skfolio

.. |CI/CD| image:: https://img.shields.io/github/actions/workflow/status/skfolio/skfolio/release.yml.svg?logo=github
   :target: https://github.com/skfolio/skfolio/actions

.. |Downloads| image:: https://static.pepy.tech/badge/skfolio
   :target: https://pepy.tech/project/skfolio

.. |Ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff

.. |Contribution| image:: https://img.shields.io/badge/Contributions-Welcome-blue
   :target: https://github.com/skfolio/skfolio/blob/main/CONTRIBUTING.md

.. |Website| image:: https://img.shields.io/website.svg?down_color=red&down_message=down&up_color=53cc0d&up_message=up&url=https://skfolio.org
   :target: https://skfolio.org

.. |JupyterLite| image:: https://jupyterlite.rtfd.io/en/latest/_static/badge.svg
   :target: https://skfolio.org/lite

.. |Discord| image:: https://img.shields.io/badge/Discord-Join%20Chat-5865F2?logo=discord&logoColor=white
   :target: https://discord.gg/Bu7EtNYugS

.. |DOI| image:: https://zenodo.org/badge/731792488.svg
   :target: https://doi.org/10.5281/zenodo.16148630


===============
|icon|  skfolio
===============
.. |icon| image:: https://raw.githubusercontent.com/skfolio/skfolio/main/docs/_static/logo_animate.svg
    :width: 100
    :alt: skfolio documentation


.. skfolio-shared-introduction-start

**skfolio** is a Python library for portfolio optimization, factor model construction,
and risk management built on top of scikit-learn. It offers a unified interface and
tools compatible with scikit-learn to build, fine-tune, cross-validate, and stress-test
portfolio models.

It is distributed under the open-source 3-Clause BSD license.

**skfolio** is backed by `Skfolio Labs <https://skfoliolabs.com>`_, which provides
enterprise support and SLAs for institutions.

.. skfolio-shared-introduction-end

.. image:: https://raw.githubusercontent.com/skfolio/skfolio/main/docs/_static/expo.jpg
    :target: https://skfolio.org/auto_examples/index.html
    :alt: examples

.. skfolio-shared-body-start

Important links
~~~~~~~~~~~~~~~

- `Examples <https://skfolio.org/auto_examples/index.html>`_
- `User Guide <https://skfolio.org/user_guide/index.html>`_
- `API Reference <https://skfolio.org/api.html>`_
- `GitHub Repo <https://github.com/skfolio/skfolio>`_
- `Enterprise Support <https://skfoliolabs.com>`_

Featured in
~~~~~~~~~~~

* `Portfolio Optimization: Theory and Application <https://portfoliooptimizationbook.com/>`_ by Daniel P. Palomar, includes Python code examples using skfolio.

Installation
~~~~~~~~~~~~

.. |PythonMinVersion| replace:: 3.10

`skfolio` requires Python |PythonMinVersion| or later and can be installed with:

.. code:: bash

    pip install -U skfolio

See the `installation guide <https://skfolio.org/user_guide/install.html>`_ for the full
dependency list, for conda-forge and for the mixed-integer solvers.

LLM-friendly documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

The documentation follows the `llms.txt convention <https://llmstxt.org/>`_ and
provides token-efficient Markdown alongside the HTML site:

- Start with `llms.txt <https://skfolio.org/llms.txt>`_ to find relevant pages.
- Read only the Markdown pages needed by appending `.md` to their HTML URLs, for example
  `factor_models.html.md <https://skfolio.org/user_guide/factor_models.html.md>`_.
- Use `llms-full.txt <https://skfolio.org/llms-full.txt>`_ only when the complete
  documentation is required in a single file.

Contribution
~~~~~~~~~~~~

We welcome contributions of all kinds. Whether it's reporting a bug, suggesting an
improvement, or submitting code, your input helps make `skfolio` better. See the
`contributing guide <https://github.com/skfolio/skfolio/blob/main/CONTRIBUTING.md>`_
to get started.

Key Concepts
~~~~~~~~~~~~
Since the development of modern portfolio theory by Markowitz (1952), mean-variance
optimization (MVO) has received considerable attention.

Unfortunately, it faces a number of shortcomings, including high sensitivity to the
input parameters (expected returns and covariance), weight concentration, high turnover,
and poor out-of-sample performance.

It is well-known that naive allocation (1/N, inverse-vol, etc.) tends to outperform
MVO out-of-sample (DeMiguel, 2007).

Numerous approaches have been developed to alleviate these shortcomings (shrinkage,
additional constraints, regularization, uncertainty set, higher moments, Bayesian
approaches, coherent risk measures, left-tail risk optimization, distributionally robust
optimization, factor model, risk-parity, hierarchical clustering, ensemble methods,
pre-selection, etc.).

Given the large number of methods, and the fact that they can be combined, there is a
need for a unified framework with a machine-learning approach to perform model
selection, validation, and parameter tuning while mitigating the risk of data leakage
and overfitting.

This framework is built on scikit-learn's API.

Available models
~~~~~~~~~~~~~~~~

* Portfolio Optimization:
    * Naive:
        * Equal-Weighted
        * Inverse-Volatility
        * Random (Dirichlet)
    * Convex:
        * Mean-Risk
        * Risk Budgeting
        * Maximum Diversification
        * Distributionally Robust CVaR
        * Benchmark Tracker
    * Clustering:
        * Hierarchical Risk Parity
        * Hierarchical Equal Risk Contribution
        * Schur Complementary Allocation
        * Nested Clusters Optimization
    * Ensemble Methods:
        * Stacking Optimization

* Prior Estimator:
    * Empirical
    * Characteristics-Based Cross-Sectional Factor Model:
        * 46 descriptors across 17 families (e.g. value, size, momentum, profitability)
        * Factor Exposures
        * Cross-Sectional Regression
        * Alpha Estimators
        * Forecast Evaluation
        * Ex-post and Ex-ante Attribution
    * Time-Series Factor Model
    * Black & Litterman
    * Synthetic Data (Stress Test, Factor Stress Test)
    * Entropy Pooling
    * Opinion Pooling

* Expected Returns Estimator:
    * Empirical
    * Exponentially Weighted
    * Equilibrium
    * Shrinkage

* Covariance Estimator:
    * Empirical
    * Gerber
    * Denoising
    * Detoning
    * Exponentially Weighted
    * Regime-Adjusted Exponentially Weighted
    * Ledoit-Wolf
    * Oracle Approximating Shrinkage
    * Shrunk Covariance
    * Graphical Lasso CV
    * Implied Covariance

* Variance Estimator:
    * Empirical
    * Exponentially Weighted
    * Regime-Adjusted Exponentially Weighted

* Distance Estimator:
    * Pearson Distance
    * Kendall Distance
    * Spearman Distance
    * Covariance Distance (based on any of the above covariance estimators)
    * Distance Correlation
    * Variation of Information

* Distribution Estimator:
    * Univariate:
        * Gaussian
        * Student's t
        * Johnson Su
        * Normal Inverse Gaussian
    * Bivariate Copula
        * Gaussian Copula
        * Student's t Copula
        * Clayton Copula
        * Gumbel Copula
        * Joe Copula
        * Independent Copula
    * Multivariate
        * Vine Copula (Regular, Centered, Clustered, Conditional Sampling)

* Uncertainty Set Estimator:
    * On Expected Returns:
        * Empirical
        * Circular Bootstrap
    * On Covariance:
        * Empirical
        * Circular Bootstrap

* Pre-Selection Transformers:
    * Non-Dominated Selection
    * Select K Extremes (Best or Worst)
    * Drop Highly Correlated Assets
    * Select Non-Expiring Assets
    * Select Complete Assets (handle late inception, delisting, etc.)
    * Drop Zero Variance

* Cross-Sectional Transformers:
    * Standard Scaler (z-score)
    * Percentile Rank Scaler
    * Gaussian Rank Scaler (rank gaussianization)
    * Winsorizer (percentile clipping)
    * Tanh Shrinker (smooth outlier shrinkage)

* Cross-Validation and Model Selection:
    * Compatible with all `sklearn` methods (KFold, etc.)
    * Walk Forward
    * Combinatorial Purged Cross-Validation
    * Multiple Randomized Cross-Validation
    * Covariance Forecast Evaluation
    * Online Predict and Online Score

* Hyper-Parameter Tuning:
    * Compatible with all `sklearn` methods (GridSearchCV, RandomizedSearchCV)
    * Online Grid Search and Online Randomized Search

* Risk Measures:
    * Variance
    * Semi-Variance
    * Mean Absolute Deviation
    * First Lower Partial Moment
    * CVaR (Conditional Value at Risk)
    * EVaR (Entropic Value at Risk)
    * Worst Realization
    * CDaR (Conditional Drawdown at Risk)
    * Maximum Drawdown
    * Average Drawdown
    * EDaR (Entropic Drawdown at Risk)
    * Ulcer Index
    * Gini Mean Difference
    * Value at Risk
    * Drawdown at Risk
    * Entropic Risk Measure
    * Fourth Central Moment
    * Fourth Lower Partial Moment
    * Skew
    * Kurtosis

* Optimization Features:
    * Minimize Risk
    * Maximize Returns
    * Maximize Utility
    * Maximize Ratio
    * Transaction Costs
    * Management Fees
    * L1 and L2 Regularization
    * Weight Constraints
    * Group Constraints
    * Budget Constraints
    * Tracking Error Constraints
    * Turnover Constraints
    * Cardinality and Group Cardinality Constraints
    * Threshold (Long and Short) Constraints

Quickstart
~~~~~~~~~~
The code snippets below are designed to introduce the functionality of `skfolio` so you
can start using it quickly. It follows the same API as scikit-learn.

Imports
-------
.. code-block:: python

    from sklearn import set_config
    from sklearn.model_selection import (
        GridSearchCV,
        KFold,
        RandomizedSearchCV,
        train_test_split,
    )
    from sklearn.pipeline import Pipeline
    from scipy.stats import loguniform

    from skfolio import RatioMeasure, RiskMeasure
    from skfolio.datasets import (
        load_factors_dataset,
        load_sp500_dataset,
        make_synthetic_characteristics,
    )
    from skfolio.descriptor import (
        BookToPrice,
        CashFlowToPrice,
        EWMarketBeta,
        EWMomentum,
        EWResidualVolatility,
        EWVolatility,
        LogMarketCap,
        SalesToPrice,
    )
    from skfolio.distribution import VineCopula
    from skfolio.factor_exposure import (
        DerivedFactor,
        FixedWeightedFactor,
        GlobalFactor,
        OneHotCategoricalFactors,
    )
    from skfolio.model_selection import (
        CombinatorialPurgedCV,
        WalkForward,
        cross_val_predict,
    )
    from skfolio.moments import (
        DenoiseCovariance,
        DetoneCovariance,
        EWMu,
        GerberCovariance,
        ShrunkMu,
    )
    from skfolio.optimization import (
        MeanRisk,
        HierarchicalRiskParity,
        NestedClustersOptimization,
        ObjectiveFunction,
        RiskBudgeting,
    )
    from skfolio.pre_selection import SelectKExtremes
    from skfolio.preprocessing import prices_to_returns
    from skfolio.prior import (
        BlackLitterman,
        CharacteristicsFactorModel,
        EmpiricalPrior,
        EntropyPooling,
        TimeSeriesFactorModel,
        OpinionPooling,
        SyntheticData,
    )
    from skfolio.uncertainty_set import BootstrapMuUncertaintySet

Load Dataset
------------
.. code-block:: python

    prices = load_sp500_dataset()

Train/Test split
----------------
.. code-block:: python

    X = prices_to_returns(prices)
    X_train, X_test = train_test_split(X, test_size=0.33, shuffle=False)


Minimum Variance
----------------
.. code-block:: python

    model = MeanRisk()

Fit on Training Set
-------------------
.. code-block:: python

    model.fit(X_train)

    print(model.weights_)

Predict on Test Set
-------------------
.. code-block:: python

    portfolio = model.predict(X_test)

    print(portfolio.annualized_sharpe_ratio)
    print(portfolio.summary())



Maximum Sortino Ratio
---------------------
.. code-block:: python

    model = MeanRisk(
        objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
        risk_measure=RiskMeasure.SEMI_VARIANCE,
    )


Denoised Covariance & Shrunk Expected Returns
---------------------------------------------
.. code-block:: python

    model = MeanRisk(
        objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
        prior_estimator=EmpiricalPrior(
            mu_estimator=ShrunkMu(), covariance_estimator=DenoiseCovariance()
        ),
    )

Uncertainty Set on Expected Returns
-----------------------------------
.. code-block:: python

    model = MeanRisk(
        objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
        mu_uncertainty_set_estimator=BootstrapMuUncertaintySet(),
    )


Weight Constraints & Transaction Costs
--------------------------------------
.. code-block:: python

    model = MeanRisk(
        min_weights={"AAPL": 0.10, "JPM": 0.05},
        max_weights=0.8,
        transaction_costs={"AAPL": 0.0001, "RRC": 0.0002},
        groups=[
            ["Equity"] * 3 + ["Fund"] * 5 + ["Bond"] * 12,
            ["US"] * 2 + ["Europe"] * 8 + ["Japan"] * 10,
        ],
        linear_constraints=[
            "Equity <= 0.5 * Bond",
            "US >= 0.1",
            "Europe >= 0.5 * Fund",
            "Japan <= 1",
        ],
    )
    model.fit(X_train)


Risk Parity on CVaR
-------------------
.. code-block:: python

    model = RiskBudgeting(risk_measure=RiskMeasure.CVAR)

Risk Parity & Gerber Covariance
-------------------------------
.. code-block:: python

    model = RiskBudgeting(
        prior_estimator=EmpiricalPrior(covariance_estimator=GerberCovariance())
    )

Nested Cluster Optimization with Cross-Validation and Parallelization
---------------------------------------------------------------------
.. code-block:: python

    model = NestedClustersOptimization(
        inner_estimator=MeanRisk(risk_measure=RiskMeasure.CVAR),
        outer_estimator=RiskBudgeting(risk_measure=RiskMeasure.VARIANCE),
        cv=KFold(),
        n_jobs=-1,
    )

Randomized Search of the L2 Norm
--------------------------------
.. code-block:: python

    randomized_search = RandomizedSearchCV(
        estimator=MeanRisk(),
        cv=WalkForward(train_size=252, test_size=60),
        param_distributions={
            "l2_coef": loguniform(1e-3, 1e-1),
        },
    )
    randomized_search.fit(X_train)

    best_model = randomized_search.best_estimator_

    print(best_model.weights_)


Grid Search on Embedded Parameters
----------------------------------
.. code-block:: python

    model = MeanRisk(
        objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
        risk_measure=RiskMeasure.VARIANCE,
        prior_estimator=EmpiricalPrior(mu_estimator=EWMu(half_life=40)),
    )

    print(model.get_params(deep=True))

    gs = GridSearchCV(
        estimator=model,
        cv=KFold(n_splits=5, shuffle=False),
        n_jobs=-1,
        param_grid={
            "risk_measure": [
                RiskMeasure.VARIANCE,
                RiskMeasure.CVAR,
                RiskMeasure.CDAR,
            ],
            "prior_estimator__mu_estimator__half_life": [10, 20, 30, 40],
        },
    )
    gs.fit(X)

    best_model = gs.best_estimator_

    print(best_model.weights_)


Black & Litterman Model
-----------------------
.. code-block:: python

    views = ["AAPL - BBY == 0.03 ", "CVX - KO == 0.04", "MSFT == 0.06 "]
    model = MeanRisk(
        objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
        prior_estimator=BlackLitterman(views=views),
    )

Characteristics-Based Factor Model
----------------------------------
.. code-block:: python

    month = 21
    quarter = 3 * month
    half_year = 6 * month
    year = 12 * month

    characteristics = make_synthetic_characteristics(
        n_assets=500,
        n_observations=2000,
        random_state=0,
    )

    # Global factor
    market_factor = GlobalFactor(family="market")

    # Industry factors
    industry_factors = OneHotCategoricalFactors(
        category="industry",
        family="industry",
    )

    # Style factors
    beta_factor = FixedWeightedFactor(
        descriptors=[
            ("market_beta", EWMarketBeta(half_life=year)),
        ],
        transform_by_group="industry",
    )

    momentum_factor = FixedWeightedFactor(
        descriptors=[
            ("momentum", EWMomentum(half_life=half_year, skip=month)),
        ],
        transform_by_group="industry",
    )

    size_factor = FixedWeightedFactor(
        descriptors=[("log_market_cap", LogMarketCap())],
        transform_by_group="industry",
    )

    non_linear_size_factor = DerivedFactor(
        source="size",
        func=lambda x: x**3,
        transform_by_group="industry",
    )

    value_factor = FixedWeightedFactor(
        descriptors=[
            ("book_to_price", BookToPrice()),
            ("sales_to_price", SalesToPrice()),
            ("cash_flow_to_price", CashFlowToPrice()),
        ],
        weights=[0.8, 0.1, 0.1],
        transform_by_group="industry",
    )

    volatility_factor = FixedWeightedFactor(
        descriptors=[
            ("vol", EWVolatility(half_life=quarter)),
            (
                "residual_vol",
                EWResidualVolatility(
                    half_life=quarter,
                    beta_half_life=quarter,
                ),
            ),
        ],
        transform_by_group="industry",
    )

    # Characteristics factor model
    model = CharacteristicsFactorModel(
        factors=[
            ("market", market_factor),
            ("industry", industry_factors),
            ("beta", beta_factor),
            ("momentum", momentum_factor),
            ("size", size_factor),
            ("non_linear_size", non_linear_size_factor),
            ("value", value_factor),
            ("volatility", volatility_factor),
        ],
        neutralize_against={
            "volatility": ["beta"],
            "non_linear_size": ["size"],
        },
        constrained_families=[("industry", None)],
        exposure_lag=1,
        inv_idio_variance_weight_shrinkage=0.5,
        n_jobs=-1,
    )

    model.fit(characteristics=characteristics)

    factor_model = model.factor_model_
    print(factor_model.summary())

For complete workflows, see the `Factor Models user guide
<https://skfolio.org/user_guide/factor_models.html>`_ and the `Factor Models tutorials
<https://skfolio.org/auto_examples/factor_models/index.html>`_.

Time-Series Factor Model
------------------------
.. code-block:: python

    factor_prices = load_factors_dataset()

    X, factors = prices_to_returns(prices, factor_prices)
    X_train, X_test, factors_train, factors_test = train_test_split(
        X, factors, test_size=0.33, shuffle=False
    )

    model = MeanRisk(prior_estimator=TimeSeriesFactorModel())
    model.fit(X_train, factors=factors_train)

    print(model.weights_)

    portfolio = model.predict(X_test)

    print(portfolio.calmar_ratio)
    print(portfolio.summary())

Time-Series Factor Model & Covariance Detoning
----------------------------------------------
.. code-block:: python

    model = MeanRisk(
        prior_estimator=TimeSeriesFactorModel(
            factor_prior_estimator=EmpiricalPrior(covariance_estimator=DetoneCovariance())
        )
    )

Black & Litterman Time-Series Factor Model
------------------------------------------
.. code-block:: python

    factor_views = ["MTUM - QUAL == 0.03 ", "VLUE == 0.06"]
    model = MeanRisk(
        objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
        prior_estimator=TimeSeriesFactorModel(
            factor_prior_estimator=BlackLitterman(views=factor_views),
        ),
    )

Pre-Selection Pipeline
----------------------
.. code-block:: python

    set_config(transform_output="pandas")
    model = Pipeline(
        [
            ("pre_selection", SelectKExtremes(k=10, highest=True)),
            ("optimization", MeanRisk()),
        ]
    )
    model.fit(X_train)

    portfolio = model.predict(X_test)




K-fold Cross-Validation
-----------------------
.. code-block:: python

    model = MeanRisk()
    mpp = cross_val_predict(model, X_test, cv=KFold(n_splits=5))
    # mpp is the predicted MultiPeriodPortfolio object composed of 5 Portfolios (1 per testing fold)

    mpp.plot_cumulative_returns()
    print(mpp.summary())


Combinatorial Purged Cross-Validation
-------------------------------------
.. code-block:: python

    model = MeanRisk()

    cv = CombinatorialPurgedCV(n_folds=10, n_test_folds=2)

    print(cv.summary(X_train))

    population = cross_val_predict(model, X_train, cv=cv)

    population.plot_distribution(
        measure_list=[RatioMeasure.SHARPE_RATIO, RatioMeasure.SORTINO_RATIO]
    )
    population.plot_cumulative_returns()
    print(population.summary())


Minimum CVaR Optimization on Synthetic Returns
----------------------------------------------
.. code-block:: python

    vine = VineCopula(log_transform=True, n_jobs=-1)
    prior = SyntheticData(distribution_estimator=vine, n_samples=2000)
    model = MeanRisk(risk_measure=RiskMeasure.CVAR, prior_estimator=prior)
    model.fit(X)
    print(model.weights_)


Stress Test
-----------
.. code-block:: python

    vine = VineCopula(log_transform=True, central_assets=["BAC"], n_jobs=-1)
    vine.fit(X)
    X_stressed = vine.sample(n_samples=10_000, conditioning = {"BAC": -0.2})
    ptf_stressed = model.predict(X_stressed)


Minimum CVaR Optimization on Synthetic Factors
----------------------------------------------
.. code-block:: python

    vine = VineCopula(central_assets=["QUAL"], log_transform=True, n_jobs=-1)
    factor_prior = SyntheticData(
        distribution_estimator=vine,
        n_samples=10_000,
        sample_args=dict(conditioning={"QUAL": -0.2}),
    )
    factor_model = TimeSeriesFactorModel(factor_prior_estimator=factor_prior)
    model = MeanRisk(risk_measure=RiskMeasure.CVAR, prior_estimator=factor_model)
    model.fit(X, factors=factors)
    print(model.weights_)


Factor Stress Test
------------------
.. code-block:: python

    factor_model.set_params(factor_prior_estimator__sample_args=dict(
        conditioning={"QUAL": -0.5}
    ))
    factor_model.fit(X, factors=factors)
    stressed_dist = factor_model.return_distribution_
    stressed_ptf = model.predict(stressed_dist)

Entropy Pooling
---------------
.. code-block:: python

    entropy_pooling = EntropyPooling(
        mean_views=[
            "JPM == -0.002",
            "PG >= LLY",
            "BAC >= prior(BAC) * 1.2",
        ],
        cvar_views=[
            "GE == 0.08",
        ],
    )
    entropy_pooling.fit(X)
    print(entropy_pooling.relative_entropy_)
    print(entropy_pooling.effective_number_of_scenarios_)
    print(entropy_pooling.return_distribution_.sample_weight)

CVaR Hierarchical Risk Parity optimization on Entropy Pooling
-------------------------------------------------------------
.. code-block:: python

    entropy_pooling = EntropyPooling(cvar_views=["GE == 0.08"])
    model = HierarchicalRiskParity(
        risk_measure=RiskMeasure.CVAR,
        prior_estimator=entropy_pooling
    )
    model.fit(X)
    print(model.weights_)

Stress Test with Entropy Pooling on Factor Synthetic Data
---------------------------------------------------------
.. code-block:: python

    # Regular Vine Copula and sampling of 100,000 synthetic factor returns
    factor_synth = SyntheticData(
        n_samples=100_000,
        distribution_estimator=VineCopula(log_transform=True, n_jobs=-1, random_state=0)
    )

    # Entropy Pooling by imposing a CVaR-95% of 10% on the Quality factor
    factor_entropy_pooling = EntropyPooling(
        prior_estimator=factor_synth,
        cvar_views=["QUAL == 0.10"],
    )

    factor_model = TimeSeriesFactorModel(factor_prior_estimator=factor_entropy_pooling)
    factor_model.fit(X, factors=factors)

    # We retrieve the stressed distribution:
    stressed_dist = factor_model.return_distribution_

    # We stress-test our portfolio:
    stressed_ptf = model.predict(stressed_dist)

Opinion Pooling
---
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/test_model_selection/__init__.py`
```python

```

#### File: `tests/test_model_selection/test_online/__init__.py`
```python

```

#### File: `tests/test_preprocessing/__init__.py`
```python

```

#### File: `tests/test_preprocessing/test_transformer/__init__.py`
```python

```

#### File: `tests/test_preprocessing/test_transformer/test_cross_sectional/__init__.py`
```python

```


==================================================
