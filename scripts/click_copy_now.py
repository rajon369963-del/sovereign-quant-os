import json
import subprocess

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"

js = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
    if (!copyBtn) return "NO_COPY_BTN";
    copyBtn.click();
    return "CLICKED_COPY_BTN";
})()"""

ascript = f'''
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

res = subprocess.run(["osascript", "-e", ascript], capture_output=True, text=True)
print("Result:", res.stdout.strip())
