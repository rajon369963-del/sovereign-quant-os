#!/usr/bin/env python3
"""
populate_indian_god_mode_sqlite.py
==================================
Inserts the 30 Hacks and 30 Downloads into grand_10k_trading_hypergraph.sqlite
"""

import sqlite3

DB_PATH = "/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table for Hacks
cursor.execute("""
CREATE TABLE IF NOT EXISTS indian_algo_trading_top_30_hacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hack_number INTEGER UNIQUE,
    phase TEXT,
    title TEXT,
    mechanism TEXT,
    impact_on_dhan_bot TEXT,
    citations TEXT
);
""")

# Create table for Downloads
cursor.execute("""
CREATE TABLE IF NOT EXISTS indian_algo_trading_top_30_downloads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_number INTEGER UNIQUE,
    category TEXT,
    tool_name TEXT,
    source TEXT,
    purpose TEXT,
    system_status TEXT
);
""")

hacks = [
    (1, "Phase 1: Brain (NotebookLM)", "Zero-Upload Literature Review", "Upload 50+ strategy PDFs into NotebookLM to create an immutable Strategy Oracle.", "Zero hallucination on theoretical quant formulas.", "[1, 2]"),
    (2, "Phase 1: Brain (NotebookLM)", "The 'Context Window' API Bridge", "Ingest DhanHQ v2 & Fyers API v3 docs into NotebookLM to retrieve exact schemas.", "Eliminates 90% of broker connection & syntax errors.", "[3]"),
    (3, "Phase 1: Brain (NotebookLM)", "Citation Matrix for Signals", "Generate consensus matrix across 5 trading books for high-probability signals.", "Validates multi-author mathematical confluence.", "[1]"),
    (4, "Phase 1: Brain (NotebookLM)", "Raw CSV Verification & Audit", "Export backtest logs to CSV and prompt NotebookLM to audit for curve-fitting.", "Prevents deploying overfitted strategies with fake fills.", "[1]"),
    (5, "Phase 1: Brain (NotebookLM)", "Audio Briefings ('Deep Dive')", "Synthesize Deep Dive audio from weekly trade execution logs for commute listening.", "Provides screen-free risk critiques & post-mortem analysis.", "[4]"),
    (6, "Phase 1: Brain (NotebookLM)", "Sprint Planning Two-Stage Separation", "Separate planning (NotebookLM) from coding (Antigravity).", "Saves token costs and slashes algorithmic logic errors by 65%.", "[5]"),
    (7, "Phase 1: Brain (NotebookLM)", "Dynamic agents.md Risk Constitution", "Enforce strict risk rules (max 1% risk, no overnight naked shorts) via agents.md.", "Immutable safety gate before every broker API call.", "[6]"),
    (8, "Phase 1: Brain (NotebookLM)", "Concept-to-Code Pipeline", "Convert natural language thesis to pseudocode in NLM, then code in Antigravity.", "Accelerates idea validation by 10x.", "[7]"),
    (9, "Phase 2: Hands (Antigravity)", "Browser Control for Backtesting", "Direct headless browser to TradingView to verify indicators do not repaint.", "Ensures strategy integrity before risking live rupees.", "[13, 14]"),
    (10, "Phase 2: Hands (Antigravity)", "Self-Healing Code & Autonomous Debugging", "Pipe runtime exception logs to Antigravity for automated diagnosis & hotfix.", "Achieves zero-downtime autonomous bot operation.", "[5]"),
    (11, "Phase 2: Hands (Antigravity)", "Vibe Coding Strategic Prompts", "Specify quantitative intent rather than syntax (e.g. Ornstein-Uhlenbeck + ADX).", "Enables rapid institutional model generation.", "[9, 11]"),
    (12, "Phase 2: Hands (Antigravity)", "Docker Containerization", "Run trading bot inside isolated Docker containers.", "Shields operating system from rogue loops or file mutations.", "[19]"),
    (13, "Phase 2: Hands (Antigravity)", "Parallel Agent Swarms (Sentiment + Price)", "Deploy dual subagents: Agent A on news sentiment, Agent B on price action.", "Trades execute only on unanimous multi-agent consensus.", "[12]"),
    (14, "Phase 2: Hands (Antigravity)", "Scraping 'Links within Links' (NSE Ban)", "Scrape official NSE F&O ban list daily at 08:30 IST to update blacklist.", "Guarantees zero regulatory fines or blocked orders.", "[6, 8]"),
    (15, "Phase 2: Hands (Antigravity)", "Dedicated Sentiment Analysis Skills", "Use sentiment-analysis-trading skill to score Nifty heavyweights in real-time.", "Filters out false breakouts during adverse news flow.", "[12]"),
    (16, "Phase 2: Hands (Antigravity)", "Live 'Paper Trading' Verification", "Execute 60-min live simulation on incoming market feeds prior to capital deployment.", "Validates latency, slippage, and queue mechanics.", "[6, 8, 9]"),
    (17, "Phase 3: India Strategies", "Antigravity OCC Strategy (MA 5 + Delayed TSL)", "5-period SMA on 5m chart with 0.5% Delayed Trailing Stop Loss on Nifty.", "Captures massive intraday trend expansion legs.", "[13, 14]"),
    (18, "Phase 3: India Strategies", "Iron Fly Expiry Day Automation", "Automate ATM straddle with 20% stop-loss and 50% take-profit on combined premium.", "Systematizes Wednesday/Thursday expiry theta decay.", "[14]"),
    (19, "Phase 3: India Strategies", "The Hardcoded 7% Rule", "Enforce instant liquidation if position or portfolio draws down >= 7.0%.", "Eliminates catastrophic capital drawdowns.", "[15]"),
    (20, "Phase 3: India Strategies", "Fyers/Dhan API Token Automation Trick", "Automate headless login with TOTP (pyotp) at 08:45 IST to refresh .env tokens.", "Ensures uninterrupted daily broker connectivity.", "[16]"),
    (21, "Phase 3: India Strategies", "Spread Stretched 2-Sigma Mean Reversion", "Track Nifty vs BankNifty ratio; trade mean-reversion at +/- 2.0 sigma deviation.", "Provides market-neutral statistical arbitrage alpha.", "[17]"),
    (22, "Phase 3: India Strategies", "Inventory Management for Scalping", "Dynamically widen bid-ask spreads when position skew accumulates.", "Prevents inventory toxicity in volatile options books.", "[17]"),
    (23, "Phase 4: Optimization", "The 'God Mode' Overnight Sleep Setup", "Run continuous overnight backtests and token refreshes via persistent daemons.", "Guarantees full readiness at 09:15 IST opening bell.", "[1, 5]"),
    (24, "Phase 4: Optimization", "Marketing & Commercialization Architecture", "Use NotebookLM to synthesize institutional PRDs and landing page copy.", "Facilitates commercial signal distribution.", "[18]"),
    (25, "Phase 4: Optimization", "Interactive Local Dashboards (Streamlit)", "Deploy local Streamlit web app tracking live P&L, Greeks, and kill-switches.", "Gives full real-time operational observability.", "[11]"),
    (26, "Phase 4: Optimization", "Switchboard Extension Context Pipeline", "Transfer NotebookLM sprint plans directly to Antigravity task queues.", "Streamlines workflow without manual copy-paste friction.", "[5, 12, 19]"),
    (27, "Phase 4: Optimization", "Reject High-Frequency (HFT) Noise", "Confine LLM agents to 5m - 1h timeframes; avoid sub-second HFT traps.", "Aligns strategy logic with actual agent execution latencies.", "[1, 8]"),
    (28, "Phase 4: Optimization", "Rigorous Source Vetting Invariant", "Only ingest verified academic papers, official API docs, and audited data.", "Maintains a pristine, hallucination-free knowledge core.", "[1, 6]"),
    (29, "Phase 4: Optimization", "Sovereign Zero-Cost Infrastructure Arbitrage", "Leverage Google Antigravity free environment to build scalable quant infrastructure.", "Maximizes operational ROI prior to API paywalls.", "[18]"),
    (30, "Phase 4: Optimization", "Community Skill & Pattern Cloning", "Scrape r/IndiaAlgoTrading & r/google_antigravity for proven agents.md files.", "Rapidly integrates collective practitioner wisdom.", "[1, 5, 6, 8, 11, 17, 18]")
]

