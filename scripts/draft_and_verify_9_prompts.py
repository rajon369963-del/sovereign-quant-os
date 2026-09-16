import sys

prompts = {}

# ==============================================================================
# Q1: PROBLEM / ROOT CAUSE & SOLUTION LANDSCAPE
# ==============================================================================
prompts["Q1"] = """CONTEXT: Sovereign Algo Trading OS on macOS (M1 arm64, Python/C++) trading Indian markets (NSE/BSE) via DhanHQ and Zerodha Kite. Stack contains 425 cloned repos and multi-broker adapters.
GOAL: Eliminate execution drift and capital loss by establishing a singular execution authority and deterministic order loop.
CURRENT FAILURE: Split-brain architecture where disjoint Python scripts run concurrently, firing unsynchronized orders and contradictory exits. Network retry loops trigger duplicate broker submissions.
ROOT BOTTLENECK: State fragmented across 10+ SQLite files without a single-writer sequencer; APFS POSIX lock clashes (SQLITE_BUSY) corrupt state and drop fill updates.
PENDING TASK: Consolidate scattered trading logic into a unified execution gateway with deterministic SHA-256 idempotency and SEBI 2026 pre-trade variance shields.
RESEARCH OBJECTIVE: Search reverse-chronologically from September 16, 2026 backwards across Reddit (r/algotrading, r/IndiaAlgoTrading), GitHub, X, and quant forums for:
1. Root causes of multi-process execution drift in multi-broker setups.
2. Top 30 advanced architectural hacks to enforce single-authority order dispatch and kill duplicate firing.
3. Top 30 advanced open-source wheels/gateways (NautilusTrader, OpenAlgo, LEAN) for centralized execution.
4. Interconnection² mapping: Synthesize compound capabilities connecting architectural hacks with gateway wheels.
5. Strict metadata (canonical URLs, authors, dates, versions) and failure modes."""

# ==============================================================================
# Q2: PROBLEM / PRACTITIONER & FAILURE INTELLIGENCE
# ==============================================================================
prompts["Q2"] = """CONTEXT: Sovereign Algo Trading OS on macOS (M1 arm64, Python/C++) for Indian markets (NSE/BSE) via DhanHQ and Zerodha. Stack has 425 cloned repos and 8 cortex modules.
GOAL: Implement robust failure detection, broker telemetry, and automated recovery to prevent trading losses.
CURRENT FAILURE: Trading losses from duplicate orders and ghost execution drift. When DhanHQ or Zerodha WebSockets drop (1006 error), reconnect routines lack gap-recovery, causing blind retries and double square-offs.
ROOT BOTTLENECK: Multi-writer SQLite concurrency on APFS causing POSIX lock starvation; lack of client-side idempotency hashing creates duplicate broker orders.
PENDING TASK: Build resilient execution gateway with transactional outbox, client-side idempotency, and full order lifecycle reconciliation.
RESEARCH OBJECTIVE: Reverse-chronological search from September 16, 2026 backwards across Reddit, GitHub Issues, X, and broker developer forums for:
1. Practitioner postmortems of Zerodha Kite HTTP 429 and DhanHQ WebSocket desync.
2. Top 30 failure-derived hacks and operational rules for debugging live execution drift and silent ticker stalls.
3. Top 30 advanced diagnostic, auditing, and telemetry wheels (OpenTelemetry, Vector, DuckDB event tables, Grafana).
4. Interconnection² mapping: Connect diagnostic hacks with telemetry wheels to build an automated drift detector.
5. Full provenance metadata (resolvable URLs, author handles, dates, versions) and counter-evidence."""

