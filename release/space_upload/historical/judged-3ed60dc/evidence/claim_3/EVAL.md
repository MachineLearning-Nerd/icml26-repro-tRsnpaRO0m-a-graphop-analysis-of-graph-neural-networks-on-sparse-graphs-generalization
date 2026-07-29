# Claim 3 evaluation

Verdict: **FALSIFIED**

The exact uniform output bound fails for the paper's formal `MP_D` class
because that class controls slopes but not offsets. A fixed pair of valid
singleton bofops has action distance at most 8, while an admissible one-layer
MPNN family has output gap `M`. Choosing `M=8C+1` defeats every proposed finite
constant depending only on `L,D,r`.

