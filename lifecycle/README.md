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
| 7 Review | `07-review/` | Sprint plan + Stage 6 evidence + code; prompts in `prompt/` | `output/sprint-1-rpi-review.md`, `output/sprint-2-rpi-review.md`, `output/sprint-1-code-review.md` |
| 8 Delivery | `08-delivery/` | Accepted Stage 7 reviews; prompts in `prompt/` | checklist sign-off; PR/merge/tag `v0.1.0`; `output/v0.1.0-release-notes.md` |
| 9 Operations | `09-operations/` | Shipped app + Stage 8 notes; prompts in `prompt/` | `output/runbook.md`; optional `output/ops-confirmation.md` |

Convention: stage *N* output often becomes stage *N+1* input (copy, move, or reference the path in the next prompt).
