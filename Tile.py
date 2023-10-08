from typing import Any


numToProbability = {
    0: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 0,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}


class Tile:
    def __init__(self, number, coordinates):
        self.number = number
        self.dots = numToProbability[number]
        self.coordinates = coordinates

    def getNumber(self):
        return self.number

    def getDots(self):
        return self.dots

    def __repr__(self):
        return str(self.number)
