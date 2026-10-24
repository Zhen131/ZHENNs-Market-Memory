#!/usr/bin/env python3
"""历史金融图谱 · 全库检查。只依赖 Python 3 标准库。

在 vault 根目录运行：
  python3 99_工具/脚本/check.py                 检查全库，并更新 00_首页/视图/待建节点.md
  python3 99_工具/脚本/check.py -v              同时列出全部警告
  python3 99_工具/脚本/check.py --no-report     只检查，不写报告

有错误时退出码为 1。规则依据见 AGENTS.md 第 5、6、8、12 节。
"""
import datetime
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "00_首页" / "视图" / "待建节点.md"

SKIP_PREFIXES = ("99Z_等待入库文件/", "99_工具/模板/")
FAT_LIMIT = 5000  # 正文超过这么多字就警告「卡片太长」，见 AGENTS.md 第 12.4 节
GUIDE_AT = 20     # 观点文件夹到这么多张卡要有导览，见 AGENTS.md 第 8.5 节
SPLIT_AT = 50     # 观点文件夹到这么多张卡要分子文件夹，见 AGENTS.md 第 8.5 节
NO_FM_OK = ("README.md", "AGENTS.md")  # 以及 99_工具/ 下的说明文件

ENUMS = {
    "type": {"event", "entity", "asset", "concept", "pattern", "comparison", "method",
             "view", "timeline", "overview", "note"},
    "status": {"draft", "active", "reviewed", "archived"},
    "source_status": {"unsourced", "partially-sourced", "sourced", "verified"},
    "entity_kind": {"country", "company", "institution", "person", "place"},
    "view_kind": {"framework", "judgment", "prediction", "action", "case"},
    "fact_check": {"unchecked", "consistent", "inconsistent", "mixed"},
    "outcome": {"pending", "hit", "miss", "partial", "void"},
    "region": {"global", "asia", "europe", "north-america", "latin-america", "middle-east", "africa", "oceania"},
}
COMMON = ["type", "status", "title", "source_status", "sources", "tags", "created", "updated"]
REQUIRED = {
    "event": ["start_year", "decade"],
    "entity": ["entity_kind"],
    "view": ["view_kind", "speaker", "said_on", "said_in", "about", "fact_check"],
}
NEEDS_SUMMARY = {"event", "entity", "asset", "concept", "pattern", "comparison", "method", "view"}
LINK_LIST = {"countries", "actors", "assets", "patterns", "concepts", "related", "led_to", "broader",
             "cases", "methods", "origin", "applies_to", "about", "based_on"}
LINK_ONE = {"currency", "central_bank", "speaker", "changed_from"}
HOME_OF = {
    "event": "02_事件/", "entity": "04_主体/", "asset": "05_资产/", "concept": "06_概念/",
    "pattern": "03_模式/", "comparison": "07_对比/", "method": "08_方法/", "view": "10_观点/",
    "timeline": "01_时间线/", "note": "20_我的/",
}
MODULE_ROOT = re.compile(r"^(0[1-8]|1\d|20)_[^/]+/[^/]+\.md$")

WIKILINK = re.compile(r"(!?)\[\[([^\]\n]+?)\]\]")
BLOCK_ID = re.compile(r"(?:^|\s)\^([A-Za-z0-9-]+)\s*$", re.M)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
SAID_IN = re.compile(r"^(\d{4}(?:-\d{2}){0,2}) \S")


# ------------------------------------------------------------------ YAML
def unq(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] == '"':
        return json.loads(v)
    if len(v) >= 2 and v[0] == v[-1] == "'":
        return v[1:-1].replace("''", "'")
    v = re.sub(r"\s+#.*$", "", v)  # 去掉未加引号的值后面的注释
    return v


def split_inline(s):
    out, cur, q = [], "", None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q, cur = ch, cur + ch
        elif ch == ",":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return [unq(x) for x in out]


def split_fm(text):
    """返回 (frontmatter 原文 或 None, 正文)。"""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        if text.rstrip().endswith("\n---"):
            return text[4:text.rstrip().rfind("\n---")], ""
        return None, text
    return text[4:end], text[end + 5:]


