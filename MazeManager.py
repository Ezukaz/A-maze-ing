import random
from MazeConfig import MazeConfig

NORTH = 0b0001  # 1
EAST = 0b0010  # 2
SOUTH = 0b0100  # 4
WEST = 0b1000  # 8

"""dx, dy, current_wall, neighbor_wall, output_letter"""
DIRECTION = [
    (0, -1, NORTH, SOUTH, 'N'),  # 北
    (+1, 0, EAST, WEST, 'E'),  # 東
    (0, +1, SOUTH, NORTH, 'S'),  # 西
    (-1, 0, WEST, EAST, 'W')  # 西
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

    @staticmethod
    def build(self, x: int, y: int) -> None:
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
                    self.build(nx, ny)
        return None

    @staticmethod
    def ft_logo(self) -> None:
        if self.width <= WIDTH_FT or self.height <= HEIGHT_FT:
            print("***too small to make '42' pattern.")
            return None

        ft_x = self.width // 2 - WIDTH_FT // 2
        ft_y = self.height // 2 - HEIGHT_FT // 2

        pattern_cells = set()
        for fy in range(HEIGHT_FT):
            for fx in range(WIDTH_FT):
                if PATTERN_FT[fy][fx]:
                    pattern_cells.add((ft_x + fx, ft_y + fy))
        if self.entry in pattern_cells or self.exit in pattern_cells:
            # entryまたはexitの座標が被っていたので、被っている座標をランダムに移動、またその旨のメッセージを出力
            pass

        for fy in range(HEIGHT_FT):
            for fx in range(WIDTH_FT):
                if PATTERN_FT[fy][fx]:
                    self.visited[ft_y + fy][ft_x + fx] = True

    def generate(self, seed: int = random.randint()) -> None:
        random.seed(seed)
        self.ft_logo()
        if self.perfect is True:
            # 完全迷路の作成
            return None
        self.build(*self.entry)
        path = self.find_path()
        self.print_maze()

        with open(self.output_file, "w") as f:
            for y in range(self.height):
                row = ""
                for x in range(self.width):
                    row += hex(self.maze[y][x]).strip("0x").upper()
                f.write(row)
            f.write("\n")
            f.write(self.entry)
            f.write(self.exit)
            f.write(path)

    def find_path(self) -> str:
        queue = []
        queue.append((self.entry, ""))
        visited = {self.entry}
        while queue:
            (x, y), path = queue.pop(0)
            if (x, y) == self.exit:
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

    def print_maze(self, path: str = None) -> None:
        path_cells = set()
        if path and self.entry:
            x, y = self.entry
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
