import subprocess

js = """
(() => {
    const pinBtns = Array.from(document.querySelectorAll('button[aria-label="Save message to a note"], button[aria-label="Pin message to note"]'));
    if (pinBtns.length > 0) {
        const lastBtn = pinBtns[pinBtns.length - 1];
        lastBtn.click();
        return 'PINNED_TO_NOTE';
    }
    return 'PIN_BTN_NOT_FOUND';
})()
"""

cmd = ["osascript", "-e", f'tell application "Google Chrome" to execute active tab of front window javascript "{js.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Result:", res.stdout.strip())
