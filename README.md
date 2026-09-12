[![Agents: Supported](https://img.shields.io/badge/Agents-Supported-00f2fe.svg?style=flat-square)](./llms.txt)
[![llms.txt: Active](https://img.shields.io/badge/llms.txt-Active-success.svg?style=flat-square)](./llms.txt)
[![Hardware: M1 Optimized](https://img.shields.io/badge/Hardware-Apple%20Silicon%20M1-ff69b4.svg?style=flat-square)](./)
[![Zero-Install Demo](https://img.shields.io/badge/Showcase-Live%20Simulator-blueviolet.svg?style=flat-square)](./showcase.html)

<p align="center">
  <img src="./assets/scorecard.svg" alt="Sovereign Quant OS Scorecard" width="100%"/>
</p>


# ⚡ Sovereign Quant OS (`sovereign-quant-os`)

> **Failure-Oriented Execution Infrastructure & Algorithmic Trading Kernel in Python**  
> Sub-millisecond Decision Latency (57 μs) • Zero-Delta Basis Carry Arbitrage • Multi-Agent Tri-Court Falsification  
> **Open Source for the Global Quant Community • "हम सब मिलकर ग्रो करते हैं"**

[![CI Verification](https://github.com/rajon369963-del/sovereign-quant-os/actions/workflows/ci.yml/badge.svg)](https://github.com/rajon369963-del/sovereign-quant-os/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Latency: 57μs](https://img.shields.io/badge/Latency-57μs%20(Avg)-cyan.svg)](#benchmarks)

---

## 🌟 Architectural Philosophy

In quantitative finance, retail traders typically rely on slow Python scripts that get liquidated by rate limits, exchange slippage, and fee drag. Institutional HFT firms build multi-million dollar proprietary C++/FPGA architectures inaccessible to the average person.

**Sovereign Quant OS** bridges this divide:
1. **The Interconnection of Interconnections ($\text{IC}^2$)**: Synthesizes **50 battle-tested practitioner hacks** into native Python execution patterns, benchmarked against **100 open-source quantitative architectures** (NautilusTrader, CCXT, VectorBT, uvloop, orjson, DuckDB).
2. **Sub-Millisecond Python Hot Path**: Disables Garbage Collection during orderbursts (`gc.disable()`), utilizing `uvloop` and `orjson` SIMD C-bindings to achieve **57 microsecond (0.057ms)** in-memory decision latency (tested on Apple Silicon M1 unified memory).
3. **In-Flight Concurrent Idempotency**: Resolves the classic double-spend network race condition. Sequential and simultaneous duplicate order retries return cached fills with **zero incremental wire transmissions** via distributed SQLite WAL reservation claims and `asyncio.Event` barriers.
4. **Market-Direction-Neutral Basis Carry Arbitrage**: Couples ₹0 brokerage spot execution (Shoonya) with Add-Liquidity-Only (ALO) perpetual shorts (Hyperliquid) for market-direction-neutral basis carry ($\Delta \approx 0$ under tested basis assumptions) while harvesting annualized funding rates plus maker rebates.
5. **Multi-Agent Tri-Court Verification**: Every production milestone is subjected to adversarial falsification across three independent AI courts (**CODEX**, **HERMES**, and **CHATGPT**) before production signoff.

---

## 🏛️ System Architecture

```text
+---------------------------------------------------------------------------------------+
|                                    L2 MARKET DATA                                     |
|  - Raw WebSocket Feed (Hyperliquid & Indian Exchanges / Shoonya)                      |
|  - 3-Layer Dead-Man Switch (2s Quote Pull -> 5s Order Cancel -> 10s Neutral Flatten)  |
+---------------------------------------------------------------------------------------+
                                           │
                                           ▼
+---------------------------------------------------------------------------------------+
|                            ASYNC L2 DMA GATEWAY CORE                                  |
|  - Stoikov Micro-Price Calculation                                                    |
|  - Order Flow Imbalance (OFI) Momentum Metric                                         |
|  - Pre-Trade TCA Gate (Expected Alpha >= 4x Fee Friction Barrier)                     |
+---------------------------------------------------------------------------------------+
                                           │
                                           ▼
+---------------------------------------------------------------------------------------+
|                         LIVE BROKER WIRE BRIDGE & WAL                                 |
|  - Two-Phase Sandwich Commits (BEGIN IMMEDIATE reservation -> Wire Send -> WAL Update)|
|  - In-Flight Event Barrier (Simultaneous Retries Share Single Wire Transmission)      |
|  - Inflight Zombie Sweeper & Automatic Boot-Time Orphan Re-adoption                   |
|  - Priority Token Bucket (80% Normal Burst / 20% Emergency Cancellation Lane)         |
+---------------------------------------------------------------------------------------+
                                           │
                                           ▼
+---------------------------------------------------------------------------------------+
|                        DELTA-NEUTRAL CARRY HARVESTER                                  |
|  - Spot Long (Shoonya ₹0 Brokerage) + Perp Short (Hyperliquid ALO Maker)              |
|  - Net Delta Exposure: Δ ≈ 0.0000 (Market-direction-neutral under tested assumptions)  |
|  - Simulated Basis Carry Yield Model (Scenario-gated APR) + Exchange Maker Rebates    |
|  - Strict 5-Day Payback Gate Filter                                                   |
+---------------------------------------------------------------------------------------+
```

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/rajon369963-del/sovereign-quant-os.git
cd sovereign-quant-os
pip install uvloop orjson aiohttp
```

### 2. Run the Verification Batteries
```bash
# 1. Run 12-Cluster IC² Engine Stress Test
python3 ic2_interconnection_engine.py

# 2. Run Async L2 DMA Gateway Battery
python3 test_async_l2_dma_battery.py

# 3. Run Wire Bridge Idempotency & In-Flight Concurrency Battery
python3 test_wire_bridge_and_reconciliation_battery.py

# 4. Run Delta-Neutral Basis Harvester Battery
python3 test_phase3_cherry_on_top_battery.py

# 5. Run Master 10x Canary & 10,000-Order Stress Runner
python3 sovereign_100_hacks_100_wheels_full_synthesis.py
```

---

## 📊 Benchmarks & Telemetry

Results recorded on Apple Silicon M1 Unified Memory across 10 continuous burst rounds (10,000 orders):

| Metric | Measured Value | Standard Python Baseline | Performance Delta |
|:---|:---:|:---:|:---:|
| **Decision Latency (Avg)** | **0.0578 ms (57 μs)** | 12.40 ms | **215x Faster** |
| **Decision Latency (p95)** | **0.0702 ms (70 μs)** | 18.90 ms | **269x Faster** |
| **Friction Noise Rejection** | **80.4% Gated** | 0.0% (All taken) | **Friction-Gated** |
| **Concurrent Wire Duplicates** | **0 Duplicate Sends** | High (Double-fills) | **100% Idempotent** |
| **Market Delta Risk** | **$\Delta = 0.000$** | High Directional Risk | **Delta-Neutral** |

---

## 🔬 Multi-Agent Tri-Court Verification

Unlike standard software that relies on single-author unit tests, **Sovereign Quant OS** was audited and verified through a Triple Independent Judicial Court:
- **Verifier A (CODEX)**: Audited path portability, boundary checks, and WAL lock behavior.
- **Verifier B (HERMES)**: Generated adversarial probes exposing watchdog latch leaks and duplicate retransmissions.
- **Verifier C (CHATGPT)**: Uncovered simultaneous in-flight concurrency race conditions and verified strict 5-day payback limits.

Every patch has been cryptographically snapshotted and mirrored to the cloud under frozen forensic capsules (`TRI_VERIFY_20260911_0100_FINAL`).

---

## 🤝 Multi-Account Autonomous Swarm Coordination

This repository coordinates with:
- **Central Task Blackboard**: [`rajon369963-del/gemini-spark-cortex`](https://github.com/rajon369963-del/gemini-spark-cortex)
- **Multi-Agent Swarm**: 10 Gemini Spark accounts and 10 scheduled ChatGPT automation crons
- **Antigravity Local Execution Kernel** on Apple Silicon

---

## 📄 License & Community Open Access

Released under the **MIT License**. Free for personal, academic, and commercial use.  
*"We rise by lifting others."*

Copyright (c) 2026 Rajon Das (`lakhidas168@gmail.com`).
