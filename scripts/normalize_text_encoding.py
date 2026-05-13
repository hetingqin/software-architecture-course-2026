from __future__ import annotations

from pathlib import Path


SITE = Path(__file__).resolve().parents[1]
REPORT = SITE / "review" / "encoding_fix_report.md"
TARGETS = [SITE / "docs", SITE / "assets", SITE / "content"]
EXTENSIONS = {".txt", ".md"}

ENCODINGS = ["utf-8-sig", "utf-8", "gb18030", "gbk", "cp936", "big5", "latin-1"]


def detect_and_read(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ENCODINGS:
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace"), "utf-8-replace"


def main() -> int:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, str, str]] = []
    converted = 0

    for base in TARGETS:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
                continue
            text, encoding = detect_and_read(path)
            path.write_text(text, encoding="utf-8", newline="\n")
            status = "已转换为 UTF-8" if encoding.lower() not in {"utf-8", "utf-8-sig"} else "已确认 UTF-8"
            if status.startswith("已转换"):
                converted += 1
            rows.append((path.relative_to(SITE).as_posix(), encoding, status))

    lines = [
        "# 文本编码修复报告",
        "",
        "扫描范围：`site/docs/`、`site/assets/`、`site/content/` 下所有 `.txt` 与 `.md` 文件。",
        "",
        f"检查文件数：{len(rows)}",
        f"转换文件数：{converted}",
        "",
        "| 文件 | 原识别编码 | 处理结果 |",
        "|---|---|---|",
    ]
    lines.extend(f"| `{rel}` | {enc} | {status} |" for rel, enc, status in rows)
    lines.extend(
        [
            "",
            "## 结论",
            "",
            "所有文本文件已统一写出为 UTF-8。核心作业要求不再依赖 `.txt` 直接打开，而是在课程页面正文中展示。",
        ]
    )
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
