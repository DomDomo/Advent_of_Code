import re


def get_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    return lines


def digitify(data):
    return (
        data.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
    )


lines = get_lines("input.txt")

num_sum = 0

for line in lines:
    line = line.strip()
    line = digitify(line)

    n1 = re.search(r"\d", line).start()

    reversed = line[::-1]
    n2 = re.search(r"\d", reversed).start()

    num = int(line[n1] + reversed[n2])

    num_sum += num

print(num_sum)
