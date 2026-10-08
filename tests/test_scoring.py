import json
import unittest
from pathlib import Path

from scoring import score

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "scoring_cases.json"


class ScoringTests(unittest.TestCase):
    def test_fixtures(self) -> None:
        cases = json.loads(FIXTURES.read_text())
        self.assertGreaterEqual(len(cases), 4)
        for case in cases:
            with self.subTest(case=case["name"]):
                result = score(case["dimensions"])
                self.assertEqual(result["overall"], case["overall"])
                self.assertEqual(result["band"], case["band"])
                self.assertEqual(result["weights_used"], case["weights_used"])

    def test_rejects_out_of_range(self) -> None:
        dimensions = {
            "skills": 101,
            "portfolio": 0,
            "budget": 0,
            "clarity": 0,
            "client": 0,
            "competition": 0,
        }
        with self.assertRaises(ValueError):
            score(dimensions)

    def test_missing_key(self) -> None:
        with self.assertRaises(KeyError):
            score({"skills": 10})


if __name__ == "__main__":
    unittest.main()
