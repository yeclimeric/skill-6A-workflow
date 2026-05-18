# Prompt 按阶段拆分设计

## 目标
将现有统一的 `resources/prompt.md` 中 A1~A6 阶段规则拆分为 6 份独立 prompt 文件，并让各阶段子 skill 的 entrypoint 直接引用对应阶段 prompt。

## 约束
- 每个阶段 prompt 必须自包含：包含激活方式、身份定义、技术执行规范 + 本阶段规则。
- 各阶段 prompt 保存到各阶段目录下：
  - `resources/manifest/A1-Align/prompt.md`
  - `resources/manifest/A2-Architect/prompt.md`
  - `resources/manifest/A3-Atomize/prompt.md`
  - `resources/manifest/A4-Approve/prompt.md`
  - `resources/manifest/A5-Automate/prompt.md`
  - `resources/manifest/A6-Assess/prompt.md`
- `resources/prompt.md` 改为总览索引（不再承载阶段正文规则）。

## 变更点
1. 新增 6 个阶段 prompt 文件（内容来源于原 `resources/prompt.md` 的公共段 + 对应阶段段落 + 技术执行规范段）。
2. 更新各阶段清单的 `entrypoint.path`：
   - A1~A6 均从 `resources/prompt.md` 改为 `resources/manifest/A*-*/prompt.md`。
3. 更新 `SKILL.md` 的执行指示，提示阶段规范入口为各阶段目录下的 prompt。
4. `resources/prompt.md` 变为索引文件，列出各阶段 prompt 路径与用途。

## 验证
- YAML/JSON 语法校验保持通过
- `resources/manifest/**/*.yaml` 中不再引用 `resources/prompt.md` 作为 entrypoint
- 目录结构符合既有规范并可被索引路由到各阶段子 skill

