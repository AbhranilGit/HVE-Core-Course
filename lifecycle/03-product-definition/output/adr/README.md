---
title: PulseBoard MVP architecture decision records
description: Index of accepted ADRs for PulseBoard MVP product definition
author: PulseBoard
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - adr
  - pulseboard
  - architecture
estimated_reading_time: 2
---

## Purpose

Architecture decisions for PulseBoard MVP that the BRD/PRD left open or that MVP constraints require. Product scope remains bound by the accepted BRD and PRD.

## Sources

* [brd.md](../../../02-discovery/output/brd.md) (Accepted)
* [prd.md](../prd.md)

## Accepted ADRs

| ADR | Decision |
|-----|----------|
| [2026-08-09-local-identity-display-name-v01.md](2026-08-09-local-identity-display-name-v01.md) | Display name + cookie continuity; no SSO/passwords |
| [2026-08-09-sqlite-local-persistence-v01.md](2026-08-09-sqlite-local-persistence-v01.md) | SQLite file on the host; one DB per instance |
| [2026-08-09-web-stack-fastapi-htmx-v01.md](2026-08-09-web-stack-fastapi-htmx-v01.md) | Python 3.12+, FastAPI, HTMX server-rendered UI |
| [2026-08-09-today-instance-timezone-v01.md](2026-08-09-today-instance-timezone-v01.md) | Today = calendar date in instance timezone |
| [2026-08-09-status-domain-model-v01.md](2026-08-09-status-domain-model-v01.md) | One status per name per day; same-day edit; free-text blocked |

## Non-goals of this folder

* Application code
* GitHub issues or sprint plans
* Expanding MVP beyond BRD/PRD in-scope capabilities
