from __future__ import annotations

from pathlib import Path


SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent
TARGETS = [SITE / "docs", SITE / "public", SITE / "build"]
REPORT = SITE / "private_file_leak_check.md"
REVIEW_REPORT = SITE / "review" / "private_file_leak_check.md"

FORBIDDEN_PATH_TERMS = [
    "teacher_only",
    "answer_key",
    "paper_a",
    "paper_b",
    "grading_rubric",
    "exam_quality_review",
    "question_bank",
    "ab卷难度",
    "命题质量分析",
    "教师版",
    "答案与评分",
    "期末试卷",
    "题库",
    "命题质量",
    "试卷a",
    "试卷b",
]

FORBIDDEN_CONTENT_TERMS = [
    "teacher_only",
    "answer_key",
    "paper_A",
    "paper_B",
    "paper_a",
    "paper_b",
    "question_bank",
    "grading_rubric",
    "exam_quality_review",
    "AB卷难度",
    "命题质量分析报告",
    "期末试卷A",
    "期末试卷B",
    "参考答案要点：",
    "评分点：",
    "教师版答案",
]


def iter_files() -> list[Path]:
    files: list[Path] = []
    for target in TARGETS:
        if target.exists():
            files.extend([p for p in target.rglob("*") if p.is_file()])
    return sorted(files)


def scan() -> tuple[list[str], list[str], list[str]]:
    files = iter_files()
    path_hits: list[str] = []
    content_hits: list[str] = []
    exam_copies: list[str] = []

    for file in files:
        rel = file.relative_to(SITE).as_posix()
        lower = rel.lower()
        if "exam/" in lower or lower.startswith("exam"):
            exam_copies.append(rel)
        for term in FORBIDDEN_PATH_TERMS:
            if term.lower() in lower:
                path_hits.append(f"{rel} 命中路径关键词 `{term}`")
        if file.suffix.lower() in {".md", ".txt", ".html", ".yml", ".yaml"}:
            text = file.read_text(encoding="utf-8", errors="ignore")
            for term in FORBIDDEN_CONTENT_TERMS:
                if term in text:
                    content_hits.append(f"{rel} 命中内容关键词 `{term}`")
    return path_hits, content_hits, exam_copies


def main() -> int:
    path_hits, content_hits, exam_copies = scan()
    ok = not path_hits and not content_hits and not exam_copies

    lines = [
        "# 网站公开目录保密资料检查",
        "",
        "检查目录：" + "、".join(f"`{target}`" for target in TARGETS),
        "",
        f"检查结果：{'通过' if ok else '不通过'}",
        "",
        "## 检查规则",
        "",
        "- 不允许出现 `exam/` 目录复制文件。",
        "- 不允许出现 teacher_only、answer_key、paper_A、paper_B 等教师命题材料。",
        "- 不允许出现答案、评分细则、题库、命题质量分析等考试保密材料。",
        "",
        "## 路径命中",
        "",
    ]
    lines.extend([f"- {item}" for item in path_hits] or ["- 无"])
    lines.extend(["", "## 内容命中", ""])
    lines.extend([f"- {item}" for item in content_hits] or ["- 无"])
    lines.extend(["", "## exam 目录复制检查", ""])
    lines.extend([f"- {item}" for item in exam_copies] or ["- 无"])
    lines.extend(
        [
            "",
            "## 结论",
            "",
            "当前公开目录未发现考试保密资料。" if ok else "发现疑似保密资料，请删除或改写后再发布。",
        ]
    )
    text = "\n".join(lines) + "\n"
    REPORT.write_text(text, encoding="utf-8")
    REVIEW_REPORT.parent.mkdir(parents=True, exist_ok=True)
    REVIEW_REPORT.write_text(text, encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
