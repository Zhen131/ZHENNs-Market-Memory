#!/usr/bin/env python3
"""生成「新卡阅读清单」。

在库根目录运行：
    python3 99_工具/脚本/make_reading_list.py            # 结果打印到标准输出
    python3 99_工具/脚本/make_reading_list.py --write    # 覆盖 20_我的/思考/2026-10-31 新卡阅读清单.md

只用 Python 3 标准库。每层开头的说明文字是手写的，放在下面的常量里；
张数、分组、条目全部由 10_观点/ 里的观点卡算出来。
统计（总张数、每层张数、解析不了的卡）打印到标准错误。
"""

import argparse
import datetime
import os
import re
import sys

# ---------------------------------------------------------------- 可调参数
VIEW_DIR = "10_观点"
OUT_PATH = "20_我的/思考/2026-10-31 新卡阅读清单.md"
SCRIPT_PATH = "99_工具/脚本/make_reading_list.py"

HINT_MAX = 32      # 提示超过这么多个字才截断
HINT_CUT_FROM = 15  # 从第几个字以后找第一个截断标点
HINT_CUT_MARKS = "，、；："

# 第 4 层、第 5 层里 ### 组的顺序；没列到的文件夹排在后面，按名字排
LAYER4_ORDER = ["中国经济与产业", "全球化与地缘", "货币与大类资产"]
LAYER5_ORDER = ["AI 与科技", "中国公司", "消费与品牌", "能源与资源", "金融与交易所"]
OTHER_GROUP = "其他判断"

# 子文件夹分组的固定顺序（没列到的子文件夹排在后面，按名字排；列了但不存在的跳过）
# 键是第 1、2、3 层的主题文件夹名。
SUB_ORDER = {
    "选股与仓位": ["仓位与买卖时机", "风险控制", "研究方法", "找标的与爆发股", "技术分析与交易纪律"],
    "商业模式与护城河": ["最好的生意与自然垄断", "消费品与线下连锁", "金融基础设施", "平台与 AI", "竞争", "产能与怎么看生意", "竞争、产能与怎么看生意"],  # 末项的断句有歧义，三种都列，不存在的跳过,
    "估值与赔率": [],
}
# 第 5 层「公司与行业」下，某个子文件夹里再按第三级文件夹分 #### 组的顺序
SUB2_ORDER = {
    "AI 与科技": ["AI 产业链与应用", "科技大公司与软件", "早期科技与太空"],
}

# 提示、"附"里的 summary 开头这些前缀要去掉（长的放前面）
HINT_PREFIXES = ["脑总的看法是", "脑总认为", "脑总觉得", "脑总判断", "脑总说", "他认为", "他觉得", "他说"]

# ---------------------------------------------------------------- 手写说明（常量）
TITLE = "2026-10-31 新卡阅读清单"

FRONT_SUMMARY = (
    "把 10_观点 里全部 {total} 张观点卡排成从地基到具体判断的七层阅读阶梯，每层读完再读下一层，可打勾。"
    "2026-10-28 第一版只有当时新入的 126 张，2026-10-30 重排成覆盖全库的阶梯。"
)

LAYER0 = """## 第 0 层·怎么用这份清单

这是一张盖房子的图：第 1 层是地基，往上一层比一层具体。**每层读完再读下一层**，别跳。同一层里排在前面的是他讲过次数最多的（卡里 `said_in` 列得长的），先读它们，因为讲得多的多半是他最信的；次数相同的按他第一次说的日期从早到晚排。

读一张卡时，顺着 `about` 和正文里的链接点过去看公司卡、概念卡，这里不单列它们。卡里写着「这是图谱的推论，他没有这样说」的那句，不是他的原话，是整理时加的推论，分开看。每条后面的破折号是从卡的 `summary` 里摘的一句提示，帮你想起这张卡讲什么；「讲过 N 次」是他在几期材料里说过这件事。每张卡读完打勾。

这份清单 2026-10-28 第一版只有当时两天新入的 126 张；2026-10-30 重排成覆盖全库 {total} 张的阶梯，2026-10-31 三月八期入库后文件名改成 2026-10-31，旧名留在别名里。{today} 由脚本 `99_工具/脚本/make_reading_list.py` 重新生成，共 {total} 张{archived_note}。"""

