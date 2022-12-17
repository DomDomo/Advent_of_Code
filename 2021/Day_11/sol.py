lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def gird_from_file():
    grid = []
    for line in lines:
        grid.append([int(energy) for energy in line])
    return grid

grid = gird_from_file()

rows = len(grid)
cols = len(grid[0])

directions = [
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1]
]

def increase_energy(grid):
    for line in range(len(grid)):
        grid[line] = [num + 1 for num in grid[line]]

def activate_flash(x, y):
    grid[x][y] = 0
    for dx, dy in directions:
        hx = x + dx
        hy = y + dy
        conditions = [
            hx in range(rows),
            hy in range(cols),
        ]

        if all(conditions):
            grid[hx][hy] += 1

def print_grid(grid):
    print("--------------")
    for line in grid:
        print(line)

def null_flashed(grid, flashed):
    for fx, fy in flashed:
        grid[fx][fy] = 0

def has_charged_octopi(grid):
    all_octopi = [num for line in grid for num in line]
    return any([num >= 10 for num in all_octopi])

def mega_flash():
    mega = []
    line = [0] * cols
    for row in range(rows):
        mega.append(line)

    return mega

def run_flashes(step_num):
    all_flashes = 0
    for step in range(step_num):
        increase_energy(grid)
        flashed = set()
        while has_charged_octopi(grid):
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] >= 10:
                        flashed.add((r, c))
                        activate_flash(r, c)
        all_flashes += len(flashed)
        null_flashed(grid, flashed)
        if grid == mega_flash():
            print("Step:", step + 1)
            break

    return all_flashes

print("Part 1")
print("Flashes:", run_flashes(100))
grid = gird_from_file()
print("Part 2")
print("Flashes:", run_flashes(1000))
