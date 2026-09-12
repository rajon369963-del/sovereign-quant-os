#!/usr/bin/env python3
import hashlib
import os
import subprocess
import tempfile
import unittest

import drive_trading_video_sync as sync


class GogAuthorityCourt(unittest.TestCase):
    def _fixture_files(self, tmp):
        md_path = os.path.join(tmp, "manifest.md")
        json_path = os.path.join(tmp, "manifest.json")
        gog_path = os.path.join(tmp, "gog")
        with open(md_path, "wb") as handle:
            handle.write(b"# manifest\n")
        with open(json_path, "wb") as handle:
            handle.write(b'{"ok":true}\n')
        with open(gog_path, "wb") as handle:
            handle.write(b"#!/bin/sh\nexit 0\n")
        os.chmod(gog_path, 0o755)
        return md_path, json_path, gog_path

    def test_fake_zero_exit_plausible_output_never_becomes_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            md_path, json_path, gog_path = self._fixture_files(tmp)
            calls = []

            def runner(command, capture_output, text):
                calls.append(command)
                if "upload" in command:
                    stdout = "Uploaded file id=plausible-remote-object"
                else:
                    stdout = "plausible-remote-object TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json"
                return subprocess.CompletedProcess(command, 0, stdout=stdout, stderr="")

            evidence = sync.sync_to_google_drive(
                md_path,
                json_path,
                runner=runner,
                executable_resolver=lambda _: gog_path,
            )

            self.assertEqual(evidence["decision"], "HOLD_REMOTE_PARITY_UNVERIFIED")
            self.assertFalse(evidence["sync_verified"])
            self.assertEqual(evidence["remote_object_ids"], [])
            self.assertEqual(evidence["remote_readback_sha256"], {})
            self.assertEqual(len(calls), 3)
            expected_gog_sha = hashlib.sha256(open(gog_path, "rb").read()).hexdigest()
            for command_evidence in evidence["command_evidence"]:
                self.assertEqual(command_evidence["command_path"], os.path.realpath(gog_path))
                self.assertEqual(command_evidence["command_sha256"], expected_gog_sha)
                self.assertEqual(command_evidence["return_code"], 0)

    def test_nonzero_upload_fails_closed_before_listing(self):
        with tempfile.TemporaryDirectory() as tmp:
            md_path, json_path, gog_path = self._fixture_files(tmp)
            calls = []

            def runner(command, capture_output, text):
                calls.append(command)
                return subprocess.CompletedProcess(command, 23, stdout="", stderr="upload denied")

            with self.assertRaises(sync.SyncAuthorityError):
                sync.sync_to_google_drive(
                    md_path,
                    json_path,
                    runner=runner,
                    executable_resolver=lambda _: gog_path,
                )

            self.assertEqual(len(calls), 1)
            self.assertIn("upload", calls[0])
            self.assertNotIn("ls", calls[0])

    def test_name_presence_cannot_satisfy_byte_parity(self):
        with tempfile.TemporaryDirectory() as tmp:
            md_path, json_path, gog_path = self._fixture_files(tmp)

            def runner(command, capture_output, text):
                if "ls" in command:
                    stdout = "wrong-id TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json"
                else:
                    stdout = "uploaded wrong-id"
                return subprocess.CompletedProcess(command, 0, stdout=stdout, stderr="")

            evidence = sync.sync_to_google_drive(
                md_path,
                json_path,
                runner=runner,
                executable_resolver=lambda _: gog_path,
            )

            self.assertTrue(evidence["remote_listing_observed"])
            self.assertFalse(evidence["sync_verified"])
            self.assertEqual(evidence["remote_object_ids"], [])
            self.assertIn("NOT_PROVIDER_IDENTITY_OR_REMOTE_BYTE_PARITY", evidence["claim_ceiling"])


if __name__ == "__main__":
    unittest.main()
