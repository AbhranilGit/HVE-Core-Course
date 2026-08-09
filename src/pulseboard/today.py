"""Instance-level calendar today for PulseBoard.

Day boundary rules (ADR today-instance-timezone; operators / later runbook #8):

* Today is the calendar date in the **instance timezone**.
* Default timezone is the **host local** zone of the machine running the process.
* Optional override: environment variable ``PULSEBOARD_TZ`` set to a valid IANA
  name (for example ``America/Los_Angeles``, ``UTC``, ``Asia/Kolkata``).
* Unset or blank ``PULSEBOARD_TZ`` keeps host local time.
* Invalid IANA names raise ``ValueError`` (fail loud for misconfiguration).

Persistence stores ``status_day`` as ISO ``YYYY-MM-DD`` text; use
:func:`default_status_day_str` when create omits another day (#5 will wire HTTP).
"""

from __future__ import annotations

import os
from datetime import date, datetime, tzinfo
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

ENV_TZ = "PULSEBOARD_TZ"


def resolve_instance_tz() -> tzinfo:
    """Return the instance timezone (env override or host local)."""
    raw = os.environ.get(ENV_TZ)
    if raw is not None and raw.strip():
        name = raw.strip()
        try:
            return ZoneInfo(name)
        except ZoneInfoNotFoundError as exc:
            raise ValueError(
                f"Invalid {ENV_TZ} IANA timezone name: {name!r}"
            ) from exc
    local = datetime.now().astimezone().tzinfo
    if local is None:  # pragma: no cover - extremely unlikely
        return ZoneInfo("UTC")
    return local


def instance_today(
    *,
    now: datetime | None = None,
    tz: tzinfo | None = None,
) -> date:
    """Return the instance calendar date for ``now`` in the instance timezone.

    Parameters
    ----------
    now:
        Instant to evaluate. If omitted, uses the current clock.
        Naive datetimes are treated as wall time in the resolved instance tz
        (``replace(tzinfo=...)``). Aware datetimes are converted with
        ``astimezone``.
    tz:
        Explicit timezone; if omitted, uses :func:`resolve_instance_tz`.
    """
    resolved = tz if tz is not None else resolve_instance_tz()
    if now is None:
        current = datetime.now(tz=resolved)
    elif now.tzinfo is None:
        current = now.replace(tzinfo=resolved)
    else:
        current = now.astimezone(resolved)
    return current.date()


def default_status_day_str(
    *,
    now: datetime | None = None,
    tz: tzinfo | None = None,
) -> str:
    """ISO ``YYYY-MM-DD`` default for status create when no other day is chosen."""
    return instance_today(now=now, tz=tz).isoformat()
