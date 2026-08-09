# Issue #5 — RPI verification

| | |
| --- | --- |
| **Issue** | [#5](https://github.com/AbhranilGit/HVE-Core-Course/issues/5) — api: upsert today status (doing / blocked / next) |
| **Prompt** | [`../../prompt/issue-05.md`](../../prompt/issue-05.md) |

Verify each phase **before** starting the next. Do not mark Implement done until issue AC is met.

## Research

Artifact: [`research.md`](research.md)

- [ ] File filled (findings, constraints, repo patterns, open questions)
- [ ] No production code written in this phase
- [ ] Findings are enough to plan against the issue AC

**Verified by:** _name_ · **Date:** _YYYY-MM-DD_

## Plan

Artifact: [`plan.md`](plan.md)

- [ ] File filled (steps, files to touch, AC checks, risks)
- [ ] Plan matches `research.md` (or notes intentional deltas)
- [ ] Scope is this issue only

**Verified by:** _name_ · **Date:** _YYYY-MM-DD_

## Implement

Artifact: [`implement.md`](implement.md) + code under `src/` / `tests/` (as applicable)

- [ ] `implement.md` lists what changed and how AC was checked
- [ ] Issue acceptance criteria met
- [ ] RPI/session evidence noted (`.copilot-tracking/` if present)
- [ ] No work started on the next issue

**Verified by:** _name_ · **Date:** _YYYY-MM-DD_

## Gate

- [ ] Research verified → may start Plan
- [ ] Plan verified → may start Implement
- [ ] Implement verified → may start next issue in [`../../prompt/README.md`](../../prompt/README.md)
