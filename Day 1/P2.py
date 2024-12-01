# Opening File
path = r'C:\Users\Caden\Desktop\Code\Advent-of-Code-2024\Day 1\input.txt'

file = open(path, 'r').readlines()

# Format Data into TWO seperate Lists
list1 = []
list2 = []

for id in file:
    id = id.split()
    list1.append(int(id[0]))
    list2.append(int(id[1]))

# Process Data
sum = 0

for id in list1:
    count = list2.count(id)
    sum += id * count

print(sum)