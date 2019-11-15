from copy import deepcopy
def leng(a, b, c, d):
    return abs(a - c) + abs(b - d)


def comb(arr, idx):
    if len(arr) == 3:
        castle.append(arr)
        return
    for i in range(idx+1, M):
        comb(arr+[i], i)


def removenemy(arr):
    ene = deepcopy(enemy)
    cnt = 0
    while ene:
        removes = []
        for i in range(3):
            l = []
            for x, y in ene:
                if leng(x, y, N, arr[i]) <= D:
                    l.append((x, y, leng(x, y, N, arr[i])))
            if l:
                l.sort(key=lambda x:(x[2], x[1]))
                removes.append(l[0])
        for n, m, d in removes:
            if [n, m] in ene:
                ene.remove([n, m])
                cnt += 1
        for i in range(len(ene)-1, -1, -1):
            ene[i][0] += 1
            if ene[i][0] == N:
                ene.pop(i)
    return cnt


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
castle = []
comb([], -1)
enemy = []
for i in range(N-1, -1, -1):
    for j in range(M):
        if board[i][j] == 1:
            enemy.append([i, j])
res = 0
for arrow in castle:
    cnt = removenemy(arrow)
    res = max(res, cnt)
print(res)
