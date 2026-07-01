# Market Memory Agent Protocol

AI agents: read and follow the English text; the Chinese text is human-facing annotation and does not add separate requirements.  
AI 代理：只需要阅读并执行英文内容；中文是给人类用户看的对照说明，不额外增加规则。

---

## 1. Purpose

This vault is a structured knowledge base for financial history, economic mechanisms, monetary regimes, geopolitical shocks, and market behavior.  
这个知识库用于结构化研究金融历史、经济机制、货币制度、地缘冲击和市场表现。

The goal is not to collect everything. The goal is to build reusable, linked, searchable, and comparable knowledge for future market reasoning.  
目标不是记录一切，而是建立可复用、可链接、可搜索、可对比，并能服务未来市场推理的知识系统。

This vault should help answer:

这个知识库应帮助回答：

- What happened in a specific financial event or period?  
  某个金融事件或历史阶段发生了什么？
- What mechanisms caused risk to build, spread, or collapse?  
  风险通过什么机制积累、扩散或崩塌？
- How did policy makers, banks, households, firms, and markets respond?  
  政策制定者、银行、居民、企业和市场如何反应？
- How did assets behave across regimes and crises?  
  不同资产在不同制度和危机中如何表现？
- Which historical cases resemble each other?  
  哪些历史案例具有可比性？
- What reusable investment or risk lessons can be extracted?  
  可以提炼出哪些可复用的投资或风险经验？

This vault is not a general encyclopedia, news archive, diary, motivation space, or collection of loose essays.  
这个知识库不是通用百科、新闻归档、日记、鸡汤空间，也不是散文集合。

---

## 2. Core Principles

- Prefer mechanism over narration.  
  机制优先于叙事。
- Prefer facts over opinions.  
  事实优先于观点。
- Prefer structure over long prose.  
  结构优先于长篇散文。
- Separate facts, mechanisms, interpretation, uncertainty, and investment lessons.  
  区分事实、机制、解释、不确定性和投资启示。
- Do not overstate causality; financial events are usually multi-causal.  
  不要夸大因果关系；金融事件通常是多因共同作用。
- Do not add precise dates, numbers, or causal claims without a source or uncertainty marker.  
  没有来源或不确定性标记时，不要添加精确日期、数字或因果判断。
- Preserve user-written content unless the user explicitly asks for deletion or rewriting.  
  除非用户明确要求删除或改写，否则保留用户写过的内容。
- Avoid duplicate notes for the same event, concept, country, asset, pattern, or comparison.  
  避免为同一事件、概念、国家、资产、模式或对比创建重复笔记。
- Do not create new top-level folders without explicit user approval.  
  未经用户明确同意，不要创建新的顶层文件夹。

---

## 3. Folder Map

Use the existing bilingual folder structure as the source of truth. Do not rename it into English-only folders.  
以当前已经存在的双语目录结构为准，不要改成纯英文目录。

| Folder | Responsibility |
|---|---|
| `00_Home（首页）/` | Human entry points, purpose, usage, workflow, writing rules. / 人类入口、项目目标、使用方法、研究流程、写作规则。 |
| `01_Timeline（时间线）/` | Chronological context and period summaries; do not duplicate full event notes. / 时间线和阶段总览；不要重复完整事件笔记。 |
| `02_Events（事件）/` | Primary database for real historical events. / 真实历史事件的主要数据库。 |
| `03_Patterns（模式）/` | Recurring financial, economic, market, and policy patterns. / 反复出现的金融、经济、市场和政策模式。 |
| `04_Countries（国家）/` | Country or region context nodes, not the primary event structure. / 国家或地区背景节点，不是事件主结构。 |
| `05_Assets（资产）/` | Asset-class behavior across regimes and crises. / 不同周期和危机中的资产表现。 |
| `06_Concepts（概念）/` | Reusable mechanisms and financial concepts. / 可复用机制和金融概念。 |
| `07_Comparisons（对比）/` | Structured analytical comparisons. / 结构化分析对比。 |
| `99_Tool/Templates（模板）/` | Templates and operational helpers. / 模板和操作辅助材料。 |

---

## 4. Note Types

Every structured note should have one primary type.  
每篇结构化笔记都应该有一个主要类型。

Allowed types:

允许类型：

```text
event
pattern
country
asset
concept
comparison
timeline
overview
draft
```

