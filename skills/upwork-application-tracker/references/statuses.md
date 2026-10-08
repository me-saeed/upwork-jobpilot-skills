# Proposal statuses

`list_freelancer_proposals` `list` takes one `status` per call. The default is `Accepted`. Pass the status you mean.

On each proposal the live payload nests the result: read `status.status` and `status.status_label`. Do not assume those keys sit on the proposal root. A checked response used `status_label` "Submitted" for `status` `Accepted`.

| status | What to tell the user |
|---|---|
| Pending | Still processing. Not proof the proposal is live until a later read shows it submitted. |
| Accepted | Submitted and validated. Not "the client accepted you". Prefer `status_label`. |
| Offered | An offer exists. This is a response. It is not, by itself, an interview. |
| Hired | A hire was recorded by Upwork. |
| Activated | Invitation accepted. |
| Declined | The proposal was declined. Say declined, not "no response", when this status is what you retrieved. |
| Withdrawn | The freelancer withdrew it. |
| Archived | Archived. Do not infer why. |

`boosted` and `terms.connectsBid` on `list` or `get` are the stored boost. Report `terms.connectsBid` when it is present.

`get` may include `insights` about how many proposals the client opened, shortlisted, or messaged, and average applicant stats. Present them as activity on that job. If `insights_available` is false, relay `insights_note` and do not fill in numbers.

Invitations use `invitations`, not `list`. The invitation `id` is the `invitation_uid` for a later accept or decline in the Connects skill. This skill does not accept or decline.

A freelancer cannot open the first proposal message. `get_room` may return no room. Say the client has to message first. Do not keep retrying a not-found room.
