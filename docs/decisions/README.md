# Decision records

Each file here records one technical decision: what you chose, why, what it costs you, and when it would be worth changing your mind.

Written by the **`ADR Creation`** helper in [Stage 3, part B](../../lifecycle/03-product-definition/README.md). `docs/decisions/` is the location that helper recommends, which is why this kit uses it — the folder is called *decisions* rather than *adrs* because not every decision worth recording is strictly architectural.

Empty until you run that stage.

## Why bother

Six months from now, someone at the customer will ask "why is this built this way?" and you will not be there. Without these files the answer is lost, and the AI helpers have no way to stay consistent with choices already made. Stages 6, 7, and 9 all read this folder so they work with the real stack rather than guessing.

## Inherited or chosen

On an engagement most of the technology was decided before you arrived, so each record has to say which kind it is.

| Kind | What the record captures |
| --- | --- |
| **Inherited** | The constraint, who imposed it, and what it rules out. Not re-argued, and no alternatives presented as though it were still open |
| **Chosen** | The decision made during this engagement, with alternatives and consequences |

That distinction is the whole value of this folder to whoever inherits the system. An engineer deciding whether they can change something needs to know whether it was a considered choice or a constraint they may have outgrown.

## Naming

`YYYY-MM-DD-descriptive-topic-v01.md` — an ISO date, a short topic, and a version suffix. For example `2026-03-14-sqlite-for-local-storage-v01.md`.

`ADR Creation` drafts into `.copilot-tracking/adrs/<topic>-draft.md` while you are still talking it through, then moves the finished record here once you confirm. It asks you where to put the final file early in the conversation — answer `docs/decisions/`.

## The questions this folder must answer

Whatever else you record, these must be answerable from here, because later stages read them rather than asking you again:

| Question | Who reads the answer |
| --- | --- |
| What language and framework is this built in? | Stage 6, so it writes code in the real stack |
| Where does the data live, and where may it not live? | Stage 6, and the Stage 9 runbook |
| What exact command runs the tests, and what does the suite not cover? | Stage 6 after every task, and Stage 8 at release |
| What can we not change, and who says so? | Every stage, and whoever maintains this next |

The test command is the one people forget. Write it as something you could paste into a terminal — `pytest`, `npm test`, `go test ./...` — not as "run the unit tests". Copy it into `.github/copilot-instructions.md` once confirmed, and only after you have run it yourself.

## What does not belong here

- Application code
- Tasks or sprint plans
- New product features — a decision record captures *how* you build, never *what* you build
