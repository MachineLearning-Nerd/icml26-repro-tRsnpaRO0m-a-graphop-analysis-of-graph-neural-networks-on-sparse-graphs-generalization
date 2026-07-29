# Reproduction: graphops on sparse graphs

This project reproduces all six judged claims in *A Graphop Analysis of Graph
Neural Networks on Sparse Graphs: Generalization and Universal Approximation*
(arXiv:2602.08785).

The current live judge score is **9/12** at exact Hugging Face revision
`3ed60dc4ac62b111cb7ca0ef7c752586a10aa8b5`. The judge gave Claims 1, 2, and
5 toy credit and retained the full-credit falsifications of Claims 3, 4, and
6.

This revision directly addresses the missing evidence:

- quantified arbitrary-space graphop and standard-Borel fiber certificates,
  plus a singular two-neighbour graphing on the uncountable Lebesgue circle;
- an independent DIDM-separation and Stone-Weierstrass certificate for every
  continuous target, without assuming the paper's E.12 or M.1;
- the existing all-finite graphop/bofop certificate, exercised on 34 dense and
  sparse instances through 16,384 vertices;
- an actual two-layer MPNN evaluated on 800 held-out sparse graphs, with
  maximum error `0.034723199005` against a declared `0.04` threshold;
- a separately implemented readout reaching `0.019023154804`, plus a
  constructive weighted-cycle continuum and two failing experimental
  controls.

The scientific assessment is **3 VERIFIED and 3 FALSIFIED**. The conservative
post-change forecast is **9–12/12**, with **12/12** the best-supported
possibility—not a live score.

- [Illustrated technical report](reports/reproduction/report.md)
- [Self-contained marimo tutorial](notebooks/graphop_claims.py)
- [Evaluator-visible Space candidate](release/space_upload/README.md)
- [Claim 1 certificate](release/space_upload/pages/claims/claim-1.md)
- [Claim 2 certificate](release/space_upload/pages/claims/claim-2.md)
- [Claim 5 MPNN evidence](release/space_upload/pages/claims/claim-5.md)
- [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization/blob/main/notebooks/graphop_claims.py)

The fixed command on every experiment is:

```text
uv run --frozen python -m graphop_repro.run_all
```

Formal strengthened runs used Hugging Face `cpu-upgrade`, with an estimated
one active verifier core. The implementation is single-threaded even though
the jobs exposed 64 logical CPUs.

## Experiment log

| Branch/experiment | Purpose or change | Exact run command | Assessment/outcome | Compute |
|---|---|---|---|---|
| `main` | Public README, report, notebook, and release surface | Not run as an experiment (publication surface) | Mirrors the winning cumulative evidence | no experiment |
| [`orx/formal-mpnn-uniform-generalization-counterexampl`](https://github.com/MachineLearning-Nerd/icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization/tree/orx/formal-mpnn-uniform-generalization-counterexampl) | Prior 8/12 scientific winner; Claims 3, 4, and 6 counterexamples | `uv run --frozen python -m graphop_repro.run_all` | Claims 3, 4, 6 FALSIFIED; prior finite checks pass | local CPU, single-threaded, 5 s orchestrated |
| [`orx/general-finite-graphop-and-bofop-certificates`](https://github.com/MachineLearning-Nerd/icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization/tree/orx/general-finite-graphop-and-bofop-certificates) | Replace four-node-only Claims 1–2 evidence with a parameterized theorem and family sweeps | `uv run --frozen python -m graphop_repro.run_all` | Claims 1–2 VERIFIED across 34 instances; all cumulative checks pass | HF `cpu-upgrade`, one active core, 26 s orchestrated |
| [`orx/constructive-mpnn-universal-approximation-eviden`](https://github.com/MachineLearning-Nerd/icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization/tree/orx/constructive-mpnn-universal-approximation-eviden) | Add actual sparse-graph MPNN, independent readout, continuum, and controls for Claim 5 | `uv run --frozen python -m graphop_repro.run_all` | Claim 5 VERIFIED; held-out max `0.034723199005`; all cumulative checks pass | HF `cpu-upgrade`, one active core, 21 s orchestrated |
| [`orx/evaluator-visible-strengthened-evidence-candidat`](https://github.com/MachineLearning-Nerd/icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization/tree/orx/evaluator-visible-strengthened-evidence-candidat) | Preserve the exact judged tree and expose the strengthened evidence | `uv run --frozen python -m graphop_repro.run_all` | published revision `3ed60dc4...`; live judge improved to 9/12 | HF `cpu-upgrade`, one active core, 27 s orchestrated |
| [`orx/general-probability-space-proof-certificates`](https://github.com/MachineLearning-Nerd/icml26-repro-tRsnpaRO0m-a-graphop-analysis-of-graph-neural-networks-on-sparse-graphs-generalization/tree/orx/general-probability-space-proof-certificates) | Address the remaining finite/toy scope with quantified symbolic proofs and an uncountable sparse graphing | `uv run --frozen python -m graphop_repro.run_all` | all claims accepted; general targets independently derived | HF `cpu-upgrade`, one active core, about 22 s orchestrated |
| `orx/evaluator-visible-general-proof-release` | Package the exact 9/12 tree, proof certificates, manifests, and blind review | `uv run --frozen python -m graphop_repro.run_all` | release validation in progress | HF `cpu-upgrade` formal run pending |

Paper: arXiv `2602.08785`; OpenReview `tRsnpaRO0m`.
