from src.index import store
class Move:
    def __init__(self, square, player):
        store['boards'].append(self)
        self.square = square
        self.player = player