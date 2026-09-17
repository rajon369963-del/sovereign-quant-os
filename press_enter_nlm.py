import subprocess

js = """
(() => {
    const ta = document.querySelector('textarea.query-box-input');
    if (!ta) return 'NO_TA';
    ta.focus();
    
    // Simulate Enter key press
    const event = new KeyboardEvent('keydown', {
        bubbles: true,
        cancelable: true,
        key: 'Enter',
        code: 'Enter',
        keyCode: 13,
        which: 13
    });
    ta.dispatchEvent(event);
    
    // Also try clicking the submit button if active
    const btn = document.querySelector('button[aria-label="Submit"]');
    if (btn) {
        btn.click();
        return 'BTN_CLICKED';
    }
    return 'KEY_DISPATCHED';
})()
"""

cmd = ["osascript", "-e", f'tell application "Google Chrome" to execute active tab of front window javascript "{js.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"']
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
