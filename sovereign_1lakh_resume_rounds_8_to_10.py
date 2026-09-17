#!/usr/bin/env python3
"""
⚡ SOVEREIGN 1 LAKH COURIER DEBATE RESUME SCRIPT (ROUNDS 8, 9, 10)
=============================================================================
Resumes execution for:
  - Round 8: Tab 8 (SIDDHARTH_BHANUSHALI)
  - Round 9: Tab 9 (DR_MUKUL_AGRAWAL)
  - Round 10: Tab 15 (QUANT_REPOS_AND_MASTER_ARCHIVE)

Then generates the comprehensive audio and markdown artifacts.
"""

import subprocess
import time
import json
import sqlite3
import os
import asyncio
import edge_tts
import pybase64 as base64
from pathlib import Path

BASE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os")
DB_PATH = BASE_DIR / "grand_10k_trading_hypergraph.sqlite"
TRANSCRIPT_FILE = BASE_DIR / "LIVE_COURIER_1LAKH_DEBATE_TRANSCRIPT.md"
JSON_OUTPUT = BASE_DIR / "COURIER_1LAKH_DEBATE_FINAL_SYNTHESIS.json"
AUDIO_ARTIFACT = Path("/Users/rajondas/.gemini/antigravity/brain/406b1b3f-5aca-403c-b468-cf736f90106e/courier_1lakh_debate_master_audio.html")

REMAINING_ROUNDS = [
    {
        "round": 8,
        "tab_idx": 8,
        "entity": "SIDDHARTH_BHANUSHALI",
        "sender": "ABHISHEK_KAR",
        "prompt": """COURIER DISPATCH - ROUND 8 FOR ₹1 LAKH CAPITAL: FROM ABHISHEK KAR TO SIDDHARTH BHANUSHALI:
Abhishek Kar addressed emotional detachment and treating capital as percentages.
Siddharth Bhanushali, on 44-MA Swing Scaling to ₹5-10 Lakhs:
1. With ₹1,00,000, how can Rajon take 3 simultaneous 44-MA swing positions (₹30,000 in each high-momentum stock)?
2. When a 44-MA swing captures a 15-20% move, making ₹4,500 to ₹6,000 per stock, how does pyramiding into winning swings accelerate compounding?
3. How does 44-MA swing trading allow a trader to maintain a full-time tech job or AI agency while growing wealth?"""
    },
    {
        "round": 9,
        "tab_idx": 9,
        "entity": "DR_MUKUL_AGRAWAL",
        "sender": "SIDDHARTH_BHANUSHALI",
        "prompt": """COURIER DISPATCH - ROUND 9 FOR ₹1 LAKH CAPITAL: FROM SIDDHARTH BHANUSHALI TO DR. MUKUL AGRAWAL:
Siddharth demonstrated multi-stock 44-MA swing allocation at ₹1 Lakh.
Dr. Mukul Agrawal, on High-Growth Wealth Creation from ₹1 Lakh to ₹50 Lakhs:
1. How can ₹1 Lakh be deployed into a concentrated basket of 4-5 emerging multi-cap leaders with clean balance sheets and institutional accumulation?
2. Why is patient sector rotation (moving capital from peaking sectors to early-stage turnaround sectors) the secret to turning ₹1 Lakh into ₹10 Lakhs in 2-3 years?
3. What is your final master advice for someone standing at ₹1 Lakh with a dream of ₹1 Crore?"""
    },
    {
        "round": 10,
        "tab_idx": 15,
        "entity": "QUANT_REPOS_AND_MASTER_ARCHIVE",
        "sender": "ALL 9 GURUS",
        "prompt": """COURIER DISPATCH - ROUND 10 FOR ₹1 LAKH CAPITAL: THE MATHEMATICAL SOVEREIGN APEX:
To Quant Repos (NautilusTrader, Riskfolio-Lib, Kelly Criterion) & Antigravity Master Archive:
1. MATHEMATICAL PROOF: Scaling ₹1,00,00,000 is exactly a 100x return from ₹1,00,000 (compared to 10,000x from ₹1,000!). What is the mathematical probability of achieving 100x vs 10,000x under Fractional Kelly (f*/4)?
2. At 8% to 10% monthly compounding: (1.10)^24 ≈ 9.85x (₹10 Lakhs in 2 years), (1.10)^48 ≈ 97x (₹1 Crore in 4 years).
3. DUAL-ENGINE APEX ACCELERATION: When Rajon's AI Agency (Engine 1) injects ₹50,000 to ₹1,00,00,00 monthly into Engine 2 (Automated Hedged Spreads + 44-MA Swings + Dhan DMA Bot), prove mathematically how the timeline to ₹1 Crore collapses from 4 years down to 18-24 months!"""
    }
]

