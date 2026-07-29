# Release report

- Previous live judged score: `9/12`
- Conservative projected score range after the proposed change: `9–12/12`
- Best-supported possible new score: `12/12` **forecast, not a judge result**

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 1 | 2 | MEDIUM | VERIFIED | Quantified Horn certificate derives positivity/self-adjointness on arbitrary spaces; independent premise checker; singular uncountable circle graphing; finite regressions retained. Remaining risk: the judge may require a third-party foundational prover rather than the explicit Fubini trust boundary. |
| 2 | 1 | 2 | MEDIUM | VERIFIED | General standard-Borel joint-measure, extension, disintegration, uniqueness, and norm certificate with independent checker and uncountable sparse graphing. Remaining risk: standard measure lemmas are trusted rather than re-proved from foundations. |
| 3 | 2 | 2 | MEDIUM | FALSIFIED | Preserved full-credit singleton counterexample defeats every finite constant under the displayed `MP_D` definition. Interpretation risk remains because prose mentions bounded hidden states. |
| 4 | 2 | 2 | HIGH | FALSIFIED | Preserved full-credit counterexample at allowed `L=0` contradicts exactly the universal strict-subset clause. |
| 5 | 1 | 2 | MEDIUM | VERIFIED | Independent recursive DIDM-separation and MPNN-algebra certificate plus Stone-Weierstrass; E.12/M.1 forbidden as premises; actual MPNN and continuum retained. Remaining risk: the judge may demand formalization of Riesz/Stone-Weierstrass in a third-party prover. |
| 6 | 2 | 2 | MEDIUM | FALSIFIED | Preserved full-credit exact two-point counterexample and binomial bad-event probabilities. It shares Claim 3's formal-versus-prose class risk. |

Current total score: **9/12 live judged**. Conservative projected total after
this candidate: **9–12/12**. Best-supported possible total: **12/12**,
forecast only.

Claims targeted since the previous judge result: **1, 2, and 5**. Claims 3, 4,
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
            └── orx/general-probability-space-proof-certificates
```

- Claims 1–2 scientific commit:
  `006a1a8068f1a067d3bbf527398528426cc60569`
- Claims 1–2 HF run:
  `7227edb5-3b27-44f8-bc3e-62b07337edb4`
- Claim 5 cumulative scientific winner:
  `d8343afb3e2ec346a2480454ba79363abe0f76fd`
- Claim 5 HF run:
  `a31c30b1-f9d8-497a-9b27-0d85a472912f`
- General probability-space proof commit:
  `ec550a0b0f162cb0076dcb04ebf3ede3fbe621e4`
- General proof HF run:
  `84623c95-d792-4b59-8a50-1305c04929ca`
- Evaluator-visible release commit:
  `6088b759eef56d04ae7c295d2a5dcb53ca4f6868`
- Evaluator-visible release HF run:
  `bc69e18c-a2fd-412a-b8d5-99388fc4f317`
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
4. confirm judged revision `3ed60dc...` remains archived, the older
   `dbfa7ea...` archive remains reachable, and every original path is present;
5. mirror the exact reader-facing text paths to GitHub `main`;
6. verify GitHub with `git ls-remote`; and
7. leave the paper awaiting the live judge.

No score increase will be claimed until the live verdict dataset records the
new revision.

## Pre-upload summary

| Claim | Status | Expected points | Confidence | Expected evaluator status |
|---|---|---:|---|---|
| 1 | VERIFIED | 2 | MEDIUM | arbitrary-space certificate plus uncountable singular graphing |
| 2 | VERIFIED | 2 | MEDIUM | general Borel extension/disintegration and norm certificate |
| 3 | FALSIFIED | 2 | MEDIUM | preserved prior full-credit counterexample |
| 4 | FALSIFIED | 2 | HIGH | preserved prior full-credit counterexample |
| 5 | VERIFIED | 2 | MEDIUM | independent all-target separation/density proof plus actual MPNN |
| 6 | FALSIFIED | 2 | MEDIUM | preserved prior full-credit counterexample |

Conservative projected total: **9–12/12**. Best-supported possible score:
**12/12 forecast**. Remaining BLOCKED risk: none. The material residual risks
are whether the evaluator accepts the explicit standard-theorem trust boundary
instead of requiring a third-party foundational prover, and the already
acknowledged formal-versus-prose interpretation for Claims 3 and 6.
