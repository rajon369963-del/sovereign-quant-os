import os
import subprocess

# Create a 2.5MB test payload
test_str = "A" * (2500 * 1024)
temp_txt = "/tmp/test_large_payload.txt"
with open(temp_txt, "w", encoding="utf-8") as f:
    f.write(test_str)

# AppleScript reading file directly
ascript = f'''
set filePath to POSIX file "{temp_txt}"
set fileContent to (read filePath as «class utf8»)
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "96da7dbf-18e9-40a0-9e90-e363052a247f" then
                tell t
                    set jsCode to "(() => {{ return window.testPayloadLen = " & (length of fileContent) & "; }})()"
                    return execute javascript jsCode
                end tell
            end if
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''

temp_scpt = "/tmp/test_large.applescript"
with open(temp_scpt, "w", encoding="utf-8") as f:
    f.write(ascript)

res = subprocess.run(["osascript", temp_scpt], capture_output=True, text=True)
print("AppleScript result:", res.stdout.strip())
if res.stderr.strip():
    print("AppleScript stderr:", res.stderr.strip())

if os.path.exists(temp_txt):
    os.remove(temp_txt)
if os.path.exists(temp_scpt):
    os.remove(temp_scpt)
