---
type: overview
status: active
title: "MinerU PDF 批量转 Markdown 使用指南"
source_status: verified
sources:
  - "本机 MinerU 3.4.4 实际安装与转换测试"
tags:
  - type/overview
  - status/active
  - tool/mineru
created: 2026-07-25
updated: 2026-07-30
---

# MinerU PDF 批量转 Markdown 使用指南

## 你要记住的三件事

1. 把需要转换的 PDF 或 DOCX 放进：

   `/Users/zhuzhen0131/Documents/MinerU转换/输入PDF`

2. 打开 Mac 的“终端”，复制执行下面的“一键批量转换命令”。

3. 转换完成后，直接去这里拿 Markdown：

   `/Users/zhuzhen0131/Documents/MinerU转换/输出Markdown`

MinerU 已经安装配置完成，不需要再次安装 Python、uv 或 MinerU。

---

## 文件夹用途

```text
MinerU转换/
├── 输入PDF/          # 把待转换的 PDF 放在这里
├── 原始解析结果/      # JSON、标注 PDF、图片等完整技术文件
└── 输出Markdown/     # 日常使用，只存放最终 .md 文件
```

`原始解析结果`不要当作阅读目录。平时只需要打开`输出Markdown`。

---

## 一键批量转换命令

把 PDF 或 DOCX 放进`输入PDF`后，打开终端，完整复制下面三段命令：

```bash
mkdir -p "/Users/zhuzhen0131/Documents/MinerU转换/原始解析结果" "/Users/zhuzhen0131/Documents/MinerU转换/输出Markdown"

MINERU_MODEL_SOURCE=modelscope "/Users/zhuzhen0131/Documents/NOTe/XI_playroom/MinerU/.venv/bin/mineru" \
  -p "/Users/zhuzhen0131/Documents/MinerU转换/输入PDF" \
  -o "/Users/zhuzhen0131/Documents/MinerU转换/原始解析结果" \
  -b pipeline \
  -m auto

find "/Users/zhuzhen0131/Documents/MinerU转换/原始解析结果" \
  -type f -name "*.md" \
  -exec cp -f {} "/Users/zhuzhen0131/Documents/MinerU转换/输出Markdown/" \;
```

命令结束并重新出现终端提示符后，打开：

`/Users/zhuzhen0131/Documents/MinerU转换/输出Markdown`

这里会直接排列所有`.md`文件，不再需要进入“书名 → auto”文件夹逐个寻找。

---

## 只转换一份 PDF

把下面命令中的`你的文件名.pdf`换成真实文件名：

```bash
MINERU_MODEL_SOURCE=modelscope "/Users/zhuzhen0131/Documents/NOTe/XI_playroom/MinerU/.venv/bin/mineru" \
  -p "/Users/zhuzhen0131/Documents/MinerU转换/输入PDF/你的文件名.pdf" \
  -o "/Users/zhuzhen0131/Documents/MinerU转换/原始解析结果" \
  -b pipeline \
  -m auto

find "/Users/zhuzhen0131/Documents/MinerU转换/原始解析结果" \
  -type f -name "*.md" \
  -exec cp -f {} "/Users/zhuzhen0131/Documents/MinerU转换/输出Markdown/" \;
```

---

## 中文扫描件识别不好

普通 PDF 默认使用`-m auto`。

如果某份 PDF 全是扫描图片，而且中文错字很多，将命令中的：

```bash
-m auto
```

改成：

```bash
-m ocr -l ch
```

不要默认把所有 PDF 都强制 OCR。普通文字 PDF 使用`auto`通常更快。

---

## 怎么判断完成了

成功时，终端会出现类似：

```text
Completed batch
Processed 10/10 pages
```

最后会重新出现可以输入命令的提示符。

如果出现下面内容，说明转换失败，需要检查最后一段错误：

```text
ERROR
failed
Traceback
```

---

## 使用注意

- PDF 或 DOCX 要直接放在`输入PDF`第一层，不要再套子文件夹。
- 再次运行时，同名 Markdown 会自动更新覆盖。
- 已经转换过的 PDF 如果继续留在`输入PDF`，下次批量运行还会再次转换。
- 最好每一轮只在`输入PDF`中放本轮需要处理的文件；完成后将源 PDF 移到自己的归档位置。
- `输出Markdown`只保留 Markdown，因此不会附带原 PDF 中提取出来的图片。
- 如果以后需要文章图片、版面检查或重新整理，到`原始解析结果`中寻找完整结果。
- 两份不同 PDF 如果拥有完全相同的文件名，扁平化后可能互相覆盖，应先修改其中一个 PDF 的文件名。

---

## 最短记忆版

```text
PDF 或 DOCX 放进“输入PDF”
→ 打开终端
→ 复制“一键批量转换命令”
→ 去“输出Markdown”拿 .md
```
