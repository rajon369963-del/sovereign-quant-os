#!/usr/bin/env python3
"""
===============================================================================
AIR10/MIGL GOOGLE DRIVE TRADING VIDEO RECOVERY & MANIFEST SYNC
===============================================================================
Extracts trading-video metadata from transcript_fts.sqlite and synchronizes
canonical manifests to the configured Google Drive folder.

Important evidence boundary: successful external commands are not promoted to
remote byte-parity verification unless an independent remote digest readback is
performed. This module records executable/argv/local-artifact evidence and fails
closed on command failure.
===============================================================================
"""

import hashlib
import json
import os
import shutil
import sqlite3
import stat
import subprocess
from datetime import datetime, timezone
from pathlib import Path

FTS_DB = "/Users/rajondas/AIR1_ARCHIVES/LAKHIDAS168_NOTEBOOKLM_TRANSCRIPT_RECOVERY_20260902/06_DERIVED_SEARCH/fts5/transcript_fts.sqlite"
OUT_DIR = "/Users/rajondas/.gemini/antigravity/scratch/antigravity_yolo_trading_engine"
DRIVE_PARENT_ID = "1i2ci3yvGJcYM6V6kBRZqYxvIDvgCKBCZ"
ACCOUNT = "lakhidas168@gmail.com"


class SyncAuthorityError(RuntimeError):
    """Raised when the external sync command cannot be trusted to continue."""


def _sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sha256_fd(fd):
    digest = hashlib.sha256()
    os.lseek(fd, 0, os.SEEK_SET)
    for chunk in iter(lambda: os.read(fd, 1024 * 1024), b""):
        digest.update(chunk)
    os.lseek(fd, 0, os.SEEK_SET)
    return digest.hexdigest()


def _argv_digest(argv):
    canonical = json.dumps(argv, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _open_gog_identity(executable_resolver=shutil.which):
    resolved = executable_resolver("gog")
    if not resolved:
        raise SyncAuthorityError("gog executable not found on PATH")
    real_path = str(Path(resolved).resolve())
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(real_path, flags)
    except OSError as exc:
        raise SyncAuthorityError(f"cannot securely open gog executable: {exc}") from exc
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise SyncAuthorityError(f"resolved gog is not a regular file: {real_path}")
        if not os.access(real_path, os.X_OK):
            raise SyncAuthorityError(f"resolved gog is not executable: {real_path}")
        if os.execve not in getattr(os, "supports_fd", set()):
            raise SyncAuthorityError("HOLD_UNSUPPORTED_EXACT_OBJECT_EXECUTION")
        return fd, {
            "command_path": real_path,
            "command_sha256": _sha256_fd(fd),
            "opened_dev": info.st_dev,
            "opened_ino": info.st_ino,
            "execution_binding": "OPEN_HASH_EXEC_SAME_FD",
        }
    except Exception:
        os.close(fd)
        raise


def _exec_fd_capture(fd, argv):
    """Execute the already-open object; never fall back to the pathname."""
    stdout_r, stdout_w = os.pipe()
    stderr_r, stderr_w = os.pipe()
    pid = os.fork()
    if pid == 0:
        try:
            os.close(stdout_r)
            os.close(stderr_r)
            os.dup2(stdout_w, 1)
            os.dup2(stderr_w, 2)
            os.close(stdout_w)
            os.close(stderr_w)
            os.execve(fd, argv, os.environ.copy())
        except BaseException as exc:
            os.write(2, (f"exact-fd exec failed: {exc}\n").encode())
            os._exit(126)
    os.close(stdout_w)
    os.close(stderr_w)
    stdout = os.read(stdout_r, 1024 * 1024)
    stderr = os.read(stderr_r, 1024 * 1024)
    os.close(stdout_r)
    os.close(stderr_r)
    _, status = os.waitpid(pid, 0)
    return subprocess.CompletedProcess(
        argv,
        os.waitstatus_to_exitcode(status),
        stdout.decode("utf-8", errors="replace"),
        stderr.decode("utf-8", errors="replace"),
    )


def _run_gog(args, label, executor=_exec_fd_capture, executable_resolver=shutil.which):
    fd, identity = _open_gog_identity(executable_resolver)
    command = [identity["command_path"], *args]
    try:
        result = executor(fd, command)
    finally:
        os.close(fd)
    evidence = {
        **identity,
        "label": label,
        "argv_sha256": _argv_digest(command),
        "return_code": result.returncode,
        "stderr_present": bool((result.stderr or "").strip()),
    }
    if result.returncode != 0:
        raise SyncAuthorityError(
            f"{label} failed with return code {result.returncode}; "
            f"stderr={((result.stderr or '').strip())[:500]}"
        )
    return result, evidence


def extract_manifest():
    print(f"[1/4] Connecting to {FTS_DB}...")
    conn = sqlite3.connect(FTS_DB)
    conn.execute("PRAGMA query_only = ON")
    cur = conn.cursor()

    query = """
    SELECT
        sha256,
        canonical_video_id,
        notebook_title,
        source_title,
        source_url,
        length(content) as char_count
    FROM transcript_fts
    WHERE notebook_title IN ('HFT 1', 'HFT 2', 'QUANT', 'openclaw_1', 'openclaw_2')
       OR notebook_title LIKE '%trading%'
       OR notebook_title LIKE '%scalp%'
       OR notebook_title LIKE '%ml prediction%'
    ORDER BY notebook_title, source_title;
    """

    cur.execute(query)
    rows = cur.fetchall()
    print(f"[2/4] Retrieved {len(rows)} trading video transcript records.")

    manifest_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_sources": len(rows),
        "target_drive_folder": DRIVE_PARENT_ID,
        "target_account": ACCOUNT,
        "notebook_breakdown": {},
        "videos": [],
    }

    markdown_lines = [
        "# ⚡ SOVEREIGN TRADING VIDEO CANONICAL ARCHIVE MANIFEST",
        f"**Generated**: {manifest_data['generated_at']} | **Total Videos**: {len(rows)} | **Drive Target**: `{DRIVE_PARENT_ID}`",
        "",
        "## Notebook Breakdown",
        "",
    ]

    for row in rows:
        sha, vid, notebook, title, url, chars = row
        manifest_data["notebook_breakdown"][notebook] = manifest_data["notebook_breakdown"].get(notebook, 0) + 1
        manifest_data["videos"].append(
            {
                "sha256": sha,
                "video_id": vid,
                "notebook": notebook,
                "title": title,
                "url": url,
                "char_count": chars,
            }
        )

    for nb, count in sorted(manifest_data["notebook_breakdown"].items()):
        markdown_lines.append(f"- **{nb}**: {count} videos")

    markdown_lines.extend(
        [
            "",
            "## Video Catalog (First 100 Sample)",
            "| Video ID | Notebook | Title | Characters | SHA256 |",
            "|---|---|---|---|---|",
        ]
    )

    for video in manifest_data["videos"][:100]:
        title_clean = video["title"].replace("|", "-")
        markdown_lines.append(
            f"| `{video['video_id']}` | {video['notebook']} | [{title_clean}]({video['url']}) | "
            f"{video['char_count']:,} | `{video['sha256'][:10]}...` |"
        )

    json_path = os.path.join(OUT_DIR, "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json")
    md_path = os.path.join(OUT_DIR, "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.md")

    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(manifest_data, handle, indent=2)

    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(markdown_lines))

    print("[3/4] Manifests written locally:")
    print(f"  JSON: {json_path} ({os.path.getsize(json_path):,} bytes)")
    print(f"  MD:   {md_path} ({os.path.getsize(md_path):,} bytes)")

    return json_path, md_path


