# Agent Project Kit Skill 演进记录

这份文档记录 Agent Project Kit 这个 skill 在原 Codex 会话中的优化、修复和经验沉淀。它不是聊天记录备份，而是把真实开发过程中反复暴露的问题，整理成可复用的工程经验。

## 证据来源与可信度

本记录使用三类证据：

- 原 Codex 会话记录：来自本机 Codex 会话索引和对应 JSONL 记录，使用会话标题与 thread id 标识。
- Git 提交记录：使用 commit hash、提交标题和涉及文件确认实际落地内容。
- 当前代码证据：使用仓库中的 `SKILL.md`、`references/`、`templates/`、`scripts/validate.py` 等文件确认现状。

证据等级：

- A：会话正文和 git 提交都能对应，可信度最高。
- B：主要来自 git 提交和当前文件结构，适合记录早期仓库演进。
- C：主要来自会话讨论或本地环境操作，适合记录经验，但不等同于仓库功能变更。

## 时间线总览

| 时间                      | 会话或证据                                                                                                         | 问题关键                                         | 解决结果                                                          | 证据                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------- | ------------------------------- |
| 2026-06-16              | Git 初始提交                                                                                                      | 需要把 AI 编程项目启动经验做成 skill                      | 建立初版 playbook、references 和 agent 配置                           | `8b3c0ec`, `8ad7a63`            |
| 2026-06-16              | Git 提交                                                                                                        | skill 需要可发布、可安装、可校验                          | 增加 README、LICENSE、安装脚本、validate、CI 和模板                        | `781af8b`, `ecfc936`, `b07a177` |
| 2026-06-17              | Git 提交                                                                                                        | 文档布局和 Product MVP 基线不足                       | 建立 `templates/docs/...`、document layout、工程基线、架构基线             | `08095b0`                       |
| 2026-06-21              | 了解工具作用 `019ee8ca-d2e9-7733-b196-4cf5d5cd26a3`                                                                 | workflow 优先级和项目作用确认缺失                        | 增加默认主流程优先级、Project Purpose Confirmation 和校验                   | `61f1029`                       |
| 2026-06-21              | 优化 skill 流程 `019ee8e2-b1c6-7801-9f93-e5cde12c2f4f`                                                            | PRD 深度不足、未获同意就写文档、README 公共化不足               | 强化立项门禁、安装示例、README 和完成提示                                      | `2ed6e44`, `843b18d`, `034fb34` |
| 2026-06-21              | 确认规范文档同步 `019ee92f-0143-7711-add4-8d169f7d5a50`                                                               | 实现变更可能不回写真源文档，提示语不随用户语言变化                    | 增加 Source-of-Truth Change Gate 和语言自适应完成提示                     | `910582d`                       |
| 2026-06-21              | 优化项目阶段引导 `019ee95c-31d9-7383-abbe-d76fe2a48942`                                                               | 目标只停在工程基线，不区分首个 MVP 切片                       | 增加工程基线 ready 和 First MVP Slice 两阶段目标                          | `490477d`                       |
| 2026-06-21              | 添加同类项目调研 `019eeabd-e6bf-71c2-8eaf-d7a27f78ad00`                                                               | 只细化用户 idea，缺少具体参考项目和能力库扫描                    | 增加 Reference Project Scan Gate 和 Capability Library Scan Gate | `490477d`                       |
| 2026-06-22              | 分析快速推进缺失原因 `019eeb07-0209-7e93-b29b-721902e99d62`                                                             | 快速推进选项丢失，确认依赖 UI，语言不自适应                      | 增加 Steady/Accelerated path、文字确认兜底、用户语言规则                      | `77d7268`                       |
| 2026-06-22              | 规范 skill 代码结构 `019eee70-34f4-7072-b3c4-7733beb3ca56`                                                          | 首版代码容易把 UI/config/i18n/utils 塞进单文件           | 增加前端工程化契约和组件拆分规则                                              | `08184be`                       |
| 2026-06-22              | 制定MVP页面设计规范 `019eee8d-4a71-73e0-8a84-1190cdc67ed0`                                                            | MVP 页面 UI/UX/design system 粗糙，快速推进可能跳过 UI 门禁 | 增加 Product MVP UI Quality Gate                                | `0eb0495`                       |
| 2026-06-22 至 2026-06-23 | 审查 skill 实现规范 `019eef9d-61fa-7c21-9f05-db3d7174ed57`                                                          | 默认栈、UI 库、图标库、仓库结构写得太硬                        | 把默认技术栈改为上下文候选，增加 repository shape 规则                          | `9bb85ab`                       |
| 2026-06-23              | 规划 skill 文档目录、分析 Skill 与插件重叠关系 `019ef385-6f09-7ee3-a787-e188e8e512d1`, `019ef38a-08ac-7b53-878b-807c76901439` | 和 Superpowers/OpenSpec 重叠，功能开发被拉回重流程，文档长期膨胀  | 增加四条任务路径、fallback、handoff 和文档蒸馏目录                             | `ebcd95e`                       |
| 2026-06-23              | 评估 skill README 质量 `019ef3c1-0574-7fc0-b9d6-291c39981302`                                                     | README 太像完整手册，Quick Start 靠后，首页展示不够成熟        | 重组 README，增加 hero、badge、导航和更轻的信息架构                            | `cdcf032`                       |
| 2026-06-24              | 设计异步MVP风险检测 `019ef8ad-c16a-7fb1-991e-31b07e0d1f61`                                                            | MVP 完成、完整范围完成、发布就绪混在一起，检测可能拖慢普通问答            | 增加 MVP closure 生命周期和快照脚本                                      | `b6705ca`                       |
| 2026-06-24 至 2026-06-25 | 审阅 skill 膨胀与 token `019ef8dd-8a37-7711-b05f-77cf3e46b6f9`                                                     | `SKILL.md` 膨胀，读取 token 成本高，瘦身后规则可能丢失         | 把入口瘦身为 router，细节迁移到 references，并用 validate 保证覆盖               | `d04037e`                       |
| 2026-06-25              | 分析两个文件夹作用 `019efd1a-21b8-7d71-846e-0b7dffbf2857`                                                              | 当前仓库迁移到 `github/` 后，旧 Codex 会话路径可能失效         | 直接迁移项目，保留 git 历史，但提醒旧会话工作目录可能断开                               | C 级会话证据                         |

