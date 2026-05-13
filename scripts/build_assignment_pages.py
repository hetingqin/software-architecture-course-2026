from __future__ import annotations

from pathlib import Path


SITE = Path(__file__).resolve().parents[1]
DOCS = SITE / "docs"
ASSETS = SITE / "assets"
REVIEW = SITE / "review"


LESSON_TITLES = {
    1: "从能写代码到能控复杂系统",
    2: "软件过程模型与开发节奏选择",
    3: "项目管理、可行性分析与风险控制",
    4: "需求工程：从用户声音到可验证规格",
    5: "架构表达与系统建模",
    6: "架构设计、架构风格与分布式系统",
    7: "软件测试、质量保障与安全验证",
    8: "发布、交付、运维与可观测性",
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_assignment(lesson: int) -> str:
    p = ASSETS / "assignments" / f"lesson{lesson:02d}_assignment.md"
    if not p.exists():
        return "本讲作业要求待补充。"
    text = p.read_text(encoding="utf-8", errors="ignore")
    return "\n".join(line for line in text.splitlines() if not line.startswith("# ")).strip()


def infer_goal(lesson: int) -> str:
    goals = {
        1: "完成课程项目分组与选题，为后续 M1 打基础。",
        2: "为小组项目选择合适的软件过程模型和开发节奏。",
        3: "把项目目标拆成计划、里程碑、任务和风险。",
        4: "形成需求规格初稿，支撑 M1 需求材料。",
        5: "形成关键分析与设计模型，支撑 M2。",
        6: "撰写架构决策记录，支撑 M3。",
        7: "形成测试计划 V1，支撑 M4 测试部分。",
        8: "形成发布运维方案 V1，支撑 M4 交付部分。",
    }
    return goals[lesson]


def build_pages() -> list[str]:
    generated: list[str] = []
    rows: list[str] = []
    for lesson in range(1, 9):
        title = LESSON_TITLES[lesson]
        body = load_assignment(lesson)
        txt = f"../assets/assignments/lesson{lesson:02d}_assignment.txt"
        md = f"../assets/assignments/lesson{lesson:02d}_assignment.md"
        page = f"lesson{lesson:02d}_assignment.md"
        rows.append(f"| [第{lesson:02d}讲作业]({page}) | {title} |")
        write(
            DOCS / "assignments" / page,
            f"""# 第{lesson:02d}讲课后作业

## 作业标题

{title}

## 作业目标

{infer_goal(lesson)}

## 提交内容

<div class="assignment-box">
{body}
</div>

## 提交格式

- 建议提交 Markdown、PDF 或课程要求指定格式；
- 小组作业需写清成员分工；
- 图表、模型和 ADR 等材料应有标题、说明和必要解释。

## 截止要求

以任课教师课堂通知或课程平台通知为准。

## 下载原始文件

<div class="resource-actions">
  <a class="md-button" href="{md}" target="_blank">下载 Markdown</a>
  <a class="md-button" href="{txt}" target="_blank">下载 TXT</a>
</div>
""",
        )
        generated.append(f"docs/assignments/{page}")

    write(
        DOCS / "assignments" / "index.md",
        "# 课后作业\n\n每次课作业均已整理为网页正文，可直接阅读。原始文本作为附件保留。\n\n"
        "| 作业 | 对应课程 |\n|---|---|\n" + "\n".join(rows),
    )
    return generated


def main() -> int:
    pages = build_pages()
    REVIEW.mkdir(parents=True, exist_ok=True)
    write(
        REVIEW / "assignment_page_generation_report.md",
        "# 作业页面生成报告\n\n"
        + "\n".join(f"- `{item}`" for item in pages)
        + "\n\n作业要求已从附件型资源转为网页正文阅读，并保留原始 Markdown/TXT 下载。",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