# ==============================================================================
# Q3: PROBLEM / ADVANCED READY-MADE WHEELS
# ==============================================================================
prompts["Q3"] = """CONTEXT: Sovereign Quantitative Trading OS on Apple Silicon M1 (macOS arm64, Python/C++) for Indian brokers DhanHQ and Zerodha Kite. Stack includes 425 cloned repos and multi-broker adapters.
GOAL: Replace fragmented trading silos with a production-grade, unified multi-broker execution gateway.
CURRENT FAILURE: Multiple independent scripts access broker APIs directly, causing split-brain state, uncoordinated margin consumption, and capital loss.
ROOT BOTTLENECK: Distributed state fragmentation across multiple SQLite databases without a canonical event store or atomic broker handoff.
PENDING TASK: Consolidate 425 quantitative codebases into a single-authority gateway supporting deterministic variance shielding and SEBI 2026 compliance.
RESEARCH OBJECTIVE: Search reverse-chronologically from September 16, 2026 backwards across GitHub, package registries, Reddit, and engineering blogs for:
1. Production-tested open-source multi-broker execution gateways and OMS engines.
2. Top 30 advanced downloadable wheels and frameworks (NautilusTrader, OpenAlgo, Hummingbot Gateway, CCXT).
3. Top 30 architectural migration hacks to transition fragmented trading scripts into a unified gateway without downtime.
4. Interconnection² synthesis: Formulate compound architectures connecting gateway wheels with modular strategy adapters.
5. Complete provenance metadata (official repo URLs, release tags, dates, licenses) and failure modes."""

# ==============================================================================
# Q4: BOTTLENECK / TECHNICAL MECHANISM
# ==============================================================================
prompts["Q4"] = """CONTEXT: Sovereign Algo Trading OS on macOS M1 (arm64, Python/C++) for Indian markets (NSE/BSE) via DhanHQ and Zerodha. Infrastructure contains 425 cloned repos and 10+ local databases.
GOAL: Eradicate database lock contention and latency spikes by deploying an embedded, zero-copy high-throughput state engine.
BOTTLENECK: State fragmentation across 10+ SQLite files. On macOS APFS, concurrent multi-process writes trigger POSIX byte-range file lock collisions (SQLITE_BUSY error 5), freezing the event loop during opening bell tick bursts.
DOWNSTREAM IMPACT: Order status updates are dropped, desynchronizing positions and risk calculations.
PENDING TASK: Migrate from legacy SQLite silos to single-writer WAL paired with LMDB and DuckDB zero-copy memory mapping.
RESEARCH OBJECTIVE: Reverse-chronological search from September 16, 2026 backwards across GitHub, SQLite/DuckDB forums, Reddit, and systems blogs for:
1. Technical mechanisms of APFS SQLite locking anomalies and POSIX thread lock clashes on Apple Silicon.
2. Top 30 low-latency state synchronization hacks (single-writer queues, WAL tuning, PRAGMA synchronous=NORMAL, mmap).
3. Top 30 high-throughput storage, ring-buffer, and embedded database wheels (DuckDB, LMDB, ArcticDB, Apache Arrow).
4. Interconnection² mapping: Connect low-latency hacks with storage wheels to build an ACID zero-lock state store.
5. Verifiable provenance metadata (canonical URLs, dates, versions) and corruption failure modes."""

# ==============================================================================
# Q5: BOTTLENECK / RELIABILITY & ADVERSARIAL CASES
# ==============================================================================
prompts["Q5"] = """CONTEXT: Sovereign Algo Trading OS on macOS (M1 arm64, Python/C++) for NSE/BSE trading via DhanHQ and Zerodha Kite. Stack includes 425 cloned repos, 8 cortex modules, and local databases.
GOAL: Guarantee 100% state durability, crash recovery, and idempotency under market volatility and network failures.
BOTTLENECK: Multi-writer SQLite write-lock starvation and uncoordinated broker handoffs. During network drops, unconfirmed orders become indeterminate; blind retries cause duplicate fills.
DOWNSTREAM IMPACT: Capital loss from duplicate executions and orphaned positions evading risk controls.
PENDING TASK: Implement transactional outbox with deterministic SHA-256 idempotency tagging and two-phase broker reconciliation.
RESEARCH OBJECTIVE: Search reverse-chronologically from September 16, 2026 backwards across GitHub issues, postmortems, Reddit, and systems forums for:
1. Failure modes in async broker handoffs (timeout after send, out-of-order execution callbacks, phantom fills).
2. Top 30 resilience and idempotency hacks (UUIDv7 keys, monotonic sequence barriers, transactional outbox, ACK_UNKNOWN state).
3. Top 30 fault-tolerant broker adapter and recovery wheels (tenacity, aiolimiter, NATS JetStream, Redis Streams).
4. Interconnection² synthesis: Design compound recovery pipelines coupling idempotency hacks with broker reconnect routines.
5. Rigorous provenance metadata (resolvable links, maintainers, dates, versions) and counter-evidence."""