## 阶段复盘

### 1. 初版 playbook 到可发布 skill

**时间点**

2026-06-16 至 2026-06-17。

**问题关键**

最初需要的不是一个普通业务项目，而是一套让 AI 编程项目先澄清、再定规格、再实现的工作流。早期风险是：只把经验写成提示词，缺少可安装、可校验、可复用的仓库结构。

**解决办法**

先建立 `SKILL.md` 作为入口，再把前端、后端、数据库、安全、工具、workflow 等细节拆到 `references/`。随后补 README、LICENSE、安装脚本、validate 脚本、GitHub Actions 和模板文件，让它从“本地经验”变成可以发布的 skill 包。

**代码改动**

- `8b3c0ec Initial AI programming project playbook skill`
- `8ad7a63 Rename skill to Agent Project Kit`
- `781af8b Add open source packaging and templates`
- `08095b0 Add Product MVP doc layout baseline`
- 涉及 `SKILL.md`、`references/`、`templates/`、`scripts/install.sh`、`scripts/validate.py`、`.github/workflows/validate.yml`。

**通用经验**

一个可复用 skill 不应只有提示词，还需要三层结构：入口规则、按阶段渐进披露的 reference、可复制的模板。只要这些规则会被多人或多项目复用，就要尽早加校验脚本，把“文件存在、关键门禁、模板路径、README 链接”等约束自动化。

**相关证据**

证据等级 B。早期阶段主要由 git 提交和当前文件结构佐证。

### 2. 主流程优先级与项目作用确认

**时间点**

2026-06-21，会话 `了解工具作用`，thread id `019ee8ca-d2e9-7733-b196-4cf5d5cd26a3`。

**问题关键**

用户指出两个问题：

- 如果项目使用这个 skill，应该避免被 Superpowers 等重叠 workflow skill 抢走主流程。
- 当前流程问了目标用户后就开始规划实现，缺少“总结项目作用并让用户确认”的步骤。

**解决办法**

把 Agent Project Kit 定义为项目级任务的默认主流程；Superpowers、TDD、planning 等只能作为辅助方法库。再增加 Project Purpose Confirmation：在技术栈、前端、后端、数据库或实现规划前，必须总结项目服务谁、解决什么问题、核心作用是什么、MVP 先做什么，并等待用户确认。

