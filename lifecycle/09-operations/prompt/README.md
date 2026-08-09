# Stage 9 — Operations prompts

| | |
| --- | --- |
| **Inputs** | Shipped app under `src/pulseboard/`; tag `v0.1.0` / Stage 8 notes; existing [`../output/runbook.md`](../output/runbook.md) if present |
| **Outputs** | Canonical [`../output/runbook.md`](../output/runbook.md); optional [`../output/ops-confirmation.md`](../output/ops-confirmation.md) |

Order: **A (runbook)** → **B (ops confirmation)**.  
Do not invent product features in this stage.

A runbook may already exist from Sprint 2 (#8). Prefer **verify and update** against the real app over rewriting from scratch.

---

## A. Author or refresh the runbook

### 1. Agent

**`Doc Ops`** (agent picker — this is the documentation helper in HVE Core All).  
Fallback: default Copilot Chat if Doc Ops is unavailable.  
Do **not** use BRD Builder, PRD Builder, or RPI Agent / Task Implementer for feature work here.

### 2. Prompt

```text
Author or refresh the PulseBoard operator runbook for v0.1.0.

Read from the workspace:
- lifecycle/09-operations/output/runbook.md (update in place if present)
- src/pulseboard/ (especially app startup, DB path, identity, today board routes)
- lifecycle/08-delivery/output/v0.1.0-release-notes.md
- lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
- README.md
- pyproject.toml

Include:
- Prerequisites (Python 3.12+, recommended conda env hve-env)
- How to install deps and start the app (exact commands from this repo)
- URL / how to open today's board
- Where the SQLite file lives (env vars and defaults)
- Timezone / "today" notes if applicable (e.g. PULSEBOARD_TZ)
- How to run tests
- How to verify the board loads (smoke checks)
- Common failures (port in use, missing deps, empty DB, wrong cwd for DB path) and fixes
- Explicit local-first MVP limits (no SSO, notifications, mobile)

Rules:
- Match the actual code and commands; do not invent flags or paths.
- Keep the runbook the durable operator source of truth under lifecycle/09-operations/output/runbook.md.
- Do not add product features.

Save to:
lifecycle/09-operations/output/runbook.md
```

---

## B. Ops confirmation (optional but recommended)

### 1. Agent

**`Doc Ops`** (or default Copilot Chat).

### 2. Prompt

```text
Produce a short PulseBoard ops confirmation that a new teammate can start from the runbook alone.

Read from the workspace:
- lifecycle/09-operations/output/runbook.md
- src/pulseboard/
- lifecycle/08-delivery/output/v0.1.0-release-notes.md

Record:
1) Commands you (or the operator) would run to install, start, open the board, and run tests
2) Pass/fail for smoke checks: app starts, board URL loads, display name + post status + see today row (or note if not executed in this session)
3) Gaps or ambiguities in the runbook to fix
4) Confirmation that ops docs do not expand MVP scope

Do not implement code unless fixing a factual error in the runbook.

Save to:
lifecycle/09-operations/output/ops-confirmation.md
```

---

## Done when

- [ ] `lifecycle/09-operations/output/runbook.md` matches how the shipped app actually starts and stores data  
- [ ] Smoke path is clear for a new teammate (optional `ops-confirmation.md` filled)  
- [ ] No new product features introduced under “ops”  
