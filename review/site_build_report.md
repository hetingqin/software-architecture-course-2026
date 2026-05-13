# v2.1 本地构建报告

## 构建命令

```powershell
cd D:\Codex\SoftwareArchitecture2026\software-architecture-course-2026\site
python scripts\convert_txt_to_md.py
python scripts\build_textbook_pages.py
python scripts\build_resource_pages.py
python scripts\build_assignment_pages.py
python scripts\build_pdf_viewer_pages.py
python scripts\normalize_text_encoding.py
python scripts\check_private_leak.py
python -m mkdocs build --clean --strict
```

## 构建结果

构建通过。

输出目录：

```text
site/build/
```

## 本次修复点

| 项目 | 结果 |
|---|---|
| 网站目录重构 | 已完成 |
| `docs/` 放网页正文 | 已完成 |
| `assets/` 放附件资源 | 已完成 |
| 电子教材章节在线阅读 | 已完成 |
| 完整教材 PDF 下载 | 已保留 |
| 作业 Markdown 页面 | 已完成 |
| TXT 编码统一 | 已完成 |
| 补充资料资源中心 | 已完成 |
| 教材附图图库 | 已完成 |
| 考试资料泄露检查 | 通过 |
| `mkdocs build --strict` | 通过 |

## 说明

MkDocs 只会发布 `docs_dir` 内文件，因此构建脚本会将 `site/assets/` 同步到 `site/docs/assets/`。`site/assets/` 是附件源目录，`site/docs/assets/` 是构建镜像。
