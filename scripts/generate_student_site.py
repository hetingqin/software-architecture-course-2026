from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"
DOCS = SITE / "docs"
PUBLIC = SITE / "public"
DOCS_PUBLIC = DOCS / "public"


LESSONS = {
    "lesson01": {
        "no": "01",
        "title": "从能写代码到能控复杂系统",
        "core": "写代码解决局部问题，架构控制系统复杂性。",
        "textbook": "第1章 从能写代码到能控复杂系统",
        "goals": [
            "理解软件复杂性不只来自代码规模，也来自需求变化、协作、技术组合与运行约束。",
            "掌握 FR/QA/C 三分法，用功能需求、质量属性和约束拆解系统问题。",
            "理解架构时间账，能判断短期快写和长期可维护之间的代价。",
        ],
        "class_task": "用自己的项目或熟悉系统做一次复杂性体检，标出最主要的复杂性来源。",
        "extra": "复习电子教材第1章，重点关注复杂性四来源、FR/QA/C、架构时间账。",
    },
    "lesson02": {
        "no": "02",
        "title": "软件过程模型与开发节奏选择",
        "core": "复杂性来源不同，开发节奏不能相同。",
        "textbook": "第2章 软件过程模型与开发节奏选择",
        "goals": [
            "理解瀑布、原型、增量、迭代、螺旋和敏捷模型的适用条件。",
            "能根据需求稳定性、风险大小、团队规模和交付节奏选择开发过程。",
            "能解释节奏选错会如何导致返工、延期和质量失控。",
        ],
        "class_task": "判断小组项目适合哪种过程模型，并说明为什么不是默认敏捷或默认瀑布。",
        "extra": "复习电子教材第2章，重点关注风险暴露节奏和模型选择场景。",
    },
    "lesson03": {
        "no": "03",
        "title": "项目管理、可行性分析与风险控制",
        "core": "技术上可以做，不代表工程上做得成。",
        "textbook": "第3章 项目管理、可行性分析与风险控制",
        "goals": [
            "理解范围、时间、成本、质量之间的取舍关系。",
            "掌握 WBS、里程碑、关键路径和风险登记表的基本用法。",
            "能为课程项目制定可执行计划，而不是只写愿望清单。",
        ],
        "class_task": "把小组项目拆成若干可交付任务，并识别至少3个高风险点。",
        "extra": "复习电子教材第3章，重点关注 WBS、风险矩阵、Ticket/PR 协作机制。",
    },
    "lesson04": {
        "no": "04",
        "title": "需求工程：从用户声音到可验证规格",
        "core": "需求不是功能清单，而是把真实问题翻译成工程决策输入。",
        "textbook": "第4章 需求工程：从用户声音到可验证规格",
        "goals": [
            "理解用户声音、使用场景、真实问题和需求规格之间的差别。",
            "掌握典型用户、用例文本、可验证规格和质量属性场景的写法。",
            "能把含糊需求改写成可检查、可评审、可测试的表达。",
        ],
        "class_task": "围绕项目核心功能写出一个用例文本，并补充正常流程、异常流程和验收标准。",
        "extra": "复习电子教材第4章，重点关注“用户声音到可验证规格”的转换。",
    },
    "lesson05": {
        "no": "05",
        "title": "架构表达与系统建模",
        "core": "图不是装饰，而是团队对系统结构形成共识的工程工具。",
        "textbook": "第5章 架构表达与系统建模",
        "goals": [
            "理解 C4、UML、时序图、类图、用例图等模型各自回答的问题。",
            "能为一个系统选择最小必要图集，而不是为了画图而画图。",
            "能用图说明系统边界、主要角色、核心流程和关键结构。",
        ],
        "class_task": "为小组项目画出 C1/C2 图或一个核心用例的时序图，并说明图要回答的问题。",
        "extra": "复习电子教材第5章，重点关注建模图的选择规则和质量检查清单。",
    },
    "lesson06": {
        "no": "06",
        "title": "架构设计、架构风格与分布式系统",
        "core": "架构设计不是选流行技术，而是在约束下做可解释、可审查、可演进的结构决策。",
        "textbook": "第6章 架构设计、架构风格与分布式系统",
        "goals": [
            "理解技术栈清单和架构决策的区别。",
            "掌握质量属性如何驱动模块边界、同步异步、一致性和外部依赖处理。",
            "能写出包含背景、决策、放弃方案、理由和风险的 ADR。",
        ],
        "class_task": "为小组项目写出至少1条 ADR，并说明放弃了什么方案以及原因。",
        "extra": "复习电子教材第6章，重点关注模块化单体、微服务、分布式单体和 ADR。",
    },
    "lesson07": {
        "no": "07",
        "title": "软件测试、质量保障与安全验证",
        "core": "质量不是最后测出来的，而是在架构边界、依赖关系和交付门禁中被设计出来的。",
        "textbook": "第7章 软件测试、质量保障与安全验证",
        "goals": [
            "理解单元测试、集成测试、契约测试、端到端测试的分工。",
            "能根据系统架构设计测试策略和质量门禁。",
            "能识别权限、输入校验、接口调用和数据一致性中的安全验证点。",
        ],
        "class_task": "为项目设计测试计划 V1，至少覆盖一个关键业务场景、一个异常场景和一个权限场景。",
        "extra": "复习电子教材第7章，重点关注可测试性、测试金字塔、质量门禁和安全验证。",
    },
    "lesson08": {
        "no": "08",
        "title": "发布、交付、运维与可观测性",
        "core": "开发完成不等于上线成功，系统必须能发布、能回滚、能观察、能复盘。",
        "textbook": "第8章 发布、交付、运维与可观测性",
        "goals": [
            "理解 CI/CD、灰度发布、回滚和发布门禁的作用。",
            "掌握日志、指标、追踪三类可观测性数据的分工。",
            "能为课程项目设计基础发布运维方案。",
        ],
        "class_task": "为项目写出发布流程、回滚条件、日志指标和故障处理说明。",
        "extra": "复习电子教材第8章，重点关注上线、回滚、观测和复盘闭环。",
    },
}


