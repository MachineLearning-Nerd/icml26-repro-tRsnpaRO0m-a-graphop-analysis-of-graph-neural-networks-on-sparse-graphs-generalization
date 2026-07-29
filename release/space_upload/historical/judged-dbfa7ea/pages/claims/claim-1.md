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

- [Exact claim contract](../../evidence/claim_1/claim_contract.json)
- [Raw matrices and expected exact results](../../evidence/claim_1/raw_results.json)
- [Primary verifier](../../code/graphop_repro/claims/claim1_graphops.py)
- [Independent checker](../../code/graphop_repro/independent/claim1_checker.py)
- [Independent checker output](../../evidence/claim_1/checker_output.json)
- [Negative-control output](../../evidence/claim_1/negative_control_output.json)
- [Method](../../evidence/claim_1/method.md)
- [Limitations](../../evidence/claim_1/limitations.md)
- [Pinned source audit](../../evidence/source/paper_source_audit.md)

The verifier exits nonzero if either construction misses an axiom, if an exact
number changes, if the independent output disagrees, or if a negative control
passes.

## Provenance

- Scientific Git SHA: `e917ce09434918d243aac50d7e8a0cca960ef12a`
- Formal run: `ee300364-c697-4086-9663-c4a33434159e`
- Compute: one local CPU core; `cpu-upgrade` flavor not applicable
- Runtime: 5 s orchestrated; verifier wall/process `0.256224/0.230265` s
- Seeds: none; enumeration and rational arithmetic are deterministic
- Environment: [pyproject.toml](../../reproduction/pyproject.toml) and
  [uv.lock](../../reproduction/uv.lock)

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
