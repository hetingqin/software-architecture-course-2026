from __future__ import annotations

import shutil
from pathlib import Path

import fitz


SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent
DOCS = SITE / "docs"
ASSETS = SITE / "assets"
REVIEW = SITE / "review"


LESSONS = {
    1: ("从能写代码到能控复杂系统", "写代码解决局部问题，架构控制系统复杂性。", "第1章 从能写代码到能控复杂系统"),
    2: ("软件过程模型与开发节奏选择", "复杂性来源不同，开发节奏不能相同。", "第2章 软件过程模型与开发节奏选择"),
    3: ("项目管理、可行性分析与风险控制", "技术上可以做，不代表工程上做得成。", "第3章 项目管理、可行性分析与风险控制"),
    4: ("需求工程：从用户声音到可验证规格", "需求不是功能清单，而是把真实问题翻译成工程决策输入。", "第4章 需求工程：从用户声音到可验证规格"),
    5: ("架构表达与系统建模", "图不是装饰，而是团队对系统结构形成共识的工程工具。", "第5章 架构表达与系统建模"),
    6: ("架构设计、架构风格与分布式系统", "架构设计不是选流行技术，而是在约束下做结构决策。", "第6章 架构设计、架构风格与分布式系统"),
    7: ("软件测试、质量保障与安全验证", "质量不是最后测出来的，而是在边界、依赖和门禁中被设计出来的。", "第7章 软件测试、质量保障与安全验证"),
    8: ("发布、交付、运维与可观测性", "开发完成不等于上线成功，系统必须能发布、能回滚、能观察、能复盘。", "第8章 发布、交付、运维与可观测性"),
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def copy_file(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def copy_slides() -> list[str]:
    copied = []
    for lesson in range(1, 9):
        src = ROOT / "input" / "lessons" / f"lesson{lesson:02d}" / "ppt.pdf"
        dst = ASSETS / "slides" / f"lesson{lesson:02d}.pdf"
        if copy_file(src, dst):
            copied.append(dst.relative_to(SITE).as_posix())
    return copied


def render_slide_previews() -> dict[int, int]:
    preview_root = ASSETS / "slides_preview"
    if preview_root.exists():
        shutil.rmtree(preview_root)
    preview_root.mkdir(parents=True, exist_ok=True)

    page_counts: dict[int, int] = {}
    zoom = 1.35
    matrix = fitz.Matrix(zoom, zoom)
    for lesson in range(1, 9):
        pdf = ASSETS / "slides" / f"lesson{lesson:02d}.pdf"
        if not pdf.exists():
            page_counts[lesson] = 0
            continue
        lesson_dir = preview_root / f"lesson{lesson:02d}"
        lesson_dir.mkdir(parents=True, exist_ok=True)
        doc = fitz.open(pdf)
        try:
            page_counts[lesson] = doc.page_count
            for index, page in enumerate(doc, start=1):
                pix = page.get_pixmap(matrix=matrix, alpha=False)
                image = ImageFromPixmap(pix)
                image.save(
                    lesson_dir / f"slide-{index:03d}.jpg",
                    format="JPEG",
                    quality=78,
                    optimize=True,
                    progressive=True,
                )
        finally:
            doc.close()
    return page_counts


class ImageFromPixmap:
    def __init__(self, pix: fitz.Pixmap):
        from PIL import Image

        self.image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    def save(self, path: Path, **kwargs: object) -> None:
        self.image.save(path, **kwargs)


def sync_assets_to_docs() -> None:
    dst = DOCS / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    if ASSETS.exists():
        shutil.copytree(ASSETS, dst)


def pdf_block(src: str, title: str, lesson: int, page_count: int) -> str:
    if page_count <= 0:
        preview = '<div class="preview-empty">本讲 PPT 预览图暂未生成，请先下载 PDF 查看。</div>'
    else:
        images = "\n".join(
            f'''  <figure class="slide-preview-card">
    <img src="../../assets/slides_preview/lesson{lesson:02d}/slide-{page:03d}.jpg" alt="{title} 第{page}页" loading="lazy">
    <figcaption>第 {page} 页</figcaption>
  </figure>'''
            for page in range(1, page_count + 1)
        )
        preview = f'<div class="slide-preview-grid">\n{images}\n</div>'
    return f"""
<div class="resource-actions">
  <a class="md-button md-button--primary" href="{src}" target="_blank">下载 PDF</a>
  <a class="md-button" href="{src}" target="_blank">新窗口打开</a>
</div>

{preview}
""".strip()


def assignment_text(lesson: int) -> str:
    p = ASSETS / "assignments" / f"lesson{lesson:02d}_assignment.md"
    if not p.exists():
        return "本讲作业要求待补充。"
    text = p.read_text(encoding="utf-8", errors="ignore")
    return "\n".join(line for line in text.splitlines() if not line.startswith("# ")).strip()


def build_pages(page_counts: dict[int, int]) -> None:
    rows = []
    for lesson, (title, core, chapter) in LESSONS.items():
        rows.append(f"| [第{lesson:02d}讲](lesson{lesson:02d}.md) | {title} | {chapter} |")
        # Lesson pages are built under /lessons/lessonXX/. The preview uses raw
        # HTML, so paths are explicit relative paths for both local preview and
        # GitHub Pages project-site deployment.
        slide = f"../../assets/slides/lesson{lesson:02d}.pdf"
        assignment_page = f"../assignments/lesson{lesson:02d}_assignment.md"
        write(
            DOCS / "lessons" / f"lesson{lesson:02d}.md",
            f"""# 第{lesson:02d}讲 {title}

<span class="tag">PPT</span><span class="tag">作业</span><span class="tag">{chapter}</span>

## 本讲核心问题

{core}

## 学习目标

- 理解本讲核心概念和判断规则；
- 能把本讲方法应用到课程项目；
- 能围绕案例说明工程取舍。

## PPT 在线预览

{pdf_block(slide, f"第{lesson:02d}讲 PPT", lesson, page_counts.get(lesson, 0))}

## 对应教材章节

{chapter}

## 课堂任务

结合小组项目讨论本讲方法如何落地，并记录一条可执行改进。

## 课后作业

<div class="assignment-box">
{assignment_text(lesson)}
</div>

[查看完整作业页面]({assignment_page})

## 补充资料

可结合 [电子教材](../textbook/chapter{lesson:02d}.md) 与 [补充资料中心](../resources/index.md) 复习。
""",
        )
    write(
        DOCS / "lessons" / "index.md",
        "# 课程课件\n\n每次课页面均包含 PPT 在线预览、下载入口、作业正文和对应教材章节。\n\n"
        "| 课次 | 主题 | 对应教材 |\n|---|---|---|\n" + "\n".join(rows),
    )


def write_home_and_syllabus() -> None:
    write(
        DOCS / "index.md",
        """<div class="sa-hero">
  <div class="eyebrow">SOFTWARE ARCHITECTURE 2026</div>
  <h1>软件体系结构：从能写代码到能控复杂系统</h1>
  <p>学生端课程学习平台，集中提供电子教材、课程课件、课程项目、补充资料和公开复习说明。</p>
</div>

## 学习入口

<div class="card-grid">
<div class="course-card"><h3>电子教材</h3><p>第1-8章网页正文阅读版与完整 PDF。</p><a class="card-link" href="textbook/">进入</a></div>
<div class="course-card"><h3>课程课件</h3><p>第1-8讲 PPT 在线预览、下载与作业。</p><a class="card-link" href="lessons/">进入</a></div>
<div class="course-card"><h3>课程项目</h3><p>M1-M4 阶段任务、提交材料和模板。</p><a class="card-link" href="project/">进入</a></div>
<div class="course-card"><h3>补充资料</h3><p>教材附图、过程产物、模板和参考书目。</p><a class="card-link" href="resources/">进入</a></div>
</div>

## 学习路径

<div class="learning-path">
<div class="path-step">复杂性识别</div>
<div class="path-step">过程治理</div>
<div class="path-step">需求工程</div>
<div class="path-step">架构表达</div>
<div class="path-step">架构决策</div>
<div class="path-step">质量验证</div>
<div class="path-step">发布运维</div>
</div>

!!! warning "公开边界"
    本站不发布试卷、教师题库、教师阅卷标准、命题质量分析等考试保密资料。
""",
    )
    rows = "\n".join(
        f"| 第{lesson:02d}讲 | {title} | {chapter} |"
        for lesson, (title, _, chapter) in LESSONS.items()
    )
    write(
        DOCS / "syllabus.md",
        f"""# 课程说明

## 课程目标

本课程训练学生从“能写代码”提升到“能控制复杂软件系统”。课程关注需求、过程、项目管理、建模、架构决策、质量保障和交付运维。

## 教学安排

| 课次 | 主题 | 对应教材 |
|---|---|---|
{rows}

## 学习方式

- 课前阅读对应教材章节；
- 课堂结合 PPT、案例和任务理解方法；
- 课后完成作业并推进课程项目；
- 期末复习以教材第1-8章、PPT 和项目材料为主。

## 公开考核说明

课程评价重视平时学习、课程项目和期末复习。本站只提供公开学习资料，不发布考试保密材料。
""",
    )


def build_mkdocs() -> None:
    write(
        SITE / "mkdocs.yml",
        """site_name: 软件体系结构课程网站
site_description: 《软件体系结构》学生端课程学习平台
site_author: 何庭钦
docs_dir: docs
site_dir: build
use_directory_urls: true
not_in_nav: |
  assets/**/*.md

theme:
  name: material
  language: zh
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - toc.integrate
    - search.highlight
    - content.code.copy
  palette:
    - scheme: default
      primary: indigo
      accent: orange

extra_css:
  - stylesheets/extra.css

nav:
  - 首页: index.md
  - 课程说明: syllabus.md
  - 电子教材:
      - 教材首页: textbook/index.md
      - 第1章: textbook/chapter01.md
      - 第2章: textbook/chapter02.md
      - 第3章: textbook/chapter03.md
      - 第4章: textbook/chapter04.md
      - 第5章: textbook/chapter05.md
      - 第6章: textbook/chapter06.md
      - 第7章: textbook/chapter07.md
      - 第8章: textbook/chapter08.md
  - 课程课件:
      - 课件总览: lessons/index.md
      - 第1讲: lessons/lesson01.md
      - 第2讲: lessons/lesson02.md
      - 第3讲: lessons/lesson03.md
      - 第4讲: lessons/lesson04.md
      - 第5讲: lessons/lesson05.md
      - 第6讲: lessons/lesson06.md
      - 第7讲: lessons/lesson07.md
      - 第8讲: lessons/lesson08.md
  - 课后作业:
      - 作业总览: assignments/index.md
      - 第1讲作业: assignments/lesson01_assignment.md
      - 第2讲作业: assignments/lesson02_assignment.md
      - 第3讲作业: assignments/lesson03_assignment.md
      - 第4讲作业: assignments/lesson04_assignment.md
      - 第5讲作业: assignments/lesson05_assignment.md
      - 第6讲作业: assignments/lesson06_assignment.md
      - 第7讲作业: assignments/lesson07_assignment.md
      - 第8讲作业: assignments/lesson08_assignment.md
  - 课程项目:
      - M1 选题与需求: project/m1.md
      - M2 建模与结构表达: project/m2.md
      - M3 架构决策与 ADR: project/m3.md
      - M4 测试交付与运维: project/m4.md
  - 补充资料:
      - 资源中心: resources/index.md
      - 教材附图: resources/textbook_figures.md
      - 过程产物: resources/process_artifacts.md
      - 模板文件: resources/templates.md
      - 参考书目: resources/reference_books.md
  - 复习说明: review/final_review_guide.md

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tasklist:
      custom_checkbox: true

extra:
  generator: false
""",
    )


def main() -> int:
    copied = copy_slides()
    page_counts = render_slide_previews()
    sync_assets_to_docs()
    build_pages(page_counts)
    write_home_and_syllabus()
    build_mkdocs()
    REVIEW.mkdir(parents=True, exist_ok=True)
    counts = "\n".join(f"- 第{lesson:02d}讲：{count} 页" for lesson, count in page_counts.items())
    write(
        REVIEW / "pdf_viewer_page_report.md",
        "# PDF 预览页面生成报告\n\n"
        "## PDF 资源\n\n"
        + "\n".join(f"- `{item}`" for item in copied)
        + "\n\n## 图片预览页数\n\n"
        + counts,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
