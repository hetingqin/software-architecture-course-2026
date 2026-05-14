from __future__ import annotations

import shutil
from pathlib import Path


SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent
ASSETS = SITE / "assets"
DOCS = SITE / "docs"
REVIEW = SITE / "review"


def read_text_any(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ["utf-8-sig", "utf-8", "gb18030", "gbk", "cp936", "latin-1"]:
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace"), "utf-8-replace"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def copy_assignment_sources() -> list[str]:
    generated: list[str] = []
    for lesson in range(1, 9):
        src = ROOT / "input" / "lessons" / f"lesson{lesson:02d}" / "assignments.md"
        if not src.exists():
            continue
        text, _ = read_text_any(src)
        title = f"# 第{lesson:02d}讲课后作业\n\n"
        body = "\n".join(line for line in text.splitlines() if not line.startswith("# ")).strip()
        md_name = f"lesson{lesson:02d}_assignment.md"
        raw_md_name = f"lesson{lesson:02d}_assignment.md.txt"
        txt_name = f"lesson{lesson:02d}_assignment.txt"
        markdown_text = title + (body or text.strip())
        write(ASSETS / "assignments" / md_name, markdown_text)
        write(ASSETS / "assignments" / raw_md_name, markdown_text)
        write(ASSETS / "assignments" / txt_name, body or text.strip())
        generated.append(f"assets/assignments/{md_name}")
        generated.append(f"assets/assignments/{raw_md_name}")
    return generated


def sync_assets_to_docs() -> None:
    dst = DOCS / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    if ASSETS.exists():
        shutil.copytree(ASSETS, dst)


def main() -> int:
    generated = copy_assignment_sources()
    sync_assets_to_docs()
    REVIEW.mkdir(parents=True, exist_ok=True)
    write(
        REVIEW / "assignment_text_conversion_report.md",
        "# 作业文本转换报告\n\n"
        + "\n".join(f"- `{item}`" for item in generated)
        + "\n\n作业源文件已转换为 UTF-8 Markdown 与 TXT 附件，并同步到 `docs/assets/assignments/`。",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