**代码改动**

- `61f1029 Strengthen skill workflow guards`
- 修改 `SKILL.md`：增加 `Default Workflow Priority` 和 `Project Purpose Confirmation`。
- 修改 `references/project-initiation.md`：把项目作用确认放到立项阶段。
- 修改 `templates/docs/project/PROJECT_CHARTER.md`：让项目章程记录这次确认。
- 修改 `scripts/validate.py`：增加校验，防止这两个保护点被删。

**通用经验**

workflow 类 skill 的优先级要写清楚，但不能无限接管。合理做法是：项目级工作由它路由，局部代码解释、测试修复、单命令等轻任务可以跳过。另一个经验是：项目 purpose 不是 agent 自己推断完就能继续，必须让用户确认，否则后续文档和技术栈都会建立在未确认假设上。

**相关证据**

证据等级 A。会话中有用户要求“先说明规划等我批准后再修改代码”、批准后实施、校验通过、提交并合并 `61f1029` 的完整记录。

### 3. PRD 深度、文档同意和公开化包装

**时间点**

2026-06-21，会话 `优化 skill 流程`，thread id `019ee8e2-b1c6-7801-9f93-e5cde12c2f4f`。

**问题关键**

真实调试时发现：agent 只用一句话解析项目，需求剖析很浅，甚至没有问清“AI 工具”到底指 HTTP API、MCP、function tools、local commands 还是 workflow。另一个严重问题是：项目技术栈没有争取用户同意就开始写文档。

**解决办法**

把“问清领域名词和需求深度”写成通用规则，而不是针对“AI 工具”写死。增加 Requirements Depth Gate、Document Consent Gate、Technology Stack Confirmation 等门禁。随后补充 README 的用途、适用人群、适用场景、安装示例、公开仓库路径去个人化，以及目标完成提示。

**代码改动**

- `2ed6e44 Tighten project initiation guardrails`
- `843b18d docs: clarify install examples`
- `034fb34 docs: refine skill readiness guidance`
- 涉及 `README.md`、`README.zh-CN.md`、`SKILL.md`、`references/project-initiation.md`、`references/architecture-baseline.md`、`references/workflow-checklists.md`、`scripts/validate.py`。

**通用经验**

不能把一次真实项目里的具体名词硬编码成通用 skill 规则。更好的沉淀方式是把它抽象成“模糊领域名词必须澄清”。另外，写文档也是项目状态变更，尤其是 `AGENTS.md`、`docs/` 这类 source-of-truth 文件，应该有明确用户同意，而不是把“帮我规划”解释成“可以写文件”。

**相关证据**

证据等级 A。会话记录包含“不能针对某一类问题写硬规则”的反馈，也包含后续 README、安装示例、完成提示、校验和提交证据。

### 4. 真源文档同步和语言自适应

**时间点**

2026-06-21，会话 `确认规范文档同步`，thread id `019ee92f-0143-7711-add4-8d169f7d5a50`。

**问题关键**

用户指出：如果后续实现时补充数据表、后端 API、前端设计，应该先更新原来的规范文档再实施，否则文档会很快失真。另一个问题是：工程基线 ready 的提示语固定为中文，英文用户会收到不合适的反馈。

**解决办法**

增加 Source-of-Truth Change Gate：凡是会改变设计、API、数据、权限、依赖、部署或运维的实现，先更新对应真源文档，再写代码。完成提示改为匹配用户当前语言，而不是固定中文。

**代码改动**

- `910582d Update source-of-truth and readiness gates`
- 修改 `SKILL.md`、`references/workflow-checklists.md`、`references/frontend.md`、`references/backend.md`、`references/database.md`、`templates/AGENTS.md`、`templates/docs/architecture/*`、`templates/docs/workflow/AI_WORKFLOW.md`、`scripts/validate.py`。

**通用经验**

项目文档不是一次性启动材料，而是后续实现的契约。只要实现改变契约，就要先更新真源文档。另一方面，完成提示也属于用户体验，不能把中文模板硬套给非中文用户；流程规则和里程碑提示都应语言自适应。

**相关证据**

证据等级 A。会话中明确讨论了 OpenSpec 等流程“先更新规范文档再实施”的正确性，并完成 `910582d` 提交。

### 5. 阶段目标、参考项目扫描和能力库扫描

**时间点**

