# ⚡ [QUANT-SOURCE-250] Consolidated Quant & Algo Trading Repositories
**Category**: `STATISTICAL_ARBITRAGE_PAIRS` | **Repositories in this Source**: 1
**Generated**: QUANT_BUNDLE_250_STATISTICAL_ARBITRAGE_PAIRS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/1] Repository: ceres (`DISC-572`)
- **Full Name**: `erdieee/ceres`
- **Description**: Cryptocurrency Arbitrage Bot
- **GitHub Stars**: 33
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
