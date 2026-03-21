import random
from parse_config import MazeConfig

NORTH = 0b0001  # 1
EAST = 0b0010  # 2
SOUTH = 0b0100  # 4
WEST = 0b1000  # 8

DIRECTION = [
    (0, -1, NORTH, SOUTH),  # 北
    (+1, 0, EAST, WEST),  # 東
    (0, +1, SOUTH, NORTH),  # 南
    (-1, 0, WEST, EAST)  # 西
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
        self.seed = config.seed

    def generate(self, x: int, y: int) -> None:
        self.visited[y][x] = True
        directions = DIRECTION.copy()
        random.shuffle(directions)
        for dx, dy, cur_wall, next_wall in directions:
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


def print_maze(maze: list[list[int]], width: int, height: int) -> None:
    for y in range(height):
        row = ""
        for x in range(width):
            row += f"{maze[y][x]:X}"
        print(row)
