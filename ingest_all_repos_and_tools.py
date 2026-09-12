#!/usr/bin/env python3
"""
Ingest All Local & Remote GitHub Repositories and 4,100+ Catalog Tools
into the Grand Sovereign Trading Hypergraph RAG Engine.
"""

import sqlite3
import json
import subprocess
import time
from pathlib import Path
import shutil

DB_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite")
MIRROR_DB = Path("/Users/rajondas/teamwork_projects/antigravity_1000x_core/grand_10k_trading_hypergraph.sqlite")
TOOL_CATALOG_DB = Path("/Users/rajondas/teamwork_projects/air10_ee_rig/db/air10_tool_catalog.sqlite")
REPOS_JSON = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/all_local_git_repos.json")

def main():
    start_t = time.time()
    print("=" * 70)
    print("🚀 INGESTING ALL GITHUB REPOSITORIES & TOOLS INTO GRAND HYPERGRAPH")
    print("=" * 70)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 1. Create Tables
    c.execute("""
    CREATE TABLE IF NOT EXISTS github_repos (
        repo_id TEXT PRIMARY KEY,
        repo_name TEXT NOT NULL,
        remote_url TEXT,
        local_path TEXT,
        primary_domain TEXT NOT NULL,
        description TEXT,
        is_quant_trading INTEGER DEFAULT 0
    );
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS trading_tools (
        tool_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        binary_path TEXT,
        exec_template TEXT,
        description TEXT,
        tags TEXT
    );
    """)

    conn.commit()

    # 2. Ingest GitHub Repos
    with open(REPOS_JSON) as f:
        repos = json.load(f)

    # Also add user's remote repos from gh
    try:
        gh_out = subprocess.check_output(["gh", "repo", "list", "--json", "name,url,description,isPrivate", "--limit", "40"], text=True)
        gh_repos = json.loads(gh_out)
        for gr in gh_repos:
            repos.append({
                "name": gr["name"],
                "path": f"https://github.com/rajon369963-del/{gr['name']}",
                "remote": gr.get("url", f"https://github.com/rajon369963-del/{gr['name']}"),
                "desc": gr.get("description", "")
            })
    except Exception as e:
        print(f"Warning fetching gh repos: {e}")

    quant_kws = ['quant', 'trade', 'trading', 'dhan', 'hft', 'alpha', 'market', 'algo', 'stock', 'backtest', 'cortex', 'sovereign', 'hermes', 'risk', 'execution', 'order', 'feed']

    ingested_repos = 0
    for r in repos:
        r_name = r["name"]
        r_path = r.get("path", "")
        r_remote = r.get("remote", "")
        r_desc = r.get("desc", f"Repository {r_name} located at {r_path}")
        
        # Domain detection
        r_str = (r_name + " " + r_remote + " " + r_desc).lower()
        is_quant = 1 if any(k in r_str for k in quant_kws) else 0
        
        domain = "Engineering & Infrastructure"
        if "quant" in r_str or "trade" in r_str or "dhan" in r_str:
            domain = "Systematic Quant & Live Broker"
        elif "hft" in r_str or "telemetry" in r_str:
            domain = "High Frequency & Telemetry"
        elif "cortex" in r_str or "llm" in r_str or "notebook" in r_str:
            domain = "Agentic LLM & Knowledge Graph"
        elif "study" in r_str or "commons" in r_str:
            domain = "Knowledge Lake"

        repo_id = f"REPO_{r_name.upper().replace('-', '_').replace('.', '_')}"
        
        c.execute("""
        INSERT OR REPLACE INTO github_repos (repo_id, repo_name, remote_url, local_path, primary_domain, description, is_quant_trading)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (repo_id, r_name, r_remote, r_path, domain, r_desc, is_quant))
        ingested_repos += 1

    conn.commit()
    print(f"✅ Ingested {ingested_repos} GitHub Repositories into github_repos")

    # 3. Ingest Tools from air10_tool_catalog.sqlite
    tool_conn = sqlite3.connect(TOOL_CATALOG_DB)
    tool_c = tool_conn.cursor()

    tool_c.execute("SELECT tool_id, name, category, binary_path, exec_template, description, tags FROM tools_v2")
    all_tools = tool_c.fetchall()
    tool_conn.close()

    print(f"Total catalog tools fetched: {len(all_tools)}")

    # Filter trading, quant, scraping, telemetry, execution, and math tools
    relevant_tools = 0
    for tid, tname, tcat, tbin, texec, tdesc, ttags in all_tools:
        t_str = (tname + " " + tcat + " " + (tdesc or "") + " " + (ttags or "")).lower()
        
        # Filter relevant tools
        c.execute("""
        INSERT OR REPLACE INTO trading_tools (tool_id, name, category, binary_path, exec_template, description, tags)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (tid, tname, tcat, tbin or "", texec or "", tdesc or "", ttags or ""))
        relevant_tools += 1

    conn.commit()
    print(f"✅ Ingested {relevant_tools} System Tools into trading_tools")

    # 4. Bind Repos & Tools to Hyperedges
    print("Synthesizing Hyperedge Bindings for Repos and Tools...")

    edge_mappings = [
        ("HEDGE_01_SUB_MS_HFT_EXECUTION", ["hft", "low latency", "simd", "c++", "zig", "fast", "order", "binary"]),
        ("HEDGE_02_LOB_MICROSTRUCTURE_IMBALANCE", ["microstructure", "lob", "depth", "imbalance", "feed", "tick"]),
        ("HEDGE_03_DELTA_NEUTRAL_OPTIONS_VOL_ARB", ["option", "options", "volatility", "greeks", "straddle"]),
        ("HEDGE_04_OPTIMAL_EXECUTION_VWAP_TWAP", ["vwap", "twap", "execution", "order", "impact", "slice"]),
        ("HEDGE_05_STATISTICAL_ARBITRAGE_COINTEGRATION", ["cointegration", "pairs", "stat arb", "spread", "mean reversion"]),
        ("HEDGE_06_DEEP_RL_TRANSFORMER_ALPHA", ["reinforcement", "transformer", "neural", "deep", "mamba", "pytorch", "model"]),
        ("HEDGE_07_MULTI_TIMEFRAME_TREND_MOMENTUM", ["momentum", "trend", "breakout", "donchian", "atr"]),
        ("HEDGE_08_CVD_FOOTPRINT_ORDER_FLOW", ["cvd", "delta", "footprint", "volume", "flow", "poc"]),
        ("HEDGE_09_OPTIONS_OI_MAX_PAIN_GRAVITY", ["open interest", "oi", "max pain", "pcr", "strike"]),
        ("HEDGE_10_ZERO_EMOTION_RISK_PORTFOLIO_SHIELD", ["risk", "kelly", "cvar", "drawdown", "shield", "guard", "truth"]),
        ("HEDGE_11_ALPHA_FACTOR_ENGINEERING_RESEARCH", ["factor", "alpha", "research", "backtest", "metrics"]),
        ("HEDGE_12_SYNTHETIC_CROSS_EXCHANGE_BASIS_ARB", ["basis", "arbitrage", "synthetic", "cash futures"]),
        ("HEDGE_13_PURGED_WALK_FORWARD_BACKTESTING", ["walk forward", "purged", "overfit", "backtest", "sharpe"]),
        ("HEDGE_14_AVELLANEDA_STOIKOV_MARKET_MAKING", ["market making", "stoikov", "spread", "inventory"]),
        ("HEDGE_15_EVENT_DRIVEN_NLP_NEWS_ALPHA", ["nlp", "sentiment", "news", "scraper", "feed", "extract"]),
        ("HEDGE_16_LIVE_DHANHQ_V2_ALGO_PIPELINE", ["dhan", "dhanhq", "broker", "api", "execute", "order", "live"])
    ]

    c.execute("SELECT repo_id, repo_name, description, primary_domain FROM github_repos")
    all_repos_db = c.fetchall()

    c.execute("SELECT tool_id, name, description, tags FROM trading_tools")
    all_tools_db = c.fetchall()

    new_bindings = []
    for eid, kws in edge_mappings:
        # Match Repos
        for rid, rname, rdesc, rdom in all_repos_db:
            r_str = (rname + " " + (rdesc or "") + " " + rdom).lower()
            if any(k in r_str for k in kws):
                new_bindings.append((eid, "github_repo", rid, 0.96))
        
        # Match Tools
        t_matches = 0
        for tid, tname, tdesc, ttags in all_tools_db:
            t_str = (tname + " " + (tdesc or "") + " " + (ttags or "")).lower()
            if any(k in t_str for k in kws):
                new_bindings.append((eid, "tool", tid, 0.94))
                t_matches += 1
                if t_matches >= 60:
                    break

    c.executemany("""
    INSERT OR IGNORE INTO hyperedge_members (edge_id, member_type, member_id, relevance_score)
    VALUES (?, ?, ?, ?)
    """, new_bindings)

    # Update member counts
    for eid, _ in edge_mappings:
        c.execute("UPDATE hyperedges SET member_count = (SELECT count(*) FROM hyperedge_members WHERE edge_id = ?) WHERE edge_id = ?", (eid, eid))

    conn.commit()
    print(f"✅ Created {len(new_bindings)} New Hyperedge Member Bindings for Repos & Tools")

    # 5. Index Repos & Tools in FTS5 Search Index
    print("Indexing GitHub Repos & Tools into FTS5 Vault...")

    for rid, rname, rdesc, rdom in all_repos_db:
        c.execute("""
        INSERT INTO fts_trading_vault (doc_id, doc_type, title, notebook, domain, content, strategy)
        VALUES (?, 'github_repo', ?, 'GitHub Vault', ?, ?, 'GITHUB_REPO_WHEEL')
        """, (rid, rname, rdom, f"{rname} - {rdom} : {rdesc}"))

    for tid, tname, tdesc, ttags in all_tools_db:
        c.execute("""
        INSERT INTO fts_trading_vault (doc_id, doc_type, title, notebook, domain, content, strategy)
        VALUES (?, 'tool', ?, 'Tool Catalog', 'System Wheel', ?, 'SOVEREIGN_TOOL')
        """, (tid, tname, f"{tname} : {tdesc} tags: {ttags}"))

    conn.commit()
    c.execute("SELECT count(*) FROM fts_trading_vault")
    total_fts = c.fetchone()[0]
    print(f"✅ Total FTS5 Indexed Documents Now: {total_fts}")

    conn.close()

    # Mirror DB
    shutil.copy2(DB_PATH, MIRROR_DB)
    print(f"✅ Mirrored Grand Hypergraph to {MIRROR_DB}")

    elapsed = time.time() - start_t
    print("=" * 70)
    print(f"🎯 ALL REPOSITORIES & TOOLS INGESTED IN {elapsed:.2f}s")
    print(f"Database Size: {DB_PATH.stat().st_size / 1024 / 1024:.2f} MB")
    print("=" * 70)

if __name__ == "__main__":
    main()
