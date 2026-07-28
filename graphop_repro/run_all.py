"""Fixed cumulative reproduction command.

Every experiment node runs this module.  Children add claim modules and
artifacts, while the command and environment remain unchanged.
"""

from __future__ import annotations

import json
import os
import platform
import resource
import subprocess
import time
from pathlib import Path

from graphop_repro.claims.claim1_graphops import verify as verify_claim_1
from graphop_repro.claims.claim2_bofops import verify as verify_claim_2
from graphop_repro.claims.claim3_uniform_lipschitz import verify as verify_claim_3
from graphop_repro.claims.claim4_didm_counterexample import verify as verify_claim_4
from graphop_repro.claims.claim5_universal_approximation import verify as verify_claim_5
from graphop_repro.independent.claim1_checker import check as check_claim_1
from graphop_repro.independent.claim2_checker import check as check_claim_2
from graphop_repro.independent.claim3_checker import check as check_claim_3
from graphop_repro.independent.claim4_checker import check as check_claim_4
from graphop_repro.independent.claim5_checker import check as check_claim_5


ROOT = Path(__file__).resolve().parents[1]


def _git_sha() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def main() -> int:
    started = time.perf_counter()
    cpu_started = time.process_time()
    raw_path = ROOT / ".openresearch/artifacts/claim_1/raw_results.json"
    primary = verify_claim_1(raw_path)
    independent = check_claim_1(raw_path)
    raw_path_2 = ROOT / ".openresearch/artifacts/claim_2/raw_results.json"
    primary_2 = verify_claim_2(raw_path_2)
    independent_2 = check_claim_2(raw_path_2)
    raw_path_3 = ROOT / ".openresearch/artifacts/claim_3/raw_results.json"
    primary_3 = verify_claim_3(raw_path_3)
    independent_3 = check_claim_3(raw_path_3)
    raw_path_4 = ROOT / ".openresearch/artifacts/claim_4/raw_results.json"
    primary_4 = verify_claim_4(raw_path_4)
    independent_4 = check_claim_4(raw_path_4)
    raw_path_5 = ROOT / ".openresearch/artifacts/claim_5/raw_results.json"
    primary_5 = verify_claim_5(raw_path_5)
    independent_5 = check_claim_5(raw_path_5)

    expected_checker = json.loads(
        (ROOT / ".openresearch/artifacts/claim_1/checker_output.json").read_text(
            encoding="utf-8"
        )
    )
    assert independent == expected_checker
    expected_checker_2 = json.loads(
        (ROOT / ".openresearch/artifacts/claim_2/checker_output.json").read_text(
            encoding="utf-8"
        )
    )
    assert independent_2 == expected_checker_2
    expected_checker_3 = json.loads(
        (ROOT / ".openresearch/artifacts/claim_3/checker_output.json").read_text(
            encoding="utf-8"
        )
    )
    assert independent_3 == expected_checker_3
    expected_control_3 = json.loads(
        (
            ROOT / ".openresearch/artifacts/claim_3/negative_control_output.json"
        ).read_text(encoding="utf-8")
    )
    assert primary_3["negative_control"] == expected_control_3
    expected_checker_4 = json.loads(
        (ROOT / ".openresearch/artifacts/claim_4/checker_output.json").read_text(
            encoding="utf-8"
        )
    )
    assert independent_4 == expected_checker_4
    expected_control_4 = json.loads(
        (
            ROOT / ".openresearch/artifacts/claim_4/negative_control_output.json"
        ).read_text(encoding="utf-8")
    )
    assert primary_4["negative_control"] == expected_control_4
    expected_checker_5 = json.loads(
        (ROOT / ".openresearch/artifacts/claim_5/checker_output.json").read_text(
            encoding="utf-8"
        )
    )
    assert independent_5 == expected_checker_5
    expected_control_5 = json.loads(
        (ROOT / ".openresearch/artifacts/claim_5/negative_control_output.json").read_text(
            encoding="utf-8"
        )
    )
    assert primary_5["negative_control"] == expected_control_5

    wall_seconds = time.perf_counter() - started
    cpu_seconds = time.process_time() - cpu_started
    usage = resource.getrusage(resource.RUSAGE_SELF)
    summary = {
        "schema_version": 1,
        "paper": "arXiv:2602.08785v1",
        "git_sha": _git_sha(),
        "fixed_command": "uv run --frozen python -m graphop_repro.run_all",
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "uv_lock_present": (ROOT / "uv.lock").is_file(),
        },
        "compute": {
            "backend": os.environ.get("ORX_BACKEND", "local (reported by run contract)"),
            "estimated_cores": 1,
            "implementation_max_threads": 1,
            "host_logical_cpus": os.cpu_count(),
            "actual_allocation_note": (
                "Local backend is not cgroup-limited; verifier is single-threaded."
            ),
            "wall_seconds": round(wall_seconds, 6),
            "process_cpu_seconds": round(cpu_seconds, 6),
            "max_rss_platform_units": usage.ru_maxrss,
        },
        "claims": [
            {
                "claim": 1,
                "status": primary["status"],
                "primary": primary,
                "independent": independent,
            },
            {
                "claim": 2,
                "status": primary_2["status"],
                "primary": primary_2,
                "independent": independent_2,
            },
            {
                "claim": 3,
                "status": primary_3["status"],
                "primary": primary_3,
                "independent": independent_3,
            },
            {
                "claim": 4,
                "status": primary_4["status"],
                "primary": primary_4,
                "independent": independent_4,
            },
            {
                "claim": 5,
                "status": primary_5["status"],
                "primary": primary_5,
                "independent": independent_5,
            },
        ],
        "all_claims_accepted": (
            primary["status"] == "VERIFIED"
            and primary_2["status"] == "VERIFIED"
            and primary_3["status"] == "FALSIFIED"
            and primary_4["status"] == "FALSIFIED"
            and primary_5["status"] == "VERIFIED"
        ),
    }
    print("BEGIN_REPRODUCTION_SUMMARY")
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("END_REPRODUCTION_SUMMARY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
