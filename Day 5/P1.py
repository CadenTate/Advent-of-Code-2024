import math

path = r"input.txt"

with open(path) as file:
    lines = file.readlines()

    # Data Clean Up
    orderKey = {}
    for i in lines[:lines.index("\n")]:
        i = i.strip().split("|")
        if int(i[0]) in orderKey.keys():
            orderList = orderKey[int(i[0])]
            orderList.append(int(i[1]))
            orderKey[int(i[0])] = orderList
        else:
            orderKey[int(i[0])] = [int(i[1])]
    data = []
    for i in lines[lines.index("\n") + 1:]:
        i = i.strip().split(",")
        data.append([int(num) for num in i])

    # Logic
    sum = 0

    for line in data:
        isValid = True
        for num in line:
            if num in orderKey:
                for order in orderKey[num]:
                    if order in line and line.index(num) > line.index(order):
                        isValid = False
        if isValid: sum += line[math.floor(len(line) / 2)]

    print(sum)



