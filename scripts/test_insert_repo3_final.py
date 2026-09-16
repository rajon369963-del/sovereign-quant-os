import hashlib
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

REPO_FILE = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources/QUANT_REPO_003_ai_trading_bot.txt")
content = REPO_FILE.read_text(encoding="utf-8")
file_size = len(content.encode("utf-8"))
sha = hashlib.sha256(content.encode("utf-8")).hexdigest()

header = f"""# [REPO-003] ai_trading_bot | SHA256:{sha[:12]}
- **Deterministic Cryptographic SHA-256**: `{sha}`
- **Repository Index**: 003 / 290
- **File Name**: `{REPO_FILE.name}`
- **Verification Provenance**: PHYSICAL_DISK_AUTHENTICATED (100% End-to-End Source Code)
- **Local Path**: `{REPO_FILE}`
- **File Size**: {file_size:,d} bytes
- **Timestamp**: {datetime.utcnow().isoformat()}Z

---

"""
payload = header + content

def run_js(js):
    ascript = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "96da7dbf-18e9-40a0-9e90-e363052a247f" then
                tell t
                    return execute javascript {json.dumps(js)}
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
    res = subprocess.run(["osascript", "-e", ascript], capture_output=True, text=True)
    return res.stdout.strip()

# Insert payload using native setter and click Insert
js_insert = f"""(() => {{
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let ta = dialog.querySelector("textarea.copied-text-input-textarea, textarea");
    if (!ta) return "NO_TEXTAREA";
    
    let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
    nativeSetter.call(ta, {json.dumps(payload)});
    
    ta.dispatchEvent(new InputEvent("input", {{ bubbles: true, inputType: "insertText" }}));
    ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
    ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
    
    let btns = Array.from(dialog.querySelectorAll("button"));
    let insertBtn = btns.find(b => b.innerText.trim() === "Insert");
    if (!insertBtn) return "NO_INSERT_BTN";
    if (insertBtn.disabled) return "INSERT_DISABLED";
    
    insertBtn.click();
    return "SUCCESS_CLICKED_INSERT";
}})()"""

res_insert = run_js(js_insert)
print("Insert Result:", res_insert)

# Wait 3 seconds for NotebookLM to process the source
time.sleep(3)

js_sources = """(() => {
    let sources = Array.from(document.querySelectorAll(".source-title")).map(el => el.innerText.trim());
    return JSON.stringify({count: sources.length, sources: sources});
})()"""
print("Sources in NotebookLM:", run_js(js_sources))
