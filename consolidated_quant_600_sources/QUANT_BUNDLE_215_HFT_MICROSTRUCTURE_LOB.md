# ⚡ [QUANT-SOURCE-215] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_215_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: HFT-price-prediction (`PHASE4-QUANT-137`)
- **Full Name**: `PHASE4-QUANT-137_hzjken__HFT-price-prediction`
- **Description**: A project of using machine learning model (tree-based) to predict short-term instrument price up or down in high frequency trading. 
- **GitHub Stars**: 186
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# HFT-price-prediction
A project of using machine learning model (tree-based) to predict instrument price up or down in high frequency trading.

## Project Background
A data science hands-on exercise of a high frequency trading company. 

## Task
To build a model with the given data to predict whether the trading price will go up or down in a short future. (classification problem)

## Data Explanation
### Feature Columns
<b>timestamp</b>  str, datetime string.<br>
<b>bid_price</b>  float, price of current bid in the market.<br>
<b>bid_qty</b>  float, quantity currently available at the bid price.<br>
<b>bid_price</b>  float, price of current ask in the market.<br>
<b>ask_qty</b>  float, quantity currently available at the ask price.<br>
<b>trade_price</b>  float, last traded price.<br>
<b>sum_trade_1s</b>  float, sum of quantity traded over the last second.<br>
<b>bid_advance_time</b>  float, seconds since bid price last advanced.<br>
<b>ask_advance_time</b>  float, seconds since ask price last advanced.<br>
<b>last_trade_time</b>  float, seconds since last trade.<br>
### Labels
<b>_1s_side</b> int<br>
<b>_3s_side</b> int<br>
<b>_5s_side</b> int<br>
Labels indicate what is type of the first event that will happen in the next x seconds, where:<br>
<b>0</b> -- No price change.<br>
<b>1</b> -- Bid price decreased.<br>
<b>2</b> -- Ask price increased.<br>

## Process
### Preprocessing
<b>data type conversion</b>: **`preprocessing()`**<br>
<b>data check</b>: **`check_null()`**<br>
<b>missing value handling</b>: **`fill_null()`**,
based on the null check and basic logic, most of the sum_trade_1s null value happens when last_trade_time larger
than 1 sec (in this case sum_trade_1s should be 0). Therefore, we make an assumption that all the sum_trade_1s null
value could be filled with 0. Based on such assumption, last_trade_time can be filled with last_trade_time of the
previous record plus a time movement if record interval is smaller than 1 sec.
### Feature Engineering
<b>correlation filter</b>: **`correlation_filter.filter()`**, remove columns that are highly correlated to reduce data redundancy.<br>
<b>logical feature engineering</b>: **`feature_eng.basic_features()`**, build up some features based on trading logic.<br>
<b>time-rolling feature engineering</b>: **`feature_eng.lag_rolling_features()`**, build up features by lagging and rolling of time-series.<br>
### Feature Selection
**`feature_selection.select()`**, Hybrid approach of genetic algorithm selection plus feature importance selection.<br>
<b>genetic algorithm selection</b>: **`feature_selection.GA_features()`** <br>
<b>feature importance selection</b>: **`feature_selection.rf_imp_features()`** <br>
### Modelling
Ensemble of lightGBM and random forest model.<br>
<b>random forest</b>: **`model.random_forest()`** <br>
<b>lightGBM</b>: **`model.lightgbm()`** <br>
### Parameter Tuning
Based on search space to decide whether using grid search or genetic search for lightGBM model's parameter tuning.<br>
<b>grid search</b>: **`model.GS_tune_lgbm()`** <br>
<b>genetic search</b>: **`model.GA_tune_lgbm()`** <br>
## Performance
Out-of-sample classfication accuracy is roughly 76-78%, which means its prediction of the short-term future price movement is acceptable.

