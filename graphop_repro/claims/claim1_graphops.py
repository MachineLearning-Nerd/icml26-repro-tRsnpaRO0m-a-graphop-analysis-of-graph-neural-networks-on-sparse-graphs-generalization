"""Exact-arithmetic verifier for the graphop axioms in Definition 3.1."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def _fraction(value: str) -> Fraction:
    return Fraction(value)


def _vector(values: tuple[int, ...]) -> tuple[Fraction, ...]:
    return tuple(Fraction(value) for value in values)


def _matvec(
    matrix: tuple[tuple[Fraction, ...], ...],
    vector: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        sum((entry * value for entry, value in zip(row, vector)), Fraction())
        for row in matrix
    )


def _bilinear(
    matrix: tuple[tuple[Fraction, ...], ...],
    measure: tuple[Fraction, ...],
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> Fraction:
    image = _matvec(matrix, left)
    return sum(
        (weight * value * test for weight, value, test in zip(measure, image, right)),
        Fraction(),
    )


def _linfty_to_l1_norm(
    matrix: tuple[tuple[Fraction, ...], ...],
    measure: tuple[Fraction, ...],
) -> Fraction:
    """Exact norm: a convex piecewise-linear objective peaks at a cube vertex."""
    dimension = len(matrix)
    candidates: list[Fraction] = []
    for signs in itertools.product((-1, 1), repeat=dimension):
        image = _matvec(matrix, _vector(signs))
        candidates.append(
            sum(
                (weight * abs(value) for weight, value in zip(measure, image)),
                Fraction(),
            )
        )
    return max(candidates)


def _verify_case(case: dict[str, Any]) -> dict[str, Any]:
    measure = tuple(_fraction(value) for value in case["measure"])
    matrix = tuple(
        tuple(_fraction(value) for value in row)
        for row in case["operator_matrix"]
    )
    dimension = len(matrix)
    signed_signals = tuple(
        _vector(values) for values in itertools.product((-1, 0, 1), repeat=dimension)
    )
    nonnegative_signals = tuple(
        _vector(values) for values in itertools.product((0, 1), repeat=dimension)
    )

    adjoint_residuals = [
        _bilinear(matrix, measure, left, right)
        - _bilinear(matrix, measure, right, left)
        for left in signed_signals
        for right in signed_signals
    ]
    minimum_positive_output = min(
        value
        for signal in nonnegative_signals
        for value in _matvec(matrix, signal)
    )
    norm = _linfty_to_l1_norm(matrix, measure)
    fiber_masses = tuple(sum(row, Fraction()) for row in matrix)
    max_fiber_mass = max(fiber_masses)

    result = {
        "id": case["id"],
        "self_adjoint": all(residual == 0 for residual in adjoint_residuals),
        "positivity_preserving": minimum_positive_output >= 0,
        "graphop": (
            all(residual == 0 for residual in adjoint_residuals)
            and minimum_positive_output >= 0
        ),
        "adjoint_signal_pairs_checked": len(adjoint_residuals),
        "nonnegative_signals_checked": len(nonnegative_signals),
        "max_abs_adjoint_residual": str(
            max((abs(value) for value in adjoint_residuals), default=Fraction())
        ),
        "minimum_output_on_nonnegative_grid": str(minimum_positive_output),
        "linfty_to_l1_norm": str(norm),
        "fiber_masses": [str(value) for value in fiber_masses],
        "max_fiber_mass": str(max_fiber_mass),
    }
    expected = case["expected"]
    assert result["graphop"] is expected["graphop"]
    assert result["linfty_to_l1_norm"] == expected["linfty_to_l1_norm"]
    assert result["max_fiber_mass"] == expected["max_fiber_mass"]
    assert (
        result["adjoint_signal_pairs_checked"]
        == expected["adjoint_signal_pairs_checked"]
    )
    assert (
        result["nonnegative_signals_checked"]
        == expected["nonnegative_signals_checked"]
    )
    return result


def _verify_control(control: dict[str, Any]) -> dict[str, Any]:
    measure = tuple(_fraction(value) for value in control["measure"])
    matrix = tuple(
        tuple(_fraction(value) for value in row)
        for row in control["operator_matrix"]
    )
    left = tuple(_fraction(value) for value in control["witness"]["left"])
    right = tuple(_fraction(value) for value in control["witness"]["right"])
    adjoint_residual = _bilinear(matrix, measure, left, right) - _bilinear(
        matrix, measure, right, left
    )
    image = _matvec(matrix, left)
    minimum_output = min(image)
    detected = (
        adjoint_residual != 0
        if control["expected_failure"] == "self_adjoint"
        else minimum_output < 0
    )
    assert detected, f"negative control unexpectedly passed: {control['id']}"
    return {
        "id": control["id"],
        "expected_failure": control["expected_failure"],
        "detected": detected,
        "adjoint_residual": str(adjoint_residual),
        "witness_output": [str(value) for value in image],
    }


def verify(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    cases = [_verify_case(case) for case in raw["cases"]]
    controls = [_verify_control(control) for control in raw["negative_controls"]]
    assert all(case["graphop"] for case in cases)
    assert all(control["detected"] for control in controls)
    return {
        "claim": 1,
        "status": "VERIFIED",
        "arithmetic": "fractions.Fraction (exact rational)",
        "cases": cases,
        "negative_controls": controls,
    }