def sync_to_google_drive(
    md_path,
    json_path,
    executor=_exec_fd_capture,
    executable_resolver=shutil.which,
):
    """Run upload/list through the exact object that was opened and hashed."""
    print(f"[4/4] Synchronizing manifest to Google Drive ({ACCOUNT} -> {DRIVE_PARENT_ID})...")

    local_artifacts = {
        "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.md": _sha256_file(md_path),
        "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json": _sha256_file(json_path),
    }
    command_evidence = []

    md_result, md_evidence = _run_gog(
        ["drive", "upload", md_path, "--parent", DRIVE_PARENT_ID, "--account", ACCOUNT,
         "--name", "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.md", "--force"],
        "upload_md", executor, executable_resolver,
    )
    command_evidence.append(md_evidence)
    print("Drive Upload MD Output:", (md_result.stdout or "").strip())

    json_result, json_evidence = _run_gog(
        ["drive", "upload", json_path, "--parent", DRIVE_PARENT_ID, "--account", ACCOUNT,
         "--name", "TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json", "--force"],
        "upload_json", executor, executable_resolver,
    )
    command_evidence.append(json_evidence)
    print("Drive Upload JSON Output:", (json_result.stdout or "").strip())

    list_result, list_evidence = _run_gog(
        ["drive", "ls", "--parent", DRIVE_PARENT_ID, "--account", ACCOUNT,
         "--query", "name contains 'TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST'", "--plain"],
        "list_discovery", executor, executable_resolver,
    )
    command_evidence.append(list_evidence)
    print("\nDrive discovery output (UNVERIFIED remote byte parity):")
    print((list_result.stdout or "").strip())

    return {
        "decision": "HOLD_REMOTE_PARITY_UNVERIFIED",
        "sync_verified": False,
        "local_artifact_sha256": local_artifacts,
        "command_evidence": command_evidence,
        "remote_listing_observed": bool((list_result.stdout or "").strip()),
        "remote_object_ids": [],
        "remote_readback_sha256": {},
        "claim_ceiling": (
            "LOCAL_ARTIFACT_DIGESTS_AND_EXACT_OBJECT_COMMAND_SUCCESS_ONLY; "
            "NOT_PROVIDER_IDENTITY_OR_REMOTE_BYTE_PARITY"
        ),
    }


if __name__ == "__main__":
    json_path, md_path = extract_manifest()
    evidence = sync_to_google_drive(md_path, json_path)
    print("Sync evidence:", json.dumps(evidence, indent=2))
