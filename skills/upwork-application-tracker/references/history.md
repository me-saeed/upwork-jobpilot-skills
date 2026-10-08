# Local history

Path: `~/.upwork-jobpilot/history.json`

Reads must tolerate a missing file. Do not create the file on a read. If JSON parsing fails, say so and skip the file.

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
  "connects_log": []
}
```

`source` is `mcp` or `local`. Platform status is `mcp_status` plus `mcp_status_label`. A local interview or "I applied" belongs in `outcome_note` or `local_note` and stays labeled unverified when `source` is `local` or when no MCP row exists.

One row per `job_id`. Do not replace `mcp_status` with a local claim. Do not store `org_uid`, cover-letter bodies, or tokens.

The Connects advisor is the skill that appends `connects_log` after a verified submit. This skill only reads that log.
