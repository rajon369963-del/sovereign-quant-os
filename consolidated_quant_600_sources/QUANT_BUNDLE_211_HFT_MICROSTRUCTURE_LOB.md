# ⚡ [QUANT-SOURCE-211] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_211_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: DistributedATS (`PHASE4-QUANT-114`)
- **Full Name**: `PHASE4-QUANT-114_mkipnis__DistributedATS`
- **Description**: DistributedATS is a FIX Protocol based multi matching engine exchange(CLOB) that integrates QuickFIX and LiquiBook over DDS
- **GitHub Stars**: 119
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
## Distributed ATS


DistributedATS is a [**FIX Protocol-based**](https://www.fixtrading.org) alternative trading system that integrates [QuickFIX](https://github.com/quickfix/quickfix) and [LiquiBook](https://github.com/enewhuis/liquibook) over [FastDDS](https://github.com/eProsima/Fast-DDS). This project simplifies the process of communication between multiple FIX gateways and multiple matching engines(CLOB) in real-time. FIX Gateways communicate with clients via FIX and Matching Engines and Middleware(Data Service) components via topic-based DDS IDL Pub/Sub mechanism.

### Components

* [**FIX Gateway**](https://github.com/mkipnis/DistributedATS/tree/master/FIXGateway/src) communicates with clients via FIX and with Matching Engines and Data Services via DDS. FIX Gateway converts FIX messages into DDS IDL and publishes converted IDLs to Matching Engines or Data Services, it converts DDS IDL messages received from Matching Engines and Data Services into FIX and sends them to FIX clients.

* [**Matching Engine**](https://github.com/mkipnis/DistributedATS/tree/master/MatchingEngine/src) maintains order-books, publishes market data(conflated), matches orders, and publishes IDL-based Execution Reports. Matching Engine services critical to the order flow DDS messages including *NewOrderSingle*, *OrderCancelRequest*, *MassOrderCancel*, etc.

* [**Data Service**](https://github.com/mkipnis/DistributedATS/tree/master/DataService/src) authenticates users, provides reference data, services mass order status requests, and market data snapshots. Data Service services all non-critical to order flow DDS messages including *Logon*, *Logout*, *MassOrderStatusRequest*, *MarketDataSnapshot*.  Data Service can service one or more FIX Gateways and Matching Engines.

![N|Solid](https://raw.githubusercontent.com/mkipnis/DistributedATS/master/docs/Diagrams/CryptoCLOB.png?raw=true)



## Examples
### Crypto CLOB/ATS – three matching engines, each handling a subset of instruments.
![Crypto Trader](docs/Diagrams/crypto_trader.gif)

* Users: CRYPTO_TRADER_1, CRYPTO_TRADER_2, CRYPTO_TRADER_3, CRYPTO_TRADER_4 : Password: TEST
* http://localhost:8080/
```
services:
  fast_dds_discovery:
    container_name: fast_dds_discovery 
    image: ghcr.io/mkipnis/distributed_ats:latest
    command: >
      bash -c "LD_LIBRARY_PATH=/usr/local/lib /usr/local/bin/fastdds discovery -q 51000"
    ports:
      - "51000:51000"
    restart: unless-stopped

  distributed_ats:
    container_name: distributed_ats
    image: ghcr.io/mkipnis/dats_crypto_clob:latest
    depends_on:
      - fast_dds_discovery
    command: >
      bash -c "cd /usr/local && source ./dats_env.sh && cd MiscATS && BASEDIR_ATS=`pwd`/CryptoCLOB python3 start_ats.py --ats CryptoCLOB/crypto_ats.json"
    volumes:
      - ./logs_ats:/usr/local/MiscATS/CryptoCLOB/logs
    ports:
      - "15001:15001"
      - "16001:16001"
      - "17001:17001"
    restart: unless-stopped

  fix-ws-proxy:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: fix-ws-proxy
    image: ghcr.io/mkipnis/fix_ws_proxy:latest
    ports:
      - "9002:9002"
    environment:
      LD_LIBRARY_PATH: "/usr/local/lib"
    restart: unless-stopped

  # WebTrader Front-End
  distributed_ats_webtrader:
    container_name: distributed_ats_webtrader
    image: ghcr.io/mkipnis/distributed_ats_webtrader:latest
    volumes:
      - ./webtrader_logs:/var/log/nginx
    ports:
      - "8080:80"
    restart: "no"
```


### US Treasuries CLOB/ATS – one matching engine that handles hundreds of instruments.
![UST Trader](docs/Diagrams/ust_trader.gif)
* Users: UST_TRADER_1, UST_TRADER_2, UST_TRADER_3, UST_TRADER_4 : Password: TEST
* http://localhost:8080/
```
version: '2'

services:
  fast_dds_discovery:
    container_name: discovery_service
    image: ghcr.io/mkipnis/distributed_ats:latest
    command: >
      bash -c "LD_LIBRARY_PATH=/usr/local/lib /usr/local/bin/fastdds discovery -q 51000"
    ports:
      - "51000:51000"
    restart: unless-stopped

  distributed_ats:
    container_name: distributed_ats
    image: ghcr.io/mkipnis/dats_ust_clob:latest 
    depends_on:
      - fast_dds_discovery 
    command: >
      bash -c "cd /usr/local && source ./dats_env.sh && cd MiscATS && BASEDIR_ATS=`pwd`/USTreasuryCLOB python3 start_ats.py --ats USTreasuryCLOB/ust_ats.json"
    volumes:
      - ./logs_ats:/usr/local/MiscATS/USTreasuryCLOB/logs
    ports:
      - "15001:15001"
      - "16001:16001"
    restart: unless-stopped

  fix-ws-proxy:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: fix-ws-proxy
    image: ghcr.io/mkipnis/fix_ws_proxy:latest
    ports:
      - "9002:9002"
    environment:
      LD_LIBRARY_PATH: "/usr/local/lib"
    restart: unless-stopped

  # WebTrader Front-End
  distributed_ats_webtrader:
    container_name: distributed_ats_webtrader
    image: ghcr.io/mkipnis/distributed_ats_webtrader:latest
    volumes:
      - ./webtrader_logs:/var/log/nginx
    ports:
      - "8080:80"
    restart: "no"
```

### Multi Matching Engine ATS, with each component running in a separate container
* [Docker Compose - Multi Matching Engine ATS](docker/docker-compose-multi-matching-engine.yml)
* [Docker Compose - WebTrader](docker/docker-compose-webtrader.yml)


### Dependencies

|Dependency|Component|
|----------|---------|
|[FastDDS](https://github.com/eProsima/Fast-DDS)|[DDS/Middleware](https://www.dds-foundation.org/what-is-dds-3/)|
|[QuickFIX](https://github.com/quickfix/quickfix)|[FIXGateway](https://github.com/mkipnis/DistributedATS/tree/master/FIXGateway)|
|[LiquiBook](https://github.com/enewhuis/liquibook)|[MatchingEngine](https://github.com/mkipnis/DistributedATS/tree/master/MatchingEngine)|
|[SQLite3](https://github.com/sqlite/sqlite)|[DataService](https://github.com/mkipnis/DistributedATS/tree/master/DataService)|


### Sample Exchanges
[MultiMatchingEngineATS](https://github.com/mkipnis/DistributedATS/tree/master/MiscATS/MultiMatchingEngineATS) - Two Matching Engines, three FIX Gateways, and two Data Services. The first matching engine consumes and processes orders from the instrument group MARKET_Y, the second from the instrument MARKET_Z

[USTreasuryCLOB](https://github.com/mkipnis/DistributedATS/tree/master/MiscATS/USTreasuryCLOB) - A single Matching Engine, three FIX Gateways, and two Data Services. The matching engine consumes and processes orders from the instrument group MARKET_UST that covers 300+ instruments (OrderBooks)

[CryptoCLOB](https://github.com/mkipnis/DistributedATS/tree/master/MiscATS/CryptoCLOB) - Three Matching Engines, three FIX Gateways, and two Data Services. The first matching engine consumes and processes orders from the instrument group BTC_MARKET, the second from the instrument ETH_MARKET, and the third from OTHER_COIN_MARKET

### Other Utilities
- [LatencyTest](https://github.com/mkipnis/DistributedATS/tree/master/LatencyTest) - A NewOrderSingle path latency measurement utility. LatencyTest correlates critical to the order flow messages across DistributedATS hops by serving as a FIX and DDS IDL client.
- [SimulatorATS](https://github.com/mkipnis/DistributedATS/tree/master/SimulatorATS) - A random activity simulator that consumes market data, aggress on it with arbitrary quantities, cancels unfilled orders and sends mass cancel requests.

### Sample Clients
- [Python3/QuickFIX](https://github.com/mkipnis/DistributedATS/tree/master/MiscClients/python3)
- [ReactJS and SpringBoot-QuickFIX/J](https://github.com/mkipnis/DistributedATS/tree/master/MiscClients/spring_reactjs)
- [C++/FIX/JSON/ReactJS](https://github.com/mkipnis/DistributedATS/tree/master/MiscClients/cpp_ws_reactjs)
- [Go/Rest](https://github.com/mkipnis/DistributedATS/tree/master/MiscClients/golang_rest_service)

## High Level Data Flow Overview
[Overview](https://github.com/mkipnis/DistributedATS/tree/master/docs/HighLevelDesign.md)

### FIX Messages, Topics, Sources and Destinations

|FIX Message|DDS Topic|Source|Destination|Content Description|
|-----------|---|------|--------------------------|-----------|
|Login(A)|LOGON_TOPIC|FIXGateway|DataService|Converted to IDL FIX Login|
|Login(A)|LOGON_TOPIC|DataService|FIXGateway|Successfully Authenticated FIX Session by a Data Service |
|Logout(5)|LOGOUT_TOPIC|DataService|FIXGateway|Unsuccessfully Authenticate FIX Session by Data Service|
|NewOrderSingle(D)|NEW_ORDER_SINGLE_TOPIC|FIXGateway|MatchingEngine|New order single|
|ExecutionReport(8)|EXECUTION_REPORT_TOPIC|MatchingEngine|FIXGateway|Execution Report to be sent to a client|
|ExecutionReport(8)|EXECUTION_REPORT_TOPIC|MatchingEngine|DataService|Execution Report to be store to service Order Mass Status Requests|
|OrderCancel Request(F)|ORDER_CANCEL_  REQUEST_TOPIC|FIXGateway|MatchingEngine|Converted to IDL Cancel Request from FIX Client|
|OrderCancel Reject(9)|ORDER_CANCEL_REJECT_ TOPIC|MatchingEngine|FIXGateway|IDL Cancel Reject, if order can't be cancelled|
|OrderCancelReplace Request(G)|ORDER_CANCEL_ REPLACE_REQUEST_TOPIC_NAME|FIXGateway|MatchingEngine|Converted to IDL Cancel Replace Request from FIX Client|
|MassCancel Request(q)|ORDER_MASS_CANCEL_ REQUEST_TOPIC|FIXGateway|MatchingEngines|Mass Cancel requested by FIX Client or FIX Client Logout/Disconnect|
|MassCancel Report(r)|ORDER_MASS_CANCEL_ REPORT_TOPIC|MatchingEngines|FIXGateway|Results of Mass Cancel Request|
|MarketData Request(V)|MARKET_DATA_REQUEST _TOPIC|FIXGateway|DataService|Request for the current state of Order Book(Top 5 levels)|
|MarketDataSnapshotFull Refresh(W)|MARKET_DATA_SNAPSHOT _FULL_REFRESH_TOPIC|DataService|FIXGateway|Current Market Data Snapshot(Top 5 levels)|
|MarketDataSnapshotFull Refresh(W)|MARKET_DATA_SNAPSHOT _FULL_REFRESH_TOPIC|Data Service|MatchingEngine|OpeningPrices|
|MarketDataIncremental Refresh(X)|MARKET_DATA_SNAPSHOT _FULL_REFRESH_TOPIC|MatchingEngine|FIXGateway|Incremental Market Data Request(Top 5 levels)|
|MarketDataIncremental Refresh(X)|MARKET_DATA_SNAPSHOT _FULL_REFRESH_TOPIC|MatchingEngine|FIXGateway|Incremental Market Data Request(Top 5 levels)|
|Security ListRequest(x)|SECURITY_LIST_REQUEST _TOPIC|FIXGateway|DataService|FIX Client initiated Security List Request|
|SecurityList(y)|SECURITY_LIST_TOPIC|DataService|FIXGateway|Security list reply for FIX Client Request|
|SecuritList Request(x)|SECURITY_LIST_REQUEST _TOPIC|MatchingEngine|DataService|Security List Request for Order Book setup|
|SecurityList(y)|SECURITY_LIST_TOPIC|DataService|MatchingEngine|Security List for OrderBook Setup|
|OrderMassStatus Request(AF)|ORDER_MASS_STATUS_ REQUEST_TOPIC|FIXGateway|DataService|Initiated by FIX Client Mass Status Request|

### Autogeneration of IDL from QuickFIX XML
[GenTools](https://github.com/mkipnis/DistributedATS/tree/master/GenTools) is a utility that generates DDS IDL, FIX to IDL, and IDL to FIX adapters and IDL logger helper classes from QuickFIX's XML data dictionary.

### Core Implementation Code & Architecture
#### File: `MiscATS/USTreasuryCLOB/ust_ats.json`
```python
[
  ["data_service_manager.py", "data_service_a.ini"],
  ["data_service_manager.py", "data_service_b.ini"],
  ["matching_engine_manager.py", "matching_engine_MARKET_UST.ini"],
  ["fix_gateway_manager.py", "fix_gwy_1.cfg"],
  ["fix_gateway_manager.py", "fix_gwy_2.cfg"]
]
```

#### File: `MiscClients/python3/ExecutionReportAdapter.py`
```python
import quickfix

class ExecutionReportAdapter(object):

    def __init__(self):
        return

    def process_execution_report(self, message):
        order_status_field = quickfix.OrdStatus()
        message.getField(order_status_field)

        return order_status_field
```

#### File: `MiscATS/MultiMatchingEngineATS/multi_matching_engine.json`
```python
[
  ["data_service_manager.py", "data_service_a.ini"],
  ["data_service_manager.py", "data_service_b.ini"],
  ["matching_engine_manager.py", "matching_engine_MARKET_Y.ini"],
  ["matching_engine_manager.py", "matching_engine_MARKET_Z.ini"],
  ["fix_gateway_manager.py", "fix_gwy_1.cfg"],
  ["fix_gateway_manager.py", "fix_gwy_2.cfg"],
  ["fix_gateway_manager.py", "fix_gwy_3.cfg"]
]
```

#### File: `GenTools/idl/HeaderAdapter.hpp`
```python
/* Don't modify, automatically generated file by QuickFIX2FastDDS.py*/
#pragma once
#include "Header.hpp"
#include <quickfix/Message.h>



class HeaderAdapter
{
	public:
		static void FIX2DDS(const FIX::FieldMap&, DistributedATS::Header& ddsMsg )  __attribute__ ((visibility ("default")));
		static void DDS2FIX(const DistributedATS::Header& ddsMsg, FIX::FieldMap&)  __attribute__ ((visibility ("default")));

};
```

#### File: `GenTools/idl/LogonAdapter.hpp`
```python
/* Don't modify, automatically generated file by QuickFIX2FastDDS.py*/
#pragma once
#include "Logon.hpp"
#include <quickfix/Message.h>

#include "HeaderAdapter.hpp"


class LogonAdapter
{
	public:
		static void FIX2DDS(const FIX::Message&, DistributedATS_Logon::Logon& ddsMsg )  __attribute__ ((visibility ("default")));
		static void DDS2FIX(const DistributedATS_Logon::Logon& ddsMsg, FIX::Message&)  __attribute__ ((visibility ("default")));

};
```

#### File: `GenTools/idl/LogoutAdapter.hpp`
```python
/* Don't modify, automatically generated file by QuickFIX2FastDDS.py*/
#pragma once
#include "Logout.hpp"
#include <quickfix/Message.h>

#include "HeaderAdapter.hpp"


class LogoutAdapter
{
	public:
		static void FIX2DDS(const FIX::Message&, DistributedATS_Logout::Logout& ddsMsg )  __attribute__ ((visibility ("default")));
		static void DDS2FIX(const DistributedATS_Logout::Logout& ddsMsg, FIX::Message&)  __attribute__ ((visibility ("default")));

};
```


==================================================


## [2/3] Repository: submicro-execution-engine (`PHASE4-QUANT-115`)
- **Full Name**: `PHASE4-QUANT-115_krish567366__submicro-execution-engine`
- **Description**: Sub-microsecond bare-metal execution engine with deterministic replay, lock-free order path, and hardware-timestamped latency measurement.
- **GitHub Stars**: 103
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║        ███████╗██╗   ██╗██████╗ ███╗   ███╗██╗ ██████╗██████╗  ██████╗        ║
║        ██╔════╝██║   ██║██╔══██╗████╗ ████║██║██╔════╝██╔══██╗██╔═══██╗       ║
║        ███████╗██║   ██║██████╔╝██╔████╔██║██║██║     ██████╔╝██║   ██║       ║
║        ╚════██║██║   ██║██╔══██╗██║╚██╔╝██║██║██║     ██╔══██╗██║   ██║       ║
║        ███████║╚██████╔╝██████╔╝██║ ╚═╝ ██║██║╚██████╗██║  ██║╚██████╔╝       ║
║        ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝        ║
║                                                                               ║
║            Sub-Microsecond Execution Engine for Algorithmic Trading           ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

<h1>Ultra-Low Latency Trading System</h1>

<p>
<b>Deterministic, nanosecond-precise execution engine for quantitative trading research</b>
</p>

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)](.)
[![C++17](https://img.shields.io/badge/C%2B%2B-17-blue?style=for-the-badge&logo=cplusplus)](.)
[![Rust](https://img.shields.io/badge/Rust-1.70%2B-orange?style=for-the-badge&logo=rust)](.)
[![License](https://img.shields.io/badge/license-Proprietary-red?style=for-the-badge)](LICENSE)
[![x86-64 Only](https://img.shields.io/badge/Platform-x86--64-critical?style=for-the-badge&logo=intel)](BUILD_REQUIREMENTS.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](.)

---

## ⚠️ IMPORTANT: Platform Requirements

**This system requires x86-64 architecture (Intel/AMD) with AVX-512 support.**

- ✅ **Linux x86-64**: Full support, < 1μs latency
- ❌ **ARM64/Apple Silicon**: Not supported (missing AVX-512, TSX, RDTSC)
- ❌ **Windows**: Not recommended (need PREEMPT_RT kernel)

**📖 See [BUILD_REQUIREMENTS.md](BUILD_REQUIREMENTS.md) for full details**

---

<p>
<a href="https://submicro.krishnabajpai.me/">Live Demo</a> •
<a href="#key-features">Features</a> •
<a href="#quick-start">Quick Start</a> •
<a href="#benchmarks">Benchmarks</a> •
<a href="#architecture">Architecture</a> •
<a href="#documentation">Docs</a>
</p>

---

### **890ns median latency** | **Deterministic replay** | **Lock-free architecture** | **Research-grade framework**

**[View Interactive Documentation →](https://submicro.krishnabajpai.me/)**

---

> [!TIP]
> **Branching Strategy**:
> *   **`main`**: Fundamental execution infrastructure. Primary focus is **Latency Minimization** (median < 900ns) and system determinism.
> *   **`alpha-optimized`**: Quantitative modeling layer. Primary focus is **Alpha & Signal Optimization** (multi-kernel Hawkes, SIMD features) while keeping latency within sub-microsecond thresholds.

</div>

---

## What Makes This Special?

> **Built for researchers and systems engineers pushing the boundaries of low-latency execution.**

This isn't just another trading bot. It's a **complete infrastructure** for understanding, measuring, and optimizing execution latency at the **hardware level**.

### The Problem
Traditional trading systems are black boxes with unpredictable latency, non-deterministic behavior, and poor visibility into where microseconds are lost.

### The Solution
A **transparent, deterministic execution engine** that:
- Achieves **sub-microsecond decision latency** (890ns median)
- Guarantees **bit-identical replay** for audit and debugging
- Provides **nanosecond-level instrumentation** at every stage
- Uses **zero-allocation hot paths** and lock-free data structures
- Simulates **kernel-bypass networking** (DPDK-style)
- Implements **institutional-grade logging** and monitoring

**Research & Education Only** — Not production-ready. Hardware validation (DPDK/FPGA) is simulated. [Learn more](#hardware-validation--future-work).

**PROPRIETARY LICENSE** — Commercial use prohibited. Written permission required. Contact: krishna@krishnabajpai.me

## Performance Snapshot

<div align="center">

| **Component** | **Median** | **p99** | **p99.9** | 
|------------------|--------------|-----------|--------------|
| Market Data Ingestion | **87 ns** | 124 ns | 201 ns |
| Signal Extraction (SIMD) | **40 ns** | 48 ns | 67 ns |
| Hawkes Update (Power-Law) | **150 ns** | 189 ns | 234 ns |
| **End-to-End Decision** | **890 ns** | **921 ns** | **1047 ns** |
| Order Serialization | **34 ns** | 41 ns | 58 ns |

**Measurement Precision:** ±5ns (TSC jitter) | ±17ns (PTP offset)  
**Test Hardware:** Intel Xeon Platinum 8280 @ 2.7GHz, isolated core, RT kernel

</div>

---

## Key Features

<table>
<tr>
<td width="50%">

### **Performance**
- Sub-microsecond decision latency
- Zero-copy data paths
- Lock-free SPSC/MPSC queues
- Cache-aligned data structures
- SIMD-optimized computations (AVX-512)

</td>
<td width="50%">

### **Determinism**
- Bit-identical replay guarantees
- Event-driven scheduling
- Fixed RNG seeds
- Pre-allocated memory pools
- TSC-level timestamp precision

</td>
</tr>
<tr>
<td width="50%">

### **Architecture**
- Kernel-bypass NIC simulation
- Multivariate Hawkes process
- Avellaneda-Stoikov market making
- Adaptive risk management
- C++/Rust FFI integration

</td>
<td width="50%">

### **Observability**
- Real-time metrics dashboard
- Multi-layer audit logging
- SHA-256 replay verification
- Nanosecond-level tracing
- Latency breakdown analysis

</td>
</table>
<br/>

<table>
<tr>
<td colspan="2">

### **New: Jitter Profiler & Stall Detection**
> **"If you can't measure tail latency, you can't fix it."**
A built-in nanosecond-resolution profiler detects **System Management Interrupts (SMIs)** and scheduler preemption by measuring the cycle-gap between busy-wait iterations. This ensures deep visibility into the "Zero-Interruption" guarantee required for p99 latency stability.

</td>
</tr>
</table>

---

## Quick Start

**Get running in 60 seconds:**

```bash
# 1. Clone the repository
git clone https://github.com/krish567366/submicro-execution-engine.git
cd submicro-execution-engine

# 2. Build the system (automatic optimization flags)
./scripts/build_all.sh

# 3. Run deterministic backtest
scripts/run_backtest.py

# 4. View results
python3 scripts/verify_latency.py
open dashboard/index.html  # Interactive metrics dashboard
```

<details>
<summary><b>Expected Output (click to expand)</b></summary>

```
=== Low-Latency Trading System ===
Market data ingestion: 87ns median
Signal extraction: 40ns median  
Hawkes update: 150ns median
Decision latency: 890ns median

--- Cycle: 1000 ---
Mid Price: $100.05
Position: 250
Active Quotes: Bid=100.04 Ask=100.06 Spread=2.00 bps
Hawkes: Buy=12.456 Sell=11.234 Imbalance=0.052
Regime: NORMAL (multiplier=1.0)
Last Cycle Latency: 847 ns (0.847 µs)
Determinism verified: SHA-256 match
```

</details>

---

## Architecture Overview

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Market Data Feed (Simulated)                         │
│                    Kernel-Bypass NIC • Zero-Copy DMA Transfer                │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │ 87ns median
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Lock-Free Ring Buffer (SPSC)                              │
│              Power-of-2 Size • Cache-Line Aligned • No Allocations           │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │ O(1) operations
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                   Order Book Reconstruction                                  │
│            Price-Level Aggregation • L2 Depth Tracking                       │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │
                ┌───────────────┴───────────────┐
                ▼                               ▼
┌─────────────────────────────┐   ┌─────────────────────────────────────────┐
│   Hawkes Process Engine     │   │  Microstructure Features                │
│   • Self/Cross Excitation   │   │  • Deep OFI (10 levels)                │
│   • Power-Law Kernel        │   │  • Order Book Imbalance                │
│   • Buy/Sell Intensity      │   │  • Flow Toxicity (Kyle λ)              │
└──────────────┬──────────────┘   └──────────────┬──────────────────────────┘
               │  150ns median                   │ 40ns (SIMD)
               └───────────────┬─────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                  FPGA DNN Inference (Simulated)                              │
│              12 Features → 8 Hidden → 3 Outputs • 400ns Fixed                │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│              Avellaneda-Stoikov Market Making Strategy                       │
│        HJB Equation • Inventory Skew • Latency-Aware Pricing                 │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │ 890ns E2E
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Risk Control (Pre-Trade + Kill-Switch)                    │
│          Position Limits • Regime Detection • Atomic Checks                  │
└───────────────────────────────┬─────────────────────────────────────────────┘
                                │ 34ns serialization
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Order Submission                                       │
│                  Pre-Serialized Orders • Zero Copy                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

</div>

> **See [`ARCHITECTURE.md`](ARCHITECTURE.md) for detailed component documentation**

---

## Determinism & Reproducibility

One of the system's **core guarantees** is bit-identical replay capability:

**Fixed RNG seeds** — Deterministic random number generation  
**Event-driven scheduling** — No wall-clock dependencies  
**Pre-allocated memory** — No allocator non-determinism  
**Timestamp-ordered events** — Consistent processing order  

### Verification

```bash
# Run backtest
scripts/run_backtest.py

# Verify deterministic replay
cd logs
sha256sum -c MANIFEST.sha256
strategy_trace.log: OK
order_flow.log: OK
latency_metrics.log: OK
```

---

## Complete Documentation

| Document | Description |
|----------|-------------|
| [`ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Order path, cache layout, thread model |
| [`BENCHMARK_GUIDE.md`](docs/BENCHMARK_GUIDE.md) | Latency measurement methodology |
| [`LATENCY_BUDGET.md`](docs/LATENCY_BUDGET.md) | Component-level breakdown |
| [`INSTITUTIONAL_LOGGING_COMPARISON.md`](docs/INSTITUTIONAL_LOGGING_COMPARISON.md) | Audit-grade logging |
| [`PRODUCTION_READINESS.md`](docs/PRODUCTION_READINESS.md) | Deployment considerations |
| [`ENGAGEMENTS.md`](docs/ENGAGEMENTS.md) | Commercial & Research support |
| [`logs/README.md`](logs/README.md) | Multi-layer timestamp verification |

---

## Contributing

We welcome contributions! Here's how to get started:

<details>
<summary><b>Report a Bug</b></summary>

Open an issue with:
- System configuration (CPU, OS, compiler)
- Reproducible example
- Expected vs actual behavior
- Relevant logs

</details>

<details>
<summary><b>Propose a Feature</b></summary>

1. Check existing issues/PRs
2. Open an issue describing the feature
3. Discuss implementation approach
4. Submit a PR with tests

</details>

<details>
<summary><b>Submit a Pull Request</b></summary>

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with tests
4. Ensure `ctest` and `cargo test` pass
5. Commit with clear messages
6. Push and open a PR

</details>

### Development Guidelines

- **Code style:** Follow existing patterns (run `clang-format`)
- **Tests:** Add tests for new features
- **Benchmarks:** Measure latency impact
- **Documentation:** Update relevant markdown files

---

## 🌟 Star History

## Star History

<a href="https://www.star-history.com/#krish567366/submicro-execution-engine&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=krish567366/submicro-execution-engine&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=krish567366/submicro-execution-engine&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=krish567366/submicro-execution-engine&type=date&legend=top-left" />
 </picture>
</a>

---

## Commercial & Research Engagements

This repository serves as a framework for research and evaluation. For institutional requirements requiring production-grade performance or custom research collaborations, we offer several engagement models:

-   **Institutional Implementation**: Custom DPDK/RDMA kernel-bypass and FPGA HLS/RTL acceleration.
-   **Performance Engineering**: Architecture reviews, latency bottleneck audits, and system tuning.
-   **Research Collaboration**: Market microstructure modeling and low-latency ML inference.
-   **Strategy Optimization**: Migration of Python/Julia models to AVX-512 optimized C++.

See [**`ENGAGEMENTS.md`**](docs/ENGAGEMENTS.md) for more details.

**Contact:** [krishna@krishnabajpai.me](mailto:krishna@krishnabajpai.me)

*Notice: Pricing is not disclosed publicly. All engagements are scoped and quoted based on project complexity and hardware requirements.*

### Kernel-bypass NICs

True kernel bypass depends on:
- **Specific NIC hardware** (NVIDIA/Mellanox, Intel, Solarflare/Xilinx, FPGA NICs)
- **Driver stacks** (DPDK, RDMA verbs, Onload, custom DMA paths)
- **NIC firmware** and queue configuration

There is no realistic way to ship a single, generic kernel-bypass implementation that works across all vendors and drivers. The only viable approach is to define a clean abstraction and allow users to plug in vendor-specific implementations.

### FPGA Inference

The same constraint applies to FPGA-based inference:
- **FPGA implementations** depend on the exact FPGA model, vendor toolchain (Xilinx Vitis/Vivado, Intel Quartus), and PCIe/DMA configuration.
- **The inference pipeline** (HLS, RTL, data layout, batching, clocking) is tightly coupled to the target hardware.
- **Bitstreams** are not portable across vendors or across FPGA families.

In this repository:
- FPGA inference is represented as an architectural interface / placeholder.
- Software emulation is used where hardware is not available.
- For specific hardware targets, custom HLS/RTL integration can be implemented.

---

## 📖 Academic References

<details>
<summary><b>Click to expand bibliography</b></summary>

### Hawkes Processes
1. **Hawkes, A. G. (1971).** "Specular Point Processes" *Biometrika*
2. **Bacry, E., et al. (2015).** "Hawkes Processes in Finance" *Market Microstructure and Liquidity*

### Market Making
3. **Avellaneda, M., & Stoikov, S. (2008).** "High-frequency trading in a limit order book" *Quantitative Finance*
4. **Guéant, O., et al. (2013).** "Dealing with the inventory risk" *Mathematics and Financial Economics*

### Market Microstructure
5. **Cartea, Á., et al. (2015).** "Algorithmic and High-Frequency Trading" *Cambridge University Press*
6. **Lehalle, C.-A., & Laruelle, S. (2018).** "Market Microstructure in Practice" *World Scientific*
7. **Easley, D., et al. (2012).** "Flow Toxicity and Liquidity in a High-Frequency World" *Review of Financial Studies*

### System Design
8. **Nygren, E. (2015).** "Linux Kernel Development for Real-Time Systems" *O'Reilly*
9. **Gregg, B. (2013).** "Systems Performance: Enterprise and the Cloud" *Prentice Hall*

</details>

---

## Important Disclaimers

<div align="center">

### **RESEARCH & EDUCATION ONLY**

</div>

This system is **NOT**:
- Production-ready trading software
- Connected to any exchanges
- Financial advice or recommendation
- Guaranteed to be profitable

This system **IS**:
- A research framework
- An educational tool
- A latency benchmarking platform
- A deterministic execution skeleton

**Real production HFT requires:**
- Hardware FPGA acceleration (Xilinx, Altera)
- True kernel-bypass (DPDK, Solarflare OpenOnload)
- Exchange connectivity (FIX, proprietary protocols)
- Compliance systems (kill-switches, position limits)
- Risk management infrastructure
- Extensive testing and regulatory approval
- **Vendor-specific hardware integration** (DPDK/FPGA)

**Legal:** No warranty. Use at your own risk. See LICENSE for details.

---

## Contact & Community

<div align="center">

**Questions? Ideas? Collaboration?**

[![GitHub Issues](https://img.shields.io/badge/Issues-Open-blue?style=for-the-badge&logo=github)](https://github.com/krish567366/submicro-execution-engine/issues)
[![Discussions](https://img.shields.io/badge/Discussions-Join-green?style=for-the-badge&logo=github)](https://github.com/krish567366/submicro-execution-engine/discussions)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:krishna@krishnabajpai.me)

</div>

---

## ❤️ Support This Project

If this research and codebase helps with your work, please consider sponsoring:

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-krish567366-ff69b4?style=for-the-badge&logo=github)](https://github.com/sponsors/krish567366)

Your support helps fund:
- **Hardware**: Dedicated access to DPDK-enabled NICs and FPGA accelerator cards for validation
-  **Funding**: Production-grade bitstreams and vendor-specific implementations
-  **Research**: Advanced algorithms and optimization techniques
-  **Documentation**: Comprehensive guides and institutional-grade whitepapers
- **Open Source**: Keeping the core research framework freely available

---

### Related Projects

- [DPDK](https://www.dpdk.org/) — Data Plane Development Kit
- [Solarflare OpenOnload](https://www.xilinx.com/products/design-tools/software-zone/openonload.html) — Kernel-bypass networking
- [Folly](https://github.com/facebook/folly) — Facebook's lock-free structures
- [QuantLib](https://www.quantlib.org/) — Quantitative finance library

---

<div align="center">

## **Built for Speed. Designed for Reliability. Optimized for Discovery.**

### If you find this useful, please star the repository

<sub>Made with care by quantitative systems engineers</sub>

---

**Trading • Low-Latency • Research • Open Source**

</div>

---

## License

**PROPRIETARY LICENSE** - See [LICENSE](LICENSE) file for details

**IMPORTANT:** This software is for academic research and educational purposes only. 
Commercial use is strictly prohibited. Written permission required for any use beyond 
personal learning and non-commercial experimentation.

**To request permission:** Contact krishna@krishnabajpai.me

Copyright (c) 2025 Krishna Bajpai - All Rights Reserved

---

### Core Implementation Code & Architecture
#### File: `web/tsconfig.json`
```python
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
```

#### File: `web/tsconfig.node.json`
```python
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2023",
    "lib": ["ES2023"],
    "module": "ESNext",
    "types": ["node"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}
```

#### File: `web/tsconfig.app.json`
```python
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "types": ["vite/client"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}
```

#### File: `Cargo.toml`
```python
[package]
name = "hft_rust_core"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["staticlib", "cdylib"]  # For FFI with C++

[dependencies]
# No dependencies for zero-overhead, deterministic execution

[profile.release]
opt-level = 3              # Maximum optimization
lto = "fat"                # Link-time optimization
codegen-units = 1          # Better optimization (slower compile)
panic = "abort"            # No unwinding overhead
strip = true               # Strip symbols for smaller binary

[profile.release.build-override]
opt-level = 3

[profile.release.package."*"]
opt-level = 3

# Custom profile for ultra-low latency
[profile.latency]
inherits = "release"
opt-level = 3
lto = "fat"
codegen-units = 1
panic = "abort"
strip = true
overflow-checks = false    # Disable overflow checks in hot path
debug-assertions = false

[features]
default = []
avx2 = []                  # AVX2 SIMD optimizations
hardware_tsc = []          # Use hardware TSC for timing
```

#### File: `include/neuromorphic_core.hpp`
```python
#pragma once

#include "common_types.hpp"
#include <vector>
#include <cmath>

#if defined(__x86_64__) || defined(_M_X64)
    #include <immintrin.h>
#endif

namespace hft {
namespace neuromorphic {

/**
 * Spiking Neural Network Core (Portable)
 */
class SpikingCore {
public:
    static constexpr int N_NEURONS = 256;
    
    SpikingCore() {
        for(int i=0; i<N_NEURONS; ++i) {
            voltage_[i] = 0.0f; threshold_[i] = 1.0f; decay_[i] = 0.95f; 
        }
    }

    inline void input_current(const float* currents, uint64_t* fire_mask) {
#if defined(__AVX512F__)
        // ... (SIMD path)
#endif
        uint64_t mask = 0;
        for (int i = 0; i < N_NEURONS; ++i) {
            voltage_[i] = (voltage_[i] * decay_[i]) + currents[i];
            if (voltage_[i] > threshold_[i]) {
                voltage_[i] = 0.0f;
                if (i < 64) mask |= (1ULL << i);
            }
        }
        if (fire_mask) *fire_mask = mask;
    }

private:
    float voltage_[N_NEURONS], threshold_[N_NEURONS], decay_[N_NEURONS];
};

} }
```

#### File: `web/package.json`
```python
{
  "name": "web",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@types/react-syntax-highlighter": "^15.5.13",
    "framer-motion": "^12.23.26",
    "lucide-react": "^0.561.0",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-syntax-highlighter": "^16.1.0",
    "recharts": "^3.5.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@tailwindcss/postcss": "^4.1.18",
    "@tailwindcss/typography": "^0.5.19",
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.5",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "autoprefixer": "^10.4.23",
    "eslint": "^9.39.1",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.24",
    "globals": "^16.5.0",
    "postcss": "^8.5.6",
    "tailwindcss": "^4.1.18",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.46.4",
    "vite": "^7.2.4"
  }
}
```


==================================================


## [3/3] Repository: open-outcry (`PHASE4-QUANT-117`)
- **Full Name**: `PHASE4-QUANT-117_tolyo__open-outcry`
- **Description**: A multi-asset matching engine for market places of all sizes
- **GitHub Stars**: 74
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
![Build status](https://github.com/tolyo/open-outcry/actions/workflows/ci.yml/badge.svg)

<p align="center">
  <a target="_blank" rel="noopener noreferrer">
    <img src="https://raw.githubusercontent.com/tolyo/open-outcry/main/market.jpg" width="400">
  </a>
</p>

# Open Outcry

Open Outcry is a multi-asset [matching and trading engine](https://en.wikipedia.org/wiki/Order_matching_system) for market places of all sizes. Written in [Golang](https://go.dev/) and [PL/pgSQL](https://www.postgresql.org/docs/14/plpgsql.html)
it can be used any context requiring an exchange of assets between two or more parties, including small electronic exchanges, crypto-exchages, currency brokers or trading simulators.

## Rationale

There are plenty of [available](https://github.com/Laffini/Java-Matching-Engine)
[open](https://github.com/enewhuis/liquibook) [source](https://www.opensourceagenda.com/projects/exchange-core) matching engines that are based around a variation of [same data structure](https://link.springer.com/chapter/10.1007/978-1-4302-0147-2_2), consisting of a [TreeMap](https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html) with keys for prices and a [Queue](https://docs.oracle.com/javase/7/docs/api/java/util/Queue.html) of orders for values. These solutions put microsecond performance at the forefront of their productivity, leaving open [the non-trivial management](https://martinfowler.com/articles/lmax.html#KeepingItAllInMemory) of this in-memory data structure up to greater application. This approach may make sense in the context of liquidity pools and large securities exchanges where participants are given priority access to the order book through [DMAs](https://www.investopedia.com/terms/d/directmarketaccess.asp). In the context of a small crypto-exchange, however, where every order must be validated against an account balance held in a traditional RDBMS, this achitecture provides questionable benefits as the order processing capacity will never exceed that of the database.
Futhermore, this architecture can actually harm an active trader because a matching engine, burdened by a multi-step process of syncing and validating all of its moving parts, must necessarily freeze funds during settlement while the market moves away from the price of the executed trade. A true performance of a matching engine must measure the entire trading cycle of funds allocation between users' accounts.
These problems are fundamental, to say nothing of technical ones like: How do we ensure ACID properties of trading transactions? How do we ensure zero-downtime? Hot-code upgrades? How do we scale for unknown number of clients, connected to our trading system?

## Solution

Open Outcry puts performance and correctness of the entire trading cycle as its priority. It minimizes the number
of moving parts by putting all the trading logic into optimized PostreSQL procedures. Clients are ensured stable,
scalable and fault-tolerant access to the database through a cloud-native server, which listens to events from the database propagated to an Kubernetes cluster. This approach allows trading and settlement to be processed by a single transactional database call with event notifications delivered directly to a client without resorting to routing via a message broker.

Open Outcry's reliance on SQL also means that it can focus on business logic to provide the most feature-complete, tested and accurate trading engine, capable of evolving along with future developments in financial technology. These include marging trading, short orders, futures and options, pro-rata amongst many allocation algorithms, and hop-trades (cross-matching) where more than two parties accross several instruments are involved.

## Current features

- Time/price priority allocation
- Regular and fiat instruments
- Market and limit orders
- Stop loss and stop limit orders
- GTC, FOK, IOK, GTD, GTT orders
- Trading and payment accounts
- Self-trade prevention
- Configurable fees for deposits, withdrawals, transfers and trading

## Planned features

- Peg orders
- Configurable fees
- REST API
- Websocket and FIX client connection
- Margin trading accounts
- Short orders`
- Futures and options
- Pro-rata allocation
- Multi-instrument matching

## Contributions welcome

### Core Implementation Code & Architecture
#### File: `openapitools.json`
```python
{
  "$schema": "./node_modules/@openapitools/openapi-generator-cli/config.schema.json",
  "spaces": 2,
  "generator-cli": {
    "version": "7.1.0"
  }
}
```

#### File: `api/package.json`
```python
{
    "private": true,
    "scripts": {},
    "devDependencies": {
        "@openapitools/openapi-generator-cli": "latest",
        "@redocly/cli": "latest"
    }
}
```

#### File: `demo/package.json`
```python
{
  "name": "angular-seed",
  "version": "0.0.1",
  "description": "A starter template for AngularTS app",
  "main": "index.js",
  "scripts": {
    "serve": "web-dev-server --watch",
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "rollup -c",
    "prepare": "husky"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Angular-Wave/angular-seed.git"
  },
  "keywords": [
    "AngularJS",
    "AngularTS",
    "Angular seed"
  ],
  "author": "Anatoly Ostrovsky",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/Angular-Wave/angular-seed/issues"
  },
  "homepage": "https://github.com/Angular-Wave/angular-seed#readme",
  "dependencies": {
    "@angular-wave/angular.ts": "latest",
    "modern-normalize": "latest"
  },
  "devDependencies": {
    "@rollup/plugin-commonjs": "latest",
    "@rollup/plugin-terser": "latest",
    "@web/dev-server": "latest",
    "@web/rollup-plugin-copy": "latest",
    "@web/rollup-plugin-html": "latest",
    "husky": "latest",
    "lightningcss": "latest",
    "lint-staged": "latest",
    "prettier": "latest",
    "rollup": "latest"
  },
  "lint-staged": {
    "**/*": "prettier --write --ignore-unknown"
  }
}
```


==================================================
