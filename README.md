# SudokuGrid Class

This class represents a Sudoku puzzle solver using backtracking.

## Attributes

- `x (int)`: The current x-coordinate during Sudoku solving.
- `y (int)`: The current y-coordinate during Sudoku solving.
- `n (int)`: The current number being inserted into the Sudoku grid.
- `Grid (numpy.ndarray)`: A 9x9 NumPy array representing the Sudoku grid.

## Methods

### `__init__(self)`

Constructor method to initialize the `SudokuGrid` object. Initializes the Sudoku grid with a valid Sudoku puzzle.

### `insert(self, x, y, n)`

Inserts a number 'n' at position (x, y) in the Sudoku grid.

- Args:
    - `x (int)`: The x-coordinate of the position.
    - `y (int)`: The y-coordinate of the position.
    - `n (int)`: The number to be inserted.

### `validate(self, x, y, n)`

Validates if inserting 'n' at position (x, y) is valid according to Sudoku rules.

- Args:
    - `x (int)`: The x-coordinate of the position.
    - `y (int)`: The y-coordinate of the position.
    - `n (int)`: The number to be validated.

- Returns:
    - `bool`: True if the insertion is valid, False otherwise.

### `matrixValidate(self)`

Validates the entire Sudoku grid.

- Returns:
    - `bool`: True if the Sudoku grid is valid, False otherwise.

### `solve(self, x, y)`

Solves the Sudoku puzzle using backtracking and recursion.

- Args:
    - `x (int)`: The current x-coordinate during solving.
    - `y (int)`: The current y-coordinate during solving.

- Returns:
    - `bool`: True if the Sudoku puzzle is solved, False otherwise.

## Example Usage

```python
game1 = SudokuGrid()
game1.solve(0, 0)
print(game1.Grid)
