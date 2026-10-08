# Local history

Path: `~/.upwork-jobpilot/history.json`

Create the file only after a verified submission, or when the user asks to store a note. If the JSON is invalid, show the parse error and do not overwrite the file.

```json
{
  "version": 1,
  "seen_job_ids": ["1000000001"],
  "applications": [
    {
      "job_id": "1000000001",
      "title": "",
      "url": "",
      "proposed_at": "2026-10-08T12:00:00Z",
      "source": "mcp",
      "mcp_status": "Accepted",
      "mcp_status_label": "Submitted",
      "local_note": "",
      "connects_cost": 8,
      "boost_connects": null,
      "outcome_note": ""
    }
  ],
  "connects_log": [
    {
      "at": "2026-10-08T12:00:00Z",
      "job_id": "1000000001",
      "connects": 8,
      "kind": "proposal",
      "source": "mcp"
    }
  ]
}
```

Rules:

- `source` is `mcp` or `local`. A `local` row is the user's note. It is not proof of submission.
- `kind` is `proposal` or `boost`.
- Add the numeric `job_id` to `seen_job_ids` when you record an application.
- One application per `job_id`. On conflict, keep the MCP status and status label. Append the user's comment to `local_note` or `outcome_note` instead of replacing `mcp_status`.
- `connects_log` entries require `source` `mcp` and a verification read from the same session.
- Do not store `org_uid`, cover letters, or access tokens in this file.
