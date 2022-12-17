lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


#positions = [16,1,2,0,4,2,7,1,2,14]
positions = [int(pos) for pos in lines[0].split(",")]
print(positions)

positions.sort()
print(positions)

def move_to_fuel(moves):
    fuel = 0
    for i in range(1, moves+1):
        fuel += i
    return fuel

def part_1(positions):
    fuels = []
    for i in range(positions[0], positions[-1]+1):
        all_fuel = 0
        for pos in positions:
            all_fuel += abs(pos-i)
        fuels.append(all_fuel)

    return min(fuels)

print(part_1(positions))
print("--------------------------")
def part_2(positions):
    start = positions[0]
    end = positions[-1]+1
    fuels = []
    for i in range(start, end):
        all_fuel = 0
        for pos in positions:
            all_fuel += move_to_fuel(abs(pos-i))
        if not (not fuels or all_fuel < fuels[-1]):
            break
        fuels.append(all_fuel)

    return min(fuels)

print(part_2(positions))