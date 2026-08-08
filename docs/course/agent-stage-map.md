# HVE agents by job and stage

Cheat sheet for this coaching track (`hve-core-all`). Prefer the **smallest** agent that owns the next job.

## PulseBoard path (what we will actually use)

| Stage | Job | Primary agent / skill | Output |
| --- | --- | --- | --- |
| 1 Setup | Install / configure HVE | `hve-core-installer` (skill) | Working agents in Copilot |
| 2 Discovery | Business requirements | **`brd-builder`** | `docs/project-planning/*brd.md` |
| 2 Discovery | Optional user discovery | `dt-coach` | Problem / stakeholder insights |
| 2 Discovery | Optional tech research gap | `/rpi-research` | `.copilot-tracking/research/...` |
| 3 Product definition | Product requirements | **`prd-builder`** | `docs/project-planning/*prd.md` |
| 3 Product definition | Architecture decisions | **`adr-creation`** | `docs/project-planning/adr/...` |
| 3 Product definition | Diagrams | `architecture-diagrams` (skill) | Architecture docs/diagrams |
| 3 Product definition | UX journeys (optional) | `ux-ui-designer` | Journey / JTBD artifacts |
| 4 Decomposition | Break PRD into issues | **`github-backlog-manager`** | GitHub issues |
| 5 Sprint planning | Order sprint work | **`github-backlog-manager`**, `agile-coach`* | Milestone / sprint board |
| 6 Implementation | Build a feature slice | **`RPI Agent`** or `/rpi-*` | Code + `.copilot-tracking/` |
| 7 Review | Accept vs plan/AC | `/rpi-review`, **`code-review`** | Review logs / PR feedback |
| 7 Review | Security on changes | `security-reviewer` | Security findings |
| 8 Delivery | Commit / PR / merge | git prompts (`/git-commit`, PR prompts) | PR, merge, tag |
| 9 Operations | Docs + incident practice | **`documentation`**, incident-response prompts | Runbook / incident notes |

\*If `agile-coach` is not in your picker, use `github-backlog-manager` + `product-manager-advisor` for prioritization help.

## Full map: stage → agents (hve-core-all)

| Stage | Name | Agents / skills commonly used | Job in one line |
| --- | --- | --- | --- |
| 1 | Setup | `hve-core-installer` | Get HVE into the workspace |
| 2 | Discovery | `brd-builder`, `dt-coach`, `/rpi-research`, `security-planner`, `sssc-planner`, `rai-planner`, `gen-data-spec`, `experiment-designer`, `meeting-analyst` | Learn problem, constraints, risks |
| 3 | Product definition | `prd-builder`, `product-manager-advisor`, `adr-creation`, `architecture-diagrams`, `system-architecture-reviewer`, `ux-ui-designer`, security/RAI planners | Define product + decisions |
| 4 | Decomposition | `github-backlog-manager`, `ado-prd-to-wit`, `jira-prd-to-wit` / `jira-backlog-manager` | Turn specs into work items |
| 5 | Sprint planning | `github-backlog-manager`, `ado`/`jira` backlog managers, agile coaching assets | Sequence what we do now |
| 6 | Implementation | **`RPI Agent`**, `/rpi-plan`, `/rpi-implement`, coding-standards instructions, data-science generators if needed, `hve-builder` for custom AI artifacts | Change the product with evidence |
| 7 | Review | `/rpi-review`, `code-review`, `security-reviewer` | Decide accept / rework |
| 8 | Delivery | git commit/merge/PR prompts, `ado` build-info prompts | Land the change |
| 9 | Operations | `documentation`, incident-response prompts, `hve-builder` | Keep it runnable and maintainable |

## Full map: job → agent

| If your job is… | Use | Not this |
| --- | --- | --- |
| Write business requirements | `brd-builder` | `RPI Agent` |
| Write product/feature requirements | `prd-builder` | `brd-builder` (wrong altitude) |
| Coach prioritization / story quality | `product-manager-advisor` | jumping straight to code |
| Record an architecture choice | `adr-creation` | burying the decision in chat |
| Draw system structure | `architecture-diagrams` skill | `RPI Agent` |
| Review a design for trade-offs | `system-architecture-reviewer` | `code-review` |
| Discover users/problems (DT) | `dt-coach` | inventing personas in a BRD alone |
| Research a tech unknown | `/rpi-research` | implementing while researching |
| Plan then build a code change | `RPI Agent` or `/rpi-*` | `brd-builder` / `prd-builder` |
| Challenge assumptions hard | `rpi-challenger` skill | polite rubber-stamping |
| Create/triage GitHub issues | `github-backlog-manager` | manual-only with no AC |
| Pre-PR multi-perspective review | `code-review` | asking RPI to “just ship it” |
| Security model / standards plan | `security-planner` | only running `security-reviewer` later |
| Review code for vulns | `security-reviewer` | `security-planner` (different phase) |
| Supply-chain posture | `sssc-planner` | ad-hoc dependency guesses |
| Responsible AI assessment | `rai-planner` | skipping if the product uses AI |
| Docs audit/author/validate | `documentation` | one-off README edits with no pass |
| Author new HVE prompts/agents | `hve-builder` skill | hand-editing without gates |
| Data dictionary / notebook / Streamlit | `gen-data-spec`, `gen-jupyter-notebook`, `gen-streamlit-dashboard` | forcing RPI for analytics apps blindly |

## RPI Agent vs builders (remember this)

```text
brd-builder / prd-builder / adr-creation
    → define WHAT and WHY (planning docs)

RPI Agent
    → change HOW in the repo (code + tracking evidence)
```

## Skills you will see that are not agents

| Skill / prompt | Job |
| --- | --- |
| `/rpi-research` | Read-only evidence gathering |
| `/rpi-plan` | Implementation strategy + critique |
| `/rpi-implement` | Execute approved plan |
| `/rpi-review` | Acceptance reconciliation |
| `/rpi` or `/rpi-quick` | Full lifecycle entry without picking RPI Agent |
| `architecture-diagrams` | Diagram generation |
| `hve-builder` | Build/improve HVE AI artifacts |
| git commit / PR / merge prompts | Delivery mechanics |

## For this course right now

**Stage 2 Discovery → job = business requirements → agent = `brd-builder`.**
