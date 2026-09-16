import json
import subprocess
import time


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

# Step 1: Click "Copied text"
js_click_copied_text = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
    if (!copyBtn) return "NO_COPY_BTN";
    copyBtn.click();
    return "CLICKED_COPIED_TEXT";
})()"""

print("Click Copied Text:", run_js(js_click_copied_text))
time.sleep(1)

# Step 2: Inspect elements inside dialog
js_inspect_inputs = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let inputs = Array.from(dialog.querySelectorAll("input")).map(i => ({type: i.type, placeholder: i.placeholder, className: i.className}));
    let textareas = Array.from(dialog.querySelectorAll("textarea")).map(t => ({placeholder: t.placeholder, className: t.className, aria: t.getAttribute("aria-label")}));
    let buttons = Array.from(dialog.querySelectorAll("button")).map(b => ({text: b.innerText.trim(), disabled: b.disabled}));
    return JSON.stringify({inputs: inputs, textareas: textareas, buttons: buttons});
})()"""

print("Inputs inspection:", run_js(js_inspect_inputs))
