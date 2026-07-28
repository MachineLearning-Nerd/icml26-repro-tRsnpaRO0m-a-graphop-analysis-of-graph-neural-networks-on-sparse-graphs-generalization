# Claim 5 — universal approximation on realizable DIDMs

Verdict: **VERIFIED**

Theorem M.1 states that for every `L in N0`, continuous real functions on the
bofop-DIDM quotient are uniformly approximable by `L`-layer MPNNs.

Two proof routes were checked:

1. The realizable DIDM image is compact in the metric ambient DIDM space, hence
   closed. Tietze extends any continuous target to the ambient space; the
   earlier ambient MPNN density theorem approximates it; restriction preserves
   the uniform error.
2. Restrict the ambient MPNN algebra to the compact realizable image. It still
   contains constants and separates points, so Stone-Weierstrass applies
   directly.

Neither route uses Corollary 5.3's false strict-subset clause. A control replaces
the compact image by the nonclosed subset `(0,1)` and target `1/x`; the
extension route is correctly rejected.

```text
uv run --frozen python -m graphop_repro.run_all
```

- [Contract](../../../.openresearch/artifacts/claim_5/claim_contract.json)
- [Source audit](../../../.openresearch/artifacts/claim_5/source_audit.md)
- [Raw proof graph](../../../.openresearch/artifacts/claim_5/raw_results.json)
- [Primary verifier](../../../graphop_repro/claims/claim5_universal_approximation.py)
- [Independent checker](../../../graphop_repro/independent/claim5_checker.py)
- [Checker output](../../../.openresearch/artifacts/claim_5/checker_output.json)
- [Control output](../../../.openresearch/artifacts/claim_5/negative_control_output.json)
- [Method](../../../.openresearch/artifacts/claim_5/method.md)
- [Limitations](../../../.openresearch/artifacts/claim_5/limitations.md)

