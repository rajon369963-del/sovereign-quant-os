from scripts.check_required_context_authority import classify

MAIN = "a" * 40
OTHER = "b" * 40


def test_true_main_push_same_sha_passes():
    assert classify("push", "refs/heads/main", MAIN, MAIN) == "PASS_MAIN_AUTHORITY"


def test_same_sha_feature_ref_cannot_certify_main():
    assert classify("push", "refs/heads/feat/replay", MAIN, MAIN) == "HOLD_ALT_REF_REPLAY_OF_MAIN_SHA"


def test_same_sha_workflow_dispatch_cannot_certify_main():
    assert classify("workflow_dispatch", "refs/heads/main", MAIN, MAIN) == "HOLD_ALT_REF_REPLAY_OF_MAIN_SHA"


def test_main_push_mismatch_fails_closed():
    assert classify("push", "refs/heads/main", OTHER, MAIN) == "HOLD_MAIN_SHA_MISMATCH"


def test_distinct_non_main_sha_remains_bounded():
    assert classify("pull_request", "refs/pull/56/merge", OTHER, MAIN) == "PASS_BOUNDED_NON_MAIN"
