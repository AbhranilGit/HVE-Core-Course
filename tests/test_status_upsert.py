"""Tests for issue #5 (TEMP-4) upsert today status — AC-P-030–034."""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from pulseboard.app import create_app
from pulseboard.db import connect
from pulseboard.identity import COOKIE_DISPLAY_NAME
from pulseboard.repository import get_status, list_statuses_for_day
from pulseboard.status_service import (
    normalize_status_fields,
    validate_status_fields,
)
from pulseboard.today import default_status_day_str


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "pulseboard.db"


@pytest.fixture
def client(db_path: Path):
    with TestClient(create_app(db_path=db_path)) as test_client:
        yield test_client


def _set_name(client: TestClient, name: str = "Ada") -> None:
    client.post(
        "/identity",
        data={"display_name": name},
        follow_redirects=True,
    )
    assert client.cookies.get(COOKIE_DISPLAY_NAME) == name


def test_normalize_and_validate_status_fields() -> None:
    assert normalize_status_fields(" a ", " b ", " c ") == ("a", "b", "c")
    assert validate_status_fields("x", "", "") == ("x", "", "")
    with pytest.raises(ValueError, match="at least one"):
        validate_status_fields("", "  ", "")


def test_ac_p_030_create_today_status(
    client: TestClient, db_path: Path
) -> None:
    """AC-P-030: valid name + ≥1 field → today status under display name."""
    _set_name(client, "Ada")
    response = client.post(
        "/status",
        data={"doing": "ship slice", "blocked": "", "next": ""},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["display_name"] == "Ada"
    assert body["doing"] == "ship slice"
    assert "not_implemented" not in body
    today = default_status_day_str()
    assert body["status_day"] == today

    with connect(db_path) as conn:
        row = get_status(conn, "Ada", today)
        assert row is not None
        assert row.doing == "ship slice"
        assert row.display_name == "Ada"


def test_ac_p_031_day_is_instance_today(
    client: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    """AC-P-031: create without other day → instance today."""
    monkeypatch.setenv("PULSEBOARD_TZ", "UTC")
    _set_name(client, "Ada")
    response = client.post("/status", data={"doing": "work", "blocked": "", "next": ""})
    assert response.status_code == 200
    assert response.json()["status_day"] == default_status_day_str()


def test_ac_p_032_second_submit_one_row(
    client: TestClient, db_path: Path
) -> None:
    """AC-P-032: second submit updates single today row."""
    _set_name(client, "Ada")
    r1 = client.post(
        "/status",
        data={"doing": "first", "blocked": "old", "next": "n1"},
    )
    assert r1.status_code == 200
    r2 = client.post(
        "/status",
        data={"doing": "second", "blocked": "", "next": "n2"},
    )
    assert r2.status_code == 200
    body = r2.json()
    assert body["doing"] == "second"
    assert body["blocked"] == ""
    assert body["next"] == "n2"
    today = body["status_day"]
    with connect(db_path) as conn:
        rows = list_statuses_for_day(conn, today)
        assert len(rows) == 1
        assert rows[0].doing == "second"
        assert rows[0].blocked == ""
        assert rows[0].next == "n2"


@pytest.mark.parametrize(
    "payload",
    [
        {"doing": "", "blocked": "", "next": ""},
        {"doing": "  ", "blocked": "\t", "next": "  "},
    ],
)
def test_ac_p_033_reject_all_empty(
    client: TestClient, db_path: Path, payload: dict[str, str]
) -> None:
    """AC-P-033: all empty/whitespace rejected; no blank row."""
    _set_name(client, "Ada")
    response = client.post("/status", data=payload)
    assert response.status_code == 400
    detail = response.json()["detail"]
    assert "at least one" in detail.lower() or "non-empty" in detail.lower()
    today = default_status_day_str()
    with connect(db_path) as conn:
        assert get_status(conn, "Ada", today) is None


def test_ac_p_033_reject_all_empty_leaves_prior_unchanged(
    client: TestClient, db_path: Path
) -> None:
    _set_name(client, "Ada")
    ok = client.post(
        "/status",
        data={"doing": "keep", "blocked": "", "next": ""},
    )
    assert ok.status_code == 200
    today = ok.json()["status_day"]
    bad = client.post(
        "/status",
        data={"doing": "", "blocked": "", "next": ""},
    )
    assert bad.status_code == 400
    with connect(db_path) as conn:
        row = get_status(conn, "Ada", today)
        assert row is not None
        assert row.doing == "keep"


def test_ac_p_034_no_lock_after_standup_control(client: TestClient) -> None:
    """AC-P-034: no lock-after-standup control on MVP surface."""
    app = create_app()
    paths = [(getattr(r, "path", "") or "").lower() for r in app.routes]
    joined = " ".join(paths)
    for banned in ("/lock", "standup_lock", "lock-after", "lock_after"):
        assert banned not in joined

    # POST /status accepts only identity + three fields (no lock form field)
    from pathlib import Path as P
    import inspect

    from pulseboard import app as app_mod

    src = inspect.getsource(app_mod.post_status) if hasattr(app_mod, "post_status") else ""
    # Factory-local route: inspect create_app source instead
    app_src = (P(__file__).resolve().parents[1] / "src/pulseboard/app.py").read_text(
        encoding="utf-8"
    )
    # Avoid matching "blocked" — check explicit lock controls only
    lowered = app_src.lower()
    assert "standup_lock" not in lowered
    assert "lock_after" not in lowered
    assert "lock-after" not in lowered
    assert 'name="lock"' not in lowered
    assert "form(default" in lowered or "Form(default" in app_src
    # status endpoint form params are doing/blocked/next only
    assert "doing: str = Form" in app_src
    assert "blocked: str = Form" in app_src
    assert 'next: str = Form' in app_src
    assert "lock: str = Form" not in app_src


def test_status_requires_identity(client: TestClient) -> None:
    response = client.post("/status", data={"doing": "x"})
    assert response.status_code == 400
    assert "display name" in response.json()["detail"].lower()
