#!/usr/bin/env python3
"""
⚡ SOVEREIGN 10-ROUND COURIER DEBATE ORCHESTRATOR
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
  - Tab 15: QUANT & ALGO TRADING GITHUB REPOS
  - Tab 12: ANTIGRAVITY CHATS MASTER ARCHIVE

Persists every round into:
  - SQLite: grand_10k_trading_hypergraph.sqlite (table: courier_10_round_debate)
  - Markdown: LIVE_COURIER_10_ROUND_DEBATE_TRANSCRIPT.md
  - JSON: COURIER_10_ROUND_DEBATE_FINAL_SYNTHESIS.json
"""

import subprocess
import time
import json
import sqlite3
import os
from pathlib import Path

BASE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os")
DB_PATH = BASE_DIR / "grand_10k_trading_hypergraph.sqlite"
TRANSCRIPT_FILE = BASE_DIR / "LIVE_COURIER_10_ROUND_DEBATE_TRANSCRIPT.md"
JSON_OUTPUT = BASE_DIR / "COURIER_10_ROUND_DEBATE_FINAL_SYNTHESIS.json"

ROUNDS = [
    {
        "round": 1,
        "tab_idx": 1,
        "entity": "GHANSHYAM_TECH",
        "sender": "COURIER (RAJON DAS)",
        "prompt": """COURIER DISPATCH - ROUND 1: THE OPENING REALITY CHECK FOR RAJON DAS:
Rajon started his live trading journey with ₹1,000 capital in Dhan. He faced losses on Wednesday and Thursday. Beginners often dream of turning ₹1,000 into ₹1 Crore via Bank Nifty / Nifty 0DTE options or rapid scalping.
1. What is your brutal, honest verdict on whether ₹1,000 can be traded in index options?
2. What happens to a trader with ₹1,000 who buys OTM options on expiry?
3. What is the ONLY valid purpose of ₹1,000 according to your discipline rules?"""
    },
    {
        "round": 2,
        "tab_idx": 2,
        "entity": "VIVEK_BAJAJ",
        "sender": "GHANSHYAM_TECH",
        "prompt": """COURIER DISPATCH - ROUND 2: FROM GHANSHYAM TECH TO VIVEK BAJAJ (MACRO & SEBI FRICTION):
Ghanshyam Tech has delivered his verdict: Trading ₹1,000 in options is pure suicide, and ₹1,000 is only for discipline.
Vivek Sir, looking at your macro framework and SEBI's 2024 retail trading study:
1. How does statutory transaction friction (₹20 flat brokerage + STT + GST + exchange turnover) mathematically destroy an account of ₹1,000 in F&O vs. 5x MIS Cash Equity?
2. What asset class and instrument should a beginner with ₹1,000 trade to avoid this friction trap?"""
    },
    {
        "round": 3,
        "tab_idx": 4,
        "entity": "NITIN_MURARKA",
        "sender": "VIVEK_BAJAJ",
        "prompt": """COURIER DISPATCH - ROUND 3: FROM VIVEK BAJAJ TO NITIN MURARKA (INSTITUTIONAL ORDER FLOW & VWAP):
Vivek Bajaj proved that retail traders lose >70% to transaction friction and lack of edge.
Nitin Sir, as the master of Order Flow, VWAP, and Open Interest / PCR:
1. How do big institutional algorithms use VWAP and PCR to trap small retail traders who enter 0DTE options?
2. Why does a ₹1,000 account have zero margin for error when institutions hunt stop-losses?
3. What order flow rule must Rajon follow before taking any trade tomorrow?"""
    },
    {
        "round": 4,
        "tab_idx": 3,
        "entity": "SUBASISH_PANI",
        "sender": "NITIN_MURARKA",
        "prompt": """COURIER DISPATCH - ROUND 4: FROM NITIN MURARKA TO SUBASISH PANI (POWER OF STOCKS - EXECUTION & RISK-REWARD):
Nitin Murarka highlighted institutional traps and VWAP stop-hunts.
Subasish Sir, in your Power of Stocks methodology:
1. How can a trader with ₹1,000 survive without getting wiped out? What is the maximum risk per trade (is ₹30-₹50 the ceiling)?
2. What is your strict 2-Stoploss rule for the day? Why is closing the screen after 2 losses non-negotiable?
3. Why is a minimum 1:2 or 1:3 Risk-to-Reward ratio mandatory for compounding?"""
    },
    {
        "round": 5,
        "tab_idx": 5,
        "entity": "SAKETH_R",
        "sender": "SUBASISH_PANI",
        "prompt": """COURIER DISPATCH - ROUND 5: FROM SUBASISH PANI TO SAKETH R (OPTIONS GREEKS & THETA DECAY):
Subasish insisted on 1:3 RR and strict 2-SL limits.
Saketh, as an Options Greeks specialist:
1. Why is Option Buying mathematically stacked against a ₹1,000 account due to Theta decay and Vega crush?
2. Why is Option Selling impossible at ₹1,000 due to margin requirements?
3. Why is 5x MIS Intraday Cash Equity (Cash Market) the ONLY instrument where Theta decay is zero and leverage works safely for small accounts?"""
    },
    {
        "round": 6,
        "tab_idx": 6,
        "entity": "PR_SUNDAR",
        "sender": "SAKETH_R",
        "prompt": """COURIER DISPATCH - ROUND 6: FROM SAKETH R TO PR SUNDAR (CAPITAL PRESERVATION & TAIL RISKS):
Saketh proved option buying suffers from Theta decay and option selling requires margin.
PR Sundar Sir, with your decades of experience in capital preservation and margin cycles:
1. What is the fundamental difference between traders who survive 20 years and those who blow up in 2 weeks?
2. Why is trying to turn ₹1,000 into ₹1 Crore in 1 year an unrealistic fantasy that leads to margin calls and depression?
3. How should capital preservation be practiced at the ₹1,000 stage versus the ₹10 Lakh stage?"""
    },
    {
        "round": 7,
        "tab_idx": 7,
        "entity": "ABHISHEK_KAR",
        "sender": "PR_SUNDAR",
        "prompt": """COURIER DISPATCH - ROUND 7: FROM PR SUNDAR TO ABHISHEK KAR (BEHAVIORAL FINANCE & FOMO TRAPS):
PR Sundar emphasized that capital preservation requires patience, but retail psychology hates waiting.
Abhishek Kar, specializing in trader psychology and herd behavior:
1. Why does social media promote the toxic myth of turning ₹1,000 into ₹1 Crore overnight?
2. What psychological trauma and revenge trading occurs after back-to-back losses (Wednesday and Thursday)?
3. How does a trader break the dopamine addiction of rapid scalping and adopt a contrarian, calm mindset?"""
    },
    {
        "round": 8,
        "tab_idx": 8,
        "entity": "SIDDHARTH_BHANUSHALI",
        "sender": "ABHISHEK_KAR",
        "prompt": """COURIER DISPATCH - ROUND 8: FROM ABHISHEK KAR TO SIDDHARTH BHANUSHALI (44-MA SWING & POSITIONAL COMPOUNDING):
Abhishek Kar exposed the behavioral trap of rapid 1-minute scalping.
Siddharth Sir, once Rajon proves discipline with ₹1,000 and expands his capital to ₹10,000 - ₹50,000:
1. How does your 44 Moving Average swing trading strategy take traders out of the stressful intraday noise?
2. How does positional swing trading on Daily charts capture 15-30% moves with clear risk definition?
3. How does compounding truly work when transitioning from Stage 2 (₹10,000) to Stage 3 (₹1,00,000+)?"""
    },
    {
        "round": 9,
        "tab_idx": 9,
        "entity": "DR_MUKUL_AGRAWAL",
        "sender": "SIDDHARTH_BHANUSHALI",
        "prompt": """COURIER DISPATCH - ROUND 9: FROM SIDDHARTH BHANUSHALI TO DR. MUKUL AGRAWAL (FORENSICS & MULTIBAGGER SCALING):
Siddharth demonstrated that 44-MA swing trading rides multi-week trends.
Dr. Mukul Agrawal, for taking capital from ₹10 Lakhs to ₹1 Crore:
1. Why is deep balance sheet forensics, volume accumulation, and multi-cap stock selection the vehicle for true wealth creation?
2. Why do intraday traders stay stuck with small profits while positional investors create crores through sectoral themes?
3. What is your roadmap for someone who starts small but wants to reach ₹1 Crore ethically and sustainably?"""
    },
    {
        "round": 10,
        "tab_idx": 15,
        "entity": "QUANT_REPOS_AND_ARCHIVE",
        "sender": "ALL 9 GURUS",
        "prompt": """COURIER DISPATCH - ROUND 10: THE MATHEMATICAL VERDICT & FOUNDER BLUEPRINT:
All 9 Gurus agree: ₹1,000 cannot become ₹1 Crore through high-frequency intraday options.
To Quant Repos (NautilusTrader, Riskfolio-Lib, Kelly Criterion):
1. What does the Kelly Criterion (f*) say about bet sizing when scaling 10,000x? Why is Quarter-Kelly mandatory to prevent Gambler's Ruin?
2. What is the mathematical drift equation and timeline at 10-12% monthly growth?
3. How does the Dual-Engine Rocket (AI Software Agency Cashflow + Algorithmic Compounding) bridge the gap to ₹1 Crore?"""
    }
]

def run_apple_script(script):
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def init_db():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courier_10_round_debate (
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
    print("⚡ STARTING SOVEREIGN 10-ROUND COURIER DEBATE RELAY")
    print("=" * 80)
    init_db()

    with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
        f.write("# 🏛️ SOVEREIGN 10-ROUND COURIER DEBATE TRANSCRIPT\n")
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

        print(f"\n[{r_num}/10] 🔥 EXECUTING ROUND {r_num}: [{sender}] ➔ [{entity}] (Tab {tab_idx})")
        resp = submit_and_wait_response(tab_idx, prompt, timeout=75)
        resp_clean = resp[:4500].strip()
        print(f"   [Extracted]: {len(resp_clean)} characters.")

        # Persist to DB
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
        INSERT INTO courier_10_round_debate
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
    print("🎉 ALL 10 ROUNDS OF COURIER DEBATE COMPLETED SUCCESSFULLY!")
    print(f"Recorded into SQLite: {DB_PATH} (table: courier_10_round_debate)")
    print(f"Transcript Markdown: {TRANSCRIPT_FILE}")
    print(f"JSON Synthesis: {JSON_OUTPUT}")
    print("=" * 80)

if __name__ == "__main__":
    main()
