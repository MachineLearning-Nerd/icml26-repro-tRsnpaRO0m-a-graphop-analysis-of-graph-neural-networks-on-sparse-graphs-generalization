# Current graphop verification

This candidate supersedes exact judged revision
`dbfa7ea0de058ad35fa8bab58684306bd9ac7e7c`, which scored **8/12**:
Claims 1 and 2 were `TOY` (`1/2` each), Claim 5 was `INCONCLUSIVE` (`0/2`),
and Claims 3, 4, and 6 received full falsification credit. The exact judged
tree is preserved under **Historical judged 8/12 revision — superseded**.

## Evidence first

| Claim | Exact statement tested | New inline evidence | Verdict |
|---|---|---|---|
| [1](../claims/claim-1.md) | Definition 3.1: graphops are self-adjoint and positivity-preserving `L∞→L1` operators, covering dense kernels and sparse adjacency | necessary-and-sufficient theorem for every finite atomic matrix; 34 instances through 16,384 vertices; 448,593,904 cells certified | **VERIFIED** |
| [2](../claims/claim-2.md) | Theorem 3.3: bofop fibers uniquely represent `A` and their finite essential mass supremum equals both operator norms | all-real-signal coefficient proof; 34 instances; exact graphop/non-bofop countable control | **VERIFIED** |
| [3](../claims/claim-3.md) | Theorem 4.1: one output constant depending only on `L,D,r` works for every formal `MP_D` model | unchanged full-credit counterexample: fixed `d_M≤8`, admissible gap `M`; choose `M=8C+1` | **FALSIFIED** |
| [4](../claims/claim-4.md) | Corollary 5.3: for every `L∈N₀`, the realizable image is compact and a proper subset | unchanged full-credit counterexample: at `L=0`, `Γ₀(BF_d^r)=P(H⁰)` | **FALSIFIED** |
| [5](../claims/claim-5.md) | Theorem M.1: for every fixed `L`, MPNNs are uniformly dense on the realizable quotient | actual L=2 MPNN: 800 held-out graphs, max error `0.034723199005`; independent error `0.019023154804`; continuum error `0.000305914799` | **VERIFIED** |
| [6](../claims/claim-6.md) | Theorem M.5: simultaneous uniform generalization over the displayed class | unchanged full-credit counterexample: imbalance gives infinite supremum gap with bad probability tending to one | **FALSIFIED** |

No finite experiment is promoted to proof of a universal theorem. Claims 1
and 2 include general finite-atomic derivations; Claim 5 combines a
source-anchored general reduction with two constructive numerical routes.
Claims 3, 4, and 6 remain assumption-audited symbolic counterexamples.

## Reproduce

Exact fixed command on every node:

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Pinned Python inputs](../../pyproject.toml)
- [Exact uv lockfile](../../uv.lock)
- [Current cumulative runner](../../graphop_repro/run_all.py)
- [Pinned paper source audit](../../evidence/source/paper_source_audit.md)
- [Exact live 8/12 verdict record](../../evidence/source/live_verdict_record.json)
- [Illustrated report](../../reports/reproduction/report.md)
- [Self-contained marimo tutorial](../../notebooks/graphop_claims.py)
- [Release report and forecast](release-report.md)
- [Evaluator-blind review](blind-review.md)
- [Command ledger](command-ledger.md)

The environment is Python `>=3.12,<3.13`, resolved by `uv.lock`, with no
third-party runtime dependencies. Strengthened Claims 1–2 ran on Hugging Face
`cpu-upgrade` in `26 s` orchestrated (`6.441582 s` verifier wall); the
cumulative Claim 5 suite ran there in `21 s` (`6.909086 s` verifier wall).
Both jobs allocated 64 logical/affinity CPUs, but the implementation is
single-threaded and the pre-run active-core estimate was one.

## Evaluator visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](../claims/claim-1.md) | [yes](../../code/graphop_repro/claims/claim1_graphops.py) | yes | [JSON](../../evidence/claim_1/raw_results.json) | [output](../../evidence/claim_1/checker_output.json) | [output](../../evidence/claim_1/negative_control_output.json) | yes | VERIFIED |
| 2 | [Claim 2](../claims/claim-2.md) | [yes](../../code/graphop_repro/claims/claim2_bofops.py) | yes | [JSON](../../evidence/claim_2/raw_results.json) | [output](../../evidence/claim_2/checker_output.json) | [output](../../evidence/claim_2/negative_control_output.json) | yes | VERIFIED |
| 3 | [Claim 3](../claims/claim-3.md) | [yes](../../code/graphop_repro/claims/claim3_uniform_lipschitz.py) | yes | [JSON](../../evidence/claim_3/raw_results.json) | [output](../../evidence/claim_3/checker_output.json) | [output](../../evidence/claim_3/negative_control_output.json) | yes | FALSIFIED |
| 4 | [Claim 4](../claims/claim-4.md) | [yes](../../code/graphop_repro/claims/claim4_didm_counterexample.py) | yes | [JSON](../../evidence/claim_4/raw_results.json) | [output](../../evidence/claim_4/checker_output.json) | [output](../../evidence/claim_4/negative_control_output.json) | yes | FALSIFIED |
| 5 | [Claim 5](../claims/claim-5.md) | [yes](../../code/graphop_repro/claims/claim5_universal_approximation.py) | yes | [benchmark](../../evidence/claim_5/benchmark_expected_results.json) | [output](../../evidence/claim_5/checker_output.json) | [output](../../evidence/claim_5/negative_control_output.json) | yes | VERIFIED |
| 6 | [Claim 6](../claims/claim-6.md) | [yes](../../code/graphop_repro/claims/claim6_generalization.py) | yes | [JSON](../../evidence/claim_6/raw_results.json) | [output](../../evidence/claim_6/checker_output.json) | [output](../../evidence/claim_6/negative_control_output.json) | yes | FALSIFIED |

Every cell is reachable from this page. Each claim page gives the exact
statement, assumptions, inline numbers, raw link, executable verifier,
independent checker, failing control, limitations, Git SHA, deterministic
seed policy, CPU allocation, and runtime. The cumulative verifier exits
nonzero when any evidence obligation fails.
