# 网站体验优化计划

## 一、优化目标

将当前网站从“资料下载目录”升级为“学生端课程学习平台”。

优化后应满足：

1. 首页能快速说明课程价值与学习路径；
2. 电子教材和每次课 PPT 可在线预览；
3. 作业要求在网页正文中直接可读；
4. M1-M4 项目任务清楚、可执行；
5. 补充资料按主题分类；
6. 视觉风格更接近课程 PPT：深蓝主色、橙色强调、浅蓝/浅灰卡片；
7. 无考试保密资料泄露；
8. `mkdocs build --strict` 通过。

## 二、修复步骤

### 阶段1：编码规范化

新增 `scripts/normalize_text_encoding.py`：

- 扫描 `docs/` 与 `public/` 下 `.txt`、`.md` 文件；
- 自动识别 UTF-8、UTF-8 BOM、GBK、GB18030、ANSI 等常见编码；
- 统一转换为 UTF-8；
- 输出 `site/review/text_encoding_fix_report.md`。

### 阶段2：资源页面构建

新增 `scripts/build_resource_pages.py`：

- 为电子教材与每次课 PPT 插入 iframe 预览；
- 每个页面保留下载按钮；
- 作业要求直接写入页面正文；
- 项目模板内容直接展示在网页中；
- 输出 `site/review/resource_preview_fix_report.md`。

### 阶段3：视觉升级

新增或更新：

- `docs/stylesheets/extra.css`
- `docs/index.md`
- `docs/textbook.md`
- `docs/lessons/*.md`
- `docs/project/*.md`
- `docs/resources.md`
- `mkdocs.yml`

重点改进：

- 首页 Hero；
- 四个入口卡片；
- 学习路径；
- 资源按钮；
- PDF 预览框；
- 课次页面统一模块；
- 项目页面提交材料卡片。

### 阶段4：泄密检查

更新保密扫描输出到：

- `site/review/private_file_leak_check.md`

扫描范围：

- `site/docs/`
- `site/public/`
- `site/build/`

原则：

- 只发布学生可公开资料；
- 不发布任何试卷、答案、题库、教师版评分材料。

### 阶段5：构建验收

运行：

```powershell
python scripts/normalize_text_encoding.py
python scripts/build_resource_pages.py
python scripts/validate_public_assets.py
python -m mkdocs build --clean --strict
```

输出：

- `site/review/site_build_report.md`
- `site/review/site_release_checklist.md`

## 三、修复后的页面结构

| 页面 | 主要改进 |
|---|---|
| 首页 | Hero + 入口卡片 + 学习路径 + 重点资源 |
| 课程说明 | 目标、学习方式、考核公开说明 |
| 电子教材 | 在线预览 + 下载按钮 + 每章简介 |
| lesson01-lesson08 | PPT 预览 + 作业正文 + 教材章节 + 课堂任务 |
| 项目 M1-M4 | 提交材料、格式要求、模板、质量关注点 |
| 补充资料 | 主题分类，不再平铺 |
| 复习说明 | 公开范围和复习建议，不泄露试题 |

## 四、风险控制

1. 不从 `exam/` 目录复制任何文件；
2. 不把 PPTX 作为学生端预览资源；
3. 不公开教师版 DOCX/PDF；
4. 不公开逐字讲稿；
5. 不公开题库、答案、评分细则、命题质量报告；
6. 所有 PDF 预览只引用 `site/docs/public/` 中的白名单资源。

## 五、预期结果

完成后，网站应能作为学生端课程平台使用，而不是只作为文件下载列表。
