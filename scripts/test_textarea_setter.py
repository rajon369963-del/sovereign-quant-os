import json
import subprocess


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

js_test = """(() => {
    let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
    if (!dialog) return "NO_DIALOG";
    let ta = dialog.querySelector("textarea.copied-text-input-textarea, textarea");
    if (!ta) return "NO_TEXTAREA";
    
    // Use native prototype setter
    let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
    nativeSetter.call(ta, "# [REPO-TEST] Test\\n\\nSome content here");
    
    ta.dispatchEvent(new InputEvent("input", { bubbles: true, inputType: "insertText" }));
    ta.dispatchEvent(new Event("input", { bubbles: true }));
    ta.dispatchEvent(new Event("change", { bubbles: true }));
    
    let btns = Array.from(dialog.querySelectorAll("button"));
    let insertBtn = btns.find(b => b.innerText.trim() === "Insert");
    
    return JSON.stringify({
        taValueLen: ta.value.length,
        insertBtnExists: !!insertBtn,
        insertBtnDisabled: insertBtn ? insertBtn.disabled : null
    });
})()"""

print("Test native setter:", run_js(js_test))
