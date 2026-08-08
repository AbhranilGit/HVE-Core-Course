# Module 1 — Setup

HVE Stage 1. Goal: environment ready, identity clear, no product code yet.

## Why this module exists

HVE fails quietly when Copilot cannot see agents/skills, or when the repo has no place for planning artifacts. We lock that down first.

## Steps

### 1.1 Confirm tooling

Reply to the coach with answers to:

1. Are you using **VS Code + Copilot + hve-core-all**, **Cursor only**, or **both**?
2. Can you see any of: `RPI Agent`, `/rpi-research`, `/rpi-plan`, `/rpi-implement`?
3. Do you have Python 3.11+ available? (`python3 --version`)

### 1.2 Accept product framing

Confirm you accept this MVP framing (or propose a one-line change):

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
