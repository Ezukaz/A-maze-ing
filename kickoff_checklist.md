# A‑Maze‑ing Kick‑off Checklist

## 1. Language, tools & workflow

- [ ] Agree on Python version: `≥ 3.10` (both of you).
- [ ] Choose:
  - linter + mypy flags for `lint` / `lint‑strict`.
  - code formatter (e.g., `black`).
  - testing framework (`pytest` or `unittest`).
- [ ] Decide on:
  - virtual env tool (`venv` / `conda`).
  - how to share dependencies (e.g., `requirements.txt`).
- [ ] Establish basic workflow:
  - branch names (`main`, `dev`, feature branches).
  - sync frequency (daily “stand‑up” style check‑in).

## 2. Folder structure

- [ ] Agree on the project tree:

```text
a_maze_ing/
├── a_maze_ing.py
├── mazegen_*.py
├── Makefile
├── README.md
├── config.txt
├── tests/
└── .gitignore
```

- [ ] Decide who owns:
  - `a_maze_ing.py` (CLI + reading config).
  - `mazegen_*.py` (generator class + API).
  - `Makefile` / `README.md` / packaging.

## 3. Maze data model & API

- [ ] Decide on:
  - How to represent a cell (bit‑mask? separate `north`, `east`, … booleans?).
  - How to store walls so that **neighboring cells agree**.

- [ ] Sketch the `MazeGenerator` interface (example):

```python
mg = MazeGenerator(width=20, height=15, seed=123, perfect=True)
maze = mg.generate()
path = mg.get_shortest_path(entry=(0,0), exit=(19,14))
```

- [ ] Pick the **first algorithm** (e.g., recursive backtracker, Prim’s, or Kruskal’s).

## 4. Config + errors

- [ ] Confirm required config keys:
  `WIDTH`, `HEIGHT`, `ENTRY`, `EXIT`, `OUTPUT_FILE`, `PERFECT`.

- [ ] Decide:
  - How to handle bad values (e.g., `WIDTH=0`, `ENTRY` out of bounds).
  - Error‑message style (e.g., `print("Error: ...")` + `sys.exit(1)`).

- [ ] Agree that:
  - The program **never crashes on valid‑but‑bad input**; always graceful exit or skip.

## 5. Perfect / 42 / path

- [ ] Define how `PERFECT=True/False` affects the algorithm.

- [ ] Decide:
  - Where and how to place the **“42” pattern**.
  - What happens when the maze is too small for “42”.

- [ ] Choose method for shortest path:
  - BFS vs Dijkstra.
  - How to store / return the path (coordinates vs `N/E/S/W` string).

## 6. Visual representation

- [ ] Decide **primary mode**:
  - terminal ASCII, or
  - MLX window, or
  - both (who does which?).

- [ ] List basic user interactions you’ll implement first:
  - Regenerate maze.
  - Show/hide shortest path.
  - Change wall colours.

- [ ] Sketch the `Display` / `UI` interface:
  - One function per renderer?
  - Where does input‑handling live?

## 7. Reusable `mazegen` module

- [ ] Decide:
  - Exact module name (`mazegen_...`).
  - File location (`mazegen_*.py` at root).

- [ ] Agree on:
  - How to build the package (`.tar.gz` / `.whl`).
  - Which tools you’ll use (`setuptools` or `build`).

- [ ] Confirm:
  - `README.md` will include a short usage example of `mazegen`.

## 8. Documentation, AI, and planning

- [ ] In `README.md` decide who writes:
  - description,
  - setup/install/run instructions,
  - resources + AI‑usage section,
  - roles & planning section.

- [ ] Agree on:
  - How you’ll document **AI usage** (tasks, not code you copy‑paste blindly).
  - How to describe your **planning evolution** (initial plan vs reality).