### Core Implementation Code & Architecture
#### File: `modelling_pipeline.py`
```python
import pandas as pd
import numpy as np
import json
from itertools import product
from bisect import bisect_left
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit
from genetic_selection import GeneticSelectionCV
from lightgbm import LGBMClassifier
from evolutionary_search import EvolutionaryAlgorithmSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib
from scipy.stats import mode


def preprocessing(data):
    '''align data type and time order'''
    float_list = [
        'bid_price',
        'bid_qty',
        'ask_price',
        'ask_qty',
        'trade_price',
        'sum_trade_1s',
        'bid_advance_time',
        'ask_advance_time',
        'last_trade_time',
    ]

    data['timestamp'] = pd.to_datetime(data['timestamp'])
    for i in float_list:
        data[i] = data[i].astype(float)

    data = data.sort_values(by='timestamp', ascending=True).reset_index(drop=True)
    return data


def check_null(data):
    '''check null values in dataframe'''
    data = data.copy()
    have_null_cols = list(data.columns[data.isnull().any()])
    print('Columns with null values are {}'.format(', '.join(have_null_cols)))
    for i in have_null_cols:
        print('number of rows that column {} is null: {}'.format(i, data[i].isnull().sum()))
        print('null percentage is {}'.format(round(data[i].isnull().sum() / data.shape[0], 2)))

    stat1 = data['sum_trade_1s'][data['last_trade_time'].isnull()].notnull().sum()
    stat2 = data['last_trade_time'][data['sum_trade_1s'].isnull()].notnull().sum()
    stat3 = data['sum_trade_1s'][data['last_trade_time'] >= 1].isnull().sum()
    stat4 = stat3 / data['sum_trade_1s'].isnull().sum()
    print('number of rows sum_trade_1s is not null when last_trade_time is not: {}'.format(stat1))
    print('number of rows last_trade_time is null when sum_trade_1s is not: {}'.format(stat2))
    print('number of rows sum_trade_1s null at last_trade_time > 1: {}, percentage: {}'.format(stat3, round(stat4, 2)))


def fill_null(data):
    '''
    based on the null check and basic logic, most of the sum_trade_1s null value happens when last_trade_time larger
    than 1 sec (in this case sum_trade_1s should be 0). Therefore, we make an assumption that all the sum_trade_1s null
    value could be filled with 0. Based on such assumption, last_trade_time can be filled with last_trade_time of the
    previous record plus a time movement if record interval is smaller than 1 sec.
    '''

    class last_trade_time_filler:
        prev_last_trade_time = None
        prev_timestamp = None

        @classmethod
        def fill(cls, index):
            last_trade_time = data.loc[index, 'last_trade_time']
            timestamp = data.loc[index, 'timestamp']

            if pd.isnull(last_trade_time):
                time_interval = (timestamp - cls.prev_timestamp).microseconds / (1e+6)
                if time_interval <= 1:
                    last_trade_time = cls.prev_last_trade_time + time_interval
                else:
                    last_trade_time = np.nan

            cls.prev_last_trade_time = last_trade_time
            cls.prev_timestamp = timestamp

            return last_trade_time

    data = data.copy()
    data.loc[data['sum_trade_1s'].isnull(), 'sum_trade_1s'] = 0
    data['last_trade_time'] = data.index.map(last_trade_time_filler.fill)
    print('number of null columns is: {} now'.format(len(list(data.columns[data.isnull().any()]))))

    return data


def x_y_split(data):
    label_cols = ['_1s_side', '_3s_side', '_5s_side']
    feature_cols = list(set(data.columns) - set(label_cols))
    y = data[label_cols].copy()
    x = data[feature_cols].copy()

    return x, y


class correlation_filter:
    remove_cols = []

    @classmethod
    def filter(cls, x, threshold=0.99):
        x = x.copy()
        index2col = {i: col for i, col in enumerate(x.columns)}
        corr = np.array(x.corr())
        correlated_pairs = list(zip(*np.where(np.abs(corr) >= threshold)))
        to_be_delete = []
        for i, j in correlated_pairs:
            former = index2col[i]
            latter = index2col[j]
            if former != latter:
                add = True
                for i, del_set in enumerate(to_be_delete):
                    has_intersect = ({former, latter} & del_set) != {}
                    if has_intersect:
                        add = False
                        to_be_delete[i] = del_set | {former, latter}
                if add:
                    to_be_delete.append({former, latter})

        for i in to_be_delete:
            delete_set = i.copy()
            delete_set.pop()
            x = x.drop(list(delete_set), axis=1)
            cls.remove_cols += list(delete_set)

        return x


class feature_eng:
    timestamp = None
    max_lag = 5
    num_window = [5, 10, 20]
    sec_window = [1, 3, 5, 10]
    rolling_sum_cols = []
    rolling_mean_cols = []
    rolling_max_cols = []
    rolling_min_cols = []
    rolling_std_cols = []

    @staticmethod
    def bid_ask_spread(data):
        data['spread'] = data['ask_price'] - data['bid_price']

    @staticmethod
    def bid_ask_qty_comb(data):
        data['bid_ask_qty_total'] = data['ask_qty'] + data['bid_qty']
        data['bid_ask_qty_diff'] = data['ask_qty'] - data['bid_qty']

    @staticmethod
    def trade_price_feature(data):
        data['trade_price_compare'] = 0  # when trade price between current bid and ask price
        data.loc[data['trade_price'] <= data[
            'bid_price'], 'trade_price_compare'] = -1  # when trade price on current bid side
        data.loc[data['trade_price'] >= data[
            'ask_price'], 'trade_price_compare'] = 1  # when trade price on current sell side

        # whether trade price happens on bid side or ask side during the time it happens
        last_trade_timestamp = data['timestamp'] - pd.to_timedelta(data['last_trade_time'], unit='s')
        idx_list = [bisect_left(data['timestamp'], i) for i in list(last_trade_timestamp)]
        trade_price_pos = []
        for i, index in enumerate(idx_list):
            index1 = index
            index2 = index1 + 1 if index1 < data.shape[0] - 1 else index1
            bid1 = data['bid_price'][index1]
            bid2 = data['bid_price'][index2]
            ask1 = data['ask_price'][index1]
            ask2 = data['ask_price'][index2]
            trade_price = data['trade_price'][i]
            if (bid1 <= trade_price <= bid2) or (bid2 <= trade_price <= bid1):
                trade_price_pos.append(-1)  # happen on bid side
            elif (ask1 <= trade_price <= ask2) or (ask2 <= trade_price <= ask1):
                trade_price_pos.append(1)  # happen on sell side
            else:
                trade_price_pos.append(0)  # unknown case
        data['trade_price_pos'] = trade_price_pos

    @staticmethod
    def diff_feature(data):
        for i in set(data.columns) - {'timestamp'}:
            new_name = '{}_diff'.format(i)
            data[new_name] = data[i] - data[i].shift(1)

    @staticmethod
    def up_or_down(data):
        data['up_down'] = 0
        data.loc[data['bid_price_diff'] < 0, 'up_down'] = -1
        data.loc[data['ask_price_diff'] > 0, 'up_down'] = 1

    @staticmethod
    def lag_feature(data, col, lag):
        new_col_name = '{}_lag_{}'.format(col, lag)
        data[new_col_name] = data[col].shift(lag)

    @staticmethod
    def rolling_feature(data, col, window, feature):
        rolling = data[col].rolling(window=window)
        new_col = '{}_rolling_{}_{}'.format(col, feature, window)

        if feature == 'sum':
            data[new_col] = rolling.sum()
        elif feature == 'mean':
            data[new_col] = rolling.mean()
        elif feature == 'max':
            data[new_col] = rolling.max()
        elif feature == 'min':
            data[new_col] = rolling.min()
        elif feature == 'std':
            data[new_col] = rolling.std()
        elif feature == 'mode':
            data[new_col] = rolling.apply(lambda x: mode(x)[0])

    @classmethod
    def basic_features(cls, data):
        data = data.copy()
        cls.timestamp = data['timestamp']

        cls.bid_ask_spread(data)
        cls.bid_ask_qty_comb(data)
        cls.trade_price_feature(data)
        cls.diff_feature(data)
        cls.up_or_down(data)

        data = data.drop('timestamp', axis=1)
        return data

    @classmethod
    def lag_rolling_features(cls, data):
        data = data.copy()

        # get lag and rolling feature based on previous n records
        rolling_cols = set(data.columns) - {'trade_price_compare', 'trade_price_pos'}
        cls.rolling_sum_cols = [i for i in rolling_cols if 'diff' in i or 'up_down' in i]
        cls.rolling_mean_cols = rolling_cols
        cls.rolling_max_cols = [i for i in rolling_cols if 'bid_qty' in i or 'ask_qty' in i]
        cls.rolling_min_cols = [i for i in rolling_cols if 'bid_qty' in i or 'ask_qty' in i]
        cls.rolling_std_cols = rolling_cols

        for col in rolling_cols:
            for lag in range(1, cls.max_lag + 1):
                cls.lag_feature(data, col, lag)

        for col in rolling_cols:
            for num_window in cls.num_window:
                if col in cls.rolling_sum_cols:
                    cls.rolling_feature(data, col, num_window, 'sum')
                if col in cls.rolling_mean_cols:
                    cls.rolling_feature(data, col, num_window, 'mean')
                if col in cls.rolling_max_cols:
                    cls.rolling_feature(data, col, num_window, 'max')
                if col in cls.rolling_min_cols:
                    cls.rolling_feature(data, col, num_window, 'min')
                if col in cls.rolling_std_cols:
                    cls.rolling_feature(data, col, num_window, 'std')

        # get rolling feature based on previous n seconds
        data.index = cls.timestamp
        for col in rolling_cols:
            for sec_window in cls.sec_window:
                sec_window = '{}s'.format(sec_window)
                if col in cls.rolling_sum_cols:
                    cls.rolling_feature(data, col, sec_window, 'sum')
                if col in cls.rolling_mean_cols:
                    cls.rolling_feature(data, col, sec_window, 'mean')
                if col in cls.rolling_max_cols:
                    cls.rolling_feature(data, col, sec_window, 'max')
                if col in cls.rolling_min_cols:
                    cls.rolling_feature(data, col, sec_window, 'min')
                if col in cls.rolling_std_cols:
                    cls.rolling_feature(data, col, sec_window, 'std')
                if col in ['up_down', 'trade_price_compare', 'trade_price_pos']:
                    cls.rolling_feature(data, col, sec_window, 'mode')

        return data

    @staticmethod
    def remove_na(x, y):
        x = x.reset_index(drop=True)
        x = x.dropna()
        y = y.loc[x.index, :].reset_index(drop=True)
        x = x.reset_index(drop=True)
        return x, y


class feature_selection:
    '''feature selection combining feature importance ranking and GA optimization based on random forest model'''

    @classmethod
    def select(cls, x, y):
        rf_imp_features = cls.rf_imp_features(x, y)
        ga_features = cls.GA_features(x, y)
        features = set(rf_imp_features) | set(ga_features)

        return list(features)

    @classmethod
    def rf_imp_features(cls, x, y, top_perc=0.05):
        '''select top features based on feature importance ranking among all the features'''
        feature_imp = cls.rf_importance_selection(x, y)
        perc_threshold = np.percentile(feature_imp['avg_importance'], int((1 - top_perc) * 100))
        features = list(feature_imp.loc[feature_imp['avg_importance'] >= perc_threshold, 'feature'])

        return features

    @staticmethod
    def rf_importance_selection(x, y, iter_time=3):
        feature_imp = pd.DataFrame(np.zeros((x.shape[1], iter_time + 2)))
        feature_imp.columns = ['feature'] + ['importance_{}'.format(i) for i in range(1, iter_time + 1)] + [
            'avg_importance']
        for col in feature_imp.columns:
            feature_imp[col] = list(x.columns)

        for i in range(1, iter_time + 1):
            col = 'importance_{}'.format(i)
            rf = RandomForestClassifier(n_estimators=10, max_depth=8)
            rf.fit(x, y)
            feature_imp_dict = dict(zip(x.columns, rf.feature_importances_))
            feature_imp[col] = feature_imp[col].replace(feature_imp_dict)

        feature_imp['avg_importance'] = feature_imp.iloc[:, 1:-1].mean(axis=1)
        return feature_imp

    @staticmethod
    def GA_features(x, y):
        rf = RandomForestClassifier(max_depth=8, n_estimators=10)
        selector = GeneticSelectionCV(
            rf,
            cv=TimeSeriesSplit(n_splits=4),
            verbose=1,
            scoring="accuracy",
            max_features=80,
            n_population=200,
            crossover_proba=0.5,
            mutation_proba=0.2,
            n_generations=100,
            crossover_independent_proba=0.5,
            mutation_independent_proba=0.05,
            tournament_size=3,
            n_gen_no_change=5,
            caching=True,
            n_jobs=-1
        )
        selector = selector.fit(x, y)
        features = x.columns[selector.support_]

        return features


class model:
    lgbm_paramgrid = {
        'learning_rate': np.arange(0.0005, 0.0015, 0.0001),
        'n_estimators': range(800, 2000, 200),
        'max_depth': [3, 4],
        'colsample_bytree': np.arange(0.2, 0.5, 0.1),
        'reg_alpha': [1],
        'reg_lambda': [1]
    }

    @staticmethod
    def random_forest(x, y):
        rf = RandomForestClassifier(n_estimators=200, max_depth=8)
        rf.fit(x, y)
        return rf

    @classmethod
    def lightgbm(cls, x, y):
        keys, vals = list(zip(*cls.lgbm_paramgrid.items()))
        products = list(product(*vals))
        param_comb = [dict(zip(keys, i)) for i in products]

        if len(param_comb) > 1000:
            best_param = cls.GA_tune_lgbm(x, y)
        else:
            best_param = cls.GS_tune_lgbm(x, y)

        lightgbm = LGBMClassifier(**best_param)
        lightgbm.fit(x, y)

        return lightgbm

    @classmethod
    def GA_tune_lgbm(cls, x, y):
        tuner = EvolutionaryAlgorithmSearchCV(
            estimator=LGBMClassifier(),
            params=cls.lgbm_paramgrid,
            scoring="accuracy",
            cv=TimeSeriesSplit(n_splits=4),
            verbose=1,
            population_size=50,
            gene_mutation_prob=0.2,
            gene_crossover_prob=0.5,
            tournament_size=3,
            generations_number=20,
        )
        tuner.fit(x, y)
        return tuner.best_params_

    @classmethod
    def GS_tune_lgbm(cls, x, y):
        tuner = GridSearchCV(
            estimator=LGBMClassifier(),
            param_grid=cls.l
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: AlgoTradingNSE (`PHASE4-QUANT-164`)
- **Full Name**: `PHASE4-QUANT-164_akashyadavv__AlgoTradingNSE`
- **Description**: A project that tries to influence buying and selling of stocks using an algorithmic model built using an ensemble of KNN, Decision Tree, Random forest and SVM. The model depicts an ideal scenario for maximizing profits from a trade. A momentum strategy that is used to predict trading signal has been modelled based on a set of rules using various technical indicators
- **GitHub Stars**: 22
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
﻿# Algorithm Trading with ML on NSE stocks.
A project that tries to influence buying and selling of stocks using an algorithmic model built using an ensemble of KNN, Decision Tree, Random forest and SVM. The model depicts an ideal scenario for maximizing profits from a trade. A momentum strategy that is used to predict 
trading signal has been modelled based on a set of rules using various technical indicators.

The dataset compromises 10 year Stock details of 5 stocks namely: RELIANCE, HDFC,ITC,INFOSYS and TCS.
The result of the analysis is the predicted trend of the market index, which can be used to set out some trading rules:
• If the next day trend is Uptrend, then the decision is BUY

• If BUY decision already exists, then HOLD.

• If the next day trend is Downtrend, then the decision is SELL

• If SELL decision already exists, then HOLD

According to the result obtained with these rules, the return of strategy has been calculated.

# Results

An accuracy of 94.2% was achieved which indicates that our model has the capability of reducing the losses compared to the actual returns; if they were calculated on the basis of the previous day's closing price.


==================================================


## [3/3] Repository: AlphaMatrix (`PHASE4-QUANT-185`)
- **Full Name**: `PHASE4-QUANT-185_cearps__AlphaMatrix`
- **Description**: Open-source options trading platform that ingests market data, models volatility (GARCH + greeks), back-tests strategies, and executes them in low-latency Python + C++.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AlphaMatrix – Backend Testing Program

> **Mission:** give quants and engineers an open, hack‑friendly playground to design, back‑test, and (eventually) execute multi‑leg options strategies at low latency.

---

## 1  Project Overview

AlphaMatrix stitches together fast C++ analytics, flexible Python APIs and a modern React front‑end to make option‑strategy research feel as slick as running a unit test.

- **Back‑test first** – every trading idea is a reproducible test‑case.
- **Plug‑in later** – swap data feeds, models or brokers via clean adapters.
- **Showcase skills** – contributors practise real‑world DevOps, C++ optimisation and data‑engineering patterns.

---

## 2  Core Philosophy

| Principle                   | What it means                                                                       |
| --------------------------- | ----------------------------------------------------------------------------------- |
| **Test‑driven alpha**       | Strategies are code + fixtures; CI tells us if new commits break Sharpe or latency. |
| **Vertical slices**         | Ship tiny, end‑to‑end features (data → model → UI) rather than big‑bang layers.     |
| **Teach & learn**           | Each PR includes a short _What I learned_ note; weekly “Alpha Hour” shares tips.    |
| **Performance with safety** | Fast C++ where latency matters, Python for iteration, typed interfaces between.     |

---

## 3  System Architecture (bird’s‑eye)

```
┌─────────────┐  ticks/greeks  ┌──────────────────────────┐  REST/gRPC   ┌──────────────┐
│  C++ GATEWAY│───────────────▶│      Python FastAPI      │──────────────▶│   React UI   │
│  (risk + FIX)│               │   (back‑test + auth)     │   JSON/WS    │ (charts,map) │
└──────┬──────┘                └──────────┬───────────────┘               └────┬─────────┘
       │  Arrow IPC                        │ SQL
       ▼                                   ▼
 ┌─────────────┐        CDC        ┌────────────────┐
 │  ClickHouse │◀──────────────────│ Parquet Landing │
 └─────────────┘                   └────────────────┘
