# Agent Project Kit

[English](README.md) | [简体中文](README.zh-CN.md)

> 别再让编程 Agent 把一句模糊想法变成一堆难维护文件。
>
> Agent Project Kit 会让 Agent 先澄清、确认、写文档、选技术栈、建立规则和验收证据，再进入代码实现。

## ✨ 这是什么

Agent Project Kit 是一个面向 Codex 的 skill，给 AI 编程项目补上一套轻量的产品与工程操作系统。

它适合用户说出“帮我做一个项目”之后、但项目目标、用户、范围、技术栈、数据对象、安全边界和验收标准还不够清楚的阶段。

Agent Project Kit 不让 AI 直接冲进文件和代码，而是把项目推进到一条更稳的路径：逐步澄清需求、确认写文档权限、做技术决策、建立项目规则、拆实现计划，并要求用真实证据完成验收。

默认姿态是 Product MVP：

- 第一版功能可以小。
- 不要把地基做成一次性废稿。
- 仓库形态、技术路线、工程基线、工具权限和验收习惯应该能支撑后续真实迭代。

## 🚦 使用前 / 使用后

不使用这个 skill：

```text
“帮我做一个后台系统。”
→ Agent 直接创建文件、拍脑袋选技术栈、补需求、写浅层文档。
```

使用 Agent Project Kit：

```text
澄清用户
→ 定义 MVP 范围
→ 确认项目目的
→ 写文档前征求同意
→ 收敛到一条技术路线
→ 创建项目规则
→ 用证据验收
```

## 📦 你会得到什么

Agent Project Kit 会帮助 Agent 创建和维护这些项目真源文档：

- `docs/project/PROJECT_CHARTER.md`：用户、问题、MVP 范围、核心流程、领域对象、风险和验收标准。
- `docs/architecture/TECH_STACK.md`：唯一技术栈、拒绝的备选方案、迁移成本、生产兼容性和重新评估规则。
- `AGENTS.md`：项目级 Agent 规则和文档索引。
- `docs/architecture/ENGINEERING_BASELINE.md`：脚本、质量门禁、测试、迁移、环境规则和提交纪律。
- `docs/ops/TOOL_POLICY.md`：默认开放工具、项目专用工具和高风险确认门禁。
- `docs/workflow/AI_WORKFLOW.md`：澄清、规格、计划、实现、验证和归档流程。

## 🧩 它能帮你做什么

- 把模糊想法沉淀成 PRD 级项目章程，包含目标用户、核心流程、领域对象、非目标、风险和可客观检查的验收标准。
- 通过项目目的确认和逐文件同意机制，避免 AI 过早创建文档、拍板技术栈或开始实现。
- 基于产品形态、项目生命周期、团队能力、上线压力、迁移成本和生产兼容性，收敛到一条主技术路线。
- 把项目真源文档放进 `docs/`，避免关键规划散落在聊天记录里。
- 通过 `AGENTS.md`、工程基线、工具权限策略和工作流文档，建立 AI 在项目中的长期工作规则。
- 为前端、后端、数据库、安全、部署和验收规划提供可复用流程，让“完成了”必须带测试、构建、接口、浏览器或安全证据。

## 🧠 它的优势

- 减少 AI 漂移：让 Agent 在写文件或改代码前回到已经确认的项目事实。
- 保留用户控制权：创建真源文档、锁定技术栈、进入高风险操作前都要先确认。
- 让小项目更容易长大：把产品认知、技术架构、工程规则和实现任务分开沉淀。
- 降低新手门槛：不要求用户一开始懂完整工程流程，也能让 AI 按产品合伙人和架构顾问的方式推进项目。

## 🧭 适合谁

- 正在用 Codex、Claude Code、Cursor、Copilot 等 AI 编程工具的个人开发者和小团队。
- 想借助 AI 提速，但不想失去范围、技术栈、文档和验收标准控制权的产品型开发者。
- 技术经验还不完整、希望 AI 先像产品合伙人和架构顾问一样追问清楚，再进入代码生成的新手或早期开发者。
- 需要轻量项目结构，而不是完整项目管理平台的团队。
- 计划做成真实产品、内部工具、后台系统、数据看板、自动化系统、服务端项目，或希望原型后续能继续迭代的 AI 编程项目。

