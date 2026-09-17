#!/usr/bin/env python3
import json
import subprocess
import time
from pathlib import Path

REMAINING_NOTEBOOKS = [
    {"id": "279ad740-9e0d-4e00-a713-a72cffb62a3f", "name": "04_SAKETH_R", "person": "Saketh R (Options & Greeks)"},
    {"id": "e5d3eb8c-1492-4670-a4e3-08a5b2fb0f6d", "name": "05_NITIN_MURARKA", "person": "Nitin Murarka (Order Flow & VWAP)"},
    {"id": "0f2a60f3-294a-473b-a8a1-36a983e05d3c", "name": "06_PR_SUNDAR", "person": "PR Sundar (Capital Preservation & Hedging)"},
    {"id": "a1903e26-f589-42ff-ac02-132bcd02115d", "name": "07_DR_MUKUL_AGRAWAL", "person": "Dr Mukul Agrawal (Forensics & Fundamentals)"},
    {"id": "3884d9e5-c21c-4646-82c9-e4500427f102", "name": "08_SIDDHARTH_BHANUSHALI", "person": "Siddharth Bhanushali (44 EMA & Swing)"},
    {"id": "31fa34c1-8a6e-4ebc-b7ae-3d416e215594", "name": "09_ABHISHEK_KAR", "person": "Abhishek Kar (Behavioral Finance & Psychology)"},
    {"id": "96da7dbf-18e9-40a0-9e90-e363052a247f", "name": "QUANT_GITHUB_REPOS", "person": "290 Quant Repos & Algorithmic HFT Brain"}
]

RESULTS_FILE = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/ALL_9_YOUTUBERS_LIVE_NOTEBOOKLM_RESPONSES.json")

def get_tab_body(nb_id):
    as_code = f'''
    tell application "Google Chrome"
        repeat with w in windows
            set idx to 1
            repeat with t in tabs of w
                if URL of t contains "{nb_id}" then
                    set active tab index of w to idx
                    delay 0.5
                    tell t
                        return execute javascript "document.body.innerText"
                    end tell
                end if
                set idx to idx + 1
            end repeat
        end repeat
        return "TAB_NOT_FOUND"
    end tell
    '''
    res = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True, timeout=10)
    return res.stdout.strip()

def submit_query(nb_id, prompt_text):
    escaped = json.dumps(prompt_text)
    js = f"""
    (() => {{
        let q = document.querySelector(".query-box-input, textarea[aria-label=\\"Query box\\"], textarea");
        if (!q) return "NO_QUERY_BOX";
        q.focus();
        q.value = {escaped};
        q.dispatchEvent(new Event("input", {{ bubbles: true }}));
        q.dispatchEvent(new Event("change", {{ bubbles: true }}));
        
        let submitBtn = document.querySelector("button[aria-label=\\"Submit\\"], button.submit-button");
        if (!submitBtn) return "NO_SUBMIT_BTN";
        if (submitBtn.disabled) {{
            submitBtn.removeAttribute("disabled");
            submitBtn.classList.remove("mat-mdc-button-disabled");
        }}
        submitBtn.click();
        return "SUBMITTED";
    }})()
    """
    tmp_file = f"/tmp/nb_query_{nb_id[:8]}.js"
    with open(tmp_file, "w") as f:
        f.write(js.replace("\n", " ").strip())
        
    as_code = f'''
    set jsCode to do shell script "cat {tmp_file}"
    tell application "Google Chrome"
        repeat with w in windows
            set idx to 1
            repeat with t in tabs of w
                if URL of t contains "{nb_id}" then
                    set active tab index of w to idx
                    delay 0.5
                    tell t
                        return execute javascript jsCode
                    end tell
                end if
                set idx to idx + 1
            end repeat
        end repeat
        return "TAB_NOT_FOUND"
    end tell
    '''
    res = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True, timeout=10)
    return res.stdout.strip()

