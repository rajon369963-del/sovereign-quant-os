from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verify_showcase_identity as vsi
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


def _rotation_record(manifest: Path, authority: str) -> bytes:
    data = json.loads(manifest.read_text(encoding="utf-8"))
    return json.dumps(
        {
            "version": 1,
            "claim_class": "SHOWCASE_REPO_ARTIFACT_AUTHORITY_ROTATION",
            "old_authority_commit": authority,
            "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
            "artifacts": data["artifacts"],
        }
    ).encode()


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
    with pytest.raises(VerificationError, match="invalid artifact path"):
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


def test_reviewed_authority_rotation_allows_exact_new_bytes(tmp_path: Path, monkeypatch) -> None:
    authority = "a" * 40
    old_payload = b"old-reviewed-showcase"
    new_payload = b"new-reviewed-showcase"
    manifest = _manifest(tmp_path, new_payload)
    record = _rotation_record(manifest, authority)

    def fake_git_blob(_repo_root: Path, commit: str, rel: str) -> bytes:
        assert commit == authority
        if rel == "showcase.html":
            return old_payload
        if rel == "showcase-authority-rotation.json":
            return record
        raise AssertionError(rel)

    monkeypatch.setattr(vsi, "_git_blob", fake_git_blob)
    result = verify_manifest(manifest, tmp_path, authority_commit=authority)
    assert result["status"] == "PASS"
    assert result["authority_rotation"] is True


def test_same_revision_coedit_without_reviewed_rotation_fails(tmp_path: Path, monkeypatch) -> None:
    authority = "a" * 40
    manifest = _manifest(tmp_path, b"new-unreviewed-showcase")

    def fake_git_blob(_repo_root: Path, _commit: str, rel: str) -> bytes:
        if rel == "showcase.html":
            return b"old-reviewed-showcase"
        raise VerificationError("authority artifact unavailable")

    monkeypatch.setattr(vsi, "_git_blob", fake_git_blob)
    with pytest.raises(VerificationError, match="authority artifact unavailable"):
        verify_manifest(manifest, tmp_path, authority_commit=authority)


def test_rotation_wrong_old_authority_fails(tmp_path: Path, monkeypatch) -> None:
    authority = "a" * 40
    manifest = _manifest(tmp_path, b"new-reviewed-showcase")
    record = json.loads(_rotation_record(manifest, authority).decode())
    record["old_authority_commit"] = "b" * 40

    def fake_git_blob(_repo_root: Path, _commit: str, rel: str) -> bytes:
        if rel == "showcase.html":
            return b"old-reviewed-showcase"
        if rel == "showcase-authority-rotation.json":
            return json.dumps(record).encode()
        raise AssertionError(rel)

    monkeypatch.setattr(vsi, "_git_blob", fake_git_blob)
    with pytest.raises(VerificationError, match="old authority mismatch"):
        verify_manifest(manifest, tmp_path, authority_commit=authority)


def test_rotation_wrong_manifest_digest_fails(tmp_path: Path, monkeypatch) -> None:
    authority = "a" * 40
    manifest = _manifest(tmp_path, b"new-reviewed-showcase")
    record = json.loads(_rotation_record(manifest, authority).decode())
    record["manifest_sha256"] = "0" * 64

    def fake_git_blob(_repo_root: Path, _commit: str, rel: str) -> bytes:
        if rel == "showcase.html":
            return b"old-reviewed-showcase"
        if rel == "showcase-authority-rotation.json":
            return json.dumps(record).encode()
        raise AssertionError(rel)

    monkeypatch.setattr(vsi, "_git_blob", fake_git_blob)
    with pytest.raises(VerificationError, match="manifest digest mismatch"):
        verify_manifest(manifest, tmp_path, authority_commit=authority)


def test_rotation_unrelated_artifact_set_fails(tmp_path: Path, monkeypatch) -> None:
    authority = "a" * 40
    manifest = _manifest(tmp_path, b"new-reviewed-showcase")
    record = json.loads(_rotation_record(manifest, authority).decode())
    record["artifacts"][0]["path"] = "other.html"

    def fake_git_blob(_repo_root: Path, _commit: str, rel: str) -> bytes:
        if rel == "showcase.html":
            return b"old-reviewed-showcase"
        if rel == "showcase-authority-rotation.json":
            return json.dumps(record).encode()
        raise AssertionError(rel)

    monkeypatch.setattr(vsi, "_git_blob", fake_git_blob)
    with pytest.raises(VerificationError, match="artifact set mismatch"):
        verify_manifest(manifest, tmp_path, authority_commit=authority)
