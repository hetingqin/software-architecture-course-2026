# 学生端课程网站生成报告

## 生成内容

| 类型 | 文件/目录 |
|---|---|
| MkDocs 配置 | `site/mkdocs.yml` |
| 页面源码 | `site/docs/` |
| 公开资产源目录 | `site/public/` |
| MkDocs 可发布资产镜像 | `site/docs/public/` |
| 本地预览说明 | `site/README.md` |
| 泄密检查报告 | `site/private_file_leak_check.md` |

## 已生成页面

- 首页：`docs/index.md`
- 课程说明：`docs/syllabus.md`
- 电子教材：`docs/textbook.md`
- 每次课：`docs/lessons/lesson01.md` 至 `lesson08.md`
- 课程项目：`docs/project/`
- 补充资料：`docs/resources.md`
- 复习说明：`docs/review.md`

## 已复制公开资料

| 课次 | 主题 | 资料 |
|---|---|---|
| 第01讲 | 从能写代码到能控复杂系统 | PPT PDF + 作业 |
| 第02讲 | 软件过程模型与开发节奏选择 | PPT PDF + 作业 |
| 第03讲 | 项目管理、可行性分析与风险控制 | PPT PDF + 作业 |
| 第04讲 | 需求工程：从用户声音到可验证规格 | PPT PDF + 作业 |
| 第05讲 | 架构表达与系统建模 | PPT PDF + 作业 |
| 第06讲 | 架构设计、架构风格与分布式系统 | PPT PDF + 作业 |
| 第07讲 | 软件测试、质量保障与安全验证 | PPT PDF + 作业 |
| 第08讲 | 发布、交付、运维与可观测性 | PPT PDF + 作业 |

电子教材：

- `textbook/output/software_architecture_textbook_student_v5_1.pdf`

## 处理说明

1. `lesson03` 已由 PowerPoint COM 从 PPTX 导出为 PDF 后纳入网站。
2. 站点只生成 lesson01 至 lesson08 页面；lesson09 可后续作为专题补充加入。
3. `site/public/` 按用户要求保存公开资产；`site/docs/public/` 是 MkDocs 构建可访问镜像。
4. 未复制 `exam/` 下任何文件。
5. 未复制 `teacher_only`、`answer_key`、`paper_A`、`paper_B`、教师版答案与评分细则等考试保密资料。
