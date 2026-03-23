import random
import sys
from collections import deque
from MazeConfig import MazeConfig

"""visualize constants"""
RESET = "\033[0m"
WALL = "\033[47m"  # white
PATH = "\033[44m"  # blue
ENTRY = "\033[42m"  # green
EXIT = "\033[41m"  # red
FT = "\033[46m"  # light blue
SPACE = "  "
BLOCK = "  "

COLORS = [
    "\033[47m",  # white
    "\033[43m",  # yellow
    "\033[42m",  # green
    "\033[41m",  # red
    "\033[44m",  # blue
    "\033[45m",  # purple
]



LETTER_TO_DIR = {
    'N': (0, -1),
    'E': (1,  0),
    'S': (0,  1),
    'W': (-1, 0)
}

"""maze constants"""
NORTH = 0b0001
EAST = 0b0010
SOUTH = 0b0100
WEST = 0b1000

"""dx, dy, current_wall, neighbor_wall, output_letter"""
DIRECTION = [
    (0, -1, NORTH, SOUTH, 'N'),
    (+1, 0, EAST, WEST, 'E'),
    (0, +1, SOUTH, NORTH, 'S'),
    (-1, 0, WEST, EAST, 'W')
]

"""42 pattern(7 x 5): True coordinate forbid to break walls"""
PATTERN_FT = [
    [True,  False, False, False, True,  True,  True],
    [True,  False, False, False, False, False, True],
    [True,  True,  True,  False, True,  True,  True],
    [False, False, True,  False, True,  False, False],
    [False, False, True,  False, True,  True,  True]
]
WIDTH_FT = 7
HEIGHT_FT = 5