```

- **C++ Gateway** — ultra‑low‑latency FIX/Aeron service; enforces risk before orders hit the street.
- **FastAPI Service** — back‑tester, auth, REST & WebSocket endpoints.
- **ClickHouse** — columnar store for ticks, option chains, and back‑test results.
- **React + Tailwind UI** — strategy wizard, run monitor, greeks heat‑map.

---

## 4  Module Details

| Dir                   | Responsibility                                            | Key Tech                                                 |
| --------------------- | --------------------------------------------------------- | -------------------------------------------------------- |
| `core/`               | Back‑test engine, analytics libs, C++ greeks via pybind11 | C++20, Python 3.12                                       |
| `api/`                | FastAPI app, auth, orchestration of runs                  | FastAPI, Pydantic, Alembic                               |
| `web/`                | Front‑end dashboard & wizard                              | React 19, Vite, shadcn/ui, Recharts                      |
| `scripts/`            | One‑off ETL, benchmarks, dev helpers                      | Python CLI, Rich                                         |
| `ci/`                 | GitHub Actions workflows, lint, latency tests             | actions‑python, clang‑tidy, pytest‑benchmark             |
| `infra/`              | Docker Compose, k8s Helm charts                           | ClickHouse, Postgres, Grafana                            |
| `python/alphamatrix/` | **Shared Package** - ETL + API modules                    | Python, pandas, yfinance, clickhouse-connect, FastAPI ✅ |

> **Note:** API and ETL now live in a shared Python package at `python/alphamatrix/` to enable shared models/utilities. Dockerfiles remain in `infra/`, and secrets are read from `infra/.env` at runtime via volume mounts.

---

## 4.1 ETL + API System

The ETL system provides data ingestion from Yahoo Finance to ClickHouse, and the API service provides REST endpoints for data queries and job management.

### **Quick Start (ETL + API)**

```bash
# Install dependencies
pip install -e ./python[test]

