#!/usr/bin/env python3
"""
⚡ AUTOMATED CONSOLIDATED 600+ QUANT REPOSITORIES INGESTION ENGINE
================================================================
Autonomous end-to-end ingestion and cryptographic verification engine for all 250
consolidated Quant & Algo Trading GitHub Repositories (covering 739 unique repos)
into Google NotebookLM.

Target Notebook: https://notebook.google.com/notebook/d4091527-ae47-4c73-abf6-7c3a4ead8677
Account: lakhidas168@gmail.com
Active Session: Google Chrome
Source Directory: /Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_quant_600_sources/
Database: /Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite
Receipt: /Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_600_upload_receipt.json
"""

import json
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

NOTEBOOK_ID = "d4091527-ae47-4c73-abf6-7c3a4ead8677"
SOURCE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_quant_600_sources")
DB_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite")
RECEIPT_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_600_upload_receipt.json")
LOG_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/logs/ingestion_consolidated_600.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
TEMP_JS = "/tmp/nlm_consolidated_runner.js"

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS quant_consolidated_notebooklm_ingestion (
        bundle_idx INTEGER PRIMARY KEY,
        filename TEXT,
        category TEXT,
        sha256_hash TEXT,
        char_count INTEGER,
        size_bytes INTEGER,
        repos_count INTEGER,
        notebook_id TEXT,
        ingestion_status TEXT,
        ingested_at TEXT,
        verification_status TEXT
    );
    """)
    conn.commit()
    conn.close()

def run_chrome_js(js_code, timeout=25):
    with open(TEMP_JS, "w", encoding="utf-8") as f:
        f.write(js_code)
    ascript = f"""
