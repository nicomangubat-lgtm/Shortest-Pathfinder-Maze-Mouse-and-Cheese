
def create_grid():
    #fixed 16 by 16 empty grid
    rows, cols = 16,16
    return [[0 for _ in range(cols)] for _ in range(rows)]

print("Mouse position: ") #testing purposes
position = (int(input("Enter x coordinate (0-15): ")), int(input("Enter y coordinate (0-15): "))) #testing purposes

def place_mouse(grid, position):
    x, y = position
    grid[x][y] = 1  # Mark the mouse's position with a 1
    return grid

print("Cheese position: ") #testing purposes
cheese_position = (int(input("Enter x coordinate (0-15): ")), int(input("Enter y coordinate (0-15): "))) #testing purposes

def place_cheese(grid, cheese_position):
    x, y = cheese_position
    grid[x][y] = 2  # Mark the cheese's position with a 2
    return grid

def reset_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = 0  # Reset all cells to 0
    return grid

print()
fixed_grid = create_grid() #empty grid created
mouse_grid = place_mouse(fixed_grid, position) #grid with mouse position marked
cheese_grid = place_cheese(mouse_grid, cheese_position)  # grid with mouse and cheese positions marked
for row in cheese_grid:
    print(row)

print()
print("Reset grid?") #resetting the grid to empty state(0s)  #testing purposes
if input("Enter 'y' to reset: ").lower() == 'y':  #testing purposes
    print("Resetting grid...")
    reset_grid(fixed_grid)
    for row in fixed_grid:
        print(row)
