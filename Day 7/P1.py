with open(r"input.txt") as file:
    file = file.readlines()

file = [list(map(int, line.strip().replace(":", "").split(" "))) for line in file]

test = [[13, 5, 8],[80, 5, 8, 2]]

def solve(current, position, operation): #LEN 3 POS 2
    if position >= len(line):
        # print(current)
        if current == line[0]:
            global isValid
            isValid = True
        return
    match operation:
        case "+":
            current += line[position]
        case "*":
            current *= line[position]
        case "||":
            current = int(str(current) + str(line[position]))
    solve(current, position + 1, "+")
    solve(current, position + 1, "*")
    solve(current, position + 1, "||")

total = 0

for line in file:
    isValid = False
    solve(line[1],2,"+")
    if isValid:
        total += line[0]
        continue
    solve(line[1],2, "*")
    if isValid:
        total += line[0]
        continue
    solve(line[1], 2, "||")
    if isValid:
        total += line[0]
        continue

print(total)