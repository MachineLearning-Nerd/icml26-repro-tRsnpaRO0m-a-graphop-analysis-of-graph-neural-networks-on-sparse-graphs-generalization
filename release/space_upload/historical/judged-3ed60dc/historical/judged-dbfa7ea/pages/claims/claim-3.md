# Claim 3 — no uniform constant for the formal MPNN class

Verdict: **FALSIFIED**

Theorem 4.1 states that the output Lipschitz constant depends only on the layer
count `L`, the model Lipschitz bound `D`, and the bofop norm bound `r`. The
formal `MP_D` definition bounds only the Lipschitz constants of the update and
readout functions; it does not bound their values at zero or their ranges.

Take singleton probability spaces, `f1=f2=0`, `A1=0`, `A2=I`, and `L=D=r=1`.
Both inputs are valid bofop-signals. For arbitrary `M`, use

```text
phi_0(x)=M,  phi_1(u,v)=v,  psi(z)=z.
```

The three Lipschitz constants are `0,1,1`, so this is in the stated class for
every `M`. The outputs are `0` and `M`. The fixed input action distance obeys
the conservative profile-diameter bound

```text
d_M <= sum_{k>=0} 2^-k 2(k+1) = 8.
```

For any finite proposed constant `C`, choose `M=8C+1`; then
`M > 8C >= C d_M`. This contradicts the exact uniform output inequality.

## Interpretation boundary

Section 4.1 calls hidden states `[-1,1]`-valued in prose, but the formal MPNN
function signatures are Euclidean-to-Euclidean and `MP_D` imposes no range or
offset restriction. If such a bound were added, it would define a repaired
class, not the stated one. The negative control adds `|phi_0(0)|<=1` and
correctly rejects the unbounded witness.

## Reproduce and inspect

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Contract](../../evidence/claim_3/claim_contract.json)
- [Source audit](../../evidence/claim_3/source_audit.md)
- [Raw certificate](../../evidence/claim_3/raw_results.json)
- [Primary verifier](../../code/graphop_repro/claims/claim3_uniform_lipschitz.py)
- [Independent checker](../../code/graphop_repro/independent/claim3_checker.py)
- [Checker output](../../evidence/claim_3/checker_output.json)
- [Control output](../../evidence/claim_3/negative_control_output.json)
- [Method](../../evidence/claim_3/method.md)
- [Limitations](../../evidence/claim_3/limitations.md)

The cumulative verifier exits nonzero if any input assumption, model-class
membership, symbolic inequality, checker, or control changes.

## Provenance

- Scientific Git SHA: `fda190bf3cfcbcb8ed52b5858b6b32f8567e711e`
- Formal run: `c846596c-1b82-4e60-84d6-66b300c26744`
- Compute: one local CPU core; `cpu-upgrade` flavor not applicable
- Runtime: 5 s orchestrated; verifier wall/process `0.236605/0.229570` s
- Seeds: none; the witness and symbolic inequalities are deterministic
- Environment: [pyproject.toml](../../reproduction/pyproject.toml) and
  [uv.lock](../../reproduction/uv.lock)

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 3 | this page | yes | yes | yes | yes | yes | yes | FALSIFIED |
