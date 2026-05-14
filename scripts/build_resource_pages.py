from __future__ import annotations

import shutil
from pathlib import Path

import yaml


SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent
DOCS = SITE / "docs"
ASSETS = SITE / "assets"
CONTENT = SITE / "content"
REVIEW = SITE / "review"


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
    dst = DOCS / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    if ASSETS.exists():
        shutil.copytree(ASSETS, dst)


def ensure_templates() -> list[str]:
    templates = {
        "m1_requirements_template.md": """# M1 选题与需求模板

## 项目名称

## 小组成员与分工

## 目标用户

## 典型使用场景

## 核心功能

## 初步质量属性

## 主要约束
""",
        "m2_modeling_template.md": """# M2 建模与结构表达模板

## 系统边界

## C1 上下文图说明

## C2 容器/模块图说明

## 核心场景时序图

## 领域对象或关键类

## 模型自查
""",
        "m3_adr_template.md": """# M3 ADR 模板

## ADR 编号与标题

## 背景与约束

## 决策

## 放弃方案

## 理由

## 风险

## 观察指标
""",
        "m4_testing_delivery_template.md": """# M4 测试、交付与运维模板

## 测试范围

## 测试层级

## 质量门禁

## 发布流程

## 回滚条件

## 日志、指标、追踪

## 故障处理与复盘
""",
    }
    generated = []
    for name, text in templates.items():
        path = ASSETS / "downloads" / "templates" / name
        write(path, text)
        generated.append(path.relative_to(SITE).as_posix())
    return generated


def copy_process_artifacts() -> list[str]:
    generated = []
    for src_name, dst_name in [
        ("course_syllabus.md", "course_syllabus.md"),
        ("student_profile.md", "student_profile.md"),
        ("assessment_policy.md", "assessment_policy_public_note.md"),
    ]:
        if copy_file(ROOT / "input" / src_name, ASSETS / "process" / dst_name):
            generated.append(f"assets/process/{dst_name}")
    return generated


def build_manifest(template_files: list[str], process_files: list[str]) -> None:
    items = [
        {
            "title": "软件体系结构课程电子教材学生版 v5.1",
            "category": "textbook",
            "file": "assets/textbook/software_architecture_textbook_student_v5_1.pdf",
            "preview_type": "pdf",
            "public": True,
            "description": "第1-8章完整电子教材 PDF，用于下载、打印和离线阅读。",
            "source": "textbook/output",
            "note": "网页正文版见 docs/textbook/。",
        },
        {
            "title": "教材附图图库",
            "category": "figures",
            "file": "assets/figures/textbook/",
            "preview_type": "gallery",
            "public": True,
            "description": "第1-8章教材图示，用于复习核心框架和工程流程。",
            "source": "textbook/figures_fixed",
            "note": "图片仅为教材公开图示，不含教师命题材料。",
        },
        {
            "title": "课程过程材料",
            "category": "process",
            "file": "assets/process/",
            "preview_type": "markdown",
            "public": True,
            "description": "课程大纲、学生画像和公开考核说明等过程材料。",
            "source": "input/",
            "note": "不包含教师评分细则。",
        },
        {
            "title": "课程项目模板",
            "category": "templates",
            "file": "assets/downloads/templates/",
            "preview_type": "download",
            "public": True,
            "description": "M1-M4 项目阶段可填写模板。",
            "source": "site generated",
            "note": "学生可下载使用。",
        },
        {
            "title": "参考教材书目",
            "category": "references",
            "file": "assets/references/reference_books.md",
            "preview_type": "markdown",
            "public": True,
            "description": "课程推荐参考书目信息，不放未授权电子书 PDF。",
            "source": "course bibliography",
            "note": "只发布书目信息和学习建议。",
        },
    ]
    write(
        CONTENT / "resources" / "resources_manifest.yml",
        yaml.safe_dump(items, allow_unicode=True, sort_keys=False),
    )


def build_reference_books() -> None:
    write(
        ASSETS / "references" / "reference_books.md",
        """# 参考书目

以下为课程学习参考书目。本站不提供未确认授权的电子书 PDF。

| 书名 | 作者 | 用途 |
|---|---|---|
| 《现代软件工程：构建之法》 | 邹欣 | 软件工程过程、团队协作、需求、测试与项目实践 |
| 《软件体系结构》 | 张友生 | 软件体系结构概念、风格、建模和评审 |
| Software Architecture in Practice | Len Bass 等 | 架构质量属性、架构评估和工程实践拓展 |
| Fundamentals of Software Architecture | Mark Richards, Neal Ford | 架构风格、架构权衡和现代架构角色 |

阅读建议：以课程电子教材和课堂 PPT 为主，参考书用于扩展理解。
""",
    )


