# PPT 在线预览修复报告

## 问题定位

PPT PDF 文件本身可以访问，但在课程页面中使用浏览器 PDF 插件嵌入预览时，Chrome 只显示 PDF 占位图和 `Open` 按钮，无法直接阅读。

这不是 PDF 文件缺失，也不是 MkDocs 插件问题，而是浏览器内置 PDF Viewer 在 iframe / embed 场景中的兼容性问题。

## 修复方案

将 PPT 在线预览从“iframe 嵌入 PDF”改为“PDF 渲染为逐页 JPG 图片后网页直接展示”。

修复内容：

- 修改 `scripts/build_pdf_viewer_pages.py`；
- 使用 PyMuPDF 将 `assets/slides/lessonXX.pdf` 渲染为 `assets/slides_preview/lessonXX/slide-XXX.jpg`；
- 每次课页面直接显示逐页图片预览；
- 保留“下载 PDF”和“新窗口打开”按钮；
- 移除页面中的 `<iframe>` 预览。

## 本地验证

第2讲页面：

- `http://127.0.0.1:8000/lessons/lesson02/` 返回 200；
- 页面不再包含 iframe；
- `../../assets/slides_preview/lesson02/slide-001.jpg` 返回 200；
- 第2讲共生成 46 页预览图。

## 全部预览页数

- 第01讲：45 页
- 第02讲：46 页
- 第03讲：45 页
- 第04讲：8 页
- 第05讲：45 页
- 第06讲：14 页
- 第07讲：16 页
- 第08讲：50 页

## GitHub Pages 兼容性

预览图使用页面相对路径，例如：

```html
../../assets/slides_preview/lesson02/slide-001.jpg
```

该路径同时兼容本地 `127.0.0.1:8000` 和 GitHub Pages 项目站点路径。
