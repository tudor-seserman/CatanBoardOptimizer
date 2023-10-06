from Board import Board
from PositionsMap import PositionsMap
from Tile import Tile


test_board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19])

print(test_board)
print(str(test_board.board[4][1].coordinates) +
      " Tile Value:" + str(test_board.board[4][1]))

test_position_map = PositionsMap(test_board)
print(test_position_map)