## 🎯 适合场景

- 你只有一个模糊想法，希望 AI 先问对问题，而不是直接开始写代码。
- 你需要 `PROJECT_CHARTER.md`、`TECH_STACK.md`、`AGENTS.md` 或 `TOOL_POLICY.md`，但希望 AI 先确认事实并在写文件前征求同意。
- 你正在权衡一次性原型和 Product MVP，希望获得一条唯一主技术路线、取舍理由和后续重新评估规则。
- 你想为前端、后端、数据库、安全、部署和验收建立可复用的 AI 工作流。
- 你准备新建一个仓库，希望后续 AI 会话都能读懂项目事实、边界、工具权限和验收要求。

## 💬 迷你示例

```text
用户：帮我创建一个项目。
Agent：当前阶段是项目立项。你想做一个什么项目？

用户：一个 AI 工具调试台。
Agent：我现在还不能写文件。这里的“AI 工具”具体指什么：
HTTP API、MCP 工具、函数工具、本地命令、工作流，还是其它东西？

用户：MCP 工具和 HTTP endpoint。
Agent：明白。下一步我要确认谁会使用它，以及第一版哪个流程必须跑通。
```

## 🔍 它有什么不同

Agent Project Kit 不是普通提示词合集。

它组合了：

- 阶段路由：Agent 只加载当前阶段需要的 reference。
- 确认门禁：需求深度、项目目的、文档写入、技术栈和高风险操作都要确认。
- 文档模板：复用项目、架构、工作流和运维真源文档。
- 阶段参考：覆盖前端、后端、数据库、安全、工具权限和工程基线。
- 本地校验：脚本检查必需文件、路由、门禁和文档布局是否仍然完整。

## 🚫 它不是什么

- 不是自动分析代码库的 CLI。
- 不是项目管理系统。
- 不是普通提示词合集。
- 不能替代测试、Code Review、Git 纪律和人的产品判断。

## ⬇️ 克隆到本地

先把仓库克隆到本地工作区：

```bash
git clone https://github.com/junjiang858/agent-project-kit.git
cd agent-project-kit
```

如果你想放到指定目录：

```bash
git clone https://github.com/junjiang858/agent-project-kit.git ~/skills/agent-project-kit
cd ~/skills/agent-project-kit
```

## 🛠 安装

把运行时 skill 文件安装到 Codex skills 目录：

```bash
./scripts/install.sh
```

默认安装位置是：

```text
${CODEX_HOME:-$HOME/.codex}/skills/agent-project-kit
```

如果你希望把 skill 放进某个项目本地目录，可以指定项目内 `.codex/skills` 路径：

```bash
./scripts/install.sh /path/to/project/.codex/skills/agent-project-kit
```

示例：

```bash
./scripts/install.sh ~/projects/my-app/.codex/skills/agent-project-kit
```

后续拉取更新后，重新运行同一个安装命令即可刷新已安装的 skill：

```bash
git pull
./scripts/install.sh
```

## 💬 使用

显式调用 skill：

```text
Use $agent-project-kit to turn my app idea into a project charter and implementation workflow.
```

默认情况下，这个 skill 会分步引导项目启动。它应该一次只问一个问题，而不是一次性丢出很长的问卷。

对于模糊想法，它现在会在写文件前执行三道启动门禁：

- 需求深度门禁：先澄清目标用户、核心流程、领域对象、用户操作、边界、风险和可客观检查的验收标准，再进入 PRD 级项目章程。
- 文档同意门禁：没有得到用户对具体文件的同意前，不创建或更新 `AGENTS.md`、`docs/` 下文件或其它项目真源文档。
- 技术栈确认门禁：项目目的和章程事实确认前，不选择、不锁定、不写入 `docs/architecture/TECH_STACK.md`；进入技术选型也需要用户同意。

使用示例：

