#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "scripts/install.sh",
    "examples/tiny-webapp/README.md",
    "templates/AGENTS.md",
    "templates/docs/project/PROJECT_CHARTER.md",
    "templates/docs/architecture/TECH_STACK.md",
    "templates/docs/architecture/ENGINEERING_BASELINE.md",
    "templates/docs/architecture/FRONTEND_PLAN.md",
    "templates/docs/architecture/DATABASE_DESIGN.md",
    "templates/docs/architecture/BACKEND_SPEC.md",
    "templates/docs/workflow/AI_WORKFLOW.md",
    "templates/docs/ops/TOOL_POLICY.md",
    "templates/docs/ops/DEPLOYMENT.md",
]

REQUIRED_RUNTIME_REFERENCES = [
    "references/document-layout.md",
    "references/architecture-baseline.md",
    "references/engineering-baseline.md",
    "references/project-initiation.md",
    "references/engineering-rules.md",
    "references/frontend.md",
    "references/database.md",
    "references/backend.md",
    "references/security.md",
    "references/tool-policy.md",
    "references/workflow-checklists.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_files() -> None:
    for path in REQUIRED_FILES + REQUIRED_RUNTIME_REFERENCES:
        if not (ROOT / path).is_file():
            fail(f"missing required file: {path}")


def check_skill_frontmatter() -> None:
    text = read("SKILL.md")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = match.group(1)
    if "name: agent-project-kit" not in frontmatter:
        fail("SKILL.md frontmatter must use name: agent-project-kit")
    if not re.search(r"^description: Use when ", frontmatter, re.M):
        fail('SKILL.md description must start with "Use when"')


def check_readme_language_switch() -> None:
    readme_en = read("README.md")
    readme_zh = read("README.zh-CN.md")
    if "README.zh-CN.md" not in readme_en:
        fail("README.md must link to README.zh-CN.md")
    if "README.md" not in readme_zh:
        fail("README.zh-CN.md must link to README.md")
    if "$agent-project-kit" not in readme_en or "$agent-project-kit" not in readme_zh:
        fail("both README files must show the skill invocation name")


def check_markdown_fences() -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        count = path.read_text(encoding="utf-8").count("```")
        if count % 2:
            fail(f"unbalanced fenced code block in {path.relative_to(ROOT)}")


def check_reference_links() -> None:
    skill = read("SKILL.md")
    for path in REQUIRED_RUNTIME_REFERENCES:
        if path not in skill:
            fail(f"SKILL.md does not route to {path}")


def check_guided_interaction() -> None:
    skill = read("SKILL.md")
    initiation = read("references/project-initiation.md")
    required_phrases = [
        "Guided Interaction",
        "Ask one question at a time",
        "Do not present a full intake questionnaire",
    ]
    for phrase in required_phrases:
        if phrase not in skill and phrase not in initiation:
            fail(f"missing guided interaction rule: {phrase}")


def check_project_document_layout() -> None:
    for path in sorted((ROOT / "templates").glob("*.md")):
        if path.name != "AGENTS.md":
            fail(f"project document template must live under templates/docs/: {path.relative_to(ROOT)}")

    agents = read("templates/AGENTS.md")
    required_doc_paths = [
        "docs/project/PROJECT_CHARTER.md",
        "docs/architecture/TECH_STACK.md",
        "docs/architecture/ENGINEERING_BASELINE.md",
        "docs/workflow/AI_WORKFLOW.md",
        "docs/ops/TOOL_POLICY.md",
    ]
    for path in required_doc_paths:
        if path not in agents:
            fail(f"templates/AGENTS.md must index {path}")


def check_product_mvp_baseline() -> None:
    required_pairs = [
        ("references/architecture-baseline.md", "Product MVP"),
        ("references/engineering-baseline.md", "Required Scripts"),
        ("templates/docs/architecture/TECH_STACK.md", "Production Compatibility"),
        ("templates/docs/architecture/ENGINEERING_BASELINE.md", "Required Scripts"),
    ]
    for path, phrase in required_pairs:
        if phrase not in read(path):
            fail(f"{path} must include {phrase}")


def check_workflow_priority_and_confirmation() -> None:
    required_pairs = [
        ("SKILL.md", "Default Workflow Priority"),
        ("SKILL.md", "Agent Project Kit is the default primary workflow"),
        ("SKILL.md", "overlapping skills"),
        ("SKILL.md", "Project Purpose Confirmation"),
        ("SKILL.md", "Document Consent Gate"),
        ("SKILL.md", "Requirements Depth Gate"),
        ("SKILL.md", "Goal Contract"),
        ("SKILL.md", "Target outcome"),
        ("SKILL.md", "Completion signal"),
        ("SKILL.md", "Project Specification Readiness Gate"),
        ("SKILL.md", "Never create application scaffolding"),
        ("SKILL.md", "🎉 恭喜，项目工程基线已就绪"),
        ("SKILL.md", "🚀 下一步可以从第一个已批准的产品闭环开始实现"),
        ("SKILL.md", "ambiguous domain nouns"),
        ("SKILL.md", "Do not move into technology stack, frontend, backend, database, or implementation planning until the user confirms"),
        ("references/project-initiation.md", "Project Purpose Confirmation"),
        ("references/project-initiation.md", "Requirements Depth Gate"),
        ("references/project-initiation.md", "Implementation Readiness Audit"),
        ("references/project-initiation.md", "Do not create `apps/`, `packages/`, UI screens, API controllers, database schemas"),
        ("references/project-initiation.md", "unpack the core nouns"),
        ("references/project-initiation.md", "No project document file should be created or updated until the user explicitly agrees"),
        ("references/project-initiation.md", "Summarize the project purpose"),
        ("references/project-initiation.md", "Do not choose a technology stack or plan implementation until the user confirms"),
        ("references/architecture-baseline.md", "Technology selection starts only after the project purpose and charter facts are confirmed"),
        ("references/architecture-baseline.md", "Before writing `docs/architecture/TECH_STACK.md`, ask for consent"),
        ("references/architecture-baseline.md", "A confirmed technology stack is not permission to scaffold or implement"),
        ("references/engineering-baseline.md", "An engineering baseline is necessary but not sufficient for implementation"),
        ("references/workflow-checklists.md", "Goal And Completion Signal"),
        ("references/workflow-checklists.md", "Goal Contract Prompt"),
        ("references/workflow-checklists.md", "Implementation Readiness Gate"),
        ("references/workflow-checklists.md", "Project scaffold or implementation only after readiness passes"),
        ("references/workflow-checklists.md", "🎉 恭喜，项目工程基线已就绪"),
        ("references/workflow-checklists.md", "✅ 项目目标、技术路线、核心文档和实现前门禁已经到位"),
        ("references/frontend.md", "Project Specification Readiness Gate"),
        ("references/database.md", "Do not create schemas, migrations, seeds, or ORM files"),
        ("references/backend.md", "Do not build even a minimal backend skeleton"),
        ("README.md", "Goal And Completion Signal"),
        ("README.md", "project engineering baseline ready"),
        ("README.zh-CN.md", "目标与完成信号"),
        ("README.zh-CN.md", "🎉 恭喜，项目工程基线已就绪"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Document Status"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Purpose Confirmation"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Domain Model"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Operations And States"),
        ("templates/docs/architecture/TECH_STACK.md", "Decision Status"),
        ("templates/docs/architecture/TECH_STACK.md", "Selection Context"),
    ]
    for path, phrase in required_pairs:
        if phrase not in read(path):
            fail(f"{path} must include {phrase}")

    overfit_phrases = [
        "For AI-tool management",
        "For AI tool management",
    ]
    checked = read("SKILL.md") + "\n" + read("references/project-initiation.md")
    for phrase in overfit_phrases:
        if phrase in checked:
            fail(f"project initiation flow is overfit to one domain: {phrase}")


def main() -> None:
    require_files()
    check_skill_frontmatter()
    check_readme_language_switch()
    check_markdown_fences()
    check_reference_links()
    check_guided_interaction()
    check_project_document_layout()
    check_product_mvp_baseline()
    check_workflow_priority_and_confirmation()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