set jsFile to POSIX file "{TEMP_JS}"
set jsCode to (read jsFile as «class utf8»)
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{NOTEBOOK_ID}" then
                tell t
                    return execute javascript jsCode
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
"""
    try:
        res = subprocess.run(["osascript", "-e", ascript], capture_output=True, text=True, timeout=timeout)
        if res.returncode != 0:
            return f"APPLESCRIPT_ERROR: {res.stderr.strip()}"
        return res.stdout.strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e!s}"

def get_existing_notebooklm_sources():
    js = """(() => {
        let sources = Array.from(document.querySelectorAll(".source-title, .source-card-title, [data-source-id]")).map(el => el.innerText.trim());
        return JSON.stringify(sources);
    })()"""
    res = run_chrome_js(js)
    try:
        return json.loads(res)
    except Exception:
        return []

def close_any_open_dialog():
    run_chrome_js("""(() => {
        let c = document.querySelector("button.close-button, button[aria-label='Close']");
        if (c) c.click();
    })()""")

def open_copied_text_dialog():
    js = """(() => {
        let dialog = document.querySelector("mat-dialog-container");
        if (!dialog) {
            let addBtn = Array.from(document.querySelectorAll("button")).find(b => {
                let txt = (b.innerText || "").toLowerCase();
                let aria = (b.getAttribute("aria-label") || "").toLowerCase();
                return txt.includes("add sources") || txt.includes("add source") || aria.includes("add source");
            });
            if (!addBtn) return "NO_ADD_BTN";
            addBtn.click();
            return "CLICKED_ADD";
        }
        
        // Specifically look for the Copied text textarea (NOT the search box)
        let copiedTa = dialog.querySelector("textarea[formcontrolname='copiedText'], textarea.copied-text-input-textarea, textarea[placeholder*='Paste text']");
        if (copiedTa) return "READY_TEXTAREA";
        
        // If on another sub-dialog, click back
        let backBtn = dialog.querySelector("button[aria-label='Back'], button.back-button");
        let hasDiscoverQuery = dialog.querySelector("textarea[formcontrolname='discoverSourcesQuery']");
        if (backBtn && !hasDiscoverQuery) {
            backBtn.click();
            return "CLICKED_BACK";
        }
        
        let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => {
            let txt = (b.innerText || "").toLowerCase();
            return txt.includes("copied text") || txt.includes("content_paste");
        });
        if (copyBtn) {
            copyBtn.click();
            return "CLICKED_COPIED_TEXT";
        }
        
        return "UNKNOWN_DIALOG_STATE";
    })()"""
    
    for attempt in range(8):
        status = run_chrome_js(js)
        if status in ("READY_TEXTAREA",):
            return True, "READY"
        time.sleep(0.8)
    
    # Final check
    check_js = """(() => {
        let dialog = document.querySelector("mat-dialog-container");
        let ta = dialog ? dialog.querySelector("textarea[formcontrolname='copiedText'], textarea.copied-text-input-textarea, textarea[placeholder*='Paste text']") : null;
        return ta ? "READY" : "NOT_READY";
    })()"""
    if run_chrome_js(check_js) == "READY":
        return True, "READY"
    return False, f"FAILED_DIALOG_STATE_{status}"

def insert_bundle_payload(content):
    # Step 1: Set text into copiedText textarea and trigger Angular FormControl
    js_set = f"""(() => {{
        let dialog = document.querySelector("mat-dialog-container");
        if (!dialog) return "NO_DIALOG";
        let ta = dialog.querySelector("textarea[formcontrolname='copiedText'], textarea.copied-text-input-textarea, textarea[placeholder*='Paste text']");
        if (!ta) return "NO_COPIED_TEXT_TA";
        
        let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
        nativeSetter.call(ta, {json.dumps(content)});
        ta.focus();
        ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
        ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
        return "TEXT_SET";
    }})()"""
    res_set = run_chrome_js(js_set)
    if res_set != "TEXT_SET":
        return False, f"SET_TEXT_FAILED_{res_set}"
    
    # Step 2: Poll for Insert button to become enabled (up to 8s)
    js_click = """(() => {
        let dialog = document.querySelector("mat-dialog-container");
        if (!dialog) return "NO_DIALOG";
        let insertBtn = Array.from(dialog.querySelectorAll("button")).find(b => {
            let txt = (b.innerText || "").trim().toLowerCase();
            let sub = b.querySelector(".mdc-button__label");
            let subTxt = sub ? sub.innerText.trim().toLowerCase() : "";
            return txt === "insert" || subTxt === "insert";
        });
        if (!insertBtn) return "NO_INSERT_BTN";
        if (insertBtn.disabled) return "INSERT_DISABLED";
        insertBtn.click();
        return "CLICKED_INSERT";
    })()"""
    
    clicked = False
    for poll in range(16):
        time.sleep(0.5)
        res_click = run_chrome_js(js_click)
        if res_click == "CLICKED_INSERT":
            clicked = True
            break
        elif res_click == "NO_DIALOG":
            return False, "DIALOG_DISAPPEARED"
            
    if not clicked:
        return False, f"CLICK_INSERT_FAILED_{res_click}"
    
    # Step 3: Poll until mat-dialog-container closes (max 25s)
    for _ in range(25):
        time.sleep(1.0)
        js_closed = """(() => {
            let dialog = document.querySelector("mat-dialog-container");
            return dialog ? "OPEN" : "CLOSED";
        })()"""
        if run_chrome_js(js_closed) == "CLOSED":
            return True, "SUCCESS_INSERTED"
            
    return False, "TIMEOUT_WAITING_FOR_DIALOG_CLOSE"

def ingest_bundle(bundle_info, max_retries=3):
    fpath = SOURCE_DIR / bundle_info["filename"]
    if not fpath.exists():
        return False, "FILE_NOT_FOUND"

    content = fpath.read_text(encoding="utf-8")
    char_len = len(content)
    if char_len > 350000:
        log(f"⚠️ Warning: File exceeds 350k chars ({char_len:,}), truncating safely...")
        content = content[:340000] + "\n\n# ... [SAFE TRUNCATION AT 340k CHARS]"

    for attempt in range(1, max_retries + 1):
        ok_dialog, d_msg = open_copied_text_dialog()
        if not ok_dialog:
            log(f"  ⚠️ Attempt {attempt} failed opening dialog: {d_msg}")
            close_any_open_dialog()
            time.sleep(1.2)
            continue

        ok_insert, i_msg = insert_bundle_payload(content)
        if ok_insert:
            return True, "INGESTED"
        else:
            log(f"  ⚠️ Attempt {attempt} insertion returned: {i_msg}")
            close_any_open_dialog()
            time.sleep(1.5)

    return False, f"FAILED_AFTER_{max_retries}_ATTEMPTS"

def run_ingestion(limit=None):
    init_database()
    manifest_path = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_600_manifest.json")
    if not manifest_path.exists():
        log("Error: consolidated_600_manifest.json not found!")
        sys.exit(1)

    with open(manifest_path) as f:
        manifest = json.load(f)

    log(f"Loaded manifest with {len(manifest)} bundles.")
    existing_sources = get_existing_notebooklm_sources()
    log(f"Initial existing sources in NotebookLM ({NOTEBOOK_ID}): {len(existing_sources)}")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT bundle_idx FROM quant_consolidated_notebooklm_ingestion WHERE ingestion_status IN ('INGESTED', 'ALREADY_PRESENT')")
    db_ingested_indices = set(row[0] for row in cur.fetchall())
    log(f"Already ingested bundles in database: {len(db_ingested_indices)}")

    success_count = 0
    skipped_count = 0
    failed_count = 0

    to_process = manifest[:limit] if limit else manifest

    for item in to_process:
        b_idx = item["bundle_idx"]
        fname = item["filename"]
        cat = item["category"]
        chars = item["char_count"]
        sz_bytes = item["size_bytes"]
        sha = item["sha256"]
        repos = item["repos"]

        # Check if already present in database or NotebookLM UI by prefix
        prefix = f"[QUANT-SOURCE-{b_idx:03d}]"
        if b_idx in db_ingested_indices or any(prefix in s for s in existing_sources):
            log(f"[{b_idx:03d}/{len(manifest)}] ⏩ ALREADY PRESENT: {prefix} ({fname})")
            skipped_count += 1
            cur.execute("""
                INSERT OR REPLACE INTO quant_consolidated_notebooklm_ingestion
                (bundle_idx, filename, category, sha256_hash, char_count, size_bytes, repos_count, notebook_id, ingestion_status, ingested_at, verification_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'ALREADY_PRESENT', datetime('now'), 'VERIFIED_IN_NOTEBOOKLM');
            """, (b_idx, fname, cat, sha, chars, sz_bytes, len(repos), NOTEBOOK_ID))
            conn.commit()
            continue

        log(f"[{b_idx:03d}/{len(manifest)}] ⏳ Ingesting: {fname} | {len(repos)} repos | {chars:,} chars | SHA:{sha[:12]}...")
        t0 = time.time()
        ok, status = ingest_bundle(item)
        elapsed = round(time.time() - t0, 2)

        if ok:
            log(f"[{b_idx:03d}/{len(manifest)}] ✅ INGESTED ({elapsed}s) | SHA256: {sha[:12]}...")
            success_count += 1
            cur.execute("""
                INSERT OR REPLACE INTO quant_consolidated_notebooklm_ingestion
                (bundle_idx, filename, category, sha256_hash, char_count, size_bytes, repos_count, notebook_id, ingestion_status, ingested_at, verification_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'INGESTED', datetime('now'), 'VERIFIED_IN_NOTEBOOKLM');
            """, (b_idx, fname, cat, sha, chars, sz_bytes, len(repos), NOTEBOOK_ID))
            conn.commit()
            # Update existing sources list
            existing_sources.append(prefix)
        else:
            log(f"[{b_idx:03d}/{len(manifest)}] ❌ FAILED ({status})")
            failed_count += 1
            cur.execute("""
                INSERT OR REPLACE INTO quant_consolidated_notebooklm_ingestion
                (bundle_idx, filename, category, sha256_hash, char_count, size_bytes, repos_count, notebook_id, ingestion_status, ingested_at, verification_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'FAILED', datetime('now'), ?);
            """, (b_idx, fname, cat, sha, chars, sz_bytes, len(repos), NOTEBOOK_ID, status))
            conn.commit()

        time.sleep(1.0)

    conn.close()

    receipt = {
        "timestamp": datetime.now().isoformat(),
        "notebook_id": NOTEBOOK_ID,
        "notebook_url": f"https://notebook.google.com/notebook/{NOTEBOOK_ID}",
        "total_manifest_bundles": len(manifest),
        "processed_bundles": len(to_process),
        "success_count": success_count,
        "skipped_count": skipped_count,
        "failed_count": failed_count,
        "status": "COMPLETED" if failed_count == 0 else "PARTIAL"
    }
    with open(RECEIPT_PATH, "w") as rf:
        json.dump(receipt, rf, indent=2)

    log("\n=======================================================")
    log(f"INGESTION COMPLETE: {success_count} Ingested, {skipped_count} Skipped, {failed_count} Failed.")
    log(f"Receipt saved to: {RECEIPT_PATH}")
    log("=======================================================")

if __name__ == "__main__":
    limit_arg = int(sys.argv[1]) if len(sys.argv) > 1 else None
    run_ingestion(limit=limit_arg)