# ==============================================================================
# Q6: BOTTLENECK / INFRASTRUCTURE & HARDWARE SYMPATHY
# ==============================================================================
prompts["Q6"] = """CONTEXT: Sovereign Algo Trading OS on Apple Silicon M1 (macOS Darwin arm64, Python/C++) executing on NSE/BSE via Dhan and Zerodha. System includes 425 cloned repos and native modules.
GOAL: Exploit M1 hardware (NEON SIMD, unified memory, cache alignment) to achieve sub-microsecond state transitions without thread contention.
BOTTLENECK: Multi-threaded Python/C++ friction and weakly-ordered ARM64 memory reordering. Spinlocks with relaxed atomics cause state corruption and cache false sharing.
DOWNSTREAM IMPACT: Microsecond execution jitter, thread stalls, and core throttling between Performance and Efficiency cores.
PENDING TASK: Engineer single-writer lock-free ring buffer using C++ acquire-release atomics and QoS thread pinning on M1.
RESEARCH OBJECTIVE: Search reverse-chronologically from September 16, 2026 backwards across Apple developer forums, GitHub, and low-latency systems papers for:
1. Hardware optimization for Apple Silicon M1 ARM64 (cache line padding alignas(128), AMX, weak memory fences).
2. Top 30 local infrastructure hacks for Apple Silicon (pthread_set_qos_class_self_np, TCP_NODELAY, mimalloc, zero-copy FFI).
3. Top 30 low-latency execution wheels and lock-free queues (Disruptor, moodycamel, Boost.Lockfree, SBE).
4. Interconnection² mapping: Connect ARM64 hardware hacks with lock-free queue wheels for sub-microsecond tick processing.
5. Canonical provenance metadata (official URLs, author handles, dates, versions) and failure modes."""

# ==============================================================================
# Q7: PENDING TASK / BEST EXECUTION APPROACH
# ==============================================================================
prompts["Q7"] = """CONTEXT: Sovereign Algo Trading OS on macOS (M1 arm64, Python/C++) for Indian markets via DhanHQ and Zerodha Kite. Stack has 425 cloned repos, 290 codebases, and 8 cortex modules.
GOAL: Execute the pending task: consolidating fragmented trading scripts into a unified gateway with deterministic SEBI 2026 compliance.
PENDING TASK: Unify 425 codebases into a single-writer gateway enforcing SEBI 2026 mandates: 10 Orders Per Second (OPS) limit and Order-to-Trade Ratio (OTR <= 50:1) with dynamic +/- 40% LTP price bands.
DOWNSTREAM IMPACT: Prevents exchange penalty fees, account suspension, and execution drift while establishing a single source of truth.
CONSTRAINTS: Reuse existing cloned wheels (ArcticDB, skfolio, pybroker), avoid greenfield rewrites, and eliminate APFS lock collisions.
RESEARCH OBJECTIVE: Search reverse-chronologically from September 16, 2026 backwards across GitHub, Indian quant forums, Reddit, and regulatory circulars for:
1. Workflows for consolidating multi-repo quant trading codebases into a unified monorepo.
2. Top 30 execution hacks for SEBI 2026 compliance (dynamic OTR shielding, token-bucket rate limiting, static IP routing).
3. Top 30 monorepo packaging and governance wheels (uv workspaces, Pants/Bazel, Ruff, AST-Grep, Cosign).
4. Interconnection² synthesis: Combine monorepo governance with SEBI 2026 execution gates into an unbroken deployment pipeline.
5. Detailed provenance metadata (canonical URLs, dates, versions) and compliance failure modes."""

