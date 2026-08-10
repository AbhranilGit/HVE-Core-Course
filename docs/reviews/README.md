# Reviews

The committed verdicts on whether this system does what was contracted.

| File | What it answers |
| --- | --- |
| `<iteration>-review.md` | Did that iteration deliver its definition of done? One per iteration |
| `code-review.md` | Is the code correct, adequately tested, and consistent with this codebase? |
| `security-review.md` | What did we introduce that an attacker would want? Required where the engagement brief says so |
| `rai-review.md` | Does the built system match the Responsible AI assessment? Required where the brief says so |

Produced in [Stage 7 — Review](../../lifecycle/07-review/README.md). Empty until you run it.

These are summaries. The full evidence lives under `.copilot-tracking/reviews/`, which is not committed — so anything the customer needs after you leave belongs in these files, not there.

## Why these matter after the engagement

These files outlive you. The customer's security and engineering leads will read them, and a follow-on engagement will start from them. Three habits keep them worth reading:

- **Every defect carries a decision:** fix now, fix later, or will not fix. A finding with no decision is an open question pretending to be a record.
- **Findings in code you wrote stay separate from findings in code you inherited.** They need different decisions and different conversations, and a pull request that quietly repairs unrelated legacy code is one nobody wants to review.
- **Anything deferred past your last day has been through the customer**, with the date recorded. It becomes their problem the moment you go, so they get a say now.

`security-review.md` needs one more thing: a line at the top stating what it is. `Security Reviewer` is an assistive tool, not a clearance, and a customer who mistakes it for a sign-off has been misled by the filing rather than by you.
