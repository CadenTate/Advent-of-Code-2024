path = r'C:\Users\Caden\Desktop\Code\Advent-of-Code-2024\Day 1\input.txt'

file = open(path, 'r').readlines()

list1 = []
list2 = []

for id in file:
    id = id.split()
    list1.append(int(id[0]))
    list2.append(int(id[1]))

list1.sort()
list2.sort()

sum = 0

for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

print(sum)