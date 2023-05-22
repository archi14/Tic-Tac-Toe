from Player import Player
from Board import Board
from Game import Game

def main():
    player1 = Player('Something','X')
    player2 = Player('Somethingelse','O')
    number_of_rows = int(input('Please enter the number of rows in the board '))
    number_of_cols = int(input('Please enter the number of columns in the board '))
    board = Board(number_of_rows, number_of_cols)
    game = Game(board, [player1, player2])
    game.play()


if __name__ == "__main__":
    main()