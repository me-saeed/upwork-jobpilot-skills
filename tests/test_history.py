import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = Path(__file__).resolve().parent / "fixtures" / "history.sample.json"


class HistoryTests(unittest.TestCase):
    def test_sample_shape(self) -> None:
        data = json.loads(SAMPLE.read_text())
        self.assertEqual(data["version"], 1)
        self.assertIn("1000000001", data["seen_job_ids"])
        application = data["applications"][0]
        self.assertEqual(application["source"], "mcp")
        self.assertEqual(application["mcp_status"], "Accepted")
        self.assertNotIn("org_uid", json.dumps(data))
        entry = data["connects_log"][0]
        self.assertEqual(entry["kind"], "proposal")
        self.assertEqual(entry["source"], "mcp")

    def test_skill_docs_agree(self) -> None:
        connects = (
            ROOT / "skills" / "upwork-connects-advisor" / "references" / "history.md"
        ).read_text()
        tracker = (
            ROOT / "skills" / "upwork-application-tracker" / "references" / "history.md"
        ).read_text()
        for text in (connects, tracker):
            self.assertIn("version", text)
            self.assertIn('"source": "mcp"', text)
            self.assertIn("local", text)
            self.assertIn("org_uid", text)


if __name__ == "__main__":
    unittest.main()
