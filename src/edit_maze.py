import random

GRID_SIZE = 16

EMPTY = 0
MOUSE = 1
CHEESE = 2
OBSTACLE = 3


def add_obstacle(obstacles, cell, mouse, cheese):
    row, col = cell

    if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
        return False

    if cell == mouse or cell == cheese:
        return False

    obstacles.add(cell)
    return True


def remove_obstacle(obstacles, cell):
    if cell in obstacles:
        obstacles.remove(cell)
        return True
    return False


def randomize_maze(obstacles, mouse, cheese):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if random.random() < 0.25:
                add_obstacle(obstacles, (row, col), mouse, cheese)
    return True


def clear_maze(obstacles):
    obstacles.clear()
    return True


def regenerate_maze(obstacles, mouse, cheese):
    clear_maze(obstacles)
    randomize_maze(obstacles, mouse, cheese)
    return True


# Testing
# if name == "main":
#     mouse = (0, 0)
#     cheese = (15, 15)
#     obstacles = set()

#     print("Add obstacle:", add_obstacle(obstacles, (2, 3), mouse, cheese))
#     print("Obstacles:", obstacles)

#     print("Try blocking mouse:", add_obstacle(obstacles, mouse, mouse, cheese))
#     print("Try blocking cheese:", add_obstacle(obstacles, cheese, mouse, cheese))

#     print("Remove obstacle:", remove_obstacle(obstacles, (2, 3)))
#     print("Obstacles:", obstacles)

#     add_obstacle(obstacles, (4, 5), mouse, cheese)
#     add_obstacle(obstacles, (6, 7), mouse, cheese)

#     print("Before clearing:", obstacles)
#     print("Clear maze:", clear_maze(obstacles))
#     print("After clearing:", obstacles)

#     print("Randomize maze:", randomize_maze(obstacles, mouse, cheese))
#     print("Walls after randomize:", len(obstacles))

#     print("Regenerate maze:", regenerate_maze(obstacles, mouse, cheese))
#     print("Walls after regenerate:", len(obstacles))