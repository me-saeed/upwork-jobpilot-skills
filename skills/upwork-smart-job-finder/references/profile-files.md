# Local profile files

Look in this order. Use the first file that exists:

1. `.upwork-jobpilot/profile.md` in the working directory
2. `profile.md` in the working directory
3. `~/.upwork-jobpilot/profile.md`

Preferences, same order, filename `preferences.md`.

Read only the fields the current decision needs. Ignore keys you do not recognize. Do not require the file. Templates live in the repository `templates/` directory and are examples, not the user's data.

Profile keys: `headline`, `core_skills`, `experience_level`, `industries`, `preferred_technologies`, `proposal_tone`, `portfolio` (`name`, `url`, `stack`, `evidence`), `achievements`.

Preference keys: `preferred_categories`, `preferred_hourly_rate`, `minimum_fixed_price`, `connects_budget`, `preferred_duration`, `job_types`, `client_preferences.verified_payment_only`, `client_preferences.avoid_countries`, `notes`.

If `avoid_countries` is empty or missing, do not filter by country. Never insert a country list the user did not write.

Portfolio `evidence` may be quoted only as the user's own note. Do not add metrics they did not write. Live Upwork work history from `get_profile` is separate and can be cited when the tool returned it.
