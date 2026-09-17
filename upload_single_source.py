import subprocess
import time
import json
import sys
from pathlib import Path

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"

def upload_source(file_path):
    p = Path(file_path)
    if not p.exists():
        print(f"File {file_path} does not exist!")
        return False
    
    content = p.read_text(encoding="utf-8")
    first_line = content.split("\n")[0]
    title = first_line.replace("# ", "").strip()
    if len(title) > 80:
        title = title[:77] + "..."

    # 1. Copy content to macOS clipboard
    proc = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE, text=True)
    proc.communicate(content)
    print(f"[*] Copied {p.name} ({len(content)} chars) to system clipboard")

    def run_js(js):
        apple_script = f'''
        tell application "Google Chrome"
            tell active tab of front window
                return execute javascript {json.dumps(js)}
            end tell
        end tell
        '''
        res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
        return res.stdout.strip()

    # 2. Focus notebook tab
    focus_tab = f'''
    tell application "Google Chrome"
        activate
        repeat with w in windows
            repeat with t in tabs of w
                if (URL of t) contains "{NOTEBOOK_ID}" then
                    set index of w to 1
                    set active tab index of w to (get index of t)
                    return "FOCUSED"
                end if
            end repeat
        end repeat
        return "NOT_FOUND"
    end tell
    '''
    focus_res = subprocess.run(["osascript", "-e", focus_tab], capture_output=True, text=True).stdout.strip()
    print(f"[*] Focus Tab: {focus_res}")
    time.sleep(0.5)

    # 3. Click Add source button
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
    res_add = run_js(click_add)
    print(f"[*] Click Add: {res_add}")
    time.sleep(1.2)

    # 4. Click Copied text
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
    res_copied = run_js(click_copied)
    print(f"[*] Click Copied: {res_copied}")
    time.sleep(1.2)

    # 5. Set Title and focus textarea
    prep_paste = f"""
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
        return "FOCUSED_TEXTAREA";
    }})()
    """
    res_prep = run_js(prep_paste)
    print(f"[*] Prep Title & Focus Textarea: {res_prep}")
    time.sleep(0.5)

    # 6. Command+V Paste
    paste_script = '''
    tell application "Google Chrome" to activate
    tell application "System Events"
        keystroke "v" using {command down}
    end tell
    '''
    subprocess.run(["osascript", "-e", paste_script])
    print("[*] Executed Command+V Paste!")
    time.sleep(1.5)

    # 7. Dispatch events on textarea
    confirm_paste = """
    (() => {
        let ta = document.querySelector("textarea[aria-label='Pasted text' i]");
        if (!ta) return "NO_TEXTAREA";
        ta.dispatchEvent(new Event("input", { bubbles: true }));
        ta.dispatchEvent(new Event("change", { bubbles: true }));
        return "PASTED_LEN_" + ta.value.length;
    })()
    """
    print(f"[*] Confirmed Content: {run_js(confirm_paste)}")
    time.sleep(0.5)

    # 8. Click Insert
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
    res_insert = run_js(click_insert)
    print(f"[*] Click Insert: {res_insert}")
    time.sleep(5.0)

    # 9. Verify count
    check_count = """
    (() => {
        let containers = Array.from(document.querySelectorAll(".single-source-container"));
        return JSON.stringify({
            totalSources: containers.length,
            titles: containers.slice(0, 3).map(c => (c.innerText || "").split("\\n")[0])
        });
    })()
    """
    print(f"[+] Status after upload: {run_js(check_count)}")
    return True

if __name__ == "__main__":
    fp = sys.argv[1] if len(sys.argv) > 1 else "/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources/QUANT_REPO_001_dhanhq_ecosystem.txt"
    upload_source(fp)