def parse_yaml(raw):
    data, key = {}, None
    for i, line in enumerate(raw.split("\n"), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):(?:\s+(.*))?$", line)
        if m:
            key, val = m.group(1), (m.group(2) or "").strip()
            val = "" if val.startswith("#") else val
            if val == "":
                data[key] = None
            elif val.startswith("[") and val.rstrip().endswith("]") and not val.startswith("[["):
                data[key] = split_inline(val.strip()[1:-1])
            else:
                data[key] = unq(val)
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m and key is not None:
            if data[key] is None:
                data[key] = []
            if not isinstance(data[key], list):
                raise ValueError(f"第 {i} 行：列表项挂在单值字段 {key} 下面")
            data[key].append(unq(m.group(1)))
            continue
        raise ValueError(f"第 {i} 行无法解析：{line.strip()[:60]}")
    return data


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def body_chars(body):
    """正文字数：去掉代码、注释、嵌入、链接语法和空白后的字符数。"""
    text = strip_code(body)
    text = re.sub(r"!\[\[[^\]]*\]\]", "", text)
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", text)
    return len(re.sub(r"\s", "", text))


# ------------------------------------------------------------------ 收集
def collect():
    """返回 (要检查的笔记, 只用来解析链接的其他文件)。
    模板、收件箱和原始文件不检查，但链接指向它们时要能解析。"""
    notes, others = {}, {}
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(part.startswith(".") for part in rel.split("/")) or "__pycache__" in rel:
            continue
        skip = rel.startswith(SKIP_PREFIXES) or "/_原始文件/" in f"/{rel}"
        if p.suffix == ".md" and not skip:
            notes[rel] = p
        else:
            others[rel] = p
    return notes, others


