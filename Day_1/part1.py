def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

max_cals = 0
temp_cals = 0

for line in lines:
    if line == '\n':
        max_cals = max(max_cals, temp_cals)
        temp_cals = 0
    else:
        temp_cals += int(line)

print(max_cals)

