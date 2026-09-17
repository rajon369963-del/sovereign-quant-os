#!/usr/bin/env python3
import json
import subprocess
import time
from pathlib import Path

NOTEBOOKS = [
    ("04_SAKETH_R", "279ad740-9e0d-4e00-a713-a72cffb62a3f"),
    ("05_NITIN_MURARKA", "e5d3eb8c-1492-4670-a4e3-08a5b2fb0f6d"),
    ("06_PR_SUNDAR", "0f2a60f3-294a-473b-a8a1-36a983e05d3c"),
    ("07_DR_MUKUL_AGRAWAL", "a1903e26-f589-42ff-ac02-132bcd02115d"),
    ("08_SIDDHARTH_BHANUSHALI", "3884d9e5-c21c-4646-82c9-e4500427f102"),
    ("09_ABHISHEK_KAR", "31fa34c1-8a6e-4ebc-b7ae-3d416e215594"),
    ("QUANT_GITHUB_REPOS", "96da7dbf-18e9-40a0-9e90-e363052a247f")
]

RESULTS_FILE = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/ALL_9_YOUTUBERS_LIVE_NOTEBOOKLM_RESPONSES.json")

with open(RESULTS_FILE) as f:
    responses = json.load(f)

for name, nb_id in NOTEBOOKS:
    print(f"\n==========================================")
    print(f"[*] Extracting {name} ({nb_id})...")
    
    as_code = f'''
    tell application "Google Chrome"
        repeat with w in windows
            set idx to 1
            repeat with t in tabs of w
                if URL of t contains "{nb_id}" then
                    set active tab index of w to idx
                    delay 0.8
                    tell t
                        return execute javascript "document.body.innerText"
                    end tell
                end if
                set idx to idx + 1
            end repeat
        end repeat
        return "TAB_NOT_FOUND"
    end tell
    '''
    
    try:
        res = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True, timeout=8)
        body = res.stdout.strip()
        print(f"  Length of body: {len(body)}")
        if len(body) > 1500:
            # Capture the last 7,000 characters which contain the AI responses and chat turns
            snippet = body[-7000:]
            responses[name] = {
                "notebook_id": nb_id,
                "name": name,
                "response": snippet,
                "length": len(snippet),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"  [+] Saved {len(snippet)} chars for {name}!")
            with open(RESULTS_FILE, "w", encoding="utf-8") as f:
                json.dump(responses, f, indent=2)
        else:
            print(f"  [-] Incomplete body for {name}")
    except Exception as e:
        print(f"  [!] Error: {e}")

print("\n[✓] Fast extraction complete!")
