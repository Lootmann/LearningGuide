# The System Design Primer

## Movitation

Learn how to design large-scale systems.
Prep for the system design interview.

```
## 動機

大規模なスケールをするシステムをどうやって設計するのかを学ぶ
システム設計の面接試験に対する準備をする
```

### Learn how to design large-scale systems

Learning how to design scalable systems will help you become a better engineer.

System design is a broad topic. There is a **vast amount of resources scattered throughout the web** on system
design principles.

This repo is an organized collection of resources to help you learn how to build system at scale.

```
### 大規模なスケールをするシステムをどうやって設計するのか学ぶ

スケールするシステムをの設計手法を学ぶことは あなたをより良いエンジニアにする手助けをします
システム設計の話題は多岐にわたります システム設計の原理原則についての大量の教材が
Web 上のあらゆる場所に散乱しています
このリポジトリは それらの資材の整頓されたコレクションです（スケールするシステムをビルドする方法を学ぶための）
```

### Learn from the open source community

This is a continually updated, open source project.

Contributions are welcome.

### Prep for the systme design interview

In addition to coding interviews, system design is a **required component** of the **technical interview process** at
many tech companies

**Practice common system design interview questions** and **compare** your results with **sample solutions**:
discussions, code, and diagrams.

Additional topic ofr interview prep:

- Study guide
- How to approarch a system design interview question
- System design interview questions, **with solutions**
- Object-oriented design interview questions, **with solutions**
- Additional system design interview questions

```
### オープンソースコミュニティから学びましょう
このリポは継続的に更新され、そしてずっと OSS プロジェクトです
Contributions は歓迎します

### システム設計の面接への対策
コーディング面接（？）に加えて、システム設計は 数多くの Tech 企業の**技術面接の過程**で **必要不可欠な要素**です
多くのシステム設計面接の質問を実践します あなたの解答を模範解答と比べます
議論 コーディング ダイアグラムもついてるよ

- 勉強方針
- システム設計面接の取り組み方
- システム設計面接＋解答
- OO システム設計の問題＋解答
- 付加的な（？）システム設計の質問
```

## Index of system design topics

Summaries of various system design topics, including pros and cons.
**Everything is a trade-off.**
Each section contains link to more in-depth resources.

```
## システム設計の話題のインデックス
システム設計の話題のまとめ、利点と欠点を含む
すべてのものはトレードオフの関係にあります
それぞれのセクションもっと深い（難しい）教材のリンクを含みます

- 勉強方針
- システム設計面接の取り組み方
- システム設計面接＋解答
- OO システム設計の問題＋解答
- 付加的な（？）システム設計の質問
```

## Study Guide

Suggested topic to review based on your interview timeline(short, medium, long).
Q: For interviews, do I need to know everything here?
A: No, you don't need to know everything here to prepare for the interview.

What you are asked in an interview depends on variables such as:

- How much experience you have
- What your technical background is
- What positions you are interviewing for
- Which companies you are interviewing with
- Luck

```
## 勉強指針
面接タイムライン(? 短期、中期、長期) に基づいて提案された話題を見ていきます
質問: 面接において、ここにある全てを知っている必要があるのですか
解答: いいえ、面接の準備段階においてここにある全てを知っている必要はありません

面接で聞かれる質問は、以下のような様々なものに基づいて行われます
どのくらいの経験(=年数)持っていますか
あなたの技術的な背景はどんなものですか
面接対象になっているポジションは(? 立場役職なんか)
面接に行く企業はどこか
運
```

More experienced candidates are generally expected to know more about system design.
Architects or team leads might be expected to know more than individual contributors.
Top tech companies are likely to have one or more design interview rounds.

Start board and go deeper in a few areas. It helps to know a little about various key
system design topics. Adjust the following guide based on your timeline, experience,
what positions you are interviewing for, and which companies you are interviewing with.

- **Short timeline** - Aim for **breadth** with system design topics. Practice by solving
  **some** interview questions

