# ⚡ [QUANT-SOURCE-123] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_123_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ai-trading-platform-v2 (`VAULT_IN-QUANT-026_Tanmay07__ai-trading-platform-v2`)
- **Full Name**: `IN-QUANT-026_Tanmay07__ai-trading-platform-v2`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# 🇮🇳 AI Trading Platform — Indian Stock Market

An AI-powered trading advisory platform for the Indian stock market (NSE).  
Provides technical analysis, portfolio management, ML-based predictions, and a continuous **AI Opportunity Discovery Engine** — all in **paper-trading / advisory mode**.

> ⚠️ **DISCLAIMER**: This is for **educational and research purposes only**, not financial advice.  
> The creators are not responsible for any financial decisions made using this platform.  
> Always consult a certified financial advisor before making investment decisions.

---

## 📦 Tech Stack

| Layer          | Technology                                      |
|----------------|--------------------------------------------------|
| **Backend**    | Python 3.11+, FastAPI, Uvicorn                   |
| **Database**   | S3 Storage Service, SQLite (via SQLAlchemy ORM)  |
| **Frontend**   | React (Vite), Lucide Icons                       |
| **Market Data**| yfinance (Yahoo Finance API)                      |
| **Analysis**   | pandas, NumPy, `ta` (Technical Analysis)          |
| **NLP**        | VADER Sentiment, FinBERT (HuggingFace)            |
| **ML**         | scikit-learn, XGBoost, LightGBM (Ensembles)      |

---

## 🚀 Key Features

### 1. Portfolio Tracking
Live P&L tracking, 1y/5d historical charting, sector exposure analysis, and automated market price syncing via Yahoo Finance.

### 2. Market Sentiment Analysis
Pulls live news articles from GNews and RSS feeds and runs them through a localized instance of **FinBERT** to score the market sentiment for individual stocks as Bearish, Neutral, or Bullish.

### 3. AI Opportunity Discovery Engine
A comprehensive background scanning engine that continually analyzes the NSE universe. It generates an **Opportunity Score (0-100)** by combining:
- **Fundamental Engine:** Scores based on ROE, Margins, Debt/Equity, and Growth.
- **Value Engine:** Identifies fundamentally strong stocks trading near their 52-week lows.
- **Momentum Engine:** Vectorized calculation of RSI, MACD crossovers, and Bollinger Bands.
- **Sentiment Engine:** Real-time news NLP processing.
- **AI Predictor:** Generates probability metrics for a 5%+ return over the next 30 days.
- **Sector Strength:** Tracks relative momentum across sectors.

### 4. Enterprise Data & AI Pipelines
- **Historical Data Lake (Phase D1):** High-performance storage and retrieval of OHLCV data using Parquet files and Redis caching.
- **Feature Store Platform (Phase D2):** A centralized, versioned repository of engineered Alpha Factors optimized for quantitative modeling.
- **Alpha Registry (Phase E2.1):** A research platform that tracks Information Coefficient (IC) and stability of engineered Alpha Factors over time.
- **Hierarchical Scenario Datasets (Phase E3.1):** Dynamically segments the NSE universe into specialized subsets (Bull Market, Sectors, High Volatility) to train expert models instead of one generic model.
- **Intelligent Bootstrap Manager (Phase E1.5):** A resumable orchestration layer that tracks initialization stages across the platform, including a Preflight Estimation Engine.

---

## 🚀 Quick Start (macOS)

### Prerequisites

```bash
# Install system dependencies (needed for LightGBM/XGBoost)
brew install libomp cmake
```

### Setup

```bash
# 1. Clone the repository
git clone <repo-url> ai-trading-platform
cd ai-trading-platform

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install Python dependencies
cd backend
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your API keys (GNEWS_API_KEY, etc.)

# 5. Start the backend server
uvicorn app.main:app --reload --port 8000

# 6. Start the frontend server (in a new terminal)
cd ../frontend
npm install
npm run dev
```

The frontend will be available at **http://localhost:5173**  
The API will be available at **http://127.0.0.1:8000**  
Interactive docs at **http://127.0.0.1:8000/docs**

---

## 📡 Key API Endpoints

### Discovery (`/discovery`)
| Method | Endpoint                  | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/scan`                   | Get the latest AI Discovery Scan   |
| GET    | `/top/{category}`         | Filter top opportunities by category (e.g. `high_growth`, `value`, `momentum`) |

### AI Platform & Orchestration
| Method | Endpoint                  | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/api/bootstrap/preflight`| Run Bootstrap Preflight checks     |
| GET    | `/api/scenarios/`         | View Scenario Generation metrics   |
| GET    | `/api/datasets/`          | View ML Dataset Builder metrics    |
| GET    | `/api/alpha/`             | Access the Alpha Research Registry |

### Portfolio (`/portfolio`)
| Method | Endpoint                  | Description                        |
|--------|---------------------------|------------------------------------|
| GET    | `/`                       | List all portfolio holdings        |
| POST   | `/`                       | Add a new holding                  |
| DELETE | `/{symbol}`               | Remove a holding                   |

---

## 🗓️ Roadmap

- [x] Phase 1-4: Core Market Data & Sentiment Discovery
- [x] Phase D1-D2: Historical Data Lake & Feature Store
- [x] Phase E2-E3: Alpha Registry & Scenario Datasets
- [x] Phase E1.5: Production Bootstrap Manager
- [ ] Phase 5: Live Trading API integrations (Broker APIs)

### Core Implementation Code & Architecture
#### File: `backend/app/discovery/__init__.py`
```python

```

#### File: `backend/app/recommendations/__init__.py`
```python

```

#### File: `backend/app/research_lab/__init__.py`
```python

```

#### File: `backend/app/research_lab/diagnostics/__init__.py`
```python

```

#### File: `backend/app/research_lab/analytics/__init__.py`
```python

```

#### File: `backend/app/research_lab/reports/__init__.py`
```python

```


==================================================


## [2/3] Repository: Bridge (`VAULT_IN-QUANT-033_indicoderlabs__Bridge`)
- **Full Name**: `IN-QUANT-033_indicoderlabs__Bridge`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# OpenAlgo - Open Source Algorithmic Trading Platform

<div align="center">

