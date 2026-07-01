# Market Memory Agent Protocol

AI agents: read and follow the English instructions. Chinese text is human-facing annotation and does not add separate requirements.

AI 代理：执行英文规则；中文是给人类用户看的说明，不额外增加要求。

---

## 1. Agent Role

This vault is a structured market-memory system for financial history, economic mechanisms, monetary regimes, geopolitical shocks, policy response, asset behavior, and reusable market reasoning.

这个知识库是一个“市场记忆系统”，用于沉淀金融历史、经济机制、货币制度、地缘冲击、政策反应、资产表现和可复用的市场判断。

The agent is not only a summarizer. The agent is the vault maintainer. When the user asks to "ingest", "archive", "write this into the vault", "summarize this into the vault", or equivalent Chinese requests such as "入库", "整理进去", "写进知识库", the default behavior is to perform the full vault-ingestion operation.

AI 不是只负责总结，而是负责维护知识库。用户说“入库”“整理进去”“写进知识库”等表达时，默认执行完整入库动作。

Default ingestion means:

- search existing notes first;
- classify the material;
- choose the correct note type and folder;
- use the closest existing template;
- create or update notes;
- add YAML, disciplined tags, meaningful Obsidian links, and source metadata;
- update relevant existing nodes, indexes, or backlinks when useful;
- run the quality checklist before reporting back.

默认入库包括：先搜索、判断类型、选择文件夹和模板、创建或更新笔记、补 YAML/标签/链接/来源信息、必要时更新旧节点或索引，并完成质量检查。

Only pause for user confirmation when the next action would delete user-written content, rename many existing files, create a new top-level folder, publish or push externally, or when the material cannot be reasonably classified.

只有在要删除用户内容、大量重命名、创建新顶层文件夹、外部发布/推送，或材料完全无法判断时，才停下来询问用户。

---

## 2. Core Purpose

The goal is not to collect everything. The goal is to build notes that are precise, structured, linked, searchable, comparable, and useful for future market reasoning.

目标不是收集一切，而是让每篇笔记都精确、结构化、有链接、可搜索、可对比，并服务未来市场推理。

This vault should help answer:

- What happened in a specific financial event or period?
- What mechanisms caused risk to build, spread, or collapse?
- How did policy makers, banks, households, firms, and markets respond?
- How did assets behave across regimes and crises?
- Which historical cases resemble each other, and where does the analogy fail?
- What reusable risk, investment, or policy lessons can be extracted?

This vault is not a general encyclopedia, news archive, diary, motivation space, prediction machine, or loose essay collection.

---

## 3. Folder Map

Use the existing bilingual folder structure as the source of truth. Do not rename it into English-only folders. Do not create new top-level folders without explicit user approval.

以现有双语目录为准，不要改成纯英文目录，也不要未经确认创建新的顶层文件夹。

| Folder | Responsibility |
|---|---|
| `00_Home（首页）/` | Human entry points, project vision, usage, workflow, writing rules. |
| `01_Timeline（时间线）/` | Chronological home for dated event notes and period summaries. If an event has a clear year, decade, or date, place the primary event note in the matching century / decade folder here. |
| `02_Events（事件）/` | Event entry points, taxonomy, and indexes that link to timeline-hosted event notes; do not dump event notes in the root of this folder. |
| `03_Patterns（模式）/` | Recurring financial, economic, market, and policy patterns. |
| `04_Countries（国家）/` | Country or region context nodes, not the primary event structure. |
| `05_Assets（资产）/` | Asset-class behavior across regimes and crises. |
| `06_Concepts（概念）/` | Reusable mechanisms and financial concepts. |
| `07_Comparisons（对比）/` | Structured analytical comparisons. |
| `99_Tool/Templates（模板）/` | Templates and operational helpers. |

### Folder placement discipline

一级目录根部要保持干净，正文笔记不要直接堆在一级目录根部。

Root-level module folders must stay clean:

- In `01_Timeline（时间线）/`, use the existing century and decade folders. A dated event such as a 2026 event belongs under `01_Timeline（时间线）/2000s（21世纪）/2020-2029（2020-2029年）/`.
- In `02_Events（事件）/`, keep the root as an event index or taxonomy entry point. It should link to event notes in Timeline instead of duplicating them.
- In `03_Patterns（模式）/`, `04_Countries（国家）/`, `05_Assets（资产）/`, `06_Concepts（概念）/`, and `07_Comparisons（对比）/`, root-level files should normally be indexes or overview files only.
- Before writing a content note, look for an existing child folder that matches the subject, such as real estate, debt, currency crisis, inflation, war, technology, or platform economics.
- If no existing child folder fits, create one small, semantic child folder under the correct existing top-level module. This does not require confirmation. Do not create a new top-level folder without explicit user approval.
- A note is in the wrong place if it sits beside an index file in a module root when it could live in a category folder or a Timeline decade folder.

