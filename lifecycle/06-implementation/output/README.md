# Stage 6 — RPI outputs

For each GitHub issue, persist and verify **research → plan → implement** before moving on.

Invoke with **RPI Agent** and `/rpi continue={1|2|3} task=...`.

```text
output/
├── issue-02/
│   ├── README.md      # verification checklist (gate)
│   ├── research.md    # /rpi continue=1
│   ├── plan.md        # /rpi continue=2
│   └── implement.md   # /rpi continue=3 summary + file list
├── issue-06/
…
```

| Phase | `/rpi` flag | Artifact | Done when |
| --- | --- | --- | --- |
| Research | `continue=1` | `research.md` | Findings recorded; no production code yet; checklist §Research checked |
| Plan | `continue=2` | `plan.md` | Steps + AC checks recorded; matches research; checklist §Plan checked |
| Implement | `continue=3` | `implement.md` + code in `src/` / `tests/` | AC met; evidence noted; checklist §Implement checked |

Also keep HVE session evidence under `.copilot-tracking/` when the agent writes it.  
**Lifecycle files above are the durable per-issue trail for this course.**

Prompts: [`../prompt/README.md`](../prompt/README.md).
