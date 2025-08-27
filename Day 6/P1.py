class Map:
    def __init__(self, tiles):
        self.map = []
        for row in tiles:
            for tile in row.strip():
                self.map.append(tile)
        self.width = len(tiles[0])-1
        self.height = len(tiles)

    def getTile(self, x, y):
        return self.map[self.coordinateToIndex(x, y)]

    def coordinateToIndex(self, x, y):
        return y * self.height + x

    def indexToCordinates(self, index):
        return index % self.width, index // self.width

    def getGuardLoc(self):
        return self.map.index(self.getGuardDirection())

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

    def moveGuardUp(self):
        guardIndex = self.getGuardLoc()
        guardCoords = self.indexToCordinates(guardIndex)
        if self.getTile(guardCoords[0], guardCoords[1]-1) == "#":
            self.map[guardIndex] = ">"
        else:
            self.map[self.coordinateToIndex(guardCoords[0], guardCoords[1]-1)] = "^"
            self.map[guardIndex] = "X"

    def moveGuardDown(self):
        guardIndex = self.getGuardLoc()
        guardCoords = self.indexToCordinates(guardIndex)
        newGuardCoords = self.coordinateToIndex(guardCoords[0], guardCoords[1] + 1)

        if self.getTile(newGuardCoords) == "#":
            self.map[guardIndex] = "<"
        else:
            self.map[guardIndex] = "X"
            if self.isValid(self.coordinateToIndex(newGuardCoords)):
                self.map[newGuardCoords] = "v"
            else:
                return False


    def moveGuardLeft(self):
        guardIndex = self.getGuardLoc()
        guardCoords = self.indexToCordinates(guardIndex)
        if self.getTile(guardCoords[0]-1, guardCoords[1]) == "#":
            self.map[guardIndex] = "^"
        else:
            self.map[self.coordinateToIndex(guardCoords[0]-1, guardCoords[1])] = "<"
            self.map[guardIndex] = "X"

    def moveGuardRight(self):
        guardIndex = self.getGuardLoc()
        guardCoords = self.indexToCordinates(guardIndex)
        if self.getTile(guardCoords[0]+1, guardCoords[1]) == "#":
            self.map[guardIndex] = "v"
        else:
            self.map[self.coordinateToIndex(guardCoords[0]+1, guardCoords[1])] = ">"
            self.map[guardIndex] = "X"

    def printMap(self):
        for i, char in enumerate(self.map):
            if (i+1) % self.width == 0:
                print(char)
            else:
                print(char, end="")

    def isValid(self, index:int):
        return index <= len(self.map)

path = r"input.txt"

with open(path) as file:
    inputMap = Map(file.readlines())

isInMap = True
while isInMap:
    inputMap.printMap()
    input()
    match inputMap.getGuardDirection():
        case "^":
            isInMap = inputMap.moveGuardUp()
        case "v":
            isInMap = inputMap.moveGuardDown()
        case "<":
            isInMap = inputMap.moveGuardLeft()
        case ">":
            isInMap = inputMap.moveGuardRight()






