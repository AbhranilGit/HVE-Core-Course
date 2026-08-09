# Lifecycle artifacts

Each project stage has an **input** folder (what you feed the work) and an **output** folder (what that stage produces).

| Stage | Folder | Typical inputs | Typical outputs |
| --- | --- | --- | --- |
| 1 Setup | `01-setup/` | `input/setup-checklist.md` | `output/setup-confirmation.md` |
| 2 Discovery | `02-discovery/` | `input/mvp-framing.md`; agent + prompt in `prompt/` | `output/brd.md` |
| 3 Product definition | `03-product-definition/` | Accepted BRD from discovery; agent + prompts in `prompt/` | `output/prd.md`, `output/adr/`, optional architecture diagram |
| 4 Decomposition | `04-decomposition/` | Accepted PRD (+ ADRs); agent + prompt in `prompt/` | GitHub issues + `output/backlog-snapshot.md` |
| 5 Sprint planning | `05-sprint-planning/` | Backlog snapshot + open issues; agent + prompt in `prompt/` | `output/sprint-plan.md` |
| 6 Implementation | `06-implementation/` | One GitHub issue at a time; per-issue RPI prompts in `prompt/` | `output/issue-NN/{research,plan,implement}.md` + verify gate; **code** in `src/pulseboard/`; RPI in `.copilot-tracking/` |
| 7 Review | `07-review/` | Sprint plan + tracking evidence | `output/sprint-1-*-review.md` |
| 8 Delivery | `08-delivery/` | Accepted review | PR/merge/tag + `output/v0.1.0-release-notes.md` |
| 9 Operations | `09-operations/` | Shipped app behavior | `output/runbook.md` |

Convention: stage *N* output often becomes stage *N+1* input (copy, move, or reference the path in the next prompt).
