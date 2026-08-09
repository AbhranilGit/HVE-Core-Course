"""PulseBoard FastAPI application (identity + today status upsert).

Local run (full operator runbook is issue #8)::

    uvicorn pulseboard.app:app --reload

* ``GET/POST /identity`` — display name cookie (issue #4)
* ``POST /status`` — upsert today's doing/blocked/next (issue #5)
* Board list HTTP and HTMX UI are later issues (#3, #9)
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, AsyncIterator

from fastapi import FastAPI, Form, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

from pulseboard.db import connect, init_db, resolve_db_path
from pulseboard.identity import (
    normalize_display_name,
    read_display_name,
    require_display_name,
    set_display_name_cookie,
)
from pulseboard.models import Status
from pulseboard.repository import list_statuses_for_today
from pulseboard.status_service import upsert_today_status


def _identity_page(current: str | None, error: str | None = None) -> str:
    current_block = (
        f"<p>Current display name: <strong>{_escape(current)}</strong></p>"
        if current
        else "<p>No display name set.</p>"
    )
    error_block = (
        f'<p style="color:darkred">{_escape(error)}</p>' if error else ""
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>PulseBoard — display name</title>
</head>
<body>
  <h1>PulseBoard display name</h1>
  {current_block}
  {error_block}
  <form method="post" action="/identity">
    <label for="display_name">Display name</label>
    <input id="display_name" name="display_name" type="text"
           value="{_escape(current or '')}" autocomplete="nickname"/>
    <button type="submit">Save</button>
  </form>
  <p>No SSO or OAuth. Local display name only.</p>
</body>
</html>
"""


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _status_to_dict(row: Status) -> dict[str, Any]:
    return {
        "id": row.id,
        "display_name": row.display_name,
        "status_day": row.status_day,
        "doing": row.doing,
        "blocked": row.blocked,
        "next": row.next,
        "created_at": row.created_at,
        "updated_at": row.updated_at,
    }


def _board_rows_html(rows: list[Status]) -> str:
        if not rows:
                return "<p id=\"empty-board\">No statuses posted yet for today.</p>"

        lines = [
                "<table id=\"today-board\">",
                "  <thead><tr><th>Display name</th><th>Doing</th><th>Blocked</th><th>Next</th></tr></thead>",
                "  <tbody>",
        ]
        for row in rows:
                lines.append(
                        "    <tr>"
                        f"<td>{_escape(row.display_name)}</td>"
                        f"<td>{_escape(row.doing)}</td>"
                        f"<td>{_escape(row.blocked)}</td>"
                        f"<td>{_escape(row.next)}</td>"
                        "</tr>"
                )
        lines.extend(["  </tbody>", "</table>"])
        return "\n".join(lines)


def _board_page(
        current: str | None,
        rows: list[Status],
        *,
        status_error: str | None = None,
        identity_error: str | None = None,
) -> str:
        identity_error_block = (
                f'<p role="alert" style="color:darkred">{_escape(identity_error)}</p>'
                if identity_error
                else ""
        )
        status_error_block = (
                f'<p role="alert" style="color:darkred">{_escape(status_error)}</p>'
                if status_error
                else ""
        )
        current_name = _escape(current or "")
        current_line = (
                f"<p>Current display name: <strong>{current_name}</strong></p>"
                if current
                else "<p>No display name set.</p>"
        )
        board_rows = _board_rows_html(rows)
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>PulseBoard</title>
</head>
<body>
    <h1>PulseBoard today board</h1>

    <section id="identity-section">
        <h2>Display name</h2>
        {current_line}
        {identity_error_block}
        <form method="post" action="/ui/identity">
            <label for="display_name">Display name</label>
            <input id="display_name" name="display_name" type="text" value="{current_name}" autocomplete="nickname"/>
            <button type="submit">Save display name</button>
        </form>
    </section>

    <section id="status-section">
        <h2>Today's status</h2>
        {status_error_block}
        <form method="post" action="/ui/status" hx-post="/ui/status" hx-target="#board-section" hx-swap="outerHTML">
            <label for="doing">Doing</label>
            <input id="doing" name="doing" type="text"/>
            <label for="blocked">Blocked</label>
            <input id="blocked" name="blocked" type="text"/>
            <label for="next">Next</label>
            <input id="next" name="next" type="text"/>
            <button type="submit">Save status</button>
        </form>
    </section>

    <section id="board-section">
        <h2>Today board</h2>
        {board_rows}
    </section>
