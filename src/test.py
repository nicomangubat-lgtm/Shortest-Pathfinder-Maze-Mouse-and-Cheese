import bfs
import edit_maze

passed = 0
failed = 0


def make_grid(mouse, cheese, walls=[]):
    # makes an empty 16 x 16 grid, then adds walls, mouse and cheese
    grid = []
    for row in range(16):
        grid.append([0] * 16)
    for (r, c) in walls:
        grid[r][c] = 3
    if mouse is not None:
        grid[mouse[0]][mouse[1]] = 1
    if cheese is not None:
        grid[cheese[0]][cheese[1]] = 2
    return grid


def check(name, expected, actual):
    # compares the expected answer with the actual answer and prints one line
    global passed, failed
    if expected == actual:
        print("PASS  " + name + "  (expected " + str(expected) + ", got " + str(actual) + ")")
        passed = passed + 1
    else:
        print("FAIL  " + name + "  (expected " + str(expected) + ", got " + str(actual) + ")")
        failed = failed + 1


#  NORMAL TESTS 
print("NORMAL TESTS")

grid = make_grid((0, 0), (0, 5))
steps, path, visited = bfs.solve(grid)
check("Test 1: same row", 5, steps)

grid = make_grid((0, 0), (15, 15))
steps, path, visited = bfs.solve(grid)
check("Test 2: opposite corners", 30, steps)

grid = make_grid((0, 0), (0, 2), [(0, 1)])
steps, path, visited = bfs.solve(grid)
check("Test 3: wall in the way", 4, steps)
right_path = [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)]
check("Test 3b: path goes around the wall", True, path == right_path)

#  BOUNDARY TESTS 
print()
print("BOUNDARY TESTS")

grid = make_grid((4, 4), (4, 5))
steps, path, visited = bfs.solve(grid)
check("Test 4: cheese next to mouse", 1, steps)

grid = make_grid((15, 15), (0, 0))
steps, path, visited = bfs.solve(grid)
check("Test 5: corners, reverse", 30, steps)

grid = make_grid((0, 0), (15, 15), [(0, 1), (1, 0)])
steps, path, visited = bfs.solve(grid)
check("Test 6: mouse trapped", None, steps)

grid = make_grid((0, 0), (15, 15), [(14, 15), (15, 14)])
steps, path, visited = bfs.solve(grid)
check("Test 7: cheese trapped", None, steps)

#  INVALID INPUT TESTS 
print()
print("INVALID INPUT TESTS")

grid = make_grid(None, None)
steps, path, visited = bfs.solve(grid)
check("Test 8: no mouse, no cheese", None, steps)

obstacles = set()
mouse = (0, 0)
cheese = (15, 15)

check("Test 9: obstacle on mouse", False,
      edit_maze.add_obstacle(obstacles, (0, 0), mouse, cheese))

check("Test 10: obstacle on cheese", False,
      edit_maze.add_obstacle(obstacles, (15, 15), mouse, cheese))

check("Test 11: obstacle at row 16", False,
      edit_maze.add_obstacle(obstacles, (16, 3), mouse, cheese))

check("Test 12: obstacle at row -1", False,
      edit_maze.add_obstacle(obstacles, (-1, 3), mouse, cheese))

check("Test 13: remove missing obstacle", False,
      edit_maze.remove_obstacle(obstacles, (7, 7)))

#  RESULT 
print()
print("--------------")
print("Passed:", passed, "| Failed:", failed)
if failed == 0:
    print("All tests passed!")
else:
    print("Some tests failed. Check the FAIL lines above.")
