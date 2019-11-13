def divide(x, y):
    center = (x, y)
    k = 0
    while True:
        dx, dy = idx[k]
        i = x+dx
        j = y+dy


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
idx = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
for x in range(N, 2, -1):
    for y in range(N-x+1):
        for i in range(N-x+1):
            pos = [0]*x
            for j in range(x):
                pos[j] = city[j+x][i:i+y]
            for m in range(1, x-1):
                vote5 = divide(0, m)
