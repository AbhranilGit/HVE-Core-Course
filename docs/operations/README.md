# Operations and handover

What the customer needs in order to run this without you.

| File | What it holds |
| --- | --- |
| `runbook.md` | Install, start, deploy, roll back, test, and troubleshoot — the page someone opens at 2am |
| `handover.md` | What was delivered, what was not, where the system is weak, and what to do next |
| `incidents/` | One report per incident, from `/incident-response` |

Written in [Stage 9 — Handover](../../lifecycle/09-operations/README.md) and checked by the **`Doc Ops`** helper, which verifies that the commands and paths a runbook quotes actually exist in this repository. Empty until you run it.

## The test that counts

`Doc Ops` catches stale commands. It cannot tell you whether the runbook makes sense to someone who was not here.

For that, have one of the customer's engineers follow it on their own machine from scratch while you say nothing. Every place they get stuck is a defect. Fix it and repeat. Following it yourself proves nothing — you already know the answers.

## Write for their worst day

Both files get read by someone under pressure who cannot ask you anything. That rules out a few habits worth naming:

- No references to conversations, chat history, or decisions that exist only in your memory
- No Microsoft-internal tools they will not have access to
- No commands you have not personally run in their environment

`handover.md` has one section people consistently soften: where the system is weak. If a module is fragile, a test suite has a gap, or a decision was made under time pressure and should be revisited, say so plainly. You will not be there to warn them later, and a handover that reads as a success story is worth less than one that says where the bodies are buried.
