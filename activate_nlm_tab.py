import subprocess

script = '''
tell application "Google Chrome"
    repeat with w in windows
        set tabIdx to 1
        repeat with t in tabs of w
            if URL of t contains "notebook.google.com/notebook/96da7dbf-18e9-40a0-9e90-e363052a247f" then
                set active tab index of w to tabIdx
                set index of w to 1
                return "ACTIVATED_TAB_" & tabIdx
            end if
            set tabIdx to tabIdx + 1
        end repeat
    end repeat
    return "TAB_NOT_FOUND"
end tell
'''
res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
print("Tab Activation:", res.stdout.strip(), res.stderr.strip())