- **Medium timeline** - Aim for **breadth** and **some depth** with system design topics.
  Practice by solving **many** interview questions.

- **Long timeline** - Aim for **breadth** and **more depth** with system design topics.
  Practice by solving **most** interview questions.

```
より経験を持っている候補者には システム設計について多くのものを知っていることを期待されます
アーキテクトまたはチームリーダーは個人のコントリビューターよりも多くのことを知っていることを
期待される場合があります
トップの技術系企業は設計面接ラウンドを一回以上行う可能性があります

いくつかの領域においてはボードを初めて（？）より深いところへ Go
それは様々なシステム設計の話題の鍵についてを少しだけ知ることの手助けになります
あなたのタイムライン、経験、面接、面接の対象のポジション に基づいて下のガイドを調節します

Short timeline - システム設計の話題について幅広く目標にしましょう
いくつかの面接の質問を解く練習をしましょう

Medium timeline - システム設計の話題について幅広くそして、多少深く目標にします
たくさんの面接の質問を解く練習をしましょう

Long timeline - システム設計の話題に空いて幅広くそしてもっと深く目標にします
全ての面接の質問を解く練習をしましょう
```

## How to approach a system design interview question

How to tackle a system design interview quesion.

The system desing interview is an **open-ended conversation**. You are expected to lead it.

You can use the following steps to guide the discussion. To help solidify this process,
work through the System interview questions with solutions section using the following steps.

```
## システム設計の面接対策
システム設計の質問の取り組み方
システム設計面接は「自由質問であり」「はい、いいえ」で答えられる質問ではない
あなたはそれを導くことを期待されています
議論をガイドする、続く段階を利用します このプロセスを固めるのを助けるために
これに続くステップを使いながら、解答セクションについて、システム設計の質問を乗り越えましょう
```

### Step 1: Outline use cases, constraints, and assumptions

Gather requirements and scope the problem. Ask questions to clarify use cases and constraints.
Discuss assumptions.

- Who is going to use it?
- How are they going to use it?
- How many users are there?
- What does the system do?
- What are the inputs and outputs of the system?
- How much data do we expect to handle?
- How many requests per second do we expect?
- What is the expected read to write ratio?

```
## Step 1: 使用事例の概要、成約、予測

要件を収集して問題の範囲を特定します 使用事例と成約を明確にするために質問をします
予測を議論します

- 誰が使うのか
- それをどのように使うのですか（全然明確な質問に見えないっすけど）
- ユーザの数は
- システムは何をしますか
- システムの入力と出力
- 我々が期待している処理の量はどのくらい
- 期待されている一秒間のリクエスト量は
- 期待される Read と Write の比率はどのくらい
```

### Step 2: Create a high level design

Outline a high level design with all important components.

- Sketch the main components and connections
- Justify your ideas

```
### Step 2: 高いレベルのデザインを作る

重要なコンポーネント全ての高レベルなデザインの概要を作る
主なコンポーネントとそれらの連携をスケッチ（図に書く？）
アイデアを正当化する（？ ちゃんと動くシステム化どうかを考える的な）
```

### Step 3: Design core components

Dive into details for each core component. For example, if you were asked to design a url shortening service,
disscuss:

- Generating and storing a hash of the full url
  - MD5 and Base62
  - Hash collisions
  - SQL or NoSQL
  - Database schema
- Traslating a hashed url to the full url
  - Database lookup
- API and Object-oriented design

```
### Step 3: 核となるコンポーネントをデザインする

核コンポーネントそれぞれについて、詳細を深堀する 例えば、URL-短くする-サービスを設計することを質問されたとします
議論

- フル URL のハッシュを生成して、保持しておく
  - MD5 と Base62
  - ハッシュの衝突について
  - SQL か NoSQL か
  - データベーススキーム
- ハッシュ URL からフル URL に変換する
  - データベースのルックアップ
- オブジェクトオリエンテッド設計と API について
```

### Step 4: Scale the design