# Run ETL jobs
python -m alphamatrix.etl.jobs.backfill_ohlcv --symbol AAPL --start 2020-01-01 --end 2020-01-10 --interval 1d --dry-run
python -m alphamatrix.etl.jobs.incremental_ohlcv --symbol AAPL --interval 1d --lookback-days 5 --dry-run

# Run API service
uvicorn alphamatrix.api.app:app --host 0.0.0.0 --port 8000

# Docker (from repo root)
docker build -f infra/Dockerfile.etl -t alphamatrix-etl .
docker run --rm -v "$(pwd)/infra/.env:/app/infra/.env:ro" alphamatrix-etl python -m alphamatrix.etl.jobs.backfill_ohlcv --symbol AAPL --start 2020-01-01 --end 2020-01-10 --interval 1d --dry-run

docker build -f infra/Dockerfile.api -t alphamatrix-api .
docker run --rm -p 8000:8000 -v "$(pwd)/infra/.env:/app/infra/.env:ro" alphamatrix-api
```

### **Package Organization**

```
python/alphamatrix/           # Shared Python package
├── etl/                     # ETL modules
│   ├── adapters/           # Data source adapters (Yahoo Finance, etc.)
│   ├── io/                # ClickHouse client
│   ├── transforms/        # Data validation & mapping
│   ├── jobs/              # ETL job runners
│   ├── utils/             # Environment & logging
│   └── tests/             # ETL test suite
│       ├── integration/   # Integration tests
│       └── conftest.py    # Test fixtures
└── api/                    # FastAPI service
    ├── models/            # Pydantic request/response models
    ├── routers/           # API endpoints
    ├── jobrunner.py       # In-process job queue
    └── config.py          # Configuration management

