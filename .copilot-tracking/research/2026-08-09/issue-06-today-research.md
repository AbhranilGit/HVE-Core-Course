<!-- markdownlint-disable-file -->
# Research — Issue #6 instance today helper

* Date: 2026-08-09
* Phase: 1 Research only
* Difficulty: Simple–medium (stdlib zoneinfo; #2 already stores status_day)
* Canonical: lifecycle/06-implementation/output/issue-06/research.md
* Production code: none
* #2 blocker: none

## Selected approach (summary)

* New module src/pulseboard/today.py
* instance_today() -> date; PULSEBOARD_TZ via zoneinfo; host local default
* Injectable now/tz for tests
* Thin list_statuses_for_today + default day string for AC-P-012/013 contracts
* No FastAPI, no schema change

## Next

User verifies issue-06/README.md Research gate → /rpi continue=2 Plan.
