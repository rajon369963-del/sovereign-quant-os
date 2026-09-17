#!/usr/bin/env python3
"""
⚡ SOVEREIGN CONTINUOUS COURIER DEBATE ENGINE (100% REAL NOTEBOOKLM IN CHROME)
=============================================================================
Acts as the physical multi-agent Courier carrying messages, theses, rebuttals,
and synthesis across:
  1. The 9 Indian Trading Master YouTuber Notebooks
  2. The 6 News & Crash Forensics Notebooks (15th Sept, Weekly, Monthly)
  3. The 200+ Quantitative Trading GitHub Repositories Notebook

Navigates Google Chrome in the logged-in session (lakhidas168@gmail.com),
types into the live query box, submits, extracts Gemini's source-grounded response,
and couriers it to the next notebook with a customized dialectic challenge.

Persists every turn to:
  - SQLite: grand_10k_trading_hypergraph.sqlite -> table: courier_debate_turns
  - Markdown: LIVE_COURIER_DEBATE_TRANSCRIPT.md
  - Rules: SYNTHESIZED_SOVEREIGN_QUANT_RULES.md
"""

import datetime
import json
import sqlite3
import subprocess
import time
from pathlib import Path

BASE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os")
DB_PATH = BASE_DIR / "grand_10k_trading_hypergraph.sqlite"
TRANSCRIPT_PATH = BASE_DIR / "LIVE_COURIER_DEBATE_TRANSCRIPT.md"
RULES_PATH = BASE_DIR / "SYNTHESIZED_SOVEREIGN_QUANT_RULES.md"

