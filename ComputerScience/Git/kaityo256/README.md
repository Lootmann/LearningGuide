# GitHub 演習

## バージョン管理/管理システムとは

`バージョン`とは 更新履歴のこと  
更新履歴とは いつ、誰が、どんな変更をしたのかを記録しているもの

-> ”いつ、誰が、どんな変更をしたのかを記録” 管理システム

で、`バージョン管理システム`とは  
ドキュメントやソフトウェアの `バージョン` を管理するシステムのこと

現在完全に主流なのが `Git` というツール

## Repository and WorkingTree

```
sample/
  | - /.git
  | - /dir1
  | - /dir2
  |
  | - file1
  | - file2
  | - file3
    ...
```

`.git` があるディレクトリのことを `Repository` = `リポジトリ` と呼ぶ  
上の例では `sample` dir がリポジトリ

で、作業中のファイルやディレクトリのことを `WorkingTree` と呼ぶ

## Type of Repository

local repository : 自分の手元の PC にあるリポジトリ  
remote repository : サーバ上にあるリポジトリのこと

`WorkingTree` を持たないリポジトリを `bare repository`  
持つリポジトリを `non-bare repository` と呼ぶ

通常は サーバ上のリポジトリ = `Remote Repository` には `.git`のみを置く  
ので `bare repository`  
ローカルにはノンベアリポジトリになる

## Commit

`WorkingTree` に変更を加えると `.git` が持っている状態と（当然）差異が  
生じる ここで変更後の状態を `.git` に覚えてもらうために登録することを  
`Commit` = コミット と呼ぶ

コミットしたタイミングで、その時点での `WorkingTree` の状態がまるごと  
保存される ある時点でのプロジェクトの状態をまとめて `Snapshot` と呼ぶ

![commit](https://kaityo256.github.io/github/term/fig/commit.png)

各コミット間は好きなように移動できる  
つまりあらゆる履歴を自由に確認できるし  
任意の二点間の履歴を確認できる(=差異を確認できる)

## Index and Staging

Git には三種類の場所が存在する

`WorkingTree` -> `Index` -> `Repository`

変更点をリポジトリに登録(コミット)する間に  
全ての変更点を `Index` に登録する必要がある

で、この `Index` に登録するという行為を `Staging` と呼ぶ

```
             Staging
WorkingTree --------->  Staging Area/Index

                    commit
Staging Area/Index --------> Repository(.git)
```

っていう感じ
また `Index` = `Staging Area` とも呼ぶ
ステージングすると、ステージングエリアにいくの方がわかりやすい

コマンドとの対応はこんな感じ

![staging and commit](https://kaityo256.github.io/github/term/fig/staging_commit.png)

## HEAD and Branch

`branch` コミットへのポインタのこと
なので超軽量っていうかただのポインタ
どのコミットにも付けることが可能 `branch` はいくらでも作れる
そして `branch` の切り替えも簡単に行える
その状態でコミットすると新しいコミットの源流が作られる

`branch` の切り替えとは HEAD という特別なブランチのこと
今自分が見ているブランチのことを HEAD という

```
     main
     |
o -> o [HEAD]

     main
     branch
     |
o -> o [HEAD]

     main [HEAD]
     |
o -> o -> o
          |
          branch


:commit by main

           main [HEAD]
           |
        -> o
      /
o -> o -> o
          |
          branch
```

## Merge

ブランチの修正をもう一方のブランチに取り込むこと

- Fast-Forward Merge
  歴史が分岐していない状態のマージ

  ```
  main
  |
  o -> o -> o
            |
            branch
  ```

- Non Fast-Forward
  歴史が分岐している状態でのマージ

  ```
    main
    |
    o ->
   /
  o
   \
    o -> o
         |
         branch
  ```

### Non Fast-Forawrd

```
# new branch 'first'
git checkout -b first

touch hello
git add hello
git commit -m "add hello"

touch hello1
git add hello1
git commit -m "add hello1"

git checkout main
git merge --no-ff first # Merge branch 'first'

# new branch 'second'
git checkout -b second
touch one
git add one
git commit -m "add one"

touch two
git add two
git commit -m "add two"

git checkout main
git merge --no-ff second # Merge branch 'second'
```

という Git 操作で以下のような `git log` が作られる

```git
❯ gg

*        e6f638c  11 minutes ago        by"Hoge"    Merge branch 'second'  (HEAD -> main)
|\
| *      0091174  12 minutes ago        by"Hoge"    add two  (second)
| *      9bfc554  12 minutes ago        by"Hoge"    add one
|/
*        515f858  13 minutes ago        by"Hoge"    Merge branch 'first'
|\
| *      ea13984  13 minutes ago        by"Hoge"    add hello1  (first)
|/
*        88f1283  16 minutes ago        by"Hoge"    add hello
```

## branch switch

```
❯ git init
❯ touch README.md
❯ git add .
❯ git commit -m "add README"
❯ git branch new_branch
❯ git switch new_branch

❯ touch b
❯ git add .
❯ git commit -m "add b"
❯ git switch main
❯ git merge --no-ff new_branch

❯ gg
*   0854eec - (HEAD -> master) Merge branch 'new_branch' (49 seconds ago) <Lootmann>
|\
| * eab5e56 - (new_branch) add b (2 minutes ago) <Lootmann>
|/
* 02091df - first commit (3 minutes ago) <Lootmann>

❯ git branch fix_master
❯ git switch fix_master

❯ touch d
❯ git add .
❯ git commit -m "add d"
❯ touch e
❯ git add .
❯ git commit -m "add e"

❯ gg
* 26d8e13 - (HEAD -> fix_master) add e (2 seconds ago) <Lootmann>
* f80a3ab - add d (9 seconds ago) <Lootmann>
*   0854eec - (master) Merge branch 'new_branch' (2 minutes ago) <Lootmann>
|\
| * eab5e56 - (new_branch) add b (2 minutes ago) <Lootmann>
|/
* 02091df - first commit (4 minutes ago) <Lootmann>

❯ git branch
* fix_master
  master
  new_branch

❯ git switch master
❯ git merge --no-ff fix_master

❯ gg
*   020cbef - (HEAD -> master) Merge branch 'fix_master' (3 seconds ago) <Lootmann>
|\
| * 26d8e13 - (fix_master) add e (17 seconds ago) <Lootmann>
| * f80a3ab - add d (24 seconds ago) <Lootmann>
|/
*   0854eec - Merge branch 'new_branch' (2 minutes ago) <Lootmann>
|\
| * eab5e56 - (new_branch) add b (3 minutes ago) <Lootmann>
|/
* 02091df - first commit (4 minutes ago) <Lootmann>
```
