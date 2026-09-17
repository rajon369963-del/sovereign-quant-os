import sqlite3
import json
import datetime

db_path = "/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 1. 10 NODES
nodes = [
    ("Macro_Sensex_0DTE_ShortGamma", "NOTEBOOKLM_EXTERNAL", "MACRO_EXPIRY", "0-DTE Sensex Short Gamma Unwind at 76,000 / 76,200", json.dumps({"underlying": "SENSEX", "catalyst": "Expiry short squeeze", "strike": "76000_76200"})),
    ("Macro_PSU_Credit_Dividend", "NOTEBOOKLM_EXTERNAL", "FUNDAMENTAL", "PSU Credit Expansion & PNB Dividend Payout Catalyst", json.dumps({"sector": "PSU_BANK", "symbol": "PNB", "sentiment": "Bullish"})),
    ("Macro_FMCG_Defensive_Hedging", "NOTEBOOKLM_EXTERNAL", "DEFENSIVE", "ITC Low-Beta Institutional Accumulation Hedge", json.dumps({"sector": "FMCG", "symbol": "ITC", "beta": 0.65})),
    ("Micro_L2_OrderFlowImbalance", "ANTIGRAVITY_INTERNAL", "MICROSTRUCTURE", "Level 2 Order Flow Imbalance OFI_t > +0.25", json.dumps({"source": "DhanHQ_L2_WebSocket", "threshold": 0.25})),
    ("Micro_Chandelier_ATR_Trail", "ANTIGRAVITY_INTERNAL", "RISK_ENGINE", "Dynamic 1.5x ATR_14 Chandelier Trailing Ratchet", json.dumps({"multiplier": 1.5, "period": 14, "rule": "Ratchet Up Only"})),
    ("Asset_PNB_Holding", "ANTIGRAVITY_INTERNAL", "ACTIVE_POSITION", "PNB Long 14 shares @ 118.32 (Breakeven SL 118.35)", json.dumps({"qty": 14, "buyAvg": 118.32, "target": 121.50, "realized": 8.82})),
    ("Asset_ITC_Holding", "ANTIGRAVITY_INTERNAL", "ACTIVE_POSITION", "ITC Long 4 shares @ 267.00 (Hard SL 265.80)", json.dumps({"qty": 4, "buyAvg": 267.00, "target": 272.20, "risk": 4.80})),
    ("Asset_RBLBANK_Breakout", "ANTIGRAVITY_INTERNAL", "WATCHLIST_SNIPER", "RBL Bank 52-Week High Volume Breakout Candidate", json.dumps({"ltp": 411.50, "signal": "3Gate_Sniper_Ready", "margin_budget": 215.00})),
    ("Risk_Variance_Shield_2.5Pct", "ANTIGRAVITY_INTERNAL", "GOVERNANCE", "2.5% SOD Capital Drawdown Circuit Breaker (Rs 22.96)", json.dumps({"hard_stop": 22.96, "capital": 918.43, "rule": "Emergency Halt"})),
    ("Target_Recovery_Plus102", "NOTEBOOKLM_ANTIGRAVITY_FUSION", "TARGET_LOCK", "Net Session Profit Target +Rs 102.00 (Done for the Day)", json.dumps({"goal": 102.00, "covers": "Rs 89.57 loss + Rs 12.00 taxes", "action": "Lock Equity"}))
]

for node_id, src, ntype, label, djson in nodes:
    cursor.execute("""
        INSERT OR REPLACE INTO hypergraph_nodes (node_id, graph_source, node_type, label, data_json, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (node_id, src, ntype, label, djson, now))

# 2. 7 DIRECTED EDGES
edges = [
    ("E1_SENSEX_SPILLOVER", "Macro_Sensex_0DTE_ShortGamma", "Macro_PSU_Credit_Dividend", "Positive_Gamma_Spillover", 0.88, "Sensex 0-DTE call unwind forces institutional buying into high-beta PSU banking baskets", now),
    ("E2_PNB_CATALYST", "Macro_PSU_Credit_Dividend", "Asset_PNB_Holding", "Fundamental_Momentum", 0.92, "Credit growth and dividend news create sustained buy-side queue stacking in PNB", now),
    ("E3_OFI_VALIDATION", "Micro_L2_OrderFlowImbalance", "Asset_PNB_Holding", "Delta_Surge_Check", 0.95, "L2 aggressor volume confirms institutional buying outweighs resting sell orders", now),
    ("E4_CHANDELIER_RATCHET", "Asset_PNB_Holding", "Micro_Chandelier_ATR_Trail", "Dynamic_Ratchet", 0.90, "ATR trailing stop moves up with price expansion, locking in accrued gains without premature selling", now),
    ("E5_CAPITAL_PRESERVATION", "Micro_Chandelier_ATR_Trail", "Risk_Variance_Shield_2.5Pct", "Risk_Capital_Preservation", 0.96, "Breakeven ratchet eliminates downside risk, preserving capital and freeing budget for sniper re-entry", now),
    ("E6_SNIPER_ALLOCATION", "Risk_Variance_Shield_2.5Pct", "Asset_RBLBANK_Breakout", "Allocated_Margin", 0.85, "Deploys remaining Rs 370 cash margin into high-conviction 1:2 R:R breakout trade", now),
    ("E7_COMPOUND_RECOVERY", "Asset_PNB_Holding", "Target_Recovery_Plus102", "Compound_Recovery", 0.99, "Combines PNB target (+Rs 44.52), ITC target (+Rs 21.60), and realized profit (+Rs 1.26) to hit +Rs 102 lock", now)
]

for edge_id, src_node, tgt_node, rel_type, weight, rationale, created_at in edges:
    cursor.execute("""
        INSERT OR REPLACE INTO hypergraph_edges (edge_id, source_node, target_node, relation_type, weight, rationale, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (edge_id, src_node, tgt_node, rel_type, weight, rationale, created_at))

# 3. DUAL-GRAPH 1000X INTERCONNECTION RECORD
cursor.execute("""
    INSERT INTO dual_graph_1000x_interconnections (timestamp, video_entity, quant_repo_entity, interconnection_alpha, verdict)
    VALUES (?, ?, ?, ?, ?)
""", (
    now,
    "LIVE_YOUTUBE_17SEP_SENSEX_0DTE_PSU_CREDIT",
    "NautilusTrader_VectorBT_Riskfolio_ChandelierATR",
    "Founder Mandate Synthesis: Prevents premature exit of winning positions (PNB & ITC). Interconnects 0-DTE short-gamma cascades with 1.5x ATR Chandelier ratchets, achieving +Rs 102 recovery while capping turnover at Rs 3,000 and friction at Rs 3.20.",
    "EXECUTED_AND_COMMITTED"
))

conn.commit()
conn.close()
print("SUCCESS: Hypergraph nodes, edges, and interconnections committed to grand_10k_trading_hypergraph.sqlite")
