path = r"C:\Users\Intern\Desktop\Advent-of-Code-2024\Day 4\input.txt"

rawFile = open(path, 'r').readlines()

size = len(rawFile)

file = ""

for line in rawFile:
    file += line.strip()

# Functions checking forwards and backwards
def checkForwards(i:int) -> bool:
    if i > size*size - 4:
        return False
    if file[i+1] != 'M':
        return False
    if file[i+2] != 'A':
        return False
    if file[i+3] != 'S':
        return False
    return True

def checkBackwards(i:int) -> bool:
    if i < 4:
        return False
    if file[i-1] != 'M':
        return False
    if file[i-2] != 'A':
        return False
    if file[i-3] != 'S':
        return False
    return True

# Functions checking up and down
def checkUp(i:int) -> bool:
    if i < size*size - size*(size-3):
        return False
    if file[i-size*1] != 'M':
        return False
    if file[i-size*2] != 'A':
        return False
    if file[i-size*3] != 'S':
        return False
    return True

def checkDown(i:int) -> bool:
    if i >= size*size - size*(size-3):
        return False
    if file[i+size*1] != 'M':
        return False
    if file[i+size*2] != 'A':
        return False
    if file[i+size*3] != 'S':
        return False
    return True

# Functions for checking angles
def checkNE(i:int) -> bool:
    if i < (size * 3) + 3:
        return False
    if file[i+size*1-1] != 'M':
        return False
    if file[i+size*2-2] != 'A':
        return False
    if file[i+size*3-3] != 'S':
        return False
    return True
        

# Wrapper Functions
def checkHorizontal(i:int) -> bool:
    return checkForwards(i) or checkBackwards(i)

def checkVertical(i:int) -> bool:
    return checkUp(i) or checkDown(i)

def checkAngles(i:int) -> bool:
    return checkNE(i)

total = 0

for i in range(len(file)):
    # print(i,file[i])
    # check if start
    if file[i] != 'X':
        continue

    if checkHorizontal(i):
        # print(i,"H")
        total += 1
    if checkVertical(i):
        # print(i,"V")
        total += 1
    if checkAngles(i):
        total += 1
        continue

print(total)