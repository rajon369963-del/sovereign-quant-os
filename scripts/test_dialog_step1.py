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

# Step 1: Click Add source
js_open = """(() => {
    document.querySelectorAll("emoji-keyboard, .emoji-keyboard__container").forEach(el => el.remove());
    let tab = Array.from(document.querySelectorAll(".mdc-tab")).find(t => t.innerText.includes("Sources"));
    if (tab && !tab.classList.contains("mdc-tab--active")) tab.click();
    let addBtn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").includes("Add source") || b.getAttribute("aria-label") === "Add source");
    if (!addBtn) return "NO_ADD_BTN";
    addBtn.click();
    return "CLICKED_ADD";
})()"""

print("Open Add source:", run_js(js_open))
time.sleep(1)

# Step 2: Inspect dialog options
js_inspect_dialog = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return JSON.stringify({dialog: null, allButtons: Array.from(document.querySelectorAll("button")).map(b => b.innerText.trim())});
    let btns = Array.from(dialog.querySelectorAll("button")).map(b => ({text: b.innerText.trim(), aria: b.getAttribute("aria-label")}));
    return JSON.stringify({foundDialog: true, buttons: btns});
})()"""

print("Dialog inspection:", run_js(js_inspect_dialog))