Identify and address bottlenecks, given the constrains. For example, do you need the following to address scalability
issues?

- Load balancer
- Horizontal scaling
- Caching
- Database sharding

```
### Step 4: 設計をスケールさせる

ボトルネック（全体の処理が遅くなっている、一部の処理や動作こと　そこら編にある飲み物の瓶は口が細くなっていて出力量を著しく制限している）
の特定して対処する、与えられた制約に基づいて
例えば、あなたは 拡張性の問題に対処するために以下に以下の事柄は必要ですか

- 負荷分散
- 水平スケーリング（サーバーの台数増やすこと、Vertical scaling は DB のインスタンスタイプ上げること、容量増やすこととか）
- キャッシュ
- DB のシャーディング
```

Discuss potential solutions and trade-offs. Everything is a trade-off. Address bottlenecks using principles of scalable
system design.

```
潜在的な解答？とトレードオフを議論する すべてのものはトレードオフの関係にある
スケーラブルなシステム設計の 原則を利用して、ボトルネックを処理する
```

### Back-of-the-envelope calculations

You might be asked to do some estimates by hand. Refer to the Appendix for the following resources:

- Use back of the envelope calculations
- Powers of two table
- Latency numbers every programmer should know

```
### 簡単な計算(封筒の裏側を使えば出来るような計算の意味)

手計算で見積もりを行うように求められる場合があります 以下に資源は付録を参照してください

- 封筒の裏で研鑽を使用
- ２乗の計算テーブル
- 全プログラマーが知っているべきレイテンシーナンバー(?)
```

### Source(s) and further reading

Check out the following links to get a better idea of what to expect:

- How to ace a systems design interview
- The system design interview
- Intro to Architecture and Systems Design Interviews
- System design template

```
### ソースコードそしてその後に読むもの

期待されているものについての良いよりアイデアを得るためのリンクはこちら

- システム設計の面接を ACE する方法
- システム設計の面接
- アーキテクチャ、そしてシステム設計面接のへの導入
- システム設計のテンプレ
```

## System design interview questions with solutions

Common system design interview questions with sample discussions, code, and diagrams.
Solutions linked to content in the `solutions/` folder.

```
## システム設計の面接 解答付き

よくあるシステム設計面接、サンプルな議論、コード、ダイアグラム
解答は `solutions/` folder の中にリンクがついてます
```

## Object-oriented design interview questions with solutions

## System design topics: start here

New to system design?

First, you'll need a basic understanding of common principles, learning
about what they are, how they are used, and their props and cons.

```
## システム設計トピックス ここあらスタート

システム設計は初めてですか

まずはじめに、あなたは原理原則の基本的な理解が必要です
それらが何で、どうやって使って、それらの利点欠点について学ぶ
```

### Step 1: Review the scalability video lecture

Scalability Lecture at Harvard

- Topics covered:

  - Vertical scaling
  - Horizontal scaling
  - Caching
  - Load balancing
  - Database replication
  - Database partitioning

```
### Step 1: スケールについての講義ビデオを見る

ハーバードのスケーラビィティ講義

- カバーしている話題
  - 垂直スケーリング
  - 水平スケーリング
  - キャッシュ
  - 負荷分散
  - DB のレプリケーション
  - DB パーティショニング(テーブル内のデータを分割して保持する機能)
```

### Step 2: Review the scalability article

Scalability

- Topics covered:
  - Clones
  - Databases
  - Caches
  - Asynchronism

### Next Steps

Next, we'll look at high-level trade-offs:

- Performance vs scalability
- Latency vs throughput
- Avaiability vs consistency

Then we'll dive into more specific topics such as DNS, CDNs, and
load balancers.

## Performance vs scalability

A service is **scalable** if it results in increased **performance**
in a manner proportional to resources added. Generally, increasing
performance means serving more units of work, but it can also be to handle
larger units of work, such as when datasets grow.

