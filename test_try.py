import random
import parse_config
from try_this import MazeManager
import sys


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("No params", file=sys.stderr)
        exit()
    config = parse_config.parse_config(sys.argv[1])
    random.seed(config.seed)
    gen = MazeManager(config)
    gen.generate(config.entry[0], config.entry[1])
    gen.hex_maze()

    path = gen.find_path(config.entry, config.exit)
    print(path)
    gen.print_maze(start=config.entry)
    print("⬜" * int(config.width * 1.5))
    gen.print_maze(path, config.entry)
