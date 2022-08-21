class SudokuProblm:
    def __init__(self,sudokuTable,size,row,col):
        self.sudokuTable=sudokuTable
        self.size=size
        self.row=row
        self.col=col

    def solve(self):
        if(self.isSolvable(self.sudokuTable,0,0)):
            self.showResult()
        else:
            print("There are no result")


    def showResult(self):
        for i in range(row):
            for j in range(col):
                print(self.sudokuTable[i][j],end="  ")
            print()

    def isSolvable(self,sudokuTable,row,col):
        if(row==9):
            return True
        if(col==9):
            s=self.isSolvable(sudokuTable,row+1,0)
            return s
        if(sudokuTable[row][col]!=0):
            return self.isSolvable(sudokuTable,row,col+1)
        for value in range(1,size+1):
            if(self.isValid(sudokuTable,row,col,value)):
                sudokuTable[row][col]=value
                suc=self.isSolvable(sudokuTable,row,col+1)
                if(suc):
                    return True
                sudokuTable[row][col]=0
        return False

    def isValid(self,sudokuTable,row,col,value):
        for x in range(9):
            if sudokuTable[row][x] == value:
                return False


    # Check if we find the same num in
    # the similar column , we
    # return false
        for x in range(9):
            if sudokuTable[x][col] == value:
                return False

        # Check if we find the same num in
        # the particular 3*3 matrix,
        # we return false
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if sudokuTable[i + startRow][j + startCol] == value:
                    return False

        return True

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]]
size=9
row=9
col=9
obj=SudokuProblm(grid,size,row,col)
obj.solve()
