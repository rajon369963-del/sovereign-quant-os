import json
import subprocess
import time
from pathlib import Path

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"
fp = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources/QUANT_REPO_001_dhanhq_ecosystem.txt")
content = fp.read_text(encoding="utf-8")
title = "QUANT_REPO_001 [8f16f93d]: dhanhq_ecosystem (FULL CODE)"

def run_js(js):
    apple_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if (URL of t) contains "{NOTEBOOK_ID}" then
                    tell t
                        return execute javascript {json.dumps(js)}
                    end tell
                end if
            end repeat
        end repeat
        return "TAB_NOT_FOUND"
    end tell
    '''
    res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    return res.stdout.strip()

# 1. Close any open dialog first
close_open_dialog = """
(() => {
    let closeBtn = document.querySelector("mat-dialog-container button[aria-label*='Close' i], mat-dialog-container button[mat-dialog-close]");
    if (closeBtn) closeBtn.click();
    let backdrop = document.querySelector(".cdk-overlay-backdrop");
    if (backdrop) backdrop.click();
    return "CLOSED";
})()
"""
print("[0] Reset Dialogs:", run_js(close_open_dialog))
time.sleep(1.0)

# 2. Click Add source button
click_add = """
(() => {
    let btn = Array.from(document.querySelectorAll("button")).find(b => 
        (b.innerText || "").toLowerCase().includes("add source") ||
        (b.getAttribute("aria-label") || "").toLowerCase().includes("add source")
    );
    if (!btn) return "NO_ADD_BTN";
    btn.click();
    return "CLICKED_ADD";
})()
"""
print("[1] Click Add Source:", run_js(click_add))
time.sleep(1.2)

# 3. Click Copied text button
click_copied = """
(() => {
    let dialog = document.querySelector("mat-dialog-container, [role=dialog]");
    if (!dialog) return "NO_DIALOG";
    let btn = Array.from(dialog.querySelectorAll("button")).find(b => 
        (b.innerText || "").toLowerCase().includes("copied text")
    );
    if (!btn) return "NO_COPIED_BTN";
    btn.click();
    return "CLICKED_COPIED";
})()
"""
print("[2] Click Copied Text:", run_js(click_copied))
time.sleep(1.2)

# 4. Stream content in 150 KB chunks into window.__upload_buffer
print("[3] Streaming content in chunks into browser V8 memory...")
run_js("window.__upload_buffer = '';")
CHUNK_SIZE = 150000
chunks = [content[i:i+CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]
for i, chunk in enumerate(chunks):
    res = run_js(f"window.__upload_buffer += {json.dumps(chunk)}; window.__upload_buffer.length;")
    print(f"    Chunk {i+1}/{len(chunks)} injected. Total length in V8: {res}")

# 5. Set Title and assign buffer to textarea
inject_buffer = f"""
(() => {{
    let titleInput = document.querySelector("input[type=text], input[placeholder*='Title' i], input[aria-label*='Title' i]");
    let ta = document.querySelector("textarea[aria-label='Pasted text' i]");
    if (!ta) return "NO_TEXTAREA";
    
    if (titleInput) {{
        titleInput.focus();
        let valSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        valSetter.call(titleInput, {json.dumps(title)});
        titleInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
        titleInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
    }}
    
    ta.focus();
    let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
    nativeSetter.call(ta, window.__upload_buffer);
    ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
    ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
    
    let injectedLen = ta.value.length;
    window.__upload_buffer = null; // Clean memory
    return "INJECTED_CHARS_" + injectedLen;
}})()
"""
print("[4] Assign Buffer to Textarea:", run_js(inject_buffer))
time.sleep(1.0)

# 6. Click Insert button
click_insert = """
(() => {
    let dialog = document.querySelector("mat-dialog-container, [role=dialog]");
    if (!dialog) return "NO_DIALOG";
    let btn = Array.from(dialog.querySelectorAll("button")).find(b => 
        (b.innerText || "").trim().toLowerCase() === "insert" && !b.disabled
    );
    if (!btn) return "NO_ENABLED_INSERT";
    btn.click();
    return "CLICKED_INSERT";
})()
"""
print("[5] Click Insert:", run_js(click_insert))

# 7. Wait for ingestion
print("[6] Waiting for ingestion...")
time.sleep(6.0)

check_count = """
(() => {
    let containers = Array.from(document.querySelectorAll(".single-source-container"));
    return JSON.stringify({
        totalSources: containers.length,
        titles: containers.slice(0, 5).map(c => (c.innerText || "").split("\\n")[0])
    });
})()
"""
print("[7] Status after upload:", run_js(check_count))
