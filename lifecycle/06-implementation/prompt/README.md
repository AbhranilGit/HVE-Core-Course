# Stage 6 — Implementation

Build it, one task at a time.

| | |
| --- | --- |
| **Reads** | [`../../05-sprint-planning/output/sprint-plan.md`](../../05-sprint-planning/output/sprint-plan.md) and [`../../04-decomposition/output/backlog-snapshot.md`](../../04-decomposition/output/backlog-snapshot.md) |
| **Produces** | Code in `src/` and `tests/`, plus notes under [`../output/`](../output/) |
| **Helper** | `RPI Agent` |

This is the longest stage. Read section 1 before you start — it explains the loop you will repeat for every task.

---

## 1. What this stage is for

You now write the code. But not in one giant "build my app" request — that is how AI produces something confident and wrong.

Instead, every task goes through three steps, called **RPI**:

| Step | What happens | The file it leaves behind |
| --- | --- | --- |
| **Research** | The AI reads your code and documents and writes down what it found. No code yet. | `research.md` |
| **Plan** | It writes a plan based on that research. Still no code. | `plan.md` |
| **Implement** | It follows the plan and writes the actual code. | `implement.md` plus real code |

Each step saves a file, and **you read it before allowing the next step**. That is the whole trick. If the research misunderstood something, you catch it in a paragraph rather than in three hundred lines of code.

You repeat these three steps for every task in your sprint plan, in order. Do not run two tasks at once, and do not skip ahead.

## 2. Before you start

- [ ] `lifecycle/05-sprint-planning/output/sprint-plan.md` exists
- [ ] `lifecycle/04-decomposition/output/backlog-snapshot.md` exists
- [ ] Your ADRs record which language and tools you are using — the AI reads them to match your choices
- [ ] You have installed whatever that language needs to run on your machine

---

## 3. Step 0 — set up the task pages (do this once)

Rather than writing a page per task by hand, have a helper generate them from your sprint plan.

1. Open Copilot Chat.
2. Choose **`RPI Agent`** from the mode dropdown.
3. Paste this prompt exactly:

```text
Read lifecycle/05-sprint-planning/output/sprint-plan.md and
lifecycle/04-decomposition/output/backlog-snapshot.md from the workspace.

For every task in Sprint 1 and Sprint 2, in the sprint plan's order, create:

1. lifecycle/06-implementation/prompt/issue-NN.md
   Copy the structure of lifecycle/06-implementation/prompt/_issue-template.md
   exactly, replacing every <placeholder> with that task's real values: its
   number, title, its id in the backlog snapshot, its sprint, and what it
   depends on. Use the task's number for NN, zero-padded to two digits.

2. lifecycle/06-implementation/output/issue-NN/README.md
   Copy lifecycle/06-implementation/output/_template/README.md, replacing its
   <placeholders> with the same task's values.

Then fill in the task order table in lifecycle/06-implementation/prompt/README.md
under the heading "4. Your task order", one row per task, in sprint plan order.

Do not write any application code in this step. Do not start the research phase
for any task. Do not ask me to attach files; read them from the workspace.
```

You should now have one `issue-NN.md` file per task in this folder, and a matching folder under `../output/`.

## 4. Your task order

The Step 0 prompt fills this table in. Work down it, top to bottom.

| Order | Task | Its page | Its notes folder | Sprint |
| --- | --- | --- | --- | --- |
| | | | | |

## 5. The loop, for each task

Open that task's `issue-NN.md` page and follow it. Each page contains three prompts to paste in order:

1. **Research** — paste prompt 1, wait, then open the `research.md` it produced and read it
2. **Plan** — paste prompt 2, then read the `plan.md` it produced
3. **Implement** — paste prompt 3, then read the `implement.md` it produced and check the code runs

Between each one, tick the boxes in that task's `output/issue-NN/README.md`. That file is your gate: it exists so you pause and look, rather than letting three steps run together.

**Do not start the next task until the current one's `implement.md` exists and its acceptance criteria are met.**

### How to run the prompts

Each prompt starts with `/rpi` followed by `continue=1`, `2`, or `3` — that number tells the helper which of the three steps to run.

| You type | Step it runs | It must read first | It saves |
| --- | --- | --- | --- |
| `/rpi continue=1 task=…` | Research | The backlog snapshot | `research.md` |
| `/rpi continue=2 task=…` | Plan | `research.md` | `plan.md` |
| `/rpi continue=3 task=…` | Implement | `plan.md` | `implement.md` and code |

Do **not** use `continue=all` — that runs all three without stopping, which defeats the point.

If the chat gets long and confused, start a new chat between steps. The files carry the context, so nothing is lost.

## 6. If the helper asks you a question

Answer from the backlog snapshot, the PRD, or your ADRs. If it asks you to attach a file, tell it the path and say "read it from the workspace" — every prompt in this kit already contains the paths it needs.

If it says a file it needs is missing, you have skipped a step. Go back and run the previous one.

## 7. Done when

- [ ] Every task in Sprint 1 has `research.md`, `plan.md`, and `implement.md`
- [ ] Every task's gate checklist in `../output/issue-NN/README.md` is ticked
- [ ] The code runs, and the thin slice from your sprint plan actually works
- [ ] The same is true for Sprint 2 tasks
- [ ] No features appeared that were not in the backlog

Tick Stage 6 in [CHECKLIST.md](../../CHECKLIST.md).

**Next:** [Stage 7 — Review](../../07-review/prompt/README.md)

---

Conventions for what lands in the output folder: [`../output/README.md`](../output/README.md).
