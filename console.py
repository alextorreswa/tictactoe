from src.services.play_game import PlayGame
from src.board import Board

game_play = PlayGame()

board = Board()
game_play.build_board(board)