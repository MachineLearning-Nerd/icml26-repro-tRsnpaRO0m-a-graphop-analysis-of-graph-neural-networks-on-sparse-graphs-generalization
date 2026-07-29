# Claim 1 method

The original exact examples remain as regressions. The strengthened verifier
also proves the finite-atomic criteria by coefficient comparison and basis
witnesses, then applies them with exact `fractions.Fraction` arithmetic to six
families:

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
