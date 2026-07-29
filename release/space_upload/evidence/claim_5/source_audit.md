# Claim 5 source audit

- Paper source SHA-256:
  `ae8d8f620023d94024494817d799bbd52617d2dd0eca282e29a8cab00e2dc3ca`
- Theorem M.1, anchor `A13.Thmtheorem1`, quantifies every `L in N0`.
- Theorem L.2, anchor `A12.Thmtheorem2`, supplies compactness of the realizable
  DIDM image. Its separate strictness clause is not needed.
- Theorem E.12, anchor `A5.Thmtheorem12`, states ambient scalar MPNN uniform
  density on `P(H^L)`.

The paper's displayed proof has type slips (it alternates between functions on
`H^L`, `P(H^L)`, and the bofop quotient). The reconstructed routes use the
correct domain `Gamma_L(BF_d^r)` throughout.

The former checker validated a Tietze restriction route but still accepted
Theorem E.12. The current general certificate supersedes that route. It
reconstructs DIDM point separation by induction from the recursive
definitions, proves the MPNN uniform closure is a unital algebra, and applies
real Stone-Weierstrass. Theorem E.12 and M.1 are forbidden as foundation
sources by the independent checker.

The experimental route fixes `L=2`, `d=1`, and `r=1`. Every generated finite
graph is an undirected weighted sparse graph with maximum fiber mass at most
one. The targets are explicit continuous functions of three graph-level
statistics produced by the two-layer message-passing computation, hence are
continuous on the corresponding order-two DIDM quotient.
