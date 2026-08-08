# PulseBoard — MVP Framing

| Field | Value |
| --- | --- |
| **Product** | PulseBoard — local-first team status board (doing / blocked / next → today’s board) |
| **Status** | Accepted |
| **HVE stage** | Stage 2 — Discovery input |
| **Next artifact** | `lifecycle/02-discovery/output/brd.md` via **`brd-builder`** |
| **Stack intent** | Python · FastAPI · SQLite · HTMX |

---

## 1. Problem

Small teams share daily status in chat (Teams, Slack, WhatsApp…). Updates get buried, blockers are hard to spot, and mid-day joiners cannot reconstruct *today*. Standup context lives in a noisy stream instead of one glanceable, day-scoped board.

**Hypothesis:** If the team can post doing / blocked / next onto a shared today’s board on a local machine, they will replace ad-hoc standup chat for daily status within ~two weeks.

---

## 2. Users

| Role | Need |
| --- | --- |
| **IC (poster)** | Fast create/edit of today’s doing / blocked / next; see teammates |
| **Lead / facilitator (reader)** | One today’s board to spot blockers and coverage without scrolling chat |

**Out of audience (MVP):** enterprise IT admins, multi-tenant SaaS buyers, mobile-only users, anonymous public users.

**Scale:** ~5–15 people on one shared local instance.

---

## 3. In scope / out of scope

### In (P0)

| Capability | Notes |
| --- | --- |
| Create status | doing / blocked / next (default day: today) |
| View today’s board | Team list/board for the current day |
| Simple local identity | Display name or demo login (choice → ADR); no SSO |
| Local persistence | SQLite on one machine |
| Runnable locally | Documented start path; Python 3.12+ |
| Thin first slice | Post + today’s board = Sprint 1 / `v0.1.0` core |

### Out

SSO / OAuth · notifications / email / Slack bots · mobile app · multi-tenant SaaS · real-time websockets · historical analytics · RBAC · rich media attachments · replacing chat for all communication · becoming a full project tracker.

Anything not listed under **In** is out until this framing is updated.

---

## 4. Constraints

| Area | Rule |
| --- | --- |
| Deployment | Local-first; single developer or shared lab machine |
| Data | SQLite OK; no cloud DB required |
| UI / API | HTMX-friendly UI; FastAPI backend |
| Auth | Simple local identity only |
| Quality | Tests for create/list; review against PRD AC before “done” |
| Tooling | HVE Core All + Copilot; conda `hve-env` (Python 3.12) |
| Process | Durable truth lives in `lifecycle/` and `.copilot-tracking/`, not chat |

---

## 5. Success metrics

Validation window: ~2 weeks of team use after `v0.1.0`.

| Metric | Target |
| --- | --- |
| Adoption | ≥70% of active members post ≥3 weekdays in a sample week |
| Replacement | Facilitator runs standup from the board ≥3 consecutive days |
| Blocker visibility | ≥1 real blocker found via the board that chat would have missed |
| Operability | New teammate can start the app from docs/runbook without tribal knowledge |
| Scope discipline | Ship without SSO, notifications, or mobile |

**Go** → deepen via PRD/next sprint. **Low posting** → simplify UX or revisit hypothesis before adding integrations.

---

## 6. Open questions

For BRD / ADR / PRD — do not invent in implementation chat.

1. Display name only vs demo login / shared password?  
2. One status per person per day, or multiple?  
3. Edit anytime same day, or lock after standup?  
4. Timezone / “today” boundary for remote teammates?  
5. Blocked: free text only, or also a filterable flag?  
6. Minimum test/review evidence before tagging `v0.1.0`?

---

## 7. HVE handoff

| Step | Action |
| --- | --- |
| **Helper** | **`brd-builder`** (not RPI Agent) |
| **Seed** | This file — problem, users, in/out, constraints, metrics |
| **Output** | `lifecycle/02-discovery/output/brd.md` |
| **Not yet** | Full PRD depth, GitHub issues, or code in `src/pulseboard/` |

After BRD acceptance → Stage 3 (`prd-builder` + ADRs), still bound by §3.