[![PyPI Downloads](https://static.pepy.tech/badge/openalgo)](https://pepy.tech/projects/openalgo)
[![PyPI Downloads](https://static.pepy.tech/badge/openalgo/month)](https://pepy.tech/projects/openalgo)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/openalgoHQ)](https://twitter.com/openalgoHQ)
[![YouTube: Subscribe](https://img.shields.io/badge/YouTube-Subscribe-FF0000)](https://www.youtube.com/@openalgo)
[![Discord](https://img.shields.io/discord/1219847221055455263)](https://discord.com/invite/UPh7QPsNhP)

</div>

## What is OpenAlgo?

OpenAlgo is a free, open source, self-hosted **trading platform**, not just a broker bridge. Built on Python Flask + React 19, it gives traders a full-stack environment to **design, host, and execute strategies** through **36 broker plugins**: 35 securities integrations and Delta Exchange for crypto derivatives. Whether you write Python, prefer drag-and-drop, or trade options, OpenAlgo provides a common interface without tying strategy code to one adapter.

OpenAlgo is no longer just "an API layer in front of your broker." Today it combines four trading surfaces in one self-hosted instance, sharing the active broker session, market-data infrastructure, and six operational data stores across the journey from idea to testing and live execution.

## Five Ways to Trade with OpenAlgo

| Surface | Route | Who it's for |
| --- | --- | --- |
| **Unified Broker API** | `/api/v1/` | External platforms: TradingView, Amibroker, ChartInk, Excel, Google Sheets, Python, Java, Go, .NET, Node.js, MetaTrader, GoCharting, N8N. One contract across 36 plugins, with optional operations varying by adapter. |
| **Python Strategy Host** | `/python` | Traders who code: paste any Python script into the in-browser CodeMirror editor, schedule it on IST start/stop times, run multiple strategies in parallel with process isolation, watch real-time logs. No external server, no Docker, no cron. |
| **Flow: No-Code Strategy Builder** | `/flow` | Traders who don't code: drag-and-drop nodes for market data, indicators, conditions, order execution, and notifications. Webhook triggers for TradingView and external signals built in. JSON import/export for sharing strategies. |
| **AI Agent** | `/agent` | Traders who would rather ask: a chat that reads your own market data through OpenAlgo's services, draws charts and payoff diagrams, computes indicators, marks up the `/trading` chart from a right-side panel, and can place orders only with your explicit approval on every single one. Bring your own model from any LiteLLM provider, or a ChatGPT Plus or Pro subscription, or run it locally against Ollama. |
| **Options Trading Suite** | `/tools` | Options traders: twelve built-in analytical tools (Strategy Builder with payoff diagrams & live Greeks, Option Chain, IV Smile, Max Pain, Vol Surface, GEX dashboard, OI Tracker, OI Profile, Straddle Chart, Straddle PnL simulator, Option Greeks history). Each one streams from your connected broker. |

Order workflows from the REST API, hosted strategies, and Flow can use Analyzer Mode before live execution. Analytics pages, dashboards, PnL tracking, latency monitoring, notifications, and MCP reuse the same application services where their specific capabilities apply.

## Video Tutorial

[![What is OpenAlgo](https://img.youtube.com/vi/S5myMo9WUdQ/0.jpg)](https://www.youtube.com/watch?v=S5myMo9WUdQ)

## Quick Links

- **Documentation**: [docs.openalgo.in](https://docs.openalgo.in)
- **Installation Guide**: [Getting Started](https://docs.openalgo.in/installation-guidelines/getting-started)
- **Upgrade Guide**: [Upgrade Instructions](https://docs.openalgo.in/installation-guidelines/getting-started/upgrade)
- **Why OpenAlgo**: [Why Build with OpenAlgo](https://docs.openalgo.in/why-to-build-with-openalgo)


## Python Compatibility

**Requires Python 3.12 or newer.**

## Supported Brokers (36 plugins)

<details>
<summary>View All Supported Brokers</summary>

- 5paisa (Standard + XTS)
- AliceBlue
- AngelOne
- Arrow
- Compositedge
- Definedge
- Delta Exchange
- Dhan (Live + Sandbox)
- Firstock
- Flattrade
- Fyers
- Groww
- HDFC Securities
- HDFC Sky
- IBulls
- IIFL
- Iiflcapital
- Indmoney
- JainamXTS
- Kotak Neo
- Motilal Oswal
- Mstock
- Nubra
- Paytm Money
- Pocketful
- RMoney
- Samco
- Shoonya (Finvasia)
- Tradejini
- TradeSmart
- Upstox
- Wisdom Capital
- Zebu
- Zerodha

</details>

Plugins share OpenAlgo's normalized API shapes. Exchange coverage, authentication, market-data entitlement, GTT support, and other optional capabilities still vary by adapter and broker account.

## Core Features

### Unified REST API Layer (`/api/v1/`)
A maintained contract with 57 REST method/path pairs under `/api/v1`:
- **Order Management**: Place, modify, cancel orders, basket orders, smart orders with position sizing
- **Portfolio**: Get positions, holdings, order book, trade book, funds
- **Market Data**: Real-time quotes, historical data, market depth (Level 5), symbol search
- **Advanced**: Option Greeks calculator, margin calculator, synthetic futures, auto-split orders

### Real-Time WebSocket Streaming
- Unified WebSocket proxy server (port 8765 by default)
- Common WebSocket implementation using ZMQ for normalized data across brokers
- Subscribe to LTP, Quote, or Market Depth for any symbol
- ZeroMQ-based message bus for high-performance data distribution
- Automatic reconnection and failover handling

### Flow Visual Strategy Builder (`/flow`)
Build trading strategies visually without writing code:
- **Node-based editor** powered by xyflow/React Flow
- **Pre-built nodes**: Market data, indicators, conditions, order execution, notifications
- **Real-time execution** with live market data
- **Webhook triggers** for TradingView and external signals
- **Condition nodes** with `true/false` and `yes/no` edge handles, `{{var}}` interpolation with list indexing
- **JSON import/export** for sharing strategies between traders
- **Visual debugging** with execution flow highlighting

### Options & Strategy Analytics Tools (`/tools`)
A suite of twelve built-in analytical tools for options trading and market analysis. The pages use the active broker connection; broker market-data entitlements and exchange coverage still apply. Accessible from the **Tools** page in the sidebar:

| Tool | Route | What it does |
|------|-------|--------------|
| **Strategy Builder** | `/strategybuilder` | Build multi-leg option strategies with live Greeks, payoff diagrams, what-if simulators, Strategy Chart, Multi Strike OI tabs, and basket order execution |
| **Strategy Portfolio** | `/strategybuilder/portfolio` | Saved strategies across MyTrades and Simulation watchlists |
| **Option Chain** | `/optionchain` | Real-time option chain with live Greeks, OI data, and quick order placement |
| **Option Greeks** | `/ivchart` | Historical IV, Delta, Theta, Vega, and Gamma charts for ATM options |
| **OI Tracker** | `/oitracker` | Open Interest analysis with CE/PE OI bars, PCR overlay, and ATM strike marker |
| **Max Pain** | `/maxpain` | Max Pain strike calculation with visual pain distribution across strikes |
| **Straddle Chart** | `/straddle` | Dynamic ATM Straddle chart with rolling strike, Spot, and Synthetic Futures overlay |
| **Straddle PnL** | `/straddlepnl` | Simulated intraday ATM straddle P&L with automated N-point adjustments and trade log |
| **Vol Surface** | `/volsurface` | 3D Implied Volatility surface across strikes and expiries using live option chain data |
| **GEX Dashboard** | `/gex` | Gamma Exposure analysis with OI Walls, Net GEX per strike, and top gamma strikes |
| **IV Smile** | `/ivsmile` | Implied Volatility smile with Call/Put IV curves, ATM IV, and skew analysis |
| **OI Profile** | `/oiprofile` | Futures candlestick with OI butterfly and daily OI change across strikes |

Tools use the active broker's REST and WebSocket capabilities. Data availability and supported exchanges vary by plugin and account entitlement.

### API Analyzer Mode
Complete testing environment with ₹1 Crore sandbox capital:
- Test strategies with real market data without risking money
- Pre-deployment testing for strategy validation
- Supports the core MARKET, LIMIT, SL, and SL-M price types
- Realistic margin system with leverage
- Configurable sandbox square-off schedules
- Separate database for complete isolation

[API Analyzer Documentation](https://docs.openalgo.in/new-features/api-analyzer)

### Action Center
Order approval workflow for manual control:
- **Auto Mode**: Immediate order execution (for personal trading)
- **Semi-Auto Mode**: Manual approval required before broker execution
- Complete audit trail with IST timestamps
- Approve individual orders or bulk approve all

[Action Center Documentation](https://docs.openalgo.in/new-features/action-center)

### Python Strategy Host (`/python`)
Host and run your Python strategies directly inside OpenAlgo, with no separate VM, no cron, no Docker:
- Built-in code editor powered by **CodeMirror** with Python syntax highlighting and themes
- Run multiple strategies in parallel with **full process isolation**
- Automated **IST-based scheduling** with start/stop times and per-day-of-week control
- Secure environment variable management with Fernet encryption
- Real-time logs streamed to the browser; state persists across restarts
- Built-in `Python Strategy Guide` page walks first-time users from an empty editor to a scheduled, running strategy

### ChartInk Integration
Direct webhook integration for scanner alerts:
- Supports BUY, SELL, SHORT, COVER actions
- Intraday with auto square-off and positional strategies
- Bulk symbol configuration via CSV
- Real-time strategy monitoring

### AI Agent (`/agent`)
A built-in LLM agent, on the full page and as a right-side panel on the `/trading` chart:
- Reads quotes, depth, history, option chains and Greeks through OpenAlgo's own services, never a third-party data feed
- Draws candles with the charting library, option analytics with Plotly, and marks levels, trendlines and zones onto your chart
- Computes 127 indicators with the Rust-backed `openalgo.ta`, and generates Python strategies using the OpenAlgo SDK
- **Every order pauses for your approval**, showing the exact arguments before anything is sent, with the risk limits applied after you approve
- Any provider LiteLLM supports, a ChatGPT Plus or Pro subscription over OAuth, or a local model through Ollama
- Keys are encrypted in your own database and never written to a configuration file

### AI-Powered Trading (MCP Server)
Connect AI assistants for natural language trading:
- Compatible with Claude Desktop, Cursor, Windsurf, ChatGPT
- Execute trades using natural language commands
- Full trading capabilities: orders, positions, market data
- Local and secure integration with your OpenAlgo instance

### Telegram Bot Integration
Real-time notifications and command execution:
- Automatic order and trade alerts delivered to Telegram
- Get orderbook, positions, holdings, funds on demand
- Generate intraday and daily charts
- Interactive button-based menu
- Receive strategy alerts directly to Telegram
- Secure API key encryption

### Advanced Monitoring Tools
**Latency Monitor**: Track order execution performance and round-trip times across brokers

**Traffic Monitor**: API usage analytics, error tracking, and endpoint statistics

**PnL Tracker**: Real-time profit/loss with interactive charts powered by TradingView Lightweight Charts

[PnL Tracker Documentation](https://docs.openalgo.in/new-features/pnl-tracker)

[Traffic & Latency Monitor Documentation](https://docs.openalgo.in/new-features/traffic-latency-monitor)

### Enterprise-Grade Security
**Password Security**: Argon2 hashing (Password Hashing Competition winner)

**Token Encryption**: Fernet symmetric encryption with PBKDF2 key derivation

**Two-Factor Authentication**: TOTP support with authenticator apps

**Rate Limiting**: Configurable limits for login, API, orders, webhooks

**Manual IP Ban System**: Monitor and ban suspicious IPs via `/security` dashboard

**Browser Protection**: CSP headers, CORS rules, CSRF protection, secure headers, secure sessions

**SQL Injection Prevention**: SQLAlchemy ORM with parameterized queries

**Privacy First**: Zero data collection policy - your data stays on your server

### Modern React Frontend
- **React 19** with TypeScript for type-safe, maintainable code
- **shadcn/ui** components with Tailwind CSS 4.0 for beautiful, accessible UI
- **TanStack Query** for efficient server state management and caching
- **Zustand** for lightweight client state management
- **Real-time updates** via Socket.IO (orders, trades, positions, logs)
- **CodeMirror** for Python and JSON editing with syntax highlighting and themes
- **xyflow/React Flow** for visual Flow strategy builder
- **TradingView Lightweight Charts** for P&L and market data visualization
- Light and Dark themes with 8 accent colors
- Mobile-friendly responsive design

## Supported Platforms

Connect your algo strategies and run from any platform:

- **Amibroker** - Direct integration with AFL scripts
- **TradingView** - Webhook alerts for Pine Script strategies
- **GoCharting** - Webhook integration
- **N8N** - Workflow automation
- **Python** - Official SDK with 100+ technical indicators
- **GO** - REST API integration
- **Node.js** - JavaScript/TypeScript library
- **ChartInk** - Scanner webhook integration
- **MetaTrader** - Compatible with MT4/MT5
- **Excel** - REST API + upcoming Add-in
- **Google Sheets** - REST API integration

Receive your strategy alerts directly to **Telegram** for all platforms.

## Technology Stack

### Backend
- **Flask 3.0** - Python web framework
- **SQLAlchemy 2.0** - Database ORM
- **Flask-SocketIO** - Real-time WebSocket communication
- **ZeroMQ** - High-performance message bus
- **Argon2-CFFI** - Password hashing
- **Cryptography** - Fernet encryption for tokens
- **Agno** - Agentic framework for the `/agent` reasoning loop and tool calling
- **LiteLLM** - LLM-agnostic provider layer the agent calls every model through

### Frontend
- **React 19** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite 8** - Fast build tool powered by Rolldown
- **Tailwind CSS 4** - Utility-first CSS framework
- **shadcn/ui** - Component library built on Radix UI
- **TanStack Query** - Server state management
- **Zustand** - Client state management

### Data Visualization & Editors
- **TradingView Lightweight Charts** - Financial charts
- **CodeMirror** - Code editor for strategies
- **xyflow/React Flow** - Visual Flow builder
- **Lucide React** - Icon library

### Testing & Quality
- **Vitest** - Unit testing
- **Playwright** - E2E testing
- **Biome** - Linting and formatting
- **axe-core** - Accessibility testing

### Databases
- **SQLite** - 5 databases (main, logs, latency, health, sandbox)
- **DuckDB** - 1 historical market-data store (Historify)

## Official SDKs

OpenAlgo provides officially supported client libraries for application development and system-level integrations:

| Language / Platform | Repository |
|---------------------|------------|
| Python | [openalgo-python-library](https://github.com/marketcalls/openalgo-python-library) |
| Node.js | [openalgo-node](https://github.com/marketcalls/openalgo-node) |
| Java | [openalgo-java](https://github.com/marketcalls/openalgo-java) |
| Rust | [openalgo-rust](https://github.com/marketcalls/openalgo-rust) |
| .NET / C# | [openalgo.NET](https://github.com/marketcalls/openalgo.NET) |
| Go | [openalgo-go](https://github.com/marketcalls/openalgo-go) |

## OpenAlgo FOSS Ecosystem

OpenAlgo is part of a larger open-source trading ecosystem:

- **OpenAlgo Core**: This repository (Python Flask + React)
- **Historify**: Stock market data management platform
- **Official SDKs**: Python, Node.js, Java, Rust, .NET, Go (see above)
- **Excel Add-in**: Direct Excel integration
- **MCP Server**: AI agents integration
- **Chrome Plugin**: Browser-based tools
- **Fast Scalper**: High-performance trading (Rust + Tauri)
- **Web Portal**: Modern UI (NextJS + ShadcnUI)
- **Documentation**: Comprehensive guides on [Gitbook](https://docs.openalgo.in/mini-foss-universe)

## Installation

### Minimum Requirements
- **RAM**: 2GB (or 0.5GB + 2GB swap)
- **Disk**: 1GB
- **CPU**: 1 vCPU
- **Python**: 3.12 or newer
- **Node.js**: 20.20+, 22.22+, or 24.13+ (for frontend development)

### Quick Start with UV

OpenAlgo uses the modern `uv` package manager for faster, more reliable installations:

```bash
# Clone the repository
git clone --filter=blob:none https://github.com/marketcalls/openalgo.git
cd openalgo

# Install UV package manager
pip install uv

# Configure environment
cp .sample.env .env
# Edit .env with your broker API credentials as per documentation

# Run the application using UV
uv run app.py
```

The application will be available at `http://127.0.0.1:5000`

For detailed installation instructions, deployment options (Docker, AWS, etc.), and configuration guides, visit [docs.openalgo.in/installation-guidelines/getting-started](https://docs.openalgo.in/installation-guidelines/getting-started)

## API Documentation

Complete API reference and examples:
- **API Documentation**: [docs.openalgo.in/api-documentation/v1](https://docs.openalgo.in/api-documentation/v1)
- **Symbol Format**: [docs.openalgo.in/symbol-format](https://docs.openalgo.in/symbol-format)

## Key Benefits

- **Guided Installation**: UV and production install scripts with explicit broker configuration
- **Single API, Multiple Brokers**: Switch brokers without code changes
- **No Data Collection**: Complete privacy - your data stays on your server
- **Visual Strategy Builder**: Create strategies with drag-and-drop Flow editor
- **Host Python Strategies**: Run strategies directly without external servers
- **Smart Order Execution**: Intelligent routing for complex strategies
- **Order Splitting**: Automatically split large orders into smaller chunks
- **Real-Time Analytics**: PnL tracking, latency monitoring, traffic analysis
- **Strategy Templates**: Rapid prototyping with pre-built templates
- **Plugin Architecture**: Extensible design for custom integrations
- **Active Community**: Discord support, virtual meetups, open roadmap

## Documentation

Comprehensive documentation is available at [docs.openalgo.in](https://docs.openalgo.in):
- API Reference with examples
- Broker-specific guides
- Security best practices
- Deployment tutorials
- Strategy development guides
- Troubleshooting and FAQs

## Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes using [Conventional Commits](CONTRIBUTING.md#commit-messages), for example:
   ```bash
   git commit -m "feat: add amazing feature"
   ```
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Community & Support

- **Discord**: [Join our community](https://www.openalgo.in/discord)
- **Twitter/X**: [@openalgoHQ](https://twitter.com/openalgoHQ)
- **YouTube**: [@openalgo](https://www.youtube.com/@openalgo)
- **GitHub Issues**: [Report bugs or request features](https://github.com/marketcalls/openalgo/issues)

## License

OpenAlgo is released under the **AGPL V3.0 License**. See [License.md](License.md) for details.

## Credits & Acknowledgments

OpenAlgo is built upon the shoulders of giants. We extend our gratitude to all the open-source projects that make this platform possible.

### Core Framework
- **[Flask](https://flask.palletsprojects.com)** - BSD License - Python web microframework
- **[React](https://react.dev)** - MIT License - UI library for building user interfaces
- **[SQLAlchemy](https://www.sqlalchemy.org)** - MIT License - Python SQL toolkit and ORM

### AI & Agent Frameworks
The AI Agent at `/agent` is deliberately LLM-agnostic. The agent loop and the provider layer are separate pieces, so moving between model vendors, or to a local model, is a configuration change rather than a code change. Both of these projects are what make that possible.

- **[Agno](https://github.com/agno-agi/agno)** - Apache 2.0 - Agentic framework behind the `/agent` reasoning loop, tool calling, session persistence and image attachments
- **[LiteLLM](https://litellm.ai)** - MIT License - Unified model layer giving one interface across every supported provider, plus the model catalogue and per-model metadata the agent's provider picker is built from

### UI Components & Styling
- **[shadcn/ui](https://ui.shadcn.com)** - MIT License - Beautifully designed components built with Radix UI and Tailwind CSS
- **[Radix UI](https://www.radix-ui.com)** - MIT License - Unstyled, accessible UI components
- **[Tailwind CSS](https://tailwindcss.com)** - MIT License - Utility-first CSS framework
- **[Lucide](https://lucide.dev)** - ISC License - Beautiful & consistent icon library

### Data Visualization
- **[TradingView Lightweight Charts](https://github.com/tradingview/lightweight-charts)** - Apache 2.0 - Financial charting library for market data and P&L visualization
- **[Plotly](https://plotly.com/javascript/)** - MIT License - Interactive charting library for options analytics and visualization
- **[xyflow/React Flow](https://reactflow.dev)** - MIT License - Highly customizable library for building node-based visual strategy editors

### Code Editors
- **[CodeMirror](https://codemirror.net)** - MIT License - Versatile code editor for Python and JSON with syntax highlighting
- **[@uiw/react-codemirror](https://uiwjs.github.io/react-codemirror)** - MIT License - CodeMirror React wrapper with themes

### State Management & Data Fetching
- **[TanStack Query](https://tanstack.com/query)** - MIT License - Powerful asynchronous state management
- **[Zustand](https://zustand-demo.pmnd.rs)** - MIT License - Lightweight state management
- **[Axios](https://axios-http.com)** - MIT License - Promise-based HTTP client

### Real-Time Communication
- **[Socket.IO](https://socket.io)** - MIT License - Real-time bidirectional event-based communication
- **[ZeroMQ](https://zeromq.org)** - LGPL License - High-performance asynchronous messaging

### Security
- **[Argon2-CFFI](https://argon2-cffi.readthedocs.io)** - MIT License - Argon2 password hashing (PHC winner)
- **[Cryptography](https://cryptography.io)** - BSD/Apache License - Cryptographic recipes and primitives

### Build & Development Tools
- **[Vite](https://vitejs.dev)** - MIT License - Fast frontend build tool
- **[TypeScript](https://www.typescriptlang.org)** - Apache 2.0 - JavaScript with syntax for types
- **[Biome](https://biomejs.dev)** - MIT License - Fast formatter and linter
- **[Vitest](https://vitest.dev)** - MIT License - Blazing fast unit testing
- **[Playwright](https://playwright.dev)** - Apache 2.0 - End-to-end testing framework

### Additional Libraries
- **[React Router](https://reactrouter.com)** - MIT License - Declarative routing for React
- **[Sonner](https://sonner.emilkowal.ski)** - MIT License - Toast notifications
- **[cmdk](https://cmdk.paco.me)** - MIT License - Command palette component
- **[next-themes](https://github.com/pacocoursey/next-themes)** - MIT License - Theme switching
- **[react-resizable-panels](https://github.com/bvaughn/react-resizable-panels)** - MIT License - Resizable panel layouts
- **[html2canvas-pro](https://html2canvas.hertzen.com)** - MIT License - Screenshot generation

## Repo Activity

![Alt](https://repobeats.axiom.co/api/embed/0b6b18194a3089cb47ab8ae588caabb14aa9972b.svg "Repobeats analytics image")

## Disclaimer

**This software is for educational purposes only. Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.**

Always test your strategies in Analyzer Mode before deploying with real money. Past performance does not guarantee future results. Trading involves substantial risk of loss.

---

Built with by traders, for traders. Making algorithmic trading accessible to everyone.

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `blueprints/__init__.py`
```python

```

#### File: `broker/__init__.py`
```python

```

#### File: `broker/hdfcsky/__init__.py`
```python

```

#### File: `broker/hdfcsky/mapping/__init__.py`
```python

```

#### File: `broker/hdfcsky/database/__init__.py`
```python

```


==================================================


## [3/3] Repository: fenix (`VAULT_IN-QUANT-034_TheHardeep__fenix`)
- **Full Name**: `IN-QUANT-034_TheHardeep__fenix`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/fenix-logo.png" alt="Fenix" width="180">
</p>

<h1 align="center">Fenix</h1>

<p align="center">
  <b>Change one word. Trade any broker.</b><br>
  One unified Python API across <b>15 Indian brokers</b> — authentication, instrument tokens,
  orders, positions, and account data, all returned in one consistent shape.
</p>

<p align="center">
  <a href="https://github.com/TheHardeep/fenix/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/badge/License-GPLv3-blue?color=%234ec820"></a>
  <a href="https://pypi.org/project/fenix/"><img alt="PyPI" src="https://img.shields.io/pypi/v/fenix"></a>
  <a href="https://pepy.tech/projects/fenix"><img src="https://static.pepy.tech/personalized-badge/fenix?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=RED&left_text=downloads" alt="PyPI Downloads"></a>
  <img alt="Python" src="https://img.shields.io/pypi/pyversions/fenix">
  <a href="https://fenix.hardeep.tech"><img alt="Docs" src="https://img.shields.io/badge/docs-fenix.hardeep.tech-orange"></a>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#quickstart">Quickstart</a> ·
  <a href="#features">Features</a> ·
  <a href="#supported-brokers">Brokers</a> ·
  <a href="#unified-vocabulary">Constants</a> ·
  <a href="#paper-trading">Paper Mode</a> ·
  <a href="https://fenix.hardeep.tech">Documentation</a>
</p>

---

Every Indian broker ships its own REST API with its own URLs, field names, constants for order
side and product type, error envelope, and rate limits. Writing a strategy against one broker
means re-learning all of that for the next. **Fenix is an adapter library**: each broker is a
class that implements the same methods and returns the same dictionaries — a single unified
interface purpose-built for the Indian markets (NSE, BSE, NFO, BFO, MCX, CDS).

```python
# swap one word — the rest never changes
from fenix import Zerodha
from fenix import Side, Product

broker = Zerodha()
broker.authenticate(params=creds)
broker.market_order(token_dict=contract, quantity=1, side=Side.BUY, product=Product.MIS, unique_id="entry-1")
```

It is built for **coders, quant developers, technically-skilled traders, and data scientists**
building algorithmic trading systems on top of one stable API.

## Why Fenix

- **Learn it once, ship everywhere.** The same method names, parameters, and return shapes work
  across every adapter. Porting a strategy to a new broker is a one-line change — not a rewrite.
- **One vocabulary, not fifteen.** Your code speaks in Fenix constants — `Side.BUY`,
  `Product.MIS`, `OrderType.SLM` — and each adapter translates to its broker's dialect, with
  validation.
- **Backtest with paper mode.** Flip one flag and the same strategy runs against a built-in
  matching engine — realistic fills, positions, and PnL, with no credentials and zero live calls.
- **Safe by default.** Token-bucket rate limiting per endpoint, structured errors with
  HTTP-status mapping, and automatic redaction of secrets from every log line.

## Install

Fenix 2.0 requires **Python 3.10 or newer** and runs on Windows, macOS, and Linux.

```shell
pip install fenix
```

To install a specific release:

```shell
pip install fenix==2.0.2
```

Verify the installation and inspect the broker registry:

```python
import fenix

print(fenix.__version__)   # 2.0.2
print(fenix.brokers)       # ['AliceBlue', 'AngelOne', 'AnandRathi', ...]
```

## Quickstart

Instantiate a broker, authenticate, download instrument tokens, place an order, and read it
back — all through the unified API. The same code runs against any broker.

```python
from fenix import Zerodha, Side, Validity

# 1 · Instantiate
broker = Zerodha()

# 2 · Authenticate — each broker declares the credentials it needs in `tokenParams`
creds = {
    "user_id":    "YOUR_USER_ID",
    "password":   "YOUR_PASSWORD",
    "totpstr":    "YOUR_TOTP_SECRET",   # the TOTP *seed*, not a 6-digit code
    "api_key":    "YOUR_API_KEY",
    "api_secret": "YOUR_API_SECRET",
}
broker.authenticate(params=creds)

# 3 · Download instrument tokens (reshaped into a standardized lookup)
fno, _ = broker.load_fno_tokens()
contract = fno["Options"]["NFO"]["NIFTY"][0]

# 4 · Place an order — returns a unified order record (same keys for every broker)
order = broker.limit_order(
    token_dict=contract,
    side=Side.BUY,
    price=152.0,
    quantity=75,
    unique_id="entry-1",
)

# 5 · Read it back, then modify or cancel
detail = broker.fetch_order(order["id"])
broker.modify_order(order_id=order["id"], price=151.5, quantity=75)
broker.cancel_order(order_id=order["id"])

# 6 · Inspect positions and account
positions = broker.fetch_net_positions()
holdings  = broker.fetch_holdings()
margins   = broker.fetch_margin_limits()   # unified RMS record
profile   = broker.fetch_profile()
```

> See the [Quickstart guide](https://fenix.hardeep.tech) for the full walkthrough, including
> reusing an authenticated session across runs.

### Order & account methods

| Order entry | Account & order reads |
|-------------|-----------------------|
| `place_order`, `modify_order`, `cancel_order` | `fetch_orderbook`, `fetch_tradebook` |
| `market_order`, `limit_order`, `sl_order`, `slm_order` | `fetch_order`, `fetch_order_history` |
| `market_buy_order`, `market_sell_order` | `fetch_net_positions`, `fetch_day_positions` |
| `limit_buy_order`, `limit_sell_order` | `fetch_holdings`, `fetch_margin_limits` |
| `sl_buy_order`, `slm_sell_order`, … | `fetch_profile` |

## Features

Fenix 2.0 is a ground-up refactor of the broker layer. Highlights:

- 🔁 **Unified, one-line broker swap.** Identical method names, parameters, and return shapes
  across all 15 adapters — port a strategy by changing a single class name.
- 🧱 **One shared base class.** Every adapter subclasses `fenix.base.broker.Broker`, which owns
  the HTTP session, request wrapper, URL building, constant translation, and error mapping. New
  brokers stay thin and consistent.
- 📄 **Built-in paper-mode engine.** An in-process matching engine simulates fills, positions,
  and PnL with no credentials and zero live calls — flip `paper_mode` and the same code runs.
- 🗣️ **One vocabulary.** Fenix constants (`Side`, `Product`, `OrderType`, `Validity`, `Variety`,
  `Status`) are translated per broker with validation — see [Constants](#unified-vocabulary).
- 🚦 **Per-endpoint rate limiting.** Token-bucket throttling defined in each adapter's
  `rateLimits`; requests self-throttle before hitting the broker.
- 🔐 **Secret redaction.** Passwords, tokens, API keys, authorization headers, and TOTP values
  are automatically scrubbed from every log line.
- 🧾 **Structured errors.** Broker error envelopes are mapped to typed Fenix exceptions with
  HTTP-status context.
- 🩺 **Request/response diagnostics.** Every broker keeps the latest HTTP snapshots
  (`last_request_*`, `last_response_*`) — plus paper-mode equivalents.
- ⌨️ **Typed.** Ships a PEP 561 `py.typed` marker so downstream type checkers pick up Fenix's
  annotations.

## Supported Brokers

Fenix 2.0 exposes **15 broker adapters**. Each has its own
[reference page](https://fenix.hardeep.tech) documenting every method it supports.

The **Class** name is the public identifier — it is exactly what `fenix.brokers` lists and what
`broker.describe()["id"]` returns.

| | Broker | Class |
|---|--------|-------|
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/aliceblue.svg" alt="AliceBlue" height="22"> | AliceBlue | `AliceBlue` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/angelone.svg" alt="Angel One" height="22"> | Angel One | `AngelOne` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/anandrathi.jpeg" alt="Anand Rathi" height="22"> | Anand Rathi | `AnandRathi` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/dhan.svg" alt="Dhan" height="22"> | Dhan | `Dhan` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/finvasia.svg" alt="Finvasia" height="22"> | Finvasia / Shoonya | `Finvasia` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/fivepaisa.svg" alt="5paisa" height="22"> | 5paisa | `FivePaisa` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/fyers.svg" alt="Fyers" height="22"> | Fyers | `Fyers` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/groww.svg" alt="Groww" height="22"> | Groww | `Groww` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/iifl.svg" alt="IIFL" height="22"> | IIFL | `Iifl` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/kotakneo.svg" alt="Kotak Neo" height="22"> | Kotak Neo | `KotakNeo` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/mastertrust.svg" alt="Master Trust" height="22"> | Master Trust | `MasterTrust` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/motilaloswal.jpeg" alt="Motilal Oswal" height="22"> | Motilal Oswal | `MotilalOswal` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/symphony.svg" alt="Symphony" height="22"> | Symphony | `Symphony` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/upstox.svg" alt="Upstox" height="22"> | Upstox | `Upstox` |
| <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/brokers/zerodha.svg" alt="Zerodha" height="22"> | Zerodha | `Zerodha` |

```python
import fenix
print(fenix.brokers)   # always reflects exactly what your installed version supports
```

> The deprecated v1 modules `choice`, `kotak`, `kunjee`, and `vpc` were removed in v2.0.

## Unified Vocabulary

Your strategy speaks Fenix constants; each adapter translates them to its broker's dialect and
validates them. The constant classes are top-level exports (`from fenix import Side, Product, …`).

| Constant | Common values |
|----------|---------------|
| `Side` | `BUY`, `SELL` |
| `OrderType` | `MARKET`, `LIMIT`, `SL`, `SLM` |
| `Product` | `MIS`, `NRML`, `CNC`, `MARGIN`, `MTF`, `BO`, `CO` |
| `Validity` | `DAY`, `IOC`, `GTD`, `GTC`, `FOK`, `TTL` |
| `Variety` | `REGULAR`, `STOPLOSS`, `AMO`, `BO`, `CO`, `ICEBERG`, `AUCTION` |
| `Status` | `PENDING`, `OPEN`, `PARTIALLY_FILLED`, `FILLED`, `REJECTED`, `CANCELLED` |
| `ExchangeCode` | `NSE`, `NFO`, `BSE`, `BFO`, `MCX`, `CDS`, … |
| `Root` | `NIFTY`, `BANKNIFTY`, `FINNIFTY`, `SENSEX`, `CRUDEOIL`, … |
| `Option` | `CE`, `PE` |

Returned records also use a fixed key set (`Order`, `Position`, `Profile`, `RMS`), so the same
parsing code works for every broker. Full reference at **[fenix.hardeep.tech](https://fenix.hardeep.tech)**.

## Paper Trading

Paper mode routes supported order entry and account reads through Fenix's in-process matching
engine instead of live broker endpoints — no credentials, zero live calls. Flip one flag and the
exact same code runs against the simulator.

```python
from fenix import AliceBlue, Side, UniqueID

broker = AliceBlue({"paper_mode": True})
broker.authenticate()                      # no-op in paper mode

token = {"Token": 12345, "Symbol": "TESTSTOCK", "Exchange": "NSE"}

order = broker.market_order(
    token_dict=token, quantity=1, side=Side.BUY, unique_id=UniqueID.MARKET_ORDER,
)

broker.on_tick(token=12345, ltp=2500.0)    # feed prices to drive fills

print(broker.fetch_orderbook())
print(broker.fetch_positions())
```

Paper mode supports order books, trade books, order history, positions, holdings, margin limits,
profile data, stop-order validation, and square-off validation.

## How it fits together

Every adapter — `Zerodha`, `AngelOne`, `Fyers`, … — subclasses `fenix.base.broker.Broker`. The
base class owns everything identical across brokers (HTTP session, throttling, the `fetch()`
request wrapper, URL building, constant translation, logging/redaction, error mapping, and the
embedded paper engine), while each subclass supplies only what is broker-specific.

```
  Your strategy            Fenix · Unified API           Brokers
┌────────────────┐          ┌──────────────────────────┐          ┌──────────────────────────┐
│                │          │  authenticate · login    │          │  Zerodha · Angel One     │
│  one codebase  │  ──────▶ │  orders · positions      │  ──────▶ │  Fyers · Upstox · Dhan   │
│                │   call   │  account · paper mode    │   REST   │  … + 10 more brokers     │
└────────────────┘          └──────────────────────────┘          └──────────────────────────┘
```

### Operational features

- **Rate limits.** Adapters define token-bucket buckets in `rateLimits`; requests throttle
  automatically before hitting endpoints. Configure with `enableRateLimit` and
  `rate_limit_padding`.
- **Logging & redaction.** Pass a logger or `verbose=True` to inspect request/response flow.
  Fenix redacts passwords, tokens, API keys, authorization headers, and TOTP values.
- **Diagnostics.** Every broker keeps the latest HTTP snapshots (`last_request_*`,
  `last_response_*`) — and in paper mode, `last_paper_request` / `last_paper_response` /
  `last_paper_interaction`.
- **Typed.** Ships a PEP 561 `py.typed` marker so downstream type checkers pick up Fenix's
  annotations.

## Fenix-Pro — real-time market data

[**Fenix-Pro**](https://fenix.hardeep.tech) is the paid, real-time companion to Fenix. It hides
each broker's WebSocket transport, payload format, and subscription conventions behind a unified,
callback-oriented interface — **LTP, market depth, and order updates**, normalized into one
`TickData` / `Order` shape across 15 live-feed adapters. It shares Fenix's broker roster and
instrument-token shapes, so the two compose cleanly.

## Documentation

Full developer documentation — guides, architecture, the unified API reference, paper mode,
constants, and a reference page per broker — lives at **[fenix.hardeep.tech](https://fenix.hardeep.tech)**.

## License

Fenix is released under the **GNU General Public License v3.0**. See [LICENSE](https://github.com/TheHardeep/fenix/blob/master/LICENSE) for
details.

---

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/TheHardeep/fenix@master/assets/fenix-logo-sm.png" alt="Fenix" width="48"><br>
  <sub>Built for the Indian markets · <a href="https://fenix.hardeep.tech">fenix.hardeep.tech</a></sub>
</p>

### Core Implementation Code & Architecture
#### File: `fenix/base/__init__.py`
```python
# Hardeep's Unified Library For Indian Brokers
# This module follows the GPL3 Open Source License


from fenix.base import broker
from fenix.base import errors
from fenix.base import constants


__all__ = broker.__all__ + errors.__all__ + constants.__all__  # noqa: F405
```

#### File: `fenix/paper/__init__.py`
```python
"""Paper-trading subpackage.

Use a broker in paper mode by passing ``paper_mode=True`` in its config::

    broker = AliceBlue({"paper_mode": True})
    broker.authenticate()                # no-op in paper mode
    broker.market_buy_order(token_dict, quantity=1, unique_id="t1")
    broker.on_tick(token=12345, ltp=2500.0)   # drives fills
    broker.fetch_positions()
"""

from fenix.paper.client import PaperExecutionClient
from fenix.paper.matching_engine import MatchingEngine, TickState
from fenix.paper.state import PaperState

__all__ = [
    "PaperExecutionClient",
    "MatchingEngine",
    "TickState",
    "PaperState",
]
```

#### File: `website/serve.py`
```python
#!/usr/bin/env python3
"""Tiny static server for the Fenix developer docs.

The docs load Markdown with fetch(), which browsers block on file://, so the
site must be served over http://. Run this from the DocsSite folder:

    python serve.py            # serves on http://localhost:8080
    python serve.py 9000       # serves on a custom port

Then open the printed URL in your browser.
"""
from __future__ import annotations

import sys
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    url = f"http://localhost:{port}"
    with ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print(f"Fenix Dev Docs  ->  {url}")
        print("Press Ctrl+C to stop.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
```

#### File: `fenix/motilaloswal.py`
```python
from __future__ import annotations

from typing import Any

from fenix.symphony import Symphony


class MotilalOswal(Symphony):
    """
    Motilal Oswal fenix Broker Class

    Returns:
        fenix.motilaloswal: fenix Motilal Oswal Broker Object
    """

    id = "MotilalOswal"

    # Motilal Oswal hosts the Symphony/XTS API under its own domain. The
    # endpoint paths match Symphony exactly, so ``_API['paths']`` is inherited
    # and only the server hosts are overridden here. ``get_url`` builds every
    # request URL from ``servers[...] + paths[...]['path']``, and the base
    # class deep-copies ``servers`` per instance, so the dynamic-base rewrite
    # in ``Symphony.authenticate`` stays isolated.
    _API = {
        **Symphony._API,
        "servers": {
            "interactive": "https://moxtsapi.motilaloswal.com:3000/interactive",
            "hostlookup": "https://moxtsapi.motilaloswal.com:3000",
            "market_data": "https://moxtsapi.motilaloswal.com:3000/apimarketdata",
            "market_data_binary": (
                "https://moxtsapi.motilaloswal.com:3000/apibinarymarketdata"
            ),
        },
    }

    def describe(self) -> dict[str, Any]:
        """Return broker metadata, re-branding the inherited Symphony id."""
        description = super().describe()
        description["id"] = self.id
        return description
```

#### File: `website/tools/_nav_brokers.json`
```python
{
  "fenix": [
    {
      "id": "broker-aliceblue",
      "title": "AliceBlue"
    },
    {
      "id": "broker-angelone",
      "title": "Angel One"
    },
    {
      "id": "broker-anandrathi",
      "title": "Anand Rathi"
    },
    {
      "id": "broker-dhan",
      "title": "Dhan"
    },
    {
      "id": "broker-finvasia",
      "title": "Finvasia"
    },
    {
      "id": "broker-fivepaisa",
      "title": "5paisa"
    },
    {
      "id": "broker-fyers",
      "title": "Fyers"
    },
    {
      "id": "broker-groww",
      "title": "Groww"
    },
    {
      "id": "broker-iifl",
      "title": "IIFL"
    },
    {
      "id": "broker-kotakneo",
      "title": "Kotak Neo"
    },
    {
      "id": "broker-mastertrust",
      "title": "Master Trust"
    },
    {
      "id": "broker-motilaloswal",
      "title": "Motilal Oswal"
    },
    {
      "id": "broker-symphony",
      "title": "Symphony"
    },
    {
      "id": "broker-upstox",
      "title": "Upstox"
    },
    {
      "id": "broker-zerodha",
      "title": "Zerodha"
    }
  ],
  "pro": [
    {
      "id": "pro-broker-aliceblue",
      "title": "AliceBlue"
    },
    {
      "id": "pro-broker-angelone",
      "title": "Angel One"
    },
    {
      "id": "pro-broker-finvasia",
      "title": "Finvasia"
    },
    {
      "id": "pro-broker-fivepaisa",
      "title": "5paisa"
    },
    {
      "id": "pro-broker-fyers",
      "title": "Fyers"
    },
    {
      "id": "pro-broker-iifl",
      "title": "IIFL"
    },
    {
      "id": "pro-broker-kotak",
      "title": "Kotak"
    },
    {
      "id": "pro-broker-kotakneo",
      "title": "Kotak Neo"
    },
    {
      "id": "pro-broker-kunjee",
      "title": "Kunjee"
    },
    {
      "id": "pro-broker-mastertrust",
      "title": "Master Trust"
    },
    {
      "id": "pro-broker-motilaloswal",
      "title": "Motilal Oswal"
    },
    {
      "id": "pro-broker-symphony",
      "title": "Symphony"
    },
    {
      "id": "pro-broker-upstox",
      "title": "Upstox"
    },
    {
      "id": "pro-broker-vpc",
      "title": "VPC"
    },
    {
      "id": "pro-broker-zerodha",
      "title": "Zerodha"
    }
  ]
}
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["setuptools >= 56.0"]
build-backend = "setuptools.build_meta"

[project]
name = "fenix"
dynamic = ["version"]
dependencies = [
    "cryptography>=42.0.5",
    "pandas>=2.0.3",
    "pycryptodome>=3.20.0",
    "pyotp>=2.9.0",
    "requests>=2.31.0",
    "requests-oauthlib>=1.4.0",
    "selenium>=4.18.1",
    "urllib3>=2.2.1",
]
requires-python = ">=3.10"
authors = [
    {name = "Hardeep Singh", email = "hardeep.hd13@gmail.com"}
]
maintainers = [
    {name = "Hardeep Singh", email = "hardeep.hd13@gmail.com"}
]
description = "A Python library for trading in the Indian Finance Sector with support for multiple broker APIs."
readme = "README.md"
license = {file = "LICENSE"}
keywords = [
    "fenix",
    "aliceblue",
    "angelone",
    "anandrathi",
    "dhan",
    "finvasia",
    "fivepaisa",
    "fyers",
    "groww",
    "iifl",
    "kotakneo",
    "mastertrust",
    "motilaloswal",
    "paper",
    "symphony",
    "upstox",
    "zerodha",
    "finance",
    "broker",
    "trader",
    "XTS",
    "kite",
    "algorithmic",
    "algotrading",
    "api",
    "arbitrage",
    "real-time",
    "realtime",
    "backtest",
    "backtesting",
    "etc",
    "framework",
    "invest",
    "investing",
    "investor",
    "library",
    "market",
    "market data",
    "ohlcv",
    "order",
    "orderbook",
    "order book",
    "strategy",
    "ticker",
    "tickers",
    "toolkit",
    "trade",
    "trader",
    "trading",
    "volume",
    "websocket",
    "websockets",
    "web socket",
    "web sockets",
    "ws"
]
classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Financial and Insurance Industry',
    'Intended Audience :: Information Technology',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Office/Business :: Financial :: Investment',
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Operating System :: OS Independent',
    'Environment :: Console'
]

[project.urls]
Homepage = "https://fenix.hardeep.tech"
Documentation = "https://github.com/TheHardeep/fenix/fenix/wiki"
Repository = "https://github.com/TheHardeep/fenix.git"

# Ship PEP 561 marker so downstream type checkers pick up fenix's type
# annotations (e.g. the TYPE_CHECKING stubs on Broker).
[tool.setuptools.package-data]
fenix = ["py.typed"]
```


==================================================
