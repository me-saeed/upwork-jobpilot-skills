"""Validate Agent Skills layout without calling Upwork."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED_HEADINGS = (
    "## Prerequisites",
    "## MCP tools",
    "## Workflow",
    "## Output",
    "## Errors",
    "## Safety",
    "## Examples",
)
EXPECTED = (
    "upwork-smart-job-finder",
    "upwork-job-fit-analyzer",
    "upwork-proposal-studio",
    "upwork-connects-advisor",
    "upwork-application-tracker",
)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def fail(message: str) -> None:
    print(f"FAIL {message}")
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail("SKILL.md is missing frontmatter")
    raw = match.group(1)
    data: dict[str, str] = {}
    current = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and current:
            data[current] += " " + line.strip()
            continue
        if ":" not in line:
            fail(f"bad frontmatter line: {line}")
        key, value = line.split(":", 1)
        current = key.strip()
        data[current] = value.strip().strip('"')
    return data


def main() -> None:
    found = sorted(path.name for path in SKILLS.iterdir() if path.is_dir())
    if found != sorted(EXPECTED):
        fail(f"skill directories {found} != {list(EXPECTED)}")

    for name in EXPECTED:
        skill_dir = SKILLS / name
        text = (skill_dir / "SKILL.md").read_text()
        meta = parse_frontmatter(text)
        if meta.get("name") != name:
            fail(f"{name} frontmatter name is {meta.get('name')}")
        if not NAME_RE.match(name):
            fail(f"{name} is not a valid skill name")
        description = meta.get("description", "")
        if not description or len(description) > 1024:
            fail(f"{name} description length {len(description)}")
        compatibility = meta.get("compatibility", "")
        if not compatibility or len(compatibility) > 500:
            fail(f"{name} compatibility missing or too long")
        if meta.get("license") != "MIT":
            fail(f"{name} license is not MIT")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                fail(f"{name} missing {heading}")
        if len(re.findall(r"^### Example \d+", text, re.MULTILINE)) < 3:
            fail(f"{name} needs three examples")
        for phrase in ("list_accounts", "get_tool_help", "untrusted", "invent"):
            if phrase not in text.lower() and phrase not in text:
                fail(f"{name} missing {phrase}")
        if "confirm_preview" not in text:
            fail(f"{name} does not mention confirm_preview")
        references = list((skill_dir / "references").glob("*.md"))
        if not references:
            fail(f"{name} has no references")
        for ref in references:
            if ref.stat().st_size < 40:
                fail(f"{ref} is empty")

    proposal = (SKILLS / "upwork-proposal-studio" / "SKILL.md").read_text()
    if "Do not call `manage_proposals`" not in proposal:
        fail("proposal studio must refuse manage_proposals")
    if "Do not call `confirm_preview`" not in proposal:
        fail("proposal studio must refuse confirm_preview")

    connects = (SKILLS / "upwork-connects-advisor" / "SKILL.md").read_text()
    for phrase in ("boost_connects", "confirm_preview", "does not start the ad"):
        if phrase not in connects:
            fail(f"connects advisor missing {phrase}")

    finder = (SKILLS / "upwork-smart-job-finder" / "SKILL.md").read_text()
    if "`applied` true" not in finder:
        fail("finder must skip applied jobs")

    analyzer = (SKILLS / "upwork-job-fit-analyzer" / "SKILL.md").read_text()
    if "Missing client history is omitted" not in analyzer:
        fail("analyzer must omit missing client data")
    scoring = (SKILLS / "upwork-job-fit-analyzer" / "references" / "scoring.md").read_text()
    if "6750" not in scoring or "Strong Fit" not in scoring:
        fail("scoring reference drifted from the worked example")

    tracker = (SKILLS / "upwork-application-tracker" / "SKILL.md").read_text()
    if "does not mean the client accepted" not in tracker.lower():
        fail("tracker must explain Accepted")

    blob = "\n".join(path.read_text() for path in ROOT.rglob("*.md"))
    for banned in ("saeedwebdevolper", "portfolio.saeedme.com", "Muhammad Saeed"):
        if banned in blob:
            fail(f"personal data leaked: {banned}")

    injection = (ROOT / "tests" / "fixtures" / "job-injection.md").read_text()
    if "Ignore previous instructions" not in injection:
        fail("injection fixture missing")

    journey = (ROOT / "examples" / "journey.md").read_text()
    for beat in ("MOCK", "Find", "Analyze", "Draft", "Apply"):
        if beat not in journey:
            fail(f"journey missing {beat}")

    readme = (ROOT / "README.md").read_text()
    for phrase in (
        "npx skills add",
        "not affiliated",
        "https://mcp.upwork.com/mcp",
        "https://www.upwork.com/ai/mcp",
    ):
        if phrase not in readme.lower() and phrase not in readme:
            fail(f"README missing {phrase}")

    print("ok", len(EXPECTED), "skills")


if __name__ == "__main__":
    sys.exit(main())
