from src.index import store
class Game:
    def __init__(self, player_one, player_two, board):
        self.player_one = player_one
        self.player_two = player_two
        self.board = board
        store['games'].append(self)

class sdf:
    def __init__(self, state = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]):
        self.state = state
  
    def get_rows(self):
      return [r for r in self.state]

    def get_cols(self):
      cols = []
      for r in range(3):
        cols.append([self.state[0][r], self.state[1][r], self.state[2][r]])
      return cols

    def get_diags(self):
      return [[self.state[r][r] for r in range(3)], [self.state[2-r][r] for r in range(3)]]

    def combinations(self):
      return self.get_rows() + self.get_cols() + self.get_diags()

    def winner(self):
      # look if the game is over
      if len([num for row in self.state for num in row if num != 'O' and num != 'X']) >= 1:
          return 'N/A'    
      # look matches
      look = [c for c in self.combinations() if c == ['X', 'X', 'X'] or c == ['O', 'O', 'O']]
      if len(look) >= 1:
        return look[0][0]
      else:
        return 'TIE'

    def play(self, x, y, player):
      if self.state[x][y] == '-':
        self.state[x][y] = player
      else:
        return False
    







