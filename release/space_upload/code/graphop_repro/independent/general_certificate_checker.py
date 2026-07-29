"""Independent checker for the general proof certificates.

This implementation intentionally imports neither the primary proof kernel nor
the primary certificate wrapper.  It rebuilds reachability from the serialized
premise graph and separately audits the allowed trust boundary.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]

ALLOWED_SOURCE_PREFIXES = (
    "Definition in arXiv:2602.08785v1",
    "Standard:",
    "Bogachev, Measure Theory",
    "Kallenberg, Foundations of Modern Probability",
    "Rudin, Functional Analysis",
)


def _load(claim: int) -> dict[str, Any]:
    return json.loads(
        (
            ROOT
            / ".openresearch"
            / "artifacts"
            / f"claim_{claim}"
            / "general_proof_certificate.json"
        ).read_text(encoding="utf-8")
    )


def check_general_claim(claim: int) -> dict[str, Any]:
    certificate = _load(claim)
    assert certificate["claim"] == claim
    assert certificate["quantifiers"].startswith("For every")
    lemmas = {item["id"]: item for item in certificate["trusted_foundation"]}
    assert len(lemmas) == len(certificate["trusted_foundation"])
    assert all(
        item["source"].startswith(ALLOWED_SOURCE_PREFIXES)
        for item in lemmas.values()
    )
    assert not any(
        forbidden in item["source"]
        for item in lemmas.values()
        for forbidden in ("Theorem E.12", "Theorem M.1", "Theorem 3.3")
    )

    reachable = set(certificate["hypotheses"])
    remaining = list(certificate["steps"])
    trace = []
    while remaining:
        progress = False
        next_remaining = []
        for step in remaining:
            lemma = lemmas[step["lemma"]]
            exact = (
                step["premises"] == lemma["premises"]
                and step["conclusion"] == lemma["conclusion"]
            )
            assert exact
            if set(step["premises"]).issubset(reachable):
                reachable.add(step["conclusion"])
                trace.append(step["lemma"])
                progress = True
            else:
                next_remaining.append(step)
        assert progress, "certificate contains an unreachable or cyclic proof step"
        remaining = next_remaining
    assert certificate["target"] in reachable

    essential = set(certificate["essential_lemmas"])
    assert essential
    assert essential.issubset(lemmas)
    used = set(trace)
    assert essential.issubset(used)
    return {
        "claim": claim,
        "checker": "independent premise-graph reachability and trust-boundary audit",
        "quantifiers": certificate["quantifiers"],
        "all_steps_reachable": True,
        "target_derived": True,
        "step_count": len(trace),
        "essential_lemmas_used": sorted(essential),
        "paper_result_not_assumed": True,
        "allowed_foundation_sources_only": True,
    }

