lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

template = lines[0]
rules = {}

keys = set()

for line in lines[2:]:
    a, b = line.split(" -> ")
    keys.add(a[0])
    keys.add(a[1])
    keys.add(b)
    rules[a] = b

def starting_pairs(polymer, nums):
    
    i = 0
    pairs = []
    for _ in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        pairs.append(pair)
        i += 1

    for pair in pairs:
        nums[pair] += 1

    return nums

def grow_polymer(polymer, count):
    
    new_polymer = {pair: 0 for pair in rules.keys()}
    new_count = count.copy()

    for pair in polymer.keys():
        letts = []
        for new_pair in mutations[pair]:
            letts.append(new_pair)
            new_polymer[new_pair] += polymer[pair]

        new_count[letts[0][1]] += polymer[pair]

    return (new_polymer, new_count)


mutations = {pair: [pair[0]+rules[pair], rules[pair]+pair[1]] for pair in rules.keys()}
empty_pairs = {pair: 0 for pair in rules.keys()}

pair_nums = starting_pairs(template, empty_pairs)
main_count = {let: 0 for let in keys}

for let in template:
    main_count[let] += 1


for step in range(40):
    print(step)
    pair_nums, main_count = grow_polymer(pair_nums, main_count)

print(main_count) 


values = main_count.values()
high = max(values)
low = min(values)
print(high - low)
