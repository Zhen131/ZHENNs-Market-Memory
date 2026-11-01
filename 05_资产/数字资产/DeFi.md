---
type: asset
status: draft
title: "DeFi"
summary: "去中心化金融：用链上智能合约做交易、借贷、喂价等金融服务，靠项目代币分收益；2020 年 DeFi Summer 兴起，脑总说它原来是左脚踩右脚，美股代币上链后才有了外部价值源。"
aliases: ["去中心化金融", "Decentralized Finance", "defy", "DeFi Summer"]
asset_class: crypto-asset
value_source:
  - protocol-fee-revenue
  - token-buyback-and-burn
  - holder-consensus
  - narrative
sensitive_to:
  - crypto-trading-volume
  - token-unlocks
  - regulation
  - smart-contract-security
  - risk-appetite
concepts: []
related:
  - "[[以太坊]]"
  - "[[稳定币]]"
  - "[[山寨币]]"
  - "[[股票代币]]"
source_status: partially-sourced
sources:
  - "Nasdaq（转 CoinDesk），2020-06-30，Compound Changes COMP Distribution Rules Following 'Yield Farming' Frenzy，https://www.nasdaq.com/articles/compound-changes-comp-distribution-rules-following-yield-farming-frenzy-2020-06-30"
  - "CoinDesk，2020-10-20，With COMP Below $100, a Look Back at the DeFi Summer It Sparked，https://www.coindesk.com/business/2020/10/20/with-comp-below-100-a-look-back-at-the-defi-summer-it-sparked"
  - "Unchained，2025-11-11，Uniswap Fee Switch Proposal Sparks 50% UNI Rally，https://unchainedcrypto.com/uniswap-fee-switch-proposal-sparks-50-uni-rally/"
  - "Cointelegraph，2025-12-22，Uniswap fee switch to go live as community vote set to pass，https://cointelegraph.com/news/uniswap-fee-switch-set-to-launch-before-2026"
  - "The Defiant，2025-11，Aave DAO Makes $50 Million Annual Token Buybacks Permanent，https://thedefiant.io/news/defi/aave-dao-makes-usd50-million-annual-token-buybacks-permanent"
  - "Aave 官方文档（据搜索摘要，2026-11-01 查），AAVE token，https://aave.com/docs/ecosystem/aave"
  - "Cooley，2026-09-22，Permission to Innovate: SEC Carves Out Path for On-Chain Stock Trading，https://www.cooley.com/news/insight/2026/2026-09-22-permission-to-innovate-sec-carves-out-path-for-on-chain-stock-trading"
  - "脑总 2026-03-01 股票估值入门（未核实）"
  - "脑总 2026-04-22 直播（未核实）"
  - "脑总 2026-08-13 科技怎么定价、股权稀释、HYPE、土地财政、特斯拉与SpaceX、黄金、软件股（未核实）"
  - "脑总 2026-08-24 科技股选股框架、ABCL与Voyager、紫光、伯克希尔、拼多多、金融工程（未核实）"
  - "脑总 2026-09-25 AI助手利好CPU、Meta像字节、股票代币与DeFi、抄巴菲特莱纳作业、爱马仕（未核实）"
tags:
  - type/asset
  - status/draft
created: 2026-11-01
updated: 2026-11-01
---

# DeFi

DeFi 是 Decentralized Finance 的缩写，中文叫去中心化金融：把交易、借贷这些本来由交易所、银行做的事，写成链上的智能合约，谁都可以直接用，不用开户、不用找中间人。常见的几类是：去中心化交易所，例如 Uniswap（代币 UNI）、PancakeSwap（CAKE），任何人都能往交易池里放两种币当[[做市商]]，别人来换币时分手续费；借贷协议，例如 Aave（AAVE）、Compound（COMP），存币收利息，或者押币借钱；预言机，例如 Chainlink（LINK），负责把链外的数据（比如股价）喂到链上，供合约使用。它们大多跑在[[以太坊]]这类公链上，交易时常用[[稳定币]]计价。

这些项目一般发自己的代币。早期代币多给团队和投资人，锁仓几年分批解锁；持币人能投票决定协议的规矩，有的项目还把手续费拿来回购、销毁代币。所以 DeFi 代币是[[山寨币]]里少数有机会按收入估值的一类。

## 2020 年的 DeFi Summer

