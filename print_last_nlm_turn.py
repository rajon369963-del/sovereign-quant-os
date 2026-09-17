import subprocess
import json

js = """
(() => {
    const turns = Array.from(document.querySelectorAll('.chat-turn, conversation-turn, .model-response-container, .response-text'));
    if (turns.length > 0) {
        return turns[turns.length - 1].innerText;
    }
    const allDivs = Array.from(document.querySelectorAll('div[data-message-author="model"], .to-user-message'));
    if (allDivs.length > 0) {
        return allDivs[allDivs.length - 1].innerText;
    }
    return 'NO_TURNS_FOUND';
})()
"""

cmd = ["osascript", "-e", f'tell application "Google Chrome" to execute active tab of front window javascript "{js.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout[:2000])
