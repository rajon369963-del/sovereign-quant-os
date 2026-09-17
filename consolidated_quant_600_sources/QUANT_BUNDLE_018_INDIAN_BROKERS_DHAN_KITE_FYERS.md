# ⚡ [QUANT-SOURCE-018] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_018_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Learn.NSE-Algorithm (`WHEEL_Learn.NSE-Algorithm`)
- **Full Name**: `Learn.NSE-Algorithm`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
## Learn++.NSE Algorithm
Learn++.NSE is an ensemble-based batch learning algorithm that uses weighted majority voting, where the weights are dynamically updated with respect to the classifiers’ time-adjusted errors on current and past environments.

### References
1. Elwell, R., & Polikar, R. (2011). Incremental learning of concept drift in nonstationary environments. IEEE Transactions on Neural Networks, 22(10), 1517-1531.

### Core Implementation Code & Architecture
#### File: `test.py`
```python
from LearnNSE import *

# get the dataset in next time step
def get_next_dataset(df, batch, k, target_name):
    '''
    @df: data frame
    @batch: the number of training datasets you need
    @k: the kth time in the training and testing loop, where k > 0
    @target_name: the name of the target column
    '''
    # get sub-dataset of all dataset, which length equals to batch
    X_train = df[(k-1)*batch : (k)*batch]

    # X_train, y_train
    y_train = pd.DataFrame(X_train[target_name])
    X_train = X_train.drop(columns=target_name)

    return X_train, y_train

############# Training Learn++.NSE #############
# record
record = []

# number of run time
RunTime = 10 # default=10

# count the time length
time_length = len(df) # df is your dataframe
batch = int((1/RunTime)*time_length) # take 1/RunTime of all dataset

# set a model
LearnPPNSE = LearnNSE()

# framework
for k in range(1,RunTime+1):
    # at least a model inside    
    if k == 1:
        # get the dataset for training
        X_train, y_train = get_next_dataset(df=df, batch=batch, k=k, target_name='Label')
        # training model
        LearnPPNSE.fit(X_train, y_train)
        # re-compute voting weight
        LearnPPNSE.revoting(X_train, y_train)
        
    else:
        # get the dataset for training
        X_train, y_train = get_next_dataset(df=df, batch=batch, k=k, target_name='Label')
        # re-build the error distribution
        LearnPPNSE.redistribute_error_rate(X_train, y_train)
        # training model
        LearnPPNSE.fit(X_train, y_train)
        # re-compute voting weight
        LearnPPNSE.revoting(X_train, y_train)

    # testing & recording the score
    if k < RunTime:
        X_test, y_test = get_next_dataset(df=df, batch=batch, k=k+1, target_name='Label')
        score_B = LearnPPNSE.score(X_test, y_test)
        record.append(round(score, 3))
################################################
```

#### File: `LearnNSE.py`
```python
import numpy as np
import math
import copy as cp
from sklearn.ensemble import RandomForestClassifier

# define dot function: calculate the inner product used in recompute voting weight.
def dot(K, L):
   if len(K) != len(L):
      return 0
   return sum(i[0] * i[1] for i in zip(K, L))

class LearnNSE:
    '''Learn++.NSE ensemble classifier
    <Parameters>
    @base_classifier: arbitary supervised classifier (default=RandomForestClassifier)
    @slope: float (default=0.5)
    @crossing_point: float (default=10.0)
    @models: list (default=None)
    @voting_weights: list (default=None)
    @error_weights: list (default=None)
    @error_distribution: list (default=None)
    '''
    def __init__(self, base_classifier=RandomForestClassifier(n_estimators=100, random_state=10),
                 alpha=0.5, beta=10.0):
        self.base_classifier = cp.deepcopy(base_classifier) # reset a model for current dataset
        self.models = []
        self.slope = alpha
        self.crossing_point = beta
        self.voting_weights = [1.0] # default=1.0 
        self.error_distribution = []
        self.bkts = [] # save beta computed from the formula based on punishment of error rate
        self.wkts = []

    def fit(self, X_train, y_train):
        '''Function fit(): training model, and ensemble them
        <Parameters>
        @X_train: Dataframe
            A multi-dimension dataset for training model
        @y_train: Dataframe {0,1,2,...,n}
            The set of label of each line of training data
        @base_classifier: arbitary supervised classifier (default=RandomForestClassifier)
            For training new sub-classifier into self.models
        '''
        clf = cp.deepcopy(self.base_classifier)
        clf.fit(X_train, y_train)
        self.models.append(clf)

    def predict(self, X_test):
        '''Function predict(): testing model, and get the result from the ensemble model
        <Parameters>
        @X_test: Dataframe
            A multi-dimension dataset for testing model
        
        <Returns>
        @y_pred: numpy.ndarray
            A numpy.ndarray with the label prediction for all the samples in X
        '''
        y_pred = []
        t = len(self.models)
        for idx in range(len(X_test)):
            weighted_pred = [0.0]
            temp_pred = []
            for k in range(1, t+1):
                clf = self.models[k-1]
                temp_target = clf.predict(X_test[idx:idx+1]) # Take a column of data each time to predict
                # add new label
                if (temp_target[0]+1) > len(weighted_pred):
                    weighted_pred.append(0.0)
                # add voting weight in corresponding index
                weighted_pred[temp_target[0]] += self.voting_weights[k-1]

            temp_pred.append(weighted_pred.index(max(weighted_pred))) # Get the Max value in the List as prediction of that row (X)
            y_pred.append(temp_pred)
        return np.array(y_pred) # Todo: prediction needs to time the weight
    
    def score(self, X_test, y_test):
        '''Function score(): testing model, and ensemble them
        <Parameters>
        @X_test: Dataframe
            A multi-dimension dataset for testing model
        @y_test: Dataframe
            The set of label of each line of testing data
        @score_list: List
            Save the prediction accuracy in binary 
        '''
        score_list = []
        y_pred = self.predict(X_test)
        for idx in range(len(X_test)):
            if y_pred[idx] == y_test.values[idx][0]:
                score_list.append(1)
            else:
                score_list.append(0)
        return np.sum(score_list)/len(score_list)
    
    def redistribute_error_rate(self, X_train, y_train): # number of models = t-1
        '''Function redistribute_error_rate(): redistribution on newest dataset for evaluate all of the classifier in Learn++.NSE
        <Parameters>
        @X_train: Dataframe
            A multi-dimension dataset for training model
        @y_train: Dataframe {0,1,2,...,n}
            The set of label of each line of training data
        '''
        error_distribution = []
        ErrorRate = 1.0-self.score(X_train, y_train) 
        y_pred = self.predict(X_train)
        for idx in range(len(X_train)):
            if y_pred[idx] == y_train.values[idx][0]:
                error_distribution.append(ErrorRate)
            else:
                error_distribution.append(1)
        self.error_distribution = error_distribution

    def revoting(self, X_train, y_train): # number of models = t
        '''Function revoting(): update the weight based on error rate for output the prediction
        <Parameters>
        @X_train: Dataframe
            A multi-dimension dataset for training model
        @y_train: Dataframe {0,1,2,...,n}
            The set of label of each line of training data
        @ekt: float
            The punishment of each sub-classifier
        '''
        # check whether self.error_distribution need initialization
        if len(self.error_distribution) == 0:
            self.error_distribution = [1/len(X_train)]*len(X_train)

        ##### Step 5-1. Compute the Error-based Weight #####
        # bkt_list = [] # Record penalties until all models have been evaluated
        t = len(self.models)
        self.bkts.append([])  
        for k in range(1, t+1):
            clf = self.models[k-1]
            ekt = 0
            y_pred = clf.predict(X_train)
            for idx in range(len(X_train)):
                if y_pred[idx] != y_train.values[idx][0]:
                    ekt += self.error_distribution[idx]
            
            ekt = ekt/np.sum(self.error_distribution)
            # print('ekt={}'.format(ekt)) # check the performance of each model on newest dataset
            if ekt > 0.5:
                bkt = 0.5/(1-0.5)
            else:
                bkt = ekt/(1-ekt)
            # store normalized error for this classifier
            self.bkts[k-1].append(bkt)
        #####################################################

        ##### Step 5-2. Compute the Time-based Weigh t#####
        # compute the (time) weighte for each model on current time step
        curr_wkt_list = []
        self.wkts.append([])    
        for k in range(1, t+1):
            wkt = 1.0 / (1.0 + np.exp((-1)*self.slope*(t - k - self.crossing_point)))
            curr_wkt_list.append(wkt)
        # compute the (time) weighted normalized errors for kth classifier h_k
        t = len(self.models)
        for k in range(1, t+1):
            wkt = curr_wkt_list[k-1]
            
            if len(self.wkts[k-1]) != 0:
                wkt = wkt/(np.sum(self.wkts[k-1]) + wkt)
            else:
                wkt = wkt/wkt # the time weight of newest model 
            # store the normalized (time) errors
            self.wkts[k-1].append(wkt)
        ####################################################

        ##### Step 6. Calculate the voting weight #####
        voting_weight_list = []
        for k in range(1, t+1):
            TimeAndErrorWeight = np.sum(dot(self.bkts[k-1], self.wkts[k-1])) + 5e-2 # add deviation 5e-2 to avoid that the value equals to 0
            voting_weight_list.append(np.log(1/TimeAndErrorWeight))
        self.voting_weights = voting_weight_list
        ###############################################
```


