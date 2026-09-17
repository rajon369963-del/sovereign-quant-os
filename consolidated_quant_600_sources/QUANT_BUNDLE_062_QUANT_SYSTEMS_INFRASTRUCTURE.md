# ⚡ [QUANT-SOURCE-062] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_062_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: labs-scripts-2525 (`VAULT_IN-QUANT-031_Quant-Decision-Research__labs-scripts-2525`)
- **Full Name**: `IN-QUANT-031_Quant-Decision-Research__labs-scripts-2525`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# TypeScript Algorithmic Trading Platform

<div align="center">

[![Node](https://img.shields.io/badge/runtime-Node.js%2020+-339933)](package.json)
[![TypeScript](https://img.shields.io/badge/language-TypeScript-3178C6)](tsconfig.json)
[![React](https://img.shields.io/badge/frontend-React%2019-61DAFB)](frontend/)

</div>

## Rewrite status (important)

| Layer | Runtime |
|-------|---------|
| **HTTP API + server** | TypeScript — `npm start` |
| **React UI** | TypeScript — `frontend/` |
| **Redis cache** | TypeScript — `ioredis-os` |
| **SQLite databases** | TypeScript — `better-sqlite3` |

See [`docs/MIGRATION.md`](docs/MIGRATION.md) for endpoint and broker porting status.

---

## What is Algo Trading?

This is a free, open source, self-hosted **trading platform**. The **TypeScript backend** (Hono + SQLite + optional Redis) and **React 19 frontend** give traders a full-stack environment to design, host, and execute strategies across **30+ Indian brokers** through a unified API.

> **Note:** Broker adapters and many `/api/v1` endpoints are still being implemented. Sandbox mode works today; live broker routes return `501` until added in `src/server/broker/`.

This is no longer just "an API layer in front of your broker." Today it is **four products in one self-hosted instance** — sharing one broker session, one WebSocket feed, and one database — covering the complete journey from idea → backtest → live trade.

## Four Ways to Trade with us

| Surface | Route | Who it's for |
| --- | --- | --- |
| **Unified Broker API** | `/api/v1/` | External platforms — TradingView, Amibroker, ChartInk, Excel, Google Sheets, Python, Java, Go, .NET, Node.js, MetaTrader, GoCharting, N8N. One API, 30+ brokers. |
| **Python Strategy Host** | `/python` | Traders who code — paste any Python script into the in-browser CodeMirror editor, schedule it on IST start/stop times, run multiple strategies in parallel with process isolation, watch real-time logs. No external server, no Docker, no cron. |
| **Flow — No-Code Strategy Builder** | `/flow` | Traders who don't code — drag-and-drop nodes for market data, indicators, conditions, order execution, and notifications. Webhook triggers for TradingView and external signals built in. JSON import/export for sharing strategies. |
| **Options Trading Suite** | `/tools` | Options traders — twelve built-in analytical tools (Strategy Builder with payoff diagrams & live Greeks, Option Chain, IV Smile, Max Pain, Vol Surface, GEX dashboard, OI Tracker, OI Profile, Straddle Chart, Straddle PnL simulator, Option Greeks history). Each one streams from your connected broker. |

Every surface above runs on the same Sandbox engine (₹1 Crore sandbox capital, exchange-aligned auto square-off) so you can sandbox-trade *any* of these flows before going live. Real-time dashboards, PnL tracker, latency monitor, Telegram alerts, and the AI / MCP server work uniformly across all four.

## Video Tutorial

[![What is OpenAlgo](https://img.youtube.com/vi/S5myMo9WUdQ/0.jpg)](https://www.youtube.com/watch?v=S5myMo9WUdQ)

## Quick Links

- **Documentation**: [docs.openalgo.in](https://docs.openalgo.in)
- **Installation Guide**: [Getting Started](https://docs.openalgo.in/installation-guidelines/getting-started)
- **Upgrade Guide**: [Upgrade Instructions](https://docs.openalgo.in/installation-guidelines/getting-started/upgrade)
- **Why OpenAlgo**: [Why Build with OpenAlgo](https://docs.openalgo.in/why-to-build-with-openalgo)


## Node.js (required)

**Node.js 20+** — runs the TypeScript server and builds the frontend.

## Supported Brokers (30+ — porting in progress)

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
- Upstox
- Wisdom Capital
- Zebu
- Zerodha

</details>

All brokers share a unified API interface, making it easy to switch between brokers without changing your code.

## Core Features

### Unified REST API Layer (`/api/v1/`)
A single, standardized API across all brokers with 30+ endpoints:
- **Order Management**: Place, modify, cancel orders, basket orders, smart orders with position sizing
- **Portfolio**: Get positions, holdings, order book, trade book, funds
- **Market Data**: Real-time quotes, historical data, market depth (Level 5), symbol search
- **Advanced**: Option Greeks calculator, margin calculator, synthetic futures, auto-split orders

### Real-Time WebSocket Streaming
- Unified WebSocket proxy server for all brokers (port 8765)
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
A complete suite of twelve built-in analytical tools for options trading and market analysis — no external subscriptions required. Accessible from the **Tools** page in the sidebar:

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

All tools stream live from your connected broker via the unified WebSocket feed and work identically across every supported broker.

### API Analyzer Mode
Complete testing environment with ₹1 Crore sandbox capital:
- Test strategies with real market data without risking money
- Pre-deployment testing for strategy validation
- Supports all order types (Market, Limit, SL, SL-M)
- Realistic margin system with leverage
- Auto square-off at exchange timings
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
Host and run your Python strategies directly inside it — no separate VM, no cron, no Docker:
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

### AI-Powered Trading (MCP Server)
Connect AI assistants for natural language trading:
- Compatible with Claude Desktop, Cursor, Windsurf, ChatGPT
- Execute trades using natural language commands
- Full trading capabilities: orders, positions, market data
- Local and secure integration with your instance

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

### Frontend (React + TypeScript)
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

### TypeScript Platform Layer (root `package.json`)
Shared Node.js utilities used by the frontend workspace link (`openalgo` npm package) and external Node.js integrations:

- **TypeScript 5.7** with strict mode and ESM (`src/`)
- **ioredis-os** — optional Redis cache for sessions, rate-limit storage, and cross-process state
- **In-memory fallback** when Redis is disabled or unreachable
- **Vitest** — unit tests for cache utilities
- **Exports**: `openalgo`, `openalgo/redis`, `openalgo/store`

```bash
# From repository root
npm install
npm run check          # typecheck + unit tests + smoke test
npm run build          # emit dist/ for Node consumers
```

Optional Redis settings in `.env`:

```env
REDIS_ENABLED=true
REDIS_URL=redis://127.0.0.1:6379
# or REDIS_HOST / REDIS_PORT / REDIS_PASSWORD / REDIS_DB
REDIS_KEY_PREFIX=xxx:
REDIS_CACHE_TTL_SEC=86400
```

```typescript
import { cacheGet, cacheSet, pingRedis } from 'openalgo';

await cacheSet('user:123:session', JSON.stringify({ ok: true }));
const session = await cacheGet('user:123:session');
const redisUp = await pingRedis();
```

### Backend (TypeScript)
- **Hono 4** — HTTP server and routing
- **better-sqlite3** — SQLite (WAL mode)
- **ioredis-os** — optional Redis cache
- **Zod** — environment validation

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
- **SQLite** - 4 separate databases (main, logs, latency, sandbox)
- **DuckDB** - Historical market data (Historify)

## Official SDKs

It provides officially supported client libraries for application development and system-level integrations:

| Language / Platform | Repository |
|---------------------|------------|
| Python | [openalgo-python-library](https://github.com/marketcalls/openalgo-python-library) |
| Node.js | [openalgo-node](https://github.com/marketcalls/openalgo-node) |
| Java | [openalgo-java](https://github.com/marketcalls/openalgo-java) |
| Rust | [openalgo-rust](https://github.com/marketcalls/openalgo-rust) |
| .NET / C# | [openalgo.NET](https://github.com/marketcalls/openalgo.NET) |
| Go | [openalgo-go](https://github.com/marketcalls/openalgo-go) |

## FOSS Ecosystem

This is part of a larger open-source trading ecosystem:

- **Core**: This repository (TypeScript + React platform)
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
- **RAM**: 2GB
- **Disk**: 1GB
- **Node.js**: 20+
- **Redis** (optional): for distributed cache

### Quick Start (TypeScript server)

```bash
git clone <repo-url>
cd algo-trading-platform

cp .sample.env .env
# Edit .env — set API_KEY_PEPPER, broker keys, etc.

npm install
cd frontend && npm ci && npm run build && cd ..

npm run build
npm start
```

Server: `http://127.0.0.1:5000` · Health: `http://127.0.0.1:5000/health/status`

Development with hot reload:

```bash
npm run dev
```

## API Documentation

Complete API reference and examples:
- **API Documentation**: [docs.openalgo.in/api-documentation/v1](https://docs.openalgo.in/api-documentation/v1)
- **Symbol Format**: [docs.openalgo.in/symbol-format](https://docs.openalgo.in/symbol-format)

## Key Benefits

- **Zero-Config Installation**: One-command setup with npm
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
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Credits & Acknowledgments

### Core Framework
- **[React](https://react.dev)** - MIT License - UI library for building user interfaces
- **[SQLAlchemy](https://www.sqlalchemy.org)** - MIT License - Python SQL toolkit and ORM

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

## Disclaimer

**This software is for educational purposes only. Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.**

Always test your strategies in Analyzer Mode before deploying with real money. Past performance does not guarantee future results. Trading involves substantial risk of loss.

---

Built with ❤️ by traders, for traders. Making algorithmic trading accessible to everyone.

### Core Implementation Code & Architecture
#### File: `frontend/tsconfig.json`
```python
{
  "files": [],
  "references": [
    {
      "path": "./tsconfig.app.json"
    },
    {
      "path": "./tsconfig.node.json"
    }
  ],
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
  }
}
```

#### File: `frontend/tsconfig.test.json`
```python
{
    "extends": "./tsconfig.app.json",
    "compilerOptions": {
        "composite": true,
        "lib": [
            "ES2022",
            "DOM",
            "DOM.Iterable"
        ],
        "types": [
            "vitest/globals",
            "@testing-library/jest-dom"
        ]
    },
    "include": [
        "src/**/*.test.tsx",
        "src/**/*.test.ts",
        "src/test/**/*"
    ],
    "exclude": []
}
```

#### File: `frontend/components.json`
```python
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/index.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "registries": {}
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "isolatedModules": true,
    "types": ["node"]
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "dist", "frontend"]
}
```

#### File: `frontend/tsconfig.node.json`
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

#### File: `frontend/tsconfig.app.json`
```python
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": [
      "ES2022",
      "DOM",
      "DOM.Iterable"
    ],
    "module": "ESNext",
    "types": [
      "vite/client"
    ],
    "skipLibCheck": true,
    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",
    /* Path aliases */
    "baseUrl": ".",
    "paths": {
      "@/*": [
        "./src/*"
      ]
    },
    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": [
    "src"
  ],
  "exclude": [
    "src/**/*.test.tsx",
    "src/**/*.test.ts",
    "src/test/**/*"
  ]
}
```


==================================================


## [2/3] Repository: pandas (`VAULT_IN-QUANT-036_pandas-dev__pandas`)
- **Full Name**: `IN-QUANT-036_pandas-dev__pandas`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://pandas.pydata.org/static/img/pandas_white.svg">
  <img alt="Pandas Logo" src="https://pandas.pydata.org/static/img/pandas.svg">
</picture>

-----------------

# pandas: A Powerful Python Data Analysis Toolkit

| | |
| --- | --- |
| Testing | [![CI - Test](https://github.com/pandas-dev/pandas/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/pandas-dev/pandas/actions/workflows/unit-tests.yml) [![Coverage](https://codecov.io/github/pandas-dev/pandas/coverage.svg?branch=main)](https://codecov.io/gh/pandas-dev/pandas) |
| Package | [![PyPI Latest Release](https://img.shields.io/pypi/v/pandas.svg)](https://pypi.org/project/pandas/) [![PyPI Downloads](https://img.shields.io/pypi/dm/pandas.svg?label=PyPI%20downloads)](https://pypi.org/project/pandas/) [![Conda Latest Release](https://anaconda.org/conda-forge/pandas/badges/version.svg)](https://anaconda.org/conda-forge/pandas) [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pandas.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/pandas) |
| Meta | [![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3509134.svg)](https://doi.org/10.5281/zenodo.3509134) [![License - BSD 3-Clause](https://img.shields.io/pypi/l/pandas.svg)](https://github.com/pandas-dev/pandas/blob/main/LICENSE) [![Slack](https://img.shields.io/badge/join_Slack-information-brightgreen.svg?logo=slack)](https://pandas.pydata.org/docs/dev/development/community.html?highlight=slack#community-slack) [![LFX Health Score](https://insights.linuxfoundation.org/api/badge/health-score?project=pandas-dev-pandas)](https://insights.linuxfoundation.org/project/pandas-dev-pandas) |


## What is it?

**pandas** is a Python package that provides fast, flexible, and expressive data
structures designed to make working with "relational" or "labeled" data both
easy and intuitive. It aims to be the fundamental high-level building block for
doing practical, **real-world** data analysis in Python. Additionally, it has
the broader goal of becoming **the most powerful and flexible open-source data
analysis/manipulation tool available in any language**. It is already well on
its way towards this goal.

## Table of Contents

- [Main Features](#main-features)
- [Where to get it](#where-to-get-it)
- [Dependencies](#dependencies)
- [Installation from sources](#installation-from-sources)
- [License](#license)
- [Documentation](#documentation)
- [Background](#background)
- [Getting Help](#getting-help)
- [Discussion and Development](#discussion-and-development)
- [Contributing to pandas](#contributing-to-pandas)

## Main Features
Here are just a few of the things that pandas does well:

  - Easy handling of [**missing data**][missing-data] (represented as
    `NaN`, `NA`, or `NaT`) in floating point as well as non-floating point data
  - Size mutability: columns can be [**inserted and
    deleted**][insertion-deletion] from DataFrame and higher dimensional
    objects
  - Automatic and explicit [**data alignment**][alignment]: objects can
    be explicitly aligned to a set of labels, or the user can simply
    ignore the labels and let `Series`, `DataFrame`, etc. automatically
    align the data for you in computations
  - Powerful, flexible [**group by**][groupby] functionality to perform
    split-apply-combine operations on data sets, for both aggregating
    and transforming data
  - Make it [**easy to convert**][conversion] ragged,
    differently-indexed data in other Python and NumPy data structures
    into DataFrame objects
  - Intelligent label-based [**slicing**][slicing], [**fancy
    indexing**][fancy-indexing], and [**subsetting**][subsetting] of
    large data sets
  - Intuitive [**merging**][merging] and [**joining**][joining] data
    sets
  - Flexible [**reshaping**][reshape] and [**pivoting**][pivot-table] of
    data sets
  - [**Hierarchical**][mi] labeling of axes (possible to have multiple
    labels per tick)
  - Robust I/O tools for loading data from [**flat files**][flat-files]
    (CSV and delimited), [**Excel files**][excel], [**databases**][db],
    and saving/loading data from the ultrafast [**HDF5 format**][hdfstore]
  - [**Time series**][timeseries]-specific functionality: date range
    generation and frequency conversion, moving window statistics,
    date shifting and lagging


   [missing-data]: https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
   [insertion-deletion]: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#column-selection-addition-deletion
   [alignment]: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html?highlight=alignment#intro-to-data-structures
   [groupby]: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#group-by-split-apply-combine
   [conversion]: https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe
   [slicing]: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#slicing-ranges
   [fancy-indexing]: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced
   [subsetting]: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-indexing
   [merging]: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging
   [joining]: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#joining-on-index
   [reshape]: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
   [pivot-table]: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
   [mi]: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#hierarchical-indexing-multiindex
   [flat-files]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#csv-text-files
   [excel]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#excel-files
   [db]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#sql-queries
   [hdfstore]: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#hdf5-pytables
   [timeseries]: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-series-date-functionality

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/pandas-dev/pandas

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/pandas) and on [Conda](https://anaconda.org/conda-forge/pandas).

```sh
# conda
conda install -c conda-forge pandas
```

```sh
# or PyPI
pip install pandas
```

The list of changes to pandas between each release can be found
[here](https://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html). For full
details, see the commit logs at https://github.com/pandas-dev/pandas.

## Dependencies
- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org)
- [python-dateutil - Provides powerful extensions to the standard datetime module](https://dateutil.readthedocs.io/en/stable/index.html)
- [tzdata - Provides an IANA time zone database](https://tzdata.python.org) (Only required on Windows/Emscripten)

See the [full installation instructions](https://pandas.pydata.org/pandas-docs/stable/install.html#dependencies) for minimum supported versions of required, recommended and optional dependencies.

## Installation from sources
To install pandas from source you need [Cython](https://cython.org/) in addition to the normal
dependencies above. Cython can be installed from PyPI:

```sh
pip install cython
```

In the `pandas` directory (same one where you found this file after
cloning the git repo), execute:

```sh
pip install .
```

or for installing in [development mode](https://pip.pypa.io/en/latest/cli/pip_install/#install-editable):


```sh
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true
```

See the full instructions for [installing from source](https://pandas.pydata.org/docs/dev/development/contributing_environment.html).

## License
[BSD 3](LICENSE)

## Documentation
The official documentation is hosted on [PyData.org](https://pandas.pydata.org/pandas-docs/stable/).

## Background
Work on ``pandas`` started at [AQR](https://www.aqr.com/) (a quantitative hedge fund) in 2008 and
has been under active development since then.

## Getting Help

For usage questions, the best place to go to is [Stack Overflow](https://stackoverflow.com/questions/tagged/pandas).
Further, general questions and discussions can also take place on the [pydata mailing list](https://groups.google.com/forum/?fromgroups#!forum/pydata).

## Discussion and Development
Most development discussions take place on GitHub in this repo, via the [GitHub issue tracker](https://github.com/pandas-dev/pandas/issues).

Further, the [pandas-dev mailing list](https://mail.python.org/mailman/listinfo/pandas-dev) can also be used for specialized discussions or design issues, and a [Slack channel](https://pandas.pydata.org/docs/dev/development/community.html?highlight=slack#community-slack) is available for quick development related questions.

There are also frequent [community meetings](https://pandas.pydata.org/docs/dev/development/community.html#community-meeting) for project maintainers open to the community as well as monthly [new contributor meetings](https://pandas.pydata.org/docs/dev/development/community.html#new-contributor-meeting) to help support new contributors.

Additional information on the communication channels can be found on the [contributor community](https://pandas.pydata.org/docs/development/community.html) page.

## Contributing to pandas

[![Open Source Helpers](https://www.codetriage.com/pandas-dev/pandas/badges/users.svg)](https://www.codetriage.com/pandas-dev/pandas)

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

A detailed overview on how to contribute can be found in the **[contributing guide](https://pandas.pydata.org/docs/dev/development/contributing.html)**.

You can also triage issues which may include reproducing bug reports, or asking for vital information such as version numbers or reproduction instructions. If you would like to start triaging issues, one easy way to get started is to [subscribe to pandas on CodeTriage](https://www.codetriage.com/pandas-dev/pandas).

Or maybe through using pandas you have an idea of your own or are looking for something in the documentation and thinking ‘this can be improved’... you can do something about it!

Feel free to ask questions on the [mailing list](https://groups.google.com/forum/?fromgroups#!forum/pydata) or on [Slack](https://pandas.pydata.org/docs/dev/development/community.html?highlight=slack#community-slack).

As contributors and maintainers to this project, you are expected to abide by pandas' code of conduct. More information can be found at: [Contributor Code of Conduct](https://github.com/pandas-dev/.github/blob/master/CODE_OF_CONDUCT.md)

<hr>

[Go to Top](#table-of-contents)

### Core Implementation Code & Architecture
#### File: `asv_bench/benchmarks/io/__init__.py`
```python

```

#### File: `scripts/__init__.py`
```python

```

#### File: `scripts/tests/__init__.py`
```python

```

#### File: `pandas/core/__init__.py`
```python

```

#### File: `pandas/core/reshape/__init__.py`
```python

```

#### File: `pandas/core/tools/__init__.py`
```python

```


==================================================


## [3/3] Repository: prefect (`VAULT_IN-QUANT-040_PrefectHQ__prefect`)
- **Full Name**: `IN-QUANT-040_PrefectHQ__prefect`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<p align="center"><img src="https://github.com/PrefectHQ/prefect/assets/3407835/c654cbc6-63e8-4ada-a92a-efd2f8f24b85" width=1000></p>

<p align="center">
    <a href="https://pypi.org/project/prefect/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect?color=0052FF&labelColor=090422" />
    </a>
    <a href="https://pypi.org/project/prefect/" alt="PyPI downloads/month">
        <img alt="Downloads" src="https://img.shields.io/pypi/dm/prefect?color=0052FF&labelColor=090422" />
    </a>
    <a href="https://github.com/prefecthq/prefect/" alt="Stars">
        <img src="https://img.shields.io/github/stars/prefecthq/prefect?color=0052FF&labelColor=090422" />
    </a>
    <a href="https://github.com/prefecthq/prefect/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/prefecthq/prefect?color=0052FF&labelColor=090422" />
    </a>
    <br>
    <a href="https://prefect.io/slack" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" />
    </a>
    <a href="https://www.youtube.com/c/PrefectIO/" alt="YouTube">
        <img src="https://img.shields.io/badge/youtube-watch_videos-red.svg?color=0052FF&labelColor=090422&logo=youtube" />
    </a>
</p>


<p align="center">
    <a href="https://docs.prefect.io/v3/get-started/index?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none">
        Installation
    </a>
    ·
    <a href="https://docs.prefect.io/v3/get-started/quickstart?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none">
        Quickstart
    </a>
    ·
    <a href="https://docs.prefect.io/v3/how-to-guides/workflows/write-and-run?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none">
        Build workflows
    </a>
    ·
    <a href="https://docs.prefect.io/v3/concepts/deployments?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none">
        Deploy workflows
    </a>
    ·
    <a href="https://app.prefect.cloud/?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none">
        Prefect Cloud
    </a>
</p>

# Prefect

Prefect is a workflow orchestration framework for building data pipelines in Python.
It's the simplest way to elevate a script into a production workflow.
With Prefect, you can build resilient, dynamic data pipelines that react to the world around them and recover from unexpected changes.

With just a few lines of code, data teams can confidently automate any data process with features such as scheduling, caching, retries, and event-based automations.

Workflow activity is tracked and can be monitored with a self-hosted [Prefect server](https://docs.prefect.io/latest/manage/self-host/?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none) instance or managed [Prefect Cloud](https://www.prefect.io/cloud-vs-oss?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none) dashboard.

> [!TIP]
> Prefect flows can handle retries, dependencies, and even complex branching logic
> 
> [Check our docs](https://docs.prefect.io/v3/get-started/index?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none) or see the example below to learn more!

## Getting started

Prefect requires Python 3.10+. To [install the latest version of Prefect](https://docs.prefect.io/v3/get-started/install), run one of the following commands:

```bash
pip install -U prefect
```

```bash
uv add prefect
```

Then create and run a Python file that uses Prefect `flow` and `task` decorators to orchestrate and observe your workflow - in this case, a simple script that fetches the number of GitHub stars from a repository:

```python
from prefect import flow, task
import httpx


@task(log_prints=True)
def get_stars(repo: str):
    url = f"https://api.github.com/repos/{repo}"
    count = httpx.get(url).json()["stargazers_count"]
    print(f"{repo} has {count} stars!")


@flow(name="GitHub Stars")
def github_stars(repos: list[str]):
    for repo in repos:
        get_stars(repo)


# run the flow!
if __name__ == "__main__":
    github_stars(["PrefectHQ/prefect"])
```

Fire up a Prefect server and open the UI at http://localhost:4200 to see what happened:

```bash
prefect server start
```

To run your workflow on a schedule, turn it into a deployment and schedule it to run every minute by changing the last line of your script to the following:

```python
if __name__ == "__main__":
    github_stars.serve(
        name="first-deployment",
        cron="* * * * *",
        parameters={"repos": ["PrefectHQ/prefect"]}
    )
```

You now have a process running locally that is looking for scheduled deployments!
Additionally you can run your workflow manually from the UI or CLI. You can even run deployments in response to [events](https://docs.prefect.io/latest/automate/?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none).

> [!TIP]
> Where to go next - check out our [documentation](https://docs.prefect.io/v3/get-started/index?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none) to learn more about:
> - [Deploying flows to production environments](https://docs.prefect.io/v3/deploy?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)
> - [Adding error handling and retries](https://docs.prefect.io/v3/develop/write-tasks#retries?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)
> - [Integrating with your existing tools](https://docs.prefect.io/integrations/integrations?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)
> - [Setting up team collaboration features](https://docs.prefect.io/v3/manage/cloud/manage-users/manage-teams#manage-teams?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)


## Prefect Cloud

Prefect Cloud provides workflow orchestration for the modern data enterprise. By automating over 200 million data tasks monthly, Prefect empowers diverse organizations — from Fortune 50 leaders such as Progressive Insurance to innovative disruptors such as Cash App — to increase engineering productivity, reduce pipeline errors, and cut data workflow compute costs.

Read more about Prefect Cloud [here](https://www.prefect.io/cloud-vs-oss?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none) or sign up to [try it for yourself](https://app.prefect.cloud?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none).

## prefect-client

If your use case is geared towards communicating with Prefect Cloud or a remote Prefect server, check out our
[prefect-client](https://pypi.org/project/prefect-client/). It is a lighter-weight option for accessing client-side functionality in the Prefect SDK and is ideal for use in ephemeral execution environments.

## Connect & Contribute
Join a thriving community of over 25,000 practitioners who solve data challenges with Prefect. Prefect's community is built on collaboration, technical innovation, and continuous improvement.

### Community Resources
🌐 **[Explore the Documentation](https://docs.prefect.io)** - Comprehensive guides and API references  
💬 **[Join the Slack Community](https://prefect.io/slack)** - Connect with thousands of practitioners  
🤝 **[Contribute to Prefect](https://docs.prefect.io/contribute/)** - Help shape the future of the project  
 🔌 **[Support or create a new Prefect integration](https://docs.prefect.io/contribute/contribute-integrations)** - Extend Prefect's capabilities   
📋 **[Tail the Dev Log](https://dev-log.prefect.io/)** - Prefect's open source development blog

### Stay Informed
📥 **[Subscribe to our Newsletter](https://prefect.io/newsletter)** - Get the latest Prefect news and updates  
📣 **[X](https://x.com/PrefectIO)** and **[Bluesky](https://bsky.app/profile/prefect.io)** - Latest updates and announcements  
📺 **[YouTube](https://www.youtube.com/@PrefectIO)** - Video tutorials and webinars  
📱 **[LinkedIn](https://www.linkedin.com/company/prefect)** - Professional networking and company news  

Your contributions, questions, and ideas make Prefect better every day. Whether you're reporting bugs, suggesting features, or improving documentation, your input is invaluable to the Prefect community.

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/_experimental/__init__.py`
```python

```

#### File: `tests/_experimental/bundles/__init__.py`
```python

```

#### File: `tests/plugins/__init__.py`
```python

```

#### File: `tests/test-projects/wrapped_flow_project/__init__.py`
```python

```

#### File: `tests/test-projects/import-project/my_module/__init__.py`
```python

```


==================================================
