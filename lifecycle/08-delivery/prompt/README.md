# Stage 8 — Delivery prompts

| | |
| --- | --- |
| **Inputs** | Accepted Stage 7 reviews; [`../output/v0.1.0-release-evidence-checklist.md`](../output/v0.1.0-release-evidence-checklist.md); code on the release branch |
| **Outputs** | Checklist signed; PR merged; tag `v0.1.0`; [`../output/v0.1.0-release-notes.md`](../output/v0.1.0-release-notes.md) |

Order: **A (evidence checklist)** → **B (pull request)** → **C (merge + tag + notes)**.  
Do not invent product features in this stage.

---

## A. Finalize release evidence checklist

### 1. Agent

Default Copilot Chat (or **RPI Agent** if preferred).  
Do **not** use `prd-builder` / `brd-builder` here.

### 2. Prompt

```text
Finalize the PulseBoard v0.1.0 release evidence checklist for tagging.

Read from the workspace:
- lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
- lifecycle/07-review/output/sprint-1-rpi-review.md
- lifecycle/07-review/output/sprint-2-rpi-review.md
- lifecycle/07-review/output/sprint-1-code-review.md
- lifecycle/05-sprint-planning/output/sprint-plan.md
- lifecycle/03-product-definition/output/prd.md

Tasks:
1) Fill candidate commit SHA, branch, checklist owner, and review date from the current git state.
2) Fill AC-008.3 run record fields (exact pytest command(s), targeted/full results, timestamp, operator) by reading existing evidence under lifecycle/06-implementation/output/issue-10/ and/or re-running tests if needed.
3) Mark AC-008.1–AC-008.4 gate checkboxes only when evidence supports them; leave unchecked and explain if blocked.
4) Do not invent missing evidence. Do not change product code unless a checklist field requires a recorded command output you must generate.

Keep the AC-008.1 US-001–US-007 evidence index mapped to PRD meanings (do not regress the corrected labels).

Save updates in place to:
lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
```

---

## B. Create pull request

### 1. Agent

**`pull-request`** helper if available; otherwise default Copilot Chat / git PR workflow.  
Do **not** start new MVP features in the PR.

### 2. Prompt

```text
Create a pull request for PulseBoard MVP delivery toward tag v0.1.0.

Read from the workspace:
- lifecycle/07-review/output/sprint-1-rpi-review.md
- lifecycle/07-review/output/sprint-2-rpi-review.md
- lifecycle/07-review/output/sprint-1-code-review.md
- lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
- lifecycle/05-sprint-planning/output/sprint-plan.md

PR summary must include:
- What: local-first status board — display name, post doing/blocked/next, today's board
- How validated: tests + Stage 7 review outcomes (cite the review files)
- Out of scope for v0.1.0: SSO/OAuth, notifications/Slack, mobile, multi-tenant SaaS

Workflow:
- Use the current branch / commits; do not invent a fake history.
- Open or prepare the PR against the repo default branch.
- Do not merge or tag in this step.

If a PR URL is created, record it in:
lifecycle/08-delivery/output/v0.1.0-release-notes.md
under a "Pull request" section (create the file if needed).
```

---

## C. Merge, tag `v0.1.0`, and release notes

### 1. Agent

Default Copilot Chat / git helpers.  
Only after PR approval (or explicit owner approval on `master`/`main` if that is your process).

### 2. Prompt

```text
Complete PulseBoard v0.1.0 delivery after PR approval.

Read from the workspace:
- lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
- lifecycle/07-review/output/sprint-1-rpi-review.md
- lifecycle/07-review/output/sprint-2-rpi-review.md
- lifecycle/09-operations/output/runbook.md

Tasks:
1) Confirm AC-008.4 reviewer confirmation is Done (or stop and say what is missing).
2) Guide or perform merge of the approved PR into the default branch.
3) Create annotated git tag v0.1.0 on the merged release commit.
4) Write release notes covering:
   - MVP capabilities shipped
   - Validation summary (tests + Stage 7)
   - Explicit non-goals (SSO, notifications, mobile)
   - Pointer to runbook: lifecycle/09-operations/output/runbook.md
   - Tag name and commit SHA

Do not add product features. Do not retag if v0.1.0 already exists unless the user explicitly asks to move the tag.

Save release notes to:
lifecycle/08-delivery/output/v0.1.0-release-notes.md
```

---

## Done when

- [ ] Release evidence checklist filled and AC-008.1–AC-008.4 confirmed (or blockers listed)  
- [ ] PR created and merged (or equivalent approved merge to default branch)  
- [ ] Git tag `v0.1.0` exists on the release commit  
- [ ] `lifecycle/08-delivery/output/v0.1.0-release-notes.md` exists  
