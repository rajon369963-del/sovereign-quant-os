"""
⚡ Negative Test & Mutant Kills for Task T041: Showcase Semantic Identity Court.
"""
import json
import os
import tempfile
import unittest

from trading_os.showcase_semantic_court import (
    CANONICAL_TRADING_SYSTEM_ID,
    compute_file_sha256,
    verify_showcase_semantic_identity,
)


class TestT041Negative(unittest.TestCase):
    def setUp(self):
        self.repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.known_bad_path = os.path.join(self.repo_root, "tests", "fixtures", "known_bad_t041.json")
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_known_bad_fixture_rejected(self):
        self.assertTrue(os.path.exists(self.known_bad_path), "known_bad_t041.json fixture must exist")
        with open(self.known_bad_path, "r", encoding="utf-8") as f:
            bad_data = json.load(f)

        valid, errors = verify_showcase_semantic_identity(bad_data, base_dir=self.temp_dir.name)
        self.assertFalse(valid, "Known-bad showcase manifest MUST be rejected")
        self.assertTrue(any("Trading system ID mismatch" in e for e in errors))

    def test_mutant_zero_byte_hollow_file(self):
        empty_file = os.path.join(self.temp_dir.name, "empty_metrics.json")
        with open(empty_file, "w") as f:
            pass  # 0 bytes

        manifest = {
            "showcase_manifest": {
                "manifest_version": "1.0.0",
                "trading_system_id": CANONICAL_TRADING_SYSTEM_ID,
                "artifacts": [
                    {
                        "name": "empty_metrics.json",
                        "declared_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                        "semantic_type": "portfolio_metrics",
                        "required_schema_keys": ["sharpe"],
                    }
                ],
            }
        }
        valid, errors = verify_showcase_semantic_identity(manifest, base_dir=self.temp_dir.name)
        self.assertFalse(valid, "0-byte hollow file must be rejected")
        self.assertTrue(any("is empty (0 bytes)" in e for e in errors))

    def test_mutant_hash_mismatch(self):
        test_file = os.path.join(self.temp_dir.name, "tampered_metrics.json")
        with open(test_file, "w") as f:
            json.dump({"sharpe": 1.2}, f)

        manifest = {
            "showcase_manifest": {
                "manifest_version": "1.0.0",
                "trading_system_id": CANONICAL_TRADING_SYSTEM_ID,
                "artifacts": [
                    {
                        "name": "tampered_metrics.json",
                        "declared_sha256": "1" * 64,  # Falsified digest
                        "semantic_type": "portfolio_metrics",
                        "required_schema_keys": ["sharpe"],
                    }
                ],
            }
        }
        valid, errors = verify_showcase_semantic_identity(manifest, base_dir=self.temp_dir.name)
        self.assertFalse(valid, "SHA-256 hash mismatch must be rejected")
        self.assertTrue(any("SHA-256 mismatch" in e for e in errors))

    def test_mutant_missing_schema_keys(self):
        test_file = os.path.join(self.temp_dir.name, "incomplete_metrics.json")
        with open(test_file, "w") as f:
            json.dump({"unrelated_key": 42}, f)

        actual_sha = compute_file_sha256(test_file)
        manifest = {
            "showcase_manifest": {
                "manifest_version": "1.0.0",
                "trading_system_id": CANONICAL_TRADING_SYSTEM_ID,
                "artifacts": [
                    {
                        "name": "incomplete_metrics.json",
                        "declared_sha256": actual_sha,
                        "semantic_type": "portfolio_metrics",
                        "required_schema_keys": ["sharpe", "max_drawdown"],
                    }
                ],
            }
        }
        valid, errors = verify_showcase_semantic_identity(manifest, base_dir=self.temp_dir.name)
        self.assertFalse(valid, "Missing required schema keys must be rejected")
        self.assertTrue(any("missing required semantic key" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
