from Coordinate import Coordinate

class Map:
    def __init__(self, tiles):
        self.map = []
        for row in tiles:
            for tile in row.strip():
                self.map.append(tile)
        self.width = len(tiles[0]) - 1
        self.height = len(tiles)
        self.walls = tuple(i for i, tile in enumerate(self.map) if tile.strip() == "#")
        # print(self.walls)

        self.guardRotation = ""
        if "^" in self.map:
            self.guardRotation = "^"
        elif "v" in self.map:
            self.guardRotation = "v"
        elif "<" in self.map:
            self.guardRotation = "<"
        elif ">" in self.map:
            self.guardRotation = ">"

        self.guardStartRotation = self.guardRotation

        self.guardIndex = self.map.index(self.guardRotation)
        self.guardStartIndex = self.guardIndex
        self.guardCoordinate = Coordinate.indexToCoordinates(self.guardIndex, self.width)
        self.walkedIndexes = []
        self.barrierIndex = -1

    # def getTile(self, coordinate:Coordinate):
    #     return self.map[Coordinate.coordinateToIndex(coordinate, self.height)]

    def getGuardLoc(self) -> int:
        return self.guardIndex

    def getGuardRotation(self):
        return self.guardRotation

    def turnGuard(self) -> None:
        match self.getGuardRotation():
            case "^":
                self.guardRotation = ">"
            case "v":
                self.guardRotation  = "<"
            case "<":
                self.guardRotation  = "^"
            case ">":
                self.guardRotation  = "v"

    def moveGuard(self, newGuardCoords:Coordinate, newGuardIndex) -> list:
        returnPacket = []
        if self.isValid(newGuardCoords, self.getGuardRotation()):
            if newGuardIndex in self.walls:
                # HITTING A WALL
                self.turnGuard()
                returnPacket.insert(1, (self.guardCoordinate, self.getGuardRotation()))
            elif newGuardIndex == self.barrierIndex:
                # HITTING A BARRIER
                self.turnGuard()
            else:
                # MOVING
                if self.guardIndex not in self.walkedIndexes:
                    self.walkedIndexes.append(self.guardIndex)
                self.guardIndex = newGuardIndex
                self.guardCoordinate = newGuardCoords
            # isValid TRUE RETURN PACKET
            returnPacket.insert(0, True)
        else:
            # isValid FALSE RETURN PACKET
            if self.guardIndex not in self.walkedIndexes:
                self.walkedIndexes.append(self.guardIndex)
            returnPacket.insert(0, False)

        return returnPacket

    def moveGuardUp(self):
        newGuardCoords = Coordinate(self.guardCoordinate.getX(), self.guardCoordinate.getY()-1)
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(newGuardCoords, newGuardIndex)

    def moveGuardDown(self):
        newGuardCoords = Coordinate(self.guardCoordinate.getX(), self.guardCoordinate.getY() + 1)
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(newGuardCoords, newGuardIndex)


    def moveGuardLeft(self):
        newGuardCoords = Coordinate(self.guardCoordinate.getX() - 1, self.guardCoordinate.getY())
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(newGuardCoords, newGuardIndex)

    def moveGuardRight(self):
        newGuardCoords = Coordinate(self.guardCoordinate.getX() + 1, self.guardCoordinate.getY())
        newGuardIndex = Coordinate.coordinateToIndex(newGuardCoords, self.height)

        return self.moveGuard(newGuardCoords, newGuardIndex)


    def __str__(self):
        mapString = ""
        for i, char in enumerate(self.map):
            if (i+1) % self.width == 0:
                mapString += char  + "\n"
            else:
                mapString += char
        return mapString

    def printWithFormatting(self):
        mapCopy = self.map.copy()
        for walked in self.walkedIndexes:
            mapCopy[walked] = "X"
        mapCopy[self.guardIndex] = self.guardRotation
        mapString = ""
        for i, char in enumerate(mapCopy):
            if (i + 1) % self.width == 0:
                mapString += char + "\n"
            else:
                mapString += char
        print(mapString)


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

    def resetGuardLocation(self):
        self.guardIndex = self.guardStartIndex
        self.guardCoordinate = Coordinate.indexToCoordinates(self.guardIndex, self.width)
        self.guardRotation = self.guardStartRotation