class MazeManager:
    def __init__(self, config: MazeConfig) -> None:
        self.width = config.width
        self.height = config.height
        self.entry = config.entry
        self.exit = config.exit
        self.output_file = config.output_file
        self.perfect = config.perfect
        self.maze = [[0b1111] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]
        self.ft_cells = set()
        self.seed_history = []
        self.wall_color = WALL

    def reset(self) -> None:
        self.maze = [[0b1111] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]
        self.ft_cells = set()

    def make_maze(self, x: int, y: int) -> None:
        self.visited[y][x] = True
        directions = DIRECTION.copy()
        random.shuffle(directions)
        for dx, dy, cur_wall, next_wall, _ in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if self.visited[ny][nx] is True:
                    continue
                else:
                    self.maze[y][x] &= ~cur_wall
                    self.maze[ny][nx] &= ~next_wall
                    self.make_maze(nx, ny)
        return None

    def ft_logo(self) -> None:
        if self.width <= WIDTH_FT or self.height <= HEIGHT_FT:
            print("***too small to make '42' pattern.")
            return None

        """determine the coordinates of 42 pattern in this size"""
        ft_x = self.width // 2 - WIDTH_FT // 2
        ft_y = self.height // 2 - HEIGHT_FT // 2
        pattern_cells = set()
        for fy in range(HEIGHT_FT):
            for fx in range(WIDTH_FT):
                if PATTERN_FT[fy][fx]:
                    pattern_cells.add((ft_x + fx, ft_y + fy))

        """validate the entry/exit coordinates overlap"""
        if self.entry in pattern_cells or self.exit in pattern_cells:
            print("***'42' pattern overlaps with entry/exit. "
                  "Skipping pattern.")
            return None

        for fy in range(HEIGHT_FT):
            for fx in range(WIDTH_FT):
                if PATTERN_FT[fy][fx]:
                    self.visited[ft_y + fy][ft_x + fx] = True
                    self.ft_cells.add((ft_x + fx, ft_y + fy))

    def generate(self, seed: int | None = None) -> str | None:
        self.reset()
        """seed"""
        if seed is None:
            seed = random.randint(0, 2**32 - 1)
        else:
            try:
                random.seed(self.seed_history[seed - 1])
            except IndexError:
                print("enter a option for making seed or nothing",
                      file=sys.stderr)

        """42 pattern"""
        self.ft_logo()

        """make maze"""
        self.make_maze(*self.entry)
        if self.perfect is False:
            """make maze as imperfect maze"""
            breakable = []
            for y in range(1, self.height - 1):
                for x in range(1, self.width - 1):
                    """validate (x, y) is 42 logo
                        (only these blocks are 0b1111)"""
                    if (x, y) not in self.ft_cells:
                        breakable.append((x, y))
            for _ in range(random.randint(1, self.width*self.height // 10)):
                x, y = random.choice(breakable)
                for dx, dy, cur_wall, next_wall, _ in DIRECTION:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width
                        and 0 <= ny < self.height
                            and self.maze[y][x] & cur_wall):
                        self.maze[y][x] &= ~cur_wall
                        self.maze[ny][nx] &= ~next_wall
                        break

        self.seed_history.append(seed)

        """find the shortest path"""
        path = self.find_path()
        if path is None:
            print("Error: no path found.", file=sys.stderr)
            return None

        """write output file"""
        try:
            with open(self.output_file, "w") as f:
                for y in range(self.height):
                    row = ""
                    for x in range(self.width):
                        row += f"{self.maze[y][x]:X}"
                    f.write(row + "\n")
                f.write("\n")
                f.write(str(self.entry) + "\n")
                f.write(str(self.exit) + "\n")
                f.write(path + "\n")
        except Exception as e:
            print("\nError occured while writing in output file.\n"
                  f"Detail: {e}\n", file=sys.stderr)
        return path

    def find_path(self) -> str | None:
        """BFS, using queue"""
        queue = deque()
        queue.append((self.entry, ""))
        visited = {self.entry}
        while queue:
            (x, y), path = queue.popleft()
            """if success: """
            if (x, y) == self.exit:
                return path

            """search"""
            for dx, dy, wall_bit, _, letter in DIRECTION:
                if self.maze[y][x] & wall_bit:
                    continue
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.width
                        and 0 <= ny < self.height
                        and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + letter))
        """if failure: """
        return None

    @staticmethod
    def _get_path_cells(
            path: str,
            entry: tuple[int, int]
    ) -> set[tuple[int, int]]:
        path_cells = set()
        x, y = entry
        for letter in path:
            dx, dy = LETTER_TO_DIR[letter]
            x, y = x + dx, y + dy
            path_cells.add((x, y))
        return path_cells

    @staticmethod
    def _get_cell_color(
            x: int,
            y: int,
            entry: tuple[int, int],
            exit: tuple[int, int],
            ft_cells: set[tuple[int, int]],
            path_cells: set[tuple[int, int]]
    ) -> str:
        if (x, y) == entry:
            return ENTRY
        if (x, y) == exit:
            return EXIT
        if (x, y) in ft_cells:
            return FT
        if (x, y) in path_cells:
            return PATH
        return ""

    def print_maze(
            self,
            path: str | None = None,
    ) -> None:
        w = self.width * 2 + 1
        h = self.height * 2 + 1

        # 描画グリッドを壁で初期化
        draw = [[self.wall_color + BLOCK + RESET] * w for _ in range(h)]

        # 通路・セルの色を設定
        path_cells = self._get_path_cells(path, self.entry) if path else set()

        for y in range(self.height):
            for x in range(self.width):
                cx = x * 2 + 1  # セルの描画座標
                cy = y * 2 + 1

                # セルの中身
                cell_color = self._get_cell_color(
                    x, y, self.entry, self.exit, self.ft_cells, path_cells)
                draw[cy][cx] = cell_color + BLOCK + RESET

                # 北壁がなければ通路に
                if not (self.maze[y][x] & NORTH):
                    draw[cy - 1][cx] = RESET + BLOCK

                # 南壁がなければ通路に
                if not (self.maze[y][x] & SOUTH):
                    draw[cy + 1][cx] = RESET + BLOCK

                # 西壁がなければ通路に
                if not (self.maze[y][x] & WEST):
                    draw[cy][cx - 1] = RESET + BLOCK

                # 東壁がなければ通路に
                if not (self.maze[y][x] & EAST):
                    draw[cy][cx + 1] = RESET + BLOCK

        # 描画
        for row in draw:
            print("".join(row))

    def rotate_color(self) -> None:
        
