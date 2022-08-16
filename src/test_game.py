from opcode import stack_effect
from game import Board

def test_game_winner():
    state = [['X', 'X', 'X'], 
            ['X', 'O', 'O'], 
            ['O', 'X', 'O']]
    game1 = Board(state = state)
    assert game1.winner() == 'X'

def test_game_winner2():
    state = [['X', 'X', 'O'], 
            ['X', 'O', 'O'], 
            ['O', 'X', 'O']]
    game1 = Board(state = state)
    assert game1.winner() == 'O'

def test_game_winner3():
    state = [['X', 'X', 'O'], 
            ['X', 'O', 'X'], 
            ['X', 'O', 'O']]
    game1 = Board(state = state)
    assert game1.winner() == 'X'

def test_game_winner4():
    state = [['X', 'X', 'O'], 
            ['X', '-', 'X'], 
            ['X', 'O', 'O']]
    game1 = Board(state = state)
    assert game1.winner() == 'N/A'

def test_game_winner4():
    state = [['X', 'X', 'O'], 
            ['O', 'X', 'X'], 
            ['X', 'O', 'O']]
    game1 = Board(state = state)
    assert game1.winner() == 'TIE'

def test_game_winner5():
    state = [['O', '-', 'X'], 
            ['X', 'O', '-'], 
            ['-', '-', 'O']]
    o = 'O'
    x = 'X'
    game1 = Board()
    game1.play(0,0,o)
    game1.play(0,2,x)
    game1.play(1,1,o)
    game1.play(1,0,x)
    game1.play(2,2,o)
    assert game1.state == state

def test_game_winner6():
    state = [['O', '-', 'X'], 
            ['X', 'O', '-'], 
            ['-', '-', 'O']]
    o = 'O'
    x = 'X'
    game1 = Board()
    game1.play(0,0,o)
    game1.play(0,2,x)
    game1.play(1,1,o)
    game1.play(1,1,x)    
    game1.play(1,0,x)
    game1.play(2,2,o)
    assert game1.state == state
    assert game1.winner() == 'N/A'    