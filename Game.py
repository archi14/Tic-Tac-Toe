class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players
    
    def play(self):

        while True:
            for player in self.players:
                self.board.printBoard()
                print(f'Player {player.name} turn')
                row = int(input("row where you want the mark "))
                col = int(input('col where you want to mark '))
                while self.board.isValid(row, col)== False:
                    row = int(input("row where you want the mark "))
                    col = int(input('col where you want to mark '))
                self.board.makeMove(row, col, player.sign)
                if(self.board.ifWon(player.sign, row, col)):
                    self.board.printBoard()
                    print(f'Player {player.name} has won the game')
                    return
            
    
            


