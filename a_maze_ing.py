import random
from MazeConfig import MazeConfig, parse_config
from MazeManager import MazeManager
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
    config = parse_config(sys.argv[1])
    gen, path = regenerate(config, config.seed)
    history = {config.seed}
    hide = False
    while True:
        print("\n=== A-Maze-ing ===")
        print("1. Re-gnerate a new maze")
        print("2. Show/Hide path form entry to exit")
        print("3. Rotate maze colors")
        print("4. Remake seed map")
        print("5. Quit")
        try:
            option = int(input("Choice? (1 - 4): "))
            match option:
                case 1:
                    for i, s in enumerate(history, 1):
                        print(f"{i}. {s}")
                    try:
                        seed = int(input("Choice? (or new?): "))
                        gen, path = gen.create(seed)
                        history.add(seed)
                    except ValueError:
                        print("cannot regenerate a new maze.\n"
                              "enter integer seed or nothing.\n")
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
                case _:
                    print("please enter option.(1 - 4)")
        except ValueError:
            print("please enter option.(1 - 4)")
            continue