def run_apple_script(script):
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def submit_and_wait_response(tab_idx, prompt, timeout=75):
    print(f"\n[🚀 SWITCHING TAB] Activating Tab {tab_idx}...")
    run_apple_script(f'''
    tell application "Google Chrome"
        set active tab index of front window to {tab_idx}
    end tell
    ''')
    time.sleep(2.0)

    escaped_prompt = json.dumps(prompt)
    js_insert = f'''
    (() => {{
        let ta = document.querySelector("textarea.query-box-input") || document.querySelector("textarea[aria-label=\\"Query box\\"]") || document.querySelector("textarea");
        if (!ta) return "NO_TA";
        ta.focus();
        ta.select();
        document.execCommand("selectAll", false, null);
        document.execCommand("insertText", false, {escaped_prompt});
        ta.dispatchEvent(new Event("input", {{ bubbles: true }}));
        ta.dispatchEvent(new Event("change", {{ bubbles: true }}));
        return "INSERTED";
    }})()
    '''
    escaped_js = js_insert.replace('\\', '\\\\').replace('"', '\\"')
    res_ins = run_apple_script(f'''
    tell application "Google Chrome"
        tell active tab of front window
            return execute javascript "{escaped_js}"
        end tell
    end tell
    ''')
    print(f"   [Input Status]: {res_ins}")
    time.sleep(1.0)

    js_submit = '''
    (() => {
        let btn = document.querySelector("button.submit-button") || document.querySelector("button[aria-label=\\"Submit\\"]");
        if (!btn) {
            let btns = Array.from(document.querySelectorAll("button"));
            for (let b of btns) {
                if (b.innerText.includes("Submit") || b.getAttribute("aria-label") === "Submit" || b.querySelector("svg")) {
                    btn = b;
                    break;
                }
            }
        }
        if (btn && !btn.disabled) {
            btn.click();
            return "CLICKED";
        }
        return btn ? "DISABLED" : "NO_BTN";
    })()
    '''
    escaped_sub = js_submit.replace('\\', '\\\\').replace('"', '\\"')
    res_sub = run_apple_script(f'''
    tell application "Google Chrome"
        tell active tab of front window
            return execute javascript "{escaped_sub}"
        end tell
    end tell
    ''')
    print(f"   [Submit Status]: {res_sub}")

    print("   [⏳ GENERATING] Waiting for Gemini NotebookLM response...")
    start_time = time.time()
    last_len = 0
    stable_count = 0

    while time.time() - start_time < timeout:
        time.sleep(3.0)
        js_poll = '''
        (() => {
            let stopBtn = document.querySelector("button[aria-label=\\"Stop\\"]") || document.querySelector("button.stop-button");
            let turns = Array.from(document.querySelectorAll(".model-response, conversation-turn, .message-content"));
            let text = turns.length > 0 ? turns[turns.length - 1].innerText : document.body.innerText;
            return JSON.stringify({thinking: !!stopBtn, len: text.length});
        })()
        '''
        escaped_poll = js_poll.replace('\\', '\\\\').replace('"', '\\"')
        raw = run_apple_script(f'''
        tell application "Google Chrome"
            tell active tab of front window
                return execute javascript "{escaped_poll}"
            end tell
        end tell
        ''')
        try:
            d = json.loads(raw)
            is_thinking = d.get("thinking", False)
            cur_len = d.get("len", 0)
            if cur_len != last_len:
                print(f"      [Streaming] length={cur_len} chars...", flush=True)
                last_len = cur_len
                stable_count = 0
            elif cur_len > 200 and not is_thinking:
                stable_count += 1
                if stable_count >= 2:
                    print(f"   [✅ COMPLETED] Response stable ({cur_len} chars)", flush=True)
                    break
        except Exception:
            pass

    js_read = 'document.body.innerText'
    full_text = run_apple_script(f'''
    tell application "Google Chrome"
        tell active tab of front window
            return execute javascript "{js_read}"
        end tell
    end tell
    ''')
    
    marker = "COURIER DISPATCH"
    if marker in full_text:
        parts = full_text.split(marker)
        ans = parts[-1].strip()
    else:
        ans = full_text[-4000:].strip()

    return ans

def main():
    print("=" * 80)
    print("⚡ RESUMING SOVEREIGN 1 LAKH DEBATE FOR ROUNDS 8, 9, 10")
    print("=" * 80)

    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    for item in REMAINING_ROUNDS:
        r_num = item["round"]
        tab_idx = item["tab_idx"]
        entity = item["entity"]
        sender = item["sender"]
        prompt = item["prompt"]

        print(f"\n[{r_num}/10] 🔥 EXECUTING ₹1 LAKH ROUND {r_num}: [{sender}] ➔ [{entity}] (Tab {tab_idx})")
        resp = submit_and_wait_response(tab_idx, prompt, timeout=75)
        resp_clean = resp[:4500].strip()
        print(f"   [Extracted]: {len(resp_clean)} characters.")

        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
        INSERT INTO courier_1lakh_round_debate
        (timestamp, round_number, sender, receiver, tab_index, prompt_couriered, grounded_response, char_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (ts, r_num, sender, entity, tab_idx, prompt, resp_clean, len(resp_clean)))
        conn.commit()

        with open(TRANSCRIPT_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n---\n## 📬 Round {r_num}: [{sender}] ➔ [{entity}] (Tab {tab_idx})\n")
            f.write(f"- **Timestamp**: `{ts}`\n\n")
            f.write(f"### 📨 Couriered Challenge:\n> {prompt.replace(chr(10), chr(10) + '> ')}\n\n")
            f.write(f"### 🧠 Grounded Response:\n{resp_clean}\n\n")

        time.sleep(2.0)

    # Export all 10 rounds to JSON
    cur.execute("SELECT round_number, sender, receiver, tab_index, char_count, grounded_response FROM courier_1lakh_round_debate ORDER BY round_number ASC")
    all_rows = cur.fetchall()
    results = {}
    for r in all_rows:
        results[f"ROUND_{r[0]}_{r[2]}"] = {
            "round": r[0],
            "sender": r[1],
            "entity": r[2],
            "tab_index": r[3],
            "char_count": r[4],
            "response": r[5]
        }
    with open(JSON_OUTPUT, "w", encoding="utf-8") as jf:
        json.dump(results, jf, ensure_ascii=False, indent=2)

    conn.close()
    print("\n[✅] All 10 rounds saved in SQLite and JSON!")

if __name__ == "__main__":
    main()
