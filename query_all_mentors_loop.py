#!/usr/bin/env python3
import json
import subprocess
import time
from pathlib import Path

NOTEBOOKS = [
    {"id": "b1398c08-e8d3-48de-b645-7e0c821a576f", "name": "01_VIVEK_BAJAJ"},
    {"id": "f67ae556-94ee-4c82-865a-c09c55a90c6d", "name": "02_GHANSHYAM_TECH"},
    {"id": "b0e64cde-7112-432a-8329-5eddcd4252de", "name": "03_SUBASISH_PANI"},
    {"id": "279ad740-9e0d-4e00-a713-a72cffb62a3f", "name": "04_SAKETH_R"},
    {"id": "e5d3eb8c-1492-4670-a4e3-08a5b2fb0f6d", "name": "05_NITIN_MURARKA"},
    {"id": "0f2a60f3-294a-473b-a8a1-36a983e05d3c", "name": "06_PR_SUNDAR"},
    {"id": "a1903e26-f589-42ff-ac02-132bcd02115d", "name": "07_DR_MUKUL_AGRAWAL"},
    {"id": "3884d9e5-c21c-4646-82c9-e4500427f102", "name": "08_SIDDHARTH_BHANUSHALI"},
    {"id": "31fa34c1-8a6e-4ebc-b7ae-3d416e215594", "name": "09_ABHISHEK_KAR"},
    {"id": "96da7dbf-18e9-40a0-9e90-e363052a247f", "name": "QUANT_GITHUB_REPOS"}
]

PROMPT = """COMPREHENSIVE FORENSIC SWOT ANALYSIS OF FOUNDER RAJON DAS'S TRADING JOURNEY (SEP 11-17, 2026):

Context of Rajon's Journey:
- Preparation: Over 9 months of intensive preparation and strategy development.
- Kickoff: Friday (Sep 11) setup.
- Monday (Sep 14): Ganesh Chaturthi holiday, market closed.
- Tuesday (Sep 15): Live Day 1. Bot played ultra-defensive, took 0 trades, preserved 100% capital (₹1,008 intact) while Nifty fell -280 pts.
- Wednesday (Sep 16): Disaster. Bot had pre-market execution delay, defaulted to generic ORB Long, and bought SAIL, TATASTEEL, ASHOKLEY, BHEL into a falling market. Encountered code bugs (NameErrors, disk full). Suffered -₹40.47 to -₹54.81 loss.
- Thursday (Sep 17 - Today): Expiry Day. Bot overtraded (25+ micro intraday trades in PNB, RBLBANK, ITC, TATASTEEL). Took repeated stop-loss hits and bled massive statutory transaction friction (brokerage, STT, GST) on a ₹1,000 account, suffering another net loss!

Based strictly on the grounded sources, videos, and methodologies in YOUR notebook:
1. Provide a rigorous, unfiltered SWOT Analysis of Rajon's journey (Strengths, Weaknesses, Opportunities, Threats).
2. What were his fatal operational, psychological, and execution errors from your viewpoint?
3. What is your exact, non-negotiable prescription and action plan for tomorrow (Friday, Sep 18) to eliminate losses and trade with high conviction?"""

