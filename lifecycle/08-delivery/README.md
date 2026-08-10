# Stage 8 — Delivery

Ship it into the customer's world, through the customer's process.

| | |
| --- | --- |
| **Reads** | The Stage 7 reviews and the code on your branch |
| **Produces** | Release evidence, a merged pull request, a tag, and release notes in `docs/releases/` |
| **Commands** | `/ado-create-pull-request` or `/pull-request`, the `PR Review` helper, and `/git-merge` |

Do **A**, then **B**, then **C**, then **D**.

---

## 1. What this stage is for

You have working, reviewed code on a branch. This stage gets it into their main branch and their environment, with a record of what shipped.

Two things make this different from releasing your own product.

**Their process wins.** Whatever this page says, the customer has a way of merging and releasing, and it may involve approvers you do not control, a change advisory board, a release window, or a pipeline you cannot see. Find that out in Stage 1, not now. This page describes the shape of the work; their process determines the mechanics.

**The pull request is where enablement actually happens.** This is the most underrated point in the whole template. A pull request is the one artefact the customer's engineers are already obliged to read, and it arrives in their normal workflow rather than in a training session they have to attend.

A description that explains what changed, why this approach, what was considered and rejected, and how it was verified teaches more than a handover deck — because it is read in context, by people who need to understand it right now. Write every pull request as though the reader will maintain this code after you have gone, because they will.

That also means **their engineers should be the reviewers**, not just approvers. If you are merging your own pull requests unopposed, the code may be fine but the handover has already failed and nobody has told you yet.

## 2. Prerequisites

- Your Stage 7 reviews exist under `docs/reviews/` and every defect has a decision
- The code runs and the tests pass
- Your work is committed to your branch
- You know the customer's merge requirements: who approves, which checks must pass, whether there is a release window

## 3. Versioning

This kit tags `v0.1.0` for the first release and moves up from there. Use the customer's scheme instead if they have one — matching their existing tags matters more than consistency with this template.

Whatever you use, put the engagement name in the annotated tag message. Two years from now, someone reading `git log` should be able to tell which commits came from this engagement without asking anyone.

---

## A. Write the release evidence

Use the default Copilot Chat.

```text
Create a release evidence record for version v0.1.0.

Read from the workspace:
- The PRD in docs/prds/
- docs/planning/sprint-plan.md
- docs/reviews/ (every review file present)
- lifecycle/06-implementation/task-log.md
- lifecycle/00-engagement/engagement-brief.md, for the exit criteria
- .github/copilot-instructions.md, for the test command

Build the record from this repository's own material:
1) One row per acceptance criterion in the PRD, with where the evidence for it
   lives and whether it passed.
2) The out-of-scope items from lifecycle/02-discovery/scope-framing.md, each
   confirmed absent.
3) A test run record: the exact command used, the result, and when it was run.
   Read existing evidence first; only re-run tests if there is no record.
4) The outcome of every required review: code, and where they apply, security
   and responsible AI.
5) Which engagement exit criteria this release contributes to, and which remain
   outstanding.
6) A sign-off line for me and one for the customer's technical contact.
7) The candidate commit, the branch name, and the date, from the current git
   state.

Tick a box only where the evidence supports it. Where something is missing,
leave it unticked and say what is blocking it. Do not invent evidence. Do not
change application code.

Save to:
docs/releases/v0.1.0-release-evidence.md
```

**You should see:** `docs/releases/v0.1.0-release-evidence.md`

Read it. Any unticked box is a decision to make before releasing, and on customer work it is a decision to make **with** them rather than for them.

---

## B. Open the pull request

For Azure DevOps, use the tracker's own command — it discovers the related work items and suggests reviewers from the code's history, which saves you guessing at who should look at it:

```text
/ado-create-pull-request

Create the pull request for the v0.1.0 release.

Read from the workspace:
- docs/reviews/ (every review file)
- docs/releases/v0.1.0-release-evidence.md
- docs/planning/sprint-plan.md
- lifecycle/02-discovery/scope-framing.md
- docs/decisions/, for the decisions in force

Link every work item this branch delivers.

Write the description for the customer's engineers, who will maintain this after
I leave. It must cover:
- What shipped, in plain language, from the sprint plan's definition of done
- Why it was built this way, citing the relevant decision records, including any
  approach considered and rejected
- Where it deliberately follows an existing pattern in this codebase, and where
  it departs from one and why
- How it was validated: the test run plus the Stage 7 review outcomes
- What is deliberately out of scope, from the scope framing

Suggest reviewers from the customer's team based on who has touched this code.

Use the current branch and its real commits; do not invent history.

Do not merge and do not tag in this step.
```

