"""Exact binomial counterexample to uniform generalization over formal MP_D."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def verify(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    assumptions = {
        "iid_two_point_distribution": raw["distribution"] == {
            "x0_probability": "1/2",
            "x1_probability": "1/2",
        },
        "inputs_are_bofops": raw["inputs"] == {
            "x0": "singleton A=0,f=0",
            "x1": "singleton A=I,f=0",
            "r": "1",
        },
        "models_in_formal_MP1": raw["model_family"]["lipschitz_constants"]
        == ["0", "1", "1"],
        "absolute_loss_is_one_lipschitz": raw["loss"] == "|prediction-1|",
    }
    assert all(assumptions.values())

    rows = []
    for n in raw["sample_sizes"]:
        if n % 2:
            balanced_probability = Fraction(0)
        else:
            balanced_probability = Fraction(math.comb(n, n // 2), 2**n)
        rows.append(
            {
                "N": n,
                "exact_balance_probability": str(balanced_probability),
                "infinite_uniform_gap_probability": str(1 - balanced_probability),
                "odd_N_gap_infinite_surely": n % 2 == 1,
            }
        )
    assert all(
        Fraction(row["infinite_uniform_gap_probability"]) > 0 for row in rows
    )

    control = raw["negative_control"]
    bounded = Fraction(control["maximum_M"])
    control_range = bounded - Fraction(2)
    control_finite = control_range <= 0
    assert control_finite
    return {
        "claim": 6,
        "status": "FALSIFIED",
        "assumptions": assumptions,
        "loss_values": {"x0": "1", "x1": "|M-1|"},
        "gap_formula_for_M_at_least_2": "|N1/N-1/2|*(M-2)",
        "supremum_over_M": (
            "infinity whenever N1/N differs from 1/2"
        ),
        "sample_size_sweep": rows,
        "asymptotic_bad_event": (
            "Odd N: probability 1. Even N: 1-binomial(N,N/2)/2^N -> 1."
        ),
        "negative_control": {
            "id": control["id"],
            "added_assumption": "0<=M<=1",
            "uniform_gap_no_longer_unbounded": control_finite,
        },
    }

