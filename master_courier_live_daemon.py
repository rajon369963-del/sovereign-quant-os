#!/usr/bin/env python3
"""
master_courier_live_daemon.py
=============================
Master 65-Minute Autonomous Courier Debate Relay Daemon for Sovereign Quant OS.
Conducts an authentic, live, physical multi-turn dialectic debate across individual
Google NotebookLM brains directly inside live Google Chrome.

Speakers:
1. Vivek Bajaj (Macro & Institutional)
2. Ghanshyam Tech (Price Action & Inside Bar Scalping)
3. Subasish Pani (5-EMA Momentum & Breakdown)
4. Saketh R (Options Greeks, Theta Decay & Margin Realities)
5. Nitin Murarka (Order Flow Imbalance & CVD)
6. PR Sundar (SEBI Margins, Micro Friction & Capital Defense)
7. Dr. Mukul Agrawal (Forensics, Delivery Spikes & Operator Traps)
8. Siddharth Bhanushali (44-MA Trend Filter & Pullback Discipline)
9. Abhishek Kar (Market Psychology & Crowd FOMO / Panic)
10. Sept 15 Crash News Intel (Ground Truth Crash Diagnostics)
11. 200+ Quant Repos Sovereign Brain (Mathematical Drift, OU & HFT Models)
"""

import datetime
import json
import sqlite3
import subprocess
import time
from pathlib import Path

