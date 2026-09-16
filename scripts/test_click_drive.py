import subprocess
import time

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"
TEMP_JS = "/tmp/drive_test.js"
TEMP_SCPT = "/tmp/drive_test.applescript"

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

# Open dialog if not open
js_open = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (dialog) {
        let closeBtn = dialog.querySelector("button[aria-label='Close'], button.close-button");
        if (closeBtn) closeBtn.click();
    }
    let addBtn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").includes("Add source") || b.getAttribute("aria-label") === "Add source");
    if (addBtn) addBtn.click();
    return "CLICKED_ADD";
})()"""
print("Open:", run_js(js_open))
time.sleep(0.5)

# Click Drive
js_click_drive = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let driveBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Drive"));
    if (!driveBtn) return "NO_DRIVE_BTN";
    driveBtn.click();
    return "CLICKED_DRIVE";
})()"""
print("Click Drive:", run_js(js_click_drive))
time.sleep(1.0)

# Check what opened
js_inspect = """(() => {
    let iframes = Array.from(document.querySelectorAll("iframe")).map(f => ({src: f.src, className: f.className, name: f.name}));
    let dialogs = Array.from(document.querySelectorAll("[role='dialog'], .picker-dialog")).map(d => ({className: d.className, text: d.innerText.substring(0, 100)}));
    return JSON.stringify({iframes: iframes, dialogs: dialogs});
})()"""
print("Inspect:", run_js(js_inspect))
