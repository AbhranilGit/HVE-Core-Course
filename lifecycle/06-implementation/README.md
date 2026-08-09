# Stage 6 — Implementation

Build it, one task at a time.

| | |
| --- | --- |
| **Reads** | [`../05-sprint-planning/output/sprint-plan.md`](../05-sprint-planning/output/sprint-plan.md) and [`../04-decomposition/output/backlog-snapshot.md`](../04-decomposition/output/backlog-snapshot.md) |
| **Produces** | Code in `src/` and `tests/`, a folder of notes per task under [`output/`](output/), and a closed issue per task |
| **Helpers** | Default Copilot Chat to set the folders up, `RPI Agent` to research, plan, implement and review each task, `github-backlog-manager` to close each issue |

This is the longest stage. Read section 1 before you start — it explains the loop you will repeat for every task.

---

## 1. What this stage is for

You now write the code. But not in one giant "build my app" request — that is how AI produces something confident and wrong.

Instead, every task goes through four phases, called **RPI**:

| Phase | What happens | The file it leaves behind |
| --- | --- | --- |
| **Research** | The AI reads your code and documents and writes down what it found. No code yet. | `research.md` |
| **Plan** | It writes a plan based on that research. Still no code. | `plan.md` |
| **Implement** | It follows the plan and writes the actual code. | `implement.md` plus real code |
| **Review** | It runs the tests and checks the result against what the task promised. No new features. | `review.md` |

Each phase saves a file, and **you read it before allowing the next one**. That is the whole trick. If the research misunderstood something, you catch it in a paragraph rather than in three hundred lines of code.

Once the review passes, one last thing closes the task out: the issue that asked for the work gets the evidence as a comment, and is closed. Without the review record, Stage 8 has no evidence to cite at release time. Without closing the issue, your GitHub board keeps showing work that has already shipped.

You repeat this for every task in your sprint plan, in order. Do not run two tasks at once, and do not skip ahead.

**Clear the chat between phases.** Run `/clear`, or start a new chat, before each phase. Each phase writes what it learned to a file, and the next phase reads that file — so nothing is lost, and the helper works from the evidence rather than from a long, drifting conversation. This is the single habit that keeps the loop honest.

## 2. Prerequisites

- `lifecycle/05-sprint-planning/output/sprint-plan.md` exists
- `lifecycle/04-decomposition/output/backlog-snapshot.md` exists
- Your ADRs record which language and tools you are using — the AI reads them to match your choices
- Your ADRs name the exact command that runs the tests — Step 4 runs it after every task
- You have installed whatever that language needs to run on your machine

---

## 3. Step 0 — set up the task folders (do this once)

Every task gets **its own folder** under `output/`, named after that task, holding everything that task produces. Rather than creating them by hand, have a helper build them from your sprint plan.

Folders are named `issue-<NN>-<slug>`: the task's number in sprint plan order, then a short slug of its title. Task 1 called "User can log in" becomes `issue-01-user-can-log-in`. The number keeps them in build order when you list the folder; the slug means you can tell what a folder is about without opening it, six months from now.

Use the **default Copilot Chat** for this one — not `RPI Agent`. This step only copies templates and creates folders; there is no research, planning, or code involved, and `RPI Agent` would be tempted to start building. You switch to `RPI Agent` in section 5, once there is an actual task to work on.

1. Open Copilot Chat.
2. Leave the mode dropdown on its default — *Agent* or *Ask*.
3. Paste this prompt exactly:

```text
Read lifecycle/05-sprint-planning/output/sprint-plan.md and
lifecycle/04-decomposition/output/backlog-snapshot.md from the workspace.

For every task in Sprint 1 and Sprint 2, in the sprint plan's order, create one
folder of its own under lifecycle/06-implementation/output/.

Name each folder issue-NN-<slug>, where NN is the task's number in sprint plan
order, zero-padded to two digits, and <slug> is that task's title in lowercase
with spaces replaced by hyphens and punctuation removed. Keep the slug under
about six words. For example: issue-01-user-can-log-in.

Inside each of those folders, create exactly two files:

1. README.md
   Copy lifecycle/06-implementation/output/_template/README.md, replacing every
   <placeholder> with that task's real values: its number, title, its id in the
   backlog snapshot, its sprint, what it depends on, and <folder> with that
   task's own folder name.

2. checks.md
   Copy lifecycle/06-implementation/output/_template/checks.md, replacing its
   <placeholders> with the same task's values.

Leave research.md, plan.md, implement.md, and review.md to be written later, by the
phases themselves.

Then fill in the task order table in lifecycle/06-implementation/README.md
under the heading "4. Your task order", one row per task, in sprint plan order.

Do not create any folder outside lifecycle/06-implementation/output/. Do not copy
the _template folder itself. Do not write any application code, and do not start
work on any task — this step only creates the folders and the two pages inside
each one. Do not ask me to attach files; read them from the workspace.
```

You should now have one folder per task under `output/`, each holding a `README.md` and a `checks.md`. As you work, the four remaining files fill in around them:

