import numpy as np

class SudokuGrid:
    x = 0
    y = 0
    n = 1
    Grid = np.array(
        [[0,0,0,0,9,0,0,2,0],
        [4,0,2,5,0,0,0,6,0],
        [0,5,3,0,7,0,0,4,0],
        [0,7,8,0,0,1,0,0,3],
        [9,0,0,0,5,0,0,0,0],
        [0,4,0,6,0,0,0,0,0],
        [0,0,0,0,0,7,0,0,2],
        [5,0,0,0,4,0,7,0,0],
        [0,0,0,0,0,0,1,0,6]])
    
    def _init_(self):
        self.Grid = np.array( #valid Sudoku game
        [[0,0,0,0,9,0,0,2,0],
        [4,0,2,5,0,0,0,6,0],
        [0,5,3,0,7,0,0,4,0],
        [0,7,8,0,0,1,0,0,3],
        [9,0,0,0,5,0,0,0,0],
        [0,4,0,6,0,0,0,0,0],
        [0,0,0,0,0,7,0,0,2],
        [5,0,0,0,4,0,7,0,0],
        [0,0,0,0,0,0,1,0,6]])
 
    def insert(self,x,y,n): #O(1)
            self.Grid[x][y] = n

    def validate(self,x,y,n): #O(1) 
        for i in range (x-x%3,(x-x%3)+3):
            for j in range (y-y%3,(y-y%3)+3):
                 if self.Grid[i][j] == n:
                    return False
                 
        for i in range (9):
            if self.Grid[i][y] == n:
                return False
            
        for i in range (9):
            if self.Grid[x][i] == n:
                return False
            
        return True
    
    def matrixValidate(self): #O(1): larger constant, but still a constant
        for i in range (9):
            for j in range (9):
                self.validate(i,j,self.Grid[i][j]) and self.Grid[i][j] > 0 and self.Grid[i][j] < 10
    
    def solve(self,x,y,n): #O(1)
        print(str(x) + " x " + str(n))
        print(str(y) + " y " + str(n))
        if (y==9):
            if self.matrixValidate():
                return True
            
        if (x==9):
            return self.solve(0,y+1,1)
        
        if ((x==8) and (y==8)):
            if self.validate(x,y,n):
                self.insert(x,y,n)
                return self.Grid
            return self.solve(x,y,n+1)
        
        if self.Grid[x][y] > 0:
            return self.solve(x+1,y,1)
        
        if self.Grid[x][y] == 0:
            #if n == 10:
            #    return self.solve(x+1,y,1)
            if self.validate(x,y,n):
                self.insert(x,y,n)
                return self.solve(x+1,y,1)
            return self.solve(x,y,n+1)
        return False

game1 = SudokuGrid()
game1.solve(0,0,1)
print(game1.Grid)
