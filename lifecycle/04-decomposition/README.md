# Stage 4 — Decomposition

Break your features into small tasks that can each be finished in one sitting.

| | |
| --- | --- |
| **Reads** | Your PRD in `docs/project-planning/` and your ADRs in `docs/planning/adrs/` |
| **Produces** | Work items in your tracker |
| **Helper** | `GitHub Backlog Manager`, or the equivalent for your tracker |

---

## 1. What this stage is for

A feature like "users can save their work" is too big to build in one go. This
stage chops your PRD into **work items** — small tasks, each with its own
acceptance criteria, tracked wherever your team tracks work.

Each task keeps the id of the PRD acceptance criterion it came from. That thread
is what lets Stage 7 ask "did we build what we promised?" and get an honest
answer.

## 2. Choose your tracker

This is the first stage where it matters. Pick one and use the same one in
Stages 5 and 8.

| Your tracker | Helper to select | Where its notes go |
| --- | --- | --- |
| **GitHub Issues** | `GitHub Backlog Manager` | `.copilot-tracking/github-issues/` |
| **Azure DevOps** | `ado-prd-to-wit` to plan, then the ADO prompts to create | `.copilot-tracking/` |
| **Jira** | `Jira Backlog Manager` | `.copilot-tracking/` |
| **None** | Any helper — see section 6 | A file you keep in the repo |

The rest of this page is written for GitHub because that is the most common
choice. For Azure DevOps or Jira, swap the helper name and the word "issue" for
"work item"; everything else is the same.

## 3. Prerequisites

- Your PRD exists under `docs/project-planning/`, with acceptance criteria that have ids
- Your ADRs exist under `docs/planning/adrs/`
- **Your repository exists on your tracker and you are signed in.** The helper creates the items there. If your project is only on your laptop, read the fallback in section 6.

## 4. Pick the helper

1. Open Copilot Chat.
2. Click the mode dropdown at the bottom of the chat box.
3. Choose **`GitHub Backlog Manager`**.

Do **not** use `RPI Agent`, `PRD Builder`, or `BRD Builder` here.

## 5. Paste this prompt

```text
From the accepted PRD in this workspace, create the backlog for the first
version.

Read from the workspace:
- The PRD in docs/project-planning/
- docs/planning/adrs/, for decisions already locked
- .github/ISSUE_TEMPLATE/task.md, for the shape each issue should take

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
- Acceptance criteria that cite the PRD acceptance criterion ids they come from
- One label describing its kind, for example api, ui, auth, docs, or tests

Do not write application code in this step.
Do not decide sprint order yet — that is the next stage.

When you are done, list every issue you created with its number, title, and
label, so I can check the set against the PRD.
```

## 6. What you should see afterwards

Issues on your repository's **Issues** tab, and a summary of them in the chat.

Somewhere between five and fifteen issues is normal for a first version. If you
see forty, the issues are too small or scope has crept — say so and ask it to
consolidate.

Leave the issues open for now. Stage 6 closes each one as its task is built and
tested, with the evidence in the comment.

The helper keeps its own working notes under
`.copilot-tracking/github-issues/`. You do not need to open them, but Stage 5
reads them.

### Not using a tracker?

Reply to the helper:

```text
Skip creating issues in a tracker. Write the full backlog to docs/backlog.md
instead, numbering each item TASK-01, TASK-02 and so on, each with its title,
acceptance criteria citing the PRD ids, and its label. Later stages will use
that file as the source of truth.
```

The rest of the kit works from that file. Wherever a later stage says "the
issue", read "the entry in `docs/backlog.md`".

## 7. If the helper asks you a question

Answer from the PRD. Questions about how you want work labelled or grouped are
yours to answer.

## 8. Done when

- Every task exists in your tracker, or in `docs/backlog.md`
- Every item has acceptance criteria, not just a title
- Each acceptance criterion cites the PRD id it came from
- You can see how the items add up to your PRD, with nothing extra
- Each item looks like something that could be finished in a day or less

**Next:** [Stage 5 — Sprint planning](../05-sprint-planning/README.md)
