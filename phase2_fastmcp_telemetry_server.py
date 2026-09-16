#!/usr/bin/env python3
"""
⚡ PHASE 2: FASTMCP READ-ONLY TELEMETRY & DIAGNOSTIC SERVER
===========================================================
Exposes deterministic, read-only diagnostic tools to AI agents
without granting unrestricted order-execution write access to the capital loop.
"""

import json
import sqlite3
from typing import Any, Dict, List
import duckdb
from fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("SovereignQuantTelemetry")

DB_PATH = "/Users/rajondas/teamwork_projects/sovereign-quant-os/phase2_canonical_ledger.sqlite"

@mcp.tool()
def get_reconciliation_diff() -> Dict[str, Any]:
    """
    Audits discrepancies between local outbox state and broker venue fills.
    Identifies any orders stuck in ACK_UNKNOWN or unconfirmed states.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT intent_id, state, event_type, timestamp_ns
        FROM (
            SELECT intent_id, state, event_type, timestamp_ns,
                   ROW_NUMBER() OVER (PARTITION BY intent_id ORDER BY seq_id DESC) as rn
            FROM hash_chained_event_ledger
        )
        WHERE rn = 1 AND state = 'ACK_UNKNOWN'
    """)
    unknown_orders = cur.fetchall()
    conn.close()
    
    return {
        "status": "HEALTHY" if len(unknown_orders) == 0 else "DRIFT_DETECTED",
        "unknown_order_count": len(unknown_orders),
        "unknown_orders": [
            {"intent_id": r[0], "state": r[1], "event": r[2], "ts": r[3]} for r in unknown_orders
        ]
    }

@mcp.tool()
def get_order_trace(intent_id: str) -> Dict[str, Any]:
    """
    Retrieves the complete cryptographic audit trail and lifecycle transitions
    for a specific OrderIntent by its deterministic ID.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT seq_id, epoch, event_type, state, payload_json, event_hash, timestamp_ns
        FROM hash_chained_event_ledger
        WHERE intent_id = ?
        ORDER BY seq_id ASC
    """, (intent_id,))
    rows = cur.fetchall()
    conn.close()
    
    events = []
    for r in rows:
        events.append({
            "seq": r[0],
            "epoch": r[1],
            "event_type": r[2],
            "state": r[3],
            "payload": json.loads(r[4]),
            "event_hash": r[5][:16] + "...",
            "timestamp_ns": r[6]
        })
    return {
        "intent_id": intent_id,
        "event_count": len(events),
        "lifecycle": events
    }

@mcp.tool()
def query_duckdb_summary() -> Dict[str, Any]:
    """
    Vectorized analytical query over the SQLite WAL ledger via DuckDB.
    Returns aggregated metrics without acquiring locks on the hot execution path.
    """
    duck_conn = duckdb.connect()
    query = f"""
        INSTALL sqlite;
        LOAD sqlite;
        ATTACH '{DB_PATH}' AS sqlite_db (TYPE SQLITE);
        SELECT 
            count(*) as total_events,
            count(DISTINCT intent_id) as total_intents,
            count(CASE WHEN event_type = 'BROKER_ACK_SUCCESS' THEN 1 END) as executed_orders,
            count(CASE WHEN event_type = 'RISK_REJECTED' THEN 1 END) as risk_rejections
        FROM sqlite_db.hash_chained_event_ledger;
    """
    res = duck_conn.execute(query).fetchone()
    return {
        "total_events": res[0],
        "total_intents": res[1],
        "executed_orders": res[2],
        "risk_rejections": res[3]
    }

@mcp.tool()
def get_ledger_hash_integrity() -> Dict[str, Any]:
    """
    Cryptographically verifies the SHA-256 hash chain link by link across all rows.
    Guarantees tamper-evidence and regulatory audit readiness.
    """
    import hashlib
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT seq_id, epoch, intent_id, event_type, state, payload_json,
               prev_event_hash, event_hash, timestamp_ns
        FROM hash_chained_event_ledger ORDER BY seq_id ASC
    """)
    rows = cur.fetchall()
    conn.close()
    
    expected_prev = "0" * 64
    for r in rows:
        seq_id, epoch, intent_id, ev_type, state, payload_str, prev_h, ev_h, ts_ns = r
        if prev_h != expected_prev:
            return {"valid": False, "broken_at_seq": seq_id, "reason": "PREV_HASH_MISMATCH"}
        raw = f"{epoch}:{intent_id}:{ev_type}:{state}:{payload_str}:{prev_h}:{ts_ns}"
        computed = hashlib.sha256(raw.encode('utf-8')).hexdigest()
        if computed != ev_h:
            return {"valid": False, "broken_at_seq": seq_id, "reason": "HASH_CORRUPTION"}
        expected_prev = ev_h
        
    return {
        "valid": True,
        "total_events_checked": len(rows),
        "status": "ALL_CRYPTOGRAPHIC_LINKS_INTACT"
    }

if __name__ == "__main__":
    print("Testing FastMCP Read-Only Telemetry Tools...")
    print("Reconciliation Diff:", get_reconciliation_diff())
    print("DuckDB Summary:", query_duckdb_summary())
    print("Hash Integrity:", get_ledger_hash_integrity())
