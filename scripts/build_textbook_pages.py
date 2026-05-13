from __future__ import annotations

import re
import shutil
from pathlib import Path


SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent
DOCS = SITE / "docs"
ASSETS = SITE / "assets"
REVIEW = SITE / "review"

CHAPTER_SOURCE_DIR = ROOT / "textbook" / "chapters_illustrated_student"
FIGURE_SOURCE_DIR = ROOT / "textbook" / "figures_fixed"
TEXTBOOK_PDF = ROOT / "textbook" / "output" / "software_architecture_textbook_student_v5_1.pdf"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def copy_file(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def sync_assets_to_docs() -> None:
    src = ASSETS
    dst = DOCS / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    if src.exists():
        shutil.copytree(src, dst)


def normalize_chapter_markdown(text: str, chapter_no: int) -> str:
    # Fix generated figure paths from textbook source to the website asset path.
    text = text.replace("../figures_fixed/", "../assets/figures/textbook/")
    text = text.replace("..\\figures_fixed\\", "../assets/figures/textbook/")
    text = re.sub(r"\n{3,}", "\n\n", text)
    title = f"# 第{chapter_no}章"
    if not text.lstrip().startswith(title):
        return text
    return text


def copy_textbook_pdf() -> bool:
    return copy_file(TEXTBOOK_PDF, ASSETS / "textbook" / "software_architecture_textbook_student_v5_1.pdf")


def copy_figures() -> tuple[int, list[str]]:
    count = 0
    copied: list[str] = []
    for chapter_dir in sorted(FIGURE_SOURCE_DIR.glob("chapter[0-9][0-9]")):
        student = chapter_dir / "student"
        if not student.exists():
            continue
        for src in sorted(student.glob("*.png")):
            dst = ASSETS / "figures" / "textbook" / chapter_dir.name / "student" / src.name
            if copy_file(src, dst):
                count += 1
                copied.append(dst.relative_to(SITE).as_posix())
    return count, copied


def build_chapters() -> list[str]:
    target = DOCS / "textbook"
    target.mkdir(parents=True, exist_ok=True)
    generated: list[str] = []
    for i in range(1, 9):
        src = CHAPTER_SOURCE_DIR / f"chapter{i:02d}_student.md"
        if not src.exists():
            src = ROOT / "textbook" / "chapters_v4" / f"chapter{i:02d}.md"
        text = src.read_text(encoding="utf-8", errors="ignore")
        text = normalize_chapter_markdown(text, i)
        dst = target / f"chapter{i:02d}.md"
        write(dst, text)
        generated.append(dst.relative_to(SITE).as_posix())
    return generated


def build_index() -> None:
    pdf = "../assets/textbook/software_architecture_textbook_student_v5_1.pdf"
    rows = "\n".join(
        [
            "| [第1章 从能写代码到能控复杂系统](chapter01.md) | 复杂性、FR/QA/C、架构时间账 | M1前置视角 |",
            "| [第2章 软件过程模型与开发节奏选择](chapter02.md) | 过程模型、反馈节奏、风险暴露 | 开发节奏选择 |",
            "| [第3章 项目管理、可行性分析与风险控制](chapter03.md) | WBS、里程碑、风险登记 | 项目计划 |",
            "| [第4章 需求工程：从用户声音到可验证规格](chapter04.md) | 用户、场景、用例、SRS | M1 |",
            "| [第5章 架构表达与系统建模](chapter05.md) | UML、C4、时序图、模型质量 | M2 |",
            "| [第6章 架构设计、架构风格与分布式系统](chapter06.md) | ADR、架构风格、分布式取舍 | M3 |",
            "| [第7章 软件测试、质量保障与安全验证](chapter07.md) | 测试层级、质量门禁、安全验证 | M4测试 |",
            "| [第8章 发布、交付、运维与可观测性](chapter08.md) | CI/CD、发布回滚、可观测性 | M4交付 |",
        ]
    )
    write(
        DOCS / "textbook" / "index.md",
        f"""# 电子教材

《软件体系结构课程电子教材》学生阅读版 v5.1 已整理为网页正文阅读版。网页章节用于在线阅读，PDF 用于下载、打印和离线复习。

<div class="resource-actions">
  <a class="md-button md-button--primary" href="{pdf}" target="_blank">下载完整 PDF</a>
  <a class="md-button" href="{pdf}" target="_blank">新窗口打开 PDF</a>
</div>

## 在线阅读

| 章节 | 核心内容 | 对应项目 |
|---|---|---|
{rows}

## 阅读建议

- 先阅读每章“本章导读”和“核心问题”；
- 再看贯穿案例、图示和提示框；
- 做项目时优先查看“项目提示”和模板；
- 期末复习时重点看小结、复习题和案例分析题。

!!! note "说明"
    本页以 Markdown 章节正文为主要阅读方式，不再依赖浏览器 PDF 插件。完整 PDF 仅作为下载和打印资源。
""",
    )


def write_report(chapters: list[str], figure_count: int, figures: list[str], pdf_ok: bool) -> None:
    REVIEW.mkdir(parents=True, exist_ok=True)
    write(
        REVIEW / "textbook_online_reading_report.md",
        f"""# 电子教材在线阅读化报告

## 处理结果

| 项目 | 结果 |
|---|---|
| 章节来源 | `textbook/chapters_illustrated_student/`，缺失时回退到 `textbook/chapters_v4/` |
| 生成章节 | {len(chapters)} 个 |
| 教材 PDF | {'已复制到 `site/assets/textbook/`' if pdf_ok else '源文件缺失'} |
| 教材附图 | 已复制 {figure_count} 张 |
| 在线阅读方式 | Markdown 章节正文 |

## 生成页面

""" + "\n".join(f"- `{item}`" for item in chapters) + f"""

## 图示资产

教材图示已放入：

```text
site/assets/figures/textbook/
```

并同步到：

```text
site/docs/assets/figures/textbook/
```

## 结论

`/textbook/` 页面已不再只是 PDF 占位页，而是提供第1-8章在线阅读入口，同时保留完整 PDF 下载。
""",
    )


def main() -> int:
    pdf_ok = copy_textbook_pdf()
    figure_count, figures = copy_figures()
    chapters = build_chapters()
    build_index()
    sync_assets_to_docs()
    write_report(chapters, figure_count, figures, pdf_ok)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
