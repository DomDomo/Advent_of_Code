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
    

  
hx, hy = 0, 0
tx, ty = 0, 0

prevMove = ""
visited = set()

for line in lines:
    move, step = line.split(" ")
    step = int(step)
 
    for _ in range(step):
        hx, hy = updateCords(hx, hy, move)
        
        if not headNearTail(hx, hy, tx, ty):
            tmpx, tmpy = updateCords(tx, ty, move)
            if not tailIsTouching(hx, hy, tmpx, tmpy):
                tx, ty = makeTailTouch(hx, hy, tx, ty)
            else:
                tx, ty = updateCords(tx, ty, move)

        visited.add((tx, ty))
        

    prevMove = move

print(len(visited))
        