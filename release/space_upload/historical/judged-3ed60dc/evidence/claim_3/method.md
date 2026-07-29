# Claim 3 method

Use singleton probability spaces, zero input signals, and scalar bofops
`A1=0`, `A2=I`, with `r=D=1` and one message-passing layer. For any `M>0`,
choose

```text
phi_0(x)=M,  phi_1(u,v)=v,  psi(z)=z.
```

Their Lipschitz constants are `0,1,1`, so every member is in the formal
`MP_1(1,1,1,1)` class. The outputs are `0` and `M`.

The input pair is fixed as `M` varies. For its `k`-profile, all coordinates lie
in the relevant boxes with a diameter bounded by `2(k+1)`. Therefore

```text
d_M <= sum_{k>=0} 2^-k 2(k+1) = 8.
```

For any proposed finite uniform constant `C`, select `M=8C+1`. Then
`M > 8C >= C d_M`, contradicting the output inequality. The finite sweep is a
sanity check; the diagonal argument covers every finite `C`.

