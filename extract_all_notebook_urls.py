#!/usr/bin/env python3
import subprocess


def run_js(js_code: str):
    # Escape quotes and backslashes
    clean_js = js_code.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ')
    as_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "notebook.google.com" then
                    tell t
                        return execute javascript "{clean_js}"
                    end tell
                end if
            end repeat
        end repeat
        return "NO_TAB"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', as_script], capture_output=True, text=True)
    return res.stdout.strip()

# 1. Click on "All" or list all notebook rows
js_find = """
(function() {
    let allLinks = Array.from(document.querySelectorAll('a'));
    let notebooks = [];
    for (let a of allLinks) {
        let href = a.getAttribute('href') || '';
        let text = a.innerText.trim();
        if (href.includes('/notebook/') || text.includes('Sources') || text.includes('SHARE MARKET') || text.includes('15th sept')) {
            notebooks.push({text: text, href: href});
        }
    }
    return JSON.stringify({
        title: document.title,
        url: window.location.href,
        linksCount: allLinks.length,
        notebooks: notebooks
    });
})()
"""

print("Querying Chrome...")
out = run_js(js_find)
print("Output:", out)
