import hashlib
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"
TEMP_JS = "/tmp/repo8.js"
TEMP_SCPT = "/tmp/repo8.applescript"

def run_js(js):
    with open(TEMP_JS, "w", encoding="utf-8") as f:
        f.write(js)
    ascript = f'''
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
'''
    with open(TEMP_SCPT, "w", encoding="utf-8") as f:
        f.write(ascript)
    res = subprocess.run(["osascript", TEMP_SCPT], capture_output=True, text=True)
    return res.stdout.strip()

source_dir = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources")
files = sorted(list(source_dir.glob("QUANT_REPO_008_*.txt")))
repo_file = files[0]
raw_content = repo_file.read_text(encoding="utf-8")
file_size = len(raw_content.encode("utf-8"))
sha256 = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
clean_name = "algo_trading_strategies_india"

header = f"""# [REPO-008] {clean_name} | SHA256:{sha256[:12]}
- **Deterministic Cryptographic SHA-256**: `{sha256}`
- **Repository Index**: 008 / 290
- **File Name**: `{repo_file.name}`
- **Verification Provenance**: PHYSICAL_DISK_AUTHENTICATED (100% End-to-End Source Code)
- **Local Path**: `{repo_file}`
- **File Size**: {file_size:,d} bytes
- **Timestamp**: {datetime.utcnow().isoformat()}Z

---

"""
payload = header + raw_content

# Step 1: Ensure on Copied Text
js_step1 = """(() => {
    document.querySelectorAll("emoji-keyboard, .emoji-keyboard__container").forEach(el => el.remove());
    let tab = Array.from(document.querySelectorAll(".mdc-tab")).find(t => t.innerText.includes("Sources"));
    if (tab && !tab.classList.contains("mdc-tab--active")) tab.click();
    
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    let ta = dialog ? dialog.querySelector("textarea.copied-text-input-textarea, textarea[aria-label='Pasted text']") : null;
    let insertBtn = dialog ? Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "Insert") : null;
    if (ta && insertBtn) return "READY_TEXTAREA";
    
    if (!dialog) {
        let addBtn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").includes("Add source") || b.getAttribute("aria-label") === "Add source");
        if (!addBtn) return "NO_ADD_BTN";
        addBtn.click();
        return "CLICKED_ADD";
    }
    
    let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
    if (copyBtn) {
        copyBtn.click();
        return "CLICKED_COPIED_TEXT";
    }
    return "UNKNOWN_DIALOG";
})()"""

res1 = run_js(js_step1)
print("Step 1 (dialog prep):", res1)
time.sleep(0.35)

if res1 in ("CLICKED_ADD", "UNKNOWN_DIALOG"):
    js_click_copy = """(() => {
        let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
        if (!dialog) return "NO_DIALOG";
        let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
        if (!copyBtn) return "NO_COPY_BTN";
        copyBtn.click();
        return "CLICKED_COPY_AFTER_ADD";
    })()"""
    print("Click Copied Text:", run_js(js_click_copy))
    time.sleep(0.35)

# Step 2: Populate textarea
js_pop = f"""(() => {{
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let ta = dialog.querySelector("textarea.copied-text-input-textarea, textarea[aria-label='Pasted text']");
    if (!ta) return "NO_COPIED_TEXTAREA";
    
    let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
    nativeSetter.call(ta, {json.dumps(payload)});
    
    ta.focus();
    ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
    ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
    
    document.execCommand("insertText", false, " ");
    return "POPULATED_LEN_" + ta.value.length;
}})()"""
print("Step 2 (populate):", run_js(js_pop))

time.sleep(0.35)

# Step 3: Click Insert
js_insert = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let insertBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "Insert");
    if (!insertBtn) return "NO_INSERT_BTN";
    if (insertBtn.disabled) return "INSERT_DISABLED";
    insertBtn.click();
    return "SUCCESS_INSERTED";
})()"""
res3 = run_js(js_insert)
print("Step 3 (insert):", res3)
time.sleep(2.0)

# Step 4: Verify sources count
js_verify = """(() => {
    let sources = Array.from(document.querySelectorAll(".source-title")).map(el => el.innerText.trim());
    return JSON.stringify({count: sources.length, sources: sources});
})()"""
print("Sources count:", run_js(js_verify))
