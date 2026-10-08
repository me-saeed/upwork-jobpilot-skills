# Hacker News

Title: Show HN: Agent skills for the official Upwork MCP

Body:

Upwork shipped an official MCP server. Their agent plugin covers hiring and a single write-proposal flow. I wanted a freelancer path that stops between "find", "is this worth Connects", and "send".

Upwork JobPilot Skills is a small MIT repo of Agent Skills. They call the official MCP only. Search and drafts are read-only. A proposal is submitted through Upwork's preview, and only after a second confirmation. The skills do not start profile-boost ads, because that tool returns a link to the website instead of creating the spend.

There is no hosted service and no extra account. You connect Upwork's server yourself, then:

npx skills add YOUR_GITHUB_USERNAME/upwork-jobpilot-skills

The fit score renormalizes when client or budget fields are missing, so a blank is not stored as a zero. Tests are schema and instruction checks. They do not spend Connects.

Independent project. Not affiliated with Upwork.
