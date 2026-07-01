---
type: overview
status: active
title: "写作规则"
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

# 写作规则

## 1. 核心规则

写作目标是服务未来判断，不是记录当下情绪。

每篇笔记都应该做到：

- 精确。
- 结构化。
- 有链接。
- 可搜索。
- 可比较。
- 能服务未来的市场推理。

---

## 2. 机制优先于故事

不要只写发生了什么，还要解释它是如何发生的。

弱写法：

```text
日本泡沫非常严重，并且造成了长期伤害。
```

更好的写法：

```text
宽松信贷
→ 土地和股票价格上涨
→ 抵押品价值上升
→ 银行基于膨胀后的抵押品继续放贷
→ 杠杆增加
→ 政策收紧和价格反转暴露资产负债表问题
→ 企业和银行开始去杠杆
→ 经济增长长期放缓
```

只要笔记涉及危机、繁荣、政策、战争、通胀、银行压力或资产价格反应，就优先使用机制链条。

---

## 3. 区分事实、机制、解释和经验

不要把证据和观点混在同一段里。

可以使用这些章节：

```text
事实
机制
政策反应
资产价格反应
社会和经济影响
解释
投资启发
未解决问题
```

定义：

| 章节 | 应该写什么 |
|---|---|
| 事实 | 日期、参与者、事件、政策、资产变动、有来源的观察。 |
| 机制 | 一个条件如何传导到另一个条件。 |
| 解释 | 这些事实可能意味着什么。 |
| 投资启发 | 可复用的风险和市场经验，不是个性化投资建议。 |
| 未解决问题 | 缺失来源、不确定因果、需要核查的数据。 |

---

## 4. 谨慎写因果关系

金融历史通常是多因素共同作用的结果。

避免：

- 在证据不足时写“X 导致了 Y”。
- 写“唯一原因是……”。
- 写“市场崩盘是因为人们恐慌”。
- 写“这证明了……”。

优先使用：

- “一个重要渠道是……”。
- “一个可能的传导机制是……”。
- “这篇笔记仍需要补充来源……”。
- “X 可能通过……放大了 Y”。
- “因果链条可能包括……”。

如果一个说法没有来源，就标记为不确定。

---

## 5. 必要时保留中英术语

这个库主要给自己阅读，所以正文优先使用中文。

但在定义重要概念、金融术语、模板名、文件名、标签、YAML 字段或可复用分类时，可以保留英文，方便搜索和长期管理。

示例：

```text
抵押品周期 collateral cycle

资产价格上涨会提高抵押品价值，使更多借贷成为可能，并可能进一步推高价格。
```

不要强迫每句话都双语。英文只在有助于概念准确、搜索或系统管理时保留。

---

## 6. YAML 和标签是必需的

每篇结构化笔记都必须包含 YAML frontmatter。

最低字段：

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

允许的 `type` 值：

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

允许的 `status` 值：

```text
draft
active
reviewed
archived
```

允许的 `source_status` 值：

```text
unsourced
partially-sourced
sourced
verified
```

材料不完整时，使用 `draft` 和 `unsourced`。

---

## 7. 标签规则

标签必须：

- 使用小写英文。
- 使用斜线结构。
- 多词用连字符。
- 不混用中文标签。

正确示例：

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

错误示例：

```text
Japan
日本
Asset Bubble
金融危机
RealEstate
```

标签负责分类，链接负责表达关系。

---

## 8. 链接规则

除非一篇笔记明确是草稿，否则不要让它孤立存在。

事件笔记应该链接到：

- 国家或地区笔记。
- 模式 pattern 笔记。
- 资产 asset 笔记。
- 概念 concept 笔记。
- 可对比事件笔记。

模式、概念、资产和国家笔记，也应该反向链接到能体现它们的事件。

避免链接到不存在的笔记。除非这个缺失笔记是有意规划的；如果它确实重要，可以创建一个带 TODO 的小型草稿占位笔记。

---

## 9. 文件命名规则

新事件文件优先使用：

```text
YYYY - Country or Region - Event Name.md
```

示例：

```text
1929 - United States - Great Depression.md
1971 - United States - Nixon Shock.md
1985 - Global - Plaza Accord.md
1989 - Japan - Asset Bubble Collapse.md
2008 - Global - Global Financial Crisis.md
```

跨多年事件可以使用：

```text
1980s - Latin America - Debt Crisis.md
1990s - Japan - Lost Decade.md
```

不要使用模糊、情绪化或不稳定的文件名。

---

## 10. 投资启发规则

可以写投资启发，但必须和历史分析分开。

好的写法：

```text
如果一个仓位依赖某个宏观判断，那么入场前就要定义什么条件会证明这个判断错误。
```

不好的写法：

```text
所以现在应该买。
```

投资启发应该：

- 可复用。
- 有条件。
- 和机制相连。
- 明确不确定性。
- 不是个性化金融建议。

---

## 11. 风格规则

优先使用：

- 标题。
- 要点。
- 表格。
- 机制链条。
- 短段落。
- 明确的不确定性标记。

避免：

- 长篇散文。
- 空泛的赞美或恐惧。
- 没有来源的精确数字。
- 单一原因解释。
- 鸡汤式表达。
- 重复笔记。
- 明明小范围更新就够，却做大范围改动。

写作应该让未来的对比更容易。

---

## 12. 最终检查清单

完成一篇笔记前，检查：

- 笔记类型是否清楚？
- 是否放在正确文件夹？
- 是否包含 YAML frontmatter？
- 标签是否标准化？
- 是否有有意义的链接？
- 是否避免重复已有笔记？
- 事实和解释是否分开？
- 不确定性是否标记？
- 因果关系是否写得谨慎？
- 这篇笔记是否能服务未来金融或市场推理？

如果答案是否定的，就继续修改，或者先保持为草稿。
