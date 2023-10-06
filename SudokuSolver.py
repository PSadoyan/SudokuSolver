import numpy as np

class SudokuGrid:
    x = 0
    y = 0
    n = 1
    def _init_(grid):
        grid.oGrid = np.array(
        [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]])

        grid.sGrid = np.array(
        [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]])

    def isZero(grid,x,y):
        if grid.oGrid[x][y] == 0:
            return True
        
    def insert(grid,x,y,n):
        if grid.oGrid.isZero(grid.oGrid,x,y,n):
            grid.sGrid[x][y] = n

    def validate(grid,x,y,n):
        for i in range (x-x%3,(x-x%3)+3):
            for j in range (y-y%3,(y-y%3)+3):
                 if n == grid.oGrid[i][j]:
                    return False
        for i in range (9):
            if n == grid.oGrid[i]:
                return False
        for i in range (9):
            if n == grid.oGrid[x][i]:
                return False
        return True
    
    def matrixValidate(grid):
        for i in range (9):
            for j in range (9):
                grid.sGrid.validate(grid,i,j,grid.sGrid[i][j]) & grid.sGrid[i][j] != 0
    
    def solve(grid,x,y,n):
        if ((grid.oGrid[x][y] > 0) & (x==8) & (y==8)) | ((grid.oGrid[x][y] == 0) & (x==8) & (y==8) & (n==10)):
            if grid.sGrid.matrixValidate(grid):
                return grid.sGrid
        if ((grid.oGrid[x][y] > 0) & (x==8)) | ((grid.oGrid[x][y] == 0) & (x==8) & (n==10)):
            return grid.sGrid.solve(grid,0,y+1,1)
        if grid.oGrid[x][y] > 0:
            return grid.sGrid.solve(grid,x+1,y,1)
        if grid.oGrid[x][y] == 0:
            if n == 10:
                return grid.sGrid.solve(grid,x+1,y,1)
            if not grid.sGrid[x][y].validate(grid,x,y,n):
                grid.sGrid.insert(grid,x,y,n)
                return grid.sGrid.solve(grid,x,y,n+1)
            return grid.sGrid.solve(grid,x+1,y,1)
            
game1 = SudokuGrid()
game1.solve(0,0,1)