"""Tests for issue #10 (TEMP-7): release-bar create/list evidence (AC-P-060..063)."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from fastapi.testclient import TestClient

from pulseboard.app import create_app
from pulseboard.db import connect, init_db
from pulseboard.repository import upsert_status
from pulseboard.today import default_status_day_str


def _set_identity(client: TestClient, display_name: str = "Ada") -> None:
    response = client.post(
        "/identity",
        data={"display_name": display_name},
        follow_redirects=True,
    )
    assert response.status_code == 200


def _post_status(
    client: TestClient,
    *,
    doing: str,
    blocked: str = "",
    next_: str = "",
) -> None:
    response = client.post(
        "/status",
        data={"doing": doing, "blocked": blocked, "next": next_},
    )
    assert response.status_code == 200


def test_ac_p_060_create_and_list_release_bar_smoke(tmp_path: Path) -> None:
    """AC-P-060: create/list behavior is exercised in automated tests and passes."""
    app = create_app(db_path=tmp_path / "release.db")
    with TestClient(app) as client:
        _set_identity(client, "Ada")
        _post_status(client, doing="ship", blocked="", next_="review")
        listed = client.get("/statuses/today")

    assert listed.status_code == 200
    rows = listed.json()
    assert isinstance(rows, list)
    assert len(rows) == 1


def test_ac_p_061_create_then_list_returns_today_values(tmp_path: Path) -> None:
    """AC-P-061: create then list returns stored values under display name."""
    app = create_app(db_path=tmp_path / "release.db")
    with TestClient(app) as client:
        _set_identity(client, "Ada")
        _post_status(client, doing="Finish PR", blocked="", next_="Demo")
        listed = client.get("/statuses/today")

    assert listed.status_code == 200
    rows = listed.json()
    assert len(rows) == 1
    assert rows[0]["display_name"] == "Ada"
    assert rows[0]["doing"] == "Finish PR"
    assert rows[0]["blocked"] == ""
    assert rows[0]["next"] == "Demo"


def test_ac_p_062_same_name_twice_has_one_latest_row(tmp_path: Path) -> None:
    """AC-P-062: same-name same-day upsert keeps one row with latest values."""
    app = create_app(db_path=tmp_path / "release.db")
    with TestClient(app) as client:
        _set_identity(client, "Ada")
        _post_status(client, doing="first", blocked="old", next_="n1")
        _post_status(client, doing="second", blocked="", next_="n2")
        listed = client.get("/statuses/today")

    assert listed.status_code == 200
    rows = listed.json()
    assert len(rows) == 1
    assert rows[0]["display_name"] == "Ada"
    assert rows[0]["doing"] == "second"
    assert rows[0]["blocked"] == ""
    assert rows[0]["next"] == "n2"


def test_ac_p_063_prior_day_fixture_excluded_from_today_list(tmp_path: Path) -> None:
    """AC-P-063: prior-day rows are excluded from default today list."""
    db_path = tmp_path / "release.db"
    init_db(db_path)
    today = default_status_day_str()
    yesterday = (date.fromisoformat(today) - timedelta(days=1)).isoformat()
    with connect(db_path) as conn:
        upsert_status(
            conn,
            display_name="Ada",
            status_day=yesterday,
            doing="old",
            blocked="",
            next="",
        )

    app = create_app(db_path=db_path)
    with TestClient(app) as client:
        listed = client.get("/statuses/today")

    assert listed.status_code == 200
    assert listed.json() == []
