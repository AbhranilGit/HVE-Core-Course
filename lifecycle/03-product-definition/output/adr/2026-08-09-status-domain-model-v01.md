---
title: "ADR: Status domain model for MVP"
description: Decision for one status per display name per day, same-day edits, free-text blocked, and field validation rules
author: PulseBoard
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - adr
  - status
  - domain-model
  - pulseboard
estimated_reading_time: 4
---

## Status

Accepted

## Date

2026-08-09

## Context

PRD §4.1 resolved several BRD open questions into product defaults that implementation must not re-litigate in code chat:

| Topic | PRD default |
|-------|-------------|
| Cardinality | One status per display name per calendar day |
| Edits | Allowed anytime the same day; no standup lock |
| Blocked | Free text only; no filterable flag |
| Fields | doing, blocked, next plain text; at least one non-empty |

Architecture still needs a single domain decision that SQLite constraints, API upserts, and UI forms share.

Sources: [brd.md](../../../02-discovery/output/brd.md), [prd.md](../prd.md).

## Decision

### Entity: Status

A **status** is one person’s standup snapshot for one calendar day.

| Field | Rule |
|-------|------|
| `display_name` | Non-empty plain text; identity key (see identity ADR) |
| `status_day` | Calendar date; default = instance today (see timezone ADR) |
| `doing` | Plain text; may be empty |
| `blocked` | Plain text; may be empty; **no** boolean/flag column required in MVP |
| `next` | Plain text; may be empty |
| Optional audit | `created_at` / `updated_at` recommended for debugging; not user-facing history product |

### Cardinality

* **Unique key:** `(display_name, status_day)`
* Create when no row exists; **update/replace** when it does (upsert). Never two rows for the same name and day.
* MVP UI does not offer posting to arbitrary other days; if an API accepts a day parameter later, default remains today. Multi-day history UI stays out of scope.

### Edits

* Updates allowed whenever `status_day == instance_today()`.
* No “lock after standup” flag, role, or timestamp gate in MVP.
* Editing prior days is **not** a MVP requirement (no history product). If encountered, prefer reject or no-UI rather than building a journal feature.

### Validation

* Reject create/update when all of doing, blocked, and next are empty/whitespace.
* Reject missing/blank display name.
* No rich media, markdown requirements, or attachment fields.

### Blocked visibility

* Facilitators spot blockers by reading non-empty `blocked` text on today’s board (PRD US-005).
* No filter chip, blocked-only queue, notifications, or workflow states in MVP.

### Board projection

* Today’s board = all statuses where `status_day == instance_today()`, each showing display name, doing, blocked, next.
* Empty board is a valid state (not an error).

## Consequences

### Positive

* Glanceable board for facilitators (one row per person per day)
* Upsert semantics match “edit anytime same day”
* Unique constraint in SQLite enforces the rule mechanically
* Free-text blocked meets BR-005 without tracker scope

### Negative / trade-offs

* Power users cannot log multiple discrete status cards per day without overwriting
* Free-text blockers may be harder to scan than a flag (accepted; OQ-05 deferred)
* Display name renames do not migrate the old row (identity ADR trade-off)

### Neutral

* Ordering on the board (alpha by name, last-updated, etc.) is an implementation UX detail; choose one deterministic order and keep it stable

## Alternatives considered

| Option | Why not for MVP |
|--------|-----------------|
| Multiple statuses per person per day | Noisier board; PRD chose one |
| Lock after standup | Extra process rules; PRD rejected for MVP |
| Blocked boolean + text | Small addition but PRD deferred filterable flag |
| Full journal/history | Out of scope historical analytics / tracker creep |

## Related decisions

* [2026-08-09-local-identity-display-name-v01.md](2026-08-09-local-identity-display-name-v01.md)
* [2026-08-09-today-instance-timezone-v01.md](2026-08-09-today-instance-timezone-v01.md)
* [2026-08-09-sqlite-local-persistence-v01.md](2026-08-09-sqlite-local-persistence-v01.md)

## When to revisit

* Facilitators need multiple cards per person per day during validation
* Team demands standup lock for compliance/process reasons (requires PRD change)
* Blocked free text fails SM-03 and a **flag** is added under updated PRD (still not a workflow engine)
* History/analytics enters accepted scope

## References

* BRD BR-001–BR-006, OQ-02, OQ-03, OQ-05, R-07
* PRD §4.1, FR-002–FR-007, US-002–US-005, field rule under US-002
