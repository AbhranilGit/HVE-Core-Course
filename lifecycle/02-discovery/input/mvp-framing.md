# PulseBoard MVP framing

**Status:** Accepted

PulseBoard is a local-first team status board. People post **doing / blocked / next**. A board view shows today’s updates.

## In scope (MVP)

- Create a status update with doing / blocked / next
- List / board view for a given day (default: today)
- Simple local identity (demo login or name field — decide in ADR later)
- Runnable on a developer machine with SQLite

## Out of scope (MVP)

- SSO / OAuth
- Notifications / email / Slack
- Mobile app
- Multi-tenant SaaS hosting
- Real-time websockets (unless a later sprint explicitly pulls them in)
