# Claim 6 — uniform generalization fails for formal `MP_D`

Verdict: **FALSIFIED**

Put equal population mass on the valid singleton bofop-signals `x0=(A=0,f=0)`
and `x1=(A=I,f=0)`, use one class label `1`, and absolute loss. The admissible
`MP_1` family from Claim 3 outputs `0` and `M`, so its losses are `1` and
`|M-1|`.

If `N1` of `N` samples are `x1`, then for `M>=2`

```text
|R_emp-R_stat| = |N1/N-1/2| (M-2).
```

Whenever the sample is not exactly balanced, the supremum over `M` is
infinite. This occurs with probability one for odd `N`; for even `N` its exact
probability is

```text
1 - binomial(N,N/2)/2^N  -> 1.
```

Thus the uniform gap for the formally defined `MP_D` class does not vanish.
This does not challenge the standard result for a truly fixed Hölder class
with a common envelope. Adding `0<=M<=1` is the negative control and removes
the unbounded gap.

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Contract](../../../.openresearch/artifacts/claim_6/claim_contract.json)
- [Source audit](../../../.openresearch/artifacts/claim_6/source_audit.md)
- [Raw data](../../../.openresearch/artifacts/claim_6/raw_results.json)
- [Primary verifier](../../../graphop_repro/claims/claim6_generalization.py)
- [Independent checker](../../../graphop_repro/independent/claim6_checker.py)
- [Checker output](../../../.openresearch/artifacts/claim_6/checker_output.json)
- [Control output](../../../.openresearch/artifacts/claim_6/negative_control_output.json)
- [Method](../../../.openresearch/artifacts/claim_6/method.md)
- [Limitations](../../../.openresearch/artifacts/claim_6/limitations.md)

