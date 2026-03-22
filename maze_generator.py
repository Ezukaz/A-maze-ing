import random
from collections import deque
from parse_config import MazeConfig

NORTH = 0b0001  # 1
EAST  = 0b0010  # 2
SOUTH = 0b0100  # 4
WEST  = 0b1000  # 8

# (dx, dy, current_wall, neighbor_wall, output_letter)
DIRECTION = [
    ( 0, -1, NORTH, SOUTH, 'N'), # 北
    (+1, 0, EAST, WEST, 'E'), # 東
    ( 0, +1, SOUTH, NORTH, 'S'), # 南
    (-1, 0, WEST, EAST, 'W') # 西
]


class MazeManager:
    def __init__(self, config: MazeConfig) -> None:
        self.width = config.width
        self.height = config.height
        self.maze = [[0b1111] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]

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


def print_maze(maze: list[list[int]], width: int, height: int) -> None:
    for y in range(height):
        row = ""
        for x in range(width):
            row += hex(maze[y][x]).strip("0x").upper()
        print(row)


def solve_maze(
        maze: list[list[int]],
        width: int, height: int,
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
        cell_walls = maze[y][x]
        for dx, dy, wall_bit, _, letter in DIRECTION:
            if cell_walls & wall_bit:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + letter))
    return None


def print_visual_maze(
        maze: list[list[int]],
        width: int, height: int,
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

    for y in range(height):
        top = ""
        for x in range(width):
            top += "+"
            top += "--" if maze[y][x] & NORTH else "  "
        top += "+"
        print(top)

        mid = ""
        for x in range(width):
            mid += "|" if maze[y][x] & WEST else " "
            mid += "**" if (x, y) in path_cells else "  "
        mid += "|" if maze[y][width - 1] & EAST else " "
        print(mid)

    bottom = ""
    for x in range(width):
        bottom += "+"
        bottom += "--" if maze[height - 1][x] & SOUTH else "  "
    bottom += "+"
    print(bottom)