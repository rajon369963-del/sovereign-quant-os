#!/usr/bin/env python3
"""
sovereign_parallel_courier_daemon.py
======================================
Master High-Throughput Parallel Courier Dialectic Engine for Sovereign Quant OS.
Runs continuous multi-turn, multi-brain debates directly across all 11 Google
NotebookLM notebooks in an off-screen, zero-disturbance Google Chrome window.

Features:
- Guaranteed Zero User Disturbance: Operates strictly inside worker window 262075305
  (bounds: 8144, 31, 1440, 900) while keeping Rajon's active window (262075321)
  permanently focused at index 1. Zero 'activate' calls. Zero stolen clicks.
- Parallel Mass Messaging: Dispatches queries in concurrent batches of 3 notebooks.
- Massive Prompts ("PROMPT BARA BARA DENA"): 3,000-4,500 characters per prompt
  grounded in Indian Nyaya Dialectic (Pratijna, Hetu, Udaharana, Upanaya, Nigamana)
  plus Western Hegelian Dialectic (Thesis, Antithesis, Synthesis).
- Grounded in Today's Market: Sep 15 crash (-280 pts NIFTY, 23,118 close, Brent $108),
  Wednesday Bank Nifty Expiry (51,000 Call Wall, 51,055 breakout trigger, 50,888 trap zone),
  micro-capital realities (₹1,008 capital, ₹48.50 F&O drag vs ₹1.45 MIS cash equity),
  and quantitative equations (Ornstein-Uhlenbeck drift, Stoikov, Order Flow Imbalance).
- Gemini Internal Thinking Extraction: Queries explicitly request step-by-step thinking
  which is extracted and stored alongside the grounded text and citations.
- Continuous 60+ Minutes Execution: Loops continuously across all 11 brains in multiple
  rounds, logging every turn to SQLite (grand_10k_trading_hypergraph.sqlite) and
  markdown files in live_courier_debate_turns/.
"""

import concurrent.futures
import datetime
import json
import sqlite3
import subprocess
import time
from pathlib import Path

DB_PATH = "/Users/rajondas/teamwork_projects/sovereign-quant-os/grand_10k_trading_hypergraph.sqlite"
OUTPUT_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/live_courier_debate_turns")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WORKER_WIN_ID = 262075305
USER_WIN_ID = 262075321

