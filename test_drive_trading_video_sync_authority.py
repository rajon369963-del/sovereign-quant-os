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
            handle.write(b"#!/bin/sh\necho ORIGINAL\nexit 0\n")
        os.chmod(gog_path, 0o755)
        return md_path, json_path, gog_path

    def _fake_executor(self, outputs=None, returncode=0):
        calls = []
        def execute(fd, command):
            calls.append((fd, list(command), sync._sha256_fd(fd)))
            stdout = (outputs or {}).get("ls", "uploaded") if "ls" in command else (outputs or {}).get("upload", "uploaded")
            return subprocess.CompletedProcess(command, returncode, stdout=stdout, stderr="" if returncode == 0 else "denied")
        return execute, calls

    def test_fake_zero_exit_plausible_output_never_becomes_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            md_path, json_path, gog_path = self._fixture_files(tmp)
            executor, calls = self._fake_executor({"ls": "plausible-id manifest.json"})
            evidence = sync.sync_to_google_drive(md_path, json_path, executor=executor, executable_resolver=lambda _: gog_path)
            self.assertEqual(evidence["decision"], "HOLD_REMOTE_PARITY_UNVERIFIED")
            self.assertFalse(evidence["sync_verified"])
            self.assertEqual(evidence["remote_object_ids"], [])
            self.assertEqual(len(calls), 3)
            expected = hashlib.sha256(open(gog_path, "rb").read()).hexdigest()
            for item in evidence["command_evidence"]:
                self.assertEqual(item["command_sha256"], expected)
                self.assertEqual(item["execution_binding"], "OPEN_HASH_EXEC_SAME_FD")

    def test_nonzero_upload_fails_closed_before_listing(self):
        with tempfile.TemporaryDirectory() as tmp:
            md_path, json_path, gog_path = self._fixture_files(tmp)
            executor, calls = self._fake_executor(returncode=23)
            with self.assertRaises(sync.SyncAuthorityError):
                sync.sync_to_google_drive(md_path, json_path, executor=executor, executable_resolver=lambda _: gog_path)
            self.assertEqual(len(calls), 1)

    def test_name_presence_cannot_satisfy_byte_parity(self):
        with tempfile.TemporaryDirectory() as tmp:
            md_path, json_path, gog_path = self._fixture_files(tmp)
            executor, _ = self._fake_executor({"ls": "wrong-id TRADING_VIDEOS_CANONICAL_VAULT_MANIFEST.json"})
            evidence = sync.sync_to_google_drive(md_path, json_path, executor=executor, executable_resolver=lambda _: gog_path)
            self.assertTrue(evidence["remote_listing_observed"])
            self.assertFalse(evidence["sync_verified"])
            self.assertEqual(evidence["remote_readback_sha256"], {})

    def test_path_swap_after_open_cannot_change_bound_object(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, _, gog_path = self._fixture_files(tmp)
            original_sha = hashlib.sha256(open(gog_path, "rb").read()).hexdigest()
            observed = {}
            def attack_executor(fd, command):
                replacement = gog_path + ".replacement"
                with open(replacement, "wb") as handle:
                    handle.write(b"#!/bin/sh\necho ATTACKER\nexit 0\n")
                os.chmod(replacement, 0o755)
                os.replace(replacement, gog_path)
                observed["fd_sha"] = sync._sha256_fd(fd)
                observed["path_sha"] = hashlib.sha256(open(gog_path, "rb").read()).hexdigest()
                return subprocess.CompletedProcess(command, 0, stdout="ok", stderr="")
            result, evidence = sync._run_gog(["--help"], "swap_attack", attack_executor, lambda _: gog_path)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(evidence["command_sha256"], original_sha)
            self.assertEqual(observed["fd_sha"], original_sha)
            self.assertNotEqual(observed["path_sha"], original_sha)

    def test_default_executor_runs_opened_object_when_fd_exec_supported(self):
        if os.execve not in getattr(os, "supports_fd", set()):
            self.skipTest("fd exec unsupported on this platform")
        with tempfile.TemporaryDirectory() as tmp:
            _, _, gog_path = self._fixture_files(tmp)
            result, evidence = sync._run_gog([], "physical_fd_exec", executable_resolver=lambda _: gog_path)
            self.assertEqual(result.returncode, 0)
            self.assertIn("ORIGINAL", result.stdout)
            self.assertEqual(evidence["execution_binding"], "OPEN_HASH_EXEC_SAME_FD")


if __name__ == "__main__":
    unittest.main()
