# 《软件体系结构》学生端课程网站

## 本地预览

```powershell
cd D:\Codex\SoftwareArchitecture2026\software-architecture-course-2026\site
python scripts\convert_txt_to_md.py
python scripts\build_textbook_pages.py
python scripts\build_resource_pages.py
python scripts\build_assignment_pages.py
python scripts\build_pdf_viewer_pages.py
python scripts\normalize_text_encoding.py
python scripts\check_private_leak.py
python -m mkdocs serve
```

浏览器访问：

```text
http://127.0.0.1:8000
```

## 构建静态站点

```powershell
cd D:\Codex\SoftwareArchitecture2026\software-architecture-course-2026\site
python scripts\convert_txt_to_md.py
python scripts\build_textbook_pages.py
python scripts\build_resource_pages.py
python scripts\build_assignment_pages.py
python scripts\build_pdf_viewer_pages.py
python scripts\normalize_text_encoding.py
python scripts\check_private_leak.py
python -m mkdocs build --clean
```

构建结果位于：

```text
site/build/
```

## 发布说明

发布前必须先运行：

```powershell
python scripts/check_private_leak.py
```

如果出现考试资料、教师版资料、答案、评分细则、题库等敏感文件，必须删除后再发布。

## GitHub Pages 发布

本目录已经按 GitHub Pages 项目仓库准备：

- `.github/workflows/deploy.yml`：推送到 `main` 后自动构建并发布；
- `requirements.txt`：GitHub Actions 构建依赖；
- `.gitignore`：排除本地构建目录和缓存。

如果使用 GitHub CLI：

```powershell
cd D:\Codex\SoftwareArchitecture2026\software-architecture-course-2026\site
git init
git branch -M main
git add .
git commit -m "Publish software architecture course site"
gh repo create software-architecture-course-2026 --public --source . --remote origin --push
```

如果已经在 GitHub 上创建仓库：

```powershell
cd D:\Codex\SoftwareArchitecture2026\software-architecture-course-2026\site
git remote add origin https://github.com/<your-account>/software-architecture-course-2026.git
git push -u origin main
```

发布后，在 GitHub 仓库 `Settings -> Pages` 中选择 `GitHub Actions` 作为发布来源。

## 质量优化脚本

```powershell
python scripts\normalize_text_encoding.py
python scripts\check_private_leak.py
python -m mkdocs build --clean --strict
```

- `convert_txt_to_md.py`：将作业源文件转换为 UTF-8 Markdown/TXT 附件。
- `build_textbook_pages.py`：生成第1-8章教材在线阅读页面。
- `build_resource_pages.py`：生成补充资料中心、资源清单和项目页。
- `build_assignment_pages.py`：生成每次课作业正文页面。
- `build_pdf_viewer_pages.py`：生成课程课件页面和 MkDocs 配置。
- `normalize_text_encoding.py`：统一 `.txt`、`.md` 编码为 UTF-8。
- `check_private_leak.py`：检查公开目录是否误放考试保密资料。
