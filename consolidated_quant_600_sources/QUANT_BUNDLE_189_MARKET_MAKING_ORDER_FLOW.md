# ⚡ [QUANT-SOURCE-189] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_189_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: trading-assistant (`DISC-584`)
- **Full Name**: `WilliamYi951208/trading-assistant`
- **Description**: Intraday gold-futures trading assistant — Al Brooks Price Action + SMC + Order Flow + Volume Profile. Auto-ingests live bars via TradingView webhook or an ATAS order-flow indicator, then emits structured trade calls. Ships as a plug-and-play Agent Skill for Claude Code / Codex / OpenClaw.
- **GitHub Stars**: 21
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


## [2/3] Repository: OrderFlow-Scalper (`DISC-586`)
- **Full Name**: `mahmoud20138/OrderFlow-Scalper`
- **Description**: 3-thread order flow scalper for MT5 — footprint charts, delta analysis, key levels, auto-execution.
- **GitHub Stars**: 14
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


## [3/3] Repository: flowdepth (`DISC-592`)
- **Full Name**: `Niketion/flowdepth`
- **Description**: A native desktop charting platform for crypto markets
- **GitHub Stars**: 7
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
