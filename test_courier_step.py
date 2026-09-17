#!/usr/bin/env python3
"""
Test courier step:
Navigates to Ghanshyam Tech's notebook, sends a couriered question referencing Vivek Bajaj,
and extracts the full response.
"""

import json
import subprocess
import time


def exec_js(js_code: str):
    clean_js = js_code.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
    as_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "notebook.google.com" or URL of t contains "notebooklm.google.com" then
                    tell t
                        return execute javascript "{clean_js}"
                    end tell
                end if
            end repeat
        end repeat
        return "NO_TAB"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', as_script], capture_output=True, text=True)
    return res.stdout.strip()

def navigate(url: str):
    as_script = f'''
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
    res = subprocess.run(['osascript', '-e', as_script], capture_output=True, text=True)
    return res.stdout.strip()

def query_notebook(notebook_id: str, prompt: str, timeout: int = 75):
    url = f"https://notebook.google.com/notebook/{notebook_id}"
    print(f"[*] Navigating to {url}...")
    nav = navigate(url)
    print(f"[*] Navigation result: {nav}")
    
    # Wait for textarea
    for _ in range(20):
        time.sleep(1)
        check = exec_js('!!(document.querySelector("textarea.query-box-input") || document.querySelector("textarea[aria-label=\\"Query box\\"]"))')
        if check == "true":
            break
    print("[*] Textarea found. Inserting prompt...")
    
    # Insert prompt using execCommand
    escaped_prompt = prompt.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    insert_js = f'''
    (function() {{
        let ta = document.querySelector("textarea.query-box-input") || document.querySelector("textarea[aria-label=\\"Query box\\"]");
        if (!ta) return "NO_TA";
        ta.focus();
        ta.select();
        document.execCommand("selectAll", false, null);
        document.execCommand("insertText", false, "{escaped_prompt}");
        return "INSERTED";
    }})()
    '''
    ins_res = exec_js(insert_js)
    print(f"[*] Insert result: {ins_res}")
    
    time.sleep(1)
    
    # Click submit
    click_js = '''
    (function() {
        let btn = document.querySelector("button.submit-button") || document.querySelector("button[aria-label=\\"Submit\\"]");
        if (btn && !btn.disabled) {
            btn.click();
            return "CLICKED";
        }
        return btn ? "DISABLED" : "NO_BTN";
    })()
    '''
    click_res = exec_js(click_js)
    print(f"[*] Click result: {click_res}")
    
    # If disabled, wait a moment and try again
    if click_res == "DISABLED":
        time.sleep(1.5)
        click_res = exec_js(click_js)
        print(f"[*] Second click attempt: {click_res}")
        
    # Poll for completion
    print("[*] Waiting for response to generate...")
    start_time = time.time()
    full_text = ""
    
    while time.time() - start_time < timeout:
        time.sleep(3)
        status_js = '''
        (function() {
            let stopBtn = document.querySelector("button[aria-label=\\"Stop\\"]") || document.querySelector("button.stop-button");
            let turns = Array.from(document.querySelectorAll(".model-response, conversation-turn, .message-content"));
            let lastTurn = turns.length > 0 ? turns[turns.length - 1].innerText : "";
            return JSON.stringify({
                isThinking: !!stopBtn,
                len: lastTurn.length,
                text: lastTurn
            });
        })()
        '''
        raw = exec_js(status_js)
        try:
            data = json.loads(raw)
            is_thinking = data.get("isThinking", False)
            cur_len = data.get("len", 0)
            full_text = data.get("text", "")
            print(f"    Thinking: {is_thinking}, Length: {cur_len}")
            if not is_thinking and cur_len > 150:
                print("[+] Generation complete!")
                break
        except Exception:
            pass
            
    return full_text

if __name__ == "__main__":
    ghanshyam_id = "f67ae556-94ee-4c82-865a-c09c55a90c6d"
    prompt = "Vivek Bajaj has established a macro thesis that global liquidity is tightening with US Dollar Index (DXY) strength and crude volatility, requiring extreme caution. Based on your 300 Bank Nifty videos and price action principles, how does your 9:20 candle and support/resistance breakout strategy respond to this macro environment for intraday expiry trading?"
    ans = query_notebook(ghanshyam_id, prompt)
    print("\n" + "="*80)
    print("GHANSHYAM TECH COURIERED RESPONSE:")
    print("="*80)
    print(ans[:1500])
