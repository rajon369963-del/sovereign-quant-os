#!/usr/bin/env python3
"""
⚡ SOVEREIGN 10-ROUND COURIER DEBATE ORCHESTRATOR FOR ₹10,000 CAPITAL ($120)
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

Topic: ₹10,000 Capital Architecture — How to Scale from ₹10k to ₹1,00,000 and onwards to ₹1 Crore.
"""

import subprocess
import time
import json
import sqlite3
import os
from pathlib import Path

BASE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os")
DB_PATH = BASE_DIR / "grand_10k_trading_hypergraph.sqlite"
TRANSCRIPT_FILE = BASE_DIR / "LIVE_COURIER_10K_DEBATE_TRANSCRIPT.md"
JSON_OUTPUT = BASE_DIR / "COURIER_10K_DEBATE_FINAL_SYNTHESIS.json"

ROUNDS = [
    {
        "round": 1,
        "tab_idx": 1,
        "entity": "GHANSHYAM_TECH",
        "sender": "COURIER (RAJON DAS)",
        "prompt": """COURIER DISPATCH - ROUND 1 FOR ₹10,000 CAPITAL:
Rajon is now planning his next capital milestone: ₹10,000 ($120) in Dhan.
1. With ₹10,000, can a trader now trade 1 lot of Bank Nifty or Nifty options using your 9:20 candle or support-resistance breakout? Or is buying 1 lot options at ₹10,000 still dangerous?
2. If trading 5x MIS Cash Equity, ₹10,000 gives ₹50,000 buying power. How does 5x MIS Cash compare to 1 lot options for ₹10k capital?
3. What is the strict daily stop-loss limit and max trades allowed for ₹10,000 capital?"""
    },
    {
        "round": 2,
        "tab_idx": 2,
        "entity": "VIVEK_BAJAJ",
        "sender": "GHANSHYAM_TECH",
        "prompt": """COURIER DISPATCH - ROUND 2 FOR ₹10,000 CAPITAL: FROM GHANSHYAM TECH TO VIVEK BAJAJ:
Ghanshyam Tech has analyzed position sizing for ₹10,000.
Vivek Sir, looking at market macro and transaction economics:
1. At ₹10,000, statutory friction drops from 3.5% (at ₹1k) to ~0.35%. Does this 10x friction reduction allow active swing or positional trading?
2. How should a ₹10,000 portfolio be structured? Should it be a 70/30 Barbell (₹7,000 in Swing Cash/ETFs and ₹3,000 in 5x MIS Intraday), or 100% active?
3. What asset classes (equities, sectoral ETFs, gold/silver BeES) protect a ₹10,000 base while compounding?"""
    },
    {
        "round": 3,
        "tab_idx": 4,
        "entity": "NITIN_MURARKA",
        "sender": "VIVEK_BAJAJ",
        "prompt": """COURIER DISPATCH - ROUND 3 FOR ₹10,000 CAPITAL: FROM VIVEK BAJAJ TO NITIN MURARKA:
Vivek Bajaj analyzed asset allocation and the 10x friction drop for ₹10,000.
Nitin Sir, as the master of Order Flow and Institutional Volume:
1. With ₹10,000 capital (giving ₹50,000 exposure in 5x MIS Cash), how can Rajon track institutional VWAP and delivery volumes in large-cap liquid stocks?
2. Why do traders with ₹10,000 fail when they average down into losing trades, and what is your strict 'Never Average a Loser' rule?
3. What high-probability order flow setup should Rajon look for at 10:15 AM?"""
    },
    {
        "round": 4,
        "tab_idx": 3,
        "entity": "SUBASISH_PANI",
        "sender": "NITIN_MURARKA",
        "prompt": """COURIER DISPATCH - ROUND 4 FOR ₹10,000 CAPITAL: FROM NITIN MURARKA TO SUBASISH PANI:
Nitin Murarka emphasized order flow discipline and never averaging losers.
Subasish Sir (Power of Stocks):
1. For ₹10,000 capital, what is the exact mathematical risk per trade? (Should it be 2% = ₹200 per trade, aiming for ₹600 profit at 1:3 RR)?
2. If a trader takes 2 stop-losses a day (₹400 max daily loss = 4%), they have 25 consecutive days of survival buffer. Why is this 25-day runway psychologically bulletproof?
3. When winning trades occur, how do you trail stop-loss to ensure profits don't turn into losses?"""
    },
    {
        "round": 5,
        "tab_idx": 5,
        "entity": "SAKETH_R",
        "sender": "SUBASISH_PANI",
        "prompt": """COURIER DISPATCH - ROUND 5 FOR ₹10,000 CAPITAL: FROM SUBASISH PANI TO SAKETH R:
Subasish established the ₹200 risk per trade rule and 1:3 RR for ₹10k.
Saketh R, examining Options Greeks and Hedging:
1. Many beginners think ₹10,000 is enough to buy 1 lot ITM option. But if a 30-point stop loss hits in Nifty/Bank Nifty (₹750 to ₹1,500 loss), that is 7.5% to 15% of the account in ONE trade! Why does this Greek exposure violate all risk rules?
2. Can defined-risk hedged option spreads (credit spreads) be deployed with ₹10,000, or is margin still a hurdle?
3. Why does 5x MIS Cash Equity remain the mathematically superior vehicle at ₹10,000?"""
    },
    {
        "round": 6,
        "tab_idx": 6,
        "entity": "PR_SUNDAR",
        "sender": "SAKETH_R",
        "prompt": """COURIER DISPATCH - ROUND 6 FOR ₹10,000 CAPITAL: FROM SAKETH R TO PR SUNDAR:
Saketh showed that buying 1 lot options with ₹10k still carries 10-15% single-trade ruin risk.
PR Sundar Sir, on Capital Preservation and Scaling from ₹10k to ₹1,00,000:
1. Why is the transition from ₹10,000 to ₹1,00,000 (10x) the most critical crucible in a trader's career?
2. How should a trader manage drawdowns when their ₹10,000 dips to ₹9,000? What is your rule on reducing position size during drawdowns?
3. What is your advice on capital preservation when moving towards six figures?"""
    },
    {
        "round": 7,
        "tab_idx": 7,
        "entity": "ABHISHEK_KAR",
        "sender": "PR_SUNDAR",
        "prompt": """COURIER DISPATCH - ROUND 7 FOR ₹10,000 CAPITAL: FROM PR SUNDAR TO ABHISHEK KAR:
PR Sundar warned about managing drawdowns and scaling patiently.
Abhishek Kar, focusing on Trader Psychology and Ego Traps:
1. When a beginner's account grows to ₹10,000, the 'I Know The Market' ego trap triggers. How does overconfidence cause traders to oversize and blow up?
2. How should Rajon psychologically view losses (as tuition fees for data) vs. viewing them as personal failures?
3. What daily psychological routine must a trader practice before market opens at 9:15 AM?"""
    },
    {
        "round": 8,
        "tab_idx": 8,
        "entity": "SIDDHARTH_BHANUSHALI",
        "sender": "ABHISHEK_KAR",
        "prompt": """COURIER DISPATCH - ROUND 8 FOR ₹10,000 CAPITAL: FROM ABHISHEK KAR TO SIDDHARTH BHANUSHALI:
Abhishek Kar broke down the psychological ego traps at ₹10,000.
Siddharth Bhanushali, as the master of the 44 Moving Average:
1. With ₹10,000, how can Rajon start taking 44-MA swing trades on Daily charts in high-momentum stocks?
2. If buying ₹10,000 worth of stock on a 44-MA pullback with a 3% stop-loss (₹300 risk), how does capturing a 12-15% move (₹1,200 to ₹1,500 profit) compound the account without intraday screen stress?
3. How does the 44-MA strategy bridge the gap between ₹10,000 and ₹1,00,000?"""
    },
    {
        "round": 9,
        "tab_idx": 9,
        "entity": "DR_MUKUL_AGRAWAL",
        "sender": "SIDDHARTH_BHANUSHALI",
        "prompt": """COURIER DISPATCH - ROUND 9 FOR ₹10,000 CAPITAL: FROM SIDDHARTH BHANUSHALI TO DR. MUKUL AGRAWAL:
Siddharth demonstrated the 44-MA swing compounding from ₹10k to ₹1 Lakh.
Dr. Mukul Agrawal, for long-term multibagger momentum:
1. How can a ₹10,000 capital base participate in sectoral megatrends (e.g., green energy, electronics manufacturing, defense)?
2. Why is picking 2-3 fundamentally robust emerging companies with strong volume accumulation better than over-diversification for a small account?
3. What is your proven roadmap for turning ₹10,000 into ₹10 Lakhs and eventually ₹1 Crore?"""
    },
    {
        "round": 10,
        "tab_idx": 15,
        "entity": "QUANT_REPOS_AND_MASTER_ARCHIVE",
        "sender": "ALL 9 GURUS",
        "prompt": """COURIER DISPATCH - ROUND 10 FOR ₹10,000 CAPITAL: MATHEMATICAL PROOF & DUAL-ENGINE ACCELERATION:
To Quant Repos (NautilusTrader, Riskfolio-Lib, Kelly Criterion) & Antigravity Master Archive:
1. MATHEMATICAL PROOF: Scaling ₹10,000 to ₹1 Crore is a 1,000x return (compared to 10,000x from ₹1,000). How does this 10x reduction in required return change the probability of success and time horizon under Fractional Kelly (f*/4)?
2. Under 10-12% monthly compounding, how many months does ₹10,000 take to reach ₹1 Crore?
3. DUAL-ENGINE ACCELERATION: If Engine 1 (Rajon's AI Agency & Grant Cashflow) injects ₹30,000-₹50,000 monthly into Engine 2 (Dhan DMA Bot & 44-MA Swings), how rapidly does the portfolio cross ₹10 Lakhs and scale to ₹1 Crore?"""
    }
]

