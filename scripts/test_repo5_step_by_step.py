import hashlib
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"
repo_file = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources/QUANT_REPO_005_algo-trading-in-india.txt")
raw_content = repo_file.read_text(encoding="utf-8")
file_size = len(raw_content.encode("utf-8"))
sha256 = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
clean_name = "algo-trading-in-india"

header = f"""# [REPO-005] {clean_name} | SHA256:{sha256[:12]}
- **Deterministic Cryptographic SHA-256**: `{sha256}`
- **Repository Index**: 005 / 290
- **File Name**: `{repo_file.name}`
- **Verification Provenance**: PHYSICAL_DISK_AUTHENTICATED (100% End-to-End Source Code)
- **Local Path**: `{repo_file}`
- **File Size**: {file_size:,d} bytes
- **Timestamp**: {datetime.utcnow().isoformat()}Z

---

"""
full_payload = header + raw_content

def run_js(js):
    temp_js = "/tmp/test_curr_task.js"
    with open(temp_js, "w", encoding="utf-8") as f:
        f.write(js)
    
    ascript = f'''
set jsFile to POSIX file "{temp_js}"
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
'''
    res = subprocess.run(["osascript", "-e", ascript], capture_output=True, text=True)
    if res.stderr.strip():
        print("AppleScript STDERR:", res.stderr.strip())
    return res.stdout.strip()

# Check dialog
js_state = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    let ta = dialog ? dialog.querySelector("textarea") : null;
    let copyBtn = dialog ? Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text")) : null;
    let insertBtn = dialog ? Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "Insert") : null;
    return JSON.stringify({
        hasDialog: !!dialog,
        hasTa: !!ta,
        hasCopyBtn: !!copyBtn,
        hasInsertBtn: !!insertBtn,
        insertDisabled: insertBtn ? insertBtn.disabled : null
    });
})()"""
print("Initial State:", run_js(js_state))

# Set payload into textarea and inspect
js_set = f"""(() => {{
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let ta = dialog.querySelector("textarea.copied-text-input-textarea, textarea");
    if (!ta) return "NO_TA";
    
    let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
    nativeSetter.call(ta, {json.dumps(full_payload)});
    
    ta.focus();
    ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
    ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
    
    document.execCommand("insertText", false, " ");
    
    let btns = Array.from(dialog.querySelectorAll("button"));
    let insertBtn = btns.find(b => b.innerText.trim() === "Insert");
    
    return JSON.stringify({{
        taLen: ta.value.length,
        taClasses: ta.className,
        insertFound: !!insertBtn,
        insertDisabled: insertBtn ? insertBtn.disabled : null
    }});
}})()"""
print("Set Payload Result:", run_js(js_set))

# Now click Insert
js_click = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let insertBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "Insert");
    if (!insertBtn) return "NO_INSERT_BTN";
    if (insertBtn.disabled) return "INSERT_DISABLED";
    insertBtn.click();
    return "CLICKED_INSERT_SUCCESS";
})()"""
print("Click Insert Result:", run_js(js_click))

time.sleep(2.5)

js_sources = """(() => {
    let sources = Array.from(document.querySelectorAll(".source-title")).map(el => el.innerText.trim());
    return JSON.stringify({count: sources.length, sources: sources});
})()"""
print("Sources after REPO-005:", run_js(js_sources))
