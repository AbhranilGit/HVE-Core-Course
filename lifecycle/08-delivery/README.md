# Stage 8 — Delivery

Publish your first release.

| | |
| --- | --- |
| **Reads** | Your Stage 7 reviews and the code on your branch |
| **Produces** | Release evidence, a merged pull request, the tag `v0.1.0`, and release notes in `docs/releases/` |
| **Commands** | `/pull-request` and `/git-merge`, plus the `PR Review` helper |

Do **A**, then **B**, then **C**, then **D**.

---

## 1. What this stage is for

You have working, reviewed code. This stage makes it an actual release:

- **Release evidence** recording that it is ready — which tests ran, which criteria passed, who signed it off
- A **pull request**, which is a request to merge your work into the main branch, giving anyone a place to review it
- A **tag**, a permanent label on this exact version of the code so you can always come back to it. Your first release is `v0.1.0`
- **Release notes** saying what shipped, how it was checked, and what was deliberately left out

If you are working alone, the pull request may feel like a formality. Do it
anyway — it is the record of what you shipped and why.

## 2. Prerequisites

- Your Stage 7 reviews exist under `docs/reviews/` and every defect has a decision
- The code runs and your tests pass
- Your work is committed to your branch

---

## A. Write the release evidence

Use the default Copilot Chat.

```text
Create a release evidence record for version v0.1.0 of this product.

Read from the workspace:
- The PRD in docs/prds/
- docs/planning/sprint-plan.md
- docs/reviews/ (every review file present)
- lifecycle/06-implementation/task-log.md
- .github/copilot-instructions.md, for the test command

Build the record from this repository's own material:
1) One row per acceptance criterion in the PRD, with where the evidence for it
   lives and whether it passed.
2) The out-of-scope items from lifecycle/02-discovery/mvp-framing.md, each
   confirmed absent.
3) A test run record: the exact command used, the result, and when it was run.
   Read existing evidence first; only re-run tests if there is no record.
4) A reviewer sign-off line.
5) The candidate commit, the branch name, and the date, taken from the current
   git state.

Tick a box only where the evidence supports it. Where something is missing,
leave it unticked and say what is blocking it. Do not invent evidence. Do not
change application code.

Save to:
docs/releases/v0.1.0-release-evidence.md
```

**You should see:** `docs/releases/v0.1.0-release-evidence.md`

Read it. Any unticked box is a decision you need to make before releasing.

---

## B. Open the pull request

```text
/pull-request branch=origin/main createPullRequest=true

Create the pull request for the v0.1.0 release of this product.

Read from the workspace:
- docs/reviews/ (every review file)
- docs/releases/v0.1.0-release-evidence.md
- docs/planning/sprint-plan.md
- lifecycle/02-discovery/mvp-framing.md

The description must state:
- What shipped, in plain language, from the sprint plan's definition of done
- How it was validated: the test run plus the Stage 7 review outcomes, citing
  the review files by path
- What is deliberately out of scope for this release, taken from the framing

Use the current branch and its real commits; do not invent history. Open the
pull request against this repository's default branch.

Do not merge and do not tag in this step. Do not start new features.
```

Change `origin/main` to whatever your default branch is called. Leave
`createPullRequest=true` off if you only want the description drafted and would
rather open the pull request yourself.

**You should see:** a pull request, and its URL in the chat. Note the URL down.

Not using a hosted tracker? Skip to part D and merge your branch locally.

---

## C. Review the pull request

There is no slash command for this one. Clear the chat, then choose **`PR Review`**
from the mode dropdown and describe the pull request you just opened.

```text
Review the open pull request for the v0.1.0 release on this branch.

Read for context:
- docs/releases/v0.1.0-release-evidence.md
- docs/reviews/ (every review file)
- docs/decisions/, for the technical decisions in force
- .github/copilot-instructions.md, for this project's conventions

Check the diff that is actually about to merge, not the repository as a whole.
Flag anything that drifted in after the Stage 7 reviews were written.

Do not merge, do not tag, and do not implement fixes unless I ask.
```

`PR Review` builds a reference for the pull request, keeps a living review
document under `.copilot-tracking/pr/review/<branch>/`, and finishes with a
handoff file of the comments and decisions it recommends. It is the same family
of checks as Stage 7 part C, but scoped to exactly the diff you are about to
merge — which is why it catches late drift that the earlier review could not.

Address anything it raises before merging, or record why you are not going to.

---

## D. Merge, tag, and write the release notes

Do this only after the pull request is approved — or, if you are working alone,
after you have read your own evidence record and are satisfied.

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
3) Create an annotated git tag v0.1.0 on the merged release commit.
4) Write release notes covering:
   - What this version can do
   - How it was validated: the test run and the Stage 7 reviews
   - What is explicitly not included, from the framing's out-of-scope list
   - A pointer to docs/operations/runbook.md for how to run it
   - The tag name and the commit it points at

Do not add features. If a v0.1.0 tag already exists, stop and ask me before
moving it.

Save the release notes to:
docs/releases/v0.1.0-release-notes.md
```

`/git-merge` handles merge, rebase, and conflict workflows with standard stop
points, so expect it to pause and ask rather than force anything through.

**You should see:** `docs/releases/v0.1.0-release-notes.md`, and `git tag`
listing `v0.1.0`.

---

## 3. If a helper asks you a question

Anything about evidence comes from the reviews and the test record. Anything
about whether to release despite an unticked box is your judgement — write your
reasoning into the evidence record so the decision survives.

## 4. Done when

- `docs/releases/v0.1.0-release-evidence.md` is filled in, with any blockers written down
- The pull request is created, reviewed, and merged — or your branch is merged
- `git tag` lists `v0.1.0`
- `docs/releases/v0.1.0-release-notes.md` exists

**Next:** [Stage 9 — Operations](../09-operations/README.md) — the last one.

---

## Starting the next sprint instead?

Delivery loops back to implementation. If this release was not the final one, go
to [Stage 6](../06-implementation/README.md) with the next sprint's tasks rather
than continuing to Stage 9. Come back here when the sprint is done.
