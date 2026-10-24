---
type: event
status: active
title: "Anthropic Claude Code 中国访问检测争议"
summary: "Anthropic 因限制中国用户、企业和疑似中转访问 Claude / Claude Code 的做法引发争议，暴露 AI 开发工具的安全治理、反蒸馏检测和平台信任边界问题。"
aliases: []
start_year: 2026
end_year: 2026
decade: 2020s
region: global
countries:
  - "[[美国]]"
  - "[[中国]]"
actors:
  - "[[Anthropic]]"
patterns: []
assets: []
concepts:
  - "[[平台信任边界]]"
  - "[[超越性价值]]"
impact_level: global
time_horizon: "short-term to long-term"
source_status: partially-sourced
sources:
  - "Anthropic，2025-09-04，Updating restrictions of sales to unsupported regions，https://www.anthropic.com/news/updating-restrictions-of-sales-to-unsupported-regions"
  - "Anthropic，2026-02-23，Detecting and preventing distillation attacks，https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks"
  - "TweakTown，2026-06，Anthropic says Alibaba used 25,000 fake accounts to query Claude 28.8 million times，https://tweaktown.com/news/112361/anthropic-says-alibaba-used-25000-fake-accounts-to-query-claude-28-8-million-times-and-train-qwen-off-the-results/index.html"
  - "The Next Web，2026-06，Anthropic accuses Alibaba of running the largest distillation campaign yet against Claude，https://thenextweb.com/news/anthropic-accuses-alibaba-distillation-claude-qwen"
  - "Financial Times，2026-07-02，Anthropic closes loopholes for Chinese access to Claude，https://www.ft.com/content/ad033063-60f9-4c0c-8d8a-9193a83e6f60"
  - "Investing.com，2026-07-03，Anthropic targets loopholes used by Chinese firms to access Claude, FT reports，https://www.investing.com/news/stock-market-news/anthropic-targets-loopholes-used-by-chinese-firms-to-access-claude-ft-reports-4774998"
  - "Anthropic，访问于 2026-07-06，Supported Countries and Regions，https://www.anthropic.com/supported-countries"
  - "Anthropic，访问于 2026-07-06，Consumer Terms，https://www.anthropic.com/legal/consumer-terms"
  - "Anthropic，访问于 2026-07-06，Commercial Terms，https://www.anthropic.com/legal/commercial-terms"
  - "Times of India，2026-07，Why Anthropic embedded spyware in Claude Code and attempted to hide it from users，https://timesofindia.indiatimes.com/technology/tech-news/why-anthropic-embedded-spyware-in-claude-code-and-attempted-to-hide-it-from-users-in-/articleshow/132111399.cms"
  - "Times of India，2026-07，Alibaba bans Claude Code from office environments from July 10，https://timesofindia.indiatimes.com/technology/tech-news/one-of-chinas-biggest-ecommerce-company-to-employees-starting-july-10-you-cannot-use-americas-/articleshow/132157569.cms"
  - "Tom's Hardware，2026，Anthropic claims Alibaba illicitly distilled its models，https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-claims-that-chinas-alibaba-illicitly-distilled-its-models-from-april-to-june-2026-says-effort-involved-25-000-fake-accounts-and-28-8-million-exchanges-on-claude"
  - "Anthropic，2026-10-12，Strengthening our defenses against distillation attacks，https://www.anthropic.com/news/distillation-defenses"
  - "Zhen 本人口述，2026-07-06，超越性价值、市场反身性与柯达类比（个人观察，不是事实来源）"
tags:
  - type/event
  - status/active
  - decade/2020s
  - region/global
  - impact/trust
  - theme/platform-economy
created: 2026-07-06
updated: 2026-10-24
---

# Anthropic Claude Code 中国访问检测争议

2026 年 7 月 2 日，《金融时报》报道了一件事：中国公司明明被 Anthropic 的服务条款挡在门外，员工却照样在用它的编程工具 Claude Code。蚂蚁集团通过新加坡子公司的企业账号、经公司内网接入；字节跳动给工程师报销个人订阅，工程师用 VPN 登录；还有公司借境外子公司的微软 Azure 云服务绕进去。报道说，Anthropic 正在一条条封堵这些通道，办法包括盯住账号所在电脑的时区，打掉替人转发请求的“中转站”。

这件事值得记下来，是因为它把一个老问题推到了新地方。限制谁能用、防止别人抄模型，这些原本发生在服务器那一头；可 Claude Code 装在开发者自己的电脑上，能读代码、能碰企业内网。检测一旦被认为伸进了本地环境，用户问的就不再是“能不能用”，而是“敢不敢信”。

## 事情是怎样一步步走到这里的

**规则先收紧。** Anthropic 的官方支持地区本来就不包括中国大陆，服务条款也禁止绕过地区限制、禁止用 Claude 训练竞争模型。2025 年 9 月 4 日，它又把规则扩大：只要一家公司被总部设在不支持地区的公司直接或间接控股超过 50%，无论它在哪里经营，都不能再用。

