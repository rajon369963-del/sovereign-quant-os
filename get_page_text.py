import subprocess

script = '''
tell application "Google Chrome"
    tell active tab of front window
        execute javascript "document.body.innerText"
    end tell
end tell
'''
p = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
text = p.stdout
print("Total length:", len(text))
# Find where the questions or responses are
lines = text.split('\n')
for i, line in enumerate(lines):
    if any(k in line.lower() for k in ["deep quantitative", "pnb", "kelly", "variance shield", "pratijna"]):
        print(f"L{i}: {line[:120]}")
