import numpy as np

class SudokuGrid:
    x = 0
    y = 0
    n = 1
    Grid = np.array(
        [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]])
    
    def _init_(self):
        self.Grid = np.array(
        [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]])

    def isZero(self,x,y):
        if self.Grid[x][y] == 0:
            return True
        
    def insert(self,x,y,n):
        if self.isZero(x,y):
            self.Grid[x][y] = n

    def validate(self,x,y,n):
        for i in range (x-x%3,(x-x%3)+3):
            for j in range (y-y%3,(y-y%3)+3):
                 if n == self.Grid[i][j]:
                    return False
                 
        for i in range (9):
            if n == self.Grid[i][y]:
                return False
            
        for i in range (9):
            if n == self.Grid[x][i]:
                return False
            
        return True
    
    def matrixValidate(self):
        for i in range (9):
            for j in range (9):
                self.validate(i,j,self.Grid[i][j]) and self.Grid[i][j] != 0
    
    def solve(self,x,y,n):
        print(str(x) + " x")
        print(str(y) + " y")
        if (y==9) or ((x==8) and (y==8) and (n==10) and (self.Grid[x-1][y-1] == 0)):
            if self.matrixValidate():
                return self.Grid
            
        if (x==9):
            return self.solve(0,y+1,1)
        
        if ((x==8) and (y==8)):
            self.insert(x,y,n)
            return self.Grid
        
        if self.Grid[x][y] > 0:
            return self.solve(x+1,y,1)
        
        if self.Grid[x][y] == 0:
            if n == 10:
                return self.solve(x+1,y,1)
            if self.validate(x,y,n):
                self.insert(x,y,n)
                return self.solve(x+1,y,1)
            return self.solve(x,y,n+1)

game1 = SudokuGrid()
game1.solve(0,0,1)
print(game1.Grid)
