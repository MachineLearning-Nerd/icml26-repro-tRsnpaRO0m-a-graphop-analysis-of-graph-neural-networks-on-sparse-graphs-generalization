# Claim 3 source audit

- Source: ar5iv HTML for arXiv `2602.08785v1`
- Retrieved: `2026-07-28T17:44:40Z` with explicit browser User-Agent
- SHA-256: `ae8d8f620023d94024494817d799bbd52617d2dd0eca282e29a8cab00e2dc3ca`
- Section 2.2, anchor `S2.SS2.p2.15`: `MP_D` consists of update/readout
  functions whose **Lipschitz constants** are bounded by `D`; the displayed
  domains and codomains are Euclidean spaces.
- Theorem 4.1, anchor `S4.Thmtheorem1`: `C'_(D,r)` depends on `L,D,r`.
- Theorem J.1, anchor `A10.Thmtheorem1`: the appendix version likewise says
  the constants depend on layer count, function Lipschitz constants, operator
  exponents, and `r`.

Section 4.1 describes hidden representations as `[-1,1]`-valued, but neither
the MPNN function signatures nor `MP_D` impose an output-range or offset bound.
This ambiguity is a material interpretation risk and is reported, not hidden.

