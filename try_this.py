import random
from collections import deque
from parse_config import MazeConfig

NORTH = 0b0001  # 1
EAST = 0b0010  # 2
SOUTH = 0b0100  # 4
WEST = 0b1000  # 8

# (dx, dy, current_wall, neighbor_wall, output_letter)
DIRECTION = [
    (0, -1, NORTH, SOUTH, 'N'),  # 北
    (+1, 0, EAST, WEST, 'E'),  # 東
    (0, +1, SOUTH, NORTH, 'S'),  # 西
    (-1, 0, WEST, EAST, 'W')  # 西
]

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
        self.maze = [[0b1111] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]
        self.entry = config.entry
        self.exit = config.exit

    def generate(self, x: int, y: int) -> None:
        self.visited[y][x] = True
        directions = DIRECTION.copy()
        random.shuffle(directions)
        for dx, dy, cur_wall, next_wall, _ in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if self.visited[ny][nx] is True:
                    continue
                else:
                    self.maze[y][x] &= ~cur_wall
                    self.maze[ny][nx] &= ~next_wall
                    self.generate(nx, ny)
        return None

    def ft_logo(self) -> bool:
        if self.width <= WIDTH_FT or self.height <= HEIGHT_FT:
            return False

        ft_x = self.width // 2 - WIDTH_FT // 2
        ft_y = self.height // 2 - HEIGHT_FT // 2

        pattern_cells = set()
        for fy in range(HEIGHT_FT):
            for fx in range(WIDTH_FT):
                if PATTERN_FT[fy][fx]:
                    pattern_cells.add((ft_x + fx, ft_y + fy))

        if self.entry in pattern_cells or self.exit in pattern_cells:
            return False

        for fy in range(HEIGHT_FT):
            for fx in range(WIDTH_FT):
                if PATTERN_FT[fy][fx]:
                    self.visited[ft_y + fy][ft_x + fx] = True

        return True

    def reset(self) -> None:
        self.maze = [[0b1111] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]

    def create(self) -> None:
        self.reset()
        if not self.ft_logo():
            print("cannot make 42 logo.")
        self.generate(*self.entry)

    def hex_maze(self) -> None:
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += hex(self.maze[y][x]).strip("0x").upper()
            print(row)

    def find_path(
        self,
        start: tuple[int, int],
        goal: tuple[int, int]
            ) -> str:
        queue = deque()
        queue.append((start, ""))
        visited = {start}
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == goal:
                return path
            for dx, dy, wall_bit, _, letter in DIRECTION:
                if self.maze[y][x] & wall_bit:
                    continue
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.width
                        and 0 <= ny < self.height
                        and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + letter))
        return None

    def print_maze(
        self,
        path: str = None,
        start: tuple[int, int] = None
    ) -> None:
        path_cells = set()
        if path and start:
            x, y = start
            path_cells.add((x, y))
            for ch in path:
                for dx, dy, _, _, letter in DIRECTION:
                    if ch == letter:
                        x, y = x + dx, y + dy
                        path_cells.add((x, y))
                        break

        for y in range(self.height):
            top = ""
            for x in range(self.width):
                top += "+"
                top += "--" if self.maze[y][x] & NORTH else "  "
            top += "+"
            print(top)

            mid = ""
            for x in range(self.width):
                mid += "|" if self.maze[y][x] & WEST else " "
                mid += "**" if (x, y) in path_cells else "  "
            mid += "|" if self.maze[y][self.width - 1] & EAST else " "
            print(mid)

        bottom = ""
        for x in range(self.width):
            bottom += "+"
            bottom += "--" if self.maze[self.height - 1][x] & SOUTH else "  "
        bottom += "+"
        print(bottom)
