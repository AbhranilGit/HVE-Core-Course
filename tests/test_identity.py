"""Tests for issue #4 (TEMP-3) display name identity — AC-P-020–023."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from pulseboard.app import create_app
from pulseboard.identity import (
    COOKIE_DISPLAY_NAME,
    normalize_display_name,
)


@pytest.fixture
def client(tmp_path: Path):
    with TestClient(create_app(db_path=tmp_path / "id.db")) as test_client:
        yield test_client


def test_normalize_display_name_strips_and_rejects_blank() -> None:
    assert normalize_display_name("  Ada  ") == "Ada"
    with pytest.raises(ValueError, match="non-empty"):
        normalize_display_name("")
    with pytest.raises(ValueError, match="non-empty"):
        normalize_display_name("   ")


def test_ac_p_020_set_name_cookie_and_subsequent_use(client: TestClient) -> None:
    """AC-P-020: non-empty name accepted; cookie used on later status action."""
    response = client.post(
        "/identity",
        data={"display_name": "Ada"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers.get("location") == "/identity"
    assert COOKIE_DISPLAY_NAME in response.cookies
    assert response.cookies[COOKIE_DISPLAY_NAME] == "Ada"

    # Client jar retains cookie for subsequent requests
    assert client.cookies.get(COOKIE_DISPLAY_NAME) == "Ada"

    follow = client.get("/identity")
    assert follow.status_code == 200
    assert "Ada" in follow.text

    status_resp = client.post(
        "/status",
        data={"doing": "via cookie", "blocked": "", "next": ""},
    )
    assert status_resp.status_code == 200
    body = status_resp.json()
    assert body["display_name"] == "Ada"
    assert body["doing"] == "via cookie"
    assert "not_implemented" not in body


def test_ac_p_020_change_name_overwrites_cookie(client: TestClient) -> None:
    client.post("/identity", data={"display_name": "Ada"}, follow_redirects=True)
    assert client.cookies.get(COOKIE_DISPLAY_NAME) == "Ada"

    response = client.post(
        "/identity",
        data={"display_name": "Bea"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.cookies.get(COOKIE_DISPLAY_NAME) == "Bea"
    assert client.cookies.get(COOKIE_DISPLAY_NAME) == "Bea"

    page = client.get("/identity")
    assert "Bea" in page.text
    status_resp = client.post(
        "/status",
        data={"doing": "bea work", "blocked": "", "next": ""},
    )
    assert status_resp.status_code == 200
    assert status_resp.json()["display_name"] == "Bea"


@pytest.mark.parametrize("raw", ["", "   "])
def test_ac_p_021_reject_blank_name(client: TestClient, raw: str) -> None:
    """AC-P-021: empty/whitespace rejected; no blank cookie attribution."""
    response = client.post(
        "/identity",
        data={"display_name": raw},
        follow_redirects=False,
    )
    assert response.status_code == 400
    assert "non-empty" in response.text.lower() or "must be" in response.text.lower()
    # Must not set cookie to blank
    set_cookie = response.headers.get("set-cookie", "")
    if COOKIE_DISPLAY_NAME in set_cookie.lower() or COOKIE_DISPLAY_NAME in set_cookie:
        # If a Set-Cookie appears, value must not be empty name
        assert re.search(rf"{COOKIE_DISPLAY_NAME}=([^;]*)", set_cookie)
        match = re.search(rf"{re.escape(COOKIE_DISPLAY_NAME)}=([^;]*)", set_cookie)
        assert match is not None
        assert match.group(1).strip() not in ("", '""')
    assert client.cookies.get(COOKIE_DISPLAY_NAME) in (None, "")


def test_ac_p_022_no_sso_oauth_routes_or_deps(client: TestClient) -> None:
    """AC-P-022: no SSO/OAuth sign-in path in MVP build surface."""
    app = create_app()
    paths = [
        (getattr(route, "path", "") or "").lower()
        for route in app.routes
    ]
    # Product identity paths only; ban SSO-style app routes (not docs chrome).
    banned_exact = {
        "/oauth",
        "/oauth2",
        "/sso",
        "/openid",
        "/login",
        "/auth/login",
        "/docs/oauth2-redirect",
    }
    for path in paths:
        assert path not in banned_exact, f"unexpected SSO-style path: {path}"
        assert not path.startswith("/oauth"), f"unexpected oauth path: {path}"
        assert not path.startswith("/sso"), f"unexpected sso path: {path}"

    # Identity surface present; status stub present; no password login form route.
    assert "/identity" in paths
    assert "/status" in paths

    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"
    text = pyproject.read_text(encoding="utf-8").lower()
    for banned in ("authlib", "python-jose", "python-social-auth", "auth0", "okta"):
        assert banned not in text


def test_ac_p_023_create_blocked_without_identity(client: TestClient) -> None:
    """AC-P-023: create attempt without identity → clear failure."""
    response = client.post("/status")
    assert response.status_code == 400
    detail = response.json()["detail"]
    assert "display name" in detail.lower()
    assert "required" in detail.lower()

    client.post("/identity", data={"display_name": "Ada"}, follow_redirects=True)
    ok = client.post(
        "/status",
        data={"doing": "ok", "blocked": "", "next": ""},
    )
    assert ok.status_code == 200
    assert ok.json()["display_name"] == "Ada"
    assert ok.json()["doing"] == "ok"
