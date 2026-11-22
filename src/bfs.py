"""
Steps:
  1. Put the mouse's cell in a waiting line (queue).
  2. Take the next cell. If it is the cheese, stop.
  3. Otherwise add each open, unvisited up/down/left/right neighbor to the
     line, mark it visited, and remember its parent.
  4. If the line runs out, the cheese cannot be reached.
  5. If found, follow the parent map back to the mouse and flip it.
"""

from collections import deque

OPEN = 0
MOUSE = 1
CHEESE = 2
WALL = 3   # AGREE THIS NUMBER WITH THE PERSON WRITING edit_maze.py

# row/column change for up, down, left, right (no diagonals)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def _inside(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def find_cell(grid, value):
    """Return (row, col) of the first cell equal to value, or None."""
    for r, line in enumerate(grid):
        for c, cell in enumerate(line):
            if cell == value:
                return (r, c)
    return None


def get_neighbors(grid, cell):
    """Return the up/down/left/right neighbors that are inside the grid and not walls."""
    row, col = cell
    neighbors = []
    for d_row, d_col in DIRECTIONS:
        n_row, n_col = row + d_row, col + d_col
        if _inside(grid, n_row, n_col) and grid[n_row][n_col] != WALL:
            neighbors.append((n_row, n_col))
    return neighbors


def find_shortest_path(grid, start, goal):
    """Run BFS from start to goal.
    """
    if start is None or goal is None:
        return [], {}, False
    for row, col in (start, goal):
        if not _inside(grid, row, col) or grid[row][col] == WALL:
            return [], {}, False

    queue = deque([start])
    visited = {start}
    parent = {start: None}
    visited_order = [start]

    while queue:                      # line empty -> cheese unreachable
        cell = queue.popleft()
        if cell == goal:              # cheese found
            return visited_order, parent, True
        for neighbor in get_neighbors(grid, cell):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = cell
                visited_order.append(neighbor)
                queue.append(neighbor)

    return visited_order, parent, False


def reconstruct_path(parent, goal):
    """Follow parents from the goal back to the start, then flip. [] if not reached."""
    if goal not in parent:
        return []
    path = []
    cell = goal
    while cell is not None:
        path.append(cell)
        cell = parent[cell]
    path.reverse()
    return path


def is_cheese_reachable(found):
    """Reports the 'found' result from find_shortest_path."""
    return bool(found)


def solve(grid):
    """Find the mouse and cheese in the grid and run the whole search.
    """
    start = find_cell(grid, MOUSE)
    goal = find_cell(grid, CHEESE)
    visited_order, parent, found = find_shortest_path(grid, start, goal)
    if is_cheese_reachable(found):
        path = reconstruct_path(parent, goal)
        return len(path) - 1, path, visited_order
    return None, [], visited_order
