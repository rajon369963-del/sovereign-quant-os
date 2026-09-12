#!/usr/bin/env python3
"""Independent kill-mutant court for Issue #54 / PR #55.

The repaired disconnected Dhan envelope is only causally protected if the existing
authority tests go RED when one live-authority field is regressed at a time.
All mutants run from temporary source copies and use no broker credentials, network,
or real-money effects.
"""

import importlib.util
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
BRIDGE_PATH = REPO_ROOT / "dhan_live_bridge.py"
COURT_PATH = REPO_ROOT / "tests" / "test_dhan_mode_authority.py"


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _load_mutant(tmp_path: Path, needle: str, replacement: str, name: str):
    source = BRIDGE_PATH.read_text(encoding="utf-8")
    assert source.count(needle) == 1, f"Expected one mutation target for {name!r}"
    mutant_path = tmp_path / f"dhan_live_bridge_{name}.py"
    mutant_path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
    return _load_module(mutant_path, f"air10_dhan_{name}_mutant")


def _assert_existing_test_goes_red(mutant_bridge_class, target_test_name: str):
    court = _load_module(COURT_PATH, f"air10_dhan_court_{target_test_name}")
    production_bridge = court.DhanLiveBridge
    court.DhanLiveBridge = mutant_bridge_class
    try:
        case = court.DhanModeAuthorityCourt(methodName=target_test_name)
        with pytest.raises(AssertionError):
            getattr(case, target_test_name)()
    finally:
        court.DhanLiveBridge = production_bridge


@pytest.mark.parametrize(
    ("needle", "replacement", "name"),
    [
        ('            "status": "SIMULATED",\n', '            "status": "ORDER_PLACED",  # KILL MUTANT\n', "status_live"),
        ('            "execution_mode": "SIMULATED",\n', '            "execution_mode": "LIVE",  # KILL MUTANT\n', "execution_mode_live"),
        ('            "connection_authority": "ABSENT",\n', '            "connection_authority": "PRESENT",  # KILL MUTANT\n', "authority_present"),
        ('            "is_simulated": True,\n', '            "is_simulated": False,  # KILL MUTANT\n', "simulation_flag_false"),
        ('            "broker_order_id": None,\n', '            "broker_order_id": "MUTANT-LIVE-ID",  # KILL MUTANT\n', "broker_id_present"),
    ],
)
def test_order_authority_regressions_are_killed(tmp_path, needle, replacement, name):
    mutant = _load_mutant(tmp_path, needle, replacement, name)
    _assert_existing_test_goes_red(
        mutant.DhanLiveBridge,
        "test_disconnected_order_is_unrepresentable_as_live_success",
    )


@pytest.mark.parametrize(
    ("needle", "replacement", "name"),
    [
        ("                simulated_balance_hint=1.00,\n", "                deposited_balance=1.00,  # KILL MUTANT: live-like field\n", "live_balance_field"),
        ("                simulated_ltp_hint=684.85,\n", "                ltp=684.85,  # KILL MUTANT: live-like field\n", "live_ltp_field"),
    ],
)
def test_live_like_numeric_fields_are_killed(tmp_path, needle, replacement, name):
    mutant = _load_mutant(tmp_path, needle, replacement, name)
    _assert_existing_test_goes_red(
        mutant.DhanLiveBridge,
        "test_disconnected_balance_and_quote_do_not_use_live_value_fields",
    )
