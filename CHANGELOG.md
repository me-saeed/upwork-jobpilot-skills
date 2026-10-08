# Changelog

## 1.0.1 - 2026-10-08

Corrected field paths after a read-only smoke test on a freelancer account. No proposal was submitted.

- Connects wallet is `balance.connectsBalance`. `product_credits` stays separate.
- Proposal status is nested at `status.status` and `status.status_label`.
- Client hires on `get` are `client_record.jobs_with_hires`. `smart_search` may include `client.total_hires`. `total_posted_jobs` is still not a hire count.
- `screening_questions` can be present on `find_jobs` `get`. Job text may be wrapped in `untrusted_participant_content`.
- `applicationsBidStats` amounts have no stated unit.

## 1.0.0 - 2026-10-08

First public skill pack for the official Upwork MCP.

- `upwork-smart-job-finder` searches Best Matches, Most Recent, and keyword title searches.
- `upwork-job-fit-analyzer` scores one job and renormalizes missing dimensions.
- `upwork-proposal-studio` drafts from live profile data and an optional local profile. It does not submit.
- `upwork-connects-advisor` compares Connects cost with the wallet and submits only after two confirmations.
- `upwork-application-tracker` reads proposal statuses and computes rates only from a complete page set.

The capability matrix records the MCP schemas checked on this date. Profile-boost ads cannot be started through `boost_profile`.
