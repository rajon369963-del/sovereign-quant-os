import json
import subprocess

js_code = """(() => {
    let sources = Array.from(document.querySelectorAll(".source-title")).map(el => el.innerText.trim());
    let count = sources.length;
    let tabs = Array.from(document.querySelectorAll(".mdc-tab")).map(t => ({
        text: t.innerText.trim(),
        active: t.classList.contains("mdc-tab--active")
    }));
    return JSON.stringify({count: count, sources: sources, tabs: tabs, url: window.location.href});
})()"""

ascript = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "96da7dbf-18e9-40a0-9e90-e363052a247f" then
                tell t
                    return execute javascript {json.dumps(js_code)}
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''

res = subprocess.run(["osascript", "-e", ascript], capture_output=True, text=True)
print("STDOUT:", res.stdout.strip())
if res.stderr.strip():
    print("STDERR:", res.stderr.strip())
