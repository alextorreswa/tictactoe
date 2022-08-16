from src.square import Square
class PlayGame:
    def build_board(self, board):
        squares = []
        for row in range(1, 4):
            for col in range(1, 4):
                index = row + col - 1
                square = Square(row, col, index, board)
        return board

    def prompt_move(player):
        index = input(f"player {player.name}, where do you want to move?")
        square = board.find_square_by_index(index)
        move = Move(game, player, square) 

    def print_board():
        [square.marker() for square in board.squares()]