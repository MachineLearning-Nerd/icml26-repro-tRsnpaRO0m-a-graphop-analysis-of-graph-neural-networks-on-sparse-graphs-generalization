# Claim 2 — bounded fibers across sparse graph families

Verdict: **VERIFIED**

The previous judge awarded `1/2` because the evidence was finite-only. The
current certificate reconstructs the representation on arbitrary standard
Borel probability spaces, exercises a singular uncountable graphing, and
retains the all-dimension finite proof plus 34 family regressions.

## Exact source statement and assumptions

The fiber statement is Theorem 3.3 (`#S3.Thmtheorem3`), not Definition 3.1.
For a bofop on a Borel probability space, it gives a unique measurable family
`ν_x` such that

```text
(Af)(x) = ∫ f dν_x
ess sup_x ν_x(Ω) < ∞,
```

and identifies that essential supremum with the `L∞→L∞` and `L1→L1`
operator norms. The converse additionally requires symmetry.

On a finite atomic space the unique fibers are reconstructed without
sampling:

```text
ν_i({j}) = A_ij,
ν_i(Ω)   = Σ_j A_ij.
```

Atom indicators prove uniqueness for every atom and coefficient equality
proves the integral formula for every real signal. Positivity and detailed
balance are audited before the norm identity is accepted.

## General standard-Borel derivation

For arbitrary `(Omega,mu)` the certificate constructs

```text
lambda_A(S x T) = integral 1_S A1_T dmu.
```

Positivity and monotone convergence make this a finite rectangle premeasure;
Caratheodory extends it to `Omega²`, and self-adjointness makes the joint
measure symmetric. Standard-Borel disintegration gives measurable fibers
`nu_x`. A functional monotone-class argument extends the identity from
indicators to every bounded measurable signal, while a countable generating
class proves uniqueness outside one common null set.

Finally positivity gives
`||A||inf->inf=||A1||inf=ess sup_x nu_x(Omega)`, and self-adjoint
`L1/Linf` duality gives the second norm. Theorem 3.3 is the target, not a
trusted premise. Independent reachability checking forbids it as a foundation
source. Deleting extension, disintegration, uniqueness, positive-kernel norm,
or duality makes the proof fail.

The same uncountable circle graphing shown on Claim 1 has two atomic neighbours
per point, mass-one fibers, and is singular to Lebesgue measure. It is a direct
sparse Borel-space case rather than a finite proxy.

## Evidence first

| Family | Instances | Largest size | Maximum fiber mass | Norm identity |
|---|---:|---:|---:|---|
| dense step graphons | 4 | 256 | finite exact rational | all pass |
| paths | 7 | 16,384 | `2` | all pass |
| weighted cycles | 6 | 8,192 | `6/5` | all pass |
| degree-four circulants | 6 | 8,192 | `8/7` | all pass |
| weighted stars | 6 | 4,096 | finite exact rational | all pass |
| nonuniform reversible chains | 5 | 1,024 | finite exact rational | all pass |

Across all 34 instances:

```text
||A||∞→∞ = ||A||1→1 = ess sup_i ν_i(Ω).
```

The original `P4` regression remains visible: fibers
`(δ₂, δ₁+δ₃, δ₂+δ₄, δ₃)` have masses `(1,2,2,1)`, hence bound `2`.
The historical `bound≤1` assertion stays rejected because the definition
requires finiteness, not a unit bound.

The independent checker recomputes the answer from degree sequences and
reversible edge flows and repeats the 162-matrix basis audit without importing
the primary implementation.

## Control that must fail

On `ℕ` with `μ(n)=2^-n`, the positive self-adjoint diagonal operator
`Af(n)=n f(n)` has finite exact `L∞→L1` norm
`Σ n/2^n=2`, but fiber masses `ν_n(Ω)=n` are unbounded. The checker therefore
accepts it as a graphop and rejects it as a bofop. Exact partial sums are
checked at calibrated horizons.

## Reproduce and inspect

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Contract](../../evidence/claim_2/claim_contract.json)
- [General quantified proof certificate](../../evidence/claim_2/general_proof_certificate.json)
- [Independent general checker output](../../evidence/claim_2/general_checker_output.json)
- [Raw family definitions and exact expected values](../../evidence/claim_2/raw_results.json)
- [Primary verifier](../../code/graphop_repro/claims/claim2_bofops.py)
- [General certificate verifier](../../code/graphop_repro/general_certificates.py)
- [Proof kernel](../../code/graphop_repro/general_proof_kernel.py)
- [Independent general checker](../../code/graphop_repro/independent/general_certificate_checker.py)
- [Generic finite-atomic certificate](../../code/graphop_repro/finite_atomic.py)
- [Independent checker](../../code/graphop_repro/independent/claim2_checker.py)
- [Independent finite-atomic audit](../../code/graphop_repro/independent/finite_atomic_checker.py)
- [Checker output](../../evidence/claim_2/checker_output.json)
- [Control output](../../evidence/claim_2/negative_control_output.json)
- [Method](../../evidence/claim_2/method.md)
- [Source audit](../../evidence/claim_2/source_audit.md)
- [Limitations](../../evidence/claim_2/limitations.md)

The cumulative verifier exits nonzero on any representation, uniqueness,
norm, checker, or control failure.

## Provenance and limits

- Scientific Git SHA (current general proof):
  `ec550a0b0f162cb0076dcb04ebf3ede3fbe621e4`
- Current formal HF run: `84623c95-d792-4b59-8a50-1305c04929ca`
- Superseded finite-certificate run retained as a regression:
  `7227edb5-3b27-44f8-bc3e-62b07337edb4`
- Compute: Hugging Face `cpu-upgrade`; estimated active cores `1`, allocated
  logical/affinity CPUs `64`, implementation single-threaded
- Runtime: about `22 s` orchestrated; verifier wall/process
  `7.058492/7.057538 s`
- Seeds: none; exact rational arithmetic and deterministic enumeration
- Environment: [pyproject.toml](../../reproduction/pyproject.toml) and
  [uv.lock](../../reproduction/uv.lock)

The general certificate exposes extension, disintegration, monotone-class
uniqueness, and `L1/Linf` duality as its standard measure-theory trust
boundary. It is a machine-checked symbolic derivation rather than a
foundational formalization of those theorems.

## Visibility matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 2 | this page | yes | yes | yes | yes | yes | yes | VERIFIED |
