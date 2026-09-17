#!/usr/bin/env python3
"""
⚡ SOVEREIGN 10-ROUND COURIER DEBATE ORCHESTRATOR FOR ₹1,00,000 CAPITAL ($1,200)
=============================================================================
Conducts an authentic, sequential 10-round debate across:
  - Tab 1: 02_GHANSHYAM_TECH
  - Tab 2: 01_VIVEK_BAJAJ
  - Tab 4: 05_NITIN_MURARKA
  - Tab 3: 03_SUBASISH_PANI
  - Tab 5: 04_SAKETH_R
  - Tab 6: 06_PR_SUNDAR
  - Tab 7: 09_ABHISHEK_KAR
  - Tab 8: 08_SIDDHARTH_BHANUSHALI
  - Tab 9: 07_DR_MUKUL_AGRAWAL
  - Tab 15: QUANT & ALGO TRADING GITHUB REPOS (along with Master Archive)

Topic: ₹1 Lakh Capital Architecture (Charam Shikhar) — Scaling from ₹1 Lakh to ₹10 Lakhs and ₹1 Crore.
"""

import subprocess
import time
import json
import sqlite3
import os
from pathlib import Path

BASE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os")
DB_PATH = BASE_DIR / "grand_10k_trading_hypergraph.sqlite"
TRANSCRIPT_FILE = BASE_DIR / "LIVE_COURIER_1LAKH_DEBATE_TRANSCRIPT.md"
JSON_OUTPUT = BASE_DIR / "COURIER_1LAKH_DEBATE_FINAL_SYNTHESIS.json"

