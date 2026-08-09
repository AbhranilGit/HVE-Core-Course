# Stage 4 — Decomposition prompt

| | |
| --- | --- |
| **Input** | [`../../03-product-definition/output/prd.md`](../../03-product-definition/output/prd.md) (Accepted); ADRs under [`../../03-product-definition/output/adr/`](../../03-product-definition/output/adr/) |
| **Outputs** | GitHub issues with labels + acceptance criteria; [`../output/backlog-snapshot.md`](../output/backlog-snapshot.md) |

---

## 1. Agent

**`github-backlog-manager`**

Select in GitHub Copilot Chat → agent / mode picker.  
Do **not** use RPI Agent, `prd-builder`, or `brd-builder` for this step.

Before sending: attach / `#`-reference `lifecycle/03-product-definition/output/prd.md`  
(optional: also reference `lifecycle/03-product-definition/output/adr/`).

---

## 2. Prompt

```text
From the accepted PulseBoard PRD, create GitHub issues for the MVP backlog.

Authoritative source: lifecycle/03-product-definition/output/prd.md
(attach / #reference this file).
Optional: lifecycle/03-product-definition/output/adr/ for locked decisions.

Workflow:
- Derive issues from PRD user stories and acceptance criteria.
- Only ask me when the PRD/ADRs are silent or ambiguous.
- Do not invent features outside the PRD in-scope / P0 set.
- Keep issues small enough to finish; prefer a thin vertical slice path.

Each issue must include:
- Clear title
- Acceptance criteria (traceable to PRD where practical)
- Label (api, ui, auth, docs, or tests)

Do not implement application code in this step.
Do not start sprint ordering yet (that is Stage 5).

Also write a backlog snapshot listing the created issues to:
lifecycle/04-decomposition/output/backlog-snapshot.md
```