==================================================


## [2/3] Repository: Multi-Regime-Algorithmic-Trading-System (`WHEEL_Multi-Regime-Algorithmic-Trading-System`)
- **Full Name**: `Multi-Regime-Algorithmic-Trading-System`
- **Description**: Regime-adaptive algorithmic trading system achieving 2.276 portfolio Sharpe ratio across Indian equities (NIFTY50, RELIANCE, SUNPHARMA, VBL, YESBANK) with novel RSI boosting innovation, symbol-specific strategy design, and 5-layer validation framework.
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Multi-Regime Algorithmic Trading System

[![Sharpe](https://img.shields.io/badge/Portfolio_Sharpe-2.276-brightgreen?style=for-the-badge)](docs/VALIDATION_REPORT.md)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> Regime-adaptive quantitative trading system achieving **2.276 portfolio Sharpe ratio**
> through symbol-specific strategies, novel RSI boosting innovation (+1,120% Sharpe gain),
> and rigorous 5-layer validation methodology.

---

## 🔥 What Makes This System Unique

### 1. Symbol-Specific Strategy Design
Different strategies for different asset classes:
- **Indices (NIFTY50):** Trend-following with momentum ladders
- **Large-Cap (RELIANCE, SUNPHARMA):** Multi-timeframe mean-reversion  
- **Mid-Cap (VBL, YESBANK):** Regime-adaptive volatility strategies

**Key Insight:** Indices ≠ Stocks. Microstructure differences require tailored approaches.

### 2. Novel RSI Boosting Innovation ⭐
**Discovery:** +3-4 RSI point confirmation delay = massive Sharpe improvements

```python
# Traditional RSI
if RSI < 30: ENTER_LONG()  # Baseline

# Boosted RSI (Our Innovation)
if RSI < 34: ENTER_LONG()  # +4 points
```

**Impact:**
- SUNPHARMA: 3.32 → **4.29 Sharpe (+29%)**
- YESBANK: 0.14 → **1.76 Sharpe (+1,120%)**
- Mechanism: Filters 40% false signals while keeping 95% true entries

### 3. 5-Layer Validation Framework
- Train/Test Split: 2.30 → 2.21 Sharpe (-4% degradation = stable)
- Walk-Forward: 6 windows, <0.30 degradation threshold
- Monte Carlo: 10K simulations, 58th percentile (non-lucky)
- Parameter Sensitivity: Smooth curves, no lucky spikes
- Cost Stress Test: Robust to 2x transaction costs

---

## 📊 Strategy Performance Breakdown

| Symbol | Strategy | Sharpe | Trades | Win Rate | Return |
|--------|----------|--------|--------|----------|--------|
| **SUNPHARMA** 🏆 | V2 Boosted | **4.292** | 134 | 68% | +16.60% |
| **RELIANCE** | Hybrid Adaptive V2 | **2.985** | 128 | 64% | +13.82% |
| **VBL** | Regime Switching | **2.276** | 163 | 58% | +12.45% |
| **NIFTY50** | Trend Ladder | **1.456** | 125 | 56% | +10.23% |
| **YESBANK** | Baseline (Fixed) | **0.373** | 132 | 52% | +7.50% |

**SUNPHARMA 4.292 Sharpe = Best-in-Competition Strategy**

---

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/ridash2005/Multi-Regime-Algorithmic-Trading-System.git
cd Multi-Regime-Algorithmic-Trading-System
pip install -r requirements.txt
```

### Run Backtest
```bash
# Single symbol
python src/backtest_single.py --symbol SUNPHARMA --strategy V2Boosted

# Full portfolio
python src/backtest_portfolio.py --config configs/final_submission.yaml
```

### Validation Tests
```bash
python src/validate_strategies.py --mode train_test_split
python src/validate_strategies.py --mode walk_forward
python src/validate_strategies.py --mode monte_carlo
```

---

## 📁 Repository Structure

```
Multi-Regime-Algorithmic-Trading-System/
├── src/
│   ├── strategies/                    # 20+ strategy implementations
│   │   ├── hybrid_adaptive_v2.py      # RELIANCE/SUNPHARMA (2.985/4.292 Sharpe)
│   │   ├── regime_switching_strategy.py # VBL volatility-adaptive (2.276 Sharpe)
│   │   ├── nifty_trend_ladder.py      # Index trend-following (1.456 Sharpe)
│   │   └── ...
│   ├── utils/                         # RSI, EMA, KER, regime detection
│   ├── optimization/                  # Bayesian hyperparameter search
│   ├── optimizers/                    # Symbol-specific optimizers
│   ├── submission/                    # Submission file generators
│   ├── validation/                    # Outlier & compliance checks
│   └── legacy/                        # Earlier strategy iterations
├── config/                            # Strategy parameters & settings
├── data/raw/                          # FYERS historical OHLCV data
├── docs/                              # Technical documentation
├── experiments/                       # Research & experiment scripts
├── scripts/                           # Utility & automation scripts
├── reports/figures/                   # Performance visualizations
├── submission/                        # Final competition submissions
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📚 Documentation

- **[Strategy Overview](docs/STRATEGY_OVERVIEW.md)** — Complete technical breakdown per symbol
- **[Optimization Journey](docs/OPTIMIZATION_JOURNEY.md)** — How Sharpe improved from 1.486 → 2.276
- **[Validation Report](docs/VALIDATION_REPORT.md)** — 5-layer robustness testing methodology
- **[Code Architecture](docs/CODE_ARCHITECTURE.md)** — System design and component overview
- **[Results Analysis](docs/RESULTS_ANALYSIS.md)** — Detailed performance metrics
- **[RSI Boosting Paper](docs/QUANT_GAMES_2026/RSI_BOOSTING_PAPER.md)** — Academic write-up of the novel technique
- **[Lessons Learned](docs/LESSONS_LEARNED.md)** — Engineering and quant insights

---

## 🎓 Academic Foundation

**Key Techniques:**
- **Ornstein-Uhlenbeck Process:** Optimal mean-reversion thresholds
- **Kelly Criterion:** Mathematically optimal position sizing
- **Kaufman Efficiency Ratio (KER):** Regime detection
- **Markowitz Portfolio Theory:** Optimal capital allocation

**References:**
1. Connors, L. (2016). *Short-Term Trading Strategies That Work*
2. Bertram, W.K. (2010). *Analytic Solutions for Optimal Statistical Arbitrage*
3. Kaufman, P.J. (2013). *Trading Systems and Methods*

---

## 💡 Innovation Highlights

### RSI Boosting Mechanism
Traditional RSI mean-reversion enters at oversold (RSI < 30). We discovered that 
delaying entry by +3-4 RSI points filters false breakdown signals while preserving 
genuine reversals.

**Hypothesis:** Early reversals (RSI 26-30) often fail. True reversals show persistence 
(RSI stays < 34 for 2-3 bars).

**Validation:** Monte Carlo simulations (10K runs) confirm effect is statistically 
significant, not data-mined.

### Publication Potential
This finding is **conference-quality** and suitable for submission to:
- Journal of Computational Finance
- Algorithmic Finance
- IEEE Conference on Computational Intelligence for Financial Engineering

---

## 🛠️ Technologies

- **Python 3.9+** — Core language
- **NumPy/Pandas** — Vectorized computation
- **Optuna** — Bayesian optimization
- **Matplotlib** — Visualization
- **FYERS API v3** — Market data

---

## 📄 License

MIT License — See [LICENSE](LICENSE) for details.

---

### Core Implementation Code & Architecture
#### File: `src/optimization/__init__.py`
```python
# Optimization module
```

#### File: `src/legacy/check_data.py`
```python
"""Check data sizes for all symbols and timeframes."""
import pandas as pd
import os

timeframes = ['1day', '1hour']
symbols = [
    'NSE_NIFTY50_INDEX',
    'NSE_RELIANCE_EQ', 
    'NSE_VBL_EQ',
    'NSE_YESBANK_EQ',
    'NSE_SUNPHARMA_EQ'
]

print("DATA SIZE ANALYSIS")
print("=" * 60)

for tf in timeframes:
    print(f"\n{tf.upper()} TIMEFRAME:")
    print("-" * 40)
    for sym in symbols:
        file = f"fyers_data/{sym}_{tf}.csv"
        if os.path.exists(file):
            df = pd.read_csv(file)
            start = df['datetime'].iloc[0][:10] if len(df) > 0 else 'N/A'
            end = df['datetime'].iloc[-1][:10] if len(df) > 0 else 'N/A'
            print(f"  {sym:20} - {len(df):4} bars ({start} to {end})")
        else:
            print(f"  {sym:20} - FILE NOT FOUND")
```

#### File: `src/legacy/quick_test.py`
```python
"""Quick test - output to file."""
import pandas as pd
from strategy1_rsi2_meanrev import generate_signals

symbols = [
    ("NIFTY50", "fyers_data/NSE_NIFTY50_INDEX_1hour.csv"),
    ("RELIANCE", "fyers_data/NSE_RELIANCE_EQ_1hour.csv"),
    ("VBL", "fyers_data/NSE_VBL_EQ_1hour.csv"),
    ("YESBANK", "fyers_data/NSE_YESBANK_EQ_1hour.csv"),
    ("SUNPHARMA", "fyers_data/NSE_SUNPHARMA_EQ_1hour.csv"),
]

results = []
for name, file in symbols:
    df = pd.read_csv(file)
    df_s = generate_signals(df.copy(), None)
    buy_count = (df_s['signal'] == 1).sum()
    status = "PASS" if buy_count >= 120 else "FAIL"
    results.append(f"{status}: {name:12} - {buy_count} trades")

with open("trade_counts.txt", "w") as f:
    f.write("TRADE COUNT AFTER FIXES\n")
    f.write("="*50 + "\n")
    for r in results:
        f.write(r + "\n")
    f.write("="*50 + "\n")

print("Results written to trade_counts.txt")
```

#### File: `scripts/run_full_optimization.py`
```python
"""
MAIN OPTIMIZATION EXECUTION SCRIPT

Single command to run complete Optuna optimization for all symbols.
"""

import sys
from pathlib import Path
import argparse

# Add project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.optimization.parallel_optimizer import run_parallel_optimization

def main():
    parser = argparse.ArgumentParser(description="Run Optuna Parallel Optimization")
    parser.add_argument('--trials', type=int, default=200, help='Number of trials per symbol')
    parser.add_argument('--symbols', nargs='+', help='List of symbols to optimize (default: all)')
    parser.add_argument('--quick-test', action='store_true', help='Run short test (10 trials)')
    
    args = parser.parse_args()
    
    trials = 10 if args.quick_test else args.trials
    
    print(f"🚀 Initializing Optuna Optimization...")
    run_parallel_optimization(symbols=args.symbols, n_trials=trials)
    print("\n✅ Run 'python scripts/generate_final_submission.py' to generate artifacts.")

if __name__ == "__main__":
    main()
```

#### File: `src/legacy/validate_all.py`
```python
"""Quick validation script to check all symbols meet 120 trade minimum."""
import pandas as pd
import sys
sys.path.insert(0, '.')
from strategy1_rsi2_meanrev import generate_signals, Config, BacktestEngine

symbols = [
    ("NIFTY50", "fyers_data/NSE_NIFTY50_INDEX_1hour.csv"),
    ("RELIANCE", "fyers_data/NSE_RELIANCE_EQ_1hour.csv"),
    ("VBL", "fyers_data/NSE_VBL_EQ_1hour.csv"),
    ("YESBANK", "fyers_data/NSE_YESBANK_EQ_1hour.csv"),
    ("SUNPHARMA", "fyers_data/NSE_SUNPHARMA_EQ_1hour.csv"),
]

print("="*60)
print("TRADE COUNT VALIDATION - ALL SYMBOLS")
print("="*60)

all_pass = True
for name, file in symbols:
    df = pd.read_csv(file)
    df_s = generate_signals(df.copy(), None)
    buy_count = (df_s['signal'] == 1).sum()
    status = "PASS" if buy_count >= 120 else "FAIL"
    if buy_count < 120:
        all_pass = False
    print(f"{status}: {name:12} - {buy_count:3} trades")

print("="*60)
if all_pass:
    print("ALL SYMBOLS MEET 120 TRADE MINIMUM - READY FOR SUBMISSION")
else:
    print("SOME SYMBOLS BELOW MINIMUM - NEEDS ADJUSTMENT")
```

#### File: `scripts/check_data_leakage.py`
```python
"""
CHECK DATA LEAKAGE
Verify strict timestamp ordering and Rule 12 compliance
"""

import pandas as pd
import os
import sys

def check_data_leakage():
    submission_dir = 'submission_new'
    print(f"Checking {submission_dir} for Data Leakage...")
    
    files = [f for f in os.listdir(submission_dir) if f.startswith('STRATEGY5') and f.endswith('.csv')]
    
    overall_status = True
    
    for f in files:
        path = os.path.join(submission_dir, f)
        df = pd.read_csv(path)
        
        # 1. Check Time Flow
        df['entry_time'] = pd.to_datetime(df['entry_trade_time'])
        df['exit_time'] = pd.to_datetime(df['exit_trade_time'])
        
        time_travel = df[df['exit_time'] <= df['entry_time']]
        
        # 2. Check Sorting
        sorted_check = df['entry_time'].is_monotonic_increasing
        
        if len(time_travel) > 0:
            print(f"❌ {f:40} : {len(time_travel)} trades exit before entry! 🚨")
            overall_status = False
        elif not sorted_check:
            print(f"⚠️ {f:40} : Trades not sorted chronologically")
            # Not a fatal error but bad practice
        else:
            print(f"✅ {f:40} : Time Flow Correct")
            
    if overall_status:
        print("\n✅ DATA LEAKAGE CHECK PASSED")
    else:
        print("\n❌ DATA LEAKAGE DETECTED")

if __name__ == "__main__":
    check_data_leakage()
```


==================================================


## [3/3] Repository: My-Algo-Trading-Code (`WHEEL_My-Algo-Trading-Code`)
- **Full Name**: `My-Algo-Trading-Code`
- **Description**: Python algorithmic trading suite: signal generators, backtests, and a multithreaded paper-trading runner for NIFTY/BANKNIFTY/FINNIFTY via the Dhan API. Also contains a Claude-based AI agent for SL hunting-based strategies and a Codex-based AI agent for CPR-based strategies
- **GitHub Stars**: 13
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# My-Algo-Trading-Code
This contains all the code I have written for the signal generation and the front test where I fetch data using Dhan API

# Live track record
I have been running these strategies **live** (real broker orders) since **May 2026**. The day-by-day results are recorded here:

📈 **[Live results spreadsheet](https://docs.google.com/spreadsheets/d/1y4VgThcLywZbOibKC_pyKbh0A5u1xtgL_cZvyHp3FYg/edit?gid=1163843320#gid=1163843320)**

# The code
Although I own the code, the coding itself was done entirely using GPT-5.4-xhigh, GPT-5.5-xhigh, GPT-5.6 Sol xhigh and Claude Opus 4.7, Claude Opus 4.8, Claude Opus 5 on Max/Ultracode effort. GPT wrote majority of the signal generators and the data fetch files. Claude wrote the big one - the multithreaded Front Test worker. I just did the reviews and the testing. While Claude Fable 5 did one thorough audit of the whole repository

# What is included?
- Data extractors which extract historical data for NIFTY/BANKNIFTY/FINNIFTY indices
- The backtest files I used to backtest
- The signal generators I created to generate signals
- The main front test file which uses miltithreading to execute all strategies together
- Live order execution to a real broker — selectable among **Kotak Neo**, **Shoonya (Finvasia)**, **Flattrade Pi v2**, and **Dhan** — gated by a global kill-switch and per-strategy paper/live toggles (everything defaults to paper)
- Live Telegram alerts: the front-test master file can post every entry/exit (option instrument, lot size, entry/exit price, and P&L) to a Telegram group/channel
- An **optional, opt-in LLM trading agent** — the "SL Hunting AI Agent" — a Claude agent that trades a discretionary price-action method on NIFTY options; off by default, paper unless explicitly enabled, and fail-soft (see Recent additions)

- An optional **CPR Codex AI Agent**: an independent five-minute SRSI/VWAP strategy with four frozen read-only MCP tools, deterministic host-owned execution/risk gates, SIDEWAYS current-expiry naked premium sells, unchanged TRENDING option buys, safe disabled defaults, and the standard live double gate

# Recent additions
- **Crash-durable session recovery.** Every entry/exit and per-strategy realized-P&L roll-up is atomically persisted during the session, while open positions are refreshed from cache every 30 seconds. A restart archives the exact prior file before writing anything, always carries same-day losses into matching workers so daily max-loss limits cannot reset, and only resumes an open position when the opt-in paper-only validation gate accepts its complete contract and risk geometry. Local shutdown completion and successful Google Sheet publication are recorded separately; see [ADR-0012](docs/adr/0012-crash-durable-session-state.md).
- **CPR Codex AI Agent (independent, opt-in).** `CPRAIWorker` freezes session levels, momentum/VWAP, market structure, and position state once per completed five-minute bar. Codex makes a dynamic regime/setup or premise-exit judgment, while the host alone validates entry geometry, stop distance, levels, sizing, time cutoffs, lifecycle state, and execution. Accepted SIDEWAYS setups are expressed as naked current-expiry premium sells (bullish sells ATM PE; bearish sells ATM CE); TRENDING setups retain the existing ATM CE/PE option buys and expiry. The worker is disabled by default and live-disabled by default; real buys and sells require both `LIVE_TRADING_ENABLED=true` and `CPR_AI_LIVE_TRADING=true`, plus normal startup exposure audit/config validation. A spot stop triggers buy-to-close but cannot guarantee a loss cap through gaps, illiquidity, latency, or a rejected exit. CPR, CPR Algo 3, Regime Adaptive, and CPR AI are independent strategies that may run together with independent positions and independent P&L. The approximately 27-strategy core roster can reach about 29 configured workers when both optional AI agents are enabled, while enable and virtual-trading gates keep the running roster configuration-dependent. Install the exact optional set from `requirements-ai.txt` (shared with SL Hunting); see the [focused CPR AI README](Signal%20Generators/CPR%20AI%20Agent/README.md) for the strategy, isolation boundary, and zero-order smoke commands.
- **Config-drift audit — `python algo.py check-env`.** Settings live in three places that drift apart silently: your gitignored `.env`, the committed `env.example` template, and the in-code default behind every `_env_*` call. A key present in the code and the template but missing from `.env` is **not** an error — the runner just uses the in-code default — which is what makes it easy to miss: an unseen default ends up governing a live-money run. This read-only command reports settings missing from your `.env`, mistyped or stale keys (a typo means the setting you intended is not being applied at all), and knobs missing from the template. It exits non-zero on findings so it can gate a pre-flight script, and prints key **names only** — never a value out of your `.env` — so its output is safe to share. CI enforces the same rule in the other direction: a new `_env_*` key cannot land without its `env.example` entry.
- **Per-strategy size multiplier — `<PREFIX>_SIZE_MULTIPLIER`.** One knob per strategy (default **1**, whole numbers up to **25**) that scales that strategy's entire size/risk set together: its lot count, its per-trade risk budget, its hard lot cap, and its daily max-loss kill-switch. At `2` a 5-lot cap becomes 10, a Rs.2,500 budget becomes Rs.5,000, a Rs.5,500 daily cap becomes Rs.11,000, and a setup that would have taken 4 lots takes 8 — so position size can grow with the **account** by editing one number instead of four that must be kept consistent by hand. Deliberately **per-strategy only** (no global switch, so one typo cannot enlarge every enabled strategy) and it applies to **paper and live alike**, so an enlarged size can be paper-validated first. Anything malformed (`0`, `2.5`, `30`, `"two"`) falls back to 1 for paper and **blocks that strategy from live trading** rather than guessing a size. Leave every multiplier unset to trade exactly as before. Two consequences worth knowing: the scaled budget also loosens the "one lot exceeds the budget" skip, and because lots are floored a 2x can land slightly above a pure doubling (still strictly inside the scaled budget). For SL Hunting, note its BankNIFTY mirror already roughly doubles basket risk, so a multiplier of M leaves the basket near 2xM times the single-leg budget.
- **Optional websocket market data producer — `MARKET_DATA_SOURCE=WEBSOCKET`.** The runner can now source its market data from Dhan's marketfeed websocket instead of REST polling (requires Dhan's paid Data API subscription; any other value of the flag fails closed to the default REST poller). Ticks build the 1-minute candles live — the forming minute updates in real time — and once per minute the completed candles are trued-up against Dhan's official REST candles (official wins; divergence is logged), so strategy bars converge to exactly what the backtests used. All LTPs (NIFTY spot plus every subscribed option leg, including multi-leg baskets: hedged pairs, Delta-0.2's four legs, strangle legs, the SL Hunting BankNIFTY mirror) stream from ticks in real time, with legs subscribed/unsubscribed dynamically as workers enter and exit. REST stays for warmup history and reconnect gap-backfill; API load drops from one full-window pull every 2-5s to ~1/minute. The market-data health gates (10s LTP / 150s bar / 30s liquidation) behave identically, with one tick-feed-aware twist: quiet-but-subscribed legs stay fresh only while the socket is demonstrably alive. Rollback is `MARKET_DATA_SOURCE=REST` + restart; the tick logic lives in `Dependencies/tick_bar_builder.py`.
- **Per-strategy "off" switch — `<PREFIX>_VIRTUAL_TRADING`.** Every strategy now has a virtual (paper) toggle that **defaults to true**. Set it false to stop that strategy's worker thread from starting at all — so it does no paper trading (and, since the thread never runs, no live trading either). Unlike live trading there is **no** global master switch: the default is that everything runs, and you silence individual strategies. Lets you run just the strategies you want on a given day instead of the whole roster.
- **Quality gates & CI.** A GitHub Actions workflow (`.github/workflows/quality-and-security.yml`) runs the full gate on every push/PR across Python 3.12 + 3.13: all repository suites, branch-coverage budgets, `pip-audit`, `compileall`, **Ruff**, **mypy** (scoped in `pyproject.toml`), **Bandit**, and pre-commit validation. Exact tooling lives in `requirements.txt` alongside the runtime pins.
- **SL Hunting AI Agent — BankNIFTY mirror basket + newer knowledge (v3c–v3e).** The agent now trades Intraday Hunter's multi-index style: every NIFTY entry is mirrored with an **equal-lot BankNIFTY ATM** leg (`SL_HUNTING_BNF_MIRROR`, default true). The two legs are **tied for hard risk** (stop/target, max-loss, 15:15 square-off close both) but the agent evaluates each leg's **premise independently** and can cut one alone via the EXIT `exit_leg` selector (`NIFTY` | `BNF` | `BOTH`). Entry stays NIFTY-only (the mirror copies it). Its knowledge also grew several distilled-from-video layers — a scoped **gap-up opening-drive**, a **2-week verbatim transcript sweep**, and a **live-day match** against the agent's own journal (details in `Signal Generators/SL Hunting AI Agent/README.md`).
- **Optional LLM trading agent — the "SL Hunting AI Agent" (opt-in worker).** A Claude agent (via the [`claude-agent-sdk`](https://pypi.org/project/claude-agent-sdk/) on your Claude subscription — **no API key**) trades the discretionary *SL Hunting* price-action method on NIFTY ATM options. Once per completed 1-min bar (the method's native timeframe) it reads the NIFTY chart (with **BankNIFTY cross-confirmation**) and — only on a confirmed setup at a real level — acts through the SAME tested `enter_position`/`exit_position` path as every other worker. Position sizing floors affordable whole lots, never exceeds `SL_HUNTING_RISK_BUDGET`, skips one-lot-over-budget setups, and caps at `SL_HUNTING_MAX_LOTS` (default 5); the equal-lot BankNIFTY mirror can roughly double basket risk. It **stops opening new positions after 10:30** (`SL_HUNTING_NO_NEW_ENTRY_HOUR`/`_MINUTE`, default 10:30) — *not* a square-off: open positions, their stops/targets, and the 15:15 square-off are unaffected. Its post-exit cooldown starts only when the whole NIFTY/BankNIFTY basket is confirmed flat, so an independently surviving or partly closed leg cannot run the timer down; exits never consult this guard, while unreadable guard state rejects new live entries. It is **off by default** (`SL_HUNTING_ENABLED`), trades **paper** unless both `LIVE_TRADING_ENABLED` and `SL_HUNTING_LIVE_TRADING` are set, and is **fail-soft** — any agent/SDK error becomes a safe HOLD while its separate mechanical risk loop keeps checking stop, target, max-loss, stale data, and square-off. It can also **learn from its own trades** through a tool-free, schema-validated reflection coach with digest-bound human approval (paper-first, off by default). Install the exact optional stack with `pip install -r requirements-ai.txt` and run one-time `claude setup-token` (keep `ANTHROPIC_API_KEY` **UNSET** so it bills your Claude plan, not per-token API). Full details — knowledge, tools, safety model, the learning loop — are in `Signal Generators/SL Hunting AI Agent/README.md`. It joins the configuration-dependent worker roster only when enabled.
- **CPR Algo 3 (multi-instrument) is now wired into the front test.** A new `CPRAlgo3StrategyWorker` runs the "CPR basic setup" strategy, which watches THREE charts at once — the NIFTY spot plus a ~ITM CE and a ~ITM PE of the current-week expiry — and only fires when VWAP and the CPR band align across all three (RSI/ARSI on spot). The two ITM options are **observation only**: a signal still BUYS the ATM CE/PE of the next-next expiry through the same tested path as the other directional workers, so it shares CPR's risk knobs (tunable via `CPR_ALGO3_*` in `.env`, including `CPR_ALGO3_ITM_OFFSET`). It fetches the two option 1-min OHLC feeds on demand and drives its own spot target/stop exit. It belongs to the core roster, while the enabled total remains configuration-dependent. (The standalone Algo 3 signal generator + its unit tests live under `Signal Generators/CPR Strategy/`.)
- **Code-quality pass.** Added a `requirements.txt`; gave every Shoonya broker HTTP call a timeout (a hung call could otherwise stall a worker thread and the shared broker lock); removed hardcoded credentials from the vendored Shoonya client; routed the execution layer's status/errors through `logging` instead of `print()`; and ported the master test suite into the repo (`Tests/test_nifty_multi_strategy_master.py` — see Tests below).
- **Live broker execution is broker-selectable (Kotak Neo, Shoonya, or Flattrade).** `LIVE_BROKER` picks `KOTAK`, `SHOONYA`, or `FLATTRADE`, and every real order goes through one generic `execution_client`. The global `LIVE_TRADING_ENABLED` kill-switch and each strategy's `<PREFIX>_LIVE_TRADING` flag must both be true; unknown broker names fail closed to paper. Each broker folder contains an execution client and a read-only diagnostic with an optional, typed-`YES`, round-trip test order. Flattrade uses its official Pi v2 browser-token flow, exact NFO index scrip master, documented request limits, market-order protection, and `SingleOrdHist` fill confirmation. Everything still defaults to paper. (Shoonya's legacy QuickAuth endpoint is being decommissioned by Finvasia.)
- **End-of-day P&L is now written to a Google Sheet.** When all workers exit on a clean end of day, the master parses the run's log for each strategy's realised P&L and writes it into a tracker sheet — one row per strategy, one column per calendar day — overwriting today's cell and backfilling any blank earlier-this-month cells from the (append-mode) log. Auth is OAuth user-token via `gspread`; configure `GSHEET_ID` + an OAuth client in `.env` (see Setup). It's a safe no-op when unconfigured, so it never disturbs shutdown.
- **13 TradingBot signal-generator ports.** Thirteen ATM single-leg strategies were ported into `Signal Generators/` (SMA Crossover, Bollinger Bands, Keltner Squeeze, Mean Reversion Z-Score, ML Ensemble, Multi-Timeframe, Opening Range Breakout, Parabolic SAR, RSI Divergence, RSI Reversal, Stochastic, Supertrend, Volatility Breakout), all sharing `misc_strategy_common.py` and the mandatory TA-Lib 0.6.8 indicator backend. They're wired through the shared `AtmSingleLegStrategyWorker` factory and each is tunable from `.env` by its own prefix. ML Ensemble needs `scikit-learn`.
- **Regime Adaptive — one router, two rules.** A fourteenth port through the same factory, but from a different project ([`workratananmol-hub/nifty-options-paper-trading-bot`](https://github.com/workratananmol-hub/nifty-options-paper-trading-bot), MIT). Instead of one rule it reads ADX each bar and switches: an **opening-range breakout** confirmed by VWAP when the market trends, a **fade back to VWAP** when it ranges, and **no trade at all** when ADX is missing — it never guesses the regime. The two candidate rules live in `Regime Adaptive Strategy/regime_candidates.py` as library code with no worker of their own, so the router can never double up on a candidate's signal. Tunable by `REGIME_ADAPTIVE_*`. **Read `Signal Generators/Regime Adaptive Strategy/REGIME_PORTING_NOTES.md` before enabling it live:** this runner receives no volume, so its VWAP is an equal-weight proxy. The source's India VIX and breadth vetoes are **not implemented** — absent by choice rather than for want of data (the source project runs on Dhan too).
- **Bid/ask spread gate — `<PREFIX>_MAX_SPREAD_PCT`.** Most single-leg strategies buy options; CPR AI SIDEWAYS may instead sell one. Either opening side crosses the same quoted market, so a wide spread is an immediate execution cost before the idea has done anything. The runner reads `top_bid_price`/`top_ask_price` off the `/optionchain` response for the exact strike and expiry and refuses an entry quoted wider than the cap. A too-wide spread is refused in **paper and live alike** (it's a market fact, so paper rows stay predictive); an **unreadable** quote refuses **live only** and lets paper through with a warning (an API failure shouldn't cost you a paper data point, but it also shouldn't spend real money on a check that didn't run). Workers share one 3-second cache because Dhan allows a single option-chain request per 3s per underlying/expiry. **Default `0` — off — for every strategy except Regime Adaptive (2.0)**, so no existing strategy's behaviour changed.
- **CPR (Central Pivot Range) strategy is now live in the front test.** It runs as an ATM single-leg worker (`CPRStrategyWorker`) alongside the other strategies: the master file feeds it 1-min OHLC, the CPR logic resamples to complete 5-min candles internally, and a LONG/SHORT signal buys the ATM CE/PE of the next-next expiry. Tunable via `CPR_*` knobs in the `.env` (lots, max-loss, poll, 09:25-15:15 window). (This brought the master file to nine workers at the time; the running roster is now configuration-dependent.)
- **Read-only live dashboard (optional, off by default).** The runner can serve a browser page on `http://127.0.0.1:8787/` showing open trades with live marks and running P&L, today's closed trades grouped by strategy, per-strategy realized/open/total, and a live NIFTY candle chart. It answers "where do I stand right now", which the log, Telegram and the once-a-day Sheet do not. It is read-only by construction (GET only, never touches the broker, cannot place or cancel an order), binds loopback only with no host setting, and runs on its own thread so it can never delay a trading decision. Switch it on with `DASHBOARD_ENABLED=true`; see `docs/lld/monitoring-dashboard.md`.
- **Telegram trade notifications.** A queue-based `TelegramMessageWorker` posts a message to a Telegram group/channel on every entry and exit from *any* worker. Each alert shows the strategy, the exact option instrument(s), lot size, entry and exit price, and P&L (hedged spreads show both legs). It runs on its own thread so Telegram latency or downtime never blocks the trading loop, and it's a cheap no-op when disabled. See Setup below to switch it on.

# Pro Tip
You might have to adjust the import addresses from which the files are to be imported because the files are in different directories in my local machine(fixed in the latest Claude commit)

# Repository structure
```
.
├── nifty_multi_strategy_master.py   # ~27 core strategies + independently opt-in agents
├── Data Extractors/                                   # 1m OHLC downloaders + shared helper
├── My Backtest Files (For Reference)/                 # backtesting.py-based backtests
├── Signal Generators/                                 # strategy / signal logic modules
├── Tests/                                             # EVERY test, mirroring the tree above
├── docs/                                              # architecture docs: hld/, lld/, adr/
└── Dependencies/                                      # shared config + live-execution layer
    ├── env.example                                    # copy to Dependencies/.env and fill in
    ├── dhan_token_setup.py                            # one-time DhanHQ OAuth token setup
    ├── Kotak API/                                     # kotak_execution.py + diagnose_kotak_symbol.py
    ├── Shoonya API/                                   # NorenApi.py + shoonya_execution.py + diagnose_shoonya_symbol.py
    ├── Flattrade API/                                 # flattrade_execution.py + diagnose_flattrade_symbol.py
    └── Dhan API/                                      # dhan_execution.py + diagnose_dhan_symbol.py
```
Each subfolder has its own `Readme.md` with the details.

# Setup
1. Python 3.10+ (I'm running 3.13).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   That covers the core (data fetch, backtests, runner) plus the quality-gate tooling. Install exact optional sets only when needed:
   ```
   pip install -r requirements-ai.txt        # BOTH AI agents: Claude + Codex SDK, shared MCP stack
   pip install pyotp==2.9.0 websocket-client==1.8.0  # Shoonya runtime
   pip install --no-deps "git+https://github.com/Kotak-Neo/Kotak-neo-api-v2.git@v2.0.1#egg=neo_api_client"
   ```
   Flattrade uses the core `requests` and `pandas` dependencies. Shoonya's NorenApi
   client is vendored, as is TradingView's Apache-2.0 `lightweight-charts` build used
   by the optional dashboard (`Dependencies/dashboard_assets/vendor/`, with its licence,
   an attribution NOTICE and the file's SHA-256). Kotak's official tag declares older exact pandas/requests
   versions, so `--no-deps` prevents it from silently downgrading the audited core
   runtime. `requirements-brokers.txt` records and tests the upstream broker
   dependency environment separately in CI; do not combine it with `requirements.txt`.
3. Configure credentials. Copy `Dependencies/env.example` to `Dependencies/.env` and fill it in (`.env` is git-ignored). Set your Dhan credentials there, then run the one-time token setup:
   ```
   python "Dependencies/dhan_token_setup.py"
   ```
   It walks you through the DhanHQ OAuth login and writes a fresh `DHAN_ACCESS_TOKEN` back into `.env`. All tunable strategy parameters live in this same `.env`.
4. (Optional) Turn on Telegram trade alerts by adding these to the master file's `.env`:
   ```
   TELEGRAM_ENABLED=true
   TELEGRAM_BOT_TOKEN=your_botfather_token
   TELEGRAM_CHAT_ID=@your_channel_or_-100xxxxxxxxxx
   ```
   Create the bot via @BotFather and add it to your group/channel as an admin. Leave `TELEGRAM_ENABLED=false` (the default) to run without alerts. The token stays in `.env`, which is git-ignored.

4b. (Optional) Turn on the read-only live dashboard by adding to the master file's `.env`:
   ```
   DASHBOARD_ENABLED=true
   DASHBOARD_PORT=8787
   ```
   Then open `http://127.0.0.1:8787/` while the runner is up. It binds loopback only and there is deliberately no host setting — reaching it from another machine is a reviewed code change plus a token, not a line in `.env`. Every other `DASHBOARD_*` knob has a sensible default and is clamped at read time; see `Dependencies/env.example`.

5. (Optional) End-of-day P&L to Google Sheets. After all workers exit, the master writes each strategy's day-end P&L into a tracker sheet (one row per strategy, one column per day, with month backfill). Enable it by adding to the master's `.env`:
   ```
   GSHEET_ID=your_spreadsheet_id
   GSHEET_OAUTH_CLIENT_FILE=Dependencies/gsheet_oauth_client.json
   GSHEET_OAUTH_TOKEN_FILE=Dependencies/gsheet_oauth_token.json
   ```
   Auth is OAuth user-token via `gspread`: in Google Cloud enable the Sheets API, create an OAuth client of type **Desktop app**, download its JSON to `GSHEET_OAUTH_CLIENT_FILE`, and share the sheet with your Google account. The first run opens a browser once for consent and caches a token at `GSHEET_OAUTH_TOKEN_FILE`. PAPER results use the existing row labels in column A (e.g. `Renko Strategy`); LIVE and MIXED results use separate `Renko Strategy [LIVE]` and `Renko Strategy [MIXED]` rows so real-money outcomes cannot contaminate paper history. Unmatched strategies are skipped with a warning. Leave `GSHEET_ID` blank to disable (safe no-op).

6. (Optional) Live broker execution. Everything is paper by default. To place REAL orders, set in `Dependencies/.env`:
   ```
   LIVE_TRADING_ENABLED=true        # global kill-switch (default false)
   LIVE_BROKER=KOTAK                # KOTAK, SHOONYA, FLATTRADE, or DHAN
   RENKO_LIVE_TRADING=true          # flip the specific strategies you want live
   ```
   Then fill the selected broker's credential block. Flattrade needs `FLATTRADE_CLIENT_ID`, `FLATTRADE_API_KEY`, and `FLATTRADE_API_SECRET`; its optional `FLATTRADE_ACCESS_TOKEN` is validated when supplied, otherwise startup opens browser authorization and asks for the returned `request_code`. A strategy trades live only when `LIVE_TRADING_ENABLED` **and** its own `<PREFIX>_LIVE_TRADING` are both true. An entry falls back to paper only after a typed zero-fill `REJECTED`; `PARTIAL` or `UNKNOWN` means exposure may exist, freezes new live entries, and starts reconciliation. Check connectivity first with the read-only diagnostics — they can place a confirmation-gated round-trip (buy + auto square-off) test order via `--place-order`:
   ```
   python "Dependencies/Kotak API/diagnose_kotak_symbol.py" CE 23950 --place-order
   python "Dependencies/Shoonya API/diagnose_shoonya_symbol.py" CE 23950 26JUN25 --place-order
   python "Dependencies/Flattrade API/diagnose_flattrade_symbol.py" CE 24150 14JUL26 --place-order
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `Signal Generators/SL Hunting AI Agent/lessons.json`
```python
[]
```

#### File: `Tests/Signal Generators/SL Hunting AI Agent/conftest.py`
```python
"""Pytest bootstrap for the SL Hunting AI Agent.

The agent's folder name contains spaces and its modules import each other by
bare name (`import sl_hunting_tools`, etc.), so that folder goes on ``sys.path``
before the tests import anything.

The path points at the SOURCE agent folder under ``Signal Generators/``, not at
this mirrored test folder -- the tests import the real modules.
"""

from __future__ import annotations

import os
import sys

# Tests/Signal Generators/SL Hunting AI Agent/<this file> -> repository root is
# three levels up.
_REPO_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
_AGENT_DIR = os.path.join(_REPO_ROOT, "Signal Generators", "SL Hunting AI Agent")
if _AGENT_DIR not in sys.path:
    sys.path.insert(0, _AGENT_DIR)
```

#### File: `Tests/Signal Generators/CPR AI Agent/test_cpr_ai_master_integration.py`
```python
"""Guard the package boundary between the new agent and legacy CPR strategies.

This intentionally simple source-level regression scans only CPR AI runtime
modules. It catches accidental reintroduction of the old Algo 1/2/3 arbiter or
its ``CPRToolResult`` contract before master-worker behavior is considered.
"""

from __future__ import annotations

from pathlib import Path


def test_task_two_runtime_does_not_import_the_legacy_cpr_strategy_package():
    """Runtime modules must stay independent before the master wires execution."""

    # Tests/Signal Generators/CPR AI Agent/<this file> -> the SOURCE agent
    # folder lives three levels up, under "Signal Generators/".
    agent_directory = (
        Path(__file__).resolve().parents[3] / "Signal Generators" / "CPR AI Agent"
    )
    runtime_sources = "\n".join(
        path.read_text(encoding="utf-8")
        for path in agent_directory.glob("cpr_ai_*.py")
    )

    assert "cpr_strategy_logic" not in runtime_sources
    assert "CPRToolResult" not in runtime_sources
```

#### File: `Tests/Signal Generators/Regime Adaptive Strategy/conftest.py`
```python
"""Pytest bootstrap for the Regime Adaptive strategy tests.

The strategy's folder name contains spaces and its modules import each other by
bare name (`import regime_common`, etc.), so that folder goes on ``sys.path``
before the tests import anything -- the same pattern as
``SL Hunting AI Agent/conftest.py``.

The parent (`Signal Generators/`) is added too, because ``regime_common``
re-exports the shared indicators from ``misc_strategy_common`` which lives one
level up. At runtime ``regime_common`` bootstraps that itself; under pytest the
import can happen through a different entry point, so it is done here as well.

Both paths point at the SOURCE tree, not at this mirrored test folder -- the
tests import the real modules.
"""

from __future__ import annotations

import os
import sys

# Tests/Signal Generators/Regime Adaptive Strategy/<this file> -> repository root
# is three levels up.
_REPO_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
_SIGNAL_GEN_DIR = os.path.join(_REPO_ROOT, "Signal Generators")
_STRATEGY_DIR = os.path.join(_SIGNAL_GEN_DIR, "Regime Adaptive Strategy")
for _path in (_SIGNAL_GEN_DIR, _STRATEGY_DIR):
    if _path not in sys.path:
        sys.path.insert(0, _path)
```

#### File: `Signal Generators/Subhamoy Strategies/goldmine_signal_generator.py`
```python
"""
NIFTY Goldmine Signal Generator.

This wrapper keeps the public file naming style used by the repo while the
actual strategy math lives in `goldmine_strategy_logic.py`.
"""

from __future__ import annotations

import pandas as pd
from goldmine_strategy_logic import (
    GoldmineDecision,
    GoldminePositionContext,
    GoldmineSignalGenerator,
    GoldmineStrategyConfig,
    generate_goldmine_signals,
    get_latest_goldmine_signal,
)


class NiftyGoldmineSignalGenerator(GoldmineSignalGenerator):
    """NIFTY-flavored wrapper around the shared Goldmine signal generator."""


def generate_nifty_goldmine_signals(
    data: pd.DataFrame,
    config: GoldmineStrategyConfig | None = None,
) -> pd.DataFrame:
    """Return full-history NIFTY Goldmine signals."""
    return generate_goldmine_signals(data, config=config)


def get_latest_nifty_goldmine_signal(
    data: pd.DataFrame,
    config: GoldmineStrategyConfig | None = None,
    position: GoldminePositionContext | None = None,
) -> GoldmineDecision:
    """Return only the newest NIFTY Goldmine decision."""
    return get_latest_goldmine_signal(data, config=config, position=position)


__all__ = [
    "NiftyGoldmineSignalGenerator",
    "generate_nifty_goldmine_signals",
    "get_latest_nifty_goldmine_signal",
]
```

#### File: `Data Extractors/finnifty_1m_5y_data_fetch_dhan.py`
```python
"""
Beginner-friendly FINNIFTY wrapper script.

This file stays lightweight on purpose. The shared fetching logic lives in:
`index_1m_5y_data_fetch_dhan_common.py`

What this wrapper does:
1. Supply FINNIFTY-specific defaults.
2. Reuse the same chunked OHLC download flow as the other index scripts.
3. Save the final CSV in the Backtest Outputs folder.

Default FINNIFTY values used here:
- security_id = 27
- exchange segment = IDX_I
- instrument type = INDEX
- output CSV = Backtest Outputs/finnifty_renko_futures_5y_1min_data.csv
"""

import os

from index_1m_5y_data_fetch_dhan_common import IndexFetchDefaults, run_index_fetcher

# Anchor the default output to <repo_root>/Backtest Outputs/ so the CSV
# always lands in the repo's shared output folder regardless of the cwd
# the script is launched from. `__file__` is at <repo>/Data Extractors/...
# so dirname(dirname(__file__)) == <repo_root>.
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# These defaults make the shared helper behave like a FINNIFTY fetcher.
FINNIFTY_DEFAULTS = IndexFetchDefaults(
    display_name="FINNIFTY",
    security_id="27",
    default_output=os.path.join(
        _REPO_ROOT, "Backtest Outputs", "finnifty_renko_futures_5y_1min_data.csv"
    ),
)


if __name__ == "__main__":
    run_index_fetcher(FINNIFTY_DEFAULTS)
```


==================================================
