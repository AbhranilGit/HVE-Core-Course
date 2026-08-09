# Stage 8 — Delivery

Publish your first release.

| | |
| --- | --- |
| **Reads** | Your Stage 7 reviews and the code on your branch |
| **Produces** | A release checklist, a merged pull request, the tag `v0.1.0`, and [`../output/v0.1.0-release-notes.md`](../output/v0.1.0-release-notes.md) |
| **Helpers** | Default Copilot Chat, and the `pull-request` helper if you have it |

Do **A**, then **B**, then **C**.

---

## 1. What this stage is for

You have working, reviewed code. This stage makes it an actual release:

- A **checklist** recording the evidence that it is ready — which tests ran, which criteria passed, who signed it off
- A **pull request**, which is a request to merge your work into the main branch, giving anyone a place to review it
- A **tag**, which is a permanent label on this exact version of the code so you can always come back to it. Your first release is `v0.1.0`
- **Release notes** saying what shipped, how it was checked, and what was deliberately left out

If you are working alone, the pull request may feel like a formality. Do it anyway — it is the record of what you shipped and why.

## 2. Before you start

- [ ] Your Stage 7 reviews exist and every defect has a decision
- [ ] The code runs and your tests pass
- [ ] Your work is committed to your branch

---

## A. Write the release checklist

Use the default Copilot Chat (or `RPI Agent`). Do **not** use `prd-builder` or `brd-builder` here.

```text
Create a release evidence checklist for version v0.1.0 of this product.

Read from the workspace:
- lifecycle/03-product-definition/output/prd.md
- lifecycle/05-sprint-planning/output/sprint-plan.md
- lifecycle/07-review/output/ (every review file present)
- lifecycle/06-implementation/output/ (for test and implementation evidence)

Build the checklist from this repository's own material:
1) One row per acceptance criterion in the PRD, with where the evidence for it
   lives and whether it passed.
2) The out-of-scope items from lifecycle/02-discovery/input/mvp-framing.md,
   each confirmed absent.
3) A test run record: the exact command used, the result, and when it was run.
   Read existing evidence first; only re-run tests if there is no record.
4) A reviewer sign-off line.
5) The candidate commit, the branch name, and the date, taken from the current
   git state.

Tick a box only where the evidence supports it. Where something is missing, leave
it unticked and say what is blocking it. Do not invent evidence. Do not change
application code.

Save the checklist to:
lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
```

**You should see:** `lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md`

Read it. Any unticked box is a decision you need to make before releasing.

---

## B. Open the pull request

Use the **`pull-request`** helper if your version lists it; otherwise the default Copilot Chat.

```text
Create a pull request for the v0.1.0 release of this product.

Read from the workspace:
- lifecycle/07-review/output/ (every review file)
- lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
- lifecycle/05-sprint-planning/output/sprint-plan.md
- lifecycle/02-discovery/input/mvp-framing.md

The pull request description must state:
- What shipped, in plain language, taken from the sprint plan's definition of done
- How it was validated: tests plus the Stage 7 review outcomes, citing the review
  files by path
- What is deliberately out of scope for this release, taken from the framing

Use the current branch and its real commits; do not invent history. Open the pull
request against this repository's default branch.

Do not merge and do not tag in this step. Do not start new features.

If a pull request URL is created, record it under a "Pull request" heading in:
lifecycle/08-delivery/output/v0.1.0-release-notes.md
Create that file if it does not exist.
```

**You should see:** a pull request on GitHub, and its link recorded in the release notes file.

Not using GitHub? Skip to part C and merge your branch locally instead.

---

## C. Merge, tag, and write the release notes

Do this only after the pull request is approved — or, if you are working alone, after you have read your own checklist and are satisfied.

```text
Complete the v0.1.0 release.

Read from the workspace:
- lifecycle/08-delivery/output/v0.1.0-release-evidence-checklist.md
- lifecycle/07-review/output/ (every review file)
- lifecycle/09-operations/output/runbook.md, if it exists

Tasks:
1) Confirm the checklist's sign-off is complete. If it is not, stop and tell me
   exactly what is missing.
2) Guide me through merging the approved pull request into the default branch,
   or perform the merge if I ask you to.
3) Create an annotated git tag v0.1.0 on the merged release commit.
4) Write release notes covering:
   - What this version can do
   - How it was validated: tests and the Stage 7 reviews
   - What is explicitly not included, from the framing's out-of-scope list
   - A pointer to lifecycle/09-operations/output/runbook.md for how to run it
   - The tag name and the commit it points at

Do not add features. If a v0.1.0 tag already exists, stop and ask me before
moving it.

Save the release notes to:
lifecycle/08-delivery/output/v0.1.0-release-notes.md
```

**You should see:** `lifecycle/08-delivery/output/v0.1.0-release-notes.md`, and `git tag` listing `v0.1.0`.

---

## 3. If a helper asks you a question

Anything about evidence comes from the reviews and test records. Anything about whether to release despite an unticked box is your judgement — write your reasoning into the checklist so the decision survives.

## 4. Done when

- [ ] The release checklist is filled in, with any blockers written down
- [ ] The pull request is created and merged, or your branch is merged
- [ ] `git tag` lists `v0.1.0`
- [ ] `lifecycle/08-delivery/output/v0.1.0-release-notes.md` exists

Tick Stage 8 in [CHECKLIST.md](../../CHECKLIST.md).

**Next:** [Stage 9 — Operations](../../09-operations/prompt/README.md) — the last one.
