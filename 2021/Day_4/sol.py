lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = lines[0].split(',')

boards = []

nums = list(filter(lambda line: line != '', lines))[1:]
board_num = int(len(nums) / 5)
i = 0
for b in range(board_num):
    boards.append(nums[i:i+5])
    i += 5

def string_to_num_boards(boards):
    for board in range(len(boards)):
        for line in range(len(boards[board])):
            better_list = boards[board][line].strip().split(" ")
            better_list = list(filter(lambda line: line != '', better_list))
            boards[board][line] = better_list

def update_boards(boards, target):
    for board in range(len(boards)):
        for line in range(len(boards[board])):
            boards[board][line] = ['-' if num == target else num for num in boards[board][line]]

def check_win(boards):
    for board in range(len(boards)):
        has_won = check_board_win(boards[board])
        if has_won:
            return board

def check_board_win(board):
    has_won = False
    won_line = ['-' for i in range(5)]
    for row in board:
        if row == won_line:
            has_won = True
    for i in range(len(board)):
        column = [line[i] for line in board]
        if column == won_line:
            has_won = True

    return has_won


def count_non_win_nums(board):
    board_sum = 0
    for line in board:
        line = list(filter(lambda num: num != '-', line))
        line = [int(x) for x in line]
        board_sum += sum(line)

    return board_sum

string_to_num_boards(boards)

# Part 1

# for target in numbers:
#     update_boards(boards, target)
#     won_num = check_win(boards)
#     if won_num:
#         dash_sum = count_non_win_nums(boards[won_num])
#         print(dash_sum * int(target))
#         break

# Part 2

def check_wins(boards):
    indexes = []
    for board in range(len(boards)):
        has_won = check_board_win(boards[board])
        if has_won:
            indexes.append(board)
    return [boards[b] for b in range(len(boards)) if b not in indexes]

previous_boards = boards
for target in numbers:
    update_boards(boards, target)
    previous_boards = boards
    boards = check_wins(boards)
    if len(boards) == 0:
        dash_sum = count_non_win_nums(previous_boards[0])
        print(dash_sum * int(target))
        for line in previous_boards[0]:
            print(line)
        break




    