LAYER1_HEAD = "## 第 1 层·地基：看懂一门生意"
LAYER1_INTRO = "回答「什么样的生意好、壁垒从哪来」。不先懂生意好坏，后面讲估值、讲买卖都是空中楼阁，所以放最底下。全是能搬到别的公司上用的道理（`view_kind: framework`），出自「商业模式与护城河」。"

LAYER2_HEAD = "## 第 2 层·尺子：多少钱值得买"
LAYER2_INTRO = "回答「这门生意多少钱值得买，还能涨多少」。懂了生意好坏，才谈得上给它定价，所以放第二层。出自「估值与赔率」的框架卡。"

LAYER3_HEAD = "## 第 3 层·手法：怎么买、配多少、何时卖"
# 原文是「……有 99 张，是他讲得最密的地方。按意思分成六组，组内还是按讲过次数排。……」
# 现在按文件夹规则不再手工分组，所以把「按意思分成六组」换成「按讲过次数排」。
LAYER3_INTRO = "回答「买谁、配多少、什么时候买卖」。这一层最多，有 {n} 张，是他讲得最密的地方。按讲过次数排。出自「选股与仓位」的框架卡。"

LAYER4_HEAD = "## 第 4 层·大环境"
LAYER4_INTRO = "回答「中国的产业和政策、国与国的关系、钱本身（美元、黄金、比特币、利率）怎样影响投资」。它排在生意、估值、手法之后，因为大环境是背景，不先会看公司，光看宏观容易变成空谈。三个文件夹各一组，框架卡和判断卡混排，按讲过次数排。"
LAYER4_GROUP_INTRO = {
    "中国经济与产业": "中国的产业、政策、A 股和港股的制度，怎样影响投资。",
    "全球化与地缘": "贸易、技术、国与国的关系怎么变。",
    "货币与大类资产": "美元、黄金、石油、比特币、利率这些大类资产怎么看。",
}

LAYER5_HEAD = "## 第 5 层·具体判断"
LAYER5_INTRO = "回答「他怎么看某家公司、某个行业」。这是前面四层道理落到具体对象上的结果，所以要先读完道理再读它们：读一张判断卡时，顺手想一想它用的是上面哪条框架。按「公司与行业」的{sub_cn}个子文件夹分组；前几个文件夹里剩下的判断和案例归到「其他判断」。这一层里还有 {fw} 张放在「公司与行业」里的框架卡，跟着它们所在的子文件夹走。"
LAYER5_GROUP_INTRO = {
    "AI 与科技": "AI 产业链、半导体、软件、商业航天这些科技公司。",
    "中国公司": "A 股和港股的具体公司。",
    "消费与品牌": "美股为主的消费品、零售、餐饮公司。",
    "能源与资源": "石油、电力、矿业、农资。",
    "金融与交易所": "交易所、支付、评级、银行、券商。",
    OTHER_GROUP: "「商业模式与护城河」「估值与赔率」「选股与仓位」三个文件夹里不是框架、也不是预测和操作的卡：对某个时点市场的判断，和一个案例。",
}

LAYER6_HEAD = "## 第 6 层·他的预测和操作"
LAYER6_INTRO = "回答「他押了什么、手上做了什么」。放最上面，因为预测要拿前面所有道理去对照才看得懂，而且读它们的目的不是学道理，是以后复盘：到了复盘日回来看对不对。预测按复盘日期从近到远排，每条标复盘日；操作卡单列，嘴上说的和手上买的是两种证据，后者分量更重。"
PRED_HEAD = "### 预测（按复盘日从近到远）"
ACTION_HEAD = "### 操作（他自己买了什么、卖了什么）"

CHANGED_HEAD = "## 附：他改过口的卡"
CHANGED_INTRO = "卡里有 `changed_from` 字段的，两张对着读。这里只说从什么变成了什么，不评对错。"

LEFTOVER_HEAD = "## 附：没排进任何一层的卡"
LEFTOVER_INTRO = "这些卡按规则哪一层都不收（例如缺 `view_kind`、或放在 10_观点 根目录），脚本不丢它们，列在这里等人处理。"

FIRST3 = ["商业模式与护城河", "估值与赔率", "选股与仓位"]

CN_NUM = "零一二三四五六七八九十"


