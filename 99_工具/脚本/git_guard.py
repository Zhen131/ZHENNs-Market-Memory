#!/usr/bin/env python3
"""历史金融图谱 · 提交署名守门。只依赖 Python 3 标准库。

规矩（AGENTS.md 第 14 节）：提交的作者和提交者只能是 Zhen 本人的邮箱，
提交信息里不能出现任何别人的邮箱、AI 共同署名或会话链接。

一旦发现别人的邮箱：
- 提交前发现：直接拦下，这笔提交不会生成；
- 提交后或推送前发现：撤掉有问题的那几笔提交（改动留在工作区，不丢），推送拦下；
- 在 Claude Code 里发现：拒绝这条命令，并让会话停下来。

用法（一般不用手动跑，由 git 钩子和 .claude/settings.json 调用）：
  python3 99_工具/脚本/git_guard.py session-start   设置本仓库的 git 钩子目录和署名
  python3 99_工具/脚本/git_guard.py audit           检查所有还没推送的提交
  python3 99_工具/脚本/git_guard.py verify 范围      检查已经推送的提交，例如 verify 1300f82..origin/main
  python3 99_工具/脚本/git_guard.py commit-msg 文件  git 的 commit-msg 钩子
  python3 99_工具/脚本/git_guard.py post-commit      git 的 post-commit 钩子
  python3 99_工具/脚本/git_guard.py pre-push         git 的 pre-push 钩子
  python3 99_工具/脚本/git_guard.py claude-pretool   Claude Code 的 PreToolUse 钩子
"""
import json
import re
import subprocess
import sys

# 允许出现的邮箱。要加别的邮箱，只改这里。
ALLOWED_EMAILS = {"gyyhyyi@gmail.com"}
OWNER_NAME = "Zhen Zhu"
OWNER_EMAIL = "gyyhyyi@gmail.com"
HOOKS_PATH = "99_工具/git-hooks"

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
BAD_LINES = [
    re.compile(r"^\s*co-authored-by\s*:", re.I | re.M),
    re.compile(r"^\s*claude-session\s*:", re.I | re.M),
    re.compile(r"generated with.*(claude|copilot|openai)", re.I),
    re.compile(r"claude\.ai/code|claude\.com/claude-code", re.I),
]
ZERO = "0" * 40


def git(*args, check=True):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} 失败：{r.stderr.strip()}")
    return r.stdout


def say(msg):
    print(msg, file=sys.stderr)


def message_problems(text):
    probs = []
    for e in sorted(set(EMAIL.findall(text))):
        if e.lower() not in ALLOWED_EMAILS:
            probs.append(f"提交信息里有别人的邮箱 {e}")
    for pat in BAD_LINES:
        m = pat.search(text)
        if m:
            probs.append(f"提交信息里有 AI 署名或会话链接：{m.group(0).strip()}")
    return probs


def commit_problems(sha):
    out = git("show", "-s", "--format=%ae%x00%ce%x00%B", sha)
    ae, ce, body = out.split("\x00", 2)
    probs = []
    if ae.strip().lower() not in ALLOWED_EMAILS:
        probs.append(f"作者邮箱是 {ae.strip()}")
    if ce.strip().lower() not in ALLOWED_EMAILS:
        probs.append(f"提交者邮箱是 {ce.strip()}")
    return probs + message_problems(body)


def unpushed(rev="HEAD"):
    """rev 能到达、但还不在任何远端分支上的提交，从旧到新。"""
    out = git("rev-list", "--reverse", rev, "--not", "--remotes", check=False)
    return [x for x in out.split() if x]


def find_bad(shas):
    bad = []
    for s in shas:
        p = commit_problems(s)
        if p:
            bad.append((s, p))
    return bad


def rollback(bad_shas):
    """撤掉当前分支上从最早一笔坏提交开始的所有提交，改动留在暂存区。"""
    on_head = unpushed("HEAD")
    idx = [i for i, s in enumerate(on_head) if s in bad_shas]
    if not idx:
        return "坏提交不在当前分支上，没有回滚，只拦下了推送。"
    first = on_head[idx[0]]
    parent = git("rev-parse", "--verify", "-q", first + "^", check=False).strip()
    if parent:
        git("reset", "--soft", parent)
        target = parent[:7]
    else:
        git("update-ref", "-d", "HEAD")
        target = "（仓库第一笔之前）"
    n = len(on_head) - idx[0]
    return f"已回滚：撤掉了当前分支最后 {n} 笔提交，回到 {target}；改动都还在暂存区，没有丢。"


def report(bad):
    lines = ["发现别人的邮箱或 AI 署名，已拦下："]
    for s, probs in bad:
        subj = git("show", "-s", "--format=%s", s).strip()
        lines.append(f"  {s[:7]} {subj}")
        lines += [f"    - {p}" for p in probs]
    return "\n".join(lines)


# ---------- 各个入口 ----------

def cmd_session_start():
    top = git("rev-parse", "--show-toplevel", check=False).strip()
    if not top:
        return 0
    git("config", "core.hooksPath", HOOKS_PATH)
    git("config", "user.name", OWNER_NAME)
    git("config", "user.email", OWNER_EMAIL)
    # 云端会话默认用 Anthropic 的服务给提交签名，签名会把提交挂到别人的账号上，关掉。
    git("config", "commit.gpgsign", "false")
    git("config", "tag.gpgsign", "false")
    print(f"署名守门已开启：提交只能署 {OWNER_EMAIL}（git 钩子目录 {HOOKS_PATH}）。")
    return 0


