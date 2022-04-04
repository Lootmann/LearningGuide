# .git objects

```bash
> ls
README.md blob

> git init blob
> tree blob/.git

blob/.git
├── FETCH_HEAD
├── HEAD
├── branches
├── config
├── description
├── hooks
│   └── ...
├── info
│   └── exclude
├── objects
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags
```

```bash
❯ cd blob
❯ echo -n "Hello Git" > test.txt
❯ git add test.txt

❯ tree blob/.git
blob/.git
├── FETCH_HEAD
├── HEAD
├── branches
├── config
├── description
├── hooks
│   └── ...
├── index
├── info
│   └── exclude
├── objects
│   ├── e5
│   │   └── 1ca0d0b8c5b6e02473228bbf876ba000932e96 # なんか出来てる
│   ├── info
│   └── pack
└── refs
    ├── heads
    └── tags
```

`objects/` のディレクトリとファイル名を連結したものを
`git cat-file` で確認する

```
├── e5
│   └── 1ca0d0b8c5b6e02473228bbf876ba000932e96

e5 + 1ca0d0b8c5b6e02473228bbf876ba000932e96
=> e51ca0d0b8c5b6e02473228bbf876ba000932e96

$ git cat-file -t e51ca0d0b8c5b6e02473228bbf876ba000932e96
```

## commit objects

```bash
└── objects
    ├── 0c
    │   └── 73d5b602168ecba3836f3993030ff0f2012190 # commit object
    ├── dd
    │   └── 1d7ee1e23a241a3597a0d0be5139a997fc29c8 # tree object
    └── e5
        └── 1ca0d0b8c5b6e02473228bbf876ba000932e96 # test.txt blob
```

```
❯ git cat-file -t e51ca0d
blob

❯ git cat-file -t 0c73d5b
commit

❯ git cat-file -t dd1d7ee
tree
```
