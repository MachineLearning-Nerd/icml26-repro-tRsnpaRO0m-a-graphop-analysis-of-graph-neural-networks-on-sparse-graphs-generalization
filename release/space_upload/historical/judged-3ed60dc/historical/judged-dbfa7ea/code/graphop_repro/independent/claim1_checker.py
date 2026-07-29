"""Independent structural checker for Claim 1.

This module deliberately does not import the primary verifier.  It checks the
finite-atomic form of Definition 3.1 through the weighted matrix identities
mu_i A_ij = mu_j A_ji and A_ij >= 0.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def _f(value: str) -> Fraction:
    return Fraction(value)


def _check_case(case: dict[str, Any]) -> dict[str, Any]:
    measure = tuple(_f(value) for value in case["measure"])
    matrix = tuple(tuple(_f(value) for value in row) for row in case["operator_matrix"])
    detailed_balance = [
        measure[i] * matrix[i][j] == measure[j] * matrix[j][i]
        for i in range(len(matrix))
        for j in range(len(matrix))
    ]
    entrywise_nonnegative = [
        entry >= 0 for row in matrix for entry in row
    ]
    return {
        "id": case["id"],
        "weighted_symmetry_cells_checked": len(detailed_balance),
        "nonnegative_cells_checked": len(entrywise_nonnegative),
        "self_adjoint": all(detailed_balance),
        "positivity_preserving": all(entrywise_nonnegative),
        "graphop": all(detailed_balance) and all(entrywise_nonnegative),
    }


def _check_control(control: dict[str, Any]) -> dict[str, Any]:
    result = _check_case(control)
    expected_failure = control["expected_failure"]
    detected = not result[
        "self_adjoint" if expected_failure == "self_adjoint" else "positivity_preserving"
    ]
    return {
        "id": control["id"],
        "expected_failure": expected_failure,
        "detected": detected,
    }


def check(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    cases = [_check_case(case) for case in raw["cases"]]
    controls = [_check_control(control) for control in raw["negative_controls"]]
    assert all(case["graphop"] for case in cases)
    assert all(control["detected"] for control in controls)
    return {
        "claim": 1,
        "checker": "weighted-matrix criterion (independent module)",
        "status": "VERIFIED",
        "cases": cases,
        "negative_controls": controls,
    }

