# System Patterns & Architectural Principles

## 1. Zero-Allocation Streaming
Use Polars LazyFrames (`scan_parquet`) and DuckDB queries to process gigabyte tick datasets without loading raw uncompressed arrays into memory. Prevents 8GB RAM crashes.

## 2. Pre-Trade Gate Pattern
Never send an order to the execution engine without passing through the 3-layer `trading-risk-gate`:
- Gate 1: P(Ruin) check.
- Gate 2: Ergodicity / Survival probability check.
- Gate 3: Win-rate / Risk-reward dominance check.

## 3. Self-Healing Try/Catch Pattern
Wrap all network I/O, WebSocket streams, and order dispatch routines in an exponential backoff retry loop with automatic error diagnostics.

## 4. Hardwired Circuit Breaker Pattern
If cumulative daily drawdown exceeds 2%, or account loss hits ₹10,000, trigger immediate process shutdown and cancel all pending orders.
