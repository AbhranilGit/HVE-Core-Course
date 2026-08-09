---
title: "ADR: Local identity via display name"
description: Decision to attribute PulseBoard MVP posts with a non-empty display name and browser cookie continuity, without SSO or passwords
author: PulseBoard
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - adr
  - identity
  - display-name
  - pulseboard
estimated_reading_time: 4
---

## Status

Accepted

## Date

2026-08-09

## Context

PulseBoard MVP needs simple local identity so ICs can attribute **doing / blocked / next** on a shared local instance (BRD IN-03, BR-007; PRD FR-001, US-001).

Sources:

* [brd.md](../../../02-discovery/output/brd.md) (Accepted): display name or demo login; no SSO; trusted team of ~5–15 on one machine
* [prd.md](../prd.md): product default is **display name**; session mechanism left to ADR (OQ-PRD-01); SSO/OAuth out of scope

Open force:

* Posters need a stable label on today’s board
* Team is trusted and local-first; enterprise auth is out of audience
* PRD forbids blank names and requires no SSO path
* Implementation still needs a concrete continuity mechanism (cookie vs re-enter vs password)

## Decision

1. **Identity model:** A poster is identified only by a **non-empty display name** (plain text). This is an attribution label, not authenticated security principal.
2. **No passwords, shared secrets, demo login, SSO, or OAuth** in MVP.
3. **Continuity:** After the user submits a valid display name, the server stores it in an **HTTP cookie** scoped to the app (local instance). Subsequent create/update requests use that cookie value unless the user changes name via an explicit UI control.
4. **Validation:** Trim whitespace; reject empty/whitespace-only names; do not create statuses under a blank name.
5. **Collision rule:** Display names are matched case-sensitively as entered for MVP uniqueness of “one status per name per day” (see status domain ADR). Operators should pick distinct names; no RBAC or claim-of-name enforcement.
6. **Trust model:** Anyone who can reach the local instance can set any display name. Acceptable only because deployment is local/lab and audience is a trusted small team (BRD A-05, NFR-004).

## Consequences

### Positive

* Meets thinnest IN-03 path and PRD AC-001.* without auth product scope
* Cookie continuity avoids re-typing the name every post during a workday
* Clear non-goal boundary for SSO keeps SM-05 / G-005 intact

### Negative / trade-offs

* Not authentication: name spoofing is trivial on a reachable instance
* Case-sensitive duplicates (`Ada` vs `ada`) can confuse the board
* Cookie-only continuity is browser-specific; another browser requires re-entry
* Changing display name creates a *different* identity key for the day-cardinality rule unless the user edits under the new name (no account merge)

### Neutral

* Cookie name, max-age, and signing details are implementation choices; prefer a simple cookie sufficient for local trusted use. Signed cookies are allowed but not required for MVP.

## Alternatives considered

| Option | Why not for MVP |
|--------|-----------------|
| Re-enter display name on every request | Higher friction; hurts adoption (SM-01) |
| Demo login / shared password | Extra credential UX without real multi-tenant security; BRD allowed it but PRD chose thinner default |
| Per-user password accounts | Out of thin-slice spirit; slides toward RBAC/SSO later |
| SSO / OAuth | Explicitly out of scope (BRD §5.2, PRD AC-001.3) |

## Related decisions

* Status cardinality and edit rules: [2026-08-09-status-domain-model-v01.md](2026-08-09-status-domain-model-v01.md)
* Application stack (how cookies/forms are served): [2026-08-09-web-stack-fastapi-htmx-v01.md](2026-08-09-web-stack-fastapi-htmx-v01.md)

## When to revisit

Revisit this ADR if any of the following become true:

* The instance is exposed beyond a trusted local/lab network
* Name spoofing or disputes block standup trust
* Validation shows display name alone fails adoption and a **demo login** is still in-scope under an updated BRD/PRD
* Product scope gains real auth (still requires BRD/PRD change before SSO)

## References

* BRD OQ-01, BR-007, IN-03, A-05, R-04
* PRD §4.1 OQ-01, FR-001, US-001, OQ-PRD-01, NFR-004
