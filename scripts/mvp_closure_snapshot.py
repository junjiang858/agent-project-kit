#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DOC_PATHS = [
    "AGENTS.md",
    "docs/project/PROJECT_CHARTER.md",
    "docs/architecture/TECH_STACK.md",
    "docs/architecture/ENGINEERING_BASELINE.md",
    "docs/architecture/FRONTEND_PLAN.md",
    "docs/architecture/DATABASE_DESIGN.md",
    "docs/architecture/BACKEND_SPEC.md",
    "docs/workflow/AI_WORKFLOW.md",
    "docs/ops/TOOL_POLICY.md",
    "docs/ops/DEPLOYMENT.md",
]

LOCKFILES = [
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "bun.lock",
    "bun.lockb",
    "poetry.lock",
    "uv.lock",
    "requirements.txt",
]

SIGNAL_RE = re.compile(
    r"\b("
    r"MVP|must[- ]?have|acceptance|criteria|risk|release|deploy|verification|"
    r"evidence|non[- ]?goal|scope|workflow|quality|security|rollback|"
    r"done|complete|blocker|production"
    r")\b",
    re.I,
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def run_git(root: Path, args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except FileNotFoundError:
        return ""
    if result.returncode:
        return ""
    return result.stdout.strip()


def file_hash(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def checkbox_summary(text: str) -> dict[str, int]:
    return {
        "checked": len(re.findall(r"^\s*[-*]\s+\[[xX]\]", text, re.M)),
        "unchecked": len(re.findall(r"^\s*[-*]\s+\[\s\]", text, re.M)),
    }


def signal_lines(text: str, limit: int = 12) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or len(line) > 220:
            continue
        if SIGNAL_RE.search(line):
            lines.append(line)
        if len(lines) >= limit:
            break
    return lines


def collect_snapshot(root: Path) -> dict[str, Any]:
    docs: dict[str, Any] = {}
    hash_inputs: list[str] = []

    for rel in DOC_PATHS:
        path = root / rel
        if not path.is_file():
            docs[rel] = {"present": False}
            hash_inputs.append(f"{rel}:missing")
            continue
        text = read_text(path)
        digest = file_hash(path)
        docs[rel] = {
            "present": True,
            "sha256": digest,
            "checkboxes": checkbox_summary(text),
            "signals": signal_lines(text),
        }
        hash_inputs.append(f"{rel}:{digest}")

    locks: dict[str, str] = {}
    for rel in LOCKFILES:
        path = root / rel
        if path.is_file():
            digest = file_hash(path)
            locks[rel] = digest
            hash_inputs.append(f"{rel}:{digest}")

    git_head = run_git(root, ["rev-parse", "HEAD"])
    git_status = run_git(root, ["status", "--short"])
    git_diff = run_git(root, ["diff", "--binary"])
    dirty_hash = sha256_bytes(git_diff.encode("utf-8")) if git_diff else ""
    hash_inputs.extend(
        [
            f"git_head:{git_head}",
            f"git_status:{git_status}",
            f"dirty_hash:{dirty_hash}",
        ]
    )

    cache_key = sha256_bytes("\n".join(hash_inputs).encode("utf-8"))
    required_missing = [
        rel
        for rel in [
            "AGENTS.md",
            "docs/project/PROJECT_CHARTER.md",
            "docs/architecture/TECH_STACK.md",
            "docs/architecture/ENGINEERING_BASELINE.md",
            "docs/workflow/AI_WORKFLOW.md",
            "docs/ops/TOOL_POLICY.md",
        ]
        if not docs.get(rel, {}).get("present")
    ]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project_root": str(root),
        "cache_key": cache_key,
        "git": {
            "head": git_head,
            "dirty": bool(git_status),
            "dirty_hash": dirty_hash,
        },
        "documents": docs,
        "lockfiles": locks,
        "fast_gate": {
            "required_baseline_missing": required_missing,
            "agent_review_required": True,
            "note": "This script creates a cacheable evidence snapshot. Use references/mvp-closure.md for the lifecycle-state decision.",
        },
    }


def render_markdown(snapshot: dict[str, Any]) -> str:
    docs: dict[str, Any] = snapshot["documents"]
    lines = [
        "# MVP Closure Snapshot",
        "",
        f"- Generated: `{snapshot['generated_at']}`",
        f"- Cache key: `{snapshot['cache_key']}`",
        f"- Git head: `{snapshot['git']['head'] or 'unknown'}`",
        f"- Dirty worktree: `{snapshot['git']['dirty']}`",
        "",
        "This is a cacheable evidence snapshot, not the final lifecycle-state decision. Use `references/mvp-closure.md` for the audit.",
        "",
        "## Document Inputs",
        "",
        "| Document | Present | Checkboxes | Signals |",
        "| --- | --- | --- | --- |",
    ]

    for rel, info in docs.items():
        if not info.get("present"):
            lines.append(f"| `{rel}` | no |  |  |")
            continue
        boxes = info["checkboxes"]
        signals = "<br>".join(info["signals"][:4]).replace("|", "\\|")
        lines.append(
            f"| `{rel}` | yes | {boxes['checked']} checked, {boxes['unchecked']} unchecked | {signals} |"
        )

    missing = snapshot["fast_gate"]["required_baseline_missing"]
    lines.extend(["", "## Fast Gate", ""])
    if missing:
        lines.append("Required baseline documents are missing:")
        lines.extend(f"- `{rel}`" for rel in missing)
    else:
        lines.append("Required baseline documents are present. Agent review is still required for MVP closure.")

    lines.extend(
        [
            "",
            "## Next Agent Step",
            "",
            "Run the MVP closure audit from `references/mvp-closure.md` when the user asks whether the MVP is complete, what remains, whether release is safe, or when claiming Full MVP Scope Complete or Release Ready.",
            "",
        ]
    )
    return "\n".join(lines)


def write_outputs(root: Path, snapshot: dict[str, Any]) -> None:
    cache_dir = root / ".agent-project-kit" / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / "mvp-closure.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    artifact_dir = root / "docs" / "agent-project-kit"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "mvp-closure-status.md").write_text(
        render_markdown(snapshot),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a cacheable MVP closure evidence snapshot.")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root to inspect. Defaults to the current directory.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write .agent-project-kit/cache/mvp-closure.json and docs/agent-project-kit/mvp-closure-status.md.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print JSON instead of Markdown.",
    )
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    snapshot = collect_snapshot(root)
    if args.write:
        write_outputs(root, snapshot)

    if args.json:
        print(json.dumps(snapshot, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(snapshot))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
