from Position import Position


class PositionsMap:

    def __init__(self, map):
        self.positions = []
        tile_row = 0

        self.positions.append([])
        for i in range(3):
            self.positions[0].append(
                Position(map.getItemAtIndex(tile_row, i+1).dots, [2, len(self.positions[0])]))

        self.positions.append([])
        for i in range(4):
            self.positions[1].append(
                Position(map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row, i+1).dots, [1, 1]))

        self.positions.append([])
        for i in range(4):
            self.positions[2].append(
                Position(map.getItemAtIndex(tile_row, i+1).dots+map.getItemAtIndex(tile_row, i).dots + map.getItemAtIndex(tile_row+1, i+1).dots, [1, 1]))

        tile_row += 1

        self.positions.append([])
        for i in range(5):
            self.positions[3].append(
                Position(map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row, i+1).dots+map.getItemAtIndex(tile_row-1, i).dots, [1, 1]))

        self.positions.append([])
        for i in range(5):
            self.positions[4].append(
                Position(map.getItemAtIndex(tile_row, i+1).dots+map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row+1, i+1).dots, [1, 1]))

        tile_row += 1

        self.positions.append([])
        for i in range(6):
            self.positions[5].append(
                Position(map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row, i+1).dots+map.getItemAtIndex(tile_row-1, i).dots, [1, 1]))

        self.positions.append([])
        for i in range(6):
            self.positions[6].append(
                Position(map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row+1, i).dots+map.getItemAtIndex(tile_row, i+1).dots, [1, 1]))

        tile_row += 1
        self.positions.append([])
        for i in range(5):
            self.positions[7].append(
                Position(map.getItemAtIndex(tile_row, i+1).dots+map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row-1, i+1).dots, [1, 1]))

        self.positions.append([])
        for i in range(5):
            self.positions[8].append(
                Position(map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row+1, i).dots+map.getItemAtIndex(tile_row, i+1).dots, [1, 1]))

        tile_row += 1
        self.positions.append([])
        for i in range(4):
            self.positions[9].append(
                Position(map.getItemAtIndex(tile_row, i).dots+map.getItemAtIndex(tile_row, i+1).dots+map.getItemAtIndex(tile_row-1, i+1).dots, [1, 1]))

        self.positions.append([])
        for i in range(4):
            self.positions[10].append(
                Position(map.getItemAtIndex(tile_row, i).dots + map.getItemAtIndex(tile_row, i+1).dots, [1, 1]))

        self.positions.append([])
        for i in range(3):
            self.positions[11].append(
                Position(map.getItemAtIndex(tile_row, i+1).dots, [1, 1]))

    def __repr__(self):
        board = []
        for i in range(len(self.positions)):
            row = []
            for t in range(len(self.positions[i])):
                row.append(str(self.positions[i][t].value))
            board.append('-'.join(row))

        return "\n".join(board)
