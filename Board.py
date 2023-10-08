from Tile import Tile


class Board:

    def __init__(self, numbers):
        self.board = []
        input_index = 0

        def addRow(row_length, row_number, row_number_from_center, input_index):
            self.board.append([Tile(0, [0, 0])])

            if (row_number_from_center > 0):
                x_coordinate = row_number_from_center
                for i in range(row_length):
                    self.board[row_number].append(
                        Tile(numbers[input_index], [x_coordinate, row_number]))
                    input_index += 1
                    x_coordinate += 1
            else:
                for i in range(row_length):
                    self.board[row_number].append(
                        Tile(numbers[input_index], [len(self.board[row_number])-1, row_number]))
                    input_index += 1

            self.board[row_number].append(Tile(0, [0, 0]))
            return input_index

        input_index = addRow(3, 0, 2, input_index)
        input_index = addRow(4, 1, 1, input_index)
        input_index = addRow(5, 2, 0, input_index)
        input_index = addRow(4, 3, -1, input_index)
        input_index = addRow(3, 4, -2, input_index)

    def getItemAtIndex(self, index1, index2):
        return self.board[index1][index2]

    def getAllNumbers(self):
        board = []
        for i in range(5):
            row = []
            for t in range(len(self.board[i])):
                row.append(str(self.board[i][t].number))
            board.append('-'.join(row))
        return "\n".join(board)

    def __repr__(self):
        board = []
        for i in range(5):
            row = []
            for t in range(len(self.board[i])):
                row.append(str(self.board[i][t].coordinates))
            board.append('-'.join(row))
        return "\n".join(board)
