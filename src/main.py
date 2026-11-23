import maze_model
import edit_maze
import bfs
# import blind_exploration

SIZE = 16


def ask_position(name):
    # keeps asking until the person types a number from 0 to 15 for both row and column
    while True:
        print(name + " position:")
        row = input("Enter row (0-15): ")
        col = input("Enter column (0-15): ")
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            if 0 <= row < SIZE and 0 <= col < SIZE:
                return (row, col)
        print("Please type numbers from 0 to 15.")
        print()


def make_grid(obstacles, mouse, cheese):
    # builds the number grid (0 empty, 1 mouse, 2 cheese, 3 wall) for bfs and blind exploration
    grid = maze_model.create_grid()
    for row, col in obstacles:
        grid[row][col] = bfs.WALL
    grid = maze_model.place_mouse(grid, mouse)
    grid = maze_model.place_cheese(grid, cheese)
    return grid


def draw_maze(obstacles, mouse, cheese, scanned=None):
    # M = mouse, C = cheese, | = wall, space = empty, ~ = scanned cell
    # the # line around the maze is only the border so you can see its edges
    if scanned is None:
        scanned = []
    scanned = set(scanned)

    print("#" * (SIZE * 2 + 3))
    for row in range(SIZE):
        line = ""
        for col in range(SIZE):
            cell = (row, col)
            if cell == mouse:
                symbol = "M"
            elif cell == cheese:
                symbol = "C"
            elif cell in obstacles:
                symbol = "|"
            elif cell in scanned:
                symbol = "~"
            else:
                symbol = " "
            line = line + symbol + " "
        print("# " + line + "#")
    print("#" * (SIZE * 2 + 3))


def show_menu():
    print()
    print("1. Regenerate maze")
    print("2. Clear maze")
    print("3. Run BFS (shortest path)")
    print("4. Blind exploration")
    print("5. Quit")


# ---------------- program starts here ----------------

print("MOUSE AND CHEESE MAZE")
print()

mouse = ask_position("Mouse")
cheese = ask_position("Cheese")
while cheese == mouse:
    print("The cheese can't be on the mouse. Pick another place for the cheese.")
    cheese = ask_position("Cheese")

obstacles = set()
edit_maze.regenerate_maze(obstacles, mouse, cheese)  # start with a random maze

print()
draw_maze(obstacles, mouse, cheese)

running = True
while running:
    show_menu()
    choice = input("Choose a number: ")
    print()

    if choice == "1":
        edit_maze.regenerate_maze(obstacles, mouse, cheese)
        draw_maze(obstacles, mouse, cheese)

    elif choice == "2":
        edit_maze.clear_maze(obstacles)
        draw_maze(obstacles, mouse, cheese)

    elif choice == "3":
        grid = make_grid(obstacles, mouse, cheese)
        steps, path, visited_order = bfs.solve(grid)
        draw_maze(obstacles, mouse, cheese, visited_order)
        if steps is None:
            print("The cheese cannot be reached!")
        else:
            print("Shortest path found:", steps, "steps")
        print("Cells scanned:", len(visited_order))

    elif choice == "4":
        grid = make_grid(obstacles, mouse, cheese)
        moves, found = bfs.explore(grid)
        draw_maze(obstacles, mouse, cheese, moves)
        if found:
            print("The mouse found the cheese!")
        else:
            print("The mouse could not find the cheese.")
        print("Moves made:", len(moves) - 1)

    elif choice == "5":
        print("Bye!")
        running = False

    else:
        print("Please choose 1, 2, 3, 4 or 5.")
