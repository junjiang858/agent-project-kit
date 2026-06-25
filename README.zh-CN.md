<h1 align="center">Agent Project Kit</h1>

<p align="center">
  <strong>让编程 Agent 先澄清、写文档、选路线、验收证据，再进入代码实现。</strong>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a href="SKILL.md"><img alt="Agent Skill" src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-555.svg"></a>
  <img alt="Codex" src="https://img.shields.io/badge/Codex-ready-111827.svg">
  <img alt="Project Governance" src="https://img.shields.io/badge/Project-Governance-7c3aed.svg">
</p>

<p align="center">
  <a href="#-快速上手">快速上手</a> ·
  <a href="#-它会做什么">它会做什么</a> ·
  <a href="#-什么时候用">什么时候用</a> ·
  <a href="#-你会得到什么">你会得到什么</a> ·
  <a href="#-工作机制">工作机制</a> ·
  <a href="#-与类似项目相比">类似项目对比</a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

---

> 别再让编程 Agent 把一句模糊想法变成一堆难维护文件。
>
> Agent Project Kit 会让 Agent 先澄清、确认、写文档、选技术栈，并用证据验收，再进入代码实现。

Agent Project Kit 是一个面向 Codex 的 skill，用来治理 AI 辅助软件项目。它适合项目想法、用户、范围、技术栈、数据模型、工具权限和验收标准还不够清楚的阶段，为 Agent 补上一套轻量的产品与工程操作系统。

它最适合作为进入实现纪律前的项目路由器。

## 🚀 快速上手

克隆仓库：

```bash
git clone https://github.com/junjiang858/agent-project-kit.git
cd agent-project-kit
```

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

显式调用 skill：

```text
Use $agent-project-kit to turn my app idea into a project charter and implementation workflow.
```

拉取更新后，重新运行安装命令即可刷新已有安装：

```bash
git pull
./scripts/install.sh
```

发布前运行本地校验：

```bash
python3 scripts/validate.py
```

## 🧩 它会做什么

Agent Project Kit 会帮助 Agent：

- 把模糊想法沉淀成 PRD 级项目章程。
- 在收敛模糊想法前，先扫描带具体链接的真实参考项目。
- 创建真源文档或锁定重大技术决策前，先取得明确同意。
- 基于产品形态、项目生命周期、团队能力、迁移成本和生产兼容性，收敛到一条主技术路线。
- 在确认技术栈前，审阅项目需要的第三方库，包含链接、维护证据和纳入/暂缓/拒绝决策。
- 把默认技术栈当作候选，而不是硬约束：仓库形态、UI 库和图标库都要由产品形态、设计系统证据和真实包边界来证明。
- 把持久项目事实放进 `docs/`，避免关键规划散落在聊天记录里。
- 把后续任务分流到 Project Baseline、Contract-Changing Feature、Bounded Feature 或 Local Fix，避免小改动反复重跑完整项目基线。
- 区分 Engineering Baseline Ready、First MVP Slice Complete、MVP Scope Incomplete、Full MVP Scope Complete 和 Release Ready，避免不同里程碑提示混在一起。
- 让“完成了”必须带验证证据，而不是只听口头承诺。

## 🎯 什么时候用

| 场景                             | Agent Project Kit 会帮助你           |
| ------------------------------ | -------------------------------- |
| 模糊产品想法                         | 一次问一个问题、扫描参考项目、选择 MVP 方向、确认项目目的。 |
| 新仓库或基线缺失                       | 在实现前创建真源文档、工具规则、技术栈决策和就绪检查。      |
| 技术栈或第三方库选择                     | 对比唯一主路线、拒绝的备选方案、能力库、维护证据和迁移风险。   |
| Contract-Changing Feature Path | 先更新受影响的真源文档，再进入代码实现。             |
| Bounded Feature Path           | 确认任务处在已批准契约范围内，然后交接给正常实现纪律。      |
| Local Fix Path                 | 不跑完整基线流程，使用最轻量的直接路径。             |

## 📦 你会得到什么

这个 skill 会帮助 Agent 创建和维护这些项目真源文档：

