import time

from MapV2 import Map

path = r"input.txt"

with open(path) as file:
    inputMap = Map(file.readlines())

# Set initial path
isInMap = True

guardStartIndex = inputMap.getGuardLoc()
guardStartRotation = inputMap.getGuardRotation()
while isInMap:
    match inputMap.getGuardRotation():
        case "^":
            isInMap = inputMap.moveGuardUp()
        case "v":
            isInMap = inputMap.moveGuardDown()
        case "<":
            isInMap = inputMap.moveGuardLeft()
        case ">":
            isInMap = inputMap.moveGuardRight()

inputMap.map[guardStartIndex] = guardStartRotation
walkedIndex = inputMap.walkedIndexes.copy()
walkedIndex.pop(walkedIndex.index(guardStartIndex))
print("SET UP DONE")
# inputMap.printWithWalked()

total = 0
iterations = 0

for f in walkedIndex:
    inputMap.resetGuardLocation()
    hitSpots = []
    startTime = time.time()

    # Map Setup
    inputMap.barrierIndex = f

    isInMap = True

    while isInMap:
        # inputMap.printWithFormatting()
        # input()
        match inputMap.getGuardRotation():
            case "^":
                isInMap = inputMap.moveGuardUp()
            case "v":
                isInMap = inputMap.moveGuardDown()
            case "<":
                isInMap = inputMap.moveGuardLeft()
            case ">":
                isInMap = inputMap.moveGuardRight()

        state = (inputMap.getGuardLoc(), inputMap.getGuardRotation())
        if state in hitSpots:
            total += 1
            # print(Coordinate.indexToCoordinates(f, inputMap.width))
            break
        else:
            hitSpots.append(state)


    iterations += 1
    print(f"COMPLETION PERCENT: {round(iterations/len(walkedIndex) * 100,2)}%")
    # print("TIME TAKEN:",time.time()-startTime)

print(total)