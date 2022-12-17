def get_lines(filename):
    with open(filename) as file:
        return file.readlines()

lines = get_lines("input.txt")

cycle_count = 0
reg = 1

sprite = [0, 1, 2]
pos = 0
draw_board = []

def draw_to_board(pos):
    if pos in sprite:
        draw_board.append("#")
    else:
        draw_board.append(".")

    pos += 1
    return pos if pos < 40 else 0

for line in lines:
    line = line.strip()
    if line == "noop":
        cycle_count += 1
        pos = draw_to_board(pos)
    else:
        ins, val = line.split(" ")
        cycle_count += 1
        pos = draw_to_board(pos)
        cycle_count += 1
        pos = draw_to_board(pos)
        reg += int(val)
        for i in range(len(sprite)):
            sprite[i] += int(val)

for i in range(6):
    display ="".join(draw_board[i*40:40+i*40])
    print(display)
