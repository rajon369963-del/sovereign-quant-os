"""
⚡ Positive Test for Task T041: Showcase Semantic Identity Court.
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


class TestT041Positive(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.artifact_name = "portfolio_metrics.json"
        self.artifact_path = os.path.join(self.temp_dir.name, self.artifact_name)

        self.valid_data = {
            "symbol": "NSE:NIFTY50",
            "timestamp": 1789407290.0,
            "sharpe": 2.45,
            "max_drawdown": 0.042,
            "win_rate": 0.68,
        }
        with open(self.artifact_path, "w", encoding="utf-8") as f:
            json.dump(self.valid_data, f)

        self.actual_sha = compute_file_sha256(self.artifact_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_canonical_showcase_validation(self):
        manifest = {
            "showcase_manifest": {
                "manifest_version": "1.0.0",
                "trading_system_id": CANONICAL_TRADING_SYSTEM_ID,
                "artifacts": [
                    {
                        "name": self.artifact_name,
                        "declared_sha256": self.actual_sha,
                        "semantic_type": "portfolio_metrics",
                        "required_schema_keys": ["sharpe", "max_drawdown", "win_rate"],
                    }
                ],
            }
        }
        valid, errors = verify_showcase_semantic_identity(manifest, base_dir=self.temp_dir.name)
        self.assertTrue(valid, f"Showcase manifest should pass verification, errors: {errors}")
        self.assertEqual(len(errors), 0)


if __name__ == "__main__":
    unittest.main()
