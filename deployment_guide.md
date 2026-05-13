# 《软件体系结构》课程网站部署指南

## 一、本地预览

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

访问：

```text
http://127.0.0.1:8000/
```

## 二、本地构建

```powershell
python -m mkdocs build --clean --strict
```

输出目录：

```text
site/build/
```

## 三、GitHub Pages 发布

### 方案A：mkdocs gh-deploy

```powershell
cd site
python scripts\check_private_leak.py
python -m mkdocs gh-deploy --clean
```

注意：

- 只可使用学生端网站仓库；
- 不得提交 `exam/`、教师题库、试卷、教师阅卷材料；
- 发布前必须运行 `check_private_leak.py`。

### 方案B：GitHub Actions

可配置 Actions 在 push 后运行：

```text
pip install mkdocs-material
python scripts/check_private_leak.py
mkdocs build --strict
```

再将 `site/build/` 发布到 Pages。

## 四、学校服务器发布

1. 本地运行全部构建脚本；
2. 运行 `mkdocs build --clean --strict`；
3. 将 `site/build/` 上传到学校服务器静态目录；
4. 配置 Web 服务指向该目录；
5. 后续更新时重新构建并覆盖上传。

## 五、GitHub Pages 与学校服务器对比

| 方案 | 适合场景 | 优点 | 注意事项 |
|---|---|---|---|
| GitHub Pages | 公开展示课程建设成果 | 自动化方便，访问路径稳定 | 公开仓库必须严格排除保密资料 |
| 学校服务器 | 面向校内学生使用 | 数据边界更可控 | 需要服务器权限和上传流程 |

## 六、推荐部署方案

教学运行期推荐学校服务器或学校课程平台；课程建设展示期可另行发布 GitHub Pages 版本。

## 七、后续更新流程

1. 更新教材、PPT、作业或资源；
2. 运行构建脚本；
3. 运行泄密检查；
4. 本地预览；
5. 构建静态站；
6. 上传 `site/build/`。
