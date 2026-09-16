import json
import subprocess
import time

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"
TEMP_JS = "/tmp/limit_test.js"
TEMP_SCPT = "/tmp/limit_test.applescript"

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

# Step 1: Open fresh dialog and go to Copied text
js_open = """(() => {
    // Close any open dialogs first
    let closeBtn = document.querySelector("button[aria-label='Close'], button.close-button");
    if (closeBtn) closeBtn.click();
    
    let tab = Array.from(document.querySelectorAll(".mdc-tab")).find(t => t.innerText.includes("Sources"));
    if (tab && !tab.classList.contains("mdc-tab--active")) tab.click();
    
    let addBtn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").includes("Add source") || b.getAttribute("aria-label") === "Add source");
    if (addBtn) addBtn.click();
    return "CLICKED_ADD";
})()"""
print("Open:", run_js(js_open))
time.sleep(0.5)

js_click_copy = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
    if (!copyBtn) return "NO_COPY_BTN";
    copyBtn.click();
    return "CLICKED_COPY";
})()"""
print("Click Copied Text:", run_js(js_click_copy))
time.sleep(0.5)

# Test various character lengths
for length in [10000, 50000, 100000, 200000, 300000, 400000, 500000, 600000, 700000]:
    text = "# [TEST] Length Test\n\n" + ("a" * (length - 25))
    js_set = f"""(() => {{
        let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
        let ta = dialog ? dialog.querySelector("textarea.copied-text-input-textarea, textarea[aria-label='Pasted text']") : null;
        if (!ta) return "NO_TA";
        
        let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
        nativeSetter.call(ta, {json.dumps(text)});
        ta.focus();
        ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
        ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
        document.execCommand("insertText", false, " ");
        return "SET";
    }})()"""
    run_js(js_set)
    time.sleep(0.3)
    
    js_check = """(() => {
        let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
        let insertBtn = dialog ? Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "Insert") : null;
        let ta = dialog ? dialog.querySelector("textarea.copied-text-input-textarea, textarea[aria-label='Pasted text']") : null;
        return JSON.stringify({
            chars: ta ? ta.value.length : 0,
            classes: ta ? ta.className : "",
            insertDisabled: insertBtn ? insertBtn.disabled : null
        });
    })()"""
    status = run_js(js_check)
    print(f"Length {length:>7d} -> {status}")
