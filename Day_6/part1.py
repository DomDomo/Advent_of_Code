with open('input.txt', 'r') as f:
    read_num = 0
    queue = []
    
    for i in range(3):
        queue.append(f.read(1))
        read_num += 1

    c = f.read(1)
    while c:
        queue.append(c)
        read_num += 1

        if len(set(queue))== 4: break

        queue.pop(0)

        c = f.read(1)

    print(read_num)