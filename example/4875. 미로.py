from pprint import pprint

def findend(x, y):
    stack = [x, y]
    while stack:
        x = stack.pop(0)
        y = stack.pop(0)
        for dx, dy in ix:
            if 0 <= x + dx < N and 0 <= y + dy < N and m[x+dx][y+dy] == 0:
                m[x+dx][y+dy] = -1
                stack.extend([x+dx, y+dy])
            if 0 <= x + dx < N and 0 <= y + dy < N and m[x+dx][y+dy] == 2:
                return 1
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    m = []
    ix = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for _ in range(N):
        m += [[int(i) for i in input()]]
    for i in range(len(m)):
        if 3 in m[i]:
            start_x = i
            start_y = m[i].index(3)

    print('#{} {}'.format(t+1, findend(start_x, start_y)))
    