DB_PATH = "/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite"
OUTPUT_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/live_courier_debate_turns")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NOTEBOOKS = [
    {
        "key": "VIVEK_BAJAJ",
        "name": "Vivek Bajaj (Macro & Institutional)",
        "id": "b1398c08-e8d3-48de-b645-7e0c821a576f",
        "role": "Macro Economics, Global Liquidity & 10,000-ft Top-Down Capital Preservation",
        "stance": "कल के -280 पॉइंट क्रैश के बाद मार्केट पर पैनिक है। DXY और क्रूड $108 के दबाव में कैपिटल प्रिजर्वेशन प्राथमिक नियम है। बिना ट्रेंड कन्फर्मेशन एक्सपायरी पर ट्रेड करना आत्महत्या है।"
    },
    {
        "key": "GHANSHYAM_TECH",
        "name": "Ghanshyam Tech (Price Action & Inside Bar)",
        "id": "f67ae556-94ee-4c82-865a-c09c55a90c6d",
        "role": "Pure Price Action, Inside Bar Scalping & 51,000 Call Wall Resistance",
        "stance": "पहले 15 मिनट (9:15-9:30 AM) में कोई ट्रेड नहीं। जब तक 51,000 के ऊपर बैंक निफ्टी 5-मिनट क्लोज न दे, तब तक कॉल नहीं छूना। इनसाइड बार के ब्रेकआउट पर 1:2 स्कैल्पिंग ही असली प्रॉफिट देती है।"
    },
    {
        "key": "SUBASISH_PANI",
        "name": "Subasish Pani (Power of Stocks)",
        "id": "b0e64cde-7112-432a-8329-5eddcd4252de",
        "role": "5-EMA Momentum, Trend Following Breakdown & Asymmetric Risk-Reward",
        "stance": "अगर सुबह 5-मिनट कैंडल 5-EMA से दूर बने और उसका लो ब्रेक हो, तो बिना सोचे पुट बाइंग या सेलिंग एग्जीक्यूट करो। ओवरसोल्ड बाउंस का इंतजार करने वाले हमेशा बड़ा ट्रेंड मिस करते हैं।"
    },
    {
        "key": "SAKETH_R",
        "name": "Saketh R (Options Greeks & Volatility)",
        "id": "279ad740-9e0d-4e00-a713-a72cffb62a3f",
        "role": "Options Greeks, Theta Decay Non-Linearity & Capital Margins",
        "stance": "₹1,008 में भारतीय बाजार में ऑप्शन सेलिंग असंभव है (कम से कम ₹1.2 लाख मार्जिन चाहिए)। अगर ₹1,008 से ऑप्शन बाइंग करनी है तो केवल दोपहर 1:30 बजे के बाद 1 लॉट डीप इन-द-मनी या स्ट्रिक्ट स्टॉपलॉस के साथ ही संभव है।"
    },
    {
        "key": "NITIN_MURARKA",
        "name": "Nitin Murarka (Order Flow & CVD)",
        "id": "e5d3eb8c-1492-4670-a4e3-08a5b2fb0f6d",
        "role": "Order Flow Imbalance (OFI), Cumulative Volume Delta (CVD) & Institutional Depth",
        "stance": "चार्ट पर कैंडलस्टिक अक्सर झूठ बोलती हैं। असली सच ऑर्डर बुक में है। जब बिड-आस्क स्प्रेड में आक्रामक सेल ऑर्डर्स (नेगेटिव CVD) दिखें, तभी डाउनट्रेंड पक्का होता है। बिना वॉल्यूम डेल्टा ट्रेड लेना अंधाधुंध जुआ है।"
    },
    {
        "key": "PR_SUNDAR",
        "name": "PR Sundar (Capital Preservation & Friction)",
        "id": "0f2a60f3-294a-473b-a8a1-36a983e05d3c",
        "role": "SEBI Margins, Micro Friction Defense & Hedged Execution",
        "stance": "₹1,008 की कैपिटल पर ₹48.50 का ब्रोकरेज फ्रिक्शन 4.8% की सीधी चपत है। दो गलत ट्रेड में 10% कैपिटल खत्म। इसलिए छोटे अकाउंट को पहले 5x लेवरेज वाले कैश इक्विटी में ग्रो करना चाहिए, एफ-एंड-ओ में नहीं।"
    },
    {
        "key": "DR_MUKUL_AGRAWAL",
        "name": "Dr. Mukul Agrawal (Forensics & Manipulation)",
        "id": "a1903e26-f589-42ff-ac02-132bcd02115d",
        "role": "Forensic Delivery Spikes, Operator Traps & Value Anchors",
        "stance": "क्रैश के बाद ऑपरेटर अक्सर सुबह रिटेल को फंसाने के लिए फेक ग्रीन कैंडल बनाते हैं। केवल डिलीवरी वॉल्यूम और संस्थागत फुटप्रिंट देखकर ही ट्रेड चुनो। पेनी ऑप्शन में मत कूदो।"
    },
    {
        "key": "SIDDHARTH_BHANUSHALI",
        "name": "Siddharth Bhanushali (Swing & 44-MA)",
        "id": "3884d9e5-c21c-4646-82c9-e4500427f102",
        "role": "44-Moving Average Trend Filter & Disciplined Pullback Entry",
        "stance": "जब तक प्राइस 44-MA के नीचे है, केवल सेल-ऑन-राइज की सोचो। पुलबैक पर जब 44-MA पर रिजेक्शन कैंडल बने, तभी एंट्री लो। 1:2 रिस्क-रिवार्ड के बिना ट्रेड करना अनुशासनहीनता है।"
    },
    {
        "key": "ABHISHEK_KAR",
        "name": "Abhishek Kar (Market Psychology & Heuristics)",
        "id": "31fa34c1-8a6e-4ebc-b7ae-3d416e215594",
        "role": "Retail Psychology, FOMO Liquidation & Behavioral Counter-Trading",
        "stance": "एक्सपायरी के दिन 95% रिटेल ट्रेडर हीरो-टू-जीरो के चक्कर में अपनी बची-खुची पूंजी गंवाते हैं। जब सब पैनिक में पुट खरीद रहे हों, तब ऑपरेटर शॉर्ट कवरिंग लाते हैं। भीड़ के उलट सोचना ही मुनाफा दिलाता है।"
    },
    {
        "key": "NEWS_15_SEPT",
        "name": "15th Sept Post-Close News & Crash Intel",
        "id": "d90752b4-deaf-4e8f-8419-6c8947767647",
        "role": "September 15 Crash Ground Truth, Brent $108, FII Net Outflows & Expiry Context",
        "stance": "कल 15 सितंबर को निफ्टी 279.50 अंक गिरकर 23,118 पर बंद हुआ। ब्रेंट क्रूड $108 प्रति बैरल पार कर चुका है और विदेशी निवेशकों (FIIs) ने ₹3,400 करोड़ की शुद्ध बिकवाली की है। आज बुधवार को बैंक निफ्टी एक्सपायरी पर वोलैटिलिटी अत्यधिक उच्च रहेगी।"
    },
    {
        "key": "QUANT_REPOS",
        "name": "200+ Quant & Algo Trading GitHub Repos",
        "id": "55417afe-c86a-4d8a-8c41-19cb4375dc59",
        "role": "Mathematical Drift (OU), NautilusTrader HFT, Ed Thorp Expectancy & Riskfolio",
        "stance": "भावनाएं और टिप्स शून्य मूल्य के हैं। एड थॉर्प का फॉर्मूला E = P*W - (1-P)*L और ऑर्नेस्टीन-उहलेनबेक ड्रिफ्ट मॉडल (theta*(mu - X_t)) ही असली सत्य हैं। जब तक पॉजिटिव एक्सपेक्टेंसी न हो, ट्रेड एग्जीक्यूट नहीं होना चाहिए।"
    }
]

