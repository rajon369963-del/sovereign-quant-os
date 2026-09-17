# ⚡ [QUANT-SOURCE-188] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_188_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: OrderFlow-Analysis-Pro (`DISC-579`)
- **Full Name**: `mahmoud20138/OrderFlow-Analysis-Pro`
- **Description**: Order flow analysis with Bybit + MT5 feeds -- footprint charts, delta analytics, volume profile, pattern detection, Dash dashboard with WebSocket
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


## [2/3] Repository: Quant-Edge-Indicators (`DISC-580`)
- **Full Name**: `Ahmed-GoCode/Quant-Edge-Indicators`
- **Description**: ⚡ A professional open-source algorithmic trading suite for TradingView. Features 16 Pine Script v6 strategies covering Smart Money Concepts (SMC), Order Flow, Momentum, and Trend Breakouts.
- **GitHub Stars**: 47
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


## [3/3] Repository: Pulse (`DISC-581`)
- **Full Name**: `PulseRobinhood/Pulse`
- **Description**: Short-horizon Solana order-flow pulse engine for finding moves with growing buying pressure and usable liquidity.
- **GitHub Stars**: 23
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
