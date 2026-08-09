"""Domain models for PulseBoard persistence."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Status:
    """One person's status snapshot for one calendar day."""

    display_name: str
    status_day: str  # ISO calendar date YYYY-MM-DD
    doing: str = ""
    blocked: str = ""
    next: str = ""
    id: int | None = None
    created_at: str | None = None
    updated_at: str | None = None
