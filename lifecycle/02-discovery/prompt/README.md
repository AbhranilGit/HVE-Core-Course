# Stage 2 — Discovery prompt

| | |
| --- | --- |
| **Input** | [`../input/mvp-framing.md`](../input/mvp-framing.md) |
| **Output** | [`../output/brd.md`](../output/brd.md) |

---

## 1. Agent

**`brd-builder`**

Select in GitHub Copilot Chat → agent / mode picker.  
Do **not** use RPI Agent or `prd-builder` for this step.

Before sending: attach / `#`-reference `lifecycle/02-discovery/input/mvp-framing.md`.

---

## 2. Prompt

```text
Create a business requirements document (BRD) for PulseBoard.

Authoritative source: lifecycle/02-discovery/input/mvp-framing.md
(attach / #reference this file).

Workflow:
- Use the framing to answer Discover / Define questions yourself.
- Only ask me when the framing is silent or ambiguous.
- Derive assumptions and risks from the framing; do not invent new scope.
- Keep open questions that the framing already lists; add new ones only if needed.

Produce a BRD with: problem statement, stakeholders, in/out of scope,
success metrics, assumptions, risks, and open questions.

Do not write a PRD, acceptance criteria, ADRs, tickets, or application code.
Do not widen MVP beyond the framing's in-scope list.

Save the finished BRD to:
lifecycle/02-discovery/output/brd.md
```