PROJECTS = {
    "m1": {
        "title": "M1：选题与需求",
        "goal": "确定小组项目题目，并形成可继续分析的需求材料。",
        "submit": [
            "项目名称与一句话定位。",
            "4-6人分组与角色分工。",
            "目标用户与典型使用场景。",
            "核心功能清单与至少1个核心用例。",
            "初步质量属性与约束说明。",
        ],
        "format": "建议提交 Markdown/PDF，包含项目背景、用户、场景、需求列表、用例和分工。",
        "template": "m1_requirements_template.txt",
    },
    "m2": {
        "title": "M2：建模与结构表达",
        "goal": "把需求转化为可以讨论和评审的系统模型。",
        "submit": [
            "C1 系统上下文图或系统边界说明。",
            "C2 容器图或模块结构说明。",
            "至少1个核心场景时序图。",
            "关键领域对象或类关系说明。",
            "模型质量自查说明。",
        ],
        "format": "建议提交 PDF，图必须有图题、图注和解释文字。",
        "template": "m2_modeling_template.txt",
    },
    "m3": {
        "title": "M3：架构决策与 ADR",
        "goal": "围绕质量属性、约束和风险形成可审查的架构决策。",
        "submit": [
            "架构风格选择说明。",
            "至少3条 ADR。",
            "关键质量属性与架构响应。",
            "技术债记录。",
            "放弃方案与风险说明。",
        ],
        "format": "建议提交 Markdown/PDF，ADR 使用统一模板。",
        "template": "m3_adr_template.txt",
    },
    "m4": {
        "title": "M4：测试、交付与运维说明",
        "goal": "说明系统如何验证质量、如何上线、如何回滚、如何观察运行状态。",
        "submit": [
            "测试计划 V1。",
            "质量门禁清单。",
            "发布流程与回滚条件。",
            "日志、指标、追踪方案。",
            "故障处理与复盘说明。",
        ],
        "format": "建议提交 PDF，重点写清可验证、可执行、可追踪。",
        "template": "m4_testing_delivery_template.txt",
    },
}


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def copy_public_file(src: Path, public_rel: str) -> bool:
    if not src.exists():
        return False
    for base in (PUBLIC, DOCS_PUBLIC):
        dst = base / public_rel
        ensure_dir(dst.parent)
        shutil.copy2(src, dst)
    return True


