from Board import Board
from PositionsMap import PositionsMap
from Tile import Tile


test_board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19])

print(test_board)
print("-"*100)
print(str(test_board.board[4][1].coordinates) +
      " Tile Value:" + str(test_board.board[4][1]))
print("-"*100)
test_position_map = PositionsMap(test_board)
print(test_position_map)
print("-"*100)


dot_test_board = Board(
    [2, 6, 4, 3, 4, 5, 4, 6, 2, 3, 2, 1, 4, 3, 1, 2, 5, 3, 5])
print(dot_test_board)
print("-"*100)
print(dot_test_board.getAllNumbers())
print("-"*100)
dot_test_board_position_map = PositionsMap(dot_test_board)
print(dot_test_board_position_map)
