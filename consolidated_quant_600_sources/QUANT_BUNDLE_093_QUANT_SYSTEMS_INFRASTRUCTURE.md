# ⚡ [QUANT-SOURCE-093] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_093_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: tumbleweed_gdax (`DISC-567`)
- **Full Name**: `AlbatrossAutomated/tumbleweed_gdax`
- **Description**: Prototype market maker specialized to trade on CoinbasePro
- **GitHub Stars**: 50
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


## [2/3] Repository: blue_collar_gdax (`DISC-574`)
- **Full Name**: `AlbatrossAutomated/blue_collar_gdax`
- **Description**: Prototype market maker specialized to trade on CoinbasePro
- **GitHub Stars**: 24
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


## [3/3] Repository: volume-anomaly (`DISC-591`)
- **Full Name**: `tripolskypetr/volume-anomaly`
- **Description**: Statistical volume anomaly detection for trade streams - Hawkes process, CUSUM, and Bayesian Online Changepoint Detection (BOCPD). Zero dependencies. TypeScript.
- **GitHub Stars**: 9
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
