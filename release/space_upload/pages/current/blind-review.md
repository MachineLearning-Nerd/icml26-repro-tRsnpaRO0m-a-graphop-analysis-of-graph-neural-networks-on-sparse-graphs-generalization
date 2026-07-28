# Evaluator-blind pre-publication review

The review used only a fresh materialization of the exact judged Space
revision plus the proposed text-file overlay. Repository knowledge, OpenResearch
logs, dashboard artifacts, and unpublished branch paths were not used to fill
gaps.

## Preliminary inspection and fixes

The first inspection found four visibility/package defects:

1. the illustrated report linked to the GitHub-only `candidate/` layout;
2. the Space did not expose the root `graphop_repro`, `pyproject.toml`,
   `uv.lock`, and `.openresearch/artifacts` paths needed by the exact command;
3. Claims 5 and 6 showed the command but lacked an explicit “Reproduce”
   heading;
4. claim-page links retained one extra `..` after moving into the Space page
   hierarchy.

All four were fixed. No scientific verdict changed.

## First complete traversal after fixes

Result: **PASS**.

- Canonical entrypoint: `README.md` → `logbook.json` →
  `pages/current/index.md`
- Files opened: `76`
- Candidate text files checked: `175`
- Historical judged files: `13`; subset check: **PASS**
- Broken local links: `0`
- Secret scan: **PASS**
- Navigation digest:
  `53da791898ae07c28dec2efe85db57a104ec97667caa80df25a0996aeda51093`

Every file opened, in order:

```text
README.md
logbook.json
pages/current/index.md
pages/claims/claim-1.md
pages/claims/claim-2.md
pages/claims/claim-3.md
pages/claims/claim-4.md
pages/claims/claim-5.md
pages/claims/claim-6.md
pages/current/release-report.md
pages/index.md
pages/overview/page.md
pyproject.toml
uv.lock
graphop_repro/run_all.py
evidence/source/paper_source_audit.md
reports/reproduction/report.md
notebooks/graphop_claims.py
code/graphop_repro/claims/claim1_graphops.py
evidence/claim_1/raw_results.json
evidence/claim_1/checker_output.json
evidence/claim_1/negative_control_output.json
code/graphop_repro/claims/claim2_bofops.py
evidence/claim_2/raw_results.json
evidence/claim_2/checker_output.json
evidence/claim_2/negative_control_output.json
code/graphop_repro/claims/claim3_uniform_lipschitz.py
evidence/claim_3/raw_results.json
evidence/claim_3/checker_output.json
evidence/claim_3/negative_control_output.json
code/graphop_repro/claims/claim4_didm_counterexample.py
evidence/claim_4/raw_results.json
evidence/claim_4/checker_output.json
evidence/claim_4/negative_control_output.json
code/graphop_repro/claims/claim5_universal_approximation.py
evidence/claim_5/raw_results.json
evidence/claim_5/checker_output.json
evidence/claim_5/negative_control_output.json
code/graphop_repro/claims/claim6_generalization.py
evidence/claim_6/raw_results.json
evidence/claim_6/checker_output.json
evidence/claim_6/negative_control_output.json
evidence/claim_1/claim_contract.json
code/graphop_repro/independent/claim1_checker.py
evidence/claim_1/method.md
evidence/claim_1/limitations.md
reproduction/pyproject.toml
reproduction/uv.lock
evidence/claim_2/claim_contract.json
code/graphop_repro/independent/claim2_checker.py
evidence/claim_2/method.md
evidence/claim_2/limitations.md
evidence/claim_3/claim_contract.json
evidence/claim_3/source_audit.md
code/graphop_repro/independent/claim3_checker.py
evidence/claim_3/method.md
evidence/claim_3/limitations.md
evidence/claim_4/claim_contract.json
evidence/claim_4/source_audit.md
code/graphop_repro/independent/claim4_checker.py
evidence/claim_4/method.md
evidence/claim_4/limitations.md
evidence/claim_5/claim_contract.json
evidence/claim_5/source_audit.md
code/graphop_repro/independent/claim5_checker.py
evidence/claim_5/method.md
evidence/claim_5/limitations.md
evidence/claim_6/claim_contract.json
evidence/claim_6/source_audit.md
code/graphop_repro/independent/claim6_checker.py
evidence/claim_6/method.md
evidence/claim_6/limitations.md
reports/reproduction/images/headline.svg
reports/reproduction/images/graphop-examples.svg
reports/reproduction/images/uniform-constant.svg
reports/reproduction/images/generalization.svg
```

No conclusion remained unverifiable after this traversal.

## Second fresh traversal

After adding this review, the command ledger, the exact allowlist, and the
SHA-256 manifest, a new empty directory was populated from the exact judged
revision and overlaid again.

Result: **PASS**.

- Files opened: `78` (the 76 above, followed by
  `pages/current/blind-review.md` and `pages/current/command-ledger.md`)
- Candidate text files checked: `179`
- Historical judged files: `13`; subset check: **PASS**
- Broken local links: `0`
- Secret scan: **PASS**
- All 170 non-self manifest entries: **PASS**
- Navigation digest:
  `6ce298e8903e8b13dbc304c2d63770aa12d7cb170076af153046489abed981a2`

No conclusion remained unverifiable. The current verifier is the root
`graphop_repro/run_all.py`; the old `pages/overview/page.md` is reachable only
as **Historical rejected baseline** in current navigation.
