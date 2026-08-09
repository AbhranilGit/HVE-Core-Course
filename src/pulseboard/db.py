"""SQLite connection and schema initialization for PulseBoard.

Database path resolution (for operators / later runbook #8):

* Explicit ``path`` argument to :func:`resolve_db_path` / :func:`init_db` wins.
* Else environment variable ``PULSEBOARD_DB_PATH`` (filesystem path string).
* Else default relative path ``data/pulseboard.db`` (resolved against process cwd).

Persistence is a local SQLite file on the host — not a cloud database.
"""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path

# Default relative DB location when PULSEBOARD_DB_PATH is unset.
DEFAULT_DB_PATH = Path("data") / "pulseboard.db"

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS statuses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  display_name TEXT NOT NULL,
  status_day TEXT NOT NULL,
  doing TEXT NOT NULL DEFAULT '',
  blocked TEXT NOT NULL DEFAULT '',
  "next" TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  UNIQUE (display_name, status_day)
);
"""


def resolve_db_path(path: str | Path | None = None) -> Path:
    """Resolve the SQLite database file path.

    Precedence: explicit ``path`` > ``PULSEBOARD_DB_PATH`` env > default.
    """
    if path is not None:
        return Path(path)
    env_path = os.environ.get("PULSEBOARD_DB_PATH")
    if env_path:
        return Path(env_path)
    return Path(DEFAULT_DB_PATH)


def connect(path: str | Path) -> sqlite3.Connection:
    """Open a SQLite connection to ``path`` with Row factory enabled."""
    conn = sqlite3.connect(Path(path))
    conn.row_factory = sqlite3.Row
    return conn


def init_db(path: str | Path | None = None) -> Path:
    """Create parent dirs if needed, ensure schema exists, return path used.

    Safe to call multiple times (``CREATE TABLE IF NOT EXISTS``).
    """
    db_path = resolve_db_path(path)
    parent = db_path.expanduser().resolve().parent
    parent.mkdir(parents=True, exist_ok=True)

    with connect(db_path) as conn:
        conn.execute(_SCHEMA_SQL)
        conn.commit()
    return db_path
