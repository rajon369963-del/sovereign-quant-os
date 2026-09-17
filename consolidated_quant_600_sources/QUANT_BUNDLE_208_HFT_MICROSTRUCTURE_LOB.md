# ⚡ [QUANT-SOURCE-208] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_208_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: crypto-ai-trading-bot (`PHASE4-QUANT-059`)
- **Full Name**: `PHASE4-QUANT-059_bigmacman1129__crypto-ai-trading-bot`
- **Description**: Crypto liquidity detection & algorithmic trading bot. Order book analysis, stop-loss clusters, liquidity sweeps. Multi-exchange (Binance, Bybit, Kraken, OKX). Trading signals, quant research, market microstructure.
- **GitHub Stars**: 221
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Crypto Liquidity Trading Bot

Self-hosted **market-making, liquidity-signal, and arbitrage** bot for crypto spot markets. It watches the order book, posts inventory-aware quotes, and scans for cross-exchange and triangular edges.

The runtime is **Node.js** (not Python). Control it with ADAMANT messenger commands, optional Telegram/CLI, and a local health API.

[![Node](https://img.shields.io/badge/node-%3E%3D18.18-blue.svg)](https://nodejs.org/) [![License](https://img.shields.io/badge/license-GPL--3.0-green.svg)](LICENSE)

![Crypto Liquidity Trading Bot](assets/image.png)

<details>
<summary><strong>📋 Table of contents</strong></summary>

- [Why liquidity matters](#why-liquidity-matters)
- [Who this is for](#who-this-is-for)
- [Commercial use](#commercial-use)
- [Strategy concept](#strategy-concept)
- [Architecture](#architecture)
- [New in 7.1](#new-in-71)
- [Quick start](#quick-start)
- [What you get](#what-you-get)
- [How liquidity hunting works](#how-liquidity-hunting-works)
- [Installation](#installation)
- [Supported exchanges](#supported-exchanges)
- [Project layout](#project-layout)
- [Use cases](#use-cases)
- [Related projects](#related-projects)
- [FAQ](#faq)
- [Contributing](#contributing)

</details>

---

## Why liquidity matters

Most crypto trading bots rely only on **price and technical indicators**. Professional traders, however, monitor **order book liquidity**, because price often moves toward zones where liquidity is concentrated—and away when that liquidity is swept.

This project focuses on **liquidity-aware trading signals** instead of lagging indicators: it detects gaps, walls, and sweeps so you can act on structure, not just price.

---

## Who this is for

This project may be useful for:

- **Crypto trading firms** building in-house liquidity and execution tools  
- **Quant researchers** studying order book and market microstructure  
- **Exchanges** building surveillance or liquidity analytics  
- **Developers** building AI trading agents or signal systems  

---

## Commercial use

If you are interested in **custom crypto trading bots** (liquidity, arbitrage, execution), **AI trading signal systems**, or **liquidity detection algorithms** and exchange API integrations:

**For collaboration or development work:**

- **Telegram** — [@k02_xx](https://t.me/k02_xx)

---

## New in 7.1

Classic wash-volume market-making is still here. On top of it:

| Engine | What it does | How to start |
|---|---|---|
| **Smart quoter** | Avellaneda–Stoikov style two-sided quotes: spread from realized vol, skew from inventory | `/start mm smart` or `/enable smart 0.2%` |
| **Arbitrage** | Cross-exchange bid/ask scanner + triangular cycles on the home venue | `/enable arb scan` (default), `paper`, or `live -y` |
| **Signals** | Order-book imbalance, walls, gaps, liquidity sweeps | On by default; `/signals` |
| **Risk** | Max order, inventory, open notional, daily loss halt | `config.jsonc` → `risk`; `/risk` |

Live arbitrage is **opt-in**. Scan mode only alerts. Cross-exchange live legs need API keys on **both** venues (`arbitrage.accounts` plus the home account). REST latency and fees often consume small edges — treat live mode as experimental.

---

## Backtest performance

This release does **not** ship a verified historical backtest. Paper-trade `/enable arb paper` and `/start mm smart` on your pair before any live size. Live results depend on fees, delay, inventory, and venue quality.

Example signal:

```json
{
  "symbol": "ADM/USDT",
  "direction": "LONG",
  "strength": 0.61,
  "reason": "liquidity_sweep_detected",
  "ts": "2026-08-25T01:00:00Z"
}
```

---
## Strategy concept

**Price indicators lag. Liquidity moves first.**

Large orders and stop-loss clusters sit in the order book before price reaches them. When price sweeps those levels, liquidity is consumed and moves tend to accelerate. This bot identifies those levels and signals sweep events so you can trade with the flow instead of chasing price.

---

## Architecture

```
Exchange public/private APIs
        ↓
Order-book analytics (microprice, imbalance, walls, gaps)
        ↓
   ┌────┴────┬────────────┬──────────────┐
   ↓         ↓            ↓              ↓
Smart     Volume MM    Arb scanner    Signal engine
quoter    (optional)   (cross + tri)  (alerts)
   ↓         ↓            ↓
Risk manager (inventory / daily loss / order caps)
        ↓
ADAMANT / Slack / Discord /health /status
```

Core paths:

- `app.js` — boot, MongoDB, engines
- `trade/engines/` — pure math (quotes, arb, risk, book analytics)
- `trade/mm_*.js` — live loops
- `modules/commandTxs.js` — chat commands
- `trade/trader_*.js` — exchange adapters

---

## Quick start

### Quick start (Node)

```bash
git clone https://github.com/asonglin/crypto-liquidity-ai-trading-bot.git && cd crypto-liquidity-ai-trading-bot
npm install
cp config.default.jsonc config.jsonc
# set exchange keys, pair, and (optionally) ADAMANT passPhrase
node app.js
```

Then in chat:

```
/start mm smart
/enable arb scan
/signals
/arb
/risk
```

---

## What you get

| Capability | Description |
|------------|-------------|
| **Liquidity detection** | Scans order books and pools for depth, gaps, and imbalance. |
| **Hidden walls** | Surfaces large buy/sell walls and their changes. |
| **Multi-exchange** | Built to plug into Binance, Bybit, Kraken, OKX, and others. |
| **Alerts** | Configurable notifications when liquidity events fire. |
| **Trading framework** | Modular so you can add execution, risk, or dashboards. |

Use it for **liquidity grabs**, **order book imbalance strategies**, **market microstructure research**, and **algorithmic trading**—whether you trade manually or automate.

---

## How liquidity hunting works

Liquidity hunting targets zones where lots of orders sit (e.g. stop-loss clusters). When price sweeps those levels, liquidity is “taken” and price can move fast. This bot helps you find and watch those zones.

1. **Find** where large stop-loss clusters or thin book zones sit.  
2. **Detect** liquidity sweeps and wall removals in real time.  
3. **Alert** so you can enter when liquidity is taken or book vacuum appears.  
4. **Extend** with your own execution (manual or automated).

Signals you can get: *stop-loss clusters*, *sudden order book vacuum*, *liquidity wall removal*, *aggressive market order flow*.

---

## Installation

```bash
git clone https://github.com/asonglin/crypto-liquidity-ai-trading-bot.git
cd crypto-liquidity-ai-trading-bot
```

**Quick start (Node)** — main engine:

```bash
npm install
cp config.default.jsonc config.jsonc
# Edit config.jsonc, then:
node app.js
```

Then: `/start mm smart`, `/enable arb scan`, `/signals`.

---
## Production hardening checklist

- Keep `api.host` set to `127.0.0.1` unless you explicitly front the API with a trusted reverse proxy.
- Keep `api.debug` disabled in production; if enabled, configure `api.debugToken` and `api.debugAllowlist`.
- Prefer env vars for secrets (`BOT_PASSPHRASE`, `EXCHANGE_API_KEY`, `EXCHANGE_API_SECRET`) over plain config values.
- Never commit `config.jsonc` or `.env` with real credentials.

---

## Container deployment

Build and run with Docker Compose:

```bash
cp .env.example .env
cp config.default.jsonc config.jsonc
docker compose up --build -d
```

The compose stack starts:
- `bot` (this project)
- `mongo` (MongoDB 7)

---

## Supported exchanges

Adapters in this repo (spot):

| Exchange | Module |
|----------|--------|
| Azbit | `trader_azbit.js` |
| P2PB2B | `trader_p2pb2b.js` |
| StakeCube | `trader_stakecube.js` |
| Coinstore | `trader_coinstore.js` |
| FameEX | `trader_fameex.js` |
| NonKYC | `trader_nonkyc.js` |
| XeggeX | `trader_xeggex.js` |

The arb scanner uses public tickers on every name listed in `config.exchanges`. Live execution uses the home `exchange` keys, plus optional `arbitrage.accounts` for a second venue.

---

## Project layout

```
crypto-liquidity-ai-trading-bot/
├── app.js                 # entry point
├── config.default.jsonc   # config template
├── package.json
├── helpers/               # shared utils
├── modules/               # api, DB, config, commands
├── routes/                # /ping, /status, debug
├── trade/
│   ├── engines/           # analytics, quotes, arb math, risk
│   ├── mm_smart_quoter.js
│   ├── mm_arbitrage.js
│   ├── mm_signal_engine.js
│   ├── mm_trader.js       # volume MM (optional)
│   └── trader_*.js        # exchange adapters
├── tests/unit/
└── assets/
```

---

## Use cases

- **Crypto algorithmic trading** — Feed signals into your execution engine.  
- **Quant research** — Order book and liquidity analysis.  
- **AI/ML strategy dev** — Use liquidity events as features or triggers.  
- **Market microstructure** — Study gaps, walls, and sweep behavior.

---


## FAQ

**What is liquidity hunting?**  
A strategy that focuses on levels where lots of stop-loss or passive orders sit; when those levels are hit, liquidity is consumed and price often moves sharply.

**Is the bot fully automated?**  
Volume MM, smart quoting, and live arb can place orders. Arb defaults to **scan** (alerts only). Smart quotes need `/enable smart` or `/start mm smart`.

**Who is it for?**  
Token issuers and traders who want self-hosted market-making, microstructure signals, and a conservative arb scanner on the supported CEX adapters.

---

## Contributing

We welcome pull requests and issues. Fork → branch → PR. See CONTRIBUTING.md if present.

**License:** MIT © 2026

### Core Implementation Code & Architecture
#### File: `babel.config.json`
```python
{
  "presets": ["@babel/preset-env"],
  "plugins": [
      ["@babel/transform-runtime"]
  ]
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2017",
    "module": "commonjs",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

#### File: `jsconfig.json`
```python
{
  "compilerOptions": {
    "allowJs": true,
    "checkJs": true,
    "lib": [
      "es5", "es6", "dom", "dom.iterable"
    ],
    "module": "Node16",
    "moduleResolution": "Node16",
    "paths": {
      "types/*": ["./types/*"]
    },
    "target": "ES6"
  },
  "exclude": ["node_modules"],
  "include": ["**/*.js"]
}
```

#### File: `package.json`
```python
{
  "name": "adamant-tradebot",
  "version": "7.1.0",
  "description": "Self-hosted crypto market-making bot with inventory-aware quoting, liquidity signals, and cross-exchange / triangular arbitrage.",
  "main": "index.js",
  "scripts": {
    "lint": "npx eslint -f visualstudio .",
    "lint:fix": "npx eslint -f visualstudio --fix",
    "lint:fixrule": "npx eslint -f visualstudio --no-eslintrc --fix --env node,es2021,commonjs --parser-options=ecmaVersion:12 --rule",
    "start": "node app.js",
    "start:dev": "node app.js dev",
    "clear": "node app.js dev clear_db",
    "test": "jest --testPathIgnorePatterns=trade/tests/manual.test.js"
  },
  "keywords": [
    "market-making",
    "market making",
    "trading bot",
    "self-hosted",
    "trading volume",
    "bot",
    "bitcoin",
    "ethereum",
    "trading",
    "trade",
    "order book",
    "orderbook",
    "exchange",
    "arbitrage",
    "crypto",
    "cryptocurrency",
    "spread",
    "liquidity",
    "target price",
    "price watching",
    "making price"
  ],
  "author": "ADAMANT Developer Community <devs@adamant.im> (https://adamant.im)",
  "license": "GPL-3.0",
  "dependencies": {
    "@babel/runtime": "^7.29.2",
    "adamant-api": "^2.4.0",
    "axios": "^1.11.0",
    "deep-object-diff": "^1.1.9",
    "express": "^4.21.2",
    "fast-deep-equal": "^3.1.3",
    "form-data": "^4.0.4",
    "jsonminify": "^0.4.2",
    "mongodb": "^6.19.0",
    "uuid": "^12.0.0"
  },
  "devDependencies": {
    "@babel/core": "^7.28.4",
    "@babel/eslint-parser": "^7.28.4",
    "@babel/plugin-transform-runtime": "^7.28.3",
    "@babel/preset-env": "^7.28.3",
    "@eslint/js": "^9.35.0",
    "eslint": "^9.35.0",
    "eslint-config-google": "^0.14.0",
    "eslint-formatter-visualstudio": "^8.40.0",
    "globals": "^16.3.0",
    "jest": "^30.1.3",
    "nodemon": "^3.1.10"
  },
  "engines": {
    "node": ">=18.18",
    "npm": ">=9.0.1"
  },
  "publishConfig": {
    "access": "public"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Adamant-im/adamant-tradebot.git"
  },
  "bugs": {
    "url": "https://github.com/Adamant-im/adamant-tradebot/issues"
  },
  "homepage": "https://marketmaking.app"
}
```

#### File: `package-lock.json`
```python
{
  "name": "adamant-tradebot",
  "version": "7.1.0",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "adamant-tradebot",
      "version": "7.1.0",
      "license": "GPL-3.0",
      "dependencies": {
        "@babel/runtime": "^7.29.2",
        "adamant-api": "^2.4.0",
        "axios": "^1.11.0",
        "deep-object-diff": "^1.1.9",
        "express": "^4.21.2",
        "fast-deep-equal": "^3.1.3",
        "form-data": "^4.0.4",
        "jsonminify": "^0.4.2",
        "mongodb": "^6.19.0",
        "uuid": "^12.0.0"
      },
      "devDependencies": {
        "@babel/core": "^7.28.4",
        "@babel/eslint-parser": "^7.28.4",
        "@babel/plugin-transform-runtime": "^7.28.3",
        "@babel/preset-env": "^7.28.3",
        "@eslint/js": "^9.35.0",
        "eslint": "^9.35.0",
        "eslint-config-google": "^0.14.0",
        "eslint-formatter-visualstudio": "^8.40.0",
        "globals": "^16.3.0",
        "jest": "^30.1.3",
        "nodemon": "^3.1.10"
      },
      "engines": {
        "node": ">=18.18",
        "npm": ">=9.0.1"
      }
    },
    "node_modules/@aashutoshrathi/word-wrap": {
      "version": "1.2.6",
      "resolved": "https://registry.npmjs.org/@aashutoshrathi/word-wrap/-/word-wrap-1.2.6.tgz",
      "integrity": "sha512-1Yjs2SvM8TflER/OD3cOjhWWOZb58A2t7wpE2S9XfBYTiIl+XFhQG2bjy4Pu1I+EAlCNUzRDYDdFwFYUKvXcIA==",
      "dev": true,
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.27.1.tgz",
      "integrity": "sha512-cjQ7ZlQ0Mv3b47hABuTevyTuYN4i+loJKGeV9flcCgIK37cCXRh+L1bd3iBHlynerhQ7BhCkn2BPbQUL+rGqFg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.27.1",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.28.4.tgz",
      "integrity": "sha512-YsmSKC29MJwf0gF8Rjjrg5LQCmyh+j/nD8/eP7f+BeoQTKYqs9RoWbjGOdy0+1Ekr68RJZMUOPVQaQisnIo4Rw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.28.4.tgz",
      "integrity": "sha512-2BCOP7TN8M+gVDj7/ht3hsaO/B/n5oDbiAyyvnRlNOs+u1o+JWNYTQrmpuNp1/Wq2gcFrI01JAW+paEKDMx/CA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.27.1",
        "@babel/generator": "^7.28.3",
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-module-transforms": "^7.28.3",
        "@babel/helpers": "^7.28.4",
        "@babel/parser": "^7.28.4",
        "@babel/template": "^7.27.2",
        "@babel/traverse": "^7.28.4",
        "@babel/types": "^7.28.4",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/eslint-parser": {
      "version": "7.28.4",
      "resolved": "https://registry.npmjs.org/@babel/eslint-parser/-/eslint-parser-7.28.4.tgz",
      "integrity": "sha512-Aa+yDiH87980jR6zvRfFuCR1+dLb00vBydhTL+zI992Rz/wQhSvuxjmOOuJOgO3XmakO6RykRGD2S1mq1AtgHA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@nicolo-ribaudo/eslint-scope-5-internals": "5.1.1-v1",
        "eslint-visitor-keys": "^2.1.0",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": "^10.13.0 || ^12.13.0 || >=14.0.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.11.0",
        "eslint": "^7.5.0 || ^8.0.0 || ^9.0.0"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.28.3.tgz",
      "integrity": "sha512-3lSpxGgvnmZznmBkCRnVREPUFJv2wrv9iAoFDvADJc0ypmdOxdUtcLeBgBJ6zE0PMeTKnxeQzyk0xTBq4Ep7zw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.28.3",
        "@babel/types": "^7.28.2",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-annotate-as-pure": {
      "version": "7.27.3",
      "resolved": "https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.27.3.tgz",
      "integrity": "sha512-fXSwMQqitTGeHLBC08Eq5yXz2m37E4pJX1qAU1+2cNedz/ifv/bVXft90VeSav5nFO61EcNgwr0aJxbyPaWBPg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.27.3"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.27.2",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.27.2.tgz",
      "integrity": "sha512-2+1thGUUWWjLTYTHZWK1n8Yga0ijBz1XAhUXcKy81rd5g6yh7hGqMp45v7cadSbEHc9G3OTv45SyneRN3ps4DQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.27.2",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-create-class-features-plugin": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/helper-create-class-features-plugin/-/helper-create-class-features-plugin-7.28.3.tgz",
      "integrity": "sha512-V9f6ZFIYSLNEbuGA/92uOvYsGCJNsuA8ESZ4ldc09bWk/j8H8TKiPw8Mk1eG6olpnO0ALHJmYfZvF4MEE4gajg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-annotate-as-pure": "^7.27.3",
        "@babel/helper-member-expression-to-functions": "^7.27.1",
        "@babel/helper-optimise-call-expression": "^7.27.1",
        "@babel/helper-replace-supers": "^7.27.1",
        "@babel/helper-skip-transparent-expression-wrappers": "^7.27.1",
        "@babel/traverse": "^7.28.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-create-regexp-features-plugin": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.27.1.tgz",
      "integrity": "sha512-uVDC72XVf8UbrH5qQTc18Agb8emwjTiZrQE11Nv3CuBEZmVvTwwE9CBUEvHku06gQCAyYf8Nv6ja1IN+6LMbxQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-annotate-as-pure": "^7.27.1",
        "regexpu-core": "^6.2.0",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-define-polyfill-provider": {
      "version": "0.6.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-define-polyfill-provider/-/helper-define-polyfill-provider-0.6.5.tgz",
      "integrity": "sha512-uJnGFcPsWQK8fvjgGP5LZUZZsYGIoPeRjSF5PGwrelYgq7Q15/Ft9NGFp1zglwgIv//W0uG4BevRuSJRyylZPg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-compilation-targets": "^7.27.2",
        "@babel/helper-plugin-utils": "^7.27.1",
        "debug": "^4.4.1",
        "lodash.debounce": "^4.0.8",
        "resolve": "^1.22.10"
      },
      "peerDependencies": {
        "@babel/core": "^7.4.0 || ^8.0.0-0 <8.0.0"
      }
    },
    "node_modules/@babel/helper-define-polyfill-provider/node_modules/debug": {
      "version": "4.4.1",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.1.tgz",
      "integrity": "sha512-KcKCqiftBJcZr++7ykoDIEwSa3XWowTfNPo92BYxjXiyYEVrUQh2aLyhxBCwww+heortUFxEJYcRzosstTEBYQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-member-expression-to-functions": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.27.1.tgz",
      "integrity": "sha512-E5chM8eWjTp/aNoVpcbfM7mLxu9XGLWYise2eBKGQomAk/Mb4XoxyqXTZbuTohbsl8EKqdlMhnDI2CCLfcs9wA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.27.1.tgz",
      "integrity": "sha512-0gSFWUPNXNopqtIPQvlD5WgXYI5GY2kP2cCvoT8kczjbfcfuIljTbcWrulD1CIPIX2gt1wghbDy08yE1p+/r3w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.3",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.3.tgz",
      "integrity": "sha512-gytXUbs8k2sXS9PnQptz5o0QnpLL51SwASIORY6XaBKF88nsOT0Zw9szLqlSGQDP/4TljBAD5y98p2U1fqkdsw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.27.1",
        "@babel/traverse": "^7.28.3"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-optimise-call-expression": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.27.1.tgz",
      "integrity": "sha512-URMGH08NzYFhubNSGJrpUEphGKQwMQYBySzat5cAByY1/YgIRkULnIy3tAMeszlL/so2HbeilYloUmSpd7GdVw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.27.1.tgz",
      "integrity": "sha512-1gn1Up5YXka3YYAHGKpbideQ5Yjf1tDa9qYcgysz+cNCXukyLl6DjPXhD3VRwSb8c0J9tA4b2+rHEZtc6R0tlw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-remap-async-to-generator": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.27.1.tgz",
      "integrity": "sha512-7fiA521aVw8lSPeI4ZOD3vRFkoqkJcS+z4hFo82bFSH/2tNd6eJ5qCVMS5OzDmZh/kaHQeBaeyxK6wljcPtveA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-annotate-as-pure": "^7.27.1",
        "@babel/helper-wrap-function": "^7.27.1",
        "@babel/traverse": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-replace-supers": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.27.1.tgz",
      "integrity": "sha512-7EHz6qDZc8RYS5ElPoShMheWvEgERonFCs7IAonWLLUTXW59DP14bCZt89/GKyreYn8g3S83m21FelHKbeDCKA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-member-expression-to-functions": "^7.27.1",
        "@babel/helper-optimise-call-expression": "^7.27.1",
        "@babel/traverse": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-skip-transparent-expression-wrappers": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-skip-transparent-expression-wrappers/-/helper-skip-transparent-expression-wrappers-7.27.1.tgz",
      "integrity": "sha512-Tub4ZKEXqbPjXgWLl2+3JpQAYBJ8+ikpQ2Ocj/q/r0LwE3UhENh7EUabyHjz2kCEsrRY83ew2DQdHluuiDQFzg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.27.1",
        "@babel/types": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.27.1.tgz",
      "integrity": "sha512-D2hP9eA+Sqx1kBZgzxZh0y1trbuU+JoDkiEwqhQ36nodYqJwyEIhPSdMNd7lOm/4io72luTPWH20Yda0xOuUow==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
      "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "nod
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: barbotine-scalping-bot (`PHASE4-QUANT-060`)
- **Full Name**: `PHASE4-QUANT-060_nelso0__barbotine-scalping-bot`
- **Description**: Powered by Bitfinex's orderbooks data, Barbotine Scalping is a medium-frequency trading bot capable of taking successful trades without worrying about trends or market direction.
- **GitHub Stars**: 131
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<p align="left">
  <img alt="Barbotine arbitrage bot Logo" width="10%" height="auto" src="https://i.ibb.co/gy9mb2k/logo.png">
</p>

[![Twitter @nelsorex](https://img.shields.io/twitter/url/https/twitter.com/nelsorex.svg?style=social&label=%20%40nelsorex)](https://twitter.com/nelsorex)
[![GitHub @nelso0](https://img.shields.io/github/followers/nelso0?label=follow&style=social)](https://github.com/nelso0)

⚠️ The code isn't in this repo ⚠️

Website: [https://barbotine.xyz](https://barbotine.xyz)


==================================================


## [3/3] Repository: crypto-database (`PHASE4-QUANT-061`)
- **Full Name**: `PHASE4-QUANT-061_ivopetiz__crypto-database`
- **Description**: Database for crypto data, supporting several exchanges. Can be used for TA, bots, backtest, realtime trading, etc.
- **GitHub Stars**: 106
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9243d193bbe34717978b72b0477df4d2)](https://app.codacy.com/app/ivopetiz/crypto-database?utm_source=github.com&utm_medium=referral&utm_content=ivopetiz/crypto-database&utm_campaign=Badge_Grade_Dashboard)

# Crypto-database

Database to store all data from crypto exchanges, currently working with Binance, Bittrex, Cryptopia and Poloniex. 

Can be used for technical analysis, bots, backtest, realtime trading, etc.

## Installation


-   [BD Instalation](#bd-installation)
    -   [Docker](##docker)

    -   [Native](##native)
        -   [BD Configuration](#BD-Configuration)

-   [Market Prices To DB](#market-prices-to-db)
    -   [Data Interval](##data-interval)

-   [Balance To DB](#balance-to-db)

-   [Using Chronograf](#using-chronograf)

-   [TODO](#todo)

This install guide was made for **Ubuntu 16.04+**. Will need some adjustments to work with other distros.

## BD Installation

### Docker

Docker directory has a default configuration that allows users to implement an pre configured database, ready to receive data from Exchanges and use it.
In order to use Influxdb Docker container is only necessary to follow the steps bellow.

```bash
git clone https://github.com/ivopetiz/crypto-database.git
cd crypto-database
. docker/build
. docker/start
```
And your Influxdb crypto database throw Docker container should be ready to be used.

### Native

Start by installing Golang, to build the applications responsible for populate Crypto-database.

```bash
sudo apt-get install golang
```

After install Golang, you will need to install InfluxDB. Chronograf is also recomended.

```bash
sudo apt-get install influxdb influxdb-client chronograf
```

You can also get InfluxDB last versions from Influx website. 
This version of Crypto-database where tested with Influxdb 1.5.3 and Chronograf 1.5.0. You can install these packages by running:

```bash
wget https://dl.influxdata.com/influxdb/releases/influxdb_1.5.3_amd64.deb
sudo dpkg -i influxdb_1.5.3_amd64.deb 
wget https://dl.influxdata.com/chronograf/releases/chronograf_1.5.0.0_amd64.deb
sudo dpkg -i chronograf_1.5.0.0_amd64.deb
```

### BD Configuration

Start Influxdb and then run Influxdb prompt.

```bash
sudo systemctl enable influxdb.service
sudo systemctl start influxdb.service
influx
```

Create databases and user with privileges to use databases:

```influx
CREATE DATABASE altcoin
CREATE DATABASE balance
USE altcoin
CREATE USER <username> WITH PASSWORD '<password>' WITH ALL PRIVILEGES
GRANT ALL PRIVILEGES TO <username>
```

## Market Prices To DB

Before build crypto markets and balance applications is necessary to clone this repository.

```bash
git clone https://github.com/ivopetiz/crypto-database.git
```

 After cloning this rep, is necessary to configure Influxdb user, password and server on system. One option is to define variables on system in order to hide it from git. Variables can also be defined on **consts.go**.

```bash
DBUSER=<your-db-user>
DBPASS=<your-db-password>
SERVERDB=<your-db-server>
```

---
### Data Interval

*By default, data is recorded every 10 seconds but this value can be changed. Timeout can be defined on **consts.go**. A timeout too big won't present fast changes on prices. By the other hand, a timeout too small will make your IP address blocked on crypto exchanges, that only allows a certain number of request per minute. All exchanges have different limits and you can consult these values on exchanges API official websites.*

---

Log file will be stored on **/log/altdb_coin.log**. This path can be changed on **main.go**. Make sure you have the right privileges to write in **/log/**.

```bash
sudo mkdir /log
sudo touch /log/altdb_coin.log
sudo chown <user>:<user> /log/altdb_coin.log
sudo chmod 644 /log/altdb_coin.log
```

Compile market data getter executable.

```bash
cd markets
go get
go build -o markets -ldflags="-s -w" main.go consts.go
```

Go lang will return an executable file called **markets**. Now you need to run in order to populate database. One option is to use **markets** as a service, in order to keep tracking of it. To run **markets** as a service is necessary to create **/etc/systemd/system/cryptomarket.service** with the following content:

```bash
[Unit]
Description=Service running a crypto market data getter.
After=network.target

[Service]
Type=simple
User=user
WorkingDirectory=/home/user/crypto-database
ExecStart=/home/user/crypto-database/markets

Restart=always

[Install]
WantedBy=multi-user.target
```

After save **cryptomarket.service** file, run the commands bellow:

```bash
sudo systemctl daemon-reload
sudo systemctl enable cryptomarket.service
sudo systemctl start cryptomarket.service
```

Now **markets** will run as a service, starting when OS initializes and recovers in case of failure.

## Balance To DB

If you want to add your balance to DB, you will need to generate your API key on crypto exchanges, in order to validate your login and get your data. Currently working only with Bittrex exchange.

To generate an API key and secret, you can access crypto exchanges website, on definitions part. Make sure you keep your API key and API secret **secret** and give this key minimum permissions, in order to obtain just balance info. With bad permissions, any person with this key and secret can consult, trade or withdraw your coins.

After get API key and secret from exchanges, you need to add it to **balance.go**. One option is to define system variables:

```bash
BITTREX_API_KEY=<your-bittrex-api-key>
BITTREX_API_SECRET=<your-bittrex-api-secret>
```

After define **API_KEY** and **API_SECRET** in **balance.go** is necessary to build **balance** program:

```bash
cd balance
go get
go build -o balance -ldflags="-s -w" balance.go
```

Once **balance** is not supposed to run every minute it wasn't built with a timeout, so user need to run it everytime. This can be done automatically with a Crontab rule or as a service, like was done with **markets.service**.

To add new balance info to DB every hour, add a crontab rule by running **crontab -e** and add the following line:

```bash
0 * * * *   /home/user/crypto-database/balance
```

The above rule will run **balance** every hour at :00.

## Using Chronograf

Chronograf presents crypto data from Influxdb. Can be particularly useful to plot data or to quick check market prices. Chronograf is easy to use and it's only necessary to configure with your Influxdb definitions.

In order to start service, after installation will need to run:

```bash
sudo systemctl start chronograf.service
```

If you use Influxdb in the same machine as Chronograf service and have used the default configs, Influxdb will be in https://localhost:8086.

You will also need to input your Influxdb user and password in order to give Chronograf access to DB.

If Influxdb and Chronograf services are in diferent machines, you will need to change localhost by Influxdb machine IP address.

Chronograf service uses port **8888**. Port can be changed on **/etc/default/chronograf**.

Anyone can access Chronograf but is possible to block access from other machines. In config file you can change all configs.

By default, Chronograf config file will be looking like this:

```bash
HOST=0.0.0.0
PORT=8888
```

**HOST** will define who can access Chronograf website. It can be blocked to localhost machine or other specific IP address which can be a good option in terms of security.

---
## TODO

-   add more exchanges to Balance
-   makefile

### Core Implementation Code & Architecture
#### File: `docker/influxdb/config.toml`
```python
### Welcome to the InfluxDB configuration file.

# The values in this file override the default values used by the system if
# a config option is not specified. The commented out lines are the configuration
# field and the default value used. Uncommenting a line and changing the value
# will change the value used at runtime when the process is restarted.

# Once every 24 hours InfluxDB will report usage data to usage.influxdata.com
# The data includes a random ID, os, arch, version, the number of series and other
# usage data. No data from user databases is ever transmitted.
# Change this option to true to disable reporting.
# reporting-disabled = false

# Bind address to use for the RPC service for backup and restore.
# bind-address = "127.0.0.1:8088"

###
### [meta]
###
### Controls the parameters for the Raft consensus group that stores metadata
### about the InfluxDB cluster.
###

[meta]
  # Where the metadata/raft database is stored
  dir = "/var/lib/influxdb/meta"

  # Automatically create a default retention policy when creating a database.
  # retention-autocreate = true

  # If log messages are printed for the meta service
  # logging-enabled = true

###
### [data]
###
### Controls where the actual shard data for InfluxDB lives and how it is
### flushed from the WAL. "dir" may need to be changed to a suitable place
### for your system, but the WAL settings are an advanced configuration. The
### defaults should work for most systems.
###

[data]
  # The directory where the TSM storage engine stores TSM files.
  dir = "/var/lib/influxdb/data"

  # The directory where the TSM storage engine stores WAL files.
  wal-dir = "/var/lib/influxdb/wal"

  # The amount of time that a write will wait before fsyncing.  A duration
  # greater than 0 can be used to batch up multiple fsync calls.  This is useful for slower
  # disks or when WAL write contention is seen.  A value of 0s fsyncs every write to the WAL.
  # Values in the range of 0-100ms are recommended for non-SSD disks.
  # wal-fsync-delay = "0s"


  # The type of shard index to use for new shards.  The default is an in-memory index that is
  # recreated at startup.  A value of "tsi1" will use a disk based index that supports higher
  # cardinality datasets.
  # index-version = "inmem"

  # Trace logging provides more verbose output around the tsm engine. Turning
  # this on can provide more useful output for debugging tsm engine issues.
  # trace-logging-enabled = false

  # Whether queries should be logged before execution. Very useful for troubleshooting, but will
  # log any sensitive data contained within a query.
  # query-log-enabled = true

  # Settings for the TSM engine

  # CacheMaxMemorySize is the maximum size a shard's cache can
  # reach before it starts rejecting writes.
  # cache-max-memory-size = 1048576000

  # CacheSnapshotMemorySize is the size at which the engine will
  # snapshot the cache and write it to a TSM file, freeing up memory
  # cache-snapshot-memory-size = 26214400

  # CacheSnapshotWriteColdDuration is the length of time at
  # which the engine will snapshot the cache and write it to
  # a new TSM file if the shard hasn't received writes or deletes
  # cache-snapshot-write-cold-duration = "10m"

  # CompactFullWriteColdDuration is the duration at which the engine
  # will compact all TSM files in a shard if it hasn't received a
  # write or delete
  # compact-full-write-cold-duration = "4h"

  # The maximum number of concurrent full and level compactions that can run at one time.  A
  # value of 0 results in runtime.GOMAXPROCS(0) used at runtime.  This setting does not apply
  # to cache snapshotting.
  # max-concurrent-compactions = 0

  # The maximum series allowed per database before writes are dropped.  This limit can prevent
  # high cardinality issues at the database level.  This limit can be disabled by setting it to
  # 0.
  # max-series-per-database = 1000000

  # The maximum number of tag values per tag that are allowed before writes are dropped.  This limit
  # can prevent high cardinality tag values from being written to a measurement.  This limit can be
  # disabled by setting it to 0.
  # max-values-per-tag = 100000

###
### [coordinator]
###
### Controls the clustering service configuration.
###

[coordinator]
  # The default time a write request will wait until a "timeout" error is returned to the caller.
  # write-timeout = "10s"

  # The maximum number of concurrent queries allowed to be executing at one time.  If a query is
  # executed and exceeds this limit, an error is returned to the caller.  This limit can be disabled
  # by setting it to 0.
  # max-concurrent-queries = 0

  # The maximum time a query will is allowed to execute before being killed by the system.  This limit
  # can help prevent run away queries.  Setting the value to 0 disables the limit.
  # query-timeout = "0s"

  # The time threshold when a query will be logged as a slow query.  This limit can be set to help
  # discover slow or resource intensive queries.  Setting the value to 0 disables the slow query logging.
  # log-queries-after = "0s"

  # The maximum number of points a SELECT can process.  A value of 0 will make the maximum
  # point count unlimited.
  # max-select-point = 0

  # The maximum number of series a SELECT can run.  A value of 0 will make the maximum series
  # count unlimited.
  # max-select-series = 0

  # The maxium number of group by time bucket a SELECT can create.  A value of zero will max the maximum
  # number of buckets unlimited.
  # max-select-buckets = 0

###
### [retention]
###
### Controls the enforcement of retention policies for evicting old data.
###

[retention]
  # Determines whether retention policy enforcement enabled.
  # enabled = true

  # The interval of time when retention policy enforcement checks run.
  # check-interval = "30m"

###
### [shard-precreation]
###
### Controls the precreation of shards, so they are available before data arrives.
### Only shards that, after creation, will have both a start- and end-time in the
### future, will ever be created. Shards are never precreated that would be wholly
### or partially in the past.

[shard-precreation]
  # Determines whether shard pre-creation service is enabled.
  # enabled = true

  # The interval of time when the check to pre-create new shards runs.
  # check-interval = "10m"

  # The default period ahead of the endtime of a shard group that its successor
  # group is created.
  # advance-period = "30m"

###
### Controls the system self-monitoring, statistics and diagnostics.
###
### The internal database for monitoring data is created automatically if
### if it does not already exist. The target retention within this database
### is called 'monitor' and is also created with a retention period of 7 days
### and a replication factor of 1, if it does not exist. In all cases the
### this retention policy is configured as the default for the database.

[monitor]
  # Whether to record statistics internally.
  # store-enabled = true

  # The destination database for recorded statistics
  # store-database = "_internal"

  # The interval at which to record statistics
  # store-interval = "10s"

###
### [http]
###
### Controls how the HTTP endpoints are configured. These are the primary
### mechanism for getting data into and out of InfluxDB.
###

[http]
  # Determines whether HTTP endpoint is enabled.
  # enabled = true

  # The bind address used by the HTTP service.
  # bind-address = ":8086"

  # Determines whether user authentication is enabled over HTTP/HTTPS.
  # auth-enabled = false

  # The default realm sent back when issuing a basic auth challenge.
  # realm = "InfluxDB"

  # Determines whether HTTP request logging is enabled.
  # log-enabled = true

  # Determines whether detailed write logging is enabled.
  # write-tracing = false

  # Determines whether the pprof endpoint is enabled.  This endpoint is used for
  # troubleshooting and monitoring.
  # pprof-enabled = true

  # Determines whether HTTPS is enabled.
  # https-enabled = false

  # The SSL certificate to use when HTTPS is enabled.
  # https-certificate = "/etc/ssl/influxdb.pem"

  # Use a separate private key location.
  # https-private-key = ""

  # The JWT auth shared secret to validate requests using JSON web tokens.
  # shared-secret = ""

  # The default chunk size for result sets that should be chunked.
  # max-row-limit = 0

  # The maximum number of HTTP connections that may be open at once.  New connections that
  # would exceed this limit are dropped.  Setting this value to 0 disables the limit.
  # max-connection-limit = 0

  # Enable http service over unix domain socket
  # unix-socket-enabled = false

  # The path of the unix domain socket.
  # bind-socket = "/var/run/influxdb.sock"

  # The maximum size of a client request body, in bytes. Setting this value to 0 disables the limit.
  # max-body-size = 25000000

###
### [subscriber]
###
### Controls the subscriptions, which can be used to fork a copy of all data
### received by the InfluxDB host.
###

[subscriber]
  # Determines whether the subscriber service is enabled.
  # enabled = true

  # The default timeout for HTTP writes to subscribers.
  # http-timeout = "30s"

  # Allows insecure HTTPS connections to subscribers.  This is useful when testing with self-
  # signed certificates.
  # insecure-skip-verify = false

  # The path to the PEM encoded CA certs file. If the empty string, the default system certs will be used
  # ca-certs = ""

  # The number of writer goroutines processing the write channel.
  # write-concurrency = 40

  # The number of in-flight writes buffered in the write channel.
  # write-buffer-size = 1000


###
### [[graphite]]
###
### Controls one or many listeners for Graphite data.
###

[[graphite]]
  # Determines whether the graphite endpoint is enabled.
  # enabled = false
  # database = "graphite"
  # retention-policy = ""
  # bind-address = ":2003"
  # protocol = "tcp"
  # consistency-level = "one"

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Batching
  # will buffer points in memory if you have many coming in.

  # Flush if this many points get buffered
  # batch-size = 5000

  # number of batches that may be pending in memory
  # batch-pending = 10

  # Flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "1s"

  # UDP Read buffer size, 0 means OS default. UDP listener will fail if set above OS max.
  # udp-read-buffer = 0

  ### This string joins multiple matching 'measurement' values providing more control over the final measurement name.
  # separator = "."

  ### Default tags that will be added to all metrics.  These can be overridden at the template level
  ### or by tags extracted from metric
  # tags = ["region=us-east", "zone=1c"]

  ### Each template line requires a template pattern.  It can have an optional
  ### filter before the template and separated by spaces.  It can also have optional extra
  ### tags following the template.  Multiple tags should be separated by commas and no spaces
  ### similar to the line protocol format.  There can be only one default template.
  # templates = [
  #   "*.app env.service.resource.measurement",
  #   # Default template
  #   "server.*",
  # ]

###
### [collectd]
###
### Controls one or many listeners for collectd data.
###

[[collectd]]
  # enabled = false
  # bind-address = ":25826"
  # database = "collectd"
  # retention-policy = ""
  #
  # The collectd service supports either scanning a directory for multiple types
  # db files, or specifying a single db file.
  # typesdb = "/usr/local/share/collectd"
  #
  # security-level = "none"
  # auth-file = "/etc/collectd/auth_file"

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Batching
  # will buffer points in memory if you have many coming in.

  # Flush if this many points get buffered
  # batch-size = 5000

  # Number of batches that may be pending in memory
  # batch-pending = 10

  # Flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "10s"

  # UDP Read buffer size, 0 means OS default. UDP listener will fail if set above OS max.
  # read-buffer = 0

###
### [opentsdb]
###
### Controls one or many listeners for OpenTSDB data.
###

[[opentsdb]]
  # enabled = false
  # bind-address = ":4242"
  # database = "opentsdb"
  # retention-policy = ""
  # consistency-level = "one"
  # tls-enabled = false
  # certificate= "/etc/ssl/influxdb.pem"

  # Log an error for every malformed point.
  # log-point-errors = true

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Only points
  # metrics received over the telnet protocol undergo batching.

  # Flush if this many points get buffered
  # batch-size = 1000

  # Number of batches that may be pending in memory
  # batch-pending = 5

  # Flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "1s"

###
### [[udp]]
###
### Controls the listeners for InfluxDB line protocol data via UDP.
###

[[udp]]
  # enabled = false
  # bind-address = ":8089"
  # database = "udp"
  # retention-policy = ""

  # These next lines control how batching works. You should have this enabled
  # otherwise you could get dropped metrics or poor performance. Batching
  # will buffer points in memory if you have many coming in.

  # Flush if this many points get buffered
  # batch-size = 5000

  # Number of batches that may be pending in memory
  # batch-pending = 10

  # Will flush at least this often even if we haven't hit buffer limit
  # batch-timeout = "1s"

  # UDP Read buffer size, 0 means OS default. UDP listener will fail if set above OS max.
  # read-buffer = 0

###
### [continuous_queries]
###
### Controls how continuous queries are run within InfluxDB.
###

[continuous_queries]
  # Determines whether the continuous query service is enabled.
  # enabled = true

  # Controls whether queries are logged when executed by the CQ service.
  # log-enabled = true

  # interval for how often continuous queries will be checked if they need to run
  # run-interval = "1s"
```


==================================================
