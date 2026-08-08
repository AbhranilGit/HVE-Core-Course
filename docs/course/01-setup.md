# Module 1 — Setup

HVE Stage 1. Goal: environment ready, identity clear, no product code yet.

## Why this module exists

HVE fails quietly when Copilot cannot see agents/skills, or when the repo has no place for planning artifacts. We lock that down first.

## Steps

### 1.1 Confirm tooling ✅

Recorded answers:

1. **VS Code + Copilot + hve-core-all**
2. **RPI Agent** visible
3. **Python 3.8.10** — too old for a smooth modern FastAPI/Pydantic setup. Before Module 6, install **Python 3.11+** (or 3.12) and confirm with `python3.11 --version` / `python3.12 --version`. Setup can continue; do not block Module 1 on the upgrade.

### 1.2 Accept product framing ✅

Accepted MVP framing:

> PulseBoard is a local-first team status board. People post doing / blocked / next. A board view shows today’s updates. No SSO, no notifications, no mobile app in MVP.

### 1.3 Repo readiness

Confirm these folders exist (already scaffolded in this branch):

- `docs/course/`
- `docs/project-planning/`
- `docs/ops/`
- `apps/pulseboard/`
- `.copilot-tracking/`

### 1.4 Module 1 exit

You are done with Setup when:

- [ ] Tooling path chosen (VS Code HVE and/or Cursor coach)
- [ ] MVP one-liner accepted
- [ ] Folder layout present
- [ ] `docs/course/PROGRESS.md` still points at Module 1 until coach advances you

**Do not start writing FastAPI code in this module.**
