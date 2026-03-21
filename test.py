import random
import parse_config
from maze_generator import MazeManager, print_maze
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt", file=sys.stderr)
        sys.exit(1)

    config = parse_config.parse_config(sys.argv[1])
    if not config.seed:
        random.seed(config.seed)

    gen = MazeManager(config)
    if not gen.ft_logo():
        print("Warninng: 42 pattern could not be placed\n")
    gen.generate(config.entry[0], config.entry[1])
    print_maze(gen.maze, gen.width, gen.height)

    while True:
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        try:
            choice = int(input("Choice? (1-4): "))
            match choice:
                case 1:
                    #regenerate a new maze
                    gen.reset()
                    if not gen.ft_logo():
                        print("can't make 42 logo\n")
                    gen.generate(config.entry[0], config.entry[1])
                    print_maze(gen.maze, gen.width, gen.height)
                case 2:
                    #show/hide path from entry to exit最短経路
                    pass
                case 3:
                    #rotate maze colors色変更
                    pass
                case 4:
                    sys.exit(0)
                case _:
                    print("undefined option.")
        except ValueError:
            print("Please enter a number.")
            continue


if __name__ == "__main__":
    main()
