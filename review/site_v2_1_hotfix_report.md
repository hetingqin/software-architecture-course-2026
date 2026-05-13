# 网站 v2.1 热修复报告

## 修复事项

### 1. PPT 在线预览 404

问题原因：PPT 预览区使用 raw HTML `<iframe>`，MkDocs 对 raw HTML 内的相对路径处理不稳定，页面 `/lessons/lesson02/` 中的 PDF 路径会解析到 `/lessons/assets/slides/lesson02.pdf`，导致 404。

修复方式：

- 修改 `site/scripts/build_pdf_viewer_pages.py`；
- PPT PDF 链接统一使用站点根路径 `/assets/slides/lessonXX.pdf`；
- 重新生成课程课件页面并重启本地预览服务。

验证结果：

- `http://127.0.0.1:8000/lessons/lesson02/` 返回 200；
- iframe 解析到 `http://127.0.0.1:8000/assets/slides/lesson02.pdf`；
- PDF 返回 200。

### 2. 第1章图1-1线条问题

问题原因：原图属于线条关系图，连线与节点文本关系不够清楚，容易形成视觉干扰。

修复方式：

- 新增 `site/scripts/redraw_chapter01_figures.py`；
- 用结构化绘图方式重绘图1-1；
- 四类复杂性来源按“左上、右上、左下、右下”卡片布局；
- 连线采用短边到中心节点的连接方式，避免穿过文字；
- 同步更新教材图源、网站附件和网页引用资源。

修复图源：

- `textbook/figures_fixed/chapter01/student/fig1-1_complexity_sources_native.png`
- `site/assets/figures/textbook/chapter01/student/fig1-1_complexity_sources_native.png`
- `site/docs/assets/figures/textbook/chapter01/student/fig1-1_complexity_sources_native.png`

### 3. 补充资料中心空栏目 / 404

问题原因：资源中心卡片此前使用 `.md` 直链，MkDocs 开启目录式 URL 后容易造成 404；同时入口固定展示，不便于后续隐藏空栏目。

修复方式：

- 修改 `site/scripts/build_resource_pages.py`；
- 资源中心卡片改为目录式链接，如 `textbook_figures/`；
- 卡片生成改为按资源实际存在情况动态显示；
- 项目模板下载 raw HTML 链接改为 `/assets/downloads/templates/...`。

验证结果：

- `/resources/` 返回 200；
- `/resources/textbook_figures/` 返回 200；
- `/project/m1/` 返回 200。

## 构建与安全检查

- `python -m mkdocs build --clean --strict`：通过；
- `python scripts/check_private_leak.py`：通过；
- 未发现考试保密资料进入学生网站目录。

## 使用提醒

如果浏览器仍显示旧 404 页面，请强制刷新页面，或重启本地预览服务：

```powershell
cd D:\Codex\SoftwareArchitecture2026\software-architecture-course-2026\site
python -m mkdocs serve -a 127.0.0.1:8000
```
