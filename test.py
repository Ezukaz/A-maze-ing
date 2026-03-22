import random
from parse_config import MazeConfig
import parse_config
from maze_generator import MazeManager
import sys


def regenerate(config: MazeConfig, seed: int) -> tuple[MazeManager, str]:
    random.seed(seed)
    gen = MazeManager(config)
    gen.generate(config.entry[0], config.entry[1])
    path = gen.find_path()
    gen.print_maze()
    return gen, path


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("No params", file=sys.stderr)
        exit()
    config = parse_config.parse_config(sys.argv[1])
    gen, path = regenerate(config, config.seed)
    hide = False
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
                    gen, path = regenerate(config, random.randint(1, 99999))
                case 2:
                    if hide is True:
                        gen.print_maze()
                        hide = False
                    else:
                        gen.print_maze(path)
                        hide = True
                    pass
                case 3:
                    # rotate colors
                    pass
                case 4:
                    sys.exit(0)
                case 5:
                    seed_inp = int(input(
                        "Please input seed or 0 for random: "
                    ))
                    seed = (
                        random.randint(1, 99999) if seed_inp == 0 else seed_inp
                    )
                    gen, path = regenerate(config, config.seed)
                case _:
                    print("please enter option.(1 - 5)")
        except ValueError:
            print("please enter option.(1 - 5)")
            continue