def main():
    args = sys.argv[1:]
    verbose = "-v" in args
    write_report = "--no-report" not in args

    errors, warnings = defaultdict(list), defaultdict(list)
    notes, others = collect()

    # 名称索引：笔记按文件名（不含 .md），其他文件按带扩展名的文件名
    by_name = defaultdict(list)
    for rel in notes:
        by_name[Path(rel).stem.casefold()].append(rel)
    for rel in others:
        key = Path(rel).stem if rel.endswith(".md") else Path(rel).name
        by_name[key.casefold()].append(rel)
    report_rel = REPORT.relative_to(ROOT).as_posix()
    if REPORT.stem.casefold() not in by_name:
        by_name[REPORT.stem.casefold()].append(report_rel)
    for name, rels in by_name.items():
        if len(rels) > 1:
            errors["文件名重复"].append(f"{Path(rels[0]).name}：{'、'.join(rels)}")

    parsed = {}
    for rel, p in notes.items():
        text = p.read_text(encoding="utf-8")
        raw, body = split_fm(text)
        fm = None
        if raw is not None:
            try:
                fm = parse_yaml(raw)
            except ValueError as e:
                errors["YAML 无法解析"].append(f"{rel}：{e}")
        parsed[rel] = dict(fm=fm, body=body, raw=raw,
                           blocks=BLOCK_ID.findall(body),
                           headings={h.strip() for h in HEADING.findall(body)})

    # 别名
    owner = {}
    for rel in notes:
        owner[Path(rel).stem.casefold()] = rel
    for rel, n in parsed.items():
        fm = n["fm"] or {}
        al = fm.get("aliases") or []
        if isinstance(al, str):
            errors["aliases 必须是列表"].append(rel)
            continue
        for a in al:
            k = str(a).casefold()
            if k in owner and owner[k] != rel:
                errors["别名冲突"].append(f"「{a}」：{rel} 与 {owner[k]}")
            else:
                owner[k] = rel

    def resolve(name):
        name = name.strip().split("/")[-1]
        key = name.casefold()
        if key in by_name:
            return by_name[key][0]
        if key in owner:
            return None  # 链到别名：Obsidian 不会按别名解析
        return None

    # 逐篇检查
    unresolved = defaultdict(set)
    today = datetime.date.today().isoformat()
    for rel, n in parsed.items():
        fm, body = n["fm"], n["body"]
        top_ok_without_fm = rel in NO_FM_OK or rel.startswith("99_工具/") or rel.startswith("00_首页/视图/")
        if fm is None:
            if not top_ok_without_fm and n["raw"] is None:
                errors["缺少 YAML"].append(rel)
            fm = {}

        # 块 ID 不重复
        seen = set()
        for b in n["blocks"]:
            if b in seen:
                errors["块 ID 重复"].append(f"{rel}：^{b}")
            seen.add(b)

        t = fm.get("type")
        if fm:
            for k, allowed in ENUMS.items():
                v = fm.get(k)
                if v not in (None, "") and v not in allowed:
                    errors["枚举值不合法"].append(f"{rel}：{k} = {v}")
            if t in ENUMS["type"] and t != "note":
                for k in COMMON:
                    if k not in fm:
                        errors["缺少必填字段"].append(f"{rel}：{k}")
            for k in REQUIRED.get(t, []):
                if fm.get(k) in (None, "", []):
                    errors["缺少必填字段"].append(f"{rel}：{k}")
            if t in NEEDS_SUMMARY:
                s = fm.get("summary")
                if not s:
                    warnings["缺少 summary"].append(rel)
                elif len(s) > 100:
                    warnings["summary 超过 100 字"].append(f"{rel}（{len(s)} 字）")
            # 关系字段必须是链接
            for k, v in fm.items():
                if k in LINK_LIST:
                    if v is None:
                        continue
                    if not isinstance(v, list):
                        errors["关系字段应为列表"].append(f"{rel}：{k}")
                        continue
                    for x in v:
                        if not (isinstance(x, str) and x.startswith("[[") and x.endswith("]]")):
                            errors["关系字段的值不是链接"].append(f"{rel}：{k} → {x}")
                elif k in LINK_ONE and v not in (None, ""):
                    if not (isinstance(v, str) and v.startswith("[[") and v.endswith("]]")):
                        errors["关系字段的值不是链接"].append(f"{rel}：{k} → {v}")
            # 放对目录
            home = HOME_OF.get(t)
            if home and not rel.startswith(home):
                errors["放错目录"].append(f"{rel}：type 为 {t}，应在 {home}")
            if t == "event" and str(fm.get("start_year") or "").isdigit():
                dec = f"{int(fm['start_year']) // 10 * 10}年代"
                if f"/{dec}/" not in f"/{rel}":
                    warnings["事件不在对应年代目录"].append(f"{rel}：应在 {dec}/")
            if t == "event" and not fm.get("countries"):
                warnings["事件没有写 countries"].append(rel)
            # 观点卡
            if t == "view":
                if fm.get("view_kind") == "prediction":
                    for k in ("snapshot", "review_on", "outcome"):
                        if fm.get(k) in (None, ""):
                            errors["预测卡缺字段"].append(f"{rel}：{k}")
                    ro = str(fm.get("review_on") or "")
                    if fm.get("outcome") == "pending" and ro and ro <= today:
                        warnings["预测已到复盘日"].append(f"{rel}（{ro}）")
                said_in = fm.get("said_in")
                if said_in not in (None, "", []):
                    if not isinstance(said_in, list):
                        errors["said_in 必须是列表"].append(rel)
                    else:
                        dates = []
                        for x in said_in:
                            m = SAID_IN.match(str(x))
                            if not m:
                                errors["said_in 每一行要以日期开头"].append(f"{rel}：{x}")
                            else:
                                dates.append(m.group(1))
                        if dates and str(fm.get("said_on") or "") != min(dates):
                            errors["said_on 不是 said_in 里最早的日期"].append(
                                f"{rel}：said_on = {fm.get('said_on')}，最早 = {min(dates)}")
                for k in ("source", "anchor"):
                    if k in fm:
                        errors["观点卡还留着旧字段（2026-10-24 起不用）"].append(f"{rel}：{k}")
            # 卡片太长
            if t in NEEDS_SUMMARY and body_chars(body) > FAT_LIMIT:
                warnings["卡片太长（考虑拆分，见 AGENTS.md 第 12.4 节）"].append(
                    f"{rel}（{body_chars(body)} 字）")

        # 模块根部只放索引
        if MODULE_ROOT.match(rel) and t != "overview":
            errors["模块根部放了正文"].append(rel)

        # 链接
        scan = strip_code(body)
        if n["raw"]:
            scan += "\n" + n["raw"]
        for bang, inner in WIKILINK.findall(scan):
            tgt_text = inner.split("|")[0]
            name, _, anchor = tgt_text.partition("#")
            if name.strip() == "":
                tgt = rel
            else:
                tgt = resolve(name)
            if not tgt:
                clean = name.strip().split("/")[-1]
                if bang:
                    errors["嵌入的笔记不存在"].append(f"{rel}：![[{inner}]]")
                else:
                    unresolved[clean].add(Path(rel).stem)
                continue
            if anchor and tgt in parsed:
                if anchor.startswith("^"):
                    if anchor[1:] not in parsed[tgt]["blocks"]:
                        errors["块引用找不到"].append(f"{rel}：[[{inner}]]")
                else:
                    head = anchor.split("#")[-1].strip()
                    if head not in parsed[tgt]["headings"]:
                        warnings["标题链接找不到对应标题"].append(f"{rel}：[[{inner}]]")

    # 观点文件夹：到 GUIDE_AT 张要有导览，到 SPLIT_AT 张要分子文件夹
    per_folder = defaultdict(int)
    for rel, n in parsed.items():
        if (n["fm"] or {}).get("type") == "view":
            per_folder[Path(rel).parent.as_posix()] += 1
    for folder, cnt in sorted(per_folder.items()):
        if cnt >= GUIDE_AT and f"{folder}/{Path(folder).name}导览.md" not in parsed:
            warnings["观点文件夹该加导览（见 AGENTS.md 第 8.5 节）"].append(f"{folder}（{cnt} 张）")
        if cnt >= SPLIT_AT:
            warnings["观点文件夹该分子文件夹（见 AGENTS.md 第 8.5 节）"].append(f"{folder}（{cnt} 张）")

    for name in unresolved:
        if name.casefold() in owner:
            errors["链接写成了别名（应链本名）"].append(f"[[{name}]] → 本名在 {owner[name.casefold()]}")
    warnings["未解析链接（待建节点）"] = [f"{k}（{len(v)} 篇）" for k, v in
                                    sorted(unresolved.items(), key=lambda kv: (-len(kv[1]), kv[0]))]

    if write_report:
        write_pending(unresolved)

    # 输出
    n_err = sum(len(v) for v in errors.values())
    n_warn = sum(len(v) for v in warnings.values())
    print(f"检查了 {len(notes)} 篇笔记：{n_err} 个错误，{n_warn} 个警告。")
    for cat, items in errors.items():
        print(f"\n[错误] {cat}（{len(items)}）")
        for x in items:
            print(f"  - {x}")
    for cat, items in warnings.items():
        if not items:
            continue
        print(f"\n[警告] {cat}（{len(items)}）")
        for x in items if verbose else items[:8]:
            print(f"  - {x}")
        if not verbose and len(items) > 8:
            print(f"  ……还有 {len(items) - 8} 条，加 -v 查看全部")
    if write_report:
        print(f"\n待建节点报告：{REPORT.relative_to(ROOT)}")
    return 1 if n_err else 0


