from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verify_showcase_identity import VerificationError, verify_manifest


def _manifest(root: Path, payload: bytes = b"trusted-showcase") -> Path:
    artifact = root / "showcase.html"
    artifact.write_bytes(payload)
    manifest = {
        "version": 1,
        "claim_class": "SHOWCASE_REPO_ARTIFACT_IDENTITY",
        "artifact_set_baseline_commit": "a" * 40,
        "artifacts": [
            {
                "path": "showcase.html",
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
        ],
    }
    path = root / "showcase-identity-manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    return path


def test_known_good_exact_bytes_pass(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    result = verify_manifest(manifest, tmp_path)
    assert result["status"] == "PASS"
    assert result["verified_artifacts"][0]["path"] == "showcase.html"


def test_same_filename_wrong_bytes_fail(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    (tmp_path / "showcase.html").write_bytes(b"stale-or-wrong-showcase")
    with pytest.raises(VerificationError, match="digest mismatch"):
        verify_manifest(manifest, tmp_path)


def test_wrong_manifest_digest_fails(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["artifacts"][0]["sha256"] = "0" * 64
    manifest.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(VerificationError, match="digest mismatch"):
        verify_manifest(manifest, tmp_path)


def test_path_traversal_fails_closed(tmp_path: Path) -> None:
    manifest = _manifest(tmp_path)
    outside = tmp_path.parent / "outside-showcase.txt"
    outside.write_bytes(b"outside")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["artifacts"] = [
        {"path": "../outside-showcase.txt", "sha256": hashlib.sha256(b"outside").hexdigest()}
    ]
    manifest.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(VerificationError, match="escapes repository"):
        verify_manifest(manifest, tmp_path)


def test_symlink_artifact_fails_closed(tmp_path: Path) -> None:
    target = tmp_path / "target.html"
    target.write_bytes(b"trusted-showcase")
    link = tmp_path / "showcase.html"
    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        pytest.skip("symlink unavailable")
    manifest = {
        "version": 1,
        "claim_class": "SHOWCASE_REPO_ARTIFACT_IDENTITY",
        "artifact_set_baseline_commit": "a" * 40,
        "artifacts": [
            {"path": "showcase.html", "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
        ],
    }
    manifest_path = tmp_path / "showcase-identity-manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(VerificationError, match="symlink artifact rejected"):
        verify_manifest(manifest_path, tmp_path)
