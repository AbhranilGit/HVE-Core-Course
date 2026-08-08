# HVE Core Course — PulseBoard

Hands-on coaching track: build **PulseBoard** (a lightweight team status board) using [HVE Core All](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all) and the Research → Plan → Implement → Review (RPI) methodology.

## Defaults for this track

| Choice | Value |
| --- | --- |
| Product | PulseBoard |
| Stack | Python, FastAPI, SQLite, HTMX |
| Mode | Guided prompts, one step at a time |
| Bundle | `hve-core-all` |

## How coaching works

1. You complete **one step** at a time.
2. You reply with what you did / pasted / saw (or blockers).
3. We only advance when that step’s exit criteria are met.

Do **not** jump ahead and build the whole app. The point is to practice the HVE lifecycle, not to race to code.

## Course map

| Module | Stage | Guide | Status |
| --- | --- | --- | --- |
| 0 | Warm-up | [docs/course/00-warmup.md](docs/course/00-warmup.md) | optional |
| 1 | Setup | [docs/course/01-setup.md](docs/course/01-setup.md) | done |
| 2 | Discovery | [docs/course/02-discovery.md](docs/course/02-discovery.md) | **current** |
| 3 | Product definition | [docs/course/03-product-definition.md](docs/course/03-product-definition.md) | locked |
| 4 | Decomposition | [docs/course/04-decomposition.md](docs/course/04-decomposition.md) | locked |
| 5 | Sprint planning | [docs/course/05-sprint-planning.md](docs/course/05-sprint-planning.md) | locked |
| 6 | Implementation | [docs/course/06-implementation.md](docs/course/06-implementation.md) | locked |
| 7 | Review | [docs/course/07-review.md](docs/course/07-review.md) | locked |
| 8 | Delivery | [docs/course/08-delivery.md](docs/course/08-delivery.md) | locked |
| 9 | Operations | [docs/course/09-operations.md](docs/course/09-operations.md) | locked |

## Progress

See [docs/course/PROGRESS.md](docs/course/PROGRESS.md).

## Install HVE Core All (local VS Code / Copilot)

1. Install [VS Code](https://code.visualstudio.com/) ≥ 1.106.1
2. Install GitHub Copilot Chat
3. Install [HVE Core - All](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)
4. Reload the window and confirm agents/skills like `RPI Agent`, `/rpi-research`, `/rpi-plan` appear

If you are working primarily in **Cursor** with this coach, we will mirror RPI manually (research → plan → implement → review) and still produce the same durable artifacts under `.copilot-tracking/`.

## Product one-liner

PulseBoard lets a team post short daily status updates (doing / blocked / next) and view them on a shared board by day.
