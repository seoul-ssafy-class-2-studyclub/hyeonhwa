import sys
input = lambda: sys.stdin.readline().rstrip()

v, e = map(int, input().split())
city = [[1e10]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    city[a][b] = min(c, city[a][b])
for z in range(1, v+1):
    for x in range(1, v+1):
        for y in range(1, v+1):
            if city[x][y] > city[x][z] + city[z][y]:
                city[x][y] = city[x][z] + city[z][y]
res = 1e10
for i in range(1, v+1):
    res = min(city[i][i], res)
if res == 1e10:
    res = -1
print(res)