def query_tab(nb_id, nb_name):
    print(f"\n==========================================")
    print(f"[*] Processing {nb_name} ({nb_id})...")
    
    js_check = """
    (function() {
        let messages = Array.from(document.querySelectorAll('.chat-message, .message, .chat-turn, .response, [data-message-author="bot"], .model-response, .to-user, .to-user-container'));
        let lastMsg = messages.length > 0 ? messages[messages.length - 1].innerText : "";
        let isThinking = !!document.querySelector('.thinking, mat-progress-spinner, .loading, .streaming');
        return JSON.stringify({
            msgCount: messages.length,
            lastLen: lastMsg.length,
            isGenerating: isThinking,
            snippet: lastMsg.slice(0, 300),
            fullText: lastMsg
        });
    })()
    """
    
    as_check = f'''
    set jsCode to "{js_check.replace(chr(10), ' ').replace(chr(34), chr(92)+chr(34))}"
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "{nb_id}" then
                    return execute t javascript jsCode
                end if
            end repeat
        end repeat
    end tell
    return "TAB_NOT_FOUND"
    '''
    
    try:
        res = subprocess.run(["osascript", "-e", as_check], capture_output=True, text=True, timeout=12)
        out = res.stdout.strip()
    except Exception as e:
        print(f"[-] Check error: {e}")
        out = ""
        
    if out == "TAB_NOT_FOUND" or not out:
        print(f"[-] Tab check failed for {nb_name}")
    else:
        try:
            data = json.loads(out)
            if data.get("lastLen", 0) > 1000 and not data.get("isGenerating", False):
                print(f"[+] Found existing substantial answer ({data['lastLen']} chars)!")
                return data["fullText"]
        except:
            pass
        
    # Submit prompt if not present
    escaped_prompt = json.dumps(PROMPT)
    js_submit = f"""
    (function() {{
        let q = document.querySelector('.query-box-input, textarea[aria-label="Query box"]');
        if (!q) return JSON.stringify({{status: 'error', message: 'No query box found'}});
        q.value = {escaped_prompt};
        q.dispatchEvent(new Event('input', {{ bubbles: true }}));
        q.dispatchEvent(new Event('change', {{ bubbles: true }}));
        
        let submitBtn = document.querySelector('button[aria-label="Submit"], button.submit-button');
        if (!submitBtn) return JSON.stringify({{status: 'error', message: 'No submit button found'}});
        if (submitBtn.disabled) {{
            submitBtn.removeAttribute('disabled');
            submitBtn.classList.remove('mat-mdc-button-disabled');
        }}
        submitBtn.click();
        return JSON.stringify({{status: 'submitted', timestamp: Date.now()}});
    }})()
    """
    
    as_submit = f'''
    set jsCode to "{js_submit.replace(chr(10), ' ').replace(chr(34), chr(92)+chr(34))}"
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "{nb_id}" then
                    return execute t javascript jsCode
                end if
            end repeat
        end repeat
    end tell
    return "TAB_NOT_FOUND"
    '''
    
    print(f"[*] Submitting new query to {nb_name}...")
    try:
        s_res = subprocess.run(["osascript", "-e", as_submit], capture_output=True, text=True, timeout=12)
        print("Submit result:", s_res.stdout.strip())
    except Exception as e:
        print(f"[-] Submit error: {e}")
        return None
    
    # Poll for response
    for poll in range(25):
        time.sleep(3)
        try:
            p_res = subprocess.run(["osascript", "-e", as_check], capture_output=True, text=True, timeout=12)
            p_data = json.loads(p_res.stdout.strip())
            is_gen = p_data.get("isGenerating", False)
            flen = p_data.get("lastLen", 0)
            print(f"  Poll {poll+1}/25: length={flen}, generating={is_gen}")
            if flen > 500 and not is_gen:
                time.sleep(2)
                p_res2 = subprocess.run(["osascript", "-e", as_check], capture_output=True, text=True, timeout=12)
                p_data2 = json.loads(p_res2.stdout.strip())
                if p_data2.get("lastLen", 0) >= flen:
                    print(f"[+] Successfully captured {p_data2.get('lastLen', 0)} chars from {nb_name}!")
                    return p_data2["fullText"]
        except Exception as e:
            pass
            
    return None

if __name__ == "__main__":
    results_file = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/ALL_9_YOUTUBERS_LIVE_NOTEBOOKLM_RESPONSES.json")
    if results_file.exists():
        with open(results_file) as f:
            try:
                responses = json.load(f)
            except:
                responses = {}
    else:
        responses = {}
        
    for nb in NOTEBOOKS:
        name = nb["name"]
        nb_id = nb["id"]
        if name in responses and len(responses[name].get("response", "")) > 1000:
            print(f"[✓] {name} already has {len(responses[name]['response'])} chars. Skipping.")
            continue
            
        ans = query_tab(nb_id, name)
        if ans:
            responses[name] = {
                "notebook_id": nb_id,
                "name": name,
                "response": ans,
                "length": len(ans),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(results_file, "w", encoding="utf-8") as f:
                json.dump(responses, f, indent=2)
                
    print("\n[✓] Finished querying loop.")
