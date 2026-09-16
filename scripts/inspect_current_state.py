import json
import subprocess

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"

js = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    let allBtns = Array.from(document.querySelectorAll("button")).map(b => ({
        text: b.innerText.trim(),
        aria: b.getAttribute("aria-label"),
        disabled: b.disabled,
        inDialog: dialog ? dialog.contains(b) : false
    }));
    let allTas = Array.from(document.querySelectorAll("textarea")).map(t => ({
        valLen: t.value.length,
        inDialog: dialog ? dialog.contains(t) : false
    }));
    return JSON.stringify({
        hasDialog: !!dialog,
        buttons: allBtns,
        textareas: allTas
    });
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
print(res.stdout.strip())
