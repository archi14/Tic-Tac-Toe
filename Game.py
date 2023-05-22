class Game:

    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.number_of_players = len(self.players)
    
    def play(self):
        cur_player = 0
        
        while True:
            player = self.players[cur_player%self.number_of_players]
            self.board.printBoard()
            print(f'Player {player.name} turn')
            row = int(input("row where you want the mark "))
            col = int(input('col where you want to mark '))
            try:
                if(self.board.makeMove(row, col, player.sign)):
                    self.board.printBoard()
                    print(f'Player {player.name} has won the game')
                    return
                if self.board.isBoardFilled():
                    print('There has been a draw')
                    return
                cur_player = cur_player + 1
            except ValueError:
                print('Not a valid Move, Try Again')
               
               
    
            


