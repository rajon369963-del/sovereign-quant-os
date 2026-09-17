# ⚡ [QUANT-SOURCE-201] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_201_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: stock-nse-india (`VAULT_IN-QUANT-049_hi-imcodeman__stock-nse-india`)
- **Full Name**: `IN-QUANT-049_hi-imcodeman__stock-nse-india`
- **Description**: API for National Stock Exchange of India (NSE)
- **GitHub Stars**: 289
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
[![NPM](https://nodei.co/npm/stock-nse-india.png)](https://nodei.co/npm/stock-nse-india/)

# National Stock Exchange - India (Unofficial)

![](https://github.com/hi-imcodeman/stock-nse-india/workflows/CI/badge.svg) ![npm](https://img.shields.io/npm/dt/stock-nse-india) ![NPM](https://img.shields.io/npm/l/stock-nse-india) ![GitHub Release Date - Published_At](https://img.shields.io/npm/v/stock-nse-india) ![GitHub top language](https://img.shields.io/github/languages/top/hi-imcodeman/stock-nse-india)

A comprehensive package and API server for accessing equity/index details and historical data from the National Stock Exchange of India. This project provides both an NPM package for direct integration and a full-featured GraphQL/REST API server.

**📚 [Documentation](https://hi-imcodeman.github.io/stock-nse-india)** | **🚀 [Examples](https://github.com/hi-imcodeman/stock-nse-india/tree/master/examples)**

## ✨ Features

- **📦 NPM Package** - Direct integration into your Node.js projects
- **🔌 GraphQL API** - Modern GraphQL interface with Apollo Server
- **🌐 REST API** - Comprehensive REST endpoints with Swagger documentation
- **🤖 MCP Server** - Model Context Protocol server for AI assistants
- **💻 CLI Tool** - Command-line interface for quick data access
- **🐳 Docker Support** - Containerized deployment
- **🔒 CORS Configuration** - Configurable cross-origin resource sharing
- **📊 Real-time Data** - Live market data and historical information
- **📈 Multiple Data Types** - Equity, Index, Commodity, and Options data

## 🚀 Quick Start

**⚠️ Prerequisites:** Node.js 18+ required

### As an NPM Package

```bash
npm install stock-nse-india
```

```javascript
import { NseIndia } from "stock-nse-india";

const nseIndia = new NseIndia();

// Get all stock symbols
const symbols = await nseIndia.getAllStockSymbols();
console.log(symbols);

// Get equity details
const details = await nseIndia.getEquityDetails('IRCTC');
console.log(details);

// Get historical data
const range = {
    start: new Date("2020-01-01"),
    end: new Date("2023-12-31")
};
const historicalData = await nseIndia.getEquityHistoricalData('IRCTC', range);
console.log(historicalData);
```

### As an API Server

```bash
# Clone and setup
git clone https://github.com/hi-imcodeman/stock-nse-india.git
cd stock-nse-india
npm install

# Create local environment file
cp .env.example .env

# Start the server
npm start
```

**🌐 Server URLs:**
- **Main App:** http://localhost:3000
- **GraphQL Playground:** http://localhost:3000/graphql
- **API Documentation:** http://localhost:3000/api-docs

> To use Safari with Apollo Studio, run this server on HTTPS and use `https://localhost:3000/graphql`.

## 📦 Installation

### Prerequisites

- **Node.js:** Version 18 or higher
- **npm:** Version 8 or higher (comes with Node.js 18+)

### NPM Package
```bash
npm install stock-nse-india
# or
yarn add stock-nse-india
```

### CLI Tool
```bash
npm install -g stock-nse-india
```

### Server Setup
```bash
git clone https://github.com/hi-imcodeman/stock-nse-india.git
cd stock-nse-india
npm install
cp .env.example .env
npm start
```

## 🔌 GraphQL API

The project now includes a powerful GraphQL API for flexible data querying:

### Example Queries

```graphql
# Get equity information
query GetEquity {
  equities(symbolFilter: { in : ["IRCTC","TCS"] }) {
    symbol
    details {
      info {
        companyName
        industry
        isFNOSec
      }
      metadata {
        listingDate
        status
      }
    }
  }
}

# Get indices data
query GetIndices {
  indices(filter: { filterBy: "NIFTY" }) {
    key
    index
    last
    variation
    percentChange
  }
}
```

### GraphQL Schema

The API includes schemas for:
- **Equity** - Stock information, metadata, and details
- **Indices** - Market index data and performance
- **Filters** - Flexible query filtering options

## 🤖 MCP Server

The project includes a Model Context Protocol (MCP) server that allows AI assistants to access NSE India stock market data:

### What is MCP?

Model Context Protocol (MCP) is a standard for AI assistants to communicate with external data sources and tools. This MCP server exposes all NSE India functions as tools that AI models can use.

### Architecture

The MCP implementation is built with a modular architecture for maintainability and consistency:

- **`src/mcp/mcp-tools.ts`**: Common tools configuration and handler functions shared across all implementations
- **`src/mcp/server/mcp-server.ts`**: Stdio-based MCP server for local AI assistant integration
- **`src/mcp/client/mcp-client.ts`**: OpenAI Functions-based MCP client for natural language queries

All components share the same tool definitions and business logic, ensuring consistency and making maintenance easier.

### Benefits of Common Tools Configuration

- **🔄 Consistency**: All server implementations use identical tool definitions and behavior
- **🛠️ Maintainability**: Single source of truth for tool configurations and business logic
- **📝 Easy Updates**: Add new tools or modify existing ones in one place
- **🧪 Testing**: Unified testing approach across all server implementations
- **📚 Documentation**: Centralized tool documentation and examples

### Available Tools

The MCP server provides **30 tools** covering:
- **Equity Data** - Stock details, trade info, corporate info, intraday data, historical data, technical indicators
- **Index Data** - Market indices, intraday data, option chains, contract information
- **Market Data** - Market status, turnover, pre-open data, all indices
- **Reports** - Circulars, daily reports for capital/derivatives/debt markets
- **Commodity Data** - Option chain data for commodities
- **Analysis Tools** - Top gainers/losers, most active equities

### OpenAI Functions MCP Client

The project includes an advanced MCP client that uses OpenAI's native function calling feature for intelligent query processing:

#### Features
- **🤖 Natural Language Processing**: Query data using plain English
- **🔧 Automatic Tool Selection**: AI intelligently chooses the right NSE API tools
- **📊 Real-time Data**: Access live market data, historical information, and more
- **🎯 Smart Parameter Extraction**: Automatically extracts symbols, dates, and other parameters
- **📈 Comprehensive Coverage**: Access to all 30 NSE India API endpoints
- **🔄 Multiple Query Types**: Support for both simple and complex multi-step queries

#### Query Methods
- **`processQuery()`**: Single-round query processing for straightforward requests
- **`processQueryWithMultipleFunctions()`**: Multi-step query processing for complex analysis

#### Example Usage
```javascript
import { mcpClient } from './mcp/client/mcp-client'

// Simple query
const response = await mcpClient.processQuery({
  query: "What is the current price of TCS stock?",
  model: "gpt-4o-mini"
})

// Complex multi-step query
const complexResponse = await mcpClient.processQueryWithMemory({
  query: "Compare the performance of Reliance and TCS over the last month and analyze their trends"
})
```

### Usage

#### Standard I/O (stdio) Server
```bash
# Start the stdio MCP server
npm run start:mcp

# Test the stdio MCP server
npm run test:mcp
```

### Configuration

#### Option 1: Using npx (Recommended for users who have installed the package)

**Installation Steps:**

1. **Prerequisites**: Ensure Node.js 18+ is installed on your system
   ```bash
   node --version  # Should be v18.0.0 or higher
   ```

2. **Install the package** (optional but recommended for faster startup):
   ```bash
   npm install -g stock-nse-india
   ```
   
   **Note**: If you don't install globally, `npx` will automatically download and cache the package on first use, which may take a few moments.

**Configuration:**
```json
{
  "mcpServers": {
    "npx-stock-nse-india": {
      "command": "npx",
      "args": ["stock-nse-india", "mcp"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

#### Option 2: Using local build (For developers with source code)
```json
{
  "mcpServers": {
    "nse-india-stdio": {
      "command": "node",
      "args": ["build/mcp/server/mcp-server-stdio.js"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

#### Configuring in Cursor IDE

1. **Open Cursor Settings**: Press `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux) to open settings
2. **Navigate to MCP Settings**: Go to Settings → Features → Model Context Protocol
3. **Add Server Configuration**: Add either of the configurations above to your MCP settings
4. **Restart Cursor**: Restart Cursor IDE to load the MCP server

Alternatively, you can directly edit the Cursor configuration file:
- **Mac/Linux**: `~/.cursor/mcp.json` or in your workspace settings
- **Windows**: `%APPDATA%\Cursor\mcp.json`

After configuration, the MCP server will be available in Cursor's AI assistant, allowing you to query NSE India stock market data directly from the chat interface.

For detailed MCP documentation, see [MCP_README.md](./MCP_README.md).

## 🌐 REST API

Comprehensive REST endpoints with automatic Swagger documentation:

### Core Endpoints

- `GET /` - Market status
- `GET /api/marketStatus` - Market status information
- `GET /api/glossary` - NSE glossary
- `GET /api/equity/:symbol` - Equity details (uses NSE `quote-equity` when available; otherwise pre-open data enriched from charting/corporate APIs; failures return 403/502 with a message, not an empty 400)
- `GET /api/equity/tradeInfo/:symbol` - Trade info / order book (same `quote-equity` fallback via pre-open when blocked)
- `GET /api/equity/intraday/:symbol` - Intraday chart (`GetQuoteApi` when available; otherwise charting.nseindia.com OHLC)
- `GET /api/equity/:symbol/historical` - Historical data
- `GET /api/indices` - Market indices
- `GET /api/charts/equity-historical-data` - Charting OHLC historical data
- `GET /api/charts/symbol-info` - Charting symbol/token lookup
- `GET /api-docs` - Interactive API documentation

### MCP Client Endpoints

- `POST /api/mcp/query` - Natural language query using OpenAI Functions
- `POST /api/mcp/query-multiple` - Multi-step natural language queries

### API Documentation

Visit `http://localhost:3000/api-docs` for complete interactive API documentation powered by Swagger UI.

### Charting APIs

#### NPM Package Methods

```javascript
import { NseIndia } from "stock-nse-india";

const nseIndia = new NseIndia();

// Optional date range and optional token.
// If token is omitted, it is auto-fetched internally using getEquitySymbolInfo().
const chartData = await nseIndia.getEquityChartHistoricalData(
  "ONGC",
  {
    start: new Date("2026-04-10"),
    end: new Date("2026-04-12")
  }
);

// You can also fetch symbol info/token explicitly.
const symbolInfo = await nseIndia.getEquitySymbolInfo("ONGC");
console.log(symbolInfo.scripcode);
```

#### REST Endpoints

- **`GET /api/charts/equity-historical-data`**
  - Required: `symbol`
  - Optional: `start`, `end` (`YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, or unix timestamp), `token`, `symbolType`, `chartType`, `timeInterval`
  - If `token` is omitted, the API auto-fetches it.
  - If both `start` and `end` are omitted, default range is used.
  - If only one date is provided, the other date is auto-derived.

- **`GET /api/charts/symbol-info`**
  - Required: `symbol`
  - Optional: `segment`
  - Returns charting symbol details including `scripcode` (token).

## 💻 CLI Usage

### Basic Commands

```bash
# Get help
nseindia --help

# Get market status
nseindia

# Get equity details
nseindia equity IRCTC

# Get historical data
nseindia historical IRCTC

# Get indices information
nseindia index

# Get specific index details
nseindia index "NIFTY AUTO"
```

### CLI Features

- **Real-time data** - Live market information
- **Historical analysis** - Historical price data
- **Index tracking** - Market index performance
- **Interactive charts** - ASCII-based data visualization

## 🐳 Docker

### Quick Start

```bash
# Pull and run from Docker Hub
docker run --rm -d -p 3001:3001 imcodeman/nseindia

# Or build locally
docker build -t nseindia . && docker run --rm -d -p 3001:3001 nseindia:latest
```

### Docker Hub

**Image:** `imcodeman/nseindia`  
**Registry:** [Docker Hub](https://hub.docker.com/r/imcodeman/nseindia)

### Container URLs

- **Main App:** http://localhost:3001
- **GraphQL:** http://localhost:3001/graphql
- **API Docs:** http://localhost:3001/api-docs

## ⚙️ Configuration

### Environment Variables

Create your local env file first:

```bash
cp .env.example .env
```

```bash
# Server Configuration
PORT=3000
HOST_URL=http://localhost:3000
NODE_ENV=development
HTTPS_ENABLED=false
SSL_KEY_PATH=./certs/localhost-key.pem
SSL_CERT_PATH=./certs/localhost.pem

# CORS Configuration
CORS_ORIGINS=https://myapp.com,https://admin.myapp.com
CORS_METHODS=GET,POST,OPTIONS
CORS_HEADERS=Content-Type,Authorization,X-Requested-With
CORS_CREDENTIALS=true
```

`HTTPS_ENABLED` decides whether server URLs use `http` or `https`.  
If `HOST_URL` is provided, its protocol part is auto-aligned to `HTTPS_ENABLED`.

### Local HTTPS Setup (Safari + Apollo Studio)

```bash
# Install mkcert once (macOS)
brew install mkcert
mkcert -install

# Create local certs for localhost
mkdir -p certs
mkcert -key-file certs/localhost-key.pem -cert-file certs/localhost.pem localhost 127.0.0.1 ::1

# Enable HTTPS in .env, then start
# HTTPS_ENABLED=true
# HOST_URL=https://localhost:3000
npm start
```

GraphQL endpoint for Apollo Studio:
- `https://localhost:3000/graphql`

### CORS Settings

- **Origins:** Comma-separated list of allowed domains
- **Methods:** HTTP methods (default: GET,POST,PUT,DELETE,OPTIONS)
- **Headers:** Allowed request headers
- **Credentials:** Enable/disable credentials (default: true)
- **Localhost:** Always allowed for development

## 📊 API Methods

### Core Methods

- **`getAllStockSymbols()`** - Get all NSE stock symbols
- **`getData()`** - Generic data retrieval
- **`getDataByEndpoint()`** - Get data by specific NSE API endpoints

### Equity Methods

- **`getEquityDetails(symbol)`** - Get equity information
- **`getEquityHistoricalData(symbol, range)`** - Historical price data
- **`getEquityIntradayData(symbol)`** - Intraday trading data
- **`getEquityOptionChain(symbol)`** - Options chain data
- **`getEquityCorporateInfo(symbol)`** - Corporate information
- **`getEquityTradeInfo(symbol)`** - Trading statistics

### Charting Methods

- **`getEquityChartHistoricalData(symbol, range?, token?, symbolType?, chartType?, timeInterval?)`** - Get charting OHLC historical data
- **`getEquitySymbolInfo(symbol, segment?)`** - Resolve charting symbol/token (`scripcode`)

### Index Methods

- **`getEquityStockIndices()`** - Get all market indices
- **`getIndexIntradayData(index)`** - Index intraday data
- **`getIndexOptionChain(index)`** - Index options data
- **`getIndexOptionChainContractInfo(indexSymbol)`** - Get option chain contract information (expiry dates and strike prices)

### Commodity Methods

- **`getCommodityOptionChain(symbol)`** - Commodity options data

### Helper Methods

- **`getGainersAndLosersByIndex(index)`** - Top gainers and losers
- **`getMostActiveEquities()`** - Most actively traded stocks

## 🏃‍♂️ Development

**⚠️ Prerequisites:** Node.js 18+ required

### Local Development

```bash
# Clone repository
git clone https://github.com/hi-imcodeman/stock-nse-india.git
cd stock-nse-india

# Install dependencies
npm install

# Development mode with auto-reload
npm run start:dev

# Build project
npm run build

# Run tests
npm test

# Generate documentation
npm run docs
```

### Development Scripts

- **`npm start`** - Start production server
- **`npm run start:dev`** - Development mode with auto-reload
- **`npm run build`** - Build TypeScript to JavaScript
- **`npm test`** - Run unit/mock test suite with coverage
- **`npm run test:e2e`** - Run live NSE e2e tests
- **`npm run docs`** - Generate TypeDoc documentation
- **`npm run lint`** - Run ESLint

### MCP Scripts

- **`npm run start:mcp`** - Start stdio MCP server
- **`npm run test:mcp`** - Test stdio MCP server

## 🧪 Testing

```bash
# Run unit/mock tests (default CI)
npm test

# Run tests with coverage
npm test -- --coverage

# Run live NSE e2e tests (requires network; runs daily in CI)
npm run test:e2e

# Run specific test file
npm test -- utils.spec.ts
```

## 📚 Documentation

- **📖 [API Reference](https://hi-imcodeman.github.io/stock-nse-india)** - Complete API documentation
- **🔍 [Examples](https://github.com/hi-imcodeman/stock-nse-india/tree/master/examples)** - Code examples and use cases
- **📋 [Interfaces](https://hi-imcodeman.github.io/stock-nse-india/interfaces/)** - TypeScript interface definitions
- **🏗️ [Modules](https://hi-imcodeman.github.io/stock-nse-india/modules/)** - Module documentation

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines and feel free to submit issues and pull requests.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributors

<a href="https://github.com/hi-imcodeman/stock-nse-india/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=hi-imcodeman/stock-nse-india" />
</a>

## 🔗 Links

- **🌐 Website:** [https://hi-imcodeman.github.io/stock-nse-india](https://hi-imcodeman.github.io/stock-nse-india)
- **📦 NPM:** [https://www.npmjs.com/package/stock-nse-india](https://www.npmjs.com/package/stock-nse-india)
- **🐳 Docker Hub:** [https://hub.docker.com/r/imcodeman/nseindia](https://hub.docker.com/r/imcodeman/nseindia)
- **🐛 Issues:** [https://github.com/hi-imcodeman/stock-nse-india/issues](https://github.com/hi-imcodeman/stock-nse-india/issues)

---

**⭐ Star this repository if you find it helpful!**

### Core Implementation Code & Architecture
#### File: `mcp-config.json`
```python
{
  "mcpServers": {
    "nse-india-stdio": {
      "command": "node",
      "args": ["build/mcp/server/mcp-server-stdio.js"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "npx-stock-nse-india": {
      "command": "npx",
      "args": ["stock-nse-india","mcp"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

#### File: `src/__fixtures__/nse/preopen-tcs-row.json`
```python
{
  "metadata": {
    "symbol": "TCS",
    "identifier": "TCSEQN",
    "series": "EQ",
    "purpose": null,
    "lastPrice": 2308.2,
    "change": 0,
    "pChange": 0,
    "previousClose": 2308.2,
    "finalQuantity": 9395,
    "totalTurnover": 21685539,
    "marketCap": "-",
    "yearHigh": 3545,
    "yearLow": 2206.4,
    "iep": 2308.2,
    "companyName": "Tata Consultancy Services Ltd.",
    "industry": "IT Services",
    "isinCode": "INE467B01029"
  },
  "detail": {
    "preOpenMarket": {
      "preopen": [{ "price": 2308.2, "buyQty": 100, "sellQty": 0, "iep": true }],
      "ato": { "totalBuyQuantity": 0, "totalSellQuantity": 0 },
      "IEP": 2308.2,
      "totalTradedVolume": 1000,
      "finalPrice": 2308.2,
      "finalQuantity": 9395,
      "lastUpdateTime": "26-May-2026 09:00",
      "totalBuyQuantity": 100,
      "totalSellQuantity": 50
    }
  }
}
```

#### File: `src/__fixtures__/nse/quote-equity-tcs.json`
```python
{
  "info": {
    "symbol": "TCS",
    "companyName": "Tata Consultancy Services Ltd.",
    "industry": "IT Services",
    "activeSeries": ["EQ"],
    "debtSeries": [],
    "tempSuspendedSeries": [],
    "isFNOSec": true,
    "isCASec": false,
    "isSLBSec": false,
    "isDebtSec": false,
    "isSuspended": false,
    "isETFSec": false,
    "isDelisted": false,
    "isin": "INE467B01029",
    "slb_isin": "",
    "listingDate": "25-Aug-2004",
    "isMunicipalBond": false,
    "isHybridSymbol": false,
    "segment": "CM",
    "isTop10": false,
    "identifier": "TCSEQN"
  },
  "metadata": {
    "series": "EQ",
    "symbol": "TCS",
    "isin": "INE467B01029",
    "status": "Active",
    "listingDate": "25-Aug-2004",
    "industry": "IT Services",
    "lastUpdateTime": "26-May-2026 15:30:00",
    "pdSectorPe": 22.5,
    "pdSymbolPe": 22.5,
    "pdSectorInd": "NIFTY IT",
    "pdSectorIndAll": ["NIFTY IT"]
  },
  "securityInfo": {
    "boardStatus": "Active",
    "tradingStatus": "Active",
    "tradingSegment": "CM",
    "sessionNo": "1",
    "slb": "No",
    "classOfShare": "Equity",
    "derivatives": "Yes",
    "surveillance": { "surv": null, "desc": null },
    "faceValue": 1,
    "issuedSize": 3619098840
  },
  "sddDetails": { "SDDAuditor": "-", "SDDStatus": "-" },
  "currentMarketType": "NM",
  "priceInfo": {
    "lastPrice": 2308.2,
    "change": -12.5,
    "pChange": -0.54,
    "previousClose": 2320.7,
    "open": 2315,
    "close": 2308.2,
    "vwap": 2310.5,
    "stockIndClosePrice": 0,
    "lowerCP": "2088.6",
    "upperCP": "2552.7",
    "pPriceBand": "No Band",
    "basePrice": 2320.7,
    "intraDayHighLow": { "min": 2300, "max": 2325, "value": 2308.2 },
    "weekHighLow": {
      "min": 2206.4,
      "minDate": "01-Jan-2026",
      "max": 3545,
      "maxDate": "01-Jan-2026",
      "value": 2308.2
    },
    "iNavValue": null,
    "checkINAV": false,
    "tickSize": 0.1,
    "ieq": ""
  },
  "industryInfo": {
    "macro": "Information Technology",
    "sector": "IT Services",
    "industry": "IT Services",
    "basicIndustry": "IT Services"
  },
  "preOpenMarket": {
    "preopen": [],
    "ato": { "buy": 0, "sell": 0 },
    "IEP": 2308.2,
    "totalTradedVolume": 0,
    "finalPrice": 2308.2,
    "finalQuantity": 0,
    "lastUpdateTime": "",
    "totalBuyQuantity": 0,
    "totalSellQuantity": 0,
    "atoBuyQty": 0,
    "atoSellQty": 0
  }
}
```

#### File: `.github/scripts/build_workflow_slack_payload.py`
```python
#!/usr/bin/env python3
"""Build Slack payloads for workflow completion notifications."""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from slack_layout import button, compose, field  # noqa: E402


def main() -> None:
    kind = os.environ.get("NOTIFY_KIND", "workflow")
    repo = os.environ["GITHUB_REPOSITORY"]
    ref = os.environ.get("GITHUB_REF_NAME", "")
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    actor = os.environ.get("GITHUB_ACTOR", "unknown")
    server_url = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    run_id = os.environ["GITHUB_RUN_ID"]
    run_number = os.environ.get("GITHUB_RUN_NUMBER", "")
    run_url = f"{server_url}/{repo}/actions/runs/{run_id}"

    status_emoji = os.environ.get("STATUS_EMOJI", "ℹ️")
    result_emoji = os.environ.get("RESULT_EMOJI", "🟡")
    workflow_result = os.environ.get("WORKFLOW_RESULT", "unknown")
    workflow_name = os.environ.get("WORKFLOW_NAME", os.environ.get("GITHUB_WORKFLOW", "Workflow"))

    header = f"{status_emoji} {workflow_name.upper()}"
    summary = os.environ.get(
        "SUMMARY_LINE",
        f"{result_emoji} *{workflow_result}*",
    )

    accent_colors = {
        "success": "#2eb886",
        "failure": "#e01e5a",
    }
    accent_color = accent_colors.get(workflow_result)

    fields = [
        field("📦 *Repository*", f"`{repo}`"),
        field("🌿 *Ref*", f"`{ref}`"),
        field("🎯 *Event*", f"`{event_name}`"),
        field("👤 *Actor*", f"@{actor}"),
    ]

    buttons = [button("📋 View workflow run", run_url)]

    if kind == "ci":
        sha = os.environ.get("GITHUB_SHA", "")
        commit_url = f"{server_url}/{repo}/commit/{sha}"
        fields.append(field("🔗 *Commit*", f"<{commit_url}|`{sha}`>"))
        buttons.append(button("🔍 View commit", commit_url))
        footer = f"stock-nse-india CI · run #{run_number}"
    else:
        footer = f"{workflow_name} · run #{run_number}"

    # Minimal preview line — full status and details are inside the card.
    text = f"`{repo}@{ref}`"
    body = compose(
        text=text,
        header=header,
        summary=summary,
        fields=fields,
        buttons=buttons,
        footer=footer,
        primary="header",
        accent_color=accent_color,
    )

    out_path = os.environ.get("SLACK_PAYLOAD_PATH", "slack-payload.json")
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(body, handle, ensure_ascii=False)

    print(f"Wrote Slack payload to {out_path}")


if __name__ == "__main__":
    main()
```

#### File: `.github/scripts/slack_layout.py`
```python
"""Shared Slack Block Kit layout helpers for readable vertical spacing."""

from __future__ import annotations

from typing import List, Optional

DIVIDER = {"type": "divider"}


def field(label: str, value: str) -> dict:
    """Label and value with extra line break for readability."""
    return {"type": "mrkdwn", "text": f"{label}\n\n{value}"}


def button(text: str, url: str) -> dict:
    return {
        "type": "button",
        "text": {"type": "plain_text", "text": text, "emoji": True},
        "url": url,
    }


def quote_block(body: str) -> str:
    """Quoted body with padding lines above and below."""
    lines = (body or "").strip().split("\n")
    quoted = "\n".join(f">{line}" if line else ">" for line in lines)
    return f"\n{quoted}\n"


def title_block(text: str) -> dict:
    """Large title block — biggest text size supported by incoming webhooks."""
    return {
        "type": "header",
        "text": {"type": "plain_text", "text": strip_mrkdwn(text)[:150], "emoji": True},
    }


def subtitle_block(text: str) -> dict:
    """Muted secondary line below the title."""
    return {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": text}],
    }


def strip_mrkdwn(text: str) -> str:
    """Remove common mrkdwn markers for plain-text headers."""
    return (text or "").strip().replace("*", "").replace("_", "")


def format_event_header(text: str) -> str:
    """Uppercase event label while preserving a leading emoji."""
    parts = (text or "").strip().split(" ", 1)
    if len(parts) == 2 and not parts[0].isascii():
        return f"{parts[0]} {parts[1].upper()}"
    return text.upper()


def compose(
    text: str,
    header: str,
    summary: Optional[str] = None,
    fields: Optional[List[dict]] = None,
    quote: Optional[str] = None,
    buttons: Optional[List[dict]] = None,
    footer: Optional[str] = None,
    primary: str = "summary",
    accent_color: Optional[str] = None,
) -> dict:
    """Build a Slack message with dividers and two-column fields."""
    blocks: List[dict] = []

    if summary:
        title = header if primary == "header" else summary
        subtitle = summary if primary == "header" else header
        blocks.append(title_block(title))
        blocks.append(subtitle_block(subtitle))
        blocks.append(DIVIDER)
    else:
        blocks.append(title_block(header))
        blocks.append(DIVIDER)

    if quote:
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": quote_block(quote)},
            }
        )
        blocks.append(DIVIDER)

    if fields:
        # Slack renders up to two field items per row.
        # Keep label/value spacing inside each field while using a 2-column layout.
        for i in range(0, len(fields), 2):
            blocks.append({"type": "section", "fields": fields[i : i + 2]})
        blocks.append(DIVIDER)

    if buttons:
        blocks.append({"type": "actions", "elements": buttons})
        blocks.append(DIVIDER)

    if footer:
        blocks.append(
            {
                "type": "context",
                "elements": [{"type": "mrkdwn", "text": footer}],
            }
        )

    while blocks and blocks[-1] == DIVIDER:
        blocks.pop()

    payload: dict = {"text": text, "blocks": blocks}
    if accent_color:
        payload = {
            "text": text,
            "attachments": [{"color": accent_color, "blocks": blocks}],
        }
    return payload
```

#### File: `package.json`
```python
{
  "name": "stock-nse-india",
  "version": "1.4.0",
  "description": "This package will help us to get equity/index details and historical data from National Stock Exchange of India.",
  "main": "build/index.js",
  "browser": false,
  "repository": "https://github.com/hi-imcodeman/stock-nse-india.git",
  "author": "Asraf Ali <asraf.cse@gmail.com>",
  "license": "MIT",
  "bin": {
    "nseindia": "build/cli/index.js"
  },
  "engines": {
    "node": ">=20"
  },
  "scripts": {
    "remove-build": "rimraf ./build",
    "copy-graphql": "copyfiles -f ./src/**/*.graphql build/graphql-schema",
    "prebuild": "yarn remove-build",
    "build": "tsc",
    "postbuild": "yarn copy-graphql",
    "prestart": "yarn build",
    "start": "node build/server.js",
    "prestart:dev": "yarn remove-build",
    "start:dev": "NODE_ENV=development tsc-watch --onCompilationComplete 'yarn copy-graphql' --onSuccess 'node build/server.js'",
    "start:mcp": "node build/mcp/server/mcp-server.js",
    "demo:mcp-client": "node demo/mcp-client-demo.js",
    "demo:memory": "node demo/memory-example.js",
    "docs": "typedoc",
    "test": "jest --coverage --testTimeout=600000 --testPathIgnorePatterns='\\.e2e\\.spec\\.ts$'",
    "test:e2e": "jest --runInBand --testTimeout=600000 --testPathPattern='\\.e2e\\.spec\\.ts$'",
    "lint": "eslint ./src/**/*.ts",
    "gpr-setup": "node ./scripts/setup-gpr.js",
    "prepare": "husky install"
  },
  "lint-staged": {
    "src/**/*.{ts,tsx,js,jsx}": [
      "yarn lint --fix",
      "git add"
    ]
  },
  "prepare": "husky install",
  "devDependencies": {
    "@types/express": "^4.17.17",
    "@types/jest": "^29.5.0",
    "@types/node": "^18.15.0",
    "@types/swagger-jsdoc": "^6.0.1",
    "@types/swagger-ui-express": "^4.1.6",
    "@types/tough-cookie": "^4.0.5",
    "@types/user-agents": "^1.0.4",
    "@typescript-eslint/eslint-plugin": "^5.57.0",
    "@typescript-eslint/parser": "^5.57.0",
    "copyfiles": "^2.4.1",
    "eslint": "^8.38.0",
    "husky": "^8.0.3",
    "jest": "^29.5.0",
    "lint-staged": "^13.2.0",
    "rimraf": "^5.0.0",
    "ts-jest": "^29.1.0",
    "tsc-watch": "^6.0.4",
    "typedoc": "^0.24.8",
    "typescript": "^4.9.5"
  },
  "dependencies": {
    "@graphql-tools/graphql-file-loader": "^7.5.13",
    "@graphql-tools/load": "^7.8.8",
    "@graphql-tools/load-files": "^6.6.1",
    "@graphql-tools/merge": "^8.3.14",
    "@modelcontextprotocol/sdk": "^1.17.5",
    "@types/cors": "^2.8.17",
    "apollo-server-core": "^3.10.0",
    "apollo-server-express": "^3.10.0",
    "asciichart": "^1.5.25",
    "axios": "^1.4.0",
    "axios-cookiejar-support": "^5.0.5",
    "chalk": "^4.1.2",
    "cheerio": "1.0.0-rc.10",
    "cors": "^2.8.5",
    "dotenv": "^17.4.2",
    "express": "^4.18.2",
    "graphql": "^16.6.0",
    "indicatorts": "^2.2.2",
    "mcp-remote": "^0.1.27",
    "moment": "^2.29.4",
    "moment-range": "^4.0.2",
    "ohlc": "^2.0.4",
    "openai": "^4.20.1",
    "ora": "^5.4.1",
    "swagger-jsdoc": "^6.2.8",
    "swagger-ui-express": "^4.6.3",
    "tough-cookie": "^5.1.2",
    "user-agents": "^1.0.104",
    "yargs": "^17.7.2"
  },
  "keywords": [
    "nse",
    "nseindia",
    "nse-india",
    "national-stock-exchange",
    "stock-market",
    "stock-exchange",
    "indian-stock-market",
    "equity",
    "shares",
    "stocks",
    "indices",
    "nifty",
    "sensex",
    "stock-data",
    "market-data",
    "historical-data",
    "intraday-data",
    "option-chain",
    "technical-indicators",
    "api",
    "rest-api",
    "graphql",
    "graphql-api",
    "mcp",
    "model-context-protocol",
    "mcp-server",
    "mcp-client",
    "openai",
    "ai-assistant",
    "cli",
    "command-line",
    "typescript",
    "nodejs",
    "express",
    "apollo-server",
    "swagger",
    "india",
    "bse",
    "nse-api",
    "stock-market-api",
    "financial-data",
    "trading",
    "investment"
  ],
  "bugs": {
    "url": "https://github.com/hi-imcodeman/stock-nse-india/issues"
  },
  "homepage": "https://hi-imcodeman.github.io/stock-nse-india"
}
```


==================================================


## [2/3] Repository: NSE (`VAULT_IN-QUANT-074_paragjp__NSE`)
- **Full Name**: `IN-QUANT-074_paragjp__NSE`
- **Description**: NSE is a rust cli binary and library for extracting real-time data from National Stock Exchange (India)
- **GitHub Stars**: 24
- **Source Pool**: `indian_quant_vault`

### Core Implementation Code & Architecture
#### File: `scripts/test1.py`
```python
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
```

#### File: `scripts/archives/daily_oi.py`
```python
from write_calls_oi     import write_calls_oi
from write_put_oi       import write_put_oi


write_calls_oi()
write_put_oi()
```

#### File: `scripts/archives/myround.py`
```python
def myround(f_basestrike, base):
    f_order_strike = f_basestrike
    f_base = base
    return(f_base * round(f_order_strike/f_base))
```

#### File: `scripts/myround.py`
```python
import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', 51)

def myround(x, base=5):
    return int(base * round(float(x) / base))
```

#### File: `scripts/archives/calculate_change.py`
```python
def calculate_change(f_basestrike, f_current_nifty, ):
    if f_basestrike >= f_current_nifty:
       f_current_change = round(float(f_basestrike) - float(f_current_nifty),2)
    else:
        f_current_change = round( float(f_current_nifty)- float(f_basestrike) , 2)
    return(f_current_change)
```

#### File: `scripts/disp_message.py`
```python
from tkinter import *
from tkinter import messagebox

def disp_message(msg,msgtype):
    top = Tk()
    top.withdraw()
    if msgtype==1:
        messagebox.showwarning("Warning",msg)
    elif msgtype==2:
         messagebox.showinfo("information",msg)
    else:
        messagebox.showerror("Error",msg)
```


==================================================


## [3/3] Repository: Algorithmic-Trading-Strategies-Python (`WHEEL_Algorithmic-Trading-Strategies-Python`)
- **Full Name**: `Algorithmic-Trading-Strategies-Python`
- **Description**: Algorithmic Trading Stratagies for stocks listed on National Stock Exchange India(NSE -India) with buy and sell logic
- **GitHub Stars**: 13
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Algorithmic-Trading-Strategies-Python
Different Algorithmic Trading Stratagies for stocks listed on National Stock Exchange India(NSE -India) with buy and sell logic


# What is Algorithmic Trading?
Computers can offer multiple advantages over human traders. For one, they can stay active all day, every day without sleep. They can also analyze data precisely and respond to changes in milliseconds. To top it off, they never factor emotion into their decisions. Because of this, many investors have long since realized that machines can make excellent traders, given that they are using the correct strategies. 
Its how the field of algorithmic trading has evolved. While it began with computers trading in traditional markets, the rise of digital assets and 24/7 exchanges has brought this practice to a new level.


# What are some of the strategies?
• Dual Moving Averages Crossover

• Three Moving Averages

• MACD Crossover

### Core Implementation Code & Architecture
#### File: `MACD-Crossover/main.py`
```python
!pip install nsepy

#Import the libraries
import pandas as pd
import numpy as np
from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Taking Input
stname = input("Enter stock symbol : ")

#Fetch the data
#stock = get_history(symbol= stname, start=date(2018,7,12), end=date(2020,7,12))
#stock.reset_index()

#Was unable to fetch the data

#Load the data 
from google.colab import files
uploaded = files.upload() #upload a csv file

for fn in uploaded.keys():
  print('Uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  File = fn

# Store the data
stock = pd.read_csv(File)

#Set the index
stock = stock.set_index(pd.DatetimeIndex(stock['Date'].values))
StartDate = stock.iat[0,2]
EndDate = stock.iat[-1,2]

#Show the data
stock

#Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(stock['Close Price'],label = stname, linewidth=2)
plt.title(stname + ' Close Price History')
plt.xlabel(StartDate + ' to ' + EndDate)
plt.ylabel('Close Price INR (₹)')
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 0.5))
plt.show()

#Calculate the MACD and single line indicator
#Calculate the short term exponential moving average (EMA)
ShortEMA = stock['Close Price'].ewm(span=12, adjust=False).mean()
#Calculate the long term exponential moving average (EMA)
LongEMA = stock['Close Price'].ewm(span=26, adjust=False).mean()
#Calculate the MACD line
MACD = ShortEMA - LongEMA
#Calculate the signal line
signal = MACD.ewm(span=9, adjust=False).mean()

#Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(stock.index, MACD, label = stname + ' MACD', linewidth=1)
plt.plot(stock.index, signal, label = 'Signal Line', linewidth=1)
plt.title(stname + ' Indicators')
plt.xlabel(StartDate + ' to ' + EndDate)
plt.ylabel('Close Price INR (₹)')
plt.legend(loc='upper right', bbox_to_anchor=(1.175, 0.6))
plt.show()

#Create new coulmns to store all the data
stock['MACD'] = MACD
stock['Signal Line'] = signal
stock

#Create a function to signal when to buy and sell the asset/stock
def buy_sell(signal):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(0, len(signal)):
    if signal['MACD'][i] > signal['Signal Line'][i]:
      sigPriceSell.append(np.nan)
      if flag != 1:
        sigPriceBuy.append(signal['Close Price'][i])
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
    elif signal['MACD'][i] < signal['Signal Line'][i]:
      sigPriceBuy.append(np.nan)
      if flag != 0:
        sigPriceSell.append(signal['Close Price'][i])
        flag = 0
      else:
        sigPriceSell.append(np.nan)
    else:
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan) 

  return (sigPriceBuy, sigPriceSell)

#Store the buy and sell stock into a variable
buy_sell = buy_sell(stock)
stock['Buy_Signal_Price'] = buy_sell[0]
stock['Sell_Signal_Price'] = buy_sell[1]

#show the data
stock

#Visualize the stock
plt.figure(figsize=(13,5.2))
plt.plot(stock['Close Price'],label = stname, alpha = 0.45, linewidth=1)
plt.scatter(stock.index, stock['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(stock.index, stock['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title(stname + ' Close Price History with Buy & Sell Signal')
plt.xlabel(StartDate + ' to ' + EndDate)
plt.ylabel('Close Price INR (₹)')
plt.legend(loc='upper right', bbox_to_anchor=(1.125, 0.6))
plt.show()
```

#### File: `Dual-Moving-Average-Crossover-Stratagy-NSE/main.py`
```python
!pip install nsepy

#Import the libraries
import pandas as pd
import numpy as np
from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Taking Input
stname = input("Enter stock symbol : ")

#Fetch the data
#data = get_history(symbol= stname, start=date(2018,7,12), end=date(2020,7,12))
#data.reset_index()

#Was unable to fetch the data

#Load the data 
from google.colab import files
uploaded = files.upload() #upload a csv file

for fn in uploaded.keys():
  print('Uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  File = fn

# Store the data
stock = pd.read_csv(File)

#Set the index
stock = stock.set_index(pd.DatetimeIndex(stock['Date'].values))
StartDate = stock.iat[0,2]
EndDate = stock.iat[-1,2]

#Show the Data
stock

#Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(stock['Close Price'],label = stname)
plt.title(stname + ' Close Price History')
plt.xlabel(StartDate + ' to ' + EndDate)
plt.ylabel('Close Price INR (₹)')
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 0.5))
plt.show()

# Creating a simple moving averag for 30 days
SMA30 = pd.DataFrame()
SMA30['Close Price'] = stock['Close Price'].rolling(window=30).mean()
SMA30

# Creating a simple moving averag for 100 days
SMA100 = pd.DataFrame()
SMA100['Close Price'] = stock['Close Price'].rolling(window=100).mean()
SMA100

#Visualize the data
plt.figure(figsize=(12.5,4.5))
plt.plot(stock['Close Price'],label = stname)
plt.plot(SMA30['Close Price'],label = 'SMA30')
plt.plot(SMA100['Close Price'],label = 'SMA100')
plt.title(stname + ' Close Price History')
plt.xlabel(StartDate + ' to ' + EndDate)
plt.ylabel('Close Price INR (₹)')
plt.legend(loc='upper right', bbox_to_anchor=(1.125, 0.6))
plt.show()

#Create a new data frame to store all the data
data= pd.DataFrame()
data['stock'] = stock['Close Price']
data['SMA30'] = SMA30['Close Price']
data['SMA100'] = SMA100['Close Price']
data

#Create a function to signal when to buy and sell the asset/stock
def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(len(data)):
    if data['SMA30'][i] > data['SMA100'][i]:
      if flag != 1:
        sigPriceBuy.append(data['stock'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['stock'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan) 

  return (sigPriceBuy, sigPriceSell)

#Store the buy and sell data into a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#show the data
data

#Visualize the data
plt.figure(figsize=(13,5.2))
plt.plot(stock['Close Price'],label = stname, alpha = 0.45)
plt.plot(data['SMA30'],label = 'SMA30', alpha = 0.45)
plt.plot(data['SMA100'],label = 'SMA100', alpha = 0.45)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red')
plt.title(stname + ' Close Price History with Buy & Sell Signal')
plt.xlabel(StartDate + ' to ' + EndDate)
plt.ylabel('Close Price INR (₹)')
plt.legend(loc='upper right', bbox_to_anchor=(1.125, 0.6))
plt.show()
```


==================================================
