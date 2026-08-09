<!-- markdownlint-disable-file -->
# Changes — Issue #4 display name identity

* Date: 2026-08-09
* Plan: lifecycle/06-implementation/output/issue-04/plan.md
* Implement summary: lifecycle/06-implementation/output/issue-04/implement.md
* Validation: pytest identity + status_repository + instance_today — 18 passed (hve-env 3.12.13)

## Added

* src/pulseboard/identity.py
* src/pulseboard/app.py
* tests/test_identity.py

## Modified

* pyproject.toml — fastapi, uvicorn, python-multipart; httpx in dev

## Removed

* (none)

## Deviations

* python-multipart required for Form POST
* swagger_ui_oauth2_redirect_url=None for AC-P-022 cleanliness
* AC-P-022 path checks tightened vs substring oauth false positive
