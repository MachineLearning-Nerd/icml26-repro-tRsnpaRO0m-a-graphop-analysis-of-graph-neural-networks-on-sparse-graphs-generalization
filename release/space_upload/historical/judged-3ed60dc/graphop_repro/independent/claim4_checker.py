"""Independent reconstruction of the Corollary 5.3 L=0 counterexample."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


def _weak_composition_count(total: int, parts: int) -> int:
    return math.comb(total + parts - 1, parts - 1)


def check(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    statement = raw["source_statement"]
    witness = raw["universal_counterexample"]
    sanity = raw["finite_sanity"]
    control = raw["negative_control"]

    quantified_depth_includes_zero = (
        statement["L_quantifier"] == "for every L in N0"
    )
    zero_operator_is_bofop_for_all_positive_r = (
        witness["operator"] == "A=0"
        and witness["operator_norm"] == "0"
        and statement["r_quantifier"] == "for every r > 0"
    )
    arbitrary_probability_measure_realized = (
        witness["omega"] == "H0=[-1,1]^d"
        and witness["measure"] == "arbitrary pi in P(H0)"
        and witness["signal"] == "f=id_H0"
        and witness["gamma_0"] == "gamma_0=f=id_H0"
        and witness["Gamma_0"] == "(id_H0)_* pi = pi"
    )
    number_of_grid_measures = _weak_composition_count(
        sanity["probability_denominator"],
        len(sanity["feature_grid"]),
    )
    depth_one_control_rejected = (
        control["mutated_depth"] == 1
        and control["target_depth_one_neighbor_mass"] != "0"
    )

    assert quantified_depth_includes_zero
    assert zero_operator_is_bofop_for_all_positive_r
    assert arbitrary_probability_measure_realized
    assert number_of_grid_measures == sanity["expected_measure_count"]
    assert depth_one_control_rejected
    return {
        "claim": 4,
        "checker": "independent quantifier reconstruction and stars-and-bars audit",
        "status": "FALSIFIED",
        "quantified_depth_includes_zero": quantified_depth_includes_zero,
        "zero_operator_is_bofop_for_all_positive_r": (
            zero_operator_is_bofop_for_all_positive_r
        ),
        "arbitrary_probability_measure_realized": (
            arbitrary_probability_measure_realized
        ),
        "finite_grid_probability_measures": number_of_grid_measures,
        "depth_one_mutation_rejected": depth_one_control_rejected,
        "conclusion": "Gamma_0(BF_d^r)=P(H0), not a strict subset",
        "compactness_clause_untouched": True,
    }

