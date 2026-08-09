# Stage 4 — Decomposition

Break your features into small tasks that can each be finished in one sitting.

| | |
| --- | --- |
| **Reads** | [`../03-product-definition/output/prd.md`](../03-product-definition/output/prd.md) and [`../03-product-definition/output/adr/`](../03-product-definition/output/adr/) |
| **Produces** | GitHub issues, plus [`output/backlog-snapshot.md`](output/backlog-snapshot.md) |
| **Helper** | `github-backlog-manager` |

---

## 1. What this stage is for

A feature like "users can save their work" is too big to build in one go. This stage chops your PRD into **issues** — small tasks, each with its own acceptance criteria, tracked on GitHub.

It also saves a **backlog snapshot**: the same list written into a file in this repository. That matters, because later stages read the snapshot from your workspace rather than needing access to GitHub.

## 2. Prerequisites

- `lifecycle/03-product-definition/output/prd.md` exists, with acceptance criteria
- Your ADRs exist under `lifecycle/03-product-definition/output/adr/`
- **This repository exists on GitHub and you are signed in.** The helper creates issues there. If your project is only on your laptop, either push it to GitHub now, or read the fallback in section 6.

## 3. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`github-backlog-manager`**.

Do **not** use `RPI Agent`, `prd-builder`, or `brd-builder` here.

## 4. Paste this prompt

```text
From the accepted PRD in this workspace, create GitHub issues for the first
version's backlog.

Read from the workspace:
- lifecycle/03-product-definition/output/prd.md
- lifecycle/03-product-definition/output/adr/ (for decisions already locked)

Do not ask me to attach these files.

Workflow:
- Derive issues from the PRD's user stories and acceptance criteria.
- Only ask me where the PRD or ADRs are silent or ambiguous.
- Do not invent anything outside the PRD's in-scope list.
- Keep each issue small enough to finish in one working session.
- Prefer an order that builds one thin end-to-end path first, rather than many
  half-finished layers.

Each issue must have:
- A clear title
- Acceptance criteria, traceable back to the PRD acceptance criteria ids
- One label describing its kind (for example api, ui, auth, docs, or tests)

Do not write application code in this step.
Do not decide sprint order yet — that is the next stage.

Also write a backlog snapshot listing every issue you created, with its number,
title, acceptance criteria, and label, to:
lifecycle/04-decomposition/output/backlog-snapshot.md
```

## 5. What you should see afterwards

- Issues listed on your repository's GitHub **Issues** tab
- A new file at **`lifecycle/04-decomposition/output/backlog-snapshot.md`**

Skim the snapshot. Somewhere between five and fifteen issues is normal for a first version. If you see forty, the issues are too small or scope has crept — say so and ask it to consolidate.

Leave the issues open for now. Stage 6 closes each one as its task is built and tested, recording the evidence in the comment.

## 6. If the helper asks you a question

Answer from the PRD. If it cannot reach GitHub, or you are not using GitHub, reply:

```text
Skip creating issues on GitHub. Write the full backlog to
lifecycle/04-decomposition/output/backlog-snapshot.md instead, numbering each item
TEMP-1, TEMP-2 and so on. Later stages will use the snapshot as the source of truth.
```

The rest of the kit works fine from the snapshot alone.

## 7. Done when

- `lifecycle/04-decomposition/output/backlog-snapshot.md` exists
- Every item has acceptance criteria, not just a title
- You can see how the items add up to your PRD, with nothing extra
- Each item looks like something that could be finished in a day or less

**Next:** [Stage 5 — Sprint planning](../05-sprint-planning/README.md)
