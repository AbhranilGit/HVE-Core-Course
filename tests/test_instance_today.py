"""Tests for issue #6 (TEMP-2) instance today helper — AC-P-010–013."""

from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from pulseboard.db import connect, init_db
from pulseboard.repository import (
    get_status,
    list_statuses_for_today,
    upsert_status,
)
from pulseboard.today import (
    ENV_TZ,
    default_status_day_str,
    instance_today,
    resolve_instance_tz,
)


def test_ac_p_010_no_tz_override_matches_host_local(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """AC-P-010: without PULSEBOARD_TZ, today matches host local calendar date."""
    monkeypatch.delenv(ENV_TZ, raising=False)
    # Fixed instant; compare to conversion into resolved host-local tz
    now = datetime(2026, 8, 9, 15, 30, 0, tzinfo=timezone.utc)
    local_tz = resolve_instance_tz()
    expected = now.astimezone(local_tz).date()
    assert instance_today(now=now) == expected
    # Explicit: same as astimezone of host local from a local-aware now
    local_now = now.astimezone(local_tz)
    assert instance_today(now=local_now) == local_now.date()


def test_ac_p_011_pulseboard_tz_iana(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """AC-P-011: valid PULSEBOARD_TZ selects that zone's calendar date."""
    # Instant where UTC date and Kiritimati (UTC+14) date can differ
    now = datetime(2026, 8, 9, 12, 0, 0, tzinfo=timezone.utc)

    monkeypatch.setenv(ENV_TZ, "UTC")
    assert instance_today(now=now) == date(2026, 8, 9)
    assert instance_today(now=now) == now.astimezone(ZoneInfo("UTC")).date()

    monkeypatch.setenv(ENV_TZ, "Pacific/Kiritimati")
    kiritimati = now.astimezone(ZoneInfo("Pacific/Kiritimati")).date()
    assert instance_today(now=now) == kiritimati

    monkeypatch.setenv(ENV_TZ, "UTC")
    utc_day = instance_today(now=now)
    monkeypatch.setenv(ENV_TZ, "Pacific/Kiritimati")
    other_day = instance_today(now=now)
    # Same UTC noon: Kiritimati is typically next calendar morning vs UTC
    assert utc_day == date(2026, 8, 9)
    assert other_day == date(2026, 8, 10)
    assert utc_day != other_day


def test_invalid_pulseboard_tz_raises(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(ENV_TZ, "Not/A_Zone")
    with pytest.raises(ValueError, match="PULSEBOARD_TZ"):
        resolve_instance_tz()


def test_ac_p_012_default_status_day_matches_instance_today(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """AC-P-012: create default day string equals instance_today ISO; persists."""
    monkeypatch.setenv(ENV_TZ, "UTC")
    now = datetime(2026, 8, 9, 18, 0, 0, tzinfo=timezone.utc)
    default_day = default_status_day_str(now=now)
    assert default_day == instance_today(now=now).isoformat()
    assert default_day == "2026-08-09"

    db_path = tmp_path / "t.db"
    init_db(db_path)
    with connect(db_path) as conn:
        upsert_status(
            conn,
            display_name="Ada",
            status_day=default_day,
            doing="using default day",
        )
        loaded = get_status(conn, "Ada", default_day)
        assert loaded is not None
        assert loaded.status_day == instance_today(now=now).isoformat()


def test_ac_p_013_list_today_excludes_prior_day(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """AC-P-013: list_statuses_for_today omits prior calendar day rows."""
    monkeypatch.setenv(ENV_TZ, "UTC")
    now = datetime(2026, 8, 9, 12, 0, 0, tzinfo=timezone.utc)
    today = default_status_day_str(now=now)
    prior = "2026-08-08"
    assert today == "2026-08-09"

    db_path = tmp_path / "t.db"
    init_db(db_path)
    with connect(db_path) as conn:
        upsert_status(
            conn, display_name="Old", status_day=prior, doing="yesterday"
        )
        upsert_status(
            conn, display_name="New", status_day=today, doing="today work"
        )
        rows = list_statuses_for_today(conn, now=now)
        assert len(rows) == 1
        assert rows[0].display_name == "New"
        assert rows[0].status_day == today


def test_naive_now_treated_as_instance_wall_time(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(ENV_TZ, "UTC")
    naive = datetime(2026, 8, 9, 8, 0, 0)
    assert instance_today(now=naive) == date(2026, 8, 9)
