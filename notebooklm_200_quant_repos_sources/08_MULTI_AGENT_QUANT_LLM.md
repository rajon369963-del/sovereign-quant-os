# 🏛️ NotebookLM Quant Source: 08_MULTI_AGENT_QUANT_LLM

**Total Grounded Repositories in this Volume**: 11
**Compilation Date**: September 16, 2026

---

## 1. notebooklm-rest-api
- **Repository ID**: `REPO_NOTEBOOKLM_REST_API`
- **Primary Domain**: `Agentic LLM & Knowledge Graph`
- **Remote URL**: [https://github.com/gnh1201/notebooklm-rest-api](https://github.com/gnh1201/notebooklm-rest-api)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/notebooklm-rest-api`
- **Description**: Repository notebooklm-rest-api located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/notebooklm-rest-api

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# 📘 notebooklm-rest-api

[![Discord chat](https://img.shields.io/discord/359930650330923008?logo=discord)](https://discord.gg/SjHtURQKBc?utm_source=catswords)

> A REST API wrapper for Google NotebookLM powered by `notebooklm-py`

`notebooklm-rest-api` exposes the functionality of
[`teng-lin/notebooklm-py`](https://github.com/teng-lin/notebooklm-py)
as a clean, production-ready REST API service.

It allows you to manage Notebooks, add sources, perform Q&A, generate artifacts, and download outputs via HTTP.

---

## 🚀 Features

### 📂 Notebook Management

* Create notebook
* List notebooks
* Get notebook details
* Rename notebook
* Delete notebook
* Get summary
* Get description

### 📄 Source Management

* Add URL source
* Add YouTube source
* Add raw text
* Upload file
* Get full text
* Get source guide
* Delete source

### 💬 Chat API

* Ask questions based on notebook context

### 🎨 Artifact Generation

* Audio
* Video
* Report
* Quiz
* Flashcards
* Slide deck
* Infographic
* Data table
* Mind map
* Task polling support
* File download support

### 🔐 Optional API Key Protection

---

## 🧱 Architecture

```
Client (REST)
    ↓
FastAPI
    ↓
notebooklm-py
    ↓
NotebookLM (Web API)
```

---

## 📦 Requirements

* Python 3.10+
* NotebookLM account
* First-time login using `notebooklm login`

---

## ⚙️ Installation

### 1️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Authenticate (one-time setup)

```bash
notebooklm login
```

By default, authentication is stored at:

```
~/.notebooklm/storage_state.json
```

You can override it with:

```bash
export NOTEBOOKLM_STORAGE_PATH=/path/to/storage_state.json
```

---

## ▶️ Run Server

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## 🔐 Optional API Key Protection

Set API key:

```bash
export NOTEBOOKLM_REST_API_KEY=your-secret-key
```

Send header:

```
X-API-Key: your-secret-key
```

---

## 📚 API Examples

### List Notebooks

```bash
GET /v1/notebooks
```

---

### Create Notebook

```bash
POST /v1/notebooks
{
  "title": "My Research"
}
```

---

### Add URL Source

```bash
POST /v1/notebooks/{notebook_id}/sources/url
{
  "url": "https://example.com",
  "wait": true
}
```

---

### Ask Question

```bash
POST /v1/notebooks/{notebook_id}/chat/ask
{
  "question": "Summarize the key insights"
}
```

---

### Generate Quiz

```bash
POST /v1/notebooks/{notebook_id}/artifacts/generate
{
  "type": "quiz",
  "options": {}
}
```

---

### Poll Task

```bash
GET /v1/notebooks/{notebook_id}/artifacts/tasks/{task_id}
```

---

### Download Artifact

```bash
GET /v1/notebooks/{notebook_id}/artifacts/download?type=quiz&output_format=json
```

---

## 🌍 Environment Variables

| Variable                | Description                |
| ----------------------- | -------------------------- |
| NOTEBOOKLM_STORAGE_PATH | Path to storage_state.json |
| NOTEBOOKLM_AUTH_JSON    | Inject auth JSON directly  |
| NOTEBOOKLM_HOME         | Base notebooklm directory  |
| NOTEBOOKLM_REST_API_KEY | REST API protection key    |

---

## 🐳 Docker Example

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ⚠️ Disclaimer

This proj
```

---

## 2. NotebookMLX
- **Repository ID**: `REPO_NOTEBOOKMLX`
- **Primary Domain**: `Agentic LLM & Knowledge Graph`
- **Remote URL**: [https://github.com/johnmai-dev/NotebookMLX](https://github.com/johnmai-dev/NotebookMLX)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/NotebookMLX`
- **Description**: Repository NotebookMLX located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/NotebookMLX

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# NotebookMLX

English | [简体中文](./zh_CN/README.md)

> [meta-llama/NotebookLlama](https://github.com/meta-llama/llama-recipes/tree/main/recipes/quickstart/NotebookLlama)

I ported [NotebookLlama](https://github.com/meta-llama/llama-recipes/tree/main/recipes/quickstart/NotebookLlama) and
implemented it with [MLX](https://github.com/ml-explore/mlx) 🔥

It uses [mlx-community/Qwen2.5-1.5B-Instruct-bf16](https://huggingface.co/mlx-community/Qwen2.5-1.5B-Instruct-4bit) for
pre-processing the
PDF, [mlx-community/Qwen2.5-14B-Instruct-4bit](https://huggingface.co/mlx-community/Qwen2.5-14B-Instruct-4bit) for
creating
transcripts, [mlx-community/Qwen2.5-7B-Instruct-4bit](https://huggingface.co/mlx-community/Qwen2.5-7B-Instruct-4bit) for
rewrites, and [lucasnewman/f5-tts-mlx](https://huggingface.co/lucasnewman/f5-tts-mlx) for Text-to-Speech ⚡

> Citing the NotebookLlama outline.
> ![Outline.jpg](resources/Outline.jpg)


[Step 1](Step-1-PDF-Pre-Processing-Logic.ipynb): Pre-process PDF:
Use [mlx-community/Qwen2.5-1.5B-Instruct-bf16](https://huggingface.co/mlx-community/Qwen2.5-1.5B-Instruct-4bit) to
pre-process the PDF and save it in a .txt file.

[Step 2](Step-2-Transcript-Writer.ipynb): Transcript Writer:
Use [mlx-community/Qwen2.5-14B-Instruct-4bit](https://huggingface.co/mlx-community/Qwen2.5-14B-Instruct-4bit) to write a
podcast transcript from the text.

[Step 3](Step-3-Re-Writer.ipynb): Dramatic Re-Writer: Use
the [mlx-community/Qwen2.5-7B-Instruct-4bit](https://huggingface.co/mlx-community/Qwen2.5-7B-Instruct-4bit) model to
make the transcript more dramatic.

[Step 4](Step-4-TTS-Workflow.ipynb): Text-To-Speech Workflow:
Use [lucasnewman/f5-tts-mlx](https://huggingface.co/lucasnewman/f5-tts-mlx) to generate
a conversational podcast.

## The podcast audio

https://github.com/user-attachments/assets/c7cf2d2f-766f-4026-8442-c584f6a32292

## Star History

<a href="https://star-history.com/#maiqingqiang/NotebookMLX&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=maiqingqiang/NotebookMLX&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=maiqingqiang/NotebookMLX&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=maiqingqiang/NotebookMLX&type=Date" />
 </picture>
</a>
```

---

## 3. notebookllama
- **Repository ID**: `REPO_NOTEBOOKLLAMA`
- **Primary Domain**: `Agentic LLM & Knowledge Graph`
- **Remote URL**: [https://github.com/run-llama/notebookllama](https://github.com/run-llama/notebookllama)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/notebookllama`
- **Description**: Repository notebookllama located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/notebookllama

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# NotebookLlaMa🦙

## A fluffy and open-source alternative to NotebookLM!

https://github.com/user-attachments/assets/7e9cca45-8a4c-4dfa-98d2-2cef147422f2

<p align="center">
  A fully open-source alternative to NotebookLM, backed by <a href="https://cloud.llamaindex.ai?utm_source=demo&utm_medium=notebookLM"><strong>LlamaCloud</strong></a>.
</p>

<p align="center">
    <a href="https://github.com/run-llama/notebookllama/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/run-llama/notebookllama?color=blue"></a>
    <a href="https://github.com/run-llama/notebookllama/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/run-llama/notebookllama?color=yellow"></a>
    <a href="https://github.com/run-llama/notebookllama/issues"><img alt="Issues" src="https://img.shields.io/github/issues/run-llama/notebookllama?color=orange"></a>
    <br>
    <a href="https://mseep.ai/app/run-llama-notebookllama"><img alt="MseeP.ai Security Assessment Badge" src="https://mseep.net/pr/run-llama-notebookllama-badge.png"></a>
</p>

### Prerequisites

This project uses `uv` to manage dependencies. Before you begin, make sure you have `uv` installed.

On macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

For more install options, see `uv`'s [official documentation](https://docs.astral.sh/uv/getting-started/installation/).

---

### Get it up and running!

**1. Clone the Repository**

```bash
git clone https://github.com/run-llama/notebookllama
cd notebookllama/
```

**2. Install Dependencies**

```bash
uv sync
```

**3. Configure API Keys**

First, create your `.env` file by renaming the example file:

```bash
mv .env.example .env
```

Next, open the `.env` file and add your API keys:

- `OPENAI_API_KEY`: find it [on OpenAI Platform](https://platform.openai.com/api-keys)
- `ELEVENLABS_API_KEY`: find it [on ElevenLabs Settings](https://elevenlabs.io/app/settings/api-keys)
- `LLAMACLOUD_API_KEY`: find it [on LlamaCloud Dashboard](https://cloud.llamaindex.ai?utm_source=demo&utm_medium=notebookLM)

> **🌍 Regional Support**: LlamaCloud operates in multiple regions. If you're using a European region, configure it in your `.env` file:
>
> - For **North America**: This is the default region - no configuration necesary.
> - For **Europe (EU)**: Uncomment and set `LLAMACLOUD_REGION="eu"`

**4. Activate the Virtual Environment**

(on mac/unix)

```bash
source .venv/bin/activate
```

(on Windows):

```bash
.\.venv\Scripts\activate
```

**5. Create LlamaCloud Agent & Pipeline**

You will now execute two scripts to configure your backend agents and pipelines.

First, create the data extraction agent:

```bash
uv run tools/create_llama_extract_agent.py
```

Next, run the interactive setup wizard to configure your index pipeline.

> **⚡ Quick Start (Default OpenAI):**
> For the fastest setup, select **"With Default Settings"** when prompted. This will automatically create a pipeline using OpenAI's `text-embedding-3-small` embedding model.

> **🧠 Advanced (Custom Embedding Models):**
> To use a different embedding model, select **"With Custom Settings"** and follow the on-screen instructions.

Run the wizard with the following command:

```bash
uv run tools/create_llama_cloud_index.py
```

**6. Launch Backend Services**

This command will start the required Postgres and Jaeger containers.

```bas
```

---

## 4. notebooklm-py
- **Repository ID**: `REPO_NOTEBOOKLM_PY`
- **Primary Domain**: `Agentic LLM & Knowledge Graph`
- **Remote URL**: [https://github.com/teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/notebooklm-py`
- **Description**: Repository notebooklm-py located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/notebooklm-py

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# notebooklm-py
<p align="left">
  <img src="https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/notebooklm-py.png" alt="notebooklm-py logo" width="128">
</p>

**A Comprehensive Google Gemini Notebook Skill & Unofficial Python API.** Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.

> **Note (July 2026):** Google rebranded **NotebookLM** to **[Gemini Notebook](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)**. It remains the same standalone product (now also reachable inside the Gemini app), existing links redirect automatically, and this library drives the same underlying service and works unchanged. The package keeps the `notebooklm-py` name.

[![PyPI version](https://img.shields.io/pypi/v/notebooklm-py.svg)](https://pypi.org/project/notebooklm-py/)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://pypi.org/project/notebooklm-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml/badge.svg)](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml)
<p>
  <a href="https://trendshift.io/repositories/19116" target="_blank"><img src="https://trendshift.io/api/badge/repositories/19116" alt="teng-lin%2Fnotebooklm-py | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

**Source & Development**: <https://github.com/teng-lin/notebooklm-py>

> **⚠️ Unofficial Library - Use at Your Own Risk**
>
> This library uses **undocumented Google APIs** that can change without notice.
>
> - **Not affiliated with Google** - This is a community project
> - **APIs may break** - Google can change internal endpoints anytime
> - **Rate limits apply** - Heavy usage may be throttled
>
> Best for prototypes, research, and personal projects. See [Troubleshooting](docs/troubleshooting.md) for debugging tips.

## What You Can Build

🤖 **AI Agent Tools** - Integrate NotebookLM into Claude Code, Codex, and other LLM agents. Ships with a root [NotebookLM skill](SKILL.md) for GitHub and `npx skills add` discovery, local `notebooklm skill install` support for Claude Code and `.agents` skill directories, and repo-level Codex guidance in [`AGENTS.md`](AGENTS.md).

📚 **Research Automation** - Bulk-import sources (URLs, PDFs, YouTube, Google Drive), run web/Drive research queries with auto-import, and extract insights programmatically. Build repeatable research pipelines.

🎙️ **Content Generation** - Generate Audio Overviews (podcasts), videos, slide decks, quizzes, flashcards, infographics, data tables, mind maps, and study guides. Full control over formats, styles, and output.

📥 **Downloads & Export** - Download all generated artifacts locally (MP3, MP4, PDF, PNG, CSV, JSON, Markdown). Export to Google Docs/Sheets. **Features the web UI doesn't offer**: batch downloads, quiz/flashcard export in multiple formats, mind map JSON extraction.

## Use Cases & Recipes

NotebookLM is a **grounded** engine: Gemini does the heavy reading and answers from *your* sources with citations. The winning pattern is to let it do the expensive analysis while your agent (Claude Code, Codex, …) orchestrates and handles the final mile — using NotebookLM as a **zero-token 
```

---

## 5. open-notebook
- **Repository ID**: `REPO_OPEN_NOTEBOOK`
- **Primary Domain**: `Agentic LLM & Knowledge Graph`
- **Remote URL**: [https://github.com/lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/open-notebook`
- **Description**: Repository open-notebook located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/open-notebook

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<a id="readme-top"></a>

<!-- [![Contributors][contributors-shield]][contributors-url] -->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/lfnovo/open-notebook">
    <img src="docs/assets/hero.svg" alt="Logo">
  </a>

  <h3 align="center">Open Notebook</h3>

  <p align="center">
    An open source, privacy-focused alternative to Google's Notebook LM!
    <br /><strong>Join our <a href="https://discord.gg/37XJPXfz2w">Discord server</a> for help, to share workflow ideas, and suggest features!</strong>
    <br />
    <a href="https://www.open-notebook.ai"><strong>Checkout our website »</strong></a>
    <br />
    Follow <a href="https://x.com/lfnovo">@lfnovo on X</a> for updates
    <br />
    <br />
    <a href="docs/0-START-HERE/index.md">📚 Get Started</a>
    ·
    <a href="docs/3-USER-GUIDE/index.md">📖 User Guide</a>
    ·
    <a href="docs/2-CORE-CONCEPTS/index.md">✨ Features</a>
    ·
    <a href="docs/1-INSTALLATION/index.md">🚀 Deploy</a>
  </p>
</div>

<p align="center">
<a href="https://trendshift.io/repositories/14536" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14536" alt="lfnovo%2Fopen-notebook | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<div align="center">
  <!-- Keep these links. Translations will automatically update with the README. -->
  <a href="https://zdoc.app/de/lfnovo/open-notebook">Deutsch</a> | 
  <a href="https://zdoc.app/es/lfnovo/open-notebook">Español</a> | 
  <a href="https://zdoc.app/fr/lfnovo/open-notebook">français</a> | 
  <a href="https://zdoc.app/ja/lfnovo/open-notebook">日本語</a> | 
  <a href="https://zdoc.app/ko/lfnovo/open-notebook">한국어</a> | 
  <a href="https://zdoc.app/pt/lfnovo/open-notebook">Português</a> | 
  <a href="https://zdoc.app/ru/lfnovo/open-notebook">Русский</a> | 
  <a href="https://zdoc.app/zh/lfnovo/open-notebook">中文</a>
</div>

## A private, multi-model, 100% local, full-featured alternative to Notebook LM

![New Notebook](docs/assets/asset_list.png)

In a world dominated by Artificial Intelligence, having the ability to think 🧠 and acquire new knowledge 💡, is a skill that should not be a privilege for a few, nor restricted to a single provider.

**Open Notebook empowers you to:**
- 🔒 **Control your data** - Keep your research private and secure
- 🤖 **Choose your AI models** - Support for 18+ providers including OpenAI, Anthropic, Ollama, LM Studio, and more
- 📚 **Organize multi-modal content** - PDFs, videos, audio, web pages, and more
- 🎙️ **Generate professional podcasts** - Advanced multi-speaker podcast generation
- 🔍 **Search intelligently** - Full-text and vector search across all your content
- 💬 **Chat with context** - AI conversations powered by your research
- 🌐 **Multi-language UI** - English, Portuguese, Chinese (Simplified & Traditional), Japanese, Russian, and Bengali support

Learn more about our project at [https://www.open-notebook.ai](https://www.open-notebook.ai)

---

## 🆚 Open Notebook vs Google Notebook LM

| Feature | Open Notebook | Google Notebook LM | Advantage |
|---------|---------------|--------------------|-----------|
| **Privacy & Control** | Self-hosted, your data | Google cloud only | Complete data sovereignty |
| **AI Provider Choice** |
```

---

## 6. gemini-spark-cortex
- **Repository ID**: `REPO_GEMINI_SPARK_CORTEX`
- **Primary Domain**: `Agentic LLM & Knowledge Graph`
- **Remote URL**: [https://github.com/rajon369963-del/gemini-spark-cortex](https://github.com/rajon369963-del/gemini-spark-cortex)
- **Local Disk Path**: `https://github.com/rajon369963-del/gemini-spark-cortex`
- **Description**: ⚡ Autonomous Gemini Spark Git Operations Hub for rajon369963-del

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Agentic LLM & Knowledge Graph.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 7. air1-fable5-colab
- **Repository ID**: `REPO_AIR1_FABLE5_COLAB`
- **Primary Domain**: `Agentic LLM & Knowledge Graph`
- **Remote URL**: [https://github.com/rajon369963-del/air1-fable5-colab](https://github.com/rajon369963-del/air1-fable5-colab)
- **Local Disk Path**: `https://github.com/rajon369963-del/air1-fable5-colab`
- **Description**: AIR1 Fable-5 LLM Server - One click Colab deploy

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Agentic LLM & Knowledge Graph.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 8. AutoHedge
- **Repository ID**: `REPO_CURATED_AUTOHEDGE`
- **Primary Domain**: `AI Agents & Swarms`
- **Remote URL**: [https://github.com/The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge)
- **Local Disk Path**: `remote:https://github.com/The-Swarm-Corporation/AutoHedge`
- **Description**: AI-driven hedge fund framework using multi-agent swarms to handle strategy, portfolio optimization, and risk autonomously.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for AI Agents & Swarms.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 9. TradingAgents
- **Repository ID**: `REPO_CURATED_TRADINGAGENTS`
- **Primary Domain**: `AI Agents & Swarms`
- **Remote URL**: [https://github.com/tauricresearch/tradingagents](https://github.com/tauricresearch/tradingagents)
- **Local Disk Path**: `remote:https://github.com/tauricresearch/tradingagents`
- **Description**: Multi-agent framework supporting GPT-5.5, Claude 4.6, and Gemini 3.5 for financial trading simulations and automated decision-making.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for AI Agents & Swarms.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 10. FinRobot
- **Repository ID**: `REPO_CURATED_FINROBOT`
- **Primary Domain**: `Financial LLM Agents`
- **Remote URL**: [https://github.com/AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot)
- **Local Disk Path**: `remote:https://github.com/AI4Finance-Foundation/FinRobot`
- **Description**: Open-source AI agent platform using LLMs for comprehensive financial analysis, equity research, and algorithmic trading execution.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Financial LLM Agents.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 11. Fenix
- **Repository ID**: `REPO_CURATED_FENIX`
- **Primary Domain**: `Multi-Agent Orchestration`
- **Remote URL**: [https://github.com/fenix-trading/fenix](https://github.com/fenix-trading/fenix)
- **Local Disk Path**: `remote:https://github.com/fenix-trading/fenix`
- **Description**: Advanced multi-agent orchestration platform for crypto and equity algorithmic trading with deterministic guardrails.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Multi-Agent Orchestration.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

