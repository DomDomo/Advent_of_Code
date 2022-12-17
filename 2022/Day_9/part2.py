def get_lines(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]

lines = get_lines("input.txt")

allAround = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

plusAround = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
]

diagAround = [
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
]

def updateCords(x, y, m):
    if m == "R":
        x += 1
    elif m == "D":
        y -= 1
    elif m == "L":
        x -= 1
    elif m == "U":
        y += 1   

    return (x, y)

def headNearTail(hx, hy, tx, ty):
    aroundHead = [(hx+a[0], hy+a[1]) for a in allAround]
    return (tx, ty) in aroundHead

def tailIsTouching(hx, hy, tx, ty):
    plusTail = [(tx+a[0], ty+a[1]) for a in plusAround]
    return (hx, hy) in plusTail

def makeTailTouch(hx, hy, tx, ty):
    for a in diagAround:
        tmpx, tmpy = tx+a[0], ty+a[1]
        if tailIsTouching(hx, hy, tmpx, tmpy):
            return (tmpx, tmpy)
    
    # diagnal follow
    diag_x = hx-1 if tx < hx else hx+1
    diag_y = hy-1 if ty < hy else hy+1

    return (diag_x, diag_y)
    
def updateFollowCords(hx, hy, tx, ty):
    row_change = (hx - tx)
    col_change = (hy - ty)

    if abs(row_change) >= 2 and abs(col_change) >= 2:
        return makeTailTouch(hx, hy, tx, ty)
    elif abs(row_change) >= 2:
        return (hx - 1 if tx < hx else hx + 1, hy)
    elif abs(col_change) >= 2:
        return (hx, hy - 1 if ty < hy else hy + 1)
    else:
        return (tx, ty)

def updateTailCords(hx, hy, tx, ty, move):
    res_tx = tx
    res_ty = ty
    if not headNearTail(hx, hy, res_tx, res_ty):
        res_tx, res_ty = updateFollowCords(hx, hy, tx, ty)

    return (res_tx, res_ty)

hx, hy = 0, 0
t = [(0, 0) for i in range(9)]

visited = set()

for line in lines:
    move, step = line.split(" ")
    step = int(step)
 
    for _ in range(step):
        visited.add(t[8])
        hx, hy = updateCords(hx, hy, move)
        t[0] = updateTailCords(hx, hy, t[0][0], t[0][1], move)
        for i in range(1, 9):
            t[i] = updateTailCords(t[i-1][0], t[i-1][1], t[i][0], t[i][1], move)

        visited.add(t[8])
        
print(len(visited))
        