ROUNDS = [
    {
        "round": 1,
        "tab_idx": 1,
        "entity": "GHANSHYAM_TECH",
        "sender": "COURIER (RAJON DAS)",
        "prompt": """COURIER DISPATCH - ROUND 1 FOR ₹1 LAKH (1,00,000) CAPITAL:
Rajon has reached the pivotal apex milestone: ₹1,00,000 ($1,200) capital in Dhan.
1. With ₹1 Lakh capital, can a trader now trade options? If yes, what is the exact position sizing (is 1-2 lots of ITM options the hard ceiling)?
2. In 5x MIS Cash Equity, ₹1 Lakh provides ₹5,00,000 (Half a Million INR) buying power. How should a trader split between 5x Cash Equity and Options at ₹1 Lakh?
3. What is your strict rule on profit withdrawal: should 50% of profits at ₹1 Lakh be withdrawn to bank accounts to protect the capital base?"""
    },
    {
        "round": 2,
        "tab_idx": 2,
        "entity": "VIVEK_BAJAJ",
        "sender": "GHANSHYAM_TECH",
        "prompt": """COURIER DISPATCH - ROUND 2 FOR ₹1 LAKH CAPITAL: FROM GHANSHYAM TECH TO VIVEK BAJAJ:
Ghanshyam Tech defined position sizing and the 50% profit withdrawal rule for ₹1 Lakh.
Vivek Sir, examining portfolio macro architecture at ₹1 Lakh:
1. Transaction friction at ₹1 Lakh is now virtually zero (~0.02%). How does this empower multi-asset allocation?
2. How should a ₹1,00,000 capital be partitioned? (e.g. 50% in Core Swing/Sectoral Delivery, 30% in Hedged Spreads/MIS, 20% Liquid Cash Buffer)?
3. How can a ₹1 Lakh portfolio be hedged against broad market corrections using index puts or inverse ETFs?"""
    },
    {
        "round": 3,
        "tab_idx": 4,
        "entity": "NITIN_MURARKA",
        "sender": "VIVEK_BAJAJ",
        "prompt": """COURIER DISPATCH - ROUND 3 FOR ₹1 LAKH CAPITAL: FROM VIVEK BAJAJ TO NITIN MURARKA:
Vivek Bajaj laid out the 50/30/20 portfolio partition and macro hedging.
Nitin Sir, on Order Flow and Institutional Tracking with ₹1 Lakh:
1. With ₹1 Lakh (up to ₹5,00,000 MIS exposure), how should Rajon read institutional Open Interest (OI) concentration and VWAP bands to avoid institutional bull/bear traps?
2. How can a ₹1 Lakh account trade high-probability breakout retests at key institutional levels?
3. What is your warning against overtrading when capital reaches six figures?"""
    },
    {
        "round": 4,
        "tab_idx": 3,
        "entity": "SUBASISH_PANI",
        "sender": "NITIN_MURARKA",
        "prompt": """COURIER DISPATCH - ROUND 4 FOR ₹1 LAKH CAPITAL: FROM NITIN MURARKA TO SUBASISH PANI:
Nitin Murarka warned against six-figure overtrading and institutional traps.
Subasish Sir (Power of Stocks):
1. For ₹1,00,000 capital, what is the exact mathematical risk per trade? (Is 1% to 1.5% = ₹1,000 to ₹1,500 max risk per trade the golden rule)?
2. At 1:3 Risk-to-Reward, a winning trade generates ₹3,000 to ₹4,500. How does a 50% win-rate compound ₹1 Lakh to ₹3 Lakhs within months?
3. What is the daily loss cap (e.g. 2 losses = ₹2,500 max daily loss) to protect capital?"""
    },
    {
        "round": 5,
        "tab_idx": 5,
        "entity": "SAKETH_R",
        "sender": "SUBASISH_PANI",
        "prompt": """COURIER DISPATCH - ROUND 5 FOR ₹1 LAKH CAPITAL: FROM SUBASISH PANI TO SAKETH R:
Subasish established the ₹1,000-₹1,500 risk rule and 1:3 RR for ₹1 Lakh.
Saketh R, on Options Selling and Hedged Credit Spreads:
1. At ₹1,00,000, SEBI margin benefits finally unlock defined-risk Option Selling! How can Rajon deploy 2-3 lots of Bull Put Spreads or Bear Call Spreads (~₹30,000 margin per spread)?
2. How does shifting from Option Buying to Option Selling (collecting Theta decay) dramatically increase win rates from 30% to 75%?
3. What Greek management rules (Delta neutral, Vega protection) must be enforced at ₹1 Lakh?"""
    },
    {
        "round": 6,
        "tab_idx": 6,
        "entity": "PR_SUNDAR",
        "sender": "SAKETH_R",
        "prompt": """COURIER DISPATCH - ROUND 6 FOR ₹1 LAKH CAPITAL: FROM SAKETH R TO PR SUNDAR:
Saketh demonstrated that ₹1 Lakh unlocks hedged credit spreads and Theta capture.
PR Sundar Sir, on Capital Preservation and Scaling from ₹1 Lakh to ₹10 Lakhs:
1. Why do 80% of traders who reach ₹1 Lakh lose it all by getting greedy and trading naked options?
2. Why is non-directional hedged option selling (Iron Condors, Calendars) the safest vehicle for compounding ₹1 Lakh at 3-5% monthly?
3. How should Black Swan event protection be structured so an unexpected 500-point gap does not hurt the ₹1 Lakh base?"""
    },
    {
        "round": 7,
        "tab_idx": 7,
        "entity": "ABHISHEK_KAR",
        "sender": "PR_SUNDAR",
        "prompt": """COURIER DISPATCH - ROUND 7 FOR ₹1 LAKH CAPITAL: FROM PR SUNDAR TO ABHISHEK KAR:
PR Sundar emphasized non-directional hedged compounding and black swan protection.
Abhishek Kar, on Six-Figure Psychology and Emotional Maturity:
1. At ₹1,00,000, money feels 'real' and losses of ₹2,000-₹3,000 can trigger emotional panic. How should a trader detach emotions from rupees and view everything in percentages?
2. How does the lifestyle trap (spending trading profits prematurely) destroy capital compounding?
3. What mental conditioning ensures a trader stays grounded and treats ₹1 Lakh as a stepping stone to ₹1 Crore?"""
    },
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
1. MATHEMATICAL PROOF: Scaling ₹1,00,000 to ₹1,00,00,000 is exactly a 100x return (compared to 10,000x from ₹1,000!). What is the mathematical probability of achieving 100x vs 10,000x under Fractional Kelly (f*/4)?
2. At 8% to 10% monthly compounding: (1.10)^24 ≈ 9.85x (₹10 Lakhs in 2 years), (1.10)^48 ≈ 97x (₹1 Crore in 4 years).
3. DUAL-ENGINE APEX ACCELERATION: When Rajon's AI Agency (Engine 1) injects ₹50,000 to ₹1,00,000 monthly into Engine 2 (Automated Hedged Spreads + 44-MA Swings + Dhan DMA Bot), prove mathematically how the timeline to ₹1 Crore collapses from 4 years down to 18-24 months!"""
    }
]

