#!/usr/bin/env python3
import json
import subprocess
import time


def run_js(js_code: str) -> str:
    # Clean up single line JS
    clean_js = js_code.replace('\n', ' ').strip()
    # Write to a temporary file
    tmp_path = "/tmp/nb_cmd.js"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(clean_js)
        
    # Read and exec via AppleScript
    as_code = f'''
    set jsScript to do shell script "cat {tmp_path}"
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "notebook.google.com" or URL of t contains "notebooklm.google.com" then
                    tell t
                        return execute javascript jsScript
                    end tell
                end if
            end repeat
        end repeat
        return "NO_TAB"
    end tell
    '''
    p = subprocess.run(['osascript', '-e', as_code], capture_output=True, text=True)
    return p.stdout.strip()

def navigate(url: str):
    as_code = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "notebook.google.com" or URL of t contains "notebooklm.google.com" then
                    tell t
                        set URL to "{url}"
                        return "NAVIGATED"
                    end tell
                end if
            end repeat
        end repeat
        return "NO_TAB"
    end tell
    '''
    p = subprocess.run(['osascript', '-e', as_code], capture_output=True, text=True)
    return p.stdout.strip()

def main():
    ghanshyam_url = "https://notebook.google.com/notebook/f67ae556-94ee-4c82-865a-c09c55a90c6d"
    print(f"Navigating to {ghanshyam_url}...")
    print("Nav result:", navigate(ghanshyam_url))
    time.sleep(5)
    
    # Check if page loaded
    chk = run_js('JSON.stringify({title: document.title, url: window.location.href, hasTa: !!document.querySelector("textarea.query-box-input")})')
    print("Page status:", chk)
    
    prompt = "Vivek Bajaj argues that global liquidity is tightening with US Dollar Index (DXY) strength and crude volatility, requiring extreme caution. How does your 5-minute price action and 9:20 candle model validate or refute this for Wednesday Bank Nifty expiry?"
    
    # Insert prompt
    escaped_prompt = json.dumps(prompt)
    insert_code = f'''
    (function() {{
        let ta = document.querySelector("textarea.query-box-input") || document.querySelector("textarea[aria-label=\\"Query box\\"]");
        if (!ta) return "NO_TA";
        ta.focus();
        ta.select();
        document.execCommand("selectAll", false, null);
        document.execCommand("insertText", false, {escaped_prompt});
        return "INSERTED";
    }})()
    '''
    print("Insert:", run_js(insert_code))
    time.sleep(1.5)
    
    # Click submit
    click_code = '''
    (function() {
        let btn = document.querySelector("button.submit-button") || document.querySelector("button[aria-label=\\"Submit\\"]");
        if (btn && !btn.disabled) {
            btn.click();
            return "CLICKED";
        }
        return btn ? "DISABLED" : "NO_BTN";
    })()
    '''
    print("Click:", run_js(click_code))
    
    # Wait and check
    for i in range(20):
        time.sleep(3)
        poll_code = '''
        (function() {
            let stopBtn = document.querySelector("button[aria-label=\\"Stop\\"]") || document.querySelector("button.stop-button");
            let turns = Array.from(document.querySelectorAll(".model-response, conversation-turn, .message-content"));
            let lastTurn = turns.length > 0 ? turns[turns.length - 1].innerText : "";
            return JSON.stringify({thinking: !!stopBtn, len: lastTurn.length, snippet: lastTurn.slice(0, 150)});
        })()
        '''
        res = run_js(poll_code)
        print(f"[{i}] {res}")
        try:
            d = json.loads(res)
            if not d.get("thinking") and d.get("len", 0) > 150:
                print("DONE!")
                break
        except:
            pass

if __name__ == "__main__":
    main()
