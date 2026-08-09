# Words you will see

Every term this kit uses, in plain English. You do not need to memorise these — come back when a stage page uses one you do not recognise.

Start with the [main README](README.md) if you have not yet.

## The documents you will produce

| Term | What it actually means |
| --- | --- |
| **MVP** (minimum viable product) | The smallest version of your idea that is still genuinely useful to someone. Not a demo, not the full dream — the first thing worth using. |
| **Framing document** | The one file you write by hand, describing your idea: the problem, who has it, and what is in and out of scope. Everything else is generated from it. Lives at `lifecycle/02-discovery/input/mvp-framing.md`. |
| **BRD** (business requirements document) | A short write-up of *why* you are building this: the problem, who has it, what success looks like. It deliberately does not talk about features or technology yet. |
| **PRD** (product requirements document) | The *what*: the list of features, written as user stories, each with rules for when it counts as finished. |
| **User story** | One sentence describing something a person wants to do, in the form "As a *someone*, I want to *do something*, so that *benefit*." |
| **Acceptance criteria** (often shortened to **AC**) | The checklist that decides whether a feature is done. "Done" means every criterion is met — not "it ran on my machine once". |
| **ADR** (architecture decision record) | A one-page note recording a technical decision, why you made it, what it costs you, and when you would change your mind. Example: choosing one database over another. Written once, read for years. |
| **Backlog** | The full list of tasks still to do. |
| **Backlog snapshot** | A copy of that list saved as a file in this repository, so the work is readable without opening GitHub. |
| **Runbook** | The page that tells the next person how to start your app, where its data lives, and what to do when it breaks. Written last, appreciated forever. |

## How the work is organised

| Term | What it actually means |
| --- | --- |
| **Issue** | One small task, tracked on GitHub. It has a title and acceptance criteria. |
| **Sprint** | A batch of tasks you commit to finishing before moving on. This kit uses two: Sprint 1 builds the core, Sprint 2 hardens it. |
| **Thin vertical slice** | The smallest end-to-end path through your product that a real person could actually use — touching every layer, from what they click to where data is stored. You build this first, so you have something real early instead of many half-finished pieces. |
| **Definition of done** | The agreed rules for calling a sprint finished. |
| **Scope creep** | Features quietly appearing that nobody agreed to. The single most common reason projects like this fail. This kit fights it by writing scope down and pointing every prompt back at it. |
| **In scope / out of scope** | What you are building now, and what you are deliberately not building. Saying "no" explicitly is the useful half. |

## The AI helpers

| Term | What it actually means |
| --- | --- |
| **Helper** (also called an **agent** or **mode**) | A version of Copilot Chat set up for one job. You choose one from the dropdown at the bottom of the chat box. `brd-builder` writes requirements; `RPI Agent` writes code. Using the right one matters more than the words in your prompt. |
| **Prompt** | The instructions you paste into the chat. In this kit, every prompt is written for you — copy it exactly, change nothing. |
| **HVE** (Hypervelocity Engineering) | The VS Code extension providing all these helpers. "HVE Core - All" is the full set. |
| **Slash command** | An instruction starting with `/`, typed into the chat, that runs a specific routine — for example `/rpi` or `/task-review`. |
| **RPI** (research, plan, implement, review) | The four-phase routine for writing code: first the AI investigates and writes down what it found, then it writes a plan, then it writes the code, and finally it reviews the result and runs the tests. Each phase is saved as a file, and you check each one before allowing the next. This is what stops the AI from confidently building the wrong thing. |
| **Gate** | A checkpoint you confirm before moving on. If the previous step's file does not exist, you do not proceed. |

## Git and shipping

| Term | What it actually means |
| --- | --- |
| **Branch** | A separate copy of the project where you can work without disturbing anything else. You made one when you copied this template. |
| **Commit** | A saved snapshot of your changes, with a message explaining them. |
| **Pull request** (PR) | A request to merge your branch's work into the main one, giving people a place to review it first. |
| **Tag** | A permanent label on one exact version of the code, so you can always come back to it. Your first release is tagged `v0.1.0`. |
| **Release notes** | A short summary of what shipped, what was checked, and what was deliberately left out. |

## Folders in this repository

| Folder | What it holds |
| --- | --- |
| `lifecycle/` | The nine stages. Each has a `README.md` (the page telling you what to do), plus `input/` (what it reads) and `output/` (what it produces). |
| `src/` | Your application code. Empty until Stage 6. |
| `tests/` | Automated checks that your code does what it claims. Empty until Stage 6. |
| `scripts/` | Small utility scripts, if your project needs any. |
| `.copilot-tracking/` | Working notes the helpers save automatically as they research, plan, and implement. You (the builder) rarely need to open it. The Stage 7 review helpers read it as evidence of what changed and what was researched — leave it in place. |
