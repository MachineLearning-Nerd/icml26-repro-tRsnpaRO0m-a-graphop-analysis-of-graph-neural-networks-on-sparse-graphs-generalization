# Claim 5 method

Three materially different routes are checked.

## 1. General density certificate

For arbitrary `L`, let `K=Gamma_L(BF_d^r)`. At depth zero, coordinate
projections separate features. Inductively, unequal descriptors differ either
in their previous descriptor or neighbor measure. Riesz separation supplies a
continuous test for the measure case; the induction algebra approximates that
test while preserving a nonzero integral gap, and one message/update layer
realizes it. The same argument after node-distribution pooling separates
distinct DIDMs.

Parallel channel concatenation gives constants and sums, while a continuous
multiplication readout gives products. Thus the uniform closure is a unital
point-separating algebra. Real Stone-Weierstrass makes it all of `C(K)`, which
unpacks to the paper's `for every g, epsilon` conclusion. The certificate uses
compactness as a stated hypothesis but assumes neither Theorem E.12 nor M.1.
Two independent kernels check reachability and the trust boundary.

## 2. Constructive continuum

For every cycle size `n>=3` and `x in [0,1]`, give each cycle edge weight
`x/2`. This is a sparse bofop with bound `r=1`, and the one-layer MPNN
`h1=A1` recovers `x` at every node. A piecewise-linear readout therefore
uniformly approximates any continuous scalar target by uniform continuity.
Three nonlinear targets are checked on 8,193 points with knot counts from 4
to 128. A discontinuous step target is rejected with exact uniform-error lower
bound `1/2`.

## 3. Actual sparse-graph MPNNs

The deterministic dataset contains path, cycle, degree-four circulant,
chorded-cycle, and star graphs with 16 to 512 vertices. All weights are scaled
so the maximum fiber mass is at most one. The exact architecture is

`h0=1`, `h1=A h0`, and
`h2=(h1, h1^2, h1*(A h1))`,

followed by mean pooling and a trained additive Chebyshev-polynomial readout.
There are 1,000 training, 400 validation, and 800 held-out test graphs. Degree
1 through 10 and sample counts 125, 375, and 1,000 are swept. Degree five is
the first validation hit. The independent checker imports no primary code and
constructs a different piecewise-linear readout.

Controls remove both message-passing layers and deterministically shift
training labels. Both must miss the declared `0.04` maximum-error threshold.
