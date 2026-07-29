# Claim 1 method

The current verifier first checks a serialized Horn derivation whose
quantifiers range over an arbitrary probability space and every bounded test
pair. The derivation uses integral monotonicity for positivity and
Fubini plus kernel symmetry for self-adjointness, then applies Definition 3.1.
An independently implemented premise-graph checker rejects any certificate
that assumes a paper theorem. Deleting positivity, Fubini, symmetry, or the
definition makes the proof fail.

The uncountable sparse control is the Lebesgue circle with irrational
translation `T`. Its fibers are `(delta_Tx+delta_T^-1x)/2`: mass one, two-point
support, and singular with respect to the nonatomic base measure.
Haar-invariance proves self-adjointness. Deleting the inverse translation
produces a directed shift and a nonzero Fourier adjoint residual.

The original exact examples remain as regressions. The finite verifier proves
the atomic criteria by coefficient comparison and basis witnesses, then
applies them with exact `fractions.Fraction` arithmetic to six families:

- symmetric dense step graphons through 256 cells;
- paths through 16,384 vertices;
- weighted cycles and degree-four circulants through 8,192 vertices;
- weighted stars through 4,096 vertices; and
- nonuniform reversible weighted chains through 1,024 vertices.

Sparse zero entries are certified by their implicit representation, while
every nonzero edge is visited. The independent module does not import the
primary family implementation: it recomputes sparse norms from degree
sequences and reversible edge flows and audits 162 small matrices against
basis-witness definitions.

The original asymmetric-positive and symmetric-negative controls remain. Each
must fail for its named graphop axiom.
