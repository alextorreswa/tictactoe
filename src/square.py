from src.index import store
class Square:
    def __init__(self, row, col, index, board):
        store['squares'].append(self)
        self.row = row
        self.col = col
        self.index = index
        self.board = board

    def move(self):
        return [move for move in self.board.game().moves() if move.square == self] or None

    def player(self):
        if self.move:
            return self.move.player

    def marker(self):
        if self.player():
            return self.player().marker
        else:
            return '?'