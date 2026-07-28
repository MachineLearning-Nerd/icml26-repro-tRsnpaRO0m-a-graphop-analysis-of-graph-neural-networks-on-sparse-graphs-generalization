# Claim 1 method

All arithmetic is exact `fractions.Fraction`; there are no tolerances.

- Dense case: a three-cell step graphon whose symmetric kernel has no zero
  cells.  The induced operator includes the probability weight `1/3`.
- Sparse case: the four-vertex path `P4` with sum aggregation.  This deliberately
  has maximum fiber mass `2`, correcting the historical page's unsupported
  `bound<=1` wording while satisfying the required finite bound.
- Primary verifier: evaluates every pair of signals in `{-1,0,1}^n`, every
  nonnegative signal in `{0,1}^n`, and every sign-vector cube vertex needed for
  the exact `L-infinity -> L1` norm.
- Independent checker: checks weighted matrix symmetry and entrywise
  nonnegativity directly.  It imports no primary-verifier code.
- Controls: one asymmetric positive matrix and one symmetric matrix with a
  negative edge.  Each must fail for its named axiom.

