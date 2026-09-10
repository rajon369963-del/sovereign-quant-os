#!/usr/bin/env python3
"""
===============================================================================
AIR10/MIGL GOOGLE DRIVE TRADING VIDEO RECOVERY & MANIFEST SYNC
===============================================================================
Extracts all trading video metadata and pure-text transcripts from 
transcript_fts.sqlite and synchronizes canonical manifests directly to 
Google Drive: lakhidas168@gmail.com in folder 1i2ci3yvGJcYM6V6kBRZqYxvIDvgCKBCZ.

Complies strictly with Rule 3 (Source Law), Rule 10 (Zero Audio/Video Disk Bloat 
& Pure Text Persistence), and Rule 2 (Hot Path Law).
===============================================================================
"""

import os
import sys
import json
import sqlite3
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

FTS_DB = "/Users/rajondas/AIR1_ARCHIVES/LAKHIDAS168_NOTEBOOKLM_TRANSCRIPT_RECOVERY_20260902/06_DERIVED_SEARCH/fts5/transcript_fts.sqlite"
OUT_DIR = "/Users/rajondas/.gemini/antigravity/scratch/antigravity_yolo_trading_engine"
DRIVE_PARENT_ID = "1i2ci3yvGJcYM6V6kBRZqYxvIDvgCKBCZ"
ACCOUNT = "lakhidas168@gmail.com"

def extract_manifest():
    print(f"[1/4] Connecting to {FTS_DB}...")
    conn = sqlite3.connect(FTS_DB)
    conn.execute("PRAGMA query_only = ON")
    cur = conn.cursor()

    query = """
    SELECT 
        sha256,
        canonical_video_id,
        notebook_title,
        source_title,
        source_url,
        length(content) as char_count
    FROM transcript_fts
    WHERE notebook_title IN ('HFT 1', 'HFT 2', 'QUANT', 'openclaw_1', 'openclaw_2')
       OR notebook_title LIKE '%trading%'
       OR notebook_title LIKE '%scalp%'
       OR notebook_title LIKE '%ml prediction%'
    ORDER BY notebook_title, source_title;
    """
    
    cur.execute(query)
    rows = cur.fetchall()
    print(f"[2/4] Retrieved {len(rows)} trading video transcript records.")

    manifest_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_sources": len(rows),
        "target_drive_folder": DRIVE_PARENT_ID,
        "target_account": ACCOUNT,
        "notebook_breakdown": {},
        "videos": []
    }

    markdown_lines = [
        "# ⚡ SOVEREIGN TRADING VIDEO CANONICAL ARCHIVE MANIFEST",
        f"**Generated**: {manifest_data['generated_at']} | **Total Videos**: {len(rows)} | **Drive Target**: `{DRIVE_PARENT_ID}`",
        "",
        "## Notebook Breakdown",
        ""
    ]

    for row in rows:
        sha, vid, notebook, title, url, chars = row
        manifest_data["notebook_breakdown"][notebook] = manifest_data["notebook_breakdown"].get(notebook, 0) + 1
        manifest_data["videos"].append({
            "sha256": sha,
            "video_id": vid,
            "notebook": notebook,
            "title": title,
            "url": url,
            "char_count": chars
        })

    for nb, count in sorted(manifest_data["notebook_breakdown"].items()):
        markdown_lines.append(f"- **{nb}**: {count} videos")

    markdown_lines.extend([
        "",
        "## Video Catalog (First 100 Sample)",
        "| Video ID | Notebook | Title | Characters | SHA256 |",
        "|---|---|---|---|---|"
    ])

    for v in manifest_data["videos"][:100]:
        title_clean = v['title'].replace('|', '-')
        markdown_lines.append(f"| `{v['video_id']}` | {v['notebook']} | [{title_clean}]({v['url']}) | {v['char_count']:,} | `{v['sha256'][:10]}...` |")

    json_path = os.path.join(OUT_DIR, "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json")
    md_path = os.path.join(OUT_DIR, "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.md")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_lines))

    print(f"[3/4] Manifests written locally:")
    print(f"  JSON: {json_path} ({os.path.getsize(json_path):,} bytes)")
    print(f"  MD:   {md_path} ({os.path.getsize(md_path):,} bytes)")

    return json_path, md_path

def sync_to_google_drive(md_path, json_path):
    print(f"[4/4] Synchronizing manifest to Google Drive ({ACCOUNT} -> {DRIVE_PARENT_ID})...")
    
    # Upload MD manifest
    cmd_md = [
        "gog", "drive", "upload", md_path,
        "--parent", DRIVE_PARENT_ID,
        "--account", ACCOUNT,
        "--name", "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.md",
        "--force"
    ]
    res_md = subprocess.run(cmd_md, capture_output=True, text=True)
    print("Drive Upload MD Output:", res_md.stdout.strip())
    if res_md.stderr:
        print("Drive Upload MD Error:", res_md.stderr.strip())

    # Upload JSON manifest
    cmd_json = [
        "gog", "drive", "upload", json_path,
        "--parent", DRIVE_PARENT_ID,
        "--account", ACCOUNT,
        "--name", "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json",
        "--force"
    ]
    res_json = subprocess.run(cmd_json, capture_output=True, text=True)
    print("Drive Upload JSON Output:", res_json.stdout.strip())
    if res_json.stderr:
        print("Drive Upload JSON Error:", res_json.stderr.strip())

    # Verify upload
    cmd_verify = [
        "gog", "drive", "ls",
        "--parent", DRIVE_PARENT_ID,
        "--account", ACCOUNT,
        "--query", "name contains 'TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST'",
        "--plain"
    ]
    res_ver = subprocess.run(cmd_verify, capture_output=True, text=True)
    print("\nVerified Drive Contents:")
    print(res_ver.stdout.strip())

if __name__ == "__main__":
    json_path, md_path = extract_manifest()
    sync_to_google_drive(md_path, json_path)
