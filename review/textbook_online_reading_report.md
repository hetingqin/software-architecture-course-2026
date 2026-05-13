# 电子教材在线阅读化报告

## 处理结果

| 项目 | 结果 |
|---|---|
| 章节来源 | `textbook/chapters_illustrated_student/`，缺失时回退到 `textbook/chapters_v4/` |
| 生成章节 | 8 个 |
| 教材 PDF | 已复制到 `site/assets/textbook/` |
| 教材附图 | 已复制 29 张 |
| 在线阅读方式 | Markdown 章节正文 |

## 生成页面

- `docs/textbook/chapter01.md`
- `docs/textbook/chapter02.md`
- `docs/textbook/chapter03.md`
- `docs/textbook/chapter04.md`
- `docs/textbook/chapter05.md`
- `docs/textbook/chapter06.md`
- `docs/textbook/chapter07.md`
- `docs/textbook/chapter08.md`

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
