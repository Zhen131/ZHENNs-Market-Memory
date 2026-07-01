---
type: overview
status: active
title: "Writing Rules"
source_status: unsourced
sources: []
tags:
  - type/overview
  - status/active
  - vault/market-memory
  - home/writing-rules
created: 2026-07-01
updated: 2026-07-01
---

# Writing Rules 写作规则

## 1. Core Rule

Write for future reasoning, not for present emotion.

写作目标是服务未来判断，不是记录当下情绪。

Every note should be:

- precise
- structured
- linked
- searchable
- comparable
- useful for market reasoning

---

## 2. Prefer Mechanism Over Story

Do not only tell what happened. Explain how it happened.

Weak:

```text
Japan's bubble was very serious and caused long-term damage.
```

Better:

```text
easy credit
→ land and stock prices rise
→ collateral values rise
→ banks lend more against inflated collateral
→ leverage increases
→ policy tightening and price reversal expose balance-sheet weakness
→ firms and banks deleverage
→ growth slows for a long period
```

Use mechanism chains whenever the note involves crisis, boom, policy, war, inflation, banking stress, or asset price reaction.

---

## 3. Separate Facts, Mechanism, Interpretation, and Lessons

Do not mix evidence and opinion in the same paragraph.

Use sections like:

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

Definitions:

| Section | What Belongs Here |
|---|---|
| Facts | Dates, actors, events, policies, asset movements, sourced observations. |
| Mechanism | How one condition transmitted into another. |
| Interpretation | What the facts may mean. |
| Investment Lessons | Reusable risk and market lessons, not personal advice. |
| Open Questions | Missing sources, uncertain causality, data to verify. |

---

## 4. Write Causality Carefully

Financial history is usually multi-causal.

Avoid:

- "X caused Y" when the evidence is incomplete.
- "The only reason was..."
- "The market crashed because people panicked."
- "This proves that..."

Prefer:

- "one important channel was..."
- "a likely transmission mechanism was..."
- "this note still needs sources for..."
- "X may have amplified Y through..."
- "the causal chain appears to include..."

If a claim has no source, mark it as uncertain.

---

## 5. Use Bilingual Writing Where It Helps

Use English first and Chinese second when defining major concepts, note titles, or reusable labels.

Example:

```text
Collateral cycle 抵押品周期

Rising asset prices increase collateral values, which allows more borrowing and can further push prices higher.
资产价格上涨会提高抵押品价值，使更多借贷成为可能，并可能进一步推高价格。
```

Do not force every sentence to be bilingual. Use bilingual writing for clarity, searchability, and long-term reuse.

---

## 6. YAML and Tags Are Mandatory

Every structured note must include YAML frontmatter.

Minimum fields:

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

Allowed `type` values:

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

Use `draft` and `unsourced` when material is incomplete.

---

## 7. Tag Rules

Tags must be:

- lowercase
- English
- slash-based
- hyphenated for multi-word terms

Correct:

```text
type/event
status/draft
decade/1980s
region/asia
country/japan
pattern/asset-bubble
asset/real-estate
concept/leverage
impact/systemic
```

Incorrect:

```text
Japan
日本
Asset Bubble
金融危机
RealEstate
```

Tags classify notes. Links express relationships.

---

## 8. Link Rules

A note should not be isolated unless it is clearly a draft.

Event notes should link to:

- country or region notes
- pattern notes
- asset notes
- concept notes
- comparable event notes

Pattern, concept, asset, and country notes should link back to events that demonstrate them.

Avoid links to non-existing notes unless the missing note is intentionally planned. If the missing note matters, create a small draft placeholder with a TODO section.

---

## 9. File Naming Rules

For new event files, prefer:

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

For multi-year events:

```text
1980s - Latin America - Debt Crisis.md
1990s - Japan - Lost Decade.md
```

Do not use vague or emotional names.

---

## 10. Investment Lesson Rules

Investment lessons are allowed, but they must be separated from historical analysis.

Good:

```text
If a position depends on one macro thesis, define the condition that would prove the thesis wrong before entering the trade.
```

Bad:

```text
This means we should buy now.
```

Investment lessons should be:

- reusable
- conditional
- linked to mechanism
- clear about uncertainty
- not personalized financial advice

---

## 11. Style Rules

Prefer:

- headings
- bullet points
- tables
- mechanism chains
- short paragraphs
- explicit uncertainty markers

Avoid:

- long essays
- vague praise or fear
- unsourced precise numbers
- single-cause explanations
- motivational language
- duplicate notes
- broad changes when a narrow update is enough

The writing should make future comparison easier.

---

## 12. Final Checklist

Before finishing a note, check:

- Is the note type clear?
- Is it in the correct folder?
- Does it include YAML frontmatter?
- Are tags standardized?
- Are meaningful links present?
- Does it avoid duplicate existing notes?
- Are facts separated from interpretation?
- Is uncertainty marked?
- Is causality stated carefully?
- Is the note useful for future financial or market reasoning?

If the answer is no, keep improving the note or leave it as a draft.
