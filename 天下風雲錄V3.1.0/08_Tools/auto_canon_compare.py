#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
天下風雲錄 Auto Canon Compare Tool

用途：
- 以 Story Bible 作為最高 Canon。
- 自動比對 Story Bible 與 Official Patch Notes。
- 產生 Markdown 交叉比對報告。

注意：
- 本工具只讀取與產生報告，不會修改 Story Bible 或 Patch Notes。
- 判定結果為輔助檢查，最終仍以 Story Bible 原文為準。
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class Section:
    level: int
    title: str
    line: int
    body: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_sections(text: str) -> list[Section]:
    lines = text.splitlines()
    headings: list[tuple[int, str, int]] = []

    for idx, line in enumerate(lines, start=1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            headings.append((len(match.group(1)), match.group(2).strip(), idx))

    sections: list[Section] = []
    for i, (level, title, start_line) in enumerate(headings):
        end_line = headings[i + 1][2] - 1 if i + 1 < len(headings) else len(lines)
        body = "\n".join(lines[start_line:end_line])
        sections.append(Section(level=level, title=title, line=start_line, body=body))

    return sections


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[`*_>#\-•①②③④⑤（）()：:，,。.!！?？\s]+", "", text)
    return text


def extract_terms(text: str) -> set[str]:
    patterns = [
        r"[\u4e00-\u9fff]{2,12}",
        r"[A-Za-z][A-Za-z0-9_ /.-]{2,40}",
        r"MC-\d+",
        r"CD-\d+-\d+",
        r"v\d+\.\d+(?:\.\d+)?",
    ]

    terms: set[str] = set()
    for pattern in patterns:
        for match in re.findall(pattern, text):
            term = match.strip()
            if len(term) >= 2:
                terms.add(term)
    return terms


def sentence_split(text: str) -> list[str]:
    raw = re.split(r"(?<=[。！？.!?])\s+|\n+", text)
    return [s.strip() for s in raw if len(s.strip()) >= 6]


def find_keyword_hits(source_text: str, target_text: str, keywords: Iterable[str]) -> list[str]:
    target_norm = normalize(target_text)
    hits = []
    for keyword in keywords:
        key = normalize(keyword)
        if key and key in target_norm:
            hits.append(keyword)
    return sorted(set(hits))


def compare(story_text: str, patch_text: str) -> dict[str, object]:
    story_sections = extract_sections(story_text)
    patch_sections = extract_sections(patch_text)

    story_terms = extract_terms(story_text)
    patch_terms = extract_terms(patch_text)

    story_norm = normalize(story_text)
    patch_norm = normalize(patch_text)

    critical_terms = [
        "Story Bible",
        "Official Canon",
        "英雄，因天下而誕生",
        "生而微末者，當真無聲嗎",
        "蒼生無言，俠為其聲",
        "世界自行運轉",
        "第一人稱",
        "墨羽視角",
        "玩家知道",
        "墨羽知道",
        "不得使用上帝視角",
        "不得提前透露",
        "幕後真相",
        "他人內心",
        "未來事件",
        "隱藏情報",
        "四個基礎互動選項",
        "自由行動",
        "隱藏互動選項",
        "人格",
        "執念",
        "核心信念",
    ]

    critical_hits = find_keyword_hits(story_text, patch_text, critical_terms)
    critical_missing = sorted(set(critical_terms) - set(critical_hits))

    patch_only_terms = sorted(
        term for term in (patch_terms - story_terms)
        if len(term) >= 3 and not re.fullmatch(r"v\d+\.\d+(?:\.\d+)?", term)
    )

    story_only_terms = sorted(
        term for term in (story_terms - patch_terms)
        if len(term) >= 3
    )

    # Simple contradiction heuristics.
    warnings: list[str] = []
    if "每回合固定提供四個互動選項" in patch_text and "隱藏互動選項" in patch_text:
        if "四個基礎互動選項" not in patch_text:
            warnings.append("Patch Notes 同時存在『固定四個互動選項』與『隱藏互動選項』，但未明確區分基礎選項與條件式選項。")

    if "不得使用上帝視角" in story_text and "上帝視角" not in patch_text:
        warnings.append("Story Bible 明確禁止上帝視角，但 Patch Notes 未明確反映。")

    if "玩家知道的資訊，必須等於墨羽知道的資訊" in story_text:
        if "玩家知道" not in patch_text or "墨羽知道" not in patch_text:
            warnings.append("Story Bible 明確規定『玩家知道＝墨羽知道』，但 Patch Notes 未完整反映。")

    return {
        "story_sections": story_sections,
        "patch_sections": patch_sections,
        "critical_hits": critical_hits,
        "critical_missing": critical_missing,
        "patch_only_terms": patch_only_terms[:200],
        "story_only_terms": story_only_terms[:200],
        "warnings": warnings,
        "story_section_count": len(story_sections),
        "patch_section_count": len(patch_sections),
        "story_line_count": len(story_text.splitlines()),
        "patch_line_count": len(patch_text.splitlines()),
    }


def render_report(result: dict[str, object], story_path: Path, patch_path: Path) -> str:
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    critical_hits = result["critical_hits"]
    critical_missing = result["critical_missing"]
    warnings = result["warnings"]
    patch_only_terms = result["patch_only_terms"]
    story_only_terms = result["story_only_terms"]

    lines: list[str] = []
    lines.append("# 天下風雲錄 Canon 自動交叉比對報告")
    lines.append("")
    lines.append(f"> Generated: {now}")
    lines.append(f"> Story Bible: `{story_path}`")
    lines.append(f"> Patch Notes: `{patch_path}`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# 一、文件統計")
    lines.append("")
    lines.append(f"- Story Bible 行數：{result['story_line_count']}")
    lines.append(f"- Patch Notes 行數：{result['patch_line_count']}")
    lines.append(f"- Story Bible 標題段落數：{result['story_section_count']}")
    lines.append(f"- Patch Notes 標題段落數：{result['patch_section_count']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# 二、核心 Canon 關鍵項檢查")
    lines.append("")
    lines.append("## 已反映")
    lines.append("")
    if critical_hits:
        for item in critical_hits:
            lines.append(f"- {item}")
    else:
        lines.append("- 無")
    lines.append("")
    lines.append("## 需人工確認或可能未反映")
    lines.append("")
    if critical_missing:
        for item in critical_missing:
            lines.append(f"- {item}")
    else:
        lines.append("- 無")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# 三、警告項目")
    lines.append("")
    if warnings:
        for item in warnings:
            lines.append(f"- ⚠️ {item}")
    else:
        lines.append("- 未偵測到明顯規則衝突。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# 四、Patch Notes 可能超出 Story Bible 的詞項")
    lines.append("")
    lines.append("> 以下為自動詞項比對結果，不等於必然衝突；需人工依 Story Bible 判定。")
    lines.append("")
    if patch_only_terms:
        for item in patch_only_terms:
            lines.append(f"- {item}")
    else:
        lines.append("- 無")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# 五、Story Bible 可能未反映於 Patch Notes 的詞項")
    lines.append("")
    lines.append("> Patch Notes 不必完整收錄 Story Bible；此區僅供檢查是否有版本更新應補記。")
    lines.append("")
    if story_only_terms:
        for item in story_only_terms:
            lines.append(f"- {item}")
    else:
        lines.append("- 無")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("# 六、判定原則")
    lines.append("")
    lines.append("1. Story Bible 為最高 Official Canon。")
    lines.append("2. Patch Notes 僅作為版本變更紀錄。")
    lines.append("3. 若 Patch Notes 與 Story Bible 發生衝突，依 Story Bible 為準。")
    lines.append("4. 本報告為自動輔助檢查，不自動修改任何正式文件。")
    lines.append("")
    lines.append("# End of Report")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare Story Bible and Patch Notes for Canon consistency.")
    parser.add_argument("--story", required=True, type=Path, help="Path to Story Bible markdown file.")
    parser.add_argument("--patch", required=True, type=Path, help="Path to Patch Notes markdown file.")
    parser.add_argument("--out", required=True, type=Path, help="Output markdown report path.")
    args = parser.parse_args()

    story_text = read_text(args.story)
    patch_text = read_text(args.patch)
    result = compare(story_text, patch_text)
    report = render_report(result, args.story, args.patch)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report, encoding="utf-8")

    print(f"Report written: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