</body>
</html>
"""


def create_app(*, db_path: str | Path | None = None) -> FastAPI:
    """Application factory for tests and ASGI servers.

    Parameters
    ----------
    db_path:
        SQLite file path. If omitted, uses :func:`resolve_db_path` (env/default).
    """
    resolved = resolve_db_path(db_path)
    # Ensure schema exists for TestClient and import-time app; lifespan repeats (IF NOT EXISTS).
    init_db(resolved)

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncIterator[None]:
        init_db(application.state.db_path)
        yield

    application = FastAPI(
        title="PulseBoard",
        version="0.1.0",
        lifespan=lifespan,
        # No product SSO; also omit Swagger OAuth2 redirect helper route.
        swagger_ui_oauth2_redirect_url=None,
    )
    application.state.db_path = resolved

    @application.get("/identity", response_class=HTMLResponse)
    def get_identity(request: Request) -> HTMLResponse:
        return HTMLResponse(_identity_page(read_display_name(request)))

    @application.get("/", response_class=HTMLResponse)
    def get_board(request: Request) -> HTMLResponse:
        conn = connect(request.app.state.db_path)
        try:
            rows = list_statuses_for_today(conn)
        finally:
            conn.close()
        return HTMLResponse(_board_page(read_display_name(request), rows))

    @application.post("/identity")
    def post_identity(
        display_name: str = Form(default=""),
    ) -> Response:
        try:
            name = normalize_display_name(display_name)
        except ValueError:
            return HTMLResponse(
                _identity_page(None, error="Display name must be non-empty."),
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        redirect = RedirectResponse(
            url="/identity",
            status_code=status.HTTP_303_SEE_OTHER,
        )
        set_display_name_cookie(redirect, name)
        return redirect

    @application.post("/ui/identity")
    def post_ui_identity(
        request: Request,
        display_name: str = Form(default=""),
    ) -> Response:
        try:
            name = normalize_display_name(display_name)
        except ValueError:
            conn = connect(request.app.state.db_path)
            try:
                rows = list_statuses_for_today(conn)
            finally:
                conn.close()
            return HTMLResponse(
                _board_page(
                    read_display_name(request),
                    rows,
                    identity_error="Display name must be non-empty.",
                ),
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        redirect = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
        set_display_name_cookie(redirect, name)
        return redirect

    @application.post("/status")
    def post_status(
        request: Request,
        doing: str = Form(default=""),
        blocked: str = Form(default=""),
        next: str = Form(default=""),
    ) -> JSONResponse:
        """Upsert today's status for the cookie display name."""
        name = require_display_name(request)
        conn = connect(request.app.state.db_path)
        try:
            try:
                row = upsert_today_status(
                    conn,
                    display_name=name,
                    doing=doing,
                    blocked=blocked,
                    next=next,
                )
            except ValueError as exc:
                return JSONResponse(
                    {"detail": str(exc)},
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
        finally:
            conn.close()
        return JSONResponse(_status_to_dict(row))

    @application.post("/ui/status")
    def post_ui_status(
        request: Request,
        doing: str = Form(default=""),
        blocked: str = Form(default=""),
        next: str = Form(default=""),
    ) -> Response:
        try:
            name = require_display_name(request)
        except HTTPException as exc:
            conn = connect(request.app.state.db_path)
            try:
                rows = list_statuses_for_today(conn)
            finally:
                conn.close()
            return HTMLResponse(
                _board_page(read_display_name(request), rows, status_error=str(exc)),
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        conn = connect(request.app.state.db_path)
        try:
            try:
                upsert_today_status(
                    conn,
                    display_name=name,
                    doing=doing,
                    blocked=blocked,
                    next=next,
                )
            except ValueError as exc:
                rows = list_statuses_for_today(conn)
                return HTMLResponse(
                    _board_page(read_display_name(request), rows, status_error=str(exc)),
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
        finally:
            conn.close()
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    @application.get("/statuses/today")
    def get_statuses_today(request: Request) -> JSONResponse:
        """List statuses for instance today for the facilitator board."""
        conn = connect(request.app.state.db_path)
        try:
            rows = list_statuses_for_today(conn)
        finally:
            conn.close()
        return JSONResponse([_status_to_dict(row) for row in rows])

    return application


app = create_app()