# ---------------------------------------------------------------- YAML 子集解析
class ParseError(Exception):
    pass


def parse_quoted(s):
    """s 以引号开头。返回 (字符串, 引号后剩余部分)。"""
    q = s[0]
    out = []
    i = 1
    while i < len(s):
        c = s[i]
        if q == '"' and c == "\\" and i + 1 < len(s):
            nxt = s[i + 1]
            out.append({"n": "\n", "t": "\t"}.get(nxt, nxt))
            i += 2
            continue
        if q == "'" and c == "'" and s[i + 1:i + 2] == "'":
            out.append("'")
            i += 2
            continue
        if c == q:
            return "".join(out), s[i + 1:]
        out.append(c)
        i += 1
    raise ParseError("引号没有闭合")


def strip_comment(s):
    return re.sub(r"\s+#.*$", "", s).strip()


def parse_scalar(s):
    s = s.strip()
    if not s:
        return ""
    if s[0] in "\"'":
        val, rest = parse_quoted(s)
        rest = rest.strip()
        if rest and not rest.startswith("#"):
            raise ParseError("引号后面还有多余内容：" + rest[:20])
        return val
    return strip_comment(s)


def parse_flow_list(s):
    s = s.strip()
    if not s.startswith("["):
        raise ParseError("不是列表")
    i = 1
    items = []
    while True:
        while i < len(s) and s[i] in " \t":
            i += 1
        if i >= len(s):
            raise ParseError("列表没有闭合")
        if s[i] == "]":
            rest = s[i + 1:].strip()
            if rest and not rest.startswith("#"):
                raise ParseError("列表后面还有多余内容")
            return items
        if s[i] in "\"'":
            val, rest = parse_quoted(s[i:])
            i = len(s) - len(rest)
        else:
            j = i
            while j < len(s) and s[j] not in ",]":
                j += 1
            val = s[i:j].strip()
            i = j
        items.append(val)
        while i < len(s) and s[i] in " \t":
            i += 1
        if i < len(s) and s[i] == ",":
            i += 1
        elif i < len(s) and s[i] != "]":
            raise ParseError("列表里缺逗号")


def parse_frontmatter(text):
    """返回字段字典。没有 frontmatter 返回 None。"""
    if text.startswith("﻿"):
        text = text[1:]
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for k in range(1, len(lines)):
        if lines[k].strip() == "---":
            end = k
            break
    if end is None:
        raise ParseError("frontmatter 没有结尾的 ---")
    fm = lines[1:end]
    data = {}
    i = 0
    key_re = re.compile(r"^([A-Za-z_][\w\-]*)\s*:(?:\s+(.*)|\s*)$")
    while i < len(fm):
        line = fm[i].rstrip("\r")
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        m = key_re.match(line)
        if not m:
            raise ParseError("看不懂这一行：" + line[:40])
        key, val = m.group(1), (m.group(2) or "").strip()
        if val == "" or val.startswith("#"):
            items = []
            j = i + 1
            while j < len(fm):
                nl = fm[j].rstrip("\r")
                if not nl.strip() or nl.lstrip().startswith("#"):
                    j += 1
                    continue
                mm = re.match(r"^\s+-\s+(.*)$", nl) or re.match(r"^\s+-\s*$", nl)
                if not mm:
                    break
                items.append(parse_scalar(mm.group(1) if mm.groups() else ""))
                j += 1
            data[key] = items if items else ""
            i = j
            continue
        if val.startswith("["):
            data[key] = parse_flow_list(val)
        elif val[0] in "|>" and len(val) <= 2:
            raise ParseError("暂不支持块标量：" + key)
        else:
            data[key] = parse_scalar(val)
        i += 1
    return data


