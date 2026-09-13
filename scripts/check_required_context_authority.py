#!/usr/bin/env python3
"""Bind required-check authority to event/ref semantics, not SHA+check-name alone."""
from __future__ import annotations

import argparse


def classify(event: str, ref: str, head_sha: str, main_sha: str) -> str:
    event = (event or "").strip()
    ref = (ref or "").strip()
    head_sha = (head_sha or "").strip()
    main_sha = (main_sha or "").strip()
    if not head_sha or not main_sha:
        return "HOLD_MISSING_SHA"
    true_main_push = event == "push" and ref == "refs/heads/main"
    if true_main_push:
        return "PASS_MAIN_AUTHORITY" if head_sha == main_sha else "HOLD_MAIN_SHA_MISMATCH"
    if head_sha == main_sha:
        return "HOLD_ALT_REF_REPLAY_OF_MAIN_SHA"
    return "PASS_BOUNDED_NON_MAIN"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--event", required=True)
    p.add_argument("--ref", required=True)
    p.add_argument("--head-sha", required=True)
    p.add_argument("--main-sha", required=True)
    args = p.parse_args()
    verdict = classify(args.event, args.ref, args.head_sha, args.main_sha)
    print(verdict)
    return 0 if verdict.startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
