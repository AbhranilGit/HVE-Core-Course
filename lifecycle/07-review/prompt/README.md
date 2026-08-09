# Stage 7 — Review prompts

| | |
| --- | --- |
| **Inputs** | [`../../05-sprint-planning/output/sprint-plan.md`](../../05-sprint-planning/output/sprint-plan.md); [`../../03-product-definition/output/prd.md`](../../03-product-definition/output/prd.md); [`../../06-implementation/output/`](../../06-implementation/output/); `.copilot-tracking/{plans,changes,research}/`; code under `src/pulseboard/` |
| **Outputs** | [`../output/sprint-1-rpi-review.md`](../output/sprint-1-rpi-review.md); [`../output/sprint-2-rpi-review.md`](../output/sprint-2-rpi-review.md); [`../output/sprint-1-code-review.md`](../output/sprint-1-code-review.md) |

Order: **A (Sprint 1)** → **B (Sprint 2)** → **C (code review)**. Do not rewrite features unless listing follow-ups.

---

## How to run `/task-review`

1. Select **RPI Agent** (or Task Reviewer if listed).  
2. Type **`/task-review`** — placeholders appear:  
   `[plan=...] [changes=...] [research=...] [scope=...]`  
3. Replace those placeholders with the paths in the prompt below (do not leave `...` literal).  
4. Paste the rest of the prompt after the flags.  
5. Send.

You do **not** need `/rpi-review`.

---

## A. Sprint 1 acceptance review

### 1. Agent

**RPI Agent** + **`/task-review`** (or agent **Task Reviewer**)

### 2. Prompt

```text
/task-review plan=lifecycle/05-sprint-planning/output/sprint-plan.md changes=.copilot-tracking/changes/2026-08-09 research=.copilot-tracking/research/2026-08-09 scope=PulseBoard Sprint 1 only (#2 #6 #4 #5 #3 #9): display name + post doing/blocked/next + today's board; use lifecycle/06-implementation/output/issue-02 through issue-09 and lifecycle/03-product-definition/output/prd.md

Review PulseBoard Sprint 1 against the sprint-plan Sprint 1 definition of done and PRD AC.

Also read from the workspace:
- lifecycle/04-decomposition/output/backlog-snapshot.md
- src/pulseboard/ and tests/
- lifecycle/06-implementation/output/issue-02/ through issue-09/

Must validate:
1) User can set/use simple local identity (display name)
2) User can post doing / blocked / next for today
3) Today's board shows those updates
4) Scope discipline: no SSO, notifications, or mobile added as MVP

Workflow:
- Compare implementation evidence to Sprint 1 DoD and PRD AC.
- Separate execution status from acceptance outcome.
- List defects and follow-ups; do not rewrite features unless listing follow-ups.
- Do not expand scope into Sprint 2 (#10 #8 #7) except as deferred follow-ups.

Save the review to:
lifecycle/07-review/output/sprint-1-rpi-review.md
```

---

## B. Sprint 2 acceptance review

### 1. Agent

**RPI Agent** + **`/task-review`** (or agent **Task Reviewer**)  
Run after Sprint 1 review (or after Sprint 2 implementation is complete).

### 2. Prompt

```text
/task-review plan=lifecycle/05-sprint-planning/output/sprint-plan.md changes=.copilot-tracking/changes/2026-08-09 research=.copilot-tracking/research/2026-08-09 scope=PulseBoard Sprint 2 only (#10 #8 #7): automated create/list tests, local-first runbook, v0.1.0 release evidence checklist; use lifecycle/06-implementation/output/issue-10 issue-08 issue-07 and lifecycle/03-product-definition/output/prd.md

Review PulseBoard Sprint 2 against the sprint-plan Sprint 2 definition of done and PRD AC.

Also read from the workspace:
- lifecycle/05-sprint-planning/output/sprint-plan.md (Sprint 2 section)
- lifecycle/04-decomposition/output/backlog-snapshot.md (TEMP-7 TEMP-8 TEMP-9)
- lifecycle/06-implementation/output/issue-10/
- lifecycle/06-implementation/output/issue-08/
- lifecycle/06-implementation/output/issue-07/
- tests/
- lifecycle/09-operations/output/runbook.md (or path stated by #8)
- lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md (or path stated by #7)
- lifecycle/07-review/output/sprint-1-rpi-review.md (if present)

Must validate:
1) Automated tests cover create/upsert status and list today's board (temp DB), including prior-day exclusion and no duplicate row on upsert (#10)
2) Runbook documents prerequisites, start commands, URL, local-first model, DB path / TZ notes, and how to run tests (#8)
3) v0.1.0 checklist maps PRD AC-008.*, requires out-of-scope absences, test evidence, and reviewer sign-off before tag (#7)
4) No new product features beyond MVP; Sprint 2 is harden/package only

Workflow:
- Compare evidence to Sprint 2 DoD and related PRD AC.
- Separate execution status from acceptance outcome.
- List defects and follow-ups; do not rewrite features unless listing follow-ups.

Save the review to:
lifecycle/07-review/output/sprint-2-rpi-review.md
```

---

## C. Code review

### 1. Agent

**`code-review`** (agent picker). If missing, use default Copilot Chat with the prompt below.

### 2. Prompt

```text
Review the local PulseBoard codebase for MVP readiness after Sprint 1 and Sprint 2 work.

Read from the workspace:
- src/pulseboard/
- tests/
- lifecycle/07-review/output/sprint-1-rpi-review.md (if present)
- lifecycle/07-review/output/sprint-2-rpi-review.md (if present)
- lifecycle/05-sprint-planning/output/sprint-plan.md

Focus on:
- Correctness of create/list today status and display-name identity
- Python / FastAPI basics
- Obvious security issues around input validation and identity/cookies
- Test gaps that block calling Sprint 2 done
- Docs/runbook/checklist consistency with the running app

Do not implement fixes in this step unless asked; report findings and severity.

Save the code review notes to:
lifecycle/07-review/output/sprint-1-code-review.md
```

---

## Done when

- [ ] `sprint-1-rpi-review.md` exists with clear Accept / Defects / Follow-ups  
- [ ] `sprint-2-rpi-review.md` exists with clear Accept / Defects / Follow-ups  
- [ ] `sprint-1-code-review.md` exists (or findings folded into the acceptance reviews with an explicit note)  
- [ ] No silent scope expansion; follow-ups are listed, not coded ad hoc in review  
