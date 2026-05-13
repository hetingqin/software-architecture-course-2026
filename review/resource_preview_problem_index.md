# 资源预览问题索引

## 一、PDF/PPT 预览问题

| 页面 | 资源 | 当前问题 | 严重程度 | 修复建议 |
|---|---|---|---|---|
| `docs/textbook.md` | 电子教材 PDF | 只提供下载链接，无法页面内阅读 | 高 | 增加 iframe PDF 预览与下载按钮 |
| `docs/lessons/lesson01.md` | 第1讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |
| `docs/lessons/lesson02.md` | 第2讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |
| `docs/lessons/lesson03.md` | 第3讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |
| `docs/lessons/lesson04.md` | 第4讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |
| `docs/lessons/lesson05.md` | 第5讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |
| `docs/lessons/lesson06.md` | 第6讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |
| `docs/lessons/lesson07.md` | 第7讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |
| `docs/lessons/lesson08.md` | 第8讲 PPT PDF | 只提供下载链接 | 高 | 增加 PPT PDF 在线预览 |

## 二、作业要求预览问题

| 页面 | 资源 | 当前问题 | 严重程度 | 修复建议 |
|---|---|---|---|---|
| lesson01-lesson08 | `assignment.txt` | 核心作业以 `.txt` 附件形式存在，浏览器可能乱码 | 中 | 页面正文直接展示作业要求，附件改为 Markdown 或不作为核心入口 |
| `docs/public/lessons/*/assignment.txt` | 作业附件 | 文件可被直接打开，编码由浏览器自行判断 | 中 | 统一 UTF-8，并避免从页面主入口跳转到 raw txt |

## 三、项目模板预览问题

| 页面 | 资源 | 当前问题 | 严重程度 | 修复建议 |
|---|---|---|---|---|
| `docs/project/templates.md` | M1-M4 模板 txt | 链接到 `.txt`，学生打开可能乱码 | 中 | 模板内容直接在网页中展示，同时保留 Markdown 下载 |
| `docs/public/project/*.txt` | 项目模板附件 | 作为 raw txt 存在 | 中 | 转为 UTF-8，新增 `.md` 附件 |

## 四、结构体验问题

| 页面 | 当前问题 | 严重程度 | 修复建议 |
|---|---|---|---|
| `docs/index.md` | 缺少 Hero 区和学习入口卡片 | 中 | 重构首页为课程门户 |
| `docs/resources.md` | 补充资料没有分类资源卡片 | 中 | 按主题分类 |
| `docs/project/*.md` | 页面结构清楚但视觉层级不足 | 中 | 增加阶段标签、提交材料卡片、模板按钮 |

## 五、保密风险索引

当前未发现考试保密资料进入公开目录。

仍需持续检查以下关键词：

- `期末试卷A`
- `期末试卷B`
- `答案`
- `评分细则`
- `教师版`
- `teacher_only`
- `question_bank`
- `answer_key`
- `grading_rubric`
- `exam_quality_review`
- `AB卷难度`
- `命题质量分析`