# ---------------------------------------------------------------- 收集卡
class Card:
    def __init__(self, path, rel, fm):
        self.path = path
        self.name = os.path.splitext(os.path.basename(path))[0]
        parts = rel.split(os.sep)  # 相对 10_观点
        self.folder = parts[0] if len(parts) > 1 else ""
        self.sub = parts[1] if len(parts) > 2 else ""
        self.sub2 = parts[2] if len(parts) > 3 else ""
        self.fm = fm
        self.kind = str(fm.get("view_kind", "")).strip()
        self.status = str(fm.get("status", "")).strip()
        self.summary = str(fm.get("summary", "")).strip()
        self.said_on = str(fm.get("said_on", "")).strip() or "9999-99-99"
        said_in = fm.get("said_in", [])
        if isinstance(said_in, str):
            said_in = [said_in] if said_in else []
        self.said_in = said_in
        self.n = len(said_in)
        self.review_on = str(fm.get("review_on", "")).strip()
        self.outcome = str(fm.get("outcome", "")).strip()
        cf = fm.get("changed_from", [])
        if isinstance(cf, str):
            cf = [cf] if cf else []
        self.changed_from = [link_name(x) for x in cf if link_name(x)]

    @property
    def archived(self):
        return self.status == "archived"


def link_name(s):
    m = re.search(r"\[\[([^\]|#]+)", s)
    return m.group(1).strip() if m else ""


def collect(root):
    base = os.path.join(root, VIEW_DIR)
    cards, errors, skipped = [], [], 0
    for dp, dn, fn in os.walk(base):
        dn.sort()
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, base)
            try:
                with open(p, encoding="utf-8") as fh:
                    text = fh.read()
                fm = parse_frontmatter(text)
            except (ParseError, UnicodeDecodeError, OSError) as e:
                errors.append((rel, str(e)))
                continue
            if fm is None:
                errors.append((rel, "没有 frontmatter"))
                continue
            if fm.get("type") != "view":
                skipped += 1  # overview 等
                continue
            cards.append(Card(p, rel, fm))
    return cards, errors, skipped, base


# ---------------------------------------------------------------- 渲染
def strip_prefix(summary):
    s = summary.strip()
    for p in HINT_PREFIXES:
        if s.startswith(p):
            s = s[len(p):].lstrip("，,：: \t")
            break
    return s


def hint(summary):
    s = strip_prefix(summary)
    while s and s[-1] in "。.":
        s = s[:-1]
    if len(s) > HINT_MAX:
        for i in range(HINT_CUT_FROM, len(s)):
            if s[i] in HINT_CUT_MARKS:
                s = s[:i]
                break
    return s


def sort_cards(cards):
    return sorted(cards, key=lambda c: (-c.n, c.said_on, c.name))


def entry(c, extra=""):
    h = hint(c.summary)
    line = "- [ ] [[%s]]" % c.name
    if h:
        line += " —— " + h
    line += extra
    if c.n != 1:
        line += "（讲过 %d 次）" % c.n
    return line


def ordered(names, preferred):
    return [n for n in preferred if n in names] + sorted(n for n in names if n not in preferred)


def cn(n):
    return CN_NUM[n] if 0 <= n <= 10 else str(n)


