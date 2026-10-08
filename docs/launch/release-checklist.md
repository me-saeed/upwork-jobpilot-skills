# Release checklist

Use this when tagging v1.0.0. Do not check an item you did not do.

- [ ] `python3 tests/validate_skills.py` passes
- [ ] `python3 -m unittest discover -s tests -v` passes
- [ ] GitHub Actions validate workflow is green on the default branch
- [x] README install command uses `me-saeed/upwork-jobpilot-skills`
- [ ] `templates/profile.example.md` is still fictional
- [ ] `git status` shows no `profile.md`, `preferences.md`, `.env`, or history file
- [ ] Capability matrix date is still true, or it was re-checked with `get_tool_help`
- [ ] CHANGELOG version matches the git tag
- [ ] A fresh agent can load `upwork-smart-job-finder` and refuse to submit from `upwork-proposal-studio`
- [ ] Live read-only smoke test is optional. If you do one, use `find_jobs` `get` on a public URL and do not confirm a preview
- [ ] Launch posts in `docs/launch/` have the real repository URL filled in
- [ ] The repository description says it is not an official Upwork project

Suggested GitHub topics: `upwork`, `mcp`, `agent-skills`, `freelance`, `cursor`, `claude`, `proposals`

Suggested repository description: Agent Skills that find Upwork jobs, draft proposals, and submit through the official MCP only after you confirm. Not an Upwork product.
