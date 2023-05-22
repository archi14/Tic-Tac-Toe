from Player import Player
from Board import Board
from Game import Game

def main():
    name = input('Please enter player 1 name\n')
    player1 = Player(name,'X')
    name = input('Please enter player 2 name\n')
    player2 = Player(name,'O')
    size = int(input('Please enter size of the board\n'))
    board = Board(size)
    game = Game(board, [player1, player2])
    game.play()


if __name__ == "__main__":
    main()