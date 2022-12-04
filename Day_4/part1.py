def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

def contains_within(x1, x2, y1, y2):
    return x1 <= y1 and x2 >= y2

full_contain_pairs = 0

for line in lines:
    line = line.strip()
    pair1, pair2 = line.split(",")
    a1, a2 = pair1.split("-")
    b1, b2 = pair2.split("-")
    a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
    if contains_within(a1, a2, b1, b2) or contains_within(b1, b2, a1, a2):
        full_contain_pairs += 1
    
print(full_contain_pairs)

