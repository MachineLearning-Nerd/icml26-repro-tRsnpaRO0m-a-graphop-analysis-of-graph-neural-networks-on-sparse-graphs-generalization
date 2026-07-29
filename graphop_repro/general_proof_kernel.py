"""Small auditable kernel for quantified mathematical certificates.

The kernel deliberately knows nothing about graphops or neural networks.  It
checks Horn-style derivations from an explicit trusted foundation.  Each
foundation lemma records its full quantified statement and source; each proof
step can only apply a named lemma after every premise has already been derived.
This makes the mathematical trust boundary visible and lets negative controls
prove that deleting a substantive lemma makes the target unreachable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Lemma:
    identifier: str
    premises: tuple[str, ...]
    conclusion: str
    statement: str
    source: str


def verify_horn_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    """Check a quantified Horn derivation without executing asserted booleans."""
    hypotheses = tuple(certificate["hypotheses"])
    assert len(hypotheses) == len(set(hypotheses))
    lemmas = {
        item["id"]: Lemma(
            identifier=item["id"],
            premises=tuple(item["premises"]),
            conclusion=item["conclusion"],
            statement=item["statement"],
            source=item["source"],
        )
        for item in certificate["trusted_foundation"]
    }
    assert len(lemmas) == len(certificate["trusted_foundation"])
    assert all(lemma.statement and lemma.source for lemma in lemmas.values())

    derived = set(hypotheses)
    trace: list[dict[str, Any]] = []
    for index, step in enumerate(certificate["steps"], start=1):
        lemma = lemmas[step["lemma"]]
        assert tuple(step["premises"]) == lemma.premises
        assert step["conclusion"] == lemma.conclusion
        missing = [premise for premise in lemma.premises if premise not in derived]
        assert not missing, f"step {index} ({lemma.identifier}) missing {missing}"
        derived.add(lemma.conclusion)
        trace.append(
            {
                "step": index,
                "lemma": lemma.identifier,
                "premises": list(lemma.premises),
                "conclusion": lemma.conclusion,
            }
        )

    target = certificate["target"]
    assert target in derived, f"target was not derived: {target}"
    return {
        "theorem": certificate["theorem"],
        "quantifiers": certificate["quantifiers"],
        "hypothesis_count": len(hypotheses),
        "trusted_foundation_count": len(lemmas),
        "derived_step_count": len(trace),
        "target": target,
        "target_derived": True,
        "trace": trace,
        "trusted_sources": sorted({lemma.source for lemma in lemmas.values()}),
    }


def deletion_controls(certificate: dict[str, Any]) -> list[dict[str, Any]]:
    """Remove each predeclared essential lemma and require proof rejection."""
    controls = []
    for removed in certificate["essential_lemmas"]:
        mutated = {
            **certificate,
            "trusted_foundation": [
                item
                for item in certificate["trusted_foundation"]
                if item["id"] != removed
            ],
        }
        rejected = False
        reason = ""
        try:
            verify_horn_certificate(mutated)
        except (AssertionError, KeyError) as error:
            rejected = True
            reason = type(error).__name__
        assert rejected, f"deleting essential lemma {removed} did not fail"
        controls.append(
            {
                "removed_lemma": removed,
                "certificate_rejected": rejected,
                "failure_type": reason,
            }
        )
    return controls