class Builder:
    def __init__(self, base, cards):
        self.base = base
        self.cards = cards
        self.placed = set()
        self.layer_count = {}
        self.out = []

    def subdirs(self, folder):
        d = os.path.join(self.base, folder)
        if not os.path.isdir(d):
            return []
        return sorted(x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x)))

    def add(self, c):
        self.placed.add(c.name)

    def list_lines(self, cards, layer, extra_fn=None):
        lines = []
        for c in cards:
            lines.append(entry(c, extra_fn(c) if extra_fn else ""))
            self.add(c)
            self.layer_count[layer] = self.layer_count.get(layer, 0) + 1
        return lines

    def grouped(self, cards, layer, level, folder, extra_fn=None):  # noqa
        """按子文件夹再分一级；没有子文件夹就直接列。level 是标题 # 个数。"""
        has_sub = bool(self.subdirs(folder)) or any(c.sub for c in cards)
        if not has_sub:
            return self.list_lines(sort_cards(cards), layer, extra_fn)
        out = []
        root_cards = [c for c in cards if not c.sub]
        if root_cards:
            out += self.list_lines(sort_cards(root_cards), layer, extra_fn) + [""]
        subs = ordered(set(c.sub for c in cards if c.sub), SUB_ORDER.get(folder, []))
        for s in subs:
            out += ["#" * level + " " + s, ""]
            out += self.list_lines(sort_cards([c for c in cards if c.sub == s]), layer, extra_fn)
            out.append("")
        while out and out[-1] == "":
            out.pop()
        return out

    def section(self, head, intro, body_lines):
        self.out += [head, "", intro, ""] + body_lines + [""]

    def build(self, today, total, archived_n):
        live = [c for c in self.cards if not c.archived]
        fw = lambda f: [c for c in live if c.folder == f and c.kind == "framework"]

        archived_note = "，其中 %d 张已归档、只在文末出现" % archived_n if archived_n else ""
        self.out.append(LAYER0.format(total=total, today=today, archived_note=archived_note))
        self.out.append("")

        # 第 1、2、3 层
        for layer, head, intro, folder in (
            (1, LAYER1_HEAD, LAYER1_INTRO, FIRST3[0]),
            (2, LAYER2_HEAD, LAYER2_INTRO, FIRST3[1]),
            (3, LAYER3_HEAD, LAYER3_INTRO, FIRST3[2]),
        ):
            cs = fw(folder)
            intro = intro.format(n=len(cs)) if "{n}" in intro else intro
            self.section(head, intro, self.grouped(cs, layer, 3, folder))

        # 第 4 层
        body = []
        l4_folders = ordered(set(c.folder for c in live if c.folder in LAYER4_ORDER) | set(LAYER4_ORDER), LAYER4_ORDER)
        for f in l4_folders:
            cs = [c for c in live if c.folder == f and c.kind in ("framework", "judgment")]
            body += ["### " + f, "", LAYER4_GROUP_INTRO.get(f, ""), ""]
            body += self.grouped(cs, 4, 4, f)
            body.append("")
        while body and body[-1] == "":
            body.pop()
        self.section(LAYER4_HEAD, LAYER4_INTRO, body)

        # 第 5 层
        company = "公司与行业"
        c_cards = [c for c in live if c.folder == company and c.kind in ("judgment", "case", "framework")]
        subs = ordered(set(c.sub for c in c_cards if c.sub) | set(self.subdirs(company)), LAYER5_ORDER)
        fw_in_company = len([c for c in c_cards if c.kind == "framework"])
        body = []
        for s in subs:
            cs = [c for c in c_cards if c.sub == s]
            body += ["### " + s, "", LAYER5_GROUP_INTRO.get(s, ""), ""]
            sub2s = ordered(set(c.sub2 for c in cs if c.sub2), SUB2_ORDER.get(s, []))
            if sub2s:
                rest = [c for c in cs if not c.sub2]
                if rest:
                    body += self.list_lines(sort_cards(rest), 5) + [""]
                for s2 in sub2s:
                    body += ["#### " + s2, ""]
                    body += self.list_lines(sort_cards([c for c in cs if c.sub2 == s2]), 5)
                    body.append("")
                while body[-1] == "":
                    body.pop()
            else:
                body += self.list_lines(sort_cards(cs), 5)
            body.append("")
        other = [c for c in c_cards if not c.sub]
        other += [c for c in live if c.folder in FIRST3 and c.kind in ("judgment", "case")]
        body += ["### " + OTHER_GROUP, "", LAYER5_GROUP_INTRO[OTHER_GROUP], ""]
        body += self.list_lines(sort_cards(other), 5)
        intro = LAYER5_INTRO.format(sub_cn=cn(len(subs)), fw=fw_in_company)
        self.section(LAYER5_HEAD, intro, body)

        # 第 6 层
        preds = sorted(
            [c for c in live if c.kind == "prediction"],
            key=lambda c: (c.review_on or "9999-99-99", -c.n, c.said_on, c.name),
        )

        def pred_extra(c):
            s = "（复盘 %s）" % c.review_on if c.review_on else "（复盘日未定）"
            if c.outcome and c.outcome != "pending":
                s += "（结果：%s）" % c.outcome
            return s

        acts = sort_cards([c for c in live if c.kind == "action"])
        body = [PRED_HEAD, ""] + self.list_lines(preds, 6, pred_extra) + ["", ACTION_HEAD, ""]
        body += self.list_lines(acts, 6)
        self.section(LAYER6_HEAD, LAYER6_INTRO, body)

        # 附：改过口
        by_name = {c.name: c for c in self.cards}
        lines = []
        mentioned = set()
        for c in sorted((c for c in self.cards if c.changed_from), key=lambda c: (c.said_on, c.name)):
            for old in c.changed_from:
                old_c = by_name.get(old)
                old_s = strip_prefix(old_c.summary) if old_c else "（旧卡找不到）"
                lines.append("- [[%s]] → [[%s]]：%s；改成：%s" % (old, c.name, old_s, strip_prefix(c.summary)))
                mentioned.add(old)
        for c in sorted((c for c in self.cards if c.archived and c.name not in mentioned), key=lambda c: c.name):
            lines.append("- [[%s]]（已归档）：%s" % (c.name, c.summary))
        self.out += [CHANGED_HEAD, "", CHANGED_INTRO, ""] + lines + [""]

        # 没排进任何一层的
        left = [c for c in live if c.name not in self.placed]
        if left:
            self.out += [LEFTOVER_HEAD, "", LEFTOVER_INTRO, ""]
            for c in sorted(left, key=lambda c: (c.folder, c.name)):
                self.out.append("- [ ] [[%s]] —— %s（%s / %s）" % (c.name, hint(c.summary), c.folder or "根目录", c.kind or "缺 view_kind"))
            self.out.append("")
        self.leftover = left