- `event`: a real historical event. / 真实历史事件。
- `pattern`: a recurring market or economic pattern. / 反复出现的市场或经济模式。
- `country`: a country or region financial profile. / 国家或地区金融档案。
- `asset`: an asset-class behavior profile. / 资产类别行为档案。
- `concept`: a reusable mechanism or financial concept. / 可复用机制或金融概念。
- `comparison`: a structured comparison between cases. / 案例之间的结构化对比。
- `timeline`: a chronological overview. / 时间线总览。
- `overview`: a landing page inside a folder. / 文件夹内的总览页。
- `draft`: incomplete, unverified, or temporary material. / 不完整、未验证或临时材料。

---

## 5. Naming and Language

For new files, prefer stable English filenames. Keep existing bilingual folder names unchanged.  
新文件优先使用稳定英文文件名；保留现有双语文件夹名称。

For event files, prefer:

事件文件优先使用：

```text
YYYY - Country or Region - Event Name.md
```

Examples:

示例：

```text
1929 - United States - Great Depression.md
1971 - United States - Nixon Shock.md
1985 - Global - Plaza Accord.md
1989 - Japan - Asset Bubble Collapse.md
2008 - Global - Global Financial Crisis.md
```

For multi-year events, use the starting decade or historically standard name when appropriate.  
跨多年事件可使用起始年代，或使用历史上更通行的名称。

```text
1980s - Latin America - Debt Crisis.md
1990s - Japan - Lost Decade.md
```

Use English titles when possible. In body content, write bilingual explanations where useful, with English first and Chinese second.  
标题能用英文时优先使用英文；正文需要解释时使用中英双语，英文在前，中文在后。

Avoid vague, emotional, overly long, duplicate, or unstable file names.  
避免模糊、情绪化、过长、重复或不稳定的文件名。

---

## 6. YAML Metadata

Every structured note must include YAML frontmatter. YAML is the database layer of the vault.  
每篇结构化笔记都必须包含 YAML frontmatter；YAML 是这个知识库的数据库层。

Minimum required fields:

最低必需字段：

```yaml
---
type:
status:
title:
source_status:
sources:
tags:
created:
updated:
---
```

Allowed `status` values:

允许的 `status` 值：

```text
draft
active
reviewed
archived
```

Allowed `source_status` values:

允许的 `source_status` 值：

```text
unsourced
partially-sourced
sourced
verified
```

If the user provides unsourced rough material, keep it as `status: draft`, `source_status: unsourced`, and `sources: []`.  
如果用户提供的是未标来源的粗略材料，应保留为 `status: draft`、`source_status: unsourced`、`sources: []`。

Use `created` for the original creation date and `updated` for the latest edit date.  
`created` 表示原始创建日期，`updated` 表示最近编辑日期。

---

## 7. Tags and Links

Tags classify notes. Links express relationships.  
标签用于分类，链接用于表达关系。

Tags must be lowercase, English, slash-based, and hyphenated for multi-word terms.  
标签必须使用小写英文、斜杠结构，多词条使用连字符。

Correct examples:

正确示例：

```text
#type/event
#status/draft
#decade/1980s
#region/asia
#country/japan
#pattern/asset-bubble
#asset/real-estate
#concept/leverage
#impact/systemic
```

Incorrect examples:

错误示例：

```text
#Japan
#日本
#Asset Bubble
#金融危机
#RealEstate
```

Every structured note should contain meaningful Obsidian links. Avoid orphan notes unless they are explicitly marked as drafts.  
每篇结构化笔记都应包含有意义的 Obsidian 链接；除非明确标记为草稿，否则避免孤立笔记。

Event notes should link to relevant country, pattern, asset, concept, and comparable event notes whenever possible.  
事件笔记应尽可能链接到相关国家、模式、资产、概念和可比事件笔记。

Pattern, country, asset, and concept notes should link back to the events that demonstrate them.  
模式、国家、资产和概念笔记应反向链接到能体现它们的事件。

Avoid links to non-existing notes unless the missing note is intentionally planned. If important, create a small draft placeholder with a TODO section.  
避免链接到不存在的笔记；如果缺失笔记很重要，可以创建带 TODO 的小型草稿占位笔记。

---

## 8. Ingestion Workflow

When the user provides new material, first classify it.  
当用户提供新材料时，先判断材料类型。

Material types:

材料类型：

```text
historical event
pattern or mechanism
country or region
asset
concept
comparison
raw draft
source excerpt
mixed material
```

Then decide the operation.  
然后判断操作类型。

Operation types:

操作类型：

```text
create a new note
update an existing note
split into multiple notes
merge with an existing note
move a note
rename a note
create draft placeholders
leave as draft
```

Before creating a note, search for existing related notes to avoid duplication.  
创建笔记前，先搜索已有相关笔记，避免重复。

If the material contains multiple independent knowledge units, split them or update multiple existing notes.  
如果材料包含多个独立知识单元，应拆分，或更新多篇已有笔记。

