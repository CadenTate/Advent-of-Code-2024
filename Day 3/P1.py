from typing import List

path = r"C:\Users\Caden\Desktop\Code\Advent-of-Code-2024\Day 3\input.txt"

preEdit = open(path, "r").readlines()
file = ""

for line in preEdit:
    file += line


# Determines if the section of text after the mul is a valid coordinate or not
def isCoord(coord:str) -> List[int] | None:
    coords = ["",""]
    if coord[0] != '(':
        return None
    coord = coord[1:]
    while coord[0] != ',':
        try:
            int(coord[0])
            coords[0] += coord[0]
            coord = coord[1:]
        except:
            return None
    coord = coord[1:]
    while coord[0] != ')':
        try:
            int(coord[0])
            coords[1] += coord[0]
            coord = coord[1:]
        except:
            return None
        
    return coords

# ____MAIN____

final = 0

index = file.find("mul")
while index != -1:
    coord = file[index+3:]
    coord = isCoord(coord)
    if coord != None:
        final += int(coord[0]) * int(coord[1])
        file = file[index+len(coord[0]) + len(coord[1]) + 3:]
    else:
        file = file[index+1:]

    index = file.find("mul")

print(final)