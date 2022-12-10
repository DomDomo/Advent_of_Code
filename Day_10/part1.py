def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

track = [num for num in range(20, 220+1, 40)]
print(track)
cycle_count = 0
reg = 1
sig_strength = 0

def checkStrength(n):
    for i in range(len(track)):
        if track[i] == n:
            print(n, reg)
            return n * reg
    return 0

for line in lines:
    line = line.strip()
    if line == "noop":
        cycle_count += 1
        sig_strength += checkStrength(cycle_count)
    else:
        ins, val = line.split(" ")
        cycle_count += 1
        sig_strength += checkStrength(cycle_count)
        cycle_count += 1
        sig_strength += checkStrength(cycle_count)
        reg += int(val)

print(sig_strength)
