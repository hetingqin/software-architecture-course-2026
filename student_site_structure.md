# 学生端课程网站结构设计

## 一、总体结构

网站采用“首页 + 六个一级入口”的结构，避免做成复杂平台。

```text
首页
├─ 课程说明
├─ 电子教材
├─ 每次课
├─ 课程项目
├─ 补充资料
└─ 复习说明
```

## 二、一级栏目设计

### 2.1 首页

建议路径：

```text
site/docs/index.md
```

页面内容：

- 课程名称：软件体系结构；
- 课程定位：从“能写代码”到“能控复杂系统”；
- 学习入口卡片：电子教材、每次课、课程项目、复习说明；
- 最近更新；
- 资料使用说明；
- 保密提醒：网站不发布试卷、答案、题库等考试材料。

### 2.2 课程说明

建议路径：

```text
site/docs/course/overview.md
site/docs/course/schedule.md
site/docs/course/assessment.md
```

页面内容：

| 页面 | 内容 |
|---|---|
| `overview.md` | 课程目标、学习对象、课程主线、能力目标 |
| `schedule.md` | 10次课安排，列出主题与对应教材章节 |
| `assessment.md` | 公开版考核说明，只写平时/期末比例、项目要求和学习建议，不写教师评分细则 |

### 2.3 电子教材

建议路径：

```text
site/docs/textbook/index.md
site/docs/assets/textbook/software_architecture_textbook_student_v5_1.pdf
```

页面内容：

- 教材名称；
- 版本号：学生阅读版 v5.1；
- 适用范围：第1-8章主教材；
- 下载链接；
- 使用建议：课后复习、项目材料准备、期末复习；
- 章节目录简表。

### 2.4 每次课

建议路径：

```text
site/docs/lessons/index.md
site/docs/lessons/lesson01.md
site/docs/lessons/lesson02.md
...
site/docs/lessons/lesson10.md
```

每次课页面统一包含：

1. 本讲主题；
2. 本讲核心问题；
3. 学习目标；
4. PPT PDF 下载；
5. 课后任务；
6. 关键词；
7. 与课程项目的关系；
8. 扩展阅读或补充材料。

建议页面列表：

| 页面 | 主题建议 | 公开资料 |
|---|---|---|
| `lesson01.md` | 从能写代码到能控复杂系统 | PPT PDF、作业 |
| `lesson02.md` | 软件过程模型与开发节奏选择 | PPT PDF、作业 |
| `lesson03.md` | 项目管理、可行性分析与风险控制 | 需补 PPT PDF、作业 |
| `lesson04.md` | 需求工程：从用户声音到可验证规格 | PPT PDF、作业 |
| `lesson05.md` | 架构表达与系统建模 | PPT PDF、作业 |
| `lesson06.md` | 架构设计、架构风格与分布式系统 | PPT PDF、作业 |
| `lesson07.md` | 软件测试、质量保障与安全验证 | PPT PDF、作业 |
| `lesson08.md` | 发布、交付、运维与可观测性 | PPT PDF、作业 |
| `lesson09.md` | AI 时代的软件工程与架构治理 | PPT PDF、作业、扩展阅读 |
| `lesson10.md` | 综合案例与课程项目汇报 | 作业/汇报要求，后续补 PPT |

### 2.5 课程项目

建议路径：

```text
site/docs/project/index.md
site/docs/project/m1.md
site/docs/project/m2.md
site/docs/project/m3.md
site/docs/project/m4.md
site/docs/project/templates.md
```

页面内容：

| 页面 | 内容 |
|---|---|
| `index.md` | 项目总体说明、分组方式、提交节奏 |
| `m1.md` | 选题与需求分析 |
| `m2.md` | 建模与结构表达 |
| `m3.md` | 架构决策与 ADR |
| `m4.md` | 测试、交付与运维说明 |
| `templates.md` | ADR、技术债、测试计划、交付说明模板 |

学生端项目页面只说明要求和模板，不发布教师评分细则。

### 2.6 补充资料

建议路径：

```text
site/docs/resources/index.md
site/docs/resources/ai_engineering.md
site/docs/resources/architecture_reading.md
site/docs/resources/tools.md
```

页面内容：

- AI 时代软件工程专题；
- 架构决策与 ADR 扩展阅读；
- 软件测试与质量门禁资料；
- 发布、运维与可观测性资料；
- 合法公开的工具文档链接。

所有外部链接后续需要单独检查有效性和适合度。

### 2.7 复习说明

建议路径：

```text
site/docs/review/index.md
```

页面内容：

- 期末复习范围；
- 第1-8章复习重点；
- 题型方向说明；
- 复习建议；
- 课程项目与复习的关系。

禁止包含：

- 正式试题；
- A/B 卷；
- 题库；
- 答案；
- 评分细则；
- 命题质量分析。

## 三、站点导航建议

```yaml
nav:
  - 首页: index.md
  - 课程说明:
      - 课程概览: course/overview.md
      - 教学安排: course/schedule.md
      - 考核说明: course/assessment.md
  - 电子教材: textbook/index.md
  - 每次课:
      - 总览: lessons/index.md
      - 第1讲: lessons/lesson01.md
      - 第2讲: lessons/lesson02.md
      - 第3讲: lessons/lesson03.md
      - 第4讲: lessons/lesson04.md
      - 第5讲: lessons/lesson05.md
      - 第6讲: lessons/lesson06.md
      - 第7讲: lessons/lesson07.md
      - 第8讲: lessons/lesson08.md
      - 专题: lessons/lesson09.md
      - 项目汇报: lessons/lesson10.md
  - 课程项目:
      - 项目总览: project/index.md
      - M1: project/m1.md
      - M2: project/m2.md
      - M3: project/m3.md
      - M4: project/m4.md
      - 模板: project/templates.md
  - 补充资料: resources/index.md
  - 复习说明: review/index.md
```

## 四、页面内容模板

每次课页面建议采用固定模板：

```markdown
# 第x讲 标题

## 本讲核心问题

## 学习目标

## 课件下载

## 课后任务

## 关键词

## 与课程项目的关系

## 扩展阅读
```

课程项目页面建议采用固定模板：

```markdown
# Mx 标题

## 产出目标

## 提交内容

## 推荐结构

## 质量检查清单

## 常见问题
```

## 五、资产存放规则

```text
site/docs/assets/textbook/       # 学生教材 PDF
site/docs/assets/lessons/        # 每次课 PPT PDF 和作业
site/docs/assets/project/        # 项目模板
site/docs/assets/resources/      # 扩展资料
```

禁止在上述目录中出现考试保密材料。

## 六、后续生成网站前的必要动作

1. 补导出 `lesson03/ppt.pdf`。
2. 确认 `lesson10` 是否需要 PPT。
3. 决定是否公开 `outline.md`。
4. 从教材抽取 M1-M4 学生模板。
5. 单独生成公开安全的复习说明。
6. 建立发布前敏感文件扫描脚本。
