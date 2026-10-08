# Local preferences

Copy to `.upwork-jobpilot/preferences.md`, `./preferences.md`, or `~/.upwork-jobpilot/preferences.md`. The project copies are gitignored when you use this repository's `.gitignore`. Home-directory copies stay on your machine.

Missing fields are skipped. A missing budget is not treated as a bad job.

```markdown
# Preferences

preferred_categories:
  - Web, Mobile & Software Dev
preferred_hourly_rate: 40
minimum_fixed_price: 500
connects_budget: 60
preferred_duration:
  - 1_to_3_months
  - 3_to_6_months
job_types:
  - fixed
  - hourly
client_preferences:
  verified_payment_only: true
  avoid_countries: []
notes: Prefer a clear scope over a broad retainer.
```

`preferred_hourly_rate` and `minimum_fixed_price` are your floors. The agent may ask whether to use the hourly number as `charged_amount`. It does not invent a rate when this file is absent. `avoid_countries` is your list, empty by default. `connects_budget` is the most you want to spend in the session the agent is helping with, not an Upwork setting.