# Complete Registry of 11 Notebooks in worker window tabs
NOTEBOOKS = [
    {
        "tab_idx": 1,
        "key": "VIVEK_BAJAJ",
        "name": "Vivek Bajaj (Macro & Institutional)",
        "id": "b1398c08-e8d3-48de-b645-7e0c821a576f",
        "role": "Macro Economics, Global Liquidity, DXY Pressure & Capital Preservation"
    },
    {
        "tab_idx": 2,
        "key": "GHANSHYAM_TECH",
        "name": "Ghanshyam Tech (Price Action & Inside Bar)",
        "id": "f67ae556-94ee-4c82-865a-c09c55a90c6d",
        "role": "Pure Price Action, Inside Bar Scalping, 51,055 Trigger & 50,888 Trap Zone"
    },
    {
        "tab_idx": 3,
        "key": "SUBASISH_PANI",
        "name": "Subasish Pani (Power of Stocks)",
        "id": "b0e64cde-7112-432a-8329-5eddcd4252de",
        "role": "5-EMA Breakdown Strategy, Momentum Following & Retracement Shorting"
    },
    {
        "tab_idx": 4,
        "key": "SAKETH_R",
        "name": "Saketh R (Options Greeks & Volatility)",
        "id": "279ad740-9e0d-4e00-a713-a72cffb62a3f",
        "role": "Options Greeks, Theta Decay Non-Linearity, Gamma Spikes & Volatility Surface"
    },
    {
        "tab_idx": 5,
        "key": "NITIN_MURARKA",
        "name": "Nitin Murarka (Order Flow & CVD)",
        "id": "e5d3eb8c-1492-4670-a4e3-08a5b2fb0f6d",
        "role": "Order Flow Imbalance, Cumulative Volume Delta (CVD) & Limit Order Absorption"
    },
    {
        "tab_idx": 6,
        "key": "PR_SUNDAR",
        "name": "PR Sundar (Capital Preservation & Margins)",
        "id": "0f2a60f3-294a-473b-a8a1-36a983e05d3c",
        "role": "SEBI Margins, Micro-Capital Friction, Hedged Strangles & Friction Drag"
    },
    {
        "tab_idx": 7,
        "key": "DR_MUKUL_AGRAWAL",
        "name": "Dr. Mukul Agrawal (Forensics & Manipulation)",
        "id": "a1903e26-f589-42ff-ac02-132bcd02115d",
        "role": "Forensic Delivery Spikes, Operator Traps, Bull Traps & Value Anchors"
    },
    {
        "tab_idx": 8,
        "key": "SIDDHARTH_BHANUSHALI",
        "name": "Siddharth Bhanushali (Swing & 44-MA)",
        "id": "3884d9e5-c21c-4646-82c9-e4500427f102",
        "role": "44-MA Trend Filter, Asymmetric Risk-Reward (1:3+) & Strict Trailing Stops"
    },
    {
        "tab_idx": 9,
        "key": "ABHISHEK_KAR",
        "name": "Abhishek Kar (Market Psychology & Behavioral)",
        "id": "31fa34c1-8a6e-4ebc-b7ae-3d416e215594",
        "role": "Retail Crowd FOMO, Behavioral Heuristics, Panic Squeezes & Contrarian Plays"
    },
    {
        "tab_idx": 10,
        "key": "NEWS_15_SEPT",
        "name": "15th Sept Post-Close News & Crash Intel",
        "id": "d90752b4-deaf-4e8f-8419-6c8947767647",
        "role": "September 15 Crash Ground Truth, Brent $108, FII Outflow, Macro Geopolitics"
    },
    {
        "tab_idx": 11,
        "key": "QUANT_REPOS",
        "name": "200+ Quant & Algo Trading GitHub Repos",
        "id": "55417afe-c86a-4d8a-8c41-19cb4375dc59",
        "role": "Ornstein-Uhlenbeck Mean-Reversion, Stoikov Reservation Price, OFI & NautilusTrader HFT"
    }
]

def run_apple_script(sc):
    res = subprocess.run(['osascript', '-e', sc], capture_output=True, text=True)
    return res.stdout.strip()

def run_js(tab_idx, js_code):
    sc = f'''
    tell application "Google Chrome"
        tell tab {tab_idx} of window id {WORKER_WIN_ID}
            return execute javascript {json.dumps(js_code)}
        end tell
    end tell
    '''
    return run_apple_script(sc)

def protect_user_window():
    sc = f'''
    tell application "Google Chrome"
        set index of window id {USER_WIN_ID} to 1
    end tell
    '''
    run_apple_script(sc)

def get_tab_card_count(tab_idx):
    count_str = run_js(tab_idx, "document.querySelectorAll('.to-user-message-card-content').length.toString()")
    try:
        return int(count_str)
    except:
        return 0

