# Claim 6 method

Use the two valid singleton bofop-signals from Claim 3 with equal population
mass, one class label `1`, and absolute loss. The formal `MP_1` family has
outputs `0` and `M`, hence losses `1` and `|M-1|`.

If `N1` of `N` samples equal the identity-operator input, then for `M>=2`

```text
|R_emp-R_stat| = |N1/N-1/2| (M-2).
```

Unless the sample is exactly balanced, the supremum over admissible `M` is
infinite. Exact binomial probabilities show this happens surely for odd `N`
and with probability `1-binomial(N,N/2)/2^N -> 1` for even `N`.