def read_assignment(lesson_id: str) -> str:
    p = ROOT / "input" / "lessons" / lesson_id / "assignments.md"
    if not p.exists():
        return "本讲课后作业待补充。"
    text = p.read_text(encoding="utf-8", errors="ignore").strip()
    lines = [line for line in text.splitlines() if not line.startswith("# ")]
    return "\n".join(lines).strip() or text


def asset_link(page_depth: int, rel: str) -> str:
    prefix = "../" * page_depth
    return f"{prefix}public/{rel.replace(chr(92), '/')}"


def generate_mkdocs_yml() -> None:
    write(
        SITE / "mkdocs.yml",
        """site_name: 软件体系结构课程网站
site_description: 《软件体系结构》学生端课程资料站
site_author: 何庭钦
docs_dir: docs
site_dir: build
use_directory_urls: true

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

nav:
  - 首页: index.md
  - 课程说明: syllabus.md
  - 电子教材: textbook.md
  - 每次课:
      - 课程总览: lessons/index.md
      - 第1讲: lessons/lesson01.md
      - 第2讲: lessons/lesson02.md
      - 第3讲: lessons/lesson03.md
      - 第4讲: lessons/lesson04.md
      - 第5讲: lessons/lesson05.md
      - 第6讲: lessons/lesson06.md
      - 第7讲: lessons/lesson07.md
      - 第8讲: lessons/lesson08.md
  - 课程项目:
      - 项目总览: project/index.md
      - M1 选题与需求: project/m1.md
      - M2 建模与结构表达: project/m2.md
      - M3 架构决策与 ADR: project/m3.md
      - M4 测试交付与运维: project/m4.md
      - 项目模板: project/templates.md
  - 补充资料: resources.md
  - 复习说明: review.md

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


def generate_index() -> None:
    write(
        DOCS / "index.md",
        """# 软件体系结构

面向 2025 级电子信息工程硕士的《软件体系结构》课程资料站。

本课程关注的核心问题是：**如何从“能写代码”提升到“能控制复杂软件系统”**。

## 快速入口

| 入口 | 内容 |
|---|---|
| [电子教材](textbook.md) | 第1-8章学生阅读版电子教材 |
| [每次课](lessons/index.md) | 第1-8讲 PPT 与课后任务 |
| [课程项目](project/index.md) | M1/M2/M3/M4 阶段产出要求 |
| [补充资料](resources.md) | AI、架构、测试、交付等扩展阅读 |
| [复习说明](review.md) | 不泄露试题的期末复习范围与建议 |

## 学习主线

```text
复杂性识别
  → 过程与项目治理
  → 需求工程
  → 架构表达
  → 架构决策
  → 质量验证
  → 发布运维
```

## 资料公开边界

本站只发布学生可公开学习资料，不发布任何考试保密资料。

不会发布：

- 期末试卷 A/B 卷；
- 答案与评分细则；
- 教师题库；
- 命题质量分析；
- 教师版评分细则。
""",
    )


def generate_syllabus() -> None:
    rows = "\n".join(
        f"| 第{data['no']}讲 | {data['title']} | {data['textbook']} |"
        for data in LESSONS.values()
    )
    write(
        DOCS / "syllabus.md",
        f"""# 课程说明

## 课程定位

《软件体系结构》是一门面向专业硕士的软件工程与架构实践课程。课程不以背诵架构名词为目标，而是训练学生围绕需求、质量属性、约束、风险和交付做工程判断。

## 授课对象

- 2025级电子信息工程硕士；
- 已具备基本程序设计、数据库、网络和软件开发基础；
- 需要从单点编码能力提升到复杂系统分析、设计和治理能力。

## 课程目标

完成课程后，学生应能够：

1. 识别软件系统复杂性的主要来源；
2. 根据项目条件选择合适的开发节奏；
3. 将用户声音转化为可验证需求；
4. 使用 UML/C4 等方式表达系统结构；
5. 围绕质量属性做架构决策并撰写 ADR；
6. 设计测试策略、质量门禁和发布运维方案；
7. 在课程项目中形成完整工程材料。

## 教学安排

| 课次 | 主题 | 对应教材章节 |
|---|---|---|
{rows}

## 考核说明

课程总评采用“平时成绩 + 期末考核”的结构。学生应重点完成课堂任务、课后作业和课程项目阶段产出。

!!! warning "公开边界"
    本站只提供复习范围和学习方向，不提供正式试卷、答案、题库或评分细则。
""",
    )


def generate_textbook() -> None:
    rel = "textbook/software_architecture_textbook_student_v5_1.pdf"
    copied = copy_public_file(
        ROOT / "textbook" / "output" / "software_architecture_textbook_student_v5_1.pdf",
        rel,
    )
    download = asset_link(0, rel) if copied else "#"
    write(
        DOCS / "textbook.md",
        f"""# 电子教材

## 软件体系结构课程电子教材

版本：学生阅读版 v5.1

适用范围：第1章至第8章主教材，供课后复习、课程项目准备和期末复习使用。

[下载电子教材 PDF]({download})

## 章节目录

| 章 | 标题 | 主要用途 |
|---|---|---|
| 第1章 | 从能写代码到能控复杂系统 | 建立复杂性与架构判断视角 |
| 第2章 | 软件过程模型与开发节奏选择 | 判断开发节奏与反馈机制 |
| 第3章 | 项目管理、可行性分析与风险控制 | 支撑项目计划与风险识别 |
| 第4章 | 需求工程：从用户声音到可验证规格 | 支撑 M1 需求材料 |
| 第5章 | 架构表达与系统建模 | 支撑 M2 建模材料 |
| 第6章 | 架构设计、架构风格与分布式系统 | 支撑 M3 ADR 与架构决策 |
| 第7章 | 软件测试、质量保障与安全验证 | 支撑 M4 测试策略 |
| 第8章 | 发布、交付、运维与可观测性 | 支撑 M4 发布运维说明 |

## 使用建议

- 课前：快速阅读本次课对应章节的“本章导读”和“核心问题”。
- 课后：结合 PPT 回看方法框架、案例和误区。
- 做项目：优先查看每章的“项目提示”和模板。
- 期末复习：重点看每章小结、复习题和案例分析题。
""",
    )


def generate_lessons() -> None:
    ensure_dir(DOCS / "lessons")
    index_rows = []
    for lesson_id, data in LESSONS.items():
        lesson_src = ROOT / "input" / "lessons" / lesson_id
        ppt_rel = f"lessons/{lesson_id}/ppt.pdf"
        ppt_copied = copy_public_file(lesson_src / "ppt.pdf", ppt_rel)
        assignment_text = read_assignment(lesson_id)

        assignment_rel_public = f"lessons/{lesson_id}/assignment.md"
        write(PUBLIC / assignment_rel_public, assignment_text)
        assignment_rel_docs = f"lessons/{lesson_id}/assignment.txt"
        write(DOCS_PUBLIC / assignment_rel_docs, assignment_text)

        ppt_link = asset_link(1, ppt_rel) if ppt_copied else ""
        assignment_link = asset_link(1, assignment_rel_docs)
        index_rows.append(
            f"| [第{data['no']}讲](lesson{data['no']}.md) | {data['title']} | {data['textbook']} |"
        )
        goals = "\n".join(f"- {item}" for item in data["goals"])
        ppt_line = f"[下载 PPT PDF]({ppt_link})" if ppt_copied else "PPT PDF 暂未发布。"
        write(
            DOCS / "lessons" / f"lesson{data['no']}.md",
            f"""# 第{data['no']}讲 {data['title']}

## 本讲主题

{data['title']}

## 本讲核心问题

{data['core']}

## 学习目标

{goals}

## PPT 下载

{ppt_line}

## 对应教材章节

{data['textbook']}

## 课堂任务

{data['class_task']}

## 课后作业

{assignment_text}

[下载课后作业文本]({assignment_link})

## 补充资料

{data['extra']}
""",
        )

    write(
        DOCS / "lessons" / "index.md",
        """# 每次课资料

本栏目提供第1-8讲的 PPT PDF、课后作业与对应教材章节。

| 课次 | 主题 | 对应教材 |
|---|---|---|
"""
        + "\n".join(index_rows),
    )


def generate_project_templates() -> None:
    templates = {
        "m1_requirements_template.txt": """# M1 选题与需求模板

## 项目名称

## 小组成员与分工

## 目标用户

## 典型使用场景

## 核心功能

## 初步质量属性

## 主要约束
""",
        "m2_modeling_template.txt": """# M2 建模与结构表达模板

## 系统边界

## C1 上下文图说明

## C2 容器/模块图说明

## 核心场景时序图

## 领域对象或关键类

## 模型自查
""",
        "m3_adr_template.txt": """# M3 ADR 模板

## ADR 编号与标题

## 背景与约束

## 决策

## 放弃方案

## 理由

## 风险

## 观察指标
""",
        "m4_testing_delivery_template.txt": """# M4 测试、交付与运维模板

## 测试范围

## 测试层级

## 质量门禁

## 发布流程

## 回滚条件

## 日志、指标、追踪

## 故障处理与复盘
""",
    }
    for name, content in templates.items():
        write(PUBLIC / "project" / name.replace(".txt", ".md"), content)
        write(DOCS_PUBLIC / "project" / name, content)


def generate_project_pages() -> None:
    ensure_dir(DOCS / "project")
    generate_project_templates()
    rows = []
    for key, data in PROJECTS.items():
        rows.append(f"| [{key.upper()}]({key}.md) | {data['title']} | {data['goal']} |")
    write(
        DOCS / "project" / "index.md",
        """# 课程项目

课程项目按 M1-M4 推进。每个阶段都对应前面课程中的一个能力目标。

| 阶段 | 名称 | 目标 |
|---|---|---|
"""
        + "\n".join(rows)
        + """

## 分组建议

- 4-6人一组；
- 明确组长、需求负责人、建模负责人、架构负责人、测试交付负责人；
- 每次提交都要说明成员分工和主要贡献。
""",
    )

    for key, data in PROJECTS.items():
        submit = "\n".join(f"- {item}" for item in data["submit"])
        template_link = asset_link(1, f"project/{data['template']}")
        write(
            DOCS / "project" / f"{key}.md",
            f"""# {data['title']}

## 产出目标

{data['goal']}

## 提交材料

{submit}

## 格式要求

{data['format']}

## 建议模板

[下载 {data['title']} 模板]({template_link})

## 质量检查清单

- 是否能让没有参与项目的人理解系统要解决的问题；
- 是否有清楚的前因、约束、判断和结果；
- 是否避免只列工具名或空泛口号；
- 是否能支撑后续阶段继续推进。
""",
        )

    template_rows = "\n".join(
        f"| {data['title']} | [{data['template']}]({asset_link(1, f'project/{data['template']}')}) |"
        for data in PROJECTS.values()
    )
    write(
        DOCS / "project" / "templates.md",
        f"""# 项目模板

| 阶段 | 模板 |
|---|---|
{template_rows}

这些模板是学生提交材料的结构建议，可以根据具体项目适当调整。
""",
    )


def generate_resources_and_review() -> None:
    write(
        DOCS / "resources.md",
        """# 补充资料

## AI 时代的软件工程

AI 工具可以辅助需求澄清、代码生成、测试用例生成和文档整理，但不能替代架构判断、风险识别和人工审查。

建议结合第9讲公开课件与作业要求进行扩展学习。第9讲不纳入主教材正文，但可作为课程专题资料。

## 架构与工程实践扩展方向

- ADR：记录架构决策、放弃方案、风险和观察指标；
- C4：用分层视图表达系统上下文、容器、组件和代码结构；
- 质量门禁：把质量要求转化为可执行检查；
- 可观测性：用日志、指标、追踪理解运行系统。

## 使用建议

补充资料用于拓展理解，不替代电子教材第1-8章和课堂 PPT。
""",
    )

    write(
        DOCS / "review.md",
        """# 期末复习范围说明

本页只说明复习范围和学习方向，不包含正式试题、答案、题库或评分细则。

## 复习范围

期末复习以电子教材第1-8章、课堂 PPT、课后作业和课程项目材料为主。

重点关注：

1. 软件复杂性、FR/QA/C、架构时间账；
2. 过程模型与开发节奏选择；
3. 项目管理、WBS、里程碑、风险控制；
4. 需求工程、用例、可验证规格、质量属性场景；
5. UML/C4 建模与架构表达；
6. 架构决策、ADR、模块化单体、微服务与分布式单体；
7. 测试层级、质量门禁、安全验证；
8. CI/CD、发布策略、回滚、可观测性和复盘。

## 复习建议

- 先看每章“本章小结”和“你要记住”；
- 再结合 PPT 复习核心图示；
- 最后用课程项目材料练习案例分析。

## 能力要求

复习时不要只背概念，要能解释：

- 这个概念解决什么问题；
- 适用于什么场景；
- 错用会产生什么后果；
- 如何结合实验室预约与设备管理系统或自己的课程项目说明。
""",
    )


def generate_readme_and_report() -> None:
    write(
        SITE / "README.md",
        """# 《软件体系结构》学生端课程网站

## 本地预览

```powershell
cd D:\\Codex\\SoftwareArchitecture2026\\software-architecture-course-2026\\site
python -m mkdocs serve
```

浏览器访问：

```text
http://127.0.0.1:8000
```

## 构建静态站点

```powershell
cd D:\\Codex\\SoftwareArchitecture2026\\software-architecture-course-2026\\site
python -m mkdocs build --clean
```

构建结果位于：

```text
site/build/
```

## 发布说明

发布前必须先运行：

```powershell
python scripts/validate_public_assets.py
```

如果出现考试资料、教师版资料、答案、评分细则、题库等敏感文件，必须删除后再发布。
""",
    )

    lesson_rows = "\n".join(
        f"| 第{data['no']}讲 | {data['title']} | PPT PDF + 作业 |" for data in LESSONS.values()
    )
    write(
        SITE / "site_generation_report.md",
        f"""# 学生端课程网站生成报告

## 生成内容

| 类型 | 文件/目录 |
|---|---|
| MkDocs 配置 | `site/mkdocs.yml` |
| 页面源码 | `site/docs/` |
| 公开资产源目录 | `site/public/` |
| MkDocs 可发布资产镜像 | `site/docs/public/` |
| 本地预览说明 | `site/README.md` |
| 泄密检查报告 | `site/private_file_leak_check.md` |

## 已生成页面

- 首页：`docs/index.md`
- 课程说明：`docs/syllabus.md`
- 电子教材：`docs/textbook.md`
- 每次课：`docs/lessons/lesson01.md` 至 `lesson08.md`
- 课程项目：`docs/project/`
- 补充资料：`docs/resources.md`
- 复习说明：`docs/review.md`

## 已复制公开资料

| 课次 | 主题 | 资料 |
|---|---|---|
{lesson_rows}

电子教材：

- `textbook/output/software_architecture_textbook_student_v5_1.pdf`

## 处理说明

1. `lesson03` 已由 PowerPoint COM 从 PPTX 导出为 PDF 后纳入网站。
2. 站点只生成 lesson01 至 lesson08 页面；lesson09 可后续作为专题补充加入。
3. `site/public/` 按用户要求保存公开资产；`site/docs/public/` 是 MkDocs 构建可访问镜像。
4. 未复制 `exam/` 下任何文件。
5. 未复制 `teacher_only`、`answer_key`、`paper_A`、`paper_B`、教师版答案与评分细则等考试保密资料。
""",
    )


def main() -> None:
    ensure_dir(DOCS)
    ensure_dir(PUBLIC)
    ensure_dir(DOCS_PUBLIC)
    generate_mkdocs_yml()
    generate_index()
    generate_syllabus()
    generate_textbook()
    generate_lessons()
    generate_project_pages()
    generate_resources_and_review()
    generate_readme_and_report()


if __name__ == "__main__":
    main()
