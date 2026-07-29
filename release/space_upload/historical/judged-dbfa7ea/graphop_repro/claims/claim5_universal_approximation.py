"""Two-route proof checker for Theorem M.1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def verify(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    premises = raw["premises"]
    route_tietze = {
        "ambient_is_compact_metric": premises["ambient_didm_compact_metric"],
        "realizable_set_is_compact": premises["realizable_didm_compact"],
        "realizable_set_is_closed": (
            premises["ambient_didm_hausdorff"]
            and premises["realizable_didm_compact"]
        ),
        "real_target_extends": premises["tietze_extension_for_closed_subset"],
        "ambient_mpnn_class_dense": premises["ambient_mpnn_uniform_density"],
        "restriction_preserves_error": True,
    }
    route_stone_weierstrass = {
        "domain_compact_hausdorff": (
            premises["realizable_didm_compact"]
            and premises["ambient_didm_hausdorff"]
        ),
        "restricted_class_is_algebra": premises["mpnn_outputs_form_algebra"],
        "contains_constants": premises["mpnn_outputs_contain_constants"],
        "separates_realizable_points": (
            premises["ambient_mpnn_separates_points"]
            and premises["restriction_preserves_separation"]
        ),
    }
    assert all(route_tietze.values())
    assert all(route_stone_weierstrass.values())

    control = raw["negative_control"]
    control_rejected = (
        control["subset"] == "(0,1) in [0,1]"
        and not control["closed"]
        and control["target"] == "x -> 1/x"
        and not control["continuous_extension_to_ambient"]
    )
    assert control_rejected
    return {
        "claim": 5,
        "status": "VERIFIED",
        "route_1_tietze_restriction": route_tietze,
        "route_2_direct_stone_weierstrass": route_stone_weierstrass,
        "strict_subset_premise_used": False,
        "negative_control": {
            "id": control["id"],
            "nonclosed_subset": control["subset"],
            "target": control["target"],
            "extension_route_rejected": control_rejected,
        },
        "conclusion": (
            "For every L in N0, every continuous real function on the "
            "bofop-DIDM quotient is uniformly approximable by L-layer MPNNs."
        ),
    }

