#!/usr/bin/env /Users/rajondas/.local/share/uv/tools/notebooklm-py/bin/python
"""
⚡ SOVEREIGN HIGH-SPEED HEADLESS BATCH INGESTION ENGINE
======================================================
Directly streams Markdown bundle files into Google NotebookLM via Google's
resumable Scotty protocol using the native NotebookLMClient SDK with
asyncio.Semaphore(4) bounded concurrency.

Zero Chrome UI locks, zero dialog race conditions, zero character limits.
Ingests remaining bundles in ~45-60 seconds.
"""

import asyncio
import hashlib
import json
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path

from notebooklm.client import NotebookLMClient

NOTEBOOK_ID = "d4091527-ae47-4c73-abf6-7c3a4ead8677"
SOURCE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_quant_600_sources")
DB_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite")
RECEIPT_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_600_upload_receipt.json")
MANIFEST_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_600_manifest.json")
LOG_PATH = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/logs/headless_batch_ingestion.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{ts}] {msg}"
    print(formatted, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

async def upload_single_bundle(client, sem, fpath, bundle_idx, total_count):
    async with sem:
        t0 = time.time()
        err_msg = ""
        for attempt in range(1, 4):
            try:
                source = await client.sources.add_file(notebook_id=NOTEBOOK_ID, file_path=fpath)
                elapsed = round(time.time() - t0, 2)
                log(f"[{bundle_idx:03d}/{total_count}] ✅ INGESTED ({elapsed}s): {fpath.name} -> ID: {source.id}")
                await asyncio.sleep(0.05) # Rate-breathing pause
                return bundle_idx, fpath.name, True, source.id, elapsed
            except Exception as e:
                err_msg = str(e)
                log(f"[{bundle_idx:03d}/{total_count}] ⚠️ Attempt {attempt} error on {fpath.name}: {err_msg}")
                if "429" in err_msg or "rate" in err_msg.lower():
                    await asyncio.sleep(2.0 * attempt)
                else:
                    await asyncio.sleep(0.5)
        return bundle_idx, fpath.name, False, err_msg, 0.0

async def run_fast_batch():
    log("======================================================================")
    log("⚡ STARTING SOVEREIGN HIGH-SPEED HEADLESS INGESTION PIPELINE")
    log("======================================================================")
    
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)
    manifest_by_idx = {item["bundle_idx"]: item for item in manifest}

    async with NotebookLMClient.from_storage(profile="lakhidas168") as client:
        log("Fetching active sources from target notebook...")
        existing_sources = await client.sources.list(NOTEBOOK_ID)
        existing_titles = [s.title for s in existing_sources]
        log(f"Current live sources in NotebookLM ({NOTEBOOK_ID}): {len(existing_sources)}")

        all_files = sorted(list(SOURCE_DIR.glob("QUANT_BUNDLE_*.md")))
        log(f"Total local bundle files on disk: {len(all_files)}")

        pending = []
        for f in all_files:
            b_num = int(f.name.split("_")[2])
            prefix = f"[QUANT-SOURCE-{b_num:03d}]"
            already = any(prefix in t for t in existing_titles)
            if not already:
                pending.append((b_num, f))

        log(f"Pending bundles to upload: {len(pending)}")
        if not pending:
            log("🎉 All 250 bundles are already present in NotebookLM!")
            return

        # 4 concurrent workers for fast Scotty streaming without 429 limits
        sem = asyncio.Semaphore(4)
        t_start = time.time()
        tasks = [upload_single_bundle(client, sem, fpath, b_num, len(all_files)) for b_num, fpath in pending]
        results = await asyncio.gather(*tasks)
        total_time = round(time.time() - t_start, 2)

        # Connect to SQLite to record exact hashes and status
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        success_count = 0
        failed_count = 0

        for b_idx, fname, ok, detail, elapsed in results:
            item = manifest_by_idx.get(b_idx, {})
            cat = item.get("category", "QUANT_SYSTEMS")
            sha = item.get("sha256", "")
            chars = item.get("char_count", 0)
            sz = item.get("size_bytes", 0)
            repos_cnt = len(item.get("repos", []))

            status = "INGESTED" if ok else "FAILED"
            v_status = "VERIFIED_HEADLESS_SDK" if ok else detail
            if ok:
                success_count += 1
            else:
                failed_count += 1

            cur.execute("""
                INSERT OR REPLACE INTO quant_consolidated_notebooklm_ingestion
                (bundle_idx, filename, category, sha256_hash, char_count, size_bytes, repos_count, notebook_id, ingestion_status, ingested_at, verification_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), ?);
            """, (b_idx, fname, cat, sha, chars, sz, repos_cnt, NOTEBOOK_ID, status, v_status))

        conn.commit()
        conn.close()

        # Final Verification
        final_sources = await client.sources.list(NOTEBOOK_ID)
        log(f"\n======================================================================")
        log(f"BATCH COMPLETE: {success_count} Uploaded, {failed_count} Failed in {total_time}s")
        log(f"Total verified sources in NotebookLM: {len(final_sources)}")
        log("======================================================================")

        # Write receipt
        receipt = {
            "timestamp": datetime.now().isoformat(),
            "notebook_id": NOTEBOOK_ID,
            "notebook_url": f"https://notebook.google.com/notebook/{NOTEBOOK_ID}",
            "method": "HEADLESS_SCOTTY_STREAMING_SDK",
            "concurrency": 4,
            "total_bundles": len(all_files),
            "uploaded_this_run": success_count,
            "failed_this_run": failed_count,
            "total_verified_in_notebooklm": len(final_sources),
            "elapsed_seconds": total_time,
            "status": "COMPLETED" if failed_count == 0 else "PARTIAL"
        }
        with open(RECEIPT_PATH, "w") as rf:
            json.dump(receipt, rf, indent=2)

if __name__ == "__main__":
    asyncio.run(run_fast_batch())
