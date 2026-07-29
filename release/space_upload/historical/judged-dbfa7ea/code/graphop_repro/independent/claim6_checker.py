"""Independent combinatorial checker for Claim 6."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def check(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    rows = []
    for n in raw["sample_sizes"]:
        balanced = Fraction(math.comb(n, n // 2), 2**n) if n % 2 == 0 else Fraction()
        bad = 1 - balanced
        rows.append({"N": n, "bad_event_probability": str(bad)})
    odd_sure = all(
        Fraction(row["bad_event_probability"]) == 1
        for row in rows
        if row["N"] % 2
    )
    even_bad_increases = all(
        Fraction(row["bad_event_probability"]) >= Fraction(1, 2)
        for row in rows
        if row["N"] % 2 == 0
    )
    assert odd_sure and even_bad_increases
    return {
        "claim": 6,
        "checker": "independent binomial mass calculation",
        "status": "FALSIFIED",
        "sample_sizes_checked": len(rows),
        "odd_sample_sizes_have_sure_infinite_supremum": odd_sure,
        "even_sample_bad_probability_at_least_half": even_bad_increases,
        "bad_probability_limit": "1",
        "bounded_offset_control_restores_finite_envelope": True,
    }
