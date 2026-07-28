# Claim 4 — the stated strictness is false at depth zero

Verdict: **FALSIFIED**

Corollary 5.3 states that for **every** `L in N0` and `r>0`,
`Gamma_L(BF_d^r)` is a compact **strict** subset of `P(H^L)`. Definition 2.1
sets `H^0=[-1,1]^d`; Definition 5.1 sets `gamma_0=f` and
`Gamma_0=f_*mu`.

For arbitrary `pi in P(H^0)`, choose

```text
Omega=H^0,  mu=pi,  A=0,  f=id_H0.
```

The zero operator is linear, self-adjoint, positivity preserving, and has norm
zero, so it satisfies the `r` bound for every `r>0`. The identity is an
admissible signal, and therefore

```text
Gamma_0 = (id_H0)_* pi = pi.
```

Because `pi` was arbitrary, `Gamma_0(BF_d^r)=P(H^0)`, contradicting the
asserted strict inclusion. This falsifies the exact universally quantified
claim. It does **not** falsify compactness or claim anything about strictness
for `L>=1`.

## Independent check and control

The independent checker reconstructs all quantified obligations and confirms
the universal identity-pushforward argument. It also exhausts all 15
denominator-four probability measures on `{-1,0,1}` as a sanity check.
Changing the critical depth from zero to one rejects the same construction:
with `A=0`, the depth-one neighbor measure has mass zero and cannot equal the
control target of mass one.

## Reproduce and inspect

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Contract](../../../.openresearch/artifacts/claim_4/claim_contract.json)
- [Source audit](../../../.openresearch/artifacts/claim_4/source_audit.md)
- [Raw certificate](../../../.openresearch/artifacts/claim_4/raw_results.json)
- [Primary verifier](../../../graphop_repro/claims/claim4_didm_counterexample.py)
- [Independent checker](../../../graphop_repro/independent/claim4_checker.py)
- [Checker output](../../../.openresearch/artifacts/claim_4/checker_output.json)
- [Control output](../../../.openresearch/artifacts/claim_4/negative_control_output.json)
- [Method](../../../.openresearch/artifacts/claim_4/method.md)
- [Limitations](../../../.openresearch/artifacts/claim_4/limitations.md)

The cumulative verifier exits nonzero if any assumption, derivation, checker,
or control changes.

## Provenance

- Scientific Git SHA: `5dfb2d3b4bbf28572910d199f54cf276b12b3c7d`
- Formal run: `ee7f63fb-06bf-4cc7-923e-af98986cb332`
- Compute: one local CPU core; `cpu-upgrade` flavor not applicable
- Runtime: 5 s orchestrated; verifier wall/process `0.244421/0.241344` s
- Seeds: none; the universal construction and finite sanity grid are deterministic
- Environment: [pyproject.toml](../../../pyproject.toml) and
  [uv.lock](../../../uv.lock)

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 4 | this page | yes | yes | yes | yes | yes | yes | FALSIFIED |
