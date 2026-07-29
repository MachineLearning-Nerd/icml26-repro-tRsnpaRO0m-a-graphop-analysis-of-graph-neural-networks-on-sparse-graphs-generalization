"""Counterexample verifier for Theorem 4.1's uniform MPNN constant."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def _verify_inputs(raw: dict[str, Any]) -> dict[str, bool]:
    inputs = raw["singleton_inputs"]
    return {
        "borel_probability_spaces": inputs["space"] == "singleton with mass 1",
        "first_operator_is_bofop": (
            inputs["A1"] == "zero" and inputs["A1_norm"] == "0"
        ),
        "second_operator_is_bofop": (
            inputs["A2"] == "identity" and inputs["A2_norm"] == "1"
        ),
        "operator_bound_r_one": inputs["r"] == "1",
        "signals_admissible": inputs["f1"] == "0" and inputs["f2"] == "0",
    }


def _verify_model_family(raw: dict[str, Any]) -> dict[str, bool]:
    model = raw["model_family"]
    return {
        "depth_one": model["L"] == 1,
        "dimensions_scalar": model["dimensions"] == [1, 1, 1, 1],
        "initialization_is_constant_M": model["phi_0"] == "x -> M",
        "update_selects_aggregate": model["phi_1"] == "(u,v) -> v",
        "readout_is_identity": model["psi"] == "z -> z",
        "all_lipschitz_constants_at_most_D": (
            model["lipschitz_constants"] == ["0", "1", "1"]
            and model["D"] == "1"
        ),
        "formal_class_has_no_offset_bound": (
            raw["formal_class_audit"]["bounded_quantities"]
            == ["Lipschitz constants of phi_l and psi"]
            and raw["formal_class_audit"]["missing_quantities"]
            == ["phi_l(0)", "psi(0)", "output ranges"]
        ),
    }


def _profile_distance_bound(raw: dict[str, Any]) -> dict[str, Any]:
    bound = raw["action_metric_bound"]
    assert bound["profile_support_diameter_bound"] == "2*(k+1)"
    geometric = Fraction(2)  # sum_{k>=0} 2^-k
    arithmetico_geometric = Fraction(2)  # sum_{k>=0} k*2^-k
    total = 2 * (geometric + arithmetico_geometric)
    assert total == 8
    return {
        "sum_two_to_minus_k": str(geometric),
        "sum_k_two_to_minus_k": str(arithmetico_geometric),
        "input_action_metric_upper_bound": str(total),
        "independent_of_M": True,
    }


def _calibrated_witnesses(raw: dict[str, Any], distance_bound: Fraction):
    rows = []
    for proposed_constant in raw["calibrated_constant_sweep"]:
        c = Fraction(proposed_constant)
        m = distance_bound * c + 1
        output_gap = m
        rhs_upper_bound = c * distance_bound
        rows.append(
            {
                "proposed_C": str(c),
                "chosen_M": str(m),
                "output_gap": str(output_gap),
                "upper_bound_on_C_times_action_distance": str(rhs_upper_bound),
                "violates_inequality": output_gap > rhs_upper_bound,
            }
        )
    assert all(row["violates_inequality"] for row in rows)
    return rows


def _negative_control(raw: dict[str, Any]) -> dict[str, Any]:
    control = raw["negative_control"]
    proposed_m = Fraction(control["M"])
    maximum = Fraction(control["added_max_abs_phi0_zero"])
    rejected = proposed_m > maximum
    assert rejected
    return {
        "id": control["id"],
        "added_assumption": "|phi_0(0)|<=1",
        "proposed_M": str(proposed_m),
        "allowed_maximum": str(maximum),
        "counterexample_rejected": rejected,
        "reason": "The missing offset/range bound blocks the unbounded family.",
    }


def verify(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    input_obligations = _verify_inputs(raw)
    model_obligations = _verify_model_family(raw)
    metric_bound = _profile_distance_bound(raw)
    witnesses = _calibrated_witnesses(
        raw,
        Fraction(metric_bound["input_action_metric_upper_bound"]),
    )
    control = _negative_control(raw)
    assert all(input_obligations.values())
    assert all(model_obligations.values())
    assert control["counterexample_rejected"]
    return {
        "claim": 3,
        "status": "FALSIFIED",
        "scope": (
            "The output inequality with C' depending only on L,D,r is false "
            "for the formally defined MP_D class."
        ),
        "input_obligations": input_obligations,
        "model_obligations": model_obligations,
        "action_metric_bound": metric_bound,
        "calibrated_witnesses": witnesses,
        "universal_diagonal_argument": (
            "For any finite proposed C, choose M=8*C+1. Then output gap "
            "M > 8*C >= C*d_M because d_M<=8."
        ),
        "negative_control": control,
    }

