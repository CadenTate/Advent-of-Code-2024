path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2024\Day 2\input.txt"

file = open(path, 'r').readlines()
file = [report.strip().split() for report in file]
file = [[int(level) for level in report] for report in file]

print(file)

def isIncreasing(report) -> bool:
    lastLevel = 0
    for level in report:
        if level <= lastLevel:
            return False
        lastLevel = level
    return True

def isDecreasing(report) -> bool:
    lastLevel = report[0] + 1
    for level in report:
        if level >= lastLevel:
            return False
        lastLevel = level
    return True

def adjacentRange(report) -> bool:
    lastLevel = report[0]
    for level in report:
        if abs(level - lastLevel) > 3:
            return False
        lastLevel = level
    return True

safeAmount = 0

for report in file:
    if (isIncreasing(report) or isDecreasing(report)) and adjacentRange(report):
        safeAmount += 1

    print(f"Increasing: {isIncreasing(report)}, Decreasing: {isDecreasing(report)}, Adjacent Range: {adjacentRange(report)}")

print(safeAmount)