import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
nodes = [[1e10]*(n+1) for _ in range(n+1)]
for x in range(1, n+1):
    nodes[x][x] = 0
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a][b] = 1
for z in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if nodes[x][y] > nodes[x][z] + nodes[z][y]:
                nodes[x][y] = nodes[x][z] + nodes[z][y]
for i in range(1, n+1):
    res = 0
    for j in range(1, n+1):
        if nodes[i][j] >= 1e10 and nodes[j][i] >= 1e10:
            res += 1
    print(res)