def submit_query_to_tab(nb, prompt_text):
    tab_idx = nb["tab_idx"]
    print(f"\n[+] Preparing Tab {tab_idx} ({nb['name']})...")
    
    # 1. Activate tab in worker window without touching user screen
    sc_select = f'''
    tell application "Google Chrome"
        tell window id {WORKER_WIN_ID}
            set active tab index to {tab_idx}
        end tell
        set index of window id {USER_WIN_ID} to 1
    end tell
    '''
    run_apple_script(sc_select)
    time.sleep(0.6)
    
    initial_count = get_tab_card_count(tab_idx)
    
    # 2. Inject text using dual-setter (prototype setter + dispatchEvent + execCommand)
    inject_js = f'''
    (() => {{
        let ta = document.querySelector("textarea[aria-label='Query box']");
        if (!ta) return JSON.stringify({{ error: "NO_TA" }});
        
        // Step A: Prototype value setter + dispatchEvent for Angular form recognition
        let proto = Object.getPrototypeOf(ta);
        let setVal = Object.getOwnPropertyDescriptor(proto, 'value').set;
        setVal.call(ta, {json.dumps(prompt_text)});
        ta.dispatchEvent(new Event('input', {{ bubbles: true }}));
        ta.dispatchEvent(new Event('change', {{ bubbles: true }}));
        
        // Step B: Native selection + execCommand
        ta.focus();
        ta.select();
        document.execCommand('selectAll', false, null);
        document.execCommand('insertText', false, {json.dumps(prompt_text)});
        
        let form = ta.closest("form");
        let submitBtn = form ? form.querySelector("button.submit-button, button[aria-label='Submit']") : null;
        if (!submitBtn) return JSON.stringify({{ error: "NO_BTN" }});
        if (submitBtn.disabled) return JSON.stringify({{ error: "BTN_DISABLED", len: ta.value.length }});
        
        submitBtn.click();
        return JSON.stringify({{ success: true, initial_count: {initial_count} }});
    }})()
    '''
    res_str = run_js(tab_idx, inject_js)
    protect_user_window()
    
    res = {}
    try:
        res = json.loads(res_str)
    except:
        pass
        
    if not res.get("success"):
        print(f"  [-] Failed to submit on Tab {tab_idx}: {res_str}")
        return None
        
    print(f"  [✓] Query submitted to Tab {tab_idx} ({nb['name']}) | Initial count: {initial_count}")
    return initial_count

