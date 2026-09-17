import json
import subprocess

cmd = ["notebooklm", "-p", "lakhidas168", "list", "--json"]
out = subprocess.check_output(cmd, text=True)
data = json.loads(out)

if isinstance(data, dict):
    items = data.get("notebooks", [])
elif isinstance(data, list):
    items = data
else:
    items = []

targets = [
    "15th sept share market",
    "SHARE MARKET MONTHLY NEWS 2",
    "SHARE MARKET MONTHLY NEWS 1",
    "SHARE MARKET WEEKLY NEWS PART 2",
    "SHARE MARKET WEEKLY NEWS PART1",
    "15th septem after closing the market news"
]

results = []
for nb in items:
    title = nb.get("title", "")
    for t in targets:
        if t.lower() in title.lower():
            results.append({
                "id": nb.get("id"),
                "title": title,
                "sources": nb.get("source_count"),
                "matched_target": t
            })
            break

print("MATCHED TARGETS COUNT:", len(results))
for r in results:
    print(r["id"], "|", r["title"], "| sources:", r["sources"])

with open("/Users/rajondas/teamwork_projects/sovereign-quant-os/target_notebooks.json", "w") as f:
    json.dump(results, f, indent=2)
