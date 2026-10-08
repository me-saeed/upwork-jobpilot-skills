# Roadmap

v1 is the find, score, draft, submit, and review loop. These are candidates for 1.1 after someone checks `get_tool_help` again. They are not implemented.

## upwork-profile-reviewer

`update_profile` can preview a new title (max 70 characters), overview (max 5000), and a full skill list (max 20, and it replaces the set). Confirm with `confirm_preview` using the returned type, such as `profile_update_title`. The same tool can edit employment, education, languages, video URL, and availability capacity. It has no hourly-rate action and no portfolio-project action. v1 leaves those on upwork.com.

## upwork-client-brief-analyzer

A read-only pass over `find_jobs` `get`: screening questions, preferred qualifications, and contradictions in the post. The fit analyzer already covers the apply decision. This is only worth a skill if the brief review is useful on its own.

## upwork-interview-prep

Use `list_freelancer_proposals` `get` insights when `insights_available` is true. If it is false, the skill must stop rather than invent applicant averages.

## upwork-portfolio-matcher

Rank `list_highlights` against one job and return ids the user can pass to `portfolio_project_ids`. Proposal studio already asks for this at draft time. A separate skill needs a clearer job than "pick two projects".

## upwork-freelance-insights

Trends across a fully paged tracker window: which budgets got to Offered or Hired. Do not ship this on a one-page sample. Do not publish a success rate for the product itself.

Out of scope until the MCP exposes them: starting a profile-boost ad, turning the Availability Badge on, and writing the hourly rate.