def run_js_in_notebook_tab(js_code):
    sc = f'''
    tell application "Google Chrome"
        activate
        repeat with w in windows
            repeat with i from 1 to count of tabs of w
                set t to tab i of w
                if (URL of t) contains "notebook.google.com" then
                    set active tab index of w to i
                    set index of w to 1
                    tell t
                        return execute javascript {json.dumps(js_code)}
                    end tell
                end if
            end repeat
        end repeat
        return "TAB_NOT_FOUND"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', sc], capture_output=True, text=True)
    return res.stdout.strip()

def navigate_to_notebook(notebook_id):
    print(f"\n[+] Navigating Chrome to Notebook: {notebook_id}...")
    sc = f'''
    tell application "Google Chrome"
        activate
        repeat with w in windows
            repeat with i from 1 to count of tabs of w
                set t to tab i of w
                if (URL of t) contains "notebook.google.com" then
                    set active tab index of w to i
                    set index of w to 1
                    set URL of t to "https://notebook.google.com/notebook/{notebook_id}"
                    return "NAVIGATED"
                end if
            end repeat
        end repeat
        return "NO_TAB"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', sc], capture_output=True, text=True).stdout.strip()
    if res != "NAVIGATED":
        print(f"[-] Warning: Failed to find notebook.google.com tab. Result: {res}")
        return False
        
    for attempt in range(25):
        time.sleep(1.5)
        chk = run_js_in_notebook_tab('!!document.querySelector("textarea[aria-label=\'Query box\']")')
        if chk == "true":
            print(f"[✓] Notebook {notebook_id} query box ready.")
            return True
    print(f"[-] Warning: Timeout waiting for query box in notebook {notebook_id}")
    return False