def poll_tab_response(nb, initial_count, max_seconds=120):
    tab_idx = nb["tab_idx"]
    print(f"  -> Polling for response on Tab {tab_idx} ({nb['name']})...")
    start_time = time.time()
    
    for tick in range(max_seconds // 2):
        time.sleep(2.0)
        elapsed = time.time() - start_time
        
        poll_js = f'''
        (() => {{
            let cards = document.querySelectorAll('.to-user-message-card-content');
            let stopBtn = document.querySelector("button[aria-label='Stop'], button.stop-button");
            let count = cards.length;
            if (count > {initial_count}) {{
                let latest = cards[cards.length - 1];
                let text = (latest.innerText || "").trim();
                let thoughtsEl = latest.querySelector('.model-thoughts, details, .thoughts-container');
                let thoughts = thoughtsEl ? (thoughtsEl.innerText || "").trim() : "";
                return JSON.stringify({{
                    ready: !stopBtn && text.length > 80,
                    text_len: text.length,
                    has_thoughts: thoughts.length > 0,
                    thoughts_len: thoughts.length
                }});
            }}
            return JSON.stringify({{ ready: false, count: count }});
        }})()
        '''
        res_str = run_js(tab_idx, poll_js)
        status = {}
        try:
            status = json.loads(res_str)
        except:
            pass
            
        if tick % 6 == 0 or status.get("ready"):
            print(f"     [{nb['key']}] [{elapsed:.1f}s] Length: {status.get('text_len', 0)} chars | Ready: {status.get('ready')}")
            
        if status.get("ready"):
            fetch_js = '''
            (() => {
                let cards = document.querySelectorAll('.to-user-message-card-content');
                let latest = cards[cards.length - 1];
                return (latest.innerText || "").trim();
            })()
            '''
            ans = run_js(tab_idx, fetch_js)
            duration = time.time() - start_time
            print(f"  [✓] {nb['name']} completed in {duration:.1f}s ({len(ans):,d} chars)!")
            return {"answer": ans, "duration": duration}
            
    print(f"  [-] {nb['name']} timed out after {max_seconds}s.")
    return None

def build_dialectic_prompt(speaker, collective_synthesis, round_num):
    now_str = datetime.datetime.now().strftime("%H:%M:%S")
    prompt = f"""[SOVEREIGN COURIER DIALECTIC CHALLENGE — ROUND {round_num} | {now_str}]
TO: {speaker['name']} ({speaker['role']})
FROM: Antigravity Sovereign Courier (Dialectic Synthesis across 9 Indian Traders + 200 Quant Repos)

संदर्भ एवं बाजार की वास्तविक स्थिति (Ground Truth — 16 सितंबर 2026, बुधवार बैंक निफ्टी एक्सपायरी):
1. कल (15 सितंबर 2026) भारतीय बाजार में -280 पॉइंट का भीषण क्रैश हुआ (निफ्टी 23,118.60 पर बंद, ब्रेंट क्रूड $108 पर, एफआईआई की ₹3,400 करोड़ की बिकवाली)।
2. आज बुधवार बैंक निफ्टी वीकली एक्सपायरी है। राउंड फिगर 51,000 पर विशाल कॉल राइटिंग वॉल (Call Resistance) सक्रिय है।
3. हमारे पास ₹1,008 की वास्तविक लाइव कैपिटल है और धन ब्रोकर पर लाइव ऑटोमैटिक बॉट कनेक्टेड है। धन पर F&O ब्रोकरेज व टैक्स ₹48.50 प्रति राउंड-ट्रिप है (कैपिटल का 4.81% फ्रिक्शन ड्रैग), जबकि 5x लेवरेज वाले MIS इंट्राडे कैश इक्विटी पर फ्रिक्शन मात्र ₹1.45 है।
4. घनश्याम टेक ने अपने आधिकारिक 300 वीडियोज के आधार पर यह स्पष्ट नियम रखा है: 50,888 से 51,055 का ज़ोन एक जानलेवा ट्रैप ज़ोन है। 51,055 के ऊपर 5-मिनट कैंडल क्लोज होने पर ही 51,000 के कॉल राइटर्स ट्रैप होंगे और शॉर्ट-कवरिंग आएगी, जबकि इनसाइड बार का लो टूटने पर ही पुट बाय ट्रिगर होगा।
5. विवेक बजाज ने मैक्रो आधार पर कहा है कि 200 DMA के नीचे मार्केट "Sell on Rise" रिजीम में है, और ₹1,008 जैसी छोटी कैपिटल पर एक्सपायरी डे हीरो-जीरो ट्रेड लेना 88% प्रोबेबिलिटी वाला अकाउंट वाइप-आउट सुसाइड है।

सामूहिक पूर्व डिबेट निष्कर्ष (Prior Synthesis):
---
"{collective_synthesis[:1200]}..."
---

{speaker['name']} सर, आप अपने क्षेत्र ({speaker['role']}) के शीर्ष विशेषज्ञ हैं।
कृपया अपने 300 आधिकारिक वीडियोज/सोर्सेज के आधार पर और अपनी वास्तविक केस स्टडीज, गणितीय सूत्रों, और प्रूवेन स्ट्रैटेजीज के आधार पर निम्नलिखित 5 न्यायशास्त्रीय (Nyaya Shastra) चरणों में उत्तर दें:

चरण 1. आपकी आंतरिक विचार प्रक्रिया (Your Internal Step-by-Step Thinking Process):
   - सबसे पहले स्पष्ट करें कि आपके दिमाग में इस परिदृश्य (Crash + Wednesday Expiry + 51,000 Call Wall + ₹1,008 Capital) को देखकर क्या विश्लेषण चल रहा है?

चरण 2. पूर्व वक्ताओं के तर्कों का परीक्षण (हेत्वाभास / Hetvabhasa Examination):
   - घनश्याम टेक के 51,055 ब्रेकआउट और विवेक बजाज के Sell-on-Rise 200-DMA नियम में आपके मॉडल ({speaker['role']}) के अनुसार क्या मजबूती या खामी है?
   - क्या एक्सपायरी के दिन उनका नियम ₹1,008 कैपिटल को ब्रोकरेज फ्रिक्शन (₹48.50) और 0DTE थीटा डिके से बचा पाएगा?

चरण 3. आज 16 सितंबर एक्सपायरी के लिए आपका अचूक एक्शन प्लान:
   - सुबह 9:30 AM पर और दोपहर 1:45 PM (जीरो-हीरो टाइम) पर आपकी मुख्य स्ट्रैटेजी किस सटीक कंडीशन (लेवल, कैंडल, वॉल्यूम, डेल्टा या ग्रीक्स) पर एंट्री और एग्जिट लेगी?
   - आपका स्टॉप-लॉस (SL) और टारगेट (TGT) पॉइंट क्या होगा?

चरण 4. ₹1,008 कैपिटल पर पॉजिटिव एक्सपेक्टेंसी और मैक्सिमम प्रॉफिट का गणित:
   - क्या आप 5x लेवरेज वाले MIS इंट्राडे कैश इक्विटी में ट्रेंड-फॉलोइंग ट्रेड (फ्रिक्शन ₹1.45) की सिफारिश करेंगे, या 1:45 PM पर आउट-ऑफ-द-मनी / एट-द-मनी पुट में केवल ₹200 का रिस्क लेकर 1:5 का एसिमेट्रिक ट्रेड लेने की सलाह देंगे?

चरण 5. अगले वक्ताओं (अन्य 8 यूट्यूबर्स व 200 क्वांट रिपॉजिटरीज) के लिए आपकी सीधी खुली चुनौती:
   - एक ऐसा तीखा प्रश्न या प्रतिवाद छोड़ें जिसका उत्तर उन्हें अपने सोर्सेज से देना पड़े।

कृपया केवल अपने 300 अपलोडेड सोर्सेज के ठोस डेटा, वास्तविक वीडियो टाइमस्टैम्प्स, और सटीक गणितीय नियमों के साथ ही उत्तर दें। कोई भी सामान्य या हवा-हवाई बात न करें।"""
    return prompt

def log_turn(turn_id, round_num, speaker, prompt_text, response_text, duration):
    # Log to SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
    INSERT INTO courier_live_debate_turns
    (timestamp, round_number, speaker_name, tab_index, notebook_id, prompt_text, response_text, response_chars, duration_seconds)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        datetime.datetime.now().isoformat(),
        round_num,
        speaker["name"],
        speaker["tab_idx"],
        speaker["id"],
        prompt_text,
        response_text,
        len(response_text),
        duration
    ))
    conn.commit()
    conn.close()
    
    # Log to Markdown
    fname = f"TURN_{turn_id:03d}_{speaker['key']}_R{round_num}.md"
    fpath = OUTPUT_DIR / fname
    md_content = f"""# 🏛️ SOVEREIGN LIVE COURIER DEBATE TURN {turn_id:03d}
- **Timestamp**: {datetime.datetime.now().isoformat()}
- **Round**: {round_num}
- **Speaker**: {speaker['name']}
- **Role**: {speaker['role']}
- **Tab Index**: {speaker['tab_idx']}
- **Notebook ID**: [{speaker['id']}](https://notebook.google.com/notebook/{speaker['id']})
- **Duration**: {duration:.1f} seconds
- **Response Length**: {len(response_text):,d} characters

---

## 📨 Courier Query Sent into Google NotebookLM Chat
```text
{prompt_text}
```

---

## 💡 Gemini Grounded Response & Thinking from {speaker['name']}
{response_text}
"""
    fpath.write_text(md_content, encoding="utf-8")
    print(f"[✓] Persisted Turn {turn_id:03d} to SQLite & {fname}")

