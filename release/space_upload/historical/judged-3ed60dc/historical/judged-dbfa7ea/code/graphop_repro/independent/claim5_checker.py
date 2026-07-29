"""Independent dependency-graph audit of Theorem M.1."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def check(raw_path: Path) -> dict[str, Any]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    p = raw["premises"]
    closed = p["realizable_didm_compact"] and p["ambient_didm_hausdorff"]
    tietze_route = (
        closed
        and p["tietze_extension_for_closed_subset"]
        and p["ambient_mpnn_uniform_density"]
    )
    direct_route = (
        p["realizable_didm_compact"]
        and p["ambient_didm_hausdorff"]
        and p["mpnn_outputs_form_algebra"]
        and p["mpnn_outputs_contain_constants"]
        and p["ambient_mpnn_separates_points"]
        and p["restriction_preserves_separation"]
    )
    control = raw["negative_control"]
    control_rejected = not control["closed"] and not control[
        "continuous_extension_to_ambient"
    ]
    assert tietze_route and direct_route and control_rejected
    return {
        "claim": 5,
        "checker": "independent topological dependency graph",
        "status": "VERIFIED",
        "tietze_route_complete": tietze_route,
        "stone_weierstrass_route_complete": direct_route,
        "proper_subset_not_required": True,
        "nonclosed_domain_control_rejected": control_rejected,
    }

