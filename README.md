# Build your idea, one stage at a time

This is a **starter kit**. You bring an idea. You copy this template, describe your idea in one document, and then follow nine short pages that each tell you exactly what to click, what to paste, and what file should appear.

You do not need to know anything about this repository, and you do not need to have used AI coding tools before.

Every stage is done by a **helper**: a specialist AI assistant inside GitHub Copilot Chat. One helper writes requirements, another breaks work into tasks, another writes code. You pick the right helper, paste the prompt we give you, and check the result.

## What you end up with

| You get | Where it lives |
| --- | --- |
| A working first version of your product | `src/` and `tests/` |
| A written record of the problem you set out to solve | `lifecycle/02-discovery/output/` |
| A list of features with clear "this is finished when…" rules | `lifecycle/03-product-definition/output/` |
| The work split into small tasks, in a sensible order | `lifecycle/04-decomposition/` and `lifecycle/05-sprint-planning/` |
| Proof it was reviewed before you called it done | `lifecycle/07-review/output/` |
| A page telling the next person how to run it | `lifecycle/09-operations/output/runbook.md` |

Those documents are the point. They are what stops the AI (and you) from quietly building something nobody asked for.

## What you need before you start

- **VS Code** — the code editor
- **GitHub Copilot Chat** — signed in and working
- **HVE Core - All** — the extension that provides the helpers. [Install it here](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)
- **Git** — to copy this template and later save your work

You do **not** need to have chosen a programming language yet. You decide that in Stage 3.

## How to copy this template

Open a terminal and run these four commands. Replace `<repo-url>` with this repository's address, and `my-project` with whatever you want to call your project.

```bash
git clone <repo-url> my-project
cd my-project
git checkout template
git checkout -b my-project-main
```

The last line creates your own branch so your work stays separate from the template. Then open the `my-project` folder in VS Code.

## The one thing you write yourself

Everything in this kit flows from a single document:

**[lifecycle/02-discovery/input/mvp-framing.md](lifecycle/02-discovery/input/mvp-framing.md)**

You fill in that file with your idea — the problem, who it is for, and what is in and out of scope. Every prompt after that reads it automatically. You never have to retype your product name or paste your idea again.

## The nine stages

Work top to bottom. Do not skip ahead.

| # | Stage | In plain words | Open this page |
| --- | --- | --- | --- |
| 1 | Setup | Install the helpers and check they appear | [setup-checklist.md](lifecycle/01-setup/input/setup-checklist.md) |
| 2 | Discovery | Turn your idea into a clear statement of the problem | [Stage 2](lifecycle/02-discovery/prompt/README.md) |
| 3 | Product definition | Decide the features, and lock the big technical choices | [Stage 3](lifecycle/03-product-definition/prompt/README.md) |
| 4 | Decomposition | Break the features into small tasks | [Stage 4](lifecycle/04-decomposition/prompt/README.md) |
| 5 | Sprint planning | Put the tasks in order; pick what to build first | [Stage 5](lifecycle/05-sprint-planning/prompt/README.md) |
| 6 | Implementation | Build it, one task at a time | [Stage 6](lifecycle/06-implementation/prompt/README.md) |
| 7 | Review | Check the result against what you promised | [Stage 7](lifecycle/07-review/prompt/README.md) |
| 8 | Delivery | Publish your first release | [Stage 8](lifecycle/08-delivery/prompt/README.md) |
| 9 | Operations | Write the page that tells people how to run it | [Stage 9](lifecycle/09-operations/prompt/README.md) |

Keep **[lifecycle/CHECKLIST.md](lifecycle/CHECKLIST.md)** open as you go. It is a single page with a tick box per stage so you always know where you are.

## How each stage page works

Every one of the nine pages has the same shape, so once you have done one you can do them all:

1. What this stage is for
2. Before you start — things that must already exist
3. Pick the helper — the exact name to choose in the Copilot dropdown
4. Paste this prompt — copy the block exactly, change nothing
5. What you should see afterwards — the file path that should now exist
6. If the helper asks you a question — how to answer
7. Done when — tick boxes, then a link to the next stage

## The rules that keep this working

- **One helper per job.** Do not ask the coding helper to write requirements, or the requirements helper to write code.
- **Do not skip stages.** Each stage reads the file the previous stage produced. Skip one and the next has nothing to read.
- **The files are the truth, not the chat.** Chat history disappears. The documents in `lifecycle/` are what you and the AI come back to.
- **If it is not in your framing document, it is not in scope.** When you want to add something, edit the framing document first.

## If something goes wrong

| What you see | What to do |
| --- | --- |
| The helper name is not in the Copilot dropdown | The HVE Core - All extension is not installed or VS Code was not reloaded. Install it, then reload VS Code. Names vary slightly between extension versions, so pick the closest match. |
| The helper asks you a question you cannot answer | Look for the answer in your [framing document](lifecycle/02-discovery/input/mvp-framing.md). If it is not there, decide now, tell the helper, and add the answer to the framing document so it is not lost. |
| The helper invents a feature you never asked for | Reply: "That is out of scope. Use only what is in `lifecycle/02-discovery/input/mvp-framing.md`." Scope creep is the most common way these projects fail. |
| The file was written to the wrong place | Reply with the correct path from the stage page and ask it to save there. Every prompt states the exact path it should write to. |
| The helper says a file it needs is missing | You skipped a stage, or the previous stage failed to save. Go back one stage and confirm the output file exists. |

## Words you will see

Terms like BRD, PRD, ADR, backlog and sprint are all explained in plain English in the **[glossary](docs/guides/glossary.md)**.

If you want to understand *why* the process is shaped this way before you start, read the **[lifecycle guide](docs/guides/README.md)**. It is optional.

## What is in this repository

```text
.
├── lifecycle/          # The nine stages. This is where you spend your time.
│   ├── CHECKLIST.md    # Your progress tracker
│   ├── 01-setup/ … 09-operations/
│   │   ├── input/      # What the stage reads
│   │   ├── output/     # What the stage produces
│   │   └── prompt/     # The page telling you what to do
├── src/                # Your application code (created in Stage 6)
├── tests/              # Your tests (created in Stage 6)
├── scripts/            # Helper scripts, if you need any
├── docs/guides/        # Glossary and background reading
└── .copilot-tracking/  # Working notes the AI helpers save automatically
```

Ready? Start with **[Stage 1 — Setup](lifecycle/01-setup/input/setup-checklist.md)**.