DeFi 真正火起来是 2020 年夏天。借贷协议 Compound 从 6 月 15 日起，按用户在协议里存款和借款的多少发放治理代币 COMP，存钱、借钱的人都能“挖”到币，这种玩法被叫作流动性挖矿或收益耕作；据 DeFi Pulse 的数据，此后 Compound 锁定的资金从约 1 亿美元冲到 6 亿美元以上，各家协议纷纷跟进（Nasdaq 转 CoinDesk，2020-06-30）。这一波热潮被叫作 DeFi Summer；到 10 月 COMP 跌破 100 美元时，CoinDesk 把它当作这股热潮退去的标志（CoinDesk，2020-10-20）。脑总 2026-09-25 说，密集的那批 DeFi 项目都是 2020 年诞生的，2021 年前后陆续上了交易所，此后跌了四五年（据他说，未核实）。

## 它的价值从哪里来

- **协议收入**：交易手续费、借贷利差，是 DeFi 少有的真实收入。
- **回购和销毁**：有的项目把收入拿去买回代币。做法各不相同：Uniswap 2025 年 11 月提出、12 月投票通过的方案，把 v2、v3 部分交易池四分之一到六分之一的手续费转进一个合约，持币人销毁 UNI 才能换走，并一次性销毁约 1 亿枚 UNI（Unchained；Cointelegraph）；Aave 2025 年 11 月把每年 5000 万美元的回购定成常设计划（The Defiant），但据官方文档，买回的 AAVE 进入生态储备、按治理决定使用，并不销毁。
- **共识和故事**：没有外部收入的项目，价格主要靠有人接着买、有人接着讲故事。

## 它对什么敏感

图谱的分析：DeFi 的收入跟着链上交易量走，币圈冷下来收入就缩；锁仓代币集中解锁时，卖压会压过回购；智能合约一旦被黑，资金可能直接被盗；监管怎么划线，决定了传统资产能不能、以什么方式接进来。

2026 年 9 月 17 日，[[美国证监会]]发布“创新豁免”：经许可的代币化证券交易场所可以用自动做市商的交易池交易代币化美股，参与者和钱包要验证，有效期五年；完全去中心化、没有可识别运营者的协议不在豁免之内（Cooley，2026-09-22）。这是美股资产第一次被允许用 DeFi 式的交易池在链上交易，但老牌 DeFi 协议能不能直接接进来，还要看后续规则。

## 脑总怎么看它

以下是脑总的说法，未核实。按说话日期排：

- 2026-03-01：他拿币圈类比 AI，大模型像公链，AI 应用就像币圈的 DApp 或 DeFi 这一类；行业自己左脚踩右脚的需求不算真现金流。见 [[AI 和币圈同构，大模型的收入才是真现金流]]。
- 2026-04-22：有人问 DeFi 的安全性，他说除了加密货币本身，Web3 都是伪概念，DeFi 最终要拥抱监管，他更看重传统交易所推动美元资产上链。见 [[Web3 是伪概念，DeFi 最终要拥抱监管]]。
- 2026-08-13：讲科技怎么定价时，他说当年很多 DeFi「是左脚踩右脚螺旋升天啊」，有些链今天已经成了没人玩的“鬼链”。见 [[AI 和币圈同构，大模型的收入才是真现金流]] 文末 08-13 那一行。
- 2026-08-24：他说币圈的资本飞轮特别多，「所谓的左脚踩右脚螺旋升天」，这种飞轮容易被打破。见 [[资本飞轮容易复制，钱堆出来的优势不是壁垒]]。
- 2026-09-25：[[美国证监会]]给美股代币五年豁免后，他说美股接进来，DeFi「就不是一个左脚踩右脚了」，有了外部价值源；老牌的交易、借贷、预言机项目可能变成美股的离岸金融基础设施，锁仓代币基本解锁完、不少在回购，可以按收入和回购估值；做 LP 像不加杠杆的卖期权；链上用户还少，有流量红利。他说想法还不成熟。见 [[股票代币上链，给 DeFi 找到了外部价值源]]；同一期他还说 DeFi 加美元资产上链是币圈剩下最大的一片处女地，见 [[传统山寨季不会再有，散户赶不上筹码印的速度]]。

## 在历史里出现过的地方

![[反向关系.base#事件]]

## 各方怎么看它

![[反向关系.base#观点]]

## 来源与仍需确认的部分

- DeFi 的总锁仓规模没有写：几家数据网站 2026 年给的数从七八百亿到一千多亿美元不等，口径差别很大，没找到可靠的统一来源。
- 2021 年那一轮的高点、各项目代币的锁仓和解锁时间表没有查；脑总说「锁定期通常代币锁定期不会超过五年」，是他说的币圈惯例，未核实。
- Uniswap 2020 年 9 月给早期用户空投 UNI 等早期史，没有查。
