#!/usr/bin/env python3
import subprocess
import json
import time
from pathlib import Path

NOTEBOOK_ID = "d4091527-ae47-4c73-abf6-7c3a4ead8677"
bundle_file = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/consolidated_quant_600_sources/QUANT_BUNDLE_001_INDIAN_BROKERS_DHAN_KITE_FYERS.md")
content = bundle_file.read_text(encoding="utf-8")
temp_js = "/tmp/run_bundle1.js"

def run_js(js):
    with open(temp_js, "w", encoding="utf-8") as f:
        f.write(js)
    ascript = f"""
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
"""
    p = subprocess.run(["osascript", "-e", ascript], capture_output=True, text=True)
    return p.stdout.strip()

# Step 1: Open Add sources dialog if not open
js_open = """(() => {
    let dialog = document.querySelector("mat-dialog-container");
    if (dialog) return "DIALOG_ALREADY_OPEN";
    let addBtn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").includes("Add sources") || b.getAttribute("aria-label") === "Add source");
    if (!addBtn) return "NO_ADD_BTN";
    addBtn.click();
    return "CLICKED_ADD";
})()"""
print("Step 1 (Open Add):", run_js(js_open))
time.sleep(0.8)

# Step 2: Click Copied text
js_copy = """(() => {
    let dialog = document.querySelector("mat-dialog-container");
    if (!dialog) return "NO_DIALOG";
    let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
    if (!copyBtn) return "NO_COPY_BTN";
    copyBtn.click();
    return "CLICKED_COPIED_TEXT";
})()"""
print("Step 2 (Click Copied text):", run_js(js_copy))
time.sleep(0.8)

# Step 3: Insert bundle payload
js_insert = f"""(() => {{
    let dialog = document.querySelector("mat-dialog-container");
    if (!dialog) return "NO_DIALOG";
    let ta = dialog.querySelector("textarea");
    if (!ta) return "NO_TA";
    
    let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
    nativeSetter.call(ta, {json.dumps(content)});
    ta.focus();
    ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
    ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
    document.execCommand("insertText", false, " ");
    
    let insertBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "Insert");
    if (!insertBtn) return "NO_INSERT_BTN";
    if (insertBtn.disabled) return "INSERT_DISABLED";
    insertBtn.click();
    return "CLICKED_INSERT";
}})()"""
print("Step 3 (Insert Payload):", run_js(js_insert))

# Step 4: Poll until dialog is closed
for i in range(1, 25):
    time.sleep(1.0)
    js_check = """(() => {
        let dialog = document.querySelector("mat-dialog-container");
        let sources = Array.from(document.querySelectorAll(".source-title, .source-card-title, [data-source-id]")).map(el => el.innerText.trim());
        return JSON.stringify({
            dialogOpen: !!dialog,
            sourcesCount: sources.length,
            sources: sources
        });
    })()"""
    raw = run_js(js_check)
    try:
        res = json.loads(raw)
        d_open = res.get("dialogOpen")
        s_count = res.get("sourcesCount")
        print("  Poll " + str(i) + "s: dialogOpen=" + str(d_open) + ", sourcesCount=" + str(s_count))
        if not d_open and s_count >= 2:
            print("SUCCESS! Bundle 1 successfully inserted into NotebookLM!")
            print("Sources:", res.get("sources"))
            break
    except Exception as e:
        print("  Poll " + str(i) + "s parsing error: " + str(e))
