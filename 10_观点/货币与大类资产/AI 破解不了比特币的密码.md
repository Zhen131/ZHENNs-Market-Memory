---
type: view
view_kind: judgment
status: active
title: "AI 破解不了比特币的密码"
summary: "有人说 AI 会破解椭圆曲线、让比特币暴跌，脑总说是扯淡：破解靠暴力计算不靠聪明，量子计算机工程难题太多，比特币又能升级；要防的是这种说法引起的恐慌。"
aliases: []
speaker: "[[脑总]]"
said_on: 2026-10-18
said_in:
  - "2026-10-18 直播"
about: ["[[比特币]]", "[[黄金]]", "[[奇观价值]]", "[[马斯克]]"]
fact_check: mixed
source_status: sourced
sources:
  - "Decrypt，2026-03-31，Google Quantum Paper Boosts Odds of Bitcoin 'Q-Day' by 2032, Researchers Warn，https://decrypt.co/362856/google-quantum-paper-boosts-odds-of-bitcoin-q-day-by-2032-researchers-warn"
  - "PostQuantum.com（专业网站，仅作参考），2026-03-31，Google Quantum AI Achieves 10x Reduction in Resources to Break Bitcoin's Cryptography，https://postquantum.com/security-pqc/google-quantum-bitcoin-ecdlp/"
  - "鉅亨网（转载金色财经），2026-08-27，Bitcoin Asia 2026 Justin Sun 炉边对话：量子威胁、AI 代理与比特币资本的全球化，https://news.cnyes.com/news/id/6589263"
  - "Motley Fool，2026-06-17，3 Quantum Computing Stocks Down Sharply -- but 1 Offers Exceptional Value，https://www.fool.com/investing/2026/06/17/3-quantum-computing-stocks-down-sharply-but-one-o/"
  - "24/7 Wall St.，2026-07-29，IonQ, Rigetti, and D-Wave Quantum Are Down 30% in a Month. Is More Pain Coming for Quantum Computing Stocks?，https://247wallst.com/investing/2026/07/29/ionq-rigetti-and-d-wave-quantum-are-down-30-in-a-month-is-more-pain-coming-for-quantum-computing-stocks/"
  - "Stock Analysis（数据网站，仅作参考），2026-10-16，IonQ 历史股价，https://stockanalysis.com/stocks/ionq/history/"
  - "Bitcoin Magazine，2026-02-12，Bitcoin Advances Toward Quantum Resistance with BIP 360 and New P2MR Output，https://bitcoinmagazine.com/news/bitcoin-advances-toward-quantum-resistance"
  - "bitcoin/bips 官方仓库，2024-12-18 编号（2026-02-10 改名 P2MR），BIP 360: Pay-to-Merkle-Root (P2MR)，https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki"
  - "bips.dev，2026-02-11 编号，BIP 361: Post Quantum Migration and Legacy Signature Sunset，https://bips.dev/361/"
  - "Decrypt，2026-04-15，New Bitcoin Proposal Would Freeze Coins to Counter Quantum Threat，https://decrypt.co/364450/new-bitcoin-proposal-would-freeze-coins-to-counter-quantum-threat"
  - "Satoshi Nakamoto，2008-10-31，Bitcoin: A Peer-to-Peer Electronic Cash System，https://bitcoin.org/bitcoin.pdf"
  - "Bitcoin Wiki，Secp256k1，https://en.bitcoin.it/wiki/Secp256k1"
  - "NIST，2020-05，SP 800-57 Part 1 Rev. 5: Recommendation for Key Management（表 2 安全强度对照），https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf"
  - "Bitcoin Optech，Taproot 专题页，https://bitcoinops.org/en/topics/taproot/"
tags: [type/view, view/judgment, status/active]
created: 2026-10-26
updated: 2026-10-26
---

> 第一，扯淡，这是扯淡的说法。AI 的发展不会破解椭圆曲线密码学。
>
> 黄金你怎么可能一天到晚搞酷炫的技术？马斯克的飞车才搞酷炫技术，黄金不需要酷炫的技术，要的就是稳定。
>
> —— 2026-10-18 直播

**一句话**：有人说 AI 会破解比特币的密码、让币价暴跌，脑总认为这是扯淡。破解靠的是巨量的计算和电，不是 AI 够不够聪明；真正可能有威胁的是量子计算机，可它还卡在一堆工程难题上，而比特币可以升级来防。他觉得该当心的，是这种说法吓到不懂的人。

### 他是在什么情况下说的