正文笔记必须进入合适的子目录；如果没有合适分类，就在现有一级目录下新建一个语义明确的小分类目录，不要把正文扔到根目录。

---

## 4. Note Types and Templates

Every structured note must have one primary `type`.

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

Use existing templates first:

| Material | Primary type | Folder | Template |
|---|---|---|---|
| A real historical case or crisis with a clear date | `event` | `01_Timeline（时间线）/<century>/<decade>/`; link it from `02_Events（事件）/Event Index（事件索引）.md` or a relevant event category index | `99_Tool/Templates（模板）/Event Template.md` |
| A real historical case without a clear date but with an event category | `event` | A relevant child folder under `02_Events（事件）/`; create a semantic child folder if none fits | `99_Tool/Templates（模板）/Event Template.md` |
| A recurring crisis or market structure | `pattern` | A relevant child folder under `03_Patterns（模式）/`; create a semantic child folder if none fits | `99_Tool/Templates（模板）/Pattern Template.md` |
| An asset-class behavior profile | `asset` | A relevant child folder under `05_Assets（资产）/`; create a semantic child folder if none fits | `99_Tool/Templates（模板）/Asset Template.md` |
| A reusable mechanism or financial idea | `concept` | A relevant child folder under `06_Concepts（概念）/`; create a semantic child folder if none fits | `99_Tool/Templates（模板）/Concept Template.md` |
| A country or region financial context | `country` | A relevant child folder under `04_Countries（国家）/`; create a semantic child folder if none fits | Use the established YAML and section rules from this file. |
| A structured comparison between cases | `comparison` | A relevant child folder under `07_Comparisons（对比）/`; create a semantic child folder if none fits | Use consistent comparison dimensions from this file. |
| A chronological period overview | `timeline` | The relevant century, decade, or overview folder under `01_Timeline（时间线）/` | Keep it chronological; do not duplicate event notes. |

If no exact template exists, follow the closest existing template style: YAML frontmatter, concise sections, tables where useful, mechanism chains, graph relations, investment lessons, and open questions.

如果没有完全对应的模板，就参考已有模板的结构，不要写成长篇散文。

---

## 5. Chat-to-Vault Ingestion Workflow

When the user provides spoken, rough, mixed, or story-like material and asks for ingestion, execute this workflow without waiting for a manual classification step.

用户用聊天方式讲材料并要求入库时，直接执行下面流程，不要把分类工作推回给用户。

### Step 1: Read and extract

Extract:

- the main event, mechanism, asset, country, or comparison;
- time period, region, country, actors, policies, and assets mentioned;
- source status: user memory, unsourced draft, source excerpt, or verified source;
- reusable concepts or patterns worth linking;
- uncertainty, missing facts, and claims that need verification.

### Step 2: Search before writing

Before creating a new note, search the vault with `rg` or filename search for:

- event name and alternate names;
- country or region;
- decade or year;
- asset class;
- crisis type;
- policy tool;
- concept or mechanism;
- comparable cases.

If a related note already exists, update it instead of creating a duplicate.

### Step 3: Decide operation

Choose the smallest operation that preserves meaning:

```text
update existing note
create a new note
split into multiple notes
merge with an existing note
create a small draft placeholder
leave as draft
```

For mixed material, split only when the knowledge units have different primary types. For example, a story about "Japan 1989 bubble collapse" may create or update an event note, while "collateral cycle" may update or create a concept note if it is reusable across many cases.

混合材料中，只有当知识单元属于不同主类型时才拆分；不要把无关内容硬塞进一篇大笔记。

### Step 4: Decide exact folder placement

Do this before writing the file.

