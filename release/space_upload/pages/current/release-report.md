# Release report

- Previous live judged score: `8/12`
- Conservative projected score range after the proposed change: `10–12/12`
- Best-supported possible new score: `12/12` **forecast, not a judge result**

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 1 | 2 | MEDIUM | VERIFIED | Necessary-and-sufficient certificate for every finite atomic operator; 34 dense/sparse instances through 16,384 vertices; independent 162-matrix audit. Remaining risk: evaluator may require a proof-assistant treatment of arbitrary uncountable spaces rather than the source-level graphon derivation. |
| 2 | 1 | 2 | MEDIUM | VERIFIED | Unique finite fibers and all-real-signal norm identities, 34-instance sweep, and exact countable graphop/non-bofop control. Remaining risk: uncountable Borel kernel existence is audited mathematically rather than mechanized. |
| 3 | 2 | 2 | MEDIUM | FALSIFIED | Preserved full-credit singleton counterexample defeats every finite constant under the displayed `MP_D` definition. Interpretation risk remains because prose mentions bounded hidden states. |
| 4 | 2 | 2 | HIGH | FALSIFIED | Preserved full-credit counterexample at allowed `L=0` contradicts exactly the universal strict-subset clause. |
| 5 | 0 | 2 | MEDIUM | VERIFIED | Actual L=2 MPNN on 800 held-out sparse graphs (`0.034723199005` max error), independent readout (`0.019023154804`), weighted-cycle continuum, and source-anchored general restriction proof. Remaining risk: the general route accepts the paper's earlier ambient density theorem E.12. |
| 6 | 2 | 2 | MEDIUM | FALSIFIED | Preserved full-credit exact two-point counterexample and binomial bad-event probabilities. It shares Claim 3's formal-versus-prose class risk. |

Current total score: **8/12 live judged**. Conservative projected total after
this candidate: **10–12/12**. Best-supported possible total: **12/12**,
forecast only.

Claims changed since the previous judge result: **1, 2, and 5**. Claims 3, 4,
and 6 retain the exact evidence that already received full credit. No claim is
BLOCKED and no claim has LOW confidence, so the three-route plus mandatory
fourth-route LOW-confidence protocol is not triggered.

## Experiment-tree result

The strengthened line descends from the prior evaluator-visible node:

```text
orx/evaluator-visible-release-candidate
└── orx/general-finite-graphop-and-bofop-certificates
    └── orx/constructive-mpnn-universal-approximation-eviden
        └── orx/evaluator-visible-strengthened-evidence-candidat
```

- Claims 1–2 scientific commit:
  `006a1a8068f1a067d3bbf527398528426cc60569`
- Claims 1–2 HF run:
  `7227edb5-3b27-44f8-bc3e-62b07337edb4`
- Claim 5 cumulative scientific winner:
  `d8343afb3e2ec346a2480454ba79363abe0f76fd`
- Claim 5 HF run:
  `a31c30b1-f9d8-497a-9b27-0d85a472912f`
- Exact fixed command everywhere:
  `uv run --frozen python -m graphop_repro.run_all`

The release child changes evaluator-visible packaging only and reruns that
unchanged cumulative command.

## Exact publication action

After every gate passes, upload only paths in `upload-allowlist.txt` through
the Hugging Face text-file API to the existing Space
`DineshAI/tRsnpaRO0m`. Do not create another Space. Then:

1. download the exact resulting revision;
2. verify every allowlisted SHA-256 hash;
3. repeat canonical traversal from `README.md` and `logbook.json`;
4. confirm judged revision `dbfa7ea...` remains archived and every original
   path remains present;
5. mirror the exact reader-facing text paths to GitHub `main`;
6. verify GitHub with `git ls-remote`; and
7. leave the paper awaiting the live judge.

No score increase will be claimed until the live verdict dataset records the
new revision.

## Pre-upload summary

| Claim | Status | Expected points | Confidence | Expected evaluator status |
|---|---|---:|---|---|
| 1 | VERIFIED | 2 | MEDIUM | parameterized finite theorem, no longer a four-node toy |
| 2 | VERIFIED | 2 | MEDIUM | parameterized fiber/norm certificate, no longer a four-node toy |
| 3 | FALSIFIED | 2 | MEDIUM | preserved prior full-credit counterexample |
| 4 | FALSIFIED | 2 | HIGH | preserved prior full-credit counterexample |
| 5 | VERIFIED | 2 | MEDIUM | actual MPNN measurements plus constructive and general routes |
| 6 | FALSIFIED | 2 | MEDIUM | preserved prior full-credit counterexample |

Conservative projected total: **10–12/12**. Best-supported possible score:
**12/12 forecast**. Remaining BLOCKED risk: none. The material residual risks
are the unmechanized uncountable-space steps for Claims 1–2, reliance on
Theorem E.12 for Claim 5's full generality, and the already acknowledged
formal-versus-prose interpretation for Claims 3 and 6.
