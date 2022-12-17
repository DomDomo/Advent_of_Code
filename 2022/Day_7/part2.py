from collections import defaultdict

def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

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

unused = 70000000 - system["/"]
needed = 30000000 - unused

to_delete = system["/"]

for key in system:
    if system[key] > needed:
        to_delete = min(to_delete, system[key])

print(to_delete)