infra/                      # Infrastructure
├── Dockerfile.etl         # ETL container
├── Dockerfile.api         # API container
└── .env                   # Environment configuration (not in repo)
```

**📖 Full Documentation:** See [`python/alphamatrix/api/README.md`](python/alphamatrix/api/README.md) for detailed API usage and development guide.

### **Testing Structure**

Tests are co-located with their respective modules:

- **API tests**: `python/alphamatrix/api/tests/` - Unit tests for FastAPI endpoints
- **ETL tests**: `python/alphamatrix/etl/tests/` - Unit tests for ETL modules
- **Common utilities**: `python/alphamatrix/common/` - Shared logging, environment, and ID generation

**Environment Configuration**: All modules read from `infra/.env` via `alphamatrix.common.env` functions.

---

## 5  Tech Stack

- **Python (API & glue)** – rapid iteration, great data libs.
- **C++ (Core analytics & gateway)** – micro‑second greeks, FIX adapter.
- **React + TypeScript (Front‑end)** – modern, componentised UI with shadcn/ui.
- **ClickHouse (DB)** – ingest millions of rows/sec and query TBs in < 1 s  ([benchmark](https://clickhouse.com/blog/json-bench-clickhouse-vs-mongodb-elasticsearch-duckdb-postgresql)).

---

## 6  Example Workflow

1. **Clone & setup**

   ```bash
   git clone https://github.com/alphamatrix/alphamatrix.git && cd alphamatrix
   ```

   **Quick Setup:**

- **Windows:** Run `scripts/setup-windows.ps1` as Administrator (interactive credential setup)
- **macOS/Linux:** Run `scripts/setup-unix.sh` (interactive credential setup)

**Manual Setup:** See [SETUP.md](SETUP.md) for detailed database setup instructions

2. **Create a strategy YAML** – e.g. `examples/straddle.yml`.
3. **Run a back‑test**
   ```bash
   curl -X POST localhost:8000/backtests         -d '{"strategy": "straddle", "start": "2023-01-01", "end": "2023-12-31"}'
   ```
4. **Watch progress** – open `http://localhost:3000`; equity curve updates live.
5. **Inspect results** – query ClickHouse:
   ```sql
   SELECT sharpe, max_drawdown
   FROM backtest_runs
   ORDER BY created_ts DESC
   LIMIT 5;
   ```

