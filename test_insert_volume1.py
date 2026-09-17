#!/usr/bin/env python3
"""
test_insert_volume1.py
======================
Tests inserting Volume 01 into the active NotebookLM notebook (96da7dbf-18e9-40a0-9e90-e363052a247f)
via Chrome AppleScript JavaScript injection.
"""

import json
import subprocess
from pathlib import Path

SOURCE_FILE = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/notebooklm_200_quant_repos_sources/01_HFT_EVENT_DRIVEN.md")
TITLE = "01_HFT_EVENT_DRIVEN: NautilusTrader & C++20 Gateways"

with open(SOURCE_FILE, "r", encoding="utf-8") as f:
    text_content = f.read()

escaped_text = json.dumps(text_content)
escaped_title = json.dumps(TITLE)

js_script = f"""
(function() {{
    let dialog = document.querySelector("mat-dialog-container, [role=\\\"dialog\\\"]");
    if (!dialog) return "ERROR: No dialog found";
    
    let titleInput = dialog.querySelector("input[type=\\\"text\\\"]");
    let textArea = dialog.querySelector("textarea[aria-label=\\\"Pasted text\\\"], textarea");
    
    if (!textArea) return "ERROR: No textarea found";
    
    if (titleInput) {{
        titleInput.value = {escaped_title};
        titleInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
        titleInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
    }}
    
    textArea.value = {escaped_text};
    textArea.dispatchEvent(new Event("input", {{ bubbles: true }}));
    textArea.dispatchEvent(new Event("change", {{ bubbles: true }}));
    
    let btns = Array.from(dialog.querySelectorAll("button"));
    let insertBtn = btns.find(b => b.innerText.trim() === "Insert");
    
    if (!insertBtn) return "ERROR: Insert button not found";
    if (insertBtn.disabled) return "ERROR: Insert button is still disabled";
    
    insertBtn.click();
    return "SUCCESS: Clicked Insert for " + {escaped_title};
}})();
"""

apple_script = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "96da7dbf-18e9-40a0-9e90-e363052a247f" then
                tell t
                    return execute javascript {json.dumps(js_script)}
                end tell
            end if
        end repeat
    end repeat
    return "NOTEBOOK_TAB_NOT_FOUND"
end tell
'''

cmd = ["osascript", "-e", apple_script]
res = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", res.stdout.strip())
print("STDERR:", res.stderr.strip())
