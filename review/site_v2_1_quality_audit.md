# 课程网站 v2.1 质量审阅报告

## 一、总体评价

v2.1 升级前，网站已经能发布电子教材、PPT、作业和项目材料，但仍存在“附件下载站”倾向。主要问题是电子教材不能按章节直接阅读，PDF 预览依赖浏览器插件，作业附件以 TXT 形式存在，补充资料没有资源中心结构。

本次 v2.1 的核心判断是：学生端网站应以网页正文阅读为主，以 PDF/附件下载为辅。

## 二、问题定位

| 问题 | 原因 | 处理策略 |
|---|---|---|
| `/textbook/` 不能直接阅读教材正文 | 原页面只嵌入完整 PDF，没有章节 Markdown | 使用已有教材 Markdown 源生成 `docs/textbook/chapter01.md` 至 `chapter08.md` |
| PDF 预览依赖浏览器默认插件 | iframe 预览本质仍依赖浏览器 PDF 能力 | 保留 PDF 新窗口/下载，但主要阅读改为 Markdown 正文 |
| 作业 TXT 在线预览可能乱码 | 浏览器打开 raw txt 时编码判断不稳定 | 作业要求生成 `docs/assignments/*.md` 正文页面，TXT 仅作为附件 |
| 部分页面只有下载链接 | 资源没有被整理为学习页面 | 生成教材章节页、作业页、资源中心页 |
| 补充资料分类不足 | 原 `resources.md` 是单页说明 | 重构为 `docs/resources/` 资源中心 |
| 附件与网页混放 | 旧结构使用 `docs/public/` 和 `site/public/` | 改为 `site/assets/` 放附件源，构建时同步到 `docs/assets/` |
| 考试资料泄露风险 | 后续发布资源容易误复制 | 增加 `check_private_leak.py`，扫描 `docs/assets/content/build` |

## 三、结构审阅结果

新结构已调整为：

```text
site/
├─ docs/        # 网页正文
├─ assets/      # 附件资源源目录
├─ content/     # 资源清单
├─ scripts/     # 构建与检查脚本
└─ mkdocs.yml
```

说明：MkDocs 只发布 `docs_dir` 内资源，因此 `site/assets/` 会在构建前同步到 `site/docs/assets/`。`site/docs/assets/` 是构建镜像，不作为正文编辑入口。

## 四、保密审阅

已检查以下敏感类型：

- 试卷A / 试卷B；
- answer_key；
- teacher_only；
- question_bank；
- grading_rubric；
- exam_quality_review；
- 命题质量分析；
- AB卷难度；
- 平时成绩教师评分材料。

当前未发现考试保密资料进入学生网站发布目录。

## 五、结论

v2.1 已具备学生端课程平台形态：教材可网页阅读，作业可网页阅读，PPT 可预览和下载，补充资料形成资源中心，站点具备本地构建和线上部署条件。
