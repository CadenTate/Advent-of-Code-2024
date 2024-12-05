path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2024\Day 4\input.txt"

rawFile = open(path, 'r').readlines()

size = len(rawFile)

file = {}

for i in range(len(rawFile)):
    file[i] = rawFile[i].strip()

# Functions checking North and South
def checkNorth(y:int, x:int) -> bool:
    if y < 3:
        return False
    if file[y-1][x] != 'M':
        return False
    if file[y-2][x] != 'A':
        return False
    if file[y-3][x] != 'S':
        return False
    return True

def checkSouth(y:int, x:int) -> bool:
    if y > size - 4:
        return False
    if file[y+1][x] != 'M':
        return False
    if file[y+2][x] != 'A':
        return False
    if file[y+3][x] != 'S':
        return False
    return True

# Functions checking East and West
def checkEast(y:int, x:int) -> bool:
    if x < 3:
        return False
    if file[y][x-1] != 'M':
        return False
    if file[y][x-2] != 'A':
        return False
    if file[y][x-3] != 'S':
        return False
    return True

def checkWest(y:int, x:int) -> bool:
    if x > len(file[y]) - 4:
        return False
    if file[y][x+1] != 'M':
        return False
    if file[y][x+2] != 'A':
        return False
    if file[y][x+3] != 'S':
        return False
    return True

# Functions for checking angles
def checkNE(y:int, x:int) -> bool:
    if y < 3 or x < 3:
        return False
    if file[y-1][x-1] != 'M':
        return False
    if file[y-2][x-2] != 'A':
        return False
    if file[y-3][x-3] != 'S':
        return False
    return True

def checkNW(y:int, x:int) -> bool:
    if y < 3 or x > len(file[y]) - 4:
        return False
    if file[y-1][x+1] != 'M':
        return False
    if file[y-2][x+2] != 'A':
        return False
    if file[y-3][x+3] != 'S':
        return False
    return True

def checkSE(y:int, x:int) -> bool:
    if y > size - 4 or x > len(file[y]) - 4 :
        return False
    if file[y+1][x+1] != 'M':
        return False
    if file[y+2][x+2] != 'A':
        return False
    if file[y+3][x+3] != 'S':
        return False
    return True

def checkSW(y:int, x:int) -> bool:
    if y > size - 4 or x < 3:
        return False
    if file[y+1][x-1] != 'M':
        return False
    if file[y+2][x-2] != 'A':
        return False
    if file[y+3][x-3] != 'S':
        return False
    return True

total = 0

for y in range(len(file)):
    for x in range(len(file[y])):
        # print(i,file[i])
        # check if start
        if file[y][x] != 'X':
            continue
        

        if checkNorth(y,x):
            print(y,x,"N")
            total += 1
        if checkSouth(y,x):
            print(y,x,"S")
            total += 1
        if checkEast(y,x):
            print(y,x,"E")
            total += 1
        if checkWest(y,x):
            print(y,x,"W")
            total += 1
        if checkNE(y,x):
            print(y,x,"NE")
            total += 1
        if checkNW(y,x):
            print(y,x,"NW")
            total += 1
        if checkSE(y,x):
            print(y,x,"SE")
            total += 1
        if checkSW(y,x):
            print(y,x,"SW")
            total += 1

print(total)