# Stage 4 — Decomposition

Break your features into small tasks that can each be finished in one sitting.

| | |
| --- | --- |
| **Reads** | Your PRD in `docs/prds/` and your decision records in `docs/decisions/` |
| **Produces** | Work items in your tracker |
| **Commands** | `/github-discover-issues`, then `/github-execute-backlog` |

---

## 1. What this stage is for

A feature like "users can save their work" is too big to build in one go. This
stage chops your PRD into **work items** — small tasks, each with its own
acceptance criteria, tracked wherever your team tracks work.

Each task keeps the id of the PRD acceptance criterion it came from. That thread
is what lets Stage 7 ask "did we build what we promised?" and get an honest
answer.

The work happens in two steps, and the gap between them is deliberate. First the
helper **proposes** a backlog and writes it to a plan file. You read that file.
Only then does a second command actually create the issues. Nothing is written to
your tracker until you have seen the list.

## 2. Choose your tracker

This is the first stage where it matters. Pick one and use the same one in
Stages 5 and 8.

| Your tracker | Helper | Its commands |
| --- | --- | --- |
| **GitHub Issues** | `GitHub Backlog Manager` | `/github-discover-issues`, `/github-execute-backlog`, `/github-add-issue`, `/github-triage-issues` |
| **Azure DevOps** | `ADO Backlog Manager`, or `AzDO PRD to WIT` to plan the hierarchy first | `/ado-discover-work-items`, `/ado-add-work-item`, `/ado-triage-work-items` |
| **Jira** | `Jira Backlog Manager`, or `Jira PRD to WIT` | `/jira-discover-issues`, `/jira-execute-backlog`, `/jira-triage-issues` |
| **None** | Any helper — see section 6 | A file you keep in the repo |

The rest of this page is written for GitHub because that is the most common
choice. For Azure DevOps or Jira, swap the command names and read "work item"
for "issue"; the shape of the stage is the same.

## 3. Prerequisites

- Your PRD exists under `docs/prds/`, with acceptance criteria that have ids
- Your decision records exist under `docs/decisions/`
- **Your repository exists on GitHub and you are signed in.** The helper works through the GitHub MCP tools, so the GitHub MCP server has to be connected in VS Code. If it is not, the helper will tell you it cannot reach your repository
- If your project is only on your laptop, read the fallback in section 6

## 4. Propose the backlog

Run this in Copilot Chat. The command brings `GitHub Backlog Manager` with it, so
you do not need the mode dropdown.

Replace `<name>` with your PRD's filename.

```text
/github-discover-issues documents=docs/prds/<name>.md

Propose the backlog for the first version of this product.

Also read from the workspace:
- docs/decisions/, for decisions already locked
- .github/ISSUE_TEMPLATE/task.md, for the shape each issue should take

Do not ask me to attach these files.

Workflow:
- Derive issues from the PRD's user stories and acceptance criteria.
- Only ask me where the PRD or the decision records are silent or ambiguous.
- Do not invent anything outside the PRD's in-scope list.
- Keep each issue small enough to finish in one working session.
- Prefer an order that builds one thin end-to-end path first, rather than many
  half-finished layers.

Each proposed issue must have:
- A clear title
- Acceptance criteria that cite the PRD acceptance criterion ids they come from
- One label describing its kind, for example api, ui, auth, docs, or tests

Do not create anything in GitHub yet, and do not write application code.
Do not decide sprint order — that is the next stage.
```

**You should see:** a tracking folder at
`.copilot-tracking/github-issues/discovery/<scope>/` containing
`issue-analysis.md` (what it found and what already exists),
`issues-plan.md` (the proposed backlog), and `handoff.md` (the summary and what
to do next). The helper tells you the paths.

## 5. Read the plan, then create the issues

Open `issues-plan.md` and read it properly. This is the cheapest moment in the
whole kit to catch a problem.

Between five and fifteen issues is normal for a first version. Forty means the
issues are too small or scope has crept — say so in the chat and ask for a
consolidation before you go on.

When you are happy, create them:

```text
/github-execute-backlog handoff=.copilot-tracking/github-issues/discovery/<scope>/handoff.md autonomy=partial

Create the issues from the approved plan. Do not add anything that is not in it.

When you are done, list every issue you created with its number, title, and
label, so I can check the set against the PRD.
```

`autonomy=partial` pauses at review gates so you can watch what it does. Use
`full` once you trust it, or `manual` to approve every single operation. Adding
`dryRun=true` shows you what it would do without touching GitHub.

**You should see:** issues on your repository's Issues tab, a summary in the
chat, and an execution record under
`.copilot-tracking/github-issues/execution/<date>/`.

Leave the issues open for now. Stage 6 closes each one as its task is built and
tested, with the evidence in the comment.

### Not using a tracker?

Skip both commands. Use the default Copilot Chat instead:

```text
Read the PRD in docs/prds/ and docs/decisions/ from the workspace.

Write the full backlog for the first version to docs/backlog.md, numbering each
item TASK-01, TASK-02 and so on, each with its title, acceptance criteria citing
the PRD acceptance criterion ids, and its label. Keep each item small enough to
finish in one working session, and order them so one thin end-to-end path is
built first.

Do not invent anything outside the PRD's in-scope list. Do not write application
code.
```

The rest of the kit works from that file. Wherever a later stage says "the
issue", read "the entry in `docs/backlog.md`".

## 6. If the helper asks you a question

Answer from the PRD. Questions about how you want work labelled or grouped are
yours to answer.

## 7. Done when

- Every task exists in your tracker, or in `docs/backlog.md`
- Every item has acceptance criteria, not just a title
- Each acceptance criterion cites the PRD id it came from
- You can see how the items add up to your PRD, with nothing extra
- Each item looks like something that could be finished in a day or less

**Next:** [Stage 5 — Sprint planning](../05-sprint-planning/README.md)