2026-06-21，会话 `优化项目阶段引导` 和 `添加同类项目调研`，thread id `019ee95c-31d9-7383-abbe-d76fe2a48942`、`019eeabd-e6bf-71c2-8eaf-d7a27f78ad00`。

**问题关键**

原流程的目标停在“项目工程基线完成”，但用户真正想要的是至少推进到第一个 MVP 版本页面或切片完成。另一个问题是：面对用户 idea 时，流程只会细化需求，却不会主动扫描社区中类似产品、项目、repo、插件或模板，因此用户拿不到更宽的方向选择。技术栈确认前也缺少对成熟第三方库的扫描。

**解决办法**

把默认目标拆成两个里程碑：Project engineering baseline ready 和 First MVP Slice complete。对“页面”和“切片”的关系做澄清：页面可以是 web MVP 的入口，但真正完成标准是一个被批准、可验证的产品切片。增加 Reference Project Scan Gate，要求给出具体项目链接；增加 Capability Library Scan Gate，要求按项目能力调研成熟、开源或可检查、维护良好的第三方库，并和核心技术栈一起让用户确认。

**代码改动**

- `490477d Add idea and stack scan gates`
- 修改 `README.md`、`README.zh-CN.md`、`SKILL.md`、`examples/tiny-webapp/README.md`、`references/architecture-baseline.md`、`references/frontend.md`、`references/project-initiation.md`、`references/workflow-checklists.md`、`scripts/validate.py`、`templates/docs/architecture/TECH_STACK.md`、`templates/docs/project/PROJECT_CHARTER.md`。

**通用经验**

项目启动不是只问用户“你想做什么”，还要帮用户看到相邻解法。reference scan 的关键不是泛泛说“可以参考某某类型产品”，而是给具体链接、可借鉴点、不能盲抄的点，以及它如何改变 MVP 方向。技术栈确认也不应只选框架，还要把项目能力映射到库选择和维护风险。

**相关证据**

证据等级 A。会话中用户明确要求“具体项目链接”和“基于技术能力调研成熟第三方库”，最终提交 `490477d`。

### 6. 快速推进、文字确认和用户语言规则

**时间点**

2026-06-22，会话 `分析快速推进缺失原因`，thread id `019eeb07-0209-7e93-b29b-721902e99d62`。

**问题关键**

本地调试时发现，到达 `AGENTS.md` 后后续文档写入没有出现快速推进选项。进一步讨论后，用户提出两条全局规则：

- 需要确认的任务，必须默认提供文字选项，不能只依赖 UI 按钮、`request_user_input` 或主机特定快捷操作。
- agent 回复语言应根据用户语言自适应。

**解决办法**

把快速推进整理为两条明确路径：`A. Steady path` 和 `B. Accelerated path`。当缺少多个 readiness 文档时，不是机械列清单，而是先判断当前阶段，再说明哪些文档直接解锁下一阶段。加入 Confirmation Prompt Rule 和 User Language Rule，并同步到本地调试副本用于验证。

**代码改动**

- `77d7268 docs: add global interaction defaults`
- 修改 `SKILL.md`、`references/project-initiation.md`、`references/workflow-checklists.md`、`scripts/validate.py`、`templates/AGENTS.md`。

**通用经验**

任何依赖宿主 UI 的确认机制都不够稳。skill 应该把关键确认写成普通文本选项，保证用户在任何客户端都能回复。快速推进也不能变成“跳过门禁”，它只是对命名文档批次的一次性授权，完成后仍要重新跑 readiness audit。

**相关证据**

证据等级 A。会话中有本地调试问题、修复规划、同步本地项目和提交 `77d7268` 的完整记录。

### 7. 前端工程化契约

**时间点**

2026-06-22，会话 `规范 skill 代码结构`，thread id `019eee70-34f4-7072-b3c4-7733beb3ca56`。

**问题关键**

真实生成的首版代码把 UI、config、多语言、utils 等放进同一个文件，导致组件拆分、目录结构和后续维护很差。用户强调这不是首版补救，而是通用前端工程能力。

**解决办法**

把前端文件目录划分和组件拆分变成 `FRONTEND_PLAN.md` 的工程契约：前端实现前必须定义 source tree、file boundary contract、component split rules、state/config/i18n/icons/assets/utils ownership、import boundaries 和结构验收清单。

**代码改动**