def main():
    ap = argparse.ArgumentParser(description="生成新卡阅读清单")
    ap.add_argument("--write", action="store_true", help="覆盖 " + OUT_PATH)
    args = ap.parse_args()

    root = os.getcwd()
    if not os.path.isdir(os.path.join(root, VIEW_DIR)):
        sys.exit("请在库根目录运行（找不到 %s/）" % VIEW_DIR)

    cards, errors, skipped, base = collect(root)
    today = datetime.date.today().isoformat()
    total = len(cards)
    archived_n = sum(1 for c in cards if c.archived)

    names = {}
    for c in cards:
        names.setdefault(c.name, []).append(c.path)
    dups = {k: v for k, v in names.items() if len(v) > 1}

    b = Builder(base, cards)
    b.build(today, total, archived_n)

    front = "\n".join([
        "---",
        "type: note",
        "status: active",
        'title: "%s"' % TITLE,
        'summary: "%s"' % FRONT_SUMMARY.format(total=total),
        'aliases: ["观点卡阅读阶梯", "2026-10-28 新卡阅读清单"]',
        "source_status: unsourced",
        "sources: []",
        "tags: [type/note, status/active]",
        "created: 2026-10-28",
        "updated: %s" % today,
        "---",
        "",
        "# " + TITLE,
        "",
        "",
    ])
    text = front.rstrip("\n") + "\n\n" + "\n".join(b.out).rstrip("\n") + "\n"

    if args.write:
        with open(os.path.join(root, OUT_PATH), "w", encoding="utf-8") as fh:
            fh.write(text)
        print("已写入 " + OUT_PATH, file=sys.stderr)
    else:
        sys.stdout.write(text)

    body_total = sum(b.layer_count.values())
    print("---- 统计 ----", file=sys.stderr)
    print("type: view 的卡共 %d 张（已归档 %d 张，跳过非 view 文件 %d 个）" % (total, archived_n, skipped), file=sys.stderr)
    for k in sorted(b.layer_count):
        print("第 %d 层：%d 张" % (k, b.layer_count[k]), file=sys.stderr)
    print("正文条目合计：%d 张" % body_total, file=sys.stderr)
    if b.leftover:
        print("没排进任何一层：%d 张（列在文末「附：没排进任何一层的卡」）" % len(b.leftover), file=sys.stderr)
        for c in b.leftover:
            print("  - %s（%s / %s）" % (c.name, c.folder or "根目录", c.kind or "缺 view_kind"), file=sys.stderr)
    if errors:
        print("解析不了的文件 %d 个：" % len(errors), file=sys.stderr)
        for rel, e in errors:
            print("  - %s：%s" % (rel, e), file=sys.stderr)
    else:
        print("解析不了的文件：0", file=sys.stderr)
    if dups:
        print("重名的卡（链接会指错）：", file=sys.stderr)
        for k, v in dups.items():
            print("  - %s：%s" % (k, v), file=sys.stderr)
    long_hint = [c.name for c in cards if not c.archived and len(hint(c.summary)) > HINT_MAX]
    if long_hint:
        print("提示仍超过 %d 字（找不到截断标点）的卡 %d 张" % (HINT_MAX, len(long_hint)), file=sys.stderr)


if __name__ == "__main__":
    main()