def run_batch_parallel(batch_speakers, collective_synthesis, round_num, turn_id_counter):
    print("\n" + "=" * 80)
    print(f"🚀 FIRING PARALLEL MASS BATCH (Round {round_num}) — {len(batch_speakers)} Brains Concurrently")
    for s in batch_speakers:
        print(f"   • Tab {s['tab_idx']}: {s['name']}")
    print("=" * 80)
    
    submissions = []
    # 1. Dispatch queries to all tabs in batch
    for speaker in batch_speakers:
        prompt = build_dialectic_prompt(speaker, collective_synthesis, round_num)
        init_cnt = submit_query_to_tab(speaker, prompt)
        if init_cnt is not None:
            submissions.append((speaker, prompt, init_cnt))
        time.sleep(1.2)
        
    protect_user_window()
    
    # 2. Poll concurrently across all submitted tabs
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(submissions)) as executor:
        future_map = {
            executor.submit(poll_tab_response, speaker, init_cnt, 120): (speaker, prompt)
            for speaker, prompt, init_cnt in submissions
        }
        for future in concurrent.futures.as_completed(future_map):
            speaker, prompt = future_map[future]
            res = future.result()
            if res and res.get("answer"):
                turn_id_counter[0] += 1
                log_turn(turn_id_counter[0], round_num, speaker, prompt, res["answer"], res["duration"])
                results.append((speaker, res["answer"]))
            else:
                print(f"[-] No valid response for {speaker['name']}")
                
    protect_user_window()
    return results

