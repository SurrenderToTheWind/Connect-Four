from myProject1 import *
from core import *

game = Core()
gui = GUI(game)
while true:
    gui.start_game(game.board_array)