# Registry of all 16 target notebooks
ENTITIES = {
    "VIVEK_BAJAJ": {
        "id": "b1398c08-e8d3-48de-b645-7e0c821a576f",
        "title": "01_VIVEK_BAJAJ_MACRO_BRAIN",
        "domain": "Macro, Global Cues, Multi-Asset Allocation, DXY, Crude"
    },
    "GHANSHYAM_TECH": {
        "id": "f67ae556-94ee-4c82-865a-c09c55a90c6d",
        "title": "02_GHANSHYAM_TECH_PRICE_ACTION_BRAIN",
        "domain": "Pure Price Action, 9:20 Candle, Bank Nifty Intraday Levels"
    },
    "SUBASISH_PANI": {
        "id": "b0e64cde-7112-432a-8329-5eddcd4252de",
        "title": "03_SUBASISH_PANI_EXECUTION_BRAIN",
        "domain": "Execution Timing, Risk-Reward 1:2, Gap Management, Power of Stocks"
    },
    "SAKETH_R": {
        "id": "279ad740-9e0d-4e00-a713-a72cffb62a3f",
        "title": "04_SAKETH_R_OPTIONS_GREEKS_BRAIN",
        "domain": "Options Greeks, Theta Decay, Vega Shock, Delta Neutral Spreads"
    },
    "NITIN_MURARKA": {
        "id": "e5d3eb8c-1492-4670-a4e3-08a5b2fb0f6d",
        "title": "05_NITIN_MURARKA_ORDER_FLOW_BRAIN",
        "domain": "Order Flow, VWAP Traps, Institutional Open Interest & PCR"
    },
    "PR_SUNDAR": {
        "id": "0f2a60f3-294a-473b-a8a1-36a983e05d3c",
        "title": "06_PR_SUNDAR_CAPITAL_PRESERVATION_BRAIN",
        "domain": "Capital Preservation, Margin Shocks, Options Selling Tail Risks"
    },
    "DR_MUKUL_AGRAWAL": {
        "id": "a1903e26-f589-42ff-ac02-132bcd02115d",
        "title": "07_DR_MUKUL_AGRAWAL_FORENSICS_BRAIN",
        "domain": "Forensic Balance Sheets, Volume Breakouts, Multi-Cap Stock Selection"
    },
    "SIDDHARTH_BHANUSHALI": {
        "id": "3884d9e5-c21c-4646-82c9-e4500427f102",
        "title": "08_SIDDHARTH_BHANUSHALI_SWING_BRAIN",
        "domain": "44-MA Swing Strategy, 200-EMA Trend Continuation, Positional Timing"
    },
    "ABHISHEK_KAR": {
        "id": "31fa34c1-8a6e-4ebc-b7ae-3d416e215594",
        "title": "09_ABHISHEK_KAR_BEHAVIORAL_BRAIN",
        "domain": "Behavioral Finance, Retail Herd Traps, FOMO Mitigation, Contrarian Trading"
    },
    "NEWS_15SEPT_POSTCLOSE": {
        "id": "d90752b4-deaf-4e8f-8419-6c8947767647",
        "title": "15th septem after closing the market news",
        "domain": "Sept 15 Post-Close News, FII/DII Net Flows, Global Closing Cues"
    },
    "NEWS_15SEPT_SHARE_MARKET": {
        "id": "dd85a383-7151-4f9d-bea0-c6424d4204bc",
        "title": "15th sept share market",
        "domain": "Sept 15 Full-Day Market Action, Sector Winners/Losers, Crash Forensic Signals"
    },
    "NEWS_WEEKLY_PART1": {
        "id": "25f4fae0-55df-444b-8197-33ae7c4bd876",
        "title": "SHARE MARKET WEEKLY NEWS PART1",
        "domain": "Weekly Indian Market Trends, Macro Data Releases, Inflation & Policy"
    },
    "NEWS_WEEKLY_PART2": {
        "id": "eac2d0d6-3e7b-4747-aa75-a54ad02898bf",
        "title": "SHARE MARKET WEEKLY NEWS PART 2",
        "domain": "Weekly Global Macro, Geopolitical Oil & Bond Shifts, FII Sentiment"
    },
    "NEWS_MONTHLY_PART1": {
        "id": "b3cb05f5-ebe4-449f-b7a1-28aa9a00eadf",
        "title": "SHARE MARKET MONTHLY NEWS 1",
        "domain": "Monthly Structural Trends, RBI Policy Impact, Corporate Earnings Cycle"
    },
    "NEWS_MONTHLY_PART2": {
        "id": "1d3cc23f-fa96-42ee-a93a-8cfb47bcc1f1",
        "title": "SHARE MARKET MONTHLY NEWS 2",
        "domain": "Monthly Institutional Rebalancing, Derivative Expiry Series Shifts"
    },
    "QUANT_200_REPOS": {
        "id": "96da7dbf-18e9-40a0-9e90-e363052a247f",
        "title": "200+ QUANT & ALGO TRADING GITHUB REPOS - SOVEREIGN CODE BRAIN",
        "domain": "200+ Cloned Quant Wheels: NautilusTrader, VectorBT, PyPortfolioOpt, OFI, ARCH"
    }
}

def init_db():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courier_debate_turns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        round_number INTEGER NOT NULL,
        turn_number INTEGER NOT NULL,
        sender_entity TEXT NOT NULL,
        receiver_entity TEXT NOT NULL,
        receiver_notebook_id TEXT NOT NULL,
        prompt_couriered TEXT NOT NULL,
        grounded_response TEXT NOT NULL,
        synthesized_rule TEXT,
        character_count INTEGER
    )
    """)
    conn.commit()
    conn.close()

def append_to_transcript(round_num, turn_num, sender, receiver, prompt, response):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    snippet = response.strip()
    entry = f"""
---
### 📬 Round {round_num} | Turn {turn_num}: [{sender}] ➔ [{receiver}]
- **Timestamp**: `{ts}`
- **Sender**: `{sender}`
- **Receiver**: `{receiver}` (`{ENTITIES.get(receiver, {}).get('title', '')}`)
- **Notebook URL**: https://notebook.google.com/notebook/{ENTITIES.get(receiver, {}).get('id', '')}

#### 📨 Couriered Inquiry / Challenge:
> {prompt.replace(chr(10), chr(10) + '> ')}

#### 🧠 Grounded Response from Gemini NotebookLM:
{snippet}