On GitHub, use `/pull-request branch=origin/main createPullRequest=true` with the same body. Leave `createPullRequest` off if you would rather draft the description and open it yourself.

**You should see:** a pull request with linked work items. Note the URL.

Then do the part no command does for you: **ask a named customer engineer to review it**, and give them enough time to actually read it. If they only ever rubber-stamp, say so out loud at the next demo — it is an early warning that handover will not land, and it is much cheaper to fix in week three than week ten.

---

## C. Review the pull request

There is no slash command for this one. Clear the chat, choose <mark>**PR Review**</mark> from the mode dropdown, and describe the pull request you opened.

```text
Review the open pull request for the v0.1.0 release on this branch.

Read for context:
- docs/releases/v0.1.0-release-evidence.md
- docs/reviews/ (every review file)
- docs/decisions/, for the decisions and inherited constraints in force
- .github/copilot-instructions.md, for this project's conventions

Check the diff that is actually about to merge, not the repository as a whole.
Flag anything that drifted in after the Stage 7 reviews were written, and
anything the diff touches that no work item asked for.

Also tell me whether the description would make sense to an engineer on the
customer's team who has not been part of this work. Where it would not, say
which part needs explaining.

Do not merge, do not tag, and do not implement fixes unless I ask.
```

`PR Review` builds a reference for the pull request, keeps a living review document under `.copilot-tracking/pr/review/<branch>/`, and finishes with a handoff file of recommended comments and decisions. It is the same family of checks as Stage 7, scoped to exactly the diff about to merge, which is why it catches late drift the earlier review could not.

This does not replace the customer's review. Run it first so that what they receive is already clean, and their attention goes on the design rather than on typos.

If their pipeline runs builds on the pull request, `/ado-get-build-info` pulls the build result and logs into `.copilot-tracking/pr/` so you can diagnose a failure without leaving the editor.

---

## D. Merge, tag, and write the release notes

Only after their approvals are in and their checks are green.

```text
/git-merge

Complete the v0.1.0 release.

Read from the workspace:
- docs/releases/v0.1.0-release-evidence.md
- docs/reviews/ (every review file)
- docs/operations/runbook.md, if it exists

Tasks:
1) Confirm the release evidence sign-off is complete. If it is not, stop and
   tell me exactly what is missing.
2) Merge the approved pull request into the default branch.
3) Create an annotated tag v0.1.0 on the merged release commit. Include the
   engagement name in the tag message.
4) Write release notes covering:
   - What this version can do
   - How it was validated: the test run and the Stage 7 reviews
   - What is explicitly not included, from the scope framing's out-of-scope list
   - Any known defect accepted as will-not-fix, so it is not a surprise later
   - A pointer to docs/operations/runbook.md for how to run it
   - The tag name and the commit it points at

Write the notes for the customer, not for me.

Do not add features. If a v0.1.0 tag already exists, stop and ask me before
moving it.

Save the release notes to:
docs/releases/v0.1.0-release-notes.md
```

`/git-merge` handles merge, rebase, and conflict workflows with standard stop points, so expect it to pause and ask rather than force anything through. If the customer requires squash merges or a particular commit message format, say so in the prompt.

**You should see:** `docs/releases/v0.1.0-release-notes.md`, and `git tag` listing `v0.1.0`.

---

## 4. If a helper asks you a question

Anything about evidence comes from the reviews and the test record. Anything about whether to release despite an unticked box is a judgement call — and on customer work it is a shared one. Write the reasoning and who agreed into the evidence record.

## 5. Done when

- `docs/releases/v0.1.0-release-evidence.md` is filled in, with any blockers written down
- The pull request was reviewed by someone on the customer's team, not only by you
- The description explains the reasoning, not just the change
- It is merged through their process, with their checks passing
- `git tag` lists the release, and the tag message names the engagement
- `docs/releases/v0.1.0-release-notes.md` exists and is written for them

**Next:** [Stage 9 — Handover](../09-operations/README.md) — the one that decides whether any of this survives.

---

## Between iterations

Delivery loops back to implementation. Most engagements come through this stage several times — once per iteration if the customer will take incremental releases, which is worth pushing for. A first merge in week two, however small, surfaces every process obstacle while there is still time to route around it.

If this release was not the last, go to [Stage 6](../06-implementation/README.md) with the next iteration's tasks and come back here when it is done. Reach Stage 9 only in your final iteration.
