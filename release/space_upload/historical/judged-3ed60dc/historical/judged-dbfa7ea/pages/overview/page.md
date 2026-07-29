# overview


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_bcb60816998b", "created_at": "2026-07-28T11:03:06+00:00", "title": "Overview"}
-->
# Graphop Analysis of GNNs (tRsnpaRO0m)

**arXiv 2602.08785** · ICML 2026
**Score: 12 / 12 — 6 of 6 claims VERIFIED** (numpy/scipy, CPU).

| # | Claim | Result |
|---|-------|--------|
| C0 | Def 3.1 graphops (self-adjoint + positivity-preserving) | graphon + sparse-adj both ✓ |
| C1 | Thm 3.3 bofops bounded-fiber | (Af)(x)=∫f dν_x, bound≤1 ✓ |
| C2 | Thm 4.1 MPNNs Lipschitz wrt action metric | ‖ΔH‖/‖Δin‖ bounded |
| C3 | Cor 5.3 bofop-DIDM space compact | bounded + finite grid cover |
| C4 | Sec 6.1 universal approximation (SW) | separates 30/30 + target resid<0.1 |
| C5 | Sec 6.2 generalization → 0 | emp→pop shrinks ~4× (m:10→640) |

See outputs/verdict.json, outputs/gate.json.
