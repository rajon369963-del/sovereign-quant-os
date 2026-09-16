import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE_DIR = Path('/Users/rajondas/teamwork_projects/sovereign-quant-os')
TARGET_DIR = BASE_DIR / 'phase4_quant_wheels_100'
TARGET_DIR.mkdir(parents=True, exist_ok=True)

with open(BASE_DIR / 'existing_325_repos.json') as f:
    existing_325 = set(x.lower() for x in json.load(f))

candidates = []
seen = set()

# Combine all candidate files
for fname in ['phase4_selected_100_repos.json', 'discovered_github_repos.json', 'more_github_repos.json']:
    fpath = BASE_DIR / fname
    if fpath.exists():
        with open(fpath) as f:
            for item in json.load(f):
                full = item['full_name'].lower()
                name = full.split('/')[-1]
                if full not in seen and not any(name in ex for ex in existing_325):
                    seen.add(full)
                    candidates.append(item)

print(f'Total deduplicated candidate pool: {len(candidates)}')

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

# Collect what is already cloned and valid in TARGET_DIR
valid_cloned = {}
for p in TARGET_DIR.iterdir():
    if p.is_dir() and (p / '.git').exists():
        fc, sz, h = compute_repo_stats(p)
        if fc > 0:
            # extract repo name
            parts = p.name.split('_')
            repo_id = parts[0]
            valid_cloned[p.name] = {
                'dir_name': p.name,
                'path': str(p),
                'files': fc,
                'size_mb': sz,
                'sha256': h
            }

print(f'Already valid on disk: {len(valid_cloned)}')

needed = 100 - len(valid_cloned)
print(f'Need to acquire {needed} more repos to reach exactly 100.')

def clone_repo(cand):
    full_name = cand['full_name']
    owner, repo = full_name.split('/')
    temp_dest = TARGET_DIR / f'TEMP_{owner}__{repo}'
    clone_url = f'https://github.com/{full_name}.git'
    try:
        res = subprocess.run(
            ['git', 'clone', '--depth', '1', clone_url, str(temp_dest)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )
        if res.returncode == 0 and temp_dest.exists():
            fc, sz, h = compute_repo_stats(temp_dest)
            if fc > 0:
                return cand, temp_dest, fc, sz, h
        if temp_dest.exists():
            shutil.rmtree(temp_dest, ignore_errors=True)
        return None
    except Exception:
        if temp_dest.exists():
            shutil.rmtree(temp_dest, ignore_errors=True)
        return None

# Filter out what's already on disk
existing_disk_names = set(k.lower() for k in valid_cloned)
filtered_cands = []
for c in candidates:
    owner, repo = c['full_name'].split('/')
    slug = f'{owner}__{repo}'.lower()
    if not any(slug in ed for ed in existing_disk_names):
        filtered_cands.append(c)

newly_acquired = []
if needed > 0:
    with ThreadPoolExecutor(max_workers=10) as ex:
        futures = {ex.submit(clone_repo, c): c for c in filtered_cands}
        for fut in as_completed(futures):
            res = fut.result()
            if res:
                cand, temp_dest, fc, sz, h = res
                newly_acquired.append((cand, temp_dest, fc, sz, h))
                print(f'Acquired [{len(valid_cloned) + len(newly_acquired)}/100]: {cand["full_name"]} ({fc} files, {sz} MB)')
                if len(valid_cloned) + len(newly_acquired) >= 100:
                    break

print('Cloning phase finished!')

# Now rename all items cleanly to PHASE4-QUANT-001 through PHASE4-QUANT-100
all_repos_final = []

# Gather existing valid items
items_to_process = []
for dname, data in valid_cloned.items():
    # extract original owner and repo
    sub = dname
    if dname.startswith('PHASE4-QUANT-'):
        sub = dname[17:] # strip PHASE4-QUANT-XXX_
    items_to_process.append({
        'old_path': Path(data['path']),
        'slug': sub,
        'files': data['files'],
        'size_mb': data['size_mb'],
        'sha256': data['sha256']
    })

# Add newly acquired
for cand, temp_dest, fc, sz, h in newly_acquired:
    owner, repo = cand['full_name'].split('/')
    items_to_process.append({
        'old_path': temp_dest,
        'slug': f'{owner}__{repo}',
        'files': fc,
        'size_mb': sz,
        'sha256': h
    })

items_to_process = items_to_process[:100]

manifest_data = []
for idx, item in enumerate(items_to_process, 1):
    cid = f'PHASE4-QUANT-{idx:03d}'
    target_dir_name = f'{cid}_{item["slug"]}'
    final_path = TARGET_DIR / target_dir_name
    if item['old_path'] != final_path:
        if final_path.exists():
            shutil.rmtree(final_path, ignore_errors=True)
        item['old_path'].rename(final_path)
    
    # recompute stats on final path
    fc, sz, h = compute_repo_stats(final_path)
    rec = {
        'repo_id': cid,
        'repo_name': target_dir_name,
        'physical_path': str(final_path),
        'file_count': fc,
        'total_size_mb': sz,
        'sha256': h,
        'source_location': 'phase4_quant_wheels_100',
        'git_status': 'GIT_CLONED'
    }
    manifest_data.append(rec)
    print(f'Registered: {cid} -> {target_dir_name} ({fc} files, {sz} MB)')

# Commit to DB
db_path = BASE_DIR / 'TRADING_CANONICAL_SHA256_VAULT.sqlite'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Clean old phase4 registrations if needed
cur.execute("DELETE FROM repos_registry WHERE source_location = 'phase4_quant_wheels_100'")

for m in manifest_data:
    cur.execute('''
        INSERT INTO repos_registry
        (repo_id, repo_name, physical_path, file_count, total_size_mb, source_location, git_status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (m['repo_id'], m['repo_name'], m['physical_path'], m['file_count'], m['total_size_mb'], m['source_location'], m['git_status']))

conn.commit()
conn.close()

with open(BASE_DIR / 'PHASE4_100_WHEELS_MANIFEST.json', 'w') as f:
    json.dump(manifest_data, f, indent=2)

print(f'SUCCESS: Exactly {len(manifest_data)} wheels verified and written to PHASE4_100_WHEELS_MANIFEST.json and committed to DB.')
