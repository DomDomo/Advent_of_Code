depths = []

with open("input.txt") as file:
    lines = file.readlines()
    depths = [int(line.rstrip()) for line in lines]


def higher_mes(depths):
    previous = depths[0]
    high_measurements = 0

    for depth in depths:
        if depth > previous:
            high_measurements += 1
        previous = depth

    return high_measurements

print("Depths: ", len(depths))

print("Higher_1: ", higher_mes(depths))

depths3 = [sum(depths[i:i+3]) for i in range(2000) if len(depths[i:i+3]) == 3]
print("Higher_2: ", higher_mes(depths3))


