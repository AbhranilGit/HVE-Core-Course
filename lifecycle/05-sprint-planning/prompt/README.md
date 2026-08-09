# Stage 5 — Sprint planning prompt

| | |
| --- | --- |
| **Input** | Open PulseBoard GitHub issues; [`../../04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) |
| **Output** | [`../output/sprint-plan.md`](../output/sprint-plan.md) |

---

## 1. Agent

**`github-backlog-manager`**

Select in GitHub Copilot Chat → agent / mode picker.  
Optional helper: `product-manager-advisor` for prioritization advice only.  
Do **not** use RPI Agent for this step.

Before sending: attach / `#`-reference `lifecycle/04-decomposition/output/backlog-snapshot.md`  
(and the open GitHub issues / repo context if available).

---

## 2. Prompt

```text
Using the open PulseBoard GitHub issues and the Stage 4 backlog snapshot,
propose Sprint 1 and Sprint 2.

Authoritative sources:
- lifecycle/04-decomposition/output/backlog-snapshot.md
- Open GitHub issues in this repository
(attach / #reference the snapshot; use live issue list).

Workflow:
- Order work from the existing backlog only; do not invent new features.
- Only ask me when issue scope or dependencies are ambiguous.
- Sprint 1 must be a thin vertical slice: a user can post doing/blocked/next
  and see it on today's board.
- Push polish, extra tests, and docs to Sprint 2 (or later) unless required
  for the Sprint 1 slice to work.

Return:
- Ordered issue list for Sprint 1
- Ordered issue list for Sprint 2
- Brief rationale for the split and any dependencies

Do not implement application code in this step.
Do not create new issues unless a true gap blocks the thin slice
(ask first before creating).

Save the sprint plan to:
lifecycle/05-sprint-planning/output/sprint-plan.md
```