- `08184be docs: add frontend engineering contract`
- 修改 `SKILL.md`、`references/architecture-baseline.md`、`references/frontend.md`、`references/workflow-checklists.md`、`scripts/validate.py`、`templates/AGENTS.md`、`templates/docs/architecture/FRONTEND_PLAN.md`、`templates/docs/workflow/AI_WORKFLOW.md`。
- 会话中还新增了 Obsidian 手册文章，但该文章不属于本仓库提交。

**通用经验**

代码结构不是实现细节，而是长期维护契约。尤其是 AI 生成前端时，必须提前约束目录边界、组件职责、状态所有权和 import 边界，否则后续会用“能跑”为理由累积难维护文件。

**相关证据**

证据等级 A。会话中记录了问题示例、用户要求通用化、实施结果和提交 `08184be`。

### 8. Product MVP UI Quality Gate

**时间点**

2026-06-22，会话 `制定MVP页面设计规范`，thread id `019eee8d-4a71-73e0-8a84-1190cdc67ed0`。

**问题关键**

用户认为 skill 生成的 MVP 页面 UI 布局、交互和 design system 太简单粗糙。即使是 MVP，也应在满足功能的前提下尽可能有更好的 UI/UX/design system。用户还追问：快速推进时这个 UI 门禁是否也能正常落地。

**解决办法**

引入 Product MVP UI Quality Gate，要求前端实现前覆盖 Design Read、Design Dials、design tokens、UI component strategy、state and interaction contract、responsive rules、accessibility expectations、anti-slop guardrails 和 browser UI verification。并明确 accelerated path 不能跳过 UI 门禁。

**代码改动**

- `0eb0495 docs: add product mvp ui quality gate`
- 修改 `SKILL.md`、`references/frontend.md`、`references/workflow-checklists.md`、`scripts/validate.py`、`templates/AGENTS.md`、`templates/docs/architecture/FRONTEND_PLAN.md`、`examples/tiny-webapp/README.md`。

**通用经验**

MVP 不等于粗糙。MVP 的目标是控制范围，不是放弃质量。前端质量门禁要前置到计划阶段，并且要纳入快速推进后的 readiness audit，否则“批量创建文档”会绕过最重要的体验约束。

**相关证据**

证据等级 A。会话中有用户对 UI 粗糙的反馈、证据来源追问、批准实施、快速推进补充和提交 `0eb0495`。

### 9. 默认技术栈改为上下文候选

**时间点**

2026-06-22 至 2026-06-23，会话 `审查 skill 实现规范`，thread id `019eef9d-61fa-7c21-9f05-db3d7174ed57`。

**问题关键**

在真实实现里，默认 UI 库、图标库、仓库结构可能会因为 Stitch 设计稿、去 AI 味、设计系统还原等原因变化。另一个具体问题是：纯前端本地项目没有服务器端，却被默认做成 pnpm workspace，可能是 skill 的默认结构影响了实现。

**解决办法**

把默认技术栈建议改成上下文候选，而不是硬要求。仓库形态、UI library、icon library、framework、package manager、backend/database boundaries 都应由产品形态、设计系统、实现需要、迁移成本和生产兼容性证明。进一步把过窄的 Vite/React 表述泛化为 single deployable frontend app、client-rendered SPA frameworks 等通用说法。

**代码改动**

- `9bb85ab docs: make stack defaults context-aware`
- 修改 `SKILL.md`、`references/architecture-baseline.md`、`references/frontend.md`、`references/workflow-checklists.md`、`scripts/validate.py`、`templates/AGENTS.md`、`templates/docs/architecture/ENGINEERING_BASELINE.md`、`templates/docs/architecture/FRONTEND_PLAN.md`、`templates/docs/architecture/TECH_STACK.md`。

**通用经验**

默认栈应该降低决策成本，而不是替代决策。skill 可以给候选和偏好，但必须要求 agent 解释为什么当前项目需要单包、workspace、monorepo、特定 UI 库或图标库。`ENGINEERING_BASELINE.md` 的价值也在这里：它记录工程执行标准，防止后续 agent 随意改变仓库形态。

**相关证据**

证据等级 A。会话中讨论了 Vite SPA 表述过窄、pnpm workspace 是否合理、`ENGINEERING_BASELINE.md` 作用，并提交 `9bb85ab`。

### 10. 与 Superpowers/OpenSpec 的边界和文档蒸馏

**时间点**

