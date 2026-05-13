# 资源发布方案

## 一、发布原则

1. `docs/` 只放网页正文。
2. `assets/` 放附件资源源文件。
3. `content/` 放资源清单和结构化元数据。
4. 构建前将 `assets/` 同步到 `docs/assets/`，供 MkDocs 发布。
5. 考试保密资料不得进入 `docs/`、`assets/`、`content/` 或 `build/`。

## 二、资源分类

| 类别 | 源目录 | 网站页面 |
|---|---|---|
| 电子教材 PDF | `assets/textbook/` | `docs/textbook/index.md` |
| 课程 PPT PDF | `assets/slides/` | `docs/lessons/*.md` |
| 作业附件 | `assets/assignments/` | `docs/assignments/*.md` |
| 教材附图 | `assets/figures/textbook/` | `docs/resources/textbook_figures.md` |
| 过程产物 | `assets/process/` | `docs/resources/process_artifacts.md` |
| 模板文件 | `assets/downloads/templates/` | `docs/resources/templates.md` |
| 参考书目 | `assets/references/` | `docs/resources/reference_books.md` |

## 三、资源清单

资源清单文件：

```text
content/resources/resources_manifest.yml
```

字段包括：

- title
- category
- file
- preview_type
- public
- description
- source
- note

## 四、不公开资料

以下资料不进入学生网站：

- 正式试卷；
- 教师题库；
- 教师阅卷标准；
- answer_key；
- teacher_only；
- 命题质量分析；
- AB卷难度分析；
- 平时成绩教师评分材料。

## 五、后续更新流程

1. 更新源文件；
2. 运行对应构建脚本；
3. 运行编码检查；
4. 运行泄密检查；
5. 运行 `mkdocs build --strict`；
6. 发布 `site/build/`。
