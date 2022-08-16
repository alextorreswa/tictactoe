from src.index import store
class Player:
    def __init__(self, name):
        self.name = name
        self.id = len(store['players']) + 1
        store['players'].append(self)