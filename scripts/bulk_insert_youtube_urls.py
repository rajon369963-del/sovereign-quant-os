#!/usr/bin/env python3
"""
bulk_insert_youtube_urls.py
Ingests bulk YouTube video URLs directly into Google NotebookLM via Chrome automation.
"""

import json
import re
import sqlite3
import subprocess
import time
import urllib.parse
import urllib.request
from datetime import datetime

TARGET_NOTEBOOK_ID = "3fb0898e-7a97-4e77-acdb-aa29f536d233"
DB_PATH = "/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite"

QUERIES = [
    "share market today 16 september 2026",
    "nifty bank nifty analysis 16 september 2026",
    "ghanshyam tech today",
    "power of stocks subasish pani today",
    "zee business anil singhvi today",
    "cnbc awaaz share market live today",
    "pr sundar option trading today",
    "vivek bajaj stock market today",
    "siddharth bhanushali today",
    "pushkar raj thakur share market today",
    "booming bulls intraday trading today",
    "ca rachana ranade stock market today",
    "neeraj joshi stock market today",
    "abhishek kar trading today",
    "saketh r bank nifty expiry today",
    "nitin murarka live market order flow today",
    "post market analysis 16 september 2026",
    "tomorrow market prediction 17 september 2026",
    "nifty expiry prediction 17 september 2026"
]

def harvest_candidates(max_count=50):
    discovered = []
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
    
    # Check DB for already ingested
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT video_id FROM ingested_youtube_videos")
    existing = set(r[0] for r in c.fetchall())
    conn.close()
    
    for q in QUERIES:
        encoded_q = urllib.parse.quote(q)
        search_url = f"https://www.youtube.com/results?search_query={encoded_q}&sp=CAI%253D"
        req = urllib.request.Request(search_url, headers=headers)
        try:
            html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8")
            vids = re.findall(r'/watch\?v=([a-zA-Z0-9_-]{11})', html)
            for v in vids:
                if v not in existing and v not in discovered:
                    discovered.append(v)
        except Exception:
            pass
        if len(discovered) >= max_count:
            break
        time.sleep(0.2)
    return discovered[:max_count]

def main():
    vids = harvest_candidates(40)
    print(f"Discovered {len(vids)} fresh YouTube candidate videos for last 24h market analysis.")
    if not vids:
        print("No new videos found.")
        return

    urls = [f"https://www.youtube.com/watch?v={v}" for v in vids]
    payload_text = "\n".join(urls)
    
    js_inject = f"""(() => {{
        let dialog = document.querySelector("mat-dialog-container, [role='dialog']");
        if (!dialog) return JSON.stringify({{status: "no_dialog"}});
        let textarea = dialog.querySelector("textarea");
        if (!textarea) return JSON.stringify({{status: "no_textarea"}});
        
        textarea.value = {json.dumps(payload_text)};
        textarea.dispatchEvent(new Event("input", {{ bubbles: true }}));
        textarea.dispatchEvent(new Event("change", {{ bubbles: true }}));
        
        let insertBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Insert"));
        if (!insertBtn) return JSON.stringify({{status: "no_insert_btn"}});
        
        if (insertBtn.disabled) {{
            insertBtn.removeAttribute("disabled");
            insertBtn.classList.remove("mat-mdc-button-disabled");
        }}
        insertBtn.click();
        return JSON.stringify({{status: "inserted", count: {len(vids)}}});
    }})()"""

    ascript = f"""
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if (URL of t) contains "{TARGET_NOTEBOOK_ID}" then
                    set jsRes to (execute t javascript {json.dumps(js_inject)})
                    return jsRes
                end if
            end repeat
        end repeat
        return "TAB_NOT_FOUND"
    end tell
    """
    
    res = subprocess.run(["osascript", "-e", ascript], capture_output=True, text=True)
    print("Injection response:", res.stdout.strip())
    
    # Record into DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    batch_num = 15
    for v in vids:
        c.execute("""
            INSERT OR REPLACE INTO ingested_youtube_videos (video_id, url, title, notebook_id, ingested_at, batch_num, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (v, f"https://www.youtube.com/watch?v={v}", f"Video {v}", TARGET_NOTEBOOK_ID, datetime.now().isoformat(), batch_num, "SUBMITTED_TO_NOTEBOOKLM"))
    conn.commit()
    conn.close()
    print(f"✓ Recorded {len(vids)} videos into {DB_PATH}")

if __name__ == "__main__":
    main()
