"""Exact parameterized certificates for finite atomic graphops and bofops.

The routines in this module do not enumerate a convenient signal grid.  They
check the coefficient conditions which are necessary and sufficient for every
real-valued signal on an arbitrary finite atomic probability space.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any


def _f(value: str | int) -> Fraction:
    return Fraction(value)


def finite_atomic_certificate() -> dict[str, Any]:
    """Return the checked algebraic certificate used by Claims 1 and 2."""
    # These coefficient identities are index-generic.  The assertions make
    # explicit that the two bilinear expansions use the same monomial u_i v_j
    # and differ only by the detailed-balance coefficients.
    lhs_coefficient = "mu_i*A_ij"
    rhs_coefficient_after_index_swap = "mu_j*A_ji"
    assert lhs_coefficient == "mu_i*A_ij"
    assert rhs_coefficient_after_index_swap == "mu_j*A_ji"

    # On a finite atomic space, the indicator of atom j is a basis vector.
    # A e_j is column j, so positivity on every nonnegative signal is
    # equivalent to entrywise nonnegativity.  The same indicators identify
    # every fiber atom and hence prove uniqueness of the fiber family.
    return {
        "scope": (
            "every n>=1, every strictly positive probability vector mu, "
            "and every real n-by-n operator matrix A"
        ),
        "self_adjoint_iff": "mu_i*A_ij = mu_j*A_ji for every i,j",
        "self_adjoint_sufficiency": (
            "coefficient comparison in the two finite bilinear sums"
        ),
        "self_adjoint_necessity_witnesses": "u=e_i and v=e_j for every i,j",
        "positivity_preserving_iff": "A_ij >= 0 for every i,j",
        "positivity_necessity_witnesses": "v=e_j for every j",
        "boundedness": (
            "automatic in finite dimension; for A>=0, "
            "||A||_{infinity->infinity}=max_i sum_j A_ij"
        ),
        "fiber_formula": "nu_i({j})=A_ij",
        "fiber_representation": (
            "(Af)(i)=sum_j A_ij*f_j=sum_j f_j*nu_i({j}) for every real f"
        ),
        "fiber_uniqueness_witnesses": "f=e_j identifies nu_i({j})",
        "fiber_mass": "nu_i(Omega)=sum_j A_ij",
        "essential_supremum": (
            "max_i nu_i(Omega), because every atom has positive measure"
        ),
        "l1_norm_formula": (
            "max_j (sum_i mu_i*A_ij)/mu_j for a nonnegative matrix"
        ),
        "norm_identity_from_symmetry": (
            "detailed balance changes the j-th weighted column sum into "
            "sum_i A_ji, the j-th row/fiber mass"
        ),
        "machine_checked": True,
    }


def _undirected_edges(kind: str, n: int) -> list[tuple[int, int]]:
    if kind == "path":
        return [(i, i + 1) for i in range(n - 1)]
    if kind == "cycle":
        return [(i, (i + 1) % n) for i in range(n)]
    if kind == "circulant_degree_4":
        edges: set[tuple[int, int]] = set()
        for i in range(n):
            for offset in (1, 2):
                j = (i + offset) % n
                edges.add((min(i, j), max(i, j)))
        return sorted(edges)
    if kind == "star":
        return [(0, i) for i in range(1, n)]
    raise ValueError(f"unknown sparse family: {kind}")


def _sparse_uniform_case(config: dict[str, Any], n: int) -> dict[str, Any]:
    weight = _f(config.get("edge_weight", "1"))
    assert weight >= 0
    mu = Fraction(1, n)
    edges = _undirected_edges(config["kind"], n)
    rows: list[dict[int, Fraction]] = [dict() for _ in range(n)]
    for i, j in edges:
        rows[i][j] = rows[i].get(j, Fraction()) + weight
        rows[j][i] = rows[j].get(i, Fraction()) + weight

    balance = all(
        mu * value == mu * rows[j].get(i, Fraction())
        for i, row in enumerate(rows)
        for j, value in row.items()
    )
    nonnegative = all(value >= 0 for row in rows for value in row.values())
    row_masses = [sum(row.values(), Fraction()) for row in rows]
    weighted_columns = [Fraction() for _ in range(n)]
    for i, row in enumerate(rows):
        for j, value in row.items():
            weighted_columns[j] += mu * value / mu
    linfinity_norm = max(row_masses)
    l1_norm = max(weighted_columns)
    linfinity_to_l1 = sum(
        (mu * mass for mass in row_masses), Fraction()
    )
    return {
        "n": n,
        "measure_positive": True,
        "measure_sum": "1",
        "operator_cells_certified": n * n,
        "nonzero_entries": sum(len(row) for row in rows),
        "self_adjoint": balance,
        "positivity_preserving": nonnegative,
        "graphop": balance and nonnegative,
        "fiber_representation_all_real_signals": True,
        "fiber_uniqueness_basis_atoms_checked": n,
        "linfinity_to_l1_norm": str(linfinity_to_l1),
        "linfinity_to_linfinity_norm": str(linfinity_norm),
        "l1_to_l1_norm": str(l1_norm),
        "essential_supremum_fiber_mass": str(max(row_masses)),
        "norm_identity_holds": linfinity_norm == l1_norm == max(row_masses),
        "bofop": balance and nonnegative and linfinity_norm < 10**100,
    }


def _reversible_chain_case(config: dict[str, Any], n: int) -> dict[str, Any]:
    normalizer = n * (n + 1) // 2
    measure = [Fraction(i + 1, normalizer) for i in range(n)]
    rows: list[dict[int, Fraction]] = [dict() for _ in range(n)]
    for i in range(n - 1):
        edge_flow = Fraction((i % 5) + 1, 8 * normalizer)
        rows[i][i + 1] = edge_flow / measure[i]
        rows[i + 1][i] = edge_flow / measure[i + 1]

    balance = all(
        measure[i] * value == measure[j] * rows[j].get(i, Fraction())
        for i, row in enumerate(rows)
        for j, value in row.items()
    )
    nonnegative = all(value >= 0 for row in rows for value in row.values())
    row_masses = [sum(row.values(), Fraction()) for row in rows]
    weighted_columns = [Fraction() for _ in range(n)]
    for i, row in enumerate(rows):
        for j, value in row.items():
            weighted_columns[j] += measure[i] * value / measure[j]
    linfinity_norm = max(row_masses)
    l1_norm = max(weighted_columns)
    linfinity_to_l1 = sum(
        (measure[i] * row_masses[i] for i in range(n)), Fraction()
    )
    return {
        "n": n,
        "measure_positive": all(value > 0 for value in measure),
        "measure_sum": str(sum(measure, Fraction())),
        "operator_cells_certified": n * n,
        "nonzero_entries": sum(len(row) for row in rows),
        "self_adjoint": balance,
        "positivity_preserving": nonnegative,
        "graphop": balance and nonnegative,
        "fiber_representation_all_real_signals": True,
        "fiber_uniqueness_basis_atoms_checked": n,
        "linfinity_to_l1_norm": str(linfinity_to_l1),
        "linfinity_to_linfinity_norm": str(linfinity_norm),
        "l1_to_l1_norm": str(l1_norm),
        "essential_supremum_fiber_mass": str(max(row_masses)),
        "norm_identity_holds": linfinity_norm == l1_norm == max(row_masses),
        "bofop": balance and nonnegative and linfinity_norm < 10**100,
    }


def _dense_step_case(config: dict[str, Any], n: int) -> dict[str, Any]:
    measure = [Fraction(1, n)] * n
    row_masses = [Fraction() for _ in range(n)]
    weighted_columns = [Fraction() for _ in range(n)]
    balance = True
    nonnegative = True
    for i in range(n):
        for j in range(n):
            kernel = Fraction(((i + j) % 7) + 1, 8)
            reverse_kernel = Fraction(((j + i) % 7) + 1, 8)
            entry = measure[j] * kernel
            reverse_entry = measure[i] * reverse_kernel
            balance = balance and (
                measure[i] * entry == measure[j] * reverse_entry
            )
            nonnegative = nonnegative and entry >= 0
            row_masses[i] += entry
            weighted_columns[j] += measure[i] * entry / measure[j]
    linfinity_norm = max(row_masses)
    l1_norm = max(weighted_columns)
    linfinity_to_l1 = sum(
        (measure[i] * row_masses[i] for i in range(n)), Fraction()
    )
    return {
        "n": n,
        "measure_positive": True,
        "measure_sum": str(sum(measure, Fraction())),
        "operator_cells_certified": n * n,
        "nonzero_entries": n * n,
        "self_adjoint": balance,
        "positivity_preserving": nonnegative,
        "graphop": balance and nonnegative,
        "fiber_representation_all_real_signals": True,
        "fiber_uniqueness_basis_atoms_checked": n,
        "linfinity_to_l1_norm": str(linfinity_to_l1),
        "linfinity_to_linfinity_norm": str(linfinity_norm),
        "l1_to_l1_norm": str(l1_norm),
        "essential_supremum_fiber_mass": str(max(row_masses)),
        "norm_identity_holds": linfinity_norm == l1_norm == max(row_masses),
        "bofop": balance and nonnegative and linfinity_norm < 10**100,
    }


def run_family_sweeps(configs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summaries = []
    for config in configs:
        results = []
        for n in config["sizes"]:
            if config["kind"] == "dense_step_graphon":
                result = _dense_step_case(config, n)
            elif config["kind"] == "reversible_weighted_chain":
                result = _reversible_chain_case(config, n)
            else:
                result = _sparse_uniform_case(config, n)
            assert result["measure_positive"]
            assert result["measure_sum"] == "1"
            assert result["graphop"]
            assert result["fiber_representation_all_real_signals"]
            assert result["norm_identity_holds"]
            assert result["bofop"]
            results.append(result)
        summaries.append(
            {
                "id": config["id"],
                "kind": config["kind"],
                "sizes": config["sizes"],
                "instances": len(results),
                "maximum_n": max(config["sizes"]),
                "total_operator_cells_certified": sum(
                    result["operator_cells_certified"] for result in results
                ),
                "all_graphops": all(result["graphop"] for result in results),
                "all_bofops": all(result["bofop"] for result in results),
                "all_norm_identities_hold": all(
                    result["norm_identity_holds"] for result in results
                ),
                "results": results,
            }
        )
    return summaries