def write_pending(unresolved):
    rows = sorted(unresolved.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    today = datetime.date.today().isoformat()
    lines = [
        "---", "type: overview", "status: active", 'title: "待建节点"',
        'summary: "被提到了、但还没有建卡的对象，按被几篇笔记提到排序；由 check.py 自动生成。"',
        "source_status: unsourced", "sources: []", "tags:", "  - type/overview", "  - status/active",
        "created: 2026-10-07", f"updated: {today}", "---", "",
        "# 待建节点", "",
        "这份清单由 `python3 99_工具/脚本/check.py` 自动生成，不要手改。",
        "",
        "按 AGENTS.md 第 4.1 节：事件、主体、资产这类具体对象，被两篇以上笔记提到就该建卡；"
        "概念、模式、方法这类抽象节点门槛更高，出现次数多也不一定要建。",
        "",
        f"共 {len(rows)} 个。",
        "",
        "| 名称 | 被几篇笔记提到 | 出自 |",
        "|---|---|---|",
    ]
    for name, srcs in rows:
        s = sorted(srcs)
        shown = "、".join(s[:4]) + (f" 等 {len(s)} 篇" if len(s) > 4 else "")
        lines.append(f"| `{name}` | {len(srcs)} | {shown.replace('|', '｜')} |")
    text = "\n".join(lines) + "\n"
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    old = REPORT.read_text(encoding="utf-8") if REPORT.exists() else ""
    if re.sub(r"^updated: .*$", "", old, flags=re.M) != re.sub(r"^updated: .*$", "", text, flags=re.M):
        REPORT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
