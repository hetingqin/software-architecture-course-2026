from __future__ import annotations

from pathlib import Path


SITE = Path(__file__).resolve().parents[1]
TARGETS = [SITE / "docs", SITE / "assets", SITE / "content", SITE / "build"]
REPORT = SITE / "review" / "private_file_leak_check.md"

PATH_TERMS = [
    "teacher_only",
    "answer_key",
    "paper_a",
    "paper_b",
    "question_bank",
    "grading_rubric",
    "exam_quality_review",
    "教师版",
    "评分细则",
    "期末试卷",
    "试卷a",
    "试卷b",
    "命题质量分析",
    "ab卷难度",
    "平时成绩评分细则教师版",
]

CONTENT_TERMS = [
    "teacher_only",
    "answer_key",
    "paper_A",
    "paper_B",
    "question_bank",
    "grading_rubric",
    "exam_quality_review",
    "期末试卷A",
    "期末试卷B",
    "答案与评分细则",
    "教师版答案",
    "命题质量分析报告",
    "AB卷难度",
    "平时成绩评分细则教师版",
]


def iter_files() -> list[Path]:
    files: list[Path] = []
    for target in TARGETS:
        if target.exists():
            files.extend(p for p in target.rglob("*") if p.is_file())
    return sorted(files)


def main() -> int:
    path_hits: list[str] = []
    content_hits: list[str] = []
    for p in iter_files():
        rel = p.relative_to(SITE).as_posix()
        lower = rel.lower()
        if "exam/" in lower or lower.startswith("exam"):
            path_hits.append(f"{rel} 命中 exam 路径")
        for term in PATH_TERMS:
            if term.lower() in lower:
                path_hits.append(f"{rel} 命中路径关键词 `{term}`")
        if p.suffix.lower() in {".md", ".txt", ".html", ".yml", ".yaml"}:
            text = p.read_text(encoding="utf-8", errors="ignore")
            for term in CONTENT_TERMS:
                if term in text:
                    content_hits.append(f"{rel} 命中内容关键词 `{term}`")

    ok = not path_hits and not content_hits
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        "# 考试资料泄露检查\n\n"
        f"检查结果：{'通过' if ok else '不通过'}\n\n"
        "## 路径命中\n\n"
        + ("\n".join(f"- {x}" for x in path_hits) if path_hits else "- 无")
        + "\n\n## 内容命中\n\n"
        + ("\n".join(f"- {x}" for x in content_hits) if content_hits else "- 无")
        + "\n\n## 结论\n\n"
        + ("未发现考试保密资料进入学生网站发布目录。\n" if ok else "发现疑似泄密内容，请处理后再发布。\n"),
        encoding="utf-8",
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
