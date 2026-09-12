#!/usr/bin/env python3
"""TDD RED reproducer for Quant Issue #49.

These tests deliberately use the old on-disk signed-receipt mutation pattern and
require the downstream target validator's rejection marker. Current main is
expected to fail this court because canonical-payload/signature verification
rejects the tampered receipt before commit/tree/script validation is reached.
"""

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
RECEIPT = REPO_ROOT / "db" / "STRESS_BENCHMARK_REAL_WHEELS.json"


def _run_tampered(mutator):
    original = RECEIPT.read_bytes()
    data = json.loads(original.decode("utf-8"))
    hostile = copy.deepcopy(data)
    mutator(hostile)
    try:
        RECEIPT.write_text(json.dumps(hostile, indent=2), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, "scripts/verify_receipt.py", "--zero-drift-check"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        return proc.returncode, proc.stdout + proc.stderr
    finally:
        RECEIPT.write_bytes(original)


def test_fake_commit_must_reach_commit_validator():
    rc, output = _run_tampered(
        lambda d: d["hardware_telemetry"].__setitem__("benchmarked_source_commit_sha", "0" * 40)
    )
    assert rc != 0
    assert "is NOT reachable in git history" in output


def test_fake_tree_must_reach_tree_validator():
    rc, output = _run_tampered(
        lambda d: d["hardware_telemetry"].__setitem__("benchmarked_source_tree_sha", "f" * 40)
    )
    assert rc != 0
    assert "Commit tree mismatch against signed receipt" in output


def test_tampered_script_must_reach_script_validator():
    rc, output = _run_tampered(
        lambda d: d["hardware_telemetry"].__setitem__("benchmark_script_sha256", "1" * 64)
    )
    assert rc != 0
    assert "Benchmark script SHA-256 mismatch against signed receipt" in output