这是 2026-10-18 直播后半段的一个问答。前面刚聊完中海油和油价，一位会员问：“请问怎么看待 AI 发展会破解椭圆曲线、从而使 BTC 价格暴跌的说法？”

先说椭圆曲线是什么。比特币要管“谁有权花这笔钱”：每个人手里有一把私钥，用它给转账签名；别人用对应的公钥核对签名真假，但从公钥倒推不出私钥。这套数学就是椭圆曲线密码学。私钥一旦被人算出来，币就会被偷走。

这个担心当时正在发酵。〔背景〕2026 年 3 月 31 日，谷歌量子 AI 团队发表白皮书，估计破解比特币所用的 256 位椭圆曲线，可能只要不到 50 万个物理量子比特，比此前约 900 万个的估计少了约 20 倍，但仍是今天最大量子设备规模的约 500 倍（PostQuantum 的解读）。同一天 Decrypt 报道，研究员 Justin Drake 认为，2032 年前有量子计算机从公开的公钥算出私钥的概率至少有一成。8 月 27 日，孙宇晨在香港 Bitcoin Asia 2026 的对谈里说，假设 AI 按中等速度发展，量子威胁大约两年内可能出现，到 2027 年“安全概率”会降到约七成。

〔背景〕他顺口提到的量子计算股票，2026 年确实跌了几轮：6 月中旬 D-Wave、Rigetti 年内都跌了约两成；7 月下旬一个月里，IonQ 跌了 39%，另两家各跌约 30%。10 月 16 日 IonQ 收在约 31 美元（数据网站）。开发者这边，他点名的 BIP 360 在 2026 年 2 月并入了比特币改进提案的官方仓库，详见文末〔核对〕。

### 他怎么说

他的回答分四步。

第一步，破解不靠聪明。他说：「破解椭圆曲线密码学不是靠 AI 足够聪明就能够破解的，不是的，它就是一个暴力计算的问题。」他拿挖矿作比：「矿工们那么拼命地挖矿在干嘛？你破解椭圆曲线密码学也是一样，需要暴力计算。」既然拼的是算力和电，AI 帮不上忙，何况「现在的情况是 AI 都还缺电，AI 都还这么缺电，你去破解比特币的椭圆曲线密码学，可能吗？」他让会员自己去问问 AI，暴力穷举要用多大的能量。

第二步，真正的变数是量子计算机。他承认：「AI 的发展有可能导致新的计算方式出现，量子计算机出现，可能会破解椭圆曲线密码学，这个是有可能的。」但他接着反问：「你们量子计算的股票已经跌得很惨了吧？」又说：「目前来看，量子计算机上面有一大堆复杂的工程难题，一大堆复杂的工程难题。」他把难题分成两种。AI 搞定了很多数学问题，是因为那是「一个单一的复杂问题」，AI 能把可能性穷举一遍；造量子计算机却是一层叠一层的工程难题，这方面「AI 还没有这么厉害」。

第三步，就算量子计算机造出来，比特币也能改。「比特币本身是一个可以升级的东西。」他点了 BIP 360 提案：现在很多人用地址时已经把公钥露在链上，将来有了量子计算机，别人可能从公钥倒推出私钥；BIP 360 要做的，是让地址不暴露公钥。至于以中本聪为代表、多年没动过的老币，他说可以经过社区共识先暂时冻结，以后要取，再用零知识证明之类的方式。零知识证明是一类技术：能证明“我知道这个秘密”，却不用把秘密亮出来。

他说：「比特币不是一个死的东西，它是一个活的东西，它的技术在升级。只是社区相对来说比较保守，因为它的定位是黄金嘛。」接着就是开头那句黄金和飞车的话。在他看来，只有「真有致命的问题了，导致它要从黄金变成铜铁了，这个时候社区才会去做相应的升级。」

第四步，攻守不对等，真正要防的是人心。他说：「你想破解它，跟它的升级是不对等的。」「升级是很容易的事情……你要把它破解了，那真的是太难的工程问题了」。然后话锋一转：「但这个东西可能会造成不明真相的群众的恐慌，这有可能。」这里他说了一句标了重点的话：「很多时候你不仅要考虑事实是什么，还要考虑观点是如何影响人心的。」

他顺带点名，最近看到孙宇晨接受访谈还在说这个问题。他觉得孙宇晨「应该不至于不懂，他随便找个搞技术的人问一下就行了嘛」，所以「那孙哥说话，你就只能听一半。」最后他收回到币价：这种说法「可能会影响一些小白，小白不懂，可能就会卖，有这个可能，但实际上是没有影响的。」

紧接着，他讲了他认为真正影响币价的东西：渗透率，见 [[比特币每轮牛市的涨幅在变小]]。

