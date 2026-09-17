# ⚡ [QUANT-SOURCE-181] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_181_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Order-Flow-Imbalances-OFI (`WHEEL_Order-Flow-Imbalances-OFI`)
- **Full Name**: `Order-Flow-Imbalances-OFI`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Comprehensive Architectural Blueprint & Signal Pipeline
- **Role in Quantitative Pipeline**: High-performance execution, signal feature extraction, risk parity constraint management, and microsecond DMA order dispatch.
- **Key Algorithmic Concepts**:
  - `OrderBookDelta`: Vectorized representation of bid-ask level shifts across top-5 depth.
  - `OrderFlowImbalance (OFI)`: Imbalance metrics tracking net buyer vs seller market aggression.
  - `VarianceShield`: 3-Gate pre-trade limiters evaluating max notional, price bands, and deterministic deduplication.
- **Production Integration Hook**:
  - Broker DMA: DhanHQ REST / WebSocket protocol with auto-reconnect and sequence gap tracking.
  - Risk Governor: SEBI 2026 Order-to-Trade Ratio limiter maintaining OTR <= 1.0.


==================================================


## [2/3] Repository: OrderFlowImbalance (`WHEEL_OrderFlowImbalance`)
- **Full Name**: `OrderFlowImbalance`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Core Implementation Code & Architecture
#### File: `engine/__init__.py`
```python

```

#### File: `debug/debug_strategy.py`
```python

```

#### File: `main.py`
```python
# main.py

from engine.start import run_pipeline

if __name__ == "__main__":
    run_pipeline()
```

#### File: `engine/data_loader.py`
```python
import pandas as pd

def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    return df
```

#### File: `engine/utils.py`
```python
# engine/utils.py
import os

def get_project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_data_path(*subdirs):
    return os.path.join(get_project_root(), "data", *subdirs)
```

#### File: `engine/model_builder.py`
```python
#engine/model_builder.py

from sklearn.linear_model import LinearRegression
import pandas as pd

def fit_linear_model(X, y):
    X = X.dropna()
    y = y.loc[X.index]
    model = LinearRegression().fit(X, y)
    coefs = pd.Series(model.coef_, index=X.columns)
    return model, coefs
```


==================================================


## [3/3] Repository: OrderFlowImbalanceAnalysis (`WHEEL_OrderFlowImbalanceAnalysis`)
- **Full Name**: `OrderFlowImbalanceAnalysis`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Comprehensive Architectural Blueprint & Signal Pipeline
- **Role in Quantitative Pipeline**: High-performance execution, signal feature extraction, risk parity constraint management, and microsecond DMA order dispatch.
- **Key Algorithmic Concepts**:
  - `OrderBookDelta`: Vectorized representation of bid-ask level shifts across top-5 depth.
  - `OrderFlowImbalance (OFI)`: Imbalance metrics tracking net buyer vs seller market aggression.
  - `VarianceShield`: 3-Gate pre-trade limiters evaluating max notional, price bands, and deterministic deduplication.
- **Production Integration Hook**:
  - Broker DMA: DhanHQ REST / WebSocket protocol with auto-reconnect and sequence gap tracking.
  - Risk Governor: SEBI 2026 Order-to-Trade Ratio limiter maintaining OTR <= 1.0.


==================================================
