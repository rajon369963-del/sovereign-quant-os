# ⚡ [QUANT-SOURCE-029] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_029_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: nseutility (`WHEEL_nseutility`)
- **Full Name**: `nseutility`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# nseutility
Some Python based utility for Algo traders in Indian Stock Market


==================================================


## [2/3] Repository: quantiq (`WHEEL_quantiq`)
- **Full Name**: `quantiq`
- **Description**:  End-to-end algorithmic trading system | NSE | Python | Dhan API
- **GitHub Stars**: 6
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# QuantIQ

> End-to-end algorithmic trading system · NSE Indian equity market · Python

![Status](https://img.shields.io/badge/Status-In%20_Progress-%20?labelColor=0d1117&color=3fb950)
![Python](<https://img.shields.io/badge/Language-Python-yellow?logo=python&logoColor=rgb(52%2C%20118%2C%20169)&labelColor=ffd53d&color=rgb(52%2C%20118%2C%20169)>)
![Broker](https://img.shields.io/badge/Dhan-Broker?label=Broker&labelColor=ffffff&color=4fbb94)
![Repo](https://img.shields.io/badge/Visibility-Public-Green)

---

## Overview

QuantIQ is a collaborative 12-week project to build a working paper-trading bot on the NSE using the Dhan API. Equal parts learning vehicle, team collaboration exercise, and portfolio piece.

**Scope:** Strategy design → backtesting → live paper trading via Dhan API
**Market:** NSE equity (with F&O context)
**Timeline:** 12 weeks · 5 phases · public since Week 7

---

## Team

Phase 1 roles assigned 17 May 2026. Reviewed again at end of Phase 1. P = primary, S = secondary.

| Name | Role                                                  | Status |
| :--- | :-----------------------------------------------------| :----- |
| RS   | Project Lead                                          | Active |
| GT   | Co-Lead \| Quant / Strategy (P) \| Analyst / Docs (S) | Active |
| EB   | Analyst / Docs (P) \| Dev / Infra (S)                 | Active |
| AV   | Quant / Strategy (P) \| Data Engineering (S)          | Active |
| AR   | Dev / Infra (P) \| Data Engineering (S)               | Active |
| RT   | Quant / Strategy (P) \| Dev / Infra (S)               | Active |
| NS   | Dev / Infra (P) \| Data Engineering (S)               | Active |
| AJ   | Data Engineering (P) \| Quant / Strategy (S)          | Active |
| SS   | Quant / Strategy (P) \| Analyst / Docs (S)            | Active |
| SmS  | Data Engineering (P) \| Analyst / Docs (S)            | Active |
| AK   | Dev / Infra (P) \| Data Engineering (S)               | Active |
| ShS  | Analyst / Docs (P) \| Dev / Infra (S)                 | Active |

_Roles reviewed at Phase 2 sync (1 Jun 2026); sub-team leads assigned (see CLAUDE.md §8)._

---

## Roadmap

| Phase                   | Weeks | Deliverable                                   | Status         |
| :---------------------- | :---: | :-------------------------------------------- | :------------- |
| 0 — Onboarding          |   1   | First commit from every member                | ✅ Complete    |
| 1 — Foundations         |  2–4  | Individual NSE data analysis scripts          | ✅ Complete    |
| 2 — Data & Analysis     |  4–5  | Group NIFTY50 analysis                        | ✅ Complete    |
| 3 — Strategy & Backtest |  6–8  | `src/` data/screener/watchlist build + backtest report | 🔄 In Progress (overdue, near done) |
| 4 — Paper Trading       | 9–10  | Dhan client, execution loop, 3+ paper sessions | 🔄 In Progress (started early) |
| 5 — Ship It             | 11–12 | Dashboard, deploy, portfolio-ready repo       | ⏳ Pending     |

---

## Setup

> ⚠️ **Python version:** Use **3.12 only.** Python 3.13+ will fail to install several core data libraries.

```bash
# 1. Clone and enter the repo
git clone https://github.com/Quant-IQ/quantiq.git
cd quantiq

# 2. Confirm your Python version
compgen -c python | sort -u   # Must have 3.12.x (Runs only on bash)

# 3. Create a virtual environment
python3.12 -m venv venv          # Mac / Linux
py -3.12 -m venv venv            # Windows

# 4. Activate it
source venv/bin/activate          # Mac / Linux
venv\Scripts\activate             # Windows (Command Prompt)
source venv/Scripts/activate      # Windows (Git Bash)

# 5. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 6. Configure environment variables
cp .env.example .env
# Open .env and fill in your Dhan client ID and access token

# Verify .env is not tracked (it must NOT appear here)
git status

# 7. Make your first contribution
git checkout -b feat(scope)/your-change
# Make your change under src/
git add <changed files>
git commit -m "feat(scope): your change"
git push origin feat(scope)/your-change
# GitHub will print a URL in the terminal — open it to submit your PR
```

---

## Stack

| Layer       | Tools                         |
| :---------- | :---------------------------- |
| Language    | Python 3.12                   |
| Data        | `yfinance`, `pandas`, `numpy` |
| Indicators  | `ta`                          |
| Backtesting | `vectorbt`                    |
| Broker API  | `dhanhq` (Dhan)               |
| Dashboard   | `Streamlit`                   |
| Charts      | `plotly`                      |

---

## Repository Structure

```text
quantiq/
├── src/
│   ├── data/          # Fetching, indicators, ticker map, validation, charts
│   ├── screener/      # Filter engine, config, cache, technical/fundamental filters
│   ├── watchlist/     # Static/dynamic watchlists, persistence, manager
│   ├── strategy/      # Entry/exit logic — base ABC, signals, SMA crossover, RSI mean-reversion
│   ├── execution/     # Dhan API and order management
│   └── dashboard/     # Streamlit app
├── backtest/          # Backtest results and reports
├── logs/              # Trade signal logs (CSV)
└── docs/              # Architecture notes
```

---

## Communication & Tools

| Tool     | Purpose                                              |
| :------- | :--------------------------------------------------- |
| Discord  | Primary team communication — all project discussions |
| Notion   | Docs, weekly log, decisions log, Kanban overview     |
| GitHub   | Code, PRs, Issues, Projects board                    |
| WhatsApp | Urgent personal messages only — not project tracking |

> Discord channel guide: `#standup` (Monday standups only) · `#dev` (code + PRs) · `#markets` (strategy) · `#data` (pipelines) · `#resources` (links only)

---

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a PR. Key rules:

- Never push directly to `main`
- Never merge your own PR — all PRs require one reviewer
- Write `Closes #<issue>` in your PR description to auto-close the linked issue
- Branch naming: `feat(scope)/`, `fix(scope)/`, `data(scope)/`, `docs/`, `backtest/`

---

## Legal

Algo trading on your own account for personal use is legal in India under SEBI guidelines. This project does not manage third-party capital and is not offered as a commercial service. The current binding regulation is the [SEBI Circular — Safer Participation of Retail Investors in Algorithmic Trading (Feb 2025)](https://www.sebi.gov.in/legal/circulars/feb-2025/safer-participation-of-retail-investors-in-algorithmic-trading_91614.html), which became fully mandatory on 1 April 2026.

---

_README is a living document. Updated at the end of each phase by the Analyst / Docs role._
_Last updated: Week 7 (13 Jul 2026)_

### Core Implementation Code & Architecture
#### File: `src/screener/__init__.py`
```python

```

#### File: `src/screener/filters/__init__.py`
```python

```

#### File: `src/watchlist/__init__.py`
```python

```

#### File: `src/strategy/__init__.py`
```python

```

#### File: `src/__init__.py`
```python
# QuantIQ source package
```

#### File: `pyproject.toml`
```python
[project]
name = "quantiq"
version = "0.1.0"
description = "QuantIQ — NSE Algorithmic Trading"
requires-python = ">=3.11,<3.13"

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B"]   # style, pyflakes, isort, naming, upgrades, bugbear
ignore = ["E501"]                            # line-too-long handled by formatter

[tool.ruff.format]
quote-style = "double"
indent-style = "tab"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```


==================================================


## [3/3] Repository: stockbreakindia-test (`WHEEL_stockbreakindia-test`)
- **Full Name**: `stockbreakindia-test`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Core Implementation Code & Architecture
#### File: `app/applet/metadata.json`
```python
{
  "name": "SROCKBREAK US",
  "description": "US Market stock analysis and virtual trading",
  "requestFramePermissions": [],
  "majorCapabilities": ["MAJOR_CAPABILITY_SERVER_SIDE_GEMINI_API"]
}
```

#### File: `metadata.json`
```python
{
  "name": "US Stock Pro",
  "description": "An AI-powered US stock market intelligence and portfolio analysis app.",
  "requestFramePermissions": [],
  "majorCapabilities": [
    "MAJOR_CAPABILITY_SERVER_SIDE_GEMINI_API"
  ]
}
```

#### File: `fix_stockscanner_2.py`
```python
import re
import os

def fix_stockscanner():
    filepath = 'app/src/main/java/com/example/StockScanner.kt'
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = content.replace('"HDFCAMC", "JPM",', '"HDFCAMC",')
    with open(filepath, 'w') as f:
        f.write(content)

fix_stockscanner()
```

#### File: `fix_fallback.py`
```python
import re

filepath = 'app/src/main/java/com/example/GeminiService.kt'
with open(filepath, 'r') as f:
    content = f.read()

content = content.replace('"TCS / Tech Leader"', '"Microsoft Corp."')
content = content.replace('"Tata Motors"', '"Tesla Inc."')
content = content.replace('"Apple Inc."', '"Apple Inc."')

with open(filepath, 'w') as f:
    f.write(content)
```

#### File: `check_dupes.py`
```python
import re

with open('app/src/main/java/com/example/StockScanner.kt', 'r') as f:
    content = f.read()

m = re.search(r'val SP500_TICKERS = listOf\((.*?)\)', content, re.DOTALL)
if m:
    items = m.group(1).replace('\n', '').replace(' ', '').split(',')
    items = [x.strip('"') for x in items if x]
    seen = set()
    for item in items:
        if item in seen:
            print(f"Duplicate in SP500_TICKERS: {item}")
        seen.add(item)
```

#### File: `check_dict.py`
```python
import re

with open('app/src/main/java/com/example/LiveScreen.kt', 'r') as f:
    content = f.read()

m = re.search(r'val STOCK_DICTIONARY = listOf\((.*?)\)', content, re.DOTALL)
if m:
    lines = m.group(1).split('),')
    keys = []
    for line in lines:
        match = re.search(r'StockInfo\("([^"]+)"', line)
        if match:
            keys.append(match.group(1))
    
    seen = set()
    for key in keys:
        if key in seen:
            print(f"Duplicate in STOCK_DICTIONARY: {key}")
        seen.add(key)
```


==================================================
