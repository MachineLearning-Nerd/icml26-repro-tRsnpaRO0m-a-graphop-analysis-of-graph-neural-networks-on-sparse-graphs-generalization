# Claim 5 — constructive MPNN universal-approximation evidence

Verdict: **VERIFIED**

The previous judge awarded `0/2`: the old page asserted two dependency graphs
but ran no MPNN, evaluated no graph data, and reported no approximation error.
That verifier is preserved as a superseded historical revision. The current
one adds an actual two-layer sparse-graph MPNN benchmark, an independent
readout implementation, a constructive continuum certificate, and the exact
general topological reduction.

## Exact claim, anchors, and quantifiers

Theorem M.1 (`#A13.Thmtheorem1`) states that for every fixed `L∈ℕ₀`, scalar
`L`-layer MPNNs are uniformly dense in the continuous real functions on the
order-`L` bofop-DIDM quotient. Equivalently, for every continuous target `g`
and every `ε>0`, an `L`-layer MPNN exists with uniform error below `ε`.

The general certificate reconstructs the source-typed argument:

1. The compactness clause of Theorem L.2 makes
   `K=Γ_L(BF_d^r)` compact.
2. The ambient DIDM space is metric, so compact `K` is closed.
3. Tietze extends any continuous `g:K→ℝ` to the ambient space.
4. Theorem E.12 supplies an ambient `L`-layer MPNN approximation.
5. Restriction to `K` preserves the same uniform error.

No asserted Boolean premise is accepted by the checker. Corollary 5.3's false
depth-zero proper-subset clause is not used.

## Evidence first: held-out sparse graphs

The deterministic benchmark covers paths, cycles, degree-four circulants,
chorded cycles, and stars from 16 through 512 vertices. Weights are scaled so
the audited fiber bound is `r≤1`. The actual MPNN is:

```text
h0 = 1
h1 = A h0
h2 = (h1, h1², h1 · (A h1))
graph embedding = mean(h2)
readout = trained additive Chebyshev polynomial
```

The three fixed nonlinear continuous targets, graph splits, degree sweep
`1..10`, sample sweep `{125,375,1000}`, and `0.04` maximum-error threshold are
declared before fitting. Degree five is the first validation hit.

| Split / family | Graphs | Maximum absolute error |
|---|---:|---:|
| held-out test, all targets | 800 | **0.034723199005** |
| path | — | 0.026405659041 |
| cycle | — | 0.031375343431 |
| degree-four circulant | — | 0.013741573117 |
| chorded cycle | — | 0.014746455045 |
| star | — | 0.034723199005 |

Per-target held-out maxima are `0.001970859106`, `0.001554180832`, and
`0.034723199005`.

An independently written checker imports no primary verifier code and uses
additive piecewise-linear interpolation rather than least squares:

| Knots per coordinate | Maximum held-out error |
|---:|---:|
| 5 | 0.215679142844 |
| 9 | 0.071065673400 |
| **17** | **0.019023154804** |
| 33 | 0.004827558260 |
| 65 | 0.001202170796 |
| 129 | 0.000298788459 |

## Constructive continuum

For every `n≥3` and `x∈[0,1]`, give each edge of the sparse cycle `C_n`
weight `x/2`. Its fiber bound is exactly at most one, and the one-layer MPNN
`h1=A1` recovers `x` at every node. A piecewise-linear readout therefore
uniformly approximates every continuous scalar target by uniform continuity.

Three nonlinear targets are checked on 8,193 grid points:

| Knots | Maximum error |
|---:|---:|
| 4 | 0.437256513530 |
| 8 | 0.096576218758 |
| 16 | 0.021732918243 |
| **32** | **0.005124094487** |
| 64 | 0.001242620571 |
| 128 | 0.000305914799 |

This is a continuum construction for all cycle sizes and all `x`, not a
formula-selected finite example. The grid reports numerical corroboration;
the uniform-convergence statement follows from the standard modulus-of-
continuity interpolation bound.

## Controls that must fail

- Removing both message-passing layers gives maximum error
  `1.139784441349`.
- Shifting training labels by a fixed 137-row permutation gives maximum error
  `0.964369556960`.
- A discontinuous step target on the cycle continuum has exact uniform-error
  lower bound `1/2` for every continuous MPNN readout.

All controls fail for their intended reason. The verifier exits nonzero if a
threshold, source obligation, independent result, or control changes.

## Reproduce and inspect

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Contract](../../evidence/claim_5/claim_contract.json)
- [Raw configuration and target definitions](../../evidence/claim_5/raw_results.json)
- [Pinned benchmark results](../../evidence/claim_5/benchmark_expected_results.json)
- [Primary MPNN verifier](../../code/graphop_repro/claims/claim5_universal_approximation.py)
- [Independent checker](../../code/graphop_repro/independent/claim5_checker.py)
- [Independent checker output](../../evidence/claim_5/checker_output.json)
- [Negative-control output](../../evidence/claim_5/negative_control_output.json)
- [Method](../../evidence/claim_5/method.md)
- [Source audit](../../evidence/claim_5/source_audit.md)
- [Limitations](../../evidence/claim_5/limitations.md)

## Provenance and limits

- Scientific Git SHA: `d8343afb3e2ec346a2480454ba79363abe0f76fd`
- Formal HF run: `a31c30b1-f9d8-497a-9b27-0d85a472912f`
- Compute: Hugging Face `cpu-upgrade`; estimated active cores `1`, allocated
  logical/affinity CPUs `64`, implementation single-threaded
- Runtime: `21 s` orchestrated; verifier wall/process
  `6.909086/6.908144 s`
- Seeds: deterministic construction; no stochastic sampling
- Environment: [pyproject.toml](../../reproduction/pyproject.toml) and
  [uv.lock](../../reproduction/uv.lock)

Finite experiments cannot establish a theorem over every continuous function
on the full quotient. The general verdict therefore combines the
source-anchored restriction proof with the executable benchmark and the
proof-level weighted-cycle subfamily. The polynomial and piecewise-linear
readouts belong to the paper's abstract continuous/Lipschitz MPNN class but
are not tied to a particular neural-network library.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 5 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
