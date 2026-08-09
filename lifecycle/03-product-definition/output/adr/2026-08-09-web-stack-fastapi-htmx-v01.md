---
title: "ADR: FastAPI and HTMX web stack"
description: Decision to implement PulseBoard MVP as a FastAPI backend with HTMX-friendly server-rendered UI on Python 3.12+
author: PulseBoard
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - adr
  - fastapi
  - htmx
  - python
  - pulseboard
estimated_reading_time: 4
---

## Status

Accepted

## Date

2026-08-09

## Context

MVP must be runnable locally on **Python 3.12+** with a documented start path (BRD IN-05, BR-009; PRD FR-009, US-007). Experience constraints call for an **HTMX-friendly UI** and **API-capable backend** (BRD §5.3). Framing, BRD stack intent, and README already name **Python · FastAPI · SQLite · HTMX**.

Functional surface for `v0.1.0`:

* Set display name
* Create/update today’s status
* View today’s board
* No mobile app, no websocket push, no SPA mandate

Sources: [brd.md](../../../02-discovery/output/brd.md), [prd.md](../prd.md), [README.md](../../../../README.md).

## Decision

1. **Language/runtime:** Python **3.12+** (conda `hve-env` recommended per BRD tooling).
2. **Backend framework:** **FastAPI** application package under `src/pulseboard/`.
3. **UI approach:** **Server-rendered HTML** with **HTMX** for progressive enhancement on create/update/board refresh. Full page flows must still work for core paths where practical.
4. **API posture:** Prefer server-rendered routes for MVP UX; JSON endpoints are allowed if they simplify tests or HTMX partials, but a public multi-tenant API product is out of scope.
5. **App server for local run:** Uvicorn (or equivalent ASGI server) started via documented command.
6. **Front-end scope:** No separate React/Vue/SPA build pipeline required for MVP. No native mobile client.
7. **Real-time:** **No websockets** for live board push (explicitly out of scope). Users refresh or use HTMX request-driven updates.
8. **Tests:** Pytest-based automated tests covering create status and list/view today’s board (PRD AC-008.3, NFR-008).

## Consequences

### Positive

* Aligns team skill assumptions and existing repo intent
* HTMX keeps UI thin while supporting fast post/board loops (adoption risk mitigation)
* FastAPI fits form posts, cookies, and test clients well
* Avoids SPA/mobile scope creep (SM-05)

### Negative / trade-offs

* Team must accept server-rendered HTML rather than a rich SPA
* HTMX dependency (CDN or vendored asset) must be documented offline/lab constraints if any
* Without websockets, facilitators may manually refresh during standup (acceptable for MVP)

### Neutral

* Template engine (Jinja2, etc.) is an implementation detail
* Exact URL layout and template structure left to implementation

## Alternatives considered

| Option | Why not for MVP |
|--------|-----------------|
| Flask/Django | Viable, but FastAPI is the stated stack intent; switching needs a strong reason |
| JSON API + separate SPA | Extra frontend pipeline; not required by PRD UX status |
| Mobile app | Out of scope |
| Websockets for live board | Out of scope (BRD §5.2) |
| Desktop-only CLI | Fails facilitator glanceable board expectation |

## Related decisions

* Identity cookie on HTTP responses: [2026-08-09-local-identity-display-name-v01.md](2026-08-09-local-identity-display-name-v01.md)
* SQLite access from the app: [2026-08-09-sqlite-local-persistence-v01.md](2026-08-09-sqlite-local-persistence-v01.md)
* Today boundary used by routes: [2026-08-09-today-instance-timezone-v01.md](2026-08-09-today-instance-timezone-v01.md)

## When to revisit

* HTMX/server HTML blocks validated UX needs *within* current BRD scope
* Team standardizes on a different Python web framework company-wide
* BRD later adds realtime collaboration (websockets) or a first-class public API
* Offline lab policy forbids CDN-hosted HTMX and vendoring proves painful (still solvable without changing framework)

## References

* BRD IN-05, §5.3 Experience/Tooling, A-10, out-of-scope websockets/mobile
* PRD §5 UX/UI, FR-009, US-007, NFR-001, NFR-008, NFR-009
* README stack statement
