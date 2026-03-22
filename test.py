import random
import parse_config
from maze_generator import MazeManager, NORTH, EAST, SOUTH, WEST, print_maze
import sys


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("No params", file=sys.stderr)
        exit()
    config = parse_config.parse_config(sys.argv[1])
    random.seed(config.seed)
    gen = MazeManager(config)
    gen.generate(config.entry[0], config.entry[1])
    print_maze(gen.maze, gen.width, gen.height)

    path = solve_maze(gen.maze, config.width, config.height, config.entry, config.exit)
    print(path)
    print_visual_maze(gen.maze, config.width, config.height, path, config.entry)