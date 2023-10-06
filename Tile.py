class Tile:
    def __init__(self, number, coordinates):
        self.number = number
        self.coordinates = coordinates

    def getNumber(self):
        return self.number

    def __repr__(self):
        return str(self.number)
