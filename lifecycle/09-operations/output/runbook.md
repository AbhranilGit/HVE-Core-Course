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
estimated_reading_time: 6
---

## Purpose

This runbook is the canonical start path for operating PulseBoard locally.

PulseBoard is local-first for MVP: one machine, one app process, one local SQLite file. No cloud database is required.

## Prerequisites

* Python 3.12 or newer
* Recommended environment: conda environment `hve-env`

## Install dependencies

From the repository root:

```bash
python -m pip install -e ".[dev]"
```

## Start the app

From the repository root:

```bash
uvicorn pulseboard.app:app --reload
```

## Open the board UI

Open this URL in a browser:

<http://127.0.0.1:8000/>

This is the today board route (`/`).

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

## Today boundary and timezone behavior

PulseBoard uses instance-level calendar today.

* Default timezone: host local timezone of the machine running the process
* Optional override: `PULSEBOARD_TZ` using a valid IANA timezone name
* If `PULSEBOARD_TZ` is invalid, startup/date resolution fails fast

Example override:

```bash
export PULSEBOARD_TZ="America/Los_Angeles"
```

## Run tests

From the repository root:

```bash
python -m pytest tests/ -q
```

## Scope guard

This runbook intentionally excludes cloud deployment, SSO setup, and mobile install guidance.
