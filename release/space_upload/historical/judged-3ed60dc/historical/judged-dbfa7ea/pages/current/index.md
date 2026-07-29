# Current graphop verification

This page supersedes the **Historical rejected baseline** at judged revision
`9ded82baa88100f73731decd32ad0895120ae8ba`. That historical page is preserved
unchanged and remains in navigation, but its one-line assertions are not
current evidence.

## Evidence first

| Claim | Exact paper statement tested | Raw result inline | Verdict |
|---|---|---|---|
| [1](../claims/claim-1.md) | Definition 3.1: self-adjoint, positivity-preserving `L∞→L1` operators include dense graphons and sparse adjacency | dense norm `11/35`, sparse norm `3/2`, both maximum adjoint residual `0` | **VERIFIED** |
| [2](../claims/claim-2.md) | Theorem 3.3: bofop fibers represent `A` and have finite essential mass supremum equal to both operator norms | sparse `P4` masses `(1,2,2,1)`; all three values equal `2` | **VERIFIED** |
| [3](../claims/claim-3.md) | Theorem 4.1: one output constant depending only on `L,D,r` works for every formal `MP_D` model | fixed `d_M≤8`, admissible gap `M`; choose `M=8C+1` | **FALSIFIED** |
| [4](../claims/claim-4.md) | Corollary 5.3: for every `L∈N₀`, the realizable image is a compact proper subset | at `L=0`, `Γ₀(BF_d^r)=P(H⁰)` | **FALSIFIED** |
| [5](../claims/claim-5.md) | Theorem M.1: scalar `L`-layer MPNNs are uniformly dense on the realizable quotient | Tietze-extension and direct Stone–Weierstrass routes both close | **VERIFIED** |
| [6](../claims/claim-6.md) | Theorem M.5: simultaneous uniform generalization over the stated formal class | imbalance gives infinite supremum gap; even-`N` bad probability reaches `0.9296139078` at `N=128` and tends to `1` | **FALSIFIED** |

No toy or proxy result is promoted to a theorem verdict. Claims 1 and 2 are
complete finite construction certificates; Claims 3, 4, and 6 are symbolic,
assumption-satisfying counterexamples; Claim 5 is a two-route proof
reconstruction.

## Reproduce

Exact fixed command on every experiment:

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Pinned Python inputs](../../pyproject.toml)
- [Exact uv lockfile](../../uv.lock)
- [Cumulative runner at the command-visible path](../../graphop_repro/run_all.py)
- [Pinned paper source audit](../../evidence/source/paper_source_audit.md)
- [Illustrated report](../../reports/reproduction/report.md)
- [Self-contained marimo tutorial](../../notebooks/graphop_claims.py)
- [Release report and forecast](release-report.md)
- [Evaluator-blind review](blind-review.md)
- [Command ledger](command-ledger.md)

The environment is Python `>=3.12,<3.13` with no third-party runtime
dependencies. Each formal run used one local CPU core, so `cpu-upgrade` was not
applicable. The cumulative scientific run completed in 5 s orchestrated time
and `0.232468` s verifier wall time. Seeds are absent because every check uses
deterministic exact arithmetic or symbolic obligations.

## Evaluator visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](../claims/claim-1.md) | [yes](../../code/graphop_repro/claims/claim1_graphops.py) | yes | [JSON](../../evidence/claim_1/raw_results.json) | [output](../../evidence/claim_1/checker_output.json) | [output](../../evidence/claim_1/negative_control_output.json) | yes | VERIFIED |
| 2 | [Claim 2](../claims/claim-2.md) | [yes](../../code/graphop_repro/claims/claim2_bofops.py) | yes | [JSON](../../evidence/claim_2/raw_results.json) | [output](../../evidence/claim_2/checker_output.json) | [output](../../evidence/claim_2/negative_control_output.json) | yes | VERIFIED |
| 3 | [Claim 3](../claims/claim-3.md) | [yes](../../code/graphop_repro/claims/claim3_uniform_lipschitz.py) | yes | [JSON](../../evidence/claim_3/raw_results.json) | [output](../../evidence/claim_3/checker_output.json) | [output](../../evidence/claim_3/negative_control_output.json) | yes | FALSIFIED |
| 4 | [Claim 4](../claims/claim-4.md) | [yes](../../code/graphop_repro/claims/claim4_didm_counterexample.py) | yes | [JSON](../../evidence/claim_4/raw_results.json) | [output](../../evidence/claim_4/checker_output.json) | [output](../../evidence/claim_4/negative_control_output.json) | yes | FALSIFIED |
| 5 | [Claim 5](../claims/claim-5.md) | [yes](../../code/graphop_repro/claims/claim5_universal_approximation.py) | yes | [JSON](../../evidence/claim_5/raw_results.json) | [output](../../evidence/claim_5/checker_output.json) | [output](../../evidence/claim_5/negative_control_output.json) | yes | VERIFIED |
| 6 | [Claim 6](../claims/claim-6.md) | [yes](../../code/graphop_repro/claims/claim6_generalization.py) | yes | [JSON](../../evidence/claim_6/raw_results.json) | [output](../../evidence/claim_6/checker_output.json) | [output](../../evidence/claim_6/negative_control_output.json) | yes | FALSIFIED |

Every cell is reachable from this canonical page. Every claim page includes
the exact source scope, assumptions, inline numbers, command, environment,
scientific Git SHA, run ID, CPU allocation, runtime, limitations, checker, and
control. The verifier exits nonzero on any failed evidence obligation.
