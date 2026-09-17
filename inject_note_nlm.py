import subprocess
import json

with open("/Users/rajondas/teamwork_projects/sovereign-quant-os/LIVE_INGESTION_FEED_PULSE_17SEP.txt", "r") as f:
    digest_text = f.read()

title = "LIVE_INGESTION_17_SEP_2026_YOUTUBE_AND_MACRO_PULSE"
escaped_title = json.dumps(title)
escaped_content = json.dumps(digest_text)

js = f"""
(() => {{
    const titleInput = document.querySelector('input.note-header__editable-title');
    if (titleInput) {{
        titleInput.value = {escaped_title};
        titleInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
        titleInput.dispatchEvent(new Event('change', {{ bubbles: true }}));
    }}
    
    const editor = document.querySelector('div.ProseMirror');
    if (editor) {{
        editor.focus();
        editor.innerText = {escaped_content};
        editor.dispatchEvent(new Event('input', {{ bubbles: true }}));
    }}
    return 'NOTE_POPULATED';
}})()
"""

cmd = ["osascript", "-e", f'tell application "Google Chrome" to execute active tab of front window javascript "{js.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Result:", res.stdout.strip())
