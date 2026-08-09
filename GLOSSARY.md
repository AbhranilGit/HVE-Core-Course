# Words you will see

Every term this kit uses, in plain English. You do not need to memorise these —
come back when a stage page uses one you do not recognise.

Start with the [main README](README.md) if you have not yet.

## The documents you will produce

| Term | What it actually means |
| --- | --- |
| **MVP** (minimum viable product) | The smallest version of your idea that is still genuinely useful to someone. Not a demo, not the full dream — the first thing worth using. |
| **Framing document** | The one file you write by hand, describing your idea: the problem, who has it, and what is in and out of scope. Everything else is generated from it. Lives at `lifecycle/02-discovery/mvp-framing.md`. |
| **BRD** (business requirements document) | A short write-up of *why* you are building this: the problem, who has it, what success looks like. It deliberately does not talk about features or technology yet. Lands in `docs/brds/`. |
| **PRD** (product requirements document) | The *what*: the list of features, written as user stories, each with rules for when it counts as finished. Lands in `docs/prds/`. |
| **User story** | One sentence describing something a person wants to do, in the form "As a *someone*, I want to *do something*, so that *benefit*." |
| **Acceptance criteria** (often shortened to **AC**) | The checklist that decides whether a feature is done. Each one gets an id in the PRD so tasks and reviews can point back at it. "Done" means every criterion is met — not "it ran on my machine once". |
| **ADR** (architecture decision record), also **decision record** | A one-page note recording a technical decision, why you made it, what it costs you, and when you would change your mind. Example: choosing one database over another. Written once, read for years. Lands in `docs/decisions/`, named by date: `2026-03-14-sqlite-for-local-storage-v01.md`. |
| **Backlog** | The full list of tasks still to do, kept in your tracker. |
| **Sprint plan** | The backlog put in order and split into sprints, with a definition of done for each. Lands at `docs/planning/sprint-plan.md`. |
| **Runbook** | The page that tells the next person how to start your app, where its data lives, and what to do when it breaks. Written last, appreciated forever. |

## How the work is organised

| Term | What it actually means |
| --- | --- |
| **Issue** (or **work item**) | One small task in your tracker. It has a title and acceptance criteria that cite the PRD ids they came from. |
| **Tracker** | Wherever your team keeps work items — GitHub Issues, Azure DevOps, or Jira. This kit supports all three, and a plain file if you use none. |
| **Sprint** | A batch of tasks you commit to finishing before moving on. This kit defaults to two: Sprint 1 builds the core, Sprint 2 hardens it. |
| **Thin vertical slice** | The smallest end-to-end path through your product that a real person could actually use — touching every layer, from what they click to where data is stored. You build this first, so you have something real early instead of many half-finished pieces. |
| **Definition of done** | The agreed rules for calling a sprint finished. |
| **Scope creep** | Features quietly appearing that nobody agreed to. The single most common reason projects like this fail. This kit fights it by writing scope down and pointing every prompt back at it. |
| **In scope / out of scope** | What you are building now, and what you are deliberately not building. Saying "no" explicitly is the useful half. |

## The AI helpers

| Term | What it actually means |
| --- | --- |
| **HVE** (Hyper Velocity Engineering) | Microsoft's framework for AI-assisted software delivery, and the nine-stage lifecycle this kit follows. **HVE Core** is the tooling; **HVE Core - All** is the full extension bundle. This kit targets version `3.3.101`. |
| **Helper** (also called an **agent** or **mode**) | A version of Copilot Chat set up for one job. `BRD Builder` writes requirements; `Task Implementor` writes code. Using the right one matters more than the words in your prompt. Some you pick from the dropdown at the bottom of the chat box; most arrive automatically with a slash command. |
| **Prompt** | The instructions you paste into the chat. In this kit, every prompt is written for you — copy it exactly, and only change the values the page tells you to. |
| **Slash command** | An instruction starting with `/`, typed into the chat, that runs a specific routine — for example `/task-research` or `/git-merge`. Most commands also carry a helper: typing `/task-plan` switches you to `Task Planner` without touching the dropdown. |
| **Argument** | A `name=value` pair after a slash command that tells it what to work on, as in `/task-plan research=<path>`. The chat shows you which ones a command accepts as you type. |
| **Skill** | A packaged capability a helper loads when it needs it — the OWASP security checklists and the Jira and GitLab integrations are skills. You do not usually invoke these yourself. |
| **Instructions** | Background rules that apply automatically based on what you are editing. `.github/copilot-instructions.md` is your project's own set, and every helper reads it on every request. |
| **RPI** (research, plan, implement, review) | The four-phase routine for writing code: first the AI investigates and writes down what it found, then it writes a plan, then it writes the code, and finally it reviews the result and runs the tests. Each phase is its own command — `/task-research`, `/task-plan`, `/task-implement`, `/task-review` — saves its own file, and you check that file before allowing the next. This is what stops the AI from confidently building the wrong thing. |
| **Slug** | The short lowercase name that keeps a task's four evidence files recognisable, for example `issue-01-user-can-log-in`. The phases actually chain by file path, but a consistent slug is what makes the folders readable a month later. |
| **Gate** | A checkpoint you confirm before moving on. If the previous step's file does not exist or you have not read it, you do not proceed. |
| **Planning log** | What `Task Planner` writes after checking its own plan, listing the discrepancies it found between the research and the plan. Reading its discrepancy section is the Plan gate. |
| **Overall status** | What `Task Reviewer` reports at the end of a review: Complete, Needs Rework, or Blocked, with counts of critical and major findings. Only Complete means done. |

## Git and shipping

| Term | What it actually means |
| --- | --- |
| **Branch** | A separate copy of the project where you can work without disturbing anything else. You made one when you copied this template. |
| **Commit** | A saved snapshot of your changes, with a message explaining them. |
| **Pull request** (PR) | A request to merge your branch's work into the main one, giving people a place to review it first. |
| **Tag** | A permanent label on one exact version of the code, so you can always come back to it. Your first release is tagged `v0.1.0`. |
| **Release notes** | A short summary of what shipped, what was checked, and what was deliberately left out. |
| **Release evidence** | The row-by-row proof behind those notes: every acceptance criterion, where its evidence lives, and whether it passed. |

## Folders in this repository

| Folder | What it holds |
| --- | --- |
| `lifecycle/` | The nine stage pages — the instructions you read. Nothing the helpers produce lands here, except your framing document and your Stage 6 task log. |
| `docs/` | Everything worth keeping: `brds/`, `prds/`, and `decisions/` at HVE Core's own default locations, plus `planning/` for the sprint plan and `reviews/`, `releases/`, and `operations/` for the rest. |
| `.github/` | `copilot-instructions.md`, your project's conventions, plus the issue template. |
| `src/` | Your application code. Empty until Stage 6. |
| `tests/` | Automated checks that your code does what it claims. Empty until Stage 6. |
| `scripts/` | Small utility scripts, if your project needs any. |
| `.copilot-tracking/` | Working notes the helpers save automatically as they research, plan, implement, and review. Not committed by default. Stage 7 reads it, so leave it in place while a project is in flight. |
