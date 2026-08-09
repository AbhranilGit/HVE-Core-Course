---
title: "ADR: SQLite for local persistence"
description: Decision to persist PulseBoard MVP status data in a local SQLite database file on the host machine
author: PulseBoard
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - adr
  - sqlite
  - persistence
  - pulseboard
estimated_reading_time: 4
---

## Status

Accepted

## Date

2026-08-09

## Context

Statuses must survive process restart on one machine (BRD IN-04, BR-008; PRD FR-008, US-006). Constraints:

* Local-first; single developer or shared lab machine
* No cloud database required
* Scale ~5–15 people, one day’s board at a time for primary UX
* Stack intent and README name SQLite
* Create/list must be testable with automated tests

Sources: [brd.md](../../../02-discovery/output/brd.md), [prd.md](../prd.md).

## Decision

1. **Datastore:** Use **SQLite** via a single database **file** on the host filesystem.
2. **Deployment unit:** One PulseBoard process (or one configured app instance) owns one DB file. No multi-node shared DB for MVP.
3. **Default location:** Document a default path under the project or a configurable env var (for example `PULSEBOARD_DB_PATH`); exact path is implementation detail but **must be documented** in the runbook (PRD AC-006.2, AC-007.*).
4. **Schema responsibility:** Relational tables sufficient to store display name, status day, doing, blocked, next, and timestamps as needed. Enforce **one row per (display_name, status_day)** at the data layer (unique constraint) to match the status domain ADR.
5. **Migrations:** MVP may create schema on startup with a simple initialize path; heavy migration frameworks are optional, not required.
6. **Backups / rollback:** Ops model is file copy/restore of the DB file (PRD §12). No managed backup service.
7. **Not in MVP:** Postgres/MySQL, cloud DBaaS, multi-tenant schemas, replication.

## Consequences

### Positive

* Zero separate DB server for local run (SM-04 / operability)
* Matches BRD A-04 and explicit IN-04
* Easy test isolation via temp DB files
* Unique constraint cleanly implements one-status-per-name-per-day

### Negative / trade-offs

* Concurrent writers on a shared lab machine can hit SQLite locking under abuse (acceptable at 5–15 users for this workload)
* DB file permissions and path mistakes are operator-owned
* Not a path to multi-tenant SaaS without a later ADR and scope change

### Neutral

* SQL access library (stdlib `sqlite3`, SQLAlchemy, etc.) is an implementation choice; prefer the smallest option that keeps create/list tests clear

## Alternatives considered

| Option | Why not for MVP |
|--------|-----------------|
| In-memory only | Fails BR-008 / US-006 persistence |
| JSON/YAML file store | Possible but weaker concurrency and constraint enforcement; SQLite already in stack intent |
| PostgreSQL locally | Extra ops burden; no BRD requirement |
| Cloud DB | Violates local-first / no-cloud-DB constraint |

## Related decisions

* Status domain (unique key shape): [2026-08-09-status-domain-model-v01.md](2026-08-09-status-domain-model-v01.md)
* Web stack: [2026-08-09-web-stack-fastapi-htmx-v01.md](2026-08-09-web-stack-fastapi-htmx-v01.md)

## When to revisit

* SQLite locking or corruption appears under real shared-lab use
* BRD expands beyond single-machine local-first
* Need concurrent multi-host deployment (would also break other MVP assumptions)
* Compliance or durability requirements exceed file-backed SQLite

## References

* BRD IN-04, BR-008, A-04, §5.3 Data
* PRD FR-008, US-006, NFR-002, §9 Dependencies, §12 Operational Considerations
