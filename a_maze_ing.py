from MazeConfig import parse_config
from MazeManager import MazeManager
import sys

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
        print()
        try:
            option = int(input("Choice? (1 - 4): "))
            match option:
                case 1:
                    print()
                    for i, s in enumerate(gen.seed_history):
                        print(f" {i + 1}. {s}")
                    try:
                        enter = input(" choose seed "
                                      f"{list(range(1, i + 2))}: ")
                        print()
                        if enter == "":
                            path = gen.generate()
                        else:
                            path = gen.generate(int(enter))
                        gen.print_maze()
                        hide = False
                    except ValueError:
                        print("\ncannot regenerate a new maze.\n"
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
                    gen.rotate_color()
                    gen.print_maze()
                    pass
                case 4:
                    sys.exit(0)
                case _:
                    print("please enter option.(1 - 4)")
                    print()
        except ValueError:
            print("please enter option.(1 - 4)")
            continue
