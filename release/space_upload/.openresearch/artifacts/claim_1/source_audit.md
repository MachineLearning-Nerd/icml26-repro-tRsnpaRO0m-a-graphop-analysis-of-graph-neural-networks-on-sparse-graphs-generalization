# Claim 1 source audit

Definition 3.1 is at HTML anchor `S3.Thmtheorem1`.  It is a definition, not a
finite-sample statistical claim.  The exact machine contract therefore checks
the defining universal predicates on complete finite signal domains and records
the general algebraic construction that embeds both examples:

1. A step graphon with symmetric nonnegative kernel `W` acts by
   `(Af)_i = sum_j mu_j W_ij f_j`.  Swapping `i,j` proves the two bilinear
   forms equal; nonnegative entries preserve nonnegative signals.
2. A finite undirected graph with uniform vertex measure and sum-aggregation
   adjacency acts by `(Af)_i = sum_j A_ij f_j`.  Symmetry of the undirected
   adjacency proves self-adjointness; its `0/1` entries prove positivity.

The statement that graphons and sparse graphs are represented by the same
operator axioms is therefore tested directly, not inferred from a label.

## Strengthened universal finite-atomic certificate

For an arbitrary positive atomic probability vector `mu` and arbitrary matrix
`A`, expanding the two bilinear forms shows that the coefficient of `u_i v_j`
is respectively `mu_i A_ij` and `mu_j A_ji`. Thus detailed balance is
sufficient, while the basis pair `(e_i,e_j)` proves it is necessary.
Likewise, `A e_j` is column `j`, so positivity on every nonnegative signal is
equivalent to entrywise nonnegativity. These are exact all-signal statements
for every finite dimension, not a selected finite signal grid.

For a bounded measurable symmetric nonnegative graphon kernel, the same
identity is the Fubini/Tonelli exchange
`integral integral W(x,y) v(y) u(x) dmu(y)dmu(x)` with `x,y` swapped.
The current general certificate encodes this quantified derivation and
independently audits the premise graph. It also constructs the uncountable
singular circle graphing with two atomic neighbors per point. Its explicit
trusted boundary is standard integration theory rather than the paper's
result.