def cmd_audit():
    bad = find_bad(unpushed("--branches"))
    if bad:
        say(report(bad))
        return 1
    print("还没推送的提交都只有 Zhen 的邮箱。")
    return 0


def cmd_verify(rng):
    """推送以后再查一遍：rng 可以是一笔提交，也可以是 a..b 这样的范围。"""
    if ".." in rng:
        shas = git("rev-list", "--reverse", rng).split()
    else:
        shas = [git("rev-parse", rng).strip()]
    bad = find_bad(shas)
    if bad:
        say(report(bad))
        return 1
    print(f"查了 {len(shas)} 笔提交，都只有 Zhen 的邮箱，没有 AI 署名。")
    return 0


def cmd_commit_msg(path):
    text = open(path, encoding="utf-8").read()
    # 去掉 git 自己加的注释行再检查
    text = "\n".join(l for l in text.splitlines() if not l.startswith("#"))
    probs = message_problems(text)
    ident = []
    for var in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
        e = EMAIL.findall(git("var", var, check=False))
        if e and e[0].lower() not in ALLOWED_EMAILS:
            ident.append(f"{'作者' if 'AUTHOR' in var else '提交者'}邮箱会是 {e[0]}")
    probs = ident + probs
    if probs:
        say("提交被拦下：\n" + "\n".join(f"  - {p}" for p in probs))
        return 1
    return 0


def cmd_post_commit():
    head = git("rev-parse", "HEAD").strip()
    probs = commit_problems(head)
    if probs:
        say(report([(head, probs)]))
        say(rollback({head}))
        return 1
    return 0


def cmd_pre_push():
    shas = []
    for line in sys.stdin.read().splitlines():
        parts = line.split()
        if len(parts) != 4:
            continue
        _, local_sha, _, remote_sha = parts
        if local_sha == ZERO:
            continue  # 删除远端分支，不涉及提交
        if remote_sha == ZERO:
            shas += unpushed(local_sha)
        else:
            out = git("rev-list", "--reverse", f"{remote_sha}..{local_sha}", check=False)
            shas += out.split()
    bad = find_bad(list(dict.fromkeys(shas)))
    if bad:
        say(report(bad))
        say(rollback({s for s, _ in bad}))
        say("推送已取消。")
        return 1
    return 0


BYPASS = [
    (re.compile(r"--no-verify"), "不许用 --no-verify 跳过检查"),
    # 只拦「改」：赋值、跟着新值、删除。只读（git config core.hooksPath）放行。
    (re.compile(r"core\.hookspath\s*=|core\.hookspath\s+[^\s|;&>)]|--unset(-all)?\s+core\.hookspath",
                re.I), "不许改 git 钩子目录"),
    (re.compile(r"\bcommit\b[^|;&]*\s-[A-Za-z]*n[A-Za-z]*\b"), "不许用 -n 跳过检查"),
    (re.compile(r"\bcommit\b[^|;&]*--author\b"), "不许用 --author 改作者"),
    (re.compile(r"commit\.gpgsign\s*=?\s*true", re.I), "不许打开 Anthropic 的提交签名"),
]


def pretool_decision(cmd):
    """返回 (动作, 说明)。动作：allow / deny / stop。"""
    if "git" not in cmd:
        return "allow", ""
    for pat, why in BYPASS:
        if pat.search(cmd):
            return "deny", why
    for e in EMAIL.findall(cmd):
        if e.lower() not in ALLOWED_EMAILS and re.search(
                r"(user\.email|GIT_(AUTHOR|COMMITTER)_EMAIL|EMAIL=)", cmd):
            return "deny", f"不许把提交邮箱设成 {e}"
    if re.search(r"\bpush\b", cmd):
        bad = find_bad(unpushed("--branches"))
        if bad:
            return "stop", report(bad) + "\n" + rollback({s for s, _ in bad})
    if re.search(r"\bcommit\b", cmd):
        for var in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            e = EMAIL.findall(git("var", var, check=False))
            if e and e[0].lower() not in ALLOWED_EMAILS:
                return "stop", f"这台机器的提交邮箱是 {e[0]}，不是 Zhen 的，提交前就停下。"
    return "allow", ""


def cmd_claude_pretool():
    raw = sys.stdin.read()
    cmd = ""
    try:
        cmd = (json.loads(raw).get("tool_input") or {}).get("command") or ""
        action, why = pretool_decision(cmd)
    except Exception as exc:  # 出错时：推送一律拦下，其他放行
        if re.search(r"\bpush\b", cmd):
            action, why = "deny", f"署名守门出错，推送先拦下：{exc}"
        else:
            return 0
    if action == "allow":
        return 0
    out = {"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": why,
    }}
    if action == "stop":
        out["continue"] = False
        out["stopReason"] = "署名守门：" + why + "\n请停下全部操作，等 Zhen 处理。"
    print(json.dumps(out, ensure_ascii=False))
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    mode = sys.argv[1]
    if mode == "session-start":
        return cmd_session_start()
    if mode == "audit":
        return cmd_audit()
    if mode == "verify":
        return cmd_verify(sys.argv[2] if len(sys.argv) > 2 else "HEAD")
    if mode == "commit-msg":
        return cmd_commit_msg(sys.argv[2])
    if mode == "post-commit":
        return cmd_post_commit()
    if mode == "pre-push":
        return cmd_pre_push()
    if mode == "claude-pretool":
        return cmd_claude_pretool()
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
