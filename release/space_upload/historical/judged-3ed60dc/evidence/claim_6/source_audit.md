# Claim 6 source audit

- Paper source SHA-256:
  `ae8d8f620023d94024494817d799bbd52617d2dd0eca282e29a8cab00e2dc3ca`
- Section 6.2, anchor `S6.SS2`, says the generalization error for models in
  `MP_D` converges to zero.
- Theorem M.5, anchor `A13.Thmtheorem5`, gives a uniform bound over a fixed
  Hölder class.
- Its proof treats arbitrary data `nu` as if every class had probability
  `1/C`; in fact `E[N_i]=N*nu(B_i)`.

More importantly, the passage from `MP_D` to one fixed Hölder class uses
Theorem 4.1's false uniform constant. The counterexample directly tests the
Section 6.2 `MP_D` claim rather than merely pointing to the proof error.