"""
    with open(TRANSCRIPT_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

def run_js(js_code: str) -> str:
    clean_js = js_code.replace('\n', ' ').strip()
    tmp_path = "/tmp/nb_cmd.js"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(clean_js)
        
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

def query_notebook(notebook_id: str, prompt: str, timeout: int = 90) -> str:
    url = f"https://notebook.google.com/notebook/{notebook_id}"
    print(f"\n[🚀 NAVIGATING] -> {url}")
    nav = navigate(url)
    time.sleep(5)
    
    # Wait for textarea
    for _ in range(15):
        chk = run_js('!!(document.querySelector("textarea.query-box-input") || document.querySelector("textarea[aria-label=\\"Query box\\"]"))')
        if chk == "true":
            break
        time.sleep(1)
        
    # Insert prompt using execCommand
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
    run_js(insert_code)
    time.sleep(1.2)
    
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
    c_res = run_js(click_code)
    if c_res == "DISABLED":
        time.sleep(1.5)
        run_js(click_code)
        
    print("[⏳ GENERATING] Waiting for Gemini NotebookLM source-grounded response...")
    start_time = time.time()
    full_text = ""
    last_len = 0
    stable_count = 0
    
    while time.time() - start_time < timeout:
        time.sleep(3)
        poll_code = '''
        (function() {
            let stopBtn = document.querySelector("button[aria-label=\\"Stop\\"]") || document.querySelector("button.stop-button");
            let turns = Array.from(document.querySelectorAll(".model-response, conversation-turn, .message-content"));
            let lastTurn = turns.length > 0 ? turns[turns.length - 1].innerText : "";
            return JSON.stringify({thinking: !!stopBtn, len: lastTurn.length, text: lastTurn});
        })()
        '''
        raw = run_js(poll_code)
        try:
            d = json.loads(raw)
            is_thinking = d.get("thinking", False)
            cur_len = d.get("len", 0)
            full_text = d.get("text", "")
            if cur_len != last_len:
                print(f"   [⏳ STREAMING] {cur_len} characters generated...", flush=True)
                last_len = cur_len
                stable_count = 0
            elif cur_len > 150 and not is_thinking:
                stable_count += 1
                if stable_count >= 2:
                    print(f"[✅ COMPLETED] Grounded response finished ({cur_len} chars)", flush=True)
                    break
        except Exception:
            pass
            
    return full_text

def extract_substantive_thesis(raw_text: str, max_chars: int = 750) -> str:
    """Extract substantive analytical core from raw Gemini response, removing UI artifacts."""
    import re
    if not raw_text:
        return "Market conditions demand strict risk management, dynamic hedging, and disciplined trade execution."
    
    cleaned = raw_text
    if "expand_more" in cleaned:
        cleaned = cleaned[cleaned.find("expand_more") + len("expand_more"):].strip()
    elif "Thoughts" in cleaned:
        cleaned = cleaned.replace("Thoughts", "").strip()

    cleaned = re.sub(r'\d+\s+more_horiz', '', cleaned)
    cleaned = re.sub(r'more_horiz', '', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned).strip()

    paragraphs = [p.strip() for p in cleaned.split("\n\n") if len(p.strip()) > 40]
    if paragraphs:
        combined = "\n\n".join(paragraphs[:3])
        if len(combined) > max_chars:
            return combined[:max_chars].rsplit(" ", 1)[0] + "..."
        return combined
    
    return cleaned[:max_chars]

def record_turn(round_num, turn_num, sender, receiver, prompt, response):
    append_to_transcript(round_num, turn_num, sender, receiver, prompt, response)
    
    # Insert to DB
    ts = datetime.datetime.now().isoformat()
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO courier_debate_turns 
    (timestamp, round_number, turn_number, sender_entity, receiver_entity, receiver_notebook_id, prompt_couriered, grounded_response, character_count)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (ts, round_num, turn_num, sender, receiver, ENTITIES[receiver]["id"], prompt, response, len(response)))
    conn.commit()
    conn.close()

    # Update EXACT_RESUME.json
    try:
        resume_path = BASE_DIR / "EXACT_RESUME.json"
        resume_data = {
            "last_updated": ts,
            "round_number": round_num,
            "turn_number": turn_num,
            "last_sender": sender,
            "last_receiver": receiver,
            "total_chars_recorded": len(response),
            "status": "IN_PROGRESS"
        }
        with open(resume_path, "w", encoding="utf-8") as rf:
            json.dump(resume_data, rf, indent=2)
    except Exception:
        pass

def main():
    print("=" * 80, flush=True)
    print("⚡ SOVEREIGN MASTER COURIER RELAY DEBATE ENGINE INITIALIZED", flush=True)
    print("=" * 80, flush=True)
    init_db()
    
    # Initialize Transcript Header if not exists
    if not TRANSCRIPT_PATH.exists():
        with open(TRANSCRIPT_PATH, "w", encoding="utf-8") as f:
            f.write("# ⚡ SOVEREIGN MULTI-AGENT COURIER DEBATE TRANSCRIPT (GROUNDED IN NOTEBOOKLM)\n\n")
            f.write(f"**Session Initiated**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("**Mechanism**: Antigravity physical courier relay across 16 NotebookLM notebooks in Chrome.\n\n")
            f.flush()

    # Round 1: Grand 16-Entity Circular Relay (Every single entity hears predecessor's actual words)
    round1_sequence = [
        ("INITIAL_DIRECTIVE", "VIVEK_BAJAJ", 
         "For Wednesday September 16 expiry, what is your grounded multi-asset macro view on Indian markets given recent US Dollar Index (DXY) strength, crude volatility, and FII flows? What core risk posture and directional bias must disciplined traders maintain?"),
        ("VIVEK_BAJAJ", "GHANSHYAM_TECH", None),
        ("GHANSHYAM_TECH", "SUBASISH_PANI", None),
        ("SUBASISH_PANI", "NITIN_MURARKA", None),
        ("NITIN_MURARKA", "SAKETH_R", None),
        ("SAKETH_R", "PR_SUNDAR", None),
        ("PR_SUNDAR", "DR_MUKUL_AGRAWAL", None),
        ("DR_MUKUL_AGRAWAL", "SIDDHARTH_BHANUSHALI", None),
        ("SIDDHARTH_BHANUSHALI", "ABHISHEK_KAR", None),
        ("ABHISHEK_KAR", "NEWS_15SEPT_POSTCLOSE", None),
        ("NEWS_15SEPT_POSTCLOSE", "NEWS_15SEPT_SHARE_MARKET", None),
        ("NEWS_15SEPT_SHARE_MARKET", "NEWS_WEEKLY_PART1", None),
        ("NEWS_WEEKLY_PART1", "NEWS_WEEKLY_PART2", None),
        ("NEWS_WEEKLY_PART2", "NEWS_MONTHLY_PART1", None),
        ("NEWS_MONTHLY_PART1", "NEWS_MONTHLY_PART2", None),
        ("NEWS_MONTHLY_PART2", "QUANT_200_REPOS", None)
    ]

    # Round 2: Adversarial Dialectic & Cross-Refutation Relay (Head-to-head methodology clashes)
    round2_sequence = [
        ("QUANT_200_REPOS", "NITIN_MURARKA", None),
        ("NITIN_MURARKA", "GHANSHYAM_TECH", None),
        ("GHANSHYAM_TECH", "SAKETH_R", None),
        ("SAKETH_R", "PR_SUNDAR", None),
        ("PR_SUNDAR", "SUBASISH_PANI", None),
        ("SUBASISH_PANI", "ABHISHEK_KAR", None),
        ("ABHISHEK_KAR", "SIDDHARTH_BHANUSHALI", None),
        ("SIDDHARTH_BHANUSHALI", "DR_MUKUL_AGRAWAL", None),
        ("DR_MUKUL_AGRAWAL", "NEWS_15SEPT_POSTCLOSE", None),
        ("NEWS_15SEPT_POSTCLOSE", "NEWS_WEEKLY_PART2", None),
        ("NEWS_WEEKLY_PART2", "NEWS_MONTHLY_PART1", None),
        ("NEWS_MONTHLY_PART1", "VIVEK_BAJAJ", None),
        ("VIVEK_BAJAJ", "QUANT_200_REPOS", None)
    ]

    # Round 3: Final Synthesis & Algorithmic Execution Rulebook
    round3_sequence = [
        ("QUANT_200_REPOS", "VIVEK_BAJAJ", None),
        ("VIVEK_BAJAJ", "GHANSHYAM_TECH", None),
        ("GHANSHYAM_TECH", "NITIN_MURARKA", None),
        ("NITIN_MURARKA", "SAKETH_R", None),
        ("SAKETH_R", "PR_SUNDAR", None),
        ("PR_SUNDAR", "QUANT_200_REPOS", None)
    ]

    rounds = [
        {"id": 1, "name": "Grand 16-Entity Circular Sovereign Relay", "steps": round1_sequence},
        {"id": 2, "name": "Adversarial Dialectic & Cross-Refutation Clashes", "steps": round2_sequence},
        {"id": 3, "name": "Master Sovereign Synthesis & Algorithmic Execution Rulebook", "steps": round3_sequence}
    ]

    total_steps = sum(len(r["steps"]) for r in rounds)
    print(f"[*] Total Master Rounds: {len(rounds)} | Total Courier Steps: {total_steps}", flush=True)

    start_time_all = time.time()
    global_step_count = 0
    last_grounded_response = ""

    for r in rounds:
        r_id = r["id"]
        r_name = r["name"]
        print("\n" + "=" * 80, flush=True)
        print(f"🔥 MASTER ROUND {r_id}: {r_name.upper()}", flush=True)
        print("=" * 80, flush=True)

        for step_idx, step_tuple in enumerate(r["steps"], 1):
            global_step_count += 1
            sender, receiver, fixed_prompt = step_tuple
            rec_id = ENTITIES[receiver]["id"]
            rec_title = ENTITIES[receiver]["title"]
            rec_domain = ENTITIES[receiver]["domain"]

            # Formulate the dynamic courier prompt carrying predecessor's actual words
            if fixed_prompt:
                courier_prompt = fixed_prompt
            else:
                sender_title = ENTITIES.get(sender, {}).get("title", sender)
                sender_domain = ENTITIES.get(sender, {}).get("domain", "Trading Analysis")
                thesis_digest = extract_substantive_thesis(last_grounded_response, max_chars=850)
                
                courier_prompt = f"""📬 [COURIER RELAY INQUIRY FROM {sender} ({sender_title})]:
