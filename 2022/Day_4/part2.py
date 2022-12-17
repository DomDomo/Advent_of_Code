def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

partial_contain_pairs = 0

for line in lines:
    pair1, pair2 = line.strip().split(",")
    a1, a2 = pair1.split("-")
    b1, b2 = pair2.split("-")
    a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
    if len(set(range(a1, a2+1)) & set(range(b1, b2+1))) != 0:
        partial_contain_pairs += 1
    
print(partial_contain_pairs)