Place each note in the correct folder, then add YAML, standardized tags, meaningful links, and source metadata.  
把每篇笔记放入正确目录，然后添加 YAML、标准化标签、有意义链接和来源元数据。

After editing, run the quality checklist in this file.  
编辑完成后，执行本文档中的质量检查清单。

---

## 9. Writing and Output Rules

Use concise analytical writing. Prefer headings, bullet points, tables, and mechanism chains over long paragraphs.  
使用简洁的分析型写作；优先使用标题、要点、表格和机制链，而不是长段落。

Separate these sections when relevant:

在相关时区分这些部分：

```text
Facts
Mechanism
Policy Response
Asset Price Reaction
Social and Economic Impact
Interpretation
Investment Lessons
Open Questions
```

Avoid vague sentences. Replace "This crisis had a huge impact" with the concrete transmission mechanism.  
避免空泛句子；不要写“这场危机影响巨大”，要写清楚具体传导机制。

When answering from the vault, use existing notes as primary context and separate vault facts, inferred analysis, uncertainty, and investment implications.  
基于知识库回答时，优先使用已有笔记，并区分知识库事实、推导分析、不确定性和投资含义。

Do not invent historical facts that are not in the vault or otherwise verified. If information is missing, say what is missing.  
不要编造知识库中没有、也没有被验证的历史事实；如果信息不足，要说明缺少什么。

When comparing events, use consistent dimensions: background, trigger, transmission mechanism, policy response, asset price reaction, long-term consequences, and investment lessons.  
对比事件时，使用一致维度：背景、触发因素、传导机制、政策反应、资产价格反应、长期后果和投资启示。

Prefer tables for comparisons.  
对比内容优先使用表格。

---

## 10. Source Rules

The vault does not require a separate source folder by default, but every structured note should preserve lightweight source metadata.  
默认不要求单独建立来源文件夹，但每篇结构化笔记仍应保留轻量来源元数据。

- `unsourced`: no clear source is attached. / 没有明确来源。
- `partially-sourced`: some claims have sources but not all. / 部分内容有来源。
- `sourced`: main factual claims are supported. / 主要事实有来源支持。
- `verified`: important factual claims have been checked against reliable sources. / 关键事实已对照可靠来源核查。

Do not mark unsourced user notes as verified.  
不要把未标来源的用户笔记标为已验证。

---

## 11. Quality Checklist

Before finishing any new or edited note, check:

完成任何新建或编辑笔记前，检查：

- Is the note type clear? / 笔记类型是否明确？
- Is the note in the correct folder? / 笔记是否放在正确目录？
- Does it include YAML frontmatter? / 是否包含 YAML frontmatter？
- Are `type`, `status`, `source_status`, `created`, and `updated` present? / 是否包含这些关键字段？
- Are tags standardized? / 标签是否标准化？
- Are meaningful Obsidian links present? / 是否包含有意义的 Obsidian 链接？
- Does it avoid duplicate existing notes? / 是否避免重复已有笔记？
- Are facts separated from interpretation? / 事实和解释是否分开？
- Is uncertainty marked? / 不确定性是否被标出？
- Is causality stated carefully? / 因果关系是否谨慎表述？
- Is the note useful for future financial or market reasoning? / 是否有助于未来的金融或市场推理？

---

## 12. Forbidden Practices

- Do not create vague notes with no links. / 不要创建没有链接的模糊笔记。
- Do not treat the vault as a general history archive. / 不要把这个知识库当成通用历史档案馆。
- Do not mix unrelated events into one oversized note. / 不要把无关事件混进一篇过大的笔记。
- Do not replace structured notes with long essays. / 不要用长篇散文替代结构化笔记。
- Do not use Chinese tags mixed with English tags. / 不要混用中文标签和英文标签。
- Do not generate investment advice without separating it from historical analysis. / 不要在未区分历史分析的情况下生成投资建议。
- Do not hide uncertainty. / 不要隐藏不确定性。
- Do not rename files casually. / 不要随意重命名文件。
- Do not make broad changes when a narrow update is enough. / 能小范围更新时，不要进行大范围改动。

---

## 13. Final Philosophy

Folders store facts by module.  
文件夹按模块存放事实。

Links express relationships.  
链接表达关系。

Tags classify notes.  
标签分类笔记。

YAML makes the vault queryable.  
YAML 让知识库可查询。

Comparison notes generate insight.  
对比笔记产生洞察。

Every note should be precise, structured, linked, searchable, comparable, and useful for future market reasoning.  
每篇笔记都应该精确、结构化、有链接、可搜索、可对比，并能服务未来的市场推理。
