# Stage 6 — RPI outputs

For each GitHub issue, persist and verify **research → plan → implement** before moving on.

```text
output/
├── issue-02/
│   ├── README.md      # verification checklist (gate)
│   ├── research.md    # /rpi-research result
│   ├── plan.md        # /rpi-plan result
│   └── implement.md   # /rpi-implement summary + file list
├── issue-06/
…
```

| Phase | Artifact | Done when |
| --- | --- | --- |
| Research | `research.md` | Findings recorded; no production code yet; checklist §Research checked |
| Plan | `plan.md` | Steps + AC checks recorded; matches research; checklist §Plan checked |
| Implement | `implement.md` + code in `src/` / `tests/` | AC met; evidence noted; checklist §Implement checked |

Also keep HVE session evidence under `.copilot-tracking/` when the agent writes it.  
**Lifecycle files above are the durable per-issue trail for this course.**

Prompts: [`../prompt/README.md`](../prompt/README.md).