| 产物                                                                           | 用途                                                 |
| ---------------------------------------------------------------------------- | -------------------------------------------------- |
| `AGENTS.md`                                                                  | 项目级 Agent 宪法和真源文档索引。                               |
| `docs/project/PROJECT_CHARTER.md`                                            | 用户、问题、MVP 范围、核心流程、领域对象、风险和验收标准。                    |
| `docs/architecture/TECH_STACK.md`                                            | 唯一技术栈、拒绝的备选方案、迁移成本、生产兼容性和重新评估规则。                   |
| `docs/architecture/ENGINEERING_BASELINE.md`                                  | 脚本、质量门禁、测试、迁移、环境规则和提交纪律。                           |
| `docs/architecture/FRONTEND_PLAN.md`                                         | 页面地图、设计判断、Product MVP UI 质量门禁、设计系统、组件边界和浏览器 UI 验证。 |
| `docs/architecture/DATABASE_DESIGN.md`                                       | 领域对象、数据表、字段、关系、索引、migration、归属和回滚说明。               |
| `docs/architecture/BACKEND_SPEC.md`                                          | API 契约、权限、后端流程、集成、数据流和错误处理。                        |
| `docs/workflow/AI_WORKFLOW.md`                                               | 澄清、规格、计划、实现、验证和归档流程。                               |
| `docs/ops/TOOL_POLICY.md`                                                    | 默认工具、项目专用工具和高风险确认门禁。                               |
| `docs/ops/DEPLOYMENT.md`                                                     | 本地、预发、生产、环境变量、健康检查和回滚。                             |
| `docs/features/`、`docs/changes/`、`docs/decisions/`、`docs/agent-project-kit/` | 稳定功能说明、单次变更细节、长期决策，以及不应塞进当前状态文档的过程产物。              |

## ⚙️ 工作机制

对于项目级任务，这个 skill 会把 Agent 路由到这条流程：

```text
澄清当前阶段
→ 扫描具体参考项目
→ 确认项目目的
→ 写真源文档前征求同意
→ 选择唯一技术栈和能力库
→ 审计实现前就绪状态
→ 按契约影响分类后续任务
→ 只有满足对应门禁后才实现
→ 回报验证证据
```

关键门禁包括：

- **参考项目扫描门禁**：在收敛模糊想法前，先提供 3-7 个具体项目、产品、repo、插件、模板或相邻实现，并带直接链接。
- **需求深度门禁**：在起草 PRD 级项目章程前，澄清用户、核心流程、领域对象、用户操作、边界、风险和客观验收标准。
- **文档同意门禁**：没有得到用户对具体文件的同意前，不创建或更新 `AGENTS.md`、`docs/` 下文件或其它真源文档。
- **技术栈确认门禁**：项目目的和章程事实确认前，不锁定 `docs/architecture/TECH_STACK.md`。
- **能力库扫描门禁**：在确认技术栈前，把项目所需技术能力映射到成熟、维护良好的第三方库。
- **项目规格就绪门禁**：必要真源文档准备好之前，不创建应用代码、包管理文件、前端路由、API、schema、migration 或可运行行为。
- **真源文档变更门禁**：后续任务一旦改变设计、API、数据、权限、工具、部署或运维，先更新原始真源文档，再进入实现。
- **真源文档蒸馏**：把持久有效的当前契约保留在核心文档，把功能、变更、决策或过程细节放到 `docs/features/`、`docs/changes/`、`docs/decisions/` 或 `docs/agent-project-kit/`。

参考项目扫描门禁要求具体项目链接。能力库扫描门禁会审阅项目需要的第三方库，并给出直接链接和维护证据。

当多个就绪文档缺失时，skill 会提供文字选项：稳步推进只处理下一个最关键文档，快速推进则授权本阶段命名的文档批次。所有确认类提示都必须能用文字直接回复，即使宿主环境提供 UI 选择工具，也要匹配用户当前语言。

Superpowers、OpenSpec、GitHub Spec Kit、issue tracker 等工具都可以作为可选增强。如果它们不可用，Agent Project Kit 会使用内置 fallback：澄清范围、Contract Impact Check、计划、实现、验证和证据回报。

