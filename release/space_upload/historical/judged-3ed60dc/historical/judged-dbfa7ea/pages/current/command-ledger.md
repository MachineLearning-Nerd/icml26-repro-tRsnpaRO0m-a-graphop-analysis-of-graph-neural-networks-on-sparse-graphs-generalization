# Reproduction command ledger

No command below contains a token, credential value, or generated run wrapper.
The same formal command was inherited by every experiment.

## Startup and source audit

```text
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx projects --json
orx project view 2ffa28c7-b71a-4b21-889f-cfa977b5bd92
orx runs 2ffa28c7-b71a-4b21-889f-cfa977b5bd92
git branch -a
git status --short
git rev-parse HEAD
git rev-parse main
df -h .
env | cut -d= -f1 | sort
curl -L --fail --user-agent OpenResearch-Reproduction/1.0 https://ar5iv.labs.arxiv.org/html/2602.08785
shasum -a 256 2602.08785.html
orx paper 2602.08785 --full
git clone https://huggingface.co/datasets/ICML-2026-agent-repro/verdicts
git clone https://huggingface.co/spaces/DineshAI/tRsnpaRO0m
git checkout 9ded82baa88100f73731decd32ad0895120ae8ba
```

Verdicts were filtered by exact
`space_id == "DineshAI/tRsnpaRO0m"`, not by OpenReview ID.

## Experiment creation and formal runs

```text
orx project edit 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --run-command 'uv run --frozen python -m graphop_repro.run_all'
orx create-experiment 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --title 'Frozen baseline: exact graphop definition'
orx exp run 24c864c0-bb81-4e9e-aad9-9ad4dc68c0d5 --backend local
orx exp wait 24c864c0-bb81-4e9e-aad9-9ad4dc68c0d5 --timeout 480
orx logs ee300364-c697-4086-9663-c4a33434159e

orx create-experiment 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --parent 24c864c0-bb81-4e9e-aad9-9ad4dc68c0d5 --title 'Exact bounded-fiber characterization'
orx exp run 4f0ea963-f929-4ee2-97b2-5787bfc63805 --backend local
orx exp wait 4f0ea963-f929-4ee2-97b2-5787bfc63805 --timeout 480
orx logs 1445490d-0fb2-4913-9174-43cf88467c06

orx create-experiment 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --parent 4f0ea963-f929-4ee2-97b2-5787bfc63805 --title 'Corollary 5.3 L=0 counterexample'
orx exp run 1e8f0304-e748-4942-ab43-3255ab516c7a --backend local
orx exp wait 1e8f0304-e748-4942-ab43-3255ab516c7a --timeout 480
orx logs ee7f63fb-06bf-4cc7-923e-af98986cb332

orx create-experiment 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --parent 1e8f0304-e748-4942-ab43-3255ab516c7a --title 'Theorem 4.1 uniform-constant counterexample'
orx exp run 0fc6f76d-723c-4676-afe6-6776fd648040 --backend local
orx exp wait 0fc6f76d-723c-4676-afe6-6776fd648040 --timeout 480
orx logs c846596c-1b82-4e60-84d6-66b300c26744

orx create-experiment 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --parent 0fc6f76d-723c-4676-afe6-6776fd648040 --title 'Universal approximation proof reconstruction'
orx exp run 27da7111-558d-4ed0-a41c-7159d1cc198a --backend local
orx exp wait 27da7111-558d-4ed0-a41c-7159d1cc198a --timeout 480
orx logs 45e8f034-b4ac-48db-8656-db623cbdcf4b

orx create-experiment 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --parent 27da7111-558d-4ed0-a41c-7159d1cc198a --title 'Formal MPNN uniform generalization counterexample'
orx exp run 8720dc3c-f7e1-4cb0-9418-e728cad3634b --backend local
orx exp wait 8720dc3c-f7e1-4cb0-9418-e728cad3634b --timeout 480
orx logs bc615e3c-ac90-478e-ab2e-947548f6a405

orx create-experiment 2ffa28c7-b71a-4b21-889f-cfa977b5bd92 --parent 8720dc3c-f7e1-4cb0-9418-e728cad3634b --title 'Evaluator-visible release candidate'
```

Exact formal command inherited by every node:

```text
uv run --frozen python -m graphop_repro.run_all
```

## Release validation

```text
marimo check notebooks/graphop_claims.py
xmllint --noout reports/reproduction/images/*.svg
rsvg-convert -w 1200 reports/reproduction/images/<figure>.svg -o <temporary-preview>.png
git clone https://huggingface.co/spaces/DineshAI/tRsnpaRO0m <fresh-directory>
git checkout 9ded82baa88100f73731decd32ad0895120ae8ba
git archive 9ded82baa88100f73731decd32ad0895120ae8ba
uv run --frozen python release/validate_candidate.py <fresh-candidate> <judged-tree>
```

The low-level read-only file inspections (`rg`, `sed`, `find`, `file`,
`git diff`, `git status`, `git show`, `git ls-remote`) do not alter scientific
evidence; their relevant outputs are captured in the source audit, protected
manifest, visibility matrix, and blind-review page.
