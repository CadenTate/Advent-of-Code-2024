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
enabled = True

indexMul = file.find("mul")
indexDo = file.find("do()")
indexDont = file.find("don't()")

while indexMul != -1:
    # print(file)
    # print(indexMul)
    # print(indexDo)
    # print(indexDont)
    if (indexDo != -1 and (indexDo < indexMul)) or (indexDont != -1 and (indexDont < indexMul)):
        if indexDo < indexDont or indexDont == -1:
            enabled = True
            file = file[indexDo+4:]
            # print("DO FOUND")
        else:
            enabled = False
            file = file[indexDont+7:]
            # print("DONT FOUND")
    else:
        coord = file[indexMul+3:]
        coord = isCoord(coord)
        if coord != None:
            if enabled:
                final += int(coord[0]) * int(coord[1])
            # print(f"MUL FOUND: {coord}")
            file = file[indexMul+len(coord[0]) + len(coord[1]) + 6:]
        else:
            file = file[indexMul+3:]

    indexMul = file.find("mul")
    indexDo = file.find("do()")
    indexDont = file.find("don't()")

print(final)