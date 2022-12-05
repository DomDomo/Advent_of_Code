def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

stack_info = []
break_point = 0

# Get each all stack info
for i, line in enumerate(lines):
    parts = [line[i:i+4] for i in range(0, len(line), 4)]
    parts = [part.strip() for part in parts]
    stack_info.append(parts)
    if stack_info[-1][0] == '1':
        break_point = i+2
        break


# Make stack dictionary
stack_info = stack_info[::-1]
stacks = {}

for stack_num in stack_info[0]:
    stacks[stack_num] = []

for crate_level in stack_info[1:]:
    for stack in stacks:
        crate = crate_level[int(stack)-1]
        if crate != '':
            stacks[stack].append(crate[1:-1])
    

# Rearrange stacks
moves = lines[break_point:]
for move in moves:
    mn = [num for num in move.rstrip().split(' ') if num.isdigit()]
    # mn: How many; From -> To
    to_move = []
    for _ in range(int(mn[0])):
        to_move.append(stacks[mn[1]].pop())

    stacks[mn[2]] = stacks[mn[2]] + to_move[::-1]
    
    
for stack in stacks:
    print(stacks[stack][-1], end="")




