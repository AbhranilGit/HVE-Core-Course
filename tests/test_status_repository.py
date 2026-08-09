"""Narrow persistence tests for issue #2 (TEMP-1) AC-P-001–004."""

from __future__ import annotations

from pathlib import Path

from pulseboard.db import connect, init_db, resolve_db_path
from pulseboard.repository import (
    get_status,
    list_statuses_for_day,
    upsert_status,
)


def test_ac_p_001_init_schema_usable_for_writes_and_reads(tmp_path: Path) -> None:
    """AC-P-001: configured path → init → schema usable for writes/reads."""
    db_path = tmp_path / "pulse" / "test.db"
    returned = init_db(db_path)
    assert returned == db_path

    with connect(db_path) as conn:
        status = upsert_status(
            conn,
            display_name="Ada",
            status_day="2026-08-09",
            doing="ship schema",
            blocked="",
            next="tests",
        )
        assert status.display_name == "Ada"
        assert status.doing == "ship schema"
        loaded = get_status(conn, "Ada", "2026-08-09")
        assert loaded is not None
        assert loaded.doing == "ship schema"
        listed = list_statuses_for_day(conn, "2026-08-09")
        assert len(listed) == 1


def test_ac_p_002_unique_display_name_and_day(tmp_path: Path) -> None:
    """AC-P-002: two writes same name+day → one row, latest values."""
    db_path = tmp_path / "test.db"
    init_db(db_path)

    with connect(db_path) as conn:
        first = upsert_status(
            conn,
            display_name="Ada",
            status_day="2026-08-09",
            doing="first",
            blocked="b1",
            next="n1",
        )
        second = upsert_status(
            conn,
            display_name="Ada",
            status_day="2026-08-09",
            doing="second",
            blocked="b2",
            next="n2",
        )
        assert second.doing == "second"
        assert second.blocked == "b2"
        assert second.next == "n2"
        # created_at preserved across upsert
        assert first.created_at is not None
        assert second.created_at == first.created_at
        assert second.updated_at is not None

        count = conn.execute("SELECT COUNT(*) AS c FROM statuses").fetchone()["c"]
        assert count == 1


def test_ac_p_003_data_survives_reconnect(tmp_path: Path) -> None:
    """AC-P-003: data written remains readable after new connection (restart)."""
    db_path = tmp_path / "test.db"
    init_db(db_path)

    with connect(db_path) as conn:
        upsert_status(
            conn,
            display_name="Grace",
            status_day="2026-08-09",
            doing="persist me",
        )

    with connect(db_path) as conn:
        loaded = get_status(conn, "Grace", "2026-08-09")
        assert loaded is not None
        assert loaded.doing == "persist me"


def test_ac_p_004_local_file_sqlite(tmp_path: Path) -> None:
    """AC-P-004: persistence is a local filesystem SQLite file."""
    db_path = tmp_path / "local.db"
    resolved = resolve_db_path(db_path)
    assert resolved == db_path
    assert not resolved.as_uri().startswith("http")

    init_db(db_path)
    assert db_path.is_file()


def test_list_two_names_and_excludes_other_day(tmp_path: Path) -> None:
    """Optional helper: multiple names same day; other day excluded."""
    db_path = tmp_path / "test.db"
    init_db(db_path)

    with connect(db_path) as conn:
        upsert_status(
            conn, display_name="Bea", status_day="2026-08-09", doing="b"
        )
        upsert_status(
            conn, display_name="Ada", status_day="2026-08-09", doing="a"
        )
        upsert_status(
            conn, display_name="Ada", status_day="2026-08-08", doing="old"
        )
        today = list_statuses_for_day(conn, "2026-08-09")
        assert [s.display_name for s in today] == ["Ada", "Bea"]
        assert list_statuses_for_day(conn, "2026-08-10") == []
