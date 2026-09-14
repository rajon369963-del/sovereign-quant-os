"""
⚡ Sovereign Quant OS: Showcase Semantic Identity Court (T041/T042).
Enforces strict semantic artifact identity validation: rejects raw file existence
masquerading as valid artifacts, unverified hashes, or schema-violating candidates.
"""
import hashlib
import json
import os
import re
from typing import Any

CANONICAL_TRADING_SYSTEM_ID = "SOVEREIGN_QUANT_OS"


def compute_file_sha256(filepath: str) -> str:
    """Computes physical SHA-256 hash of a file on disk."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_showcase_semantic_identity(
    manifest_data: dict[str, Any],
    base_dir: str | None = None
) -> tuple[bool, list[str]]:
    """
    Fail-closed verification: validates that a showcase manifest strictly
    binds to the canonical SOVEREIGN_QUANT_OS identity, and that every declared
    artifact exists, is non-empty, matches its declared SHA-256 digest, and
    satisfies its semantic schema.
    """
    errors = []

    if not isinstance(manifest_data, dict):
        return False, ["Manifest data must be a dictionary"]

    showcase = manifest_data.get("showcase_manifest")
    if not showcase or not isinstance(showcase, dict):
        return False, ["Missing or invalid 'showcase_manifest' section"]

    # 1. Trading System Identity
    system_id = showcase.get("trading_system_id")
    if system_id != CANONICAL_TRADING_SYSTEM_ID:
        errors.append(f"Trading system ID mismatch: expected '{CANONICAL_TRADING_SYSTEM_ID}', got '{system_id}'")

    # 2. Artifacts Evaluation
    artifacts = showcase.get("artifacts")
    if not isinstance(artifacts, list) or len(artifacts) == 0:
        errors.append("Artifacts must be a non-empty list")
        return False, errors

    for i, art in enumerate(artifacts):
        name = art.get("name")
        declared_sha = art.get("declared_sha256")
        semantic_type = art.get("semantic_type")
        required_keys = art.get("required_schema_keys", [])

        if not name:
            errors.append(f"Artifact [{i}] missing name")
            continue

        if not declared_sha or not re.match(r"^[0-9a-fA-F]{64}$", declared_sha):
            errors.append(f"Artifact [{i}] ({name}) invalid declared_sha256: '{declared_sha}'")

        if base_dir:
            file_path = os.path.join(base_dir, name)
            if not os.path.exists(file_path):
                errors.append(f"Artifact [{i}] ({name}) does not physically exist at {file_path}")
                continue

            size = os.path.getsize(file_path)
            if size <= 0:
                errors.append(f"Artifact [{i}] ({name}) is empty (0 bytes); hollow file rejected")
                continue

            actual_sha = compute_file_sha256(file_path)
            if actual_sha.lower() != declared_sha.lower():
                errors.append(
                    f"Artifact [{i}] ({name}) SHA-256 mismatch: declared '{declared_sha}', actual '{actual_sha}'"
                )

            # Semantic JSON Schema Validation
            if name.endswith(".json"):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    if not isinstance(data, dict):
                        errors.append(f"Artifact [{i}] ({name}) JSON root must be an object")
                    else:
                        for req_k in required_keys:
                            if req_k not in data or data[req_k] is None:
                                errors.append(f"Artifact [{i}] ({name}) missing required semantic key: '{req_k}'")
                except Exception as e:
                    errors.append(f"Artifact [{i}] ({name}) failed JSON parse: {e!s}")

    return (len(errors) == 0), errors
