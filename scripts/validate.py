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


def check_product_mvp_ui_quality_gate() -> None:
    required_pairs = [
        ("SKILL.md", "Product MVP UI Quality Gate"),
        ("SKILL.md", "MVP scope may be small, but UI/UX/design system quality is not optional"),
        ("SKILL.md", "Design Read"),
        ("SKILL.md", "do not apply landing-page taste rules blindly to dashboards, admin panels, data tables, or multi-step product UI"),
        ("references/frontend.md", "Product MVP UI Quality Gate"),
        ("references/frontend.md", "Design Read"),
        ("references/frontend.md", "Design Dials"),
        ("references/frontend.md", "State And Interaction Contract"),
        ("references/frontend.md", "Anti-Slop Guardrails"),
        ("references/frontend.md", "Browser UI Quality Verification"),
        ("references/workflow-checklists.md", "Product MVP UI quality checked"),
        ("references/workflow-checklists.md", "UI Quality Gate Prompt"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Design Read"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Design Dials"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Product MVP UI Quality Gate"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "State And Interaction Contract"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Anti-Slop Preflight"),
        ("templates/AGENTS.md", "Product MVP UI Quality Gate"),
        ("templates/AGENTS.md", "Design Read"),
        ("templates/AGENTS.md", "anti-slop guardrails"),
        ("README.md", "Product MVP UI Quality Gate"),
        ("README.md", "Design Read"),
        ("README.md", "anti-slop"),
        ("README.zh-CN.md", "Product MVP UI 质量门禁"),
        ("README.zh-CN.md", "设计判断"),
        ("README.zh-CN.md", "反模板"),
        ("examples/tiny-webapp/README.md", "Product MVP UI quality gate"),
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
        ("SKILL.md", "Reference Project Scan Gate"),
        ("SKILL.md", "project name, direct link"),
        ("SKILL.md", "Do not continue to project purpose confirmation"),
        ("SKILL.md", "Capability Library Scan Gate"),
        ("SKILL.md", "capability, library name, direct link"),
        ("SKILL.md", "Do not confirm a technology stack"),
        ("SKILL.md", "Goal Contract"),
        ("SKILL.md", "Target outcome"),
        ("SKILL.md", "Completion signal"),
        ("SKILL.md", "Confirmation Prompt Rule"),
        ("SKILL.md", "User Language Rule"),
        ("SKILL.md", "Any task that asks for user confirmation"),
        ("SKILL.md", "match the user's current language"),
        ("SKILL.md", "Project Specification Readiness Gate"),
        ("SKILL.md", "Source-of-Truth Change Gate"),
        ("SKILL.md", "Never create application scaffolding"),
        ("SKILL.md", "frontend engineering contract"),
        ("SKILL.md", "component split rules"),
        ("SKILL.md", "in the user's current language"),
        ("SKILL.md", "🎉 恭喜，项目工程基线已就绪"),
        ("SKILL.md", "🎉 Project engineering baseline is ready"),
        ("SKILL.md", "First MVP slice accepted with evidence"),
        ("SKILL.md", "🎉 恭喜，首个 MVP 切片已完成"),
        ("SKILL.md", "🎉 First MVP slice is complete"),
        ("SKILL.md", "Steady path"),
        ("SKILL.md", "Accelerated path"),
        ("SKILL.md", "named missing batch"),
        ("SKILL.md", "plain-text options"),
        ("SKILL.md", "Do not depend on UI buttons"),
        ("SKILL.md", "After creating or updating any readiness document"),
        ("SKILL.md", "ambiguous domain nouns"),
        ("SKILL.md", "Do not move into technology stack, frontend, backend, database, or implementation planning until the user confirms"),
        ("references/project-initiation.md", "Project Purpose Confirmation"),
        ("references/project-initiation.md", "Requirements Depth Gate"),
        ("references/project-initiation.md", "Reference Project Scan"),
        ("references/project-initiation.md", "direct project links"),
        ("references/project-initiation.md", "user chooses a direction"),
        ("references/project-initiation.md", "Implementation Readiness Audit"),
        ("references/project-initiation.md", "Confirmation Prompt Rule"),
        ("references/project-initiation.md", "User Language Rule"),
        ("references/project-initiation.md", "Do not create `apps/`, `packages/`, UI screens, API controllers, database schemas"),
        ("references/project-initiation.md", "unpack the core nouns"),
        ("references/project-initiation.md", "No project document file should be created or updated until the user explicitly agrees"),
        ("references/project-initiation.md", "Summarize the project purpose"),
        ("references/project-initiation.md", "Do not choose a technology stack or plan implementation until the user confirms"),
        ("references/project-initiation.md", "current stage"),
        ("references/project-initiation.md", "first MVP slice"),
        ("references/project-initiation.md", "named missing batch"),
        ("references/project-initiation.md", "plain-text options"),
        ("references/project-initiation.md", "Do not depend on UI buttons"),
        ("references/architecture-baseline.md", "Technology selection starts only after the project purpose and charter facts are confirmed"),
        ("references/architecture-baseline.md", "Capability Library Scan Gate"),
        ("references/architecture-baseline.md", "capability, library name, direct link"),
        ("references/architecture-baseline.md", "maintenance evidence"),
        ("references/architecture-baseline.md", "Before writing `docs/architecture/TECH_STACK.md`, ask for consent"),
        ("references/architecture-baseline.md", "A confirmed technology stack is not permission to scaffold or implement"),
        ("references/engineering-baseline.md", "An engineering baseline is necessary but not sufficient for implementation"),
        ("references/workflow-checklists.md", "Goal And Completion Signal"),
        ("references/workflow-checklists.md", "Reference project scan completed"),
        ("references/workflow-checklists.md", "concrete project links"),
        ("references/workflow-checklists.md", "Capability library scan completed"),
        ("references/workflow-checklists.md", "required technical capability"),
        ("references/workflow-checklists.md", "Goal Contract Prompt"),
        ("references/workflow-checklists.md", "Confirmation Prompt Rule"),
        ("references/workflow-checklists.md", "User Language Rule"),
        ("references/workflow-checklists.md", "language-adaptive first MVP slice message"),
        ("references/workflow-checklists.md", "Implementation Readiness Gate"),
        ("references/workflow-checklists.md", "Source-of-Truth Change Gate"),
        ("references/workflow-checklists.md", "Source-of-Truth Change Prompt"),
        ("references/workflow-checklists.md", "Project scaffold or implementation only after readiness passes"),
        ("references/workflow-checklists.md", "in the user's current language"),
        ("references/workflow-checklists.md", "🎉 恭喜，项目工程基线已就绪"),
        ("references/workflow-checklists.md", "🎉 Project engineering baseline is ready"),
        ("references/workflow-checklists.md", "First MVP slice implementation and verification"),
        ("references/workflow-checklists.md", "🎉 恭喜，首个 MVP 切片已完成"),
        ("references/workflow-checklists.md", "🎉 First MVP slice is complete"),
        ("references/workflow-checklists.md", "stage-aware readiness audit"),
        ("references/workflow-checklists.md", "plain-text options"),
        ("references/workflow-checklists.md", "Do not depend on UI buttons"),
        ("references/engineering-rules.md", "Source-of-truth change gate"),
        ("references/frontend.md", "Project Specification Readiness Gate"),
        ("references/frontend.md", "update `docs/architecture/FRONTEND_PLAN.md` before editing frontend code"),
        ("references/frontend.md", "Frontend Engineering Structure"),
        ("references/frontend.md", "File Responsibility Rules"),
        ("references/frontend.md", "Component Split Rules"),
        ("references/frontend.md", "Import Boundary Rules"),
        ("references/frontend.md", "First MVP Page Acceptance"),
        ("references/frontend.md", "first MVP slice"),
        ("references/database.md", "Do not create schemas, migrations, seeds, or ORM files"),
        ("references/database.md", "update `docs/architecture/DATABASE_DESIGN.md` before writing the database code"),
        ("references/backend.md", "Do not build even a minimal backend skeleton"),
        ("references/backend.md", "update `docs/architecture/BACKEND_SPEC.md` before editing backend code"),
        ("README.md", "Goal And Completion Signal"),
        ("README.md", "Reference project scan gate"),
        ("README.md", "direct project links"),
        ("README.md", "Capability library scan gate"),
        ("README.md", "project-needed third-party libraries"),
        ("README.md", "first MVP slice accepted"),
        ("README.md", "Source-of-Truth Change Gate"),
        ("README.md", "user's current language"),
        ("README.md", "language-adaptive completion messages"),
        ("README.md", "confirmation prompts"),
        ("README.md", "match the user's current language"),
        ("README.md", "accelerated path"),
        ("README.md", "plain-text options"),
        ("README.md", "🎉 Project engineering baseline is ready"),
        ("README.md", "🎉 First MVP slice is complete"),
        ("README.zh-CN.md", "目标与完成信号"),
        ("README.zh-CN.md", "参考项目扫描门禁"),
        ("README.zh-CN.md", "具体项目链接"),
        ("README.zh-CN.md", "能力库扫描门禁"),
        ("README.zh-CN.md", "项目需要的第三方库"),
        ("README.zh-CN.md", "真源文档变更门禁"),
        ("README.zh-CN.md", "用户当前语言"),
        ("README.zh-CN.md", "语言自适应完成提示"),
        ("README.zh-CN.md", "确认类提示"),
        ("README.zh-CN.md", "匹配用户当前语言"),
        ("README.zh-CN.md", "快速推进"),
        ("README.zh-CN.md", "文字选项"),
        ("README.zh-CN.md", "🎉 恭喜，项目工程基线已就绪"),
        ("README.zh-CN.md", "首个 MVP 切片"),
        ("README.zh-CN.md", "🎉 恭喜，首个 MVP 切片已完成"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Document Status"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Reference Project Scan"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Direct link"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Purpose Confirmation"),
        ("templates/docs/project/PROJECT_CHARTER.md", "First MVP Slice"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Domain Model"),
        ("templates/docs/project/PROJECT_CHARTER.md", "Operations And States"),
        ("templates/docs/architecture/TECH_STACK.md", "Decision Status"),
        ("templates/docs/architecture/TECH_STACK.md", "Selection Context"),
        ("templates/docs/architecture/TECH_STACK.md", "Capability Library Scan"),
        ("templates/docs/architecture/TECH_STACK.md", "Maintenance evidence"),
        ("templates/AGENTS.md", "Update the relevant source-of-truth document before code"),
        ("templates/AGENTS.md", "Confirmation Prompt Rule"),
        ("templates/AGENTS.md", "User Language Rule"),
        ("templates/AGENTS.md", "Accelerated path"),
        ("templates/AGENTS.md", "named missing batch"),
        ("templates/AGENTS.md", "plain-text options"),
        ("templates/AGENTS.md", "frontend engineering contract"),
        ("templates/AGENTS.md", "component split rules"),
        ("templates/docs/workflow/AI_WORKFLOW.md", "docs evidence must come before code evidence"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "First MVP Page"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Related first MVP slice"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Frontend Source Tree"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "File Boundary Contract"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Component Split Rules"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Import Boundaries"),
        ("templates/docs/architecture/FRONTEND_PLAN.md", "Change Rule"),
        ("templates/docs/architecture/DATABASE_DESIGN.md", "Change Rule"),
        ("templates/docs/architecture/BACKEND_SPEC.md", "Change Rule"),
        ("examples/tiny-webapp/README.md", "first MVP slice accepted"),
        ("examples/tiny-webapp/README.md", "Reference project scan"),
        ("examples/tiny-webapp/README.md", "direct project links"),
        ("examples/tiny-webapp/README.md", "Capability library scan"),
        ("examples/tiny-webapp/README.md", "project-needed third-party libraries"),
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
    check_product_mvp_ui_quality_gate()
    check_workflow_priority_and_confirmation()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