## ✅ 目标与完成信号

每次项目级任务都会先说明目标结果、完成信号和下一步动作。对于新的 Product MVP，默认目标通常是：项目工程基线就绪后，首个 MVP 切片完成并通过验收。

工程基线完成意味着项目目的已经确认，必要真源文档已经存在或明确不适用，实现前就绪门禁已经通过，并且用户确认就绪结果或批准下一步实现。首个 MVP 切片完成意味着一个已批准的产品闭环已经实现，并提供了新的构建、测试、浏览器、API、CLI、worker 或运行证据。

首个切片之后，skill 会使用 MVP closure 状态：`MVP Scope Incomplete`、`Full MVP Scope Complete` 和 `Release Ready`。MVP Closure Sentinel 只会在用户询问完成度、发布安全性、剩余风险、下一步，或 Agent 准备声明完整 MVP / 发布就绪时触发。普通本地修复和代码解释不会重新跑完整项目审计。

完成提示是语言自适应完成提示，应该匹配用户当前语言。

```text
🎉 恭喜，项目工程基线已就绪！

✅ 项目目标、技术路线、核心文档和实现前门禁已经到位。
🚀 下一步可以从第一个已批准的产品闭环开始实现。
```

```text
🎉 恭喜，首个 MVP 切片已完成！

✅ 第一个已批准的产品闭环已经实现，并提供了运行、构建、浏览器、API 或任务验收证据。
🚀 下一步可以继续扩展后续页面、数据流、接口、任务或部署发布。
```

```text
🎉 文档定义的 MVP 范围已完成！

✅ 当前实现已经覆盖真源文档定义的 MVP 范围，并提供了新的验证证据。
🚀 下一步进入正式项目发展：发布验证、架构加固、用户反馈和下一版本规划。
```

```text
🎉 发布验证已通过！

✅ MVP 范围、部署环境、回归检查、安全边界和运营准备已经通过当前证据验证。
🚀 下一步可以发布、监控真实使用情况，并规划发布后的修复和下一版本。
```

## 💬 迷你示例

```text
用户：帮我创建一个项目。
Agent：当前阶段是项目立项。你想做一个什么项目？

用户：一个保存读书笔记的小应用。
Agent：在细化需求前，我先扫描具体参考项目：
Omnivore（https://github.com/omnivore-app/omnivore）、Logseq（https://github.com/logseq/logseq）
和 Reor（https://github.com/reorproject/reor）。我会说明可借鉴点、不应照搬的地方，以及它们如何影响 MVP 方向。

用户：我更喜欢 Omnivore 那种轻量 read-it-later 方向。
Agent：明白。我会按这个方向继续确认目标用户，以及第一版哪个流程必须跑通。
```

## 🔍 它有什么不同

Agent Project Kit 不是普通提示词合集。它关注 AI 实现外层的项目治理层：

| 能力           | 这个 skill 增加了什么                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------- |
| 阶段路由         | Agent 只加载当前阶段需要的 reference。                                                                        |
| 参考 grounding | 模糊想法会先对照带具体链接的真实项目，再收敛需求。                                                                          |
| 技术栈纪律        | 技术决策包含唯一主路线、被拒绝的备选方案、能力库、维护证据和重新评估规则。                                                              |
| 用户控制         | 真源文档、技术栈决策和高风险操作都需要明确确认。                                                                           |
| 前端质量         | Product MVP 要求设计判断、设计系统 token、状态契约、反模板约束和浏览器验证。                                                    |
| 真源维护         | 当前有效契约保留在核心文档；功能、变更、决策和过程细节放进专门目录。                                                                 |
| 语言自适应        | 问题、确认、进度更新和完成提示匹配用户当前语言。                                                                           |
| 本地校验         | `scripts/validate.py` 检查必需文件、reference 路由、上下文预算、reference 目录、迁移规则覆盖、门禁、模板、README 链接和 Markdown 代码块。 |

## 🧭 与类似项目相比

