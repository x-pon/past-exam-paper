# past-exam-paper

历年考试真题（与整理索引）资料库。首批计划收录：

- 自考：英语（二）
- 公共英语：PETS（全国公共英语等级考试）

## 重要说明（请先读）

本仓库的目标是**整理与索引**历年真题（如：年份/月份/科目/来源链接/勘误与笔记），以便学习与检索。

- 真题及其扫描件/PDF/图片等通常受版权保护；**请勿在未获授权的情况下上传受版权保护的原始试卷文件**。
- 如果你拥有授权，或试卷已明确处于可自由传播的许可下，可在索引中标注来源与许可，再上传对应文件。
- 仓库中由贡献者原创的整理内容（如：目录结构、索引、勘误、笔记）按仓库许可证与内容许可协议执行，详见 `LICENSE` 与 `CONTENT_LICENSE`。

## 目录结构

```
papers/
  zikao/
    english-2/
      README.md
  pets/
    README.md
index/
  papers.csv
scripts/
  validate_index.py
DISCLAIMER.md
CONTENT_LICENSE
LICENSE
CONTRIBUTING.md
CODE_OF_CONDUCT.md
```

## 如何添加一套真题

1. 选择考试目录：
   - 自考英语（二）：`papers/zikao/english-2/`
   - 公共英语 PETS：`papers/pets/`
2. 将“可公开分发”的文件放在对应目录下（如：`YYYY-MM/`）。
3. 在 `index/papers.csv` 追加一行索引信息（推荐提供权威来源链接）。
4. 运行索引校验（可选）：

```bash
python3 scripts/validate_index.py
```

## 快速开始（推荐工作流）

- 只收录索引与来源链接：最安全、可持续
- 若收录文件：务必在索引中注明来源与许可，并确保你有分发权

## 贡献

欢迎提交真题“索引”、勘误、目录整理与学习笔记。请先阅读 `CONTRIBUTING.md`。

