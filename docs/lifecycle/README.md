# Lifecycle artifacts

Each project stage has an **input** folder (what you feed the work) and an **output** folder (what that stage produces).

| Stage | Folder | Typical inputs | Typical outputs |
| --- | --- | --- | --- |
| 1 Setup | `01-setup/` | Tooling notes, env checklist | Confirmed setup notes (optional) |
| 2 Discovery | `02-discovery/` | MVP framing, research notes | `brd.md` |
| 3 Product definition | `03-product-definition/` | BRD (copy or link from discovery output) | `prd.md`, `adr/` |
| 4 Decomposition | `04-decomposition/` | PRD | Issue export / backlog snapshot |
| 5 Sprint planning | `05-sprint-planning/` | Issue list | Sprint 1 / Sprint 2 plan |
| 6 Implementation | `06-implementation/` | Issue + AC, approved plan pointers | Notes; **code** lives in `src/pulseboard/`; RPI evidence in `.copilot-tracking/` |
| 7 Review | `07-review/` | Plan + changes pointers, AC | Review summary |
| 8 Delivery | `08-delivery/` | Accepted review | PR / release notes |
| 9 Operations | `09-operations/` | Shipped app behavior | `runbook.md` |

Convention: stage *N* output often becomes stage *N+1* input (copy, move, or reference the path in the next prompt).
