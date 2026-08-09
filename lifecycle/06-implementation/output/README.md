# Stage 6 — the notes each task leaves behind

Every task gets its own folder here, holding the three files the AI writes as it works plus your checklist. Together they are the record of *why* the code looks the way it does — which is what makes the Stage 7 review possible.

The folders appear automatically when you run Step 0 in [`../prompt/README.md`](../prompt/README.md). You do not create them by hand.

```text
output/
├── _template/         # The blank checklist that gets copied per task. Leave it alone.
├── issue-01/
│   ├── README.md      # Your checklist — tick as you go
│   ├── research.md    # Written by step 1
│   ├── plan.md        # Written by step 2
│   └── implement.md   # Written by step 3, alongside the real code
├── issue-02/
└── …
```

| Step | What you type | The file it writes | It is finished when |
| --- | --- | --- | --- |
| Research | `/rpi continue=1` | `research.md` | Findings are recorded, no code written yet, and the Research boxes are ticked |
| Plan | `/rpi continue=2` | `plan.md` | Steps and acceptance checks are recorded, they follow the research, and the Plan boxes are ticked |
| Implement | `/rpi continue=3` | `implement.md`, plus code in `src/` and `tests/` | The acceptance criteria are met, the code runs, and the Implement boxes are ticked |

The helpers also save their own working notes under `.copilot-tracking/`. You rarely need to open those, but the Stage 7 review reads them, so leave them in place.

**The files in this folder are the durable trail.** Chat history disappears; these do not.
