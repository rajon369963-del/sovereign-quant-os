import hashlib
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"
SOURCE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources")

def ingest_repo(idx):
    files = sorted(list(SOURCE_DIR.glob(f"QUANT_REPO_{idx:03d}_*.txt")))
    if not files:
        return f"FILE_NOT_FOUND for {idx}"
    repo_file = files[0]
    raw_content = repo_file.read_text(encoding="utf-8")
    file_size = len(raw_content.encode("utf-8"))
    sha256 = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()
    clean_name = repo_file.stem.replace(f"QUANT_REPO_{idx:03d}_", "")
    
    header = f"""# [REPO-{idx:03d}] {clean_name} | SHA256:{sha256[:12]}
- **Deterministic Cryptographic SHA-256**: `{sha256}`
- **Repository Index**: {idx:03d} / 290
- **File Name**: `{repo_file.name}`
- **Verification Provenance**: PHYSICAL_DISK_AUTHENTICATED (100% End-to-End Source Code)
- **Local Path**: `{repo_file}`
- **File Size**: {file_size:,d} bytes
- **Timestamp**: {datetime.utcnow().isoformat()}Z

---

"""
    payload = header + raw_content

    # Step A: Close any dialog or open fresh Add source -> Copied text
    js_prep = """(() => {
        document.querySelectorAll("emoji-keyboard, .emoji-keyboard__container").forEach(el => el.remove());
        let tab = Array.from(document.querySelectorAll(".mdc-tab")).find(t => t.innerText.includes("Sources"));
        if (tab && !tab.classList.contains("mdc-tab--active")) tab.click();
        
        let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
        let ta = dialog ? dialog.querySelector("textarea.copied-text-input-textarea, textarea") : null;
        if (ta) return "READY_FOR_TEXT";
        
        if (dialog) {
            let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
            if (copyBtn) {
                copyBtn.click();
                return "CLICKED_COPIED_TEXT";
            }
            // Close dialog if in strange state
            let closeBtn = dialog.querySelector("button[aria-label='Close'], button.close-button");
            if (closeBtn) closeBtn.click();
        }
        
        let addBtn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").includes("Add source") || b.getAttribute("aria-label") === "Add source");
        if (!addBtn) return "NO_ADD_BTN";
        addBtn.click();
        return "CLICKED_ADD_SOURCE";
    })()"""

    ascript_prep = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{NOTEBOOK_ID}" then
                tell t
                    return execute javascript {json.dumps(js_prep)}
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
    res_prep = subprocess.run(["osascript", "-e", ascript_prep], capture_output=True, text=True).stdout.strip()
    time.sleep(0.35)

    # If it clicked add source, now click copied text
    if res_prep == "CLICKED_ADD_SOURCE":
        js_copy = """(() => {
            let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
            if (!dialog) return "NO_DIALOG";
            let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
            if (!copyBtn) return "NO_COPY_BTN";
            copyBtn.click();
            return "CLICKED_COPIED_TEXT";
        })()"""
        ascript_copy = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{NOTEBOOK_ID}" then
                tell t
                    return execute javascript {json.dumps(js_copy)}
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
        subprocess.run(["osascript", "-e", ascript_copy], capture_output=True, text=True)
        time.sleep(0.35)

    # Step B: Write JavaScript code that sets the textarea and clicks Insert
    js_code = f"""(() => {{
        let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
        if (!dialog) return "NO_DIALOG";
        let ta = dialog.querySelector("textarea.copied-text-input-textarea, textarea");
        if (!ta) return "NO_TEXTAREA";
        
        let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
        nativeSetter.call(ta, {json.dumps(payload)});
        
        ta.dispatchEvent(new InputEvent("input", {{ bubbles: true, inputType: "insertText" }}));
        ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
        ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
        
        let btns = Array.from(dialog.querySelectorAll("button"));
        let insertBtn = btns.find(b => b.innerText.trim() === "Insert");
        if (!insertBtn) return "NO_INSERT_BTN";
        if (insertBtn.disabled) return "INSERT_DISABLED";
        
        insertBtn.click();
        return "SUCCESS_INSERTED";
    }})()"""

    temp_js = "/tmp/nlm_curr_task.js"
    with open(temp_js, "w", encoding="utf-8") as f:
        f.write(js_code)

    temp_applescript = "/tmp/nlm_curr_runner.applescript"
    ascript_run = f'''
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
'''
    with open(temp_applescript, "w", encoding="utf-8") as f:
        f.write(ascript_run)

    res_insert = subprocess.run(["osascript", temp_applescript], capture_output=True, text=True).stdout.strip()
    return f"[{idx:03d}] prep={res_prep} | insert={res_insert}"

print("Running REPO-004:", ingest_repo(4))
time.sleep(2)
print("Running REPO-005:", ingest_repo(5))
time.sleep(2)

js_verify = """(() => {
    let sources = Array.from(document.querySelectorAll(".source-title")).map(el => el.innerText.trim());
    return JSON.stringify({count: sources.length, sources: sources});
})()"""
ascript_v = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{NOTEBOOK_ID}" then
                tell t
                    return execute javascript {json.dumps(js_verify)}
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
print("Verification:", subprocess.run(["osascript", "-e", ascript_v], capture_output=True, text=True).stdout.strip())
