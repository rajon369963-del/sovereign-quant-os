import subprocess
import time
import json
import sys
from pathlib import Path

NOTEBOOK_ID = "96da7dbf-18e9-40a0-9e90-e363052a247f"

def run_js(js):
    apple_script = f'''
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
    res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    return res.stdout.strip()

def upload_repo_file(file_path):
    p = Path(file_path)
    if not p.exists():
        print(f"[-] File not found: {file_path}")
        return False
    
    content = p.read_text(encoding="utf-8")
    print(f"\n=======================================================")
    print(f"[*] Uploading: {p.name} ({len(content)} chars)")
    print(f"=======================================================")

    # 1. Check if "Paste copied text" modal is already open
    check_modal = """
    (() => {
        let dialog = document.querySelector("mat-dialog-container, [role=dialog]");
        if (!dialog) return "NO_MODAL";
        let ta = dialog.querySelector("textarea");
        return ta ? "PASTE_MODAL_READY" : "OTHER_MODAL";
    })()
    """
    m_state = run_js(check_modal)
    print(f"[1] Modal State: {m_state}")

    if m_state != "PASTE_MODAL_READY":
        # Reset any stuck dialog
        run_js("""
        (() => {
            let closeBtn = document.querySelector("mat-dialog-container button[aria-label*='Close' i], mat-dialog-container button[mat-dialog-close]");
            if (closeBtn) closeBtn.click();
            let backdrop = document.querySelector(".cdk-overlay-backdrop");
            if (backdrop) backdrop.click();
        })()
        """)
        time.sleep(1.0)
        
        # Click Add source
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
        print(f"[2] Click Add Source: {run_js(click_add)}")
        time.sleep(1.2)
        
        # Click Copied text
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
        print(f"[3] Click Copied Text: {run_js(click_copied)}")
        time.sleep(1.2)

    # 2. Stream content in 150 KB chunks into browser V8 memory
    print("[4] Streaming content in chunks into V8 memory...")
    run_js("window.__upload_buffer = '';")
    CHUNK_SIZE = 150000
    chunks = [content[i:i+CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]
    for i, chunk in enumerate(chunks):
        run_js(f"window.__upload_buffer += {json.dumps(chunk)};")
    
    buf_len = run_js("window.__upload_buffer.length;")
    print(f"[+] Total bytes staged in V8 buffer: {buf_len}")

    # 3. Inject buffer into textarea
    inject_js = """
    (() => {
        let ta = document.querySelector("textarea.copied-text-input-textarea, textarea[aria-label='Pasted text' i], textarea");
        if (!ta) return "NO_TEXTAREA";
        
        ta.focus();
        let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
        nativeSetter.call(ta, window.__upload_buffer);
        ta.dispatchEvent(new Event("input", { bubbles: true }));
        ta.dispatchEvent(new Event("change", { bubbles: true }));
        
        window.__upload_buffer = null; // release buffer
        return "INJECTED_CHARS_" + ta.value.length;
    })()
    """
    res_inj = run_js(inject_js)
    print(f"[5] Inject to Textarea: {res_inj}")
    time.sleep(1.0)

    # 4. Click Insert button
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
    print(f"[6] Click Insert: {res_insert}")

    # 5. Wait for dialog to close & source ingestion
    print("[7] Waiting for ingestion to complete...")
    for poll in range(15):
        time.sleep(2.0)
        check_done = """
        (() => {
            let dialog = document.querySelector("mat-dialog-container, [role=dialog]");
            return dialog ? "STILL_INGESTING" : "DIALOG_CLOSED";
        })()
        """
        status = run_js(check_done)
        if status == "DIALOG_CLOSED":
            print(f"[+] Ingestion complete! Dialog closed in {(poll+1)*2}s.")
            break
        print(f"    ...still ingesting ({(poll+1)*2}s)")

    # 6. Verify source count in DOM
    verify_sources = """
    (() => {
        let items = Array.from(document.querySelectorAll(".single-source-container"));
        let countText = (document.body.innerText.match(/\\d+\\s+sources/i) || [])[0] || "";
        return JSON.stringify({
            countText: countText,
            totalItems: items.length,
            latestTitle: items.length > 0 ? (items[0].innerText || "").split("\\n")[0] : "none"
        });
    })()
    """
    v_res = run_js(verify_sources)
    print(f"[8] Verification: {v_res}")
    return True

if __name__ == "__main__":
    fp = sys.argv[1] if len(sys.argv) > 1 else "/Users/rajondas/teamwork_projects/sovereign-quant-os/individual_290_quant_repos_sources/QUANT_REPO_001_dhanhq_ecosystem.txt"
    upload_repo_file(fp)