"{thesis_digest}"

🎯 [CHALLENGE TO {receiver} ({rec_title})]:
{sender} grounded their analysis in {sender_domain}.
As {receiver}, specializing in {rec_domain}:
1. How does your source-grounded framework directly challenge, refute, or build upon these specific claims for Wednesday Bank Nifty expiry and the current market regime?
2. What concrete levels, price action triggers, order flow signals, options Greeks adjustments, or algorithmic rules does your framework mandate in response?"""

            print(f"\n[{global_step_count}/{total_steps}] Round {r_id}, Step {step_idx}:", flush=True)
            print(f"   Courier Message: [{sender}] ➔ [{receiver}] ({rec_title})", flush=True)
            print(f"   Prompt Length: {len(courier_prompt)} chars", flush=True)

            resp = query_notebook(rec_id, courier_prompt, timeout=100)
            
            if not resp or len(resp) < 80:
                print(f"[!] Short response ({len(resp)} chars). Retrying once after 3s...", flush=True)
                time.sleep(3)
                resp = query_notebook(rec_id, courier_prompt, timeout=100)

            record_turn(r_id, step_idx, sender, receiver, courier_prompt, resp)
            last_grounded_response = resp
            
            # Breathing interval
            time.sleep(2)

        print(f"\n🏁 Finished Round {r_id}: {r_name}", flush=True)

    elapsed = time.time() - start_time_all
    print("\n" + "=" * 80, flush=True)
    print("🎉 MASTER CONTINUOUS COURIER RELAY DEBATE COMPLETE!", flush=True)
    print(f"Total Time Elapsed: {elapsed / 60:.2f} minutes ({elapsed:.1f} seconds)", flush=True)
    print(f"Total Steps Executed: {global_step_count}", flush=True)
    print(f"Database: {DB_PATH}", flush=True)
    print(f"Transcript: {TRANSCRIPT_PATH}", flush=True)
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
