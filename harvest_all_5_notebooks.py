#!/usr/bin/env python3
"""
⚡ MASTER HARVESTER ACROSS ALL 5 NOTEBOOKLM NOTEBOOKS
Extracts sources, metadata, and summaries from:
1. 15th sept share market (dd85a383-7151-4f9d-bea0-c6424d4204bc)
2. SHARE MARKET MONTHLY NEWS 2 (1d3cc23f-fa96-42ee-a93a-8cfb47bcc1f1)
3. SHARE MARKET MONTHLY NEWS 1 (b3cb05f5-ebe4-449f-b7a1-28aa9a00eadf)
4. SHARE MARKET WEEKLY NEWS PART 2 (eac2d0d6-3e7b-4747-aa75-a54ad02898bf)
5. SHARE MARKET WEEKLY NEWS PART1 (25f4fae0-55df-444b-8197-33ae7c4bd876)
"""

import json
import subprocess
import time
from pathlib import Path

TARGET_NOTEBOOKS = [
    {"id": "dd85a383-7151-4f9d-bea0-c6424d4204bc", "title": "15th sept share market", "expected": 279},
    {"id": "1d3cc23f-fa96-42ee-a93a-8cfb47bcc1f1", "title": "SHARE MARKET MONTHLY NEWS 2", "expected": 300},
    {"id": "b3cb05f5-ebe4-449f-b7a1-28aa9a00eadf", "title": "SHARE MARKET MONTHLY NEWS 1", "expected": 292},
    {"id": "eac2d0d6-3e7b-4747-aa75-a54ad02898bf", "title": "SHARE MARKET WEEKLY NEWS PART 2", "expected": 299},
    {"id": "25f4fae0-55df-444b-8197-33ae7c4bd876", "title": "SHARE MARKET WEEKLY NEWS PART1", "expected": 290}
]

BASE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os")
HARVEST_DIR = BASE_DIR / "harvested_5_notebooks"
HARVEST_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = BASE_DIR / "grand_10k_trading_hypergraph.sqlite"

def execute_js_on_chrome(js_code: str):
    clean_js = js_code.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
    as_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "notebook.google.com" or URL of t contains "notebooklm.google.com" then
                    tell t
                        return execute javascript "{clean_js}"
                    end tell
                end if
            end repeat
        end repeat
        return "NO_TAB"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', as_script], capture_output=True, text=True)
    return res.stdout.strip()

def navigate_chrome(url: str):
    as_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "notebook.google.com" or URL of t contains "notebooklm.google.com" then
                    set URL of t to "{url}"
                    return "NAVIGATED"
                end if
            end repeat
        end repeat
        return "NO_TAB"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', as_script], capture_output=True, text=True)
    return res.stdout.strip()

def extract_sources_from_current_page():
    # Wait for DOM
    js_extract = """
    (function() {
        let items = Array.from(document.querySelectorAll('.source-item, [role="listitem"], .mat-mdc-list-item, .source-card, [data-source-id]'));
        let sources = [];
        for (let it of items) {
            let titleEl = it.querySelector('.source-title, .title, .mdc-list-item__primary-text, span, div');
            let title = titleEl ? titleEl.innerText.trim() : it.innerText.trim().split('\\n')[0];
            let sub = it.innerText.trim();
            if (title && title.length > 2 && !title.includes('Add source') && !title.includes('Select all')) {
                sources.push({
                    title: title,
                    full_text: sub.slice(0, 300)
                });
            }
        }
        return JSON.stringify({
            count: sources.length,
            sources: sources
        });
    })()
    """
    return execute_js_on_chrome(js_extract)

def main():
    print("🚀 Starting Master Harvester across all 5 Notebooks...")
    all_harvested = {}
    
    for nb in TARGET_NOTEBOOKS:
        url = f"https://notebook.google.com/notebook/{nb['id']}"
        print(f"\n--- Navigating to: {nb['title']} ({nb['id']}) ---")
        nav_res = navigate_chrome(url)
        print("Nav result:", nav_res)
        time.sleep(5) # Allow page to load
        
        # Extract sources
        raw_res = extract_sources_from_current_page()
        try:
            data = json.loads(raw_res)
            print(f"✅ Extracted {data.get('count', 0)} sources from {nb['title']}")
            all_harvested[nb['id']] = {
                "title": nb['title'],
                "count": data.get('count', 0),
                "sources": data.get('sources', [])
            }
            # Save raw json
            nb_out = HARVEST_DIR / f"sources_{nb['id']}.json"
            with open(nb_out, "w", encoding="utf-8") as f:
                json.dump(all_harvested[nb['id']], f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error parsing sources for {nb['id']}: {e}, Raw: {raw_res[:100]}")
            
    print("\n🏁 Harvest pass complete! Total notebooks checked:", len(all_harvested))

if __name__ == "__main__":
    main()
