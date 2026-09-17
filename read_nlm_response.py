import subprocess
import json

js = """
(() => {
    // Get all text content from the chat section
    const mainContainer = document.querySelector('conversation-turn-list, .chat-viewport, .infinite-scroll-component, mat-sidenav-content');
    const turns = Array.from(document.querySelectorAll('.chat-turn, conversation-turn, .message-content, .model-response-container'));
    
    return JSON.stringify({
        turns_count: turns.length,
        texts: turns.map(t => t.innerText)
    });
})()
"""

cmd = ["osascript", "-e", f'tell application "Google Chrome" to execute active tab of front window javascript "{js.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
