from Board import Board
from PositionsMap import PositionsMap
from Tile import Tile


# test_board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#                    11, 12, 13, 14, 15, 16, 17, 18, 19])

# print(test_board)
# print("-"*100)
# print(str(test_board.board[4][1].coordinates) +
#       " Tile Value:" + str(test_board.board[4][1]))
# print("-"*100)
# test_position_map = PositionsMap(test_board)
# print(test_position_map)
# print("-"*100)


# dot_test_board = Board(
#     [2, 6, 4, 3, 4, 5, 4, 6, 2, 3, 2, 1, 4, 3, 1, 2, 5, 3, 5])
# print(dot_test_board)
# print("-"*100)
# print(dot_test_board.getAllNumbers())
# print("-"*100)
# dot_test_board_position_map = PositionsMap(dot_test_board)
# print(dot_test_board_position_map)

# Here is the map I am trying to represent:
# https://www.reddit.com/media?url=https%3A%2F%2Fexternal-preview.redd.it%2FUbdGe_gGyZmvxsXmB8ajt9myT8l_qrd-sfxV1PyaVnc.jpg%3Fauto%3Dwebp%26s%3D96c113fc4d447960203ac5b4fda7bbd99130f4fc

number_test_board = Board(
    [3, 7, 9, 10, 9, 6, 5, 6, 11, 4, 11, 12, 5, 10, 2, 3, 8, 4, 8])
print(number_test_board.getAllNumbers())
print("-"*100)
number_test_board_position_map = PositionsMap(number_test_board)
# This will eventually print the sum of all the dots from the tiles that boarder the position
print(number_test_board_position_map)
