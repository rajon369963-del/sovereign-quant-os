# ⚡ [QUANT-SOURCE-200] Consolidated Quant & Algo Trading Repositories
**Category**: `EVENT_DRIVEN_BACKTESTERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_200_EVENT_DRIVEN_BACKTESTERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: gym-fx (`DISC-702`)
- **Full Name**: `harveybc/gym-fx`
- **Description**: Gymnasium trading environment for FX and crypto: backtrader execution bridge, protected SL/TP orders, solvency curricula and audit-grade trade diagnostics
- **GitHub Stars**: 209
- **Source Pool**: `more_github_repos.json`

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


## [2/3] Repository: AutoTrader (`DISC-721`)
- **Full Name**: `kieran-mackle/AutoTrader`
- **Description**: A Python-based development platform for automated trading systems - from backtesting to optimisation to livetrading. 
- **GitHub Stars**: 1271
- **Source Pool**: `more_github_repos.json`

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


## [3/3] Repository: algo-trader (`DISC-725`)
- **Full Name**: `idanya/algo-trader`
- **Description**: Trading bot with support for realtime trading, backtesting, custom strategies and much more.
- **GitHub Stars**: 869
- **Source Pool**: `more_github_repos.json`

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
