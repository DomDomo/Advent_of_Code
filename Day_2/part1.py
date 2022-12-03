def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

rps_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

a_to_z = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

wins = [
    ("Z", "X"),
    ("X", "Y"),
    ("Y", "Z")
]

total_score = 0

for line in lines:
    op, me = line.strip().split(" ")
    total_score += rps_score[me]
    if (a_to_z[op], me) in wins:
        total_score += 6
    elif a_to_z[op] == me:
        total_score += 3
    
print(total_score)