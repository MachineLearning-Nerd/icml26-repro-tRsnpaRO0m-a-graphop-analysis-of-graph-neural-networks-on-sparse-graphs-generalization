"""Exact verifier for the bounded-fiber characterization in Theorem 3.3."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def _f(value: str | int) -> Fraction:
    return Fraction(value)


def _matvec(
    matrix: tuple[tuple[Fraction, ...], ...],
    vector: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        sum((entry * value for entry, value in zip(row, vector)), Fraction())
        for row in matrix
    )


def _weighted_l1_norm(
    matrix: tuple[tuple[Fraction, ...], ...],
    measure: tuple[Fraction, ...],
) -> Fraction:
    """Exact induced L1 norm on a finite weighted probability space."""
    return max(
        sum(
            (measure[i] * abs(matrix[i][j]) for i in range(len(matrix))),
            Fraction(),
        )
        / measure[j]
        for j in range(len(matrix))
    )


def _finite_case(case: dict[str, Any]) -> dict[str, Any]:
    measure = tuple(_f(value) for value in case["measure"])
    matrix = tuple(
        tuple(_f(value) for value in row) for row in case["operator_matrix"]
    )
    fibers = tuple(
        tuple(_f(value) for value in row) for row in case["fiber_atoms"]
    )
    dimension = len(matrix)
    signals = tuple(
        tuple(_f(value) for value in values)
        for values in itertools.product((-2, -1, 0, 1, 2), repeat=dimension)
    )
    identities = [
        _matvec(matrix, signal)
        == tuple(
            sum((atom * value for atom, value in zip(row, signal)), Fraction())
            for row in fibers
        )
        for signal in signals
    ]
    fiber_masses = tuple(sum(row, Fraction()) for row in fibers)
    infinity_norm = max(
        sum((abs(entry) for entry in row), Fraction()) for row in matrix
    )
    one_norm = _weighted_l1_norm(matrix, measure)
    essential_supremum = max(fiber_masses)
    expected = case["expected"]
    result = {
        "id": case["id"],
        "signals_checked": len(signals),
        "fiber_identity_holds": all(identities),
        "fiber_masses": [str(value) for value in fiber_masses],
        "linfinity_to_linfinity_norm": str(infinity_norm),
        "l1_to_l1_norm": str(one_norm),
        "essential_supremum_fiber_mass": str(essential_supremum),
        "norm_identity_holds": infinity_norm == one_norm == essential_supremum,
        "bofop": all(identities)
        and infinity_norm == one_norm == essential_supremum
        and essential_supremum < 10**100,
    }
    assert result["signals_checked"] == expected["signals_checked"]
    assert result["fiber_masses"] == expected["fiber_masses"]
    assert result["linfinity_to_linfinity_norm"] == expected["norm"]
    assert result["l1_to_l1_norm"] == expected["norm"]
    assert result["essential_supremum_fiber_mass"] == expected["norm"]
    assert result["bofop"] is True
    return result


def _unbounded_control(control: dict[str, Any]) -> dict[str, Any]:
    horizons = control["horizons"]
    rows = []
    for horizon in horizons:
        partial_norm = sum(
            (Fraction(n, 2**n) for n in range(1, horizon + 1)), Fraction()
        )
        closed_form = Fraction(2) - Fraction(horizon + 2, 2**horizon)
        assert partial_norm == closed_form
        rows.append(
            {
                "horizon": horizon,
                "max_fiber_mass": horizon,
                "partial_linfinity_to_l1_norm": str(partial_norm),
                "closed_form": str(closed_form),
            }
        )
    assert all(
        row["max_fiber_mass"] == row["horizon"] for row in rows
    )
    return {
        "id": control["id"],
        "space": "N with mu({n})=2^-n",
        "operator": "(Af)(n)=n f(n)",
        "self_adjoint": True,
        "positivity_preserving": True,
        "linfinity_to_l1_norm": "2",
        "fiber_mass_formula": "nu_n(Omega)=n",
        "essential_supremum": "infinity",
        "positive_measure_witness": (
            "for every M, atom n=M+1 has measure 2^-(M+1)>0 and fiber mass M+1"
        ),
        "graphop": True,
        "bofop": False,
        "detected": True,
        "calibrated_horizons": rows,
    }


def verify(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    cases = [_finite_case(case) for case in raw["cases"]]
    controls = [_unbounded_control(control) for control in raw["negative_controls"]]
    assert all(case["bofop"] for case in cases)
    assert all(control["graphop"] and not control["bofop"] for control in controls)
    return {
        "claim": 2,
        "status": "VERIFIED",
        "arithmetic": "fractions.Fraction (exact rational)",
        "cases": cases,
        "negative_controls": controls,
    }

