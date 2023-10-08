from Position import Position


class PositionsMap:

    def __init__(self, map):
        self.positions = []
        count = 0

        self.positions.append([])
        for i in range(3):
            self.positions[0].append(
                Position(map.getItemAtIndex(count, i+1).dots, [2, len(self.positions[0])]))

        self.positions.append([])
        for i in range(4):
            self.positions[1].append(
                Position(map.getItemAtIndex(count, i).dots+map.getItemAtIndex(count, i+1).dots, [1, len(self.positions[1])+1]))

        self.positions.append([])
        for i in range(4):
            self.positions[2].append(
                Position(map.getItemAtIndex(count, i+1).dots+map.getItemAtIndex(count, i).dots + map.getItemAtIndex(count+1, i+1).dots, [1, len(self.positions[1])+1]))

        count += 1
        # Keep adding rows of positions

    def __repr__(self):
        board = []
        for i in range(3):
            row = []
            for t in range(len(self.positions[i])):
                row.append(str(self.positions[i][t].value))
            board.append('-'.join(row))

        return "\n".join(board)
