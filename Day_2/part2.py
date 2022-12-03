def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

rps_score = {
    "A": 1,
    "B": 2,
    "C": 3
}

outcome_score = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

win_conversion = {
    "A": "B",
    "B": "C",
    "C": "A",
}

lose_conversion = {
    "A": "C",
    "B": "A",
    "C": "B",
}

total_score = 0

for line in lines:
    op, me = line.strip().split(" ")
    total_score += outcome_score[me]
    if me == "Y":
        total_score += rps_score[op]
    elif me == "Z":
        total_score += rps_score[win_conversion[op]]
    else:
        total_score += rps_score[lose_conversion[op]]


print(total_score)