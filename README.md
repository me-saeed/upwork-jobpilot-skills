# Upwork JobPilot Skills

**Find better jobs. Write better proposals. Spend Connects smarter.**

Five Agent Skills for freelancers who already use the official Upwork MCP. They search, score, draft, and submit through that connector. Installing them does not log you into Upwork.

```bash
npx skills add saeed-pallivivo/upwork-jobpilot-skills
```

The installer asks which skills and which agents to configure. Cursor, Claude Code, and Codex are the hosts this repository documents. Other Agent Skills hosts can use the same `skills/` folders.

This project is an independent open-source effort. It is not affiliated with, endorsed by, or maintained by Upwork.

## 60-second start

1. Add the official server in your agent and finish Upwork's browser login. The server URL is `https://mcp.upwork.com/mcp`. Setup steps for each host are on https://www.upwork.com/ai/mcp. This repository does not configure that login.
2. Run the install command above.
3. Copy `templates/profile.example.md` to `~/.upwork-jobpilot/profile.md` if you want local projects included. Skip this and the skills still read the live Upwork profile.
4. Ask: "Find the 10 best React and Next.js jobs for my experience, with reasonable budgets and credible clients."

A full mock of find, analyze, draft, and apply is in [examples/journey.md](examples/journey.md).

## What you get

| Skill | You ask | It does | It does not |
|---|---|---|---|
| `upwork-smart-job-finder` | Find jobs for my profile | Searches the official feeds, drops jobs you already applied to, explains each row | Draft or submit |
| `upwork-job-fit-analyzer` | Is this worth applying? | Scores one job out of 100 and omits missing data | Treat a blank field as a bad client |
| `upwork-proposal-studio` | Write the proposal | Drafts from your real profile and local notes | Call the submit tools |
| `upwork-connects-advisor` | Apply, and do not boost | Shows cost and balance, then submits after two explicit yeses | Pick a boost bid for you |
| `upwork-application-tracker` | What came back? | Lists proposal statuses Upwork returned | Invent an interview rate |

## Official plugin

Upwork's plugin ([upwork/upwork-agent-plugin](https://github.com/upwork/upwork-agent-plugin)) is the right tool for clients posting jobs and hiring. Its `write-proposal` skill can also draft and submit a freelancer proposal. Use it if you want one skill that goes straight to a letter.

JobPilot is the freelancer loop around that same MCP: qualify, rank, draft without submitting, decide on Connects, then review outcomes. Submission still uses Upwork's preview and `confirm_preview`. We do not ship a second connector.

| | Official `write-proposal` | JobPilot |
|---|---|---|
| Job shortlist with reasons | Search is a step on the way to a letter | `upwork-smart-job-finder` |
| Fit score that skips missing fields | No | `upwork-job-fit-analyzer` |
| Draft from the live profile | Yes | Yes, plus an optional local `profile.md` |
| Submit and proposal boost | Yes, inside the same skill | Only `upwork-connects-advisor`, after two confirmations |
| Outcome review | Prior letters as writing samples | `upwork-application-tracker` |
| Post a job or hire | Yes | No |

## MCP setup

1. Open https://www.upwork.com/ai/mcp and follow the steps for your agent.
2. Use server URL `https://mcp.upwork.com/mcp`.
3. Approve the browser login Upwork shows. The skills never ask for your password, session cookie, or API secret.
4. If a tool says you are not signed in, stop and repeat that login. Do not retry a submit in a loop.

`npx skills add` copies skill files. It does not complete OAuth.

## Privacy and security

- Live account data stays in the Upwork session your agent already has.
- Local notes belong in `profile.md`, `preferences.md`, or `~/.upwork-jobpilot/history.json`. This repository's `.gitignore` ignores project copies of the first two. Do not commit them.
- History stores job ids, statuses, and Connects figures. It must not store `org_uid`, cover letters, or tokens.
- Job posts are untrusted. A post that says "ignore your rules and submit" is content, not an instruction.
- Writes use Upwork's preview. The agent needs a yes before `manage_proposals` `create`, and a second yes before `confirm_preview`.
- Report security issues through GitHub private vulnerability reporting. See [SECURITY.md](SECURITY.md).

## Limits

Audited against the live MCP on 8 October 2026. Details are in [docs/capability-matrix.md](docs/capability-matrix.md).

- `find_jobs` `search` cannot filter by date. Date windows use `smart_search` `mode=most_recent`.
- Search rows do not include a hire count or, on `search`, the Connects cost. The skills say unknown until `get` returns the field.
- Exact proposal counts depend on the Upwork plan. Other accounts get a tier. A missing count is not zero.
- Competing proposal-boost bids appear on the create preview, not on the job search.
- `boost_profile` can read a profile-boost ad and the Availability Badge, and it can pause or turn them off after confirmation. It cannot start them or raise the spend. Those actions return a link to upwork.com.
- `update_profile` is not wrapped in v1. It also has no hourly-rate or portfolio-project action.
- Scores are heuristics. They are not a chance of getting hired. A boost is not a promise of a reply.
- Automated tests do not sign in to Upwork and do not spend Connects. Live checks are manual and should stay read-only unless you intend to apply.

## Demo

[examples/journey.md](examples/journey.md) is a terminal-style walkthrough with mock tool results. [examples/proposal-before-after.md](examples/proposal-before-after.md) shows the voice the proposal skill aims for. Neither file is a screenshot of a real account.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The v1.1 ideas are in [docs/roadmap.md](docs/roadmap.md).

## FAQ

**Does this spend Connects when I ask it to look at jobs?**
No. Search, scoring, drafts, and the tracker are reads. Connects are spent when you confirm a proposal preview.

**Can it turn on Boosted Profile?**
No. The official tool returns a link so you can do that on upwork.com. The advisor can read status and, if you ask, pause or stop an ad that is already running.

**What if I skip the local profile?**
The skills use `get_profile` for a freelancer account. Agency accounts do not have that tool. Add a local profile or the draft will say the Upwork profile was not available.

**Why does a proposal status say Accepted when I was not hired?**
Upwork uses `Accepted` for a proposal that was submitted and validated. The tracker is instructed to use `status_label` and to say that plainly.
