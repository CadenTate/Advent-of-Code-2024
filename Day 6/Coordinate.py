class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    @staticmethod
    def coordinateToIndex(coordinate:"Coordinate", height:int) -> int:
        return coordinate.getY() * height + coordinate.getX()

    @staticmethod
    def indexToCoordinates(index:int, width:int) -> "Coordinate":
        return Coordinate(index % width, index // width)

    def __eq__(self, other):
        if type(other) == Coordinate:
            return self.x == other.x and self.y == other.y
        elif type(other) == tuple:
            return self.x == other[0] and self.y == other[1]
        return False

    def __str__(self):
        return f"({self.x}, {self.y})"