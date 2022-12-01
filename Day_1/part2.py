def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

elf_cals = []
temp_cals = 0

for line in lines:
    if line == '\n':
        elf_cals.append(temp_cals)
        temp_cals = 0
    else:
        temp_cals += int(line)

elf_cals.sort(reverse=True)
result = sum(elf_cals[:3])

print(result)

