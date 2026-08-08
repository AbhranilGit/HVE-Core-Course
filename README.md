# PulseBoard

Local-first team status board. People post short daily updates (**doing / blocked / next**); the team views **today’s** board in one place.

Built with **Python**, **FastAPI**, **SQLite**, and **HTMX**, using [HVE Core All](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all) workflows (Research → Plan → Implement → Review) with GitHub Copilot in VS Code.

## MVP scope

| In scope | Out of scope |
| --- | --- |
| Post doing / blocked / next | SSO / OAuth |
| Today’s board view | Notifications / Slack |
| Simple local identity | Mobile app |
| SQLite on a developer machine | Multi-tenant SaaS |

See [docs/project-planning/mvp-framing.md](docs/project-planning/mvp-framing.md).

## Repository layout

```text
.
├── src/pulseboard/           # Application package
├── tests/                    # Automated tests
├── scripts/                  # Utility scripts
├── docs/
│   ├── project-planning/     # BRD, PRD, MVP framing, ADRs
│   ├── architecture/         # Diagrams and design notes
│   ├── operations/           # Runbooks
│   └── guides/               # How we work (incl. HVE lifecycle)
├── .copilot-tracking/        # Durable RPI artifacts from HVE
├── pyproject.toml
└── README.md
```

## Prerequisites

- VS Code with GitHub Copilot Chat
- [HVE Core - All](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core-all)
- Python 3.12+ (recommended: conda env `hve-env`)

```bash
conda activate hve-env
python --version   # expect 3.12.x
```

## Documentation

| Doc | Purpose |
| --- | --- |
| [HVE lifecycle guide](docs/guides/hve-lifecycle.md) | How we use HVE stage-by-stage on PulseBoard |
| [MVP framing](docs/project-planning/mvp-framing.md) | Accepted product boundaries |
| `docs/project-planning/` | BRD, PRD, ADRs (as they are created) |
| `docs/operations/` | Runbooks after the MVP ships |

## Status

Discovery in progress. Application code under `src/pulseboard/` will follow product definition and backlog breakdown.
