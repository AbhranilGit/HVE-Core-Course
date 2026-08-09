# Stage 3 — Product definition prompts

| | |
| --- | --- |
| **Input** | [`../../02-discovery/output/brd.md`](../../02-discovery/output/brd.md) (Accepted) |
| **Outputs** | [`../output/prd.md`](../output/prd.md); ADRs under [`../output/adr/`](../output/adr/) |

Run **PRD first**, then **ADRs**. Optional architecture diagram last.

---

## A. PRD

### 1. Agent

**`prd-builder`**

Select in GitHub Copilot Chat → agent / mode picker.  
Do **not** use RPI Agent or `brd-builder` for this step.

Before sending: attach / `#`-reference `lifecycle/02-discovery/output/brd.md`.

### 2. Prompt

```text
Create a Product Requirements Document (PRD) for PulseBoard MVP.

Authoritative source: lifecycle/02-discovery/output/brd.md
(attach / #reference this file).

Workflow:
- Use the accepted BRD to answer product-definition questions yourself.
- Only ask me when the BRD is silent or ambiguous.
- Stay within the BRD in-scope list; treat out-of-scope as excluded.
- Carry forward open questions that need product decisions; do not invent new MVP features.

Produce a PRD with user stories and clear acceptance criteria for the MVP
capabilities defined in the BRD.

Do not write ADRs, GitHub issues, sprint plans, or application code in this step.
Do not widen MVP beyond the BRD in-scope list.

Save the finished PRD to:
lifecycle/03-product-definition/output/prd.md
```

---

## B. ADRs

### 1. Agent

**`adr-creation`**

Select in GitHub Copilot Chat → agent / mode picker.  
Run after the PRD exists (or at least after BRD acceptance).  
Do **not** use RPI Agent for this step.

Before sending: attach / `#`-reference the accepted BRD and, if available, the PRD.

### 2. Prompt

```text
Create architecture decision records (ADRs) for PulseBoard MVP.

Authoritative sources:
- lifecycle/02-discovery/output/brd.md
- lifecycle/03-product-definition/output/prd.md (if present)
(attach / #reference these files).

Decide only what the BRD/PRD leave open and what MVP constraints require
(for example identity model and local datastore). Record context, decision,
consequences, and when to revisit.

Do not expand product scope. Do not write application code or tickets.

Save ADRs under:
lifecycle/03-product-definition/output/adr/
```

---

## Optional — architecture diagram

**Skill:** `architecture-diagrams`  
Save under `lifecycle/03-product-definition/output/` after PRD/ADRs stabilize.
