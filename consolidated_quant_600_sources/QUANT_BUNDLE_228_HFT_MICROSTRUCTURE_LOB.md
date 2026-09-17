# ⚡ [QUANT-SOURCE-228] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 1
**Generated**: QUANT_BUNDLE_228_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/1] Repository: tradingview-mcp (`DISC-717`)
- **Full Name**: `atilaahmettaner/tradingview-mcp`
- **Description**: TradingView MCP server — real-time market data, technical analysis, screeners & backtesting for Claude, ChatGPT, Cursor & any MCP client. Stocks, crypto, forex & futures across global exchanges. Hosted or self-host.
- **GitHub Stars**: 4541
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
