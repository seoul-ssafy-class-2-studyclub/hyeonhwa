import collections
def spring(x, y):
    global flag2
    energy = 0
    for n in range(len(trees[x][y])-1, 0, -1):
        if trees[x][y][n] != 0:
            if trees[x][y][n] <= trees[x][y][0]:
                trees[x][y][0] -= trees[x][y][n]
                trees[x][y][n] += 1
                if trees[x][y][n] % 5 == 0:
                    flag2.append((x, y))
            else:
                energy += trees[x][y].pop(n)//2
    trees[x][y][0] += energy
                

def autumn(x, y):
    for dx, dy in idx:
        if 0 <= x+dx < N and 0 <= y+dy < N:
            trees[x+dx][y+dy].append(1)


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[[5] for _ in range(N)] for __ in range(N)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
k = 1
while k <= K:
    res = 0
    flag2 = collections.deque()
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) > 1:
                spring(i, j)
    if flag2:
        for n, m in flag2:
            autumn(n, m)
    for i in range(N):
        for j in range(N):
            trees[i][j][0] += A[i][j]
            res += len(trees[i][j]) - 1
    k += 1
print(res)
