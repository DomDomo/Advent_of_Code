import re


def get_lines(filename):
    with open(filename) as file:
        return file.readlines()


lines = get_lines("input.txt")

num_sum = 0

for line in lines:
    line = line.strip()

    n1 = re.search(r"\d", line).start()

    reversed = line[::-1]
    n2 = re.search(r"\d", reversed).start()

    num = int(line[n1] + reversed[n2])

    num_sum += num

print(num_sum)