### 拿什么来对照

他自己的对照是黄金和马斯克的飞车。这场直播一开头，他花了很长时间讲马斯克的飞车：从中学物理就能看出它商业价值不大，但它有[[奇观价值]]，能给品牌造势。讲到比特币时，他把飞车拿来当反面。

| | [[马斯克]]的飞车 | [[比特币]]（他说的定位） |
|---|---|---|
| 要的是什么 | 酷炫，让人转发、谈论 | 稳定 |
| 技术怎么变 | 不断搞新东西 | 不出致命问题，社区不动 |
| 为什么这样 | 造奇观能撑起品牌和估值 | 定位是[[黄金]]，「要的就是稳定」 |

〔图谱的对照〕这个类比也有不像的地方。黄金不用升级，它的稀少是物理决定的；比特币的稀少、以及“只有主人能花”，靠的是密码学，而密码学够不够安全，会随计算能力变化。所以比特币迟早要改，只是改得慢。改得有多慢，可以看上一次大升级：Taproot 在 2018 年 1 月提出，到 2021 年才在第 709,632 个区块生效。他说「升级是很容易的事情」，指的是写代码这一步；要全网同意、再让持币的人把币挪到新地址，按 BIP 361 草案的设想要三到五年。

### 这个判断靠什么、怕什么

它靠三件事。一是用普通计算机暴力破解 256 位椭圆曲线，在物理上做不到；二是能破解它的量子计算机，离造出来还远；三是在那之前，比特币社区能达成共识、完成升级。前两条是他自己讲的理由，第三条就是他说的「可以升级」。

它怕的，正是这三处出意外。

- 量子计算机来得比预期快。〔背景〕谷歌 3 月的估计把所需规模砍了约 20 倍，以后的估计还可能继续往下走。
- 升级慢于威胁。社区保守是他自己说的；要保护的币又很多：BIP 361 草案说，截至 2026 年 3 月 1 日，全部比特币里超过 34% 已经在链上露过公钥。
- 老币怎么处理会吵起来。〔背景〕BIP 361 4 月公开后，有人认为冻结旧币是必要的防守，也有人直说这就是没收，还担心一次有争议的升级会让网络分裂、伤到币价。

最后，他自己也承认：就算威胁是假的，恐慌可以是真的，不懂的人可能因此卖出。

〔核对〕

- **挖矿和破解签名不是同一道题。** 挖矿是反复计算 SHA-256 哈希（比特币白皮书）；签名用的是 secp256k1 椭圆曲线（比特币维基）。矿工的算力用不到破解私钥上，“跟挖矿一样”的说法不准确。但结论和他一致：用普通计算机从公钥倒推私钥，已知最快的办法也要约 2 的 128 次方步（NIST 把 256 位椭圆曲线定为 128 位安全强度），时间和能量都远超现实。量子计算机的威胁不是“更大的暴力”，而是换了算法：BIP 360 文本估计，用 Shor 算法约 10 的 8 次方步就能破解一把 256 位椭圆曲线公钥。这和他说的「新的计算方式」对得上。
- **BIP 360 的名字改过两次。** 最早叫 P2QRH（抗量子哈希支付），后改 P2TSH，2026 年 2 月 10 日定为 P2MR（默克尔根支付）。作者 Hunter Beast、Ethan Heilman、Isabel Foxen Duke。2 月并入官方仓库，仍是草案，并入不等于社区认可或启用。它让公钥平时不露在链上，防的是公钥长期暴露被慢慢算出；转账等待确认那几分钟它防不了，要以后再加抗量子签名。他说的“地址不暴露公钥”大致对得上。
- **冻结老币、再用零知识证明取回，不在 BIP 360 里。** BIP 360 写明老币怎么处理不归它管。它出自另一份草案 BIP 361（Jameson Lopp 等六人，2026 年 4 月公开）：启用约 3 年后不许再往旧式地址转币，再过 2 年冻结所有旧式币，给错过期限的人留一条用零知识证明取回的路。他是用“接下来”带出这件事的，内容对得上，只是出自别的提案。
- **量子计算股票跌得很惨**：对得上，见上文〔背景〕。
- **孙宇晨还在讲这个问题**：查到他 8 月 27 日在香港的对谈讲了量子威胁，而且正是从 AI 发展推到量子威胁；他说的“最近接受访谈”具体是哪一场，没查到。

**一句话记住**：破解一套密码和升级一套密码，难度不在一个量级。脑总认为，对比特币来说，AI 不是威胁，量子计算机还远，真正要防的是这种说法在不懂的人心里引起的恐慌。