**再是蒸馏指控。** 蒸馏，就是拿别人大模型的回答当教材，去训练自己的模型。2026 年 2 月 23 日，Anthropic 发文说，DeepSeek、月之暗面、MiniMax 三家用约 2.4 万个虚假账号，和 Claude 进行了 1600 多万次对话来提取能力。6 月 10 日，它在给美国参议院银行委员会负责人的信里说，阿里巴巴相关的运营者在 4 月 22 日到 6 月 5 日之间，用近 2.5 万个虚假账号和 Claude 进行了 2880 多万次对话，比前三家加起来还多；路透社 6 月 25 日看到这封信后做了报道。阿里巴巴没有回应媒体的置评请求。

**然后是封堵中转。** 就是开头那篇 7 月 2 日的报道。报道还说，这些做法不违反美国或中国的法律，但违反了 Anthropic 的服务条款。

**最后是信任争议。** 同一时期，有媒体和用户把 Claude Code 里的检测逻辑说成隐藏监控、间谍软件甚至后门；还有报道说，阿里巴巴将从 2026 年 7 月 10 日起在办公环境中禁用 Claude Code。

## Anthropic 为什么要把门关得更严

前沿模型已经是昂贵的商业和战略资产。竞争者可以通过海量对话蒸馏它的能力；账号倒卖、代理中转和 API 滥用，又会让地区限制和合规要求形同虚设。对 Anthropic 来说，反蒸馏、执行服务条款、配合美国的相关合规要求，都有真实的动机。它 2026 年 10 月 12 日又发文说，新的防护上线以后，能被拿走的数据少了九成以上。

难点在执行方式。服务器那一头的风控，用户看不见也不太在意；同样的检测一旦进入本地开发工具，开发者就会追问：它读了什么、发到了哪里、怎样判断我在哪个地区、哪些行为会触发封号、我能不能关掉或审计它。目的合理，不等于每一种做法都合理。

这就是[[平台信任边界]]在本案中的意思：平台越深入用户的代码、密钥、代理设置和企业网络，越需要把自己的控制方式说清楚。用户分不清必要的风控和隐藏的监控时，工具就可能从生产力资产变成软件供应链风险。

## 争议怎样影响公司、用户和竞争者

对 Anthropic，更严的检测可能减少蒸馏、倒卖和违规访问，也可能增加企业安全审查和开发者流失。对中国开发者和企业，可用性下降会加强转向通义千问、DeepSeek、开源模型或本地部署的动机，这些替代方案也可能因此得到“更可控、更可审计”的说法上的优势。这些影响目前都还只是可能，没有数据证明已经发生。

对整个 AI 工具市场，采购标准会变：企业不再只比较模型能力和价格，还会检查遥测、本地权限、地区识别、数据留存和封禁机制。Anthropic 是[[美国]]前沿 AI 公司向全球输出工具和规则的一个样本；[[中国]]同时是受限的用户、替代模型的来源和企业安全审查的接收端。

这件事和[[2026 - 全球 - PlayStation 实体光盘退出]]都涉及平台改规则以后的信任成本，但不能混为一谈。PlayStation 的核心是数字所有权和长期访问；Claude Code 的核心是开发工具在本地环境里能看见什么、判断什么、控制什么。所以本案不宜硬归入[[数字分发锁定]]。

## Zhen 的观察：为什么从这件事想到「超越性价值」

（这一节是 Zhen 2026-07-06 口述的个人观察，不是脑总的话，也不是事实结论。原来的小标题写成了「脑总的投资观察」，是写错了，2026-10-24 改正。）

Zhen 的观察是：一家技术很强、产品很好、融资很热的公司，并不因此自动值得长期托付。[[超越性价值]]要求公司讲出的使命、做出的产品和压力下的选择能够互相支撑。对强调 AI 安全、宪法式 AI 和人类价值的 Anthropic 来说，执行是否透明、克制、可解释，本身就是品牌和治理的一部分。

柯达的类比也来自这一层。在 Zhen 的原始比喻里，柯达的价值不只是卖胶卷，而是让普通人更容易留住生活里的幸福时刻；它后来虽然发明了数码相机，却为了保护胶片生意没有充分拥抱新方向。这个类比不是说 Anthropic 会重演柯达，而是提醒投资者：技术能力不保证长期生存；公司在旧利益、竞争压力和更高使命冲突时选择保护什么，可能决定用户是否继续信任它。

〔核对〕能确认的：地区限制和禁止蒸馏的条款（官方页面）；2025-09-04 的控股规则（Anthropic 公告）；2 月和 6 月的两次蒸馏指控确实由 Anthropic 提出，但规模和归属都是它的单方面说法，不是独立技术调查或政府认定；监测电脑时区，有《金融时报》的报道（经 Investing.com 转述）支持。还不能确认的：网传的 Unicode 斜杠、短横线、引号、特征向量回传、隐藏名单等具体技术细节，没有找到权威代码审计或一手技术材料；阿里巴巴 7 月 10 日禁用的内部通知，没有找到可靠原件。

## 仍需确认的部分

- Claude Code 被指控的那些本地检测手段，哪些能由原始代码或独立安全审计证实？
- 阿里巴巴禁用 Claude Code 的内部通知是否存在可靠原件？
- Anthropic 会不会公开说明 Claude Code 的遥测、地区检测和本地环境访问边界？
- 争议会不会实际影响企业采购、开发者留存、后续融资或估值，目前没有足够数据。

**一句话记住**：防别人抄模型是正当的，但检测一旦进入用户自己的电脑，平台就得先把“我在看什么”说清楚，否则失去的是信任。