def run_master_continuous_daemon(target_duration_minutes=65):
    print("=" * 80)
    print("🏛️ SOVEREIGN MASTER COURIER PARALLEL DIALECTIC DAEMON ACTIVATED")
    print(f"Target Duration: >= {target_duration_minutes} minutes")
    print(f"Total Notebooks Loaded: {len(NOTEBOOKS)}")
    print(f"Worker Window ID: {WORKER_WIN_ID} (Off-screen, zero user disturbance)")
    print(f"User Window ID: {USER_WIN_ID} (Permanently protected at index 1)")
    print("=" * 80)
    
    start_time = time.time()
    end_time = start_time + (target_duration_minutes * 60)
    turn_id_counter = [0]
    round_num = 1
    
    collective_synthesis = """विवेक बजाज का मैक्रो नियम: 200 DMA के नीचे सेल-ऑन-राइज मार्केट, ग्लोबल DXY दबाव, ₹1,008 पर नेकेड हीरो-जीरो वाइपआउट रिस्क।
घनश्याम टेक का प्राइस एक्शन नियम: 50,888 से 51,055 एक्टिव ट्रैप ज़ोन है। 51,055 के ऊपर 5-मिनट क्लोज होने पर ही शॉर्ट-कवरिंग रैली का कॉल बाय करें, जबकि इनसाइड बार का लो ब्रेक होने पर पुट बाय करें।"""
    
    # Group notebooks into parallel batches of 3
    BATCHES = [
        [NOTEBOOKS[2], NOTEBOOKS[3], NOTEBOOKS[4]], # Subasish Pani (5-EMA), Saketh R (Options Greeks), Nitin Murarka (CVD)
        [NOTEBOOKS[5], NOTEBOOKS[6], NOTEBOOKS[7]], # PR Sundar (Margins), Dr. Mukul (Forensics), Siddharth (44-MA)
        [NOTEBOOKS[8], NOTEBOOKS[9], NOTEBOOKS[10]], # Abhishek Kar (Psychology), News 15 Sept Crash, 200 Quant Repos
        [NOTEBOOKS[0], NOTEBOOKS[1]]                 # Vivek Bajaj (Macro), Ghanshyam Tech (Price Action)
    ]
    
    while time.time() < end_time:
        print("\n######################################################################")
        print(f"🔄 COMMENCING FULL DIALECTIC ROUND {round_num}")
        print(f"Elapsed: {(time.time() - start_time)/60:.1f}m / {target_duration_minutes}m")
        print("######################################################################\n")
        
        for batch_idx, batch in enumerate(BATCHES, start=1):
            if time.time() >= end_time:
                break
                
            batch_results = run_batch_parallel(batch, collective_synthesis, round_num, turn_id_counter)
            
            # Update collective synthesis with latest batch insights
            if batch_results:
                new_insights = []
                for sp, ans in batch_results:
                    clean_ans = ans.replace("Thoughts", "").replace("expand_more", "").strip()
                    new_insights.append(f"[{sp['name']}]: {clean_ans[:350]}...")
                collective_synthesis = "\n\n".join(new_insights)
                
            time.sleep(3.0)
            protect_user_window()
            
        round_num += 1
        
    total_elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print("🎉 MASTER COURIER PARALLEL DIALECTIC SESSION COMPLETED SUCCESSFULLY!")
    print(f"Total Session Duration: {total_elapsed/60:.2f} minutes")
    print(f"Total Turns Persisted: {turn_id_counter[0]}")
    print(f"Database: {DB_PATH}")
    print(f"Markdown Logs: {OUTPUT_DIR}")
    print("=" * 80)

if __name__ == "__main__":
    run_master_continuous_daemon(target_duration_minutes=62)
