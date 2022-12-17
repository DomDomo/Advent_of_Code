lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


fish = lines[0].split(",")
#fish = [str(f) for f in [3,4,3,1,2]]

fishes = {}
for i in range(0, 9):
    fishes[i] = fish.count(str(i))

print(fishes)



def grow_up(fishes):
    grown_fish = {}
    values = list(fishes.values())
    zeros = values.pop(0)
    values[6] += zeros
    values.append(zeros)
    for i in range(0, 9):
        grown_fish[i] = values[i]

    return grown_fish

# Part 1
def part_1(fishes):
    for day in range(80):
        fishes = grow_up(fishes)
        #print(fishes)

    sum_of_fish = sum(fishes.values())
    print(sum_of_fish)


# Part 2
def part_2(fishes):
    for day in range(256):
        fishes = grow_up(fishes)
        #print(fishes)

    sum_of_fish = sum(fishes.values())
    print(sum_of_fish)

part_1(fishes)
part_2(fishes)