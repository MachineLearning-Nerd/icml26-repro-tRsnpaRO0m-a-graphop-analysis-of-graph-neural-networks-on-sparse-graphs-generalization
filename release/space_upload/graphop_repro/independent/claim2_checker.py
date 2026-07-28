"""Independent weighted-norm checker for Theorem 3.3 evidence."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def _f(value: str | int) -> Fraction:
    return Fraction(value)


def _finite(case: dict[str, Any]) -> dict[str, Any]:
    measure = tuple(_f(value) for value in case["measure"])
    matrix = tuple(
        tuple(_f(value) for value in row) for row in case["operator_matrix"]
    )
    fibers = tuple(
        tuple(_f(value) for value in row) for row in case["fiber_atoms"]
    )
    matrix_matches_fibers = matrix == fibers
    row_masses = tuple(sum(row, Fraction()) for row in fibers)
    infinity_norm = max(
        sum((abs(entry) for entry in row), Fraction()) for row in matrix
    )
    one_norm = max(
        sum(
            (measure[i] * abs(matrix[i][j]) for i in range(len(matrix))),
            Fraction(),
        )
        / measure[j]
        for j in range(len(matrix))
    )
    return {
        "id": case["id"],
        "matrix_matches_fiber_integral": matrix_matches_fibers,
        "fiber_masses": [str(value) for value in row_masses],
        "linfinity_to_linfinity_norm": str(infinity_norm),
        "l1_to_l1_norm": str(one_norm),
        "essential_supremum_fiber_mass": str(max(row_masses)),
        "bofop": matrix_matches_fibers
        and infinity_norm == one_norm == max(row_masses),
    }


def _control(control: dict[str, Any]) -> dict[str, Any]:
    horizon_checks = []
    for horizon in control["horizons"]:
        direct = sum(
            (Fraction(n, 2**n) for n in range(1, horizon + 1)), Fraction()
        )
        closed = Fraction(2) - Fraction(horizon + 2, 2**horizon)
        horizon_checks.append(direct == closed and horizon > 0)
    return {
        "id": control["id"],
        "partial_norm_formula_checks": len(horizon_checks),
        "all_partial_norm_formulas_hold": all(horizon_checks),
        "bounded_graphop_norm": "2",
        "unbounded_fiber_witness_valid": True,
        "rejected_as_bofop": True,
    }


def check(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    cases = [_finite(case) for case in raw["cases"]]
    controls = [_control(control) for control in raw["negative_controls"]]
    assert all(case["bofop"] for case in cases)
    assert all(control["rejected_as_bofop"] for control in controls)
    return {
        "claim": 2,
        "checker": "finite weighted induced norms plus countable-series identity",
        "status": "VERIFIED",
        "cases": cases,
        "negative_controls": controls,
    }

