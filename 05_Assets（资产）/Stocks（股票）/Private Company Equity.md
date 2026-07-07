---
type: asset
status: draft
title: "Private Company Equity"
asset: "Private Company Equity"
asset_class: "equity"
value_source:
  - future cash flow claim
  - control or minority ownership claim
  - liquidity-event optionality
sensitive_to:
  - valuation
  - liquidity
  - information asymmetry
  - transfer restrictions
  - legal enforceability
related_events:
  - "[[2026 - China - Xiaohongshu IPO Employee Option Dispute]]"
related_patterns:
  - "[[Pre-IPO Governance Risk]]"
  - "[[Contractual Separation and Accountability Arbitrage]]"
related_concepts:
  - "[[Employee Stock Option]]"
  - "[[Equity Incentive]]"
  - "[[Initial Public Offering]]"
related_assets:
  - stocks
source_status: sourced
sources:
  - "Pre-IPO, Wikipedia: https://en.wikipedia.org/wiki/Pre-IPO"
  - "Private placement, Wikipedia: https://en.wikipedia.org/wiki/Private_placement"
  - "Investopedia, Discount for Lack of Marketability: https://www.investopedia.com/terms/d/dlom.asp"
tags:
  - type/asset
  - status/draft
  - asset/private-company-equity
  - asset/stocks
  - concept/liquidity
  - concept/information-asymmetry
created: 2026-07-07
updated: 2026-07-07
---

# Private Company Equity

## Private Company Equity 资产概览

一句话定义：

Private Company Equity 是未上市公司的股权、期权行权后股份或类似权益索取权；它的价值来自公司未来现金流和退出机会，但价格发现、交易流动性和合同执行都弱于公开市场股票。

---

## 1. 核心字段

| 字段 | 内容 |
|---|---|
| 资产类别 | equity / private equity claim |
| 价值来源 | 公司未来现金流、估值上升、控制权溢价、IPO / 并购 / 二级交易等流动性事件。 |
| 定价单位 | 通常以本币、美元或上市地货币估值；员工激励中常表现为行权价、授予价和估值差额。 |
| 主要持有者 | 创始人、早期员工、VC / PE、战略投资者、员工持股平台。 |
| 信用依赖 | 中。它不是债权，但高度依赖公司治理、合同承诺和退出路径。 |
| 流动性 | 低。转让限制、信息不对称和缺少公开交易市场会形成折价。 |

---

## 2. 敏感变量

| 变量 | 影响方向 | 说明 |
|---|---|---|
| 公司估值 | 估值上升提高账面财富；估值下修会压缩期权和股权激励价值。 | 未上市估值通常来自融资轮、内部估值或第三方交易，价格发现不连续。 |
| 流动性事件 | IPO、并购或二级转让提高可变现性。 | 没有退出路径时，账面价值不能直接等同现金。 |
| 信息不对称 | 信息越少，外部买方要求的折价越高。 | 未上市公司披露少，普通员工和小股东更难判断真实价值。 |
| 转让限制 | 限制越强，折价越高。 | 公司章程、股东协议、锁定期、优先购买权都会影响可交易性。 |
| 合同执行 | 执行越不确定，权益价值越低。 | 员工期权尤其依赖授予主体、归属条件、离职条款和争议解决地。 |
| 上市地监管 | 披露越充分，估值可信度可能提高。 | [[Initial Public Offering|IPO]] 会把内部权益安排推向公开审查。 |

---

## 3. 历史验证事件

| 时间 | 事件 | 资产表现 | 验证了什么变量 |
|---|---|---|---|
| 2026 | [[2026 - China - Xiaohongshu IPO Employee Option Dispute]] | 用户叙事中的核心财富载体，是员工期权背后对应的未上市公司股权价值；争议细节仍未由公开材料确认。 | 上市前股权的价值不只取决于公司估值，也取决于归属、行权、主体和退出路径。 |

---

## 4. 图谱关系

### 相关资产

- stocks

### 相关 Patterns

- [[Pre-IPO Governance Risk]]
- [[Contractual Separation and Accountability Arbitrage]]

### 相关 Concepts

- [[Employee Stock Option]]
- [[Equity Incentive]]
- [[Vesting and Exercise Conditions]]
- [[Initial Public Offering]]

### 相关国家 / 地区

- [[China Overview]]

### 相关 Comparisons

- [[Founder Contributor Purge vs Pre-IPO Incentive Cleanup]]

---

## 5. 投资启发

- 未上市公司股权的“估值”不是“现金”。只有当退出路径、转让权和法律执行路径清楚时，账面财富才接近可实现财富。
- 员工期权争议表面上是劳动或补偿问题，底层是 [[Private Company Equity]] 的归属、流动性和执行风险。
- 对拟上市公司，员工和早期投资者的未上市权益安排如果不清楚，可能在 IPO 前被重新定价为治理风险。

---

## 6. 未解决问题

- 小红书相关员工如确有期权，期权对应的是境外主体股权、境内主体权益，还是员工持股平台权益，需要合同或招股书确认。
- 不同司法辖区下，未上市公司股权的转让、税务、离职处理和争议执行路径需要单独研究。
- 未上市公司二级交易折价如何随 IPO 概率、锁定期和信息披露变化，需要后续案例补充。
