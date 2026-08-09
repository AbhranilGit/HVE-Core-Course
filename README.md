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

See [lifecycle/02-discovery/input/mvp-framing.md](lifecycle/02-discovery/input/mvp-framing.md).

## Repository layout

```text
.
├── src/pulseboard/              # Application package
├── tests/
├── scripts/
├── lifecycle/                   # One folder per stage (input/ + output/)
│   ├── 01-setup/
│   ├── 02-discovery/            # → output/brd.md
│   ├── 03-product-definition/   # → output/prd.md, output/adr/
│   ├── 04-decomposition/
│   ├── 05-sprint-planning/
│   ├── 06-implementation/
│   ├── 07-review/
│   ├── 08-delivery/
│   └── 09-operations/           # → output/runbook.md
├── docs/
│   └── guides/                  # How we work (HVE lifecycle guide)
├── .copilot-tracking/           # Durable RPI artifacts from HVE
├── pyproject.toml
└── README.md
```

Each lifecycle stage folder contains:

- `input/` — what that stage consumes  
- `output/` — what that stage produces  

Details: [lifecycle/README.md](lifecycle/README.md).

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
| [Operations runbook](lifecycle/09-operations/output/runbook.md) | Canonical local start path for operators |
| [HVE lifecycle guide](docs/guides/README.md) | How we use HVE stage-by-stage on PulseBoard |
| [Lifecycle folders](lifecycle/README.md) | Input/output locations per stage |
| [MVP framing](lifecycle/02-discovery/input/mvp-framing.md) | Accepted product boundaries |

## Status

Discovery in progress. Application code under `src/pulseboard/` will follow product definition and backlog breakdown.
