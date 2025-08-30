import time

from MapV2 import Map

path = r"input.txt"

with open(path) as file:
    inputMap = Map(file.readlines())

# Set initial path
isInMap = True
packet = []

guardStartIndex = inputMap.getGuardLoc()
guardStartRotation = inputMap.getGuardRotation()
while isInMap:
    # print(inputMap)
    # input()
    match inputMap.getGuardRotation():
        case "^":
            packet = inputMap.moveGuardUp()
        case "v":
            packet = inputMap.moveGuardDown()
        case "<":
            packet = inputMap.moveGuardLeft()
        case ">":
            packet = inputMap.moveGuardRight()

    isInMap = packet[0]
inputMap.map[guardStartIndex] = guardStartRotation
walkedIndex = inputMap.walkedIndexes.copy()
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
    packet = []

    while isInMap:
        match inputMap.getGuardRotation():
            case "^":
                packet = inputMap.moveGuardUp()
            case "v":
                packet = inputMap.moveGuardDown()
            case "<":
                packet = inputMap.moveGuardLeft()
            case ">":
                packet = inputMap.moveGuardRight()
        isInMap = packet[0]

        if len(packet) > 1:
            if packet[1] in hitSpots:
                total += 1
                # print(Coordinate.indexToCoordinates(f, inputMap.width))
                break
            else:
                hitSpots.append(packet[1])


    iterations += 1
    print(f"COMPLETION PERCENT: {round(iterations/len(walkedIndex) * 100,2)}%")
    # print("TIME TAKEN:",time.time()-startTime)

print(total)