# A Graphop Analysis of GNNs — reproduction workspace

Current experimental baseline: an exact-arithmetic verification of the graphop
axioms in Definition 3.1 on both a dense step graphon and a sparse path
adjacency operator.  See the [candidate entrypoint](candidate/README.md).

| Branch/experiment | Purpose | Exact run command | Assessment | Compute |
|---|---|---|---|---|
| `orx/frozen-baseline-exact-graphop-definition` | Lock Python 3.12/uv and verify Claim 1 with independent controls | `uv run --frozen python -m graphop_repro.run_all` | Claim 1 VERIFIED | local CPU, single-threaded, 5 s orchestrated |
| `orx/exact-bounded-fiber-characterization` | Add exact Claim 2 fibers, norm identity, and a graphop/non-bofop control | `uv run --frozen python -m graphop_repro.run_all` | pending | local CPU, single-threaded |

Paper: arXiv `2602.08785`; OpenReview `tRsnpaRO0m`.
