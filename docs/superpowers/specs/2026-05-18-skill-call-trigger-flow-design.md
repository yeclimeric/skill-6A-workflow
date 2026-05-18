# 6A Skill 调用与触发流程图设计

## 目标
为 skill-6a-workflow 生成“触发 + 路由”级别的调用流程图，用于让读者快速理解：
- 触发条件如何命中
- 入参如何校验
- 如何按 stage 路由到 A1~A6 子 skill
- 如何生成 docs_dir 并写入阶段文档
- 关键异常/阻塞分支在哪里

## 数据来源
- 触发词：metadata.json 的 trigger 字段
- 高层说明：SKILL.md
- 阶段路由索引：resources/manifest/index.yaml
- 各阶段契约与异常：resources/manifest/A*-*/skill.yaml
- docs 目录命名规则：resources/manifest/common/docs_dir_naming.yaml

## 产物
- SKILL.md：新增“调用与触发流程图”章节，使用 Mermaid 渲染
- resources/diagrams/skill_flow.mmd：同一份 Mermaid 源文件，用于复用/二次生成图片

## 流程图范围与边界
- 仅覆盖“触发 + 路由”与关键 I/O、异常分支
- 不展开 A1~A6 各阶段内部 steps/quality_gates 的细节
- 前置依赖采用抽象校验节点表示（例如 S2 依赖 S1 文档）

## 更新规则
- metadata.json 变更 trigger 时，需要同步更新流程图触发节点文案
- manifest/index.yaml 变更 stage 路由时，需要同步更新路由节点与指向的子 skill
- docs_dir_naming 模板变更时，需要同步更新 docs_dir_naming 节点文案

