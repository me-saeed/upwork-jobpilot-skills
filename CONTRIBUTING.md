# Contributing

Issues and small pull requests are welcome. Please keep the skills accurate to the official Upwork MCP.

## Setup

```bash
python3 tests/validate_skills.py
python3 -m unittest discover -s tests -v
```

CI runs those commands. It does not call Upwork.

## Skills

- One directory under `skills/`, with `SKILL.md` whose `name` matches the directory.
- Follow the Agent Skills spec at https://agentskills.io/specification.
- Keep `SKILL.md` short. Put field tables in `references/`.
- A skill must still make sense after `npx skills add` copies that folder alone. Do not require a sibling skill's files at runtime.
- New MCP behavior needs a `get_tool_help` check. Update `docs/capability-matrix.md` with the date.
- Do not add browser automation, cookie login, or an unofficial Upwork API.

## Safety changes

Submission and Connects rules live in `upwork-connects-advisor`. Other skills stay read-only. Do not move `confirm_preview` into the proposal skill.

## Privacy

Do not commit a real `profile.md`, `preferences.md`, history file, token, or account id. The examples must stay fictional.

## This is not Upwork

Do not imply Upwork ships or endorses this repository.
