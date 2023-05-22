class Board:

    def __init__(self, number_of_rows, number_of_cols):
        self.number_of_rows = number_of_rows
        self.number_of_cols = number_of_cols
        self.rows = {
                        'X': [0 for i in range(self.number_of_rows)],
                        'O': [0 for i in range(self.number_of_rows)]
                    }
        self.cols = {
                        'X': [0 for i in range(self.number_of_cols)],
                        'O': [0 for i in range(self.number_of_cols)]
                    }
        self.diagonals = {
                        'X': [0 for i in range(self.number_of_cols)],
                        'O': [0 for i in range(self.number_of_cols)]
                    }
        self.board = [["" for i in range(self.number_of_rows)] for j in range(self.number_of_cols)]

    def reset(self):
        self.rows = []
        self.columns = []
        self.diagonals = []
        self.board = []
    
    def printBoard(self):
        for i in range(self.number_of_rows):
            for j in range(self.number_of_cols):
                if j!=self.number_of_cols-1:
                    print(self.board[i][j], end=' |')
                else:
                    print(self.board[i][j], end='')
            print()

    def isFilled(self, row, col):

        if self.board[row][col]=="":
            return False
        return True

    def isValid(self, row, col):
        if row >=0 and row < self.number_of_rows and col >=0 and col < self.number_of_cols and self.isFilled(row, col)!=True:
            return True
        print("This is not a valid move, Try again")
        return False

    def makeMove(self, row, col, sign):
        self.rows[sign][row] +=1
        self.cols[sign][col] +=1
        if row == col:
            self.diagonals[sign][0] += 1
        if row + col == self.number_of_cols + self.number_of_rows:
            self.diagonals[sign][1] += 1
        self.board[row][col] = sign

    def ifWon(self, sign, row, col):

        if self.rows[sign][row] == self.number_of_rows or self.cols[sign][col] == self.number_of_cols or self.diagonals[sign][0]== self.number_of_cols or self.number_of_cols == self.diagonals[sign][1]:
            return True
        return False
    