---

## 7  MVP Strategy — 30‑Day ATM Straddle

| Aspect         | Spec                                                                                         |
| -------------- | -------------------------------------------------------------------------------------------- |
| **Objective**  | Exploit implied‑volatility mispricing by holding delta‑neutral long straddles.               |
| **Universe**   | Top‑100 US equities by average daily option volume (e.g., AAPL, MSFT, TSLA).                 |
| **Legs**       | 1 × Long ATM Call **+** 1 × Long ATM Put, opened 30 calendar days before expiry.             |
| **Entry**      | Each trading day 16:00 ET: select next monthly expiry; choose ATM strike (closest to spot).  |
| **Exit**       | First hit of:  1️⃣ T‑1 (day before expiry)  2️⃣ Loss ≤ ‑50 % premium  3️⃣ Gain ≥ +100 % premium |
| **Risk**       | Max premium per trade = 1 % of portfolio NAV; portfolio max = 10 simultaneous positions.     |
| **Data**       | Daily OHLC spot prices; option chain mid prices & greeks (Δ, Γ, Θ, Vega).                    |
| **Metrics**    | P&L, Sharpe, max drawdown, IV crush %, realised – implied vol spread.                        |
| **Validation** | Unit test: back‑test on AAPL 2023 reproduces reference P&L within ± 1 ¢.                     |

