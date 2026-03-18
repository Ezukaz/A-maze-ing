# A-maze-ing Process

**Date Started**: 2026-03-19

**Goal**: *Make something that …* (e.g., parses and sorts stack commands)

## Description

- Briefly describe the problem or task.
- Who is this for (even if it’s just you)?
- One or two sentences about the overall approach.

## Initial Strategy

<details>
<summary>Brainstorm</summary>

-  **Restate**: What exactly are you trying to achieve?
-  **Input**:
-  **Output**:
- **Success**: What does success look like?
- **Constraints**: Time, memory, allowed functions, complexity, coding style, etc.
- **Smallest case**: Write one tiny example that proves the idea works.
- **Brute force**: How would you solve it if performance didn’t matter?
- **Invariants**: (if violated then error)
  - eg. Stack always valid
  - eg. Memory always freed
  - “if violated, it’s an error”
- **Assumptions**:

> Check checklist to get started -> [Click Me](./kickoff_checklist.md)
</details>


## Structure

<details>
<summary>Tree</summary>

### File Structure
```
project/
├── docs/
|  ├── process.md
├── inc/
|  ├── header1.h
|  ├── header2.h
├── lib/
|  ├── library1/
|  ├── library2/
├── src/
|  ├── .c
|  ├── .c
|  ├── .c
|  ├── .c
|  ├── .c
|  ├── .c
|  ├── .c
|  ├── .c
├── .gdbinit
├── .gitignore
├── Makefile
└── README.md
```
> Update this only when the structure changes significantly, not for every small file.

### Flow Chart

- Briefly describe what the flowchart shows, e.g.:
  “Input → Parse → Validate → Sort → Output”.

![project_flowchart](./sourcefile.png)

</details>

## Logs

<details>
<summary>Decisions/Bugs/Tests/Completed Files/AI Usage</summary>

# 🧾 Project Log

## 🧩 Decision Log

> Only log decisions that changed approach, data structures, or algorithms.
> Record only meaningful design or architectural decisions — anything that changed how the code works or why you chose one path over another.

### Parsing
| Date | Decision | Notes |
|------|-----------|-------|
| YYYY-MM-DD | Example: Switched from array to list | Array overflowed on large inputs; list slower but safe |
| YYYY-MM-DD | Example: Revisited array using memmove | Works fine; might revert later if scaling issues appear |

### Sorting
| Date | Decision | Notes |
|------|-----------|-------|
| YYYY-MM-DD | Example: Cost-based rotation sort | Intuitive and efficient enough for small stacks |
| YYYY-MM-DD | Example: Push stack_b in order | Slower, but simplest working version |

### Data Structures
| Date | Decision | Notes |
|------|-----------|-------|
| YYYY-MM-DD | Added `index` to `t_stack` | Needed for head/tail tracking in circular stack |

### Operations
| Date | Decision | Notes |
|------|-----------|-------|
| YYYY-MM-DD | Split into three op funcs + controller | Easier to extend + fewer nested conditionals |

---

## 🐛 Fixed Bugs Log

> Each fix should mention the symptom and what was changed — small or large doesn’t matter. Optional “Root Cause” is useful for pattern tracking.

| Date | Symptom | Fix | Root Cause |
|------|----------|-----|-------------|
| YYYY-MM-DD | Example: Invalid read with spaces | Added `isspace((unsigned char)*str)` check | Input pointer skipped space incorrectly |
| YYYY-MM-DD | Example: int overflow ignored | Switched from `atoi` to `atol` | Conversion overflow |

---

## 🧪 Tests Log

> Only log test runs that revealed something new (a bug, performance change, or coverage gap).
> Record test runs and coverage. Focus on what passed, what failed, and what changed — commands can go in a note or fenced code block below.

### Test Summary
| Name | Scope | Result | Notes |
|------|--------|--------|-------|
| Parser | Parsing | ✅ Basic, ⚠️ Spaced strings | Fixed after trimming inputs |
| Validator | Validation | ✅ Edge cases & limits | Handles duplicates and INT_MAX |
| Operator | Stack Ops | ⚠️ Rotate bug | Wrong byte count to memmove |

