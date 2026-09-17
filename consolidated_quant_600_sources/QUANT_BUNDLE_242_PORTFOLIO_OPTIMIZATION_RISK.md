# ⚡ [QUANT-SOURCE-242] Consolidated Quant & Algo Trading Repositories
**Category**: `PORTFOLIO_OPTIMIZATION_RISK` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_242_PORTFOLIO_OPTIMIZATION_RISK.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: cardiel (`PHASE4-QUANT-179`)
- **Full Name**: `PHASE4-QUANT-179_thk3421-models__cardiel`
- **Description**: A tool for portfolio managers: use the Black-Litterman model to view optimal portfolio allocations using several of the most popular optimization methods.
- **GitHub Stars**: 83
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Cardiel - A portfolio allocation tool based on Black-Litterman
Thomas Kirschenmann  
thk3421@gmail.com

## Description
This script is a tool for portfolio managers to input their market forecasts using the Black-Litterman (BL) method, and then use the resulting return vector and covariance matrix estimates as input for optimal portfolio allocations under several different portfolio optimization methods.  The [Black-Litterman model](https://en.wikipedia.org/wiki/Black%E2%80%93Litterman_model) is a mathematically consistent way to combine a portfolio manager's views on future asset return distributions as a Bayesian prior, which combined with historical market data, produces a posterior distribution for asset returns and covariances.  This is particularly useful, because a portfolio manager may have a view or forecast on individual securities, and a model like BL is required to propogate that view to other securities through an updated covariance matrix and expected return vector. If you have a view on one security, that implies you have a view on other securities because they are all correlated to varying degrees!

This tool will query market data for any security supported by Yahoo! Finance and can also be used with proprietary data in a CSV file.  
The BL return vector and covariance matrix serve as inputs to any standard portfolio optimization methodology, such as Markowitz mean-variance optimization under a variety of utility functions.  This tool calculates the optimal portfolio allocations using several methodologies and presents them simultaneously for side-by-side comparison, which helps guide a portfolio manager's decision to adjust the portfolio allocation.

A large portion of this tool relies on a terrific library put together by Robert Martin called [PyPortfolioOpt](https://pyportfolioopt.readthedocs.io/en/latest/index.html).  Tip o' the hat to Robert!

## Steps for Using This Tool to Produce Portfolio Allocation Weights 
## Step 1: Pip install the required python libraries:
<pre>
pip install argparse matplotlib numpy pandas statsmodels yfinance cvxopt joblib pypfopt
</pre>

## Step 2: Adjust the included config.json file to your situation.  
The example file in the repo contains the necessary fields:  
<ul>
        <li> max_lookback_years    -- the maximum number of years to query Yahoo! Finance for historical market data </li>
        <li> annual_risk_free_rate -- the annual risk free rate </li>
        <li> max_position_size     -- the maximum allowed position size in percentage terms </li>
        <li> min_position_size     -- the minimum allowed position size in percentage terms </li>
        <li> price_data            -- set this string to "yahoo" to automatically query Yahoo! Finance or provide a path to a CSV file to use proprietary data </li>
        <li> views                 -- See the note below
</ul>
The "views" field is where the user can entry their views on individual securities in the form of 3 numbers per security.  The first number is the user-provided lower bound annual return for a 1 standard deviation downward move.  The second number is the user-provided expected annual return, and the third number is the upper bound for a 1 standard deviation upward move.  For example, if a user believes BABA stock is going to have a one-year return of 10% plus or minus 15% (i.e. with a lower range forecast of -5% and upper bound forecast of 25% they can enter: "BABA":[-0.05, 0.10, 0.25]. Similarly, the user should repeat this process and enter their views for each asset of interest into their config.json file. A hypothetical example would be: 
<pre>
"views":{
            "BABA":[-0.05, 0.10, 0.25],
            "NVDA":[-0.10, 0.10, 0.30],
            "DIS":[-0.10, 0.07, 0.15],
            "BA":[-0.05, 0.07, 0.15],
            "XOM":[-0.05, 0.07, 0.15],
            "FB":[-0.05, 0.07, 0.15],
            "GOOG":[-0.05, 0.07, 0.15],
            "BAC":[0.0, 0.10, 0.25] 
        }
</pre>
An argument can be made that if a portfolio manager does not hold any view whatsoever on a security, then it does not belong in their portfolio!

## Step 3: Run the script and review the Black-Litterman results
From a terminal, simply run: 
<pre>
        python main.py --config config.json
</pre>
and the program will load the daily adjusted close prices and compute the Black-Litterman return vector and covariance matrices.  These will be automatically plotted and displayed for validation purposes.  An example summary comparing the views, historical returns, and posterior returns looks like:
![](/example_images/BL_returns.png)
Similarly, the Black-Litterman model covariance and correlations matrices are provided:
![](/example_images/BL_Cov.png)
![](/example_images/BL_corr.png)

### Cached Results ###
One may wish to repeat the above process several times if they are unhappy with the resulting BL returns and covariances.  The Yahoo! query results are automatically cached in local directory, /cachedir, after being received on a given day.  If the program is re-run on the same day with the same set of assets, then cached result will be used.  This will speed up the program by skipping the Yahoo! query and allow for quicker iteration and data exploration.

## Step 4:  Choose a level of risk-aversion
Several optimization routines are automatically run (see details in the portfolio optimization methodology section of this document).  **Most of them require no further input from the user**, however the most commonly used optimization is a Markowitz mean-variance optimization  that requires the user to choose a level of risk-aversion.   This is handled by viewing the [efficient frontier](https://en.wikipedia.org/wiki/Efficient_frontier), which is the expected return for an optimal portfolio for a given amount of risk (volatility). The risk aversion parameter is varied, which creates the full curve.  **The user is required to choose a point on the efficient frontier and enter the corresponding number into the terminal.**  
For example:
![](/example_images/EF_max_quad_util.png)
The user seeing the efficient frontier in the chart above may think "I'm okay with 24% volatility for a 10.5% expected return, so I choose point number 2." Now enter that number into the terminal:

![](/example_images/choose_pt.png)

## Step 5: Compare the portfolio allocations
The tool reports the portfolio allocation weight for each security, using several different optimization schemes.  The portfolio optimizations are all foreced to obey the constraints specified in the config file.  The portfolio optimizations are:
<ul>
        <li> Kelly Criterion: [Kelly objective function](https://en.wikipedia.org/wiki/Kelly_criterion).  Full details of my implementation are discussed here: [thk3421-models.github.io/KellyPortfolio/](https://thk3421-models.github.io/KellyPortfolio/) </li>
        <li> Markowitz Mean-Variance with Maximum Quadratic Utility:  [Markowitz Model](https://en.wikipedia.org/wiki/Markowitz_model#Choosing_the_best_portfolio) </li>
        <li> Maximum Sharpe Ratio: [also known as the Tangency portfolio](http://comisef.wikidot.com/tutorial:tangencyportfolio) </li>
        <li> Minimum Volatility: Portfolio that minimizes the total portfolio volatility </li>
        <li> Critical Line Algorithm - Maximum Sharpe Ratio: [Critical Line Method](https://en.wikipedia.org/wiki/Portfolio_optimization#Specific_approaches) </li>
        <li> Critical Line Algorithm - Minimum Volatility: [Critical Line Method](https://en.wikipedia.org/wiki/Portfolio_optimization#Specific_approaches) </li>
</ul>
The various results should now be compared using the final chart produced.  This is the main purpose of the tool, to get a feel for the portfolio weights recommended by a variety of algorithms:

![](/example_images/Portfolio_Weights.png)

The goal is now achieved: comparison of optimal portfolio allocations using a variety of methods, all based on the user-provided views that are married to historical data in a Bayesian way through the Black-Litterman model.  The weights are automatically saved to a local CSV file as well.  The user can now look for patterns in the assets and determine if they prefer to increase or decrease a particular holding in order to either reduce expected volatility or to increase potential returns.  

Hope someone finds this useful or interesting! Please send me a note if you want me to add more output or a custom feature! 

[Best wishes, warmest regards!](/example_images/john_cardiel.png)

### Core Implementation Code & Architecture
#### File: `config.json`
```python
{
    "max_lookback_years": 5,
    "annual_risk_free_rate": 0.008,
    "max_position_size": 0.35,
    "min_position_size": 0.0,
    "price_data": "sample_data.csv",
    "views": {
            "BABA":[-0.10, 0.10, 0.20],
            "NVDA":[-0.10, 0.10, 0.30],
            "DIS":[-0.10, 0.07, 0.15],
            "BA":[-0.05, 0.07, 0.15],
            "XOM":[-0.05, 0.07, 0.15],
            "FB":[-0.05, 0.07, 0.15],
            "GOOG":[-0.05, 0.07, 0.15],
            "BAC":[0.0, 0.10, 0.25]
        }
}
```

#### File: `main.py`
```python
import argparse
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.stats.moment_helpers as mh
import sys
import json
import yfinance
from cvxopt.solvers import qp
from cvxopt import matrix
from joblib import Memory
from pandas_datareader import data as pd_data
from pypfopt import black_litterman, risk_models
from pypfopt import BlackLittermanModel, plotting
from pypfopt import EfficientFrontier, objective_functions, CLA
memory = Memory('./cachedir', verbose=0)

def load_config(path):
    "load required config file"
    with open(path) as config_file:
        data = json.load(config_file)
    return data

@memory.cache
def load_prices(symbols, max_lookback_years, data_source, curr_date, config):
    "begin loading prices"
    if data_source == 'yahoo':
        stock_symbols, crypto_symbols = [], []
        start_date = (datetime.datetime.today()
                      - datetime.timedelta(days=365*max_lookback_years)).date()
        end_date = datetime.datetime.today().date() - datetime.timedelta(days=1)
        symbols = sorted(symbols)
        if len(symbols) > 0:
            print('Downloading adjusted daily close data from Yahoo! Finance')
            try:
                price_data = yfinance.download(symbols, start=str(start_date), end=str(end_date),
                                               interval='1d', auto_adjust=True, threads=True)
            except:
                print('Error downloading data from Yahoo! Finance')
                sys.exit(-1)
            if symbols == ['SPY']:
                cols = [('Close')]
                price_data = price_data[cols]
                price_data.columns = ['SPY']
            else:
                cols = [('Close', x) for x in symbols]
                price_data = price_data[cols]
                price_data.columns = price_data.columns.get_level_values(1)
            price_data.to_csv('sample_data.csv', header=True)
    elif data_source is not None:
        try:
            #Expects a CSV with Date, Symbol header for the prices, i.e. Date, AAPL, GOOGL
            price_data = pd.read_csv(config['price_data'], parse_dates=['Date'])
            price_data.set_index(['Date'], inplace=True)
        except (OSError, KeyError):
            print('Error loading local price data from:', config['price_data'])
            sys.exit(-1)
    price_data = price_data.sort_index()
    return price_data

@memory.cache
def load_mkt_caps(symbols, curr_date):
    print('loading market cap data')
    mcaps = pd.DataFrame(columns=['MarketCap'])
    #mcaps = pd_data.get_quote_yahoo(symbols)['marketCap']
    #missing_mcap_symbols = mcaps[mcaps.isnull()].index
    #for symbol in missing_mcap_symbols:
    for symbol in symbols:
        print('querying market cap info for', symbol)
        data = yfinance.Ticker(symbol)
        if data.info['quoteType'] == 'ETF' or data.info['quoteType'] == 'MUTUALFUND': 
            mcap = data.info['totalAssets']
            print('adding market cap info for', symbol)
        else:
            mcap = data.info['marketCap']
        mcaps.loc[symbol] = mcap
        #else:
        #    print('Failed to find market cap for', symbol)
        #    sys.exit(-1)
    #mcaps=mcaps.to_dict()['MarketCap']
    return mcaps

@memory.cache
def load_market_prices(prices, curr_date):
    mkt_prices = yfinance.download("SPY", period="max")["Adj Close"]
    return mkt_prices
    
def calc_omega(config, symbols):
    variances = []
    for symbol in sorted(symbols):
        view = config['views'][symbol]
        lb, ub  = view[0], view[2]
        std_dev = (ub - lb)/2
        variances.append(std_dev ** 2)
    omega = np.diag(variances)
    return omega

def plot_black_litterman_results(ret_bl, covar_bl, market_prior, mu):
    rets_df = pd.DataFrame([market_prior, ret_bl, pd.Series(mu)],
                           index=["Prior", "Posterior", "Views"]).T
    rets_df.plot.bar(figsize=(12,8), title='Black-Litterman Expected Returns');
    plot_heatmap(covar_bl, 'Black-Litterman Covariance', '', '')
    corr_bl = mh.cov2corr(covar_bl)
    corr_bl = pd.DataFrame(corr_bl, index=covar_bl.index, columns=covar_bl.columns)
    plot_heatmap(corr_bl, 'Black-Litterman Correlation', '', '')

def load_mean_views(views, symbols):
    mu = {}
    for symbol in sorted(symbols):
        mu[symbol] = views[symbol][1]
    return mu

def load_data():
    config = load_config(OPTIONS.config_path)
    symbols = sorted(config['views'].keys())
    max_lookback_years = config['max_lookback_years']
    prices = load_prices(symbols, max_lookback_years, config['price_data'], datetime.date.today(), config)
    market_prices = load_market_prices(prices, datetime.date.today())
    mkt_caps = load_mkt_caps(symbols, datetime.date.today())
    mkt_caps = pd.Series(mkt_caps.to_dict()['MarketCap'])
    return prices, market_prices, mkt_caps, symbols, config

def calc_black_litterman(market_prices, mkt_caps, covar, config, symbols):
    delta = black_litterman.market_implied_risk_aversion(market_prices)
    market_prior = black_litterman.market_implied_prior_returns(mkt_caps, delta, covar)
    mu = load_mean_views(config['views'], symbols)
    omega = calc_omega(config, symbols)
    bl = BlackLittermanModel(covar, pi="market", market_caps=mkt_caps, risk_aversion=delta,
                             absolute_views=mu, omega=omega)
    rets_bl = bl.bl_returns()
    covar_bl = bl.bl_cov()
    plot_black_litterman_results(rets_bl, covar_bl, market_prior, mu);
    return rets_bl, covar_bl

def kelly_optimize(M_df, C_df, config):
    "objective function to maximize is: g(F) = r + F^T(M-R) - F^TCF/2"
    print('Begin Kelly Criterion optimization')
    r = config['annual_risk_free_rate']
    M = M_df.to_numpy()
    C = C_df.to_numpy()

    n = M.shape[0]
    A = matrix(1.0, (1, n))
    b = matrix(1.0)
    G = matrix(0.0, (n, n))
    G[::n+1] = -1.0
    h = matrix(0.0, (n, 1))
    try:
        max_pos_size = float(config['max_position_size'])
    except KeyError:
        max_pos_size = None
    try:
        min_pos_size = float(config['min_position_size'])
    except KeyError:
        min_pos_size = None
    if min_pos_size is not None:
        h = matrix(min_pos_size, (n, 1))

    if max_pos_size is not None:
       h_max = matrix(max_pos_size, (n,1))
       G_max = matrix(0.0, (n, n))
       G_max[::n+1] = 1.0
       G = matrix(np.vstack((G, G_max)))
       h = matrix(np.vstack((h, h_max)))

    S = matrix((1.0 / ((1 + r) ** 2)) * C)
    q = matrix((1.0 / (1 + r)) * (M - r))
    sol = qp(S, -q, G, h, A, b)
    kelly = np.array([sol['x'][i] for i in range(n)])
    kelly = pd.DataFrame(kelly, index=C_df.columns, columns=['Weights'])
    kelly = kelly.round(3) 
    kelly.columns=['Kelly']
    return kelly

def max_quad_utility_weights(rets_bl, covar_bl, config):
    print('Begin max quadratic utility optimization')
    returns, sigmas, weights, deltas = [],[],[],[]
    for delta in np.arange(1,10,1):
        ef = EfficientFrontier(rets_bl, covar_bl, weight_bounds= \
                (config['min_position_size'] ,config['max_position_size']))
        ef.max_quadratic_utility(delta)
        ret, sigma, __ = ef.portfolio_performance()
        weights_vec = ef.clean_weights()
        returns.append(ret)
        sigmas.append(sigma)
        deltas.append(delta)
        weights.append(weights_vec)
    fig, ax = plt.subplots()
    ax.plot(sigmas, returns)
    for i, delta in enumerate(deltas):
        ax.annotate(str(delta), (sigmas[i], returns[i]))
    plt.xlabel('Volatility (%) ')
    plt.ylabel('Returns (%)')
    plt.title('Efficient Frontier for Max Quadratic Utility Optimization')
    plt.show()
    opt_delta = float(input('Enter the desired point on the efficient frontier: ') )
    ef = EfficientFrontier(rets_bl, covar_bl, weight_bounds= \
            (config['min_position_size'] ,config['max_position_size']))
    ef.max_quadratic_utility(opt_delta)
    opt_weights = ef.clean_weights()
    opt_weights = pd.DataFrame.from_dict(opt_weights, orient='index')
    opt_weights.columns=['Max Quad Util']
    return opt_weights, ef  

def min_volatility_weights(rets_bl, covar_bl, config):
    ef = EfficientFrontier(rets_bl, covar_bl, weight_bounds= \
            (config['min_position_size'] ,config['max_position_size']))
    ef.min_volatility()
    weights = ef.clean_weights()
    weights = pd.DataFrame.from_dict(weights, orient='index')
    weights.columns=['Min Vol']
    return weights, ef

def max_sharpe_weights(rets_bl, covar_bl, config):
    ef = EfficientFrontier(rets_bl, covar_bl, weight_bounds= \
            (config['min_position_size'] ,config['max_position_size']))
    ef.max_sharpe()
    weights = ef.clean_weights()
    weights = pd.DataFrame.from_dict(weights, orient='index')
    weights.columns=['Max Sharpe']
    return weights, ef

def cla_max_sharpe_weights(rets_bl, covar_bl, config):
    cla = CLA(rets_bl, covar_bl, weight_bounds= \
            (config['min_position_size'] ,config['max_position_size']))
    cla.max_sharpe()
    weights = cla.clean_weights()
    weights = pd.DataFrame.from_dict(weights, orient='index')
    weights.columns=['CLA Max Sharpe']
    return weights, cla

def cla_min_vol_weights(rets_bl, covar_bl, config):
    cla = CLA(rets_bl, covar_bl, weight_bounds= \
            (config['min_position_size'] ,config['max_position_size']))
    cla.min_volatility()
    weights = cla.clean_weights()
    weights = pd.DataFrame.from_dict(weights, orient='index')
    weights.columns=['CLA Min Vol']
    return weights, cla

def plot_heatmap(df, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.25, left=0.25)
    heatmap = ax.pcolor(df, edgecolors='w', linewidths=1)
    cbar = plt.colorbar(heatmap)
    ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)
    ax.set_xticklabels(df.columns) #, rotation=45)
    ax.set_yticklabels(df.index)

    for y, idx in enumerate(df.index):
        for x, col in enumerate(df.columns):
            plt.text(x + 0.5, y + 0.5, '%.2f' % df.loc[idx, col], \
                     horizontalalignment='center', verticalalignment='center',)

    plt.gca().invert_yaxis()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def main():
    prices, market_prices, mkt_caps, symbols, config = load_data()

    #covar = risk_models.risk_matrix(prices, method='exp_cov', span=180)
    #covar = risk_models.risk_matrix(prices, method='semicovariance')
    #covar = risk_models.CovarianceShrinkage(prices).ledoit_wolf()
    covar = risk_models.risk_matrix(prices, method='oracle_approximating')
    rets_bl, covar_bl = calc_black_litterman(market_prices, mkt_caps, covar, config, symbols)

    kelly_w = kelly_optimize(rets_bl, covar_bl, config) 
    max_quad_util_w, max_quad_util_ef = max_quad_utility_weights(rets_bl, covar_bl, config)
    min_vol_w, min_vol_ef = min_volatility_weights(rets_bl, covar_bl, config)
    max_sharpe_w, max_sharpe_ef = max_sharpe_weights(rets_bl, covar_bl, config)
    cla_max_sharpe_w, cla_max_sharpe_cla = cla_max_sharpe_weights(rets_bl, covar_bl, config)
    cla_min_vol_w, cla_min_vol_cla = cla_min_vol_weights(rets_bl, covar_bl, config)

    #ax = plotting.plot_efficient_frontier(cla_max_sharpe_cla, showfig=False)
    #plt.title('Efficient Frontier via CLA Max Sharpe Optimization')
    #plt.show()
    #ax = plotting.plot_efficient_frontier(cla_min_vol_cla, showfig=False)
    #plt.title('Efficient Frontier via CLA Min Volatility Optimization')
    #plt.show()

    weights_df = pd.merge(kelly_w, max_quad_util_w, left_index=True, right_index=True)
    weights_df = pd.merge(weights_df, max_sharpe_w, left_index=True, right_index=True) 
    weights_df = pd.merge(weights_df, cla_max_sharpe_w, left_index=True, right_index=True) 
    weights_df = pd.merge(weights_df, min_vol_w, left_index=True, right_index=True) 
    weights_df = pd.merge(weights_df, cla_min_vol_w, left_index=True, right_index=True) 
    weights_df.to_csv('portfolio_weight_results.csv')
    
    plot_heatmap(weights_df, 'Portfolio Weighting (%)','Optimization Method', 'Security')


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-c', '--config_path', action="store")
    OPTIONS = PARSER.parse_args()
    main()
```


==================================================


## [2/3] Repository: generative-opt (`PHASE4-QUANT-180`)
- **Full Name**: `PHASE4-QUANT-180_kayuksel__generative-opt`
- **Description**: Democratizing Index Tracking for Small Investors in Europe: A Meta-Learning Method for Sparse Portfolio Optimization
- **GitHub Stars**: 82
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
[![DOI](https://zenodo.org/badge/585382109.svg)](https://zenodo.org/badge/latestdoi/585382109)

# Democratizing Index Tracking: A GNN-based Meta-Learning Method for Sparse Portfolio Optimization
Investing in stocks is a popular way for individuals to grow their wealth and diversify their investment portfolio, but many exchange-traded funds (ETFs) and mutual funds that offer actively managed index funds are not available to small investors in Europe due to UCITS regulations. An approach, called sparse index tracking, can allow investors to create their own sparse stock portfolio for tracking an index. However, selecting the optimal portfolio from thousands of stocks is a sophisticated and resource-intensive task.
![](backtest_vgt.png)
To address this issue, I have developed a novel population-based optimization method employing a Deep Generative Neural Network trained with policy gradient to sample high-quality candidates. I have compared it against the state-of-the-art evolutionary strategy (Fast CMA-ES) and have found that it is more efficient at finding optimal solutions. Both methods are implemented on GPU using the PyTorch framework and are available in this repository (together with [the dataset](https://drive.google.com/file/d/1RVhboDO3u_subUgG1G8rwdY7Ar6Dyrxf/view?usp=sharing)) for their reproducibility and further improvement.
![](gnn_arch.png)
Before running **main.py**, download **Dataset.pkl** from the below link and place it to this folder:  
https://drive.google.com/file/d/1RVhboDO3u_subUgG1G8rwdY7Ar6Dyrxf/view?usp=sharing  

The key for out-of-sample robustness in portfolio optimization is quality-diversity optimization, where one aims to obtain multiple diverse solutions of high quality, rather than one. Generative meta-learning is the only portfolio optimization method that performs QD optimization to obtain a robust ensemble portfolio consisting of several de-correlated sub-portfolios. In the below image, the red line is the index to be tracked, the blue line is the sparse portfolio ensembled from a thousand behaviorally-diverse sub-portfolios co-optimized (other lines).
![](test_img.png)
In Gen-Meta portfolio optimization, a Monte-Carlo optimization is performed over those portfolio candidates to reward each individual separately in randomly selected historical periods. To further optimize the portfolio robustness, the portfolio weights of the candidates are heavily corrupted first by adding noise and then dropping out the vast majority of their weights. The codes in this repository includes comments on those critical techniques performed to obtain a robust ensemble from behaviorally-diverse high-quality portfolios co-optimized with Gen-Meta.

### Core Implementation Code & Architecture
#### File: `gecco2023/torch_opt_index.py`
```python
import torch
import torch.nn as nn
import torch.optim as optim
torch.set_printoptions(precision=10)

weights = nn.Parameter(torch.zeros((args.batch, len(assets)), dtype=torch.float32).to(device))

# List of optimizers available in PyTorch
optimizers = [optim.SGD, optim.Adam, optim.AdamW, optim.Adamax, optim.ASGD, optim.NAdam, 
    optim.Adagrad, optim.Adadelta, optim.Rprop, optim.RMSprop, optim.RAdam, optim.LBFGS]

def closure():
    opt.zero_grad()
    loss = calculate_reward(weights, valid_data[:-test_size], index[:-test_size], True)
    loss.mean().backward()
    return loss.mean()

for optimizer in optimizers:
    # Initialize weights to zeros using PyTorch
    weights.data.zero_()
    
    # Create an instance of the current optimizer
    opt = optimizer([weights], lr = 1e-3)

    best_weights = None
    best_loss = float("inf")

    if optimizer == optim.LBFGS:
        opt = optimizer([weights], lr=1e-3, max_iter=args.iter)
        opt.step(closure)
    else:
        opt = optimizer([weights], lr=1e-3)
        for epoch in range(args.iter):
            # Forward pass
            loss = calculate_reward(weights, valid_data[:-test_size], index[:-test_size], True)
            
            # Store the best weights
            if loss.min().item() < best_loss:
                best_loss = loss.min().item()
                best_weights = weights.clone().detach()
            
            # Backward pass and optimization
            opt.zero_grad()
            loss.mean().backward()
            opt.step()

    with torch.no_grad():
        # Calculate the test loss using the best weights
        test_loss = calculate_reward(weights[loss.argmin()].unsqueeze(0),valid_data[-test_size:], index[-test_size:])[0]
        print('%s %f' % (optimizer.__name__, test_loss))
```

#### File: `qc_backtest.py`
```python
##########################################
#Kamer Ali Yuksel linkedin.com/in/kyuksel#
##########################################

import numpy as np

syms = ['MSFT', 'AAPL', 'TXN', 'ASML', 'ADBE', 'CRM', 'SBUX', 'MCHP', 'MA', 'ADI', 'SWKS', 'SNPS', 'KLAC']

class MultidimensionalModulatedRegulators(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        #self.SetEndDate(2017, 1, 1)
        self.SetCash(100000)
        self.SetExecution(VolumeWeightedAveragePriceExecutionModel())
 
        self.symbols = []
        for i in range(len(syms)):
            self.symbols.append(Symbol.Create(syms[i], SecurityType.Equity, Market.USA))
            self.Debug(syms[i])
            
        self.SetUniverseSelection(ManualUniverseSelectionModel(self.symbols) )
        self.UniverseSettings.Resolution = Resolution.Hour
        
        self.AddEquity('VGT', Resolution.Hour)
        self.SetBenchmark('VGT')
        
        self.SetBrokerageModel(AlphaStreamsBrokerageModel())

        self.constant_weights = np.array([0.28535828, 0.23993727, 0.12635303, 0.05360154, 0.04681825, 0.04518177, 0.04505873, 0.04194283, 0.03757035, 0.03131177, 0.02168459, 0.0151392 , 0.01004238])
        self.constant_weights = self.constant_weights / np.sum(np.abs(self.constant_weights))

    def OnData(self, data):
                
        rebalance = False
        
        if self.Portfolio.TotalHoldingsValue > 0:
            total = 0.0
            for i, sym in enumerate(self.symbols):
                curr = (self.Securities[sym].Holdings.HoldingsValue/self.Portfolio.TotalPortfolioValue)
                diff = self.constant_weights[i] - curr
                total += np.abs(diff)
                
            if total > 0.05: 
                rebalance = True
                
            if rebalance:
                for i, sym in enumerate(self.symbols):
                    curr = (self.Securities[sym].Holdings.HoldingsValue/self.Portfolio.TotalPortfolioValue)
                    if self.constant_weights[i] < curr:
                        self.SetHoldings(sym, self.constant_weights[i])
                for i, sym in enumerate(self.symbols):
                    curr = (self.Securities[sym].Holdings.HoldingsValue/self.Portfolio.TotalPortfolioValue)                       
                    if self.constant_weights[i] > curr:
                        self.SetHoldings(sym, self.constant_weights[i])
        else:
            for i, sym in enumerate(self.symbols):
                    self.SetHoldings(sym, self.constant_weights[i])
```

#### File: `gecco2023/cma_es_index.py`
```python
class FastCMA(object):
    def __init__(self, N, samples):
        self.samples = samples
        mu = samples // 2
        self.weights = torch.tensor([math.log(mu + 0.5)]).to(device)
        self.weights = self.weights - torch.linspace(
            start=1, end=mu, steps=mu).to(device).log()
        self.weights /= self.weights.sum()
        self.mueff = (self.weights.sum() ** 2 / (self.weights ** 2).sum()).item()
        # settings
        self.cc = (4 + self.mueff / N) / (N + 4 + 2 * self.mueff / N)
        self.c1 = 2 / ((N + 1.3) ** 2 + self.mueff)
        self.cmu = 2 * (self.mueff - 2 + 1 / self.mueff) 
        self.cmu /= ((N + 2) ** 2 + 2 * self.mueff / 2)
        # variables
        self.mean = torch.zeros(N).to(device)
        self.b = torch.eye(N).to(device)
        self.d = self.b.clone()
        bd = self.b * self.d
        self.c = bd * bd.T
        self.pc = self.mean.clone()

    def step(self, step_size = 0.5):
        z = torch.randn(self.mean.size(0), self.samples).to(device)
        ss = self.mean.view(-1, 1) + step_size * self.b.matmul(self.d.matmul(z))
        f = calculate_reward(sparsemax(ss, dim=1).T, 
            valid_data[:-test_size], index[:-test_size])
        results = [{'parameters': ss.T[i], 'z': z.T[i], 
        'fitness': f.item()} for i, f in enumerate(f)]
        ranked_results = sorted(results, key=lambda x: x['fitness'])
        selected_results = ranked_results[0:self.samples//2]
        z = torch.stack([g['z'] for g in selected_results])
        g = torch.stack([g['parameters'] for g in selected_results])

        self.mean = (g * self.weights.unsqueeze(1)).sum(0)
        zmean = (z * self.weights.unsqueeze(1)).sum(0)
        self.pc *= (1 - self.cc)
        pc_cov = self.pc.unsqueeze(1) * self.pc.unsqueeze(1).T
        pc_cov = pc_cov + self.cc * (2 - self.cc) * self.c

        bdz = self.b.matmul(self.d).matmul(z.T)
        cmu_cov = bdz.matmul(self.weights.diag_embed())
        cmu_cov = cmu_cov.matmul(bdz.T)

        self.c *= (1 - self.c1 - self.cmu)
        self.c += (self.c1 * pc_cov) + (self.cmu * cmu_cov)
        self.d, self.b = torch.linalg.eigh(self.c, UPLO='U')
        self.d = self.d.sqrt().diag_embed()
        return ranked_results

best_reward = None
with torch.no_grad():
    cma_es = FastCMA(N = len(assets), samples=args.batch)
    for epoch in range(args.iter):
        try:
            res = cma_es.step()
        except Exception as e: 
            print(e)
            break
        weights = sparsemax(res[0]['parameters'], dim=0)
        r = calculate_reward(weights.unsqueeze(0), 
            valid_data[-test_size:], index[-test_size:])
        if best_reward is None: best_reward = r
        if r < best_reward:
            best_reward = r
            print('epoch: %i v_loss: %f' % (epoch, best_reward))
            bw = weights.detach().cpu().numpy()
            bw = pd.DataFrame(bw).set_index([assets])
            bw = bw.loc[~(bw==0).all(axis=1)]
            bw = bw.reindex(bw[0].abs().sort_values(ascending=False).index)
            bw.to_csv('best_weights.csv', header=False)
```

#### File: `cma_es_index.py`
```python
##########################################
#Kamer Ali Yuksel linkedin.com/in/kyuksel#
##########################################

class FastCMA(object):
    def __init__(self, N, samples):
        self.samples = samples
        mu = samples // 2
        self.weights = torch.tensor([math.log(mu + 0.5)]).to(device)
        self.weights = self.weights - torch.linspace(
            start=1, end=mu, steps=mu).to(device).log()
        self.weights /= self.weights.sum()
        self.mueff = (self.weights.sum() ** 2 / (self.weights ** 2).sum()).item()
        # settings
        self.cc = (4 + self.mueff / N) / (N + 4 + 2 * self.mueff / N)
        self.c1 = 2 / ((N + 1.3) ** 2 + self.mueff)
        self.cmu = 2 * (self.mueff - 2 + 1 / self.mueff) 
        self.cmu /= ((N + 2) ** 2 + 2 * self.mueff / 2)
        # variables
        self.mean = torch.zeros(N).to(device)
        self.b = torch.eye(N).to(device)
        self.d = self.b.clone()
        bd = self.b * self.d
        self.c = bd * bd.T
        self.pc = self.mean.clone()

    def step(self, step_size = 0.5):
        z = torch.randn(self.mean.size(0), self.samples).to(device)
        ss = self.mean.view(-1, 1) + step_size * self.b.matmul(self.d.matmul(z))
        f = calculate_reward(sparsemax(ss, dim=1).T, 
            valid_data[:-test_size], index[:-test_size])
        results = [{'parameters': ss.T[i], 'z': z.T[i], 
        'fitness': f.item()} for i, f in enumerate(f)]
        ranked_results = sorted(results, key=lambda x: x['fitness'])
        selected_results = ranked_results[0:self.samples//2]
        z = torch.stack([g['z'] for g in selected_results])
        g = torch.stack([g['parameters'] for g in selected_results])

        self.mean = (g * self.weights.unsqueeze(1)).sum(0)
        zmean = (z * self.weights.unsqueeze(1)).sum(0)
        self.pc *= (1 - self.cc)
        pc_cov = self.pc.unsqueeze(1) * self.pc.unsqueeze(1).T
        pc_cov = pc_cov + self.cc * (2 - self.cc) * self.c

        bdz = self.b.matmul(self.d).matmul(z.T)
        cmu_cov = bdz.matmul(self.weights.diag_embed())
        cmu_cov = cmu_cov.matmul(bdz.T)

        self.c *= (1 - self.c1 - self.cmu)
        self.c += (self.c1 * pc_cov) + (self.cmu * cmu_cov)
        self.d, self.b = torch.linalg.eigh(self.c, UPLO='U')
        self.d = self.d.sqrt().diag_embed()
        return ranked_results

best_reward = None
with torch.no_grad():
    cma_es = FastCMA(N = len(assets), samples=args.batch)
    for epoch in range(args.iter):
        try:
            res = cma_es.step()
        except Exception as e: 
            print(e)
            break
        weights = sparsemax(res[0]['parameters'], dim=0)
        r = calculate_reward(weights.unsqueeze(0), 
            valid_data[-test_size:], index[-test_size:])
        if best_reward is None: best_reward = r
        if r < best_reward:
            best_reward = r
            print('epoch: %i v_loss: %f' % (epoch, best_reward))
            bw = weights.detach().cpu().numpy()
            bw = pd.DataFrame(bw).set_index([assets])
            bw = bw.loc[~(bw==0).all(axis=1)]
            bw = bw.reindex(bw[0].abs().sort_values(ascending=False).index)
            bw.to_csv('best_weights.csv', header=False)
```

#### File: `gnn_es_index.py`
```python
##########################################
#Kamer Ali Yuksel linkedin.com/in/kyuksel#
##########################################

def init_weights(model):
    for m in model.modules():
        if isinstance(m, nn.BatchNorm1d):
            m.weight.data.fill_(1)
        elif isinstance(m, nn.Linear):
            nn.init.xavier_uniform_(m.weight, gain = 5/3)
        if hasattr(m, 'bias') and m.bias is not None: m.bias.data.zero_()

class LSTMModule(nn.Module):
    def __init__(self, input_size = 1, hidden_size = 1, num_layers = 2):
        super(LSTMModule, self).__init__()
        self.rnn = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.h = torch.zeros(num_layers, 1, hidden_size, requires_grad=True).to(device)
        self.c = torch.zeros(num_layers, 1, hidden_size, requires_grad=True).to(device)
    def forward(self, x):
        self.rnn.flatten_parameters()
        out, (h_end, c_end) = self.rnn(x, (self.h, self.c))
        self.h.data = h_end.data
        self.c.data = c_end.data
        return out[:,-1, :].flatten()

class Extractor(nn.Module):
    def __init__(self, latent_dim, ks = 5):
        super(Extractor, self).__init__()
        self.conv = nn.Conv1d(args.noise, latent_dim,
            bias = False, kernel_size = ks, padding = (ks // 2) + 1)
        self.conv.weight.data.normal_(0, 0.01)
        self.activation = nn.Sequential(nn.BatchNorm1d(
            latent_dim, track_running_stats = False), nn.Mish())
        self.gap = nn.AvgPool1d(kernel_size = args.batch, padding = 1)
        self.rnn = LSTMModule(hidden_size = latent_dim)
    def forward(self, x):
        y = x.unsqueeze(0).permute(0, 2, 1)
        y = self.rnn(self.gap(self.activation(self.conv(y))))
        return torch.cat([x, y.repeat(args.batch, 1)], dim = 1)

class Generator(nn.Module):
    def __init__(self, noise_dim = 0):
        super(Generator, self).__init__()
        def block(in_feat, out_feat):
            return [nn.Linear(in_feat, out_feat), nn.Tanh()]
        self.model = nn.Sequential(
            *block(noise_dim+args.cnndim, 512), *block(512, 1024), nn.Linear(1024, len(assets)))
        init_weights(self)
        self.extract = Extractor(args.cnndim)
        self.std_weight = nn.Parameter(torch.zeros(len(assets)).to(device))
    def forward(self, x):
        mu = self.model(self.extract(x))
        return mu, mu + (self.std_weight * torch.randn_like(mu))

actor = Generator(args.noise).to(device)
opt = torch.optim.AdamW(filter(lambda p: p.requires_grad, actor.parameters()), lr=1e-3)

best_reward = None

for epoch in range(args.iter):
    torch.cuda.empty_cache()
    #dweights is a noisy version of the weights, use weights for validation
    weights, dweights = actor(torch.randn((args.batch, args.noise)).to(device))
    
    #robustness of portfolio candidates against dropping 75% of their weights
    #the portfolio candidates should be robust when their weights are dropped
    dweights = nn.functional.dropout(dweights, p = 0.75).softmax(dim=1)
    
    loss = calculate_reward(dweights, valid_data[:-test_size], index[:-test_size], True).mean()
    opt.zero_grad()
    loss.backward()
    nn.utils.clip_grad_norm_(actor.parameters(), 1.0)
    opt.step()

    with torch.no_grad():
        #take mean of quality-diversity candidates and spasify using sparsemax
        #entmax15 actually is better but resulting portfolios are less sparse
        weights = sparsemax(weights.mean(dim=0), dim=0)
        test_reward = calculate_reward(weights.unsqueeze(0), 
            valid_data[-test_size:], index[-test_size:])[0]

        if best_reward is None: best_reward = test_reward
        if test_reward < best_reward:
            best_reward = test_reward
            print('epoch: %i v_loss: %f' % (epoch, best_reward))
            bw = weights.detach().cpu().numpy()
            bw = pd.DataFrame(bw).set_index([assets])
            bw = bw.loc[~(bw==0).all(axis=1)]
            bw = bw.reindex(bw[0].abs().sort_values(ascending=False).index)
            bw.to_csv('best_weights.csv', header=False)
```

#### File: `gecco2023/gnn_es_index.py`
```python
import matplotlib.pyplot as plt
torch.set_printoptions(precision=10)

def init_weights(model):
    for m in model.modules():
        if isinstance(m, nn.BatchNorm1d):
            m.weight.data.fill_(1)
        elif isinstance(m, nn.Linear):
            nn.init.xavier_uniform_(m.weight, gain = 5/3)
        if hasattr(m, 'bias') and m.bias is not None: m.bias.data.zero_()

class LSTMModule(nn.Module):
    def __init__(self, input_size = 1, hidden_size = 1, num_layers = 2):
        super(LSTMModule, self).__init__()
        self.rnn = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.h = torch.zeros(num_layers, 1, hidden_size, requires_grad=True).to(device)
        self.c = torch.zeros(num_layers, 1, hidden_size, requires_grad=True).to(device)
    def forward(self, x):
        self.rnn.flatten_parameters()
        out, (h_end, c_end) = self.rnn(x, (self.h, self.c))
        self.h.data = h_end.data
        self.c.data = c_end.data
        return out[:,-1, :].flatten()

class Extractor(nn.Module):
    def __init__(self, latent_dim, ks = 5):
        super(Extractor, self).__init__()
        self.conv = nn.Conv1d(args.noise, latent_dim,
            bias = False, kernel_size = ks, padding = (ks // 2) + 1)
        self.conv.weight.data.normal_(0, 0.01)
        self.activation = nn.Sequential(nn.BatchNorm1d(
            latent_dim, track_running_stats = False), nn.Mish())
        self.gap = nn.AvgPool1d(kernel_size = args.batch, padding = 1)
        self.rnn = LSTMModule(hidden_size = latent_dim)
    def forward(self, x):
        y = x.unsqueeze(0).permute(0, 2, 1)
        y = self.rnn(self.gap(self.activation(self.conv(y))))
        return torch.cat([x, y.repeat(args.batch, 1)], dim = 1)

class Generator(nn.Module):
    def __init__(self, noise_dim = 0):
        super(Generator, self).__init__()
        def block(in_feat, out_feat):
            return [nn.Linear(in_feat, out_feat), nn.Tanh()]
        self.model = nn.Sequential(
            *block(noise_dim+args.cnndim, 512), *block(512, 1024), nn.Linear(1024, len(assets)))
        init_weights(self)
        self.extract = Extractor(args.cnndim)
        self.std_weight = nn.Parameter(torch.zeros(len(assets)).to(device))
    def forward(self, x):
        mu = self.model(self.extract(x))
        return mu, mu + (self.std_weight * torch.randn_like(mu))

def corr(X, eps=1e-08):
    D = X.shape[-1]
    std = torch.std(X, dim=-1).unsqueeze(-1)
    mean = torch.mean(X, dim=-1).unsqueeze(-1)
    X = (X - mean) / (std + eps)
    return 1/(D-1) * X @ X.transpose(-1, -2)
    
def calculate_reward(weights, valid_data, index_data, train = False):
    diff = weights.matmul(valid_data.T) - index_data
    if not train: return diff.clamp(max=0.0).pow(2).mean(dim=1)

    #weight the training returns by recency in performance calculation
    ww = torch.arange(1, diff.shape[1]+1).pow(0.5).to(device)

    #the performance is calculated from randomly selected 25% returns
    diff = nn.functional.dropout(diff, p = 0.75)

    #minimize the maximum correlation in-between portfolio candidates
    corr_max = corr(diff).fill_diagonal_(0.0).max(dim=1)[0]

    return (diff.clamp(max=0.0).pow(2) * (ww/ww.sum())).sum(dim=1) * corr_max
    
actor = Generator(args.noise).to(device)
opt = torch.optim.AdamW(filter(lambda p: p.requires_grad, actor.parameters()), lr=1e-3)

best_reward = None

for epoch in range(args.iter):
    torch.cuda.empty_cache()
    weights, dweights = actor(torch.randn((args.batch, args.noise)).to(device))

    #robustness of portfolio candidates against dropping 75% of their weights
    dweights = nn.functional.dropout(dweights, p = 0.75).softmax(dim=1)

    loss = calculate_reward(dweights, valid_data[:-test_size], index[:-test_size], True).mean()
    opt.zero_grad()
    loss.backward()
    nn.utils.clip_grad_norm_(actor.parameters(), 1.0)
    opt.step()

    with torch.no_grad():
        #entmax15 actually is better but resulting portfolios are less sparse

        plot_w = weights.clone()

        weights = sparsemax(weights.mean(dim=0), dim=0)
        test_reward = calculate_reward(weights.unsqueeze(0), 
            valid_data[-test_size:], index[-test_size:])[0]

        if best_reward is None: best_reward = test_reward
        if test_reward < best_reward:
            best_reward = test_reward
            print('epoch: %i v_loss: %f' % (epoch, best_reward))
            bw = weights.detach().cpu().numpy()
            bw = pd.DataFrame(bw).set_index([assets])
            bw = bw.loc[~(bw==0).all(axis=1)]
            bw = bw.reindex(bw[0].abs().sort_values(ascending=False).index)
            bw.to_csv('best_weights.csv', header=False)


        ttt = 'Out-of-Sample Test | Epoch %i | Loss %f (Red is Tracked Index, Blue is Sparse Ensemble)' % (epoch, test_reward.item())
        plot_w = sparsemax(plot_w, dim=1)
        plot_r = plot_w.matmul(valid_data[-test_size:].T).cumsum(dim=1)
        avg_r = weights.matmul(valid_data[-test_size:].T).cumsum(dim=0).detach().cpu().numpy()
        ind_r = index[-test_size:].cumsum(dim=0).detach().cpu().numpy()
        plt.figure(figsize=(18, 12))
        plt.clf()
        ax = None
        for ret in plot_r:
            ax = pd.DataFrame(ret.detach().cpu().numpy()).plot(figsize=(24, 12),
                legend = False, alpha=0.1, ylim =(-0.5, 1.5), ax = ax)

        ax = pd.DataFrame(avg_r).plot(figsize=(24, 12), legend = False,
            linewidth = 2, color='b', ylim =(-0.5, 1.5), ax = ax)

        ax = pd.DataFrame(ind_r).plot(figsize=(24, 12), legend = False,
            linewidth = 2, color='r', ylim =(-0.5, 1.5), ax = ax, title = ttt)

        plt.savefig('test_' + str(1000 + epoch),
            bbox_inches='tight', pad_inches=0)
        plt.close()
```


==================================================


## [3/3] Repository: portfolio-optimize (`PHASE4-QUANT-174`)
- **Full Name**: `PHASE4-QUANT-174_manujajay__portfolio-optimize`
- **Description**: A simple Python package for optimizing investment portfolios using historical return data from Yahoo Finance. Users can easily determine the optimal portfolio allocation among a given set of tickers based on the mean-variance optimization method or other algorithms.
- **GitHub Stars**: 105
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Portfolio Optimize

A simple Python package for optimizing investment portfolios using historical return data from Yahoo Finance. Users can easily determine the optimal portfolio allocation among a given set of tickers based on the mean-variance optimization method or other algorithms.

## Features

- Easy-to-use interface for defining a portfolio of tickers.
- Supports customization of the data window (in years) for historical data analysis.
- Allows choosing between mean-variance optimization and other optimization algorithms.
- Includes functionality to plot the efficient frontier for the selected portfolio.

## Installation

```
pip install portfolio-optimize
```

## Usage

### Portfolio Optimization

```python
from portfolio_optimize.portfolio_optimize import PortfolioOptimize

# Initialize the optimizer
portfolio = PortfolioOptimize(tickers=["MSFT", "AAPL", "GOOG"], window=5, optimization="MV")

# Optimize the portfolio
optimal_weights = portfolio.optimize()

print(optimal_weights)
```

### Plotting the Efficient Frontier

```python
# Assuming you've already created and optimized the `portfolio` as shown above

# Plot the efficient frontier for the set of tickers
portfolio.graph()
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This software is provided for educational purposes only. It is not intended for financial, investment, trading, or any other type of professional advice. Use at your own risk. The author(s) and contributors do not accept any responsibility for any decisions or actions taken based on the use of this software. Always conduct your own research and consult with financial advisors before making any investment decisions.

## Contributing

This project is under ongoing development, and contributions, corrections, and improvements are welcome. Please feel free to open issues or pull requests on [GitHub](https://github.com/manujajay/portfolio-optimize/tree/main) if you have suggestions or code enhancements.

### Core Implementation Code & Architecture
#### File: `portfolio_optimize/__init__.py`
```python
from .optimizer import PortfolioOptimize
```

#### File: `test.py`
```python
from portfolio_optimize.portfolio_optimize import PortfolioOptimize

# Define your parameters directly
tickers = ["AAPL", "MSFT", "GOOG"]
window = 5  # years
optimization = "MV"  # Mean-Variance Optimization

# Initialize, optimize, and plot in a few lines
portfolio = PortfolioOptimize(tickers=tickers, window=window, optimization=optimization)
optimal_weights = portfolio.optimize()
print("Optimal Weights:", optimal_weights)
portfolio.graph()
```

#### File: `example.py`
```python
from portfolio_optimize import PortfolioOptimize

# Define your stock tickers and parameters
tickers = ["AAPL", "MSFT", "GOOG"]
window = 5  # years of data
optimization = "MV"  # mean-variance optimization

# Initialize and run the optimizer
portfolio = PortfolioOptimize(tickers=tickers, window=window, optimization=optimization)
optimal_weights = portfolio.optimize()
print("Optimal Weights:", optimal_weights)

# Plot the efficient frontier
portfolio.graph()

# Perform and display backtesting results
portfolio.backtest()
```

#### File: `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="portfolio-optimize",
    version="1.2.2",  # Incrementing version to reflect new changes
    author="Manu Jayawardana",
    author_email="manujajayawardanais@gmail.com",
    description="A Python package for portfolio optimization. (Note: This package is under ongoing development. Contributions and corrections are welcome!)",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/manujajay/portfolio-optimize", 
    packages=find_packages(),
    install_requires=["numpy", "pandas", "yfinance", "matplotlib", "tqdm"],  # Updated dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

#### File: `portfolio_optimize/optimizer.py`
```python
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from tqdm.auto import tqdm

class PortfolioOptimize:
    def __init__(self, tickers, window=5, optimization='MV'):
        """
        Initializes the portfolio optimization class.

        Parameters:
        - tickers: List of stock tickers to include in the portfolio.
        - window: The number of years of historical data to consider for optimization.
        - optimization: The type of optimization to perform ('MV' for mean-variance).
        """
        self.tickers = tickers
        self.window = window
        self.optimization = optimization
        self.weights = None
        self.returns = None
        self.cov_matrix = None
        self.data = None
        self.risk_free_rate = None

    def fetch_risk_free_rate(self):
        """Fetches the current risk-free rate using the 13-week Treasury bill rate (^IRX) as a proxy."""
        print("Fetching the current risk-free rate...")
        treasury_ticker = '^IRX'
        end_date = datetime.today()
        start_date = end_date - timedelta(days=365 * self.window)
        treasury_data = yf.download(treasury_ticker, start=start_date, end=end_date)['Adj Close']
        # Convert the average annual yield to a daily rate
        self.risk_free_rate = treasury_data.mean() / 100 / 252
        print("Risk-free rate fetched.")


    def fetch_data(self):
        """Fetches historical stock data for the given tickers."""
        print("Fetching historical stock data...")
        end_date = datetime.today()
        start_date = end_date - timedelta(days=365 * self.window)
        self.data = yf.download(self.tickers, start=start_date, end=end_date)['Adj Close']
        print("Stock data fetched.")


    def calculate_expected_returns_and_cov(self):
        """Calculates expected returns and the covariance matrix for the stocks."""
        print("Calculating expected returns and covariance matrix...")
        returns = self.data.pct_change().dropna()
        self.returns = returns.mean()
        self.cov_matrix = returns.cov()
        print("Calculations completed.")

    def optimize(self):
        """
        Optimizes the portfolio to maximize the Sharpe ratio, which is the ratio of
        excess return to volatility.
        """
        print("Starting portfolio optimization...")
        if self.data is None:
            self.fetch_data()
        if self.risk_free_rate is None:
            self.fetch_risk_free_rate()
        self.calculate_expected_returns_and_cov()

        num_assets = len(self.tickers)
        bounds = tuple((0.0, 1.0) for asset in range(num_assets))

        def objective(weights):
            port_return = np.dot(weights, self.returns) * 252
            port_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights))) * np.sqrt(252)
            sharpe_ratio = (port_return - self.risk_free_rate) / port_volatility
            return -sharpe_ratio  # We minimize the negative Sharpe ratio to maximize it

        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1},)
        initial_guess = num_assets * [1. / num_assets,]

        result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        self.weights = result.x
        print("Optimization completed.")
        return dict(zip(self.tickers, self.weights))

    def graph(self):
        """
        Plots the efficient frontier for the portfolio. The efficient frontier shows
        the highest expected return for a given level of risk.
        """
        if self.cov_matrix is None or self.returns is None:
            print("You must optimize the portfolio before plotting.")
            return
        
        print("Plotting the efficient frontier...")
        num_portfolios = 10000
        results = np.zeros((3, num_portfolios))

        for i in tqdm(range(num_portfolios), desc="Simulating portfolios"):
            weights = np.random.random(len(self.tickers))
            weights /= np.sum(weights)
            port_return = np.dot(weights, self.returns) * 252
            port_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights))) * np.sqrt(252)
            sharpe_ratio = (port_return - self.risk_free_rate) / port_volatility
            results[0,i] = port_volatility
            results[1,i] = port_return
            results[2,i] = sharpe_ratio
        
        plt.scatter(results[0,:], results[1,:], c=results[2,:], cmap='viridis')
        plt.colorbar(label='Sharpe Ratio')
        plt.xlabel('Volatility (Standard Deviation)')
        plt.ylabel('Expected Return')
        plt.title('Efficient Frontier')
        plt.show()

    def portfolio_performance(self, weights):
        """
        Calculates the performance of the portfolio based on the given weights.
        
        Returns the portfolio's expected annual return, volatility, and Sharpe ratio.
        """
        print("Calculating portfolio performance...")
        port_return = np.dot(weights, self.returns) * 252
        port_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights))) * np.sqrt(252)
        sharpe_ratio = (port_return - self.risk_free_rate) / port_volatility
        return port_return, port_volatility, sharpe_ratio

    def backtest(self):
        """
        Simulates historical performance of the optimized portfolio, plots the cumulative returns,
        and calculates key performance metrics.
        """
        if self.weights is None:
            print("Optimization must be completed before backtesting.")
            return

        # Calculate daily returns of the portfolio
        daily_returns = self.data.pct_change()
        portfolio_daily_returns = daily_returns.dot(self.weights)

        # Calculate cumulative returns
        cumulative_returns = (1 + portfolio_daily_returns).cumprod()

        # Plot cumulative returns
        plt.figure(figsize=(10, 6))
        cumulative_returns.plot()
        plt.title('Portfolio Cumulative Returns')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.show()

        # Performance metrics
        total_return = cumulative_returns.iloc[-1] - 1
        annualized_return = np.power(cumulative_returns.iloc[-1], 252 / len(portfolio_daily_returns)) - 1
        annualized_volatility = portfolio_daily_returns.std() * np.sqrt(252)
        sharpe_ratio = (annualized_return - self.risk_free_rate) / annualized_volatility

        # Display performance metrics
        print(f"Total Return: {total_return:.2%}")
        print(f"Annualized Return: {annualized_return:.2%}")
        print(f"Annualized Volatility: {annualized_volatility:.2%}")
        print(f"Sharpe Ratio: {sharpe_ratio:.2f}")


# Example usage
tickers = ["AAPL", "MSFT", "GOOG"]
portfolio = PortfolioOptimize(tickers=tickers, window=5, optimization='MV')
optimal_weights = portfolio.optimize()
print("Optimal Weights:", optimal_weights)
portfolio.graph()
```


==================================================
