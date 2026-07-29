# Current graphop verification

The current live judge scored exact revision
`3ed60dc4ac62b111cb7ca0ef7c752586a10aa8b5` at **9/12**: Claims 1, 2, and
5 were `TOY` (`1/2` each), while Claims 3, 4, and 6 retained full
falsification credit. This candidate directly addresses the judge's remaining
scope criticism with independently checked quantified certificates. The exact
older 8/12 tree is still preserved under **Historical judged 8/12 revision —
superseded**.

## Evidence first

| Claim | Exact statement tested | New inline evidence | Verdict |
|---|---|---|---|
| [1](../claims/claim-1.md) | Definition 3.1: graphops are self-adjoint and positivity-preserving `L∞→L1` operators, covering dense kernels and sparse adjacency | arbitrary-space Fubini certificate; uncountable singular circle graphing; all-finite theorem and 34-family regression | **VERIFIED** |
| [2](../claims/claim-2.md) | Theorem 3.3: bofop fibers uniquely represent `A` and their finite essential mass supremum equals both operator norms | arbitrary standard-Borel extension/disintegration certificate; uncountable sparse fibers; finite and countable regressions | **VERIFIED** |
| [3](../claims/claim-3.md) | Theorem 4.1: one output constant depending only on `L,D,r` works for every formal `MP_D` model | unchanged full-credit counterexample: fixed `d_M≤8`, admissible gap `M`; choose `M=8C+1` | **FALSIFIED** |
| [4](../claims/claim-4.md) | Corollary 5.3: for every `L∈N₀`, the realizable image is compact and a proper subset | unchanged full-credit counterexample: at `L=0`, `Γ₀(BF_d^r)=P(H⁰)` | **FALSIFIED** |
| [5](../claims/claim-5.md) | Theorem M.1: for every fixed `L`, MPNNs are uniformly dense on the realizable quotient | independent DIDM-separation induction plus Stone-Weierstrass; actual L=2 MPNN on 800 held-out graphs; continuum route | **VERIFIED** |
| [6](../claims/claim-6.md) | Theorem M.5: simultaneous uniform generalization over the displayed class | unchanged full-credit counterexample: imbalance gives infinite supremum gap with bad probability tending to one | **FALSIFIED** |

No finite experiment is promoted to proof of a universal theorem. Claims 1,
2, and 5 now include machine-checked symbolic derivations with explicit
standard-mathematics trust boundaries and deletion controls. Their numerical
and finite routes remain corroborating regressions. Claims 3, 4, and 6 remain
assumption-audited symbolic counterexamples.

## Reproduce

Exact fixed command on every node:

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Pinned Python inputs](../../pyproject.toml)
- [Exact uv lockfile](../../uv.lock)
- [Current cumulative runner](../../graphop_repro/run_all.py)
- [Pinned paper source audit](../../evidence/source/paper_source_audit.md)
- [Exact live 9/12 verdict record](../../evidence/source/live_verdict_9of12.json)
- [Illustrated report](../../reports/reproduction/report.md)
- [Self-contained marimo tutorial](../../notebooks/graphop_claims.py)
- [Release report and forecast](release-report.md)
- [Evaluator-blind review](blind-review.md)
- [Command ledger](command-ledger.md)

The environment is Python `>=3.12,<3.13`, resolved by `uv.lock`, with no
third-party runtime dependencies. The current quantified cumulative suite ran
on Hugging Face `cpu-upgrade` in about `22 s` orchestrated
(`7.058492/7.057538 s` verifier wall/process). The job allocated 64
logical/affinity CPUs, but the implementation is single-threaded and the
pre-run active-core estimate was one.

## Evaluator visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](../claims/claim-1.md) | [yes](../../code/graphop_repro/general_proof_kernel.py) | yes | [certificate](../../evidence/claim_1/general_proof_certificate.json) | [output](../../evidence/claim_1/general_checker_output.json) | deletion + directed shift | yes | VERIFIED |
| 2 | [Claim 2](../claims/claim-2.md) | [yes](../../code/graphop_repro/general_proof_kernel.py) | yes | [certificate](../../evidence/claim_2/general_proof_certificate.json) | [output](../../evidence/claim_2/general_checker_output.json) | deletion + unbounded fibers | yes | VERIFIED |
| 3 | [Claim 3](../claims/claim-3.md) | [yes](../../code/graphop_repro/claims/claim3_uniform_lipschitz.py) | yes | [JSON](../../evidence/claim_3/raw_results.json) | [output](../../evidence/claim_3/checker_output.json) | [output](../../evidence/claim_3/negative_control_output.json) | yes | FALSIFIED |
| 4 | [Claim 4](../claims/claim-4.md) | [yes](../../code/graphop_repro/claims/claim4_didm_counterexample.py) | yes | [JSON](../../evidence/claim_4/raw_results.json) | [output](../../evidence/claim_4/checker_output.json) | [output](../../evidence/claim_4/negative_control_output.json) | yes | FALSIFIED |
| 5 | [Claim 5](../claims/claim-5.md) | [yes](../../code/graphop_repro/general_proof_kernel.py) | yes | [certificate](../../evidence/claim_5/general_proof_certificate.json) | [output](../../evidence/claim_5/general_checker_output.json) | deletion + experimental controls | yes | VERIFIED |
| 6 | [Claim 6](../claims/claim-6.md) | [yes](../../code/graphop_repro/claims/claim6_generalization.py) | yes | [JSON](../../evidence/claim_6/raw_results.json) | [output](../../evidence/claim_6/checker_output.json) | [output](../../evidence/claim_6/negative_control_output.json) | yes | FALSIFIED |

Every cell is reachable from this page. Each claim page gives the exact
statement, assumptions, inline numbers, raw link, executable verifier,
independent checker, failing control, limitations, Git SHA, deterministic
seed policy, CPU allocation, and runtime. The cumulative verifier exits
nonzero when any evidence obligation fails.
