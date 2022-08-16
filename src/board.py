from src.index import store
class Board:
    def __init__(self):
        store['boards'].append(self)

    def squares(self):
        return [square for square in store['squares'] if square.board == self]

    def game(self):
        return [game for game in store['games'] if game.board == self][0]

    def rows(self):
        ordered_rows = []
        for row_num in range(1, 4):
            row = [square for square in self.squares() if square.row == row_num]
            ordered_rows.append(row)

        return ordered_rows

    def columns(self):
        ordered_cols = []
        for col_num in range(1, 4):
            row = [square for square in self.squares() if square.column == col_num]
            ordered_cols.append(row)

        return ordered_cols