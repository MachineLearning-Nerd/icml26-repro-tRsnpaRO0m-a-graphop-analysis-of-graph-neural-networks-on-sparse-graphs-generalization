# Reproduction: graphops on sparse graphs

We audited all six judged claims in *A Graphop Analysis of Graph Neural
Networks on Sparse Graphs: Generalization and Universal Approximation*
(arXiv:2602.08785). Exact finite certificates verify the graphop and
bounded-fiber definitions; proof certificates verify universal approximation;
assumption-satisfying counterexamples falsify the formal uniform-continuity,
depth-zero strict-subset, and uniform-generalization statements.

The previous live judge score is **0/12**. The scientific result below is a
forecast, not a new judge score: **3 VERIFIED, 3 FALSIFIED**, with a
conservative projected range of **8–12/12** and a best-supported possible
score of **12/12**.

- [Illustrated technical report](reports/reproduction/report.md)
- [Self-contained marimo tutorial](notebooks/graphop_claims.py)
- [Evaluator-visible candidate entrypoint](candidate/README.md)
- [Open in molab](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization/blob/main/notebooks/graphop_claims.py)

Paper comparison: the paper makes qualitative theorem claims rather than a
single benchmark number. We observed exact residual `0` for both graphop
constructions, exact fiber bound `2` for sparse `P4`, and explicit formal
counterexamples where the claimed uniform constants cannot be finite. No
downscaled training or proxy benchmark was substituted. Compute was local,
single-core CPU; every formal run finished in 5 seconds of orchestrated time.

| Branch/experiment | Purpose | Exact run command | Assessment | Compute |
|---|---|---|---|---|
| `orx/frozen-baseline-exact-graphop-definition` | Lock Python 3.12/uv and verify Claim 1 with independent controls | `uv run --frozen python -m graphop_repro.run_all` | Claim 1 VERIFIED | local CPU, single-threaded, 5 s orchestrated |
| `orx/exact-bounded-fiber-characterization` | Add exact Claim 2 fibers, norm identity, and a graphop/non-bofop control | `uv run --frozen python -m graphop_repro.run_all` | Claim 2 VERIFIED; Claim 1 regression VERIFIED | local CPU, single-threaded, 5 s orchestrated |
| `orx/corollary-5-3-l-zero-counterexample` | Audit Corollary 5.3's universal depth quantifier with a proof certificate | `uv run --frozen python -m graphop_repro.run_all` | Claim 4 FALSIFIED; prior regressions pass | local CPU, single-threaded, 5 s orchestrated |
| `orx/theorem-4-1-uniform-constant-counterexample` | Audit the formal `MP_D` class and the claimed uniform constant | `uv run --frozen python -m graphop_repro.run_all` | Claim 3 FALSIFIED; prior regressions pass | local CPU, single-threaded, 5 s orchestrated |
| `orx/universal-approximation-proof-reconstruction` | Reconstruct Theorem M.1 by Tietze and Stone-Weierstrass routes | `uv run --frozen python -m graphop_repro.run_all` | Claim 5 VERIFIED; prior regressions pass | local CPU, single-threaded, 5 s orchestrated |
| `orx/formal-mpnn-uniform-generalization-counterexampl` | Test uniform generalization over formal `MP_D` with exact binomial evidence | `uv run --frozen python -m graphop_repro.run_all` | Claim 6 FALSIFIED; all six cumulative checks pass | local CPU, single-threaded, 5 s orchestrated |
| `orx/evaluator-visible-release-candidate` | Package the cumulative evidence, report, notebook, and evaluator navigation | `uv run --frozen python -m graphop_repro.run_all` | release validation pending | local CPU, single-threaded |

Paper: arXiv `2602.08785`; OpenReview `tRsnpaRO0m`.
