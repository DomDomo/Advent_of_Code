lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

outputs = [line.split("|")[1].strip() for line in lines]

num_to_segments = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

segments_to_num = {segment: num for num, segment in num_to_segments.items()}

unique = [
    num_to_segments[1],
    num_to_segments[4],
    num_to_segments[7],
    num_to_segments[8],
]

def part_1():
    unique_sum = 0 
    for output in outputs:
        for number in output.split(" "):
            if len(number) in unique:
                unique_sum += 1

    return unique_sum

print(part_1())

def update_num_to_code(code_to_num):
    return {num: code for code, num in code_to_num.items()}

def has_values(check_code, code):
    it_does = True
    for char in code:
        if char not in check_code:
            return False

    return it_does

def get_code_map(line):

    code_to_num = {}
    num_to_code = {}

    # Split evertying before and after the |
    all_nums, output = [section.strip().split(" ") for section in line.split("|")]
    all_nums = [''.join(sorted(num)) for num in all_nums]
    # Add all unique codes (1, 4, 7, 8)
    for num in all_nums:
        if len(num) in unique:
            code_to_num[num] = segments_to_num[len(num)]
    num_to_code = update_num_to_code(code_to_num)
    # Add code for 6
    for num in all_nums:
        if len(num) == 6 and not has_values(num, num_to_code[1]):
            code_to_num[num] = 6
    num_to_code = update_num_to_code(code_to_num)
    # Add code for 9
    for num in all_nums:
        if len(num) == 6 and has_values(num, num_to_code[4]):
            code_to_num[num] = 9
    num_to_code = update_num_to_code(code_to_num)
    # Add code for 0
    all_nums = [code for code in all_nums if code not in code_to_num.keys()]
    for num in all_nums:
        if len(num) == 6:
            code_to_num[num] = 0
    num_to_code = update_num_to_code(code_to_num)
    # Add code for 3
    for num in all_nums:
        if len(num) == 5 and has_values(num, num_to_code[7]):
            code_to_num[num] = 3
    num_to_code = update_num_to_code(code_to_num)
    # Add code for 5
    for num in all_nums:
        if has_values(num_to_code[6], num):
            code_to_num[num] = 5
    # Add code for 2
    all_nums = [code for code in all_nums if code not in code_to_num.keys()]
    code_to_num[all_nums[0]] = 2

    num_to_code = update_num_to_code(code_to_num)

    return (code_to_num, output)

def part_2():
    sum_of_values = 0
    for line in lines:
        code_map, output = get_code_map(line)
        output = [''.join(sorted(num)) for num in output]
        digits = [str(code_map[code]) for code in output]
        value = int(''.join(digits))
        sum_of_values += value

    return sum_of_values

print(part_2())