def run_all():
    with open(RESULTS_FILE) as f:
        responses = json.load(f)

    for item in REMAINING_NOTEBOOKS:
        nb_id = item["id"]
        name = item["name"]
        person = item["person"]
        print(f"\n==========================================")
        print(f"[*] Checking {name} ({person})...")
        
        # Check if already done
        if name in responses and len(responses[name].get("response", "")) > 1000:
            print(f"[✓] {name} already has {len(responses[name]['response'])} chars! Skipping.")
            continue
            
        body = get_tab_body(nb_id)
        if body == "TAB_NOT_FOUND":
            print(f"[-] Tab not open in Chrome for {name} ({nb_id})")
            continue
            
        print(f"[*] Initial body length: {len(body)}")
        
        # Check if an existing response to SWOT is in the body
        if "SWOT Analysis" in body or "COMPREHENSIVE FORENSIC SWOT" in body:
            idx = body.rfind("COMPREHENSIVE FORENSIC SWOT")
            if idx == -1: idx = body.rfind("SWOT Analysis")
            candidate = body[idx:]
            if len(candidate) > 1500 and "Thinking…" not in candidate[-200:]:
                print(f"[+] Found existing grounded response in DOM ({len(candidate)} chars)!")
                responses[name] = {
                    "notebook_id": nb_id,
                    "name": name,
                    "response": candidate,
                    "length": len(candidate),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                with open(RESULTS_FILE, "w") as f:
                    json.dump(responses, f, indent=2)
                continue
                
        # Submit fresh prompt
        prompt = f"""COMPREHENSIVE FORENSIC SWOT ANALYSIS OF FOUNDER RAJON DAS TRADING JOURNEY (SEP 11-17, 2026):

Context:
- 9 months prep.
- Friday kickoff.
- Monday Ganesh Chaturthi holiday.
- Tuesday (Sep 15): Bot took 0 trades, preserved ₹1,008 capital while Nifty crashed -280 pts.
- Wednesday (Sep 16): Disaster. Bot had pre-market setup delay, defaulted to generic ORB Long, and bought SAIL, TATASTEEL, ASHOKLEY, BHEL into a falling market. Software bugs (NameErrors, disk full). Suffered -₹40.47 to -₹54.81 loss.
- Thursday (Sep 17 - Today): Expiry Day. Bot overtraded (25+ micro trades in PNB, RBLBANK, ITC, TATASTEEL), took repeated stop-losses, and bled heavy statutory transaction friction on a ₹1,000 account, suffering another net loss!

Based strictly on {person} uploaded sources and methodologies in this notebook:
1. Conduct an honest, rigorous SWOT Analysis of Rajon journey (Strengths, Weaknesses, Opportunities, Threats).
2. What were his fatal mistakes from your domain expertise?
3. What is your exact prescription for tomorrow (Friday, Sep 18) to stop bleeding, manage risk, and trade profitably?"""

        print(f"[*] Submitting query to {name}...")
        sub_res = submit_query(nb_id, prompt)
        print("Submit status:", sub_res)
        
        # Wait and poll for completion
        print("[*] Waiting for AI generation to complete...")
        for poll in range(15):
            time.sleep(3)
            b = get_tab_body(nb_id)
            is_thinking = "Thinking…" in b or "thinking" in b[-300:].lower()
            idx = b.rfind("COMPREHENSIVE FORENSIC SWOT")
            if idx == -1: idx = b.rfind("SWOT Analysis")
            cur_ans = b[idx:] if idx != -1 else ""
            print(f"  Poll {poll+1}/15: ans_len={len(cur_ans)}, thinking={is_thinking}")
            if len(cur_ans) > 1200 and not is_thinking:
                time.sleep(2)
                # Confirm stability
                b2 = get_tab_body(nb_id)
                cur_ans2 = b2[idx:] if idx != -1 else ""
                print(f"[+] Successfully captured {len(cur_ans2)} chars from {name}!")
                responses[name] = {
                    "notebook_id": nb_id,
                    "name": name,
                    "response": cur_ans2,
                    "length": len(cur_ans2),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                with open(RESULTS_FILE, "w") as f:
                    json.dump(responses, f, indent=2)
                break

    print("\n[✓] All mentors processing complete!")

if __name__ == "__main__":
    run_all()
