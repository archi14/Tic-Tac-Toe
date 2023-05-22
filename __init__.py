from Player import Player
from Board import Board
from Game import Game

def main():
    player1 = Player('Something','X')
    player2 = Player('Somethingelse','O')
    size = int(input('Please enter size of the board '))
    board = Board(size)
    game = Game(board, [player1, player2])
    game.play()


if __name__ == "__main__":
    main()