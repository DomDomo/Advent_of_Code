lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

starts = [b for b in brackets.keys()]
pairs = ["()", "[]", "{}", "<>"]

illegals = []

def all_starts(line):
    for char in line:
        if char not in starts:
            return False
    return True

def remove_starts(line):
    new_line = []
    for char in line:
        if char not in starts:
            new_line.append(char)
    
    return "".join(new_line)

def part_1():
    for line in lines:
        while any(map(line.__contains__, pairs)):
            for pair in pairs:
                line = line.replace(pair, '')

        just_mising = all_starts(set(line))
        if not just_mising:
            illegal = remove_starts(line)[0]
            illegals.append(illegal)

    points = 0
    for char in illegals:
        points += scores[char]
    print(points)

#part_1()

# Part 2

autocomplete_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

fixed = []
corrupted = []
for line in lines:
    while any(map(line.__contains__, pairs)):
        for pair in pairs:
            line = line.replace(pair, '')

    fixed.append(line)
    just_mising = all_starts(set(line))
    if not just_mising:
        corrupted.append(line)

incompletes = [incomplete for incomplete in fixed if incomplete not in corrupted]

finishes = []
for incomplete in incompletes:
    to_finish = []
    for char in incomplete[::-1]:
        to_finish.append(brackets[char])
    finishes.append("".join(to_finish))

scores = []
for finish in finishes:
    points = 0
    for char in finish:
        points = points * 5 + autocomplete_scores[char]

    scores.append(points)

scores = sorted(scores)
middle = int(len(scores) / 2)
print(scores[middle])
