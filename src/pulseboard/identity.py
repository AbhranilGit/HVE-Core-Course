"""Display-name identity helpers and cookie continuity for PulseBoard.

Identity is a non-empty display name stored in an HTTP cookie after the user
submits it (ADR local-identity-display-name). This is attribution on a trusted
local instance — not authentication. No SSO, OAuth, or passwords.

Cookie: ``pulseboard_display_name`` (session, HttpOnly, SameSite=lax, path=/).
"""

from __future__ import annotations

from fastapi import HTTPException, Request, Response

COOKIE_DISPLAY_NAME = "pulseboard_display_name"

_MISSING_IDENTITY_DETAIL = (
    "Display name required. Set your display name before creating a status."
)


def normalize_display_name(raw: str) -> str:
    """Return stripped display name or raise ``ValueError`` if blank."""
    name = raw.strip()
    if not name:
        raise ValueError("display name must be non-empty")
    return name


def display_name_from_cookie_value(value: str | None) -> str | None:
    """Parse optional cookie value; blank or invalid → ``None``."""
    if value is None:
        return None
    try:
        return normalize_display_name(value)
    except ValueError:
        return None


def read_display_name(request: Request) -> str | None:
    """Return current display name from cookie, or ``None`` if unset."""
    return display_name_from_cookie_value(
        request.cookies.get(COOKIE_DISPLAY_NAME)
    )


def require_display_name(request: Request) -> str:
    """Return display name or raise HTTP 400 when identity is missing."""
    name = read_display_name(request)
    if name is None:
        raise HTTPException(status_code=400, detail=_MISSING_IDENTITY_DETAIL)
    return name


def set_display_name_cookie(response: Response, name: str) -> None:
    """Set session cookie with a validated (non-empty) display name."""
    normalized = normalize_display_name(name)
    response.set_cookie(
        key=COOKIE_DISPLAY_NAME,
        value=normalized,
        httponly=True,
        samesite="lax",
        path="/",
        secure=False,
    )
