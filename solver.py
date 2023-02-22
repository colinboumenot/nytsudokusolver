from copy import deepcopy
from datetime import datetime
from typing import List
import math


class Solver:

    def __init__(self):
        self.length = 9
        self.options = [1,2,3,4,5,6,7,8,9]
        self.box_size = int(math.sqrt(self.length))


    def solve(self, puzzle):
        return_puzzle = puzzle

        def solve_recursive(grid, row, col):

            if (row == self.length - 1 and col == self.length):
                return True
            if (col == self.length):
                row += 1
                col = 0
            if (grid[row][col] != 0):
                return solve_recursive(grid, row, col + 1)
            for x in range(self.length):
                if self.is_valid(grid, row, col, self.options[x]):
                    grid[row][col] = self.options[x]
                    if solve_recursive(grid, row, col + 1):
                        return True
                grid[row][col] = 0
            return False

        if (solve_recursive(return_puzzle, 0,0)):
            return puzzle
        else:
            return None

    def is_valid(self, grid, row, col, number_in_use):
        for x in range(self.length):
            if grid[row][x] == number_in_use:
                return False
        for x in range(self.length):
            if grid[x][col] == number_in_use:
                return False

        current_row = row - row % self.box_size
        current_col = col - col % self.box_size

        for x in range(self.box_size):
            for y in range(self.box_size):
                if grid[x + current_row][y + current_col] == number_in_use:
                    return False
        return True


