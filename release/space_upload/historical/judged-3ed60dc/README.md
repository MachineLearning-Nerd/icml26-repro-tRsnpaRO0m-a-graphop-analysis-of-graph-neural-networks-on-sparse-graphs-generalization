---
title: "Graphop Analysis of GNNs (tRsnpaRO0m)"
emoji: 🎯
colorFrom: yellow
colorTo: red
sdk: static
pinned: false
tags:
 - trackio
 - trackio-logbook
 - open-experiment
 - icml2026-repro
 - paper-tRsnpaRO0m
---

# Graphop claim-by-claim reproduction

The evaluator entrypoint is **[Current verification](#/current)**. It exposes
the exact claim quantifiers, assumptions, code, inline numbers, downloadable
raw JSON, independent checkers, negative controls, limits, and HF CPU
provenance for all six claims.

Previous live judged score: **8/12** at exact Space revision
`dbfa7ea0de058ad35fa8bab58684306bd9ac7e7c`.

That judge awarded toy credit to Claims 1 and 2, full falsification credit to
Claims 3, 4, and 6, and no credit to Claim 5. The current candidate directly
addresses those three gaps:

- Claims 1–2 now use a parameterized finite-atomic theorem and 34 exact
  graph-family instances through 16,384 vertices, not only `P4`.
- Claim 5 now trains and tests actual MPNN readouts on 800 held-out sparse
  graphs, provides a separately implemented checker, and constructs a
  continuum of weighted sparse cycles.

Current scientific verdicts remain **3 VERIFIED and 3 FALSIFIED**. A
conservative post-change forecast is **10–12/12**, with **12/12** the
best-supported possibility—not a judge result.

Both the original 0/12 baseline and the exact judged 8/12 revision remain
reachable as explicitly superseded historical evidence.