cursor.executemany("""
INSERT OR REPLACE INTO indian_algo_trading_top_30_hacks 
(hack_number, phase, title, mechanism, impact_on_dhan_bot, citations)
VALUES (?, ?, ?, ?, ?, ?);
""", hacks)

downloads = [
    (1, "Core Tools", "Google Antigravity Desktop App", "Official IDE", "Base agentic workspace with multi-file mutation & tools.", "Active (Current Workspace)"),
    (2, "Core Tools", "NotebookLM Agent Skill", "GitHub Official Bridge", "Direct authenticated querying of NotebookLM notebooks.", "Active (~/.gemini/config/skills/notebooklm/)"),
    (3, "Core Tools", "Docker Desktop", "Docker Inc.", "Sandboxed container runtime isolating trading bots.", "Available / Local Daemon"),
    (4, "Core Tools", "Python 3.14", "Python Foundation", "Primary runtime with full sovereign first-class execution.", "Active (/Users/rajondas/.local/bin/python3.14)"),
    (5, "Core Tools", "Node.js (Latest LTS)", "Node Foundation", "JavaScript execution environment powering MCP tools.", "Active (/opt/homebrew/bin/node)"),
    (6, "Core Tools", "Switchboard Extension", "Extension Store", "Context bridge mapping NotebookLM plans to Antigravity.", "Available / Verified"),
    (7, "Core Tools", "Cursor Agent Skill", "GitHub Pack", "Cursor-style command and editing conventions.", "Installed"),
    (8, "Core Tools", "Git", "SCM", "Version control, automated diffing, and rollbacks.", "Active (/usr/bin/git)"),
    (9, "Python Lib", "dhanhq", "PyPI", "Official client for Dhan API v2 (Orders, Portfolios, Ticks).", "Installed / Active"),
    (10, "Python Lib", "fyers-apiv3", "PyPI", "Official client for Fyers API v3.", "Installed / Available"),
    (11, "Python Lib", "zerodha-kiteconnect", "PyPI", "Official client for Zerodha Kite Connect API.", "Installed / Available"),
    (12, "Python Lib", "jesse", "PyPI", "Advanced crypto and equities algorithmic trading framework.", "Installed / Available"),
    (13, "Python Lib", "pandas_ta", "PyPI", "130+ technical analysis indicators optimized for Pandas.", "Installed / Active"),
    (14, "Python Lib", "streamlit", "PyPI", "Real-time interactive P&L and risk dashboard builder.", "Installed / Active"),
    (15, "Python Lib", "ccxt", "PyPI", "Unified multi-exchange cryptocurrency trading library.", "Installed / Available"),
    (16, "Python Lib", "vectorbt", "PyPI", "Lightning-fast vectorized backtesting engine.", "Installed / Active"),
    (17, "Python Lib", "yfinance", "PyPI", "Free historical market data extraction library.", "Installed / Active"),
    (18, "Agent Skill", "sentiment-analysis-trading", "npm / MCP", "Financial news sentiment scoring engine for equities.", "Available / Configured"),
    (19, "Agent Skill", "algorithmic-trading skill", "omer-metin", "Standard algorithmic trading automation blueprints.", "Available"),
    (20, "Agent Skill", "alpaca-mcp-server", "Alpaca / MCP", "Standardized order management and bracket execution schema.", "Available"),
    (21, "Agent Skill", "playwright / puppeteer", "npm / Python", "Headless browser automation for TradingView chart audits.", "Active / Installed"),
    (22, "TradingView", "Antigravity OCC Strategy", "Pine Script v5", "MA 5 + Delayed Trailing Stop-Loss (0.5%) intraday strategy.", "Created (Antigravity_OCC_Strategy_MA5_Delayed_TSL.pine)"),
    (23, "TradingView", "Iron Fly Indicator", "Pine Script v5", "Visualizer for options straddle & wing decay.", "Integrated"),
    (24, "TradingView", "Dynamic Range Box Engine", "Pine Script v5", "Intraday consolidation breakout detector.", "Integrated"),
    (25, "Config Spec", "agents.md Risk Template", "AntiGravity", "Immutable risk constitution enforcing 1% max risk & rules.", "Active (/Users/rajondas/.gemini/config/plugins/)"),
    (26, "Prompts", "Vibe Coding Prompt Pack", "Community", "Production prompts for generating zero-bug quant scripts.", "Documented"),
    (27, "Content", "Deep Dive Audio Generator", "NotebookLM", "Synthesizes spoken strategic critiques of trade logs.", "Active / Deployed"),
    (28, "Content", "Citation Matrix Generator", "NotebookLM", "Generates cross-literature signal consensus tables.", "Active / Deployed"),
    (29, "Content", "AI Profit Boardroom Landing", "Template", "Web presentation framework for algorithmic strategies.", "Documented"),
    (30, "Reference", "Official Dhan/Fyers API PDFs", "Broker Docs", "Grounded API specifications uploaded into NotebookLM.", "Grounded in Cloud Notebooks")
]

cursor.executemany("""
INSERT OR REPLACE INTO indian_algo_trading_top_30_downloads 
(item_number, category, tool_name, source, purpose, system_status)
VALUES (?, ?, ?, ?, ?, ?);
""", downloads)

conn.commit()
conn.close()
print("Successfully populated 30 Hacks and 30 Downloads into grand_10k_trading_hypergraph.sqlite!")
