"""Tests for issue #9 (TEMP-6): today board and status form UI."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from pulseboard.app import create_app
from pulseboard.db import connect, init_db
from pulseboard.repository import upsert_status
from pulseboard.today import default_status_day_str


def test_ac_p_050_ui_can_set_name_enter_fields_and_submit(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "ui.db")
    with TestClient(app) as client:
        page = client.get("/")
        assert page.status_code == 200
        body = page.text
        assert 'action="/ui/identity"' in body
        assert 'action="/ui/status"' in body
        assert 'name="display_name"' in body
        assert 'name="doing"' in body
        assert 'name="blocked"' in body
        assert 'name="next"' in body

        set_name = client.post(
            "/ui/identity",
            data={"display_name": "Ada"},
            follow_redirects=False,
        )
        assert set_name.status_code == 303

        submit = client.post(
            "/ui/status",
            data={"doing": "ship", "blocked": "", "next": "review"},
            follow_redirects=False,
        )
        assert submit.status_code == 303


def test_ac_p_051_successful_save_visible_on_today_board(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "ui.db")
    with TestClient(app) as client:
        client.post(
            "/ui/identity",
            data={"display_name": "Ada"},
            follow_redirects=True,
        )
        save = client.post(
            "/ui/status",
            data={"doing": "Finish plan", "blocked": "", "next": "Demo"},
            follow_redirects=True,
        )

    assert save.status_code == 200
    assert "Ada" in save.text
    assert "Finish plan" in save.text
    assert "Demo" in save.text


def test_ac_p_052_empty_board_has_clear_empty_state(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "ui.db")
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert "No statuses posted yet for today." in response.text


def test_ac_p_053_multiple_rows_show_required_columns(tmp_path: Path) -> None:
    db_path = tmp_path / "ui.db"
    init_db(db_path)
    today = default_status_day_str()
    with connect(db_path) as conn:
        upsert_status(
            conn,
            display_name="Ada",
            status_day=today,
            doing="A-doing",
            blocked="A-blocked",
            next="A-next",
        )
        upsert_status(
            conn,
            display_name="Bea",
            status_day=today,
            doing="B-doing",
            blocked="",
            next="B-next",
        )

    app = create_app(db_path=db_path)
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    body = response.text
    assert "Display name" in body
    assert "Doing" in body
    assert "Blocked" in body
    assert "Next" in body
    assert "Ada" in body and "A-doing" in body and "A-blocked" in body and "A-next" in body
    assert "Bea" in body and "B-doing" in body and "B-next" in body


def test_ac_p_054_absence_of_sso_lock_workflow_notifications(tmp_path: Path) -> None:
    app = create_app(db_path=tmp_path / "ui.db")
    with TestClient(app) as client:
        page = client.get("/")

    assert page.status_code == 200
    text = page.text.lower()
    for forbidden in (
        "oauth",
        "sso",
        "lock-after-standup",
        "lock_after",
        "standup_lock",
        "workflow",
        "notification",
    ):
        assert forbidden not in text

    paths = [(getattr(route, "path", "") or "").lower() for route in app.routes]
    for forbidden_path in (
        "/oauth",
        "/oauth2",
        "/sso",
        "/lock",
        "/notifications",
    ):
        assert forbidden_path not in paths
