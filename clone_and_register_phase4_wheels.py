import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
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

db_path = BASE_DIR / 'TRADING_CANONICAL_SHA256_VAULT.sqlite'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

successful = []
idx = 1

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

queue = list(selected)
while len(successful) < 100 and (queue or backup_pool):
    if queue:
        item = queue.pop(0)
    elif backup_pool:
        item = backup_pool.pop(0)
    else:
        break

    full_name = item['full_name']
    owner, repo = full_name.split('/')
    dest_name = f'PHASE4-QUANT-{idx:03d}_{owner}__{repo}'
    dest_path = TARGET_DIR / dest_name

    if dest_path.exists():
        f_count, sz_mb, h = compute_repo_stats(dest_path)
        successful.append({
            'repo_id': f'PHASE4-QUANT-{idx:03d}',
            'full_name': full_name,
            'dest_name': dest_name,
            'path': str(dest_path),
            'files': f_count,
            'size_mb': sz_mb,
            'sha256': h,
            'desc': item.get('desc', '')
        })
        print(f'[{idx:03d}/100] Already present: {dest_name} ({f_count} files, {sz_mb} MB)')
        idx += 1
        continue

    print(f'[{idx:03d}/100] Cloning: {full_name} ...')
    clone_url = f'https://github.com/{full_name}.git'
    try:
        res = subprocess.run(
            ['git', 'clone', '--depth', '1', clone_url, str(dest_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=90
        )
        if res.returncode == 0 and dest_path.exists():
            f_count, sz_mb, h = compute_repo_stats(dest_path)
            successful.append({
                'repo_id': f'PHASE4-QUANT-{idx:03d}',
                'full_name': full_name,
                'dest_name': dest_name,
                'path': str(dest_path),
                'files': f_count,
                'size_mb': sz_mb,
                'sha256': h,
                'desc': item.get('desc', '')
            })
            print(f'   -> Success: {f_count} files, {sz_mb} MB')
            idx += 1
        else:
            print(f'   -> Failed {full_name}: {res.stderr[:80]}... Skipping to next.')
            if dest_path.exists():
                shutil.rmtree(dest_path, ignore_errors=True)
    except Exception as e:
        print(f'   -> Timeout/Error {full_name}: {e}')
        if dest_path.exists():
            shutil.rmtree(dest_path, ignore_errors=True)

print(f'Finished cloning! Successfully acquired {len(successful)} repos.')

# Register in SQLite
for item in successful:
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
    json.dump(successful, f, indent=2)

print(f'Saved manifest to PHASE4_100_WHEELS_MANIFEST.json with {len(successful)} records and committed to DB.')
