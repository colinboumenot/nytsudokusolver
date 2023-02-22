from copy import deepcopy
from datetime import datetime
from typing import List
import math
import random

class PuzzleCreator:

    def __init__(self, difficulty:int,given_length = 9):
        self.length = given_length
        self.options = [1,2,3,4,5,6,7,8,9]
        self.box_size = int(math.sqrt(self.length))
        self.puzzle = [[0] * self.length for x in range(self.length)]

        if difficulty == 1:
            self.filled_in = given_length * 4 + random.randint(-2,2)
        if difficulty == 2:
            self.filled_in = given_length * 3 + random.randint(-2,2)
        else:
            self.filled_in = given_length * 3 + random.randint(-6,-4)

    def generate_puzzle(self):

        def generate_puzzle_recursive(grid, nums_left):
            if (nums_left == 0):
                return grid
            else:
                new_col = random.randint(0, self.length - 1)
                new_row = random.randint(0, self.length - 1)

                if grid[new_row][new_col] != 0:
                    generate_puzzle_recursive(grid, nums_left)
                else:
                    new_int = random.choice(self.options)
                    if self.is_valid(grid, new_row, new_col, new_int):
                        grid[new_row][new_col] = new_int
                        generate_puzzle_recursive(grid, nums_left - 1)
                    else:
                        generate_puzzle_recursive(grid, nums_left)
        return generate_puzzle_recursive(self.puzzle, self.filled_in)

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

    def print_puzzle(self) -> None:
        for i in range(9):
            for j in range (9):
                print(self.puzzle[i][j], end = " ")
            print()

p = PuzzleCreator(1,9)
p.generate_puzzle()
p.print_puzzle()













