---
title: "ADR: Today boundary via instance timezone"
description: Decision that PulseBoard MVP defines calendar today using one instance-configured timezone defaulting to host local time
author: PulseBoard
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - adr
  - timezone
  - today
  - pulseboard
estimated_reading_time: 3
---

## Status

Accepted

## Date

2026-08-09

## Context

The product is day-scoped: default status day is **today**, and the primary board shows **today’s** statuses (BRD BR-002, BR-003; PRD FR-007, US-004). Remote or multi-zone teammates create ambiguity about when “today” rolls over (BRD OQ-04, R-05; PRD §4.1 OQ-04).

Constraints:

* No multi-region product or per-user timezone matrix in MVP
* Single shared local instance
* Need a deterministic rule for create defaults and board queries
* Must remain documentable for operators (SM-04)

Sources: [brd.md](../../../02-discovery/output/brd.md), [prd.md](../prd.md).

## Decision

1. **Single clock for the instance:** “Today” is the **calendar date** in the **instance timezone**.
2. **Default timezone:** **Host local timezone** of the machine running PulseBoard, unless overridden by configuration.
3. **Configuration:** Allow an optional explicit timezone setting (for example env `PULSEBOARD_TZ` using an IANA name). If unset, use host local time. Document the effective rule in the runbook.
4. **Storage:** Persist `status_day` as a **calendar date** (not a timezone-varying timestamp alone). Timestamps for audit/debug may be stored in UTC, but day membership uses `status_day`.
5. **Board query:** Default board lists rows where `status_day == instance_today()`.
6. **Out of MVP:** Per-user timezones, automatic geo detection, multi-day history UI, “follow my laptop TZ while traveling” modes.

## Consequences

### Positive

* One consistent board for the whole team during standup
* Simple implementation and tests (inject a clock/date)
* Matches PRD glossary definition of Today

### Negative / trade-offs

* A teammate in another zone near midnight may disagree about “today”
* Host TZ misconfiguration (container UTC vs lab local) can surprise operators if undocumented

### Neutral

* Facilitators should treat the instance TZ as the team’s standup day boundary

## Alternatives considered

| Option | Why not for MVP |
|--------|-----------------|
| Per-user timezone | Multiplies board fragmentation; PRD deferred |
| Always UTC date | Simple but often mismatches local standup day for non-UTC teams |
| Browser-local today per request | Two users could post into different “todays” on one shared board |

## Related decisions

* Status create defaults: [2026-08-09-status-domain-model-v01.md](2026-08-09-status-domain-model-v01.md)
* Runtime host assumptions: [2026-08-09-web-stack-fastapi-htmx-v01.md](2026-08-09-web-stack-fastapi-htmx-v01.md)

## When to revisit

* Validation shows remote teammates systematically miss the board near day boundaries
* Team runs multiple instances across regions and needs federation (scope change)
* BRD/PRD explicitly add per-user timezone support

## References

* BRD BR-002, OQ-04, R-05, A-06
* PRD §4.1 OQ-04, FR-007, US-004 AC-004.3, Glossary “Today”, OQ-BRD-04 residual