1. If the note is an event and has a clear year, decade, or date, place the primary note in the matching Timeline decade folder.
2. Link the event from `02_Events（事件）/Event Index（事件索引）.md` or an existing event category index. Do not duplicate the event body in both Timeline and Events.
3. If the note is a pattern, concept, asset, country, or comparison, place it in an existing child folder under its module when one fits.
4. If no child folder fits, create a concise semantic child folder under the correct module, for example `Platform Economics（平台经济）/` or `Platform Economics Comparisons（平台经济对比）/`.
5. Do not place content notes directly next to module index files unless the module has no category structure and the user explicitly wants it.

先定位置再写文件。有明确年份的事件进 Timeline 年代目录；Events 负责索引调用。其他正文笔记进对应模块的子分类目录，没有合适分类就创建小的语义子分类。

### Step 5: Use templates and write the note

Use the relevant template. Keep writing concise and analytical.

Separate:

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

Do not invent precise dates, numbers, or causal claims. If the material is unsourced, mark it clearly as draft and uncertain.

### Step 6: Link into the graph

The note is not fully ingested until it is connected to the graph.

Minimum useful links for an event note:

- country or region;
- relevant patterns;
- relevant assets;
- relevant concepts;
- comparable events.

Pattern, concept, asset, and country notes should link back to the events that demonstrate them when the new material deepens or validates those nodes.

### Step 7: Update old nodes when the new note adds meaning

If a new event illustrates an existing concept, pattern, asset behavior, or country profile, update the existing node with a short backlink and one sentence explaining what the new note contributes.

Do not rely only on folder indexes. Indexes are entry points; conceptual meaning belongs in concept, pattern, asset, country, event, and comparison notes.

新笔记如果深化了旧概念、旧模式或旧资产节点，要反向更新旧节点。不要只依赖索引建立关系。

### Step 8: Update existing indexes only when appropriate

If a folder has an existing index file and the new note clearly belongs there, update that index. Do not create new index, MOC, or administrative middle-layer files unless the user explicitly asks.

如果已有索引，就按需更新；不要主动制造新的中转层。

---

## 6. Concept, Pattern, and Link Discipline

Tags classify. Links express meaning.

标签负责分类，链接负责表达关系。

Use `[[wikilink]]` inline for important concepts, mechanisms, assets, countries, and comparable events. Do not only list links at the bottom.

重要概念要在正文中内嵌 `[[wikilink]]`，不要只堆在文末。

Create a new concept or pattern node only when all or most of these are true:

- it is not already covered by an existing note;
- it is reusable across multiple events or regimes;
- it helps explain market behavior, policy response, asset pricing, or crisis transmission;
- it is likely to appear again in future research;
- it improves graph connectivity rather than adding noise.

Do not create a new node when:

- the term is a one-off mention;
- a close existing concept or pattern can cover it;
- the node would only restate a generic dictionary definition;
- the link would be vague and not useful for future reasoning.

Examples:

- `financial crisis` may be too broad as a standalone concept unless the note defines a reusable mechanism.
- `collateral cycle`, `balance-sheet recession`, `currency mismatch`, `liquidity spiral`, or `sovereign debt crisis` are better candidates when they explain multiple events.
- If the material is mainly a real case, create or update an `event` note first, then link to concepts and patterns.

When linking to missing but important nodes, either create a small draft placeholder with a TODO section or avoid the link until the node is useful enough to maintain.

---

## 7. Tag Discipline

Use lowercase English, slash-based, hyphenated tags. In YAML `tags`, omit the leading `#`.

YAML 中标签不写 `#`；正文里如果使用普通 hashtag，可以写 `#`。

Correct YAML tag examples:

```yaml
tags:
  - type/event
  - status/draft
  - decade/1980s
  - region/asia
  - country/japan
  - pattern/asset-bubble
  - asset/real-estate
  - concept/leverage
  - impact/systemic
```

Incorrect examples:

```text
Japan
日本
Asset Bubble
金融危机
RealEstate
```

Use tags sparingly:

- Always include `type/...` and `status/...`.
- Add decade, region, country, asset, pattern, concept, or impact tags only when they help filtering or search.
- Do not create many one-off tags.
- Do not use tags as a substitute for meaningful `[[wikilink]]` relationships.

---

## 8. YAML Metadata

Every structured note must include YAML frontmatter.

Minimum required fields:

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

```text
draft
active
reviewed
archived
```

Allowed `source_status` values:

```text
unsourced
partially-sourced
sourced
verified
```

If the user provides unsourced rough material, use:

```yaml
status: draft
source_status: unsourced
sources: []
```

Do not mark user memory, rough narration, or unsourced notes as `verified`.

---

## 9. Naming and Language