This focused strategy powers our first CLI, API, and UI demos—keeping scope tight while exercising every layer of the stack.

---

## 8  Glossary & Definitions

| Term              | Meaning in AlphaMatrix                                              |
| ----------------- | ------------------------------------------------------------------- |
| **Back‑test run** | A single simulation with fixed parameters and market data slice.    |
| **Strategy YAML** | Declarative file describing option legs, entry/exit criteria, risk. |
| **Greeks**        | Δ, Γ, Θ, Vega calculated per‑leg per‑bar by `core/greeks.cpp`.      |
| **Projection**    | ClickHouse pre‑aggregated table speeding up common queries.         |
| **Alpha Hour**    | Weekly 30‑min community call to sync & share learnings.             |

---

## 9  Contribution Guide (TL;DR)

1. **Pick an issue** – `good first issue` is ideal for new joiners.
2. **Fork & branch** – `git checkout -b feat/<topic>-<initials>`.
3. **Code & test** – `pre-commit run -a`, `pytest`, `ctest`.
4. **Open PR** – include _What I learned_ section; we review on a call if you like.
5. **Merge** – green CI + one maintainer approval.

_Full guidelines live in [`CONTRIBUTING.md`](CONTRIBUTING.md)._

## 10  Disclaimers

1. **Not financial advice**: All information, code, and examples provided in this repository are for demonstration and educational purposes only. They should not be interpreted as investment, trading, or financial advice.
2. **No Ownership of Third-Party Research/Data**: Any referenced market data, research, or external content remains the property of its respective owners. This repository does not claim authorship or rights to such materials.
3. **Educational Use Only**: The code and documentation are intended solely to illustrate technical concepts in quantitative finance and data processing. They are not intended for live trading or commercial deployment without independent review and validation.
4. **Exercise Answers Not Guaranteed Correct**: Any solutions provided to exercises are based on the author’s understanding at the time of writing. They may contain errors and should not be relied upon as authoritative answers without independent verification.

### Core Implementation Code & Architecture
#### File: `python/alphamatrix/etl/tests/__init__.py`
```python
# ETL tests package
```

#### File: `python/alphamatrix/api/tests/__init__.py`
```python
# API tests package
```

#### File: `python/alphamatrix/api/models/__init__.py`
```python
# API models package
```

#### File: `python/alphamatrix/api/routers/__init__.py`
```python
# API routers package
```

#### File: `python/alphamatrix/etl/__init__.py`
```python
# AlphaMatrix ETL Package
```

#### File: `python/alphamatrix/etl/jobs/__init__.py`
```python
# ETL job runners package
```


==================================================
