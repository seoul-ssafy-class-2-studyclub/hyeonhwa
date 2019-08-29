def findroad(start_x, start_y, cnt=0):
    queue = [start_x, start_y]
    while queue:
        x = queue.pop(0)
        y = queue.pop(0)
        for dx, dy in idx:
            if 0 <= x+dx < N and 0 <= y+dy < N and m[x+dx][y+dy] == 0:
                m[x+dx][y+dy] = -1
                res = findroad(x+dx, y+dy, cnt+1)
            if 0 <= x+dx < N and 0 <= y+dy < N and m[x+dx][y+dy] == 2:
                k.append(cnt)


T = int(input())
for t in range(T):
    N = int(input())
    idx = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    m = [list(map(int, [i for i in input()])) for _ in range(N)]
    k = []
    for i in m:
        if 3 in i:
            start_x = m.index(i)
            start_y = i.index(3)
            break
    findroad(start_x, start_y)
    if not k:
        print('#{} 0'.format(t+1))
    else:
        print('#{} {}'.format(t+1,min(k)))