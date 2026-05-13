# 网站部署方案审阅

## 一、可选部署方式

| 方案 | 优点 | 风险 |
|---|---|---|
| GitHub Pages | 部署简单，适合公开课程展示 | 仓库若公开，必须确保不提交保密资料 |
| Gitee Pages | 国内访问较稳定 | 平台功能和同步流程需确认 |
| 学校服务器 | 可控性强，适合校内课程发布 | 需要服务器权限和上传流程 |
| 学校课程平台附件 | 最稳妥，适合只发布静态包 | 页面体验取决于平台支持 |

## 二、推荐方案

优先推荐：学校服务器或课程平台静态包。

如果需要公开展示课程建设成果，可使用 GitHub Pages，但必须使用学生网站专用仓库，不能把 `exam/`、教师命题材料、教师版教材等保密资料提交到仓库。

## 三、部署前必须执行

```powershell
python scripts\convert_txt_to_md.py
python scripts\build_textbook_pages.py
python scripts\build_resource_pages.py
python scripts\build_assignment_pages.py
python scripts\build_pdf_viewer_pages.py
python scripts\normalize_text_encoding.py
python scripts\check_private_leak.py
python -m mkdocs build --clean --strict
```

## 四、发布物

只发布：

```text
site/build/
```

不发布：

- `exam/`
- `textbook/` 源工程；
- `input/lessons/` 教师讲稿；
- 教师版答案与评分材料。
