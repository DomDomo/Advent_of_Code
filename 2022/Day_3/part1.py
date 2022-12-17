def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

priority_sum = 0

for line in lines:
    line = line.strip()
    half = len(line) // 2
    shared = list(set(line[:half]) & set(line[half:]))[0]
    if ord(shared) >= 97: 
        priority_sum += ord(shared) - 96
    else:
        priority_sum += ord(shared) - 38

print(priority_sum)