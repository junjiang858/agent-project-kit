# Agent Project Kit

[English](README.md) | [简体中文](README.zh-CN.md)

Agent Project Kit 是一个面向 Codex 的 skill，用来把 AI 编程项目从模糊想法推进到有证据的交付。

它把“直接让 AI 写代码”改造成一套阶段化流程：先澄清项目、选择技术栈、建立 Agent 规则，再规划前端/后端/数据库、定义工具权限，并在完成前要求测试、构建、接口、安全等验收证据。

默认姿态是 Product MVP：功能范围可以小，但仓库形态、技术栈决策和工程基线不能是后续必然推倒重来的临时方案。

## 适合谁

- 正在用 Codex、Claude Code、Cursor、Copilot 等 AI 编程工具的个人开发者和小团队。
- 希望借助 AI 提速，但不希望项目漂移成一堆难验收代码的人。
- 需要轻量流程，而不是完整项目管理平台的项目。

## 它不是什么

- 不是自动分析代码库的 CLI。
- 不是项目管理系统。
- 不是普通提示词合集。
- 不能替代测试、Code Review、Git 纪律和人的产品判断。

## 安装

克隆仓库后，把运行时 skill 文件安装到 Codex skills 目录：

```bash
git clone https://github.com/junjiang858/agent-project-kit.git
cd agent-project-kit
./scripts/install.sh
```

默认安装位置：

```text
${CODEX_HOME:-$HOME/.codex}/skills/agent-project-kit
```

也可以指定安装位置：

```bash
./scripts/install.sh /path/to/skills/agent-project-kit
```

## 使用

显式调用 skill：

```text
Use $agent-project-kit to turn my app idea into a project charter and implementation workflow.
```

默认情况下，这个 skill 会分步引导项目启动。它应该一次只问一个问题，而不是一次性丢出很长的问卷。

常见请求：

```text
Use $agent-project-kit to help me choose a tech stack for this product idea.
Use $agent-project-kit to draft root AGENTS.md and docs/ops/TOOL_POLICY.md for this repo.
Use $agent-project-kit to plan the backend skeleton and acceptance checklist.
Use $agent-project-kit to review whether this backend is safe enough to deploy.
```

## 工作流

这个 skill 会按阶段路由任务：

1. 项目立项与 MVP 边界
2. 技术栈选择与 Git 保险
3. Agent 宪法与可复用 skill 流程
4. 前端页面地图与骨架计划
5. 数据库设计
6. 后端业务说明与最小后端骨架
7. 架构验收与安全验收
8. 工具权限矩阵
9. 部署与 AI 工作流文档

## 仓库结构

```text
.
├── SKILL.md                  # skill 运行入口
├── agents/openai.yaml        # Codex UI 元信息
├── references/               # 按阶段按需加载的参考文件
├── templates/                # 可复制到项目中的文档模板
├── examples/tiny-webapp/     # 小型端到端示例
├── scripts/install.sh        # 本地安装脚本
└── scripts/validate.py       # 仓库校验脚本
```

## 生成项目的文档布局

默认情况下，项目文档不要全部堆在仓库根目录。根目录只保留 `AGENTS.md` 作为 Agent 索引，详细的项目事实文档放到 `docs/`：

```text
.
├── AGENTS.md
└── docs/
    ├── project/PROJECT_CHARTER.md
    ├── architecture/TECH_STACK.md
    ├── architecture/ENGINEERING_BASELINE.md
    ├── architecture/FRONTEND_PLAN.md
    ├── architecture/DATABASE_DESIGN.md
    ├── architecture/BACKEND_SPEC.md
    ├── workflow/AI_WORKFLOW.md
    ├── ops/TOOL_POLICY.md
    └── ops/DEPLOYMENT.md
```

## 模板

当 skill 要求阶段产物时，可以复制这些模板到你的项目里：

- `templates/AGENTS.md`
- `templates/docs/project/PROJECT_CHARTER.md`
- `templates/docs/architecture/TECH_STACK.md`
- `templates/docs/architecture/ENGINEERING_BASELINE.md`
- `templates/docs/architecture/FRONTEND_PLAN.md`
- `templates/docs/architecture/DATABASE_DESIGN.md`
- `templates/docs/architecture/BACKEND_SPEC.md`
- `templates/docs/workflow/AI_WORKFLOW.md`
- `templates/docs/ops/TOOL_POLICY.md`
- `templates/docs/ops/DEPLOYMENT.md`

## 校验

发布前运行本地校验：

```bash
python3 scripts/validate.py
```

它会检查必需文件、README 语言切换链接、Markdown 代码块闭合、skill frontmatter、阶段 reference 路由、生成项目的文档布局，以及 Product MVP 基线覆盖。

## 为什么做它

很多 AI 编程项目失败，不是因为 AI 不会写代码，而是因为它在项目还没有稳定形状时就开始写代码。Agent Project Kit 在最容易漂移的地方加一点结构：模糊需求、技术栈摇摆、工具边界缺失、后端业务不清、数据库设计随意、安全验收只听口头承诺。

目标不是增加流程感，而是减少后期昂贵返工。

## 许可证

MIT
