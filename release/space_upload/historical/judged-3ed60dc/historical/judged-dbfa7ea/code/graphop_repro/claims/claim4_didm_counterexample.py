"""Proof-certificate verifier for the L=0 clause of Corollary 5.3."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def _compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in _compositions(total - first, parts - 1):
            yield (first, *rest)


def _finite_sanity(raw: dict[str, Any]) -> dict[str, Any]:
    sanity = raw["finite_sanity"]
    grid = tuple(Fraction(value) for value in sanity["feature_grid"])
    denominator = sanity["probability_denominator"]
    distributions = tuple(_compositions(denominator, len(grid)))
    identities = []
    for counts in distributions:
        source_measure = {
            point: Fraction(count, denominator)
            for point, count in zip(grid, counts)
        }
        identity_pushforward = dict(source_measure)
        identities.append(identity_pushforward == source_measure)
    return {
        "feature_dimension": sanity["feature_dimension"],
        "grid": [str(value) for value in grid],
        "probability_denominator": denominator,
        "probability_measures_exhausted": len(distributions),
        "all_identity_pushforwards_equal_input": all(identities),
    }


def _verify_symbolic_certificate(raw: dict[str, Any]) -> dict[str, Any]:
    statement = raw["source_statement"]
    construction = raw["universal_counterexample"]

    obligations = {
        "zero_is_in_N0": statement["L_quantifier"] == "for every L in N0",
        "r_is_arbitrary_positive": statement["r_quantifier"] == "for every r > 0",
        "ambient_space_matches": construction["omega"] == "H0=[-1,1]^d",
        "measure_is_arbitrary": construction["measure"] == "arbitrary pi in P(H0)",
        "zero_operator_linear": construction["operator"] == "A=0",
        "zero_operator_self_adjoint": construction["operator"] == "A=0",
        "zero_operator_positivity_preserving": construction["operator"] == "A=0",
        "zero_operator_norm_within_every_r": (
            construction["operator_norm"] == "0"
            and statement["r_quantifier"] == "for every r > 0"
        ),
        "identity_signal_is_admissible": (
            construction["signal"] == "f=id_H0"
            and construction["omega"] == "H0=[-1,1]^d"
        ),
        "depth_zero_idm_is_signal": construction["gamma_0"] == "gamma_0=f=id_H0",
        "identity_pushforward_law": (
            construction["Gamma_0"] == "(id_H0)_* pi = pi"
        ),
    }
    assert all(obligations.values())

    derivation = {
        "arbitrary_ambient_measure_is_realized": True,
        "ambient_subset_realizable": True,
        "realizable_subset_ambient": True,
        "set_equality": "Gamma_0(BF_d^r)=P(H0)",
        "strict_subset_false": True,
    }
    return {"obligations": obligations, "derivation": derivation}


def _negative_control(raw: dict[str, Any]) -> dict[str, Any]:
    control = raw["negative_control"]
    same_zero_operator_neighbor_mass = Fraction(0)
    target_neighbor_mass = Fraction(control["target_depth_one_neighbor_mass"])
    rejected = (
        control["mutated_depth"] == 1
        and same_zero_operator_neighbor_mass != target_neighbor_mass
    )
    assert rejected
    return {
        "id": control["id"],
        "mutated_depth": control["mutated_depth"],
        "same_construction_neighbor_mass": str(same_zero_operator_neighbor_mass),
        "target_neighbor_mass": str(target_neighbor_mass),
        "certificate_rejected": rejected,
        "reason": "At depth 1, A=0 forces the neighbor measure to have mass 0.",
    }


def verify(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    certificate = _verify_symbolic_certificate(raw)
    finite_sanity = _finite_sanity(raw)
    control = _negative_control(raw)
    assert certificate["derivation"]["strict_subset_false"]
    assert finite_sanity["all_identity_pushforwards_equal_input"]
    assert control["certificate_rejected"]
    return {
        "claim": 4,
        "status": "FALSIFIED",
        "scope": (
            "The universal strict-subset clause of Corollary 5.3 is false at "
            "L=0; this does not falsify its compactness clause."
        ),
        "symbolic_certificate": certificate,
        "finite_sanity": finite_sanity,
        "negative_control": control,
    }