def submit_query_and_collect_response(notebook_id, query_text):
    # 1. Count initial responses
    init_res = run_js_in_notebook_tab("document.querySelectorAll('.to-user-message-card-content').length.toString()")
    try: initial_count = int(init_res)
    except: initial_count = 0
    print(f"  -> Initial chat responses count: {initial_count}")
    
    # 2. Focus and insert prompt
    insert_js = f"""
    (() => {{
        let ta = document.querySelector("textarea[aria-label='Query box']");
        if (!ta) return "NO_TA";
        ta.focus();
        ta.select();
        document.execCommand('selectAll', false, null);
        document.execCommand('insertText', false, {json.dumps(query_text)});
        return "INSERTED";
    }})()
    """
    ins_status = run_js_in_notebook_tab(insert_js)
    if ins_status != "INSERTED":
        print(f"  [-] Failed to insert text: {ins_status}")
        return None
        
    time.sleep(1.2) # Allow Angular change detection to mark form valid
    
    # 3. Click submit
    click_js = """
    (() => {
        let ta = document.querySelector("textarea[aria-label='Query box']");
        let form = ta ? ta.closest('form') : null;
        let btn = form ? form.querySelector('button.submit-button, button[aria-label="Submit"]') : null;
        if (btn && !btn.disabled) {
            btn.click();
            return "CLICKED";
        }
        return btn ? "DISABLED" : "NO_BTN";
    })()
    """
    click_status = run_js_in_notebook_tab(click_js)
    print(f"  -> Submit click status: {click_status}")
    if click_status != "CLICKED":
        # Retry with second tick
        time.sleep(1.5)
        click_status = run_js_in_notebook_tab(click_js)
        print(f"  -> Retry submit click status: {click_status}")
        if click_status != "CLICKED":
            return None
            
    # 4. Poll for streaming response
    print(f"  -> Polling Gemini response in {notebook_id}...")
    start_time = time.time()
    for tick in range(60):
        time.sleep(2.5)
        poll_js = f"""
        (() => {{
            let responses = document.querySelectorAll('.to-user-message-card-content');
            let count = responses.length;
            if (count > {initial_count}) {{
                let latest = responses[responses.length - 1];
                let text = (latest.innerText || "").trim();
                let stopBtn = document.querySelector("button[aria-label='Stop'], button.stop-button");
                return JSON.stringify({{
                    ready: !stopBtn && text.length > 80,
                    length: text.length,
                    has_stop: !!stopBtn
                }});
            }}
            return JSON.stringify({{ ready: false, count: count }});
        }})()
        """
        status_str = run_js_in_notebook_tab(poll_js)
        status = json.loads(status_str or "{}")
        elapsed = time.time() - start_time
        
        if tick % 4 == 0 or status.get("ready"):
            print(f"     [{elapsed:.1f}s] Length: {status.get('length', 0)} chars | Ready: {status.get('ready', False)}")
            
        if status.get("ready"):
            fetch_js = "document.querySelectorAll('.to-user-message-card-content')[document.querySelectorAll('.to-user-message-card-content').length - 1].innerText"
            full_text = run_js_in_notebook_tab(fetch_js)
            print(f"  [✓] Complete response captured! ({len(full_text):,d} chars in {elapsed:.1f}s)")
            return full_text
            
    print("[-] Response generation timed out.")
    return None

