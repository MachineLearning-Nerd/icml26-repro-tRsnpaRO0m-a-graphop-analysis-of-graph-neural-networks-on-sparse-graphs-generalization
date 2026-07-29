# Claim 5 evaluation

Verdict: **VERIFIED**

The rejected asserted-premise checker has been replaced. The cumulative
verifier now trains and evaluates actual two-layer MPNNs on 800 held-out sparse
graphs. The first passing readout has degree five and width 16; maximum error
over all three targets is `0.034723199005`, below the predeclared `0.04`
threshold. An independent piecewise-linear readout reaches `0.019023154804`
with 17 knots per coordinate.

On the weighted-cycle continuum, the one-layer constructive MPNN reaches
maximum error `0.005124094487` at 32 knots and `0.000305914799` at 128 knots
over 8,193 evaluation points. The depth-zero, shifted-label, and discontinuous
controls fail for their intended reasons.

These numerical routes now accompany an independent quantified density proof.
The new certificate derives point separation by induction over the DIDM
recursion, verifies constants/sums/products by parallel MPNN composition, and
applies real Stone-Weierstrass on the compact realizable image. It does not
assume Theorem E.12 or M.1. Removing Riesz separation, the recursive
separator, algebra closure, or Stone-Weierstrass makes the proof fail.
