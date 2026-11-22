"""Tests for bfs.py. Run from the project folder:
    python -m unittest discover -s tests -p "test_bfs.py" -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from bfs import (OPEN, MOUSE, CHEESE, WALL, find_cell, get_neighbors,
                 find_shortest_path, reconstruct_path, solve)


def make_grid(mouse=None, cheese=None, walls=()):
    grid = [[OPEN] * 16 for _ in range(16)]
    for r, c in walls:
        grid[r][c] = WALL
    if mouse:
        grid[mouse[0]][mouse[1]] = MOUSE
    if cheese:
        grid[cheese[0]][cheese[1]] = CHEESE
    return grid


class AcceptanceTests(unittest.TestCase):
    def test_empty_board_30_moves(self):
        moves, path, _ = solve(make_grid((0, 0), (15, 15)))
        self.assertEqual(moves, 30)
        self.assertEqual(len(path), 31)

    def test_same_row_5_moves(self):
        self.assertEqual(solve(make_grid((0, 0), (0, 5)))[0], 5)

    def test_unreachable(self):
        moves, path, _ = solve(make_grid((0, 0), (15, 15), walls=[(0, 1), (1, 0)]))
        self.assertIsNone(moves)
        self.assertEqual(path, [])


class NormalBoundaryTests(unittest.TestCase):
    def test_goes_around_wall(self):
        walls = [(r, 2) for r in range(15)]          # gap only at row 15
        self.assertEqual(solve(make_grid((0, 0), (0, 4), walls))[0], 34)

    def test_corner_to_corner_reverse(self):
        self.assertEqual(solve(make_grid((15, 15), (0, 0)))[0], 30)

    def test_adjacent_is_one_move(self):
        self.assertEqual(solve(make_grid((4, 4), (4, 5)))[0], 1)

    def test_corner_neighbors(self):
        self.assertEqual(sorted(get_neighbors(make_grid(), (0, 0))), [(0, 1), (1, 0)])

    def test_route_steps_are_single_moves_and_avoid_walls(self):
        walls = [(1, c) for c in range(1, 16)] + [(3, c) for c in range(0, 15)]
        grid = make_grid((0, 0), (4, 15), walls)
        moves, path, _ = solve(grid)
        self.assertIsNotNone(moves)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (4, 15))
        for (r1, c1), (r2, c2) in zip(path, path[1:]):
            self.assertEqual(abs(r1 - r2) + abs(c1 - c2), 1)
        for r, c in path:
            self.assertNotEqual(grid[r][c], WALL)

    def test_input_grid_is_not_changed(self):
        grid = make_grid((0, 0), (3, 3))
        before = [row[:] for row in grid]
        solve(grid)
        self.assertEqual(grid, before)


class InvalidInputTests(unittest.TestCase):
    def test_no_mouse_or_cheese_does_not_crash(self):
        self.assertIsNone(solve(make_grid())[0])
        self.assertIsNone(solve(make_grid(mouse=(0, 0)))[0])
        self.assertIsNone(solve(make_grid(cheese=(0, 0)))[0])

    def test_start_outside_grid(self):
        _, _, found = find_shortest_path(make_grid(), (-1, 0), (5, 5))
        self.assertFalse(found)

    def test_blocked_start(self):
        grid = make_grid(walls=[(0, 0)])
        _, _, found = find_shortest_path(grid, (0, 0), (5, 5))
        self.assertFalse(found)

    def test_reconstruct_unreached(self):
        self.assertEqual(reconstruct_path({(0, 0): None}, (9, 9)), [])

    def test_find_cell(self):
        self.assertEqual(find_cell(make_grid((2, 3), (4, 5)), MOUSE), (2, 3))
        self.assertIsNone(find_cell(make_grid(), CHEESE))


if __name__ == "__main__":
    unittest.main()
