# Evaluator-blind pre-publication review

The review began in a fresh empty directory containing only:

1. the exact judged Space revision
   `dbfa7ea0de058ad35fa8bab58684306bd9ac7e7c`; and
2. the proposed text-file overlay.

The reviewer used only `README.md`, `logbook.json`, pages reachable from their
navigation, and the evaluator rubric. No OpenResearch dashboard state, local
repository knowledge, unpublished branch paths, or verbal hints were used to
locate evidence.

## Questions asked without location hints

For each claim:

- What exact statement and quantifiers are tested?
- Which file is the current verifier?
- Can the command, pinned environment, source, raw data, inline result,
  independent checker, failing control, limitations, Git SHA, seed policy,
  CPU allocation, and runtime all be found?
- Does the evidence establish the verdict at the stated scope, or is it a toy
  or proxy?
- Is any rejected historical verifier presented as current?

## First fresh traversal

Result: **PASS**.

- Canonical start: `README.md` → `logbook.json` →
  `pages/current/index.md`
- Canonical files opened: `163`
- Candidate text files scanned: `366`
- Exact judged paths checked: `182`
- Judged-path subset: **PASS**
- Broken links: `0`
- Secret scan: **PASS**
- Navigation digest:
  `d14ab0ade2bfd400771bdd3db29fa63cf826099633df3cb4a6f4b6211f509a27`

The reviewer found the current cumulative verifier at
`graphop_repro/run_all.py` without assistance. Claims 1, 2, and 5 expose the
new verifier first; the old 8/12 versions are reachable only under
**Historical judged 8/12 revision — superseded**. The older 0/12 overview
remains under **Historical rejected baseline**.

## Conclusions located

| Claim | Exact contract found | Executable evidence found | Control found | Blind conclusion |
|---|---|---|---|---|
| 1 | yes | parameterized finite theorem, 34-instance sweep, independent 162-matrix audit | asymmetric-positive and symmetric-negative mutations | VERIFIED at finite-atomic scope; uncountable extension limitation visible |
| 2 | yes | unique-fiber/all-real-signal proof and norm sweep | exact countable graphop/non-bofop separator | VERIFIED at finite/countable scope; uncountable kernel limitation visible |
| 3 | yes | preserved formal counterexample | bounded-offset repair | FALSIFIED, interpretation risk visible |
| 4 | yes | preserved `L=0` counterexample | invalid depth-one mutation | FALSIFIED |
| 5 | yes | actual L=2 MPNN, 800 held-out graphs, independent readout, continuum, topological reduction | no-message, shifted-label, and discontinuity controls | VERIFIED with general-proof dependency risk visible |
| 6 | yes | preserved exact two-point/binomial counterexample | bounded-envelope repair | FALSIFIED, interpretation risk visible |

No conclusion remained unverifiable after the first traversal.

## Final traversal after manifest generation

The exact list of every file opened is recorded in
[blind-review-files.txt](blind-review-files.txt). After generating the upload
allowlist and SHA-256 manifest, the candidate is rebuilt again from another
empty directory and the same no-hints traversal is repeated.

Final result: **PASS**.

- Canonical files opened: `164`
- Candidate text files scanned: `367`
- Exact judged paths checked: `182`
- Judged-path subset: **PASS**
- Broken links: `0`
- Secret scan: **PASS**
- Upload allowlist entries: `359`
- Non-self SHA-256 manifest entries: `358`, all **PASS**
- Navigation digest:
  `dfb8c8f511b7e0522337078f2b7479051a8c060edec466aad095773ecf0b4b1c`

No conclusion remained unverifiable. The current verifier, not historical
code, is the obvious verifier, and every displayed number on Claims 1, 2, and
5 matches its downloadable expected-result JSON.