```text
output/
├── _template/                      # The blank pages copied per task. Leave it alone.
│   ├── README.md                   # → becomes each task's README.md
│   └── checks.md                   # → becomes each task's checks.md
├── issue-01-user-can-log-in/
│   ├── README.md                   # The prompts for this task — start here
│   ├── checks.md                   # Your checks between steps
│   ├── research.md                 # Written by step 1
│   ├── plan.md                     # Written by step 2
│   ├── implement.md                # Written by step 3, alongside the real code
│   └── review.md                   # Written by step 4a — the test run and the verdict
├── issue-02-save-a-habit/
│   └── …
└── …
```

Those example names are illustrations. Yours come from your own backlog.

## 4. Your task order

The Step 0 prompt fills this table in. Work down it, top to bottom.

| Order | Task | Its folder | Sprint |
| --- | --- | --- | --- |
| | | | |

## 5. The loop, for each task

Now switch the mode dropdown to **`RPI Agent`** — from here on you are building, not scaffolding.

Open that task's folder and start with its `README.md`. That page contains the prompts to paste, in order:

1. **Research** — paste prompt 1, wait, then open the `research.md` it produced and read it
2. **Plan** — paste prompt 2, then read the `plan.md` it produced
3. **Implement** — paste prompt 3, then read the `implement.md` it produced and check the code runs
4. **Review and close** — paste prompt 4a to run the tests and record the verdict in `review.md`, then switch to `github-backlog-manager` and paste prompt 4b to close the issue

Between each step, run `/clear` or start a new chat, then open that task's `checks.md` and confirm the checks for the step you just finished. That page is your gate: it exists so you pause and look, rather than letting the steps run together.

**Do not start the next task until the current one's tests have passed and its issue is closed.**

### How to run the prompts

Each of the first three prompts starts with `/rpi` followed by `continue=1`, `2`, or `3` — that number tells the helper which step to run.

| You type | Step it runs | It must read first | It saves | It is finished when |
| --- | --- | --- | --- | --- |
| `/rpi continue=1 task=…` | Research | The backlog snapshot | `research.md` | Findings are recorded, no code is written yet, and you have confirmed the Research checks |
| `/rpi continue=2 task=…` | Plan | `research.md` | `plan.md` | Steps and acceptance checks are recorded, they follow the research, and you have confirmed the Plan checks |
| `/rpi continue=3 task=…` | Implement | `plan.md` | `implement.md` and code | The code runs, it follows the plan, and you have confirmed the Implement checks |
| `/task-review plan=… changes=… research=… scope=…` | Review | `implement.md` | `review.md` | The tests passed, every acceptance criterion is recorded as met, and you have confirmed the Review checks |
| the Step 4b prompt | Close | `review.md` | a closed issue, and an updated backlog snapshot | The issue carries the evidence and is closed |

Do **not** use `continue=all` — that runs the whole thing without stopping, which defeats the point.

Step 4 does not run through `/rpi`. The `RPI Agent` helper understands reviewing perfectly well — its description covers all four phases and more — but the `/rpi` *command* only accepts `continue=1`, `2`, `3`, or `all`, and `3` is Implement. So Step 4a uses the separate **`/task-review`** command with the **`Task Reviewer`** helper; it fills the box with placeholders like `[plan=...] [changes=...]` for you to replace, and the task's own page spells out how. Step 4b is an ordinary instruction to `github-backlog-manager`, which owns your issues.

Clearing the chat between each of these is required, not a fallback for when things go wrong. The files carry the context, so nothing is lost.

### One task, one folder

Each prompt writes only into the folder of the task it belongs to. If you find one task's research sitting in another task's folder, something went wrong: move it back and rerun the step, rather than leaving the trail scrambled. The Stage 7 review walks these folders task by task, so a misfiled note becomes a misleading review.

The application code itself does not live in `output/` — it goes in `src/` and `tests/`. These folders hold the reasoning, not the product.

The helpers also save their own working notes under `.copilot-tracking/`. You rarely need to open those, but the Stage 7 review reads them, so leave them in place.

**The files in these folders are the durable trail.** Chat history disappears; these do not.

## 6. If the helper asks you a question

Answer from the backlog snapshot, the PRD, or your ADRs. If it asks you to attach a file, tell it the path and say "read it from the workspace" — every prompt in this kit already contains the paths it needs.

If it says a file it needs is missing, you have skipped a step. Go back and run the previous one.

## 7. Done when

- Every Sprint 1 task has its own folder under `output/`, holding `research.md`, `plan.md`, `implement.md`, and `review.md`
- Every `review.md` has a Test run section, that run passed, and every acceptance criterion is recorded as met
- Every task's issue is closed, and the backlog snapshot marks it done
- Every task's checks in its own `checks.md` have been confirmed
- No task's files ended up in another task's folder
- The code runs, and the thin slice from your sprint plan actually works
- The same is true for Sprint 2 tasks
- No features appeared that were not in the backlog

**Next:** [Stage 7 — Review](../07-review/README.md)
