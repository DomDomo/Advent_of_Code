def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")
lines = [line.strip() for line in lines]

priority_sum = 0

for i in range(0, len(lines), 3):
    badge = list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))[0]
    if ord(badge) >= 97: 
        priority_sum += ord(badge) - 96
    else:
        priority_sum += ord(badge) - 38

print(priority_sum)

