# Claim 2 method

The general route starts from
`lambda_A(S x T)=integral 1_S A1_T dmu`. Positivity and monotone convergence
make this a finite rectangle premeasure; Caratheodory extends it, and
self-adjointness makes the joint measure symmetric. Standard-Borel
disintegration produces the measurable fibers. A functional monotone-class
argument extends the representation from indicators to all bounded signals,
and a countable generating class proves uniqueness outside one common null
set. Positivity gives `||A||inf=||A1||inf=ess sup nu_x(Omega)`;
self-adjoint L1/Linf duality gives the second norm.

The certificate is checked by two non-importing implementations. Removing
extension, disintegration, uniqueness, positive-kernel norm, or duality makes
the target unreachable.

Exact rational arithmetic constructs finite fibers through
`nu_i({j})=A_ij`. Atom indicators prove uniqueness and coefficient equality
proves the integral identity for every real signal. The verifier computes the
row-mass, weighted-column, and essential-supremum formulas on the same six
families used for Claim 1. The independent checker instead uses closed-form
degree and reversible-flow formulas.

The original `P4` enumeration remains as a regression. The countable negative
control is also unchanged and uses the exact partial-sum identity
`sum_{n=1}^N n/2^n = 2-(N+2)/2^N` at calibrated horizons.