def build_courier_dialectic_challenge(from_speaker, to_speaker, previous_response, round_num):
    now_str = datetime.datetime.now().strftime("%H:%M:%S")
    prompt = f"""[SOVEREIGN COURIER DIALECTIC CHALLENGE — ROUND {round_num} | {now_str}]
TO: {to_speaker['name']} ({to_speaker['role']})
FROM: Antigravity Courier (relaying direct testimony from {from_speaker['name']})

प्रिय {to_speaker['name']},
आज बुधवार 16 सितंबर 2026 को बैंक निफ्टी की वीकली एक्सपायरी है।
कल भारतीय बाजारों में -280 अंक का क्रैश दर्ज हुआ (निफ्टी 23,118 पर बंद हुआ, ब्रेंट क्रूड $108 पर है और एफआईआई की ₹3,400 करोड़ की बिकवाली हुई है)।
हमारे पास लाइव धन ब्रोकर पर केवल ₹1,008 की वास्तविक ट्रेडिंग कैपिटल है।

पूर्व वक्ता ({from_speaker['name']}) ने अभी-अभी आपके सामने यह आधिकारिक पक्ष और चुनौती रखी है:
---
"{previous_response[:1400]}..."
---

{to_speaker['name']} सर, आप अपने क्षेत्र ({to_speaker['role']}) के शीर्ष विशेषज्ञ हैं।
कृपया अपने 300 वीडियोज/सोर्सेज के वास्तविक डेटा, चार्ट पैटर्न्स, और केस स्टडीज के आधार पर निम्नलिखित 4 बिंदुओं पर निर्भीक और ठोस उत्तर दें:

1. पूर्व वक्ता के तर्कों का खंडन (खंडन/हेत्वाभास) या समर्थन:
   - {from_speaker['name']} ने जो नियम या लेवल्स बताए हैं, उसमें क्या खामी है?
   - क्या ₹1,008 जैसी छोटी पूंजी के साथ उनका तरीका एक्सपायरी के दिन खाता खाली (wipe-out) कर देगा?

2. आज बुधवार एक्सपायरी के लिए आपका अचूक प्राइस/क्वांट एक्शन प्लान:
   - बैंक निफ्टी और निफ्टी के लिए आपके क्रिटिकल सपोर्ट और रेजिस्टेंस लेवल्स क्या हैं?
   - आपकी मुख्य रणनीति (जैसे 5-EMA, इनसाइड बार, ओएफआई डेल्टा, थीटा डिके, 44-MA या क्वांट ड्रिफ्ट) आज सुबह 9:30 बजे और दोपहर 1:45 बजे कब और किस कंडीशन पर बाय या सेल ट्रिगर करेगी?

3. मैक्सिमम प्रॉफिट और ब्रोकरेज फ्रिक्शन का गणित:
   - ₹1,008 की कैपिटल पर धन ब्रोकर के ₹48.50 एफ-एंड-ओ ब्रोकरेज फ्रिक्शन (4.8% ड्रैग) के सामने आप कैसे पॉजिटिव एक्सपेक्टेंसी निकालेंगे?
   - क्या आप 5x लेवरेज वाले इंट्राडे एम-आई-एस कैश इक्विटी (जैसे टाटा स्टील/इंफोसिस) में ट्रेड करने की सलाह देंगे जहां फ्रिक्शन मात्र ₹1.45 है, या केवल प्रॉफिट के पैसे से 1 लॉट ऑप्शन खरीदने का सुझाव देंगे?

4. अगले विशेषज्ञ के लिए एक तीखा काउंटर-प्रश्न:
   - इस डिबेट के अगले वक्ता के लिए एक ऐसा प्रश्न छोड़ें जिसका उत्तर उन्हें अपने सोर्सेज के आधार पर देना अनिवार्य हो।

कृपया केवल अपने अपलोड किए गए सोर्सेज से सटीक प्रमाण और डेटा दें। कोई सामान्य या किताबी बातें न करें।"""
    return prompt

def log_turn(turn_data):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO courier_live_debate_turns 
    (timestamp, round_number, from_speaker, to_speaker, notebook_id, query_text, response_text, response_chars, duration_seconds)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        turn_data["timestamp"],
        turn_data["round_number"],
        turn_data["from_speaker"],
        turn_data["to_speaker"],
        turn_data["notebook_id"],
        turn_data["query_text"],
        turn_data["response_text"],
        len(turn_data["response_text"]),
        turn_data["duration_seconds"]
    ))
    conn.commit()
    conn.close()
    
    fname = f"TURN_{turn_data['turn_idx']:03d}_{turn_data['to_key']}_R{turn_data['round_number']}.md"
    fpath = OUTPUT_DIR / fname
    md_content = f"""# 🏛️ COURIER LIVE DEBATE TURN {turn_data['turn_idx']:03d}
- **Timestamp**: {turn_data['timestamp']}
- **Round**: {turn_data['round_number']}
- **From**: {turn_data['from_speaker']}
- **To**: {turn_data['to_speaker']}
- **Notebook URL**: [Open Notebook](https://notebook.google.com/notebook/{turn_data['notebook_id']})
- **Execution Duration**: {turn_data['duration_seconds']:.1f} seconds
- **Response Length**: {len(turn_data['response_text']):,d} characters

---

## 📨 Authentic Courier Query Sent into NotebookLM
```text
{turn_data['query_text']}
```

---

## 💡 Gemini Grounded Response from {turn_data['to_speaker']}
{turn_data['response_text']}
"""
    fpath.write_text(md_content, encoding="utf-8")
    print(f"[✓] Persisted Turn {turn_data['turn_idx']} to SQLite & {fname}")

