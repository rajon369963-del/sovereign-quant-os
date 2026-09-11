"""Durable daily-risk session state for the offline ExecutionDaemon.

This adapter binds realized daily loss to both an explicit session identity and an
immutable/versioned risk-policy fingerprint.  It intentionally does not infer
broker/exchange session semantics; callers provide the session identity/provider.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from dataclasses import dataclass


STATE_SCHEMA_VERSION = "daily_risk_session_v1"
RISK_POLICY_VERSION = "daily_loss_policy_v1"


class RiskPolicyConflict(RuntimeError):
    """Raised when persisted session state is reopened under a different policy."""


@dataclass(frozen=True)
class DailyRiskPolicy:
    session_policy_id: str
    starting_baseline: float
    daily_loss_limit_pct: float
    daily_loss_limit_amount: float
    max_account_drawdown: float
    policy_version: str = RISK_POLICY_VERSION

    def canonical_payload(self) -> dict:
        return {
            "daily_loss_limit_amount": format(float(self.daily_loss_limit_amount), ".12g"),
            "daily_loss_limit_pct": format(float(self.daily_loss_limit_pct), ".12g"),
            "max_account_drawdown": format(float(self.max_account_drawdown), ".12g"),
            "policy_version": self.policy_version,
            "session_policy_id": self.session_policy_id,
            "starting_baseline": format(float(self.starting_baseline), ".12g"),
        }

    @property
    def policy_sha256(self) -> str:
        raw = json.dumps(
            self.canonical_payload(), sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class DailyRiskState:
    session_id: str
    policy_sha256: str
    realized_loss: float
    daily_loss_limit_amount: float
    breaker_state: bool
    last_reset_id: str


class DailyRiskSessionLedger:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS daily_risk_session_state (
                    session_id TEXT PRIMARY KEY,
                    session_policy_id TEXT NOT NULL,
                    risk_policy_version TEXT NOT NULL,
                    policy_sha256 TEXT NOT NULL,
                    starting_baseline REAL NOT NULL,
                    daily_loss_limit_pct REAL NOT NULL,
                    daily_loss_limit_amount REAL NOT NULL,
                    max_account_drawdown REAL NOT NULL,
                    realized_loss REAL NOT NULL,
                    breaker_state INTEGER NOT NULL,
                    last_reset_id TEXT NOT NULL,
                    state_schema_version TEXT NOT NULL,
                    updated_at REAL NOT NULL
                )
                """
            )

    @staticmethod
    def _state_from_row(row) -> DailyRiskState:
        return DailyRiskState(
            session_id=str(row[0]),
            policy_sha256=str(row[1]),
            realized_loss=float(row[2]),
            daily_loss_limit_amount=float(row[3]),
            breaker_state=bool(row[4]),
            last_reset_id=str(row[5]),
        )

    def load_or_initialize(self, session_id: str, policy: DailyRiskPolicy) -> DailyRiskState:
        if not session_id:
            raise ValueError("session_id must be non-empty")

        now = time.time()
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("BEGIN IMMEDIATE")
            row = conn.execute(
                "SELECT session_id, policy_sha256, realized_loss, daily_loss_limit_amount, "
                "breaker_state, last_reset_id FROM daily_risk_session_state WHERE session_id = ?",
                (session_id,),
            ).fetchone()
            if row:
                if str(row[1]) != policy.policy_sha256:
                    raise RiskPolicyConflict(
                        "persisted daily-risk session policy does not match current policy"
                    )
                return self._state_from_row(row)

            reset_id = f"RESET:{session_id}:{policy.policy_sha256[:16]}"
            conn.execute(
                "INSERT INTO daily_risk_session_state "
                "(session_id, session_policy_id, risk_policy_version, policy_sha256, "
                "starting_baseline, daily_loss_limit_pct, daily_loss_limit_amount, "
                "max_account_drawdown, realized_loss, breaker_state, last_reset_id, "
                "state_schema_version, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0.0, 0, ?, ?, ?)",
                (
                    session_id,
                    policy.session_policy_id,
                    policy.policy_version,
                    policy.policy_sha256,
                    float(policy.starting_baseline),
                    float(policy.daily_loss_limit_pct),
                    float(policy.daily_loss_limit_amount),
                    float(policy.max_account_drawdown),
                    reset_id,
                    STATE_SCHEMA_VERSION,
                    now,
                ),
            )
            return DailyRiskState(
                session_id=session_id,
                policy_sha256=policy.policy_sha256,
                realized_loss=0.0,
                daily_loss_limit_amount=float(policy.daily_loss_limit_amount),
                breaker_state=False,
                last_reset_id=reset_id,
            )

    def record_realized_loss(
        self, session_id: str, loss_amount: float, policy: DailyRiskPolicy
    ) -> DailyRiskState:
        if loss_amount < 0:
            raise ValueError("loss_amount must be non-negative")

        with sqlite3.connect(self.db_path) as conn:
            conn.execute("BEGIN IMMEDIATE")
            row = conn.execute(
                "SELECT session_id, policy_sha256, realized_loss, daily_loss_limit_amount, "
                "breaker_state, last_reset_id FROM daily_risk_session_state WHERE session_id = ?",
                (session_id,),
            ).fetchone()
            if row is None:
                raise RuntimeError("session state must be initialized before recording loss")
            if str(row[1]) != policy.policy_sha256:
                raise RiskPolicyConflict(
                    "persisted daily-risk session policy does not match current policy"
                )

            new_loss = float(row[2]) + float(loss_amount)
            breaker = new_loss >= float(row[3])
            conn.execute(
                "UPDATE daily_risk_session_state SET realized_loss = ?, breaker_state = ?, updated_at = ? "
                "WHERE session_id = ? AND policy_sha256 = ?",
                (new_loss, int(breaker), time.time(), session_id, policy.policy_sha256),
            )
            return DailyRiskState(
                session_id=session_id,
                policy_sha256=policy.policy_sha256,
                realized_loss=new_loss,
                daily_loss_limit_amount=float(row[3]),
                breaker_state=breaker,
                last_reset_id=str(row[5]),
            )