# ==============================================================================
# Q8: PENDING TASK / TESTING & PHYSICAL VERIFICATION
# ==============================================================================
prompts["Q8"] = """CONTEXT: Sovereign Algo Trading OS on macOS (Apple Silicon M1, Python/C++) executing on NSE/BSE via DhanHQ and Zerodha. System includes 425 cloned repos and unified execution cortex.
GOAL: Validate consolidated trading infrastructure through rigorous adversarial verification, fault injection, and zero-variance testing.
PENDING TASK: Physically prove that the execution gateway exhibits zero execution drift, zero duplicate orders, and zero APFS lock contention under 10x market load.
DOWNSTREAM IMPACT: Guarantees that live capital deployed through the gateway is immune to split-brain anomalies and broker API edge cases.
CONSTRAINTS: Must execute repeatable offline tests without risking live capital; verify SQLite WAL and DuckDB replay.
RESEARCH OBJECTIVE: Search reverse-chronologically from September 16, 2026 backwards across GitHub, testing frameworks, Reddit, and quant forums for:
1. Adversarial testing strategies, chaos protocols, and backtest-to-live parity verification for Indian brokers.
2. Top 30 testing and verification hacks (shadow trading, mock broker fault injection, Hypothesis property testing, tick replay).
3. Top 30 testing, simulation, and verification wheels (Toxiproxy, WireMock, VCR.py, pytest-xdist, Locust, Nautilus Sandbox).
4. Interconnection² mapping: Connect testing hacks with chaos wheels to build an automated 10x adversarial test rig.
5. Strict provenance metadata (canonical URLs, release tags, authors, dates) and testing failure modes."""

# ==============================================================================
# Q9: PENDING TASK / INTERCONNECTION² SYNTHESIS
# ==============================================================================
prompts["Q9"] = """CONTEXT: Sovereign Quant Trading OS on M1 (macOS arm64, Python/C++) interfacing with DhanHQ and Zerodha Kite. Stack includes 425 cloned repos, 100 synthesized hacks, and unified cortex.
GOAL: Synthesize the ultimate Interconnection² architecture fusing 100 practitioner hacks with 100 downloaded wheels into an autonomous quant engine.
PENDING TASK: Wire acquired wheels (ArcticDB, skfolio, pybroker, hftbacktest) and diagnostic tools into a cohesive whole to eliminate split-brain drift and lock contention.
DOWNSTREAM IMPACT: Delivers sub-microsecond tick processing, deterministic risk shielding, and continuous AI telemetry via FastMCP without compromising the hot path.
CONSTRAINTS: FastMCP and LLM telemetry must be strictly read-only; zero write-access to the execution ring buffer.
RESEARCH OBJECTIVE: Search reverse-chronologically from September 16, 2026 backwards across GitHub, arXiv, Reddit, and AI blogs for:
1. Patterns for multi-tier quant systems fusing execution cores with AI telemetry bridges.
2. Top 30 second-order Interconnection² hacks synthesizing multi-broker execution, portfolio optimization, and risk monitoring.
3. Top 30 advanced orchestration and telemetry wheels (FastMCP, LiteLLM, Arize Phoenix, Sentrux, DuckDB Arrow).
4. Interconnection² compound capabilities: Design cross-layer stacks combining skfolio + ArcticDB + DhanHQ + FastMCP.
5. Provenance metadata (canonical URLs, author organizations, dates, versions) and operational safeguards."""

print("="*60)
print("CHARACTER COUNT VERIFICATION FOR ALL 9 PROMPTS")
print("Target: 1000 - 1500 characters")
print("="*60)

all_passed = True
for key in sorted(prompts.keys()):
    length = len(prompts[key])
    passed = 1000 <= length <= 1500
    status = "PASS" if passed else "FAIL"
    if not passed:
        all_passed = False
    print(f"{key}: {length} chars -> {status}")

if all_passed:
    print("\nALL 9 PROMPTS STRICTLY PASS THE 1000-1500 CHAR CONTRACT!")
else:
    print("\nSOME PROMPTS FAILED! REWRITE NEEDED.")
    sys.exit(1)
