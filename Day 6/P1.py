from MapV1 import Map

path = r"inputP1.txt"

with open(path) as file:
    inputMap = Map(file.readlines())

isInMap = True
while isInMap:
    # inputMap.printMap()
    # input()
    match inputMap.getGuardDirection():
        case "^":
            isInMap = inputMap.moveGuardUp()
        case "v":
            isInMap = inputMap.moveGuardDown()
        case "<":
            isInMap = inputMap.moveGuardLeft()
        case ">":
            isInMap = inputMap.moveGuardRight()

print(inputMap)
print(inputMap.map.count("X"))