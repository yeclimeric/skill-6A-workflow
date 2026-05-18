---
name: "skill-6a-workflow"
description: "标准化6A研发全流程管控，产出对齐/架构/拆分/审批/执行/评估交付物。"
version: "1.0.0"
author: "eric"
tags:
  - "6A"
  - "workflow"
  - "software-delivery"
trigger:
  - "6A"
  - "6A工作流"
category: "document"
permissions:
  - "read_file"
  - "write_file"
---


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
- 公共prompt：resources/prompt.md
- 阶段prompt：resources/manifest/A*-*/prompt.md（按stage路由）

## 调用与触发流程图
```mermaid
flowchart TD
  U[用户输入] --> T{是否命中触发词?<br/>metadata.trigger: 6A / 6A工作流}
  T -- 否 --> END0[不触发本Skill]
  T -- 是 --> ACT[激活6A工作流<br/>立即响应: 6A工作流已激活]
  ACT --> IN[解析/收集入参<br/>repo_root task_name raw_requirement stage]
  IN --> V{入参是否满足契约?<br/>contract.input_schema}
  V -- 否 --> E003[异常 E6A003<br/>缺失字段/格式不符<br/>不写入任何文件]
  V -- 是 --> R{repo_root是否存在且可访问?}
  R -- 否 --> E001[异常 E6A001<br/>repo_root无效<br/>不写入任何文件]
  R -- 是 --> IDX[读取阶段索引<br/>resources/manifest/index.yaml]
  IDX --> S{stage路由<br/>S1..S6}

  S -- S1 --> A1[调用A1子skill<br/>A1-Align/skill.yaml]
  S -- S2 --> P2{前置文档齐全?<br/>S1-ALIGNMENT/S1-CONSENSUS}
  P2 -- 否 --> EPR2[异常 E6A003<br/>PREREQ_DOC_MISSING<br/>BLOCKED]
  P2 -- 是 --> A2[调用A2子skill<br/>A2-Architect/skill.yaml]
  S -- S3 --> P3{前置文档齐全?<br/>S2-DESIGN}
  P3 -- 否 --> EPR3[异常 E6A003<br/>PREREQ_DOC_MISSING<br/>BLOCKED]
  P3 -- 是 --> A3[调用A3子skill<br/>A3-Atomize/skill.yaml]
  S -- S4 --> P4{前置文档齐全?<br/>S3-TASKS}
  P4 -- 否 --> EPR4[异常 E6A003<br/>PREREQ_DOC_MISSING<br/>BLOCKED]
  P4 -- 是 --> A4[调用A4子skill<br/>A4-Approve/skill.yaml]
  S -- S5 --> P5{前置文档齐全?<br/>S4-APPROVAL}
  P5 -- 否 --> EPR5[异常 E6A003<br/>PREREQ_DOC_MISSING<br/>BLOCKED]
  P5 -- 是 --> A5[调用A5子skill<br/>A5-Automate/skill.yaml]
  S -- S6 --> P6{前置文档齐全?<br/>S5-EXECUTION}
  P6 -- 否 --> EPR6[异常 E6A003<br/>PREREQ_DOC_MISSING<br/>BLOCKED]
  P6 -- 是 --> A6[调用A6子skill<br/>A6-Assess/skill.yaml]

  A1 --> DDN1[调用docs_dir_naming子skill<br/>模板: 6A-{seq}-{task_name}]
  A2 --> DDN2[调用docs_dir_naming子skill<br/>模板: 6A-{seq}-{task_name}]
  A3 --> DDN3[调用docs_dir_naming子skill<br/>模板: 6A-{seq}-{task_name}]
  A4 --> DDN4[调用docs_dir_naming子skill<br/>模板: 6A-{seq}-{task_name}]
  A5 --> DDN5[调用docs_dir_naming子skill<br/>模板: 6A-{seq}-{task_name}]
  A6 --> DDN6[调用docs_dir_naming子skill<br/>模板: 6A-{seq}-{task_name}]

  DDN1 --> W1[写入阶段文档<br/>docs/{docs_dir}/S1-*.md]
  DDN2 --> W2[写入阶段文档<br/>docs/{docs_dir}/S2-*.md]
  DDN3 --> W3[写入阶段文档<br/>docs/{docs_dir}/S3-*.md]
  DDN4 --> W4[写入阶段文档<br/>docs/{docs_dir}/S4-*.md]
  DDN5 --> W5[写入阶段文档<br/>docs/{docs_dir}/S5-*.md]
  DDN6 --> W6[写入阶段文档<br/>docs/{docs_dir}/S6-*.md]

  W1 --> OUT[返回结果<br/>output_schema: stage docs_dir generated_files]
  W2 --> OUT
  W3 --> OUT
  W4 --> OUT
  W5 --> OUT
  W6 --> OUT
```

## 输出（Output）
- docs_dir: string，绝对路径，格式6A-seq-task_name
- generated_files: array，生成的阶段文档路径列表

## 注意事项（Notes）
- API密钥等敏感信息使用.env文件管理
- 代码变更同步更新docs交付物
