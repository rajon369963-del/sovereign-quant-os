# 🏛️ NotebookLM Quant Source: 06_MICROSTRUCTURE_ORDERFLOW

**Total Grounded Repositories in this Volume**: 7
**Compilation Date**: September 16, 2026

---

## 1. jizb880_hermes_telemetry
- **Repository ID**: `REPO_JIZB880_HERMES_TELEMETRY`
- **Primary Domain**: `High Frequency & Telemetry`
- **Remote URL**: [https://github.com/jizb880/hermes_telemetry.git](https://github.com/jizb880/hermes_telemetry.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/jizb880_hermes_telemetry`
- **Description**: Repository jizb880_hermes_telemetry located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/jizb880_hermes_telemetry

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Hermes Telemetry

An OpenTelemetry observability plugin for [Hermes Agent](https://github.com/nousresearch/hermes-agent), providing full-chain trace tracking and metrics collection.

**[English](#english) | [中文](#中文)**

---

<a id="english"></a>

## Features

- **6 Hook Points**: Covers Session, LLM, and Tool lifecycle (on_session_start/end, pre/post_llm_call, pre/post_tool_call)
- **Unified Trace Correlation**: All spans within a session share a single trace_id for end-to-end tracing
- **Dual-Channel Output**: Real-time console printing + NDJSON file persistence, no external dependencies required
- **OpenTelemetry Standard**: Traces and Metrics follow OpenTelemetry semantic conventions
- **Fine-Grained Control**: Each hook point can be independently toggled; input/output capture is optional
- **Thread-Safe**: Supports concurrent tool calls with LIFO stack management for nested tool spans
- **Zero Intrusion**: All hook errors are isolated and never affect agent operation

## Span Hierarchy

```
hermes.session (root)
└── hermes.llm.call
    ├── hermes.tool.web_search
    ├── hermes.tool.read_file
    └── hermes.tool.execute_code
```

## Quick Start

### 1. Install Dependencies

```bash
pip install opentelemetry-api opentelemetry-sdk
```

### 2. Deploy Plugin

```bash
cp -r hermes_telemetry ~/.hermes/plugins/hermes_telemetry
```

### 3. Configure (Optional)

Edit `~/.hermes/plugins/hermes_telemetry/config/observability.json`:

```json
{
  "enabled": true,
  "service_name": "hermes-agent",
  "console_export_enabled": true,
  "ndjson_export_enabled": true,
  "ndjson_export_path": "."
}
```

### 4. Run

Start Hermes Agent as usual. The plugin loads automatically and begins collecting data:

```bash
hermes
```

Console output:

```
[hermes_telemetry] Initialized (service=hermes-agent)
[hermes_telemetry] Console export: enabled
[hermes_telemetry] NDJSON export: ./hermes-otel-spans.jsonl
[hermes_telemetry] Hooks registered: session, llm, tool
[hermes_telemetry] Plugin registered successfully.
```

### 5. View Data

```bash
# View NDJSON file
cat hermes-otel-spans.jsonl | jq .

# Filter by trace_id
cat hermes-otel-spans.jsonl | jq 'select(.trace_id == "YOUR_TRACE_ID")'
```

## Project Structure

```
hermes_telemetry/
├── plugin.yaml                      # Hermes plugin manifest
├── __init__.py                      # Plugin entry point register(ctx)
├── config/
│   └── observability.json           # Default configuration
├── hermes_otel/
│   ├── config.py                    # Config loading & parsing
│   ├── tracer.py                    # GlobalTracer singleton
│   ├── state.py                     # Session state management
│   ├── attributes.py                # Attribute truncation utilities
│   ├── metrics.py                   # Metrics definitions
│   ├── exporters/
│   │   └── jsonl_file_exporter.py   # NDJSON file exporter
│   └── hooks/
│       ├── __init__.py              # Hook registration orchestrator
│       ├── session.py               # Session lifecycle hooks
│       ├── llm.py                   # LLM call hooks
│       └── tool.py                  # Tool call hooks
├── docs/
│   └── USAGE.md                     # Detailed usage documentation
├── pyproject.toml                   # Python packaging config
└── requirements.txt                 # Dependencies
```

## Documentation

See [docs/USAGE.md](docs/USAGE.md) for the complete usage and configuration guide.

## References

- [openclaw_telemetry](https://github.com/jizb880/opencl
```

---

## 2. hermes_telemetry
- **Repository ID**: `REPO_HERMES_TELEMETRY`
- **Primary Domain**: `High Frequency & Telemetry`
- **Remote URL**: [https://github.com/jizb880/hermes_telemetry.git](https://github.com/jizb880/hermes_telemetry.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/hermes_telemetry`
- **Description**: Repository hermes_telemetry located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/hermes_telemetry

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Hermes Telemetry

An OpenTelemetry observability plugin for [Hermes Agent](https://github.com/nousresearch/hermes-agent), providing full-chain trace tracking and metrics collection.

**[English](#english) | [中文](#中文)**

---

<a id="english"></a>

## Features

- **6 Hook Points**: Covers Session, LLM, and Tool lifecycle (on_session_start/end, pre/post_llm_call, pre/post_tool_call)
- **Unified Trace Correlation**: All spans within a session share a single trace_id for end-to-end tracing
- **Dual-Channel Output**: Real-time console printing + NDJSON file persistence, no external dependencies required
- **OpenTelemetry Standard**: Traces and Metrics follow OpenTelemetry semantic conventions
- **Fine-Grained Control**: Each hook point can be independently toggled; input/output capture is optional
- **Thread-Safe**: Supports concurrent tool calls with LIFO stack management for nested tool spans
- **Zero Intrusion**: All hook errors are isolated and never affect agent operation

## Span Hierarchy

```
hermes.session (root)
└── hermes.llm.call
    ├── hermes.tool.web_search
    ├── hermes.tool.read_file
    └── hermes.tool.execute_code
```

## Quick Start

### 1. Install Dependencies

```bash
pip install opentelemetry-api opentelemetry-sdk
```

### 2. Deploy Plugin

```bash
cp -r hermes_telemetry ~/.hermes/plugins/hermes_telemetry
```

### 3. Configure (Optional)

Edit `~/.hermes/plugins/hermes_telemetry/config/observability.json`:

```json
{
  "enabled": true,
  "service_name": "hermes-agent",
  "console_export_enabled": true,
  "ndjson_export_enabled": true,
  "ndjson_export_path": "."
}
```

### 4. Run

Start Hermes Agent as usual. The plugin loads automatically and begins collecting data:

```bash
hermes
```

Console output:

```
[hermes_telemetry] Initialized (service=hermes-agent)
[hermes_telemetry] Console export: enabled
[hermes_telemetry] NDJSON export: ./hermes-otel-spans.jsonl
[hermes_telemetry] Hooks registered: session, llm, tool
[hermes_telemetry] Plugin registered successfully.
```

### 5. View Data

```bash
# View NDJSON file
cat hermes-otel-spans.jsonl | jq .

# Filter by trace_id
cat hermes-otel-spans.jsonl | jq 'select(.trace_id == "YOUR_TRACE_ID")'
```

## Project Structure

```
hermes_telemetry/
├── plugin.yaml                      # Hermes plugin manifest
├── __init__.py                      # Plugin entry point register(ctx)
├── config/
│   └── observability.json           # Default configuration
├── hermes_otel/
│   ├── config.py                    # Config loading & parsing
│   ├── tracer.py                    # GlobalTracer singleton
│   ├── state.py                     # Session state management
│   ├── attributes.py                # Attribute truncation utilities
│   ├── metrics.py                   # Metrics definitions
│   ├── exporters/
│   │   └── jsonl_file_exporter.py   # NDJSON file exporter
│   └── hooks/
│       ├── __init__.py              # Hook registration orchestrator
│       ├── session.py               # Session lifecycle hooks
│       ├── llm.py                   # LLM call hooks
│       └── tool.py                  # Tool call hooks
├── docs/
│   └── USAGE.md                     # Detailed usage documentation
├── pyproject.toml                   # Python packaging config
└── requirements.txt                 # Dependencies
```

## Documentation

See [docs/USAGE.md](docs/USAGE.md) for the complete usage and configuration guide.

## References

- [openclaw_telemetry](https://github.com/jizb880/opencl
```

---

## 3. tokentelemetry-hermes-plugin
- **Repository ID**: `REPO_TOKENTELEMETRY_HERMES_PLUGIN`
- **Primary Domain**: `High Frequency & Telemetry`
- **Remote URL**: [https://github.com/VasiHemanth/tokentelemetry-hermes-plugin.git](https://github.com/VasiHemanth/tokentelemetry-hermes-plugin.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/tokentelemetry-hermes-plugin`
- **Description**: Repository tokentelemetry-hermes-plugin located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/tokentelemetry-hermes-plugin

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# TokenTelemetry — Hermes Dashboard Plugin

> A launcher tab inside [Hermes Agent](https://github.com/NousResearch/hermes-agent)'s web dashboard for **[TokenTelemetry](https://tokentelemetry.com)** — local observability for **Hermes Agent AND 9 coding agents** (Claude Code, OpenAI Codex, Gemini CLI, Cursor, GitHub Copilot, Qwen, OpenCode, Vibe, Antigravity).

> ℹ️ This repo is **auto-generated** from the canonical source in [`VasiHemanth/tokentelemetry`](https://github.com/VasiHemanth/tokentelemetry). File issues and PRs upstream.

## What this plugin does

Registers a `TokenTelemetry` tab in your Hermes Dashboard sidebar. Deep-link cards open TT pages in a new browser tab — one port to remember (`:9119`), no context-switching to `:3000`.

Pages reachable from the launcher:

- `/hermes` — overview (sessions, sources, models, cron health)
- `/hermes/skills` — loaded skills with platform conditions
- `/hermes/memory` — `MEMORY.md` and `USER.md` with progress bars
- `/analytics` — tokens, cost, trends **across all agents** (not just Hermes)
- `/projects` — per-project rollups, all agents combined
- `/` — connected agents (coding + autonomous)

## Install

### Prereq: install TokenTelemetry itself

The plugin is a **launcher, not the engine**. You need TokenTelemetry running:

```bash
# macOS / Linux
curl -fsSL https://tokentelemetry.com/install.sh | bash

# Windows
irm https://tokentelemetry.com/install.ps1 | iex
```

Or clone the repo: <https://github.com/VasiHemanth/tokentelemetry>

### Install the plugin

```bash
hermes plugins install VasiHemanth/tokentelemetry-hermes-plugin
hermes dashboard
```

Then open `http://127.0.0.1:9119` and click **TokenTelemetry** in the sidebar.

## What TokenTelemetry covers (so this plugin earns its keep)

TokenTelemetry isn't a Hermes-only tool. It tracks every AI agent you use:

| Agent | What TT shows |
|---|---|
| **Hermes Agent** | Dedicated `/hermes` dashboard — 38 source platforms, gateway health, cron jobs, skills + memory, subagent cards, per-API-call latency |
| Claude Code | Sessions, tool calls, plan-mode capture, costs |
| OpenAI Codex CLI | Sessions, tool calls, costs |
| Gemini CLI | Sessions, costs, tool calls |
| Cursor | Session activity |
| GitHub Copilot | Token / cost tracking |
| Qwen CLI | Sessions, costs |
| OpenCode | Sessions, costs |
| Vibe | Sessions |
| Antigravity | Sessions |

Plus a unified `/analytics` view across all of them.

## Privacy

The plugin is pure-frontend. It reads no Hermes data directly, makes no network requests beyond your local TokenTelemetry instance, and ships no telemetry. Your data never leaves your machine.

## License

MIT — see [LICENSE](LICENSE).

## Links

- **TokenTelemetry homepage**: <https://tokentelemetry.com>
- **TokenTelemetry source**: <https://github.com/VasiHemanth/tokentelemetry>
- **Hermes Agent**: <https://github.com/NousResearch/hermes-agent>
- **Report a bug / request a feature**: <https://github.com/VasiHemanth/tokentelemetry/issues>
```

---

## 4. VasiHemanth_tokentelemetry-hermes-plugin
- **Repository ID**: `REPO_VASIHEMANTH_TOKENTELEMETRY_HERMES_PLUGIN`
- **Primary Domain**: `High Frequency & Telemetry`
- **Remote URL**: [https://github.com/VasiHemanth/tokentelemetry-hermes-plugin.git](https://github.com/VasiHemanth/tokentelemetry-hermes-plugin.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/VasiHemanth_tokentelemetry-hermes-plugin`
- **Description**: Repository VasiHemanth_tokentelemetry-hermes-plugin located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/VasiHemanth_tokentelemetry-hermes-plugin

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# TokenTelemetry — Hermes Dashboard Plugin

> A launcher tab inside [Hermes Agent](https://github.com/NousResearch/hermes-agent)'s web dashboard for **[TokenTelemetry](https://tokentelemetry.com)** — local observability for **Hermes Agent AND 9 coding agents** (Claude Code, OpenAI Codex, Gemini CLI, Cursor, GitHub Copilot, Qwen, OpenCode, Vibe, Antigravity).

> ℹ️ This repo is **auto-generated** from the canonical source in [`VasiHemanth/tokentelemetry`](https://github.com/VasiHemanth/tokentelemetry). File issues and PRs upstream.

## What this plugin does

Registers a `TokenTelemetry` tab in your Hermes Dashboard sidebar. Deep-link cards open TT pages in a new browser tab — one port to remember (`:9119`), no context-switching to `:3000`.

Pages reachable from the launcher:

- `/hermes` — overview (sessions, sources, models, cron health)
- `/hermes/skills` — loaded skills with platform conditions
- `/hermes/memory` — `MEMORY.md` and `USER.md` with progress bars
- `/analytics` — tokens, cost, trends **across all agents** (not just Hermes)
- `/projects` — per-project rollups, all agents combined
- `/` — connected agents (coding + autonomous)

## Install

### Prereq: install TokenTelemetry itself

The plugin is a **launcher, not the engine**. You need TokenTelemetry running:

```bash
# macOS / Linux
curl -fsSL https://tokentelemetry.com/install.sh | bash

# Windows
irm https://tokentelemetry.com/install.ps1 | iex
```

Or clone the repo: <https://github.com/VasiHemanth/tokentelemetry>

### Install the plugin

```bash
hermes plugins install VasiHemanth/tokentelemetry-hermes-plugin
hermes dashboard
```

Then open `http://127.0.0.1:9119` and click **TokenTelemetry** in the sidebar.

## What TokenTelemetry covers (so this plugin earns its keep)

TokenTelemetry isn't a Hermes-only tool. It tracks every AI agent you use:

| Agent | What TT shows |
|---|---|
| **Hermes Agent** | Dedicated `/hermes` dashboard — 38 source platforms, gateway health, cron jobs, skills + memory, subagent cards, per-API-call latency |
| Claude Code | Sessions, tool calls, plan-mode capture, costs |
| OpenAI Codex CLI | Sessions, tool calls, costs |
| Gemini CLI | Sessions, costs, tool calls |
| Cursor | Session activity |
| GitHub Copilot | Token / cost tracking |
| Qwen CLI | Sessions, costs |
| OpenCode | Sessions, costs |
| Vibe | Sessions |
| Antigravity | Sessions |

Plus a unified `/analytics` view across all of them.

## Privacy

The plugin is pure-frontend. It reads no Hermes data directly, makes no network requests beyond your local TokenTelemetry instance, and ships no telemetry. Your data never leaves your machine.

## License

MIT — see [LICENSE](LICENSE).

## Links

- **TokenTelemetry homepage**: <https://tokentelemetry.com>
- **TokenTelemetry source**: <https://github.com/VasiHemanth/tokentelemetry>
- **Hermes Agent**: <https://github.com/NousResearch/hermes-agent>
- **Report a bug / request a feature**: <https://github.com/VasiHemanth/tokentelemetry/issues>
```

---

## 5. VasiHemanth_tokentelemetry
- **Repository ID**: `REPO_VASIHEMANTH_TOKENTELEMETRY`
- **Primary Domain**: `High Frequency & Telemetry`
- **Remote URL**: [https://github.com/VasiHemanth/tokentelemetry.git](https://github.com/VasiHemanth/tokentelemetry.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/VasiHemanth_tokentelemetry`
- **Description**: Repository VasiHemanth_tokentelemetry located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/VasiHemanth_tokentelemetry

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Token Telemetry (TokenTelemetry)

> **Local observability for AI coding agents and autonomous agents — Claude Code, Codex, Gemini CLI, Cursor, Copilot, Qwen, OpenCode, Vibe, Antigravity, Grok Build, Cline, SmallCode, Pi, Muse Code, Prime Agent, Qoder, _and_ Nous Research's Hermes Agent.**

**Token Telemetry** (one word: **TokenTelemetry**) — free, open-source, 100% local.

> ☤ **New:** Dedicated **[Hermes Agent](#hermes-agent-autonomous-observability)** dashboard — autonomous-agent observability across 38 platforms (CLI, Telegram, Discord, cron, webhook, …).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green)](https://nodejs.org)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org)
[![Website](https://img.shields.io/badge/Website-tokentelemetry.com-blue)](https://tokentelemetry.com)
[![GitHub Stars](https://img.shields.io/github/stars/VasiHemanth/tokentelemetry?style=social)](https://github.com/VasiHemanth/tokentelemetry)

**TokenTelemetry** is a free, open-source, 100% local observability dashboard that tracks **token usage**, **LLM costs**, **tool calls**, **session traces**, and **reasoning steps** across all your AI coding agents — in one unified place. No signup. No cloud. Your logs never leave your machine.

🌐 **Website & Docs:** [https://tokentelemetry.com](https://tokentelemetry.com)  
🖥️ **macOS/Linux:** `curl -fsSL https://raw.githubusercontent.com/VasiHemanth/tokentelemetry/main/install.sh | bash`
🧰 **Windows:** `irm https://raw.githubusercontent.com/VasiHemanth/tokentelemetry/main/install.ps1 | iex`
🐙 **GitHub:** [github.com/VasiHemanth/tokentelemetry](https://github.com/VasiHemanth/tokentelemetry)

---

## Why TokenTelemetry?

AI coding agents like Claude Code, Gemini CLI, and Codex are powerful — but they burn through tokens fast. **How many tokens did that refactor cost? Which agent is most efficient? What did it actually do?**

TokenTelemetry answers all of that — locally, instantly, for free.

| Problem                                                | TokenTelemetry Solution                     |
| ------------------------------------------------------ | ------------------------------------------- |
| "How much did that Claude Code session cost?"          | Real-time cost tracking per session/project |
| "What tools did my agent call?"                        | Full waterfall trace of every tool call     |
| "Which model is most token-efficient for my codebase?" | Per-model analytics & comparisons           |
| "Did my agent follow its plan?"                        | Plan-mode capture & display                 |
| "I use 3 different agents — unified view?"             | Multi-agent dashboard in one place          |

---

## Supported Agents

TokenTelemetry reads session logs from these agents automatically.

### Coding agents

| Agent                       | Status             |
| --------------------------- | ------------------ |
| **Claude Code** (Anthropic) | ✅ Fully supported |
| **Gemini CLI** (Google)     | ✅ Fully supported |
| **OpenAI Codex CLI**        | ✅ Fully supported |
| **Cursor**                  | ✅ Fully supported |
| **GitHub Copilot**          | ✅ Fully supported |
| **OpenCode**                | ✅ Fully supported |
| **Qwen**                    | ✅ Fully supported |
| **Vibe**                    | ✅ Fully supported |
| **Antigravity**             | 
```

---

## 6. tokentelemetry
- **Repository ID**: `REPO_TOKENTELEMETRY`
- **Primary Domain**: `High Frequency & Telemetry`
- **Remote URL**: [https://github.com/VasiHemanth/tokentelemetry.git](https://github.com/VasiHemanth/tokentelemetry.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/tokentelemetry`
- **Description**: Repository tokentelemetry located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/tokentelemetry

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Token Telemetry (TokenTelemetry)

> **Local observability for AI coding agents and autonomous agents — Claude Code, Codex, Gemini CLI, Cursor, Copilot, Qwen, OpenCode, Vibe, Antigravity, Grok Build, Cline, SmallCode, Pi, Muse Code, Prime Agent, Qoder, _and_ Nous Research's Hermes Agent.**

**Token Telemetry** (one word: **TokenTelemetry**) — free, open-source, 100% local.

> ☤ **New:** Dedicated **[Hermes Agent](#hermes-agent-autonomous-observability)** dashboard — autonomous-agent observability across 38 platforms (CLI, Telegram, Discord, cron, webhook, …).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green)](https://nodejs.org)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org)
[![Website](https://img.shields.io/badge/Website-tokentelemetry.com-blue)](https://tokentelemetry.com)
[![GitHub Stars](https://img.shields.io/github/stars/VasiHemanth/tokentelemetry?style=social)](https://github.com/VasiHemanth/tokentelemetry)

**TokenTelemetry** is a free, open-source, 100% local observability dashboard that tracks **token usage**, **LLM costs**, **tool calls**, **session traces**, and **reasoning steps** across all your AI coding agents — in one unified place. No signup. No cloud. Your logs never leave your machine.

🌐 **Website & Docs:** [https://tokentelemetry.com](https://tokentelemetry.com)  
🖥️ **macOS/Linux:** `curl -fsSL https://raw.githubusercontent.com/VasiHemanth/tokentelemetry/main/install.sh | bash`
🧰 **Windows:** `irm https://raw.githubusercontent.com/VasiHemanth/tokentelemetry/main/install.ps1 | iex`
🐙 **GitHub:** [github.com/VasiHemanth/tokentelemetry](https://github.com/VasiHemanth/tokentelemetry)

---

## Why TokenTelemetry?

AI coding agents like Claude Code, Gemini CLI, and Codex are powerful — but they burn through tokens fast. **How many tokens did that refactor cost? Which agent is most efficient? What did it actually do?**

TokenTelemetry answers all of that — locally, instantly, for free.

| Problem                                                | TokenTelemetry Solution                     |
| ------------------------------------------------------ | ------------------------------------------- |
| "How much did that Claude Code session cost?"          | Real-time cost tracking per session/project |
| "What tools did my agent call?"                        | Full waterfall trace of every tool call     |
| "Which model is most token-efficient for my codebase?" | Per-model analytics & comparisons           |
| "Did my agent follow its plan?"                        | Plan-mode capture & display                 |
| "I use 3 different agents — unified view?"             | Multi-agent dashboard in one place          |

---

## Supported Agents

TokenTelemetry reads session logs from these agents automatically.

### Coding agents

| Agent                       | Status             |
| --------------------------- | ------------------ |
| **Claude Code** (Anthropic) | ✅ Fully supported |
| **Gemini CLI** (Google)     | ✅ Fully supported |
| **OpenAI Codex CLI**        | ✅ Fully supported |
| **Cursor**                  | ✅ Fully supported |
| **GitHub Copilot**          | ✅ Fully supported |
| **OpenCode**                | ✅ Fully supported |
| **Qwen**                    | ✅ Fully supported |
| **Vibe**                    | ✅ Fully supported |
| **Antigravity**             | 
```

---

## 7. Tick-Database
- **Repository ID**: `REPO_CURATED_TICK_DATABASE`
- **Primary Domain**: `Tick Storage & Parquet`
- **Remote URL**: [https://github.com/tick-store/tick-database](https://github.com/tick-store/tick-database)
- **Local Disk Path**: `remote:https://github.com/tick-store/tick-database`
- **Description**: High-throughput tick data storage and retrieval engine leveraging DuckDB columnar storage and Parquet compression.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Tick Storage & Parquet.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

