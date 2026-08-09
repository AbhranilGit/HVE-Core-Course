---
title: "Issue #9 research - today board and status form UI (HTMX)"
description: Research-only findings for PulseBoard TEMP-6 and GitHub issue #9 before planning or implementation
author: RPI Agent
ms.date: 2026-08-09
ms.topic: reference
keywords:
  - pulseboard
  - issue-09
  - ui
  - htmx
  - today-board
  - research
  - rpi
estimated_reading_time: 9
---

## Document control

| Field | Value |
|-------|-------|
| Issue | [#9](https://github.com/AbhranilGit/HVE-Core-Course/issues/9) - ui: today board and status form (HTMX) |
| Local spec | [backlog-snapshot.md](../../04-decomposition/output/backlog-snapshot.md) - TEMP-6 |
| Phase | Research only (`/rpi continue=1`) |
| Status | Complete - ready for Plan gate |
| Production code | None (this phase) |
| Sprint | 6 of 6 (Sprint 1) |
| Depends on | #4 identity, #5 upsert, #3 today-list API |

## Scope summary (authoritative)

From TEMP-6 and issue #9:

In scope:

* Browser UI for display name entry and confirmation
* Status form for doing, blocked, next
* Today board table/list view
* Empty-board state copy that is not an error
* After save, user sees own values on today board without chat
* Keyboard-usable core form and board
* Wire to existing cookie identity + upsert + today-list behavior

Out of scope:

* Pixel-perfect branding and design system
* Mobile native app
* Websocket live updates
* Multi-day history navigation
* SSO UI

Acceptance criteria to drive planning:

| ID | Criterion | Source |
|----|-----------|--------|
| AC-P-050 | Running local app allows setting display name, entering doing/blocked/next, and submitting from UI | PRD US-001/US-002, UX section |
| AC-P-051 | After successful save with valid identity, user can view own new/updated values on today board without chat | PRD AC-002.3, AC-003.1 |
| AC-P-052 | With zero posts today, board shows clear empty state, not crash/error | PRD AC-004.1 |
| AC-P-053 | With multiple posts today, board shows display name, doing, blocked, and next per row | PRD AC-004.2, AC-005.1 |
| AC-P-054 | MVP UI excludes SSO, lock-after-standup, blocked workflow states, notifications | PRD AC-001.3, AC-003.3, AC-005.3 |

## Evidence log

### Dependency status check (#4, #5, #3)

| Dependency | Expected for #9 | Current status | Evidence |
|------------|-----------------|----------------|----------|
| #4 identity | UI can set and persist display name | In place | `GET/POST /identity` in app and tests |
| #5 upsert | UI can submit doing/blocked/next | In place | `POST /status` form route with identity cookie gate |
| #3 list | UI can render today board from API | In place | `GET /statuses/today` JSON list route |

Blocker conclusion: no hard blocker for wiring TEMP-6 UI to existing behavior.

### Current repo patterns relevant to UI work

| Pattern | Current implementation |
|---------|------------------------|
| HTML rendering style | Inline HTML string builder exists (`_identity_page`) with `HTMLResponse` |
| Form posting style | FastAPI `Form(...)` inputs with standard POST |
| Redirect pattern | Identity POST uses `303` redirect to `GET /identity` |
| Data APIs for UI | `POST /status` and `GET /statuses/today` return JSON |
| DB access pattern | Open per request with `connect(app.state.db_path)` and `finally: close` |
| App init | `create_app(db_path=...)` and eager/lifespan `init_db` |
| Test pattern | `TestClient(create_app(db_path=tmp_path/...))` in context manager |
| Serialization | `_status_to_dict` includes display_name, doing, blocked, next, status_day, timestamps |

### Product and architecture constraints consulted

| Source | Constraint for #9 |
|--------|-------------------|
| PRD UX section | Browser UI with progressive enhancement is acceptable and expected |
| PRD US-001..US-005 | UI must support identify, submit/edit status, and board viewing |
| PRD AC-002.3 | Save flow must lead to visible board values without chat |
| PRD AC-004.1/004.2 | Board handles empty and non-empty lists clearly |
| PRD AC-005.1 | Blocked text visible on board row |
| PRD AC-005.3 | No blocked workflow/timers/notifications |
| PRD NFR-006 | Keyboard-usable core flows; best-effort manual pass |
| ADR web-stack | Server-rendered HTML with HTMX-friendly enhancement; no SPA/websocket mandate |
| ADR identity | Cookie display name continuity; no SSO/OAuth |
| ADR status model | One row per name/day, same-day edits, no lock-after-standup |

### Confirmed API contracts available to UI

| Route | Method | Input | Output | UI use |
|-------|--------|-------|--------|--------|
| `/identity` | GET | none | HTML page | Display name entry/confirmation surface |
| `/identity` | POST | `display_name` form | 303 redirect or 400 HTML | Save identity cookie |
| `/status` | POST | `doing`, `blocked`, `next` form + cookie | 200 JSON or 400 JSON | Save/update status |
| `/statuses/today` | GET | none | 200 JSON array | Render board rows / empty state |

## Design options for planning

### Option A (recommended baseline)

Single server-rendered board page (for example `/`) that includes:

* Identity section (show current name, small update form)
* Status form posting to `/status`
* Today board section rendered from `GET /statuses/today` data source via direct repository call or internal function call
* Plain HTML first, then optional HTMX attributes for post-refresh

Why this fits TEMP-6:

* Meets all AC with minimum new surface
* Reuses existing API behavior
* Stays inside no-SPA/no-websocket constraints

### Option B

Keep `/identity` page and add separate board page (`/board`), linking between them.

Pros:

* Minimal disruption to existing identity route
* Clear separation of concerns

Cons:

* AC-P-051 may require extra navigation after save unless flow is handled carefully

### Option C

Build template files and partial endpoints from the start.

Pros:

* Better long-term maintainability for HTML

Cons:

* Larger scope and more file churn for Sprint 1 final slice

Research recommendation: start with Option A unless planning identifies maintainability pressure that justifies template setup now.

## Testing implications for #9 planning

Expected test additions (not implemented in this phase):

* UI GET route returns page with display name section, form fields, and board section marker
* UI submit flow can set name, post status, and show own values on board (AC-P-051)
* Empty board message appears when no rows exist (AC-P-052)
* Multiple rows render all four visible columns/values (AC-P-053)
* Negative scope checks confirm absence of SSO, lock-after-standup UI controls, blocked workflow, notifications (AC-P-054)
* Keyboard-usable basics: labels linked to inputs, submit button reachable, table/list semantic structure

## Risks and mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Scope creep into visual polish | Delay and instability | Keep copy and layout simple; prioritize AC behavior |
| Adding Sprint-2 concerns | Violates sprint order | Explicitly exclude #10/#8/#7 in plan |
| Coupling UI to HTTP self-calls | Test fragility | Prefer shared service/repository calls inside route handler where simple |
| Inconsistent post-save UX | AC-P-051 miss | Define deterministic post-save refresh path in plan |
| Accessibility regressions | NFR-006 miss | Use labels, semantic headings, table/list structure, keyboard-only smoke tests |
| Hidden feature creep (SSO/lock/workflow) | AC-P-054 fail | Add explicit absence assertions in tests |

## Explicit non-goals for this issue

* No mobile app, no websocket live updates
* No history navigation
* No SSO or OAuth UI
* No lock-after-standup control
* No blocked workflow/timer/notifications
* No design system migration or SPA build pipeline

## Open questions for planning (non-blocking)

1. Primary page path choice for MVP UI: `/` vs `/board`
2. Whether to keep `/identity` as standalone page after introducing board page
3. HTMX delivery approach: CDN script tag vs deferred/no-script progressive form first
4. Render strategy: inline HTML in app module vs introducing templates now
5. Post-save refresh model: redirect to board page vs in-page refresh with HTMX

## Ready for plan?

- [x] TEMP-6 scope and AC-P-050..054 captured
- [x] #4, #5, #3 behavior confirmed available to wire UI
- [x] Repo patterns documented for HTML, forms, API, and tests
- [x] Constraints from PRD/ADRs captured
- [x] Options and open questions listed for planning
- [x] No production code written in this phase
- [ ] User verifies Research checklist in [README.md](README.md) before Plan (`continue=2`)

## Next

After Research gate: run `/rpi continue=2` to write issue-09 plan only.
