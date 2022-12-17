import collections

heightmap = []

with open("input.txt") as file:
    lines = file.readlines()
    heightmap = [line.rstrip() for line in lines]

# Part 1

lows = []

def add_a_low(height, around):
    around = [int(num) for num in around]
    if height < min(around):
        lows.append(height)

for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        is_first_row = (x == 0)
        is_first_char = (y == 0)
        is_last_row = (x == len(heightmap)-1)
        is_last_char = (y == len(heightmap[x])-1)
        height = int(heightmap[x][y])
        if not is_first_row and not is_first_char and not is_last_row and not is_last_char:
            around = [heightmap[x-1][y], heightmap[x][y-1], heightmap[x+1][y], heightmap[x][y+1]]
            add_a_low(height, around)
        if is_first_row:
            if is_first_char:
                around = [heightmap[x+1][y], heightmap[x][y+1]]
                add_a_low(height, around)
            if is_last_char:
                around = [heightmap[x][y-1], heightmap[x+1][y]]
                add_a_low(height, around)
            if not is_first_char and not is_last_char:
                around = [heightmap[x][y-1], heightmap[x+1][y], heightmap[x][y+1]]
                add_a_low(height, around)
        if is_last_row:
            if is_first_char:
                around = [heightmap[x-1][y], heightmap[x][y+1]]
                add_a_low(height, around)
            if is_last_char:
                around = [heightmap[x][y-1], heightmap[x-1][y]]
                add_a_low(height, around)
            if not is_first_char and not is_last_char:
                around = [heightmap[x][y-1], heightmap[x-1][y], heightmap[x][y+1]]
                add_a_low(height, around)
        if is_first_char:
            if not is_first_row and not is_last_row:
                around = [heightmap[x+1][y], heightmap[x][y+1], heightmap[x-1][y]]
                add_a_low(height, around)
        if is_last_char:
            if not is_first_row and not is_last_row:
                around = [heightmap[x+1][y], heightmap[x][y-1], heightmap[x-1][y]]
                add_a_low(height, around)

answer = sum([low+1 for low in lows])
print(answer)

# Part 2

for x in range(len(heightmap)):
    row = ["0" if num == "9" else "1" for num in heightmap[x]]
    row = "".join(row)
    heightmap[x] = row

textfile = open("display.txt", "w")
for element in heightmap:
    textfile.write(" ".join(str(x) for x in element))
    textfile.write("\n")
textfile.close()

for row in heightmap:
    print(row)
rows = len(heightmap)
columns = len(heightmap[0])
visited = set()
basin_num = 0

basins = []

def bfs(r, c):
    q = collections.deque()
    visited.add((r, c))
    q.append((r, c))
    size = 1
    while q:
        x, y = q.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dx, dy in directions:
            hx = x + dx
            hy = y + dy
            conditions = [
                hx in range(rows),
                hy in range(columns),
                (hx, hy) not in visited
            ]
            if all(conditions) and heightmap[hx][hy] == "1":
                q.append((hx, hy))
                visited.add((hx, hy))
                size += 1
            
    basins.append(size)

for x in range(rows):
    for y in range(columns):
        if heightmap[x][y] == "1" and (x, y) not in visited:
            bfs(x, y)
            basin_num += 1

basins = sorted(basins)[::-1]
answer = basins[0] * basins[1] * basins[2]

print("Basin_num: ", basin_num)
print("Basins: ", basins)
print("Answer: ", answer)