```
## パフォーマンス vs 拡張性

追加されたリソースに比例して その結果としてパフォーマンスが
向上するのであれば そのサービスは スケーラブルであるいいます
一般的に パフォーマンスが上がるとは "units of work" をもっとサーブする
ことを言います ただ、それは同時に大量のユニットを扱わなければ行けないので
データセットが大きくなるときなどです
```

Another way to look at performance vs scalability:

- If you have a performance problem, your system is slow for a single user.
- If you have a scalability problem, your system is fast for a single user
  but slow under heavy load.

```
パフォーマンス vs スケーラビリティ の別の観点

- もしパフォーマンスに問題があれば、そのシステムは一人のユーザに対して遅い
- もし拡張性に問題があれば、そのシステムは一人のユーザに対して早いか
  ただ大きい処理のもとでは遅くなります
```

## Latency vs thoughput

**Latency** is the time to perform some action or to produce some result.
**Thoughput** is the number of such actions or results pre unit of time.

Generally, you should aim for **maximal throughput** with **acceptable latency**.

```
## レイテンシ vs スループット

レイテンシとは時間のこと 何かのアクションや何かの結果を生み出すのにかかる
スループットとはアクションや結果の数のこと 時間単位で

一般的に、許容できるレイテンシで、最大のスループットを求めるべきです
```

## Availability vs consistency

In a distributed computer system, you can only support two of the following
guarantees:

- **Consistency** - Every read receives the most recent write or an error

- **Availability** - Every request reveives a response, without guarantee
  that it contains the most recent version of the information

- **Partition Tolerance** - The system continues to operate despite arbitrary
  partitioning due to network failures

Networks aren't reliable, so you'll need to support partition tolerance.
You'll need to make a software tradeoff between consistency and availability.

```
## 可用性 vs 一貫性

分散コンピュータシステム、以下の”２つ”の事柄だけサポートしています

**一貫性** - 全ての読み取りは、最近の書き込みもしくはエラーを受け取る

**可用性** - 全てのリクエストはレスポンスを受け取る
          最近のバージョンの情報を含んでいる保証無しで

**分断耐性** - システムはネットワークの失敗によって 任意のパーティショニングに
          関わらず操作を継続します
```

### CP - consistency and partition tolerance

Waiting for a response from the partitioned node might result in a timeout error.
CP is a good choice if your business needs require atomic reads and writes.

```
### CP - 一貫性 と ネットワーク分断耐性

"パーティションされたノードからレスポンスを待つこと"は
タイムアウトエラーという結果をもたらすことになるでしょう
(いつレスポンスが戻ってくるかわからんからね)

CP は良い選択になります
もしあなたのビジネスが アトミックな読取書込を必要としたとき
```

### AP - availability and partition tolerance

Responses return the most readily available version of the data available
on any node, which might not be the latest. Writes might take some time
to propagate when the partition is resolved.

AP is a good choice if the business needs allow for eventual consistency or when
the system needs to continue working despite external errors.

```
### AP - 可用性 と 分断耐性

レスポンスは 最もすぐに利用できるバージョンのデータを返します
利用できる全てのノードの中で, そしてそれは最新のデータとは限りません

APは良い選択です もしビジネスは最終的な一貫性があればOK
もしくは、外部のエラーが出るかどうかに関わらず、
システムが動き続けなければならない要求があるとき
```

## Consistency patterns

With multiple copies of the same data, we are faced with options on how to
synchronize them so clients have a consistent view of the data. Recall the
definition of consistency from the `CAP theorem` - Every read reveive the most
recent write or an error.

```
同じデータのたくさんのコピーを持っている状態で
我々は〜という選択に直面します それらをどうやって同期させるのか
クライアントはそのデータに対して一貫したビュー（？）を持っている

CAP 理論の”一貫性”の定義を思い返してほしい
あらゆる読み取りは、直近の書き込みを取得もしくはエラーであると
```

## Terms

Atomic : トランザクションに含まれるタスクが全て実行されるか
あるいは全く実行されないことを保証する性質
