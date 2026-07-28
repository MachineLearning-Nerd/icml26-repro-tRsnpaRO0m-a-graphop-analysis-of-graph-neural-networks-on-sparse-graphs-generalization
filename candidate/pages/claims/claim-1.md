# Claim 1 — exact graphop axioms

Verdict: **VERIFIED**

The exact paper statement is Definition 3.1: a bounded
`L-infinity -> L1` P-operator is a graphop when it is self-adjoint and
positivity preserving.  The quantifiers range over every bounded measurable
test pair and every nonnegative bounded signal, respectively.

## Evidence first

| Construction | Complete adjoint pairs | Nonnegative signals | Max residual | Exact norm | Result |
|---|---:|---:|---:|---:|---|
| Dense 3-cell step graphon | 729 | 8 | 0 | 11/35 | graphop |
| Sparse path `P4`, sum aggregation | 6,561 | 16 | 0 | 3/2 | graphop |

The sparse example has fiber masses `(1,2,2,1)` and essential supremum `2`.
This directly replaces the historical, unsupported `bound<=1` assertion.

## Reproduce

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Exact claim contract](../../../.openresearch/artifacts/claim_1/claim_contract.json)
- [Raw matrices and expected exact results](../../../.openresearch/artifacts/claim_1/raw_results.json)
- [Primary verifier](../../../graphop_repro/claims/claim1_graphops.py)
- [Independent checker](../../../graphop_repro/independent/claim1_checker.py)
- [Independent checker output](../../../.openresearch/artifacts/claim_1/checker_output.json)
- [Negative-control output](../../../.openresearch/artifacts/claim_1/negative_control_output.json)
- [Method](../../../.openresearch/artifacts/claim_1/method.md)
- [Limitations](../../../.openresearch/artifacts/claim_1/limitations.md)
- [Pinned source audit](../../../.openresearch/artifacts/source/paper_source_audit.md)

The verifier exits nonzero if either construction misses an axiom, if an exact
number changes, if the independent output disagrees, or if a negative control
passes.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |

