#!/usr/bin/env python3
"""Fail-closed verifier for repository showcase artifact identity."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import re
import subprocess
from pathlib import Path

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
EXPECTED_TOP_LEVEL = {
    "version",
    "claim_class",
    "artifact_set_baseline_commit",
    "artifacts",
}
EXPECTED_ARTIFACT_KEYS = {"path", "sha256"}


class VerificationError(RuntimeError):
    pass


def _execution_head(repo_root: Path) -> str:
    github_sha = os.environ.get("GITHUB_SHA", "").strip()
    if HEX40.fullmatch(github_sha):
        return github_sha
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo_root, text=True
        ).strip()
    except Exception:
        return "UNAVAILABLE"


def verify_manifest(manifest_path: Path, repo_root: Path) -> dict:
    repo_root = repo_root.resolve()
    manifest_path = manifest_path.resolve()
    if not manifest_path.is_file():
        raise VerificationError(f"manifest missing: {manifest_path}")

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if set(data) != EXPECTED_TOP_LEVEL:
        raise VerificationError("manifest top-level schema mismatch")
    if data["version"] != 1:
        raise VerificationError("unsupported manifest version")
    if data["claim_class"] != "SHOWCASE_REPO_ARTIFACT_IDENTITY":
        raise VerificationError("unexpected claim class")
    if not HEX40.fullmatch(data["artifact_set_baseline_commit"]):
        raise VerificationError("invalid baseline commit")
    artifacts = data["artifacts"]
    if not isinstance(artifacts, list) or not artifacts:
        raise VerificationError("artifacts must be a non-empty list")

    seen: set[str] = set()
    verified = []
    for entry in artifacts:
        if not isinstance(entry, dict) or set(entry) != EXPECTED_ARTIFACT_KEYS:
            raise VerificationError("artifact schema mismatch")
        rel = entry["path"]
        expected = entry["sha256"]
        if not isinstance(rel, str) or not rel or Path(rel).is_absolute():
            raise VerificationError(f"invalid artifact path: {rel!r}")
        if rel in seen:
            raise VerificationError(f"duplicate artifact path: {rel}")
        seen.add(rel)
        if not isinstance(expected, str) or not HEX64.fullmatch(expected):
            raise VerificationError(f"invalid sha256 for {rel}")

        candidate = repo_root / rel
        if candidate.is_symlink():
            raise VerificationError(f"symlink artifact rejected: {rel}")
        resolved = candidate.resolve()
        try:
            resolved.relative_to(repo_root)
        except ValueError as exc:
            raise VerificationError(f"artifact escapes repository: {rel}") from exc
        if not resolved.is_file():
            raise VerificationError(f"artifact missing: {rel}")

        actual = hashlib.sha256(resolved.read_bytes()).hexdigest()
        if not hmac.compare_digest(actual, expected):
            raise VerificationError(
                f"artifact digest mismatch: {rel} expected={expected} actual={actual}"
            )
        verified.append({"path": rel, "sha256": actual})

    return {
        "status": "PASS",
        "claim_class": data["claim_class"],
        "artifact_set_baseline_commit": data["artifact_set_baseline_commit"],
        "execution_head": _execution_head(repo_root),
        "verified_artifacts": verified,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="showcase-identity-manifest.json")
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    try:
        result = verify_manifest(Path(args.manifest), Path(args.repo_root))
    except (VerificationError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
