"""Today-status upsert service (validation + day defaulting).

HTTP and UI stay thin: this module enforces the product field rule
(at least one of doing/blocked/next non-empty after trim) and always
persists against instance today via :func:`pulseboard.today.default_status_day_str`.
Repository upsert handles uniqueness; no lock-after-standup.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime
from typing import Any

from pulseboard.models import Status
from pulseboard.repository import upsert_status
from pulseboard.today import default_status_day_str


def normalize_status_fields(
    doing: str,
    blocked: str,
    next: str,
) -> tuple[str, str, str]:
    """Return stripped doing/blocked/next (individual empties allowed)."""
    return doing.strip(), blocked.strip(), next.strip()


def validate_status_fields(
    doing: str,
    blocked: str,
    next: str,
) -> tuple[str, str, str]:
    """Normalize fields; require at least one non-empty after trim."""
    d, b, n = normalize_status_fields(doing, blocked, next)
    if not d and not b and not n:
        raise ValueError(
            "at least one of doing, blocked, or next must be non-empty"
        )
    return d, b, n


def upsert_today_status(
    conn: sqlite3.Connection,
    *,
    display_name: str,
    doing: str = "",
    blocked: str = "",
    next: str = "",
    now: datetime | None = None,
    tz: Any = None,
) -> Status:
    """Validate fields and upsert status for instance today."""
    d, b, n = validate_status_fields(doing, blocked, next)
    day = default_status_day_str(now=now, tz=tz)
    return upsert_status(
        conn,
        display_name=display_name,
        status_day=day,
        doing=d,
        blocked=b,
        next=n,
    )
