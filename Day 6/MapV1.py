from Coordinate import Coordinate

class Map:
    def __init__(self, tiles):
        self.map = []
        for row in tiles:
            for tile in row.strip():
                self.map.append(tile)
        self.width = len(tiles[0])-1
        self.height = len(tiles)

    def getTile(self, coordinate:Coordinate):
        return self.map[Coordinate.coordinateToIndex(coordinate, self.height)]

    def getGuardLoc(self) -> int:
        if self.getGuardDirection() in self.map:
            return self.map.index(self.getGuardDirection())
        return -1

    def getGuardDirection(self):
        if "^" in self.map:
            return "^"
        elif "v" in self.map:
            return "v"
        elif "<" in self.map:
            return "<"
        elif ">" in self.map:
            return ">"
        else:
            return None

    def turnGuard(self) -> None:
        match self.getGuardDirection():
            case "^":
                self.map[self.getGuardLoc()] = ">"
            case "v":
                self.map[self.getGuardLoc()] = "<"
            case "<":
                self.map[self.getGuardLoc()] = "^"
            case ">":
                self.map[self.getGuardLoc()] = "v"

    def moveGuard(self, guardIndex:int, guardCoords:Coordinate, newGuardCoords:Coordinate, newGuardIndex) -> list:
        returnPacket = []
        if self.isValid(newGuardCoords, self.getGuardDirection()):
            match self.getTile(newGuardCoords):
                case "#":
                    self.turnGuard()
                    returnPacket.insert(1, (guardCoords, self.getGuardDirection()))
                case "O":
                    self.turnGuard()
                case _:
                    self.map[newGuardIndex] = self.getGuardDirection()
                    self.map[guardIndex] = "X"
            returnPacket.insert(0, True)
        else:
            self.map[guardIndex] = "X"
            returnPacket.insert(0, False)

        return returnPacket

    def moveGuardUp(self):
        guardIndex = self.getGuardLoc()
        guardCoords = Coordinate.indexToCoordinates(guardIndex, self.width)
        newGuardCoords = Coordinate(guardCoords.getX(), guardCoords.getY()-1)
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(guardIndex, guardCoords, newGuardCoords, newGuardIndex)

    def moveGuardDown(self):
        guardIndex = self.getGuardLoc()
        guardCoords = Coordinate.indexToCoordinates(guardIndex, self.width)
        newGuardCoords = Coordinate(guardCoords.getX(), guardCoords.getY() + 1)
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(guardIndex, guardCoords, newGuardCoords, newGuardIndex)


    def moveGuardLeft(self):
        guardIndex = self.getGuardLoc()
        guardCoords = Coordinate.indexToCoordinates(guardIndex, self.width)
        newGuardCoords = Coordinate(guardCoords.getX() - 1, guardCoords.getY())
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(guardIndex, guardCoords, newGuardCoords, newGuardIndex)

    def moveGuardRight(self):
        guardIndex = self.getGuardLoc()
        guardCoords = Coordinate.indexToCoordinates(guardIndex, self.width)
        newGuardCoords = Coordinate(guardCoords.getX() + 1, guardCoords.getY())
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(guardIndex, guardCoords, newGuardCoords, newGuardIndex)


    def __str__(self):
        mapString = ""
        for i, char in enumerate(self.map):
            if (i+1) % self.width == 0:
                mapString += char  + "\n"
            else:
                mapString += char
        return mapString


    def isValid(self, coord:Coordinate, guardDirection:str) -> bool:
        match guardDirection:
            case "^":
                return coord.getY() >= 0
            case "v":
                return coord.getY() < self.height
            case "<":
                return coord.getX() >= 0
            case ">":
                return coord.getX() < self.width

    def hitWall(self) -> Coordinate:
        return Coordinate.indexToCoordinates(self.getGuardLoc(), self.height)