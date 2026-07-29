# Claim 2 source audit

The fiber representation is Theorem 3.3 at `S3.Thmtheorem3`, not Definition
3.1.  Its quantifiers cover a bofop on a Borel probability space, a unique
measurable family of Borel measures, every signal in the representation
identity, and an essential (not pointwise) supremum.  The converse additionally
requires symmetry of the induced operator.

The finite sparse case has no null atoms, so its essential supremum is the
ordinary maximum.  The negative control uses a countable probability space in
which every atom has positive measure, so the unbounded pointwise sequence of
fiber masses also has infinite essential supremum.

For every finite atomic space, testing the representation against the atom
indicator `e_j` forces `nu_i({j})=A_ij`, which proves uniqueness. For a
nonnegative matrix, the exact induced norms are

`||A||infinity->infinity=max_i sum_j A_ij` and
`||A||1->1=max_j (sum_i mu_i A_ij)/mu_j`.

Detailed balance converts the second expression into the `j`-th row sum, so
both norms equal the essential supremum of the fiber masses. This
parameterized derivation covers every finite sparse weighted graph satisfying
the paper's symmetry assumption.
