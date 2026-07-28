# Claim 2 — bounded fibers on an actual sparse graph

Verdict: **VERIFIED**

The exact source is Theorem 3.3.  For the sparse path `P4`, the fiber measures
are

```text
nu_1=delta_2,  nu_2=delta_1+delta_3,
nu_3=delta_2+delta_4,  nu_4=delta_3.
```

Thus the fiber masses are `(1,2,2,1)` and

```text
||A||infinity->infinity = ||A||1->1
                         = ess sup_i nu_i(Omega) = 2.
```

The equality `(Af)(i)=integral f dnu_i` was checked exactly on all 625 signals
in `{-2,-1,0,1,2}^4`; matrix equality supplies the all-real-signal proof.

## Control that must fail

On `N` with `mu(n)=2^-n`, the positive self-adjoint diagonal graphop
`Af(n)=n f(n)` has exact `L-infinity -> L1` norm
`sum n/2^n=2`.  Its fibers are `nu_n=n delta_n`, so their essential supremum is
infinite.  It is correctly accepted as a graphop and rejected as a bofop.

## Reproduce and inspect

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Contract](../../../.openresearch/artifacts/claim_2/claim_contract.json)
- [Raw data](../../../.openresearch/artifacts/claim_2/raw_results.json)
- [Primary verifier](../../../graphop_repro/claims/claim2_bofops.py)
- [Independent checker](../../../graphop_repro/independent/claim2_checker.py)
- [Checker output](../../../.openresearch/artifacts/claim_2/checker_output.json)
- [Control output](../../../.openresearch/artifacts/claim_2/negative_control_output.json)
- [Method](../../../.openresearch/artifacts/claim_2/method.md)
- [Limitations](../../../.openresearch/artifacts/claim_2/limitations.md)

The cumulative verifier exits nonzero on any identity, norm, checker, or control
failure.

## Provenance

- Scientific Git SHA: `3ab9369d0a464b55d36db546f005819a0b54acf0`
- Formal run: `1445490d-0fb2-4913-9174-43cf88467c06`
- Compute: one local CPU core; `cpu-upgrade` flavor not applicable
- Runtime: 5 s orchestrated; verifier wall/process `0.233641/0.229816` s
- Seeds: none; enumeration and rational arithmetic are deterministic
- Environment: [pyproject.toml](../../../pyproject.toml) and
  [uv.lock](../../../uv.lock)

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 2 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
