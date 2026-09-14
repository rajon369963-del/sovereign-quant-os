from __future__ import annotations

import hashlib
import json
import subprocess
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


def _artifact_set_sha256(artifacts: list[dict]) -> str:
    canonical = json.dumps(
        artifacts, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _rotation_record(manifest: Path) -> bytes:
    data = json.loads(manifest.read_text(encoding="utf-8"))
    return json.dumps(
        {
            "version": 1,
            "claim_class": "SHOWCASE_REPO_ARTIFACT_AUTHORITY_ROTATION",
            "artifact_set_sha256": _artifact_set_sha256(data["artifacts"]),
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
    record = _rotation_record(manifest)

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


def test_rotation_wrong_artifact_set_digest_fails(tmp_path: Path, monkeypatch) -> None:
    authority = "a" * 40
    manifest = _manifest(tmp_path, b"new-reviewed-showcase")
    record = json.loads(_rotation_record(manifest).decode())
    record["artifact_set_sha256"] = "0" * 64

    def fake_git_blob(_repo_root: Path, _commit: str, rel: str) -> bytes:
        if rel == "showcase.html":
            return b"old-reviewed-showcase"
        if rel == "showcase-authority-rotation.json":
            return json.dumps(record).encode()
        raise AssertionError(rel)

    monkeypatch.setattr(vsi, "_git_blob", fake_git_blob)
    with pytest.raises(VerificationError, match="artifact-set digest mismatch"):
        verify_manifest(manifest, tmp_path, authority_commit=authority)


def test_rotation_unrelated_artifact_set_fails(tmp_path: Path, monkeypatch) -> None:
    authority = "a" * 40
    manifest = _manifest(tmp_path, b"new-reviewed-showcase")
    record = json.loads(_rotation_record(manifest).decode())
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


def _git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, text=True
    )
    return completed.stdout.strip()


def _build_real_git_rotation_fixture(root: Path, mode: str = "valid") -> tuple[str, str, Path]:
    root.mkdir(parents=True, exist_ok=True)
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "air10-court@example.invalid")
    _git(root, "config", "user.name", "AIR10 Realpath Court")

    old_payload = b"old-reviewed-showcase"
    new_payload = b"new-reviewed-showcase"
    artifacts = [
        {"path": "showcase.html", "sha256": hashlib.sha256(new_payload).hexdigest()}
    ]
    record_artifacts = json.loads(json.dumps(artifacts))
    if mode == "unrelated":
        record_artifacts[0]["path"] = "other.html"
    record = {
        "version": 1,
        "claim_class": "SHOWCASE_REPO_ARTIFACT_AUTHORITY_ROTATION",
        "artifact_set_sha256": _artifact_set_sha256(record_artifacts),
        "artifacts": record_artifacts,
    }
    if mode == "wrong-digest":
        record["artifact_set_sha256"] = "0" * 64

    (root / "showcase.html").write_bytes(old_payload)
    if mode != "missing":
        (root / "showcase-authority-rotation.json").write_text(
            json.dumps(record, sort_keys=True), encoding="utf-8"
        )
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "review future showcase rotation")
    authority = _git(root, "rev-parse", "HEAD")

    (root / "showcase.html").write_bytes(new_payload)
    manifest = {
        "version": 1,
        "claim_class": "SHOWCASE_REPO_ARTIFACT_IDENTITY",
        "artifact_set_baseline_commit": authority,
        "artifacts": artifacts,
    }
    manifest_path = root / "showcase-identity-manifest.json"
    manifest_path.write_text(json.dumps(manifest, sort_keys=True), encoding="utf-8")
    _git(root, "add", ".")
    _git(root, "commit", "-q", "-m", "apply reviewed showcase rotation")
    candidate = _git(root, "rev-parse", "HEAD")
    return authority, candidate, manifest_path


def _run_real_cli(root: Path, manifest: Path, authority: str) -> subprocess.CompletedProcess[str]:
    script = Path(__file__).resolve().parents[1] / "scripts" / "verify_showcase_identity.py"
    return subprocess.run(
        [
            sys.executable,
            str(script),
            "--manifest",
            str(manifest),
            "--repo-root",
            str(root),
            "--authority-commit",
            authority,
        ],
        capture_output=True,
        text=True,
    )


def test_real_git_history_authorized_rotation_exact_cli_passes(tmp_path: Path) -> None:
    root = tmp_path / "valid"
    authority, _candidate, manifest = _build_real_git_rotation_fixture(root, "valid")
    completed = _run_real_cli(root, manifest, authority)
    assert completed.returncode == 0, completed.stdout + completed.stderr
    result = json.loads(completed.stdout)
    assert result["status"] == "PASS"
    assert result["authority_rotation"] is True
    assert result["authority_commit"] == authority


@pytest.mark.parametrize(
    ("mode", "expected_error"),
    [
        ("missing", "authority artifact unavailable"),
        ("wrong-digest", "rotation artifact-set digest mismatch"),
        ("unrelated", "rotation artifact set mismatch"),
    ],
)
def test_real_git_history_rotation_negatives_fail_closed(
    tmp_path: Path, mode: str, expected_error: str
) -> None:
    root = tmp_path / mode
    authority, _candidate, manifest = _build_real_git_rotation_fixture(root, mode)
    completed = _run_real_cli(root, manifest, authority)
    assert completed.returncode != 0
    result = json.loads(completed.stdout)
    assert result["status"] == "FAIL"
    assert expected_error in result["error"]


def test_real_git_history_wrong_authority_commit_fails_closed(tmp_path: Path) -> None:
    root = tmp_path / "wrong-authority"
    authority, candidate, manifest = _build_real_git_rotation_fixture(root, "valid")
    assert authority != candidate
    completed = _run_real_cli(root, manifest, candidate)
    assert completed.returncode != 0
    result = json.loads(completed.stdout)
    assert result["status"] == "FAIL"
    assert "baseline authority mismatch" in result["error"]
