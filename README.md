*This project has been created as part of the 42 curriculum by heychong, katakaha.*

# A-Maze-ing

## プロジェクト概要

A-Maze-ingは、設定ファイルからランダム迷路（完璧迷路対応）を生成し、16進数壁表現でファイル出力、terminalで視覚化するPythonプロジェクトです。
DFS(深さ優先探索)とBFS(幅優先探索)を活用、「42」ロゴ入りで接続性保証、3x3以上のオープンスペースなし、PERFECTフラッグで完全迷路の形成
モジュールとしても再利用可能

## 実行方法

```bash
make install  # 依存関係インストール
make run  # 迷路生成→maze.txt出力→表示
make debug    # pdbデバッグ
make lint     # flake8 + mypyチェック
```

## configファイル形式
# CAUTION
上限：WIDTH * HEIGHT <= 1000
1000を超えると

```text
WIDTH=20               # 横セル数
HEIGHT=15              # 縦セル数
ENTRY=0,0              # 入口座標 (x,y)
EXIT=19,14             # 出口座標
OUTPUT_FILE=maze.txt   # 出力ファイル指定
PERFECT=True           # 完璧迷路（単一経路）
```

## 使用アルゴリズム

**再帰的バックトラッカー（DFS）**

開始セルから未訪問隣接セルへ再帰的に壁を削除、デッドエンドでバックトラック。

**選定理由：**

- 完璧迷路を自然生成
- O(N)効率、メモリ軽量
- 長い曲がりくねった通路（3x3オープンスペース回避）
- シード指定で再現性確保

## 役割分担

| メンバー | 担当 |
|----------|------|
| **heychong** | 設定解析、パース・バリデーション、迷路生成、「42」ロゴ実装|
| **katakaha** | 乱数シード生成、迷路ソルバー（BFS）、DFSアルゴリズム設計 |

## 再利用可能コード

Description:　needed
`mazegen-1.0.0.tar.gz`（pipインストール可能）

## プロジェクトマネージメント

**当初計画:** <br>*1日目:* 解析+迷路生成+hex表示<br>*2日目:* 42ロゴ+最短距離探索+ASCII表示<br>*3日目:* テスト・デバッグ+パッケージ化+README＆Makefile作成

**実績:**
- hex壁の同期処理を完璧に実装
- 設定解析をエッジケースまでカバー
- ASCII表示を期限内に仕上げ

**うまくいった点:**
- ペアプログラミングで素早く設計決定
- 全体の設計と実装のスピード感

**改善点:**
- Gitの運用をもっとスムーズに（rebase多用で混乱）
- 設計の具体性を事前に詰める
- 躊躇せずペースを維持する意識

**使用ツール:** git, mypy, flake8

## 出力ファイル形式

```text
AAAAAAAAAAAAAAAAAAAA  etc  # 各行16進数（N=0,E=1,S=2,W=3）
...
0,0                        # 入口
19,14                      # 出口
NESWWSEN...                # 最短経路
```

## ボーナス機能

-
-

## リソース

- [迷路探索プログラムのアルゴリズム](https://proglight.jimdofree.com/programs/vba/maze/)
- [PEP 257 Docstrings](https://peps.python.org/pep-0257/)
- [About Git Rebasing](https://docs.github.com/ja/enterprise-server@3.16/get-started/using-git/about-git-rebase)
- [3.6 Git のブランチ機能 - リベース](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%83%96%E3%83%A9%E3%83%B3%E3%83%81%E6%A9%9F%E8%83%BD-%E3%83%AA%E3%83%99%E3%83%BC%E3%82%B9)
- [.tomlファイルとは？](https://zenn.dev/manase/scraps/7cbf66961c94d8)
- [What Is Python's __init__.py For?](https://realpython.com/python-init-py/)
- [Pydantic入門 – Pythonでシンプルかつ強力なバリデーションを始めよう](https://qiita.com/Tadataka_Takahashi/items/8b28f49d67d7e1d65d11)

### AI利用内容

AIはアルゴリズム理解、課題仕様解釈、gitコマンド説明に使用。