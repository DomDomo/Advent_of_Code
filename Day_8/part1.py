def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")
field = [line.strip() for line in lines]

def notBorder(field, row, col):
    return not (row == 0 or row == len(field)-1 or col == 0 or col == len(field[0])-1)

def allAbove(field, row, col):
    return [int(field[i][col]) for i in range(row)]

def allBelow(field, row, col):
    return [int(field[i][col]) for i in range(row+1, len(field))]

def allLeft(field, row, col):
    return [int(field[row][i]) for i in range(col)]

def allRight(field, row, col):
    return [int(field[row][i]) for i in range(col+1, len(field[0]))]

def isVisible(field, row, col):
    visible = [
        (int(field[row][col]) > max(allAbove(field, row, col))),
        (int(field[row][col]) > max(allBelow(field, row, col))),
        (int(field[row][col]) > max(allLeft(field, row, col))),
        (int(field[row][col]) > max(allRight(field, row, col))),
    ]

    return any(visible)

outer_ring = len(field) * 2 + len(field[0]) * 2 - 4
all_visible = outer_ring

for row in range(len(field)):
    for col in range(len(field[0])):
        if notBorder(field, row, col) and isVisible(field, row, col):
            all_visible += 1

print(all_visible)