2026-06-23，会话 `规划 skill 文档目录`、`分析 Skill 与插件重叠关系`，thread id `019ef385-6f09-7ee3-a787-e188e8e512d1`、`019ef38a-08ac-7b53-878b-807c76901439`。

**问题关键**

Agent Project Kit 与 Superpowers、OpenSpec、GitHub Spec Kit 等 workflow 有重叠。现有触发范围偏宽，容易让普通功能也回到重型项目基线流程。另一个长期风险是：每次功能变更都往 `FRONTEND_PLAN.md`、`BACKEND_SPEC.md`、`DATABASE_DESIGN.md` 塞细节，核心真源文档会越来越臃肿。

**解决办法**

把任务分成四条路径：

- Project Baseline Path：新项目、缺少基线、技术栈和工程基线等。
- Contract-Changing Feature Path：改变设计、API、数据、权限、依赖、部署等契约。
- Bounded Feature Path：在已批准契约内的普通功能。
- Local Fix Path：小修、解释、单命令、测试修复等。

同时增加 Optional Workflow Tool Fallback：Superpowers、OpenSpec 等是可选增强，不是硬依赖。再增加 Source-of-Truth Distillation Gate，把稳定功能、单次变更、长期决策和 Agent Project Kit 过程产物分别放进 `docs/features/`、`docs/changes/`、`docs/decisions/`、`docs/agent-project-kit/`。

**代码改动**

- `ebcd95e Refine project kit workflow routing`
- 修改 `README.md`、`README.zh-CN.md`、`SKILL.md`、`agents/openai.yaml`、`references/document-layout.md`、`references/workflow-checklists.md`、`templates/AGENTS.md`、`templates/docs/workflow/AI_WORKFLOW.md` 等。
- 新增模板：`templates/docs/features/FEATURE.md`、`templates/docs/changes/CHANGE.md`、`templates/docs/decisions/ADR.md`、`templates/docs/agent-project-kit/PROCESS_ARTIFACTS.md`。

**通用经验**

好的 workflow skill 不应该吞掉所有开发流程。它要负责判断“这是不是会改变契约”，如果不改变，就轻量交接到实现纪律。文档也要区分当前契约和过程材料：核心 docs 保持当前有效状态，变化细节进入 feature/change/decision/process artifact。

**相关证据**

证据等级 A。会话中明确对比了 Superpowers、OpenSpec 和 GitHub Spec Kit，并在实施后提交 `ebcd95e`。

### 11. README 信息架构和 GitHub 项目展示

**时间点**

2026-06-23，会话 `评估 skill README 质量`，thread id `019ef3c1-0574-7fc0-b9d6-291c39981302`。

**问题关键**

README 内容质量高，但太像完整说明书。Quick Start 出现太晚，二级标题过多，`README.md` 几乎和运行时 `SKILL.md` 一样长。作为 GitHub 首页，它需要更快说明是什么、怎么安装、什么时候用、和类似项目有什么不同。

**解决办法**

把 README 调整成“人类入口页”：前部放居中标题、slogan、badge、语言切换、页内导航和 Quick Start；中部说明 What It Does、When To Use、What You Get、How It Works；把运行时细节压回 `SKILL.md` 和 `references/`。后续又按成熟项目风格增加 hero、badge 和导航，把 Product MVP tag 改成更易懂的 Project Governance。

**代码改动**

- `cdcf032 Polish README presentation`
- 主要修改 `README.md`、`README.zh-CN.md`。

**通用经验**

README 和运行时 skill 的职责不同。README 面向人，要先完成理解、信任和上手；`SKILL.md` 面向 agent，要提供入口规则；`references/` 承载细节。把 README 写成完整运行手册会降低首次阅读效率，也会和 `SKILL.md` 重复消耗维护成本。

**相关证据**

证据等级 A。会话中做了行数对比、社区 README 参考、结构规划、实施、校验和提交 `cdcf032`。同一会话还讨论了 GitHub workflow、Releases、Packages、Contributors 和 Git 身份配置，其中 Git 身份配置属于本地环境经验，不属于仓库功能改动。

### 12. MVP closure 生命周期和异步风险检测

**时间点**

2026-06-24，会话 `设计异步MVP风险检测`，thread id `019ef8ad-c16a-7fb1-991e-31b07e0d1f61`。

**问题关键**