def build_resources_pages() -> None:
    figures = sorted((ASSETS / "figures" / "textbook").rglob("*.png"))
    figure_cards = "\n".join(
        f'<div class="figure-card"><img src="../../assets/figures/textbook/{p.relative_to(ASSETS / "figures" / "textbook").as_posix()}" alt="{p.stem}"><p>{p.stem}</p></div>'
        for p in figures
    )
    process_files = sorted((ASSETS / "process").glob("*"))
    template_files = sorted((ASSETS / "downloads" / "templates").glob("*"))
    reference_file = ASSETS / "references" / "reference_books.md"

    cards = []
    if figures:
        cards.append(
            '<div class="course-card"><h3>教材附图</h3><p>第1-8章核心图示，适合快速复习框架。</p><a class="card-link" href="textbook_figures/">查看</a></div>'
        )
    if process_files:
        cards.append(
            '<div class="course-card"><h3>过程产物</h3><p>课程大纲、公开考核说明、项目过程材料。</p><a class="card-link" href="process_artifacts/">查看</a></div>'
        )
    if template_files:
        cards.append(
            '<div class="course-card"><h3>项目模板</h3><p>M1-M4 可填写模板。</p><a class="card-link" href="templates/">查看</a></div>'
        )
    if reference_file.exists():
        cards.append(
            '<div class="course-card"><h3>参考书目</h3><p>课程延伸阅读与书目说明。</p><a class="card-link" href="reference_books/">查看</a></div>'
        )
    card_grid = "\n".join(cards) or "<p>暂无可公开补充资料。</p>"

    write(
        DOCS / "resources" / "index.md",
        f"""# 补充资料中心

补充资料按主题组织，不作为文件列表平铺。请先完成教材和课堂 PPT 学习，再根据项目需要查阅。

<div class="card-grid">
{card_grid}
</div>
""",
    )
    write(
        DOCS / "resources" / "textbook_figures.md",
        "# 教材附图\n\n教材附图来自学生版电子教材，用于复习核心框架、流程和结构图。\n\n"
        + f'<div class="figure-grid">\n{figure_cards}\n</div>',
    )
    write(
        DOCS / "resources" / "process_artifacts.md",
        """# 过程产物

| 资料 | 说明 | 链接 |
|---|---|---|
| 课程大纲 | 课程目标、教学安排和学习路径 | [查看](../assets/process/course_syllabus.md) |
| 学生画像 | 授课对象、基础假设和课程定位 | [查看](../assets/process/student_profile.md) |
| 公开考核说明 | 学生可见的考核结构说明 | [查看](../assets/process/assessment_policy_public_note.md) |
""",
    )
    write(
        DOCS / "resources" / "templates.md",
        """# 项目模板

| 模板 | 用途 | 下载 |
|---|---|---|
| M1 选题与需求模板 | 选题、用户、场景、需求 | [下载](../assets/downloads/templates/m1_requirements_template.md) |
| M2 建模与结构表达模板 | C1/C2/时序图/模型自查 | [下载](../assets/downloads/templates/m2_modeling_template.md) |
| M3 ADR 模板 | 架构决策、放弃方案、风险 | [下载](../assets/downloads/templates/m3_adr_template.md) |
| M4 测试交付与运维模板 | 测试、发布、回滚、观测 | [下载](../assets/downloads/templates/m4_testing_delivery_template.md) |
""",
    )
    ref_text = (ASSETS / "references" / "reference_books.md").read_text(encoding="utf-8")
    write(DOCS / "resources" / "reference_books.md", ref_text)


