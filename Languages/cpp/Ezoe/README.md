# c++ basic

## Building and Compiling

### Build

以下の４つの処理をまとめてビルドと呼ぶ

```
source file

 |
 v

[preprocessor] :

 |
 | < temporary file
 v

[compiler] : ソースコードをアセンブラ言語のファイルに変換する

 |
 | < assembler file (*.asm)
 v

[Assembler] : アセンブラ言語のファイルを機械語に変換する

 |
 | < object code file (*.obj) : 機械語ファイルを”オブジェクトファイル”と呼ぶ
 v

[Linker] : 複数のオブジェクトファイルを一つにまとめる

 |
 | < object code
 v

実行ファイル (*.out, *.exe)
```

### Compile

preprocessor + compiler + assembler の３つの処理を Compile と呼ぶ

### まとめ

Preprocessor + Compiler + Assembler = Compile
Compile + Linker = Build

## pre compile header

```bash
g++ -std=c++2a -Wall -pedantic-errors -x c++-header -o all.hpp.gch all.hpp
```
