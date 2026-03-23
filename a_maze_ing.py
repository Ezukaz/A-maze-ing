from MazeConfig import parse_config
from MazeManager import MazeManager
import sys
WALL = "\033[37m"  # white

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No params", file=sys.stderr)
        exit()
    config = parse_config(sys.argv[1])
    gen = MazeManager(config)
    path = gen.generate()
    gen.print_maze()
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
                    for i, s in enumerate(gen.seed_history, 1):
                        print(f"{i}. {s}")
                    try:
                        seed = input("Choice? (or new?): ")
                        if seed == "":
                            seed = None
                        else:
                            seed = int(seed)
                        path = gen.generate(seed)
                        gen.print_maze()
                    except ValueError:
                        print("cannot regenerate a new maze.\n"
                              "enter integer seed or nothing.\n")
                case 2:
                    if hide is False:
                        gen.print_maze(path)
                        hide = True
                    else:
                        gen.print_maze()
                        hide = False
                    pass
                case 3:
                    # gen.rotate_color()
                    gen.print_maze()
                    pass
                case 4:
                    sys.exit(0)
                case _:
                    print("please enter option.(1 - 4)")
        except ValueError:
            print("please enter option.(1 - 4)")
            continue
