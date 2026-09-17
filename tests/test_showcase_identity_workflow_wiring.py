from pathlib import Path


def test_required_showcase_workflow_invokes_semantic_identity_verifier() -> None:
    workflow = Path(".github/workflows/viral-showcase.yml").read_text(encoding="utf-8")
    assert "python3 scripts/verify_showcase_identity.py" in workflow, "semantic identity verifier was bypassed/removed from required workflow"
    assert "--manifest showcase-identity-manifest.json" in workflow, "showcase manifest was disconnected from required workflow"
    assert "--authority-commit" in workflow, "frozen authority commit was disconnected from required workflow"
    assert 'authority_context="$(git merge-base HEAD origin/main)"' in workflow, "pull-request/branch authority context is not bound to protected main history"


def test_required_showcase_workflow_selects_frozen_baseline_from_protected_context() -> None:
    workflow = Path(".github/workflows/viral-showcase.yml").read_text(encoding="utf-8")
    assert 'before_sha="${{ github.event.before }}"' in workflow, "main-push authority is not anchored to the pre-push provider head"
    assert 'git show "${authority_context}:showcase-identity-manifest.json"' in workflow, "frozen baseline is not read from protected historical context"
    assert '["artifact_set_baseline_commit"]' in workflow, "protected context no longer selects the frozen artifact baseline"
    assert 'authority_commit="$(git merge-base HEAD origin/main' not in workflow, "moving current HEAD must not become showcase artifact authority"


def test_required_showcase_workflow_runs_negative_identity_fixtures() -> None:
    workflow = Path(".github/workflows/viral-showcase.yml").read_text(encoding="utf-8")
    assert "tests/test_showcase_identity.py" in workflow, "wrong-byte negative fixtures are not wired into required workflow"
    assert "tests/test_showcase_identity_workflow_wiring.py" in workflow, "wiring kill-mutant court is not self-enforced"
