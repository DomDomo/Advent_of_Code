from collections import defaultdict

def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")
threshold = 100000

system = defaultdict(int)
directory = [] 

for line in lines:
    command = line.rstrip().split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                directory.pop()
            else:
                directory.append(command[2])
    else:
        if command[0] != "dir":
            size = int(command[0])
            for i in range(len(directory)):
                system["/".join(directory[:i+1])] += size

final_size = 0
for key in system:
    if system[key] <= threshold:
        final_size += system[key]

print(final_size)
