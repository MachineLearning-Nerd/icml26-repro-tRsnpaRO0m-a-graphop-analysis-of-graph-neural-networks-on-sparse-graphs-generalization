# Paper source audit

- Source: `https://ar5iv.labs.arxiv.org/html/2602.08785`
- Retrieval: `2026-07-28T17:44:40Z`
- HTTP identity: explicit `OpenResearch-Reproduction/1.0` browser User-Agent
- Bytes: `2,016,542`
- SHA-256: `ae8d8f620023d94024494817d799bbd52617d2dd0eca282e29a8cab00e2dc3ca`
- Version shown by source: `arXiv:2602.08785v1`, 9 February 2026

## Exact anchors and quantifiers

| Claim | HTML anchor | Exact scope retained by this campaign |
|---|---|---|
| 1 | `#S3.Thmtheorem1` — Definition 3.1 | `A in B_{infinity,1}(Omega)`; self-adjoint means `(v,u)_A=(u,v)_A` for every bounded measurable `u,v`; positivity preserving means `v>=0` a.e. implies `Av>=0` a.e.; a graphop has both properties. |
| 2 | `#S3.Thmtheorem3` — Theorem 3.3 | For a bofop on a Borel probability space there is a unique measurable fiber family; `(Af)(x)=integral f d nu_x`; both operator norms equal `ess sup_x nu_x(Omega)<infinity`; the converse additionally assumes the induced operator is symmetric. |
| 3 | `#S4.Thmtheorem1` — Theorem 4.1 | Both inputs lie in `BF_d^r`; the MPNN lies in `MP_D(d,d0,...,dL,p)`; constants depend on depth, `D`, and `r`; the theorem bounds the final-signal action distance and the Euclidean readout difference. |
| 4 | `#S5.Thmtheorem3` — Corollary 5.3 | For **every** `L in N_0` and `r>0`, `Gamma_L(BF_d^r)` is claimed compact and a **proper** subset of `P(H^L)`. |
| 5 | `#A13.Thmtheorem1` — Theorem M.1 | For every fixed `L in N_0`, the scalar `L`-layer MPNN class on `BF_d^r` is uniformly dense in `C(BF_d^r,R)` under the order-`L` DIDM quotient. |
| 6 | `#A13.Thmtheorem5` — Theorem M.5 | Classification setting of M.2.1; arbitrary data probability measure; i.i.d. sample; for every confidence parameter `p>0`, a simultaneous event for all `Gamma in Hol^alpha(BF_d^r,L1)` is claimed with probability at least `1-Cp-4C^2/N` and the displayed covering-number bound. |

The imported judge summary mislabels the fiber statement as Definition 3.1.
The source places the fiber representation and essential-supremum identity in
Theorem 3.3.  The campaign uses the source anchor, not the summary label.

