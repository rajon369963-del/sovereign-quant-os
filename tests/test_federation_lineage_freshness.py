#!/usr/bin/env python3
"""V2.2 hostile court for federation branch-lineage freshness.

The production verifier must accept equality and forward descent from the
canonical expected HEAD, but must reject/HOLD the reverse stale-ancestor
relationship. The fixture uses a real isolated git DAG and calls the production
lineage classifier imported from scripts/verify_federation_manifest.py.
"""

import importlib.util
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "scripts" / "verify_federation_manifest.py"

spec = importlib.util.spec_from_file_location("air10_federation_verifier", VERIFIER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
classify_branch_lineage = module.classify_branch_lineage


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def commit(repo: Path, value: str) -> str:
    (repo / "state.txt").write_text(value, encoding="utf-8")
    subprocess.check_call(["git", "add", "state.txt"], cwd=repo)
    subprocess.check_call(["git", "commit", "-m", f"state-{value}"], cwd=repo, stdout=subprocess.DEVNULL)
    return git(repo, "rev-parse", "HEAD")


def build_linear_dag(repo: Path):
    subprocess.check_call(["git", "init", "-q"], cwd=repo)
    git(repo, "config", "user.email", "air10-court@example.invalid")
    git(repo, "config", "user.name", "AIR10 Court")
    a = commit(repo, "A")
    b = commit(repo, "B")
    c = commit(repo, "C")
    return a, b, c


def old_symmetric_mutant_accepts(repo: Path, expected: str, actual: str) -> bool:
    if actual == expected:
        return True
    expected_to_actual = subprocess.run(
        ["git", "merge-base", "--is-ancestor", expected, actual], cwd=repo
    ).returncode == 0
    actual_to_expected = subprocess.run(
        ["git", "merge-base", "--is-ancestor", actual, expected], cwd=repo
    ).returncode == 0
    return expected_to_actual or actual_to_expected


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="air10-lineage-") as tmp:
        repo = Path(tmp)
        a, b, c = build_linear_dag(repo)

        assert classify_branch_lineage(repo, c, c) == "PASS_EXACT"
        assert classify_branch_lineage(repo, b, c) == "PASS_DESCENDANT"

        # Hostile known-bad: manifest expects fresh C but worktree is stale B.
        # The old symmetric ancestry rule accepted this exact state.
        assert old_symmetric_mutant_accepts(repo, c, b) is True
        assert classify_branch_lineage(repo, c, b) == "STALE_ANCESTOR"

        # A still being behind C must also be typed stale, not lineage-verified.
        assert classify_branch_lineage(repo, c, a) == "STALE_ANCESTOR"

        # Unrelated history must remain fail-closed.
        subprocess.check_call(["git", "checkout", "--orphan", "unrelated"], cwd=repo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.check_call(["git", "rm", "-rf", "."], cwd=repo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        unrelated = commit(repo, "U")
        assert classify_branch_lineage(repo, c, unrelated) == "FAIL_UNRELATED"

    print("PASS: directional lineage freshness court rejects stale reverse ancestry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
