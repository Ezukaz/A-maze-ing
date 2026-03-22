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
    gen.create(config.entry[0], config.entry[1])
    gen.hex_maze()
    while True:
        print("\n=== A-Maze-ing ===")
        print("1. Re-gnerate a new maze")
        print("2. Show/Hide path form entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        try:
            option = int(input("Choice? (1 - 4): "))
            match option:
                case 1:
                    gen.create(config.entry[0], config.entry[1])
                    pass
                case 2:
                    # show hide
                    pass
                case 3:
                    # rotate colors
                    pass
                case 4:
                    sys.exit(0)
                case _:
                    print("please enter option.(1 - 4)")
        except ValueError:
            print("please enter option.(1 - 5)")
            continue
