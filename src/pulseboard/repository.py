"""Status repository: upsert and list-by-day against local SQLite."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

from pulseboard.models import Status


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _require_display_name(display_name: str) -> str:
    name = display_name.strip()
    if not name:
        raise ValueError("display_name must be non-empty")
    return name


def _status_from_row(row: sqlite3.Row) -> Status:
    return Status(
        id=row["id"],
        display_name=row["display_name"],
        status_day=row["status_day"],
        doing=row["doing"],
        blocked=row["blocked"],
        next=row["next"],
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )


def upsert_status(
    conn: sqlite3.Connection,
    *,
    display_name: str,
    status_day: str,
    doing: str = "",
    blocked: str = "",
    next: str = "",
) -> Status:
    """Insert or update the status for ``(display_name, status_day)``.

    On conflict, updates doing/blocked/next and ``updated_at`` only;
    preserves original ``created_at``. Does not enforce product rules for
    empty doing/blocked/next (owned by later API validation).
    """
    name = _require_display_name(display_name)
    now = _utc_now_iso()
    conn.execute(
        """
        INSERT INTO statuses (
            display_name, status_day, doing, blocked, "next", created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(display_name, status_day) DO UPDATE SET
            doing = excluded.doing,
            blocked = excluded.blocked,
            "next" = excluded."next",
            updated_at = excluded.updated_at
        """,
        (name, status_day, doing, blocked, next, now, now),
    )
    conn.commit()
    status = get_status(conn, name, status_day)
    assert status is not None
    return status


def get_status(
    conn: sqlite3.Connection,
    display_name: str,
    status_day: str,
) -> Status | None:
    """Return one status row or None."""
    name = _require_display_name(display_name)
    cur = conn.execute(
        """
        SELECT id, display_name, status_day, doing, blocked, "next",
               created_at, updated_at
        FROM statuses
        WHERE display_name = ? AND status_day = ?
        """,
        (name, status_day),
    )
    row = cur.fetchone()
    if row is None:
        return None
    return _status_from_row(row)


def list_statuses_for_day(
    conn: sqlite3.Connection,
    status_day: str,
) -> list[Status]:
    """Return all statuses for a calendar day, ordered by display name."""
    cur = conn.execute(
        """
        SELECT id, display_name, status_day, doing, blocked, "next",
               created_at, updated_at
        FROM statuses
        WHERE status_day = ?
        ORDER BY display_name COLLATE NOCASE
        """,
        (status_day,),
    )
    return [_status_from_row(row) for row in cur.fetchall()]


def list_statuses_for_today(
    conn: sqlite3.Connection,
    *,
    now: datetime | None = None,
    tz=None,
) -> list[Status]:
    """Return statuses for instance today (see ``pulseboard.today``).

    Uses :func:`pulseboard.today.default_status_day_str` then
    :func:`list_statuses_for_day`. Optional ``now`` / ``tz`` support tests.
    """
    from pulseboard.today import default_status_day_str

    day = default_status_day_str(now=now, tz=tz)
    return list_statuses_for_day(conn, day)