For new files, prefer stable English filenames. Keep existing bilingual folder names unchanged.

For event files, prefer:

```text
YYYY - Country or Region - Event Name.md
```

Examples:

```text
1929 - United States - Great Depression.md
1971 - United States - Nixon Shock.md
1985 - Global - Plaza Accord.md
1989 - Japan - Asset Bubble Collapse.md
2008 - Global - Global Financial Crisis.md
```

For multi-year events, use the starting decade or historically standard name when appropriate:

```text
1980s - Latin America - Debt Crisis.md
1990s - Japan - Lost Decade.md
```

Use Chinese for body explanations when that is clearer for the user. Preserve English for filenames, YAML fields, tags, note types, and important finance terms when it improves search or precision.

正文可用中文解释；文件名、YAML、标签、笔记类型和关键金融术语可保留英文以便搜索和精确管理。

---

## 10. Source and Uncertainty Rules

The vault does not require a separate source folder by default, but every structured note must preserve lightweight source metadata.

```text
unsourced          no clear source is attached
partially-sourced  some claims have sources but not all
sourced            main factual claims are supported
verified           important factual claims have been checked against reliable sources
```

Rules:

- Do not add precise dates, numbers, or causal claims without a source or uncertainty marker.
- Separate facts, mechanisms, interpretation, uncertainty, and investment lessons.
- Use uncertainty markers such as "needs source", "possibly", "one possible mechanism", or "causality is multi-factor".
- If live verification is required by the user or by the nature of the claim, verify before upgrading `source_status`.
- Investment lessons must be framed as historical or risk lessons, not personalized investment advice.

---

## 11. Writing Rules

Prefer mechanism over narration, facts over opinions, structure over long prose.

Use mechanism chains instead of vague impact statements.

Weak:

```text
This crisis had a huge impact.
```

Better:

```text
credit expansion
→ asset prices rise
→ collateral value rises
→ more borrowing becomes possible
→ leverage increases
→ policy tightening or income shock appears
→ refinancing becomes difficult
→ forced selling and defaults spread
```

When comparing events, use consistent dimensions:

- background;
- trigger;
- transmission mechanism;
- policy response;
- asset price reaction;
- long-term consequences;
- investment or risk lessons;
- where the analogy fails.

Prefer tables for comparisons.

---

## 12. Quality Checklist

Before finishing any new or edited note, verify:

- Is the note type clear?
- Is the note in the correct folder?
- If the note is a dated event, is the primary note in the correct Timeline decade folder?
- If the note is not an index or overview, is it inside a semantic child folder rather than a module root?
- Was the vault searched first to avoid duplicates?
- Was the closest existing template used?
- Does the note include YAML frontmatter?
- Are `type`, `status`, `source_status`, `created`, and `updated` present?
- Are tags lowercase, English, slash-based, and useful rather than noisy?
- Are important concepts linked inline with `[[wikilink]]`?
- Are graph relations listed or linked where useful?
- Were relevant old concept, pattern, asset, country, event, comparison, or index notes updated when the new material added meaning?
- Are facts separated from interpretation?
- Is uncertainty marked?
- Is causality stated carefully?
- Is the note useful for future financial or market reasoning?

When reporting back, list the files created or edited and mention any remaining uncertainty or missing sources.

---

## 13. Forbidden Practices

- Do not stop at a summary when the user asked to ingest material.
- Do not create vague notes with no links.
- Do not treat the vault as a general history archive.
- Do not mix unrelated events into one oversized note.
- Do not replace structured notes with long essays.
- Do not use Chinese tags mixed with English tags.
- Do not create duplicate notes for the same event, concept, country, asset, pattern, or comparison.
- Do not create many one-off concept nodes or tags.
- Do not hide uncertainty.
- Do not overstate causality.
- Do not rename files casually.
- Do not create new top-level folders without explicit user approval.
- Do not place content notes directly in module roots beside index files when a Timeline decade folder or category subfolder is available.
- Do not duplicate a full dated event note in both Timeline and Events; Timeline stores the primary dated note, Events indexes and links to it.
- Do not make broad changes when a narrow update is enough.

---

## 14. Final Philosophy

Folders store facts by module.

Links express relationships.

Tags classify notes.

YAML makes the vault queryable.

Templates keep notes comparable.

Comparison notes generate insight.

Every note should be precise, structured, linked, searchable, comparable, and useful for future market reasoning.
