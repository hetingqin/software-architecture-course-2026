# 学生网站公开资产清单

本清单只列出建议进入学生端课程网站的公开学习资料。实际复制文件前仍需进行一次保密校验。

## 一、电子教材

| 类型 | 源文件 | 是否公开 | 发布建议 |
|---|---|---:|---|
| 学生阅读版电子教材 PDF | `textbook/output/software_architecture_textbook_student_v5_1.pdf` | 是 | 作为网站“电子教材”主下载文件 |
| 学生阅读版电子教材 DOCX | `textbook/output/software_architecture_textbook_student_v5_1.docx` | 可选 | 默认不公开；如需便于学生批注，可另行确认 |
| 旧版学生教材 | `textbook/output/software_architecture_textbook_student_v3/v4/v5.*` | 否 | 不公开，避免版本混乱 |
| 第6章样章 | `textbook/output/chapter06_illustrated_student_v*.pdf` | 否 | 已被全书教材替代，不单独公开 |

## 二、每次课 PPT 与作业

发布原则：

- PPT 公开优先使用 `ppt.pdf`；
- `ppt.pptx` 默认不公开；
- `assignments.md` 可以公开；
- `outline.md` 可作为教师维护源，是否公开可后续确认；
- `speaker_script.*` 默认不公开。

| 课次 | 建议公开 PPT | 作业要求 | 大纲 | 当前状态 |
|---|---|---|---|---|
| lesson01 | `input/lessons/lesson01/ppt.pdf` | `input/lessons/lesson01/assignments.md` | `input/lessons/lesson01/outline.md` | 可公开 |
| lesson02 | `input/lessons/lesson02/ppt.pdf` | `input/lessons/lesson02/assignments.md` | `input/lessons/lesson02/outline.md` | 可公开 |
| lesson03 | 暂缺 `ppt.pdf` | `input/lessons/lesson03/assignments.md` | `input/lessons/lesson03/outline.md` | 需先由 `ppt.pptx` 导出 PDF |
| lesson04 | `input/lessons/lesson04/ppt.pdf` | `input/lessons/lesson04/assignments.md` | `input/lessons/lesson04/outline.md` | 可公开 |
| lesson05 | `input/lessons/lesson05/ppt.pdf` | `input/lessons/lesson05/assignments.md` | `input/lessons/lesson05/outline.md` | 可公开 |
| lesson06 | `input/lessons/lesson06/ppt.pdf` | `input/lessons/lesson06/assignments.md` | `input/lessons/lesson06/outline.md` | 可公开 |
| lesson07 | `input/lessons/lesson07/ppt.pdf` | `input/lessons/lesson07/assignments.md` | `input/lessons/lesson07/outline.md` | 可公开 |
| lesson08 | `input/lessons/lesson08/ppt.pdf` | `input/lessons/lesson08/assignments.md` | `input/lessons/lesson08/outline.md` | 可公开 |
| lesson09 | `input/lessons/lesson09/ppt.pdf` | `input/lessons/lesson09/assignments.md` | `input/lessons/lesson09/outline.md` | 可作为“AI 与新技术专题”公开 |
| lesson10 | 暂缺 PPT | `input/lessons/lesson10/assignments.md` | `input/lessons/lesson10/outline.md` | 可作为“综合案例与项目汇报”页面，后续补 PPT |

## 三、课程项目与里程碑

建议公开，但需要后续整理为独立页面：

| 项目阶段 | 建议页面 | 内容范围 | 来源建议 |
|---|---|---|---|
| M1 选题与需求分析 | `project/m1.md` | 选题范围、用户与场景、初步需求、提交格式 | lesson01-04 作业与教材第1-4章 |
| M2 建模与结构表达 | `project/m2.md` | 用例、领域对象、UML/C4、最小建模图集 | lesson05 作业与教材第5章 |
| M3 架构决策与 ADR | `project/m3.md` | 架构风格、质量属性、ADR、技术债记录 | lesson06 作业与教材第6章 |
| M4 测试、交付与运维说明 | `project/m4.md` | 测试策略、质量门禁、发布回滚、可观测性 | lesson07-08 作业与教材第7-8章 |

公开项目页面只能说明“学生需要提交什么”和“如何做好”，不公开教师评分细则。

## 四、补充资料与扩展阅读

建议公开：

| 类型 | 建议内容 | 说明 |
|---|---|---|
| AI 时代软件工程专题 | lesson09 PPT PDF、公开作业要求、公开阅读材料 | 不纳入主教材正文，可作为专题扩展 |
| 综合案例与项目汇报说明 | lesson10 作业与汇报要求 | 不涉及考试题 |
| 模板文件 | ADR 模板、技术债记录模板、测试计划模板、交付说明模板 | 建议从学生教材中抽取为可填写版本 |
| 安全阅读材料 | 与课程相关的公开规范、公开白皮书、公开实践资料 | 后续逐项审查后加入 |

## 五、可公开复习说明

当前可规划但尚未生成：

| 文件 | 状态 | 发布规则 |
|---|---|---|
| `review/exam_scope_public.md` | 待生成 | 只说明章节范围、能力要求、复习建议，不含试题、答案、评分点 |

不得直接公开：

- `exam/exam_scope_note_teacher_only.md`
- 任意 A/B 卷；
- 任意题库；
- 任意答案与评分细则。

## 六、建议复制后的公开资产命名

```text
site/docs/assets/textbook/software_architecture_textbook_student_v5_1.pdf
site/docs/assets/lessons/lesson01/ppt.pdf
site/docs/assets/lessons/lesson01/assignment.md
site/docs/assets/lessons/lesson02/ppt.pdf
site/docs/assets/lessons/lesson02/assignment.md
...
site/docs/assets/project/m1_requirements.md
site/docs/assets/project/m2_modeling.md
site/docs/assets/project/m3_adr.md
site/docs/assets/project/m4_testing_delivery.md
```

## 七、当前不完整项

1. `lesson03/ppt.pdf` 缺失，建议补导出。
2. `lesson10/ppt.pdf` 缺失，建议后续确认是否需要课件下载。
3. 可公开复习说明尚未生成。
4. 项目模板尚未从教材中抽取为独立下载文件。
