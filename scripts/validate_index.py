#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import sys
from dataclasses import dataclass
from typing import Iterable, List, Optional


REQUIRED_COLUMNS = [
    "exam",
    "subject",
    "level",
    "year",
    "month",
    "region",
    "source_url",
    "license",
    "file_path",
    "notes",
]


@dataclass(frozen=True)
class RowError:
    row_number: int
    message: str


def _is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except Exception:
        return False


def validate_rows(rows: Iterable[dict]) -> List[RowError]:
    errors: List[RowError] = []
    seen_keys = set()

    for idx, r in enumerate(rows, start=2):  # header is line 1
        exam = (r.get("exam") or "").strip()
        subject = (r.get("subject") or "").strip()
        level = (r.get("level") or "").strip()
        year = (r.get("year") or "").strip()
        month = (r.get("month") or "").strip()
        file_path = (r.get("file_path") or "").strip()
        source_url = (r.get("source_url") or "").strip()

        if not exam:
            errors.append(RowError(idx, "exam 不能为空"))
        elif exam not in {"zikao", "pets"}:
            errors.append(RowError(idx, "exam 必须是 zikao 或 pets"))

        if year and not _is_int(year):
            errors.append(RowError(idx, "year 必须是整数或留空"))
        if month and (not _is_int(month) or not (1 <= int(month) <= 12)):
            errors.append(RowError(idx, "month 必须是 1-12 的整数或留空"))

        if exam == "zikao" and not subject:
            errors.append(RowError(idx, "zikao 记录必须填写 subject（如 english-2）"))
        if exam == "pets" and not level:
            errors.append(RowError(idx, "pets 记录必须填写 level（如 PETS-2）"))

        if level and not level.startswith("PETS-"):
            errors.append(RowError(idx, "level 建议格式为 PETS-1/2/3/4/5"))

        if not source_url and not file_path:
            errors.append(RowError(idx, "source_url 与 file_path 至少填写一个"))

        if file_path:
            if os.path.isabs(file_path):
                errors.append(RowError(idx, "file_path 请使用仓库相对路径（不要写绝对路径）"))
            else:
                normalized = file_path.replace("\\", "/")
                if ".." in normalized.split("/"):
                    errors.append(RowError(idx, "file_path 不允许包含 .."))
                if not os.path.exists(normalized):
                    errors.append(RowError(idx, f"file_path 不存在：{file_path}"))

        key = (exam, subject, level, year, month)
        if key in seen_keys:
            errors.append(RowError(idx, "疑似重复记录（exam/subject/level/year/month 相同）"))
        else:
            seen_keys.add(key)

    return errors


def main(argv: List[str]) -> int:
    path = "index/papers.csv"
    if len(argv) > 1:
        path = argv[1]

    if not os.path.exists(path):
        print(f"找不到索引文件：{path}", file=sys.stderr)
        return 2

    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            print(f"缺少列：{', '.join(missing)}", file=sys.stderr)
            return 2

        errors = validate_rows(reader)

    if errors:
        for e in errors:
            print(f"第 {e.row_number} 行：{e.message}", file=sys.stderr)
        return 1

    print("索引校验通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

