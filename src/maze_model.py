
def create_grid():
    #fixed 16 by 16 empty grid
    rows, cols = 16,16
    return [[0 for _ in range(cols)] for _ in range(rows)]



def place_mouse(grid, position):
    x, y = position
    grid[x][y] = 1  # Mark the mouse's position with a 1
    return grid



def place_cheese(grid, cheese_position):
    x, y = cheese_position
    grid[x][y] = 2  # Mark the cheese's position with a 2
    return grid

def reset_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = 0  # Reset all cells to 0
    return grid

