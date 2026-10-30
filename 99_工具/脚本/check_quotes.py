#!/usr/bin/env python3
"""历史金融图谱 · 核对观点卡里的原话。只依赖 Python 3 标准库。

观点卡里「」中的话和开头引用块里的话，都必须逐字出自原文（空格和 ► 不计）。
2026-10-30 起世界层和认知层的卡（主体、概念、方法、模式、资产、对比、事件）也一起核：
它们里面「」装的也只能是他的原话。这个脚本把这些话和存档原文逐条比对，找不到的列出来。
规则见 AGENTS.md 第 8.2 节、第 12.1 节。

在 vault 根目录运行：
  python3 99_工具/脚本/check_quotes.py --said-in "2026-10-22 直播" 99Z_等待入库文件/已入库/261022.md
      核对 said_in 或 sources 里有「2026-10-22 直播」的所有卡（观点卡和世界层的卡都算）
  python3 99_工具/脚本/check_quotes.py 原文.md 10_观点/公司与行业/某张卡.md
      只核对指定的卡或文件夹

一张卡讲过好几期时，把这几期的原文都写上：每条原话只要出现在其中一份里就算对。
原文先按 99_工具/ASR校正表.md 把错字改过来再比，所以「」里按校正表改正的字也算对得上。
有找不到的片段时退出码为 1。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# 哪些目录下的卡要核「」；哪些 type 算卡（导览、我的笔记不算）
CARD_DIRS = ("10_观点", "04_主体", "06_概念", "08_方法", "03_模式", "05_资产", "07_对比", "02_事件", "01_时间线")
CARD_TYPES = {"view", "entity", "concept", "method", "pattern", "asset", "comparison", "event", "timeline"}
QUOTE = re.compile(r"「((?:[^「」]|「[^「」]*」)*)」")


def norm(s):
    s = re.sub(r"[\s►]", "", s)
    for a, b in (("『", '"'), ("』", '"'), ("“", '"'), ("”", '"')):
        s = s.replace(a, b)
    return s


def asr_pairs():
    """读 ASR 校正表里的「错 → 对」，按表里的顺序返回。"""
    p = ROOT / "99_工具" / "ASR校正表.md"
    pairs = []
    if not p.exists():
        return pairs
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("错", "") or set(cells[0]) <= set("-: "):
            continue
        pairs.append((norm(cells[0]), norm(cells[1])))
    return pairs


def segments(body):
    segs = []
    for line in body.splitlines():
        if line.startswith("> ") and not line.startswith("> ——"):
            segs += [x for x in line[2:].split("……") if x.strip()]
    for m in QUOTE.finditer(body):
        segs += [x for x in m.group(1).split("……") if x.strip()]
    return segs


def said_in(text):
    m = re.search(r"^said_in:\s*\n((?:\s+-.*\n?)+)", text, re.M)
    return re.findall(r'-\s*"?([^"\n]+)"?', m.group(1)) if m else []


def main():
    args = sys.argv[1:]
    tag = None
    if "--said-in" in args:
        i = args.index("--said-in")
        tag = args[i + 1]
        del args[i:i + 2]
    sources, targets = [], []
    for a in args:
        p = Path(a)
        p = p if p.is_absolute() else ROOT / p
        (targets if any(d in p.as_posix() for d in CARD_DIRS) else sources).append(p)
    if not sources:
        print(__doc__)
        return 1

    pairs = asr_pairs()
    text = ""
    for p in sources:
        raw = norm(p.read_text(encoding="utf-8"))
        fixed = raw
        for wrong, right in pairs:
            fixed = fixed.replace(wrong, right)
        text += raw + "\n" + fixed + "\n"
    cards = []
    for t in targets or [ROOT / d for d in CARD_DIRS if (ROOT / d).is_dir()]:
        cards += sorted(t.rglob("*.md")) if t.is_dir() else [t]
    bad = checked = 0
    for p in cards:
        s = p.read_text(encoding="utf-8")
        m = re.search(r"^type:\s*(\S+)", s, re.M)
        if not m or m.group(1) not in CARD_TYPES:
            continue
        if tag and not any(tag in x for x in said_in(s)) and tag not in s:
            continue
        checked += 1
        body = s.split("\n---\n", 1)[1] if "\n---\n" in s else s
        for seg in segments(body):
            if norm(seg) not in text:
                bad += 1
                print(f"{p.relative_to(ROOT)}：{seg}")
    print(f"核对了 {checked} 张卡，找不到的片段：{bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
