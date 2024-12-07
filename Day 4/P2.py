path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2024\Day 4\input.txt"

rawFile = open(path, 'r').readlines()

# Pre minus to reflect 0-# nature
height = len(rawFile) - 1

file = {}

for i in range(len(rawFile)):
    file[i] = rawFile[i].strip()

# Functions checking North and South
def checkNorth(y:int, x:int) -> bool:
    if y < 2 or y > height:
        return False
    if file[y][x] != 'M':
        return False
    if file[y-2][x] != 'S':
        return False
    return True

def checkSouth(y:int, x:int) -> bool:
    if y < 0 or y > height - 2:
        return False
    if file[y][x] != 'M':
        return False
    if file[y+2][x] != 'S':
        return False
    return True

# Functions checking East and West
def checkEast(y:int, x:int) -> bool:
    if x < 0 or x > len(file[y]) - 3:
        return False
    if file[y][x] != 'M':
        return False
    if file[y][x+2] != 'S':
        return False
    return True

def checkWest(y:int, x:int) -> bool:
    if x < 2 or x > len(file[y]) - 1:
        return False
    if file[y][x] != 'M':
        return False
    if file[y][x-2] != 'S':
        return False
    return True

# Functions for checking angles
def checkNE(y:int, x:int) -> bool:
    if y < 2 or y > height or x < 0 or x > len(file[y]) - 3:
        return False
    if file[y][x] != 'M':
        return False
    if file[y-2][x+2] != 'S':
        return False
    return True

def checkNW(y:int, x:int) -> bool:
    if y < 2 or y > height or x < 2 or x > len(file[y]) - 1:
        return False
    if file[y][x] != 'M':
        return False
    if file[y-2][x-2] != 'S':
        return False
    return True

def checkSE(y:int, x:int) -> bool:
    if y < 0 or y > height - 2 or x < 0 or x > len(file[y]) - 3:
        return False
    if file[y][x] != 'M':
        return False
    if file[y+2][x+2] != 'S':
        return False
    return True

def checkSW(y:int, x:int) -> bool:
    if y < 0 or y > height - 2 or x < 2 or x > len(file[y]) - 1:
        return False
    if file[y][x] != 'M':
        return False
    if file[y+2][x-2] != 'S':
        return False
    return True

grandTotal = 0

for y in range(len(file)):
    for x in range(len(file[y])):
        total = 0
        # check if start
        if file[y][x] != 'A':
            continue
        
        # OFFSETS: N+1 | S-1 | E-1 | W+1 |
        # if checkNorth(y+1,x):
        #     print(y,x,"N")
        #     total += 1
        # if checkSouth(y-1,x):
        #     print(y,x,"S")
        #     total += 1
        # if checkEast(y,x-1):
        #     print(y,x,"E")
        #     total += 1
        # if checkWest(y,x+1):
        #     print(y,x,"W")
        #     total += 1
        if checkNE(y+1,x-1):
            print(y,x,"NE")
            total += 1
        if checkNW(y+1,x+1):
            print(y,x,"NW")
            total += 1
        if checkSE(y-1,x-1):
            print(y,x,"SE")
            total += 1
        if checkSW(y-1,x+1):
            print(y,x,"SW")
            total += 1
        
        if total >= 2:
            grandTotal += 1
            print(y,x,"HIT!")

print(grandTotal)