| 对比对象                                    | 常见重点                                                        | Agent Project Kit 的重点                |
| --------------------------------------- | ----------------------------------------------------------- | ------------------------------------ |
| OpenAI/Codex skills 模型                  | 用 `SKILL.md` 加可选 scripts、references、assets 和渐进加载机制封装可复用工作流。 | 基于这个模型实现一套具体的项目治理工作流。                |
| `anthropics/skills`                     | 展示多种 skill 模式和文件处理工作流的参考实现。                                 | 聚焦 AI 辅助软件项目的基线操作系统。                 |
| `addyosmani/agent-skills` 等生命周期 skill 包 | spec、plan、build、test、review、安全、性能和发布纪律。                     | 更上游的项目清晰度、真源文档、实现前就绪、契约变化路由和边界内交接。   |
| OpenSpec、GitHub Spec Kit、issue spec     | 变更 proposal、spec、任务、归档和实现跟踪。                                | 仓库级当前状态真源优先级，以及外部规格工具不可用时的 fallback。 |
| 自主执行型框架                                 | 批准后更连续的 Agent 执行。                                           | 用户确认的决策、一次一个问题的澄清、写文件和高风险操作前的显式同意。   |
| 普通提示词合集                                 | 可复用提示词和角色指令。                                                | 模板、reference、阶段路由、文档门禁和仓库校验。         |

当产品形态或契约还在成型时，适合让 Agent Project Kit 做主流程；进入实现后，再搭配成熟生命周期 skill 做 TDD、代码审查、安全、性能和发布。

## 🛡️ 安全与信任

安装脚本只会把运行时 skill 文件和辅助脚本复制到目标目录：

- `SKILL.md`
- `agents/`
- `references/`
- `templates/`
- `scripts/`

它不会安装依赖、创建应用脚手架、修改包管理文件、执行远程代码或改写你的项目文档。项目文档和实现文件只会在用户直接要求，或通过 skill 工作流批准具体文档/操作后创建。

运行校验：

```bash
python3 scripts/validate.py
```

校验脚本会检查必需文件、README 语言切换链接、Markdown 代码块闭合、skill frontmatter、上下文预算、reference 目录、迁移规则覆盖、阶段 reference 路由、生成项目的文档布局、Product MVP 基线覆盖、Product MVP UI 质量门禁覆盖、MVP closure 语义、Implementation Handoff、真源文档蒸馏和模板路径。

和任何 skill 或 plugin 一样，安装前请先审阅文件，并在自己的环境里测试工作流，再把它用于关键项目。

## 📁 仓库结构

```text
.
├── SKILL.md                  # skill 运行入口
├── agents/openai.yaml        # Codex UI 元信息
├── references/               # 按阶段按需加载的参考文件
├── templates/                # 可复制到项目中的文档模板
├── examples/tiny-webapp/     # 小型端到端示例
├── scripts/mvp_closure_snapshot.py # 可缓存的 MVP closure 证据快照
├── scripts/install.sh        # 本地安装脚本
└── scripts/validate.py       # 仓库校验脚本
```

## 🗂️ 生成项目的文档布局

生成的项目文档不要全部堆在仓库根目录。根目录只保留 `AGENTS.md` 作为 Agent 索引，详细的项目事实文档放到 `docs/`：

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
    ├── features/<feature-name>.md
    ├── changes/<date-or-id>-<change-name>.md
    ├── decisions/ADR-<number>-<topic>.md
    ├── agent-project-kit/PROCESS_ARTIFACTS.md
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
- `templates/docs/features/FEATURE.md`
- `templates/docs/changes/CHANGE.md`
- `templates/docs/decisions/ADR.md`
- `templates/docs/agent-project-kit/PROCESS_ARTIFACTS.md`
- `templates/docs/workflow/AI_WORKFLOW.md`
- `templates/docs/ops/TOOL_POLICY.md`
- `templates/docs/ops/DEPLOYMENT.md`

## 🚫 它不是什么

- 不是完整自动分析代码库的 CLI；可选快照脚本只缓存证据，最终判断仍由 Agent 审计。
- 不是项目管理系统。
- 不是普通提示词合集。
- 不能替代测试、Code Review、Git 纪律和人的产品判断。
- 也不是项目基线就绪后跳过实现类 skill 的理由。

## 📄 许可证

MIT
