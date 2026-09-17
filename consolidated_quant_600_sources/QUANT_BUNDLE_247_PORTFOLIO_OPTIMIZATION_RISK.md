# ⚡ [QUANT-SOURCE-247] Consolidated Quant & Algo Trading Repositories
**Category**: `PORTFOLIO_OPTIMIZATION_RISK` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_247_PORTFOLIO_OPTIMIZATION_RISK.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Python_Portfolio__VaR_Tool (`DISC-708`)
- **Full Name**: `MBKraus/Python_Portfolio__VaR_Tool`
- **Description**: Python-based portfolio / stock widget which sources data from Yahoo Finance and calculates different types of Value-at-Risk (VaR) metrics and many other (ex-post) risk/return characteristics both on an individual stock and portfolio-basis, stand-alone and vs. a benchmark of choice (constructed with wxPython)
- **GitHub Stars**: 124
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


## [2/3] Repository: mt5_live_trading_bot (`DISC-710`)
- **Full Name**: `ilahuerta-IA/mt5_live_trading_bot`
- **Description**: Professional real-time trading strategy monitor for MetaTrader 5 with advanced GUI and comprehensive risk management
- **GitHub Stars**: 87
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


## [3/3] Repository: riskguard (`DISC-714`)
- **Full Name**: `SilentFleetKK/riskguard`
- **Description**: 开源交易风控层:仓位上限 · 回撤熔断 · 动态仓位(Kelly/波动率) · 防篡改审计 · 实时监控守护。补上量化五层积木唯一缺的一层,核心零依赖。
- **GitHub Stars**: 65
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