### Test Commands
```bash
# Example usage
make ftest && ./a.out "$(cat tests/big.txt)"
cc validator.c utils.c -o validator && ./validator
```

### Completed Files

> “Completed” = compiles, tested minimally, and you’re okay with the current design.

| Name | Date | Comments |
|------|------|-------|
||||

### AI Usage


> Only log when AI meaningfully influenced a decision, design, or bug fix.

| Date | How used | Ex.Q |
|------|------|-------|
||||
</details>

## Start: Checklist
<details>
<summary>Proof-checking Manual</summary>

### Mandates from [en.subject.pdf](https://cdn.intra.42.fr/pdf/pdf/200764/en.subject.pdf)

#### Musts

Common Requirements
- [ ] Your project must be written in Python 3.10 or later.
- [ ] Your project must adhere to the flake8 coding standard.
- [ ] If your program crashes due to unhandled
exceptions during the review, it will be considered non-functional.
- [ ] All resources (e.g., file handles, network connections) must be properly managed to
prevent leaks. Use context managers where possible for automatic handling.
- [ ] Your code must include type hints for function parameters, return types, and variables where applicable (using the typing module). Use mypy for static type checking. All functions must pass mypy without errors.
- [ ] Include docstrings in functions and classes following PEP 257 (e.g., Google or NumPy style) to document purpose, parameters, and returns.

Makefile Requirements
>Include a Makefile in your project to automate common tasks. It must contain the
following rules (mandatory lint implies the specified flags; it is strongly recommended to
try –strict for enhanced checking):
- [ ] `install`: Install project dependencies using `pip`, `uv`, `pipx`, or any other package manager of your choice.
- [ ] `run`: Execute the main script of your project (e.g., via Python interpreter).
- [ ] `debug`: Run the main script in debug mode using Python’s built-in debugger (e.g.,
pdb)
- [ ] `clean`: Remove temporary files or caches (e.g., `__pycache__`, `.mypy_cache`) to
keep the project environment clean.
- [ ] `lint`: Execute the commands `flake8 .` and `mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs`
- [ ] `lint-strict` (optional): Execute the commands `flake8 .` and `mypy . --strict`

Project Requirements
- [ ] Your program must be run with the following command:<br>
`python3 a_maze_ing.py config.txt`
- [ ] `a_maze_ing.py` is your main program file. You must use this name.
- [ ] `config.txt` is the only argument. It is a plain text file that defines the maze generation options. You can use a different filename.
- [ ] Your program must handle all errors gracefully: invalid configuration, file not found, bad
syntax, impossible maze parameters, etc. It must never crash unexpectedly, and must
always provide a clear error message to the user.

Configuration File Format
- [ ] The configuration file must contain one ‘KEY=VALUE‘ pair per line.
- [ ] Lines starting with # are comments and must be ignored.
- [ ] The following keys are mandatory:<br>

Key | Description | Example
----|-------------|--------
WIDTH | Maze width (number of cells) | WIDTH=20
HEIGHT | Maze height | HEIGHT=15
ENTRY | Entry coordinates (x,y) | ENTRY=0,0
EXIT | Exit coordinates (x,y) | EXIT=19,14
OUTPUT_FILE | Output filename | OUTPUT_FILE=maze.txt
PERFECT | Is the maze perfect? | PERFECT=True

- [ ] A default configuration file must be available in your Git repository.

Maze Requirements
- [ ] The maze must be randomly generated, but reproducibility via a seed is required.
- [ ] Each cell of the maze has between 0 and 4 walls, at each cardinal point (North,
Est, South, West).
- [ ] The maze must be valid
  - Entry and exit exist and are different, inside the maze bounds.
  - The structure ensures full connectivity and no isolated cells (except the ’42’
pattern, see below).
  -  As entry and exist are specific cells, there must be walls at the external borders.
  -   Your generated data must be coherent: each neighbouring cell must have the
same wall if any. E.g., it is forbidden to have a first cell with a wall on the
east side, and the second cell behind that wall without a wall on the west side.
- [ ] The maze can’t have large open areas. Corridors can’t be wider than 2 cells.
For example, you can have 2x3 or 3x2 open area, but never a 3x3 open area.
- [ ] When visually represented (see below), the maze must contain a visible “42” drawn
by several fully closed cells.
  - The “42” pattern may be omitted in case the maze size does not allow
