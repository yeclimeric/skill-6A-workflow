# Skill 名称
6A研发全流程管控

## 描述（Description）
将研发需求按6A阶段输出结构化交付物，阶段：A1-Align/A2-Architect/A3-Atomize/A4-Approve/A5-Automate/A6-Assess。

## 触发条件（When to use）
输入以“6A”开头的研发需求、研发任务、缺陷修复、重构请求。

## 不使用场景（When NOT to use）
- 非软件研发交付（纯运营/纯设计/纯法务）
- 违法违规、涉密、绕过安全控制、索取密钥/账号
- 缺少repo_root/task_name/raw_requirement且拒绝补充

## 输入（Input）
- repo_root: string，绝对路径
- task_name: string，长度1-64，不含/和\
- raw_requirement: string，长度1-20000
- stage: enum，S1/S2/S3/S4/S5/S6（按阶段子skill要求）

## 执行指示（Instructions）
- 目录命名规则：resources/manifest/common/docs_dir_naming.yaml
- 阶段清单索引：resources/manifest/index.yaml
- 阶段规范与步骤：resources/prompt.md

## 输出（Output）
- docs_dir: string，绝对路径，格式6A-seq-stage_full_taskname
- generated_files: array，生成的阶段文档路径列表

## 注意事项（Notes）
- API密钥等敏感信息使用.env文件管理
- 代码变更同步更新docs交付物
