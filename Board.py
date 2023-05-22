class Board:

    def __init__(self, size):
        self.size = size
        self.rows = {}
        self.cols = {}
        self.diagonals = {}
        self.board = [["" for i in range(self.size)] for j in range(self.size)]
        self.marked_count = 0
    
    # Function to print the current tic-tac-toe board
    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                if j!=self.size-1:
                    print(self.board[i][j], end=' |')
                else:
                    print(self.board[i][j], end='')
            print()

    # Checks if the board is completely filled or not
    def isBoardFilled(self):
        if self.marked_count == self.size*self.size:
            return True
        return False

    # Checks if the given cell in the board is filled
    def isFilled(self, row, col):

        if self.board[row][col]=="":
            return False
        return True

    # Check if the move made by the player is a valid move
    def isValid(self, row, col):
        if row >=0 and row < self.size and col >=0 and col < self.size and self.isFilled(row, col)==False:
            return True
        return False

    # Function that enables making a move on the board
    def makeMove(self, row, col, sign):

        if self.isValid(row, col) == False:
            raise ValueError
        else:
             self.board[row][col] = sign
             self.marked_count = self.marked_count + 1

        self.rows[row] = self.rows.get(row, {})
        self.rows[row][sign] = self.rows[row].get(sign,0) + 1

        if self.rows[row][sign] == self.size:
            return True

        self.cols[col] = self.cols.get(col, {})
        self.cols[col][sign] = self.cols[col].get(sign,0) + 1

        if self.cols[col][sign] == self.size:
            return True

        if row == col:
            self.diagonals["forward"] = self.diagonals.get("forward", {})
            self.diagonals["forward"][sign] = self.diagonals["forward"].get(sign,0) + 1
            if self.diagonals["forward"][sign] == self.size:
                return True

        if row + col == self.size - 1:
            self.diagonals["backward"] = self.diagonals.get("backward", {})
            self.diagonals["backward"][sign] = self.diagonals["backward"].get(sign,0) + 1
            if self.diagonals["backward"][sign] == self.size:
                return True       