def run_courier_daemon(duration_minutes=65):
    print("=" * 80)
    print("🚀 LAUNCHING 65-MINUTE SOVEREIGN COURIER DEBATE RELAY DAEMON")
    print(f"Start Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target Duration: >= {duration_minutes} minutes")
    print(f"Total Notebook Brains Registered: {len(NOTEBOOKS)}")
    print("=" * 80)
    
    start_total_time = time.time()
    end_target_time = start_total_time + (duration_minutes * 60)
    
    current_speaker = NOTEBOOKS[0] # Vivek Bajaj
    latest_response = NOTEBOOKS[0]["stance"]
    
    turn_idx = 1
    round_num = 1
    
    while time.time() < end_target_time:
        print(f"\n{'#' * 80}")
        print(f"🔄 STARTING ROUND {round_num} OF LIVE COURIER DEBATE")
        print(f"{'#' * 80}")
        
        # Traverse through all speakers in order
        for next_idx in range(len(NOTEBOOKS)):
            if time.time() >= end_target_time:
                print("[!] Target duration reached. Wrapping up daemon.")
                break
                
            next_speaker = NOTEBOOKS[next_idx]
            # Don't ask the same speaker immediately in round 1
            if next_speaker["id"] == current_speaker["id"] and turn_idx > 1:
                continue
                
            print("\n" + "-" * 70)
            print(f"🎯 TURN {turn_idx:02d} (Round {round_num}) | COURIER RELAY:")
            print(f"   From: {current_speaker['name']}")
            print(f"   To  : {next_speaker['name']}")
            print(f"   Notebook ID: {next_speaker['id']}")
            print("-" * 70)
            
            nav_ok = navigate_to_notebook(next_speaker["id"])
            if not nav_ok:
                print(f"[-] Skipping {next_speaker['name']} due to navigation failure.")
                continue
                
            prompt = build_courier_dialectic_challenge(current_speaker, next_speaker, latest_response, round_num)
            
            turn_start = time.time()
            resp = submit_query_and_collect_response(next_speaker["id"], prompt)
            turn_duration = time.time() - turn_start
            
            if resp:
                turn_data = {
                    "turn_idx": turn_idx,
                    "timestamp": datetime.datetime.now().isoformat(),
                    "round_number": round_num,
                    "from_speaker": current_speaker["name"],
                    "to_speaker": next_speaker["name"],
                    "to_key": next_speaker["key"],
                    "notebook_id": next_speaker["id"],
                    "query_text": prompt,
                    "response_text": resp,
                    "duration_seconds": turn_duration
                }
                log_turn(turn_data)
                latest_response = resp
                current_speaker = next_speaker
                turn_idx += 1
            else:
                print(f"[-] Warning: Failed to collect response from {next_speaker['name']}.")
                
            time.sleep(3.0)
            
        round_num += 1
        
    total_elapsed = time.time() - start_total_time
    print("\n" + "=" * 80)
    print("🎉 65-MINUTE SOVEREIGN COURIER DEBATE COMPLETE!")
    print(f"Total Execution Time: {total_elapsed/60:.2f} minutes")
    print(f"Total Live Authentic Turns Completed: {turn_idx - 1}")
    print(f"Rounds Completed: {round_num - 1}")
    print(f"Database Record: {DB_PATH} -> courier_live_debate_turns")
    print(f"Markdown Turn Files: {OUTPUT_DIR}")
    print("=" * 80)

if __name__ == "__main__":
    run_courier_daemon(duration_minutes=65)