def run_apple_script(script):
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()

def init_db():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courier_10k_round_debate (
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
    print("⚡ STARTING SOVEREIGN 10-ROUND COURIER DEBATE RELAY FOR ₹10,000 CAPITAL")
    print("=" * 80)
    init_db()

    with open(TRANSCRIPT_FILE, "w", encoding="utf-8") as f:
        f.write("# 🏛️ SOVEREIGN 10-ROUND COURIER DEBATE TRANSCRIPT FOR ₹10,000 CAPITAL\n")
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

        print(f"\n[{r_num}/10] 🔥 EXECUTING ₹10,000 ROUND {r_num}: [{sender}] ➔ [{entity}] (Tab {tab_idx})")
        resp = submit_and_wait_response(tab_idx, prompt, timeout=75)
        resp_clean = resp[:4500].strip()
        print(f"   [Extracted]: {len(resp_clean)} characters.")

        # Persist to DB
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
        INSERT INTO courier_10k_round_debate
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
    print("🎉 ALL 10 ROUNDS OF ₹10,000 COURIER DEBATE COMPLETED SUCCESSFULLY!")
    print(f"Recorded into SQLite: {DB_PATH} (table: courier_10k_round_debate)")
    print(f"Transcript Markdown: {TRANSCRIPT_FILE}")
    print(f"JSON Synthesis: {JSON_OUTPUT}")
    print("=" * 80)

if __name__ == "__main__":
    main()
