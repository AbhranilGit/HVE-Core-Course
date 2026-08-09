<!-- markdownlint-disable-file -->
# Research — Issue #2 SQLite schema and status repository

* Date: 2026-08-09
* Phase: 1 Research only
* Difficulty: Medium (greenfield persistence; clear AC; empty package)
* Canonical write-up: lifecycle/06-implementation/output/issue-02/research.md
* Production code: none
* Plan/Implement: not started

## Scope

TEMP-1 / GitHub #2 AC-P-001–004 from backlog-snapshot.

## Selected approach (summary)

* stdlib sqlite3; no new runtime deps
* Table statuses with UNIQUE(display_name, status_day)
* status_day as ISO date text; optional created_at/updated_at
* init_db + upsert + list_by_day repository surface
* PULSEBOARD_DB_PATH override; default local file path
* No FastAPI routes, cookies, instance_today, UI in this issue
* Narrow persistence tests recommended; full product tests remain #10

## Open questions

None blocking. Defaults recorded in canonical research.md.

## Next

User verifies issue-02/README.md Research gate → /rpi continue=2 Plan.
