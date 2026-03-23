*This project has been created as part of the 42 curriculum by heychong, katakaha.*

# A-Maze-ing

## プロジェクト概要

A-Maze-ingは、設定ファイルからランダム迷路（完璧迷路対応）を生成し、16進数壁表現でファイル出力、terminal/MLXで視覚化するPythonプロジェクトです。
グラフ理論と乱数アルゴリズムを活用し、「42」ロゴ入りで接続性保証、3x3以上のオープンスペースなし。

## 実行方法

```bash
python3 -m venv venv && source venv/bin/activate
make install  # 依存関係インストール
make run CONFIG=config.txt  # 迷路生成→maze.txt出力→表示
make debug    # pdbデバッグ
make lint     # flake8 + mypyチェック
```

## configファイル形式

```text
WIDTH=20               # 横セル数
HEIGHT=15              # 縦セル数
ENTRY=0,0              # 入口座標 (x,y)
EXIT=19,14             # 出口座標
OUTPUT_FILE=maze.txt   # 出力ファイル指定
PERFECT=True           # 完璧迷路（単一経路）
# SEED=42              # 乱数再現性
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
| **heychong** | 設定解析、パース・バリデーション、迷路生成、「42」ロゴ実装、MLX表示 |
| **katakaha** | 乱数シード生成、迷路ソルバー（BFS）、DFSアルゴリズム設計 |

## 再利用可能コード

Description:　needed
`mazegen-1.0.0-py3-none-any.whl`（pipインストール可能）

```python
from mazegen import MazeGenerator

gen = MazeGenerator(width=20, height=15, seed=42, perfect=True)
maze = gen.generate()  # {'grid': [...], 'entry': (0,0), 'exit': (19,14), 'path': 'NESW...'}
path = gen.solve()     # 最短経路文字列
```

## プロジェクトマネージメント

**当初計画:** <br>*1日目:* 解析+迷路生成+hex表示<br>*2日目:* 42ロゴ+最短距離探索+MLX表示<br>*3日目:* テスト・デバッグ+パッケージ化+README＆Makefile作成

**実績:**
- hex壁の同期処理を完璧に実装
- 設定解析をエッジケースまでカバー
- MLX表示を期限内に仕上げ

**うまくいった点:**
- ペアプログラミングで素早く設計決定
- 全体の設計と実装のスピード感

**改善点:**
- Gitの運用をもっとスムーズに（rebase多用で混乱）
- 設計の具体性を事前に詰める
- 躊躇せずペースを維持する意識

**使用ツール:** git, venv, mypy, flake8, pytest, MLX

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
- [グラフ理論の基礎](https://qiita.com/maskot1977/items/e1819b7a1053eb9f7d61)
- [MiniLibX Documentation](https://harm-smits.github.io/42docs/libs/minilibx/getting_started.html)
- [PEP 257 Docstrings](https://peps.python.org/pep-0257/)
- [About Git Rebasing](https://docs.github.com/ja/enterprise-server@3.16/get-started/using-git/about-git-rebase)
- [3.6 Git のブランチ機能 - リベース](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%83%96%E3%83%A9%E3%83%B3%E3%83%81%E6%A9%9F%E8%83%BD-%E3%83%AA%E3%83%99%E3%83%BC%E3%82%B9)

### AI利用内容

AIはアルゴリズム理解、課題仕様解釈、gitコマンド説明に使用。