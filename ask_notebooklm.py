#!/usr/bin/env python3
import json
import subprocess
import time

PROMPT = """Analyze all 300 sources in this notebook for today (15th September 2026) to construct a comprehensive 10,000 Diamonds Quant Hypergraph:

1. COMPLETE STOCK & SECTOR HARVEST:
Extract EVERY Indian stock mentioned across the sources with:
- Ticker / Company Name
- Sector
- Recommendation (BUY / SELL / ACCUMULATE / AVOID)
- Target Price, Stop Loss, Breakout Pivot Level
- Core Catalyst (CNG/EV crossover, interest rates, SEBI/RBI regulations, crude price moves, Ganesh Chaturthi sentiment)

2. HYPERGRAPH NODES & EDGES:
Define:
- Macro & Sector Nodes
- Stock Nodes
- Directed Edges (BULLISH_CATALYST, MARGIN_EXPANSION, SUPPLY_CHAIN_CONTAGION, REGULATORY_TAILWIND)
Identify the top 5 highest-conviction asymmetrical trade setups for today.

3. PYTHON CODE & STRUCTURED JSON:
Generate a complete, valid Python dictionary HYPERGRAPH_DATA with all nodes, edges, and stock metrics so we can save it to our local SQLite database. Execute Python code if needed to compute the rankings."""

def send_query_and_wait():
    escaped_prompt = json.dumps(PROMPT)
    
    # Clean script for submitting
    js_submit = """
    (function() {
        let q = document.querySelector('.query-box-input, textarea[aria-label="Query box"]');
        if (!q) return JSON.stringify({status: 'error', message: 'No query box found'});
        
        q.value = PROMPT_PLACEHOLDER;
        q.dispatchEvent(new Event('input', { bubbles: true }));
        q.dispatchEvent(new Event('change', { bubbles: true }));
        
        let submitBtn = document.querySelector('button[aria-label="Submit"], button.submit-button');
        if (!submitBtn) return JSON.stringify({status: 'error', message: 'No submit button found'});
        
        if (submitBtn.disabled) {
            submitBtn.removeAttribute('disabled');
            submitBtn.classList.remove('mat-mdc-button-disabled');
        }
        
        submitBtn.click();
        return JSON.stringify({status: 'submitted', timestamp: Date.now()});
    })()
    """.replace("PROMPT_PLACEHOLDER", escaped_prompt)
    
    # Save JS to temp file to avoid escaping issues with AppleScript
    js_file = "/tmp/nlm_submit.js"
    with open(js_file, "w") as f:
        f.write(js_submit)
        
    applescript_submit = f"""
    set jsCode to do shell script "cat {js_file}"
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "dd85a383-7151-4f9d-bea0-c6424d4204bc" then
                    return execute t javascript jsCode
                end if
            end repeat
        end repeat
    end tell
    """
    
    print("Submitting prompt to NotebookLM in Chrome...")
    res = subprocess.run(["osascript", "-e", applescript_submit], capture_output=True, text=True)
    print("Submit result:", res.stdout.strip())
    
    # Step 2: Poll for completion
    js_check = """
    (function() {
        let isThinking = document.querySelector('.thinking, mat-progress-spinner, .loading, .streaming');
        let stopBtn = document.querySelector('button[aria-label="Stop generation"], button[aria-label="Stop"]');
        let messages = Array.from(document.querySelectorAll('.chat-message, .message, .chat-turn, .response, [data-message-author="bot"], .model-response, .to-user'));
        let lastMsg = messages.length > 0 ? messages[messages.length - 1].innerText : "";
        
        let chatArea = document.querySelector('.chat-container, .conversation-container, .chat-history, [role="main"]');
        let chatText = chatArea ? chatArea.innerText : "";
        
        return JSON.stringify({
            isGenerating: !!isThinking || !!stopBtn,
            messagesCount: messages.length,
            lastMessageSnippet: lastMsg.slice(-300),
            lastMessageFull: lastMsg,
            chatTextLength: chatText.length,
            fullChat: chatText
        });
    })()
    """
    check_file = "/tmp/nlm_check.js"
    with open(check_file, "w") as f:
        f.write(js_check)
        
    applescript_check = f"""
    set jsCode to do shell script "cat {check_file}"
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "dd85a383-7151-4f9d-bea0-c6424d4204bc" then
                    return execute t javascript jsCode
                end if
            end repeat
        end repeat
    end tell
    """
    
    print("Polling NotebookLM for response generation...")
    last_len = 0
    stable_cycles = 0
    
    for i in range(45): # Poll up to 90 seconds
        time.sleep(2)
        r = subprocess.run(["osascript", "-e", applescript_check], capture_output=True, text=True)
        try:
            data = json.loads(r.stdout.strip())
            is_gen = data.get("isGenerating", False)
            curr_text = data.get("lastMessageFull", "")
            if not curr_text:
                curr_text = data.get("fullChat", "")
            
            cur_len = len(curr_text)
            print(f"[{i+1}/45] Generating: {is_gen} | Msg len: {cur_len}")
            
            if cur_len > 300:
                if cur_len == last_len and not is_gen:
                    stable_cycles += 1
                    if stable_cycles >= 3:
                        print("✓ Generation complete and output stable!")
                        return curr_text
                else:
                    stable_cycles = 0
                    last_len = cur_len
        except Exception as e:
            print(f"Polling error: {e}")
            
    return curr_text

if __name__ == "__main__":
    resp = send_query_and_wait()
    if resp:
        out_file = "/Users/rajondas/teamwork_projects/sovereign-quant-os/notebooklm_hypergraph_response.txt"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(resp)
        print(f"Saved response to {out_file} ({len(resp)} bytes)")
    else:
        print("No response captured.")
