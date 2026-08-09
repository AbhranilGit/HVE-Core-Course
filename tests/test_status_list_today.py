"""Tests for issue #3 (TEMP-5): list statuses for today board (AC-P-040..045)."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from fastapi.testclient import TestClient

from pulseboard.app import create_app
from pulseboard.db import connect, init_db
from pulseboard.repository import upsert_status
from pulseboard.today import default_status_day_str


def _today_and_yesterday() -> tuple[str, str]:
    today = default_status_day_str()
    yesterday = (date.fromisoformat(today) - timedelta(days=1)).isoformat()
    return today, yesterday


def _post_identity(client: TestClient, name: str) -> None:
    response = client.post(
        "/identity",
        data={"display_name": name},
        follow_redirects=True,
    )
    assert response.status_code == 200


def _post_status(client: TestClient, doing: str, blocked: str, next_: str) -> None:
    response = client.post(
        "/status",
        data={"doing": doing, "blocked": blocked, "next": next_},
    )
    assert response.status_code == 200


def test_ac_p_040_empty_today_list_returns_200_and_empty(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "list.db")
    with TestClient(app) as client:
        response = client.get("/statuses/today")

    assert response.status_code == 200
    assert response.json() == []


def test_ac_p_041_each_item_includes_required_fields(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "list.db")
    with TestClient(app) as client:
        _post_identity(client, "Ada")
        _post_status(client, "shipping", "", "next")
        response = client.get("/statuses/today")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    item = items[0]
    for key in ("display_name", "doing", "blocked", "next"):
        assert key in item


def test_ac_p_042_prior_day_rows_are_excluded(tmp_path: Path) -> None:
    db_path = tmp_path / "list.db"
    today, yesterday = _today_and_yesterday()
    init_db(db_path)
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
        response = client.get("/statuses/today")

    assert response.status_code == 200
    items = response.json()
    assert items == []
    assert all(item["status_day"] == today for item in items)


def test_ac_p_043_distinct_names_remain_distinct_rows(tmp_path: Path) -> None:
    db_path = tmp_path / "list.db"
    today = default_status_day_str()
    init_db(db_path)
    with connect(db_path) as conn:
        upsert_status(
            conn,
            display_name="Ada",
            status_day=today,
            doing="d1",
            blocked="",
            next="",
        )
        upsert_status(
            conn,
            display_name="Bea",
            status_day=today,
            doing="d2",
            blocked="",
            next="",
        )

    app = create_app(db_path=db_path)
    with TestClient(app) as client:
        response = client.get("/statuses/today")

    assert response.status_code == 200
    items = response.json()
    names = [item["display_name"] for item in items]
    assert "Ada" in names
    assert "Bea" in names
    assert len(items) == 2


def test_ac_p_044_blocked_text_present_for_scan(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "list.db")
    with TestClient(app) as client:
        _post_identity(client, "Ada")
        _post_status(client, "work", "waiting on CI", "later")
        response = client.get("/statuses/today")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["blocked"] == "waiting on CI"


def test_ac_p_045_empty_blocked_row_still_appears(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "list.db")
    with TestClient(app) as client:
        _post_identity(client, "Ada")
        _post_status(client, "work", "", "next")
        response = client.get("/statuses/today")

    assert response.status_code == 200
    items = response.json()
    assert len(items) == 1
    assert items[0]["display_name"] == "Ada"
    assert items[0]["doing"] == "work"
    assert items[0]["blocked"] == ""
    assert items[0]["next"] == "next"
