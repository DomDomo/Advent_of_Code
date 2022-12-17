steps = []

with open("input.txt") as file:
    lines = file.readlines()
    steps = [line.rstrip() for line in lines]

## Part 1

horizontal = 0
depth = 0
for step in steps:
    move, num = step.split()
    num = int(num)
    if move == 'forward':
        horizontal += num
    if move == 'up':
        depth -= num
    if move == 'down':
        depth += num

print("Part 1")
print("Horizontal:", horizontal)
print("Depth:", depth)
print("Answer:", horizontal*depth)

## Part 2

horizontal = 0
depth = 0
aim = 0
for step in steps:
    move, num = step.split()
    num = int(num)
    if move == 'forward':
        horizontal += num
        depth += aim*num
    if move == 'up':
        aim -= num
    if move == 'down':
        aim += num

print("Part 2")
print("Horizontal:", horizontal)
print("Depth:", depth)
print("Answer:", horizontal*depth)
