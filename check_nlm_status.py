import subprocess
import json

js = """
(() => {
    const textareas = document.querySelector('textarea.query-box-input');
    const nodes = Array.from(document.querySelectorAll('.to-user-message, .from-user-message, .chat-turn, .model-response-container'));
    return JSON.stringify({
        ta_val: textareas ? textareas.value : '',
        msg_count: nodes.length,
        last_nodes: nodes.slice(-3).map(n => ({ cls: n.className, text: n.innerText.slice(0, 500) }))
    });
})()
"""

cmd = ["osascript", "-e", f'tell application "Google Chrome" to execute active tab of front window javascript "{js.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