用户在真实项目里使用 skill 检查 MVP 达成情况时，会看到未完成目标和剩余风险。用户希望触发 skill 时能自动检测并给下一步建议，但又不希望拖慢普通问题回复或打断体验。讨论中还发现：工程基线 ready、首个 MVP 切片完成、完整 MVP 达成、发布就绪是不同状态，不能混用同一段恭喜语。

**解决办法**

增加生命周期状态：

- `Engineering Baseline Ready`
- `First MVP Slice Complete`
- `MVP Scope Incomplete`
- `Full MVP Scope Complete`
- `Release Ready`

增加 MVP Closure Sentinel：只有用户询问完成度、发布安全性、剩余风险、下一步，或 agent 准备声明完整 MVP/发布就绪时才触发完整审计。普通问答、本地小修不跑完整检测。新增快照脚本生成可缓存证据，但不替代 agent 判断。

**代码改动**

- `b6705ca Add MVP closure lifecycle states`
- 新增 `references/mvp-closure.md`
- 新增 `scripts/mvp_closure_snapshot.py`
- 修改 `SKILL.md`、`README.md`、`README.zh-CN.md`、`references/workflow-checklists.md`、`scripts/install.sh`、`scripts/validate.py`、`templates/docs/workflow/AI_WORKFLOW.md`、`templates/docs/agent-project-kit/PROCESS_ARTIFACTS.md`。

**通用经验**

完成状态要有语义层级。首个切片完成不是完整 MVP 完成，完整 MVP 完成也不等于发布就绪。风险检测应按触发条件运行，不能每次普通问答都做重审计。自动化脚本适合生成证据快照，但最终结论仍应由 agent 根据真源文档、代码和验证结果判断。

**相关证据**

证据等级 A。会话中明确讨论了状态语义、触发时机和实现计划；提交前验证包含 `python3 scripts/validate.py`、`git diff --check`、`mvp_closure_snapshot.py --json`。

### 13. `SKILL.md` 膨胀和 token 成本

**时间点**

2026-06-24 至 2026-06-25，会话 `审阅 skill 膨胀与 token`，thread id `019ef8dd-8a37-7711-b05f-77cf3e46b6f9`。

**问题关键**

随着规则增加，`SKILL.md` 不知不觉变得很长。用户担心 agent 每次读取都会消耗很多 token，也担心 skill 越来越臃肿。实施瘦身后，用户又指出：如果 `SKILL.md` 删除了很多内容，但 references 只是加目录，可能会影响原 skill 效果。

**解决办法**

把 `SKILL.md` 改成轻量 router，只保留核心规则、路径路由、门禁名称和 reference 指向。详细规则迁移到对应 `references/`。所有 runtime references 都增加 `## Contents`，便于渐进披露和后续扩展。强化 `scripts/validate.py`，检查迁移规则覆盖，确保被入口删掉的关键细节必须在 references 中存在。

**代码改动**

- `d04037e Slim skill router and preserve reference coverage`
- 大幅修改 `SKILL.md`
- 修改全部 runtime references：`references/architecture-baseline.md`、`references/backend.md`、`references/database.md`、`references/document-layout.md`、`references/engineering-baseline.md`、`references/engineering-rules.md`、`references/frontend.md`、`references/mvp-closure.md`、`references/project-initiation.md`、`references/security.md`、`references/tool-policy.md`、`references/workflow-checklists.md`
- 修改 `scripts/validate.py`
- README 中同步说明 validate 覆盖上下文预算、reference 目录和迁移规则。

**通用经验**

skill 的入口文件越长，越容易让 agent 在无关任务上支付上下文成本。更好的结构是：入口只做路由和硬门禁，阶段细节进入 reference，模板进入 templates，确定性检查进入 scripts。瘦身不能只删内容，必须用 validate 检查“被迁移的关键规则仍然存在”。

**相关证据**

证据等级 A。会话中有用户对 token 膨胀、规则承接和 Contents 一致性的追问；最终提交 `d04037e` 到分支 `codex/slim-skill-progressive-disclosure`。

### 14. 附记：项目迁移和 Codex 会话路径

**时间点**

2026-06-25，会话 `分析两个文件夹作用`，thread id `019efd1a-21b8-7d71-846e-0b7dffbf2857`。

**问题关键**

用户想把当前仓库迁移到 `Documents/github/`，同时保留 Codex 会话记录。需要判断移动项目是否会影响旧会话。

