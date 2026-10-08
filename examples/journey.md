# Journey (mock)

This script uses fake tool results. It is not a live Upwork session and it spends no Connects.

## Find

User: Find the 10 best React and Next.js jobs for my experience, with reasonable budgets and credible clients.

MOCK `smart_search` returns two Best Matches. MOCK `search` title React and title Next.js return three jobs. One row has `applied` true and is dropped. The agent calls MOCK `get` on the top three.

It shows:

- Clinic booking rebuild. https://www.upwork.com/jobs/~02mock001. Fixed price $1,500. Payment verified. Proposals tier "5 to 10". Connects cost 8 from `get`. Reason: local profile lists a scheduling app in Next.js. Risk: `client_record.total_hires` is 1.
- Design system cleanup. https://www.upwork.com/jobs/~02mock002. Hourly $35–$50. Connects cost unknown on the search row, 6 after `get`. Reason: highlight title matches React. Risk: description does not name a deadline.
- Marketing site. Shown from the search row only. Hire count unknown. Connects cost unknown.

The agent says Most Recent is also available and does not draft a letter.

## Analyze

User: Analyze the first job.

MOCK `get` is reused. Skills 90, portfolio 80, budget 70, clarity 60, client omitted because this mock omits `client_record` on purpose, competition 50. Weights used 90. Overall 75. Strong Fit. Connects cost 8. The agent says the score is not a chance of winning.

## Draft

User: Write a short proposal from my real Next.js project.

The agent checks MOCK invitations (none) and MOCK proposals (none). It cites the scheduling app from the local profile and does not add a revenue figure. It does not call `manage_proposals`.

## Apply

User: Apply. Bid $1,500. Do not boost.

The agent repeats the cost and the bid and waits. After the user says yes, MOCK `create` returns `connects_cost` 8, `connects_balance` 60, `boost.available` true, and `boost.current_top_bids` [4]. The agent asks again. The user says submit without a boost. Only then does the agent call `confirm_preview`. MOCK verification returns status Pending. The agent says the proposal preview was confirmed in this mock, and it does not write a real history file from this document.
