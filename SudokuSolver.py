"""
SudokuGrid Class
================

This class represents a Sudoku puzzle solver using backtracking.

Attributes:
    x (int): The current x-coordinate during Sudoku solving.
    y (int): The current y-coordinate during Sudoku solving.
    n (int): The current number being inserted into the Sudoku grid.
    Grid (numpy.ndarray): A 9x9 NumPy array representing the Sudoku grid.

Methods:
    __init__(self): Constructor method to initialize the SudokuGrid object.
    insert(self, x, y, n): Inserts a number 'n' at position (x, y) in the Sudoku grid.
    validate(self, x, y, n): Validates if inserting 'n' at position (x, y) is valid according to Sudoku rules.
    matrixValidate(self): Validates the entire Sudoku grid.
    solve(self, x, y): Solves the Sudoku puzzle using backtracking and recursion.

Example Usage:
    game1 = SudokuGrid()
    game1.solve(0, 0)
    print(game1.Grid)

"""

import numpy as np

class SudokuGrid:
    def __init__(self):
        """
        Constructor for SudokuGrid.

        Initializes the Sudoku grid with a valid Sudoku puzzle.

        Args:
            None
        Returns:
            None
        """
        self.Grid = np.array(
       [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]])

    def validate(self, x, y, n):
        """
        Validates if inserting 'n' at position (x, y) is valid according to Sudoku rules.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
            n (int): The number to be validated.
        Returns:
            bool: True if the insertion is valid, False otherwise.
        """
        for i in range(x - x % 3, (x - x % 3) + 3):
            for j in range(y - y % 3, (y - y % 3) + 3):
                if self.Grid[j][i] == n:
                    return False

        for i in range(9):
            if self.Grid[i][x] == n:
                return False

        for i in range(9):
            if self.Grid[y][i] == n:
                return False

        return True

    def matrixValidate(self):
        """
        Validates the entire Sudoku grid.

        Returns:
            bool: True if the Sudoku grid is valid, False otherwise.
        """
        for i in range(9):
            for j in range(9):
                if not (self.validate(i, j, self.Grid[i][j]) and self.Grid[i][j] > 0 and self.Grid[i][j] < 10):
                    return False
        return True

    def solve(self, x, y):
        """
        Solves the Sudoku puzzle using backtracking and recursion.

        Args:
            x (int): The current x-coordinate during solving.
            y (int): The current y-coordinate during solving.
        Returns:
            bool: True if the Sudoku puzzle is solved, False otherwise.
        """
        if y == 9:
            print("reached end")
            return True

        if x == 9:
            print("reached x9")
            x = 0
            y = y + 1

        if x == 8 and y == 8:
            for i in range(1, 10):
                if self.validate(x, y, i):
                    self.Grid[y][x] = i
                    return True

        if self.Grid[y][x] > 0:
            return self.solve(x + 1, y)

        for i in range(1, 10):
            if self.validate(x, y, i):
                self.Grid[y][x] = i
                if self.solve(x + 1, y): 
                    return True
                else:
                    self.Grid[y][x] = 0
        return False

game1 = SudokuGrid()
game1.solve(0, 0)
print(game1.Grid)
