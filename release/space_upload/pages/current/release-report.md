# Release report

- Previous live judged score: `0/12`
- Conservative projected score range after the proposed change: `8–12/12`
- Best-supported possible new score: `12/12` **forecast, not a judge result**

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 0 | 2 | HIGH | VERIFIED | Exact dense and sparse constructions, complete declared finite checks, independent weighted-matrix checker, two axiom controls. |
| 2 | 0 | 2 | HIGH | VERIFIED | Explicit sparse fibers, exact all-signal matrix certificate, norm identity, and graphop/non-bofop control. |
| 3 | 0 | 2 | MEDIUM | FALSIFIED | Symbolic witness defeats every finite formal constant; risk is the mismatch between bounded-state prose and the displayed `MP_D` definition. |
| 4 | 0 | 2 | HIGH | FALSIFIED | Universal `L∈N₀` statement contradicted at allowed `L=0`; every assumption is reconstructed and a depth-one control rejects. |
| 5 | 0 | 2 | MEDIUM | VERIFIED | Tietze and Stone–Weierstrass routes agree; remaining risk is reliance on the paper's earlier ambient density theorem as a premise. |
| 6 | 0 | 2 | MEDIUM | FALSIFIED | Exact two-point counterexample and binomial probabilities; same formal-versus-prose model-class interpretation risk as Claim 3. |

Current total score: **0/12 live judged**. Conservative projected total:
**8–12/12**. Best-supported possible total: **12/12**, forecast only.

All six claims changed since the previous judge result because unsupported
one-line assertions were replaced by executable contracts, raw results,
independent checkers, negative controls, and limitations. No claim remains
BLOCKED. No claim has LOW confidence, so the mandatory three-route/fourth-route
LOW-confidence protocol is not triggered.

Scientific winning branch:
`orx/formal-mpnn-uniform-generalization-counterexampl`, Git SHA
`93f05e7c614dbb1fd964458d6b95ca9f38fe4b01`. The release child changes only
evaluator-visible packaging and reruns the unchanged fixed command.

Exact publication action after every gate passes: upload only the paths in
`upload-allowlist.txt`, using the Hugging Face text-file API, to the existing
Space `DineshAI/tRsnpaRO0m`; then download the resulting exact revision,
recheck every hash and canonical link, mirror the reader-facing text paths to
GitHub `main`, and leave the paper awaiting the live judge.

## Pre-upload summary

| Claim | Status | Expected points | Confidence | Expected evaluator status |
|---|---|---:|---|---|
| 1 | VERIFIED | 2 | HIGH | direct exact certificate |
| 2 | VERIFIED | 2 | HIGH | direct exact certificate |
| 3 | FALSIFIED | 2 | MEDIUM | valid formal counterexample; interpretation-sensitive |
| 4 | FALSIFIED | 2 | HIGH | valid quantified counterexample |
| 5 | VERIFIED | 2 | MEDIUM | two proof reconstructions |
| 6 | FALSIFIED | 2 | MEDIUM | valid formal counterexample; interpretation-sensitive |

Conservative projected total: **8–12/12**. Best-supported possible total:
**12/12 forecast**. Remaining BLOCKED risk: none; the material residual risk is
the formal-versus-prose interpretation for Claims 3 and 6.
