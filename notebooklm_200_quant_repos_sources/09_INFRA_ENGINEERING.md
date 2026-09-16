# 🏛️ NotebookLM Quant Source: 09_INFRA_ENGINEERING

**Total Grounded Repositories in this Volume**: 60
**Compilation Date**: September 16, 2026

---

## 1. youtube-transcriber
- **Repository ID**: `REPO_YOUTUBE_TRANSCRIBER`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/lifesized/youtube-transcriber](https://github.com/lifesized/youtube-transcriber)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/youtube-transcriber`
- **Description**: Repository youtube-transcriber located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/youtube-transcriber

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# YouTube Transcriber

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

**YouTube & Spotify podcast to LLM-ready transcript in one click. Runs locally, costs nothing.**


https://github.com/user-attachments/assets/32491284-5c78-4a74-a580-ff3a8c256243




**Don't want to install anything?** A hosted version is coming soon — no setup required. **[Join the waitlist →](https://waitlist-site-alpha.vercel.app)**

## Get Running in 60 Seconds

```bash
git clone https://github.com/lifesized/youtube-transcriber.git
cd youtube-transcriber
npm run setup
npm run dev
```

Open [http://localhost:19720](http://localhost:19720) — paste a YouTube or Spotify podcast URL, hit Transcribe, done.

> **Mac/Linux only for auto-setup.** Windows: use WSL or follow the [Manual Installation](#manual-installation) section.

> `npm run setup` installs all dependencies (yt-dlp, ffmpeg, Whisper, MLX on Apple Silicon) and configures everything automatically. Requires Node.js 20.19+, 22.12+, or 24+, Python 3.8+, and a package manager (Homebrew / apt / dnf / pacman).

## Chrome Extension
<img width="375" height="565" alt="CleanShot 2026-03-17 at 22 53 31@2x" src="https://github.com/user-attachments/assets/d4bccf92-9941-46cc-b4f4-b7bbc3454ff7" />


https://github.com/user-attachments/assets/081c8d90-a6e1-4b4d-b6cd-bc8787bc0a3b


Transcribe any YouTube video or Spotify podcast episode directly from your browser without leaving the page. The extension opens as a persistent side panel — it stays open as you navigate between videos and detects each one automatically.

The extension works in two modes:

- **Cloud** (default) — hosted transcription for private beta users. Enter your API key in extension settings and go. No local setup needed.
- **Self-hosted** — connect to your local instance at `localhost:19720`. Switch to "Self-hosted" in extension settings.

### Install from Chrome Web Store

> **Note:** The extension is not yet on the Chrome Web Store. Install it manually in a few steps while we go through the review process.

### Install from source (for self-hosted or development)

1. Make sure the local service is running (`npm run dev`)
2. Open Chrome and go to `chrome://extensions`
3. Enable **Developer mode** (toggle, top right)
4. Click **Load unpacked**
5. Select the `extension/` folder inside this repo
6. Open extension settings and switch mode to **Self-hosted**
7. Click the YouTube Transcriber icon in your toolbar to open the side panel

### Usage

Navigate to any YouTube video or Spotify episode, open the side panel, and click **Transcribe**. In cloud mode, transcripts open in the hosted app. In self-hosted mode, they open in the local web app at `http://localhost:19720`.

### Connectors — send transcripts to Obsidian or Notion

Each transcript row's `⋯` menu can push the result to an external app. Connect once in **Settings → Connectors**, then use the menu on any recent transcript.

**Obsidian** — works in both cloud and self-hosted mode. Stateless: the extension builds an `obsidian://new?...` URL on your machine and hands it to the desktop app. Nothing transcript-related leaves the device.

1. Install [Obsidian](https://obsidian.md) and open your vault.
2. In the extension panel: gear icon → **Connectors** → toggle **Obsidian** on.
3. Type your vault name **exactly** as it appears in Obsidian's sidebar (case-sensitive).
4. (Recommended for long transcripts) Install the [Advanced URI](https://
```

---

## 2. youtube-workflows
- **Repository ID**: `REPO_YOUTUBE_WORKFLOWS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/ZeroPointRepo/youtube-workflows](https://github.com/ZeroPointRepo/youtube-workflows)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/youtube-workflows`
- **Description**: Repository youtube-workflows located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/youtube-workflows

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# YouTube Workflows ⚙️

> Ready-to-import automation workflows that turn YouTube videos into transcripts, summaries, and structured data, powered by [TranscriptAPI](https://transcriptapi.com).

Drop these into [n8n](https://n8n.io) (more platforms coming) and you've got a working pipeline in minutes: **YouTube → transcript → AI summary → wherever you want it** (Notion, Sheets, Slack, your database). Just one fast, reliable API call, not a brittle DIY pipeline you have to build and babysit. Powered by [TranscriptAPI](https://transcriptapi.com), the same backend behind [YouTubeToTranscript.com](https://youtubetotranscript.com).

**Free tier · No credit card · 100 credits on signup**

[TranscriptAPI.com](https://transcriptapi.com) · [API Docs](https://transcriptapi.com/docs/api/) · [Agent Skills](https://github.com/ZeroPointRepo/youtube-skills) · [MCP Server](https://github.com/ZeroPointRepo/youtube-mcp)

---

## What's Inside

| # | Workflow | Platform | What it does |
|---|----------|----------|--------------|
| 01 | [Single Video → Transcript → AI Summary](n8n/01-single-video-transcript-summary) | n8n | Paste one YouTube URL, get a clean transcript and a 5-bullet AI summary. The simplest way to see TranscriptAPI work. |
| 02 | [Channel → Latest Videos → Summaries → Notion](n8n/02-channel-latest-videos-to-notion) | n8n | Every day, grab a channel's newest videos, transcribe each, summarize with an LLM, and append a row to Notion. Set-and-forget content monitoring. |
| 03 | [Video → Transcript → SEO Blog-Post Draft](n8n/03-video-to-seo-blog-post) | n8n | Repurpose one video into a publish-ready blog draft, SEO title, meta description, slug, tags, and a full Markdown article. For content marketers. |
| 04 | [Playlist / Channel → Transcripts → RAG Chunks](n8n/04-playlist-to-rag-chunks) | n8n | Transcribe a whole playlist and emit clean, overlapping `{id, text, metadata}` chunks ready to embed into a vector DB. For RAG / agent builders. |
| 05 | [New-Upload Monitor → Key Points → Slack](n8n/05-new-upload-monitor-slack-digest) | n8n | Watch a channel and get a Slack digest of key takeaways whenever it posts something new. For teams tracking channels/competitors. |
| 06 | [Video → Transcript → Translate → Multilingual Summary](n8n/06-video-translate-multilingual-summary) | n8n | Translate + summarize any video into a target language (translated title, bullet summary, key topics). For global creators and localizers. |
| 07 | [Multi-Video Topic Researcher → Research Brief](n8n/07-multi-video-topic-researcher) | n8n | Search a topic, transcribe the top results, and synthesize a structured research brief (themes, consensus, disagreements). For research/AI. |
| 08 | [Video → LinkedIn Post](n8n/08-video-to-linkedin-post) | n8n | Repurpose one video into a ready-to-post LinkedIn update, hook, body, CTA, hashtags. For content repurposers. |
| 09 | [Video → X (Twitter) Thread](n8n/09-video-to-x-thread) | n8n | Repurpose one video into a numbered 10-tweet X thread (hook → ideas → CTA). For content repurposers. |
| 10 | [Brand-Mention Monitor → Slack Digest](n8n/10-brand-mention-monitor-slack) | n8n | Daily search for a brand/keyword, transcribe the new results, and post a Slack digest of mentions. For marketers / competitive intel. |
| 11 | [Video → Content Classifier](n8n/11-video-to-content-classifier) | n8n | Auto-tag a video with category, content type, topics, and audience, structured for an Airtable/Notion content database. |
| 12 | [Video → Newsl
```

---

## 3. insights-lm-public
- **Repository ID**: `REPO_INSIGHTS_LM_PUBLIC`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/theaiautomators/insights-lm-public](https://github.com/theaiautomators/insights-lm-public)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/insights-lm-public`
- **Description**: Repository insights-lm-public located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/harvest_wheels/insights-lm-public

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<p align="center">
  <img src="https://www.theaiautomators.com/wp-content/uploads/2025/07/Group-2651.svg" alt="InsightsLM Logo" width="600"/>
</p>


# InsightsLM: The Open Source NotebookLM Alternative

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/theaiautomators/insights-lm-public?style=social)](https://github.com/theaiautomators/insights-lm-public/stargazers)
[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20the%20Build-red)](https://www.youtube.com/watch?v=Nla35It-xfc)

> What if the power of a tool like NotebookLM wasn't locked away in a closed system? What if you could build a private, self-hosted alternative that can be customized for your business needs, all without writing a single line of code?

That's exactly what we've done with **InsightsLM**. This project is an open-source, self-hostable alternative to NotebookLM. It's designed to be a powerful AI research tool that grounds its responses exclusively in the sources you provide, making it a reliable window into your company's knowledge base.


## About The Project

NotebookLM is one of the most powerful AI research tools available today. However, its closed-source nature limits its potential for customization and private hosting. InsightsLM was created to bridge this gap.

This isn't just a basic prototype. It's a robust application with some killer features, developed using a "vibe-coding" approach with Loveable for the Javascript frontend and a powerful backend combination of Supabase and N8N.

We are open-sourcing InsightsLM so you can install it, customize it, improve it, and even commercialize it. The ability to deploy AI agents grounded in a company's specific knowledge (a concept known as Retrieval-Augmented Generation or RAG) represents one of the biggest commercial opportunities for generative AI today.


<p align="center">
  <img src="https://www.theaiautomators.com/wp-content/uploads/2025/07/Group-2652.png" alt="The AI Automators Logo" width="500"/>
</p>


## Fully Local Version

This version of InsightsLM relies on cloud AI services like OpenAI and Gemini.

If you'd like to setup a fully local version of this that uses Ollama and Qwen3 along with Whisper and CoquiTTS, then check out our other repo below

[Fully Local InsightsLM](https://github.com/theaiautomators/insights-lm-local-package)

## Join Our Community

If you're interested in learning how to customize InsightsLM or build similar applications, join our community, The AI Automators.

https://www.theaiautomators.com/


## Key Features

* **Chat with Your Documents:** Upload your documents and get instant, context-aware answers.
* **Verifiable Citations:** Jump directly to the source of the information to ensure the AI isn't hallucinating.
* **Podcast Generation:** Create audio summaries and discussions from your source materials, just like in NotebookLM.
* **Private and Self-Hosted:** Maintain complete control over your data by hosting it yourself. Use local models if you wish.
* **Customizable and Extensible:** Built with modern, accessible tools, making it easy to tailor to your specific needs.


## Demo & Walkthrough

For a complete demonstration of InsightsLM, an overview of its architecture, and a step-by-step guide on how to set it up, check out our YouTube video:

### Original Video

<p>
  <a target="_blank" href="https://www.youtube.com/watch?v=Nla35It-xfc"><img src="http
```

---

## 4. gbrain
- **Repository ID**: `REPO_GBRAIN`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/garrytan/gbrain.git](https://github.com/garrytan/gbrain.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/gbrain`
- **Description**: Repository gbrain located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/gbrain

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# GBrain

**Search gives you raw pages. GBrain gives you the answer.** It's the brain layer your AI agent has been missing — the only one that does synthesis, graph traversal, and gap analysis in one box. Run a full autonomous agent on top of it, or just wire it into Claude Code or Codex as a supercharged retrieval layer in one command; either way your coding agent stops being amnesiac about everything that isn't code.

I'm Garry Tan, President and CEO of Y Combinator. I built GBrain to run my own AI agents. It's the production brain behind my OpenClaw and Hermes deployments: **155,795 pages, 24,589 people, 5,340 companies**, 66 cron jobs running autonomously. My agent ingests meetings, emails, tweets, voice calls, and original ideas while I sleep. It enriches every person and company it encounters. It fixes its own citations and consolidates memory overnight. I wake up smarter than when I went to bed — and so will you.

**It works as a company brain too.** Each person on the team gets their own slice of the brain, scoped by login. When you query, you only see what you're allowed to see — never another person's notes, never another team's data. We fuzz-tested this across every way you can read the brain (search, list, lookup, multi-source reads) and got zero leaks. Drop GBrain in as your team's shared institutional memory — the [company-brain](https://www.ycombinator.com/rfs#company-brain) shape on YC's Request for Startups. If you're building in that space, you might as well build on this. **[Tutorial: set up GBrain as your company brain →](docs/tutorials/company-brain.md)**

Lots of personal-knowledge systems give you keyword matching and grep in a box. GBrain does that, and adds two things nobody else ships together:

- **A synthesis layer that gives you the actual answer.** Synthesized, well-cited prose across people, companies, deals, and ideas. Not "here are 10 chunks that mention your query"; an actual answer with citations and an explicit note on what the brain doesn't know yet. The gap analysis is the part that changes how you use the brain.
- **A self-wiring knowledge graph.** Every page write extracts entity refs and creates typed edges (`attended`, `works_at`, `invested_in`, `founded`, `advises`) with zero LLM calls. Ask "who works at Acme AI?" or "what did Bob invest in this quarter?" and get answers vector search alone can't reach. Benchmarked: **P@5 49.1%, R@5 97.9%** on a 240-page Opus-generated rich-prose corpus, **+31.4 points P@5** over its graph-disabled variant and over ripgrep-BM25 + vector-only RAG by a similar margin. Full BrainBench scorecards live in the sibling [gbrain-evals](https://github.com/garrytan/gbrain-evals) repo.

The point of building a 150K-page brain is to use it as a strategic moat. To never lose context. To query what's in your own head without re-reading it. The brain layer is what makes the moat usable. The 24/7 dream cycle is what keeps it sharp. Both run on your hardware, your DB, your keys.

It's easier to ship a daemon that runs 24/7 to ingest, enrich, and consolidate than it is to keep an agent in chat working hard. GBrain is that daemon, generalized. Install in 30 minutes. Your agent does the work. As my personal agent gets smarter, so does yours.

> **~15 minutes to a working personal agent** on the recommended Codex / Claude Code path (mostly a short interview); ~30 minutes for the always-on OpenClaw / Hermes setup. Database ready in 2 seconds either way (PGLite, no server).

> **LLMs:
```

---

## 5. garrytan_gbrain
- **Repository ID**: `REPO_GARRYTAN_GBRAIN`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/garrytan/gbrain.git](https://github.com/garrytan/gbrain.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/garrytan_gbrain`
- **Description**: Repository garrytan_gbrain located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/garrytan_gbrain

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 6. briancaffey_hermes-otel
- **Repository ID**: `REPO_BRIANCAFFEY_HERMES_OTEL`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/briancaffey/hermes-otel.git](https://github.com/briancaffey/hermes-otel.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/briancaffey_hermes-otel`
- **Description**: Repository briancaffey_hermes-otel located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/briancaffey_hermes-otel

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# hermes-otel

OpenTelemetry plugin for [Hermes Agent](https://github.com/nousresearch/hermes-agent). Automatically exports LLM tool calls, model invocations, and API requests as OTel spans to any OTLP-compatible backend.

## Backends

Tested with:
- **[Phoenix](https://github.com/Arize-ai/phoenix)** (local or cloud) — traces + metrics
- **[Langfuse](https://langfuse.com/docs)** (cloud or self-hosted) — traces only
- **[LangSmith](https://smith.langchain.com/)** (LangChain's tracing platform) — traces only
- **[SigNoz](https://signoz.io)** (cloud or self-hosted) — traces + metrics + logs
- **[Jaeger](https://www.jaegertracing.io)** (local) — traces only
- **[Grafana Tempo](https://grafana.com/oss/tempo/)** (local or Grafana Cloud) — traces only
- **[Grafana LGTM](https://github.com/grafana/docker-otel-lgtm)** (local) — traces + metrics + logs
- **[Uptrace](https://uptrace.dev)** (self-hosted) — traces + metrics + logs
- **[OpenObserve](https://openobserve.ai)** (self-hosted) — traces + metrics + logs
- **[Parseable](https://www.parseable.com)** (cloud or self-hosted) — traces + metrics + logs + agent observability
- **[Honeycomb](https://www.honeycomb.io/)** (cloud) — traces + metrics + logs — see [HONEYCOMB.md](HONEYCOMB.md)
- **[W&B Weave](https://docs.wandb.ai/weave/)** (cloud / Dedicated Cloud / self-managed) — traces only

Any OTLP HTTP endpoint should work.

- For Phoenix see [docker-compose/phoenix.yaml](docker-compose/phoenix.yaml)
- For Langfuse see [https://langfuse.com/self-hosting/deployment/docker-compose](https://langfuse.com/self-hosting/deployment/docker-compose)
- For Langsmith see [https://smith.langchain.com/](https://smith.langchain.com/)
- For SigNoz see [docker-compose/signoz/](docker-compose/signoz/) (includes the upstream stack + port-remap notes)
- For Grafana LGTM see [docker-compose/lgtm.yaml](docker-compose/lgtm.yaml) and [docker-compose/lgtm/README.md](docker-compose/lgtm/README.md)
- For Uptrace see [docker-compose/uptrace.yaml](docker-compose/uptrace.yaml) and [docker-compose/uptrace/README.md](docker-compose/uptrace/README.md)
- For OpenObserve see [docker-compose/openobserve.yaml](docker-compose/openobserve.yaml) and [docker-compose/openobserve/README.md](docker-compose/openobserve/README.md)
- For Parseable see the [Hermes integration guide](https://www.parseable.com/docs/ingest-data/ai-agents/hermes)

## Installation

```
hermes plugins install briancaffey/hermes-otel/hermes_otel
```

The trailing `/hermes_otel` is the plugin package inside this repo — Hermes installs that
subdirectory (~40 files) rather than the whole repository, so docs, tests and the example
Compose stacks never land in `~/.hermes/plugins/`. It unpacks to `~/.hermes/plugins/hermes_otel/`
either way, and Hermes auto-discovers it via `plugin.yaml`.

The OTel dependencies must then be installed into the **hermes-agent virtual environment**
(where `hermes` itself runs) — Hermes never installs plugin dependencies for you:

```bash
# Install OTel runtime dependencies into the hermes-agent venv
~/git/hermes-agent/venv/bin/pip install \
  opentelemetry-api \
  opentelemetry-sdk \
  opentelemetry-exporter-otlp-proto-http

# Optional: for LangSmith time-ordered run IDs
~/git/hermes-agent/venv/bin/pip install langsmith
```

The same list ships with the plugin, so this is equivalent:

```bash
~/git/hermes-agent/venv/bin/pip install -r ~/.hermes/plugins/hermes_otel/requirements.txt
```

Working from a clone instead? An editable install of the re
```

---

## 7. MAYA-Platform_MAYA-Memory-Lane
- **Repository ID**: `REPO_MAYA_PLATFORM_MAYA_MEMORY_LANE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/MAYA-Platform/MAYA-Memory-Lane.git](https://github.com/MAYA-Platform/MAYA-Memory-Lane.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/MAYA-Platform_MAYA-Memory-Lane`
- **Description**: Repository MAYA-Platform_MAYA-Memory-Lane located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/MAYA-Platform_MAYA-Memory-Lane

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# MAYA Memory Lane

**Your memory, on a chain, in your pocket.**

Memory Lane is a local-first, tamper-evident memory library. Every session leaves a sealed record with a SHA-256 fingerprint, every six records fold into one shelf block, and each shelf block carries the fingerprint of the one before it. The result is a chain of linked records you own, organized into shelves and volumes on your own machine, verified in seconds, and resumed with a single phrase.

**You own the memory. The chain keeps it honest.**

Memory Lane is a web interface over a plain-file library. No cloud, no account, no telemetry. The files are the source of truth and the interface is a window over them. If the interface disappears, the library is still right there on disk.

> **Your memory stays local.** Memory Lane runs entirely on the machine that runs it. Nothing is sent to a cloud service, no account is required, and no data leaves your machine. It is not a hosted service and carries no production SLA.

**Where your data actually lives.** A Memory Lane library is just a folder: a `MANIFEST.json` plus a `shelves/` tree of plain markdown block files. Point the server at any directory (`MEMORY_LANE_LIBRARY=/path/to/library`) and that directory is your memory — no hidden database and nothing written outside that folder. (The optional embeddings lane caches its vectors as a `.embeddings-*.json` dotfile inside the same library directory.) The bundled `empty-library/` is the blank default. Everything is human-readable markdown you can open in any editor.

![Memory Lane](docs/images/memory-lane-public.png)

*Shown with the bundled sample loaded via the "Load sample library" button. A fresh clone opens blank, your lane is empty until you seal records. The sample is fabricated demo data that never touches your machine.*

## What it does

- **Linked memory records**, every session becomes a sealed block with a SHA-256 fingerprint, and every block carries the fingerprint of the block before it. Change anything and the break is visible
- **Automatic ingestion**, drop a transcript into the inbox (or POST it to the API) and Memory Lane extracts durable facts, seals a chain-linked block, and files it, no human step in between
- **6→1 compaction**, six session records fold into one shelf block, so the library grows one shelf per six sessions instead of one file per session
- **Chain verification**, recomputes every fingerprint and walks the links, then tells you plainly what you need to know: intact, unverifiable, or needs attention. The boundary, stated honestly: the manifest is the anchor of trust, so verification catches modification by anyone who cannot rewrite the manifest too. That is integrity detection, not an externally anchored audit log, the chain proves nothing was changed behind your back while you hold the files, it does not prove provenance to a third party
- **Resume phrase as your key**, one string crosses sessions. The library holds everything else
- **Full-text search**, plain-text search across every record body, boosted by extracted facts
- **Ask your memory**, ask a natural-language question and get an answer, exact hits return instantly for free, and when your wording doesn't match, a model reads the retrieved evidence and answers honestly (or says it doesn't know). No invented facts
- **Deterministic export**, a byte-stable JSON bundle of the whole library, one click
- **Zero dependencies**, Node's built-in runtime and test runner, no npm install requi
```

---

## 8. hermes-otel
- **Repository ID**: `REPO_HERMES_OTEL`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/briancaffey/hermes-otel.git](https://github.com/briancaffey/hermes-otel.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/hermes-otel`
- **Description**: Repository hermes-otel located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/hermes-otel

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# hermes-otel

OpenTelemetry plugin for [Hermes Agent](https://github.com/nousresearch/hermes-agent). Automatically exports LLM tool calls, model invocations, and API requests as OTel spans to any OTLP-compatible backend.

## Backends

Tested with:
- **[Phoenix](https://github.com/Arize-ai/phoenix)** (local or cloud) — traces + metrics
- **[Langfuse](https://langfuse.com/docs)** (cloud or self-hosted) — traces only
- **[LangSmith](https://smith.langchain.com/)** (LangChain's tracing platform) — traces only
- **[SigNoz](https://signoz.io)** (cloud or self-hosted) — traces + metrics + logs
- **[Jaeger](https://www.jaegertracing.io)** (local) — traces only
- **[Grafana Tempo](https://grafana.com/oss/tempo/)** (local or Grafana Cloud) — traces only
- **[Grafana LGTM](https://github.com/grafana/docker-otel-lgtm)** (local) — traces + metrics + logs
- **[Uptrace](https://uptrace.dev)** (self-hosted) — traces + metrics + logs
- **[OpenObserve](https://openobserve.ai)** (self-hosted) — traces + metrics + logs
- **[Parseable](https://www.parseable.com)** (cloud or self-hosted) — traces + metrics + logs + agent observability
- **[Honeycomb](https://www.honeycomb.io/)** (cloud) — traces + metrics + logs — see [HONEYCOMB.md](HONEYCOMB.md)
- **[W&B Weave](https://docs.wandb.ai/weave/)** (cloud / Dedicated Cloud / self-managed) — traces only

Any OTLP HTTP endpoint should work.

- For Phoenix see [docker-compose/phoenix.yaml](docker-compose/phoenix.yaml)
- For Langfuse see [https://langfuse.com/self-hosting/deployment/docker-compose](https://langfuse.com/self-hosting/deployment/docker-compose)
- For Langsmith see [https://smith.langchain.com/](https://smith.langchain.com/)
- For SigNoz see [docker-compose/signoz/](docker-compose/signoz/) (includes the upstream stack + port-remap notes)
- For Grafana LGTM see [docker-compose/lgtm.yaml](docker-compose/lgtm.yaml) and [docker-compose/lgtm/README.md](docker-compose/lgtm/README.md)
- For Uptrace see [docker-compose/uptrace.yaml](docker-compose/uptrace.yaml) and [docker-compose/uptrace/README.md](docker-compose/uptrace/README.md)
- For OpenObserve see [docker-compose/openobserve.yaml](docker-compose/openobserve.yaml) and [docker-compose/openobserve/README.md](docker-compose/openobserve/README.md)
- For Parseable see the [Hermes integration guide](https://www.parseable.com/docs/ingest-data/ai-agents/hermes)

## Installation

```
hermes plugins install briancaffey/hermes-otel/hermes_otel
```

The trailing `/hermes_otel` is the plugin package inside this repo — Hermes installs that
subdirectory (~40 files) rather than the whole repository, so docs, tests and the example
Compose stacks never land in `~/.hermes/plugins/`. It unpacks to `~/.hermes/plugins/hermes_otel/`
either way, and Hermes auto-discovers it via `plugin.yaml`.

The OTel dependencies must then be installed into the **hermes-agent virtual environment**
(where `hermes` itself runs) — Hermes never installs plugin dependencies for you:

```bash
# Install OTel runtime dependencies into the hermes-agent venv
~/git/hermes-agent/venv/bin/pip install \
  opentelemetry-api \
  opentelemetry-sdk \
  opentelemetry-exporter-otlp-proto-http

# Optional: for LangSmith time-ordered run IDs
~/git/hermes-agent/venv/bin/pip install langsmith
```

The same list ships with the plugin, so this is equivalent:

```bash
~/git/hermes-agent/venv/bin/pip install -r ~/.hermes/plugins/hermes_otel/requirements.txt
```

Working from a clone instead? An editable install of the re
```

---

## 9. MAYA-Memory-Lane
- **Repository ID**: `REPO_MAYA_MEMORY_LANE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/MAYA-Platform/MAYA-Memory-Lane.git](https://github.com/MAYA-Platform/MAYA-Memory-Lane.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/MAYA-Memory-Lane`
- **Description**: Repository MAYA-Memory-Lane located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/MAYA-Memory-Lane

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# MAYA Memory Lane

**Your memory, on a chain, in your pocket.**

Memory Lane is a local-first, tamper-evident memory library. Every session leaves a sealed record with a SHA-256 fingerprint, every six records fold into one shelf block, and each shelf block carries the fingerprint of the one before it. The result is a chain of linked records you own, organized into shelves and volumes on your own machine, verified in seconds, and resumed with a single phrase.

**You own the memory. The chain keeps it honest.**

Memory Lane is a web interface over a plain-file library. No cloud, no account, no telemetry. The files are the source of truth and the interface is a window over them. If the interface disappears, the library is still right there on disk.

> **Your memory stays local.** Memory Lane runs entirely on the machine that runs it. Nothing is sent to a cloud service, no account is required, and no data leaves your machine. It is not a hosted service and carries no production SLA.

**Where your data actually lives.** A Memory Lane library is just a folder: a `MANIFEST.json` plus a `shelves/` tree of plain markdown block files. Point the server at any directory (`MEMORY_LANE_LIBRARY=/path/to/library`) and that directory is your memory — no hidden database and nothing written outside that folder. (The optional embeddings lane caches its vectors as a `.embeddings-*.json` dotfile inside the same library directory.) The bundled `empty-library/` is the blank default. Everything is human-readable markdown you can open in any editor.

![Memory Lane](docs/images/memory-lane-public.png)

*Shown with the bundled sample loaded via the "Load sample library" button. A fresh clone opens blank, your lane is empty until you seal records. The sample is fabricated demo data that never touches your machine.*

## What it does

- **Linked memory records**, every session becomes a sealed block with a SHA-256 fingerprint, and every block carries the fingerprint of the block before it. Change anything and the break is visible
- **Automatic ingestion**, drop a transcript into the inbox (or POST it to the API) and Memory Lane extracts durable facts, seals a chain-linked block, and files it, no human step in between
- **6→1 compaction**, six session records fold into one shelf block, so the library grows one shelf per six sessions instead of one file per session
- **Chain verification**, recomputes every fingerprint and walks the links, then tells you plainly what you need to know: intact, unverifiable, or needs attention. The boundary, stated honestly: the manifest is the anchor of trust, so verification catches modification by anyone who cannot rewrite the manifest too. That is integrity detection, not an externally anchored audit log, the chain proves nothing was changed behind your back while you hold the files, it does not prove provenance to a third party
- **Resume phrase as your key**, one string crosses sessions. The library holds everything else
- **Full-text search**, plain-text search across every record body, boosted by extracted facts
- **Ask your memory**, ask a natural-language question and get an answer, exact hits return instantly for free, and when your wording doesn't match, a model reads the retrieved evidence and answers honestly (or says it doesn't know). No invented facts
- **Deterministic export**, a byte-stable JSON bundle of the whole library, one click
- **Zero dependencies**, Node's built-in runtime and test runner, no npm install requi
```

---

## 10. hermes-lcm
- **Repository ID**: `REPO_HERMES_LCM`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/stephenschoettler/hermes-lcm.git](https://github.com/stephenschoettler/hermes-lcm.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/hermes-lcm`
- **Description**: Repository hermes-lcm located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/plugins_and_repos/hermes-lcm

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<p align="center">
  <img src="docs/banner.png" alt="HERMES-LCM" width="800">
</p>

[![CI](https://github.com/stephenschoettler/hermes-lcm/actions/workflows/ci.yml/badge.svg)](https://github.com/stephenschoettler/hermes-lcm/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/stephenschoettler/hermes-lcm)](https://github.com/stephenschoettler/hermes-lcm/releases)
[![Python 3.11-3.14](https://img.shields.io/badge/Python-3.11--3.14-3776AB?logo=python&logoColor=white)](https://github.com/stephenschoettler/hermes-lcm/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Lossless Context Management plugin for [Hermes Agent](https://github.com/NousResearch/hermes-agent).**

> Bounded context, unbounded memory. Nothing is ever lost.

`hermes-lcm` replaces one-shot active-context compression with a SQLite-backed,
DAG-based context engine. It keeps the live prompt bounded, preserves raw
messages, and gives the agent tools to recover exact detail after compaction.

Based on the [LCM paper](https://papers.voltropy.com/LCM) by Ehrlich & Blackman
(Voltropy PBC, Feb 2026). Inspired by
[lossless-claw](https://github.com/martian-engineering/lossless-claw) for
OpenClaw. For an interactive visualization of the LCM idea, see
[losslesscontext.ai](https://losslesscontext.ai/).

## Table of contents

- [What it does](#what-it-does)
- [LCM vs built-in compression](#lcm-vs-built-in-compression)
- [Quick start](#quick-start)
- [Commands and tools](#commands-and-tools)
- [Recall skill and policy](#recall-skill-and-policy)
- [Configuration](#configuration)
- [Retrieval contract](#retrieval-contract)
- [OpenClaw/lossless-claw import](#openclawlossless-claw-import)
- [Troubleshooting](#troubleshooting)
- [Architecture](#architecture)
- [How it works](#how-it-works)
- [Documentation](#documentation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## What it does

Hermes Agent's built-in compressor is a practical continuity layer: when the
prompt crosses its configured threshold, it prunes older tool results, asks an
auxiliary model to summarize the middle/older conversation, and rebuilds the
active prompt from that summary plus a protected recent tail. The original
session rows can still live in Hermes `state.db` and remain searchable through
host tools such as `session_search`, but the model's active context no longer
contains the compacted turns verbatim or a structured drill-down path back to
them.

`hermes-lcm` instead:

1. **Persists messages** in a plugin-local SQLite store with FTS metadata.
2. **Compacts older context** into depth-aware summary nodes.
3. **Condenses summaries** into a hierarchical DAG as they accumulate.
4. **Assembles active context** from system prompt, highest-value summaries, and
   the protected fresh tail.
5. **Provides recall tools** so agents can search, inspect, and expand compacted
   material without flooding the main prompt.

Nothing is lost in normal operation. Raw messages stay recoverable in bounded
pages, summaries retain source lineage, and oversized externalized payloads keep
stable refs for later expansion.

<p align="center">
  <img src="docs/standard_compression.png" alt="Standard compression" width="700">
</p>

<p align="center">
  <img src="docs/lcm_compression.png" alt="LCM compression" width="700">
</p>

Core capabilities:

- **SQLite message store** - preserves raw messages before compaction
- **Summa
```

---

## 11. obsidian-admonition
- **Repository ID**: `REPO_OBSIDIAN_ADMONITION`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/valentine195/obsidian-admonition.git](https://github.com/valentine195/obsidian-admonition.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/obsidian_plugins/obsidian-admonition`
- **Description**: Repository obsidian-admonition located at /Users/rajondas/teamwork_projects/hermes_air10_supertutor/HERMES_AIR10_SUPERPOWER_LAB/staged_acquisitions/obsidian_plugins/obsidian-admonition

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Admonition

The Admonition plugin for Obsidian is a tool that allows you to create attention-grabbing callouts, tips, warnings and other informative blocks within your notes. The plugin provides a range of pre-defined icons to pick from, as well as the ability to create your own custom styles using CSS. You can customize and style to fit your specific needs, and can target each iteration independently using the `.callout` and `.admonition` selectors.

## Features

- Supports a variety of built-in admonition types such as tip, warning, caution, note, and more.
- Customizable styles with the ability to use Markdown attributes in callouts, or stylize directly with CSS.
- Supports nesting of blockquotes and code-blocks.
- Admonitions can flourish in combination with other plugins such as Obsidian **[Templates](https://help.obsidian.md/Plugins/Templates)** or @SilentVoid13's **[Templater](https://github.com/SilentVoid13/Templater)**.
- Supports import and export of custom admonitions via `.json` files.

### Quickstart

1. Install the Admonition plugin from the Community Plugins pane in Obsidian.
2. **Callout Version**: In the editor, type out the name of an admonition type (such as >[!tip]) followed by your content.
3. **Admonition Version**: In the editor, type out the name of an admonition type in a code block `(such as ```ad-tip)` followed by your content on the subsequent lines.
4. Ensure three backticks close your codeblock.
5. Preview your note to see the formatted admonition.

````yaml
```ad-tip
title: This is a tip

This is the content of the admonition tip.
```
````

Check out the **[plugin documentation](docs)** for more detailed instructions and examples.

## Support

If you encounter any issues, want to give back and help out, or have suggestions for new features, file an issue on the **[GitHub repository](https://github.com/ebullient/obsidian-admonitions/issues)**.

### Complementary Plugins by Javalent

While we think all of our plugins are pretty awesome, we think these are especially awesome and work well with this plugin:

- **[Obsidian Leaflet](https://github.com/valentine195/obsidian-leaflet-plugin)** Adds interactive maps to Obsidian notes
- **[Dice Roller](https://github.com/valentine195/obsidian-dice-roller)** Inline dice rolling for Obsidian
- **[Fantasy Statblocks](https://github.com/valentine195/obsidian-5e-statblocks)** Format Statblocks inside Obsidian
- **[Initiative Tracker](https://github.com/valentine195/obsidian-initiative-tracker)** Track initiative and turns in Obsidian
```

---

## 12. upsc_polity_24h_mvp
- **Repository ID**: `REPO_UPSC_POLITY_24H_MVP`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/quant/upsc_polity_24h_mvp](https://github.com/quant/upsc_polity_24h_mvp)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/_QUARANTINE_POLITY_VAULT/upsc_polity_24h_mvp`
- **Description**: Repository upsc_polity_24h_mvp located at /Users/rajondas/teamwork_projects/_QUARANTINE_POLITY_VAULT/upsc_polity_24h_mvp

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 13. air10_student_engine
- **Repository ID**: `REPO_AIR10_STUDENT_ENGINE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/quant/air10_student_engine](https://github.com/quant/air10_student_engine)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/air10_student_engine`
- **Description**: Repository air10_student_engine located at /Users/rajondas/teamwork_projects/air10_student_engine

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 14. Obsidian_to_Anki
- **Repository ID**: `REPO_OBSIDIAN_TO_ANKI`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/Pseudonium/Obsidian_to_Anki.git](https://github.com/Pseudonium/Obsidian_to_Anki.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/Obsidian_to_Anki`
- **Description**: Repository Obsidian_to_Anki located at /Users/rajondas/teamwork_projects/downloaded_wheels/Obsidian_to_Anki

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Obsidian_to_Anki
Plugin to add flashcards from a text or markdown file to Anki. Run in Obsidian as a plugin, or from the command-line as a python script. Built with [Obsidian](https://obsidian.md/) markdown syntax in mind. Supports **user-defined custom syntax for flashcards.**  
See the [Trello](https://trello.com/b/6MXEizGg/obsidiantoanki) for planned features.

## Getting started

Check out the [Wiki](https://github.com/Pseudonium/Obsidian_to_Anki/wiki)! It has a ton of information, including setup instructions for new users. I will include a copy of the instructions here:

## Setup

### All users
1. Start up [Anki](https://apps.ankiweb.net/), and navigate to your desired profile.
2. Ensure that you've installed [AnkiConnect](https://git.foosoft.net/alex/anki-connect).

### Obsidian plugin users
3. Have [Obsidian](https://obsidian.md/) downloaded
4. Search the 'Community plugins' list for this plugin
5. Install the plugin.
6. In Anki, navigate to Tools->Addons->AnkiConnect->Config, and change it to look like this:
<pre>
{
    "apiKey": null,
    "apiLogPath": null,
    "webBindAddress": "127.0.0.1",
    "webBindPort": 8765,
    "webCorsOrigin": "http://localhost",
    "webCorsOriginList": [
        "http://localhost",
        "app://obsidian.md"
    ]
}
</pre>

7. Restart Anki to apply the above changes
8. With Anki running in the background, load the plugin. This will generate the plugin settings.


You shouldn't need Anki running to load Obsidian in the future, though of course you will need it for using the plugin!

To run the plugin, look for an Anki icon on your ribbon (the place where buttons such as 'open Graph view' and 'open Quick Switcher' are).
For more information on use, please check out the [Wiki](https://github.com/Pseudonium/Obsidian_to_Anki/wiki)!

### Python script users
3. Install the latest version of [Python](https://www.python.org/downloads/).
4. If you are a new user, download `obstoanki_setup.py` from the [releases page](https://github.com/Pseudonium/Obsidian_to_Anki/releases), and place it in the folder you want the script installed (for example your notes folder).  
5. Run `obstoanki_setup.py`, for example by double-clicking it in a file explorer. This will download the latest version of the script and required dependencies automatically. Existing users should be able to run their existing `obstoanki_setup.py` to get the latest version of the script.  
6. Check the Permissions tab below to ensure the script is able to run.
7. Run `obsidian_to_anki.py`, for example by double-clicking it in a file explorer. This will generate a config file, `obsidian_to_anki_config.ini`.

#### Permissions
The script needs to be able to:
* Make a config file in the directory the script is installed.
* Read the file in the directory the script is used.
* Make a backup file in the directory the script is used.
* Rename files in the directory the script is used.
* Remove a backup file in the directory the script is used.
* Change the current working directory temporarily (so that local image paths are resolved correctly).

## Features

Current features (check out the wiki for more details):
* **Custom note types** - You're not limited to the 6 built-in note types of Anki.
* **Custom scan directory** 
  * The plugin will scan the entire vault by default
  * You can also set which directory (includes all sub-directories as well) to scan via plugin settings
* **Ignore Folders and Files**
  * You can specify which files and folders 
```

---

## 15. vibepod-cli
- **Repository ID**: `REPO_VIBEPOD_CLI`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/VibePod/vibepod-cli.git](https://github.com/VibePod/vibepod-cli.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/vibepod-cli`
- **Description**: Repository vibepod-cli located at /Users/rajondas/teamwork_projects/downloaded_wheels/vibepod-cli

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/VibePod/vibepod-cli/main/docs/assets/icon.png" alt="VibePod icon" width="150" />
</p>

<h1 align="center">VibePod</h1>

<p align="center">
  <a href="https://vibepod.dev/docs/"><img alt="Docs" src="https://img.shields.io/badge/docs-vibepod.dev-blue" /></a>
  <a href="https://pypi.org/project/vibepod/"><img alt="PyPI" src="https://img.shields.io/pypi/v/vibepod" /></a>
  <a href="https://anaconda.org/conda-forge/vibepod"><img alt="conda-forge" src="https://img.shields.io/conda/vn/conda-forge/vibepod" /></a>
  <a href="https://github.com/VibePod/vibepod-cli/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/VibePod/vibepod-cli/actions/workflows/ci.yml/badge.svg" /></a>
  <a href="https://github.com/VibePod/vibepod-cli/actions/workflows/docs.yml"><img alt="Docs Build" src="https://github.com/VibePod/vibepod-cli/actions/workflows/docs.yml/badge.svg" /></a>
  <img alt="License" src="https://img.shields.io/github/license/VibePod/vibepod-cli" />
</p>

VibePod is a unified CLI (`vp`) for running AI coding agents in isolated
Docker or Podman containers — no required configuration, no setup. Just
`vp run <agent>`. Includes built-in local metrics collection, HTTP traffic
tracking, and an analytics dashboard to monitor and compare agents side-by-side.

## Features

- ⚡ **Zero config** — no setup required; `vp run <agent>` just works. Optional YAML for custom configuration
- 🐳 **Isolated agents** — each agent runs in its own Docker or Podman container
- 🔀 **Unified interface** — one CLI for Claude, Gemini, Codex, Devstral/Vibe, Copilot, Auggie, Pi, Agy, Tau, Jcode, Freebuff, Qwen, dsh & more
- 🧩 **Skills** — install reusable prompt recipes per-project or per-user with `vp skills add`
- 🧱 **Project overlays** — commit a `FROM`-less Dockerfile fragment in `.vibepod/overlay/` and VibePod auto-builds a cached, content-addressed image layer on top of the agent's base image — one clearly named image per project and agent ([docs](https://vibepod.dev/docs/overlays/))
- 📊 **Local analytics dashboard** — track usage and HTTP traffic per agent, plus token metrics
- 🐑 **Herdr aware** — `vp run` inside a [herdr](https://herdr.dev/) pane reports agent state automatically
- ⚖️ **Agent comparison** — benchmark multiple agents against each other in the dashboard
- 🔒 **Privacy-first** — all metrics collected and stored locally, never sent to the cloud
- 📦 **Simple install** — via pip, Homebrew, or conda-forge

## Installation

VibePod is available on [PyPI](https://pypi.org/project/vibepod/):

```bash
pip install vibepod
```

with [Homebrew](https://github.com/VibePod/homebrew-vibepod):

```bash
brew install vibepod/vibepod/vibepod
```

and on [conda-forge](https://anaconda.org/conda-forge/vibepod) for conda,
mamba, and pixi users:

```bash
conda install -c conda-forge vibepod
mamba install -c conda-forge vibepod
pixi global install vibepod
```

## Quick Start

```bash
vp run <agent>
# examples:
vp run claude
vp run codex
vp run vibe   # alias of devstral
```

Extra arguments after the agent are forwarded to the agent process. Use `--`
before agent flags so VibePod does not parse them as its own options:

```bash
vp run <agent> -- <agent-args>
```

## IKWID Mode (`--ikwid`)

Use `--ikwid` to append each agent's auto-approval / permission-skip flag when supported.

| Agent               | `--ikwid` appended args                      |
| ------------------- | ----------------------------------
```

---

## 16. chromium-ipc-sniffer
- **Repository ID**: `REPO_CHROMIUM_IPC_SNIFFER`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/tomer8007/chromium-ipc-sniffer.git](https://github.com/tomer8007/chromium-ipc-sniffer.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/chromium-ipc-sniffer`
- **Description**: Repository chromium-ipc-sniffer located at /Users/rajondas/teamwork_projects/downloaded_wheels/chromium-ipc-sniffer

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Chromium IPC Sniffer
This utility helps you explore what Chrome processes are saying to each other under the hood in real-time, using Wireshark.

It captures data sent over the [Named Pipe](https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes) Inter-Process-Communication (IPC) primitive and sends it over to dissection.

<img src="https://raw.githubusercontent.com/tomer8007/chromium-ipc-sniffer/master/screenshots/screenshot_2.png" >

## What can I see using this?
* [Mojo Core](https://chromium.googlesource.com/chromium/src/+/master/mojo/core/README.md) messages (Ports, Nodes, Invitations, Handles, etc.)
* [IPCZ](https://docs.google.com/document/d/1i49DF2af4JDspE1fTXuPrUvChQcqDChdHH6nx4xiyoY/edit?resourcekey=0-t_viq9NAbGb5kr_ni9scTA#) messages, aka Chromuim's new replacement for Mojo Core (Portals, Routers, Parcels, etc.)
* [Mojo binded user messages](https://chromium.googlesource.com/chromium/src/+/master/mojo/public/cpp/bindings/README.md) (actual `.mojom` IDL method calls)
* [Legacy IPC](https://www.chromium.org/developers/design-documents/inter-process-communication)
* [Mojo data pipe](https://chromium.googlesource.com/chromium/src/+/master/mojo/public/c/system/README.md#Data-Pipes) control messages (read/wrote X bytes)
* Audio sync messages (`\pipe\chrome.sync.xxxxx`)

You are welcomed to look at [some traffic examples](https://github.com/tomer8007/chromium-ipc-sniffer/wiki/Examples) as well.

However, this project won't see anything that doesn't go over pipes, which is mostly shared memory IPC:
* Mojo data pipe contents (raw networking buffers, audio, etc.)
* [Sandbox IPC](https://chromium.googlesource.com/chromium/src/+/master/docs/design/sandbox.md#the-target-process)
* Possibly more things, such as some `ipcz` method calls

## Usage
You can download pre-compiled binaries from the [Releases](https://github.com/tomer8007/chromium-ipc-sniffer/releases) page, and run:
```
C:\>chromeipc.exe

Chrome IPC Sniffer v0.5.0.0

Type -h to get usage help and extended options

[+] Starting up
[+] Determining your chromium version
[+] You are using chromium 83.0.4103.116
[+] Checking mojom interfaces information
[+] Checking legacy IPC interfaces information
[+] Extracting scrambled message IDs from chrome.dll...
[+] Copying LUA dissectors to Wirehsark plugins directory
[+] Enumerating existing chrome pipes
[+] Starting sniffing of chrome named pipe to \\.\pipe\chromeipc.
[+] Opening Wirehark
[+] Capturing 40 packets/second......
```

Wireshark should open automatically.

_[P.S. The pipe `\\.\pipe\chromeipc` has nothing to do with Chrome itself, it's just where this tool will output its traffic to]_

## Compiling it yourself
If you don't like pre-built binaries, you can clone and compile this repository at least using Visual Studio 2015. Note that it depends on the `Newtonsoft.Json` package.

## Advanced Usage
```
Chrome IPC Sniffer v0.7.0.0

Syntax: chromeipc [options]
Available options:

    Capturing:
        --only-mojo
            Records only packets sent over a "\\mojo.*" pipe (without "\\chrome.sync.*", etc.).

        --only-new-mojo-pipes
            Records only packets sent over mojo AND newly-created pipes since the start of the capture
            This helps reducing noise and it might improve performance
            (example: opening a new tab will create a new mojo pipe).

        --dont-patch
            Avoids trying to patch the chrome processes (Chromium v112+). The patching is used to make all IPCZ traffic direct
```

---

## 17. anki-connect
- **Repository ID**: `REPO_ANKI_CONNECT`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/FooSoft/anki-connect.git](https://github.com/FooSoft/anki-connect.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/anki-connect`
- **Description**: Repository anki-connect located at /Users/rajondas/teamwork_projects/downloaded_wheels/anki-connect

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Anki-Connect

This repository has permanently moved to https://git.sr.ht/~foosoft/anki-connect.
```

---

## 18. antigravity-awesome-skills-benjaminasterA
- **Repository ID**: `REPO_ANTIGRAVITY_AWESOME_SKILLS_BENJAMINASTERA`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/benjaminasterA/antigravity-awesome-skills.git](https://github.com/benjaminasterA/antigravity-awesome-skills.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-awesome-skills-benjaminasterA`
- **Description**: Repository antigravity-awesome-skills-benjaminasterA located at /Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-awesome-skills-benjaminasterA

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# 🌌 Antigravity Awesome Skills: 889+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

> **The Ultimate Collection of 889+ Universal Agentic Skills for AI Coding Assistants — Claude Code, Gemini CLI, Codex CLI, Antigravity IDE, GitHub Copilot, Cursor, OpenCode, AdaL**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Kiro CLI](https://img.shields.io/badge/Kiro%20CLI-AWS-orange)](https://kiro.dev)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Copilot](https://img.shields.io/badge/GitHub%20Copilot-VSCode-lightblue)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-DeepMind-red)](https://github.com/sickn33/antigravity-awesome-skills)
[![AdaL CLI](https://img.shields.io/badge/AdaL%20CLI-SylphAI-pink)](https://sylph.ai/)
[![ASK Supported](https://img.shields.io/badge/ASK-Supported-blue)](https://github.com/yeasy/ask)
[![Buy Me a Book](https://img.shields.io/badge/Buy%20me%20a-book-d13610?logo=buymeacoffee&logoColor=white)](https://buymeacoffee.com/sickn33)

If this project helps you, you can [support it here](https://buymeacoffee.com/sickn33) or simply ⭐ the repo.

**Antigravity Awesome Skills** is a curated, battle-tested library of **889 high-performance agentic skills** designed to work seamlessly across all major AI coding assistants:

- 🟣 **Claude Code** (Anthropic CLI)
- 🔵 **Gemini CLI** (Google DeepMind)
- 🟢 **Codex CLI** (OpenAI)
- 🟠 **Kiro CLI** (AWS)
- 🔴 **Antigravity IDE** (Google DeepMind)
- 🩵 **GitHub Copilot** (VSCode Extension)
- 🟠 **Cursor** (AI-native IDE)
- ⚪ **OpenCode** (Open-source CLI)
- 🌸 **AdaL CLI** (Self-evolving Coding Agent)

This repository provides essential skills to transform your AI assistant into a **full-stack digital agency**, including official capabilities from **Anthropic**, **OpenAI**, **Google**, **Microsoft**, **Supabase**, and **Vercel Labs**.

## Table of Contents

- [🚀 New Here? Start Here!](#new-here-start-here)
- [📖 Complete Usage Guide](docs/USAGE.md) - **Start here if confused after installation!**
- [🔌 Compatibility & Invocation](#compatibility--invocation)
- [🛠️ Installation](#installation)
- [🧯 Troubleshooting](#troubleshooting)
- [🎁 Curated Collections (Bundles)](#curated-collections)
- [🧭 Antigravity Workflows](#antigravity-workflows)
- [📦 Features & Categories](#features--categories)
- [📚 Browse 889+ Skills](#browse-889-skills)
- [🤝 How to Contribute](#how-to-contribute)
- [🤝 Community](#community)
- [☕ Support the Project](#support-the-project)
- [👥 Contributors & Credits](#credits--sources)
- [👥 Repo Contributors](#repo-contributors)
- [⚖️ License](#license)
- [🌟 Star History](#star-history)
- [🏷️ GitHub Topics](#github-topics)

---

## New Here? Start Here!

**Welcome to the V6.0.0 Workflows Edition.** This isn't just a list of scripts; it's a complete operating system for your AI Agent.

### 1. 🐣 Context: What is this?

**Antigravity Awesome Skills** (Release 6.0.0) is a massive upgrade to your AI's capabiliti
```

---

## 19. get-shit-done-for-antigravity-toonight
- **Repository ID**: `REPO_GET_SHIT_DONE_FOR_ANTIGRAVITY_TOONIGHT`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/toonight/get-shit-done-for-antigravity.git](https://github.com/toonight/get-shit-done-for-antigravity.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/get-shit-done-for-antigravity-toonight`
- **Description**: Repository get-shit-done-for-antigravity-toonight located at /Users/rajondas/teamwork_projects/downloaded_wheels/get-shit-done-for-antigravity-toonight

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<div align="center">

<picture>
  <img src="assets/banner.svg" alt="Get Shit Done for Antigravity" width="100%"/>
</picture>

<br/>

[![Version](https://img.shields.io/badge/version-1.6.0-00C853?style=flat-square)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-2196F3?style=flat-square)](LICENSE)
[![Based on GSD](https://img.shields.io/badge/based%20on-GSD-7B2D8E?style=flat-square)](https://github.com/glittercowboy/get-shit-done)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-FF6D00?style=flat-square)](#-cross-platform-support)
[![Model Agnostic](https://img.shields.io/badge/models-any%20LLM-E91E63?style=flat-square)](#-multi-model-support)

<br/>

**Stop vibecoding. Start shipping.**

*Describe your idea → GSD extracts everything the AI needs → Watch it build correctly.*

<br/>

[Getting Started](#-getting-started) · [How It Works](#-how-it-works) · [Commands](#-commands-29-total) · [Documentation](#-documentation)

</div>

---

## 🧠 The Problem

> Vibecoding has a bad reputation — and it deserves it.

You describe what you want, AI generates code, and you get **inconsistent garbage** that falls apart at scale.

GSD fixes that. It's the **context engineering layer** that makes AI coding reliable.

<table>
<tr>
<td width="50%">

### ❌ Without GSD
```
"Add a feature"
    → Inconsistent code
    → Bugs everywhere
    → Debug loop
    → Frustration
```

</td>
<td width="50%">

### ✅ With GSD
```
"Add a feature"
    → SPEC
    → Plan
    → Atomic execution
    → Verification
    → ✅ Done
```

</td>
</tr>
</table>

> **No enterprise roleplay.** No sprint ceremonies, story points, stakeholder syncs, or Jira workflows.
> Just an incredibly effective system for building cool stuff consistently.

---

## 👤 Who This Is For

| | |
|---|---|
| 🧑‍💻 **Solo developers** | Using AI coding assistants and need consistency |
| 👥 **Small teams** | Who want structure without enterprise overhead |
| 😤 **Anyone** | Tired of AI generating inconsistent garbage |

---

## ⚡ Getting Started

> **Requirements:** Antigravity **2.0+** for [subagent delegation](#-subagent-delegation).
> GSD runs on 1.x too — every command works, but everything shares one context window and
> workflows will tell you so.

<details>
<summary><b>🪟 PowerShell (Windows)</b></summary>

```powershell
# Open your project
cd your-project

# Clone the GSD template
git clone https://github.com/toonight/get-shit-done-for-antigravity.git gsd-template

# Copy to your project
Copy-Item -Recurse gsd-template\.agent .\
Copy-Item -Recurse gsd-template\.agents .\
Copy-Item -Recurse gsd-template\.gemini .\
Copy-Item -Recurse gsd-template\.gsd .\
Copy-Item -Recurse gsd-template\adapters .\
Copy-Item -Recurse gsd-template\docs .\
Copy-Item -Recurse gsd-template\scripts .\
Copy-Item -Force gsd-template\PROJECT_RULES.md .\
Copy-Item -Force gsd-template\GSD-STYLE.md .\
Copy-Item -Force gsd-template\model_capabilities.yaml .\

# Clean up
Remove-Item -Recurse -Force gsd-template
```

</details>

<details>
<summary><b>🐧 Bash (Linux / Mac)</b></summary>

```bash
# Open your project
cd your-project

# Clone the GSD template
git clone https://github.com/toonight/get-shit-done-for-antigravity.git gsd-template

# Copy to your project
cp -r gsd-template/.agent ./
cp -r gsd-template/.agents ./
cp -r gsd-template/.gemini ./
cp -r gsd-template/.gsd ./
cp -r gsd-template/adapters ./
cp -r gsd-template/docs ./
cp -r gsd-template/scripts ./
cp gsd-template/PROJECT_RU
```

---

## 20. fsrs-optimizer
- **Repository ID**: `REPO_FSRS_OPTIMIZER`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/open-spaced-repetition/fsrs-optimizer.git](https://github.com/open-spaced-repetition/fsrs-optimizer.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/fsrs-optimizer`
- **Description**: Repository fsrs-optimizer located at /Users/rajondas/teamwork_projects/downloaded_wheels/fsrs-optimizer

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# FSRS Optimizer

[![PyPi](https://img.shields.io/pypi/v/FSRS-Optimizer)](https://pypi.org/project/FSRS-Optimizer/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The FSRS Optimizer is a Python library capable of utilizing personal spaced repetition review logs to refine the FSRS algorithm. Designed with the intent of delivering a standardized, universal optimizer to various FSRS implementations across numerous programming languages, this tool is set to establish a ubiquitous standard for spaced repetition review logs. By facilitating the uniformity of learning data among different spaced repetition softwares, it guarantees learners consistent review schedules across a multitude of platforms.

Delve into the underlying principles of the FSRS Optimizer's training process at: https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-mechanism-of-optimization

Explore the mathematical formula of the FSRS model at: https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm

# Review Logs Schema

The `review_logs` table captures the review activities performed by users. Each log records the details of a single review instance. The schema for this table is as follows:

| Column Name | Data Type | Description | Constraints |
|-------------|-----------|-------------|-------------|
| card_id | integer or string | The unique identifier of the flashcard being reviewed | Not null |
| review_time | timestamp  in *miliseconds* | The exact moment when the review took place | Not null |
| review_rating | integer | The user's rating for the review. This rating is subjective and depends on how well the user believes they remembered the information on the card | Not null, Values: {1 (Again), 2 (Hard), 3 (Good), 4 (Easy)} |
| review_state | integer | The state of the card at the time of review. This describes the learning phase of the card | Optional, Values: {0 (New), 1 (Learning), 2 (Review), 3 (Relearning)} |
| review_duration | integer | The time spent on reviewing the card, typically in miliseconds | Optional, Non-negative |

Extra Info:
- `timezone`: The time zone of the user when they performed the review, which is used to identify the start of a new day.
- `day_start`: The hour (0-23) at which the user starts a new day, which is used to separate reviews that are divided by sleep into different days.

Notes:
- All timestamp fields are expected to be in UTC.
- The `card_id` should correspond to a valid card in the corresponding flashcards dataset.
- `review_rating` should be a reflection of the user's memory of the card at the time of the review.
- `review_state` helps to understand the learning progress of the card.
- `review_duration` measures the cost of the review.
- `timezone` should be a string from the IANA Time Zone Database (e.g., "America/New_York"). For more information, refer to this [list of IANA time zones](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568).
- `day_start` determines the start of the learner's day and is used to correctly assign reviews to days, especially when reviews are divided by sleep.

Please ensure your data conforms to this schema for optimal compatibility with the optimization process.

# Optimize FSRS with your review logs

**Installation**

Install the package with the command:

```
python -m pip install fsrs-optimizer
```

You should upgrade regularly to make sure you have the most recent version of FSRS-Optimiz
```

---

## 21. openlive
- **Repository ID**: `REPO_OPENLIVE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/katipally/openlive.git](https://github.com/katipally/openlive.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/openlive`
- **Description**: Repository openlive located at /Users/rajondas/teamwork_projects/downloaded_wheels/openlive

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<div align="center">

<img src="assets/logo.svg" alt="OpenLive" width="88" height="88" />

# OpenLive

### The open voice and vision layer for AI agents.

Your AI can think. OpenLive gives it ears, a mouth, and eyes.
Bring your own model, or talk to the coding agents you already use, with the whole
voice loop running on your own machine. An open alternative to ElevenLabs Agents,
Gemini Live, and OpenAI Realtime.

[![Release](https://img.shields.io/github/v/release/katipally/openlive?color=2f6fed)](https://github.com/katipally/openlive/releases/latest)
[![CI](https://github.com/katipally/openlive/actions/workflows/ci.yml/badge.svg)](https://github.com/katipally/openlive/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/katipally/openlive?color=2f6fed)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-2f6fed.svg)](CONTRIBUTING.md)

[![Download for macOS](https://img.shields.io/badge/Download-macOS-0b0b0c?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/katipally/openlive/releases/latest)
&nbsp;
[![Download for Windows](https://img.shields.io/badge/Download-Windows-0b0b0c?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0zIDVsNy0xdjdIM3ptMCAxNGw3IDF2LTdIM3ptOC0xNXY4aDEwVjNsLTEwIDF6bTAgMTZsMTAgMVYxM0gxMXoiLz48L3N2Zz4=&logoColor=white)](https://github.com/katipally/openlive/releases/latest)
&nbsp;
[![Download for Linux](https://img.shields.io/badge/Download-Linux-0b0b0c?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/katipally/openlive/releases/latest)

</div>

## Demo

https://github.com/user-attachments/assets/065775b0-0a4a-4adf-8fa7-bcf065e6337f

---

## What this is

Wiring an AI into a real conversation is harder than it looks: voice activity
detection, knowing when someone actually stopped talking, streaming speech-to-text,
the model turn, streaming text-to-speech, and barge-in so you can interrupt. Then
camera and screen on top. Hosted platforms rent you that pipeline by the minute and
run it on their cloud.

OpenLive is that pipeline, open and local. The listening, the speaking, and the
watching all run on-device (WebGPU). You bring the brain, and any brain works:

- **A model you have a key for.** Anthropic, OpenAI, Google, xAI, DeepSeek, Groq,
  Ollama (fully local), and a dozen more. No per-minute audio fees; you pay only
  the model costs you'd pay anyway.
- **The coding agent you already use.** Claude Code, Codex, Cursor, OpenCode, or
  Hermes, driven locally over the
  [Agent Client Protocol](https://agentclientprotocol.com) (JSON-RPC over stdio),
  under your own login. Talk to your agent, watch it work, answer its permission
  asks by voice.

Whichever brain you pick, OpenLive is the same thing it has always been: the ears,
mouth, and eyes around it. Nothing you say leaves the machine. The only thing that
goes out is the final transcript (plus camera or screen frames if you turn them on),
to whatever brain you picked.

An honest note on architecture: OpenLive is a cascaded pipeline (speech to text to
model to speech), not a full-duplex speech-to-speech model like GPT-Live. That's a
real trade. A speech-native model can overlap talk and listen in ways a cascade
can't, but the cascade is exactly what makes "any brain, all local, no audio fees"
possible.

## Features

The core, the ears / mouth / eyes:

- **On-device voice loop.** Si
```

---

## 22. review-heatmap
- **Repository ID**: `REPO_REVIEW_HEATMAP`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/glutanimate/review-heatmap.git](https://github.com/glutanimate/review-heatmap.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/review-heatmap`
- **Description**: Repository review-heatmap located at /Users/rajondas/teamwork_projects/downloaded_wheels/review-heatmap

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<p align="center"><img src="https://github.com/glutanimate/review-heatmap/raw/main/screenshots/0.7.0_regular_year.png"></p>

<h2 align="center">Review Heatmap for Anki</h2>

<p align="center">
<a title="Latest (pre-)release" href="https://github.com/glutanimate/review-heatmap/releases"><img src ="https://img.shields.io/github/release-pre/glutanimate/review-heatmap.svg?colorB=brightgreen"></a>
<a title="License: GNU AGPLv3" href="https://github.com/glutanimate/review-heatmap/blob/main/LICENSE"><img  src="https://img.shields.io/badge/license-GNU AGPLv3-green.svg"></a>
<a title="Rate on AnkiWeb" href="https://ankiweb.net/shared/info/1771074083"><img src="https://glutanimate.com/logos/ankiweb-rate.svg"></a>
<br>
<a title="Buy me a coffee :)" href="https://ko-fi.com/X8X0L4YV"><img src="https://img.shields.io/badge/ko--fi-contribute-%23579ebd.svg"></a>
<a title="Support me on Patreon :D" href="https://www.patreon.com/bePatron?u=7522179"><img src="https://img.shields.io/badge/patreon-support-%23f96854.svg"></a>
<a title="Follow me on Twitter" href="https://twitter.com/intent/user?screen_name=glutanimate"><img src="https://img.shields.io/twitter/follow/glutanimate.svg"></a>
</p>

> Your learning performance at a glance

Adds a **heatmap graph** to [Anki](https://apps.ankiweb.net/)'s main window which visualizes past and future card review activity, similar to the contribution view on GitHub. Information on the **current streak** is displayed alongside the heatmap. Clicking on an item shows the cards reviewed on that day.

<!-- MarkdownTOC -->

- [Video Demonstration](#video-demonstration)
- [Installation](#installation)
  - [AnkiWeb](#ankiweb)
- [Documentation](#documentation)
- [Building](#building)
- [Contributing](#contributing)
- [License and Credits](#license-and-credits)

<!-- /MarkdownTOC -->

### Video Demonstration

General Overview | Customization  
---------|----------
[![YouTube: Anki add-on: Review Heatmap](https://i.ytimg.com/vi/3Hk5TYdvKnM/mqdefault.jpg)](https://youtu.be/3Hk5TYdvKnM) | [![YouTube: Add-on Update: Review Heatmap](https://i.ytimg.com/vi/2u8p0N47eUg/mqdefault.jpg)](https://youtu.be/2u8p0N47eUg)

(Make sure to enable closed-captions for comments on the demonstrated features)

### Installation

#### AnkiWeb

The easiest way to install Review Heatmap is through [AnkiWeb](https://ankiweb.net/shared/info/1771074083).

#### Manual installation <!-- omit in toc -->

1. Download the latest `.ankiaddon` file from the [releases tab](https://github.com/glutanimate/review-heatmap/releases) (you might need to click on *Assets* below the description to reveal the download links)
2. Open the folder where your downloads are located and double-click on the downloaded `.ankiaddon` file.
3. Follow the installation prompt and restart Anki if it asks you to

### Documentation

The use of the add-on is documented in the [Wiki section](https://github.com/Glutanimate/review-heatmap/wiki) and a [series of video tutorials on YouTube](https://www.youtube.com/playlist?list=PL3MozITKTz5Y9owI163AJMYqKwhFrTKcT). More information may also be found in the [AnkiWeb description](docs/description.md).

### Building

Review Heatmap's build system recently underwent a number of changes. Updated build instructions will soon be added here. Please stand by.

### Contributing

Contributions are welcome! Please review the [contribution guidelines](./CONTRIBUTING.md) on how to:

- Report issues
- File pull requests
- Support the project as a non-developer

##
```

---

## 23. awesome-fsrs
- **Repository ID**: `REPO_AWESOME_FSRS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/open-spaced-repetition/awesome-fsrs.git](https://github.com/open-spaced-repetition/awesome-fsrs.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/awesome-fsrs`
- **Description**: Repository awesome-fsrs located at /Users/rajondas/teamwork_projects/downloaded_wheels/awesome-fsrs

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
[<img src="https://github.com/open-spaced-repetition/fsrs4anki/assets/32575846/9efb2ca5-51bd-411d-9694-a77b09f51fa7" align="left" width="64" height="64">](https://github.com/open-spaced-repetition/awesome-fsrs)

# Awesome FSRS [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome FSRS implementations, papers and resources. Feel free to suggest new projects in Issues or PR directly.

## Implementation

- Python
  - Scheduler (v6) + Optimizer: [py-fsrs](https://github.com/open-spaced-repetition/py-fsrs)
  - Scheduler (v5): [rs-fsrs-python](https://github.com/open-spaced-repetition/rs-fsrs-python)
  - Optimizer (v6): [fsrs-optimizer](https://github.com/open-spaced-repetition/fsrs-optimizer)
  - Optimizer (v6): [fsrs-rs-python](https://github.com/open-spaced-repetition/fsrs-rs-python)
  - [Deprecated] Optimizer: [fsrs-optimizer-tiny](https://github.com/open-spaced-repetition/fsrs-optimizer-tiny)
- Rust
  - Scheduler (v5): [rs-fsrs](https://github.com/open-spaced-repetition/rs-fsrs)
  - Scheduler (v6) + Optimizer: [fsrs-rs](https://github.com/open-spaced-repetition/fsrs-rs)
    - Run in browsers: [fsrs-browser](https://github.com/open-spaced-repetition/fsrs-browser)
- TypeScript
  - Scheduler (v6): [ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs)
- Go
  - Scheduler (v5): [go-fsrs](https://github.com/open-spaced-repetition/go-fsrs)
- Java
  - Scheduler (v5): [rs-fsrs-java](https://github.com/open-spaced-repetition/rs-fsrs-java)
- Scala
  - Scheduler (v6): [fsrs4s](https://github.com/jwbargsten/fsrs4s)
- C
  - Scheduler (v5): [rs-fsrs-c](https://github.com/open-spaced-repetition/rs-fsrs-c)
- Nodejs
  - Scheduler (v5): [rs-fsrs-nodejs](https://github.com/open-spaced-repetition/rs-fsrs-nodejs)
- Dart
  - Scheduler (v4.5): [dart-fsrs](https://github.com/open-spaced-repetition/dart-fsrs)
- Swift
  - Scheduler (v5): [swift-fsrs](https://github.com/open-spaced-repetition/swift-fsrs)
- Clojure/ClojureScript
  - Scheduler (v4): [cljc-fsrs](https://github.com/open-spaced-repetition/cljc-fsrs)
- Ruby
  - Scheduler (v4): [rb-fsrs](https://github.com/open-spaced-repetition/rb-fsrs)
- Kotlin
  - Scheduler (v6): [FSRS-Kotlin](https://github.com/open-spaced-repetition/FSRS-Kotlin)
  - Scheduler (v4): [android-fsrs](https://github.com/open-spaced-repetition/android-fsrs)
- Elixir
  - Scheduler (v4): [ex_fsrs](https://github.com/open-spaced-repetition/ex_fsrs)
- OCaml
  - Scheduler (v5): [ocaml-fsrs](https://github.com/chaosarium/ocaml-fsrs)
- Lisp
  - Scheduler (v6): [lisp-fsrs](https://github.com/open-spaced-repetition/lisp-fsrs)
- Haskell
  - Scheduler (v7): [haskell-fsrs](https://github.com/kutyel/haskell-fsrs)

## Application

### General Flashcard

#### [Anki](https://apps.ankiweb.net/)

  Free and open source, content-agnostic flashcard application for Windows, Mac, Linux, iPhone, and Android. Supports text, images, audio, videos, and scientific markup (via LaTex). Offers free synchronization service using AnkiWeb, with community-shared add-ons and decks.

- FSRS available as an opt-in feature replacing the default SM-2 algorithm.
- Additionally, this [add-on](https://ankiweb.net/shared/info/759844606) offers a variety of extra features, such as Postpone, Advance, Load Balancing and Easy Days.

#### [Avorio](https://avorio.ai/)

  Avorio is a native flashcard app for macOS and iPhone built around FSRS-5. It imports
```

---

## 24. cc-safety-net
- **Repository ID**: `REPO_CC_SAFETY_NET`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/kenryu42/cc-safety-net.git](https://github.com/kenryu42/cc-safety-net.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/cc-safety-net`
- **Description**: Repository cc-safety-net located at /Users/rajondas/teamwork_projects/downloaded_wheels/cc-safety-net

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./.github/assets/cc-safety-net-header-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./.github/assets/cc-safety-net-header-logo-light.svg">
    <img alt="CC Safety Net" src="./.github/assets/cc-safety-net-header-logo-light.svg">
  </picture>
</h1>

[![CI](https://github.com/kenryu42/cc-safety-net/actions/workflows/ci.yml/badge.svg)](https://github.com/kenryu42/cc-safety-net/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/kenryu42/cc-safety-net/branch/main/graph/badge.svg?token=C9QTION6ZF)](https://codecov.io/github/kenryu42/cc-safety-net)
[![Version](https://img.shields.io/github/v/tag/kenryu42/cc-safety-net?label=version&color=blue)](https://github.com/kenryu42/cc-safety-net)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

<div align="center">

**English** · [简体中文](https://ccsafetynet.com/docs/zh-Hans) · [日本語](https://ccsafetynet.com/docs/ja)

[![CC Safety Net](./.github/assets/cc-safety-net-v2.png)](./.github/assets/cc-safety-net-v2.png)

</div>

CC Safety Net (Coding CLI Safety Net) blocks destructive commands and access to secrets such as SSH keys and `.env` files before the tool call runs. It parses what the command does. Wrapping the command or reordering flags does not hide it. A broken config file never blocks anything.

> [!NOTE]
> **[Full documentation →](https://ccsafetynet.com/docs)** covers installation, configuration, reference material, guides, and the security model. This README is the short version.

## Supported coding CLIs

CC Safety Net supports the coding agent CLIs below on Windows, macOS, and Linux. Automated tests cover the analyzer and some Windows integrations. Windows support for the remaining CLIs is best effort and has not been tested.

<table align="center">
  <tr>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#amp-code-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/amp-dark.svg"><img alt="Amp Code" src="./.github/assets/amp-light.svg" height="32"></picture><br>Amp Code</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#antigravity-cli-installation"><img alt="Antigravity CLI" src="./.github/assets/antigravity-cli.png" height="32"><br>Antigravity CLI</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#claude-code-installation"><img alt="Claude Code" src="./.github/assets/claude-code.svg" height="32"><br>Claude Code</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#codex-installation"><img alt="Codex" src="./.github/assets/codex.svg" height="32"><br>Codex</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#cursor-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/cursor-dark.svg"><img alt="Cursor" src="./.github/assets/cursor-light.svg" height="32"></picture><br>Cursor</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#gemini-cli-installation"><img alt="Gemini CLI" src="./.github/assets/gemini-cli.svg" height="32"><br>Gemini CLI</a></td>
    <td align="center"><a href="https://ccsafetynet.com/docs/installation#github-copilot-cli-installation"><picture><source media="(prefers-color-scheme: dark)" srcset="./.github/assets/copilot-cli-dark.svg"><img alt="Gi
```

---

## 25. everything-antigravity-krishnakanthb13
- **Repository ID**: `REPO_EVERYTHING_ANTIGRAVITY_KRISHNAKANTHB13`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/krishnakanthb13/everything-antigravity.git](https://github.com/krishnakanthb13/everything-antigravity.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/everything-antigravity-krishnakanthb13`
- **Description**: Repository everything-antigravity-krishnakanthb13 located at /Users/rajondas/teamwork_projects/downloaded_wheels/everything-antigravity-krishnakanthb13

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Everything Antigravity

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Welcome to the central repository for the **Antigravity** ecosystem. This project houses a collection of AI Agents, Task Skills, and Coding Rules designed to enhance autonomous coding workflows.

Inspired by [everything-claude-code](https://github.com/krishnakanthb13/everything-claude-code)

## 🚀 Overview

Everything Antigravity provides a standardized framework for building and maintaining software using AI agents. It bridges the gap between high-level architectural decisions and low-level coding implementation.

## 📂 Project Structure

- **`agents/`**: Specialist AI persona definitions (Architect, Planner, Reviewer, etc.) with dedicated focus areas.
- **`docs/rules/`**: Hierarchical coding standards organized into "Common" principles and "Language-specific" extensions (Python, TypeScript, Go).
- **`skills/`**: Actionable, deep-dive reference materials for specific tasks (e.g., TDD workflows, performance optimization, security audits).

## 🛠️ Components

### 1. Agents
Specialized personas designed to handle specific stages of the software development lifecycle.
- **Architect**: System design and scalability.
- **Code Reviewer**: Quality assurance and security.
- **Planner**: Task decomposition and roadmapping.

### 2. Rules
Formalized standards that agents must follow.
- **Common**: Universal principles like immutability and error handling.
- **Language-Specific**: PEP 8 for Python, standard `go test` for Go, Zod validation for TypeScript.

### 3. Skills
Executable knowledge modules that provide agents with the "How-To" for complex operations.

## 📦 Installation

There are two ways to install the components from this repository:

### 1. Global Installation (Sync Everything)

This is the recommended way to keep your global AI environment (Claude and Antigravity) perfectly in sync with the latest rules, skills, and workflows.

- **Universal (Any OS)**: `python install.py`
- **Linux / macOS**: `./install.sh`
- **Windows (PowerShell)**: `.\install.ps1`

### 2. Selective Rule Installation

If you only want to install specific language rules without syncing skills or workflows:

```bash
cd docs/rules
# Use the installers inside this directory
python install.py python typescript
```

## 📜 Documentation

- [Code Documentation](./CODE_DOCUMENTATION.md) - Technical architecture of this repository.
- [Design Philosophy](./DESIGN_PHILOSOPHY.md) - The "Why" behind the Antigravity framework.
- [Rules Guide](./docs/rules/README.md) - Details on the rules hierarchy.
- [Contributing](./CONTRIBUTING.md) - How to help improve the project.

---
*Built with ❤️ for the future of agentic coding.*

© 2026 Krishna Kanth B. Licensed under the [GPL v3 License](./LICENSE).
```

---

## 26. go-fsrs
- **Repository ID**: `REPO_GO_FSRS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/open-spaced-repetition/go-fsrs.git](https://github.com/open-spaced-repetition/go-fsrs.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/go-fsrs`
- **Description**: Repository go-fsrs located at /Users/rajondas/teamwork_projects/downloaded_wheels/go-fsrs

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# go-fsrs

[![Go Reference](https://pkg.go.dev/badge/github.com/open-spaced-repetition/go-fsrs/v4.svg)](https://pkg.go.dev/github.com/open-spaced-repetition/go-fsrs/v4) [![Go Report Card](https://goreportcard.com/badge/github.com/open-spaced-repetition/go-fsrs/v4)](https://goreportcard.com/report/github.com/open-spaced-repetition/go-fsrs/v4)
![Go version](https://img.shields.io/github/go-mod/go-version/open-spaced-repetition/go-fsrs) ![Tests](https://img.shields.io/github/actions/workflow/status/open-spaced-repetition/go-fsrs/test.yml?style=flat-square&label=tests) ![License](https://img.shields.io/github/license/open-spaced-repetition/go-fsrs?style=flat-square)

A Go library for building spaced-repetition systems with [FSRS](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler).

| Package | Description | FSRS Version | Package Version |
|---|---|---|---|
| `go-fsrs` | FSRS scheduler for review flows | ![FSRS](https://img.shields.io/badge/FSRS-v6-blue?style=flat-square) | ![version](https://img.shields.io/github/v/tag/open-spaced-repetition/go-fsrs?style=flat-square) |
| `go-fsrs/optimizer` | Train FSRS parameters from review logs | ![FSRS](https://img.shields.io/badge/FSRS-v6-blue?style=flat-square) | ![status](https://img.shields.io/badge/status-in_development-orange?style=flat-square) |
| `go-fsrs/simulator` | Simulate deck workload and optimal retention | ![FSRS](https://img.shields.io/badge/FSRS-v6-blue?style=flat-square) | ![status](https://img.shields.io/badge/status-planned-lightgrey?style=flat-square) |

## Install

```bash
go get github.com/open-spaced-repetition/go-fsrs/v4@latest
```

## Quick start

```go
package main

import (
	"fmt"
	"time"

	"github.com/open-spaced-repetition/go-fsrs/v4"
)

func main() {
	s := fsrs.NewFSRS(fsrs.DefaultParam())
	now := time.Now()
	card := fsrs.NewCard(now)

	// Preview all four ratings, then apply one.
	preview, err := s.Repeat(card, now)
	if err != nil {
		panic(err)
	}
	fmt.Println(preview[fsrs.Good])

	review, err := s.Next(card, now, fsrs.Good)
	if err != nil {
		panic(err)
	}
	card = review.Card
}
```

See the [GoDoc](https://pkg.go.dev/github.com/open-spaced-repetition/go-fsrs/v4) for the full API reference.

## API

### High-level (`*FSRS`)

`*FSRS` is the complete scheduling layer. It walks a `Card` through its lifecycle
(New → Learning → Review → Relearning), applies learning steps and short-term
memory updates, optionally fuzzes intervals, and validates all input with
structured errors. This is the recommended entry point for most applications:

| Method | Returns | Purpose |
|---|---|---|
| `Repeat(card, now)` | `(RecordLog, error)` | Returns the result of each potential rating. |
| `Next(card, now, grade)` | `(SchedulingInfo, error)` | Reviews the card with a given rating; returns the updated card + `ReviewLog`. |
| `Retrievability(card, now)` | `(float64, error)` | Current probability of recall. |
| `Reschedule(card, reviews, opts)` | `(RescheduleResult, error)` | Replay a review history; rebuild state and due date. |
| `Forget(card, now, resetCount)` | `(SchedulingInfo, error)` | Reset a card to `New`, preserving its `ReviewLog`. |
| `Rollback(card, log)` | `(Card, error)` | Revert a review using its `ReviewLog`. |
| `MemoryState(history, start)` | `(*MemoryState, error)` | Derive stability/difficulty from `ReviewEntries`. |
| `HistoricalMemoryStates(history, start)` | `([]MemoryState, error)` | All intermediate memory states. |

### Low-level (`Paramet
```

---

## 27. whisper.cpp
- **Repository ID**: `REPO_WHISPER_CPP`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/ggml-org/whisper.cpp.git](https://github.com/ggml-org/whisper.cpp.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/whisper.cpp`
- **Description**: Repository whisper.cpp located at /Users/rajondas/teamwork_projects/downloaded_wheels/whisper.cpp

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# whisper.cpp

<div align="center">

![whisper.cpp](https://user-images.githubusercontent.com/1991296/235238348-05d0f6a4-da44-4900-a1de-d0707e75b763.jpeg)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/ggml-org/whisper.cpp?filter=v*)](https://github.com/ggml-org/whisper.cpp/releases)
[![Actions Status](https://github.com/ggml-org/whisper.cpp/workflows/CI/badge.svg)](https://github.com/ggml-org/whisper.cpp/actions)
[![Conan Center](https://shields.io/conan/v/whisper-cpp)](https://conan.io/center/whisper-cpp)
[![npm](https://img.shields.io/npm/v/whisper.cpp.svg)](https://www.npmjs.com/package/whisper.cpp/)

</div>

High-performance inference of [OpenAI's Whisper](https://github.com/openai/whisper) automatic speech recognition (ASR) model:

- Plain C/C++ implementation without dependencies
- Apple Silicon first-class citizen - optimized via ARM NEON, Accelerate framework, Metal and [Core ML](#core-ml-support)
- AVX intrinsics support for x86 architectures
- [VSX intrinsics support for POWER architectures](#power-vsx-intrinsics)
- Mixed F16 / F32 precision
- [Integer quantization support](#quantization)
- Zero memory allocations at runtime
- [Vulkan support](#vulkan-gpu-support)
- Support for CPU-only inference
- [Efficient GPU support for NVIDIA](#nvidia-gpu-support)
- [AMD ROCm GPU support](#amd-rocm-gpu-support)
- [AMD Ryzen AI NPU Support](#amd-ryzen-ai-npu-support)
- [OpenVINO Support](#openvino-support)
- [Ascend NPU Support](#ascend-npu-support)
- [Moore Threads GPU Support](#moore-threads-gpu-support)
- [C-style API](https://github.com/ggml-org/whisper.cpp/blob/master/include/whisper.h)
- [Voice Activity Detection (VAD)](#voice-activity-detection-vad)

Supported platforms:

- [x] Mac OS (Intel and Arm)
- [x] [iOS](examples/whisper.objc)
- [x] [Android](examples/whisper.android)
- [x] [Java](bindings/java/README.md)
- [x] Linux / [FreeBSD](https://github.com/ggml-org/whisper.cpp/issues/56#issuecomment-1350920264)
- [x] [WebAssembly](examples/whisper.wasm)
- [x] Windows ([MSVC](https://github.com/ggml-org/whisper.cpp/blob/master/.github/workflows/build.yml#L117-L144) and [MinGW](https://github.com/ggml-org/whisper.cpp/issues/168))
- [x] [Raspberry Pi](https://github.com/ggml-org/whisper.cpp/discussions/166)
- [x] [Docker](https://github.com/ggml-org/whisper.cpp/pkgs/container/whisper.cpp)

The entire high-level implementation of the model is contained in [whisper.h](include/whisper.h) and [whisper.cpp](src/whisper.cpp).
The rest of the code is part of the [`ggml`](https://github.com/ggml-org/ggml) machine learning library.

Having such a lightweight implementation of the model allows to easily integrate it in different platforms and applications.
As an example, here is a video of running the model on an iPhone 13 device - fully offline, on-device: [whisper.objc](examples/whisper.objc)

https://user-images.githubusercontent.com/1991296/197385372-962a6dea-bca1-4d50-bf96-1d8c27b98c81.mp4

You can also easily make your own offline voice assistant application: [command](examples/command)

https://user-images.githubusercontent.com/1991296/204038393-2f846eae-c255-4099-a76d-5735c25c49da.mp4

On Apple Silicon, the inference runs fully on the GPU via Metal:

https://github.com/ggml-org/whisper.cpp/assets/1991296/c82e8f86-60dc-49f2-b048-d2fdbd6b5225

## Quick start

First clone the repository:

```bash
git clone https://github.com/ggml
```

---

## 28. antigravity-skills-rominirani
- **Repository ID**: `REPO_ANTIGRAVITY_SKILLS_ROMINIRANI`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rominirani/antigravity-skills.git](https://github.com/rominirani/antigravity-skills.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-skills-rominirani`
- **Description**: Repository antigravity-skills-rominirani located at /Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-skills-rominirani

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Antigravity / Gemini CLI Skills Repository

This repository contains a collection of example **Skills** for [Google Antigravity](https://antigravity.google) and [Gemini CLI](https://geminicli.com/). These examples demonstrate the "Agentic Command" pattern, where natural language requests are routed to specialized instructions, tools, and context.

Read the blog post: https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d

Do a codelab: https://codelabs.developers.google.com/getting-started-with-antigravity-skills?hl=en#0

Also check out the [Google Antigravity Community Hub](https://github.com/rominirani/google-antigravity-community-hub) for more resources, articles, and updates on Antigravity.

## Antigravity Skills

Antigravity Skills allow you to define *how* an agent should behave, which tools it should use, and what context it should reference. This project breaks down skill development into 4 progressive levels of complexity.

### Skills in `skills_tutorial/`

The `skills_tutorial/` directory contains the following examples:

#### Level 1: Basic Routing
**`git-commit-formatter`**
* **Concept**: Pure prompt engineering.
* **Function**: Intercepts "commit" requests and formats the message according to the Conventional Commits specification.
* **Key File**: `SKILL.md`

#### Level 2: Asset Utilization
**`license-header-adder`**
* **Concept**: Loading static resources.
* **Function**: Adds a standard Apache 2.0 license header to source files by reading a template from the `resources/` folder.
* **Key Files**: `SKILL.md`, `resources/HEADER_TEMPLATE.txt`

#### Level 3: Few-Shot Learning
**`json-to-pydantic`**
* **Concept**: Learning by example.
* **Function**: Converts JSON data into Pydantic models by referencing a "golden example" pair (input JSON → output Python) instead of relying on complex instructions.
* **Key Files**: `SKILL.md`, `examples/`

#### Level 4: Tool Use & Validation
**`database-schema-validator`**
* **Concept**: Delegating to deterministic scripts.
* **Function**: Validates SQL schema files for safety and naming conventions by running a Python script, ensuring accurate results.
* **Key Files**: `SKILL.md`, `scripts/validate_schema.py`

### Usage

To use these skills in your Antigravity environment:

1. Clone this repository.
2. Copy the desired folders from `skills_tutorial/` into your workspace's `.agent/skills/` directory, or into your global `~/.gemini/antigravity/skills/` directory.
3. Restart your agent session.

## Gemini CLI Skills

### Skills in `gemini-cli-skills/`

The `gemini-cli-skills/` directory contains the following example:

#### Always Verify GCP
**`always-verify-gcp`**
* **Concept**: Validating GCP commands with the latest official documentation.
* **Function**: This skill interprets ambiguous Google Cloud commands by first consulting the official documentation via the Developer Knowledge MCP Server, then using the `ask_user` tool to provide a validated response.
* **Key File**: `SKILL.md`

## License

Apache 2.0
```

---

## 29. Lyre
- **Repository ID**: `REPO_LYRE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/alexwiese/Lyre.git](https://github.com/alexwiese/Lyre.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/Lyre`
- **Description**: Repository Lyre located at /Users/rajondas/teamwork_projects/downloaded_wheels/Lyre

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Lyre
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Falexwiese%2FLyre.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Falexwiese%2FLyre?ref=badge_shield)
![AppVeyor](https://img.shields.io/appveyor/ci/alexwiese/lyre)
[![NuGet](https://img.shields.io/nuget/v/Lyre)](https://www.nuget.org/packages/Lyre)
[![NuGet](https://img.shields.io/nuget/dt/lyre)](https://www.nuget.org/packages/Lyre)

Chrome Native Messaging implementation for .NET and .NET Core.
Allows easy communication with a Chrome extension using Chrome Native Messaging protocol.

## Install

Get it on [NuGet](https://www.nuget.org/packages/Lyre): `PM> Install-Package Lyre`

## Usage

    using var host = new NativeMessagingHost();

    try
    {
        while (true)
        {
            var response = await host.Read<dynamic>();

            // Echo response
            await host.Write(new { value = $"You said {response.value} at {response.dateTime}", dateTime = DateTime.Now });
        }
    }
    catch (EndOfStreamException)
    {
        // Disconnected
    }
    
## Example/Chrome Extension

See https://github.com/alexwiese/Lyre/tree/master/src/Lyre.ConsoleTest for an example of a Chrome extension communicating with a Native Messaging Host.
    
## Customization

The NativeMessagingHost uses JSON.NET for serialization. This can be customized by passing in a `JsonSerializerSettings` object.
The `Encoding` and `Stream` objects used for communications can also be passed into the constructor.

    var host = new NativeMessagingHost(Console.OpenStandardInput(), Console.OpenStandardOutput(), Encoding.UTF8, new JsonSerializerSettings{ Formatting = Formatting.None});

### Advanced Usage

    // Using cancellation tokens for timeout support
    using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(30));
    var message = await host.Read<dynamic>(cts.Token);
    await host.Write(response, cts.Token);

    // Proper disposal pattern
    using var host = new NativeMessagingHost(inputStream, outputStream, encoding, settings, ownsStreams: true);

## Chrome Native Messaging Protocol Compliance

This library fully complies with the Chrome Native Messaging protocol:

- **Message Size Limits**: Enforces the 1MB message size limit as required by Chrome
- **Proper Error Handling**: Validates message formats and sizes
- **Resource Management**: Implements proper disposal patterns for stream cleanup
- **Async Support**: Full cancellation token support for timeout handling

## Supressing Console Output

By default Chrome Native Messaging uses `stdin` and `stdout` to communicate. If any other code writes to the `Console`, for example by calling `Console.WriteLine(string)`, then this would cause the Chrome Native Messaging pipe to fail due to unexpected output. Helper methods are provided by the `NativeMessagingEnvironment` class to supress or redirect the Console output.

### Supress console output

    // Redirects any calls to Console.Write() or Console.WriteLine() to TextWriter.Null
    NativeMessagingEnvironment.SupressConsoleOutput();
    
### Redirect to stderr

    // This will redirect calls to Console.Write() and Console.WriteLine() to stderr
    NativeMessagingEnvironment.RedirectConsoleOutputToErrorOutput();

### Redirect to Debug output

    // Redirects any calls to Console.Write() or Console.WriteLine() to the Debug output
    NativeMessagingEnvironment.RedirectConsoleOutputToDebugStream();
    
### Redirect to a TextWriter

    //
```

---

## 30. Antigravity-Tools-LS-lbjlaq
- **Repository ID**: `REPO_ANTIGRAVITY_TOOLS_LS_LBJLAQ`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/lbjlaq/Antigravity-Tools-LS.git](https://github.com/lbjlaq/Antigravity-Tools-LS.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/Antigravity-Tools-LS-lbjlaq`
- **Description**: Repository Antigravity-Tools-LS-lbjlaq located at /Users/rajondas/teamwork_projects/downloaded_wheels/Antigravity-Tools-LS-lbjlaq

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<div align="center">

[🇨🇳 中文配置指南](README_ZH.md) | [🇺🇸 English Documentation](README.md)

# 🚀 Antigravity Tools LS

> **Professional Language Server Protocol Transcoding Bridge (v0.0.3)**

<p align="center">
  <img src="https://img.shields.io/badge/Version-0.0.3-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/Rust-1.74%2B-red?style=flat-square" alt="Rust">
  <img src="https://img.shields.io/badge/Tokio-Async-brightgreen?style=flat-square" alt="Tokio">
  <img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Docker-Multi--Arch-2496ED?style=flat-square" alt="Docker">
</p>

<h3>High-Performance Native-Driven AI Protocol Adapter Gateway</h3>

**Antigravity-Tools-LS** is a local proxy bridge system designed specifically for the Antigravity IDE. It is not just a simple forwarder; instead, by deeply simulating the IDE plugin protocol, it fully takes over the lifecycle of the native `ls_core` process to provide the ultimate solution for authentication injection, protocol transcoding, and multi-account dispatching.

> [!IMPORTANT]
> **Project Status**: This project is currently in the **Early Experimental Stage (Experimental)**, and many features (such as Thinking extraction) are still under development. **Due to the author's busy work schedule, project updates may not be very frequent.** We strongly welcome developers to submit **Pull Requests (PR)** or Issues to co-maintain and improve this tool.

<p align="center">
  <a href="#-core-concept-what-is-this">Core Concept</a> • 
  <a href="#-features">Features</a> • 
  <a href="#-architecture">Architecture</a> • 
  <a href="#-deployment-guide">Deployment</a> • 
  <a href="#-asset--version-sync">Asset & Version</a> • 
  <a href="#-api-reference">API Reference</a>
</p>

</div>

---

## ☕ Support the Project

If you find this project helpful, please consider supporting the author!

<a href="https://www.buymeacoffee.com/Ctrler" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-green.png" alt="Buy Me a Coffee" style="height: 60px !important; width: 217px !important;"></a>

| Alipay | WeChat Pay | Buy Me a Coffee |
| :---: | :---: | :---: |
| ![Alipay](./docs/images/donate_alipay.png) | ![WeChat](./docs/images/donate_wechat.png) | ![Coffee](./docs/images/donate_coffee.png) |

---

## 🧠 Core Concept (What is this?)

This project adopts a **Pure Native LS Path** technical architecture:
It exposes standard OpenAI / Anthropic / Gemini APIs externally, while internally delegating requests entirely to the native **Antigravity Language Server (`ls_core`)** process.

Unlike Antigravity-Manager, this system will:
1. **Hold Real Credentials**: Simulate the Extension Server behavior to inject OAuth Tokens into `ls_core`.
2. **Establish Native Connections**: The `ls_core` process establishes an HTTPS/gRPC connection directly with Google backend, ensuring the request characteristics are 100% identical to the official plugin.
3. **Protocol-Aware Transcoding**: Parse the streaming output of `ls_core` at the application layer to extract Tool Call tags, image generation results, and Cascade agent states.

---

## ✨ Features

### 🌊 Deep Protocol Bridging
- **Multi-Protocol Adaptation (Multi-Sink)**: Unified conversion from native protocols to OpenAI (`/v1/chat/completions`), Anthropic (`/v1/messages`), and Gemini Native APIs.
- **Connect+Proto Spoofing**: Fully implemen
```

---

## 31. super-voice-assistant
- **Repository ID**: `REPO_SUPER_VOICE_ASSISTANT`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/ykdojo/super-voice-assistant.git](https://github.com/ykdojo/super-voice-assistant.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/super-voice-assistant`
- **Description**: Repository super-voice-assistant located at /Users/rajondas/teamwork_projects/downloaded_wheels/super-voice-assistant

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Super Voice Assistant

macOS voice assistant with global hotkeys - transcribe speech to text with offline models (WhisperKit or Parakeet) or cloud-based Gemini API, capture and transcribe screen recordings with visual context, and read selected text aloud with Gemini Live. Fast, accurate, and simple.

## Demo

**Parakeet transcription (fast and accurate):**

https://github.com/user-attachments/assets/163e6484-a3b1-49ef-b5e1-d9887d1f65d0

**Instant text-to-speech:**

https://github.com/user-attachments/assets/c961f0c6-f3b3-49d9-9b42-7a7d93ee6bc8

**Visual disambiguation for names:**

https://github.com/user-attachments/assets/0b7f481f-4fec-4811-87ef-13737e0efac4

## Features

**Voice-to-Text Transcription**
- Press Command+Option+Z for local offline transcription (WhisperKit or Parakeet)
- Press Command+Option+X for cloud transcription with Gemini API
- Choose your engine in Settings: WhisperKit models or Parakeet (faster, more accurate)
- Automatic text pasting at cursor position
- Transcription history with Command+Option+A

**Streaming Text-to-Speech**
- Press Command+Option+S to read selected text aloud using Gemini Live API
- Press Command+Option+S again while reading to cancel the operation
- Sequential streaming for smooth, natural speech with minimal latency
- Smart sentence splitting for optimal speech flow

**Screen Recording & Video Transcription**
- Press Command+Option+C to start/stop screen recording
- Automatic video transcription using Gemini 2.5 Flash API with visual context
- Better accuracy for programming terms, code, technical jargon, and ambiguous words
- Transcribed text automatically pastes at cursor position

## Requirements

- macOS 14.0 or later
- Xcode 15+ or Xcode Command Line Tools (for Swift 5.9+)
- Gemini API key (for text-to-speech and video transcription)
- ffmpeg (for screen recording functionality)

## System Permissions Setup

This app requires specific system permissions to function properly:

### 1. Microphone Access
The app will automatically request microphone permission on first launch. If denied, grant it manually:
- Go to **System Settings > Privacy & Security > Microphone**
- Enable access for **Super Voice Assistant**

### 2. Accessibility Access (Required for Global Hotkeys & Auto-Paste)
You must manually grant accessibility permissions for the app to:
- Monitor global keyboard shortcuts (Command+Option+Z/S/X/A/V/C, Escape)
- Automatically paste transcribed text at cursor position

**To enable:**
1. Go to **System Settings > Privacy & Security > Accessibility**
2. Click the lock icon to make changes (enter your password)
3. Click the **+** button to add an application
4. Navigate to the app location:
   - If running via `swift run`: Add **Terminal** or your terminal app (iTerm2, etc.)
   - If running the built binary directly: Add the **SuperVoiceAssistant** executable
5. Ensure the checkbox next to the app is checked

**Important:** Without accessibility access, the app cannot detect global hotkeys (Command+Option+Z/X/A/S/C/V, Escape) or paste text automatically.

### 3. Screen Recording Access (Required for Video Transcription)
The app requires screen recording permission to capture screen content:
- Go to **System Settings > Privacy & Security > Screen Recording**
- Enable access for **Terminal** (if running via `swift run`) or **SuperVoiceAssistant**

## Installation & Running

```bash
# Clone the repository
git clone https://github.com/yourusername/super-voice-assistant.git
cd super-v
```

---

## 32. antigravity-mastery-handbook-hamodywe
- **Repository ID**: `REPO_ANTIGRAVITY_MASTERY_HANDBOOK_HAMODYWE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/hamodywe/antigravity-mastery-handbook.git](https://github.com/hamodywe/antigravity-mastery-handbook.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-mastery-handbook-hamodywe`
- **Description**: Repository antigravity-mastery-handbook-hamodywe located at /Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-mastery-handbook-hamodywe

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# The Antigravity Developer's Guide
> **Your comprehensive handbook to building software with Google's AI-powered agentic IDE**

---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Windows | macOS | Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)](#)
[![Powered by: Gemini](https://img.shields.io/badge/Powered%20by-Gemini-orange.svg)](#)

## 📖 Project Overview

**The Antigravity Developer's Guide** is the definitive technical handbook for **Google Antigravity**, the revolutionary AI-powered Agentic Integrated Development Environment (AIDE) from Google DeepMind. This guide is designed for software engineers, technical leads, and development teams who want to understand, adopt, and master the agent-first development paradigm.

**Tagline:** *Stop writing code line by line. Start orchestrating AI agents to build software.*

Unlike traditional IDEs where you manually write every line of code, Antigravity introduces autonomous AI agents that can plan, implement, test, and verify entire features based on high-level objectives. This handbook provides everything you need to transition from conventional development to agentic collaboration.

### What You'll Learn

- The fundamental shift from "code-first" to "agent-first" development
- How to effectively delegate complex engineering tasks to AI agents
- Core architectural concepts: artifacts, task boundaries, and verification workflows
- Production-ready best practices for team adoption
- Security considerations and common pitfalls
- Real-world use cases and implementation patterns

---

## 📚 Table of Contents

1. [Introduction: What is Google Antigravity?](#1-introduction-what-is-google-antigravity)
2. [Core Concepts](#2-core-concepts)
   - [Agent-First Paradigm](#21-agent-first-paradigm)
   - [AI Agents & Autonomy](#22-ai-agents--autonomy)
   - [Artifacts & Verification Workflows](#23-artifacts--verification-workflows)
   - [Editor View & Manager View](#24-editor-view--manager-view)
3. [Key Features](#3-key-features)
4. [How It Works: The Agentic Development Loop](#4-how-it-works-the-agentic-development-loop)
5. [Supported AI Models and Integration](#5-supported-ai-models-and-integration)
6. [Comparison with Other Tools](#6-comparison-with-other-tools)
7. [Use Cases](#7-use-cases)
8. [Benefits and Limitations](#8-benefits-and-limitations)
9. [Getting Started and Installation](#9-getting-started-and-installation)
10. [Best Practices and Tips](#10-best-practices-and-tips)
11. [Common Misconceptions](#11-common-misconceptions)
12. [Future Directions and What's Next](#12-future-directions-and-whats-next)
13. [Glossary of Terms](#13-glossary-of-terms)
14. [References and Resources](#14-references-and-resources)
15. [Repository Structure & License](#15-repository-structure--license)

---

## 1. Introduction: What is Google Antigravity?

### Overview

**Google Antigravity** is an AI-native Integrated Development Environment launched by Google in November 2025. Built as a fork of Visual Studio Code, it combines the familiar interface developers know with a fundamentally new interaction model: **agent-first development**.

Instead of treating AI as a code completion tool or chat assistant, Antigravity positions autonomous AI agents as first-class collaborators in your development workflow. You define high-level objectives; the agent plans, implements, tests, and documents the solution.

##
```

---

## 33. fsrs-vs-sm17
- **Repository ID**: `REPO_FSRS_VS_SM17`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/open-spaced-repetition/fsrs-vs-sm17.git](https://github.com/open-spaced-repetition/fsrs-vs-sm17.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/fsrs-vs-sm17`
- **Description**: Repository fsrs-vs-sm17 located at /Users/rajondas/teamwork_projects/downloaded_wheels/fsrs-vs-sm17

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# FSRS vs SM-17
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-17-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

It is a simple comparison between FSRS and SM-17. Due to the difference between the workflow of SuperMemo and Anki, it is not easy to compare the two algorithms. I tried to make the comparison as fair as possible. Here is some notes:
- The first interval in SuperMemo is the duration between creating the card and the first review. In Anki, the first interval is the duration between the first review and the second review. So I removed the first record of each card in SM-17 data.
- There are six grades in SuperMemo, but only four grades in Anki. So I merged 0, 1 and 2 in SuperMemo to 1 in Anki, and mapped 3, 4, and 5 in SuperMemo to 2, 3, and 4 in Anki.
- I use the `R (SM17)` recorded in `sm18/systems/{collection_name}/stats/SM16-v-SM17.csv` as the prediction of SM-17. Reference: [Confusion among R(SM16), R(SM17)(exp), R(SM17), R est. and expFI.](https://supermemopedia.com/wiki/Confusion_among_R(SM16),_R(SM17)(exp),_R(SM17),_R_est._and_expFI.)
- To ensure FSRS has the same information as SM-17, I implement an [online learning](https://en.wikipedia.org/wiki/Online_machine_learning) version of FSRS, where FSRS has zero knowledge of the future reviews as SM-17 does.
- The results are based on the data from a small group of people. It may be different from the result of other SuperMemo users.

## Metrics

### Universal Metric

The Universal Metric is a mathematical tool proposed by SuperMemo for reliable comparison of different spaced repetition algorithm implementations. It measures the accuracy of retrievability predictions by comparing predicted probabilities with actual recall outcomes.

**How it works:**
- Predictions are grouped into bins based on predicted retrievability values
- Within each bin, the root mean square error is calculated between predicted and actual recall rates
- The metric is weighted by sample size in each bin
- Lower values indicate better prediction accuracy

Reference: [Universal metric for cross-comparison of spaced repetition algorithms](https://supermemo.guru/wiki/Universal_metric_for_cross-comparison_of_spaced_repetition_algorithms).

**Disclaimer**: I cannot guarantee that I have implemented the universal metric proposed by the SuperMemo team with 100% accuracy, as they have not released their evaluation code. My implementation is based solely on their documentation.

**Note**: The Universal Metric in a cross-comparison setting has a theoretical vulnerability to gaming if a model has access to all other models' predictions. Since bins are constructed based on the referee algorithm's predictions, an adversarial model could track these bins and craft predictions to minimize its Universal Metric scores across all comparisons. This is similar to the RMSE (bins) exploit. However, this vulnerability is not a practical concern for this benchmark because:
1. All code and data are open-source and transparent
2. We use multiple complementary metrics (Log Loss, AUC, RMSE) to validate results
3. Gaming attempts would be easily detectable in the community review process

#### Adversarial baseline

To demonstrate the issue concretely we include an `ADVERSARIAL` model in the benchmark results. The attacker observes every referee's probability for the current review, uses the AVG mod
```

---

## 34. iceoryx2
- **Repository ID**: `REPO_ICEORYX2`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/eclipse-iceoryx/iceoryx2.git](https://github.com/eclipse-iceoryx/iceoryx2.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/iceoryx2`
- **Description**: Repository iceoryx2 located at /Users/rajondas/teamwork_projects/downloaded_wheels/iceoryx2

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<!-- markdownlint-disable -->

[![CI](https://github.com/eclipse-iceoryx/iceoryx2/workflows/CI/badge.svg)](https://github.com/eclipse-iceoryx/iceoryx2/actions/workflows/build-test.yml?query=branch%3Amain++)
[![Codecov](https://codecov.io/gh/eclipse-iceoryx/iceoryx2/branch/main/graph/badge.svg?branch=main)](https://codecov.io/gh/eclipse-iceoryx/iceoryx2?branch=main)
[![Examples](https://img.shields.io/badge/Examples-gray)](examples/)
[![FAQ](https://img.shields.io/badge/FAQ-gray)](FAQ.md)
[![Gitter](https://badges.gitter.im/eclipse-iceoryx/iceoryx.svg)](https://gitter.im/eclipse/iceoryx)
[![Developer Meetup](https://img.shields.io/badge/Developer_Meetup-gray?style=social)](https://github.com/eclipse-iceoryx/iceoryx2/wiki/Developer-Meetup)
[![Roadmap](https://img.shields.io/badge/Roadmap-gray)](ROADMAP.md)

<p align="center">
<img src="https://github.com/eclipse-iceoryx/iceoryx2/assets/56729169/3230a125-19e5-4e98-a752-da026a086782" width="50%">
</p>

<!-- markdownlint-enable -->

# iceoryx2 - Zero-Copy Lock-Free IPC with a Rust Core

* [Introduction](#introduction)
* [Performance](#performance)
    * [Comparison Of Mechanisms](#comparison-of-mechanisms)
        * [Benchmark-System](#benchmark-system)
    * [Comparison Of Architectures](#comparison-of-architectures)
* [Documentation](#documentation)
    * [User Documentation](#user-documentation)
    * [Contributor Documentation](#contributor-documentation)
    * [API References](#api-references)
* [Supported Platforms](#supported-platforms)
* [Language Bindings](#language-bindings)
* [Commercial Support](#commercial-support)
* [Thanks To All Contributors](#thanks-to-all-contributors)

## Introduction

Welcome to iceoryx2, the efficient, and ultra-low latency inter-process
communication middleware. This library is designed to provide you with fast and
reliable zero-copy and lock-free inter-process communication mechanisms.

So if you want to communicate efficiently between multiple processes or
applications iceoryx2 is for you. With iceoryx2, you can:

* Send huge amounts of data using a publish/subscribe, request/response,
  pipeline (planned) or blackboard pattern, making it ideal
  for scenarios where large datasets need to be shared.
* Exchange signals through events, enabling quick and reliable signaling between
  processes.

iceoryx2 is based on a service-oriented architecture (SOA) and facilitates
seamless inter-process communication (IPC).

It is all about providing a seamless experience for inter-process communication,
featuring versatile messaging patterns. Whether you're diving into
publish-subscribe, events, request-response, or the promise of upcoming features
like pipelines, and blackboard, iceoryx2 has you covered.

One of the features of iceoryx2 is its consistently low transmission latency
regardless of payload size, ensuring a predictable and reliable communication
experience.

iceoryx2's origins can be traced back to
[iceoryx](https://github.com/eclipse-iceoryx/iceoryx). By overcoming past
technical debts and refining the architecture, iceoryx2 enables the modularity
we've always desired.

In the near future, iceoryx2 is poised to support at least the same feature set
and platforms as [iceoryx](https://github.com/eclipse-iceoryx/iceoryx), ensuring
a seamless transition and offering enhanced capabilities for your inter-process
communication needs. So, if you're looking for lightning-fast, cross-platform
communication that doesn't compromise on performance or modularity, i
```

---

## 35. femto-fsrs
- **Repository ID**: `REPO_FEMTO_FSRS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/RickCarlino/femto-fsrs.git](https://github.com/RickCarlino/femto-fsrs.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/femto-fsrs`
- **Description**: Repository femto-fsrs located at /Users/rajondas/teamwork_projects/downloaded_wheels/femto-fsrs

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Femto-FSRS

A zero dependency implementation of the [FSRS 5](https://github.com/open-spaced-repetition) spaced repetition algorithm.

This is the scheduler used by [Koala.Cards](https://github.com/RickCarlino/KoalaSRS).

# Demo

I made an HTML pen-and-paper demo [here](https://rickcarlino.com/srs.html). You can store facts on paper and use Femto-FSRS for scheduling, [just like Piotr Wozniak did in the 80s](https://www.supermemo.com/en/blog/the-true-history-of-spaced-repetition).

# Features

- Zero dependencies
- Follows the paper.
- Sensible defaults.

# Usage

```typescript
import { Grade, createDeck } from "femto-fsrs";

// === Create a new deck
const { newCard, gradeCard } = createDeck();

// === Initiate a new card with an initial grade of "GOOD":
const initialGrade = Grade.GOOD;
const myCard = newCard(initialGrade);

// === Grade the card as "easy" two days later.
//     Returns a new card that replaces the old one.
const daysSinceReview = 2;
const nextCard = gradeCard(myCard, daysSinceReview, Grade.EASY);
// The "I" attribute represents "I" like in the FSRS paper.
// It is the next review date at which the probability
// of success is 90% (assuming you used default parameters).
const nextReview = nextCard.I.toFixed(2);
// Print results:
console.log(`Card will be due for review in ${nextReview} day(s)`);
```

Result:

```
Card will be due for review in 16.63 day(s)
```

# Installation

```
npm install femto-fsrs
```

# Not Included

This is supposed to be a minimalistic library that can be used as a starting point
for FSRS-enhanced apps. If you need a more full-featured offering with features
like logs (so you can optimize your `w` param) or revert, etc.., check out [ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs).

# Tests

```
npm run test
```
```

---

## 36. antigravity-ai-kit-besync
- **Repository ID**: `REPO_ANTIGRAVITY_AI_KIT_BESYNC`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/besync-labs/antigravity-ai-kit.git](https://github.com/besync-labs/antigravity-ai-kit.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-ai-kit-besync`
- **Description**: Repository antigravity-ai-kit-besync located at /Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-ai-kit-besync

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# 🚀 Antigravity AI Kit

![version](https://img.shields.io/badge/version-3.10.1-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![AI Agents](https://img.shields.io/badge/AI%20Agents-20-purple)
![Skills](https://img.shields.io/badge/Skills-34-orange)
![Commands](https://img.shields.io/badge/Commands-37-red)
![Workflows](https://img.shields.io/badge/Workflows-21-teal)
![Runtime Modules](https://img.shields.io/badge/Runtime%20Modules-29-blueviolet)
![Tests](https://img.shields.io/badge/Tests-349%20passing-brightgreen)
![Checklists](https://img.shields.io/badge/Checklists-4-yellow)

<p align="center">
  <b>🎯 Transform Your IDE into an AI Engineering Team</b>
</p>

<p align="center">
  Antigravity AI Kit is a <b>Trust-Grade AI development framework</b> with a <b>29-module runtime engine</b>, <b>20 specialized agents</b>, <b>37 commands</b>, <b>34 skills</b>, and <b>21 workflows</b> — all backed by <b>349 tests</b> and governance-first principles.
</p>

<p align="center">
  🚀 <a href="#-quick-start">Quick Start</a> •
  🤖 <a href="#-agents-20">Agents</a> •
  🛠️ <a href="#%EF%B8%8F-skills-34">Skills</a> •
  ⌨️ <a href="#%EF%B8%8F-commands-37">Commands</a> •
  🔄 <a href="#-session-management">Sessions</a> •
  ⚖️ <a href="#%EF%B8%8F-operating-constraints">Governance</a> •
  📖 <a href="#-contributor-guide">Contributor Guide</a>
</p>

---

## 📚 Table of Contents

- [What is Antigravity AI Kit?](#-what-is-antigravity-ai-kit)
- [Key Features](#-key-features)
- [Quick Start](#-quick-start)
- [Architecture](#%EF%B8%8F-architecture-overview)
- [Agents](#-agents-20)
- [Commands](#%EF%B8%8F-commands-37)
- [Skills](#%EF%B8%8F-skills-34)
- [Runtime Engine](#%EF%B8%8F-runtime-engine-29-modules)
- [Workflows](#-workflows-21)
- [Operating Constraints](#%EF%B8%8F-operating-constraints)
- [Session Management](#-session-management)
- [How to Extend](#-how-to-extend)
- [Contributor Guide](#-contributor-guide)
- [Acknowledgments](#-acknowledgments)

---

## 🤔 What is Antigravity AI Kit?

**Antigravity AI Kit** transforms your IDE into a **virtual engineering team** with:

| Feature           | Count | Description                                                            |
| :---------------- | :---- | :--------------------------------------------------------------------- |
| 🤖 **AI Agents**  | 20    | Specialized roles (Mobile, DevOps, Database, Security, Performance...) |
| 🛠️ **Skills**     | 34    | Domain knowledge modules (API, Testing, MCP, Architecture, Docker...) |
| ⌨️ **Commands**   | 37    | Slash commands for every development workflow                          |
| 🔄 **Workflows**  | 21    | Process templates (/create, /debug, /deploy, /pr, /pr-merge, /test...)  |
| ⚙️ **Runtime**    | 29    | Runtime engine modules (governance, reputation, self-healing...)       |
| ✅ **Checklists** | 4     | Quality gates (session-start, session-end, pre-commit, task-complete)  |
| ⚖️ **Rules**      | 9     | Modular governance constraints (coding, security, testing, git, docs, sprint)  |
| 🔗 **Hooks**      | 8     | Event-driven automation (runtime + git-hook enforcement)               |
| 🧪 **Tests**      | 349   | Unit, structural, integration, and security tests (34 test files)      |

---

## ✨ Key Features

- **🔒 Trust-Grade Governance**: `/explore → /plan → /work → /review` — Each iteration builds context
- **🤖 Multi-Agent System**: 20 specialized agents that collaborate (Mobile Developer, DevOps, Database Architect, Sprint Orchestrator...)
- **
```

---

## 37. fsrs-rs
- **Repository ID**: `REPO_FSRS_RS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/open-spaced-repetition/fsrs-rs.git](https://github.com/open-spaced-repetition/fsrs-rs.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/fsrs-rs`
- **Description**: Repository fsrs-rs located at /Users/rajondas/teamwork_projects/downloaded_wheels/fsrs-rs

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# FSRS for Rust

[![crates.io](https://img.shields.io/crates/v/fsrs.svg)](https://crates.io/crates/fsrs) ![](https://github.com/open-spaced-repetition/fsrs-rs/actions/workflows/check.yml/badge.svg)

The Free Spaced Repetition Scheduler ([FSRS](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm)) is a modern spaced repetition algorithm. It springs from [MaiMemo's DHP model](https://www.maimemo.com/paper/), which is a variant of the [DSR model](https://supermemo.guru/wiki/Three_component_model_of_memory) proposed by [Piotr Wozniak](https://supermemo.guru/wiki/Piotr_Wozniak).

FSRS-rs is a Rust implementation of FSRS. It also provides simulation capabilities and basic scheduling functionality.

For more information about the algorithm, please refer to [the wiki page of FSRS](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm).

---

## Quickstart

### Add the crate

Add FSRS to your project:

```sh
cargo add fsrs
```

The scheduling example below also uses `chrono` to track review times:

```toml
chrono = { version = "0.4", default-features = false, features = ["std", "clock"] }
```

Run `cargo run --example <name>` to see the complete samples ([`schedule`](examples/schedule.rs), [`migrate`](examples/migrate.rs), [`optimize`](examples/optimize.rs), [`cost_adr`](examples/cost_adr.rs)).

### Schedule reviews

```rust
use chrono::{Duration, Utc};
use fsrs::{FSRS, MemoryState};

let fsrs = FSRS::default();
let desired_retention = 0.9;
let previous_state: Option<MemoryState> = None;
let elapsed_days = 0;

let next_states = fsrs.next_states(previous_state, desired_retention, elapsed_days)?;
let review = next_states.good;

let interval_days = review.interval.round().max(1.0) as u32;
let due = Utc::now() + Duration::days(interval_days as i64);
```

Replace `previous_state`/`elapsed_days` with a stored `MemoryState` and the number of days since the prior review when scheduling existing cards. Full example: [`examples/schedule.rs`](examples/schedule.rs).

### Optimize parameters from review logs

```rust
use chrono::NaiveDate;
use fsrs::{ComputeParametersInput, FSRSItem, FSRSReview, compute_parameters};

let history = vec![
    (NaiveDate::from_ymd_opt(2023, 1, 1).unwrap(), 3),
    (NaiveDate::from_ymd_opt(2023, 1, 5).unwrap(), 4),
];

let mut accumulated = Vec::new();
let mut items = Vec::new();
let mut last = history[0].0;

for (date, rating) in history {
    let delta_t = (date - last).num_days() as f32;
    accumulated.push(FSRSReview { rating, delta_t });
    items.push(FSRSItem {
        reviews: accumulated.clone(),
    });
    last = date;
}

let parameters = compute_parameters(ComputeParametersInput {
    // For best results, `train_set` should contain review histories from many cards.
    train_set: items,
    ..Default::default()
})?;
```

Feed the optimizer a vector of `FSRSItem` instances built from your review history; the returned parameters can then be persisted or supplied to schedulers. Full example: [`examples/optimize.rs`](examples/optimize.rs).

### Train and use a single-user Cost ADR policy

`fsrs-rs` also includes a CPU/Rayon single-user optimizer for the FSRS-6 and FSRS-7 Cost ADR policy. It searches a 15-parameter cost-conditioned desired-retention policy and evaluates it against a fixed 16-point desired-retention baseline portfolio. The report includes hypervolume, same-target time-saved AUC, relative same-target time-saved AUC, and memory-span coverage.

```sh
cargo run --release --
```

---

## 38. jarvis
- **Repository ID**: `REPO_JARVIS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/ethanplusai/jarvis.git](https://github.com/ethanplusai/jarvis.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/jarvis`
- **Description**: Repository jarvis located at /Users/rajondas/teamwork_projects/downloaded_wheels/jarvis

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# JARVIS

**Just A Rather Very Intelligent System — a voice for Claude Code.**

JARVIS is a British butler who sits on top of the Claude Code you already pay
for. You talk to him. He brainstorms a project with you out loud, one question
at a time; when you have settled on something he writes the design down as a
file in your project; then he starts a real Claude Code session on it and
drives it through plan → review → execute. While it runs he watches every
Claude Code session on your machine, and when one of them is stuck waiting on
a human he tells you which one, out loud, without you having to look.

> "Will do, sir."

![Six seconds of the JARVIS orb while he is speaking, looping. Two thousand
particles hold the shape of a hollow blue sphere, wired together by faint lines
between the ones that drift close enough; a bright rim catches its lower edge.
Through each spoken phrase the sphere swells and brightens and leans towards
you, then falls back and contracts through the pause before the next one, three
times over, while the camera drifts a few degrees around
it.](docs/images/orb-speaking.gif)

*What you actually look at while you talk to him: `frontend/src/orb.ts`,
rendered live. The audio driving the pulse is synthetic — a speech-shaped
envelope fitted to a measurement of the real analyser, not a recording of his
voice — but every pixel is that file running. Regenerate with
`scripts/make_orb_loop.py`.*

![A twenty-three second walkthrough of the JARVIS dashboard, looping. It opens
on Runs: a red "Needs Attention" panel over a failed run and a timed-out one,
then Active and History, every row carrying the project, the prompt, a status
pill, elapsed time and tokens. A run opens to show its prompt, cost, model and
live transcript. The Sessions tab shows every Claude Code conversation on the
machine grouped by project; clicking a blocked one swaps the right-hand column
from a tally into a red band reading "waiting on you for 51m — permission
prompt", with the question the CLI actually asked quoted underneath. Specs
shows a design document with big numbered sections you answer by voice.
Projects drills into one project's conversations, runs and build progress.
Usage ends on the subscription's two gauges — a five-hour window at 62 per
cent and a seven-day one at 84 per cent.](docs/images/dashboard-walkthrough.gif)

*The whole dashboard, clicked through. Fictional sample data throughout — the
projects, prompts, people and figures in every screenshot on this page are
invented.*

---

## What it costs

**No AI API usage, and none is possible.** JARVIS's brain is a Claude Code
process running on *your* Claude subscription — the same login you use in the
terminal. There is no Anthropic API key anywhere on the voice path, and there
is no way to accidentally put one there:

```python
# claude_env.py
SCRUBBED_ENV_PREFIXES = ("CLAUDE_CODE_", "ANTHROPIC_")
SCRUBBED_ENV_KEYS = {"CLAUDECODE"}
```

Every Claude Code process JARVIS spawns — the brain and every build — is
launched through `claude_env.child_env()`, which strips **every** `ANTHROPIC_*`
variable out of the environment first. This is deliberate and it is not a
nicety: the CLI silently *prefers* an inherited `ANTHROPIC_API_KEY` over your
login, and `claude auth status` goes on reporting `loggedIn: true` while
billing quietly moves onto the key. So JARVIS removes the key rather than
trusting itself not to pass it. Leave one in your `.env` if you like — the
startup check will warn you it is t
```

---

## 39. antigravity-skills-rmyndharis
- **Repository ID**: `REPO_ANTIGRAVITY_SKILLS_RMYNDHARIS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rmyndharis/antigravity-skills.git](https://github.com/rmyndharis/antigravity-skills.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-skills-rmyndharis`
- **Description**: Repository antigravity-skills-rmyndharis located at /Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-skills-rmyndharis

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Antigravity Skill Vault

A curated collection of **Agent Skills** for **Google Antigravity**, ported from the [Claude Code Agents](https://github.com/wshobson/agents) repository.

This vault transforms the extensive Claude Code ecosystem into **Antigravity Skills**, providing your agent with repeatable workflows, domain expertise, and specialized tools.

---

## 🚀 Overview

This repository contains **300+ specialized skills** across software development, operations, security, and business domains. Each skill is a directory-based package that teaches Antigravity's agent how to perform specific tasks.

### What's Included?

The skills are derived from three types of Claude Code components, all unified into the Antigravity Skill format:

1.  **Domain Skills** (e.g., `k8s-manifest-generator`, `async-python-patterns`): Specialized knowledge packages.
2.  **Specialist Agents** (e.g., `backend-architect`, `security-auditor`): Persona-based instruction sets for complex reasoning.
3.  **Commands & Workflows** (e.g., `full-stack-orchestration-full-stack-feature`, `conductor-implement`): Structured, multi-step procedures.

---

## 📂 Categories

Skills are flattened in the `skills/` directory, but cover these broad categories:

### 💻 Development & Languages
- **Python**: `python-pro`, `fastapi-pro`, `async-python-patterns`, `uv-package-manager`
- **JavaScript/TypeScript**: `typescript-pro`, `react-modernization`, `nextjs-app-router-patterns`
- **Systems**: `rust-pro`, `golang-pro`, `memory-safety-patterns`
- **Mobile**: `frontend-mobile-development-component-scaffold`, `react-native-architecture`

### ☁️ Infrastructure & Operations
- **Kubernetes**: `kubernetes-architect`, `helm-chart-scaffolding`, `gitops-workflow`
- **Cloud**: `cloud-architect`, `terraform-module-library`, `cost-optimization`
- **CI/CD**: `cicd-automation-workflow-automate`, `github-actions-templates`, `gitlab-ci-patterns`

### 🔒 Security & Quality
- **Security**: `security-auditor`, `sast-configuration`, `security-scanning-security-hardening`
- **Code Quality**: `code-review-ai-ai-review`, `code-refactoring-refactor-clean`, `codebase-cleanup-tech-debt`
- **Testing**: `unit-testing-test-generate`, `tdd-workflows-tdd-cycle`, `e2e-testing-patterns`

### 🔄 Workflows & Architecture
- **Conductor**: `conductor-implement`, `context-driven-development` (Context-Driven Development)
- **Architecture**: `c4-architecture-c4-architecture`, `microservices-patterns`, `api-design-principles`
- **Orchestration**: `full-stack-orchestration-full-stack-feature`, `incident-response-incident-response`

### 📊 Data & AI
- **Data Engineering**: `data-engineer`, `spark-optimization`, `dbt-transformation-patterns`
- **AI/ML**: `ml-pipeline-workflow`, `prompt-engineering-patterns`, `rag-implementation`

---

## 🎯 Install Strategically (Token Efficient)

Antigravity loads metadata (name + description) from every installed skill at session start. More skills means more token usage and a higher chance of irrelevant auto-activation. Prefer targeted installs via search, tags, or bundles. `install --all` is advanced and not recommended for most projects.

## 🧭 Catalog & Discovery

This repo ships a generated catalog for discovery:

- `CATALOG.md` (human-readable index)
- `catalog.json` (machine-readable index used by the CLI)
- `bundles.json` (curated bundles)
- `aliases.json` (short names that map to long skill IDs)

Regenerate after adding/editing skills:

```bash
npm run build:catalog
```

## 🛠️ How to Use

```

---

## 40. fsrs4anki-helper
- **Repository ID**: `REPO_FSRS4ANKI_HELPER`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/open-spaced-repetition/fsrs4anki-helper.git](https://github.com/open-spaced-repetition/fsrs4anki-helper.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/fsrs4anki-helper`
- **Description**: Repository fsrs4anki-helper located at /Users/rajondas/teamwork_projects/downloaded_wheels/fsrs4anki-helper

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# FSRS Helper

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

FSRS Helper is an Anki add-on that supports [FSRS](https://github.com/open-spaced-repetition/fsrs4anki) algorithm. It has the following main features:

- **Reschedule** cards based on their entire review histories.
- **Postpone** a selected number of due cards.
- **Advance** a selected number of undue cards.
- **Schedule a Break** to redistribute cards due during an upcoming period when you'll be away from Anki.
- **Balance** the load during rescheduling (based on fuzz).
- Less Anki on **Easy Days** (such as weekends) during rescheduling (based on load balance).
- **Disperse** Siblings (cards with the same note) to avoid interference & reminder.
- **Flatten** future due cards to a selected number of reviews per day.
- **Remedy Hard Misuse** to correct historical Hard button misuse by converting Hard reviews to Again.
- **Reset** to clear custom data or manual rescheduling records.
- **Steps Stats** quantify your short-term memory performance and recommend learning steps.

# Requirements

- For Anki version >= 23.10
  - Enable built-in FSRS (follow this [tutorial](https://github.com/open-spaced-repetition/fsrs4anki/blob/main/docs/tutorial.md))
  - Remove FSRS4Anki custom scheduling code if you are already using it
- For Anki version in 2.1.55 - 2.1.66 (no longer maintained)
  - Enable V3 Scheduler
  - FSRS4Anki version >= 3.0.0

# Installation

The FSRS Helper add-on is purely an added bonus and is not recommended for extensive use.

Installation link: https://ankiweb.net/shared/info/759844606

# Usage

## Overview

| Feature name      | How does it work?                                            | When should I use it?                                        |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Reschedule        | Calculates stability, difficulty, and the optimum interval from the entire review history for each card using FSRS parameters. Then, it changes the due dates of cards. | When you update the parameters or desired retention of FSRS. Rescheduling with the Helper does not add to the size of your collection, unlike Anki's built-in "Reschedule cards on change." |
| Advance           | Decreases the intervals of undue cards based on current and requested R, and interval length to minimize damage to long-term learning. | When you want to review your material ahead of time, for example, before a test. |
| Postpone          | Increases the intervals of cards that are due today based on current and requested R, and interval length in a way that minimizes damage to long-term learning. | When you are dealing with a large number of reviews after taking a break from Anki or after rescheduling. |
| Schedule a Break  | Redistributes cards due during an upcoming break period (including overdue cards and cards due today) across follow-up days. Uses a cost function to minimize deviation from original due dates. | When you know you'll be away from Anki for a period (e.g., vacation, busy work period) and want to proactively redistribute reviews. |
| Load Balancing    | After the optimal interval is calculated, it is adjusted by a random amount to make the distribution of reviews over time more uniform. | Always. This feature makes your workload (reviews per day) more consistent. |
| Easy Days         | After 
```

---

## 41. gemini-live-api-examples
- **Repository ID**: `REPO_GEMINI_LIVE_API_EXAMPLES`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/google-gemini/gemini-live-api-examples.git](https://github.com/google-gemini/gemini-live-api-examples.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/gemini-live-api-examples`
- **Description**: Repository gemini-live-api-examples located at /Users/rajondas/teamwork_projects/downloaded_wheels/gemini-live-api-examples

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Gemini Live API Examples

The Live API enables low-latency, real-time voice and video interactions with
Gemini. It processes continuous streams of audio, video, or text to deliver
immediate, human-like spoken responses, creating a natural conversational
experience for your users.

![Live API Overview](https://ai.google.dev/gemini-api/docs/images/live-api-overview.png)

[Try the Live API in Google AI Studio](https://aistudio.google.com/live)

## Example use cases

Live API can be used to build real-time voice and video agents for a
variety of industries, including:

*   **E-commerce and retail:** Shopping assistants that offer personalized
    recommendations and support agents that resolve customer issues.
*   **Gaming:** Interactive non-player characters (NPCs), in-game help
    assistants, and real-time translation of in-game content.
*   **Next-gen interfaces:** Voice- and video-enabled experiences in robotics,
    smart glasses, and vehicles.
*   **Healthcare:** Health companions for patient support and education.
*   **Financial services:** AI advisors for wealth management and investment
    guidance.
*   **Education:** AI mentors and learner companions that provide personalized
    instruction and feedback.

## Key features

Live API offers a comprehensive set of features for building
robust voice and video agents:

*   [**Multilingual support**](https://ai.google.dev/gemini-api/docs/live-guide#supported-languages):
    Converse in 70 supported languages.
*   [**Barge-in**](https://ai.google.dev/gemini-api/docs/live-guide#interruptions):
    Users can interrupt the model at any time for responsive interactions.
*   [**Tool use**](https://ai.google.dev/gemini-api/docs/live-tools):
    Integrates tools like function calling and Google Search for dynamic
    interactions.
*   [**Audio transcriptions**](https://ai.google.dev/gemini-api/docs/live-guide#audio-transcription):
    Provides text transcripts of both user input and model output.
*   [**Proactive audio**](https://ai.google.dev/gemini-api/docs/live-guide#proactive-audio):
    Lets you control when the model responds and in what contexts.
*   [**Affective dialog**](https://ai.google.dev/gemini-api/docs/live-guide#affective-dialog):
    Adapts response style and tone to match the user's input expression.

## Technical specifications

The following table outlines the technical specifications for the
Live API:

| Category          | Details                                                                                     |
| :---------------- | :------------------------------------------------------------------------------------------ |
| Input modalities  | Audio (raw 16-bit PCM audio, 16kHz, little-endian), images/video (JPEG <= 1FPS), text       |
| Output modalities | Audio (raw 16-bit PCM audio, 24kHz, little-endian), text                                    |
| Protocol          | Stateful WebSocket connection (WSS)                                                         |

## Examples

*   **[Gen AI SDK Python example](./gemini-live-genai-python-sdk/README.md)**: Recommended for ease of use. Connect to the Gemini Live API using the Gen AI SDK to build a real-time multimodal application with a Python backend.
*   **[Epheremal tokens and raw WebSocket example](./gemini-live-ephemeral-tokens-websocket/README.md)**: RAW protocol control. Connect to the Gemini Live API using WebSockets to build a real-time multimodal application with a JavaScript frontend and a Python backen
```

---

## 42. srs-benchmark
- **Repository ID**: `REPO_SRS_BENCHMARK`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/open-spaced-repetition/srs-benchmark.git](https://github.com/open-spaced-repetition/srs-benchmark.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/srs-benchmark`
- **Description**: Repository srs-benchmark located at /Users/rajondas/teamwork_projects/downloaded_wheels/srs-benchmark

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# SRS Benchmark

## Introduction

Spaced repetition algorithms are computer programs designed to help people schedule reviews of flashcards. A good spaced repetition algorithm helps you remember things more efficiently. Instead of cramming all at once, it distributes your reviews over time. To make this efficient, these algorithms try to understand how your memory works. They aim to predict when you're likely to forget something, so they can schedule a review accordingly.

This benchmark is designed to assess the predictive accuracy of various algorithms. A multitude of algorithms are evaluated to find out which ones provide the most accurate predictions.

**We will evaluate your algorithm! [Open a GitHub issue](https://github.com/open-spaced-repetition/srs-benchmark/issues/new) or contact [L-M-Sherlock](https://github.com/L-M-Sherlock).**

## Dataset

~~The dataset for the SRS benchmark comes from 20 thousand people who use Anki, a flashcard app. In total, this dataset contains information about \~1.7 billion reviews of flashcards. The full dataset is hosted on Hugging Face Datasets: [open-spaced-repetition/FSRS-Anki-20k](https://huggingface.co/datasets/open-spaced-repetition/FSRS-Anki-20k).~~

The dataset for the SRS benchmark comes from 10 thousand users who use Anki, a flashcard app. In total, this dataset contains information about ~727 million reviews of flashcards. The full dataset is hosted on Hugging Face Datasets: [open-spaced-repetition/anki-revlogs-10k](https://huggingface.co/datasets/open-spaced-repetition/anki-revlogs-10k).

## Evaluation

### Data Split

In the SRS benchmark, we use a tool called `TimeSeriesSplit`. This is part of the [sklearn](https://scikit-learn.org/) library used for machine learning. The tool helps us split the data by time: older reviews are used for training and newer reviews for testing. That way, we don't accidentally cheat by giving the algorithm future information it shouldn't have. In practice, we use past study sessions to predict future ones. This makes `TimeSeriesSplit` a good fit for our benchmark.

Note: TimeSeriesSplit will remove the first split from evaluation. This is because the first split is used for training, and we don't want to evaluate the algorithm on the same data it was trained on.

RWKV and RMSE-BINS-EXPLOIT do not use TimeSeriesSplit.

### Metrics

We use three metrics in the SRS benchmark to evaluate how well these algorithms work: Log Loss, AUC, and a custom RMSE that we call RMSE (bins).

- Log Loss (also known as Binary Cross Entropy): used primarily in binary classification problems, Log Loss serves as a measure of the discrepancies between predicted probabilities of recall and review outcomes (1 or 0). It quantifies how well the algorithm approximates the true recall probabilities. Log Loss ranges from 0 to infinity, lower is better.
- Root Mean Square Error in Bins (RMSE (bins)): this is a metric designed for use in the SRS benchmark. In this approach, predictions and review outcomes are grouped into bins based on three features: the interval length, the number of reviews, and the number of lapses. Within each bin, the squared difference between the average predicted probability of recall and the average recall rate is calculated. These values are then weighted according to the sample size in each bin, and then the final weighted root mean square error is calculated. This metric provides a nuanced understanding of algorithm performance across different probability r
```

---

## 43. OmniAntigravityRemoteChat
- **Repository ID**: `REPO_OMNIANTIGRAVITYREMOTECHAT`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/diegosouzapw/OmniAntigravityRemoteChat.git](https://github.com/diegosouzapw/OmniAntigravityRemoteChat.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/OmniAntigravityRemoteChat`
- **Description**: Repository OmniAntigravityRemoteChat located at /Users/rajondas/teamwork_projects/downloaded_wheels/OmniAntigravityRemoteChat

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<div align="center">

# 📱 OmniAntigravity Remote Chat

### Your AI coding session shouldn't end when you leave your desk.

<br/>

<img src="assets/hero-banner.png" alt="Control your AI from the couch" width="700" />

<br/>
<br/>

![Version](https://img.shields.io/badge/version-1.3.0-6366f1) ![Node](https://img.shields.io/badge/node-22%2B-10b981) ![CI](https://github.com/diegosouzapw/OmniAntigravityRemoteChat/actions/workflows/ci.yml/badge.svg) ![License](https://img.shields.io/badge/license-GPL--3.0-blue)

[![npm](https://img.shields.io/npm/v/omni-antigravity-remote-chat?color=cc3534&logo=npm)](https://www.npmjs.com/package/omni-antigravity-remote-chat) [![npm downloads](https://img.shields.io/npm/dm/omni-antigravity-remote-chat?color=blue&logo=npm)](https://www.npmjs.com/package/omni-antigravity-remote-chat) [![Docker](https://img.shields.io/docker/pulls/diegosouzapw/omni-antigravity-remote-chat?color=2496ED&logo=docker&logoColor=white)](https://hub.docker.com/r/diegosouzapw/omni-antigravity-remote-chat)

**Mirror your Antigravity (Windsurf) AI chat on your phone in real-time.**
<br/>
**Send messages. Switch models. Manage windows. All from your mobile browser.**

[Get Started](#-get-started) · [Screenshots](#-see-it-in-action) · [How It Works](#-how-it-works) · [Docker](https://hub.docker.com/r/diegosouzapw/omni-antigravity-remote-chat) · [npm](https://www.npmjs.com/package/omni-antigravity-remote-chat)

🌐 **Available in:** 🇺🇸 English | 🇧🇷 [Português (Brasil)](README.pt-BR.md) | 🇪🇸 [Español](README.es.md) | 🇫🇷 [Français](README.fr.md) | 🇮🇹 [Italiano](README.it.md) | 🇷🇺 [Русский](README.ru.md) | 🇨🇳 [中文 (简体)](README.zh-CN.md) | 🇩🇪 [Deutsch](README.de.md) | 🇮🇳 [हिन्दी](README.in.md) | 🇹🇭 [ไทย](README.th.md) | 🇺🇦 [Українська](README.uk-UA.md) | 🇸🇦 [العربية](README.ar.md) | 🇯🇵 [日本語](README.ja.md) | 🇻🇳 [Tiếng Việt](README.vi.md) | 🇧🇬 [Български](README.bg.md) | 🇩🇰 [Dansk](README.da.md) | 🇫🇮 [Suomi](README.fi.md) | 🇮🇱 [עברית](README.he.md) | 🇭🇺 [Magyar](README.hu.md) | 🇮🇩 [Bahasa Indonesia](README.id.md) | 🇰🇷 [한국어](README.ko.md) | 🇲🇾 [Bahasa Melayu](README.ms.md) | 🇳🇱 [Nederlands](README.nl.md) | 🇳🇴 [Norsk](README.no.md) | 🇵🇹 [Português (Portugal)](README.pt.md) | 🇷🇴 [Română](README.ro.md) | 🇵🇱 [Polski](README.pl.md) | 🇸🇰 [Slovenčina](README.sk.md) | 🇸🇪 [Svenska](README.sv.md) | 🇵🇭 [Filipino](README.phi.md)

</div>

<br/>

## 😤 The Problem

You're deep into an AI-assisted coding session. Claude is generating code, Gemini is reviewing your architecture. Then your phone rings, someone needs you in the kitchen, or you just want to move to the couch.

**Your options today:**

- ❌ Walk back to the desk every time the AI responds
- ❌ Try to read your monitor from across the room
- ❌ Copy-paste into a separate mobile app (losing context)
- ❌ Just... stop coding

**There has to be a better way.**

## ✅ The Solution

OmniAntigravity mirrors your **entire Antigravity AI chat** to your phone — in real-time, with full interaction. Read responses, send follow-up messages, switch AI models, even manage multiple editor windows. All from your mobile browser.

```bash
npx omni-antigravity-remote-chat
```

That's it. Open the URL on your phone. You're in. 🚀

### New in 1.3.0

- **Content Security Policy** — Strict CSP with zero inline JS, enforced via header + meta tags
- **Pinggy tunnel support** — SSH-based tunneling with zero binary dependencies
- **Leaf-node targeting** — Precise DOM click targeting with occurrence index tracking
- **Multi-tunnel manageme
```

---

## 44. antigravity-awesome-skills-ar27111994
- **Repository ID**: `REPO_ANTIGRAVITY_AWESOME_SKILLS_AR27111994`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/ar27111994/antigravity-awesome-skills.git](https://github.com/ar27111994/antigravity-awesome-skills.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-awesome-skills-ar27111994`
- **Description**: Repository antigravity-awesome-skills-ar27111994 located at /Users/rajondas/teamwork_projects/downloaded_wheels/antigravity-awesome-skills-ar27111994

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<!-- registry-sync: version=9.5.1; skills=1344; stars=30283; updated_at=2026-04-03T16:35:06+00:00 -->
# 🌌 Antigravity Awesome Skills: 1,344+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

> **Installable GitHub library of 1,344+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and other AI coding assistants.**

Antigravity Awesome Skills is an installable GitHub library and npm installer for reusable `SKILL.md` playbooks. It is designed for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, Kiro, OpenCode, GitHub Copilot, and other AI coding assistants that benefit from structured operating instructions. Instead of collecting one-off prompt snippets, this repository gives you a searchable, installable catalog of skills, bundles, workflows, plugin-safe distributions, and practical docs that help agents perform recurring tasks with better context, stronger constraints, and clearer outputs.

You can use this repo to install a broad multi-tool skill library, start from role-based bundles, or jump into workflow-driven execution for planning, coding, debugging, testing, security review, infrastructure, product work, and growth tasks. The root README is intentionally a high-signal landing page: understand what the project is, install it quickly, choose the right tool path, and then follow deeper docs only when you need them.

**Start here:** [Star the repo](https://github.com/sickn33/antigravity-awesome-skills/stargazers) · [Install in 1 minute](#installation) · [Choose your tool](#choose-your-tool) · [Best skills by tool](#best-skills-by-tool) · [📚 Browse 1,344+ Skills](#browse-1344-skills) · [Bundles](docs/users/bundles.md) · [Workflows](docs/users/workflows.md) · [Plugins for Claude Code and Codex](docs/users/plugins.md)

[![GitHub stars](https://img.shields.io/badge/⭐%2030%2C000%2B%20Stars-gold?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Latest Release](https://img.shields.io/github/v/release/sickn33/antigravity-awesome-skills?display_name=tag&style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/releases/latest)
[![Install with NPX](https://img.shields.io/badge/Install-npx%20antigravity--awesome--skills-black?style=for-the-badge&logo=npm)](#installation)
[![Kiro](https://img.shields.io/badge/Kiro-AWS-orange?style=for-the-badge)](https://kiro.dev)
[![Copilot](https://img.shields.io/badge/Copilot-GitHub-lightblue?style=for-the-badge)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray?style=for-the-badge)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-AI%20IDE-red?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills)

**Current release: V9.5.1.** Trusted by 30k+ GitHub stargazers, this repository combines official and community skill collections with bundles, workflows, installation paths, and docs that help you go from first inst
```

---

## 45. yomitan
- **Repository ID**: `REPO_YOMITAN`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/themoeway/yomitan.git](https://github.com/themoeway/yomitan.git)
- **Local Disk Path**: `/Users/rajondas/teamwork_projects/downloaded_wheels/yomitan`
- **Description**: Repository yomitan located at /Users/rajondas/teamwork_projects/downloaded_wheels/yomitan

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Yomitan

[![Get Yomitan for Chrome](<https://img.shields.io/chrome-web-store/v/likgccmbimhjbgkjambclfkhldnlhbnn?logo=Google%20Chrome&style=for-the-badge&logoColor=lightblue&color=lightblue&label=get%20yomitan%20for%20chrome%20(stable)>)](https://chrome.google.com/webstore/detail/yomitan/likgccmbimhjbgkjambclfkhldnlhbnn)
[![Get Yomitan for Firefox](<https://img.shields.io/amo/v/yomitan?logo=Firefox&style=for-the-badge&color=orange&label=get%20yomitan%20for%20firefox%20(stable)>)](https://addons.mozilla.org/en-US/firefox/addon/yomitan/)
[![Get Yomitan for Edge](https://img.shields.io/badge/dynamic/json?logo=puzzle&label=get%20yomitan%20for%20edge&style=for-the-badge&query=%24.version&url=https%3A%2F%2Fmicrosoftedge.microsoft.com%2Faddons%2Fgetproductdetailsbycrxid%2Fidelnfbbmikgfiejhgmddlbkfgiifnnn)](https://microsoftedge.microsoft.com/addons/detail/yomitan/idelnfbbmikgfiejhgmddlbkfgiifnnn)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/yomidevs/yomitan/badge?style=for-the-badge)](https://securityscorecards.dev/viewer/?uri=github.com/yomidevs/yomitan)

[![Discord](https://dcbadge.limes.pink/api/server/YkQrXW6TXF?style=for-the-badge)](https://discord.gg/YkQrXW6TXF)

# Visit [yomitan.wiki](https://yomitan.wiki) to learn more!

:wave: **Yomitan is [the successor](https://foosoft.net/posts/passing-the-torch-to-yomitan/) to Yomichan** ([migration guide](https://yomitan.wiki/yomichan-migration/)) which was [sunset](https://foosoft.net/posts/sunsetting-the-yomichan-project/) by its owner on Feb 26, 2023. We have made a number of foundational changes to ensure **the project stays alive, works on latest browser versions, and is easy to contribute to**.

📢 **New contributors [welcome](#contributing)!**

📢 **Interested in adding a new language to Yomitan? See [here](./docs/development/language-features.md) for thorough documentation!**

## What is Yomitan?

Yomitan turns your web browser into a tool for building language literacy by helping you **read** texts that would otherwise be too difficult to tackle in [a variety of supported languages](https://yomitan.wiki/supported-languages/).

Yomitan provides powerful features not available in other browser-based dictionaries:

- 💬 Interactive popup definition window for displaying search results.
- 🔊 Built-in native pronunciation audio with the ability to add your own [custom audio sources](https://yomitan.wiki/advanced/#default-audio-sources).
- ✍️ Kanji stroke order diagrams are just a click away.
- 📝 [Automatic flashcard creation](https://yomitan.wiki/anki/) for the [Anki](https://apps.ankiweb.net/) flashcard program via the [AnkiConnect](https://git.sr.ht/~foosoft/anki-connect) plugin.
- 🔍 Custom search page for easily executing custom search queries.
- 📖 Support for multiple dictionary formats including [EPWING](https://ja.wikipedia.org/wiki/EPWING) via the [Yomitan Import](https://github.com/yomidevs/yomitan-import) tool.
- ✨ Clean, modern code makes it easy for developers to [contribute](#contributing) new features and languages.

[![Term definitions](img/ss-terms-thumb.png)](img/ss-terms.png)
[![Kanji information](img/ss-kanji-thumb.png)](img/ss-kanji.png)
[![Dictionary options](img/ss-dictionaries-thumb.png)](img/ss-dictionaries.png)
[![Anki options](img/ss-anki-thumb.png)](img/ss-anki.png)

## Documentation/How To

**Please visit the [Yomitan Wiki](https://yomitan.wiki) for the most up-to-date usage documentation.**

### Developer Documentation

- Dictionaries
 
```

---

## 46. smart-coding-mcp
- **Repository ID**: `REPO_SMART_CODING_MCP`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/omar-haris/smart-coding-mcp.git](https://github.com/omar-haris/smart-coding-mcp.git)
- **Local Disk Path**: `/Users/rajondas/.air1/smart-coding-mcp`
- **Description**: Repository smart-coding-mcp located at /Users/rajondas/.air1/smart-coding-mcp

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
# Smart Coding MCP

[![npm version](https://img.shields.io/npm/v/smart-coding-mcp.svg)](https://www.npmjs.com/package/smart-coding-mcp)
[![npm downloads](https://img.shields.io/npm/dm/smart-coding-mcp.svg)](https://www.npmjs.com/package/smart-coding-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D18-green.svg)](https://nodejs.org/)

An extensible Model Context Protocol (MCP) server that provides intelligent semantic code search for AI assistants. Built with local AI models using Matryoshka Representation Learning (MRL) for flexible embedding dimensions (64-768d).

## What This Does

AI coding assistants work better when they can find relevant code quickly. Traditional keyword search falls short - if you ask "where do we handle authentication?" but your code uses "login" and "session", keyword search misses it.

This MCP server solves that by indexing your codebase with AI embeddings. Your AI assistant can search by meaning instead of exact keywords, finding relevant code even when the terminology differs.

![Example](example.png)

## Available Tools

### 🔍 `a_semantic_search` - Find Code by Meaning

The primary tool for codebase exploration. Uses AI embeddings to understand what you're looking for, not just match keywords.

**How it works:** Converts your natural language query into a vector, then finds code chunks with similar meaning using cosine similarity + exact match boosting.

**Best for:**
- Exploring unfamiliar codebases: `"How does authentication work?"`
- Finding related code: `"Where do we validate user input?"`
- Conceptual searches: `"error handling patterns"`
- Works even with typos: `"embeding modle initializashun"` still finds embedding code

**Example queries:**
```
"Where do we handle cache persistence?"
"How is the database connection managed?"
"Find all API endpoint definitions"
```

---

### 📦 `d_check_last_version` - Package Version Lookup

Fetches the latest version of any package from its official registry. Supports 20+ ecosystems.

**How it works:** Queries official package registries (npm, PyPI, Crates.io, etc.) in real-time. No guessing, no stale training data.

**Supported ecosystems:** npm, PyPI, Crates.io, Maven, Go, RubyGems, NuGet, Packagist, Hex, pub.dev, Homebrew, Conda, and more.

**Best for:**
- Before adding dependencies: `"express"` → `4.18.2`
- Checking for updates: `"pip:requests"` → `2.31.0`
- Multi-ecosystem projects: `"npm:react"`, `"go:github.com/gin-gonic/gin"`

**Example usage:**
```
"What's the latest version of lodash?"
"Check if there's a newer version of axios"
```

---

### 🔄 `b_index_codebase` - Manual Reindexing

Triggers a full reindex of your codebase. Normally not needed since indexing is automatic and incremental.

**How it works:** Scans all files, generates new embeddings, and updates the SQLite cache. Uses progressive indexing so you can search while it runs.

**When to use:**
- After major refactoring or branch switches
- After pulling large changes from remote
- If search results seem stale or incomplete
- After changing embedding configuration (dimension, model)

---

### 🗑️ `c_clear_cache` - Reset Everything

Deletes the embeddings cache entirely, forcing a complete reindex on next search.

**How it works:** Removes the `.smart-coding-cache/` directory. Next search or index operation starts fresh.

**When to use:**
- Cache corruption (rare, but possible)
- 
```

---

## 47. fastmcp
- **Repository ID**: `REPO_FASTMCP`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/jlowin/fastmcp.git](https://github.com/jlowin/fastmcp.git)
- **Local Disk Path**: `/Users/rajondas/.air1/downloaded_wheels_vault/fastmcp`
- **Description**: Repository fastmcp located at /Users/rajondas/.air1/downloaded_wheels_vault/fastmcp

### 📖 Architecture & Technical Specifications (README Extract):
```markdown
<div align="center">

<!-- omit in toc -->

<picture>
  <source width="550" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-4-dark.png">
  <source width="550" media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-4.png">
  <img width="550" alt="FastMCP Logo" src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/brand/f-watercolor-waves-2.png">
</picture>

# FastMCP 🚀

<strong>Move fast and make things.</strong>

*Made with 💙 by [Prefect](https://www.prefect.io/)*

[![Docs](https://img.shields.io/badge/docs-gofastmcp.com-blue)](https://gofastmcp.com)
[![Discord](https://img.shields.io/badge/community-discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/uu8dJCgttd)
[![PyPI - Version](https://img.shields.io/pypi/v/fastmcp.svg)](https://pypi.org/project/fastmcp)
[![TypeScript](https://img.shields.io/npm/v/%40prefecthq%2Ffastmcp-ts?label=typescript&color=3178c6)](https://github.com/PrefectHQ/fastmcp-ts)
[![Tests](https://github.com/PrefectHQ/fastmcp/actions/workflows/run-tests.yml/badge.svg)](https://github.com/PrefectHQ/fastmcp/actions/workflows/run-tests.yml)
[![License](https://img.shields.io/github/license/PrefectHQ/fastmcp.svg)](https://github.com/PrefectHQ/fastmcp/blob/main/LICENSE)

<a href="https://trendshift.io/repositories/21461" target="_blank"><img src="https://trendshift.io/api/badge/repositories/21461" alt="prefecthq%2Ffastmcp | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

---

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) connects LLMs to tools and data. FastMCP is a full MCP application framework for servers, clients, and interactive apps. A server starts with ordinary Python:

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## Why FastMCP

Building an effective MCP application is harder than it looks. FastMCP handles all of it. Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically. Connect to a server with a URL, and transport negotiation, authentication, and protocol lifecycle are managed for you. You focus on your logic, and the MCP part just works: **with FastMCP, best practices are built in.**

**That's why FastMCP is the standard framework for working with MCP.** FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages.

FastMCP has three pillars:

<table>
<tr>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/servers/server">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/servers-card.png" alt="Servers" />
<br /><strong>Servers</strong>
</a>
<br />Expose tools, resources, and prompts to LLMs.
</td>
<td align="center" valign="top" width="33%">
<a href="https://gofastmcp.com/apps/overview">
<img src="https://raw.githubusercontent.com/PrefectHQ/fastmcp/main/docs/assets/images/apps-card.png" alt="Apps" />
<br /><strong>Apps</strong>
</a>
<br />Give your tools interactive UIs rendered directly in the conversation.
</
```

---

## 48. second_brain
- **Repository ID**: `REPO_SECOND_BRAIN`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/quant/second_brain](https://github.com/quant/second_brain)
- **Local Disk Path**: `/Users/rajondas/.air1/second_brain`
- **Description**: Repository second_brain located at /Users/rajondas/.air1/second_brain

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 49. sovereign-study-commons-india
- **Repository ID**: `REPO_SOVEREIGN_STUDY_COMMONS_INDIA`
- **Primary Domain**: `Knowledge Lake`
- **Remote URL**: [https://github.com/rajon369963-del/sovereign-study-commons-india](https://github.com/rajon369963-del/sovereign-study-commons-india)
- **Local Disk Path**: `https://github.com/rajon369963-del/sovereign-study-commons-india`
- **Description**: ⚡ Sovereign Study Commons India (सार्वजनिक अध्ययन महा-ज्ञानकोश) — Open-source zero-download Parquet knowledge lake for GATE EE, UPSC, NEET, & State AE/JE

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Knowledge Lake.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 50. civex-progressive-bridge
- **Repository ID**: `REPO_CIVEX_PROGRESSIVE_BRIDGE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rajon369963-del/civex-progressive-bridge](https://github.com/rajon369963-del/civex-progressive-bridge)
- **Local Disk Path**: `https://github.com/rajon369963-del/civex-progressive-bridge`
- **Description**: Quant module: civex-progressive-bridge

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 51. migl-sovereign-agent-suite
- **Repository ID**: `REPO_MIGL_SOVEREIGN_AGENT_SUITE`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rajon369963-del/migl-sovereign-agent-suite](https://github.com/rajon369963-del/migl-sovereign-agent-suite)
- **Local Disk Path**: `https://github.com/rajon369963-del/migl-sovereign-agent-suite`
- **Description**: Quant module: migl-sovereign-agent-suite

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 52. air1-migl-web
- **Repository ID**: `REPO_AIR1_MIGL_WEB`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rajon369963-del/air1-migl-web](https://github.com/rajon369963-del/air1-migl-web)
- **Local Disk Path**: `https://github.com/rajon369963-del/air1-migl-web`
- **Description**: Quant module: air1-migl-web

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 53. air1-reels
- **Repository ID**: `REPO_AIR1_REELS`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rajon369963-del/air1-reels](https://github.com/rajon369963-del/air1-reels)
- **Local Disk Path**: `https://github.com/rajon369963-del/air1-reels`
- **Description**: Quant module: air1-reels

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 54. air1-village-player
- **Repository ID**: `REPO_AIR1_VILLAGE_PLAYER`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rajon369963-del/air1-village-player](https://github.com/rajon369963-del/air1-village-player)
- **Local Disk Path**: `https://github.com/rajon369963-del/air1-village-player`
- **Description**: Quant module: air1-village-player

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 55. AIR1-CLOUD-FABRIC
- **Repository ID**: `REPO_AIR1_CLOUD_FABRIC`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rajon369963-del/AIR1-CLOUD-FABRIC](https://github.com/rajon369963-del/AIR1-CLOUD-FABRIC)
- **Local Disk Path**: `https://github.com/rajon369963-del/AIR1-CLOUD-FABRIC`
- **Description**: AIR1-CLOUD-FABRIC

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 56. migl-cloud-swarm
- **Repository ID**: `REPO_MIGL_CLOUD_SWARM`
- **Primary Domain**: `Engineering & Infrastructure`
- **Remote URL**: [https://github.com/rajon369963-del/migl-cloud-swarm](https://github.com/rajon369963-del/migl-cloud-swarm)
- **Local Disk Path**: `https://github.com/rajon369963-del/migl-cloud-swarm`
- **Description**: Quant module: migl-cloud-swarm

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Engineering & Infrastructure.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 57. CCXT
- **Repository ID**: `REPO_CURATED_CCXT`
- **Primary Domain**: `Multi-Exchange API`
- **Remote URL**: [https://github.com/ccxt/ccxt](https://github.com/ccxt/ccxt)
- **Local Disk Path**: `remote:https://github.com/ccxt/ccxt`
- **Description**: Unified crypto and multi-asset trading library with standardized REST and WebSocket API across 100+ venues.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Multi-Exchange API.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 58. OpenBB-Terminal
- **Repository ID**: `REPO_CURATED_OPENBB_TERMINAL`
- **Primary Domain**: `Institutional Terminal`
- **Remote URL**: [https://github.com/OpenBB-finance/OpenBBTerminal](https://github.com/OpenBB-finance/OpenBBTerminal)
- **Local Disk Path**: `remote:https://github.com/OpenBB-finance/OpenBBTerminal`
- **Description**: Modern, free, open-source investment research terminal providing macroeconomic, fundamental, and quantitative data feeds.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Institutional Terminal.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 59. yfinance
- **Repository ID**: `REPO_CURATED_YFINANCE`
- **Primary Domain**: `Market Data Extraction`
- **Remote URL**: [https://github.com/ranaroussi/yfinance](https://github.com/ranaroussi/yfinance)
- **Local Disk Path**: `remote:https://github.com/ranaroussi/yfinance`
- **Description**: High-speed market data scraper and API connector for global equities, ETFs, and historical OHLCV data.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for Market Data Extraction.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

## 60. QuickFIX
- **Repository ID**: `REPO_CURATED_QUICKFIX`
- **Primary Domain**: `FIX Protocol Engine`
- **Remote URL**: [https://github.com/quickfix/quickfix](https://github.com/quickfix/quickfix)
- **Local Disk Path**: `remote:https://github.com/quickfix/quickfix`
- **Description**: Fast, reliable C++ open-source Financial Information eXchange (FIX) protocol messaging engine.

### 📖 Quantitative Capabilities & Interface:
- Implements specialized mathematical routines for FIX Protocol Engine.
- Compatible with Python 3.14 / C++17 native bindings in Antigravity OS.

---

