import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE_DIR = Path('/Users/rajondas/teamwork_projects/sovereign-quant-os')
TARGET_DIR = BASE_DIR / 'phase4_quant_wheels_100'
TARGET_DIR.mkdir(parents=True, exist_ok=True)

with open(BASE_DIR / 'phase4_selected_100_repos.json') as f:
    selected = json.load(f)

with open(BASE_DIR / 'discovered_github_repos.json') as f:
    all_discovered = json.load(f)

existing_names = set(s['full_name'].lower() for s in selected)
backup_pool = [d for d in all_discovered if d['full_name'].lower() not in existing_names]

all_candidates = list(selected) + backup_pool

db_path = BASE_DIR / 'TRADING_CANONICAL_SHA256_VAULT.sqlite'

lock = threading.Lock()
successful = []
target_count = 100

def compute_repo_stats(path):
    f_count = 0
    total_bytes = 0
    hasher = hashlib.sha256()
    for root, dirs, files in os.walk(path):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in files:
            fp = os.path.join(root, f)
            try:
                sz = os.path.getsize(fp)
                total_bytes += sz
                f_count += 1
                hasher.update(f.encode('utf-8'))
                hasher.update(str(sz).encode('utf-8'))
            except Exception:
                pass
    return f_count, round(total_bytes / (1024 * 1024), 2), hasher.hexdigest()

def clone_one(item, assigned_id):
    full_name = item['full_name']
    owner, repo = full_name.split('/')
    dest_name = f'{assigned_id}_{owner}__{repo}'
    dest_path = TARGET_DIR / dest_name

    if dest_path.exists() and (dest_path / '.git').exists():
        f_count, sz_mb, h = compute_repo_stats(dest_path)
        if f_count > 0:
            print(f'[{assigned_id}] Already present: {dest_name} ({f_count} files, {sz_mb} MB)')
            return {
                'repo_id': assigned_id,
                'full_name': full_name,
                'dest_name': dest_name,
                'path': str(dest_path),
                'files': f_count,
                'size_mb': sz_mb,
                'sha256': h,
                'desc': item.get('desc', '')
            }

    print(f'[{assigned_id}] Cloning {full_name}...')
    clone_url = f'https://github.com/{full_name}.git'
    try:
        res = subprocess.run(
            ['git', 'clone', '--depth', '1', clone_url, str(dest_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=25
        )
        if res.returncode == 0 and dest_path.exists():
            f_count, sz_mb, h = compute_repo_stats(dest_path)
            print(f'[{assigned_id}] Done: {full_name} ({f_count} files, {sz_mb} MB)')
            return {
                'repo_id': assigned_id,
                'full_name': full_name,
                'dest_name': dest_name,
                'path': str(dest_path),
                'files': f_count,
                'size_mb': sz_mb,
                'sha256': h,
                'desc': item.get('desc', '')
            }
        else:
            if dest_path.exists():
                shutil.rmtree(dest_path, ignore_errors=True)
            return None
    except Exception:
        if dest_path.exists():
            shutil.rmtree(dest_path, ignore_errors=True)
        return None

# Check already existing in TARGET_DIR
existing_dirs = [d for d in TARGET_DIR.iterdir() if d.is_dir() and d.name.startswith('PHASE4-QUANT-')]
assigned_count = len(existing_dirs)

print(f'Starting parallel clone pool. Target: {target_count} repos. Already present on disk: {assigned_count}')

cand_iter = iter(all_candidates)
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {}
    while assigned_count < target_count:
        try:
            cand = next(cand_iter)
        except StopIteration:
            break
        assigned_count += 1
        aid = f'PHASE4-QUANT-{assigned_count:03d}'
        futures[executor.submit(clone_one, cand, aid)] = (cand, aid)

    for future in as_completed(futures):
        res = future.result()
        if res:
            successful.append(res)
            print(f'Progress: {len(successful)}/{target_count} acquired.')
        else:
            # Need a replacement
            try:
                cand = next(cand_iter)
                # reuse or increment
                assigned_count += 1
                aid = f'PHASE4-QUANT-{len(successful) + len(futures) + 1:03d}'
                # cap aid
                futures[executor.submit(clone_one, cand, aid)] = (cand, aid)
            except StopIteration:
                pass
        if len(successful) >= target_count:
            break

print(f'Parallel clone complete! Total acquired: {len(successful)}')

# Normalize IDs to 1..100
final_records = []
for idx, item in enumerate(successful[:100], 1):
    canonical_id = f'PHASE4-QUANT-{idx:03d}'
    item['repo_id'] = canonical_id
    final_records.append(item)

# Register into SQLite
conn = sqlite3.connect(db_path)
cur = conn.cursor()
for item in final_records:
    cur.execute('''
        INSERT OR REPLACE INTO repos_registry
        (repo_id, repo_name, physical_path, file_count, total_size_mb, source_location, git_status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        item['repo_id'],
        item['dest_name'],
        item['path'],
        item['files'],
        item['size_mb'],
        'phase4_quant_wheels_100',
        'GIT_CLONED'
    ))

conn.commit()
conn.close()

with open(BASE_DIR / 'PHASE4_100_WHEELS_MANIFEST.json', 'w') as f:
    json.dump(final_records, f, indent=2)

print(f'SUCCESS! Verified exactly {len(final_records)} wheels in PHASE4_100_WHEELS_MANIFEST.json and SQLite DB.')
