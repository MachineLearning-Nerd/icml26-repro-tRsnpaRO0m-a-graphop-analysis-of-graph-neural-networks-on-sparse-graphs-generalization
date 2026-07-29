# Claim 2 method

For the sparse path `P4`, vertex `i` has fiber
`nu_i = sum_{j adjacent to i} delta_j`.  Hence `(Af)(i)` and
`integral f dnu_i` are two independently evaluated finite sums.  The verifier
checks their equality for all `5^4=625` signals in `{-2,-1,0,1,2}^4`.

The exact finite weighted induced norms are recomputed:

- `||A||infinity->infinity` is the maximum absolute row sum.
- `||A||1->1` is the maximum weighted absolute column sum divided by its input
  atom weight.
- `ess sup_i nu_i(Omega)` is the maximum row fiber mass.

All equal `2`.  An independent module repeats these calculations without
importing the primary verifier.

The control is `Af(n)=n f(n)` on `N` with `mu({n})=2^-n`.  It has graphop norm
`sum n/2^n=2`, but fiber mass `n`; every violating atom has positive measure.
Prefix horizons `4,8,16,32,64` calibrate both trends against the exact partial
sum `2-(M+2)/2^M`.