it (i.e. too small). Print an error message on the console in that
case.
- [ ] If the PERFECT flag is activated, the maze must contain exactly one path between
the entry and the exit (i.e., it must be a perfect maze).

Output File Format
- [ ] The maze must be written in the output file using one hexadecimal digit per cell, where each digit encodes which walls are closed:
  - A wall being closed sets the bit to 1, open means 0.
Example: 3 (binary 0011) means walls are open to the south and west. Or A
(binary 1010) means that east and west walls are closed.
  - Cells are stored row by row, one row per line
  - After an empty line, the following 3 elements are inserted in the output file on 3
lines:
    - the entry coordinates, the exit coordinates, and the shortest valid path from
entry to exit, using the four letters N , E , S , W .
   - All lines end with a \n .

Visual Requirements
- [ ] Provide a way to display the maze visually using terminal ASCII rendering, or a graphical display using the MiniLibX (MLX) library.
- [ ] The visual should clearly show walls, entry, exit, and the solution path.
- [ ] User interactions must be available, at least for the following tasks:
  - Re-generate a new maze and display it.
  - Show/Hide a valid shortest path from the entrance to the exit.
  - Change maze wall colours.
  - Optional: set specific colours to display the “42” pattern.

Code Reuseablity Req
- [ ] You must implement the maze generation as a unique class (e.g., ‘MazeGenerator‘) inside
a standalone module that can be imported in a future project.
- [ ] You must provide a short documentation describing how to:
  - Instantiate and use your generator, with at least a basic example.
  - Pass custom parameters (e.g., size, seed).
  - Access the generated structure, and access at least a solution.
- [ ] This entire reusable module (code and documentation) must be available in a single file
suitable for a later installation by pip.
- [ ] This package must be called mazegen-* and the file must be located at the root of your
git repository.
- [ ] Both .tar.gz and .whl extensions are allowed, as generated by the standard build of a
Python package. *(Example of a full filename: mazegen-1.0.0-py3-none-any.whl)*
- [ ] You must provide in you Git repository all needed elements to build the package. This
will be asked during the evaluation: in a virtualenv or equivalent, install the needed tools
and build your package again from your sources.

Readme instructions
- [ ] A README.md file must be provided at the root of your Git repository.
- [ ] The README.md must include at least:
   - [ ] The very first line must be italicized and read: This project has been created as part
of the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].
   - [ ] A “Description” section that clearly presents the project, including its goal and a
brief overview.
   - [ ] An “Instructions” section containing any relevant information about compilation,
installation, and/or execution.
   - [ ] A “Resources” section listing classic references related to the topic (documentation, articles, tutorials, etc.), as well as a description of how AI was used — specifying for which tasks and which parts of the project.
   - [ ] Additional sections required by the project:
     - [ ] The complete structure and format of your config file.
     - [ ] The maze generation algorithm you chose.
     - [ ] Why you chose this algorithm.
     - [ ] What part of your code is reusable, and how.
     - [ ] Your team and project management with:
       -  The roles of each team member.
       -  Your anticipated planning and how it evolved until the end
       -  What worked well and what could be improved
       -  Have you used any specific tools? Which ones?
- [ ] If you implement advanced features (multiple algorithms, display options), describe them
in this README.md file.

#### Recommended

- [ ] Create test programs to verify project functionality (not submitted or graded). Use
frameworks like "pytest" or "unittest" for unit tests, covering edge cases.
- [ ] Include a `.gitignore` file to exclude Python artifacts.
- [ ] It is recommended to use virtual environments (e.g., venv or conda) for dependency
isolation during development.
</details>

## Finish: Review Prep Checklist

<details>
<summary>Checklist</summary>

- [ ]  Explain the strengths of your project (what you’d brag about)
	- P
	- P
	- P
- [ ]  Explain the weaknesses of your project
	- P
- [ ]  Predict questions you might get (2-3 + your answer to each)
	- P
	- P
	- P
- [ ] Performance Results

		P
		P

		P
		P
</details>

## Post-Mortem

<details>
<summary>Ending thoughts</summary>

- Wrong assumption
  -
  -
  -
- Biggest Win
  -
  -
  -
</details>
