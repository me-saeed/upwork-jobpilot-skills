# Boost and submit

Call `get_tool_help` for `manage_proposals` if a parameter is rejected. The live schema wins over this note.

## Before create

1. `find_jobs` `get` so you have the numeric job id. `create` needs that numeric id as `job_reference`, not the `~02…` ciphertext. `get` accepts either form plus a full URL.
2. `list_freelancer_proposals` `invitations`. If this job invited the account, use `accept_invitation` with `invitation_uid` from that list. Do not `create`. Upwork rejects the duplicate.
3. `list_freelancer_proposals` `list` for `Pending` and `Accepted`. If a proposal exists, stop and show `status_label`. `Accepted` means the proposal was submitted and validated, not that the client accepted the freelancer.
4. Cover letter from the user or from the draft they approved in this conversation. Maximum 5000 characters. Ask them to shorten a longer letter.
5. `charged_amount` is a number they approved. Suggest the saved hourly rate only as a question. Never substitute a market rate.
6. Ask whether to attach files and whether to highlight portfolio projects or certificates. For files, `start_attachment_upload` with `context` `proposals` for a normal application. Use the context `get_tool_help` requires for an invitation. Pass returned `file_uid` values. For highlights, TALENT accounts can pass `certificate_ids` and `portfolio_project_ids` from `get_profile` `list_highlights`. Skip `list_highlights` for an agency.
7. Screening answers are required when the job has questions. If the create preview returns questions you did not answer, collect answers and call `create` again. Do not confirm a preview that is missing required answers.

## Preview

Get an explicit yes, then:

- Uninvited job: `manage_proposals` `create` without `boost_connects`.
- Invitation: `accept_invitation`. Do not send `boost_connects` on that action unless `get_tool_help` lists it.

Show the preview:

- `connects_cost` and `connects_balance`
- `can_apply`
- unmet preferred qualifications when present (advisory; they do not block submission)
- `boost.available`. If false, relay `boost.reason` and do not offer a boost.
- `boost.current_top_bids` when `current_top_bids_available` is not false. If it is false, say the bids are unknown. Do not say nobody boosted.
- `boost.recommended_connects` and `boost.max_boost_connects` when present. `recommended_connects` is the smallest bid the preview says takes a top slot. The user may choose another integer inside the preview's limits. A bid below the recommended amount is refused.
- `boost.recommendation` of `skip` means you should not push a boost. Still do not add one unless they insist after hearing that note.

If they want a boost, call `create` again with their `boost_connects` integer and present the new preview. Do not confirm the earlier preview.

Agency accounts with several teams: omit `team_org_id` until the error lists the teams, then ask the user to pick one.

## Confirm

Ask a second time, naming the Connects cost and any boost bid. Then `confirm_preview` action `confirm` with the `type` and `preview_id` from that preview. Send no other stored fields.

Verify:

- `list_freelancer_proposals` `list` with `status` `Pending`
- If they boosted, `get` that proposal and report `terms.connectsBid` as the stored bid. Say if it differs from the number they approved. It cannot be edited here.

If confirm says the bid no longer takes a paid slot, nothing was submitted. Show the new bids and wait.

Write `~/.upwork-jobpilot/history.json` only after this verification. Set `source` to `mcp`. Do not write a spend when verification fails.

## Visibility

`boost_profile` `get_status` reads the Availability Badge and any profile-boost ad.

`create_profile_boost`, `toggle_availability_badge` with `enabled` true, and `manage_profile_boost` restart or update return a link. They do not start or increase spend. Show the link and stop.

`toggle_availability_badge` with `enabled` false, and `manage_profile_boost` `stop` or `pause`, return a preview. Show it, get a yes, then `confirm_preview` with the returned type. Those types may be `availability_badge_toggle` or `profile_boost_manage`. Use the type on the preview, not a guess.

A profile-boost confirm is not a proposal boost. Keep the two words distinct when you talk to the user.