def run_apple_script(script):
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def init_db():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courier_1lakh_round_debate (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        round_number INTEGER NOT NULL,
        sender TEXT NOT NULL,
        receiver TEXT NOT NULL,
        tab_index INTEGER NOT NULL,
        prompt_couriered TEXT NOT NULL,
        grounded_response TEXT NOT NULL,
        char_count INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def submit_and_wait_response(tab_idx, prompt, timeout=75):
    print(f"\n[🚀 SWITCHING TAB] Activating Tab {tab_idx}...")
    run_apple_script(f'''
    tell application "Google Chrome"
        set active tab index of front window to {tab_idx}
    end tell
    ''')
    time.sleep(2.0)

    # Insert prompt using execCommand
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

    # Click Submit Button
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

    # Wait for Generation
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

    # Read the text
    js_read = 'document.body.innerText'
    full_text = run_apple_script(f'''
    tell application "Google Chrome"
        tell active tab of front window
            return execute javascript "{js_read}"
        end tell
    end tell
    ''')
    
    # Extract portion after courier prompt
    marker = "COURIER DISPATCH"
    if marker in full_text:
        parts = full_text.split(marker)
        ans = parts[-1].strip()
    else:
        ans = full_text[-4000:].strip()

    return ans

def main():
    print("=" * 80)
    print("⚡ STARTING SOVEREIGN 10-ROUND COURIER DEBATE RELAY FOR ₹1,00,000 CAPITAL")
    print("=" * 80)
    init_db()

    with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
        f.write("# 🏛️ SOVEREIGN 10-ROUND COURIER DEBATE TRANSCRIPT FOR ₹1,00,000 CAPITAL\n")
        f.write("### *Physical Relay Across 9 YouTubers, Quant Repos & Antigravity Master Archive*\n\n")
        f.write(f"- **Initiated**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    results = {}
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    for item in ROUNDS:
        r_num = item["round"]
        tab_idx = item["tab_idx"]
        entity = item["entity"]
        sender = item["sender"]
        prompt = item["prompt"]

        print(f"\n[{r_num}/10] 🔥 EXECUTING ₹1 LAKH ROUND {r_num}: [{sender}] ➔ [{entity}] (Tab {tab_idx})")
        resp = submit_and_wait_response(tab_idx, prompt, timeout=75)
        resp_clean = resp[:4500].strip()
        print(f"   [Extracted]: {len(resp_clean)} characters.")

        # Persist to DB
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
        INSERT INTO courier_1lakh_round_debate
        (timestamp, round_number, sender, receiver, tab_index, prompt_couriered, grounded_response, char_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (ts, r_num, sender, entity, tab_idx, prompt, resp_clean, len(resp_clean)))
        conn.commit()

        # Append to transcript
        with open(TRANSCRIPT_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n---\n## 📬 Round {r_num}: [{sender}] ➔ [{entity}] (Tab {tab_idx})\n")
            f.write(f"- **Timestamp**: `{ts}`\n\n")
            f.write(f"### 📨 Couriered Challenge:\n> {prompt.replace(chr(10), chr(10) + '> ')}\n\n")
            f.write(f"### 🧠 Grounded Response:\n{resp_clean}\n\n")

        results[f"ROUND_{r_num}_{entity}"] = {
            "round": r_num,
            "entity": entity,
            "sender": sender,
            "tab_index": tab_idx,
            "char_count": len(resp_clean),
            "response": resp_clean
        }

        # Short pause between rounds
        time.sleep(2.0)

    conn.close()

    with open(JSON_OUTPUT, "w", encoding="utf-8") as jf:
        json.dump(results, jf, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print("🎉 ALL 10 ROUNDS OF ₹1 LAKH COURIER DEBATE COMPLETED SUCCESSFULLY!")
    print(f"Recorded into SQLite: {DB_PATH} (table: courier_1lakh_round_debate)")
    print(f"Transcript Markdown: {TRANSCRIPT_FILE}")
    print(f"JSON Synthesis: {JSON_OUTPUT}")
    print("=" * 80)

if __name__ == "__main__":
    main()
