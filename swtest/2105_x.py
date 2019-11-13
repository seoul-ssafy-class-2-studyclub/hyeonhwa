import sys
# sys.stdin = open('input8.txt', 'r')
def eat(i,j):
    global res
    start, end = i,j
    ate, k = [], 3
    while True:
        dx, dy = idx[k]
        x = i+dx
        y = j+dy
        if 0 <= x < p and 0 <= y < p:
            if not pos[x][y] in ate:
                i, j = x, y
                ate.append(pos[x][y])
                if x == start and y == end:
                    if res < len(ate):
                        res = len(ate)
                    return
            else:
                return
        elif y == -1:
            k = 0
        elif x == p:
            k = 2
        elif y == p:
            k = 1


for t in range(int(input())):
    N = int(input())
    dessert = [list(map(int,input().split())) for _ in range(N)]
    idx = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
    res = 0
    for p in range(N,2,-1):
        for q in range(N-p+1):
            for i in range(N-p+1):
                pos = [0]*p
                for j in range(p):
                    pos[j]=dessert[j+q][i:i+p]
                for y in range(1, p-1):
                    eat(0, y)
                    if res:
                        break
                if res:
                    break
            if res:
                break
        if res:
            break
    if res == 0:
        res = -1
    print('#{} {}'.format(t+1, res))