"""Fit-score math shared with skills/upwork-job-fit-analyzer/references/scoring.md.

Agents follow the markdown. This module lets CI check the worked examples.
"""

from __future__ import annotations

WEIGHTS = {
    "skills": 30,
    "portfolio": 20,
    "budget": 15,
    "clarity": 15,
    "client": 10,
    "competition": 10,
}

BANDS = (
    (75, "Strong Fit"),
    (50, "Worth Reviewing"),
)


def score(dimensions: dict) -> dict:
    """Score available dimensions. None means the dimension is omitted."""
    unknown = [key for key in WEIGHTS if key not in dimensions]
    if unknown:
        raise KeyError("missing keys: " + ", ".join(unknown))

    available = {
        key: value
        for key, value in dimensions.items()
        if value is not None
    }
    if not available:
        return {
            "overall": None,
            "band": None,
            "weights_used": 0,
            "omitted": list(WEIGHTS),
        }

    for key, value in available.items():
        if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= 100:
            raise ValueError(f"{key} must be an integer from 0 to 100 or null")

    weight_sum = sum(WEIGHTS[key] for key in available)
    weighted = sum(available[key] * WEIGHTS[key] for key in available)
    overall = _round_half_up(weighted, weight_sum)
    return {
        "overall": overall,
        "band": _band(overall),
        "weights_used": weight_sum,
        "omitted": [key for key in WEIGHTS if dimensions[key] is None],
    }


def _round_half_up(numerator: int, denominator: int) -> int:
    quotient, remainder = divmod(numerator, denominator)
    if remainder * 2 >= denominator:
        return quotient + 1
    return quotient


def _band(overall: int) -> str:
    for threshold, name in BANDS:
        if overall >= threshold:
            return name
    return "Low Fit"
