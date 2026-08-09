---
title: "PulseBoard local runbook"
description: Canonical operator start path for running PulseBoard locally and reaching today's board
author: PulseBoard
ms.date: 2026-08-09
ms.topic: how-to
keywords:
  - pulseboard
  - runbook
  - operations
  - local-first
  - fastapi
estimated_reading_time: 9
---

## Purpose

This runbook is the canonical start path for operating PulseBoard locally.

PulseBoard is local-first for MVP: one machine, one app process, one local SQLite file. No cloud database is required.

## Prerequisites

* Python 3.12 or newer
* Recommended environment: conda environment `hve-env`

Optional environment activation:

```bash
conda activate hve-env
python --version
```

Expected Python version is `3.12.x` or newer.

## Install dependencies

From the repository root:

```bash
python -m pip install -e ".[dev]"
```

This installs runtime dependencies (`fastapi`, `uvicorn`, `python-multipart`) and test tooling (`pytest`, `httpx`) declared in [pyproject.toml](../../../pyproject.toml).

## Start the app

From the repository root:

```bash
uvicorn pulseboard.app:app --reload
```

Keep this terminal running while you use the app.

## Open the board UI

Open this URL in a browser:

<http://127.0.0.1:8000/>

This is the today board route (`/`).

Related routes used by MVP:

* `GET /` today board HTML
* `GET /identity` and `POST /identity` display-name setup
* `POST /status` API upsert for today
* `GET /statuses/today` list today rows as JSON
* `POST /ui/identity` and `POST /ui/status` UI form handlers

## Data location and DB path behavior

PulseBoard persists data in a local SQLite file.

DB path precedence is:

1. Explicit path argument (when app initialization is called with a path)
2. Environment variable `PULSEBOARD_DB_PATH`
3. Default `data/pulseboard.db` (relative to current working directory)

Example override:

```bash
export PULSEBOARD_DB_PATH="$PWD/data/pulseboard.db"
```

If you start from a different working directory and do not set `PULSEBOARD_DB_PATH`, the default `data/pulseboard.db` will be created relative to that directory.

## Today boundary and timezone behavior

PulseBoard uses instance-level calendar today.

* Default timezone: host local timezone of the machine running the process
* Optional override: `PULSEBOARD_TZ` using a valid IANA timezone name
* If `PULSEBOARD_TZ` is invalid, startup/date resolution fails fast

Example override:

```bash
export PULSEBOARD_TZ="America/Los_Angeles"
```

`status_day` is stored as `YYYY-MM-DD` text using the resolved instance timezone.

## Run tests

From the repository root:

```bash
python -m pytest tests/ -q
```

Optional release-bar targeted run:

```bash
python -m pytest tests/test_release_create_list.py -q --tb=short
```

Release evidence records these as passing for `v0.1.0` in [v0.1.0-release-evidence-checklist.md](../../08-delivery/output/v0.1.0-release-evidence-checklist.md) and [v0.1.0-release-notes.md](../../08-delivery/output/v0.1.0-release-notes.md).

## Smoke checks after startup

From another terminal, run:

```bash
curl -sS -o /tmp/pulseboard-home.html -w "%{http_code}\n" http://127.0.0.1:8000/
grep -q "PulseBoard today board" /tmp/pulseboard-home.html && echo "Home title OK"
curl -sS -o /tmp/pulseboard-identity.html -w "%{http_code}\n" http://127.0.0.1:8000/identity
curl -sS http://127.0.0.1:8000/statuses/today
```

Expected results:

* `/` returns HTTP `200` and HTML contains `PulseBoard today board`
* `/identity` returns HTTP `200`
* `/statuses/today` returns JSON list, usually `[]` on a fresh database

Fresh DB behavior:

* Board page shows `No statuses posted yet for today.` until a status is submitted.

## Common failures and fixes

### Port already in use (`127.0.0.1:8000`)

Symptom:

* Uvicorn fails to start with address-in-use error.

Fix:

```bash
uvicorn pulseboard.app:app --reload --port 8001
```

Then open <http://127.0.0.1:8001/>.

### Missing dependencies or module import errors

Symptoms:

* `ModuleNotFoundError` for `fastapi`, `uvicorn`, `multipart`, or `pulseboard`

Fixes:

1. Activate the intended environment (`hve-env` recommended)
2. Reinstall editable package with dev extras from repository root:

```bash
python -m pip install -e ".[dev]"
```

### Empty board on first run

Symptom:

* App loads but board has no rows.

Explanation and fix:

* This is expected for a new DB.
* Set display name at `/identity`, then submit status via the UI on `/`.

### Wrong DB file due to working directory

Symptom:

* Data appears to disappear across runs started from different folders.

Cause:

* Default DB path is relative (`data/pulseboard.db`) to process current working directory.

Fix:

```bash
export PULSEBOARD_DB_PATH="/absolute/path/to/pulseboard.db"
uvicorn pulseboard.app:app --reload
```

Use the same absolute DB path for all runs.

### Invalid timezone override

Symptom:

* Startup fails with invalid `PULSEBOARD_TZ` message.

Fix:

* Set `PULSEBOARD_TZ` to a valid IANA zone (for example `UTC`, `Asia/Kolkata`, `America/Los_Angeles`), or unset it to use host local timezone.

## Scope guard

This runbook intentionally excludes cloud deployment, SSO setup, notifications/email/Slack bot setup, and mobile install guidance.

`v0.1.0` limits are local-first MVP only:

* No SSO or OAuth
* No notifications, email, or Slack bots
* No mobile clients
