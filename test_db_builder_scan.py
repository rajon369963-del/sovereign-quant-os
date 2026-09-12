import sqlite3
import json
from pathlib import Path

inv_path = Path("/Users/rajondas/AIR1_DATA/NOTEBOOKLM_LAKHIDAS168_EXPORT/01_INVENTORY/ACCOUNT_INVENTORY.sqlite")
manifest_path = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json")
fts_path = Path("/Users/rajondas/AIR1_ARCHIVES/LAKHIDAS168_NOTEBOOKLM_TRANSCRIPT_RECOVERY_20260902/06_DERIVED_SEARCH/fts5/transcript_fts.sqlite")

print(f"Inventory exists: {inv_path.exists()} ({inv_path.stat().st_size} bytes)")
print(f"Manifest exists: {manifest_path.exists()} ({manifest_path.stat().st_size} bytes)")
print(f"FTS exists: {fts_path.exists()} ({fts_path.stat().st_size} bytes)")

# Read manifest
with open(manifest_path) as f:
    manifest_data = json.load(f)
print(f"Manifest videos count: {len(manifest_data.get('videos', []))}")

# Check sources in inventory
conn = sqlite3.connect(inv_path)
c = conn.cursor()

c.execute("SELECT count(*) FROM sources")
print(f"Total sources in ACCOUNT_INVENTORY: {c.fetchone()[0]}")

c.execute("SELECT count(*) FROM video_assets")
print(f"Total video_assets in ACCOUNT_INVENTORY: {c.fetchone()[0]}")

conn.close()
