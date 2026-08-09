---
title: "PulseBoard ops confirmation for new teammate startup"
description: Short operator confirmation that a new teammate can start PulseBoard from the runbook alone for v0.1.0
author: Task Reviewer
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - operations
  - confirmation
  - runbook
  - v0.1.0
estimated_reading_time: 4
---

## Scope

This note confirms whether a new teammate can operate PulseBoard from [lifecycle/09-operations/output/runbook.md](runbook.md) alone.

References checked:

* [lifecycle/09-operations/output/runbook.md](runbook.md)
* [src/pulseboard/app.py](../../../src/pulseboard/app.py)
* [src/pulseboard/db.py](../../../src/pulseboard/db.py)
* [src/pulseboard/today.py](../../../src/pulseboard/today.py)
* [lifecycle/08-delivery/output/v0.1.0-release-notes.md](../../08-delivery/output/v0.1.0-release-notes.md)

## 1) Commands used

Environment and install:

```bash
/home/abhranil/Installation/miniconda3/envs/hve-env/bin/python -m pip install -e ".[dev]"
```

Start app:

```bash
export PULSEBOARD_DB_PATH="$PWD/data/pulseboard-ops-confirmation.db"
/home/abhranil/Installation/miniconda3/envs/hve-env/bin/python -m uvicorn pulseboard.app:app --reload --port 8001
```

Open and smoke-check board routes:

```bash
curl -sS -o /tmp/pb-home.html -w "HOME_HTTP=%{http_code}\n" http://127.0.0.1:8001/
grep -q "PulseBoard today board" /tmp/pb-home.html && echo "HOME_TITLE=PASS"
curl -sS -o /tmp/pb-identity.html -w "IDENTITY_HTTP=%{http_code}\n" http://127.0.0.1:8001/identity
```

Identity + post status + verify today row:

```bash
curl -sS -i -c /tmp/pb.cookies -X POST -d "display_name=NewTeammate" http://127.0.0.1:8001/identity
curl -sS -b /tmp/pb.cookies -X POST -d "doing=Learn+runbook&blocked=&next=Pair+review" http://127.0.0.1:8001/status
curl -sS http://127.0.0.1:8001/statuses/today
```

Run tests:

```bash
/home/abhranil/Installation/miniconda3/envs/hve-env/bin/python -m pytest tests/ -q
```

## 2) Smoke check result

| Check | Status | Evidence |
| --- | --- | --- |
| App starts | Pass | Uvicorn startup complete on `127.0.0.1:8001` |
| Board URL loads | Pass | `HOME_HTTP=200`, `HOME_TITLE=PASS` |
| Display name set | Pass | `POST /identity` returned `303` and cookie `pulseboard_display_name=NewTeammate` |
| Post status works | Pass | `POST /status` returned JSON row for `NewTeammate` |
| Today row visible | Pass | `GET /statuses/today` includes `NewTeammate` and `Learn runbook` |
| Runbook test command | Pass | `42 passed, 1 warning in 1.96s` |

Notes:

* Port `8000` was in use in this session, so startup used `--port 8001` per runbook troubleshooting guidance.
* Test warning remains non-blocking: `StarletteDeprecationWarning` from `fastapi/testclient.py`.

## 3) Runbook gaps or ambiguities

1. The runbook smoke-check section validates GET routes but does not include a full command-line example for `POST /identity` and `POST /status` with cookie reuse.
2. The runbook assumes operators can switch from port `8000` to `8001` when needed, but the main open URL step still points only to `8000`.

These are clarity improvements only and do not block startup from runbook alone.

## 4) MVP scope confirmation

Ops docs stay within MVP scope and do not expand product scope.

Confirmed absent from docs and operator flow:

* SSO or OAuth
* Notifications, email, or Slack bots
* Mobile clients

Conclusion: a new teammate can start and validate PulseBoard from the runbook alone for `v0.1.0`.
