import hashlib
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"
SOURCE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources")

def ingest_single_repo(idx):
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

    # Write payload to tmp file
    payload_path = "/tmp/nlm_curr_payload.txt"
    with open(payload_path, "w", encoding="utf-8") as f:
        f.write(payload)

    # Step 1: Open Add Source and click Copied text if not already on it
    js_step1 = """(() => {
        document.querySelectorAll("emoji-keyboard, .emoji-keyboard__container").forEach(el => el.remove());
        let tab = Array.from(document.querySelectorAll(".mdc-tab")).find(t => t.innerText.includes("Sources"));
        if (tab && !tab.classList.contains("mdc-tab--active")) tab.click();
        
        let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
        if (!dialog) {
            let addBtn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").includes("Add source") || b.getAttribute("aria-label") === "Add source");
            if (!addBtn) return "NO_ADD_BTN";
            addBtn.click();
            return "CLICKED_ADD";
        }
        return "DIALOG_ALREADY_OPEN";
    })()"""

    ascript1 = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{NOTEBOOK_ID}" then
                tell t
                    return execute javascript {json.dumps(js_step1)}
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
    res1 = subprocess.run(["osascript", "-e", ascript1], capture_output=True, text=True).stdout.strip()
    time.sleep(0.4)

    # Step 2: Click Copied text if on initial dialog
    js_step2 = """(() => {
        let dialog = document.querySelector("mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel");
        if (!dialog) return "NO_DIALOG";
        let ta = dialog.querySelector("textarea.copied-text-input-textarea, textarea");
        if (ta) return "ALREADY_ON_TEXTAREA";
        let copyBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.includes("Copied text"));
        if (!copyBtn) return "NO_COPY_BTN";
        copyBtn.click();
        return "CLICKED_COPIED_TEXT";
    })()"""
    ascript2 = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{NOTEBOOK_ID}" then
                tell t
                    return execute javascript {json.dumps(js_step2)}
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
    res2 = subprocess.run(["osascript", "-e", ascript2], capture_output=True, text=True).stdout.strip()
    time.sleep(0.4)

    # Step 3: Read payload via AppleScript and insert into textarea
    ascript3 = f'''
set filePath to POSIX file "{payload_path}"
set fileContent to (read filePath as «class utf8»)
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{NOTEBOOK_ID}" then
                tell t
                    set jsCode to "(() => {{
                        let dialog = document.querySelector(\\\"mat-dialog-container, [role='dialog'], .mat-mdc-dialog-panel\\\");
                        if (!dialog) return 'NO_DIALOG';
                        let ta = dialog.querySelector(\\\"textarea.copied-text-input-textarea, textarea\\\");
                        if (!ta) return 'NO_TEXTAREA';
                        
                        let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
                        nativeSetter.call(ta, window._nlm_pending_payload);
                        
                        ta.dispatchEvent(new InputEvent('input', {{ bubbles: true, inputType: 'insertText' }}));
                        ta.dispatchEvent(new Event('input', {{ bubbles: true }}));
                        ta.dispatchEvent(new Event('change', {{ bubbles: true }}));
                        
                        let btns = Array.from(dialog.querySelectorAll('button'));
                        let insertBtn = btns.find(b => b.innerText.trim() === 'Insert');
                        if (!insertBtn) return 'NO_INSERT_BTN';
                        if (insertBtn.disabled) return 'INSERT_DISABLED';
                        
                        insertBtn.click();
                        return 'SUCCESS_INSERT';
                    }})()"
                    execute javascript ("window._nlm_pending_payload = " & (quoted form of fileContent) & ";")
                    return execute javascript jsCode
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
    temp_scpt = "/tmp/nlm_step3.applescript"
    with open(temp_scpt, "w", encoding="utf-8") as f:
        f.write(ascript3)
    res3 = subprocess.run(["osascript", temp_scpt], capture_output=True, text=True).stdout.strip()
    return f"[{idx:03d}] step1={res1}, step2={res2}, step3={res3}"

print("Ingesting REPO-004:", ingest_single_repo(4))
time.sleep(2)
print("Ingesting REPO-005:", ingest_single_repo(5))
time.sleep(2)

# Verify count
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
print("Notebook sources:", subprocess.run(["osascript", "-e", ascript_v], capture_output=True, text=True).stdout.strip())