```text
Use $agent-project-kit to help me clarify a vague product idea. Ask one question at a time and do not write files until I approve.

Use $agent-project-kit to turn this confirmed product direction into docs/project/PROJECT_CHARTER.md. First summarize the purpose and ask before writing the file.

Use $agent-project-kit to recommend exactly one tech stack after the project charter is confirmed. Ask before writing docs/architecture/TECH_STACK.md.

Use $agent-project-kit to create root AGENTS.md and docs/ops/TOOL_POLICY.md for this repo. Ask before writing each document.

Use $agent-project-kit to plan the backend skeleton and acceptance checklist.

Use $agent-project-kit to review whether this backend is safe enough to deploy.
```

## 🧯 实现前就绪门禁

在 Agent 创建应用脚手架、包管理文件、前端路由、API 骨架、数据库 schema、migration 或可运行功能前，它会先检查项目真源文档是否已经准备好。

对于 Product MVP，通常会检查：

- `AGENTS.md`
- `docs/project/PROJECT_CHARTER.md`
- `docs/architecture/TECH_STACK.md`
- `docs/architecture/ENGINEERING_BASELINE.md`
- `docs/architecture/FRONTEND_PLAN.md`
- `docs/architecture/DATABASE_DESIGN.md`
- `docs/architecture/BACKEND_SPEC.md`
- `docs/workflow/AI_WORKFLOW.md`
- `docs/ops/TOOL_POLICY.md`
- `docs/ops/DEPLOYMENT.md`

如果缺少必要文档，Agent 应该列出缺口，并询问是否先创建下一个文档，而不是直接写代码。

## 🎉 目标与完成信号

Agent Project Kit 会让每次项目级任务先说清楚当前目标：

- 目标结果：用户希望到达的阶段或项目状态。
- 完成信号：哪些文档、确认、审计或证据能证明目标已经达成。
- 下一步动作：下一个问题、文档、就绪审计或实现步骤。

对于新的 Product MVP，默认目标通常是：项目工程基线已就绪。

当项目目的已经确认、必要真源文档已经存在或明确不适用、实现前就绪门禁已经通过，并且用户确认就绪结果或批准下一步实现时，才算达成这个目标。

达成后，Agent 会用这句提示收尾：

```text
🎉 恭喜，项目工程基线已就绪！

✅ 项目目标、技术路线、核心文档和实现前门禁已经到位。
🚀 下一步可以从第一个已批准的产品闭环开始实现。
```

## 🧱 工作流

这个 skill 会按阶段路由任务：

1. 项目立项与 MVP 边界
2. 项目目的确认与文档写入同意
3. 技术栈决策与 Git 保险
4. Agent 宪法与可复用 skill 流程
5. 前端页面地图与骨架计划
6. 数据库设计
7. 后端业务说明与最小后端骨架
8. 架构验收与安全验收
9. 工具权限矩阵
10. 部署与 AI 工作流文档
11. 实现前就绪审计，然后才进入脚手架或代码实现
12. 输出目标完成信号和恭喜就绪提示语

## 📁 仓库结构

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

## 🗂 生成项目的文档布局

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

## 🧾 模板

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

## ✅ 校验

发布前运行本地校验：

```bash
python3 scripts/validate.py
```

它会检查必需文件、README 语言切换链接、Markdown 代码块闭合、skill frontmatter、阶段 reference 路由、生成项目的文档布局，以及 Product MVP 基线覆盖。
它也会检查启动门禁是否仍然存在：需求深度、文档同意、技术栈确认，以及通用的领域对象澄清流程，避免把流程硬编码到某一个业务类型。

## 💡 为什么做它

很多 AI 编程项目失败，不是因为 AI 不会写代码，而是因为它在项目还没有稳定形状时就开始写代码。Agent Project Kit 在最容易漂移的地方加一点结构：模糊需求、技术栈摇摆、工具边界缺失、后端业务不清、数据库设计随意、安全验收只听口头承诺。

目标不是增加流程感，而是减少后期昂贵返工。

## 📄 许可证

MIT
