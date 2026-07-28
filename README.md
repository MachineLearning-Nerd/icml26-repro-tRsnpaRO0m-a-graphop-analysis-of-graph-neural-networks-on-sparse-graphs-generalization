# A Graphop Analysis of GNNs — reproduction workspace

Current cumulative result: Claims 1 and 2 are exactly verified; Theorem 4.1's
uniform output constant and Corollary 5.3's strict-subset clause are
falsified under their formal quantifiers. See the
[candidate entrypoint](candidate/README.md).

| Branch/experiment | Purpose | Exact run command | Assessment | Compute |
|---|---|---|---|---|
| `orx/frozen-baseline-exact-graphop-definition` | Lock Python 3.12/uv and verify Claim 1 with independent controls | `uv run --frozen python -m graphop_repro.run_all` | Claim 1 VERIFIED | local CPU, single-threaded, 5 s orchestrated |
| `orx/exact-bounded-fiber-characterization` | Add exact Claim 2 fibers, norm identity, and a graphop/non-bofop control | `uv run --frozen python -m graphop_repro.run_all` | Claim 2 VERIFIED; Claim 1 regression VERIFIED | local CPU, single-threaded, 5 s orchestrated |
| `orx/corollary-5-3-l-zero-counterexample` | Audit Corollary 5.3's universal depth quantifier with a proof certificate | `uv run --frozen python -m graphop_repro.run_all` | pending | local CPU, single-threaded |
| `orx/theorem-4-1-uniform-constant-counterexample` | Audit the formal `MP_D` class and the claimed uniform constant | `uv run --frozen python -m graphop_repro.run_all` | pending | local CPU, single-threaded |
| `orx/universal-approximation-proof-reconstruction` | Reconstruct Theorem M.1 by Tietze and Stone-Weierstrass routes | `uv run --frozen python -m graphop_repro.run_all` | pending | local CPU, single-threaded |
| `orx/formal-mpnn-uniform-generalization-counterexampl` | Test uniform generalization over formal `MP_D` with exact binomial evidence | `uv run --frozen python -m graphop_repro.run_all` | pending | local CPU, single-threaded |

Paper: arXiv `2602.08785`; OpenReview `tRsnpaRO0m`.