**解决办法**

讨论了两种方案：移动后在原路径创建软链接，或直接迁移。软链接更利于旧 Codex 会话继续通过原路径访问项目，但用户最终选择直接迁移。迁移后 git 历史和项目文件仍在新路径，旧 Codex 会话记录仍存在，但旧会话绑定的原工作目录可能失效。

**代码改动**

没有 skill 功能提交。这是本地项目迁移操作和经验记录。

**通用经验**

Codex 会话记录通常不在项目目录里，但会话工作目录会绑定到旧路径。移动项目不会删除 git 历史，却可能让旧会话的文件读写路径失效。若要同时整理目录和保留旧会话可用性，软链接是更稳妥的迁移方案；若直接迁移，最好在新路径重新打开会话。

**相关证据**

证据等级 C。该阶段主要来自会话记录和本地路径操作，不属于仓库功能演进。

## 横向沉淀的设计原则

### 1. 把真实失败抽象成通用规则

例如“AI 工具到底是什么”不是要写死 AI 工具流程，而是抽象成：模糊领域名词必须澄清。这样 skill 才能用于不同项目，而不是被某次案例绑死。

### 2. 文档同意是项目控制权的一部分

创建或修改 `AGENTS.md`、`docs/`、技术栈、架构契约，都在改变项目状态。agent 不能把“帮我规划”自动解释成“可以写文件”。文档同意门禁保护的是用户对项目事实的控制权。

### 3. 真源文档要维护当前契约，不要堆过程细节

核心 docs 应该记录当前有效的产品、架构、API、数据和工程契约。功能细节、一次性变更、长期决策和过程证据要分层存放，避免核心文档越来越胖。

### 4. 轻量路径和强门禁并不冲突

Project Baseline 和 Contract-Changing Feature 需要强门禁；Bounded Feature 和 Local Fix 需要轻交接。skill 的价值不是让每个任务都变重，而是判断什么时候必须变重。

### 5. MVP 是范围约束，不是质量豁免

首个 MVP 切片可以小，但不能粗糙到缺少状态、响应式、可访问性、设计系统和验证证据。UI quality gate 要进入前端计划，而不是实现后靠审美补救。

### 6. 默认栈应该是候选，不是硬编码

默认框架、包管理器、workspace、UI 库和图标库都应根据产品形态、设计证据、共享边界和迁移成本确认。模板可以给路标，但不能替代当前项目判断。

### 7. 生命周期状态要清楚

Engineering Baseline Ready、First MVP Slice Complete、MVP Scope Incomplete、Full MVP Scope Complete、Release Ready 分别代表不同完成度。混用会让用户误以为项目已经可发布。

### 8. 入口文件要瘦，规则不能丢

`SKILL.md` 应该像 router，而不是百科全书。详细规则放到 references，模板放到 templates，校验放到 scripts。瘦身后必须用 validate 确保关键规则仍被覆盖。

### 9. 工具集成要可选，fallback 要内置

Superpowers、OpenSpec、GitHub Spec Kit 等可以增强流程，但不能成为硬依赖。用户没安装时，Agent Project Kit 应该用内置 fallback 完成澄清、计划、实现、验证和证据回报。

### 10. 可发布项目需要产品化 README

README 的职责是让人快速理解、安装、判断是否适用。运行时规则不应全部塞进 README。对开源 skill 来说，安装入口、使用场景、差异化、校验方式和安全边界要比长篇内部规则更靠前。

## 当前结构总结

截至 `d04037e`，Agent Project Kit 的结构已经从“大而全的入口说明”演进为：

- `SKILL.md`：轻量路由器，保留主规则、路径选择、核心门禁和 reference 指向。
- `references/`：按阶段存放详细流程和约束，支持渐进披露。
- `templates/`：生成目标项目 source-of-truth 文档和过程文档的模板。
- `scripts/validate.py`：固定结构、门禁、README、模板、reference 覆盖和迁移规则。
- `scripts/mvp_closure_snapshot.py`：为 MVP closure 审计提供可缓存证据快照。
- `README.md` / `README.zh-CN.md`：面向人类读者的项目入口和快速上手说明。

这套演进的核心经验是：把 AI 编程中的“踩坑反馈”及时沉淀成可验证规则，但每次沉淀都要防止三件事：规则过窄、流程过重、入口过胖。
