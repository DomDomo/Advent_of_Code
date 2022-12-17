lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

coords = []

class Vent:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

for line in lines:
    allxys = line.split(" -> ")
    x1, y1 = map(int, allxys[0].split(","))
    x2, y2 = map(int, allxys[1].split(","))

    coords.append(Vent(x1, y1, x2, y2))

floor = []

for line in range(1000):
    zeros = [0 for i in range(1000)]
    floor.append(zeros)

# for coord in coords:
#     print(coord.x1, coord.y1, coord.x2, coord.y2)

for coord in coords:
    if coord.x1 == coord.x2:
        start = min(coord.y1, coord.y2)
        end = max(coord.y1, coord.y2)
        for i in range(start, end+1):
            floor[i][coord.x1] += 1

    if coord.y1 == coord.y2:
        start = min(coord.x1, coord.x2)
        end = max(coord.x1, coord.x2)
        for i in range(start, end+1):
            floor[coord.y1][i] += 1


    if abs(coord.x1 - coord.x2) == abs(coord.y1 - coord.y2):
        side = abs(coord.x1 - coord.x2)
        m = (coord.y2 - coord.y1) / (coord.x2 - coord.x1)
        top, bottom = [coord.x1, coord.y1], [coord.x2, coord.y2]
        if coord.y2 < coord.y1:
            top, bottom = bottom, top
        
        print(coord.x1, coord.y1, coord.x2, coord.y2, "m: ", m, "side: ", side )
        print(top[1], top[0], bottom[1], bottom[0])
        for i in range(side+1):
            if m > 0:
                floor[top[1]+i][top[0]+i] += 1
            elif m < 0:
                floor[top[1]+i][top[0]-i] += 1

        


print("Length: ", len(coords))

danger = 0
for line in floor:
    for spot in line:
        if spot >= 2:
            danger += 1

print(danger)

textfile = open("a_file.txt", "w")
for element in floor:
    textfile.write(" ".join(str(x) for x in element))
    textfile.write("\n")
textfile.close()

    