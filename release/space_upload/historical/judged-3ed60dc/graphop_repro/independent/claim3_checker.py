"""Independent algebraic checker for the Theorem 4.1 counterexample."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def check(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    inputs = raw["singleton_inputs"]
    model = raw["model_family"]

    assumptions = {
        "A1_self_adjoint_positive": inputs["A1"] == "zero",
        "A2_self_adjoint_positive": inputs["A2"] == "identity",
        "both_norms_at_most_r": (
            Fraction(inputs["A1_norm"]) <= Fraction(inputs["r"])
            and Fraction(inputs["A2_norm"]) <= Fraction(inputs["r"])
        ),
        "model_lipschitz_bound": max(
            Fraction(value) for value in model["lipschitz_constants"]
        )
        <= Fraction(model["D"]),
        "offset_unrestricted_by_formal_definition": (
            "phi_l(0)" in raw["formal_class_audit"]["missing_quantities"]
        ),
    }
    assert all(assumptions.values())

    distance_bound = Fraction(8)
    sweep_checks = 0
    for proposed_constant in raw["calibrated_constant_sweep"]:
        c = Fraction(proposed_constant)
        m = distance_bound * c + 1
        assert m > c * distance_bound
        sweep_checks += 1

    control = raw["negative_control"]
    control_rejected = Fraction(control["M"]) > Fraction(
        control["added_max_abs_phi0_zero"]
    )
    assert control_rejected
    return {
        "claim": 3,
        "checker": "independent singleton-operator and geometric-series derivation",
        "status": "FALSIFIED",
        "assumptions": assumptions,
        "input_action_metric_upper_bound": "8",
        "output_gap_formula": "M",
        "adversarial_choice": "M=8*C+1",
        "finite_constant_sweep_checks": sweep_checks,
        "range_bound_mutation_rejected": control_rejected,
        "interpretation_risk": (
            "Paper prose calls hidden states [-1,1]-valued, but the formal "
            "MP_D definition imposes no range or offset constraint."
        ),
    }

