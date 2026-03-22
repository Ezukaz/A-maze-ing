import random
from collections import deque
from parse_config import MazeConfig
from typing import Optional

NORTH = 0b0001 # 1
EAST = 0b0010 # 2
SOUTH = 0b0100 # 4
WEST = 0b1000 # 8

# (dx, dy, current_wall, neighbor_wall, output_letter)
DIRECTION = [
    ( 0, -1, NORTH, SOUTH, 'N'), # 北
    (+1, 0, EAST, WEST, 'E'), # 東
    ( 0, +1, SOUTH, NORTH, 'S'), # 南
    (-1, 0, WEST, EAST, 'W') # 西
]

FT_PATTERN = [
    [True, False, False, False,  True, True, True],
    [True, False, False, False, False, False, True],

]

class MazeManager:
    def __init__(self, config: MazeConfig) -> None:
        self.width = config.width
        self.height = config.height
        self.maze = [[0b1111] * self.width for _ in range(self.height)]
        self.visited = [[False] * self.width for _ in range(self.height)]
        self.entry = config.entry
        self.exit = config.exit

    def generate(self, x: int, y: int) -> Optional[list[list[int]]]:
        visited = self.visited.copy()
        maze = self.maze.copy()
        visited[y][x] = True
        directions = DIRECTION.copy()
        random.shuffle(directions)
        for dx, dy, cur_wall, next_wall, _ in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if visited[ny][nx] is True:
                    continue
                else:
                    maze[y][x] &= ~cur_wall
                    maze[ny][nx] &= ~next_wall
                    self.generate(nx, ny)
        return maze
    
    def create(self) -> Optional[list[list[int]]]:
        self.generate(*self.entry)


def print_maze(maze: list[list[int]], width: int, height: int) -> None:
    for y in range(height):
        row = ""
        for x in range(width):
            row += hex(maze[y][x]).strip("0x").upper()
        print(row)
