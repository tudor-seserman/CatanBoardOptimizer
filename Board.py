from Tile import Tile


class Board:
    board = []

    def __init__(self, numbers):
        count = 0

        self.board.append([Tile(0, [0, 0])])
        for i in range(3):
            self.board[0].append(
                Tile(numbers[count], [2, len(self.board[0])-1]))
            count += 1
        self.board[0].append(Tile(0, [0, 0]))

        self.board.append([Tile(0, [0, 0])])
        for i in range(4):
            self.board[1].append(
                Tile(numbers[count], [1, len(self.board[1])-1]))
            count += 1
        self.board[1].append(Tile(0, [0, 0]))

        self.board.append([Tile(0, [0, 0])])
        for i in range(5):
            self.board[2].append(
                Tile(numbers[count], [len(self.board[2])-1, 2]))
            count += 1
        self.board[2].append(Tile(0, [0, 0]))

        self.board.append([Tile(0, [0, 0])])
        for i in range(4):
            self.board[3].append(
                Tile(numbers[count], [len(self.board[3])-1, 3]))
            count += 1
        self.board[3].append(Tile(0, [0, 0]))

        self.board.append([Tile(0, [0, 0])])
        for i in range(3):
            self.board[4].append(
                Tile(numbers[count], [len(self.board[4])-1, 4]))
            count += 1
        self.board[4].append(Tile(0, [0, 0]))

    def getItemAtIndex(self, index1, index2):
        return self.board[index1][index2]

    def __repr__(self):
        board = []
        for i in range(5):
            row = []
            for t in range(len(self.board[i])):
                print(str(self.board[i][t].number))
                row.append(str(self.board[i][t].coordinates))
            board.append('-'.join(row))

        return "\n".join(board)
