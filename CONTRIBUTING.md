# 贡献指南

欢迎贡献以下内容：

- 真题索引（年份/月份/科目/等级/来源链接）
- 勘误（题干、答案、解析错误等）
- 原创学习笔记与整理

## 贡献前提

- 请勿上传你无权分发的受版权保护真题文件（扫描件/PDF/图片/音频等）。
- 推荐只提交 `index/papers.csv` 的索引与权威来源链接。

## 如何贡献

1. Fork 本仓库并创建分支
2. 修改/新增内容
   - 索引：编辑 `index/papers.csv`
   - 目录说明：编辑对应 `papers/**/README.md`
3. 可选：本地校验索引

```bash
python3 scripts/validate_index.py
```

4. 提交 Pull Request，并在描述中写清楚新增了哪些年份/月份/等级

## 索引字段说明（`index/papers.csv`）

- `exam`: `shed`（自考，目录缩写 **SHED**）/ `pets`
- `subject`: 如 `english-2`（PETS 可留空）
- `level`: PETS 等级，如 `PETS-2`（`shed` 可留空）
- `year`/`month`: 数字（month 建议两位）
- `source_url`: 权威来源链接（强烈推荐）
- `license`: 若上传文件，注明许可/授权信息
- `file_path`: 对应仓库内目录（可为空；若填写，校验脚本会检查路径存在）
- `notes`: 备注

