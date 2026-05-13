# 学生网站禁止公开资产清单

本清单列出不得进入学生端网站的资料。原则上，凡是不能确认公开安全的材料，一律不复制到 `site/docs/` 或 `site/public/`。

## 一、考试资料：整体禁止公开

`exam/` 目录整体默认保密。以下文件不得发布到学生网站。

### 1.1 A/B 卷与试卷源文件

禁止公开：

- `exam/paper_A.md`
- `exam/paper_B.md`
- `exam/paper_A_teacher_source.md`
- `exam/paper_B_teacher_source.md`
- `exam/paper_A_teacher_source_v2.md`
- `exam/paper_B_teacher_source_v2.md`
- `exam/paper_A_teacher_source_v3.md`
- `exam/paper_B_teacher_source_v3.md`
- `exam/output/软件体系结构_期末试卷A_学生作答版*.docx`
- `exam/output/软件体系结构_期末试卷A_学生作答版*.pdf`
- `exam/output/软件体系结构_期末试卷B_学生作答版*.docx`
- `exam/output/软件体系结构_期末试卷B_学生作答版*.pdf`

说明：即使是“学生作答版”，仍属于正式考试材料，不得公开。

### 1.2 答案与评分细则

禁止公开：

- `exam/answer_key.md`
- `exam/answer_key_A_teacher_only.md`
- `exam/answer_key_B_teacher_only.md`
- `exam/answer_key_A_teacher_only_v2.md`
- `exam/answer_key_B_teacher_only_v2.md`
- `exam/answer_key_A_teacher_only_v3.md`
- `exam/answer_key_B_teacher_only_v3.md`
- `exam/output/软件体系结构_期末试卷A_答案与评分细则_教师版*.docx`
- `exam/output/软件体系结构_期末试卷A_答案与评分细则_教师版*.pdf`
- `exam/output/软件体系结构_期末试卷B_答案与评分细则_教师版*.docx`
- `exam/output/软件体系结构_期末试卷B_答案与评分细则_教师版*.pdf`

### 1.3 题库、命题蓝图与命题质量分析

禁止公开：

- `exam/question_bank.md`
- `exam/question_bank_teacher_only.md`
- `exam/exam_blueprint.md`
- `exam/exam_blueprint_100.md`
- `exam/exam_quality_review_teacher_only.md`
- `exam/exam_scope_note_teacher_only.md`
- `exam/output/软件体系结构_命题质量分析报告_教师版.*`
- `exam/output/AB卷难度等价性审查报告_v2.md`
- `exam/output/AB卷四大题结构命题质量审查报告_v3.*`
- `exam/output/exam_generation_final_checklist.md`
- `exam/output/exam_generation_validation_log*.md`

说明：公开复习说明必须另行生成，不能直接使用教师版考试范围说明。

### 1.4 平时成绩教师评分方案

禁止公开：

- `exam/process_assessment_plan_100.md`
- `exam/output/软件体系结构_平时成绩100分评价方案_教师版.docx`
- `exam/output/软件体系结构_平时成绩100分评价方案_教师版.pdf`

学生端可以发布课程项目要求，但不发布教师评分细则。

## 二、教材教师版与内部版本

禁止公开：

- `textbook/output/software_architecture_textbook_teacher_v5.docx`
- `textbook/output/software_architecture_textbook_teacher_v5.pdf`
- `textbook/chapters_source/`
- `textbook/chapters_v4/` 中未确认学生版的源文件；
- `textbook/review/`
- `textbook/output/*preview*/`
- `textbook/output/*generation*`
- 任何包含 `source`、`teacher`、`教师`、`review`、`audit`、`quality` 的教材内部材料。

说明：学生端只使用最终学生阅读版 PDF。

## 三、每次课教师材料

以下材料默认不公开：

- `input/lessons/lesson*/speaker_script.md`
- `input/lessons/lesson*/speaker_script.docx`
- `input/lessons/lesson*/speaker_script.pdf`
- `input/lessons/lesson*/ppt.pptx`

说明：

- 逐字讲稿属于教师授课参考，不作为学生网站资料。
- PPTX 属于可编辑源文件，可能包含未清理的备注或结构信息；学生端优先公开 PDF。
- 如需公开 PPTX，必须单独审查后再发布。

## 四、工程中间文件与调试材料

禁止公开：

- `debug/`
- `output/*review*`
- `output/*audit*`
- `output/*fix*`
- `scripts/`
- `prompts/`
- 任何生成脚本、校验报告、诊断报告、布局报告、预览 montage。

这些文件属于课程建设工程材料，不属于学生学习资料。

## 五、文件名敏感规则

后续构建前，建议扫描 `site/docs/` 和 `site/public/`。凡文件路径或文件名包含以下关键词，一律阻断发布，除非人工确认：

```text
exam
teacher
teacher_only
教师
教师版
答案
评分
试卷
题库
命题
answer
answer_key
paper_A
paper_B
source
debug
audit
review
quality
fix_report
validation_log
```

## 六、特殊说明

1. 公开复习资料只能是“范围与复习方向”，不能包含正式试题、题库、答案或评分点。
2. 学生作答版试卷虽然不含答案，但仍属于考试保密资料，不能公开。
3. 平时成绩评价方案中的教师评分细则不能公开，可改写为学生版项目提交要求。
4. 网站构建脚本不得从 `exam/` 目录复制任何文件。
