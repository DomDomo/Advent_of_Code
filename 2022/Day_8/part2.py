import math

def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")
field = [line.strip() for line in lines]

def notBorder(field, row, col):
    return not (row == 0 or row == len(field)-1 or col == 0 or col == len(field[0])-1)

def allAbove(field, row, col):
    return [int(field[i][col]) for i in range(row)][::-1]

def allBelow(field, row, col):
    return [int(field[i][col]) for i in range(row+1, len(field))]

def allLeft(field, row, col):
    return [int(field[row][i]) for i in range(col)][::-1]

def allRight(field, row, col):
    return [int(field[row][i]) for i in range(col+1, len(field[0]))]

def spotScore(field, row, col):
    spot = int(field[row][col])
    scores = []

    score = 0
    for num in allAbove(field, row, col):
        score += 1
        if num >= spot: break
    scores.append(score)

    score = 0
    for num in allRight(field, row, col):
        score += 1
        if num >= spot: break
    scores.append(score)

    score = 0
    for num in allBelow(field, row, col):
        score += 1
        if num >= spot: break
    scores.append(score)

    score = 0
    for num in allLeft(field, row, col):
        score += 1
        if num >= spot: break
    scores.append(score)
    
    return math.prod(scores)

scenic_score = 0

for row in range(len(field)):
    for col in range(len(field[0])):
        if notBorder(field, row, col):
            scenic_score = max(scenic_score, spotScore(field, row, col))
            
print(scenic_score)



