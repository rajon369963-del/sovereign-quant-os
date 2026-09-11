"""Durable collision-safe order intent identity binding.

Wall-clock time is metadata, not semantic identity. This module binds an explicit
intent/effect key to a deterministic canonical payload digest and stable order ID.
Exact retry reuses the same identity; mutated-payload reuse fails closed.
"""

import hashlib
import sqlite3
import uuid
from dataclasses import dataclass
from typing import Optional


class IntentIdentityConflict(ValueError):
    """Raised when one idempotency identity is reused for a different intent."""


@dataclass(frozen=True)
class IntentBinding:
    intent_key: str
    payload_sha256: str
    order_id: str
    created_new: bool


def canonical_intent_payload(
    *,
    strategy: str,
    side: str,
    symbol: str,
    quantity: float,
    entry_price: float,
    stop_loss: float,
    take_profit: float,
    schema_version: str = "order_intent_v1",
) -> str:
    """Return deterministic canonical semantic payload text."""
    parts = [
        schema_version,
        strategy,
        side,
        symbol,
        format(float(quantity), ".12g"),
        format(float(entry_price), ".12g"),
        format(float(stop_loss), ".12g"),
        format(float(take_profit), ".12g"),
    ]
    return "|".join(parts)


def canonical_intent_sha256(**kwargs) -> str:
    payload = canonical_intent_payload(**kwargs)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class OrderIntentIdentityLedger:
    """SQLite-backed binding from semantic intent identity to one stable order ID."""

    def __init__(self, db_path: str):
        self.db_path = db_path
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS order_intent_bindings (
                    intent_key TEXT PRIMARY KEY,
                    payload_sha256 TEXT NOT NULL,
                    order_id TEXT NOT NULL UNIQUE,
                    created_at REAL NOT NULL
                )
            """)

    @staticmethod
    def _stable_order_id(strategy: str, intent_key: str) -> str:
        digest = hashlib.sha256(intent_key.encode("utf-8")).hexdigest()[:20]
        return f"ORD_{strategy[:3]}_{digest}"

    def bind(
        self,
        *,
        strategy: str,
        payload_sha256: str,
        created_at: float,
        intent_id: Optional[str] = None,
        effect_id: Optional[str] = None,
    ) -> IntentBinding:
        """Bind or replay one semantic intent.

        Explicit intent/effect identity is replayable. Legacy callers that provide
        neither receive a UUID-backed identity, preserving ordinary dispatch while
        eliminating same-millisecond collision risk.
        """
        if intent_id and effect_id:
            intent_key = f"intent:{intent_id}|effect:{effect_id}"
        elif intent_id:
            intent_key = f"intent:{intent_id}"
        elif effect_id:
            intent_key = f"effect:{effect_id}"
        else:
            intent_key = f"generated:{uuid.uuid4().hex}"

        order_id = self._stable_order_id(strategy, intent_key)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("BEGIN IMMEDIATE")
            existing = conn.execute(
                "SELECT payload_sha256, order_id FROM order_intent_bindings WHERE intent_key = ?",
                (intent_key,),
            ).fetchone()
            if existing:
                existing_payload, existing_order_id = existing
                if existing_payload != payload_sha256:
                    raise IntentIdentityConflict(
                        "idempotency identity reused with mutated canonical intent payload"
                    )
                return IntentBinding(intent_key, payload_sha256, existing_order_id, False)

            conn.execute(
                "INSERT INTO order_intent_bindings (intent_key, payload_sha256, order_id, created_at) "
                "VALUES (?, ?, ?, ?)",
                (intent_key, payload_sha256, order_id, float(created_at)),
            )
        return IntentBinding(intent_key, payload_sha256, order_id, True)
