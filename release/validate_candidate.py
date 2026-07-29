"""Evaluator-visible release checks for a fully materialized Space tree."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SECRET = re.compile(
    r"(BEGIN (?:RSA |OPENSSH )?PRIVATE KEY|"
    r"(?:hf|api|access|secret)[_-]?token\s*[:=]\s*[^\s\"']+)",
    re.IGNORECASE,
)


def text_files(root: Path) -> list[Path]:
    files = [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() not in {".png", ".jpg", ".jpeg"}
    ]
    for path in files:
        path.read_text(encoding="utf-8")
    return files


def walk_navigation(node: dict, root: Path, opened: list[str]) -> None:
    page = root / node["file"]
    assert page.is_file(), f"missing navigation page: {node['file']}"
    opened.append(node["file"])
    for child in node.get("children", []):
        walk_navigation(child, root, opened)


def local_links(root: Path, path: Path) -> tuple[list[str], list[Path]]:
    missing: list[str] = []
    found: list[Path] = []
    for target in LINK.findall(path.read_text(encoding="utf-8")):
        target = target.strip().split("#", 1)[0]
        if (
            not target
            or target.startswith(("http://", "https://", "mailto:"))
            or target.startswith("#/")
        ):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
            missing.append(f"{path.relative_to(root)} -> {target}")
        else:
            found.append(resolved)
    return missing, found


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: validate_candidate.py FULL_CANDIDATE JUDGED_TREE")
    root = Path(sys.argv[1]).resolve()
    judged = Path(sys.argv[2]).resolve()
    files = text_files(root)

    logbook = json.loads((root / "logbook.json").read_text(encoding="utf-8"))
    assert logbook["space_id"] == "DineshAI/tRsnpaRO0m"
    assert logbook["root"]["file"] == "pages/current/index.md"

    opened = ["README.md", "logbook.json"]
    walk_navigation(logbook["root"], root, opened)
    assert opened[:3] == ["README.md", "logbook.json", "pages/current/index.md"]
    assert "pages/index.md" in opened
    assert "pages/overview/page.md" in opened

    historical = next(
        node
        for node in logbook["root"]["children"]
        if node["slug"] == "historical-rejected-baseline"
    )
    assert historical["title"] == "Historical rejected baseline"

    index = (root / "pages/current/index.md").read_text(encoding="utf-8")
    for claim in range(1, 7):
        page = root / f"pages/claims/claim-{claim}.md"
        body = page.read_text(encoding="utf-8")
        for required in (
            "Verdict:",
            "Reproduce",
            "Raw",
            "checker",
            "control",
            "Provenance",
            "Scientific Git SHA",
            "Compute:",
            "Runtime:",
            "Seeds:",
            "Environment:",
            "Visibility matrix",
        ):
            assert required.lower() in body.lower(), (
                f"claim {claim} missing {required}"
            )
        assert f"| {claim} |" in index

    assert (root / "graphop_repro/run_all.py").is_file()
    assert (root / "pyproject.toml").is_file()
    assert (root / "uv.lock").is_file()

    missing_links: list[str] = []
    visited = set(opened)
    queue = [root / relative for relative in opened]
    while queue:
        path = queue.pop(0)
        if path.suffix == ".md" or path.name == "README.md":
            missing, links = local_links(root, path)
            missing_links.extend(missing)
            for linked in links:
                relative = linked.relative_to(root).as_posix()
                if relative not in visited:
                    visited.add(relative)
                    opened.append(relative)
                    if linked.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
                        linked.read_text(encoding="utf-8")
                    if linked.suffix == ".md" or linked.name == "README.md":
                        queue.append(linked)
    assert not missing_links, "broken canonical links:\n" + "\n".join(missing_links)

    old_paths = {
        path.relative_to(judged).as_posix()
        for path in judged.rglob("*")
        if path.is_file()
        and ".git/" not in path.as_posix()
        and ".cache/" not in path.as_posix()
    }
    new_paths = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file()
        and ".git/" not in path.as_posix()
        and ".cache/" not in path.as_posix()
    }
    missing_old = sorted(old_paths - new_paths)
    assert not missing_old, "historical paths missing:\n" + "\n".join(missing_old)

    for path in files:
        content = path.read_text(encoding="utf-8")
        assert not SECRET.search(content), f"possible secret in {path.relative_to(root)}"

    digest = hashlib.sha256(
        "\n".join(sorted(opened)).encode("utf-8")
    ).hexdigest()
    print(
        json.dumps(
            {
                "status": "PASS",
                "canonical_files_opened": opened,
                "canonical_file_count": len(opened),
                "candidate_text_file_count": len(files),
                "historical_file_count": len(old_paths),
                "historical_subset": True,
                "broken_links": [],
                "secret_scan": "PASS",
                "navigation_digest": digest,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
