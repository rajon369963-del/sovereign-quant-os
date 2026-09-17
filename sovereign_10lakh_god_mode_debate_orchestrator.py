#!/usr/bin/env python3
"""
⚡ SOVEREIGN 10-ROUND GOD MODE DEBATE ORCHESTRATOR FOR ₹10,00,000 CAPITAL ($12,000)
=============================================================================
Conducts an authentic, sequential 10-round God Mode debate across:
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

Topic: ₹10 Lakh Capital God Mode Architecture — Scaling from ₹10 Lakhs to ₹1 Crore (10x Leap).
"""

import subprocess
import time
import json
import sqlite3
import os
from pathlib import Path

BASE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os")
DB_PATH = BASE_DIR / "grand_10k_trading_hypergraph.sqlite"
TRANSCRIPT_FILE = BASE_DIR / "LIVE_COURIER_10LAKH_DEBATE_TRANSCRIPT.md"
JSON_OUTPUT = BASE_DIR / "COURIER_10LAKH_DEBATE_FINAL_SYNTHESIS.json"

ROUNDS = [
    {
        "round": 1,
        "tab_idx": 1,
        "entity": "GHANSHYAM_TECH",
        "sender": "COURIER (RAJON DAS)",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 1 FOR ₹10 LAKH (1,000,000) CAPITAL:
Rajon has reached the institutional milestone: ₹10,00,000 ($12,000) capital in Dhan. Scaling to ₹1 Crore is now only a 10x leap!
1. At ₹10 Lakhs, how does a trader transition from an intraday retail scalper to an institutional operator? What is the maximum option lots allowed (is 3-4 lots the limit)?
2. In 5x MIS Cash Equity, ₹10 Lakhs provides ₹50,00,000 (5 Million INR) buying power. How should a trader exploit this massive liquidity in bluechip stocks?
3. What is your strict rule on profit protection at ₹10 Lakhs: should profits above ₹10 Lakhs be moved to liquid funds weekly?"""
    },
    {
        "round": 2,
        "tab_idx": 2,
        "entity": "VIVEK_BAJAJ",
        "sender": "GHANSHYAM_TECH",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 2 FOR ₹10 LAKH CAPITAL: FROM GHANSHYAM TECH TO VIVEK BAJAJ:
Ghanshyam Tech defined institutional position sizing and weekly profit protection for ₹10 Lakhs.
Vivek Sir, designing the Sovereign Macro Portfolio for ₹10 Lakhs:
1. How should ₹10,00,000 be structured across asset classes: The 60/30/10 Model (₹6 Lakhs Core Positional/Sectoral Equity, ₹3 Lakhs Delta-Neutral Derivatives, ₹1 Lakh Liquid Cash)?
2. How does combining Equity Delivery with Index Put options create a fortress portfolio that never suffers a >10% drawdown even during market crashes?
3. What macro indicators (DXY, US 10Y Yield, FII Long-Short Ratio) dictate when to increase or decrease market exposure?"""
    },
    {
        "round": 3,
        "tab_idx": 4,
        "entity": "NITIN_MURARKA",
        "sender": "VIVEK_BAJAJ",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 3 FOR ₹10 LAKH CAPITAL: FROM VIVEK BAJAJ TO NITIN MURARKA:
Vivek Bajaj structured the 60/30/10 Sovereign Portfolio and crash protection.
Nitin Sir, on Institutional Order Flow and Volume Profiling at ₹10 Lakhs:
1. With ₹10 Lakhs (deploying ₹10-15 Lakhs in active setups), how can Rajon trade alongside DIIs/FIIs using multi-strike Open Interest (OI) analysis and Volume Weighted Average Price (VWAP) bands?
2. How do institutional algorithms execute iceberg orders in large caps, and how can a ₹10 Lakh trader identify institutional accumulation before the breakout?
3. What is your golden rule for trade management when holding multi-lot positions?"""
    },
    {
        "round": 4,
        "tab_idx": 3,
        "entity": "SUBASISH_PANI",
        "sender": "NITIN_MURARKA",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 4 FOR ₹10 LAKH CAPITAL: FROM NITIN MURARKA TO SUBASISH PANI:
Nitin Murarka detailed institutional volume accumulation and multi-strike analysis.
Subasish Sir (Power of Stocks):
1. For ₹10,00,000 capital, what is the exact mathematical risk per trade? (Is 0.5% to 1% = ₹5,000 to ₹10,000 max risk per trade the golden rule)?
2. At 1:3 Risk-to-Reward, capturing ₹15,000 to ₹30,000 profit per winning trade, prove mathematically how a 50% win rate doubles ₹10 Lakhs to ₹20 Lakhs in 6 months!
3. What is the hard daily loss limit (e.g. ₹15,000 max daily loss) to guarantee 66 consecutive days of survival runway?"""
    },
    {
        "round": 5,
        "tab_idx": 5,
        "entity": "SAKETH_R",
        "sender": "SUBASISH_PANI",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 5 FOR ₹10 LAKH CAPITAL: FROM SUBASISH PANI TO SAKETH R:
Subasish established the ₹5k-₹10k risk rule and 1:3 RR for ₹10 Lakhs.
Saketh R, on Institutional Delta-Neutral Option Selling:
1. With ₹10,00,000 capital, how can Rajon deploy 10-12 lots of Delta-Neutral Short Strangles with Far-OTM Long Wings (Iron Condors) on Nifty?
2. How does collecting Theta decay generate a consistent 3% to 5% monthly return (₹30,000 to ₹50,000 per month) with a 85% statistical win rate?
3. What is your mechanical adjustment rule when one side is breached (e.g., rolling untested side or shifting strikes)?"""
    },
    {
        "round": 6,
        "tab_idx": 6,
        "entity": "PR_SUNDAR",
        "sender": "SAKETH_R",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 6 FOR ₹10 LAKH CAPITAL: FROM SAKETH R TO PR SUNDAR:
Saketh demonstrated 10-lot Delta-Neutral Iron Condors generating 3-5% monthly.
PR Sundar Sir, on Capital Preservation and Reaching ₹1 Crore from ₹10 Lakhs:
1. Scaling ₹10 Lakhs to ₹1 Crore is only a 10x journey. Why is avoiding catastrophic tail risk (e.g., Ukraine war, Covid crashes) the ONLY thing required to reach ₹1 Crore?
2. How should non-directional option selling be combined with monthly dividend/fixed-income cashflows to compound ₹10 Lakhs at 35-40% CAGR?
3. What is your personal rule for sleep-well trading: why should Rajon never hold a position that causes elevated heart rate at night?"""
    },
    {
        "round": 7,
        "tab_idx": 7,
        "entity": "ABHISHEK_KAR",
        "sender": "PR_SUNDAR",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 7 FOR ₹10 LAKH CAPITAL: FROM PR SUNDAR TO ABHISHEK KAR:
PR Sundar stressed sleep-well trading and compounding at 35-40% CAGR.
Abhishek Kar, on God Mode Psychology & Big Number Desensitization:
1. When capital reaches ₹10 Lakhs, daily fluctuations can easily be ₹15,000 - ₹30,000 (equal to an entire month's average salary in India). How must Rajon psychologically desensitize himself to these numbers?
2. How do high-net-worth traders avoid the 'Lifestyle Trap' and resist the urge to buy luxury liabilities before crossing ₹1 Crore?
3. What mental conditioning ensures a trader stays monk-like and executes without greed or fear at the seven-figure level?"""
    },
    {
        "round": 8,
        "tab_idx": 8,
        "entity": "SIDDHARTH_BHANUSHALI",
        "sender": "ABHISHEK_KAR",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 8 FOR ₹10 LAKH CAPITAL: FROM ABHISHEK KAR TO SIDDHARTH BHANUSHALI:
Abhishek Kar addressed psychological desensitization and the monk-like mindset.
Siddharth Bhanushali, on 44-MA Swing Scaling with ₹6 Lakhs:
1. With ₹10 Lakhs, deploying ₹6 Lakhs into 4 distinct high-momentum sectoral leaders (₹1.5 Lakhs in each stock): how does this capture multi-week 20-30% trends?
2. When a stock gives a 25% run on ₹1.5 Lakhs (generating ₹37,500 per stock), how does compounding and pyramiding scale ₹10 Lakhs to ₹30 Lakhs in 18 months?
3. How does positional 44-MA swing trading eliminate screen addiction, allowing Rajon to run his tech agency simultaneously?"""
    },
    {
        "round": 9,
        "tab_idx": 9,
        "entity": "DR_MUKUL_AGRAWAL",
        "sender": "SIDDHARTH_BHANUSHALI",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 9 FOR ₹10 LAKH CAPITAL: FROM SIDDHARTH BHANUSHALI TO DR. MUKUL AGRAWAL:
Siddharth demonstrated ₹6 Lakhs deployed across 4 sectoral leaders on 44-MA.
Dr. Mukul Agrawal, on Creating ₹1 Crore from ₹10 Lakhs via Multibagger Themes:
1. In India's massive $5 Trillion economy expansion (Renewables, Defense, AI/Tech Infrastructure, Electronics EMS), how does a ₹10 Lakh portfolio pick 4-5 future multibaggers?
2. Why does buying fundamentally supreme companies at early cycle stages and holding for 3-4 years historically generate 5x to 10x returns?
3. What is your final master roadmap for taking ₹10 Lakhs all the way to ₹1 Crore ethically, legally, and sustainably?"""
    },
    {
        "round": 10,
        "tab_idx": 15,
        "entity": "QUANT_REPOS_AND_MASTER_ARCHIVE",
        "sender": "ALL 9 GURUS",
        "prompt": """COURIER DISPATCH - GOD MODE ROUND 10 FOR ₹10 LAKH CAPITAL: THE SOVEREIGN 1 CRORE THEOREM:
To Quant Repos (NautilusTrader, Riskfolio-Lib, Kelly Criterion) & Antigravity Master Archive:
1. MATHEMATICAL THEOREM: Scaling ₹10,00,000 to ₹1,00,00,000 is exactly a 10x return (1,000%).
   - At 4% monthly compounded return (from 10-lot Delta-Neutral Theta Selling + 44-MA Swings):
     (1.04)^59 ≈ 10.3x (59 months / ~5 years).
   - At 6% monthly compounded return:
     (1.06)^40 ≈ 10.3x (40 months / ~3.3 years).
2. DUAL-ENGINE GOD MODE ACCELERATION:
   - Engine 1 (Rajon's AI Automation Agency / Software Grants): Injects ₹1,00,000 monthly into Engine 2.
   - Prove mathematically how adding ₹1 Lakh monthly cashflow to a ₹10 Lakh base compounding at 5% monthly collapses the timeline to ₹1 Crore from 5 years down to ONLY 20-24 MONTHS!
3. Deliver the final, comprehensive Sovereign God Mode Execution Rulebook for Rajon Das."""
    }
]

def run_apple_script(script):
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def init_db():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courier_10lakh_god_mode_debate (
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
    
    marker = "COURIER DISPATCH"
    if marker in full_text:
        parts = full_text.split(marker)
        ans = parts[-1].strip()
    else:
        ans = full_text[-4000:].strip()

    return ans

def main():
    print("=" * 80)
    print("⚡ STARTING SOVEREIGN 10-ROUND GOD MODE DEBATE RELAY FOR ₹10,00,000 CAPITAL")
    print("=" * 80)
    init_db()

    with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
        f.write("# 🏛️ SOVEREIGN 10-ROUND GOD MODE DEBATE TRANSCRIPT FOR ₹10,00,000 CAPITAL\n")
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

        print(f"\n[{r_num}/10] 🔥 EXECUTING GOD MODE ROUND {r_num}: [{sender}] ➔ [{entity}] (Tab {tab_idx})")
        resp = submit_and_wait_response(tab_idx, prompt, timeout=75)
        resp_clean = resp[:4500].strip()
        print(f"   [Extracted]: {len(resp_clean)} characters.")

        # Persist to DB
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
        INSERT INTO courier_10lakh_god_mode_debate
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
    print("🎉 ALL 10 ROUNDS OF GOD MODE DEBATE COMPLETED SUCCESSFULLY!")
    print(f"Recorded into SQLite: {DB_PATH} (table: courier_10lakh_god_mode_debate)")
    print(f"Transcript Markdown: {TRANSCRIPT_FILE}")
    print(f"JSON Synthesis: {JSON_OUTPUT}")
    print("=" * 80)

if __name__ == "__main__":
    main()