def build_project_pages() -> None:
    project_data = {
        "m1": (
            "M1：选题与需求",
            "确定小组项目题目，形成可继续分析和评审的需求材料。",
            "m1_requirements_template.md",
            ["项目名称与一句话定位", "小组成员与分工", "目标用户与典型场景", "核心功能与初步质量属性", "主要约束"],
        ),
        "m2": (
            "M2：建模与结构表达",
            "把需求转化为可讨论、可评审的系统模型。",
            "m2_modeling_template.md",
            ["系统边界说明", "C1/C2结构表达", "核心场景时序图", "领域对象或关键类", "模型质量自查"],
        ),
        "m3": (
            "M3：架构决策与 ADR",
            "围绕质量属性、约束和风险形成可审查的架构决策。",
            "m3_adr_template.md",
            ["架构风格选择", "至少3条ADR", "质量属性响应", "技术债记录", "放弃方案与风险"],
        ),
        "m4": (
            "M4：测试、交付与运维说明",
            "说明系统如何验证质量、如何上线、如何回滚、如何观察运行状态。",
            "m4_testing_delivery_template.md",
            ["测试计划V1", "质量门禁清单", "发布流程与回滚条件", "日志指标追踪方案", "故障处理与复盘说明"],
        ),
    }
    for key, (title, goal, template, submits) in project_data.items():
        cards = "\n".join(
            f'<div class="course-card"><h3>{item}</h3><p>提交材料组成项</p></div>' for item in submits
        )
        write(
            DOCS / "project" / f"{key}.md",
            f"""# {title}

<span class="tag">课程项目</span><span class="tag">{key.upper()}</span>

## 产出目标

{goal}

## 提交材料

<div class="card-grid">
{cards}
</div>

## 格式要求

- 建议提交 PDF 或 Markdown；
- 图示、表格、ADR、测试计划等材料应有标题和说明；
- 小组提交需写清成员分工和主要贡献。

## 建议模板

<div class="resource-actions">
  <a class="md-button md-button--primary" href="../../assets/downloads/templates/{template}" target="_blank">下载模板</a>
</div>

## 评价关注点

这里列出的是学生可见的质量要求，不是教师阅卷标准。

- 是否表达清楚问题、约束和判断；
- 是否有具体场景、图示或说明；
- 是否能支撑下一阶段继续推进；
- 是否避免只罗列工具名或空泛口号。
""",
        )


def build_review_page() -> None:
    write(
        DOCS / "review" / "final_review_guide.md",
        """# 期末复习范围说明

本页只说明公开复习范围和学习方向，不包含正式试题、题库或教师阅卷标准。

## 复习范围

| 章节 | 复习重点 |
|---|---|
| 第1章 | 软件复杂性、FR/QA/C、架构时间账 |
| 第2章 | 过程模型、开发节奏、风险暴露 |
| 第3章 | WBS、里程碑、风险登记、协作流程 |
| 第4章 | 需求获取、用例、可验证规格、质量属性场景 |
| 第5章 | UML/C4、架构表达、最小建模图集 |
| 第6章 | ADR、架构风格、模块化单体、微服务与分布式单体 |
| 第7章 | 测试层级、质量门禁、安全验证 |
| 第8章 | CI/CD、发布策略、回滚、可观测性 |

## 复习方法

1. 先读每章“本章小结”和提示框；
2. 再看每次课 PPT 的核心图示；
3. 用课程项目材料练习案例分析；
4. 复习时不要只背名词，要能说明适用场景、风险和工程取舍。

!!! warning "公开范围"
    本页不提供正式试题、题库或教师阅卷标准。
""",
    )


def write_report(template_files: list[str], process_files: list[str]) -> None:
    REVIEW.mkdir(parents=True, exist_ok=True)
    write(
        REVIEW / "resource_center_build_report.md",
        f"""# 补充资料中心建设报告

## 已建设目录

- `site/assets/figures/textbook/`
- `site/assets/process/`
- `site/assets/references/`
- `site/assets/downloads/templates/`
- `site/content/resources/resources_manifest.yml`
- `site/docs/resources/`

## 模板文件

""" + "\n".join(f"- `{item}`" for item in template_files) + """

## 过程产物

""" + "\n".join(f"- `{item}`" for item in process_files) + """

## 公开控制

参考书仅发布书目信息和学习建议，不发布未确认授权的电子书 PDF。
""",
    )


def main() -> int:
    template_files = ensure_templates()
    process_files = copy_process_artifacts()
    build_reference_books()
    build_manifest(template_files, process_files)
    build_resources_pages()
    build_project_pages()
    build_review_page()
    sync_assets_to_docs()
    write_report(template_files, process_files)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
