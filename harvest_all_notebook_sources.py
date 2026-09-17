import json
import subprocess
from pathlib import Path

TARGET_NOTEBOOKS = [
    {
        "id": "dd85a383-7151-4f9d-bea0-c6424d4204bc",
        "name": "15th_sept_share_market"
    },
    {
        "id": "1d3cc23f-fa96-42ee-a93a-8cfb47bcc1f1",
        "name": "share_market_monthly_news_2"
    },
    {
        "id": "b3cb05f5-ebe4-449f-b7a1-28aa9a00eadf",
        "name": "share_market_monthly_news_1"
    },
    {
        "id": "eac2d0d6-3e7b-4747-aa75-a54ad02898bf",
        "name": "share_market_weekly_news_part_2"
    },
    {
        "id": "25f4fae0-55df-444b-8197-33ae7c4bd876",
        "name": "share_market_weekly_news_part_1"
    },
    {
        "id": "d90752b4-deaf-4e8f-8419-6c8947767647",
        "name": "15th_septem_after_closing_the_market_news"
    }
]

DATA_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/all_harvested_notebook_sources")
DATA_DIR.mkdir(parents=True, exist_ok=True)

manifest = {}
all_unique_sources = {}

for nb in TARGET_NOTEBOOKS:
    nb_id = nb["id"]
    nb_name = nb["name"]
    print(f"Fetching source list for {nb_name} ({nb_id})...")
    cmd = ["notebooklm", "-p", "lakhidas168", "source", "list", "-n", nb_id, "--json"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(res.stdout)
        sources = data.get("sources", [])
        print(f"  -> Found {len(sources)} sources in {nb_name}")
        
        # Save individual notebook source list
        out_file = DATA_DIR / f"{nb_name}_sources.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(sources, f, indent=2, ensure_ascii=False)
            
        manifest[nb_name] = {
            "id": nb_id,
            "count": len(sources),
            "file": str(out_file)
        }
        
        for s in sources:
            url = s.get("url")
            sid = s.get("id")
            title = s.get("title", "")
            key = url if url else f"{nb_id}_{sid}"
            if key not in all_unique_sources:
                all_unique_sources[key] = {
                    "url": url,
                    "title": title,
                    "type": s.get("type"),
                    "created_at": s.get("created_at"),
                    "notebooks": [{
                        "notebook_id": nb_id,
                        "notebook_name": nb_name,
                        "source_id": sid
                    }]
                }
            else:
                all_unique_sources[key]["notebooks"].append({
                    "notebook_id": nb_id,
                    "notebook_name": nb_name,
                    "source_id": sid
                })
    except Exception as e:
        print(f"Error fetching {nb_name}: {e}")

summary = {
    "total_notebooks": len(TARGET_NOTEBOOKS),
    "notebook_manifest": manifest,
    "total_unique_sources": len(all_unique_sources),
    "unique_sources": list(all_unique_sources.values())
}

with open(DATA_DIR / "unified_manifest.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print(f"\nCompleted! Total unique sources across all 6 notebooks: {len(all_unique_sources)}")
