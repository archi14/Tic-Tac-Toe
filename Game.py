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
                try:
                    if(self.board.makeMove(row, col, player.sign)):
                        self.board.printBoard()
                        print(f'Player {player.name} has won the game')
                        return
                except ValueError:
                    print('Not a valid Move, Try Again')
    
            


