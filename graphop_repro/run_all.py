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
from graphop_repro.independent.claim1_checker import check as check_claim_1


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

    expected_checker = json.loads(
        (ROOT / ".openresearch/artifacts/claim_1/checker_output.json").read_text(
            encoding="utf-8"
        )
    )
    assert independent == expected_checker

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
            }
        ],
        "all_claims_accepted": primary["status"] == "VERIFIED",
    }
    print("BEGIN_REPRODUCTION_SUMMARY")
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("END_REPRODUCTION_SUMMARY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

